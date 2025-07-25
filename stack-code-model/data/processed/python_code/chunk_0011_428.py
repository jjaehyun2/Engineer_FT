CLASS zcl_abapgit_gui_view_repo DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.

    INTERFACES zif_abapgit_gui_page .
    INTERFACES zif_abapgit_gui_page_hotkey.

    ALIASES render
      FOR zif_abapgit_gui_page~render .

    CONSTANTS:
      BEGIN OF c_actions,
        change_dir        TYPE string VALUE 'change_dir' ##NO_TEXT,
        toggle_hide_files TYPE string VALUE 'toggle_hide_files' ##NO_TEXT,
        toggle_folders    TYPE string VALUE 'toggle_folders' ##NO_TEXT,
        toggle_changes    TYPE string VALUE 'toggle_changes' ##NO_TEXT,
        display_more      TYPE string VALUE 'display_more' ##NO_TEXT,
      END OF c_actions .

    METHODS constructor
      IMPORTING
        !iv_key TYPE zif_abapgit_persistence=>ty_repo-key
      RAISING
        zcx_abapgit_exception .
  PRIVATE SECTION.

    DATA: mo_repo         TYPE REF TO zcl_abapgit_repo,
          mv_cur_dir      TYPE string,
          mv_hide_files   TYPE abap_bool,
          mv_max_lines    TYPE i,
          mv_max_setting  TYPE i,
          mv_show_folders TYPE abap_bool,
          mv_changes_only TYPE abap_bool.

    METHODS:
      render_head_line
        IMPORTING iv_lstate      TYPE char1
                  iv_rstate      TYPE char1
        RETURNING VALUE(ro_html) TYPE REF TO zcl_abapgit_html
        RAISING   zcx_abapgit_exception,
      build_head_menu
        IMPORTING iv_lstate         TYPE char1
                  iv_rstate         TYPE char1
        RETURNING VALUE(ro_toolbar) TYPE REF TO zcl_abapgit_html_toolbar
        RAISING   zcx_abapgit_exception,
      build_grid_menu
        RETURNING VALUE(ro_toolbar) TYPE REF TO zcl_abapgit_html_toolbar
        RAISING   zcx_abapgit_exception,
      render_item
        IMPORTING is_item        TYPE zif_abapgit_definitions=>ty_repo_item
        RETURNING VALUE(ro_html) TYPE REF TO zcl_abapgit_html
        RAISING   zcx_abapgit_exception,
      render_item_files
        IMPORTING is_item        TYPE zif_abapgit_definitions=>ty_repo_item
        RETURNING VALUE(ro_html) TYPE REF TO zcl_abapgit_html,
      render_item_command
        IMPORTING is_item        TYPE zif_abapgit_definitions=>ty_repo_item
        RETURNING VALUE(ro_html) TYPE REF TO zcl_abapgit_html,
      get_item_class
        IMPORTING is_item        TYPE zif_abapgit_definitions=>ty_repo_item
        RETURNING VALUE(rv_html) TYPE string,
      get_item_icon
        IMPORTING is_item        TYPE zif_abapgit_definitions=>ty_repo_item
        RETURNING VALUE(rv_html) TYPE string,
      render_empty_package
        RETURNING VALUE(rv_html) TYPE string,
      render_parent_dir
        RETURNING VALUE(ro_html) TYPE REF TO zcl_abapgit_html
        RAISING   zcx_abapgit_exception.

    METHODS:
      build_obj_jump_link
        IMPORTING is_item        TYPE zif_abapgit_definitions=>ty_repo_item
        RETURNING VALUE(rv_html) TYPE string,
      build_dir_jump_link
        IMPORTING iv_path        TYPE string
        RETURNING VALUE(rv_html) TYPE string.
ENDCLASS.



