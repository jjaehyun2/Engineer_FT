class ZCL_MDG_MM_HELPER definition
  public
  create private

  global friends ZCL_MDG_MM_HELPER_ACTIVE
                 ZCL_MDG_MM_HELPER_STAGING .

public section.

  interfaces IF_MDG_BS_MAT_GEN_C .

  constants:
    BEGIN OF cs_entities,
        material_txt TYPE usmd_entity VALUE 'MATTXT',
        maraqtmng    TYPE usmd_entity VALUE 'MARAQTMNG',
        dradbasic    TYPE usmd_entity VALUE 'DRADBASIC',
        dradtxt      TYPE usmd_entity VALUE 'DRADTXT',
        maraspm      TYPE usmd_entity VALUE 'MARASPM',
        marastor     TYPE usmd_entity VALUE 'MARASTOR',
        marcpurch    TYPE usmd_entity VALUE 'MARCPURCH',
        marcstore    TYPE usmd_entity VALUE 'MARCSTORE',
        matchgmng    TYPE usmd_entity VALUE 'MATCHGMNG',
      END OF cs_entities .
  constants:
    BEGIN OF cs_fields,
        material_txt TYPE usmd_fieldname VALUE 'MATTXT',
        maraqtmng    TYPE usmd_fieldname VALUE 'MARAQTMNG',
        dradbasic    TYPE usmd_fieldname VALUE 'DRADBASIC',
        dradtxt      TYPE usmd_fieldname VALUE 'DRADTXT',
        maraspm      TYPE usmd_fieldname VALUE 'MARASPM',
        marastor     TYPE usmd_fieldname VALUE 'MARASTOR',
        marcpurch    TYPE usmd_fieldname VALUE 'MARCPURCH',
        marcstore    TYPE usmd_fieldname VALUE 'MARCSTORE',
        matchgmng    TYPE usmd_fieldname VALUE 'MATCHGMNG',
      END OF cs_fields .
  constants:
    BEGIN OF cs_material_types,
        production_material   TYPE mtart VALUE 'Z001',
        packaging             TYPE mtart VALUE 'Z002',
        service_product       TYPE mtart VALUE 'Z003',
        non_stock_materials   TYPE mtart VALUE 'Z004',
        spare_parts           TYPE mtart VALUE 'Z005',
        nonvaluated_materials TYPE mtart VALUE 'Z006',
        returnable_packaging  TYPE mtart VALUE 'Z007',
        production_resource   TYPE mtart VALUE 'Z008',
      END OF cs_material_types .
  constants:
    BEGIN OF cs_lab_office,
        npp TYPE labor VALUE '021',
      END OF cs_lab_office .
  constants:
    BEGIN OF cs_cr_types,
        create_npp_master_data TYPE usmd_crequest_type VALUE 'ZMATNP01',
      END OF cs_cr_types .

  methods COMPARE_INSTANCE
    importing
      !IO_MAT_DATA type ref to ZCL_MDG_MM_HELPER
    exporting
      !ET_CHANGED_ENTITIES type ZIF_MDG_DATATYPES=>GTY_T_ENTITY_DATA
      !ET_DELETED_ENTITIES type ZIF_MDG_DATATYPES=>GTY_T_ENTITY_DATA
      !ET_CHANGED_FIELDS type ZIF_MDG_DATATYPES=>GTY_T_ENTITY_ATTRIBUTE .
  methods COPY_INSTANCE
    returning
      value(RO_MAT_DATA) type ref to ZCL_MDG_MM_HELPER
    exceptions
      ATTRIBUTE_ASSIGNMENT_ERROR
      VALUE_TRANSFER_ERROR .
  methods DEL_BSCDATTXT
    importing
      !IT_BSCDATTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_BSCDATTXT .
  methods DEL_CLASSASGN
    importing
      !IT_CLASSASGN type ZIF_MDG_MM_DATATYPES=>GTY_T_CLASSASGN .
  methods DEL_DRADBASIC
    importing
      !IT_DRADBASIC type ZIF_MDG_MM_DATATYPES=>GTY_T_DRADBASIC .
  methods DEL_DRADTXT
    importing
      !IT_DRADTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_DRADTXT .
  methods DEL_INTCMNT
    importing
      !IT_INTCMNT type ZIF_MDG_MM_DATATYPES=>GTY_T_INTCMNT .
  methods DEL_MARAPURCH
    importing
      !IT_MARAPURCH type ZIF_MDG_MM_DATATYPES=>GTY_T_MARAPURCH .
  methods DEL_MARAQTMNG
    importing
      !IT_MARAQTMNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MARAQTMNG .
  methods DEL_MARASALES
    importing
      !IT_MARASALES type ZIF_MDG_MM_DATATYPES=>GTY_T_MARASALES .
  methods DEL_MARASPM
    importing
      !IT_MARASPM type ZIF_MDG_MM_DATATYPES=>GTY_T_MARASPM .
  methods DEL_MARASTOR
    importing
      !IT_MARASTOR type ZIF_MDG_MM_DATATYPES=>GTY_T_MARASTOR .
  methods DEL_MARCATP
    importing
      !IT_MARCATP type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCATP .
  methods DEL_MARCBASIC
    importing
      !IT_MARCBASIC type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCBASIC .
  methods DEL_MARCCSTNG
    importing
      !IT_MARCCSTNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCCSTNG .
  methods DEL_MARCFRCST
    importing
      !IT_MARCFRCST type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCFRCST .
  methods DEL_MARCFRGTR
    importing
      !IT_MARCFRGTR type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCFRGTR .
  methods DEL_MARCFRPAR
    importing
      !IT_MARCFRPAR type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCFRPAR .
  methods DEL_MARCMRPFC
    importing
      !IT_MARCMRPFC type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCMRPFC .
  methods DEL_MARCMRPLS
    importing
      !IT_MARCMRPLS type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCMRPLS .
  methods DEL_MARCMRPMI
    importing
      !IT_MARCMRPMI type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCMRPMI .
  methods DEL_MARCMRPPP
    importing
      !IT_MARCMRPPP type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCMRPPP .
  methods DEL_MARCMRPSP
    importing
      !IT_MARCMRPSP type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCMRPSP .
  methods DEL_MARCPRT
    importing
      !IT_MARCPRT type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCPRT .
  methods DEL_MARCPURCH
    importing
      !IT_MARCPURCH type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCPURCH .
  methods DEL_MARCQTMNG
    importing
      !IT_MARCQTMNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCQTMNG .
  methods DEL_MARCSALES
    importing
      !IT_MARCSALES type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCSALES .
  methods DEL_MARCSTORE
    importing
      !IT_MARCSTORE type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCSTORE .
  methods DEL_MARCWRKSD
    importing
      !IT_MARCWRKSD type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCWRKSD .
  methods DEL_MARDMRP
    importing
      !IT_MARDMRP type ZIF_MDG_MM_DATATYPES=>GTY_T_MARDMRP .
  methods DEL_MARDSTOR
    importing
      !IT_MARDSTOR type ZIF_MDG_MM_DATATYPES=>GTY_T_MARDSTOR .
  methods DEL_MATCHGMNG
    importing
      !IT_MATCHGMNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MATCHGMNG .
  methods DEL_MATERIAL
    importing
      !IT_MATERIAL type ZIF_MDG_MM_DATATYPES=>GTY_T_MATERIAL .
  methods DEL_MATTXT
    importing
      !IT_MATTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_MATTXT .
  methods DEL_MBEWACTNG
    importing
      !IT_MBEWACTNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MBEWACTNG .
  methods DEL_MBEWCSTNG
    importing
      !IT_MBEWCSTNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MBEWCSTNG .
  methods DEL_MBEWMLAC
    importing
      !IT_MBEWMLAC type ZIF_MDG_MM_DATATYPES=>GTY_T_MBEWMLAC .
  methods DEL_MBEWMLVAL
    importing
      !IT_MBEWMLVAL type ZIF_MDG_MM_DATATYPES=>GTY_T_MBEWMLVAL .
  methods DEL_MBEWVALUA
    importing
      !IT_MBEWVALUA type ZIF_MDG_MM_DATATYPES=>GTY_T_MBEWVALUA .
  methods DEL_MDMABASIC
    importing
      !IT_MDMABASIC type ZIF_MDG_MM_DATATYPES=>GTY_T_MDMABASIC .
  methods DEL_MEAN_GTIN
    importing
      !IT_MEAN_GTIN type ZIF_MDG_MM_DATATYPES=>GTY_T_MEAN_GTIN .
  methods DEL_MKALBASIC
    importing
      !IT_MKALBASIC type ZIF_MDG_MM_DATATYPES=>GTY_T_MKALBASIC .
  methods DEL_MLANPURCH
    importing
      !IT_MLANPURCH type ZIF_MDG_MM_DATATYPES=>GTY_T_MLANPURCH .
  methods DEL_MLANSALES
    importing
      !IT_MLANSALES type ZIF_MDG_MM_DATATYPES=>GTY_T_MLANSALES .
  methods DEL_MLGNSTOR
    importing
      !IT_MLGNSTOR type ZIF_MDG_MM_DATATYPES=>GTY_T_MLGNSTOR .
  methods DEL_MLGTSTOR
    importing
      !IT_MLGTSTOR type ZIF_MDG_MM_DATATYPES=>GTY_T_MLGTSTOR .
  methods DEL_MPGDPRODG
    importing
      !IT_MPGDPRODG type ZIF_MDG_MM_DATATYPES=>GTY_T_MPGDPRODG .
  methods DEL_MRPTXT
    importing
      !IT_MRPTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_MRPTXT .
  methods DEL_MVKEGRPNG
    importing
      !IT_MVKEGRPNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MVKEGRPNG .
  methods DEL_MVKESALES
    importing
      !IT_MVKESALES type ZIF_MDG_MM_DATATYPES=>GTY_T_MVKESALES .
  methods DEL_PURCHTXT
    importing
      !IT_PURCHTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_PURCHTXT .
  methods DEL_QINSPTXT
    importing
      !IT_QINSPTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_QINSPTXT .
  methods DEL_QMATBASIC
    importing
      !IT_QMATBASIC type ZIF_MDG_MM_DATATYPES=>GTY_T_QMATBASIC .
  methods DEL_SALESTXT
    importing
      !IT_SALESTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_SALESTXT .
  methods DEL_UNITOFMSR
    importing
      !IT_UNITOFMSR type ZIF_MDG_MM_DATATYPES=>GTY_T_UNITOFMSR .
  methods DEL_VALUATION
    importing
      !IT_VALUATION type ZIF_MDG_MM_DATATYPES=>GTY_T_VALUATION .
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
  methods GET_BSCDATTXT
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_BSCDATTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_BSCDATTXT
      !ES_BSCDATTXT type /MDGMM/_S_MM_PP_BSCDATTXT .
  methods GET_CLASSASGN
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_CLASSASGN type ZIF_MDG_MM_DATATYPES=>GTY_T_CLASSASGN
      !ES_CLASSASGN type /MDGMM/_S_MM_PP_CLASSASGN .
  methods GET_DRADBASIC
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_DRADBASIC type ZIF_MDG_MM_DATATYPES=>GTY_T_DRADBASIC
      !ES_DRADBASIC type /MDGMM/_S_MM_PP_DRADBASIC .
  methods GET_DRADTXT
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_DRADTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_DRADTXT
      !ES_DRADTXT type /MDGMM/_S_MM_PP_DRADTXT .
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
  methods GET_INTCMNT
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_INTCMNT type ZIF_MDG_MM_DATATYPES=>GTY_T_INTCMNT
      !ES_INTCMNT type /MDGMM/_S_MM_PP_INTCMNT .
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
  methods GET_MARAPURCH
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARAPURCH type ZIF_MDG_MM_DATATYPES=>GTY_T_MARAPURCH
      !ES_MARAPURCH type /MDGMM/_S_MM_PP_MARAPURCH .
  methods GET_MARAQTMNG
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARAQTMNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MARAQTMNG
      !ES_MARAQTMNG type /MDGMM/_S_MM_PP_MARAQTMNG .
  methods GET_MARASALES
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARASALES type ZIF_MDG_MM_DATATYPES=>GTY_T_MARASALES
      !ES_MARASALES type /MDGMM/_S_MM_PP_MARASALES .
  methods GET_MARASPM
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARASPM type ZIF_MDG_MM_DATATYPES=>GTY_T_MARASPM
      !ES_MARASPM type /MDGMM/_S_MM_PP_MARASPM .
  methods GET_MARASTOR
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARASTOR type ZIF_MDG_MM_DATATYPES=>GTY_T_MARASTOR
      !ES_MARASTOR type /MDGMM/_S_MM_PP_MARASTOR .
  methods GET_MARCATP
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARCATP type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCATP
      !ES_MARCATP type /MDGMM/_S_MM_PP_MARCATP .
  methods GET_MARCBASIC
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARCBASIC type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCBASIC
      !ES_MARCBASIC type /MDGMM/_S_MM_PP_MARCBASIC .
  methods GET_MARCCSTNG
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARCCSTNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCCSTNG
      !ES_MARCCSTNG type /MDGMM/_S_MM_PP_MARCCSTNG .
  methods GET_MARCFRCST
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARCFRCST type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCFRCST
      !ES_MARCFRCST type /MDGMM/_S_MM_PP_MARCFRCST .
  methods GET_MARCFRGTR
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARCFRGTR type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCFRGTR
      !ES_MARCFRGTR type /MDGMM/_S_MM_PP_MARCFRGTR .
  methods GET_MARCFRPAR
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARCFRPAR type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCFRPAR
      !ES_MARCFRPAR type /MDGMM/_S_MM_PP_MARCFRPAR .
  methods GET_MARCMRPFC
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARCMRPFC type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCMRPFC
      !ES_MARCMRPFC type /MDGMM/_S_MM_PP_MARCMRPFC .
  methods GET_MARCMRPLS
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARCMRPLS type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCMRPLS
      !ES_MARCMRPLS type /MDGMM/_S_MM_PP_MARCMRPLS .
  methods GET_MARCMRPMI
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARCMRPMI type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCMRPMI
      !ES_MARCMRPMI type /MDGMM/_S_MM_PP_MARCMRPMI .
  methods GET_MARCMRPPP
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARCMRPPP type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCMRPPP
      !ES_MARCMRPPP type /MDGMM/_S_MM_PP_MARCMRPPP .
  methods GET_MARCMRPSP
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARCMRPSP type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCMRPSP
      !ES_MARCMRPSP type /MDGMM/_S_MM_PP_MARCMRPSP .
  methods GET_MARCPRT
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARCPRT type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCPRT
      !ES_MARCPRT type /MDGMM/_S_MM_PP_MARCPRT .
  methods GET_MARCPURCH
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARCPURCH type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCPURCH
      !ES_MARCPURCH type /MDGMM/_S_MM_PP_MARCPURCH .
  methods GET_MARCQTMNG
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARCQTMNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCQTMNG
      !ES_MARCQTMNG type /MDGMM/_S_MM_PP_MARCQTMNG .
  methods GET_MARCSALES
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARCSALES type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCSALES
      !ES_MARCSALES type /MDGMM/_S_MM_PP_MARCSALES .
  methods GET_MARCSTORE
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARCSTORE type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCSTORE
      !ES_MARCSTORE type /MDGMM/_S_MM_PP_MARCSTORE .
  methods GET_MARCWRKSD
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARCWRKSD type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCWRKSD
      !ES_MARCWRKSD type /MDGMM/_S_MM_PP_MARCWRKSD .
  methods GET_MARDMRP
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARDMRP type ZIF_MDG_MM_DATATYPES=>GTY_T_MARDMRP
      !ES_MARDMRP type /MDGMM/_S_MM_PP_MARDMRP .
  methods GET_MARDSTOR
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MARDSTOR type ZIF_MDG_MM_DATATYPES=>GTY_T_MARDSTOR
      !ES_MARDSTOR type /MDGMM/_S_MM_PP_MARDSTOR .
  methods GET_MATCHGMNG
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MATCHGMNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MATCHGMNG
      !ES_MATCHGMNG type /MDGMM/_S_MM_PP_MATCHGMNG .
  methods GET_MATERIAL
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MATERIAL type ZIF_MDG_MM_DATATYPES=>GTY_T_MATERIAL
      !ES_MATERIAL type /MDGMM/_S_MM_PP_MATERIAL .
  methods GET_MATTXT
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MATTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_MATTXT
      !ES_MATTXT type /MDGMM/_ST_MM_PP_MATERIAL .
  methods GET_MBEWACTNG
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MBEWACTNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MBEWACTNG
      !ES_MBEWACTNG type /MDGMM/_S_MM_PP_MBEWACTNG .
  methods GET_MBEWCSTNG
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MBEWCSTNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MBEWCSTNG
      !ES_MBEWCSTNG type /MDGMM/_S_MM_PP_MBEWCSTNG .
  methods GET_MBEWMLAC
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MBEWMLAC type ZIF_MDG_MM_DATATYPES=>GTY_T_MBEWMLAC
      !ES_MBEWMLAC type /MDGMM/_S_MM_PP_MBEWMLAC .
  methods GET_MBEWMLVAL
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MBEWMLVAL type ZIF_MDG_MM_DATATYPES=>GTY_T_MBEWMLVAL
      !ES_MBEWMLVAL type /MDGMM/_S_MM_PP_MBEWMLVAL .
  methods GET_MBEWVALUA
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MBEWVALUA type ZIF_MDG_MM_DATATYPES=>GTY_T_MBEWVALUA
      !ES_MBEWVALUA type /MDGMM/_S_MM_PP_MBEWVALUA .
  methods GET_MDMABASIC
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MDMABASIC type ZIF_MDG_MM_DATATYPES=>GTY_T_MDMABASIC
      !ES_MDMABASIC type /MDGMM/_S_MM_PP_MDMABASIC .
  methods GET_MEAN_GTIN
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MEAN_GTIN type ZIF_MDG_MM_DATATYPES=>GTY_T_MEAN_GTIN
      !ES_MEAN_GTIN type /MDGMM/_S_MM_PP_MEAN_GTIN .
  methods GET_MKALBASIC
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MKALBASIC type ZIF_MDG_MM_DATATYPES=>GTY_T_MKALBASIC
      !ES_MKALBASIC type /MDGMM/_S_MM_PP_MKALBASIC .
  methods GET_MLANPURCH
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MLANPURCH type ZIF_MDG_MM_DATATYPES=>GTY_T_MLANPURCH
      !ES_MLANPURCH type /MDGMM/_S_MM_PP_MLANPURCH .
  methods GET_MLANSALES
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MLANSALES type ZIF_MDG_MM_DATATYPES=>GTY_T_MLANSALES
      !ES_MLANSALES type /MDGMM/_S_MM_PP_MLANSALES .
  methods GET_MLGNSTOR
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MLGNSTOR type ZIF_MDG_MM_DATATYPES=>GTY_T_MLGNSTOR
      !ES_MLGNSTOR type /MDGMM/_S_MM_PP_MLGNSTOR .
  methods GET_MLGTSTOR
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MLGTSTOR type ZIF_MDG_MM_DATATYPES=>GTY_T_MLGTSTOR
      !ES_MLGTSTOR type /MDGMM/_S_MM_PP_MLGTSTOR .
  methods GET_MPGDPRODG
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MPGDPRODG type ZIF_MDG_MM_DATATYPES=>GTY_T_MPGDPRODG
      !ES_MPGDPRODG type /MDGMM/_S_MM_PP_MPGDPRODG .
  methods GET_MRPTXT
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MRPTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_MRPTXT
      !ES_MRPTXT type /MDGMM/_S_MM_PP_MRPTXT .
  methods GET_MVKEGRPNG
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MVKEGRPNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MVKEGRPNG
      !ES_MVKEGRPNG type /MDGMM/_S_MM_PP_MVKEGRPNG .
  methods GET_MVKESALES
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_MVKESALES type ZIF_MDG_MM_DATATYPES=>GTY_T_MVKESALES
      !ES_MVKESALES type /MDGMM/_S_MM_PP_MVKESALES .
  methods GET_PURCHTXT
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_PURCHTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_PURCHTXT
      !ES_PURCHTXT type /MDGMM/_S_MM_PP_PURCHTXT .
  methods GET_QINSPTXT
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_QINSPTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_QINSPTXT
      !ES_QINSPTXT type /MDGMM/_S_MM_PP_QINSPTXT .
  methods GET_QMATBASIC
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_QMATBASIC type ZIF_MDG_MM_DATATYPES=>GTY_T_QMATBASIC
      !ES_QMATBASIC type /MDGMM/_S_MM_PP_QMATBASIC .
  methods GET_SALESTXT
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_SALESTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_SALESTXT
      !ES_SALESTXT type /MDGMM/_S_MM_PP_SALESTXT .
  methods GET_UNITOFMSR
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_UNITOFMSR type ZIF_MDG_MM_DATATYPES=>GTY_T_UNITOFMSR
      !ES_UNITOFMSR type /MDGMM/_S_MM_PP_UNITOFMSR .
  methods GET_VALUATION
    importing
      !IT_KEY_VALUE type ZIF_MDG_DATATYPES=>GTY_T_KEY_VALUE optional
    exporting
      !ET_VALUATION type ZIF_MDG_MM_DATATYPES=>GTY_T_VALUATION
      !ES_VALUATION type /MDGMM/_S_MM_PP_VALUATION .
  methods SET_BSCDATTXT
    importing
      !IT_BSCDATTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_BSCDATTXT .
  methods SET_CLASSASGN
    importing
      !IT_CLASSASGN type ZIF_MDG_MM_DATATYPES=>GTY_T_CLASSASGN .
  methods SET_DRADBASIC
    importing
      !IT_DRADBASIC type ZIF_MDG_MM_DATATYPES=>GTY_T_DRADBASIC .
  methods SET_DRADTXT
    importing
      !IT_DRADTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_DRADTXT .
  methods SET_INTCMNT
    importing
      !IT_INTCMNT type ZIF_MDG_MM_DATATYPES=>GTY_T_INTCMNT .
  methods SET_MARAPURCH
    importing
      !IT_MARAPURCH type ZIF_MDG_MM_DATATYPES=>GTY_T_MARAPURCH .
  methods SET_MARAQTMNG
    importing
      !IT_MARAQTMNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MARAQTMNG .
  methods SET_MARASALES
    importing
      !IT_MARASALES type ZIF_MDG_MM_DATATYPES=>GTY_T_MARASALES .
  methods SET_MARASPM
    importing
      !IT_MARASPM type ZIF_MDG_MM_DATATYPES=>GTY_T_MARASPM .
  methods SET_MARASTOR
    importing
      !IT_MARASTOR type ZIF_MDG_MM_DATATYPES=>GTY_T_MARASTOR .
  methods SET_MARCATP
    importing
      !IT_MARCATP type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCATP .
  methods SET_MARCBASIC
    importing
      !IT_MARCBASIC type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCBASIC .
  methods SET_MARCCSTNG
    importing
      !IT_MARCCSTNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCCSTNG .
  methods SET_MARCFRCST
    importing
      !IT_MARCFRCST type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCFRCST .
  methods SET_MARCFRGTR
    importing
      !IT_MARCFRGTR type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCFRGTR .
  methods SET_MARCFRPAR
    importing
      !IT_MARCFRPAR type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCFRPAR .
  methods SET_MARCMRPFC
    importing
      !IT_MARCMRPFC type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCMRPFC .
  methods SET_MARCMRPLS
    importing
      !IT_MARCMRPLS type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCMRPLS .
  methods SET_MARCMRPMI
    importing
      !IT_MARCMRPMI type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCMRPMI .
  methods SET_MARCMRPPP
    importing
      !IT_MARCMRPPP type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCMRPPP .
  methods SET_MARCMRPSP
    importing
      !IT_MARCMRPSP type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCMRPSP .
  methods SET_MARCPRT
    importing
      !IT_MARCPRT type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCPRT .
  methods SET_MARCPURCH
    importing
      !IT_MARCPURCH type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCPURCH .
  methods SET_MARCQTMNG
    importing
      !IT_MARCQTMNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCQTMNG .
  methods SET_MARCSALES
    importing
      !IT_MARCSALES type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCSALES .
  methods SET_MARCSTORE
    importing
      !IT_MARCSTORE type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCSTORE .
  methods SET_MARCWRKSD
    importing
      !IT_MARCWRKSD type ZIF_MDG_MM_DATATYPES=>GTY_T_MARCWRKSD .
  methods SET_MARDMRP
    importing
      !IT_MARDMRP type ZIF_MDG_MM_DATATYPES=>GTY_T_MARDMRP .
  methods SET_MARDSTOR
    importing
      !IT_MARDSTOR type ZIF_MDG_MM_DATATYPES=>GTY_T_MARDSTOR .
  methods SET_MATCHGMNG
    importing
      !IT_MATCHGMNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MATCHGMNG .
  methods SET_MATERIAL
    importing
      !IT_MATERIAL type ZIF_MDG_MM_DATATYPES=>GTY_T_MATERIAL .
  methods SET_MATTXT
    importing
      !IT_MATTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_MATTXT .
  methods SET_MBEWACTNG
    importing
      !IT_MBEWACTNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MBEWACTNG .
  methods SET_MBEWCSTNG
    importing
      !IT_MBEWCSTNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MBEWCSTNG .
  methods SET_MBEWMLAC
    importing
      !IT_MBEWMLAC type ZIF_MDG_MM_DATATYPES=>GTY_T_MBEWMLAC .
  methods SET_MBEWMLVAL
    importing
      !IT_MBEWMLVAL type ZIF_MDG_MM_DATATYPES=>GTY_T_MBEWMLVAL .
  methods SET_MBEWVALUA
    importing
      !IT_MBEWVALUA type ZIF_MDG_MM_DATATYPES=>GTY_T_MBEWVALUA .
  methods SET_MDMABASIC
    importing
      !IT_MDMABASIC type ZIF_MDG_MM_DATATYPES=>GTY_T_MDMABASIC .
  methods SET_MEAN_GTIN
    importing
      !IT_MEAN_GTIN type ZIF_MDG_MM_DATATYPES=>GTY_T_MEAN_GTIN .
  methods SET_MKALBASIC
    importing
      !IT_MKALBASIC type ZIF_MDG_MM_DATATYPES=>GTY_T_MKALBASIC .
  methods SET_MLANPURCH
    importing
      !IT_MLANPURCH type ZIF_MDG_MM_DATATYPES=>GTY_T_MLANPURCH .
  methods SET_MLANSALES
    importing
      !IT_MLANSALES type ZIF_MDG_MM_DATATYPES=>GTY_T_MLANSALES .
  methods SET_MLGNSTOR
    importing
      !IT_MLGNSTOR type ZIF_MDG_MM_DATATYPES=>GTY_T_MLGNSTOR .
  methods SET_MLGTSTOR
    importing
      !IT_MLGTSTOR type ZIF_MDG_MM_DATATYPES=>GTY_T_MLGTSTOR .
  methods SET_MPGDPRODG
    importing
      !IT_MPGDPRODG type ZIF_MDG_MM_DATATYPES=>GTY_T_MPGDPRODG .
  methods SET_MRPTXT
    importing
      !IT_MRPTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_MRPTXT .
  methods SET_MVKEGRPNG
    importing
      !IT_MVKEGRPNG type ZIF_MDG_MM_DATATYPES=>GTY_T_MVKEGRPNG .
  methods SET_MVKESALES
    importing
      !IT_MVKESALES type ZIF_MDG_MM_DATATYPES=>GTY_T_MVKESALES .
  methods SET_PURCHTXT
    importing
      !IT_PURCHTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_PURCHTXT .
  methods SET_QINSPTXT
    importing
      !IT_QINSPTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_QINSPTXT .
  methods SET_QMATBASIC
    importing
      !IT_QMATBASIC type ZIF_MDG_MM_DATATYPES=>GTY_T_QMATBASIC .
  methods SET_SALESTXT
    importing
      !IT_SALESTXT type ZIF_MDG_MM_DATATYPES=>GTY_T_SALESTXT .
  methods SET_UNITOFMSR
    importing
      !IT_UNITOFMSR type ZIF_MDG_MM_DATATYPES=>GTY_T_UNITOFMSR .
  methods SET_VALUATION
    importing
      !IT_VALUATION type ZIF_MDG_MM_DATATYPES=>GTY_T_VALUATION .
  PROTECTED SECTION.

    DATA go_matchgmng_api TYPE REF TO cl_cmd_bs_mat_chgmng_api .
    DATA go_model TYPE REF TO if_usmd_model_ext .
    DATA gt_bscdattxt TYPE zif_mdg_mm_datatypes=>gty_t_bscdattxt .
    DATA gt_classasgn TYPE zif_mdg_mm_datatypes=>gty_t_classasgn .
    DATA gt_dradbasic TYPE zif_mdg_mm_datatypes=>gty_t_dradbasic .
    DATA gt_dradtxt TYPE zif_mdg_mm_datatypes=>gty_t_dradtxt .
    DATA gt_entity_attributes_rel TYPE zif_mdg_datatypes=>gty_t_entity_attributes_rel .
    DATA gt_intcmnt TYPE zif_mdg_mm_datatypes=>gty_t_intcmnt .
    DATA gt_marapurch TYPE zif_mdg_mm_datatypes=>gty_t_marapurch .
    DATA gt_maraqtmng TYPE zif_mdg_mm_datatypes=>gty_t_maraqtmng .
    DATA gt_marasales TYPE zif_mdg_mm_datatypes=>gty_t_marasales .
    DATA gt_maraspm TYPE zif_mdg_mm_datatypes=>gty_t_maraspm .
    DATA gt_marastor TYPE zif_mdg_mm_datatypes=>gty_t_marastor .
    DATA gt_marcatp TYPE zif_mdg_mm_datatypes=>gty_t_marcatp .
    DATA gt_marcbasic TYPE zif_mdg_mm_datatypes=>gty_t_marcbasic .
    DATA gt_marccstng TYPE zif_mdg_mm_datatypes=>gty_t_marccstng .
    DATA gt_marcfrcst TYPE zif_mdg_mm_datatypes=>gty_t_marcfrcst .
    DATA gt_marcfrgtr TYPE zif_mdg_mm_datatypes=>gty_t_marcfrgtr .
    DATA gt_marcfrpar TYPE zif_mdg_mm_datatypes=>gty_t_marcfrpar .
    DATA gt_marcmrpfc TYPE zif_mdg_mm_datatypes=>gty_t_marcmrpfc .
    DATA gt_marcmrpls TYPE zif_mdg_mm_datatypes=>gty_t_marcmrpls .
    DATA gt_marcmrpmi TYPE zif_mdg_mm_datatypes=>gty_t_marcmrpmi .
    DATA gt_marcmrppp TYPE zif_mdg_mm_datatypes=>gty_t_marcmrppp .
    DATA gt_marcmrpsp TYPE zif_mdg_mm_datatypes=>gty_t_marcmrpsp .
    DATA gt_marcprt TYPE zif_mdg_mm_datatypes=>gty_t_marcprt .
    DATA gt_marcpurch TYPE zif_mdg_mm_datatypes=>gty_t_marcpurch .
    DATA gt_marcqtmng TYPE zif_mdg_mm_datatypes=>gty_t_marcqtmng .
    DATA gt_marcsales TYPE zif_mdg_mm_datatypes=>gty_t_marcsales .
    DATA gt_marcstore TYPE zif_mdg_mm_datatypes=>gty_t_marcstore .
    DATA gt_marcwrksd TYPE zif_mdg_mm_datatypes=>gty_t_marcwrksd .
    DATA gt_mardmrp TYPE zif_mdg_mm_datatypes=>gty_t_mardmrp .
    DATA gt_mardstor TYPE zif_mdg_mm_datatypes=>gty_t_mardstor .
    DATA gt_matchgmng TYPE zif_mdg_mm_datatypes=>gty_t_matchgmng .
    DATA gt_material TYPE zif_mdg_mm_datatypes=>gty_t_material .
    DATA gt_mattxt TYPE zif_mdg_mm_datatypes=>gty_t_mattxt .
    DATA gt_mbewactng TYPE zif_mdg_mm_datatypes=>gty_t_mbewactng .
    DATA gt_mbewcstng TYPE zif_mdg_mm_datatypes=>gty_t_mbewcstng .
    DATA gt_mbewmlac TYPE zif_mdg_mm_datatypes=>gty_t_mbewmlac .
    DATA gt_mbewmlval TYPE zif_mdg_mm_datatypes=>gty_t_mbewmlval .
    DATA gt_mbewvalua TYPE zif_mdg_mm_datatypes=>gty_t_mbewvalua .
    DATA gt_mdmabasic TYPE zif_mdg_mm_datatypes=>gty_t_mdmabasic .
    DATA gt_mean_gtin TYPE zif_mdg_mm_datatypes=>gty_t_mean_gtin .
    DATA gt_mkalbasic TYPE zif_mdg_mm_datatypes=>gty_t_mkalbasic .
    DATA gt_mlanpurch TYPE zif_mdg_mm_datatypes=>gty_t_mlanpurch .
    DATA gt_mlansales TYPE zif_mdg_mm_datatypes=>gty_t_mlansales .
    DATA gt_mlgnstor TYPE zif_mdg_mm_datatypes=>gty_t_mlgnstor .
    DATA gt_mlgtstor TYPE zif_mdg_mm_datatypes=>gty_t_mlgtstor .
    DATA gt_mpgdprodg TYPE zif_mdg_mm_datatypes=>gty_t_mpgdprodg .
    DATA gt_mrptxt TYPE zif_mdg_mm_datatypes=>gty_t_mrptxt .
    DATA gt_mvkegrpng TYPE zif_mdg_mm_datatypes=>gty_t_mvkegrpng .
    DATA gt_mvkesales TYPE zif_mdg_mm_datatypes=>gty_t_mvkesales .
    DATA gt_purchtxt TYPE zif_mdg_mm_datatypes=>gty_t_purchtxt .
    DATA gt_qinsptxt TYPE zif_mdg_mm_datatypes=>gty_t_qinsptxt .
    DATA gt_qmatbasic TYPE zif_mdg_mm_datatypes=>gty_t_qmatbasic .
    DATA gt_salestxt TYPE zif_mdg_mm_datatypes=>gty_t_salestxt .
    DATA gt_unitofmsr TYPE zif_mdg_mm_datatypes=>gty_t_unitofmsr .
    DATA gt_valuation TYPE zif_mdg_mm_datatypes=>gty_t_valuation .
  PRIVATE SECTION.

    DATA gt_attribute_entity_rel TYPE zif_mdg_datatypes=>gty_t_attribute_entity_rel .
    DATA gt_dependent_entities TYPE zif_mdg_datatypes=>gty_t_dependent_entities .
    DATA gt_entity_keys TYPE usmd_ts_entity_cont .

    METHODS constructor .
    METHODS create_dependent_entities
      IMPORTING
        !iv_entity TYPE usmd_entity
        !is_record TYPE any .
    METHODS delete_dependent_entities
      IMPORTING
        !iv_entity TYPE usmd_entity
        !is_record TYPE any .
    METHODS get_all_entities
      RETURNING
        VALUE(rt_all_entities) TYPE usmd_t_entity .
    METHODS get_entity_reference
      IMPORTING
        !iv_entity TYPE usmd_entity
      EXPORTING
        !er_entity TYPE REF TO data .
    METHODS get_where_condition
      IMPORTING
        !it_key_value TYPE zif_mdg_datatypes=>gty_t_key_value
      EXPORTING
        !ev_where     TYPE string .
    METHODS init_dependent_entities .
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



