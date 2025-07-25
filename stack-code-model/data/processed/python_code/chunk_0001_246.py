CLASS ycl_abapgit_services_repo DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.

    CLASS-METHODS new_online
      IMPORTING
        !iv_url        TYPE string
      RETURNING
        VALUE(ro_repo) TYPE REF TO ycl_abapgit_repo_online
      RAISING
        ycx_abapgit_exception
        ycx_abapgit_cancel .
    CLASS-METHODS refresh
      IMPORTING
        !iv_key TYPE yif_abapgit_persistence=>ty_repo-key
      RAISING
        ycx_abapgit_exception .
    CLASS-METHODS remove
      IMPORTING
        !iv_key TYPE yif_abapgit_persistence=>ty_repo-key
      RAISING
        ycx_abapgit_exception
        ycx_abapgit_cancel .
    CLASS-METHODS purge
      IMPORTING
        !iv_key TYPE yif_abapgit_persistence=>ty_repo-key
      RAISING
        ycx_abapgit_exception
        ycx_abapgit_cancel .
    CLASS-METHODS new_offline
      RAISING
        ycx_abapgit_exception
        ycx_abapgit_cancel .
    CLASS-METHODS remote_attach
      IMPORTING
        !iv_key TYPE yif_abapgit_persistence=>ty_repo-key
      RAISING
        ycx_abapgit_exception
        ycx_abapgit_cancel .
    CLASS-METHODS remote_detach
      IMPORTING
        !iv_key TYPE yif_abapgit_persistence=>ty_repo-key
      RAISING
        ycx_abapgit_exception
        ycx_abapgit_cancel .
    CLASS-METHODS remote_change
      IMPORTING
        !iv_key TYPE yif_abapgit_persistence=>ty_repo-key
      RAISING
        ycx_abapgit_exception
        ycx_abapgit_cancel .
    CLASS-METHODS refresh_local_checksums
      IMPORTING
        !iv_key TYPE yif_abapgit_persistence=>ty_repo-key
      RAISING
        ycx_abapgit_exception
        ycx_abapgit_cancel .
    CLASS-METHODS toggle_favorite
      IMPORTING
        !iv_key TYPE yif_abapgit_persistence=>ty_repo-key
      RAISING
        ycx_abapgit_exception .
    CLASS-METHODS open_se80
      IMPORTING
        !iv_package TYPE devclass
      RAISING
        ycx_abapgit_exception .
    CLASS-METHODS transport_to_branch
      IMPORTING
        !iv_repository_key TYPE yif_abapgit_persistence=>ty_value
      RAISING
        ycx_abapgit_exception
        ycx_abapgit_cancel .
    CLASS-METHODS gui_deserialize
      IMPORTING
        !io_repo TYPE REF TO ycl_abapgit_repo
      RAISING
        ycx_abapgit_exception .
  PRIVATE SECTION.

    CLASS-METHODS popup_overwrite
      CHANGING
        !ct_overwrite TYPE yif_abapgit_definitions=>ty_overwrite_tt
      RAISING
        ycx_abapgit_exception
        ycx_abapgit_cancel .
    CLASS-METHODS popup_package_overwrite
      CHANGING
        !ct_overwrite TYPE yif_abapgit_definitions=>ty_overwrite_tt
      RAISING
        ycx_abapgit_exception
        ycx_abapgit_cancel .
ENDCLASS.



CLASS YCL_ABAPGIT_SERVICES_REPO IMPLEMENTATION.


  METHOD gui_deserialize.

    DATA: ls_checks       TYPE yif_abapgit_definitions=>ty_deserialize_checks,
          lt_requirements TYPE yif_abapgit_dot_abapgit=>ty_requirement_tt.


* find troublesome objects
    ls_checks = io_repo->deserialize_checks( ).

