class ZCL_EUI_SCREEN definition
  public
  inheriting from ZCL_EUI_MANAGER
  final
  create public .

public section.
  type-pools SSCR .
  type-pools SYDB0 .
  class ZCL_EUI_TYPE DEFINITION LOAD. "Required in ABAP 7.01
  types:
    TT_SCREEN type STANDARD TABLE OF SCREEN WITH DEFAULT KEY .
  types:
    BEGIN OF ts_map.
    INCLUDE TYPE zcl_eui_type=>ts_field_desc AS field_desc.
  types:
    input       TYPE char1,
    required    TYPE char1,
    cur_value   TYPE REF TO DATA,
    par_name    TYPE string,
    is_list_box TYPE abap_bool,
   END OF ts_map .
  types:
    tt_map TYPE STANDARD TABLE OF ts_map WITH DEFAULT KEY .

  constants:
    BEGIN OF MC_DYNNR,
     FREE_SEL  type SYDYNNR VALUE 'FREE',
     AUTO_GEN  type SYDYNNR VALUE 'AUTO',
     DYN_POPUP type SYDYNNR VALUE 'DPOP',
   END OF MC_DYNNR .

  methods CONSTRUCTOR
    importing
      !IV_DYNNR type SYDYNNR
      !IV_CPROG type SYCPROG default SY-CPROG
      !IR_CONTEXT type ref to DATA optional
      !IV_READ_ONLY type ABAP_BOOL optional
    raising
      ZCX_EUI_EXCEPTION .
  methods CUSTOMIZE
    importing
      !NAME type CSEQUENCE optional
      !GROUP1 type CHAR3 optional
      !REQUIRED type CHAR1 optional
      !INPUT type CHAR1 optional
      !OUTPUT type CHAR1 optional
      !INVISIBLE type CHAR1 optional
      !ACTIVE type CHAR1 optional
      !IV_FIELDNAME type ZCL_EUI_TYPE=>TS_FIELD_DESC-NAME optional
      !IV_LABEL type ZCL_EUI_TYPE=>TS_FIELD_DESC-LABEL optional
      !IV_SUB_FDESC type ZCL_EUI_TYPE=>TS_FIELD_DESC-SUB_FDESC optional .
  methods GET_CONTEXT
    importing
      !IV_READ type ABAP_BOOL default ABAP_TRUE
    returning
      value(RR_CONTEXT) type ref to DATA .
  class-methods EDIT_IN_POPUP
    importing
      !IV_TITLE type CSEQUENCE default 'Edit value'
      !IV_LABEL type CSEQUENCE optional
      !IV_REQUIRED type ABAP_BOOL optional
    changing
      !CV_OK type ABAP_BOOL optional
      !CV_VALUE type ANY .
  class-methods CONFIRM
    importing
      !IV_TITLE type CSEQUENCE
      !IV_QUESTION type CSEQUENCE
      !IV_ICON_1 type ICON-NAME default 'ICON_OKAY'
      !IV_TEXT_1 type CSEQUENCE optional
      !IV_ICON_2 type ICON-NAME default 'ICON_CANCEL'
      !IV_TEXT_2 type CSEQUENCE optional
      !IV_DEFAULT type CHAR1 default '2'
      !IV_DISPLAY_CANCEL type ABAP_BOOL optional
    returning
      value(RV_OK) type ABAP_BOOL .
  class-methods SHOW_RANGE
    importing
      !IS_FIELD_DESC type ZCL_EUI_TYPE=>TS_FIELD_DESC
      !IR_CUR_VALUE type ref to DATA
      !IV_READ_ONLY type ABAP_BOOL
    returning
      value(RV_UPDATE) type ABAP_BOOL .

  methods ZIF_EUI_MANAGER~PAI
    redefinition .
  methods ZIF_EUI_MANAGER~PBO
    redefinition .
  methods ZIF_EUI_MANAGER~SHOW
    redefinition .
protected section.
private section.

  data MO_HELPER type ref to LCL_SCREEN .
ENDCLASS.



