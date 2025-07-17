CLASS /hec1/cl_config_action_db_se DEFINITION
  PUBLIC
  INHERITING FROM /hec1/cl_lib_a_superclass
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.

    METHODS /bobf/if_frw_action~execute
        REDEFINITION .
  PROTECTED SECTION.
private section.

  data MR_ACT_PARAM_DELETE type ref to DATA .
  data MR_ACT_PARAM_CREATE type ref to DATA .

  methods DO_SYNCHRONIZE_CONTAINER
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
  methods DO_SYNCHRONIZE_DB_NODE
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
  methods RESET_DB_BACKUP
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
  methods RESET_DB_SERVER
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
  methods RESET_DB_SERVER_INSTANCE
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
  methods RESET_DB_SERVER_PC
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
  methods RESET_DB_STORAGE
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
  methods RESET_INSTANCE_DB
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



CLASS /HEC1/CL_CONFIG_ACTION_DB_SE IMPLEMENTATION.


  METHOD /bobf/if_frw_action~execute.

    TRY.
        CASE is_ctx-act_key.
            " **********************************
            " DB node synchronize configuration
            " DB cluster type: HA/Multi node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-db_node-sync_config.
            me->do_synchronize_db_node( EXPORTING is_ctx                  = is_ctx
                                                  it_key                  = it_key
                                                  io_read                 = io_read
                                                  io_modify               = io_modify
                                                  is_parameters           = is_parameters
                                        IMPORTING eo_message              = eo_message
                                                  et_failed_key           = et_failed_key
                                                  ev_static_action_failed = ev_static_action_failed
                                                  et_data                 = et_data
                                                  et_data_link            = et_data_link            ).


            " **********************************
            " Synchronize configuration
            " Instance DB: container
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-instance_db-sync_config.
            me->do_synchronize_container( EXPORTING is_ctx                  = is_ctx
                                                    it_key                  = it_key
                                                    io_read                 = io_read
                                                    io_modify               = io_modify
                                                    is_parameters           = is_parameters
                                          IMPORTING eo_message              = eo_message
                                                    et_failed_key           = et_failed_key
                                                    ev_static_action_failed = ev_static_action_failed
                                                    et_data                 = et_data
                                                    et_data_link            = et_data_link            ).

            " **********************************
            " Reset DB Server Instance
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-db_server_instance-modify_server_instance
            OR /hec1/if_configuration_c=>sc_action-db_server_instance-modify_db_type
            OR /hec1/if_configuration_c=>sc_action-db_server_instance-modify_implement_type
            OR /hec1/if_configuration_c=>sc_action-db_server_instance-modify_instance_type
            OR /hec1/if_configuration_c=>sc_action-db_server_instance-modify_allocation
            OR /hec1/if_configuration_c=>sc_action-db_server_instance-reset_operating_system.
            me->reset_db_server_instance( EXPORTING is_ctx                  = is_ctx
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
            " Reset Instance DB
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-instance_db-modify_cluster_type.
            me->reset_instance_db( EXPORTING is_ctx                  = is_ctx
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
            " Reset DB Server Performance Category
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-db_server_perform_cat-reset_server_pc.
            me->reset_db_server_pc( EXPORTING is_ctx                  = is_ctx
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
            " Reset DB Server
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-db_server-reset_server.
            me->reset_db_server( EXPORTING is_ctx                  = is_ctx
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
            " Reset DB Storage
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-db_storage-reset_storage.
            me->reset_db_storage( EXPORTING is_ctx                  = is_ctx
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
            " Reset DB Backup
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-db_storage_backup-reset_backup.
            me->reset_db_backup( EXPORTING is_ctx                  = is_ctx
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


  METHOD do_synchronize_container.

    CLEAR: eo_message,
           et_failed_key,
           ev_static_action_failed,
           et_data,
           et_data_link.

    IF eo_message IS NOT BOUND.
      eo_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.


  ENDMETHOD.


  METHOD do_synchronize_db_node.

    CLEAR: eo_message,
           et_failed_key,
           ev_static_action_failed,
           et_data,
           et_data_link.


    " Disable determinations
    /hec1/cl_lib_d_superclass=>set_switch( abap_false ).

    /hec1/cl_config_action_helper=>/hec1/if_bopf_action_helper~do_synchronize_db_node( EXPORTING is_ctx                  = is_ctx
                                                                                                 it_key                  = it_key
                                                                                                 io_read                 = io_read
                                                                                                 io_modify               = io_modify
                                                                                                 is_parameters           = is_parameters
                                                                                       IMPORTING et_failed_key           = et_failed_key
                                                                                                 ev_static_action_failed = ev_static_action_failed
                                                                                                 et_data                 = et_data
                                                                                                 et_data_link            = et_data_link
                                                                                       CHANGING  co_message              = eo_message               ).

    " Enabale determinations
    /hec1/cl_lib_d_superclass=>set_switch( abap_true ).


  ENDMETHOD.


  METHOD reset_db_backup.

    DATA: lt_db_backup TYPE /hec1/t_data_db_backup_ct,
          ls_db_backup TYPE REF TO /hec1/s_data_db_backup_cs.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_backup ).

    TRY.
        ls_db_backup = NEW #( lt_db_backup[ 1 ] ).
      CATCH cx_sy_itab_line_not_found.
        RETURN. ">>>>>
    ENDTRY.

    CLEAR: ls_db_backup->price,
           ls_db_backup->hec_backup_month_price_fee,
           ls_db_backup->hec_backup_class_descr,
           ls_db_backup->hec_backup_class_guid,
           ls_db_backup->hec_tree_descr.

    io_modify->update( iv_node           = is_ctx-node_key
                       iv_key            = ls_db_backup->key
                       is_data           = ls_db_backup ).

  ENDMETHOD.


  METHOD reset_db_server.

    DATA: lt_db_server TYPE /hec1/t_data_db_serv_ct.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_server ).

    TRY.
        DATA(lr_db_server) = NEW /hec1/s_data_db_serv_cs( lt_db_server[ 1 ] ).
      CATCH cx_sy_itab_line_not_found.
        RETURN. ">>>>
    ENDTRY.

    CLEAR: lr_db_server->price,
           lr_db_server->hec_ip_server_guid,
           lr_db_server->hec_ip_server_descr,
           lr_db_server->hec_host_type_descr,
           lr_db_server->hec_host_type_value,
           lr_db_server->hec_ram_size,
           lr_db_server->hec_cpu_size,
           lr_db_server->hec_tree_descr.

    io_modify->update( iv_node           = is_ctx-node_key
                       iv_key            = lr_db_server->key
                       is_data           = lr_db_server ).

  ENDMETHOD.


  METHOD reset_db_server_instance.

    DATA: lt_db_server_instance TYPE /hec1/t_data_db_server_inst_ct.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_server_instance ).

    TRY.
        DATA(lr_db_server_instance) = NEW /hec1/s_data_db_server_inst_cs( lt_db_server_instance[ 1 ] ).
      CATCH cx_sy_itab_line_not_found.
        RETURN. ">>>>>
    ENDTRY.

    CASE is_ctx-act_key.
      WHEN /hec1/if_configuration_c=>sc_action-db_server_instance-modify_server_instance.
      WHEN /hec1/if_configuration_c=>sc_action-db_server_instance-modify_db_type.
      WHEN /hec1/if_configuration_c=>sc_action-db_server_instance-modify_implement_type.
      WHEN /hec1/if_configuration_c=>sc_action-db_server_instance-modify_instance_type.
      WHEN /hec1/if_configuration_c=>sc_action-db_server_instance-modify_allocation.

      WHEN /hec1/if_configuration_c=>sc_action-db_server_instance-reset_operating_system.

        CLEAR: lr_db_server_instance->hec_sol_dbst_oper_sys_guid,
               lr_db_server_instance->hec_operating_sys_value,
               lr_db_server_instance->hec_operating_sys_guid,
               lr_db_server_instance->hec_operating_sys_descr.

        DATA(lv_changed) = abap_true.
    ENDCASE.

    IF lv_changed = abap_true.
      io_modify->update( iv_node = is_ctx-node_key
                         iv_key  = lr_db_server_instance->key
                         is_data = lr_db_server_instance      ).
    ENDIF.


  ENDMETHOD.


  METHOD reset_db_server_pc.

    DATA: lt_db_server_pc   TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_storage_qty TYPE /hec1/t_data_db_storage_qty_ct,
          lt_db_server      TYPE /hec1/t_data_db_serv_ct,
          lt_db_storage     TYPE /hec1/t_data_db_storage_ct,
          lt_modification   TYPE /bobf/t_frw_modification.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_server_pc ).

    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount
                                      IMPORTING et_data        = lt_db_storage_qty ).

    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_server
                                      IMPORTING et_data        = lt_db_server
                                                et_target_key  = DATA(lt_db_server_key) ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server
                                                it_key         = lt_db_server_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server-db_storage
                                      IMPORTING et_data        = lt_db_storage ).

    TRY.
        DATA(lr_db_server_pc) = NEW /hec1/s_data_db_serv_pc_cs( lt_db_server_pc[ 1 ] ).
      CATCH cx_sy_itab_line_not_found.
        RETURN. ">>>>
    ENDTRY.

    CLEAR: lr_db_server_pc->hec_db_intended_srv_ram_class,
           lr_db_server_pc->hec_srv_cpu_class,
           lr_db_server_pc->hec_srv_ram_class,
           lr_db_server_pc->hec_srv_perf_cat_guid,
           lr_db_server_pc->hec_srv_perf_cat_descr,
           lr_db_server_pc->hec_tree_descr.

    INSERT VALUE #( data        = lr_db_server_pc
                    node        = is_ctx-node_key
                    change_mode = /bobf/if_frw_c=>sc_modify_update
                    key         = lr_db_server_pc->key
                    ) INTO TABLE lt_modification.

    " TODO: Move to determination for each level

    " DB Storage Qty
    LOOP AT lt_db_storage_qty REFERENCE INTO DATA(lr_db_storage_qty).

      CLEAR: lr_db_storage_qty->hec_dsq_main_stor_qty_physical,
             lr_db_storage_qty->hec_dsq_main_stor_qty_virtual,
             lr_db_storage_qty->hec_dsq_additional_stor_qty.

      INSERT VALUE #( data        = lr_db_storage_qty
                      node        = /hec1/if_configuration_c=>sc_node-db_storage_amount
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_db_storage_qty->key
                      ) INTO TABLE lt_modification.

    ENDLOOP.

    " DB Server
    LOOP AT lt_db_server REFERENCE INTO DATA(lr_db_server).

      CLEAR: lr_db_server->price,
             lr_db_server->hec_ip_server_guid,
             lr_db_server->hec_ip_server_descr,
             lr_db_server->hec_host_type_descr,
             lr_db_server->hec_host_type_value,
             lr_db_server->hec_ram_size,
             lr_db_server->hec_cpu_size,
             lr_db_server->hec_tree_descr.

      INSERT VALUE #( data        = lr_db_server
                      node        = /hec1/if_configuration_c=>sc_node-db_server
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_db_server->key
                      ) INTO TABLE lt_modification.

    ENDLOOP.

    " DB Storage
    LOOP AT lt_db_storage REFERENCE INTO DATA(lr_db_storage).

      CLEAR: lr_db_storage->hec_storage_quantity,
             lr_db_storage->hec_month_price_fee.

      INSERT VALUE #( data        = lr_db_storage
                      node        = /hec1/if_configuration_c=>sc_node-db_storage
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_db_storage->key
                      ) INTO TABLE lt_modification.

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


  METHOD reset_db_storage.

    DATA: lt_db_storage TYPE /hec1/t_data_db_storage_ct.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_storage ).

    TRY.
        DATA(lr_db_storage) = NEW /hec1/s_data_db_storage_cs( lt_db_storage[ 1 ] ).
      CATCH cx_sy_itab_line_not_found.
        RETURN. ">>>>>
    ENDTRY.

    CLEAR: lr_db_storage->price,
           lr_db_storage->hec_ip_storage_guid,
           lr_db_storage->hec_storage_descr,
           lr_db_storage->hec_tree_descr.

    io_modify->update( iv_node           = is_ctx-node_key
                       iv_key            = lr_db_storage->key
                       is_data           = lr_db_storage ).

  ENDMETHOD.


  METHOD reset_instance_db.

    "This is the modify action for the cluster type

    DATA: lt_instance_db       TYPE /hec1/t_data_db_inst_ct,
          lr_instance_db_param TYPE /hec1/s_data_db_inst_cs, "parameters
          lt_db_node           TYPE /hec1/t_data_db_node_ct,
          lt_solution          TYPE /hec1/t_data_solution_ct,
          lt_landscape         TYPE /hec1/t_data_landscape_ct,
          lt_tier              TYPE /hec1/t_data_tier_ct,
          lt_delivery_unit     TYPE /hec1/t_data_dlvy_unit_ct,
          lt_modification      TYPE /bobf/t_frw_modification,
          lt_act_param_delete  TYPE /bobf/t_frw_node,
          lt_act_param_create  TYPE /hec1/t_act_create_db_node.

    CLEAR: eo_message,
           et_failed_key.

    ASSIGN is_parameters->* TO FIELD-SYMBOL(<fs_parameters>).
    lr_instance_db_param = <fs_parameters>.  "#EC CI_FLDEXT_OK[2215424]

    " Get Instance DB
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_instance_db ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key       = is_ctx-node_key
                                                        it_key            = it_key
                                                        io_read           = io_read
                                              IMPORTING ev_root_key       = DATA(lv_root_key)
                                                        er_landscape      = DATA(lr_landscape)
                                                        er_delivery_unit  = DATA(lr_delivery_unit) ).

    " Get Landscape
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-to_root
                                                iv_fill_data   = abap_false
                                      IMPORTING et_target_key  = DATA(lt_key_root) ).

    " Get Delivery Unit
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = lt_key_root
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-delivery_unit
                                      IMPORTING et_data        = lt_delivery_unit ).

    " Get Solution
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-instance_db
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key_db_server_instance) ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                it_key         = lt_key_db_server_instance
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key_tier)
                                                et_data        = lt_tier ).

