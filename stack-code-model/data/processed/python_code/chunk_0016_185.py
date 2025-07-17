INTERFACE zif_mdg_mm_datatypes
  PUBLIC .


  TYPES:
    gty_t_material  TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_material  WITH UNIQUE KEY material .
  TYPES:
    gty_t_valuation TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_valuation WITH UNIQUE KEY material changeno charid classtype ecocntr guid valcnt .
  TYPES:
    gty_t_unitofmsr TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_unitofmsr WITH UNIQUE KEY material qteunit .
  TYPES:
    gty_t_salestxt  TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_salestxt  WITH UNIQUE KEY material langucode vkorg vtweg .
  TYPES:
    gty_t_qmatbasic TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_qmatbasic WITH UNIQUE KEY material art werks .
  TYPES:
    gty_t_qinsptxt  TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_qinsptxt  WITH UNIQUE KEY material langucode .
  TYPES:
    gty_t_purchtxt  TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_purchtxt  WITH UNIQUE KEY material langucode .
  TYPES:
    gty_t_mvkesales TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_mvkesales WITH UNIQUE KEY material vkorg vtweg .
  TYPES:
    gty_t_mvkegrpng TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_mvkegrpng WITH UNIQUE KEY material vkorg vtweg .
  TYPES:
    gty_t_mrptxt    TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_mrptxt  WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_mpgdprodg TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_mpgdprodg WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_mlgtstor  TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_mlgtstor  WITH UNIQUE KEY material lgnum lgtyp .
  TYPES:
    gty_t_mlgnstor  TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_mlgnstor  WITH UNIQUE KEY material lgnum .
  TYPES:
    gty_t_mlansales TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_mlansales WITH UNIQUE KEY material aland tatyp .
  TYPES:
    gty_t_mlanpurch TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_mlanpurch WITH UNIQUE KEY material aland .
  TYPES:
    gty_t_mean_gtin TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_mean_gtin WITH UNIQUE KEY material ean qteunit .
  TYPES:
  gty_t_marcprt TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marcprt WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_mdmabasic TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_mdmabasic WITH UNIQUE KEY material berid werks .
  TYPES:
    gty_t_mbewvalua TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_mbewvalua WITH UNIQUE KEY material bwkey bwtar .
  TYPES:
    gty_t_mbewcstng TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_mbewcstng WITH UNIQUE KEY material bwkey .
  TYPES:
    gty_t_mardstor  TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_mardstor  WITH UNIQUE KEY material lgort werks .
  TYPES:
    gty_t_mardmrp   TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_mardmrp WITH UNIQUE KEY material lgort werks .
  TYPES:
    gty_t_marcwrksd TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marcwrksd WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_marcstore TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marcstore WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_marcsales TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marcsales WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_marcqtmng TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marcqtmng WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_marcpurch TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marcpurch WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_marcmrpsp TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marcmrpsp WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_marcmrppp TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marcmrppp WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_marcmrpmi TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marcmrpmi WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_marcmrpls TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marcmrpls WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_marcmrpfc TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marcmrpfc WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_marcfrpar TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marcfrpar WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_marcfrgtr TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marcfrgtr WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_marcfrcst TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marcfrcst WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_marccstng TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marccstng WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_marcbasic TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marcbasic WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_marcatp   TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marcatp WITH UNIQUE KEY material werks .
  TYPES:
    gty_t_marastor  TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marastor  WITH UNIQUE KEY material .
  TYPES:
    gty_t_maraspm   TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_maraspm WITH UNIQUE KEY material .
  TYPES:
    gty_t_marasales TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marasales WITH UNIQUE KEY material .
  TYPES:
    gty_t_maraqtmng TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_maraqtmng WITH UNIQUE KEY material .
  TYPES:
    gty_t_marapurch TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_marapurch WITH UNIQUE KEY material .
  TYPES:
    gty_t_intcmnt   TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_intcmnt WITH UNIQUE KEY material langucode .
  TYPES:
    gty_t_classasgn TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_classasgn WITH UNIQUE KEY material changeno class classtype ecocntr guid .
  TYPES:
    gty_t_bscdattxt TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_bscdattxt WITH UNIQUE KEY material langucode .
  TYPES:
    gty_t_mkalbasic TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_mkalbasic WITH UNIQUE KEY mkalbasic material werks .
  TYPES:
    gty_t_matchgmng TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_matchgmng WITH UNIQUE KEY material matchgmng  .
  TYPES:
    gty_t_dradbasic TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_dradbasic WITH UNIQUE KEY dokar doknr doktl dokvr material .
  TYPES:
    gty_t_dradtxt   TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_dradtxt WITH UNIQUE KEY dokar doknr doktl dokvr material langucode .
  TYPES:
    gty_t_mattxt    TYPE SORTED TABLE OF  /mdgmm/_st_mm_pp_material WITH UNIQUE KEY material langu .
  TYPES:
    gty_t_mbewactng TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_mbewactng WITH UNIQUE KEY bwkey bwtar material .
  TYPES:
    gty_t_mbewmlac  TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_mbewmlac WITH UNIQUE KEY bwkey bwtar material curtp .
  TYPES:
    gty_t_mbewmlval TYPE SORTED TABLE OF  /mdgmm/_s_mm_pp_mbewmlval WITH UNIQUE KEY bwkey bwtar material curtp .
  TYPES:
    BEGIN OF gty_s_mm_where,
      material TYPE matnr,
      where    TYPE comt_clear_string,
    END OF gty_s_mm_where .
  TYPES:
    gty_t_mm_where TYPE SORTED TABLE OF gty_s_mm_where WITH NON-UNIQUE KEY material .
  TYPES:
    gty_t_mm_field_prop TYPE STANDARD TABLE OF zmdg_t_mm_fprop WITH NON-UNIQUE KEY mandt
                                                                                   cr_type
                                                                                   cr_step
                                                                                   mtart
                                                                                   entity
                                                                                   fieldname .
  TYPES:
    gty_t_mm_entity_prop TYPE STANDARD TABLE OF zmdg_t_mm_eprop WITH NON-UNIQUE KEY mandt
                                                                                    cr_type
                                                                                    cr_step
                                                                                    mtart
                                                                                    entity .
  TYPES:
    BEGIN OF gty_s_mm_entity_prop_by_mat,
      material    TYPE matnr,
      entity_prop TYPE gty_t_mm_entity_prop,
    END OF gty_s_mm_entity_prop_by_mat .
  TYPES:
    gty_t_mm_entity_prop_by_mat TYPE SORTED TABLE OF gty_s_mm_entity_prop_by_mat WITH NON-UNIQUE KEY material .
  TYPES: BEGIN OF gty_s_mm_message,
           material   TYPE matnr,
           key_fields TYPE cl_mdg_bs_mat_assist_ui=>ty_s_key_fields.
           INCLUDE TYPE usmd_s_message.
  TYPES: END OF gty_s_mm_message .

  TYPES:
    gty_t_mm_message TYPE STANDARD TABLE OF gty_s_mm_message .
  TYPES:
    gty_t_mm_rules TYPE STANDARD TABLE OF ZMDG_T_MM_RULES .


  TYPES:
    BEGIN OF gty_s_mdg_mm_attrinfo,
      mm_attrinfo  TYPE mdg_bs_mat_s_attrinfo_from_fld,
      is_key_field TYPE xfeld,
    END OF gty_s_mdg_mm_attrinfo,

    gty_t_mdg_mm_attrinfo TYPE STANDARD TABLE OF gty_s_mdg_mm_attrinfo.

  CONSTANTS: BEGIN OF gc_s_entities,
               bscdattxt    TYPE usmd_entity VALUE 'BSCDATTXT',
               classasgn    TYPE usmd_entity VALUE 'CLASSASGN',
               dradbasic    TYPE usmd_entity VALUE 'DRADBASIC',
               dradtxt      TYPE usmd_entity VALUE 'DRADTXT',
               intcmnt      TYPE usmd_entity VALUE 'INTCMNT',
               marapurch    TYPE usmd_entity VALUE 'MARAPURCH',
               maraqtmng    TYPE usmd_entity VALUE 'MARAQTMNG',
               marasales    TYPE usmd_entity VALUE 'MARASALES',
               maraspm      TYPE usmd_entity VALUE 'MARASPM',
               marastor     TYPE usmd_entity VALUE 'MARASTOR',
               marcatp      TYPE usmd_entity VALUE 'MARCATP',
               marcbasic    TYPE usmd_entity VALUE 'MARCBASIC',
               marccstng    TYPE usmd_entity VALUE 'MARCCSTNG',
               marcfrcst    TYPE usmd_entity VALUE 'MARCFRCST',
               marcfrgtr    TYPE usmd_entity VALUE 'MARCFRGTR',
               marcfrpar    TYPE usmd_entity VALUE 'MARCFRPAR',
               marcmrpfc    TYPE usmd_entity VALUE 'MARCMRPFC',
               marcmrpls    TYPE usmd_entity VALUE 'MARCMRPLS',
               marcmrpmi    TYPE usmd_entity VALUE 'MARCMRPMI',
               marcmrppp    TYPE usmd_entity VALUE 'MARCMRPPP',
               marcmrpsp    TYPE usmd_entity VALUE 'MARCMRPSP',
               marcpurch    TYPE usmd_entity VALUE 'MARCPURCH',
               marcqtmng    TYPE usmd_entity VALUE 'MARCQTMNG',
               marcsales    TYPE usmd_entity VALUE 'MARCSALES',
               marcstore    TYPE usmd_entity VALUE 'MARCSTORE',
               marcwrksd    TYPE usmd_entity VALUE 'MARCWRKSD',
               mardmrp      TYPE usmd_entity VALUE 'MARDMRP',
               mardstor     TYPE usmd_entity VALUE 'MARDSTOR',
               matchgmng    TYPE usmd_entity VALUE 'MATCHGMNG',
               material     TYPE usmd_entity VALUE 'MATERIAL',
               material_txt TYPE usmd_entity VALUE 'MATTXT',
               mbewactng    TYPE usmd_entity VALUE 'MBEWACTNG',
               mbewcstng    TYPE usmd_entity VALUE 'MBEWCSTNG',
               mbewmlac     TYPE usmd_entity VALUE 'MBEWMLAC',
               mbewmlval    TYPE usmd_entity VALUE 'MBEWMLVAL',
               mbewvalua    TYPE usmd_entity VALUE 'MBEWVALUA',
               mdmabasic    TYPE usmd_entity VALUE 'MDMABASIC',
               mean_gtin    TYPE usmd_entity VALUE 'MEAN_GTIN',
               mkalbasic    TYPE usmd_entity VALUE 'MKALBASIC',
               mlanpurch    TYPE usmd_entity VALUE 'MLANPURCH',
               mlansales    TYPE usmd_entity VALUE 'MLANSALES',
               mlgnstor     TYPE usmd_entity VALUE 'MLGNSTOR',
               mlgtstor     TYPE usmd_entity VALUE 'MLGTSTOR',
               mpgdprodg    TYPE usmd_entity VALUE 'MPGDPRODG',
               mrptxt       TYPE usmd_entity VALUE 'MRPTXT',
               mvkegrpng    TYPE usmd_entity VALUE 'MVKEGRPNG',
               mvkesales    TYPE usmd_entity VALUE 'MVKESALES',
               purchtxt     TYPE usmd_entity VALUE 'PURCHTXT',
               qinsptxt     TYPE usmd_entity VALUE 'QINSPTXT',
               qmatbasic    TYPE usmd_entity VALUE 'QMATBASIC',
               salestxt     TYPE usmd_entity VALUE 'SALESTXT',
               unitofmsr    TYPE usmd_entity VALUE 'UNITOFMSR',
               valuation    TYPE usmd_entity VALUE 'VALUATION',
             END OF gc_s_entities.

  CONSTANTS: BEGIN OF gc_s_keys,
               material  TYPE usmd_entity VALUE 'MATERIAL',
               abcin     TYPE usmd_entity VALUE 'ABCIN',
               aland     TYPE usmd_entity VALUE 'ALAND',
               alortmkal TYPE usmd_entity VALUE 'ALORTMKAL',
               art       TYPE usmd_entity VALUE 'ART',
               auftl     TYPE usmd_entity VALUE 'AUFTL',
               block     TYPE usmd_entity VALUE 'BLOCK',
               bsskz     TYPE usmd_entity VALUE 'BSSKZ',
               bwkey     TYPE usmd_entity VALUE 'BWKEY',
               bwtar     TYPE usmd_entity VALUE 'BWTAR',
               changeno  TYPE usmd_entity VALUE 'CHANGENO',
               charid    TYPE usmd_entity VALUE 'CHARID',
               chgmngno  TYPE usmd_entity VALUE 'CHGMNGNO',
               class     TYPE usmd_entity VALUE 'CLASS',
               classtype TYPE usmd_entity VALUE 'CLASSTYPE',
               curtp     TYPE usmd_entity VALUE 'CURTP',
               disgr     TYPE usmd_entity VALUE 'DISGR',
               dispo     TYPE usmd_entity VALUE 'DISPO',
               dokar     TYPE usmd_entity VALUE 'DOKAR',
               dwerk     TYPE usmd_entity VALUE 'DWERK',
               ean       TYPE usmd_entity VALUE 'EAN',
               ecocntr   TYPE usmd_entity VALUE 'ECOCNTR',
               ekgrp_x   TYPE usmd_entity VALUE 'EKGRP_X',
               elpromkal TYPE usmd_entity VALUE 'ELPROMKAL',
               eprio     TYPE usmd_entity VALUE 'EPRIO',
               fevor     TYPE usmd_entity VALUE 'FEVOR',
               fhori     TYPE usmd_entity VALUE 'FHORI',
               guid      TYPE usmd_entity VALUE 'GUID',
               herkl_x   TYPE usmd_entity VALUE 'HERKL_X',
               kober     TYPE usmd_entity VALUE 'KOBER',
               lagpr     TYPE usmd_entity VALUE 'LAGPR',
               langucode TYPE usmd_entity VALUE 'LANGUCODE',
               lety1     TYPE usmd_entity VALUE 'LETY1',
               lety2     TYPE usmd_entity VALUE 'LETY2',
               lety3     TYPE usmd_entity VALUE 'LETY3',
               lfrhy     TYPE usmd_entity VALUE 'LFRHY',
               lgbkz     TYPE usmd_entity VALUE 'LGBKZ',
               lgfsb     TYPE usmd_entity VALUE 'LGFSB',
               lgnum     TYPE usmd_entity VALUE 'LGNUM',
               lgort     TYPE usmd_entity VALUE 'LGORT',
               lgpla     TYPE usmd_entity VALUE 'LGPLA',
               lgpro     TYPE usmd_entity VALUE 'LGPRO',
               lgtyp     TYPE usmd_entity VALUE 'LGTYP',
               lsobs     TYPE usmd_entity VALUE 'LSOBS',
               ltkza     TYPE usmd_entity VALUE 'LTKZA',
               ltkze     TYPE usmd_entity VALUE 'LTKZE',
               mdv02mkal TYPE usmd_entity VALUE 'MDV02MKAL',
               mrppp     TYPE usmd_entity VALUE 'MRPPP',
               perkz     TYPE usmd_entity VALUE 'PERKZ',
               plkpt     TYPE usmd_entity VALUE 'PLKPT',
               plnty_g   TYPE usmd_entity VALUE 'PLNTY_G',
               plnty_m   TYPE usmd_entity VALUE 'PLNTY_M',
               plnty_p   TYPE usmd_entity VALUE 'PLNTY_P',
               prgrp     TYPE usmd_entity VALUE 'PRGRP',
               prvbemkal TYPE usmd_entity VALUE 'PRVBEMKAL',
               prwrk     TYPE usmd_entity VALUE 'PRWRK',
               qteunit   TYPE usmd_entity VALUE 'QTEUNIT',
               revlv     TYPE usmd_entity VALUE 'REVLV',
               rwpro     TYPE usmd_entity VALUE 'RWPRO',
               sfcpf     TYPE usmd_entity VALUE 'SFCPF',
               shpro     TYPE usmd_entity VALUE 'SHPRO',
               sobsk     TYPE usmd_entity VALUE 'SOBSK',
               sobsl     TYPE usmd_entity VALUE 'SOBSL',
               taxim     TYPE usmd_entity VALUE 'TAXIM',
               valcnt    TYPE usmd_entity VALUE 'VALCNT',
               vertomkal TYPE usmd_entity VALUE 'VERTOMKAL',
               vkorg     TYPE usmd_entity VALUE 'VKORG',
               vspvb     TYPE usmd_entity VALUE 'VSPVB',
               vtweg     TYPE usmd_entity VALUE 'VTWEG',
               werks     TYPE usmd_entity VALUE 'WERKS',
             END OF gc_s_keys.

ENDINTERFACE.