CLASS ZCL_EUI_SCREEN IMPLEMENTATION.


METHOD confirm.
  DATA lt_param  TYPE abap_func_parmbind_tab.
  DATA ls_param  TYPE abap_func_parmbind.
  DATA lt_exc    TYPE abap_func_excpbind_tab.
  DATA ls_exc    TYPE abap_func_excpbind.
  DATA lv_answer TYPE char1.

  DEFINE add_param.
    GET REFERENCE OF &1 INTO ls_param-value.
    ls_param-name = &2.
    ls_param-kind = &3.
    INSERT ls_param INTO TABLE lt_param.
  END-OF-DEFINITION.

  " Parameters
  add_param iv_title           'TITLEBAR'               abap_func_exporting.
  add_param iv_question        'TEXT_QUESTION'          abap_func_exporting.
  add_param iv_icon_1          'ICON_BUTTON_1'          abap_func_exporting.
  add_param iv_icon_2          'ICON_BUTTON_2'          abap_func_exporting.
  add_param iv_default         'DEFAULT_BUTTON'         abap_func_exporting.
  add_param iv_display_cancel  'DISPLAY_CANCEL_BUTTON'  abap_func_exporting.
  add_param lv_answer          'ANSWER'                 abap_func_importing.

  " Yes
  IF iv_text_1 IS SUPPLIED.
    add_param iv_text_1        'TEXT_BUTTON_1'          abap_func_exporting.
  ENDIF.

  " No
  IF iv_text_2 IS SUPPLIED.
    add_param iv_text_2        'TEXT_BUTTON_2'          abap_func_exporting.
  ENDIF.

  " Exceptions
  ls_exc-name  = 'OTHERS'.
  ls_exc-value = 1.
  INSERT ls_exc INTO TABLE lt_exc.

  CALL FUNCTION 'POPUP_TO_CONFIRM'
    PARAMETER-TABLE lt_param
    EXCEPTION-TABLE lt_exc.
  CHECK sy-subrc = 0. " No ?

  CASE lv_answer.
    WHEN '0'. " No
      rv_ok = abap_false.

    WHEN '1'. " Yes
      rv_ok = abap_true.

    WHEN 'A'. " Cancel
      rv_ok = abap_undefined.
  ENDCASE.
ENDMETHOD.


METHOD constructor.
  DATA lv_class  TYPE string.
  DATA lv_number TYPE i.
  DATA lo_err    TYPE REF TO cx_root.

  super->constructor( iv_read_only = iv_read_only ).

  " Screen info
  ms_screen-dynnr = iv_dynnr.
  ms_screen-prog  = iv_cprog.

  " Is integer?
  TRY.
      lv_number = iv_dynnr.
    CATCH cx_sy_conversion_no_number.
      lv_number = -1.
  ENDTRY.

  " Hide functionality in inner class
  IF lv_number > 0.
    " Use default class
    lv_class  = 'LCL_SCREEN'.
  ELSE.
    " Based on name
    CONCATENATE 'LCL_SCR_' iv_dynnr INTO lv_class.
  ENDIF.

  TRY.
      CREATE OBJECT mo_helper TYPE (lv_class)
        EXPORTING
          io_eui_screen = me
          ir_context    = ir_context.
    CATCH cx_sy_create_object_error INTO lo_err.
      zcx_eui_exception=>raise_sys_error( io_error = lo_err ).
      RETURN.
  ENDTRY.

  mo_helper->fill_from_context( ).
ENDMETHOD.


METHOD customize.
  DATA ls_screen TYPE screen.
  DATA ls_map TYPE ts_map.

  " Pass as 1 parameter
  ls_screen-name      = name.
  ls_screen-group1    = group1.
  ls_screen-input     = ls_map-input    = input.
  ls_screen-required  = ls_map-required = required.
  ls_screen-output    = output.
  ls_screen-invisible = invisible.
  ls_screen-active    = active.

  ls_map-name      = iv_fieldname.
  ls_map-label     = iv_label.
  ls_map-sub_fdesc = iv_sub_fdesc.

  mo_helper->customize(
   is_screen = ls_screen
   is_map    = ls_map ).
