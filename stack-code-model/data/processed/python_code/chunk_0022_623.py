INTERFACE zif_mdg_bp_datatypes
PUBLIC .

*  TYPES:
*    gty_t_bp_entity_prop TYPE STANDARD TABLE OF ymdg_c_bp_eprop WITH NON-UNIQUE KEY mandt
*                                                                                    cr_type
*                                                                                    cr_step
*                                                                                    bu_type
*                                                                                    bu_role
*                                                                                    bu_group
*                                                                                    ktokk
*                                                                                    ktokd
*                                                                                    entity .
*
*  TYPES:
*    BEGIN OF gty_s_bp_entity_prop_by_bp,
*      bp          TYPE bu_partner,
*      entity_prop TYPE gty_t_bp_entity_prop,
*    END OF gty_s_bp_entity_prop_by_bp .
  TYPES:
    BEGIN OF gty_s_bp_message.
  TYPES         partner TYPE bu_partner.
  INCLUDE TYPE usmd_s_message.
  TYPES         END OF gty_s_bp_message .
  TYPES:
    BEGIN OF gty_s_bp_where,
      bp    TYPE bu_partner,
      where TYPE comt_clear_string,
    END OF gty_s_bp_where .
  TYPES:
    BEGIN OF gty_s_mdg_bs_bp_fldgrp,
      bp_fldgrp    TYPE mdg_bs_bp_fldgrp,
      is_key_field TYPE xfeld,
    END OF gty_s_mdg_bs_bp_fldgrp .
  TYPES:
    gty_t_address   TYPE SORTED TABLE OF  /mdgbp/_s_bp_pp_address WITH UNIQUE KEY bp_header addrno .
  TYPES:
    gty_t_addrno    TYPE SORTED TABLE OF mdg_bs_addrno WITH UNIQUE KEY addrno .
  TYPES:
    gty_t_ad_email  TYPE SORTED TABLE OF  /mdgbp/_s_bp_pp_ad_email  WITH UNIQUE KEY bp_header addrno ad_consno .
  TYPES:
    gty_t_ad_fax    TYPE SORTED TABLE OF  /mdgbp/_s_bp_pp_ad_fax  WITH UNIQUE KEY bp_header addrno ad_consno .
  TYPES:
    gty_t_ad_name_o TYPE SORTED TABLE OF  /mdgbp/_s_bp_pp_ad_name_o WITH UNIQUE KEY bp_header addrno ad_nation .
  TYPES:
    gty_t_ad_name_p TYPE SORTED TABLE OF  /mdgbp/_s_bp_pp_ad_name_p WITH UNIQUE KEY bp_header addrno ad_nation .
  TYPES:
    gty_t_ad_postal TYPE SORTED TABLE OF  /mdgbp/_s_bp_pp_ad_postal WITH UNIQUE KEY bp_header addrno ad_nation .
  TYPES:
    gty_t_ad_tel    TYPE SORTED TABLE OF  /mdgbp/_s_bp_pp_ad_tel  WITH UNIQUE KEY bp_header addrno ad_consno .
  TYPES:
    gty_t_ad_url    TYPE SORTED TABLE OF  /mdgbp/_s_bp_pp_ad_url  WITH UNIQUE KEY bp_header addrno ad_consno .
  TYPES:
    gty_t_bp_addr   TYPE SORTED TABLE OF  /mdgbp/_s_bp_pp_bp_addr WITH UNIQUE KEY bp_header addrno .
  TYPES:
    gty_t_bp_addusg TYPE SORTED TABLE OF  /mdgbp/_s_bp_pp_bp_addusg WITH UNIQUE KEY addrno bp_header bp_adrknd .
  TYPES:
    gty_t_bp_bkdtl  TYPE SORTED TABLE OF  /mdgbp/_s_bp_pp_bp_bkdtl  WITH UNIQUE KEY bp_header bank_id .
  TYPES:
    gty_t_bp_ccdtl  TYPE SORTED TABLE OF  /mdgbp/_s_bp_pp_bp_ccdtl  WITH UNIQUE KEY bp_header card_id .
  TYPES:
    gty_t_bp_centrl TYPE SORTED TABLE OF  /mdgbp/_s_bp_pp_bp_centrl WITH UNIQUE KEY bp_header .
  TYPES:
    gty_t_bp_compny TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_compny WITH UNIQUE KEY assgnm_id bp_header company .
  TYPES:
    gty_t_bp_cpgen  TYPE SORTED TABLE OF /mdgbp/_s_bp_pp_bp_cpgen WITH UNIQUE KEY bp_rel partner1 partner2 .
  TYPES:
    gty_t_bp_cuscla TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_cuscla WITH UNIQUE KEY assgnm_id bp_header class classtype ecocntr .
  TYPES:
    gty_t_bp_cusddb TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_cusddb WITH UNIQUE KEY assgnm_id bp_header cus_dokar cus_doknr cus_doktl cus_dokvr .
  TYPES:
    gty_t_bp_cusdun TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_cusdun WITH UNIQUE KEY assgnm_id bp_header company maber .
  TYPES:
    gty_t_bp_cusfcn TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_cusfcn WITH UNIQUE KEY assgnm_id bp_header spart vkorg vtweg parvw parza .
  TYPES:
    gty_t_bp_cusgen TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_cusgen WITH UNIQUE KEY assgnm_id bp_header .
  TYPES:
    gty_t_bp_custax TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_custax WITH UNIQUE KEY assgnm_id bp_header aland tatyp .
  TYPES:
    gty_t_bp_cusulp TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_cusulp WITH UNIQUE KEY assgnm_id bp_header ablad .
  TYPES:
    gty_t_bp_cusval TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_cusval WITH UNIQUE KEY assgnm_id bp_header charid classtype ecocntr valcnt .
  TYPES:
    gty_t_bp_cuswht TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_cuswht WITH UNIQUE KEY assgnm_id bp_header company witht .
  TYPES:
    gty_t_bp_cus_cc TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_cus_cc WITH UNIQUE KEY assgnm_id bp_header company .
  TYPES:
    gty_t_bp_dunn   TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_dunn WITH UNIQUE KEY assgnm_id bp_header company maber .
