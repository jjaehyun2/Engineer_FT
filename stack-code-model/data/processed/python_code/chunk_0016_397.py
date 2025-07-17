*&---------------------------------------------------------------------*
*&  Include           ZKR_OTRF01
*&---------------------------------------------------------------------*
*&---------------------------------------------------------------------*
*&      Form  INITIALIZATION
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM initialization .
  DATA: lt_vrm TYPE vrm_values,
        ls_vrm TYPE vrm_value.

  button1         = TEXT-010. " 검색/수정
  button2         = TEXT-011. " 생성
  mytab-prog      = sy-repid.
  mytab-dynnr     = 100. "검색/수정탭이 Defualt
  mytab-activetab = 'BUTTON1'.

  SELECT devclass AS key ctext AS text
    INTO TABLE lt_vrm
    FROM tdevct
    WHERE ( devclass LIKE 'Y%' OR devclass LIKE 'Z%' )
      AND spras = 'E'.
  LOOP AT lt_vrm INTO ls_vrm.
    ls_vrm-text = |{ ls_vrm-key } : { ls_vrm-text }|.
    MODIFY lt_vrm FROM ls_vrm.
  ENDLOOP.

  CALL FUNCTION 'VRM_SET_VALUES'
    EXPORTING
      id     = 'P_PKGC'
      values = lt_vrm.

  CLEAR: ls_vrm.
  ls_vrm-text = 'Y*,Z* packages'.
  APPEND ls_vrm TO lt_vrm.

  CALL FUNCTION 'VRM_SET_VALUES'
    EXPORTING
      id     = 'P_PKG'
      values = lt_vrm.



ENDFORM.                    " INITIALIZATION
*&---------------------------------------------------------------------*
*&      Form  AT_SELECTION_SCREEN
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM at_selection_screen .

  CASE sy-dynnr.
    WHEN 1000.
      CASE sy-ucomm.
        WHEN 'PUSH1'.
          mytab-dynnr     = 100.
          mytab-activetab = 'BUTTON1'.

        WHEN 'PUSH2'.
          mytab-dynnr     = 200.
          mytab-activetab = 'BUTTON2'.

      ENDCASE.

  ENDCASE.

ENDFORM.                    " AT_SELECTION_SCREEN
*&---------------------------------------------------------------------*
*&      Form  START_OF_SELECTION
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM start_of_selection .


  CASE mytab-dynnr.
    WHEN 100.
      PERFORM get_disp_data.
    WHEN 200.
      PERFORM append_crea_data.
  ENDCASE.

ENDFORM.                    " START_OF_SELECTION
*&---------------------------------------------------------------------*
*&      Form  GET_DISP_DATA
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM get_disp_data .

  DATA: BEGIN OF ls_otr,
          alias_name TYPE sotr_head-alias_name,
          langu      TYPE sotr_text-langu,
          text       TYPE sotr_text-text,
          chan_name  TYPE sotr_head-chan_name,
          chan_tstut TYPE sotr_head-chan_tstut,
          concept    TYPE sotr_head-concept,
          paket      TYPE sotr_head-paket,
          obj_name   TYPE e071-obj_name,
          trkorr     TYPE e071-trkorr,
          used_count TYPE i,
          objid_vec  TYPE sotr_head-objid_vec,
          flag_cntxt TYPE sotr_text-flag_cntxt,
          country    TYPE sotr_text-country,
          extension  TYPE sotr_text-extension,
          status     TYPE sotr_text-status,
          length     TYPE sotr_text-length,
          object     TYPE sotr_text-object,
          last_rel   TYPE sotr_text-last_rel,
          last_irel  TYPE sotr_text-last_irel,
          add_cntxt  TYPE sotr_text-add_cntxt,
          crea_name  TYPE sotr_text-crea_name,
          crea_tstut TYPE sotr_text-crea_tstut,
          flag_corr  TYPE sotr_text-flag_corr,
        END OF ls_otr.
  DATA: lt_otr LIKE TABLE OF ls_otr.
  DATA: lt_otr_temp LIKE TABLE OF ls_otr.
  DATA: BEGIN OF ls_used,
          concept TYPE sotr_use-concept,
          count   TYPE i,
        END OF ls_used.
  DATA: lt_used LIKE TABLE OF ls_used.
  DATA: BEGIN OF ls_e071,
          trkorr   TYPE e071-trkorr,
          obj_name TYPE e071-obj_name,
          as4user  TYPE e070-as4user,
        END OF ls_e071.
  DATA: lt_e071 LIKE TABLE OF ls_e071.
  DATA: lv_timestamp TYPE timestamp.
  DATA: lr_pack TYPE RANGE OF devclass.
  DATA: ls_pack LIKE LINE OF lr_pack.
  DATA: lr_langu TYPE RANGE OF langu.
  DATA: ls_langu LIKE LINE OF lr_langu.
  DATA: lv_tabix TYPE sy-tabix.

*--------------------------------------------------------------------*
  "Package
  IF p_pkg IS NOT INITIAL.
    ls_pack-sign   = 'I'.
    ls_pack-option = 'EQ'.
    ls_pack-low = p_pkg.
    APPEND ls_pack TO lr_pack.
  ELSE.
    ls_pack-sign   = 'I'.
    ls_pack-option = 'CP'.
    ls_pack-low = 'Y*'.
    APPEND ls_pack TO lr_pack.
    ls_pack-sign   = 'I'.
    ls_pack-option = 'CP'.
    ls_pack-low = 'Z*'.
    APPEND ls_pack TO lr_pack.
  ENDIF.

  "Language
  ls_langu-sign   = 'I'.
  ls_langu-option = 'EQ'.
  IF p_en = abap_true.
    ls_langu-low = 'E'.
    APPEND ls_langu TO lr_langu.
  ENDIF.
  IF p_ko = abap_true.
    ls_langu-low = '3'.
    APPEND ls_langu TO lr_langu.
  ENDIF.
  IF p_zh = abap_true.
    ls_langu-low = '1'.
    APPEND ls_langu TO lr_langu.
  ENDIF.
  IF p_zf = abap_true.
    ls_langu-low = 'M'.
    APPEND ls_langu TO lr_langu.
  ENDIF.

*  "ALIAS_NAME이 없는건은 제외하고 추출한다.
*  CLEAR s_alias.
*  s_alias-sign   = 'E'.
*  s_alias-option = 'EQ'.
*  s_alias-low    = ''.
*  APPEND s_alias.

*--------------------------------------------------------------------*
*// OTR 데이타 추출
  SELECT a~concept a~paket a~alias_name a~objid_vec b~chan_name b~chan_tstut
         b~langu b~text b~flag_cntxt b~country b~extension b~status b~length
         b~object b~last_rel b~last_irel b~add_cntxt b~crea_name b~crea_tstut b~flag_corr
    INTO CORRESPONDING FIELDS OF TABLE lt_otr
    FROM sotr_head AS a
   INNER JOIN sotr_text AS b
      ON a~concept = b~concept
   WHERE a~paket IN lr_pack
     AND a~alias_name IN s_alias
     AND a~concept IN s_concpt
     AND b~langu IN lr_langu
     AND b~text IN s_text.

  IF s_pgid[] IS NOT INITIAL.
    "Used Program
    LOOP AT s_pgid.
      s_pgid-option = 'CP'.
      IF s_pgid-low IS NOT INITIAL.
        CONCATENATE '*' s_pgid-low '*' INTO s_pgid-low.
      ENDIF.
      MODIFY s_pgid.
    ENDLOOP.

    lt_otr_temp[] = lt_otr[].
    SORT lt_otr_temp BY concept.
    DELETE ADJACENT DUPLICATES FROM lt_otr_temp COMPARING concept.
    IF lt_otr_temp IS NOT INITIAL.

      SELECT concept
        INTO CORRESPONDING FIELDS OF TABLE lt_used
        FROM sotr_use
         FOR ALL ENTRIES IN lt_otr_temp
       WHERE concept = lt_otr_temp-concept
         AND obj_name IN s_pgid.
      IF sy-subrc = 0.
*// 사용처에 없는 건은 삭제
        SORT lt_used BY concept.
        LOOP AT lt_otr INTO ls_otr.
          lv_tabix = sy-tabix.
          READ TABLE lt_used INTO ls_used WITH KEY concept = ls_otr-concept BINARY SEARCH.
          IF sy-subrc <> 0.
            DELETE lt_otr INDEX lv_tabix.
          ENDIF.
        ENDLOOP.
      ENDIF.
    ENDIF.

  ENDIF.

*// Used Count
  REFRESH: lt_otr_temp, lt_used.
  lt_otr_temp[] = lt_otr[].
  SORT lt_otr_temp BY concept.
  DELETE ADJACENT DUPLICATES FROM lt_otr_temp COMPARING concept.
  IF lt_otr_temp IS NOT INITIAL.

    SELECT concept
      INTO CORRESPONDING FIELDS OF TABLE lt_used
      FROM sotr_use
       FOR ALL ENTRIES IN lt_otr_temp
     WHERE concept = lt_otr_temp-concept.
    IF sy-subrc = 0.
      LOOP AT lt_used INTO ls_used.
        ls_used-count = 1.
        COLLECT ls_used INTO lt_used.
      ENDLOOP.
      SORT lt_used BY concept.
    ENDIF.
  ENDIF.

*// Task No.
  LOOP AT lt_otr INTO ls_otr.
    lv_tabix               = sy-tabix.
    ls_otr-obj_name(30)    = ls_otr-paket.
    ls_otr-obj_name+30(32) = ls_otr-concept.
    MODIFY lt_otr FROM ls_otr INDEX lv_tabix TRANSPORTING obj_name.
  ENDLOOP.

  REFRESH lt_otr_temp.
  lt_otr_temp[] = lt_otr[].
  SORT lt_otr_temp BY obj_name.
  DELETE ADJACENT DUPLICATES FROM lt_otr_temp COMPARING obj_name.
  IF lt_otr_temp[] IS NOT INITIAL.
    SELECT a~trkorr a~obj_name b~as4user
      INTO CORRESPONDING FIELDS OF TABLE lt_e071
      FROM e071 AS a
     INNER JOIN e070 AS b
        ON a~trkorr EQ b~trkorr
       FOR ALL ENTRIES IN lt_otr_temp
     WHERE obj_name = lt_otr_temp-obj_name
       AND lockflag = abap_true.
    IF sy-subrc = 0.
      SORT lt_e071 BY obj_name as4user.
    ENDIF.
  ENDIF.

*// ALV데이타 구성
  LOOP AT lt_otr INTO ls_otr.
    "Task No.
    "본인것이 있으면 본인의 Task No.를 Display
    READ TABLE lt_e071 INTO ls_e071
      WITH KEY obj_name = ls_otr-obj_name BINARY SEARCH.
*               as4user = sy-uname BINARY SEARCH.
    IF sy-subrc = 0.
      ls_otr-trkorr = ls_e071-trkorr.
    ELSE.
      READ TABLE lt_e071 INTO ls_e071
        WITH KEY obj_name = ls_otr-obj_name BINARY SEARCH.
      IF sy-subrc = 0.
        ls_otr-trkorr = ls_e071-trkorr.
      ENDIF.
    ENDIF.

    "Used Count
    READ TABLE lt_used INTO ls_used WITH KEY concept = ls_otr-concept BINARY SEARCH.
    IF sy-subrc = 0.
      ls_otr-used_count = ls_used-count.
    ENDIF.

    MOVE-CORRESPONDING ls_otr TO gt_outtab1.
    "Changed Date
*    gt_outtab1-chan_date = ls_otr-chan_tstut(8).
    lv_timestamp = ls_otr-crea_tstut.
    CONVERT TIME STAMP lv_timestamp TIME ZONE sy-zonlo INTO DATE gt_outtab1-crea_date TIME gt_outtab1-crea_time.
    lv_timestamp = ls_otr-chan_tstut.
    CONVERT TIME STAMP lv_timestamp TIME ZONE sy-zonlo INTO DATE gt_outtab1-chan_date TIME gt_outtab1-chan_time.

    APPEND gt_outtab1.
  ENDLOOP.

  REFRESH gt_first1.
  gt_first1[] = gt_outtab1[].

ENDFORM.                    " GET_DISP_DATA
*&---------------------------------------------------------------------*
*&      Form  END_OF_SELECTION
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM end_of_selection .

  DATA: lv_lines TYPE i.
  DATA: lv_char(10).
  DATA: lv_str(20).
  DATA: lv_subrc TYPE sy-subrc.

  CASE mytab-dynnr.
    WHEN 100.
      DESCRIBE TABLE gt_outtab1 LINES lv_lines.
      IF gt_outtab1[] IS INITIAL.
        "MESSAGE
        MESSAGE s001(00) WITH 'There are no data.'.

      ELSE.

        lv_char = lv_lines.
        CONCATENATE lv_char ` rows.` INTO lv_str.
        MESSAGE s001(00) WITH lv_str.
        " 변경화면 출력
        CALL SCREEN 400.
      ENDIF.

    WHEN 200.
*// 유효한 Package인지 체크
      PERFORM check_exist_pakage USING gv_paket
                                 CHANGING lv_subrc.
      IF lv_subrc <> 0.
        MESSAGE i001(00) WITH gv_paket 'is not valid package.'.
        STOP.
      ENDIF.

      CHECK gt_outtab2[] IS NOT INITIAL.
      " 생성화면 출력
      CALL SCREEN 500.

  ENDCASE.

ENDFORM.                    " END-OF-SELECTION
*&---------------------------------------------------------------------*
*&      Form  ALV_CONTROL1
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM alv_control1 .

*Docking Container
  CREATE OBJECT g_dock_cont1
    EXPORTING
*     PARENT                      =
      repid                       = sy-repid
      dynnr                       = sy-dynnr
      side                        = cl_gui_docking_container=>dock_at_top
      extension                   = 500
    EXCEPTIONS
      cntl_error                  = 1
      cntl_system_error           = 2
      create_error                = 3
      lifetime_error              = 4
      lifetime_dynpro_dynpro_link = 5
      OTHERS                      = 6.

*Grid
  CREATE OBJECT g_grid1
    EXPORTING
      i_parent      = g_dock_cont1   "CONTAINER
      i_appl_events = 'X'.          "Application Event

*ALV CELLTAB
  PERFORM init_alv_style1.
*ALV Grid Layout
  PERFORM alv_layout1.
*ALV Grid Field Catalog
  PERFORM alv_fieldcatalog1.
*ALV Grid Fuction Code
  PERFORM alv_exclude_fcode1.
*ALV Grid Sort
  PERFORM alv_sort1.

*Calling the Method for ALV output
  CALL METHOD g_grid1->set_table_for_first_display
    EXPORTING
      is_layout            = gs_layout1
      i_save               = 'A'
      it_toolbar_excluding = gt_fcode1
    CHANGING
      it_fieldcatalog      = gt_fdcat1[]
      it_sort              = gt_sort1[]
      it_outtab            = gt_outtab1[].

*Set Event Handler
  CREATE OBJECT g_events.
  SET HANDLER g_events->hotspot_click FOR g_grid1.

ENDFORM.                    " ALV_CONTROL1
*&---------------------------------------------------------------------*
*&      Form  ALV_LAYOUT1
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM alv_layout1 .

  gs_layout1-stylefname = 'CELLTAB'.
  gs_layout1-box_fname = 'BOX'.
  gs_layout1-no_rowmark = abap_false.