* and let the user decide what to do
    TRY.
        popup_overwrite( CHANGING ct_overwrite = ls_checks-overwrite ).
        popup_package_overwrite( CHANGING ct_overwrite = ls_checks-warning_package ).

        IF ls_checks-requirements-met = 'N'.
          lt_requirements = io_repo->get_dot_abapgit( )->get_data( )-requirements.
          ycl_abapgit_requirement_helper=>requirements_popup( lt_requirements ).
          ls_checks-requirements-decision = 'Y'.
        ENDIF.

        IF ls_checks-transport-required = abap_true.
          ls_checks-transport-transport = ycl_abapgit_ui_factory=>get_popups( )->popup_transport_request(
            is_transport_type = ls_checks-transport-type ).
        ENDIF.

      CATCH ycx_abapgit_cancel.
        RETURN.
    ENDTRY.

* and pass decisions to deserialize
    io_repo->deserialize( ls_checks ).

  ENDMETHOD.


  METHOD new_offline.

    DATA: lo_repo  TYPE REF TO ycl_abapgit_repo,
          ls_popup TYPE yif_abapgit_popups=>ty_popup.

    ls_popup  = ycl_abapgit_ui_factory=>get_popups( )->repo_new_offline( ).
    IF ls_popup-cancel = abap_true.
      RAISE EXCEPTION TYPE ycx_abapgit_cancel.
    ENDIF.

    lo_repo = ycl_abapgit_repo_srv=>get_instance( )->new_offline(
      iv_url     = ls_popup-url
      iv_package = ls_popup-package ).

    ycl_abapgit_persistence_user=>get_instance( )->set_repo_show( lo_repo->get_key( ) ). " Set default repo for user
    toggle_favorite( lo_repo->get_key( ) ).

    COMMIT WORK AND WAIT.

  ENDMETHOD.


  METHOD new_online.

    DATA: ls_popup TYPE yif_abapgit_popups=>ty_popup.

    ls_popup = ycl_abapgit_ui_factory=>get_popups( )->repo_popup( iv_url ).
    IF ls_popup-cancel = abap_true.
      RAISE EXCEPTION TYPE ycx_abapgit_cancel.
    ENDIF.

    ro_repo = ycl_abapgit_repo_srv=>get_instance( )->new_online(
      iv_url         = ls_popup-url
      iv_branch_name = ls_popup-branch_name
      iv_package     = ls_popup-package ).

    toggle_favorite( ro_repo->get_key( ) ).

* Set default repo for user
    ycl_abapgit_persistence_user=>get_instance( )->set_repo_show( ro_repo->get_key( ) ).

    COMMIT WORK.

  ENDMETHOD.


  METHOD open_se80.

    CALL FUNCTION 'RS_TOOL_ACCESS'
      EXPORTING
        operation       = 'SHOW'
        in_new_window   = abap_true
        object_name     = iv_package
        object_type     = 'DEVC'
        with_objectlist = abap_true.

  ENDMETHOD.


  METHOD popup_overwrite.

    DATA: lt_columns  TYPE stringtab,
          lt_selected LIKE ct_overwrite,
          lv_column   LIKE LINE OF lt_columns,
          li_popups   TYPE REF TO yif_abapgit_popups.

    FIELD-SYMBOLS: <ls_overwrite> LIKE LINE OF ct_overwrite.


    IF lines( ct_overwrite ) = 0.
      RETURN.
    ENDIF.

    lv_column = 'OBJ_TYPE'.
    INSERT lv_column INTO TABLE lt_columns.
    lv_column = 'OBJ_NAME'.
    INSERT lv_column INTO TABLE lt_columns.

    li_popups = ycl_abapgit_ui_factory=>get_popups( ).
    li_popups->popup_to_select_from_list(
      EXPORTING
        it_list               = ct_overwrite
        iv_header_text         = |The following Objects have been modified locally.|
                            && | Select the Objects which should be overwritten.|
        iv_select_column_text  = 'Overwrite?'
        it_columns_to_display = lt_columns
      IMPORTING
        et_list               = lt_selected ).

    LOOP AT ct_overwrite ASSIGNING <ls_overwrite>.
      READ TABLE lt_selected WITH KEY
        obj_type = <ls_overwrite>-obj_type
        obj_name = <ls_overwrite>-obj_name
        TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        <ls_overwrite>-decision = 'Y'.
      ELSE.
        <ls_overwrite>-decision = 'N'.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD popup_package_overwrite.

    DATA: lv_question TYPE c LENGTH 200,
          lv_answer   TYPE c.

    FIELD-SYMBOLS: <ls_overwrite> LIKE LINE OF ct_overwrite.


    IF lines( ct_overwrite ) = 0.
      RETURN.
    ENDIF.

    LOOP AT ct_overwrite ASSIGNING <ls_overwrite>.
      CONCATENATE 'Overwrite object' <ls_overwrite>-obj_type <ls_overwrite>-obj_name
        'from package' <ls_overwrite>-devclass
        INTO lv_question SEPARATED BY space.                "#EC NOTEXT

      lv_answer = ycl_abapgit_ui_factory=>get_popups( )->popup_to_confirm(
        iv_titlebar              = 'Warning'
        iv_text_question         = lv_question
        iv_text_button_1         = 'Ok'
        iv_icon_button_1         = 'ICON_DELETE'
        iv_text_button_2         = 'Cancel'
        iv_icon_button_2         = 'ICON_CANCEL'
        iv_default_button        = '2'
        iv_display_cancel_button = abap_false ).               "#EC NOTEXT

      IF lv_answer = '2'.
        RAISE EXCEPTION TYPE ycx_abapgit_cancel.
      ENDIF.

