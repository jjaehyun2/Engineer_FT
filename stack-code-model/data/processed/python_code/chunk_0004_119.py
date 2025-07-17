CLASS /hec1/cl_config_det_db_server DEFINITION
  PUBLIC
  INHERITING FROM /hec1/cl_lib_d_superclass
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.
  PROTECTED SECTION.

    METHODS execute
        REDEFINITION .
    METHODS execute_tree
        REDEFINITION .
  PRIVATE SECTION.

    DATA mr_act_param TYPE REF TO data .
    DATA mr_act_param1 TYPE REF TO data .
    DATA mr_act_param_datac TYPE REF TO data .
    DATA mr_act_param_db_node TYPE REF TO data .
    DATA mr_act_param_db_storage_amount TYPE REF TO data .
    DATA mr_act_param_delete TYPE REF TO data .
    DATA mr_act_param_dlvy TYPE REF TO data .
    DATA mr_act_param_instance TYPE REF TO data .
    DATA mr_act_param_phasing TYPE REF TO data .
    DATA mr_act_param_tier_bck_amount TYPE REF TO data .

    METHODS determine_db_instance
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key
      RAISING
        /bobf/cx_frw .
    METHODS determine_db_instance_cr
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key
      RAISING
        /bobf/cx_frw .
    METHODS determine_db_node
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key
      RAISING
        /bobf/cx_frw .
    METHODS determine_db_node_cr
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key
      RAISING
        /bobf/cx_frw .
    METHODS determine_db_server
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key
      RAISING
        /bobf/cx_frw .
    METHODS determine_db_server_cr
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key
      RAISING
        /bobf/cx_frw .
    METHODS determine_db_server_instance
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key
      RAISING
        /bobf/cx_frw .
    METHODS determine_db_server_instanc_cr
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key
      RAISING
        /bobf/cx_frw .
    METHODS determine_db_server_pc_cr
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key
      RAISING
        /bobf/cx_frw .
    METHODS determine_db_server_perf_cat
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key
      RAISING
        /bobf/cx_frw .
    METHODS determine_db_storage
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key
      RAISING
        /bobf/cx_frw .
    METHODS determine_db_storage_cr
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key
      RAISING
        /bobf/cx_frw .
    METHODS determine_db_storage_amount
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key
      RAISING
        /bobf/cx_frw .
    METHODS determine_db_storage_amount_cr
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key
      RAISING
        /bobf/cx_frw .
    METHODS determine_db_storage_backup
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key
      RAISING
        /bobf/cx_frw .
    METHODS determine_db_storage_backup_cr
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key
      RAISING
        /bobf/cx_frw .
ENDCLASS.



CLASS /hec1/cl_config_det_db_server IMPLEMENTATION.


  METHOD determine_db_instance.

    DATA: lt_db_serv_inst       TYPE /hec1/t_data_db_server_inst_ct,
          lt_db_serv_inst_all   TYPE /hec1/t_data_db_server_inst_ct,
          lt_instance_db        TYPE /hec1/t_data_db_inst_ct,
          lt_instance_db_all    TYPE /hec1/t_data_db_inst_ct,
          lt_inst_db_before     TYPE /hec1/t_data_db_inst_ct,
          lt_tier               TYPE /hec1/t_data_tier_ct,
          lt_tier_all           TYPE /hec1/t_data_tier_ct,
          lt_act_param          TYPE /hec1/t_act_create_db_node,
          lt_act_param_instance TYPE /hec1/t_act_update_instance_db,
          lt_phase              TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing  TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    " Data before update
    io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                 it_key          = it_key
                                 iv_before_image = abap_true
                       IMPORTING et_data         = lt_inst_db_before ).

    " Data after update
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_instance_db ).


    " Get DB server instance
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-to_parent
                                      IMPORTING et_data        = lt_db_serv_inst
                                                et_target_key  = DATA(lt_db_serv_inst_key) ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-instance_db-create.

            " Get Tier
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                        it_key         = lt_db_serv_inst_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-to_parent
                                              IMPORTING et_data        = lt_tier
                                                        et_target_key  = DATA(lt_tier_key) ).

            " Get all tiers for multitenancy
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_false
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-solution
                                              IMPORTING et_target_key  = DATA(lt_solution_all_key) ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-solution
                                                        it_key         = lt_solution_all_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                              IMPORTING et_data        = lt_tier_all
                                                        et_target_key  = DATA(lt_tier_all_key) ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                        it_key         = lt_tier_all_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier-db_server_instance
                                              IMPORTING et_data        = lt_db_serv_inst_all
                                                        et_target_key  = DATA(lt_db_serv_inst_all_key) ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                        it_key         = lt_db_serv_inst_all_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-instance_db
                                              IMPORTING et_data        = lt_instance_db_all ).



            LOOP AT lt_instance_db REFERENCE INTO DATA(lr_instance_db).
              lr_instance_db->hec_delete_visible = abap_false.

              "-----------------------------------
              " Set Value List Quantity - Cluster Type
              "-----------------------------------
              lr_instance_db->hec_dbst_nodety_clust_ty_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_cluster_type(
                                                                                        iv_apm_guid                   = lr_landscape->hec_apm_guid
                                                                                        iv_sol_tier_dsi_dbstype_guid  = lr_instance_db->hec_sol_tier_dsi_dbstype_guid
                                                                                        iv_sol_dbst_alloc_nodety_guid = lr_instance_db->hec_sol_dbst_alloc_nodety_guid ) )
                                                                        THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                        ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_db_serv_inst[ key = lr_instance_db->parent_key ] TO FIELD-SYMBOL(<fs_db_serv_inst>).

              IF <fs_db_serv_inst>-hec_sol_tier_stack_si_guid     IS NOT INITIAL AND
                 <fs_db_serv_inst>-hec_sol_tier_dsi_dbstype_guid  IS NOT INITIAL AND
                 <fs_db_serv_inst>-hec_sol_dbst_oper_sys_guid     IS NOT INITIAL AND
                 <fs_db_serv_inst>-hec_sol_dbst_impltype_guid     IS NOT INITIAL AND
                 <fs_db_serv_inst>-hec_sol_dbst_impty_instty_guid IS NOT INITIAL AND
                 <fs_db_serv_inst>-hec_sol_dbst_imty_inty_al_guid IS NOT INITIAL AND
                 <fs_db_serv_inst>-hec_row_selectable = abap_true.
                DATA(lv_release) = abap_true.
              ENDIF.

              IF lv_release <> lr_instance_db->hec_row_selectable.
                lr_instance_db->hec_row_selectable = lv_release.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_instance_db->hec_dbst_nodety_clust_ty_guid IS NOT INITIAL AND
                                                                             lr_instance_db->hec_phase_guid                IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete    ).

              IF lv_inst_status <> lr_instance_db->hec_instance_status.
                lr_instance_db->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " instance DB action
              "-----------------------------------
              INSERT VALUE #( key                = lr_instance_db->key
                              parent_key         = lr_instance_db->parent_key
                              hec_cluster_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master
                              hec_def_master_node         = abap_true
                              hec_db_node_qty             = 1                                                       ) INTO TABLE lt_act_param.

              "-----------------------------------
              " Modify instance DB
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_instance_db->key
                                   is_data = lr_instance_db ).
              ENDIF.

              CLEAR: lv_release,
                     lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_db_serv_inst>.
            ENDLOOP.

            "-----------------------------------
            " Set create DB node action
            " to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_db_node( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_node )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                ).

            ENDIF.

            "-----------------------------------
            " Set Update Instance DB action
            " to general
            "-----------------------------------
            IF lt_act_param_instance IS NOT INITIAL.
              CLEAR me->mr_act_param_instance.
              me->mr_act_param_instance = NEW /hec1/t_act_update_instance_db( lt_act_param_instance ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_instance_db )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_instance                                                                                                                ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-instance_db-update.

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).


            LOOP AT lt_instance_db REFERENCE INTO lr_instance_db.

              ASSIGN lt_inst_db_before[ key = lr_instance_db->key ] TO FIELD-SYMBOL(<fs_inst_db_before>).
              IF <fs_inst_db_before> IS ASSIGNED.
                lr_instance_db->hec_delete_visible = abap_false.

                "-----------------------------------
                " Value List Quanitty
                "-----------------------------------
                "  Cluster Type
                IF lr_instance_db->hec_dbst_nodety_clust_ty_guid <> <fs_inst_db_before>-hec_dbst_nodety_clust_ty_guid.
                  lr_instance_db->hec_dbst_nodety_clust_ty_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_cluster_type(
                                                                                            iv_apm_guid                   = lr_landscape->hec_apm_guid
                                                                                            iv_sol_tier_dsi_dbstype_guid  = lr_instance_db->hec_sol_tier_dsi_dbstype_guid
                                                                                            iv_sol_dbst_alloc_nodety_guid = lr_instance_db->hec_sol_dbst_alloc_nodety_guid ) )
                                                                            THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                            ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                  lv_data_changed = abap_true.

                ENDIF. "cluster type has changed

                " HEC_DB_HSR_OP_MODE_VALUE
                IF lr_instance_db->hec_db_hsr_op_mode_value <> <fs_inst_db_before>-hec_db_hsr_op_mode_value.
                  lr_instance_db->hec_db_hsr_op_mode_vlqt = COND #( WHEN 1 < lines( /rbp/cl_fpm_utilities=>get_characteristic_values( CONV #( 'HEC_DB_HSR_OP_MODE_VALUE' ) ) )
                                                                    THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                    ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).
                ENDIF.

                "-----------------------------------
                " Master, standby or
                " worker node is added
                "-----------------------------------
                IF lr_instance_db->hec_dbst_nodety_clust_ty_guid = <fs_inst_db_before>-hec_dbst_nodety_clust_ty_guid AND
                  ( lr_instance_db->hec_db_master_node_qty  <> <fs_inst_db_before>-hec_db_master_node_qty  OR
                    lr_instance_db->hec_db_standby_node_qty <> <fs_inst_db_before>-hec_db_standby_node_qty OR
                    lr_instance_db->hec_db_worker_node_qty  <> <fs_inst_db_before>-hec_db_worker_node_qty     ).
                  "-----------------------------------
                  " Non default master node
                  "-----------------------------------
                  IF lr_instance_db->hec_db_master_node_qty > <fs_inst_db_before>-hec_db_master_node_qty.
                    " Add non default master node to action table
                    INSERT VALUE #( key                         = lr_instance_db->key
                                    parent_key                  = lr_instance_db->parent_key
                                    hec_cluster_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master
                                    hec_def_master_node         = abap_false
                                    hec_db_node_qty             = lr_instance_db->hec_db_master_node_qty - <fs_inst_db_before>-hec_db_master_node_qty ) INTO TABLE lt_act_param.

                    " Success message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_master_node_added
                                                                   iv_severity = /bobf/cm_frw=>co_severity_success
                                                                   iv_attr1    = CONV #( lr_instance_db->hec_db_master_node_qty -
                                                                                 <fs_inst_db_before>-hec_db_master_node_qty )
                                                         CHANGING  co_message  = eo_message ).

                  ELSEIF lr_instance_db->hec_db_master_node_qty < <fs_inst_db_before>-hec_db_master_node_qty.
                    DATA(lv_attr_name) = /hec1/if_configuration_c=>sc_node_attribute-instance_db-hec_db_master_node_qty.

                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_instance_db->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_instance_db->hec_db_master_node_qty = <fs_inst_db_before>-hec_db_master_node_qty.
                    lv_data_changed = abap_true.

                  ELSEIF lr_instance_db->hec_db_master_node_limit_qty < lr_instance_db->hec_db_master_node_limit_qty.
                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>node_limit_is_exceeded
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_instance_db->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_instance_db->hec_db_master_node_qty = <fs_inst_db_before>-hec_db_master_node_qty.
                    lv_data_changed = abap_true.
                  ENDIF. " IF lr_instance_db->hec_db_master_node_qty > <fs_inst_db_before>-hec_db_master_node_qty.


                  "-----------------------------------
                  " Standby node
                  "-----------------------------------
                  IF lr_instance_db->hec_db_standby_node_qty > <fs_inst_db_before>-hec_db_standby_node_qty.
                    " Add non default master node to action table
                    INSERT VALUE #( key                         = lr_instance_db->key
                                    parent_key                  = lr_instance_db->parent_key
                                    hec_cluster_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-standby
                                    hec_def_master_node         = abap_false
                                    hec_db_node_qty             = lr_instance_db->hec_db_standby_node_qty - <fs_inst_db_before>-hec_db_standby_node_qty ) INTO TABLE lt_act_param.

                    " Success message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_standby_node_added
                                                                   iv_severity = /bobf/cm_frw=>co_severity_success
                                                                   iv_attr1    = CONV #( lr_instance_db->hec_db_standby_node_qty -
                                                                                 <fs_inst_db_before>-hec_db_standby_node_qty )
                                                         CHANGING  co_message  = eo_message ).

                  ELSEIF lr_instance_db->hec_db_standby_node_qty < <fs_inst_db_before>-hec_db_standby_node_qty.
                    lv_attr_name = /hec1/if_configuration_c=>sc_node_attribute-instance_db-hec_db_standby_node_qty.

                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_instance_db->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_instance_db->hec_db_standby_node_qty = <fs_inst_db_before>-hec_db_standby_node_qty.
                    lv_data_changed = abap_true.

                  ELSEIF lr_instance_db->hec_db_standby_node_limit_qty < lr_instance_db->hec_db_standby_node_limit_qty.
                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>node_limit_is_exceeded
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_instance_db->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_instance_db->hec_db_standby_node_qty = <fs_inst_db_before>-hec_db_standby_node_qty.
                    lv_data_changed = abap_true.
                  ENDIF. " IF lr_instance_db->hec_db_standby_node_qty > <fs_inst_db_before>-hec_db_standby_node_qty.

                  "-----------------------------------
                  " Worker node
                  "-----------------------------------
                  IF lr_instance_db->hec_db_worker_node_qty > <fs_inst_db_before>-hec_db_worker_node_qty.
                    " Add non default master node to action table
                    INSERT VALUE #( key                         = lr_instance_db->key
                                    parent_key                  = lr_instance_db->parent_key
                                    hec_cluster_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-worker
                                    hec_def_master_node         = abap_false
                                    hec_db_node_qty             = lr_instance_db->hec_db_worker_node_qty - <fs_inst_db_before>-hec_db_worker_node_qty ) INTO TABLE lt_act_param.

                    " Success message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_worker_node_added
                                                                   iv_severity = /bobf/cm_frw=>co_severity_success
                                                                   iv_attr1    = CONV #( lr_instance_db->hec_db_worker_node_qty -
                                                                                 <fs_inst_db_before>-hec_db_worker_node_qty )
                                                         CHANGING  co_message  = eo_message ).

                  ELSEIF lr_instance_db->hec_db_worker_node_qty < <fs_inst_db_before>-hec_db_worker_node_qty.
                    lv_attr_name = /hec1/if_configuration_c=>sc_node_attribute-instance_db-hec_db_worker_node_qty.

                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_instance_db->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_instance_db->hec_db_worker_node_qty = <fs_inst_db_before>-hec_db_worker_node_qty.
                    lv_data_changed = abap_true.

                  ELSEIF lr_instance_db->hec_db_worker_node_limit_qty < lr_instance_db->hec_db_worker_node_limit_qty.
                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>node_limit_is_exceeded
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_instance_db->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_instance_db->hec_db_worker_node_qty = <fs_inst_db_before>-hec_db_worker_node_qty.
                    lv_data_changed = abap_true.
                  ENDIF. " IF lr_instance_db->hec_db_worker_node_qty > <fs_inst_db_before>-hec_db_worker_node_qty.

                  CLEAR lv_attr_name.
                ENDIF. " IF lr_instance_db->hec_db_cluster_type_guid = <fs_inst_db_before>-hec_db_cluster_type_guid     AND...

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_instance_db->hec_phase_guid NE <fs_inst_db_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_instance_db->key
                                  hec_phase_guid_new = lr_instance_db->hec_phase_guid
                                  hec_phase_guid_old = <fs_inst_db_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_instance_db->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "phasing changed
              ENDIF. " IF <fs_inst_db_before> IS ASSIGNED.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_instance_db->hec_dbst_nodety_clust_ty_guid IS NOT INITIAL AND
                                                                       lr_instance_db->hec_phase_guid                IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete          ).

              IF lv_inst_status <> lr_instance_db->hec_instance_status.
                lr_instance_db->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify instance DB
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_instance_db->key
                                   is_data = lr_instance_db ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_inst_db_before>.
            ENDLOOP.


            "-----------------------------------
            " Set create DB node action to
            " general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param_db_node.
              me->mr_act_param_db_node = NEW /hec1/t_act_create_db_node( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = CORRESPONDING #( is_ctx )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param
                                              ( key = wa_act_node-key )        )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_db_node                                                                                                       ).
            ENDIF.


            "-----------------------------------
            " Set update Phasing action to
            " general
            "-----------------------------------
            IF lt_act_param_phasing IS NOT INITIAL.
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.


            " **********************************
            " Update mode after DB server
            " instance update
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-instance_db-update_after_server_instance.

            LOOP AT lt_instance_db REFERENCE INTO lr_instance_db.
              ASSIGN lt_db_serv_inst[ key = lr_instance_db->parent_key ] TO <fs_db_serv_inst>.

              IF <fs_db_serv_inst> IS ASSIGNED.
                "-----------------------------------
                " Release instance for selection
                "-----------------------------------
                IF <fs_db_serv_inst>-hec_sol_tier_stack_si_guid     IS NOT INITIAL AND
                   <fs_db_serv_inst>-hec_sol_tier_dsi_dbstype_guid  IS NOT INITIAL AND
                   <fs_db_serv_inst>-hec_sol_dbst_oper_sys_guid     IS NOT INITIAL AND
                   <fs_db_serv_inst>-hec_sol_dbst_impltype_guid     IS NOT INITIAL AND
                   <fs_db_serv_inst>-hec_sol_dbst_impty_instty_guid IS NOT INITIAL AND
                   <fs_db_serv_inst>-hec_sol_dbst_imty_inty_al_guid IS NOT INITIAL AND
                   <fs_db_serv_inst>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.

                IF lv_release <> lr_instance_db->hec_row_selectable.
                  lr_instance_db->hec_row_selectable = lv_release.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Modify instance DB
                "-----------------------------------
                IF lv_data_changed = abap_true.
                  io_modify->update( iv_node = is_ctx-node_key
                                     iv_key  = lr_instance_db->key
                                     is_data = lr_instance_db ).
                ENDIF.
              ENDIF. " IF <fs_db_serv_inst> IS ASSIGNED.

              UNASSIGN <fs_db_serv_inst>.
              CLEAR: lv_release,
                     lv_data_changed.

            ENDLOOP. " LOOP AT lt_instance_db...
        ENDCASE.
      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_db_node.

    DATA: lt_instance_db       TYPE /hec1/t_data_db_inst_ct,
          lt_db_node_all       TYPE /hec1/t_data_db_node_ct,
          lt_db_node           TYPE /hec1/t_data_db_node_ct,
          lt_db_node_before    TYPE /hec1/t_data_db_node_ct,
          lt_db_serv_perf_cat  TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_storage_qty    TYPE /hec1/t_data_db_storage_qty_ct,
          lt_db_serv_pc        TYPE /hec1/t_data_db_serv_pc_ct,
          lt_node_key          TYPE /bobf/t_frw_key,
          lt_act_param         TYPE /hec1/t_act_create_db_spc,
          lt_act_param_node    TYPE /hec1/t_act_update_db_node,
          lt_phase             TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    " Get data after update
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_node ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_node-create.
            " Get instance DB node (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_node-to_parent
                                              IMPORTING et_data        = lt_instance_db ).

            " DB master node
            LOOP AT        lt_db_node
            REFERENCE INTO DATA(lr_db_node)
                    WHERE hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master.

              "TODO this needs a more complex logic
              lr_db_node->hec_delete_visible = abap_false.

              "-----------------------------------
              " Check and switch instance status
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_db_node->hec_db_srv_perf_cat_qty IS NOT INITIAL AND
                                                                             lr_db_node->hec_phase_guid          IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete    ).

              IF lv_inst_status <> lr_db_node->hec_instance_status.
                lr_db_node->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_instance_db[ key = lr_db_node->parent_key ] TO FIELD-SYMBOL(<fs_instance_db>).
              IF <fs_instance_db> IS ASSIGNED.
                IF <fs_instance_db>-hec_db_cluster_type_guid IS NOT INITIAL AND
                   <fs_instance_db>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lr_db_node->hec_row_selectable <> lv_release.
                lr_db_node->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " DB server performance category
              "-----------------------------------
              IF NOT ( lr_db_node->hec_server_required    = abap_false AND
                       lr_db_node->hec_db_impl_type_value = '01'           ).  " Implementation type <> Dedicated
                INSERT VALUE #( key            = lr_db_node->key
                                parent_key     = lr_db_node->parent_key
                                hec_db_srv_perf_cat_qty = lr_db_node->hec_db_srv_perf_cat_qty ) INTO TABLE lt_act_param.
              ENDIF.

              "-----------------------------------
              " Modify DB server node
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_node->key
                                   is_data = lr_db_node ).
              ENDIF.

              UNASSIGN <fs_instance_db>.
              CLEAR: lv_inst_status,
                     lv_release,
                     lv_data_changed.
            ENDLOOP.


            "-----------------------------------
            " DB standby/worker node
            "-----------------------------------
            LOOP AT        lt_db_node
            REFERENCE INTO lr_db_node
                     WHERE ( hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha    OR
                             hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi           ) AND
                           ( hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-standby OR
                             hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-worker     ).

              lr_db_node->hec_delete_visible = abap_false.

              "-----------------------------------
              " Check and switch instance status
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_db_node->hec_db_srv_perf_cat_qty IS NOT INITIAL AND
                                                                       lr_db_node->hec_phase_guid          IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete    ).

              IF lv_inst_status <> lr_db_node->hec_instance_status.
                lr_db_node->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Release selection standby/worker
              " node
              "-----------------------------------
              " Check default master node is complete configered
              " ( including sub nodes: server performance category and storage amount )
              DATA(lv_complete) = /hec1/cl_bopf_config_validat_h=>check_master_node_is_complete( iv_check_rule = /hec1/if_bopf_constants=>gc_check_rule-node
                                                                                                 is_ctx        = is_ctx
                                                                                                 it_key        = VALUE #( ( key = lr_db_node->key ) )
                                                                                                 io_read       = io_read ).

              IF ( lv_complete                    = abap_true AND
                   lr_db_node->hec_row_selectable = abap_false    ) OR
                 ( lv_complete                    = abap_false AND
                   lr_db_node->hec_row_selectable = abap_true     ).

                lr_db_node->hec_row_selectable = COND #( WHEN lv_complete = abap_true
                                                         THEN abap_true
                                                         ELSE abap_false              ).
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify DB standby/worker node
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_node->key
                                   is_data = lr_db_node ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_complete,
                     lv_data_changed.
            ENDLOOP.


            "-----------------------------------
            " Set create DB server performance
            " category action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_spc( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_spc )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                              ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_node-update.

            " Get data before update
            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_db_node_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                                              IMPORTING et_data        = lt_db_serv_pc ).



            LOOP AT lt_db_node REFERENCE INTO lr_db_node.

              ASSIGN lt_db_node_before[ key = lr_db_node->key ] TO FIELD-SYMBOL(<fs_db_node_before>).
              IF <fs_db_node_before> IS ASSIGNED.
                "-----------------------------------
                " Fill action table for create
                " DB server performance category
                " for master node
                "-----------------------------------
                IF lr_db_node->hec_db_srv_perf_cat_qty > <fs_db_node_before>-hec_db_srv_perf_cat_qty.
                  " Only for master node
                  IF lr_db_node->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master.
                    INSERT VALUE #( key            = lr_db_node->key
                                    parent_key     = lr_db_node->parent_key
                                    hec_db_srv_perf_cat_qty = lr_db_node->hec_db_srv_perf_cat_qty - <fs_db_node_before>-hec_db_srv_perf_cat_qty ) INTO TABLE lt_act_param.

                    " Success message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_serv_perf_cat_added
                                                                   iv_severity = /bobf/cm_frw=>co_severity_success
                                                                   iv_attr1    = CONV #( lr_db_node->hec_db_srv_perf_cat_qty -
                                                                                 <fs_db_node_before>-hec_db_srv_perf_cat_qty )
                                                         CHANGING  co_message  = eo_message ).

                    " Set flag for deleting subnodes of standby/worker node
                    IF ( lr_db_node->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                         lr_db_node->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi   )   AND
                         lr_db_node->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                         lr_db_node->hec_master_default            = abap_true.
                      lv_data_changed         = abap_true.
                      DATA(lv_delete_subnode) = abap_true.
                    ENDIF.
                  ENDIF. " IF lr_db_node->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master.
                ELSEIF lr_db_node->hec_db_srv_perf_cat_qty < <fs_db_node_before>-hec_db_srv_perf_cat_qty
                   AND lr_db_node->hec_db_srv_perf_cat_qty < lines( VALUE /hec1/t_data_db_serv_pc_ct( FOR db_serv_pc IN lt_db_serv_pc
                                                                                                      WHERE ( parent_key = lr_db_node->key )
                                                                                                      ( db_serv_pc )                         ) ).

                  DATA(lv_attr_name) = /hec1/if_configuration_c=>sc_node_attribute-db_node-hec_db_srv_perf_cat_qty.

                  " Error message
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                 is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                               key      = lr_db_node->key
                                                                                               attributes = VALUE #( ( lv_attr_name ) ) )
                                                       CHANGING  co_message         = eo_message ).

                  " Set node number to value before update
                  lr_db_node->hec_db_srv_perf_cat_qty = <fs_db_node_before>-hec_db_srv_perf_cat_qty.
                  lv_data_changed = abap_true.
                ENDIF. " IF lr_db_node->hec_dn_srv_perf_cat_qty > <fs_db_node_before>-hec_dn_srv_perf_cat_qty.

                "-----------------------------------
                " Fill action table for update
                " phasing
                "-----------------------------------
                IF lr_db_node->hec_phase_guid NE <fs_db_node_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_db_node->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                     lr_db_node->hec_master_default           = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_db_node->key
                                    hec_phase_guid_new = lr_db_node->hec_phase_guid
                                    hec_phase_guid_old = <fs_db_node_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_db_node->hec_phase_changed = abap_true.
                  lv_data_changed               = abap_true.

                  " Set flag for deleting subnodes of standby/worker node
                  IF lr_db_node->hec_db_cluster_type_value = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                     lr_db_node->hec_db_cluster_type_value = /hec1/if_config_constants=>gc_db_clust_node-multi.
                    lv_delete_subnode = abap_true.
                  ENDIF.
                ENDIF. "phasing changed
              ENDIF. " IF <fs_db_node_before> IS ASSIGNED.


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_db_node->hec_db_srv_perf_cat_qty IS NOT INITIAL AND
                                                                       lr_db_node->hec_phase_guid          IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_db_node->hec_instance_status.
                lr_db_node->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Fill action table for delete
              " subnodes of DB standby/worker node
              " or relase standby/worker node
              "-----------------------------------
              IF ( lr_db_node->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                   lr_db_node->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi   )   AND
                   lr_db_node->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                   lr_db_node->hec_master_default            = abap_true                                              AND
                   lv_data_changed                           = abap_true.

                IF NOT line_exists( lt_act_param_node[ key = lr_db_node->key ] ).
                  INSERT VALUE #( key               = lr_db_node->key
                                  parent_key        = lr_db_node->parent_key
                                  do_release_node   = COND #( WHEN lr_db_node->hec_instance_status         = /hec1/if_config_constants=>gc_instance_status-complete   AND
                                                                   <fs_db_node_before>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                              THEN abap_true
                                                               ELSE abap_false                                                  )
                                  do_delete_subnode = COND #( WHEN lr_db_node->hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete OR
                                                                   lv_delete_subnode               = abap_true
                                                              THEN abap_true
                                                              ELSE abap_false                                                                                     ) ) INTO TABLE lt_act_param_node.
                ENDIF.
              ENDIF. " IF ( lr_db_node->hec_db_cluster_type_value = /hec1/if_config_constants=>gc_db_clust_node-ha   OR...


              "-----------------------------------
              " Modify DB node
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_node->key
                                   is_data = lr_db_node ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_attr_name,
                     lv_delete_subnode.

              UNASSIGN <fs_db_node_before>.
            ENDLOOP.

            "-----------------------------------
            " Set create DB server performance
            " category action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_db_spc( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_spc )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                              ).

            ENDIF.

            "-----------------------------------
            " Set update phasing action to
            " general
            "-----------------------------------
            IF lt_act_param_phasing IS NOT INITIAL.
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.


            "-----------------------------------
            " Set update DB node action to
            " general
            "-----------------------------------
            IF lt_act_param_node IS NOT INITIAL.
              CLEAR me->mr_act_param_db_node.
              me->mr_act_param_db_node = NEW /hec1/t_act_update_db_node( lt_act_param_node ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-db_node )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param_node
                                              ( key = wa_act_node-key )     )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_db_node                                                                                                       ).
            ENDIF.


            " **********************************
            " Update mode after instance DB
            " update
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_node-update_after_instance_db.
            " Get instance DB
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_node-to_parent
                                              IMPORTING et_data        = lt_instance_db ).


            LOOP AT lt_db_node REFERENCE INTO lr_db_node.
              ASSIGN lt_instance_db[ key = lr_db_node->parent_key ] TO <fs_instance_db>.

              IF <fs_instance_db> IS ASSIGNED.
                IF <fs_instance_db>-hec_db_cluster_type_guid IS NOT INITIAL AND
                   <fs_instance_db>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              " Release instance for selection
              IF lr_db_node->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                 lv_release <> lr_db_node->hec_row_selectable.
                lr_db_node->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              " Release instance for selection( standby/worker node)
              IF ( lr_db_node->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-standby OR
                   lr_db_node->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-worker     ) AND
                 /hec1/cl_bopf_config_validat_h=>check_standby_node_is_released( iv_check_rule = /hec1/if_bopf_constants=>gc_check_rule-node
                                                                                 is_ctx        = is_ctx
                                                                                 it_key        = it_key
                                                                                 io_read       = io_read                                      ) = abap_true.

                IF lr_db_node->hec_row_selectable <> lv_release.
                  lr_db_node->hec_row_selectable = lv_release.
                  lv_data_changed                = abap_true.
                ENDIF.
              ENDIF.

              " Update DB server cluster type
              IF lr_db_node->hec_db_cluster_type_value <> <fs_instance_db>-hec_db_cluster_type_value.
                lr_db_node->hec_db_cluster_type_value = <fs_instance_db>-hec_db_cluster_type_value.
                lv_data_changed = abap_true.
              ENDIF.
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_node->key
                                   is_data = lr_db_node ).
              ENDIF.

              UNASSIGN <fs_instance_db>.
              CLEAR: lv_data_changed,
                     lv_release.
            ENDLOOP.
        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_db_server.

    DATA: lt_line              TYPE TABLE OF string,
          lv_inf_provider_guid TYPE /hec1/inf_provider_id,
          lv_datacenter_guid   TYPE /hec1/datacenter_fdt_guid,
          lt_db_server         TYPE /hec1/t_data_db_serv_ct,
          lt_db_server_before  TYPE /hec1/t_data_db_serv_ct,
          lt_db_serv_perf_cat  TYPE /hec1/t_data_db_serv_pc_ct,
          lt_phase             TYPE /hec1/t_data_phase_ct,
          lt_act_param         TYPE /hec1/t_act_create_db_storage,
*          lt_act_param_server  TYPE /hec1/t_act_update_db_server,
          lt_act_param_storage TYPE /bobf/t_frw_key,
          lt_act_param_dlvy    TYPE /hec1/t_act_update_dlvy_unit,
          lt_act_param_datac   TYPE /hec1/t_act_update_datacenter,
          lt_act_param_node    TYPE /hec1/t_act_update_db_node,
          lt_act_param_phasing TYPE TABLE OF /hec1/s_act_phase_inherit.



    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_server ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server-create.

            " Get DB server performance category node (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server-to_parent
                                              IMPORTING et_data        = lt_db_serv_perf_cat ).

            LOOP AT        lt_db_server
            REFERENCE INTO DATA(lr_db_server)
                WHERE hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master.

              "-----------------------------------
              " Set Value List Quantity - Server
              "-----------------------------------
              lr_db_server->hec_ip_server_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server(
                                                                           iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                           iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                           iv_sec_datacenter_guid = lr_db_server->hec_sec_datacenter_guid
                                                                           iv_srv_perf_cat_guid   = VALUE #( lt_db_serv_perf_cat[ 1 ]-hec_srv_perf_cat_guid OPTIONAL ) ) )
                                                         THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                         ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              lr_db_server->hec_delete_visible = abap_false.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_db_server->hec_ip_server_guid IS NOT INITIAL AND
                                                                             lr_db_server->hec_phase_guid     IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete          ).

              IF lv_inst_status <> lr_db_server->hec_instance_status.
                lr_db_server->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_db_serv_perf_cat[ key = lr_db_server->parent_key ] TO FIELD-SYMBOL(<fs_db_serv_perf_cat>).
              IF <fs_db_serv_perf_cat> IS ASSIGNED.
                IF <fs_db_serv_perf_cat>-hec_srv_perf_cat_guid IS NOT INITIAL AND
                   <fs_db_serv_perf_cat>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_db_server->hec_row_selectable.
                lr_db_server->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " DB server storage
              "-----------------------------------
              INSERT VALUE #( key         = lr_db_server->key
                              parent_key  = lr_db_server->parent_key
                              hec_pricing_included = abap_false               ) INTO TABLE lt_act_param.

              "-----------------------------------
              " Modify DB server
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_server->key
                                   is_data = lr_db_server ).
              ENDIF.

              UNASSIGN <fs_db_serv_perf_cat>.
              CLEAR: lv_inst_status,
                     lv_release,
                     lv_data_changed.
            ENDLOOP.


            "-----------------------------------
            " Set create DB server storage
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_db_storage( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_storage )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                  ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_db_server_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get DB Server PC (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server
                                                        it_key         = it_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server-to_parent
                                              IMPORTING et_target_key  = DATA(lt_db_serv_pc_key)
                                                        et_key_link    = DATA(lt_db_serv_pc_key_link) ).

            " Get DB Node (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                        it_key         = lt_db_serv_pc_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-to_parent
                                              IMPORTING et_key_link    = DATA(lt_db_node_key_link) ).

            " Get DB Storage (child)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server-db_storage
                                              IMPORTING et_key_link    = DATA(lt_server_to_storage_link) ).



            LOOP AT lt_db_server REFERENCE INTO lr_db_server.
              ASSIGN lt_db_server_before[ key = lr_db_server->key ] TO FIELD-SYMBOL(<fs_db_server_before>).
              IF <fs_db_server_before> IS ASSIGNED.

                "-----------------------------------
                " Split DB server infrastructure
                " provider server GUID
                "-----------------------------------
                IF lr_db_server->hec_ip_server_guid CA ';'.
                  SPLIT lr_db_server->hec_ip_server_guid
                     AT ';'
                   INTO TABLE lt_line.

                  LOOP AT lt_line ASSIGNING FIELD-SYMBOL(<fs_line>).
                    CASE sy-tabix.
                      WHEN 1.
                        lr_db_server->hec_ip_server_guid = <fs_line>.
                      WHEN 2.
                        lv_inf_provider_guid = <fs_line>.
                      WHEN 3.
                        lv_datacenter_guid = <fs_line>.
                    ENDCASE.
                  ENDLOOP.


                  "-----------------------------------
                  " Fill action table for update
                  " delivery unit
                  "-----------------------------------
                  IF lr_dlvy_unit->hec_inf_provider_guid IS INITIAL.
                    INSERT VALUE #( key                   = lr_dlvy_unit->key
                                    parent_key            = lr_dlvy_unit->parent_key
                                    hec_inf_provider_guid = lv_inf_provider_guid      ) INTO TABLE lt_act_param_dlvy.
                  ENDIF.


                  "-----------------------------------
                  " Fill action table for update
                  " data center
                  "-----------------------------------
                  TRY.
                      DATA(ls_datacenter) = lt_datacenter[ hec_node_datacenter = lr_db_server->hec_tier_datacenter_guid ].

                      IF ls_datacenter-hec_datacenter_guid IS INITIAL.
                        INSERT VALUE #( key                     = ls_datacenter-key
                                        parent_key              = ls_datacenter-parent_key
                                        hec_datacenter_fdt_guid = lv_datacenter_guid       ) INTO TABLE lt_act_param_datac.