ENDMETHOD.


METHOD edit_in_popup.
  DATA lt_comp             TYPE cl_abap_structdescr=>component_table.
  DATA ls_comp             TYPE abap_componentdescr.
  DATA lo_struc            TYPE REF TO cl_abap_structdescr.
  DATA lr_data             TYPE REF TO data.
  DATA lv_required         TYPE screen-required VALUE '0'.
  DATA lo_screen           TYPE REF TO zcl_eui_screen.
  DATA lo_manager          TYPE REF TO zif_eui_manager.
  DATA lo_error            TYPE REF TO cx_root.
  DATA lv_list_box         TYPE abap_bool.
  FIELD-SYMBOLS <ls_struc> TYPE any.
  FIELD-SYMBOLS <lv_value> TYPE any.

  CLEAR cv_ok.

  " 1 field only
  ls_comp-name = 'P_OK'.
  ls_comp-type ?= cl_abap_typedescr=>describe_by_data( cv_value ).
  INSERT ls_comp INTO TABLE lt_comp.

  " Create data
  lo_struc = cl_abap_structdescr=>create( lt_comp ).
  CREATE DATA lr_data TYPE HANDLE lo_struc.

  " As structure
  ASSIGN lr_data->* TO <ls_struc>.
  CHECK sy-subrc = 0.

  " Initial value
  ASSIGN COMPONENT 'P_OK' OF STRUCTURE <ls_struc> TO <lv_value>.
  CHECK sy-subrc = 0.
  <lv_value> = cv_value.

  TRY.
      " Pass params
      CREATE OBJECT lo_screen
        EXPORTING
          iv_dynnr   = zcl_eui_screen=>mc_dynnr-free_sel
          ir_context = lr_data. " <--- Set initial values
      lo_manager = lo_screen.
    CATCH zcx_eui_exception INTO lo_error.
      MESSAGE lo_error TYPE 'S' DISPLAY LIKE 'E'.
      RETURN.
  ENDTRY.

**********************************************************************
  " For pbo
  IF iv_required = abap_true.
    lv_required = '1'.
  ENDIF.

  lo_screen->customize(
   iv_fieldname = 'P_OK'
   iv_label     = iv_label
   required     = lv_required ).

  lo_manager->popup( iv_col_end = 118 ).

  " Do not clear status & title
  lo_manager->ms_status-title    = iv_title.
  lo_manager->ms_status-is_fixed = abap_true.

  " If pressed OK
  CHECK lo_manager->show( ) = 'OK'.

  " Set new value
  cv_value = <lv_value>.
  MESSAGE s019(zeui_message).
  cv_ok = abap_true.

*  IF iv_rollname IS NOT INITIAL.
*    DATA lt_field TYPE STANDARD TABLE OF sval.
*    DATA ls_field TYPE REF TO sval.
*    DATA lv_rc    TYPE char1.
*    APPEND INITIAL LINE TO lt_field REFERENCE INTO ls_field.
*
*    " For F4
*    SPLIT iv_rollname AT '-' INTO ls_field->tabname ls_field->fieldname.
*    CHECK sy-subrc = 0
*     AND ls_field->tabname IS NOT INITIAL
*     AND ls_field->fieldname IS NOT INITIAL.
*
*    ls_field->value = cv_value.
*
*    CALL FUNCTION 'POPUP_GET_VALUES'
*      EXPORTING
*        no_value_check  = abap_true
*        popup_title     = iv_title
*      IMPORTING
*        returncode      = lv_rc
*      TABLES
*        fields          = lt_field
*      EXCEPTIONS
*        error_in_fields = 1
*        OTHERS          = 2.
*    IF sy-subrc <> 0 OR lv_rc = 'A'.
*      MESSAGE s118(ed) DISPLAY LIKE 'E'.
*      RETURN.
*    ENDIF.
*
*    " First row
*    READ TABLE lt_field REFERENCE INTO ls_field INDEX 1.
*    CHECK sy-subrc = 0.
*  ENDIF.
ENDMETHOD.


