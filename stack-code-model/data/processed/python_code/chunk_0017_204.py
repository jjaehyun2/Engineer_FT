CLASS zcl_abapgit_repo DEFINITION
  PUBLIC
  ABSTRACT
  CREATE PUBLIC.

  PUBLIC SECTION.

    METHODS bind_listener
      IMPORTING
        ii_listener TYPE REF TO zif_abapgit_repo_listener.
    METHODS deserialize_checks
      RETURNING
        VALUE(rs_checks) TYPE zif_abapgit_definitions=>ty_deserialize_checks
      RAISING
        zcx_abapgit_exception .
    METHODS delete_checks
      RETURNING
        VALUE(rs_checks) TYPE zif_abapgit_definitions=>ty_delete_checks
      RAISING
        zcx_abapgit_exception .
    METHODS constructor
      IMPORTING
        !is_data TYPE zif_abapgit_persistence=>ty_repo .
    METHODS get_key
      RETURNING
        VALUE(rv_key) TYPE zif_abapgit_persistence=>ty_value .
    METHODS get_name
          ABSTRACT
      RETURNING
        VALUE(rv_name) TYPE string
      RAISING
        zcx_abapgit_exception .
    METHODS get_files_local
      IMPORTING
        !io_log         TYPE REF TO zcl_abapgit_log OPTIONAL
        !it_filter      TYPE zif_abapgit_definitions=>ty_tadir_tt OPTIONAL
      RETURNING
        VALUE(rt_files) TYPE zif_abapgit_definitions=>ty_files_item_tt
      RAISING
        zcx_abapgit_exception .
    METHODS get_local_checksums
      RETURNING
        VALUE(rt_checksums) TYPE zif_abapgit_persistence=>ty_local_checksum_tt .
    METHODS get_local_checksums_per_file
      RETURNING
        VALUE(rt_checksums) TYPE zif_abapgit_definitions=>ty_file_signatures_tt .
    METHODS get_files_remote
      RETURNING
        VALUE(rt_files) TYPE zif_abapgit_definitions=>ty_files_tt
      RAISING
        zcx_abapgit_exception .
    METHODS get_package
      RETURNING
        VALUE(rv_package) TYPE zif_abapgit_persistence=>ty_repo-package .
    METHODS get_dot_abapgit
      RETURNING
        VALUE(ro_dot_abapgit) TYPE REF TO zcl_abapgit_dot_abapgit .
    METHODS set_dot_abapgit
      IMPORTING
        !io_dot_abapgit TYPE REF TO zcl_abapgit_dot_abapgit
      RAISING
        zcx_abapgit_exception .
    METHODS deserialize
      IMPORTING
        !is_checks TYPE zif_abapgit_definitions=>ty_deserialize_checks
      RAISING
        zcx_abapgit_exception .
    METHODS refresh
      IMPORTING
        !iv_drop_cache TYPE abap_bool DEFAULT abap_false
      RAISING
        zcx_abapgit_exception .
    METHODS update_local_checksums
      IMPORTING
        !it_files TYPE zif_abapgit_definitions=>ty_file_signatures_tt
      RAISING
        zcx_abapgit_exception .
    METHODS rebuild_local_checksums
      RAISING
        zcx_abapgit_exception .
    METHODS find_remote_dot_abapgit
      RETURNING
        VALUE(ro_dot) TYPE REF TO zcl_abapgit_dot_abapgit
      RAISING
        zcx_abapgit_exception .
    METHODS is_offline
      RETURNING
        VALUE(rv_offline) TYPE abap_bool
      RAISING
        zcx_abapgit_exception .
    METHODS set_files_remote
      IMPORTING
        !it_files TYPE zif_abapgit_definitions=>ty_files_tt .
    METHODS get_local_settings
      RETURNING
        VALUE(rs_settings) TYPE zif_abapgit_persistence=>ty_repo-local_settings .
    METHODS set_local_settings
      IMPORTING
        !is_settings TYPE zif_abapgit_persistence=>ty_repo-local_settings
      RAISING
        zcx_abapgit_exception .
    METHODS run_code_inspector
      RETURNING
        VALUE(rt_list) TYPE scit_alvlist
      RAISING
        zcx_abapgit_exception .
    METHODS has_remote_source
          ABSTRACT
      RETURNING
        VALUE(rv_yes) TYPE abap_bool .
    METHODS status
      IMPORTING
        !io_log           TYPE REF TO zcl_abapgit_log OPTIONAL
      RETURNING
        VALUE(rt_results) TYPE zif_abapgit_definitions=>ty_results_tt
      RAISING
        zcx_abapgit_exception .
    METHODS get_unnecessary_local_objs
      RETURNING
        VALUE(rt_unnecessary_local_objects) TYPE zif_abapgit_definitions=>ty_tadir_tt
      RAISING
        zcx_abapgit_exception .
    METHODS switch_repo_type
      IMPORTING
        iv_offline TYPE abap_bool
      RAISING
        zcx_abapgit_exception .

  PROTECTED SECTION.

    DATA mt_local TYPE zif_abapgit_definitions=>ty_files_item_tt .
    DATA mt_remote TYPE zif_abapgit_definitions=>ty_files_tt .
    DATA mv_request_local_refresh TYPE abap_bool .
    DATA mv_last_serialization TYPE timestamp .
    DATA ms_data TYPE zif_abapgit_persistence=>ty_repo .
    DATA mv_code_inspector_successful TYPE abap_bool .
    DATA mv_request_remote_refresh TYPE abap_bool .
    DATA mt_status TYPE zif_abapgit_definitions=>ty_results_tt .

    METHODS set
      IMPORTING it_checksums       TYPE zif_abapgit_persistence=>ty_local_checksum_tt OPTIONAL
                iv_url             TYPE zif_abapgit_persistence=>ty_repo-url OPTIONAL
                iv_branch_name     TYPE zif_abapgit_persistence=>ty_repo-branch_name OPTIONAL
                iv_head_branch     TYPE zif_abapgit_persistence=>ty_repo-head_branch OPTIONAL
                iv_offline         TYPE zif_abapgit_persistence=>ty_repo-offline OPTIONAL
                is_dot_abapgit     TYPE zif_abapgit_persistence=>ty_repo-dot_abapgit OPTIONAL
                is_local_settings  TYPE zif_abapgit_persistence=>ty_repo-local_settings OPTIONAL
                iv_deserialized_at TYPE zif_abapgit_persistence=>ty_repo-deserialized_at OPTIONAL
                iv_deserialized_by TYPE zif_abapgit_persistence=>ty_repo-deserialized_by OPTIONAL
      RAISING
                zcx_abapgit_exception .
    METHODS reset_status .
    METHODS reset_remote .
  PRIVATE SECTION.

    DATA mi_listener TYPE REF TO zif_abapgit_repo_listener .

    TYPES:
      ty_cache_tt TYPE SORTED TABLE OF zif_abapgit_definitions=>ty_file_item
                             WITH NON-UNIQUE KEY item .
    METHODS notify_listener
      IMPORTING
        is_change_mask TYPE zif_abapgit_persistence=>ty_repo_meta_mask
      RAISING
        zcx_abapgit_exception .
    METHODS apply_filter
      IMPORTING
        !it_filter TYPE zif_abapgit_definitions=>ty_tadir_tt
      CHANGING
        !ct_tadir  TYPE zif_abapgit_definitions=>ty_tadir_tt .
    METHODS build_dotabapgit_file
      RETURNING
        VALUE(rs_file) TYPE zif_abapgit_definitions=>ty_file
      RAISING
        zcx_abapgit_exception .
    METHODS lookup_cache
      IMPORTING
        !it_cache TYPE ty_cache_tt
      EXPORTING
        !et_found TYPE zif_abapgit_definitions=>ty_files_item_tt
      CHANGING
        !ct_tadir TYPE zif_abapgit_definitions=>ty_tadir_tt
      RAISING
        zcx_abapgit_exception .
    METHODS update_last_deserialize
      RAISING
        zcx_abapgit_exception .