CLASS zcl_abapgit_gui_view_repo IMPLEMENTATION.


  METHOD build_dir_jump_link.

    DATA: lv_path   TYPE string,
          lv_encode TYPE string.

    lv_path = iv_path.
    REPLACE FIRST OCCURRENCE OF mv_cur_dir IN lv_path WITH ''.
    lv_encode = zcl_abapgit_html_action_utils=>dir_encode( lv_path ).

    rv_html = zcl_abapgit_html=>a( iv_txt = lv_path
                                   iv_act = |{ c_actions-change_dir }?{ lv_encode }| ).

  ENDMETHOD.


  METHOD build_grid_menu.

    CREATE OBJECT ro_toolbar.

    IF mo_repo->is_offline( ) = abap_false.
      ro_toolbar->add(  " Show/Hide files
        iv_txt = 'Show files'
        iv_chk = boolc( NOT mv_hide_files = abap_true )
        iv_act = c_actions-toggle_hide_files ).

      ro_toolbar->add(  " Show changes only
        iv_txt = 'Show changes only'
        iv_chk = mv_changes_only
        iv_act = c_actions-toggle_changes ).
    ENDIF.

    ro_toolbar->add(  " Show/Hide folders
      iv_txt = 'Show folders'
      iv_chk = mv_show_folders
      iv_act = c_actions-toggle_folders ).

  ENDMETHOD.


  METHOD build_head_menu.

    DATA: lo_tb_advanced TYPE REF TO zcl_abapgit_html_toolbar,
          lo_tb_branch   TYPE REF TO zcl_abapgit_html_toolbar,
          lo_tb_tag      TYPE REF TO zcl_abapgit_html_toolbar,
          lv_key         TYPE zif_abapgit_persistence=>ty_value,
          lv_wp_opt      LIKE zif_abapgit_definitions=>c_html_opt-crossout,
          lv_crossout    LIKE zif_abapgit_definitions=>c_html_opt-crossout,
          lv_pull_opt    LIKE zif_abapgit_definitions=>c_html_opt-crossout.

    CREATE OBJECT ro_toolbar.
    CREATE OBJECT lo_tb_branch.
    CREATE OBJECT lo_tb_advanced.
    CREATE OBJECT lo_tb_tag.

    lv_key = mo_repo->get_key( ).

    IF mo_repo->get_local_settings( )-write_protected = abap_true.
      lv_wp_opt   = zif_abapgit_definitions=>c_html_opt-crossout.
      lv_pull_opt = zif_abapgit_definitions=>c_html_opt-crossout.
    ELSE.
      lv_pull_opt = zif_abapgit_definitions=>c_html_opt-strong.
    ENDIF.

    " Build branch drop-down ========================
    IF mo_repo->is_offline( ) = abap_false. " Online ?
      lo_tb_branch->add( iv_txt = 'Overview'
                         iv_act = |{ zif_abapgit_definitions=>c_action-go_branch_overview }?{ lv_key }| ).
      lo_tb_branch->add( iv_txt = 'Switch'
                         iv_act = |{ zif_abapgit_definitions=>c_action-git_branch_switch }?{ lv_key }|
                         iv_opt = lv_wp_opt ).
      lo_tb_branch->add( iv_txt = 'Create'
                         iv_act = |{ zif_abapgit_definitions=>c_action-git_branch_create }?{ lv_key }| ).
      lo_tb_branch->add( iv_txt = 'Delete'
                         iv_act = |{ zif_abapgit_definitions=>c_action-git_branch_delete }?{ lv_key }| ).

      lo_tb_tag->add( iv_txt = 'Overview'
                      iv_act = |{ zif_abapgit_definitions=>c_action-go_tag_overview }?{ lv_key }| ).
      lo_tb_tag->add( iv_txt = 'Switch'
                      iv_act = |{ zif_abapgit_definitions=>c_action-git_tag_switch }?{ lv_key }|
                      iv_opt = lv_wp_opt ).
      lo_tb_tag->add( iv_txt = 'Create'
                      iv_act = |{ zif_abapgit_definitions=>c_action-git_tag_create }?{ lv_key }| ).
      lo_tb_tag->add( iv_txt = 'Delete'
                      iv_act = |{ zif_abapgit_definitions=>c_action-git_tag_delete }?{ lv_key }| ).

    ENDIF.

    " Build advanced drop-down ========================
    IF mo_repo->is_offline( ) = abap_false. " Online ?
      lo_tb_advanced->add( iv_txt = 'Reset local'
                           iv_act = |{ zif_abapgit_definitions=>c_action-git_reset }?{ lv_key }|
                           iv_opt = lv_wp_opt ).
      lo_tb_advanced->add( iv_txt = 'Background mode'
                           iv_act = |{ zif_abapgit_definitions=>c_action-go_background }?{ lv_key }| ).
      lo_tb_advanced->add( iv_txt = 'Change remote'
                           iv_act = |{ zif_abapgit_definitions=>c_action-repo_remote_change }?{ lv_key }| ).
      lo_tb_advanced->add( iv_txt = 'Make off-line'
                           iv_act = |{ zif_abapgit_definitions=>c_action-repo_remote_detach }?{ lv_key }| ).
      lo_tb_advanced->add( iv_txt = 'Force stage'
                           iv_act = |{ zif_abapgit_definitions=>c_action-go_stage }?{ lv_key }| ).

      CLEAR lv_crossout.
      IF zcl_abapgit_auth=>is_allowed( zif_abapgit_auth=>gc_authorization-transport_to_branch ) = abap_false.
        lv_crossout = zif_abapgit_definitions=>c_html_opt-crossout.
      ENDIF.
      lo_tb_advanced->add( iv_txt = 'Transport to Branch'
                           iv_act = |{ zif_abapgit_definitions=>c_action-repo_transport_to_branch }?{ lv_key }|
                           iv_opt = lv_crossout ).

    ELSE.
      lo_tb_advanced->add( iv_txt = 'Make on-line'
                           iv_act = |{ zif_abapgit_definitions=>c_action-repo_remote_attach }?{ lv_key }| ).
    ENDIF.
    lo_tb_advanced->add( iv_txt = 'Syntax Check'
                         iv_act = |{ zif_abapgit_definitions=>c_action-repo_syntax_check }?{ lv_key }| ).
    lo_tb_advanced->add( iv_txt = 'Run Code Inspector'
                         iv_act = |{ zif_abapgit_definitions=>c_action-repo_code_inspector }?{ lv_key }| ).
    lo_tb_advanced->add( iv_txt = 'Repo settings'
                         iv_act = |{ zif_abapgit_definitions=>c_action-repo_settings }?{ lv_key }| ).

    CLEAR lv_crossout.
    IF zcl_abapgit_auth=>is_allowed( zif_abapgit_auth=>gc_authorization-update_local_checksum ) = abap_false.
      lv_crossout = zif_abapgit_definitions=>c_html_opt-crossout.
    ENDIF.
    lo_tb_advanced->add( iv_txt = 'Update local checksums'
                         iv_act = |{ zif_abapgit_definitions=>c_action-repo_refresh_checksums }?{ lv_key }|
                         iv_opt = lv_crossout ).

    lo_tb_advanced->add( iv_txt = 'Remove'
                         iv_act = |{ zif_abapgit_definitions=>c_action-repo_remove }?{ lv_key }| ).

    CLEAR lv_crossout.
    IF mo_repo->get_local_settings( )-write_protected = abap_true
        OR zcl_abapgit_auth=>is_allowed( zif_abapgit_auth=>gc_authorization-uninstall ) = abap_false.
      lv_crossout = zif_abapgit_definitions=>c_html_opt-crossout.
    ENDIF.
    lo_tb_advanced->add( iv_txt = 'Uninstall'
                         iv_act = |{ zif_abapgit_definitions=>c_action-repo_purge }?{ lv_key }|
                         iv_opt = lv_crossout ).

    " Build main toolbar ==============================
    IF mo_repo->is_offline( ) = abap_false. " Online ?
      TRY.
          IF iv_rstate IS NOT INITIAL. " Something new at remote
            ro_toolbar->add( iv_txt = 'Pull'
                             iv_act = |{ zif_abapgit_definitions=>c_action-git_pull }?{ lv_key }|
                             iv_opt = lv_pull_opt ).
          ENDIF.
          IF iv_lstate IS NOT INITIAL. " Something new at local
            ro_toolbar->add( iv_txt = 'Stage'
                             iv_act = |{ zif_abapgit_definitions=>c_action-go_stage }?{ lv_key }|
                             iv_opt = zif_abapgit_definitions=>c_html_opt-strong ).
          ENDIF.
          IF iv_rstate IS NOT INITIAL OR iv_lstate IS NOT INITIAL. " Any changes
            ro_toolbar->add( iv_txt = 'Show diff'
                             iv_act = |{ zif_abapgit_definitions=>c_action-go_diff }?key={ lv_key }|
                             iv_opt = zif_abapgit_definitions=>c_html_opt-strong ).
          ENDIF.
        CATCH zcx_abapgit_exception ##NO_HANDLER.
          " authorization error or repository does not exist
          " ignore error
      ENDTRY.
      ro_toolbar->add( iv_txt = 'Branch'
                       io_sub = lo_tb_branch ) ##NO_TEXT.
      ro_toolbar->add( iv_txt = 'Tag'
                       io_sub = lo_tb_tag ) ##NO_TEXT.
    ELSE.
      ro_toolbar->add( iv_txt = 'Import ZIP'
                       iv_act = |{ zif_abapgit_definitions=>c_action-zip_import }?{ lv_key }|
                       iv_opt = zif_abapgit_definitions=>c_html_opt-strong ).
      ro_toolbar->add( iv_txt = 'Export ZIP'
                       iv_act = |{ zif_abapgit_definitions=>c_action-zip_export }?{ lv_key }|
                       iv_opt = zif_abapgit_definitions=>c_html_opt-strong ).
    ENDIF.

    ro_toolbar->add( iv_txt = 'Advanced'
                     io_sub = lo_tb_advanced ) ##NO_TEXT.
    ro_toolbar->add( iv_txt = 'Refresh'
                     iv_act = |{ zif_abapgit_definitions=>c_action-repo_refresh }?{ lv_key }| ).
    ro_toolbar->add( iv_txt = zcl_abapgit_html=>icon( iv_name = 'settings/grey70' )
                     io_sub = build_grid_menu( ) ).

  ENDMETHOD.


  METHOD build_obj_jump_link.

    DATA: lv_encode TYPE string.

    lv_encode = zcl_abapgit_html_action_utils=>jump_encode( iv_obj_type = is_item-obj_type
                                                    iv_obj_name = is_item-obj_name ).

    rv_html = zcl_abapgit_html=>a( iv_txt = |{ is_item-obj_name }|
                                   iv_act = |{ zif_abapgit_definitions=>c_action-jump }?{ lv_encode }| ).

  ENDMETHOD.


  METHOD constructor.

    DATA lo_settings TYPE REF TO zcl_abapgit_settings.

    super->constructor( ).

    mo_repo         = zcl_abapgit_repo_srv=>get_instance( )->get( iv_key ).
    mv_cur_dir      = '/'. " Root
    mv_hide_files   = zcl_abapgit_persistence_user=>get_instance( )->get_hide_files( ).
    mv_changes_only = zcl_abapgit_persistence_user=>get_instance( )->get_changes_only( ).

    " Read global settings to get max # of objects to be listed
    lo_settings     = zcl_abapgit_persist_settings=>get_instance( )->read( ).
    mv_max_lines    = lo_settings->get_max_lines( ).
    mv_max_setting  = mv_max_lines.

  ENDMETHOD.


  METHOD get_item_class.

    DATA lt_class TYPE TABLE OF string.

    IF is_item-is_dir = abap_true.
      APPEND 'folder' TO lt_class.
    ELSEIF is_item-changes > 0.
      APPEND 'modified' TO lt_class.
    ELSEIF is_item-obj_name IS INITIAL.
      APPEND 'unsupported' TO lt_class.
    ENDIF.

    IF lines( lt_class ) > 0.
      rv_html = | class="{ concat_lines_of( table = lt_class sep = ` ` ) }"|.
    ENDIF.

  ENDMETHOD.


  METHOD get_item_icon.

    CASE is_item-obj_type.
      WHEN 'PROG' OR 'CLAS' OR 'FUGR'.
        rv_html = zcl_abapgit_html=>icon( 'file-code/darkgrey' ).
      WHEN 'W3MI' OR 'W3HT'.
        rv_html = zcl_abapgit_html=>icon( 'file-binary/darkgrey' ).
      WHEN ''.
        rv_html = space. " no icon
      WHEN OTHERS.
        rv_html = zcl_abapgit_html=>icon( 'file/darkgrey' ).
    ENDCASE.

    IF is_item-is_dir = abap_true.
      rv_html = zcl_abapgit_html=>icon( 'file-directory/darkgrey' ).
    ENDIF.

  ENDMETHOD.


  METHOD render_empty_package.

    DATA: lv_text TYPE string.

    IF mv_changes_only = abap_true.
      lv_text = |No changes|.
    ELSE.
      lv_text = |Empty package|.
    ENDIF.

    rv_html = |<tr class="unsupported"><td class="paddings">|
           && |  <center>{ lv_text }</center>|
           && |</td></tr>|.

  ENDMETHOD.


  METHOD render_head_line.

    DATA lo_toolbar TYPE REF TO zcl_abapgit_html_toolbar.

    CREATE OBJECT ro_html.
    lo_toolbar = build_head_menu( iv_lstate = iv_lstate iv_rstate = iv_rstate ).

    ro_html->add( '<div class="paddings">' ).
    ro_html->add( '<table class="w100"><tr>' ).

    IF mv_show_folders = abap_true.
      ro_html->add( |<td class="current_dir">{ mv_cur_dir }</td>| ).
    ENDIF.

    ro_html->add( '<td class="right">' ).
    ro_html->add( lo_toolbar->render( iv_right = abap_true ) ).
    ro_html->add( '</td>' ).
    ro_html->add( '</tr></table>' ).
    ro_html->add( '</div>' ).

  ENDMETHOD.


  METHOD render_item.

    DATA: lv_link TYPE string.

    CREATE OBJECT ro_html.


    ro_html->add( |<tr{ get_item_class( is_item ) }>| ).

    IF is_item-obj_name IS INITIAL AND is_item-is_dir = abap_false.
      ro_html->add( '<td colspan="2"></td>'
                 && '<td class="object">'
                 && '<i class="grey">non-code and meta files</i>'
                 && '</td>' ).
    ELSE.
      ro_html->add( |<td class="icon">{ get_item_icon( is_item ) }</td>| ).

      IF is_item-is_dir = abap_true. " Subdir
        lv_link = build_dir_jump_link( is_item-path ).
        ro_html->add( |<td class="dir" colspan="2">{ lv_link }</td>| ).
      ELSE.
        lv_link = build_obj_jump_link( is_item ).
        ro_html->add( |<td class="type">{ is_item-obj_type }</td>| ).
        ro_html->add( |<td class="object">{ lv_link }</td>| ).
      ENDIF.
    ENDIF.

    IF mo_repo->is_offline( ) = abap_false.

      " Files
      ro_html->add( '<td class="files">' ).
      ro_html->add( render_item_files( is_item ) ).
      ro_html->add( '</td>' ).

      " Command
      ro_html->add( '<td class="cmd">' ).
      ro_html->add( render_item_command( is_item ) ).
      ro_html->add( '</td>' ).

    ENDIF.

    ro_html->add( '</tr>' ).

  ENDMETHOD.


  METHOD render_item_command.

    DATA: lv_difflink TYPE string,
          ls_file     LIKE LINE OF is_item-files.

    CREATE OBJECT ro_html.

    IF is_item-is_dir = abap_true. " Directory

      ro_html->add( '<div>' ).
      ro_html->add( |<span class="grey">{ is_item-changes } changes</span>| ).
      ro_html->add( zcl_abapgit_gui_chunk_lib=>render_item_state( iv_lstate = is_item-lstate
                                                          iv_rstate = is_item-rstate ) ).
      ro_html->add( '</div>' ).

    ELSEIF is_item-changes > 0.

      IF mv_hide_files = abap_true AND is_item-obj_name IS NOT INITIAL.

        lv_difflink = zcl_abapgit_html_action_utils=>obj_encode(
          iv_key    = mo_repo->get_key( )
          ig_object = is_item ).

        ro_html->add( '<div>' ).
        ro_html->add_a( iv_txt = |view diff ({ is_item-changes })|
                        iv_act = |{ zif_abapgit_definitions=>c_action-go_diff }?{ lv_difflink }| ).
        ro_html->add( zcl_abapgit_gui_chunk_lib=>render_item_state( iv_lstate = is_item-lstate
                                                            iv_rstate = is_item-rstate ) ).
        ro_html->add( '</div>' ).

      ELSE.
        LOOP AT is_item-files INTO ls_file.

          ro_html->add( '<div>' ).
          IF ls_file-is_changed = abap_true.
            lv_difflink = zcl_abapgit_html_action_utils=>file_encode(
              iv_key  = mo_repo->get_key( )
              ig_file = ls_file ).
            ro_html->add_a( iv_txt = 'view diff'
                            iv_act = |{ zif_abapgit_definitions=>c_action-go_diff }?{ lv_difflink }| ).
            ro_html->add( zcl_abapgit_gui_chunk_lib=>render_item_state( iv_lstate = ls_file-lstate
                                                                iv_rstate = ls_file-rstate ) ).
          ELSE.
            ro_html->add( '&nbsp;' ).
          ENDIF.
          ro_html->add( '</div>' ).

        ENDLOOP.
      ENDIF.

    ENDIF.

  ENDMETHOD.


  METHOD render_item_files.

    DATA: ls_file     LIKE LINE OF is_item-files.

    CREATE OBJECT ro_html.

    IF mv_hide_files = abap_true AND is_item-obj_type IS NOT INITIAL.
      RETURN.
    ENDIF.

    LOOP AT is_item-files INTO ls_file.
      ro_html->add( |<div>{ ls_file-path && ls_file-filename }</div>| ).
    ENDLOOP.

  ENDMETHOD.


  METHOD render_parent_dir.

    CREATE OBJECT ro_html.

    ro_html->add( '<tr class="folder">' ).
    ro_html->add( |<td class="icon">{ zcl_abapgit_html=>icon( 'dir' ) }</td>| ).
    ro_html->add( |<td class="object" colspan="2">{ build_dir_jump_link( '..' ) }</td>| ).
    IF mo_repo->is_offline( ) = abap_false.
      ro_html->add( |<td colspan="2"></td>| ). " Dummy for online
    ENDIF.
    ro_html->add( '</tr>' ).

  ENDMETHOD.


  METHOD zif_abapgit_gui_page~on_event.

    DATA: lv_path TYPE string.

    CASE iv_action.
      WHEN c_actions-toggle_hide_files. " Toggle file diplay
        mv_hide_files   = zcl_abapgit_persistence_user=>get_instance( )->toggle_hide_files( ).
        ev_state        = zif_abapgit_definitions=>c_event_state-re_render.
      WHEN c_actions-change_dir.        " Change dir
        lv_path         = zcl_abapgit_html_action_utils=>dir_decode( iv_getdata ).
        mv_cur_dir      = zcl_abapgit_path=>change_dir( iv_cur_dir = mv_cur_dir iv_cd = lv_path ).
        ev_state        = zif_abapgit_definitions=>c_event_state-re_render.
      WHEN c_actions-toggle_folders.    " Toggle folder view
        mv_show_folders = boolc( mv_show_folders <> abap_true ).
        mv_cur_dir      = '/'. " Root
        ev_state        = zif_abapgit_definitions=>c_event_state-re_render.
      WHEN c_actions-toggle_changes.    " Toggle changes only view
        mv_changes_only = zcl_abapgit_persistence_user=>get_instance( )->toggle_changes_only( ).
        ev_state        = zif_abapgit_definitions=>c_event_state-re_render.
      WHEN c_actions-display_more.      " Increase MAX lines limit
        mv_max_lines    = mv_max_lines + mv_max_setting.
        ev_state        = zif_abapgit_definitions=>c_event_state-re_render.
    ENDCASE.

  ENDMETHOD.


  METHOD zif_abapgit_gui_page~render.

    DATA: lt_repo_items TYPE zif_abapgit_definitions=>tt_repo_items,
          lo_browser    TYPE REF TO zcl_abapgit_repo_content_list,
          lx_error      TYPE REF TO zcx_abapgit_exception,
          lv_lstate     TYPE char1,
          lv_rstate     TYPE char1,
          lv_max        TYPE abap_bool,
          lv_max_str    TYPE string,
          lv_add_str    TYPE string,
          lo_log        TYPE REF TO zcl_abapgit_log.

    FIELD-SYMBOLS <ls_item> LIKE LINE OF lt_repo_items.

    " Reinit, for the case of type change
    mo_repo = zcl_abapgit_repo_srv=>get_instance( )->get( mo_repo->get_key( ) ).

    CREATE OBJECT ro_html.

    TRY.

        CREATE OBJECT lo_browser
          EXPORTING
            io_repo = mo_repo.

        lt_repo_items = lo_browser->list( iv_path         = mv_cur_dir
                                          iv_by_folders   = mv_show_folders
                                          iv_changes_only = mv_changes_only ).

        LOOP AT lt_repo_items ASSIGNING <ls_item>.
          zcl_abapgit_state=>reduce( EXPORTING iv_cur = <ls_item>-lstate
                                     CHANGING cv_prev = lv_lstate ).
          zcl_abapgit_state=>reduce( EXPORTING iv_cur = <ls_item>-rstate
                                     CHANGING cv_prev = lv_rstate ).
        ENDLOOP.

        ro_html->add( render_head_line( iv_lstate = lv_lstate
                                        iv_rstate = lv_rstate ) ).

        lo_log = lo_browser->get_log( ).
        IF mo_repo->is_offline( ) = abap_false AND lo_log->count( ) > 0.
          ro_html->add( '<div class="log">' ).
          ro_html->add( lo_log->to_html( ) ). " shows eg. list of unsupported objects
          ro_html->add( '</div>' ).
        ENDIF.

        ro_html->add( '<div class="repo_container">' ).

        " Repo content table
        ro_html->add( '<table class="repo_tab">' ).

        IF zcl_abapgit_path=>is_root( mv_cur_dir ) = abap_false.
          ro_html->add( render_parent_dir( ) ).
        ENDIF.

        IF lines( lt_repo_items ) = 0.
          ro_html->add( render_empty_package( ) ).
        ELSE.
          LOOP AT lt_repo_items ASSIGNING <ls_item>.
            IF mv_max_lines > 0 AND sy-tabix > mv_max_lines.
              lv_max = abap_true.
              EXIT. " current loop
            ENDIF.
            ro_html->add( render_item( <ls_item> ) ).
          ENDLOOP.
        ENDIF.

        ro_html->add( '</table>' ).

        IF lv_max = abap_true.
          ro_html->add( '<div class = "dummydiv">' ).
          IF mv_max_lines = 1.
            lv_max_str = '1 object'.
          ELSE.
            lv_max_str = |first { mv_max_lines } objects|.
          ENDIF.
          lv_add_str = |+{ mv_max_setting }|.
          ro_html->add( |Only { lv_max_str } shown in list. Display {
            zcl_abapgit_html=>a( iv_txt = lv_add_str iv_act = c_actions-display_more )
            } more. (Set in Advanced > {
            zcl_abapgit_html=>a( iv_txt = 'Settings' iv_act = zif_abapgit_definitions=>c_action-go_settings )
            } )| ).
          ro_html->add( '</div>' ).
        ENDIF.

        ro_html->add( '</div>' ).

      CATCH zcx_abapgit_exception INTO lx_error.
        ro_html->add( render_head_line( iv_lstate = lv_lstate iv_rstate = lv_rstate ) ).
        ro_html->add( zcl_abapgit_gui_chunk_lib=>render_error( ix_error = lx_error ) ).
    ENDTRY.

  ENDMETHOD.


  METHOD zif_abapgit_gui_page_hotkey~get_hotkey_actions.

  ENDMETHOD.

ENDCLASS.