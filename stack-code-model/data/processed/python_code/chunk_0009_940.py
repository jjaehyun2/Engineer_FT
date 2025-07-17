class ZCL_FLIFM_FETCH definition
  public
  create public .

public section.

  types:
    BEGIN OF tys_company,
        bukrs TYPE bseg-bukrs,
        butxt TYPE butxt,
        land1 TYPE t001-land1,
        waers TYPE t001-waers,
        ktopl TYPE t001-ktopl,
      END OF tys_company .
  types:
    tyt_company TYPE HASHED TABLE OF tys_company WITH UNIQUE KEY bukrs .
  types:
    tyt_dd03t TYPE STANDARD TABLE OF dd03t WITH DEFAULT KEY .
  types:
    tyt_dd07t TYPE STANDARD TABLE OF dd07t WITH DEFAULT KEY .
  types:
    tyt_gl_tot TYPE STANDARD TABLE OF zif_flifm_definitions=>tys_gl_tot WITH DEFAULT KEY .
  types:
    BEGIN OF tys_tcurr,
        gjahr	TYPE gjahr,
        monat	TYPE monat,
        fcurr	TYPE fcurr_curr,
        tcurr	TYPE tcurr_curr,
        frate	TYPE zflifme_frate,
        trate	TYPE zflifme_trate,
        ukurs TYPE zflifme_ukurs,
      END OF tys_tcurr .
  types:
    tyt_tcurr TYPE STANDARD TABLE OF tys_tcurr WITH DEFAULT KEY .
  types:
    TYR_RFAREA TYPE RANGE OF FKBER .

  data SND_JOBS type I value 1 ##NO_TEXT.
  data RCV_JOBS type I value 1 ##NO_TEXT.
  data STARTED_JOBS type I .
  data COMPLETED_JOBS type I .
  data MV_RUNNING_ARFC_WPS type I .
  data TASKNAME type SYINDEX .
  data:
    excp_flag(1)        TYPE c .
  data MV_MESSAGE type BAPIRET2-MESSAGE .
  constants MC_RLDNR type FAGLFLEXT-RLDNR value '0L' ##NO_TEXT.
  constants MC_RRCTY type FAGLFLEXT-RRCTY value '0' ##NO_TEXT.
  constants MC_RVERS type FAGLFLEXT-RVERS value '001' ##NO_TEXT.
  constants MC_GROUP type RZLLI_APCL value 'parallel_generators' ##NO_TEXT.

  class-methods GET_INSTANCE
    importing
      !IO_SELECTION type ref to ZCL_FLIFM_SELECTION optional
    returning
      value(RO_FETCH) type ref to ZCL_FLIFM_FETCH .
  methods SET_DATA_INIT
    raising
      ZCX_FLIFM_EXCEPTION .
  methods FETCH_DATA .
  methods FETCH_DATA_SINGLE .
  methods FETCH_DATA_PARALLEL
    importing
      !IV_GROUP type RZLLI_APCL .
  methods RETURN_INFO
    importing
      !P_TASK type CLIKE .
  methods GET_IFM_NODE_TAB_BS
    returning
      value(RT_IFM_NODE_TAB_BS) type ZIF_FLIFM_DEFINITIONS=>TYT_NODE_TAB .
  methods GET_IFM_NODE_TAB_PL
    returning
      value(RT_IFM_NODE_TAB_PL) type ZIF_FLIFM_DEFINITIONS=>TYT_NODE_TAB .
  methods GET_IFM_NODE_TAB_TB
    returning
      value(RT_IFM_NODE_TAB_TB) type ZIF_FLIFM_DEFINITIONS=>TYT_NODE_TAB .
  methods GET_COMPANY
    returning
      value(RT_COMPANY) type TYT_COMPANY .
  methods GET_DD03T
    returning
      value(RT_DD03T) type TYT_DD03T .
  methods GET_GL_TOT
    returning
      value(RT_GL_TOT) type TYT_GL_TOT .
  methods GET_SKAT
    returning
      value(RT_SKAT) type ZIF_FLIFM_DEFINITIONS=>TYT_SKAT .
  methods GET_LAYOUT
    returning
      value(RT_LAYOUT) type ZIF_FLIFM_DEFINITIONS=>TYT_LAYOUT .
  methods GET_SAVED_LAYOUT
    returning
      value(RS_SAVED_LAYOUT) type ZIF_FLIFM_DEFINITIONS=>TY_SAVED_LAYOUT .
  methods GET_INTER_WAERS
    returning
      value(RV_INTER_WAERS) type WAERS .
  methods GET_TCURR
    importing
      !IV_GJAHR type GJAHR
      !IV_MONAT type MONAT
      !IV_FCURR type FCURR_CURR
      !IV_TCURR type TCURR_CURR
    returning
      value(RV_UKURS) type ZFLIFME_UKURS
    raising
      ZCX_FLIFM_EXCEPTION .
  methods GET_T030
    returning
      value(RT_T030) type ZIF_FLIFM_DEFINITIONS=>TYT_T030 .
  PROTECTED SECTION.
