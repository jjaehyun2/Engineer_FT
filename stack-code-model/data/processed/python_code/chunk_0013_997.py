class ZCL_MDG_BP_HELPER definition
  public
  create protected

  global friends ZCL_MDG_BP_HELPER_STAGING .

public section.

  interfaces IF_MDG_BP_CONSTANTS .
  interfaces IF_MDG_BS_ECC_BP_CONSTANTS .

  constants:
    BEGIN OF sgc_attribute,
        ad_nation  TYPE usmd_fieldname VALUE 'AD_NATION',
        building   TYPE usmd_fieldname VALUE 'BUILDING',
        chckstatu  TYPE usmd_fieldname VALUE 'CHCKSTATU',
        co_name    TYPE usmd_fieldname VALUE 'CO_NAME',
        cty_code   TYPE usmd_fieldname VALUE 'CTY_CODE',
        district   TYPE usmd_fieldname VALUE 'DISTRICT',
        dlvsrv_nr  TYPE usmd_fieldname VALUE 'DLVSRV_NR',
        dlvsrv_ty  TYPE usmd_fieldname VALUE 'DLVSRV_TY',
        dontuse_p  TYPE usmd_fieldname VALUE 'DONTUSE_P',
        dontuse_s  TYPE usmd_fieldname VALUE 'DONTUSE_S',
        flaggroup  TYPE usmd_fieldname VALUE 'FLAGGROUP',
        floor      TYPE usmd_fieldname VALUE 'FLOOR',
        home_city  TYPE usmd_fieldname VALUE 'HOME_CITY',
        house_nr2  TYPE usmd_fieldname VALUE 'HOUSE_NR2',
        langu_com  TYPE usmd_fieldname VALUE 'LANGU_COM',
        location   TYPE usmd_fieldname VALUE 'LOCATION',
        pers_addr  TYPE usmd_fieldname VALUE 'PERS_ADDR',
        pobox_cty  TYPE usmd_fieldname VALUE 'POBOX_CTY',
        pobox_lby  TYPE usmd_fieldname VALUE 'POBOX_LBY',
        pobox_loc  TYPE usmd_fieldname VALUE 'POBOX_LOC',
        pobox_num  TYPE usmd_fieldname VALUE 'POBOX_NUM',
        post_cod3  TYPE usmd_fieldname VALUE 'POST_COD3',
        ref_posta  TYPE usmd_fieldname VALUE 'REF_POSTA',
        ref_pstal  TYPE usmd_fieldname VALUE 'REF_PSTAL',
        rfe_posta  TYPE usmd_fieldname VALUE 'RFE_POSTA',
        rfe_postl  TYPE usmd_fieldname VALUE 'RFE_POSTL',
        rfe_pstal  TYPE usmd_fieldname VALUE 'RFE_PSTAL',
        rf_postal  TYPE usmd_fieldname VALUE 'RF_POSTAL',
        roomnum    TYPE usmd_fieldname VALUE 'ROOMNUM',
        sort1_ad   TYPE usmd_fieldname VALUE 'SORT1_AD',
        sort2_ad   TYPE usmd_fieldname VALUE 'SORT2_AD',
        strsuppl1  TYPE usmd_fieldname VALUE 'STRSUPPL1',
        strsuppl2  TYPE usmd_fieldname VALUE 'STRSUPPL2',
        strsuppl3  TYPE usmd_fieldname VALUE 'STRSUPPL3',
        taxjurcod  TYPE usmd_fieldname VALUE 'TAXJURCOD',
        time_zone  TYPE usmd_fieldname VALUE 'TIME_ZONE',
        name_org1  TYPE usmd_fieldname VALUE 'NAME_ORG1',
        name_org2  TYPE usmd_fieldname VALUE 'NAME_ORG2',
        name_org3  TYPE usmd_fieldname VALUE 'NAME_ORG3',
        name_org4  TYPE usmd_fieldname VALUE 'name_Org4',
        name_grp1  TYPE usmd_fieldname VALUE 'NAME_GRP1',
        name_grp2  TYPE usmd_fieldname VALUE 'NAME_GRP2',
        name_first TYPE usmd_fieldname VALUE 'NAM_FIRST',
        name_last  TYPE usmd_fieldname VALUE 'NAME_LAST',
        house_num1 TYPE usmd_fieldname VALUE 'HOUSE_NUM1',
        street     TYPE usmd_fieldname VALUE 'STREET',
        post_cod1  TYPE usmd_fieldname VALUE 'POST_COD1',
        city1      TYPE usmd_fieldname VALUE 'CITY1',
        city2      TYPE usmd_fieldname VALUE 'CITY2',
        bp_tx_type TYPE usmd_fieldname  VALUE 'BP_TX_TYPE',
        bp_rol_id  TYPE usmd_fieldname  VALUE 'BP_ROL_ID',
        bp_indsct  TYPE usmd_fieldname  VALUE 'BP_INDSCT',
        bp_indsys  TYPE usmd_fieldname  VALUE 'BP_INDSYS',
        bp_idtype  TYPE usmd_fieldname  VALUE 'BP_IDTYPE',
        bp_id_num  TYPE usmd_fieldname  VALUE 'BP_ID_NUM',
        ven_langu  TYPE usmd_fieldname  VALUE 'VEN_LANGU',
        venlangu   TYPE usmd_fieldname  VALUE 'VENLANGU',
        ven_tdid   TYPE usmd_fieldname  VALUE 'VEN_TDID',
        koart      TYPE usmd_fieldname  VALUE 'KOART',
        taxgr      TYPE usmd_fieldname  VALUE 'TAXGR',
        yyvstel    TYPE usmd_fieldname  VALUE 'YYVSTEL', "to be adjusted project based
      END OF sgc_attribute .
  constants:
    BEGIN OF sgc_bu_grp,
        bu_grp_yic TYPE bu_group  VALUE 'YIC', "to be adjusted project based
        bu_grp_yst TYPE bu_group  VALUE 'YST', "to be adjusted project based
        bu_grp_ycp TYPE bu_group  VALUE 'YCP', "to be adjusted project based
      END OF sgc_bu_grp .
  constants:
    BEGIN OF sgc_bp_business_activities,
        create_customer TYPE usmd_process VALUE 'CUP1',
        change_customer TYPE usmd_process VALUE 'CUP2',
        block_customer  TYPE usmd_process VALUE 'CUP5',
        delete_customer TYPE usmd_process VALUE 'CUP6',
        create_supplier TYPE usmd_process VALUE 'SUP1',
        change_supplier TYPE usmd_process VALUE 'SUP2',
        block_supplier  TYPE usmd_process VALUE 'SUP5',
        delete_supplier TYPE usmd_process VALUE 'SUP6',
        create_bp       TYPE usmd_process VALUE 'BPP1',
        change_bp       TYPE usmd_process VALUE 'BPP2',
        block_bp        TYPE usmd_process VALUE 'BPP5',
        delete_bp       TYPE usmd_process VALUE 'BPP6',
      END OF sgc_bp_business_activities .
  constants:
    BEGIN OF sgc_bp_bi_bp_roles,
        customer          TYPE bu_partnerrole VALUE 'YBIRCU', "to be adjusted project based
        basic_vendor      TYPE bu_partnerrole VALUE 'YBIRBV', "to be adjusted project based
        financial_vendor  TYPE bu_partnerrole VALUE 'YBIRFV', "to be adjusted project based
        purchasing_vendor TYPE bu_partnerrole VALUE 'YBIRPV', "to be adjusted project based
        manufacturer      TYPE bu_partnerrole VALUE 'YBIRMA', "to be adjusted project based
      END OF sgc_bp_bi_bp_roles .
  constants:
    BEGIN OF sgc_bp_role_abr,
        customer          TYPE char2 VALUE 'CU',
        basic_vendor      TYPE char2 VALUE 'BV',
        financial_vendor  TYPE char2 VALUE 'FV',
        purchasing_vendor TYPE char2 VALUE 'PV',
        manufacturer      TYPE char2 VALUE 'MA',
      END OF sgc_bp_role_abr .
  constants:
    BEGIN OF sgc_cr_abr,
        cus_creat TYPE char3 VALUE 'CCR',
        cus_chan  TYPE char3 VALUE 'CCH',
        cus_bloc  TYPE char3 VALUE 'CBL',
        cus_dele  TYPE char3 VALUE 'CDE',
        ven_creat TYPE char3 VALUE 'VCR',
        ven_chan  TYPE char3 VALUE 'VCH',
        ven_bloc  TYPE char3 VALUE 'VBL',
        ven_dele  TYPE char3 VALUE 'VDE',
      END OF sgc_cr_abr .
  constants:
    BEGIN OF sgc_bp_template_category,
        customer TYPE char1  VALUE 'C', "to be adjusted project based
        vendor   TYPE char1  VALUE 'S', "to be adjusted project based
      END OF sgc_bp_template_category .

  methods COMPARE_INSTANCE
    importing
      !IO_BUPA_DATA type ref to ZCL_MDG_BP_HELPER
    exporting
      !ET_CHANGED_ENTITIES type ZIF_MDG_DATATYPES=>GTY_T_ENTITY_DATA
      !ET_DELETED_ENTITIES type ZIF_MDG_DATATYPES=>GTY_T_ENTITY_DATA
      !ET_CHANGED_FIELDS type ZIF_MDG_DATATYPES=>GTY_T_ENTITY_ATTRIBUTE .
  methods COMPARE_INSTANCE_NEW
    importing
      !IO_BUPA_DATA type ref to ZCL_MDG_BP_HELPER
    exporting
      !ET_CHANGED_ENTITIES type ZIF_MDG_DATATYPES=>GTY_T_ENTITY_DATA
      !ET_DELETED_ENTITIES type ZIF_MDG_DATATYPES=>GTY_T_ENTITY_DATA
      !ET_CHANGED_FIELDS type ZIF_MDG_DATATYPES=>GTY_T_ENTITY_ATTRIBUTE .
  methods CONSTRUCTOR .
  methods COPY_INSTANCE
    returning
      value(RO_BUPA_DATA) type ref to ZCL_MDG_BP_HELPER
    exceptions
      ATTRIBUTE_ASSIGNMENT_ERROR
      VALUE_TRANSFER_ERROR .
  methods MERGE_INSTANCE
    importing
      !IO_BP_DATA type ref to ZCL_MDG_BP_HELPER .
  methods DEL_ADDRESS
    importing
      !IT_ADDRESS type ZIF_MDG_BP_DATATYPES=>GTY_T_ADDRESS .
  methods DEL_ADDRNO
    importing
      !IT_ADDRNO type ZIF_MDG_BP_DATATYPES=>GTY_T_ADDRNO .
  methods DEL_AD_EMAIL
    importing
      !IT_AD_EMAIL type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_EMAIL .
  methods DEL_AD_FAX
    importing
      !IT_AD_FAX type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_FAX .
  methods DEL_AD_NAME_O
    importing
      !IT_AD_NAME_O type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_NAME_O .
  methods DEL_AD_NAME_P
    importing
      !IT_AD_NAME_P type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_NAME_P .
  methods DEL_AD_POSTAL
    importing
      !IT_AD_POSTAL type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_POSTAL .
  methods DEL_AD_TEL
    importing
      !IT_AD_TEL type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_TEL .
  methods DEL_AD_URL
    importing
      !IT_AD_URL type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_URL .
  methods DEL_BP_ADDR
    importing
      !IT_BP_ADDR type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_ADDR .
  methods DEL_BP_ADDUSG
    importing
      !IT_BP_ADDUSG type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_ADDUSG .
  methods DEL_BP_BKDTL
    importing
      !IT_BP_BKDTL type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_BKDTL .
  methods DEL_BP_CCDTL
    importing
      !IT_BP_CCDTL type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CCDTL .
  methods DEL_BP_CENTRL
    importing
      !IT_BP_CENTRL type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CENTRL .
  methods DEL_BP_COMPNY
    importing
      !IT_BP_COMPNY type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_COMPNY .
  methods DEL_BP_CPGEN
    importing
      !IT_BP_CPGEN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CPGEN .
  methods DEL_BP_CUSCLA
    importing
      !IT_BP_CUSCLA type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSCLA .
  methods DEL_BP_CUSDDB
    importing
      !IT_BP_CUSDDB type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSDDB .
  methods DEL_BP_CUSDUN
    importing
      !IT_BP_CUSDUN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSDUN .
  methods DEL_BP_CUSFCN
    importing
      !IT_BP_CUSFCN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSFCN .
  methods DEL_BP_CUSGEN
    importing
      !IT_BP_CUSGEN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSGEN .
  methods DEL_BP_CUSTAX
    importing
      !IT_BP_CUSTAX type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSTAX .
  methods DEL_BP_CUSULP
    importing
      !IT_BP_CUSULP type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSULP .
  methods DEL_BP_CUSVAL
    importing
      !IT_BP_CUSVAL type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSVAL .
  methods DEL_BP_CUSWHT
    importing
      !IT_BP_CUSWHT type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSWHT .
  methods DEL_BP_CUS_CC
    importing
      !IT_BP_CUS_CC type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUS_CC .
  methods DEL_BP_DUNN
    importing
      !IT_BP_DUNN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_DUNN .
  methods DEL_BP_HEADER
    importing
      !IT_BP_HEADER type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_HEADER .
  methods DEL_BP_HRCHY
    importing
      !IT_BP_HRCHY type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_HRCHY .
  methods DEL_BP_IDNUM
    importing
      !IT_BP_IDNUM type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_IDNUM .
  methods DEL_BP_INDSTR
    importing
      !IT_BP_INDSTR type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_INDSTR .
  methods DEL_BP_MLT_AD
    importing
      !IT_BP_MLT_AD type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_MLT_AD .
  methods DEL_BP_MLT_AS
    importing
      !IT_BP_MLT_AS type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_MLT_AS .
  methods DEL_BP_PORG
    importing
      !IT_BP_PORG type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_PORG .
  methods DEL_BP_PORG2
    importing
      !IT_BP_PORG2 type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_PORG2 .
  methods DEL_BP_REL
    importing
      !IT_BP_REL type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_REL .
  methods DEL_BP_ROLE
    importing
      !IT_BP_ROLE type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_ROLE .
  methods DEL_BP_SALES
    importing
      !IT_BP_SALES type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_SALES .
  methods DEL_BP_SUBHRY
    importing
      !IT_BP_SUBHRY type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_SUBHRY .
  methods DEL_BP_TAXGRP
    importing
      !IT_BP_TAXGRP type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_TAXGRP .
  methods DEL_BP_TAXNUM
    importing
      !IT_BP_TAXNUM type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_TAXNUM .
  methods DEL_BP_VENCLA
    importing
      !IT_BP_VENCLA type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_VENCLA .
  methods DEL_BP_VENDDB
    importing
      !IT_BP_VENDDB type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_VENDDB .
  methods DEL_BP_VENFCN
    importing
      !IT_BP_VENFCN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_VENFCN .
  methods DEL_BP_VENGEN
    importing
      !IT_BP_VENGEN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_VENGEN .
  methods DEL_BP_VENSUB
    importing
      !IT_BP_VENSUB type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_VENSUB .
  methods DEL_BP_VENVAL
    importing
      !IT_BP_VENVAL type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_VENVAL .
  methods DEL_BP_WHTAX
    importing
      !IT_BP_WHTAX type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_WHTAX .
  methods DEL_BP_WPAD
    importing
      !IT_BP_WPAD type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_WPAD .
  methods DEL_CUSCCTXT
    importing
      !IT_CUSCCTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_CUSCCTXT .
  methods DEL_CUSGENTXT
    importing
      !IT_CUSGENTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_CUSGENTXT .
  methods DEL_CUSSALTXT
    importing
      !IT_CUSSALTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_CUSSALTXT .
  methods DEL_FKKLOCKS
    importing
      !IT_FKKLOCKS type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKLOCKS .
  methods DEL_FKKTAXEX
    importing
      !IT_FKKTAXEX type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKTAXEX .
  methods DEL_FKKTXT
    importing
      !IT_FKKTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKTXT .
  methods DEL_FKKVK
    importing
      !IT_FKKVK type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKVK .
  methods DEL_FKKVKCORR
    importing
      !IT_FKKVKCORR type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKVKCORR .
  methods DEL_FKKVKP
    importing
      !IT_FKKVKP type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKVKP .
  methods DEL_FKKVKTD
    importing
      !IT_FKKVKTD type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKVKTD .
  methods DEL_VENCCTXT
    importing
      !IT_VENCCTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_VENCCTXT .
  methods DEL_VENGENTXT
    importing
      !IT_VENGENTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_VENGENTXT .
  methods DEL_VENPOTXT
    importing
      !IT_VENPOTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_VENPOTXT .
  methods DEL_WP_EMAIL
    importing
      !IT_WP_EMAIL type ZIF_MDG_BP_DATATYPES=>GTY_T_WP_EMAIL .
  methods DEL_WP_FAX
    importing
      !IT_WP_FAX type ZIF_MDG_BP_DATATYPES=>GTY_T_WP_FAX .
  methods DEL_WP_POSTAL
    importing
      !IT_WP_POSTAL type ZIF_MDG_BP_DATATYPES=>GTY_T_WP_POSTAL .
  methods DEL_WP_TEL
    importing
      !IT_WP_TEL type ZIF_MDG_BP_DATATYPES=>GTY_T_WP_TEL .
  methods DEL_WP_URL
    importing
      !IT_WP_URL type ZIF_MDG_BP_DATATYPES=>GTY_T_WP_URL .
  methods GET_ADDRESS
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_ADDRESS type ZIF_MDG_BP_DATATYPES=>GTY_T_ADDRESS
      !ES_ADDRESS type /MDGBP/_S_BP_PP_ADDRESS .
  methods GET_ADDRNO
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_ADDRNO type ZIF_MDG_BP_DATATYPES=>GTY_T_ADDRNO
      !ES_ADDRNO type MDG_BS_ADDRNO .
  methods GET_AD_EMAIL
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
      !IV_STD_ADDRESS type XFELD default ABAP_FALSE
    exporting
      !ET_AD_EMAIL type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_EMAIL
      !ES_AD_EMAIL type /MDGBP/_S_BP_PP_AD_EMAIL .
  methods GET_AD_FAX
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
      !IV_STD_ADDRESS type XFELD default ABAP_FALSE
    exporting
      !ET_AD_FAX type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_FAX
      !ES_AD_FAX type /MDGBP/_S_BP_PP_AD_FAX .
  methods GET_AD_NAME_O
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_AD_NAME_O type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_NAME_O
      !ES_AD_NAME_O type /MDGBP/_S_BP_PP_AD_NAME_O .
  methods GET_AD_NAME_P
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_AD_NAME_P type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_NAME_P
      !ES_AD_NAME_P type /MDGBP/_S_BP_PP_AD_NAME_P .
  methods GET_AD_POSTAL
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
      !IV_STD_ADDRESS type XFELD default ABAP_FALSE
    exporting
      !ET_AD_POSTAL type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_POSTAL
      !ES_AD_POSTAL type /MDGBP/_S_BP_PP_AD_POSTAL .
  methods GET_AD_TEL
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
      !IV_STD_ADDRESS type XFELD default ABAP_FALSE
    exporting
      !ET_AD_TEL type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_TEL
      !ES_AD_TEL type /MDGBP/_S_BP_PP_AD_TEL .
  methods GET_AD_URL
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
      !IV_STD_ADDRESS type XFELD default ABAP_FALSE
    exporting
      !ET_AD_URL type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_URL
      !ES_AD_URL type /MDGBP/_S_BP_PP_AD_URL .
  methods GET_ATTRIBUTE_ENTITY
    importing
      !IV_ATTRIBUTE type USMD_ATTRIBUTE
    exporting
      !EV_ENTITY type USMD_ENTITY
    exceptions
      ATTRIBUTE_NOT_FOUND .
  methods GET_ATTRIBUTE_ENTITY_LIST
    exporting
      !ET_ATTRIBUTE_ENTITY_REL type ZIF_MDG_DATATYPES=>GTY_T_ATTRIBUTE_ENTITY_REL .
  methods GET_BP_ADDR
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_ADDR type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_ADDR
      !ES_BP_ADDR type /MDGBP/_S_BP_PP_BP_ADDR .
  methods GET_BP_ADDUSG
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_ADDUSG type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_ADDUSG
      !ES_BP_ADDUSG type /MDGBP/_S_BP_PP_BP_ADDUSG .
  methods GET_BP_BKDTL
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_BKDTL type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_BKDTL
      !ES_BP_BKDTL type /MDGBP/_S_BP_PP_BP_BKDTL .
  methods GET_BP_CCDTL
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_CCDTL type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CCDTL
      !ES_BP_CCDTL type /MDGBP/_S_BP_PP_BP_CCDTL .
  methods GET_BP_CENTRL
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_CENTRL type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CENTRL
      !ES_BP_CENTRL type /MDGBP/_S_BP_PP_BP_CENTRL .
  methods GET_BP_COMPNY
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_COMPNY type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_COMPNY
      !ES_BP_COMPNY type /MDGBPX/_S_BP_PP_BP_COMPNY .
  methods GET_BP_CPGEN
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_CPGEN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CPGEN
      !ES_BP_CPGEN type /MDGBP/_S_BP_PP_BP_CPGEN .
  methods GET_BP_CUSCLA
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_CUSCLA type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSCLA
      !ES_BP_CUSCLA type /MDGBPX/_S_BP_PP_BP_CUSCLA .
  methods GET_BP_CUSDDB
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_CUSDDB type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSDDB
      !ES_BP_CUSDDB type /MDGBPX/_S_BP_PP_BP_CUSDDB .
  methods GET_BP_CUSDUN
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_CUSDUN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSDUN
      !ES_BP_CUSDUN type /MDGBPX/_S_BP_PP_BP_CUSDUN .
  methods GET_BP_CUSFCN
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_CUSFCN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSFCN
      !ES_BP_CUSFCN type /MDGBPX/_S_BP_PP_BP_CUSFCN .
  methods GET_BP_CUSGEN
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_CUSGEN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSGEN
      !ES_BP_CUSGEN type /MDGBPX/_S_BP_PP_BP_CUSGEN .
  methods GET_BP_CUSTAX
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_CUSTAX type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSTAX
      !ES_BP_CUSTAX type /MDGBPX/_S_BP_PP_BP_CUSTAX .
  methods GET_BP_CUSULP
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_CUSULP type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSULP
      !ES_BP_CUSULP type /MDGBPX/_S_BP_PP_BP_CUSULP .
  methods GET_BP_CUSVAL
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_CUSVAL type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSVAL
      !ES_BP_CUSVAL type /MDGBPX/_S_BP_PP_BP_CUSVAL .
  methods GET_BP_CUSWHT
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_CUSWHT type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSWHT
      !ES_BP_CUSWHT type /MDGBPX/_S_BP_PP_BP_CUSWHT .
  methods GET_BP_CUS_CC
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_CUS_CC type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUS_CC
      !ES_BP_CUS_CC type /MDGBPX/_S_BP_PP_BP_CUS_CC .
  methods GET_BP_DUNN
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_DUNN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_DUNN
      !ES_BP_DUNN type /MDGBPX/_S_BP_PP_BP_DUNN .
  methods GET_BP_HEADER
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_HEADER type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_HEADER
      !ES_BP_HEADER type /MDGBP/_S_BP_PP_BP_HEADER .
  methods GET_BP_HRCHY
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_HRCHY type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_HRCHY
      !ES_BP_HRCHY type /MDGBP/_S_BP_PP_BP_HRCHY .
  methods GET_BP_IDNUM
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_IDNUM type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_IDNUM
      !ES_BP_IDNUM type /MDGBP/_S_BP_PP_BP_IDNUM .
  methods GET_BP_INDSTR
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_INDSTR type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_INDSTR
      !ES_BP_INDSTR type /MDGBP/_S_BP_PP_BP_INDSTR .
  methods GET_BP_MLT_AD
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_MLT_AD type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_MLT_AD
      !ES_BP_MLT_AD type /MDGBPX/_S_BP_PP_BP_MLT_AD .
  methods GET_BP_MLT_AS
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_MLT_AS type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_MLT_AS
      !ES_BP_MLT_AS type /MDGBPX/_S_BP_PP_BP_MLT_AS .
  methods GET_BP_PORG
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_PORG type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_PORG
      !ES_BP_PORG type /MDGBPX/_S_BP_PP_BP_PORG .
  methods GET_BP_PORG2
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_PORG2 type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_PORG2
      !ES_BP_PORG2 type /MDGBPX/_S_BP_PP_BP_PORG2 .
  methods GET_BP_REL
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_REL type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_REL
      !ES_BP_REL type /MDGBP/_S_BP_PP_BP_REL .
  methods GET_BP_ROLE
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_ROLE type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_ROLE
      !ES_BP_ROLE type /MDGBP/_S_BP_PP_BP_ROLE .
  methods GET_BP_SALES
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_SALES type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_SALES
      !ES_BP_SALES type /MDGBPX/_S_BP_PP_BP_SALES .
  methods GET_BP_SUBHRY
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_SUBHRY type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_SUBHRY
      !ES_BP_SUBHRY type /MDGBP/_S_BP_PP_BP_SUBHRY .
  methods GET_BP_TAXGRP
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_TAXGRP type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_TAXGRP
      !ES_BP_TAXGRP type /MDGBPX/_S_BP_PP_BP_TAXGRP .
  methods GET_BP_TAXNUM
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_TAXNUM type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_TAXNUM
      !ES_BP_TAXNUM type /MDGBP/_S_BP_PP_BP_TAXNUM .
  methods GET_BP_VENCLA
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_VENCLA type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_VENCLA
      !ES_BP_VENCLA type /MDGBPX/_S_BP_PP_BP_VENCLA .
  methods GET_BP_VENDDB
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_VENDDB type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_VENDDB
      !ES_BP_VENDDB type /MDGBPX/_S_BP_PP_BP_VENDDB .
  methods GET_BP_VENFCN
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_VENFCN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_VENFCN
      !ES_BP_VENFCN type /MDGBPX/_S_BP_PP_BP_VENFCN .
  methods GET_BP_VENGEN
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_VENGEN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_VENGEN
      !ES_BP_VENGEN type /MDGBPX/_S_BP_PP_BP_VENGEN .
  methods GET_BP_VENSUB
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_VENSUB type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_VENSUB
      !ES_BP_VENSUB type /MDGBPX/_S_BP_PP_BP_VENSUB .
  methods GET_BP_VENVAL
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_VENVAL type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_VENVAL
      !ES_BP_VENVAL type /MDGBPX/_S_BP_PP_BP_VENVAL .
  methods GET_BP_WHTAX
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_WHTAX type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_WHTAX
      !ES_BP_WHTAX type /MDGBPX/_S_BP_PP_BP_WHTAX .
  methods GET_BP_WPAD
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BP_WPAD type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_WPAD
      !ES_BP_WPAD type /MDGBP/_S_BP_PP_BP_WPAD .
  methods GET_CUSCCTXT
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_CUSCCTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_CUSCCTXT
      !ES_CUSCCTXT type /MDGBPX/_S_BP_PP_BP_CCCTXT .
  methods GET_CUSGENTXT
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_CUSGENTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_CUSGENTXT
      !ES_CUSGENTXT type /MDGBPX/_S_BP_PP_BP_CUSTXT .
  methods GET_CUSSALTXT
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_CUSSALTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_CUSSALTXT
      !ES_CUSSALTXT type /MDGBPX/_S_BP_PP_BP_CSDTXT .
  methods GET_ENTITY_ATTRIBUTES
    importing
      !IV_ENTITY type USMD_ENTITY
    exporting
      !ET_ENTITY_ATTRIBUTES type USMD_T_ATTRIBUTE
    exceptions
      ENTITY_NOT_FOUND .
  methods GET_ENTITY_ATTRIBUTES_LIST
    exporting
      !ET_ENTITY_ATTRIBUTES type ZIF_MDG_DATATYPES=>GTY_T_ENTITY_ATTRIBUTES_REL .
  methods GET_ENTITY_INFO
    importing
      !IV_ENTITY type USMD_ENTITY
    returning
      value(RS_ENTITY_INFO) type ZIF_MDG_DATATYPES=>GTY_S_ENTITY_INFO
    exceptions
      ENTITY_NOT_FOUND .
  methods GET_ENTITY_INFO_LIST
    returning
      value(RT_ENTITY_INFO) type ZIF_MDG_DATATYPES=>GTY_T_ENTITY_INFO .
  methods GET_FKKLOCKS
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_FKKLOCKS type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKLOCKS
      !ES_FKKLOCKS type /MDGBPX/_S_BP_PP_FKKLOCKS .
  methods GET_FKKTAXEX
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_FKKTAXEX type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKTAXEX
      !ES_FKKTAXEX type /MDGBPX/_S_BP_PP_FKKTAXEX .
  methods GET_FKKTXT
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_FKKTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKTXT
      !ES_FKKTXT type /MDGBPX/_S_BP_PP_FKKTXT .
  methods GET_FKKVK
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_FKKVK type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKVK
      !ES_FKKVK type /MDGBPX/_S_BP_PP_FKKVK .
  methods GET_FKKVKCORR
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_FKKVKCORR type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKVKCORR
      !ES_FKKVKCORR type /MDGBPX/_S_BP_PP_FKKVKCORR .
  methods GET_FKKVKP
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_FKKVKP type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKVKP
      !ES_FKKVKP type /MDGBPX/_S_BP_PP_FKKVKP .
  methods GET_FKKVKTD
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_FKKVKTD type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKVKTD
      !ES_FKKVKTD type /MDGBPX/_S_BP_PP_FKKVKTD .
  methods GET_KEYS_OF_ENTITY
    importing
      !IV_ENTITY type USMD_ENTITY
    exporting
      !ET_ENTITY_KEYS type USMD_T_ENTITY .
  methods GET_KEY_VALUE_TABLE
    importing
      !IV_ENTITY type USMD_ENTITY
      !IS_RECORD type ANY
    exporting
      !ET_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE .
  methods GET_VENCCTXT
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_VENCCTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_VENCCTXT
      !ES_VENCCTXT type /MDGBPX/_S_BP_PP_BP_VCCTXT .
  methods GET_VENGENTXT
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_VENGENTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_VENGENTXT
      !ES_VENGENTXT type /MDGBPX/_S_BP_PP_BP_VENTXT .
  methods GET_VENPOTXT
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_VENPOTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_VENPOTXT
      !ES_VENPOTXT type /MDGBPX/_S_BP_PP_BP_VPOTXT .
  methods GET_WP_EMAIL
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_WP_EMAIL type ZIF_MDG_BP_DATATYPES=>GTY_T_WP_EMAIL
      !ES_WP_EMAIL type /MDGBP/_S_BP_PP_WP_EMAIL .
  methods GET_WP_FAX
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_WP_FAX type ZIF_MDG_BP_DATATYPES=>GTY_T_WP_FAX
      !ES_WP_FAX type /MDGBP/_S_BP_PP_WP_FAX .
  methods GET_WP_POSTAL
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_WP_POSTAL type ZIF_MDG_BP_DATATYPES=>GTY_T_WP_POSTAL
      !ES_WP_POSTAL type /MDGBP/_S_BP_PP_WP_POSTAL .
  methods GET_WP_TEL
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_WP_TEL type ZIF_MDG_BP_DATATYPES=>GTY_T_WP_TEL
      !ES_WP_TEL type /MDGBP/_S_BP_PP_WP_TEL .
  methods GET_WP_URL
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_WP_URL type ZIF_MDG_BP_DATATYPES=>GTY_T_WP_URL
      !ES_WP_URL type /MDGBP/_S_BP_PP_WP_URL .
  methods SET_ADDRESS
    importing
      !IT_ADDRESS type ZIF_MDG_BP_DATATYPES=>GTY_T_ADDRESS .
  methods SET_ADDRNO
    importing
      !IT_ADDRNO type ZIF_MDG_BP_DATATYPES=>GTY_T_ADDRNO .
  methods SET_AD_EMAIL
    importing
      !IT_AD_EMAIL type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_EMAIL .
  methods SET_AD_FAX
    importing
      !IT_AD_FAX type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_FAX .
  methods SET_AD_NAME_O
    importing
      !IT_AD_NAME_O type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_NAME_O .
  methods SET_AD_NAME_P
    importing
      !IT_AD_NAME_P type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_NAME_P .
  methods SET_AD_POSTAL
    importing
      !IT_AD_POSTAL type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_POSTAL .
  methods SET_AD_TEL
    importing
      !IT_AD_TEL type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_TEL .
  methods SET_AD_URL
    importing
      !IT_AD_URL type ZIF_MDG_BP_DATATYPES=>GTY_T_AD_URL .
  methods SET_BP_ADDR
    importing
      !IT_BP_ADDR type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_ADDR .
  methods SET_BP_ADDUSG
    importing
      !IT_BP_ADDUSG type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_ADDUSG .
  methods SET_BP_BKDTL
    importing
      !IT_BP_BKDTL type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_BKDTL .
  methods SET_BP_CCDTL
    importing
      !IT_BP_CCDTL type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CCDTL .
  methods SET_BP_CENTRL
    importing
      !IT_BP_CENTRL type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CENTRL .
  methods SET_BP_COMPNY
    importing
      !IT_BP_COMPNY type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_COMPNY .
  methods SET_BP_CPGEN
    importing
      !IT_BP_CPGEN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CPGEN .
  methods SET_BP_CUSCLA
    importing
      !IT_BP_CUSCLA type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSCLA .
  methods SET_BP_CUSDDB
    importing
      !IT_BP_CUSDDB type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSDDB .
  methods SET_BP_CUSDUN
    importing
      !IT_BP_CUSDUN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSDUN .
  methods SET_BP_CUSFCN
    importing
      !IT_BP_CUSFCN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSFCN .
  methods SET_BP_CUSGEN
    importing
      !IT_BP_CUSGEN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSGEN .
  methods SET_BP_CUSTAX
    importing
      !IT_BP_CUSTAX type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSTAX .
  methods SET_BP_CUSULP
    importing
      !IT_BP_CUSULP type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSULP .
  methods SET_BP_CUSVAL
    importing
      !IT_BP_CUSVAL type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSVAL .
  methods SET_BP_CUSWHT
    importing
      !IT_BP_CUSWHT type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUSWHT .
  methods SET_BP_CUS_CC
    importing
      !IT_BP_CUS_CC type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_CUS_CC .
  methods SET_BP_DUNN
    importing
      !IT_BP_DUNN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_DUNN .
  methods SET_BP_HEADER
    importing
      !IT_BP_HEADER type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_HEADER .
  methods SET_BP_HRCHY
    importing
      !IT_BP_HRCHY type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_HRCHY .
  methods SET_BP_IDNUM
    importing
      !IT_BP_IDNUM type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_IDNUM .
  methods SET_BP_INDSTR
    importing
      !IT_BP_INDSTR type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_INDSTR .
  methods SET_BP_MLT_AD
    importing
      !IT_BP_MLT_AD type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_MLT_AD .
  methods SET_BP_MLT_AS
    importing
      !IT_BP_MLT_AS type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_MLT_AS .
  methods SET_BP_PORG
    importing
      !IT_BP_PORG type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_PORG .
  methods SET_BP_PORG2
    importing
      !IT_BP_PORG2 type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_PORG2 .
  methods SET_BP_REL
    importing
      !IT_BP_REL type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_REL .
  methods SET_BP_ROLE
    importing
      !IT_BP_ROLE type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_ROLE .
  methods SET_BP_SALES
    importing
      !IT_BP_SALES type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_SALES .
  methods SET_BP_SUBHRY
    importing
      !IT_BP_SUBHRY type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_SUBHRY .
  methods SET_BP_TAXGRP
    importing
      !IT_BP_TAXGRP type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_TAXGRP .
  methods SET_BP_TAXNUM
    importing
      !IT_BP_TAXNUM type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_TAXNUM .
  methods SET_BP_VENCLA
    importing
      !IT_BP_VENCLA type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_VENCLA .
  methods SET_BP_VENDDB
    importing
      !IT_BP_VENDDB type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_VENDDB .
  methods SET_BP_VENFCN
    importing
      !IT_BP_VENFCN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_VENFCN .
  methods SET_BP_VENGEN
    importing
      !IT_BP_VENGEN type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_VENGEN .
  methods SET_BP_VENSUB
    importing
      !IT_BP_VENSUB type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_VENSUB .
  methods SET_BP_VENVAL
    importing
      !IT_BP_VENVAL type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_VENVAL .
  methods SET_BP_WHTAX
    importing
      !IT_BP_WHTAX type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_WHTAX .
  methods SET_BP_WPAD
    importing
      !IT_BP_WPAD type ZIF_MDG_BP_DATATYPES=>GTY_T_BP_WPAD .
  methods SET_CUSCCTXT
    importing
      !IT_CUSCCTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_CUSCCTXT .
  methods SET_CUSGENTXT
    importing
      !IT_CUSGENTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_CUSGENTXT .
  methods SET_CUSSALTXT
    importing
      !IT_CUSSALTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_CUSSALTXT .
  methods SET_FKKLOCKS
    importing
      !IT_FKKLOCKS type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKLOCKS .
  methods SET_FKKTAXEX
    importing
      !IT_FKKTAXEX type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKTAXEX .
  methods SET_FKKTXT
    importing
      !IT_FKKTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKTXT .
  methods SET_FKKVK
    importing
      !IT_FKKVK type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKVK .
  methods SET_FKKVKCORR
    importing
      !IT_FKKVKCORR type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKVKCORR .
  methods SET_FKKVKP
    importing
      !IT_FKKVKP type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKVKP .
  methods SET_FKKVKTD
    importing
      !IT_FKKVKTD type ZIF_MDG_BP_DATATYPES=>GTY_T_FKKVKTD .
  methods SET_VENCCTXT
    importing
      !IT_VENCCTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_VENCCTXT .
  methods SET_VENGENTXT
    importing
      !IT_VENGENTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_VENGENTXT .
  methods SET_VENPOTXT
    importing
      !IT_VENPOTXT type ZIF_MDG_BP_DATATYPES=>GTY_T_VENPOTXT .
  methods SET_WP_EMAIL
    importing
      !IT_WP_EMAIL type ZIF_MDG_BP_DATATYPES=>GTY_T_WP_EMAIL .
  methods SET_WP_FAX
    importing
      !IT_WP_FAX type ZIF_MDG_BP_DATATYPES=>GTY_T_WP_FAX .
  methods SET_WP_POSTAL
    importing
      !IT_WP_POSTAL type ZIF_MDG_BP_DATATYPES=>GTY_T_WP_POSTAL .
  methods SET_WP_TEL
    importing
      !IT_WP_TEL type ZIF_MDG_BP_DATATYPES=>GTY_T_WP_TEL .
  methods SET_WP_URL
    importing
      !IT_WP_URL type ZIF_MDG_BP_DATATYPES=>GTY_T_WP_URL .
  PROTECTED SECTION.

    DATA gt_entity_attributes_rel TYPE zif_mdg_datatypes=>gty_t_entity_attributes_rel .
    DATA gt_fkktxt TYPE zif_mdg_bp_datatypes=>gty_t_fkktxt .
    DATA gt_fkkvk TYPE zif_mdg_bp_datatypes=>gty_t_fkkvk .
    DATA gt_fkkvkcorr TYPE zif_mdg_bp_datatypes=>gty_t_fkkvkcorr .
    DATA gt_fkkvkp TYPE zif_mdg_bp_datatypes=>gty_t_fkkvkp .
    DATA gt_fkkvktd TYPE zif_mdg_bp_datatypes=>gty_t_fkkvktd .
    DATA gt_vencctxt TYPE zif_mdg_bp_datatypes=>gty_t_vencctxt .
    DATA gt_vengentxt TYPE zif_mdg_bp_datatypes=>gty_t_vengentxt .
    DATA gt_venpotxt TYPE zif_mdg_bp_datatypes=>gty_t_venpotxt .
    DATA gt_wp_email TYPE zif_mdg_bp_datatypes=>gty_t_wp_email .
    DATA gt_wp_fax TYPE zif_mdg_bp_datatypes=>gty_t_wp_fax .
    DATA gt_wp_postal TYPE zif_mdg_bp_datatypes=>gty_t_wp_postal .
    DATA gt_wp_tel TYPE zif_mdg_bp_datatypes=>gty_t_wp_tel .
    DATA gt_wp_url TYPE zif_mdg_bp_datatypes=>gty_t_wp_url .
    DATA gt_fkktaxex TYPE zif_mdg_bp_datatypes=>gty_t_fkktaxex .
    DATA gt_bp_subhry TYPE zif_mdg_bp_datatypes=>gty_t_bp_subhry .
    DATA gt_bp_taxgrp TYPE zif_mdg_bp_datatypes=>gty_t_bp_taxgrp .
    DATA gt_bp_taxnum TYPE zif_mdg_bp_datatypes=>gty_t_bp_taxnum .
    DATA gt_bp_vencla TYPE zif_mdg_bp_datatypes=>gty_t_bp_vencla .
    DATA gt_bp_venddb TYPE zif_mdg_bp_datatypes=>gty_t_bp_venddb .
    DATA gt_bp_venfcn TYPE zif_mdg_bp_datatypes=>gty_t_bp_venfcn .
    DATA gt_bp_vengen TYPE zif_mdg_bp_datatypes=>gty_t_bp_vengen .
    DATA gt_bp_vensub TYPE zif_mdg_bp_datatypes=>gty_t_bp_vensub .
    DATA gt_bp_venval TYPE zif_mdg_bp_datatypes=>gty_t_bp_venval .
    DATA gt_bp_whtax TYPE zif_mdg_bp_datatypes=>gty_t_bp_whtax .
    DATA gt_bp_wpad TYPE zif_mdg_bp_datatypes=>gty_t_bp_wpad .
    DATA gt_cuscctxt TYPE zif_mdg_bp_datatypes=>gty_t_cuscctxt .
    DATA gt_cusgentxt TYPE zif_mdg_bp_datatypes=>gty_t_cusgentxt .
    DATA gt_cussaltxt TYPE zif_mdg_bp_datatypes=>gty_t_cussaltxt .
    DATA gt_fkklocks TYPE zif_mdg_bp_datatypes=>gty_t_fkklocks .
    DATA gt_bp_mlt_as TYPE zif_mdg_bp_datatypes=>gty_t_bp_mlt_as .
    DATA gt_bp_porg TYPE zif_mdg_bp_datatypes=>gty_t_bp_porg .
    DATA gt_bp_porg2 TYPE zif_mdg_bp_datatypes=>gty_t_bp_porg2 .
    DATA gt_bp_rel TYPE zif_mdg_bp_datatypes=>gty_t_bp_rel .
    DATA gt_bp_role TYPE zif_mdg_bp_datatypes=>gty_t_bp_role .
    DATA gt_bp_sales TYPE zif_mdg_bp_datatypes=>gty_t_bp_sales .
    DATA gt_bp_cusval TYPE zif_mdg_bp_datatypes=>gty_t_bp_cusval .
    DATA gt_bp_cuswht TYPE zif_mdg_bp_datatypes=>gty_t_bp_cuswht .
    DATA gt_bp_cus_cc TYPE zif_mdg_bp_datatypes=>gty_t_bp_cus_cc .
    DATA gt_bp_dunn TYPE zif_mdg_bp_datatypes=>gty_t_bp_dunn .
    DATA gt_bp_header TYPE zif_mdg_bp_datatypes=>gty_t_bp_header .
    DATA gt_bp_hrchy TYPE zif_mdg_bp_datatypes=>gty_t_bp_hrchy .
    DATA gt_bp_idnum TYPE zif_mdg_bp_datatypes=>gty_t_bp_idnum .
    DATA gt_bp_indstr TYPE zif_mdg_bp_datatypes=>gty_t_bp_indstr .
    DATA gt_bp_mlt_ad TYPE zif_mdg_bp_datatypes=>gty_t_bp_mlt_ad .
    DATA gt_bp_cusulp TYPE zif_mdg_bp_datatypes=>gty_t_bp_cusulp .
    DATA gt_bp_custax TYPE zif_mdg_bp_datatypes=>gty_t_bp_custax .
    DATA gt_bp_cusgen TYPE zif_mdg_bp_datatypes=>gty_t_bp_cusgen .
    DATA gt_bp_cusfcn TYPE zif_mdg_bp_datatypes=>gty_t_bp_cusfcn .
    DATA gt_bp_cusdun TYPE zif_mdg_bp_datatypes=>gty_t_bp_cusdun .
    DATA gt_bp_cusddb TYPE zif_mdg_bp_datatypes=>gty_t_bp_cusddb .
    DATA gt_bp_cuscla TYPE zif_mdg_bp_datatypes=>gty_t_bp_cuscla .
    DATA gt_bp_cpgen TYPE zif_mdg_bp_datatypes=>gty_t_bp_cpgen .
    DATA gt_bp_compny TYPE zif_mdg_bp_datatypes=>gty_t_bp_compny .
    DATA gt_bp_centrl TYPE zif_mdg_bp_datatypes=>gty_t_bp_centrl .
    DATA gt_bp_ccdtl TYPE zif_mdg_bp_datatypes=>gty_t_bp_ccdtl .
    DATA gt_bp_bkdtl TYPE zif_mdg_bp_datatypes=>gty_t_bp_bkdtl .
    DATA gt_bp_addusg TYPE zif_mdg_bp_datatypes=>gty_t_bp_addusg .
    DATA gt_bp_addr TYPE zif_mdg_bp_datatypes=>gty_t_bp_addr .
    DATA gt_ad_url TYPE zif_mdg_bp_datatypes=>gty_t_ad_url .
    DATA gt_ad_tel TYPE zif_mdg_bp_datatypes=>gty_t_ad_tel .
    DATA gt_ad_postal TYPE zif_mdg_bp_datatypes=>gty_t_ad_postal .
    DATA gt_ad_name_p TYPE zif_mdg_bp_datatypes=>gty_t_ad_name_p .
    DATA gt_ad_fax TYPE zif_mdg_bp_datatypes=>gty_t_ad_fax .
    DATA gt_addrno TYPE zif_mdg_bp_datatypes=>gty_t_addrno .
    DATA gt_ad_email TYPE zif_mdg_bp_datatypes=>gty_t_ad_email .
    DATA gt_ad_name_o TYPE zif_mdg_bp_datatypes=>gty_t_ad_name_o .
    DATA go_model TYPE REF TO if_usmd_model_ext .
    DATA gt_address TYPE zif_mdg_bp_datatypes=>gty_t_address .

    METHODS get_all_entities
      RETURNING
        VALUE(rt_all_entities) TYPE usmd_t_entity .
    METHODS get_entity_reference
      IMPORTING
        !iv_entity TYPE usmd_entity
      EXPORTING
        !er_entity TYPE REF TO data .
  PRIVATE SECTION.

