CLASS /hec1/cl_config_action_app_se DEFINITION
  PUBLIC
  INHERITING FROM /HEC1/CL_LIB_A_SUPERCLASS
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.

    METHODS /bobf/if_frw_action~execute
        REDEFINITION .
  PROTECTED SECTION.
private section.

  data MR_ACT_PARAM_DELETE type ref to DATA .
  data MR_ACT_PARAM_CREATE type ref to DATA .

  methods DO_SYNCHRONIZE_APP_NODE
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ACT
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IO_MODIFY type ref to /BOBF/IF_FRW_MODIFY
      !IS_PARAMETERS type ref to DATA
    exporting
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EV_STATIC_ACTION_FAILED type ABAP_BOOL
      !ET_DATA type INDEX TABLE
      !ET_DATA_LINK type /BOBF/T_FRW_ACT_EXP_DATA_LINK
    raising
      /BOBF/CX_FRW .
  methods RESET_APP_BACKUP
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ACT
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IO_MODIFY type ref to /BOBF/IF_FRW_MODIFY
      !IS_PARAMETERS type ref to DATA
    exporting
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EV_STATIC_ACTION_FAILED type ABAP_BOOL
      !ET_DATA type INDEX TABLE
      !ET_DATA_LINK type /BOBF/T_FRW_ACT_EXP_DATA_LINK
    raising
      /BOBF/CX_FRW .
  methods RESET_APP_NODE
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ACT
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IO_MODIFY type ref to /BOBF/IF_FRW_MODIFY
      !IS_PARAMETERS type ref to DATA
    exporting
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EV_STATIC_ACTION_FAILED type ABAP_BOOL
      !ET_DATA type INDEX TABLE
      !ET_DATA_LINK type /BOBF/T_FRW_ACT_EXP_DATA_LINK
    raising
      /BOBF/CX_FRW .
  methods RESET_APP_SERVER
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ACT
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IO_MODIFY type ref to /BOBF/IF_FRW_MODIFY
      !IS_PARAMETERS type ref to DATA
    exporting
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EV_STATIC_ACTION_FAILED type ABAP_BOOL
      !ET_DATA type INDEX TABLE
      !ET_DATA_LINK type /BOBF/T_FRW_ACT_EXP_DATA_LINK
    raising
      /BOBF/CX_FRW .
  methods RESET_APP_SERVER_INSTANCE
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ACT
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IO_MODIFY type ref to /BOBF/IF_FRW_MODIFY
      !IS_PARAMETERS type ref to DATA
    exporting
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EV_STATIC_ACTION_FAILED type ABAP_BOOL
      !ET_DATA type INDEX TABLE
      !ET_DATA_LINK type /BOBF/T_FRW_ACT_EXP_DATA_LINK
    raising
      /BOBF/CX_FRW .
  methods RESET_APP_SERVER_PC
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ACT
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IO_MODIFY type ref to /BOBF/IF_FRW_MODIFY
      !IS_PARAMETERS type ref to DATA
    exporting
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EV_STATIC_ACTION_FAILED type ABAP_BOOL
      !ET_DATA type INDEX TABLE
      !ET_DATA_LINK type /BOBF/T_FRW_ACT_EXP_DATA_LINK
    raising
      /BOBF/CX_FRW .
  methods RESET_APP_STORAGE
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ACT
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IO_MODIFY type ref to /BOBF/IF_FRW_MODIFY
      !IS_PARAMETERS type ref to DATA
    exporting
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EV_STATIC_ACTION_FAILED type ABAP_BOOL
      !ET_DATA type INDEX TABLE
      !ET_DATA_LINK type /BOBF/T_FRW_ACT_EXP_DATA_LINK
    raising
      /BOBF/CX_FRW .
ENDCLASS.



