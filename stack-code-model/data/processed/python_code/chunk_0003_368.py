CLASS zcl_abapgit_repo_online DEFINITION
  PUBLIC
  INHERITING FROM zcl_abapgit_repo
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.

    METHODS constructor
      IMPORTING
        !is_data TYPE zif_abapgit_persistence=>ty_repo
      RAISING
        zcx_abapgit_exception .
    METHODS get_url
      RETURNING
        VALUE(rv_url) TYPE zif_abapgit_persistence=>ty_repo-url .
    METHODS get_branch_name
      RETURNING
        VALUE(rv_name) TYPE zif_abapgit_persistence=>ty_repo-branch_name .
    METHODS get_head_branch_name
      RETURNING
        VALUE(rv_name) TYPE zif_abapgit_persistence=>ty_repo-head_branch .
    METHODS set_url
      IMPORTING
        !iv_url TYPE zif_abapgit_persistence=>ty_repo-url
      RAISING
        zcx_abapgit_exception .
    METHODS set_branch_name
      IMPORTING
        !iv_branch_name TYPE zif_abapgit_persistence=>ty_repo-branch_name
      RAISING
        zcx_abapgit_exception .
    METHODS set_new_remote
      IMPORTING
        !iv_url         TYPE zif_abapgit_persistence=>ty_repo-url
        !iv_branch_name TYPE zif_abapgit_persistence=>ty_repo-branch_name
      RAISING
        zcx_abapgit_exception .
    METHODS get_sha1_local
      RETURNING
        VALUE(rv_sha1) TYPE zif_abapgit_persistence=>ty_repo-sha1 .
    METHODS get_sha1_remote
      RETURNING
        VALUE(rv_sha1) TYPE zif_abapgit_persistence=>ty_repo-sha1
      RAISING
        zcx_abapgit_exception .
    METHODS get_objects
      RETURNING
        VALUE(rt_objects) TYPE zif_abapgit_definitions=>ty_objects_tt
      RAISING
        zcx_abapgit_exception .
    METHODS status
      IMPORTING
        !io_log           TYPE REF TO zcl_abapgit_log OPTIONAL
      RETURNING
        VALUE(rt_results) TYPE zif_abapgit_definitions=>ty_results_tt
      RAISING
        zcx_abapgit_exception .
    METHODS reset_status .
    METHODS set_objects
      IMPORTING
        !it_objects TYPE zif_abapgit_definitions=>ty_objects_tt
      RAISING
        zcx_abapgit_exception .
    METHODS initialize
      RAISING
        zcx_abapgit_exception .
    METHODS push
      IMPORTING
        !is_comment TYPE zif_abapgit_definitions=>ty_comment
        !io_stage   TYPE REF TO zcl_abapgit_stage
      RAISING
        zcx_abapgit_exception .
    METHODS get_unnecessary_local_objs
      RETURNING
        VALUE(rt_unnecessary_local_objects) TYPE zif_abapgit_definitions=>ty_tadir_tt
      RAISING
        zcx_abapgit_exception .

    METHODS deserialize
        REDEFINITION .
    METHODS get_files_remote
        REDEFINITION .
    METHODS rebuild_local_checksums
        REDEFINITION .
    METHODS refresh
        REDEFINITION .
  PRIVATE SECTION.
    DATA:
      mt_objects     TYPE zif_abapgit_definitions=>ty_objects_tt,
      mv_branch      TYPE zif_abapgit_definitions=>ty_sha1,
      mv_initialized TYPE abap_bool,
      mo_branches    TYPE REF TO zcl_abapgit_git_branch_list,
      mt_status      TYPE zif_abapgit_definitions=>ty_results_tt.

    METHODS:
      handle_stage_ignore
        IMPORTING io_stage TYPE REF TO zcl_abapgit_stage
        RAISING   zcx_abapgit_exception,
      actualize_head_branch
        RAISING zcx_abapgit_exception,
      delete_initial_online_repo
        IMPORTING iv_commit TYPE flag
        RAISING   zcx_abapgit_exception.

ENDCLASS.



