class ZCL_FLIFM_I18N definition
  public
  create public .

public section.

  data FLIFM_TITLE type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data BLOCK1 type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data BLOCK2 type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data BLOCK3 type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data REPORTING_YEAR type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data REPORTING_PERIOD type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data COMPANY_CODE type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data COMPARISON_YEAR type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data TREE_DISPLAY_LEVEL type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data NOT_ASSIGNED type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data CALC_NET_PROFIT type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data CALC_NET_PROFIT_YTD type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data EXPAND_ALL type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data COLLAPSE_ALL type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data FSV_POPUP type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data FSV_EXCEL type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data ITEM_ACCOUNT type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data BALANCE_CF type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data YTD type ZIF_FLIFM_DEFINITIONS=>TY_I18N .
  data:
    BEGIN OF fsv_tot_i18n,
        tb TYPE seu_text VALUE 'TB(Total)',
        pl TYPE seu_text VALUE 'PL(Total)',
        bs TYPE seu_text VALUE 'BS(Total)',
      END OF fsv_tot_i18n .
  data FUNCTIONAL_AREA type ZIF_FLIFM_DEFINITIONS=>TY_I18N .

  class-methods GET_INSTANCE
    returning
      value(RO_TEXT) type ref to ZCL_FLIFM_I18N .
  methods CONSTRUCTOR .
  methods GET_MENU_DESCRIPTION
    importing
      !IV_MENU type ZIF_FLIFM_DEFINITIONS=>TY_FLIFM_MENU_TYPE
    returning
      value(RV_DESCR) type TEXT30 .
  methods GET_INITIAL_MENU_DESC
    returning
      value(RS_DESC) type ZIF_FLIFM_DEFINITIONS=>TYS_FLIFM_MENU_DESC_I18N .
  PROTECTED SECTION.
private section.

  types:
    BEGIN OF tys_flifm_menu_desc,
             menu_type TYPE zif_flifm_definitions=>ty_flifm_menu_type,
             descr     TYPE text30,
           END OF tys_flifm_menu_desc .
  types:
    tyt_flifm_menu_desc TYPE HASHED TABLE OF tys_flifm_menu_desc WITH UNIQUE KEY menu_type .

  class-data GO_FLIFM_TEXT type ref to ZCL_FLIFM_I18N .
  data MT_FLIFM_MENU_DESC type TYT_FLIFM_MENU_DESC .
ENDCLASS.



CLASS ZCL_FLIFM_I18N IMPLEMENTATION.


  METHOD CONSTRUCTOR.

    FLIFM_TITLE         = 'FI LAB. IFM Report'(t01).
    BLOCK1              = 'Select Option'(t02).
    BLOCK2              = 'Comparison Option'(t03).
    BLOCK3              = 'Etc Option'(t04).
    REPORTING_YEAR      = 'Reporting Year'(t05).
    REPORTING_PERIOD    = 'Reporting Period'(t06).
    COMPANY_CODE        = 'Company Code'(t07).
    FUNCTIONAL_AREA     = 'Functional Area'(t23).
    COMPARISON_YEAR     = 'Comparison Year'(t08).
    TREE_DISPLAY_LEVEL  = 'Tree Display Level'(t09).
    NOT_ASSIGNED        = 'Not Assigned'(t10).
    CALC_NET_PROFIT     = 'Calculated Net Profit'(t11).
    CALC_NET_PROFIT_YTD = 'Calculated Net Profit(Cumulation)'(t12).
    EXPAND_ALL          = 'Expand All'(t13).
    COLLAPSE_ALL        = 'Collapse All'(t14).
    FSV_POPUP           = 'Drag & Copy'(t15).
    FSV_EXCEL           = 'Download Excel'(t16).
    ITEM_ACCOUNT        = 'Item/Account'(t17).
    BALANCE_CF          = 'Balance Carryforward'(t18).
    YTD                 = 'YTD'(t19).

    FSV_TOT_I18N-TB = 'TB(Total)'(t20).
    FSV_TOT_I18N-PL = 'PL(Total)'(t21).
    FSV_TOT_I18N-BS = 'BS(Total)'(t22).

**// Menu Description
*    SELECT * INTO CORRESPONDING FIELDS OF TABLE mt_flifm_menu_desc
*      FROM zflifmt_mtypet
*      WHERE spras = sy-langu.
*
*    IF sy-subrc <> 0.
*      SELECT * INTO CORRESPONDING FIELDS OF TABLE mt_flifm_menu_desc
*        FROM zflifmt_mtypet
*        WHERE spras = zif_flifm_definitions=>c_default_langu.
*    ENDIF.

  ENDMETHOD.


  METHOD get_initial_menu_desc.

    rs_desc-tb          = 'Trial Balance'(d01).
    rs_desc-tb_ttb      = 'Total Trial Balance'(d02).
    rs_desc-tb_trend    = 'Trial Balance Trend'(d03).
    rs_desc-tb_rptb     = 'T/B of Reporting Period'(d04).
    rs_desc-pl          = 'Profit and Loss'(d05).
    rs_desc-pl_rp_cysp  = 'Rpt Period vs CY Same Period'(d06).
    rs_desc-pl_try_tcy  = 'Tot of RY vs Tot of CY'(d07).
    rs_desc-pl_ry_trend = 'Reporting Year Monthly Trend'(d08).
    rs_desc-pl_cy_trend = 'Comparison Year Monthly Trend'(d09).
    rs_desc-bs          = 'Balance Sheet'(d10).
    rs_desc-bs_cy_rp_ry = 'Tot of CY vs RP vs Tot of RY'(d11).
    rs_desc-bs_try_tcy  = 'Tot of RY vs Tot of CY'(d12).
    rs_desc-bs_rp_cysp  = 'Rpt Period vs CY Same Period'(d13).
    rs_desc-bs_ry_trend = 'Reporting Year Monthly Trend'(d14).
    rs_desc-bs_cy_trend = 'Comparison Year Monthly Trend'(d15).

  ENDMETHOD.


  METHOD get_instance.


    IF go_flifm_text IS NOT BOUND.
      CREATE OBJECT go_flifm_text.
    ENDIF.

    ro_text = go_flifm_text.


  ENDMETHOD.


  METHOD get_menu_description.

    DATA ls_flifm_menu_desc LIKE LINE OF mt_flifm_menu_desc.

    IF mt_flifm_menu_desc IS INITIAL.
      SELECT * INTO CORRESPONDING FIELDS OF TABLE mt_flifm_menu_desc
        FROM zflifmt_mtypet
        WHERE spras = sy-langu.

      IF sy-subrc <> 0.
        SELECT * INTO CORRESPONDING FIELDS OF TABLE mt_flifm_menu_desc
          FROM zflifmt_mtypet
          WHERE spras = zif_flifm_definitions=>c_default_langu.
      ENDIF.
    ENDIF.

    READ TABLE mt_flifm_menu_desc INTO ls_flifm_menu_desc WITH TABLE KEY menu_type = iv_menu.

    IF sy-subrc = 0.
      rv_descr = ls_flifm_menu_desc-descr.
    ENDIF.

  ENDMETHOD.
ENDCLASS.