*
                        "-----------------------------------
                        " Fill action table for update
                        " db node pricing
                        "-----------------------------------
                        INSERT VALUE #( key = lt_db_node_key_link[ source_key = lr_db_server->parent_key ]-target_key ) INTO TABLE lt_act_param_node.

                      ENDIF. " IF ls_datacenter-hec_datacenter_guid IS INITIAL.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                ENDIF. " IF ls_db_server-hec_ds_ip_server_guid CA ';'.


                "-----------------------------------
                " Infrastructure provider server
                " has changed
                "-----------------------------------
                IF lr_db_server->hec_ip_server_guid    IS NOT INITIAL                            AND
                   lr_db_server->hec_ip_server_guid <> <fs_db_server_before>-hec_ip_server_guid.

                  IF lv_inf_provider_guid IS NOT INITIAL.
                    lr_dlvy_unit->hec_inf_provider_guid = lv_inf_provider_guid.
                  ENDIF.

                  IF lr_db_server->hec_sec_datacenter_guid IS INITIAL     AND
                     lv_datacenter_guid                    IS NOT INITIAL.
                    lr_db_server->hec_sec_datacenter_guid = lv_datacenter_guid.
                    lv_data_changed                   = abap_true.
                  ENDIF.

                  SELECT SINGLE *
                    FROM /hec1/i_serverbasic
                   WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid            AND
                         hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid   AND
                         hec_sec_datacenter_guid = @lr_db_server->hec_sec_datacenter_guid AND
                         hec_ip_server_guid      = @lr_db_server->hec_ip_server_guid
                    INTO @DATA(ls_server).

                  IF ls_server IS NOT INITIAL.
                    lr_db_server->hec_ip_server_descr     = ls_server-hec_ip_server_descr.
                    lr_db_server->hec_ip_server_guid      = ls_server-hec_ip_server_guid.
                    lr_db_server->hec_host_type_descr     = ls_server-hec_srv_host_type_descr.
                    lr_db_server->hec_host_type_value     = ls_server-hec_srv_host_type_value.
                    lr_db_server->hec_ram_size            = ls_server-hec_srv_ram_size.
                    lr_db_server->hec_cpu_size            = ls_server-hec_srv_cpu_size.
                    lr_db_server->hec_sec_datacenter_guid = ls_server-hec_sec_datacenter_guid.
                    lr_db_server->hec_srv_main_stor_qty   = ls_server-hec_srv_main_storage_qty.
                    lr_db_server->hec_tree_descr          = ls_server-hec_ip_server_descr. "#EC CI_FLDEXT_OK[2215424]
                    lr_db_server->hec_srv_flavour         = ls_server-hec_srv_flavour.
                    lr_db_server->hec_saps                = ls_server-hec_saps.
                    lr_db_server->hec_approval_needed     = ls_server-hec_approval_needed.

                    lv_data_changed                       = abap_true.

                    " Set Value List Quantity - Server
                    lr_db_server->hec_ip_server_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server(
                                                                                 iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                 iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                                 iv_sec_datacenter_guid = lr_db_server->hec_sec_datacenter_guid
                                                                                 iv_srv_perf_cat_guid   = VALUE #( lt_db_serv_perf_cat[ 1 ]-hec_srv_perf_cat_guid OPTIONAL ) ) )
                                                               THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                               ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                    " ************************
                    " Get DB server pricing
                    " ************************
                    SELECT SINGLE hec_cb_pricing_lb_guid
                    FROM /hec1/i_serverlbbasic
                   WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid            AND
                         hec_sec_datacenter_guid = @lr_db_server->hec_sec_datacenter_guid AND
                         hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid   AND
                         hec_ip_server_guid      = @lr_db_server->hec_ip_server_guid
                    INTO @DATA(lv_lb_guid).

                    SELECT SINGLE * FROM /hec1/c_cbp_lb "#EC CI_ALL_FIELDS_NEEDED
                       INTO @DATA(ls_pricing)
                      WHERE hec_price_lb = @lv_lb_guid.

                    lr_db_server->* = CORRESPONDING #( BASE ( lr_db_server->* ) ls_pricing ).

                    "-----------------------------------
                    " Fill action table for update
                    " DB server storage
                    "-----------------------------------
                    LOOP AT lt_server_to_storage_link REFERENCE INTO DATA(lr_server_to_storage_link)
                      WHERE source_key = lr_db_server->key.
                      INSERT VALUE #( key = lr_server_to_storage_link->target_key ) INTO TABLE lt_act_param_storage.
                    ENDLOOP.

                  ENDIF. " IF ls_server IS NOT INITIAL.
                ENDIF. " IF lr_db_server->hec_ip_server_guid IS INITIAL

                "-----------------------------------
                " Value List Quanitty
                "-----------------------------------
                "  HEC_DS_BACKUPSLA_VALUE
                IF lr_db_server->hec_ds_backupsla_value <> <fs_db_server_before>-hec_ds_backupsla_value.
                  lr_db_server->hec_ds_backupsla_vlqt = COND #( WHEN 1 < lines( /rbp/cl_fpm_utilities=>get_characteristic_values( CONV #( 'HEC_DS_BACKUPSLA_VALUE' ) ) )
                                                                THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).
                ENDIF.

                " HEC_DS_BACKUPSLA_FILE_VALUE
                IF lr_db_server->hec_ds_backupsla_file_value <> <fs_db_server_before>-hec_ds_backupsla_file_value.
                  lr_db_server->hec_ds_backupsla_file_vlqt = COND #( WHEN 1 < lines( /rbp/cl_fpm_utilities=>get_characteristic_values( CONV #( 'HEC_DS_BACKUPSLA_FILE_VALUE' ) ) )
                                                                     THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                     ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).
                ENDIF.

                "-----------------------------------
                " Phase has changed
                "-----------------------------------
                IF lr_db_server->hec_phase_guid NE <fs_db_server_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_db_server->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                     lr_db_server->hec_db_node_default          = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_db_server->key
                                    hec_phase_guid_new = lr_db_server->hec_phase_guid
                                    hec_phase_guid_old = <fs_db_server_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_db_server->hec_phase_changed = abap_true.
                  lv_data_changed                 = abap_true.

                ENDIF. "phasing changed
              ENDIF. " if <fs_db_server_before> is assigned.


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_db_server->hec_ip_server_guid IS NOT INITIAL AND
                                                                       lr_db_server->hec_phase_guid     IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_db_server->hec_instance_status.
                lr_db_server->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Modify DB server
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_server->key
                                   is_data = lr_db_server ).
              ENDIF.

              UNASSIGN: <fs_line>,
                        <fs_db_server_before>.

              CLEAR: lv_inf_provider_guid,
                     lv_datacenter_guid,
                     lv_lb_guid,
                     lv_inst_status,
                     lv_data_changed,
                     ls_datacenter,
                     ls_server,
                     ls_pricing,
                     lt_line.
            ENDLOOP.

            "-----------------------------------
            " Set update delivery unit action to
            " general
            "-----------------------------------
            IF lt_act_param_dlvy IS NOT INITIAL.
              CLEAR me->mr_act_param_dlvy.
              me->mr_act_param_dlvy = NEW /hec1/t_act_update_dlvy_unit( lt_act_param_dlvy ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-delivery_unit )
                    it_key          = VALUE #( FOR wa_act_dlvy IN lt_act_param_dlvy
                                              ( key = wa_act_dlvy-key )    )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_delivery_unit )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_dlvy                                                                                                                ).

            ENDIF.

            "-----------------------------------
            " Set update data center action to
            " general
            "-----------------------------------
            IF lt_act_param_datac IS NOT INITIAL.
              CLEAR me->mr_act_param_datac.
              me->mr_act_param_datac = NEW /hec1/t_act_update_datacenter( lt_act_param_datac ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-datacenter )
                    it_key          = VALUE #( FOR wa_act_datac IN lt_act_param_datac
                                              ( key = wa_act_datac-key )     )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_datacenter )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_datac                                                                                                            ).

            ENDIF.

            "-----------------------------------
            " Set DB Node action to
            " general
            "-----------------------------------
            IF lt_act_param_node IS NOT INITIAL.

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-db_node )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param_node
                                             ( key = wa_act_node-key )             )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                           ).

            ENDIF.

            "-----------------------------------
            " Set update DB Storage action to
            " general
            "-----------------------------------
            IF lt_act_param_storage IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-db_storage )
                  it_key          = lt_act_param_storage
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_storage )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                                                                          ).
            ENDIF.

            "-----------------------------------
            " Set update phase action to general
            "-----------------------------------
            IF lt_act_param_phasing IS NOT INITIAL.
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).

            ENDIF.


            " ***************************************************************************
            " Update mode after app server
            " performance category update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server-update_after_serv_perf_cat.

            io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                         it_key  = it_key
                               IMPORTING et_data = lt_db_server ).

            " Get DB server performance category (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server-to_parent
                                              IMPORTING et_data        = lt_db_serv_perf_cat ).


            LOOP AT lt_db_server REFERENCE INTO lr_db_server.
              ASSIGN lt_db_serv_perf_cat[ key = lr_db_server->parent_key ] TO <fs_db_serv_perf_cat>.

              IF <fs_db_serv_perf_cat> IS ASSIGNED.
                IF <fs_db_serv_perf_cat>-hec_srv_perf_cat_guid IS NOT INITIAL AND
                   <fs_db_serv_perf_cat>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              IF lv_release <> lr_db_server->hec_row_selectable.
                lr_db_server->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Update DB server cluster type
              "-----------------------------------
              IF lr_db_server->hec_db_cluster_type_value <> <fs_db_serv_perf_cat>-hec_db_cluster_type_value.
                lr_db_server->hec_db_cluster_type_value = <fs_db_serv_perf_cat>-hec_db_cluster_type_value.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_server->key
                                   is_data = lr_db_server ).
              ENDIF.

              UNASSIGN <fs_db_serv_perf_cat>.
              CLEAR: lv_release,
                     lv_data_changed.

            ENDLOOP. " LOOP AT lt_db_server REFERENCE INTO lr_db_server.
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_db_server_instance.

    DATA: lt_db_serv_inst        TYPE /hec1/t_data_db_server_inst_ct,
          lt_db_serv_inst_before TYPE /hec1/t_data_db_server_inst_ct,
          lt_instance_db         TYPE /hec1/t_data_db_inst_ct,
          lt_tier                TYPE /hec1/t_data_tier_ct,
          lt_tier_all            TYPE /hec1/t_data_tier_ct,
          lt_db_serv_inst_all    TYPE /hec1/t_data_db_server_inst_ct,
          lt_instance_db_all     TYPE /hec1/t_data_db_inst_ct,
          lt_solution            TYPE /hec1/t_data_solution_ct,
          ls_landscape           TYPE /hec1/s_config_root_cs,
          lt_act_param           TYPE /hec1/t_act_create_instance_db,
          lt_act_param_delete    TYPE /bobf/t_frw_node,
          lt_act_param_instance  TYPE /hec1/t_act_update_instance_db,
          lt_phase               TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing   TYPE TABLE OF /hec1/s_act_phase_inherit,
          lt_vals                TYPE TABLE OF dd07v.

    CLEAR: eo_message,
           et_failed_key.

    " Data before update
    io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                 it_key          = it_key
                                 iv_before_image = abap_true
                       IMPORTING et_data         = lt_db_serv_inst_before ).

    " Data after update
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_serv_inst ).


    " Get tier
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-to_parent
                                      IMPORTING et_data        = lt_tier
                                                et_target_key  = DATA(lt_tier_key) ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    "-----------------------------------
    " Get APM model GUID and description
    "-----------------------------------
    /hec1/cl_config_helper=>get_apm_model( EXPORTING iv_node_key   = is_ctx-node_key
                                                     it_key        = it_key
                                                     io_read       = io_read
                                           IMPORTING et_failed_key = et_failed_key
                                                     es_apm_model  = ls_landscape ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server_instance-create.

            LOOP AT lt_db_serv_inst REFERENCE INTO DATA(lr_db_serv_inst).

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              " Server Instance
              lr_db_serv_inst->hec_sol_tier_stack_si_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server_instance(
                                                                                      iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                      iv_sol_tier_stack_guid = lr_db_serv_inst->hec_sol_tier_stack_si_guid
                                                                                      iv_srv_inst_rel_value  = lr_db_serv_inst->hec_srv_inst_rel_value
                                                                                      iv_solution_guid       = lr_db_serv_inst->hec_solution_guid ) )
                                                                    THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                    ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " DB Type
              lr_db_serv_inst->hec_sol_tier_dsi_dbstype_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_server_type(
                                                                                          iv_apm_guid               = lr_landscape->hec_apm_guid
                                                                                          iv_sol_tier_stack_si_guid = lr_db_serv_inst->hec_sol_tier_stack_si_guid ) )
                                                                       THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                       ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " Implementation Type
              lr_db_serv_inst->hec_sol_dbst_impltype_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_implementation_type(
                                                                                      iv_apm_guid                  = lr_landscape->hec_apm_guid
                                                                                      iv_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid ) )
                                                                    THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                    ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " Instance Type
              lr_db_serv_inst->hec_sol_dbst_impty_instty_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_instance_type(
                                                                                          iv_apm_guid                  = lr_landscape->hec_apm_guid
                                                                                          iv_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid
                                                                                          iv_sol_dbst_impltype_guid    = lr_db_serv_inst->hec_sol_dbst_impltype_guid ) )
                                                                        THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                        ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " Allocation
              lr_db_serv_inst->hec_sol_dbst_imty_inty_al_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_allocation(
                                                                                          iv_apm_guid                   = lr_landscape->hec_apm_guid
                                                                                          iv_sol_tier_dsi_dbstype_guid  = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid
                                                                                          iv_sol_dbst_impty_instty_guid = lr_db_serv_inst->hec_sol_dbst_impty_instty_guid ) )
                                                                        THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                        ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " Operating System
              lr_db_serv_inst->hec_sol_dbst_oper_sys_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_operating_system(
                                                                                      iv_apm_guid                  = lr_landscape->hec_apm_guid
                                                                                      iv_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid ) )
                                                                    THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                    ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " HEC_DSI_OPSYS_IMAGE_VAL
              CALL FUNCTION 'GET_DOMAIN_VALUES'
                EXPORTING
                  domname         = '/HEC1/DOM_OS_VERSION'
                  text            = 'X'
                TABLES
                  values_tab      = lt_vals
                EXCEPTIONS
                  no_values_found = 1
                  OTHERS          = 2.

              IF sy-subrc = 0.
                lr_db_serv_inst->hec_dsi_opsys_image_vlqt = COND #( WHEN 1 < lines( lt_vals )
                                                                    THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                    ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).
              ENDIF.

              lr_db_serv_inst->hec_delete_visible = abap_false.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_db_serv_inst->hec_sol_tier_stack_si_guid     IS NOT INITIAL AND
                                                                             lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid  IS NOT INITIAL AND
                                                                             lr_db_serv_inst->hec_sol_dbst_oper_sys_guid     IS NOT INITIAL AND
                                                                             lr_db_serv_inst->hec_sol_dbst_impltype_guid     IS NOT INITIAL AND
                                                                             lr_db_serv_inst->hec_sol_dbst_impty_instty_guid IS NOT INITIAL AND
                                                                             lr_db_serv_inst->hec_sol_dbst_imty_inty_al_guid IS NOT INITIAL AND
                                                                             lr_db_serv_inst->hec_phase_guid                 IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete            ).

              IF lv_inst_status <> lr_db_serv_inst->hec_instance_status.
                lr_db_serv_inst->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.


              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_tier[ key = lr_db_serv_inst->parent_key ] TO FIELD-SYMBOL(<fs_tier>).
              IF <fs_tier> IS ASSIGNED.
                IF <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                   <fs_tier>-hec_tier_type_value      IS NOT INITIAL AND
                   <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_db_serv_inst->hec_row_selectable.
                lr_db_serv_inst->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Fill action table for create
              " instance DB action
              "-----------------------------------
              IF lr_db_serv_inst->hec_db_quantity IS NOT INITIAL.
                INSERT VALUE #( key             = lr_db_serv_inst->key
                                parent_key      = lr_db_serv_inst->parent_key
                                hec_db_quantity = lr_db_serv_inst->hec_db_quantity ) INTO TABLE lt_act_param.
              ENDIF.

              "-----------------------------------
              " Modify DB server instance
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_serv_inst->key
                                   is_data = lr_db_serv_inst ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP.

            "-----------------------------------
            " Set create Instance DB action to
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_instance_db( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_inst_db )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                ).
            ENDIF.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server_instance-update.

            " Get instance DB
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-instance_db
                                              IMPORTING et_data        = lt_instance_db ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get all Instance DBs (for multitenancy id)
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-solution
                                              IMPORTING et_target_key  = DATA(lt_solution_key_all) ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-solution
                                                        it_key         = lt_solution_key_all
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                              IMPORTING et_data        = lt_tier_all
                                                        et_target_key  = DATA(lt_tier_key_all) ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                        it_key         = lt_tier_key_all
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier-db_server_instance
                                              IMPORTING et_data        = lt_db_serv_inst_all
                                                        et_target_key  = DATA(lt_db_serv_inst_key_all) ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                        it_key         = lt_db_serv_inst_key_all
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-instance_db
                                              IMPORTING et_data        = lt_instance_db_all
                                                        et_target_key  = DATA(lt_instance_db_key_all) ).


            "-----------------------------------
            " Get DB server type
            "-----------------------------------
            SELECT *
              FROM /hec1/i_dbservertypebasic
             WHERE hec_apm_guid  = @ls_landscape-hec_apm_guid
              INTO TABLE @DATA(lt_db_server_type).


            "-----------------------------------
            " Get DB server operating system
            "-----------------------------------
            SELECT *
              FROM /hec1/i_dboperssystembasic
             WHERE hec_apm_guid  = @ls_landscape-hec_apm_guid
              INTO TABLE @DATA(lt_db_operating_sys).


            "-----------------------------------
            " Get DB server implementation type
            "-----------------------------------
            SELECT *
              FROM /hec1/i_dbimplementtypebasic
             WHERE hec_apm_guid  = @ls_landscape-hec_apm_guid
              INTO TABLE @DATA(lt_db_impl_type).


            "-----------------------------------
            " Get DB server instance type
            "-----------------------------------
            SELECT *
              FROM /hec1/i_dbinstancetypebasic
             WHERE hec_apm_guid  = @ls_landscape-hec_apm_guid
              INTO TABLE @DATA(lt_db_inst_type).


            "-----------------------------------
            " Get DB server allocation
            "-----------------------------------
            SELECT *
              FROM /hec1/i_dballocationbasic
             WHERE hec_apm_guid  = @ls_landscape-hec_apm_guid
              INTO TABLE @DATA(lt_db_allocation).



            LOOP AT lt_db_serv_inst REFERENCE INTO lr_db_serv_inst.

              ASSIGN lt_db_serv_inst_before[ key = lr_db_serv_inst->key ] TO FIELD-SYMBOL(<fs_db_serv_inst_before>).
              IF <fs_db_serv_inst_before> IS ASSIGNED.

                lr_db_serv_inst->hec_delete_visible = abap_false.

                "-----------------------------------
                " DB server type has changed
                "-----------------------------------
                IF lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid IS NOT INITIAL                                   AND
                   lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid <> <fs_db_serv_inst_before>-hec_sol_tier_dsi_dbstype_guid.
                  TRY.
                      DATA(ls_db_server_type) = lt_db_server_type[ hec_sol_tier_stack_si_guid    = lr_db_serv_inst->hec_sol_tier_stack_si_guid
                                                                   hec_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid ].

                      lr_db_serv_inst->hec_db_srv_type_guid      = ls_db_server_type-hec_db_srv_type_guid.
                      lr_db_serv_inst->hec_db_srv_type_value     = ls_db_server_type-hec_db_srv_type_value.
                      lr_db_serv_inst->hec_db_srv_type_descr     = ls_db_server_type-hec_db_srv_type_descr.
                      lr_db_serv_inst->hec_calc_setup_dr         = ls_db_server_type-hec_calc_setup_dr.
                      lr_db_serv_inst->hec_ty_support_stat_value = ls_db_server_type-hec_ty_support_stat_value.
                      lr_db_serv_inst->hec_ty_support_stat_descr = ls_db_server_type-hec_ty_support_stat_descr.
                      lr_db_serv_inst->hec_tree_descr            = ls_db_server_type-hec_db_srv_type_descr.

                      lv_data_changed                            = abap_true.

                      " Set Value List Quantity
                      " DB Type
                      lr_db_serv_inst->hec_sol_tier_dsi_dbstype_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_server_type(
                                                                                                  iv_apm_guid               = lr_landscape->hec_apm_guid
                                                                                                  iv_sol_tier_stack_si_guid = lr_db_serv_inst->hec_sol_tier_stack_si_guid ) )
                                                                               THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                               ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                      IF lr_db_serv_inst->hec_init_ty_support_stat_value IS INITIAL.
                        lr_db_serv_inst->hec_init_ty_support_stat_value = lr_db_serv_inst->hec_ty_support_stat_value.
                        lr_db_serv_inst->hec_init_ty_support_stat_descr = lr_db_serv_inst->hec_ty_support_stat_descr.
                      ENDIF.

                      IF lr_db_serv_inst->hec_sol_dbst_oper_sys_guid IS INITIAL.
                        "-----------------------------------
                        " If there is only one operating
                        " system, then it should be
                        " preselected
                        "-----------------------------------
                        DATA(lt_operating_sys) = VALUE /hec1/t_apm_db_operating_sys( FOR wa_os IN lt_db_operating_sys
                                                                                     WHERE ( hec_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid )
                                                                                     ( CORRESPONDING #( wa_os ) )                                                             ).

                        IF lines( lt_operating_sys ) = 1.
                          TRY.
                              lr_db_serv_inst->hec_sol_dbst_oper_sys_guid = lt_operating_sys[ 1 ]-hec_sol_dbst_oper_sys_guid.
                            CATCH cx_sy_itab_line_not_found.
                          ENDTRY.
                          "-----------------------------------
                          " If there are multiple operating
                          " systems possible and Linux is
                          " between them - set it preselected
                          "-----------------------------------
                        ELSEIF lines( lt_operating_sys ) > 1 AND line_exists( lt_operating_sys[ hec_operating_sys_value = /hec1/cl_rep_config_data=>c_os_linux ] ).
                          TRY.
                              lr_db_serv_inst->hec_sol_dbst_oper_sys_guid = lt_operating_sys[ hec_operating_sys_value = /hec1/cl_rep_config_data=>c_os_linux ]-hec_sol_dbst_oper_sys_guid.
                            CATCH cx_sy_itab_line_not_found.
                          ENDTRY.
                        ENDIF. " IF lines( lt_operating_sys ) = 1.
                      ENDIF. " IF lr_db_serv_inst->hec_sol_dbst_oper_sys_guid IS INITIAL.

                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  CLEAR: ls_db_server_type,
                         lt_operating_sys.
                ENDIF.

                "-----------------------------------
                " DB operating system has changed
                "-----------------------------------
                IF lr_db_serv_inst->hec_sol_dbst_oper_sys_guid IS NOT INITIAL                                         AND
                   lr_db_serv_inst->hec_sol_dbst_oper_sys_guid <> <fs_db_serv_inst_before>-hec_sol_dbst_oper_sys_guid.

                  TRY.
                      DATA(ls_operating_sys) = lt_db_operating_sys[ hec_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid
                                                                    hec_sol_dbst_oper_sys_guid    = lr_db_serv_inst->hec_sol_dbst_oper_sys_guid    ].

                      lr_db_serv_inst->hec_operating_sys_guid    = ls_operating_sys-hec_operating_sys_guid.
                      lr_db_serv_inst->hec_operating_sys_value   = ls_operating_sys-hec_operating_sys_value.
                      lr_db_serv_inst->hec_operating_sys_descr   = ls_operating_sys-hec_operating_sys_descr.
                      lr_db_serv_inst->hec_os_support_stat_value = ls_operating_sys-hec_os_support_stat_value.
                      lr_db_serv_inst->hec_os_support_stat_descr = ls_operating_sys-hec_os_support_stat_descr.

                      lv_data_changed                            = abap_true.

                      " Set Value List Quantity - Operating System
                      lr_db_serv_inst->hec_sol_dbst_oper_sys_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_operating_system(
                                                                                              iv_apm_guid                  = lr_landscape->hec_apm_guid
                                                                                              iv_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid ) )
                                                                            THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                            ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                      IF lr_db_serv_inst->hec_init_os_support_stat_value IS INITIAL.
                        lr_db_serv_inst->hec_init_os_support_stat_value = lr_db_serv_inst->hec_os_support_stat_value.
                        lr_db_serv_inst->hec_init_os_support_stat_descr = lr_db_serv_inst->hec_os_support_stat_descr.
                      ENDIF.

                      IF lr_db_serv_inst->hec_sol_dbst_impltype_guid IS INITIAL.
                        DATA(lt_impl_type) = VALUE /hec1/t_apm_db_implement_type( FOR wa_imp IN lt_db_impl_type
                                                                                  WHERE ( hec_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid )
                                                                                 ( CORRESPONDING #( wa_imp ) )                                                             ).

                        IF lines( lt_impl_type ) = 1.
                          lr_db_serv_inst->hec_sol_dbst_impltype_guid = lt_impl_type[ 1 ]-hec_sol_dbst_impltype_guid.
                        ENDIF.
                      ENDIF. " IF lr_db_serv_inst->hec_sol_dbst_impltype_guid IS INITIAL.

                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  CLEAR: ls_operating_sys,
                         lt_impl_type.
                ENDIF.

                "-----------------------------------
                " DB implementation type has changed
                "-----------------------------------
                IF lr_db_serv_inst->hec_sol_dbst_impltype_guid IS NOT INITIAL                                         AND
                   lr_db_serv_inst->hec_sol_dbst_impltype_guid <> <fs_db_serv_inst_before>-hec_sol_dbst_impltype_guid.

                  TRY.
                      DATA(ls_impl_type) = lt_db_impl_type[ hec_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid
                                                            hec_sol_dbst_impltype_guid    = lr_db_serv_inst->hec_sol_dbst_impltype_guid    ].

                      lr_db_serv_inst->hec_db_impl_type_guid      = ls_impl_type-hec_db_impl_type_guid.
                      lr_db_serv_inst->hec_db_impl_type_value     = ls_impl_type-hec_db_impl_type_value.
                      lr_db_serv_inst->hec_db_impl_type_descr     = ls_impl_type-hec_db_impl_type_descr.
                      lr_db_serv_inst->hec_imp_support_stat_value = ls_impl_type-hec_imp_support_stat_value.
                      lr_db_serv_inst->hec_imp_support_stat_descr = ls_impl_type-hec_imp_support_stat_descr.

                      lv_data_changed                             = abap_true.

                      " Set Value List Quantity - Implementation Type
                      lr_db_serv_inst->hec_sol_dbst_impltype_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_implementation_type(
                                                                                              iv_apm_guid                  = lr_landscape->hec_apm_guid
                                                                                              iv_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid ) )
                                                                            THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                            ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                      IF lr_db_serv_inst->hec_init_imp_supp_stat_value IS INITIAL.
                        lr_db_serv_inst->hec_init_imp_supp_stat_value = lr_db_serv_inst->hec_imp_support_stat_value.
                        lr_db_serv_inst->hec_init_imp_supp_stat_descr = lr_db_serv_inst->hec_imp_support_stat_descr.
                      ENDIF.

                      " Get DB instance type
                      DATA(lt_inst_type) = VALUE /hec1/t_apm_db_instance_type( FOR wa IN lt_db_inst_type
                                                                               WHERE ( hec_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid AND
                                                                                       hec_sol_dbst_impltype_guid    = lr_db_serv_inst->hec_sol_dbst_impltype_guid        )
                                                                               ( CORRESPONDING #( wa ) )                                                                    ).

                      IF lines( lt_inst_type ) = 1.
                        lr_db_serv_inst->hec_sol_dbst_impty_instty_guid = lt_inst_type[ 1 ]-hec_sol_dbst_impty_instty_guid.
                      ENDIF.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  CLEAR: ls_impl_type,
                         lt_inst_type.
                ENDIF. " IF lr_db_serv_inst->hec_db_impl_type_guid IS NOT INITIAL...

                "-----------------------------------
                " DB instance type has changed
                "-----------------------------------
                IF lr_db_serv_inst->hec_sol_dbst_impty_instty_guid IS NOT INITIAL                                             AND
                   lr_db_serv_inst->hec_sol_dbst_impty_instty_guid <> <fs_db_serv_inst_before>-hec_sol_dbst_impty_instty_guid.

                  TRY.
                      DATA(ls_inst_type) = lt_db_inst_type[ hec_sol_tier_dsi_dbstype_guid  = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid
                                                            hec_sol_dbst_impltype_guid     = lr_db_serv_inst->hec_sol_dbst_impltype_guid
                                                            hec_sol_dbst_impty_instty_guid = lr_db_serv_inst->hec_sol_dbst_impty_instty_guid ].

                      lr_db_serv_inst->hec_db_inst_type_guid       = ls_inst_type-hec_db_inst_type_guid.
                      lr_db_serv_inst->hec_db_inst_type_value      = ls_inst_type-hec_db_inst_type_value.
                      lr_db_serv_inst->hec_db_inst_type_descr      = ls_inst_type-hec_db_inst_type_descr.
                      lr_db_serv_inst->hec_inst_support_stat_value = ls_inst_type-hec_inst_support_stat_value.
                      lr_db_serv_inst->hec_inst_support_stat_descr = ls_inst_type-hec_inst_support_stat_descr.

                      lv_data_changed                              = abap_true.

                      " Set Value List Quantity - Instance Type
                      lr_db_serv_inst->hec_sol_dbst_impty_instty_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_instance_type(
                                                                                                  iv_apm_guid                  = lr_landscape->hec_apm_guid
                                                                                                  iv_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid
                                                                                                  iv_sol_dbst_impltype_guid    = lr_db_serv_inst->hec_sol_dbst_impltype_guid ) )
                                                                                THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                                ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                      IF lr_db_serv_inst->hec_init_inst_supp_stat_value IS INITIAL.
                        lr_db_serv_inst->hec_init_inst_supp_stat_value = lr_db_serv_inst->hec_inst_support_stat_value.
                        lr_db_serv_inst->hec_init_inst_supp_stat_descr = lr_db_serv_inst->hec_inst_support_stat_descr.
                      ENDIF.

                      DATA(lt_allocation) = VALUE /hec1/t_apm_db_allocation( FOR wa_allo IN lt_db_allocation
                                                                             WHERE ( hec_sol_tier_dsi_dbstype_guid  = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid  AND
                                                                                     hec_sol_dbst_impty_instty_guid = lr_db_serv_inst->hec_sol_dbst_impty_instty_guid     )
                                                                             ( CORRESPONDING #( wa_allo ) ) ).

                      IF lines( lt_allocation ) = 1.
                        lr_db_serv_inst->hec_sol_dbst_imty_inty_al_guid = lt_allocation[ 1 ]-hec_sol_dbst_imty_inty_al_guid.
                      ENDIF.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  CLEAR: ls_inst_type,
                         lt_allocation.
                ENDIF.

                "-----------------------------------
                " DB allocation has changed
                "-----------------------------------
                IF lr_db_serv_inst->hec_sol_dbst_imty_inty_al_guid IS NOT INITIAL                                             AND
                   lr_db_serv_inst->hec_sol_dbst_imty_inty_al_guid <> <fs_db_serv_inst_before>-hec_sol_dbst_imty_inty_al_guid.

                  TRY.
                      DATA(ls_allocation) = lt_db_allocation[ hec_sol_tier_dsi_dbstype_guid  = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid
                                                              hec_sol_dbst_impty_instty_guid = lr_db_serv_inst->hec_sol_dbst_impty_instty_guid
                                                              hec_sol_dbst_imty_inty_al_guid = lr_db_serv_inst->hec_sol_dbst_imty_inty_al_guid ].

                      lr_db_serv_inst->hec_db_allocation_guid       = ls_allocation-hec_db_allocation_guid.
                      lr_db_serv_inst->hec_db_allocation_value      = ls_allocation-hec_db_allocation_value.
                      lr_db_serv_inst->hec_db_allocation_descr      = ls_allocation-hec_db_allocation_descr.
                      lr_db_serv_inst->hec_db_quantity              = ls_allocation-hec_db_quantity.
                      lr_db_serv_inst->hec_alloc_support_stat_value = ls_allocation-hec_alloc_support_stat_value.
                      lr_db_serv_inst->hec_alloc_support_stat_descr = ls_allocation-hec_alloc_support_stat_descr.

                      lv_data_changed = abap_true.

                      " Set Value List Quantity - Allocation
                      lr_db_serv_inst->hec_sol_dbst_imty_inty_al_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_allocation(
                                                                                                  iv_apm_guid                   = lr_landscape->hec_apm_guid
                                                                                                  iv_sol_tier_dsi_dbstype_guid  = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid
                                                                                                  iv_sol_dbst_impty_instty_guid = lr_db_serv_inst->hec_sol_dbst_impty_instty_guid ) )
                                                                                THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                                ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                      IF lr_db_serv_inst->hec_init_alloc_supp_stat_value IS INITIAL.
                        lr_db_serv_inst->hec_init_alloc_supp_stat_value = lr_db_serv_inst->hec_alloc_support_stat_value.
                        lr_db_serv_inst->hec_init_alloc_supp_stat_descr = lr_db_serv_inst->hec_alloc_support_stat_descr.
                      ENDIF.

                      " After a reset of the DB allocation the subnodes are not deleted.
                      " In this case, no additional instance DB should be created.
                      IF NOT line_exists( lt_instance_db[ parent_key = lr_db_serv_inst->key ] ).
                        "-----------------------------------
                        " Fill action table for create
                        " instance DB action
                        "-----------------------------------
                        INSERT VALUE #( key             = lr_db_serv_inst->key
                                        parent_key      = lr_db_serv_inst->parent_key
                                        hec_db_quantity = lr_db_serv_inst->hec_db_quantity ) INTO TABLE lt_act_param.
                      ENDIF.

                      " Set Tier
                      IF lr_db_serv_inst->hec_db_allocation_value = /hec1/if_config_constants=>gc_db_allocation-internal.
                        DATA(ls_tier) = VALUE #( lt_tier[ key = lr_db_serv_inst->parent_key ] OPTIONAL ).
                        lr_db_serv_inst->hec_db_tier_guid  = ls_tier-hec_node_tier.
                        lr_db_serv_inst->hec_db_tier_descr = ls_tier-hec_tree_descr.
                      ENDIF.

                      " If the allocation type is "related tier" the related tier needs to be selected automatically.
                      IF lr_db_serv_inst->hec_db_allocation_value = /hec1/if_config_constants=>gc_db_allocation-related_stack.
                        ls_tier = VALUE #( lt_tier[ key = lr_db_serv_inst->parent_key ] OPTIONAL ).

                        LOOP AT lt_tier_all ASSIGNING FIELD-SYMBOL(<fs_tier_related>)
                          WHERE hec_node_tier NE ls_tier-hec_node_tier
                            AND hec_related_stack_guid = ls_tier-hec_related_stack_guid.
                          DATA(ls_tier_related) = <fs_tier_related>.
                        ENDLOOP.

                        lr_db_serv_inst->hec_db_tier_guid  = ls_tier_related-hec_node_tier.
                        lr_db_serv_inst->hec_db_tier_descr = ls_tier_related-hec_tree_descr.
                      ENDIF.

                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  CLEAR ls_allocation.
                ENDIF. " IF lr_db_serv_inst->hec_db_allocation_guid IS NOT INITIAL

                "-----------------------------------
                " DB Tier has changed
                " -> Update Multitenancy for Tenants
                "-----------------------------------
                IF lr_db_serv_inst->hec_db_tier_guid NE <fs_db_serv_inst_before>-hec_db_tier_guid
                  AND lr_db_serv_inst->hec_db_allocation_guid NE /hec1/if_config_constants=>gc_db_allocation-internal.

                  " get instance db (tenant)
                  TRY.
                      DATA(ls_instance_db_tenant) = lt_instance_db_all[ parent_key             = lr_db_serv_inst->key
                                                                        hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-tenant ].

                      " get tier, that is referenced in db_tier
                      " get db server instance -> instance db (container) underneath

                      ls_tier = lt_tier_all[ hec_node_tier = lr_db_serv_inst->hec_db_tier_guid ].

                      LOOP AT lt_db_serv_inst_all INTO DATA(ls_db_serv_inst)
                        WHERE hec_db_allocation_value = /hec1/if_config_constants=>gc_db_allocation-internal
                          AND hec_db_impl_type_value = /hec1/if_config_constants=>gc_db_impl_type-multitenancy.

                        LOOP AT lt_instance_db_all INTO DATA(ls_instance_db_container)
                          WHERE hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-container.

                          " Add action to update tenant to general
                          INSERT VALUE #( key                          = ls_instance_db_tenant-key
                                          parent_key                   = ls_instance_db_tenant-parent_key
                                          hec_multi_tenant_rel_guid    = ls_instance_db_container-hec_multi_tenant_rel_guid
                                          do_update_multi_tenancy_guid = abap_true
                                          ) INTO TABLE lt_act_param_instance.

                        ENDLOOP.

                      ENDLOOP.

                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                ENDIF.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_db_serv_inst->hec_phase_guid NE <fs_db_serv_inst_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_db_serv_inst->key
                                  hec_phase_guid_new = lr_db_serv_inst->hec_phase_guid
                                  hec_phase_guid_old = <fs_db_serv_inst_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_db_serv_inst->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "phasing changed

                "-----------------------------------
                " Reset fields
                " - these are all triggered from
                "   the BOPF-actions
                "-----------------------------------
                " The following fields are all dependent on each other. If one field is cleared, the subsequent fields have to be cleared as well.
                " These fields always come in triples (GUID, Value, Description)
                IF lr_db_serv_inst->hec_sol_tier_stack_si_guid          IS INITIAL      AND
                   <fs_db_serv_inst_before>-hec_sol_tier_stack_si_guid  IS NOT INITIAL.

                  CLEAR: lr_db_serv_inst->hec_sol_tier_stack_si_guid,
                         lr_db_serv_inst->hec_sol_tier_dsi_descr,
                         " Reset Server Type
                         lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid.

                ENDIF.

                IF lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid          IS INITIAL      AND
                   <fs_db_serv_inst_before>-hec_sol_tier_dsi_dbstype_guid  IS NOT INITIAL.

                  CLEAR: lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid,
                         lr_db_serv_inst->hec_db_srv_type_guid,
                         lr_db_serv_inst->hec_db_srv_type_value,
                         lr_db_serv_inst->hec_db_srv_type_descr,
                         " Reset Operating System
                         lr_db_serv_inst->hec_operating_sys_guid.

                ENDIF.

                IF lr_db_serv_inst->hec_operating_sys_guid         IS INITIAL   AND
                   <fs_db_serv_inst_before>-hec_operating_sys_guid IS NOT INITIAL.

                  CLEAR: lr_db_serv_inst->hec_sol_dbst_oper_sys_guid,
                         lr_db_serv_inst->hec_operating_sys_guid,
                         lr_db_serv_inst->hec_operating_sys_value,
                         lr_db_serv_inst->hec_operating_sys_descr,
                         " Reset Implementation Type
                         lr_db_serv_inst->hec_db_impl_type_guid.

                  lv_data_changed = abap_true.
                ENDIF.

                IF lr_db_serv_inst->hec_db_impl_type_guid         IS INITIAL     AND
                   <fs_db_serv_inst_before>-hec_db_impl_type_guid IS NOT INITIAL.

                  CLEAR: lr_db_serv_inst->hec_sol_dbst_impltype_guid,
                         lr_db_serv_inst->hec_db_impl_type_guid,
                         lr_db_serv_inst->hec_db_impl_type_value,
                         lr_db_serv_inst->hec_db_impl_type_descr,
                         " Reset Instance Type
                         lr_db_serv_inst->hec_db_inst_type_guid.

                  lv_data_changed = abap_true.
                ENDIF.

                IF lr_db_serv_inst->hec_db_inst_type_guid         IS INITIAL      AND
                   <fs_db_serv_inst_before>-hec_db_inst_type_guid IS NOT INITIAL.

                  CLEAR: lr_db_serv_inst->hec_sol_dbst_impty_instty_guid,
                         lr_db_serv_inst->hec_db_inst_type_guid,
                         lr_db_serv_inst->hec_db_inst_type_value,
                         lr_db_serv_inst->hec_db_inst_type_descr,
                         " Reset Allocation
                         lr_db_serv_inst->hec_db_allocation_guid.

                  lv_data_changed = abap_true.

                  LOOP AT lt_instance_db ASSIGNING FIELD-SYMBOL(<fs_instance_db>)
                    WHERE parent_key = lr_db_serv_inst->key.

                    " Add instance db to delete table
                    INSERT VALUE #( node = /hec1/if_configuration_c=>sc_node-instance_db
                                    key  = <fs_instance_db>-key ) INTO TABLE lt_act_param_delete.

                  ENDLOOP.
                ENDIF.

                IF lr_db_serv_inst->hec_db_allocation_guid        IS INITIAL      AND
                  <fs_db_serv_inst_before>-hec_db_allocation_guid IS NOT INITIAL.

                  CLEAR: lr_db_serv_inst->hec_db_allocation_descr,
                         lr_db_serv_inst->hec_db_allocation_value,
                         lr_db_serv_inst->hec_sol_dbst_imty_inty_al_guid,
                         lr_db_serv_inst->hec_db_tier_guid,
                         lr_db_serv_inst->hec_db_tier_descr.

                  lv_data_changed = abap_true.

                ENDIF.

              ENDIF. " if <fs_db_server_instance_before> is assigned.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_db_serv_inst->hec_operating_sys_value IS NOT INITIAL AND
                                                                       lr_db_serv_inst->hec_db_impl_type_guid       IS NOT INITIAL AND
                                                                       lr_db_serv_inst->hec_db_inst_type_guid       IS NOT INITIAL AND
                                                                       lr_db_serv_inst->hec_db_allocation_guid      IS NOT INITIAL AND
                                                                       lr_db_serv_inst->hec_phase_guid              IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete         ).

              IF lv_inst_status <> lr_db_serv_inst->hec_instance_status.
                lr_db_serv_inst->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify DB server instance
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_serv_inst->key
                                   is_data = lr_db_serv_inst ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_db_serv_inst_before>.
            ENDLOOP.

            "-----------------------------------
            " Set Update Instance DB action
            " to general
            "-----------------------------------
            IF lt_act_param_instance IS NOT INITIAL.
              CLEAR me->mr_act_param_instance.
              me->mr_act_param_instance = NEW /hec1/t_act_update_instance_db( lt_act_param_instance ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act_inst IN lt_act_param_instance
                                            ( key = wa_act_inst-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_instance_db )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_instance                                                                                                                ).

            ENDIF.

            "-----------------------------------
            " Set create Instance DB action to
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_instance_db( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_inst_db )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                ).
            ENDIF.


            "-----------------------------------
            " Set Delete action DB Instance
            " to general
            "-----------------------------------
            IF lt_act_param_delete IS NOT INITIAL.
              me->mr_act_param_delete = NEW /bobf/t_frw_node( lt_act_param_delete ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-delete_node )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_delete ).
            ENDIF.

            "-----------------------------------
            " Set update phase action to
            " general
            "-----------------------------------
            IF lt_act_param_phasing IS NOT INITIAL.
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.

            " ***************************************************************************
            " Update mode after tier update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server_instance-update_after_tier.

            "-----------------------------------
            " Release instance for selection
            "-----------------------------------
            LOOP AT lt_db_serv_inst REFERENCE INTO lr_db_serv_inst.
              ASSIGN lt_tier[ key = lr_db_serv_inst->parent_key ] TO <fs_tier>.

              IF <fs_tier> IS ASSIGNED.
                "-----------------------------------
                " Release instance for selection
                "-----------------------------------
                IF <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                   <fs_tier>-hec_tier_type_value      IS NOT INITIAL AND
                   <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL.
                  lv_release = abap_true.
                ENDIF.

                IF lv_release <> lr_db_serv_inst->hec_row_selectable.
                  lr_db_serv_inst->hec_row_selectable = lv_release.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Modify DB server instance
                "-----------------------------------
                IF lv_data_changed = abap_true.
                  io_modify->update( iv_node = is_ctx-node_key
                                     iv_key  = lr_db_serv_inst->key
                                     is_data = lr_db_serv_inst ).
                ENDIF.
              ENDIF. "  IF <fs_tier> IS ASSIGNED.

              UNASSIGN <fs_tier>.
              CLEAR: lv_release,
                     lv_data_changed.
            ENDLOOP.
        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_db_server_perf_cat.

    DATA: lt_db_serv_perf_cat         TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_serv_perf_cat_pernode TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_serv_perf_cat_before  TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_node                  TYPE /hec1/t_data_db_node_ct,
          lt_db_server                TYPE /hec1/t_data_db_serv_ct,
          lt_instance_db              TYPE /hec1/t_data_db_inst_ct,
          lt_db_storage_qty           TYPE /hec1/t_data_db_storage_qty_ct,
          lt_node_key                 TYPE /bobf/t_frw_key,
          lt_phase                    TYPE /hec1/t_data_phase_ct,
          lt_act_param                TYPE /hec1/t_act_create_db_qty,
          lt_act_param_server         TYPE /hec1/t_act_update_db_server,
          lt_act_param_node           TYPE /hec1/t_act_update_db_node,
          lt_act_param_storage        TYPE /bobf/t_frw_key,
          lt_act_param_succ           TYPE /hec1/t_act_set_success_predec,
          lt_act_param_storage_qty    TYPE /hec1/t_act_update_db_strg_qty,
          lt_act_param_phasing        TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.


    "-----------------------------------
    " Get data
    "-----------------------------------
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_serv_perf_cat ).

    " Get DB node (parent)
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-to_parent
                                      IMPORTING et_data        = lt_db_node ).


    " Get landscape( APM GUID), delivery unit and data center
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server_perform_cat-create.

            " Get for each DB node
            " the DB server performance category
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_node
                                                        it_key         = VALUE #( FOR wa_node IN lt_db_node
                                                                                 ( key = wa_node-key )      )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                                              IMPORTING et_data        = lt_db_serv_perf_cat_pernode ).



            LOOP AT        lt_db_serv_perf_cat
            REFERENCE INTO DATA(lr_db_serv_perf_cat)
                WHERE hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master.

              "-----------------------------------
              " Set Value List Quantity
              " - Server Performance Category
              "-----------------------------------
              lr_db_serv_perf_cat->hec_srv_perf_cat_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server_perf_cat(
                                                                                     iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                     iv_inf_provider_guid   = lr_dlvy_unit->hec_inf_provider_guid
                                                                                     iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_db_serv_perf_cat->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL )
                                                                                     iv_server_type_guid    = lr_db_serv_perf_cat->hec_db_srv_type_guid
                                                                                     iv_is_app_server       = abap_false ) )
              THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
              ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " TODO this might need a more complex logic depending on the number of entries
              lr_db_serv_perf_cat->hec_delete_visible = abap_true.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_db_serv_perf_cat->hec_srv_perf_cat_guid IS NOT INITIAL AND
                                                                             lr_db_serv_perf_cat->hec_phase_guid        IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete      ).

              IF lv_inst_status <> lr_db_serv_perf_cat->hec_instance_status.
                lr_db_serv_perf_cat->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_db_node[ key = lr_db_serv_perf_cat->parent_key ] TO FIELD-SYMBOL(<fs_db_node>).
              IF <fs_db_node> IS ASSIGNED.
                IF <fs_db_node>-hec_db_srv_perf_cat_qty IS NOT INITIAL AND
                   <fs_db_node>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_db_serv_perf_cat->hec_row_selectable.
                lr_db_serv_perf_cat->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " DB server storage amount
              "-----------------------------------
              IF NOT lr_db_serv_perf_cat->hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-tenant.
                INSERT VALUE #( key                    = lr_db_serv_perf_cat->key
                                parent_key             = lr_db_serv_perf_cat->parent_key
                                hec_storage_amount_qty = lr_db_serv_perf_cat->hec_storage_qty ) INTO TABLE lt_act_param.
              ENDIF.

              "-----------------------------------
              " Fill action table for setting
              " DB server performance category
              " successor/predecessor
              "-----------------------------------
              DATA(lv_node_count) = REDUCE i( INIT x = 0
                                              FOR <l> IN lt_db_serv_perf_cat_pernode WHERE ( parent_key = lr_db_serv_perf_cat->parent_key )
                                              NEXT x = x + 1                                                                                  ).

              IF NOT line_exists( lt_act_param_succ[ key = lr_db_serv_perf_cat->parent_key ] ) AND lv_node_count > 1.
                TRY.
                    INSERT VALUE #( key                  = lr_db_serv_perf_cat->parent_key
                                    parent_key           = lt_db_node[ key = lr_db_serv_perf_cat->parent_key ]-parent_key
                                    hec_no_children_node = lv_node_count                                                  ) INTO TABLE lt_act_param_succ.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.

              "-----------------------------------
              " Modify DB server performance
              " category
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_serv_perf_cat->key
                                   is_data = lr_db_serv_perf_cat ).
              ENDIF.

              UNASSIGN <fs_db_node>.
              CLEAR: lv_inst_status,
                     lv_release,
                     lv_data_changed,
                     lv_node_count.

            ENDLOOP.

            "-----------------------------------
            " Set successor/predecessor action
            " to GENERAL
            "-----------------------------------
            IF lt_act_param_succ IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_set_success_predec( lt_act_param_succ ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key  = /hec1/if_configuration_c=>sc_node-db_node
                                             assoc_key = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat )
                  it_key          = VALUE #( FOR wa_act_succ IN lt_act_param_succ
                                            ( key = wa_act_succ-key )    )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-set_success_predec )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

            ENDIF.

            "-----------------------------------
            " Set create DB server storage
            " amount and create DB server
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_db_qty( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_qty )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                              ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_server )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                                                                        ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server_perform_cat-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_db_serv_perf_cat_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get DB Node
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-to_parent
                                              IMPORTING et_target_key  = DATA(lt_db_node_key)
                                                        et_data        = lt_db_node ).

            " Get instance DB
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_node
                                                        it_key         = lt_db_node_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_node-to_parent
                                              IMPORTING et_target_key  = DATA(lt_instance_db_key)
                                                        et_data        = lt_instance_db ).

            " Get DB Server
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_server
                                              IMPORTING et_data        = lt_db_server
                                                        et_target_key  = DATA(lt_db_server_key) ).

            " Get Storage Qty
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount
                                              IMPORTING et_data        = lt_db_storage_qty ).


            "-----------------------------------
            " Get server performance category
            "-----------------------------------
            DATA(lt_range_table) = VALUE /hec1/t_selection_range( FOR wa_spc IN lt_db_serv_perf_cat
                                                                ( option = /hec1/if_config_constants=>gc_range_option-eq
                                                                  sign   = /hec1/if_config_constants=>gc_range_sign-i
                                                                  low    = wa_spc-hec_srv_perf_cat_guid                   ) ).

            SELECT *
              FROM /hec1/i_dbservperfcatbasic
             WHERE hec_apm_guid = @lr_landscape->hec_apm_guid AND
                   hec_srv_perf_cat_guid IN @lt_range_table
              INTO TABLE @DATA(lt_serv_perf_cat).


            "-----------------------------------
            " Get server
            "-----------------------------------
            CLEAR lt_range_table.
            lt_range_table = VALUE /hec1/t_selection_range( FOR wa IN lt_db_serv_perf_cat
                                                           ( option = /hec1/if_config_constants=>gc_range_option-eq
                                                             sign   = /hec1/if_config_constants=>gc_range_sign-i
                                                             low    = wa-hec_srv_perf_cat_guid                   ) ).

            SELECT *                          "#EC CI_ALL_FIELDS_NEEDED
              FROM /hec1/i_serverbasic
             WHERE hec_apm_guid = @lr_landscape->hec_apm_guid AND
                   hec_srv_perf_cat_guid   IN @lt_range_table
              INTO TABLE @DATA(lt_server_data).



            LOOP AT lt_db_serv_perf_cat REFERENCE INTO lr_db_serv_perf_cat.
              ASSIGN lt_db_serv_perf_cat_before[ key = lr_db_serv_perf_cat->key ] TO FIELD-SYMBOL(<fs_db_serv_perf_cat_before>).

              IF <fs_db_serv_perf_cat_before> IS ASSIGNED.
                TRY.
                    DATA(ls_instance_db) = lt_instance_db[ key = lt_db_node[ key = lr_db_serv_perf_cat->parent_key ]-parent_key ].
                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.

                "-----------------------------------
                " DB server performance category
                " has changed
                "-----------------------------------
                IF lr_db_serv_perf_cat->hec_srv_perf_cat_guid IS NOT INITIAL                                             AND
                   lr_db_serv_perf_cat->hec_srv_perf_cat_guid <> <fs_db_serv_perf_cat_before>-hec_srv_perf_cat_guid.

                  TRY.
                      DATA(ls_serv_perf_cat) = lt_serv_perf_cat[ hec_srv_perf_cat_guid = lr_db_serv_perf_cat->hec_srv_perf_cat_guid ].

                      IF ls_instance_db-hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-container.

                        lr_db_serv_perf_cat->hec_srv_perf_cat_descr        = ls_serv_perf_cat-hec_srv_perf_cat_descr.
                        lr_db_serv_perf_cat->hec_db_intended_srv_ram_class = ls_serv_perf_cat-hec_srv_ram_class.
                        lr_db_serv_perf_cat->hec_tree_descr                = ls_serv_perf_cat-hec_srv_perf_cat_descr. "#EC CI_FLDEXT_OK[2215424]

                      ELSE.
                        lr_db_serv_perf_cat->hec_srv_perf_cat_descr = ls_serv_perf_cat-hec_srv_perf_cat_descr.
                        lr_db_serv_perf_cat->hec_srv_ram_class      = ls_serv_perf_cat-hec_srv_ram_class.
                        lr_db_serv_perf_cat->hec_srv_cpu_class      = ls_serv_perf_cat-hec_srv_cpu_class.
                        lr_db_serv_perf_cat->hec_tree_descr         = ls_serv_perf_cat-hec_srv_perf_cat_descr. "#EC CI_FLDEXT_OK[2215424]
                      ENDIF.

                      lv_data_changed = abap_true.

                      " Set Value List Quantity
                      lr_db_serv_perf_cat->hec_srv_perf_cat_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server_perf_cat(
                                                                                             iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                             iv_inf_provider_guid   = lr_dlvy_unit->hec_inf_provider_guid
                                                                                             iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_db_serv_perf_cat->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL )
                                                                                             iv_server_type_guid    = lr_db_serv_perf_cat->hec_db_srv_type_guid
                                                                                             iv_is_app_server       = abap_false ) )
                                                                           THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                           ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.


                  TRY.
                      DATA(lv_datacenter_guid) = lt_datacenter[ hec_node_datacenter = lr_db_serv_perf_cat->hec_tier_datacenter_guid ]-hec_datacenter_guid.

                      DATA(lt_server) = /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server( iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                                                   iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                                                                   iv_sec_datacenter_guid = lv_datacenter_guid
                                                                                                                   iv_srv_perf_cat_guid   = lr_db_serv_perf_cat->hec_srv_perf_cat_guid ).
                      "-----------------------------------
                      " Fill action table for Update
                      " DB server
                      "-----------------------------------
                      IF lines( lt_server ) = 1.
                        INSERT VALUE #( key                 = lt_db_server[ parent_key = lr_db_serv_perf_cat->key ]-key
                                        parent_key          = lr_db_serv_perf_cat->key
                                        hec_ip_server_guid  = lt_server[ 1 ]-value
                                        do_update_db_server = abap_true                                                 ) INTO TABLE lt_act_param_server.
                      ENDIF.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  CLEAR: lv_datacenter_guid,
                         lt_server.

                  "-----------------------------------
                  " Fill action table for update
                  " DB server storage amount
                  "-----------------------------------
                  INSERT VALUE #( parent_key = lr_db_serv_perf_cat->key ) INTO TABLE lt_act_param_storage_qty.
                ENDIF. " IF ls_db_server_perf_cat-hec_srv_perf_cat_guid IS NOT INITIAL AND ...


                "-----------------------------------
                " DB server storage is added
                "-----------------------------------
                IF lr_db_serv_perf_cat->hec_storage_qty > <fs_db_serv_perf_cat_before>-hec_storage_qty.
                  "-----------------------------------
                  " Fill action table for create
                  " DB server storage amount
                  "-----------------------------------
                  INSERT VALUE #( key                    = lr_db_serv_perf_cat->key
                                  parent_key             = lr_db_serv_perf_cat->parent_key
                                  hec_storage_amount_qty = lr_db_serv_perf_cat->hec_storage_qty - <fs_db_serv_perf_cat_before>-hec_storage_qty ) INTO TABLE lt_act_param.

                  "-----------------------------------
                  " Fill action table for create
                  " DB server storage
                  "-----------------------------------
                  TRY.
                      " DB Storage is added without any parameters necessary
                      INSERT VALUE #( key = lt_db_server[ parent_key = lr_db_serv_perf_cat->key ]-key ) INTO TABLE lt_act_param_storage.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  " Success message
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_storage_added
                                                                 iv_severity = /bobf/cm_frw=>co_severity_success
                                                                 iv_attr1    = CONV #( lr_db_serv_perf_cat->hec_storage_qty -
                                                                               <fs_db_serv_perf_cat_before>-hec_storage_qty )
                                                       CHANGING  co_message  = eo_message ).

                  " Set flag for deleting subnodes of standby/worker node
                  IF ( lr_db_serv_perf_cat->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                       lr_db_serv_perf_cat->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi   )   AND
                       lr_db_serv_perf_cat->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                       lr_db_serv_perf_cat->hec_db_node_default          = abap_true.
                    lv_data_changed         = abap_true.
                    DATA(lv_delete_subnode) = abap_true.
                  ENDIF.

                ELSEIF lr_db_serv_perf_cat->hec_storage_qty < <fs_db_serv_perf_cat_before>-hec_storage_qty                                                       AND
                       lr_db_serv_perf_cat->hec_storage_qty < lines( VALUE /hec1/t_data_db_storage_qty_ct( FOR db_storage_qty IN lt_db_storage_qty
                                                                                                           WHERE ( parent_key = lr_db_serv_perf_cat->key )
                                                                                                            ( db_storage_qty )                             ) ).

                  DATA(lv_attr_name) = /hec1/if_configuration_c=>sc_node_attribute-db_server_perform_cat-hec_storage_qty.

                  " Error
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                 is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                               key      = lr_db_serv_perf_cat->key
                                                                                               attributes = VALUE #( ( lv_attr_name ) ) )
                                                       CHANGING  co_message         = eo_message ).

                  " Set node number to value before update
                  lr_db_serv_perf_cat->hec_storage_qty = <fs_db_serv_perf_cat_before>-hec_storage_qty.
                  lv_data_changed = abap_true.
                ENDIF. " IF ls_db_server_perf_cat-hec_storage_qty > ls_db_server_perf_cat_old-hec_storage_qty.

                "-----------------------------------
                " Phase has changed
                "-----------------------------------
                IF lr_db_serv_perf_cat->hec_phase_guid <> <fs_db_serv_perf_cat_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_db_serv_perf_cat->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                     lr_db_serv_perf_cat->hec_db_node_default          = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_db_serv_perf_cat->key
                                    hec_phase_guid_new = lr_db_serv_perf_cat->hec_phase_guid
                                    hec_phase_guid_old = <fs_db_serv_perf_cat_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_db_serv_perf_cat->hec_phase_changed = abap_true.
                  lv_data_changed                        = abap_true.

                  " Set flag for deleting subnodes of standby/worker node
                  IF ( lr_db_serv_perf_cat->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                       lr_db_serv_perf_cat->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi   )   AND
                       lr_db_serv_perf_cat->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                       lr_db_serv_perf_cat->hec_db_node_default          = abap_true.
                    lv_delete_subnode = abap_true.
                  ENDIF.
                ENDIF. "phasing changed
              ENDIF. " IF <fs_db_serv_perf_cat_before> IS ASSIGNED.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_db_serv_perf_cat->hec_srv_perf_cat_guid IS NOT INITIAL AND
                                                                       lr_db_serv_perf_cat->hec_phase_guid            IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete          ).

              IF lv_inst_status <> lr_db_serv_perf_cat->hec_instance_status.
                lr_db_serv_perf_cat->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for delete
              " subnodes of DB standby/worker node
              " or relase standby/worker node
              "-----------------------------------
              IF ( lr_db_serv_perf_cat->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                   lr_db_serv_perf_cat->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi   )   AND
                   lr_db_serv_perf_cat->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                   lr_db_serv_perf_cat->hec_db_node_default          = abap_true                                               AND
                   lv_data_changed                                   = abap_true.

                IF NOT line_exists( lt_act_param_node[ key = lr_db_serv_perf_cat->parent_key ] ).
                  TRY.
                      INSERT VALUE #( key               = lr_db_serv_perf_cat->parent_key
                                      parent_key        = lt_db_node[ key = lr_db_serv_perf_cat->parent_key ]-parent_key
                                      do_release_node   = COND #( WHEN lr_db_serv_perf_cat->hec_instance_status         = /hec1/if_config_constants=>gc_instance_status-complete   AND
                                                                       <fs_db_serv_perf_cat_before>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                                  THEN abap_true
                                                                  ELSE abap_false                                                  )
                                      do_delete_subnode = COND #( WHEN lr_db_serv_perf_cat->hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete OR
                                                                       lv_delete_subnode                        = abap_true
                                                                  THEN abap_true
                                                                  ELSE abap_false                                                                                     ) ) INTO TABLE lt_act_param_node.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                ENDIF.
              ENDIF. " IF ( lr_db_serv_perf_cat->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR...


              "-----------------------------------
              " Modify DB server performance
              " category
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_serv_perf_cat->key
                                   is_data = lr_db_serv_perf_cat ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_attr_name,
                     lv_delete_subnode.

              UNASSIGN <fs_db_serv_perf_cat_before>.
            ENDLOOP.


            "-----------------------------------
            " Set update Phasing action to
            " general
            "-----------------------------------
            IF lt_act_param_phasing IS NOT INITIAL.
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.

            "-----------------------------------
            " Set create DB server storage
            " amount and DB server storage
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_db_qty( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_qty )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                              ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                              node_key = /hec1/if_configuration_c=>sc_node-db_server )
                  it_key          = VALUE #( FOR wa_act_serv IN lt_act_param_storage
                                            ( key = wa_act_serv-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_storage )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                                                                        ).

            ENDIF.

            "-----------------------------------
            " Set Update DB Storage Amount
            " to general
            "-----------------------------------
            IF lt_act_param_storage_qty IS NOT INITIAL.

              me->mr_act_param_db_storage_amount = NEW /hec1/t_act_update_db_strg_qty( FOR strg_qty IN lt_act_param_storage_qty
                ( parent_key = strg_qty-parent_key
                do_update_storage = abap_true ) ).

              " Update DB storage amount (in general)
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR strg_qty IN lt_act_param_storage_qty   "pass the server performance category key
                                           ( key = strg_qty-parent_key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_storage_amount )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_db_storage_amount ).
            ENDIF.

            "-----------------------------------
            " Set Update DB server action
            " to general
            "-----------------------------------
            IF lt_act_param_server IS NOT INITIAL.
              CLEAR me->mr_act_param1.
              me->mr_act_param1 = NEW /hec1/t_act_update_db_server( lt_act_param_server ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act_server IN lt_act_param_server
                                            ( key = wa_act_server-parent_key )        )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_server )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param1                                                                                                              ).
            ENDIF.


            "-----------------------------------
            " Set update DB node action to
            " general
            "-----------------------------------
            IF lt_act_param_node IS NOT INITIAL.
              CLEAR me->mr_act_param_db_node.
              me->mr_act_param_db_node = NEW /hec1/t_act_update_db_node( lt_act_param_node ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-db_node )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param_node
                                              ( key = wa_act_node-key )     )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_db_node                                                                                                       ).
            ENDIF.


            " ***************************************************************************
            " Update mode after DB node update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server_perform_cat-update_after_node.

            LOOP AT lt_db_serv_perf_cat REFERENCE INTO lr_db_serv_perf_cat.
              ASSIGN lt_db_node[ key = lr_db_serv_perf_cat->parent_key ] TO <fs_db_node>.

              IF <fs_db_node> IS ASSIGNED.
                "-----------------------------------
                " Release instance for selection
                "-----------------------------------
                IF <fs_db_node>-hec_db_srv_perf_cat_qty IS NOT INITIAL AND
                   <fs_db_node>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.


                IF lv_release <> lr_db_serv_perf_cat->hec_row_selectable.
                  lr_db_serv_perf_cat->hec_row_selectable = lv_release.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Update DB server cluster type
                "-----------------------------------
                IF lr_db_serv_perf_cat->hec_db_cluster_type_value <> <fs_db_node>-hec_db_cluster_type_value.
                  lr_db_serv_perf_cat->hec_db_cluster_type_value = <fs_db_node>-hec_db_cluster_type_value.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Modify DB server performance
                " category
                "-----------------------------------
                IF lv_data_changed = abap_true.
                  io_modify->update( iv_node = is_ctx-node_key
                                     iv_key  = lr_db_serv_perf_cat->key
                                     is_data = lr_db_serv_perf_cat ).
                ENDIF.
              ENDIF. " IF <fs_db_node> IS ASSIGNED.

              UNASSIGN <fs_db_node>.
              CLEAR: lv_data_changed,
                     lv_release.

            ENDLOOP. " LOOP AT lt_db_serv_perf_cat...
        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_db_storage.

    DATA: lt_db_server            TYPE /hec1/t_data_db_serv_ct,
          lt_db_storage           TYPE /hec1/t_data_db_storage_ct,
          lt_db_storage_perserver TYPE /hec1/t_data_db_storage_ct,
          lt_db_storage_before    TYPE /hec1/t_data_db_storage_ct,
          lt_db_storage_succ      TYPE /hec1/t_data_db_storage_ct,
          lt_db_node              TYPE /hec1/t_data_db_node_ct,
          lt_db_serv_perf_cat     TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_storage_qty       TYPE /hec1/t_data_db_storage_qty_ct,
          lt_db_backup            TYPE /hec1/t_data_db_backup_ct,
          lt_phase                TYPE /hec1/t_data_phase_ct,
          lt_act_param            TYPE /hec1/t_act_create_db_backup,
          lt_act_param_storage    TYPE /bobf/t_frw_key,
          lt_act_param_phasing    TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_storage ).

    " Get DB server (parent)
    " Get DB server (parent)
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_storage-to_parent
                                      IMPORTING et_data        = lt_db_server ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage-create.

            " Get for each DB server the DB storage
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server
                                                        it_key         = VALUE #( FOR wa_serv IN lt_db_server
                                                                                 ( key = wa_serv-key )                )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server-db_storage
                                              IMPORTING et_data        = lt_db_storage_perserver ).

            LOOP AT        lt_db_storage
            REFERENCE INTO DATA(lr_db_storage)
                     WHERE hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master.

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              lr_db_storage->hec_storage_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_storage(
                                                                          iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                          iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                          iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_db_storage->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL ) ) )
                                                        THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                        ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              lr_db_storage->hec_delete_visible = abap_false.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_db_storage->hec_ip_storage_guid IS NOT INITIAL AND
                                                                             lr_db_storage->hec_phase_guid      IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_db_storage->hec_instance_status.
                lr_db_storage->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_db_server[ key = lr_db_storage->parent_key ] TO FIELD-SYMBOL(<fs_db_server>).
              IF <fs_db_server> IS ASSIGNED.
                IF <fs_db_server>-hec_ip_server_guid IS NOT INITIAL AND
                   <fs_db_server>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_db_storage->hec_row_selectable.
                lr_db_storage->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " DB server storage backup
              "-----------------------------------
              IF lr_db_storage->hec_backup_relev_value = '01'. " mandantory
                INSERT VALUE #( key            = lr_db_storage->key
                                parent_key     = lr_db_storage->parent_key
                                hec_backup_qty = lr_db_storage->hec_backup_qty ) INTO TABLE lt_act_param.
              ENDIF.

              "-----------------------------------
              " Fill action table for setting
              " App server storage
              " successor/predecessor
              "-----------------------------------
              DATA(lv_node_count) = REDUCE i( INIT x = 0
                                              FOR <l> IN lt_db_storage_perserver WHERE ( parent_key = lr_db_storage->parent_key )
                                              NEXT x = x + 1                                                                        ).

              IF NOT line_exists( lt_act_param_storage[ key = lr_db_storage->key ] ) AND lv_node_count > 1.
                TRY.
                    INSERT VALUE #( key = lr_db_storage->key ) INTO TABLE lt_act_param_storage.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.

              "-----------------------------------
              " Modify DB server storage
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_storage->key
                                   is_data = lr_db_storage ).
              ENDIF.

              UNASSIGN <fs_db_server>.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release,
                     lv_node_count.

            ENDLOOP.

            "-----------------------------------
            " Set create DB server storage
            " backup action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_db_backup( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_backup )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

            ENDIF.

            "-----------------------------------
            " Set update DB storage action
            " to GENERAL
            "-----------------------------------
            IF lt_act_param_storage IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-db_storage )
                  it_key          = lt_act_param_storage
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_storage )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                                                                          ).
            ENDIF.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_db_storage_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get Backup
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_storage-db_storage_backup
                                              IMPORTING et_data        = lt_db_backup ).


            LOOP AT lt_db_storage REFERENCE INTO lr_db_storage.

              ASSIGN lt_db_storage_before[ key = lr_db_storage->key ] TO FIELD-SYMBOL(<fs_db_storage_before>).
              IF <fs_db_storage_before> IS ASSIGNED.
                "-----------------------------------
                " DB storage has changed
                "-----------------------------------
                IF lr_db_storage->hec_ip_storage_guid IS INITIAL    OR ( lr_db_storage->hec_ip_storage_guid IS NOT INITIAL AND
                   lr_db_storage->hec_ip_storage_guid  <> <fs_db_storage_before>-hec_ip_storage_guid ).

                  ASSIGN lt_db_server[ key = lr_db_storage->parent_key ] TO <fs_db_server>.

                  IF <fs_db_server> IS ASSIGNED.
                    SELECT SINGLE *
                      FROM /hec1/i_storagelbbasic
                     WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid              AND
                           hec_sec_datacenter_guid = @<fs_db_server>-hec_sec_datacenter_guid  AND
                           hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid     AND
                           hec_ip_storage_guid     = @lr_db_storage->hec_ip_storage_guid
                      INTO @DATA(ls_storage).

                    SELECT SINGLE * FROM /hec1/c_cbp_lb "#EC CI_ALL_FIELDS_NEEDED
                       INTO @DATA(ls_pricing)
                      WHERE hec_price_lb = @ls_storage-hec_cb_pricing_lb_guid.

                    lr_db_storage->*                   = CORRESPONDING #( BASE ( lr_db_storage->* ) ls_pricing ).
                    lr_db_storage->hec_ip_storage_guid = ls_storage-hec_ip_storage_guid.
                    lr_db_storage->hec_storage_descr   = ls_storage-hec_storage_descr.
                    lr_db_storage->hec_month_price_fee = lr_db_storage->hec_storage_quantity * lr_db_storage->hec_month_price_eur.
                    lr_db_storage->hec_tree_descr      = ls_storage-hec_storage_descr. "#EC CI_FLDEXT_OK[2215424]

                    lv_data_changed                    = abap_true.

                    " Set Value List Quantity - DB Storage
                    lr_db_storage->hec_storage_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_storage(
                                                                                iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                                iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_db_storage->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL ) ) )
                                                              THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                              ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                  ENDIF. " <fs_db_server> is assigned
                ENDIF. " db storage changed

                "-----------------------------------
                " DB storage amount has changed
                "-----------------------------------
                IF lr_db_storage->hec_storage_quantity IS NOT INITIAL                                 AND
                   lr_db_storage->hec_storage_quantity <> <fs_db_storage_before>-hec_storage_quantity.
                  lr_db_storage->hec_month_price_fee = lr_db_storage->hec_storage_quantity * lr_db_storage->hec_month_price_eur.

                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Fill action table for create
                " DB server storage backup
                "-----------------------------------
                IF lr_db_storage->hec_backup_qty > <fs_db_storage_before>-hec_backup_qty.

                  INSERT VALUE #( key            = lr_db_storage->key
                                  parent_key     = lr_db_storage->parent_key
                                  hec_backup_qty = lr_db_storage->hec_backup_qty - <fs_db_storage_before>-hec_backup_qty ) INTO TABLE lt_act_param.

                  " Success message
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_backup_added
                                                                 iv_severity = /bobf/cm_frw=>co_severity_success
                                                                 iv_attr1    = CONV #( lr_db_storage->hec_backup_qty -
                                                                               <fs_db_storage_before>-hec_backup_qty )
                                                       CHANGING  co_message  = eo_message ).

                ELSEIF lr_db_storage->hec_backup_qty < <fs_db_storage_before>-hec_backup_qty
                   AND lr_db_storage->hec_backup_qty < lines( VALUE /hec1/t_data_db_backup_ct( FOR db_backup IN lt_db_backup
                                                                                                     WHERE ( parent_key = lr_db_storage->key )
                                                                                                     ( db_backup ) ) ).
                  DATA(lv_attr_name) = /hec1/if_configuration_c=>sc_node_attribute-db_storage-hec_backup_qty.

                  " Error message
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                 is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                               key      = lr_db_storage->key
                                                                                               attributes = VALUE #( ( lv_attr_name ) ) )
                                                       CHANGING  co_message         = eo_message ).

                  " Set node number to value before update
                  lr_db_storage->hec_backup_qty = <fs_db_storage_before>-hec_backup_qty.
                  lv_data_changed = abap_true.
                ENDIF. " IF lr_db_storage->hec_dst_backup_qty > <fs_db_storage_before>-hec_dst_backup_qty.

                "-----------------------------------
                " Phase has changed - update phase and inherit phase assignment
                "-----------------------------------
                IF lr_db_storage->hec_phase_guid NE <fs_db_storage_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_db_storage->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                     lr_db_storage->hec_db_node_default          = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_db_storage->key
                                    hec_phase_guid_new = lr_db_storage->hec_phase_guid
                                    hec_phase_guid_old = <fs_db_storage_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_db_storage->hec_phase_changed = abap_true.
                  lv_data_changed                  = abap_true.

                ENDIF. "phasing changed
              ENDIF.  " IF <fs_db_storage_before> IS ASSIGNED.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_db_storage->hec_ip_storage_guid IS NOT INITIAL AND
                                                                       lr_db_storage->hec_phase_guid      IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_db_storage->hec_instance_status.
                lr_db_storage->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify DB server storage
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_storage->key
                                   is_data = lr_db_storage ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_attr_name,
                     ls_storage,
                     ls_pricing.

              UNASSIGN <fs_db_storage_before>.
            ENDLOOP.

            "-----------------------------------
            " Update Phasing
            "-----------------------------------
            IF lt_act_param_phasing IS NOT INITIAL.
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.

            "-----------------------------------
            " Set create DB server storage
            " backup action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_db_backup( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_backup )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

            ENDIF.

            " ***************************************************************************
            " Update mode after server update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage-update_after_server.

            LOOP AT lt_db_storage REFERENCE INTO lr_db_storage.
              ASSIGN lt_db_server[ key = lr_db_storage->parent_key ] TO <fs_db_server>.

              IF <fs_db_server> IS ASSIGNED.
                IF <fs_db_server>-hec_ip_server_guid IS NOT INITIAL AND
                   <fs_db_server>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              IF lv_release <> lr_db_storage->hec_row_selectable.
                lr_db_storage->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Update DB server cluster type
              "-----------------------------------
              IF lr_db_storage->hec_db_cluster_type_value <> <fs_db_server>-hec_db_cluster_type_value.
                lr_db_storage->hec_db_cluster_type_value = <fs_db_server>-hec_db_cluster_type_value.
                lv_data_changed = abap_true.
              ENDIF.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_storage->key
                                   is_data = lr_db_storage ).
              ENDIF.

              UNASSIGN <fs_db_server>.
              CLEAR: lv_release,
                     lv_data_changed.
            ENDLOOP. "  LOOP AT lt_db_storage
        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_db_storage_amount.

    DATA: lt_db_storage_qty        TYPE /hec1/t_data_db_storage_qty_ct,
          lt_db_storage_qty_perspc TYPE /hec1/t_data_db_storage_qty_ct,
          lt_db_storage_qty_before TYPE /hec1/t_data_db_storage_qty_ct,
          lr_db_storage_qty        TYPE REF TO /hec1/s_data_db_storage_qty_cs,
          lt_db_node               TYPE /hec1/t_data_db_node_ct,
          lt_db_serv_perf_cat      TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_server             TYPE /hec1/t_data_db_serv_ct,
          lt_db_storage            TYPE /hec1/t_data_db_storage_ct,
          lt_phase                 TYPE /hec1/t_data_phase_ct,
          lt_act_param_node        TYPE /hec1/t_act_update_db_node,
          lt_act_param_storage     TYPE /bobf/t_frw_key,
          lt_act_param_succ        TYPE /hec1/t_act_set_success_predec,
          lt_act_param_phasing     TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    "-----------------------------------
    " Get data
    "-----------------------------------
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_storage_qty ).

    " Get DB server performance category (parent)
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_storage_amount-to_parent
                                      IMPORTING et_data        = lt_db_serv_perf_cat ).

    " Get landscape( APM GUID), delivery unit and data center
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage_amount-create.

            " Get for each DB server performance category
            " the DB storage amount
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                        it_key         = VALUE #( FOR wa_spc IN lt_db_serv_perf_cat
                                                                                 ( key = wa_spc-key )               )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount
                                              IMPORTING et_data        = lt_db_storage_qty_perspc ).


            LOOP AT lt_db_storage_qty REFERENCE INTO lr_db_storage_qty.

              lr_db_storage_qty->hec_delete_visible = abap_true.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_db_storage_qty->hec_phase_guid IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_db_storage_qty->hec_instance_status.
                lr_db_storage_qty->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.

                " If standby node exist
                IF ( lr_db_storage_qty->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                     lr_db_storage_qty->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi   )  AND
                     lr_db_storage_qty->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                     lr_db_storage_qty->hec_db_node_default          = abap_true                                               AND
                     lr_db_storage_qty->hec_instance_status          = /hec1/if_config_constants=>gc_instance_status-complete.

                  io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                              it_key         = VALUE #( ( key = lr_db_storage_qty->key ) )
                                                              iv_fill_data   = abap_false
                                                              iv_association = /hec1/if_configuration_c=>sc_association-db_storage_amount-to_def_master_node
                                                    IMPORTING et_target_key  = DATA(lt_key) ).

                  IF NOT line_exists( lt_act_param_node[ key = lt_key[ 1 ]-key ] ).
                    TRY.
                        INSERT VALUE #( key             = lt_key[ 1 ]-key
                                        do_release_node = abap_true       ) INTO TABLE lt_act_param_node.
                      CATCH cx_sy_itab_line_not_found.
                    ENDTRY.
                  ENDIF.
                ENDIF.
              ENDIF. " IF lv_inst_status <> lr_db_storage_qty->hec_instance_status.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_db_serv_perf_cat[ key = lr_db_storage_qty->parent_key ] TO FIELD-SYMBOL(<fs_db_serv_perf_cat>).
              IF <fs_db_serv_perf_cat> IS ASSIGNED.
                IF <fs_db_serv_perf_cat>-hec_srv_perf_cat_guid IS NOT INITIAL AND
                   <fs_db_serv_perf_cat>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_db_storage_qty->hec_row_selectable.
                lr_db_storage_qty->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for setting
              " DB server storage amount
              " successor/predecessor
              "-----------------------------------
              DATA(lv_node_count) = REDUCE i( INIT x = 0
                                              FOR <l> IN lt_db_storage_qty_perspc WHERE ( parent_key = lr_db_storage_qty->parent_key )
                                              NEXT x = x + 1                                                                              ).

              IF NOT line_exists( lt_act_param_succ[ key = lr_db_storage_qty->parent_key ] ) AND lv_node_count > 1.
                TRY.
                    INSERT VALUE #( key         = lr_db_storage_qty->parent_key
                                    parent_key  = lt_db_serv_perf_cat[ key = lr_db_storage_qty->parent_key ]-parent_key
                                    hec_no_children_node = lv_node_count                                                         ) INTO TABLE lt_act_param_succ.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.


              "-----------------------------------
              " Modify DB storage amount
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_storage_qty->key
                                   is_data = lr_db_storage_qty ).
              ENDIF.

              UNASSIGN <fs_db_serv_perf_cat>.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release,
                     lv_node_count.

            ENDLOOP.


            "-----------------------------------
            " Set update DB node action to
            " general
            "-----------------------------------
            IF lt_act_param_node IS NOT INITIAL.
              CLEAR me->mr_act_param_db_node.
              me->mr_act_param_db_node = NEW /hec1/t_act_update_db_node( lt_act_param_node ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-db_node )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param_node
                                              ( key = wa_act_node-key )     )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_db_node                                                                                                       ).
            ENDIF.


            "-----------------------------------
            " Set successor/predecessor action
            " to GENERAL
            "-----------------------------------
            IF lt_act_param_succ IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_set_success_predec( lt_act_param_succ ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key  = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                             assoc_key = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount )
                  it_key          = VALUE #( FOR wa_act_succ IN lt_act_param_succ
                                            ( key = wa_act_succ-key )    )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-set_success_predec )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage_amount-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_db_storage_qty_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_storage_amount-to_parent
                                              IMPORTING et_target_key  = DATA(lt_db_serv_pc_key) ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                        it_key         = lt_db_serv_pc_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_server
                                              IMPORTING et_target_key  = DATA(lt_db_serv_key)
                                                        et_key_link    = DATA(lt_perf_cat_to_serv_link) ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server
                                                        it_key         = lt_db_serv_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server-db_storage
                                              IMPORTING et_target_key  = DATA(lt_db_storage_key)
                                                        et_key_link    = DATA(lt_serv_to_storage_link) ).


            LOOP AT lt_db_storage_qty REFERENCE INTO lr_db_storage_qty.

              ASSIGN lt_db_storage_qty_before[ key = lr_db_storage_qty->key ] TO FIELD-SYMBOL(<fs_db_storage_qty_before>).
              IF <fs_db_storage_qty_before> IS ASSIGNED.
                "-----------------------------------
                " Physical, virtual or additional storage
                " has changed
                "-----------------------------------
                IF lr_db_storage_qty->hec_dsq_main_stor_qty_physical <> <fs_db_storage_qty_before>-hec_dsq_main_stor_qty_physical OR
                   lr_db_storage_qty->hec_dsq_main_stor_qty_virtual  <> <fs_db_storage_qty_before>-hec_dsq_main_stor_qty_virtual  OR
                   lr_db_storage_qty->hec_dsq_additional_stor_qty    <> <fs_db_storage_qty_before>-hec_dsq_additional_stor_qty OR
                   lr_db_storage_qty->hec_successor_guid             <> <fs_db_storage_qty_before>-hec_successor_guid OR
                   lr_db_storage_qty->hec_predecessor_guid           <> <fs_db_storage_qty_before>-hec_predecessor_guid.

                  lr_db_storage_qty->hec_tree_descr = |{ lr_db_storage_qty->hec_dsq_main_stor_qty_virtual } + { lr_db_storage_qty->hec_dsq_additional_stor_qty } [GiB] |.
                  lv_data_changed = abap_true.

                  " Storage needs to be adjusted
                  LOOP AT lt_serv_to_storage_link REFERENCE INTO DATA(lr_serv_to_storage_link)
                    WHERE source_key = lt_perf_cat_to_serv_link[ source_key = lr_db_storage_qty->parent_key ]-target_key.

                    INSERT VALUE #( key = lr_serv_to_storage_link->target_key ) INTO TABLE lt_act_param_storage.

                  ENDLOOP.

                  " Set flag for deleting subnodes of standby/worker node
                  IF ( lr_db_storage_qty->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                       lr_db_storage_qty->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi   )   AND
                       lr_db_storage_qty->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                       lr_db_storage_qty->hec_db_node_default          = abap_true.
                    DATA(lv_delete_subnode) = abap_true.
                  ENDIF.
                ENDIF. " IF ls_db_storage_qty-hec_dsq_main_stor_qty_physical <> ls_db_storage_qty_old-hec_dsq_main_stor_qty_physical OR

                "-----------------------------------
                " Phase has changed - update phase
                " and inherit phase assignment
                "-----------------------------------
                IF lr_db_storage_qty->hec_phase_guid NE <fs_db_storage_qty_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_db_storage_qty->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                     lr_db_storage_qty->hec_db_node_default          = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_db_storage_qty->key
                                    hec_phase_guid_new = lr_db_storage_qty->hec_phase_guid
                                    hec_phase_guid_old = <fs_db_storage_qty_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_db_storage_qty->hec_phase_changed = abap_true.
                  lv_data_changed                      = abap_true.

                  " Set flag for deleting subnodes of standby/worker node
                  IF ( lr_db_storage_qty->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                       lr_db_storage_qty->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi   )   AND
                       lr_db_storage_qty->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                       lr_db_storage_qty->hec_db_node_default          = abap_true.
                    lv_delete_subnode = abap_true.
                  ENDIF.
                ENDIF. " IF lr_db_storage_qty->hec_phase_guid NE <fs_db_storage_qty_before>-hec_phase_guid.
              ENDIF. " IF <fs_db_storage_qty_before> IS ASSIGNED.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_db_storage_qty->hec_phase_guid IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_db_storage_qty->hec_instance_status.
                lr_db_storage_qty->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for delete
              " subnodes of DB standby/worker node
              " or relase standby/worker node
              "-----------------------------------
              IF ( lr_db_storage_qty->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                   lr_db_storage_qty->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi   )   AND
                   lr_db_storage_qty->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                   lr_db_storage_qty->hec_db_node_default          = abap_true                                               AND
                   lv_data_changed                                 = abap_true.

                " Only one master node per storage amount can exist
                io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                            it_key         = VALUE #( ( key = lr_db_storage_qty->key ) )
                                                            iv_fill_data   = abap_false
                                                            iv_association = /hec1/if_configuration_c=>sc_association-db_storage_amount-to_def_master_node
                                                  IMPORTING et_target_key  = lt_key ).

                IF NOT line_exists( lt_act_param_node[ key = lt_key[ 1 ]-key ] ).
                  TRY.
                      INSERT VALUE #( key               = lt_key[ 1 ]-key
                                      parent_key        = space
                                      do_release_node   = COND #( WHEN lr_db_storage_qty->hec_instance_status         = /hec1/if_config_constants=>gc_instance_status-complete   AND
                                                                       <fs_db_storage_qty_before>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                                  THEN abap_true
                                                                  ELSE abap_false                                                  )
                                      do_delete_subnode = COND #( WHEN lr_db_storage_qty->hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete OR
                                                                       lv_delete_subnode                      = abap_true
                                                                  THEN abap_true
                                                                  ELSE abap_false                                                                                     ) ) INTO TABLE lt_act_param_node.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                ENDIF.
              ENDIF. " IF ( lr_db_serv_perf_cat->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR...


              "-----------------------------------
              " Modify DB storage amount
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_storage_qty->key
                                   is_data = lr_db_storage_qty ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_delete_subnode,
                     lt_key.

              UNASSIGN <fs_db_storage_qty_before>.
            ENDLOOP.

            "-----------------------------------
            " Set update DB Storage action to
            " general
            "-----------------------------------
            IF lt_act_param_storage IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-db_storage )
                  it_key          = lt_act_param_storage
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_storage )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation ).                                                                                      .
            ENDIF.

            "-----------------------------------
            " Update Phasing
            "-----------------------------------
            IF lt_act_param_phasing IS NOT INITIAL.
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.


            "-----------------------------------
            " Set update DB node action to
            " general
            "-----------------------------------
            IF lt_act_param_node IS NOT INITIAL.
              CLEAR me->mr_act_param_db_node.
              me->mr_act_param_db_node = NEW /hec1/t_act_update_db_node( lt_act_param_node ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-db_node )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param_node
                                              ( key = wa_act_node-key )     )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_db_node                                                                                                       ).
            ENDIF.


            " ***************************************************************************
            " Update mode after DB server
            " performance category update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage_amount-update_after_serv_perf_cat.

            LOOP AT lt_db_storage_qty REFERENCE INTO lr_db_storage_qty.
              ASSIGN lt_db_serv_perf_cat[ key = lr_db_storage_qty->parent_key ] TO <fs_db_serv_perf_cat>.

              IF <fs_db_serv_perf_cat> IS ASSIGNED.
                "-----------------------------------
                " Release instance for selection
                "-----------------------------------
                IF <fs_db_serv_perf_cat>-hec_srv_perf_cat_guid IS NOT INITIAL AND
                   <fs_db_serv_perf_cat>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.

                IF lv_release <> lr_db_storage_qty->hec_row_selectable.
                  lr_db_storage_qty->hec_row_selectable = lv_release.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Update DB server cluster type
                "-----------------------------------
                IF lr_db_storage_qty->hec_db_cluster_type_value <> <fs_db_serv_perf_cat>-hec_db_cluster_type_value.
                  lr_db_storage_qty->hec_db_cluster_type_value = <fs_db_serv_perf_cat>-hec_db_cluster_type_value.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Modify DB storage amount
                "-----------------------------------
                IF lv_data_changed = abap_true.
                  io_modify->update( iv_node = is_ctx-node_key
                                     iv_key  = lr_db_storage_qty->key
                                     is_data = lr_db_storage_qty ).
                ENDIF.
              ENDIF. " IF <fs_db_serv_perf_cat> IS ASSIGNED.

              UNASSIGN <fs_db_serv_perf_cat>.
              CLEAR: lv_release,
                     lv_data_changed.

            ENDLOOP. " LOOP AT lt_db_storage_qty
        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD determine_db_storage_backup.

    DATA: lt_db_backup            TYPE /hec1/t_data_db_backup_ct,
          lt_db_backup_perstorage TYPE /hec1/t_data_db_backup_ct,
          lt_db_backup_before     TYPE /hec1/t_data_db_backup_ct,
          lt_db_storage           TYPE /hec1/t_data_db_storage_ct,
          lt_phase                TYPE /hec1/t_data_phase_ct,
          lt_act_param_succ       TYPE /hec1/t_act_set_success_predec,
          lt_act_param_phasing    TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_backup ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage_backup-create.

            " Get DB server storage (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_storage_backup-to_parent
                                              IMPORTING et_data        = lt_db_storage ).


            " Get for each DB storage the DB backup
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_storage
                                                        it_key         = VALUE #( FOR wa_node IN lt_db_storage
                                                                                 ( key = wa_node-key )         )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_storage-db_storage_backup
                                              IMPORTING et_data        = lt_db_backup_perstorage ).


            LOOP AT lt_db_backup REFERENCE INTO DATA(lr_db_backup).
              lr_db_backup->hec_delete_visible = abap_true.

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              lr_db_backup->hec_backup_class_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_backup(
                                                                              iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                              iv_tier_category_value = lr_db_backup->hec_tier_cat_value
                                                                              iv_srv_type_guid       = lr_db_backup->hec_db_srv_type_guid
                                                                              iv_is_app_backup       = abap_false ) )
                                                        THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                        ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_db_backup->hec_backup_class_guid IS NOT INITIAL AND
                                                                             lr_db_backup->hec_backup_size       IS NOT INITIAL AND
                                                                             lr_db_backup->hec_phase_guid        IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_db_backup->hec_instance_status.
                lr_db_backup->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.


              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_db_storage[ key = lr_db_backup->parent_key ] TO FIELD-SYMBOL(<fs_db_storage>).
              IF <fs_db_storage> IS ASSIGNED.
                IF <fs_db_storage>-hec_ip_storage_guid IS NOT INITIAL AND
                   <fs_db_storage>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_db_backup->hec_row_selectable.
                lr_db_backup->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for setting
              " DB server storage backup
              " successor/predecessor
              "-----------------------------------
              DATA(lv_node_count) = REDUCE i( INIT x = 0
                                              FOR <l> IN lt_db_backup_perstorage WHERE ( parent_key = lr_db_backup->parent_key )
                                              NEXT x = x + 1                                                                       ).

              IF NOT line_exists( lt_act_param_succ[ key = lr_db_backup->parent_key ] ) AND lv_node_count > 1.
                TRY.
                    INSERT VALUE #( key                  = lr_db_backup->parent_key
                                    parent_key           = lt_db_storage[ key = lr_db_backup->parent_key ]-parent_key
                                    hec_no_children_node = lv_node_count                                              ) INTO TABLE lt_act_param_succ.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.


              "-----------------------------------
              " Modify DB backup
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_backup->key
                                   is_data = lr_db_backup ).
              ENDIF.


              UNASSIGN <fs_db_storage>.
              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release,
                     lv_node_count.
            ENDLOOP.


            "-----------------------------------
            " Set successor/predecessor action
            " to GENERAL
            "-----------------------------------
            IF lt_act_param_succ IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_set_success_predec( lt_act_param_succ ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key  = /hec1/if_configuration_c=>sc_node-db_storage
                                             assoc_key = /hec1/if_configuration_c=>sc_association-db_storage-db_storage_backup )
                  it_key          = VALUE #( FOR wa_act_succ IN lt_act_param_succ
                                            ( key = wa_act_succ-key )    )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-set_success_predec )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage_backup-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                                         iv_fill_data    = abap_true
                               IMPORTING et_data         = lt_db_backup_before ).


            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get DB storage
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_storage_backup-to_parent
                                              IMPORTING et_target_key  = DATA(lt_db_storage_key)
                                                        et_data        = lt_db_storage ).


            LOOP AT lt_db_backup REFERENCE INTO lr_db_backup.
              ASSIGN lt_db_backup_before[ key = lr_db_backup->key ] TO FIELD-SYMBOL(<fs_db_backup_before>).

              IF <fs_db_backup_before> IS ASSIGNED.
                "-----------------------------------
                " Backup GUID has changed
                "-----------------------------------
                IF lr_db_backup->hec_backup_class_guid    IS NOT INITIAL                              AND
                  lr_db_backup->hec_backup_class_guid <> <fs_db_backup_before>-hec_backup_class_guid.

                  " Get backup class and backup class pricing
                  /hec1/cl_config_action_helper=>/hec1/if_bopf_action_helper~get_backup_class_and_price( EXPORTING is_ctx                  = CORRESPONDING #( is_ctx )
                                                                                                                   it_key                  = VALUE #( ( key = lr_db_backup->key ) )
                                                                                                                   iv_tier_category_value  = lr_db_backup->hec_tier_cat_value
                                                                                                                   iv_tier_datacenter_guid = lr_db_backup->hec_tier_datacenter_guid
                                                                                                                   iv_backup_class_guid    = lr_db_backup->hec_backup_class_guid
                                                                                                                   io_read                 = io_read
                                                                                                         IMPORTING es_backup_class         = DATA(ls_backup_class)
                                                                                                                   es_backup_pricing       = DATA(ls_backup_pricing) ).

                  lr_db_backup->price                      = CORRESPONDING #( ls_backup_pricing ).
                  lr_db_backup->hec_backup_class_guid      = ls_backup_class-hec_backup_class_guid.
                  lr_db_backup->hec_backup_class_descr     = ls_backup_class-hec_backup_class_descr.
                  lr_db_backup->hec_tree_descr             = ls_backup_class-hec_backup_class_descr. "#EC CI_FLDEXT_OK[2215424]
                  lr_db_backup->hec_backup_month_price_fee = lr_db_backup->hec_backup_size * lr_db_backup->hec_month_price_eur.

                  lv_data_changed                          = abap_true.

                  "-----------------------------------
                  " Set Value List Quantity
                  "-----------------------------------
                  lr_db_backup->hec_backup_class_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_backup(
                                                                                      iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                      iv_tier_category_value = lr_db_backup->hec_tier_cat_value
                                                                                      iv_srv_type_guid       = lr_db_backup->hec_db_srv_type_guid
                                                                                      iv_is_app_backup       = abap_false ) )
                                                                THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                ENDIF. " IF ls_db_backup-hec_backup_class_guid IS NOT INITIAL AND

                "-----------------------------------
                " Backup size has changed
                "-----------------------------------
                IF lr_db_backup->hec_backup_size IS NOT INITIAL AND
                   lr_db_backup->hec_backup_size <> <fs_db_backup_before>-hec_backup_size.
                  lr_db_backup->hec_backup_month_price_fee = lr_db_backup->hec_backup_size * lr_db_backup->hec_month_price_eur.
                  lv_data_changed = abap_true.

                ENDIF.

                "-----------------------------------
                " Phase has changed
                "-----------------------------------
                IF lr_db_backup->hec_phase_guid NE <fs_db_backup_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_db_backup->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                     lr_db_backup->hec_db_node_default          = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_db_backup->key
                                    hec_phase_guid_new = lr_db_backup->hec_phase_guid
                                    hec_phase_guid_old = <fs_db_backup_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_db_backup->hec_phase_changed = abap_true.
                  lv_data_changed                 = abap_true.

                ENDIF.
              ENDIF. "IF <fs_db_backup_before> IS ASSIGNED.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_db_backup->hec_backup_class_guid IS NOT INITIAL AND
                                                         lr_db_backup->hec_backup_size       IS NOT INITIAL AND
                                                         lr_db_backup->hec_phase_guid        IS NOT INITIAL
                                                    THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                    ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_db_backup->hec_instance_status.
                lr_db_backup->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify DB backup
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_backup->key
                                   is_data = lr_db_backup ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     ls_backup_class,
                     ls_backup_pricing.

              UNASSIGN <fs_db_backup_before>.
            ENDLOOP.

            "-----------------------------------
            " Update Phasing
            "-----------------------------------
            IF lt_act_param_phasing IS NOT INITIAL.
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.

            " ***************************************************************************
            " Update mode after storage update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage_backup-update_after_storage.

            " Get DB server storage (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_storage_backup-to_parent
                                              IMPORTING et_data        = lt_db_storage ).


            LOOP AT lt_db_backup REFERENCE INTO lr_db_backup.
              ASSIGN lt_db_storage[ key = lr_db_backup->parent_key ] TO <fs_db_storage>.

              IF <fs_db_storage> IS ASSIGNED.
                "-----------------------------------
                " Release instance for selection
                "-----------------------------------
                IF <fs_db_storage>-hec_ip_storage_guid IS NOT INITIAL AND
                   <fs_db_storage>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.

                IF lv_release <> lr_db_backup->hec_row_selectable.
                  lr_db_backup->hec_row_selectable = lv_release.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Update DB server cluster type
                "-----------------------------------
                IF lr_db_backup->hec_db_cluster_type_value <> <fs_db_storage>-hec_db_cluster_type_value.
                  lr_db_backup->hec_db_cluster_type_value = <fs_db_storage>-hec_db_cluster_type_value.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Modify DB storage backup
                "-----------------------------------
                IF lv_data_changed = abap_true.
                  io_modify->update( iv_node = is_ctx-node_key
                                     iv_key  = lr_db_backup->key
                                     is_data = lr_db_backup ).
                ENDIF.
              ENDIF. "  IF <fs_db_storage> IS ASSIGNED.

              UNASSIGN <fs_db_storage>.
              CLEAR: lv_release,
                     lv_data_changed.

            ENDLOOP.
        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD execute.

    CLEAR: eo_message,
           et_failed_key.

    DATA(ls_root) = /hec1/cl_config_helper=>get_root_node( iv_node_key = is_ctx-node_key
                                                           it_key      = it_key
                                                           io_read     = io_read
                                                           io_modify   = io_modify ).

    TRY.
        CASE is_ctx-det_key.
            " **********************************
            " Determine DB server instance node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server_instance-create            OR
               /hec1/if_configuration_c=>sc_determination-db_server_instance-update            OR
               /hec1/if_configuration_c=>sc_determination-db_server_instance-update_after_tier.

            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_db_server_instance( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                            it_key        = it_key                           " Key Table
                                                            io_read       = io_read                          " Interface to Reading Data
                                                            io_modify     = io_modify                        " Interface to Change Data
                                                  IMPORTING eo_message    = eo_message                       " Message Object
                                                            et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_db_server_instanc_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                              it_key        = it_key                           " Key Table
                                                              io_read       = io_read                          " Interface to Reading Data
                                                              io_modify     = io_modify                        " Interface to Change Data
                                                    IMPORTING eo_message    = eo_message                       " Message Object
                                                              et_failed_key = et_failed_key ).                 " Key Table
            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determine instance DB node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-instance_db-create                        OR
               /hec1/if_configuration_c=>sc_determination-instance_db-update                        OR
               /hec1/if_configuration_c=>sc_determination-instance_db-update_after_server_instance.

            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_db_instance( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                     it_key        = it_key                           " Key Table
                                                     io_read       = io_read                          " Interface to Reading Data
                                                     io_modify     = io_modify                        " Interface to Change Data
                                           IMPORTING eo_message    = eo_message                       " Message Object
                                                     et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_db_instance_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                        it_key        = it_key                           " Key Table
                                                        io_read       = io_read                          " Interface to Reading Data
                                                        io_modify     = io_modify                        " Interface to Change Data
                                              IMPORTING eo_message    = eo_message                       " Message Object
                                                        et_failed_key = et_failed_key ).                 " Key Table
            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determine DB node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_node-create                   OR
               /hec1/if_configuration_c=>sc_determination-db_node-update                   OR
               /hec1/if_configuration_c=>sc_determination-db_node-update_after_instance_db.

            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_db_node( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                 it_key        = it_key                           " Key Table
                                                 io_read       = io_read                          " Interface to Reading Data
                                                 io_modify     = io_modify                        " Interface to Change Data
                                       IMPORTING eo_message    = eo_message                       " Message Object
                                                 et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_db_node_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                    it_key        = it_key                           " Key Table
                                                    io_read       = io_read                          " Interface to Reading Data
                                                    io_modify     = io_modify                        " Interface to Change Data
                                          IMPORTING eo_message    = eo_message                       " Message Object
                                                    et_failed_key = et_failed_key ).                 " Key Table
            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determine DB server performance
            " category node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server_perform_cat-create            OR
               /hec1/if_configuration_c=>sc_determination-db_server_perform_cat-update            OR
               /hec1/if_configuration_c=>sc_determination-db_server_perform_cat-update_after_node.

            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_db_server_perf_cat( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                            it_key        = it_key                           " Key Table
                                                            io_read       = io_read                          " Interface to Reading Data
                                                            io_modify     = io_modify                        " Interface to Change Data
                                                  IMPORTING eo_message    = eo_message                       " Message Object
                                                            et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_db_server_pc_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                         it_key        = it_key                           " Key Table
                                                         io_read       = io_read                          " Interface to Reading Data
                                                         io_modify     = io_modify                        " Interface to Change Data
                                               IMPORTING eo_message    = eo_message                       " Message Object
                                                         et_failed_key = et_failed_key ).                 " Key Table
            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determine DB storage amount
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage_amount-create                     OR
               /hec1/if_configuration_c=>sc_determination-db_storage_amount-update                     OR
               /hec1/if_configuration_c=>sc_determination-db_storage_amount-update_after_serv_perf_cat.

            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_db_storage_amount( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                           it_key        = it_key                           " Key Table
                                                           io_read       = io_read                          " Interface to Reading Data
                                                           io_modify     = io_modify                        " Interface to Change Data
                                                 IMPORTING eo_message    = eo_message                       " Message Object
                                                           et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_db_storage_amount_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                              it_key        = it_key                           " Key Table
                                                              io_read       = io_read                          " Interface to Reading Data
                                                              io_modify     = io_modify                        " Interface to Change Data
                                                    IMPORTING eo_message    = eo_message                       " Message Object
                                                              et_failed_key = et_failed_key ).                 " Key Table
            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determine DB server
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server-create                      OR
               /hec1/if_configuration_c=>sc_determination-db_server-update                      OR
               /hec1/if_configuration_c=>sc_determination-db_server-update_after_serv_perf_cat.

            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_db_server( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                   it_key        = it_key                           " Key Table
                                                   io_read       = io_read                          " Interface to Reading Data
                                                   io_modify     = io_modify                        " Interface to Change Data
                                         IMPORTING eo_message    = eo_message                       " Message Object
                                                   et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_db_server_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                      it_key        = it_key                           " Key Table
                                                      io_read       = io_read                          " Interface to Reading Data
                                                      io_modify     = io_modify                        " Interface to Change Data
                                            IMPORTING eo_message    = eo_message                       " Message Object
                                                      et_failed_key = et_failed_key ).                 " Key Table
            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determine DB storage
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage-create              OR
               /hec1/if_configuration_c=>sc_determination-db_storage-update              OR
               /hec1/if_configuration_c=>sc_determination-db_storage-update_after_server.

            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_db_storage( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                    it_key        = it_key                           " Key Table
                                                    io_read       = io_read                          " Interface to Reading Data
                                                    io_modify     = io_modify                        " Interface to Change Data
                                          IMPORTING eo_message    = eo_message                       " Message Object
                                                    et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_db_storage_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                       it_key        = it_key                           " Key Table
                                                       io_read       = io_read                          " Interface to Reading Data
                                                       io_modify     = io_modify                        " Interface to Change Data
                                             IMPORTING eo_message    = eo_message                       " Message Object
                                                       et_failed_key = et_failed_key ).                 " Key Table
            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determine DB storage backup
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage_backup-create               OR
               /hec1/if_configuration_c=>sc_determination-db_storage_backup-update               OR
               /hec1/if_configuration_c=>sc_determination-db_storage_backup-update_after_storage.

            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_db_storage_backup( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                           it_key        = it_key                           " Key Table
                                                           io_read       = io_read                          " Interface to Reading Data
                                                           io_modify     = io_modify                        " Interface to Change Data
                                                 IMPORTING eo_message    = eo_message                       " Message Object
                                                           et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_db_storage_backup_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                              it_key        = it_key                           " Key Table
                                                              io_read       = io_read                          " Interface to Reading Data
                                                              io_modify     = io_modify                        " Interface to Change Data
                                                    IMPORTING eo_message    = eo_message                       " Message Object
                                                              et_failed_key = et_failed_key ).                 " Key Table
            ENDCASE. "ls_root-hec_contract_status.

        ENDCASE.
      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD execute_tree.
    " **************************************************************************************************************************************************
    " Attention!!!!!!
    " This is only a temporary solution, because this is
    " a mix between UI logic and BOPF logic. Normally no
    " UI logic has to be set into a BOPF object. But at
    " the moment there is the problem, that the Application
    " is not running with FBI, therefore we can't control
    " the tree about the FBI feeder class
    " **************************************************************************************************************************************************

    DATA lr_data TYPE REF TO data.
    FIELD-SYMBOLS <lt_data> TYPE ANY TABLE.

    /bobf/cl_frw_factory=>get_configuration( is_ctx-bo_key )->get_node( EXPORTING iv_node_key = is_ctx-node_key IMPORTING es_node = DATA(ls_node) ).

    DATA(lo_tabledescr) = CAST cl_abap_tabledescr( cl_abap_tabledescr=>describe_by_name( ls_node-data_table_type ) ).

    CREATE DATA lr_data TYPE HANDLE lo_tabledescr.

    ASSIGN lr_data->* TO <lt_data>.
    IF sy-subrc = 0.
      io_read->retrieve(
        EXPORTING
          iv_node = is_ctx-node_key
          it_key  = it_key
        IMPORTING
          et_data = <lt_data> ).

    ENDIF.

    IF <lt_data> IS NOT ASSIGNED OR <lt_data> IS INITIAL.
      RETURN.
    ENDIF.

    CASE is_ctx-det_key.
        " **********************************
        " Determine DB server instance node
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_determination-db_server_instance-create.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_db_server_instance IN CORRESPONDING /hec1/t_data_db_server_inst_ct( <lt_data> )
                                                                                                             ( VALUE #( parent_node_key     = wa_db_server_instance-parent_key
                                                                                                                        node_key            = wa_db_server_instance-key
                                                                                                                        hec_instance_status = wa_db_server_instance-hec_instance_status
                                                                                                                        hec_tree_descr      = wa_db_server_instance-hec_tree_descr
                                                                                                                        hec_row_selectable  = wa_db_server_instance-hec_row_selectable
                                                                                                                        hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-db_serv_inst
                                                                                                                        hec_phase_guid      = wa_db_server_instance-hec_phase_guid
                                                                                                                        crea_date_time      = wa_db_server_instance-crea_date_time
                                                                                                                        hec_delete_visible  = wa_db_server_instance-hec_delete_visible
                                                                                                                        change_request      = wa_db_server_instance-change_request ) ) ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-db_server_instance-update            OR
           /hec1/if_configuration_c=>sc_determination-db_server_instance-update_after_tier.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_db_server_instance IN CORRESPONDING /hec1/t_data_db_server_inst_ct( <lt_data> )
                                                                                                             ( VALUE #( parent_node_key     = wa_db_server_instance-parent_key
                                                                                                                        node_key            = wa_db_server_instance-key
                                                                                                                        hec_instance_status = wa_db_server_instance-hec_instance_status
                                                                                                                        hec_tree_descr      = wa_db_server_instance-hec_tree_descr
                                                                                                                        hec_row_selectable  = wa_db_server_instance-hec_row_selectable
                                                                                                                        hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-db_serv_inst
                                                                                                                        hec_phase_guid      = wa_db_server_instance-hec_phase_guid
                                                                                                                        crea_date_time      = wa_db_server_instance-crea_date_time
                                                                                                                        hec_delete_visible  = wa_db_server_instance-hec_delete_visible
                                                                                                                        change_request      = wa_db_server_instance-change_request ) ) ) ).


      WHEN /hec1/if_configuration_c=>sc_determination-instance_db-create.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_db_inst IN CORRESPONDING /hec1/t_data_db_inst_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_db_inst-parent_key
                                                                                                                    node_key            = wa_db_inst-key
                                                                                                                    hec_instance_status = wa_db_inst-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_db_inst-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_db_inst-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-db_inst
                                                                                                                    hec_phase_guid      = wa_db_inst-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_db_inst-hec_delete_visible
                                                                                                                    crea_date_time      = wa_db_inst-crea_date_time
                                                                                                                    hec_sort_order      = SWITCH #( wa_db_inst-hec_db_node_type_value
                                                                                                                                                    WHEN /hec1/if_config_constants=>gc_db_node_type-container THEN 1
                                                                                                                                                    WHEN /hec1/if_config_constants=>gc_db_node_type-single    THEN 2
                                                                                                                                                    WHEN /hec1/if_config_constants=>gc_db_node_type-tenant    THEN 3 )
                                                                                                                    change_request      = wa_db_inst-change_request ) ) ) ).
      WHEN /hec1/if_configuration_c=>sc_determination-instance_db-update                        OR
        /hec1/if_configuration_c=>sc_determination-instance_db-update_after_server_instance.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_db_inst IN CORRESPONDING /hec1/t_data_db_inst_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_db_inst-parent_key
                                                                                                                    node_key            = wa_db_inst-key
                                                                                                                    hec_instance_status = wa_db_inst-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_db_inst-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_db_inst-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-db_inst
                                                                                                                    hec_phase_guid      = wa_db_inst-hec_phase_guid
                                                                                                                    crea_date_time      = wa_db_inst-crea_date_time
                                                                                                                    hec_delete_visible  = wa_db_inst-hec_delete_visible
                                                                                                                    hec_sort_order      = SWITCH #( wa_db_inst-hec_db_node_type_value
                                                                                                                                                    WHEN /hec1/if_config_constants=>gc_db_node_type-container THEN 1
                                                                                                                                                    WHEN /hec1/if_config_constants=>gc_db_node_type-single    THEN 2
                                                                                                                                                    WHEN /hec1/if_config_constants=>gc_db_node_type-tenant    THEN 3 )
                                                                                                                    change_request      = wa_db_inst-change_request ) ) ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-db_node-create.


        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_db_node IN CORRESPONDING /hec1/t_data_db_node_ct( <lt_data> )
                                                                                                 ( VALUE #( parent_node_key     = wa_db_node-parent_key
                                                                                                            node_key            = wa_db_node-key
                                                                                                            hec_instance_status = wa_db_node-hec_instance_status
                                                                                                            hec_tree_descr      = wa_db_node-hec_tree_descr
                                                                                                            hec_row_selectable  = wa_db_node-hec_row_selectable
                                                                                                            hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-db_node
                                                                                                            hec_phase_guid      = wa_db_node-hec_phase_guid
                                                                                                            hec_delete_visible  = wa_db_node-hec_delete_visible
                                                                                                            crea_date_time      = wa_db_node-crea_date_time
                                                                                                            hec_sort_order      = SWITCH #( wa_db_node-hec_db_node_type_value
                                                                                                                                            WHEN /hec1/if_config_constants=>gc_db_clust_node_type-master  THEN 1
                                                                                                                                            WHEN /hec1/if_config_constants=>gc_db_clust_node_type-standby THEN 2
                                                                                                                                            WHEN /hec1/if_config_constants=>gc_db_clust_node_type-worker  THEN 3 )
                                                                                                            change_request      = wa_db_node-change_request ) ) ) ).


      WHEN /hec1/if_configuration_c=>sc_determination-db_node-update                   OR
           /hec1/if_configuration_c=>sc_determination-db_node-update_after_instance_db.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_db_node IN CORRESPONDING /hec1/t_data_db_node_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_db_node-parent_key
                                                                                                                    node_key            = wa_db_node-key
                                                                                                                    hec_instance_status = wa_db_node-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_db_node-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_db_node-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-db_node
                                                                                                                    hec_phase_guid      = wa_db_node-hec_phase_guid
                                                                                                                    crea_date_time      = wa_db_node-crea_date_time
                                                                                                                    hec_delete_visible  = wa_db_node-hec_delete_visible
                                                                                                                    hec_sort_order      = SWITCH #( wa_db_node-hec_db_node_type_value
                                                                                                                                                    WHEN /hec1/if_config_constants=>gc_db_clust_node_type-master  THEN 1
                                                                                                                                                    WHEN /hec1/if_config_constants=>gc_db_clust_node_type-standby THEN 2
                                                                                                                                                    WHEN /hec1/if_config_constants=>gc_db_clust_node_type-worker  THEN 3 )
                                                                                                                    change_request      = wa_db_node-change_request ) ) ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-db_server_perform_cat-create.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_db_serv_pc IN CORRESPONDING /hec1/t_data_db_serv_pc_ct( <lt_data> )
                                                                                                 ( VALUE #( parent_node_key     = wa_db_serv_pc-parent_key
                                                                                                            node_key            = wa_db_serv_pc-key
                                                                                                            hec_instance_status = wa_db_serv_pc-hec_instance_status
                                                                                                            hec_tree_descr      = wa_db_serv_pc-hec_tree_descr
                                                                                                            hec_row_selectable  = wa_db_serv_pc-hec_row_selectable
                                                                                                            hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-db_serv_pc
                                                                                                            hec_phase_guid      = wa_db_serv_pc-hec_phase_guid
                                                                                                            hec_delete_visible  = wa_db_serv_pc-hec_delete_visible
                                                                                                            crea_date_time      = wa_db_serv_pc-crea_date_time
                                                                                                            hec_successor_guid  = wa_db_serv_pc-hec_successor_guid
                                                                                                            change_request      = wa_db_serv_pc-change_request ) ) ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-db_server_perform_cat-update            OR
           /hec1/if_configuration_c=>sc_determination-db_server_perform_cat-update_after_node.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_db_serv_pc IN CORRESPONDING /hec1/t_data_db_serv_pc_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_db_serv_pc-parent_key
                                                                                                                    node_key            = wa_db_serv_pc-key
                                                                                                                    hec_instance_status = wa_db_serv_pc-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_db_serv_pc-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_db_serv_pc-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-db_serv_pc
                                                                                                                    hec_phase_guid      = wa_db_serv_pc-hec_phase_guid
                                                                                                                    crea_date_time      = wa_db_serv_pc-crea_date_time
                                                                                                                    hec_delete_visible  = wa_db_serv_pc-hec_delete_visible
                                                                                                                    hec_successor_guid  = wa_db_serv_pc-hec_successor_guid
                                                                                                                    change_request      = wa_db_serv_pc-change_request ) ) ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-db_storage_amount-create.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_db_storage_qty IN CORRESPONDING /hec1/t_data_db_storage_qty_ct( <lt_data> )
                                                                                                 ( VALUE #( parent_node_key     = wa_db_storage_qty-parent_key
                                                                                                            node_key            = wa_db_storage_qty-key
                                                                                                            hec_instance_status = wa_db_storage_qty-hec_instance_status
                                                                                                            hec_tree_descr      = wa_db_storage_qty-hec_tree_descr
                                                                                                            hec_row_selectable  = wa_db_storage_qty-hec_row_selectable
                                                                                                            hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-db_storage_qty
                                                                                                            hec_phase_guid      = wa_db_storage_qty-hec_phase_guid
                                                                                                            hec_delete_visible  = wa_db_storage_qty-hec_delete_visible
                                                                                                            crea_date_time      = wa_db_storage_qty-crea_date_time
                                                                                                            hec_successor_guid  = wa_db_storage_qty-hec_successor_guid
                                                                                                            change_request      = wa_db_storage_qty-change_request ) ) ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-db_storage_amount-update                     OR
           /hec1/if_configuration_c=>sc_determination-db_storage_amount-update_after_serv_perf_cat.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_db_storage_qty IN CORRESPONDING /hec1/t_data_db_storage_qty_ct( <lt_data> )
                                                                                                 ( VALUE #( parent_node_key     = wa_db_storage_qty-parent_key
                                                                                                            node_key            = wa_db_storage_qty-key
                                                                                                            hec_instance_status = wa_db_storage_qty-hec_instance_status
                                                                                                            hec_tree_descr      = wa_db_storage_qty-hec_tree_descr
                                                                                                            hec_row_selectable  = wa_db_storage_qty-hec_row_selectable
                                                                                                            hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-db_storage_qty
                                                                                                            hec_phase_guid      = wa_db_storage_qty-hec_phase_guid
                                                                                                            crea_date_time      = wa_db_storage_qty-crea_date_time
                                                                                                            hec_delete_visible  = wa_db_storage_qty-hec_delete_visible
                                                                                                            hec_successor_guid  = wa_db_storage_qty-hec_successor_guid
                                                                                                            change_request      = wa_db_storage_qty-change_request ) ) ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-db_server-create.


        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_db_server IN CORRESPONDING /hec1/t_data_db_serv_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_db_server-parent_key
                                                                                                                    node_key            = wa_db_server-key
                                                                                                                    hec_instance_status = wa_db_server-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_db_server-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_db_server-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-db_server
                                                                                                                    hec_phase_guid      = wa_db_server-hec_phase_guid
                                                                                                                    crea_date_time      = wa_db_server-crea_date_time
                                                                                                                    hec_delete_visible  = wa_db_server-hec_delete_visible
                                                                                                                    change_request      = wa_db_server-change_request ) ) ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-db_server-update                      OR
           /hec1/if_configuration_c=>sc_determination-db_server-update_after_serv_perf_cat.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_db_server IN CORRESPONDING /hec1/t_data_db_serv_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_db_server-parent_key
                                                                                                                    node_key            = wa_db_server-key
                                                                                                                    hec_instance_status = wa_db_server-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_db_server-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_db_server-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-db_server
                                                                                                                    hec_phase_guid      = wa_db_server-hec_phase_guid
                                                                                                                    crea_date_time      = wa_db_server-crea_date_time
                                                                                                                    hec_delete_visible  = wa_db_server-hec_delete_visible
                                                                                                                    change_request      = wa_db_server-change_request ) ) ) ).


      WHEN /hec1/if_configuration_c=>sc_determination-db_storage-create.
        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_db_storage IN CORRESPONDING /hec1/t_data_db_storage_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_db_storage-parent_key
                                                                                                                    node_key            = wa_db_storage-key
                                                                                                                    hec_instance_status = wa_db_storage-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_db_storage-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_db_storage-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-db_storage
                                                                                                                    hec_phase_guid      = wa_db_storage-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_db_storage-hec_delete_visible
                                                                                                                    crea_date_time      = wa_db_storage-crea_date_time
                                                                                                                    hec_successor_guid  = wa_db_storage-hec_successor_guid
                                                                                                                    change_request      = wa_db_storage-change_request ) ) ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-db_storage-update              OR
           /hec1/if_configuration_c=>sc_determination-db_storage-update_after_server.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_db_storage IN CORRESPONDING /hec1/t_data_db_storage_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_db_storage-parent_key
                                                                                                                    node_key            = wa_db_storage-key
                                                                                                                    hec_instance_status = wa_db_storage-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_db_storage-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_db_storage-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-db_storage
                                                                                                                    hec_phase_guid      = wa_db_storage-hec_phase_guid
                                                                                                                    crea_date_time      = wa_db_storage-crea_date_time
                                                                                                                    hec_delete_visible  = wa_db_storage-hec_delete_visible
                                                                                                                    hec_successor_guid  = wa_db_storage-hec_successor_guid
                                                                                                                    change_request      = wa_db_storage-change_request ) ) ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-db_storage_backup-create.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_db_backup IN CORRESPONDING /hec1/t_data_db_backup_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_db_backup-parent_key
                                                                                                                    node_key            = wa_db_backup-key
                                                                                                                    hec_instance_status = wa_db_backup-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_db_backup-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_db_backup-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-db_backup
                                                                                                                    hec_phase_guid      = wa_db_backup-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_db_backup-hec_delete_visible
                                                                                                                    crea_date_time      = wa_db_backup-crea_date_time
                                                                                                                    hec_successor_guid  = wa_db_backup-hec_successor_guid
                                                                                                                    change_request      = wa_db_backup-change_request ) ) ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-db_storage_backup-update               OR
           /hec1/if_configuration_c=>sc_determination-db_storage_backup-update_after_storage.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_db_backup IN CORRESPONDING /hec1/t_data_db_backup_ct( <lt_data> )
                                                                                                 ( VALUE #( parent_node_key     = wa_db_backup-parent_key
                                                                                                            node_key            = wa_db_backup-key
                                                                                                            hec_instance_status = wa_db_backup-hec_instance_status
                                                                                                            hec_tree_descr      = wa_db_backup-hec_tree_descr
                                                                                                            hec_row_selectable  = wa_db_backup-hec_row_selectable
                                                                                                            hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-db_backup
                                                                                                            hec_phase_guid      = wa_db_backup-hec_phase_guid
                                                                                                            hec_delete_visible  = wa_db_backup-hec_delete_visible
                                                                                                            hec_successor_guid  = wa_db_backup-hec_successor_guid
                                                                                                            change_request      = wa_db_backup-change_request ) ) ) ).

    ENDCASE.


  ENDMETHOD.


  METHOD determine_db_instance_cr.

    DATA: lt_db_serv_inst       TYPE /hec1/t_data_db_server_inst_ct,
          lt_db_serv_inst_all   TYPE /hec1/t_data_db_server_inst_ct,
          lt_instance_db        TYPE /hec1/t_data_db_inst_ct,
          lt_instance_db_all    TYPE /hec1/t_data_db_inst_ct,
          lt_inst_db_before     TYPE /hec1/t_data_db_inst_ct,
          lt_tier               TYPE /hec1/t_data_tier_ct,
          lt_tier_all           TYPE /hec1/t_data_tier_ct,
          lt_act_param          TYPE /hec1/t_act_create_db_node,
          lt_act_param_instance TYPE /hec1/t_act_update_instance_db,
          lt_phase              TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing  TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    " Data before update
    io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                 it_key          = it_key
                                 iv_before_image = abap_true
                       IMPORTING et_data         = lt_inst_db_before ).

    " Data after update
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_instance_db ).


    " Get DB server instance
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-to_parent
                                      IMPORTING et_data        = lt_db_serv_inst
                                                et_target_key  = DATA(lt_db_serv_inst_key) ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-instance_db-create.

            " Get Tier
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                        it_key         = lt_db_serv_inst_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-to_parent
                                              IMPORTING et_data        = lt_tier
                                                        et_target_key  = DATA(lt_tier_key) ).

            " Get all tiers for multitenancy
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_false
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-solution
                                              IMPORTING et_target_key  = DATA(lt_solution_all_key) ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-solution
                                                        it_key         = lt_solution_all_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                              IMPORTING et_data        = lt_tier_all
                                                        et_target_key  = DATA(lt_tier_all_key) ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                        it_key         = lt_tier_all_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier-db_server_instance
                                              IMPORTING et_data        = lt_db_serv_inst_all
                                                        et_target_key  = DATA(lt_db_serv_inst_all_key) ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                        it_key         = lt_db_serv_inst_all_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-instance_db
                                              IMPORTING et_data        = lt_instance_db_all ).



            LOOP AT lt_instance_db REFERENCE INTO DATA(lr_instance_db).
              lr_instance_db->hec_delete_visible = abap_false.

              "-----------------------------------
              " Set Multitenancy Relation ID
              "   to tenant
              " The corresponding tier is in:
              "   DB_SERVER_INSTANCE-HEC_DB_TIER_GUID
              "-----------------------------------
              " if tenant is created: check for existing container
              IF lr_instance_db->hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-tenant       "Tenant
                OR lr_instance_db->hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-container. "Container

                DATA(ls_db_serv_inst) = VALUE #( lt_db_serv_inst[ key = lr_instance_db->parent_key ] OPTIONAL ).
                DATA(ls_tier) = VALUE #( lt_tier[ key = ls_db_serv_inst-parent_key ] OPTIONAL ).

                CASE lr_instance_db->hec_db_node_type_value.
                  WHEN /hec1/if_config_constants=>gc_db_node_type-tenant. "Tenant

                    IF ls_db_serv_inst-hec_db_tier_guid IS NOT INITIAL.

                      " 1. get related tier
                      " This loop should only run once. We need the loop to exclude the own tier.
                      LOOP AT lt_tier_all ASSIGNING FIELD-SYMBOL(<fs_tier_related>)
                        WHERE hec_node_tier = ls_db_serv_inst-hec_db_tier_guid
                          AND hec_node_tier <> ls_db_serv_inst-hec_node_tier.

                        " 2. get instance db for referenced tier
                        LOOP AT lt_db_serv_inst_all ASSIGNING FIELD-SYMBOL(<fs_db_serv_inst_related>)
                          WHERE parent_key              = <fs_tier_related>-key
                            AND hec_db_impl_type_value  = /hec1/if_config_constants=>gc_db_impl_type-multitenancy
                            AND hec_db_allocation_value = /hec1/if_config_constants=>gc_db_allocation-internal.

                          DATA(ls_instance_db_related) = VALUE #( lt_instance_db_all[ parent_key = <fs_db_serv_inst_related>-key
                                                                                      hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-container ] OPTIONAL ). "Container

                          lr_instance_db->hec_multi_tenant_rel_guid = ls_instance_db_related-hec_multi_tenant_rel_guid.

                          DATA(lv_data_changed) = abap_true.
                        ENDLOOP. "lt_db_serv_inst_all

                      ENDLOOP. " lt_tier_all

                    ENDIF. " IF ls_db_serv_inst-hec_db_tier_guid IS NOT INITIAL.

                    " if container is created and the tenants already exist, set update of tenant to general
                    "   each of these tenants will have the DB Tier in the DB Server Instance
                  WHEN /hec1/if_config_constants=>gc_db_node_type-container. "Container

                    IF ls_db_serv_inst-hec_db_impl_type_value = /hec1/if_config_constants=>gc_db_impl_type-multitenancy     AND
                       ls_db_serv_inst-hec_db_allocation_value = /hec1/if_config_constants=>gc_db_allocation-internal.

                      " 2. check if tenant instance for related stack exists
                      LOOP AT lt_db_serv_inst_all ASSIGNING FIELD-SYMBOL(<fs_db_serv_inst_all>)
                        WHERE hec_db_tier_guid = ls_db_serv_inst-hec_node_tier.

                        LOOP AT lt_instance_db_all INTO DATA(ls_db_instance_db_all)
                          WHERE parent_key = <fs_db_serv_inst_all>-key
                            AND hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-tenant. "Tenant

                          " 3. Add action to update tenant to general
                          INSERT VALUE #( key                          = ls_db_instance_db_all-key
                                          parent_key                   = ls_db_instance_db_all-parent_key
                                          hec_multi_tenant_rel_guid    = lr_instance_db->hec_multi_tenant_rel_guid
                                          do_update_multi_tenancy_guid = abap_true
                                          ) INTO TABLE lt_act_param_instance.

                        ENDLOOP. "lt_instance_db_all

                      ENDLOOP. "lt_db_serv_inst_all
                    ENDIF.
                    " IF ls_db_serv_inst-hec_db_impl_type_value = /hec1/if_config_constants=>gc_db_impl_type-multitenancy
                    " AND ls_db_serv_inst-hec_db_allocation_value = /hec1/if_config_constants=>gc_db_allocation-internal.

                ENDCASE.

              ENDIF. "lr_instance_db->hec_db_node_type = '02' OR '03'

              "-----------------------------------
              " Set Value List Quantity - Cluster Type
              "-----------------------------------
              lr_instance_db->hec_dbst_nodety_clust_ty_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_cluster_type(
                                                                                        iv_apm_guid                   = lr_landscape->hec_apm_guid
                                                                                        iv_sol_tier_dsi_dbstype_guid  = lr_instance_db->hec_sol_tier_dsi_dbstype_guid
                                                                                        iv_sol_dbst_alloc_nodety_guid = lr_instance_db->hec_sol_dbst_alloc_nodety_guid ) )
                                                                        THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                        ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_db_serv_inst[ key = lr_instance_db->parent_key ] TO FIELD-SYMBOL(<fs_db_serv_inst>).

              IF <fs_db_serv_inst>-hec_sol_tier_stack_si_guid     IS NOT INITIAL AND
                 <fs_db_serv_inst>-hec_sol_tier_dsi_dbstype_guid  IS NOT INITIAL AND
                 <fs_db_serv_inst>-hec_sol_dbst_oper_sys_guid     IS NOT INITIAL AND
                 <fs_db_serv_inst>-hec_sol_dbst_impltype_guid     IS NOT INITIAL AND
                 <fs_db_serv_inst>-hec_sol_dbst_impty_instty_guid IS NOT INITIAL AND
                 <fs_db_serv_inst>-hec_sol_dbst_imty_inty_al_guid IS NOT INITIAL AND
                 <fs_db_serv_inst>-hec_row_selectable = abap_true.
                DATA(lv_release) = abap_true.
              ENDIF.

              IF lv_release <> lr_instance_db->hec_row_selectable.
                lr_instance_db->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_instance_db->hec_dbst_nodety_clust_ty_guid IS NOT INITIAL AND
                                                                             lr_instance_db->hec_phase_guid                IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete    ).

              IF lv_inst_status <> lr_instance_db->hec_instance_status.
                lr_instance_db->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "------------------------------------------
              " Set CR related fields from the ROOT node
              "------------------------------------------
              DATA(lv_cr_data_changed) = /hec1/cl_config_helper=>SET_CR_RELATED_FIELDS(
                EXPORTING
                  is_ctx       = is_ctx
                  it_key       = it_key
                  io_read      = io_read
                  io_modify    = io_modify
                  iv_mod_type  = /hec1/if_config_constants=>gc_comp_mod_type-added
                  is_node_data = lr_instance_db
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              IF lv_data_changed = abap_false.
                lv_data_changed = lv_cr_data_changed.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " instance DB action
              "-----------------------------------
              INSERT VALUE #( key                = lr_instance_db->key
                              parent_key         = lr_instance_db->parent_key
                              hec_cluster_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master
                              hec_def_master_node         = abap_true
                              hec_db_node_qty             = 1                                                       ) INTO TABLE lt_act_param.

              "-----------------------------------
              " Modify instance DB
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_instance_db->key
                                   is_data = lr_instance_db ).
              ENDIF.

              CLEAR: lv_release,
                     lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_db_serv_inst>.
            ENDLOOP.

            "-----------------------------------
            " Set create DB node action
            " to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_db_node( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_node )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                ).

            ENDIF.

            "-----------------------------------
            " Set Update Instance DB action
            " to general
            "-----------------------------------
            IF lt_act_param_instance IS NOT INITIAL.
              CLEAR me->mr_act_param_instance.
              me->mr_act_param_instance = NEW /hec1/t_act_update_instance_db( lt_act_param_instance ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_instance_db )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_instance                                                                                                                ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-instance_db-update.

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).


            LOOP AT lt_instance_db REFERENCE INTO lr_instance_db.

              ASSIGN lt_inst_db_before[ key = lr_instance_db->key ] TO FIELD-SYMBOL(<fs_inst_db_before>).
              IF <fs_inst_db_before> IS ASSIGNED.
                lr_instance_db->hec_delete_visible = abap_false.

                "-----------------------------------
                " Set Value List Quantity - Cluster Type
                "-----------------------------------
                IF lr_instance_db->hec_dbst_nodety_clust_ty_guid <> <fs_inst_db_before>-hec_dbst_nodety_clust_ty_guid.
                  lr_instance_db->hec_dbst_nodety_clust_ty_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_cluster_type(
                                                                                            iv_apm_guid                   = lr_landscape->hec_apm_guid
                                                                                            iv_sol_tier_dsi_dbstype_guid  = lr_instance_db->hec_sol_tier_dsi_dbstype_guid
                                                                                            iv_sol_dbst_alloc_nodety_guid = lr_instance_db->hec_sol_dbst_alloc_nodety_guid ) )
                                                                            THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                            ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                  lv_data_changed = abap_true.

                ENDIF. "cluster type has changed

                "-----------------------------------
                " Master, standby or
                " worker node is added
                "-----------------------------------
                IF lr_instance_db->hec_dbst_nodety_clust_ty_guid = <fs_inst_db_before>-hec_dbst_nodety_clust_ty_guid AND
                  ( lr_instance_db->hec_db_master_node_qty  <> <fs_inst_db_before>-hec_db_master_node_qty  OR
                    lr_instance_db->hec_db_standby_node_qty <> <fs_inst_db_before>-hec_db_standby_node_qty OR
                    lr_instance_db->hec_db_worker_node_qty  <> <fs_inst_db_before>-hec_db_worker_node_qty     ).
                  "-----------------------------------
                  " Non default master node
                  "-----------------------------------
                  IF lr_instance_db->hec_db_master_node_qty > <fs_inst_db_before>-hec_db_master_node_qty.
                    " Add non default master node to action table
                    INSERT VALUE #( key                         = lr_instance_db->key
                                    parent_key                  = lr_instance_db->parent_key
                                    hec_cluster_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master
                                    hec_def_master_node         = abap_false
                                    hec_db_node_qty             = lr_instance_db->hec_db_master_node_qty - <fs_inst_db_before>-hec_db_master_node_qty ) INTO TABLE lt_act_param.

                    " Success message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_master_node_added
                                                                   iv_severity = /bobf/cm_frw=>co_severity_success
                                                                   iv_attr1    = CONV #( lr_instance_db->hec_db_master_node_qty -
                                                                                 <fs_inst_db_before>-hec_db_master_node_qty )
                                                         CHANGING  co_message  = eo_message ).

                  ELSEIF lr_instance_db->hec_db_master_node_qty < <fs_inst_db_before>-hec_db_master_node_qty.
                    DATA(lv_attr_name) = /hec1/if_configuration_c=>sc_node_attribute-instance_db-hec_db_master_node_qty.

                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_instance_db->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_instance_db->hec_db_master_node_qty = <fs_inst_db_before>-hec_db_master_node_qty.
                    lv_data_changed = abap_true.

                  ELSEIF lr_instance_db->hec_db_master_node_limit_qty < lr_instance_db->hec_db_master_node_limit_qty.
                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>node_limit_is_exceeded
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_instance_db->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_instance_db->hec_db_master_node_qty = <fs_inst_db_before>-hec_db_master_node_qty.
                    lv_data_changed = abap_true.
                  ENDIF. " IF lr_instance_db->hec_db_master_node_qty > <fs_inst_db_before>-hec_db_master_node_qty.


                  "-----------------------------------
                  " Standby node
                  "-----------------------------------
                  IF lr_instance_db->hec_db_standby_node_qty > <fs_inst_db_before>-hec_db_standby_node_qty.
                    " Add non default master node to action table
                    INSERT VALUE #( key                         = lr_instance_db->key
                                    parent_key                  = lr_instance_db->parent_key
                                    hec_cluster_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-standby
                                    hec_def_master_node         = abap_false
                                    hec_db_node_qty             = lr_instance_db->hec_db_standby_node_qty - <fs_inst_db_before>-hec_db_standby_node_qty ) INTO TABLE lt_act_param.

                    " Success message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_standby_node_added
                                                                   iv_severity = /bobf/cm_frw=>co_severity_success
                                                                   iv_attr1    = CONV #( lr_instance_db->hec_db_standby_node_qty -
                                                                                 <fs_inst_db_before>-hec_db_standby_node_qty )
                                                         CHANGING  co_message  = eo_message ).

                  ELSEIF lr_instance_db->hec_db_standby_node_qty < <fs_inst_db_before>-hec_db_standby_node_qty.
                    lv_attr_name = /hec1/if_configuration_c=>sc_node_attribute-instance_db-hec_db_standby_node_qty.

                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_instance_db->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_instance_db->hec_db_standby_node_qty = <fs_inst_db_before>-hec_db_standby_node_qty.
                    lv_data_changed = abap_true.

                  ELSEIF lr_instance_db->hec_db_standby_node_limit_qty < lr_instance_db->hec_db_standby_node_limit_qty.
                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>node_limit_is_exceeded
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_instance_db->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_instance_db->hec_db_standby_node_qty = <fs_inst_db_before>-hec_db_standby_node_qty.
                    lv_data_changed = abap_true.
                  ENDIF. " IF lr_instance_db->hec_db_standby_node_qty > <fs_inst_db_before>-hec_db_standby_node_qty.


                  "-----------------------------------
                  " Worker node
                  "-----------------------------------
                  IF lr_instance_db->hec_db_worker_node_qty > <fs_inst_db_before>-hec_db_worker_node_qty.
                    " Add non default master node to action table
                    INSERT VALUE #( key                         = lr_instance_db->key
                                    parent_key                  = lr_instance_db->parent_key
                                    hec_cluster_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-worker
                                    hec_def_master_node         = abap_false
                                    hec_db_node_qty             = lr_instance_db->hec_db_worker_node_qty - <fs_inst_db_before>-hec_db_worker_node_qty ) INTO TABLE lt_act_param.

                    " Success message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_worker_node_added
                                                                   iv_severity = /bobf/cm_frw=>co_severity_success
                                                                   iv_attr1    = CONV #( lr_instance_db->hec_db_worker_node_qty -
                                                                                 <fs_inst_db_before>-hec_db_worker_node_qty )
                                                         CHANGING  co_message  = eo_message ).

                  ELSEIF lr_instance_db->hec_db_worker_node_qty < <fs_inst_db_before>-hec_db_worker_node_qty.
                    lv_attr_name = /hec1/if_configuration_c=>sc_node_attribute-instance_db-hec_db_worker_node_qty.

                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_instance_db->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_instance_db->hec_db_worker_node_qty = <fs_inst_db_before>-hec_db_worker_node_qty.
                    lv_data_changed = abap_true.

                  ELSEIF lr_instance_db->hec_db_worker_node_limit_qty < lr_instance_db->hec_db_worker_node_limit_qty.
                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>node_limit_is_exceeded
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_instance_db->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_instance_db->hec_db_worker_node_qty = <fs_inst_db_before>-hec_db_worker_node_qty.
                    lv_data_changed = abap_true.
                  ENDIF. " IF lr_instance_db->hec_db_worker_node_qty > <fs_inst_db_before>-hec_db_worker_node_qty.

                  CLEAR lv_attr_name.
                ENDIF. " IF lr_instance_db->hec_db_cluster_type_guid = <fs_inst_db_before>-hec_db_cluster_type_guid     AND...

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_instance_db->hec_phase_guid NE <fs_inst_db_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_instance_db->key
                                  hec_phase_guid_new = lr_instance_db->hec_phase_guid
                                  hec_phase_guid_old = <fs_inst_db_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_instance_db->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "phasing changed
              ENDIF. " IF <fs_inst_db_before> IS ASSIGNED.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_instance_db->hec_dbst_nodety_clust_ty_guid IS NOT INITIAL AND
                                                                       lr_instance_db->hec_phase_guid                IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete          ).

              IF lv_inst_status <> lr_instance_db->hec_instance_status.
                lr_instance_db->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify instance DB
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_instance_db->key
                                   is_data = lr_instance_db ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_inst_db_before>.
            ENDLOOP.


            "-----------------------------------
            " Set create DB node action to
            " general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param_db_node.
              me->mr_act_param_db_node = NEW /hec1/t_act_create_db_node( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = CORRESPONDING #( is_ctx )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param
                                              ( key = wa_act_node-key )        )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_db_node                                                                                                       ).
            ENDIF.


            "-----------------------------------
            " Set update Phasing action to
            " general
            "-----------------------------------
            IF lt_act_param_phasing IS NOT INITIAL.
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.


            " **********************************
            " Update mode after DB server
            " instance update
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-instance_db-update_after_server_instance.

            LOOP AT lt_instance_db REFERENCE INTO lr_instance_db.
              ASSIGN lt_db_serv_inst[ key = lr_instance_db->parent_key ] TO <fs_db_serv_inst>.

              IF <fs_db_serv_inst> IS ASSIGNED.
                "-----------------------------------
                " Release instance for selection
                "-----------------------------------
                IF <fs_db_serv_inst>-hec_sol_tier_stack_si_guid     IS NOT INITIAL AND
                   <fs_db_serv_inst>-hec_sol_tier_dsi_dbstype_guid  IS NOT INITIAL AND
                   <fs_db_serv_inst>-hec_sol_dbst_oper_sys_guid     IS NOT INITIAL AND
                   <fs_db_serv_inst>-hec_sol_dbst_impltype_guid     IS NOT INITIAL AND
                   <fs_db_serv_inst>-hec_sol_dbst_impty_instty_guid IS NOT INITIAL AND
                   <fs_db_serv_inst>-hec_sol_dbst_imty_inty_al_guid IS NOT INITIAL AND
                   <fs_db_serv_inst>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.

                IF lv_release <> lr_instance_db->hec_row_selectable.
                  lr_instance_db->hec_row_selectable = lv_release.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Modify instance DB
                "-----------------------------------
                IF lv_data_changed = abap_true.
                  io_modify->update( iv_node = is_ctx-node_key
                                     iv_key  = lr_instance_db->key
                                     is_data = lr_instance_db ).
                ENDIF.
              ENDIF. " IF <fs_db_serv_inst> IS ASSIGNED.

              UNASSIGN <fs_db_serv_inst>.
              CLEAR: lv_release,
                     lv_data_changed.

            ENDLOOP. " LOOP AT lt_instance_db...
        ENDCASE.
      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_db_node_cr.

    DATA: lt_instance_db       TYPE /hec1/t_data_db_inst_ct,
          lt_db_node_all       TYPE /hec1/t_data_db_node_ct,
          lt_db_node           TYPE /hec1/t_data_db_node_ct,
          lt_db_node_before    TYPE /hec1/t_data_db_node_ct,
          lt_db_serv_perf_cat  TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_storage_qty    TYPE /hec1/t_data_db_storage_qty_ct,
          lt_db_serv_pc        TYPE /hec1/t_data_db_serv_pc_ct,
          lt_node_key          TYPE /bobf/t_frw_key,
          lt_act_param         TYPE /hec1/t_act_create_db_spc,
          lt_act_param_node    TYPE /hec1/t_act_update_db_node,
          lt_phase             TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    " Get data after update
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_node ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_node-create.
            " Get instance DB node (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_node-to_parent
                                              IMPORTING et_data        = lt_instance_db ).

            " DB master node
            LOOP AT        lt_db_node
            REFERENCE INTO DATA(lr_db_node)
                    WHERE hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master.

              "TODO this needs a more complex logic
              lr_db_node->hec_delete_visible = abap_false.

              "-----------------------------------
              " Check and switch instance status
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_db_node->hec_db_srv_perf_cat_qty IS NOT INITIAL AND
                                                                             lr_db_node->hec_phase_guid          IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete    ).

              IF lv_inst_status <> lr_db_node->hec_instance_status.
                lr_db_node->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_instance_db[ key = lr_db_node->parent_key ] TO FIELD-SYMBOL(<fs_instance_db>).
              IF <fs_instance_db> IS ASSIGNED.
                IF <fs_instance_db>-hec_db_cluster_type_guid IS NOT INITIAL AND
                   <fs_instance_db>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lr_db_node->hec_row_selectable <> lv_release.
                lr_db_node->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "------------------------------------------
              " Set CR related fields from the ROOT node
              "------------------------------------------
              DATA(lv_cr_data_changed) = /hec1/cl_config_helper=>SET_CR_RELATED_FIELDS(
                EXPORTING
                  is_ctx       = is_ctx
                  it_key       = it_key
                  io_read      = io_read
                  io_modify    = io_modify
                  iv_mod_type  = /hec1/if_config_constants=>gc_comp_mod_type-added
                  is_node_data = lr_db_node
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              IF lv_data_changed = abap_false.
                lv_data_changed = lv_cr_data_changed.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " DB server performance category
              "-----------------------------------
              IF NOT ( lr_db_node->hec_server_required    = abap_false AND
                       lr_db_node->hec_db_impl_type_value = '01'           ).  " Implementation type <> Dedicated
                INSERT VALUE #( key            = lr_db_node->key
                                parent_key     = lr_db_node->parent_key
                                hec_db_srv_perf_cat_qty = lr_db_node->hec_db_srv_perf_cat_qty ) INTO TABLE lt_act_param.
              ENDIF.

              "-----------------------------------
              " Modify DB server node
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_node->key
                                   is_data = lr_db_node ).
              ENDIF.

              UNASSIGN <fs_instance_db>.
              CLEAR: lv_inst_status,
                     lv_release,
                     lv_data_changed.
            ENDLOOP.


            "-----------------------------------
            " DB standby/worker node
            "-----------------------------------
            LOOP AT        lt_db_node
            REFERENCE INTO lr_db_node
                     WHERE ( hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha    OR
                             hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi           ) AND
                           ( hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-standby OR
                             hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-worker     ).

              lr_db_node->hec_delete_visible = abap_false.

              "-----------------------------------
              " Check and switch instance status
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_db_node->hec_db_srv_perf_cat_qty IS NOT INITIAL AND
                                                                       lr_db_node->hec_phase_guid          IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete    ).

              IF lv_inst_status <> lr_db_node->hec_instance_status.
                lr_db_node->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Release selection standby/worker
              " node
              "-----------------------------------
              " Check default master node is complete configered
              " ( including sub nodes: server performance category and storage amount )
              DATA(lv_complete) = /hec1/cl_bopf_config_validat_h=>check_master_node_is_complete( iv_check_rule = /hec1/if_bopf_constants=>gc_check_rule-node
                                                                                                 is_ctx        = is_ctx
                                                                                                 it_key        = VALUE #( ( key = lr_db_node->key ) )
                                                                                                 io_read       = io_read ).

              IF ( lv_complete                    = abap_true AND
                   lr_db_node->hec_row_selectable = abap_false    ) OR
                 ( lv_complete                    = abap_false AND
                   lr_db_node->hec_row_selectable = abap_true     ).

                lr_db_node->hec_row_selectable = COND #( WHEN lv_complete = abap_true
                                                         THEN abap_true
                                                         ELSE abap_false              ).
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify DB standby/worker node
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_node->key
                                   is_data = lr_db_node ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_complete,
                     lv_data_changed.
            ENDLOOP.


            "-----------------------------------
            " Set create DB server performance
            " category action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_spc( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_spc )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                              ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_node-update.

            " Get data before update
            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_db_node_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                                              IMPORTING et_data        = lt_db_serv_pc ).



            LOOP AT lt_db_node REFERENCE INTO lr_db_node.

              ASSIGN lt_db_node_before[ key = lr_db_node->key ] TO FIELD-SYMBOL(<fs_db_node_before>).
              IF <fs_db_node_before> IS ASSIGNED.
                "-----------------------------------
                " Fill action table for create
                " DB server performance category
                " for master node
                "-----------------------------------
                IF lr_db_node->hec_db_srv_perf_cat_qty > <fs_db_node_before>-hec_db_srv_perf_cat_qty.
                  " Only for master node
                  IF lr_db_node->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master.
                    INSERT VALUE #( key            = lr_db_node->key
                                    parent_key     = lr_db_node->parent_key
                                    hec_db_srv_perf_cat_qty = lr_db_node->hec_db_srv_perf_cat_qty - <fs_db_node_before>-hec_db_srv_perf_cat_qty ) INTO TABLE lt_act_param.

                    " Success message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_serv_perf_cat_added
                                                                   iv_severity = /bobf/cm_frw=>co_severity_success
                                                                   iv_attr1    = CONV #( lr_db_node->hec_db_srv_perf_cat_qty -
                                                                                 <fs_db_node_before>-hec_db_srv_perf_cat_qty )
                                                         CHANGING  co_message  = eo_message ).

                    " Set flag for deleting subnodes of standby/worker node
                    IF ( lr_db_node->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                         lr_db_node->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi   )   AND
                         lr_db_node->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                         lr_db_node->hec_master_default            = abap_true.
                      lv_data_changed         = abap_true.
                      DATA(lv_delete_subnode) = abap_true.
                    ENDIF.
                  ENDIF. " IF lr_db_node->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master.
                ELSEIF lr_db_node->hec_db_srv_perf_cat_qty < <fs_db_node_before>-hec_db_srv_perf_cat_qty
                   AND lr_db_node->hec_db_srv_perf_cat_qty < lines( VALUE /hec1/t_data_db_serv_pc_ct( FOR db_serv_pc IN lt_db_serv_pc
                                                                                                      WHERE ( parent_key = lr_db_node->key )
                                                                                                      ( db_serv_pc )                         ) ).

                  DATA(lv_attr_name) = /hec1/if_configuration_c=>sc_node_attribute-db_node-hec_db_srv_perf_cat_qty.

                  " Error message
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                 is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                               key      = lr_db_node->key
                                                                                               attributes = VALUE #( ( lv_attr_name ) ) )
                                                       CHANGING  co_message         = eo_message ).

                  " Set node number to value before update
                  lr_db_node->hec_db_srv_perf_cat_qty = <fs_db_node_before>-hec_db_srv_perf_cat_qty.
                  lv_data_changed = abap_true.
                ENDIF. " IF lr_db_node->hec_dn_srv_perf_cat_qty > <fs_db_node_before>-hec_dn_srv_perf_cat_qty.

                "-----------------------------------
                " Fill action table for update
                " phasing
                "-----------------------------------
                IF lr_db_node->hec_phase_guid NE <fs_db_node_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_db_node->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                     lr_db_node->hec_master_default           = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_db_node->key
                                    hec_phase_guid_new = lr_db_node->hec_phase_guid
                                    hec_phase_guid_old = <fs_db_node_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_db_node->hec_phase_changed = abap_true.
                  lv_data_changed               = abap_true.

                  " Set flag for deleting subnodes of standby/worker node
                  IF lr_db_node->hec_db_cluster_type_value = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                     lr_db_node->hec_db_cluster_type_value = /hec1/if_config_constants=>gc_db_clust_node-multi.
                    lv_delete_subnode = abap_true.
                  ENDIF.
                ENDIF. "phasing changed
              ENDIF. " IF <fs_db_node_before> IS ASSIGNED.


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_db_node->hec_db_srv_perf_cat_qty IS NOT INITIAL AND
                                                                       lr_db_node->hec_phase_guid          IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_db_node->hec_instance_status.
                lr_db_node->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Fill action table for delete
              " subnodes of DB standby/worker node
              " or relase standby/worker node
              "-----------------------------------
              IF ( lr_db_node->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                   lr_db_node->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi   )   AND
                   lr_db_node->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                   lr_db_node->hec_master_default            = abap_true                                              AND
                   lv_data_changed                           = abap_true.

                IF NOT line_exists( lt_act_param_node[ key = lr_db_node->key ] ).
                  INSERT VALUE #( key               = lr_db_node->key
                                  parent_key        = lr_db_node->parent_key
                                  do_release_node   = COND #( WHEN lr_db_node->hec_instance_status         = /hec1/if_config_constants=>gc_instance_status-complete   AND
                                                                   <fs_db_node_before>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                              THEN abap_true
                                                               ELSE abap_false                                                  )
                                  do_delete_subnode = COND #( WHEN lr_db_node->hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete OR
                                                                   lv_delete_subnode               = abap_true
                                                              THEN abap_true
                                                              ELSE abap_false                                                                                     ) ) INTO TABLE lt_act_param_node.
                ENDIF.
              ENDIF. " IF ( lr_db_node->hec_db_cluster_type_value = /hec1/if_config_constants=>gc_db_clust_node-ha   OR...


              "-----------------------------------
              " Modify DB node
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_node->key
                                   is_data = lr_db_node ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_attr_name,
                     lv_delete_subnode.

              UNASSIGN <fs_db_node_before>.
            ENDLOOP.

            "-----------------------------------
            " Set create DB server performance
            " category action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_db_spc( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_spc )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                              ).

            ENDIF.

            "-----------------------------------
            " Set update phasing action to
            " general
            "-----------------------------------
            IF lt_act_param_phasing IS NOT INITIAL.
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.


            "-----------------------------------
            " Set update DB node action to
            " general
            "-----------------------------------
            IF lt_act_param_node IS NOT INITIAL.
              CLEAR me->mr_act_param_db_node.
              me->mr_act_param_db_node = NEW /hec1/t_act_update_db_node( lt_act_param_node ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-db_node )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param_node
                                              ( key = wa_act_node-key )     )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_db_node                                                                                                       ).
            ENDIF.


            " **********************************
            " Update mode after instance DB
            " update
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_node-update_after_instance_db.
            " Get instance DB
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_node-to_parent
                                              IMPORTING et_data        = lt_instance_db ).


            LOOP AT lt_db_node REFERENCE INTO lr_db_node.
              ASSIGN lt_instance_db[ key = lr_db_node->parent_key ] TO <fs_instance_db>.

              IF <fs_instance_db> IS ASSIGNED.
                IF <fs_instance_db>-hec_db_cluster_type_guid IS NOT INITIAL AND
                   <fs_instance_db>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              " Release instance for selection
              IF lr_db_node->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                 lv_release <> lr_db_node->hec_row_selectable.
                lr_db_node->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              " Release instance for selection( standby/worker node)
              IF ( lr_db_node->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-standby OR
                   lr_db_node->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-worker     ) AND
                 /hec1/cl_bopf_config_validat_h=>check_standby_node_is_released( iv_check_rule = /hec1/if_bopf_constants=>gc_check_rule-node
                                                                                 is_ctx        = is_ctx
                                                                                 it_key        = it_key
                                                                                 io_read       = io_read                                      ) = abap_true.

                IF lr_db_node->hec_row_selectable <> lv_release.
                  lr_db_node->hec_row_selectable = lv_release.
                  lv_data_changed                = abap_true.
                ENDIF.
              ENDIF.

              " Update DB server cluster type
              IF lr_db_node->hec_db_cluster_type_value <> <fs_instance_db>-hec_db_cluster_type_value.
                lr_db_node->hec_db_cluster_type_value = <fs_instance_db>-hec_db_cluster_type_value.
                lv_data_changed = abap_true.
              ENDIF.
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_node->key
                                   is_data = lr_db_node ).
              ENDIF.

              UNASSIGN <fs_instance_db>.
              CLEAR: lv_data_changed,
                     lv_release.
            ENDLOOP.
        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_db_server_cr.

    DATA: lt_line              TYPE TABLE OF string,
          lv_inf_provider_guid TYPE /hec1/inf_provider_id,
          lv_datacenter_guid   TYPE /hec1/datacenter_fdt_guid,
          lt_db_server         TYPE /hec1/t_data_db_serv_ct,
          lt_db_server_before  TYPE /hec1/t_data_db_serv_ct,
          lt_db_serv_perf_cat  TYPE /hec1/t_data_db_serv_pc_ct,
          lt_phase             TYPE /hec1/t_data_phase_ct,
          lt_act_param         TYPE /hec1/t_act_create_db_storage,