CLASS ZCL_MDG_MM_HELPER IMPLEMENTATION.


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
      IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_mm TYPE 'X' NUMBER 000. ENDIF.
      ls_update_param-value = lr_update_tab.
      INSERT ls_update_param INTO TABLE lt_update_param.
      TRY.
          CALL METHOD me->(<ls_entity_info>-get_meth)
            PARAMETER-TABLE
            lt_update_param.
        CATCH cx_sy_dyn_call_error.
          MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_mm TYPE 'X' NUMBER 001 WITH <ls_entity_info>-get_meth.
      ENDTRY.

* Get Entity data from snapshot
      CLEAR: ls_snapshot_param , lt_snapshot_param .
      ls_snapshot_param-name = <ls_entity_info>-get_meth_exp_tab.
      ls_snapshot_param-kind = cl_abap_objectdescr=>importing.
      CREATE DATA lr_snapshot_tab TYPE (<ls_entity_info>-tab_type).
      ASSIGN lr_snapshot_tab->* TO <lt_compare_data>.
      IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_mm TYPE 'X' NUMBER 000. ENDIF.
      ls_snapshot_param-value = lr_snapshot_tab.
      INSERT ls_snapshot_param INTO TABLE lt_snapshot_param.
      TRY.
          CALL METHOD io_mat_data->(<ls_entity_info>-get_meth)
            PARAMETER-TABLE
            lt_snapshot_param.
        CATCH cx_sy_dyn_call_error.
          MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_mm TYPE 'X' NUMBER 001 WITH <ls_entity_info>-get_meth.
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
              IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_mm TYPE 'X' NUMBER 000. ENDIF.
              ASSIGN COMPONENT <ls_orig_data_comp>-name OF STRUCTURE <ls_compare_data> TO <lv_compare_value>.
              IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_mm TYPE 'X' NUMBER 000. ENDIF.
              IF <lv_orig_value> <> <lv_compare_value>.