*  data GT_DEPENDENT_ENTITIES type zif_mdg_datatypes=>gty_T_DEPENDENT_ENTITIES .
    DATA gt_entity_keys TYPE usmd_ts_entity_cont .
    CONSTANTS:
      BEGIN OF gc_bp_model_entity,
        sub_hierarchy TYPE usmd_entity VALUE 'BP_SUBHRY',   "#EC NOTEXT
        fkklocks      TYPE usmd_entity VALUE 'FKKLOCKS',    "#EC NOTEXT
        fkktaxex      TYPE usmd_entity VALUE 'FKKTAXEX',    "#EC NOTEXT
        fkktxt        TYPE usmd_entity VALUE 'FKKTXT',      "#EC NOTEXT
        fkkvk         TYPE usmd_entity VALUE 'FKKVK',       "#EC NOTEXT
        fkkvkcorr     TYPE usmd_entity VALUE 'FKKVKCORR',   "#EC NOTEXT
        fkkvkp        TYPE usmd_entity VALUE 'FKKVKP',      "#EC NOTEXT
        fkkvktd       TYPE usmd_entity VALUE 'FKKVKTD',     "#EC NOTEXT
      END OF gc_bp_model_entity .
    DATA gt_attribute_entity_rel TYPE zif_mdg_datatypes=>gty_t_attribute_entity_rel .
    DATA gt_dependent_entities TYPE zif_mdg_datatypes=>gty_t_dependent_entities .

    METHODS get_where_condition
      IMPORTING
        !it_key_value TYPE zif_mdg_datatypes=>gty_t_key_value
      EXPORTING
        !ev_where     TYPE string .
    METHODS init_entity_attribute_rel
      EXCEPTIONS
        entity_attribute_not_found .
    METHODS init_entity_keys .
    METHODS init_model .
    METHODS limit_key_value_table_entity
      IMPORTING
        !iv_entity    TYPE usmd_entity
        !it_key_value TYPE zif_mdg_datatypes=>gty_t_key_value
      EXPORTING
        !et_key_value TYPE zif_mdg_datatypes=>gty_t_key_value .
ENDCLASS.



CLASS ZCL_MDG_BP_HELPER IMPLEMENTATION.


  METHOD compare_instance.

    DATA:
      ls_changed_entity    TYPE zif_mdg_datatypes=>gty_s_entity_data,
      ls_deleted_entity    TYPE zif_mdg_datatypes=>gty_s_entity_data,
      lt_update_param      TYPE abap_parmbind_tab,
      ls_update_param      TYPE abap_parmbind,
      lr_update_tab        TYPE REF TO data,
      lt_snapshot_param    TYPE abap_parmbind_tab,
      ls_snapshot_param    TYPE abap_parmbind,
      lr_snapshot_tab      TYPE REF TO data,
      lt_orig_data_comp    TYPE TABLE OF abap_simple_componentdescr,
      lt_compare_data_comp TYPE TABLE OF abap_simple_componentdescr,
      ls_changed_field     TYPE zif_mdg_datatypes=>gty_s_entity_attribute.

    FIELD-SYMBOLS:
      <ls_entity_info>       TYPE zif_mdg_datatypes=>gty_s_entity_info,
      <lt_orig_data>         TYPE ANY TABLE,
      <ls_orig_data>         TYPE any,
      <lt_compare_data>      TYPE ANY TABLE,
      <ls_compare_data>      TYPE any,
      <lt_del_data>          TYPE ANY TABLE,
      <lt_chg_data>          TYPE ANY TABLE,
      <ls_orig_data_comp>    TYPE abap_simple_componentdescr,
      <ls_compare_data_comp> TYPE abap_simple_componentdescr,
      <lv_orig_value>        TYPE any,
      <lv_compare_value>     TYPE any,
      <ls_changed_entity>    TYPE zif_mdg_datatypes=>gty_s_entity_data,
      <ls_deleted_entity>    TYPE zif_mdg_datatypes=>gty_s_entity_data.

    CLEAR:
      et_changed_entities,
      et_deleted_entities,
      et_changed_fields.

    LOOP AT get_entity_info_list( ) ASSIGNING <ls_entity_info>.