METHOD get_context.
  DATA ls_map                TYPE REF TO ts_map.

  " Read from screen
  IF iv_read = abap_true.
    LOOP AT mo_helper->mt_map REFERENCE INTO ls_map WHERE ui_type <> zcl_eui_type=>mc_ui_type-table
                                                      AND ui_type <> zcl_eui_type=>mc_ui_type-string.
      mo_helper->read_from_screen( ir_map = ls_map ).
    ENDLOOP.
  ENDIF.

  " Return updated
  rr_context = mo_helper->mr_context.
ENDMETHOD.


METHOD SHOW_RANGE.
  DATA ls_tabfld            TYPE rstabfield.
  DATA lv_title             TYPE sytitle.
  FIELD-SYMBOLS <lt_range>  TYPE STANDARD TABLE.

  " Table name and field
  zcl_eui_type=>split_type(
   EXPORTING
     iv_datatype = is_field_desc-rollname
   IMPORTING
     ev_table    = ls_tabfld-tablename
     ev_field    = ls_tabfld-fieldname ).
  CHECK ls_tabfld-fieldname IS NOT INITIAL.

  " Range table
  ASSIGN ir_cur_value->* TO <lt_range>.

  " Show ranges
  lv_title = is_field_desc-label.
*    IF lcl_opt=>is_editable( is_fld_value-is_editable ) <> abap_true.
*      lv_display = abap_true.
*    ENDIF.

  CALL FUNCTION 'COMPLEX_SELECTIONS_DIALOG'
    EXPORTING
      title         = lv_title
      tab_and_field = ls_tabfld
      just_display  = iv_read_only
    TABLES
      range         = <lt_range>
    EXCEPTIONS
      OTHERS        = 1.
  CHECK sy-subrc = 0.

  " ok
  rv_update = abap_true.
ENDMETHOD.


METHOD zif_eui_manager~pai.
  super->pai(
   EXPORTING
    iv_command = iv_command
   CHANGING
    cv_close   = cv_close ).

  " String or table editor
  DATA lv_map_index  TYPE i.
  DATA lv_read_after TYPE abap_bool.

  mo_helper->check_pai(
   EXPORTING
     iv_command = iv_command
   CHANGING
     cv_close      = cv_close
     cv_read_after = lv_read_after
     cv_map_index  = lv_map_index ).

  mo_helper->call_editor( lv_map_index ).

  " Copy data back & Read from screen
  IF cv_close = abap_true AND lv_read_after = abap_true.
    get_context( ).
  ENDIF.
ENDMETHOD.


METHOD zif_eui_manager~pbo.
  DATA lv_set_status LIKE iv_set_status.
  lv_set_status = iv_set_status.

  mo_helper->pbo(
   EXPORTING
     iv_before     = abap_true
   CHANGING
     cv_set_status = lv_set_status ).

  " Just call event handlers. No container
  super->pbo(
   io_container  = io_container
   iv_set_status = lv_set_status ).

  mo_helper->pbo( iv_after = abap_true ).
ENDMETHOD.


METHOD zif_eui_manager~show.
  DATA lo_err TYPE REF TO zcx_eui_exception.
  TRY.
      " Show or preapre screen
      mo_helper->show(
       EXPORTING
         iv_before    = abap_true
       CHANGING
         cv_close_cmd = rv_close_cmd ).

      " Default behaviour
      IF rv_close_cmd IS INITIAL.
        rv_close_cmd = super->show(
          io_handler      = io_handler
          iv_handlers_map = iv_handlers_map ).
      ENDIF.

      " second time
      mo_helper->show(
       EXPORTING
         iv_after      = abap_true
       CHANGING
         cv_close_cmd = rv_close_cmd ).

    CATCH zcx_eui_exception INTO lo_err.
      MESSAGE lo_err TYPE 'S' DISPLAY LIKE 'E'.
      RETURN.
  ENDTRY.
ENDMETHOD.
ENDCLASS.