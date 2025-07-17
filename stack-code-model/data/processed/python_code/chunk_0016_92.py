class zcl_excel_ole definition
  public
  final
  create public .

*"* public components of class ZCL_EXCEL_OLE
*"* do not include other source files here!!!
  public section.

    types:
      begin of ts_cell,
        row        type i,
        column     type i,
        value(255),
      end of ts_cell .
    types:
      tt_cells type table of ts_cell .

    data r_container type ref to cl_gui_docking_container read-only .
    data r_proxy type ref to i_oi_document_proxy read-only .
    data r_excel type ref to i_oi_spreadsheet read-only .
    data s_handle type cntl_handle read-only .
    data r_application type ole2_object read-only .
    data r_window type ole2_object read-only .
    data r_sheet type ole2_object read-only .
    data data type xstring read-only .

    class-methods create_from_path
      importing
        !i_path         type string
        !i_inplace      type abap_bool default abap_false
      returning
        value(er_excel) type ref to zcl_excel_ole
      raising
        zcx_generic .
    class-methods create_from_mime
      importing
        !i_path         type string
        !i_inplace      type abap_bool default abap_false
      returning
        value(er_excel) type ref to zcl_excel_ole
      raising
        zcx_generic .
    class-methods create_from_data
      importing
        !i_data         type xstring
        !i_inplace      type abap_bool default abap_false
      returning
        value(er_excel) type ref to zcl_excel_ole
      raising
        zcx_generic .
    methods constructor
      importing
        !i_path    type string optional
        !i_mime    type string optional
        !i_data    type xstring optional
        !i_inplace type abap_bool optional
      raising
        zcx_generic .
    methods select_sheet
      importing
        !i_sheet type c
        !i_flush type abap_bool default abap_false
      raising
        zcx_generic .
    methods get_value
      importing
        !i_column      type i default 1
        !i_row         type i default 1
        !i_flush       type abap_bool default abap_false
          preferred parameter i_column
      returning
        value(e_value) type string
      raising
        zcx_generic .
    methods set_value
      importing
        !i_name   type string optional
        !i_column type i optional
        !i_row    type i optional
        !i_value  type data
        !i_flush  type abap_bool default abap_false
      raising
        zcx_generic .
    methods replace
      importing
        !i_column  type i optional
        !i_row     type i optional
        !i_pattern type simple
        !i_with    type simple
        !i_flush   type abap_bool default abap_false
      raising
        zcx_generic .
    methods get_range
      importing
        !i_column      type i default 1
        !i_columns     type i default 26
        !i_row         type i default 1
        !i_rows        type i default 999999
        !i_package     type i default 1000
      exporting
        value(et_data) type tt_cells
      raising
        zcx_generic .
    methods insert_rows
      importing
        !i_row   type i
        !i_rows  type i
        !i_flush type abap_bool default abap_false
      raising
        zcx_generic .
    methods delete_rows
      importing
        !i_row   type i
        !i_rows  type i default 1
        !i_flush type abap_bool default abap_false
      raising
        zcx_generic .
    methods copy_rows
      importing
        !i_row   type i
        !i_rows  type i default 1
        !i_to    type i optional
        !i_times type i default 1
        !i_flush type abap_bool default abap_false
      raising
        zcx_generic .
    methods insert_table
      importing
        !i_column type i default 1
        !i_row    type i default 1
        !it_data  type table
        !i_flush  type abap_bool default abap_false
      raising
        zcx_generic .
    methods set_focus
      importing
        !i_row    type i default 1
        !i_column type i default 1
        !i_flush  type abap_bool default abap_false
      raising
        zcx_generic .
    methods maximize
      importing
        !i_flush type abap_bool default abap_false
      raising
        zcx_generic .
    methods hide
      importing
        !i_flush type abap_bool default abap_false
      raising
        zcx_generic .
    methods show
      importing
        !i_flush type abap_bool default abap_false
      raising
        zcx_generic .
    methods close
      raising
        zcx_generic .
    methods flush
      raising
        zcx_generic .
  protected section.
*"* protected components of class ZATMCL_BNF_EXCEL
*"* do not include other source files here!!!
  private section.
*"* private components of class ZCL_EXCEL_OLE
*"* do not include other source files here!!!

    data r_cell type ole2_object .
    data r_rows type ole2_object .
ENDCLASS.