* Get Entity data from updated BP cache
      CLEAR: ls_update_param , lt_update_param .
      ls_update_param-name = <ls_entity_info>-get_meth_exp_tab.
      ls_update_param-kind = cl_abap_objectdescr=>importing.
      CREATE DATA lr_update_tab TYPE (<ls_entity_info>-tab_type).
      ASSIGN lr_update_tab->* TO <lt_orig_data>.
      IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 000. ENDIF.
      ls_update_param-value = lr_update_tab.
      INSERT ls_update_param INTO TABLE lt_update_param.
      TRY.
          CALL METHOD me->(<ls_entity_info>-get_meth)
            PARAMETER-TABLE
            lt_update_param.
        CATCH cx_sy_dyn_call_error.
          MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 001 WITH <ls_entity_info>-get_meth.
      ENDTRY.

* Get Entity data from snapshot
      CLEAR: ls_snapshot_param , lt_snapshot_param .
      ls_snapshot_param-name = <ls_entity_info>-get_meth_exp_tab.
      ls_snapshot_param-kind = cl_abap_objectdescr=>importing.
      CREATE DATA lr_snapshot_tab TYPE (<ls_entity_info>-tab_type).
      ASSIGN lr_snapshot_tab->* TO <lt_compare_data>.
      IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 000. ENDIF.
      ls_snapshot_param-value = lr_snapshot_tab.
      INSERT ls_snapshot_param INTO TABLE lt_snapshot_param.
      TRY.
          CALL METHOD io_bupa_data->(<ls_entity_info>-get_meth)
            PARAMETER-TABLE
            lt_snapshot_param.
        CATCH cx_sy_dyn_call_error.
          MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 001 WITH <ls_entity_info>-get_meth.
      ENDTRY.

* Process Modifications (Update/Insert)
      CLEAR ls_changed_entity.
      IF <lt_orig_data> <> <lt_compare_data>.
        LOOP AT <lt_orig_data> ASSIGNING <ls_orig_data>. "#EC CI_NESTED
          UNASSIGN <ls_changed_entity>.
          READ TABLE <lt_compare_data> ASSIGNING <ls_compare_data> FROM <ls_orig_data>. "#EC CI_ANYSEQ
          IF sy-subrc IS INITIAL.

* Entry does exist => check for field changes
            lt_orig_data_comp = CAST cl_abap_structdescr( cl_abap_structdescr=>describe_by_data( <ls_orig_data> )
                                                           )->get_included_view( ).
            LOOP AT lt_orig_data_comp ASSIGNING <ls_orig_data_comp>. "#EC CI_NESTED
              ASSIGN COMPONENT <ls_orig_data_comp>-name OF STRUCTURE <ls_orig_data> TO <lv_orig_value>.
              IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 000. ENDIF.
              ASSIGN COMPONENT <ls_orig_data_comp>-name OF STRUCTURE <ls_compare_data> TO <lv_compare_value>.
              IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 000. ENDIF.
              IF <lv_orig_value> <> <lv_compare_value>.
* Difference found => add updated entry
                IF ls_changed_entity IS INITIAL.
                  ls_changed_entity = zcl_mdg_data_utilities=>create_entity_data( iv_entity   = <ls_entity_info>-entity
                                                                                       iv_tab_type = <ls_entity_info>-tab_type ).
                  ASSIGN ls_changed_entity-entity_data->* TO <lt_chg_data>.
                  IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 000. ENDIF.
                  INSERT ls_changed_entity INTO TABLE et_changed_entities.
                ENDIF.
* Add changed entity record
                READ TABLE <lt_chg_data> FROM <ls_orig_data> TRANSPORTING NO FIELDS. "#EC CI_ANYSEQ
                IF sy-subrc <> 0.
                  INSERT <ls_orig_data> INTO TABLE <lt_chg_data>.
                ENDIF.
* Add changed field
                ls_changed_field-entity    = <ls_entity_info>-entity.
                ls_changed_field-attribute = <ls_orig_data_comp>-name.
                CALL METHOD get_key_value_table
                  EXPORTING
                    iv_entity    = <ls_entity_info>-entity
                    is_record    = <ls_orig_data>
                  IMPORTING
                    et_key_value = ls_changed_field-key_value.
                ls_changed_field-value_old = <lv_compare_value>.
                ls_changed_field-value_new = <lv_orig_value>.

* write changed attributes to entry.
                INSERT ls_changed_field INTO TABLE et_changed_fields.

              ENDIF.
            ENDLOOP.
          ELSE.
* Entry not in compare data set => new entry added
            IF ls_changed_entity IS INITIAL.
              ls_changed_entity = zcl_mdg_data_utilities=>create_entity_data( iv_entity   = <ls_entity_info>-entity
                                                                                   iv_tab_type = <ls_entity_info>-tab_type ).
              ASSIGN ls_changed_entity-entity_data->* TO <lt_chg_data>.
              IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 000. ENDIF.
              INSERT ls_changed_entity INTO TABLE et_changed_entities.
            ENDIF.
            INSERT <ls_orig_data> INTO TABLE <lt_chg_data>.
* Add all fields as changed fields
            lt_orig_data_comp = CAST cl_abap_structdescr( cl_abap_structdescr=>describe_by_data( <ls_orig_data> )
                                                          )->get_included_view( ).

            CALL METHOD get_key_value_table
              EXPORTING
                iv_entity    = <ls_entity_info>-entity
                is_record    = <ls_orig_data>
              IMPORTING
                et_key_value = ls_changed_field-key_value.

            LOOP AT lt_orig_data_comp ASSIGNING <ls_orig_data_comp>. "#EC CI_NESTED
              ASSIGN COMPONENT <ls_orig_data_comp>-name OF STRUCTURE <ls_orig_data> TO <lv_orig_value>.
              IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 000. ENDIF.

              ls_changed_field-entity    = <ls_entity_info>-entity.
              ls_changed_field-attribute = <ls_orig_data_comp>-name.
              ls_changed_field-value_new = <lv_orig_value>.

* write changed attributes to entry.
              IF <lv_orig_value> IS INITIAL.
                CONTINUE.
              ENDIF.

              INSERT ls_changed_field INTO TABLE et_changed_fields.
              CLEAR: ls_changed_field-value_new.

            ENDLOOP.
          ENDIF.
        ENDLOOP.

* Process deletions
        CLEAR ls_deleted_entity.
        LOOP AT <lt_compare_data> ASSIGNING <ls_compare_data>. "#EC CI_NESTED
          READ TABLE <lt_orig_data> FROM <ls_compare_data> TRANSPORTING NO FIELDS. "#EC CI_ANYSEQ
          IF sy-subrc <> 0.
* Entry not in original data set => entry deleted
            IF ls_deleted_entity IS INITIAL.
              ls_deleted_entity = zcl_mdg_data_utilities=>create_entity_data( iv_entity   = <ls_entity_info>-entity
                                                                                        iv_tab_type = <ls_entity_info>-tab_type ).
              ASSIGN ls_deleted_entity-entity_data->* TO <lt_del_data>.
              IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 000. ENDIF.
              INSERT ls_deleted_entity INTO TABLE et_deleted_entities.
            ENDIF.
            INSERT <ls_compare_data> INTO TABLE <lt_del_data>.
* Add all fields as changed fields
            lt_compare_data_comp = CAST cl_abap_structdescr( cl_abap_structdescr=>describe_by_data( <ls_compare_data> )
                                                            )->get_included_view( ).

            CALL METHOD get_key_value_table
              EXPORTING
                iv_entity    = <ls_entity_info>-entity
                is_record    = <ls_compare_data>
              IMPORTING
                et_key_value = ls_changed_field-key_value.

            LOOP AT lt_compare_data_comp ASSIGNING <ls_compare_data_comp>. "#EC CI_NESTED
              CLEAR: ls_changed_field-value_old, ls_changed_field-value_new.

              ls_changed_field-entity    = <ls_entity_info>-entity.
              ls_changed_field-attribute = <ls_compare_data_comp>-name.

              INSERT ls_changed_field INTO TABLE et_changed_fields.

            ENDLOOP.
          ENDIF.
        ENDLOOP.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD compare_instance_new.

    DATA:
      lv_del_flg           TYPE wdy_boolean,
      lv_chg_flg           TYPE wdy_boolean,
      ls_changed_entity    TYPE zif_mdg_datatypes=>gty_s_entity_data,
      ls_deleted_entity    TYPE zif_mdg_datatypes=>gty_s_entity_data,
      lt_update_param      TYPE abap_parmbind_tab,
      ls_update_param      TYPE abap_parmbind,
      lr_update_tab        TYPE REF TO data,
      lt_snapshot_param    TYPE abap_parmbind_tab,
      ls_snapshot_param    TYPE abap_parmbind,
      lr_snapshot_tab      TYPE REF TO data,
      lt_orig_data_comp    TYPE TABLE OF abap_simple_componentdescr,
      lt_compare_data_comp TYPE TABLE OF abap_simple_componentdescr,
      ls_changed_field     TYPE zif_mdg_datatypes=>gty_s_entity_attribute.

    FIELD-SYMBOLS:
      <ls_entity_info>       TYPE zif_mdg_datatypes=>gty_s_entity_info,
      <lt_orig_data>         TYPE ANY TABLE,
      <ls_orig_data>         TYPE any,
      <lt_compare_data>      TYPE ANY TABLE,
      <ls_compare_data>      TYPE any,
      <lt_del_data>          TYPE ANY TABLE,
      <lt_chg_data>          TYPE ANY TABLE,
      <ls_orig_data_comp>    TYPE abap_simple_componentdescr,
      <ls_compare_data_comp> TYPE abap_simple_componentdescr,
      <lv_orig_value>        TYPE any,
      <lv_compare_value>     TYPE any,
      <ls_changed_entity>    TYPE zif_mdg_datatypes=>gty_s_entity_data,
      <ls_deleted_entity>    TYPE zif_mdg_datatypes=>gty_s_entity_data.

    CLEAR:
      et_changed_entities,
      et_deleted_entities,
      et_changed_fields.

    LOOP AT get_entity_info_list( ) ASSIGNING <ls_entity_info>.

* Get Entity data from updated BP cache
      CLEAR: ls_update_param , lt_update_param .
      ls_update_param-name = <ls_entity_info>-get_meth_exp_tab.
      ls_update_param-kind = cl_abap_objectdescr=>importing.
      CREATE DATA lr_update_tab TYPE (<ls_entity_info>-tab_type).
      ASSIGN lr_update_tab->* TO <lt_orig_data>.
      IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 000. ENDIF.
      ls_update_param-value = lr_update_tab.
      INSERT ls_update_param INTO TABLE lt_update_param.
      TRY.
          CALL METHOD me->(<ls_entity_info>-get_meth)
            PARAMETER-TABLE
            lt_update_param.
        CATCH cx_sy_dyn_call_error.
          MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 001 WITH <ls_entity_info>-get_meth.
      ENDTRY.

* Get Entity data from snapshot
      CLEAR: ls_snapshot_param , lt_snapshot_param .
      ls_snapshot_param-name = <ls_entity_info>-get_meth_exp_tab.
      ls_snapshot_param-kind = cl_abap_objectdescr=>importing.
      CREATE DATA lr_snapshot_tab TYPE (<ls_entity_info>-tab_type).
      ASSIGN lr_snapshot_tab->* TO <lt_compare_data>.
      IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 000. ENDIF.
      ls_snapshot_param-value = lr_snapshot_tab.
      INSERT ls_snapshot_param INTO TABLE lt_snapshot_param.
      IF NOT io_bupa_data IS INITIAL.
        TRY.
            CALL METHOD io_bupa_data->(<ls_entity_info>-get_meth)
              PARAMETER-TABLE
              lt_snapshot_param.
          CATCH cx_sy_dyn_call_error.
            MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 001 WITH <ls_entity_info>-get_meth.
        ENDTRY.
      ENDIF.

* Process Modifications (Update/Insert)
      CLEAR ls_changed_entity.
      IF <lt_orig_data> <> <lt_compare_data>.
        LOOP AT <lt_orig_data> ASSIGNING <ls_orig_data>. "#EC CI_NESTED
          UNASSIGN <ls_changed_entity>.
          READ TABLE <lt_compare_data> ASSIGNING <ls_compare_data> FROM <ls_orig_data>. "#EC CI_ANYSEQ
          IF sy-subrc IS INITIAL.

* Entry does exist => check for field changes
            lt_orig_data_comp = CAST cl_abap_structdescr( cl_abap_structdescr=>describe_by_data( <ls_orig_data> )
                                                           )->get_included_view( ).
            LOOP AT lt_orig_data_comp ASSIGNING <ls_orig_data_comp>. "#EC CI_NESTED
              ASSIGN COMPONENT <ls_orig_data_comp>-name OF STRUCTURE <ls_orig_data> TO <lv_orig_value>.
              IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 000. ENDIF.
              ASSIGN COMPONENT <ls_orig_data_comp>-name OF STRUCTURE <ls_compare_data> TO <lv_compare_value>.
              IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 000. ENDIF.
              IF <lv_orig_value> <> <lv_compare_value>.
* Difference found => add updated entry
                IF ls_changed_entity IS INITIAL.
                  ls_changed_entity = zcl_mdg_data_utilities=>create_entity_data( iv_entity   = <ls_entity_info>-entity
                                                                                iv_tab_type = <ls_entity_info>-tab_type ).
                  ASSIGN ls_changed_entity-entity_data->* TO <lt_chg_data>.
                  IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 000. ENDIF.
                  INSERT ls_changed_entity INTO TABLE et_changed_entities.
                  READ TABLE et_changed_entities FROM ls_changed_entity ASSIGNING <ls_changed_entity>.
                  IF sy-subrc = 0 AND <ls_changed_entity> IS ASSIGNED.
                    lv_chg_flg = abap_true.
                  ENDIF.
                ENDIF.
* Add changed entity record
                READ TABLE <lt_chg_data> FROM <ls_orig_data> TRANSPORTING NO FIELDS. "#EC CI_ANYSEQ
                IF sy-subrc <> 0.
                  INSERT <ls_orig_data> INTO TABLE <lt_chg_data>.
                ENDIF.
* Add changed field
                ls_changed_field-entity    = <ls_entity_info>-entity.
                ls_changed_field-attribute = <ls_orig_data_comp>-name.
                CALL METHOD get_key_value_table
                  EXPORTING
                    iv_entity    = <ls_entity_info>-entity
                    is_record    = <ls_orig_data>
                  IMPORTING
                    et_key_value = ls_changed_field-key_value.
                ls_changed_field-value_old = <lv_compare_value>.
                ls_changed_field-value_new = <lv_orig_value>.

* write changed attributes to entry.
                IF <ls_changed_entity> IS ASSIGNED AND lv_chg_flg EQ abap_true.
                  INSERT ls_changed_field INTO TABLE <ls_changed_entity>-changed_attributes.
                ENDIF.

                READ TABLE et_changed_fields FROM ls_changed_field TRANSPORTING NO FIELDS.
                IF sy-subrc <> 0.
                  INSERT ls_changed_field INTO TABLE et_changed_fields.
                ENDIF.
              ENDIF.
            ENDLOOP.
          ELSE.
* Entry not in compare data set => new entry added
            IF ls_changed_entity IS INITIAL.
              ls_changed_entity = zcl_mdg_data_utilities=>create_entity_data( iv_entity   = <ls_entity_info>-entity
                                                                                   iv_tab_type = <ls_entity_info>-tab_type ).
              ASSIGN ls_changed_entity-entity_data->* TO <lt_chg_data>.
              IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 000. ENDIF.
              INSERT ls_changed_entity INTO TABLE et_changed_entities.
              READ TABLE et_changed_entities FROM ls_changed_entity ASSIGNING <ls_changed_entity>.
              IF sy-subrc = 0 AND <ls_changed_entity> IS ASSIGNED.
                lv_chg_flg = abap_true.
              ENDIF.
            ENDIF.
            INSERT <ls_orig_data> INTO TABLE <lt_chg_data>.
* Add all fields as changed fields
            lt_orig_data_comp = CAST cl_abap_structdescr( cl_abap_structdescr=>describe_by_data( <ls_orig_data> )
                                                          )->get_included_view( ).
            LOOP AT lt_orig_data_comp ASSIGNING <ls_orig_data_comp>. "#EC CI_NESTED
              ASSIGN COMPONENT <ls_orig_data_comp>-name OF STRUCTURE <ls_orig_data> TO <lv_orig_value>.
              IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 000. ENDIF.

              ls_changed_field-entity    = <ls_entity_info>-entity.
              ls_changed_field-attribute = <ls_orig_data_comp>-name.

* write changed attributes to entry.
              IF <ls_changed_entity> IS ASSIGNED AND lv_chg_flg EQ abap_true.
                INSERT ls_changed_field INTO TABLE <ls_changed_entity>-changed_attributes.
              ENDIF.

              READ TABLE et_changed_fields FROM ls_changed_field TRANSPORTING NO FIELDS.
              IF sy-subrc <> 0.
                IF <lv_orig_value> IS INITIAL.
                  CONTINUE.
                ENDIF.

                INSERT ls_changed_field INTO TABLE et_changed_fields.
              ENDIF.
            ENDLOOP.
          ENDIF.
        ENDLOOP.

* Process deletions
        CLEAR ls_deleted_entity.
        LOOP AT <lt_compare_data> ASSIGNING <ls_compare_data>. "#EC CI_NESTED
          READ TABLE <lt_orig_data> FROM <ls_compare_data> TRANSPORTING NO FIELDS. "#EC CI_ANYSEQ
          IF sy-subrc <> 0.
* Entry not in original data set => entry deleted
            IF ls_deleted_entity IS INITIAL.
              ls_deleted_entity = zcl_mdg_data_utilities=>create_entity_data( iv_entity   = <ls_entity_info>-entity
                                                                              iv_tab_type = <ls_entity_info>-tab_type ).
              ASSIGN ls_deleted_entity-entity_data->* TO <lt_del_data>.
              IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 000. ENDIF.
              INSERT ls_deleted_entity INTO TABLE et_deleted_entities.
              READ TABLE et_deleted_entities FROM ls_deleted_entity ASSIGNING <ls_deleted_entity>.
              IF sy-subrc = 0 AND <ls_deleted_entity> IS ASSIGNED.
                lv_del_flg = abap_true.
              ENDIF.
            ENDIF.
            INSERT <ls_compare_data> INTO TABLE <lt_del_data>.
* Add all fields as changed fields
            lt_compare_data_comp = CAST cl_abap_structdescr( cl_abap_structdescr=>describe_by_data( <ls_compare_data> )
                                                            )->get_included_view( ).
            LOOP AT lt_compare_data_comp ASSIGNING <ls_compare_data_comp>. "#EC CI_NESTED
              ASSIGN COMPONENT <ls_orig_data_comp>-name OF STRUCTURE <ls_orig_data> TO <lv_orig_value>.
              IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 000. ENDIF.

              ls_changed_field-entity    = <ls_entity_info>-entity.
              ls_changed_field-attribute = <ls_orig_data_comp>-name.
              CALL METHOD get_key_value_table
                EXPORTING
                  iv_entity    = <ls_entity_info>-entity
                  is_record    = <ls_orig_data>
                IMPORTING
                  et_key_value = ls_changed_field-key_value.
              CLEAR: ls_changed_field-value_old.
              ls_changed_field-value_new = <lv_orig_value>.

              ls_changed_field-entity    = <ls_entity_info>-entity.
              ls_changed_field-attribute = <ls_compare_data_comp>-name.

              IF <ls_deleted_entity> IS ASSIGNED AND lv_del_flg EQ abap_true.
                INSERT ls_changed_field INTO TABLE <ls_deleted_entity>-changed_attributes.
              ENDIF.

              READ TABLE et_changed_fields FROM ls_changed_field TRANSPORTING NO FIELDS.
              IF sy-subrc <> 0.
                INSERT ls_changed_field INTO TABLE et_changed_fields.
              ENDIF.
            ENDLOOP.
          ENDIF.
        ENDLOOP.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD constructor.

    init_model( ).
    init_entity_keys( ).
    init_entity_attribute_rel( ).

  ENDMETHOD.


  METHOD copy_instance.
    DATA:
       lo_bupa_class_descr TYPE REF TO cl_abap_objectdescr.

    FIELD-SYMBOLS:
      <ls_attribute> TYPE abap_attrdescr,
      <lv_target>    TYPE any,
      <lv_source>    TYPE any.

    CONSTANTS:
      lc_msg000 TYPE symsgno VALUE '000'.

* Initialize object and transfer attributes
    CREATE OBJECT ro_bupa_data.
    lo_bupa_class_descr ?= cl_abap_objectdescr=>describe_by_object_ref( ro_bupa_data ).

