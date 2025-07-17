*&---------------------------------------------------------------------*
*& Report  zdemogit_rept_alv_factory2
*&
*&---------------------------------------------------------------------*
*&
*&
*&---------------------------------------------------------------------*
REPORT zdemogit_rept_alv_factory2.

"Define Selection screen
PARAMETERS: p_test TYPE xfeld.
"global table
"define the global table display
TYPES: BEGIN OF ty_output,
*       <here your fields...>
         field TYPE c,
       END OF ty_output,
       ty_output_tt TYPE STANDARD TABLE OF ty_output.
" Table global
DATA gt_output TYPE ty_output_tt.
"e.g
DATA: lt_output TYPE STANDARD TABLE OF vbap.

*------------------------------------------------------------------------------*
* SELECTION SCREEN
*------------------------------------------------------------------------------*
*SELECTION-SCREEN BEGIN OF BLOCK report WITH FRAME TITLE text-001.
*PARAMETERS : p_date TYPE zzbc_log_ks-start_date DEFAULT sy-datum OBLIGATORY.
*SELECT-OPTIONS s_time FOR ztimez-uzeit DEFAULT sy-timlo.
*
*PARAMETERS: p_sddoc TYPE vbeln OBLIGATORY,
*            p_func  TYPE sycprog DEFAULT 'ZKS_SD_DOC_CHANGE' NO-DISPLAY,
*            p_uname TYPE uname DEFAULT 'RFCPO' NO-DISPLAY.
*SELECTION-SCREEN END OF BLOCK report.

CLASS lcl_report DEFINITION ABSTRACT FINAL CREATE PRIVATE.
  PUBLIC SECTION.
    INTERFACES: zif_git_report.

ENDCLASS.

CLASS lcl_alv_factory DEFINITION.
  PUBLIC SECTION.
    INTERFACES zif_git_report_alv_factory_v2.
    METHODS constructor IMPORTING it_table TYPE REF TO data." IMPORTING et_table TYPE table.
ENDCLASS.

CLASS lcl_report IMPLEMENTATION.

  METHOD zif_git_report~initialization.
  ENDMETHOD.
  METHOD zif_git_report~start_of_selection.
  ENDMETHOD.
  METHOD zif_git_report~end_of_selection.
  ENDMETHOD.
  METHOD zif_git_report~load_of_program.
  ENDMETHOD.
  METHOD zif_git_report~at_selection_screen_output.
  ENDMETHOD.
  METHOD zif_git_report~at_selection_screen.
  ENDMETHOD.
  METHOD zif_git_report~at_selection_screen_on.
  ENDMETHOD.
  METHOD zif_git_report~at_selection_screen_on_end_of.
  ENDMETHOD.
  METHOD zif_git_report~atsel_scrn_on_help_request_for.
  ENDMETHOD.
  METHOD zif_git_report~atsel_scr_on_value_request_for.
  ENDMETHOD.
  METHOD zif_git_report~at_selection_screen_on_block.
  ENDMETHOD.
  METHOD zif_git_report~atsel_scr_on_radiobutton_group.
  ENDMETHOD.


ENDCLASS.

CLASS lcl_alv_factory IMPLEMENTATION.
  METHOD constructor.
    " pass it_table table as import doesn't allow to use as changing on factory call
    FIELD-SYMBOLS <table> TYPE ANY TABLE.