CLASS /HEC1/CL_CONFIG_ACTION_APP_SE IMPLEMENTATION.


  METHOD /bobf/if_frw_action~execute.

    TRY.
        CASE is_ctx-act_key.
            " **********************************
            " App node Synchronize configuration
            " App cluster type: HA
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-app_node-sync_config.
            me->do_synchronize_app_node( EXPORTING is_ctx                  = is_ctx
                                                   it_key                  = it_key
                                                   io_read                 = io_read
                                                   io_modify               = io_modify
                                                   is_parameters           = is_parameters
                                         IMPORTING eo_message              = eo_message
                                                   et_failed_key           = et_failed_key
                                                   ev_static_action_failed = ev_static_action_failed
                                                   et_data                 = et_data
                                                   et_data_link            = et_data_link ).

            " **********************************
            " Reset App Server Instance
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-app_server_instance-reset_server_instance
            OR /hec1/if_configuration_c=>sc_action-app_server_instance-reset_operating_system
            OR /hec1/if_configuration_c=>sc_action-app_server_instance-modify_cluster_type.
            me->reset_app_server_instance( EXPORTING is_ctx                  = is_ctx
                                                     it_key                  = it_key
                                                     io_read                 = io_read
                                                     io_modify               = io_modify
                                                     is_parameters           = is_parameters
                                           IMPORTING eo_message              = eo_message
                                                     et_failed_key           = et_failed_key
                                                     ev_static_action_failed = ev_static_action_failed
                                                     et_data                 = et_data
                                                     et_data_link            = et_data_link ).

            " **********************************
            " Reset App Server Node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-app_node-reset_ha_info_prov_date  OR
               /hec1/if_configuration_c=>sc_action-app_node-modify_ha_type_prov_date OR
               /hec1/if_configuration_c=>sc_action-app_node-reset_ha_type.
            me->reset_app_node( EXPORTING is_ctx                  = is_ctx
                                          it_key                  = it_key
                                          io_read                 = io_read
                                          io_modify               = io_modify
                                          is_parameters           = is_parameters
                                IMPORTING eo_message              = eo_message
                                          et_failed_key           = et_failed_key
                                          ev_static_action_failed = ev_static_action_failed
                                          et_data                 = et_data
                                          et_data_link            = et_data_link ).


            " **********************************
            " Reset App Server Performance Category
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-app_server_perform_cat-reset_server_pc.
            me->reset_app_server_pc( EXPORTING is_ctx                  = is_ctx
                                               it_key                  = it_key
                                               io_read                 = io_read
                                               io_modify               = io_modify
                                               is_parameters           = is_parameters
                                     IMPORTING eo_message              = eo_message
                                               et_failed_key           = et_failed_key
                                               ev_static_action_failed = ev_static_action_failed
                                               et_data                 = et_data
                                               et_data_link            = et_data_link ).

            " **********************************
            " Reset App Server
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-app_server-reset_server.
            me->reset_app_server( EXPORTING is_ctx                  = is_ctx
                                            it_key                  = it_key
                                            io_read                 = io_read
                                            io_modify               = io_modify
                                            is_parameters           = is_parameters
                                  IMPORTING eo_message              = eo_message
                                            et_failed_key           = et_failed_key
                                            ev_static_action_failed = ev_static_action_failed
                                            et_data                 = et_data
                                            et_data_link            = et_data_link ).

            " **********************************
            " Reset App Storage
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-app_storage-reset_storage.
            me->reset_app_storage( EXPORTING is_ctx                  = is_ctx
                                             it_key                  = it_key
                                             io_read                 = io_read
                                             io_modify               = io_modify
                                             is_parameters           = is_parameters
                                   IMPORTING eo_message              = eo_message
                                             et_failed_key           = et_failed_key
                                             ev_static_action_failed = ev_static_action_failed
                                             et_data                 = et_data
                                             et_data_link            = et_data_link ).

            " **********************************
            " Reset App Backup
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-app_storage_backup-reset_backup.
            me->reset_app_backup( EXPORTING is_ctx                  = is_ctx
                                            it_key                  = it_key
                                            io_read                 = io_read
                                            io_modify               = io_modify
                                            is_parameters           = is_parameters
                                  IMPORTING eo_message              = eo_message
                                            et_failed_key           = et_failed_key
                                            ev_static_action_failed = ev_static_action_failed
                                            et_data                 = et_data
                                            et_data_link            = et_data_link ).

        ENDCASE.
      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD do_synchronize_app_node.

    CLEAR: eo_message,
           et_failed_key,
           ev_static_action_failed,
           et_data,
           et_data_link.


    " Disable determinations
    /hec1/cl_lib_d_superclass=>set_switch( abap_false ).


    /hec1/cl_config_action_helper=>/hec1/if_bopf_action_helper~do_synchronize_app_node( EXPORTING is_ctx                  = is_ctx
                                                                                                  it_key                  = it_key
                                                                                                  io_read                 = io_read
                                                                                                  io_modify               = io_modify
                                                                                                  is_parameters           = is_parameters
                                                                                        IMPORTING et_failed_key           = et_failed_key
                                                                                                  ev_static_action_failed = ev_static_action_failed
                                                                                                  et_data                 = et_data
                                                                                                  et_data_link            = et_data_link
                                                                                        CHANGING  co_message              = eo_message              ).

    " Enabale determinations
    /hec1/cl_lib_d_superclass=>set_switch( abap_true ).


  ENDMETHOD.


  METHOD reset_app_backup.

    DATA: lt_app_backup TYPE /hec1/t_data_app_backup_ct.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_backup   ).

    TRY.
        DATA(lr_app_backup) = NEW /hec1/s_data_app_backup_cs( lt_app_backup[ 1 ] ).
      CATCH cx_sy_itab_line_not_found.
        RETURN. ">>>
    ENDTRY.

    CLEAR: lr_app_backup->price,
           lr_app_backup->hec_backup_month_price_fee,
           lr_app_backup->hec_backup_class_descr,
           lr_app_backup->hec_backup_class_guid,
           lr_app_backup->hec_tree_descr.

    io_modify->update( iv_node           = is_ctx-node_key
                       iv_key            = lr_app_backup->key
                       is_data           = lr_app_backup ).

  ENDMETHOD.


  METHOD reset_app_server.

    DATA: lt_app_server   TYPE /hec1/t_data_app_serv_ct,
          lt_app_storage  TYPE /hec1/t_data_app_storage_ct,
          lt_modification TYPE /bobf/t_frw_modification.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_server   ).

    " Get App Storage
    io_read->retrieve_by_association( EXPORTING iv_node                 = is_ctx-node_key
                                                it_key                  = it_key
                                                iv_fill_data            = abap_true
                                                iv_association          = /hec1/if_configuration_c=>sc_association-app_server-app_storage
                                      IMPORTING et_data                 = lt_app_storage ).

    TRY.
        DATA(lr_app_server) = REF /hec1/s_data_app_serv_cs( lt_app_server[ 1 ] ).
      CATCH cx_sy_itab_line_not_found.
        RETURN. ">>>>>
    ENDTRY.

    CLEAR: lr_app_server->hec_ip_server_descr,
           lr_app_server->hec_ip_server_guid,
           lr_app_server->hec_host_type_descr,
           lr_app_server->hec_host_type_value,
           lr_app_server->hec_srv_ram_size,
           lr_app_server->hec_srv_cpu_size,
           lr_app_server->hec_sec_datacenter_guid,
           lr_app_server->hec_srv_main_storage_qty,
           lr_app_server->hec_tree_descr,
           lr_app_server->hec_as_flavour,
           lr_app_server->hec_saps,
           lr_app_server->hec_approval_needed,
           lr_app_server->price.

    lr_app_server->hec_ip_server_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.

    INSERT VALUE #( data        = lr_app_server
                    node        = /hec1/if_configuration_c=>sc_node-app_server
                    change_mode = /bobf/if_frw_c=>sc_modify_update
                    key         = lr_app_server->key
                    ) INTO TABLE lt_modification.

    LOOP AT lt_app_storage REFERENCE INTO DATA(lr_app_storage).

      CLEAR: lr_app_storage->hec_ip_storage_guid,
             lr_app_storage->hec_storage_descr,
             lr_app_storage->hec_month_price_fee,
             lr_app_storage->hec_tree_descr,
             lr_app_storage->price.

      lr_app_storage->hec_ip_storage_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.

      INSERT VALUE #( data        = lr_app_storage
                      node        = /hec1/if_configuration_c=>sc_node-app_storage
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_app_storage->key
                      ) INTO TABLE lt_modification.

    ENDLOOP. "lt_app_storage

    "-----------------------------------
    " Do Modify
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message) ).
    ENDIF.

  ENDMETHOD.


  METHOD reset_app_server_instance.

    DATA: lt_app_server_instance TYPE /hec1/t_data_app_serv_inst_ct,
          ls_action_param        TYPE /hec1/s_act_import_parameter, "parameters
          lt_solution            TYPE /hec1/t_data_solution_ct,
          lt_landscape           TYPE /hec1/t_config_root_ct,
          lt_app_node            TYPE /hec1/t_data_app_node_ct,
          lt_modification        TYPE /bobf/t_frw_modification,
          lt_act_param_delete    TYPE /bobf/t_frw_node,
          lt_act_param_create    TYPE /hec1/t_act_create_app_node.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_server_instance   ).

    " Get App Nodes
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-app_node
                                      IMPORTING et_data        = lt_app_node ).

    TRY.
        DATA(lr_app_server_instance) = REF /hec1/s_data_app_serv_inst_cs( lt_app_server_instance[ 1 ] ).
      CATCH cx_sy_itab_line_not_found.
        RETURN. ">>>>
    ENDTRY.

    CASE is_ctx-act_key.

      WHEN /hec1/if_configuration_c=>sc_action-app_server_instance-reset_operating_system
        OR /hec1/if_configuration_c=>sc_action-app_server_instance-reset_server_instance.

        " ***********************
        " Reset Operating System
        "
        "  these fields are also
        "  cleared when the app
        "  server instance is
        "  reset
        " ***********************
        CLEAR: lr_app_server_instance->hec_sol_apsi_oper_sys_guid,
               lr_app_server_instance->hec_operating_sys_guid,
               lr_app_server_instance->hec_operating_sys_value,
               lr_app_server_instance->hec_operating_sys_descr,
               lr_app_server_instance->hec_os_support_stat_value,
               lr_app_server_instance->hec_os_support_stat_descr,

               "clear os image (technical field)
               lr_app_server_instance->hec_asi_opsys_image,
               lr_app_server_instance->hec_asi_opsys_image_val,

               "clear patch level (technical field)
               lr_app_server_instance->hec_asi_patch_level_descr,
               lr_app_server_instance->hec_asi_patch_level_guid,
               lr_app_server_instance->hec_asi_patch_level_value,

               lr_app_server_instance->hec_os_support_stat_value,
               lr_app_server_instance->hec_os_support_stat_descr.

        lr_app_server_instance->hec_sol_apsi_oper_sys_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.
        lr_app_server_instance->hec_asi_opsys_image_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.
        lr_app_server_instance->hec_asi_patch_level_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.

        DATA(lv_changed) = abap_true.

        IF is_ctx-act_key = /hec1/if_configuration_c=>sc_action-app_server_instance-reset_server_instance.
          " **********************************
          " Reset App Server Instance
          " **********************************

          " Here all nodes are deleted

          CLEAR: lr_app_server_instance->hec_sol_tier_stack_si_guid,
                 lr_app_server_instance->hec_sol_tier_asi_descr,

                 " cluster type
                 lr_app_server_instance->hec_app_cluster_type_value,
                 lr_app_server_instance->hec_app_cluster_type_descr,
                 lr_app_server_instance->hec_app_cluster_type_guid,
                 lr_app_server_instance->hec_sol_apsi_clusttyp_guid,

                 lr_app_server_instance->hec_clu_support_stat_value,
                 lr_app_server_instance->hec_clu_support_stat_descr,

                 lr_app_server_instance->hec_tree_descr.

          lr_app_server_instance->hec_sol_tier_stack_si_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.
          lr_app_server_instance->hec_sol_apsi_clusttyp_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.

          "delete all nodes underneath
          LOOP AT lt_app_node REFERENCE INTO DATA(lr_app_node).

            " Delete DB Node
            INSERT VALUE #( node = /hec1/if_configuration_c=>sc_node-app_node
                            key  = lr_app_node->key ) INTO TABLE lt_act_param_delete.

          ENDLOOP.

          lv_changed = abap_true.

        ENDIF. " app server instance is changed

        " **************************
        " Modify Cluster Type
        " **************************
      WHEN /hec1/if_configuration_c=>sc_action-app_server_instance-modify_cluster_type.

        " Get Landscape
        io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                    it_key         = it_key
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-to_root
                                                    iv_fill_data   = abap_true
                                          IMPORTING et_data        = lt_landscape ).

        " Get Solution
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_false
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-to_parent
                                          IMPORTING et_target_key  = DATA(lt_solution_key) ).

        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                    it_key         = lt_solution_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-tier-to_parent
                                          IMPORTING et_data        = lt_solution ).

        " Master node will always stay. Depending on the cluster type another node will be added or removed.
        ASSIGN is_parameters->* TO FIELD-SYMBOL(<fs_parameters>).
        IF <fs_parameters> IS ASSIGNED.
          ls_action_param = <fs_parameters>. "#EC CI_FLDEXT_OK[2215424]

          TRY.
              DATA(lv_clusttyp_guid) = ls_action_param-name_value[ fieldname = /hec1/if_configuration_c=>sc_node_attribute-app_server_instance-hec_sol_apsi_clusttyp_guid ]-value.
            CATCH cx_sy_itab_line_not_found.
          ENDTRY.

        ENDIF. "<fs_parameters> is assigned.

        " get results from decision table (TODO: move to determination)
        DATA(ls_landscape) = VALUE #( lt_landscape[ 1 ] OPTIONAL ).

        SELECT SINGLE *
          FROM /hec1/i_appclustertypebasic
          INTO @DATA(ls_fdt_cluster_type)
         WHERE hec_apm_guid = @ls_landscape-hec_apm_guid
           AND hec_sol_tier_stack_si_guid = @lr_app_server_instance->hec_sol_tier_stack_si_guid "ls_app_server_inst_param-hec_sol_tier_stack_si_guid
           AND hec_sol_apsi_clusttyp_guid = @lv_clusttyp_guid. "ls_app_server_inst_param-hec_sol_apsi_clusttyp_guid.

        lr_app_server_instance->hec_sol_apsi_clusttyp_guid    = ls_fdt_cluster_type-hec_sol_apsi_clusttyp_guid.
        lr_app_server_instance->hec_app_serv_type_clust_guid  = ls_fdt_cluster_type-hec_app_serv_type_clust_guid.
        lr_app_server_instance->hec_app_cluster_type_value    = ls_fdt_cluster_type-hec_app_cluster_type_value.
        lr_app_server_instance->hec_app_cluster_type_descr    = ls_fdt_cluster_type-hec_app_cluster_type_descr.

        lv_changed = abap_true.

