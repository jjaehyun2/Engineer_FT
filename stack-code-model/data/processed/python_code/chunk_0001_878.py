class ZCL_ALV_TOOL definition
  public
  final
  create public .

public section.

  methods CONSTRUCTOR
    importing
      !IM_EVENT_HANDLER type ref to ZIF_ALV_EVENT_HANDLER optional .
  methods GET_ALV_ROW
    importing
      !IM_ROW type SALV_DE_ROW
    returning
      value(RE_ROW) type ref to DATA .
  methods INITIALIZE
    importing
      !IM_ALV_KEY type ZZE_ALV_KEY optional
      !IM_OBJECT type ref to OBJECT
      !IM_EVENT_HANDLER type ref to ZIF_ALV_EVENT_HANDLER optional
    changing
      !CH_DATA type TABLE .
  methods GET_EVENT
    returning
      value(RE_EVENT) type ref to CL_SALV_EVENTS_TABLE .
  methods REFRESH .
  type-pools ABAP .
  methods GET_STRUCT_NAME
    returning
      value(RE_STRUCT) type ABAP_ABSTYPENAME .
  methods GET_COLUMNS
    returning
      value(RE_RETURN) type ref to CL_SALV_COLUMNS_TABLE .
  methods DISPLAY .
  methods SET_EVENT_HANDLER
    importing
      !IM_EVENT_HANDLER type ref to ZIF_ALV_EVENT_HANDLER .
protected section.
private section.

  data AT_O_ALV type ref to CL_SALV_TABLE .
  data AT_ALV_KEY type ZZE_ALV_KEY .
  data AT_DATA type ref to DATA .
  data AT_OBJECT type ref to OBJECT .
  data AT_EVENT_HANDLER type ref to ZIF_ALV_EVENT_HANDLER .
  constants C_PROG type SYREPID value 'ZPR_REPORT_TEMPLATE'. "#EC NOTEXT
  constants C_PFSTATUS type SYPFKEY value 'STANDARD'. "#EC NOTEXT

  methods GET_REPID
    returning
      value(RE_RETURN) type SYREPID .
  methods SET_FUNCTIONS_ALV .
  methods COLUMN_HEADING
    importing
      !IM_COLUMN_NAME type LVC_FNAME
      !IM_TXT type SCRTEXT_L .
  methods SET_COLUMNS_ALV .
  methods SET_HEADER_ALV .
  methods ONDOUBLE_CLICK
    for event DOUBLE_CLICK of CL_SALV_EVENTS_TABLE
    importing
      !ROW
      !COLUMN .
  methods ONLINK_CLICK
    for event LINK_CLICK of CL_SALV_EVENTS_TABLE
    importing
      !ROW
      !COLUMN .
  methods ONUSER_COMMAND
    for event ADDED_FUNCTION of CL_SALV_EVENTS
    importing
      !E_SALV_FUNCTION .
  methods ONBEFORE_ACTION
    for event BEFORE_SALV_FUNCTION of CL_SALV_EVENTS_TABLE
    importing
      !E_SALV_FUNCTION .
  methods ONAFTER_ACTION
    for event AFTER_SALV_FUNCTION of CL_SALV_EVENTS_TABLE
    importing
      !E_SALV_FUNCTION .
ENDCLASS.



CLASS ZCL_ALV_TOOL IMPLEMENTATION.


method COLUMN_HEADING.

  DATA lo_cx_salv_not_found TYPE REF TO cx_salv_not_found.
  data lv_string TYPE string.
  data lo_columns  TYPE  REF TO  cl_salv_columns_table.
  data lo_column   TYPE  REF TO  cl_salv_column.
  data lv_len type DDLENG.
  data lv_medium type scrtext_m.
  data lv_short type scrtext_s.

  lv_len = strlen( im_txt ).
  lv_medium = im_txt.
  lv_short = im_txt.

  lo_columns = at_o_alv->get_columns( ).
  TRY.
      lo_column = lo_columns->get_column( im_column_name ).
      lo_column->set_long_text( im_txt ).
      lo_column->set_medium_text( lv_medium ).
      lo_column->set_short_text( lv_short ).
      lo_column->set_output_length( lv_len ).
    CATCH cx_salv_not_found INTO lo_cx_salv_not_found.
      lv_string = lo_cx_salv_not_found->get_text( ).
      MESSAGE i999 WITH lv_string.
  ENDTRY.

  endmethod.


method CONSTRUCTOR.

  at_event_handler = im_event_handler.

  endmethod.


