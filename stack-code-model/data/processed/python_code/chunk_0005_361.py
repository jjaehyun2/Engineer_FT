CLASS zcl_abapgit_gui_chunk_lib DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.

    CLASS-METHODS render_error
      IMPORTING
        !ix_error      TYPE REF TO zcx_abapgit_exception OPTIONAL
        !iv_error      TYPE string OPTIONAL
      RETURNING
        VALUE(ro_html) TYPE REF TO zcl_abapgit_html .
    CLASS-METHODS render_repo_top
      IMPORTING
        !io_repo               TYPE REF TO zcl_abapgit_repo
        !iv_show_package       TYPE abap_bool DEFAULT abap_true
        !iv_show_branch        TYPE abap_bool DEFAULT abap_true
        !iv_interactive_branch TYPE abap_bool DEFAULT abap_false
        !iv_branch             TYPE string OPTIONAL
        !io_news               TYPE REF TO zcl_abapgit_news OPTIONAL
      RETURNING
        VALUE(ro_html)         TYPE REF TO zcl_abapgit_html
      RAISING
        zcx_abapgit_exception .
    CLASS-METHODS render_item_state
      IMPORTING
        !iv_lstate     TYPE char1
        !iv_rstate     TYPE char1
      RETURNING
        VALUE(rv_html) TYPE string .
    CLASS-METHODS render_js_error_banner
      RETURNING
        VALUE(ro_html) TYPE REF TO zcl_abapgit_html
      RAISING
        zcx_abapgit_exception .
    CLASS-METHODS render_news
      IMPORTING
        !io_news       TYPE REF TO zcl_abapgit_news
      RETURNING
        VALUE(ro_html) TYPE REF TO zcl_abapgit_html
      RAISING
        zcx_abapgit_exception .
    CLASS-METHODS render_hotkey_overview
      IMPORTING
        !io_page       TYPE REF TO zcl_abapgit_gui_page
      RETURNING
        VALUE(ro_html) TYPE REF TO zcl_abapgit_html
      RAISING
        zcx_abapgit_exception .
    CLASS-METHODS render_commit_popup
      IMPORTING
        iv_content     TYPE csequence
        iv_id          TYPE csequence
      RETURNING
        VALUE(ro_html) TYPE REF TO zcl_abapgit_html
      RAISING
        zcx_abapgit_exception .
    CLASS-METHODS render_error_message_box
      IMPORTING
        ix_error       TYPE REF TO zcx_abapgit_exception
      RETURNING
        VALUE(ro_html) TYPE REF TO zcl_abapgit_html.
  PROTECTED SECTION.
  PRIVATE SECTION.

    CLASS-METHODS render_branch_span
      IMPORTING
        !iv_branch      TYPE string
        !io_repo        TYPE REF TO zcl_abapgit_repo_online
        !iv_interactive TYPE abap_bool
      RETURNING
        VALUE(ro_html)  TYPE REF TO zcl_abapgit_html
      RAISING
        zcx_abapgit_exception .
    CLASS-METHODS render_infopanel
      IMPORTING
        iv_div_id      TYPE string
        iv_title       TYPE string
        iv_hide        TYPE abap_bool DEFAULT abap_true
        iv_hint        TYPE string OPTIONAL
        iv_scrollable  TYPE abap_bool DEFAULT abap_true
        io_content     TYPE REF TO zcl_abapgit_html
      RETURNING
        VALUE(ro_html) TYPE REF TO zcl_abapgit_html
      RAISING
        zcx_abapgit_exception .
    CLASS-METHODS get_t100_text
      IMPORTING
        iv_msgid       TYPE scx_t100key-msgid
        iv_msgno       TYPE scx_t100key-msgno
      RETURNING
        VALUE(rv_text) TYPE string.
    CLASS-METHODS normalize_program_name
      IMPORTING
        iv_program_name                   TYPE syrepid
      RETURNING
        VALUE(rv_normalized_program_name) TYPE string.