* Difference found => add updated entry
                IF ls_changed_entity IS INITIAL.
                  ls_changed_entity = zcl_mdg_data_utilities=>create_entity_data( iv_entity   = <ls_entity_info>-entity
                                                                                       iv_tab_type = <ls_entity_info>-tab_type ).
                  ASSIGN ls_changed_entity-entity_data->* TO <lt_chg_data>.
                  IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_mm TYPE 'X' NUMBER 000. ENDIF.
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
              IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_mm TYPE 'X' NUMBER 000. ENDIF.
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
              IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_mm TYPE 'X' NUMBER 000. ENDIF.

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
              IF sy-subrc <> 0. MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_mm TYPE 'X' NUMBER 000. ENDIF.
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


  METHOD constructor.

    init_model( ).
    init_entity_keys( ).
    init_entity_attribute_rel( ).
    init_dependent_entities( ).

  ENDMETHOD.


  METHOD copy_instance.
    DATA:
        lo_mat_class_descr TYPE REF TO cl_abap_objectdescr.

    FIELD-SYMBOLS:
      <ls_attribute> TYPE abap_attrdescr,
      <lv_target>    TYPE any,
      <lv_source>    TYPE any.

* Initialize object and transfer attributes
    CREATE OBJECT ro_mat_data.
    lo_mat_class_descr ?= cl_abap_objectdescr=>describe_by_object_ref( ro_mat_data ).

* Transfer attributes to new instance
    LOOP AT lo_mat_class_descr->attributes ASSIGNING <ls_attribute> WHERE is_constant = abap_false. "#EC CI_STDSEQ
      ASSIGN ro_mat_data->(<ls_attribute>-name) TO <lv_target>.
      IF sy-subrc <> 0.
        CLEAR ro_mat_data.
        MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_mm TYPE 'X' NUMBER 004 WITH <ls_attribute>-name INTO zcl_mdg_general_functions=>gv_error_message .
        sy-msgid = zcl_mdg_general_functions=>gc_msg_class_dm_mm.
        sy-msgno = '004'.
        sy-msgty = usmd1_cs_msgty-error.
        sy-msgv1 = <ls_attribute>-name.
        MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_mm TYPE 'X' NUMBER 011 RAISING  attribute_assignment_error.
      ENDIF.
      ASSIGN me->(<ls_attribute>-name) TO <lv_source>.
      IF sy-subrc <> 0.
        CLEAR ro_mat_data.
        MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_mm TYPE 'X' NUMBER 004 WITH <ls_attribute>-name INTO zcl_mdg_general_functions=>gv_error_message.
        sy-msgid = zcl_mdg_general_functions=>gc_msg_class_dm_mm.
        sy-msgno = '004'.
        sy-msgty = usmd1_cs_msgty-error.
        sy-msgv1 = <ls_attribute>-name.
        MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_mm TYPE 'X' NUMBER 011 RAISING attribute_assignment_error.
      ENDIF.
      <lv_target> = <lv_source>.
      IF sy-subrc <> 0.
        CLEAR ro_mat_data.
        MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_mm TYPE 'X' NUMBER 004 WITH <ls_attribute>-name INTO zcl_mdg_general_functions=>gv_error_message.
        sy-msgid = zcl_mdg_general_functions=>gc_msg_class_dm_mm.
        sy-msgno = '004'.
        sy-msgty = usmd1_cs_msgty-error.
        sy-msgv1 = <ls_attribute>-name.
        MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_mm TYPE 'X' NUMBER 011 RAISING attribute_assignment_error.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD create_dependent_entities.

    DATA:
      lt_key_value             TYPE zif_mdg_datatypes=>gty_t_key_value,
      lr_dependent_entity_data TYPE REF TO data,
      lr_new_record            TYPE REF TO data,
      lt_entity_keys           TYPE usmd_t_entity,
      lv_where                 TYPE string,
      lv_found                 TYPE abap_bool VALUE abap_false.

    FIELD-SYMBOLS:
      <ls_dependent_entities>    TYPE zif_mdg_datatypes=>gty_s_dependent_entities,
      <lv_dependent_entity>      TYPE usmd_entity,
      <lt_dependent_entity_data> TYPE ANY TABLE,
      <ls_new_record>            TYPE any,
      <lv_source>                TYPE any,
      <lv_target>                TYPE any,
      <lv_key>                   TYPE usmd_entity,
      <ls_data>                  TYPE any.

    READ TABLE gt_dependent_entities WITH TABLE KEY entity = iv_entity ASSIGNING <ls_dependent_entities> .

    IF sy-subrc = 0.
      CALL METHOD get_key_value_table
        EXPORTING
          iv_entity    = iv_entity
          is_record    = is_record
        IMPORTING
          et_key_value = lt_key_value.

      LOOP AT <ls_dependent_entities>-dependent_entities ASSIGNING <lv_dependent_entity>.
        UNASSIGN: <lt_dependent_entity_data>, <ls_new_record>.
        CLEAR: lt_entity_keys.

        CALL METHOD get_entity_reference
          EXPORTING
            iv_entity = <lv_dependent_entity>
          IMPORTING
            er_entity = lr_dependent_entity_data.

        ASSIGN lr_dependent_entity_data->* TO <lt_dependent_entity_data>.

        IF sy-subrc = 0.
          CALL METHOD get_where_condition
            EXPORTING
              it_key_value = lt_key_value
            IMPORTING
              ev_where     = lv_where.

          CLEAR lv_found.
          LOOP AT <lt_dependent_entity_data> ASSIGNING <ls_data> WHERE (lv_where). "#EC CI_NESTED
            lv_found = abap_true.
            EXIT.
          ENDLOOP.

          IF lv_found = abap_false.

            CREATE DATA lr_new_record LIKE LINE OF <lt_dependent_entity_data>.
            ASSIGN lr_new_record->* TO <ls_new_record>.

            CALL METHOD get_keys_of_entity
              EXPORTING
                iv_entity      = <lv_dependent_entity>
              IMPORTING
                et_entity_keys = lt_entity_keys.

            LOOP AT lt_entity_keys ASSIGNING <lv_key>. "#EC CI_NESTED
              ASSIGN COMPONENT <lv_key> OF STRUCTURE is_record TO <lv_source>.
              ASSIGN COMPONENT <lv_key> OF STRUCTURE <ls_new_record> TO <lv_target>.
              <lv_target> = <lv_source>.
            ENDLOOP.

            INSERT <ls_new_record> INTO TABLE <lt_dependent_entity_data>.

          ENDIF.
        ELSE.
          MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 000. "#EC CI_USE_WANTED
        ENDIF.

      ENDLOOP.
    ENDIF.

  ENDMETHOD.


  METHOD delete_dependent_entities.

    DATA:
      lt_key_value             TYPE zif_mdg_datatypes=>gty_t_key_value,
      lr_dependent_entity_data TYPE REF TO data,
      lv_where                 TYPE string.

    FIELD-SYMBOLS:
      <ls_dependent_entities>    TYPE zif_mdg_datatypes=>gty_s_dependent_entities,
      <lv_dependent_entity>      TYPE usmd_entity,
      <lt_dependent_entity_data> TYPE ANY TABLE.


    READ TABLE gt_dependent_entities WITH TABLE KEY entity = iv_entity ASSIGNING <ls_dependent_entities> .

    IF sy-subrc = 0.
      CALL METHOD get_key_value_table
        EXPORTING
          iv_entity    = iv_entity
          is_record    = is_record
        IMPORTING
          et_key_value = lt_key_value.

      LOOP AT <ls_dependent_entities>-dependent_entities ASSIGNING <lv_dependent_entity>.
        UNASSIGN: <lt_dependent_entity_data>.

        CALL METHOD get_entity_reference
          EXPORTING
            iv_entity = <lv_dependent_entity>
          IMPORTING
            er_entity = lr_dependent_entity_data.

        ASSIGN lr_dependent_entity_data->* TO <lt_dependent_entity_data>.

        IF sy-subrc = 0.
          CALL METHOD get_where_condition
            EXPORTING
              it_key_value = lt_key_value
            IMPORTING
              ev_where     = lv_where.

          DELETE <lt_dependent_entity_data> WHERE (lv_where).
        ELSE.
          MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 000.
        ENDIF.
      ENDLOOP.
    ENDIF.

  ENDMETHOD.


  METHOD del_bscdattxt.

    FIELD-SYMBOLS:
      <ls_bscdattxt> TYPE /mdgmm/_s_mm_pp_bscdattxt.

    LOOP AT it_bscdattxt ASSIGNING <ls_bscdattxt>.
      DELETE TABLE gt_bscdattxt FROM <ls_bscdattxt>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c~gc_entity_bscdattxt
          is_record = <ls_bscdattxt>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_classasgn.

    FIELD-SYMBOLS:
      <ls_classasgn> TYPE /mdgmm/_s_mm_pp_classasgn.

    LOOP AT it_classasgn ASSIGNING <ls_classasgn>.
      DELETE TABLE gt_classasgn FROM <ls_classasgn>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c~gc_entity_classasgn
          is_record = <ls_classasgn>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_dradbasic.

    FIELD-SYMBOLS:
      <ls_dradbasic> TYPE /mdgmm/_s_mm_pp_dradbasic.

    LOOP AT it_dradbasic ASSIGNING <ls_dradbasic>.
      DELETE TABLE gt_dradbasic FROM <ls_dradbasic>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = zcl_mdg_mm_helper=>cs_entities-dradbasic
          is_record = <ls_dradbasic>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_dradtxt.

    FIELD-SYMBOLS:
      <ls_dradtxt> TYPE /mdgmm/_s_mm_pp_dradtxt.

    LOOP AT it_dradtxt ASSIGNING <ls_dradtxt>.
      DELETE TABLE gt_dradtxt FROM <ls_dradtxt>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = zcl_mdg_mm_helper=>cs_entities-dradtxt
          is_record = <ls_dradtxt>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_intcmnt.

    FIELD-SYMBOLS:
      <ls_intcmnt> TYPE /mdgmm/_s_mm_pp_intcmnt.

    LOOP AT it_intcmnt ASSIGNING <ls_intcmnt>.
      DELETE TABLE gt_intcmnt FROM <ls_intcmnt>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_intcmnt
          is_record = <ls_intcmnt>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marapurch.

    FIELD-SYMBOLS:
      <ls_marapurch> TYPE /mdgmm/_s_mm_pp_marapurch.

    LOOP AT it_marapurch ASSIGNING <ls_marapurch>.
      DELETE TABLE gt_marapurch FROM <ls_marapurch>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_marapurch
          is_record = <ls_marapurch>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_maraqtmng.

    FIELD-SYMBOLS:
      <ls_maraqtmng> TYPE /mdgmm/_s_mm_pp_maraqtmng.

    LOOP AT it_maraqtmng ASSIGNING <ls_maraqtmng>.
      DELETE TABLE gt_maraqtmng FROM <ls_maraqtmng>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = zcl_mdg_mm_helper=>cs_entities-maraqtmng
          is_record = <ls_maraqtmng>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marasales.

    FIELD-SYMBOLS:
      <ls_marasales> TYPE /mdgmm/_s_mm_pp_marasales.

    LOOP AT it_marasales ASSIGNING <ls_marasales>.
      DELETE TABLE gt_marasales FROM <ls_marasales>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_marasales
          is_record = <ls_marasales>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_maraspm.

    FIELD-SYMBOLS:
      <ls_maraspm> TYPE /mdgmm/_s_mm_pp_maraspm.

    LOOP AT it_maraspm ASSIGNING <ls_maraspm>.
      DELETE TABLE gt_maraspm FROM <ls_maraspm>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = zcl_mdg_mm_helper=>cs_entities-maraspm
          is_record = <ls_maraspm>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marastor.

    FIELD-SYMBOLS:
      <ls_marastor> TYPE /mdgmm/_s_mm_pp_marastor.

    LOOP AT it_marastor ASSIGNING <ls_marastor>.
      DELETE TABLE gt_marastor FROM <ls_marastor>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = zcl_mdg_mm_helper=>cs_entities-marastor
          is_record = <ls_marastor>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marcatp.

    FIELD-SYMBOLS:
      <ls_marcatp> TYPE /mdgmm/_s_mm_pp_marcatp.

    LOOP AT it_marcatp ASSIGNING <ls_marcatp>.
      DELETE TABLE gt_marcatp FROM <ls_marcatp>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_marcatp
          is_record = <ls_marcatp>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marcbasic.

    FIELD-SYMBOLS:
      <ls_marcbasic> TYPE /mdgmm/_s_mm_pp_marcbasic.

    LOOP AT it_marcbasic ASSIGNING <ls_marcbasic>.
      DELETE TABLE gt_marcbasic FROM <ls_marcbasic>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_marcbasic
          is_record = <ls_marcbasic>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marccstng.

    FIELD-SYMBOLS:
      <ls_marccstng> TYPE /mdgmm/_s_mm_pp_marccstng.

    LOOP AT it_marccstng ASSIGNING <ls_marccstng>.
      DELETE TABLE gt_marccstng FROM <ls_marccstng>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_marccstng
          is_record = <ls_marccstng>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marcfrcst.

    FIELD-SYMBOLS:
      <ls_marcfrcst> TYPE /mdgmm/_s_mm_pp_marcfrcst.

    LOOP AT it_marcfrcst ASSIGNING <ls_marcfrcst>.
      DELETE TABLE gt_marcfrcst FROM <ls_marcfrcst>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_marcfrcst
          is_record = <ls_marcfrcst>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marcfrgtr.

    FIELD-SYMBOLS:
      <ls_marcfrgtr> TYPE /mdgmm/_s_mm_pp_marcfrgtr.

    LOOP AT it_marcfrgtr ASSIGNING <ls_marcfrgtr>.
      DELETE TABLE gt_marcfrgtr FROM <ls_marcfrgtr>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_marcfrgtr
          is_record = <ls_marcfrgtr>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marcfrpar.

    FIELD-SYMBOLS:
      <ls_marcfrpar> TYPE /mdgmm/_s_mm_pp_marcfrpar.

    LOOP AT it_marcfrpar ASSIGNING <ls_marcfrpar>.
      DELETE TABLE gt_marcfrpar FROM <ls_marcfrpar>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_marcfrpar
          is_record = <ls_marcfrpar>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marcmrpfc.

    FIELD-SYMBOLS:
      <ls_marcmrpfc> TYPE /mdgmm/_s_mm_pp_marcmrpfc.

    LOOP AT it_marcmrpfc ASSIGNING <ls_marcmrpfc>.
      DELETE TABLE gt_marcmrpfc FROM <ls_marcmrpfc>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_marcmrpfc
          is_record = <ls_marcmrpfc>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marcmrpls.

    FIELD-SYMBOLS:
      <ls_marcmrpls> TYPE /mdgmm/_s_mm_pp_marcmrpls.

    LOOP AT it_marcmrpls ASSIGNING <ls_marcmrpls>.
      DELETE TABLE gt_marcmrpls FROM <ls_marcmrpls>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_marcmrpls
          is_record = <ls_marcmrpls>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marcmrpmi.

    FIELD-SYMBOLS:
      <ls_marcmrpmi> TYPE /mdgmm/_s_mm_pp_marcmrpmi.

    LOOP AT it_marcmrpmi ASSIGNING <ls_marcmrpmi>.
      DELETE TABLE gt_marcmrpmi FROM <ls_marcmrpmi>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_marcmrpmi
          is_record = <ls_marcmrpmi>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marcmrppp.

    FIELD-SYMBOLS:
      <ls_marcmrppp> TYPE /mdgmm/_s_mm_pp_marcmrppp.

    LOOP AT it_marcmrppp ASSIGNING <ls_marcmrppp>.
      DELETE TABLE gt_marcmrppp FROM <ls_marcmrppp>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_marcmrppp
          is_record = <ls_marcmrppp>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marcmrpsp.

    FIELD-SYMBOLS:
      <ls_marcmrpsp> TYPE /mdgmm/_s_mm_pp_marcmrpsp.

    LOOP AT it_marcmrpsp ASSIGNING <ls_marcmrpsp>.
      DELETE TABLE gt_marcmrpsp FROM <ls_marcmrpsp>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_marcmrpsp
          is_record = <ls_marcmrpsp>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marcprt.

    FIELD-SYMBOLS:
      <ls_marcprt> TYPE /mdgmm/_s_mm_pp_marcprt.

    LOOP AT it_marcprt ASSIGNING <ls_marcprt>.
      DELETE TABLE gt_marcprt FROM <ls_marcprt>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_marcprt
          is_record = <ls_marcprt>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marcpurch.

    FIELD-SYMBOLS:
      <ls_marcpurch> TYPE /mdgmm/_s_mm_pp_marcpurch.

    LOOP AT it_marcpurch ASSIGNING <ls_marcpurch>.
      DELETE TABLE gt_marcpurch FROM <ls_marcpurch>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = zcl_mdg_mm_helper=>cs_entities-marcpurch
          is_record = <ls_marcpurch>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marcqtmng.

    FIELD-SYMBOLS:
      <ls_marcqtmng> TYPE /mdgmm/_s_mm_pp_marcqtmng.

    LOOP AT it_marcqtmng ASSIGNING <ls_marcqtmng>.
      DELETE TABLE gt_marcqtmng FROM <ls_marcqtmng>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_marcqtmng
          is_record = <ls_marcqtmng>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marcsales.

    FIELD-SYMBOLS:
      <ls_marcsales> TYPE /mdgmm/_s_mm_pp_marcsales.

    LOOP AT it_marcsales ASSIGNING <ls_marcsales>.
      DELETE TABLE gt_marcsales FROM <ls_marcsales>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_marcsales
          is_record = <ls_marcsales>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marcstore.

    FIELD-SYMBOLS:
      <ls_marcstore> TYPE /mdgmm/_s_mm_pp_marcstore.

    LOOP AT it_marcstore ASSIGNING <ls_marcstore>.
      DELETE TABLE gt_marcstore FROM <ls_marcstore>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = zcl_mdg_mm_helper=>cs_entities-marcstore
          is_record = <ls_marcstore>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_marcwrksd.

    FIELD-SYMBOLS:
      <ls_marcwrksd> TYPE /mdgmm/_s_mm_pp_marcwrksd.

    LOOP AT it_marcwrksd ASSIGNING <ls_marcwrksd>.
      DELETE TABLE gt_marcwrksd FROM <ls_marcwrksd>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_marcwrksd
          is_record = <ls_marcwrksd>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mardmrp.

    FIELD-SYMBOLS:
      <ls_mardmrp> TYPE /mdgmm/_s_mm_pp_mardmrp.

    LOOP AT it_mardmrp ASSIGNING <ls_mardmrp>.
      DELETE TABLE gt_mardmrp FROM <ls_mardmrp>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_mardmrp
          is_record = <ls_mardmrp>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mardstor.

    FIELD-SYMBOLS:
      <ls_mardstor> TYPE /mdgmm/_s_mm_pp_mardstor.

    LOOP AT it_mardstor ASSIGNING <ls_mardstor>.
      DELETE TABLE gt_mardstor FROM <ls_mardstor>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_mardstor
          is_record = <ls_mardstor>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_matchgmng.

    FIELD-SYMBOLS:
      <ls_matchgmng> TYPE /mdgmm/_s_mm_pp_matchgmng.

    LOOP AT it_matchgmng ASSIGNING <ls_matchgmng>.
      DELETE TABLE gt_matchgmng FROM <ls_matchgmng>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = zcl_mdg_mm_helper=>cs_entities-matchgmng
          is_record = <ls_matchgmng>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_material.

    FIELD-SYMBOLS:
      <ls_material> TYPE /mdgmm/_s_mm_pp_material.

    LOOP AT it_material ASSIGNING <ls_material>.
      DELETE TABLE gt_material FROM <ls_material>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_material
          is_record = <ls_material>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mattxt.

    FIELD-SYMBOLS:
      <ls_mattxt> TYPE /mdgmm/_st_mm_pp_material.

    LOOP AT it_mattxt ASSIGNING <ls_mattxt>.
      DELETE TABLE gt_mattxt FROM <ls_mattxt>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = zcl_mdg_mm_helper=>cs_entities-material_txt
          is_record = <ls_mattxt>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mbewactng.

    FIELD-SYMBOLS:
      <ls_mbewactng> TYPE /mdgmm/_s_mm_pp_mbewactng.

    LOOP AT it_mbewactng ASSIGNING <ls_mbewactng>.
      DELETE TABLE gt_mbewactng FROM <ls_mbewactng>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_mbewactng
          is_record = <ls_mbewactng>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mbewcstng.

    FIELD-SYMBOLS:
      <ls_mbewcstng> TYPE /mdgmm/_s_mm_pp_mbewcstng.

    LOOP AT it_mbewcstng ASSIGNING <ls_mbewcstng>.
      DELETE TABLE gt_mbewcstng FROM <ls_mbewcstng>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_mbewcstng
          is_record = <ls_mbewcstng>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mbewmlac.

    FIELD-SYMBOLS:
      <ls_mbewmlac> TYPE /mdgmm/_s_mm_pp_mbewmlac.

    LOOP AT it_mbewmlac ASSIGNING <ls_mbewmlac>.
      DELETE TABLE gt_mbewmlac FROM <ls_mbewmlac>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_mbewmlac
          is_record = <ls_mbewmlac>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mbewmlval.

    FIELD-SYMBOLS:
      <ls_mbewmlval> TYPE /mdgmm/_s_mm_pp_mbewmlval.

    LOOP AT it_mbewmlval ASSIGNING <ls_mbewmlval>.
      DELETE TABLE gt_mbewmlval FROM <ls_mbewmlval>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_mbewmlval
          is_record = <ls_mbewmlval>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mbewvalua.

    FIELD-SYMBOLS:
      <ls_mbewvalua> TYPE /mdgmm/_s_mm_pp_mbewvalua.

    LOOP AT it_mbewvalua ASSIGNING <ls_mbewvalua>.
      DELETE TABLE gt_mbewvalua FROM <ls_mbewvalua>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_mbewvalua
          is_record = <ls_mbewvalua>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mdmabasic.

    FIELD-SYMBOLS:
      <ls_mdmabasic> TYPE /mdgmm/_s_mm_pp_mdmabasic.

    LOOP AT it_mdmabasic ASSIGNING <ls_mdmabasic>.
      DELETE TABLE gt_mdmabasic FROM <ls_mdmabasic>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_mdmabasic
          is_record = <ls_mdmabasic>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mean_gtin.

    FIELD-SYMBOLS:
      <ls_mean_gtin> TYPE /mdgmm/_s_mm_pp_mean_gtin.

    LOOP AT it_mean_gtin ASSIGNING <ls_mean_gtin>.
      DELETE TABLE gt_mean_gtin FROM <ls_mean_gtin>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_mean_gtin
          is_record = <ls_mean_gtin>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mkalbasic.

    FIELD-SYMBOLS:
      <ls_mkalbasic> TYPE /mdgmm/_s_mm_pp_mkalbasic.

    LOOP AT it_mkalbasic ASSIGNING <ls_mkalbasic>.
      DELETE TABLE gt_mkalbasic FROM <ls_mkalbasic>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_mkalbasic
          is_record = <ls_mkalbasic>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mlanpurch.

    FIELD-SYMBOLS:
      <ls_mlanpurch> TYPE /mdgmm/_s_mm_pp_mlanpurch.

    LOOP AT it_mlanpurch ASSIGNING <ls_mlanpurch>.
      DELETE TABLE gt_mlanpurch FROM <ls_mlanpurch>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_mlanpurch
          is_record = <ls_mlanpurch>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mlansales.

    FIELD-SYMBOLS:
      <ls_mlansales> TYPE /mdgmm/_s_mm_pp_mlansales.

    LOOP AT it_mlansales ASSIGNING <ls_mlansales>.
      DELETE TABLE gt_mlansales FROM <ls_mlansales>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_mlansales
          is_record = <ls_mlansales>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mlgnstor.

    FIELD-SYMBOLS:
      <ls_mlgnstor> TYPE /mdgmm/_s_mm_pp_mlgnstor.

    LOOP AT it_mlgnstor ASSIGNING <ls_mlgnstor>.
      DELETE TABLE gt_mlgnstor FROM <ls_mlgnstor>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_mlgnstor
          is_record = <ls_mlgnstor>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mlgtstor.

    FIELD-SYMBOLS:
      <ls_mlgtstor> TYPE /mdgmm/_s_mm_pp_mlgtstor.

    LOOP AT it_mlgtstor ASSIGNING <ls_mlgtstor>.
      DELETE TABLE gt_mlgtstor FROM <ls_mlgtstor>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_mlgtstor
          is_record = <ls_mlgtstor>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mpgdprodg.

    FIELD-SYMBOLS:
      <ls_mpgdprodg> TYPE /mdgmm/_s_mm_pp_mpgdprodg.

    LOOP AT it_mpgdprodg ASSIGNING <ls_mpgdprodg>.
      DELETE TABLE gt_mpgdprodg FROM <ls_mpgdprodg>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_mpgdprodg
          is_record = <ls_mpgdprodg>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mrptxt.

    FIELD-SYMBOLS:
      <ls_mrptxt> TYPE /mdgmm/_s_mm_pp_mrptxt.

    LOOP AT it_mrptxt ASSIGNING <ls_mrptxt>.
      DELETE TABLE gt_mrptxt FROM <ls_mrptxt>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_mrptxt
          is_record = <ls_mrptxt>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mvkegrpng.

    FIELD-SYMBOLS:
      <ls_mvkegrpng> TYPE /mdgmm/_s_mm_pp_mvkegrpng.

    LOOP AT it_mvkegrpng ASSIGNING <ls_mvkegrpng>.
      DELETE TABLE gt_mvkegrpng FROM <ls_mvkegrpng>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_mvkegrpng
          is_record = <ls_mvkegrpng>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_mvkesales.

    FIELD-SYMBOLS:
      <ls_mvkesales> TYPE /mdgmm/_s_mm_pp_mvkesales.

    LOOP AT it_mvkesales ASSIGNING <ls_mvkesales>.
      DELETE TABLE gt_mvkesales FROM <ls_mvkesales>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_mvkesales
          is_record = <ls_mvkesales>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_purchtxt.

    FIELD-SYMBOLS:
      <ls_purchtxt> TYPE /mdgmm/_s_mm_pp_purchtxt.

    LOOP AT it_purchtxt ASSIGNING <ls_purchtxt>.
      DELETE TABLE gt_purchtxt FROM <ls_purchtxt>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_purchtxt
          is_record = <ls_purchtxt>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_qinsptxt.

    FIELD-SYMBOLS:
      <ls_qinsptxt> TYPE /mdgmm/_s_mm_pp_qinsptxt.

    LOOP AT it_qinsptxt ASSIGNING <ls_qinsptxt>.
      DELETE TABLE gt_qinsptxt FROM <ls_qinsptxt>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_qinsptxt
          is_record = <ls_qinsptxt>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_qmatbasic.

    FIELD-SYMBOLS:
      <ls_qmatbasic> TYPE /mdgmm/_s_mm_pp_qmatbasic.

    LOOP AT it_qmatbasic ASSIGNING <ls_qmatbasic>.
      DELETE TABLE gt_qmatbasic FROM <ls_qmatbasic>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_qmatbasic
          is_record = <ls_qmatbasic>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_salestxt.

    FIELD-SYMBOLS:
      <ls_salestxt> TYPE /mdgmm/_s_mm_pp_salestxt.

    LOOP AT it_salestxt ASSIGNING <ls_salestxt>.
      DELETE TABLE gt_salestxt FROM <ls_salestxt>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_salestxt
          is_record = <ls_salestxt>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_unitofmsr.

    FIELD-SYMBOLS:
      <ls_unitofmsr> TYPE /mdgmm/_s_mm_pp_unitofmsr.

    LOOP AT it_unitofmsr ASSIGNING <ls_unitofmsr>.
      DELETE TABLE gt_unitofmsr FROM <ls_unitofmsr>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_unitofmsr
          is_record = <ls_unitofmsr>.
    ENDLOOP.

  ENDMETHOD.


  METHOD del_valuation.

    FIELD-SYMBOLS:
      <ls_valuation> TYPE /mdgmm/_s_mm_pp_valuation.

    LOOP AT it_valuation ASSIGNING <ls_valuation>.
      DELETE TABLE gt_valuation FROM <ls_valuation>.

      CALL METHOD delete_dependent_entities
        EXPORTING
          iv_entity = if_mdg_bs_mat_gen_c=>gc_entity_valuation
          is_record = <ls_valuation>.
    ENDLOOP.

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

