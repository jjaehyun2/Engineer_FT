FUNCTION zalv_popup.
*"----------------------------------------------------------------------
*"*"Interface local:
*"  IMPORTING
*"     REFERENCE(I_TABLE_DATA) TYPE  ANY TABLE
*"     REFERENCE(I_STRUCTURE) TYPE  RSRD1-DDTYPE_VAL
*"     REFERENCE(I_IGNORING_FIELDS) TYPE  ALFIELDNAMES OPTIONAL
*"     REFERENCE(I_HOTSPOT) TYPE  ZTHOTSPOT OPTIONAL
*"     REFERENCE(I_TOTALROW) TYPE  ALFIELDNAMES OPTIONAL
*"     REFERENCE(I_SELECTION_MODE) TYPE  SALV_DE_CONSTANT OPTIONAL
*"     REFERENCE(I_DIMENSION) TYPE  ZSDIMENSIONS OPTIONAL
*"     REFERENCE(I_TITLE) TYPE  LVC_TITLE OPTIONAL
*"  EXPORTING
*"     REFERENCE(E_SELECTED_ROWS) TYPE  SALV_T_ROW
*"----------------------------------------------------------------------

* For dinamic table
  DATA: gt_table_data  TYPE REF TO data,
        lt_fcat        TYPE lvc_t_fcat.

* For ALV
  DATA: lo_selections TYPE REF TO cl_salv_selections,
        lo_columns    TYPE REF TO cl_salv_columns_table,
        lo_column     TYPE REF TO cl_salv_column_table,
        lo_aggrs      TYPE REF TO cl_salv_aggregations,
        lo_events     TYPE REF TO cl_salv_events_table,
        lo_display    TYPE REF TO cl_salv_display_settings.

  FIELD-SYMBOLS: <field_ignored> LIKE LINE OF i_ignoring_fields,
                 <hotspot>       LIKE LINE OF i_hotspot,
                 <totalrow>      LIKE LINE OF i_totalrow.

* Init global variables
  CLEAR: gt_selected_rows, gt_table_data.

* Create dinamic table to receive import data
  CALL FUNCTION 'LVC_FIELDCATALOG_MERGE'
    EXPORTING
      i_structure_name       = i_structure
    CHANGING
      ct_fieldcat            = lt_fcat
    EXCEPTIONS
      inconsistent_interface = 1
      program_error          = 2
      OTHERS                 = 3.
  IF sy-subrc <> 0.
    RETURN.
  ENDIF.

  cl_alv_table_create=>create_dynamic_table(
   EXPORTING
    i_style_table             = 'X'
    it_fieldcatalog           = lt_fcat
   IMPORTING
    ep_table                  = gt_table_data
   EXCEPTIONS
    generate_subpool_dir_full = 1
    OTHERS                    = 2
 ).

  ASSIGN gt_table_data->* TO <gt_table_data>.

* Populate dinamic table
  LOOP AT i_table_data ASSIGNING <table_data>.

    APPEND INITIAL LINE TO <gt_table_data> ASSIGNING <row_data>.
    MOVE-CORRESPONDING <table_data> TO <row_data>.

  ENDLOOP.

* Create ALV
  TRY.
      cl_salv_table=>factory(
        IMPORTING
          r_salv_table = go_salv_table
        CHANGING
          t_table      = <gt_table_data> ).
    CATCH cx_salv_msg.
  ENDTRY.

  go_salv_table->set_screen_status(
    EXPORTING
      report        = sy-repid                        " ABAP Program: Current Master Program
      pfstatus      = 'SALV_POPUP'                    " Screens, Current GUI Status
      set_functions = go_salv_table->c_functions_none " ALV: Data Element for Constants
  ).

* Select multiple rows
  lo_selections = go_salv_table->get_selections( ).
  IF i_selection_mode IS INITIAL.
    lo_selections->set_selection_mode( if_salv_c_selection_mode=>row_column ).
  ELSE.
    lo_selections->set_selection_mode( i_selection_mode ).
  ENDIF.

* Optimize columns
  lo_columns = go_salv_table->get_columns( ).
  lo_columns->set_optimize( 'X' ).

* Ignore columns
  LOOP AT i_ignoring_fields ASSIGNING <field_ignored>.
    TRY.
        lo_column ?= lo_columns->get_column( <field_ignored> ).
        lo_column->set_visible( if_salv_c_bool_sap=>false ).
      CATCH cx_salv_not_found.
        CONTINUE.
    ENDTRY.
  ENDLOOP.

* Hotspot
  gt_hotspot = i_hotspot.
  LOOP AT i_hotspot ASSIGNING <hotspot>.
    TRY.
        lo_column ?= lo_columns->get_column( <hotspot>-field ).
        lo_column->set_cell_type( if_salv_c_cell_type=>hotspot ).
      CATCH cx_salv_not_found..
    ENDTRY.
  ENDLOOP.

* Total row
  LOOP AT i_totalrow ASSIGNING <totalrow>.
    lo_aggrs = go_salv_table->get_aggregations( ).
    TRY.
        CALL METHOD lo_aggrs->add_aggregation
          EXPORTING
            columnname  = <totalrow>
            aggregation = if_salv_c_aggregation=>total.
      CATCH cx_salv_data_error.
      CATCH cx_salv_not_found.
      CATCH cx_salv_existing.
    ENDTRY.
  ENDLOOP.

* Title
  IF i_title IS NOT INITIAL.
    lo_display = go_salv_table->get_display_settings( ).
    lo_display->set_list_header( i_title ).
  ENDIF.

* Events
  lo_events = go_salv_table->get_event( ).

  CREATE OBJECT event_handler.
  SET HANDLER event_handler->on_link_click FOR lo_events.
  SET HANDLER event_handler->on_user_command FOR lo_events.

* Display ALV
  IF i_dimension IS INITIAL.
    go_salv_table->set_screen_popup(
        start_column = 3
        end_column   = 180
        start_line   = 1
        end_line     = 15 ).
  ELSE.
    go_salv_table->set_screen_popup(
        start_column = i_dimension-start_column
        end_column   = i_dimension-end_column
        start_line   = i_dimension-start_line
        end_line     = i_dimension-end_line ).
  ENDIF.

  go_salv_table->display( ).

* Return selected rows
  e_selected_rows = gt_selected_rows.

ENDFUNCTION.