private section.

  types:
    BEGIN OF TYS_COMPANY_SELECT,
        BUKRS TYPE BUKRS,
        GJAHR TYPE GJAHR,
      END OF TYS_COMPANY_SELECT .
  types:
    TYT_COMPANY_SELECT TYPE STANDARD TABLE OF TYS_COMPANY_SELECT WITH DEFAULT KEY .
  types:
    BEGIN OF TYS_RE, "Retained earnings items
        SAKNR TYPE SAKNR,
        GVTYP TYPE GVTYP,
        KTOPL TYPE KTOPL,
        KOMOK TYPE KOMOK,
        KONTS TYPE SAKNR,
      END OF TYS_RE .
  types:
    TYT_RE TYPE HASHED TABLE OF TYS_RE WITH UNIQUE KEY SAKNR .
  types:
    BEGIN OF TYS_FAGLFLEXT,
        RBUKRS TYPE FAGLFLEXT-RBUKRS,
        RYEAR  TYPE FAGLFLEXT-RYEAR,
        DRCRK  TYPE FAGLFLEXT-DRCRK,
        RACCT  TYPE FAGLFLEXT-RACCT,
        RBUSA  TYPE FAGLFLEXT-RBUSA,
        PRCTR  TYPE FAGLFLEXT-PRCTR,
        HSLVT  TYPE FAGLFLEXT-HSLVT,
        HSL01  TYPE FAGLFLEXT-HSL01,
        HSL02  TYPE FAGLFLEXT-HSL02,
        HSL03  TYPE FAGLFLEXT-HSL03,
        HSL04  TYPE FAGLFLEXT-HSL04,
        HSL05  TYPE FAGLFLEXT-HSL05,
        HSL06  TYPE FAGLFLEXT-HSL06,
        HSL07  TYPE FAGLFLEXT-HSL07,
        HSL08  TYPE FAGLFLEXT-HSL08,
        HSL09  TYPE FAGLFLEXT-HSL09,
        HSL10  TYPE FAGLFLEXT-HSL10,
        HSL11  TYPE FAGLFLEXT-HSL11,
        HSL12  TYPE FAGLFLEXT-HSL12,
        HSL13  TYPE FAGLFLEXT-HSL13,
        HSL14  TYPE FAGLFLEXT-HSL14,
        HSL15  TYPE FAGLFLEXT-HSL15,
        HSL16  TYPE FAGLFLEXT-HSL16,
      END OF TYS_FAGLFLEXT .
  types:
    TYT_FAGLFLEXT TYPE STANDARD TABLE OF TYS_FAGLFLEXT WITH DEFAULT KEY .
  types:
    TYR_BUKRS TYPE RANGE OF BUKRS .
  types:
    TYR_GJAHR TYPE RANGE OF GJAHR .

  class-data GO_FETCH type ref to ZCL_FLIFM_FETCH .
  data MT_GL_TOT type TYT_GL_TOT .
  data MT_COMPANY type TYT_COMPANY .
  data:
    MS_COMPANY        TYPE LINE OF TYT_COMPANY .
  data MT_COMPANY_SELECT type TYT_COMPANY_SELECT .
  data:
    MS_COMPANY_SELECT TYPE LINE OF TYT_COMPANY_SELECT .
  data MT_T030 type ZIF_FLIFM_DEFINITIONS=>TYT_T030 .
  data MT_RE type TYT_RE .
  data MT_SKAT type ZIF_FLIFM_DEFINITIONS=>TYT_SKAT .
  data MT_LAYOUT type ZIF_FLIFM_DEFINITIONS=>TYT_LAYOUT .
  data MS_SAVED_LAYOUT type ZIF_FLIFM_DEFINITIONS=>TY_SAVED_LAYOUT .
  data MT_DD03T type TYT_DD03T .
  data MT_DD07T type TYT_DD07T .
  data MT_IFM_NODE_TAB_BS type ZIF_FLIFM_DEFINITIONS=>TYT_NODE_TAB .
  data MT_IFM_NODE_TAB_PL type ZIF_FLIFM_DEFINITIONS=>TYT_NODE_TAB .
  data MT_IFM_NODE_TAB_TB type ZIF_FLIFM_DEFINITIONS=>TYT_NODE_TAB .
  data MV_INTER_WAERS type WAERS .
  data MT_TCURR type TYT_TCURR .

  methods _SELECT_SETTING
    raising
      ZCX_FLIFM_EXCEPTION .
  methods _CHECK_COMPANY_CODE
    raising
      ZCX_FLIFM_EXCEPTION .
  methods _BUILD_RE_ACCOUNTS .
  methods _GET_ACCOUNT_TEXT .
  methods _GET_FIELD_TEXT .
  methods _BUILD_IFM_FSV_LAYOUT
    raising
      ZCX_FLIFM_EXCEPTION .
  methods _BUILD_FSV_LAYOUT
    raising
      ZCX_FLIFM_EXCEPTION .
  methods _BUILD_CURRENCY
    raising
      ZCX_FLIFM_EXCEPTION .