* add material texts
    APPEND cs_entities-material_txt TO lt_all_entities.

    SORT lt_all_entities.

    rt_all_entities = lt_all_entities.

  ENDMETHOD.


  METHOD get_attribute_entity.

    DATA:
          ls_attribute_entity TYPE zif_mdg_datatypes=>gty_s_attribute_entity_rel.

    CLEAR ev_entity.

    READ TABLE gt_attribute_entity_rel INTO ls_attribute_entity WITH TABLE KEY attribute = iv_attribute.

    IF sy-subrc <> 0.
      RAISE attribute_not_found.
    ENDIF.

    ev_entity = ls_attribute_entity-entity.

  ENDMETHOD.


  METHOD get_attribute_entity_list.

    et_attribute_entity_rel = gt_attribute_entity_rel.

  ENDMETHOD.


  METHOD get_bscdattxt.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_bscdattxt, es_bscdattxt.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_bscdattxt
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_bscdattxt ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_bscdattxt.
      ENDLOOP.
    ELSE .
      et_bscdattxt = gt_bscdattxt.
    ENDIF.

    IF lines( et_bscdattxt ) = 1.
      READ TABLE et_bscdattxt INTO es_bscdattxt INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_classasgn.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_classasgn, es_classasgn.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_classasgn
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_classasgn ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_classasgn.
      ENDLOOP.
    ELSE .
      et_classasgn = gt_classasgn.
    ENDIF.

    IF lines( et_classasgn ) = 1.
      READ TABLE et_classasgn INTO es_classasgn INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_dradbasic.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_dradbasic, es_dradbasic.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>cs_entities-dradbasic
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_dradbasic ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_dradbasic.
      ENDLOOP.
    ELSE .
      et_dradbasic = gt_dradbasic.
    ENDIF.

    IF lines( et_dradbasic ) = 1.
      READ TABLE et_dradbasic INTO es_dradbasic INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_dradtxt.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_dradtxt, es_dradtxt.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>cs_entities-dradtxt
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_dradtxt ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_dradtxt.
      ENDLOOP.
    ELSE .
      et_dradtxt = gt_dradtxt.
    ENDIF.

    IF lines( et_dradtxt ) = 1.
      READ TABLE et_dradtxt INTO es_dradtxt INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_entity_attributes.

    DATA:
          ls_entity_attributes TYPE zif_mdg_datatypes=>gty_s_entity_attributes_rel.

    READ TABLE gt_entity_attributes_rel INTO ls_entity_attributes WITH TABLE KEY entity = iv_entity.

    CLEAR: et_entity_attributes.

    IF sy-subrc <> 0.
      RAISE entity_not_found.
    ENDIF.

    et_entity_attributes = ls_entity_attributes-attributes.

  ENDMETHOD.


  METHOD get_entity_attributes_list.

    et_entity_attributes = gt_entity_attributes_rel.

  ENDMETHOD.


  METHOD get_entity_info.

    DATA:
      ls_entity_info TYPE zif_mdg_datatypes=>gty_s_entity_info.

    CLEAR: rs_entity_info.

    READ TABLE get_entity_info_list( ) INTO ls_entity_info WITH TABLE KEY entity = iv_entity.

    IF sy-subrc <> 0.
      MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 004 RAISING entity_not_found.
    ENDIF.

    rs_entity_info = ls_entity_info.

  ENDMETHOD.


  METHOD get_entity_info_list.

    DATA:
      ls_entity_info  TYPE zif_mdg_datatypes=>gty_s_entity_info.

    CLEAR rt_entity_info.