*        " get new node quantities from cluster node type
        SELECT *                              "#EC CI_ALL_FIELDS_NEEDED
          FROM /hec1/i_appclustnodetypebasic
          INTO TABLE @DATA(lt_fdt_cluster_node_type)
         WHERE hec_apm_guid = @ls_landscape-hec_apm_guid
           AND hec_app_serv_type_clust_guid = @lr_app_server_instance->hec_app_serv_type_clust_guid.

        " Get default master app node (relevant for adding nodes)
        DATA(lr_app_node_master) = NEW /hec1/s_data_app_node_cs( lt_app_node[ hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master "#EC CI_SORTSEQ
                                                                              hec_master_default            = abap_true ] ).

        " set quantity of node types and determine how many nodes need to be added and deleted
        " The result from the decision table contains one line for each required app node. The node type for each line defines the node type for the app node
        " A comparison needs to be made to see which nodes need to be added or removed. The master node will always stay

*                DATA(lv_master_node_lines) = lines( VALUE /hec1/t_data_app_node_ct( FOR wa IN lt_app_node
*                                                                  WHERE ( hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master )
*                                                                  ( wa ) ) ).

        SELECT COUNT( * )
          FROM @lt_fdt_cluster_node_type AS clust_node_type
         WHERE hec_app_clust_node_type_value = @/hec1/if_config_constants=>gc_app_clust_node_type-standby
          INTO @DATA(lv_standby_node_lines_req).

        DATA(lv_standby_node_lines_is) = lines( VALUE /hec1/t_data_app_node_ct( FOR app_node IN lt_app_node
                                                                              WHERE ( hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-standby )
                                                                              ( app_node ) ) ).

        " ************
        " delete node
        " ************
        IF lv_standby_node_lines_is GT lv_standby_node_lines_req.

          DATA(lv_delete_counter) = 0.

          SORT lt_app_node DESCENDING. "Delete, starting with latest
          LOOP AT lt_app_node REFERENCE INTO lr_app_node
            WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-standby.

            IF lv_delete_counter GE ( lv_standby_node_lines_is - lv_standby_node_lines_req ).
              CONTINUE. ">>>
            ENDIF.

            " Delete DB Node
            INSERT VALUE #( node = /hec1/if_configuration_c=>sc_node-app_node
                            key  = lr_app_node->key ) INTO TABLE lt_act_param_delete.

            ADD 1 TO lv_delete_counter.
          ENDLOOP.

          lr_app_server_instance->hec_app_standby_node_qty = lv_standby_node_lines_req.

          " *********
          " add node
          " *********
        ELSEIF lv_standby_node_lines_is LT lv_standby_node_lines_req.

          DATA(ls_fdt_clust_node_type) = VALUE #( lt_fdt_cluster_node_type[ hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-standby ] OPTIONAL ).

          DO ( lv_standby_node_lines_req - lv_standby_node_lines_is ) TIMES.

            "-----------------------------------
            " Fill action table for
            " create App node
            "-----------------------------------
            INSERT VALUE #( key               = lr_app_server_instance->key
                            parent_key        = lr_app_server_instance->parent_key
                            hec_app_cluster_type_value = SWITCH #( lr_app_server_instance->hec_app_cluster_type_value
                                                                   WHEN /hec1/if_config_constants=>gc_app_clust_node-none
                                                                   THEN /hec1/if_config_constants=>gc_app_clust_node-none
                                                                   WHEN /hec1/if_config_constants=>gc_app_clust_node-ha
                                                                   THEN /hec1/if_config_constants=>gc_app_clust_node-ha
                                                                   ELSE /hec1/if_config_constants=>gc_app_clust_node-none )
                            hec_default_app_server     = lr_app_server_instance->hec_default_app_server_inst
                            ) INTO TABLE lt_act_param_create.

          ENDDO.
          lr_app_server_instance->hec_app_standby_node_qty = lv_standby_node_lines_req.
        ENDIF.

    ENDCASE. "action

    IF lv_changed = abap_true.
      INSERT VALUE #( data        = lr_app_server_instance
                      node        = is_ctx-node_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_app_server_instance->key
                      ) INTO TABLE lt_modification.
    ENDIF.

    "-----------------------------------
    " Set delete action
    " to GENERAL
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
    " Set create DB/App server instance
    " action to general
    "-----------------------------------
    IF lt_act_param_create IS NOT INITIAL.
      CLEAR me->mr_act_param_create.
      me->mr_act_param_create = NEW /hec1/t_act_create_app_node( lt_act_param_create ).

      /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
          is_ctx          = CORRESPONDING #( is_ctx )
          it_key          = it_key
          iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_app_node )
          iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
          ir_act_param    = me->mr_act_param_create ).

    ENDIF.

    "-----------------------------------
    " Do Modify
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message) ).
    ENDIF.

    " TODO: Update Tree Selectability

  ENDMETHOD.


  METHOD reset_app_server_pc.

    " If the app server performance category is reset, all the nodes below it also need to be reset:
    "  - app storage qty (this does not need to be adjusted separately as the determination triggers an update
    "  - app storage
    "  - app server
    " if there is only one possible entry for storage or server, that entry is preset

    DATA: lt_app_server_pc TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_server    TYPE /hec1/t_data_app_serv_ct,
          lt_app_storage   TYPE /hec1/t_data_app_storage_ct,
          lt_modification  TYPE /bobf/t_frw_modification.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_server_pc   ).

    " Get App Server
    io_read->retrieve_by_association( EXPORTING iv_node                 = is_ctx-node_key
                                                it_key                  = it_key
                                                iv_fill_data            = abap_true
                                                iv_association          = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_server
                                      IMPORTING et_data                 = lt_app_server
                                                et_target_key           = DATA(lt_app_server_key) ).

    " Get App Storage
    io_read->retrieve_by_association( EXPORTING iv_node                 = /hec1/if_configuration_c=>sc_node-app_server
                                                it_key                  = lt_app_server_key
                                                iv_fill_data            = abap_true
                                                iv_association          = /hec1/if_configuration_c=>sc_association-app_server-app_storage
                                      IMPORTING et_data                 = lt_app_storage ).

    TRY.
        DATA(lr_app_server_pc) = REF #( lt_app_server_pc[ 1 ] ).
      CATCH cx_sy_itab_line_not_found.
        RETURN. ">>>>>
    ENDTRY.

    CLEAR: lr_app_server_pc->hec_srv_perf_cat_guid,
           lr_app_server_pc->hec_srv_perf_cat_descr,
           lr_app_server_pc->hec_srv_cpu_class,
           lr_app_server_pc->hec_srv_ram_class,
           lr_app_server_pc->price,
           lr_app_server_pc->hec_tree_descr.

    lr_app_server_pc->hec_srv_perf_cat_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.

    INSERT VALUE #( data        = lr_app_server_pc
                    node        = is_ctx-node_key
                    change_mode = /bobf/if_frw_c=>sc_modify_update
                    key         = lr_app_server_pc->key
                    ) INTO TABLE lt_modification.

    " there is only one server in each server performance category
    LOOP AT lt_app_server REFERENCE INTO DATA(lr_app_server).

      CLEAR: lr_app_server->hec_ip_server_descr,
             lr_app_server->hec_ip_server_guid,
             lr_app_server->hec_host_type_descr,
             lr_app_server->hec_host_type_value,
             lr_app_server->hec_srv_ram_size,
             lr_app_server->hec_srv_cpu_size,
             lr_app_server->hec_sec_datacenter_guid,
             lr_app_server->hec_srv_main_storage_qty,
             lr_app_server->hec_tree_descr,
             lr_app_server->hec_as_flavour,
             lr_app_server->hec_saps,
             lr_app_server->hec_approval_needed,
             lr_app_server->price.

      lr_app_server->hec_ip_server_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.

      INSERT VALUE #( data        = lr_app_server
                      node        = /hec1/if_configuration_c=>sc_node-app_server
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_app_server->key
                      ) INTO TABLE lt_modification.

    ENDLOOP. "lt_app_server

    " All Storages need to be updated
    LOOP AT lt_app_storage REFERENCE INTO DATA(lr_app_storage).

      CLEAR: lr_app_storage->hec_ip_storage_guid,
             lr_app_storage->hec_storage_descr,
             lr_app_storage->hec_month_price_fee,
             lr_app_storage->hec_tree_descr,
             lr_app_storage->price.

      lr_app_storage->hec_ip_storage_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.

      INSERT VALUE #( data        = lr_app_storage
                      node        = /hec1/if_configuration_c=>sc_node-app_storage
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_app_storage->key
                      ) INTO TABLE lt_modification.

    ENDLOOP. "lt_app_storage

    "-----------------------------------
    " Do Modify
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message) ).
    ENDIF.

  ENDMETHOD.


  METHOD reset_app_storage.

    DATA: lt_app_storage TYPE /hec1/t_data_app_storage_ct.

    CLEAR: eo_message,
           et_failed_key.

    " **********************************
    " Check instance status and switch
    " **********************************
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_storage   ).

    TRY.
        DATA(lr_app_storage) = REF #( lt_app_storage[ 1 ] ).
      CATCH cx_sy_itab_line_not_found.
        RETURN. ">>>>
    ENDTRY.

    CLEAR: lr_app_storage->hec_ip_storage_guid,
           lr_app_storage->hec_storage_descr,
           lr_app_storage->price,
           lr_app_storage->hec_tree_descr.

    io_modify->update( iv_node           = is_ctx-node_key
                       iv_key            = lr_app_storage->key
                       is_data           = lr_app_storage ).

  ENDMETHOD.


  METHOD reset_app_node.

    DATA: lt_app_node     TYPE /hec1/t_data_app_node_ct,
          lt_modification TYPE /bobf/t_frw_modification.


    CLEAR: eo_message,
           et_failed_key.

    " Get data
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_node ).

    LOOP AT lt_app_node REFERENCE INTO DATA(lr_app_node).

      CASE is_ctx-act_key.
        WHEN /hec1/if_configuration_c=>sc_action-app_node-reset_ha_info_prov_date.
          CLEAR: lr_app_node->hec_ha_inf_prov_date,
                 lr_app_node->hec_ha_info_guid,
                 lr_app_node->hec_ha_category_value,
                 lr_app_node->hec_ha_category_descr,
                 lr_app_node->hec_spc_inst_feature_value,
                 lr_app_node->hec_spc_inst_feature_descr.

        WHEN /hec1/if_configuration_c=>sc_action-app_node-modify_ha_type_prov_date OR
             /hec1/if_configuration_c=>sc_action-app_node-reset_ha_type.

          IF is_ctx-act_key = /hec1/if_configuration_c=>sc_action-app_node-modify_ha_type_prov_date.
            CLEAR lr_app_node->hec_ha_type_prov_date.
          ENDIF.

          CLEAR: lr_app_node->hec_ha_type_guid,
                 lr_app_node->hec_ha_type_value,
                 lr_app_node->hec_ha_type_descr,
                 lr_app_node->hec_ha_type_curr_suppstat_guid,
                 lr_app_node->hec_ha_type_curr_suppstat_val,
                 lr_app_node->hec_ha_type_curr_suppstat_desc.

      ENDCASE.

      " Fill modification table
      INSERT VALUE #( data        = lr_app_node
                      node        = /hec1/if_configuration_c=>sc_node-app_node
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_app_node->key                           ) INTO TABLE lt_modification.

    ENDLOOP.


    "-----------------------------------
    " Do Modify
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message) ).
    ENDIF.


  ENDMETHOD.
ENDCLASS.