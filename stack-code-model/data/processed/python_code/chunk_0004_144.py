class ZCL_ALV_TABLE definition
  public
  final
  create public .

*"* public components of class ZCL_ALV_TABLE
*"* do not include other source files here!!!
public section.

  data R_CONTAINER type ref to CL_GUI_CONTAINER read-only .
  data R_TABLE type ref to CL_GUI_ALV_GRID read-only .
  data R_DATA type ref to DATA read-only .

  events HOTSPOT_CLICK
    exporting
      value(I_COLUMN) type STRING
      value(I_ROW) type I .
  events DOUBLE_CLICK
    exporting
      value(I_COLUMN) type STRING
      value(I_ROW) type I .
  events TOOLBAR_DEFINE
    exporting
      value(IR_TOOLBAR) type ref to CL_ALV_EVENT_TOOLBAR_SET .
  events USER_COMMAND
    exporting
      value(I_ACTION) type SIMPLE .

  class-methods CREATE
    importing
      !IR_PARENT type ref to CL_GUI_CONTAINER optional
      !I_PARENT type C default 'C_TABLE'
      value(I_REPID) type SIMPLE default SY-REPID
      !I_TCODE type SIMPLE optional
      !I_ZEBRA type ABAP_BOOL default ABAP_TRUE
      !IT_DATA type TABLE
      !I_HIDE_TECH type ABAP_BOOL default ABAP_TRUE
      !I_HANDLE type SLIS_HANDL optional
      !IT_FIELDCATALOG type LVC_T_FCAT optional
    returning
      value(ER_TABLE) type ref to ZCL_ALV_TABLE
    raising
      ZCX_GENERIC .
  class-methods DISPLAY
    importing
      !IT_DATA type TABLE
    returning
      value(ER_TABLE) type ref to ZCL_ALV_TABLE
    raising
      ZCX_GENERIC .
  methods CONSTRUCTOR
    importing
      !IR_PARENT type ref to CL_GUI_CONTAINER optional
      !I_PARENT type C optional
      !I_REPID type SIMPLE optional
      !I_TCODE type SIMPLE optional
      !I_ZEBRA type ABAP_BOOL optional
      !IT_DATA type TABLE
      !I_HIDE_TECH type ABAP_BOOL default ABAP_TRUE
      !I_HANDLE type SLIS_HANDL optional
      !IT_FIELDCATALOG type LVC_T_FCAT optional
    raising
      ZCX_GENERIC .
  methods REFRESH
    importing
      !I_STABLE type ABAP_BOOL default ABAP_TRUE
      !IT_DATA type TABLE optional
    preferred parameter I_STABLE .
  methods GET_LAYOUT
    returning
      value(ES_LAYOUT) type LVC_S_LAYO .
  methods SET_LAYOUT
    importing
      !IS_LAYOUT type LVC_S_LAYO .
  methods HIDE_TOOLBAR .
  methods HIDE_COLUMNS .
  methods HIDE_COLUMN
    importing
      !I_NAME type DATA
    raising
      ZCX_GENERIC .
  methods SHOW_COLUMN
    importing
      !I_NAME type DATA
    raising
      ZCX_GENERIC .
  methods SET_COLUMN
    importing
      !I_NAME type DATA
      !I_KEY type ABAP_BOOL default ABAP_FALSE
      !I_POS type I optional
      !I_HIDE type ABAP_BOOL default ABAP_FALSE
      !I_HOTSPOT type ABAP_BOOL default ABAP_FALSE
      !I_EDIT type ABAP_BOOL default ABAP_FALSE
      !I_ICON type ABAP_BOOL default ABAP_FALSE
      !I_JUST type C optional
      !I_SUM type ABAP_BOOL default ABAP_FALSE
      !I_TECH type ABAP_BOOL default ABAP_FALSE
      !I_SILENT type ABAP_BOOL default ABAP_TRUE
      !I_TEXT type SIMPLE optional
    raising
      ZCX_GENERIC .
  methods SET_EDIT_MODE .
  methods SET_DISPLAY_MODE .
  methods SET_ROW_COLOR
    importing
      !I_FIELDNAME type SIMPLE default 'ROW_COLOR' .
  methods SET_CELLS_COLOR
    importing
      !I_FIELDNAME type SIMPLE default 'CELLS_COLOR' .
  methods SET_CELLS_STYLE
    importing
      !I_FIELDNAME type SIMPLE default 'CELLS_STYLE' .
  methods OPTIMIZE_COLUMS .
  methods GET_DATA
    exporting
      !ET_DATA type TABLE .
  methods GET_SELECTED
    exporting
      !ET_DATA type TABLE .
  methods GET_ROW
    importing
      !I_ROW type I
    exporting
      value(ES_DATA) type DATA .
  methods SET_ROW
    importing
      !I_ROW type I
      !IS_DATA type DATA .
  methods CLOSE .
