CLASS /hec1/cl_config_validation DEFINITION
  PUBLIC
  INHERITING FROM /bobf/cl_lib_v_superclass
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.

    METHODS /bobf/if_frw_validation~execute
        REDEFINITION .
  PROTECTED SECTION.

private section.

  methods CHECK_APP_NODE_SYNC_CONFIG
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_VAL
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
    exporting
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
    changing
      !CO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE .
  methods CHECK_DELETE
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_VAL
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
    exporting
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
    changing
      !CO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE .
  methods CHECK_DB_NODE_SYNC_CONFIG
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_VAL
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
    exporting
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
    changing
      !CO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE .
  methods CHECK_PRICE_CHANGED
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_VAL
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
    exporting
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
    changing
      !CO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE .
  methods CHECK_TIER_NODE_CLIENTS
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_VAL
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
    exporting
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
    changing
      !CO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE .
  methods CHECK_TIER_SID_BLACKLIST
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_VAL
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
    exporting
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
    changing
      !CO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE .
ENDCLASS.



CLASS /HEC1/CL_CONFIG_VALIDATION IMPLEMENTATION.


  METHOD /bobf/if_frw_validation~execute.

    CLEAR: eo_message,
           et_failed_key.

    IF eo_message IS NOT BOUND.
      eo_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    TRY.
        CASE is_ctx-val_key.
            " ------------------------
            " Check pricing changes
            " ------------------------
          WHEN /hec1/if_configuration_c=>sc_validation-root-check_price_change.
            me->check_price_changed( EXPORTING is_ctx        = is_ctx
                                               it_key        = it_key
                                               io_read       = io_read
                                     IMPORTING et_failed_key = et_failed_key
                                     CHANGING  co_message    = eo_message    ).

            " ------------------------
            " Check Action App node
            " sync configuration
            " ------------------------
          WHEN /hec1/if_configuration_c=>sc_validation-app_node-check_sync_config.
            me->check_app_node_sync_config( EXPORTING is_ctx        = is_ctx
                                                      it_key        = it_key
                                                      io_read       = io_read
                                            IMPORTING et_failed_key = et_failed_key
                                            CHANGING  co_message    = eo_message    ).

            " ------------------------
            " Check Action DB node
            " sync configuration
            " ------------------------
          WHEN /hec1/if_configuration_c=>sc_validation-db_node-check_sync_config.
            me->check_db_node_sync_config( EXPORTING is_ctx        = is_ctx
                                                     it_key        = it_key
                                                     io_read       = io_read
                                           IMPORTING et_failed_key = et_failed_key
                                           CHANGING  co_message    = eo_message    ).
            " ------------------------
            " Check Action Tier node
            " check provided clients
            " ------------------------
          WHEN /hec1/if_configuration_c=>sc_validation-tier-check_tech_clients.
            me->check_tier_node_clients( EXPORTING is_ctx        = is_ctx
                                                     it_key        = it_key
                                                     io_read       = io_read
                                           IMPORTING et_failed_key = et_failed_key
                                           CHANGING  co_message    = eo_message    ).
            " ------------------------
            " Check Action Tier node
            " check SID blacklisting
            " ------------------------
          WHEN /hec1/if_configuration_c=>sc_validation-tier-check_sid_is_in_blacklist.
            me->check_tier_sid_blacklist( EXPORTING is_ctx        = is_ctx
                                                    it_key        = it_key
                                                    io_read       = io_read
                                          IMPORTING et_failed_key = et_failed_key
                                          CHANGING  co_message    = eo_message  ).

            " ------------------------
            " Delete Container
            " ------------------------
          WHEN /hec1/if_configuration_c=>sc_validation-root-check_delete.
            me->check_delete( EXPORTING is_ctx        = is_ctx
                                        it_key        = it_key
                                        io_read       = io_read
                              IMPORTING et_failed_key = et_failed_key
                              CHANGING  co_message    = eo_message  ).

        ENDCASE.
      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD check_price_changed.

    DATA: l_changed TYPE sap_bool.

    DATA: para              TYPE tpara-paramid VALUE '/HEC1/CONFIG_DEBUG',
          ls_debug_own_code TYPE /hec1/s_config_debug_modus.

    GET PARAMETER ID para FIELD ls_debug_own_code.


    "Safety first
    IF ls_debug_own_code-hec_debug_modus      = abap_true AND "Todo (remove before transport )
       ls_debug_own_code-hec_debuf_modus_vers = '09'.


      "-----------------------------------
      " Get all relevant nodes data with root key where
      " prices are stored for validation, if prices
      " have changed in the meanwhile
      "-----------------------------------

      /hec1/cl_config_helper=>get_price_relevant_node_data( EXPORTING is_ctx                   = CORRESPONDING #( is_ctx )
                                                                      it_key                   = it_key
                                                                      io_read                  = io_read
                                                            IMPORTING et_landscape             = DATA(lt_landscape)
                                                                      et_managed_serv_baseline = DATA(lt_man_serv_base)
                                                                      et_delivery_unit         = DATA(lt_delivery_unit)
                                                                      et_infra_struc_baseline  = DATA(lt_inf_base)
                                                                      et_connectivity          = DATA(lt_connectivity)
                                                                      et_add_service           = DATA(lt_add_service)
                                                                      et_tier                  = DATA(lt_tier)
                                                                      et_tier_add_service      = DATA(lt_tier_add_service)
                                                                      et_db_node               = DATA(lt_db_node)
                                                                      et_db_server             = DATA(lt_db_server)
                                                                      et_db_storage            = DATA(lt_db_storage)
                                                                      et_db_backup             = DATA(lt_db_backup)
                                                                      et_app_serv_perf_cat     = DATA(lt_app_serv_perf_cat)
                                                                      et_app_server            = DATA(lt_app_server)
                                                                      et_app_storage           = DATA(lt_app_storage)
                                                                      et_app_backup            = DATA(lt_app_backup)        ).

      READ TABLE lt_landscape INTO DATA(ls_landscape) INDEX 1.
      READ TABLE lt_delivery_unit INTO DATA(ls_delivery_unit) INDEX 1.

      "-----------------------------------
      " Loop at all relevant objects and get the legoblock-data from Database
      " Comparing of the price fields, if there is a difference in any object, loop will and and the validation is done
      " Due to the next step (update prices, where a full validation is done), there is no need to compare all items
      "-----------------------------------

