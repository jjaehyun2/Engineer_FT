CLASS cl_abapgit_res_repo_stage DEFINITION
  PUBLIC
  INHERITING FROM cl_adt_rest_resource
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.

    TYPES:
      BEGIN OF ty_abapgit_file,
        filename    TYPE string,
        path        TYPE string,
        localstate  TYPE char1,
        remotestate TYPE char1,
        atom_links  TYPE if_atom_types=>link_t,
      END OF ty_abapgit_file .
    TYPES:
      tt_abapgit_file TYPE STANDARD TABLE OF ty_abapgit_file WITH KEY filename path .
    TYPES:
      BEGIN OF ty_abapgit_object,
        object_ref TYPE sadt_object_reference,
        wbkey      TYPE string,
        version    TYPE sadt_obj_version,
        files      TYPE tt_abapgit_file,
        atom_links TYPE if_atom_types=>link_t,
      END OF ty_abapgit_object .
    TYPES:
      tt_abapgit_object TYPE STANDARD TABLE OF ty_abapgit_object WITH KEY object_ref-name object_ref-type .
    TYPES:
      BEGIN OF ty_abapgit_staging,
        unstaged_objects TYPE tt_abapgit_object,
        staged_objects   TYPE tt_abapgit_object,
        ignored_objects  TYPE tt_abapgit_object,
        abapgit_comment  TYPE if_abapgit_definitions=>ty_comment,
        atom_links       TYPE if_atom_types=>link_t,
      END OF ty_abapgit_staging .

    CONSTANTS co_content_type_v1 TYPE string VALUE 'application/abapgit.adt.repo.stage.v1+xml' ##NO_TEXT.
    CONSTANTS co_root_name       TYPE string VALUE 'ABAPGITSTAGING' ##NO_TEXT.
    CONSTANTS co_st_name         TYPE string VALUE 'ABAPGIT_ST_REPO_STAGE' ##NO_TEXT.

    METHODS get
        REDEFINITION .

    "! <p class="shorttext synchronized" lang="en">Returns the global workbench key for an object</p>
    METHODS get_object_wb_type
      IMPORTING
                iv_obj_name      TYPE sobj_name
                iv_obj_type      TYPE trobjtype
      RETURNING VALUE(rs_wbtype) TYPE wbobjtype.

    "! <p class="shorttext synchronized" lang="en">Returns the ADT URI for an object</p>
    METHODS get_object_adt_uri
      IMPORTING
                iv_obj_name       TYPE sobj_name
                is_wbtype         TYPE wbobjtype
      RETURNING VALUE(rv_adt_uri) TYPE string.

    "! <p class="shorttext synchronized" lang="en">Returns the File links</p>
    METHODS get_file_links
      IMPORTING
        !iv_repo_key    TYPE if_abapgit_persistence=>ty_value
        !iv_filename    TYPE string
      RETURNING
        VALUE(rt_links) TYPE if_atom_types=>link_t.

  PROTECTED SECTION.
  PRIVATE SECTION.

ENDCLASS.