* Writes the information from method BSCDATTXT GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_bscdattxt.
    ls_entity_info-get_meth         = 'GET_BSCDATTXT'.
    ls_entity_info-set_meth         = 'SET_BSCDATTXT'.
    ls_entity_info-del_meth         = 'DEL_BSCDATTXT'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_BSCDATTXT'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_BSCDATTXT'.
    ls_entity_info-get_meth_exp_tab = 'ET_BSCDATTXT'.
    ls_entity_info-del_meth_imp_tab = 'IT_BSCDATTXT'.
    ls_entity_info-set_meth_imp_tab = 'IT_BSCDATTXT'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method CLASSASGN GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_classasgn.
    ls_entity_info-get_meth         = 'GET_CLASSASGN'.
    ls_entity_info-set_meth         = 'SET_CLASSASGN'.
    ls_entity_info-del_meth         = 'DEL_CLASSASGN'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_CLASSASGN'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_CLASSASGN'.
    ls_entity_info-get_meth_exp_tab = 'ET_CLASSASGN'.
    ls_entity_info-del_meth_imp_tab = 'IT_CLASSASGN'.
    ls_entity_info-set_meth_imp_tab = 'IT_CLASSASGN'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method DRADBASIC GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>cs_entities-dradbasic.
    ls_entity_info-get_meth         = 'GET_DRADBASIC'.
    ls_entity_info-set_meth         = 'SET_DRADBASIC'.
    ls_entity_info-del_meth         = 'DEL_DRADBASIC'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_DRADBASIC'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_DRADBASIC'.
    ls_entity_info-get_meth_exp_tab = 'ET_DRADBASIC'.
    ls_entity_info-del_meth_imp_tab = 'IT_DRADBASIC'.
    ls_entity_info-set_meth_imp_tab = 'IT_DRADBASIC'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method DRADTXT GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>cs_entities-dradtxt.
    ls_entity_info-get_meth         = 'GET_DRADTXT'.
    ls_entity_info-set_meth         = 'SET_DRADTXT'.
    ls_entity_info-del_meth         = 'DEL_DRADTXT'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_DRADTXT'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_dradtxt'.
    ls_entity_info-get_meth_exp_tab = 'ET_DRADTXT'.
    ls_entity_info-del_meth_imp_tab = 'IT_DRADTXT'.
    ls_entity_info-set_meth_imp_tab = 'IT_DRADTXT'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method INTCMNT GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_intcmnt.
    ls_entity_info-get_meth         = 'GET_INTCMNT'.
    ls_entity_info-set_meth         = 'SET_INTCMNT'.
    ls_entity_info-del_meth         = 'DEL_INTCMNT'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_INTCMNT'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_INTCMNT'.
    ls_entity_info-get_meth_exp_tab = 'ET_INTCMNT'.
    ls_entity_info-del_meth_imp_tab = 'IT_INTCMNT'.
    ls_entity_info-set_meth_imp_tab = 'IT_INTCMNT'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARAPURCH GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marapurch.
    ls_entity_info-get_meth         = 'GET_MARAPURCH'.
    ls_entity_info-set_meth         = 'SET_MARAPURCH'.
    ls_entity_info-del_meth         = 'DEL_MARAPURCH'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARAPURCH'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARAPURCH'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARAPURCH'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARAPURCH'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARAPURCH'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARAQTMNG GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>cs_entities-maraqtmng.
    ls_entity_info-get_meth         = 'GET_MARAQTMNG'.
    ls_entity_info-set_meth         = 'SET_MARAQTMNG'.
    ls_entity_info-del_meth         = 'DEL_MARAQTMNG'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARAQTMNG'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARAQTMNG'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARAQTMNG'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARAQTMNG'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARAQTMNG'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARASALES GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marasales.
    ls_entity_info-get_meth         = 'GET_MARASALES'.
    ls_entity_info-set_meth         = 'SET_MARASALES'.
    ls_entity_info-del_meth         = 'DEL_MARASALES'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARASALES'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARASALES'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARASALES'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARASALES'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARASALES'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARASPM GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>cs_entities-maraspm.
    ls_entity_info-get_meth         = 'GET_MARASPM'.
    ls_entity_info-set_meth         = 'SET_MARASPM'.
    ls_entity_info-del_meth         = 'DEL_MARASPM'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARASPM'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARASPM'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARASPM'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARASPM'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARASPM'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARASTOR GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>cs_entities-marastor.
    ls_entity_info-get_meth         = 'GET_MARASTOR'.
    ls_entity_info-set_meth         = 'SET_MARASTOR'.
    ls_entity_info-del_meth         = 'DEL_MARASTOR'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARASTOR'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARASTOR'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARASTOR'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARASTOR'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARASTOR'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARCATP GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcatp.
    ls_entity_info-get_meth         = 'GET_MARCATP'.
    ls_entity_info-set_meth         = 'SET_MARCATP'.
    ls_entity_info-del_meth         = 'DEL_MARCATP'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARCATP'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARCATP'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARCATP'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARCATP'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARCATP'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARCBASIC GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcbasic.
    ls_entity_info-get_meth         = 'GET_MARCBASIC'.
    ls_entity_info-set_meth         = 'SET_MARCBASIC'.
    ls_entity_info-del_meth         = 'DEL_MARCBASIC'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARCBASIC'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARCBASIC'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARCBASIC'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARCBASIC'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARCBASIC'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARCCSTNG GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marccstng.
    ls_entity_info-get_meth         = 'GET_MARCCSTNG'.
    ls_entity_info-set_meth         = 'SET_MARCCSTNG'.
    ls_entity_info-del_meth         = 'DEL_MARCCSTNG'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARCCSTNG'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARCCSTNG'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARCCSTNG'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARCCSTNG'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARCCSTNG'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARCFRCST GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcfrcst.
    ls_entity_info-get_meth         = 'GET_MARCFRCST'.
    ls_entity_info-set_meth         = 'SET_MARCFRCST'.
    ls_entity_info-del_meth         = 'DEL_MARCFRCST'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARCFRCST'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARCFRCST'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARCFRCST'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARCFRCST'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARCFRCST'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARCFRGTR GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcfrgtr.
    ls_entity_info-get_meth         = 'GET_MARCFRGTR'.
    ls_entity_info-set_meth         = 'SET_MARCFRGTR'.
    ls_entity_info-del_meth         = 'DEL_MARCFRGTR'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARCFRGTR'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARCFRGTR'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARCFRGTR'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARCFRGTR'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARCFRGTR'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARCFRPAR GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcfrpar.
    ls_entity_info-get_meth         = 'GET_MARCFRPAR'.
    ls_entity_info-set_meth         = 'SET_MARCFRPAR'.
    ls_entity_info-del_meth         = 'DEL_MARCFRPAR'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARCFRPAR'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARCFRPAR'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARCFRPAR'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARCFRPAR'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARCFRPAR'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method marcmrpfc GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcmrpfc.
    ls_entity_info-get_meth         = 'GET_MARCMRPFC'.
    ls_entity_info-set_meth         = 'SET_MARCMRPFC'.
    ls_entity_info-del_meth         = 'DEL_MARCMRPFC'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARCMRPFC'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARCMRPFC'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARCMRPFC'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARCMRPFC'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARCMRPFC'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARCMRPLS GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcmrpls.
    ls_entity_info-get_meth         = 'GET_MARCMRPLS'.
    ls_entity_info-set_meth         = 'SET_MARCMRPLS'.
    ls_entity_info-del_meth         = 'DEL_MARCMRPLS'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARCMRPLS'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARCMRPLS'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARCMRPLS'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARCMRPLS'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARCMRPLS'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARCMRPMI GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcmrpmi.
    ls_entity_info-get_meth         = 'GET_MARCMRPMI'.
    ls_entity_info-set_meth         = 'SET_MARCMRPMI'.
    ls_entity_info-del_meth         = 'DEL_MARCMRPMI'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARCMRPMI'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARCMRPMI'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARCMRPMI'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARCMRPMI'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARCMRPMI'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARCMRPPP GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcmrppp.
    ls_entity_info-get_meth         = 'GET_MARCMRPPP'.
    ls_entity_info-set_meth         = 'SET_MARCMRPPP'.
    ls_entity_info-del_meth         = 'DEL_MARCMRPPP'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARCMRPPP'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARCMRPPP'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARCMRPPP'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARCMRPPP'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARCMRPPP'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARCMRPSP GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcmrpsp.
    ls_entity_info-get_meth         = 'GET_MARCMRPSP'.
    ls_entity_info-set_meth         = 'SET_MARCMRPSP'.
    ls_entity_info-del_meth         = 'DEL_MARCMRPSP'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARCMRPSP'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARCMRPSP'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARCMRPSP'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARCMRPSP'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARCMRPSP'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARCPURCH GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>cs_entities-marcpurch.
    ls_entity_info-get_meth         = 'GET_MARCPURCH'.
    ls_entity_info-set_meth         = 'SET_MARCPURCH'.
    ls_entity_info-del_meth         = 'DEL_MARCPURCH'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARCPURCH'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARCPURCH'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARCPURCH'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARCPURCH'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARCPURCH'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARCQTMNG GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcqtmng.
    ls_entity_info-get_meth         = 'GET_MARCQTMNG'.
    ls_entity_info-set_meth         = 'SET_MARCQTMNG'.
    ls_entity_info-del_meth         = 'DEL_MARCQTMNG'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARCQTMNG'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARCQTMNG'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARCQTMNG'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARCQTMNG'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARCQTMNG'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARCSALES GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcsales.
    ls_entity_info-get_meth         = 'GET_MARCSALES'.
    ls_entity_info-set_meth         = 'SET_MARCSALES'.
    ls_entity_info-del_meth         = 'DEL_MARCSALES'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARCSALES'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARCSALES'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARCSALES'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARCSALES'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARCSALES'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARCSTORE GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>cs_entities-marcstore.
    ls_entity_info-get_meth         = 'GET_MARCSTORE'.
    ls_entity_info-set_meth         = 'SET_MARCSTORE'.
    ls_entity_info-del_meth         = 'DEL_MARCSTORE'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARCSTORE'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARCSTORE'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARCSTORE'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARCSTORE'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARCSTORE'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARCWRKSD GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcwrksd.
    ls_entity_info-get_meth         = 'GET_MARCWRKSD'.
    ls_entity_info-set_meth         = 'SET_MARCWRKSD'.
    ls_entity_info-del_meth         = 'DEL_MARCWRKSD'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARCWRKSD'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARCWRKSD'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARCWRKSD'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARCWRKSD'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARCWRKSD'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARDMRP GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mardmrp.
    ls_entity_info-get_meth         = 'GET_MARDMRP'.
    ls_entity_info-set_meth         = 'SET_MARDMRP'.
    ls_entity_info-del_meth         = 'DEL_MARDMRP'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARDMRP'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARDMRP'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARDMRP'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARDMRP'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARDMRP'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARCPRT GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcprt.
    ls_entity_info-get_meth         = 'GET_MARCPRT'.
    ls_entity_info-set_meth         = 'SET_MARCPRT'.
    ls_entity_info-del_meth         = 'DEL_MARCPRT'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARCPRT'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARCPRT'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARCPRT'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARCPRT'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARCPRT'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MARDSTOR GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mardstor.
    ls_entity_info-get_meth         = 'GET_MARDSTOR'.
    ls_entity_info-set_meth         = 'SET_MARDSTOR'.
    ls_entity_info-del_meth         = 'DEL_MARDSTOR'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MARDSTOR'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MARDSTOR'.
    ls_entity_info-get_meth_exp_tab = 'ET_MARDSTOR'.
    ls_entity_info-del_meth_imp_tab = 'IT_MARDSTOR'.
    ls_entity_info-set_meth_imp_tab = 'IT_MARDSTOR'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MATCHGMNG GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>cs_entities-matchgmng.
    ls_entity_info-get_meth         = 'GET_MATCHGMNG'.
    ls_entity_info-set_meth         = 'SET_MATCHGMNG'.
    ls_entity_info-del_meth         = 'DEL_MATCHGMNG'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MATCHGMNG'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MATCHGMNG'.
    ls_entity_info-get_meth_exp_tab = 'ET_MATCHGMNG'.
    ls_entity_info-del_meth_imp_tab = 'IT_MATCHGMNG'.
    ls_entity_info-set_meth_imp_tab = 'IT_MATCHGMNG'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MATERIAL GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_material.
    ls_entity_info-get_meth         = 'GET_MATERIAL'.
    ls_entity_info-set_meth         = 'SET_MATERIAL'.
    ls_entity_info-del_meth         = 'DEL_MATERIAL'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MATERIAL'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MATERIAL'.
    ls_entity_info-get_meth_exp_tab = 'ET_MATERIAL'.
    ls_entity_info-del_meth_imp_tab = 'IT_MATERIAL'.
    ls_entity_info-set_meth_imp_tab = 'IT_MATERIAL'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MBEWACTNG GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mbewactng.
    ls_entity_info-get_meth         = 'GET_MBEWACTNG'.
    ls_entity_info-set_meth         = 'SET_MBEWACTNG'.
    ls_entity_info-del_meth         = 'DEL_MBEWACTNG'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MBEWACTNG'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MBEWACTNG'.
    ls_entity_info-get_meth_exp_tab = 'ET_MBEWACTNG'.
    ls_entity_info-del_meth_imp_tab = 'IT_MBEWACTNG'.
    ls_entity_info-set_meth_imp_tab = 'IT_MBEWACTNG'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MBEWCSTNG GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mbewcstng.
    ls_entity_info-get_meth         = 'GET_MBEWCSTNG'.
    ls_entity_info-set_meth         = 'SET_MBEWCSTNG'.
    ls_entity_info-del_meth         = 'DEL_MBEWCSTNG'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MBEWCSTNG'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MBEWCSTNG'.
    ls_entity_info-get_meth_exp_tab = 'ET_MBEWCSTNG'.
    ls_entity_info-del_meth_imp_tab = 'IT_MBEWCSTNG'.
    ls_entity_info-set_meth_imp_tab = 'IT_MBEWCSTNG'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MBEWMLAC GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mbewmlac.
    ls_entity_info-get_meth         = 'GET_MBEWMLAC'.
    ls_entity_info-set_meth         = 'SET_MBEWMLAC'.
    ls_entity_info-del_meth         = 'DEL_MBEWMLAC'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MBEWMLAC'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MBEWMLAC'.
    ls_entity_info-get_meth_exp_tab = 'ET_MBEWMLAC'.
    ls_entity_info-del_meth_imp_tab = 'IT_MBEWMLAC'.
    ls_entity_info-set_meth_imp_tab = 'IT_MBEWMLAC'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MBEWMLVAL GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mbewmlval.
    ls_entity_info-get_meth         = 'GET_MBEWMLVAL'.
    ls_entity_info-set_meth         = 'SET_MBEWMLVAL'.
    ls_entity_info-del_meth         = 'DEL_MBEWMLVAL'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MBEWMLVAL'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MBEWMLVAL'.
    ls_entity_info-get_meth_exp_tab = 'ET_MBEWMLVAL'.
    ls_entity_info-del_meth_imp_tab = 'IT_MBEWMLVAL'.
    ls_entity_info-set_meth_imp_tab = 'IT_MBEWMLVAL'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MBEWVALUA GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mbewvalua.
    ls_entity_info-get_meth         = 'GET_MBEWVALUA'.
    ls_entity_info-set_meth         = 'SET_MBEWVALUA'.
    ls_entity_info-del_meth         = 'DEL_MBEWVALUA'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MBEWVALUA'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MBEWVALUA'.
    ls_entity_info-get_meth_exp_tab = 'ET_MBEWVALUA'.
    ls_entity_info-del_meth_imp_tab = 'IT_MBEWVALUA'.
    ls_entity_info-set_meth_imp_tab = 'IT_MBEWVALUA'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MDMABASIC GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mdmabasic.
    ls_entity_info-get_meth         = 'GET_MDMABASIC'.
    ls_entity_info-set_meth         = 'SET_MDMABASIC'.
    ls_entity_info-del_meth         = 'DEL_MDMABASIC'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MDMABASIC'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MDMABASIC'.
    ls_entity_info-get_meth_exp_tab = 'ET_MDMABASIC'.
    ls_entity_info-del_meth_imp_tab = 'IT_MDMABASIC'.
    ls_entity_info-set_meth_imp_tab = 'IT_MDMABASIC'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MEAN_GTIN GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mean_gtin.
    ls_entity_info-get_meth         = 'GET_MEAN_GTIN'.
    ls_entity_info-set_meth         = 'SET_MEAN_GTIN'.
    ls_entity_info-del_meth         = 'DEL_MEAN_GTIN'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MEAN_GTIN'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MEAN_GTIN'.
    ls_entity_info-get_meth_exp_tab = 'ET_MEAN_GTIN'.
    ls_entity_info-del_meth_imp_tab = 'IT_MEAN_GTIN'.
    ls_entity_info-set_meth_imp_tab = 'IT_MEAN_GTIN'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MKALBASIC GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mkalbasic.
    ls_entity_info-get_meth         = 'GET_MKALBASIC'.
    ls_entity_info-set_meth         = 'SET_MKALBASIC'.
    ls_entity_info-del_meth         = 'DEL_MKALBASIC'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MKALBASIC'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MKALBASIC'.
    ls_entity_info-get_meth_exp_tab = 'ET_MKALBASIC'.
    ls_entity_info-del_meth_imp_tab = 'IT_MKALBASIC'.
    ls_entity_info-set_meth_imp_tab = 'IT_MKALBASIC'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MLANPURCH GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mlanpurch.
    ls_entity_info-get_meth         = 'GET_MLANPURCH'.
    ls_entity_info-set_meth         = 'SET_MLANPURCH'.
    ls_entity_info-del_meth         = 'DEL_MLANPURCH'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MLANPURCH'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MLANPURCH'.
    ls_entity_info-get_meth_exp_tab = 'ET_MLANPURCH'.
    ls_entity_info-del_meth_imp_tab = 'IT_MLANPURCH'.
    ls_entity_info-set_meth_imp_tab = 'IT_MLANPURCH'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MLANSALES GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mlansales.
    ls_entity_info-get_meth         = 'GET_MLANSALES'.
    ls_entity_info-set_meth         = 'SET_MLANSALES'.
    ls_entity_info-del_meth         = 'DEL_MLANSALES'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MLANSALES'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MLANSALES'.
    ls_entity_info-get_meth_exp_tab = 'ET_MLANSALES'.
    ls_entity_info-del_meth_imp_tab = 'IT_MLANSALES'.
    ls_entity_info-set_meth_imp_tab = 'IT_MLANSALES'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MLGNSTOR GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mlgnstor.
    ls_entity_info-get_meth         = 'GET_MLGNSTOR'.
    ls_entity_info-set_meth         = 'SET_MLGNSTOR'.
    ls_entity_info-del_meth         = 'DEL_MLGNSTOR'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MLGNSTOR'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MLGNSTOR'.
    ls_entity_info-get_meth_exp_tab = 'ET_MLGNSTOR'.
    ls_entity_info-del_meth_imp_tab = 'IT_MLGNSTOR'.
    ls_entity_info-set_meth_imp_tab = 'IT_MLGNSTOR'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MLGTSTOR GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mlgtstor.
    ls_entity_info-get_meth         = 'GET_MLGTSTOR'.
    ls_entity_info-set_meth         = 'SET_MLGTSTOR'.
    ls_entity_info-del_meth         = 'DEL_MLGTSTOR'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MLGTSTOR'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MLGTSTOR'.
    ls_entity_info-get_meth_exp_tab = 'ET_MLGTSTOR'.
    ls_entity_info-del_meth_imp_tab = 'IT_MLGTSTOR'.
    ls_entity_info-set_meth_imp_tab = 'IT_MLGTSTOR'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MPGDPRODG GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mpgdprodg.
    ls_entity_info-get_meth         = 'GET_MPGDPRODG'.
    ls_entity_info-set_meth         = 'SET_MPGDPRODG'.
    ls_entity_info-del_meth         = 'DEL_MPGDPRODG'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MPGDPRODG'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MPGDPRODG'.
    ls_entity_info-get_meth_exp_tab = 'ET_MPGDPRODG'.
    ls_entity_info-del_meth_imp_tab = 'IT_MPGDPRODG'.
    ls_entity_info-set_meth_imp_tab = 'IT_MPGDPRODG'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MRPTXT GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mrptxt.
    ls_entity_info-get_meth         = 'GET_MRPTXT'.
    ls_entity_info-set_meth         = 'SET_MRPTXT'.
    ls_entity_info-del_meth         = 'DEL_MRPTXT'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MRPTXT'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MRPTXT'.
    ls_entity_info-get_meth_exp_tab = 'ET_MRPTXT'.
    ls_entity_info-del_meth_imp_tab = 'IT_MRPTXT'.
    ls_entity_info-set_meth_imp_tab = 'IT_MRPTXT'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.


* Writes the information from method MVKEGRPNG GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mvkegrpng.
    ls_entity_info-get_meth         = 'GET_MVKEGRPNG'.
    ls_entity_info-set_meth         = 'SET_MVKEGRPNG'.
    ls_entity_info-del_meth         = 'DEL_MVKEGRPNG'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MVKEGRPNG'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MVKEGRPNG'.
    ls_entity_info-get_meth_exp_tab = 'ET_MVKEGRPNG'.
    ls_entity_info-del_meth_imp_tab = 'IT_MVKEGRPNG'.
    ls_entity_info-set_meth_imp_tab = 'IT_MVKEGRPNG'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MVKESALES GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mvkesales.
    ls_entity_info-get_meth         = 'GET_MVKESALES'.
    ls_entity_info-set_meth         = 'SET_MVKESALES'.
    ls_entity_info-del_meth         = 'DEL_MVKESALES'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_MVKESALES'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MVKESALES'.
    ls_entity_info-get_meth_exp_tab = 'ET_MVKESALES'.
    ls_entity_info-del_meth_imp_tab = 'IT_MVKESALES'.
    ls_entity_info-set_meth_imp_tab = 'IT_MVKESALES'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method PURCHTXT GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_purchtxt.
    ls_entity_info-get_meth         = 'GET_PURCHTXT'.
    ls_entity_info-set_meth         = 'SET_PURCHTXT'.
    ls_entity_info-del_meth         = 'DEL_PURCHTXT'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_PURCHTXT'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_PURCHTXT'.
    ls_entity_info-get_meth_exp_tab = 'ET_PURCHTXT'.
    ls_entity_info-del_meth_imp_tab = 'IT_PURCHTXT'.
    ls_entity_info-set_meth_imp_tab = 'IT_PURCHTXT'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method QINSPTXT GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_qinsptxt.
    ls_entity_info-get_meth         = 'GET_QINSPTXT'.
    ls_entity_info-set_meth         = 'SET_QINSPTXT'.
    ls_entity_info-del_meth         = 'DEL_QINSPTXT'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_QINSPTXT'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_QINSPTXT'.
    ls_entity_info-get_meth_exp_tab = 'ET_QINSPTXT'.
    ls_entity_info-del_meth_imp_tab = 'IT_QINSPTXT'.
    ls_entity_info-set_meth_imp_tab = 'IT_QINSPTXT'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method QMATBASIC GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_qmatbasic.
    ls_entity_info-get_meth         = 'GET_QMATBASIC'.
    ls_entity_info-set_meth         = 'SET_QMATBASIC'.
    ls_entity_info-del_meth         = 'DEL_QMATBASIC'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_QMATBASIC'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_QMATBASIC'.
    ls_entity_info-get_meth_exp_tab = 'ET_QMATBASIC'.
    ls_entity_info-del_meth_imp_tab = 'IT_QMATBASIC'.
    ls_entity_info-set_meth_imp_tab = 'IT_QMATBASIC'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method SALESTXT GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_salestxt.
    ls_entity_info-get_meth         = 'GET_SALESTXT'.
    ls_entity_info-set_meth         = 'SET_SALESTXT'.
    ls_entity_info-del_meth         = 'DEL_SALESTXT'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_SALESTXT'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_SALESTXT'.
    ls_entity_info-get_meth_exp_tab = 'ET_SALESTXT'.
    ls_entity_info-del_meth_imp_tab = 'IT_SALESTXT'.
    ls_entity_info-set_meth_imp_tab = 'IT_SALESTXT'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method UNITOFMSR GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_unitofmsr.
    ls_entity_info-get_meth         = 'GET_UNITOFMSR'.
    ls_entity_info-set_meth         = 'SET_UNITOFMSR'.
    ls_entity_info-del_meth         = 'DEL_UNITOFMSR'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_UNITOFMSR'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_UNITOFMSR'.
    ls_entity_info-get_meth_exp_tab = 'ET_UNITOFMSR'.
    ls_entity_info-del_meth_imp_tab = 'IT_UNITOFMSR'.
    ls_entity_info-set_meth_imp_tab = 'IT_UNITOFMSR'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method VALUATION GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_valuation.
    ls_entity_info-get_meth         = 'GET_VALUATION'.
    ls_entity_info-set_meth         = 'SET_VALUATION'.
    ls_entity_info-del_meth         = 'DEL_VALUATION'.
    ls_entity_info-structure        = '/MDGMM/_S_MM_PP_VALUATION'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_VALUATION'.
    ls_entity_info-get_meth_exp_tab = 'ET_VALUATION'.
    ls_entity_info-del_meth_imp_tab = 'IT_VALUATION'.
    ls_entity_info-set_meth_imp_tab = 'IT_VALUATION'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.