method DISPLAY.

  data lv_badi TYPE REF TO ZBADI_MANIPULATE_ALV.
  data lo_columns  TYPE  REF TO  cl_salv_columns_table.
  data lo_events type ref to CL_SALV_EVENTS_TABLE.

  check at_data is bound.

  TRY.
    GET BADI lv_badi FILTERS alv_key = at_alv_key.

    CALL BADI lv_badi->manipulate_alv
      EXPORTING
        im_alv = me
        im_report = at_object.

  CATCH cx_badi_not_implemented.
  CATCH cx_badi               "No BADI implementation exist
        cx_sy_dyn_call_error.
  ENDTRY.


  lo_events = get_event( ).
  set handler ondouble_click for lo_events.
  set handler onlink_click for lo_events.
  set handler onuser_command for lo_events.
  set handler onbefore_action for lo_events.
  set handler onafter_action for lo_events.

*   Display the ALV
*   Column Optimize
  lo_columns = at_o_alv->get_columns( ).
  lo_columns->set_optimize( 'X' ).

  at_o_alv->display( ).

  endmethod.


method GET_ALV_ROW.

    data: lv_data type ref to data.
    field-symbols: <table> type standard table.
    field-symbols: <row> type any.

    assign at_data->* to <table>.
    create data lv_data like line of <table>.

    read table <table> assigning <row> index im_row.
    if <row> is assigned.
      get reference of <row> into lv_data.
    endif.

    re_row = lv_data.

  endmethod.


method GET_COLUMNS.

  re_return = at_o_alv->get_columns( ).

  endmethod.


method GET_EVENT.

  re_event = at_o_alv->get_event( ).

  endmethod.


method GET_REPID.

  CALL FUNCTION 'RS_CUA_GET_STATUS_FUNCTIONS'
    EXPORTING
      PROGRAM                 = sy-cprog
      STATUS                  = c_pfstatus
   EXCEPTIONS
     MENU_NOT_FOUND          = 1
     PROGRAM_NOT_FOUND       = 2
     STATUS_NOT_FOUND        = 3
     OTHERS                  = 4.

  if SY-SUBRC <> 0.
    CALL FUNCTION 'RS_CUA_GET_STATUS_FUNCTIONS'
      EXPORTING
        PROGRAM                 = c_prog
        STATUS                  = c_pfstatus
     EXCEPTIONS
       MENU_NOT_FOUND          = 1
       PROGRAM_NOT_FOUND       = 2
       STATUS_NOT_FOUND        = 3
       OTHERS                  = 4.

    if sy-subrc = 0.
       re_return = c_prog.
    endif.
  else.
    re_return = sy-cprog.
  endif.

  endmethod.


method GET_STRUCT_NAME.

  re_struct = CL_ABAP_STRUCTDESCR=>describe_by_data_ref( at_data )->GET_RELATIVE_NAME( ).

  endmethod.


method INITIALIZE.

  data lo_msg TYPE REF TO cx_salv_msg.
  data lv_string type string.
  DATA lv_badi TYPE REF TO ZBADI_ALV_TOOL_TRANSFORM_DATA.
  field-symbols <fs_table> type table.
  field-symbols <fs_line> type any.
  field-symbols <fs_new_line> type any.
  data lv_line type ref to data.
  data lt_table type ref to data.
  data lv_name type string.

  if im_event_handler is supplied.
    at_event_handler = im_event_handler.
  endif.

  if im_alv_key is supplied.
    at_alv_key = im_alv_key.
  endif.
  if at_object is not bound.
    at_object = im_object.
  endif.

*** Get the BADI using ALV KEY as filter
*** This BAdI is used to modify the data and/or structure of the displayed table
  TRY.
    GET BADI lv_badi FILTERS alv_key = at_alv_key.

    CALL BADI lv_badi->get_struct_name
      CHANGING
        ch_name = lv_name.

    if lv_name is not initial.
      create data lv_line type (lv_name).
      create data lt_table type table of (lv_name).
      assign lv_line->* to <fs_new_line>.

      loop at ch_data assigning <fs_line>.
        TRY.
            CALL BADI lv_badi->transform_data_alv
              EXPORTING
                im_data = <fs_line>
                im_object = at_object
              CHANGING
                ch_data = <fs_new_line>.

            if <fs_table> is not assigned.
              assign lt_table->* TO <fs_table>.
            endif.

            append <fs_new_line> to <fs_table>.

          CATCH cx_badi               "No BADI implementation exist
                cx_sy_dyn_call_error. "Catch dynamic call errors
        ENDTRY.
      endloop.
    else.
      assign ch_data to <fs_table>.
    endif.