ENDCLASS.



CLASS ZCL_FLIFM_FETCH IMPLEMENTATION.


  METHOD fetch_data.

    zcl_flifm_progress=>show( iv_text = |Select data...| ).

    fetch_data_single( ).

    SORT mt_gl_tot BY gjahr monat bukrs waers hkont.

    zcl_flifm_progress=>show( iv_text = |Preparing output...| ).

  ENDMETHOD.


  METHOD fetch_data_parallel.

  ENDMETHOD.


  METHOD FETCH_DATA_SINGLE.


*// Build select data
    DATA: LR_BUKRS   TYPE TYR_BUKRS,
          LRS_BUKRS  LIKE LINE OF LR_BUKRS,
          LR_GJAHR   TYPE TYR_GJAHR,
          LRS_GJAHR  LIKE LINE OF LR_GJAHR,
          LR_RFAREA  TYPE TYR_RFAREA,
          LRS_RFAREA LIKE LINE OF LR_RFAREA.

    DATA LV_TO_PERIOD TYPE ZFLIFME_TO_PERIOD.

    CLEAR LRS_GJAHR.
    LRS_GJAHR-SIGN = 'I'.
    LRS_GJAHR-OPTION = 'EQ'.
    LRS_GJAHR-LOW = ZCL_FLIFM_SELECTION=>GET_CMP_GJAHR( ).
    APPEND LRS_GJAHR TO LR_GJAHR.

    CLEAR LRS_GJAHR.
    LRS_GJAHR-SIGN = 'I'.
    LRS_GJAHR-OPTION = 'EQ'.
    LRS_GJAHR-LOW = ZCL_FLIFM_SELECTION=>GET_GJAHR( ).
    APPEND LRS_GJAHR TO LR_GJAHR.

    LOOP AT MT_COMPANY INTO MS_COMPANY.

      CLEAR LRS_BUKRS.
      LRS_BUKRS-SIGN = 'I'.
      LRS_BUKRS-OPTION = 'EQ'.
      LRS_BUKRS-LOW = MS_COMPANY-BUKRS.
      APPEND LRS_BUKRS TO LR_BUKRS.

    ENDLOOP.

    LR_RFAREA = ZCL_FLIFM_SELECTION=>GET_RFAREA( ).

    LV_TO_PERIOD = ZCL_FLIFM_SELECTION=>GET_TO_PERIOD( ).

