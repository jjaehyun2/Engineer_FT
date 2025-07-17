CLASS zcl_git_alvfactgrid_template DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.

    INTERFACES zif_git_report_alv_factory_v2.
    ALIASES: m_alv_obj FOR zif_git_report_alv_factory_v2~m_alv_fact,
             on_user_command FOR zif_git_report_alv_factory_v2~on_added_function.
    TYPES:
      "Define types of screen selection
      BEGIN OF ts_selection,
        sdate TYPE sydate,
*        .
*        .
      END OF ts_selection .

    CLASS-METHODS get_instance
      IMPORTING                                           "....
        !iv_date       TYPE sydate
      RETURNING
        VALUE(ro_temp) TYPE REF TO zcl_git_alvfactgrid_template
      RAISING
        zcx_bc_exception .
    "instance methods
    METHODS constructor             "params ...
      IMPORTING
        !iv_date TYPE sydate
      RAISING
        zcx_bc_exception .
    METHODS run .
  PROTECTED SECTION.
    "output definition
    TYPES: BEGIN OF ty_output,
             disp_log(1) TYPE c,
             ".
             ".
           END OF ty_output.

    DATA: ms_selection TYPE ts_selection,
          output_table TYPE TABLE OF ty_output.
  PRIVATE SECTION.
    METHODS: get_data,
      alv_display,
      alv_settings,
      get_where_cond RETURNING VALUE(rt_where_tab) TYPE rsds_where_tab.
ENDCLASS.



CLASS zcl_git_alvfactgrid_template IMPLEMENTATION.


  METHOD alv_display.
    " pass it_table table as import doesn't allow to use as changing on factory call
    FIELD-SYMBOLS <table> TYPE ANY TABLE.
    ASSIGN zif_git_report_alv_factory_v2~m_output_table->* TO <table>.
    CHECK <table> IS  ASSIGNED.
    TRY.
        cl_salv_table=>factory(
*    EXPORTING
*      list_display   = IF_SALV_C_BOOL_SAP=>FALSE    " ALV Displayed in List Mode
*      r_container    =     " Abstract Container for GUI Controls
*      container_name =
      IMPORTING
        r_salv_table   =    me->m_alv_obj   " Basis Class Simple ALV Tables
          CHANGING
            t_table        = <table>
        ).
      CATCH cx_salv_msg.    "
    ENDTRY.

    "get events
    me->zif_git_report_alv_factory_v2~m_tb_fact_evt = me->m_alv_obj->get_event( ). "table cl_salv_events_table.
    me->zif_git_report_alv_factory_v2~m_alv_fact_evt = me->m_alv_obj->get_event( ). "ALV object cl_salv_events.
    "get selections
    me->zif_git_report_alv_factory_v2~m_selections_alv = me->m_alv_obj->get_selections( ).
    "get functions
    me->zif_git_report_alv_factory_v2~m_functions_alv = me->m_alv_obj->get_functions( ).
    " get sorting
    me->zif_git_report_alv_factory_v2~m_sorts_alv = me->m_alv_obj->get_sorts( ).
    "
    me->zif_git_report_alv_factory_v2~m_display_alv = me->m_alv_obj->get_display_settings( ).
    me->zif_git_report_alv_factory_v2~m_layout_alv = me->m_alv_obj->get_layout( ).

    "EVENTS to register!
    SET HANDLER me->zif_git_report_alv_factory_v2~on_added_function  "on user command
               FOR me->zif_git_report_alv_factory_v2~m_tb_fact_evt.

    SET HANDLER me->zif_git_report_alv_factory_v2~on_after_salv_function
               FOR me->zif_git_report_alv_factory_v2~m_tb_fact_evt.
    SET HANDLER me->zif_git_report_alv_factory_v2~on_before_salv_function
              FOR me->zif_git_report_alv_factory_v2~m_tb_fact_evt.
    SET HANDLER me->zif_git_report_alv_factory_v2~on_end_of_page
              FOR me->zif_git_report_alv_factory_v2~m_tb_fact_evt.
    SET HANDLER me->zif_git_report_alv_factory_v2~on_top_of_page
              FOR me->zif_git_report_alv_factory_v2~m_tb_fact_evt.
    SET HANDLER me->zif_git_report_alv_factory_v2~on_double_click
              FOR me->zif_git_report_alv_factory_v2~m_tb_fact_evt.
    SET HANDLER me->zif_git_report_alv_factory_v2~on_link_click
              FOR me->zif_git_report_alv_factory_v2~m_tb_fact_evt.

    alv_settings( ).
    me->m_alv_obj->display( ).
  ENDMETHOD.


  METHOD alv_settings.
    " work on columns settings
    DATA lr_column  TYPE REF TO cl_salv_column_table.
    DATA(gr_columns) = me->m_alv_obj->get_columns( ).
    TRY.
        gr_columns->set_optimize( if_salv_c_bool_sap=>true ).

        "hide columns MAMDT, ....
        lr_column ?= gr_columns->get_column( 'MANDT' ).
        lr_column->set_visible( abap_false ).
*        lr_column ?= gr_columns->get_column( 'LOG_ID' ).
*        lr_column->set_visible( abap_false ).
*        lr_column ?= gr_columns->get_column( 'CPROG' ).
*        lr_column->set_visible( abap_false ).
*        lr_column ?= gr_columns->get_column( 'UNAME' ).
*        lr_column->set_visible( abap_false ).
*        lr_column ?= gr_columns->get_column( 'TSTAMP_START' ).
*        lr_column->set_visible( abap_false ).

*... §4 set layout / SALV_DEMO_TABLE_LAYOUT
        DATA: lr_layout TYPE REF TO cl_salv_layout,
              ls_key    TYPE salv_s_layout_key.
        "to allow saving of layout output table
        lr_layout = me->m_alv_obj->get_layout( ).