** If BAdI is not implemented, just copy the table
  CATCH cx_badi_not_implemented.
    assign ch_data to <fs_table>.
  ENDTRY.

**  Call factory method of ALV Grid
  check <fs_table> is assigned.

  TRY.
    if at_o_alv is bound.
      free at_o_alv.
    endif.
      CALL METHOD cl_salv_table=>factory
        IMPORTING
          r_salv_table = at_o_alv
        CHANGING
          t_table      = <fs_table>.

  CATCH cx_salv_msg INTO lo_msg.
    lv_string = lo_msg->get_text( ).
    MESSAGE i999 WITH lv_string.
  ENDTRY.

** Save the data in a Class Attribute
  get reference of <fs_table> into at_data.


** Configure ALV based on tables
  me->set_functions_alv( ).
  me->set_header_alv( ).
  me->set_columns_alv( ).

  endmethod.


method ONAFTER_ACTION.

  check at_event_handler is bound.

  at_event_handler->onafter_action( exporting im_function = e_salv_function
                                              im_alv_key = at_alv_key ).

  refresh( ).

  endmethod.


method ONBEFORE_ACTION.

  check at_event_handler is bound.

  at_event_handler->onbefore_action( exporting im_function = e_salv_function
                                               im_alv_key = at_alv_key ).

  refresh( ).

  endmethod.


method ONDOUBLE_CLICK.

  check at_event_handler is bound.

  at_event_handler->ondouble_click( im_row = row
                                    im_col = column
                                    im_data = get_alv_row( row )
                                    im_struct = get_struct_name( )
                                    im_alv_key = at_alv_key ).
  refresh( ).

  endmethod.


method ONLINK_CLICK.

  check at_event_handler is bound.

  at_event_handler->onlink_click( im_row = row
                                  im_col = column
                                  im_data = get_alv_row( row )
                                  im_struct = get_struct_name( )
                                  im_alv_key = at_alv_key ).
  refresh( ).

  endmethod.


method ONUSER_COMMAND.

  data lv_method type string.

  check at_event_handler is bound.

  concatenate 'ONFUNC' e_salv_function+4(2) into lv_method.
  try.
    call method at_event_handler->(lv_method) exporting im_alv_key = at_alv_key.
  catch cx_root.

  endtry.

  refresh( ).

  endmethod.


method REFRESH.

  at_o_alv->refresh( ).

  endmethod.


method SET_COLUMNS_ALV.

*   Column Heading
*    DATA: ls_components TYPE abap_compdescr.
    DATA: ls_components TYPE DFIES.
    data: lo_tabdescr type ref to cl_abap_structdescr.
    data lt_dfies type ddfields.
    data: lv_data type ref to data.
    field-symbols: <table> type standard table.
    data lo_columns TYPE REF TO cl_salv_columns_table.
    data lo_column TYPE REF TO cl_salv_column_table.

    lo_columns = at_o_alv->get_columns( ).

    assign at_data->* to <table>.
    create data lv_data like line of <table>.

    lo_tabdescr ?= cl_abap_structdescr=>describe_by_data_ref( lv_data ).
    lt_dfies = CL_SALV_DATA_DESCR=>read_structdescr( lo_tabdescr ).


*    loop at lo_tabdescr->components into ls_components.
    loop at lt_dfies into ls_components.
      if ZCL_ALV_CONFIG=>exists_text( im_alv_key = at_alv_key im_column_name = ls_components-FIELDNAME ) = 'X'.
        me->column_heading( im_column_name = ls_components-FIELDNAME im_txt = ZCL_ALV_CONFIG=>get_text( im_alv_key = at_alv_key im_column_name = ls_components-FIELDNAME ) ).
        lo_column ?= lo_columns->get_column( ls_components-FIELDNAME ).
        lo_column->set_visible( ZCL_ALV_CONFIG=>is_active( im_alv_key = at_alv_key im_column_name = ls_components-FIELDNAME ) ).
        if ZCL_ALV_CONFIG=>is_hotspot( im_alv_key = at_alv_key im_column_name = ls_components-FIELDNAME ) = 'X'.
          lo_column->set_cell_type( if_salv_c_cell_type=>hotspot ).
        endif.
      endif.
    endloop.

  endmethod.


method SET_EVENT_HANDLER.

  check at_event_handler is bound.

  at_event_handler = im_event_handler.

  endmethod.


method SET_FUNCTIONS_ALV.

