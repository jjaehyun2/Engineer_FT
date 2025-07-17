class /HEC1/CL_CONFIG_HELPER definition
  public
  final
  create public .

public section.

  class-methods GET_NODE_DATA_DYNAMIC
    importing
      !IV_KEY type /BOBF/CONF_KEY
      !IV_NODE type /BOPF/OBM_NODE_KEY
    exporting
      value(ET_DATA) type ANY .
  class-methods GET_PARENT_NODE_DATA_DYNAMIC
    importing
      !IV_KEY type /BOBF/CONF_KEY
      !IV_NODE type /BOPF/OBM_NODE_KEY
    exporting
      value(ET_DATA) type ANY .
  class-methods CALCULATE_DURATION
    importing
      !IV_START_DATE type /HEC1/PHASE_START_DATE
      !IV_END_DATE type /HEC1/PHASE_END_DATE
      !IV_UNIT type CHAR2
    returning
      value(RV_DURATION) type NUMC3 .
  class-methods CONVERT_KEY_2_UUID_C22
    importing
      !IV_KEY type /BOBF/CONF_KEY
    returning
      value(RV_UUID_C22) type SYSUUID_C22 .
  class-methods CONVERT_KEY_2_UUID_C26
    importing
      !IV_KEY type /BOBF/CONF_KEY
    returning
      value(RV_UUID_C26) type SYSUUID_C26 .
  class-methods CONVERT_UIDD_C22_2_KEY
    importing
      !IV_UIDD_C22 type SYSUUID_C22
    returning
      value(RV_KEY) type /BOBF/CONF_KEY .
  class-methods CONVERT_BOPF_MSG_TO_FPM_MSG
    importing
      !IO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    returning
      value(RT_FPM_MESSAGE) type FPMGB_T_MESSAGES .
  class-methods CONVERT_UIDD_C26_2_KEY
    importing
      !IV_UIDD_C26 type SYSUUID_C26
    returning
      value(RV_KEY) type /BOBF/CONF_KEY .
  class-methods CREATE_CR_CMS_CASE
    importing
      !IS_LANDSCAPE type /HEC1/S_CONFIG_ROOT_CS
    exporting
      !EV_CMS_CASE_ID type SCMG_EXT_KEY .
  class-methods DELETE_GENERATED_PHASES
    importing
      !IV_NODE_KEY type /BOBF/OBM_NODE_KEY
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IT_PARAM_CHILD_LIST type /BOBF/T_FRW_NODE
    exporting
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
    returning
      value(RT_MODIFICATION) type /BOBF/T_FRW_MODIFICATION .
  class-methods DO_CURRENCY_EXCHANGE
    importing
      !IV_CURRENCY_FROM type FCURR_CURR
      !IV_CURRENCY_AMOUNT type /HEC1/PRICE_SSP100
      !IV_CURRENCY_TO type TCURR_CURR
      !IV_DATE type /HEC1/APM_FX_RATE_DATE
    exporting
      !EV_EXCHANGE_RATE type /HEC1/EXCHANGE_RATE
      !EV_EXCHANGE_VALUE type /HEC1/EXCHANGE_VALUE .
  class-methods DO_PRICE_VALIDATION
    importing
      !IV_NODE_KEY type /BOBF/OBM_NODE_KEY
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IV_EFFORT_BB_GUID type SYSUUID_C32
      !IV_TIER_IS_DR_NODE type /HEC1/TIER_IS_DR_NODE
      !IV_DR_OPERATING_MODE type /HEC1/DR_OPER_MODE_VALUE
    returning
      value(RS_PRICING) type /HEC1/S_TIMEBASED_EFFORT_PRICE .
  class-methods GET_APM_DESCRIPTION
    importing
      !IV_APM_GUID type /HEC1/APM_GUID
    returning
      value(RV_APM_DESCR) type /HEC1/APM_DESCR .
  class-methods GET_APM_MODEL
    importing
      !IV_NODE_KEY type /BOBF/OBM_NODE_KEY
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
    exporting
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !ES_APM_MODEL type DATA .
  class-methods GET_DATACENTER
    importing
      !IT_ROOT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
    returning
      value(RR_VALUE) type ref to DATA .
  class-methods GET_DATA_AND_KEY_BY_QUERY
    importing
      !IV_QUERY_KEY type /BOBF/OBM_QUERY_KEY
      !IT_FILTER_KEY type /BOBF/T_FRW_KEY optional
      !IT_SELECTION_PARAM type /BOBF/T_FRW_QUERY_SELPARAM optional
      !IS_QUERY_OPTIONS type /BOBF/S_FRW_QUERY_OPTIONS optional
      !IV_FILL_DATA type BOOLE_D optional
      !IT_REQUESTED_ATTR type /BOBF/T_FRW_NAME optional
    exporting
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
      !EV_HITS_FOUND type INT4
      !ET_DATA type INDEX TABLE
      !ET_KEY type /BOBF/T_FRW_KEY .
  class-methods GET_EXCHANGE_RATE
    importing
      !IV_CURRENCY_FROM type FCURR_CURR
      !IV_CURRENCY_TO type TCURR_CURR
      !IV_DATE type /HEC1/APM_FX_RATE_DATE
    returning
      value(RV_EXCHANGE_RATE) type /HEC1/EXCHANGE_RATE .
  class-methods GET_GENERAL_DATA
    importing
      !IV_NODE_KEY type /BOBF/OBM_NODE_KEY
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
    exporting
      !EV_ROOT_KEY type /BOBF/CONF_KEY
      !ER_LANDSCAPE type ref to /HEC1/S_CONFIG_ROOT_CS
      !ER_DELIVERY_UNIT type ref to /HEC1/S_DATA_DLVY_UNIT_CS
      !ET_MAN_SERV_BASELINE type /HEC1/T_DATA_MAN_SERV_BASEL_CT
      !ET_DATACENTER type /HEC1/T_DATA_DATACENTER_CT
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY .
  class-methods GET_NEW_KEY
    returning
      value(RV_KEY) type /BOBF/CONF_KEY .
  class-methods GET_PHASE_ASSIGNMENT
    importing
      !IV_NODE_KEY type /BOBF/OBM_NODE_KEY
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
    exporting
      !RV_IS_ASSIGNED type ABAP_BOOLEAN .
  class-methods GET_PRICE_COSTBASED
    importing
      !IV_PRICE_LB_GUID type /HEC1/PRICE_LB_GUID
    returning
      value(RS_PRICING) type /HEC1/S_COSTBASED_PRICE_LB .
  class-methods GET_PRICE_FROM_DATABASE .
  class-methods GET_PRICE_RELEVANT_NODE_DATA
    importing
      !IS_CTX type /HEC1/S_CTX_GENERAL
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
    exporting
      !ET_LANDSCAPE type /HEC1/T_CONFIG_ROOT_CT
      !ET_PHASE type /HEC1/T_DATA_PHASE_CT
      !ET_MANAGED_SERV_BASELINE type /HEC1/T_DATA_MAN_SERV_BASEL_CT
      !ET_DELIVERY_UNIT type /HEC1/T_DATA_DLVY_UNIT_CT
      !ET_INFRA_STRUC_BASELINE type /HEC1/T_DATA_IF_BASELINE_CT
      !ET_CONNECTIVITY type /HEC1/T_DATA_CONNECTIVITY_CT
      !ET_ADD_SERVICE type /HEC1/T_DATA_ADD_SERVICES_CT
      !ET_LT_BACKUP_DATACENTER type /HEC1/T_DATA_LT_BACKUP_DC_CT
      !ET_LT_BACKUP_CLASS type /HEC1/T_DATA_LT_BACKUP_CL_CT
      !ET_LT_BACKUP_AMOUNT type /HEC1/T_LT_BACKUP_AMOUNT_CT
      !ET_ADD_STORAGE_DATACENTER type /HEC1/T_ADD_STORAGE_DC_CT
      !ET_ADD_STORAGE_CLASS type /HEC1/T_ADD_STORAGE_CLASS_CT
      !ET_ADD_STORAGE_AMOUNT type /HEC1/T_ADD_STORAGE_AMOUNT_CT
      !ET_TIER type /HEC1/T_DATA_TIER_CT
      !ET_SOFTWARE_ITEM type /HEC1/T_DATA_SW_ITEM_CT
      !ET_TIER_ADD_SERVICE type /HEC1/T_DATA_TIER_ADD_SERV_CT
      !ET_DB_NODE type /HEC1/T_DATA_DB_NODE_CT
      !ET_DB_SERVER type /HEC1/T_DATA_DB_SERV_CT
      !ET_DB_STORAGE type /HEC1/T_DATA_DB_STORAGE_CT
      !ET_DB_BACKUP type /HEC1/T_DATA_DB_BACKUP_CT
      !ET_APP_SERV_PERF_CAT type /HEC1/T_DATA_APP_SERV_PC_CT
      !ET_APP_SERVER type /HEC1/T_DATA_APP_SERV_CT
      !ET_APP_STORAGE type /HEC1/T_DATA_APP_STORAGE_CT
      !ET_APP_BACKUP type /HEC1/T_DATA_APP_BACKUP_CT
      !ET_TIER_PRICE_PHASE type /HEC1/T_TIER_PRICE_AGGRE_CT
      !ET_LANDSC_PRICE_PHASE type /HEC1/T_LANDSC_PRICE_AGGRE_CT
      !ET_CONNECT_PRICE_PHASE type /HEC1/T_CONNECT_PRICE_AGGRE_CT
      !ET_SERVICE_PRICE_PHASE type /HEC1/T_SERVICE_PRICE_AGGRE_CT
      !ET_LT_BACKUP_PRICE_PHASE type /HEC1/S_LT_BACKUP_PRICE_AGG_CT
      !ET_ADD_STORAGE_PRICE_PHASE type /HEC1/T_ADD_STORAGE_PRICE_PHAS .
  class-methods GET_PRICE_TIMEBASED_BB
    importing
      !IV_EFFORT_BB_GUID type SYSUUID_C32
      !IV_ROOT_KEY type /BOBF/CONF_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
    returning
      value(RS_PRICING) type /HEC1/S_TIMEBASED_EFFORT_PRICE .
  class-methods GET_PRICE_TIMEBASED_LB
    importing
      !IV_PRICE_LB_GUID type /HEC1/PRICE_LB_GUID
    returning
      value(RS_PRICING) type /HEC1/S_TIMEBASED_PRICING_LB .
  class-methods GET_ROOT_KEY
    importing
      !IV_NODE_KEY type /BOBF/OBM_NODE_KEY
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
    exporting
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
    returning
      value(RV_KEY) type /BOBF/CONF_KEY .
  class-methods GET_ROOT_KEY_BY_QUERY
    importing
      !IV_CONFID type /HEC1/CONFIG_ID
      !IV_CONF_VERSION type /HEC1/CONFIG_VERSION
    exporting
      !EV_HITS_FOUND type INT4
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    returning
      value(RV_KEY) type /BOBF/CONF_KEY .
  class-methods GET_ROOT_NODE
    importing
      !IV_NODE_KEY type /BOBF/OBM_NODE_KEY
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IO_MODIFY type ref to /BOBF/IF_FRW_MODIFY
    returning
      value(RS_ROOT) type /HEC1/S_CONFIG_ROOT_CS .
  class-methods GET_ROOT_NODE_KEY
    importing
      !IV_BO_KEY type /BOBF/OBM_BO_KEY default /HEC1/IF_CONFIGURATION_C=>SC_BO_KEY
    returning
      value(RV_ROOT_NODE_KEY) type /BOBF/OBM_NODE_KEY .
  class-methods SET_CR_RELATED_FIELDS
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_DET
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IO_MODIFY type ref to /BOBF/IF_FRW_MODIFY
      !IV_MOD_TYPE type /HEC1/COMP_MOD_TYPE
      !IS_NODE_DATA type ref to DATA
      !IV_SET_APM type ABAP_BOOL
      !IV_CLEAR_PHASE type ABAP_BOOL
    returning
      value(RV_DATA_CHANGED) type BOOLEAN .
  class-methods SET_MESSAGE
    importing
      !IV_TEXTID type SCX_T100KEY
      !IV_SEVERITY type /BOBF/CM_FRW=>TY_MESSAGE_SEVERITY default /BOBF/CM_FRW=>CO_SEVERITY_ERROR
      !IV_LIFETIME type /BOBF/CM_FRW=>TY_MESSAGE_LIFETIME default /BOBF/IF_FRW_C=>SC_LIFETIME_SET_BY_BOPF
      !IV_SYMPTOM type /BOBF/CM_FRW=>TY_MESSAGE_SYMPTOM default /BOBF/IF_FRW_MESSAGE_SYMPTOMS=>CO_BO_INCONSISTENCY
      !IS_ORIGIN_LOCATION type /BOBF/S_FRW_LOCATION optional
      !IV_ATTR1 type SYMSGV optional
      !IV_ATTR2 type SYMSGV optional
      !IV_ATTR3 type SYMSGV optional
      !IV_ATTR4 type SYMSGV optional
    changing
      !CO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE .
  class-methods CHECK_APM_VALIDITY_BY_GRACE_P
    importing
      !IS_ROOT type /HEC1/S_CONFIG_ROOT_CS optional
    changing
      !CT_APM_VALIDITY type /HEC1/T_APM_VALIDITY .
  class-methods GET_CONNECTIVITY_DESCRIPTION
    importing
      !IV_CONNECTIVITY_GUID type /HEC1/CONNECTIVITY_FDT_GUID
    returning
      value(RV_CONNECTIVITY_DESCR) type /HEC1/CONNECTIVITY_DESCR .
  PROTECTED SECTION.