ENDCLASS.



CLASS ZCL_ABAPGIT_REPO IMPLEMENTATION.


  METHOD apply_filter.

    DATA: lt_filter TYPE SORTED TABLE OF zif_abapgit_definitions=>ty_tadir
                      WITH NON-UNIQUE KEY object obj_name,
          lv_index  TYPE i.

    FIELD-SYMBOLS: <ls_tadir> LIKE LINE OF ct_tadir.


    IF lines( it_filter ) = 0.
      RETURN.
    ENDIF.

    lt_filter = it_filter.

* this is another loop at TADIR, but typically the filter is blank
    LOOP AT ct_tadir ASSIGNING <ls_tadir>.
      lv_index = sy-tabix.
      READ TABLE lt_filter TRANSPORTING NO FIELDS WITH KEY object = <ls_tadir>-object
                                                           obj_name = <ls_tadir>-obj_name
                                                  BINARY SEARCH.
      IF sy-subrc <> 0.
        DELETE ct_tadir INDEX lv_index.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD bind_listener.
    mi_listener = ii_listener.
  ENDMETHOD.


  METHOD build_dotabapgit_file.

    rs_file-path     = zif_abapgit_definitions=>c_root_dir.
    rs_file-filename = zif_abapgit_definitions=>c_dot_abapgit.
    rs_file-data     = get_dot_abapgit( )->serialize( ).
    rs_file-sha1     = zcl_abapgit_hash=>sha1( iv_type = zif_abapgit_definitions=>c_type-blob
                                               iv_data = rs_file-data ).

  ENDMETHOD.


  METHOD constructor.

    ASSERT NOT is_data-key IS INITIAL.

    ms_data = is_data.
    mv_request_remote_refresh = abap_true.

  ENDMETHOD.


  METHOD delete_checks.

    DATA: li_package TYPE REF TO zif_abapgit_sap_package.

    li_package = zcl_abapgit_factory=>get_sap_package( get_package( ) ).
    rs_checks-transport-required = li_package->are_changes_recorded_in_tr_req( ).

  ENDMETHOD.


  METHOD deserialize.

    DATA: lt_updated_files TYPE zif_abapgit_definitions=>ty_file_signatures_tt,
          lx_error         TYPE REF TO zcx_abapgit_exception.


    deserialize_checks( ).

    IF is_checks-requirements-met = 'N' AND is_checks-requirements-decision IS INITIAL.
      zcx_abapgit_exception=>raise( 'Requirements not met and undecided' ).
    ENDIF.

    IF is_checks-transport-required = abap_true AND is_checks-transport-transport IS INITIAL.
      zcx_abapgit_exception=>raise( |No transport request was supplied| ).
    ENDIF.

    TRY.
        lt_updated_files = zcl_abapgit_objects=>deserialize(
            io_repo   = me
            is_checks = is_checks ).
      CATCH zcx_abapgit_exception INTO lx_error.