ENDFORM.                    " ALV_LAYOUT1
*&---------------------------------------------------------------------*
*&      Form  EXIT_PROGRAM
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM exit_program .

  LEAVE PROGRAM.

ENDFORM.                    " EXIT_PROGRAM
*&---------------------------------------------------------------------*
*&      Form  SWITCH_EDIT_MODE
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM switch_edit_mode .

  IF g_grid1->is_ready_for_input( ) EQ 0.
* set edit enabled cells ready for input
    CALL METHOD g_grid1->set_ready_for_input
      EXPORTING
        i_ready_for_input = 1.

  ELSE.
* lock edit enabled cells against input
    CALL METHOD g_grid1->set_ready_for_input
      EXPORTING
        i_ready_for_input = 0.
  ENDIF.

ENDFORM.                    " SWITCH_EDIT_MODE
*&---------------------------------------------------------------------*
*&      Form  INIT_ALV_STYLE1
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM init_alv_style1.

  DATA: lv_tabix TYPE sy-tabix.
  DATA: lt_celltab TYPE lvc_t_styl.

  LOOP AT gt_outtab1.
    lv_tabix = sy-tabix.
    REFRESH lt_celltab.

    PERFORM fill_celltab1 USING 'RW'
                         CHANGING lt_celltab.

    INSERT LINES OF lt_celltab INTO TABLE gt_outtab1-celltab.
    MODIFY gt_outtab1 INDEX lv_tabix.
  ENDLOOP.

ENDFORM.                    " INIT_ALV_STYLE1
*&---------------------------------------------------------------------*
*&      Form  FILL_CELLTAB1
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      -->P_0841   text
*      <--P_LT_CELLTAB  text
*----------------------------------------------------------------------*
FORM fill_celltab1  USING    VALUE(pv_mode)
                  CHANGING pt_celltab TYPE lvc_t_styl.

  DATA: ls_celltab TYPE lvc_s_styl,
        lv_mode    TYPE raw4.

  IF pv_mode EQ 'RW'.
    lv_mode = cl_gui_alv_grid=>mc_style_enabled.
  ELSE.
    lv_mode = cl_gui_alv_grid=>mc_style_disabled.
  ENDIF.

  ls_celltab-fieldname = 'ALIAS'.
  ls_celltab-style = cl_gui_alv_grid=>mc_style_disabled.
  INSERT ls_celltab INTO TABLE pt_celltab.

  ls_celltab-fieldname = 'LANG'.
  ls_celltab-style = cl_gui_alv_grid=>mc_style_disabled.
  INSERT ls_celltab INTO TABLE pt_celltab.

  ls_celltab-fieldname = 'TEXT'.
  ls_celltab-style = lv_mode.
  INSERT ls_celltab INTO TABLE pt_celltab.

  ls_celltab-fieldname = 'USED_COUNT'.
  ls_celltab-style = cl_gui_alv_grid=>mc_style_disabled.
  INSERT ls_celltab INTO TABLE pt_celltab.

  ls_celltab-fieldname = 'CREA_NAME'.
  ls_celltab-style = cl_gui_alv_grid=>mc_style_disabled.
  INSERT ls_celltab INTO TABLE pt_celltab.

  ls_celltab-fieldname = 'CREA_DATE'.
  ls_celltab-style = cl_gui_alv_grid=>mc_style_disabled.
  INSERT ls_celltab INTO TABLE pt_celltab.

  ls_celltab-fieldname = 'CREA_TIME'.
  ls_celltab-style = cl_gui_alv_grid=>mc_style_disabled.
  INSERT ls_celltab INTO TABLE pt_celltab.

  ls_celltab-fieldname = 'CHAN_NAME'.
  ls_celltab-style = cl_gui_alv_grid=>mc_style_disabled.
  INSERT ls_celltab INTO TABLE pt_celltab.

  ls_celltab-fieldname = 'CHAN_DATE'.
  ls_celltab-style = cl_gui_alv_grid=>mc_style_disabled.
  INSERT ls_celltab INTO TABLE pt_celltab.

  ls_celltab-fieldname = 'CHAN_TIME'.
  ls_celltab-style = cl_gui_alv_grid=>mc_style_disabled.
  INSERT ls_celltab INTO TABLE pt_celltab.

  ls_celltab-fieldname = 'CONCEPT'.
  ls_celltab-style = cl_gui_alv_grid=>mc_style_disabled.
  INSERT ls_celltab INTO TABLE pt_celltab.

  ls_celltab-fieldname = 'TRKORR'.
  ls_celltab-style = cl_gui_alv_grid=>mc_style_disabled.
  INSERT ls_celltab INTO TABLE pt_celltab.

ENDFORM.                    " FILL_CELLTAB1
*&---------------------------------------------------------------------*
*&      Form  append_catalog1
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
FORM append_catalog1 USING p_key
                          p_field
                          p_text
                          p_length
                          p_ref_table
                          p_ref_field
                          p_just
                          p_check
                          p_hotspot
                          p_no_zero.

  DATA: ls_fldcat TYPE lvc_s_fcat.
  CLEAR ls_fldcat.

  g_pos1 = g_pos1 + 1.
  ls_fldcat-col_pos   = g_pos1.
  ls_fldcat-key      = p_key.
  ls_fldcat-fieldname = p_field.
  ls_fldcat-coltext   = p_text.

  ls_fldcat-scrtext_m = p_text.
  ls_fldcat-scrtext_s = p_text.
  ls_fldcat-outputlen = p_length.
  ls_fldcat-ref_table = p_ref_table.
  ls_fldcat-ref_field = p_ref_field.
  ls_fldcat-just      = p_just.
  ls_fldcat-checkbox  = p_check.
  ls_fldcat-hotspot   = p_hotspot.
  ls_fldcat-no_zero   = p_no_zero.

  APPEND ls_fldcat TO gt_fdcat1.

ENDFORM.                    " APPEND_CATALOG1
*&---------------------------------------------------------------------*
*&      Form  ALV_FIELDCATALOG1
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM alv_fieldcatalog1 .

  PERFORM append_catalog1 USING:
  'X' 'ALIAS_NAME'    'Alias'        '40'   'SOTR_HEAD'  'ALIAS_NAME'  ''  ''  ''  '',
  'X' 'LANGU'         'Language'     '08'   'T002'  'SPRAS'  ''  ''  ''  '',
  ' ' 'TEXT'          'Text'         '30'   'SOTR_TEXT'  'TEXT'  ''  ''  ''  '',
  ' ' 'USED_COUNT'    'Used Count'   '10'   ''  ''  ''  ''  'X'  '',
  ' ' 'CREA_NAME'     'Created User' '12'   'TPCUSER'  'USERID'  ''  ''  ''  '',
  ' ' 'CREA_DATE'     'Created Date' '12'   ''  ''  ''  ''  ''  '',
  ' ' 'CREA_TIME'     'Created Time' '12'   ''  ''  ''  ''  ''  '',
  ' ' 'CHAN_NAME'     'Changed User' '12'   'TPCUSER'  'USERID'  ''  ''  ''  '',
  ' ' 'CHAN_DATE'     'Changed Date' '12'   ''  ''  ''  ''  ''  '',
  ' ' 'CHAN_TIME'     'Changed Time' '12'   ''  ''  ''  ''  ''  '',
  ' ' 'CONCEPT'       'Concept'      '34'   'SOTR_HEAD'  'CONCEPT'  ''  ''  'X'  '',
  ' ' 'TRKORR'        'Task No.'     '11'   'E071'  'TRKORR'  ''  ''  ''  '',
  ' ' 'ICON'          ' '            '02'   ''  ''  ''  ''  ''  '',
  ' ' 'MESSAGE'       'Message'      '30'   ''  ''  ''  ''  ''  ''.

ENDFORM.                    " ALV_FIELDCATALOG1
*&---------------------------------------------------------------------*
*&      Form  ALV_EXCLUDE_FCODE1
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM alv_exclude_fcode1 .

  REFRESH gt_fcode1.

  PERFORM alv_append_exclude_function
        TABLES gt_fcode1 "<TABLE>
*        USING : cl_gui_alv_grid=>mc_fc_excl_all. " ** 툴바 모두제거 **
        USING :
                cl_gui_alv_grid=>mc_fc_loc_undo, " 실행취소&LOCAL&UNDO
                cl_gui_alv_grid=>mc_fc_auf,      " 소계확장 &AUF
                cl_gui_alv_grid=>mc_fc_average,  " &AVERAGE
                cl_gui_alv_grid=>mc_fc_back_classic,
                cl_gui_alv_grid=>mc_fc_call_abc, " &ABC
                cl_gui_alv_grid=>mc_fc_call_chain,
                cl_gui_alv_grid=>mc_fc_call_crbatch,
                cl_gui_alv_grid=>mc_fc_call_crweb,
                cl_gui_alv_grid=>mc_fc_call_lineitems,
                cl_gui_alv_grid=>mc_fc_call_master_data,
                cl_gui_alv_grid=>mc_fc_call_more,
                cl_gui_alv_grid=>mc_fc_call_report,
                cl_gui_alv_grid=>mc_fc_call_xint,
                cl_gui_alv_grid=>mc_fc_call_xxl,
                cl_gui_alv_grid=>mc_fc_col_invisible,
                cl_gui_alv_grid=>mc_fc_col_optimize,
                cl_gui_alv_grid=>mc_fc_current_variant,
                cl_gui_alv_grid=>mc_fc_data_save,
*                CL_GUI_ALV_GRID=>MC_FC_DELETE_FILTER,
*                CL_GUI_ALV_GRID=>MC_FC_DESELECT_ALL,
                 cl_gui_alv_grid=>mc_fc_detail,
                cl_gui_alv_grid=>mc_fc_expcrdata,
                cl_gui_alv_grid=>mc_fc_expcrdesig,
                cl_gui_alv_grid=>mc_fc_expcrtempl,
                cl_gui_alv_grid=>mc_fc_expmdb,
                cl_gui_alv_grid=>mc_fc_extend,
                cl_gui_alv_grid=>mc_fc_f4,
                cl_gui_alv_grid=>mc_fc_filter,
*                CL_GUI_ALV_GRID=>MC_FC_FIND,
                cl_gui_alv_grid=>mc_fc_fix_columns,
                cl_gui_alv_grid=>mc_fc_graph,
                cl_gui_alv_grid=>mc_fc_help,
                cl_gui_alv_grid=>mc_fc_info,
                cl_gui_alv_grid=>mc_fc_load_variant,
                cl_gui_alv_grid=>mc_fc_loc_copy,          " 행 카피.
                cl_gui_alv_grid=>mc_fc_html,
                cl_gui_alv_grid=>mc_fc_loc_copy_row,      " 행 카피.
                cl_gui_alv_grid=>mc_fc_loc_cut,           " 가위.
                cl_gui_alv_grid=>mc_fc_loc_delete_row,    " 행삭제.
                cl_gui_alv_grid=>mc_fc_loc_insert_row,    " 행삽입.
                cl_gui_alv_grid=>mc_fc_loc_move_row,
                cl_gui_alv_grid=>mc_fc_loc_append_row,    " 라인생성.
                cl_gui_alv_grid=>mc_fc_loc_paste,         " 겹쳐쓰기.
                cl_gui_alv_grid=>mc_fc_loc_paste_new_row, " 겹쳐쓰기.
                cl_gui_alv_grid=>mc_fc_maintain_variant,
                cl_gui_alv_grid=>mc_fc_maximum,
                cl_gui_alv_grid=>mc_fc_minimum,
*                CL_GUI_ALV_GRID=>MC_FC_PC_FILE,  "Excel Exporting
*                CL_GUI_ALV_GRID=>MC_FC_PRINT,
*                CL_GUI_ALV_GRID=>MC_FC_PRINT_BACK,
*                CL_GUI_ALV_GRID=>MC_FC_PRINT_PREV,
                cl_gui_alv_grid=>mc_fc_refresh,
                cl_gui_alv_grid=>mc_fc_reprep,
                cl_gui_alv_grid=>mc_fc_save_variant,
*                CL_GUI_ALV_GRID=>MC_FC_SELECT_ALL.
                cl_gui_alv_grid=>mc_fc_send,
                cl_gui_alv_grid=>mc_fc_separator,
*                CL_GUI_ALV_GRID=>MC_FC_SORT,
*                CL_GUI_ALV_GRID=>MC_FC_SORT_ASC,
*                CL_GUI_ALV_GRID=>MC_FC_SORT_DSC,
                cl_gui_alv_grid=>mc_fc_subtot,
                cl_gui_alv_grid=>mc_mb_sum,
                cl_gui_alv_grid=>mc_fc_sum,
                cl_gui_alv_grid=>mc_fc_to_office,
                cl_gui_alv_grid=>mc_fc_to_rep_tree,
                cl_gui_alv_grid=>mc_fc_unfix_columns,
*                CL_GUI_ALV_GRID=>MC_FC_VIEWS,
                cl_gui_alv_grid=>mc_fc_view_crystal,
                cl_gui_alv_grid=>mc_fc_view_excel,
*                CL_GUI_ALV_GRID=>MC_FC_VIEW_GRID,
                cl_gui_alv_grid=>mc_fc_word_processor
                .

ENDFORM.                    " ALV_EXCLUDE_FCODE1
*&---------------------------------------------------------------------*
*&      Form  ALV_APPEND_EXCLUDE_FUNCTION
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      -->P_GT_FCODE1  text
*      -->P_CL_GUI_ALV_GRID=>MC_FC_LOC_UND  text
*----------------------------------------------------------------------*
FORM alv_append_exclude_function  TABLES pt_fcode
                                  USING  p_value.

  DATA : ls_exclude TYPE ui_func.

  ls_exclude = p_value.
  APPEND ls_exclude TO pt_fcode.

ENDFORM.                    " ALV_APPEND_EXCLUDE_FUNCTION
*&---------------------------------------------------------------------*
*&      Form  EVENT_TOP_OF_PAGE
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      -->P_G_DYNDOC_ID  text
*----------------------------------------------------------------------*
FORM event_hotspot_click USING VALUE(i_row)    TYPE lvc_s_row
                               VALUE(i_column) TYPE lvc_s_col.

  CLEAR gt_outtab1.
  READ TABLE gt_outtab1 INDEX i_row-index.

  CASE i_column-fieldname.
    WHEN 'USED_COUNT'.
*// OTR Where Used
      CALL FUNCTION 'BTFR_DISPLAY_USAGE'
        EXPORTING
          concept = gt_outtab1-concept.
    WHEN 'CONCEPT'.
      CLEAR: bdcdata, bdcdata[].
      PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0100'.
      PERFORM bdc_field  USING:
            'BDC_CURSOR'                'G_DYNP_0100-CONCEPT',
            'BDC_OKCODE'                '/00',
            'G_DYNP_0100-SLANG'         gt_outtab1-langu,
            'G_DYNP_0100-CONCEPT'       gt_outtab1-concept,
            'G_DYNP_0100-ALIAS'         gt_outtab1-alias_name.
      CALL TRANSACTION 'SOTR_EDIT' USING bdcdata MODE 'E'.

  ENDCASE.