*    et_failed_key = VALUE #( BASE et_failed_key ( key = ls_landscape-key ) ).
*    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_non_prod_tier_added
*                                                   iv_severity = /bobf/cm_frw=>co_severity_error
*                                                   iv_attr1    = CONV #( 'Test' )
*                                         CHANGING co_message   = co_message                                      ).


      "-----------------------------------
      " Managed service baseline
      "-----------------------------------
      LOOP AT lt_man_serv_base ASSIGNING FIELD-SYMBOL(<fs_man_serv_base>).

*        DATA(ls_man_serv_base_lb) = /hec1/cl_config_helper=>get_price_timebased_bb( iv_effort_bb_guid = <fs_man_serv_base>-hec_timebased_effort_bb_guid
*                                                                                    iv_root_key       = <fs_man_serv_base>-root_key
*                                                                                    io_read           = io_read                                         ).

        DATA(ls_man_serv_base_lb) = /hec1/cl_config_helper=>do_price_validation( iv_node_key          = is_ctx-node_key
                                                                                 it_key               = it_key
                                                                                 io_read              = io_read
                                                                                 iv_effort_bb_guid    = <fs_man_serv_base>-hec_timebased_effort_bb_guid
                                                                                 iv_tier_is_dr_node   = abap_false
                                                                                 iv_dr_operating_mode = ''                                              ).

        IF ls_man_serv_base_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: l_changed.

        IF <fs_man_serv_base>-hec_one_time_setup_effort    <> ls_man_serv_base_lb-hec_one_time_setup_effort.    l_changed = abap_true. ENDIF.
        IF <fs_man_serv_base>-hec_monthly_operating_effort <> ls_man_serv_base_lb-hec_monthly_operating_effort. l_changed = abap_true. ENDIF.
        IF <fs_man_serv_base>-hec_setup_rate               <> ls_man_serv_base_lb-hec_setup_rate.               l_changed = abap_true. ENDIF.
        IF <fs_man_serv_base>-hec_operation_rate           <> ls_man_serv_base_lb-hec_operation_rate.           l_changed = abap_true. ENDIF.
        IF <fs_man_serv_base>-hec_monthly_setup_fee        <> ls_man_serv_base_lb-hec_monthly_setup_fee.        l_changed = abap_true. ENDIF.
        IF <fs_man_serv_base>-hec_monthly_operation_fee    <> ls_man_serv_base_lb-hec_monthly_operation_fee.    l_changed = abap_true. ENDIF.

        IF l_changed = abap_true.
          et_failed_key = VALUE #( BASE et_failed_key ( key = <fs_man_serv_base>-key ) ).
          RETURN.
        ENDIF.

      ENDLOOP.


      "-----------------------------------
      " Infrastructure baseline
      "-----------------------------------
      LOOP AT lt_inf_base ASSIGNING FIELD-SYMBOL(<fs_inf_base>).

        DATA(ls_inf_base_lb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = <fs_inf_base>-hec_price_lb ).

        IF ls_inf_base_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: l_changed.

        IF <fs_inf_base>-hec_final_month_cost_eur <> ls_inf_base_lb-hec_final_month_cost_eur.   l_changed = abap_true. ENDIF.
        IF <fs_inf_base>-hec_cost_of_sales_eur    <> ls_inf_base_lb-hec_cost_of_sales_eur.      l_changed = abap_true. ENDIF.
        IF <fs_inf_base>-hec_margin_eur           <> ls_inf_base_lb-hec_margin_eur.             l_changed = abap_true. ENDIF.
        IF <fs_inf_base>-hec_month_price_eur      <> ls_inf_base_lb-hec_month_price_eur.        l_changed = abap_true. ENDIF.

        IF l_changed = abap_true.
          et_failed_key = VALUE #( BASE et_failed_key ( key = <fs_inf_base>-key ) ).
          RETURN.
        ENDIF.

      ENDLOOP.


      "-----------------------------------
      " Connectivity
      "-----------------------------------
      LOOP AT lt_connectivity ASSIGNING FIELD-SYMBOL(<fs_connectivity>).

        DATA(ls_connectivity_lb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = <fs_connectivity>-hec_price_lb ).

        IF ls_connectivity_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: l_changed.

        IF <fs_connectivity>-hec_final_month_cost_eur <> ls_connectivity_lb-hec_final_month_cost_eur.   l_changed = abap_true. ENDIF.
        IF <fs_connectivity>-hec_cost_of_sales_eur    <> ls_connectivity_lb-hec_cost_of_sales_eur.      l_changed = abap_true. ENDIF.
        IF <fs_connectivity>-hec_margin_eur           <> ls_connectivity_lb-hec_margin_eur.             l_changed = abap_true. ENDIF.
        IF <fs_connectivity>-hec_month_price_eur      <> ls_connectivity_lb-hec_month_price_eur.        l_changed = abap_true. ENDIF.

        IF l_changed = abap_true.
          et_failed_key = VALUE #( BASE et_failed_key ( key = <fs_connectivity>-key ) ).
          RETURN.
        ENDIF.

      ENDLOOP.


      "-----------------------------------
      " Additional Service
      "-----------------------------------
      LOOP AT lt_add_service ASSIGNING FIELD-SYMBOL(<fs_add_service>).

        DATA(ls_add_service_lb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = <fs_add_service>-hec_price_lb ).

        IF ls_add_service_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: l_changed.

        IF <fs_add_service>-hec_final_month_cost_eur <> ls_add_service_lb-hec_final_month_cost_eur.   l_changed = abap_true. ENDIF.
        IF <fs_add_service>-hec_cost_of_sales_eur    <> ls_add_service_lb-hec_cost_of_sales_eur.      l_changed = abap_true. ENDIF.
        IF <fs_add_service>-hec_margin_eur           <> ls_add_service_lb-hec_margin_eur.             l_changed = abap_true. ENDIF.
        IF <fs_add_service>-hec_month_price_eur      <> ls_add_service_lb-hec_month_price_eur.        l_changed = abap_true. ENDIF.

        IF l_changed = abap_true.
          et_failed_key = VALUE #( BASE et_failed_key ( key = <fs_add_service>-key ) ).
          RETURN.
        ENDIF.

      ENDLOOP.


      "-----------------------------------
      " Tier
      "-----------------------------------
      LOOP AT lt_tier ASSIGNING FIELD-SYMBOL(<fs_tier>).