* todo, let the user decide yes/no/cancel
      <ls_overwrite>-decision = 'Y'.

    ENDLOOP.

  ENDMETHOD.


  METHOD purge.

    DATA: lt_tadir    TYPE yif_abapgit_definitions=>ty_tadir_tt,
          lv_answer   TYPE c LENGTH 1,
          lo_repo     TYPE REF TO ycl_abapgit_repo,
          lv_package  TYPE devclass,
          lv_question TYPE c LENGTH 100,
          ls_checks   TYPE yif_abapgit_definitions=>ty_delete_checks.


    lo_repo = ycl_abapgit_repo_srv=>get_instance( )->get( iv_key ).

    lv_package = lo_repo->get_package( ).
    lt_tadir   = ycl_abapgit_factory=>get_tadir( )->read( lv_package ).

    IF lines( lt_tadir ) > 0.

      lv_question = |This will DELETE all objects in package { lv_package
        } ({ lines( lt_tadir ) } objects) from the system|. "#EC NOTEXT

      lv_answer = ycl_abapgit_ui_factory=>get_popups( )->popup_to_confirm(
        iv_titlebar              = 'Uninstall'
        iv_text_question         = lv_question
        iv_text_button_1         = 'Delete'
        iv_icon_button_1         = 'ICON_DELETE'
        iv_text_button_2         = 'Cancel'
        iv_icon_button_2         = 'ICON_CANCEL'
        iv_default_button        = '2'
        iv_display_cancel_button = abap_false ).               "#EC NOTEXT

      IF lv_answer = '2'.
        RAISE EXCEPTION TYPE ycx_abapgit_cancel.
      ENDIF.

    ENDIF.

    ls_checks = lo_repo->delete_checks( ).
    IF ls_checks-transport-required = abap_true.
      ls_checks-transport-transport = ycl_abapgit_ui_factory=>get_popups(
                                        )->popup_transport_request(  ls_checks-transport-type ).
    ENDIF.

    ycl_abapgit_repo_srv=>get_instance( )->purge( io_repo   = lo_repo
                                                  is_checks = ls_checks ).

    COMMIT WORK.

  ENDMETHOD.


  METHOD refresh.

    ycl_abapgit_repo_srv=>get_instance( )->get( iv_key )->refresh( ).

  ENDMETHOD.  "refresh


  METHOD refresh_local_checksums.

    DATA: lv_answer   TYPE c,
          lv_question TYPE string,
          lo_repo     TYPE REF TO ycl_abapgit_repo.


    IF ycl_abapgit_auth=>is_allowed( yif_abapgit_auth=>gc_authorization-update_local_checksum ) = abap_false.
      ycx_abapgit_exception=>raise( 'Not authorized' ).
    ENDIF.

    lo_repo = ycl_abapgit_repo_srv=>get_instance( )->get( iv_key ).

    lv_question =  'This will rebuild and overwrite local repo checksums.'.

    IF lo_repo->is_offline( ) = abap_false.
      lv_question = lv_question
                && ' The logic: if local and remote file differs then:'
                && ' if remote branch is ahead then assume changes are remote,'
                && ' else (branches are equal) assume changes are local.'
                && ' This will lead to incorrect state for files changed on both sides.'
                && ' Please make sure you don''t have ones like that.'.
    ENDIF.

    lv_answer = ycl_abapgit_ui_factory=>get_popups( )->popup_to_confirm(
      iv_titlebar              = 'Warning'
      iv_text_question         = lv_question
      iv_text_button_1         = 'OK'
      iv_icon_button_1         = 'ICON_DELETE'
      iv_text_button_2         = 'Cancel'
      iv_icon_button_2         = 'ICON_CANCEL'
      iv_default_button        = '2'
      iv_display_cancel_button = abap_false ).                 "#EC NOTEXT

    IF lv_answer = '2'.
      RAISE EXCEPTION TYPE ycx_abapgit_cancel.
    ENDIF.

    lo_repo->rebuild_local_checksums( ).

    COMMIT WORK AND WAIT.

  ENDMETHOD.


  METHOD remote_attach.

    DATA: ls_popup TYPE yif_abapgit_popups=>ty_popup,
          lo_repo  TYPE REF TO ycl_abapgit_repo_online.

    ls_popup = ycl_abapgit_ui_factory=>get_popups( )->repo_popup(
      iv_title          = 'Attach repo to remote ...'
      iv_url            = ''
      iv_package        = ycl_abapgit_repo_srv=>get_instance( )->get( iv_key )->get_package( )
      iv_freeze_package = abap_true ).
    IF ls_popup-cancel = abap_true.
      RAISE EXCEPTION TYPE ycx_abapgit_cancel.
    ENDIF.

    ycl_abapgit_repo_srv=>get_instance( )->switch_repo_type(
      iv_key = iv_key
      iv_offline = abap_false ).

    lo_repo ?= ycl_abapgit_repo_srv=>get_instance( )->get( iv_key ).
    lo_repo->set_url( ls_popup-url ).
    lo_repo->set_branch_name( ls_popup-branch_name ).

    COMMIT WORK.

  ENDMETHOD.


  METHOD remote_change.

    DATA: ls_popup TYPE yif_abapgit_popups=>ty_popup,
          lo_repo  TYPE REF TO ycl_abapgit_repo_online.

    lo_repo ?= ycl_abapgit_repo_srv=>get_instance( )->get( iv_key ).

    ls_popup = ycl_abapgit_ui_factory=>get_popups( )->repo_popup(
      iv_title          = 'Change repo remote ...'
      iv_url            = lo_repo->get_url( )
      iv_package        = lo_repo->get_package( )
      iv_freeze_package = abap_true ).
    IF ls_popup-cancel = abap_true.
      RAISE EXCEPTION TYPE ycx_abapgit_cancel.
    ENDIF.

    lo_repo ?= ycl_abapgit_repo_srv=>get_instance( )->get( iv_key ).
    lo_repo->set_url( ls_popup-url ).
    lo_repo->set_branch_name( ls_popup-branch_name ).

    COMMIT WORK.

  ENDMETHOD.


  METHOD remote_detach.

    DATA: lv_answer TYPE c LENGTH 1.

    lv_answer = ycl_abapgit_ui_factory=>get_popups( )->popup_to_confirm(
      iv_titlebar              = 'Make repository OFF-line'
      iv_text_question         = 'This will detach the repo from remote and make it OFF-line'
      iv_text_button_1         = 'Make OFF-line'
      iv_icon_button_1         = 'ICON_WF_UNLINK'
      iv_text_button_2         = 'Cancel'
      iv_icon_button_2         = 'ICON_CANCEL'
      iv_default_button        = '2'
      iv_display_cancel_button = abap_false ).                 "#EC NOTEXT

    IF lv_answer = '2'.
      RAISE EXCEPTION TYPE ycx_abapgit_cancel.
    ENDIF.

    ycl_abapgit_repo_srv=>get_instance( )->switch_repo_type( iv_key = iv_key  iv_offline = abap_true ).

    COMMIT WORK.

  ENDMETHOD.


  METHOD remove.

    DATA: lv_answer   TYPE c LENGTH 1,
          lo_repo     TYPE REF TO ycl_abapgit_repo,
          lv_package  TYPE devclass,
          lv_question TYPE c LENGTH 200.


    lo_repo     = ycl_abapgit_repo_srv=>get_instance( )->get( iv_key ).
    lv_package  = lo_repo->get_package( ).
    lv_question = |This will remove the repository reference to the package { lv_package
      }. All objects will safely remain in the system.|.

    lv_answer = ycl_abapgit_ui_factory=>get_popups( )->popup_to_confirm(
      iv_titlebar              = 'Remove'
      iv_text_question         = lv_question
      iv_text_button_1         = 'Remove'
      iv_icon_button_1         = 'ICON_WF_UNLINK'
      iv_text_button_2         = 'Cancel'
      iv_icon_button_2         = 'ICON_CANCEL'
      iv_default_button        = '2'
      iv_display_cancel_button = abap_false ).                 "#EC NOTEXT

    IF lv_answer = '2'.
      RAISE EXCEPTION TYPE ycx_abapgit_cancel.
    ENDIF.

    ycl_abapgit_repo_srv=>get_instance( )->delete( lo_repo ).

    COMMIT WORK.

  ENDMETHOD.


  METHOD toggle_favorite.

    ycl_abapgit_persistence_user=>get_instance( )->toggle_favorite( iv_key ).

  ENDMETHOD.


  METHOD transport_to_branch.

    DATA:
      lo_repository          TYPE REF TO ycl_abapgit_repo_online,
      lo_transport_to_branch TYPE REF TO ycl_abapgit_transport_2_branch,
      lt_transport_headers   TYPE trwbo_request_headers,
      lt_transport_objects   TYPE yif_abapgit_definitions=>ty_tadir_tt,
      ls_transport_to_branch TYPE yif_abapgit_definitions=>ty_transport_to_branch.


    IF ycl_abapgit_auth=>is_allowed( yif_abapgit_auth=>gc_authorization-transport_to_branch ) = abap_false.
      ycx_abapgit_exception=>raise( 'Not authorized' ).
    ENDIF.

    lo_repository ?= ycl_abapgit_repo_srv=>get_instance( )->get( iv_repository_key ).

    lt_transport_headers = ycl_abapgit_ui_factory=>get_popups( )->popup_to_select_transports( ).
    lt_transport_objects = ycl_abapgit_transport=>to_tadir( lt_transport_headers ).
    IF lt_transport_objects IS INITIAL.
      ycx_abapgit_exception=>raise( 'Canceled or List of objects is empty ' ).
    ENDIF.

    ls_transport_to_branch = ycl_abapgit_ui_factory=>get_popups( )->popup_to_create_transp_branch(
      lt_transport_headers ).

    CREATE OBJECT lo_transport_to_branch.
    lo_transport_to_branch->create(
      io_repository          = lo_repository
      is_transport_to_branch = ls_transport_to_branch
      it_transport_objects   = lt_transport_objects ).

  ENDMETHOD.
ENDCLASS.