ENDFORM.                    " EVENT_TOP_OF_PAGE
*&---------------------------------------------------------------------*
*&      Form  LEAVE_SCREEN
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM leave_screen .

  LEAVE TO SCREEN 0.

ENDFORM.                    " LEAVE_SCREEN
*&---------------------------------------------------------------------*
*&      Form  SAVE_OTR
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM save_otr .

  DATA: lv_answer.
  DATA: l_valid.

  IF g_grid1->is_ready_for_input( ) EQ 0. "Display Mode
* Message
    MESSAGE s001(00) WITH 'in display mode, can not save'.
    RETURN.
  ENDIF.

*저장 확인 팝업
  CALL FUNCTION 'POPUP_TO_CONFIRM'
    EXPORTING
      titlebar       = 'Save'
*     DIAGNOSE_OBJECT             = ' '
      text_question  = 'Do you want to save?'
      text_button_1  = 'Yes'
*     ICON_BUTTON_1  = ' '
      text_button_2  = 'No'
*     ICON_BUTTON_2  = ' '
*     DEFAULT_BUTTON = '1'
*     DISPLAY_CANCEL_BUTTON       = 'X'
*     USERDEFINED_F1_HELP         = ' '
*     START_COLUMN   = 25
*     START_ROW      = 6
*     POPUP_TYPE     =
*     IV_QUICKINFO_BUTTON_1       = ' '
*     IV_QUICKINFO_BUTTON_2       = ' '
    IMPORTING
      answer         = lv_answer "Return values: '1', '2', 'A'
*   TABLES
*     PARAMETER      =
    EXCEPTIONS
      text_not_found = 1
      OTHERS         = 2.
*// 저장 Yes시에 탄다.
********************************
  CHECK lv_answer = '1'.
********************************

  CALL METHOD g_grid1->check_changed_data
    IMPORTING
      e_valid = l_valid.

*// 저장 수행
  PERFORM save_yes.

ENDFORM.                    " SAVE_OTR
*&---------------------------------------------------------------------*
*&      Form  SAVE_YES
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM save_yes .

*// 변경 데이타 담기.
  PERFORM get_changed_data.

  IF gt_save1[] IS INITIAL.
*// 변경된 Text가 없으면  메세지 처리
    MESSAGE s001(00) WITH 'no changes'.
    RETURN.
  ENDIF.

*// 변경 데이타 저장.
  PERFORM save_changed_data.
  MESSAGE s001(00) WITH 'Please see message.'.

ENDFORM.                    " SAVE_YES
*&---------------------------------------------------------------------*
*&      Form  GET_CHANGED_DATA
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM get_changed_data .

  DATA: ls_first LIKE LINE OF gt_first1.
  DATA: ls_outtab1 LIKE LINE OF gt_outtab1.

  REFRESH gt_save1.

  SORT gt_first1 BY alias_name langu.
  LOOP AT gt_outtab1 INTO ls_outtab1.
    READ TABLE gt_first1 INTO ls_first
      WITH KEY alias_name = ls_outtab1-alias_name
               langu = ls_outtab1-langu BINARY SEARCH.
    IF sy-subrc = 0.
      IF ls_outtab1-text <> ls_first-text.
        APPEND ls_outtab1 TO gt_save1.
      ENDIF.

    ENDIF.
  ENDLOOP.

ENDFORM.                    " GET_CHANGED_DATA
*&---------------------------------------------------------------------*
*&      Form  SAVE_CHANGED_DATA
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM save_changed_data .

  DATA: ls_save LIKE LINE OF gt_save1.
  DATA: ls_header TYPE btfr_head.
  DATA: ls_text TYPE btfr_text.
  DATA: ls_check           TYPE btfr_check.
  DATA: lt_check_result    TYPE btfr_check_result_tt.
  DATA: lv_timestamp       TYPE tzonref-tstamps.
  DATA: lt_text_tab        TYPE btfr_text_tt.
  DATA: lv_flag_cancelled  TYPE btfr_flag.
  DATA: lv_flag_string     TYPE btfr_f_string.
  DATA: lv_tabix           TYPE sy-tabix.

  LOOP AT gt_save1 INTO ls_save.

    READ TABLE gt_outtab1 WITH KEY alias_name = ls_save-alias_name
                                   langu = ls_save-langu.
    IF sy-subrc = 0.
      lv_tabix = sy-tabix.
    ENDIF.

    CLEAR: ls_header, ls_text.
    MOVE-CORRESPONDING ls_save TO ls_header.
    MOVE-CORRESPONDING ls_save TO ls_text.

*Get Text Length
    PERFORM get_text_length USING ls_text-text
                            CHANGING ls_text-length.

    REFRESH lt_text_tab.
    GET TIME STAMP FIELD lv_timestamp.
    ls_text-chan_name  = sy-uname.
    ls_text-chan_tstut = lv_timestamp.
    APPEND ls_text TO lt_text_tab.

    CLEAR: lv_flag_cancelled.
    CALL FUNCTION 'BTFR_CORR_CHECK'
      EXPORTING
        package            = ls_header-paket
        concept            = ls_header-concept
        flag_string        = lv_flag_string
      IMPORTING
        flag_cancelled     = lv_flag_cancelled
      EXCEPTIONS
        invalid_package    = 1
        permission_failure = 2
        OTHERS             = 3.

*Include request
    CLEAR: lv_flag_cancelled.
    CALL FUNCTION 'BTFR_CORR_INSERT'
      EXPORTING
        package            = ls_header-paket
        concept            = ls_header-concept
        flag_string        = lv_flag_string
      IMPORTING
        flag_cancelled     = lv_flag_cancelled
      EXCEPTIONS
        invalid_package    = 1
        permission_failure = 2
        OTHERS             = 3.
    "Request 선택 Pop-up에서 Cancel한 경우.
    IF lv_flag_cancelled = abap_true.
      "Action canceled
      MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno INTO gt_outtab1-message
              WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
      gt_outtab1-icon = '@5C@'.

    ELSE.

      "The concept has been included in request &1
      IF sy-msgid = 'BTFR_MESS' AND  sy-msgty = 'S' AND sy-msgno = '030'.
        gt_outtab1-trkorr = sy-msgv1.
      ENDIF.

*Enqueue
      CALL FUNCTION 'ENQUEUE_E_BTFR_HEAD'
        EXPORTING
          concept      = ls_header-concept
        EXCEPTIONS
          foreign_lock = 1
          OTHERS       = 3.

*Update data to OTR DB
      CALL FUNCTION 'BTFR_UPDATE'
        EXPORTING
          flag_string             = lv_flag_string
          text_tab                = lt_text_tab
        EXCEPTIONS
          concept_not_updated     = 1
          not_all_entries_updated = 2
          invalid_parameters      = 3
          OTHERS                  = 4.
      IF sy-subrc <> 0.
        MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno INTO gt_outtab1-message
                WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
        gt_outtab1-icon = '@5C@'.

      ELSE.
        MESSAGE ID 'BTFR_MESS' TYPE 'S' NUMBER '010' INTO gt_outtab1-message. "Text saved
        gt_outtab1-icon = '@5B@'.
      ENDIF.

* Dequeue
      CALL FUNCTION 'DEQUEUE_E_BTFR_HEAD'
        EXPORTING
          concept = ls_header-concept.

    ENDIF.

    MODIFY gt_outtab1 INDEX lv_tabix TRANSPORTING icon message trkorr.

  ENDLOOP.

ENDFORM.                    " SAVE_CHANGED_DATA
*&---------------------------------------------------------------------*
*&      Form  GET_TEXT_LENGTH
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      -->P_LS_TEXT_TEXT  text
*      <--P_LS_TEXT_LENGTH  text
*----------------------------------------------------------------------*
FORM get_text_length  USING    pv_text
                      CHANGING cv_length.

  DATA: lv_length     TYPE sotr_leng,
        lv_add_length TYPE sotr_leng.

  lv_length = strlen( pv_text ).
  IF lv_length > 20.
    lv_add_length = lv_length / 2.
    lv_length = lv_length + lv_add_length.
  ELSE.
    lv_length = lv_length + 10.
  ENDIF.

  IF lv_length > 255.
    lv_length = 255.
  ENDIF.

  cv_length = lv_length.

ENDFORM.                    " GET_TEXT_LENGTH
*&---------------------------------------------------------------------*
*&      Form  REFRESH_DISPLAY
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM refresh_display .

  CALL METHOD g_grid1->refresh_table_display
    EXCEPTIONS
      OTHERS = 1.

ENDFORM.                    " REFRESH_DISPLAY
*&---------------------------------------------------------------------*
*&      Form  ALV_CONTROL2
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM alv_control2 .

*Docking Container
  CREATE OBJECT g_dock_cont2
    EXPORTING
*     PARENT                      =
      repid                       = sy-repid
      dynnr                       = sy-dynnr
      side                        = cl_gui_docking_container=>dock_at_top
      extension                   = 500
    EXCEPTIONS
      cntl_error                  = 1
      cntl_system_error           = 2
      create_error                = 3
      lifetime_error              = 4
      lifetime_dynpro_dynpro_link = 5
      OTHERS                      = 6.

*Grid
  CREATE OBJECT g_grid2
    EXPORTING
      i_parent      = g_dock_cont2   "CONTAINER
      i_appl_events = 'X'.          "Application Event

*ALV CELLTAB
*  PERFORM INIT_ALV_STYLE2.
*ALV Grid Layout
  PERFORM alv_layout2.
*ALV Grid Field Catalog
  PERFORM alv_fieldcatalog2.
*ALV Grid Fuction Code
  PERFORM alv_exclude_fcode2.

*Calling the Method for ALV output
  CALL METHOD g_grid2->set_table_for_first_display
    EXPORTING
      is_layout            = gs_layout2
      i_save               = 'A'
      it_toolbar_excluding = gt_fcode2
    CHANGING
      it_fieldcatalog      = gt_fdcat2[]
      it_outtab            = gt_outtab2[].

*Set editable cells to ready for input initially
  CALL METHOD g_grid2->set_ready_for_input
    EXPORTING
      i_ready_for_input = 1.

ENDFORM.                    " ALV_CONTROL2
*&---------------------------------------------------------------------*
*&      Form  INIT_ALV_STYLE2
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM init_alv_style2 .

  DATA: lv_tabix TYPE sy-tabix.
  DATA: lt_celltab TYPE lvc_t_styl.

  LOOP AT gt_outtab2.
    lv_tabix = sy-tabix.
    REFRESH lt_celltab.

    PERFORM fill_celltab2 USING 'RW'
                         CHANGING lt_celltab.

    INSERT LINES OF lt_celltab INTO TABLE gt_outtab2-celltab.
    MODIFY gt_outtab2 INDEX lv_tabix.
  ENDLOOP.

ENDFORM.                    " INIT_ALV_STYLE2
*&---------------------------------------------------------------------*
*&      Form  FILL_CELLTAB2
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      -->P_2349   text
*      <--P_LT_CELLTAB  text
*----------------------------------------------------------------------*
FORM fill_celltab2  USING  VALUE(pv_mode)
                  CHANGING pt_celltab TYPE lvc_t_styl.

  DATA: ls_celltab TYPE lvc_s_styl,
        lv_mode    TYPE raw4.

  IF pv_mode EQ 'RW'.
    lv_mode = cl_gui_alv_grid=>mc_style_enabled.
  ELSE.
    lv_mode = cl_gui_alv_grid=>mc_style_disabled.
  ENDIF.

  ls_celltab-fieldname = 'PAKET'.
  ls_celltab-style = cl_gui_alv_grid=>mc_style_disabled.
  INSERT ls_celltab INTO TABLE pt_celltab.

  ls_celltab-fieldname = 'ALIAS_NAME'.
  ls_celltab-style = lv_mode.
  INSERT ls_celltab INTO TABLE pt_celltab.

  ls_celltab-fieldname = 'OBJTYPE'.
  ls_celltab-style = lv_mode.
  INSERT ls_celltab INTO TABLE pt_celltab.

  ls_celltab-fieldname = 'EN_TEXT'.
  ls_celltab-style = lv_mode.
  INSERT ls_celltab INTO TABLE pt_celltab.

  ls_celltab-fieldname = 'KO_TEXT'.
  ls_celltab-style = lv_mode.
  INSERT ls_celltab INTO TABLE pt_celltab.

  ls_celltab-fieldname = 'ZH_TEXT'.
  ls_celltab-style = lv_mode.
  INSERT ls_celltab INTO TABLE pt_celltab.

  ls_celltab-fieldname = 'ZF_TEXT'.
  ls_celltab-style = lv_mode.
  INSERT ls_celltab INTO TABLE pt_celltab.

  ls_celltab-fieldname = 'CONCEPT'.
  ls_celltab-style = cl_gui_alv_grid=>mc_style_disabled.
  INSERT ls_celltab INTO TABLE pt_celltab.

ENDFORM.                    " FILL_CELLTAB2
*&---------------------------------------------------------------------*
*&      Form  ALV_LAYOUT2
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM alv_layout2 .

  gs_layout2-stylefname = 'CELLTAB'.
  gs_layout2-no_rowmark = abap_false.

ENDFORM.                    " ALV_LAYOUT2
*&---------------------------------------------------------------------*
*&      Form  append_catalog2
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
FORM append_catalog2 USING p_key
                          p_field
                          p_text
                          p_length
                          p_ref_table
                          p_ref_field
                          p_just
                          p_check
                          p_hotspot
                          p_no_zero
                          p_edit.

  DATA: ls_fldcat TYPE lvc_s_fcat.
  CLEAR ls_fldcat.

  g_pos2 = g_pos2 + 1.
  ls_fldcat-col_pos   = g_pos2.
  ls_fldcat-key      = p_key.
  ls_fldcat-fieldname = p_field.
  ls_fldcat-coltext   = p_text.

  ls_fldcat-scrtext_m = p_text.
  ls_fldcat-scrtext_s = p_text.
  ls_fldcat-outputlen = p_length.
  ls_fldcat-ref_table = p_ref_table.
  ls_fldcat-ref_field = p_ref_field.
  ls_fldcat-just      = p_just.
  ls_fldcat-checkbox  = p_check.
  ls_fldcat-hotspot   = p_hotspot.
  ls_fldcat-no_zero   = p_no_zero.
  ls_fldcat-edit   = p_edit.

  APPEND ls_fldcat TO gt_fdcat2.

ENDFORM.                    " APPEND_CATALOG2
*&---------------------------------------------------------------------*
*&      Form  ALV_FIELDCATALOG2
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM alv_fieldcatalog2 .

  PERFORM append_catalog2 USING:
  'X' 'PAKET'         'Package'      '14'   'SOTR_HEAD'  'PAKET'  ''  ''  ''  '' '',
  'X' 'ALIAS_NAME'    'Alias'        '40'   'SOTR_HEAD'  'ALIAS_NAME'  ''  ''  ''  '' 'X',
  ' ' 'OBJTYPE'       'Object Type'  '10'   'SOTR_TREE'  'OBJECT'  ''  ''  ''  '' '',
  ' ' 'EN_TEXT'       'English'      '20'   'SOTR_TEXT'  'TEXT'  ''  ''  ''  '' 'X',
  ' ' 'KO_TEXT'       'Korean'       '20'   'SOTR_TEXT'  'TEXT'  ''  ''  ''  '' 'X',
  ' ' 'ZH_TEXT'       'Chinese'      '20'   'SOTR_TEXT'  'TEXT'  ''  ''  ''  '' 'X',
  ' ' 'ZF_TEXT'       'Chinese trad.'      '20'   'SOTR_TEXT'  'TEXT'  ''  ''  ''  '' 'X',
  ' ' 'ICON'          ' '            '02'   ''  ''  ''  ''  ''  '' '',
  ' ' 'MESSAGE'       'Message'      '30'   ''  ''  ''  ''  ''  '' ''.

