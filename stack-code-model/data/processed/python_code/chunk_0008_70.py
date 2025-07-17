class ZCL_FLIFM_EXCEL definition
  public
  final
  create public .

public section.

  interfaces ZIF_FLIFM_EXCEL .

  aliases DOWNLOAD_FSV_LIST_EXCEL
    for ZIF_FLIFM_EXCEL~DOWNLOAD_FSV_LIST_EXCEL .
  PROTECTED SECTION.
private section.

  data MO_EXCEL type OLE2_OBJECT .
  data MO_WORKBOOKS type OLE2_OBJECT .
  data MO_WORKBOOK type OLE2_OBJECT .
  data MO_WORKSHEETS type OLE2_OBJECT .
  data MO_SHEET type OLE2_OBJECT .
  data MO_CELLS type OLE2_OBJECT .
  data MO_TO_CELLS type OLE2_OBJECT .
  data MO_FONT type OLE2_OBJECT .
  data MO_INTERIOR type OLE2_OBJECT .
  data MO_RANGE type OLE2_OBJECT .
  data MO_BORDERS type OLE2_OBJECT .
  data MO_COLUMNS type OLE2_OBJECT .
  data MV_ROW type I .
  data MV_COLUMN type I .

  methods _INIT_EXCEL
    importing
      !IV_MENU_DESC type ZIF_FLIFM_DEFINITIONS=>TY_FLIFM_MENU_DESC
    raising
      ZCX_FLIFM_EXCEPTION .
  methods _SET_TITLE_EXCEL
    importing
      !IV_CELL type I
      !IV_TITLE type STRING
    raising
      ZCX_FLIFM_EXCEPTION .
  methods _FILL_CELL
    importing
      !IV_ROW type I
      !IV_COLUMN type I
      !IV_BOLD type I
      !IV_SIZE type I
      !IV_COLOR type CHAR4 optional
      !IV_VALUE type STRING
    raising
      ZCX_FLIFM_EXCEPTION .
  methods _GET_COMPANY
    returning
      value(RV_BUTXT) type BUTXT
    raising
      ZCX_FLIFM_EXCEPTION .
  methods _SET_HEADER_EXCEL
    importing
      !IT_FIELDCAT type LVC_T_FCAT
    raising
      ZCX_FLIFM_EXCEPTION .
  methods _SET_ROW_EXCEL
    importing
      !IT_TABLE type STANDARD TABLE
      !IT_FIELDCAT type LVC_T_FCAT
    raising
      ZCX_FLIFM_EXCEPTION .
  methods _SET_FORMAT_EXCEL
    raising
      ZCX_FLIFM_EXCEPTION .
  methods _CLEAR_EXCEL_OBJECT .
ENDCLASS.