private section.
ENDCLASS.



CLASS /HEC1/CL_CONFIG_HELPER IMPLEMENTATION.


  METHOD convert_key_2_uuid_c22.

    CHECK iv_key IS NOT INITIAL.

    TRY.
        cl_system_uuid=>convert_uuid_x16_static( EXPORTING uuid     = iv_key
                                                 IMPORTING uuid_c22 = rv_uuid_c22 ).

      CATCH cx_uuid_error. " Error Class for UUID Processing Errors
    ENDTRY.


  ENDMETHOD.


  METHOD set_message.

    IF co_message IS NOT BOUND.
      co_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    IF is_origin_location IS NOT INITIAL.
      DATA(ls_origin_location) = VALUE /bobf/s_frw_location( BASE CORRESPONDING #( is_origin_location )
                                                             bo_key = /hec1/if_configuration_c=>sc_bo_key ).
    ENDIF.

    co_message->add_cm( NEW /hec1/cx_bopf_config( textid             = iv_textid
                                                  severity           = iv_severity
                                                  lifetime           = iv_lifetime
                                                  symptom            = iv_symptom
                                                  ms_origin_location = ls_origin_location
                                                  mv_attr1           = iv_attr1
                                                  mv_attr2           = iv_attr2
                                                  mv_attr3           = iv_attr3
                                                  mv_attr4           = iv_attr4           ) ).

  ENDMETHOD.


  METHOD do_price_validation.

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = iv_node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit) ).

    SELECT SINGLE * FROM /hec1/c_tbe_bb
           INTO @DATA(ls_effort_timebased_bb)
           WHERE hec_timebased_effort_bb_guid = @iv_effort_bb_guid.

    rs_pricing = CORRESPONDING #( ls_effort_timebased_bb ).


    " Get effort lego block GUID
    CASE iv_tier_is_dr_node.
      WHEN abap_false.
        DATA(lt_range_table) = VALUE /hec1/t_selection_range( ( option = /hec1/if_config_constants=>gc_range_option-eq
                                                                sign   = /hec1/if_config_constants=>gc_range_sign-i
                                                                low    = '05'                                           )
                                                              ( option = /hec1/if_config_constants=>gc_range_option-eq
                                                                sign   = /hec1/if_config_constants=>gc_range_sign-i
                                                                low    = '06'                                           ) ).
      WHEN abap_true.
        lt_range_table = VALUE /hec1/t_selection_range( ( option = /hec1/if_config_constants=>gc_range_option-eq
                                                          sign   = /hec1/if_config_constants=>gc_range_sign-i
                                                          low    = iv_dr_operating_mode                          ) ).

    ENDCASE.

    SELECT SINGLE hec_timebased_effort_lb_guid
      FROM /hec1/i_efforttimebasedlbbasic
     WHERE hec_apm_guid                = @lr_landscape->hec_apm_guid                   AND
           hec_block_cat_value         = @ls_effort_timebased_bb-hec_block_cat         AND
           hec_block_ref_value         = @ls_effort_timebased_bb-hec_block_ref         AND
           hec_block_type_value        = @ls_effort_timebased_bb-hec_block_type        AND
           hec_delivery_unit_cat_value = @lr_delivery_unit->hec_delivery_unit_category AND
           hec_inf_provider_cat_value  = @lr_delivery_unit->hec_inf_provider_category  AND
           hec_mat_oper_mode_value     = @lr_landscape->hec_material_opmode_value      AND
           hec_access_dlvy_cat_value   = @lr_landscape->hec_acccess_dlvy_cat_value     AND
           hec_tier_is_dr_node         = @iv_tier_is_dr_node                           AND
           hec_dr_oper_mode_value IN @lt_range_table
      INTO @DATA(lv_effort_lb_guid).


    IF lv_effort_lb_guid IS NOT INITIAL.
      SELECT SINGLE * FROM /hec1/c_tbp_lb
         INTO @DATA(ls_effort_timebased_lb)
        WHERE hec_timebased_price_lb = @lv_effort_lb_guid.

      rs_pricing = VALUE #( BASE rs_pricing
                            hec_timebased_price_lb    = ls_effort_timebased_lb-hec_timebased_price_lb
                            hec_timeb_price_lb_descr  = ls_effort_timebased_lb-hec_timeb_price_lb_descr
                            hec_operation_rate        = ls_effort_timebased_lb-hec_operation_rate
                            hec_setup_rate            = ls_effort_timebased_lb-hec_setup_rate
                            hec_monthly_setup_fee     = rs_pricing-hec_one_time_setup_effort    * ls_effort_timebased_lb-hec_setup_rate
                            hec_monthly_operation_fee = rs_pricing-hec_monthly_operating_effort * ls_effort_timebased_lb-hec_operation_rate ).
    ENDIF.


  ENDMETHOD.


  METHOD get_datacenter.

    DATA: lt_dlvy_unit_key TYPE /bobf/t_frw_key,
          lt_datacenter    TYPE /hec1/t_data_datacenter_ct.


    " Get delivery unit
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = it_root_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-delivery_unit
                                      IMPORTING et_target_key  = lt_dlvy_unit_key                                            ).

    " Get data center
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-delivery_unit
                                                it_key         = lt_dlvy_unit_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-delivery_unit-datacenter
                                      IMPORTING et_data        = lt_datacenter                                                     ).

    rr_value = NEW /hec1/t_data_datacenter_ct( lt_datacenter ).


  ENDMETHOD.


  METHOD get_data_and_key_by_query.

    TRY.
        /bobf/cl_tra_serv_mgr_factory=>get_service_manager( iv_bo_key = /hec1/if_configuration_c=>sc_bo_key )->query(
          EXPORTING
            iv_query_key            = iv_query_key
            it_filter_key           = it_filter_key
            it_selection_parameters = it_selection_param
            is_query_options        = is_query_options
            iv_fill_data            = iv_fill_data
            it_requested_attributes = it_requested_attr
          IMPORTING
            eo_message              = eo_message
            es_query_info           = DATA(ls_query_info)
            et_data                 = et_data
            et_key                  = et_key                                                                            ).

        ev_hits_found = ls_query_info-count.

      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.


  ENDMETHOD.


  METHOD get_general_data.

    DATA: lt_landscape     TYPE /hec1/t_config_root_ct,
          lt_delivery_unit TYPE /hec1/t_data_dlvy_unit_ct.


    ev_root_key = get_root_key( EXPORTING iv_node_key   = iv_node_key
                                          it_key        = it_key
                                          io_read       = io_read
                                IMPORTING et_failed_key = et_failed_key ).

    " Get Landscape
    io_read->retrieve( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                 it_key         = VALUE #( ( key = ev_root_key ) )
                       IMPORTING et_data        = lt_landscape ).


    er_landscape = NEW #( VALUE #( lt_landscape[ 1 ] OPTIONAL ) ).

    " Get managed service baseline
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = VALUE #( ( key = ev_root_key ) )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-managed_service_baseline
                                      IMPORTING et_data        = et_man_serv_baseline
                                                et_target_key  = DATA(lt_man_service_baseline_key) ).

    " Get Delivery Unit
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = VALUE #( ( key = ev_root_key ) )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-delivery_unit
                                      IMPORTING et_data        = lt_delivery_unit
                                                et_target_key  = DATA(lt_delivery_unit_key) ).

    TRY.
        er_delivery_unit = NEW #( lt_delivery_unit[ 1 ] ).
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

    " Get Datacenter
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-delivery_unit
                                                it_key         = lt_delivery_unit_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-delivery_unit-datacenter
                                      IMPORTING et_data        = et_datacenter ).

  ENDMETHOD.


  METHOD get_new_key.

    TRY.
        rv_key = /bobf/cl_tra_serv_mgr_factory=>get_service_manager( iv_bo_key = /hec1/if_configuration_c=>sc_bo_key )->get_new_key( ).
      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.


  ENDMETHOD.


  METHOD get_price_costbased.

    CHECK iv_price_lb_guid IS NOT INITIAL.

    SELECT SINGLE * FROM /hec1/c_cbp_lb       "#EC CI_ALL_FIELDS_NEEDED
      INTO @rs_pricing
      WHERE hec_price_lb = @iv_price_lb_guid.

  ENDMETHOD.


  METHOD get_price_from_database.




  ENDMETHOD.


  METHOD get_price_relevant_node_data.

    " The hand over key has to be the root key, otherwise function will work
    " in an unaspected way(means error!!!)
    CHECK is_ctx-node_key = /hec1/if_configuration_c=>sc_node-root.

    " Get landscape data
    io_read->retrieve( EXPORTING iv_node        = is_ctx-node_key
                                 it_key         = it_key
                       IMPORTING et_data        = et_landscape ). "landscape = root

    " Get managed service baseline data
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-managed_service_baseline
                                      IMPORTING et_data        = et_managed_serv_baseline                                               ).


    " Get additional service data
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-add_service
                                      IMPORTING et_data        = et_add_service                                            ).

    " Get longterm backup datacenter key
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-lt_backup_datacenter
                                      IMPORTING et_data        = et_lt_backup_datacenter
                                                et_target_key  = DATA(lt_key_ltbd)                                                  ).


    " Get longterm backup class key
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-lt_backup_datacenter
                                                it_key         = lt_key_ltbd
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-lt_backup_datacenter-lt_backup_class
                                      IMPORTING et_data        = et_lt_backup_class
                                                et_target_key  = DATA(lt_key_ltbc)                                                              ).


    " Get longterm backup amount data
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-lt_backup_class
                                                it_key         = lt_key_ltbc
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-lt_backup_class-lt_backup_amount
                                      IMPORTING et_data        = et_lt_backup_amount                                                       ).


    " Get additional storage datacenter key
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-add_storage_datacenter
                                      IMPORTING et_data        = et_add_storage_datacenter
                                                et_target_key  = DATA(lt_key_add_storage_dc)                                                  ).


    " Get additional storage class key
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-add_storage_datacenter
                                                it_key         = lt_key_add_storage_dc
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-add_storage_datacenter-add_storage_class
                                      IMPORTING et_data        = et_add_storage_class
                                                et_target_key  = DATA(lt_key_add_storage_cl)                                                              ).


    " Get additional storage amount data
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-add_storage_class
                                                it_key         = lt_key_add_storage_cl
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-add_storage_class-add_storage_amount
                                      IMPORTING et_data        = et_add_storage_amount                                                       ).

    " Get phase data
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                      IMPORTING et_data        = et_phase                                            ).


    " Get service price phase data
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-add_service_price_phase
                                      IMPORTING et_data        = et_service_price_phase                                                ).


    " Get connectivity price phase data
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-connectivity_price_phase
                                      IMPORTING et_data        = et_connect_price_phase                                                 ).


    " Get landscape base price phase data
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-landsc_base_price_phase
                                      IMPORTING et_data        = et_landsc_price_phase                                                 ).

    " Get add storage price phase data
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-add_storage_price_phase
                                      IMPORTING et_data        = et_add_storage_price_phase                                                ).


    " Get add storage price phase data
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-lt_backup_price_phase
                                      IMPORTING et_data        = et_lt_backup_price_phase                                       ).


    " Get delivery unit key
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-delivery_unit
                                      IMPORTING et_target_key  = DATA(lt_key)                                                      ).


    " Get delivery unit data
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-delivery_unit
                                      IMPORTING et_data        = et_delivery_unit
                                                et_target_key  = DATA(lt_key_dlvu)                                             ).


    " Get data center key
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-delivery_unit
                                                it_key         = lt_key_dlvu
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-delivery_unit-datacenter
                                      IMPORTING et_target_key  = DATA(lt_key_dc)                                                   ).


    " Get infrastructure baseline data
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-datacenter
                                                it_key         = lt_key_dc
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-datacenter-infrastructure_baseline
                                      IMPORTING et_data        = et_infra_struc_baseline                                                     ).

    " Get connectivity data
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-datacenter
                                                it_key         = lt_key_dc
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-datacenter-connectivity
                                      IMPORTING et_data        = et_connectivity                                                  ).


    " Get solution key