CLASS ZCL_EXCEL_OLE IMPLEMENTATION.


  method close.

    data lr_error type ref to i_oi_error.
    r_proxy->close_document(
      importing
          error = lr_error ).
    if lr_error->error_code ne c_oi_errors=>ret_ok.
      zcx_generic=>raise( ir_oi_error = lr_error ).
    endif.

    try.
        if r_container is bound.
          r_container->free( ).
        endif.
      catch cx_root.
    endtry.

  endmethod.


  method constructor.

    if i_path is supplied.
      data = zcl_file_static=>read( i_path ).
    elseif i_mime is supplied.
      data = zcl_mime_static=>read( i_mime ).
    elseif i_data is supplied.
      data = i_data.
    else.
      assert 1 = 2.
    endif.

    " Ïîëó÷àåì ActiveX Control
    data lr_control type ref to i_oi_container_control.
    data lr_error type ref to i_oi_error.
    c_oi_container_control_creator=>get_container_control(
      importing
        control = lr_control
        error   = lr_error ).
    if lr_error->error_code ne c_oi_errors=>ret_ok.
      zcx_generic=>raise( ir_oi_error = lr_error ).
    endif.

    if i_inplace eq abap_true.

      " Ñîçäàåì ôåéê êîíòåéíåð
      create object r_container
        exporting
          side      = cl_gui_docking_container=>dock_at_bottom
          extension = 0.

      r_container->set_visible( abap_false ).

    endif.

    " Èíèöèàëèçèðóåì êîíòðîë â íàøåì êîíòåéíåðå
    lr_control->init_control(
      exporting
        r3_application_name = ' '
        inplace_enabled     = i_inplace
        parent              = r_container
        no_flush            = abap_true
      importing
        error               = lr_error ).
    if lr_error->error_code ne c_oi_errors=>ret_ok.
      zcx_generic=>raise( ir_oi_error = lr_error ).
    endif.

    " Óêàçûâàåì êàêîé äîêóìåíò áóäåì îòêðûâàòü
    lr_control->get_document_proxy(
      exporting
        document_type  = soi_doctype_excel_sheet
        no_flush       = abap_true
      importing
        document_proxy = r_proxy
        error          = lr_error ).
    if lr_error->error_code ne c_oi_errors=>ret_ok.
      zcx_generic=>raise( ir_oi_error = lr_error ).
    endif.

    data l_size type i.
    l_size = xstrlen( data ).

    data lt_data type tsfixml.
    zcl_convert_static=>xtext2xtable(
      exporting i_data  = data
      importing et_data = lt_data ).

    " Îòêðûâàåì äîêóìåíò
    r_proxy->open_document_from_table(
      exporting
        document_size  = l_size
        document_table = lt_data
        open_inplace   = i_inplace
        open_readonly  = abap_false
        no_flush       = abap_true
      importing
        error          = lr_error ).
    if lr_error->error_code ne c_oi_errors=>ret_ok.
      zcx_generic=>raise( ir_oi_error = lr_error ).
    endif.

    " Ïîëó÷àåì èíòåðôåéñ äëÿ ðàáîòû ñ äîêóìåíòîì
    r_proxy->get_spreadsheet_interface(
      exporting
        no_flush        = abap_true
      importing
        sheet_interface = r_excel
        error           = lr_error ).
    if lr_error->error_code ne c_oi_errors=>ret_ok.
      zcx_generic=>raise( ir_oi_error = lr_error ).
    endif.

    r_proxy->get_document_handle(
      exporting
        no_flush = abap_true
      importing
        handle   = s_handle
        error    = lr_error ).
    if lr_error->error_code ne c_oi_errors=>ret_ok.
      zcx_generic=>raise( ir_oi_error = lr_error ).
    endif.

    get property of s_handle-obj 'Application' = r_application no flush.

    get property of r_application 'ActiveWindow' = r_window no flush.

    get property of r_application 'ActiveSheet' = r_sheet no flush.

    hide( ).

    flush( ).

  endmethod.


  method copy_rows.

* r_rows("21:21").Select
* Selection.Copy

    data l_row1(5).
    l_row1 = i_row.
    condense l_row1.

    data l_row2(5).
    l_row2 = i_row + i_rows - 1.
    condense l_row2.

    data l_range(11).
    concatenate l_row1 ':' l_row2 into l_range.

    call method of r_sheet 'Rows' = r_rows                  "#EC NOTEXT
      exporting
        #1 = l_range.
    check sy-subrc eq 0.

    call method of r_rows 'Select' no flush. "#EC NOTEXT
    check sy-subrc eq 0.

    call method of r_rows 'Copy' no flush. "#EC NOTEXT
    check sy-subrc eq 0.

    data l_to type i.
    l_to = i_to.
    if l_to is initial.
      l_to = i_row + i_rows.
    endif.

