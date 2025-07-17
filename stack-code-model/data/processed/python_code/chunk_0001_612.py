CLASS /hec1/cl_config_det_app_server DEFINITION
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
    DATA mr_act_param_app_node TYPE REF TO data .
    DATA mr_act_param_datac TYPE REF TO data .
    DATA mr_act_param_dlvy TYPE REF TO data .
    DATA mr_act_param_phasing TYPE REF TO data .
    DATA mr_act_param_server TYPE REF TO data .
    DATA mr_act_param_server_pc TYPE REF TO data .
    DATA mr_act_param_app_backup TYPE REF TO data .

    METHODS determine_app_node
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
    METHODS determine_app_node_cr
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
    METHODS determine_app_server
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
    METHODS determine_app_server_cr
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
    METHODS determine_app_server_instance
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
    METHODS determine_app_server_inst_cr
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
    METHODS determine_app_server_pc_cr
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
    METHODS determine_app_server_perf_cat
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
    METHODS determine_app_storage
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
    METHODS determine_app_storage_cr
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
    METHODS determine_app_storage_amount
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
    METHODS determine_app_storage_amoun_cr
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
    METHODS determine_app_storage_backup
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
    METHODS determine_app_storage_backu_cr
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



CLASS /HEC1/CL_CONFIG_DET_APP_SERVER IMPLEMENTATION.


  METHOD determine_app_node.

    DATA: lt_app_serv_inst     TYPE /hec1/t_data_app_serv_inst_ct,
          lt_app_node          TYPE /hec1/t_data_app_node_ct,
          lt_app_node_before   TYPE /hec1/t_data_app_node_ct,
          lt_node_key          TYPE /bobf/t_frw_key,
          lt_phase             TYPE /hec1/t_data_phase_ct,
          lt_app_serv_pc       TYPE /hec1/t_data_app_serv_pc_ct,
          lt_act_param         TYPE /hec1/t_act_create_app_spc,
          lt_act_param_node    TYPE /hec1/t_act_update_app_node,
          lt_act_param_phasing TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_node ).

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
          WHEN /hec1/if_configuration_c=>sc_determination-app_node-create.

            " Get App server instance node (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_node-to_parent
                                              IMPORTING et_data        = lt_app_serv_inst ).

            "-----------------------------------
            " App master node
            "-----------------------------------
            LOOP AT        lt_app_node
            REFERENCE INTO DATA(lr_app_node)
                    WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master.

              lr_app_node->hec_delete_visible = abap_false.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_app_node->hec_app_srv_perf_cat_qty IS NOT INITIAL AND
                                                                             lr_app_node->hec_phase_guid           IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_app_node->hec_instance_status.
                lr_app_node->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_app_serv_inst[ key = lr_app_node->parent_key ] TO FIELD-SYMBOL(<fs_app_serv_inst>).
              IF <fs_app_serv_inst> IS ASSIGNED.
                IF <fs_app_serv_inst>-hec_operating_sys_guid IS NOT INITIAL AND
                   <fs_app_serv_inst>-hec_app_cluster_type_value IS NOT INITIAL AND
                   <fs_app_serv_inst>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lr_app_node->hec_row_selectable            <> lv_release                                               AND
                 lr_app_node->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master.
                lr_app_node->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " App server performance category
              "-----------------------------------
              IF NOT ( lr_app_node->hec_server_required = abap_false AND
                       lr_app_node->hec_effort_required = abap_false     ).
                INSERT VALUE #( key             = lr_app_node->key
                                parent_key      = lr_app_node->parent_key
                                hec_app_srv_perf_cat_qty = lr_app_node->hec_app_srv_perf_cat_qty ) INTO TABLE lt_act_param.
              ENDIF.

              "-----------------------------------
              " Modify App server node
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_node->key
                                   is_data = lr_app_node ).

              ENDIF.

              UNASSIGN <fs_app_serv_inst>.
              CLEAR: lv_inst_status,
                     lv_release,
                     lv_data_changed.
            ENDLOOP.

            "-----------------------------------
            " App standby node
            "-----------------------------------
            LOOP AT        lt_app_node
            REFERENCE INTO lr_app_node
                     WHERE hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha           AND
                           hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-standby.

              lr_app_node->hec_delete_visible = abap_false.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_app_node->hec_app_srv_perf_cat_qty IS NOT INITIAL AND
                                                                       lr_app_node->hec_phase_guid           IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_app_node->hec_instance_status.
                lr_app_node->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Release selection standby node
              "-----------------------------------
              " Check master node is complete configered
              " ( including sub nodes: server performance category and storage amount )
              DATA(lv_complete) = /hec1/cl_bopf_config_validat_h=>check_master_node_is_complete( iv_is_app_server = abap_true
                                                                                                 iv_check_rule    = /hec1/if_bopf_constants=>gc_check_rule-node
                                                                                                 is_ctx           = is_ctx
                                                                                                 it_key           = VALUE #( ( key = lr_app_node->key ) )
                                                                                                 io_read          = io_read ).

              IF ( lv_complete                     = abap_true AND
                   lr_app_node->hec_row_selectable = abap_false    ) OR
                 ( lv_complete                     = abap_false AND
                   lr_app_node->hec_row_selectable = abap_true     ).

                lr_app_node->hec_row_selectable = COND #( WHEN lv_complete = abap_true
                                                          THEN abap_true
                                                          ELSE abap_false              ).
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify App server node
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_node->key
                                   is_data = lr_app_node ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_complete,
                     lv_data_changed.
            ENDLOOP.


            "-----------------------------------
            " Set create App server performance
            " category action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_spc( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_spc )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_node-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_app_node_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
                                              IMPORTING et_data        = lt_app_serv_pc ).


            LOOP AT lt_app_node REFERENCE INTO lr_app_node.

              ASSIGN lt_app_node_before[ key = lr_app_node->key ] TO FIELD-SYMBOL(<fs_app_node_before>).
              IF <fs_app_node_before> IS ASSIGNED.

                "-----------------------------------
                " App server performance category added
                "-----------------------------------
                IF <fs_app_node_before>-hec_app_srv_perf_cat_qty < lr_app_node->hec_app_srv_perf_cat_qty.
                  CASE lr_app_node->hec_app_clust_node_type_value.

                    WHEN /hec1/if_config_constants=>gc_app_clust_node_type-master.
                      "-----------------------------------
                      " Fill action table for create
                      " App server performance category
                      "-----------------------------------
                      INSERT VALUE #( key             = lr_app_node->key
                                      parent_key      = lr_app_node->parent_key
                                      hec_app_srv_perf_cat_qty = lr_app_node->hec_app_srv_perf_cat_qty - <fs_app_node_before>-hec_app_srv_perf_cat_qty ) INTO TABLE lt_act_param.

                      " Success message
                      /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_serv_perf_cat_added
                                                                     iv_severity = /bobf/cm_frw=>co_severity_success
                                                                     iv_attr1    = CONV #( lr_app_node->hec_app_srv_perf_cat_qty -
                                                                                   <fs_app_node_before>-hec_app_srv_perf_cat_qty )
                                                           CHANGING  co_message  = eo_message ).

                      " Set flag for deleting sub nodes of standby node
                      IF lr_app_node->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha          AND
                         lr_app_node->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                         lr_app_node->hec_master_default            = abap_true.
                        lv_data_changed            = abap_true.
                        DATA(lv_delete_ha_subnode) = abap_true.
                      ENDIF.
                  ENDCASE.

                ELSEIF <fs_app_node_before>-hec_app_srv_perf_cat_qty > lr_app_node->hec_app_srv_perf_cat_qty
                  AND lr_app_node->hec_app_srv_perf_cat_qty < lines( VALUE /hec1/t_data_app_serv_pc_ct( FOR app_serv_pc IN lt_app_serv_pc
                                                                                                        WHERE ( parent_key = lr_app_node->key )
                                                                                                        ( app_serv_pc ) ) ).
                  DATA(lv_attr_name) = /hec1/if_configuration_c=>sc_node_attribute-app_node-hec_app_srv_perf_cat_qty.

                  " Error message
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                 is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                               key      = lr_app_node->key
                                                                                               attributes = VALUE #( ( lv_attr_name ) ) )
                                                       CHANGING  co_message         = eo_message ).

                  " Set node number to value before update
                  lr_app_node->hec_app_srv_perf_cat_qty = <fs_app_node_before>-hec_app_srv_perf_cat_qty.
                  lv_data_changed                       = abap_true.
                ENDIF. " IF ls_app_node_old-hec_app_srv_perf_cat_qty < ls_app_node-hec_app_srv_perf_cat_qty.

                "-----------------------------------
                " Phase has changed - update phase
                " and inherit phase assignment
                "-----------------------------------
                IF lr_app_node->hec_phase_guid <> <fs_app_node_before>-hec_phase_guid.

                  IF lr_app_node->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                     lr_app_node->hec_master_default            = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_app_node->key
                                    hec_phase_guid_new = lr_app_node->hec_phase_guid
                                    hec_phase_guid_old = <fs_app_node_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_app_node->hec_phase_changed = abap_true.
                  lv_data_changed                = abap_true.

                  " Set flag for deleting subnodes of standby node
                  IF lr_app_node->hec_app_cluster_type_value = /hec1/if_config_constants=>gc_app_clust_node-ha.
                    lv_delete_ha_subnode = abap_true.
                  ENDIF.
                ENDIF. "phasing changed
              ENDIF. "IF <fs_app_node_before> IS ASSIGNED.

              "-----------------------------------
              " Set HA Info value/description
              " for standby node only
              "-----------------------------------
              IF lr_app_node->hec_app_clust_node_type_value =  /hec1/if_config_constants=>gc_app_clust_node_type-standby AND
                 lr_app_node->hec_ha_inf_prov_date          <> <fs_app_node_before>-hec_ha_inf_prov_date                 AND
                 lr_app_node->hec_ha_inf_prov_date          IS NOT INITIAL.
                CLEAR: lr_app_node->hec_ha_info_guid,
                       lr_app_node->hec_ha_category_value,
                       lr_app_node->hec_ha_category_descr,
                       lr_app_node->hec_spc_inst_feature_value,
                       lr_app_node->hec_spc_inst_feature_descr.

                SELECT SINGLE *
                  FROM /HEC1/I_AppNodeHAInfoBasic
                 WHERE hec_app_clust_node_type_guid = @lr_app_node->hec_app_clust_node_type_guid AND
                       hec_app_clnt_hai_val_start  <= @lr_app_node->hec_ha_inf_prov_date         AND
                       hec_app_clnt_hai_val_end    >= @lr_app_node->hec_ha_inf_prov_date
                  INTO @DATA(ls_ha_info).

                IF ls_ha_info IS NOT INITIAL.
                  lr_app_node->hec_ha_info_guid           = ls_ha_info-hec_app_clnt_hai_guid.
                  lr_app_node->hec_ha_category_value      = ls_ha_info-hec_app_clnt_hai_cat_value.
                  lr_app_node->hec_ha_category_descr      = ls_ha_info-hec_app_clnt_hai_cat_descr.
                  lr_app_node->hec_spc_inst_feature_value = ls_ha_info-hec_app_clnt_hai_sif_value.
                  lr_app_node->hec_spc_inst_feature_descr = ls_ha_info-hec_app_clnt_hai_sif_descr.
                  lv_data_changed                         = abap_true.
                ENDIF.
              ENDIF. " IF lr_app_node->hec_app_clust_node_type_value =  /hec1/if_config_constants=>gc_app_clust_node_type-standby AND...


              "-----------------------------------
              " Set HA Type Provisioning Date and
              " dependencies (standby node only)
              "-----------------------------------
              IF lr_app_node->hec_app_clust_node_type_value =  /hec1/if_config_constants=>gc_app_clust_node_type-standby AND
                 lr_app_node->hec_ha_type_prov_date         <> <fs_app_node_before>-hec_ha_type_prov_date                AND
                 lr_app_node->hec_ha_type_prov_date         IS NOT INITIAL.

                CLEAR: lr_app_node->hec_ha_type_guid,
                       lr_app_node->hec_ha_type_value,
                       lr_app_node->hec_ha_type_descr,
                       lr_app_node->hec_ha_type_curr_suppstat_guid,
                       lr_app_node->hec_ha_type_curr_suppstat_val,
                       lr_app_node->hec_ha_type_curr_suppstat_desc.


                SELECT *                      "#EC CI_ALL_FIELDS_NEEDED
                  FROM /HEC1/I_AppNodeTyWithAssocPa
                 WHERE hec_app_clust_node_type_guid    = @lr_app_node->hec_app_clust_node_type_guid AND
                       hec_app_clnt_hat_sust_valstart <= @lr_app_node->hec_ha_type_prov_date        AND
                       hec_app_clnt_hat_sust_val_end  >= @lr_app_node->hec_ha_type_prov_date
                  INTO TABLE @DATA(lt_ha_type).

                ASSIGN lt_ha_type[ hec_app_clnt_hat_sust_value = '02' ] TO FIELD-SYMBOL(<fs_ha_type>).

                IF <fs_ha_type> IS ASSIGNED.
                  lr_app_node->hec_ha_type_guid               = <fs_ha_type>-hec_app_clnt_ha_type_guid.
                  lr_app_node->hec_ha_type_value              = <fs_ha_type>-hec_app_clnt_ha_type_value.
                  lr_app_node->hec_ha_type_descr              = <fs_ha_type>-hec_app_clnt_ha_type_descr.
                  lr_app_node->hec_ha_type_curr_suppstat_guid = <fs_ha_type>-hec_app_clnt_ha_type_sust_guid.
                  lr_app_node->hec_ha_type_curr_suppstat_val  = <fs_ha_type>-hec_app_clnt_hat_sust_value.
                  lr_app_node->hec_ha_type_curr_suppstat_desc = <fs_ha_type>-hec_app_clnt_hat_sust_descr.

                  IF lr_app_node->hec_ha_type_init_suppstat_guid IS INITIAL.
                    lr_app_node->hec_ha_type_init_suppstat_guid = <fs_ha_type>-hec_app_clnt_ha_type_sust_guid.
                    lr_app_node->hec_ha_type_init_suppstat_val  = <fs_ha_type>-hec_app_clnt_hat_sust_value.
                    lr_app_node->hec_ha_type_init_suppstat_desc = <fs_ha_type>-hec_app_clnt_hat_sust_descr.
                  ENDIF.

                  lv_data_changed = abap_true.
                ENDIF. " IF <fs_ha_type> IS ASSIGNED.
              ENDIF. " IF lr_app_node->hec_app_clust_node_type_value =  /hec1/if_config_constants=>gc_app_clust_node_type-standby AND...


              "-----------------------------------
              " Set HA Type (standby node only)
              "-----------------------------------
              IF lr_app_node->hec_app_clust_node_type_value =  /hec1/if_config_constants=>gc_app_clust_node_type-standby AND
                 lr_app_node->hec_ha_type_guid              <> <fs_app_node_before>-hec_ha_type_guid                     AND
                 lr_app_node->hec_ha_type_prov_date         =  <fs_app_node_before>-hec_ha_type_prov_date                AND
                 lr_app_node->hec_ha_type_prov_date         IS NOT INITIAL                                               AND
                 lr_app_node->hec_ha_type_guid              IS NOT INITIAL.

                CLEAR: lr_app_node->hec_ha_type_value,
                       lr_app_node->hec_ha_type_descr,
                       lr_app_node->hec_ha_type_curr_suppstat_guid,
                       lr_app_node->hec_ha_type_curr_suppstat_val,
                       lr_app_node->hec_ha_type_curr_suppstat_desc.


                SELECT SINGLE *               "#EC CI_ALL_FIELDS_NEEDED
                  FROM /HEC1/I_AppNodeTyWithAssocPa
                 WHERE hec_app_clust_node_type_guid    = @lr_app_node->hec_app_clust_node_type_guid AND
                       hec_app_clnt_ha_type_guid       = @lr_app_node->hec_ha_type_guid             AND
                       hec_app_clnt_hat_sust_valstart <= @lr_app_node->hec_ha_type_prov_date        AND
                       hec_app_clnt_hat_sust_val_end  >= @lr_app_node->hec_ha_type_prov_date
                  INTO @DATA(ls_ha_type).


                IF ls_ha_type IS NOT INITIAL.
                  lr_app_node->hec_ha_type_guid               = ls_ha_type-hec_app_clnt_ha_type_guid.
                  lr_app_node->hec_ha_type_value              = ls_ha_type-hec_app_clnt_ha_type_value.
                  lr_app_node->hec_ha_type_descr              = ls_ha_type-hec_app_clnt_ha_type_descr.
                  lr_app_node->hec_ha_type_curr_suppstat_guid = ls_ha_type-hec_app_clnt_ha_type_sust_guid.
                  lr_app_node->hec_ha_type_curr_suppstat_val  = ls_ha_type-hec_app_clnt_hat_sust_value.
                  lr_app_node->hec_ha_type_curr_suppstat_desc = ls_ha_type-hec_app_clnt_hat_sust_descr.
                ENDIF.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_app_node->hec_app_srv_perf_cat_qty IS NOT INITIAL AND
                                                                       lr_app_node->hec_phase_guid           IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_app_node->hec_instance_status.
                lr_app_node->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Fill action table for delete
              " App server standby node subnodes
              " or relase standby node
              "-----------------------------------
              IF lr_app_node->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha          AND
                 lr_app_node->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                 lr_app_node->hec_master_default            = abap_true                                                AND
                 lv_data_changed                            = abap_true.

                IF NOT line_exists( lt_act_param_node[ key = lr_app_node->key ] ).
                  INSERT VALUE #( key                  = lr_app_node->key
                                  parent_key           = lr_app_node->parent_key
                                  do_release_ha_node   = COND #( WHEN lr_app_node->hec_instance_status         = /hec1/if_config_constants=>gc_instance_status-complete    AND
                                                                      <fs_app_node_before>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                                 THEN abap_true
                                                                 ELSE abap_false                                                  )
                                  do_delete_ha_subnode = COND #( WHEN lr_app_node->hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete OR
                                                                      lv_delete_ha_subnode             = abap_true
                                                                 THEN abap_true
                                                                 ELSE abap_false                                                                                        ) ) INTO TABLE lt_act_param_node.
                ENDIF.
              ENDIF. " IF lr_app_serv_perf_cat->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha


              "-----------------------------------
              " Modify App server node
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_node->key
                                   is_data = lr_app_node ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_attr_name,
                     lv_delete_ha_subnode.

              UNASSIGN <fs_app_node_before>.

            ENDLOOP.

            "-----------------------------------
            " Set create App server performance
            " category action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_spc( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_spc )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param    ).

            ENDIF.

            "-----------------------------------
            " Set Update Phasing
            " to general
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
            " Set update App node action to
            " general
            "-----------------------------------
            IF lt_act_param_node IS NOT INITIAL.
              CLEAR me->mr_act_param_app_node.
              me->mr_act_param_app_node = NEW /hec1/t_act_update_app_node( lt_act_param_node ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-app_node )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param_node
                                              ( key = wa_act_node-key )     )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_app_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_app_node                                                                                                       ).
            ENDIF.


            " ***************************************************************************
            " Update mode after app server
            " instance update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_node-update_after_server_inst.

            " Get App server instance
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_node-to_parent
                                              IMPORTING et_data        = lt_app_serv_inst ).



            LOOP AT lt_app_node REFERENCE INTO lr_app_node.
              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_app_serv_inst[ key = lr_app_node->parent_key ] TO <fs_app_serv_inst>.

              IF <fs_app_serv_inst> IS ASSIGNED.
                IF <fs_app_serv_inst>-hec_operating_sys_guid IS NOT INITIAL AND
                   <fs_app_serv_inst>-hec_app_cluster_type_value IS NOT INITIAL AND
                   <fs_app_serv_inst>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              IF lr_app_node->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                 lr_app_node->hec_row_selectable            <> lv_release.
                lr_app_node->hec_row_selectable = lv_release.
                lv_data_changed                 = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              " ( standby node)
              "-----------------------------------
              IF lr_app_node->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-standby AND
                 lr_app_node->hec_row_selectable            <> lv_release.

                IF lv_release                      = abap_false AND
                   lr_app_node->hec_row_selectable = abap_true.
                  lr_app_node->hec_row_selectable = abap_false.
                  lv_data_changed                 = abap_true.
                ELSE.
                  " Check master node is complete configered
                  " ( including sub nodes: server performance category and storage amount )
                  lv_complete = /hec1/cl_bopf_config_validat_h=>check_master_node_is_complete( iv_is_app_server = abap_true
                                                                                               iv_check_rule    = /hec1/if_bopf_constants=>gc_check_rule-node
                                                                                               is_ctx           = is_ctx
                                                                                               it_key           = VALUE #( ( key = lr_app_node->key ) )
                                                                                               io_read          = io_read ).
                  IF lv_complete = abap_true.
                    lr_app_node->hec_row_selectable = abap_true.
                    lv_data_changed                 = abap_true.
                  ENDIF.
                ENDIF. " IF lv_release = abap_false AND...
              ENDIF. " IF lr_app_node->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-standby AND...


              "-----------------------------------
              " Update App server cluster type
              "-----------------------------------
              IF lr_app_node->hec_app_cluster_type_value <> <fs_app_serv_inst>-hec_app_cluster_type_value.
                lr_app_node->hec_app_cluster_type_value = <fs_app_serv_inst>-hec_app_cluster_type_value.
                lv_data_changed                         = abap_true.
              ENDIF.


              "-----------------------------------
              " Modify App node
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_node->key
                                   is_data = lr_app_node ).
              ENDIF.


              UNASSIGN <fs_app_serv_inst>.
              CLEAR: lv_release,
                     lv_complete,
                     lv_data_changed.
            ENDLOOP.
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_app_server.

    DATA: lt_app_server        TYPE /hec1/t_data_app_serv_ct,
          lt_app_serv_perf_cat TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_storage       TYPE /hec1/t_data_app_storage_ct,
          lt_line              TYPE TABLE OF string,
          lt_phase             TYPE /hec1/t_data_phase_ct,
          lt_app_server_before TYPE /hec1/t_data_app_serv_ct,
          lt_act_param         TYPE /hec1/t_act_create_app_storage,
          lt_act_param_storage TYPE /bobf/t_frw_key,
          lt_act_param_server  TYPE /hec1/t_act_update_app_server,
          lt_act_param_dlvy    TYPE /hec1/t_act_update_dlvy_unit,
          lt_act_param_datac   TYPE /hec1/t_act_update_datacenter,
          lt_act_param_serv_pc TYPE /hec1/t_act_update_app_serv_pc,
          lt_act_param_phasing TYPE TABLE OF /hec1/s_act_phase_inherit.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_server ).

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
          WHEN /hec1/if_configuration_c=>sc_determination-app_server-create.

            " Get App server performance category node (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server-to_parent
                                              IMPORTING et_data        = lt_app_serv_perf_cat ).

            LOOP AT        lt_app_server
            REFERENCE INTO DATA(lr_app_server)
                     WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master.

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              lr_app_server->hec_ip_server_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server(
                                                                            iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                            iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                            iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_app_server->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL )
                                                                            iv_srv_perf_cat_guid   = VALUE #( lt_app_serv_perf_cat[ key = lr_app_server->parent_key ]-hec_srv_perf_cat_guid OPTIONAL ) ) )
                                                          THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                          ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              lr_app_server->hec_delete_visible = abap_false.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_app_server->hec_ip_server_guid IS NOT INITIAL AND
                                                                             lr_app_server->hec_phase_guid     IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete          ).

              IF lv_inst_status <> lr_app_server->hec_instance_status.
                lr_app_server->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_app_serv_perf_cat[ key = lr_app_server->parent_key ] TO FIELD-SYMBOL(<fs_app_serv_perf_cat>).
              IF <fs_app_serv_perf_cat> IS ASSIGNED.
                IF <fs_app_serv_perf_cat>-hec_srv_perf_cat_guid IS NOT INITIAL AND
                   <fs_app_serv_perf_cat>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_app_server->hec_row_selectable.
                lr_app_server->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " App server storage
              "-----------------------------------
              INSERT VALUE #( key         = lr_app_server->key
                              parent_key  = lr_app_server->parent_key
                              hec_pricing_included = abap_false                ) INTO TABLE lt_act_param.

              "-----------------------------------
              " Modify
              "-----------------------------------
              IF lv_data_changed = abap_true.


                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_server->key
                                   is_data = lr_app_server ).
              ENDIF.

              UNASSIGN <fs_app_serv_perf_cat>.
              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release.
            ENDLOOP.


            "-----------------------------------
            " Set create App server storage
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_storage( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_storage )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                    ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_server-update.

            " Get Before image
            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_fill_data    = abap_true
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_app_server_before ).

            " Get App server performance category (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server-to_parent
                                              IMPORTING et_data        = lt_app_serv_perf_cat ).

            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server-app_storage
                                              IMPORTING et_data        = lt_app_storage ).

            " Get Phases
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            LOOP AT lt_app_server REFERENCE INTO lr_app_server.
              ASSIGN lt_app_server_before[ key = lr_app_server->key ] TO FIELD-SYMBOL(<fs_app_server_before>).
              IF <fs_app_server_before> IS ASSIGNED.

                "-----------------------------------
                " Split DB server infrastructure
                " provider server GUID
                "-----------------------------------
                IF lr_app_server->hec_ip_server_guid CA ';'.
                  SPLIT lr_app_server->hec_ip_server_guid
                     AT ';'
                   INTO TABLE lt_line.

                  LOOP AT lt_line ASSIGNING FIELD-SYMBOL(<fs_line>).
                    CASE sy-tabix.
                      WHEN 1.
                        lr_app_server->hec_ip_server_guid = <fs_line>.
                      WHEN 2.
                        DATA(lv_inf_provider_guid) = <fs_line>.
                      WHEN 3.
                        DATA(lv_datacenter_guid) = <fs_line>.
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
                      DATA(ls_datacenter) = lt_datacenter[ hec_node_datacenter = lr_app_server->hec_tier_datacenter_guid ].

                      IF ls_datacenter-hec_datacenter_guid IS INITIAL.
                        INSERT VALUE #( key                     = ls_datacenter-key
                                        parent_key              = ls_datacenter-parent_key
                                        hec_datacenter_fdt_guid = lv_datacenter_guid       ) INTO TABLE lt_act_param_datac.