*        DATA(ls_tier_lb) = /hec1/cl_config_helper=>get_price_timebased_bb( iv_effort_bb_guid = <fs_tier>-hec_timebased_effort_bb_guid
*                                                                           iv_root_key       = <fs_tier>-root_key
*                                                                           io_read           = io_read                                ).

        DATA(ls_tier_lb) = /hec1/cl_config_helper=>do_price_validation( iv_node_key          = is_ctx-node_key
                                                                        it_key               = it_key
                                                                        io_read              = io_read
                                                                        iv_effort_bb_guid    = <fs_tier>-hec_timebased_effort_bb_guid
                                                                        iv_tier_is_dr_node   = <fs_tier>-hec_tier_is_dr_node
                                                                        iv_dr_operating_mode = <fs_tier>-hec_dr_oper_mode_value ).

        IF ls_tier_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: l_changed.

        IF <fs_tier>-hec_one_time_setup_effort    <> ls_tier_lb-hec_one_time_setup_effort.    l_changed = abap_true. ENDIF.
        IF <fs_tier>-hec_monthly_operating_effort <> ls_tier_lb-hec_monthly_operating_effort. l_changed = abap_true. ENDIF.
        IF <fs_tier>-hec_setup_rate               <> ls_tier_lb-hec_setup_rate.               l_changed = abap_true. ENDIF.
        IF <fs_tier>-hec_operation_rate           <> ls_tier_lb-hec_operation_rate.           l_changed = abap_true. ENDIF.
        IF <fs_tier>-hec_monthly_setup_fee        <> ls_tier_lb-hec_monthly_setup_fee.        l_changed = abap_true. ENDIF.
        IF <fs_tier>-hec_monthly_operation_fee    <> ls_tier_lb-hec_monthly_operation_fee.    l_changed = abap_true. ENDIF.

        IF l_changed = abap_true.
          et_failed_key = VALUE #( BASE et_failed_key ( key = <fs_tier>-key ) ).
          RETURN.
        ENDIF.

      ENDLOOP.

      "-----------------------------------
      " Tier Additional Services - have no prices, only generates uplifts to the tier
      "-----------------------------------
      "LOOP AT lt_tier_add_service ASSIGNING FIELD-SYMBOL(<fs_tier_add_service>).
      "
      "  data(lt_tier_add_service_lb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = <fs_tier_add_service>-hec ).
      "
      "ENDLOOP.

      LOOP AT lt_db_node ASSIGNING FIELD-SYMBOL(<fs_db_node>).