* Transfer attributes to new instance
    LOOP AT lo_bupa_class_descr->attributes ASSIGNING <ls_attribute> WHERE is_constant = abap_false. "#EC CI_STDSEQ
      ASSIGN ro_bupa_data->(<ls_attribute>-name) TO <lv_target>.
      IF sy-subrc <> 0.
        CLEAR ro_bupa_data.
        MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_bp TYPE 'X' NUMBER 000 WITH <ls_attribute>-name INTO zcl_mdg_general_functions=>gv_error_message .
        sy-msgid = zcl_mdg_general_functions=>gc_msg_class_dm_bp.
        sy-msgno = lc_msg000.
        sy-msgty = usmd1_cs_msgty-error.
        sy-msgv1 = <ls_attribute>-name.
        RAISE attribute_assignment_error.
      ENDIF.
      ASSIGN me->(<ls_attribute>-name) TO <lv_source>.
      IF sy-subrc <> 0.
        CLEAR ro_bupa_data.
        MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_bp TYPE 'X' NUMBER 000 WITH <ls_attribute>-name INTO zcl_mdg_general_functions=>gv_error_message .
        sy-msgid = zcl_mdg_general_functions=>gc_msg_class_dm_bp.
        sy-msgno = lc_msg000.
        sy-msgty = usmd1_cs_msgty-error.
        sy-msgv1 = <ls_attribute>-name.
        RAISE attribute_assignment_error.
      ENDIF.
      <lv_target> = <lv_source>.
      IF sy-subrc <> 0.
        CLEAR ro_bupa_data.
        MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_bp TYPE 'X' NUMBER 000 WITH <ls_attribute>-name INTO zcl_mdg_general_functions=>gv_error_message .
        sy-msgid = zcl_mdg_general_functions=>gc_msg_class_dm_bp.
        sy-msgno = lc_msg000.
        sy-msgty = usmd1_cs_msgty-error.
        sy-msgv1 = <ls_attribute>-name.
        RAISE attribute_assignment_error.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_address.

    FIELD-SYMBOLS:
      <ls_address> TYPE /mdgbp/_s_bp_pp_address.

    LOOP AT it_address ASSIGNING <ls_address> ##ENH_OK.
      DELETE TABLE gt_address FROM <ls_address>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_addrno.

    FIELD-SYMBOLS:
      <ls_addrno> TYPE mdg_bs_addrno.

    LOOP AT it_addrno ASSIGNING <ls_addrno> ##ENH_OK.
      DELETE TABLE gt_addrno FROM <ls_addrno>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_ad_email.

    FIELD-SYMBOLS:
      <ls_ad_email> TYPE /mdgbp/_s_bp_pp_ad_email.

    LOOP AT it_ad_email ASSIGNING <ls_ad_email> ##ENH_OK.
      DELETE TABLE gt_ad_email FROM <ls_ad_email>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_ad_fax.

    FIELD-SYMBOLS:
      <ls_ad_fax> TYPE /mdgbp/_s_bp_pp_ad_fax.

    LOOP AT it_ad_fax ASSIGNING <ls_ad_fax> ##ENH_OK.
      DELETE TABLE gt_ad_fax FROM <ls_ad_fax>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_ad_name_o.

    FIELD-SYMBOLS:
      <ls_ad_name_o> TYPE /mdgbp/_s_bp_pp_ad_name_o.

    LOOP AT it_ad_name_o ASSIGNING <ls_ad_name_o> ##ENH_OK.
      DELETE TABLE gt_ad_name_o FROM <ls_ad_name_o>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_ad_name_p.

    FIELD-SYMBOLS:
      <ls_ad_name_p> TYPE /mdgbp/_s_bp_pp_ad_name_p.

    LOOP AT it_ad_name_p ASSIGNING <ls_ad_name_p> ##ENH_OK.
      DELETE TABLE gt_ad_name_p FROM <ls_ad_name_p>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_ad_postal.

    FIELD-SYMBOLS:
      <ls_ad_postal> TYPE /mdgbp/_s_bp_pp_ad_postal.

    LOOP AT it_ad_postal ASSIGNING <ls_ad_postal> ##ENH_OK.
      DELETE TABLE gt_ad_postal FROM <ls_ad_postal>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_ad_tel.

    FIELD-SYMBOLS:
      <ls_ad_tel> TYPE /mdgbp/_s_bp_pp_ad_tel.

    LOOP AT it_ad_tel ASSIGNING <ls_ad_tel> ##ENH_OK.
      DELETE TABLE gt_ad_tel FROM <ls_ad_tel>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_ad_url.

    FIELD-SYMBOLS:
      <ls_ad_url> TYPE /mdgbp/_s_bp_pp_ad_url.

    LOOP AT it_ad_url ASSIGNING <ls_ad_url> ##ENH_OK.
      DELETE TABLE gt_ad_url FROM <ls_ad_url>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_addr.

    FIELD-SYMBOLS:
      <ls_bp_addr> TYPE /mdgbp/_s_bp_pp_bp_addr.

    LOOP AT it_bp_addr ASSIGNING <ls_bp_addr> ##ENH_OK.
      DELETE TABLE gt_bp_addr FROM <ls_bp_addr>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_addusg.

    FIELD-SYMBOLS:
      <ls_bp_addusg> TYPE /mdgbp/_s_bp_pp_bp_addusg.

    LOOP AT it_bp_addusg ASSIGNING <ls_bp_addusg> ##ENH_OK.
      DELETE TABLE gt_bp_addusg FROM <ls_bp_addusg>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_bkdtl.

    FIELD-SYMBOLS:
      <ls_bp_bkdtl> TYPE /mdgbp/_s_bp_pp_bp_bkdtl.

    LOOP AT it_bp_bkdtl ASSIGNING <ls_bp_bkdtl> ##ENH_OK.
      DELETE TABLE gt_bp_bkdtl FROM <ls_bp_bkdtl>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_ccdtl.

    FIELD-SYMBOLS:
      <ls_bp_ccdtl> TYPE /mdgbp/_s_bp_pp_bp_ccdtl.

    LOOP AT it_bp_ccdtl ASSIGNING <ls_bp_ccdtl> ##ENH_OK.
      DELETE TABLE gt_bp_ccdtl FROM <ls_bp_ccdtl>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_centrl.

    FIELD-SYMBOLS:
      <ls_bp_centrl> TYPE /mdgbp/_s_bp_pp_bp_centrl.

    LOOP AT it_bp_centrl ASSIGNING <ls_bp_centrl> ##ENH_OK.
      DELETE TABLE gt_bp_centrl FROM <ls_bp_centrl>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_compny.

    FIELD-SYMBOLS:
      <ls_bp_compny> TYPE /mdgbpx/_s_bp_pp_bp_compny.

    LOOP AT it_bp_compny ASSIGNING <ls_bp_compny> ##ENH_OK.
      DELETE TABLE gt_bp_compny FROM <ls_bp_compny>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_cpgen.

    FIELD-SYMBOLS:
      <ls_bp_cpgen> TYPE /mdgbp/_s_bp_pp_bp_cpgen.

    LOOP AT it_bp_cpgen ASSIGNING <ls_bp_cpgen> ##ENH_OK.
      DELETE TABLE gt_bp_cpgen FROM <ls_bp_cpgen>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_cuscla.

    FIELD-SYMBOLS:
      <ls_bp_cuscla> TYPE /mdgbpx/_s_bp_pp_bp_cuscla.

    LOOP AT it_bp_cuscla ASSIGNING <ls_bp_cuscla> ##ENH_OK.
      DELETE TABLE gt_bp_cuscla FROM <ls_bp_cuscla>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_cusddb.

    FIELD-SYMBOLS:
      <ls_bp_cusddb> TYPE /mdgbpx/_s_bp_pp_bp_cusddb.

    LOOP AT it_bp_cusddb ASSIGNING <ls_bp_cusddb> ##ENH_OK.
      DELETE TABLE gt_bp_cusddb FROM <ls_bp_cusddb>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_cusdun.

    FIELD-SYMBOLS:
      <ls_bp_cusdun> TYPE /mdgbpx/_s_bp_pp_bp_cusdun.

    LOOP AT it_bp_cusdun ASSIGNING <ls_bp_cusdun> ##ENH_OK.
      DELETE TABLE gt_bp_cusdun FROM <ls_bp_cusdun>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_cusfcn.

    FIELD-SYMBOLS:
      <ls_bp_cusfcn> TYPE /mdgbpx/_s_bp_pp_bp_cusfcn.

    LOOP AT it_bp_cusfcn ASSIGNING <ls_bp_cusfcn> ##ENH_OK.
      DELETE TABLE gt_bp_cusfcn FROM <ls_bp_cusfcn>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_cusgen.

    FIELD-SYMBOLS:
      <ls_bp_cusgen> TYPE /mdgbpx/_s_bp_pp_bp_cusgen.

    LOOP AT it_bp_cusgen ASSIGNING <ls_bp_cusgen> ##ENH_OK.
      DELETE TABLE gt_bp_cusgen FROM <ls_bp_cusgen>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_custax.

    FIELD-SYMBOLS:
      <ls_bp_custax> TYPE /mdgbpx/_s_bp_pp_bp_custax.

    LOOP AT it_bp_custax ASSIGNING <ls_bp_custax> ##ENH_OK.
      DELETE TABLE gt_bp_custax FROM <ls_bp_custax>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_cusulp.

    FIELD-SYMBOLS:
      <ls_bp_cusulp> TYPE /mdgbpx/_s_bp_pp_bp_cusulp.

    LOOP AT it_bp_cusulp ASSIGNING <ls_bp_cusulp> ##ENH_OK.
      DELETE TABLE gt_bp_cusulp FROM <ls_bp_cusulp>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_cusval.

    FIELD-SYMBOLS:
      <ls_bp_cusval> TYPE /mdgbpx/_s_bp_pp_bp_cusval.

    LOOP AT it_bp_cusval ASSIGNING <ls_bp_cusval> ##ENH_OK.
      DELETE TABLE gt_bp_cusval FROM <ls_bp_cusval>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_cuswht.

    FIELD-SYMBOLS:
      <ls_bp_cuswht> TYPE /mdgbpx/_s_bp_pp_bp_cuswht.

    LOOP AT it_bp_cuswht ASSIGNING <ls_bp_cuswht> ##ENH_OK.
      DELETE TABLE gt_bp_cuswht FROM <ls_bp_cuswht>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_cus_cc.

    FIELD-SYMBOLS:
      <ls_bp_cus_cc> TYPE /mdgbpx/_s_bp_pp_bp_cus_cc.

    LOOP AT it_bp_cus_cc ASSIGNING <ls_bp_cus_cc> ##ENH_OK.
      DELETE TABLE gt_bp_cus_cc FROM <ls_bp_cus_cc>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_dunn.

    FIELD-SYMBOLS:
      <ls_bp_dunn> TYPE /mdgbpx/_s_bp_pp_bp_dunn.

    LOOP AT it_bp_dunn ASSIGNING <ls_bp_dunn> ##ENH_OK.
      DELETE TABLE gt_bp_dunn FROM <ls_bp_dunn>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_header.

    FIELD-SYMBOLS:
      <ls_bp_header> TYPE /mdgbp/_s_bp_pp_bp_header.

    LOOP AT it_bp_header ASSIGNING <ls_bp_header> ##ENH_OK.
      DELETE TABLE gt_bp_header FROM <ls_bp_header>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_hrchy.

    FIELD-SYMBOLS:
      <ls_bp_hrchy> TYPE /mdgbp/_s_bp_pp_bp_hrchy.

    LOOP AT it_bp_hrchy ASSIGNING <ls_bp_hrchy> ##ENH_OK.
      DELETE TABLE gt_bp_hrchy FROM <ls_bp_hrchy>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_idnum.

    FIELD-SYMBOLS:
      <ls_bp_idnum> TYPE /mdgbp/_s_bp_pp_bp_idnum.

    LOOP AT it_bp_idnum ASSIGNING <ls_bp_idnum> ##ENH_OK.
      DELETE TABLE gt_bp_idnum FROM <ls_bp_idnum>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_indstr.

    FIELD-SYMBOLS:
     <ls_bp_indstr> TYPE /mdgbp/_s_bp_pp_bp_indstr.

    LOOP AT it_bp_indstr ASSIGNING <ls_bp_indstr> ##ENH_OK.
      DELETE TABLE gt_bp_indstr FROM <ls_bp_indstr>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_mlt_ad.

    FIELD-SYMBOLS:
      <ls_bp_mlt_ad> TYPE /mdgbpx/_s_bp_pp_bp_mlt_ad.

    LOOP AT it_bp_mlt_ad ASSIGNING <ls_bp_mlt_ad> ##ENH_OK.
      DELETE TABLE gt_bp_mlt_ad FROM <ls_bp_mlt_ad>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_mlt_as.

    FIELD-SYMBOLS:
      <ls_bp_mlt_as> TYPE /mdgbpx/_s_bp_pp_bp_mlt_as.

    LOOP AT it_bp_mlt_as ASSIGNING <ls_bp_mlt_as> ##ENH_OK.
      DELETE TABLE gt_bp_mlt_as FROM <ls_bp_mlt_as>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_porg.

    FIELD-SYMBOLS:
      <ls_bp_porg> TYPE /mdgbpx/_s_bp_pp_bp_porg.

    LOOP AT it_bp_porg ASSIGNING <ls_bp_porg> ##ENH_OK.
      DELETE TABLE gt_bp_porg FROM <ls_bp_porg>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_porg2.

    FIELD-SYMBOLS:
      <ls_bp_porg2> TYPE /mdgbpx/_s_bp_pp_bp_porg2.

    LOOP AT it_bp_porg2 ASSIGNING <ls_bp_porg2> ##ENH_OK.
      DELETE TABLE gt_bp_porg2 FROM <ls_bp_porg2>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_rel.

    FIELD-SYMBOLS:
      <ls_bp_rel> TYPE /mdgbp/_s_bp_pp_bp_rel.

    LOOP AT it_bp_rel ASSIGNING <ls_bp_rel> ##ENH_OK.
      DELETE TABLE gt_bp_rel FROM <ls_bp_rel>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_role.

    FIELD-SYMBOLS:
      <ls_bp_role> TYPE /mdgbp/_s_bp_pp_bp_role.

    LOOP AT it_bp_role ASSIGNING <ls_bp_role> ##ENH_OK.
      DELETE TABLE gt_bp_role FROM <ls_bp_role>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_sales.

    FIELD-SYMBOLS:
      <ls_bp_sales> TYPE /mdgbpx/_s_bp_pp_bp_sales.

    LOOP AT it_bp_sales ASSIGNING <ls_bp_sales> ##ENH_OK.
      DELETE TABLE gt_bp_sales FROM <ls_bp_sales>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_subhry.

    FIELD-SYMBOLS:
      <ls_bp_subhry> TYPE /mdgbp/_s_bp_pp_bp_subhry.

    LOOP AT it_bp_subhry ASSIGNING <ls_bp_subhry> ##ENH_OK.
      DELETE TABLE gt_bp_subhry FROM <ls_bp_subhry>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_taxgrp.

    FIELD-SYMBOLS:
      <ls_bp_taxgrp> TYPE /mdgbpx/_s_bp_pp_bp_taxgrp.

    LOOP AT it_bp_taxgrp ASSIGNING <ls_bp_taxgrp> ##ENH_OK.
      DELETE TABLE gt_bp_taxgrp FROM <ls_bp_taxgrp>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_taxnum.

    FIELD-SYMBOLS:
      <ls_bp_taxnum> TYPE /mdgbp/_s_bp_pp_bp_taxnum.

    LOOP AT it_bp_taxnum ASSIGNING <ls_bp_taxnum> ##ENH_OK.
      DELETE TABLE gt_bp_taxnum FROM <ls_bp_taxnum>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_vencla.

    FIELD-SYMBOLS:
      <ls_bp_vencla> TYPE /mdgbpx/_s_bp_pp_bp_vencla.

    LOOP AT it_bp_vencla ASSIGNING <ls_bp_vencla> ##ENH_OK.
      DELETE TABLE gt_bp_vencla FROM <ls_bp_vencla>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_venddb.

    FIELD-SYMBOLS:
      <ls_bp_venddb> TYPE /mdgbpx/_s_bp_pp_bp_venddb.

    LOOP AT it_bp_venddb ASSIGNING <ls_bp_venddb> ##ENH_OK.
      DELETE TABLE gt_bp_venddb FROM <ls_bp_venddb>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_venfcn.

    FIELD-SYMBOLS:
      <ls_bp_venfcn> TYPE /mdgbpx/_s_bp_pp_bp_venfcn.

    LOOP AT it_bp_venfcn ASSIGNING <ls_bp_venfcn> ##ENH_OK.
      DELETE TABLE gt_bp_venfcn FROM <ls_bp_venfcn>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_vengen.

    FIELD-SYMBOLS:
      <ls_bp_vengen> TYPE /mdgbpx/_s_bp_pp_bp_vengen.

    LOOP AT it_bp_vengen ASSIGNING <ls_bp_vengen> ##ENH_OK.
      DELETE TABLE gt_bp_vengen FROM <ls_bp_vengen>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_vensub.

    FIELD-SYMBOLS:
      <ls_bp_vensub> TYPE /mdgbpx/_s_bp_pp_bp_vensub.

    LOOP AT it_bp_vensub ASSIGNING <ls_bp_vensub> ##ENH_OK.
      DELETE TABLE gt_bp_vensub FROM <ls_bp_vensub>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_venval.

    FIELD-SYMBOLS:
      <ls_bp_venval> TYPE /mdgbpx/_s_bp_pp_bp_venval.

    LOOP AT it_bp_venval ASSIGNING <ls_bp_venval> ##ENH_OK.
      DELETE TABLE gt_bp_venval FROM <ls_bp_venval>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_whtax.

    FIELD-SYMBOLS:
      <ls_bp_whtax> TYPE /mdgbpx/_s_bp_pp_bp_whtax.

    LOOP AT it_bp_whtax ASSIGNING <ls_bp_whtax> ##ENH_OK.
      DELETE TABLE gt_bp_whtax FROM <ls_bp_whtax>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_bp_wpad.

    FIELD-SYMBOLS:
      <ls_bp_wpad> TYPE /mdgbp/_s_bp_pp_bp_wpad.

    LOOP AT it_bp_wpad ASSIGNING <ls_bp_wpad> ##ENH_OK.
      DELETE TABLE gt_bp_wpad FROM <ls_bp_wpad>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_cuscctxt.

    FIELD-SYMBOLS:
      <ls_cuscctxt> TYPE /mdgbpx/_s_bp_pp_bp_ccctxt.

    LOOP AT it_cuscctxt ASSIGNING <ls_cuscctxt> ##ENH_OK.
      DELETE TABLE gt_cuscctxt FROM <ls_cuscctxt>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_cusgentxt.

    FIELD-SYMBOLS:
      <ls_cusgentxt> TYPE /mdgbpx/_s_bp_pp_bp_custxt.

    LOOP AT it_cusgentxt ASSIGNING <ls_cusgentxt> ##ENH_OK.
      DELETE TABLE gt_cusgentxt FROM <ls_cusgentxt>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_cussaltxt.

    FIELD-SYMBOLS:
      <ls_cussaltxt> TYPE /mdgbpx/_s_bp_pp_bp_csdtxt.

    LOOP AT it_cussaltxt ASSIGNING <ls_cussaltxt> ##ENH_OK.
      DELETE TABLE gt_cussaltxt FROM <ls_cussaltxt>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_fkklocks.

    FIELD-SYMBOLS:
      <ls_fkklocks> TYPE /mdgbpx/_s_bp_pp_fkklocks.

    LOOP AT it_fkklocks ASSIGNING <ls_fkklocks> ##ENH_OK.
      DELETE TABLE gt_fkklocks FROM <ls_fkklocks>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_fkktaxex.

    FIELD-SYMBOLS:
      <ls_fkktaxex> TYPE /mdgbpx/_s_bp_pp_fkktaxex.

    LOOP AT it_fkktaxex ASSIGNING <ls_fkktaxex> ##ENH_OK.
      DELETE TABLE gt_fkktaxex FROM <ls_fkktaxex>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_fkktxt.

    FIELD-SYMBOLS:
      <ls_fkktxt> TYPE /mdgbpx/_s_bp_pp_fkktxt.

    LOOP AT it_fkktxt ASSIGNING <ls_fkktxt> ##ENH_OK.
      DELETE TABLE gt_fkktxt FROM <ls_fkktxt>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_fkkvk.

    FIELD-SYMBOLS:
      <ls_fkkvk> TYPE /mdgbpx/_s_bp_pp_fkkvk.

    LOOP AT it_fkkvk ASSIGNING <ls_fkkvk> ##ENH_OK.
      DELETE TABLE gt_fkkvk FROM <ls_fkkvk>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_fkkvkcorr.

    FIELD-SYMBOLS:
      <ls_fkkvkcorr> TYPE /mdgbpx/_s_bp_pp_fkkvkcorr.

    LOOP AT it_fkkvkcorr ASSIGNING <ls_fkkvkcorr> ##ENH_OK.
      DELETE TABLE gt_fkkvkcorr FROM <ls_fkkvkcorr>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_fkkvkp.

    FIELD-SYMBOLS:
      <ls_fkkvkp> TYPE /mdgbpx/_s_bp_pp_fkkvkp.

    LOOP AT it_fkkvkp ASSIGNING <ls_fkkvkp> ##ENH_OK.
      DELETE TABLE gt_fkkvkp FROM <ls_fkkvkp>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_fkkvktd.

    FIELD-SYMBOLS:
      <ls_fkkvktd> TYPE /mdgbpx/_s_bp_pp_fkkvktd.

    LOOP AT it_fkkvktd ASSIGNING <ls_fkkvktd> ##ENH_OK.
      DELETE TABLE gt_fkkvktd FROM <ls_fkkvktd>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_vencctxt.

    FIELD-SYMBOLS:
      <ls_vencctxt> TYPE /mdgbpx/_s_bp_pp_bp_vcctxt.

    LOOP AT it_vencctxt ASSIGNING <ls_vencctxt> ##ENH_OK.
      DELETE TABLE gt_vencctxt FROM <ls_vencctxt>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_vengentxt.

    FIELD-SYMBOLS:
      <ls_vengentxt> TYPE /mdgbpx/_s_bp_pp_bp_ventxt.

    LOOP AT it_vengentxt ASSIGNING <ls_vengentxt> ##ENH_OK.
      DELETE TABLE gt_vengentxt FROM <ls_vengentxt>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_venpotxt.

    FIELD-SYMBOLS:
      <ls_venpotxt> TYPE /mdgbpx/_s_bp_pp_bp_vpotxt.

    LOOP AT it_venpotxt ASSIGNING <ls_venpotxt> ##ENH_OK.
      DELETE TABLE gt_venpotxt FROM <ls_venpotxt>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_wp_email.

    FIELD-SYMBOLS:
     <ls_wp_email> TYPE /mdgbp/_s_bp_pp_wp_email.

    LOOP AT it_wp_email ASSIGNING <ls_wp_email> ##ENH_OK.
      DELETE TABLE gt_wp_email FROM <ls_wp_email>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_wp_fax.

    FIELD-SYMBOLS:
      <ls_wp_fax> TYPE /mdgbp/_s_bp_pp_wp_fax.

    LOOP AT it_wp_fax ASSIGNING <ls_wp_fax> ##ENH_OK.
      DELETE TABLE gt_wp_fax FROM <ls_wp_fax>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_wp_postal.

    FIELD-SYMBOLS:
      <ls_wp_postal> TYPE /mdgbp/_s_bp_pp_wp_postal.

    LOOP AT it_wp_postal ASSIGNING <ls_wp_postal> ##ENH_OK.
      DELETE TABLE gt_wp_postal FROM <ls_wp_postal>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_wp_tel.

    FIELD-SYMBOLS:
      <ls_wp_tel> TYPE /mdgbp/_s_bp_pp_wp_tel.

    LOOP AT it_wp_tel ASSIGNING <ls_wp_tel> ##ENH_OK.
      DELETE TABLE gt_wp_tel FROM <ls_wp_tel>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_wp_url.

    FIELD-SYMBOLS:
      <ls_wp_url> TYPE /mdgbp/_s_bp_pp_wp_url.

    LOOP AT it_wp_url ASSIGNING <ls_wp_url> ##ENH_OK.
      DELETE TABLE gt_wp_url FROM <ls_wp_url>.
    ENDLOOP.

  ENDMETHOD.


  METHOD get_address.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_address, es_address.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-address
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_address ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_address.
      ENDLOOP.
    ELSE .
      et_address = gt_address.
    ENDIF.

    IF lines( et_address ) = 1.
      READ TABLE et_address INTO es_address INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_addrno.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_addrno, es_addrno.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-address_number
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_addrno ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_addrno.
      ENDLOOP.
    ELSE .
      et_addrno = gt_addrno.
    ENDIF.

    IF lines( et_addrno ) = 1.
      READ TABLE et_addrno INTO es_addrno INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_ad_email.

    DATA:
      ls_bp_addusg TYPE /mdgbp/_s_bp_pp_bp_addusg,
      lt_bp_addusg TYPE zif_mdg_bp_datatypes=>gty_t_bp_addusg,
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_ad_email, es_ad_email.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-address_email
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_ad_email ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_ad_email.
      ENDLOOP.
    ELSE .
      et_ad_email = gt_ad_email.
    ENDIF.

    IF lines( et_ad_email ) = 1.
      READ TABLE et_ad_email INTO es_ad_email INDEX 1 ##ENH_OK.

    ELSEIF iv_std_address EQ abap_true.
      CLEAR: lt_key_value.
      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants=>gc_bp_model_entity-address_usage
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_bp_addusg
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          et_bp_addusg = lt_bp_addusg.
      READ TABLE lt_bp_addusg INTO ls_bp_addusg WITH KEY bp_adrknd = if_mdg_bp_constants=>gc_standard_address.
      READ TABLE gt_ad_email INTO es_ad_email  WITH KEY addrno = ls_bp_addusg-addrno.
    ENDIF.

  ENDMETHOD.


  METHOD get_ad_fax.

    DATA:
      ls_bp_addusg TYPE /mdgbp/_s_bp_pp_bp_addusg,
      lt_bp_addusg TYPE zif_mdg_bp_datatypes=>gty_t_bp_addusg,
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_ad_fax, es_ad_fax.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-address_fax
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_ad_fax ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_ad_fax.
      ENDLOOP.
    ELSE .
      et_ad_fax = gt_ad_fax.
    ENDIF.

    IF lines( et_ad_fax ) = 1.
      READ TABLE et_ad_fax INTO es_ad_fax INDEX 1 ##ENH_OK.

    ELSEIF iv_std_address EQ abap_true.
      CLEAR: lt_key_value.
      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants=>gc_bp_model_entity-address_usage
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_bp_addusg
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          et_bp_addusg = lt_bp_addusg.
      READ TABLE lt_bp_addusg INTO ls_bp_addusg WITH KEY bp_adrknd = if_mdg_bp_constants=>gc_standard_address.
      READ TABLE gt_ad_fax INTO es_ad_fax WITH KEY addrno = ls_bp_addusg-addrno.
    ENDIF.

  ENDMETHOD.


  METHOD get_ad_name_o.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_ad_name_o, es_ad_name_o.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-address_name_org
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_ad_name_o ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_ad_name_o.
      ENDLOOP.
    ELSE .
      et_ad_name_o = gt_ad_name_o.
    ENDIF.

    IF lines( et_ad_name_o ) = 1.
      READ TABLE et_ad_name_o INTO es_ad_name_o INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_ad_name_p.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_ad_name_p, es_ad_name_p.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-address_name_pers
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_ad_name_p ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_ad_name_p.
      ENDLOOP.
    ELSE .
      et_ad_name_p = gt_ad_name_p.
    ENDIF.

    IF lines( et_ad_name_p ) = 1.
      READ TABLE et_ad_name_p INTO es_ad_name_p INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_ad_postal.

    DATA:
      ls_bp_addusg TYPE /mdgbp/_s_bp_pp_bp_addusg,
      lt_bp_addusg TYPE zif_mdg_bp_datatypes=>gty_t_bp_addusg,
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_ad_postal, es_ad_postal.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-address_postal
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_ad_postal ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_ad_postal.
      ENDLOOP.
    ELSE .
      et_ad_postal = gt_ad_postal.
    ENDIF.

    IF lines( et_ad_postal ) = 1.
      READ TABLE et_ad_postal INTO es_ad_postal INDEX 1 ##ENH_OK.

    ELSEIF iv_std_address EQ abap_true.
      CLEAR: lt_key_value.
      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants=>gc_bp_model_entity-address_usage
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_bp_addusg
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          et_bp_addusg = lt_bp_addusg.
      READ TABLE lt_bp_addusg INTO ls_bp_addusg WITH KEY bp_adrknd = if_mdg_bp_constants=>gc_standard_address.
      READ TABLE gt_ad_postal INTO es_ad_postal WITH KEY addrno = ls_bp_addusg-addrno.
    ENDIF.

  ENDMETHOD.


  METHOD get_ad_tel.

    DATA:
      ls_bp_addusg TYPE /mdgbp/_s_bp_pp_bp_addusg,
      lt_bp_addusg TYPE zif_mdg_bp_datatypes=>gty_t_bp_addusg,
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_ad_tel, es_ad_tel.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-address_phone
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_ad_tel ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_ad_tel.
      ENDLOOP.
    ELSE .
      et_ad_tel = gt_ad_tel.
    ENDIF.

    IF lines( et_ad_tel ) = 1.
      READ TABLE et_ad_tel INTO es_ad_tel INDEX 1 ##ENH_OK.

    ELSEIF iv_std_address EQ abap_true.
      CLEAR: lt_key_value.
      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants=>gc_bp_model_entity-address_usage
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_bp_addusg
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          et_bp_addusg = lt_bp_addusg.
      READ TABLE lt_bp_addusg INTO ls_bp_addusg WITH KEY bp_adrknd = if_mdg_bp_constants=>gc_standard_address.
      READ TABLE gt_ad_tel INTO es_ad_tel WITH KEY addrno = ls_bp_addusg-addrno.
    ENDIF.

  ENDMETHOD.


  METHOD get_ad_url.

    DATA:
      ls_bp_addusg TYPE /mdgbp/_s_bp_pp_bp_addusg,
      lt_bp_addusg TYPE zif_mdg_bp_datatypes=>gty_t_bp_addusg,
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_ad_url, es_ad_url.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-address_url
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_ad_url ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_ad_url.
      ENDLOOP.
    ELSE .
      et_ad_url = gt_ad_url.
    ENDIF.

    IF lines( et_ad_url ) = 1.
      READ TABLE et_ad_url INTO es_ad_url INDEX 1 ##ENH_OK.

    ELSEIF iv_std_address EQ abap_true.
      CLEAR: lt_key_value.
      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants=>gc_bp_model_entity-address_usage
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_bp_addusg
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          et_bp_addusg = lt_bp_addusg.
      READ TABLE lt_bp_addusg INTO ls_bp_addusg WITH KEY bp_adrknd = if_mdg_bp_constants=>gc_standard_address.
      READ TABLE gt_ad_url INTO es_ad_url WITH KEY addrno = ls_bp_addusg-addrno.
    ENDIF.

  ENDMETHOD.


  METHOD get_all_entities.

    DATA:
      lt_entity_names TYPE  usmd_ts_entity_prop_ext,
      lt_all_entities TYPE usmd_t_entity.

    FIELD-SYMBOLS:
      <ls_entity_key> TYPE usmd_s_entity_prop_ext.

    CLEAR: rt_all_entities.