*        ls_key-report = <report_name> .
        lr_layout->set_key( ls_key ).
*... §4.2 set usage of default Layouts
        lr_layout->set_default( 'X' ).

*... §4.3 set Layout save restriction
        " restrict = if_salv_c_layout=>restrict_none.
        " restrict = if_salv_c_layout=>restrict_user_dependant.
        " restrict = if_salv_c_layout=>restrict_user_independant.
        lr_layout->set_save_restriction( if_salv_c_layout=>restrict_none ).

*... §4.4 set initial Layout
*        IF gs_test-load_layo EQ gc_true.
*          lr_layout->set_initial_layout( gs_test-layout ).
*        ENDIF.


*... §3 Functions SALV_DEMO_TABLE_LAYOUT PF-status
*... §3.1 activate ALV generic Functions
*... §3.2 include own functions by setting own status
        me->m_alv_obj->set_screen_status(
          pfstatus      =  'SALV_DEMO' "<report_pf_status>
          report        = 'SALV_DEMO_TABLE_LAYOUT' "  <report_name>
          set_functions = me->m_alv_obj->c_functions_all ).

*        " add button display log
*        lr_column ?= gr_columns->get_column( 'DISP_LOG' ).
**        lr_column->set_cell_type(
**            value = if_salv_c_cell_type=>button
**        ).
*        lr_column->set_icon(
*            value = if_salv_c_bool_sap=>true
*        ).

      CATCH cx_salv_not_found.
        "handle column not found

    ENDTRY.
  ENDMETHOD.


  METHOD constructor.
    "fill screeen elements
    ms_selection-sdate =  iv_date.
*    ms_selection-func_name = iv_func_name.
*    ms_selection-st_date = iv_date_rg.
*    ms_selection-sdate = iv_date.
*    ms_selection-st_time = iv_time_rg.
*    ms_selection-user_name = iv_user_name.
*    ms_selection-vbeln =  iv_vbeln.
  ENDMETHOD.


  METHOD get_data.
    DATA(l_where_cond) = get_where_cond(  ).
*    SELECT * FROM zzbc_log_ks
*    UP TO 5 ROWS "to be define
**    INTO TABLE output_table
*    INTO TABLE @DATA(lt_data)
*    WHERE (l_where_cond).
*    output_table =  CORRESPONDING #( lt_data MAPPING mandt = mandt ).
    GET REFERENCE OF output_table INTO zif_git_report_alv_factory_v2~m_output_table.
  ENDMETHOD.


  METHOD get_instance.
    ro_temp = NEW zcl_git_alvfactgrid_template(
        iv_date      = iv_date
*        iv_time_rg   = iv_time_rg
*        iv_vbeln     = iv_vbeln
*        iv_func_name = iv_func_name
*        iv_user_name =  iv_user_name
    ).
  ENDMETHOD.


  METHOD get_where_cond.
    DATA: lt_field_ranges  TYPE rsds_trange,
          ls_field_ranges  LIKE LINE OF lt_field_ranges,
          ls_range         TYPE rsds_frange,
          lt_where_clauses TYPE rsds_twhere.
    "when parameter
    IF ms_selection-sdate IS NOT INITIAL.
      ls_range-fieldname = 'PDATE'.
*      APPEND VALUE #( sign = 'I' option = 'EQ' low = ms_selection-sdate ) TO ls_range-selopt_t.
      ls_range-selopt_t =  VALUE #( ( sign = 'I' option = 'EQ' low = ms_selection-sdate ) ).
      APPEND ls_range TO ls_field_ranges-frange_t.
    ENDIF.
    "when select option
*    IF ms_selection-st_time IS NOT INITIAL. "select options
*      ls_range-fieldname = 'START_TIME'.
*      ls_range-selopt_t = VALUE #( FOR lw_time IN  ms_selection-st_time
*       ( sign = lw_time-sign option = lw_time-option low = lw_time-low high = lw_time-high ) ).
*      APPEND ls_range TO ls_field_ranges-frange_t.
*    ENDIF.
    "when parameter to have search with *
*    IF ms_selection-vbeln IS NOT INITIAL.
*      ls_range-fieldname = 'CONTEXT'.
**      APPEND VALUE #( sign = 'I' option = 'EQ' low = ms_selection-vbeln ) TO ls_range-selopt_t.
*      "CP contains pattern => LIKE
*      DATA(l_str) = |*{ ms_selection-vbeln }*|.
*      ls_range-selopt_t = VALUE #( ( sign = 'I' option = 'CP' low = l_str ) ).
*      APPEND ls_range TO ls_field_ranges-frange_t.
*    ENDIF.
*    ls_field_ranges-tablename = <table name>.
*    APPEND ls_field_ranges TO lt_field_ranges.
*
*    CALL FUNCTION 'FREE_SELECTIONS_RANGE_2_WHERE'
*      EXPORTING
*        field_ranges  = lt_field_ranges
*      IMPORTING
*        where_clauses = lt_where_clauses.
*
*    IF lt_where_clauses[] IS NOT INITIAL.
*      rt_where_tab = lt_where_clauses[ 1 ]-where_tab.
*    ENDIF.
  ENDMETHOD.


  METHOD run.
    get_data(  ).
    alv_display( ).
  ENDMETHOD.
  METHOD zif_git_report_alv_factory_v2~on_added_function.

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

  ENDMETHOD.

  METHOD zif_git_report_alv_factory_v2~on_link_click.

  ENDMETHOD.

  METHOD zif_git_report_alv_factory_v2~get_data_to_display.

  ENDMETHOD.

ENDCLASS.