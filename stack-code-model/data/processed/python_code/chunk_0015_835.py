class ZCL_FLIFM_UTILS definition
  public
  create public .

public section.

  types:
    tyt_dfies TYPE STANDARD TABLE OF dfies WITH DEFAULT KEY .

  class-methods GET_FIELDINFO
    importing
      !IV_TABNAME type TABNAME
    returning
      value(RT_FIELDINFO) type TYT_DFIES
    raising
      ZCX_FLIFM_EXCEPTION .
  class-methods SPLIT_MENU
    importing
      !IV_MENU type ZIF_FLIFM_DEFINITIONS=>TY_FLIFM_MENU_TYPE
      !IV_SUB type ABAP_BOOL optional
    returning
      value(RV_MENU) type ZIF_FLIFM_DEFINITIONS=>TY_FLIFM_MENU_TYPE .
  class-methods GET_FIELDCATALOG
    importing
      !IT_TABLE type ANY TABLE
    returning
      value(RT_FCAT) type LVC_T_FCAT
    raising
      ZCX_FLIFM_EXCEPTION .
  class-methods MOVE_NUMBER_TO_CHAR
    importing
      !IV_WAERS type WAERS
    changing
      !CV_DATA type CLIKE .
protected section.
private section.
ENDCLASS.



CLASS ZCL_FLIFM_UTILS IMPLEMENTATION.


  METHOD get_fieldcatalog.

    DATA: lo_columns      TYPE REF TO cl_salv_columns_table,
          lo_aggregations TYPE REF TO cl_salv_aggregations,
          lo_salv_table   TYPE REF TO cl_salv_table,
          lr_table        TYPE REF TO data,
          lx_cx           TYPE REF TO cx_root.

    FIELD-SYMBOLS: <table> TYPE STANDARD TABLE.

    CREATE DATA lr_table LIKE it_table.
    ASSIGN lr_table->* TO <table>.

    TRY.
        cl_salv_table=>factory(
          EXPORTING
            list_display = abap_false
          IMPORTING
            r_salv_table = lo_salv_table
          CHANGING
            t_table      = <table> ).
      CATCH cx_salv_msg cx_salv_not_found cx_salv_data_error INTO lx_cx.
        zcx_flifm_exception=>raise_msg( lx_cx->get_text( ) ).
    ENDTRY.

    lo_columns  = lo_salv_table->get_columns( ).
    lo_aggregations = lo_salv_table->get_aggregations( ).

    rt_fcat = cl_salv_controller_metadata=>get_lvc_fieldcatalog( r_columns = lo_columns
                                                                 r_aggregations = lo_aggregations ).

    DELETE rt_fcat WHERE rollname = 'MANDT'.

  ENDMETHOD.


  method GET_FIELDINFO.


    CALL FUNCTION 'DDIF_FIELDINFO_GET'
      EXPORTING
        tabname        = iv_tabname
      TABLES
        dfies_tab      = rt_fieldinfo
      EXCEPTIONS
        not_found      = 1
        internal_error = 2
        OTHERS         = 3.

    IF sy-subrc <> 0.

      zcx_flifm_exception=>raise_t100( iv_msgno = 001
                                       iv_msgv1 = 'DDIF_FIELDINFO_GET'
                                       iv_msgv2 = |{ sy-subrc }|
                                       iv_msgv3 = |{ iv_tabname }| ).

    ENDIF.


  endmethod.


  METHOD MOVE_NUMBER_TO_CHAR.

    DATA: lv_calc TYPE zif_flifm_definitions=>ty_amt_calc.

    IF iv_waers IS NOT INITIAL.

      lv_calc = cv_data.

      IF lv_calc IS NOT INITIAL.
        lv_calc = lv_calc / 1000000.
      ENDIF.

      WRITE lv_calc TO cv_data CURRENCY iv_waers.

    ENDIF.

  ENDMETHOD.


  METHOD split_menu.

    TYPES: BEGIN OF tys_menu,
             menu_type TYPE zflifme_menu_type,
           END OF tys_menu.

    TYPES: tyt_menu TYPE STANDARD TABLE OF tys_menu WITH NON-UNIQUE KEY menu_type.

    DATA: lt_menu       TYPE tyt_menu,
          lv_split_menu TYPE zif_flifm_definitions=>ty_flifm_menu_type,
          lv_copy_menu  TYPE zif_flifm_definitions=>ty_flifm_menu_type.

    SPLIT iv_menu AT zif_flifm_definitions=>c_underscore INTO TABLE lt_menu.

" Clean Code: Split method instead of Boolean input parameter
    IF iv_sub IS INITIAL.
      READ TABLE lt_menu INTO rv_menu INDEX 1.
    ELSE.
      lv_copy_menu = iv_menu.
      READ TABLE lt_menu INTO lv_split_menu INDEX 1.
      CONCATENATE lv_split_menu zif_flifm_definitions=>c_underscore INTO lv_split_menu.
      REPLACE ALL OCCURRENCES OF lv_split_menu IN lv_copy_menu WITH ''.
      rv_menu = lv_copy_menu.
    ENDIF.

  ENDMETHOD.
ENDCLASS.