*    CLEAR lt_key.
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-solution
                                      IMPORTING et_target_key  = DATA(lt_key_sol)                                               ).


    " Get tier data
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-solution
                                                it_key         = lt_key_sol
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                      IMPORTING et_data        = et_tier
                                                et_target_key  = DATA(lt_key_tier)                                                ).


    " Get tier key
*    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-solution
*                                                it_key         = lt_key
*                                                iv_fill_data   = abap_false
*                                                iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
*                                      IMPORTING et_target_key  = data(lt_key_tier)                                      ).


    " Get tier price phase data
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                it_key         = lt_key_tier
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier-tier_price_phase
                                      IMPORTING et_data        = et_tier_price_phase                                            ).

    " Get Material key
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                it_key         = lt_key_tier
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier-material
                                      IMPORTING et_target_key  = DATA(lt_key_material)                                             ).

    " Get software item data
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-material
                                                it_key         = lt_key_material
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-material-software_item
                                      IMPORTING et_data        = et_software_item                                                 ).

    " Get DB server instance key
*    CLEAR lt_key.
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                it_key         = VALUE #( FOR wa IN et_tier
                                                                          ( key = wa-key )  )
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier-db_server_instance
                                      IMPORTING et_target_key  = DATA(lt_key_dbsi)                                                           ).

    " Get Instance DB key
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                it_key         = lt_key_dbsi
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-instance_db
                                      IMPORTING et_target_key  = DATA(lt_key_idb)                                                        ).

    " Get DB Node key
*    io_read->retrieve_by_association( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-instance_db
*                                                it_key         = lt_key_idb
*                                                iv_fill_data   = abap_false
*                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-db_node
*                                      IMPORTING et_target_key  = DATA(lt_key_dbn)                                             ).

    " Get DB Node Data
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-instance_db
                                                it_key         = lt_key_idb
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-db_node
                                      IMPORTING et_data        = et_db_node
                                                et_target_key  = DATA(lt_key_dbn)                                                   ).

    " Get DB Server performance category key
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_node
                                                it_key         = lt_key_dbn
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                                      IMPORTING et_target_key  = DATA(lt_key_dbspc)                                                     ).


    " Get DB Server
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                it_key         = lt_key_dbspc
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_server
                                      IMPORTING et_data        = et_db_server
                                                et_target_key  = DATA(lt_key_dbs)                                                             ).


    "db storage
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server
                                                it_key         = lt_key_dbs
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server-db_storage
                                      IMPORTING et_target_key  = DATA(lt_db_storage_key)
                                                et_data        = et_db_storage ).

    "db backup
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_storage
                                                it_key         = lt_db_storage_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_storage-db_storage_backup
                                      IMPORTING et_target_key  = DATA(lt_db_backup_key)
                                                et_data        = et_db_backup ).


    " Get App server instance key
    CLEAR lt_key.
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                it_key         = VALUE #( FOR wa IN et_tier
                                                                          ( key = wa-key )  )
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier-app_server_instance
                                      IMPORTING et_target_key  = DATA(lt_key_asi)                                                  ).

    "app node
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                it_key         = lt_key_asi
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-app_node
                                      IMPORTING et_target_key  = DATA(lt_app_node_key)                                                  ).

    "app serv pc
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
                                                it_key         = lt_app_node_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
                                      IMPORTING et_target_key  = DATA(lt_app_serv_pc_key)
                                                et_data        = et_app_serv_perf_cat                                                     ).

    "app server
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                it_key         = lt_app_serv_pc_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_server
                                      IMPORTING et_target_key  = DATA(lt_app_server_key)
                                                et_data        = et_app_server ).

    "app storage
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server
                                                it_key         = lt_app_server_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server-app_storage
                                      IMPORTING et_target_key  = DATA(lt_app_storage_key)
                                                et_data        = et_app_storage ).

    "app backup
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_storage
                                                it_key         = lt_app_storage_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_storage-app_storage_backup
                                      IMPORTING et_target_key  = DATA(lt_app_backup_key)
                                                et_data        = et_app_backup ).