*// Select Data
    DATA: LT_FAGLFLEXT TYPE TYT_FAGLFLEXT,
          LS_FAGLFLEXT LIKE LINE OF LT_FAGLFLEXT.

    SELECT RBUKRS
           RYEAR
           DRCRK
           RACCT
           SUM( HSLVT ) AS HSLVT
           SUM( HSL01 ) AS HSL01
           SUM( HSL02 ) AS HSL02
           SUM( HSL03 ) AS HSL03
           SUM( HSL04 ) AS HSL04
           SUM( HSL05 ) AS HSL05
           SUM( HSL06 ) AS HSL06
           SUM( HSL07 ) AS HSL07
           SUM( HSL08 ) AS HSL08
           SUM( HSL09 ) AS HSL09
           SUM( HSL10 ) AS HSL10
           SUM( HSL11 ) AS HSL11
           SUM( HSL12 ) AS HSL12
           SUM( HSL13 ) AS HSL13
           SUM( HSL14 ) AS HSL14
           SUM( HSL15 ) AS HSL15
           SUM( HSL16 ) AS HSL16
      INTO CORRESPONDING FIELDS OF TABLE LT_FAGLFLEXT
      FROM FAGLFLEXT
     WHERE RLDNR  EQ MC_RLDNR
       AND RRCTY  EQ MC_RRCTY
       AND RVERS  EQ MC_RVERS
       AND RBUKRS IN LR_BUKRS
       AND RYEAR  IN LR_GJAHR
       AND RFAREA IN LR_RFAREA
     GROUP BY RBUKRS
             RYEAR
             DRCRK
             RACCT.