* fetch all entities from data model
    lt_entity_names = go_model->if_usmd_model_metadata_ext~dt_entity_prop.

* only entity of type 1 and 4 are considered for cache (everything else are key fields)
    DELETE lt_entity_names WHERE ( usage_type <> '1' AND usage_type <> '4' ). "#EC CI_SORTSEQ "sorted access not required due to table size >100

* write date to internal entity list
    LOOP AT lt_entity_names ASSIGNING <ls_entity_key>.
      APPEND <ls_entity_key>-usmd_entity TO lt_all_entities.
    ENDLOOP.
    SORT lt_all_entities.

    rt_all_entities = lt_all_entities.

  ENDMETHOD.


  METHOD get_attribute_entity.

    DATA:
          ls_attribute_entity TYPE zif_mdg_datatypes=>gty_s_attribute_entity_rel.

    CLEAR: ev_entity.

    READ TABLE gt_attribute_entity_rel INTO ls_attribute_entity WITH TABLE KEY attribute = iv_attribute.

    IF sy-subrc <> 0.
      RAISE attribute_not_found.
    ENDIF.

    ev_entity = ls_attribute_entity-entity.

  ENDMETHOD.


  METHOD get_attribute_entity_list.

    CLEAR: et_attribute_entity_rel.

    et_attribute_entity_rel = gt_attribute_entity_rel.

  ENDMETHOD.


  METHOD get_bp_addr.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_addr, es_bp_addr.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-bp_address
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_addr ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_addr.
      ENDLOOP.
    ELSE .
      et_bp_addr = gt_bp_addr.
    ENDIF.

    IF lines( et_bp_addr ) = 1.
      READ TABLE et_bp_addr INTO es_bp_addr INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_addusg.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_addusg, es_bp_addusg.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-address_usage
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_addusg ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_addusg.
      ENDLOOP.
    ELSE .
      et_bp_addusg = gt_bp_addusg.
    ENDIF.

    IF lines( et_bp_addusg ) = 1.
      READ TABLE et_bp_addusg INTO es_bp_addusg INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_bkdtl.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_bkdtl, es_bp_bkdtl.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-bank_details
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_bkdtl ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_bkdtl.
      ENDLOOP.
    ELSE .
      et_bp_bkdtl = gt_bp_bkdtl.
    ENDIF.

    IF lines( et_bp_bkdtl ) = 1.
      READ TABLE et_bp_bkdtl INTO es_bp_bkdtl INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_ccdtl.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_ccdtl, es_bp_ccdtl.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-card_details
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_ccdtl ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_ccdtl.
      ENDLOOP.
    ELSE .
      et_bp_ccdtl = gt_bp_ccdtl.
    ENDIF.

    IF lines( et_bp_ccdtl ) = 1.
      READ TABLE et_bp_ccdtl INTO es_bp_ccdtl INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_centrl.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_centrl, es_bp_centrl.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-central
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_centrl ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_centrl.
      ENDLOOP.
    ELSE .
      et_bp_centrl = gt_bp_centrl.
    ENDIF.

    IF lines( et_bp_centrl ) = 1.
      READ TABLE et_bp_centrl INTO es_bp_centrl INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_compny.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_compny, es_bp_compny.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-company_code
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_compny ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_compny.
      ENDLOOP.
    ELSE .
      et_bp_compny = gt_bp_compny.
    ENDIF.

    IF lines( et_bp_compny ) = 1.
      READ TABLE et_bp_compny INTO es_bp_compny INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_cpgen.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_cpgen, es_bp_cpgen.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-contact_person
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_cpgen ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_cpgen.
      ENDLOOP.
    ELSE .
      et_bp_cpgen = gt_bp_cpgen.
    ENDIF.

    IF lines( et_bp_cpgen ) = 1.
      READ TABLE et_bp_cpgen INTO es_bp_cpgen INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_cuscla.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_cuscla, es_bp_cuscla.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-class_assignment
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_cuscla ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_cuscla.
      ENDLOOP.
    ELSE .
      et_bp_cuscla = gt_bp_cuscla.
    ENDIF.

    IF lines( et_bp_cuscla ) = 1.
      READ TABLE et_bp_cuscla INTO es_bp_cuscla INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_cusddb.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_cusddb, es_bp_cusddb.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-document_link
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_cusddb ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_cusddb.
      ENDLOOP.
    ELSE .
      et_bp_cusddb = gt_bp_cusddb.
    ENDIF.

    IF lines( et_bp_cusddb ) = 1.
      READ TABLE et_bp_cusddb INTO es_bp_cusddb INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_cusdun.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_cusdun, es_bp_cusdun.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-dunning_area
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_cusdun ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_cusdun.
      ENDLOOP.
    ELSE .
      et_bp_cusdun = gt_bp_cusdun.
    ENDIF.

    IF lines( et_bp_cusdun ) = 1.
      READ TABLE et_bp_cusdun INTO es_bp_cusdun INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_cusfcn.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_cusfcn, es_bp_cusfcn.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-partner_functions
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_cusfcn ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_cusfcn.
      ENDLOOP.
    ELSE .
      et_bp_cusfcn = gt_bp_cusfcn.
    ENDIF.

    IF lines( et_bp_cusfcn ) = 1.
      READ TABLE et_bp_cusfcn INTO es_bp_cusfcn INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_cusgen.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_cusgen, es_bp_cusgen.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-general_data
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_cusgen ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_cusgen.
      ENDLOOP.
    ELSE .
      et_bp_cusgen = gt_bp_cusgen.
    ENDIF.

    IF lines( et_bp_cusgen ) = 1.
      READ TABLE et_bp_cusgen INTO es_bp_cusgen INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_custax.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_custax, es_bp_custax.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-tax_indicators
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_custax ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_custax.
      ENDLOOP.
    ELSE .
      et_bp_custax = gt_bp_custax.
    ENDIF.

    IF lines( et_bp_custax ) = 1.
      READ TABLE et_bp_custax INTO es_bp_custax INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_cusulp.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_cusulp, es_bp_cusulp.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-loading_points
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_cusulp ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_cusulp.
      ENDLOOP.
    ELSE .
      et_bp_cusulp = gt_bp_cusulp.
    ENDIF.

    IF lines( et_bp_cusulp ) = 1.
      READ TABLE et_bp_cusulp INTO es_bp_cusulp INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_cusval.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_cusval, es_bp_cusval.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-class_valuation
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_cusval ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_cusval.
      ENDLOOP.
    ELSE .
      et_bp_cusval = gt_bp_cusval.
    ENDIF.

    IF lines( et_bp_cusval ) = 1.
      READ TABLE et_bp_cusval INTO es_bp_cusval INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_cuswht.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_cuswht, es_bp_cuswht.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-withholding_tax
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_cuswht ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_cuswht.
      ENDLOOP.
    ELSE .
      et_bp_cuswht = gt_bp_cuswht.
    ENDIF.

    IF lines( et_bp_cuswht ) = 1.
      READ TABLE et_bp_cuswht INTO es_bp_cuswht INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_cus_cc.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_cus_cc, es_bp_cus_cc.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-company_code
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_cus_cc ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_cus_cc.
      ENDLOOP.
    ELSE .
      et_bp_cus_cc = gt_bp_cus_cc.
    ENDIF.

    IF lines( et_bp_cus_cc ) = 1.
      READ TABLE et_bp_cus_cc INTO es_bp_cus_cc INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_dunn.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_dunn, es_bp_dunn.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-dunning_area
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_dunn ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_dunn.
      ENDLOOP.
    ELSE .
      et_bp_dunn = gt_bp_dunn.
    ENDIF.

    IF lines( et_bp_dunn ) = 1.
      READ TABLE et_bp_dunn INTO es_bp_dunn INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_header.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_header, es_bp_header.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-bp
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_header ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_header.
      ENDLOOP.
    ELSE .
      et_bp_header = gt_bp_header.
    ENDIF.

    IF lines( et_bp_header ) = 1.
      READ TABLE et_bp_header INTO es_bp_header INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_hrchy.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_hrchy, es_bp_hrchy.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-hierarchy
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_hrchy ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_hrchy.
      ENDLOOP.
    ELSE .
      et_bp_hrchy = gt_bp_hrchy.
    ENDIF.

    IF lines( et_bp_hrchy ) = 1.
      READ TABLE et_bp_hrchy INTO es_bp_hrchy INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_idnum.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_idnum, es_bp_idnum.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-ids
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_idnum ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_idnum.
      ENDLOOP.
    ELSE .
      et_bp_idnum = gt_bp_idnum.
    ENDIF.

    IF lines( et_bp_idnum ) = 1.
      READ TABLE et_bp_idnum INTO es_bp_idnum INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_indstr.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_indstr, es_bp_indstr.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-industries
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_indstr ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_indstr.
      ENDLOOP.
    ELSE .
      et_bp_indstr = gt_bp_indstr.
    ENDIF.

    IF lines( et_bp_indstr ) = 1.
      READ TABLE et_bp_indstr INTO es_bp_indstr INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_mlt_ad.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_mlt_ad, es_bp_mlt_ad.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_ma_ad_model_entity
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_mlt_ad ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_mlt_ad.
      ENDLOOP.
    ELSE .
      et_bp_mlt_ad = gt_bp_mlt_ad.
    ENDIF.

    IF lines( et_bp_mlt_ad ) = 1.
      READ TABLE et_bp_mlt_ad INTO es_bp_mlt_ad INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_mlt_as.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_mlt_as, es_bp_mlt_as.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_ma_model_entity
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_mlt_as ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_mlt_as.
      ENDLOOP.
    ELSE .
      et_bp_mlt_as = gt_bp_mlt_as.
    ENDIF.

    IF lines( et_bp_mlt_as ) = 1.
      READ TABLE et_bp_mlt_as INTO es_bp_mlt_as INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_porg.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_porg, es_bp_porg.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-purchasing_org
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_porg ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_porg.
      ENDLOOP.
    ELSE .
      et_bp_porg = gt_bp_porg.
    ENDIF.

    IF lines( et_bp_porg ) = 1.
      READ TABLE et_bp_porg INTO es_bp_porg INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_porg2.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_porg2, es_bp_porg2.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-additional_purchasing
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_porg2 ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_porg2.
      ENDLOOP.
    ELSE .
      et_bp_porg2 = gt_bp_porg2.
    ENDIF.

    IF lines( et_bp_porg2 ) = 1.
      READ TABLE et_bp_porg2 INTO es_bp_porg2 INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_rel.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_rel, es_bp_rel.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-relation
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_rel ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_rel.
      ENDLOOP.
    ELSE .
      et_bp_rel = gt_bp_rel.
    ENDIF.

    IF lines( et_bp_rel ) = 1.
      READ TABLE et_bp_rel INTO es_bp_rel INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_role.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_role, es_bp_role.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-roles
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_role ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_role.
      ENDLOOP.
    ELSE .
      et_bp_role = gt_bp_role.
    ENDIF.

    IF lines( et_bp_role ) = 1.
      READ TABLE et_bp_role INTO es_bp_role INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_sales.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_sales, es_bp_sales.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-sales_area
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_sales ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_sales.
      ENDLOOP.
    ELSE .
      et_bp_sales = gt_bp_sales.
    ENDIF.

    IF lines( et_bp_sales ) = 1.
      READ TABLE et_bp_sales INTO es_bp_sales INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_subhry.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_subhry, es_bp_subhry.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = ZCL_MDG_BP_HELPER=>gc_bp_model_entity-sub_hierarchy
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_subhry ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_subhry.
      ENDLOOP.
    ELSE .
      et_bp_subhry = gt_bp_subhry.
    ENDIF.

    IF lines( et_bp_subhry ) = 1.
      READ TABLE et_bp_subhry INTO es_bp_subhry INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_taxgrp.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_taxgrp, es_bp_taxgrp.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-tax_groupings
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_taxgrp ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_taxgrp.
      ENDLOOP.
    ELSE .
      et_bp_taxgrp = gt_bp_taxgrp.
    ENDIF.

    IF lines( et_bp_taxgrp ) = 1.
      READ TABLE et_bp_taxgrp INTO es_bp_taxgrp INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_taxnum.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_taxnum, es_bp_taxnum.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-tax
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_taxnum ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_taxnum.
      ENDLOOP.
    ELSE .
      et_bp_taxnum = gt_bp_taxnum.
    ENDIF.

    IF lines( et_bp_taxnum ) = 1.
      READ TABLE et_bp_taxnum INTO es_bp_taxnum INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_vencla.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_vencla, es_bp_vencla.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-class_assignment
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_vencla ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_vencla.
      ENDLOOP.
    ELSE .
      et_bp_vencla = gt_bp_vencla.
    ENDIF.

    IF lines( et_bp_vencla ) = 1.
      READ TABLE et_bp_vencla INTO es_bp_vencla INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_venddb.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_venddb, es_bp_venddb.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-document_link
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_venddb ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_venddb.
      ENDLOOP.
    ELSE .
      et_bp_venddb = gt_bp_venddb.
    ENDIF.

    IF lines( et_bp_venddb ) = 1.
      READ TABLE et_bp_venddb INTO es_bp_venddb INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_venfcn.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_venfcn, es_bp_venfcn.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-partner_functions
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_venfcn ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_venfcn.
      ENDLOOP.
    ELSE .
      et_bp_venfcn = gt_bp_venfcn.
    ENDIF.

    IF lines( et_bp_venfcn ) = 1.
      READ TABLE et_bp_venfcn INTO es_bp_venfcn INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_vengen.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_vengen, es_bp_vengen.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-general_data
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_vengen ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_vengen.
      ENDLOOP.
    ELSE .
      et_bp_vengen = gt_bp_vengen.
    ENDIF.

    IF lines( et_bp_vengen ) = 1.
      READ TABLE et_bp_vengen INTO es_bp_vengen INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_vensub.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_vensub, es_bp_vensub.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-sub_range
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_vensub ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_vensub.
      ENDLOOP.
    ELSE .
      et_bp_vensub = gt_bp_vensub.
    ENDIF.

    IF lines( et_bp_vensub ) = 1.
      READ TABLE et_bp_vensub INTO es_bp_vensub INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_venval.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_venval, es_bp_venval.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-class_valuation
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_venval ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_venval.
      ENDLOOP.
    ELSE .
      et_bp_venval = gt_bp_venval.
    ENDIF.

    IF lines( et_bp_venval ) = 1.
      READ TABLE et_bp_venval INTO es_bp_venval INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_whtax.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_whtax, es_bp_whtax.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-withholding_tax
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_whtax ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_whtax.
      ENDLOOP.
    ELSE .
      et_bp_whtax = gt_bp_whtax.
    ENDIF.

    IF lines( et_bp_whtax ) = 1.
      READ TABLE et_bp_whtax INTO es_bp_whtax INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_bp_wpad.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bp_wpad, es_bp_wpad.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-workplace
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bp_wpad ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bp_wpad.
      ENDLOOP.
    ELSE .
      et_bp_wpad = gt_bp_wpad.
    ENDIF.

    IF lines( et_bp_wpad ) = 1.
      READ TABLE et_bp_wpad INTO es_bp_wpad INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_cuscctxt.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_cuscctxt, es_cuscctxt.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-company_code_text
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_cuscctxt ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_cuscctxt.
      ENDLOOP.
    ELSE .
      et_cuscctxt = gt_cuscctxt.
    ENDIF.

    IF lines( et_cuscctxt ) = 1.
      READ TABLE et_cuscctxt INTO es_cuscctxt INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_cusgentxt.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_cusgentxt, es_cusgentxt.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-general_data_text
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_cusgentxt ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_cusgentxt.
      ENDLOOP.
    ELSE .
      et_cusgentxt = gt_cusgentxt.
    ENDIF.

    IF lines( et_cusgentxt ) = 1.
      READ TABLE et_cusgentxt INTO es_cusgentxt INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_cussaltxt.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_cussaltxt, es_cussaltxt.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-sales_area_text
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_cussaltxt ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_cussaltxt.
      ENDLOOP.
    ELSE .
      et_cussaltxt = gt_cussaltxt.
    ENDIF.

    IF lines( et_cussaltxt ) = 1.
      READ TABLE et_cussaltxt INTO es_cussaltxt INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_entity_attributes.

    DATA:
          ls_entity_attributes TYPE zif_mdg_datatypes=>gty_s_entity_attributes_rel.

    CLEAR: et_entity_attributes.

    READ TABLE gt_entity_attributes_rel INTO ls_entity_attributes WITH TABLE KEY entity = iv_entity.

    IF sy-subrc <> 0.
      RAISE entity_not_found.
    ENDIF.

    et_entity_attributes = ls_entity_attributes-attributes.

  ENDMETHOD.


  METHOD get_entity_attributes_list.

    CLEAR: et_entity_attributes.

    et_entity_attributes = gt_entity_attributes_rel.

  ENDMETHOD.


  METHOD get_entity_info.

    DATA:
          ls_entity_info TYPE zif_mdg_datatypes=>gty_s_entity_info.

    CLEAR: rs_entity_info.


    READ TABLE get_entity_info_list( ) INTO ls_entity_info WITH TABLE KEY entity = iv_entity.

    IF sy-subrc <> 0.
      RAISE entity_not_found.
    ENDIF.

    rs_entity_info = ls_entity_info.

  ENDMETHOD.


  METHOD get_entity_info_list.

    DATA:
      ls_entity_info  TYPE zif_mdg_datatypes=>gty_s_entity_info.

    CLEAR rt_entity_info.