ENDFORM.                    " ALV_FIELDCATALOG2
*&---------------------------------------------------------------------*
*&      Form  ALV_EXCLUDE_FCODE2
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM alv_exclude_fcode2 .

  REFRESH gt_fcode2.

  PERFORM alv_append_exclude_function
        TABLES gt_fcode2 "<TABLE>
*        USING : cl_gui_alv_grid=>mc_fc_excl_all. " ** 툴바 모두제거 **
        USING :
                cl_gui_alv_grid=>mc_fc_loc_undo, " 실행취소&LOCAL&UNDO
                cl_gui_alv_grid=>mc_fc_auf,      " 소계확장 &AUF
                cl_gui_alv_grid=>mc_fc_average,  " &AVERAGE
                cl_gui_alv_grid=>mc_fc_back_classic,
                cl_gui_alv_grid=>mc_fc_call_abc, " &ABC
                cl_gui_alv_grid=>mc_fc_call_chain,
                cl_gui_alv_grid=>mc_fc_call_crbatch,
                cl_gui_alv_grid=>mc_fc_call_crweb,
                cl_gui_alv_grid=>mc_fc_call_lineitems,
                cl_gui_alv_grid=>mc_fc_call_master_data,
                cl_gui_alv_grid=>mc_fc_call_more,
                cl_gui_alv_grid=>mc_fc_call_report,
                cl_gui_alv_grid=>mc_fc_call_xint,
                cl_gui_alv_grid=>mc_fc_call_xxl,
                cl_gui_alv_grid=>mc_fc_col_invisible,
                cl_gui_alv_grid=>mc_fc_col_optimize,
                cl_gui_alv_grid=>mc_fc_current_variant,
                cl_gui_alv_grid=>mc_fc_data_save,
*                CL_GUI_ALV_GRID=>MC_FC_DELETE_FILTER,
*                CL_GUI_ALV_GRID=>MC_FC_DESELECT_ALL,
                 cl_gui_alv_grid=>mc_fc_detail,
                cl_gui_alv_grid=>mc_fc_expcrdata,
                cl_gui_alv_grid=>mc_fc_expcrdesig,
                cl_gui_alv_grid=>mc_fc_expcrtempl,
                cl_gui_alv_grid=>mc_fc_expmdb,
                cl_gui_alv_grid=>mc_fc_extend,
                cl_gui_alv_grid=>mc_fc_f4,
                cl_gui_alv_grid=>mc_fc_filter,
*                CL_GUI_ALV_GRID=>MC_FC_FIND,
                cl_gui_alv_grid=>mc_fc_fix_columns,
                cl_gui_alv_grid=>mc_fc_graph,
                cl_gui_alv_grid=>mc_fc_help,
                cl_gui_alv_grid=>mc_fc_info,
                cl_gui_alv_grid=>mc_fc_load_variant,
                cl_gui_alv_grid=>mc_fc_loc_copy,          " 행 카피.
                cl_gui_alv_grid=>mc_fc_html,
*                CL_GUI_ALV_GRID=>MC_FC_LOC_COPY_ROW,      " 행 카피.
                cl_gui_alv_grid=>mc_fc_loc_cut,           " 가위.
*                CL_GUI_ALV_GRID=>MC_FC_LOC_DELETE_ROW,    " 행삭제.
                cl_gui_alv_grid=>mc_fc_loc_insert_row,    " 행삽입.
                cl_gui_alv_grid=>mc_fc_loc_move_row,
                cl_gui_alv_grid=>mc_fc_loc_append_row,    " 라인생성.
                cl_gui_alv_grid=>mc_fc_loc_paste,         " 겹쳐쓰기.
                cl_gui_alv_grid=>mc_fc_loc_paste_new_row, " 겹쳐쓰기.
                cl_gui_alv_grid=>mc_fc_maintain_variant,
                cl_gui_alv_grid=>mc_fc_maximum,
                cl_gui_alv_grid=>mc_fc_minimum,
*                CL_GUI_ALV_GRID=>MC_FC_PC_FILE,  "Excel Exporting
*                CL_GUI_ALV_GRID=>MC_FC_PRINT,
*                CL_GUI_ALV_GRID=>MC_FC_PRINT_BACK,
*                CL_GUI_ALV_GRID=>MC_FC_PRINT_PREV,
                cl_gui_alv_grid=>mc_fc_refresh,
                cl_gui_alv_grid=>mc_fc_reprep,
                cl_gui_alv_grid=>mc_fc_save_variant,
*                CL_GUI_ALV_GRID=>MC_FC_SELECT_ALL.
                cl_gui_alv_grid=>mc_fc_send,
                cl_gui_alv_grid=>mc_fc_separator,
*                CL_GUI_ALV_GRID=>MC_FC_SORT,
*                CL_GUI_ALV_GRID=>MC_FC_SORT_ASC,
*                CL_GUI_ALV_GRID=>MC_FC_SORT_DSC,
                cl_gui_alv_grid=>mc_fc_subtot,
                cl_gui_alv_grid=>mc_mb_sum,
                cl_gui_alv_grid=>mc_fc_sum,
                cl_gui_alv_grid=>mc_fc_to_office,
                cl_gui_alv_grid=>mc_fc_to_rep_tree,
                cl_gui_alv_grid=>mc_fc_unfix_columns,
*                CL_GUI_ALV_GRID=>MC_FC_VIEWS,
                cl_gui_alv_grid=>mc_fc_view_crystal,
                cl_gui_alv_grid=>mc_fc_view_excel,
*                CL_GUI_ALV_GRID=>MC_FC_VIEW_GRID,
                cl_gui_alv_grid=>mc_fc_word_processor
                .

ENDFORM.                    " ALV_EXCLUDE_FCODE2
*&---------------------------------------------------------------------*
*&      Form  APPEND_CREA_DATA
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM append_crea_data .

  CLEAR: gv_paket.
  gv_paket = p_pkgc.

  REFRESH: gt_outtab2.
  CLEAR: gt_outtab2.

  gt_outtab2-paket = gv_paket.
  CONCATENATE gv_paket '/' INTO gt_outtab2-alias_name.
  gt_outtab2-objtype = 'WDYV'.

  APPEND gt_outtab2.


ENDFORM.                    " APPEND_CREA_DATA
*&---------------------------------------------------------------------*
*&      Form  CREATE_OTR
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM create_otr .

  DATA: lv_answer.
  DATA: lv_valid.
  DATA: lv_err.

  IF g_grid2->is_ready_for_input( ) EQ 0. "Display Mode
* Message
    MESSAGE s001(00) WITH 'in display mode, can not save'.
    RETURN.
  ENDIF.

  CALL METHOD g_grid2->check_changed_data
    IMPORTING
      e_valid = lv_valid.

*// 저장전 데이타 체크
  PERFORM check_create_date CHANGING lv_err.
  PERFORM refresh_display2.
  IF lv_err = abap_true.
    RETURN.
  ENDIF.

*저장 확인 팝업
  CALL FUNCTION 'POPUP_TO_CONFIRM'
    EXPORTING
      titlebar       = 'Save'
*     DIAGNOSE_OBJECT             = ' '
      text_question  = 'Do you want to save?'
      text_button_1  = 'Yes'
*     ICON_BUTTON_1  = ' '
      text_button_2  = 'No'
*     ICON_BUTTON_2  = ' '
*     DEFAULT_BUTTON = '1'
*     DISPLAY_CANCEL_BUTTON       = 'X'
*     USERDEFINED_F1_HELP         = ' '
*     START_COLUMN   = 25
*     START_ROW      = 6
*     POPUP_TYPE     =
*     IV_QUICKINFO_BUTTON_1       = ' '
*     IV_QUICKINFO_BUTTON_2       = ' '
    IMPORTING
      answer         = lv_answer "Return values: '1', '2', 'A'
*   TABLES
*     PARAMETER      =
    EXCEPTIONS
      text_not_found = 1
      OTHERS         = 2.
*// 저장 Yes시에 탄다.
********************************
  CHECK lv_answer = '1'.
********************************

*// 저장 수행
  PERFORM create_yes.
  PERFORM refresh_display2.
  PERFORM readonly_display2.

ENDFORM.                    " CREATE_OTR
*&---------------------------------------------------------------------*
*&      Form  CREATE_YES
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM create_yes .

  DATA: lv_subrc TYPE sy-subrc.

*첫번째 OTR생성때만 Request No.선택 팝업을 띄워 생성할 Request No.를 구해온다.
  PERFORM create_first_otr CHANGING lv_subrc.
  PERFORM message_subrc USING lv_subrc.

*첫번째 OTR이 정상 생성되어 Assigned Request No.를 가져온 경우
*다음 OTR은 BDC로 처리.
**********************************
  CHECK gv_trkorr IS NOT INITIAL AND ( lv_subrc = 0 OR lv_subrc = 4 ).
**********************************
  PERFORM create_bdc_otr.

ENDFORM.                    " CREATE_YES
*&---------------------------------------------------------------------*
*&      Form  CREATE_BDC_DATA
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM create_bdc_data .

  DATA: lv_length TYPE sotr_leng.
  DATA: lv_leng_cha(3).
  DATA: lv_subrc TYPE sy-subrc.
  DATA: lv_tabix TYPE sy-tabix.
  DATA: lv_msgtx TYPE char200.
  DATA : lv_length_en TYPE sotr_leng,
         lv_length_ko TYPE sotr_leng,
         lv_length_zh TYPE sotr_leng,
         lv_length_zf TYPE sotr_leng.


  LOOP AT gt_outtab2.
    lv_tabix = sy-tabix.

    CLEAR: bdcdata, bdcdata[].

    PERFORM get_text_crea_length    USING gt_outtab2-en_text
                                          abap_true
                                 CHANGING lv_length_en.
    PERFORM get_text_crea_length    USING gt_outtab2-ko_text
                                          abap_true
                                 CHANGING lv_length_ko.
    PERFORM get_text_crea_length    USING gt_outtab2-zh_text
                                          abap_true
                                 CHANGING lv_length_zh.
    PERFORM get_text_crea_length    USING gt_outtab2-zf_text
                                          abap_true
                                 CHANGING lv_length_zf.
    "
    CLEAR lv_length.
    " 한글 텍스트 자릿수와 영문 자릿수 체크 - 가장 긴 텍스트 기준으로 생성
    IF lv_length_ko GT lv_length_en.
      lv_length = lv_length_ko.
    ELSE.
      lv_length = lv_length_en.
    ENDIF.
    " 중문 자릿수 체크
    IF lv_length LT lv_length_zh.
      lv_length = lv_length_zh.
    ENDIF.
    IF lv_length LT lv_length_zf.
      lv_length = lv_length_zf.
    ENDIF.

****************************************
    IF lv_tabix = 1.
****************************************
      PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0100'.
      PERFORM bdc_field  USING:
            'BDC_CURSOR'                'G_DYNP_0100-ALIAS',
            'BDC_OKCODE'                '=MAINTAIN',
            'G_DYNP_0100-RAD_T'         'X',
            'G_DYNP_0100-SLANG'         'EN',
            'G_DYNP_0100-ALIAS'         gt_outtab2-alias_name.

      PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0200'.
      PERFORM bdc_field  USING:
            'BDC_OKCODE'                '=CNTXT_MAINTAIN',
            'BDC_SUBSCR'                'SAPLSOTR_EDIT                           0205GL_SUB_TC1'.

      PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0105'.
      PERFORM bdc_field  USING:
            'BDC_CURSOR'                'G_DYNP_0105-COUNTRY',
            'BDC_OKCODE'                '=CONTINUE'.

*Korean
      lv_leng_cha = lv_length.
      PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0200'.
      PERFORM bdc_field  USING:
            'BDC_CURSOR'                  'G_DYNP_0200-SLANG',
            'BDC_OKCODE'                  '=SAVE',
            'G_DYNP_0200-SLANG'           'KO',
            'G_DYNP_0200-PACKAGE'         gt_outtab2-paket,
            'G_DYNP_0200-ALIAS'           gt_outtab2-alias_name,
            'G_DYNP_0200-OBJTYPE'         gt_outtab2-objtype,
            'BDC_SUBSCR'                  'SAPLSOTR_EDIT                           0205GL_SUB_TC1',
            'G_DYNP_0205_LENGTH'          lv_leng_cha,
            'G_DYNP_0205_TEXT'            gt_outtab2-ko_text.

*Chinese
      lv_leng_cha = lv_length.
      PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0200'.
      PERFORM bdc_field  USING:
            'BDC_CURSOR'                  'G_DYNP_0200-SLANG',
            'BDC_OKCODE'                  '=SAVE',
            'G_DYNP_0200-SLANG'           'ZH',
            'G_DYNP_0200-PACKAGE'         gt_outtab2-paket,
            'G_DYNP_0200-ALIAS'           gt_outtab2-alias_name,
            'G_DYNP_0200-OBJTYPE'         gt_outtab2-objtype,
            'BDC_SUBSCR'                  'SAPLSOTR_EDIT                           0205GL_SUB_TC1',
            'G_DYNP_0205_LENGTH'          lv_leng_cha,
            'G_DYNP_0205_TEXT'            gt_outtab2-zh_text.

*Chinese
      lv_leng_cha = lv_length.
      PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0200'.
      PERFORM bdc_field  USING:
            'BDC_CURSOR'                  'G_DYNP_0200-SLANG',
            'BDC_OKCODE'                  '=SAVE',
            'G_DYNP_0200-SLANG'           'ZF',
            'G_DYNP_0200-PACKAGE'         gt_outtab2-paket,
            'G_DYNP_0200-ALIAS'           gt_outtab2-alias_name,
            'G_DYNP_0200-OBJTYPE'         gt_outtab2-objtype,
            'BDC_SUBSCR'                  'SAPLSOTR_EDIT                           0205GL_SUB_TC1',
            'G_DYNP_0205_LENGTH'          lv_leng_cha,
            'G_DYNP_0205_TEXT'            gt_outtab2-zf_text.

      PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0200'.
      PERFORM bdc_field  USING:
            'BDC_OKCODE'                  '/EEND',
            'BDC_SUBSCR'                  'SAPLSOTR_EDIT                           0205GL_SUB_TC1',
            'BDC_CURSOR'                  'G_DYNP_0205_LENGTH'.

*****************************************
    ELSEIF lv_tabix > 1.
****************************************

************************************************************
      IF gv_non_org_system = abap_true. "Non-Orginal System