CLASS cl_abapgit_res_repo_stage IMPLEMENTATION.


  METHOD get.
    DATA:
      lv_repo_key      TYPE if_abapgit_persistence=>ty_value,
      ls_obj_wbtype    TYPE wbobjtype,
      lo_repo_online   TYPE REF TO cl_abapgit_repo_online,
      ls_response_data TYPE ty_abapgit_staging,
      ls_object        TYPE ty_abapgit_object,
      ls_object_ref    TYPE sadt_object_reference,
      ls_file          TYPE ty_abapgit_file,
      lt_file          TYPE tt_abapgit_file,
      lo_repo_content  TYPE REF TO cl_abapgit_repo_content_list,
      lo_user          TYPE REF TO if_abapgit_persist_user.

    FIELD-SYMBOLS:
      <ls_repo_items> TYPE if_abapgit_definitions=>ty_repo_item,
      <ls_repo_file>  TYPE if_abapgit_definitions=>ty_repo_file.

    TRY.
        " Handle request data

        " Get repository key
        request->get_uri_attribute( EXPORTING
                                      name = 'key'
                                      mandatory = abap_true
                                    IMPORTING
                                      value = lv_repo_key ).

        " Get credentials from request header
        DATA(lv_username) = request->get_inner_rest_request( )->get_header_field( 'Username' ).
        " Client encodes password with base64 algorithm
        DATA(lv_password) = cl_abapgit_res_util=>encode_password(
          request->get_inner_rest_request( )->get_header_field( 'Password' ) ).

        " Set credentials in case there are supplied
        IF lv_username IS NOT INITIAL AND lv_password IS NOT INITIAL.
          cl_abapgit_default_auth_info=>set_auth_info( iv_user     = lv_username
                                                       iv_password = lv_password ).
        ENDIF.

        " Determine changed data
        cl_abapgit_factory=>get_environment( )->set_repo_action( if_abapgit_app_log=>c_action_push ).
        DATA(lo_repo) = cl_abapgit_repo_srv=>get_instance( )->get( lv_repo_key ).
        lo_repo_online ?= lo_repo.

        " Check if a different action is still running
        DATA(ls_repo) = cl_abapgit_persist_factory=>get_repo( )->read( iv_key = lv_repo_key
                                                                       iv_with_status = abap_true ).
        DATA(lo_plain_text_handler) = cl_adt_rest_cnt_hdl_factory=>get_instance( )->get_handler_for_plain_text( ).

        IF ls_repo-status = if_abapgit_app_log=>c_run_status-running.
          CASE ls_repo-action.
            WHEN if_abapgit_app_log=>c_action_push.
              response->set_body_data( content_handler = lo_plain_text_handler
                                       data            = |Another Push is currently running| ).
            WHEN if_abapgit_app_log=>c_action_pull.
              response->set_body_data( content_handler = lo_plain_text_handler
                                       data            = |Another Pull is currently running| ).
            WHEN OTHERS.
              cx_abapgit_exception=>raise( 'Unknown Action Type' ).
          ENDCASE.
          " 409
          response->set_status( cl_rest_status_code=>gc_client_error_conflict ).
          EXIT.
        ELSEIF ls_repo-status = if_abapgit_app_log=>c_run_status-initial.
          CASE ls_repo-action.
            WHEN if_abapgit_app_log=>c_action_push.
              response->set_body_data( content_handler = lo_plain_text_handler
                                       data            = |Another Push action is waiting to be executed| ).
            WHEN if_abapgit_app_log=>c_action_pull.
              response->set_body_data( content_handler = lo_plain_text_handler
                                       data            = |Another Pull action is waiting to be executed| ).
            WHEN OTHERS.
              cx_abapgit_exception=>raise( 'Unknown Action Type' ).
          ENDCASE.
          " 409
          response->set_status( cl_rest_status_code=>gc_client_error_conflict ).
          EXIT.
        ENDIF.

        " Force refresh on stage, to make sure the latest local and remote files are used
        lo_repo_online->refresh( ).

        " Retrieve repository content
        lo_repo_content = NEW #( lo_repo ).

        DATA(lt_repo_items) = lo_repo_content->list( iv_path         = '/'
                                                     iv_by_folders   = abap_false
                                                     iv_changes_only = abap_true ).
        " Process data to output structure
        LOOP AT lt_repo_items ASSIGNING <ls_repo_items>.
          " Consider only those files which already exist locally
          IF <ls_repo_items>-lstate IS NOT INITIAL.
            CLEAR: ls_object, ls_object_ref.

            " Header data
            " non-code and meta files
            IF <ls_repo_items>-obj_name IS INITIAL.

              " handle non-code and meta files
              IF <ls_repo_items>-files IS NOT INITIAL.
                " if the logic is proper move the text to a message class
                ls_object_ref-name = 'non-code and meta files'.
              ENDIF.
            ELSE.
              ls_object_ref-name = <ls_repo_items>-obj_name.
              ls_object_ref-type = <ls_repo_items>-obj_type.

              IF <ls_repo_items>-obj_type IS NOT INITIAL.
                " get object workbench type
                ls_obj_wbtype = get_object_wb_type( iv_obj_name = <ls_repo_items>-obj_name
                                                    iv_obj_type = <ls_repo_items>-obj_type ).
                " get workbench key and adt uri for the object
                IF ls_obj_wbtype IS NOT INITIAL.
                  ls_object-wbkey = cl_wb_object_type=>get_global_id_from_global_type( p_global_type = ls_obj_wbtype ).
                  ls_object_ref-uri = get_object_adt_uri( iv_obj_name = <ls_repo_items>-obj_name
                                                          is_wbtype   = ls_obj_wbtype ).
                ENDIF.
              ENDIF.
            ENDIF.
            ls_object-object_ref = ls_object_ref.

            " File specific data
            CLEAR: ls_file, lt_file.
            LOOP AT <ls_repo_items>-files ASSIGNING <ls_repo_file>.
              ls_file-path = <ls_repo_file>-path.
              ls_file-filename = <ls_repo_file>-filename.
              ls_file-remotestate = <ls_repo_file>-rstate.
              ls_file-localstate = <ls_repo_file>-lstate.
              ls_file-atom_links = get_file_links( iv_repo_key = lo_repo_online->get_key( )
                                                   iv_filename = ls_file-filename ).
              INSERT ls_file INTO TABLE lt_file.
            ENDLOOP.
            ls_object-files = lt_file.
            INSERT ls_object INTO TABLE ls_response_data-unstaged_objects.
          ENDIF.
        ENDLOOP.

        " Author and Committer details
        lo_user = cl_abapgit_persistence_user=>get_instance( ).

        DATA(lv_user) = lo_user->get_repo_git_user_name( lo_repo_online->get_url( ) ).
        IF lv_user IS INITIAL.
          lv_user  = lo_user->get_default_git_user_name( ).
        ENDIF.
        IF lv_user IS INITIAL.
          " get default from user master record
          lv_user = cl_abapgit_user_master_record=>get_instance( sy-uname )->get_name( ).
        ENDIF.

        DATA(lv_email) = lo_user->get_repo_git_user_email( lo_repo_online->get_url( ) ).
        IF lv_email IS INITIAL.
          lv_email = lo_user->get_default_git_user_email( ).
        ENDIF.
        IF lv_email IS INITIAL.
          " get default from user master record
          lv_email = cl_abapgit_user_master_record=>get_instance( sy-uname )->get_email( ).
        ENDIF.

        ls_response_data-abapgit_comment-author-name     = lv_user.
        ls_response_data-abapgit_comment-author-email    = lv_email.
        ls_response_data-abapgit_comment-committer-name  = lv_user.
        ls_response_data-abapgit_comment-committer-email = lv_email.

        " Create Response Content Handler
        DATA(lo_response_content_handler) = cl_adt_rest_cnt_hdl_factory=>get_instance( )->get_handler_for_xml_using_st(
          st_name      = co_st_name
          root_name    = co_root_name
          content_type = co_content_type_v1 ).

        " Prepare Response
        response->set_body_data( content_handler = lo_response_content_handler
                                 data = ls_response_data ).
        response->set_status( cl_rest_status_code=>gc_success_ok ).

        " Handle issues
      CATCH cx_abapgit_exception cx_abapgit_app_log cx_a4c_logger cx_cbo_job_scheduler cx_uuid_error
          cx_abapgit_not_found INTO DATA(lx_exception).
        ROLLBACK WORK.
        cx_adt_rest_abapgit=>raise_with_error(
          ix_error       = lx_exception
          iv_http_status = cl_rest_status_code=>gc_server_error_internal ).
    ENDTRY.
  ENDMETHOD.


  METHOD get_file_links.

   DATA:
      lv_file_rel_fetch_local  TYPE string VALUE 'http://www.sap.com/adt/abapgit/file/relations/fetch/localversion',
      lv_file_rel_fetch_remote TYPE string VALUE 'http://www.sap.com/adt/abapgit/file/relations/fetch/remoteversion',
      lv_root_path             TYPE string VALUE '/sap/bc/adt/abapgit'.

    DATA(lo_atom_util) = cl_adt_atom_utility=>create_instance( ).

    lo_atom_util->append_link(
      EXPORTING
        rel  = lv_file_rel_fetch_local
        href = |{ lv_root_path }/repos/{ escape( val = iv_repo_key format = cl_abap_format=>e_xss_url ) }/files?filename={ escape( val = iv_filename format = cl_abap_format=>e_xss_url ) }&version=local|
        type = |fetch_link|
      CHANGING
        links = rt_links ).

    lo_atom_util->append_link(
      EXPORTING
        rel  = lv_file_rel_fetch_remote
        href = |{ lv_root_path }/repos/{ escape( val = iv_repo_key format = cl_abap_format=>e_xss_url ) }/files?filename={ escape( val = iv_filename format = cl_abap_format=>e_xss_url ) }&version=remote|
        type = |fetch_link|
      CHANGING
        links = rt_links ).

  ENDMETHOD.


  METHOD get_object_adt_uri.

    TRY.
        rv_adt_uri = cl_adt_uri_mapper=>get_instance( )->if_adt_uri_mapper~get_adt_object_ref_uri(
           name = CONV #( iv_obj_name )
           type = VALUE #( objtype_tr = is_wbtype-objtype_tr subtype_wb = is_wbtype-subtype_wb ) ).
      CATCH cx_adt_uri_mapping.
    ENDTRY.

  ENDMETHOD.


  METHOD get_object_wb_type.

    cl_wb_object=>create_from_transport_key(
      EXPORTING
          p_obj_name = CONV trobj_name( iv_obj_name )
          p_object   = iv_obj_type
      RECEIVING
          p_wb_object = DATA(lr_wb_object)
      EXCEPTIONS
          objecttype_not_existing = 1
          OTHERS = 2 ).

    IF lr_wb_object IS NOT INITIAL.
      lr_wb_object->get_global_wb_key( IMPORTING p_object_type = rs_wbtype ).
    ENDIF.

  ENDMETHOD.
ENDCLASS.