*// Build Total Data
    DATA LS_GL_TOT LIKE LINE OF MT_GL_TOT.
    DATA LS_RE LIKE LINE OF MT_RE.
    DATA LS_SKAT LIKE LINE OF MT_SKAT.

    FIELD-SYMBOLS: <LV_HSL>  TYPE ANY.
    DATA: LV_CNT(2)  TYPE N,
          LV_FNM(20) TYPE C.

    LOOP AT LT_FAGLFLEXT INTO LS_FAGLFLEXT.

      CLEAR: MS_COMPANY, LS_GL_TOT.
      READ TABLE MT_COMPANY INTO MS_COMPANY WITH TABLE KEY BUKRS = LS_FAGLFLEXT-RBUKRS.

      IF SY-SUBRC = 0.
        LS_GL_TOT-WAERS = MS_COMPANY-WAERS.
      ENDIF.

      LS_GL_TOT-GJAHR = LS_FAGLFLEXT-RYEAR.
      LS_GL_TOT-BUKRS = LS_FAGLFLEXT-RBUKRS.
      LS_GL_TOT-HKONT = LS_FAGLFLEXT-RACCT.

      " Opening Balance
      LS_GL_TOT-OBAMT = LS_FAGLFLEXT-HSLVT.

      CASE LS_FAGLFLEXT-DRCRK.
        WHEN 'S'.
          " Debit Opening Balance
          LS_GL_TOT-DOBAMT = LS_FAGLFLEXT-HSLVT.
        WHEN 'H'.
          " Credit Opening Balance
          LS_GL_TOT-COBAMT = LS_FAGLFLEXT-HSLVT.
      ENDCASE.

      " Retained earnings
      READ TABLE MT_RE INTO LS_RE WITH TABLE KEY SAKNR = LS_FAGLFLEXT-RACCT.

      IF SY-SUBRC = 0.
        LS_GL_TOT-KOMOK = LS_RE-KOMOK.
        LS_GL_TOT-KONTS = LS_RE-KONTS.
      ENDIF.

      " Total
      CLEAR : LV_CNT, LV_FNM.
      DO LV_TO_PERIOD TIMES.
        LV_CNT = LV_CNT + 1.

        CONCATENATE 'LS_FAGLFLEXT-HSL' LV_CNT INTO LV_FNM.
        ASSIGN (LV_FNM)  TO  <LV_HSL>.

        " Period
        LS_GL_TOT-MONAT = LV_CNT.
        " Monthly Balance
        LS_GL_TOT-MBAMT = <LV_HSL>.
        " Monthly Cumulative Balance
        LS_GL_TOT-MCBAMT = LS_GL_TOT-MCBAMT + <LV_HSL>.
        " Yearly Cumulative Balance = Opening Balance + Monthly Cumulative Balance
        LS_GL_TOT-YCBAMT = LS_GL_TOT-OBAMT + LS_GL_TOT-MCBAMT.

        " T/B
        CASE LS_FAGLFLEXT-DRCRK.
          WHEN 'S'.
            "  Debit Balance
            LS_GL_TOT-DBAMT = <LV_HSL>.
            "  Debit Total
            LS_GL_TOT-DTAMT = LS_GL_TOT-DTAMT + <LV_HSL>.
          WHEN 'H'.
            "  Credit Balance
            LS_GL_TOT-CBAMT = <LV_HSL>.
            "  Credit Total
            LS_GL_TOT-CTAMT = LS_GL_TOT-CTAMT + <LV_HSL>.
        ENDCASE.

        COLLECT LS_GL_TOT INTO MT_GL_TOT.

      ENDDO.

    ENDLOOP.


  ENDMETHOD.


  METHOD get_company.

    rt_company = mt_company.

  ENDMETHOD.


  METHOD get_dd03t.

    rt_dd03t = mt_dd03t.

  ENDMETHOD.


  METHOD get_gl_tot.

    rt_gl_tot = mt_gl_tot.

  ENDMETHOD.


  METHOD get_ifm_node_tab_bs.

    rt_ifm_node_tab_bs = mt_ifm_node_tab_bs.

  ENDMETHOD.


  METHOD get_ifm_node_tab_pl.

    rt_ifm_node_tab_pl = mt_ifm_node_tab_pl.

  ENDMETHOD.


  METHOD get_ifm_node_tab_tb.

    rt_ifm_node_tab_tb = mt_ifm_node_tab_tb.

  ENDMETHOD.


  METHOD get_instance.

    IF go_fetch IS NOT BOUND.
      CREATE OBJECT go_fetch.
    ENDIF.

    ro_fetch = go_fetch.

  ENDMETHOD.


  METHOD get_inter_waers.

    rv_inter_waers = mv_inter_waers.

  ENDMETHOD.


  METHOD get_layout.

    rt_layout = mt_layout.

  ENDMETHOD.


  METHOD get_saved_layout.

    rs_saved_layout = ms_saved_layout.

  ENDMETHOD.


  METHOD get_skat.

    rt_skat = mt_skat.

  ENDMETHOD.


  METHOD get_t030.

    rt_t030 = mt_t030.

  ENDMETHOD.


  METHOD get_tcurr.


    DATA: ls_tcurr LIKE LINE OF mt_tcurr.

    READ TABLE mt_tcurr INTO ls_tcurr WITH KEY gjahr = iv_gjahr
                                               monat = iv_monat
                                               fcurr = iv_fcurr
                                               tcurr = iv_tcurr BINARY SEARCH.

    IF ls_tcurr-ukurs IS INITIAL.

      READ TABLE mt_tcurr INTO ls_tcurr WITH KEY gjahr = iv_gjahr
                                               monat = '0'
                                               fcurr = iv_fcurr
                                               tcurr = iv_tcurr BINARY SEARCH.

      IF ls_tcurr-ukurs IS INITIAL.

        zcx_flifm_exception=>raise_t100( iv_msgno = 007
                                         iv_msgv1 = |{ iv_fcurr }|
                                         iv_msgv2 = |{ iv_tcurr }|
                                         iv_msgv3 = |{ iv_monat } or 0|
                                         iv_msgv4 = |{ iv_gjahr }| ).
      ENDIF.

    ENDIF.

    rv_ukurs = ls_tcurr-ukurs.


  ENDMETHOD.


  METHOD return_info.

  ENDMETHOD.


  METHOD set_data_init.

    _select_setting( ).

    _check_company_code( ).

    _build_re_accounts( ).

    _get_account_text( ).

    _get_field_text( ).

    _build_ifm_fsv_layout( ).

*// FSV Layout / T-Code : FSE3
    _build_fsv_layout( ).

    _build_currency( ).

  ENDMETHOD.


  METHOD _build_currency.

*// Check currency key
    mv_inter_waers = zcl_flifm_selection=>get_waers( ).

    IF mv_inter_waers IS INITIAL.
      zcx_flifm_exception=>raise_t100( iv_msgno = 006 ).
    ENDIF.

*// Get the set exchange rate.
    DATA: lv_gjahr     TYPE gjahr,
          lv_cmp_gjahr TYPE gjahr,
          lv_monat     TYPE monat.

    lv_gjahr = zcl_flifm_selection=>get_gjahr( ).
    lv_cmp_gjahr = zcl_flifm_selection=>get_cmp_gjahr( ).
    lv_monat = zcl_flifm_selection=>get_monat( ).

    SELECT * INTO CORRESPONDING FIELDS OF TABLE mt_tcurr
      FROM zflifmt_tcurr
      WHERE gjahr IN (lv_gjahr, lv_cmp_gjahr)
    AND monat IN (lv_monat, '00').

    IF sy-subrc <> 0.