*    " Get App Node key
*    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_instance
*                                                it_key         = lt_key_asi
*                                                iv_fill_data   = abap_false
*                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-app_node
*                                      IMPORTING et_target_key  = DATA(lt_key_an)                                                        ).
*
*
*    " Get App Server Performance Category key
*    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
*                                                it_key         = lt_key_an
*                                                iv_fill_data   = abap_false
*                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
*                                      IMPORTING et_target_key  = DATA(lt_key_aspc)                                                        ).
*
*    " Get App Server Performance Category data
*    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
*                                                it_key         = lt_key_an
*                                                iv_fill_data   = abap_true
*                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
*                                      IMPORTING et_data        = et_app_serv_perf_cat                                                     ).
*
*    " Get App Server key
*    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
*                                                it_key         = lt_key_aspc
*                                                iv_fill_data   = abap_false
*                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_server
*                                      IMPORTING et_target_key  = DATA(lt_key_as)                                                            ).
*
*    " Get App Server Data
*    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
*                                                it_key         = lt_key_aspc
*                                                iv_fill_data   = abap_true
*                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_server
*                                      IMPORTING et_data        = et_app_server                                                              ).
*
*    " Get App Storage data
*    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server
*                                                it_key         = lt_key_aspc
*                                                iv_fill_data   = abap_true
*                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server-app_storage
*                                      IMPORTING et_data        = et_app_storage                                                  ).



  ENDMETHOD.


  METHOD get_price_timebased_bb.

    DATA: lt_landscape TYPE /hec1/t_config_root_ct,
          lt_dlvy_unit TYPE /hec1/t_data_dlvy_unit_ct.


    " Get landscape
    io_read->retrieve( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                 it_key         = VALUE #( ( key = iv_root_key ) )
                       IMPORTING et_data        = lt_landscape                                            ).


    " Get delivery unit
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = VALUE #( ( key = iv_root_key ) )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-delivery_unit
                                      IMPORTING et_data        = lt_dlvy_unit                                                ).


    " In the BOPF model there is only one landscape instance
    TRY.
        DATA(ls_landscape) = lt_landscape[ 1 ].
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

    " In the BOPF model there is only one delivery unit instance
    TRY.
        DATA(ls_dlvy_unit) = lt_dlvy_unit[ 1 ].
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.


    SELECT SINGLE *
      FROM /hec1/c_tbe_bb
       INTO @DATA(ls_effort_timebased_bb)
      WHERE hec_timebased_effort_bb_guid = @iv_effort_bb_guid.

    rs_pricing = CORRESPONDING #( ls_effort_timebased_bb ).

    " Get effort lego block GUID
    SELECT SINGLE hec_timebased_effort_lb_guid
      FROM /hec1/i_efforttimebasedlbbasic
     WHERE hec_apm_guid                = @ls_landscape-hec_apm_guid               AND
           hec_block_type_value        = @ls_effort_timebased_bb-hec_block_type   AND
           hec_block_cat_value         = @ls_effort_timebased_bb-hec_block_cat    AND
           hec_block_ref_value         = @ls_effort_timebased_bb-hec_block_ref    AND
           hec_mat_oper_mode_value     = @ls_landscape-hec_material_opmode_value  AND
           hec_delivery_unit_cat_value = @ls_dlvy_unit-hec_delivery_unit_category AND
           hec_inf_provider_cat_value  = @ls_dlvy_unit-hec_inf_provider_category  AND
           hec_access_dlvy_cat_value   = @ls_landscape-hec_acccess_dlvy_cat_value
    INTO @DATA(lv_effort_lb_guid).


    IF lv_effort_lb_guid IS NOT INITIAL.
      SELECT SINGLE * FROM /hec1/c_tbp_lb
         INTO @DATA(ls_effort_timebased_lb)
        WHERE hec_timebased_price_lb = @lv_effort_lb_guid.

      rs_pricing = VALUE #( BASE rs_pricing
                            hec_timebased_price_lb          = ls_effort_timebased_lb-hec_timebased_price_lb
                            hec_timeb_price_lb_descr        = ls_effort_timebased_lb-hec_timeb_price_lb_descr
                            hec_operation_rate              = ls_effort_timebased_lb-hec_operation_rate
                            hec_setup_rate                  = ls_effort_timebased_lb-hec_setup_rate
                            hec_monthly_setup_fee           = rs_pricing-hec_one_time_setup_effort    * ls_effort_timebased_lb-hec_setup_rate
                            hec_monthly_operation_fee       = rs_pricing-hec_monthly_operating_effort * ls_effort_timebased_lb-hec_operation_rate ).
    ENDIF.


  ENDMETHOD.


  METHOD get_price_timebased_lb.

    CHECK iv_price_lb_guid IS NOT INITIAL.

    SELECT SINGLE * FROM /hec1/c_tbp_lb       "#EC CI_ALL_FIELDS_NEEDED
      INTO @rs_pricing
      WHERE hec_timebased_price_lb = @iv_price_lb_guid.

  ENDMETHOD.


  METHOD get_root_key.

    io_read->get_root_key( EXPORTING iv_node         = iv_node_key
                                     it_key          = it_key
                           IMPORTING et_failed_key   = et_failed_key
                                     et_target_key   = DATA(lt_root_key) ).

    " The root instance should exist always once
    TRY.
        rv_key = lt_root_key[ 1 ]-key.
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.


  ENDMETHOD.


  METHOD get_root_key_by_query.

    CHECK: iv_confid       IS NOT INITIAL,
           iv_conf_version IS NOT INITIAL.

    TRY.
        /bobf/cl_tra_serv_mgr_factory=>get_service_manager( iv_bo_key = /hec1/if_configuration_c=>sc_bo_key )->query(
          EXPORTING
            iv_query_key            = /hec1/if_configuration_c=>sc_query-root-select_by_elements
            it_selection_parameters = VALUE #( ( attribute_name = /hec1/if_configuration_c=>sc_query_attribute-root-select_by_elements-hec_confid
                                                 low            = iv_confid
                                                 option         = /hec1/if_bopf_constants=>gc_range_option-eq
                                                 sign           = /hec1/if_bopf_constants=>gc_range_sign-i                                               )
                                               ( attribute_name = /hec1/if_configuration_c=>sc_query_attribute-root-select_by_elements-hec_conf_version
                                                 low            = iv_conf_version
                                                 option         = /hec1/if_bopf_constants=>gc_range_option-eq
                                                 sign           = /hec1/if_bopf_constants=>gc_range_sign-i                                               ) )
            iv_fill_data            = abap_false
          IMPORTING
            eo_message              = eo_message
            es_query_info           = DATA(ls_query_info)
            et_key                  = DATA(lt_key)                                                                                                           ).

        ev_hits_found = ls_query_info-count.

        " The root instance should exist always once
        TRY.
            rv_key = lt_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.


  ENDMETHOD.


  METHOD get_root_node_key.

    CLEAR rv_root_node_key.

    " Get BO Configuration
    TRY.
        /bobf/cl_frw_factory=>get_configuration( iv_bo_key )->get_bo( IMPORTING es_obj = DATA(ls_confro_obj) ).
        rv_root_node_key = ls_confro_obj-root_node_key.

      CATCH /bobf/cx_frw.
    ENDTRY.


  ENDMETHOD.


  METHOD convert_uidd_c22_2_key.

    CHECK iv_uidd_c22 IS NOT INITIAL.

    TRY.
        cl_system_uuid=>convert_uuid_c22_static( EXPORTING uuid     = iv_uidd_c22
                                                 IMPORTING uuid_x16 = rv_key ).

      CATCH cx_uuid_error. " Error Class for UUID Processing Errors
    ENDTRY.


  ENDMETHOD.


  METHOD get_apm_model.

    DATA: lt_landscape TYPE /hec1/t_config_root_ct.


    DATA(lv_root_key) = get_root_key( EXPORTING iv_node_key   = iv_node_key
                                                it_key        = it_key
                                                io_read       = io_read
                                      IMPORTING et_failed_key = et_failed_key ).


    " Get APM model (root = landscape)
    io_read->retrieve( EXPORTING iv_node = /hec1/if_configuration_c=>sc_node-root
                                 it_key  = VALUE #( ( key = lv_root_key ) )
                       IMPORTING et_data = lt_landscape                           ).


    IF lt_landscape IS NOT INITIAL.
      TRY.
          es_apm_model = lt_landscape[ 1 ] .
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.
    ENDIF.


  ENDMETHOD.


  METHOD calculate_duration.

    DATA: lv_start_month_perc TYPE p DECIMALS 2,
          lv_end_month_perc   TYPE p DECIMALS 2.

    " Convert dates to required format
    CASE iv_unit.
      WHEN '01'. "weeks
        rv_duration = ( iv_end_date - iv_start_date ) / 7 .
      WHEN '02'. "months
        " for months we can't use the average number of days
        " instead we will substract years and dates from each other individually

        DATA(lv_start_year) = iv_start_date+0(4).
        DATA(lv_start_month) = iv_start_date+4(2).
        DATA(lv_start_day) = iv_start_date+6(2).

        DATA(lv_end_year) = iv_end_date+0(4).
        DATA(lv_end_month) = iv_end_date+4(2).
        DATA(lv_end_day) = iv_end_date+6(2).

        rv_duration = ( ( lv_end_year - lv_start_year ) * 12 ) + ( lv_end_month - lv_start_month ).

        lv_start_month_perc = lv_start_day / SWITCH #( lv_start_month
                                                       WHEN 1 OR 3 OR 5 OR 7 OR 8 OR 10 OR 12
                                                       THEN 31
                                                       WHEN 4 OR 6 OR 9 OR 11
                                                       THEN 30
                                                       WHEN 2
                                                       THEN COND #( WHEN lv_start_year MOD 4 = 0
                                                                    THEN 29
                                                                    ELSE 28 ) ).

        lv_end_month_perc = lv_end_day / SWITCH #( lv_end_month
                                                   WHEN 1 OR 3 OR 5 OR 7 OR 8 OR 10 OR 12
                                                   THEN 31
                                                   WHEN 4 OR 6 OR 9 OR 11
                                                   THEN 30
                                                   WHEN 2
                                                   THEN COND #( WHEN lv_end_year MOD 4 = 0
                                                                THEN 29
                                                                ELSE 28 ) ).

        IF ( lv_end_month_perc - lv_start_month_perc ) > +'0.5'.
          ADD 1 TO rv_duration.
        ELSEIF ( lv_end_month_perc - lv_start_month_perc ) < -'0.5'.
          SUBTRACT 1 FROM rv_duration.
        ENDIF.

      WHEN '03'. "year
        rv_duration = ( iv_end_date - iv_start_date ) * 100 / 36525.
    ENDCASE.

  ENDMETHOD.


  METHOD get_exchange_rate.

    DATA: lv_foreign_factor TYPE ffact_curr,
          lv_local_factor   TYPE tfact_curr,
          lv_exchange_rate  TYPE ukurs_curr,
          lv_type_of_rate   TYPE kurst_curr.

    DATA(lv_currency_from) = iv_currency_from.
    DATA(lv_currency_to) = iv_currency_to.
    DATA(lv_date) = iv_date.

    CLEAR: rv_exchange_rate, lv_foreign_factor, lv_local_factor, lv_exchange_rate, lv_type_of_rate.

    IF lv_currency_from IS INITIAL.
*    lv_currency_from = 'EUR'.
      RETURN.
    ENDIF.

    IF lv_currency_to IS INITIAL.
*    lv_currency_to = 'USD'.
      RETURN.
    ENDIF.

    IF lv_date IS INITIAL.
*    lv_date = sy-datum.
      RETURN.
    ENDIF.

*    lv_type_of_rate = 'M'. "Default
    lv_type_of_rate = 'FL01'. "#+ C5310379 28.09.2021

    CALL FUNCTION 'READ_EXCHANGE_RATE'
      EXPORTING
*       client           = SY-MANDT
        date             = lv_date                 " Currency translation date
        foreign_currency = lv_currency_from                 " Currency key for foreign currency
        local_currency   = lv_currency_to                 " Currency key for local currency
        type_of_rate     = lv_type_of_rate              " Type of rate M=Average rate G=Bank buying rate B=bank selling rate
*       exact_date       = space            " Exchange Rate for Exact Day Required
      IMPORTING
        exchange_rate    = lv_exchange_rate                 " Exchange rate
        foreign_factor   = lv_foreign_factor                 " Factor for the foreign currency units
        local_factor     = lv_local_factor                 " Factor for the local currency units
*       valid_from_date  =                  " Date of read entry in TCURR
*       derived_rate_type =                  " Alternative exchange rate type, where used
*       fixed_rate       =                  " Fixed exchange rate 4,5, if present
*       oldest_rate_from =                  " Date of Oldest Exchange Rate Calculation
      EXCEPTIONS
        no_rate_found    = 1                " No exch.rate entered in table TCURR
        no_factors_found = 2                " No conversion factors in TCURF
        no_spread_found  = 3                " No spread entered in table TCURS
        derived_2_times  = 4
        overflow         = 5
        zero_rate        = 6                " Indicator: No Exchange Rate Exists
        OTHERS           = 7.

    rv_exchange_rate = lv_exchange_rate.

    IF lv_foreign_factor > 1.
      rv_exchange_rate = rv_exchange_rate / lv_foreign_factor.
    ENDIF.

    IF lv_local_factor > 1.
      rv_exchange_rate = rv_exchange_rate * lv_local_factor.
    ENDIF.

    IF sy-subrc <> 0.