*    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
*                                                it_key         = lt_key_tier
*                                                iv_fill_data   = abap_true
*                                                iv_association = /hec1/if_configuration_c=>sc_association-tier-to_parent
*                                      IMPORTING et_data        = lt_solution ).

    " Get DB Node
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-db_node
                                      IMPORTING et_data        = lt_db_node ).

    TRY.
        DATA(lr_instance_db) = NEW /hec1/s_data_db_inst_cs( lt_instance_db[ 1 ] ).
      CATCH cx_sy_itab_line_not_found.
        RETURN. ">>>>
    ENDTRY.

    " get results from decision table (TODO: move to determination)
    TRY.
        DATA(lv_apm) = lr_landscape->hec_apm_guid.
        DATA(lr_tier) = REF #( lt_tier[ 1 ] ).
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.


    SELECT SINGLE *
      FROM /hec1/i_dbclustertypebasic
      INTO @DATA(ls_fdt_cluster_type)
     WHERE hec_apm_guid                   = @lr_landscape->hec_apm_guid
       AND hec_sol_tier_dsi_dbstype_guid  = @lr_instance_db->hec_sol_tier_dsi_dbstype_guid
       AND hec_sol_dbst_alloc_nodety_guid = @lr_instance_db->hec_sol_dbst_alloc_nodety_guid
       AND hec_dbst_nodety_clust_ty_guid  = @lr_instance_db_param-hec_dbst_nodety_clust_ty_guid.

    " *******************
    " 1. determine the required number of db nodes - only standby nodes
    " update value list and get new node quantities

    SELECT *
      FROM /hec1/i_dbclustnodetypebasic
      INTO TABLE @DATA(lt_fdt_cluster_node_type)
     WHERE hec_apm_guid                   = @lr_landscape->hec_apm_guid
       AND hec_dbst_nodety_clust_ty_guid  = @lr_instance_db_param-hec_dbst_nodety_clust_ty_guid.

    TRY.
        DATA(ls_fdt_clust_node_type_master) = lt_fdt_cluster_node_type[ hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master ].
        DATA(ls_fdt_clust_node_type_standby) = lt_fdt_cluster_node_type[ hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-standby ].

        IF ls_fdt_cluster_type-hec_db_cluster_type_value = /hec1/if_config_constants=>gc_db_clust_node-ha.
          ls_fdt_clust_node_type_standby-hec_db_node_limit_low  = 1.
          ls_fdt_clust_node_type_standby-hec_db_node_limit_high = 1.
        ENDIF.

        DATA(ls_fdt_clust_node_type_worker) = lt_fdt_cluster_node_type[ hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-worker ].
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.


    TRY.
        DATA(lr_db_node_master) = REF #( lt_db_node[ hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master ] ).
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

    " ************
    " delete node
    " ************
    IF ls_fdt_clust_node_type_standby-hec_db_node_limit_high LT lr_instance_db->hec_db_standby_node_qty.

      DATA(lv_delete_counter) = 0.

      SORT lt_db_node DESCENDING. "Delete, starting with latest
      LOOP AT lt_db_node REFERENCE INTO DATA(lr_db_node) WHERE hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-standby.

        IF lv_delete_counter GE ( lr_instance_db->hec_db_standby_node_qty - ls_fdt_clust_node_type_standby-hec_db_node_limit_high ).
          CONTINUE. ">>>
        ENDIF.

        " Delete DB Node
        INSERT VALUE #( node = /hec1/if_configuration_c=>sc_node-db_node
                        key  = lr_db_node->key ) INTO TABLE lt_act_param_delete.

        ADD 1 TO lv_delete_counter.
      ENDLOOP.

      lr_instance_db->hec_db_standby_node_qty = ls_fdt_clust_node_type_standby-hec_db_node_limit_high.

      " *********
      " add node
      " *********
    ELSEIF ls_fdt_clust_node_type_standby-hec_db_node_limit_low GT lr_instance_db->hec_db_standby_node_qty.

      " Get effort building block GUID
      SELECT SINGLE hec_timebased_effort_bb_guid
        FROM /hec1/i_dbservnodetbbbbasic
        INTO @DATA(lv_fdt_effort_bb_guid)
       WHERE hec_apm_guid                  = @lr_landscape->hec_apm_guid
         AND hec_dbst_clustty_clustntyguid = @ls_fdt_clust_node_type_standby-hec_dbst_clustty_clustntyguid
         AND hec_tier_cat_value            = @lr_instance_db->hec_tier_cat_value.

      SELECT SINGLE * FROM /hec1/c_tbe_bb
         INTO @DATA(ls_fdt_effort_timebased_bb)
        WHERE hec_timebased_effort_bb_guid = @lv_fdt_effort_bb_guid.

      DATA(ls_pricing) = CORRESPONDING /hec1/s_timebased_effort_price( ls_fdt_effort_timebased_bb ).

      " Get effort lego block GUID
      SELECT SINGLE *                         "#EC CI_ALL_FIELDS_NEEDED
        FROM /hec1/i_efforttimebasedlbbasic
        INTO @DATA(ls_fdt_effort)
       WHERE hec_apm_guid                 = @lr_landscape->hec_apm_guid
         AND hec_timebased_effort_lb_guid = @lv_fdt_effort_bb_guid.

      " Get Efforts
      IF ls_fdt_effort-hec_timebased_effort_lb_guid IS NOT INITIAL.
        SELECT SINGLE * FROM /hec1/c_tbp_lb   "#EC CI_ALL_FIELDS_NEEDED
           INTO @DATA(ls_effort_timebased_lb)
          WHERE hec_timebased_price_lb = @ls_fdt_effort-hec_timebased_effort_lb_guid.

        ls_pricing = VALUE #( BASE ls_pricing
                              hec_timebased_price_lb          = ls_effort_timebased_lb-hec_timebased_price_lb
                              hec_timeb_price_lb_descr        = ls_effort_timebased_lb-hec_timeb_price_lb_descr
                              hec_operation_rate              = ls_effort_timebased_lb-hec_operation_rate
                              hec_setup_rate                  = ls_effort_timebased_lb-hec_setup_rate
                              hec_monthly_setup_fee           = ls_pricing-hec_one_time_setup_effort    * ls_effort_timebased_lb-hec_setup_rate
                              hec_monthly_operation_fee       = ls_pricing-hec_monthly_operating_effort * ls_effort_timebased_lb-hec_operation_rate ).
      ENDIF.

      "-----------------------------------
      " Fill action table for create
      " instance DB action
      "-----------------------------------
      INSERT VALUE #( key                         = lr_instance_db->key
                      parent_key                  = lr_instance_db->parent_key
                      hec_cluster_node_type_value = ls_fdt_clust_node_type_standby-hec_db_clust_node_type_value
                      hec_def_master_node         = abap_true
                      hec_db_node_qty             = ( ls_fdt_clust_node_type_standby-hec_db_node_limit_low - lr_instance_db->hec_db_standby_node_qty )
                      ) INTO TABLE lt_act_param_create.

      lr_instance_db->hec_db_standby_node_qty = ls_fdt_clust_node_type_standby-hec_db_node_limit_low.

    ENDIF.

    " Update Field values
    lr_instance_db->hec_dbst_nodety_clust_ty_guid  = ls_fdt_cluster_type-hec_dbst_nodety_clust_ty_guid.
    lr_instance_db->hec_db_cluster_type_descr      = ls_fdt_cluster_type-hec_db_cluster_type_descr.
    lr_instance_db->hec_db_cluster_type_value      = ls_fdt_cluster_type-hec_db_cluster_type_value.
    lr_instance_db->hec_db_cluster_type_guid       = ls_fdt_cluster_type-hec_db_cluster_type_guid.
    lr_instance_db->hec_db_master_node_limit_qty   = ls_fdt_clust_node_type_master-hec_db_node_limit_high.
    lr_instance_db->hec_db_master_node_lower_qty   = ls_fdt_clust_node_type_master-hec_db_node_limit_low.