*    GET REFERENCE OF it_table INTO gr_table.
    ASSIGN it_table->* TO <table>.
    TRY.
        cl_salv_table=>factory(
*    EXPORTING
*      list_display   = IF_SALV_C_BOOL_SAP=>FALSE    " ALV Displayed in List Mode
*      r_container    =     " Abstract Container for GUI Controls
*      container_name =
      IMPORTING
        r_salv_table   =    me->zif_git_report_alv_factory_v2~m_alv_fact   " Basis Class Simple ALV Tables
          CHANGING
            t_table        = <table>
        ).
      CATCH cx_salv_msg.    "
    ENDTRY.

    "get events
    me->zif_git_report_alv_factory_v2~m_tb_fact_evt = me->zif_git_report_alv_factory_v2~m_alv_fact->get_event( ).  "table cl_salv_events_table.
    me->zif_git_report_alv_factory_v2~m_alv_fact_evt = me->zif_git_report_alv_factory_v2~m_alv_fact->get_event( ). "ALV object cl_salv_events.
    "get selections
    me->zif_git_report_alv_factory_v2~m_selections_alv = me->zif_git_report_alv_factory_v2~m_alv_fact->get_selections( ).
    "get functions
    me->zif_git_report_alv_factory_v2~m_functions_alv = me->zif_git_report_alv_factory_v2~m_alv_fact->get_functions( ).
    " get sorting
    me->zif_git_report_alv_factory_v2~m_sorts_alv = me->zif_git_report_alv_factory_v2~m_alv_fact->get_sorts( ).
    "
    me->zif_git_report_alv_factory_v2~m_display_alv = me->zif_git_report_alv_factory_v2~m_alv_fact->get_display_settings( ).
    me->zif_git_report_alv_factory_v2~m_layout_alv = me->zif_git_report_alv_factory_v2~m_alv_fact->get_layout( ).

    "EVENTS to register!
    SET HANDLER me->zif_git_report_alv_factory_v2~on_added_function  "on user command
               FOR me->zif_git_report_alv_factory_v2~m_alv_fact_evt.

    SET HANDLER me->zif_git_report_alv_factory_v2~on_after_salv_function
               FOR me->zif_git_report_alv_factory_v2~m_alv_fact_evt.
    SET HANDLER me->zif_git_report_alv_factory_v2~on_before_salv_function
               FOR me->zif_git_report_alv_factory_v2~m_alv_fact_evt.
    SET HANDLER me->zif_git_report_alv_factory_v2~on_end_of_page
              FOR me->zif_git_report_alv_factory_v2~m_alv_fact_evt.
    SET HANDLER me->zif_git_report_alv_factory_v2~on_top_of_page
              FOR me->zif_git_report_alv_factory_v2~m_alv_fact_evt.
    SET HANDLER me->zif_git_report_alv_factory_v2~on_double_click
              FOR me->zif_git_report_alv_factory_v2~m_tb_fact_evt.
    SET HANDLER me->zif_git_report_alv_factory_v2~on_link_click
              FOR me->zif_git_report_alv_factory_v2~m_tb_fact_evt.

  ENDMETHOD.
  METHOD zif_git_report_alv_factory_v2~on_added_function.
    "Equal to to on user command
    BREAK-POINT.
  ENDMETHOD.

  METHOD zif_git_report_alv_factory_v2~on_after_salv_function.

  ENDMETHOD.

  METHOD zif_git_report_alv_factory_v2~on_before_salv_function.

  ENDMETHOD.

  METHOD zif_git_report_alv_factory_v2~on_end_of_page.

  ENDMETHOD.

  METHOD zif_git_report_alv_factory_v2~on_top_of_page.

  ENDMETHOD.
  METHOD zif_git_report_alv_factory_v2~on_double_click.
    BREAK-POINT.
  ENDMETHOD.

  METHOD zif_git_report_alv_factory_v2~on_link_click.

  ENDMETHOD.

  METHOD zif_git_report_alv_factory_v2~get_data_to_display.
    "select data
    SELECT vbeln, posnr
      FROM vbap
      INTO CORRESPONDING FIELDS OF TABLE @ct_table_data
        "lt_output
      " @DATA(lt_data)
      UP TO 100 ROWS.
    "link output table to class attributes
    GET REFERENCE OF ct_table_data INTO zif_git_report_alv_factory_v2~m_output_table.

  ENDMETHOD.

ENDCLASS.

INITIALIZATION.
  lcl_report=>zif_git_report~initialization( ).

AT SELECTION-SCREEN OUTPUT.
  lcl_report=>zif_git_report~at_selection_screen_output( ).

AT SELECTION-SCREEN.
  lcl_report=>zif_git_report~at_selection_screen( ).

LOAD-OF-PROGRAM.
  lcl_report=>zif_git_report~load_of_program( ).



AT SELECTION-SCREEN ON p_test.
  lcl_report=>zif_git_report~at_selection_screen_on( ).

*AT SELECTION-SCREEN ON END OF p_test.
*  lcl_report=>zif_git_report~at_selection_screen_on_end_of( ).

AT SELECTION-SCREEN ON HELP-REQUEST FOR p_test.
  lcl_report=>zif_git_report~atsel_scrn_on_help_request_for( ).

AT SELECTION-SCREEN ON VALUE-REQUEST FOR  p_test.
  lcl_report=>zif_git_report~atsel_scr_on_value_request_for( ).

*  AT SELECTION-SCREEN ON BLOCK
*  lcl_report=>zif_git_report~at_selection_screen_on_block( ).
*    AT SELECTION-SCREEN on RADIOBUTTON GROUP
*  lcl_report=>zif_git_report~atsel_scr_on_radiobutton_group( ).


START-OF-SELECTION.
  lcl_report=>zif_git_report~start_of_selection( ).