*    MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
*      WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
      CLEAR: rv_exchange_rate.
    ENDIF.

  ENDMETHOD.


  METHOD delete_generated_phases.

    DATA: lt_phase           TYPE /hec1/t_data_phase_ct,
          lt_tier            TYPE /hec1/t_data_tier_ct,
          lt_db_serv_inst    TYPE /hec1/t_data_db_server_inst_ct,
          lt_instance_db     TYPE /hec1/t_data_db_inst_ct,
          lt_db_node         TYPE /hec1/t_data_db_node_ct,
          lt_db_serv_pc      TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_storage_qty  TYPE /hec1/t_data_db_storage_qty_ct,
          lt_db_server       TYPE /hec1/t_data_db_serv_ct,
          lt_db_storage      TYPE /hec1/t_data_db_storage_ct,
          lt_db_backup       TYPE /hec1/t_data_db_backup_ct,
          lt_app_serv_inst   TYPE /hec1/t_data_app_serv_inst_ct,
          lt_app_node        TYPE /hec1/t_data_app_node_ct,
          lt_app_serv_pc     TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_storage_qty TYPE /hec1/t_data_app_storageqty_ct,
          lt_app_server      TYPE /hec1/t_data_app_serv_ct,
          lt_app_storage     TYPE /hec1/t_data_app_storage_ct,
          lt_app_backup      TYPE /hec1/t_data_app_backup_ct.

    CHECK it_param_child_list IS NOT INITIAL.

    DATA(lt_param_child_list) = it_param_child_list.

    " if a node is deleted, all child nodes need to be checked for generated phases.
    "   those generated phases need to be deleted, because they will otherwise never be used again.
    io_read->get_root_key( EXPORTING iv_node         = iv_node_key
                                     it_key          = it_key
                           IMPORTING et_target_key   = DATA(lt_root_key) ).

    io_read->retrieve_by_association( EXPORTING iv_node                 = /hec1/if_configuration_c=>sc_node-root
                                                it_key                  = lt_root_key
                                                iv_association          = /hec1/if_configuration_c=>sc_association-root-phase
                                                iv_fill_data            = abap_true
                                      IMPORTING et_data                 = lt_phase ).

    DATA(lt_phase_generated) = VALUE /hec1/t_data_phase_ct( FOR phase IN lt_phase
                                                            WHERE ( hec_phase_generated = abap_true )
                                                                  ( phase ) ).

    " if the configuration has no generated phases,
    "  all the nodes don't need to be read.
    IF lt_phase_generated IS NOT INITIAL.

      " Otherwise, we need to check if the paramater list contains nodes
      "  that either have generated phases themselves or have child nodes with generated phases
      "
      "  We add the nodes of each level to our temporary parameter table.
      "  This way we can select the nodes of the lower levels and still include all parameters

      " ---------------
      " Solution
      " ---------------
      IF line_exists( lt_param_child_list[ node = /hec1/if_configuration_c=>sc_node-solution ] ).
        " add children to lt_param_child_list

        " ---------------
        " Tier
        " the nodes are read by using the parent key
        "  from the previous node type
        " ---------------

        " add children to lt_param_child_list
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-solution
                                                    it_key         = VALUE #( FOR param IN lt_param_child_list
                                                                              WHERE ( node = /hec1/if_configuration_c=>sc_node-solution )
                                                                                    ( key  = param-key ) )
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                          IMPORTING et_data        = lt_tier ).

        INSERT LINES OF VALUE /bobf/t_frw_modification( FOR tier IN lt_tier
                                                        FOR phase IN lt_phase_generated
                                                        WHERE ( hec_node_phase = tier-hec_phase_guid )
                                                              ( node        = /hec1/if_configuration_c=>sc_node-phase
                                                                change_mode = /bobf/if_frw_c=>sc_modify_delete
                                                                key         = phase-key ) ) INTO TABLE rt_modification.

        APPEND LINES OF VALUE /bobf/t_frw_node( FOR tier IN lt_tier "#EC CI_APPEND_OK
                                                  ( node = /hec1/if_configuration_c=>sc_node-tier
                                                    key  = tier-key ) ) TO lt_param_child_list.

      ENDIF. "IF line_exists( lt_param_child_list[ node = /hec1/if_configuration_c=>sc_node-solution ] ).

      " ---------------
      " Tier
      " Starting from here, the nodes are read
      "   by using the parent key from the previous node type
      " ---------------
      IF line_exists( lt_param_child_list[ node = /hec1/if_configuration_c=>sc_node-tier ] ).
        " add children to lt_param_child_list

        "DB Server Instance
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                    it_key         = VALUE #( FOR param IN lt_param_child_list
                                                                              WHERE ( node = /hec1/if_configuration_c=>sc_node-tier )
                                                                                    ( key  = param-key ) )
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-tier-db_server_instance
                                          IMPORTING et_data        = lt_db_serv_inst ).

        INSERT LINES OF VALUE /bobf/t_frw_modification( FOR dbsi IN lt_db_serv_inst
                                                        FOR phase IN lt_phase_generated
                                                        WHERE ( hec_node_phase = dbsi-hec_phase_guid )
                                                              ( node        = /hec1/if_configuration_c=>sc_node-phase
                                                                change_mode = /bobf/if_frw_c=>sc_modify_delete
                                                                key         = phase-key ) ) INTO TABLE rt_modification.

        APPEND LINES OF VALUE /bobf/t_frw_node( FOR db_si IN lt_db_serv_inst "#EC CI_APPEND_OK
                                                  ( node = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                    key  = db_si-key ) ) TO lt_param_child_list.

        "App Server Instance
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                    it_key         = VALUE #( FOR param IN lt_param_child_list
                                                                              WHERE ( node = /hec1/if_configuration_c=>sc_node-tier )
                                                                                    ( key  = param-key ) )
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-tier-app_server_instance
                                          IMPORTING et_data        = lt_app_serv_inst ).

        INSERT LINES OF VALUE /bobf/t_frw_modification( FOR appsi IN lt_app_serv_inst
                                                        FOR phase IN lt_phase_generated
                                                        WHERE ( hec_node_phase = appsi-hec_phase_guid )
                                                              ( node        = /hec1/if_configuration_c=>sc_node-phase
                                                                change_mode = /bobf/if_frw_c=>sc_modify_delete
                                                                key         = phase-key ) ) INTO TABLE rt_modification.

        APPEND LINES OF VALUE /bobf/t_frw_node( FOR app_si IN lt_app_serv_inst "#EC CI_APPEND_OK
                                                  ( node = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                    key  = app_si-key ) ) TO lt_param_child_list.

      ENDIF. "IF line_exists( lt_param_child_list[ node = /hec1/if_configuration_c=>sc_node-tier ] ).

      " ---------------
      " DB Server Instance
      " ---------------
      IF line_exists( lt_param_child_list[ node = /hec1/if_configuration_c=>sc_node-db_server_instance ] ).
        " add children to lt_param_child_list

        "DB Instance DB
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                    it_key         = VALUE #( FOR param IN lt_param_child_list
                                                                              WHERE ( node = /hec1/if_configuration_c=>sc_node-db_server_instance )
                                                                                    ( key  = param-key ) )
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-instance_db
                                          IMPORTING et_data        = lt_instance_db ).

        INSERT LINES OF VALUE /bobf/t_frw_modification( FOR inst IN lt_instance_db
                                                        FOR phase IN lt_phase_generated
                                                        WHERE ( hec_node_phase = inst-hec_phase_guid )
                                                              ( node        = /hec1/if_configuration_c=>sc_node-phase
                                                                change_mode = /bobf/if_frw_c=>sc_modify_delete
                                                                key         = phase-key ) ) INTO TABLE rt_modification.

        APPEND LINES OF VALUE /bobf/t_frw_node( FOR inst IN lt_instance_db "#EC CI_APPEND_OK
                                                  ( node = /hec1/if_configuration_c=>sc_node-instance_db
                                                    key  = inst-key ) ) TO lt_param_child_list.

      ENDIF.

      " ---------------
      " Instance DB
      " ---------------
      IF line_exists( lt_param_child_list[ node = /hec1/if_configuration_c=>sc_node-instance_db ] ).
        " add children to lt_param_child_list

        "DB Node
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-instance_db
                                                    it_key         = VALUE #( FOR param IN lt_param_child_list
                                                                              WHERE ( node = /hec1/if_configuration_c=>sc_node-instance_db )
                                                                                    ( key  = param-key ) )
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-instance_db-db_node
                                          IMPORTING et_data        = lt_db_node ).

        INSERT LINES OF VALUE /bobf/t_frw_modification( FOR db_node IN lt_db_node
                                                        FOR phase IN lt_phase_generated
                                                        WHERE ( hec_node_phase = db_node-hec_phase_guid )
                                                              ( node        = /hec1/if_configuration_c=>sc_node-phase
                                                                change_mode = /bobf/if_frw_c=>sc_modify_delete
                                                                key         = phase-key ) ) INTO TABLE rt_modification.

        APPEND LINES OF VALUE /bobf/t_frw_node( FOR db_node IN lt_db_node "#EC CI_APPEND_OK
                                                  ( node = /hec1/if_configuration_c=>sc_node-db_node
                                                    key  = db_node-key ) ) TO lt_param_child_list.

      ENDIF.

      " ---------------
      " DB Node
      " ---------------
      IF line_exists( lt_param_child_list[ node = /hec1/if_configuration_c=>sc_node-db_node ] ).
        " add children to lt_param_child_list

        "DB Server Performance Category
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_node
                                                    it_key         = VALUE #( FOR param IN lt_param_child_list
                                                                            WHERE ( node = /hec1/if_configuration_c=>sc_node-db_node )
                                                                                  ( key  = param-key ) )
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                                          IMPORTING et_data        = lt_db_serv_pc ).

        INSERT LINES OF VALUE /bobf/t_frw_modification( FOR db_spc IN lt_db_serv_pc
                                                        FOR phase IN lt_phase_generated
                                                        WHERE ( hec_node_phase = db_spc-hec_phase_guid )
                                                              ( node        = /hec1/if_configuration_c=>sc_node-phase
                                                                change_mode = /bobf/if_frw_c=>sc_modify_delete
                                                                key         = phase-key ) ) INTO TABLE rt_modification.

        APPEND LINES OF VALUE /bobf/t_frw_node( FOR db_spc IN lt_db_serv_pc "#EC CI_APPEND_OK
                                                  ( node = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                    key  = db_spc-key ) ) TO lt_param_child_list.

      ENDIF.

      " ---------------
      " DB Server Performance Category
      " ---------------
      IF line_exists( lt_param_child_list[ node = /hec1/if_configuration_c=>sc_node-db_server_perform_cat ] ).
        " add children to lt_param_child_list

        "DB Storage Qty
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                    it_key         = VALUE #( FOR param IN lt_param_child_list
                                                                            WHERE ( node = /hec1/if_configuration_c=>sc_node-db_server_perform_cat )
                                                                                  ( key  = param-key ) )
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount
                                          IMPORTING et_data        = lt_db_storage_qty ).

        INSERT LINES OF VALUE /bobf/t_frw_modification( FOR db_stq IN lt_db_storage_qty
                                                        FOR phase IN lt_phase_generated
                                                        WHERE ( hec_node_phase = db_stq-hec_phase_guid )
                                                              ( node        = /hec1/if_configuration_c=>sc_node-phase
                                                                change_mode = /bobf/if_frw_c=>sc_modify_delete
                                                                key         = phase-key ) ) INTO TABLE rt_modification.

        APPEND LINES OF VALUE /bobf/t_frw_node( FOR db_stq IN lt_db_storage_qty "#EC CI_APPEND_OK
                                                  ( node = /hec1/if_configuration_c=>sc_node-db_storage_amount
                                                    key  = db_stq-key ) ) TO lt_param_child_list.

        "DB Server
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                    it_key         = VALUE #( FOR param IN lt_param_child_list
                                                                            WHERE ( node = /hec1/if_configuration_c=>sc_node-db_server_perform_cat )
                                                                                  ( key  = param-key ) )
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_server
                                          IMPORTING et_data        = lt_db_server ).

        INSERT LINES OF VALUE /bobf/t_frw_modification( FOR db_server IN lt_db_server
                                                        FOR phase IN lt_phase_generated
                                                        WHERE ( hec_node_phase = db_server-hec_phase_guid )
                                                              ( node        = /hec1/if_configuration_c=>sc_node-phase
                                                                change_mode = /bobf/if_frw_c=>sc_modify_delete
                                                                key         = phase-key ) ) INTO TABLE rt_modification.

        APPEND LINES OF VALUE /bobf/t_frw_node( FOR db_server IN lt_db_server "#EC CI_APPEND_OK
                                                  ( node = /hec1/if_configuration_c=>sc_node-db_server
                                                    key  = db_server-key ) ) TO lt_param_child_list.

      ENDIF.

      " ---------------
      " DB Server
      " ---------------
      IF line_exists( lt_param_child_list[ node = /hec1/if_configuration_c=>sc_node-db_server ] ).
        " add children to lt_param_child_list

        "DB Storage
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server
                                                    it_key         = VALUE #( FOR param IN lt_param_child_list
                                                                            WHERE ( node = /hec1/if_configuration_c=>sc_node-db_server )
                                                                                  ( key  = param-key ) )
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_server-db_storage
                                          IMPORTING et_data        = lt_db_storage ).

        INSERT LINES OF VALUE /bobf/t_frw_modification( FOR db_storage IN lt_db_storage
                                                        FOR phase IN lt_phase_generated
                                                        WHERE ( hec_node_phase = db_storage-hec_phase_guid )
                                                              ( node        = /hec1/if_configuration_c=>sc_node-phase
                                                                change_mode = /bobf/if_frw_c=>sc_modify_delete
                                                                key         = phase-key ) ) INTO TABLE rt_modification.

        APPEND LINES OF VALUE /bobf/t_frw_node( FOR db_storage IN lt_db_storage "#EC CI_APPEND_OK
                                                  ( node = /hec1/if_configuration_c=>sc_node-db_server
                                                    key  = db_storage-key ) ) TO lt_param_child_list.

      ENDIF.

      " ---------------
      " DB Backup
      " ---------------
      IF line_exists( lt_param_child_list[ node = /hec1/if_configuration_c=>sc_node-db_storage ] ).
        " add children to lt_param_child_list

        "DB Backup
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_storage
                                                    it_key         = VALUE #( FOR param IN lt_param_child_list
                                                                            WHERE ( node = /hec1/if_configuration_c=>sc_node-db_storage )
                                                                                  ( key  = param-key ) )
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_storage-db_storage_backup
                                          IMPORTING et_data        = lt_db_backup ).

        INSERT LINES OF VALUE /bobf/t_frw_modification( FOR db_backup IN lt_db_backup
                                                        FOR phase IN lt_phase_generated
                                                        WHERE ( hec_node_phase = db_backup-hec_phase_guid )
                                                              ( node        = /hec1/if_configuration_c=>sc_node-phase
                                                                change_mode = /bobf/if_frw_c=>sc_modify_delete
                                                                key         = phase-key ) ) INTO TABLE rt_modification.

        APPEND LINES OF VALUE /bobf/t_frw_node( FOR db_backup IN lt_db_backup "#EC CI_APPEND_OK
                                                  ( node = /hec1/if_configuration_c=>sc_node-db_storage_backup
                                                    key  = db_backup-key ) ) TO lt_param_child_list.

      ENDIF.

      " ---------------
      " App Server Instance
      " ---------------
      IF line_exists( lt_param_child_list[ node = /hec1/if_configuration_c=>sc_node-app_server_instance ] ).
        " add children to lt_param_child_list

        "App Node
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                    it_key         = VALUE #( FOR param IN lt_param_child_list
                                                                              WHERE ( node = /hec1/if_configuration_c=>sc_node-app_server_instance )
                                                                                    ( key  = param-key ) )
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-app_node
                                          IMPORTING et_data        = lt_app_node ).

        INSERT LINES OF VALUE /bobf/t_frw_modification( FOR app_node IN lt_app_node
                                                        FOR phase IN lt_phase_generated
                                                        WHERE ( hec_node_phase = app_node-hec_phase_guid )
                                                              ( node        = /hec1/if_configuration_c=>sc_node-phase
                                                                change_mode = /bobf/if_frw_c=>sc_modify_delete
                                                                key         = phase-key ) ) INTO TABLE rt_modification.

        APPEND LINES OF VALUE /bobf/t_frw_node( FOR app_node IN lt_app_node "#EC CI_APPEND_OK
                                                  ( node = /hec1/if_configuration_c=>sc_node-app_node
                                                    key  = app_node-key ) ) TO lt_param_child_list.

      ENDIF.

      " ---------------
      " App Node
      " ---------------
      IF line_exists( lt_param_child_list[ node = /hec1/if_configuration_c=>sc_node-app_node ] ).
        " add children to lt_param_child_list

        "App Server Performance Category
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
                                                    it_key         = VALUE #( FOR param IN lt_param_child_list
                                                                            WHERE ( node = /hec1/if_configuration_c=>sc_node-app_node )
                                                                                  ( key  = param-key ) )
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
                                          IMPORTING et_data        = lt_app_serv_pc ).

        INSERT LINES OF VALUE /bobf/t_frw_modification( FOR app_spc IN lt_app_serv_pc
                                                        FOR phase IN lt_phase_generated
                                                        WHERE ( hec_node_phase = app_spc-hec_phase_guid )
                                                              ( node        = /hec1/if_configuration_c=>sc_node-phase
                                                                change_mode = /bobf/if_frw_c=>sc_modify_delete
                                                                key         = phase-key ) ) INTO TABLE rt_modification.

        APPEND LINES OF VALUE /bobf/t_frw_node( FOR app_spc IN lt_app_serv_pc "#EC CI_APPEND_OK
                                                  ( node = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                    key  = app_spc-key ) ) TO lt_param_child_list.

      ENDIF.

      " ---------------
      " App Server Performance Category
      " ---------------
      IF line_exists( lt_param_child_list[ node = /hec1/if_configuration_c=>sc_node-app_server_perform_cat ] ).
        " add children to lt_param_child_list

        "App Storage Qty
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                    it_key         = VALUE #( FOR param IN lt_param_child_list
                                                                            WHERE ( node = /hec1/if_configuration_c=>sc_node-app_server_perform_cat )
                                                                                  ( key  = param-key ) )
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_storage_amount
                                          IMPORTING et_data        = lt_app_storage_qty ).

        INSERT LINES OF VALUE /bobf/t_frw_modification( FOR app_stq IN lt_app_storage_qty
                                                        FOR phase IN lt_phase_generated
                                                        WHERE ( hec_node_phase = app_stq-hec_phase_guid )
                                                              ( node        = /hec1/if_configuration_c=>sc_node-phase
                                                                change_mode = /bobf/if_frw_c=>sc_modify_delete
                                                                key         = phase-key ) ) INTO TABLE rt_modification.

        APPEND LINES OF VALUE /bobf/t_frw_node( FOR app_stq IN lt_app_storage_qty "#EC CI_APPEND_OK
                                                  ( node = /hec1/if_configuration_c=>sc_node-app_storage_amount
                                                    key  = app_stq-key ) ) TO lt_param_child_list.

        "App Server
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                    it_key         = VALUE #( FOR param IN lt_param_child_list
                                                                            WHERE ( node = /hec1/if_configuration_c=>sc_node-app_server_perform_cat )
                                                                                  ( key  = param-key ) )
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_server
                                          IMPORTING et_data        = lt_app_server ).

        INSERT LINES OF VALUE /bobf/t_frw_modification( FOR app_server IN lt_app_server
                                                        FOR phase IN lt_phase_generated
                                                        WHERE ( hec_node_phase = app_server-hec_phase_guid )
                                                              ( node        = /hec1/if_configuration_c=>sc_node-phase
                                                                change_mode = /bobf/if_frw_c=>sc_modify_delete
                                                                key         = phase-key ) ) INTO TABLE rt_modification.

        APPEND LINES OF VALUE /bobf/t_frw_node( FOR app_server IN lt_app_server "#EC CI_APPEND_OK
                                                  ( node = /hec1/if_configuration_c=>sc_node-app_server
                                                    key  = app_server-key ) ) TO lt_param_child_list.

      ENDIF.

      " ---------------
      " App Server
      " ---------------
      IF line_exists( lt_param_child_list[ node = /hec1/if_configuration_c=>sc_node-app_server ] ).
        " add children to lt_param_child_list

        "App Storage
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server
                                                    it_key         = VALUE #( FOR param IN lt_param_child_list
                                                                            WHERE ( node = /hec1/if_configuration_c=>sc_node-app_server )
                                                                                  ( key  = param-key ) )
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_server-app_storage
                                          IMPORTING et_data        = lt_app_storage ).

        INSERT LINES OF VALUE /bobf/t_frw_modification( FOR app_storage IN lt_app_storage
                                                        FOR phase IN lt_phase_generated
                                                        WHERE ( hec_node_phase = app_storage-hec_phase_guid )
                                                              ( node        = /hec1/if_configuration_c=>sc_node-phase
                                                                change_mode = /bobf/if_frw_c=>sc_modify_delete
                                                                key         = phase-key ) ) INTO TABLE rt_modification.

        APPEND LINES OF VALUE /bobf/t_frw_node( FOR app_storage IN lt_app_storage "#EC CI_APPEND_OK
                                                  ( node = /hec1/if_configuration_c=>sc_node-app_server
                                                    key  = app_storage-key ) ) TO lt_param_child_list.

      ENDIF.

      " ---------------
      " App Backup
      " ---------------
      IF line_exists( lt_param_child_list[ node = /hec1/if_configuration_c=>sc_node-app_storage ] ).
        " add children to lt_param_child_list

        "App Backup
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_storage
                                                    it_key         = VALUE #( FOR param IN lt_param_child_list
                                                                            WHERE ( node = /hec1/if_configuration_c=>sc_node-app_storage )
                                                                                  ( key  = param-key ) )
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_storage-app_storage_backup
                                          IMPORTING et_data        = lt_app_backup ).

        INSERT LINES OF VALUE /bobf/t_frw_modification( FOR app_backup IN lt_app_backup
                                                        FOR phase IN lt_phase_generated
                                                        WHERE ( hec_node_phase = app_backup-hec_phase_guid )
                                                              ( node        = /hec1/if_configuration_c=>sc_node-phase
                                                                change_mode = /bobf/if_frw_c=>sc_modify_delete
                                                                key         = phase-key ) ) INTO TABLE rt_modification.

        APPEND LINES OF VALUE /bobf/t_frw_node( FOR app_backup IN lt_app_backup "#EC CI_APPEND_OK
                                                  ( node = /hec1/if_configuration_c=>sc_node-app_storage_backup
                                                    key  = app_backup-key ) ) TO lt_param_child_list.

      ENDIF.

    ENDIF. " IF lt_phase_generated IS INITIAL.

  ENDMETHOD.


  METHOD get_phase_assignment.

    DATA: lt_root             TYPE /hec1/t_config_root_ct,
          lt_phase            TYPE /hec1/t_data_phase_ct,
          lt_datacenter       TYPE /hec1/t_data_datacenter_ct,
          lt_tier             TYPE /hec1/t_data_tier_ct,
          lt_db_serv_inst     TYPE /hec1/t_data_db_server_inst_ct,
          lt_inst_db          TYPE /hec1/t_data_db_inst_ct,
          lt_db_serv_pc       TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_storage_qty   TYPE /hec1/t_data_db_storage_qty_ct,
          lt_db_server        TYPE /hec1/t_data_db_serv_ct,
          lt_db_storage       TYPE /hec1/t_data_db_storage_ct,
          lt_db_backup        TYPE /hec1/t_data_db_backup_ct,
          lt_app_serv_inst    TYPE /hec1/t_data_app_serv_inst_ct,
          lt_app_serv_pc      TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_storage_qty  TYPE /hec1/t_data_app_storageqty_ct,
          lt_app_server       TYPE /hec1/t_data_app_serv_ct,
          lt_app_storage      TYPE /hec1/t_data_app_storage_ct,
          lt_app_backup       TYPE /hec1/t_data_app_backup_ct,

          lt_add_service      TYPE /hec1/t_data_add_services_ct,
          lt_tier_add_service TYPE /hec1/t_data_tier_add_serv_ct.

    "TODO, add missing nodes as well (additional services, storage, ...)

    io_read->get_root_key( EXPORTING iv_node         = iv_node_key
                                     it_key          = it_key
                           IMPORTING et_target_key   = DATA(lt_root_key) ).

    " Get Delivery Unit
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = lt_root_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-delivery_unit
                                      IMPORTING et_target_key  = DATA(lt_delivery_unit_key) ).

    " Get Datacenter
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-delivery_unit
                                                it_key         = lt_delivery_unit_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-delivery_unit-datacenter
                                      IMPORTING et_data        = lt_datacenter ).

  ENDMETHOD.


  METHOD do_currency_exchange.

    DATA: lv_foreign_factor TYPE ffact_curr,
          lv_local_factor   TYPE tfact_curr,
          lv_exchange_rate  TYPE ukurs_curr,
          lv_exchange_value TYPE /hec1/exchange_value,
          lv_type_of_rate   TYPE kurst_curr.

    DATA(lv_currency_from) = iv_currency_from.
    DATA(lv_currency_amount) = iv_currency_amount.
    DATA(lv_currency_to) = iv_currency_to.
    DATA(lv_date) = iv_date.

    CLEAR:  lv_foreign_factor, lv_local_factor, lv_exchange_rate, lv_exchange_value, ev_exchange_rate, ev_exchange_value, lv_type_of_rate.

    CHECK lv_currency_from IS NOT INITIAL.
    CHECK lv_currency_amount IS NOT INITIAL.
    CHECK lv_currency_to IS NOT INITIAL.
    CHECK lv_date IS NOT INITIAL.