************************************************************
*English
        PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0100'.
        PERFORM bdc_field  USING:
              'BDC_CURSOR'                'G_DYNP_0100-ALIAS',
              'BDC_OKCODE'                '=CREATE',
              'G_DYNP_0100-RAD_T'         'X',
              'G_DYNP_0100-SLANG'         'EN',
              'G_DYNP_0100-STEXT'         gt_outtab2-en_text,
              'G_DYNP_0100-ALIAS'         gt_outtab2-alias_name.

        lv_leng_cha = lv_length.
        PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0200'.
        PERFORM bdc_field  USING:
              'BDC_CURSOR'                'G_DYNP_0200-OBJTYPE',
              'BDC_OKCODE'                '=SAVE',
              'G_DYNP_0200-SLANG'         'EN',
              'G_DYNP_0200-PACKAGE'       gt_outtab2-paket,
              'G_DYNP_0200-ALIAS'         gt_outtab2-alias_name,
              'G_DYNP_0200-OBJTYPE'       gt_outtab2-objtype,
              'BDC_SUBSCR'                'SAPLSOTR_EDIT                           0205GL_SUB_TC1',
              'G_DYNP_0205_LENGTH'        lv_leng_cha,
              'G_DYNP_0205_TEXT'          gt_outtab2-en_text.

        PERFORM bdc_dynpro USING 'SAPLSPO1' '0500'.
        PERFORM bdc_field  USING:
              'BDC_OKCODE'                '=OPT1',
              'BDC_SUBSCR'                'SAPLSPO1                                0501SUBSCREEN',
              'BDC_CURSOR'                'TEXT_TAB1-TEXTZEILE(01)'.

        PERFORM bdc_dynpro USING 'SAPLSTRD' '0300'.
        PERFORM bdc_field  USING:
              'BDC_CURSOR'                'KO008-TRKORR',
              'BDC_OKCODE'                '=LOCK',
              'KO008-TRKORR'              gv_trkorr.

        PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0200'.
        PERFORM bdc_field  USING:
              'BDC_OKCODE'                '=CNTXT_MAINTAIN',
              'BDC_SUBSCR'                'SAPLSOTR_EDIT                           0205GL_SUB_TC1',
              'BDC_CURSOR'                'G_DYNP_0205_LENGTH',
              'G_DYNP_0205_LENGTH'        lv_leng_cha,
              'G_DYNP_0205_TEXT'          gt_outtab2-en_text.

        PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0105'.
        PERFORM bdc_field  USING:
              'BDC_CURSOR'                'G_DYNP_0105-COUNTRY',
              'BDC_OKCODE'                '=CONTINUE'.

*Korean
        lv_leng_cha = lv_length.
        PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0200'.
        PERFORM bdc_field  USING:
              'BDC_CURSOR'                  'G_DYNP_0200-SLANG',
              'BDC_OKCODE'                 '=SAVE',
              'G_DYNP_0200-SLANG'	         'KO',
              'G_DYNP_0200-PACKAGE'	        gt_outtab2-paket,
              'G_DYNP_0200-ALIAS'           gt_outtab2-alias_name,
              'G_DYNP_0200-OBJTYPE'         gt_outtab2-objtype,
              'BDC_SUBSCR'                  'SAPLSOTR_EDIT                           0205GL_SUB_TC1',
              'G_DYNP_0205_LENGTH'          lv_leng_cha,
              'G_DYNP_0205_TEXT'            gt_outtab2-ko_text.

*Chinese
        lv_leng_cha = lv_length.
        PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0200'.
        PERFORM bdc_field  USING:
              'BDC_CURSOR'               	 'G_DYNP_0200-SLANG',
              'BDC_OKCODE'                 '=SAVE',
              'G_DYNP_0200-SLANG'	         'ZH',
              'G_DYNP_0200-PACKAGE'	        gt_outtab2-paket,
              'G_DYNP_0200-ALIAS'           gt_outtab2-alias_name,
              'G_DYNP_0200-OBJTYPE'         gt_outtab2-objtype,
              'BDC_SUBSCR'                  'SAPLSOTR_EDIT                           0205GL_SUB_TC1',
              'G_DYNP_0205_LENGTH'          lv_leng_cha,
              'G_DYNP_0205_TEXT'            gt_outtab2-zh_text.

*Chinese
        lv_leng_cha = lv_length.
        PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0200'.
        PERFORM bdc_field  USING:
              'BDC_CURSOR'               	 'G_DYNP_0200-SLANG',
              'BDC_OKCODE'                 '=SAVE',
              'G_DYNP_0200-SLANG'	         'ZF',
              'G_DYNP_0200-PACKAGE'	        gt_outtab2-paket,
              'G_DYNP_0200-ALIAS'           gt_outtab2-alias_name,
              'G_DYNP_0200-OBJTYPE'         gt_outtab2-objtype,
              'BDC_SUBSCR'                  'SAPLSOTR_EDIT                           0205GL_SUB_TC1',
              'G_DYNP_0205_LENGTH'          lv_leng_cha,
              'G_DYNP_0205_TEXT'            gt_outtab2-zf_text.

        PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0200'.
        PERFORM bdc_field  USING:
              'BDC_OKCODE'                 '/EEND',
              'BDC_SUBSCR'                  'SAPLSOTR_EDIT                           0205GL_SUB_TC1',
              'BDC_CURSOR'               	  'G_DYNP_0205_LENGTH'.


***********************************************
      ELSE.  "Orginal System
***********************************************
*English
        PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0100'.
        PERFORM bdc_field  USING:
              'BDC_CURSOR'                'G_DYNP_0100-ALIAS',
              'BDC_OKCODE'                '=CREATE',
              'G_DYNP_0100-RAD_T'         'X',
              'G_DYNP_0100-SLANG'         'EN',
              'G_DYNP_0100-STEXT'         gt_outtab2-en_text,
              'G_DYNP_0100-ALIAS'         gt_outtab2-alias_name.

        lv_leng_cha = lv_length.
        PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0200'.
        PERFORM bdc_field  USING:
              'BDC_CURSOR'                'G_DYNP_0200-OBJTYPE',
              'BDC_OKCODE'                '=SAVE',
              'G_DYNP_0200-SLANG'         'EN',
              'G_DYNP_0200-PACKAGE'       gt_outtab2-paket,
              'G_DYNP_0200-ALIAS'         gt_outtab2-alias_name,
              'G_DYNP_0200-OBJTYPE'       gt_outtab2-objtype,
              'BDC_SUBSCR'                'SAPLSOTR_EDIT                           0205GL_SUB_TC1',
              'G_DYNP_0205_LENGTH'        lv_leng_cha,
              'G_DYNP_0205_TEXT'          gt_outtab2-en_text.

        PERFORM bdc_dynpro USING 'SAPLSTRD' '0300'.
        PERFORM bdc_field  USING:
              'BDC_CURSOR'                'KO008-TRKORR',
              'BDC_OKCODE'                '=LOCK',
              'KO008-TRKORR'              gv_trkorr.

        PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0200'.
        PERFORM bdc_field  USING:
              'BDC_OKCODE'                '=CNTXT_MAINTAIN',
              'BDC_SUBSCR'                'SAPLSOTR_EDIT                           0205GL_SUB_TC1',
              'BDC_CURSOR'                'G_DYNP_0205_LENGTH',
              'G_DYNP_0205_LENGTH'        lv_leng_cha,
              'G_DYNP_0205_TEXT'          gt_outtab2-en_text.

        PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0105'.
        PERFORM bdc_field  USING:
              'BDC_CURSOR'                'G_DYNP_0105-COUNTRY',
              'BDC_OKCODE'                '=CONTINUE'.

*Korean
        lv_leng_cha = lv_length.
        PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0200'.
        PERFORM bdc_field  USING:
              'BDC_CURSOR'                  'G_DYNP_0200-SLANG',
              'BDC_OKCODE'                 '=SAVE',
              'G_DYNP_0200-SLANG'	         'KO',
              'G_DYNP_0200-PACKAGE'	        gt_outtab2-paket,
              'G_DYNP_0200-ALIAS'           gt_outtab2-alias_name,
              'G_DYNP_0200-OBJTYPE'         gt_outtab2-objtype,
              'BDC_SUBSCR'                  'SAPLSOTR_EDIT                           0205GL_SUB_TC1',
              'G_DYNP_0205_LENGTH'          lv_leng_cha,
              'G_DYNP_0205_TEXT'            gt_outtab2-ko_text.

*Chinese
        lv_leng_cha = lv_length.
        PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0200'.
        PERFORM bdc_field  USING:
              'BDC_CURSOR'               	 'G_DYNP_0200-SLANG',
              'BDC_OKCODE'                 '=SAVE',
              'G_DYNP_0200-SLANG'	         'ZH',
              'G_DYNP_0200-PACKAGE'	        gt_outtab2-paket,
              'G_DYNP_0200-ALIAS'           gt_outtab2-alias_name,
              'G_DYNP_0200-OBJTYPE'         gt_outtab2-objtype,
              'BDC_SUBSCR'                  'SAPLSOTR_EDIT                           0205GL_SUB_TC1',
              'G_DYNP_0205_LENGTH'          lv_leng_cha,
              'G_DYNP_0205_TEXT'            gt_outtab2-zh_text.

*Chinese
        lv_leng_cha = lv_length.
        PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0200'.
        PERFORM bdc_field  USING:
              'BDC_CURSOR'               	 'G_DYNP_0200-SLANG',
              'BDC_OKCODE'                 '=SAVE',
              'G_DYNP_0200-SLANG'	         'ZF',
              'G_DYNP_0200-PACKAGE'	        gt_outtab2-paket,
              'G_DYNP_0200-ALIAS'           gt_outtab2-alias_name,
              'G_DYNP_0200-OBJTYPE'         gt_outtab2-objtype,
              'BDC_SUBSCR'                  'SAPLSOTR_EDIT                           0205GL_SUB_TC1',
              'G_DYNP_0205_LENGTH'          lv_leng_cha,
              'G_DYNP_0205_TEXT'            gt_outtab2-zf_text.

        PERFORM bdc_dynpro USING 'SAPLSOTR_EDIT' '0200'.
        PERFORM bdc_field  USING:
              'BDC_OKCODE'                 '/EEND',
              'BDC_SUBSCR'                  'SAPLSOTR_EDIT                           0205GL_SUB_TC1',
              'BDC_CURSOR'               	  'G_DYNP_0205_LENGTH'.

      ENDIF.
    ENDIF.

*** Call Transaction 'SOTR_EDIT' ********************************
    CALL TRANSACTION 'SOTR_EDIT' USING bdcdata OPTIONS FROM gs_opt.
******************************************************************
    lv_subrc = sy-subrc.

    IF lv_subrc EQ 0 OR lv_subrc = 1001.
      lv_msgtx = 'Text has been created'. "Message no. SOTR_MESS061

    ELSE.
*에러 출력
      CALL FUNCTION 'FI_MESSAGE_TEXT_GET'
        EXPORTING
*         I_LANGU          = SY-LANGU
          i_msgid          = sy-msgid
          i_msgno          = sy-msgno
          i_msgty          = sy-msgty
          i_msgv1          = sy-msgv1
          i_msgv2          = sy-msgv2
          i_msgv3          = sy-msgv3
          i_msgv4          = sy-msgv4
*         I_TOTAL          =
        IMPORTING
          e_msgtx          = lv_msgtx
        EXCEPTIONS
          no_message_found = 1
          msgid_missing    = 2
          msgno_missing    = 3
          OTHERS           = 4.
      IF sy-subrc <> 0.
* Implement suitable error handling here
      ENDIF.

    ENDIF.

    PERFORM update_outtab2 USING lv_subrc
                                 lv_msgtx
                                 lv_tabix.
  ENDLOOP.

ENDFORM.                    " CREATE_BDC_DATA
*&---------------------------------------------------------------------*
*&      Form  SET_OPTIONS
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM set_options .

  CLEAR: gs_opt.
  gs_opt-dismode = 'N'.
  gs_opt-updmode = 'S'.
  gs_opt-defsize = 'X'.

ENDFORM.                    " SET_OPTIONS
*&---------------------------------------------------------------------*
*&      Form  CREATE_FIRST_OTR
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM create_first_otr CHANGING cv_subrc.

  DATA: ls_header TYPE btfr_head.
  DATA: ls_text TYPE btfr_text.
  DATA: ls_check TYPE btfr_check.
  DATA: lt_result TYPE btfr_check_result_tt.
  DATA: ls_result TYPE btfr_check_result.
  DATA: ls_text_db TYPE sotr_text.
  DATA: ls_btfr TYPE btfr_text.
  DATA: lt_text_tab TYPE sotr_text_tt.
  DATA: ls_text_tab TYPE sotr_text.
  DATA: lv_timestamp TYPE tzonref-tstamps.
  DATA: ls_text_wa TYPE btfr_text.
  DATA: lt_text_wa TYPE btfr_text_tt.
  DATA: lv_concept TYPE sysuuid-c.
  DATA: lv_flag_cancelled TYPE btfr_flag.
  DATA: lv_flag_string TYPE btfr_f_string.
  DATA: lv_subrc TYPE sy-subrc.
  DATA: lv_length    TYPE sotr_leng,
        lv_length_en TYPE sotr_leng,
        lv_length_ko TYPE sotr_leng,
        lv_length_zh TYPE sotr_leng,
        lv_length_zf TYPE sotr_leng.

  DATA: lt_string_tab TYPE btfr_string_tt.
  DATA: lv_source_langu TYPE spras.
  DATA: lv_answer,
        lv_text(400).
  CONSTANTS: cl_answer_yes VALUE '1'.   "left button

  CLEAR: gv_non_org_system.

  READ TABLE gt_outtab2 INDEX 1.
************************
  CHECK sy-subrc = 0.
************************

  "Header
  MOVE-CORRESPONDING gt_outtab2 TO ls_header.
  ls_header-crea_lan = 'E'.
  CALL FUNCTION 'BTFR_OBJTYPE_ATTRIBUTES_GET'
    EXPORTING
      object_type         = gt_outtab2-objtype
    IMPORTING
      object_vector       = ls_header-objid_vec
    EXCEPTIONS
      invalid_object_type = 1
      no_attributes       = 2
      OTHERS              = 3.
  "Text
  MOVE-CORRESPONDING gt_outtab2 TO ls_text.
  ls_text-langu = 'E'.
  ls_text-text = gt_outtab2-en_text.
*Get Text Length

*  PERFORM GET_TEXT_LENGTH USING LS_TEXT-TEXT
*                          CHANGING LS_TEXT-LENGTH.
  PERFORM get_text_crea_length    USING gt_outtab2-en_text
                                        abap_true
                               CHANGING lv_length_en.
  PERFORM get_text_crea_length    USING gt_outtab2-ko_text
                                        abap_true
                               CHANGING lv_length_ko.
  PERFORM get_text_crea_length    USING gt_outtab2-zh_text
                                        abap_true
                               CHANGING lv_length_zh.
  PERFORM get_text_crea_length    USING gt_outtab2-zf_text
                                        abap_true
                               CHANGING lv_length_zf.

  " 한글 텍스트 자릿수와 영문 자릿수 체크 - 가장 긴 텍스트 기준으로 생성
  IF lv_length_ko GT lv_length_en.
    lv_length = lv_length_ko.
  ELSE.
    lv_length = lv_length_en.
  ENDIF.
  " 중문 자릿수 체크
  IF lv_length LT lv_length_zh.
    lv_length = lv_length_zh.
  ENDIF.
  IF lv_length LT lv_length_zf.
    lv_length = lv_length_zf.
  ENDIF.

  ls_text-length = lv_length.