*        lr_instance_db->hec_db_master_node_qty         = ls_fdt_clust_node_type_master-hec_db_.
    lr_instance_db->hec_db_standby_node_limit_qty  = ls_fdt_clust_node_type_standby-hec_db_node_limit_high.
    lr_instance_db->hec_db_standby_node_lower_qty  = ls_fdt_clust_node_type_standby-hec_db_node_limit_low.
*        lr_instance_db->hec_db_standby_node_qty        = ls_fdt_clust_node_type_standby-hec_db_.
    lr_instance_db->hec_db_worker_node_limit_qty  = ls_fdt_clust_node_type_worker-hec_db_node_limit_high.
    lr_instance_db->hec_db_worker_node_lower_qty  = ls_fdt_clust_node_type_worker-hec_db_node_limit_low.

    INSERT VALUE #( data        = lr_instance_db
                    node        = /hec1/if_configuration_c=>sc_node-instance_db
                    change_mode = /bobf/if_frw_c=>sc_modify_update
                    key         = lr_instance_db->key
                    ) INTO TABLE lt_modification.

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
    " Set create DB Node instance
    " action to general
    "-----------------------------------
    IF lt_act_param_create IS NOT INITIAL.
      CLEAR me->mr_act_param_create.
      me->mr_act_param_create = NEW /hec1/t_act_create_db_node( lt_act_param_create ).

      /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
          is_ctx          = CORRESPONDING #( is_ctx )
          it_key          = it_key
          iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_db_node )
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

  ENDMETHOD.
ENDCLASS.