*    lv_type_of_rate = 'M'. "Default
    lv_type_of_rate = 'FL01'. "#+ C5310379 30.09.2021

    CALL FUNCTION 'CONVERT_TO_LOCAL_CURRENCY'
      EXPORTING
*       client           = SY-MANDT
        date             = lv_date
        foreign_amount   = lv_currency_amount
        foreign_currency = lv_currency_from
        local_currency   = lv_currency_to
        type_of_rate     = lv_type_of_rate
      IMPORTING
        exchange_rate    = lv_exchange_rate
        foreign_factor   = lv_foreign_factor
        local_amount     = lv_exchange_value
        local_factor     = lv_local_factor
      EXCEPTIONS
        no_rate_found    = 1
        overflow         = 2
        no_factors_found = 3
        no_spread_found  = 4
        derived_2_times  = 5
        OTHERS           = 6.

    IF sy-subrc <> 0.
*     MESSAGE ID SY-MSGID TYPE SY-MSGTY NUMBER SY-MSGNO
*       WITH SY-MSGV1 SY-MSGV2 SY-MSGV3 SY-MSGV4.
    ENDIF.

    ev_exchange_rate = lv_exchange_rate.

    IF lv_foreign_factor > 1.
      ev_exchange_rate = lv_exchange_rate / lv_foreign_factor.
    ENDIF.

    IF lv_local_factor > 1.
      ev_exchange_rate = lv_exchange_rate * lv_local_factor.
    ENDIF.

    ev_exchange_value = lv_exchange_value.
  ENDMETHOD.


  METHOD get_root_node.

    DATA: lt_root     TYPE /hec1/t_config_root_ct.

    DATA(lv_root_key) = get_root_key( EXPORTING iv_node_key   = iv_node_key
                                                it_key        = it_key
                                                io_read       = io_read ).

    " Get root
    io_read->retrieve( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                 it_key         = VALUE #( ( key = lv_root_key ) )
                       IMPORTING et_data        = lt_root ).

    rs_root = VALUE #( lt_root[ 1 ] OPTIONAL ). "there is only always one root-line

  ENDMETHOD.


  METHOD create_cr_cms_case.