CLASS ZCL_FLIFM_EXCEL IMPLEMENTATION.


  METHOD zif_flifm_excel~download_fsv_list_excel.

    DATA: lv_cell TYPE i.
    DATA: lv_rc TYPE i.

    DATA: lv_menu_desc     TYPE zif_flifm_definitions=>ty_flifm_menu_desc,
          lv_sub_menu_desc TYPE zif_flifm_definitions=>ty_flifm_menu_desc.

    DATA: lt_data TYPE REF TO data.
    FIELD-SYMBOLS: <lt_table> TYPE STANDARD TABLE.

    zcl_flifm_progress=>show( iv_text = |Starting Excel...| ).

    CREATE DATA lt_data LIKE it_popup_table.
    ASSIGN lt_data->* TO <lt_table>.

    zcl_flifm_event_data_provider=>filtering_data( EXPORTING it_nkey  = it_nkey
                                                             it_table = it_popup_table
                                                   IMPORTING et_table = <lt_table> ).

    DATA: lt_fieldcat TYPE lvc_t_fcat,
          ls_fieldcat LIKE LINE OF lt_fieldcat.

    lt_fieldcat = zcl_flifm_event_data_provider=>create_event_fieldcat( it_popup_table ).

    lv_menu_desc = zcl_flifm_i18n=>get_instance( )->get_menu_description( zcl_flifm_utils=>split_menu( iv_menu ) ).

    _init_excel( lv_menu_desc ).

    zcl_flifm_progress=>show( iv_text = |Fill cells from list...| ).

    ADD 1 TO mv_row.

    LOOP AT lt_fieldcat INTO ls_fieldcat WHERE no_out IS INITIAL.
      IF ls_fieldcat-fieldname CP 'AMT*'.
        IF ls_fieldcat-fieldname+3(2) <= zcl_flifm_selection=>get_to_period( ).
        ELSE.
          CONTINUE.
        ENDIF.
      ENDIF.
      ADD 1 TO lv_cell.
    ENDLOOP.
    ADD 1 TO lv_cell.

    _set_title_excel( EXPORTING iv_cell  = lv_cell
                                iv_title = |{ sy-title }| ).

    ADD 2 TO mv_row.

    lv_sub_menu_desc = zcl_flifm_i18n=>get_instance( )->get_menu_description( iv_menu ).

    _set_title_excel( EXPORTING iv_cell  = lv_cell
                                iv_title = |{ lv_sub_menu_desc }| ).

    ADD 1 TO mv_row.
    ADD 1 TO mv_column.

    _set_header_excel( lt_fieldcat ).

    _set_row_excel( EXPORTING it_table = <lt_table>
                              it_fieldcat = lt_fieldcat ).

    _set_format_excel( ).

    _clear_excel_object( ).

  ENDMETHOD.


  METHOD _clear_excel_object.

    FREE OBJECT:
      mo_excel,
      mo_workbooks,
      mo_workbook,
      mo_worksheets,
      mo_cells,
      mo_to_cells,
      mo_font,
      mo_interior,
      mo_range,
      mo_borders,
      mo_columns.

    CLEAR: mv_row, mv_column.

  ENDMETHOD.


  METHOD _fill_cell.


    CALL METHOD OF
        mo_excel
        'CELLS'  = mo_cells
      EXPORTING
        #1       = iv_row
        #2       = iv_column.

    SET PROPERTY OF mo_cells 'VALUE' = iv_value.

    GET PROPERTY OF mo_cells 'FONT' = mo_font.

    SET PROPERTY OF mo_font 'SIZE' = iv_size.

    SET PROPERTY OF mo_font 'BOLD' = iv_bold.

    CASE iv_color.
      WHEN zif_flifm_definitions=>c_row_color-yellow.
        GET PROPERTY OF mo_cells 'Interior' = mo_interior.
        SET PROPERTY OF mo_interior 'ColorIndex' = 36.
      WHEN zif_flifm_definitions=>c_row_color-green.
        GET PROPERTY OF mo_cells 'Interior' = mo_interior.
        SET PROPERTY OF mo_interior 'ColorIndex' = 35.
      WHEN zif_flifm_definitions=>c_row_color-red.
        GET PROPERTY OF mo_cells 'Interior' = mo_interior.
        SET PROPERTY OF mo_interior 'ColorIndex' = 3.
      WHEN zif_flifm_definitions=>c_row_color-sky_blue.
        GET PROPERTY OF mo_cells 'Interior' = mo_interior.
        SET PROPERTY OF mo_interior 'ColorIndex' = 20.
    ENDCASE.


  ENDMETHOD.


  METHOD _get_company.


    DATA: lt_company TYPE zcl_flifm_fetch=>tyt_company,
          ls_company LIKE LINE OF lt_company,
          lv_lines   TYPE i.

*//Display company
    lt_company = zcl_flifm_fetch=>get_instance( )->get_company( ).

    lv_lines = lines( lt_company ).

    IF lv_lines EQ 1.
      LOOP AT lt_company INTO ls_company. ENDLOOP.
      rv_butxt = ls_company-butxt.
    ELSE.
      rv_butxt = zcl_flifm_i18n=>get_instance( )->flifm_title.
    ENDIF.


  ENDMETHOD.


  METHOD _init_excel.