*
                        "-----------------------------------
                        " Fill action table for update
                        " App node pricing
                        "-----------------------------------
                        INSERT VALUE #( key               = lr_app_server->parent_key
                                        do_update_pricing = abap_true                 ) INTO TABLE lt_act_param_serv_pc.

                      ENDIF. " IF ls_datacenter-hec_datacenter_guid IS INITIAL.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                ENDIF. " IF ls_app_server-hec_ds_ip_server_guid CA ';'.


                "-----------------------------------
                " App server has changed
                "-----------------------------------
                IF lr_app_server->hec_ip_server_guid     IS NOT INITIAL                            AND
                   lr_app_server->hec_ip_server_guid <> <fs_app_server_before>-hec_ip_server_guid.

                  IF lv_inf_provider_guid IS NOT INITIAL.
                    lr_dlvy_unit->hec_inf_provider_guid = lv_inf_provider_guid.
                  ENDIF.

                  IF lr_app_server->hec_sec_datacenter_guid IS     INITIAL AND
                     lv_datacenter_guid                     IS NOT INITIAL.
                    lr_app_server->hec_sec_datacenter_guid = lv_datacenter_guid.
                    lv_data_changed                   = abap_true.
                  ENDIF.

                  SELECT SINGLE *
                    FROM /hec1/i_serverbasic
                   WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid             AND
                         hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid    AND
                         hec_sec_datacenter_guid = @lr_app_server->hec_sec_datacenter_guid AND
                         hec_ip_server_guid      = @lr_app_server->hec_ip_server_guid
                    INTO @DATA(ls_server).

                  IF ls_server IS NOT INITIAL.
                    lr_app_server->hec_ip_server_descr      = ls_server-hec_ip_server_descr.
                    lr_app_server->hec_ip_server_guid       = ls_server-hec_ip_server_guid.
                    lr_app_server->hec_host_type_descr      = ls_server-hec_srv_host_type_descr.
                    lr_app_server->hec_host_type_value      = ls_server-hec_srv_host_type_value.
                    lr_app_server->hec_srv_ram_size         = ls_server-hec_srv_ram_size.
                    lr_app_server->hec_srv_cpu_size         = ls_server-hec_srv_cpu_size.
                    lr_app_server->hec_sec_datacenter_guid  = ls_server-hec_sec_datacenter_guid.
                    lr_app_server->hec_srv_main_storage_qty = ls_server-hec_srv_main_storage_qty.
                    lr_app_server->hec_tree_descr           = ls_server-hec_ip_server_descr. "#EC CI_FLDEXT_OK[2215424]
                    lr_app_server->hec_as_flavour           = ls_server-hec_srv_flavour.
                    lr_app_server->hec_saps                 = ls_server-hec_saps.
                    lr_app_server->hec_approval_needed      = ls_server-hec_approval_needed.

                    lv_data_changed                         = abap_true.

                    " Set Value List Quantity
                    lr_app_server->hec_ip_server_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server(
                                                                                  iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                  iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                                  iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_app_server->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL )
                                                                                  iv_srv_perf_cat_guid   = VALUE #( lt_app_serv_perf_cat[ key = lr_app_server->parent_key ]-hec_srv_perf_cat_guid OPTIONAL ) ) )
                                                                THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                    "-------------------------
                    " Get App server pricing
                    "-------------------------
                    SELECT SINGLE hec_cb_pricing_lb_guid
                      FROM /hec1/i_serverlbbasic
                     WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid             AND
                           hec_sec_datacenter_guid = @lr_app_server->hec_sec_datacenter_guid AND
                           hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid    AND
                           hec_ip_server_guid      = @lr_app_server->hec_ip_server_guid
                      INTO @DATA(lv_lb_guid).

                    IF lv_lb_guid IS NOT INITIAL.
                      SELECT SINGLE * FROM /hec1/c_cbp_lb "#EC CI_ALL_FIELDS_NEEDED
                         INTO @DATA(ls_pricing)
                        WHERE hec_price_lb = @lv_lb_guid.

                      lr_app_server->* = CORRESPONDING #( BASE ( lr_app_server->* ) ls_pricing ).
                    ENDIF.

                    "-----------------------------------
                    " Fill action table for update
                    " App server storage
                    "-----------------------------------
                    LOOP AT lt_app_storage REFERENCE INTO DATA(lr_app_storage)
                      WHERE parent_key = lr_app_server->key.
                      INSERT VALUE #( key = lr_app_storage->key ) INTO TABLE lt_act_param_storage.
                    ENDLOOP.
                  ENDIF. " IF ls_server IS NOT INITIAL.
                ENDIF. "  IF ls_app_server-hec_as_ip_server_guid IS NOT INITIAL AND...

                "-----------------------------------
                " Value List Quanitty
                "-----------------------------------
                " HEC_AS_BACKUPSLA_VALUE
                IF lr_app_server->hec_as_backupsla_value <> <fs_app_server_before>-hec_as_backupsla_value.
                  lr_app_server->hec_as_backupsla_vlqt = COND #( WHEN 1 < lines( /rbp/cl_fpm_utilities=>get_characteristic_values( CONV #( 'HEC_AS_BACKUPSLA_VALUE' ) ) )
                                                                 THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                 ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).
                ENDIF.

                " HEC_AS_BACKUPSLA_FILE_VALUE
                IF lr_app_server->hec_as_backupsla_file_value <> <fs_app_server_before>-hec_as_backupsla_file_value.
                  lr_app_server->hec_as_backupsla_file_vlqt = COND #( WHEN 1 < lines( /rbp/cl_fpm_utilities=>get_characteristic_values( CONV #( 'HEC_AS_BACKUPSLA_FILE_VALUE' ) ) )
                                                                      THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                      ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).
                ENDIF.

                "-----------------------------------
                " Phase has changed -
                " update phase and inherit phase assignment
                "-----------------------------------
                IF lr_app_server->hec_phase_guid NE <fs_app_server_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_app_server->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                     lr_app_server->hec_app_node_default          = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_app_server->key
                                    hec_phase_guid_new = lr_app_server->hec_phase_guid
                                    hec_phase_guid_old = <fs_app_server_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_app_server->hec_phase_changed = abap_true.
                  lv_data_changed                  = abap_true.

                ENDIF. "phasing changed
              ENDIF. " if <fs_app_server_before> is assigned.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_app_server->hec_ip_server_guid IS NOT INITIAL AND
                                                                       lr_app_server->hec_phase_guid     IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_app_server->hec_instance_status.
                lr_app_server->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_server->key
                                   is_data = lr_app_server ).
              ENDIF.

              UNASSIGN: <fs_line>,
                             <fs_app_server_before>.

              CLEAR: lv_inf_provider_guid,
                     lv_datacenter_guid,
                     lv_lb_guid,
                     lv_inst_status,
                     lv_data_changed,
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
            " Set App Server PC action to
            " general
            "-----------------------------------
            IF lt_act_param_serv_pc IS NOT INITIAL.

              me->mr_act_param_server_pc = NEW /hec1/t_act_update_app_serv_pc( lt_act_param_serv_pc ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-app_server_perform_cat )
                    it_key          = VALUE #( FOR wa_act_spc IN lt_act_param_serv_pc
                                             ( key = wa_act_spc-key )             )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_app_server_perf_cat )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_server_pc   ).

            ENDIF.

            "-----------------------------------
            " Set update App Storage action to
            " general
            "-----------------------------------
            IF lt_act_param_storage IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-app_storage )
                  it_key          = lt_act_param_storage
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_app_storage )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                                               ).
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
                  ir_act_param    = me->mr_act_param_phasing                                                                                                                 ).
            ENDIF.


            " ***************************************************************************
            " Update mode after app server
            " performance category update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_server-update_after_serv_perf_cat.

            " Get App server performance category (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server-to_parent
                                              IMPORTING et_data        = lt_app_serv_perf_cat ).


            LOOP AT lt_app_server REFERENCE INTO lr_app_server.
              ASSIGN lt_app_serv_perf_cat[ key = lr_app_server->parent_key ] TO <fs_app_serv_perf_cat>.

              IF <fs_app_serv_perf_cat> IS ASSIGNED.
                IF <fs_app_serv_perf_cat>-hec_srv_perf_cat_guid IS NOT INITIAL AND
                   <fs_app_serv_perf_cat>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              IF lv_release <> lr_app_server->hec_row_selectable.
                lr_app_server->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Update App server cluster type
              "-----------------------------------
              IF lr_app_server->hec_app_cluster_type_value <> <fs_app_serv_perf_cat>-hec_app_cluster_type_value.
                lr_app_server->hec_app_cluster_type_value = <fs_app_serv_perf_cat>-hec_app_cluster_type_value.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_server->key
                                   is_data = lr_app_server ).
              ENDIF.

              UNASSIGN <fs_app_serv_perf_cat>.

              CLEAR: lv_release,
                     lv_data_changed.

            ENDLOOP. " LOOP AT lt_app_server
        ENDCASE.



      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_app_server_instance.

    DATA: lt_app_serv_inst         TYPE /hec1/t_data_app_serv_inst_ct,
          lt_app_serv_inst_before  TYPE /hec1/t_data_app_serv_inst_ct,
          lt_app_serv_inst_pertier TYPE /hec1/t_data_app_serv_inst_ct,
          lt_app_node              TYPE /hec1/t_data_app_node_ct,
          lt_tier                  TYPE /hec1/t_data_tier_ct,
          lt_act_param             TYPE /hec1/t_act_create_app_node,
          lt_phase                 TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing     TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_serv_inst ).

    " Get tier
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-to_parent
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

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_server_instance-create.
            LOOP AT lt_app_serv_inst REFERENCE INTO DATA(lr_app_serv_inst).

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              " App Server Instance
              lr_app_serv_inst->hec_sol_tier_stack_si_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server_instance(
                                                                                       iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                       iv_sol_tier_stack_guid = lr_app_serv_inst->hec_sol_tier_stack_guid
                                                                                       iv_srv_inst_rel_value  = lr_app_serv_inst->hec_srv_inst_rel_value
                                                                                       iv_solution_guid       = lr_app_serv_inst->hec_solution_guid
                                                                                       iv_is_app_server       = abap_true ) )
                                                                     THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                     ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " Operating System
              lr_app_serv_inst->hec_sol_apsi_oper_sys_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_app_operating_system(
                                                                                                     iv_apm_guid               = lr_landscape->hec_apm_guid
                                                                                                     iv_sol_tier_stack_si_guid = lr_app_serv_inst->hec_sol_tier_stack_si_guid ) )
                                                                     THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                     ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " Cluster Type
              lr_app_serv_inst->hec_sol_apsi_clusttyp_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_app_cluster_type(
                                                                                                     iv_apm_guid               = lr_landscape->hec_apm_guid
                                                                                                     iv_sol_tier_stack_si_guid = lr_app_serv_inst->hec_sol_tier_stack_si_guid ) )
                                                                     THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                     ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              lr_app_serv_inst->hec_delete_visible = COND #( WHEN lr_app_serv_inst->hec_default_app_server_inst = abap_true
                                                             THEN abap_false
                                                             ELSE abap_true ).

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_app_serv_inst->hec_sol_tier_stack_si_guid IS NOT INITIAL AND
                                                                             lr_app_serv_inst->hec_sol_apsi_oper_sys_guid IS NOT INITIAL AND
                                                                             lr_app_serv_inst->hec_sol_apsi_clusttyp_guid IS NOT INITIAL AND
                                                                             lr_app_serv_inst->hec_phase_guid             IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete         ).

              IF lv_inst_status <> lr_app_serv_inst->hec_instance_status.
                lr_app_serv_inst->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_tier[ key = lr_app_serv_inst->parent_key ] TO FIELD-SYMBOL(<fs_tier>).
              IF <fs_tier> IS ASSIGNED.
                IF <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                   <fs_tier>-hec_tier_type_value      IS NOT INITIAL AND
                   <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_app_serv_inst->hec_row_selectable.
                lr_app_serv_inst->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for
              " create App node
              "-----------------------------------
              IF lr_app_serv_inst->hec_sol_tier_stack_si_guid IS NOT INITIAL AND
                 lr_app_serv_inst->hec_sol_apsi_oper_sys_guid IS NOT INITIAL AND
                 lr_app_serv_inst->hec_sol_apsi_clusttyp_guid IS NOT INITIAL.

                INSERT VALUE #( key                        = lr_app_serv_inst->key
                                parent_key                 = lr_app_serv_inst->parent_key
                                hec_app_cluster_type_value = SWITCH #( lr_app_serv_inst->hec_app_cluster_type_value
                                                                       WHEN /hec1/if_config_constants=>gc_app_clust_node-none
                                                                       THEN /hec1/if_config_constants=>gc_app_clust_node-none
                                                                       WHEN /hec1/if_config_constants=>gc_app_clust_node-ha
                                                                       THEN /hec1/if_config_constants=>gc_app_clust_node-ha
                                                                       ELSE /hec1/if_config_constants=>gc_app_clust_node-none )
                                hec_default_app_server     = SWITCH #( lr_app_serv_inst->hec_default_app_server_inst
                                                                       WHEN abap_true
                                                                       THEN abap_true
                                                                       ELSE abap_false                               )           ) INTO TABLE lt_act_param.
              ENDIF.

              "-----------------------------------
              " Modify App server instance
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_serv_inst->key
                                   is_data = lr_app_serv_inst ).
              ENDIF.

              UNASSIGN <fs_tier>.

              CLEAR: lv_inst_status,
                     lv_release,
                     lv_data_changed.
            ENDLOOP.


            "-----------------------------------
            " Set create App server node
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_node( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key )        )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_node )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_server_instance-update.

            " Get data before update
            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_app_serv_inst_before ).

            " Get app ndde
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-app_node
                                              IMPORTING et_data        = lt_app_node ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get all app server instances per tier
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                        it_key         = lt_tier_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier-app_server_instance
                                              IMPORTING et_data        = lt_app_serv_inst_pertier ).

            "-----------------------------------
            " Get App server instance data
            "-----------------------------------
            SELECT *                          "#EC CI_ALL_FIELDS_NEEDED
              FROM /hec1/i_appservinstancenobasic
             WHERE hec_apm_guid = @lr_landscape->hec_apm_guid
              INTO TABLE @DATA(lt_app_serv_inst_no).

            "-----------------------------------
            " Get App server operating system
            "-----------------------------------
            SELECT *                          "#EC CI_ALL_FIELDS_NEEDED
              FROM /hec1/i_appopersystembasic
             WHERE hec_apm_guid = @lr_landscape->hec_apm_guid
              INTO TABLE @DATA(lt_app_operating_sys).

            "-----------------------------------
            " Get App server cluster type
            "-----------------------------------
            SELECT *                          "#EC CI_ALL_FIELDS_NEEDED
              FROM /hec1/i_appclustertypebasic
             WHERE hec_apm_guid = @lr_landscape->hec_apm_guid
              INTO TABLE @DATA(lt_cluster_type).


            LOOP AT lt_app_serv_inst REFERENCE INTO lr_app_serv_inst.

              ASSIGN lt_app_serv_inst_before[ key = lr_app_serv_inst->key ] TO FIELD-SYMBOL(<fs_serv_inst_before>).
              IF <fs_serv_inst_before> IS ASSIGNED.

                " Can this value change? TODO
                lr_app_serv_inst->hec_delete_visible = COND #( WHEN lr_app_serv_inst->hec_default_app_server_inst = abap_true
                                                               THEN abap_false
                                                               ELSE abap_true ).

                "-----------------------------------
                " Update operating system
                "-----------------------------------
                IF <fs_serv_inst_before>-hec_sol_apsi_oper_sys_guid IS INITIAL     AND
                   lr_app_serv_inst->hec_sol_apsi_oper_sys_guid     IS NOT INITIAL.

                  TRY.
                      DATA(ls_operating_sys) = lt_app_operating_sys[ hec_sol_tier_stack_si_guid = lr_app_serv_inst->hec_sol_tier_stack_si_guid
                                                                     hec_sol_apsi_oper_sys_guid = lr_app_serv_inst->hec_sol_apsi_oper_sys_guid     ].

                      lr_app_serv_inst->hec_sol_apsi_oper_sys_guid = ls_operating_sys-hec_sol_apsi_oper_sys_guid.
                      lr_app_serv_inst->hec_operating_sys_guid     = ls_operating_sys-hec_operating_sys_guid.
                      lr_app_serv_inst->hec_operating_sys_value    = ls_operating_sys-hec_operating_sys_value.
                      lr_app_serv_inst->hec_operating_sys_descr    = ls_operating_sys-hec_operating_sys_descr.
                      lr_app_serv_inst->hec_os_support_stat_value  = ls_operating_sys-hec_os_support_stat_value.
                      lr_app_serv_inst->hec_os_support_stat_descr  = ls_operating_sys-hec_os_support_stat_descr.

                      lv_data_changed                              = abap_true.

                      "-----------------------------------
                      " Value List Quanitty
                      "-----------------------------------
                      " Operating System
                      IF lr_app_serv_inst->hec_sol_apsi_oper_sys_guid <> <fs_serv_inst_before>-hec_sol_apsi_oper_sys_guid.
                        lr_app_serv_inst->hec_sol_apsi_oper_sys_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_app_operating_system(
                                                                                                               iv_apm_guid               = lr_landscape->hec_apm_guid
                                                                                                               iv_sol_tier_stack_si_guid = lr_app_serv_inst->hec_sol_tier_stack_si_guid ) )
                                                                               THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                               ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).
                      ENDIF.

                      " HEC_ASI_PATCH_LEVEL_VALUE
                      IF lr_app_serv_inst->hec_asi_patch_level_value <> <fs_serv_inst_before>-hec_asi_patch_level_value.
                        lr_app_serv_inst->hec_asi_patch_level_vlqt = COND #( WHEN 1 < lines( /rbp/cl_fpm_utilities=>get_characteristic_values( CONV #( 'HEC_ASI_PATCH_LEVEL_VALUE' ) ) )
                                                                             THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                             ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).
                      ENDIF.

                      " HEC_ASI_OPSYS_IMAGE_VAL
                      IF lr_app_serv_inst->hec_asi_opsys_image_val <> <fs_serv_inst_before>-hec_asi_opsys_image_val.
                        lr_app_serv_inst->hec_asi_opsys_image_vlqt = COND #( WHEN 1 < lines( /rbp/cl_fpm_utilities=>get_characteristic_values( CONV #( 'HEC_ASI_OPSYS_IMAGE_VAL' ) ) )
                                                                             THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                             ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).
                      ENDIF.

                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                  CLEAR ls_operating_sys.
                ENDIF. " IF <fs_serv_inst_before>-hec_asi_operating_sys_guid IS INITIAL     AND...

                "-----------------------------------
                " Update App server instance GUID
                "-----------------------------------
                IF <fs_serv_inst_before>-hec_sol_tier_stack_si_guid IS INITIAL     AND
                   lr_app_serv_inst->hec_sol_tier_stack_si_guid     IS NOT INITIAL AND
                   lr_app_serv_inst->hec_default_app_server_inst = abap_false.

                  TRY.
                      DATA(ls_server_inst_no) = lt_app_serv_inst_no[ hec_sol_tier_stack_guid    = lr_app_serv_inst->hec_sol_tier_stack_guid
                                                                     hec_sol_tier_stack_si_guid = lr_app_serv_inst->hec_sol_tier_stack_si_guid ].


                      DATA(ls_cluster_type) = lt_cluster_type[ hec_sol_tier_stack_si_guid  = lr_app_serv_inst->hec_sol_tier_stack_si_guid
                                                               hec_app_cluster_type_value  = /hec1/if_config_constants=>gc_app_clust_node-none ].


                      lr_app_serv_inst->* = CORRESPONDING #( BASE ( lr_app_serv_inst->* ) ls_server_inst_no EXCEPT hec_srv_inst_rel_value
                                                                                                                   hec_srv_inst_rel_descr ).

                      lr_app_serv_inst->*                      = CORRESPONDING #( BASE ( lr_app_serv_inst->* ) ls_cluster_type ).
                      lr_app_serv_inst->hec_backup_relev_value = ls_server_inst_no-hec_backup_relevance.
                      lr_app_serv_inst->hec_tree_descr         = ls_server_inst_no-hec_sol_tier_asi_descr.

                      lv_data_changed                          = abap_true.

                      " Set Value List Quantity - App Server Instance
                      lr_app_serv_inst->hec_sol_tier_stack_si_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server_instance(
                                                                                               iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                               iv_sol_tier_stack_guid = lr_app_serv_inst->hec_sol_tier_stack_guid
                                                                                               iv_srv_inst_rel_value  = lr_app_serv_inst->hec_srv_inst_rel_value
                                                                                               iv_solution_guid       = lr_app_serv_inst->hec_solution_guid
                                                                                               iv_is_app_server       = abap_true ) )
                                                                             THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                             ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                      " Set Value List Quantity - Cluster Type
                      lr_app_serv_inst->hec_sol_apsi_clusttyp_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_app_cluster_type(
                                                                                                             iv_apm_guid               = lr_landscape->hec_apm_guid
                                                                                                             iv_sol_tier_stack_si_guid = lr_app_serv_inst->hec_sol_tier_stack_si_guid ) )
                                                                             THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                             ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                      " Same app server exist, then operating system
                      " has to be set same as the existing app server
                      " is set
                      DATA(lt_filter) = VALUE /hec1/t_filter_app_serv_inst( ( hec_node_solution      = lr_app_serv_inst->hec_node_solution
                                                                              hec_node_tier          = lr_app_serv_inst->hec_node_tier     ) ).

                      DATA(lt_filter_app_serv_inst) = FILTER #( lt_app_serv_inst_pertier IN lt_filter WHERE hec_node_solution = hec_node_solution AND
                                                                                                            hec_node_tier     = hec_node_tier         ).

                      " Delete current app server instacne
                      DELETE lt_filter_app_serv_inst
                       WHERE hec_node_app_serv_inst = lr_app_serv_inst->hec_node_app_serv_inst.


                      ASSIGN lt_filter_app_serv_inst[ hec_sol_tier_stack_guid    = lr_app_serv_inst->hec_sol_tier_stack_guid
                                                      hec_sol_tier_stack_si_guid = lr_app_serv_inst->hec_sol_tier_stack_si_guid ] TO FIELD-SYMBOL(<fs_app_server_inst>). "#EC CI_SORTSEQ

                      IF <fs_app_server_inst> IS ASSIGNED.
                        lr_app_serv_inst->hec_sol_apsi_oper_sys_guid = <fs_app_server_inst>-hec_sol_apsi_oper_sys_guid.
                        lr_app_serv_inst->hec_operating_sys_guid     = <fs_app_server_inst>-hec_operating_sys_guid.
                        lr_app_serv_inst->hec_operating_sys_value    = <fs_app_server_inst>-hec_operating_sys_value.
                        lr_app_serv_inst->hec_operating_sys_descr    = <fs_app_server_inst>-hec_operating_sys_descr.
                        lr_app_serv_inst->hec_os_support_stat_value  = <fs_app_server_inst>-hec_os_support_stat_value.
                        lr_app_serv_inst->hec_os_support_stat_descr  = <fs_app_server_inst>-hec_os_support_stat_descr.
                      ENDIF.

                      IF lr_app_serv_inst->hec_sol_apsi_oper_sys_guid IS INITIAL.
                        " Is only one operating system available, it
                        " can be set directly
                        DATA(lt_operating_sys) = VALUE /hec1/t_apm_app_operating_sys( FOR wa IN lt_app_operating_sys
                                                                                      WHERE ( hec_sol_tier_stack_si_guid = ls_server_inst_no-hec_sol_tier_stack_value )
                                                                                      ( CORRESPONDING #( wa )                                                          ) ).

                        IF lines( lt_operating_sys ) = 1.
                          DATA(ls_oper_sys) = lt_operating_sys[ 1 ].
                          lr_app_serv_inst->hec_sol_apsi_oper_sys_guid = ls_oper_sys-hec_sol_apsi_oper_sys_guid.
                          lr_app_serv_inst->hec_operating_sys_guid     = ls_oper_sys-hec_operating_sys_guid.
                          lr_app_serv_inst->hec_operating_sys_value    = ls_oper_sys-hec_operating_sys_value.
                          lr_app_serv_inst->hec_operating_sys_descr    = ls_oper_sys-hec_operating_sys_descr.
                          lr_app_serv_inst->hec_os_support_stat_value  = ls_oper_sys-hec_os_support_stat_value.
                          lr_app_serv_inst->hec_os_support_stat_descr  = ls_oper_sys-hec_os_support_stat_descr.
                        ENDIF. " IF lines( lt_app_oper_sys ) = 1.
                      ENDIF. " IF ls_app_server_inst-hec_asi_operating_sys_guid IS INITIAL.

                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                ENDIF. " IF ls_app_server_inst_old-hec_app_srv_guid IS INITIAL     AND


                "-----------------------------------
                " Phase has changed -
                " update phase and inherit phase assignment
                "-----------------------------------
                IF lr_app_serv_inst->hec_phase_guid NE <fs_serv_inst_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_app_serv_inst->key
                                  hec_phase_guid_new = lr_app_serv_inst->hec_phase_guid
                                  hec_phase_guid_old = <fs_serv_inst_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_app_serv_inst->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "phasing changed
              ENDIF." IF <fs_serv_inst_before> IS ASSIGNED.

              "-----------------------------------
              " Fill action table for
              " create App node
              "-----------------------------------
              IF lr_app_serv_inst->hec_sol_tier_stack_si_guid IS NOT INITIAL AND
                 lr_app_serv_inst->hec_sol_apsi_oper_sys_guid IS NOT INITIAL AND
                 lr_app_serv_inst->hec_sol_apsi_clusttyp_guid IS NOT INITIAL AND
             NOT line_exists( lt_app_node[ parent_key = lr_app_serv_inst->key ] ).

                INSERT VALUE #( key                        = lr_app_serv_inst->key
                                parent_key                 = lr_app_serv_inst->parent_key
                                hec_app_cluster_type_value = SWITCH #( lr_app_serv_inst->hec_app_cluster_type_value
                                                                       WHEN /hec1/if_config_constants=>gc_app_clust_node-none
                                                                       THEN /hec1/if_config_constants=>gc_app_clust_node-none
                                                                       WHEN /hec1/if_config_constants=>gc_app_clust_node-ha
                                                                       THEN /hec1/if_config_constants=>gc_app_clust_node-ha
                                                                       ELSE /hec1/if_config_constants=>gc_app_clust_node-none )
                                hec_default_app_server     = SWITCH #( lr_app_serv_inst->hec_default_app_server_inst
                                                                       WHEN abap_true
                                                                       THEN abap_true
                                                                       ELSE abap_false                               )           ) INTO TABLE lt_act_param.
              ENDIF.



              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_app_serv_inst->hec_sol_tier_stack_si_guid IS NOT INITIAL AND
                                                                       lr_app_serv_inst->hec_sol_apsi_oper_sys_guid IS NOT INITIAL AND
                                                                       lr_app_serv_inst->hec_sol_apsi_clusttyp_guid IS NOT INITIAL AND
                                                                       lr_app_serv_inst->hec_phase_guid             IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete         ).

              IF lv_inst_status <> lr_app_serv_inst->hec_instance_status.
                lr_app_serv_inst->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify App server instance
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_serv_inst->key
                                   is_data = lr_app_serv_inst ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     ls_server_inst_no,
                     ls_cluster_type,
                     ls_oper_sys,
                     ls_operating_sys,
                     lt_filter,
                     lt_filter_app_serv_inst,
                     lt_operating_sys.

              UNASSIGN <fs_serv_inst_before>.
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
            " Set create App server node
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_node( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key )        )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_node )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                ).

            ENDIF.


            " ***************************************************************************
            " " Update mode after tier update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_server_instance-update_after_tier.

            LOOP AT lt_app_serv_inst REFERENCE INTO lr_app_serv_inst.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_tier[ key = lr_app_serv_inst->parent_key ] TO <fs_tier>.
              IF <fs_tier> IS ASSIGNED.
                IF <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                   <fs_tier>-hec_tier_type_value      IS NOT INITIAL AND
                   <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_app_serv_inst->hec_row_selectable.
                lr_app_serv_inst->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Modify App server instance
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_serv_inst->key
                                   is_data = lr_app_serv_inst ).
              ENDIF.

              UNASSIGN <fs_tier>.
              CLEAR: lv_release,
                     lv_data_changed.
            ENDLOOP.
        ENDCASE.



      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_app_server_perf_cat.

    DATA: lt_app_serv_perf_cat         TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_serv_perf_cat_before  TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_serv_perf_cat_pernode TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_node                  TYPE /hec1/t_data_app_node_ct,
          lt_app_serv_inst             TYPE /hec1/t_data_app_serv_inst_ct,
          lt_app_server                TYPE /hec1/t_data_app_serv_ct,
          lt_app_storage_qty           TYPE /hec1/t_data_app_storageqty_ct,
          lt_act_param                 TYPE /hec1/t_act_create_app_qty,
          lt_act_param_server_key      TYPE /bobf/t_frw_key,
          lt_act_param_server          TYPE /hec1/t_act_update_app_server,
          lt_act_param_node            TYPE /hec1/t_act_update_app_node,
          lt_act_param_succ            TYPE /hec1/t_act_set_success_predec,
          lt_phase                     TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing         TYPE TABLE OF /hec1/s_act_phase_inherit,
          lt_range                     TYPE RANGE OF string.

    CLEAR: eo_message,
           et_failed_key.

    "-----------------------------------
    " Get data
    "-----------------------------------
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_serv_perf_cat ).

    " Get App node (parent)
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_parent
                                      IMPORTING et_data        = lt_app_node ).

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
          WHEN /hec1/if_configuration_c=>sc_determination-app_server_perform_cat-create.

            " Get for each App master node
            " the App server performance category
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
                                                        it_key         = VALUE #( FOR wa_node IN lt_app_node
                                                                                 ( key = wa_node-key )                )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
                                              IMPORTING et_data        = lt_app_serv_perf_cat_pernode ).


            LOOP AT         lt_app_serv_perf_cat
            REFERENCE INTO DATA(lr_app_serv_perf_cat)
                     WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master.

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              lr_app_serv_perf_cat->hec_srv_perf_cat_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server_perf_cat(
                                                                                      iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                      iv_inf_provider_guid   = lr_dlvy_unit->hec_inf_provider_guid
                                                                                      iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_app_serv_perf_cat->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL )
                                                                                      iv_is_app_server       = abap_true ) )
                                                                    THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                    ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              lr_app_serv_perf_cat->hec_delete_visible = abap_true.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_app_serv_perf_cat->hec_srv_perf_cat_guid IS NOT INITIAL AND
                                                                             lr_app_serv_perf_cat->hec_phase_guid        IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete          ).

              IF lv_inst_status <> lr_app_serv_perf_cat->hec_instance_status.
                lr_app_serv_perf_cat->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_app_node[ key = lr_app_serv_perf_cat->parent_key ] TO FIELD-SYMBOL(<fs_app_node>).
              IF <fs_app_node> IS ASSIGNED.
                IF <fs_app_node>-hec_app_srv_perf_cat_qty IS NOT INITIAL AND
                  <fs_app_node>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_app_serv_perf_cat->hec_row_selectable.
                lr_app_serv_perf_cat->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " App server storage amount
              "-----------------------------------
              IF NOT lr_app_serv_perf_cat->hec_server_required = abap_false.
                INSERT VALUE #( key                    = lr_app_serv_perf_cat->key
                                parent_key             = lr_app_serv_perf_cat->parent_key
                                hec_storage_amount_qty = lr_app_serv_perf_cat->hec_storage_qty ) INTO TABLE lt_act_param.
              ENDIF.

              "-----------------------------------
              " Fill action table for setting
              " App server performance category
              " successor/predecessor
              "-----------------------------------
              DATA(lv_node_count) = REDUCE i( INIT x = 0
                                              FOR <l> IN lt_app_serv_perf_cat_pernode WHERE ( parent_key = lr_app_serv_perf_cat->parent_key )
                                              NEXT x = x + 1                                                                                  ).

              IF NOT line_exists( lt_act_param_succ[ key = lr_app_serv_perf_cat->parent_key ] ) AND lv_node_count > 1.
                TRY.
                    INSERT VALUE #( key                  = lr_app_serv_perf_cat->parent_key
                                    parent_key           = lt_app_node[ key = lr_app_serv_perf_cat->parent_key ]-parent_key
                                    hec_no_children_node = lv_node_count                                                    ) INTO TABLE lt_act_param_succ.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.

              "-----------------------------------
              " Modify App server storage amount
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_serv_perf_cat->key
                                   is_data = lr_app_serv_perf_cat ).

              ENDIF.

              UNASSIGN <fs_app_node>.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release,
                     lv_node_count.

            ENDLOOP.           " LOOP AT lt_app_serv_perf_cat REFERENCE INTO lr_app_serv_perf_cat.


            "-----------------------------------
            " Set successor/predecessor action
            " to GENERAL
            "-----------------------------------
            IF lt_act_param_succ IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_set_success_predec( lt_act_param_succ ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key  = /hec1/if_configuration_c=>sc_node-app_node
                                             assoc_key = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat )
                  it_key          = VALUE #( FOR wa_act_succ IN lt_act_param_succ
                                            ( key = wa_act_succ-key )    )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-set_success_predec )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

            ENDIF.

            "-----------------------------------
            " Set create App server storage
            " amount and create App server
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_qty( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_qty )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_server )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                                                                          ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_server_perform_cat-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_app_serv_perf_cat_before ).


            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get App Node
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_parent
                                              IMPORTING et_target_key  = DATA(lt_app_node_key)
                                                        et_data        = lt_app_node ).

            " Get App server instance
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
                                                        it_key         = lt_app_node_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_node-to_parent
                                              IMPORTING et_data        = lt_app_serv_inst ).

            " Get App Server
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_server
                                              IMPORTING et_data        = lt_app_server
                                                        et_target_key  = DATA(lt_app_server_key) ).

            " Get App Storage Qty
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_storage_amount
                                              IMPORTING et_data        = lt_app_storage_qty ).


            "-----------------------------------
            " Get server performance category
            "-----------------------------------
            DATA(lt_range_table) = VALUE /hec1/t_selection_range( FOR wa_spc IN lt_app_serv_perf_cat
                                                                ( option = /hec1/if_config_constants=>gc_range_option-eq
                                                                  sign   = /hec1/if_config_constants=>gc_range_sign-i
                                                                  low    = wa_spc-hec_srv_perf_cat_guid                   ) ).

            SELECT *                          "#EC CI_ALL_FIELDS_NEEDED
              FROM /hec1/i_appservperfcatbasic
             WHERE hec_apm_guid          = @lr_landscape->hec_apm_guid AND
                   hec_srv_perf_cat_guid IN @lt_range_table
              INTO TABLE @DATA(lt_serv_perf_cat).


            "-----------------------------------
            " Get server
            "-----------------------------------
            CLEAR lt_range_table.
            lt_range_table = VALUE /hec1/t_selection_range( FOR wa IN lt_app_serv_perf_cat
                                                           ( option = /hec1/if_config_constants=>gc_range_option-eq
                                                             sign   = /hec1/if_config_constants=>gc_range_sign-i
                                                             low    = wa-hec_srv_perf_cat_guid                   ) ).

            SELECT *                          "#EC CI_ALL_FIELDS_NEEDED
              FROM /hec1/i_serverbasic
             WHERE hec_apm_guid = @lr_landscape->hec_apm_guid AND
                   hec_srv_perf_cat_guid IN @lt_range_table
              INTO TABLE @DATA(lt_server_data).



            LOOP AT lt_app_serv_perf_cat REFERENCE INTO lr_app_serv_perf_cat.

              ASSIGN lt_app_serv_perf_cat_before[ key = lr_app_serv_perf_cat->key ] TO FIELD-SYMBOL(<fs_app_serv_perf_cat_before>).
              IF <fs_app_serv_perf_cat_before> IS ASSIGNED.
                "-----------------------------------
                " App server performance category
                " has changed
                "-----------------------------------
                IF lr_app_serv_perf_cat->hec_srv_perf_cat_guid IS NOT INITIAL                                          AND
                   lr_app_serv_perf_cat->hec_srv_perf_cat_guid <> <fs_app_serv_perf_cat_before>-hec_srv_perf_cat_guid.

                  " Set server RAM class and CPU
                  TRY.
                      DATA(ls_serv_perf_cat) = lt_serv_perf_cat[ hec_srv_perf_cat_guid = lr_app_serv_perf_cat->hec_srv_perf_cat_guid ].

                      lr_app_serv_perf_cat->hec_srv_perf_cat_descr = ls_serv_perf_cat-hec_srv_perf_cat_descr.
                      lr_app_serv_perf_cat->hec_srv_ram_class      = ls_serv_perf_cat-hec_srv_ram_class.
                      lr_app_serv_perf_cat->hec_srv_cpu_class      = ls_serv_perf_cat-hec_srv_cpu_class.
                      lr_app_serv_perf_cat->hec_tree_descr         = ls_serv_perf_cat-hec_srv_perf_cat_descr. "#EC CI_FLDEXT_OK[2215424]

                      lv_data_changed                              = abap_true.

                      " Set Value List Quantity
                      lr_app_serv_perf_cat->hec_srv_perf_cat_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server_perf_cat(
                                                                                              iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                              iv_inf_provider_guid   = lr_dlvy_unit->hec_inf_provider_guid
                                                                                              iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_app_serv_perf_cat->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL )
                                                                                              iv_is_app_server       = abap_true ) )
                                                                            THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                            ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                      IF lr_app_serv_perf_cat->hec_effort_required = abap_true.
                        " Get effort time based legoblock GUID
                        SELECT hec_ram_condition_op,
                               hec_ram_condition,
                               hec_timebased_effort_bb_guid
                          FROM /hec1/i_appservnodetbbbbasic
                         WHERE hec_apm_guid                   = @lr_landscape->hec_apm_guid                           AND
                               hec_apst_clustty_clustnty_guid = @lr_app_serv_perf_cat->hec_apst_clustty_clustnty_guid AND
                               hec_tier_cat_value             = @lr_app_serv_perf_cat->hec_tier_cat_value
                          INTO TABLE @DATA(lt_timebased_bb).


                        LOOP AT lt_timebased_bb ASSIGNING FIELD-SYMBOL(<fs_timebased_bb>).
                          DATA(lv_option) = SWITCH ddoption( <fs_timebased_bb>-hec_ram_condition_op
                                                             WHEN '<'  THEN 'LT'
                                                             WHEN '>'  THEN 'GT'
                                                             WHEN '='  THEN 'EQ'
                                                             WHEN '<=' THEN 'LE'
                                                             WHEN '>=' THEN 'GE'                      ).

                          INSERT VALUE #( sign   = 'I'
                                          option = lv_option
                                          low    = <fs_timebased_bb>-hec_ram_condition ) INTO TABLE lt_range.


                          IF lr_app_serv_perf_cat->hec_srv_ram_class IN lt_range.
                            DATA(lv_effort_bb_guid) = <fs_timebased_bb>-hec_timebased_effort_bb_guid.
                            EXIT. " >>>>>>>
                          ENDIF.
                        ENDLOOP.

                        IF lv_effort_bb_guid IS NOT INITIAL.
                          " Get the pricing
                          DATA(ls_price) = /hec1/cl_config_helper=>do_price_validation( iv_node_key          = is_ctx-node_key
                                                                                        it_key               = VALUE #( ( key = lr_app_serv_perf_cat->key ) )
                                                                                        io_read              = io_read
                                                                                        iv_effort_bb_guid    = lv_effort_bb_guid
                                                                                        iv_tier_is_dr_node   = lr_app_serv_perf_cat->hec_tier_is_dr_node
                                                                                        iv_dr_operating_mode = lr_app_serv_perf_cat->hec_dr_oper_mode_value ).

                          lr_app_serv_perf_cat->price = CORRESPONDING #( ls_price ).
                        ENDIF.
                      ENDIF. " IF lr_app_serv_perf_cat->hec_effort_required = abap_true.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  TRY.
                      DATA(lv_datacenter_guid) = lt_datacenter[ hec_node_datacenter = lr_app_serv_perf_cat->hec_tier_datacenter_guid ]-hec_datacenter_guid.

                      DATA(lt_server) = /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server( iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                                                   iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                                                                   iv_sec_datacenter_guid = lv_datacenter_guid
                                                                                                                   iv_srv_perf_cat_guid   = lr_app_serv_perf_cat->hec_srv_perf_cat_guid ).

                      "-----------------------------------
                      " Fill action table for Update
                      " App server
                      "-----------------------------------
                      IF lines( lt_server ) = 1.
                        INSERT VALUE #( key                  = lt_app_server[ parent_key = lr_app_serv_perf_cat->key ]-key
                                        parent_key           = lr_app_serv_perf_cat->key
                                        hec_ip_server_guid   = lt_server[ 1 ]-value
                                        do_update_app_server = abap_true                                                    ) INTO TABLE lt_act_param_server.
                      ENDIF.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  CLEAR: lv_datacenter_guid,
                         lt_server.
                ENDIF. " IF lr_app_serv_perf_cat->hec_srv_perf_cat_guid IS NOT INITIAL AND...


                "-----------------------------------
                " App server storage is added
                "-----------------------------------
                IF lr_app_serv_perf_cat->hec_storage_qty > <fs_app_serv_perf_cat_before>-hec_storage_qty.
                  "-----------------------------------
                  " Fill action table for create
                  " App server storage amount
                  "-----------------------------------
                  INSERT VALUE #( key                    = lr_app_serv_perf_cat->key
                                 parent_key             = lr_app_serv_perf_cat->parent_key
                                 hec_storage_amount_qty = lr_app_serv_perf_cat->hec_storage_qty - <fs_app_serv_perf_cat_before>-hec_storage_qty ) INTO TABLE lt_act_param.

                  "-----------------------------------
                  " Fill action table for create
                  " App server storage
                  "-----------------------------------
                  TRY.
                      " App Storage is added without any parameters necessary
                      INSERT CORRESPONDING #( lt_app_server[ parent_key = lr_app_serv_perf_cat->key ] ) INTO TABLE lt_act_param_server_key.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  " Success message
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_storage_added
                                                                 iv_severity = /bobf/cm_frw=>co_severity_success
                                                                 iv_attr1    = CONV #( lr_app_serv_perf_cat->hec_storage_qty -
                                                                               <fs_app_serv_perf_cat_before>-hec_storage_qty )
                                                       CHANGING  co_message  = eo_message ).

                  " Set flag for deleting subnodes of standby node
                  IF lr_app_serv_perf_cat->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha          AND
                     lr_app_serv_perf_cat->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                     lr_app_serv_perf_cat->hec_app_node_default          = abap_true.
                    lv_data_changed            = abap_true.
                    DATA(lv_delete_ha_subnode) = abap_true.
                  ENDIF.

                ELSEIF lr_app_serv_perf_cat->hec_storage_qty < <fs_app_serv_perf_cat_before>-hec_storage_qty
                   AND lr_app_serv_perf_cat->hec_storage_qty < lines( VALUE /hec1/t_data_app_storageqty_ct( FOR app_storage_qty IN lt_app_storage_qty
                                                                                                                WHERE ( parent_key = lr_app_serv_perf_cat->key )
                                                                                                               ( app_storage_qty ) ) ).
                  DATA(lv_attr_name) = /hec1/if_configuration_c=>sc_node_attribute-app_server_perform_cat-hec_storage_qty.

                  " Error message
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                 is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                               key      = lr_app_serv_perf_cat->key
                                                                                               attributes = VALUE #( ( lv_attr_name ) ) )
                                                       CHANGING  co_message         = eo_message ).

                  " Set node number to value before update
                  lr_app_serv_perf_cat->hec_storage_qty = <fs_app_serv_perf_cat_before>-hec_storage_qty.
                  lv_data_changed = abap_true.
                ENDIF. " IF ls_db_server_perf_cat-hec_dsp_storage_qty > ls_db_server_perf_cat_old-hec_dsp_storage_qty.

                "-----------------------------------
                " Phase has changed -
                " update phase and inherit phase assignment
                "-----------------------------------
                IF lr_app_serv_perf_cat->hec_phase_guid NE <fs_app_serv_perf_cat_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_app_serv_perf_cat->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                     lr_app_serv_perf_cat->hec_app_node_default          = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_app_serv_perf_cat->key
                                    hec_phase_guid_new = lr_app_serv_perf_cat->hec_phase_guid
                                    hec_phase_guid_old = <fs_app_serv_perf_cat_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_app_serv_perf_cat->hec_phase_changed = abap_true.
                  lv_data_changed                         = abap_true.

                  " Set flag for deleting subnodes of standby node
                  IF lr_app_serv_perf_cat->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha          AND
                     lr_app_serv_perf_cat->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                     lr_app_serv_perf_cat->hec_app_node_default          = abap_true.
                    lv_delete_ha_subnode = abap_true.
                  ENDIF.

                ENDIF. "phasing changed
              ENDIF. "if <fs_app_serv_perf_cat> is assigned.


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_app_serv_perf_cat->hec_srv_perf_cat_guid IS NOT INITIAL AND
                                                                       lr_app_serv_perf_cat->hec_phase_guid        IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete          ).

              IF lv_inst_status <> lr_app_serv_perf_cat->hec_instance_status.
                lr_app_serv_perf_cat->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Fill action table for delete
              " App server standby node subnodes
              " or relase standby node
              "-----------------------------------
              IF lr_app_serv_perf_cat->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha          AND
                 lr_app_serv_perf_cat->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                 lr_app_serv_perf_cat->hec_app_node_default          = abap_true                                                AND
                 lv_data_changed                                     = abap_true.

                IF NOT line_exists( lt_act_param_node[ key = lr_app_serv_perf_cat->parent_key ] ).
                  TRY.
                      INSERT VALUE #( key                  = lr_app_serv_perf_cat->parent_key
                                      parent_key           = lt_app_node[ key = lr_app_serv_perf_cat->parent_key ]-parent_key
                                      do_release_ha_node   = COND #( WHEN lr_app_serv_perf_cat->hec_instance_status         = /hec1/if_config_constants=>gc_instance_status-complete    AND
                                                                          <fs_app_serv_perf_cat_before>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                                     THEN abap_true
                                                                     ELSE abap_false                                                  )
                                      do_delete_ha_subnode = COND #( WHEN lr_app_serv_perf_cat->hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete OR
                                                                          lv_delete_ha_subnode                      = abap_true
                                                                     THEN abap_true
                                                                     ELSE abap_false                                                                                 ) ) INTO TABLE lt_act_param_node.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                ENDIF.
              ENDIF. " IF lr_app_serv_perf_cat->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha


              "-----------------------------------
              " Modify App server performance
              " category
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_serv_perf_cat->key
                                   is_data = lr_app_serv_perf_cat ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_delete_ha_subnode,
                     lv_attr_name,
                     lv_option,
                     lv_effort_bb_guid,
                     ls_serv_perf_cat,
                     ls_price,
                     lt_range,
                     lt_timebased_bb.

              UNASSIGN <fs_app_serv_perf_cat_before>.

            ENDLOOP.

            "-----------------------------------
            " Set Create App Server amount
            " and Storage action to
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_qty( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_qty )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param ).


              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-app_server )
                  it_key          = VALUE #( FOR wa_act_serv IN lt_act_param_server_key
                                            ( key = wa_act_serv-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_storage )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                                                                          ).

            ENDIF. "lt_act_param is not initial


            "-----------------------------------
            " Set update App Server action to
            " general
            "-----------------------------------
            IF lt_act_param_server IS NOT INITIAL.
              CLEAR me->mr_act_param_server.
              me->mr_act_param_server = NEW /hec1/t_act_update_app_server( lt_act_param_server ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act_server IN lt_act_param_server
                                            ( key = wa_act_server-parent_key )        )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_app_server )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_server ).
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
            " Set update App node action to
            " general
            "-----------------------------------
            IF lt_act_param_node IS NOT INITIAL.
              CLEAR me->mr_act_param_app_node.
              me->mr_act_param_app_node = NEW /hec1/t_act_update_app_node( lt_act_param_node ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-app_node )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param_node
                                              ( key = wa_act_node-key )     )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_app_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_app_node                                                                                                       ).
            ENDIF.


            " ***************************************************************************
            " Update mode after app node update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_server_perform_cat-update_after_node.

            LOOP AT lt_app_serv_perf_cat REFERENCE INTO lr_app_serv_perf_cat.
              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_app_node[ key = lr_app_serv_perf_cat->parent_key ] TO <fs_app_node>.

              IF <fs_app_node> IS ASSIGNED.
                IF <fs_app_node>-hec_app_srv_perf_cat_qty > 0          AND
                   <fs_app_node>-hec_row_selectable       = abap_true.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_app_serv_perf_cat->hec_row_selectable.
                lr_app_serv_perf_cat->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Update App server cluster type
              "-----------------------------------
              IF lr_app_serv_perf_cat->hec_app_cluster_type_value <> <fs_app_node>-hec_app_cluster_type_value.
                lr_app_serv_perf_cat->hec_app_cluster_type_value = <fs_app_node>-hec_app_cluster_type_value.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Modify App server performance
              " category
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_serv_perf_cat->key
                                   is_data = lr_app_serv_perf_cat ).
              ENDIF.

              UNASSIGN <fs_app_node>.
              CLEAR: lv_release,
                     lv_data_changed.
            ENDLOOP. " LOOP AT lt_app_serv_perf_cat

        ENDCASE.



      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_app_storage.

    DATA: lt_app_server            TYPE /hec1/t_data_app_serv_ct,
          lt_app_storage           TYPE /hec1/t_data_app_storage_ct,
          lt_app_storage_perserver TYPE /hec1/t_data_app_storage_ct,
          lt_app_storage_before    TYPE /hec1/t_data_app_storage_ct,
          lt_app_storage_succ      TYPE /hec1/t_data_app_storage_ct,
          lt_app_serv_perf_cat     TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_storage_qty       TYPE /hec1/t_data_app_storageqty_ct,
          lt_phase                 TYPE /hec1/t_data_phase_ct,
          lt_app_backup            TYPE /hec1/t_data_app_backup_ct,
          lt_act_param             TYPE /hec1/t_act_create_app_backup,
          lt_act_param_storage     TYPE /bobf/t_frw_key,
          lt_act_param_phasing     TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    "-----------------------------------
    " Get data
    "-----------------------------------
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_storage ).

    " Get App server (parent)
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_storage-to_parent
                                      IMPORTING et_data        = lt_app_server ).

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
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage-create.

            " Get for each App server the App storage
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server
                                                        it_key         = VALUE #( FOR wa_serv IN lt_app_server
                                                                                 ( key = wa_serv-key )                )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server-app_storage
                                              IMPORTING et_data        = lt_app_storage_perserver ).

            LOOP AT        lt_app_storage
            REFERENCE INTO DATA(lr_app_storage)
                     WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master.

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              lr_app_storage->hec_ip_storage_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_storage(
                                                                              iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                              iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                              iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_app_storage->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL ) ) )
                                                            THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                            ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              lr_app_storage->hec_delete_visible = abap_false.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_app_storage->hec_ip_storage_guid IS NOT INITIAL AND
                                                                             lr_app_storage->hec_phase_guid      IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_app_storage->hec_instance_status.
                lr_app_storage->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_app_server[ key = lr_app_storage->parent_key ] TO FIELD-SYMBOL(<fs_app_server>).
              IF <fs_app_server> IS ASSIGNED.
                IF <fs_app_server>-hec_ip_server_guid IS NOT INITIAL AND
                   <fs_app_server>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_app_storage->hec_row_selectable.
                lr_app_storage->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " App server storage backup
              "-----------------------------------
              IF lr_app_storage->hec_backup_relev_value = '01'. " mandantory
                INSERT VALUE #( key            = lr_app_storage->key
                                parent_key     = lr_app_storage->parent_key
                                hec_backup_qty = lr_app_storage->hec_backup_qty ) INTO TABLE lt_act_param.
              ENDIF.

              "-----------------------------------
              " Fill action table for setting
              " App server storage
              " successor/predecessor
              "-----------------------------------
              DATA(lv_node_count) = REDUCE i( INIT x = 0
                                              FOR <l> IN lt_app_storage_perserver WHERE ( parent_key = lr_app_storage->parent_key )
                                              NEXT x = x + 1                                                                        ).

              IF NOT line_exists( lt_act_param_storage[ key = lr_app_storage->key ] ) AND lv_node_count > 1.
                TRY.
                    INSERT VALUE #( key = lr_app_storage->key ) INTO TABLE lt_act_param_storage.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.

              "-----------------------------------
              " Modify App server storage
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_storage->key
                                   is_data = lr_app_storage ).
              ENDIF.

              UNASSIGN <fs_app_server>.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release,
                     lv_node_count.

            ENDLOOP.

            "-----------------------------------
            " Set create App server storage
            " backup action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_backup( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_backup )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

            ENDIF.

            "-----------------------------------
            " Set update App storage action
            " to GENERAL
            "-----------------------------------
            IF lt_act_param_storage IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-app_storage )
                  it_key          = lt_act_param_storage
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_app_storage )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                                                                          ).
            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_app_storage_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get App server (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_storage-to_parent
                                              IMPORTING et_data        = lt_app_server ).

            " Get Backup
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_storage-app_storage_backup
                                              IMPORTING et_data        = lt_app_backup ).


            LOOP AT lt_app_storage REFERENCE INTO lr_app_storage.

              ASSIGN lt_app_storage_before[ key = lr_app_storage->key ] TO FIELD-SYMBOL(<fs_app_storage_before>).
              IF <fs_app_storage_before> IS ASSIGNED.

                "-----------------------------------
                " App storage IP GUID has changed
                "-----------------------------------
                IF lr_app_storage->hec_ip_storage_guid IS NOT INITIAL AND
                  lr_app_storage->hec_ip_storage_guid <> <fs_app_storage_before>-hec_ip_storage_guid.

                  " since this is the parent there can only be one entry
                  TRY.
                      DATA(ls_app_server) = lt_app_server[ key = lr_app_storage->parent_key ].
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  SELECT SINGLE *
                    FROM /hec1/i_storagelbbasic
                   WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid            AND
                         hec_sec_datacenter_guid = @ls_app_server-hec_sec_datacenter_guid AND
                         hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid   AND
                         hec_ip_storage_guid     = @lr_app_storage->hec_ip_storage_guid
                    INTO @DATA(ls_storage).

                  SELECT SINGLE * FROM /hec1/c_cbp_lb "#EC CI_ALL_FIELDS_NEEDED
                     INTO @DATA(ls_pricing)
                    WHERE hec_price_lb = @ls_storage-hec_cb_pricing_lb_guid.

                  lr_app_storage->*                    = CORRESPONDING #( BASE ( lr_app_storage->* ) ls_pricing ).
                  lr_app_storage->hec_ip_storage_guid  = ls_storage-hec_ip_storage_guid.
                  lr_app_storage->hec_storage_descr    = ls_storage-hec_storage_descr.
                  lr_app_storage->hec_month_price_fee  = lr_app_storage->hec_storage_quantity * lr_app_storage->hec_month_price_eur.
                  lr_app_storage->hec_tree_descr       = ls_storage-hec_storage_descr. "#EC CI_FLDEXT_OK[2215424]

                  lv_data_changed = abap_true.

                  " Set Value List Quantity
                  lr_app_storage->hec_ip_storage_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_storage(
                                                                                  iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                  iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                                  iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_app_storage->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL ) ) )
                                                                THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                ENDIF. "ip storage has changed

                "-----------------------------------
                " App storage amount has changed
                "-----------------------------------
                IF lr_app_storage->hec_storage_quantity IS NOT INITIAL                                 AND
                   lr_app_storage->hec_storage_quantity <> <fs_app_storage_before>-hec_storage_quantity.
                  lr_app_storage->hec_month_price_fee = lr_app_storage->hec_storage_quantity * lr_app_storage->hec_month_price_eur.

                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " App storage backup quantity is added
                "-----------------------------------
                IF lr_app_storage->hec_backup_qty > <fs_app_storage_before>-hec_backup_qty.

                  INSERT VALUE #( key            = lr_app_storage->key
                                  parent_key     = lr_app_storage->parent_key
                                  hec_backup_qty = lr_app_storage->hec_backup_qty - <fs_app_storage_before>-hec_backup_qty ) INTO TABLE lt_act_param.

                  " Success message
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_backup_added
                                                                 iv_severity = /bobf/cm_frw=>co_severity_success
                                                                 iv_attr1    = CONV #( lr_app_storage->hec_backup_qty -
                                                                               <fs_app_storage_before>-hec_backup_qty )
                                                       CHANGING  co_message  = eo_message ).

                ELSEIF lr_app_storage->hec_backup_qty < <fs_app_storage_before>-hec_backup_qty
                  AND lr_app_storage->hec_backup_qty < lines( VALUE /hec1/t_data_app_backup_ct( FOR app_backup IN lt_app_backup
                                                                                                    WHERE ( parent_key = lr_app_storage->key )
                                                                                                    ( app_backup ) ) ).
                  DATA(lv_attr_name) = /hec1/if_configuration_c=>sc_node_attribute-solution-hec_tier_qty_nprod_level.

                  " Error message
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                 is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                               key      = lr_app_storage->key
                                                                                               attributes = VALUE #( ( lv_attr_name ) ) )
                                                       CHANGING  co_message         = eo_message ).

                  " Set node number to value before update
                  lr_app_storage->hec_backup_qty = <fs_app_storage_before>-hec_backup_qty.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Phase has changed - update phase and inherit phase assignment
                "-----------------------------------
                IF lr_app_storage->hec_phase_guid NE <fs_app_storage_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_app_storage->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                     lr_app_storage->hec_app_node_default          = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_app_storage->key
                                    hec_phase_guid_new = lr_app_storage->hec_phase_guid
                                    hec_phase_guid_old = <fs_app_storage_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_app_storage->hec_phase_changed = abap_true.
                  lv_data_changed                   = abap_true.

                ENDIF. "phasing changed
              ENDIF. "if <fs_app_storage_before> is assigned.


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_app_storage->hec_ip_storage_guid IS NOT INITIAL AND
                                                                       lr_app_storage->hec_phase_guid      IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_app_storage->hec_instance_status.
                lr_app_storage->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_storage->key
                                   is_data = lr_app_storage ).

              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     ls_app_server,
                     ls_pricing,
                     ls_storage.

              UNASSIGN <fs_app_storage_before>.

            ENDLOOP.

            "-----------------------------------
            " Set create App server storage
            " backup action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_backup( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_backup )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

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

            " ***************************************************************************
            " Update mode after server update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage-update_after_server.

            LOOP AT lt_app_storage REFERENCE INTO lr_app_storage.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_app_server[ key = lr_app_storage->parent_key ] TO <fs_app_server>.

              IF <fs_app_server> IS ASSIGNED.
                IF <fs_app_server>-hec_ip_server_guid IS NOT INITIAL AND
                   <fs_app_server>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              IF lr_app_storage->hec_row_selectable            <> lv_release.
                lr_app_storage->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Update App server cluster type
              "-----------------------------------
              IF lr_app_storage->hec_app_cluster_type_value <> <fs_app_server>-hec_app_cluster_type_value.
                lr_app_storage->hec_app_cluster_type_value = <fs_app_server>-hec_app_cluster_type_value.
                lv_data_changed = abap_true.
              ENDIF.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_storage->key
                                   is_data = lr_app_storage ).
              ENDIF.

              UNASSIGN <fs_app_server>.
              CLEAR: lv_release,
                     lv_data_changed.
            ENDLOOP. "  LOOP AT lt_app_storage
        ENDCASE.



      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_app_storage_amount.

    DATA: lt_app_storage_qty         TYPE /hec1/t_data_app_storageqty_ct,
          lt_app_storage_qty_per_spc TYPE /hec1/t_data_app_storageqty_ct,
          lt_app_serv_perf_cat       TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_node                TYPE /hec1/t_data_app_node_ct,
          lt_app_storage_qty_before  TYPE /hec1/t_data_app_storageqty_ct,
          lt_app_server              TYPE /hec1/t_data_app_serv_ct,
          lt_app_storage             TYPE /hec1/t_data_app_storage_ct,
          lt_phase                   TYPE /hec1/t_data_phase_ct,
          lt_app_storage_qty_succ    TYPE /hec1/t_data_app_storageqty_ct,
          lt_act_param_node          TYPE /hec1/t_act_update_app_node,
          lt_act_param_storage       TYPE /bobf/t_frw_key,
          lt_act_param_succ          TYPE /hec1/t_act_set_success_predec,
          lt_act_param_phasing       TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    "-----------------------------------
    " Get data
    "-----------------------------------
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_storage_qty ).

    " Get App server performance category (parent)
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_storage_amount-to_parent
                                      IMPORTING et_data        = lt_app_serv_perf_cat ).

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
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage_amount-create.

            " Get for each App server performance category
            " the App storage amounts
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                        it_key         = VALUE #( FOR wa_spc IN lt_app_serv_perf_cat
                                                                                 ( key = wa_spc-key )                )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_storage_amount
                                              IMPORTING et_data        = lt_app_storage_qty_per_spc ).


            LOOP AT        lt_app_storage_qty
            REFERENCE INTO DATA(lr_app_storage_qty)
                     WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master.

              lr_app_storage_qty->hec_delete_visible = abap_true.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_app_storage_qty->hec_phase_guid IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_app_storage_qty->hec_instance_status.
                lr_app_storage_qty->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.

                " If standby node exist
                IF lr_app_storage_qty->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha          AND
                   lr_app_storage_qty->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                   lr_app_storage_qty->hec_app_node_default          = abap_true                                                AND
                   lr_app_storage_qty->hec_instance_status           = /hec1/if_config_constants=>gc_instance_status-complete.

                  io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                              it_key         = VALUE #( ( key = lr_app_storage_qty->key ) )
                                                              iv_fill_data   = abap_false
                                                              iv_association = /hec1/if_configuration_c=>sc_association-app_storage_amount-to_def_master_node
                                                    IMPORTING et_target_key  = DATA(lt_key) ).

                  IF NOT line_exists( lt_act_param_node[ key = lt_key[ 1 ]-key ] ).
                    TRY.
                        INSERT VALUE #( key                = lt_key[ 1 ]-key
                                        do_release_ha_node = abap_true       ) INTO TABLE lt_act_param_node.
                      CATCH cx_sy_itab_line_not_found.
                    ENDTRY.
                  ENDIF.
                ENDIF.
              ENDIF. " IF lv_inst_status <> lr_app_storage_qty->hec_instance_status.


              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_app_serv_perf_cat[ key = lr_app_storage_qty->parent_key ] TO FIELD-SYMBOL(<fs_app_serv_perf_cat>).
              IF <fs_app_serv_perf_cat> IS ASSIGNED.
                IF <fs_app_serv_perf_cat>-hec_srv_perf_cat_guid IS NOT INITIAL AND
                   <fs_app_serv_perf_cat>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_app_storage_qty->hec_row_selectable.
                lr_app_storage_qty->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for setting
              " App server storage amount
              " successor/predecessor
              "-----------------------------------
              DATA(lv_node_count) = REDUCE i( INIT x = 0
                                              FOR <l> IN lt_app_storage_qty_per_spc WHERE ( parent_key = lr_app_storage_qty->parent_key )
                                              NEXT x = x + 1                                                                              ).

              IF NOT line_exists( lt_act_param_succ[ key = lr_app_storage_qty->parent_key ] ) AND lv_node_count > 1.
                TRY.
                    INSERT VALUE #( key         = lr_app_storage_qty->parent_key
                                    parent_key  = lt_app_serv_perf_cat[ key = lr_app_storage_qty->parent_key ]-parent_key
                                    hec_no_children_node = lv_node_count                                                  ) INTO TABLE lt_act_param_succ.
                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.


              "-----------------------------------
              " Modify App storage amount
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_storage_qty->key
                                   is_data = lr_app_storage_qty ).
              ENDIF.

              UNASSIGN <fs_app_serv_perf_cat>.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release,
                     lv_node_count.

            ENDLOOP.


            "-----------------------------------
            " Set update App node action to
            " general
            "-----------------------------------
            IF lt_act_param_node IS NOT INITIAL.
              CLEAR me->mr_act_param_app_node.
              me->mr_act_param_app_node = NEW /hec1/t_act_update_app_node( lt_act_param_node ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-app_node )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param_node
                                              ( key = wa_act_node-key )     )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_app_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_app_node                                                                                                       ).
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
                                             node_key  = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                             assoc_key = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_storage_amount )
                  it_key          = VALUE #( FOR wa_act_succ IN lt_act_param_succ
                                            ( key = wa_act_succ-key )    )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-set_success_predec )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

            ENDIF.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage_amount-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_app_storage_qty_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_storage_amount-to_parent
                                              IMPORTING et_target_key  = DATA(lt_app_serv_pc_key) ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                        it_key         = lt_app_serv_pc_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_server
                                              IMPORTING et_target_key  = DATA(lt_app_serv_key)
                                                        et_key_link    = DATA(lt_perf_cat_to_serv_link) ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server
                                                        it_key         = lt_app_serv_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server-app_storage
                                              IMPORTING et_target_key  = DATA(lt_app_storage_key)
                                                        et_key_link    = DATA(lt_serv_to_storage_link)
                                                        et_data        = lt_app_storage ).

            LOOP AT lt_app_storage_qty REFERENCE INTO lr_app_storage_qty.

              ASSIGN lt_app_storage_qty_before[ key = lr_app_storage_qty->key ] TO FIELD-SYMBOL(<fs_app_storage_qty_before>).
              IF <fs_app_storage_qty_before> IS ASSIGNED.
                "-----------------------------------
                " Physical, virtual or additional storage
                " has changed
                "-----------------------------------
                IF lr_app_storage_qty->hec_asq_main_stor_qty_virtual <> <fs_app_storage_qty_before>-hec_asq_main_stor_qty_virtual OR
                   lr_app_storage_qty->hec_asq_additional_stor_qty   <> <fs_app_storage_qty_before>-hec_asq_additional_stor_qty   OR
                   lr_app_storage_qty->hec_successor_guid            <> <fs_app_storage_qty_before>-hec_successor_guid            OR
                   lr_app_storage_qty->hec_predecessor_guid          <> <fs_app_storage_qty_before>-hec_predecessor_guid.

                  lr_app_storage_qty->hec_tree_descr = |{ lr_app_storage_qty->hec_asq_main_stor_qty_virtual } + { lr_app_storage_qty->hec_asq_additional_stor_qty } [GiB] |.
                  lv_data_changed = abap_true.

                  " Storage needs to be adjusted
                  LOOP AT lt_serv_to_storage_link REFERENCE INTO DATA(lr_serv_to_storage_link)
                    WHERE source_key = lt_perf_cat_to_serv_link[ source_key = lr_app_storage_qty->parent_key ]-target_key.

                    INSERT VALUE #( key = lr_serv_to_storage_link->target_key ) INTO TABLE lt_act_param_storage.

                  ENDLOOP.

                  " Set flag for deleting subnodes of standby node
                  IF lr_app_storage_qty->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha          AND
                     lr_app_storage_qty->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                     lr_app_storage_qty->hec_app_node_default          = abap_true.
                    DATA(lv_delete_ha_subnode) = abap_true.
                  ENDIF.
                ENDIF. "storage changed

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_app_storage_qty->hec_phase_guid NE <fs_app_storage_qty_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_app_storage_qty->key
                                  hec_phase_guid_new = lr_app_storage_qty->hec_phase_guid
                                  hec_phase_guid_old = <fs_app_storage_qty_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_app_storage_qty->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                  " Set flag for deleting subnodes of standby node
                  IF lr_app_storage_qty->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha          AND
                     lr_app_storage_qty->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                     lr_app_storage_qty->hec_app_node_default          = abap_true.
                    lv_delete_ha_subnode = abap_true.
                  ENDIF.
                ENDIF. "phasing changed

              ENDIF. " if <fs_app_storage_qty_before> is assigned
              " end of before <-> after comparison

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_app_storage_qty->hec_phase_guid IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_app_storage_qty->hec_instance_status.
                lr_app_storage_qty->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for delete
              " App server standby node subnodes
              " or relase standby node
              "-----------------------------------
              IF lr_app_storage_qty->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha          AND
                 lr_app_storage_qty->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                 lr_app_storage_qty->hec_app_node_default          = abap_true                                                AND
                 lv_data_changed                                   = abap_true.

                " Only one master node per storage amount can exist
                io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                            it_key         = VALUE #( ( key = lr_app_storage_qty->key ) )
                                                            iv_fill_data   = abap_false
                                                            iv_association = /hec1/if_configuration_c=>sc_association-app_storage_amount-to_def_master_node
                                                  IMPORTING et_target_key  = lt_key ).

                IF NOT line_exists( lt_act_param_node[ key = lt_key[ 1 ]-key ] ).
                  TRY.
                      INSERT VALUE #( key                  = lt_key[ 1 ]-key
                                      parent_key           = space
                                      do_release_ha_node   = COND #( WHEN lr_app_storage_qty->hec_instance_status         = /hec1/if_config_constants=>gc_instance_status-complete    AND
                                                                          <fs_app_storage_qty_before>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                                     THEN abap_true
                                                                     ELSE abap_false                                                  )
                                      do_delete_ha_subnode = COND #( WHEN lr_app_storage_qty->hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete OR
                                                                          lv_delete_ha_subnode                    = abap_true
                                                                     THEN abap_true
                                                                     ELSE abap_false                                                                                 ) ) INTO TABLE lt_act_param_node.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                ENDIF.
              ENDIF. " IF lr_app_serv_perf_cat->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha


              "-----------------------------------
              " Modify
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_storage_qty->key
                                   is_data = lr_app_storage_qty ).
              ENDIF.

              UNASSIGN <fs_app_storage_qty_before>.
              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_delete_ha_subnode,
                     lt_key.

            ENDLOOP. "LOOP AT lt_app_storage_qty REFERENCE INTO lr_app_storage_qty.


            "-----------------------------------
            " Set update App Storage action to
            " general
            "-----------------------------------
            IF lt_act_param_storage IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-app_storage )
                  it_key          = lt_act_param_storage
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_app_storage )
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
            " Set update App node action to
            " general
            "-----------------------------------
            IF lt_act_param_node IS NOT INITIAL.
              CLEAR me->mr_act_param_app_node.
              me->mr_act_param_app_node = NEW /hec1/t_act_update_app_node( lt_act_param_node ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-app_node )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param_node
                                              ( key = wa_act_node-key )     )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_app_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_app_node                                                                                                       ).
            ENDIF.


            " ***************************************************************************
            " Update mode after app server
            " performance category update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage_amount-update_after_serv_perf_cat.

            LOOP AT lt_app_storage_qty REFERENCE INTO lr_app_storage_qty.
              ASSIGN lt_app_serv_perf_cat[ key = lr_app_storage_qty->parent_key ] TO <fs_app_serv_perf_cat>.

              IF <fs_app_serv_perf_cat> IS ASSIGNED.
                IF <fs_app_serv_perf_cat>-hec_srv_perf_cat_guid IS NOT INITIAL AND
                   <fs_app_serv_perf_cat>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