*        DATA(ls_db_node_lb) = /hec1/cl_config_helper=>get_price_timebased_bb( iv_effort_bb_guid = <fs_db_node>-hec_timebased_effort_bb_guid
*                                                                              iv_root_key       = <fs_db_node>-root_key
*                                                                              io_read           = io_read                                   ).

        DATA(ls_db_node_lb) = /hec1/cl_config_helper=>do_price_validation( iv_node_key          = is_ctx-node_key
                                                                           it_key               = it_key
*                                                                           it_key               = VALUE #( ( key = lr_db_node->key ) )
                                                                           io_read              = io_read
                                                                           iv_effort_bb_guid    = <fs_db_node>-hec_timebased_effort_bb_guid
                                                                           iv_tier_is_dr_node   = <fs_db_node>-hec_tier_is_dr_node
                                                                           iv_dr_operating_mode = <fs_db_node>-hec_dr_oper_mode_value ).

        IF ls_db_node_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: l_changed.

        IF <fs_db_node>-hec_one_time_setup_effort    <> ls_db_node_lb-hec_one_time_setup_effort.    l_changed = abap_true. ENDIF.
        IF <fs_db_node>-hec_monthly_operating_effort <> ls_db_node_lb-hec_monthly_operating_effort. l_changed = abap_true. ENDIF.
        IF <fs_db_node>-hec_setup_rate               <> ls_db_node_lb-hec_setup_rate.               l_changed = abap_true. ENDIF.
        IF <fs_db_node>-hec_operation_rate           <> ls_db_node_lb-hec_operation_rate.           l_changed = abap_true. ENDIF.
        IF <fs_db_node>-hec_monthly_setup_fee        <> ls_db_node_lb-hec_monthly_setup_fee.        l_changed = abap_true. ENDIF.
        IF <fs_db_node>-hec_monthly_operation_fee    <> ls_db_node_lb-hec_monthly_operation_fee.    l_changed = abap_true. ENDIF.

        IF l_changed = abap_true.
          et_failed_key = VALUE #( BASE et_failed_key ( key = <fs_db_node>-key ) ).
          RETURN.
        ENDIF.

      ENDLOOP.

      LOOP AT lt_db_server ASSIGNING FIELD-SYMBOL(<fs_db_server>).

        DATA(ls_db_server_cblb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = <fs_db_server>-hec_price_lb ).

        IF ls_db_server_cblb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: l_changed.

        IF <fs_db_server>-hec_final_month_cost_eur <> ls_db_server_cblb-hec_final_month_cost_eur.   l_changed = abap_true. ENDIF.
        IF <fs_db_server>-hec_cost_of_sales_eur    <> ls_db_server_cblb-hec_cost_of_sales_eur.      l_changed = abap_true. ENDIF.
        IF <fs_db_server>-hec_margin_eur           <> ls_db_server_cblb-hec_margin_eur.             l_changed = abap_true. ENDIF.
        IF <fs_db_server>-hec_month_price_eur      <> ls_db_server_cblb-hec_month_price_eur.        l_changed = abap_true. ENDIF.

        IF l_changed = abap_true.
          et_failed_key = VALUE #( BASE et_failed_key ( key = <fs_db_server>-key ) ).
          RETURN.
        ENDIF.

      ENDLOOP.

      LOOP AT lt_db_storage ASSIGNING FIELD-SYMBOL(<fs_db_storage>).

        DATA(ls_db_storage_lb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = <fs_db_storage>-hec_price_lb ).

        IF ls_db_storage_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: l_changed.

        IF <fs_db_storage>-hec_final_month_cost_eur <> ls_db_storage_lb-hec_final_month_cost_eur.   l_changed = abap_true. ENDIF.
        IF <fs_db_storage>-hec_cost_of_sales_eur    <> ls_db_storage_lb-hec_cost_of_sales_eur.      l_changed = abap_true. ENDIF.
        IF <fs_db_storage>-hec_margin_eur           <> ls_db_storage_lb-hec_margin_eur.             l_changed = abap_true. ENDIF.
        IF <fs_db_storage>-hec_month_price_eur      <> ls_db_storage_lb-hec_month_price_eur.        l_changed = abap_true. ENDIF.

        IF l_changed = abap_true.
          et_failed_key = VALUE #( BASE et_failed_key ( key = <fs_db_storage>-key ) ).
          RETURN.
        ENDIF.

      ENDLOOP.

      LOOP AT lt_db_backup ASSIGNING FIELD-SYMBOL(<fs_db_backup>).

        DATA(ls_db_backup_lb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = <fs_db_backup>-hec_price_lb ).

        IF ls_db_backup_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: l_changed.

        IF <fs_db_backup>-hec_final_month_cost_eur <> ls_db_backup_lb-hec_final_month_cost_eur.   l_changed = abap_true. ENDIF.
        IF <fs_db_backup>-hec_cost_of_sales_eur    <> ls_db_backup_lb-hec_cost_of_sales_eur.      l_changed = abap_true. ENDIF.
        IF <fs_db_backup>-hec_margin_eur           <> ls_db_backup_lb-hec_margin_eur.             l_changed = abap_true. ENDIF.
        IF <fs_db_backup>-hec_month_price_eur      <> ls_db_backup_lb-hec_month_price_eur.        l_changed = abap_true. ENDIF.

        IF l_changed = abap_true.
          et_failed_key = VALUE #( BASE et_failed_key ( key = <fs_db_backup>-key ) ).
          RETURN.
        ENDIF.

      ENDLOOP.

      LOOP AT lt_app_serv_perf_cat ASSIGNING FIELD-SYMBOL(<fs_app_serv_perf_cat>).