*// Create OLE object for excel application.
    CREATE OBJECT mo_excel 'EXCEL.APPLICATION'.
    IF sy-subrc <> 0.
      _clear_excel_object( ).

      zcx_flifm_exception=>raise_msg( |Can't open Excel Application| ).
    ENDIF.

*// The excel sheet is not visible to the user while data transfer.
    SET PROPERTY OF mo_excel 'Visible' = 0.

*// Get the control
    CALL METHOD OF
      mo_excel
        'Workbooks' = mo_workbooks.

*// Create a new workbook
    CALL METHOD OF
      mo_workbooks
        'Add' = mo_workbook.

*// Create sheets
    CALL METHOD OF
      mo_excel
        'Worksheets' = mo_worksheets.

*// Set sheet name
    CALL METHOD OF
      mo_worksheets
        'Add' = mo_sheet.

    SET PROPERTY OF mo_sheet 'Name' = iv_menu_desc.


  ENDMETHOD.


  METHOD _set_format_excel.

    "Start table cell
    CALL METHOD OF
        mo_excel
        'Cells'  = mo_cells
      EXPORTING
        #1       = 4
        #2       = 2.

    "End table cell
    CALL METHOD OF
        mo_excel
        'Cells'  = mo_to_cells
      EXPORTING
        #1       = mv_row
        #2       = mv_column.

    CALL METHOD OF
        mo_excel
        'Range'  = mo_range
      EXPORTING
        #1       = mo_cells
        #2       = mo_to_cells.

    CALL METHOD OF
      mo_range
        'Borders' = mo_borders.

    SET PROPERTY OF mo_borders 'LINESTYLE' = 1.

*// Autofit
    CALL METHOD OF
      mo_excel
        'COLUMNS' = mo_columns.

    CALL METHOD OF
      mo_columns
      'AUTOFIT'.

*// Start excel
    SET PROPERTY OF mo_excel  'Visible' = 1.


  ENDMETHOD.


  METHOD _set_header_excel.

    DATA: ls_fieldcat LIKE LINE OF it_fieldcat.

    LOOP AT it_fieldcat INTO ls_fieldcat WHERE no_out IS INITIAL.
      IF ls_fieldcat-fieldname CP 'AMT*'.
        IF ls_fieldcat-fieldname+3(2) <= zcl_flifm_selection=>get_to_period( ).
        ELSE.
          CONTINUE.
        ENDIF.
      ENDIF.
      ADD 1 TO mv_column.
      _fill_cell( EXPORTING iv_row    = mv_row
                            iv_column = mv_column
                            iv_bold   = 1
                            iv_size   = 15
                            iv_value  = |{ ls_fieldcat-scrtext_l }| ).

    ENDLOOP.

  ENDMETHOD.


  METHOD _set_row_excel.

    DATA: lt_data TYPE REF TO data.

    DATA: ls_fieldcat LIKE LINE OF it_fieldcat.

    FIELD-SYMBOLS: <ls_table> TYPE any,
                   <lv_value> TYPE any,
                   <lv_color> TYPE any.

    CREATE DATA lt_data LIKE it_table.
    ASSIGN lt_data->* TO <ls_table>.

    LOOP AT it_table ASSIGNING <ls_table>.

      ADD 1 TO mv_row.
      CLEAR mv_column.
      ADD 2 TO mv_column.

      ASSIGN COMPONENT 'ROW_COLOR' OF STRUCTURE <ls_table> TO <lv_color>.

      ASSIGN COMPONENT 'TLEVEL' OF STRUCTURE <ls_table> TO <lv_value>.
      _fill_cell( EXPORTING iv_row    = mv_row
                            iv_column = mv_column
                            iv_bold   = 1
                            iv_size   = 10
                            iv_color  = <lv_color>
                            iv_value  = |{ <lv_value> }| ).

      ADD 1 TO mv_column.
      ASSIGN COMPONENT 'TEXT' OF STRUCTURE <ls_table> TO <lv_value>.
      _fill_cell( EXPORTING iv_row    = mv_row
                            iv_column = mv_column
                            iv_bold   = 1
                            iv_size   = 10
                            iv_color  = <lv_color>
                            iv_value  = |{ <lv_value> }| ).

      ADD 1 TO mv_column.
      ASSIGN COMPONENT 'HKONT' OF STRUCTURE <ls_table> TO <lv_value>.
      _fill_cell( EXPORTING iv_row    = mv_row
                            iv_column = mv_column
                            iv_bold   = 1
                            iv_size   = 10
                            iv_color  = <lv_color>
                            iv_value  = |{ <lv_value> }| ).

      ADD 1 TO mv_column.
      ASSIGN COMPONENT 'TXT50' OF STRUCTURE <ls_table> TO <lv_value>.
      _fill_cell( EXPORTING iv_row    = mv_row
                            iv_column = mv_column
                            iv_bold   = 1
                            iv_size   = 10
                            iv_color  = <lv_color>
                            iv_value  = |{ <lv_value> }| ).

      LOOP AT it_fieldcat INTO ls_fieldcat WHERE fieldname CP '*AMT*' OR fieldname CP '*PER'.
        IF ls_fieldcat-fieldname CP 'AMT*'.
          IF ls_fieldcat-fieldname+3(2) <= zcl_flifm_selection=>get_to_period( ).
          ELSE.
            CONTINUE.
          ENDIF.
        ENDIF.
        ADD 1 TO mv_column.
        ASSIGN COMPONENT ls_fieldcat-fieldname OF STRUCTURE <ls_table> TO <lv_value>.
        _fill_cell( EXPORTING iv_row  = mv_row
                              iv_column = mv_column
                              iv_bold   = 1
                              iv_size   = 10
                              iv_color  = <lv_color>
                              iv_value  = |{ <lv_value> }| ).
      ENDLOOP.

      ADD 1 TO mv_column.
      ASSIGN COMPONENT 'WAERS' OF STRUCTURE <ls_table> TO <lv_value>.
      _fill_cell( EXPORTING iv_row = mv_row
                            iv_column = mv_column
                            iv_bold   = 1
                            iv_size   = 10
                            iv_color  = <lv_color>
                            iv_value  = |{ <lv_value> }| ).

    ENDLOOP.


  ENDMETHOD.


  METHOD _set_title_excel.

    _fill_cell( EXPORTING iv_row    = mv_row
                          iv_column = 2
                          iv_bold   = 1
                          iv_size   = 17
                          iv_value  = iv_title ).

    CALL METHOD OF
        mo_excel
        'CELLS'  = mo_to_cells
      EXPORTING
        #1       = mv_row
        #2       = iv_cell.

    CALL METHOD OF
        mo_excel
        'Range'  = mo_range
      EXPORTING
        #1       = mo_cells
        #2       = mo_to_cells.

    CALL METHOD OF
      mo_range
      'SELECT'.

    CALL METHOD OF
      mo_range
      'MERGE'.

  ENDMETHOD.
ENDCLASS.