* r_rows("22:39").Select
* Active r_sheet.Paste
    if i_rows eq 1.

      l_row1 = l_to.
      condense l_row1.

      l_row2 = l_to + i_times - 1.
      condense l_row2.

      concatenate l_row1 ':' l_row2 into l_range.

      call method of r_sheet 'Rows' = r_rows                "#EC NOTEXT
        exporting
          #1 = l_range.
      check sy-subrc eq 0.

      call method of r_rows 'Select' no flush. "#EC NOTEXT
      check sy-subrc eq 0.

      call method of r_sheet 'Paste' no flush. "#EC NOTEXT
      check sy-subrc eq 0.

    else.

      do i_times times.

        l_row1 = l_to + ( i_rows * ( sy-index - 1 ) ).
        condense l_row1.

        l_row2 = l_row1.
        condense l_row2.

        concatenate l_row1 ':' l_row2 into l_range.

        call method of r_sheet 'Rows' = r_rows              "#EC NOTEXT
          exporting
            #1 = l_range.
        check sy-subrc eq 0.

        call method of r_rows 'Select' no flush. "#EC NOTEXT
        check sy-subrc eq 0.

        call method of r_sheet 'Paste' no flush. "#EC NOTEXT
        check sy-subrc eq 0.

      enddo.

    endif.

    data lr_cell type ole2_object.
    call method of r_sheet 'Cells' = lr_cell                "#EC NOTEXT
      exporting
        #1 = 1
        #2 = 1.
    check sy-subrc eq 0.

    call method of lr_cell 'Select' no flush. "#EC NOTEXT
    check sy-subrc eq 0.

    set property of r_application 'CutCopyMode' = 'False' no flush. "#EC NOTEXT
    check sy-subrc eq 0.

    if i_flush eq abap_true.
      flush( ).
    endif.

  endmethod.


  method create_from_data.

    create object er_excel
      exporting
        i_data    = i_data
        i_inplace = i_inplace.

  endmethod.


  method create_from_mime.

    create object er_excel
      exporting
        i_mime    = i_path
        i_inplace = i_inplace.

  endmethod.


  method create_from_path.

    create object er_excel
      exporting
        i_path    = i_path
        i_inplace = i_inplace.

  endmethod.


  method delete_rows.

    data l_row1(5).
    l_row1 = i_row.
    condense l_row1.

    data l_row2(5).
    l_row2 = i_row - 1 + i_rows.
    condense l_row2.

    data l_range(11).
    concatenate l_row1 ':' l_row2 into l_range.

    call method of r_sheet 'Rows' = r_rows no flush
      exporting
        #1 = l_range.
    check sy-subrc eq 0.

    call method of r_rows 'Delete' no flush.
    check sy-subrc eq 0.

    if i_flush eq abap_true.
      flush( ).
    endif.

  endmethod.


  method flush.

    zcl_abap_static=>flush( ).

  endmethod.


  method get_range.

    do.

      data l_from type i.
      l_from = sy-index * i_package - i_package + i_row.

      data ls_range type soi_dimension_item.
      ls_range-row     = l_from.
      ls_range-rows    = i_package.
      ls_range-column  = i_column.
      ls_range-columns = i_columns.

      data lt_range type soi_dimension_table.
      clear lt_range.
      insert ls_range into table lt_range.

      data lr_error type ref to i_oi_error.
      data lt_ranges type soi_range_list.
      data lt_data type soi_generic_table.
      clear lt_data.
      r_excel->get_ranges_data(
        exporting
          rangesdef = lt_range
        importing
          contents  = lt_data
          error     = lr_error
        changing
          ranges    = lt_ranges ).
      if lr_error->error_code ne c_oi_errors=>ret_ok.
        zcx_generic=>raise( ir_oi_error = lr_error ).
      endif.

      delete lt_data where value is initial.

      if lt_data is initial.
        return.
      endif.

      data ls_data like line of lt_data.
      loop at lt_data into ls_data.

        field-symbols <ls_data> like line of et_data.
        append initial line to et_data assigning <ls_data>.

        move-corresponding ls_data to <ls_data>.

        <ls_data>-row = <ls_data>-row + l_from - 1.

      endloop.

    enddo.

  endmethod.


  method get_value.

    call method of r_sheet 'Cells' = r_cell no flush
      exporting
        #1 = i_row
        #2 = i_column.
    check sy-subrc eq 0.

    get property of r_cell 'Value' = e_value no flush.
    check sy-subrc eq 0.