*              IF lr_app_node->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
              IF lr_app_storage_qty->hec_row_selectable <> lv_release.
                lr_app_storage_qty->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

*              " Release instance for selection( standby node)
*              IF lr_app_storage_qty->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-standby                 AND
*                 me->check_standby_node_is_released( iv_is_app_server = abap_true
*                                                     iv_check_rule    = /hec1/if_bopf_constants=>gc_check_rule-storage_amount
*                                                     is_ctx           = is_ctx
*                                                     it_key           = it_key
*                                                     io_read          = io_read
*                                                     io_modify        = io_modify                                             ) = abap_true.
*
*                IF lr_app_node->hec_row_selectable <> lv_release.
*                  lr_app_node->hec_row_selectable = lv_release.
*                  lv_data_changed                 = abap_true.
*                ENDIF.
*              ENDIF.

              " Update App server cluster type
              IF lr_app_storage_qty->hec_app_cluster_type_value <> <fs_app_serv_perf_cat>-hec_app_cluster_type_value.
                lr_app_storage_qty->hec_app_cluster_type_value = <fs_app_serv_perf_cat>-hec_app_cluster_type_value.
                lv_data_changed = abap_true.
              ENDIF.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_storage_qty->key
                                   is_data = lr_app_storage_qty ).
              ENDIF.

              UNASSIGN <fs_app_serv_perf_cat>.
              CLEAR: lv_release,
                     lv_data_changed.
            ENDLOOP. " LOOP AT lt_app_storage_qty
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_app_storage_backup.

    DATA: lt_app_backup_before     TYPE /hec1/t_data_app_backup_ct,
          lt_app_backup            TYPE /hec1/t_data_app_backup_ct,
          lt_app_backup_perstorage TYPE /hec1/t_data_app_backup_ct,
          lt_app_storage           TYPE /hec1/t_data_app_storage_ct,
          lt_phase                 TYPE /hec1/t_data_phase_ct,
          lt_act_param_succ        TYPE /hec1/t_act_set_success_predec,
          lt_act_param_phasing     TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_backup ).

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
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage_backup-create.

            " Get App server storage (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_storage_backup-to_parent
                                              IMPORTING et_data        = lt_app_storage ).


            " Get for each App storage the App backup
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_storage
                                                        it_key         = VALUE #( FOR wa_node IN lt_app_storage
                                                                                 ( key = wa_node-key )          )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_storage-app_storage_backup
                                              IMPORTING et_data        = lt_app_backup_perstorage ).


            LOOP AT        lt_app_backup
            REFERENCE INTO DATA(lr_app_backup)
                     WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master.

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              lr_app_backup->hec_backup_class_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_backup(
                                                                               iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                               iv_tier_category_value = lr_app_backup->hec_tier_cat_value
                                                                               iv_is_app_backup       = abap_true ) )
                                                             THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                             ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              lr_app_backup->hec_delete_visible = abap_true.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_app_backup->hec_backup_class_guid IS NOT INITIAL AND
                                                                             lr_app_backup->hec_backup_size       IS NOT INITIAL AND
                                                                             lr_app_backup->hec_phase_guid        IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_app_backup->hec_instance_status.
                lr_app_backup->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.


              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_app_storage[ key = lr_app_backup->parent_key ] TO FIELD-SYMBOL(<fs_app_storage>).
              IF <fs_app_storage> IS ASSIGNED.
                IF <fs_app_storage>-hec_ip_storage_guid IS NOT INITIAL AND
                   <fs_app_storage>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
                UNASSIGN <fs_app_storage>.
              ENDIF.

              IF lv_release <> lr_app_backup->hec_row_selectable.
                lr_app_backup->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Fill action table for setting
              " App server storage backup
              " successor/predecessor
              "-----------------------------------
              DATA(lv_node_count) = REDUCE i( INIT x = 0
                                              FOR <l> IN lt_app_backup_perstorage WHERE ( parent_key = lr_app_backup->parent_key )
                                              NEXT x = x + 1                                                                       ).

              IF NOT line_exists( lt_act_param_succ[ key = lr_app_backup->parent_key ] ) AND lv_node_count > 1.
                TRY.
                    INSERT VALUE #( key                  = lr_app_backup->parent_key
                                    parent_key           = lt_app_storage[ key = lr_app_backup->parent_key ]-parent_key
                                    hec_no_children_node = lv_node_count                                                ) INTO TABLE lt_act_param_succ.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.


              "-----------------------------------
              " Modify
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_backup->key
                                   is_data = lr_app_backup ).
              ENDIF.

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
                                             node_key  = /hec1/if_configuration_c=>sc_node-app_storage
                                             assoc_key = /hec1/if_configuration_c=>sc_association-app_storage-app_storage_backup )
                  it_key          = VALUE #( FOR wa_act_succ IN lt_act_param_succ
                                            ( key = wa_act_succ-key )    )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-set_success_predec )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage_backup-update.

            " Data before update
            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_app_backup_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get App Storage
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_false
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_storage_backup-to_parent
                                              IMPORTING et_target_key  = DATA(lt_app_storage_key)
                                                        et_data        = lt_app_storage ).


            LOOP AT lt_app_backup REFERENCE INTO lr_app_backup.
              ASSIGN lt_app_backup_before[ key = lr_app_backup->key ] TO FIELD-SYMBOL(<fs_app_backup_before>).

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_app_backup->hec_backup_class_guid IS NOT INITIAL AND
                                                                       lr_app_backup->hec_backup_size       IS NOT INITIAL AND
                                                                       lr_app_backup->hec_phase_guid        IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_app_backup->hec_instance_status.
                lr_app_backup->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              IF <fs_app_backup_before> IS ASSIGNED.
                "-----------------------------------
                " Backup GUID has changed
                "-----------------------------------
                IF lr_app_backup->hec_backup_class_guid IS NOT INITIAL AND
                  lr_app_backup->hec_backup_class_guid <> <fs_app_backup_before>-hec_backup_class_guid.

                  " Get backup class and backup class pricing
                  /hec1/cl_config_action_helper=>/hec1/if_bopf_action_helper~get_backup_class_and_price( EXPORTING is_ctx                  = CORRESPONDING #( is_ctx )
                                                                                                                   it_key                  = VALUE #( ( key = lr_app_backup->key ) )
                                                                                                                   iv_app_server           = abap_true
                                                                                                                   iv_tier_category_value  = lr_app_backup->hec_tier_cat_value
                                                                                                                   iv_tier_datacenter_guid = lr_app_backup->hec_tier_datacenter_guid
                                                                                                                   iv_backup_class_guid    = lr_app_backup->hec_backup_class_guid
                                                                                                                   io_read                 = io_read
                                                                                                         IMPORTING es_backup_class         = DATA(ls_backup_class)
                                                                                                                   es_backup_pricing       = DATA(ls_backup_pricing) ).

                  lr_app_backup->price                      = CORRESPONDING #( ls_backup_pricing ).
                  lr_app_backup->hec_backup_class_guid      = ls_backup_class-hec_backup_class_guid.
                  lr_app_backup->hec_backup_class_descr     = ls_backup_class-hec_backup_class_descr.
                  lr_app_backup->hec_tree_descr             = ls_backup_class-hec_backup_class_descr. "#EC CI_FLDEXT_OK[2215424]
                  lr_app_backup->hec_backup_month_price_fee = lr_app_backup->hec_backup_size * lr_app_backup->hec_month_price_eur.

                  lv_data_changed                           = abap_true.

                  " Set Value List Quantity
                  lr_app_backup->hec_backup_class_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_backup(
                                                                                   iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                   iv_tier_category_value = lr_app_backup->hec_tier_cat_value
                                                                                   iv_is_app_backup       = abap_true ) )
                                                                 THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                 ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                ENDIF. " IF <fs_app_backup_before>-hec_backup_class_guid IS NOT INITIAL AND...

                "-----------------------------------
                " Backup size has changed
                "-----------------------------------
                IF lr_app_backup->hec_backup_size IS NOT INITIAL AND
                   lr_app_backup->hec_backup_size <> <fs_app_backup_before>-hec_backup_size.
                  lr_app_backup->hec_backup_month_price_fee = lr_app_backup->hec_backup_size * lr_app_backup->hec_month_price_eur.

                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Phase has changed
                "-----------------------------------
                IF lr_app_backup->hec_phase_guid NE <fs_app_backup_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_app_backup->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                     lr_app_backup->hec_app_node_default          = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_app_backup->key
                                    hec_phase_guid_new = lr_app_backup->hec_phase_guid
                                    hec_phase_guid_old = <fs_app_backup_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_app_backup->hec_phase_changed = abap_true.
                  lv_data_changed                  = abap_true.

                ENDIF. "phasing changed
              ENDIF. "IF <fs_app_backup_before> IS ASSIGNED.


              "-----------------------------------
              " Modify App backup
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_backup->key
                                   is_data = lr_app_backup ).
              ENDIF.

              UNASSIGN <fs_app_backup_before>.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     ls_backup_class,
                     ls_backup_pricing.
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
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage_backup-update_after_storage.

            " Get App server storage (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_storage_backup-to_parent
                                              IMPORTING et_data        = lt_app_storage ).


            LOOP AT lt_app_backup REFERENCE INTO lr_app_backup.
              ASSIGN lt_app_storage[ key = lr_app_backup->parent_key ] TO <fs_app_storage>.

              IF <fs_app_storage> IS ASSIGNED.
                "-----------------------------------
                " Release instance for selection
                "-----------------------------------
                IF <fs_app_storage>-hec_ip_storage_guid IS NOT INITIAL AND
                   <fs_app_storage>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.

                IF lv_release <> lr_app_backup->hec_row_selectable.
                  lr_app_backup->hec_row_selectable = lv_release.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Update App server cluster type
                "-----------------------------------
                IF lr_app_backup->hec_app_cluster_type_value <> <fs_app_storage>-hec_app_cluster_type_value.
                  lr_app_backup->hec_app_cluster_type_value = <fs_app_storage>-hec_app_cluster_type_value.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Modify App storage backup
                "-----------------------------------
                IF lv_data_changed = abap_true.
                  io_modify->update( iv_node = is_ctx-node_key
                                     iv_key  = lr_app_backup->key
                                     is_data = lr_app_backup ).
                ENDIF.
              ENDIF. "  IF <fs_app_storage> IS ASSIGNED.

              UNASSIGN <fs_app_storage>.

              CLEAR: lv_data_changed,
                     lv_release.
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
            " Determine App server instance node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_server_instance-create             OR
               /hec1/if_configuration_c=>sc_determination-app_server_instance-update             OR
               /hec1/if_configuration_c=>sc_determination-app_server_instance-update_after_tier.

            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_app_server_instance( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                             it_key        = it_key                           " Key Table
                                                             io_read       = io_read                          " Interface to Reading Data
                                                             io_modify     = io_modify                        " Interface to Change Data
                                                   IMPORTING eo_message    = eo_message                       " Message Object
                                                             et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_app_server_inst_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                            it_key        = it_key                           " Key Table
                                                            io_read       = io_read                          " Interface to Reading Data
                                                            io_modify     = io_modify                        " Interface to Change Data
                                                  IMPORTING eo_message    = eo_message                       " Message Object
                                                            et_failed_key = et_failed_key ).                 " Key Table
            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determine App node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_node-create                    OR
               /hec1/if_configuration_c=>sc_determination-app_node-update                    OR
               /hec1/if_configuration_c=>sc_determination-app_node-update_after_server_inst.

            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_app_node( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                  it_key        = it_key                           " Key Table
                                                  io_read       = io_read                          " Interface to Reading Data
                                                  io_modify     = io_modify                        " Interface to Change Data
                                        IMPORTING eo_message    = eo_message                       " Message Object
                                                  et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_app_node_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                     it_key        = it_key                           " Key Table
                                                     io_read       = io_read                          " Interface to Reading Data
                                                     io_modify     = io_modify                        " Interface to Change Data
                                           IMPORTING eo_message    = eo_message                       " Message Object
                                                     et_failed_key = et_failed_key ).                 " Key Table

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determine App server performance
            " category node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_server_perform_cat-create            OR
               /hec1/if_configuration_c=>sc_determination-app_server_perform_cat-update            OR
               /hec1/if_configuration_c=>sc_determination-app_server_perform_cat-update_after_node.

            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_app_server_perf_cat( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                             it_key        = it_key                           " Key Table
                                                             io_read       = io_read                          " Interface to Reading Data
                                                             io_modify     = io_modify                        " Interface to Change Data
                                                   IMPORTING eo_message    = eo_message                       " Message Object
                                                             et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_app_server_pc_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                          it_key        = it_key                           " Key Table
                                                          io_read       = io_read                          " Interface to Reading Data
                                                          io_modify     = io_modify                        " Interface to Change Data
                                                IMPORTING eo_message    = eo_message                       " Message Object
                                                          et_failed_key = et_failed_key ).                 " Key Table

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determine App storage amount
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage_amount-create                     OR
               /hec1/if_configuration_c=>sc_determination-app_storage_amount-update                     OR
               /hec1/if_configuration_c=>sc_determination-app_storage_amount-update_after_serv_perf_cat.

            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_app_storage_amount( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                            it_key        = it_key                           " Key Table
                                                            io_read       = io_read                          " Interface to Reading Data
                                                            io_modify     = io_modify                        " Interface to Change Data
                                                  IMPORTING eo_message    = eo_message                       " Message Object
                                                            et_failed_key = et_failed_key ).                 " Key Table


              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_app_storage_amoun_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                              it_key        = it_key                           " Key Table
                                                              io_read       = io_read                          " Interface to Reading Data
                                                              io_modify     = io_modify                        " Interface to Change Data
                                                    IMPORTING eo_message    = eo_message                       " Message Object
                                                              et_failed_key = et_failed_key ).                 " Key Table

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determine App server
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_server-create                     OR
               /hec1/if_configuration_c=>sc_determination-app_server-update                     OR
               /hec1/if_configuration_c=>sc_determination-app_server-update_after_serv_perf_cat.

            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_app_server( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                    it_key        = it_key                           " Key Table
                                                    io_read       = io_read                          " Interface to Reading Data
                                                    io_modify     = io_modify                        " Interface to Change Data
                                          IMPORTING eo_message    = eo_message                       " Message Object
                                                    et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_app_server_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                       it_key        = it_key                           " Key Table
                                                       io_read       = io_read                          " Interface to Reading Data
                                                       io_modify     = io_modify                        " Interface to Change Data
                                             IMPORTING eo_message    = eo_message                       " Message Object
                                                       et_failed_key = et_failed_key ).                 " Key Table

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determine App storage
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage-create              OR
               /hec1/if_configuration_c=>sc_determination-app_storage-update              OR
               /hec1/if_configuration_c=>sc_determination-app_storage-update_after_server.

            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_app_storage( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                     it_key        = it_key                           " Key Table
                                                     io_read       = io_read                          " Interface to Reading Data
                                                     io_modify     = io_modify                        " Interface to Change Data
                                           IMPORTING eo_message    = eo_message                       " Message Object
                                                     et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_app_storage_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                        it_key        = it_key                           " Key Table
                                                        io_read       = io_read                          " Interface to Reading Data
                                                        io_modify     = io_modify                        " Interface to Change Data
                                              IMPORTING eo_message    = eo_message                       " Message Object
                                                        et_failed_key = et_failed_key ).                 " Key Table

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determine App storage backup
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage_backup-create               OR
               /hec1/if_configuration_c=>sc_determination-app_storage_backup-update               OR
               /hec1/if_configuration_c=>sc_determination-app_storage_backup-update_after_storage.

            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_app_storage_backup( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                            it_key        = it_key                           " Key Table
                                                            io_read       = io_read                          " Interface to Reading Data
                                                            io_modify     = io_modify                        " Interface to Change Data
                                                  IMPORTING eo_message    = eo_message                       " Message Object
                                                            et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_app_storage_backu_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
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
        " Determine App server instance node
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_determination-app_server_instance-create.


        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_app_serv_inst IN CORRESPONDING /hec1/t_data_app_serv_inst_ct( <lt_data> )
                                                                                                    ( VALUE #( parent_node_key     = wa_app_serv_inst-parent_key
                                                                                                               node_key            = wa_app_serv_inst-key
                                                                                                               hec_instance_status = wa_app_serv_inst-hec_instance_status
                                                                                                               hec_tree_descr      = wa_app_serv_inst-hec_tree_descr
                                                                                                               hec_row_selectable  = wa_app_serv_inst-hec_row_selectable
                                                                                                               hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-app_serv_inst
                                                                                                               hec_phase_guid      = wa_app_serv_inst-hec_phase_guid
                                                                                                               hec_delete_visible  = wa_app_serv_inst-hec_delete_visible
                                                                                                               crea_date_time      = wa_app_serv_inst-crea_date_time
                                                                                                               change_request      = wa_app_serv_inst-change_request ) ) ) ).

      WHEN     /hec1/if_configuration_c=>sc_determination-app_server_instance-update
        OR     /hec1/if_configuration_c=>sc_determination-app_server_instance-update_after_tier.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_app_serv_inst IN CORRESPONDING /hec1/t_data_app_serv_inst_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_app_serv_inst-parent_key
                                                                                                                    node_key            = wa_app_serv_inst-key
                                                                                                                    hec_instance_status = wa_app_serv_inst-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_app_serv_inst-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_app_serv_inst-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-app_serv_inst
                                                                                                                    hec_phase_guid      = wa_app_serv_inst-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_app_serv_inst-hec_delete_visible
                                                                                                                    change_request      = wa_app_serv_inst-change_request ) ) ) ).

        " **********************************
        " Determine App node
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_determination-app_node-create.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_app_node IN CORRESPONDING /hec1/t_data_app_node_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_app_node-parent_key
                                                                                                                    node_key            = wa_app_node-key
                                                                                                                    hec_instance_status = wa_app_node-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_app_node-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_app_node-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-app_node
                                                                                                                    hec_phase_guid      = wa_app_node-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_app_node-hec_delete_visible
                                                                                                                    crea_date_time      = wa_app_node-crea_date_time
                                                                                                                    hec_sort_order      = SWITCH #( wa_app_node-hec_app_clust_node_type_value
                                                                                                                                                    WHEN /hec1/if_config_constants=>gc_db_clust_node_type-master
                                                                                                                                                    THEN 1
                                                                                                                                                    WHEN /hec1/if_config_constants=>gc_db_clust_node_type-standby
                                                                                                                                                    THEN 2
                                                                                                                                                    WHEN /hec1/if_config_constants=>gc_db_clust_node_type-worker
                                                                                                                                                    THEN 3 )
                                                                                                                    change_request      = wa_app_node-change_request ) ) ) ).
      WHEN     /hec1/if_configuration_c=>sc_determination-app_node-update
        OR     /hec1/if_configuration_c=>sc_determination-app_node-update_after_server_inst.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_app_node IN CORRESPONDING /hec1/t_data_app_node_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_app_node-parent_key
                                                                                                                    node_key            = wa_app_node-key
                                                                                                                    hec_instance_status = wa_app_node-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_app_node-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_app_node-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-app_node
                                                                                                                    hec_phase_guid      = wa_app_node-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_app_node-hec_delete_visible
                                                                                                                    hec_sort_order      = SWITCH #( wa_app_node-hec_app_clust_node_type_value
                                                                                                                                                    WHEN /hec1/if_config_constants=>gc_app_clust_node_type-master
                                                                                                                                                    THEN 1
                                                                                                                                                    WHEN /hec1/if_config_constants=>gc_app_clust_node_type-standby
                                                                                                                                                    THEN 2
                                                                                                                                                    WHEN /hec1/if_config_constants=>gc_app_clust_node_type-worker
                                                                                                                                                    THEN 3  )
                                                                                                                    change_request      = wa_app_node-change_request ) ) ) ).



        " **********************************
        " Determine App server performance
        " category node
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_determination-app_server_perform_cat-create.


        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_app_serv_pc IN CORRESPONDING /hec1/t_data_app_serv_pc_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_app_serv_pc-parent_key
                                                                                                                    node_key            = wa_app_serv_pc-key
                                                                                                                    hec_instance_status = wa_app_serv_pc-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_app_serv_pc-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_app_serv_pc-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-app_serv_pc
                                                                                                                    hec_phase_guid      = wa_app_serv_pc-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_app_serv_pc-hec_delete_visible
                                                                                                                    hec_successor_guid  = wa_app_serv_pc-hec_successor_guid
                                                                                                                    crea_date_time      = wa_app_serv_pc-crea_date_time
                                                                                                                    change_request      = wa_app_serv_pc-change_request ) ) ) ).


      WHEN     /hec1/if_configuration_c=>sc_determination-app_server_perform_cat-update
        OR     /hec1/if_configuration_c=>sc_determination-app_server_perform_cat-update_after_node.
        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_app_serv_pc IN CORRESPONDING /hec1/t_data_app_serv_pc_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_app_serv_pc-parent_key
                                                                                                                    node_key            = wa_app_serv_pc-key
                                                                                                                    hec_instance_status = wa_app_serv_pc-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_app_serv_pc-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_app_serv_pc-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-app_serv_pc
                                                                                                                    hec_phase_guid      = wa_app_serv_pc-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_app_serv_pc-hec_delete_visible
                                                                                                                    hec_successor_guid  = wa_app_serv_pc-hec_successor_guid
                                                                                                                    change_request      = wa_app_serv_pc-change_request ) ) ) ).

        " **********************************
        " Determine App storage amount
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_determination-app_storage_amount-create.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_app_storage_qty IN CORRESPONDING /hec1/t_data_app_storageqty_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_app_storage_qty-parent_key
                                                                                                                    node_key            = wa_app_storage_qty-key
                                                                                                                    hec_instance_status = wa_app_storage_qty-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_app_storage_qty-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_app_storage_qty-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-app_storage_qty
                                                                                                                    hec_phase_guid      = wa_app_storage_qty-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_app_storage_qty-hec_delete_visible
                                                                                                                    hec_successor_guid  = wa_app_storage_qty-hec_successor_guid
                                                                                                                    crea_date_time      = wa_app_storage_qty-crea_date_time
                                                                                                                    change_request      = wa_app_storage_qty-change_request ) ) ) ).



      WHEN     /hec1/if_configuration_c=>sc_determination-app_storage_amount-update
        OR     /hec1/if_configuration_c=>sc_determination-app_storage_amount-update_after_serv_perf_cat.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_app_storage_qty IN CORRESPONDING /hec1/t_data_app_storageqty_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_app_storage_qty-parent_key
                                                                                                                    node_key            = wa_app_storage_qty-key
                                                                                                                    hec_instance_status = wa_app_storage_qty-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_app_storage_qty-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_app_storage_qty-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-app_storage_qty
                                                                                                                    hec_phase_guid      = wa_app_storage_qty-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_app_storage_qty-hec_delete_visible
                                                                                                                    hec_successor_guid  = wa_app_storage_qty-hec_successor_guid
                                                                                                                    change_request      = wa_app_storage_qty-change_request ) ) ) ).

        " **********************************
        " Determine App server
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_determination-app_server-create.
        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_app_server IN CORRESPONDING /hec1/t_data_app_serv_ct( <lt_data> )
                                                                                                 ( VALUE #( parent_node_key     = wa_app_server-parent_key
                                                                                                            node_key            = wa_app_server-key
                                                                                                            hec_instance_status = wa_app_server-hec_instance_status
                                                                                                            hec_tree_descr      = wa_app_server-hec_tree_descr
                                                                                                            hec_row_selectable  = wa_app_server-hec_row_selectable
                                                                                                            hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-app_server
                                                                                                            hec_phase_guid      = wa_app_server-hec_phase_guid
                                                                                                            hec_delete_visible  = wa_app_server-hec_delete_visible
                                                                                                            crea_date_time      = wa_app_server-crea_date_time
                                                                                                            change_request      = wa_app_server-change_request ) ) ) ).

      WHEN     /hec1/if_configuration_c=>sc_determination-app_server-update
        OR     /hec1/if_configuration_c=>sc_determination-app_server-update_after_serv_perf_cat.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_app_server IN CORRESPONDING /hec1/t_data_app_serv_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_app_server-parent_key
                                                                                                                    node_key            = wa_app_server-key
                                                                                                                    hec_instance_status = wa_app_server-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_app_server-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_app_server-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-app_server
                                                                                                                    hec_phase_guid      = wa_app_server-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_app_server-hec_delete_visible
                                                                                                                    change_request      = wa_app_server-change_request ) ) ) ).

        " **********************************
        " Determine App storage
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_determination-app_storage-create.
        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_app_storage IN CORRESPONDING /hec1/t_data_app_storage_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_app_storage-parent_key
                                                                                                                    node_key            = wa_app_storage-key
                                                                                                                    hec_instance_status = wa_app_storage-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_app_storage-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_app_storage-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-app_storage
                                                                                                                    hec_phase_guid      = wa_app_storage-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_app_storage-hec_delete_visible
                                                                                                                    hec_successor_guid  = wa_app_storage-hec_successor_guid
                                                                                                                    crea_date_time      = wa_app_storage-crea_date_time
                                                                                                                    change_request      = wa_app_storage-change_request ) ) ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-app_storage-update
        OR /hec1/if_configuration_c=>sc_determination-app_storage-update_after_server.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_app_storage IN CORRESPONDING /hec1/t_data_app_storage_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_app_storage-parent_key
                                                                                                                    node_key            = wa_app_storage-key
                                                                                                                    hec_instance_status = wa_app_storage-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_app_storage-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_app_storage-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-app_storage
                                                                                                                    hec_phase_guid      = wa_app_storage-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_app_storage-hec_delete_visible
                                                                                                                    hec_successor_guid  = wa_app_storage-hec_successor_guid
                                                                                                                    change_request      = wa_app_storage-change_request ) ) ) ).

        " **********************************
        " Determine App storage backup
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_determination-app_storage_backup-create.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_s IN CORRESPONDING /hec1/t_data_app_backup_ct( <lt_data> )
                                                                                                  ( VALUE #( parent_node_key     = wa_s-parent_key
                                                                                                             node_key            = wa_s-key
                                                                                                             hec_instance_status = wa_s-hec_instance_status
                                                                                                             hec_tree_descr      = wa_s-hec_tree_descr
                                                                                                             hec_row_selectable  = wa_s-hec_row_selectable
                                                                                                             hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-app_backup
                                                                                                             hec_phase_guid      = wa_s-hec_phase_guid
                                                                                                             hec_delete_visible  = wa_s-hec_delete_visible
                                                                                                             hec_successor_guid  = wa_s-hec_successor_guid
                                                                                                             crea_date_time      = wa_s-crea_date_time
                                                                                                             change_request      = wa_s-change_request ) ) ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-app_storage_backup-update
        OR /hec1/if_configuration_c=>sc_determination-app_storage_backup-update_after_storage.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_s IN CORRESPONDING /hec1/t_data_app_backup_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_s-parent_key
                                                                                                                    node_key            = wa_s-key
                                                                                                                    hec_instance_status = wa_s-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_s-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_s-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-app_backup
                                                                                                                    hec_phase_guid      = wa_s-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_s-hec_delete_visible
                                                                                                                    hec_successor_guid  = wa_s-hec_successor_guid
                                                                                                                    change_request      = wa_s-change_request ) ) ) ).

    ENDCASE.
  ENDMETHOD.


  METHOD determine_app_node_cr.

    DATA: lt_app_serv_inst     TYPE /hec1/t_data_app_serv_inst_ct,
          lt_app_node          TYPE /hec1/t_data_app_node_ct,
          lt_app_node_before   TYPE /hec1/t_data_app_node_ct,
          lt_node_key          TYPE /bobf/t_frw_key,
          lt_phase             TYPE /hec1/t_data_phase_ct,
          lt_app_serv_pc       TYPE /hec1/t_data_app_serv_pc_ct,
          lt_act_param         TYPE /hec1/t_act_create_app_spc,
          lt_act_param_node    TYPE /hec1/t_act_update_app_node,
          lt_act_param_phasing TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_node ).

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
          WHEN /hec1/if_configuration_c=>sc_determination-app_node-create.

            " Get App server instance node (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_node-to_parent
                                              IMPORTING et_data        = lt_app_serv_inst ).

            "-----------------------------------
            " App master node
            "-----------------------------------
            LOOP AT        lt_app_node
            REFERENCE INTO DATA(lr_app_node)
                    WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master.

              lr_app_node->hec_delete_visible = abap_false.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_app_node->hec_app_srv_perf_cat_qty IS NOT INITIAL AND
                                                                             lr_app_node->hec_phase_guid           IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_app_node->hec_instance_status.
                lr_app_node->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_app_serv_inst[ key = lr_app_node->parent_key ] TO FIELD-SYMBOL(<fs_app_serv_inst>).
              IF <fs_app_serv_inst> IS ASSIGNED.
                IF <fs_app_serv_inst>-hec_operating_sys_guid IS NOT INITIAL AND
                   <fs_app_serv_inst>-hec_app_cluster_type_value IS NOT INITIAL AND
                   <fs_app_serv_inst>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lr_app_node->hec_row_selectable            <> lv_release                                               AND
                 lr_app_node->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master.
                lr_app_node->hec_row_selectable = lv_release.
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
                  is_node_data = lr_app_node
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              IF lv_data_changed = abap_false.
                lv_data_changed = lv_cr_data_changed.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " App server performance category
              "-----------------------------------
              IF NOT ( lr_app_node->hec_server_required = abap_false AND
                       lr_app_node->hec_effort_required = abap_false     ).
                INSERT VALUE #( key             = lr_app_node->key
                                parent_key      = lr_app_node->parent_key
                                hec_app_srv_perf_cat_qty = lr_app_node->hec_app_srv_perf_cat_qty ) INTO TABLE lt_act_param.
              ENDIF.

              "-----------------------------------
              " Modify App server node
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_node->key
                                   is_data = lr_app_node ).

              ENDIF.

              UNASSIGN <fs_app_serv_inst>.
              CLEAR: lv_inst_status,
                     lv_release,
                     lv_data_changed.
            ENDLOOP.

            "-----------------------------------
            " App standby node
            "-----------------------------------
            LOOP AT        lt_app_node
            REFERENCE INTO lr_app_node
                     WHERE hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha           AND
                           hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-standby.

              lr_app_node->hec_delete_visible = abap_false.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_app_node->hec_app_srv_perf_cat_qty IS NOT INITIAL AND
                                                                       lr_app_node->hec_phase_guid           IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_app_node->hec_instance_status.
                lr_app_node->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Release selection standby node
              "-----------------------------------
              " Check master node is complete configered
              " ( including sub nodes: server performance category and storage amount )
              DATA(lv_complete) = /hec1/cl_bopf_config_validat_h=>check_master_node_is_complete( iv_is_app_server = abap_true
                                                                                                 iv_check_rule    = /hec1/if_bopf_constants=>gc_check_rule-node
                                                                                                 is_ctx           = is_ctx
                                                                                                 it_key           = VALUE #( ( key = lr_app_node->key ) )
                                                                                                 io_read          = io_read ).

              IF ( lv_complete                     = abap_true AND
                   lr_app_node->hec_row_selectable = abap_false    ) OR
                 ( lv_complete                     = abap_false AND
                   lr_app_node->hec_row_selectable = abap_true     ).

                lr_app_node->hec_row_selectable = COND #( WHEN lv_complete = abap_true
                                                          THEN abap_true
                                                          ELSE abap_false              ).
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify App server node
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_node->key
                                   is_data = lr_app_node ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_complete,
                     lv_data_changed.
            ENDLOOP.


            "-----------------------------------
            " Set create App server performance
            " category action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_spc( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_spc )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_node-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_app_node_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
                                              IMPORTING et_data        = lt_app_serv_pc ).

            LOOP AT lt_app_node REFERENCE INTO lr_app_node.

              ASSIGN lt_app_node_before[ key = lr_app_node->key ] TO FIELD-SYMBOL(<fs_app_node_before>).
              IF <fs_app_node_before> IS ASSIGNED.

                "-----------------------------------
                " App server performance category added
                "-----------------------------------
                IF <fs_app_node_before>-hec_app_srv_perf_cat_qty < lr_app_node->hec_app_srv_perf_cat_qty.
                  CASE lr_app_node->hec_app_clust_node_type_value.

                    WHEN /hec1/if_config_constants=>gc_app_clust_node_type-master.
                      "-----------------------------------
                      " Fill action table for create
                      " App server performance category
                      "-----------------------------------
                      INSERT VALUE #( key             = lr_app_node->key
                                      parent_key      = lr_app_node->parent_key
                                      hec_app_srv_perf_cat_qty = lr_app_node->hec_app_srv_perf_cat_qty - <fs_app_node_before>-hec_app_srv_perf_cat_qty ) INTO TABLE lt_act_param.

                      " Success message
                      /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_serv_perf_cat_added
                                                                     iv_severity = /bobf/cm_frw=>co_severity_success
                                                                     iv_attr1    = CONV #( lr_app_node->hec_app_srv_perf_cat_qty -
                                                                                   <fs_app_node_before>-hec_app_srv_perf_cat_qty )
                                                           CHANGING  co_message  = eo_message ).

                      " Set flag for deleting subnodes of standby node
                      IF lr_app_node->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha          AND
                         lr_app_node->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                         lr_app_node->hec_master_default            = abap_true.
                        lv_data_changed            = abap_true.
                        DATA(lv_delete_ha_subnode) = abap_true.
                      ENDIF.
                  ENDCASE.

                ELSEIF <fs_app_node_before>-hec_app_srv_perf_cat_qty > lr_app_node->hec_app_srv_perf_cat_qty
                  AND lr_app_node->hec_app_srv_perf_cat_qty < lines( VALUE /hec1/t_data_app_serv_pc_ct( FOR app_serv_pc IN lt_app_serv_pc
                                                                                                        WHERE ( parent_key = lr_app_node->key )
                                                                                                        ( app_serv_pc ) ) ).
                  DATA(lv_attr_name) = /hec1/if_configuration_c=>sc_node_attribute-app_node-hec_app_srv_perf_cat_qty.

                  " Error message
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                 is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                               key      = lr_app_node->key
                                                                                               attributes = VALUE #( ( lv_attr_name ) ) )
                                                       CHANGING  co_message         = eo_message ).

                  " Set node number to value before update
                  lr_app_node->hec_app_srv_perf_cat_qty = <fs_app_node_before>-hec_app_srv_perf_cat_qty.
                  lv_data_changed                       = abap_true.
                ENDIF. " IF ls_app_node_old-hec_app_srv_perf_cat_qty < ls_app_node-hec_app_srv_perf_cat_qty.

                "-----------------------------------
                " Phase has changed - update phase
                " and inherit phase assignment
                "-----------------------------------
                IF lr_app_node->hec_phase_guid <> <fs_app_node_before>-hec_phase_guid.

                  IF lr_app_node->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                     lr_app_node->hec_master_default            = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_app_node->key
                                    hec_phase_guid_new = lr_app_node->hec_phase_guid
                                    hec_phase_guid_old = <fs_app_node_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_app_node->hec_phase_changed = abap_true.
                  lv_data_changed                = abap_true.

                  " Set flag for deleting subnodes of standby node
                  IF lr_app_node->hec_app_cluster_type_value = /hec1/if_config_constants=>gc_app_clust_node-ha.
                    lv_delete_ha_subnode = abap_true.
                  ENDIF.
                ENDIF. "phasing changed
              ENDIF. "IF <fs_app_node_before> IS ASSIGNED.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_app_node->hec_app_srv_perf_cat_qty IS NOT INITIAL AND
                                                                       lr_app_node->hec_phase_guid           IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_app_node->hec_instance_status.
                lr_app_node->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Fill action table for delete
              " App server standby node subnodes
              " or relase standby node
              "-----------------------------------
              IF lr_app_node->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha          AND
                 lr_app_node->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                 lr_app_node->hec_master_default            = abap_true                                                AND
                 lv_data_changed                            = abap_true.

                IF NOT line_exists( lt_act_param_node[ key = lr_app_node->key ] ).
                  INSERT VALUE #( key                  = lr_app_node->key
                                  parent_key           = lr_app_node->parent_key
                                  do_release_ha_node   = COND #( WHEN lr_app_node->hec_instance_status         = /hec1/if_config_constants=>gc_instance_status-complete    AND
                                                                      <fs_app_node_before>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                                 THEN abap_true
                                                                 ELSE abap_false                                                  )
                                  do_delete_ha_subnode = COND #( WHEN lr_app_node->hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete OR
                                                                      lv_delete_ha_subnode             = abap_true
                                                                 THEN abap_true
                                                                 ELSE abap_false                                                                                        ) ) INTO TABLE lt_act_param_node.
                ENDIF.
              ENDIF. " IF lr_app_serv_perf_cat->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha


              "-----------------------------------
              " Modify App server node
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_node->key
                                   is_data = lr_app_node ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_attr_name,
                     lv_delete_ha_subnode.

              UNASSIGN <fs_app_node_before>.

            ENDLOOP.

            "-----------------------------------
            " Set create App server performance
            " ategory action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_spc( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_spc )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param    ).

            ENDIF.

            "-----------------------------------
            " Set Update Phasing
            " to general
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
            " Set update App node action to
            " general
            "-----------------------------------
            IF lt_act_param_node IS NOT INITIAL.
              CLEAR me->mr_act_param_app_node.
              me->mr_act_param_app_node = NEW /hec1/t_act_update_app_node( lt_act_param_node ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-app_node )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param_node
                                              ( key = wa_act_node-key )     )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_app_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_app_node                                                                                                       ).
            ENDIF.


            " ***************************************************************************
            " Update mode after app server
            " instance update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_node-update_after_server_inst.

            " Get App server instance
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_node-to_parent
                                              IMPORTING et_data        = lt_app_serv_inst ).



            LOOP AT lt_app_node REFERENCE INTO lr_app_node.
              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_app_serv_inst[ key = lr_app_node->parent_key ] TO <fs_app_serv_inst>.

              IF <fs_app_serv_inst> IS ASSIGNED.
                IF <fs_app_serv_inst>-hec_operating_sys_guid IS NOT INITIAL AND
                   <fs_app_serv_inst>-hec_app_cluster_type_value IS NOT INITIAL AND
                   <fs_app_serv_inst>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              IF lr_app_node->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                 lr_app_node->hec_row_selectable            <> lv_release.
                lr_app_node->hec_row_selectable = lv_release.
                lv_data_changed                 = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              " ( standby node)
              "-----------------------------------
              IF lr_app_node->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-standby AND
                 lr_app_node->hec_row_selectable            <> lv_release.

                IF lv_release                      = abap_false AND
                   lr_app_node->hec_row_selectable = abap_true.
                  lr_app_node->hec_row_selectable = abap_false.
                  lv_data_changed                 = abap_true.
                ELSE.
                  " Check master node is complete configered
                  " ( including sub nodes: server performance category and storage amount )
                  lv_complete = /hec1/cl_bopf_config_validat_h=>check_master_node_is_complete( iv_is_app_server = abap_true
                                                                                               iv_check_rule    = /hec1/if_bopf_constants=>gc_check_rule-node
                                                                                               is_ctx           = is_ctx
                                                                                               it_key           = VALUE #( ( key = lr_app_node->key ) )
                                                                                               io_read          = io_read ).
                  IF lv_complete = abap_true.
                    lr_app_node->hec_row_selectable = abap_true.
                    lv_data_changed                 = abap_true.
                  ENDIF.
                ENDIF. " IF lv_release = abap_false AND...
              ENDIF. " IF lr_app_node->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-standby AND...


              "-----------------------------------
              " Update App server cluster type
              "-----------------------------------
              IF lr_app_node->hec_app_cluster_type_value <> <fs_app_serv_inst>-hec_app_cluster_type_value.
                lr_app_node->hec_app_cluster_type_value = <fs_app_serv_inst>-hec_app_cluster_type_value.
                lv_data_changed                         = abap_true.
              ENDIF.


              "-----------------------------------
              " Modify App node
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_node->key
                                   is_data = lr_app_node ).
              ENDIF.


              UNASSIGN <fs_app_serv_inst>.
              CLEAR: lv_release,
                     lv_complete,
                     lv_data_changed.
            ENDLOOP.
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_app_server_cr.

    DATA: lt_app_server        TYPE /hec1/t_data_app_serv_ct,
          lt_app_serv_perf_cat TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_storage       TYPE /hec1/t_data_app_storage_ct,
          lt_line              TYPE TABLE OF string,
          lt_phase             TYPE /hec1/t_data_phase_ct,
          lt_app_server_before TYPE /hec1/t_data_app_serv_ct,
          lt_act_param         TYPE /hec1/t_act_create_app_storage,
          lt_act_param_storage TYPE /bobf/t_frw_key,
          lt_act_param_server  TYPE /hec1/t_act_update_app_server,
          lt_act_param_dlvy    TYPE /hec1/t_act_update_dlvy_unit,
          lt_act_param_datac   TYPE /hec1/t_act_update_datacenter,
          lt_act_param_serv_pc TYPE /hec1/t_act_update_app_serv_pc,
          lt_act_param_phasing TYPE TABLE OF /hec1/s_act_phase_inherit.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_server ).

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
          WHEN /hec1/if_configuration_c=>sc_determination-app_server-create.

            " Get App server performance category node (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server-to_parent
                                              IMPORTING et_data        = lt_app_serv_perf_cat ).

            LOOP AT        lt_app_server
            REFERENCE INTO DATA(lr_app_server)
                     WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master.

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              lr_app_server->hec_ip_server_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server(
                                                                            iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                            iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                            iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_app_server->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL )
                                                                            iv_srv_perf_cat_guid   = VALUE #( lt_app_serv_perf_cat[ key = lr_app_server->parent_key ]-hec_srv_perf_cat_guid OPTIONAL ) ) )
                                                          THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                          ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              lr_app_server->hec_delete_visible = abap_false.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_app_server->hec_ip_server_guid IS NOT INITIAL AND
                                                                             lr_app_server->hec_phase_guid     IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete          ).

              IF lv_inst_status <> lr_app_server->hec_instance_status.
                lr_app_server->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_app_serv_perf_cat[ key = lr_app_server->parent_key ] TO FIELD-SYMBOL(<fs_app_serv_perf_cat>).
              IF <fs_app_serv_perf_cat> IS ASSIGNED.
                IF <fs_app_serv_perf_cat>-hec_srv_perf_cat_guid IS NOT INITIAL AND
                   <fs_app_serv_perf_cat>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_app_server->hec_row_selectable.
                lr_app_server->hec_row_selectable = lv_release.
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
                  is_node_data = lr_app_server
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              IF lv_data_changed = abap_false.
                lv_data_changed = lv_cr_data_changed.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " App server storage
              "-----------------------------------
              INSERT VALUE #( key         = lr_app_server->key
                              parent_key  = lr_app_server->parent_key
                              hec_pricing_included = abap_false                ) INTO TABLE lt_act_param.

              "-----------------------------------
              " Modify
              "-----------------------------------
              IF lv_data_changed = abap_true.


                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_server->key
                                   is_data = lr_app_server ).
              ENDIF.

              UNASSIGN <fs_app_serv_perf_cat>.
              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release.
            ENDLOOP.


            "-----------------------------------
            " Set create App server storage
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_storage( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_storage )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                    ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_server-update.

            " Get Before image
            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_fill_data    = abap_true
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_app_server_before ).

            " Get App server performance category (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server-to_parent
                                              IMPORTING et_data        = lt_app_serv_perf_cat ).

            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server-app_storage
                                              IMPORTING et_data        = lt_app_storage ).

            " Get Phases
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            LOOP AT lt_app_server REFERENCE INTO lr_app_server.
              ASSIGN lt_app_server_before[ key = lr_app_server->key ] TO FIELD-SYMBOL(<fs_app_server_before>).
              IF <fs_app_server_before> IS ASSIGNED.

                "-----------------------------------
                " Split DB server infrastructure
                " provider server GUID
                "-----------------------------------
                IF lr_app_server->hec_ip_server_guid CA ';'.
                  SPLIT lr_app_server->hec_ip_server_guid
                     AT ';'
                   INTO TABLE lt_line.

                  LOOP AT lt_line ASSIGNING FIELD-SYMBOL(<fs_line>).
                    CASE sy-tabix.
                      WHEN 1.
                        lr_app_server->hec_ip_server_guid = <fs_line>.
                      WHEN 2.
                        DATA(lv_inf_provider_guid) = <fs_line>.
                      WHEN 3.
                        DATA(lv_datacenter_guid) = <fs_line>.
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
                      DATA(ls_datacenter) = lt_datacenter[ hec_node_datacenter = lr_app_server->hec_tier_datacenter_guid ].

                      IF ls_datacenter-hec_datacenter_guid IS INITIAL.
                        INSERT VALUE #( key                     = ls_datacenter-key
                                        parent_key              = ls_datacenter-parent_key
                                        hec_datacenter_fdt_guid = lv_datacenter_guid       ) INTO TABLE lt_act_param_datac.