*// Check Input
  ls_check-alias_name = 'X'.
  CALL FUNCTION 'BTFR_CHECK'
    EXPORTING
      langu           = sy-langu
      alias           = ls_header-alias_name
      check           = ls_check
      flag_string     = lv_flag_string
    IMPORTING
      check_result    = lt_result
    CHANGING
      btfr_head       = ls_header
    EXCEPTIONS
      invalid_package = 1
      OTHERS          = 2.
  IF sy-subrc = 0.
    DESCRIBE TABLE lt_result LINES sy-tabix.
    IF sy-tabix > 0.
      READ TABLE lt_result INTO ls_result INDEX 1.
*      P_SUBRC = 4.
*      MESSAGE ID     L_RESULT_WA-ID
*              TYPE   'I'
*              NUMBER L_RESULT_WA-NR
*              WITH   L_RESULT_WA-VAR1.
    ENDIF.
  ENDIF.
  IF lv_length > 255.
    lv_length = 255.
  ENDIF.

*// Save Concept
  REFRESH lt_text_tab.
  MOVE-CORRESPONDING ls_text TO ls_text_db.
  ls_btfr-text = ls_text_db-text.
  "Set Length
  PERFORM get_compare_text USING ls_btfr-text
                        CHANGING lv_length
                                 ls_btfr-length.
  ls_text_db-length = ls_btfr-length.
  APPEND ls_text_db TO lt_text_tab.

* create - btfr_create
  GET TIME STAMP FIELD lv_timestamp.
  PERFORM get_concept_id CHANGING lv_concept.
  ls_header-concept = lv_concept.
  ls_header-crea_name  = sy-uname.
  ls_header-crea_tstut = lv_timestamp.
  ls_header-chan_name  = sy-uname.
  ls_header-chan_tstut = lv_timestamp.

  CLEAR: ls_check, lt_result[].
  ls_check-alias_name    = 'X'.
  ls_check-master_system = 'X'.
  CALL FUNCTION 'BTFR_CHECK'
    EXPORTING
      langu           = sy-langu
      alias           = ls_header-alias_name
      check           = ls_check
      flag_string     = ''
    IMPORTING
      check_result    = lt_result
    CHANGING
      btfr_head       = ls_header
    EXCEPTIONS
      invalid_package = 1
      OTHERS          = 2.
  IF sy-subrc <> 0.
*    MESSAGE ID     sy-msgid
*            TYPE   sy-msgty
*            NUMBER sy-msgno
*            WITH   sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
  ENDIF.
  DESCRIBE TABLE lt_result LINES sy-tfill.
  IF sy-tfill > 0.
    LOOP AT lt_result INTO ls_result.
      CASE ls_result-s_kind.
*       original system
        WHEN 'S'.
          cv_subrc = 4.   "no_master_system
*       alias
        WHEN 'A'.
          cv_subrc = 5.   "error in alias
          RETURN.
      ENDCASE.
    ENDLOOP.
  ENDIF.

  CHECK cv_subrc = 0 OR cv_subrc = 4.

  IF      cv_subrc = 4
  AND NOT ls_header-alias_name IS INITIAL.
*   alias should be created in no master system --> warning
    CONCATENATE 'Creating the alias in the non-original system'
                'could result in database errors Read Notes 1037771 and 1031500.'
                '-'
                'Do you want to create the alias here anyway?'
                INTO lv_text SEPARATED BY space.
*   alias should be created in correction system --> WARNING!!
    CALL FUNCTION 'POPUP_TO_CONFIRM'
      EXPORTING
        titlebar              = 'Create Alias in Non-Original System'
        text_question         = lv_text
        text_button_1         = 'Yes'
        text_button_2         = 'No'
        default_button        = '2'
        display_cancel_button = ' '
      IMPORTING
        answer                = lv_answer
      EXCEPTIONS
        OTHERS                = 0. "function does not rise any exceptions
    IF lv_answer = cl_answer_yes.
      gv_non_org_system = abap_true.
    ELSE.
      cv_subrc = 9.    "user cancelled
      RETURN.
    ENDIF.
  ENDIF.

  REFRESH lt_text_wa.
  LOOP AT lt_text_tab INTO ls_text_tab.
    MOVE-CORRESPONDING ls_text_tab TO ls_text_wa.
    ls_text_wa-concept = ls_header-concept.
    ls_text_wa-crea_name  = sy-uname.
    ls_text_wa-chan_name  = sy-uname.
    ls_text_wa-crea_tstut = lv_timestamp.
    ls_text_wa-chan_tstut = lv_timestamp.
    IF ls_text_wa-country   IS INITIAL AND
       ls_text_wa-extension IS INITIAL.
      ls_text_wa-flag_cntxt = 'X'.
    ELSE.
      CLEAR: ls_text_wa-flag_cntxt.
      PERFORM get_concept_id CHANGING lv_concept.
      ls_text_wa-object = lv_concept.
    ENDIF.

    APPEND ls_text_wa TO lt_text_wa.
  ENDLOOP.

  CLEAR: lv_flag_cancelled.
  CALL FUNCTION 'BTFR_CORR_CHECK'
    EXPORTING
      package            = ls_header-paket
      concept            = ls_header-concept
      flag_string        = lv_flag_string
    IMPORTING
      flag_cancelled     = lv_flag_cancelled
    EXCEPTIONS
      invalid_package    = 1
      permission_failure = 2
      OTHERS             = 3.
  IF sy-subrc = 0.
    IF lv_flag_cancelled = 'X'.
      cv_subrc = 9. RETURN.
    ENDIF.
  ELSE.
    cv_subrc = 6. RETURN.  "message e035.
  ENDIF.

*Include request
  CLEAR: lv_flag_cancelled.
  CALL FUNCTION 'BTFR_CORR_INSERT'
    EXPORTING
      package            = ls_header-paket
      concept            = ls_header-concept
      flag_string        = lv_flag_string
    IMPORTING
      flag_cancelled     = lv_flag_cancelled
    CHANGING
      corr_num           = gv_trkorr
    EXCEPTIONS
      invalid_package    = 1
      permission_failure = 2
      OTHERS             = 3.
  IF sy-subrc = 0.
    IF lv_flag_cancelled = 'X'.
      cv_subrc = 9. RETURN.
    ENDIF.
  ELSE.
    cv_subrc = 6. RETURN.  "message e035.
  ENDIF.

* insert concept
  CALL FUNCTION 'BTFR_INSERT'
    EXPORTING
      flag_string          = lv_flag_string
      header               = ls_header
      text_tab             = lt_text_wa
      string_tab           = lt_string_tab
      source_langu         = lv_source_langu
    EXCEPTIONS
      concept_not_inserted = 1
      invalid_parameters   = 2
      OTHERS               = 3.
  IF sy-subrc <> 0.
    cv_subrc = 7.    "error_in_update
    RETURN.
  ELSE.
    REFRESH lt_text_tab.
    LOOP AT lt_text_wa INTO ls_text_wa.
      CLEAR: ls_text_tab.
      MOVE-CORRESPONDING ls_text_wa TO ls_text_tab.
      APPEND ls_text_tab TO lt_text_tab.
    ENDLOOP.
  ENDIF.

  IF cv_subrc = 0 OR cv_subrc = 4.
    IF cv_subrc = 4.
*      MESSAGE I137.
    ENDIF.
*    MESSAGE S061.  "Text has been created
* Get request no.
    COMMIT WORK.
*    PERFORM get_request_no USING ls_header-concept
*                                 ls_header-paket.
  ENDIF.

ENDFORM.                    " CREATE_FIRST_OTR
*&---------------------------------------------------------------------*
*&      Form  GET_CONCEPT_ID
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      <--P_L_CONCEPT  text
*----------------------------------------------------------------------*
FORM get_concept_id  CHANGING pv_object TYPE sotr_conc.

  DATA: lv_uuid_x16 TYPE sysuuid_x16.

  TRY.
*   create uuid_x16
      lv_uuid_x16 = cl_system_uuid=>create_uuid_x16_static( ).
*   catch error
    CATCH cx_uuid_error.
      lv_uuid_x16 = 0.
  ENDTRY.

  pv_object = lv_uuid_x16.

ENDFORM.                    " GET_CONCEPT_ID
*&---------------------------------------------------------------------*
*&      Form  GET_REQUEST_NO
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      -->P_LS_HEADER_CONCEPT  text
*      -->P_LS_HEADER_PAKET  text
*----------------------------------------------------------------------*
FORM get_request_no  USING  pv_concept
                            pv_paket.

  DATA: lv_obj_name TYPE e071-obj_name.

  lv_obj_name(30) = pv_paket.
  lv_obj_name+30(32) = pv_concept.

  CLEAR: gv_trkorr.

  SELECT SINGLE a~strkorr
    INTO gv_trkorr
    FROM e070 AS a
   INNER JOIN e071 AS b
      ON a~trkorr = b~trkorr
   WHERE b~obj_name = lv_obj_name
     AND b~lockflag = abap_true.

ENDFORM.                    " GET_REQUEST_NO
*&---------------------------------------------------------------------*
*&      Form  CREATE_BDC_OTR
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM create_bdc_otr .

  PERFORM set_options.
  PERFORM create_bdc_data.

ENDFORM.                    " CREATE_BDC_OTR
*&---------------------------------------------------------------------*
*&      Form  GET_TEXT_CREA_LENGTH
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      -->P_LS_TEXT_TEXT  text
*      <--P_LV_LENGTH  text
*----------------------------------------------------------------------*
FORM get_text_crea_length  USING    pv_text
                                    pv_case
                           CHANGING pv_length.

  DATA: lv_add_length TYPE sotr_leng.

  pv_length = strlen( pv_text ).
  IF pv_length > 40.
    lv_add_length = pv_length / 10.
    pv_length = pv_length + lv_add_length.
    IF pv_length > 255.
      pv_length = 255.
    ENDIF.
  ELSE.
    pv_length = pv_length + 6.
  ENDIF.

ENDFORM.                    " GET_TEXT_CREA_LENGTH
*&---------------------------------------------------------------------*
*&      Form  GET_COMPARE_TEXT
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      -->P_LS_TEXT_TEXT  text
*      -->P_LV_LENGTH  text
*      <--P_LS_TEXT_LENGTH  text
*----------------------------------------------------------------------*
FORM get_compare_text  USING    pv_text
                       CHANGING cv_length_g
                                cv_length.
  "set_length

  DATA: lv_length     TYPE sotr_leng,
        lv_add_length TYPE sotr_leng.

  lv_length = strlen( pv_text ).
  IF lv_length > 20.
    lv_add_length = lv_length / 2.
    lv_length = lv_length + lv_add_length.
  ELSE.
    lv_length = lv_length + 10.
  ENDIF.

  IF cv_length_g > 255.
    cv_length_g = 255.
  ENDIF.

  IF cv_length_g >= strlen( pv_text ).
    cv_length = cv_length_g.

*      IF G_OBJTYPE ='WAPP'.
*        P_FLAG_DIFFERENT_LENGTH = TRUE.
*      ENDIF.

  ELSE.
    cv_length = lv_length.
  ENDIF.

  IF cv_length > 255.
    cv_length = cv_length_g = 255.
  ELSE.
    cv_length_g = cv_length.
  ENDIF.

ENDFORM.                    " GET_COMPARE_TEXT
*&---------------------------------------------------------------------*
*&      Form  UPDATE_OUTTAB2
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      -->P_LV_SUBRC  text
*      -->P_LV_MSGTX  text
*      -->P_LV_TABIX  text
*----------------------------------------------------------------------*
FORM update_outtab2  USING    pv_subrc
                              pv_msgtx
                              pv_tabix.

  IF pv_subrc = 0 OR pv_subrc = 1001.
    gt_outtab2-icon = '@5B@'.
  ELSE.
    gt_outtab2-icon = '@5C@'.
  ENDIF.

  gt_outtab2-message = pv_msgtx.

  MODIFY gt_outtab2 INDEX pv_tabix TRANSPORTING icon message.

ENDFORM.                    " UPDATE_OUTTAB2
*&---------------------------------------------------------------------*
*&      Form  REFRESH_DISPLAY2
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM refresh_display2 .

  CALL METHOD g_grid2->refresh_table_display
    EXCEPTIONS
      OTHERS = 1.

ENDFORM.                    " REFRESH_DISPLAY2
*&---------------------------------------------------------------------*
*&      Form  READONLY_DISPLAY2
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM readonly_display2 .

* ICON이 SPACE인 값이 있다는건 저장하지 않았다는 거다.
  READ TABLE gt_outtab2 WITH KEY icon = space.
  CHECK sy-subrc <> 0.

  READ TABLE gt_outtab2 WITH KEY icon = '@5C@'.
  IF sy-subrc <> 0.
*Set Non-editable cells to ready for input initially
    CALL METHOD g_grid2->set_ready_for_input
      EXPORTING
        i_ready_for_input = 0.
  ENDIF.

ENDFORM.                    " READONLY_DISPLAY2
*&---------------------------------------------------------------------*
*&      Form  MESSAGE_SUBRC
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      -->P_LV_SUBRC  text
*----------------------------------------------------------------------*
FORM message_subrc  USING    pv_subrc.

  CASE pv_subrc.
    WHEN 1.
      MESSAGE e100(sotr_mess).              "no entry found
    WHEN 2.
      MESSAGE e101(sotr_mess).              "concept_not_found
    WHEN 3.
      MESSAGE i305(sotr_mess).              "invalid object type
    WHEN 4.
      MESSAGE i137(sotr_mess).              "no originalsystem
    WHEN 5.
      MESSAGE e504(sotr_mess).              "invalid alias
    WHEN 6.
      MESSAGE e035(sotr_mess).              "error_in_correction.
    WHEN 7.
      MESSAGE e170(sotr_mess).              "error_in_update.
    WHEN 8.
      MESSAGE s500(sotr_mess) WITH 'KO'.    "no master langu
    WHEN 9.
      MESSAGE s102(sotr_mess).              "user_cancelled.
  ENDCASE.

ENDFORM.                    " MESSAGE_SUBRC
*&---------------------------------------------------------------------*
*&      Form  CHECK_CREATE_DATE
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      <--P_LV_ERR  text
*----------------------------------------------------------------------*
FORM check_create_date  CHANGING cv_err.

  DATA: BEGIN OF ls_alias,
          alias_name TYPE sotr_head-alias_name,
        END OF ls_alias.
  DATA: lt_alias LIKE TABLE OF ls_alias.
  DATA: lt_duptab LIKE TABLE OF gt_outtab2.
  DATA: lt_outtab2 LIKE TABLE OF gt_outtab2.
  DATA: ls_outtab2 LIKE LINE OF lt_outtab2.
  DATA: lv_tabix TYPE sy-tabix.
  DATA: lv_package(20).
  DATA: lv_strlen TYPE i.
  DATA: lv_cnt TYPE i.
  DATA: lv_flag_string TYPE btfr_f_string.
  DATA: lt_result TYPE btfr_check_result_tt.
  DATA: ls_result TYPE btfr_check_result.
  DATA: ls_header TYPE btfr_head.
  DATA: ls_check TYPE btfr_check.
  DATA: lv_srcsystem TYPE srcsystem.

  CLEAR: cv_err.

*1. ALIAS_NAME이 'PACKAGE/' 로 시작하지 않으면 에러
  CONCATENATE gv_paket '/' INTO lv_package.
  lv_strlen = strlen( lv_package ).