***  data ls_range type soi_dimension_item.
***  ls_range-row     = i_row.
***  ls_range-rows    = i_row.
***  ls_range-column  = i_column.
***  ls_range-columns = i_column.
***
***  data lt_range type soi_dimension_table.
***  insert ls_range into table lt_range.
***
***  data lr_error type ref to i_oi_error.
***  data lt_ranges type soi_range_list.
***  data lt_content type soi_generic_table.
***  r_excel->get_ranges_data(
***    exporting
***      rangesdef = lt_range
***    importing
***      contents  = lt_content
***      error     = lr_error
***    changing
***      ranges    = lt_ranges ).
***  if lr_error->error_code ne c_oi_errors=>ret_ok.
***    zcx_generic=>raise( ir_oi_error = lr_error ).
***  endif.
***
***  data ls_content like line of lt_content.
***  read table lt_content into ls_content index 1.
***  if sy-subrc eq 0.
***    e_value = ls_content-value.
***  endif.

    if i_flush eq abap_true.
      flush( ).
    endif.

  endmethod.


  method hide.

    if r_container is bound.

      r_container->set_visible( abap_false ).

    else.

      set property of r_application 'Visible' = 0 no flush.
      check sy-subrc eq 0.

      if i_flush eq abap_true.
        flush( ).
      endif.

    endif.

  endmethod.


  method insert_rows.

    data l_row1(5).
    l_row1 = i_row.
    condense l_row1.

    data l_row2(5).
    l_row2 = i_row.
    condense l_row2.

    data l_range(11).
    concatenate l_row1 ':' l_row2 into l_range.

    call method of r_sheet 'Rows' = r_rows
      exporting
        #1 = l_range.
    check sy-subrc eq 0.

    call method of r_rows 'Select' no flush.
    check sy-subrc eq 0.

    do i_rows times.
      call method of r_rows 'Insert' no flush.
      check sy-subrc eq 0.
    enddo.

    if i_flush eq abap_true.
      flush( ).
    endif.

  endmethod.


  method insert_table.

    data lr_data type ref to data.
    create data lr_data like it_data.

    field-symbols <lt_data> type standard table.
    assign lr_data->* to <lt_data>.

    data lt_fields type soi_fields_table.
    call function 'DP_GET_FIELDS_FROM_TABLE'
      tables
        data   = it_data
        fields = lt_fields.

    data l_rows type i value 1000.

    do 100 times.

      data l_index type i.
      l_index = sy-index.

      data l_row like i_row.
      l_row = i_row + ( sy-index - 1 ) * l_rows.

      data l_from type i.
      l_from = l_rows * sy-index - l_rows + 1.

      data l_to type i.
      l_to = l_rows * sy-index.

      clear <lt_data>.
      field-symbols <is_data> type any.
      loop at it_data assigning <is_data> from l_from  to l_to.
        field-symbols <ls_data> type any.
        append initial line to <lt_data> assigning <ls_data>.
        <ls_data> = <is_data>.
      endloop.
      if sy-subrc ne 0.
        exit.
      endif.

      data l_range type guid_32.
      l_range = 'Table'.                                    "#EC NOTEXT
      write l_index to l_range+5 left-justified.

      data lt_ranges type soi_range_list.
      data ls_range like line of lt_ranges.
      ls_range-name = l_range.
      insert ls_range into table lt_ranges.

      data lr_error type ref to i_oi_error.
      r_excel->insert_range_dim(
        exporting
          name     = l_range
          top      = l_row
          left     = i_column
          rows     = 1
          columns  = 1
          "no_flush = abap_true
        importing
          error    = lr_error ).
      if lr_error->error_code ne c_oi_errors=>ret_ok.
        zcx_generic=>raise( ir_oi_error = lr_error ).
      endif.

      r_excel->insert_one_table(
        exporting
          data_table   = <lt_data>
          fields_table = lt_fields
          rangename    = l_range
          wholetable   = abap_true
          "no_flush     = abap_true
        importing
          error        = lr_error ).
      if lr_error->error_code ne c_oi_errors=>ret_ok.
        zcx_generic=>raise( ir_oi_error = lr_error ).
      endif.

    enddo.

    if lt_ranges is not initial.
      r_excel->delete_ranges(
        exporting
          ranges   = lt_ranges
          "no_flush = abap_false
        importing
          error    = lr_error ).
      if lr_error->error_code ne c_oi_errors=>ret_ok.
        zcx_generic=>raise( ir_oi_error = lr_error ).
      endif.
    endif.

    if i_flush eq abap_true.
      flush( ).
    endif.

  endmethod.


  method maximize.

    set property of r_application 'WindowState' = zcl_excel_static=>xl_maximized no flush.
    check sy-subrc eq 0.

    set property of r_window 'WindowState' = zcl_excel_static=>xl_maximized no flush.
    check sy-subrc eq 0.

    if i_flush eq abap_true.
      flush( ).
    endif.

  endmethod.


  method replace.

    if i_column is initial and
       i_row    is initial.

      call method of r_application 'CELLS' = r_cell no flush.
      check sy-subrc eq 0.

      call method of r_cell 'Replace' no flush
        exporting
          #1 = i_pattern
          #2 = i_with.
      check sy-subrc eq 0.

    else.

      data l_value(255).
      l_value =
        get_value(
          i_column = i_column
          i_row    = i_row
          i_flush  = abap_true ).

      replace i_pattern in l_value with i_with.

      set_value(
        i_column = i_column
        i_row    = i_row
        i_value  = l_value ).

    endif.

    if i_flush eq abap_true.
      flush( ).
    endif.

  endmethod.


  method select_sheet.

    data lr_error type ref to i_oi_error.
    r_excel->select_sheet(
      exporting
        name     = i_sheet
        no_flush = abap_true
      importing
        error    = lr_error ).
    if lr_error->error_code ne c_oi_errors=>ret_ok.
      zcx_generic=>raise( ir_oi_error = lr_error ).
    endif.

    if i_flush eq abap_true.
      flush( ).
    endif.

  endmethod.


  method set_focus.

    call method of r_sheet 'Cells' = r_cell no flush
      exporting
        #1 = i_row
        #2 = i_column.
    check sy-subrc eq 0.

    call method of r_cell 'Select' no flush.
    check sy-subrc eq 0.

    if i_flush eq abap_true.
      flush( ).
    endif.

  endmethod.


  method set_value.

    if i_name is initial.

      call method of r_sheet 'Cells' = r_cell no flush
        exporting
          #1 = i_row
          #2 = i_column.
      check sy-subrc eq 0.

      set property of r_cell 'Value' = i_value no flush.
      check sy-subrc eq 0.