*-- If not set intetgrated currency....
*      zcx_flifm_exception=>raise_t100( iv_msgno = 008 ).
    ENDIF.

    DATA: lv_tdec   TYPE currdec,
          lv_fdec   TYPE currdec,
          lv_tmpdec TYPE i.

    FIELD-SYMBOLS: <ls_tcurr>     LIKE LINE OF mt_tcurr,
                   <ls_opp_tcurr> LIKE LINE OF mt_tcurr.

    LOOP AT mt_tcurr ASSIGNING <ls_tcurr>.

      CLEAR : lv_fdec, lv_tdec.

      <ls_tcurr>-ukurs = <ls_tcurr>-trate / <ls_tcurr>-frate.

      SELECT SINGLE currdec INTO lv_fdec
              FROM tcurx WHERE currkey = <ls_tcurr>-fcurr.

      IF sy-subrc <> 0.
        lv_fdec = 2.
      ENDIF.

      SELECT SINGLE currdec INTO lv_tdec
              FROM tcurx WHERE currkey = <ls_tcurr>-tcurr.

      IF sy-subrc <> 0.
        lv_tdec = 2.
      ENDIF.

      IF lv_fdec <> lv_tdec AND lv_fdec <> 0.
        lv_tmpdec = 10 ** lv_fdec.
        <ls_tcurr>-ukurs = <ls_tcurr>-ukurs / lv_tmpdec.
      ENDIF.

    ENDLOOP.

*// Set input currecny to reverse.- Except for manual input.
    DATA: ls_tcurr LIKE LINE OF mt_tcurr.

    LOOP AT mt_tcurr ASSIGNING <ls_tcurr>.

      MOVE-CORRESPONDING <ls_tcurr> TO ls_tcurr.

      READ TABLE mt_tcurr TRANSPORTING NO FIELDS
        WITH KEY monat = ls_tcurr-monat fcurr = ls_tcurr-tcurr tcurr = ls_tcurr-fcurr.

      IF sy-subrc NE 0.

        APPEND INITIAL LINE TO mt_tcurr ASSIGNING <ls_opp_tcurr>.

        CLEAR : lv_fdec, lv_tdec.

        <ls_opp_tcurr>-gjahr = <ls_tcurr>-gjahr.
        <ls_opp_tcurr>-monat = <ls_tcurr>-monat.
        <ls_opp_tcurr>-fcurr = <ls_tcurr>-tcurr.
        <ls_opp_tcurr>-tcurr = <ls_tcurr>-fcurr.
        <ls_opp_tcurr>-frate = <ls_tcurr>-trate.
        <ls_opp_tcurr>-trate = <ls_tcurr>-frate.

        <ls_opp_tcurr>-ukurs = <ls_opp_tcurr>-trate / <ls_opp_tcurr>-frate.

        SELECT SINGLE currdec INTO lv_fdec
                FROM tcurx WHERE currkey = <ls_opp_tcurr>-fcurr.
        IF sy-subrc <> 0.
          lv_fdec = 2.
        ENDIF.

        SELECT SINGLE currdec INTO lv_tdec
                FROM tcurx WHERE currkey = <ls_opp_tcurr>-tcurr.
        IF sy-subrc <> 0.
          lv_tdec = 2.
        ENDIF.

        IF lv_fdec <> lv_tdec AND lv_fdec <> 0.
          lv_tmpdec = 10 ** lv_fdec.
          <ls_opp_tcurr>-ukurs = <ls_opp_tcurr>-ukurs /  lv_tmpdec.
        ENDIF.

      ENDIF.

    ENDLOOP.