protected section.
  private section.
*"* private components of class ZCL_ALV_TABLE
*"* do not include other source files here!!!

    methods on_hotspot_click
          for event hotspot_click of cl_gui_alv_grid
      importing
          !e_row_id
          !e_column_id
          !es_row_no .
    methods on_double_click
          for event double_click of cl_gui_alv_grid
      importing
          !e_row
          !e_column
          !es_row_no .
    methods on_button_click
        for event button_click of cl_gui_alv_grid .
    methods on_toolbar_define
          for event toolbar of cl_gui_alv_grid
      importing
          !e_object
          !e_interactive .
    methods on_user_command
          for event user_command of cl_gui_alv_grid
      importing
          !e_ucomm .
ENDCLASS.



CLASS ZCL_ALV_TABLE IMPLEMENTATION.


  method close.

    r_table->free( ).
    r_container->free( ).

  endmethod.


  method constructor.

    if ir_parent is bound.
      r_container = ir_parent.
    else.
      data lr_container type ref to cl_gui_custom_container.
      create object lr_container
        exporting
          container_name = i_parent.
      r_container ?= lr_container.
    endif.

    create object r_table
      exporting
        i_parent = r_container.

    create data r_data like it_data.

    field-symbols <lt_data> type any table.
    assign r_data->* to <lt_data>.

    <lt_data> = it_data.

    data lr_struc type ref to data.
    create data lr_struc like line of <lt_data>.

    data lr_descr type ref to cl_abap_structdescr.
    lr_descr ?= cl_abap_structdescr=>describe_by_data_ref( lr_struc ).

    data lt_fieldcatalog like it_fieldcatalog.
    lt_fieldcatalog = it_fieldcatalog.

    data l_struc type tabname.
    if lt_fieldcatalog is initial.
      l_struc = lr_descr->absolute_name+6.
    endif.

    if i_tcode is initial.
      data ls_vrnt type disvariant.
      ls_vrnt-report = i_repid.
    else.
      concatenate i_repid '/' i_tcode into ls_vrnt-report.
    endif.

    ls_vrnt-handle = i_handle.

    data ls_layo type lvc_s_layo.
    ls_layo-zebra      = i_zebra.
    ls_layo-cwidth_opt = abap_true.
    ls_layo-sel_mode   = 'A'.


    r_table->set_table_for_first_display(
      exporting
        i_structure_name              = l_struc
        is_variant                    = ls_vrnt
        is_layout                     = ls_layo
        i_save                        = 'A'
        i_bypassing_buffer            = abap_true
      changing
        it_outtab                     = <lt_data>
        it_fieldcatalog               = lt_fieldcatalog
      exceptions
        others                        = 1 ).
    if sy-subrc ne 0.
      zcx_generic=>raise( ).
    endif.

    data lt_fcat type lvc_t_fcat.
    r_table->get_frontend_fieldcatalog(
      importing et_fieldcatalog  = lt_fcat ).

    field-symbols <ls_fcat> like line of lt_fcat.
    loop at lt_fcat assigning <ls_fcat>.
      if i_hide_tech eq abap_true. " 04.12.2012 13:51:46 vvpikalov: ×òîáû áûëî
        if <ls_fcat>-fieldname cs 'GUID' or
           <ls_fcat>-fieldname cs 'TECH' or
           <ls_fcat>-fieldname cs 'COLOR'.
          <ls_fcat>-tech = abap_true.
        endif.
      endif.

      if <ls_fcat>-fieldname cs 'ICON'.
        <ls_fcat>-icon = abap_true.
      endif.