* ensure to reset default transport request task
        zcl_abapgit_default_transport=>get_instance( )->reset( ).
        RAISE EXCEPTION lx_error.
    ENDTRY.

    APPEND get_dot_abapgit( )->get_signature( ) TO lt_updated_files.

    CLEAR: mt_local, mv_last_serialization.

    update_local_checksums( lt_updated_files ).
    update_last_deserialize( ).
    reset_status( ).

    COMMIT WORK AND WAIT.

  ENDMETHOD.


  METHOD deserialize_checks.

    DATA: lt_requirements    TYPE zif_abapgit_dot_abapgit=>ty_requirement_tt,
          lv_master_language TYPE spras,
          lv_logon_language  TYPE spras.


    find_remote_dot_abapgit( ).

    lv_master_language = get_dot_abapgit( )->get_master_language( ).
    lv_logon_language  = sy-langu.

    IF get_local_settings( )-write_protected = abap_true.
      zcx_abapgit_exception=>raise( 'Cannot deserialize. Local code is write-protected by repo config' ).
    ELSEIF lv_master_language <> lv_logon_language.
      zcx_abapgit_exception=>raise( |Current login language |
                                 && |'{ zcl_abapgit_convert=>conversion_exit_isola_output( lv_logon_language ) }'|
                                 && | does not match master language |
                                 && |'{ zcl_abapgit_convert=>conversion_exit_isola_output( lv_master_language ) }'.|
                                 && | Run 'Advanced' > 'Open in master language'| ).
    ENDIF.

    rs_checks = zcl_abapgit_objects=>deserialize_checks( me ).

    lt_requirements = get_dot_abapgit( )->get_data( )-requirements.
    rs_checks-requirements-met = zcl_abapgit_requirement_helper=>is_requirements_met(
      lt_requirements ).

  ENDMETHOD.


  METHOD find_remote_dot_abapgit.

    FIELD-SYMBOLS: <ls_remote> LIKE LINE OF mt_remote.

    get_files_remote( ).

    READ TABLE mt_remote ASSIGNING <ls_remote>
      WITH KEY path = zif_abapgit_definitions=>c_root_dir
      filename = zif_abapgit_definitions=>c_dot_abapgit.
    IF sy-subrc = 0.
      ro_dot = zcl_abapgit_dot_abapgit=>deserialize( <ls_remote>-data ).
      set_dot_abapgit( ro_dot ).
    ENDIF.

  ENDMETHOD.


  METHOD get_dot_abapgit.
    CREATE OBJECT ro_dot_abapgit
      EXPORTING
        is_data = ms_data-dot_abapgit.
  ENDMETHOD.


  METHOD get_files_local.

    DATA: lt_tadir     TYPE zif_abapgit_definitions=>ty_tadir_tt,
          lo_serialize TYPE REF TO zcl_abapgit_serialize,
          lt_cache     TYPE ty_cache_tt,
          lt_found     LIKE rt_files.

    FIELD-SYMBOLS: <ls_return> LIKE LINE OF rt_files.


    " Serialization happened before and no refresh request
    IF mv_last_serialization IS NOT INITIAL AND mv_request_local_refresh = abap_false.
      rt_files = mt_local.
      RETURN.
    ENDIF.

    APPEND INITIAL LINE TO rt_files ASSIGNING <ls_return>.
    <ls_return>-file = build_dotabapgit_file( ).

    lt_cache = mt_local.

    lt_tadir = zcl_abapgit_factory=>get_tadir( )->read(
      iv_package            = get_package( )
      iv_ignore_subpackages = get_local_settings( )-ignore_subpackages
      iv_only_local_objects = get_local_settings( )-only_local_objects
      io_dot                = get_dot_abapgit( )
      io_log                = io_log ).

    apply_filter( EXPORTING it_filter = it_filter
                  CHANGING ct_tadir  = lt_tadir ).

    lookup_cache(
      EXPORTING it_cache = lt_cache
      IMPORTING et_found = lt_found
      CHANGING ct_tadir = lt_tadir ).
    APPEND LINES OF lt_found TO rt_files.

    CREATE OBJECT lo_serialize.

    lt_found = lo_serialize->serialize(
      it_tadir    = lt_tadir
      iv_language = get_dot_abapgit( )->get_master_language( )
      io_log      = io_log ).
    APPEND LINES OF lt_found TO rt_files.

    GET TIME STAMP FIELD mv_last_serialization.
    mt_local                 = rt_files.
    mv_request_local_refresh = abap_false. " Fulfill refresh

  ENDMETHOD.


  METHOD get_files_remote.
    rt_files = mt_remote.
  ENDMETHOD.


  METHOD get_key.
    rv_key = ms_data-key.
  ENDMETHOD.


  METHOD get_local_checksums.
    rt_checksums = ms_data-local_checksums.
  ENDMETHOD.


  METHOD get_local_checksums_per_file.

    FIELD-SYMBOLS <ls_object> LIKE LINE OF ms_data-local_checksums.

    LOOP AT ms_data-local_checksums ASSIGNING <ls_object>.
      APPEND LINES OF <ls_object>-files TO rt_checksums.
    ENDLOOP.

  ENDMETHOD.


  METHOD get_local_settings.

    rs_settings = ms_data-local_settings.

  ENDMETHOD.


  METHOD get_package.
    rv_package = ms_data-package.
  ENDMETHOD.


  METHOD get_unnecessary_local_objs.

    DATA: lt_tadir        TYPE zif_abapgit_definitions=>ty_tadir_tt,
          lt_tadir_unique TYPE HASHED TABLE OF zif_abapgit_definitions=>ty_tadir
                               WITH UNIQUE KEY pgmid object obj_name,
          lt_local        TYPE zif_abapgit_definitions=>ty_files_item_tt,
          lt_remote       TYPE zif_abapgit_definitions=>ty_files_tt,
          lt_status       TYPE zif_abapgit_definitions=>ty_results_tt,
          lv_package      TYPE zif_abapgit_persistence=>ty_repo-package.

    FIELD-SYMBOLS: <ls_status> TYPE zif_abapgit_definitions=>ty_result,
                   <ls_tadir>  TYPE zif_abapgit_definitions=>ty_tadir.


    " delete objects which are added locally but are not in remote repo
    lt_local  = get_files_local( ).
    lt_remote = get_files_remote( ).
    lt_status = status( ).

    lv_package = get_package( ).
    lt_tadir = zcl_abapgit_factory=>get_tadir( )->read( lv_package ).
    SORT lt_tadir BY pgmid ASCENDING object ASCENDING obj_name ASCENDING devclass ASCENDING.

    LOOP AT lt_status ASSIGNING <ls_status>
                      WHERE lstate = zif_abapgit_definitions=>c_state-added.

      READ TABLE lt_tadir ASSIGNING <ls_tadir>
                          WITH KEY pgmid    = 'R3TR'
                                   object   = <ls_status>-obj_type
                                   obj_name = <ls_status>-obj_name
                                   devclass = <ls_status>-package
                          BINARY SEARCH.
      IF sy-subrc <> 0.