*// Create lines with FCUURR = TCURR
    LOOP AT mt_company INTO ms_company.

      APPEND INITIAL LINE TO mt_tcurr ASSIGNING <ls_tcurr>.

      <ls_tcurr>-gjahr = lv_gjahr.
      <ls_tcurr>-monat = lv_monat.
      <ls_tcurr>-tcurr = <ls_tcurr>-fcurr = ms_company-waers.
      <ls_tcurr>-ukurs = '1.00'.

      APPEND INITIAL LINE TO mt_tcurr ASSIGNING <ls_tcurr>.

      <ls_tcurr>-gjahr = lv_gjahr.
      <ls_tcurr>-monat = '00'.
      <ls_tcurr>-tcurr = <ls_tcurr>-fcurr = ms_company-waers.
      <ls_tcurr>-ukurs = '1.00'.

      APPEND INITIAL LINE TO mt_tcurr ASSIGNING <ls_tcurr>.

      <ls_tcurr>-gjahr = lv_cmp_gjahr.
      <ls_tcurr>-monat = lv_monat.
      <ls_tcurr>-tcurr = <ls_tcurr>-fcurr = ms_company-waers.
      <ls_tcurr>-ukurs = '1.00'.

      APPEND INITIAL LINE TO mt_tcurr ASSIGNING <ls_tcurr>.

      <ls_tcurr>-gjahr = lv_cmp_gjahr.
      <ls_tcurr>-monat = '00'.
      <ls_tcurr>-tcurr = <ls_tcurr>-fcurr = ms_company-waers.
      <ls_tcurr>-ukurs = '1.00'.

    ENDLOOP.

    SORT mt_tcurr BY gjahr monat fcurr tcurr.

  ENDMETHOD.


  METHOD _build_fsv_layout.

    mt_ifm_node_tab_bs = zcl_flifm_fsv=>get_fsv_tree(
                                          it_layout = mt_layout
                                          iv_menu = zif_flifm_definitions=>c_flifm_menu_type-bs
                                          iv_versn = zcl_flifm_selection=>get_versn( ) ).

    mt_ifm_node_tab_pl = zcl_flifm_fsv=>get_fsv_tree(
                                          it_layout = mt_layout
                                          iv_menu = zif_flifm_definitions=>c_flifm_menu_type-pl
                                          iv_versn = zcl_flifm_selection=>get_versn( ) ).

    mt_ifm_node_tab_tb = zcl_flifm_fsv=>get_fsv_tree(
                                          it_layout = mt_layout
                                          iv_menu = zif_flifm_definitions=>c_flifm_menu_type-tb
                                          iv_versn = zcl_flifm_selection=>get_versn( ) ).

  ENDMETHOD.


  METHOD _build_ifm_fsv_layout.