* Writes the information from method MATTXT GET_, SET_ and DEL_ into rt_entity_info
    CLEAR ls_entity_info.
    ls_entity_info-entity           = zcl_mdg_mm_helper=>cs_entities-material_txt.
    ls_entity_info-get_meth         = 'GET_MATTXT'.
    ls_entity_info-set_meth         = 'SET_MATTXT'.
    ls_entity_info-del_meth         = 'DEL_MATTXT'.
    ls_entity_info-structure        = '/MDGMM/_ST_MM_PP_MATERIAL'.
    ls_entity_info-tab_type         = 'zif_mdg_mm_datatypes=>gty_t_MATTXT'.
    ls_entity_info-get_meth_exp_tab = 'ET_MATTXT'.
    ls_entity_info-del_meth_imp_tab = 'IT_MATTXT'.
    ls_entity_info-set_meth_imp_tab = 'IT_MATTXT'.
    INSERT ls_entity_info INTO TABLE rt_entity_info.


  ENDMETHOD.


  METHOD get_entity_reference.

    CONSTANTS:
      c_prefix TYPE string VALUE 'GT_'.

    DATA:
     lv_gt_name TYPE seocpdname.

    FIELD-SYMBOLS:
      <lt_entity>  TYPE SORTED TABLE.

    CLEAR er_entity.

    CONCATENATE c_prefix iv_entity INTO lv_gt_name.

    ASSIGN (lv_gt_name) TO <lt_entity>.
    IF sy-subrc <> 0.
      RETURN.
    ENDIF.
    GET REFERENCE OF <lt_entity> INTO er_entity.

  ENDMETHOD.


  METHOD get_intcmnt.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_intcmnt, es_intcmnt.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_intcmnt
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_intcmnt ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_intcmnt.
      ENDLOOP.
    ELSE .
      et_intcmnt = gt_intcmnt.
    ENDIF.

    IF lines( et_intcmnt ) = 1.
      READ TABLE et_intcmnt INTO es_intcmnt INDEX 1.
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


  METHOD get_marapurch.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marapurch, es_marapurch.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marapurch
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marapurch ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marapurch.
      ENDLOOP.
    ELSE .
      et_marapurch = gt_marapurch.
    ENDIF.

    IF lines( et_marapurch ) = 1.
      READ TABLE et_marapurch INTO es_marapurch INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_maraqtmng.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_maraqtmng, es_maraqtmng.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>cs_entities-maraqtmng
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_maraqtmng ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_maraqtmng.
      ENDLOOP.
    ELSE .
      et_maraqtmng = gt_maraqtmng.
    ENDIF.

    IF lines( et_maraqtmng ) = 1.
      READ TABLE et_maraqtmng INTO es_maraqtmng INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marasales.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marasales, es_marasales.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marasales
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marasales ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marasales.
      ENDLOOP.
    ELSE .
      et_marasales = gt_marasales.
    ENDIF.

    IF lines( et_marasales ) = 1.
      READ TABLE et_marasales INTO es_marasales INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_maraspm.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_maraspm, es_maraspm.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>cs_entities-maraspm
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_maraspm ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_maraspm.
      ENDLOOP.
    ELSE .
      et_maraspm = gt_maraspm.
    ENDIF.

    IF lines( et_maraspm ) = 1.
      READ TABLE et_maraspm INTO es_maraspm INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marastor.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marastor, es_marastor.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>cs_entities-marastor
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marastor ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marastor.
      ENDLOOP.
    ELSE .
      et_marastor = gt_marastor.
    ENDIF.

    IF lines( et_marastor ) = 1.
      READ TABLE et_marastor INTO es_marastor INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marcatp.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marcatp, es_marcatp.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcatp
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marcatp ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marcatp.
      ENDLOOP.
    ELSE .
      et_marcatp = gt_marcatp.
    ENDIF.

    IF lines( et_marcatp ) = 1.
      READ TABLE et_marcatp INTO es_marcatp INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marcbasic.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marcbasic, es_marcbasic.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcbasic
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marcbasic ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marcbasic.
      ENDLOOP.
    ELSE .
      et_marcbasic = gt_marcbasic.
    ENDIF.

    IF lines( et_marcbasic ) = 1.
      READ TABLE et_marcbasic INTO es_marcbasic INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marccstng.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marccstng, es_marccstng.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marccstng
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marccstng ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marccstng.
      ENDLOOP.
    ELSE .
      et_marccstng = gt_marccstng.
    ENDIF.

    IF lines( et_marccstng ) = 1.
      READ TABLE et_marccstng INTO es_marccstng INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marcfrcst.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marcfrcst, es_marcfrcst.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcfrcst
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marcfrcst ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marcfrcst.
      ENDLOOP.
    ELSE .
      et_marcfrcst = gt_marcfrcst.
    ENDIF.

    IF lines( et_marcfrcst ) = 1.
      READ TABLE et_marcfrcst INTO es_marcfrcst INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marcfrgtr.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marcfrgtr, es_marcfrgtr.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcfrgtr
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marcfrgtr ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marcfrgtr.
      ENDLOOP.
    ELSE .
      et_marcfrgtr = gt_marcfrgtr.
    ENDIF.

    IF lines( et_marcfrgtr ) = 1.
      READ TABLE et_marcfrgtr INTO es_marcfrgtr INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marcfrpar.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marcfrpar, es_marcfrpar.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcfrpar
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marcfrpar ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marcfrpar.
      ENDLOOP.
    ELSE .
      et_marcfrpar = gt_marcfrpar.
    ENDIF.

    IF lines( et_marcfrpar ) = 1.
      READ TABLE et_marcfrpar INTO es_marcfrpar INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marcmrpfc.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marcmrpfc, es_marcmrpfc.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcmrpfc
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marcmrpfc ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marcmrpfc.
      ENDLOOP.
    ELSE .
      et_marcmrpfc = gt_marcmrpfc.
    ENDIF.

    IF lines( et_marcmrpfc ) = 1.
      READ TABLE et_marcmrpfc INTO es_marcmrpfc INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marcmrpls.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marcmrpls, es_marcmrpls.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcmrpls
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marcmrpls ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marcmrpls.
      ENDLOOP.
    ELSE .
      et_marcmrpls = gt_marcmrpls.
    ENDIF.

    IF lines( et_marcmrpls ) = 1.
      READ TABLE et_marcmrpls INTO es_marcmrpls INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marcmrpmi.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marcmrpmi, es_marcmrpmi.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcmrpmi
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marcmrpmi ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marcmrpmi.
      ENDLOOP.
    ELSE .
      et_marcmrpmi = gt_marcmrpmi.
    ENDIF.

    IF lines( et_marcmrpmi ) = 1.
      READ TABLE et_marcmrpmi INTO es_marcmrpmi INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marcmrppp.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marcmrppp, es_marcmrppp.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcmrppp
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marcmrppp ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marcmrppp.
      ENDLOOP.
    ELSE .
      et_marcmrppp = gt_marcmrppp.
    ENDIF.

    IF lines( et_marcmrppp ) = 1.
      READ TABLE et_marcmrppp INTO es_marcmrppp INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marcmrpsp.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marcmrpsp, es_marcmrpsp.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcmrpsp
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marcmrpsp ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marcmrpsp.
      ENDLOOP.
    ELSE .
      et_marcmrpsp = gt_marcmrpsp.
    ENDIF.

    IF lines( et_marcmrpsp ) = 1.
      READ TABLE et_marcmrpsp INTO es_marcmrpsp INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marcprt.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marcprt, es_marcprt.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcprt
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marcprt ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marcprt.
      ENDLOOP.
    ELSE .
      et_marcprt = gt_marcprt.
    ENDIF.

    IF lines( et_marcprt ) = 1.
      READ TABLE et_marcprt INTO es_marcprt INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marcpurch.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marcpurch, es_marcpurch.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>cs_entities-marcpurch
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marcpurch ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marcpurch.
      ENDLOOP.
    ELSE .
      et_marcpurch = gt_marcpurch.
    ENDIF.

    IF lines( et_marcpurch ) = 1.
      READ TABLE et_marcpurch INTO es_marcpurch INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marcqtmng.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marcqtmng, es_marcqtmng.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcqtmng
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marcqtmng ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marcqtmng.
      ENDLOOP.
    ELSE .
      et_marcqtmng = gt_marcqtmng.
    ENDIF.

    IF lines( et_marcqtmng ) = 1.
      READ TABLE et_marcqtmng INTO es_marcqtmng INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marcsales.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marcsales, es_marcsales.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcsales
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marcsales ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marcsales.
      ENDLOOP.
    ELSE .
      et_marcsales = gt_marcsales.
    ENDIF.

    IF lines( et_marcsales ) = 1.
      READ TABLE et_marcsales INTO es_marcsales INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marcstore.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marcstore, es_marcstore.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>cs_entities-marcstore
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marcstore ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marcstore.
      ENDLOOP.
    ELSE .
      et_marcstore = gt_marcstore.
    ENDIF.

    IF lines( et_marcstore ) = 1.
      READ TABLE et_marcstore INTO es_marcstore INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_marcwrksd.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_marcwrksd, es_marcwrksd.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_marcwrksd
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_marcwrksd ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_marcwrksd.
      ENDLOOP.
    ELSE .
      et_marcwrksd = gt_marcwrksd.
    ENDIF.

    IF lines( et_marcwrksd ) = 1.
      READ TABLE et_marcwrksd INTO es_marcwrksd INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mardmrp.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mardmrp, es_mardmrp.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mardmrp
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mardmrp ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mardmrp.
      ENDLOOP.
    ELSE .
      et_mardmrp = gt_mardmrp.
    ENDIF.

    IF lines( et_mardmrp ) = 1.
      READ TABLE et_mardmrp INTO es_mardmrp INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mardstor.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mardstor, es_mardstor.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mardstor
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mardstor ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mardstor.
      ENDLOOP.
    ELSE .
      et_mardstor = gt_mardstor.
    ENDIF.

    IF lines( et_mardstor ) = 1.
      READ TABLE et_mardstor INTO es_mardstor INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_matchgmng.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_matchgmng, es_matchgmng.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>cs_entities-matchgmng
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_matchgmng ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_matchgmng.
      ENDLOOP.
    ELSE .
      et_matchgmng = gt_matchgmng.
    ENDIF.

    IF lines( et_matchgmng ) = 1.
      READ TABLE et_matchgmng INTO es_matchgmng INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_material.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_material, es_material.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_material
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_material ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_material.
      ENDLOOP.
    ELSE .
      et_material = gt_material.
    ENDIF.

    IF lines( et_material ) = 1.
      READ TABLE et_material INTO es_material INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mattxt.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mattxt, es_mattxt.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>cs_entities-material_txt
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mattxt ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mattxt.
      ENDLOOP.
    ELSE .
      et_mattxt = gt_mattxt.
    ENDIF.

    IF lines( et_mattxt ) = 1.
      READ TABLE et_mattxt INTO es_mattxt INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mbewactng.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mbewactng, es_mbewactng.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mbewactng
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mbewactng ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mbewactng.
      ENDLOOP.
    ELSE .
      et_mbewactng = gt_mbewactng.
    ENDIF.

    IF lines( et_mbewactng ) = 1.
      READ TABLE et_mbewactng INTO es_mbewactng INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mbewcstng.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mbewcstng, es_mbewcstng.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mbewcstng
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mbewcstng ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mbewcstng.
      ENDLOOP.
    ELSE .
      et_mbewcstng = gt_mbewcstng.
    ENDIF.

    IF lines( et_mbewcstng ) = 1.
      READ TABLE et_mbewcstng INTO es_mbewcstng INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mbewmlac.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mbewmlac, es_mbewmlac.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mbewmlac
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mbewmlac ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mbewmlac.
      ENDLOOP.
    ELSE .
      et_mbewmlac = gt_mbewmlac.
    ENDIF.

    IF lines( et_mbewmlac ) = 1.
      READ TABLE et_mbewmlac INTO es_mbewmlac INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mbewmlval.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mbewmlval, es_mbewmlval.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mbewmlval
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mbewmlval ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mbewmlval.
      ENDLOOP.
    ELSE .
      et_mbewmlval = gt_mbewmlval.
    ENDIF.

    IF lines( et_mbewmlval ) = 1.
      READ TABLE et_mbewmlval INTO es_mbewmlval INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mbewvalua.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mbewvalua, es_mbewvalua.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mbewvalua
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mbewvalua ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mbewvalua.
      ENDLOOP.
    ELSE .
      et_mbewvalua = gt_mbewvalua.
    ENDIF.

    IF lines( et_mbewvalua ) = 1.
      READ TABLE et_mbewvalua INTO es_mbewvalua INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mdmabasic.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mdmabasic, es_mdmabasic.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mdmabasic
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mdmabasic ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mdmabasic.
      ENDLOOP.
    ELSE .
      et_mdmabasic = gt_mdmabasic.
    ENDIF.

    IF lines( et_mdmabasic ) = 1.
      READ TABLE et_mdmabasic INTO es_mdmabasic INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mean_gtin.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mean_gtin, es_mean_gtin.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mean_gtin
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mean_gtin ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mean_gtin.
      ENDLOOP.
    ELSE .
      et_mean_gtin = gt_mean_gtin.
    ENDIF.

    IF lines( et_mean_gtin ) = 1.
      READ TABLE et_mean_gtin INTO es_mean_gtin INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mkalbasic.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mkalbasic, es_mkalbasic.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mkalbasic
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mkalbasic ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mkalbasic.
      ENDLOOP.
    ELSE .
      et_mkalbasic = gt_mkalbasic.
    ENDIF.

    IF lines( et_mkalbasic ) = 1.
      READ TABLE et_mkalbasic INTO es_mkalbasic INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mlanpurch.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mlanpurch, es_mlanpurch.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mlanpurch
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mlanpurch ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mlanpurch.
      ENDLOOP.
    ELSE .
      et_mlanpurch = gt_mlanpurch.
    ENDIF.

    IF lines( et_mlanpurch ) = 1.
      READ TABLE et_mlanpurch INTO es_mlanpurch INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mlansales.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mlansales, es_mlansales.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mlansales
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mlansales ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mlansales.
      ENDLOOP.
    ELSE .
      et_mlansales = gt_mlansales.
    ENDIF.

    IF lines( et_mlansales ) = 1.
      READ TABLE et_mlansales INTO es_mlansales INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mlgnstor.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mlgnstor, es_mlgnstor.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mlgnstor
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mlgnstor ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mlgnstor.
      ENDLOOP.
    ELSE .
      et_mlgnstor = gt_mlgnstor.
    ENDIF.

    IF lines( et_mlgnstor ) = 1.
      READ TABLE et_mlgnstor INTO es_mlgnstor INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mlgtstor.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mlgtstor, es_mlgtstor.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mlgtstor
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mlgtstor ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mlgtstor.
      ENDLOOP.
    ELSE .
      et_mlgtstor = gt_mlgtstor.
    ENDIF.

    IF lines( et_mlgtstor ) = 1.
      READ TABLE et_mlgtstor INTO es_mlgtstor INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mpgdprodg.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mpgdprodg, es_mpgdprodg.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mpgdprodg
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mpgdprodg ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mpgdprodg.
      ENDLOOP.
    ELSE .
      et_mpgdprodg = gt_mpgdprodg.
    ENDIF.

    IF lines( et_mpgdprodg ) = 1.
      READ TABLE et_mpgdprodg INTO es_mpgdprodg INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mrptxt.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mrptxt, es_mrptxt.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mrptxt
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mrptxt ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mrptxt.
      ENDLOOP.
    ELSE .
      et_mrptxt = gt_mrptxt.
    ENDIF.

    IF lines( et_mrptxt ) = 1.
      READ TABLE et_mrptxt INTO es_mrptxt INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mvkegrpng.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mvkegrpng, es_mvkegrpng.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mvkegrpng
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mvkegrpng ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mvkegrpng.
      ENDLOOP.
    ELSE .
      et_mvkegrpng = gt_mvkegrpng.
    ENDIF.

    IF lines( et_mvkegrpng ) = 1.
      READ TABLE et_mvkegrpng INTO es_mvkegrpng INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_mvkesales.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_mvkesales, es_mvkesales.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_mvkesales
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_mvkesales ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_mvkesales.
      ENDLOOP.
    ELSE .
      et_mvkesales = gt_mvkesales.
    ENDIF.

    IF lines( et_mvkesales ) = 1.
      READ TABLE et_mvkesales INTO es_mvkesales INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_purchtxt.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_purchtxt, es_purchtxt.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_purchtxt
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_purchtxt ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_purchtxt.
      ENDLOOP.
    ELSE .
      et_purchtxt = gt_purchtxt.
    ENDIF.

    IF lines( et_purchtxt ) = 1.
      READ TABLE et_purchtxt INTO es_purchtxt INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_qinsptxt.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_qinsptxt, es_qinsptxt.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_qinsptxt
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_qinsptxt ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_qinsptxt.
      ENDLOOP.
    ELSE .
      et_qinsptxt = gt_qinsptxt.
    ENDIF.

    IF lines( et_qinsptxt ) = 1.
      READ TABLE et_qinsptxt INTO es_qinsptxt INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_qmatbasic.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_qmatbasic, es_qmatbasic.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_qmatbasic
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_qmatbasic ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_qmatbasic.
      ENDLOOP.
    ELSE .
      et_qmatbasic = gt_qmatbasic.
    ENDIF.

    IF lines( et_qmatbasic ) = 1.
      READ TABLE et_qmatbasic INTO es_qmatbasic INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_salestxt.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_salestxt, es_salestxt.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_salestxt
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_salestxt ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_salestxt.
      ENDLOOP.
    ELSE .
      et_salestxt = gt_salestxt.
    ENDIF.

    IF lines( et_salestxt ) = 1.
      READ TABLE et_salestxt INTO es_salestxt INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_unitofmsr.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_unitofmsr, es_unitofmsr.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_unitofmsr
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_unitofmsr ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_unitofmsr.
      ENDLOOP.
    ELSE .
      et_unitofmsr = gt_unitofmsr.
    ENDIF.

    IF lines( et_unitofmsr ) = 1.
      READ TABLE et_unitofmsr INTO es_unitofmsr INDEX 1.
    ENDIF.

  ENDMETHOD.


  METHOD get_valuation.

    DATA:
      lt_key_value TYPE zif_mdg_datatypes=>gty_t_key_value,
      lv_where     TYPE string.

    FIELD-SYMBOLS:
      <ls_data>      TYPE any.

    CLEAR: et_valuation, es_valuation.

    IF it_key_value IS SUPPLIED.

      CALL METHOD limit_key_value_table_entity
        EXPORTING
          iv_entity    = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_entity_valuation
          it_key_value = it_key_value
        IMPORTING
          et_key_value = lt_key_value.

      CALL METHOD get_where_condition
        EXPORTING
          it_key_value = lt_key_value
        IMPORTING
          ev_where     = lv_where.

      LOOP AT gt_valuation ASSIGNING <ls_data> WHERE (lv_where).
        INSERT <ls_data> INTO TABLE et_valuation.
      ENDLOOP.
    ELSE .
      et_valuation = gt_valuation.
    ENDIF.

    IF lines( et_valuation ) = 1.
      READ TABLE et_valuation INTO es_valuation INDEX 1.
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
          CONCATENATE ev_where <ls_key_value>-key_field ' = ' '''' lv_key INTO ev_where RESPECTING BLANKS.
          CONCATENATE ev_where  ''' )' INTO ev_where RESPECTING BLANKS.
        ENDIF.
      ENDLOOP.
    ENDIF.

  ENDMETHOD.


  METHOD init_dependent_entities.

    DATA:
      ls_dependent_entities TYPE zif_mdg_datatypes=>gty_s_dependent_entities.