*          lt_act_param_server  TYPE /hec1/t_act_update_db_server,
          lt_act_param_storage TYPE /bobf/t_frw_key,
          lt_act_param_dlvy    TYPE /hec1/t_act_update_dlvy_unit,
          lt_act_param_datac   TYPE /hec1/t_act_update_datacenter,
          lt_act_param_node    TYPE /hec1/t_act_update_db_node,
          lt_act_param_phasing TYPE TABLE OF /hec1/s_act_phase_inherit.



    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_server ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server-create.

            " Get DB server performance category node (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server-to_parent
                                              IMPORTING et_data        = lt_db_serv_perf_cat ).

            LOOP AT        lt_db_server
            REFERENCE INTO DATA(lr_db_server)
                WHERE hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master.

              "-----------------------------------
              " Set Value List Quantity - Server
              "-----------------------------------
              lr_db_server->hec_ip_server_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server(
                                                                           iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                           iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                           iv_sec_datacenter_guid = lr_db_server->hec_sec_datacenter_guid
                                                                           iv_srv_perf_cat_guid   = VALUE #( lt_db_serv_perf_cat[ 1 ]-hec_srv_perf_cat_guid OPTIONAL ) ) )
                                                         THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                         ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              lr_db_server->hec_delete_visible = abap_false.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_db_server->hec_ip_server_guid IS NOT INITIAL AND
                                                                             lr_db_server->hec_phase_guid     IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete          ).

              IF lv_inst_status <> lr_db_server->hec_instance_status.
                lr_db_server->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_db_serv_perf_cat[ key = lr_db_server->parent_key ] TO FIELD-SYMBOL(<fs_db_serv_perf_cat>).
              IF <fs_db_serv_perf_cat> IS ASSIGNED.
                IF <fs_db_serv_perf_cat>-hec_srv_perf_cat_guid IS NOT INITIAL AND
                   <fs_db_serv_perf_cat>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_db_server->hec_row_selectable.
                lr_db_server->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "------------------------------------------
              " Set CR related fields from the ROOT node
              "------------------------------------------
              DATA(lv_cr_data_changed) = /hec1/cl_config_helper=>SET_CR_RELATED_FIELDS(
                EXPORTING
                  is_ctx       = is_ctx
                  it_key       = it_key
                  io_read      = io_read
                  io_modify    = io_modify
                  iv_mod_type  = /hec1/if_config_constants=>gc_comp_mod_type-added
                  is_node_data = lr_db_server
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              "-----------------------------------
              " Fill action table for create
              " DB server storage
              "-----------------------------------
              INSERT VALUE #( key         = lr_db_server->key
                              parent_key  = lr_db_server->parent_key
                              hec_pricing_included = abap_false               ) INTO TABLE lt_act_param.

              "-----------------------------------
              " Modify DB server
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_server->key
                                   is_data = lr_db_server ).
              ENDIF.

              UNASSIGN <fs_db_serv_perf_cat>.
              CLEAR: lv_inst_status,
                     lv_release,
                     lv_data_changed.
            ENDLOOP.


            "-----------------------------------
            " Set create DB server storage
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_db_storage( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_storage )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                  ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_db_server_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get DB Server PC (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server
                                                        it_key         = it_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server-to_parent
                                              IMPORTING et_target_key  = DATA(lt_db_serv_pc_key)
                                                        et_key_link    = DATA(lt_db_serv_pc_key_link) ).

            " Get DB Node (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                        it_key         = lt_db_serv_pc_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-to_parent
                                              IMPORTING et_key_link    = DATA(lt_db_node_key_link) ).

            " Get DB Storage (child)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server-db_storage
                                              IMPORTING et_key_link    = DATA(lt_server_to_storage_link) ).



            LOOP AT lt_db_server REFERENCE INTO lr_db_server.
              ASSIGN lt_db_server_before[ key = lr_db_server->key ] TO FIELD-SYMBOL(<fs_db_server_before>).
              IF <fs_db_server_before> IS ASSIGNED.

                "-----------------------------------
                " Split DB server infrastructure
                " provider server GUID
                "-----------------------------------
                IF lr_db_server->hec_ip_server_guid CA ';'.
                  SPLIT lr_db_server->hec_ip_server_guid
                     AT ';'
                   INTO TABLE lt_line.

                  LOOP AT lt_line ASSIGNING FIELD-SYMBOL(<fs_line>).
                    CASE sy-tabix.
                      WHEN 1.
                        lr_db_server->hec_ip_server_guid = <fs_line>.
                      WHEN 2.
                        lv_inf_provider_guid = <fs_line>.
                      WHEN 3.
                        lv_datacenter_guid = <fs_line>.
                    ENDCASE.
                  ENDLOOP.


                  "-----------------------------------
                  " Fill action table for update
                  " delivery unit
                  "-----------------------------------
                  IF lr_dlvy_unit->hec_inf_provider_guid IS INITIAL.
                    INSERT VALUE #( key                   = lr_dlvy_unit->key
                                    parent_key            = lr_dlvy_unit->parent_key
                                    hec_inf_provider_guid = lv_inf_provider_guid      ) INTO TABLE lt_act_param_dlvy.
                  ENDIF.


                  "-----------------------------------
                  " Fill action table for update
                  " data center
                  "-----------------------------------
                  TRY.
                      DATA(ls_datacenter) = lt_datacenter[ hec_node_datacenter = lr_db_server->hec_tier_datacenter_guid ].

                      IF ls_datacenter-hec_datacenter_guid IS INITIAL.
                        INSERT VALUE #( key                     = ls_datacenter-key
                                        parent_key              = ls_datacenter-parent_key
                                        hec_datacenter_fdt_guid = lv_datacenter_guid       ) INTO TABLE lt_act_param_datac.