* C5310379: Commented out the code, because of structures from CMS-Case-Team are not existing in IST, have to wait for transport.
    DATA: lt_root TYPE /hec1/t_config_root_ct.

    DATA: ls_cms_header TYPE zzv_s_cms_hec_configurator,
          l_case_guid   TYPE  scmg_case_guid,
          l_case_num    TYPE  scmg_ext_key,
          lt_return     TYPE  bapiret2_tab,
          ls_return     TYPE  bapiret2.

    DATA: l_temp_cms_num TYPE n LENGTH 12.

    DATA: l_file_name TYPE sdok_titel.

*    DATA(lv_root_key) = get_root_key( EXPORTING iv_node_key   = iv_node_key
*                                                it_key        = it_key
*                                                io_read       = io_read
*                                      IMPORTING et_failed_key = et_failed_key ).
*
*    " Get Root data (root = landscape)
*    io_read->retrieve( EXPORTING iv_node = /hec1/if_configuration_c=>sc_node-root
*                                 it_key  = VALUE #( ( key = lv_root_key ) )
*                       IMPORTING et_data = lt_root                           ).
*
*
*
*    TRY.
*        DATA(ls_root) = lt_root[ 1 ].
*      CATCH cx_sy_itab_line_not_found .
*    ENDTRY.
*
*    CHECK ls_root IS NOT INITIAL.

    l_temp_cms_num = is_landscape-hec_ls_cms_case_id.

    ls_cms_header-linked_case_id = l_temp_cms_num.

    ls_cms_header-customer_id_erp = is_landscape-hec_businesspartner.
*  ls_cms_header-customer_id_hs = ls_root-HEC_LS_CRM_ACCOUNT_NUMBER.
*    ls_cms_header-sales_org = '0001'.

    CALL FUNCTION 'Z_V_CMS_INT_HEC_CASE_SYNC'
      EXPORTING
        is_header        = ls_cms_header                 " Input from Hec configurator
        hec_confid       = is_landscape-hec_confid                 " Configuration ID
        hec_conf_version = is_landscape-hec_conf_version                 " HEC
*       iv_doc_generate  = 'X'              " Boolean Variable (X = True, - = False, Space = Unknown)
*       iv_convert_pdf   = 'X'              " Boolean Variable (X = True, - = False, Space = Unknown)
      IMPORTING
        ev_case_guid     = l_case_guid                 " Technical Case Key (Case GUID)
        ev_case_num      = l_case_num                 " Case ID
      TABLES
        gt_return        = lt_return.                 " Return Parameter

    ev_cms_case_id = l_case_num.