*DRADBASIC
    ls_dependent_entities-entity = 'DRADBASIC'.
    ls_dependent_entities-dependent_entities = VALUE #( ( zcl_mdg_mm_helper=>cs_entities-dradtxt ) ).
    INSERT ls_dependent_entities INTO TABLE gt_dependent_entities.

*MATERIAL
    ls_dependent_entities-entity = 'MATERIAL'.
    ls_dependent_entities-dependent_entities = VALUE #( ( if_mdg_bs_mat_gen_c~gc_entity_marapurch )
                                                        ( zcl_mdg_mm_helper=>cs_entities-maraqtmng )
                                                        ( if_mdg_bs_mat_gen_c~gc_entity_marasales )
                                                        ( zcl_mdg_mm_helper=>cs_entities-maraspm )
                                                        ( zcl_mdg_mm_helper=>cs_entities-marastor ) ).
    INSERT ls_dependent_entities INTO TABLE gt_dependent_entities.

*MBEWVALUA
    ls_dependent_entities-entity = 'MBEWVALUA'.
    ls_dependent_entities-dependent_entities = VALUE #( ( if_mdg_bs_mat_gen_c=>gc_entity_mbewactng )
                                                        ( if_mdg_bs_mat_gen_c=>gc_entity_mbewcstng )
                                                        ( if_mdg_bs_mat_gen_c=>gc_entity_mbewmlac )
                                                        ( if_mdg_bs_mat_gen_c=>gc_entity_mbewmlval ) ).
    INSERT ls_dependent_entities INTO TABLE gt_dependent_entities.

*MARCBASIC
    ls_dependent_entities-entity ='MARCBASIC'.
    ls_dependent_entities-dependent_entities = VALUE #( ( if_mdg_bs_mat_gen_c=>gc_entity_marcatp )
                                                        ( if_mdg_bs_mat_gen_c=>gc_entity_marccstng )
                                                        ( if_mdg_bs_mat_gen_c=>gc_entity_marcfrcst )
                                                        ( if_mdg_bs_mat_gen_c=>gc_entity_marcfrgtr )
                                                        ( if_mdg_bs_mat_gen_c=>gc_entity_marcfrpar )
                                                        ( if_mdg_bs_mat_gen_c=>gc_entity_marcmrpfc )
                                                        ( if_mdg_bs_mat_gen_c=>gc_entity_marcmrpls )
                                                        ( if_mdg_bs_mat_gen_c=>gc_entity_marcmrpmi )
                                                        ( if_mdg_bs_mat_gen_c=>gc_entity_marcmrppp )
                                                        ( if_mdg_bs_mat_gen_c=>gc_entity_marcmrpsp )
                                                        ( if_mdg_bs_mat_gen_c=>gc_entity_marcprt )
                                                        ( if_mdg_bs_mat_gen_c=>gc_entity_marcqtmng )
                                                        ( if_mdg_bs_mat_gen_c=>gc_entity_marcsales )
                                                        ( if_mdg_bs_mat_gen_c=>gc_entity_marcwrksd )
                                                        ( if_mdg_bs_mat_gen_c=>gc_entity_mpgdprodg )
                                                        ( zcl_mdg_mm_helper=>cs_entities-marcpurch )
                                                        ( zcl_mdg_mm_helper=>cs_entities-marcstore ) ).
    INSERT ls_dependent_entities INTO TABLE gt_dependent_entities.

*MARDSTOR
    ls_dependent_entities-entity ='MARDSTOR'.
    ls_dependent_entities-dependent_entities = VALUE #( ( if_mdg_bs_mat_gen_c=>gc_entity_mardmrp ) ).
    INSERT ls_dependent_entities INTO TABLE gt_dependent_entities.

*MVKESALES
    ls_dependent_entities-entity ='MVKESALES'.
    ls_dependent_entities-dependent_entities = VALUE #( ( if_mdg_bs_mat_gen_c=>gc_entity_mvkegrpng ) ).
    INSERT ls_dependent_entities INTO TABLE gt_dependent_entities.

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
        MESSAGE e003(zmdg_bp_dm_msg) INTO zcl_mdg_general_functions=>gv_error_message RAISING entity_attribute_not_found.
        MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 003 RAISING entity_attribute_not_found.
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

      LOOP AT lt_components ASSIGNING <ls_component>. "#EC CI_NESTED
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
      ls_component   TYPE abap_compdescr,
      ls_entity_cont TYPE usmd_s_entity_cont,
      lt_entities    TYPE usmd_t_entity,
      lt_components  TYPE abap_compdescr_tab,
      lv_fieldname   TYPE usmd_fieldname.

    FIELD-SYMBOLS:
      <lv_entity>    TYPE usmd_entity,
      <lv_component> TYPE any.

* loop over all type 1 and 4 entites to build table with keys
    LOOP AT get_all_entities( ) ASSIGNING <lv_entity>.
      CLEAR: lv_fieldname, ls_component, lt_components,
             ls_entity_cont, lt_entities, lr_data.
      UNASSIGN: <lv_component>.

      lv_fieldname = <lv_entity>.

      IF <lv_entity> = cs_entities-material_txt.
        " get key structure reference of current entity
        CALL METHOD go_model->create_data_reference
          EXPORTING
            i_fieldname = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_fieldname_material
            i_struct    = if_usmd_model=>gc_struct_key_langu
            if_table    = abap_false
          IMPORTING
            er_data     = lr_data.
      ELSE.
        " get key structure reference of current entity
        CALL METHOD go_model->create_data_reference
          EXPORTING
            i_fieldname = lv_fieldname
            i_struct    = if_usmd_model=>gc_struct_key
            if_table    = abap_false
          IMPORTING
            er_data     = lr_data.
      ENDIF.

      lo_structdescr ?= cl_abap_typedescr=>describe_by_data_ref( p_data_ref = lr_data ).
      lt_components = lo_structdescr->components.

      " write all key entities of current entity into entity list
      LOOP AT lt_components INTO ls_component. "#EC CI_NESTED
        ASSIGN COMPONENT 'NAME' OF STRUCTURE ls_component TO <lv_component>.
        IF <lv_component> IS ASSIGNED.
          APPEND <lv_component> TO lt_entities.
        ENDIF.
      ENDLOOP.

      " build entity key table
      ls_entity_cont-usmd_entity = <lv_entity>.
      APPEND LINES OF lt_entities TO ls_entity_cont-t_entity_key.
      INSERT ls_entity_cont INTO TABLE gt_entity_keys.
    ENDLOOP.

  ENDMETHOD.


  METHOD init_model.

    CALL METHOD cl_usmd_model_ext=>get_instance
      EXPORTING
        i_usmd_model = zcl_mdg_mm_helper=>if_mdg_bs_mat_gen_c~gc_model_mm
      IMPORTING
        eo_instance  = go_model.