ENDCLASS.



CLASS zcl_abapgit_gui_chunk_lib IMPLEMENTATION.


  METHOD normalize_program_name.

    rv_normalized_program_name = substring_before(
                                     val   = iv_program_name
                                     regex = `(=+CP)?$` ).

  ENDMETHOD.


  METHOD render_branch_span.

    DATA: lv_text  TYPE string,
          lv_class TYPE string.

    lv_text = zcl_abapgit_git_branch_list=>get_display_name( iv_branch ).

    IF zcl_abapgit_git_branch_list=>get_type( iv_branch ) = zif_abapgit_definitions=>c_git_branch_type-branch.
      lv_class = 'branch branch_branch'.
    ELSE.
      lv_class = 'branch'.
    ENDIF.

    CREATE OBJECT ro_html.
    ro_html->add( |<span class="{ lv_class }">| ).
    ro_html->add_icon( iv_name = 'code-branch/grey70' iv_hint = 'Current branch' ).
    IF iv_interactive = abap_true.
      ro_html->add_a( iv_act = |{ zif_abapgit_definitions=>c_action-git_branch_switch }?{ io_repo->get_key( ) }|
                      iv_txt = lv_text ).
    ELSE.
      ro_html->add( lv_text ).
    ENDIF.
    ro_html->add( '</span>' ).

  ENDMETHOD.


  METHOD render_commit_popup.

    CREATE OBJECT ro_html.

    ro_html->add( '<ul class="hotkeys">' ).
    ro_html->add( |<li>|
      && |<span>{ iv_content }</span>|
      && |</li>| ).
    ro_html->add( '</ul>' ).

    ro_html = render_infopanel(
      iv_div_id     = |{ iv_id }|
      iv_title      = 'Commit details'
      iv_hide       = abap_true
      iv_scrollable = abap_false
      io_content    = ro_html ).

  ENDMETHOD.


  METHOD render_error.

    DATA lv_error TYPE string.

    CREATE OBJECT ro_html.

    IF ix_error IS BOUND.
      lv_error = ix_error->get_text( ).
    ELSE.
      lv_error = iv_error.
    ENDIF.

    ro_html->add( '<div class="dummydiv error">' ).
    ro_html->add( |{ zcl_abapgit_html=>icon( 'exclamation-circle/red' ) } Error: { lv_error }| ).
    ro_html->add( '</div>' ).

  ENDMETHOD.


  METHOD render_error_message_box.

    DATA:
      lv_error_text   TYPE string,
      lv_longtext     TYPE string,
      lv_program_name TYPE syrepid,
      lv_title        TYPE string,
      lv_text         TYPE string.


    CREATE OBJECT ro_html.

    lv_error_text = ix_error->get_text( ).
    lv_longtext = ix_error->get_longtext( abap_true ).

    REPLACE FIRST OCCURRENCE OF REGEX |(<br>{ zcl_abapgit_message_helper=>gc_section_text-cause }<br>)|
            IN lv_longtext
            WITH |<h3>$1</h3>|.

    REPLACE FIRST OCCURRENCE OF REGEX |(<br>{ zcl_abapgit_message_helper=>gc_section_text-system_response }<br>)|
            IN lv_longtext
            WITH |<h3>$1</h3>|.

    REPLACE FIRST OCCURRENCE OF REGEX |(<br>{ zcl_abapgit_message_helper=>gc_section_text-what_to_do }<br>)|
            IN lv_longtext
            WITH |<h3>$1</h3>|.

    REPLACE FIRST OCCURRENCE OF REGEX |(<br>{ zcl_abapgit_message_helper=>gc_section_text-sys_admin }<br>)|
            IN lv_longtext
            WITH |<h3>$1</h3>|.

    ro_html->add( |<div id="message" class="message-panel">| ).
    ro_html->add( |{ lv_error_text }| ).
    ro_html->add( |<div class="float-right">| ).

    ro_html->add_a(
        iv_txt   = `&#x274c;`
        iv_act   = `toggleDisplay('message')`
        iv_class = `close-btn`
        iv_typ   = zif_abapgit_html=>c_action_type-onclick ).

    ro_html->add( |</div>| ).

    ro_html->add( |<div class="float-right message-panel-commands">| ).

    IF ix_error->if_t100_message~t100key-msgid IS NOT INITIAL.

      lv_title = get_t100_text(
                    iv_msgid = ix_error->if_t100_message~t100key-msgid
                    iv_msgno = ix_error->if_t100_message~t100key-msgno ).

      lv_text = |Message ({ ix_error->if_t100_message~t100key-msgid }/{ ix_error->if_t100_message~t100key-msgno })|.

      ro_html->add_a(
          iv_txt   = lv_text
          iv_typ   = zif_abapgit_html=>c_action_type-sapevent
          iv_act   = zif_abapgit_definitions=>c_action-goto_message
          iv_title = lv_title
          iv_id    = `a_goto_message` ).

    ENDIF.

    ix_error->get_source_position(
      IMPORTING
        program_name = lv_program_name ).

    lv_title = normalize_program_name( lv_program_name ).

    ro_html->add_a(
        iv_txt   = `Goto source`
        iv_act   = zif_abapgit_definitions=>c_action-goto_source
        iv_typ   = zif_abapgit_html=>c_action_type-sapevent
        iv_title = lv_title
        iv_id    = `a_goto_source` ).

    ro_html->add_a(
        iv_txt = `Callstack`
        iv_act = zif_abapgit_definitions=>c_action-show_callstack
        iv_typ = zif_abapgit_html=>c_action_type-sapevent
        iv_id  = `a_callstack` ).

    ro_html->add( |</div>| ).
    ro_html->add( |<div class="message-panel-commands">| ).
    ro_html->add( |{ lv_longtext }| ).
    ro_html->add( |</div>| ).
    ro_html->add( |</div>| ).

  ENDMETHOD.


  METHOD render_hotkey_overview.

    DATA: lv_hint                 TYPE string,
          lt_user_defined_hotkeys TYPE zif_abapgit_definitions=>tty_hotkey,
          lt_hotkeys_for_page     TYPE zif_abapgit_gui_page_hotkey=>tty_hotkey_with_name,
          lo_settings             TYPE REF TO zcl_abapgit_settings,
          lv_hotkey               TYPE string.

    FIELD-SYMBOLS:
      <ls_hotkey>              LIKE LINE OF lt_hotkeys_for_page,
      <ls_user_defined_hotkey> LIKE LINE OF lt_user_defined_hotkeys.

    lo_settings             = zcl_abapgit_persist_settings=>get_instance( )->read( ).
    lt_user_defined_hotkeys = lo_settings->get_hotkeys( ).
    lt_hotkeys_for_page     = zcl_abapgit_hotkeys=>get_all_default_hotkeys( io_page ).

    CREATE OBJECT ro_html.

    " Render hotkeys
    ro_html->add( '<ul class="hotkeys">' ).
    LOOP AT lt_hotkeys_for_page ASSIGNING <ls_hotkey>.

      READ TABLE lt_user_defined_hotkeys ASSIGNING <ls_user_defined_hotkey>
                                         WITH TABLE KEY action
                                         COMPONENTS action = <ls_hotkey>-action.
      IF sy-subrc = 0.
        lv_hotkey = <ls_user_defined_hotkey>-hotkey.
      ELSE.
        lv_hotkey = <ls_hotkey>-hotkey.
      ENDIF.

      ro_html->add( |<li>|
          && |<span class="key-id">{ lv_hotkey }</span>|
          && |<span class="key-descr">{ <ls_hotkey>-name }</span>|
          && |</li>| ).

    ENDLOOP.
    ro_html->add( '</ul>' ).

    " Wrap
    CLEAR: lv_hotkey.

    READ TABLE lt_hotkeys_for_page ASSIGNING <ls_hotkey>
      WITH TABLE KEY action
      COMPONENTS action = zcl_abapgit_gui_page=>c_global_page_action-showhotkeys.
    IF sy-subrc = 0.
      lv_hotkey = <ls_hotkey>-hotkey.
    ENDIF.

    READ TABLE lt_user_defined_hotkeys ASSIGNING <ls_user_defined_hotkey>
      WITH TABLE KEY action
      COMPONENTS action = zcl_abapgit_gui_page=>c_global_page_action-showhotkeys.
    IF sy-subrc = 0.
      lv_hotkey = <ls_user_defined_hotkey>-hotkey.
    ENDIF.

    IF lv_hotkey IS NOT INITIAL.
      lv_hint = |Close window with '{ <ls_hotkey>-hotkey }' or upper right corner 'X'|.
    ENDIF.

    ro_html = render_infopanel(
      iv_div_id     = 'hotkeys'
      iv_title      = 'Hotkeys'
      iv_hint       = lv_hint
      iv_hide       = abap_true
      iv_scrollable = abap_false
      io_content    = ro_html ).

    IF <ls_hotkey> IS ASSIGNED AND zcl_abapgit_hotkeys=>should_show_hint( ) = abap_true.
      ro_html->add( |<div id="hotkeys-hint" class="corner-hint">|
        && |Press '{ <ls_hotkey>-hotkey }' to get keyboard shortcuts list|
        && |</div>| ).
    ENDIF.

  ENDMETHOD.


  METHOD render_infopanel.

    DATA lv_display TYPE string.
    DATA lv_class TYPE string.

    CREATE OBJECT ro_html.

    IF iv_hide = abap_true. " Initially hide
      lv_display = 'display:none'.
    ENDIF.

    lv_class = 'info-panel'.
    IF iv_scrollable = abap_false. " Initially hide
      lv_class = lv_class && ' info-panel-fixed'.
    ENDIF.

    ro_html->add( |<div id="{ iv_div_id }" class="{ lv_class }" style="{ lv_display }">| ).

    ro_html->add( |<div class="info-title">{ iv_title }|
               && '<div class="float-right">'
               && zcl_abapgit_html=>a(
                    iv_txt   = '&#x274c;'
                    iv_typ   = zif_abapgit_html=>c_action_type-onclick
                    iv_act   = |toggleDisplay('{ iv_div_id }')|
                    iv_class = 'close-btn' )
               && '</div></div>' ).

    IF iv_hint IS NOT INITIAL.
      ro_html->add( '<div class="info-hint">'
        && zcl_abapgit_html=>icon( iv_name = 'exclamation-triangle' iv_class = 'pad-right' )
        && iv_hint
        && '</div>' ).
    ENDIF.

    ro_html->add( |<div class="info-list">| ).
    ro_html->add( io_content ).
    ro_html->add( '</div>' ).
    ro_html->add( '</div>' ).

  ENDMETHOD.


  METHOD render_item_state.

    DATA: lv_system TYPE string.

    FIELD-SYMBOLS <lv_state> TYPE char1.


    rv_html = '<span class="state-block">'.

    DO 2 TIMES.
      CASE sy-index.
        WHEN 1.
          ASSIGN iv_lstate TO <lv_state>.
          lv_system = 'Local:'.
        WHEN 2.
          ASSIGN iv_rstate TO <lv_state>.
          lv_system = 'Remote:'.
      ENDCASE.

      CASE <lv_state>.
        WHEN zif_abapgit_definitions=>c_state-unchanged.  "None or unchanged
          IF iv_lstate = zif_abapgit_definitions=>c_state-added OR iv_rstate = zif_abapgit_definitions=>c_state-added.
            rv_html = rv_html && |<span class="none" title="{ lv_system } Not exists">X</span>|.
          ELSE.
            rv_html = rv_html && |<span class="none" title="{ lv_system } No changes">&nbsp;</span>|.
          ENDIF.
        WHEN zif_abapgit_definitions=>c_state-modified.   "Changed
          rv_html = rv_html && |<span class="changed" title="{ lv_system } Modified">M</span>|.
        WHEN zif_abapgit_definitions=>c_state-added.      "Added new
          rv_html = rv_html && |<span class="added" title="{ lv_system } Added new">A</span>|.
        WHEN zif_abapgit_definitions=>c_state-mixed.      "Multiple changes (multifile)
          rv_html = rv_html && |<span class="mixed" title="{ lv_system } Multiple changes">&#x25A0;</span>|.
        WHEN zif_abapgit_definitions=>c_state-deleted.    "Deleted
          rv_html = rv_html && |<span class="deleted" title="{ lv_system } Deleted">D</span>|.
      ENDCASE.
    ENDDO.

    rv_html = rv_html && '</span>'.

  ENDMETHOD.


  METHOD render_js_error_banner.
    CREATE OBJECT ro_html.
    ro_html->add( '<div id="js-error-banner" class="dummydiv error">' ).
    ro_html->add( |{ zcl_abapgit_html=>icon( 'exclamation-triangle/red' ) }| &&
                  ' If this does not disappear soon,' &&
                  ' then there is a JS init error, please log an issue' ).
    ro_html->add( '</div>' ).
  ENDMETHOD.


  METHOD render_news.

    DATA: lv_text TYPE string,
          lv_hint TYPE string,
          lt_log  TYPE zcl_abapgit_news=>tt_log.

    FIELD-SYMBOLS: <ls_line> LIKE LINE OF lt_log.

    CREATE OBJECT ro_html.

    IF io_news IS NOT BOUND OR io_news->has_news( ) = abap_false.
      RETURN.
    ENDIF.

    lt_log = io_news->get_log( ).

    " Render news
    LOOP AT lt_log ASSIGNING <ls_line>.
      IF <ls_line>-is_header = abap_true.
        IF <ls_line>-pos_to_cur > 0.
          lv_text = <ls_line>-text && '<span class="version-marker update">update</span>'.
        ELSEIF <ls_line>-pos_to_cur = 0.
          lv_text = <ls_line>-text && '<span class="version-marker">current</span>'.
        ELSE. " < 0
          lv_text = <ls_line>-text.
        ENDIF.
        ro_html->add( |<h1>{ lv_text }</h1>| ).
      ELSE.
        ro_html->add( |<li>{ <ls_line>-text }</li>| ).
      ENDIF.
    ENDLOOP.

    " Wrap
    IF io_news->has_important( ) = abap_true.
      lv_hint = 'Please note changes marked with "!"'.
    ENDIF.

    ro_html = render_infopanel(
      iv_div_id  = 'news'
      iv_title   = 'Announcement of the latest changes'
      iv_hint    = lv_hint
      iv_hide    = boolc( io_news->has_unseen( ) = abap_false )
      io_content = ro_html ).

  ENDMETHOD.


  METHOD render_repo_top.

    DATA: lo_repo_online       TYPE REF TO zcl_abapgit_repo_online,
          lo_pback             TYPE REF TO zcl_abapgit_persist_background,
          lv_hint              TYPE string,
          lv_icon              TYPE string,
          lv_package_jump_data TYPE string.

    CREATE OBJECT ro_html.
    CREATE OBJECT lo_pback.

    IF io_repo->is_offline( ) = abap_true.
      lv_icon = 'plug/darkgrey' ##NO_TEXT.
      lv_hint = 'Offline repository' ##NO_TEXT.
    ELSE.
      lv_icon = 'cloud-upload-alt/blue' ##NO_TEXT.
      lv_hint = 'On-line repository' ##NO_TEXT.
    ENDIF.

    ro_html->add( '<table class="w100"><tr>' ).

    ro_html->add( '<td class="repo_name">' ).

    " Repo type and name
    ro_html->add_icon( iv_name = lv_icon  iv_hint = lv_hint ).
    ro_html->add( |<span class="name">{ io_repo->get_name( ) }</span>| ).
    IF io_repo->is_offline( ) = abap_false.
      lo_repo_online ?= io_repo.

      ro_html->add_a( iv_txt   = lo_repo_online->get_url( )
                      iv_act   = |{ zif_abapgit_definitions=>c_action-url }?|
                              && |{ lo_repo_online->get_url( ) }|
                      iv_class = |url| ).

    ENDIF.

    " News
    IF io_news IS BOUND AND io_news->has_news( ) = abap_true.
      IF io_news->has_updates( ) = abap_true.
        lv_icon = 'arrow-circle-up/warning'.
      ELSE.
        lv_icon = 'arrow-circle-up/grey80'.
      ENDIF.
      ro_html->add_a( iv_act = |toggleDisplay('news')|
                      iv_typ = zif_abapgit_html=>c_action_type-onclick
                      iv_txt = zcl_abapgit_html=>icon( iv_name  = lv_icon
                                                       iv_class = 'pad-sides'
                                                       iv_hint  = 'Display changelog' ) ).
    ENDIF.
    ro_html->add( '</td>' ).

    ro_html->add( '<td class="repo_attr right">' ).

    " Fav
    IF abap_true = zcl_abapgit_persistence_user=>get_instance( )->is_favorite_repo( io_repo->get_key( ) ).
      lv_icon = 'star/blue' ##NO_TEXT.
    ELSE.
      lv_icon = 'star/grey' ##NO_TEXT.
    ENDIF.
    ro_html->add_a( iv_act = |{ zif_abapgit_definitions=>c_action-repo_toggle_fav }?{ io_repo->get_key( ) }|
                    iv_txt = zcl_abapgit_html=>icon( iv_name  = lv_icon
                                                     iv_class = 'pad-sides'
                                                     iv_hint  = 'Click to toggle favorite' ) ).

    " BG
    IF lo_pback->exists( io_repo->get_key( ) ) = abap_true.
      ro_html->add( '<span class="bg_marker" title="background">BG</span>' ).
    ENDIF.

    " Write protect
    IF io_repo->get_local_settings( )-write_protected = abap_true.
      ro_html->add_icon( iv_name = 'lock/grey70' iv_hint = 'Locked from pulls' ).
    ENDIF.

    " Branch
    IF io_repo->is_offline( ) = abap_false.
      lo_repo_online ?= io_repo.
      IF iv_show_branch = abap_true.
        IF iv_branch IS INITIAL.
          ro_html->add( render_branch_span( iv_branch      = lo_repo_online->get_branch_name( )
                                            io_repo        = lo_repo_online
                                            iv_interactive = iv_interactive_branch ) ).
        ELSE.
          ro_html->add( render_branch_span( iv_branch      = iv_branch
                                            io_repo        = lo_repo_online
                                            iv_interactive = iv_interactive_branch ) ).
        ENDIF.
      ENDIF.
    ENDIF.

    " Package
    IF iv_show_package = abap_true.
      ro_html->add_icon( iv_name = 'box/grey70' iv_hint = 'SAP package' ).
      ro_html->add( '<span>' ).

      lv_package_jump_data = zcl_abapgit_html_action_utils=>jump_encode(
        iv_obj_type = 'DEVC'
        iv_obj_name = io_repo->get_package( ) ).

      ro_html->add_a( iv_txt = io_repo->get_package( )
                      iv_act = |{ zif_abapgit_definitions=>c_action-jump }?{ lv_package_jump_data }| ).
      ro_html->add( '</span>' ).
    ENDIF.

    ro_html->add( '</td>' ).
    ro_html->add( '</tr></table>' ).

  ENDMETHOD.

  METHOD get_t100_text.

    SELECT SINGLE text
           FROM t100
           INTO rv_text
           WHERE arbgb = iv_msgid
           AND   msgnr = iv_msgno
           AND   sprsl = sy-langu.

  ENDMETHOD.

ENDCLASS.