*END-OF-SELECTION. "obsolete
*  lcl_report=>zif_git_report~end_of_selection( ).

  GET REFERENCE OF lt_output INTO DATA(lr_tab).
  DATA(lr_factory) = NEW lcl_alv_factory( it_table = lr_tab ).



*  TRY.
*      cl_salv_table=>factory(
**    EXPORTING
**      list_display   = IF_SALV_C_BOOL_SAP=>FALSE    " ALV Displayed in List Mode
**      r_container    =     " Abstract Container for GUI Controls
**      container_name =
*    IMPORTING
*      r_salv_table   =   lr_factory->zif_git_report_alv_factory_v2~m_alv_fact   " Basis Class Simple ALV Tables
*        CHANGING
*          t_table        = lt_output
*      ).
*    CATCH cx_salv_msg.    "
*  ENDTRY.
*
*  "get events
*  lr_factory->zif_git_report_alv_factory_v2~m_tb_fact_evt = lr_factory->zif_git_report_alv_factory_v2~m_alv_fact->get_event( ).
*  lr_factory->zif_git_report_alv_factory_v2~m_alv_fact_evt = lr_factory->zif_git_report_alv_factory_v2~m_alv_fact->get_event( ).
*  "get selections
*  lr_factory->zif_git_report_alv_factory_v2~m_selections_alv = lr_factory->zif_git_report_alv_factory_v2~m_alv_fact->get_selections( ).
*  "get functions
*  lr_factory->zif_git_report_alv_factory_v2~m_functions_alv = lr_factory->zif_git_report_alv_factory_v2~m_alv_fact->get_functions( ).
*  " get sorting
*  lr_factory->zif_git_report_alv_factory_v2~m_sorts_alv = lr_factory->zif_git_report_alv_factory_v2~m_alv_fact->get_sorts( ).
*  "
*  lr_factory->zif_git_report_alv_factory_v2~m_display_alv = lr_factory->zif_git_report_alv_factory_v2~m_alv_fact->get_display_settings( ).
*  lr_factory->zif_git_report_alv_factory_v2~m_layout_alv = lr_factory->zif_git_report_alv_factory_v2~m_alv_fact->get_layout( ).
*
*  "EVENTS to register!
*  SET HANDLER lr_factory->zif_git_report_alv_factory_v2~on_added_function  "on user command
*             FOR lr_factory->zif_git_report_alv_factory_v2~m_alv_fact_evt.
*
*  SET HANDLER lr_factory->zif_git_report_alv_factory_v2~on_after_salv_function
*             FOR lr_factory->zif_git_report_alv_factory_v2~m_alv_fact_evt.
*  SET HANDLER lr_factory->zif_git_report_alv_factory_v2~on_before_salv_function
*             FOR lr_factory->zif_git_report_alv_factory_v2~m_alv_fact_evt.
*  SET HANDLER lr_factory->zif_git_report_alv_factory_v2~on_end_of_page
*            FOR lr_factory->zif_git_report_alv_factory_v2~m_alv_fact_evt.
*  SET HANDLER lr_factory->zif_git_report_alv_factory_v2~on_top_of_page
*            FOR lr_factory->zif_git_report_alv_factory_v2~m_alv_fact_evt.
*  SET HANDLER lr_factory->zif_git_report_alv_factory_v2~on_double_click
*            FOR lr_factory->zif_git_report_alv_factory_v2~m_tb_fact_evt.
*  SET HANDLER lr_factory->zif_git_report_alv_factory_v2~on_link_click
*            FOR lr_factory->zif_git_report_alv_factory_v2~m_tb_fact_evt.

  " work on columns settings
  DATA lr_column  TYPE REF TO cl_salv_column_table.
  DATA(gr_columns) = lr_factory->zif_git_report_alv_factory_v2~m_alv_fact->get_columns( ).
  TRY.
      "hide columns
      lr_column ?= gr_columns->get_column( 'NAME' ).
      lr_column->set_visible( abap_false ).

    CATCH cx_salv_not_found.
      "handle column not found

  ENDTRY.

  lr_factory->zif_git_report_alv_factory_v2~m_alv_fact->set_screen_status(
    pfstatus      = 'DISP_MAIN'
    report        = sy-repid
    set_functions = cl_salv_model_base=>c_functions_all ).

  DATA lo_functions TYPE REF TO cl_salv_functions_list.
  lo_functions =  lr_factory->zif_git_report_alv_factory_v2~m_alv_fact->get_functions( ).
  lo_functions->set_default( ).
  lo_functions->set_group_export( ).

  lr_factory->zif_git_report_alv_factory_v2~get_data_to_display( CHANGING ct_table_data = lt_output  ). "gt_output ).
  lr_factory->zif_git_report_alv_factory_v2~m_alv_fact->display( ).