* material change management
    CREATE OBJECT go_matchgmng_api TYPE cl_cmd_bs_mat_chgmng_api.

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


  METHOD set_bscdattxt.

    FIELD-SYMBOLS:
      <ls_bscdattxt> TYPE /mdgmm/_s_mm_pp_bscdattxt.

    LOOP AT it_bscdattxt ASSIGNING <ls_bscdattxt>.
      READ TABLE gt_bscdattxt FROM <ls_bscdattxt> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_bscdattxt FROM <ls_bscdattxt>.
      ELSE.
        INSERT <ls_bscdattxt> INTO TABLE gt_bscdattxt.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_bscdattxt
            is_record = <ls_bscdattxt>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_classasgn.

    FIELD-SYMBOLS:
      <ls_classasgn> TYPE /mdgmm/_s_mm_pp_classasgn.

    LOOP AT it_classasgn ASSIGNING <ls_classasgn>.
      READ TABLE gt_classasgn FROM <ls_classasgn> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        IF <ls_classasgn>-lkenz_cla EQ abap_true.
          DELETE TABLE gt_classasgn FROM <ls_classasgn>.
        ELSE.
          MODIFY TABLE gt_classasgn FROM <ls_classasgn>.
        ENDIF.
      ELSE.
        INSERT <ls_classasgn> INTO TABLE gt_classasgn.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_classasgn
            is_record = <ls_classasgn>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_dradbasic.

    FIELD-SYMBOLS:
      <ls_dradbasic> TYPE /mdgmm/_s_mm_pp_dradbasic.

    LOOP AT it_dradbasic ASSIGNING <ls_dradbasic>.
      READ TABLE gt_dradbasic FROM <ls_dradbasic> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_dradbasic FROM <ls_dradbasic>.
      ELSE.
        INSERT <ls_dradbasic> INTO TABLE gt_dradbasic.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = zcl_mdg_mm_helper=>cs_entities-dradbasic
            is_record = <ls_dradbasic>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_dradtxt.

    FIELD-SYMBOLS:
      <ls_dradtxt> TYPE /mdgmm/_s_mm_pp_dradtxt.

    LOOP AT it_dradtxt ASSIGNING <ls_dradtxt>.
      READ TABLE gt_dradtxt FROM <ls_dradtxt> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_dradtxt FROM <ls_dradtxt>.
      ELSE.
        INSERT <ls_dradtxt> INTO TABLE gt_dradtxt.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = zcl_mdg_mm_helper=>cs_entities-dradtxt
            is_record = <ls_dradtxt>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_intcmnt.

    FIELD-SYMBOLS:
      <ls_intcmnt> TYPE /mdgmm/_s_mm_pp_intcmnt.

    LOOP AT it_intcmnt ASSIGNING <ls_intcmnt>.
      READ TABLE gt_intcmnt FROM <ls_intcmnt> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_intcmnt FROM <ls_intcmnt>.
      ELSE.
        INSERT <ls_intcmnt> INTO TABLE gt_intcmnt.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_intcmnt
            is_record = <ls_intcmnt>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marapurch.

    FIELD-SYMBOLS:
      <ls_marapurch> TYPE /mdgmm/_s_mm_pp_marapurch.

    LOOP AT it_marapurch ASSIGNING <ls_marapurch>.
      READ TABLE gt_marapurch FROM <ls_marapurch> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marapurch FROM <ls_marapurch>.
      ELSE.
        INSERT <ls_marapurch> INTO TABLE gt_marapurch.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_marapurch
            is_record = <ls_marapurch>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_maraqtmng.

    FIELD-SYMBOLS:
      <ls_maraqtmng> TYPE /mdgmm/_s_mm_pp_maraqtmng.

    LOOP AT it_maraqtmng ASSIGNING <ls_maraqtmng>.
      READ TABLE gt_maraqtmng FROM <ls_maraqtmng> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_maraqtmng FROM <ls_maraqtmng>.
      ELSE.
        INSERT <ls_maraqtmng> INTO TABLE gt_maraqtmng.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = zcl_mdg_mm_helper=>cs_entities-maraqtmng
            is_record = <ls_maraqtmng>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marasales.

    FIELD-SYMBOLS:
      <ls_marasales> TYPE /mdgmm/_s_mm_pp_marasales.

    LOOP AT it_marasales ASSIGNING <ls_marasales>.
      READ TABLE gt_marasales FROM <ls_marasales> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marasales FROM <ls_marasales>.
      ELSE.
        INSERT <ls_marasales> INTO TABLE gt_marasales.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_marasales
            is_record = <ls_marasales>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_maraspm.

    FIELD-SYMBOLS:
      <ls_maraspm> TYPE /mdgmm/_s_mm_pp_maraspm.

    LOOP AT it_maraspm ASSIGNING <ls_maraspm>.
      READ TABLE gt_maraspm FROM <ls_maraspm> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_maraspm FROM <ls_maraspm>.
      ELSE.
        INSERT <ls_maraspm> INTO TABLE gt_maraspm.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = zcl_mdg_mm_helper=>cs_entities-maraspm
            is_record = <ls_maraspm>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marastor.

    FIELD-SYMBOLS:
      <ls_marastor> TYPE /mdgmm/_s_mm_pp_marastor.

    LOOP AT it_marastor ASSIGNING <ls_marastor>.
      READ TABLE gt_marastor FROM <ls_marastor> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marastor FROM <ls_marastor>.
      ELSE.
        INSERT <ls_marastor> INTO TABLE gt_marastor.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = zcl_mdg_mm_helper=>cs_entities-marastor
            is_record = <ls_marastor>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marcatp.

    FIELD-SYMBOLS:
      <ls_marcatp> TYPE /mdgmm/_s_mm_pp_marcatp.

    LOOP AT it_marcatp ASSIGNING <ls_marcatp>.
      READ TABLE gt_marcatp FROM <ls_marcatp> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marcatp FROM <ls_marcatp>.
      ELSE.
        INSERT <ls_marcatp> INTO TABLE gt_marcatp.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_marcatp
            is_record = <ls_marcatp>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marcbasic.

    FIELD-SYMBOLS:
      <ls_marcbasic> TYPE /mdgmm/_s_mm_pp_marcbasic.

    LOOP AT it_marcbasic ASSIGNING <ls_marcbasic>.
      READ TABLE gt_marcbasic FROM <ls_marcbasic> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marcbasic FROM <ls_marcbasic>.
      ELSE.
        INSERT <ls_marcbasic> INTO TABLE gt_marcbasic.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_marcbasic
            is_record = <ls_marcbasic>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marccstng.

    FIELD-SYMBOLS:
      <ls_marccstng> TYPE /mdgmm/_s_mm_pp_marccstng.

    LOOP AT it_marccstng ASSIGNING <ls_marccstng>.
      READ TABLE gt_marccstng FROM <ls_marccstng> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marccstng FROM <ls_marccstng>.
      ELSE.
        INSERT <ls_marccstng> INTO TABLE gt_marccstng.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_marccstng
            is_record = <ls_marccstng>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marcfrcst.

    FIELD-SYMBOLS:
      <ls_marcfrcst> TYPE /mdgmm/_s_mm_pp_marcfrcst.

    LOOP AT it_marcfrcst ASSIGNING <ls_marcfrcst>.
      READ TABLE gt_marcfrcst FROM <ls_marcfrcst> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marcfrcst FROM <ls_marcfrcst>.
      ELSE.
        INSERT <ls_marcfrcst> INTO TABLE gt_marcfrcst.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_marcfrcst
            is_record = <ls_marcfrcst>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marcfrgtr.

    FIELD-SYMBOLS:
      <ls_marcfrgtr> TYPE /mdgmm/_s_mm_pp_marcfrgtr.

    LOOP AT it_marcfrgtr ASSIGNING <ls_marcfrgtr>.
      READ TABLE gt_marcfrgtr FROM <ls_marcfrgtr> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marcfrgtr FROM <ls_marcfrgtr>.
      ELSE.
        INSERT <ls_marcfrgtr> INTO TABLE gt_marcfrgtr.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_marcfrgtr
            is_record = <ls_marcfrgtr>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marcfrpar.

    FIELD-SYMBOLS:
      <ls_marcfrpar> TYPE /mdgmm/_s_mm_pp_marcfrpar.

    LOOP AT it_marcfrpar ASSIGNING <ls_marcfrpar>.
      READ TABLE gt_marcfrpar FROM <ls_marcfrpar> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marcfrpar FROM <ls_marcfrpar>.
      ELSE.
        INSERT <ls_marcfrpar> INTO TABLE gt_marcfrpar.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_marcfrpar
            is_record = <ls_marcfrpar>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marcmrpfc.

    FIELD-SYMBOLS:
      <ls_marcmrpfc> TYPE /mdgmm/_s_mm_pp_marcmrpfc.

    LOOP AT it_marcmrpfc ASSIGNING <ls_marcmrpfc>.
      READ TABLE gt_marcmrpfc FROM <ls_marcmrpfc> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marcmrpfc FROM <ls_marcmrpfc>.
      ELSE.
        INSERT <ls_marcmrpfc> INTO TABLE gt_marcmrpfc.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_marcmrpfc
            is_record = <ls_marcmrpfc>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marcmrpls.

    FIELD-SYMBOLS:
      <ls_marcmrpls> TYPE /mdgmm/_s_mm_pp_marcmrpls.

    LOOP AT it_marcmrpls ASSIGNING <ls_marcmrpls>.
      READ TABLE gt_marcmrpls FROM <ls_marcmrpls> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marcmrpls FROM <ls_marcmrpls>.
      ELSE.
        INSERT <ls_marcmrpls> INTO TABLE gt_marcmrpls.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_marcmrpls
            is_record = <ls_marcmrpls>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marcmrpmi.

    FIELD-SYMBOLS:
      <ls_marcmrpmi> TYPE /mdgmm/_s_mm_pp_marcmrpmi.

    LOOP AT it_marcmrpmi ASSIGNING <ls_marcmrpmi>.
      READ TABLE gt_marcmrpmi FROM <ls_marcmrpmi> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marcmrpmi FROM <ls_marcmrpmi>.
      ELSE.
        INSERT <ls_marcmrpmi> INTO TABLE gt_marcmrpmi.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_marcmrpmi
            is_record = <ls_marcmrpmi>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marcmrppp.

    FIELD-SYMBOLS:
      <ls_marcmrppp> TYPE /mdgmm/_s_mm_pp_marcmrppp.

    LOOP AT it_marcmrppp ASSIGNING <ls_marcmrppp>.
      READ TABLE gt_marcmrppp FROM <ls_marcmrppp> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marcmrppp FROM <ls_marcmrppp>.
      ELSE.
        INSERT <ls_marcmrppp> INTO TABLE gt_marcmrppp.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_marcmrppp
            is_record = <ls_marcmrppp>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marcmrpsp.

    FIELD-SYMBOLS:
      <ls_marcmrpsp> TYPE /mdgmm/_s_mm_pp_marcmrpsp.

    LOOP AT it_marcmrpsp ASSIGNING <ls_marcmrpsp>.
      READ TABLE gt_marcmrpsp FROM <ls_marcmrpsp> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marcmrpsp FROM <ls_marcmrpsp>.
      ELSE.
        INSERT <ls_marcmrpsp> INTO TABLE gt_marcmrpsp.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_marcmrpsp
            is_record = <ls_marcmrpsp>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marcprt.

    FIELD-SYMBOLS:
      <ls_marcprt> TYPE /mdgmm/_s_mm_pp_marcprt.

    LOOP AT it_marcprt ASSIGNING <ls_marcprt>.
      READ TABLE gt_marcprt FROM <ls_marcprt> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marcprt FROM <ls_marcprt>.
      ELSE.
        INSERT <ls_marcprt> INTO TABLE gt_marcprt.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_marcprt
            is_record = <ls_marcprt>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marcpurch.

    FIELD-SYMBOLS:
      <ls_marcpurch> TYPE /mdgmm/_s_mm_pp_marcpurch.

    LOOP AT it_marcpurch ASSIGNING <ls_marcpurch>.
      READ TABLE gt_marcpurch FROM <ls_marcpurch> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marcpurch FROM <ls_marcpurch>.
      ELSE.
        INSERT <ls_marcpurch> INTO TABLE gt_marcpurch.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = zcl_mdg_mm_helper=>cs_entities-marcpurch
            is_record = <ls_marcpurch>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marcqtmng.

    FIELD-SYMBOLS:
      <ls_marcqtmng> TYPE /mdgmm/_s_mm_pp_marcqtmng.

    LOOP AT it_marcqtmng ASSIGNING <ls_marcqtmng>.
      READ TABLE gt_marcqtmng FROM <ls_marcqtmng> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marcqtmng FROM <ls_marcqtmng>.
      ELSE.
        INSERT <ls_marcqtmng> INTO TABLE gt_marcqtmng.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_marcqtmng
            is_record = <ls_marcqtmng>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marcsales.

    FIELD-SYMBOLS:
      <ls_marcsales> TYPE /mdgmm/_s_mm_pp_marcsales.

    LOOP AT it_marcsales ASSIGNING <ls_marcsales>.
      READ TABLE gt_marcsales FROM <ls_marcsales> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marcsales FROM <ls_marcsales>.
      ELSE.
        INSERT <ls_marcsales> INTO TABLE gt_marcsales.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_marcsales
            is_record = <ls_marcsales>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marcstore.

    FIELD-SYMBOLS:
      <ls_marcstore> TYPE /mdgmm/_s_mm_pp_marcstore.

    LOOP AT it_marcstore ASSIGNING <ls_marcstore>.
      READ TABLE gt_marcstore FROM <ls_marcstore> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marcstore FROM <ls_marcstore>.
      ELSE.
        INSERT <ls_marcstore> INTO TABLE gt_marcstore.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = zcl_mdg_mm_helper=>cs_entities-marcstore
            is_record = <ls_marcstore>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_marcwrksd.

    FIELD-SYMBOLS:
      <ls_marcwrksd> TYPE /mdgmm/_s_mm_pp_marcwrksd.

    LOOP AT it_marcwrksd ASSIGNING <ls_marcwrksd>.
      READ TABLE gt_marcwrksd FROM <ls_marcwrksd> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_marcwrksd FROM <ls_marcwrksd>.
      ELSE.
        INSERT <ls_marcwrksd> INTO TABLE gt_marcwrksd.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_marcwrksd
            is_record = <ls_marcwrksd>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mardmrp.

    FIELD-SYMBOLS:
      <ls_mardmrp> TYPE /mdgmm/_s_mm_pp_mardmrp.

    LOOP AT it_mardmrp ASSIGNING <ls_mardmrp>.
      READ TABLE gt_mardmrp FROM <ls_mardmrp> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mardmrp FROM <ls_mardmrp>.
      ELSE.
        INSERT <ls_mardmrp> INTO TABLE gt_mardmrp.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_mardmrp
            is_record = <ls_mardmrp>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mardstor.

    FIELD-SYMBOLS:
      <ls_mardstor> TYPE /mdgmm/_s_mm_pp_mardstor.

    LOOP AT it_mardstor ASSIGNING <ls_mardstor>.
      READ TABLE gt_mardstor FROM <ls_mardstor> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mardstor FROM <ls_mardstor>.
      ELSE.
        INSERT <ls_mardstor> INTO TABLE gt_mardstor.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_mardstor
            is_record = <ls_mardstor>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_matchgmng.

    FIELD-SYMBOLS:
      <ls_matchgmng> TYPE /mdgmm/_s_mm_pp_matchgmng.

    LOOP AT it_matchgmng ASSIGNING <ls_matchgmng>.
      READ TABLE gt_matchgmng FROM <ls_matchgmng> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_matchgmng FROM <ls_matchgmng>.
      ELSE.
        INSERT <ls_matchgmng> INTO TABLE gt_matchgmng.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = zcl_mdg_mm_helper=>cs_entities-matchgmng
            is_record = <ls_matchgmng>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_material.

    FIELD-SYMBOLS:
      <ls_material> TYPE /mdgmm/_s_mm_pp_material.

    LOOP AT it_material ASSIGNING <ls_material>.
      READ TABLE gt_material FROM <ls_material> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_material FROM <ls_material>.
      ELSE.
        INSERT <ls_material> INTO TABLE gt_material.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_material
            is_record = <ls_material>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mattxt.

    FIELD-SYMBOLS:
      <ls_mattxt> TYPE /mdgmm/_st_mm_pp_material.

    LOOP AT it_mattxt ASSIGNING <ls_mattxt>.
      READ TABLE gt_mattxt FROM <ls_mattxt> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mattxt FROM <ls_mattxt>.
      ELSE.
        INSERT <ls_mattxt> INTO TABLE gt_mattxt.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = zcl_mdg_mm_helper=>cs_entities-material_txt
            is_record = <ls_mattxt>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mbewactng.

    FIELD-SYMBOLS:
      <ls_mbewactng> TYPE /mdgmm/_s_mm_pp_mbewactng.

    LOOP AT it_mbewactng ASSIGNING <ls_mbewactng>.
      READ TABLE gt_mbewactng FROM <ls_mbewactng> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mbewactng FROM <ls_mbewactng>.
      ELSE.
        INSERT <ls_mbewactng> INTO TABLE gt_mbewactng.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_mbewactng
            is_record = <ls_mbewactng>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mbewcstng.

    FIELD-SYMBOLS:
      <ls_mbewcstng> TYPE /mdgmm/_s_mm_pp_mbewcstng.

    LOOP AT it_mbewcstng ASSIGNING <ls_mbewcstng>.
      READ TABLE gt_mbewcstng FROM <ls_mbewcstng> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mbewcstng FROM <ls_mbewcstng>.
      ELSE.
        INSERT <ls_mbewcstng> INTO TABLE gt_mbewcstng.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_mbewcstng
            is_record = <ls_mbewcstng>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mbewmlac.

    FIELD-SYMBOLS:
      <ls_mbewmlac> TYPE /mdgmm/_s_mm_pp_mbewmlac.

    LOOP AT it_mbewmlac ASSIGNING <ls_mbewmlac>.
      READ TABLE gt_mbewmlac FROM <ls_mbewmlac> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mbewmlac FROM <ls_mbewmlac>.
      ELSE.
        INSERT <ls_mbewmlac> INTO TABLE gt_mbewmlac.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_mbewmlac
            is_record = <ls_mbewmlac>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mbewmlval.

    FIELD-SYMBOLS:
      <ls_mbewmlval> TYPE /mdgmm/_s_mm_pp_mbewmlval.

    LOOP AT it_mbewmlval ASSIGNING <ls_mbewmlval>.
      READ TABLE gt_mbewmlval FROM <ls_mbewmlval> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mbewmlval FROM <ls_mbewmlval>.
      ELSE.
        INSERT <ls_mbewmlval> INTO TABLE gt_mbewmlval.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_mbewmlval
            is_record = <ls_mbewmlval>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mbewvalua.

    FIELD-SYMBOLS:
      <ls_mbewvalua> TYPE /mdgmm/_s_mm_pp_mbewvalua.

    LOOP AT it_mbewvalua ASSIGNING <ls_mbewvalua>.
      READ TABLE gt_mbewvalua FROM <ls_mbewvalua> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mbewvalua FROM <ls_mbewvalua>.
      ELSE.
        INSERT <ls_mbewvalua> INTO TABLE gt_mbewvalua.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_mbewvalua
            is_record = <ls_mbewvalua>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mdmabasic.

    FIELD-SYMBOLS:
      <ls_mdmabasic> TYPE /mdgmm/_s_mm_pp_mdmabasic.

    LOOP AT it_mdmabasic ASSIGNING <ls_mdmabasic>.
      READ TABLE gt_mdmabasic FROM <ls_mdmabasic> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mdmabasic FROM <ls_mdmabasic>.
      ELSE.
        INSERT <ls_mdmabasic> INTO TABLE gt_mdmabasic.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_mdmabasic
            is_record = <ls_mdmabasic>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mean_gtin.

    FIELD-SYMBOLS:
      <ls_mean_gtin> TYPE /mdgmm/_s_mm_pp_mean_gtin.

    LOOP AT it_mean_gtin ASSIGNING <ls_mean_gtin>.
      READ TABLE gt_mean_gtin FROM <ls_mean_gtin> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mean_gtin FROM <ls_mean_gtin>.
      ELSE.
        INSERT <ls_mean_gtin> INTO TABLE gt_mean_gtin.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_mean_gtin
            is_record = <ls_mean_gtin>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mkalbasic.

    FIELD-SYMBOLS:
      <ls_mkalbasic> TYPE /mdgmm/_s_mm_pp_mkalbasic.

    LOOP AT it_mkalbasic ASSIGNING <ls_mkalbasic>.
      READ TABLE gt_mkalbasic FROM <ls_mkalbasic> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mkalbasic FROM <ls_mkalbasic>.
      ELSE.
        INSERT <ls_mkalbasic> INTO TABLE gt_mkalbasic.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_mkalbasic
            is_record = <ls_mkalbasic>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mlanpurch.

    FIELD-SYMBOLS:
      <ls_mlanpurch> TYPE /mdgmm/_s_mm_pp_mlanpurch.

    LOOP AT it_mlanpurch ASSIGNING <ls_mlanpurch>.
      READ TABLE gt_mlanpurch FROM <ls_mlanpurch> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mlanpurch FROM <ls_mlanpurch>.
      ELSE.
        INSERT <ls_mlanpurch> INTO TABLE gt_mlanpurch.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_mlanpurch
            is_record = <ls_mlanpurch>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mlansales.

    FIELD-SYMBOLS:
      <ls_mlansales> TYPE /mdgmm/_s_mm_pp_mlansales.

    LOOP AT it_mlansales ASSIGNING <ls_mlansales>.
      READ TABLE gt_mlansales FROM <ls_mlansales> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mlansales FROM <ls_mlansales>.
      ELSE.
        INSERT <ls_mlansales> INTO TABLE gt_mlansales.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_mlansales
            is_record = <ls_mlansales>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mlgnstor.

    FIELD-SYMBOLS:
      <ls_mlgnstor> TYPE /mdgmm/_s_mm_pp_mlgnstor.

    LOOP AT it_mlgnstor ASSIGNING <ls_mlgnstor>.
      READ TABLE gt_mlgnstor FROM <ls_mlgnstor> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mlgnstor FROM <ls_mlgnstor>.
      ELSE.
        INSERT <ls_mlgnstor> INTO TABLE gt_mlgnstor.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_mlgnstor
            is_record = <ls_mlgnstor>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mlgtstor.

    FIELD-SYMBOLS:
      <ls_mlgtstor> TYPE /mdgmm/_s_mm_pp_mlgtstor.

    LOOP AT it_mlgtstor ASSIGNING <ls_mlgtstor>.
      READ TABLE gt_mlgtstor FROM <ls_mlgtstor> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mlgtstor FROM <ls_mlgtstor>.
      ELSE.
        INSERT <ls_mlgtstor> INTO TABLE gt_mlgtstor.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_mlgtstor
            is_record = <ls_mlgtstor>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mpgdprodg.

    FIELD-SYMBOLS:
      <ls_mpgdprodg> TYPE /mdgmm/_s_mm_pp_mpgdprodg.

    LOOP AT it_mpgdprodg ASSIGNING <ls_mpgdprodg>.
      READ TABLE gt_mpgdprodg FROM <ls_mpgdprodg> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mpgdprodg FROM <ls_mpgdprodg>.
      ELSE.
        INSERT <ls_mpgdprodg> INTO TABLE gt_mpgdprodg.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_mpgdprodg
            is_record = <ls_mpgdprodg>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mrptxt.

    FIELD-SYMBOLS:
      <ls_mrptxt> TYPE /mdgmm/_s_mm_pp_mrptxt.

    LOOP AT it_mrptxt ASSIGNING <ls_mrptxt>.
      READ TABLE gt_mrptxt FROM <ls_mrptxt> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mrptxt FROM <ls_mrptxt>.
      ELSE.
        INSERT <ls_mrptxt> INTO TABLE gt_mrptxt.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_mrptxt
            is_record = <ls_mrptxt>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mvkegrpng.

    FIELD-SYMBOLS:
      <ls_mvkegrpng> TYPE /mdgmm/_s_mm_pp_mvkegrpng.

    LOOP AT it_mvkegrpng ASSIGNING <ls_mvkegrpng>.
      READ TABLE gt_mvkegrpng FROM <ls_mvkegrpng> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mvkegrpng FROM <ls_mvkegrpng>.
      ELSE.
        INSERT <ls_mvkegrpng> INTO TABLE gt_mvkegrpng.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_mvkegrpng
            is_record = <ls_mvkegrpng>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_mvkesales.

    FIELD-SYMBOLS:
      <ls_mvkesales> TYPE /mdgmm/_s_mm_pp_mvkesales.

    LOOP AT it_mvkesales ASSIGNING <ls_mvkesales>.
      READ TABLE gt_mvkesales FROM <ls_mvkesales> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_mvkesales FROM <ls_mvkesales>.
      ELSE.
        INSERT <ls_mvkesales> INTO TABLE gt_mvkesales.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_mvkesales
            is_record = <ls_mvkesales>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_purchtxt.

    FIELD-SYMBOLS:
      <ls_purchtxt> TYPE /mdgmm/_s_mm_pp_purchtxt.

    LOOP AT it_purchtxt ASSIGNING <ls_purchtxt>.
      READ TABLE gt_purchtxt FROM <ls_purchtxt> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_purchtxt FROM <ls_purchtxt>.
      ELSE.
        INSERT <ls_purchtxt> INTO TABLE gt_purchtxt.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_purchtxt
            is_record = <ls_purchtxt>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_qinsptxt.

    FIELD-SYMBOLS:
      <ls_qinsptxt> TYPE /mdgmm/_s_mm_pp_qinsptxt.

    LOOP AT it_qinsptxt ASSIGNING <ls_qinsptxt>.
      READ TABLE gt_qinsptxt FROM <ls_qinsptxt> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_qinsptxt FROM <ls_qinsptxt>.
      ELSE.
        INSERT <ls_qinsptxt> INTO TABLE gt_qinsptxt.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_qinsptxt
            is_record = <ls_qinsptxt>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_qmatbasic.

    FIELD-SYMBOLS:
      <ls_qmatbasic> TYPE /mdgmm/_s_mm_pp_qmatbasic.

    LOOP AT it_qmatbasic ASSIGNING <ls_qmatbasic>.
      READ TABLE gt_qmatbasic FROM <ls_qmatbasic> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_qmatbasic FROM <ls_qmatbasic>.
      ELSE.
        INSERT <ls_qmatbasic> INTO TABLE gt_qmatbasic.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_qmatbasic
            is_record = <ls_qmatbasic>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_salestxt.

    FIELD-SYMBOLS:
      <ls_salestxt> TYPE /mdgmm/_s_mm_pp_salestxt.

    LOOP AT it_salestxt ASSIGNING <ls_salestxt>.
      READ TABLE gt_salestxt FROM <ls_salestxt> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_salestxt FROM <ls_salestxt>.
      ELSE.
        INSERT <ls_salestxt> INTO TABLE gt_salestxt.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_salestxt
            is_record = <ls_salestxt>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_unitofmsr.

    FIELD-SYMBOLS:
      <ls_unitofmsr> TYPE /mdgmm/_s_mm_pp_unitofmsr.

    LOOP AT it_unitofmsr ASSIGNING <ls_unitofmsr>.
      READ TABLE gt_unitofmsr FROM <ls_unitofmsr> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        MODIFY TABLE gt_unitofmsr FROM <ls_unitofmsr>.
      ELSE.
        INSERT <ls_unitofmsr> INTO TABLE gt_unitofmsr.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_unitofmsr
            is_record = <ls_unitofmsr>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD set_valuation.

    FIELD-SYMBOLS:
      <ls_valuation> TYPE /mdgmm/_s_mm_pp_valuation.

    LOOP AT it_valuation ASSIGNING <ls_valuation>.
      READ TABLE gt_valuation FROM <ls_valuation> TRANSPORTING NO FIELDS.
      IF sy-subrc = 0.
        IF <ls_valuation>-lkenz_val EQ abap_true.
          DELETE TABLE gt_valuation FROM <ls_valuation>.
        ELSE.
          MODIFY TABLE gt_valuation FROM <ls_valuation>.
        ENDIF.
      ELSE.
        INSERT <ls_valuation> INTO TABLE gt_valuation.

        CALL METHOD create_dependent_entities
          EXPORTING
            iv_entity = if_mdg_bs_mat_gen_c~gc_entity_valuation
            is_record = <ls_valuation>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.
ENDCLASS.