*    /hec1/cl_config_form=>get_config_pdf(
*      EXPORTING
*        i_config_id      = is_landscape-hec_confid            " Configuration ID
*        i_config_version = is_landscape-hec_conf_version     " Configuration Version
*        i_doctype        = /hec1/cl_config_form=>c_doctype_handover  "C_DOCTYPE_PREVIEW
*      IMPORTING
*        e_pdf            = DATA(l_pdf)
*        e_file_size      = DATA(l_file_size)
**        et_tline         =                  " Text Lines
*      EXCEPTIONS
*        formatting_error = 1
*        OTHERS           = 2
*    ).
*
*    CLEAR: l_file_name.
*    CONCATENATE 'Config' is_landscape-hec_confid is_landscape-hec_conf_version INTO l_file_name SEPARATED BY '_'.
*
*    data: l_file_length type NUM12.
*    l_file_length = l_file_size.
*
*    CALL FUNCTION 'Z_V_CMS_INT_CLOUD_DOC_TRANSFER'
*      EXPORTING
*        iv_case_guid        = l_case_guid
*        iv_file_length      = l_file_length
*        iv_file_name        = l_file_name
*        iv_doc_category     = 'CMSD060600'
*        iv_doc_release      = '02'
*        iv_named_created_by = sy-uname
*        iv_bin_content      = l_pdf
*      IMPORTING
*        es_return           = ls_return.

  ENDMETHOD.


  METHOD set_cr_related_fields.

    rv_data_changed = abap_false. "Initialize data changed flag

    " Get ROOT node data from buffer for copying CR related fields
    DATA(ls_root) = /hec1/cl_config_helper=>get_root_node( EXPORTING iv_node_key = is_ctx-node_key
                                                                     it_key      = it_key
                                                                     io_read     = io_read
                                                                     io_modify   = io_modify    ).
    FIELD-SYMBOLS: <fs_config_cr> TYPE /hec1/s_config_change_request,
                   <fs_apm_guid>  TYPE /hec1/apm_guid,
                   <fs_apm_descr> TYPE /hec1/apm_descr,
                   <fs_phase>     TYPE /hec1/s_assignment_fields,
                   <fs_data>      TYPE any.


    "Set APM
    IF iv_set_apm = abap_true.
      ASSIGN is_node_data->* TO <fs_data>.
      IF sy-subrc = 0.
        ASSIGN COMPONENT 'HEC_APM_GUID' OF STRUCTURE <fs_data> TO <fs_apm_guid>.
        IF sy-subrc = 0.
          <fs_apm_guid> = ls_root-hec_apm_guid.
          ASSIGN COMPONENT 'HEC_APM_DESCR' OF STRUCTURE <fs_data> TO <fs_apm_descr>.
          IF sy-subrc = 0.
            <fs_apm_descr> = ls_root-hec_apm_descr.
          ENDIF.
        ENDIF.
      ENDIF.
    ENDIF.

    "Set CR Fields
    ASSIGN is_node_data->('CHANGE_REQUEST') TO <fs_config_cr>.
    IF ls_root IS NOT INITIAL AND sy-subrc = 0.
      " Copy CR related fields from the ROOT node
      <fs_config_cr>-hec_comp_cr_counter = ls_root-hec_cr_counter.
      <fs_config_cr>-hec_comp_cr_active = abap_true.
      <fs_config_cr>-hec_comp_mod_type = iv_mod_type.
      rv_data_changed = abap_true.
    ENDIF.

    "Clear Phase Defaults
    IF iv_clear_phase = abap_true.
      ASSIGN is_node_data->('ASSIGNMENT') TO <fs_phase>.
      IF ls_root IS NOT INITIAL AND sy-subrc = 0.
        " Copy CR related fields from the ROOT node
        CLEAR: <fs_phase>-hec_phase_guid,
               <fs_phase>-hec_phase_fixed,
               <fs_phase>-hec_phase_changed.
        rv_data_changed = abap_true.
      ENDIF.
    ENDIF.
  ENDMETHOD.


  METHOD get_apm_description.
    CLEAR rv_apm_descr.

    SELECT SINGLE hec_apm_descr FROM /hec1/a_model INTO @rv_apm_descr WHERE hec_apm_guid = @iv_apm_guid.
    IF ( sy-subrc <> 0 ).
      CLEAR rv_apm_descr.
    ENDIF.

  ENDMETHOD.


  METHOD convert_uidd_c26_2_key.

    CHECK iv_uidd_c26 IS NOT INITIAL.

    TRY.
        cl_system_uuid=>convert_uuid_c26_static( EXPORTING uuid     = iv_uidd_c26
                                                 IMPORTING uuid_x16 = rv_key      ).

      CATCH cx_uuid_error. " Error Class for UUID Processing Errors
    ENDTRY.


  ENDMETHOD.


  METHOD convert_key_2_uuid_c26.

    CHECK iv_key IS NOT INITIAL.

    TRY.
        cl_system_uuid=>convert_uuid_x16_static( EXPORTING uuid     = iv_key
                                                 IMPORTING uuid_c26 = rv_uuid_c26 ).

      CATCH cx_uuid_error. " Error Class for UUID Processing Errors
    ENDTRY.


  ENDMETHOD.


  METHOD convert_bopf_msg_to_fpm_msg.

    IF io_message IS BOUND.
      io_message->get_messages( IMPORTING et_message = DATA(lt_message) ).  " Table of msg instance that are contained in the msg object

      LOOP AT lt_message ASSIGNING FIELD-SYMBOL(<fs_message>).
        APPEND VALUE #( severity      = SWITCH #( <fs_message>-severity
                                                  WHEN 'I'
                                                  THEN 'W'
                                                  ELSE <fs_message>-severity )
                        message_index = sy-tabix
                        plaintext     = <fs_message>-message->get_message_id( ) ) TO rt_fpm_message.
      ENDLOOP.
    ENDIF.


  ENDMETHOD.


  METHOD check_apm_validity_by_grace_p.

    DATA ls_root TYPE  /hec1/s_config_root_cs.

    "Set the root node data
    ls_root = is_root.
    IF ls_root IS INITIAL.
      ls_root = /hec1/cl_bopf_config_model_fac=>get_instance( )->/hec1/if_bopf_config_model_get~get_root( ).
    ENDIF.

    CHECK ls_root-hec_flat_mat_guid IS NOT INITIAL.

    "if ct_apm_validity is initial, get the APM details for the current selected ROOT APM
    IF ct_apm_validity IS INITIAL  AND
          ls_root-hec_apm_guid IS NOT INITIAL.
      "Get APM Master data
      SELECT SINGLE *
          FROM /hec1/a_model
          INTO @DATA(ls_a_model)
          WHERE hec_apm_guid = @ls_root-hec_apm_guid.

      APPEND ls_a_model TO ct_apm_validity.
    ENDIF.

    "Get APM Grace Period details
    SELECT SINGLE *
        FROM /hec1/a_grace_p
        INTO @DATA(ls_grace_p)
        WHERE hec_flat_mat_guid = @ls_root-hec_flat_mat_guid.

    CHECK sy-subrc = 0.

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    " Check Validity for initial deal
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    IF ls_root-hec_contract_status = /hec1/if_config_constants=>gc_contract_status-initial OR
       ls_root-hec_contract_status IS INITIAL. "For previous configurations where contract status is not set to 01
      LOOP AT ct_apm_validity ASSIGNING FIELD-SYMBOL(<lfs_apm_validity>).
        "Add Grace period days to APM Validity End Date
        DATA lv_grc_period_date TYPE /hec1/apm_validity_end_date.
        lv_grc_period_date = sy-datum - ls_grace_p-hec_apm_id_grc_period_days.

        IF <lfs_apm_validity>-hec_validity_end_date <= lv_grc_period_date. "Not Valid anymore
          <lfs_apm_validity>-validity_level = /hec1/if_config_constants=>gc_msg_severity-error.
        ELSE. "Check if it is within the warning limit
          DATA lv_grc_period_wrn_date TYPE /hec1/apm_validity_end_date.
          lv_grc_period_wrn_date = sy-datum - ls_grace_p-hec_apm_id_grc_period_warn.
          IF <lfs_apm_validity>-hec_validity_end_date <= lv_grc_period_wrn_date.
            <lfs_apm_validity>-validity_level = /hec1/if_config_constants=>gc_msg_severity-warning.
            <lfs_apm_validity>-days_remaining = <lfs_apm_validity>-hec_validity_end_date - lv_grc_period_date.
          ELSE.
            <lfs_apm_validity>-validity_level = /hec1/if_config_constants=>gc_msg_severity-success.
            <lfs_apm_validity>-days_remaining = <lfs_apm_validity>-hec_validity_end_date - lv_grc_period_date.
          ENDIF.
        ENDIF.
      ENDLOOP.
    ENDIF.
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    " Check Validity for CR
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    IF ls_root-hec_contract_status = /hec1/if_config_constants=>gc_contract_status-change_request.
      LOOP AT ct_apm_validity ASSIGNING <lfs_apm_validity>.
        "Add Grace period days to APM Validity End Date
        lv_grc_period_date = sy-datum - ls_grace_p-hec_apm_cr_grc_period_days.

        IF <lfs_apm_validity>-hec_validity_end_date <= lv_grc_period_date. "Not Valid anymore
          <lfs_apm_validity>-validity_level = /hec1/if_config_constants=>gc_msg_severity-error.
        ELSE. "Check if it is within the warning limit
          lv_grc_period_wrn_date = sy-datum - ls_grace_p-hec_apm_cr_grc_period_warn.
          IF <lfs_apm_validity>-hec_validity_end_date <= lv_grc_period_wrn_date.
            <lfs_apm_validity>-validity_level = /hec1/if_config_constants=>gc_msg_severity-warning.
            <lfs_apm_validity>-days_remaining = <lfs_apm_validity>-hec_validity_end_date - lv_grc_period_date.
          ELSE.
            <lfs_apm_validity>-validity_level = /hec1/if_config_constants=>gc_msg_severity-success.
            <lfs_apm_validity>-days_remaining = <lfs_apm_validity>-hec_validity_end_date - lv_grc_period_date.
          ENDIF.
        ENDIF.
      ENDLOOP.
    ENDIF.
  ENDMETHOD.


  METHOD get_connectivity_description.
    SELECT  SINGLE hec_connectivity_descr
       FROM /hec1/i_connectivitybasic
       INTO @rv_connectivity_descr
      WHERE hec_connectivity_guid = @iv_connectivity_guid.
  ENDMETHOD.


  METHOD get_node_data_dynamic.

    DATA: lo_result_descriptor TYPE REF TO cl_abap_tabledescr,
          lr_data              TYPE REF TO data.

    FIELD-SYMBOLS        <lt_data> TYPE STANDARD TABLE.

    " Get node from lv_modify_action
    CLEAR: et_data.

    TRY.
        DATA(lo_bopf_config) = /bobf/cl_frw_factory=>get_configuration( /hec1/if_configuration_c=>sc_bo_key ).
      CATCH /bobf/cx_frw.
        RETURN. ">>>>>
    ENDTRY.

    " Get data type of current node
    lo_bopf_config->get_node( EXPORTING iv_node_key = iv_node
                              IMPORTING es_node     = DATA(ls_node_config) ).

    lo_result_descriptor ?= cl_abap_tabledescr=>describe_by_name( ls_node_config-data_table_type ).
    CREATE DATA lr_data TYPE HANDLE lo_result_descriptor.
    ASSIGN lr_data->* TO <lt_data>.

    " Get Data
    DATA(lo_service_manager) = /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key ).

    lo_service_manager->retrieve(
          EXPORTING
            iv_node_key             = iv_node
            it_key                  = VALUE #( ( key = iv_key ) )
          IMPORTING
            et_data                 = <lt_data>       ).

    IF <lt_data> IS ASSIGNED.
      et_data = <lt_data>.
    ENDIF.

  ENDMETHOD.


  METHOD get_parent_node_data_dynamic.

    DATA: lo_result_descriptor TYPE REF TO cl_abap_tabledescr,
          lr_data              TYPE REF TO data,
          r_node               TYPE REF TO cl_abap_structdescr.

    FIELD-SYMBOLS        <lt_data> TYPE STANDARD TABLE.

    " Get node from lv_modify_action
    CLEAR: et_data.

    TRY.
        DATA(lo_bopf_config) = /bobf/cl_frw_factory=>get_configuration( /hec1/if_configuration_c=>sc_bo_key ).
      CATCH /bobf/cx_frw.
        RETURN. ">>>>>
    ENDTRY.

    DATA(lo_service_manager) = /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key ).

    " Get config description of current node
    lo_bopf_config->get_node( EXPORTING iv_node_key = iv_node
                              IMPORTING es_node     = DATA(ls_node_config) ).

    " Get config description of parent node
    lo_bopf_config->get_node( EXPORTING iv_node_key = ls_node_config-parent_node_key
                              IMPORTING es_node     = DATA(ls_parent_node_config) ).

    " Get table of the type of the parent
    lo_result_descriptor ?= cl_abap_tabledescr=>describe_by_name( ls_parent_node_config-data_table_type ).
    CREATE DATA lr_data TYPE HANDLE lo_result_descriptor.
    ASSIGN lr_data->* TO <lt_data>.

    "IV_NODE is unfortunately a C32 BOPF-GUID. That's why we need to get the fieldname for that GUID.
    " for that we read the field names in the BOPF-Interface
    r_node ?= cl_abap_structdescr=>describe_by_data( /hec1/if_configuration_c=>sc_node ).
    LOOP AT r_node->components ASSIGNING FIELD-SYMBOL(<fs_node_components>).
      ASSIGN COMPONENT <fs_node_components>-name OF STRUCTURE /hec1/if_configuration_c=>sc_node TO FIELD-SYMBOL(<fs_node_value>).
      IF <fs_node_value> = iv_node.
        DATA(lv_node_field_desc) = <fs_node_components>-name.
        EXIT. ">>>>>>
      ENDIF.
    ENDLOOP.

    " Get Association 'TO_PARENT' from BOPF-Interface
    ASSIGN COMPONENT lv_node_field_desc OF STRUCTURE /hec1/if_configuration_c=>sc_association TO FIELD-SYMBOL(<fs_association>).

    IF <fs_association> IS ASSIGNED.
      ASSIGN COMPONENT 'TO_PARENT' OF STRUCTURE <fs_association> TO FIELD-SYMBOL(<fs_association_to_parent>).
      IF <fs_association_to_parent> IS ASSIGNED.

        " Get Data
        lo_service_manager->retrieve_by_association(
              EXPORTING
                iv_node_key             = iv_node
                iv_association          = <fs_association_to_parent>
                iv_fill_data            = abap_true
                it_key                  = VALUE #( ( key = iv_key ) )
              IMPORTING
                et_data                 = <lt_data>       ).

        IF <lt_data> IS ASSIGNED.
          et_data = <lt_data>.
        ENDIF.

      ENDIF.
    ENDIF.

  ENDMETHOD.
ENDCLASS.