*        DATA(ls_app_serv_pc_lb) = /hec1/cl_config_helper=>get_price_timebased_bb( iv_effort_bb_guid = <fs_app_serv_perf_cat>-hec_timebased_effort_bb_guid
*                                                                                  iv_root_key       = <fs_app_serv_perf_cat>-root_key
*                                                                                  io_read           = io_read                                             ).

        DATA(ls_app_serv_pc_lb) = /hec1/cl_config_helper=>do_price_validation( iv_node_key          = is_ctx-node_key
                                                                               it_key               = it_key
*                                                                               it_key               = VALUE #( ( key = lr_app_serv_perf_cat->key ) )
                                                                               io_read              = io_read
                                                                               iv_effort_bb_guid    = <fs_app_serv_perf_cat>-hec_timebased_effort_bb_guid
                                                                               iv_tier_is_dr_node   = <fs_app_serv_perf_cat>-hec_tier_is_dr_node
                                                                               iv_dr_operating_mode = <fs_app_serv_perf_cat>-hec_dr_oper_mode_value ).

        IF ls_app_serv_pc_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: l_changed.

        IF <fs_app_serv_perf_cat>-hec_one_time_setup_effort    <> ls_app_serv_pc_lb-hec_one_time_setup_effort.    l_changed = abap_true. ENDIF.
        IF <fs_app_serv_perf_cat>-hec_monthly_operating_effort <> ls_app_serv_pc_lb-hec_monthly_operating_effort. l_changed = abap_true. ENDIF.
        IF <fs_app_serv_perf_cat>-hec_setup_rate               <> ls_app_serv_pc_lb-hec_setup_rate.               l_changed = abap_true. ENDIF.
        IF <fs_app_serv_perf_cat>-hec_operation_rate           <> ls_app_serv_pc_lb-hec_operation_rate.           l_changed = abap_true. ENDIF.
        IF <fs_app_serv_perf_cat>-hec_monthly_setup_fee        <> ls_app_serv_pc_lb-hec_monthly_setup_fee.        l_changed = abap_true. ENDIF.
        IF <fs_app_serv_perf_cat>-hec_monthly_operation_fee    <> ls_app_serv_pc_lb-hec_monthly_operation_fee.    l_changed = abap_true. ENDIF.

        IF l_changed = abap_true.
          et_failed_key = VALUE #( BASE et_failed_key ( key = <fs_app_serv_perf_cat>-key ) ).
          RETURN.
        ENDIF.

      ENDLOOP.

      LOOP AT lt_app_server ASSIGNING FIELD-SYMBOL(<fs_app_server>).

        DATA(ls_app_server_lb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = <fs_app_server>-hec_price_lb ).

        IF ls_app_server_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: l_changed.

        IF <fs_app_server>-hec_final_month_cost_eur <> ls_app_server_lb-hec_final_month_cost_eur.   l_changed = abap_true. ENDIF.
        IF <fs_app_server>-hec_cost_of_sales_eur    <> ls_app_server_lb-hec_cost_of_sales_eur.      l_changed = abap_true. ENDIF.
        IF <fs_app_server>-hec_margin_eur           <> ls_app_server_lb-hec_margin_eur.             l_changed = abap_true. ENDIF.
        IF <fs_app_server>-hec_month_price_eur      <> ls_app_server_lb-hec_month_price_eur.        l_changed = abap_true. ENDIF.

        IF l_changed = abap_true.
          et_failed_key = VALUE #( BASE et_failed_key ( key = <fs_app_server>-key ) ).
          RETURN.
        ENDIF.

      ENDLOOP.

      LOOP AT lt_app_storage ASSIGNING FIELD-SYMBOL(<fs_app_storage>).

        DATA(ls_app_storage_lb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = <fs_app_storage>-hec_price_lb ).

        IF ls_app_storage_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: l_changed.

        IF <fs_app_storage>-hec_final_month_cost_eur <> ls_app_storage_lb-hec_final_month_cost_eur.   l_changed = abap_true. ENDIF.
        IF <fs_app_storage>-hec_cost_of_sales_eur    <> ls_app_storage_lb-hec_cost_of_sales_eur.      l_changed = abap_true. ENDIF.
        IF <fs_app_storage>-hec_margin_eur           <> ls_app_storage_lb-hec_margin_eur.             l_changed = abap_true. ENDIF.
        IF <fs_app_storage>-hec_month_price_eur      <> ls_app_storage_lb-hec_month_price_eur.        l_changed = abap_true. ENDIF.

        IF l_changed = abap_true.
          et_failed_key = VALUE #( BASE et_failed_key ( key = <fs_app_storage>-key ) ).
          RETURN.
        ENDIF.

      ENDLOOP.

      LOOP AT lt_app_backup ASSIGNING FIELD-SYMBOL(<fs_app_backup>).

        DATA(ls_app_backup_lb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = <fs_app_backup>-hec_price_lb ).

        IF ls_app_backup_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: l_changed.

        IF <fs_app_backup>-hec_final_month_cost_eur <> ls_app_backup_lb-hec_final_month_cost_eur.   l_changed = abap_true. ENDIF.
        IF <fs_app_backup>-hec_cost_of_sales_eur    <> ls_app_backup_lb-hec_cost_of_sales_eur.      l_changed = abap_true. ENDIF.
        IF <fs_app_backup>-hec_margin_eur           <> ls_app_backup_lb-hec_margin_eur.             l_changed = abap_true. ENDIF.
        IF <fs_app_backup>-hec_month_price_eur      <> ls_app_backup_lb-hec_month_price_eur.        l_changed = abap_true. ENDIF.

        IF l_changed = abap_true.
          et_failed_key = VALUE #( BASE et_failed_key ( key = <fs_app_backup>-key ) ).
          RETURN.
        ENDIF.

      ENDLOOP.

    ENDIF.

  ENDMETHOD.


  METHOD check_app_node_sync_config.

    " Get standby node: server performance category
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
                                      IMPORTING et_target_key  = DATA(lt_key)                                                             ).

    IF lt_key IS NOT INITIAL.
      et_failed_key = it_key.

      /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>sync_config_not_needed
                                                     iv_severity = /bobf/cm_frw=>co_severity_info
                                           CHANGING co_message   = co_message                                   ).
    ENDIF.


  ENDMETHOD.


  METHOD check_db_node_sync_config.

    " Get standby/worker node: server performance category
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                                      IMPORTING et_target_key  = DATA(lt_key)                                                             ).

    IF lt_key IS NOT INITIAL.
      et_failed_key = it_key.

      /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>sync_config_not_needed
                                                     iv_severity = /bobf/cm_frw=>co_severity_info
                                           CHANGING co_message   = co_message                                   ).
    ENDIF.


  ENDMETHOD.


  METHOD check_tier_node_clients.

    DATA:
        lt_tier_data                TYPE /hec1/t_data_tier_ct.

    io_read->retrieve(
      EXPORTING
        iv_node                 = /hec1/if_configuration_c=>sc_node-tier
        it_key                  = it_key
        iv_fill_data            = abap_true
      IMPORTING
        eo_message              = DATA(lo_message)
        et_data                 = lt_tier_data
        et_failed_key           = DATA(lt_failed_key)                   ).

    LOOP AT lt_tier_data ASSIGNING FIELD-SYMBOL(<fs_tier>).
      IF ( <fs_tier>-hec_tier_requ_client_def = '000' ).
        et_failed_key = it_key.

        " Default Client 000 is not allowed.
        /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>default_client_is_zero
                                                       iv_severity = /bobf/cm_frw=>co_severity_error
                                                       is_origin_location = VALUE #( bo_key   = is_ctx-bo_key
                                                                                     node_key = is_ctx-node_key
                                                                                     key      = it_key[ 1 ]-key
                                                                                     attributes = VALUE #( ( |HEC_TIER_REQU_CLIENT_DEF| ) ) )
                                              CHANGING co_message   = co_message                                   ).
        RETURN.
      ENDIF.


      DATA(lt_additional_clients) = /hec1/cl_prov_utility=>conv_csv_to_table( iv_csv = |{ <fs_tier>-hec_tier_requ_client_list }| ).

      LOOP AT lt_additional_clients ASSIGNING FIELD-SYMBOL(<fs_add_client>).
        IF ( <fs_add_client> = <fs_tier>-hec_tier_requ_client_def ).
          et_failed_key = it_key.

          " Default client should not be used under additional clients.
          /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>default_client_in_add_clients
                                                         iv_severity = /bobf/cm_frw=>co_severity_error
                                                         is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                       key      = it_key[ 1 ]-key )
                                                CHANGING co_message   = co_message                                   ).
          RETURN.
        ENDIF.
      ENDLOOP.
    ENDLOOP.

  ENDMETHOD.


  METHOD check_tier_sid_blacklist.

    DATA t_tier_data TYPE /hec1/t_data_tier_ct.

    io_read->retrieve(
      EXPORTING
        iv_node                 = /hec1/if_configuration_c=>sc_node-tier
        it_key                  = it_key
        iv_fill_data            = abap_true
      IMPORTING
        eo_message              = DATA(o_message)
        et_data                 = t_tier_data
        et_failed_key           = DATA(t_failed_key)                   ).

    LOOP AT t_tier_data ASSIGNING FIELD-SYMBOL(<s_tier>).
      IF /hec1/cl_customizing_utility=>is_sid_on_blacklist( <s_tier>-hec_tier_sid ).
        et_failed_key = it_key.

        " SID is not allowed
        /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>sid_blacklisted
                                                       iv_severity = /bobf/cm_frw=>co_severity_error
                                                       iv_attr1    = conv symsgv( <s_tier>-hec_tier_sid )
                                                       is_origin_location = VALUE #( bo_key     = is_ctx-bo_key
                                                                                     node_key   = is_ctx-node_key
                                                                                     key        = it_key[ 1 ]-key
                                                                                     attributes = VALUE #( ( |HEC_TIER_SID| ) ) )
                                              CHANGING co_message  = co_message ).
        RETURN.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD check_delete.

    DATA: ls_parameters      TYPE /hec1/s_act_delete_node,

          lt_solution_all    TYPE /hec1/t_data_solution_ct,
          lt_tier_all        TYPE /hec1/t_data_tier_ct,
          lt_db_si_all       TYPE /hec1/t_data_db_server_inst_ct,
          lt_instance_db_all TYPE /hec1/t_data_db_inst_ct.

    ASSIGN is_ctx-act_parameters->* TO FIELD-SYMBOL(<fs_parameters>).
    IF <fs_parameters> IS ASSIGNED.
      ls_parameters = <fs_parameters>.
    ENDIF.

    " At this point it_key is the root key, because the delete action runs on root level!!

    " The logic in this method needs to be reusable at a later point
    " The same logic applies when a reset or modify is performed on the corresponding nodes

    DATA(lv_node) = /hec1/cl_config_utilities=>get_node_key_by_object_type( iv_object_type = ls_parameters-node ).

    CASE lv_node.

      WHEN /hec1/if_configuration_c=>sc_node-solution
        OR /hec1/if_configuration_c=>sc_node-tier
        OR /hec1/if_configuration_c=>sc_node-db_server_instance
        OR /hec1/if_configuration_c=>sc_node-instance_db.

        " For these nodes it needs to be ensured that there is either no container
        " or that the container does not have other batches assigned.

        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                    it_key         = it_key
                                                    iv_association = /hec1/if_configuration_c=>sc_association-root-solution
                                                    iv_fill_data   = abap_true
                                          IMPORTING et_data        = lt_solution_all
                                                    et_target_key  = DATA(lt_solution_key) ).

        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-solution
                                                    it_key         = lt_solution_key
                                                    iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                                    iv_fill_data   = abap_true
                                          IMPORTING et_data        = lt_tier_all
                                                    et_target_key  = DATA(lt_tier_key) ).

        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                    it_key         = lt_tier_key
                                                    iv_association = /hec1/if_configuration_c=>sc_association-tier-db_server_instance
                                                    iv_fill_data   = abap_true
                                          IMPORTING et_data        = lt_db_si_all
                                                    et_target_key  = DATA(lt_db_si_key) ).

        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                    it_key         = lt_db_si_key
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-instance_db
                                                    iv_fill_data   = abap_true
                                          IMPORTING et_data        = lt_instance_db_all ).

        TRY.
            " Read the container. If there is no container underneath the current selection, this Validation stops and jumps to the catch (cx_sy_itab_line_not_found)
            " Depending on the selected node, different keys need to be used to read the container
            CASE lv_node.
              WHEN /hec1/if_configuration_c=>sc_node-solution.
                DATA(ls_instance_db_container) = lt_instance_db_all[ hec_node_solution      = lt_solution_all[ key = ls_parameters-key ]-hec_node_solution
                                                                     hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-container ].
              WHEN /hec1/if_configuration_c=>sc_node-tier.
                ls_instance_db_container = lt_instance_db_all[ hec_node_tier          = lt_tier_all[ key = ls_parameters-key ]-hec_node_tier
                                                               hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-container ].
              WHEN /hec1/if_configuration_c=>sc_node-db_server_instance.
                ls_instance_db_container = lt_instance_db_all[ hec_node_db_serv_inst  = lt_db_si_all[ key = ls_parameters-key ]-hec_node_db_serv_inst
                                                               hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-container ].
              WHEN /hec1/if_configuration_c=>sc_node-instance_db.
                ls_instance_db_container = lt_instance_db_all[ key                    = ls_parameters-key
                                                               hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-container ].
            ENDCASE.

            " Check if a tenant exists with the same multitenancy ID but a different parent
            LOOP AT lt_instance_db_all INTO DATA(ls_instance_db_tenant)
              WHERE hec_multi_tenant_rel_guid = ls_instance_db_container-hec_multi_tenant_rel_guid.

              " e.g if a solution is deleted that has 2 tiers containing the container and the tenant,
              " that solution can be deleted without issues, because all objects that are connected with the same multitenancy ID
              " are deleted together
              CASE lv_node.
                WHEN /hec1/if_configuration_c=>sc_node-solution.
                  IF ls_instance_db_tenant-hec_node_solution <> ls_instance_db_container-hec_node_solution.
                    DATA(lv_failed) = abap_true.
                  ENDIF.
                WHEN /hec1/if_configuration_c=>sc_node-tier.
                  IF ls_instance_db_tenant-hec_node_tier <> ls_instance_db_container-hec_node_tier.
                    lv_failed = abap_true.
                  ENDIF.
                WHEN /hec1/if_configuration_c=>sc_node-db_server_instance.
                  IF ls_instance_db_tenant-hec_node_db_serv_inst <> ls_instance_db_container-hec_node_db_serv_inst.
                    lv_failed = abap_true.
                  ENDIF.
                WHEN /hec1/if_configuration_c=>sc_node-instance_db.
                  lv_failed = abap_true.
              ENDCASE.

              IF lv_failed = abap_true.
                et_failed_key = it_key.
                /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>container_still_referenced
                                                               iv_severity = /bobf/cm_frw=>co_severity_info
                                                     CHANGING co_message   = co_message ).
                EXIT. ">>>>
              ENDIF. "lv_failed = abap_true.

            ENDLOOP.

          CATCH cx_sy_itab_line_not_found.
            " If there is no instance db with node type container, we can skip these checks.
            RETURN. ">>>>>
        ENDTRY.

    ENDCASE.

  ENDMETHOD.
ENDCLASS.