*2. 생성 리스트에 중복된 ALIAS_NAME이 있는지 체크
  lt_duptab[] = gt_outtab2[].
  SORT lt_duptab BY alias_name.

*3. Object Type이 입력되었는지 체크
*4. 유효한 objtect type인지 체크
*5. Alias 체크
*6. 이미 생성된 OTR인지 체크
  lt_outtab2[] = gt_outtab2[].
  SORT lt_outtab2 BY alias_name.
  DELETE ADJACENT DUPLICATES FROM lt_outtab2 COMPARING alias_name.
  IF lt_outtab2[] IS NOT INITIAL.
    SELECT alias_name
      INTO CORRESPONDING FIELDS OF TABLE lt_alias
      FROM sotr_head
       FOR ALL ENTRIES IN lt_outtab2
     WHERE alias_name = lt_outtab2-alias_name.
    IF sy-subrc = 0.
      SORT lt_alias BY alias_name.
    ENDIF.
  ENDIF.
*7. Korean은 필수 필드

*----------------------------------
  LOOP AT gt_outtab2.
    lv_tabix = sy-tabix.

*1. ALIAS_NAME이 'PACKAGE/' 로 시작하지 않으면 에러
    IF gt_outtab2-alias_name(lv_strlen) <> lv_package .
      gt_outtab2-icon = '@5C@'.
      gt_outtab2-message = 'Please check alias.(start with package/)'.
      MODIFY gt_outtab2 INDEX lv_tabix TRANSPORTING icon message.
      CONTINUE.
    ENDIF.

*2. 생성 리스트에 중복된 ALIAS_NAME이 있는지 체크
    CLEAR: lv_cnt.
    READ TABLE lt_duptab INTO ls_outtab2
      WITH KEY alias_name = gt_outtab2-alias_name BINARY SEARCH.
    IF sy-subrc = 0.
      LOOP AT lt_duptab INTO ls_outtab2 FROM sy-tabix.
        IF ls_outtab2-alias_name = gt_outtab2-alias_name.
          lv_cnt = lv_cnt + 1.
        ENDIF.
      ENDLOOP.
    ENDIF.

    IF lv_cnt > 1.
      gt_outtab2-icon    = '@5C@'.
      gt_outtab2-message = 'duplicated alias.'.
      MODIFY gt_outtab2 INDEX lv_tabix TRANSPORTING icon message.
      CONTINUE.
    ENDIF.

*3. Object Type이 입력되었는지 체크
    IF gt_outtab2-objtype IS INITIAL.
      gt_outtab2-icon    = '@5C@'.
      gt_outtab2-message = 'Enter an object type and a name.'.
      MODIFY gt_outtab2 INDEX lv_tabix TRANSPORTING icon message.
      CONTINUE.
    ENDIF.

*4. 유효한 objtect type인지 체크
    CLEAR: ls_header.
    IF NOT gt_outtab2-objtype IS INITIAL.
      CALL FUNCTION 'SOTR_OBJECT_SET_VECTOR'
        EXPORTING
          object           = gt_outtab2-objtype
        CHANGING
          object_vector    = ls_header-objid_vec
        EXCEPTIONS
          object_not_found = 1
          OTHERS           = 2.
      IF sy-subrc <> 0.
        gt_outtab2-icon    = '@5C@'.
        gt_outtab2-message = 'Enter a permitted object type.'.  "s305(SOTR_MESS)
        MODIFY gt_outtab2 INDEX lv_tabix TRANSPORTING icon message.
        CONTINUE.
      ENDIF.
    ENDIF.

*5. Alias 체크
    ls_check-alias_name = 'X'.
    ls_header-paket = gt_outtab2-paket.
    ls_header-crea_lan = 'E'.
    ls_header-alias_name = gt_outtab2-alias_name.

    CALL FUNCTION 'BTFR_CHECK'
      EXPORTING
        langu           = sy-langu
        alias           = ls_header-alias_name
        check           = ls_check
        flag_string     = lv_flag_string
      IMPORTING
        check_result    = lt_result
      CHANGING
        btfr_head       = ls_header
      EXCEPTIONS
        invalid_package = 1
        OTHERS          = 2.
    IF sy-subrc = 0.
      DESCRIBE TABLE lt_result LINES sy-tabix.
      IF sy-tabix > 0.
        READ TABLE lt_result INTO ls_result INDEX 1.
        gt_outtab2-icon = '@5C@'.
        gt_outtab2-message = ls_result-text.
        MODIFY gt_outtab2 INDEX lv_tabix TRANSPORTING icon message.
        CONTINUE.

      ENDIF.
    ENDIF.

*6. 이미 생성된 OTR인지 체크
    IF lt_alias[] IS NOT INITIAL.
      READ TABLE lt_alias INTO ls_alias
        WITH KEY alias_name = gt_outtab2-alias_name BINARY SEARCH.
      IF sy-subrc = 0.
        gt_outtab2-icon    = '@5C@'. " ICON_LED_RED
        gt_outtab2-message = 'Alias name already exists.'.
        MODIFY gt_outtab2 INDEX lv_tabix TRANSPORTING icon message.
        CONTINUE.
      ENDIF.
    ENDIF.

*7. English는 필수 필드
    IF gt_outtab2-en_text IS INITIAL.
      gt_outtab2-icon    = '@5C@'.
      gt_outtab2-message = 'English Text field is required.'.
      MODIFY gt_outtab2 INDEX lv_tabix TRANSPORTING icon message.
      CONTINUE.
    ENDIF.

*" Korean 없으면 English로 채워준다.
    IF gt_outtab2-ko_text IS INITIAL.
      gt_outtab2-ko_text = gt_outtab2-en_text.
      MODIFY gt_outtab2 INDEX lv_tabix TRANSPORTING ko_text.
    ENDIF.
*" Chinese 없으면 English로 채워준다.
    IF gt_outtab2-zh_text IS INITIAL.
      gt_outtab2-zh_text = gt_outtab2-en_text.
      MODIFY gt_outtab2 INDEX lv_tabix TRANSPORTING zh_text.
    ENDIF.
*" Chinese 없으면 English로 채워준다.
    IF gt_outtab2-zf_text IS INITIAL.
      gt_outtab2-zf_text = gt_outtab2-en_text.
      MODIFY gt_outtab2 INDEX lv_tabix TRANSPORTING zf_text.
    ENDIF.

* " 정상건은 MESSAGE CLEAR
    CLEAR: gt_outtab2-icon, gt_outtab2-message.
    MODIFY gt_outtab2 INDEX lv_tabix TRANSPORTING icon message.
  ENDLOOP.

  " 에러체크
  READ TABLE gt_outtab2 WITH KEY icon = '@5C@'.
  IF sy-subrc = 0.
    cv_err = abap_true.
  ENDIF.

ENDFORM.                    " CHECK_CREATE_DATE
*&---------------------------------------------------------------------*
*&      Form  ALV_SORT1
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM alv_sort1 .

  DATA: ls_sort TYPE lvc_s_sort.

  REFRESH gt_sort1.

  ls_sort-spos = '01'.
  ls_sort-fieldname = 'ALIAS_NAME'.
  ls_sort-down = 'X'.
  APPEND ls_sort TO gt_sort1.

  ls_sort-spos = '02'.
  ls_sort-fieldname = 'CONCEPT'.
  ls_sort-down = 'X'.
  APPEND ls_sort TO gt_sort1.

  ls_sort-spos = '03'.
  ls_sort-fieldname = 'LANGU'.
  ls_sort-up = 'X'.
  APPEND ls_sort TO gt_sort1.

ENDFORM.                    " ALV_SORT1
*&---------------------------------------------------------------------*
*&      Form  CHECK_EXIST_PAKAGE
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      -->P_GV_PAKET  text
*      <--P_LV_SUBRC  text
*----------------------------------------------------------------------*
FORM check_exist_pakage  USING    pv_paket
                         CHANGING cv_subrc.

*  DATA: lv_srcsystem TYPE tadir-srcsystem.
*
*  IF pv_paket(1) <> '$' AND pv_paket(1) <> 'T'.
*    SELECT SINGLE srcsystem
*      INTO lv_srcsystem
*      FROM tadir
*     WHERE pgmid = 'R3TR'
*       AND object = 'DEVC'
*       AND obj_name = pv_paket.
*
*    cv_subrc = sy-subrc.
*  ENDIF.

  DATA: lv_devclass TYPE devclass.
  SELECT SINGLE devclass
    INTO lv_devclass
    FROM tdevc
    WHERE devclass = pv_paket.

  cv_subrc = sy-subrc.

ENDFORM.                    " CHECK_EXIST_PAKAGE
*&---------------------------------------------------------------------*
*&      Form  DOWNLOAD_TEMPLATE
*&---------------------------------------------------------------------*
*       text : OTR 생성기준 폼 다운로드
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM download_template .

  CONSTANTS : lc_name        TYPE char30 VALUE 'ZKR_OTR'.

  DATA : lv_object_name TYPE char30 .

  lv_object_name = lc_name.
  PERFORM export_form     USING sy-dynnr
                                lv_object_name.


ENDFORM.                    " DOWNLOAD_TEMPLATE
*&---------------------------------------------------------------------*
*&      Form  EXCEL_UPLOAD
*&---------------------------------------------------------------------*
*       text : OTR 생성용 자료 EXCEL 업로드
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM excel_upload .

  DATA : lv_title    TYPE text70,
         lv_question TYPE text70,
         lv_answer   TYPE char1,
         lv_subrc    TYPE sysubrc.

*--------------------------------------------------------------------*

  " 1. 화면 출력자료 삭제 경고
  "   Excel Upload
  lv_title = TEXT-016.
  "    출력자료가 삭제됩니다. 진행하시겠습니까?
  MESSAGE s001(00) WITH 'screen input data will be deleted. continue?' INTO lv_question.
  PERFORM check_confirm USING  lv_title
                               lv_question
                               lv_answer.
  CHECK lv_answer EQ 1.
  CLEAR : gt_outtab2, gt_outtab2[].

  " 2. 엑셀 업로드 처리
  PERFORM excel_data_upload USING lv_subrc.

  " 3. 업로드 자료 화면 출력
  PERFORM refresh_display2.


ENDFORM.                    " EXCEL_UPLOAD
*&---------------------------------------------------------------------*
*&      Form  EXPORT_FORM
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      -->P_SY_DYNNR  text
*      -->P_LV_OBJECT_NAME  text
*----------------------------------------------------------------------*
FORM export_form  USING    p_dynnr
                           pv_object_name.

  CONSTANTS : lc_text        TYPE text30 VALUE 'OTR_TEXT',
              lc_root        TYPE text30 VALUE 'C:\temp\',
              lc_extension   TYPE text30 VALUE '.xls',
              lc_under_score TYPE char1  VALUE '_'.

  DATA : lv_file_name(80) TYPE c,
         lv_file_addr     LIKE rlgrap-filename.

*--------------------------------------------------------------------*

  " 파일저장경로 설정 - OTR_TEMPLATE + 일자 + 시간
  CONCATENATE gv_paket lc_text sy-datum sy-uzeit INTO lv_file_name
    SEPARATED BY lc_under_score.
  " C:\temp\ + File name + .xls
  CONCATENATE lc_root lv_file_name lc_extension
         INTO lv_file_addr.

  PERFORM close_excel_doc  USING lv_file_addr.

  " OBJECT FREE
  PERFORM free_object.
  PERFORM open_excel_doc   USING pv_object_name
                                 lv_file_addr.

  " visible
  SET PROPERTY OF go_excel 'Visible'     = 1.
  GET PROPERTY OF go_excel 'ACTIVESHEET' = go_sheet.

  " File Open 정보
  MESSAGE i001(00) WITH lv_file_addr 'file dowdloaded.'.


ENDFORM.                    " EXPORT_FORM
*&---------------------------------------------------------------------*
*&      Form  CLOSE_EXCEL_DOC
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      -->P_LV_FILE_ADDR  text
*----------------------------------------------------------------------*
FORM close_excel_doc  USING    pv_file_addr.

  CALL FUNCTION 'WS_FILE_DELETE'
    EXPORTING
      file = pv_file_addr.


ENDFORM.                    " CLOSE_EXCEL_DOC
*&---------------------------------------------------------------------*
*&      Form  FREE_OBJECT
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM free_object .

  FREE : go_excel ,
         go_mapl  ,
         go_map   ,
         go_sheets,
         go_sheet ,
         go_zl    ,
         go_zl2   ,
         go_f     ,
         go_zrl   .


ENDFORM.                    " FREE_OBJECT
*&---------------------------------------------------------------------*
*&      Form  OPEN_EXCEL_DOC
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      -->P_LV_FILE_NAME  text
*      -->P_LV_FILE_ADDR  text
*----------------------------------------------------------------------*
FORM open_excel_doc  USING pv_object_name
                           pv_file_addr.

  DATA: lt_doc_table      LIKE w3mime OCCURS 0,
        lv_doc_size       TYPE i,
        lv_doc_type(80)   VALUE soi_doctype_excel_sheet,
        lv_doc_format(80) TYPE c,
        lv_err            TYPE c,
        lv_filename       TYPE string.

*--------------------------------------------------------------------*

  lv_filename = pv_file_addr.

  CALL FUNCTION 'SAP_OI_LOAD_MIME_DATA'
    EXPORTING
      object_id        = pv_object_name
    IMPORTING
      data_size        = lv_doc_size
      document_format  = lv_doc_format
      document_type    = lv_doc_type
    TABLES
      data_table       = lt_doc_table
    EXCEPTIONS
      object_not_found = 1
      internal_error   = 2
      OTHERS           = 3.

  CHECK sy-subrc EQ 0.

  CALL FUNCTION 'GUI_DOWNLOAD'
    EXPORTING
      bin_filesize = lv_doc_size
      filename     = lv_filename
      filetype     = 'BIN'
    IMPORTING
      filelength   = gv_file_length
    TABLES
      data_tab     = lt_doc_table.
  IF sy-subrc <> 0.
    MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
            WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
  ENDIF.

  IF go_excel-header = space OR go_excel-handle = -1.
    CREATE OBJECT go_excel 'Excel.Application'.
    PERFORM err_hdl USING lv_err.
    CHECK lv_err IS INITIAL.
  ENDIF.

  CALL METHOD OF
    go_excel
      'Workbooks' = go_mapl.
  PERFORM err_hdl USING lv_err.
  CHECK lv_err IS INITIAL.

  CALL METHOD OF
      go_mapl
      'OPEN'  = go_map
    EXPORTING
      #1      = pv_file_addr.


ENDFORM.                    " OPEN_EXCEL_DOC
*&---------------------------------------------------------------------*
*&      Form  ERR_HDL
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*  -->  p1        text
*  <--  p2        text
*----------------------------------------------------------------------*
FORM err_hdl USING pv_err .

  IF sy-subrc <> 0.
    " &1 작업중 오류가 발생했습니다.
    MESSAGE s001(00) WITH 'error occurs.' DISPLAY LIKE 'E'.
    pv_err = abap_true.
*    WRITE: / 'Error Occurs : ', sy-subrc.
*    REJECT.
  ENDIF.

ENDFORM.                    " ERR_HDL
*&---------------------------------------------------------------------*
*&      Form  CHECK_CONFIRM
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      -->P_LV_ANSWER  text
*----------------------------------------------------------------------*
FORM check_confirm  USING  pv_title
                           pv_question
                           pv_answer.