* skip objects that does not exist locally
        CONTINUE.
      ENDIF.

      INSERT <ls_tadir> INTO TABLE lt_tadir_unique.

    ENDLOOP.

    rt_unnecessary_local_objects = lt_tadir_unique.

  ENDMETHOD.


  METHOD is_offline.
    rv_offline = ms_data-offline.
  ENDMETHOD.


  METHOD lookup_cache.

    DATA: ls_item  TYPE zif_abapgit_definitions=>ty_item,
          lv_index TYPE i.

    FIELD-SYMBOLS: <ls_cache> LIKE LINE OF it_cache,
                   <ls_tadir> LIKE LINE OF ct_tadir.

    CLEAR et_found.

    IF mv_last_serialization IS INITIAL.
      RETURN.
    ENDIF.

    LOOP AT ct_tadir ASSIGNING <ls_tadir>.
      lv_index = sy-tabix.

      ls_item-obj_type = <ls_tadir>-object.
      ls_item-obj_name = <ls_tadir>-obj_name.
      ls_item-devclass = <ls_tadir>-devclass.


      READ TABLE it_cache TRANSPORTING NO FIELDS
        WITH KEY item = ls_item. " type+name+package key
      " There is something in cache and the object is unchanged
      IF sy-subrc = 0
          AND abap_false = zcl_abapgit_objects=>has_changed_since(
          is_item      = ls_item
          iv_timestamp = mv_last_serialization ).
        LOOP AT it_cache ASSIGNING <ls_cache> WHERE item = ls_item.
          APPEND <ls_cache> TO et_found.
        ENDLOOP.
        DELETE ct_tadir INDEX lv_index.
      ENDIF.

    ENDLOOP.

  ENDMETHOD.


  METHOD notify_listener.

    DATA ls_meta_slug TYPE zif_abapgit_persistence=>ty_repo_xml.

    IF mi_listener IS BOUND.
      MOVE-CORRESPONDING ms_data TO ls_meta_slug.
      mi_listener->on_meta_change(
        iv_key         = ms_data-key
        is_meta        = ls_meta_slug
        is_change_mask = is_change_mask ).
    ENDIF.

  ENDMETHOD.


  METHOD rebuild_local_checksums.

    DATA:
      lt_local     TYPE zif_abapgit_definitions=>ty_files_item_tt,
      ls_last_item TYPE zif_abapgit_definitions=>ty_item,
      lt_checksums TYPE zif_abapgit_persistence=>ty_local_checksum_tt.

    FIELD-SYMBOLS:
      <ls_checksum> LIKE LINE OF lt_checksums,
      <ls_file_sig> LIKE LINE OF <ls_checksum>-files,
      <ls_local>    LIKE LINE OF lt_local.

    lt_local = get_files_local( ).

    DELETE lt_local " Remove non-code related files except .abapgit
      WHERE item IS INITIAL
      AND NOT ( file-path     = zif_abapgit_definitions=>c_root_dir
      AND       file-filename = zif_abapgit_definitions=>c_dot_abapgit ).
    SORT lt_local BY item.

    LOOP AT lt_local ASSIGNING <ls_local>.
      IF ls_last_item <> <ls_local>-item OR sy-tabix = 1. " First or New item reached ?
        APPEND INITIAL LINE TO lt_checksums ASSIGNING <ls_checksum>.
        <ls_checksum>-item = <ls_local>-item.
        ls_last_item       = <ls_local>-item.
      ENDIF.

      APPEND INITIAL LINE TO <ls_checksum>-files ASSIGNING <ls_file_sig>.
      MOVE-CORRESPONDING <ls_local>-file TO <ls_file_sig>.

    ENDLOOP.

    set( it_checksums = lt_checksums ).
    reset_status( ).

  ENDMETHOD.


  METHOD refresh.

    mv_request_local_refresh = abap_true.
    reset_remote( ).

    IF iv_drop_cache = abap_true.
      CLEAR: mv_last_serialization, mt_local.
    ENDIF.

  ENDMETHOD.


  METHOD reset_remote.
    CLEAR mt_remote.
    mv_request_remote_refresh = abap_true.
    reset_status( ).
  ENDMETHOD.


  METHOD reset_status.
    CLEAR mt_status.
  ENDMETHOD.


  METHOD run_code_inspector.

    DATA: li_code_inspector TYPE REF TO zif_abapgit_code_inspector,
          lv_check_variant  TYPE string.

    lv_check_variant = get_local_settings( )-code_inspector_check_variant.

    IF lv_check_variant IS INITIAL.
      zcx_abapgit_exception=>raise( |No check variant maintained in repo settings.| ).
    ENDIF.

    li_code_inspector = zcl_abapgit_factory=>get_code_inspector(
                                  iv_package            = get_package( )
                                  iv_check_variant_name = |{ lv_check_variant }| ).

    rt_list = li_code_inspector->run( ).

    DELETE rt_list WHERE kind = 'N'.

    READ TABLE rt_list TRANSPORTING NO FIELDS
                       WITH KEY kind = 'E'.

    mv_code_inspector_successful = boolc( sy-subrc <> 0 ).

  ENDMETHOD.


  METHOD set.