***    data ls_rangedef type soi_dimension_item.
***    ls_rangedef-row     = i_row.
***    ls_rangedef-column  = i_column.
***    ls_rangedef-rows    = 1.
***    ls_rangedef-columns = 1.
***
      data lt_rangesdef type soi_dimension_table.
***    insert ls_rangedef into table lt_rangesdef.

    else.

      data ls_range type soi_range_item.
      ls_range-name       = i_name.
      ls_range-rows       = 1.
      ls_range-columns    = 1.

      data lt_ranges type soi_range_list.
      insert ls_range into table lt_ranges.

    endif.

    if lt_ranges is not initial or
       lt_rangesdef is not initial.

      data ls_content type soi_generic_item.
      ls_content-row      = 1.
      ls_content-column   = 1.
      ls_content-value    = i_value.

      data lt_content type soi_generic_table.
      insert ls_content into table lt_content.

      data lr_error type ref to i_oi_error.
      r_excel->set_ranges_data(
        exporting
          ranges    = lt_ranges
          contents  = lt_content
          rangesdef = lt_rangesdef
          "no_flush  = abap_true
        importing
          error     = lr_error ).
      if lr_error->error_code ne c_oi_errors=>ret_ok.
        zcx_generic=>raise( ir_oi_error = lr_error ).
      endif.

    endif.

    if i_flush eq abap_true.
      flush( ).
    endif.

  endmethod.


  method show.

    if r_container is bound.

      r_container->set_visible( abap_true ).

    else.

      set property of r_application 'Visible' = 1 no flush.
      check sy-subrc eq 0.

      if i_flush eq abap_true.
        flush( ).
      endif.

    endif.

  endmethod.
ENDCLASS.