*
                        "-----------------------------------
                        " Fill action table for update
                        " App node pricing
                        "-----------------------------------
                        INSERT VALUE #( key               = lr_app_server->parent_key
                                        do_update_pricing = abap_true                 ) INTO TABLE lt_act_param_serv_pc.

                      ENDIF. " IF ls_datacenter-hec_datacenter_guid IS INITIAL.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                ENDIF. " IF ls_app_server-hec_ds_ip_server_guid CA ';'.


                "-----------------------------------
                " App server has changed
                "-----------------------------------
                IF lr_app_server->hec_ip_server_guid     IS NOT INITIAL                            AND
                   lr_app_server->hec_ip_server_guid <> <fs_app_server_before>-hec_ip_server_guid.

                  IF lv_inf_provider_guid IS NOT INITIAL.
                    lr_dlvy_unit->hec_inf_provider_guid = lv_inf_provider_guid.
                  ENDIF.

                  IF lr_app_server->hec_sec_datacenter_guid IS     INITIAL AND
                     lv_datacenter_guid                     IS NOT INITIAL.
                    lr_app_server->hec_sec_datacenter_guid = lv_datacenter_guid.
                    lv_data_changed                   = abap_true.
                  ENDIF.

                  SELECT SINGLE *
                    FROM /hec1/i_serverbasic
                   WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid             AND
                         hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid    AND
                         hec_sec_datacenter_guid = @lr_app_server->hec_sec_datacenter_guid AND
                         hec_ip_server_guid      = @lr_app_server->hec_ip_server_guid
                    INTO @DATA(ls_server).

                  IF ls_server IS NOT INITIAL.
                    lr_app_server->hec_ip_server_descr      = ls_server-hec_ip_server_descr.
                    lr_app_server->hec_ip_server_guid       = ls_server-hec_ip_server_guid.
                    lr_app_server->hec_host_type_descr      = ls_server-hec_srv_host_type_descr.
                    lr_app_server->hec_host_type_value      = ls_server-hec_srv_host_type_value.
                    lr_app_server->hec_srv_ram_size         = ls_server-hec_srv_ram_size.
                    lr_app_server->hec_srv_cpu_size         = ls_server-hec_srv_cpu_size.
                    lr_app_server->hec_sec_datacenter_guid  = ls_server-hec_sec_datacenter_guid.
                    lr_app_server->hec_srv_main_storage_qty = ls_server-hec_srv_main_storage_qty.
                    lr_app_server->hec_tree_descr           = ls_server-hec_ip_server_descr. "#EC CI_FLDEXT_OK[2215424]
                    lr_app_server->hec_as_flavour           = ls_server-hec_srv_flavour.
                    lr_app_server->hec_saps                 = ls_server-hec_saps.
                    lr_app_server->hec_approval_needed      = ls_server-hec_approval_needed.

                    lv_data_changed                         = abap_true.

                    " Set Value List Quantity
                    lr_app_server->hec_ip_server_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server(
                                                                                  iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                  iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                                  iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_app_server->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL )
                                                                                  iv_srv_perf_cat_guid   = VALUE #( lt_app_serv_perf_cat[ key = lr_app_server->parent_key ]-hec_srv_perf_cat_guid OPTIONAL ) ) )
                                                                THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                    "-------------------------
                    " Get App server pricing
                    "-------------------------
                    SELECT SINGLE hec_cb_pricing_lb_guid
                      FROM /hec1/i_serverlbbasic
                     WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid             AND
                           hec_sec_datacenter_guid = @lr_app_server->hec_sec_datacenter_guid AND
                           hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid    AND
                           hec_ip_server_guid      = @lr_app_server->hec_ip_server_guid
                      INTO @DATA(lv_lb_guid).

                    IF lv_lb_guid IS NOT INITIAL.
                      SELECT SINGLE * FROM /hec1/c_cbp_lb "#EC CI_ALL_FIELDS_NEEDED
                         INTO @DATA(ls_pricing)
                        WHERE hec_price_lb = @lv_lb_guid.

                      lr_app_server->* = CORRESPONDING #( BASE ( lr_app_server->* ) ls_pricing ).
                    ENDIF.

                    "-----------------------------------
                    " Fill action table for update
                    " App server storage
                    "-----------------------------------
                    LOOP AT lt_app_storage REFERENCE INTO DATA(lr_app_storage)
                      WHERE parent_key = lr_app_server->key.
                      INSERT VALUE #( key = lr_app_storage->key ) INTO TABLE lt_act_param_storage.
                    ENDLOOP.
                  ENDIF. " IF ls_server IS NOT INITIAL.
                ENDIF. "  IF ls_app_server-hec_as_ip_server_guid IS NOT INITIAL AND...


                "-----------------------------------
                " Phase has changed -
                " update phase and inherit phase assignment
                "-----------------------------------
                IF lr_app_server->hec_phase_guid NE <fs_app_server_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_app_server->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                     lr_app_server->hec_app_node_default          = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_app_server->key
                                    hec_phase_guid_new = lr_app_server->hec_phase_guid
                                    hec_phase_guid_old = <fs_app_server_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_app_server->hec_phase_changed = abap_true.
                  lv_data_changed                  = abap_true.

                ENDIF. "phasing changed
              ENDIF. " if <fs_app_server_before> is assigned.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_app_server->hec_ip_server_guid IS NOT INITIAL AND
                                                                       lr_app_server->hec_phase_guid     IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_app_server->hec_instance_status.
                lr_app_server->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_server->key
                                   is_data = lr_app_server ).
              ENDIF.

              UNASSIGN: <fs_line>,
                             <fs_app_server_before>.

              CLEAR: lv_inf_provider_guid,
                     lv_datacenter_guid,
                     lv_lb_guid,
                     lv_inst_status,
                     lv_data_changed,
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
            " Set App Server PC action to
            " general
            "-----------------------------------
            IF lt_act_param_serv_pc IS NOT INITIAL.

              me->mr_act_param_server_pc = NEW /hec1/t_act_update_app_serv_pc( lt_act_param_serv_pc ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-app_server_perform_cat )
                    it_key          = VALUE #( FOR wa_act_spc IN lt_act_param_serv_pc
                                             ( key = wa_act_spc-key )             )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_app_server_perf_cat )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_server_pc   ).

            ENDIF.

            "-----------------------------------
            " Set update App Storage action to
            " general
            "-----------------------------------
            IF lt_act_param_storage IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-app_storage )
                  it_key          = lt_act_param_storage
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_app_storage )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                                               ).
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
                  ir_act_param    = me->mr_act_param_phasing                                                                                                                 ).
            ENDIF.


            " ***************************************************************************
            " Update mode after app server
            " performance category update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_server-update_after_serv_perf_cat.

            " Get App server performance category (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server-to_parent
                                              IMPORTING et_data        = lt_app_serv_perf_cat ).


            LOOP AT lt_app_server REFERENCE INTO lr_app_server.
              ASSIGN lt_app_serv_perf_cat[ key = lr_app_server->parent_key ] TO <fs_app_serv_perf_cat>.

              IF <fs_app_serv_perf_cat> IS ASSIGNED.
                IF <fs_app_serv_perf_cat>-hec_srv_perf_cat_guid IS NOT INITIAL AND
                   <fs_app_serv_perf_cat>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              IF lv_release <> lr_app_server->hec_row_selectable.
                lr_app_server->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Update App server cluster type
              "-----------------------------------
              IF lr_app_server->hec_app_cluster_type_value <> <fs_app_serv_perf_cat>-hec_app_cluster_type_value.
                lr_app_server->hec_app_cluster_type_value = <fs_app_serv_perf_cat>-hec_app_cluster_type_value.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_server->key
                                   is_data = lr_app_server ).
              ENDIF.

              UNASSIGN <fs_app_serv_perf_cat>.

              CLEAR: lv_release,
                     lv_data_changed.

            ENDLOOP. " LOOP AT lt_app_server
        ENDCASE.



      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_app_server_inst_cr.

    DATA: lt_app_serv_inst         TYPE /hec1/t_data_app_serv_inst_ct,
          lt_app_serv_inst_before  TYPE /hec1/t_data_app_serv_inst_ct,
          lt_app_serv_inst_pertier TYPE /hec1/t_data_app_serv_inst_ct,
          lt_app_node              TYPE /hec1/t_data_app_node_ct,
          lt_tier                  TYPE /hec1/t_data_tier_ct,
          lt_act_param             TYPE /hec1/t_act_create_app_node,
          lt_phase                 TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing     TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_serv_inst ).

    " Get tier
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-to_parent
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

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_server_instance-create.
            LOOP AT lt_app_serv_inst REFERENCE INTO DATA(lr_app_serv_inst).

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              " App Server Instance
              lr_app_serv_inst->hec_sol_tier_stack_si_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server_instance(
                                                                                       iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                       iv_sol_tier_stack_guid = lr_app_serv_inst->hec_sol_tier_stack_guid
                                                                                       iv_srv_inst_rel_value  = lr_app_serv_inst->hec_srv_inst_rel_value
                                                                                       iv_solution_guid       = lr_app_serv_inst->hec_solution_guid
                                                                                       iv_is_app_server       = abap_true ) )
                                                                     THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                     ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " Operating System
              lr_app_serv_inst->hec_sol_apsi_oper_sys_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_app_operating_system(
                                                                                                     iv_apm_guid               = lr_landscape->hec_apm_guid
                                                                                                     iv_sol_tier_stack_si_guid = lr_app_serv_inst->hec_sol_tier_stack_si_guid ) )
                                                                     THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                     ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " Cluster Type
              lr_app_serv_inst->hec_sol_apsi_clusttyp_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_app_cluster_type(
                                                                                                     iv_apm_guid               = lr_landscape->hec_apm_guid
                                                                                                     iv_sol_tier_stack_si_guid = lr_app_serv_inst->hec_sol_tier_stack_si_guid ) )
                                                                     THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                     ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              lr_app_serv_inst->hec_delete_visible = COND #( WHEN lr_app_serv_inst->hec_default_app_server_inst = abap_true
                                                             THEN abap_false
                                                             ELSE abap_true ).

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_app_serv_inst->hec_sol_tier_stack_si_guid IS NOT INITIAL AND
                                                                             lr_app_serv_inst->hec_sol_apsi_oper_sys_guid IS NOT INITIAL AND
                                                                             lr_app_serv_inst->hec_sol_apsi_clusttyp_guid IS NOT INITIAL AND
                                                                             lr_app_serv_inst->hec_phase_guid             IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete         ).

              IF lv_inst_status <> lr_app_serv_inst->hec_instance_status.
                lr_app_serv_inst->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_tier[ key = lr_app_serv_inst->parent_key ] TO FIELD-SYMBOL(<fs_tier>).
              IF <fs_tier> IS ASSIGNED.
                IF <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                   <fs_tier>-hec_tier_type_value      IS NOT INITIAL AND
                   <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_app_serv_inst->hec_row_selectable.
                lr_app_serv_inst->hec_row_selectable = lv_release.
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
                  is_node_data = lr_app_serv_inst
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              IF lv_data_changed = abap_false.
                lv_data_changed = lv_cr_data_changed.
              ENDIF.

              "-----------------------------------
              " Fill action table for
              " create App node
              "-----------------------------------
              IF lr_app_serv_inst->hec_sol_tier_stack_si_guid IS NOT INITIAL AND
                 lr_app_serv_inst->hec_sol_apsi_oper_sys_guid IS NOT INITIAL AND
                 lr_app_serv_inst->hec_sol_apsi_clusttyp_guid IS NOT INITIAL.

                INSERT VALUE #( key                        = lr_app_serv_inst->key
                                parent_key                 = lr_app_serv_inst->parent_key
                                hec_app_cluster_type_value = SWITCH #( lr_app_serv_inst->hec_app_cluster_type_value
                                                                       WHEN /hec1/if_config_constants=>gc_app_clust_node-none
                                                                       THEN /hec1/if_config_constants=>gc_app_clust_node-none
                                                                       WHEN /hec1/if_config_constants=>gc_app_clust_node-ha
                                                                       THEN /hec1/if_config_constants=>gc_app_clust_node-ha
                                                                       ELSE /hec1/if_config_constants=>gc_app_clust_node-none )
                                hec_default_app_server     = SWITCH #( lr_app_serv_inst->hec_default_app_server_inst
                                                                       WHEN abap_true
                                                                       THEN abap_true
                                                                       ELSE abap_false                               )           ) INTO TABLE lt_act_param.
              ENDIF.

              "-----------------------------------
              " Modify App server instance
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_serv_inst->key
                                   is_data = lr_app_serv_inst ).
              ENDIF.

              UNASSIGN <fs_tier>.

              CLEAR: lv_inst_status,
                     lv_release,
                     lv_data_changed.
            ENDLOOP.


            "-----------------------------------
            " Set create App server node
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_node( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key )        )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_node )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_server_instance-update.

            " Get data before update
            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_app_serv_inst_before ).

            " Get app ndde
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-app_node
                                              IMPORTING et_data        = lt_app_node ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get all app server instances per tier
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                        it_key         = lt_tier_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier-app_server_instance
                                              IMPORTING et_data        = lt_app_serv_inst_pertier ).

            "-----------------------------------
            " Get App server instance data
            "-----------------------------------
            SELECT *                          "#EC CI_ALL_FIELDS_NEEDED
              FROM /hec1/i_appservinstancenobasic
             WHERE hec_apm_guid = @lr_landscape->hec_apm_guid
              INTO TABLE @DATA(lt_app_serv_inst_no).

            "-----------------------------------
            " Get App server operating system
            "-----------------------------------
            SELECT *                          "#EC CI_ALL_FIELDS_NEEDED
              FROM /hec1/i_appopersystembasic
             WHERE hec_apm_guid = @lr_landscape->hec_apm_guid
              INTO TABLE @DATA(lt_app_operating_sys).

            "-----------------------------------
            " Get App server cluster type
            "-----------------------------------
            SELECT *                          "#EC CI_ALL_FIELDS_NEEDED
              FROM /hec1/i_appclustertypebasic
             WHERE hec_apm_guid = @lr_landscape->hec_apm_guid
              INTO TABLE @DATA(lt_cluster_type).


            LOOP AT lt_app_serv_inst REFERENCE INTO lr_app_serv_inst.

              ASSIGN lt_app_serv_inst_before[ key = lr_app_serv_inst->key ] TO FIELD-SYMBOL(<fs_serv_inst_before>).
              IF <fs_serv_inst_before> IS ASSIGNED.

                " Can this value change? TODO
                lr_app_serv_inst->hec_delete_visible = COND #( WHEN lr_app_serv_inst->hec_default_app_server_inst = abap_true
                                                               THEN abap_false
                                                               ELSE abap_true ).

                "-----------------------------------
                " Update operating system
                "-----------------------------------
                IF <fs_serv_inst_before>-hec_sol_apsi_oper_sys_guid IS INITIAL     AND
                   lr_app_serv_inst->hec_sol_apsi_oper_sys_guid     IS NOT INITIAL.

                  TRY.
                      DATA(ls_operating_sys) = lt_app_operating_sys[ hec_sol_tier_stack_si_guid = lr_app_serv_inst->hec_sol_tier_stack_si_guid
                                                                     hec_sol_apsi_oper_sys_guid = lr_app_serv_inst->hec_sol_apsi_oper_sys_guid     ].

                      lr_app_serv_inst->hec_sol_apsi_oper_sys_guid = ls_operating_sys-hec_sol_apsi_oper_sys_guid.
                      lr_app_serv_inst->hec_operating_sys_guid     = ls_operating_sys-hec_operating_sys_guid.
                      lr_app_serv_inst->hec_operating_sys_value    = ls_operating_sys-hec_operating_sys_value.
                      lr_app_serv_inst->hec_operating_sys_descr    = ls_operating_sys-hec_operating_sys_descr.
                      lr_app_serv_inst->hec_os_support_stat_value  = ls_operating_sys-hec_os_support_stat_value.
                      lr_app_serv_inst->hec_os_support_stat_descr  = ls_operating_sys-hec_os_support_stat_descr.

                      lv_data_changed                              = abap_true.

                      " Set Value List Quantity - Operating System
                      lr_app_serv_inst->hec_sol_apsi_oper_sys_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_app_operating_system(
                                                                                                             iv_apm_guid               = lr_landscape->hec_apm_guid
                                                                                                             iv_sol_tier_stack_si_guid = lr_app_serv_inst->hec_sol_tier_stack_si_guid ) )
                                                                             THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                             ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                  CLEAR ls_operating_sys.
                ENDIF. " IF <fs_serv_inst_before>-hec_asi_operating_sys_guid IS INITIAL     AND...

                "-----------------------------------
                " Update App server instance GUID
                "-----------------------------------
                IF <fs_serv_inst_before>-hec_sol_tier_stack_si_guid IS INITIAL     AND
                   lr_app_serv_inst->hec_sol_tier_stack_si_guid     IS NOT INITIAL AND
                   lr_app_serv_inst->hec_default_app_server_inst = abap_false.

                  TRY.
                      DATA(ls_server_inst_no) = lt_app_serv_inst_no[ hec_sol_tier_stack_guid    = lr_app_serv_inst->hec_sol_tier_stack_guid
                                                                     hec_sol_tier_stack_si_guid = lr_app_serv_inst->hec_sol_tier_stack_si_guid ].


                      DATA(ls_cluster_type) = lt_cluster_type[ hec_sol_tier_stack_si_guid  = lr_app_serv_inst->hec_sol_tier_stack_si_guid
                                                               hec_app_cluster_type_value  = /hec1/if_config_constants=>gc_app_clust_node-none ].


                      lr_app_serv_inst->* = CORRESPONDING #( BASE ( lr_app_serv_inst->* ) ls_server_inst_no EXCEPT hec_srv_inst_rel_value
                                                                                                                   hec_srv_inst_rel_descr ).

                      lr_app_serv_inst->*                      = CORRESPONDING #( BASE ( lr_app_serv_inst->* ) ls_cluster_type ).
                      lr_app_serv_inst->hec_backup_relev_value = ls_server_inst_no-hec_backup_relevance.
                      lr_app_serv_inst->hec_tree_descr         = ls_server_inst_no-hec_sol_tier_asi_descr.

                      lv_data_changed                          = abap_true.

                      " Set Value List Quantity - App Server Instance
                      lr_app_serv_inst->hec_sol_tier_stack_si_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server_instance(
                                                                                               iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                               iv_sol_tier_stack_guid = lr_app_serv_inst->hec_sol_tier_stack_guid
                                                                                               iv_srv_inst_rel_value  = lr_app_serv_inst->hec_srv_inst_rel_value
                                                                                               iv_solution_guid       = lr_app_serv_inst->hec_solution_guid
                                                                                               iv_is_app_server       = abap_true ) )
                                                                             THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                             ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                      " Set Value List Quantity - Cluster Type
                      lr_app_serv_inst->hec_sol_apsi_clusttyp_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_app_cluster_type(
                                                                                                             iv_apm_guid               = lr_landscape->hec_apm_guid
                                                                                                             iv_sol_tier_stack_si_guid = lr_app_serv_inst->hec_sol_tier_stack_si_guid ) )
                                                                             THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                             ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                      " Same app server exist, then operating system
                      " has to be set same as the existing app server
                      " is set
                      DATA(lt_filter) = VALUE /hec1/t_filter_app_serv_inst( ( hec_node_solution      = lr_app_serv_inst->hec_node_solution
                                                                              hec_node_tier          = lr_app_serv_inst->hec_node_tier     ) ).

                      DATA(lt_filter_app_serv_inst) = FILTER #( lt_app_serv_inst_pertier IN lt_filter WHERE hec_node_solution = hec_node_solution AND
                                                                                                            hec_node_tier     = hec_node_tier         ).

                      " Delete current app server instacne
                      DELETE lt_filter_app_serv_inst
                       WHERE hec_node_app_serv_inst = lr_app_serv_inst->hec_node_app_serv_inst.


                      ASSIGN lt_filter_app_serv_inst[ hec_sol_tier_stack_guid    = lr_app_serv_inst->hec_sol_tier_stack_guid
                                                      hec_sol_tier_stack_si_guid = lr_app_serv_inst->hec_sol_tier_stack_si_guid ] TO FIELD-SYMBOL(<fs_app_server_inst>). "#EC CI_SORTSEQ

                      IF <fs_app_server_inst> IS ASSIGNED.
                        lr_app_serv_inst->hec_sol_apsi_oper_sys_guid = <fs_app_server_inst>-hec_sol_apsi_oper_sys_guid.
                        lr_app_serv_inst->hec_operating_sys_guid     = <fs_app_server_inst>-hec_operating_sys_guid.
                        lr_app_serv_inst->hec_operating_sys_value    = <fs_app_server_inst>-hec_operating_sys_value.
                        lr_app_serv_inst->hec_operating_sys_descr    = <fs_app_server_inst>-hec_operating_sys_descr.
                        lr_app_serv_inst->hec_os_support_stat_value  = <fs_app_server_inst>-hec_os_support_stat_value.
                        lr_app_serv_inst->hec_os_support_stat_descr  = <fs_app_server_inst>-hec_os_support_stat_descr.
                      ENDIF.

                      IF lr_app_serv_inst->hec_sol_apsi_oper_sys_guid IS INITIAL.
                        " Is only one operating system available, it
                        " can be set directly
                        DATA(lt_operating_sys) = VALUE /hec1/t_apm_app_operating_sys( FOR wa IN lt_app_operating_sys
                                                                                      WHERE ( hec_sol_tier_stack_si_guid = ls_server_inst_no-hec_sol_tier_stack_value )
                                                                                      ( CORRESPONDING #( wa )                                                          ) ).

                        IF lines( lt_operating_sys ) = 1.
                          DATA(ls_oper_sys) = lt_operating_sys[ 1 ].
                          lr_app_serv_inst->hec_sol_apsi_oper_sys_guid = ls_oper_sys-hec_sol_apsi_oper_sys_guid.
                          lr_app_serv_inst->hec_operating_sys_guid     = ls_oper_sys-hec_operating_sys_guid.
                          lr_app_serv_inst->hec_operating_sys_value    = ls_oper_sys-hec_operating_sys_value.
                          lr_app_serv_inst->hec_operating_sys_descr    = ls_oper_sys-hec_operating_sys_descr.
                          lr_app_serv_inst->hec_os_support_stat_value  = ls_oper_sys-hec_os_support_stat_value.
                          lr_app_serv_inst->hec_os_support_stat_descr  = ls_oper_sys-hec_os_support_stat_descr.
                        ENDIF. " IF lines( lt_app_oper_sys ) = 1.
                      ENDIF. " IF ls_app_server_inst-hec_asi_operating_sys_guid IS INITIAL.

                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                ENDIF. " IF ls_app_server_inst_old-hec_app_srv_guid IS INITIAL     AND


                "-----------------------------------
                " Phase has changed -
                " update phase and inherit phase assignment
                "-----------------------------------
                IF lr_app_serv_inst->hec_phase_guid NE <fs_serv_inst_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_app_serv_inst->key
                                  hec_phase_guid_new = lr_app_serv_inst->hec_phase_guid
                                  hec_phase_guid_old = <fs_serv_inst_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_app_serv_inst->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "phasing changed
              ENDIF." IF <fs_serv_inst_before> IS ASSIGNED.

              "-----------------------------------
              " Fill action table for
              " create App node
              "-----------------------------------
              IF lr_app_serv_inst->hec_sol_tier_stack_si_guid IS NOT INITIAL AND
                 lr_app_serv_inst->hec_sol_apsi_oper_sys_guid IS NOT INITIAL AND
                 lr_app_serv_inst->hec_sol_apsi_clusttyp_guid IS NOT INITIAL AND
             NOT line_exists( lt_app_node[ parent_key = lr_app_serv_inst->key ] ).

                INSERT VALUE #( key                        = lr_app_serv_inst->key
                                parent_key                 = lr_app_serv_inst->parent_key
                                hec_app_cluster_type_value = SWITCH #( lr_app_serv_inst->hec_app_cluster_type_value
                                                                       WHEN /hec1/if_config_constants=>gc_app_clust_node-none
                                                                       THEN /hec1/if_config_constants=>gc_app_clust_node-none
                                                                       WHEN /hec1/if_config_constants=>gc_app_clust_node-ha
                                                                       THEN /hec1/if_config_constants=>gc_app_clust_node-ha
                                                                       ELSE /hec1/if_config_constants=>gc_app_clust_node-none )
                                hec_default_app_server     = SWITCH #( lr_app_serv_inst->hec_default_app_server_inst
                                                                       WHEN abap_true
                                                                       THEN abap_true
                                                                       ELSE abap_false                               )           ) INTO TABLE lt_act_param.
              ENDIF.



              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_app_serv_inst->hec_sol_tier_stack_si_guid IS NOT INITIAL AND
                                                                       lr_app_serv_inst->hec_sol_apsi_oper_sys_guid IS NOT INITIAL AND
                                                                       lr_app_serv_inst->hec_sol_apsi_clusttyp_guid IS NOT INITIAL AND
                                                                       lr_app_serv_inst->hec_phase_guid             IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete         ).

              IF lv_inst_status <> lr_app_serv_inst->hec_instance_status.
                lr_app_serv_inst->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify App server instance
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_serv_inst->key
                                   is_data = lr_app_serv_inst ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     ls_server_inst_no,
                     ls_cluster_type,
                     ls_oper_sys,
                     ls_operating_sys,
                     lt_filter,
                     lt_filter_app_serv_inst,
                     lt_operating_sys.

              UNASSIGN <fs_serv_inst_before>.
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
            " Set create App server node
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_node( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key )        )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_node )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                ).

            ENDIF.


            " ***************************************************************************
            " " Update mode after tier update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_server_instance-update_after_tier.

            LOOP AT lt_app_serv_inst REFERENCE INTO lr_app_serv_inst.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_tier[ key = lr_app_serv_inst->parent_key ] TO <fs_tier>.
              IF <fs_tier> IS ASSIGNED.
                IF <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                   <fs_tier>-hec_tier_type_value      IS NOT INITIAL AND
                   <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_app_serv_inst->hec_row_selectable.
                lr_app_serv_inst->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Modify App server instance
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_serv_inst->key
                                   is_data = lr_app_serv_inst ).
              ENDIF.

              UNASSIGN <fs_tier>.
              CLEAR: lv_release,
                     lv_data_changed.
            ENDLOOP.
        ENDCASE.



      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_app_server_pc_cr.

    DATA: lt_app_serv_perf_cat         TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_serv_perf_cat_before  TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_serv_perf_cat_pernode TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_node                  TYPE /hec1/t_data_app_node_ct,
          lt_app_serv_inst             TYPE /hec1/t_data_app_serv_inst_ct,
          lt_app_server                TYPE /hec1/t_data_app_serv_ct,
          lt_app_storage_qty           TYPE /hec1/t_data_app_storageqty_ct,
          lt_act_param                 TYPE /hec1/t_act_create_app_qty,
          lt_act_param_server_key      TYPE /bobf/t_frw_key,
          lt_act_param_server          TYPE /hec1/t_act_update_app_server,
          lt_act_param_node            TYPE /hec1/t_act_update_app_node,
          lt_act_param_succ            TYPE /hec1/t_act_set_success_predec,
          lt_phase                     TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing         TYPE TABLE OF /hec1/s_act_phase_inherit,
          lt_range                     TYPE RANGE OF string.

    CLEAR: eo_message,
           et_failed_key.

    "-----------------------------------
    " Get data
    "-----------------------------------
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_serv_perf_cat ).

    " Get App node (parent)
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_parent
                                      IMPORTING et_data        = lt_app_node ).

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
          WHEN /hec1/if_configuration_c=>sc_determination-app_server_perform_cat-create.

            " Get for each App master node
            " the App server performance category
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
                                                        it_key         = VALUE #( FOR wa_node IN lt_app_node
                                                                                 ( key = wa_node-key )                )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
                                              IMPORTING et_data        = lt_app_serv_perf_cat_pernode ).


            LOOP AT         lt_app_serv_perf_cat
            REFERENCE INTO DATA(lr_app_serv_perf_cat)
                     WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master.

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              lr_app_serv_perf_cat->hec_srv_perf_cat_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server_perf_cat(
                                                                                      iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                      iv_inf_provider_guid   = lr_dlvy_unit->hec_inf_provider_guid
                                                                                      iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_app_serv_perf_cat->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL )
                                                                                      iv_is_app_server       = abap_true ) )
                                                                    THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                    ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              lr_app_serv_perf_cat->hec_delete_visible = abap_true.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_app_serv_perf_cat->hec_srv_perf_cat_guid IS NOT INITIAL AND
                                                                             lr_app_serv_perf_cat->hec_phase_guid        IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete          ).

              IF lv_inst_status <> lr_app_serv_perf_cat->hec_instance_status.
                lr_app_serv_perf_cat->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_app_node[ key = lr_app_serv_perf_cat->parent_key ] TO FIELD-SYMBOL(<fs_app_node>).
              IF <fs_app_node> IS ASSIGNED.
                IF <fs_app_node>-hec_app_srv_perf_cat_qty IS NOT INITIAL AND
                  <fs_app_node>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_app_serv_perf_cat->hec_row_selectable.
                lr_app_serv_perf_cat->hec_row_selectable = lv_release.
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
                  is_node_data = lr_app_serv_perf_cat
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              IF lv_data_changed = abap_false.
                lv_data_changed = lv_cr_data_changed.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " App server storage amount
              "-----------------------------------
              IF NOT lr_app_serv_perf_cat->hec_server_required = abap_false.
                INSERT VALUE #( key                    = lr_app_serv_perf_cat->key
                                parent_key             = lr_app_serv_perf_cat->parent_key
                                hec_storage_amount_qty = lr_app_serv_perf_cat->hec_storage_qty ) INTO TABLE lt_act_param.
              ENDIF.

              "-----------------------------------
              " Fill action table for setting
              " App server performance category
              " successor/predecessor
              "-----------------------------------
              DATA(lv_node_count) = REDUCE i( INIT x = 0
                                              FOR <l> IN lt_app_serv_perf_cat_pernode WHERE ( parent_key = lr_app_serv_perf_cat->parent_key )
                                              NEXT x = x + 1                                                                                  ).

              IF NOT line_exists( lt_act_param_succ[ key = lr_app_serv_perf_cat->parent_key ] ) AND lv_node_count > 1.
                TRY.
                    INSERT VALUE #( key                  = lr_app_serv_perf_cat->parent_key
                                    parent_key           = lt_app_node[ key = lr_app_serv_perf_cat->parent_key ]-parent_key
                                    hec_no_children_node = lv_node_count                                                    ) INTO TABLE lt_act_param_succ.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.

              "-----------------------------------
              " Modify App server storage amount
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_serv_perf_cat->key
                                   is_data = lr_app_serv_perf_cat ).

              ENDIF.

              UNASSIGN <fs_app_node>.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release,
                     lv_node_count.

            ENDLOOP.           " LOOP AT lt_app_serv_perf_cat REFERENCE INTO lr_app_serv_perf_cat.


            "-----------------------------------
            " Set successor/predecessor action
            " to GENERAL
            "-----------------------------------
            IF lt_act_param_succ IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_set_success_predec( lt_act_param_succ ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key  = /hec1/if_configuration_c=>sc_node-app_node
                                             assoc_key = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat )
                  it_key          = VALUE #( FOR wa_act_succ IN lt_act_param_succ
                                            ( key = wa_act_succ-key )    )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-set_success_predec )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

            ENDIF.

            "-----------------------------------
            " Set create App server storage
            " amount and create App server
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_qty( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_qty )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_server )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                                                                          ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_server_perform_cat-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_app_serv_perf_cat_before ).


            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get App Node
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_parent
                                              IMPORTING et_target_key  = DATA(lt_app_node_key)
                                                        et_data        = lt_app_node ).

            " Get App server instance
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
                                                        it_key         = lt_app_node_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_node-to_parent
                                              IMPORTING et_data        = lt_app_serv_inst ).

            " Get App Server
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_server
                                              IMPORTING et_data        = lt_app_server
                                                        et_target_key  = DATA(lt_app_server_key) ).

            " Get App Storage Qty
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_storage_amount
                                              IMPORTING et_data        = lt_app_storage_qty ).


            "-----------------------------------
            " Get server performance category
            "-----------------------------------
            DATA(lt_range_table) = VALUE /hec1/t_selection_range( FOR wa_spc IN lt_app_serv_perf_cat
                                                                ( option = /hec1/if_config_constants=>gc_range_option-eq
                                                                  sign   = /hec1/if_config_constants=>gc_range_sign-i
                                                                  low    = wa_spc-hec_srv_perf_cat_guid                   ) ).

            SELECT *                          "#EC CI_ALL_FIELDS_NEEDED
              FROM /hec1/i_appservperfcatbasic
             WHERE hec_apm_guid          = @lr_landscape->hec_apm_guid AND
                   hec_srv_perf_cat_guid IN @lt_range_table
              INTO TABLE @DATA(lt_serv_perf_cat).


            "-----------------------------------
            " Get server
            "-----------------------------------
            CLEAR lt_range_table.
            lt_range_table = VALUE /hec1/t_selection_range( FOR wa IN lt_app_serv_perf_cat
                                                           ( option = /hec1/if_config_constants=>gc_range_option-eq
                                                             sign   = /hec1/if_config_constants=>gc_range_sign-i
                                                             low    = wa-hec_srv_perf_cat_guid                   ) ).

            SELECT *                          "#EC CI_ALL_FIELDS_NEEDED
              FROM /hec1/i_serverbasic
             WHERE hec_apm_guid = @lr_landscape->hec_apm_guid AND
                   hec_srv_perf_cat_guid IN @lt_range_table
              INTO TABLE @DATA(lt_server_data).



            LOOP AT lt_app_serv_perf_cat REFERENCE INTO lr_app_serv_perf_cat.

              ASSIGN lt_app_serv_perf_cat_before[ key = lr_app_serv_perf_cat->key ] TO FIELD-SYMBOL(<fs_app_serv_perf_cat_before>).
              IF <fs_app_serv_perf_cat_before> IS ASSIGNED.
                "-----------------------------------
                " App server performance category
                " has changed
                "-----------------------------------
                IF lr_app_serv_perf_cat->hec_srv_perf_cat_guid IS NOT INITIAL                                          AND
                   lr_app_serv_perf_cat->hec_srv_perf_cat_guid <> <fs_app_serv_perf_cat_before>-hec_srv_perf_cat_guid.

                  " Set server RAM class and CPU
                  TRY.
                      DATA(ls_serv_perf_cat) = lt_serv_perf_cat[ hec_srv_perf_cat_guid = lr_app_serv_perf_cat->hec_srv_perf_cat_guid ].

                      lr_app_serv_perf_cat->hec_srv_perf_cat_descr = ls_serv_perf_cat-hec_srv_perf_cat_descr.
                      lr_app_serv_perf_cat->hec_srv_ram_class      = ls_serv_perf_cat-hec_srv_ram_class.
                      lr_app_serv_perf_cat->hec_srv_cpu_class      = ls_serv_perf_cat-hec_srv_cpu_class.
                      lr_app_serv_perf_cat->hec_tree_descr         = ls_serv_perf_cat-hec_srv_perf_cat_descr. "#EC CI_FLDEXT_OK[2215424]

                      lv_data_changed                              = abap_true.

                      " Set Value List Quantity
                      lr_app_serv_perf_cat->hec_srv_perf_cat_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server_perf_cat(
                                                                                              iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                              iv_inf_provider_guid   = lr_dlvy_unit->hec_inf_provider_guid
                                                                                              iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_app_serv_perf_cat->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL )
                                                                                              iv_is_app_server       = abap_true ) )
                                                                            THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                            ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                      IF lr_app_serv_perf_cat->hec_effort_required = abap_true.
                        " Get effort time based legoblock GUID
                        SELECT hec_ram_condition_op,
                               hec_ram_condition,
                               hec_timebased_effort_bb_guid
                          FROM /hec1/i_appservnodetbbbbasic
                         WHERE hec_apm_guid                   = @lr_landscape->hec_apm_guid                           AND
                               hec_apst_clustty_clustnty_guid = @lr_app_serv_perf_cat->hec_apst_clustty_clustnty_guid AND
                               hec_tier_cat_value             = @lr_app_serv_perf_cat->hec_tier_cat_value
                          INTO TABLE @DATA(lt_timebased_bb).


                        LOOP AT lt_timebased_bb ASSIGNING FIELD-SYMBOL(<fs_timebased_bb>).
                          DATA(lv_option) = SWITCH ddoption( <fs_timebased_bb>-hec_ram_condition_op
                                                             WHEN '<'  THEN 'LT'
                                                             WHEN '>'  THEN 'GT'
                                                             WHEN '='  THEN 'EQ'
                                                             WHEN '<=' THEN 'LE'
                                                             WHEN '>=' THEN 'GE'                      ).

                          INSERT VALUE #( sign   = 'I'
                                          option = lv_option
                                          low    = <fs_timebased_bb>-hec_ram_condition ) INTO TABLE lt_range.


                          IF lr_app_serv_perf_cat->hec_srv_ram_class IN lt_range.
                            DATA(lv_effort_bb_guid) = <fs_timebased_bb>-hec_timebased_effort_bb_guid.
                            EXIT. " >>>>>>>
                          ENDIF.
                        ENDLOOP.

                        IF lv_effort_bb_guid IS NOT INITIAL.
                          " Get the pricing
                          DATA(ls_price) = /hec1/cl_config_helper=>do_price_validation( iv_node_key          = is_ctx-node_key
                                                                                        it_key               = VALUE #( ( key = lr_app_serv_perf_cat->key ) )
                                                                                        io_read              = io_read
                                                                                        iv_effort_bb_guid    = lv_effort_bb_guid
                                                                                        iv_tier_is_dr_node   = lr_app_serv_perf_cat->hec_tier_is_dr_node
                                                                                        iv_dr_operating_mode = lr_app_serv_perf_cat->hec_dr_oper_mode_value ).

                          lr_app_serv_perf_cat->price = CORRESPONDING #( ls_price ).
                        ENDIF.
                      ENDIF. " IF lr_app_serv_perf_cat->hec_effort_required = abap_true.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  TRY.
                      DATA(lv_datacenter_guid) = lt_datacenter[ hec_node_datacenter = lr_app_serv_perf_cat->hec_tier_datacenter_guid ]-hec_datacenter_guid.

                      DATA(lt_server) = /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_server( iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                                                   iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                                                                   iv_sec_datacenter_guid = lv_datacenter_guid
                                                                                                                   iv_srv_perf_cat_guid   = lr_app_serv_perf_cat->hec_srv_perf_cat_guid ).

                      "-----------------------------------
                      " Fill action table for Update
                      " App server
                      "-----------------------------------
                      IF lines( lt_server ) = 1.
                        INSERT VALUE #( key                  = lt_app_server[ parent_key = lr_app_serv_perf_cat->key ]-key
                                        parent_key           = lr_app_serv_perf_cat->key
                                        hec_ip_server_guid   = lt_server[ 1 ]-value
                                        do_update_app_server = abap_true                                                    ) INTO TABLE lt_act_param_server.
                      ENDIF.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  CLEAR: lv_datacenter_guid,
                         lt_server.
                ENDIF. " IF lr_app_serv_perf_cat->hec_srv_perf_cat_guid IS NOT INITIAL AND...


                "-----------------------------------
                " App server storage is added
                "-----------------------------------
                IF lr_app_serv_perf_cat->hec_storage_qty > <fs_app_serv_perf_cat_before>-hec_storage_qty.
                  "-----------------------------------
                  " Fill action table for create
                  " App server storage amount
                  "-----------------------------------
                  INSERT VALUE #( key                    = lr_app_serv_perf_cat->key
                                 parent_key             = lr_app_serv_perf_cat->parent_key
                                 hec_storage_amount_qty = lr_app_serv_perf_cat->hec_storage_qty - <fs_app_serv_perf_cat_before>-hec_storage_qty ) INTO TABLE lt_act_param.

                  "-----------------------------------
                  " Fill action table for create
                  " App server storage
                  "-----------------------------------
                  TRY.
                      " App Storage is added without any parameters necessary
                      INSERT CORRESPONDING #( lt_app_server[ parent_key = lr_app_serv_perf_cat->key ] ) INTO TABLE lt_act_param_server_key.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  " Success message
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_storage_added
                                                                 iv_severity = /bobf/cm_frw=>co_severity_success
                                                                 iv_attr1    = CONV #( lr_app_serv_perf_cat->hec_storage_qty -
                                                                               <fs_app_serv_perf_cat_before>-hec_storage_qty )
                                                       CHANGING  co_message  = eo_message ).

                  " Set flag for deleting subnodes of standby node
                  IF lr_app_serv_perf_cat->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha          AND
                     lr_app_serv_perf_cat->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                     lr_app_serv_perf_cat->hec_app_node_default          = abap_true.
                    lv_data_changed            = abap_true.
                    DATA(lv_delete_ha_subnode) = abap_true.
                  ENDIF.

                ELSEIF lr_app_serv_perf_cat->hec_storage_qty < <fs_app_serv_perf_cat_before>-hec_storage_qty
                   AND lr_app_serv_perf_cat->hec_storage_qty < lines( VALUE /hec1/t_data_app_storageqty_ct( FOR app_storage_qty IN lt_app_storage_qty
                                                                                                                WHERE ( parent_key = lr_app_serv_perf_cat->key )
                                                                                                               ( app_storage_qty ) ) ).
                  DATA(lv_attr_name) = /hec1/if_configuration_c=>sc_node_attribute-app_server_perform_cat-hec_storage_qty.

                  " Error message
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                 is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                               key      = lr_app_serv_perf_cat->key
                                                                                               attributes = VALUE #( ( lv_attr_name ) ) )
                                                       CHANGING  co_message         = eo_message ).

                  " Set node number to value before update
                  lr_app_serv_perf_cat->hec_storage_qty = <fs_app_serv_perf_cat_before>-hec_storage_qty.
                  lv_data_changed = abap_true.
                ENDIF. " IF ls_db_server_perf_cat-hec_dsp_storage_qty > ls_db_server_perf_cat_old-hec_dsp_storage_qty.

                "-----------------------------------
                " Phase has changed -
                " update phase and inherit phase assignment
                "-----------------------------------
                IF lr_app_serv_perf_cat->hec_phase_guid NE <fs_app_serv_perf_cat_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_app_serv_perf_cat->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                     lr_app_serv_perf_cat->hec_app_node_default          = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_app_serv_perf_cat->key
                                    hec_phase_guid_new = lr_app_serv_perf_cat->hec_phase_guid
                                    hec_phase_guid_old = <fs_app_serv_perf_cat_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_app_serv_perf_cat->hec_phase_changed = abap_true.
                  lv_data_changed                         = abap_true.

                  " Set flag for deleting subnodes of standby node
                  IF lr_app_serv_perf_cat->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha          AND
                     lr_app_serv_perf_cat->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                     lr_app_serv_perf_cat->hec_app_node_default          = abap_true.
                    lv_delete_ha_subnode = abap_true.
                  ENDIF.

                ENDIF. "phasing changed
              ENDIF. "if <fs_app_serv_perf_cat> is assigned.


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_app_serv_perf_cat->hec_srv_perf_cat_guid IS NOT INITIAL AND
                                                                       lr_app_serv_perf_cat->hec_phase_guid        IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete          ).

              IF lv_inst_status <> lr_app_serv_perf_cat->hec_instance_status.
                lr_app_serv_perf_cat->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Fill action table for delete
              " App server standby node subnodes
              " or relase standby node
              "-----------------------------------
              IF lr_app_serv_perf_cat->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha          AND
                 lr_app_serv_perf_cat->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                 lr_app_serv_perf_cat->hec_app_node_default          = abap_true                                                AND
                 lv_data_changed                                     = abap_true.

                IF NOT line_exists( lt_act_param_node[ key = lr_app_serv_perf_cat->parent_key ] ).
                  TRY.
                      INSERT VALUE #( key                  = lr_app_serv_perf_cat->parent_key
                                      parent_key           = lt_app_node[ key = lr_app_serv_perf_cat->parent_key ]-parent_key
                                      do_release_ha_node   = COND #( WHEN lr_app_serv_perf_cat->hec_instance_status         = /hec1/if_config_constants=>gc_instance_status-complete    AND
                                                                          <fs_app_serv_perf_cat_before>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                                     THEN abap_true
                                                                     ELSE abap_false                                                  )
                                      do_delete_ha_subnode = COND #( WHEN lr_app_serv_perf_cat->hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete OR
                                                                          lv_delete_ha_subnode                      = abap_true
                                                                     THEN abap_true
                                                                     ELSE abap_false                                                                                 ) ) INTO TABLE lt_act_param_node.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                ENDIF.
              ENDIF. " IF lr_app_serv_perf_cat->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha


              "-----------------------------------
              " Modify App server performance
              " category
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_serv_perf_cat->key
                                   is_data = lr_app_serv_perf_cat ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_delete_ha_subnode,
                     lv_attr_name,
                     lv_option,
                     lv_effort_bb_guid,
                     ls_serv_perf_cat,
                     ls_price,
                     lt_range,
                     lt_timebased_bb.

              UNASSIGN <fs_app_serv_perf_cat_before>.

            ENDLOOP.

            "-----------------------------------
            " Set Create App Server amount
            " and Storage action to
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_qty( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_qty )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param ).


              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-app_server )
                  it_key          = VALUE #( FOR wa_act_serv IN lt_act_param_server_key
                                            ( key = wa_act_serv-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_storage )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                                                                          ).

            ENDIF. "lt_act_param is not initial


            "-----------------------------------
            " Set update App Server action to
            " general
            "-----------------------------------
            IF lt_act_param_server IS NOT INITIAL.
              CLEAR me->mr_act_param_server.
              me->mr_act_param_server = NEW /hec1/t_act_update_app_server( lt_act_param_server ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act_server IN lt_act_param_server
                                            ( key = wa_act_server-parent_key )        )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_app_server )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_server ).
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
            " Set update App node action to
            " general
            "-----------------------------------
            IF lt_act_param_node IS NOT INITIAL.
              CLEAR me->mr_act_param_app_node.
              me->mr_act_param_app_node = NEW /hec1/t_act_update_app_node( lt_act_param_node ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-app_node )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param_node
                                              ( key = wa_act_node-key )     )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_app_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_app_node                                                                                                       ).
            ENDIF.


            " ***************************************************************************
            " Update mode after app node update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_server_perform_cat-update_after_node.

            LOOP AT lt_app_serv_perf_cat REFERENCE INTO lr_app_serv_perf_cat.
              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_app_node[ key = lr_app_serv_perf_cat->parent_key ] TO <fs_app_node>.

              IF <fs_app_node> IS ASSIGNED.
                IF <fs_app_node>-hec_app_srv_perf_cat_qty > 0          AND
                   <fs_app_node>-hec_row_selectable       = abap_true.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_app_serv_perf_cat->hec_row_selectable.
                lr_app_serv_perf_cat->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Update App server cluster type
              "-----------------------------------
              IF lr_app_serv_perf_cat->hec_app_cluster_type_value <> <fs_app_node>-hec_app_cluster_type_value.
                lr_app_serv_perf_cat->hec_app_cluster_type_value = <fs_app_node>-hec_app_cluster_type_value.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Modify App server performance
              " category
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_serv_perf_cat->key
                                   is_data = lr_app_serv_perf_cat ).
              ENDIF.

              UNASSIGN <fs_app_node>.
              CLEAR: lv_release,
                     lv_data_changed.
            ENDLOOP. " LOOP AT lt_app_serv_perf_cat

        ENDCASE.



      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_app_storage_amoun_cr.

    DATA: lt_app_storage_qty         TYPE /hec1/t_data_app_storageqty_ct,
          lt_app_storage_qty_per_spc TYPE /hec1/t_data_app_storageqty_ct,
          lt_app_serv_perf_cat       TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_node                TYPE /hec1/t_data_app_node_ct,
          lt_app_storage_qty_before  TYPE /hec1/t_data_app_storageqty_ct,
          lt_app_server              TYPE /hec1/t_data_app_serv_ct,
          lt_app_storage             TYPE /hec1/t_data_app_storage_ct,
          lt_phase                   TYPE /hec1/t_data_phase_ct,
          lt_app_storage_qty_succ    TYPE /hec1/t_data_app_storageqty_ct,
          lt_act_param_node          TYPE /hec1/t_act_update_app_node,
          lt_act_param_storage       TYPE /bobf/t_frw_key,
          lt_act_param_succ          TYPE /hec1/t_act_set_success_predec,
          lt_act_param_phasing       TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    "-----------------------------------
    " Get data
    "-----------------------------------
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_storage_qty ).

    " Get App server performance category (parent)
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_storage_amount-to_parent
                                      IMPORTING et_data        = lt_app_serv_perf_cat ).

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
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage_amount-create.

            " Get for each App server performance category
            " the App storage amounts
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                        it_key         = VALUE #( FOR wa_spc IN lt_app_serv_perf_cat
                                                                                 ( key = wa_spc-key )                )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_storage_amount
                                              IMPORTING et_data        = lt_app_storage_qty_per_spc ).


            LOOP AT        lt_app_storage_qty
            REFERENCE INTO DATA(lr_app_storage_qty)
                     WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master.

              lr_app_storage_qty->hec_delete_visible = abap_true.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_app_storage_qty->hec_phase_guid IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_app_storage_qty->hec_instance_status.
                lr_app_storage_qty->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.

                " If standby node exist
                IF lr_app_storage_qty->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha          AND
                   lr_app_storage_qty->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                   lr_app_storage_qty->hec_app_node_default          = abap_true                                                AND
                   lr_app_storage_qty->hec_instance_status           = /hec1/if_config_constants=>gc_instance_status-complete.

                  io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                              it_key         = VALUE #( ( key = lr_app_storage_qty->key ) )
                                                              iv_fill_data   = abap_false
                                                              iv_association = /hec1/if_configuration_c=>sc_association-app_storage_amount-to_def_master_node
                                                    IMPORTING et_target_key  = DATA(lt_key) ).

                  IF NOT line_exists( lt_act_param_node[ key = lt_key[ 1 ]-key ] ).
                    TRY.
                        INSERT VALUE #( key                = lt_key[ 1 ]-key
                                        do_release_ha_node = abap_true       ) INTO TABLE lt_act_param_node.
                      CATCH cx_sy_itab_line_not_found.
                    ENDTRY.
                  ENDIF.
                ENDIF.
              ENDIF. " IF lv_inst_status <> lr_app_storage_qty->hec_instance_status.


              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_app_serv_perf_cat[ key = lr_app_storage_qty->parent_key ] TO FIELD-SYMBOL(<fs_app_serv_perf_cat>).
              IF <fs_app_serv_perf_cat> IS ASSIGNED.
                IF <fs_app_serv_perf_cat>-hec_srv_perf_cat_guid IS NOT INITIAL AND
                   <fs_app_serv_perf_cat>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_app_storage_qty->hec_row_selectable.
                lr_app_storage_qty->hec_row_selectable = lv_release.
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
                  is_node_data = lr_app_storage_qty
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              IF lv_data_changed = abap_false.
                lv_data_changed = lv_cr_data_changed.
              ENDIF.

              "-----------------------------------
              " Fill action table for setting
              " App server storage amount
              " successor/predecessor
              "-----------------------------------
              DATA(lv_node_count) = REDUCE i( INIT x = 0
                                              FOR <l> IN lt_app_storage_qty_per_spc WHERE ( parent_key = lr_app_storage_qty->parent_key )
                                              NEXT x = x + 1                                                                              ).

              IF NOT line_exists( lt_act_param_succ[ key = lr_app_storage_qty->parent_key ] ) AND lv_node_count > 1.
                TRY.
                    INSERT VALUE #( key         = lr_app_storage_qty->parent_key
                                    parent_key  = lt_app_serv_perf_cat[ key = lr_app_storage_qty->parent_key ]-parent_key
                                    hec_no_children_node = lv_node_count                                                  ) INTO TABLE lt_act_param_succ.
                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.


              "-----------------------------------
              " Modify App storage amount
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_storage_qty->key
                                   is_data = lr_app_storage_qty ).
              ENDIF.

              UNASSIGN <fs_app_serv_perf_cat>.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release,
                     lv_node_count.

            ENDLOOP.


            "-----------------------------------
            " Set update App node action to
            " general
            "-----------------------------------
            IF lt_act_param_node IS NOT INITIAL.
              CLEAR me->mr_act_param_app_node.
              me->mr_act_param_app_node = NEW /hec1/t_act_update_app_node( lt_act_param_node ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-app_node )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param_node
                                              ( key = wa_act_node-key )     )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_app_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_app_node                                                                                                       ).
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
                                             node_key  = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                             assoc_key = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_storage_amount )
                  it_key          = VALUE #( FOR wa_act_succ IN lt_act_param_succ
                                            ( key = wa_act_succ-key )    )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-set_success_predec )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

            ENDIF.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage_amount-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_app_storage_qty_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_storage_amount-to_parent
                                              IMPORTING et_target_key  = DATA(lt_app_serv_pc_key) ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                        it_key         = lt_app_serv_pc_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_server
                                              IMPORTING et_target_key  = DATA(lt_app_serv_key)
                                                        et_key_link    = DATA(lt_perf_cat_to_serv_link) ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server
                                                        it_key         = lt_app_serv_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server-app_storage
                                              IMPORTING et_target_key  = DATA(lt_app_storage_key)
                                                        et_key_link    = DATA(lt_serv_to_storage_link)
                                                        et_data        = lt_app_storage ).

            LOOP AT lt_app_storage_qty REFERENCE INTO lr_app_storage_qty.

              ASSIGN lt_app_storage_qty_before[ key = lr_app_storage_qty->key ] TO FIELD-SYMBOL(<fs_app_storage_qty_before>).
              IF <fs_app_storage_qty_before> IS ASSIGNED.
                "-----------------------------------
                " Physical, virtual or additional storage
                " has changed
                "-----------------------------------
                IF lr_app_storage_qty->hec_asq_main_stor_qty_virtual <> <fs_app_storage_qty_before>-hec_asq_main_stor_qty_virtual OR
                   lr_app_storage_qty->hec_asq_additional_stor_qty   <> <fs_app_storage_qty_before>-hec_asq_additional_stor_qty   OR
                   lr_app_storage_qty->hec_successor_guid            <> <fs_app_storage_qty_before>-hec_successor_guid            OR
                   lr_app_storage_qty->hec_predecessor_guid          <> <fs_app_storage_qty_before>-hec_predecessor_guid.

                  lr_app_storage_qty->hec_tree_descr = |{ lr_app_storage_qty->hec_asq_main_stor_qty_virtual } + { lr_app_storage_qty->hec_asq_additional_stor_qty } [GiB] |.
                  lv_data_changed = abap_true.

                  " Storage needs to be adjusted
                  LOOP AT lt_serv_to_storage_link REFERENCE INTO DATA(lr_serv_to_storage_link)
                    WHERE source_key = lt_perf_cat_to_serv_link[ source_key = lr_app_storage_qty->parent_key ]-target_key.

                    INSERT VALUE #( key = lr_serv_to_storage_link->target_key ) INTO TABLE lt_act_param_storage.

                  ENDLOOP.

                  " Set flag for deleting subnodes of standby node
                  IF lr_app_storage_qty->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha          AND
                     lr_app_storage_qty->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                     lr_app_storage_qty->hec_app_node_default          = abap_true.
                    DATA(lv_delete_ha_subnode) = abap_true.
                  ENDIF.
                ENDIF. "storage changed

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_app_storage_qty->hec_phase_guid NE <fs_app_storage_qty_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_app_storage_qty->key
                                  hec_phase_guid_new = lr_app_storage_qty->hec_phase_guid
                                  hec_phase_guid_old = <fs_app_storage_qty_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_app_storage_qty->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                  " Set flag for deleting subnodes of standby node
                  IF lr_app_storage_qty->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha          AND
                     lr_app_storage_qty->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                     lr_app_storage_qty->hec_app_node_default          = abap_true.
                    lv_delete_ha_subnode = abap_true.
                  ENDIF.
                ENDIF. "phasing changed

              ENDIF. " if <fs_app_storage_qty_before> is assigned
              " end of before <-> after comparison

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_app_storage_qty->hec_phase_guid IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_app_storage_qty->hec_instance_status.
                lr_app_storage_qty->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for delete
              " App server standby node subnodes
              " or relase standby node
              "-----------------------------------
              IF lr_app_storage_qty->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha          AND
                 lr_app_storage_qty->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                 lr_app_storage_qty->hec_app_node_default          = abap_true                                                AND
                 lv_data_changed                                   = abap_true.

                " Only one master node per storage amount can exist
                io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                            it_key         = VALUE #( ( key = lr_app_storage_qty->key ) )
                                                            iv_fill_data   = abap_false
                                                            iv_association = /hec1/if_configuration_c=>sc_association-app_storage_amount-to_def_master_node
                                                  IMPORTING et_target_key  = lt_key ).

                IF NOT line_exists( lt_act_param_node[ key = lt_key[ 1 ]-key ] ).
                  TRY.
                      INSERT VALUE #( key                  = lt_key[ 1 ]-key
                                      parent_key           = space
                                      do_release_ha_node   = COND #( WHEN lr_app_storage_qty->hec_instance_status         = /hec1/if_config_constants=>gc_instance_status-complete    AND
                                                                          <fs_app_storage_qty_before>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                                     THEN abap_true
                                                                     ELSE abap_false                                                  )
                                      do_delete_ha_subnode = COND #( WHEN lr_app_storage_qty->hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete OR
                                                                          lv_delete_ha_subnode                    = abap_true
                                                                     THEN abap_true
                                                                     ELSE abap_false                                                                                 ) ) INTO TABLE lt_act_param_node.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                ENDIF.
              ENDIF. " IF lr_app_serv_perf_cat->hec_app_cluster_type_value    = /hec1/if_config_constants=>gc_app_clust_node-ha


              "-----------------------------------
              " Modify
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_storage_qty->key
                                   is_data = lr_app_storage_qty ).
              ENDIF.

              UNASSIGN <fs_app_storage_qty_before>.
              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_delete_ha_subnode,
                     lt_key.

            ENDLOOP. "LOOP AT lt_app_storage_qty REFERENCE INTO lr_app_storage_qty.


            "-----------------------------------
            " Set update App Storage action to
            " general
            "-----------------------------------
            IF lt_act_param_storage IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-app_storage )
                  it_key          = lt_act_param_storage
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_app_storage )
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
            " Set update App node action to
            " general
            "-----------------------------------
            IF lt_act_param_node IS NOT INITIAL.
              CLEAR me->mr_act_param_app_node.
              me->mr_act_param_app_node = NEW /hec1/t_act_update_app_node( lt_act_param_node ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                               node_key = /hec1/if_configuration_c=>sc_node-app_node )
                    it_key          = VALUE #( FOR wa_act_node IN lt_act_param_node
                                              ( key = wa_act_node-key )     )
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_app_node )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param_app_node                                                                                                       ).
            ENDIF.


            " ***************************************************************************
            " Update mode after app server
            " performance category update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage_amount-update_after_serv_perf_cat.

            LOOP AT lt_app_storage_qty REFERENCE INTO lr_app_storage_qty.
              ASSIGN lt_app_serv_perf_cat[ key = lr_app_storage_qty->parent_key ] TO <fs_app_serv_perf_cat>.

              IF <fs_app_serv_perf_cat> IS ASSIGNED.
                IF <fs_app_serv_perf_cat>-hec_srv_perf_cat_guid IS NOT INITIAL AND
                   <fs_app_serv_perf_cat>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