*-> Financial Statement Version / T-Code : FSE3
*-- If you want to see the item keys, go to Menu: Settings-Change.
*-- Check Item keys visible.
*-- If 'Item keys visible' is disable, your fsv is not automatically allocate item keys.
*-- Check table T011(Financial Statement Versions). Field: XAUTO

    DATA: ls_layout LIKE LINE OF mt_layout.

    DATA lv_versn TYPE versn_011.
    DATA ls_saved_layout TYPE zif_flifm_definitions=>ty_saved_layout.

    lv_versn = zcl_flifm_selection=>get_versn( ).

    SELECT SINGLE * INTO ms_saved_layout
      FROM zflifmt_layout
      WHERE versn = lv_versn.

    IF sy-subrc <> 0.
      zcx_flifm_exception=>raise_t100( iv_msgno = 009 ).
    ENDIF.

    ls_layout-item = zif_flifm_definitions=>c_flifm_menu_type-bs.
    ls_layout-name = ms_saved_layout-assets.
    APPEND ls_layout TO mt_layout.
    ls_layout-item = zif_flifm_definitions=>c_flifm_menu_type-tb.
    APPEND ls_layout TO mt_layout.

    CLEAR ls_layout.
    ls_layout-item = zif_flifm_definitions=>c_flifm_menu_type-bs.
    ls_layout-name = ms_saved_layout-liab_equity.
    APPEND ls_layout TO mt_layout.
    ls_layout-item = zif_flifm_definitions=>c_flifm_menu_type-tb.
    APPEND ls_layout TO mt_layout.

    CLEAR ls_layout.
    ls_layout-item = zif_flifm_definitions=>c_flifm_menu_type-pl.
    ls_layout-name = ms_saved_layout-pl.
    APPEND ls_layout TO mt_layout.
    ls_layout-item = zif_flifm_definitions=>c_flifm_menu_type-tb.
    APPEND ls_layout TO mt_layout.

    IF ms_saved_layout-etc IS NOT INITIAL.
      CLEAR ls_layout.
      ls_layout-item = zif_flifm_definitions=>c_flifm_menu_type-bs.
      ls_layout-name = ms_saved_layout-etc.
      APPEND ls_layout TO mt_layout.
      ls_layout-item = zif_flifm_definitions=>c_flifm_menu_type-tb.
      APPEND ls_layout TO mt_layout.
    ENDIF.

    SORT mt_layout BY item.


  ENDMETHOD.


  METHOD _build_re_accounts.


    DATA: ls_t030 LIKE LINE OF mt_t030,
          lt_ska1 TYPE STANDARD TABLE OF ska1 WITH DEFAULT KEY,
          ls_ska1 LIKE LINE OF lt_ska1,
          ls_re   TYPE tys_re.

    DATA: lv_ktopl TYPE ktopl.

    lv_ktopl = zcl_flifm_selection=>get_ktopl( ).

    SELECT *
      INTO CORRESPONDING FIELDS OF TABLE mt_t030
      FROM t030
      WHERE ktopl = lv_ktopl
      AND ktosl = 'BIL'.

    SELECT *
      INTO CORRESPONDING FIELDS OF TABLE lt_ska1
      FROM ska1
      WHERE ktopl = lv_ktopl
      AND xbilk = space.

    LOOP AT lt_ska1 INTO ls_ska1.

      MOVE-CORRESPONDING ls_ska1 TO ls_re.

      CLEAR ls_t030.
      READ TABLE mt_t030 INTO ls_t030 WITH KEY komok = ls_ska1-gvtyp.

      IF sy-subrc = 0.
        ls_re-komok = ls_t030-komok.
        ls_re-konts = ls_t030-konts.
      ENDIF.

      INSERT ls_re INTO TABLE mt_re.

    ENDLOOP.


  ENDMETHOD.


  METHOD _check_company_code.

    DATA: lr_bukrs TYPE zcl_flifm_selection=>tyr_bukrs.
    DATA: lv_ktopl TYPE ktopl.

    lv_ktopl = zcl_flifm_selection=>get_ktopl( ).
    lr_bukrs = zcl_flifm_selection=>get_bukrs( ).

    SELECT bukrs butxt land1 waers ktopl
      FROM t001
    INTO CORRESPONDING FIELDS OF TABLE mt_company
      WHERE bukrs IN lr_bukrs
      AND ktopl = lv_ktopl.

    IF sy-subrc <> 0.
      zcx_flifm_exception=>raise_t100( iv_msgno = 005 ).
    ENDIF.

  ENDMETHOD.


  METHOD _get_account_text.

    DATA: lv_ktopl TYPE ktopl.
    DATA: lr_bukrs TYPE zcl_flifm_selection=>tyr_bukrs.

    lv_ktopl = zcl_flifm_selection=>get_ktopl( ).
    lr_bukrs = zcl_flifm_selection=>get_bukrs( ).

    SELECT DISTINCT b~saknr b~txt50
      INTO TABLE mt_skat
     FROM t001 AS a INNER JOIN skat AS b ON a~ktopl = b~ktopl
      WHERE b~spras = sy-langu
      AND a~bukrs IN lr_bukrs
      AND a~ktopl = lv_ktopl.

    SORT mt_skat.

  ENDMETHOD.


  METHOD _get_field_text.

    SELECT * INTO TABLE mt_dd03t
         FROM dd03t
        WHERE tabname    LIKE 'ZFLIFM%'
          AND as4local   = 'A'
          AND ddlanguage = sy-langu.

    IF sy-subrc <> 0.
      SELECT * INTO TABLE mt_dd03t
               FROM dd03t
              WHERE tabname    LIKE 'ZFLIFM%'
                AND as4local   = 'A'
                AND ddlanguage = 'E'.
    ENDIF.

    SORT mt_dd03t BY tabname fieldname.


  ENDMETHOD.


  METHOD _select_setting.


    DATA: ls_setting TYPE zflifmt_setting.

    SELECT SINGLE * INTO CORRESPONDING FIELDS OF ls_setting
      FROM zflifmt_setting.

    IF sy-subrc = 0.

      zcl_flifm_selection=>set_data(
        iv_ktopl     = ls_setting-ktopl
        iv_versn     = ls_setting-versn
        iv_waers     = ls_setting-waers
        iv_to_period = ls_setting-to_period
        iv_parallel  = ls_setting-parallel ).

    ELSE.
      zcx_flifm_exception=>raise_t100( iv_msgno = 011 ).
    ENDIF.


  ENDMETHOD.
ENDCLASS.