* TODO: refactor

    DATA:
          ls_mask        TYPE zif_abapgit_persistence=>ty_repo_meta_mask.


    ASSERT it_checksums IS SUPPLIED
      OR iv_url IS SUPPLIED
      OR iv_branch_name IS SUPPLIED
      OR iv_head_branch IS SUPPLIED
      OR iv_offline IS SUPPLIED
      OR is_dot_abapgit IS SUPPLIED
      OR is_local_settings IS SUPPLIED
      OR iv_deserialized_by IS SUPPLIED
      OR iv_deserialized_at IS SUPPLIED.


    IF it_checksums IS SUPPLIED.
      ms_data-local_checksums = it_checksums.
      ls_mask-local_checksums = abap_true.
    ENDIF.

    IF iv_url IS SUPPLIED.
      ms_data-url = iv_url.
      ls_mask-url = abap_true.
    ENDIF.

    IF iv_branch_name IS SUPPLIED.
      ms_data-branch_name = iv_branch_name.
      ls_mask-branch_name = abap_true.
    ENDIF.

    IF iv_head_branch IS SUPPLIED.
      ms_data-head_branch = iv_head_branch.
      ls_mask-head_branch = abap_true.
    ENDIF.

    IF iv_offline IS SUPPLIED.
      ms_data-offline = iv_offline.
      ls_mask-offline = abap_true.
    ENDIF.

    IF is_dot_abapgit IS SUPPLIED.
      ms_data-dot_abapgit = is_dot_abapgit.
      ls_mask-dot_abapgit = abap_true.
    ENDIF.

    IF is_local_settings IS SUPPLIED.
      ms_data-local_settings = is_local_settings.
      ls_mask-local_settings = abap_true.
    ENDIF.

    IF iv_deserialized_at IS SUPPLIED OR iv_deserialized_by IS SUPPLIED.
      ms_data-deserialized_at = iv_deserialized_at.
      ms_data-deserialized_by = iv_deserialized_by.
      ls_mask-deserialized_at = abap_true.
      ls_mask-deserialized_by = abap_true.
    ENDIF.

    notify_listener( ls_mask ).

  ENDMETHOD.


  METHOD set_dot_abapgit.
    set( is_dot_abapgit = io_dot_abapgit->get_data( ) ).
  ENDMETHOD.


  METHOD set_files_remote.

    mt_remote = it_files.
    mv_request_remote_refresh = abap_false.

  ENDMETHOD.


  METHOD set_local_settings.

    set( is_local_settings = is_settings ).

  ENDMETHOD.


  METHOD status.

    IF lines( mt_status ) = 0.
      mt_status = zcl_abapgit_file_status=>status(
        io_repo = me
        io_log  = io_log ).
    ENDIF.

    rt_results = mt_status.

  ENDMETHOD.


  METHOD switch_repo_type.

    IF iv_offline = ms_data-offline.
      zcx_abapgit_exception=>raise( |Cannot switch_repo_type, offline already = "{ ms_data-offline }"| ).
    ENDIF.

    IF iv_offline = abap_true. " On-line -> OFFline
      set(
        iv_url         = zcl_abapgit_url=>name( ms_data-url )
        iv_branch_name = ''
        iv_head_branch = ''
        iv_offline     = abap_true ).
    ELSE. " OFFline -> On-line
      set( iv_offline = abap_false ).
    ENDIF.

  ENDMETHOD.


  METHOD update_last_deserialize.

    DATA: lv_deserialized_at TYPE zif_abapgit_persistence=>ty_repo-deserialized_at,
          lv_deserialized_by TYPE zif_abapgit_persistence=>ty_repo-deserialized_by.

    GET TIME STAMP FIELD lv_deserialized_at.
    lv_deserialized_by = sy-uname.

    set( iv_deserialized_at = lv_deserialized_at
         iv_deserialized_by = lv_deserialized_by ).

  ENDMETHOD.


  METHOD update_local_checksums.

    " ASSUMTION: SHA1 in param is actual and correct.
    " Push fills it from local files before pushing, deserialize from remote
    " If this is not true that there is an error somewhere but not here

    DATA: lt_checksums TYPE zif_abapgit_persistence=>ty_local_checksum_tt,
          lt_files_idx TYPE zif_abapgit_definitions=>ty_file_signatures_tt,
          lt_local     TYPE zif_abapgit_definitions=>ty_files_item_tt,
          lv_chks_row  TYPE i,
          lv_file_row  TYPE i.

    FIELD-SYMBOLS: <ls_checksum>  LIKE LINE OF lt_checksums,
                   <ls_file>      LIKE LINE OF <ls_checksum>-files,
                   <ls_local>     LIKE LINE OF lt_local,
                   <ls_new_state> LIKE LINE OF it_files.

    lt_checksums = get_local_checksums( ).
    lt_files_idx = it_files.
    SORT lt_files_idx BY path filename. " Sort for binary search

    " Loop through current chacksum state, update sha1 for common files
    LOOP AT lt_checksums ASSIGNING <ls_checksum>.
      lv_chks_row = sy-tabix.

      LOOP AT <ls_checksum>-files ASSIGNING <ls_file>.
        lv_file_row = sy-tabix.

        READ TABLE lt_files_idx ASSIGNING <ls_new_state>
          WITH KEY path = <ls_file>-path filename = <ls_file>-filename
          BINARY SEARCH.
        CHECK sy-subrc = 0. " Missing in param table, skip

        IF <ls_new_state>-sha1 IS INITIAL. " Empty input sha1 is a deletion marker
          DELETE <ls_checksum>-files INDEX lv_file_row.
        ELSE.
          <ls_file>-sha1 = <ls_new_state>-sha1.  " Update sha1
          CLEAR <ls_new_state>-sha1.             " Mark as processed
        ENDIF.
      ENDLOOP.

      IF lines( <ls_checksum>-files ) = 0. " Remove empty objects
        DELETE lt_checksums INDEX lv_chks_row.
      ENDIF.
    ENDLOOP.

    DELETE lt_files_idx WHERE sha1 IS INITIAL. " Remove processed
    IF lines( lt_files_idx ) > 0.
      lt_local = get_files_local( ).
      SORT lt_local BY file-path file-filename. " Sort for binary search
    ENDIF.

    " Add new files - not deleted and not marked as processed above
    LOOP AT lt_files_idx ASSIGNING <ls_new_state>.

      READ TABLE lt_local ASSIGNING <ls_local>
        WITH KEY file-path = <ls_new_state>-path file-filename = <ls_new_state>-filename
        BINARY SEARCH.
      IF sy-subrc <> 0.
* if the deserialization fails, the local file might not be there
        CONTINUE.
      ENDIF.

      READ TABLE lt_checksums ASSIGNING <ls_checksum> " TODO Optimize
        WITH KEY item = <ls_local>-item.
      IF sy-subrc > 0.
        APPEND INITIAL LINE TO lt_checksums ASSIGNING <ls_checksum>.
        <ls_checksum>-item = <ls_local>-item.
      ENDIF.

      APPEND <ls_new_state> TO <ls_checksum>-files.
    ENDLOOP.

    SORT lt_checksums BY item.
    set( it_checksums = lt_checksums ).

  ENDMETHOD.
ENDCLASS.