*              IF lr_app_node->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
              IF lr_app_storage_qty->hec_row_selectable <> lv_release.
                lr_app_storage_qty->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

*              " Release instance for selection( standby node)
*              IF lr_app_storage_qty->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-standby                 AND
*                 me->check_standby_node_is_released( iv_is_app_server = abap_true
*                                                     iv_check_rule    = /hec1/if_bopf_constants=>gc_check_rule-storage_amount
*                                                     is_ctx           = is_ctx
*                                                     it_key           = it_key
*                                                     io_read          = io_read
*                                                     io_modify        = io_modify                                             ) = abap_true.
*
*                IF lr_app_node->hec_row_selectable <> lv_release.
*                  lr_app_node->hec_row_selectable = lv_release.
*                  lv_data_changed                 = abap_true.
*                ENDIF.
*              ENDIF.

              " Update App server cluster type
              IF lr_app_storage_qty->hec_app_cluster_type_value <> <fs_app_serv_perf_cat>-hec_app_cluster_type_value.
                lr_app_storage_qty->hec_app_cluster_type_value = <fs_app_serv_perf_cat>-hec_app_cluster_type_value.
                lv_data_changed = abap_true.
              ENDIF.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_storage_qty->key
                                   is_data = lr_app_storage_qty ).
              ENDIF.

              UNASSIGN <fs_app_serv_perf_cat>.
              CLEAR: lv_release,
                     lv_data_changed.
            ENDLOOP. " LOOP AT lt_app_storage_qty
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_app_storage_backu_cr.

    DATA: lt_app_backup_before     TYPE /hec1/t_data_app_backup_ct,
          lt_app_backup            TYPE /hec1/t_data_app_backup_ct,
          lt_app_backup_perstorage TYPE /hec1/t_data_app_backup_ct,
          lt_app_storage           TYPE /hec1/t_data_app_storage_ct,
          lt_phase                 TYPE /hec1/t_data_phase_ct,
          lt_act_param_succ        TYPE /hec1/t_act_set_success_predec,
          lt_act_param_phasing     TYPE TABLE OF /hec1/s_act_phase_inherit.



    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_backup ).

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
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage_backup-create.

            " Get App server storage (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_storage_backup-to_parent
                                              IMPORTING et_data        = lt_app_storage ).


            " Get for each App storage the App backup
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_storage
                                                        it_key         = VALUE #( FOR wa_node IN lt_app_storage
                                                                                 ( key = wa_node-key )          )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_storage-app_storage_backup
                                              IMPORTING et_data        = lt_app_backup_perstorage ).


            LOOP AT        lt_app_backup
            REFERENCE INTO DATA(lr_app_backup)
                     WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master.

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              lr_app_backup->hec_backup_class_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_backup(
                                                                               iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                               iv_tier_category_value = lr_app_backup->hec_tier_cat_value
                                                                               iv_is_app_backup       = abap_true ) )
                                                             THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                             ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              lr_app_backup->hec_delete_visible = abap_true.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_app_backup->hec_backup_class_guid IS NOT INITIAL AND
                                                                             lr_app_backup->hec_backup_size       IS NOT INITIAL AND
                                                                             lr_app_backup->hec_phase_guid        IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_app_backup->hec_instance_status.
                lr_app_backup->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.


              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_app_storage[ key = lr_app_backup->parent_key ] TO FIELD-SYMBOL(<fs_app_storage>).
              IF <fs_app_storage> IS ASSIGNED.
                IF <fs_app_storage>-hec_ip_storage_guid IS NOT INITIAL AND
                   <fs_app_storage>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
                UNASSIGN <fs_app_storage>.
              ENDIF.

              IF lv_release <> lr_app_backup->hec_row_selectable.
                lr_app_backup->hec_row_selectable = lv_release.
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
                  is_node_data = lr_app_backup
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              IF lv_data_changed = abap_false.
                lv_data_changed = lv_cr_data_changed.
              ENDIF.


              "-----------------------------------
              " Fill action table for setting
              " App server storage backup
              " successor/predecessor
              "-----------------------------------
              DATA(lv_node_count) = REDUCE i( INIT x = 0
                                              FOR <l> IN lt_app_backup_perstorage WHERE ( parent_key = lr_app_backup->parent_key )
                                              NEXT x = x + 1                                                                       ).

              IF NOT line_exists( lt_act_param_succ[ key = lr_app_backup->parent_key ] ) AND lv_node_count > 1.
                TRY.
                    INSERT VALUE #( key                  = lr_app_backup->parent_key
                                    parent_key           = lt_app_storage[ key = lr_app_backup->parent_key ]-parent_key
                                    hec_no_children_node = lv_node_count                                                ) INTO TABLE lt_act_param_succ.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.


              "-----------------------------------
              " Modify
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_backup->key
                                   is_data = lr_app_backup ).
              ENDIF.

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
                                             node_key  = /hec1/if_configuration_c=>sc_node-app_storage
                                             assoc_key = /hec1/if_configuration_c=>sc_association-app_storage-app_storage_backup )
                  it_key          = VALUE #( FOR wa_act_succ IN lt_act_param_succ
                                            ( key = wa_act_succ-key )    )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-set_success_predec )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage_backup-update.

            " Data before update
            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_app_backup_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get App Storage
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_false
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_storage_backup-to_parent
                                              IMPORTING et_target_key  = DATA(lt_app_storage_key)
                                                        et_data        = lt_app_storage ).


            LOOP AT lt_app_backup REFERENCE INTO lr_app_backup.
              ASSIGN lt_app_backup_before[ key = lr_app_backup->key ] TO FIELD-SYMBOL(<fs_app_backup_before>).

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_app_backup->hec_backup_class_guid IS NOT INITIAL AND
                                                                       lr_app_backup->hec_backup_size       IS NOT INITIAL AND
                                                                       lr_app_backup->hec_phase_guid        IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_app_backup->hec_instance_status.
                lr_app_backup->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              IF <fs_app_backup_before> IS ASSIGNED.
                "-----------------------------------
                " Backup GUID has changed
                "-----------------------------------
                IF lr_app_backup->hec_backup_class_guid IS NOT INITIAL AND
                  lr_app_backup->hec_backup_class_guid <> <fs_app_backup_before>-hec_backup_class_guid.

                  " Get backup class and backup class pricing
                  /hec1/cl_config_action_helper=>/hec1/if_bopf_action_helper~get_backup_class_and_price( EXPORTING is_ctx                  = CORRESPONDING #( is_ctx )
                                                                                                                   it_key                  = VALUE #( ( key = lr_app_backup->key ) )
                                                                                                                   iv_app_server           = abap_true
                                                                                                                   iv_tier_category_value  = lr_app_backup->hec_tier_cat_value
                                                                                                                   iv_tier_datacenter_guid = lr_app_backup->hec_tier_datacenter_guid
                                                                                                                   iv_backup_class_guid    = lr_app_backup->hec_backup_class_guid
                                                                                                                   io_read                 = io_read
                                                                                                         IMPORTING es_backup_class         = DATA(ls_backup_class)
                                                                                                                   es_backup_pricing       = DATA(ls_backup_pricing) ).

                  lr_app_backup->price                      = CORRESPONDING #( ls_backup_pricing ).
                  lr_app_backup->hec_backup_class_guid      = ls_backup_class-hec_backup_class_guid.
                  lr_app_backup->hec_backup_class_descr     = ls_backup_class-hec_backup_class_descr.
                  lr_app_backup->hec_tree_descr             = ls_backup_class-hec_backup_class_descr. "#EC CI_FLDEXT_OK[2215424]
                  lr_app_backup->hec_backup_month_price_fee = lr_app_backup->hec_backup_size * lr_app_backup->hec_month_price_eur.

                  lv_data_changed                           = abap_true.

                  " Set Value List Quantity
                  lr_app_backup->hec_backup_class_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_backup(
                                                                                   iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                   iv_tier_category_value = lr_app_backup->hec_tier_cat_value
                                                                                   iv_is_app_backup       = abap_true ) )
                                                                 THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                 ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                ENDIF. " IF <fs_app_backup_before>-hec_backup_class_guid IS NOT INITIAL AND...

                "-----------------------------------
                " Backup size has changed
                "-----------------------------------
                IF lr_app_backup->hec_backup_size IS NOT INITIAL AND
                   lr_app_backup->hec_backup_size <> <fs_app_backup_before>-hec_backup_size.
                  lr_app_backup->hec_backup_month_price_fee = lr_app_backup->hec_backup_size * lr_app_backup->hec_month_price_eur.

                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Phase has changed
                "-----------------------------------
                IF lr_app_backup->hec_phase_guid NE <fs_app_backup_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_app_backup->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                     lr_app_backup->hec_app_node_default          = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_app_backup->key
                                    hec_phase_guid_new = lr_app_backup->hec_phase_guid
                                    hec_phase_guid_old = <fs_app_backup_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_app_backup->hec_phase_changed = abap_true.
                  lv_data_changed                  = abap_true.

                ENDIF. "phasing changed
              ENDIF. "IF <fs_app_backup_before> IS ASSIGNED.


              "-----------------------------------
              " Modify App backup
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_backup->key
                                   is_data = lr_app_backup ).
              ENDIF.

              UNASSIGN <fs_app_backup_before>.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     ls_backup_class,
                     ls_backup_pricing.
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
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage_backup-update_after_storage.

            " Get App server storage (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_storage_backup-to_parent
                                              IMPORTING et_data        = lt_app_storage ).


            LOOP AT lt_app_backup REFERENCE INTO lr_app_backup.
              ASSIGN lt_app_storage[ key = lr_app_backup->parent_key ] TO <fs_app_storage>.

              IF <fs_app_storage> IS ASSIGNED.
                "-----------------------------------
                " Release instance for selection
                "-----------------------------------
                IF <fs_app_storage>-hec_ip_storage_guid IS NOT INITIAL AND
                   <fs_app_storage>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.

                IF lv_release <> lr_app_backup->hec_row_selectable.
                  lr_app_backup->hec_row_selectable = lv_release.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Update App server cluster type
                "-----------------------------------
                IF lr_app_backup->hec_app_cluster_type_value <> <fs_app_storage>-hec_app_cluster_type_value.
                  lr_app_backup->hec_app_cluster_type_value = <fs_app_storage>-hec_app_cluster_type_value.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Modify App storage backup
                "-----------------------------------
                IF lv_data_changed = abap_true.
                  io_modify->update( iv_node = is_ctx-node_key
                                     iv_key  = lr_app_backup->key
                                     is_data = lr_app_backup ).
                ENDIF.
              ENDIF. "  IF <fs_app_storage> IS ASSIGNED.

              UNASSIGN <fs_app_storage>.

              CLEAR: lv_data_changed,
                     lv_release.
            ENDLOOP.
        ENDCASE.
      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_app_storage_cr.

    DATA: lt_app_server            TYPE /hec1/t_data_app_serv_ct,
          lt_app_storage           TYPE /hec1/t_data_app_storage_ct,
          lt_app_storage_perserver TYPE /hec1/t_data_app_storage_ct,
          lt_app_storage_before    TYPE /hec1/t_data_app_storage_ct,
          lt_app_storage_succ      TYPE /hec1/t_data_app_storage_ct,
          lt_app_serv_perf_cat     TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_storage_qty       TYPE /hec1/t_data_app_storageqty_ct,
          lt_phase                 TYPE /hec1/t_data_phase_ct,
          lt_app_backup            TYPE /hec1/t_data_app_backup_ct,
          lt_act_param             TYPE /hec1/t_act_create_app_backup,
          lt_act_param_storage     TYPE /bobf/t_frw_key,
          lt_act_param_phasing     TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    "-----------------------------------
    " Get data
    "-----------------------------------
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_storage ).

    " Get App server (parent)
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_storage-to_parent
                                      IMPORTING et_data        = lt_app_server ).

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
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage-create.

            " Get for each App server the App storage
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server
                                                        it_key         = VALUE #( FOR wa_serv IN lt_app_server
                                                                                 ( key = wa_serv-key )                )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_server-app_storage
                                              IMPORTING et_data        = lt_app_storage_perserver ).

            LOOP AT        lt_app_storage
            REFERENCE INTO DATA(lr_app_storage)
                     WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master.

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              lr_app_storage->hec_ip_storage_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_storage(
                                                                              iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                              iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                              iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_app_storage->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL ) ) )
                                                            THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                            ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              lr_app_storage->hec_delete_visible = abap_false.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_app_storage->hec_ip_storage_guid IS NOT INITIAL AND
                                                                             lr_app_storage->hec_phase_guid      IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_app_storage->hec_instance_status.
                lr_app_storage->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_app_server[ key = lr_app_storage->parent_key ] TO FIELD-SYMBOL(<fs_app_server>).
              IF <fs_app_server> IS ASSIGNED.
                IF <fs_app_server>-hec_ip_server_guid IS NOT INITIAL AND
                   <fs_app_server>-hec_row_selectable = abap_true.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_app_storage->hec_row_selectable.
                lr_app_storage->hec_row_selectable = lv_release.
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
                  is_node_data = lr_app_storage
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              IF lv_data_changed = abap_false.
                lv_data_changed = lv_cr_data_changed.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " App server storage backup
              "-----------------------------------
              IF lr_app_storage->hec_backup_relev_value = '01'. " mandantory
                INSERT VALUE #( key            = lr_app_storage->key
                                parent_key     = lr_app_storage->parent_key
                                hec_backup_qty = lr_app_storage->hec_backup_qty ) INTO TABLE lt_act_param.
              ENDIF.

              "-----------------------------------
              " Fill action table for setting
              " App server storage
              " successor/predecessor
              "-----------------------------------
              DATA(lv_node_count) = REDUCE i( INIT x = 0
                                              FOR <l> IN lt_app_storage_perserver WHERE ( parent_key = lr_app_storage->parent_key )
                                              NEXT x = x + 1                                                                        ).

              IF NOT line_exists( lt_act_param_storage[ key = lr_app_storage->key ] ) AND lv_node_count > 1.
                TRY.
                    INSERT VALUE #( key = lr_app_storage->key ) INTO TABLE lt_act_param_storage.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.

              "-----------------------------------
              " Modify App server storage
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_storage->key
                                   is_data = lr_app_storage ).
              ENDIF.

              UNASSIGN <fs_app_server>.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release,
                     lv_node_count.

            ENDLOOP.

            "-----------------------------------
            " Set create App server storage
            " backup action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_backup( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_backup )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

            ENDIF.

            "-----------------------------------
            " Set update App storage action
            " to GENERAL
            "-----------------------------------
            IF lt_act_param_storage IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-app_storage )
                  it_key          = lt_act_param_storage
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_app_storage )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                                                                          ).
            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_app_storage_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get App server (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_storage-to_parent
                                              IMPORTING et_data        = lt_app_server ).

            " Get Backup
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-app_storage-app_storage_backup
                                              IMPORTING et_data        = lt_app_backup ).


            LOOP AT lt_app_storage REFERENCE INTO lr_app_storage.

              ASSIGN lt_app_storage_before[ key = lr_app_storage->key ] TO FIELD-SYMBOL(<fs_app_storage_before>).
              IF <fs_app_storage_before> IS ASSIGNED.

                "-----------------------------------
                " App storage IP GUID has changed
                "-----------------------------------
                IF lr_app_storage->hec_ip_storage_guid IS NOT INITIAL AND
                  lr_app_storage->hec_ip_storage_guid <> <fs_app_storage_before>-hec_ip_storage_guid.

                  " since this is the parent there can only be one entry
                  TRY.
                      DATA(ls_app_server) = lt_app_server[ key = lr_app_storage->parent_key ].
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  SELECT SINGLE *
                    FROM /hec1/i_storagelbbasic
                   WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid            AND
                         hec_sec_datacenter_guid = @ls_app_server-hec_sec_datacenter_guid AND
                         hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid   AND
                         hec_ip_storage_guid     = @lr_app_storage->hec_ip_storage_guid
                    INTO @DATA(ls_storage).

                  SELECT SINGLE * FROM /hec1/c_cbp_lb "#EC CI_ALL_FIELDS_NEEDED
                     INTO @DATA(ls_pricing)
                    WHERE hec_price_lb = @ls_storage-hec_cb_pricing_lb_guid.

                  lr_app_storage->*                    = CORRESPONDING #( BASE ( lr_app_storage->* ) ls_pricing ).
                  lr_app_storage->hec_ip_storage_guid  = ls_storage-hec_ip_storage_guid.
                  lr_app_storage->hec_storage_descr    = ls_storage-hec_storage_descr.
                  lr_app_storage->hec_month_price_fee  = lr_app_storage->hec_storage_quantity * lr_app_storage->hec_month_price_eur.
                  lr_app_storage->hec_tree_descr       = ls_storage-hec_storage_descr. "#EC CI_FLDEXT_OK[2215424]

                  lv_data_changed = abap_true.

                  " Set Value List Quantity
                  lr_app_storage->hec_ip_storage_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_storage(
                                                                                  iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                  iv_infra_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                                  iv_sec_datacenter_guid = VALUE #( lt_datacenter[ hec_node_datacenter = lr_app_storage->hec_tier_datacenter_guid ]-hec_sec_datacenter_guid OPTIONAL ) ) )
                                                                THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                ENDIF. "ip storage has changed

                "-----------------------------------
                " App storage amount has changed
                "-----------------------------------
                IF lr_app_storage->hec_storage_quantity IS NOT INITIAL                                 AND
                   lr_app_storage->hec_storage_quantity <> <fs_app_storage_before>-hec_storage_quantity.
                  lr_app_storage->hec_month_price_fee = lr_app_storage->hec_storage_quantity * lr_app_storage->hec_month_price_eur.

                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " App storage backup quantity is added
                "-----------------------------------
                IF lr_app_storage->hec_backup_qty > <fs_app_storage_before>-hec_backup_qty.

                  INSERT VALUE #( key            = lr_app_storage->key
                                  parent_key     = lr_app_storage->parent_key
                                  hec_backup_qty = lr_app_storage->hec_backup_qty - <fs_app_storage_before>-hec_backup_qty ) INTO TABLE lt_act_param.

                  " Success message
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_backup_added
                                                                 iv_severity = /bobf/cm_frw=>co_severity_success
                                                                 iv_attr1    = CONV #( lr_app_storage->hec_backup_qty -
                                                                               <fs_app_storage_before>-hec_backup_qty )
                                                       CHANGING  co_message  = eo_message ).

                ELSEIF lr_app_storage->hec_backup_qty < <fs_app_storage_before>-hec_backup_qty
                  AND lr_app_storage->hec_backup_qty < lines( VALUE /hec1/t_data_app_backup_ct( FOR app_backup IN lt_app_backup
                                                                                                    WHERE ( parent_key = lr_app_storage->key )
                                                                                                    ( app_backup ) ) ).
                  DATA(lv_attr_name) = /hec1/if_configuration_c=>sc_node_attribute-solution-hec_tier_qty_nprod_level.

                  " Error message
                  /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                 is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                               key      = lr_app_storage->key
                                                                                               attributes = VALUE #( ( lv_attr_name ) ) )
                                                       CHANGING  co_message         = eo_message ).

                  " Set node number to value before update
                  lr_app_storage->hec_backup_qty = <fs_app_storage_before>-hec_backup_qty.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Phase has changed - update phase and inherit phase assignment
                "-----------------------------------
                IF lr_app_storage->hec_phase_guid NE <fs_app_storage_before>-hec_phase_guid.
                  " Only for default master node
                  IF lr_app_storage->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                     lr_app_storage->hec_app_node_default          = abap_true.

                    APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                    hec_bopf_key       = lr_app_storage->key
                                    hec_phase_guid_new = lr_app_storage->hec_phase_guid
                                    hec_phase_guid_old = <fs_app_storage_before>-hec_phase_guid ) TO lt_act_param_phasing.
                  ENDIF.

                  lr_app_storage->hec_phase_changed = abap_true.
                  lv_data_changed                   = abap_true.

                ENDIF. "phasing changed
              ENDIF. "if <fs_app_storage_before> is assigned.


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_app_storage->hec_ip_storage_guid IS NOT INITIAL AND
                                                                       lr_app_storage->hec_phase_guid      IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_app_storage->hec_instance_status.
                lr_app_storage->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_storage->key
                                   is_data = lr_app_storage ).

              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     ls_app_server,
                     ls_pricing,
                     ls_storage.

              UNASSIGN <fs_app_storage_before>.

            ENDLOOP.

            "-----------------------------------
            " Set create App server storage
            " backup action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_app_backup( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_backup )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                                                                                                   ).

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

            " ***************************************************************************
            " Update mode after server update
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_storage-update_after_server.

            LOOP AT lt_app_storage REFERENCE INTO lr_app_storage.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_app_server[ key = lr_app_storage->parent_key ] TO <fs_app_server>.

              IF <fs_app_server> IS ASSIGNED.
                IF <fs_app_server>-hec_ip_server_guid IS NOT INITIAL AND
                   <fs_app_server>-hec_row_selectable = abap_true.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              IF lr_app_storage->hec_row_selectable            <> lv_release.
                lr_app_storage->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Update App server cluster type
              "-----------------------------------
              IF lr_app_storage->hec_app_cluster_type_value <> <fs_app_server>-hec_app_cluster_type_value.
                lr_app_storage->hec_app_cluster_type_value = <fs_app_server>-hec_app_cluster_type_value.
                lv_data_changed = abap_true.
              ENDIF.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_app_storage->key
                                   is_data = lr_app_storage ).
              ENDIF.

              UNASSIGN <fs_app_server>.
              CLEAR: lv_release,
                     lv_data_changed.
            ENDLOOP. "  LOOP AT lt_app_storage
        ENDCASE.



      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.
ENDCLASS.