*  data lt_functions type SALV_T_UI_FUNC.
*  data lv_function type line of SALV_T_UI_FUNC.
*  data lv_prog type syrepid.
*  data lt_active_functions type ZZT_ALV_FUNC.
*  data lv_func_name type zze_alv_functions.
*  data lo_functions type ref to cl_salv_functions_list.
*  data lo_layout TYPE REF TO cl_salv_layout.
*  data lv_key TYPE salv_s_layout_key.
*
*** Look for program ID to use to get the PF Status
*  lv_prog = get_repid( ).
*
*  check lv_prog is not initial and at_o_alv is bound.
*
*** Activate the saving layout option
*  lo_layout = at_o_alv->get_layout( ).
*  lv_key-report = lv_prog.
*  lo_layout->set_key( lv_key ).
*  lo_layout->set_default( 'X' ).
*  lo_layout->set_save_restriction( if_salv_c_layout=>restrict_none ).
*
*** Set PF Status with predefined functions
*  at_o_alv->set_screen_status( pfstatus = c_pfstatus
*                               report = lv_prog
*                               set_functions = at_o_alv->c_functions_all ).
*
*** Get Active Functions from Config
*  lt_active_functions = ZCL_ALV_CONFIG=>get_functions( at_alv_key ).
**
*  lo_functions = at_o_alv->get_functions( ).
**  lo_functions->set_all( abap_true ).
*  lt_functions = lo_functions->get_functions( ).
*
** Deactivate those client functions  not in config
*  loop at lt_functions into lv_function.
*    lv_func_name = lv_function-r_function->GET_NAME( ).
*    if lv_func_name(4) eq 'FUNC'.
*      read table lt_active_functions transporting no fields with key function = lv_func_name.
*      if sy-subrc eq 4.
*        lv_function-r_function->set_visible( abap_false ).
*      endif.
*    endif.
*  endloop.

  endmethod.


method SET_HEADER_ALV.

  data lv_line type ZHRT_ALV_HEADER.
  data lt_table type ZZT_ALV_HEADER.
  data lv_string type string.
  data lv_method type string.
  data lv_field type string.
  data lv_struct type string.
  field-symbols <fs_string> type any.
  field-symbols <fs_struct> type any.
  field-symbols <fs_field> type any.
  data lv_data type ref to data.
  data lo_grid TYPE REF TO cl_salv_form_layout_grid.
  data lo_flow TYPE REF TO cl_salv_form_layout_flow.
  data lv_row type i.
  data lv_col type i.

  CREATE OBJECT lo_grid.

  lt_table = ZCL_ALV_CONFIG=>get_header( at_alv_key ).

  loop at lt_table into lv_line.
    lv_row = lv_line-alv_row.
*    lv_col = ( lv_line-alv_col * 2 ) - 1.
    lv_col = lv_line-alv_col.
    lo_flow = lo_grid->create_flow( row = lv_row column = lv_col ).
    if lv_line-alv_label is not initial.
      lo_flow->create_label( text = lv_line-alv_label tooltip = lv_line-alv_label ).
*      lv_col = lv_col + 1.
    endif.
    try.
      case lv_line-alv_header.
        when '1'.
          call method at_object->(lv_line-source) receiving re_return = lv_string.
        when '2'.
          assign at_object->(lv_line-source) to <fs_string>.
          if sy-subrc eq 0.
            lv_string = <fs_string>.
          endif.
        when '3'.
          assign component lv_line-source of structure sy to <fs_string>.
          if sy-subrc eq 0.
            lv_string = <fs_string>.
          endif.
        when '4'.
          lv_string = lv_line-source.
        when '5'.
          lv_method = substring_before( val = lv_line-source sub = '-' ).
          lv_struct = substring_before( val = substring_after( val = lv_line-source sub = '-' ) sub = '-' ).
          lv_field = substring_after( val = substring_after( val = lv_line-source sub = '-' ) sub = '-' ).
          create data lv_data type (lv_struct).
          assign lv_data->* to <fs_struct>.
          call method at_object->(lv_method) receiving re_return = <fs_struct>.
          assign component lv_field of structure <fs_struct> to <fs_field>.
          if sy-subrc eq 0.
            lv_string = <fs_field>.
          endif.
      endcase.
      lo_flow->create_text( text = lv_string tooltip = lv_string ).
      clear lv_string.
      unassign <fs_string>.
    catch cx_root.
    endtry.
  endloop.

  at_o_alv->set_top_of_list( value = lo_grid ).

  endmethod.
ENDCLASS.