*  TYPES:
*    gty_t_bp_entity_prop_by_bp TYPE SORTED TABLE OF gty_s_bp_entity_prop_by_bp WITH NON-UNIQUE KEY bp .
  TYPES:
    gty_t_bp_field_prop TYPE STANDARD TABLE OF ZMDG_T_BP_FPROP WITH NON-UNIQUE KEY mandt
                                                                                   cr_type
                                                                                   cr_step
                                                                                   bu_group
                                                                                   ktokk
                                                                                   ktokd
                                                                                   entity
                                                                                   fieldname .
  TYPES:
    gty_t_bp_header TYPE SORTED TABLE OF  /mdgbp/_s_bp_pp_bp_header WITH UNIQUE KEY bp_header .
  TYPES:
    gty_t_bp_hrchy  TYPE SORTED TABLE OF /mdgbp/_s_bp_pp_bp_hrchy WITH UNIQUE KEY bp_hrchy .
  TYPES:
    gty_t_bp_idnum  TYPE SORTED TABLE OF  /mdgbp/_s_bp_pp_bp_idnum  WITH UNIQUE KEY bp_header bp_idtype bp_id_num .
  TYPES:
    gty_t_bp_indstr TYPE SORTED TABLE OF  /mdgbp/_s_bp_pp_bp_indstr WITH UNIQUE KEY bp_header bp_indsct bp_indsys .
  TYPES:
    gty_t_bp_message TYPE STANDARD TABLE OF gty_s_bp_message .
  TYPES:
    gty_t_bp_mlt_ad TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_mlt_ad WITH UNIQUE KEY assgnm_id bp_header addrno .
  TYPES:
    gty_t_bp_mlt_as TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_mlt_as WITH UNIQUE KEY bp_header assgnm_id .
  TYPES:
    gty_t_bp_porg   TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_porg WITH UNIQUE KEY assgnm_id bp_header prch_org .
  TYPES:
    gty_t_bp_porg2  TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_porg2  WITH UNIQUE KEY assgnm_id bp_header prch_org ltsnr werks_d .
  TYPES:
    gty_t_bp_rel    TYPE SORTED TABLE OF /mdgbp/_s_bp_pp_bp_rel WITH UNIQUE KEY bp_rel partner1 partner2 .
  TYPES:
    gty_t_bp_role   TYPE SORTED TABLE OF  /mdgbp/_s_bp_pp_bp_role WITH UNIQUE KEY bp_header bp_rol_id .
  TYPES:
    gty_t_bp_rules TYPE STANDARD TABLE OF zmdg_t_bp_rules.
  TYPES:
    gty_t_bp_sales  TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_sales  WITH UNIQUE KEY assgnm_id bp_header spart vkorg vtweg .
  TYPES:
    gty_t_bp_subhry TYPE SORTED TABLE OF /mdgbp/_s_bp_pp_bp_subhry WITH UNIQUE KEY bp_subhry .
  TYPES:
    gty_t_bp_taxgrp TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_taxgrp WITH UNIQUE KEY assgnm_id bp_header koart taxgr .
  TYPES:
    gty_t_bp_taxnum TYPE SORTED TABLE OF  /mdgbp/_s_bp_pp_bp_taxnum WITH UNIQUE KEY bp_header bp_tx_typ .
  TYPES:
    gty_t_bp_vencla TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_vencla WITH UNIQUE KEY assgnm_id bp_header class classtype ecocntr .
  TYPES:
    gty_t_bp_venddb TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_venddb WITH UNIQUE KEY assgnm_id bp_header ven_dokar ven_doknr ven_doktl ven_dokvr .
  TYPES:
    gty_t_bp_venfcn TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_venfcn WITH UNIQUE KEY assgnm_id bp_header prch_org ltsnr parvw parza werks_d .
  TYPES:
    gty_t_bp_vengen TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_vengen WITH UNIQUE KEY assgnm_id bp_header .
  TYPES:
    gty_t_bp_vensub TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_vensub WITH UNIQUE KEY assgnm_id bp_header ltsnr ven_langu .
  TYPES:
    gty_t_bp_venval TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_venval WITH UNIQUE KEY assgnm_id bp_header charid classtype ecocntr valcnt .
  TYPES:
    gty_t_bp_where TYPE SORTED TABLE OF gty_s_bp_where WITH NON-UNIQUE KEY bp .
  TYPES:
    gty_t_bp_whtax  TYPE SORTED TABLE OF  /mdgbpx/_s_bp_pp_bp_whtax  WITH UNIQUE KEY assgnm_id bp_header company land_1 witht .
  TYPES:
    gty_t_bp_wpad   TYPE SORTED TABLE OF /mdgbp/_s_bp_pp_bp_wpad WITH UNIQUE KEY bp_rel addrno partner1 partner2 .
  TYPES:
    gty_t_cuscctxt  TYPE SORTED TABLE OF  mdg_bs_cust_cuscctxt  WITH UNIQUE KEY assgnm_id bp_header company cuslangu cus_tdid .
  TYPES:
    gty_t_cusgentxt TYPE SORTED TABLE OF  mdg_bs_cust_cusgentxt WITH UNIQUE KEY assgnm_id bp_header cuslangu cus_tdid .
  TYPES:
    gty_t_cussaltxt TYPE SORTED TABLE OF  mdg_bs_cust_cussaltxt  WITH UNIQUE KEY assgnm_id bp_header spart vkorg vtweg cuslangu cus_tdid .
  TYPES:
    gty_t_fkklocks  TYPE SORTED TABLE OF /mdgbpx/_s_bp_pp_fkklocks WITH UNIQUE KEY bp_header fkkvk fkk_valdt fkk_fdate fkk_lockr fkk_proid fkk_tdate .
  TYPES:
    gty_t_fkktaxex  TYPE SORTED TABLE OF /mdgbpx/_s_bp_pp_fkktaxex WITH UNIQUE KEY fkkvk fkk_exdfr fkk_kschl fkk_mwskz .
  TYPES:
    gty_t_fkktxt    TYPE SORTED TABLE OF /mdgbpx/_s_bp_pp_fkktxt WITH UNIQUE KEY bp_header fkkvk fkk_valdt fkk_langu fkk_tdid .
  TYPES:
    gty_t_fkkvk     TYPE SORTED TABLE OF /mdgbpx/_s_bp_pp_fkkvk WITH UNIQUE KEY fkkvk .
  TYPES:
    gty_t_fkkvkcorr TYPE SORTED TABLE OF /mdgbpx/_s_bp_pp_fkkvkcorr WITH UNIQUE KEY bp_header fkkvk fkk_valdt fkk_ident .
  TYPES:
    gty_t_fkkvkp    TYPE SORTED TABLE OF /mdgbpx/_s_bp_pp_fkkvkp WITH UNIQUE KEY fkkvk fkk_valdt bp_header .
  TYPES:
    gty_t_fkkvktd   TYPE SORTED TABLE OF /mdgbpx/_s_bp_pp_fkkvktd WITH UNIQUE KEY fkkvk fkk_valdt .
  TYPES:
    gty_t_mdg_bs_bp_fldgrp TYPE STANDARD TABLE OF gty_s_mdg_bs_bp_fldgrp .
  TYPES:
    gty_t_vencctxt  TYPE SORTED TABLE OF  mdg_bs_suppl_vencctxt  WITH UNIQUE KEY assgnm_id bp_header company venlangu ven_tdid .
  TYPES:
    gty_t_vengentxt TYPE SORTED TABLE OF  mdg_bs_suppl_vengentxt WITH UNIQUE KEY assgnm_id bp_header venlangu ven_tdid .
  TYPES:
    gty_t_venpotxt  TYPE SORTED TABLE OF  mdg_bs_suppl_venpotxt  WITH UNIQUE KEY assgnm_id bp_header prch_org venlangu ven_tdid .
  TYPES:
    gty_t_wp_email  TYPE SORTED TABLE OF /mdgbp/_s_bp_pp_wp_email WITH UNIQUE KEY addrno bp_rel ad_consno partner1 partner2 .
  TYPES:
    gty_t_wp_fax    TYPE SORTED TABLE OF /mdgbp/_s_bp_pp_wp_fax WITH UNIQUE KEY addrno bp_rel ad_consno partner1 partner2 .
  TYPES:
    gty_t_wp_postal TYPE SORTED TABLE OF /mdgbp/_s_bp_pp_wp_postal WITH UNIQUE KEY addrno bp_rel ad_nation partner1 partner2 .
  TYPES:
    gty_t_wp_tel    TYPE SORTED TABLE OF /mdgbp/_s_bp_pp_wp_tel WITH UNIQUE KEY addrno bp_rel ad_consno partner1 partner2 .
  TYPES:
    gty_t_wp_url    TYPE SORTED TABLE OF /mdgbp/_s_bp_pp_wp_url WITH UNIQUE KEY addrno bp_rel ad_consno partner1 partner2 .
ENDINTERFACE.