*----------------------------------------------------------------------*

  " 작업진행
  CALL FUNCTION 'POPUP_TO_CONFIRM'
    EXPORTING
      titlebar              = pv_title
      text_question         = pv_question
      text_button_1         = 'Yes'
      text_button_2         = 'No'
      default_button        = '2'
      display_cancel_button = ' '
    IMPORTING
      answer                = pv_answer
    EXCEPTIONS
      OTHERS                = 0. "function does not rise any exceptions


ENDFORM.                    " CHECK_CONFIRM
*&---------------------------------------------------------------------*
*&      Form  EXCEL_DATA_UPLOAD
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      -->P_LV_SUBRC  text
*----------------------------------------------------------------------*
FORM excel_data_upload  USING    p_lv_subrc.

  DATA : lv_file   TYPE filename,  " FC03TAB-PL00_FILE.
         lv_object TYPE char30.

*--------------------------------------------------------------------*

  " File Open Dialog
  PERFORM file_open_dialog      CHANGING lv_file.

  " File Open
  CHECK lv_file IS NOT INITIAL.
  PERFORM excel_upload_process  USING    lv_file
                                         lv_object.


ENDFORM.                    " EXCEL_DATA_UPLOAD
*&---------------------------------------------------------------------*
*&      Form  FILE_OPEN_DIALOG
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      <--P_LV_FILE  text
*----------------------------------------------------------------------*
FORM file_open_dialog  CHANGING pv_file.

  " CALL METHOD CL_GUI_FRONTEND_SERVICES=>FILE_OPEN_DIALOG.
  DATA: lt_filenametable    TYPE filetable,
        lv_rc               TYPE i,
        lv_default_filename TYPE string,
        lv_fullpath_used    TYPE string,
        lv_directory        TYPE string,
        lv_fieldname        TYPE string.

  FIELD-SYMBOLS: <filename_wa>   TYPE file_table.

  MOVE : 'C:\TEMP' TO lv_default_filename.


  cl_gui_frontend_services=>get_temp_directory( CHANGING temp_dir = lv_directory ).

  CALL METHOD cl_gui_frontend_services=>file_open_dialog
    EXPORTING
*     WINDOW_TITLE            =
*     DEFAULT_EXTENSION       =
      default_filename        = lv_default_filename
*     FILE_FILTER             =
*     WITH_ENCODING           =
      initial_directory       = lv_directory
*     MULTISELECTION          =
    CHANGING
      file_table              = lt_filenametable
      rc                      = lv_rc
*     USER_ACTION             =
*     FILE_ENCODING           =
    EXCEPTIONS
      file_open_dialog_failed = 1
      cntl_error              = 2
      error_no_gui            = 3
      not_supported_by_gui    = 4
      OTHERS                  = 5.

  IF sy-subrc EQ 0.
    READ TABLE lt_filenametable INDEX 1 ASSIGNING <filename_wa>.
    IF sy-subrc IS INITIAL AND
       <filename_wa> IS NOT INITIAL.
      MOVE : <filename_wa>    TO lv_fullpath_used,
             <filename_wa>    TO pv_file.
    ELSE.
*      MESSAGE E205 RAISING FILE_OPEN_DIALOG_ERROR.
    ENDIF.

  ELSE.

*    MESSAGE ID     SY-MSGID
*            TYPE   SY-MSGTY
*            NUMBER SY-MSGNO
*            WITH   SY-MSGV1 SY-MSGV2 SY-MSGV3 SY-MSGV4.

  ENDIF.


  DATA : lv_return TYPE abap_bool.
  lv_fieldname = pv_file.
  " 파일확인
  CALL METHOD cl_gui_frontend_services=>file_exist
    EXPORTING
      file                 = lv_fieldname
    RECEIVING
      result               = lv_return
    EXCEPTIONS
      cntl_error           = 1
      error_no_gui         = 2
      wrong_parameter      = 3
      not_supported_by_gui = 4
      OTHERS               = 5.

  IF lv_return IS INITIAL OR sy-subrc NE 0.
    " 파일경로를 확인하시기 바랍니다.
    MESSAGE i001(00)  WITH 'Please check file path.' DISPLAY LIKE 'E'.
    CLEAR   pv_file.
    EXIT.
  ENDIF.


ENDFORM.                    " FILE_OPEN_DIALOG
*&---------------------------------------------------------------------*
*&      Form  EXCEL_UPLOAD_PROCESS
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      -->P_LV_FILE  text
*      -->P_PV_OBJECT  text
*----------------------------------------------------------------------*
FORM excel_upload_process  USING    pv_file
                                    pv_object.

  DATA : lv_index  TYPE sy-tabix,
         lt_upload LIKE TABLE OF gs_excel_up,
         lt_updata LIKE TABLE OF gs_excel_up,
         ls_updata LIKE          gs_excel_up,
         lt_error  LIKE TABLE OF gs_excel_up.

  DATA : ls_outtab  LIKE LINE OF gt_outtab2,
         lv_message TYPE         text70.

*--------------------------------------------------------------------*

  REFRESH : gt_intern.

  CLEAR : gt_intern,
          gv_stripped  ,
          gv_file_path ,
          gv_extension ,
          gv_split_name,
          gv_filename  ,
          gv_flag      ,
          lv_index.

  " File 명과 경로 분리
  PERFORM split_file_name USING    pv_file
                          CHANGING gv_filename
                                   gv_stripped
                                   gv_file_path.
  " 확장자 Check
  PERFORM file_type_check USING    gv_filename
                          CHANGING gv_split_name
                                   gv_extension
                                   gv_flag.
  CASE pv_object.
    WHEN space.
      " Itab
      CHECK gv_flag IS INITIAL.
      PERFORM excel_move_itab TABLES   gt_intern
                              USING    gv_filename
                                       1
                                       2
                                       13
                                       50000
                              CHANGING gv_flag.

      " Excel Upload Itab.
      CHECK gv_flag IS INITIAL.
      PERFORM move_row_col_itab TABLES   gt_intern
                                         lt_updata
                                CHANGING lv_index
                                         gv_flag.

      IF lt_updata[] IS INITIAL.
        EXIT.
      ELSE.
        "
        " 출력 데이터 구성
        CLEAR : gt_outtab2, gt_outtab2[].
        LOOP AT lt_updata INTO ls_updata.
          CLEAR : ls_outtab, lv_message.
          " 패키지 정보 설정 : PAKET
          ls_outtab-paket = gv_paket.
          " alias 입력 체크
          IF ls_updata-alias_name IS INITIAL.
            ls_outtab-icon    = icon_led_red.
            " alias field is required.
            MESSAGE s001(00) WITH 'alias field is required'.
            ls_outtab-message = 'alias field is required.'.
          ELSE.
            CONCATENATE gv_paket co_hypen ls_updata-alias_name
                   INTO ls_outtab-alias_name.
          ENDIF.
          " Object Type : OBJTYPE
          ls_outtab-objtype = co_wdyv.
          " EN 텍스트 입력확인
          IF ls_updata-en_text IS INITIAL.
            ls_outtab-icon    = icon_led_red.
            " alias field is required.
            IF ls_outtab-message IS NOT INITIAL.
              lv_message = 'English Text field is required.'.
              CONCATENATE ls_outtab-message lv_message INTO ls_outtab-message
                SEPARATED BY space.
            ELSE.
              MESSAGE s001(00) WITH 'English Text field is required.'.
              ls_outtab-message = 'English Text field is required.'.
            ENDIF.

          ELSE.
            " English : EN_TEXT
            ls_outtab-en_text = ls_updata-en_text.
          ENDIF.
          " Korean : KO_TEXT
          IF ls_updata-ko_text IS INITIAL.
            ls_outtab-ko_text = ls_updata-en_text.
          ELSE.
            ls_outtab-ko_text = ls_updata-ko_text.
          ENDIF.
          " Chineses : ZN_TEXT
          IF ls_updata-zh_text IS INITIAL.
            ls_outtab-zh_text = ls_updata-en_text.
          ELSE.
            ls_outtab-zh_text = ls_updata-zh_text.
          ENDIF.
          " Chineses : ZF_TEXT
          IF ls_updata-zf_text IS INITIAL.
            ls_outtab-zf_text = ls_updata-en_text.
          ELSE.
            ls_outtab-zf_text = ls_updata-zf_text.
          ENDIF.

          " 출력자료 생성
          APPEND ls_outtab TO gt_outtab2.
        ENDLOOP. " LOOP AT lt_updata INTO ls_updata.

        " 업로드 건수 출력 : lv_index - &1 record have been uploaded.
        lv_index = lines( gt_outtab2 ).
        MESSAGE s001(00) WITH lv_index 'record have been uploaded'.

      ENDIF.

*      "Error Check & Error ouput tab Setting
*      PERFORM move_error_disp_itab TABLES   lt_updata
*                                            lt_error
*                                            lt_upload
*                                   CHANGING gv_flag.
*
*      IF LT_ERROR IS INITIAL.
*        "Error Data 가 없으면 Screen 0100 호출
*
*        "  Result Display
*        PERFORM SET_DISP_UPLOAD      TABLES   LT_ERROR
*                                              LT_UPLOAD
*                                              GT_DISP.
*
*      ELSE."Error Data 존재시
*
*        "Error 용 popup 호출
*        " 에러 내역 출력
*        PERFORM SHOW_ERROR TABLES LT_ERROR .
*
*      ENDIF.

    WHEN OTHERS.

  ENDCASE. " CASE pv_object.

  REFRESH : gt_intern.

  CLEAR : gt_intern    ,
          gv_stripped  ,
          gv_file_path ,
          gv_extension ,
          gv_split_name,
          gv_filename  ,
          gv_flag      .


ENDFORM.                    " EXCEL_UPLOAD_PROCESS
*&---------------------------------------------------------
*&---------------------------------------------------------------------*
*&      Form  SPLIT_FILE_NAME
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
FORM split_file_name USING    pv_file
                     CHANGING pv_filename
                              pv_stripped
                              pv_file_path.

  CLEAR: pv_stripped,
         pv_file_path,
         pv_filename.

  pv_filename = pv_file.

  CALL FUNCTION 'TRINT_SPLIT_FILE_AND_PATH'
    EXPORTING
      full_name     = pv_filename
    IMPORTING
      stripped_name = pv_stripped
      file_path     = pv_file_path.

  IF pv_file_path IS INITIAL.
    CONCATENATE 'C:\' pv_filename INTO pv_filename.
  ENDIF.

ENDFORM.                    " SPLIT_FILE_NAME
*&---------------------------------------------------------------------*
*&      Form  FILE_TYPE_CHECK
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
FORM file_type_check  USING    pv_filename
                      CHANGING pv_split_name
                               pv_extension
                               pv_flag.

  CLEAR pv_extension.

  CALL FUNCTION 'CRM_IC_WZ_SPLIT_FILE_EXTENSION'
    EXPORTING
      iv_filename_with_ext = pv_filename
    IMPORTING
      ev_filename          = pv_split_name
      ev_extension         = pv_extension.


  TRANSLATE pv_extension TO UPPER CASE.

  IF pv_extension NE 'XLS' AND
     pv_extension NE 'XLSX'.

    MESSAGE i001(00) WITH 'File Not In Excel Format'(e15)
                 DISPLAY LIKE 'e'.
    pv_flag = 'X'.
  ELSE.

  ENDIF.

ENDFORM.                    " FILE_TYPE_CHECK
*&---------------------------------------------------------------------*
*&      Form  EXCEL_MOVE_ITAB
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
FORM excel_move_itab  TABLES pt_intern STRUCTURE gt_intern
                      USING    pv_filename
                               VALUE(p_st_col)
                               VALUE(p_st_row)
                               VALUE(p_end_col)
                               VALUE(p_end_row)
                      CHANGING pv_flag.

  REFRESH: pt_intern.
  CALL FUNCTION 'KCD_EXCEL_OLE_TO_INT_CONVERT'
    EXPORTING
      filename                = pv_filename
      i_begin_col             = p_st_col
      i_begin_row             = p_st_row
      i_end_col               = p_end_col
      i_end_row               = p_end_row
    TABLES
      intern                  = pt_intern
    EXCEPTIONS
      inconsistent_parameters = 201
      upload_ole              = 201.

  IF pt_intern[] IS INITIAL.
    MESSAGE i001(00)   WITH 'No Data In Excel File'(e16)
          DISPLAY LIKE 'E'.
    pv_flag = 'X'.
  ENDIF.

ENDFORM.                    " EXCEL_MOVE_ITAB
*&---------------------------------------------------------------------*
*&      Form  move_row_col_itab
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
*      -->PT_INTERN  text
*      -->PT_UPDATA  text
*      -->PV_INDEX   text
*      -->PV_FLAG    text
*----------------------------------------------------------------------*
FORM move_row_col_itab  TABLES   pt_intern STRUCTURE gt_intern
                                 pt_updata STRUCTURE gs_excel_up
                        CHANGING pv_index
                                 pv_flag.

  DATA : ls_struct   TYPE REF TO data,
         lv_index    TYPE        sy-tabix,
         ls_struct_1 TYPE REF TO data,
         lv_index_1  TYPE        sy-tabix.

  FIELD-SYMBOLS : <istruct> TYPE any,
                  <lfs>.

*--------------------------------------------------------------------*

  CLEAR pv_index.

  CREATE DATA ls_struct   LIKE LINE OF pt_updata.
  ASSIGN ls_struct->* TO <istruct>.

  SORT  pt_intern BY row
                     col.

  CLEAR   ls_struct.
  REFRESH pt_updata.

  LOOP AT pt_intern.
    " 셀포지션 정보
    MOVE pt_intern-col TO pv_index.

*    " 필드 설정 필요시
    lv_index_1 = pv_index.

    " 스트럭쳐 정보
    ASSIGN COMPONENT lv_index_1 OF STRUCTURE <istruct> TO <lfs>.

    " 필드별 작업
*    CASE pv_index.
*      WHEN 1."Version
*        ranges_set_low : gr_up_versi 'I' 'EQ' pt_intern-value.
*      WHEN 2."Fiscal Year
*      WHEN 3."Period
*      WHEN 4." Material
*        TRANSLATE pt_intern-value TO UPPER CASE.
*        "Materail Number Conversion
*        PERFORM conv_matn1       CHANGING pt_intern-value.
*        ranges_set_low : gr_up_matnr 'I' 'EQ' pt_intern-value.
*      WHEN 5.
*
*      WHEN 6.
*
*      WHEN 7.
*      WHEN 8.
*      WHEN 9.
*      WHEN 10.
*      WHEN 11.
*      WHEN 12.
*      WHEN 13.
*
*      WHEN OTHERS.
*    ENDCASE.
    IF pv_index EQ 1.
      TRANSLATE pt_intern-value  TO UPPER CASE .
    ENDIF.

    MOVE pt_intern-value TO <lfs>.

    " 최종 셀 레코드 생성
    AT END OF row.
      APPEND <istruct>   TO pt_updata.
      CLEAR  <istruct>.
      " 업로드 레코드 건수 설정
      ADD 1 TO pv_index.
    ENDAT.

  ENDLOOP. " LOOP AT pt_intern.


ENDFORM.                    " MOVE_ROW_COL_ITAB