***    if <ls_fcat>-datatype eq 'CURR' or
***       <ls_fcat>-datatype eq 'QUAN'.
***      <ls_fcat>-emphasize = 'C300'.
***    endif.

    endloop.

    r_table->set_frontend_fieldcatalog( exporting it_fieldcatalog  = lt_fcat ).

    set handler on_hotspot_click  for r_table.
    set handler on_double_click   for r_table.
    set handler on_button_click   for r_table.
    set handler on_toolbar_define for r_table.
    set handler on_user_command   for r_table.


    refresh( ).

  endmethod.


  method create.

    create object er_table
      exporting
        ir_parent       = ir_parent
        i_parent        = i_parent
        i_repid         = i_repid
        i_tcode         = i_tcode
        i_zebra         = i_zebra
        i_hide_tech     = i_hide_tech
        i_handle        = i_handle " 26.02.2013 17:15:35 vvpikalov: Îäèí ALV äëÿ íåñêîëüêèõ ðàçíûõ ñòðóêòóð â îäíîé ïðîãðàììå
        it_fieldcatalog = it_fieldcatalog
        it_data         = it_data.

  endmethod.


  method display.

    create object er_table
      exporting
        ir_parent = cl_gui_container=>screen0
        it_data   = it_data.

    er_table->optimize_colums( ).

    er_table->refresh( ).

    write 1.

  endmethod.


  method get_data.

    field-symbols <lt_data> type standard table.
    assign r_data->* to <lt_data>.

    field-symbols <ls_data> type any.
    loop at <lt_data> assigning <ls_data>.

      field-symbols <es_data> type any.
      append initial line to et_data assigning <es_data>.

      move-corresponding <ls_data> to <es_data>.

    endloop.

  endmethod.


  method get_layout.

    r_table->get_frontend_layout( importing es_layout = es_layout ).

  endmethod.


  method get_row.

    field-symbols <lt_data> type standard table.
    assign r_data->* to <lt_data>.

    field-symbols <ls_data> type any.
    read table <lt_data> assigning <ls_data> index i_row.
    if sy-subrc eq 0.
      move-corresponding <ls_data> to es_data.
    endif.

  endmethod.


  method get_selected.

    data lt_rows type lvc_t_row.
    r_table->get_selected_rows( importing et_index_rows = lt_rows ).

    delete lt_rows where rowtype is not initial.

    if lt_rows is initial.
      return.
    endif.

    field-symbols <lt_data> type standard table.
    assign r_data->* to <lt_data>.

    data ls_row like line of lt_rows.
    loop at lt_rows into ls_row.

      field-symbols <ls_data> type any.
      read table <lt_data> assigning <ls_data> index ls_row-index.
      assert sy-subrc eq 0.

      field-symbols <es_data> type any.
      append initial line to et_data assigning <es_data>.

      move-corresponding <ls_data> to <es_data>.

    endloop.

  endmethod.


  method hide_column.

    set_column(
      i_name = i_name
      i_hide = abap_true ).

  endmethod.


  method hide_columns.

    data lt_fcat type lvc_t_fcat.
    r_table->get_frontend_fieldcatalog(
      importing et_fieldcatalog  = lt_fcat ).

    field-symbols <ls_fcat> like line of lt_fcat.
    loop at lt_fcat assigning <ls_fcat>.
      <ls_fcat>-no_out = abap_true.
    endloop.

    r_table->set_frontend_fieldcatalog(
      exporting it_fieldcatalog  = lt_fcat ).

  endmethod.


  method hide_toolbar.