*
                        "-----------------------------------
                        " Fill action table for update
                        " db node pricing
                        "-----------------------------------
                        INSERT VALUE #( key = lt_db_node_key_link[ source_key = lr_db_server->parent_key ]-target_key ) INTO TABLE lt_act_param_node.

                      ENDIF. " IF ls_datacenter-hec_datacenter_guid IS INITIAL.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                ENDIF. " IF ls_db_server-hec_ds_ip_server_guid CA ';'.


                "-----------------------------------
                " Infrastructure provider server
                " has changed
                "-----------------------------------
                IF lr_db_server->hec_ip_server_guid    IS NOT INITIAL                            AND
                   lr_db_server->hec_ip_server_guid <> <fs_db_server_before>-hec_ip_server_guid.

                  IF lv_inf_provider_guid IS NOT INITIAL.
                    lr_dlvy_unit->hec_inf_provider_guid = lv_inf_provider_guid.
                  ENDIF.

                  IF lr_db_server->hec_sec_datacenter_guid IS INITIAL     AND
                     lv_datacenter_guid                    IS NOT INITIAL.
                    lr_db_server->hec_sec_datacenter_guid = lv_datacenter_guid.
                    lv_data_changed                   = abap_true.
                  ENDIF.

                  SELECT SINGLE *
                    FROM /hec1/i_serverbasic
                   WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid            AND
                         hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid   AND
                         hec_sec_datacenter_guid = @lr_db_server->hec_sec_datacenter_guid AND
                         hec_ip_server_guid      = @lr_db_server->hec_ip_server_guid
                    INTO @DATA(ls_server).

                  IF ls_server IS NOT INITIAL.
                    lr_db_server->hec_ip_server_descr     = ls_server-hec_ip_server_descr.
                    lr_db_server->hec_ip_server_guid      = ls_server-hec_ip_server_guid.
                    lr_db_server->hec_host_type_descr     = ls_server-hec_srv_host_type_descr.
                    lr_db_server->hec_host_type_value     = ls_server-hec_srv_host_type_value.
                    lr_db_server->hec_ram_size            = ls_server-hec_srv_ram_size.
                    lr_db_server->hec_cpu_size            = ls_server-hec_srv_cpu_size.
                    lr_db_server->hec_sec_datacenter_guid = ls_server-hec_sec_datacenter_guid.
                    lr_db_server->hec_srv_main_stor_qty   = ls_server-hec_srv_main_storage_qty.
                    lr_db_server->hec_tree_descr          = ls_server-hec_ip_server_descr. "#EC CI_FLDEXT_OK[2215424]
                    lr_db_server->hec_srv_flavour         = ls_server-hec_srv_flavour.
                    lr_db_server->hec_saps                = ls_server-hec_saps.
                    lr_db_server->hec_approval_needed     = ls_server-hec_approval_needed.

                    lv_data_changed                       = abap_true.

                    " Set Value List Quantity - Server
                    lr_db_server->hec_ip_server_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server(
                                                                                 iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                 iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                                 iv_sec_datacenter_guid = lr_db_server->hec_sec_datacenter_guid
                                                                                 iv_srv_perf_cat_guid   = VALUE #( lt_db_serv_perf_cat[ 1 ]-hec_srv_perf_cat_guid OPTIONAL ) ) )
                                                               THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                               ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                    " ************************
                    " Get DB server pricing
                    " ************************
                    SELECT SINGLE hec_cb_pricing_lb_guid
                    FROM /hec1/i_serverlbbasic
                   WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid            AND
                         hec_sec_datacenter_guid = @lr_db_server->hec_sec_datacenter_guid AND
                         hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid   AND
                         hec_ip_server_guid      = @lr_db_server->hec_ip_server_guid
                    INTO @DATA(lv_lb_guid).

                    SELECT SINGLE * FROM /hec1/c_cbp_lb "#EC CI_ALL_FIELDS_NEEDED
                       INTO @DATA(ls_pricing)
                      WHERE hec_price_lb = @lv_lb_guid.

                    lr_db_server->* = CORRESPONDING #( BASE ( lr_db_server->* ) ls_pricing ).

                    "-----------------------------------
                    " Fill action table for update
                    " DB server storage
                    "-----------------------------------
                    LOOP AT lt_server_to_storage_link REFERENCE INTO DATA(lr_server_to_storage_link)
                      WHERE source_key = lr_db_server->key.
                      INSERT VALUE #( key = lr_server_to_storage_link->target_key ) INTO TABLE lt_act_param_storage.
                    ENDLOOP.

                  ENDIF. " IF ls_server IS NOT INITIAL.
                ENDIF. " IF lr_db_server->hec_ip_server_guid IS INITIAL


                "-----------------------------------
                " Phase has changed
                "-----------------------------------
                IF lr_db_server->hec_phase_guid NE <fs_db_server_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_db_server->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                     lr_db_server->hec_db_node_default          = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_db_server->key
                                    hec_phase_guid_new = lr_db_server->hec_phase_guid
                                    hec_phase_guid_old = <fs_db_server_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_db_server->hec_phase_changed = abap_true.
                  lv_data_changed                 = abap_true.

                ENDIF. "phasing changed
              ENDIF. " if <fs_db_server_before> is assigned.


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_db_server->hec_ip_server_guid IS NOT INITIAL AND
                                                                       lr_db_server->hec_phase_guid     IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_db_server->hec_instance_status.
                lr_db_server->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Modify DB server
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_server->key
                                   is_data = lr_db_server ).
              ENDIF.

              UNASSIGN: <fs_line>,
                        <fs_db_server_before>.

              CLEAR: lv_inf_provider_guid,
                     lv_datacenter_guid,
                     lv_lb_guid,
                     lv_inst_status,
                     lv_data_changed,
                     ls_datacenter,
                     ls_server,
                     ls_pricing,
                     lt_line.
            ENDLOOP.

            "-----------------------------------
            " Set update delivery unit action to
            " general
            "-----------------------------------
            IF lt_act_param_dlvy IS NOT INITIAL.
              CLEAR me->mr_act_param_dlvy.
              me->mr_act_param_dlvy = NEW /hec1/t_act_update_dlvy_unit( lt_act_param_dlvy ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-delivery_unit )
                    it_key          = VALUE #( FOR wa_act_dlvy IN lt_act_param_dlvy
                                              ( key = wa_act_dlvy-key )    )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_delivery_unit )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_dlvy                                                                                                                ).

            ENDIF.

            "-----------------------------------
            " Set update data center action to
            " general
            "-----------------------------------
            IF lt_act_param_datac IS NOT INITIAL.
              CLEAR me->mr_act_param_datac.
              me->mr_act_param_datac = NEW /hec1/t_act_update_datacenter( lt_act_param_datac ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-datacenter )
                    it_key          = VALUE #( FOR wa_act_datac IN lt_act_param_datac
                                              ( key = wa_act_datac-key )     )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_datacenter )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_datac                                                                                                            ).

            ENDIF.

            "-----------------------------------
            " Set DB Node action to
            " general
            "-----------------------------------
            IF lt_act_param_node IS NOT INITIAL.

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-db_node )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param_node
                                             ( key = wa_act_node-key )             )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                           ).

            ENDIF.

            "-----------------------------------
            " Set update DB Storage action to
            " general
            "-----------------------------------
            IF lt_act_param_storage IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-db_storage )
                  it_key          = lt_act_param_storage
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_storage )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                                                                          ).
            ENDIF.

            "-----------------------------------
            " Set update phase action to general
            "-----------------------------------
            IF lt_act_param_phasing IS NOT INITIAL.
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).

            ENDIF.


            " ***************************************************************************
            " Update mode after app server
            " performance category update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server-update_after_serv_perf_cat.

            io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                         it_key  = it_key
                               IMPORTING et_data = lt_db_server ).

            " Get DB server performance category (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server-to_parent
                                              IMPORTING et_data        = lt_db_serv_perf_cat ).


            LOOP AT lt_db_server REFERENCE INTO lr_db_server.
              ASSIGN lt_db_serv_perf_cat[ key = lr_db_server->parent_key ] TO <fs_db_serv_perf_cat>.

              IF <fs_db_serv_perf_cat> IS ASSIGNED.
                IF <fs_db_serv_perf_cat>-hec_srv_perf_cat_guid IS NOT INITIAL AND
                   <fs_db_serv_perf_cat>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              IF lv_release <> lr_db_server->hec_row_selectable.
                lr_db_server->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Update DB server cluster type
              "-----------------------------------
              IF lr_db_server->hec_db_cluster_type_value <> <fs_db_serv_perf_cat>-hec_db_cluster_type_value.
                lr_db_server->hec_db_cluster_type_value = <fs_db_serv_perf_cat>-hec_db_cluster_type_value.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_server->key
                                   is_data = lr_db_server ).
              ENDIF.

              UNASSIGN <fs_db_serv_perf_cat>.
              CLEAR: lv_release,
                     lv_data_changed.

            ENDLOOP. " LOOP AT lt_db_server REFERENCE INTO lr_db_server.
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_db_server_instanc_cr.

    DATA: lt_db_serv_inst        TYPE /hec1/t_data_db_server_inst_ct,
          lt_db_serv_inst_before TYPE /hec1/t_data_db_server_inst_ct,
          lt_instance_db         TYPE /hec1/t_data_db_inst_ct,
          lt_tier                TYPE /hec1/t_data_tier_ct,
          lt_tier_all            TYPE /hec1/t_data_tier_ct,
          lt_solution            TYPE /hec1/t_data_solution_ct,
          ls_landscape           TYPE /hec1/s_config_root_cs,
          lt_act_param           TYPE /hec1/t_act_create_instance_db,
          lt_act_param_delete    TYPE /bobf/t_frw_node,
          lt_phase               TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing   TYPE TABLE OF /hec1/s_act_phase_inherit.

    CLEAR: eo_message,
           et_failed_key.

    " Data before update
    io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                 it_key          = it_key
                                 iv_before_image = abap_true
                       IMPORTING et_data         = lt_db_serv_inst_before ).

    " Data after update
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_serv_inst ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    "-----------------------------------
    " Get APM model GUID and description
    "-----------------------------------
    /hec1/cl_config_helper=>get_apm_model( EXPORTING iv_node_key   = is_ctx-node_key
                                                     it_key        = it_key
                                                     io_read       = io_read
                                           IMPORTING et_failed_key = et_failed_key
                                                     es_apm_model  = ls_landscape ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server_instance-create.

            LOOP AT lt_db_serv_inst REFERENCE INTO DATA(lr_db_serv_inst).

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              " Server Instance
              lr_db_serv_inst->hec_sol_tier_stack_si_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server_instance(
                                                                                      iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                      iv_sol_tier_stack_guid = lr_db_serv_inst->hec_sol_tier_stack_si_guid
                                                                                      iv_srv_inst_rel_value  = lr_db_serv_inst->hec_srv_inst_rel_value
                                                                                      iv_solution_guid       = lr_db_serv_inst->hec_solution_guid ) )
                                                                    THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                    ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " DB Type
              lr_db_serv_inst->hec_sol_tier_dsi_dbstype_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_server_type(
                                                                                          iv_apm_guid               = lr_landscape->hec_apm_guid
                                                                                          iv_sol_tier_stack_si_guid = lr_db_serv_inst->hec_sol_tier_stack_si_guid ) )
                                                                       THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                       ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " Implementation Type
              lr_db_serv_inst->hec_sol_dbst_impltype_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_implementation_type(
                                                                                      iv_apm_guid                  = lr_landscape->hec_apm_guid
                                                                                      iv_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid ) )
                                                                    THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                    ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " Instance Type
              lr_db_serv_inst->hec_sol_dbst_impty_instty_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_instance_type(
                                                                                          iv_apm_guid                  = lr_landscape->hec_apm_guid
                                                                                          iv_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid
                                                                                          iv_sol_dbst_impltype_guid    = lr_db_serv_inst->hec_sol_dbst_impltype_guid ) )
                                                                        THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                        ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " Allocation
              lr_db_serv_inst->hec_sol_dbst_imty_inty_al_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_allocation(
                                                                                          iv_apm_guid                   = lr_landscape->hec_apm_guid
                                                                                          iv_sol_tier_dsi_dbstype_guid  = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid
                                                                                          iv_sol_dbst_impty_instty_guid = lr_db_serv_inst->hec_sol_dbst_impty_instty_guid ) )
                                                                        THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                        ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " Operating System
              lr_db_serv_inst->hec_sol_dbst_oper_sys_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_operating_system(
                                                                                      iv_apm_guid                  = lr_landscape->hec_apm_guid
                                                                                      iv_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid ) )
                                                                    THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                    ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              lr_db_serv_inst->hec_delete_visible = abap_false.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_db_serv_inst->hec_sol_tier_stack_si_guid     IS NOT INITIAL AND
                                                                             lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid  IS NOT INITIAL AND
                                                                             lr_db_serv_inst->hec_sol_dbst_oper_sys_guid     IS NOT INITIAL AND
                                                                             lr_db_serv_inst->hec_sol_dbst_impltype_guid     IS NOT INITIAL AND
                                                                             lr_db_serv_inst->hec_sol_dbst_impty_instty_guid IS NOT INITIAL AND
                                                                             lr_db_serv_inst->hec_sol_dbst_imty_inty_al_guid IS NOT INITIAL AND
                                                                             lr_db_serv_inst->hec_phase_guid                 IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete            ).

              IF lv_inst_status <> lr_db_serv_inst->hec_instance_status.
                lr_db_serv_inst->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "------------------------------------------
              " Set CR related fields from the ROOT node
              "------------------------------------------
              DATA(lv_cr_data_changed) = /hec1/cl_config_helper=>SET_CR_RELATED_FIELDS(
                EXPORTING
                  is_ctx       = is_ctx
                  it_key       = it_key
                  io_read      = io_read
                  io_modify    = io_modify
                  iv_mod_type  = /hec1/if_config_constants=>gc_comp_mod_type-added
                  is_node_data = lr_db_serv_inst
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              IF lv_data_changed = abap_false.
                lv_data_changed = lv_cr_data_changed.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " instance DB action
              "-----------------------------------
              IF lr_db_serv_inst->hec_db_quantity IS NOT INITIAL.
                INSERT VALUE #( key             = lr_db_serv_inst->key
                                parent_key      = lr_db_serv_inst->parent_key
                                hec_db_quantity = lr_db_serv_inst->hec_db_quantity ) INTO TABLE lt_act_param.
              ENDIF.

              "-----------------------------------
              " Modify DB server instance
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_serv_inst->key
                                   is_data = lr_db_serv_inst ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP.

            "-----------------------------------
            " Set create Instance DB action to
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_instance_db( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_inst_db )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                ).
            ENDIF.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server_instance-update.

            " Get instance DB
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-instance_db
                                              IMPORTING et_data        = lt_instance_db ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-to_parent
                                              IMPORTING et_data        = lt_tier
                                                        et_target_key  = DATA(lt_tier_key) ).


            IF line_exists( lt_tier[ hec_related_stack = abap_true ] ).
              io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                          it_key         = lt_tier_key
                                                          iv_fill_data   = abap_true
                                                          iv_association = /hec1/if_configuration_c=>sc_association-tier-to_parent
                                                IMPORTING et_data        = lt_solution
                                                          et_target_key  = DATA(lt_solution_key) ).


              io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-solution
                                                          it_key         = lt_solution_key
                                                          iv_fill_data   = abap_true
                                                          iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                                IMPORTING et_data        = lt_tier_all ).
            ENDIF.

            "-----------------------------------
            " Get DB server type
            "-----------------------------------
            SELECT *
              FROM /hec1/i_dbservertypebasic
             WHERE hec_apm_guid  = @ls_landscape-hec_apm_guid
              INTO TABLE @DATA(lt_db_server_type).


            "-----------------------------------
            " Get DB server operating system
            "-----------------------------------
            SELECT *
              FROM /hec1/i_dboperssystembasic
             WHERE hec_apm_guid  = @ls_landscape-hec_apm_guid
              INTO TABLE @DATA(lt_db_operating_sys).


            "-----------------------------------
            " Get DB server implementation type
            "-----------------------------------
            SELECT *
              FROM /hec1/i_dbimplementtypebasic
             WHERE hec_apm_guid  = @ls_landscape-hec_apm_guid
              INTO TABLE @DATA(lt_db_impl_type).


            "-----------------------------------
            " Get DB server instance type
            "-----------------------------------
            SELECT *
              FROM /hec1/i_dbinstancetypebasic
             WHERE hec_apm_guid  = @ls_landscape-hec_apm_guid
              INTO TABLE @DATA(lt_db_inst_type).


            "-----------------------------------
            " Get DB server allocation
            "-----------------------------------
            SELECT *
              FROM /hec1/i_dballocationbasic
             WHERE hec_apm_guid  = @ls_landscape-hec_apm_guid
              INTO TABLE @DATA(lt_db_allocation).



            LOOP AT lt_db_serv_inst REFERENCE INTO lr_db_serv_inst.

              ASSIGN lt_db_serv_inst_before[ key = lr_db_serv_inst->key ] TO FIELD-SYMBOL(<fs_db_serv_inst_before>).
              IF <fs_db_serv_inst_before> IS ASSIGNED.

                lr_db_serv_inst->hec_delete_visible = abap_false.

                "-----------------------------------
                " DB server type has changed
                "-----------------------------------
                IF lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid IS NOT INITIAL                                   AND
                   lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid <> <fs_db_serv_inst_before>-hec_sol_tier_dsi_dbstype_guid.
                  TRY.
                      DATA(ls_db_server_type) = lt_db_server_type[ hec_sol_tier_stack_si_guid    = lr_db_serv_inst->hec_sol_tier_stack_si_guid
                                                                   hec_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid ].

                      lr_db_serv_inst->hec_db_srv_type_guid      = ls_db_server_type-hec_db_srv_type_guid.
                      lr_db_serv_inst->hec_db_srv_type_value     = ls_db_server_type-hec_db_srv_type_value.
                      lr_db_serv_inst->hec_db_srv_type_descr     = ls_db_server_type-hec_db_srv_type_descr.
                      lr_db_serv_inst->hec_calc_setup_dr         = ls_db_server_type-hec_calc_setup_dr.
                      lr_db_serv_inst->hec_ty_support_stat_value = ls_db_server_type-hec_ty_support_stat_value.
                      lr_db_serv_inst->hec_ty_support_stat_descr = ls_db_server_type-hec_ty_support_stat_descr.
                      lr_db_serv_inst->hec_tree_descr            = ls_db_server_type-hec_db_srv_type_descr.

                      lv_data_changed                            = abap_true.

                      " Set Value List Quantity
                      " DB Type
                      lr_db_serv_inst->hec_sol_tier_dsi_dbstype_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_server_type(
                                                                                                  iv_apm_guid               = lr_landscape->hec_apm_guid
                                                                                                  iv_sol_tier_stack_si_guid = lr_db_serv_inst->hec_sol_tier_stack_si_guid ) )
                                                                               THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                               ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                      IF lr_db_serv_inst->hec_init_ty_support_stat_value IS INITIAL.
                        lr_db_serv_inst->hec_init_ty_support_stat_value = lr_db_serv_inst->hec_ty_support_stat_value.
                        lr_db_serv_inst->hec_init_ty_support_stat_descr = lr_db_serv_inst->hec_ty_support_stat_descr.
                      ENDIF.

                      IF lr_db_serv_inst->hec_sol_dbst_oper_sys_guid IS INITIAL.
                        "-----------------------------------
                        " If there is only one operating
                        " system, then it should be
                        " preselected
                        "-----------------------------------
                        DATA(lt_operating_sys) = VALUE /hec1/t_apm_db_operating_sys( FOR wa_os IN lt_db_operating_sys
                                                                                     WHERE ( hec_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid )
                                                                                     ( CORRESPONDING #( wa_os ) )                                                             ).

                        IF lines( lt_operating_sys ) = 1.
                          TRY.
                              lr_db_serv_inst->hec_sol_dbst_oper_sys_guid = lt_operating_sys[ 1 ]-hec_sol_dbst_oper_sys_guid.
                            CATCH cx_sy_itab_line_not_found.
                          ENDTRY.
                          "-----------------------------------
                          " If there are multiple operating
                          " systems possible and Linux is
                          " between them - set it preselected
                          "-----------------------------------
                        ELSEIF lines( lt_operating_sys ) > 1 AND line_exists( lt_operating_sys[ hec_operating_sys_value = /hec1/cl_rep_config_data=>c_os_linux ] ).
                          TRY.
                              lr_db_serv_inst->hec_sol_dbst_oper_sys_guid = lt_operating_sys[ hec_operating_sys_value = /hec1/cl_rep_config_data=>c_os_linux ]-hec_sol_dbst_oper_sys_guid.
                            CATCH cx_sy_itab_line_not_found.
                          ENDTRY.
                        ENDIF. " IF lines( lt_operating_sys ) = 1.
                      ENDIF. " IF lr_db_serv_inst->hec_sol_dbst_oper_sys_guid IS INITIAL.

                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  CLEAR: ls_db_server_type,
                         lt_operating_sys.
                ENDIF.

                "-----------------------------------
                " DB operating system has changed
                "-----------------------------------
                IF lr_db_serv_inst->hec_sol_dbst_oper_sys_guid IS NOT INITIAL                                         AND
                   lr_db_serv_inst->hec_sol_dbst_oper_sys_guid <> <fs_db_serv_inst_before>-hec_sol_dbst_oper_sys_guid.

                  TRY.
                      DATA(ls_operating_sys) = lt_db_operating_sys[ hec_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid
                                                                    hec_sol_dbst_oper_sys_guid    = lr_db_serv_inst->hec_sol_dbst_oper_sys_guid    ].

                      lr_db_serv_inst->hec_operating_sys_guid    = ls_operating_sys-hec_operating_sys_guid.
                      lr_db_serv_inst->hec_operating_sys_value   = ls_operating_sys-hec_operating_sys_value.
                      lr_db_serv_inst->hec_operating_sys_descr   = ls_operating_sys-hec_operating_sys_descr.
                      lr_db_serv_inst->hec_os_support_stat_value = ls_operating_sys-hec_os_support_stat_value.
                      lr_db_serv_inst->hec_os_support_stat_descr = ls_operating_sys-hec_os_support_stat_descr.

                      lv_data_changed                            = abap_true.

                      " Set Value List Quantity - Operating System
                      lr_db_serv_inst->hec_sol_dbst_oper_sys_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_operating_system(
                                                                                              iv_apm_guid                  = lr_landscape->hec_apm_guid
                                                                                              iv_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid ) )
                                                                            THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                            ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                      IF lr_db_serv_inst->hec_init_os_support_stat_value IS INITIAL.
                        lr_db_serv_inst->hec_init_os_support_stat_value = lr_db_serv_inst->hec_os_support_stat_value.
                        lr_db_serv_inst->hec_init_os_support_stat_descr = lr_db_serv_inst->hec_os_support_stat_descr.
                      ENDIF.

                      IF lr_db_serv_inst->hec_sol_dbst_impltype_guid IS INITIAL.
                        DATA(lt_impl_type) = VALUE /hec1/t_apm_db_implement_type( FOR wa_imp IN lt_db_impl_type
                                                                                  WHERE ( hec_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid )
                                                                                 ( CORRESPONDING #( wa_imp ) )                                                             ).

                        IF lines( lt_impl_type ) = 1.
                          lr_db_serv_inst->hec_sol_dbst_impltype_guid = lt_impl_type[ 1 ]-hec_sol_dbst_impltype_guid.
                        ENDIF.
                      ENDIF. " IF lr_db_serv_inst->hec_sol_dbst_impltype_guid IS INITIAL.

                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  CLEAR: ls_operating_sys,
                         lt_impl_type.
                ENDIF.

                "-----------------------------------
                " DB implementation type has changed
                "-----------------------------------
                IF lr_db_serv_inst->hec_sol_dbst_impltype_guid IS NOT INITIAL                                         AND
                   lr_db_serv_inst->hec_sol_dbst_impltype_guid <> <fs_db_serv_inst_before>-hec_sol_dbst_impltype_guid.

                  TRY.
                      DATA(ls_impl_type) = lt_db_impl_type[ hec_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid
                                                            hec_sol_dbst_impltype_guid    = lr_db_serv_inst->hec_sol_dbst_impltype_guid    ].

                      lr_db_serv_inst->hec_db_impl_type_guid      = ls_impl_type-hec_db_impl_type_guid.
                      lr_db_serv_inst->hec_db_impl_type_value     = ls_impl_type-hec_db_impl_type_value.
                      lr_db_serv_inst->hec_db_impl_type_descr     = ls_impl_type-hec_db_impl_type_descr.
                      lr_db_serv_inst->hec_imp_support_stat_value = ls_impl_type-hec_imp_support_stat_value.
                      lr_db_serv_inst->hec_imp_support_stat_descr = ls_impl_type-hec_imp_support_stat_descr.

                      lv_data_changed                             = abap_true.

                      " Set Value List Quantity - Implementation Type
                      lr_db_serv_inst->hec_sol_dbst_impltype_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_implementation_type(
                                                                                              iv_apm_guid                  = lr_landscape->hec_apm_guid
                                                                                              iv_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid ) )
                                                                            THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                            ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                      IF lr_db_serv_inst->hec_init_imp_supp_stat_value IS INITIAL.
                        lr_db_serv_inst->hec_init_imp_supp_stat_value = lr_db_serv_inst->hec_imp_support_stat_value.
                        lr_db_serv_inst->hec_init_imp_supp_stat_descr = lr_db_serv_inst->hec_imp_support_stat_descr.
                      ENDIF.

                      " Get DB instance type
                      DATA(lt_inst_type) = VALUE /hec1/t_apm_db_instance_type( FOR wa IN lt_db_inst_type
                                                                               WHERE ( hec_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid AND
                                                                                       hec_sol_dbst_impltype_guid    = lr_db_serv_inst->hec_sol_dbst_impltype_guid        )
                                                                               ( CORRESPONDING #( wa ) )                                                                    ).

                      IF lines( lt_inst_type ) = 1.
                        lr_db_serv_inst->hec_sol_dbst_impty_instty_guid = lt_inst_type[ 1 ]-hec_sol_dbst_impty_instty_guid.
                      ENDIF.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  CLEAR: ls_impl_type,
                         lt_inst_type.
                ENDIF. " IF lr_db_serv_inst->hec_db_impl_type_guid IS NOT INITIAL...

                "-----------------------------------
                " DB instance type has changed
                "-----------------------------------
                IF lr_db_serv_inst->hec_sol_dbst_impty_instty_guid IS NOT INITIAL                                             AND
                   lr_db_serv_inst->hec_sol_dbst_impty_instty_guid <> <fs_db_serv_inst_before>-hec_sol_dbst_impty_instty_guid.

                  TRY.
                      DATA(ls_inst_type) = lt_db_inst_type[ hec_sol_tier_dsi_dbstype_guid  = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid
                                                            hec_sol_dbst_impltype_guid     = lr_db_serv_inst->hec_sol_dbst_impltype_guid
                                                            hec_sol_dbst_impty_instty_guid = lr_db_serv_inst->hec_sol_dbst_impty_instty_guid ].

                      lr_db_serv_inst->hec_db_inst_type_guid       = ls_inst_type-hec_db_inst_type_guid.
                      lr_db_serv_inst->hec_db_inst_type_value      = ls_inst_type-hec_db_inst_type_value.
                      lr_db_serv_inst->hec_db_inst_type_descr      = ls_inst_type-hec_db_inst_type_descr.
                      lr_db_serv_inst->hec_inst_support_stat_value = ls_inst_type-hec_inst_support_stat_value.
                      lr_db_serv_inst->hec_inst_support_stat_descr = ls_inst_type-hec_inst_support_stat_descr.

                      lv_data_changed                              = abap_true.

                      " Set Value List Quantity - Instance Type
                      lr_db_serv_inst->hec_sol_dbst_impty_instty_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_instance_type(
                                                                                                  iv_apm_guid                  = lr_landscape->hec_apm_guid
                                                                                                  iv_sol_tier_dsi_dbstype_guid = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid
                                                                                                  iv_sol_dbst_impltype_guid    = lr_db_serv_inst->hec_sol_dbst_impltype_guid ) )
                                                                                THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                                ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                      IF lr_db_serv_inst->hec_init_inst_supp_stat_value IS INITIAL.
                        lr_db_serv_inst->hec_init_inst_supp_stat_value = lr_db_serv_inst->hec_inst_support_stat_value.
                        lr_db_serv_inst->hec_init_inst_supp_stat_descr = lr_db_serv_inst->hec_inst_support_stat_descr.
                      ENDIF.

                      DATA(lt_allocation) = VALUE /hec1/t_apm_db_allocation( FOR wa_allo IN lt_db_allocation
                                                                             WHERE ( hec_sol_tier_dsi_dbstype_guid  = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid  AND
                                                                                     hec_sol_dbst_impty_instty_guid = lr_db_serv_inst->hec_sol_dbst_impty_instty_guid     )
                                                                             ( CORRESPONDING #( wa_allo ) ) ).

                      IF lines( lt_allocation ) = 1.
                        lr_db_serv_inst->hec_sol_dbst_imty_inty_al_guid = lt_allocation[ 1 ]-hec_sol_dbst_imty_inty_al_guid.
                      ENDIF.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  CLEAR: ls_inst_type,
                         lt_allocation.
                ENDIF.

                "-----------------------------------
                " DB allocation has changed
                "-----------------------------------
                IF lr_db_serv_inst->hec_sol_dbst_imty_inty_al_guid IS NOT INITIAL                                             AND
                   lr_db_serv_inst->hec_sol_dbst_imty_inty_al_guid <> <fs_db_serv_inst_before>-hec_sol_dbst_imty_inty_al_guid.

                  TRY.
                      DATA(ls_allocation) = lt_db_allocation[ hec_sol_tier_dsi_dbstype_guid  = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid
                                                              hec_sol_dbst_impty_instty_guid = lr_db_serv_inst->hec_sol_dbst_impty_instty_guid
                                                              hec_sol_dbst_imty_inty_al_guid = lr_db_serv_inst->hec_sol_dbst_imty_inty_al_guid ].

                      lr_db_serv_inst->hec_db_allocation_guid       = ls_allocation-hec_db_allocation_guid.
                      lr_db_serv_inst->hec_db_allocation_value      = ls_allocation-hec_db_allocation_value.
                      lr_db_serv_inst->hec_db_allocation_descr      = ls_allocation-hec_db_allocation_descr.
                      lr_db_serv_inst->hec_db_quantity              = ls_allocation-hec_db_quantity.
                      lr_db_serv_inst->hec_alloc_support_stat_value = ls_allocation-hec_alloc_support_stat_value.
                      lr_db_serv_inst->hec_alloc_support_stat_descr = ls_allocation-hec_alloc_support_stat_descr.

                      lv_data_changed = abap_true.

                      " Set Value List Quantity - Allocation
                      lr_db_serv_inst->hec_sol_dbst_imty_inty_al_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_db_allocation(
                                                                                                  iv_apm_guid                   = lr_landscape->hec_apm_guid
                                                                                                  iv_sol_tier_dsi_dbstype_guid  = lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid
                                                                                                  iv_sol_dbst_impty_instty_guid = lr_db_serv_inst->hec_sol_dbst_impty_instty_guid ) )
                                                                                THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                                ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                      IF lr_db_serv_inst->hec_init_alloc_supp_stat_value IS INITIAL.
                        lr_db_serv_inst->hec_init_alloc_supp_stat_value = lr_db_serv_inst->hec_alloc_support_stat_value.
                        lr_db_serv_inst->hec_init_alloc_supp_stat_descr = lr_db_serv_inst->hec_alloc_support_stat_descr.
                      ENDIF.

                      " After a reset of the DB allocation the subnodes are not deleted.
                      " In this case, no additional instance DB should be created.
                      IF NOT line_exists( lt_instance_db[ parent_key = lr_db_serv_inst->key ] ).
                        "-----------------------------------
                        " Fill action table for create
                        " instance DB action
                        "-----------------------------------
                        INSERT VALUE #( key             = lr_db_serv_inst->key
                                        parent_key      = lr_db_serv_inst->parent_key
                                        hec_db_quantity = lr_db_serv_inst->hec_db_quantity ) INTO TABLE lt_act_param.
                      ENDIF.

                      " Set Tier
                      IF lr_db_serv_inst->hec_db_allocation_value = /hec1/if_config_constants=>gc_db_allocation-internal.
                        DATA(ls_tier) = VALUE #( lt_tier[ key = lr_db_serv_inst->parent_key ] OPTIONAL ).
                        lr_db_serv_inst->hec_db_tier_guid  = ls_tier-hec_node_tier.
                        lr_db_serv_inst->hec_db_tier_descr = ls_tier-hec_tree_descr.
                      ENDIF.

                      " If the allocation type is "related tier" the related tier needs to be selected automatically.
                      IF lr_db_serv_inst->hec_db_allocation_value = /hec1/if_config_constants=>gc_db_allocation-related_stack.
                        ls_tier = VALUE #( lt_tier[ key = lr_db_serv_inst->parent_key ] OPTIONAL ).

                        LOOP AT lt_tier_all ASSIGNING FIELD-SYMBOL(<fs_tier_related>)
                          WHERE hec_node_tier NE ls_tier-hec_node_tier
                            AND hec_related_stack_guid = ls_tier-hec_related_stack_guid.
                          DATA(ls_tier_related) = <fs_tier_related>.
                        ENDLOOP.

                        lr_db_serv_inst->hec_db_tier_guid  = ls_tier_related-hec_node_tier.
                        lr_db_serv_inst->hec_db_tier_descr = ls_tier_related-hec_tree_descr.
                      ENDIF.

                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  CLEAR ls_allocation.
                ENDIF. " IF lr_db_serv_inst->hec_db_allocation_guid IS NOT INITIAL

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_db_serv_inst->hec_phase_guid NE <fs_db_serv_inst_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_db_serv_inst->key
                                  hec_phase_guid_new = lr_db_serv_inst->hec_phase_guid
                                  hec_phase_guid_old = <fs_db_serv_inst_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_db_serv_inst->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "phasing changed

                "-----------------------------------
                " Reset fields
                " - these are all triggered from
                "   the BOPF-actions
                "-----------------------------------
                " The following fields are all dependent on each other. If one field is cleared, the subsequent fields have to be cleared as well.
                " These fields always come in triples (GUID, Value, Description)
                IF lr_db_serv_inst->hec_sol_tier_stack_si_guid          IS INITIAL      AND
                   <fs_db_serv_inst_before>-hec_sol_tier_stack_si_guid  IS NOT INITIAL.

                  CLEAR: lr_db_serv_inst->hec_sol_tier_stack_si_guid,
                         lr_db_serv_inst->hec_sol_tier_dsi_descr,
                         " Reset Server Type
                         lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid.

                ENDIF.

                IF lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid          IS INITIAL      AND
                   <fs_db_serv_inst_before>-hec_sol_tier_dsi_dbstype_guid  IS NOT INITIAL.

                  CLEAR: lr_db_serv_inst->hec_sol_tier_dsi_dbstype_guid,
                         lr_db_serv_inst->hec_db_srv_type_guid,
                         lr_db_serv_inst->hec_db_srv_type_value,
                         lr_db_serv_inst->hec_db_srv_type_descr,
                         " Reset Operating System
                         lr_db_serv_inst->hec_operating_sys_guid.

                ENDIF.

                IF lr_db_serv_inst->hec_operating_sys_guid         IS INITIAL   AND
                   <fs_db_serv_inst_before>-hec_operating_sys_guid IS NOT INITIAL.

                  CLEAR: lr_db_serv_inst->hec_sol_dbst_oper_sys_guid,
                         lr_db_serv_inst->hec_operating_sys_guid,
                         lr_db_serv_inst->hec_operating_sys_value,
                         lr_db_serv_inst->hec_operating_sys_descr,
                         " Reset Implementation Type
                         lr_db_serv_inst->hec_db_impl_type_guid.

                  lv_data_changed = abap_true.
                ENDIF.

                IF lr_db_serv_inst->hec_db_impl_type_guid         IS INITIAL     AND
                   <fs_db_serv_inst_before>-hec_db_impl_type_guid IS NOT INITIAL.

                  CLEAR: lr_db_serv_inst->hec_sol_dbst_impltype_guid,
                         lr_db_serv_inst->hec_db_impl_type_guid,
                         lr_db_serv_inst->hec_db_impl_type_value,
                         lr_db_serv_inst->hec_db_impl_type_descr,
                         " Reset Instance Type
                         lr_db_serv_inst->hec_db_inst_type_guid.

                  lv_data_changed = abap_true.
                ENDIF.

                IF lr_db_serv_inst->hec_db_inst_type_guid         IS INITIAL      AND
                   <fs_db_serv_inst_before>-hec_db_inst_type_guid IS NOT INITIAL.

                  CLEAR: lr_db_serv_inst->hec_sol_dbst_impty_instty_guid,
                         lr_db_serv_inst->hec_db_inst_type_guid,
                         lr_db_serv_inst->hec_db_inst_type_value,
                         lr_db_serv_inst->hec_db_inst_type_descr,
                         " Reset Allocation
                         lr_db_serv_inst->hec_db_allocation_guid.

                  lv_data_changed = abap_true.

                  LOOP AT lt_instance_db ASSIGNING FIELD-SYMBOL(<fs_instance_db>)
                    WHERE parent_key = lr_db_serv_inst->key.

                    " Add instance db to delete table
                    INSERT VALUE #( node = /hec1/if_configuration_c=>sc_node-instance_db
                                    key  = <fs_instance_db>-key ) INTO TABLE lt_act_param_delete.

                  ENDLOOP.
                ENDIF.

                IF lr_db_serv_inst->hec_db_allocation_guid        IS INITIAL      AND
                  <fs_db_serv_inst_before>-hec_db_allocation_guid IS NOT INITIAL.

                  CLEAR: lr_db_serv_inst->hec_db_allocation_descr,
                         lr_db_serv_inst->hec_db_allocation_value,
                         lr_db_serv_inst->hec_sol_dbst_imty_inty_al_guid,
                         lr_db_serv_inst->hec_db_tier_guid,
                         lr_db_serv_inst->hec_db_tier_descr.

                  lv_data_changed = abap_true.

                ENDIF.

              ENDIF. " if <fs_db_server_instance_before> is assigned.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_db_serv_inst->hec_operating_sys_value IS NOT INITIAL AND
                                                                       lr_db_serv_inst->hec_db_impl_type_guid       IS NOT INITIAL AND
                                                                       lr_db_serv_inst->hec_db_inst_type_guid       IS NOT INITIAL AND
                                                                       lr_db_serv_inst->hec_db_allocation_guid      IS NOT INITIAL AND
                                                                       lr_db_serv_inst->hec_phase_guid              IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete         ).

              IF lv_inst_status <> lr_db_serv_inst->hec_instance_status.
                lr_db_serv_inst->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify DB server instance
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_serv_inst->key
                                   is_data = lr_db_serv_inst ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_db_serv_inst_before>.
            ENDLOOP.


            "-----------------------------------
            " Set create Instance DB action to
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_instance_db( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_inst_db )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                ).
            ENDIF.


            "-----------------------------------
            " Set Delete action DB Instance
            " to general
            "-----------------------------------
            IF lt_act_param_delete IS NOT INITIAL.
              me->mr_act_param_delete = NEW /bobf/t_frw_node( lt_act_param_delete ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-delete_node )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_delete ).
            ENDIF.

            "-----------------------------------
            " Set update phase action to
            " general
            "-----------------------------------
            IF lt_act_param_phasing IS NOT INITIAL.
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.

            " ***************************************************************************
            " Update mode after tier update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server_instance-update_after_tier.

            " Get tier
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-to_parent
                                              IMPORTING et_data        = lt_tier ).

            "-----------------------------------
            " Release instance for selection
            "-----------------------------------
            LOOP AT lt_db_serv_inst REFERENCE INTO lr_db_serv_inst.
              ASSIGN lt_tier[ key = lr_db_serv_inst->parent_key ] TO FIELD-SYMBOL(<fs_tier>).

              IF <fs_tier> IS ASSIGNED.
                "-----------------------------------
                " Release instance for selection
                "-----------------------------------
                IF <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                   <fs_tier>-hec_tier_type_value      IS NOT INITIAL AND
                   <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL.
                  DATA(lv_release) = abap_true.
                ENDIF.

                IF lv_release <> lr_db_serv_inst->hec_row_selectable.
                  lr_db_serv_inst->hec_row_selectable = lv_release.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Modify DB server instance
                "-----------------------------------
                IF lv_data_changed = abap_true.
                  io_modify->update( iv_node = is_ctx-node_key
                                     iv_key  = lr_db_serv_inst->key
                                     is_data = lr_db_serv_inst ).
                ENDIF.
              ENDIF. "  IF <fs_tier> IS ASSIGNED.

              UNASSIGN <fs_tier>.
              CLEAR: lv_release,
                     lv_data_changed.
            ENDLOOP.
        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_db_server_pc_cr.

    DATA: lt_db_serv_perf_cat         TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_serv_perf_cat_pernode TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_serv_perf_cat_before  TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_node                  TYPE /hec1/t_data_db_node_ct,
          lt_db_server                TYPE /hec1/t_data_db_serv_ct,
          lt_instance_db              TYPE /hec1/t_data_db_inst_ct,
          lt_db_storage_qty           TYPE /hec1/t_data_db_storage_qty_ct,
          lt_node_key                 TYPE /bobf/t_frw_key,
          lt_phase                    TYPE /hec1/t_data_phase_ct,
          lt_act_param                TYPE /hec1/t_act_create_db_qty,
          lt_act_param_server         TYPE /hec1/t_act_update_db_server,
          lt_act_param_node           TYPE /hec1/t_act_update_db_node,
          lt_act_param_storage        TYPE /bobf/t_frw_key,
          lt_act_param_succ           TYPE /hec1/t_act_set_success_predec,
          lt_act_param_storage_qty    TYPE /hec1/t_act_update_db_strg_qty,
          lt_act_param_phasing        TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.


    "-----------------------------------
    " Get data
    "-----------------------------------
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_serv_perf_cat ).

    " Get DB node (parent)
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-to_parent
                                      IMPORTING et_data        = lt_db_node ).


    " Get landscape( APM GUID), delivery unit and data center
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server_perform_cat-create.

            " Get for each DB node
            " the DB server performance category
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_node
                                                        it_key         = VALUE #( FOR wa_node IN lt_db_node
                                                                                 ( key = wa_node-key )      )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                                              IMPORTING et_data        = lt_db_serv_perf_cat_pernode ).



            LOOP AT        lt_db_serv_perf_cat
            REFERENCE INTO DATA(lr_db_serv_perf_cat)
                WHERE hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master.

              "-----------------------------------
              " Set Value List Quantity
              " - Server Performance Category
              "-----------------------------------
              lr_db_serv_perf_cat->hec_srv_perf_cat_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server_perf_cat(
                                                                                     iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                     iv_inf_provider_guid   = lr_dlvy_unit->hec_inf_provider_guid
                                                                                     iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_db_serv_perf_cat->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL )
                                                                                     iv_server_type_guid    = lr_db_serv_perf_cat->hec_db_srv_type_guid
                                                                                     iv_is_app_server       = abap_false ) )
              THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
              ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " TODO this might need a more complex logic depending on the number of entries
              lr_db_serv_perf_cat->hec_delete_visible = abap_true.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_db_serv_perf_cat->hec_srv_perf_cat_guid IS NOT INITIAL AND
                                                                             lr_db_serv_perf_cat->hec_phase_guid        IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete      ).

              IF lv_inst_status <> lr_db_serv_perf_cat->hec_instance_status.
                lr_db_serv_perf_cat->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_db_node[ key = lr_db_serv_perf_cat->parent_key ] TO FIELD-SYMBOL(<fs_db_node>).
              IF <fs_db_node> IS ASSIGNED.
                IF <fs_db_node>-hec_db_srv_perf_cat_qty IS NOT INITIAL AND
                   <fs_db_node>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_db_serv_perf_cat->hec_row_selectable.
                lr_db_serv_perf_cat->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "------------------------------------------
              " Set CR related fields from the ROOT node
              "------------------------------------------
              DATA(lv_cr_data_changed) = /hec1/cl_config_helper=>SET_CR_RELATED_FIELDS(
                EXPORTING
                  is_ctx       = is_ctx
                  it_key       = it_key
                  io_read      = io_read
                  io_modify    = io_modify
                  iv_mod_type  = /hec1/if_config_constants=>gc_comp_mod_type-added
                  is_node_data = lr_db_serv_perf_cat
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              "-----------------------------------
              " Fill action table for create
              " DB server storage amount
              "-----------------------------------
              IF NOT lr_db_serv_perf_cat->hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-tenant.
                INSERT VALUE #( key                    = lr_db_serv_perf_cat->key
                                parent_key             = lr_db_serv_perf_cat->parent_key
                                hec_storage_amount_qty = lr_db_serv_perf_cat->hec_storage_qty ) INTO TABLE lt_act_param.
              ENDIF.

              "-----------------------------------
              " Fill action table for setting
              " DB server performance category
              " successor/predecessor
              "-----------------------------------
              DATA(lv_node_count) = REDUCE i( INIT x = 0
                                              FOR <l> IN lt_db_serv_perf_cat_pernode WHERE ( parent_key = lr_db_serv_perf_cat->parent_key )
                                              NEXT x = x + 1                                                                                  ).

              IF NOT line_exists( lt_act_param_succ[ key = lr_db_serv_perf_cat->parent_key ] ) AND lv_node_count > 1.
                TRY.
                    INSERT VALUE #( key                  = lr_db_serv_perf_cat->parent_key
                                    parent_key           = lt_db_node[ key = lr_db_serv_perf_cat->parent_key ]-parent_key
                                    hec_no_children_node = lv_node_count                                                  ) INTO TABLE lt_act_param_succ.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.

              "-----------------------------------
              " Modify DB server performance
              " category
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_serv_perf_cat->key
                                   is_data = lr_db_serv_perf_cat ).
              ENDIF.

              UNASSIGN <fs_db_node>.
              CLEAR: lv_inst_status,
                     lv_release,
                     lv_data_changed,
                     lv_node_count.

            ENDLOOP.

            "-----------------------------------
            " Set successor/predecessor action
            " to GENERAL
            "-----------------------------------
            IF lt_act_param_succ IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_set_success_predec( lt_act_param_succ ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key  = /hec1/if_configuration_c=>sc_node-db_node
                                             assoc_key = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat )
                  it_key          = VALUE #( FOR wa_act_succ IN lt_act_param_succ
                                            ( key = wa_act_succ-key )    )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-set_success_predec )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

            ENDIF.

            "-----------------------------------
            " Set create DB server storage
            " amount and create DB server
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_db_qty( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_qty )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                              ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_server )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                                                                        ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server_perform_cat-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_db_serv_perf_cat_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get DB Node
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-to_parent
                                              IMPORTING et_target_key  = DATA(lt_db_node_key)
                                                        et_data        = lt_db_node ).

            " Get instance DB
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_node
                                                        it_key         = lt_db_node_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_node-to_parent
                                              IMPORTING et_target_key  = DATA(lt_instance_db_key)
                                                        et_data        = lt_instance_db ).

            " Get DB Server
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_server
                                              IMPORTING et_data        = lt_db_server
                                                        et_target_key  = DATA(lt_db_server_key) ).

            " Get Storage Qty
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount
                                              IMPORTING et_data        = lt_db_storage_qty ).


            "-----------------------------------
            " Get server performance category
            "-----------------------------------
            DATA(lt_range_table) = VALUE /hec1/t_selection_range( FOR wa_spc IN lt_db_serv_perf_cat
                                                                ( option = /hec1/if_config_constants=>gc_range_option-eq
                                                                  sign   = /hec1/if_config_constants=>gc_range_sign-i
                                                                  low    = wa_spc-hec_srv_perf_cat_guid                   ) ).

            SELECT *
              FROM /hec1/i_dbservperfcatbasic
             WHERE hec_apm_guid = @lr_landscape->hec_apm_guid AND
                   hec_srv_perf_cat_guid IN @lt_range_table
              INTO TABLE @DATA(lt_serv_perf_cat).


            "-----------------------------------
            " Get server
            "-----------------------------------
            CLEAR lt_range_table.
            lt_range_table = VALUE /hec1/t_selection_range( FOR wa IN lt_db_serv_perf_cat
                                                           ( option = /hec1/if_config_constants=>gc_range_option-eq
                                                             sign   = /hec1/if_config_constants=>gc_range_sign-i
                                                             low    = wa-hec_srv_perf_cat_guid                   ) ).

            SELECT *                          "#EC CI_ALL_FIELDS_NEEDED
              FROM /hec1/i_serverbasic
             WHERE hec_apm_guid = @lr_landscape->hec_apm_guid AND
                   hec_srv_perf_cat_guid   IN @lt_range_table
              INTO TABLE @DATA(lt_server_data).



            LOOP AT lt_db_serv_perf_cat REFERENCE INTO lr_db_serv_perf_cat.
              ASSIGN lt_db_serv_perf_cat_before[ key = lr_db_serv_perf_cat->key ] TO FIELD-SYMBOL(<fs_db_serv_perf_cat_before>).

              IF <fs_db_serv_perf_cat_before> IS ASSIGNED.
                TRY.
                    DATA(ls_instance_db) = lt_instance_db[ key = lt_db_node[ key = lr_db_serv_perf_cat->parent_key ]-parent_key ].
                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.

                "-----------------------------------
                " DB server performance category
                " has changed
                "-----------------------------------
                IF lr_db_serv_perf_cat->hec_srv_perf_cat_guid IS NOT INITIAL                                             AND
                   lr_db_serv_perf_cat->hec_srv_perf_cat_guid <> <fs_db_serv_perf_cat_before>-hec_srv_perf_cat_guid.

                  TRY.
                      DATA(ls_serv_perf_cat) = lt_serv_perf_cat[ hec_srv_perf_cat_guid = lr_db_serv_perf_cat->hec_srv_perf_cat_guid ].

                      IF ls_instance_db-hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-container.

                        lr_db_serv_perf_cat->hec_srv_perf_cat_descr        = ls_serv_perf_cat-hec_srv_perf_cat_descr.
                        lr_db_serv_perf_cat->hec_db_intended_srv_ram_class = ls_serv_perf_cat-hec_srv_ram_class.
                        lr_db_serv_perf_cat->hec_tree_descr                = ls_serv_perf_cat-hec_srv_perf_cat_descr. "#EC CI_FLDEXT_OK[2215424]

                      ELSE.
                        lr_db_serv_perf_cat->hec_srv_perf_cat_descr = ls_serv_perf_cat-hec_srv_perf_cat_descr.
                        lr_db_serv_perf_cat->hec_srv_ram_class      = ls_serv_perf_cat-hec_srv_ram_class.
                        lr_db_serv_perf_cat->hec_srv_cpu_class      = ls_serv_perf_cat-hec_srv_cpu_class.
                        lr_db_serv_perf_cat->hec_tree_descr         = ls_serv_perf_cat-hec_srv_perf_cat_descr. "#EC CI_FLDEXT_OK[2215424]
                      ENDIF.

                      lv_data_changed = abap_true.

                      " Set Value List Quantity
                      lr_db_serv_perf_cat->hec_srv_perf_cat_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server_perf_cat(
                                                                                             iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                             iv_inf_provider_guid   = lr_dlvy_unit->hec_inf_provider_guid
                                                                                             iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_db_serv_perf_cat->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL )
                                                                                             iv_server_type_guid    = lr_db_serv_perf_cat->hec_db_srv_type_guid
                                                                                             iv_is_app_server       = abap_false ) )
                                                                           THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                           ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.


                  TRY.
                      DATA(lv_datacenter_guid) = lt_datacenter[ hec_node_datacenter = lr_db_serv_perf_cat->hec_tier_datacenter_guid ]-hec_datacenter_guid.

                      DATA(lt_server) = /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server( iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                                                   iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                                                                   iv_sec_datacenter_guid = lv_datacenter_guid
                                                                                                                   iv_srv_perf_cat_guid   = lr_db_serv_perf_cat->hec_srv_perf_cat_guid ).
                      "-----------------------------------
                      " Fill action table for Update
                      " DB server
                      "-----------------------------------
                      IF lines( lt_server ) = 1.
                        INSERT VALUE #( key                 = lt_db_server[ parent_key = lr_db_serv_perf_cat->key ]-key
                                        parent_key          = lr_db_serv_perf_cat->key
                                        hec_ip_server_guid  = lt_server[ 1 ]-value
                                        do_update_db_server = abap_true                                                 ) INTO TABLE lt_act_param_server.
                      ENDIF.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  CLEAR: lv_datacenter_guid,
                         lt_server.

                  "-----------------------------------
                  " Fill action table for update
                  " DB server storage amount
                  "-----------------------------------
                  INSERT VALUE #( parent_key = lr_db_serv_perf_cat->key ) INTO TABLE lt_act_param_storage_qty.
                ENDIF. " IF ls_db_server_perf_cat-hec_srv_perf_cat_guid IS NOT INITIAL AND ...


                "-----------------------------------
                " DB server storage is added
                "-----------------------------------
                IF lr_db_serv_perf_cat->hec_storage_qty > <fs_db_serv_perf_cat_before>-hec_storage_qty.
                  "-----------------------------------
                  " Fill action table for create
                  " DB server storage amount
                  "-----------------------------------
                  INSERT VALUE #( key                    = lr_db_serv_perf_cat->key
                                  parent_key             = lr_db_serv_perf_cat->parent_key
                                  hec_storage_amount_qty = lr_db_serv_perf_cat->hec_storage_qty - <fs_db_serv_perf_cat_before>-hec_storage_qty ) INTO TABLE lt_act_param.

                  "-----------------------------------
                  " Fill action table for create
                  " DB server storage
                  "-----------------------------------
                  TRY.
                      " DB Storage is added without any parameters necessary
                      INSERT VALUE #( key = lt_db_server[ parent_key = lr_db_serv_perf_cat->key ]-key ) INTO TABLE lt_act_param_storage.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  " Success message
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_storage_added
                                                                 iv_severity = /bobf/cm_frw=>co_severity_success
                                                                 iv_attr1    = CONV #( lr_db_serv_perf_cat->hec_storage_qty -
                                                                               <fs_db_serv_perf_cat_before>-hec_storage_qty )
                                                       CHANGING  co_message  = eo_message ).

                  " Set flag for deleting subnodes of standby/worker node
                  IF ( lr_db_serv_perf_cat->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                       lr_db_serv_perf_cat->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi   )   AND
                       lr_db_serv_perf_cat->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                       lr_db_serv_perf_cat->hec_db_node_default          = abap_true.
                    lv_data_changed         = abap_true.
                    DATA(lv_delete_subnode) = abap_true.
                  ENDIF.

                ELSEIF lr_db_serv_perf_cat->hec_storage_qty < <fs_db_serv_perf_cat_before>-hec_storage_qty                                                       AND
                       lr_db_serv_perf_cat->hec_storage_qty < lines( VALUE /hec1/t_data_db_storage_qty_ct( FOR db_storage_qty IN lt_db_storage_qty
                                                                                                           WHERE ( parent_key = lr_db_serv_perf_cat->key )
                                                                                                            ( db_storage_qty )                             ) ).

                  DATA(lv_attr_name) = /hec1/if_configuration_c=>sc_node_attribute-db_server_perform_cat-hec_storage_qty.

                  " Error
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                 is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                               key      = lr_db_serv_perf_cat->key
                                                                                               attributes = VALUE #( ( lv_attr_name ) ) )
                                                       CHANGING  co_message         = eo_message ).

                  " Set node number to value before update
                  lr_db_serv_perf_cat->hec_storage_qty = <fs_db_serv_perf_cat_before>-hec_storage_qty.
                  lv_data_changed = abap_true.
                ENDIF. " IF ls_db_server_perf_cat-hec_storage_qty > ls_db_server_perf_cat_old-hec_storage_qty.

                "-----------------------------------
                " Phase has changed
                "-----------------------------------
                IF lr_db_serv_perf_cat->hec_phase_guid <> <fs_db_serv_perf_cat_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_db_serv_perf_cat->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                     lr_db_serv_perf_cat->hec_db_node_default          = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_db_serv_perf_cat->key
                                    hec_phase_guid_new = lr_db_serv_perf_cat->hec_phase_guid
                                    hec_phase_guid_old = <fs_db_serv_perf_cat_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_db_serv_perf_cat->hec_phase_changed = abap_true.
                  lv_data_changed                        = abap_true.

                  " Set flag for deleting subnodes of standby/worker node
                  IF ( lr_db_serv_perf_cat->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                       lr_db_serv_perf_cat->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi   )   AND
                       lr_db_serv_perf_cat->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                       lr_db_serv_perf_cat->hec_db_node_default          = abap_true.
                    lv_delete_subnode = abap_true.
                  ENDIF.
                ENDIF. "phasing changed
              ENDIF. " IF <fs_db_serv_perf_cat_before> IS ASSIGNED.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_db_serv_perf_cat->hec_srv_perf_cat_guid IS NOT INITIAL AND
                                                                       lr_db_serv_perf_cat->hec_phase_guid            IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete          ).

              IF lv_inst_status <> lr_db_serv_perf_cat->hec_instance_status.
                lr_db_serv_perf_cat->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for delete
              " subnodes of DB standby/worker node
              " or relase standby/worker node
              "-----------------------------------
              IF ( lr_db_serv_perf_cat->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                   lr_db_serv_perf_cat->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi   )   AND
                   lr_db_serv_perf_cat->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                   lr_db_serv_perf_cat->hec_db_node_default          = abap_true                                               AND
                   lv_data_changed                                   = abap_true.

                IF NOT line_exists( lt_act_param_node[ key = lr_db_serv_perf_cat->parent_key ] ).
                  TRY.
                      INSERT VALUE #( key               = lr_db_serv_perf_cat->parent_key
                                      parent_key        = lt_db_node[ key = lr_db_serv_perf_cat->parent_key ]-parent_key
                                      do_release_node   = COND #( WHEN lr_db_serv_perf_cat->hec_instance_status         = /hec1/if_config_constants=>gc_instance_status-complete   AND
                                                                       <fs_db_serv_perf_cat_before>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                                  THEN abap_true
                                                                  ELSE abap_false                                                  )
                                      do_delete_subnode = COND #( WHEN lr_db_serv_perf_cat->hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete OR
                                                                       lv_delete_subnode                        = abap_true
                                                                  THEN abap_true
                                                                  ELSE abap_false                                                                                     ) ) INTO TABLE lt_act_param_node.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                ENDIF.
              ENDIF. " IF ( lr_db_serv_perf_cat->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR...


              "-----------------------------------
              " Modify DB server performance
              " category
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_serv_perf_cat->key
                                   is_data = lr_db_serv_perf_cat ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_attr_name,
                     lv_delete_subnode.

              UNASSIGN <fs_db_serv_perf_cat_before>.
            ENDLOOP.


            "-----------------------------------
            " Set update Phasing action to
            " general
            "-----------------------------------
            IF lt_act_param_phasing IS NOT INITIAL.
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.

            "-----------------------------------
            " Set create DB server storage
            " amount and DB server storage
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_db_qty( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_qty )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                              ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                              node_key = /hec1/if_configuration_c=>sc_node-db_server )
                  it_key          = VALUE #( FOR wa_act_serv IN lt_act_param_storage
                                            ( key = wa_act_serv-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_storage )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                                                                        ).

            ENDIF.

            "-----------------------------------
            " Set Update DB Storage Amount
            " to general
            "-----------------------------------
            IF lt_act_param_storage_qty IS NOT INITIAL.

              me->mr_act_param_db_storage_amount = NEW /hec1/t_act_update_db_strg_qty( FOR strg_qty IN lt_act_param_storage_qty
                ( parent_key = strg_qty-parent_key
                do_update_storage = abap_true ) ).

              " Update DB storage amount (in general)
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR strg_qty IN lt_act_param_storage_qty   "pass the server performance category key
                                           ( key = strg_qty-parent_key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_storage_amount )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_db_storage_amount ).
            ENDIF.

            "-----------------------------------
            " Set Update DB server action
            " to general
            "-----------------------------------
            IF lt_act_param_server IS NOT INITIAL.
              CLEAR me->mr_act_param1.
              me->mr_act_param1 = NEW /hec1/t_act_update_db_server( lt_act_param_server ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act_server IN lt_act_param_server
                                            ( key = wa_act_server-parent_key )        )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_server )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param1                                                                                                              ).
            ENDIF.


            "-----------------------------------
            " Set update DB node action to
            " general
            "-----------------------------------
            IF lt_act_param_node IS NOT INITIAL.
              CLEAR me->mr_act_param_db_node.
              me->mr_act_param_db_node = NEW /hec1/t_act_update_db_node( lt_act_param_node ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-db_node )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param_node
                                              ( key = wa_act_node-key )     )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_db_node                                                                                                       ).
            ENDIF.


            " ***************************************************************************
            " Update mode after DB node update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_server_perform_cat-update_after_node.

            LOOP AT lt_db_serv_perf_cat REFERENCE INTO lr_db_serv_perf_cat.
              ASSIGN lt_db_node[ key = lr_db_serv_perf_cat->parent_key ] TO <fs_db_node>.

              IF <fs_db_node> IS ASSIGNED.
                "-----------------------------------
                " Release instance for selection
                "-----------------------------------
                IF <fs_db_node>-hec_db_srv_perf_cat_qty IS NOT INITIAL AND
                   <fs_db_node>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.


                IF lv_release <> lr_db_serv_perf_cat->hec_row_selectable.
                  lr_db_serv_perf_cat->hec_row_selectable = lv_release.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Update DB server cluster type
                "-----------------------------------
                IF lr_db_serv_perf_cat->hec_db_cluster_type_value <> <fs_db_node>-hec_db_cluster_type_value.
                  lr_db_serv_perf_cat->hec_db_cluster_type_value = <fs_db_node>-hec_db_cluster_type_value.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Modify DB server performance
                " category
                "-----------------------------------
                IF lv_data_changed = abap_true.
                  io_modify->update( iv_node = is_ctx-node_key
                                     iv_key  = lr_db_serv_perf_cat->key
                                     is_data = lr_db_serv_perf_cat ).
                ENDIF.
              ENDIF. " IF <fs_db_node> IS ASSIGNED.

              UNASSIGN <fs_db_node>.
              CLEAR: lv_data_changed,
                     lv_release.

            ENDLOOP. " LOOP AT lt_db_serv_perf_cat...
        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_db_storage_amount_cr.

    DATA: lt_db_storage_qty        TYPE /hec1/t_data_db_storage_qty_ct,
          lt_db_storage_qty_perspc TYPE /hec1/t_data_db_storage_qty_ct,
          lt_db_storage_qty_before TYPE /hec1/t_data_db_storage_qty_ct,
          lr_db_storage_qty        TYPE REF TO /hec1/s_data_db_storage_qty_cs,
          lt_db_node               TYPE /hec1/t_data_db_node_ct,
          lt_db_serv_perf_cat      TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_server             TYPE /hec1/t_data_db_serv_ct,
          lt_db_storage            TYPE /hec1/t_data_db_storage_ct,
          lt_phase                 TYPE /hec1/t_data_phase_ct,
          lt_act_param_node        TYPE /hec1/t_act_update_db_node,
          lt_act_param_storage     TYPE /bobf/t_frw_key,
          lt_act_param_succ        TYPE /hec1/t_act_set_success_predec,
          lt_act_param_phasing     TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    "-----------------------------------
    " Get data
    "-----------------------------------
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_storage_qty ).

    " Get DB server performance category (parent)
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_storage_amount-to_parent
                                      IMPORTING et_data        = lt_db_serv_perf_cat ).

    " Get landscape( APM GUID), delivery unit and data center
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage_amount-create.

            " Get for each DB server performance category
            " the DB storage amount
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                        it_key         = VALUE #( FOR wa_spc IN lt_db_serv_perf_cat
                                                                                 ( key = wa_spc-key )               )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount
                                              IMPORTING et_data        = lt_db_storage_qty_perspc ).


            LOOP AT lt_db_storage_qty REFERENCE INTO lr_db_storage_qty.

              lr_db_storage_qty->hec_delete_visible = abap_true.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_db_storage_qty->hec_phase_guid IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_db_storage_qty->hec_instance_status.
                lr_db_storage_qty->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.

                " If standby node exist
                IF ( lr_db_storage_qty->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                     lr_db_storage_qty->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi   )  AND
                     lr_db_storage_qty->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                     lr_db_storage_qty->hec_db_node_default          = abap_true                                               AND
                     lr_db_storage_qty->hec_instance_status          = /hec1/if_config_constants=>gc_instance_status-complete.

                  io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                              it_key         = VALUE #( ( key = lr_db_storage_qty->key ) )
                                                              iv_fill_data   = abap_false
                                                              iv_association = /hec1/if_configuration_c=>sc_association-db_storage_amount-to_def_master_node
                                                    IMPORTING et_target_key  = DATA(lt_key) ).

                  IF NOT line_exists( lt_act_param_node[ key = lt_key[ 1 ]-key ] ).
                    TRY.
                        INSERT VALUE #( key             = lt_key[ 1 ]-key
                                        do_release_node = abap_true       ) INTO TABLE lt_act_param_node.
                      CATCH cx_sy_itab_line_not_found.
                    ENDTRY.
                  ENDIF.
                ENDIF.
              ENDIF. " IF lv_inst_status <> lr_db_storage_qty->hec_instance_status.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_db_serv_perf_cat[ key = lr_db_storage_qty->parent_key ] TO FIELD-SYMBOL(<fs_db_serv_perf_cat>).
              IF <fs_db_serv_perf_cat> IS ASSIGNED.
                IF <fs_db_serv_perf_cat>-hec_srv_perf_cat_guid IS NOT INITIAL AND
                   <fs_db_serv_perf_cat>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_db_storage_qty->hec_row_selectable.
                lr_db_storage_qty->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "------------------------------------------
              " Set CR related fields from the ROOT node
              "------------------------------------------
              DATA(lv_cr_data_changed) = /hec1/cl_config_helper=>SET_CR_RELATED_FIELDS(
                EXPORTING
                  is_ctx       = is_ctx
                  it_key       = it_key
                  io_read      = io_read
                  io_modify    = io_modify
                  iv_mod_type  = /hec1/if_config_constants=>gc_comp_mod_type-added
                  is_node_data = lr_db_storage_qty
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              "-----------------------------------
              " Fill action table for setting
              " DB server storage amount
              " successor/predecessor
              "-----------------------------------
              DATA(lv_node_count) = REDUCE i( INIT x = 0
                                              FOR <l> IN lt_db_storage_qty_perspc WHERE ( parent_key = lr_db_storage_qty->parent_key )
                                              NEXT x = x + 1                                                                              ).

              IF NOT line_exists( lt_act_param_succ[ key = lr_db_storage_qty->parent_key ] ) AND lv_node_count > 1.
                TRY.
                    INSERT VALUE #( key         = lr_db_storage_qty->parent_key
                                    parent_key  = lt_db_serv_perf_cat[ key = lr_db_storage_qty->parent_key ]-parent_key
                                    hec_no_children_node = lv_node_count                                                         ) INTO TABLE lt_act_param_succ.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.


              "-----------------------------------
              " Modify DB storage amount
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_storage_qty->key
                                   is_data = lr_db_storage_qty ).
              ENDIF.

              UNASSIGN <fs_db_serv_perf_cat>.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release,
                     lv_node_count.

            ENDLOOP.


            "-----------------------------------
            " Set update DB node action to
            " general
            "-----------------------------------
            IF lt_act_param_node IS NOT INITIAL.
              CLEAR me->mr_act_param_db_node.
              me->mr_act_param_db_node = NEW /hec1/t_act_update_db_node( lt_act_param_node ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-db_node )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param_node
                                              ( key = wa_act_node-key )     )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_db_node                                                                                                       ).
            ENDIF.


            "-----------------------------------
            " Set successor/predecessor action
            " to GENERAL
            "-----------------------------------
            IF lt_act_param_succ IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_set_success_predec( lt_act_param_succ ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key  = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                             assoc_key = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount )
                  it_key          = VALUE #( FOR wa_act_succ IN lt_act_param_succ
                                            ( key = wa_act_succ-key )    )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-set_success_predec )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage_amount-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_db_storage_qty_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_storage_amount-to_parent
                                              IMPORTING et_target_key  = DATA(lt_db_serv_pc_key) ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                        it_key         = lt_db_serv_pc_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_server
                                              IMPORTING et_target_key  = DATA(lt_db_serv_key)
                                                        et_key_link    = DATA(lt_perf_cat_to_serv_link) ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server
                                                        it_key         = lt_db_serv_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server-db_storage
                                              IMPORTING et_target_key  = DATA(lt_db_storage_key)
                                                        et_key_link    = DATA(lt_serv_to_storage_link) ).


            LOOP AT lt_db_storage_qty REFERENCE INTO lr_db_storage_qty.

              ASSIGN lt_db_storage_qty_before[ key = lr_db_storage_qty->key ] TO FIELD-SYMBOL(<fs_db_storage_qty_before>).
              IF <fs_db_storage_qty_before> IS ASSIGNED.
                "-----------------------------------
                " Physical, virtual or additional storage
                " has changed
                "-----------------------------------
                IF lr_db_storage_qty->hec_dsq_main_stor_qty_physical <> <fs_db_storage_qty_before>-hec_dsq_main_stor_qty_physical OR
                   lr_db_storage_qty->hec_dsq_main_stor_qty_virtual  <> <fs_db_storage_qty_before>-hec_dsq_main_stor_qty_virtual  OR
                   lr_db_storage_qty->hec_dsq_additional_stor_qty    <> <fs_db_storage_qty_before>-hec_dsq_additional_stor_qty OR
                   lr_db_storage_qty->hec_successor_guid             <> <fs_db_storage_qty_before>-hec_successor_guid OR
                   lr_db_storage_qty->hec_predecessor_guid           <> <fs_db_storage_qty_before>-hec_predecessor_guid.

                  lr_db_storage_qty->hec_tree_descr = |{ lr_db_storage_qty->hec_dsq_main_stor_qty_virtual } + { lr_db_storage_qty->hec_dsq_additional_stor_qty } [GiB] |.
                  lv_data_changed = abap_true.

                  " Storage needs to be adjusted
                  LOOP AT lt_serv_to_storage_link REFERENCE INTO DATA(lr_serv_to_storage_link)
                    WHERE source_key = lt_perf_cat_to_serv_link[ source_key = lr_db_storage_qty->parent_key ]-target_key.

                    INSERT VALUE #( key = lr_serv_to_storage_link->target_key ) INTO TABLE lt_act_param_storage.

                  ENDLOOP.

                  " Set flag for deleting subnodes of standby/worker node
                  IF ( lr_db_storage_qty->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                       lr_db_storage_qty->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi   )   AND
                       lr_db_storage_qty->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                       lr_db_storage_qty->hec_db_node_default          = abap_true.
                    DATA(lv_delete_subnode) = abap_true.
                  ENDIF.
                ENDIF. " IF ls_db_storage_qty-hec_dsq_main_stor_qty_physical <> ls_db_storage_qty_old-hec_dsq_main_stor_qty_physical OR

                "-----------------------------------
                " Phase has changed - update phase
                " and inherit phase assignment
                "-----------------------------------
                IF lr_db_storage_qty->hec_phase_guid NE <fs_db_storage_qty_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_db_storage_qty->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                     lr_db_storage_qty->hec_db_node_default          = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_db_storage_qty->key
                                    hec_phase_guid_new = lr_db_storage_qty->hec_phase_guid
                                    hec_phase_guid_old = <fs_db_storage_qty_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_db_storage_qty->hec_phase_changed = abap_true.
                  lv_data_changed                      = abap_true.

                  " Set flag for deleting subnodes of standby/worker node
                  IF ( lr_db_storage_qty->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                       lr_db_storage_qty->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi   )   AND
                       lr_db_storage_qty->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                       lr_db_storage_qty->hec_db_node_default          = abap_true.
                    lv_delete_subnode = abap_true.
                  ENDIF.
                ENDIF. " IF lr_db_storage_qty->hec_phase_guid NE <fs_db_storage_qty_before>-hec_phase_guid.
              ENDIF. " IF <fs_db_storage_qty_before> IS ASSIGNED.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_db_storage_qty->hec_phase_guid IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_db_storage_qty->hec_instance_status.
                lr_db_storage_qty->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for delete
              " subnodes of DB standby/worker node
              " or relase standby/worker node
              "-----------------------------------
              IF ( lr_db_storage_qty->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR
                   lr_db_storage_qty->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-multi   )   AND
                   lr_db_storage_qty->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                   lr_db_storage_qty->hec_db_node_default          = abap_true                                               AND
                   lv_data_changed                                 = abap_true.

                " Only one master node per storage amount can exist
                io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                            it_key         = VALUE #( ( key = lr_db_storage_qty->key ) )
                                                            iv_fill_data   = abap_false
                                                            iv_association = /hec1/if_configuration_c=>sc_association-db_storage_amount-to_def_master_node
                                                  IMPORTING et_target_key  = lt_key ).

                IF NOT line_exists( lt_act_param_node[ key = lt_key[ 1 ]-key ] ).
                  TRY.
                      INSERT VALUE #( key               = lt_key[ 1 ]-key
                                      parent_key        = space
                                      do_release_node   = COND #( WHEN lr_db_storage_qty->hec_instance_status         = /hec1/if_config_constants=>gc_instance_status-complete   AND
                                                                       <fs_db_storage_qty_before>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                                  THEN abap_true
                                                                  ELSE abap_false                                                  )
                                      do_delete_subnode = COND #( WHEN lr_db_storage_qty->hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete OR
                                                                       lv_delete_subnode                      = abap_true
                                                                  THEN abap_true
                                                                  ELSE abap_false                                                                                     ) ) INTO TABLE lt_act_param_node.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                ENDIF.
              ENDIF. " IF ( lr_db_serv_perf_cat->hec_db_cluster_type_value    = /hec1/if_config_constants=>gc_db_clust_node-ha   OR...


              "-----------------------------------
              " Modify DB storage amount
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_storage_qty->key
                                   is_data = lr_db_storage_qty ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_delete_subnode,
                     lt_key.

              UNASSIGN <fs_db_storage_qty_before>.
            ENDLOOP.

            "-----------------------------------
            " Set update DB Storage action to
            " general
            "-----------------------------------
            IF lt_act_param_storage IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-db_storage )
                  it_key          = lt_act_param_storage
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_storage )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation ).                                                                                      .
            ENDIF.

            "-----------------------------------
            " Update Phasing
            "-----------------------------------
            IF lt_act_param_phasing IS NOT INITIAL.
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.


            "-----------------------------------
            " Set update DB node action to
            " general
            "-----------------------------------
            IF lt_act_param_node IS NOT INITIAL.
              CLEAR me->mr_act_param_db_node.
              me->mr_act_param_db_node = NEW /hec1/t_act_update_db_node( lt_act_param_node ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-db_node )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param_node
                                              ( key = wa_act_node-key )     )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_db_node                                                                                                       ).
            ENDIF.


            " ***************************************************************************
            " Update mode after DB server
            " performance category update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage_amount-update_after_serv_perf_cat.

            LOOP AT lt_db_storage_qty REFERENCE INTO lr_db_storage_qty.
              ASSIGN lt_db_serv_perf_cat[ key = lr_db_storage_qty->parent_key ] TO <fs_db_serv_perf_cat>.

              IF <fs_db_serv_perf_cat> IS ASSIGNED.
                "-----------------------------------
                " Release instance for selection
                "-----------------------------------
                IF <fs_db_serv_perf_cat>-hec_srv_perf_cat_guid IS NOT INITIAL AND
                   <fs_db_serv_perf_cat>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.

                IF lv_release <> lr_db_storage_qty->hec_row_selectable.
                  lr_db_storage_qty->hec_row_selectable = lv_release.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Update DB server cluster type
                "-----------------------------------
                IF lr_db_storage_qty->hec_db_cluster_type_value <> <fs_db_serv_perf_cat>-hec_db_cluster_type_value.
                  lr_db_storage_qty->hec_db_cluster_type_value = <fs_db_serv_perf_cat>-hec_db_cluster_type_value.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Modify DB storage amount
                "-----------------------------------
                IF lv_data_changed = abap_true.
                  io_modify->update( iv_node = is_ctx-node_key
                                     iv_key  = lr_db_storage_qty->key
                                     is_data = lr_db_storage_qty ).
                ENDIF.
              ENDIF. " IF <fs_db_serv_perf_cat> IS ASSIGNED.

              UNASSIGN <fs_db_serv_perf_cat>.
              CLEAR: lv_release,
                     lv_data_changed.

            ENDLOOP. " LOOP AT lt_db_storage_qty
        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD determine_db_storage_backup_cr.

    DATA: lt_db_backup            TYPE /hec1/t_data_db_backup_ct,
          lt_db_backup_perstorage TYPE /hec1/t_data_db_backup_ct,
          lt_db_backup_before     TYPE /hec1/t_data_db_backup_ct,
          lt_db_storage           TYPE /hec1/t_data_db_storage_ct,
          lt_phase                TYPE /hec1/t_data_phase_ct,
          lt_act_param_succ       TYPE /hec1/t_act_set_success_predec,
          lt_act_param_phasing    TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_backup ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage_backup-create.

            " Get DB server storage (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_storage_backup-to_parent
                                              IMPORTING et_data        = lt_db_storage ).


            " Get for each DB storage the DB backup
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_storage
                                                        it_key         = VALUE #( FOR wa_node IN lt_db_storage
                                                                                 ( key = wa_node-key )         )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_storage-db_storage_backup
                                              IMPORTING et_data        = lt_db_backup_perstorage ).


            LOOP AT lt_db_backup REFERENCE INTO DATA(lr_db_backup).
              lr_db_backup->hec_delete_visible = abap_true.

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              lr_db_backup->hec_backup_class_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_backup(
                                                                              iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                              iv_tier_category_value = lr_db_backup->hec_tier_cat_value
                                                                              iv_srv_type_guid       = lr_db_backup->hec_db_srv_type_guid
                                                                              iv_is_app_backup       = abap_false ) )
                                                        THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                        ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_db_backup->hec_backup_class_guid IS NOT INITIAL AND
                                                                             lr_db_backup->hec_backup_size       IS NOT INITIAL AND
                                                                             lr_db_backup->hec_phase_guid        IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_db_backup->hec_instance_status.
                lr_db_backup->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.


              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_db_storage[ key = lr_db_backup->parent_key ] TO FIELD-SYMBOL(<fs_db_storage>).
              IF <fs_db_storage> IS ASSIGNED.
                IF <fs_db_storage>-hec_ip_storage_guid IS NOT INITIAL AND
                   <fs_db_storage>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_db_backup->hec_row_selectable.
                lr_db_backup->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "------------------------------------------
              " Set CR related fields from the ROOT node
              "------------------------------------------
              DATA(lv_cr_data_changed) = /hec1/cl_config_helper=>SET_CR_RELATED_FIELDS(
                EXPORTING
                  is_ctx       = is_ctx
                  it_key       = it_key
                  io_read      = io_read
                  io_modify    = io_modify
                  iv_mod_type  = /hec1/if_config_constants=>gc_comp_mod_type-added
                  is_node_data = lr_db_backup
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              "-----------------------------------
              " Fill action table for setting
              " DB server storage backup
              " successor/predecessor
              "-----------------------------------
              DATA(lv_node_count) = REDUCE i( INIT x = 0
                                              FOR <l> IN lt_db_backup_perstorage WHERE ( parent_key = lr_db_backup->parent_key )
                                              NEXT x = x + 1                                                                       ).

              IF NOT line_exists( lt_act_param_succ[ key = lr_db_backup->parent_key ] ) AND lv_node_count > 1.
                TRY.
                    INSERT VALUE #( key                  = lr_db_backup->parent_key
                                    parent_key           = lt_db_storage[ key = lr_db_backup->parent_key ]-parent_key
                                    hec_no_children_node = lv_node_count                                              ) INTO TABLE lt_act_param_succ.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.


              "-----------------------------------
              " Modify DB backup
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_backup->key
                                   is_data = lr_db_backup ).
              ENDIF.


              UNASSIGN <fs_db_storage>.
              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release,
                     lv_node_count.
            ENDLOOP.


            "-----------------------------------
            " Set successor/predecessor action
            " to GENERAL
            "-----------------------------------
            IF lt_act_param_succ IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_set_success_predec( lt_act_param_succ ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key  = /hec1/if_configuration_c=>sc_node-db_storage
                                             assoc_key = /hec1/if_configuration_c=>sc_association-db_storage-db_storage_backup )
                  it_key          = VALUE #( FOR wa_act_succ IN lt_act_param_succ
                                            ( key = wa_act_succ-key )    )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-set_success_predec )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage_backup-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                                         iv_fill_data    = abap_true
                               IMPORTING et_data         = lt_db_backup_before ).


            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get DB storage
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_storage_backup-to_parent
                                              IMPORTING et_target_key  = DATA(lt_db_storage_key)
                                                        et_data        = lt_db_storage ).


            LOOP AT lt_db_backup REFERENCE INTO lr_db_backup.
              ASSIGN lt_db_backup_before[ key = lr_db_backup->key ] TO FIELD-SYMBOL(<fs_db_backup_before>).

              IF <fs_db_backup_before> IS ASSIGNED.
                "-----------------------------------
                " Backup GUID has changed
                "-----------------------------------
                IF lr_db_backup->hec_backup_class_guid    IS NOT INITIAL                              AND
                  lr_db_backup->hec_backup_class_guid <> <fs_db_backup_before>-hec_backup_class_guid.

                  " Get backup class and backup class pricing
                  /hec1/cl_config_action_helper=>/hec1/if_bopf_action_helper~get_backup_class_and_price( EXPORTING is_ctx                  = CORRESPONDING #( is_ctx )
                                                                                                                   it_key                  = VALUE #( ( key = lr_db_backup->key ) )
                                                                                                                   iv_tier_category_value  = lr_db_backup->hec_tier_cat_value
                                                                                                                   iv_tier_datacenter_guid = lr_db_backup->hec_tier_datacenter_guid
                                                                                                                   iv_backup_class_guid    = lr_db_backup->hec_backup_class_guid
                                                                                                                   io_read                 = io_read
                                                                                                         IMPORTING es_backup_class         = DATA(ls_backup_class)
                                                                                                                   es_backup_pricing       = DATA(ls_backup_pricing) ).

                  lr_db_backup->price                      = CORRESPONDING #( ls_backup_pricing ).
                  lr_db_backup->hec_backup_class_guid      = ls_backup_class-hec_backup_class_guid.
                  lr_db_backup->hec_backup_class_descr     = ls_backup_class-hec_backup_class_descr.
                  lr_db_backup->hec_tree_descr             = ls_backup_class-hec_backup_class_descr. "#EC CI_FLDEXT_OK[2215424]
                  lr_db_backup->hec_backup_month_price_fee = lr_db_backup->hec_backup_size * lr_db_backup->hec_month_price_eur.

                  lv_data_changed                          = abap_true.

                  "-----------------------------------
                  " Set Value List Quantity
                  "-----------------------------------
                  lr_db_backup->hec_backup_class_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_backup(
                                                                                      iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                      iv_tier_category_value = lr_db_backup->hec_tier_cat_value
                                                                                      iv_srv_type_guid       = lr_db_backup->hec_db_srv_type_guid
                                                                                      iv_is_app_backup       = abap_false ) )
                                                                THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                ENDIF. " IF ls_db_backup-hec_backup_class_guid IS NOT INITIAL AND

                "-----------------------------------
                " Backup size has changed
                "-----------------------------------
                IF lr_db_backup->hec_backup_size IS NOT INITIAL AND
                   lr_db_backup->hec_backup_size <> <fs_db_backup_before>-hec_backup_size.
                  lr_db_backup->hec_backup_month_price_fee = lr_db_backup->hec_backup_size * lr_db_backup->hec_month_price_eur.
                  lv_data_changed = abap_true.

                ENDIF.

                "-----------------------------------
                " Phase has changed
                "-----------------------------------
                IF lr_db_backup->hec_phase_guid NE <fs_db_backup_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_db_backup->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                     lr_db_backup->hec_db_node_default          = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_db_backup->key
                                    hec_phase_guid_new = lr_db_backup->hec_phase_guid
                                    hec_phase_guid_old = <fs_db_backup_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_db_backup->hec_phase_changed = abap_true.
                  lv_data_changed                 = abap_true.

                ENDIF.
              ENDIF. "IF <fs_db_backup_before> IS ASSIGNED.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_db_backup->hec_backup_class_guid IS NOT INITIAL AND
                                                         lr_db_backup->hec_backup_size       IS NOT INITIAL AND
                                                         lr_db_backup->hec_phase_guid        IS NOT INITIAL
                                                    THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                    ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_db_backup->hec_instance_status.
                lr_db_backup->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify DB backup
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_backup->key
                                   is_data = lr_db_backup ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     ls_backup_class,
                     ls_backup_pricing.

              UNASSIGN <fs_db_backup_before>.
            ENDLOOP.

            "-----------------------------------
            " Update Phasing
            "-----------------------------------
            IF lt_act_param_phasing IS NOT INITIAL.
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.

            " ***************************************************************************
            " Update mode after storage update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage_backup-update_after_storage.

            " Get DB server storage (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_storage_backup-to_parent
                                              IMPORTING et_data        = lt_db_storage ).


            LOOP AT lt_db_backup REFERENCE INTO lr_db_backup.
              ASSIGN lt_db_storage[ key = lr_db_backup->parent_key ] TO <fs_db_storage>.

              IF <fs_db_storage> IS ASSIGNED.
                "-----------------------------------
                " Release instance for selection
                "-----------------------------------
                IF <fs_db_storage>-hec_ip_storage_guid IS NOT INITIAL AND
                   <fs_db_storage>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.

                IF lv_release <> lr_db_backup->hec_row_selectable.
                  lr_db_backup->hec_row_selectable = lv_release.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Update DB server cluster type
                "-----------------------------------
                IF lr_db_backup->hec_db_cluster_type_value <> <fs_db_storage>-hec_db_cluster_type_value.
                  lr_db_backup->hec_db_cluster_type_value = <fs_db_storage>-hec_db_cluster_type_value.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Modify DB storage backup
                "-----------------------------------
                IF lv_data_changed = abap_true.
                  io_modify->update( iv_node = is_ctx-node_key
                                     iv_key  = lr_db_backup->key
                                     is_data = lr_db_backup ).
                ENDIF.
              ENDIF. "  IF <fs_db_storage> IS ASSIGNED.

              UNASSIGN <fs_db_storage>.
              CLEAR: lv_release,
                     lv_data_changed.

            ENDLOOP.
        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_db_storage_cr.

    DATA: lt_db_server            TYPE /hec1/t_data_db_serv_ct,
          lt_db_storage           TYPE /hec1/t_data_db_storage_ct,
          lt_db_storage_perserver TYPE /hec1/t_data_db_storage_ct,
          lt_db_storage_before    TYPE /hec1/t_data_db_storage_ct,
          lt_db_storage_succ      TYPE /hec1/t_data_db_storage_ct,
          lt_db_node              TYPE /hec1/t_data_db_node_ct,
          lt_db_serv_perf_cat     TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_storage_qty       TYPE /hec1/t_data_db_storage_qty_ct,
          lt_db_backup            TYPE /hec1/t_data_db_backup_ct,
          lt_phase                TYPE /hec1/t_data_phase_ct,
          lt_act_param            TYPE /hec1/t_act_create_db_backup,
          lt_act_param_storage    TYPE /bobf/t_frw_key,
          lt_act_param_phasing    TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_storage ).

    " Get DB server (parent)
    " Get DB server (parent)
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_storage-to_parent
                                      IMPORTING et_data        = lt_db_server ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage-create.

            " Get for each DB server the DB storage
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server
                                                        it_key         = VALUE #( FOR wa_serv IN lt_db_server
                                                                                 ( key = wa_serv-key )                )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_server-db_storage
                                              IMPORTING et_data        = lt_db_storage_perserver ).

            LOOP AT        lt_db_storage
            REFERENCE INTO DATA(lr_db_storage)
                     WHERE hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master.

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              lr_db_storage->hec_storage_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_storage(
                                                                          iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                          iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                          iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_db_storage->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL ) ) )
                                                        THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                        ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              lr_db_storage->hec_delete_visible = abap_false.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_db_storage->hec_ip_storage_guid IS NOT INITIAL AND
                                                                             lr_db_storage->hec_phase_guid      IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_db_storage->hec_instance_status.
                lr_db_storage->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_db_server[ key = lr_db_storage->parent_key ] TO FIELD-SYMBOL(<fs_db_server>).
              IF <fs_db_server> IS ASSIGNED.
                IF <fs_db_server>-hec_ip_server_guid IS NOT INITIAL AND
                   <fs_db_server>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_db_storage->hec_row_selectable.
                lr_db_storage->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "------------------------------------------
              " Set CR related fields from the ROOT node
              "------------------------------------------
              DATA(lv_cr_data_changed) = /hec1/cl_config_helper=>SET_CR_RELATED_FIELDS(
                EXPORTING
                  is_ctx       = is_ctx
                  it_key       = it_key
                  io_read      = io_read
                  io_modify    = io_modify
                  iv_mod_type  = /hec1/if_config_constants=>gc_comp_mod_type-added
                  is_node_data = lr_db_storage
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              "-----------------------------------
              " Fill action table for create
              " DB server storage backup
              "-----------------------------------
              IF lr_db_storage->hec_backup_relev_value = '01'. " mandantory
                INSERT VALUE #( key            = lr_db_storage->key
                                parent_key     = lr_db_storage->parent_key
                                hec_backup_qty = lr_db_storage->hec_backup_qty ) INTO TABLE lt_act_param.
              ENDIF.

              "-----------------------------------
              " Fill action table for setting
              " App server storage
              " successor/predecessor
              "-----------------------------------
              DATA(lv_node_count) = REDUCE i( INIT x = 0
                                              FOR <l> IN lt_db_storage_perserver WHERE ( parent_key = lr_db_storage->parent_key )
                                              NEXT x = x + 1                                                                        ).

              IF NOT line_exists( lt_act_param_storage[ key = lr_db_storage->key ] ) AND lv_node_count > 1.
                TRY.
                    INSERT VALUE #( key = lr_db_storage->key ) INTO TABLE lt_act_param_storage.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.

              "-----------------------------------
              " Modify DB server storage
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_storage->key
                                   is_data = lr_db_storage ).
              ENDIF.

              UNASSIGN <fs_db_server>.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release,
                     lv_node_count.

            ENDLOOP.

            "-----------------------------------
            " Set create DB server storage
            " backup action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_db_backup( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_backup )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

            ENDIF.

            "-----------------------------------
            " Set update DB storage action
            " to GENERAL
            "-----------------------------------
            IF lt_act_param_storage IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-db_storage )
                  it_key          = lt_act_param_storage
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_db_storage )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                                                                          ).
            ENDIF.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_db_storage_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get Backup
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-db_storage-db_storage_backup
                                              IMPORTING et_data        = lt_db_backup ).


            LOOP AT lt_db_storage REFERENCE INTO lr_db_storage.

              ASSIGN lt_db_storage_before[ key = lr_db_storage->key ] TO FIELD-SYMBOL(<fs_db_storage_before>).
              IF <fs_db_storage_before> IS ASSIGNED.
                "-----------------------------------
                " DB storage has changed
                "-----------------------------------
                IF lr_db_storage->hec_ip_storage_guid IS INITIAL    OR ( lr_db_storage->hec_ip_storage_guid IS NOT INITIAL AND
                   lr_db_storage->hec_ip_storage_guid  <> <fs_db_storage_before>-hec_ip_storage_guid ).

                  ASSIGN lt_db_server[ key = lr_db_storage->parent_key ] TO <fs_db_server>.

                  IF <fs_db_server> IS ASSIGNED.
                    SELECT SINGLE *
                      FROM /hec1/i_storagelbbasic
                     WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid              AND
                           hec_sec_datacenter_guid = @<fs_db_server>-hec_sec_datacenter_guid  AND
                           hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid     AND
                           hec_ip_storage_guid     = @lr_db_storage->hec_ip_storage_guid
                      INTO @DATA(ls_storage).

                    SELECT SINGLE * FROM /hec1/c_cbp_lb "#EC CI_ALL_FIELDS_NEEDED
                       INTO @DATA(ls_pricing)
                      WHERE hec_price_lb = @ls_storage-hec_cb_pricing_lb_guid.

                    lr_db_storage->*                   = CORRESPONDING #( BASE ( lr_db_storage->* ) ls_pricing ).
                    lr_db_storage->hec_ip_storage_guid = ls_storage-hec_ip_storage_guid.
                    lr_db_storage->hec_storage_descr   = ls_storage-hec_storage_descr.
                    lr_db_storage->hec_month_price_fee = lr_db_storage->hec_storage_quantity * lr_db_storage->hec_month_price_eur.
                    lr_db_storage->hec_tree_descr      = ls_storage-hec_storage_descr. "#EC CI_FLDEXT_OK[2215424]

                    lv_data_changed                    = abap_true.

                    " Set Value List Quantity - DB Storage
                    lr_db_storage->hec_storage_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_storage(
                                                                                iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                                iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_db_storage->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL ) ) )
                                                              THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                              ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                  ENDIF. " <fs_db_server> is assigned
                ENDIF. " db storage changed

                "-----------------------------------
                " DB storage amount has changed
                "-----------------------------------
                IF lr_db_storage->hec_storage_quantity IS NOT INITIAL                                 AND
                   lr_db_storage->hec_storage_quantity <> <fs_db_storage_before>-hec_storage_quantity.
                  lr_db_storage->hec_month_price_fee = lr_db_storage->hec_storage_quantity * lr_db_storage->hec_month_price_eur.

                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Fill action table for create
                " DB server storage backup
                "-----------------------------------
                IF lr_db_storage->hec_backup_qty > <fs_db_storage_before>-hec_backup_qty.

                  INSERT VALUE #( key            = lr_db_storage->key
                                  parent_key     = lr_db_storage->parent_key
                                  hec_backup_qty = lr_db_storage->hec_backup_qty - <fs_db_storage_before>-hec_backup_qty ) INTO TABLE lt_act_param.

                  " Success message
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_backup_added
                                                                 iv_severity = /bobf/cm_frw=>co_severity_success
                                                                 iv_attr1    = CONV #( lr_db_storage->hec_backup_qty -
                                                                               <fs_db_storage_before>-hec_backup_qty )
                                                       CHANGING  co_message  = eo_message ).

                ELSEIF lr_db_storage->hec_backup_qty < <fs_db_storage_before>-hec_backup_qty
                   AND lr_db_storage->hec_backup_qty < lines( VALUE /hec1/t_data_db_backup_ct( FOR db_backup IN lt_db_backup
                                                                                                     WHERE ( parent_key = lr_db_storage->key )
                                                                                                     ( db_backup ) ) ).
                  DATA(lv_attr_name) = /hec1/if_configuration_c=>sc_node_attribute-db_storage-hec_backup_qty.

                  " Error message
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                 is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                               key      = lr_db_storage->key
                                                                                               attributes = VALUE #( ( lv_attr_name ) ) )
                                                       CHANGING  co_message         = eo_message ).

                  " Set node number to value before update
                  lr_db_storage->hec_backup_qty = <fs_db_storage_before>-hec_backup_qty.
                  lv_data_changed = abap_true.
                ENDIF. " IF lr_db_storage->hec_dst_backup_qty > <fs_db_storage_before>-hec_dst_backup_qty.

                "-----------------------------------
                " Phase has changed - update phase and inherit phase assignment
                "-----------------------------------
                IF lr_db_storage->hec_phase_guid NE <fs_db_storage_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_db_storage->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                     lr_db_storage->hec_db_node_default          = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_db_storage->key
                                    hec_phase_guid_new = lr_db_storage->hec_phase_guid
                                    hec_phase_guid_old = <fs_db_storage_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_db_storage->hec_phase_changed = abap_true.
                  lv_data_changed                  = abap_true.

                ENDIF. "phasing changed
              ENDIF.  " IF <fs_db_storage_before> IS ASSIGNED.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_db_storage->hec_ip_storage_guid IS NOT INITIAL AND
                                                                       lr_db_storage->hec_phase_guid      IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_db_storage->hec_instance_status.
                lr_db_storage->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify DB server storage
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_storage->key
                                   is_data = lr_db_storage ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_attr_name,
                     ls_storage,
                     ls_pricing.

              UNASSIGN <fs_db_storage_before>.
            ENDLOOP.

            "-----------------------------------
            " Update Phasing
            "-----------------------------------
            IF lt_act_param_phasing IS NOT INITIAL.
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.

            "-----------------------------------
            " Set create DB server storage
            " backup action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_db_backup( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_backup )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

            ENDIF.

            " ***************************************************************************
            " Update mode after server update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-db_storage-update_after_server.

            LOOP AT lt_db_storage REFERENCE INTO lr_db_storage.
              ASSIGN lt_db_server[ key = lr_db_storage->parent_key ] TO <fs_db_server>.

              IF <fs_db_server> IS ASSIGNED.
                IF <fs_db_server>-hec_ip_server_guid IS NOT INITIAL AND
                   <fs_db_server>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              IF lv_release <> lr_db_storage->hec_row_selectable.
                lr_db_storage->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Update DB server cluster type
              "-----------------------------------
              IF lr_db_storage->hec_db_cluster_type_value <> <fs_db_server>-hec_db_cluster_type_value.
                lr_db_storage->hec_db_cluster_type_value = <fs_db_server>-hec_db_cluster_type_value.
                lv_data_changed = abap_true.
              ENDIF.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_db_storage->key
                                   is_data = lr_db_storage ).
              ENDIF.

              UNASSIGN <fs_db_server>.
              CLEAR: lv_release,
                     lv_data_changed.
            ENDLOOP. "  LOOP AT lt_db_storage
        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.
ENDCLASS.