CLASS zcl_abapgit_repo_online IMPLEMENTATION.


  METHOD actualize_head_branch.
    DATA lv_branch_name TYPE string.
    lv_branch_name = mo_branches->get_head( )-name.

    IF lv_branch_name <> ms_data-head_branch.
      set( iv_head_branch = lv_branch_name ).
    ENDIF.

  ENDMETHOD.                    "actualize_head_branch


  METHOD constructor.

    super->constructor( is_data ).

    mv_initialized = abap_false.

  ENDMETHOD.                    "constructor


  METHOD delete_initial_online_repo.

    IF me->is_offline( ) = abap_false AND me->get_sha1_local( ) IS INITIAL.

      zcl_abapgit_repo_srv=>get_instance( )->delete( me ).

      IF iv_commit = abap_true.
        COMMIT WORK.
      ENDIF.

    ENDIF.

  ENDMETHOD.  " delete_initial_online_repo


  METHOD deserialize.

    initialize( ).

    super->deserialize( is_checks ).

    set( iv_sha1 = mv_branch ).

    reset_status( ).

    COMMIT WORK AND WAIT.

  ENDMETHOD.                    "deserialize


  METHOD get_branch_name.
    rv_name = ms_data-branch_name.
  ENDMETHOD.                    "get_branch_name


  METHOD get_files_remote.
    initialize( ).

    rt_files = mt_remote.
  ENDMETHOD.                    "get_files


  METHOD get_head_branch_name.
    rv_name = ms_data-head_branch.
  ENDMETHOD.                    "get_head_branch_name


  METHOD get_objects.
    initialize( ).

    rt_objects = mt_objects.
  ENDMETHOD.                    "get_objects


  METHOD get_sha1_local.
    rv_sha1 = ms_data-sha1.
  ENDMETHOD.                    "get_sha1_local


  METHOD get_sha1_remote.
    initialize( ).

    rv_sha1 = mv_branch.
  ENDMETHOD.                    "get_sha1_remote


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

    lv_package = me->get_package( ).
    lt_tadir = zcl_abapgit_tadir=>read( lv_package ).
    SORT lt_tadir BY pgmid ASCENDING object ASCENDING obj_name ASCENDING devclass ASCENDING.

    LOOP AT lt_status ASSIGNING <ls_status>
                      WHERE lstate = zif_abapgit_definitions=>gc_state-added.

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


  METHOD get_url.
    rv_url = ms_data-url.
  ENDMETHOD.                    "get_url


  METHOD handle_stage_ignore.

    DATA: lv_add         TYPE abap_bool,
          lo_dot_abapgit TYPE REF TO zcl_abapgit_dot_abapgit,
          lt_stage       TYPE zcl_abapgit_stage=>ty_stage_tt.

    FIELD-SYMBOLS: <ls_stage> LIKE LINE OF lt_stage.


    lo_dot_abapgit = get_dot_abapgit( ).
    lt_stage = io_stage->get_all( ).
    LOOP AT lt_stage ASSIGNING <ls_stage> WHERE method = zcl_abapgit_stage=>c_method-ignore.

      lo_dot_abapgit->add_ignore(
        iv_path     = <ls_stage>-file-path
        iv_filename = <ls_stage>-file-filename ).

      " remove it from the staging object, as the action is handled here
      io_stage->reset( iv_path     = <ls_stage>-file-path
                       iv_filename = <ls_stage>-file-filename ).

      lv_add = abap_true.

    ENDLOOP.

    IF lv_add = abap_true.
      io_stage->add(
        iv_path     = zif_abapgit_definitions=>gc_root_dir
        iv_filename = zif_abapgit_definitions=>gc_dot_abapgit
        iv_data     = lo_dot_abapgit->serialize( ) ).

      set_dot_abapgit( lo_dot_abapgit ).
    ENDIF.

  ENDMETHOD.


  METHOD initialize.
    IF mv_initialized = abap_false.
      refresh( ).
    ENDIF.
  ENDMETHOD.


  METHOD push.

    DATA: lv_branch        TYPE zif_abapgit_definitions=>ty_sha1,
          lt_updated_files TYPE zif_abapgit_definitions=>ty_file_signatures_tt,
          lv_text          TYPE string.

    IF ms_data-branch_name CP 'refs/tags*'.
      lv_text = |You're working on a tag. Currently it's not |
             && |possible to push on tags. Consider creating a branch instead|.
      zcx_abapgit_exception=>raise( lv_text ).
    ENDIF.

    handle_stage_ignore( io_stage ).

    zcl_abapgit_git_porcelain=>push( EXPORTING is_comment       = is_comment
                                       io_repo          = me
                                       io_stage         = io_stage
                             IMPORTING ev_branch        = lv_branch
                                       et_updated_files = lt_updated_files ).

    IF io_stage->get_branch_sha1( ) = get_sha1_local( ).