***
***
***  data ls_tlbe like line of et_tlbe.
***
***  clear et_tlbe.
***
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_detail.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_refresh.
****  append ls_tlbe to et_tlbe.
***
***
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_sort.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_sort_asc.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_sort_dsc.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_find.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_filter.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_mb_sum.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_mb_subtot.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_mb_variant.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_mb_export.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_mb_view.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_print.
****  append ls_tlbe to et_tlbe.
***
***
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_graph.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_info.
****  append ls_tlbe to et_tlbe.
***
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_loc_append_row.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_loc_delete_row.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_loc_insert_row.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_loc_cut.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_loc_copy.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_loc_copy_row.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_loc_paste.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_loc_paste_new_row.
****  append ls_tlbe to et_tlbe.
****
****  ls_tlbe = cl_gui_alv_grid=>mc_fc_loc_undo.
****  append ls_tlbe to et_tlbe.


  endmethod.


  method on_button_click.

  endmethod.


  method on_double_click.

    data l_column type string.
    l_column = e_column-fieldname.

    data l_row type i.
    l_row = e_row-index.

    raise event double_click
      exporting
        i_column = l_column
        i_row    = l_row.

  endmethod.


  method on_hotspot_click.

    data l_column type string.
    l_column = e_column_id-fieldname.

    data l_row type i.
    l_row = e_row_id-index.

    raise event hotspot_click
      exporting
        i_column = l_column
        i_row    = l_row.

  endmethod.


  method on_toolbar_define.

    raise event toolbar_define
      exporting ir_toolbar = e_object.

  endmethod.


  method on_user_command.

    raise event user_command
      exporting
        i_action = e_ucomm.

  endmethod.


  method optimize_colums.

    data ls_layout type lvc_s_layo.
    ls_layout = get_layout( ).

    ls_layout-cwidth_opt = abap_true.

    set_layout( ls_layout ).

  endmethod.


  method refresh.

    if it_data is supplied.
      field-symbols <lt_data> type any table.
      assign r_data->* to <lt_data>.
      <lt_data> = it_data.
    endif.

    if i_stable eq abap_true.
      data ls_stab type lvc_s_stbl.
      ls_stab = 'XX'.
    endif.

    r_table->refresh_table_display( is_stable = ls_stab ).

  endmethod.


  method set_cells_color.

    data ls_layout type lvc_s_layo.
    ls_layout = get_layout( ).

    ls_layout-ctab_fname = i_fieldname.

    set_layout( ls_layout ).

  endmethod.


  method set_cells_style.

    data ls_layout type lvc_s_layo.
    ls_layout = get_layout( ).

    ls_layout-stylefname = i_fieldname.

    set_layout( ls_layout ).

  endmethod.


  method set_column.

    data lt_fcat type lvc_t_fcat.
    r_table->get_frontend_fieldcatalog(
      importing et_fieldcatalog  = lt_fcat ).

    field-symbols <ls_fcat> like line of lt_fcat.
    read table lt_fcat assigning <ls_fcat>
      with key fieldname = i_name.
    if sy-subrc ne 0.
      return.
    endif.

    if i_key is supplied.
      <ls_fcat>-key = i_key.
    endif.

    if i_pos is supplied.
      <ls_fcat>-col_pos = i_pos.
    endif.

    if i_hide is supplied.
      <ls_fcat>-no_out = i_hide.
    endif.

    if i_hotspot is supplied.
      <ls_fcat>-hotspot = i_hotspot.
    endif.

    if i_edit is supplied.
      <ls_fcat>-edit = i_edit.
    endif.

    if i_icon is supplied.
      <ls_fcat>-icon = i_icon.
    endif.

    if i_just is supplied.
      <ls_fcat>-just = i_just.
    endif.

    if i_sum is supplied.
      <ls_fcat>-do_sum = i_sum.
    endif.

    if i_tech is supplied.
      <ls_fcat>-tech = i_tech.
    endif.

    if i_text is supplied.
      <ls_fcat>-coltext = i_text.
      <ls_fcat>-tooltip = i_text.
    endif.

    r_table->set_frontend_fieldcatalog(
      exporting it_fieldcatalog  = lt_fcat ).

  endmethod.


  method set_display_mode.

    r_table->set_ready_for_input( 0 ).

  endmethod.


  method set_edit_mode.

    " Ðåãèñòðàöèÿ ñîáûòèÿ íà èçìåíåíèå äàííûõ
    r_table->register_edit_event( cl_gui_alv_grid=>mc_evt_modified ).

    " Ðåãèñòðàöèÿ ñîáûòèÿ íà íàæàòèå ENTER
    r_table->register_edit_event( cl_gui_alv_grid=>mc_evt_enter ).

    r_table->set_ready_for_input( 1 ).

  endmethod.


  method set_layout.

    r_table->set_frontend_layout( is_layout ).

  endmethod.


  method set_row.

    field-symbols <lt_data> type standard table.
    assign r_data->* to <lt_data>.

    field-symbols <ls_data> type any.
    read table <lt_data> assigning <ls_data> index i_row.
    if sy-subrc eq 0.
      move-corresponding is_data to <ls_data>.
    endif.

  endmethod.


  method set_row_color.

    data ls_layout type lvc_s_layo.
    ls_layout = get_layout( ).

    ls_layout-info_fname = i_fieldname.

    set_layout( ls_layout ).

  endmethod.


  method show_column.

    set_column(
      i_name = i_name
      i_hide = abap_false ).

  endmethod.
ENDCLASS.