* Writes the information from method Address GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-address.
    ls_entity_info-get_meth         = 'GET_ADDRESS'.
    ls_entity_info-set_meth         = 'SET_ADDRESS'.
    ls_entity_info-del_meth         = 'DEL_ADDRESS'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_ADDRESS'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_ADDRESS'.
    ls_entity_info-get_meth_exp_tab = 'ET_ADDRESS'.
    ls_entity_info-del_meth_imp_tab = 'IT_ADDRESS'.
    ls_entity_info-set_meth_imp_tab = 'IT_ADDRESS'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method ADDRNO GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-address_number.
    ls_entity_info-get_meth         = 'GET_ADDRNO'.
    ls_entity_info-set_meth         = 'SET_ADDRNO'.
    ls_entity_info-del_meth         = 'DEL_ADDRNO'.
    ls_entity_info-structure        = 'MDG_BS_ADDRNO'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_ADDRNO'.
    ls_entity_info-get_meth_exp_tab = 'ET_ADDRNO'.
    ls_entity_info-del_meth_imp_tab = 'IT_ADDRNO'.
    ls_entity_info-set_meth_imp_tab = 'IT_ADDRNO'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method AD_EMAIL GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-address_email.
    ls_entity_info-get_meth         = 'GET_AD_EMAIL'.
    ls_entity_info-set_meth         = 'SET_AD_EMAIL'.
    ls_entity_info-del_meth         = 'DEL_AD_EMAIL'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_AD_EMAIL'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_AD_EMAIL'.
    ls_entity_info-get_meth_exp_tab = 'ET_AD_EMAIL'.
    ls_entity_info-del_meth_imp_tab = 'IT_AD_EMAIL'.
    ls_entity_info-set_meth_imp_tab = 'IT_AD_EMAIL'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method AD_FAX GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-address_fax.
    ls_entity_info-get_meth         = 'GET_AD_FAX'.
    ls_entity_info-set_meth         = 'SET_AD_FAX'.
    ls_entity_info-del_meth         = 'DEL_AD_FAX'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_AD_FAX'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_AD_FAX'.
    ls_entity_info-get_meth_exp_tab = 'ET_AD_FAX'.
    ls_entity_info-del_meth_imp_tab = 'IT_AD_FAX'.
    ls_entity_info-set_meth_imp_tab = 'IT_AD_FAX'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method AD_NAME_O GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-address_name_org.
    ls_entity_info-get_meth         = 'GET_AD_NAME_O'.
    ls_entity_info-set_meth         = 'SET_AD_NAME_O'.
    ls_entity_info-del_meth         = 'DEL_AD_NAME_O'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_AD_NAME_O'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_AD_NAME_O'.
    ls_entity_info-get_meth_exp_tab = 'ET_AD_NAME_O'.
    ls_entity_info-del_meth_imp_tab = 'IT_AD_NAME_O'.
    ls_entity_info-set_meth_imp_tab = 'IT_AD_NAME_O'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method AD_NAME_P GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-address_name_pers.
    ls_entity_info-get_meth         = 'GET_AD_NAME_P'.
    ls_entity_info-set_meth         = 'SET_AD_NAME_P'.
    ls_entity_info-del_meth         = 'DEL_AD_NAME_P'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_AD_NAME_P'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_AD_NAME_P'.
    ls_entity_info-get_meth_exp_tab = 'ET_AD_NAME_P'.
    ls_entity_info-del_meth_imp_tab = 'IT_AD_NAME_P'.
    ls_entity_info-set_meth_imp_tab = 'IT_AD_NAME_P'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method AD_POSTAL GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-address_postal.
    ls_entity_info-get_meth         = 'GET_AD_POSTAL'.
    ls_entity_info-set_meth         = 'SET_AD_POSTAL'.
    ls_entity_info-del_meth         = 'DEL_AD_POSTAL'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_AD_POSTAL'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_AD_POSTAL'.
    ls_entity_info-get_meth_exp_tab = 'ET_AD_POSTAL'.
    ls_entity_info-del_meth_imp_tab = 'IT_AD_POSTAL'.
    ls_entity_info-set_meth_imp_tab = 'IT_AD_POSTAL'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method AD_TEL GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-address_phone.
    ls_entity_info-get_meth         = 'GET_AD_TEL'.
    ls_entity_info-set_meth         = 'SET_AD_TEL'.
    ls_entity_info-del_meth         = 'DEL_AD_TEL'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_AD_TEL'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_AD_TEL'.
    ls_entity_info-get_meth_exp_tab = 'ET_AD_TEL'.
    ls_entity_info-del_meth_imp_tab = 'IT_AD_TEL'.
    ls_entity_info-set_meth_imp_tab = 'IT_AD_TEL'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method AD_URL GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-address_url.
    ls_entity_info-get_meth         = 'GET_AD_URL'.
    ls_entity_info-set_meth         = 'SET_AD_URL'.
    ls_entity_info-del_meth         = 'DEL_AD_URL'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_AD_URL'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_AD_URL'.
    ls_entity_info-get_meth_exp_tab = 'ET_AD_URL'.
    ls_entity_info-del_meth_imp_tab = 'IT_AD_URL'.
    ls_entity_info-set_meth_imp_tab = 'IT_AD_URL'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_ADDR GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-bp_address.
    ls_entity_info-get_meth         = 'GET_BP_ADDR'.
    ls_entity_info-set_meth         = 'SET_BP_ADDR'.
    ls_entity_info-del_meth         = 'DEL_BP_ADDR'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_BP_ADDR'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_ADDR'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_ADDR'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_ADDR'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_ADDR'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_ADDUSG GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-address_usage.
    ls_entity_info-get_meth         = 'GET_BP_ADDUSG'.
    ls_entity_info-set_meth         = 'SET_BP_ADDUSG'.
    ls_entity_info-del_meth         = 'DEL_BP_ADDUSG'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_BP_ADDUSG'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_ADDUSG'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_ADDUSG'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_ADDUSG'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_ADDUSG'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method P_BKDTL GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-bank_details.
    ls_entity_info-get_meth         = 'GET_BP_BKDTL'.
    ls_entity_info-set_meth         = 'SET_BP_BKDTL'.
    ls_entity_info-del_meth         = 'DEL_BP_BKDTL'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_BP_BKDTL'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_BKDTL'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_BKDTL'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_BKDTL'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_BKDTL'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_CCDTL GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-card_details.
    ls_entity_info-get_meth         = 'GET_BP_CCDTL'.
    ls_entity_info-set_meth         = 'SET_BP_CCDTL'.
    ls_entity_info-del_meth         = 'DEL_BP_CCDTL'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_BP_CCDTL'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_CCDTL'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_CCDTL'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_CCDTL'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_CCDTL'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_CENTRL GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-central.
    ls_entity_info-get_meth         = 'GET_BP_CENTRL'.
    ls_entity_info-set_meth         = 'SET_BP_CENTRL'.
    ls_entity_info-del_meth         = 'DEL_BP_CENTRL'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_BP_CENTRL'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_CENTRL'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_CENTRL'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_CENTRL'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_CENTRL'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_COMPNY GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-company_code.
    ls_entity_info-get_meth         = 'GET_BP_COMPNY'.
    ls_entity_info-set_meth         = 'SET_BP_COMPNY'.
    ls_entity_info-del_meth         = 'DEL_BP_COMPNY'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_COMPNY'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_COMPNY'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_COMPNY'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_COMPNY'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_COMPNY'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_CPGEN GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-contact_person.
    ls_entity_info-get_meth         = 'GET_BP_CPGEN'.
    ls_entity_info-set_meth         = 'SET_BP_CPGEN'.
    ls_entity_info-del_meth         = 'DEL_BP_CPGEN'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_BP_CPGEN'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_CPGEN'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_CPGEN'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_CPGEN'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_CPGEN'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_CUSCLA GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-class_assignment.
    ls_entity_info-get_meth         = 'GET_BP_CUSCLA'.
    ls_entity_info-set_meth         = 'SET_BP_CUSCLA'.
    ls_entity_info-del_meth         = 'DEL_BP_CUSCLA'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_CUSCLA'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_CUSCLA'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_CUSCLA'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_CUSCLA'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_CUSCLA'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_CUSDDB GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-document_link.
    ls_entity_info-get_meth         = 'GET_BP_CUSDDB'.
    ls_entity_info-set_meth         = 'SET_BP_CUSDDB'.
    ls_entity_info-del_meth         = 'DEL_BP_CUSDDB'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_CUSDDB'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_CUSDDB'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_CUSDDB'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_CUSDDB'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_CUSDDB'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_CUSDUN GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-dunning_area.
    ls_entity_info-get_meth         = 'GET_BP_CUSDUN'.
    ls_entity_info-set_meth         = 'SET_BP_CUSDUN'.
    ls_entity_info-del_meth         = 'DEL_BP_CUSDUN'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_CUSDUN'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_CUSDUN'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_CUSDUN'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_CUSDUN'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_CUSDUN'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_CUSFCN GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-partner_functions.
    ls_entity_info-get_meth         = 'GET_BP_CUSFCN'.
    ls_entity_info-set_meth         = 'SET_BP_CUSFCN'.
    ls_entity_info-del_meth         = 'DEL_BP_CUSFCN'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_CUSFCN'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_CUSFCN'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_CUSFCN'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_CUSFCN'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_CUSFCN'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_CUSGEN GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-general_data.
    ls_entity_info-get_meth         = 'GET_BP_CUSGEN'.
    ls_entity_info-set_meth         = 'SET_BP_CUSGEN'.
    ls_entity_info-del_meth         = 'DEL_BP_CUSGEN'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_CUSGEN'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_CUSGEN'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_CUSGEN'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_CUSGEN'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_CUSGEN'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_CUSTAX GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-tax_indicators.
    ls_entity_info-get_meth         = 'GET_BP_CUSTAX'.
    ls_entity_info-set_meth         = 'SET_BP_CUSTAX'.
    ls_entity_info-del_meth         = 'DEL_BP_CUSTAX'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_CUSTAX'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_CUSTAX'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_CUSTAX'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_CUSTAX'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_CUSTAX'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_CUSULP GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-loading_points.
    ls_entity_info-get_meth         = 'GET_BP_CUSULP'.
    ls_entity_info-set_meth         = 'SET_BP_CUSULP'.
    ls_entity_info-del_meth         = 'DEL_BP_CUSULP'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_CUSULP'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_CUSULP'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_CUSULP'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_CUSULP'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_CUSULP'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_CUSVAL GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-class_valuation.
    ls_entity_info-get_meth         = 'GET_BP_CUSVAL'.
    ls_entity_info-set_meth         = 'SET_BP_CUSVAL'.
    ls_entity_info-del_meth         = 'DEL_BP_CUSVAL'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_CUSVAL'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_CUSVAL'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_CUSVAL'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_CUSVAL'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_CUSVAL'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_CUSWHT GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-withholding_tax.
    ls_entity_info-get_meth         = 'GET_BP_CUSWHT'.
    ls_entity_info-set_meth         = 'SET_BP_CUSWHT'.
    ls_entity_info-del_meth         = 'DEL_BP_CUSWHT'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_CUSWHT'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_CUSWHT'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_CUSWHT'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_CUSWHT'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_CUSWHT'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_CUS_CC GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-company_code.
    ls_entity_info-get_meth         = 'GET_BP_CUS_CC'.
    ls_entity_info-set_meth         = 'SET_BP_CUS_CC'.
    ls_entity_info-del_meth         = 'DEL_BP_CUS_CC'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_CUS_CC'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_CUS_CC'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_CUS_CC'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_CUS_CC'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_CUS_CC'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_DUNN GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-dunning_area.
    ls_entity_info-get_meth         = 'GET_BP_DUNN'.
    ls_entity_info-set_meth         = 'SET_BP_DUNN'.
    ls_entity_info-del_meth         = 'DEL_BP_DUNN'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_DUNN'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_DUNN'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_DUNN'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_DUNN'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_DUNN'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_HEADER GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-bp.
    ls_entity_info-get_meth         = 'GET_BP_HEADER'.
    ls_entity_info-set_meth         = 'SET_BP_HEADER'.
    ls_entity_info-del_meth         = 'DEL_BP_HEADER'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_BP_HEADER'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_HEADER'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_HEADER'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_HEADER'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_HEADER'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_HRCHY GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-hierarchy.
    ls_entity_info-get_meth         = 'GET_BP_HRCHY'.
    ls_entity_info-set_meth         = 'SET_BP_HRCHY'.
    ls_entity_info-del_meth         = 'DEL_BP_HRCHY'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_BP_HRCHY'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_HRCHY'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_HRCHY'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_HRCHY'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_HRCHY'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_IDNUM GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-ids.
    ls_entity_info-get_meth         = 'GET_BP_IDNUM'.
    ls_entity_info-set_meth         = 'SET_BP_IDNUM'.
    ls_entity_info-del_meth         = 'DEL_BP_IDNUM'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_BP_IDNUM'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_IDNUM'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_IDNUM'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_IDNUM'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_IDNUM'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_INDSTR GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-industries.
    ls_entity_info-get_meth         = 'GET_BP_INDSTR'.
    ls_entity_info-set_meth         = 'SET_BP_INDSTR'.
    ls_entity_info-del_meth         = 'DEL_BP_INDSTR'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_BP_INDSTR'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_INDSTR'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_INDSTR'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_INDSTR'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_INDSTR'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_MLT_AD GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_ma_ad_model_entity.
    ls_entity_info-get_meth         = 'GET_BP_MLT_AD'.
    ls_entity_info-set_meth         = 'SET_BP_MLT_AD'.
    ls_entity_info-del_meth         = 'DEL_BP_MLT_AD'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_MLT_AD'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_MLT_AD'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_MLT_AD'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_MLT_AD'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_MLT_AD'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_MLT_AS GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_ma_model_entity.
    ls_entity_info-get_meth         = 'GET_BP_MLT_AS'.
    ls_entity_info-set_meth         = 'SET_BP_MLT_AS'.
    ls_entity_info-del_meth         = 'DEL_BP_MLT_AS'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_MLT_AS'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_MLT_AS'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_MLT_AS'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_MLT_AS'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_MLT_AS'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_PORG GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-purchasing_org.
    ls_entity_info-get_meth         = 'GET_BP_PORG'.
    ls_entity_info-set_meth         = 'SET_BP_PORG'.
    ls_entity_info-del_meth         = 'DEL_BP_PORG'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_PORG'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_PORG'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_PORG'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_PORG'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_PORG'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_PORG2 GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-additional_purchasing.
    ls_entity_info-get_meth         = 'GET_BP_PORG2'.
    ls_entity_info-set_meth         = 'SET_BP_PORG2'.
    ls_entity_info-del_meth         = 'DEL_BP_PORG2'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_PORG2'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_PORG2'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_PORG2'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_PORG2'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_PORG2'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_REL GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-relation.
    ls_entity_info-get_meth         = 'GET_BP_REL'.
    ls_entity_info-set_meth         = 'SET_BP_REL'.
    ls_entity_info-del_meth         = 'DEL_BP_REL'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_BP_REL'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_REL'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_REL'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_REL'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_REL'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_ROLE GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-roles.
    ls_entity_info-get_meth         = 'GET_BP_ROLE'.
    ls_entity_info-set_meth         = 'SET_BP_ROLE'.
    ls_entity_info-del_meth         = 'DEL_BP_ROLE'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_BP_ROLE'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_ROLE'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_ROLE'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_ROLE'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_ROLE'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_SUBHRY GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = ZCL_MDG_BP_HELPER=>gc_bp_model_entity-sub_hierarchy.
    ls_entity_info-get_meth         = 'GET_BP_SUBHRY'.
    ls_entity_info-set_meth         = 'SET_BP_SUBHRY'.
    ls_entity_info-del_meth         = 'DEL_BP_SUBHRY'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_BP_SUBHRY'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_SUBHRY'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_SUBHRY'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_SUBHRY'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_SUBHRY'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_TAXGRP GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-tax_groupings.
    ls_entity_info-get_meth         = 'GET_BP_TAXGRP'.
    ls_entity_info-set_meth         = 'SET_BP_TAXGRP'.
    ls_entity_info-del_meth         = 'DEL_BP_TAXGRP'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_TAXGRP'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_TAXGRP'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_TAXGRP'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_TAXGRP'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_TAXGRP'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_TAXNUM GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-tax.
    ls_entity_info-get_meth         = 'GET_BP_TAXNUM'.
    ls_entity_info-set_meth         = 'SET_BP_TAXNUM'.
    ls_entity_info-del_meth         = 'DEL_BP_TAXNUM'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_BP_TAXNUM'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_TAXNUM'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_TAXNUM'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_TAXNUM'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_TAXNUM'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_VENCLA GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-class_assignment.
    ls_entity_info-get_meth         = 'GET_BP_VENCLA'.
    ls_entity_info-set_meth         = 'SET_BP_VENCLA'.
    ls_entity_info-del_meth         = 'DEL_BP_VENCLA'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_VENCLA'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_VENCLA'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_VENCLA'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_VENCLA'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_VENCLA'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_VENDDB GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-document_link.
    ls_entity_info-get_meth         = 'GET_BP_VENDDB'.
    ls_entity_info-set_meth         = 'SET_BP_VENDDB'.
    ls_entity_info-del_meth         = 'DEL_BP_VENDDB'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_VENDDB'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_VENDDB'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_VENDDB'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_VENDDB'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_VENDDB'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_VENFCN GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-partner_functions.
    ls_entity_info-get_meth         = 'GET_BP_VENFCN'.
    ls_entity_info-set_meth         = 'SET_BP_VENFCN'.
    ls_entity_info-del_meth         = 'DEL_BP_VENFCN'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_VENFCN'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_VENFCN'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_VENFCN'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_VENFCN'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_VENFCN'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_VENGEN GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-general_data.
    ls_entity_info-get_meth         = 'GET_BP_VENGEN'.
    ls_entity_info-set_meth         = 'SET_BP_VENGEN'.
    ls_entity_info-del_meth         = 'DEL_BP_VENGEN'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_VENGEN'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_VENGEN'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_VENGEN'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_VENGEN'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_VENGEN'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_VENSUB GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-sub_range.
    ls_entity_info-get_meth         = 'GET_BP_VENSUB'.
    ls_entity_info-set_meth         = 'SET_BP_VENSUB'.
    ls_entity_info-del_meth         = 'DEL_BP_VENSUB'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_VENSUB'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_VENSUB'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_VENSUB'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_VENSUB'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_VENSUB'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_SALES GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-sales_area.
    ls_entity_info-get_meth         = 'GET_BP_SALES'.
    ls_entity_info-set_meth         = 'SET_BP_SALES'.
    ls_entity_info-del_meth         = 'DEL_BP_SALES'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_SALES'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_SALES'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_SALES'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_SALES'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_SALES'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_VENVAL GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-class_valuation.
    ls_entity_info-get_meth         = 'GET_BP_VENVAL'.
    ls_entity_info-set_meth         = 'SET_BP_VENVAL'.
    ls_entity_info-del_meth         = 'DEL_BP_VENVAL'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_VENVAL'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_VENVAL'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_VENVAL'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_VENVAL'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_VENVAL'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_WHTAX GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-withholding_tax.
    ls_entity_info-get_meth         = 'GET_BP_WHTAX'.
    ls_entity_info-set_meth         = 'SET_BP_WHTAX'.
    ls_entity_info-del_meth         = 'DEL_BP_WHTAX'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_WHTAX'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_WHTAX'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_WHTAX'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_WHTAX'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_WHTAX'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method BP_WPAD GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-workplace.
    ls_entity_info-get_meth         = 'GET_BP_WPAD'.
    ls_entity_info-set_meth         = 'SET_BP_WPAD'.
    ls_entity_info-del_meth         = 'DEL_BP_WPAD'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_BP_WPAD'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_BP_WPAD'.
    ls_entity_info-get_meth_exp_tab = 'ET_BP_WPAD'.
    ls_entity_info-del_meth_imp_tab = 'IT_BP_WPAD'.
    ls_entity_info-set_meth_imp_tab = 'IT_BP_WPAD'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method CUSCCTXT GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-company_code_text.
    ls_entity_info-get_meth         = 'GET_CUSCCTXT'.
    ls_entity_info-set_meth         = 'SET_CUSCCTXT'.
    ls_entity_info-del_meth         = 'DEL_CUSCCTXT'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_CCCTXT'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_CUSCCTXT'.
    ls_entity_info-get_meth_exp_tab = 'ET_CUSCCTXT'.
    ls_entity_info-del_meth_imp_tab = 'IT_CUSCCTXT'.
    ls_entity_info-set_meth_imp_tab = 'IT_CUSCCTXT'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method CUSGENTXT GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-general_data_text.
    ls_entity_info-get_meth         = 'GET_CUSGENTXT'.
    ls_entity_info-set_meth         = 'SET_CUSGENTXT'.
    ls_entity_info-del_meth         = 'DEL_CUSGENTXT'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_CUSTXT'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_CUSGENTXT'.
    ls_entity_info-get_meth_exp_tab = 'ET_CUSGENTXT'.
    ls_entity_info-del_meth_imp_tab = 'IT_CUSGENTXT'.
    ls_entity_info-set_meth_imp_tab = 'IT_CUSGENTXT'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method FKKLOCKS GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = ZCL_MDG_BP_HELPER=>gc_bp_model_entity-fkklocks.
    ls_entity_info-get_meth         = 'GET_FKKLOCKS'.
    ls_entity_info-set_meth         = 'SET_FKKLOCKS'.
    ls_entity_info-del_meth         = 'DEL_FKKLOCKS'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_FKKLOCKS'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_FKKLOCKS'.
    ls_entity_info-get_meth_exp_tab = 'ET_FKKLOCKS'.
    ls_entity_info-del_meth_imp_tab = 'IT_FKKLOCKS'.
    ls_entity_info-set_meth_imp_tab = 'IT_FKKLOCKS'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method FKKTAXEX GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = ZCL_MDG_BP_HELPER=>gc_bp_model_entity-fkktaxex.
    ls_entity_info-get_meth         = 'GET_FKKTAXEX'.
    ls_entity_info-set_meth         = 'SET_FKKTAXEX'.
    ls_entity_info-del_meth         = 'DEL_FKKTAXEX'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_FKKTAXEX'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_FKKTAXEX'.
    ls_entity_info-get_meth_exp_tab = 'ET_FKKTAXEX'.
    ls_entity_info-del_meth_imp_tab = 'IT_FKKTAXEX'.
    ls_entity_info-set_meth_imp_tab = 'IT_FKKTAXEX'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method FKKTXT GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = ZCL_MDG_BP_HELPER=>gc_bp_model_entity-fkktxt.
    ls_entity_info-get_meth         = 'GET_FKKTXT'.
    ls_entity_info-set_meth         = 'SET_FKKTXT'.
    ls_entity_info-del_meth         = 'DEL_FKKTXT'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_FKKTXT'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_FKKTXT'.
    ls_entity_info-get_meth_exp_tab = 'ET_FKKTXT'.
    ls_entity_info-del_meth_imp_tab = 'IT_FKKTXT'.
    ls_entity_info-set_meth_imp_tab = 'IT_FKKTXT'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method FKKVK GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = ZCL_MDG_BP_HELPER=>gc_bp_model_entity-fkkvk.
    ls_entity_info-get_meth         = 'GET_FKKVK'.
    ls_entity_info-set_meth         = 'SET_FKKVK'.
    ls_entity_info-del_meth         = 'DEL_FKKVK'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_FKKVK'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_FKKVK'.
    ls_entity_info-get_meth_exp_tab = 'ET_FKKVK'.
    ls_entity_info-del_meth_imp_tab = 'IT_FKKVK'.
    ls_entity_info-set_meth_imp_tab = 'IT_FKKVK'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method FKKVK GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = ZCL_MDG_BP_HELPER=>gc_bp_model_entity-fkkvk.
    ls_entity_info-get_meth         = 'GET_FKKVK'.
    ls_entity_info-set_meth         = 'SET_FKKVK'.
    ls_entity_info-del_meth         = 'DEL_FKKVK'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_FKKVK'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_FKKVK'.
    ls_entity_info-get_meth_exp_tab = 'ET_FKKVK'.
    ls_entity_info-del_meth_imp_tab = 'IT_FKKVK'.
    ls_entity_info-set_meth_imp_tab = 'IT_FKKVK'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method FKKVKCORR GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = ZCL_MDG_BP_HELPER=>gc_bp_model_entity-fkkvkcorr.
    ls_entity_info-get_meth         = 'GET_FKKVKCORR'.
    ls_entity_info-set_meth         = 'SET_FKKVKCORR'.
    ls_entity_info-del_meth         = 'DEL_FKKVKCORR'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_FKKVKCORR'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_FKKVKCORR'.
    ls_entity_info-get_meth_exp_tab = 'ET_FKKVKCORR'.
    ls_entity_info-del_meth_imp_tab = 'IT_FKKVKCORR'.
    ls_entity_info-set_meth_imp_tab = 'IT_FKKVKCORR'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method FKKVKP GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = ZCL_MDG_BP_HELPER=>gc_bp_model_entity-fkkvkp.
    ls_entity_info-get_meth         = 'GET_FKKVKP'.
    ls_entity_info-set_meth         = 'SET_FKKVKP'.
    ls_entity_info-del_meth         = 'DEL_FKKVKP'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_FKKVKP'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_FKKVKP'.
    ls_entity_info-get_meth_exp_tab = 'ET_FKKVKP'.
    ls_entity_info-del_meth_imp_tab = 'IT_FKKVKP'.
    ls_entity_info-set_meth_imp_tab = 'IT_FKKVKP'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method FKKVKTD GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = ZCL_MDG_BP_HELPER=>gc_bp_model_entity-fkkvktd.
    ls_entity_info-get_meth         = 'GET_FKKVKTD'.
    ls_entity_info-set_meth         = 'SET_FKKVKTD'.
    ls_entity_info-del_meth         = 'DEL_FKKVKTD'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_FKKVKTD'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_FKKVKTD'.
    ls_entity_info-get_meth_exp_tab = 'ET_FKKVKTD'.
    ls_entity_info-del_meth_imp_tab = 'IT_FKKVKTD'.
    ls_entity_info-set_meth_imp_tab = 'IT_FKKVKTD'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method VENCCTXT GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-company_code_text.
    ls_entity_info-get_meth         = 'GET_VENCCTXT'.
    ls_entity_info-set_meth         = 'SET_VENCCTXT'.
    ls_entity_info-del_meth         = 'DEL_VENCCTXT'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_VCCTXT'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_VENCCTXT'.
    ls_entity_info-get_meth_exp_tab = 'ET_VENCCTXT'.
    ls_entity_info-del_meth_imp_tab = 'IT_VENCCTXT'.
    ls_entity_info-set_meth_imp_tab = 'IT_VENCCTXT'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method VENGENTXT GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-general_data_text.
    ls_entity_info-get_meth         = 'GET_VENGENTXT'.
    ls_entity_info-set_meth         = 'SET_VENGENTXT'.
    ls_entity_info-del_meth         = 'DEL_VENGENTXT'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_VENTXT'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_VENGENTXT'.
    ls_entity_info-get_meth_exp_tab = 'ET_VENGENTXT'.
    ls_entity_info-del_meth_imp_tab = 'IT_VENGENTXT'.
    ls_entity_info-set_meth_imp_tab = 'IT_VENGENTXT'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method VENPOTXT GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-purchasing_org_text.
    ls_entity_info-get_meth         = 'GET_VENPOTXT'.
    ls_entity_info-set_meth         = 'SET_VENPOTXT'.
    ls_entity_info-del_meth         = 'DEL_VENPOTXT'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_VPOTXT'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_VENPOTXT'.
    ls_entity_info-get_meth_exp_tab = 'ET_VENPOTXT'.
    ls_entity_info-del_meth_imp_tab = 'IT_VENPOTXT'.
    ls_entity_info-set_meth_imp_tab = 'IT_VENPOTXT'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method WP_EMAIL GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-workplace_email.
    ls_entity_info-get_meth         = 'GET_WP_EMAIL'.
    ls_entity_info-set_meth         = 'SET_WP_EMAIL'.
    ls_entity_info-del_meth         = 'DEL_WP_EMAIL'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_WP_EMAIL'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_WP_EMAIL'.
    ls_entity_info-get_meth_exp_tab = 'ET_WP_EMAIL'.
    ls_entity_info-del_meth_imp_tab = 'IT_WP_EMAIL'.
    ls_entity_info-set_meth_imp_tab = 'IT_WP_EMAIL'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method WP_FAX GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-workplace_fax.
    ls_entity_info-get_meth         = 'GET_WP_FAX'.
    ls_entity_info-set_meth         = 'SET_WP_FAX'.
    ls_entity_info-del_meth         = 'DEL_WP_FAX'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_WP_FAX'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_WP_FAX'.
    ls_entity_info-get_meth_exp_tab = 'ET_WP_FAX'.
    ls_entity_info-del_meth_imp_tab = 'IT_WP_FAX'.
    ls_entity_info-set_meth_imp_tab = 'IT_WP_FAX'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method WP_POSTAL GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-workplace_int_addr.
    ls_entity_info-get_meth         = 'GET_WP_POSTAL'.
    ls_entity_info-set_meth         = 'SET_WP_POSTAL'.
    ls_entity_info-del_meth         = 'DEL_WP_POSTAL'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_WP_POSTAL'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_WP_POSTAL'.
    ls_entity_info-get_meth_exp_tab = 'ET_WP_POSTAL'.
    ls_entity_info-del_meth_imp_tab = 'IT_WP_POSTAL'.
    ls_entity_info-set_meth_imp_tab = 'IT_WP_POSTAL'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method WP_TEL GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-workplace_phone.
    ls_entity_info-get_meth         = 'GET_WP_TEL'.
    ls_entity_info-set_meth         = 'SET_WP_TEL'.
    ls_entity_info-del_meth         = 'DEL_WP_TEL'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_WP_TEL'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_WP_TEL'.
    ls_entity_info-get_meth_exp_tab = 'ET_WP_TEL'.
    ls_entity_info-del_meth_imp_tab = 'IT_WP_TEL'.
    ls_entity_info-set_meth_imp_tab = 'IT_WP_TEL'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method WP_URL GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bp_constants~gc_bp_model_entity-workplace_url.
    ls_entity_info-get_meth         = 'GET_WP_URL'.
    ls_entity_info-set_meth         = 'SET_WP_URL'.
    ls_entity_info-del_meth         = 'DEL_WP_URL'.
    ls_entity_info-structure        = '/MDGBP/_S_BP_PP_WP_URL'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_WP_URL'.
    ls_entity_info-get_meth_exp_tab = 'ET_WP_URL'.
    ls_entity_info-del_meth_imp_tab = 'IT_WP_URL'.
    ls_entity_info-set_meth_imp_tab = 'IT_WP_URL'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method CUSSALTXT GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = if_mdg_bs_ecc_bp_constants~gc_cu_model_entity-sales_area_text.
    ls_entity_info-get_meth         = 'GET_CUSSALTXT'.
    ls_entity_info-set_meth         = 'SET_CUSSALTXT'.
    ls_entity_info-del_meth         = 'DEL_CUSSALTXT'.
    ls_entity_info-structure        = '/MDGBPX/_S_BP_PP_BP_CSDTXT'.
    ls_entity_info-tab_type         = 'zif_mdg_bp_datatypes=>gty_T_CUSSALTXT'.
    ls_entity_info-get_meth_exp_tab = 'ET_CUSSALTXT'.
    ls_entity_info-del_meth_imp_tab = 'IT_CUSSALTXT'.
    ls_entity_info-set_meth_imp_tab = 'IT_CUSSALTXT'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

  ENDMETHOD.


  METHOD get_entity_reference.

    CONSTANTS:
      lc_prefix TYPE string VALUE 'GT_'.

    DATA:
     lv_gt_name TYPE seocpdname.

    FIELD-SYMBOLS:
      <lt_entity>  TYPE SORTED TABLE.

    CLEAR: er_entity.

    CONCATENATE lc_prefix iv_entity INTO lv_gt_name.

    ASSIGN (lv_gt_name) TO <lt_entity>.
    IF sy-subrc <> 0.
      RETURN.
    ENDIF.
    GET REFERENCE OF <lt_entity> INTO er_entity.

  ENDMETHOD.


  METHOD get_fkklocks.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_fkklocks, es_fkklocks.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = ZCL_MDG_BP_HELPER=>gc_bp_model_entity-fkklocks
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_fkklocks ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_fkklocks.
      ENDLOOP.
    ELSE .
      et_fkklocks = gt_fkklocks.
    ENDIF.

    IF lines( et_fkklocks ) = 1.
      READ TABLE et_fkklocks INTO es_fkklocks INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_fkktaxex.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_fkktaxex, es_fkktaxex.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = ZCL_MDG_BP_HELPER=>gc_bp_model_entity-fkktaxex
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_fkktaxex ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_fkktaxex.
      ENDLOOP.
    ELSE .
      et_fkktaxex = gt_fkktaxex.
    ENDIF.

    IF lines( et_fkktaxex ) = 1.
      READ TABLE et_fkktaxex INTO es_fkktaxex INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_fkktxt.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_fkktxt, es_fkktxt.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = ZCL_MDG_BP_HELPER=>gc_bp_model_entity-fkktxt
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_fkktxt ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_fkktxt.
      ENDLOOP.
    ELSE .
      et_fkktxt = gt_fkktxt.
    ENDIF.

    IF lines( et_fkktxt ) = 1.
      READ TABLE et_fkktxt INTO es_fkktxt INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_fkkvk.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_fkkvk, es_fkkvk.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = ZCL_MDG_BP_HELPER=>gc_bp_model_entity-fkkvk
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_fkkvk ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_fkkvk.
      ENDLOOP.
    ELSE .
      et_fkkvk = gt_fkkvk.
    ENDIF.

    IF lines( et_fkkvk ) = 1.
      READ TABLE et_fkkvk INTO es_fkkvk INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_fkkvkcorr.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_fkkvkcorr, es_fkkvkcorr.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = ZCL_MDG_BP_HELPER=>gc_bp_model_entity-fkkvkcorr
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_fkkvkcorr ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_fkkvkcorr.
      ENDLOOP.
    ELSE .
      et_fkkvkcorr = gt_fkkvkcorr.
    ENDIF.

    IF lines( et_fkkvkcorr ) = 1.
      READ TABLE et_fkkvkcorr INTO es_fkkvkcorr INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_fkkvkp.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_fkkvkp, es_fkkvkp.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = ZCL_MDG_BP_HELPER=>gc_bp_model_entity-fkkvkp
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_fkkvkp ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_fkkvkp.
      ENDLOOP.
    ELSE .
      et_fkkvkp = gt_fkkvkp.
    ENDIF.

    IF lines( et_fkkvkp ) = 1.
      READ TABLE et_fkkvkp INTO es_fkkvkp INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_fkkvktd.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_fkkvktd, es_fkkvktd.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = ZCL_MDG_BP_HELPER=>gc_bp_model_entity-fkkvktd
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_fkkvktd ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_fkkvktd.
      ENDLOOP.
    ELSE .
      et_fkkvktd = gt_fkkvktd.
    ENDIF.

    IF lines( et_fkkvktd ) = 1.
      READ TABLE et_fkkvktd INTO es_fkkvktd INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_keys_of_entity.

    FIELD-SYMBOLS:
      <ls_entity_keys> TYPE usmd_s_entity_cont.

    CLEAR et_entity_keys.

    READ TABLE gt_entity_keys WITH KEY usmd_entity = iv_entity ASSIGNING <ls_entity_keys>.
    IF sy-subrc = 0.
      APPEND LINES OF <ls_entity_keys>-t_entity_key TO et_entity_keys.
    ENDIF.

  ENDMETHOD.


  METHOD get_key_value_table.

    DATA:
      lt_entity_keys TYPE usmd_t_entity,
      ls_key_value   TYPE zif_mdg_datatypes=>gty_s_key_value.

    FIELD-SYMBOLS:
      <lv_entity_key> TYPE usmd_entity,
      <lv_value>      TYPE any.

    CLEAR et_key_value.

    CALL METHOD get_keys_of_entity
      EXPORTING
        iv_entity      = iv_entity
      IMPORTING
        et_entity_keys = lt_entity_keys.

    LOOP AT lt_entity_keys ASSIGNING <lv_entity_key>.
      ASSIGN COMPONENT <lv_entity_key> OF STRUCTURE is_record TO <lv_value>.
      ls_key_value-key_field = <lv_entity_key>.
      ls_key_value-value     = <lv_value>.
      INSERT ls_key_value INTO TABLE et_key_value.
    ENDLOOP.

  ENDMETHOD.


  METHOD get_vencctxt.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_vencctxt, es_vencctxt.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-company_code_text
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_vencctxt ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_vencctxt.
      ENDLOOP.
    ELSE .
      et_vencctxt = gt_vencctxt.
    ENDIF.

    IF lines( et_vencctxt ) = 1.
      READ TABLE et_vencctxt INTO es_vencctxt INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_vengentxt.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_vengentxt, es_vengentxt.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-general_data_text
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_vengentxt ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_vengentxt.
      ENDLOOP.
    ELSE .
      et_vengentxt = gt_vengentxt.
    ENDIF.

    IF lines( et_vengentxt ) = 1.
      READ TABLE et_vengentxt INTO es_vengentxt INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_venpotxt.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_venpotxt, es_venpotxt.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bs_ecc_bp_constants~gc_sp_model_entity-purchasing_org_text
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_venpotxt ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_venpotxt.
      ENDLOOP.
    ELSE .
      et_venpotxt = gt_venpotxt.
    ENDIF.

    IF lines( et_venpotxt ) = 1.
      READ TABLE et_venpotxt INTO es_venpotxt INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_where_condition.

    DATA:
       lv_key TYPE string.

    FIELD-SYMBOLS:
      <ls_key_value> TYPE zif_mdg_datatypes=>gty_s_key_value.

    CLEAR ev_where.

    IF it_key_value IS NOT INITIAL.
      LOOP AT it_key_value ASSIGNING <ls_key_value>.
        IF <ls_key_value>-value IS NOT INITIAL.
          lv_key = <ls_key_value>-value.
          IF ev_where IS NOT INITIAL.
            CONCATENATE ev_where ' AND ' INTO ev_where RESPECTING BLANKS.
          ENDIF.
          CONCATENATE ev_where  '( ' INTO ev_where RESPECTING BLANKS.
          REPLACE ALL OCCURRENCES OF '''' IN lv_key WITH ''''''.
          CONCATENATE ev_where <ls_key_value>-key_field ' = ' '''' lv_key INTO ev_where RESPECTING BLANKS.
          CONCATENATE ev_where  ''' )' INTO ev_where RESPECTING BLANKS.
        ENDIF.
      ENDLOOP.
    ENDIF.

  ENDMETHOD.


  METHOD get_wp_email.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_wp_email, es_wp_email.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-workplace_email
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_wp_email ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_wp_email.
      ENDLOOP.
    ELSE .
      et_wp_email = gt_wp_email.
    ENDIF.

    IF lines( et_wp_email ) = 1.
      READ TABLE et_wp_email INTO es_wp_email INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_wp_fax.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_wp_fax, es_wp_fax.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-workplace_fax
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_wp_fax ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_wp_fax.
      ENDLOOP.
    ELSE .
      et_wp_fax = gt_wp_fax.
    ENDIF.

    IF lines( et_wp_fax ) = 1.
      READ TABLE et_wp_fax INTO es_wp_fax INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_wp_postal.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_wp_postal, es_wp_postal.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-workplace_int_addr
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_wp_postal ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_wp_postal.
      ENDLOOP.
    ELSE .
      et_wp_postal = gt_wp_postal.
    ENDIF.

    IF lines( et_wp_postal ) = 1.
      READ TABLE et_wp_postal INTO es_wp_postal INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_wp_tel.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_wp_tel, es_wp_tel.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-workplace_phone
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_wp_tel ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_wp_tel.
      ENDLOOP.
    ELSE .
      et_wp_tel = gt_wp_tel.
    ENDIF.

    IF lines( et_wp_tel ) = 1.
      READ TABLE et_wp_tel INTO es_wp_tel INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD get_wp_url.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_wp_url, es_wp_url.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = if_mdg_bp_constants~gc_bp_model_entity-workplace_url
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_wp_url ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_wp_url.
      ENDLOOP.
    ELSE .
      et_wp_url = gt_wp_url.
    ENDIF.

    IF lines( et_wp_url ) = 1.
      READ TABLE et_wp_url INTO es_wp_url INDEX 1 ##ENH_OK.
    ENDIF.

  ENDMETHOD.


  METHOD init_entity_attribute_rel.

    DATA:
      lr_new_table            TYPE REF TO data,
      lr_entity               TYPE REF TO data,
      lr_new_record           TYPE REF TO data,
      lo_strucdescr           TYPE REF TO cl_abap_structdescr,
      lt_components           TYPE abap_compdescr_tab,
      ls_entity_attribute_rel TYPE zif_mdg_datatypes=>gty_s_entity_attributes_rel,
      ls_attribute_entity_rel TYPE zif_mdg_datatypes=>gty_s_attribute_entity_rel,
      lv_attrbiute            TYPE usmd_attribute.

    FIELD-SYMBOLS:
      <lt_entity>      TYPE SORTED TABLE,
      <lv_entity_name> TYPE usmd_entity,
      <lt_new_records> TYPE SORTED TABLE,
      <ls_new_record>  TYPE any,
      <ls_component>   TYPE abap_compdescr.

    LOOP AT get_all_entities( ) ASSIGNING <lv_entity_name>.
      CALL METHOD get_entity_reference
        EXPORTING
          iv_entity = <lv_entity_name>
        IMPORTING
          er_entity = lr_entity.

      IF lr_entity IS NOT BOUND.
        RAISE entity_attribute_not_found.
      ENDIF.

      ASSIGN lr_entity->* TO <lt_entity>.

      CREATE DATA lr_new_table LIKE <lt_entity>.
      ASSIGN lr_new_table->* TO <lt_new_records>.

      CREATE DATA lr_new_record LIKE LINE OF <lt_new_records>.
      ASSIGN lr_new_record->* TO <ls_new_record>.

      lo_strucdescr ?= cl_abap_typedescr=>describe_by_data( p_data = <ls_new_record> ).
      lt_components = lo_strucdescr->components.

      CLEAR: ls_entity_attribute_rel.
      ls_entity_attribute_rel-entity = <lv_entity_name>.

      LOOP AT lt_components ASSIGNING <ls_component>.
        CLEAR: ls_attribute_entity_rel.
        lv_attrbiute = <ls_component>-name.

        INSERT lv_attrbiute INTO TABLE ls_entity_attribute_rel-attributes.

        ls_attribute_entity_rel-attribute = lv_attrbiute.
        ls_attribute_entity_rel-entity = <lv_entity_name>.
        INSERT ls_attribute_entity_rel INTO TABLE gt_attribute_entity_rel.
      ENDLOOP.

      INSERT ls_entity_attribute_rel INTO TABLE gt_entity_attributes_rel.
    ENDLOOP.

  ENDMETHOD.


  METHOD init_entity_keys.

    DATA:
      lo_structdescr TYPE REF TO cl_abap_structdescr,
      lr_data        TYPE REF TO data,
      ls_entity_cont TYPE usmd_s_entity_cont,
      lt_entities    TYPE usmd_t_entity,
      lt_components  TYPE abap_compdescr_tab,
      lv_fieldname   TYPE usmd_fieldname.

    FIELD-SYMBOLS:
      <lv_entity>    TYPE usmd_entity,
      <ls_component> TYPE abap_compdescr,
      <lv_component> TYPE any.

* loop over all type 1 and 4 entites to build table with keys
    LOOP AT get_all_entities( ) ASSIGNING <lv_entity>.
      CLEAR: lv_fieldname, lt_components,
             ls_entity_cont, lt_entities, lr_data.
      UNASSIGN: <lv_component>.

      lv_fieldname = <lv_entity>.

**    get key structure reference of current entity
      CALL METHOD go_model->create_data_reference
        EXPORTING
          i_fieldname = lv_fieldname
          i_struct    = if_usmd_model=>gc_struct_key
          if_table    = abap_false
        IMPORTING
          er_data     = lr_data.

      lo_structdescr ?= cl_abap_typedescr=>describe_by_data_ref( p_data_ref = lr_data ).
      lt_components = lo_structdescr->components.

**     write all key entities of current entity into entity list
      LOOP AT lt_components ASSIGNING <ls_component>.
        ASSIGN COMPONENT 'NAME' OF STRUCTURE <ls_component> TO <lv_component>.
        IF <lv_component> IS ASSIGNED.
          APPEND <lv_component> TO lt_entities.
        ENDIF.
      ENDLOOP.

**      build entity key table
      ls_entity_cont-usmd_entity = <lv_entity>.
      APPEND LINES OF lt_entities TO ls_entity_cont-t_entity_key.
      INSERT ls_entity_cont INTO TABLE gt_entity_keys.
    ENDLOOP.

  ENDMETHOD.


  METHOD init_model.

    CALL METHOD cl_usmd_model_ext=>get_instance
      EXPORTING
        i_usmd_model = if_mdg_bp_constants~gc_bp_model
      IMPORTING
        eo_instance  = go_model.

  ENDMETHOD.


  METHOD limit_key_value_table_entity.

    DATA:
          lt_entity_keys TYPE usmd_t_entity.

    FIELD-SYMBOLS:
      <lv_entity_key> TYPE usmd_entity,
      <ls_key_value>  TYPE zif_mdg_datatypes=>gty_s_key_value.

    CLEAR et_key_value.

    CALL METHOD get_keys_of_entity
      EXPORTING
        iv_entity      = iv_entity
      IMPORTING
        et_entity_keys = lt_entity_keys.

    LOOP AT lt_entity_keys ASSIGNING <lv_entity_key>.
      READ TABLE it_key_value WITH TABLE KEY key_field = <lv_entity_key> ASSIGNING <ls_key_value>.
      IF sy-subrc = 0.
        INSERT <ls_key_value> INTO TABLE et_key_value.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD merge_instance.

    DATA:
      lt_update_param   TYPE abap_parmbind_tab,
      ls_update_param   TYPE abap_parmbind,
      lr_update_tab     TYPE REF TO data,
      lt_source_param   TYPE abap_parmbind_tab,
      ls_source_param   TYPE abap_parmbind,
      lr_source_tab     TYPE REF TO data,
      lr_bp_class_tab   TYPE REF TO data,
      lr_bp_class_struc TYPE REF TO data,
      lt_bp_class_param TYPE abap_parmbind_tab,
      ls_bp_class_param TYPE abap_parmbind.


    FIELD-SYMBOLS:
      <ls_entity_info> TYPE zif_mdg_datatypes=>gty_s_entity_info,
      <lt_orig_data>   TYPE ANY TABLE,
      <lt_add_data>    TYPE ANY TABLE.


    LOOP AT get_entity_info_list( ) ASSIGNING <ls_entity_info>.

* Get Entity data from source cache
      CLEAR: ls_source_param , lt_source_param .
      ls_source_param-name = <ls_entity_info>-get_meth_exp_tab.
      ls_source_param-kind = cl_abap_objectdescr=>importing.
      CREATE DATA lr_source_tab TYPE (<ls_entity_info>-tab_type).
      ASSIGN lr_source_tab->* TO <lt_add_data>.
      IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 000. ENDIF.
      ls_source_param-value = lr_source_tab.
      INSERT ls_source_param INTO TABLE lt_source_param.
      TRY.
          CALL METHOD io_bp_data->(<ls_entity_info>-get_meth)
            PARAMETER-TABLE
            lt_source_param.
        CATCH cx_sy_dyn_call_error.
          MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 001 WITH <ls_entity_info>-get_meth.
      ENDTRY.

* Add source data to original data
      IF <lt_add_data> IS NOT INITIAL.

        CLEAR: ls_bp_class_param, lt_bp_class_param.
        ls_bp_class_param-name = <ls_entity_info>-set_meth_imp_tab.
        ls_bp_class_param-kind = cl_abap_objectdescr=>exporting.
        ls_bp_class_param-value = lr_source_tab.
        INSERT ls_bp_class_param INTO TABLE lt_bp_class_param.

        TRY.
            CALL METHOD me->(<ls_entity_info>-set_meth)
              PARAMETER-TABLE
              lt_bp_class_param.
          CATCH cx_sy_dyn_call_error.
            MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 001 WITH <ls_entity_info>-get_meth.
        ENDTRY.

      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_address.

    FIELD-SYMBOLS:
      <ls_address> TYPE /mdgbp/_s_bp_pp_address.

    LOOP AT it_address ASSIGNING <ls_address> ##ENH_OK.
      READ TABLE gt_address FROM <ls_address> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_address FROM <ls_address>.
      ELSE.
        INSERT <ls_address> INTO TABLE gt_address.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_addrno.

    FIELD-SYMBOLS:
      <ls_addrno> TYPE mdg_bs_addrno.

    LOOP AT it_addrno ASSIGNING <ls_addrno> ##ENH_OK.
      READ TABLE gt_addrno FROM <ls_addrno> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_addrno FROM <ls_addrno>.
      ELSE.
        INSERT <ls_addrno> INTO TABLE gt_addrno.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_ad_email.

    FIELD-SYMBOLS:
      <ls_ad_email> TYPE /mdgbp/_s_bp_pp_ad_email.

    LOOP AT it_ad_email ASSIGNING <ls_ad_email> ##ENH_OK.
      READ TABLE gt_ad_email FROM <ls_ad_email> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_ad_email FROM <ls_ad_email>.
      ELSE.
        INSERT <ls_ad_email> INTO TABLE gt_ad_email.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_ad_fax.

    FIELD-SYMBOLS:
      <ls_ad_fax> TYPE /mdgbp/_s_bp_pp_ad_fax.

    LOOP AT it_ad_fax ASSIGNING <ls_ad_fax> ##ENH_OK.
      READ TABLE gt_ad_fax FROM <ls_ad_fax> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_ad_fax FROM <ls_ad_fax>.
      ELSE.
        INSERT <ls_ad_fax> INTO TABLE gt_ad_fax.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_ad_name_o.

    FIELD-SYMBOLS:
      <ls_ad_name_o> TYPE /mdgbp/_s_bp_pp_ad_name_o.

    LOOP AT it_ad_name_o ASSIGNING  <ls_ad_name_o> ##ENH_OK.
      READ TABLE gt_ad_name_o FROM  <ls_ad_name_o> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_ad_name_o FROM  <ls_ad_name_o>.
      ELSE.
        INSERT <ls_ad_name_o> INTO TABLE gt_ad_name_o.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_ad_name_p.

    FIELD-SYMBOLS:
      <ls_ad_name_p> TYPE /mdgbp/_s_bp_pp_ad_name_p.

    LOOP AT it_ad_name_p ASSIGNING <ls_ad_name_p> ##ENH_OK.
      READ TABLE gt_ad_name_p FROM <ls_ad_name_p> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_ad_name_p FROM <ls_ad_name_p>.
      ELSE.
        INSERT <ls_ad_name_p> INTO TABLE gt_ad_name_p.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_ad_postal.

    FIELD-SYMBOLS:
      <ls_ad_postal> TYPE /mdgbp/_s_bp_pp_ad_postal.

    LOOP AT it_ad_postal ASSIGNING <ls_ad_postal> ##ENH_OK.
      READ TABLE gt_ad_postal FROM <ls_ad_postal> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_ad_postal FROM <ls_ad_postal>.
      ELSE.
        INSERT <ls_ad_postal> INTO TABLE gt_ad_postal.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_ad_tel.

    FIELD-SYMBOLS:
      <ls_ad_tel> TYPE /mdgbp/_s_bp_pp_ad_tel.

    LOOP AT it_ad_tel ASSIGNING  <ls_ad_tel> ##ENH_OK.
      READ TABLE gt_ad_tel FROM <ls_ad_tel> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_ad_tel FROM  <ls_ad_tel> .
      ELSE.
        INSERT <ls_ad_tel> INTO TABLE gt_ad_tel.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_ad_url.

    FIELD-SYMBOLS:
      <ls_ad_url> TYPE /mdgbp/_s_bp_pp_ad_url.

    LOOP AT it_ad_url ASSIGNING <ls_ad_url> ##ENH_OK.
      READ TABLE gt_ad_url FROM <ls_ad_url> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_ad_url FROM <ls_ad_url>.
      ELSE.
        INSERT <ls_ad_url> INTO TABLE gt_ad_url.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_addr.

    FIELD-SYMBOLS:
      <ls_bp_addr> TYPE /mdgbp/_s_bp_pp_bp_addr.

    LOOP AT it_bp_addr ASSIGNING <ls_bp_addr> ##ENH_OK.
      READ TABLE gt_bp_addr FROM <ls_bp_addr> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_addr FROM <ls_bp_addr>.
      ELSE.
        INSERT <ls_bp_addr> INTO TABLE gt_bp_addr.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_addusg.

    FIELD-SYMBOLS:
      <ls_bp_addusg> TYPE /mdgbp/_s_bp_pp_bp_addusg.

    LOOP AT it_bp_addusg ASSIGNING <ls_bp_addusg> ##ENH_OK.
      READ TABLE gt_bp_addusg FROM <ls_bp_addusg> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_addusg FROM <ls_bp_addusg>.
      ELSE.
        INSERT <ls_bp_addusg> INTO TABLE gt_bp_addusg.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_bkdtl.

    FIELD-SYMBOLS:
      <ls_bp_bkdtl> TYPE /mdgbp/_s_bp_pp_bp_bkdtl.

    LOOP AT it_bp_bkdtl ASSIGNING <ls_bp_bkdtl> ##ENH_OK.
      READ TABLE gt_bp_bkdtl FROM <ls_bp_bkdtl> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_bkdtl FROM <ls_bp_bkdtl>.
      ELSE.
        INSERT <ls_bp_bkdtl> INTO TABLE gt_bp_bkdtl.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_ccdtl.

    FIELD-SYMBOLS:
      <ls_bp_ccdtl> TYPE /mdgbp/_s_bp_pp_bp_ccdtl.

    LOOP AT it_bp_ccdtl ASSIGNING <ls_bp_ccdtl> ##ENH_OK.
      READ TABLE gt_bp_ccdtl FROM <ls_bp_ccdtl> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_ccdtl FROM <ls_bp_ccdtl>.
      ELSE.
        INSERT <ls_bp_ccdtl> INTO TABLE gt_bp_ccdtl.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_centrl.

    FIELD-SYMBOLS:
      <ls_bp_centrl> TYPE /mdgbp/_s_bp_pp_bp_centrl.

    LOOP AT it_bp_centrl ASSIGNING <ls_bp_centrl> ##ENH_OK.
      READ TABLE gt_bp_centrl FROM <ls_bp_centrl> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_centrl FROM <ls_bp_centrl>.
      ELSE.
        INSERT <ls_bp_centrl> INTO TABLE gt_bp_centrl.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_compny.

    FIELD-SYMBOLS:
      <ls_bp_compny> TYPE /mdgbpx/_s_bp_pp_bp_compny.

    LOOP AT it_bp_compny ASSIGNING <ls_bp_compny> ##ENH_OK.
      READ TABLE gt_bp_compny FROM <ls_bp_compny> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_compny FROM <ls_bp_compny>.
      ELSE.
        INSERT <ls_bp_compny> INTO TABLE gt_bp_compny.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_cpgen.

    FIELD-SYMBOLS:
      <ls_bp_cpgen> TYPE /mdgbp/_s_bp_pp_bp_cpgen.

    LOOP AT it_bp_cpgen ASSIGNING <ls_bp_cpgen> ##ENH_OK.
      READ TABLE gt_bp_cpgen FROM <ls_bp_cpgen> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_cpgen FROM <ls_bp_cpgen>.
      ELSE.
        INSERT <ls_bp_cpgen> INTO TABLE gt_bp_cpgen.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_cuscla.

    FIELD-SYMBOLS:
      <ls_bp_cuscla> TYPE /mdgbpx/_s_bp_pp_bp_cuscla.

    LOOP AT it_bp_cuscla ASSIGNING <ls_bp_cuscla> ##ENH_OK.
      READ TABLE gt_bp_cuscla FROM <ls_bp_cuscla> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_cuscla FROM <ls_bp_cuscla>.
      ELSE.
        INSERT <ls_bp_cuscla> INTO TABLE gt_bp_cuscla.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_cusddb.

    FIELD-SYMBOLS:
      <ls_bp_cusddb> TYPE /mdgbpx/_s_bp_pp_bp_cusddb.

    LOOP AT it_bp_cusddb ASSIGNING <ls_bp_cusddb> ##ENH_OK.
      READ TABLE gt_bp_cusddb FROM <ls_bp_cusddb> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_cusddb FROM <ls_bp_cusddb>.
      ELSE.
        INSERT <ls_bp_cusddb> INTO TABLE gt_bp_cusddb.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_cusdun.

    FIELD-SYMBOLS:
      <ls_bp_cusdun> TYPE /mdgbpx/_s_bp_pp_bp_cusdun.

    LOOP AT it_bp_cusdun ASSIGNING <ls_bp_cusdun> ##ENH_OK.
      READ TABLE gt_bp_cusdun FROM <ls_bp_cusdun> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_cusdun FROM <ls_bp_cusdun>.
      ELSE.
        INSERT <ls_bp_cusdun> INTO TABLE gt_bp_cusdun.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_cusfcn.

    FIELD-SYMBOLS:
      <ls_bp_cusfcn> TYPE /mdgbpx/_s_bp_pp_bp_cusfcn.

    LOOP AT it_bp_cusfcn ASSIGNING <ls_bp_cusfcn> ##ENH_OK.
      READ TABLE gt_bp_cusfcn FROM <ls_bp_cusfcn> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_cusfcn FROM <ls_bp_cusfcn>.
      ELSE.
        INSERT <ls_bp_cusfcn> INTO TABLE gt_bp_cusfcn.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_cusgen.

    FIELD-SYMBOLS:
      <ls_bp_cusgen> TYPE /mdgbpx/_s_bp_pp_bp_cusgen.

    LOOP AT it_bp_cusgen ASSIGNING <ls_bp_cusgen> ##ENH_OK.
      READ TABLE gt_bp_cusgen FROM <ls_bp_cusgen> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_cusgen FROM <ls_bp_cusgen>.
      ELSE.
        INSERT <ls_bp_cusgen> INTO TABLE gt_bp_cusgen.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_custax.

    FIELD-SYMBOLS:
      <ls_bp_custax> TYPE /mdgbpx/_s_bp_pp_bp_custax.

    LOOP AT it_bp_custax ASSIGNING <ls_bp_custax> ##ENH_OK.
      READ TABLE gt_bp_custax FROM <ls_bp_custax> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_custax FROM <ls_bp_custax>.
      ELSE.
        INSERT <ls_bp_custax> INTO TABLE gt_bp_custax.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_cusulp.

    FIELD-SYMBOLS:
      <ls_bp_cusulp> TYPE /mdgbpx/_s_bp_pp_bp_cusulp.

    LOOP AT it_bp_cusulp ASSIGNING <ls_bp_cusulp> ##ENH_OK.
      READ TABLE gt_bp_cusulp FROM <ls_bp_cusulp> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_cusulp FROM <ls_bp_cusulp>.
      ELSE.
        INSERT <ls_bp_cusulp> INTO TABLE gt_bp_cusulp.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_cusval.

    FIELD-SYMBOLS:
      <ls_bp_cusval> TYPE /mdgbpx/_s_bp_pp_bp_cusval.

    LOOP AT it_bp_cusval ASSIGNING <ls_bp_cusval> ##ENH_OK.
      READ TABLE gt_bp_cusval FROM <ls_bp_cusval> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_cusval FROM <ls_bp_cusval>.
      ELSE.
        INSERT <ls_bp_cusval> INTO TABLE gt_bp_cusval.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_cuswht.

    FIELD-SYMBOLS:
      <ls_bp_cuswht> TYPE /mdgbpx/_s_bp_pp_bp_cuswht.

    LOOP AT it_bp_cuswht ASSIGNING <ls_bp_cuswht> ##ENH_OK.
      READ TABLE gt_bp_cuswht FROM <ls_bp_cuswht> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_cuswht FROM <ls_bp_cuswht>.
      ELSE.
        INSERT <ls_bp_cuswht> INTO TABLE gt_bp_cuswht.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_cus_cc.

    FIELD-SYMBOLS:
      <ls_bp_cus_cc> TYPE /mdgbpx/_s_bp_pp_bp_cus_cc.

    LOOP AT it_bp_cus_cc ASSIGNING <ls_bp_cus_cc> ##ENH_OK.
      READ TABLE gt_bp_cus_cc FROM <ls_bp_cus_cc> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_cus_cc FROM <ls_bp_cus_cc>.
      ELSE.
        INSERT <ls_bp_cus_cc> INTO TABLE gt_bp_cus_cc.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_dunn.

    FIELD-SYMBOLS:
      <ls_bp_dunn> TYPE /mdgbpx/_s_bp_pp_bp_dunn.

    LOOP AT it_bp_dunn ASSIGNING <ls_bp_dunn> ##ENH_OK.
      READ TABLE gt_bp_dunn FROM <ls_bp_dunn> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_dunn FROM <ls_bp_dunn>.
      ELSE.
        INSERT <ls_bp_dunn> INTO TABLE gt_bp_dunn.
      ENDIF.
    ENDLOOP.


  ENDMETHOD.


  METHOD set_bp_header.

    FIELD-SYMBOLS:
      <ls_bp_header> TYPE /mdgbp/_s_bp_pp_bp_header.

    LOOP AT it_bp_header ASSIGNING <ls_bp_header> ##ENH_OK.
      READ TABLE gt_bp_header FROM <ls_bp_header> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_header FROM <ls_bp_header>.
      ELSE.
        INSERT <ls_bp_header> INTO TABLE  gt_bp_header.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_hrchy.

    FIELD-SYMBOLS:
      <ls_bp_hrchy> TYPE /mdgbp/_s_bp_pp_bp_hrchy.

    LOOP AT it_bp_hrchy ASSIGNING <ls_bp_hrchy> ##ENH_OK.
      READ TABLE gt_bp_hrchy FROM <ls_bp_hrchy> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_hrchy FROM <ls_bp_hrchy>.
      ELSE.
        INSERT <ls_bp_hrchy> INTO TABLE  gt_bp_hrchy.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_idnum.

    FIELD-SYMBOLS:
      <ls_bp_idnum> TYPE /mdgbp/_s_bp_pp_bp_idnum.

    LOOP AT it_bp_idnum ASSIGNING <ls_bp_idnum> ##ENH_OK.
      READ TABLE gt_bp_idnum FROM <ls_bp_idnum> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_idnum FROM <ls_bp_idnum>.
      ELSE.
        INSERT <ls_bp_idnum> INTO TABLE gt_bp_idnum.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_indstr.

    FIELD-SYMBOLS:
      <ls_bp_indstr> TYPE /mdgbp/_s_bp_pp_bp_indstr.

    LOOP AT it_bp_indstr ASSIGNING <ls_bp_indstr> ##ENH_OK.
      READ TABLE gt_bp_indstr FROM <ls_bp_indstr> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_indstr FROM <ls_bp_indstr>.
      ELSE.
        INSERT <ls_bp_indstr> INTO TABLE gt_bp_indstr.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_mlt_ad.

    FIELD-SYMBOLS:
      <ls_bp_mlt_ad> TYPE /mdgbpx/_s_bp_pp_bp_mlt_ad.

    LOOP AT it_bp_mlt_ad ASSIGNING <ls_bp_mlt_ad> ##ENH_OK.
      READ TABLE gt_bp_mlt_ad FROM <ls_bp_mlt_ad> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_mlt_ad FROM <ls_bp_mlt_ad>.
      ELSE.
        INSERT <ls_bp_mlt_ad> INTO TABLE gt_bp_mlt_ad.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_mlt_as.

    FIELD-SYMBOLS:
      <ls_bp_mlt_as> TYPE /mdgbpx/_s_bp_pp_bp_mlt_as.

    LOOP AT it_bp_mlt_as ASSIGNING <ls_bp_mlt_as> ##ENH_OK.
      READ TABLE gt_bp_mlt_as FROM <ls_bp_mlt_as> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_mlt_as FROM <ls_bp_mlt_as>.
      ELSE.
        INSERT <ls_bp_mlt_as> INTO TABLE gt_bp_mlt_as.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_porg.

    FIELD-SYMBOLS:
      <ls_bp_porg> TYPE /mdgbpx/_s_bp_pp_bp_porg.

    LOOP AT it_bp_porg ASSIGNING <ls_bp_porg> ##ENH_OK.
      READ TABLE gt_bp_porg FROM <ls_bp_porg> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_porg FROM <ls_bp_porg>.
      ELSE.
        INSERT <ls_bp_porg> INTO TABLE gt_bp_porg.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_porg2.

    FIELD-SYMBOLS:
      <ls_bp_porg2> TYPE /mdgbpx/_s_bp_pp_bp_porg2.

    LOOP AT it_bp_porg2 ASSIGNING <ls_bp_porg2> ##ENH_OK.
      READ TABLE gt_bp_porg2 FROM <ls_bp_porg2> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_porg2 FROM <ls_bp_porg2>.
      ELSE.
        INSERT <ls_bp_porg2> INTO TABLE gt_bp_porg2.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_rel.

    FIELD-SYMBOLS:
      <ls_bp_rel> TYPE /mdgbp/_s_bp_pp_bp_rel.

    LOOP AT it_bp_rel ASSIGNING <ls_bp_rel> ##ENH_OK.
      READ TABLE gt_bp_rel FROM <ls_bp_rel> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_rel FROM <ls_bp_rel>.
      ELSE.
        INSERT <ls_bp_rel> INTO TABLE gt_bp_rel.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_role.

    FIELD-SYMBOLS:
      <ls_bp_role> TYPE /mdgbp/_s_bp_pp_bp_role.

    LOOP AT it_bp_role ASSIGNING <ls_bp_role> ##ENH_OK.
      READ TABLE gt_bp_role FROM <ls_bp_role> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_role FROM <ls_bp_role>.
      ELSE.
        INSERT <ls_bp_role> INTO TABLE gt_bp_role.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_sales.

    FIELD-SYMBOLS:
      <ls_bp_sales> TYPE /mdgbpx/_s_bp_pp_bp_sales.

    LOOP AT it_bp_sales ASSIGNING <ls_bp_sales> ##ENH_OK.
      READ TABLE gt_bp_sales FROM <ls_bp_sales> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_sales FROM <ls_bp_sales>.
      ELSE.
        INSERT <ls_bp_sales> INTO TABLE gt_bp_sales.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_subhry.

    FIELD-SYMBOLS:
      <ls_bp_subhry> TYPE /mdgbp/_s_bp_pp_bp_subhry.

    LOOP AT it_bp_subhry ASSIGNING <ls_bp_subhry> ##ENH_OK.
      READ TABLE gt_bp_subhry FROM <ls_bp_subhry> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_subhry FROM <ls_bp_subhry>.
      ELSE.
        INSERT <ls_bp_subhry> INTO TABLE gt_bp_subhry.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_taxgrp.

    FIELD-SYMBOLS:
      <ls_bp_taxgrp> TYPE /mdgbpx/_s_bp_pp_bp_taxgrp.

    LOOP AT it_bp_taxgrp ASSIGNING <ls_bp_taxgrp> ##ENH_OK.
      READ TABLE gt_bp_taxgrp FROM <ls_bp_taxgrp> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_taxgrp FROM <ls_bp_taxgrp>.
      ELSE.
        INSERT <ls_bp_taxgrp> INTO TABLE gt_bp_taxgrp.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_taxnum.

    FIELD-SYMBOLS:
      <ls_bp_taxnum> TYPE /mdgbp/_s_bp_pp_bp_taxnum.

    LOOP AT it_bp_taxnum ASSIGNING <ls_bp_taxnum> ##ENH_OK.
      READ TABLE gt_bp_taxnum FROM <ls_bp_taxnum> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_taxnum FROM <ls_bp_taxnum>.
      ELSE.
        INSERT <ls_bp_taxnum> INTO TABLE gt_bp_taxnum.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_vencla.

    FIELD-SYMBOLS:
      <ls_bp_vencla> TYPE /mdgbpx/_s_bp_pp_bp_vencla.

    LOOP AT it_bp_vencla ASSIGNING <ls_bp_vencla> ##ENH_OK.
      READ TABLE gt_bp_vencla FROM <ls_bp_vencla> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_vencla FROM <ls_bp_vencla>.
      ELSE.
        INSERT <ls_bp_vencla> INTO TABLE gt_bp_vencla.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_venddb.

    FIELD-SYMBOLS:
      <ls_bp_venddb> TYPE /mdgbpx/_s_bp_pp_bp_venddb.

    LOOP AT it_bp_venddb ASSIGNING <ls_bp_venddb> ##ENH_OK.
      READ TABLE gt_bp_venddb FROM <ls_bp_venddb> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_venddb FROM <ls_bp_venddb>.
      ELSE.
        INSERT <ls_bp_venddb> INTO TABLE gt_bp_venddb.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_venfcn.

    FIELD-SYMBOLS:
      <ls_bp_venfcn> TYPE /mdgbpx/_s_bp_pp_bp_venfcn.

    LOOP AT it_bp_venfcn ASSIGNING <ls_bp_venfcn> ##ENH_OK.
      READ TABLE gt_bp_venfcn FROM <ls_bp_venfcn> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_venfcn FROM <ls_bp_venfcn>.
      ELSE.
        INSERT <ls_bp_venfcn> INTO TABLE gt_bp_venfcn.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_vengen.

    FIELD-SYMBOLS:
      <ls_bp_vengen> TYPE /mdgbpx/_s_bp_pp_bp_vengen.

    LOOP AT it_bp_vengen ASSIGNING <ls_bp_vengen> ##ENH_OK.
      READ TABLE gt_bp_vengen FROM <ls_bp_vengen> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_vengen FROM <ls_bp_vengen>.
      ELSE.
        INSERT <ls_bp_vengen> INTO TABLE gt_bp_vengen.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_vensub.

    FIELD-SYMBOLS:
      <ls_bp_vensub> TYPE /mdgbpx/_s_bp_pp_bp_vensub.

    LOOP AT it_bp_vensub ASSIGNING <ls_bp_vensub> ##ENH_OK.
      READ TABLE gt_bp_vensub FROM <ls_bp_vensub> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_vensub FROM <ls_bp_vensub>.
      ELSE.
        INSERT <ls_bp_vensub> INTO TABLE gt_bp_vensub.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_venval.

    FIELD-SYMBOLS:
      <ls_bp_venval> TYPE /mdgbpx/_s_bp_pp_bp_venval.

    LOOP AT it_bp_venval ASSIGNING <ls_bp_venval> ##ENH_OK.
      READ TABLE gt_bp_venval FROM <ls_bp_venval> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_venval FROM <ls_bp_venval>.
      ELSE.
        INSERT <ls_bp_venval> INTO TABLE gt_bp_venval.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_whtax.

    FIELD-SYMBOLS:
      <ls_bp_whtax> TYPE /mdgbpx/_s_bp_pp_bp_whtax.

    LOOP AT it_bp_whtax ASSIGNING <ls_bp_whtax> ##ENH_OK.
      READ TABLE gt_bp_whtax FROM <ls_bp_whtax> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_whtax FROM <ls_bp_whtax>.
      ELSE.
        INSERT <ls_bp_whtax> INTO TABLE gt_bp_whtax.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_bp_wpad.

    FIELD-SYMBOLS:
      <ls_bp_wpad> TYPE /mdgbp/_s_bp_pp_bp_wpad.

    LOOP AT it_bp_wpad ASSIGNING <ls_bp_wpad> ##ENH_OK.
      READ TABLE gt_bp_wpad FROM <ls_bp_wpad> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bp_wpad FROM <ls_bp_wpad>.
      ELSE.
        INSERT <ls_bp_wpad> INTO TABLE gt_bp_wpad.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_cuscctxt.

    FIELD-SYMBOLS:
      <ls_cuscctxt> TYPE /mdgbpx/_s_bp_pp_bp_ccctxt.

    LOOP AT it_cuscctxt ASSIGNING <ls_cuscctxt> ##ENH_OK.
      READ TABLE gt_cuscctxt FROM <ls_cuscctxt> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_cuscctxt FROM <ls_cuscctxt>.
      ELSE.
        INSERT <ls_cuscctxt> INTO TABLE gt_cuscctxt.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_cusgentxt.

    FIELD-SYMBOLS:
      <ls_cusgentxt> TYPE /mdgbpx/_s_bp_pp_bp_custxt.

    LOOP AT it_cusgentxt ASSIGNING <ls_cusgentxt> ##ENH_OK.
      READ TABLE gt_cusgentxt FROM <ls_cusgentxt> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_cusgentxt FROM <ls_cusgentxt>.
      ELSE.
        INSERT <ls_cusgentxt> INTO TABLE gt_cusgentxt.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_cussaltxt.

    FIELD-SYMBOLS:
      <ls_cussaltxt> TYPE /mdgbpx/_s_bp_pp_bp_csdtxt.

    LOOP AT it_cussaltxt ASSIGNING <ls_cussaltxt> ##ENH_OK.
      READ TABLE gt_cussaltxt FROM <ls_cussaltxt> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_cussaltxt FROM <ls_cussaltxt>.
      ELSE.
        INSERT <ls_cussaltxt> INTO TABLE gt_cussaltxt.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_fkklocks.

    FIELD-SYMBOLS:
      <ls_fkklocks> TYPE /mdgbpx/_s_bp_pp_fkklocks.

    LOOP AT it_fkklocks ASSIGNING <ls_fkklocks> ##ENH_OK.
      READ TABLE gt_fkklocks FROM <ls_fkklocks> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_fkklocks FROM <ls_fkklocks>.
      ELSE.
        INSERT <ls_fkklocks> INTO TABLE gt_fkklocks.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_fkktaxex.

    FIELD-SYMBOLS:
      <ls_fkktaxex> TYPE /mdgbpx/_s_bp_pp_fkktaxex.

    LOOP AT it_fkktaxex ASSIGNING <ls_fkktaxex> ##ENH_OK.
      READ TABLE gt_fkktaxex FROM <ls_fkktaxex> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_fkktaxex FROM <ls_fkktaxex>.
      ELSE.
        INSERT <ls_fkktaxex> INTO TABLE gt_fkktaxex.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_fkktxt.

    FIELD-SYMBOLS:
       <ls_fkktxt> TYPE /mdgbpx/_s_bp_pp_fkktxt.

    LOOP AT it_fkktxt ASSIGNING <ls_fkktxt> ##ENH_OK.
      READ TABLE gt_fkktxt FROM <ls_fkktxt> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_fkktxt FROM <ls_fkktxt>.
      ELSE.
        INSERT <ls_fkktxt> INTO TABLE gt_fkktxt.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_fkkvk.

    FIELD-SYMBOLS:
      <ls_fkkvk> TYPE /mdgbpx/_s_bp_pp_fkkvk.

    LOOP AT it_fkkvk ASSIGNING <ls_fkkvk> ##ENH_OK.
      READ TABLE gt_fkkvk FROM <ls_fkkvk> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_fkkvk FROM <ls_fkkvk>.
      ELSE.
        INSERT <ls_fkkvk> INTO TABLE gt_fkkvk.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_fkkvkcorr.

    FIELD-SYMBOLS:
      <ls_fkkvkcorr> TYPE /mdgbpx/_s_bp_pp_fkkvkcorr.

    LOOP AT it_fkkvkcorr ASSIGNING <ls_fkkvkcorr> ##ENH_OK.
      READ TABLE gt_fkkvkcorr FROM <ls_fkkvkcorr> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_fkkvkcorr FROM <ls_fkkvkcorr>.
      ELSE.
        INSERT <ls_fkkvkcorr> INTO TABLE gt_fkkvkcorr.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_fkkvkp.

    FIELD-SYMBOLS:
      <ls_fkkvkp> TYPE /mdgbpx/_s_bp_pp_fkkvkp.

    LOOP AT it_fkkvkp ASSIGNING <ls_fkkvkp> ##ENH_OK.
      READ TABLE gt_fkkvkp FROM <ls_fkkvkp> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_fkkvkp FROM <ls_fkkvkp>.
      ELSE.
        INSERT <ls_fkkvkp> INTO TABLE gt_fkkvkp.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_fkkvktd.

    FIELD-SYMBOLS:
      <ls_fkkvktd> TYPE /mdgbpx/_s_bp_pp_fkkvktd.

    LOOP AT it_fkkvktd ASSIGNING <ls_fkkvktd> ##ENH_OK.
      READ TABLE gt_fkkvktd FROM <ls_fkkvktd> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_fkkvktd FROM <ls_fkkvktd>.
      ELSE.
        INSERT <ls_fkkvktd> INTO TABLE gt_fkkvktd.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_vencctxt.

    FIELD-SYMBOLS:
      <ls_vencctxt> TYPE /mdgbpx/_s_bp_pp_bp_vcctxt.

    LOOP AT it_vencctxt ASSIGNING <ls_vencctxt> ##ENH_OK.
      READ TABLE gt_vencctxt FROM <ls_vencctxt> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_vencctxt FROM <ls_vencctxt>.
      ELSE.
        INSERT <ls_vencctxt> INTO TABLE gt_vencctxt.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_vengentxt.

    FIELD-SYMBOLS:
      <ls_vengentxt> TYPE /mdgbpx/_s_bp_pp_bp_ventxt.

    LOOP AT it_vengentxt ASSIGNING <ls_vengentxt> ##ENH_OK.
      READ TABLE gt_vengentxt FROM <ls_vengentxt> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_vengentxt FROM <ls_vengentxt>.
      ELSE.
        INSERT <ls_vengentxt> INTO TABLE gt_vengentxt.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_venpotxt.

    FIELD-SYMBOLS:
      <ls_venpotxt> TYPE /mdgbpx/_s_bp_pp_bp_vpotxt.

    LOOP AT it_venpotxt ASSIGNING <ls_venpotxt> ##ENH_OK.
      READ TABLE gt_venpotxt FROM <ls_venpotxt> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_venpotxt FROM <ls_venpotxt>.
      ELSE.
        INSERT <ls_venpotxt> INTO TABLE gt_venpotxt.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_wp_email.

    FIELD-SYMBOLS:
      <ls_wp_email> TYPE /mdgbp/_s_bp_pp_wp_email.

    LOOP AT it_wp_email ASSIGNING <ls_wp_email> ##ENH_OK.
      READ TABLE gt_wp_email FROM <ls_wp_email> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_wp_email FROM <ls_wp_email>.
      ELSE.
        INSERT <ls_wp_email> INTO TABLE gt_wp_email.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_wp_fax.

    FIELD-SYMBOLS:
      <ls_wp_fax> TYPE /mdgbp/_s_bp_pp_wp_fax.

    LOOP AT it_wp_fax ASSIGNING <ls_wp_fax> ##ENH_OK.
      READ TABLE gt_wp_fax FROM <ls_wp_fax> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_wp_fax FROM <ls_wp_fax>.
      ELSE.
        INSERT <ls_wp_fax> INTO TABLE gt_wp_fax.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_wp_postal.

    FIELD-SYMBOLS:
      <ls_wp_postal> TYPE /mdgbp/_s_bp_pp_wp_postal.

    LOOP AT it_wp_postal ASSIGNING <ls_wp_postal> ##ENH_OK.
      READ TABLE gt_wp_postal FROM <ls_wp_postal> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_wp_postal FROM <ls_wp_postal>.
      ELSE.
        INSERT <ls_wp_postal> INTO TABLE gt_wp_postal.
      ENDIF.
    ENDLOOP.
  ENDMETHOD.


  METHOD set_wp_tel.

    FIELD-SYMBOLS:
      <ls_wp_tel> TYPE /mdgbp/_s_bp_pp_wp_tel.

    LOOP AT it_wp_tel ASSIGNING <ls_wp_tel> ##ENH_OK.
      READ TABLE gt_wp_tel FROM <ls_wp_tel> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_wp_tel FROM <ls_wp_tel>.
      ELSE.
        INSERT <ls_wp_tel> INTO TABLE gt_wp_tel.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_wp_url.

    FIELD-SYMBOLS:
      <ls_wp_url> TYPE /mdgbp/_s_bp_pp_wp_url.

    LOOP AT it_wp_url ASSIGNING <ls_wp_url> ##ENH_OK.
      READ TABLE gt_wp_url FROM <ls_wp_url> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_wp_url FROM <ls_wp_url>.
      ELSE.
        INSERT <ls_wp_url> INTO TABLE gt_wp_url.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.
ENDCLASS.