* pushing to the branch currently represented by this repository object
      mv_branch = lv_branch.
      set( iv_sha1 = lv_branch ).
    ELSE.
      refresh( ).
    ENDIF.

    update_local_checksums( lt_updated_files ).

    IF zcl_abapgit_stage_logic=>count( me ) = 0.
      set( iv_sha1 = lv_branch ).
    ENDIF.

  ENDMETHOD.                    "push


  METHOD rebuild_local_checksums. "REMOTE

    DATA: lt_remote       TYPE zif_abapgit_definitions=>ty_files_tt,
          lt_local        TYPE zif_abapgit_definitions=>ty_files_item_tt,
          ls_last_item    TYPE zif_abapgit_definitions=>ty_item,
          lv_branch_equal TYPE abap_bool,
          lt_checksums    TYPE zif_abapgit_persistence=>ty_local_checksum_tt.

    FIELD-SYMBOLS: <ls_checksum> LIKE LINE OF lt_checksums,
                   <ls_file_sig> LIKE LINE OF <ls_checksum>-files,
                   <ls_remote>   LIKE LINE OF lt_remote,
                   <ls_local>    LIKE LINE OF lt_local.

    lt_remote       = get_files_remote( ).
    lt_local        = get_files_local( ).
    lv_branch_equal = boolc( get_sha1_remote( ) = get_sha1_local( ) ).

    DELETE lt_local " Remove non-code related files except .abapgit
      WHERE item IS INITIAL
      AND NOT ( file-path     = zif_abapgit_definitions=>gc_root_dir
      AND       file-filename = zif_abapgit_definitions=>gc_dot_abapgit ).

    SORT lt_local BY item.
    SORT lt_remote BY path filename.

    LOOP AT lt_local ASSIGNING <ls_local>.
      IF ls_last_item <> <ls_local>-item OR sy-tabix = 1. " First or New item reached ?
        APPEND INITIAL LINE TO lt_checksums ASSIGNING <ls_checksum>.
        <ls_checksum>-item = <ls_local>-item.
        ls_last_item       = <ls_local>-item.
      ENDIF.

      READ TABLE lt_remote ASSIGNING <ls_remote>
        WITH KEY path = <ls_local>-file-path filename = <ls_local>-file-filename
        BINARY SEARCH.
      CHECK sy-subrc = 0.  " Ignore new ones

      APPEND INITIAL LINE TO <ls_checksum>-files ASSIGNING <ls_file_sig>.
      MOVE-CORRESPONDING <ls_local>-file TO <ls_file_sig>.

      " If hashes are equal -> local sha1 is OK
      " Else if R-branch is ahead  -> assume changes were remote, state - local sha1
      "      Else (branches equal) -> assume changes were local, state - remote sha1
      IF <ls_local>-file-sha1 <> <ls_remote>-sha1 AND lv_branch_equal = abap_true.
        <ls_file_sig>-sha1 = <ls_remote>-sha1.
      ENDIF.
    ENDLOOP.

    set( it_checksums = lt_checksums ).
    reset_status( ).

  ENDMETHOD.  " rebuild_local_checksums.


  METHOD refresh.

    DATA: lo_progress  TYPE REF TO zcl_abapgit_progress,
          lx_exception TYPE REF TO zcx_abapgit_exception.

    super->refresh( iv_drop_cache ).
    reset_status( ).

    CREATE OBJECT lo_progress
      EXPORTING
        iv_total = 1.

    lo_progress->show( iv_current = 1
                       iv_text    = 'Fetch remote files' ) ##NO_TEXT.

    TRY.
        zcl_abapgit_git_porcelain=>pull(
          EXPORTING
            io_repo    = me
          IMPORTING
            et_files   = mt_remote
            et_objects = mt_objects
            ev_branch  = mv_branch ).

      CATCH zcx_abapgit_exception INTO lx_exception.

        delete_initial_online_repo( abap_true ).

        RAISE EXCEPTION lx_exception.

    ENDTRY.

    mo_branches = zcl_abapgit_git_transport=>branches( get_url( ) ).
    actualize_head_branch( ).

    mv_initialized = abap_true.

  ENDMETHOD.                    "refresh


  METHOD reset_status.
    CLEAR mt_status.
  ENDMETHOD.  " reset_status.


  METHOD set_branch_name.

    IF ms_data-local_settings-write_protected = abap_true.
      zcx_abapgit_exception=>raise( 'Cannot switch branch. Local code is write-protected by repo config' ).
    ENDIF.

    mv_initialized = abap_false.
    set( iv_branch_name = iv_branch_name ).

  ENDMETHOD.


  METHOD set_new_remote.

    IF ms_data-local_settings-write_protected = abap_true.
      zcx_abapgit_exception=>raise( 'Cannot change remote. Local code is write-protected by repo config' ).
    ENDIF.

    mv_initialized = abap_false.
    set( iv_url         = iv_url
         iv_branch_name = iv_branch_name
         iv_head_branch = ''
         iv_sha1        = '' ).

  ENDMETHOD.  "set_new_remote


  METHOD set_objects.
    mt_objects = it_objects.
  ENDMETHOD.


  METHOD set_url.

    IF ms_data-local_settings-write_protected = abap_true.
      zcx_abapgit_exception=>raise( 'Cannot change URL. Local code is write-protected by repo config' ).
    ENDIF.

    mv_initialized = abap_false.
    set( iv_url = iv_url ).

  ENDMETHOD.


  METHOD status.

    initialize( ).

    IF lines( mt_status ) = 0.
      mt_status = zcl_abapgit_file_status=>status( io_repo = me
                                                   io_log  = io_log ).
    ENDIF.
    rt_results = mt_status.

  ENDMETHOD.                    "status
ENDCLASS.