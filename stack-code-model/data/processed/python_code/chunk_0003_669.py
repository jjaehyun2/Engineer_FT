class /HEC1/CL_CONFIG_ACTION_INTERN definition
  public
  final
  create private

  global friends /HEC1/CL_CONFIG_DET_GENERAL .

public section.

  interfaces /HEC1/IF_CONFIG_ACTION_INTERN .
  PROTECTED SECTION.
private section.

  aliases COPY_NODE
    for /HEC1/IF_CONFIG_ACTION_INTERN~COPY_NODE .
  aliases CREATE_APP_NODE
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_APP_NODE .
  aliases CREATE_APP_SERVER
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_APP_SERVER .
  aliases CREATE_APP_SERVER_PC
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_APP_SERVER_PC .
  aliases CREATE_APP_STORAGE
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_APP_STORAGE .
  aliases CREATE_APP_STORAGE_AMOUNT
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_APP_STORAGE_AMOUNT .
  aliases CREATE_APP_STORAGE_BACKUP
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_APP_STORAGE_BACKUP .
  aliases CREATE_DB_NODE
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_DB_NODE .
  aliases CREATE_DB_SERVER
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_DB_SERVER .
  aliases CREATE_DB_SERVER_PC
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_DB_SERVER_PC .
  aliases CREATE_DB_STORAGE
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_DB_STORAGE .
  aliases CREATE_DB_STORAGE_AMOUNT
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_DB_STORAGE_AMOUNT .
  aliases CREATE_DB_STORAGE_BACKUP
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_DB_STORAGE_BACKUP .
  aliases CREATE_DELIVERY_UNIT
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_DELIVERY_UNIT .
  aliases CREATE_INSTANCE_DB
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_INSTANCE_DB .
  aliases CREATE_MAN_SERV_BASELINE
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_MAN_SERV_BASELINE .
  aliases CREATE_MATERIAL
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_MATERIAL .
  aliases CREATE_PHASE
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_PHASE .
  aliases CREATE_SERVER_INSTANCE
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_SERVER_INSTANCE .
  aliases CREATE_SOFTWARE_ITEM
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_SOFTWARE_ITEM .
  aliases CREATE_TIER
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_TIER .
  aliases CREATE_TIER_SLA
    for /HEC1/IF_CONFIG_ACTION_INTERN~CREATE_TIER_SLA .
  aliases DELETE_NODE
    for /HEC1/IF_CONFIG_ACTION_INTERN~DELETE_NODE .
  aliases INHERIT_PHASE_ASSIGNMENT
    for /HEC1/IF_CONFIG_ACTION_INTERN~INHERIT_PHASE_ASSIGNMENT .
  aliases SET_SUCCESSOR_PREDECESSOR
    for /HEC1/IF_CONFIG_ACTION_INTERN~SET_SUCCESSOR_PREDECESSOR .
  aliases UPDATE_ADDITIONAL_SERVICE
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_ADDITIONAL_SERVICE .
  aliases UPDATE_APP_NODE
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_APP_NODE .
  aliases UPDATE_APP_SERVER
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_APP_SERVER .
  aliases UPDATE_APP_SERVER_PERF_CAT
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_APP_SERVER_PERF_CAT .
  aliases UPDATE_APP_STORAGE
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_APP_STORAGE .
  aliases UPDATE_APP_STORAGE_AMOUNT
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_APP_STORAGE_AMOUNT .
  aliases UPDATE_APP_STORAGE_BACKUP
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_APP_STORAGE_BACKUP .
  aliases UPDATE_CONNECTIVITY
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_CONNECTIVITY .
  aliases UPDATE_DATACENTER
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_DATACENTER .
  aliases UPDATE_DB_NODE
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_DB_NODE .
  aliases UPDATE_DB_SERVER
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_DB_SERVER .
  aliases UPDATE_DB_SERVER_INSTANCE
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_DB_SERVER_INSTANCE .
  aliases UPDATE_DB_SERVER_PERF_CAT
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_DB_SERVER_PERF_CAT .
  aliases UPDATE_DB_STORAGE
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_DB_STORAGE .
  aliases UPDATE_DB_STORAGE_AMOUNT
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_DB_STORAGE_AMOUNT .
  aliases UPDATE_DB_STORAGE_BACKUP
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_DB_STORAGE_BACKUP .
  aliases UPDATE_DELIVERY_UNIT
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_DELIVERY_UNIT .
  aliases UPDATE_IF_BASELINE
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_IF_BASELINE .
  aliases UPDATE_INSTANCE_DB
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_INSTANCE_DB .
  aliases UPDATE_LANDSCAPE
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_LANDSCAPE .
  aliases UPDATE_MAN_SERV_BASELINE
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_MAN_SERV_BASELINE .
  aliases UPDATE_PHASE
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_PHASE .
  aliases UPDATE_SOLUTION
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_SOLUTION .
  aliases UPDATE_STORAGE_BACKUP_PRICE
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_STORAGE_BACKUP_PRICE .
  aliases UPDATE_TIER
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_TIER .
  aliases UPDATE_TIER_ADD_SERVICE
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_TIER_ADD_SERVICE .
  aliases UPDATE_TIER_FROM_LANDSCAPE
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_TIER_FROM_LANDSCAPE .
  aliases UPDATE_TIER_LT_BACKUP
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_TIER_LT_BACKUP .
  aliases UPDATE_TIER_SOFTWARE
    for /HEC1/IF_CONFIG_ACTION_INTERN~UPDATE_TIER_SOFTWARE .

  class-data MO_INSTANCE type ref to /HEC1/CL_CONFIG_ACTION_INTERN .
  data MR_ACT_PARAM type ref to DATA .
  data MR_ACT_PARAM_MATERIAL_ADD type ref to DATA .
  data MR_ACT_PARAM_SW_ITEM_ADD type ref to DATA .
  data MR_ACT_PARAM_DELETE type ref to DATA .

  class-methods GET_INSTANCE
    returning
      value(RO_INSTANCE) type ref to /HEC1/IF_CONFIG_ACTION_INTERN .
  methods CONSTRUCTOR .
ENDCLASS.



CLASS /HEC1/CL_CONFIG_ACTION_INTERN IMPLEMENTATION.


  METHOD /hec1/if_config_action_intern~delete_node.

    " This method allows the deletion of multiple nodes.
    " It should only be used inside the application
    " If a node is deleted through a user-action (e.g. pressing a button) the action DELETE_NODE on the root-node should be used.

    DATA: lt_modification    TYPE /bobf/t_frw_modification,
          lt_phase           TYPE /hec1/t_data_phase_ct,

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

    FIELD-SYMBOLS: <fs_param> TYPE /bobf/t_frw_node.

    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_param>.

    IF <fs_param> IS NOT ASSIGNED.
      RETURN. ">>>>>>
    ENDIF.

    " Check for generated phases. Those phases need to be deleted with the objects
    lt_modification = /hec1/cl_config_helper=>delete_generated_phases( iv_node_key         = is_ctx-node_key
                                                                       it_key              = it_key
                                                                       io_read             = io_read
                                                                       it_param_child_list = <fs_param> ).

    "-----------------------------------
    " Add input parameters to modification table
    "-----------------------------------
    LOOP AT <fs_param> ASSIGNING FIELD-SYMBOL(<fs_param_line>).

      INSERT VALUE #( node        = <fs_param_line>-node
                      change_mode = /bobf/if_frw_c=>sc_modify_delete
                      key         = <fs_param_line>-key ) INTO TABLE lt_modification.

    ENDLOOP.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.

    " **************************************************************************************************************************************************
    " Attention!!!!!!
    " This is only a temporary solution, because this is
    " a mix between UI logic and BOPF logic. Normally no
    " UI logic has to be set into a BOPF object. But at
    " the moment there is the problem, that the Application
    " is not running with FBI, therefore we can't control
    " the tree about the FBI feeder class

    " Switch to FBI, this part can be deleted
    LOOP AT lt_modification INTO DATA(ls_modification).
      /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~delete( iv_node_key = ls_modification-key ).
    ENDLOOP.

  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~inherit_phase_assignment.

    " ***************************************************************************
    " In this method we inherit the phase assignment. If a phase is cleared, the
    " empty phase assignment is passed on. Phases are either inherited to the
    " children, or the successors get the successor phase assigned.
    "
    " In addition, this method defines whether a phase can be assigned on the nodes.
    " If a phase is assigned automatically, it usually cannot be changed by the user.
    " ***************************************************************************

    DATA: lt_tier                TYPE /hec1/t_data_tier_ct,
          lt_tier_sla            TYPE /hec1/t_data_tier_sla_ct,
          lt_tier_all            TYPE /hec1/t_data_tier_ct,
          lt_material            TYPE /hec1/t_data_material_ct,
          lt_software_item       TYPE /hec1/t_data_sw_item_ct,
          lt_app_si              TYPE /hec1/t_data_app_serv_inst_ct,
          lt_db_si               TYPE /hec1/t_data_db_server_inst_ct,
          lt_instance_db         TYPE /hec1/t_data_db_inst_ct,
          lt_db_node             TYPE /hec1/t_data_db_node_ct,
          lt_db_server           TYPE /hec1/t_data_db_serv_ct,
          lt_db_server_all       TYPE /hec1/t_data_db_serv_ct,
          lt_db_storage          TYPE /hec1/t_data_db_storage_ct,
          lt_db_backup           TYPE /hec1/t_data_db_backup_ct,
          lt_db_backup_all       TYPE /hec1/t_data_db_backup_ct,
          lt_db_serv_pc          TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_serv_pc_all      TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_storage_qty      TYPE /hec1/t_data_db_storage_qty_ct,
          lt_db_storage_qty_all  TYPE /hec1/t_data_db_storage_qty_ct,
          lt_app_node            TYPE /hec1/t_data_app_node_ct,
          lt_app_serv_pc         TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_serv_pc_all     TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_storage_qty     TYPE /hec1/t_data_app_storageqty_ct,
          lt_app_storage_qty_all TYPE /hec1/t_data_app_storageqty_ct,
          lt_app_server          TYPE /hec1/t_data_app_serv_ct,
          lt_app_server_all      TYPE /hec1/t_data_app_serv_ct,
          lt_app_storage         TYPE /hec1/t_data_app_storage_ct,
          lt_app_storage_all     TYPE /hec1/t_data_app_storage_ct,
          lt_app_backup          TYPE /hec1/t_data_app_backup_ct,
          lt_app_backup_all      TYPE /hec1/t_data_app_backup_ct,

          lt_phase               TYPE /hec1/t_data_phase_ct,
          lt_phase_successor     TYPE /hec1/t_data_phase_ct,
          lt_parameter           TYPE /hec1/t_act_phase_inherit,

          lt_modification        TYPE /bobf/t_frw_modification.

    CLEAR: eo_message,
           et_failed_key.

    "is parameter will contain new PHASE_GUID and old PHASE_GUID
    ASSIGN ir_parameter->* TO FIELD-SYMBOL(<fs_parameter>).
    lt_parameter = <fs_parameter>.

    SORT lt_parameter ASCENDING BY hec_bopf_key.
    DELETE ADJACENT DUPLICATES FROM lt_parameter.

    " ***************************************************************************
    " Get Data
    " Get all the data outside any loops
    " ***************************************************************************

    io_read->get_root_key( EXPORTING iv_node       = is_ctx-node_key
                                     it_key        = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = lt_root_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                      IMPORTING et_data        = lt_phase ).

    CASE is_ctx-node_key.
        "-----------------------------------
        " Tier
        "-----------------------------------
      WHEN /hec1/if_configuration_c=>sc_node-tier.

        io_read->retrieve( EXPORTING iv_node      = is_ctx-node_key
                                     it_key       = it_key
                                     iv_fill_data = abap_true
                           IMPORTING et_data      = lt_tier ).

        io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-tier-material
                                          IMPORTING et_data        = lt_material ).

        io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-tier-tier_sla
                                          IMPORTING et_data        = lt_tier_sla ).

        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-tier-app_server_instance
                                          IMPORTING et_data        = lt_app_si ).

        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-tier-db_server_instance
                                          IMPORTING et_data        = lt_db_si ).

        IF line_exists( lt_tier[ hec_related_stack = abap_true ] ).
          io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-solution
                                                      it_key         = VALUE #( FOR wa IN lt_tier
                                                                                ( key = wa-parent_key ) )
                                                      iv_fill_data   = abap_true
                                                      iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                            IMPORTING et_data        = lt_tier_all ).
        ENDIF.

        "-----------------------------------
        " Material
        "-----------------------------------
      WHEN /hec1/if_configuration_c=>sc_node-material.

        io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                     it_key  = it_key
                           IMPORTING et_data = lt_material ).

        io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-material-software_item
                                          IMPORTING et_data        = lt_software_item ).

        "-----------------------------------
        " DB Server Instance
        "-----------------------------------
      WHEN /hec1/if_configuration_c=>sc_node-db_server_instance.

        io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                     it_key  = it_key
                           IMPORTING et_data = lt_db_si ).

        " get db instance
        io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-instance_db
                                          IMPORTING et_data        = lt_instance_db ).

        "-----------------------------------
        " Instance DB
        "-----------------------------------
      WHEN /hec1/if_configuration_c=>sc_node-instance_db.

        io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                     it_key  = it_key
                           IMPORTING et_data = lt_instance_db ).

        " get db node
        io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-instance_db-db_node
                                          IMPORTING et_data        = lt_db_node ).

        "-----------------------------------
        " DB Node
        "-----------------------------------
      WHEN /hec1/if_configuration_c=>sc_node-db_node.

        io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                     it_key  = it_key
                           IMPORTING et_data = lt_db_node ).

        io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                    it_key         = it_key
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                                                    iv_fill_data   = abap_true
                                          IMPORTING et_data        = lt_db_serv_pc ).

        "-----------------------------------
        " DB Server Performance Category
        "-----------------------------------
      WHEN /hec1/if_configuration_c=>sc_node-db_server_perform_cat.

        io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                     it_key  = it_key
                           IMPORTING et_data = lt_db_serv_pc ).

        " Get all other db server pc; the successor/predecessor link is created through the node-attribute and not the bopf key !!!
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_false
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-to_parent
                                          IMPORTING et_target_key  = DATA(lt_db_node_key) ).

        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_node
                                                    it_key         = lt_db_node_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                                          IMPORTING et_data        = lt_db_serv_pc_all ) .

        "get all db storage quantity
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount
                                          IMPORTING et_data        = lt_db_storage_qty_all ).

        "get all db server
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_server
                                          IMPORTING et_data        = lt_db_server_all ).

        "-----------------------------------
        " DB Storage Amount
        "-----------------------------------
      WHEN /hec1/if_configuration_c=>sc_node-db_storage_amount.

        " get db storage amount
        io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                     it_key  = it_key
                           IMPORTING et_data = lt_db_storage_qty ).

        " get db server performance category (parent)
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_storage_amount
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_false
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_storage_amount-to_parent
                                          IMPORTING et_target_key  = DATA(lt_db_serv_pc_key) ).

        " get db server
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                    it_key         = lt_db_serv_pc_key
                                                    iv_fill_data   = abap_false
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_server
                                          IMPORTING et_target_key  = DATA(lt_db_server_key) ).

        " get db storage
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server
                                                    it_key         = lt_db_server_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_server-db_storage
                                          IMPORTING et_data        = lt_db_storage ).

        " Get all other db storage qtys; the successor/predecessor link is created through the node-attribute and not the bopf key !!!
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                    it_key         = lt_db_serv_pc_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount
                                          IMPORTING et_data        = lt_db_storage_qty_all ) .

        "-----------------------------------
        " DB Storage
        "-----------------------------------
      WHEN /hec1/if_configuration_c=>sc_node-db_storage.

        io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                     it_key  = it_key
                           IMPORTING et_data = lt_db_storage ).

        "change db storage backup
        io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_storage-db_storage_backup
                                          IMPORTING et_data        = lt_db_backup ).

        "-----------------------------------
        " DB Backup
        "-----------------------------------
      WHEN /hec1/if_configuration_c=>sc_node-db_storage_backup.

        " get db backup
        io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                     it_key  = it_key
                           IMPORTING et_data = lt_db_backup ).

        " get db storage (parent)
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_storage_backup
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_false
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_storage_backup-to_parent
                                          IMPORTING et_target_key  = DATA(lt_db_storage_key) ).

        " Get all other db backups; the successor/predecessor link is created through the node-attribute and not the bopf key !!!
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_storage
                                                    it_key         = lt_db_storage_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_storage-db_storage_backup
                                          IMPORTING et_data        = lt_db_backup_all ).

        "-----------------------------------
        " App Server Instance
        "-----------------------------------
      WHEN /hec1/if_configuration_c=>sc_node-app_server_instance.

        io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                     it_key  = it_key
                           IMPORTING et_data = lt_app_si ).

        " get app instance
        io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-app_node
                                          IMPORTING et_data        = lt_app_node ).

        "-----------------------------------
        " App Node
        "-----------------------------------
      WHEN /hec1/if_configuration_c=>sc_node-app_node.

        io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                     it_key  = it_key
                           IMPORTING et_data = lt_app_node ).

        io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                    it_key         = it_key
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
                                                    iv_fill_data   = abap_true
                                          IMPORTING et_data        = lt_app_serv_pc ).

        "-----------------------------------
        " App Server Performance Category
        "-----------------------------------
      WHEN /hec1/if_configuration_c=>sc_node-app_server_perform_cat.

        io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                     it_key  = it_key
                           IMPORTING et_data = lt_app_serv_pc ).

        " Get all other db server pc; the successor/predecessor link is created through the node-attribute and not the bopf key !!!
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_false
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_parent
                                          IMPORTING et_target_key  = DATA(lt_app_node_key) ).

        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
                                                    it_key         = lt_app_node_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
                                          IMPORTING et_data        = lt_app_serv_pc_all ) .

        "get all db storage quantity
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_storage_amount
                                          IMPORTING et_data        = lt_app_storage_qty_all ).

        "get all db server
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_server
                                          IMPORTING et_data        = lt_app_server_all ).

        "-----------------------------------
        " App Storage Amount
        "-----------------------------------
      WHEN /hec1/if_configuration_c=>sc_node-app_storage_amount.

        " get app storage amount
        io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                     it_key  = it_key
                           IMPORTING et_data = lt_app_storage_qty ).

        " get app server performance category (parent)
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_storage_amount
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_false
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_storage_amount-to_parent
                                          IMPORTING et_target_key  = DATA(lt_app_serv_pc_key) ).

        " get app server
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                    it_key         = lt_app_serv_pc_key
                                                    iv_fill_data   = abap_false
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_server
                                          IMPORTING et_target_key  = DATA(lt_app_server_key) ).

        " get app storage
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server
                                                    it_key         = lt_app_server_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_server-app_storage
                                          IMPORTING et_data        = lt_app_storage ).

        " Get all other app storage qtys; the successor/predecessor link is created through the node-attribute and not the bopf key !!!
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                    it_key         = lt_app_serv_pc_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_storage_amount
                                          IMPORTING et_data        = lt_app_storage_qty_all ) .

        "-----------------------------------
        " App Storage
        "-----------------------------------
      WHEN /hec1/if_configuration_c=>sc_node-app_storage.

        io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                     it_key  = it_key
                           IMPORTING et_data = lt_app_storage ).

        "change app storage backup
        io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_storage-app_storage_backup
                                          IMPORTING et_data        = lt_app_backup ).

        "-----------------------------------
        " App Backup
        "-----------------------------------
      WHEN /hec1/if_configuration_c=>sc_node-app_storage_backup.

        " get app backup
        io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                     it_key  = it_key
                           IMPORTING et_data = lt_app_backup ).

        " get app storage (parent)
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_storage_backup
                                                    it_key         = it_key
                                                    iv_fill_data   = abap_false
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_storage_backup-to_parent
                                          IMPORTING et_target_key  = DATA(lt_app_storage_key) ).

        " Get all other db backups; the successor/predecessor link is created through the node-attribute and not the bopf key !!!
        io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_storage
                                                    it_key         = lt_app_storage_key
                                                    iv_fill_data   = abap_true
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_storage-app_storage_backup
                                          IMPORTING et_data        = lt_app_backup_all ).

    ENDCASE. "is_ctx-node_key

    " ***************************************************************************
    " Update Phases
    " ***************************************************************************
    LOOP AT lt_parameter ASSIGNING FIELD-SYMBOL(<fs_phase_parameter>).

      IF    <fs_phase_parameter>-hec_phase_guid_new IS INITIAL
        AND <fs_phase_parameter>-hec_phase_guid_old IS INITIAL.
        RETURN. ">>>>
      ENDIF.

      "-----------------------------------
      " get old and new phase
      "-----------------------------------
      TRY.
          " phase guid needs to be converted to raw value to be able to read the bopf-node directly
          " phase_guid and phase-key contain the same converted value

          IF <fs_phase_parameter>-hec_phase_guid_old IS NOT INITIAL.
            DATA(lr_phase_old) = NEW /hec1/s_data_phase_cs( lt_phase[ hec_node_phase = <fs_phase_parameter>-hec_phase_guid_old ] ).
          ENDIF.

          IF <fs_phase_parameter>-hec_phase_guid_new IS NOT INITIAL.
            DATA(lr_phase_new) = NEW /hec1/s_data_phase_cs( lt_phase[ hec_node_phase = <fs_phase_parameter>-hec_phase_guid_new ] ).
          ENDIF.

          "-----------------------------------
          " Update new phase
          "-----------------------------------
          IF lr_phase_new IS NOT INITIAL.
            lr_phase_new->hec_phase_assigned = abap_true.
            lr_phase_new->hec_phase_assigned_qty = lr_phase_new->hec_phase_assigned_qty + 1.

            INSERT VALUE #( data        = lr_phase_new
                            node        = /hec1/if_configuration_c=>sc_node-phase
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_phase_new->key    ) INTO TABLE lt_modification.

          ENDIF.
          "-----------------------------------
          " Update old phase
          "-----------------------------------
          IF lr_phase_old IS NOT INITIAL.
            lr_phase_old->hec_phase_assigned = COND #( WHEN lr_phase_old->hec_phase_assigned_qty = 1
                                                  THEN abap_false
                                                  ELSE abap_true ).
            lr_phase_old->hec_phase_assigned_qty = lr_phase_old->hec_phase_assigned_qty - 1.

            INSERT VALUE #( data        = lr_phase_old
                            node        = /hec1/if_configuration_c=>sc_node-phase
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_phase_old->key    ) INTO TABLE lt_modification.

          ENDIF.

        CATCH cx_uuid_error.
        CATCH cx_sy_itab_line_not_found.

      ENDTRY.

      " ***************************************************************************
      " Pass on Phase assignment
      " ***************************************************************************
      CASE is_ctx-node_key.
          "-----------------------------------
          " Tier
          "-----------------------------------
        WHEN /hec1/if_configuration_c=>sc_node-tier.

          LOOP AT lt_tier ASSIGNING FIELD-SYMBOL(<fs_tier>) WHERE hec_related_stack = abap_true.

            TRY.
                DATA(lr_tier) = NEW /hec1/s_data_tier_cs( lt_tier_all[ hec_related_stack = <fs_tier>-hec_related_stack ] ).
                lr_tier->hec_phase_guid = <fs_phase_parameter>-hec_phase_guid_new.
                lr_tier->hec_phase_assign_allowed = abap_true.

                INSERT VALUE #( data        = lr_tier
                                node        = /hec1/if_configuration_c=>sc_node-tier
                                change_mode = /bobf/if_frw_c=>sc_modify_update
                                key         = lr_tier->key    ) INTO TABLE lt_modification.

              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

          ENDLOOP. "lt_tier
          CLEAR lr_tier.

          "-----------------------------------
          "change Tier SLA
          "-----------------------------------
          LOOP AT lt_tier_sla REFERENCE INTO DATA(lr_tier_sla).

            " set phase
            lr_tier_sla->hec_phase_guid = <fs_phase_parameter>-hec_phase_guid_new.
            lr_tier_sla->hec_phase_assign_allowed = abap_false.

            INSERT VALUE #( data        = lr_tier_sla
                            node        = /hec1/if_configuration_c=>sc_node-tier_sla
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_tier_sla->key    ) INTO TABLE lt_modification.

          ENDLOOP. "lt_tier_sla
          CLEAR lr_tier_sla.

          "-----------------------------------
          "change material
          "-----------------------------------
          LOOP AT lt_material REFERENCE INTO DATA(lr_material).

            " set phase
            lr_material->hec_phase_guid = <fs_phase_parameter>-hec_phase_guid_new.
            lr_material->hec_phase_assign_allowed = COND #( WHEN <fs_phase_parameter>-hec_phase_guid_new IS INITIAL
                                                              OR lr_material->hec_material_rel_value = /hec1/if_config_constants=>gc_material_rel-mandatory
                                                            THEN abap_false
                                                            ELSE abap_true ).

            INSERT VALUE #( data        = lr_material
                            node        = /hec1/if_configuration_c=>sc_node-material
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_material->key    ) INTO TABLE lt_modification.

          ENDLOOP. "lt_material
          CLEAR lr_material.

          "-----------------------------------
          "change app server instance
          "-----------------------------------
          LOOP AT lt_app_si REFERENCE INTO DATA(lr_app_si).
            lr_app_si->hec_phase_guid = <fs_phase_parameter>-hec_phase_guid_new.
            "for the default app server the phasing is fixed and set by the system
            lr_app_si->hec_phase_assign_allowed = COND #( WHEN <fs_phase_parameter>-hec_phase_guid_new IS NOT INITIAL
                                                            OR lr_app_si->hec_default_app_server_inst = abap_true
                                                          THEN abap_false
                                                          ELSE abap_true ).

            INSERT VALUE #( data        = lr_app_si
                            node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_app_si->key    ) INTO TABLE lt_modification.

          ENDLOOP. "lt_app_si
          CLEAR lr_app_si.

          "-----------------------------------
          "change db server instance
          "-----------------------------------
          LOOP AT lt_db_si REFERENCE INTO DATA(lr_db_si).
            lr_db_si->hec_phase_guid = <fs_phase_parameter>-hec_phase_guid_new.
            lr_db_si->hec_phase_assign_allowed = COND #( WHEN <fs_phase_parameter>-hec_phase_guid_new IS NOT INITIAL
                                                           OR lr_db_si->hec_default_db_server_inst = abap_true
                                                         THEN abap_false
                                                         ELSE abap_true ).
*            lr_db_si->hec_phase_changed = abap_true.

            INSERT VALUE #( data        = lr_db_si
                            node        = /hec1/if_configuration_c=>sc_node-db_server_instance
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_db_si->key    ) INTO TABLE lt_modification.

          ENDLOOP. "lt_db_si
          CLEAR lr_db_si.

          "-----------------------------------
          " Material
          "-----------------------------------
        WHEN /hec1/if_configuration_c=>sc_node-material.

          LOOP AT lt_software_item REFERENCE INTO DATA(lr_software_item).

            " set phase
            lr_software_item->hec_phase_guid = <fs_phase_parameter>-hec_phase_guid_new.
            "description is retrieved in the object's determination
            lr_software_item->hec_phase_assign_allowed = COND #( WHEN <fs_phase_parameter>-hec_phase_guid_new IS NOT INITIAL
                                                                   OR lr_software_item->hec_sw_item_mat_rel_value = /hec1/if_config_constants=>gc_material_rel-mandatory "01
                                                                 THEN abap_false
                                                                 ELSE abap_true ).

            INSERT VALUE #( data        = lr_software_item
                            node        = /hec1/if_configuration_c=>sc_node-software_item
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_software_item->key    ) INTO TABLE lt_modification.

          ENDLOOP. "lt_software_item
          CLEAR lr_software_item.

          "-----------------------------------
          " DB Server Instance
          "-----------------------------------
        WHEN /hec1/if_configuration_c=>sc_node-db_server_instance.

          LOOP AT lt_db_si ASSIGNING FIELD-SYMBOL(<fs_db_si>).
            " !!!!!! Later we will have to differentiate between allocation types.
            " !!!!!! If a container is used the container's phase is dependant on the Tenants' phases.

*            WHERE hec_db_allocation_value = /hec1/if_config_constants=>gc_db_allocation-internal
*               OR hec_db_allocation_value = /hec1/if_config_constants=>gc_db_allocation-separate_db
*               OR hec_db_allocation_value = /hec1/if_config_constants=>gc_db_allocation-other_tier.

            LOOP AT lt_instance_db REFERENCE INTO DATA(lr_instance_db).

              lr_instance_db->hec_phase_guid = <fs_phase_parameter>-hec_phase_guid_new.
              lr_instance_db->hec_phase_assign_allowed = abap_false. "this never changes

              INSERT VALUE #( data        = lr_instance_db
                              node        = /hec1/if_configuration_c=>sc_node-instance_db
                              change_mode = /bobf/if_frw_c=>sc_modify_update
                              key         = lr_instance_db->key    ) INTO TABLE lt_modification.

            ENDLOOP. "lt_instance_db
            CLEAR lr_instance_db.

          ENDLOOP. "lt_db_si

          "-----------------------------------
          " Instance DB
          "-----------------------------------
        WHEN /hec1/if_configuration_c=>sc_node-instance_db.

          LOOP AT lt_db_node REFERENCE INTO DATA(lr_db_node)
            WHERE hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master.

            lr_db_node->hec_phase_guid = <fs_phase_parameter>-hec_phase_guid_new.
            lr_db_node->hec_phase_assign_allowed = COND #( WHEN <fs_phase_parameter>-hec_phase_guid_new IS INITIAL
                                                             OR lr_db_node->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master
                                                           THEN abap_false
                                                           ELSE abap_true ).

            INSERT VALUE #( data        = lr_db_node
                            node        = /hec1/if_configuration_c=>sc_node-db_node
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_db_node->key    ) INTO TABLE lt_modification.

          ENDLOOP. "lt_db_node
          CLEAR lr_db_node.

          "-----------------------------------
          " DB Node
          "-----------------------------------
        WHEN /hec1/if_configuration_c=>sc_node-db_node.

          LOOP AT lt_db_serv_pc REFERENCE INTO DATA(lr_db_serv_pc).

            ASSIGN lt_db_node[ key = lr_db_serv_pc->parent_key ] TO FIELD-SYMBOL(<fs_db_node>).
            IF <fs_db_node> IS ASSIGNED.

              IF <fs_db_node>-hec_db_srv_perf_cat_qty = 1.
                lr_db_serv_pc->hec_phase_guid = <fs_phase_parameter>-hec_phase_guid_new.
              ENDIF.

              lr_db_serv_pc->hec_phase_assign_allowed = COND #( WHEN <fs_phase_parameter>-hec_phase_guid_new IS INITIAL
                                                                  OR lr_db_serv_pc->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master
                                                                  OR lr_db_serv_pc->hec_predecessor_guid IS NOT INITIAL "this means that this node is the first node in the chain
                                                                THEN abap_false
                                                                ELSE abap_true ).

              INSERT VALUE #( data        = lr_db_serv_pc
                              node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                              change_mode = /bobf/if_frw_c=>sc_modify_update
                              key         = lr_db_serv_pc->key    ) INTO TABLE lt_modification.

            ENDIF. "<fs_db_node> is assigned.

          ENDLOOP. "lt_db_serv_pc
          CLEAR lr_db_serv_pc.

          "-----------------------------------
          " DB Server Performance Category
          " (Successor / Predecessor)
          "-----------------------------------
        WHEN /hec1/if_configuration_c=>sc_node-db_server_perform_cat.

          "change db server performance category (if there are successor/predecessor nodes)
          LOOP AT lt_db_serv_pc ASSIGNING FIELD-SYMBOL(<fs_db_serv_pc>).
            IF <fs_db_serv_pc>-hec_has_successor = abap_true.

              TRY.
                  DATA(lr_db_serv_pc_successor) = NEW /hec1/s_data_db_serv_pc_cs( lt_db_serv_pc_all[ key = <fs_db_serv_pc>-hec_successor_guid ] ).

                  " Get successor
                  IF lr_phase_new IS NOT INITIAL.

                    DATA(ls_phase_successor) = lt_phase[ key = lr_phase_new->hec_phase_successor_guid ].

                    lr_db_serv_pc_successor->hec_phase_guid = ls_phase_successor-hec_node_phase.
                    lr_db_serv_pc_successor->hec_phase_assign_allowed = abap_false. "only the first object in the chain may have a manual phase assignment. At this point we are definately at the 2nd or later object

                    INSERT VALUE #( data        = lr_db_serv_pc_successor
                                    node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                    change_mode = /bobf/if_frw_c=>sc_modify_update
                                    key         = lr_db_serv_pc_successor->key    ) INTO TABLE lt_modification.

                    CLEAR lr_db_serv_pc_successor.

                  ELSE.
                    CLEAR: lr_db_serv_pc_successor->hec_phase_guid.

                    lr_db_serv_pc_successor->hec_phase_assign_allowed = abap_false.

                  ENDIF. " IF lr_phase_new IS NOT INITIAL.

                CATCH cx_sy_itab_line_not_found.
                CATCH cx_uuid_error.
              ENDTRY.

            ENDIF. "has successor

            lt_db_storage_qty = VALUE #( FOR db_storage_qty IN lt_db_storage_qty_all
                                WHERE ( parent_key = <fs_db_serv_pc>-key )
                                      ( db_storage_qty ) ).

            IF lines( lt_db_storage_qty ) = 1.
              " the storage amount gets the same phase as the server performance category, only if there is just one entry. otherwise, successor predecessor need to be assigned
              TRY.
                  DATA(lr_db_storage_qty) = NEW /hec1/s_data_db_storage_qty_cs( lt_db_storage_qty[ 1 ] ).
                  lr_db_storage_qty->hec_phase_guid = <fs_db_serv_pc>-hec_phase_guid.
                  lr_db_storage_qty->hec_phase_assign_allowed = abap_false.

                  INSERT VALUE #( data        = lr_db_storage_qty
                                  node        = /hec1/if_configuration_c=>sc_node-db_storage_amount
                                  change_mode = /bobf/if_frw_c=>sc_modify_update
                                  key         = lr_db_storage_qty->key    ) INTO TABLE lt_modification.

                  CLEAR lr_db_storage_qty.

                CATCH cx_sy_itab_line_not_found.
              ENDTRY.

            ELSE.
              " clear phasing for all storage quantities
              LOOP AT lt_db_storage_qty ASSIGNING FIELD-SYMBOL(<fs_db_storage_qty>). "REFERENCE INTO lr_db_storage_qty.

                lr_db_storage_qty = NEW #( <fs_db_storage_qty> ).

                CLEAR: lr_db_storage_qty->hec_phase_guid.

                lr_db_storage_qty->hec_phase_assign_allowed = COND #( WHEN lr_db_storage_qty->hec_predecessor_guid IS NOT INITIAL
                                                                        OR <fs_phase_parameter>-hec_phase_guid_new IS INITIAL
                                                                        OR lr_db_storage_qty->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master
                                                                      THEN abap_false
                                                                      ELSE abap_true ).

                INSERT VALUE #( data        = lr_db_storage_qty
                                node        = /hec1/if_configuration_c=>sc_node-db_storage_amount
                                change_mode = /bobf/if_frw_c=>sc_modify_update
                                key         = lr_db_storage_qty->key    ) INTO TABLE lt_modification.

                CLEAR lr_db_storage_qty.

              ENDLOOP. "lt_db_storage_qty

            ENDIF. "lines( lt_db_storage_qty ) = 1.

            " Set Phasing for Server
            " there is only always 1 server
            TRY.
                DATA(lr_db_server) = NEW /hec1/s_data_db_serv_cs( lt_db_server_all[ parent_key = <fs_db_serv_pc>-key ] ).

                lr_db_server->hec_phase_guid = <fs_db_serv_pc>-hec_phase_guid.
                lr_db_server->hec_phase_assign_allowed = abap_false.

                INSERT VALUE #( data        = lr_db_server
                                node        = /hec1/if_configuration_c=>sc_node-db_server
                                change_mode = /bobf/if_frw_c=>sc_modify_update
                                key         = lr_db_server->key    ) INTO TABLE lt_modification.

                CLEAR: lr_db_server.

              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

          ENDLOOP. "lt_db_serv_pc

          "-----------------------------------
          " DB Storage Amount
          " (Successor / Predecessor)
          "-----------------------------------
        WHEN /hec1/if_configuration_c=>sc_node-db_storage_amount.

          "change db storage qty (successor/predecessor)
          LOOP AT lt_db_storage_qty ASSIGNING <fs_db_storage_qty>.
            IF <fs_db_storage_qty>-hec_has_successor = abap_true.

              TRY.
                  DATA(lr_db_storage_qty_successor) = NEW /hec1/s_data_db_storage_qty_cs( lt_db_storage_qty_all[ key = <fs_db_storage_qty>-hec_successor_guid ] ).

                  " Get successor
                  IF lr_phase_new IS NOT INITIAL.

                    ls_phase_successor = lt_phase[ key = lr_phase_new->hec_phase_successor_guid ].

                    lr_db_storage_qty_successor->hec_phase_guid = ls_phase_successor-hec_node_phase.
                    lr_db_storage_qty_successor->hec_phase_assign_allowed = abap_false. "the successor is never allowed to have a phasing assignment

                    INSERT VALUE #( data        = lr_db_storage_qty_successor
                                    node        = /hec1/if_configuration_c=>sc_node-db_storage_amount "db_server_perform_cat
                                    change_mode = /bobf/if_frw_c=>sc_modify_update
                                    key         = lr_db_storage_qty_successor->key    ) INTO TABLE lt_modification.

                    CLEAR lr_db_storage_qty_successor.

                  ELSE.
                    CLEAR: lr_db_storage_qty_successor->hec_phase_guid.

                    lr_db_storage_qty_successor->hec_phase_assign_allowed = abap_false.

                  ENDIF. "if lr_phase_new is not initial

                CATCH cx_sy_itab_line_not_found.
                CATCH cx_uuid_error.
              ENDTRY.

            ENDIF. "has successor

*            " the storage gets the same phase as the storage quantity
            TRY.
                DATA(lr_db_storage) = NEW /hec1/s_data_db_storage_cs( lt_db_storage[ hec_storage_qty_ref_guid = <fs_db_storage_qty>-hec_node_db_storage_qty ] ).
                lr_db_storage->hec_phase_guid = <fs_db_storage_qty>-hec_phase_guid.
                lr_db_storage->hec_phase_assign_allowed = abap_false. "the storage cannot have a different phase assigned as the storage quantity

                INSERT VALUE #( data        = lr_db_storage
                                node        = /hec1/if_configuration_c=>sc_node-db_storage
                                change_mode = /bobf/if_frw_c=>sc_modify_update
                                key         = lr_db_storage->key    ) INTO TABLE lt_modification.

                CLEAR lr_db_storage.

              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

          ENDLOOP. "lt_db_serv_pc

          "-----------------------------------
          " DB Storage
          " (Successor / Predecessor)
          "-----------------------------------
        WHEN /hec1/if_configuration_c=>sc_node-db_storage.

          LOOP AT lt_db_backup ASSIGNING FIELD-SYMBOL(<fs_db_backup>)
            GROUP BY <fs_db_backup>-parent_key .

            DATA(lt_db_backup_filter) = VALUE /hec1/t_data_db_backup_ct( FOR backup IN lt_db_backup
                                                                         WHERE ( parent_key = <fs_db_backup>-parent_key )
                                                                         ( backup ) ).

            IF lines( lt_db_backup_filter ) = 1.
              TRY.
                  DATA(lr_db_backup) = NEW /hec1/s_data_db_backup_cs( lt_db_backup_filter[ 1 ] ).

                  lr_db_backup->hec_phase_guid = <fs_phase_parameter>-hec_phase_guid_new.
                  lr_db_backup->hec_phase_assign_allowed = abap_false. "the successors cannot have a manual phase assignment

                  INSERT VALUE #( data        = lr_db_backup
                                  node        = /hec1/if_configuration_c=>sc_node-db_storage_backup
                                  change_mode = /bobf/if_frw_c=>sc_modify_update
                                  key         = lr_db_backup->key    ) INTO TABLE lt_modification.


                CATCH cx_sy_itab_line_not_found.
              ENDTRY.

            ENDIF. "lines( lt_db_backup ) = 1.

          ENDLOOP. "lt_db_backup
          CLEAR lr_db_backup.

          "if there are multiple lines, successor/predecessor needs to be used and set by the user

          "-----------------------------------
          " DB Backup
          " (Successor / Predecessor)
          "-----------------------------------
        WHEN /hec1/if_configuration_c=>sc_node-db_storage_backup.

          "change db backup (successor/predecessor)
          LOOP AT lt_db_backup ASSIGNING <fs_db_backup>.
            IF <fs_db_backup>-hec_has_successor = abap_true.

              TRY.
                  DATA(lr_db_backup_successor) = NEW /hec1/s_data_db_backup_cs( lt_db_backup_all[ key = <fs_db_backup>-hec_successor_guid ] ).

                  " Get successor
                  IF lr_phase_new IS NOT INITIAL.

                    ls_phase_successor = lt_phase[ key = lr_phase_new->hec_phase_successor_guid ].

                    lr_db_backup_successor->hec_phase_guid = ls_phase_successor-hec_node_phase.
                    lr_db_backup_successor->hec_phase_assign_allowed = abap_false. "the successor cannot have a manual phase assignment

                    INSERT VALUE #( data        = lr_db_backup_successor
                                    node        = /hec1/if_configuration_c=>sc_node-db_storage_backup
                                    change_mode = /bobf/if_frw_c=>sc_modify_update
                                    key         = lr_db_backup_successor->key    ) INTO TABLE lt_modification.

                    CLEAR lr_db_backup_successor.

                  ELSE.
                    CLEAR: lr_db_backup_successor->hec_phase_guid.

                    lr_db_backup_successor->hec_phase_assign_allowed = abap_false.

                  ENDIF. " if lr_phase_new is not initial.

                CATCH cx_sy_itab_line_not_found.
                CATCH cx_uuid_error.
              ENDTRY.

            ENDIF. "has successor
          ENDLOOP. "lt_app_backup

          "-----------------------------------
          " App Server Instance
          "-----------------------------------
        WHEN /hec1/if_configuration_c=>sc_node-app_server_instance.

          LOOP AT lt_app_node REFERENCE INTO DATA(lr_app_node)
            WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master.

            lr_app_node->hec_phase_guid = <fs_phase_parameter>-hec_phase_guid_new.
            lr_app_node->hec_phase_assign_allowed = abap_false.

            INSERT VALUE #( data        = lr_app_node
                            node        = /hec1/if_configuration_c=>sc_node-app_node
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_app_node->key    ) INTO TABLE lt_modification.

          ENDLOOP. "lt_app_node
          CLEAR lr_app_node.

          "-----------------------------------
          " App Node
          "-----------------------------------
        WHEN /hec1/if_configuration_c=>sc_node-app_node.

          LOOP AT lt_app_serv_pc REFERENCE INTO DATA(lr_app_serv_pc).

            ASSIGN lt_app_node[ key = lr_app_serv_pc->parent_key ] TO FIELD-SYMBOL(<fs_app_node>).
            IF <fs_app_node> IS ASSIGNED.

              IF <fs_app_node>-hec_app_srv_perf_cat_qty = 1.
                lr_app_serv_pc->hec_phase_guid = <fs_phase_parameter>-hec_phase_guid_new.
              ENDIF.

              lr_app_serv_pc->hec_phase_assign_allowed = COND #( WHEN <fs_phase_parameter>-hec_phase_guid_new IS INITIAL
                                                                   OR lr_app_serv_pc->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master
                                                                   OR lr_app_serv_pc->hec_predecessor_guid IS NOT INITIAL "this means that this node is the first node in the chain
                                                                 THEN abap_false
                                                                 ELSE abap_true ).

              INSERT VALUE #( data        = lr_app_serv_pc
                              node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                              change_mode = /bobf/if_frw_c=>sc_modify_update
                              key         = lr_app_serv_pc->key    ) INTO TABLE lt_modification.

            ENDIF. "<fs_app_node> is assigned.

          ENDLOOP. "lt_app_serv_pc
          CLEAR lr_app_serv_pc.

          "-----------------------------------
          " App Server Performance Category
          " (Successor / Predecessor)
          "-----------------------------------
        WHEN /hec1/if_configuration_c=>sc_node-app_server_perform_cat.

          "change db server performance category (if there are successor/predecessor nodes)
          LOOP AT lt_app_serv_pc ASSIGNING FIELD-SYMBOL(<fs_app_serv_pc>).
            IF <fs_app_serv_pc>-hec_has_successor = abap_true.

              TRY.
                  DATA(lr_app_serv_pc_successor) = NEW /hec1/s_data_app_serv_pc_cs( lt_app_serv_pc_all[ key = <fs_app_serv_pc>-hec_successor_guid ] ).

                  " Get successor
                  IF lr_phase_new IS NOT INITIAL.

                    ls_phase_successor = lt_phase[ key = lr_phase_new->hec_phase_successor_guid ].

                    lr_app_serv_pc_successor->hec_phase_guid = ls_phase_successor-hec_node_phase.
                    lr_app_serv_pc_successor->hec_phase_assign_allowed = abap_false. "the successor does not allow manual phase assignment

                    INSERT VALUE #( data        = lr_app_serv_pc_successor
                                    node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                    change_mode = /bobf/if_frw_c=>sc_modify_update
                                    key         = lr_app_serv_pc_successor->key    ) INTO TABLE lt_modification.

                    CLEAR lr_app_serv_pc_successor.

                  ELSE.
                    CLEAR: lr_app_serv_pc_successor->hec_phase_guid.

                    lr_app_serv_pc_successor->hec_phase_assign_allowed = abap_false.

                  ENDIF. "if lr_phase_new is not initial

                CATCH cx_sy_itab_line_not_found.
                CATCH cx_uuid_error.
              ENDTRY.

            ENDIF. "has successor

            lt_app_storage_qty = VALUE #( FOR app_storage_qty IN lt_app_storage_qty_all
                                WHERE ( parent_key = <fs_app_serv_pc>-key )
                                      ( app_storage_qty ) ).

            IF lines( lt_app_storage_qty ) = 1.
              " the storage amount gets the same phase as the server performance category, only if there is just one entry. otherwise, successor predecessor need to be assigned
              TRY.
                  DATA(lr_app_storage_qty) = NEW /hec1/s_data_app_storageqty_cs( lt_app_storage_qty[ 1 ] ).
                  lr_app_storage_qty->hec_phase_guid = <fs_app_serv_pc>-hec_phase_guid.
                  lr_app_storage_qty->hec_phase_assign_allowed = abap_false.

                  INSERT VALUE #( data        = lr_app_storage_qty
                                  node        = /hec1/if_configuration_c=>sc_node-app_storage_amount
                                  change_mode = /bobf/if_frw_c=>sc_modify_update
                                  key         = lr_app_storage_qty->key    ) INTO TABLE lt_modification.

                  CLEAR lr_app_storage_qty.

                CATCH cx_sy_itab_line_not_found.
              ENDTRY.

            ELSE.
              " clear phasing for all storage quantities
              LOOP AT lt_app_storage_qty ASSIGNING FIELD-SYMBOL(<fs_app_storage_qty>).

                lr_app_storage_qty = NEW #( <fs_app_storage_qty> ).

                CLEAR: lr_app_storage_qty->hec_phase_guid.

                lr_app_storage_qty->hec_phase_assign_allowed = COND #( WHEN lr_app_storage_qty->hec_predecessor_guid IS NOT INITIAL
                                                                         OR <fs_phase_parameter>-hec_phase_guid_new IS INITIAL
                                                                         OR lr_app_storage_qty->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master
                                                                       THEN abap_false
                                                                       ELSE abap_true ).

                INSERT VALUE #( data        = lr_app_storage_qty
                                node        = /hec1/if_configuration_c=>sc_node-app_storage_amount
                                change_mode = /bobf/if_frw_c=>sc_modify_update
                                key         = lr_app_storage_qty->key    ) INTO TABLE lt_modification.

                CLEAR lr_app_storage_qty.

              ENDLOOP. "lt_app_storage_qty

            ENDIF. "lines( lt_app_storage_qty ) = 1.

            " Set Phasing for Server
            " there is only always 1 server
            TRY.
                DATA(lr_app_server) = NEW /hec1/s_data_app_serv_cs( lt_app_server_all[ parent_key = <fs_app_serv_pc>-key ] ).

                lr_app_server->hec_phase_guid = <fs_app_serv_pc>-hec_phase_guid.
                lr_app_server->hec_phase_assign_allowed = abap_false.

                INSERT VALUE #( data        = lr_app_server
                                node        = /hec1/if_configuration_c=>sc_node-app_server
                                change_mode = /bobf/if_frw_c=>sc_modify_update
                                key         = lr_app_server->key    ) INTO TABLE lt_modification.

                CLEAR lr_app_server.

              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

          ENDLOOP. "lt_app_serv_pc

          "-----------------------------------
          " App Storage Amount
          " (Successor / Predecessor)
          "-----------------------------------
        WHEN /hec1/if_configuration_c=>sc_node-app_storage_amount.

          "change app storage qty (successor/predecessor)
          LOOP AT lt_app_storage_qty ASSIGNING <fs_app_storage_qty>.
            IF <fs_app_storage_qty>-hec_has_successor = abap_true.

              TRY.
                  DATA(lr_app_storage_qty_successor) = NEW /hec1/s_data_app_storageqty_cs( lt_app_storage_qty_all[ key = <fs_app_storage_qty>-hec_successor_guid ] ).

                  " Get successor
                  IF lr_phase_new IS NOT INITIAL.

                    ls_phase_successor = lt_phase[ key = lr_phase_new->hec_phase_successor_guid ].

                    lr_app_storage_qty_successor->hec_phase_guid = ls_phase_successor-hec_node_phase.
                    lr_app_storage_qty_successor->hec_phase_assign_allowed = abap_false. "the successor does not allow manual phase assignment

                    INSERT VALUE #( data        = lr_app_storage_qty_successor
                                    node        = /hec1/if_configuration_c=>sc_node-app_storage_amount "server_perform_cat
                                    change_mode = /bobf/if_frw_c=>sc_modify_update
                                    key         = lr_app_storage_qty_successor->key    ) INTO TABLE lt_modification.

                    CLEAR lr_app_storage_qty_successor.

                  ELSE.
                    CLEAR: lr_app_storage_qty_successor->hec_phase_guid.

                    lr_app_storage_qty_successor->hec_phase_assign_allowed = abap_false.

                  ENDIF. "lr_phase is not initial

                CATCH cx_sy_itab_line_not_found.
                CATCH cx_uuid_error.
              ENDTRY.

            ENDIF. "has successor

*            " the storage gets the same phase as the storage quantity
            TRY.
                DATA(lr_app_storage) = NEW /hec1/s_data_app_storage_cs( lt_app_storage[ hec_storage_qty_ref_guid = <fs_app_storage_qty>-hec_node_app_storage_qty ] ).
                lr_app_storage->hec_phase_guid = <fs_app_storage_qty>-hec_phase_guid.
                lr_app_storage->hec_phase_assign_allowed = abap_false. "the storage cannot have a different phase assigned as the storage quantity

                INSERT VALUE #( data        = lr_app_storage
                                node        = /hec1/if_configuration_c=>sc_node-app_storage
                                change_mode = /bobf/if_frw_c=>sc_modify_update
                                key         = lr_app_storage->key    ) INTO TABLE lt_modification.

                CLEAR lr_app_storage.

              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

          ENDLOOP. "lt_app_serv_pc

          "-----------------------------------
          " App Storage
          " (Successor / Predecessor)
          "-----------------------------------
        WHEN /hec1/if_configuration_c=>sc_node-app_storage.

          LOOP AT lt_app_backup ASSIGNING FIELD-SYMBOL(<fs_app_backup>)
            GROUP BY <fs_app_backup>-parent_key .

            DATA(lt_app_backup_filter) = VALUE /hec1/t_data_app_backup_ct( FOR app_backup IN lt_app_backup
                                                                           WHERE ( parent_key = <fs_app_backup>-parent_key )
                                                                           ( app_backup ) ).

            IF lines( lt_app_backup_filter ) = 1.
              TRY.
                  DATA(lr_app_backup) = NEW /hec1/s_data_app_backup_cs( lt_app_backup_filter[ 1 ] ).

                  lr_app_backup->hec_phase_guid = <fs_phase_parameter>-hec_phase_guid_new.
                  lr_app_backup->hec_phase_assign_allowed = abap_false. "the successors cannot have a manual phase assignment

                  INSERT VALUE #( data        = lr_app_backup
                                  node        = /hec1/if_configuration_c=>sc_node-app_storage_backup
                                  change_mode = /bobf/if_frw_c=>sc_modify_update
                                  key         = lr_app_backup->key    ) INTO TABLE lt_modification.

                  CLEAR lr_app_backup.

                CATCH cx_sy_itab_line_not_found.
              ENDTRY.

            ENDIF. "lines( lt_app_backup ) = 1.

          ENDLOOP. "lt_app_backup
          CLEAR lr_app_backup.

          "if there are multiple lines, successor/predecessor needs to be used and set by the user

          "-----------------------------------
          " App Backup
          " (Successor / Predecessor)
          "-----------------------------------
        WHEN /hec1/if_configuration_c=>sc_node-app_storage_backup.

          "change app backup (successor/predecessor)
          LOOP AT lt_app_backup ASSIGNING <fs_app_backup>.
            IF <fs_app_backup>-hec_has_successor = abap_true.

              TRY.
                  DATA(lr_app_backup_successor) = NEW /hec1/s_data_app_backup_cs( lt_app_backup_all[ key = <fs_app_backup>-hec_successor_guid ] ).

                  " Get successor
                  IF lr_phase_new IS NOT INITIAL.

                    ls_phase_successor = lt_phase[ key = lr_phase_new->hec_phase_successor_guid ].

                    lr_app_backup_successor->hec_phase_guid = ls_phase_successor-hec_node_phase.
                    lr_app_backup_successor->hec_phase_assign_allowed = abap_false. "the successor does not allow manual phase assignment

                    INSERT VALUE #( data        = lr_app_backup_successor
                                    node        = /hec1/if_configuration_c=>sc_node-app_storage_backup
                                    change_mode = /bobf/if_frw_c=>sc_modify_update
                                    key         = lr_app_backup_successor->key    ) INTO TABLE lt_modification.

                    CLEAR lr_app_backup_successor.

                  ELSE.
                    CLEAR: lr_app_backup_successor->hec_phase_guid.

                    lr_app_backup_successor->hec_phase_assign_allowed = abap_false.

                  ENDIF. " if lr_phase_new is not initial.

                CATCH cx_sy_itab_line_not_found.
                CATCH cx_uuid_error.
              ENDTRY.

            ENDIF. "has successor
          ENDLOOP. "lt_app_backup

      ENDCASE. "is_ctx-node_key

      CLEAR: lr_phase_new,
             lr_phase_old.

    ENDLOOP.

    "-----------------------------------
    " Change Instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~set_successor_predecessor.

    DATA: lr_data_table   TYPE REF TO data,
          lr_data         TYPE REF TO data,
          lv_predecessor  TYPE /bobf/conf_key,
          lt_succ_predec  TYPE /hec1/t_config_succes_predec,
          lt_modification TYPE /bobf/t_frw_modification.

    FIELD-SYMBOLS: <fs_data_table> TYPE INDEX TABLE,
                   <fs_act_param>  TYPE /hec1/t_act_set_success_predec.


    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_act_param>.
    IF <fs_act_param> IS ASSIGNED.
      TRY.
          DATA(lo_config) = /bobf/cl_frw_factory=>get_configuration( is_ctx-bo_key ).

          " Get node with depending structure type
          lo_config->get_assoc( EXPORTING iv_assoc_key  = is_ctx-assoc_key                 " Association Key
                                          iv_node_key   = is_ctx-node_key                  " Node Key
                                IMPORTING es_assoc      = DATA(ls_assoc)   ).              " Configuration: Link

          lo_config->get_node( EXPORTING iv_node_key = ls_assoc-target_node_key
                               IMPORTING es_node     = DATA(ls_node_conf)       ).

          " Create retrieve structure
          CREATE DATA lr_data_table TYPE (ls_node_conf-data_table_type).
          ASSIGN lr_data_table->* TO <fs_data_table>.

          IF <fs_data_table> IS ASSIGNED.
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = is_ctx-assoc_key
                                              IMPORTING et_data        = <fs_data_table>
                                                        et_target_key  = DATA(lt_key)
                                                        et_key_link    = DATA(lt_key_link)
                                                        et_failed_key  = et_failed_key      ).


            LOOP AT <fs_data_table> ASSIGNING FIELD-SYMBOL(<fs_data>).
              TRY.
                  ASSIGN COMPONENT 'KEY'
                     OF STRUCTURE <fs_data>
                  TO FIELD-SYMBOL(<fs_key>).

                  ASSIGN COMPONENT 'PARENT_KEY'
                     OF STRUCTURE <fs_data>
                  TO FIELD-SYMBOL(<fs_parent_key>).

                  ASSIGN COMPONENT 'CREA_DATE_TIME'
                     OF STRUCTURE <fs_data>
                  TO FIELD-SYMBOL(<fs_crea_date_time>).

                  IF <fs_key>            IS ASSIGNED AND
                     <fs_parent_key>     IS ASSIGNED AND
                     <fs_crea_date_time> IS ASSIGNED.
                    INSERT VALUE #( key            = <fs_key>
                                    parent_key     = <fs_parent_key>
                                    crea_date_time = <fs_crea_date_time> ) INTO TABLE lt_succ_predec.
                  ENDIF.

                  UNASSIGN: <fs_key>,
                            <fs_parent_key>,
                            <fs_crea_date_time>.
                CATCH cx_root.
              ENDTRY.
            ENDLOOP.

            SORT lt_succ_predec ASCENDING BY crea_date_time.

            LOOP AT lt_succ_predec
                 INTO DATA(ls_succ_predec)
                 GROUP BY ls_succ_predec-parent_key

                 ASCENDING
                 ASSIGNING FIELD-SYMBOL(<group>).

              DATA(lt_filter) = VALUE /hec1/t_config_succes_predec( FOR wa IN lt_succ_predec
                                                                    WHERE ( parent_key = <group> )
                                                                     ( wa )                         ).

              LOOP AT GROUP <group>
                   ASSIGNING FIELD-SYMBOL(<fs_group>).

                DATA(lv_tabix) = sy-tabix.

                " Get successor
                TRY.
                    DATA(ls_succ) = lt_filter[ lv_tabix + 1 ].
                    <fs_group>-hec_successor_guid = ls_succ-key.
                    <fs_group>-hec_has_successor = abap_true.
                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.

                " Get predecessor
                TRY.
                    DATA(ls_predec) = lt_filter[ lv_tabix - 1 ].
                    <fs_group>-hec_predecessor_guid = ls_predec-key.
                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.

                CLEAR: ls_succ,
                       ls_predec.
              ENDLOOP.         " LOOP AT GROUP <group>

              CLEAR: lv_tabix,
                     lt_filter.
            ENDLOOP. " LOOP AT lt_succ_predec...


            LOOP AT <fs_data_table> ASSIGNING <fs_data>.

              TRY.
                  ASSIGN COMPONENT 'KEY'
                     OF STRUCTURE <fs_data>
                               TO <fs_key>.

                  ASSIGN COMPONENT 'PARENT_KEY'
                     OF STRUCTURE <fs_data>
                               TO <fs_parent_key>.

                  ASSIGN COMPONENT 'HEC_HAS_SUCCESSOR'
                     OF STRUCTURE <fs_data>
                  TO FIELD-SYMBOL(<fs_has_successor>).

                  ASSIGN COMPONENT 'HEC_SUCCESSOR_GUID'
                     OF STRUCTURE <fs_data>
                  TO FIELD-SYMBOL(<fs_successor_guid>).

                  ASSIGN COMPONENT 'HEC_PREDECESSOR_GUID'
                     OF STRUCTURE <fs_data>
                  TO FIELD-SYMBOL(<fs_predecessor_guid>).

                  IF <fs_key>              IS ASSIGNED AND
                     <fs_has_successor>    IS ASSIGNED AND
                     <fs_successor_guid>   IS ASSIGNED AND
                     <fs_predecessor_guid> IS ASSIGNED.
                    TRY.
                        ls_succ_predec = lt_succ_predec[ key = <fs_key> ].

                        <fs_has_successor>    = ls_succ_predec-hec_has_successor.
                        <fs_successor_guid>   = ls_succ_predec-hec_successor_guid.
                        <fs_predecessor_guid> = ls_succ_predec-hec_predecessor_guid.

                      CATCH cx_sy_itab_line_not_found.
                    ENDTRY.
                  ENDIF.

                  DATA(lo_strucdescr) = CAST cl_abap_structdescr( cl_abap_structdescr=>describe_by_name( ls_node_conf-data_type ) ).
                  CREATE DATA lr_data TYPE HANDLE lo_strucdescr.

                  lr_data = REF #( <fs_data> ).

                  INSERT VALUE #( data        = lr_data
                                  node        = ls_assoc-target_node_key
                                  source_node = is_ctx-node_key
                                  association = is_ctx-assoc_key
                                  source_key  = <fs_parent_key>
                                  change_mode = /bobf/if_frw_c=>sc_modify_update
                                  key         = <fs_key>                         ) INTO TABLE lt_modification.

                  CLEAR: lo_strucdescr,
                         lr_data.

                  UNASSIGN: <fs_key>,
                            <fs_parent_key>,
                            <fs_has_successor>,
                            <fs_successor_guid>,
                            <fs_predecessor_guid>.
                CATCH cx_root.
              ENDTRY.
            ENDLOOP.

          ENDIF.
        CATCH /bobf/cx_frw. " BOPF Exception Class
      ENDTRY.
    ENDIF. " IF <fs_act_param> IS ASSIGNED.

    "-----------------------------------
    " Update instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_additional_service.

    DATA: lt_dlvy_unit    TYPE /hec1/t_data_dlvy_unit_ct,
          lt_add_service  TYPE /hec1/t_data_add_services_ct,
          lt_datacenter   TYPE /hec1/t_data_datacenter_ct,
          lt_modification TYPE /bobf/t_frw_modification.

    CLEAR: eo_message,
           et_failed_key.

    "it_key contains the datacenter key.

    io_read->retrieve( EXPORTING iv_node     = is_ctx-node_key
                                 it_key      = it_key
                       IMPORTING et_data     = lt_datacenter ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_failed_key    = et_failed_key ).

    "-----------------------------------
    " Get additional services
    "-----------------------------------
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = VALUE #( ( key = lr_landscape->key ) )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-add_service
                                      IMPORTING et_data        = lt_add_service                                             ).

    LOOP AT lt_datacenter ASSIGNING FIELD-SYMBOL(<fs_datacenter>).

      LOOP AT lt_add_service REFERENCE INTO DATA(lr_add_service).

        SELECT SINGLE *
          FROM /hec1/i_addserviceclasslbbasic
         WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid          AND
               hec_inf_provider_guid   = @lr_dlvy_unit->hec_inf_provider_guid AND
               hec_sec_datacenter_guid = @<fs_datacenter>-hec_datacenter_guid AND
               hec_as_class_guid       = @lr_add_service->hec_as_class_guid
          INTO @DATA(ls_service_data).


        " Get pricing
        SELECT SINGLE * FROM /hec1/c_cbp_lb   "#EC CI_ALL_FIELDS_NEEDED
           INTO @DATA(ls_pricing)
          WHERE hec_price_lb = @ls_service_data-hec_cb_pricing_lb_guid.

        "-----------------------------------
        " update additional service
        "-----------------------------------
        lr_add_service->* = VALUE #( BASE CORRESPONDING #( lr_add_service->* )
                                     hec_as_datacenter_guid  = <fs_datacenter>-hec_node_datacenter
                                     hec_as_datacenter_descr = <fs_datacenter>-hec_datacenter_descr
                                     hec_as_quota            = ls_service_data-hec_as_quota
                                     hec_as_tier_uplift_perc = ls_service_data-hec_as_upflift_percent
                                     hec_price_lb            = ls_service_data-hec_cb_pricing_lb_guid
                                     hec_tree_descr          = |{ lr_add_service->hec_as_class_descr } - { <fs_datacenter>-hec_datacenter_descr } : {
                                                                  lr_add_service->hec_as_class_descr_ext }|
                                     price                   = CORRESPONDING #( ls_pricing )                                                          ).

        INSERT VALUE #( data        = lr_add_service
                        node        = /hec1/if_configuration_c=>sc_node-add_service
                        change_mode = /bobf/if_frw_c=>sc_modify_update
                        key         = lr_add_service->key                           ) INTO TABLE lt_modification.

        CLEAR: ls_service_data,
               ls_pricing.

      ENDLOOP. "lt_additional_service
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


  METHOD /hec1/if_config_action_intern~update_app_node.

    DATA: lt_app_node           TYPE /hec1/t_data_app_node_ct,
          lt_ha_node            TYPE /hec1/t_data_app_node_ct,
          lt_app_serv_pc        TYPE /hec1/t_data_app_serv_pc_ct,
          lt_node_key           TYPE /bobf/t_frw_key,
          lt_ha_key             TYPE /bobf/t_frw_key,
          lt_act_param_succ     TYPE /hec1/t_act_set_success_predec,
          lt_act_param_del_node TYPE /bobf/t_frw_node,
          lt_modification       TYPE /bobf/t_frw_modification.

    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_update_app_node.


    CLEAR: eo_message,
           et_failed_key.


    ASSIGN ir_parameter->* TO <fs_act_param>.
    IF <fs_act_param> IS ASSIGNED.
      DATA(lt_act_parameter) = <fs_act_param>.

      LOOP AT lt_act_parameter ASSIGNING FIELD-SYMBOL(<fs_act_paramter>)
        WHERE do_release_ha_node   = abap_true OR
              do_delete_ha_subnode = abap_true.

        IF NOT line_exists( lt_ha_key[ key = <fs_act_paramter>-key ] ).
          /hec1/cl_bopf_config_validat_h=>check_standby_node_is_released( EXPORTING iv_is_app_server = abap_true
                                                                                    iv_check_rule    = /hec1/if_bopf_constants=>gc_check_rule-node
                                                                                    is_ctx           = CORRESPONDING #( is_ctx )
                                                                                    it_key           = VALUE #( ( key = <fs_act_paramter>-key ) )
                                                                                    io_read          = io_read
                                                                          IMPORTING et_node_key      = lt_node_key                                  ).

          APPEND LINES OF lt_node_key TO lt_ha_key.
          CLEAR lt_node_key.
        ENDIF.
      ENDLOOP.

      " Get standby node
      IF lt_ha_key IS NOT INITIAL.
        io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                     it_key  = lt_ha_key
                           IMPORTING et_data = lt_ha_node      ).

        " Get standby node: server performance category
        io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                    it_key         = lt_ha_key
                                                    iv_fill_data   = abap_false
                                                    iv_association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
                                          IMPORTING et_key_link    = DATA(lt_ha_spc_key_link)                                                 ).
      ENDIF.
    ENDIF. " IF <fs_act_param> IS ASSIGNED.


    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_node     ).

    " App Storage Qty
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
                                      IMPORTING et_data        = lt_app_serv_pc  ).


    LOOP AT lt_app_node REFERENCE INTO DATA(lr_app_node).
      "-----------------------------------
      " Release standby node for selection
      " or delete subnodes of standby node
      "-----------------------------------
      IF line_exists( lt_act_parameter[ key                  = lr_app_node->key
                                        do_release_ha_node   = abap_true        ] ) OR
         line_exists( lt_act_parameter[ key                  = lr_app_node->key
                                        do_delete_ha_subnode = abap_true        ] ).

        " Check master node is complete configered
        " ( including sub nodes: server performance category and storage amount )
        DATA(lv_complete) = /hec1/cl_bopf_config_validat_h=>check_master_node_is_complete( iv_is_app_server = abap_true
                                                                                           iv_check_rule    = /hec1/if_bopf_constants=>gc_check_rule-node
                                                                                           is_ctx           = CORRESPONDING #( is_ctx )
                                                                                           it_key           = VALUE #( ( key = lr_app_node->key ) )
                                                                                           io_read          = io_read                                      ).

        LOOP AT lt_ha_node
        REFERENCE INTO DATA(lr_ha_node)
        WHERE parent_key = lr_app_node->parent_key.

          IF lr_ha_node->hec_row_selectable <> lv_complete.
            lr_ha_node->hec_row_selectable = lv_complete.
            DATA(lv_data_changed) = abap_true.
          ENDIF.


          IF line_exists( lt_act_parameter[ key                  = lr_app_node->key
                                            do_delete_ha_subnode = abap_true        ] ).

            CLEAR: lr_ha_node->hec_phase_guid,
                   lr_ha_node->hec_app_srv_perf_cat_qty.

            lv_data_changed = abap_true.
          ENDIF.

          IF lv_data_changed = abap_true.
            INSERT VALUE #( data        = lr_ha_node
                            node        = is_ctx-node_key
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_ha_node->key                  ) INTO TABLE lt_modification.
          ENDIF.
          CLEAR lv_data_changed.
        ENDLOOP.

        "-----------------------------------
        "  Fill action table for delete
        " standby node subnodes
        "-----------------------------------
        IF line_exists( lt_act_parameter[ key                  = lr_app_node->key
                                          do_delete_ha_subnode = abap_true        ] ) AND
           lt_ha_spc_key_link IS NOT INITIAL.

          lt_act_param_del_node = VALUE #( FOR wa IN lt_ha_spc_key_link
                                          ( node = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                            key  = wa-target_key                                            ) ).
        ENDIF. " IF line_exists( lt_act_parameter[ key = lr_app_node->key...

        EXIT. ">>>>>>
      ENDIF.

      "-----------------------------------
      " Update Serv PC Quantities
      "-----------------------------------
      DATA(lv_lines) = lines( VALUE /hec1/t_data_app_serv_pc_ct( FOR serv_pc IN lt_app_serv_pc
                                                                 WHERE ( parent_key = lr_app_node->key )
                                                                       ( serv_pc ) ) ).

      IF lr_app_node->hec_app_srv_perf_cat_qty > lv_lines.
        lr_app_node->hec_app_srv_perf_cat_qty = lv_lines.

        " Add line to adjust successor/predecessor
        INSERT VALUE #( key                  = lr_app_node->key
                        parent_key           = lr_app_node->parent_key
                        hec_no_children_node = lv_lines                 ) INTO TABLE lt_act_param_succ.
      ENDIF.

      INSERT VALUE #( data        = lr_app_node
                      node        = is_ctx-node_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_app_node->key                 ) INTO TABLE lt_modification.
    ENDLOOP.


    "-----------------------------------
    " Do Modify
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message) ).
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
                                     node_key  = /hec1/if_configuration_c=>sc_node-app_node
                                     assoc_key = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat )
          it_key          = VALUE #( FOR wa_act_succ IN lt_act_param_succ
                                    ( key = wa_act_succ-key )    )
          iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-set_success_predec )
          iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
          ir_act_param    = me->mr_act_param                                                                                                                   ).

    ENDIF.


    "-----------------------------------
    " Set delete node action
    " to GENERAL
    "-----------------------------------
    IF lt_act_param_del_node IS NOT INITIAL.
      CLEAR me->mr_act_param_delete.
      me->mr_act_param_delete = NEW /bobf/t_frw_node( lt_act_param_del_node ).

      /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
          is_ctx          = CORRESPONDING #( is_ctx )
          it_key          = VALUE #( FOR wa_key IN lt_act_param_del_node
                                     ( key = wa_key-key )                )
          iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-delete_node )
          iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
          ir_act_param    = me->mr_act_param_delete ).

    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_app_server_perf_cat.

    DATA: lt_app_serv_pc     TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_serv_pc_all TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_storage_qty TYPE /hec1/t_data_app_storageqty_ct,
          lt_app_node        TYPE /hec1/t_data_app_node_ct,
          lt_act_param_succ  TYPE /hec1/t_act_set_success_predec,
          lt_modification    TYPE /bobf/t_frw_modification.

    FIELD-SYMBOLS: <fs_param> TYPE /hec1/t_act_update_app_serv_pc.

    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_param>.

    CHECK <fs_param> IS ASSIGNED.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_serv_pc ).

    " DB Node
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_parent
                                      IMPORTING et_data        = lt_app_node
                                                et_target_key  = DATA(lt_app_node_key) ).

    " Get all DB Server Performance Categories
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
                                                it_key         = lt_app_node_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
                                      IMPORTING et_data        = lt_app_serv_pc_all ).

    " App Storage Qty
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_storage_amount
                                      IMPORTING et_data        = lt_app_storage_qty ).

    LOOP AT lt_app_serv_pc REFERENCE INTO DATA(lr_app_serv_pc).

      "-----------------------------------
      " UPDATE pricing for NODES
      "-----------------------------------
      IF line_exists( <fs_param>[ do_update_pricing = abap_true
                                  key               = lr_app_serv_pc->key ] ).

        IF lr_app_serv_pc->hec_effort_required = abap_true.
          DATA(ls_node_pricing) = /hec1/cl_config_helper=>do_price_validation( iv_node_key          = is_ctx-node_key
                                                                               it_key               = VALUE #( ( key = lr_app_serv_pc->key ) )
                                                                               io_read              = io_read
                                                                               iv_effort_bb_guid    = lr_app_serv_pc->hec_timebased_effort_bb_guid
                                                                               iv_tier_is_dr_node   = lr_app_serv_pc->hec_tier_is_dr_node
                                                                               iv_dr_operating_mode = lr_app_serv_pc->hec_dr_oper_mode_value ).


          lr_app_serv_pc->price = CORRESPONDING #( ls_node_pricing ).

          CLEAR ls_node_pricing.
        ENDIF.
      ENDIF. "do_update_pricing

      "-----------------------------------
      " Update Storage Quantities
      "-----------------------------------
      IF line_exists( <fs_param>[ do_update_storage_qty = abap_true
                                  key                   = lr_app_serv_pc->key ] ).

        DATA(lv_lines) = lines( VALUE /hec1/t_data_app_storageqty_ct( FOR storage_qty IN lt_app_storage_qty
                                                                      WHERE ( parent_key = lr_app_serv_pc->key )
                                                                            ( storage_qty ) ) ).

        IF lr_app_serv_pc->hec_storage_qty > lv_lines.

          lr_app_serv_pc->hec_storage_qty = lv_lines.

          " Add line to adjust successor/predecessor
          INSERT VALUE #( key         = lr_app_serv_pc->key
                          parent_key  = lr_app_serv_pc->parent_key
                          hec_no_children_node = lv_lines
                          ) INTO TABLE lt_act_param_succ.

        ENDIF.

      ENDIF. "do_update_storage_qty

      "-----------------------------------
      " Clear Phasing
      "-----------------------------------
      IF line_exists( <fs_param>[ do_clear_phasing = abap_true
                                  key              = lr_app_serv_pc->key ] ).

        IF lines( lt_app_serv_pc_all ) = 1.

          DATA(ls_app_node) = lt_app_node[ key = lr_app_serv_pc->parent_key ].

          lr_app_serv_pc->hec_phase_guid = ls_app_node-hec_phase_guid.
          lr_app_serv_pc->hec_phase_assign_allowed = abap_false.
          lr_app_serv_pc->hec_phase_changed = abap_true.
          lr_app_serv_pc->hec_phase_fixed = abap_true.

        ELSE.

          CLEAR: lr_app_serv_pc->hec_phase_guid,
                 lr_app_serv_pc->hec_phase_fixed.

          lr_app_serv_pc->hec_phase_changed = abap_true.

        ENDIF. " lines(lt_app_serv_pc) = 1

      ENDIF. "do_clear_phasing

      INSERT VALUE #( data        = lr_app_serv_pc
                      node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_app_serv_pc->key
                      ) INTO TABLE lt_modification.

    ENDLOOP. "LOOP AT lt_app_serv_pc REFERENCE INTO DATA(lr_app_serv_pc).

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

    "-----------------------------------
    " Do Modify
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message) ).
    ENDIF.



  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_app_storage.

    DATA: lt_app_server      TYPE /hec1/t_data_app_serv_ct,
          lt_app_serv_pc     TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_storage_qty TYPE /hec1/t_data_app_storageqty_ct,
          lt_app_backup      TYPE /hec1/t_data_app_backup_ct,
          lt_app_storage     TYPE /hec1/t_data_app_storage_ct,
          lt_modification    TYPE /bobf/t_frw_modification.

    CLEAR: eo_message,
           et_failed_key.

    "-----------------------------------
    " this action can be triggered
    " from app server or app storage amount
    " or from app storage
    "-----------------------------------
    CHECK is_ctx-node_key = /hec1/if_configuration_c=>sc_node-app_storage.

    " Get landscape( APM GUID), delivery unit and data center
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).


    io_read->retrieve( EXPORTING iv_node    = is_ctx-node_key
                               it_key       = it_key
                               iv_fill_data = abap_true
                     IMPORTING et_data      = lt_app_storage   ).

    " get backup (children)
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_storage-app_storage_backup
                                      IMPORTING et_data        = lt_app_backup ).

    " get server (parent)
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_storage-to_parent
                                      IMPORTING et_data        = lt_app_server
                                                et_target_key  = DATA(lt_app_server_key) ).

    " get storage qty (parent)
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_storage-to_app_storage_amount
                                      IMPORTING et_data        = lt_app_storage_qty ).

    "-----------------------------------
    " Update app Storage
    "-----------------------------------
    LOOP AT lt_app_server ASSIGNING FIELD-SYMBOL(<fs_app_server>).
      LOOP AT lt_app_storage REFERENCE INTO DATA(lr_app_storage) WHERE parent_key = <fs_app_server>-key.
        TRY.
            DATA(ls_app_storage_qty) = lt_app_storage_qty[ hec_node_app_storage_qty = lr_app_storage->hec_storage_qty_ref_guid ]. "#EC CI_SORTSEQ

            lr_app_storage->hec_has_successor    = ls_app_storage_qty-hec_has_successor.
            lr_app_storage->hec_successor_guid   = ls_app_storage_qty-hec_successor_guid.
            lr_app_storage->hec_predecessor_guid = ls_app_storage_qty-hec_predecessor_guid.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        "-----------------------------------
        " Update App Storage
        "-----------------------------------
        lr_app_storage->hec_storage_quantity = COND #( WHEN <fs_app_server>-hec_srv_main_storage_qty IS NOT INITIAL
                                                       THEN <fs_app_server>-hec_srv_main_storage_qty + ls_app_storage_qty-hec_asq_additional_stor_qty
                                                       ELSE ls_app_storage_qty-hec_asq_main_stor_qty_virtual + ls_app_storage_qty-hec_asq_additional_stor_qty ).

        IF <fs_app_server>-hec_ip_server_guid  IS NOT INITIAL AND
           lr_app_storage->hec_ip_storage_guid IS     INITIAL.

          SELECT *
            FROM /hec1/i_storagelbbasic
           WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid              AND
                 hec_sec_datacenter_guid = @<fs_app_server>-hec_sec_datacenter_guid AND
                 hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid
           INTO TABLE @DATA(lt_storage).

          IF lines( lt_storage ) = 1.
            TRY.
                lr_app_storage->hec_ip_storage_guid = lt_storage[ 1 ]-hec_ip_storage_guid.
              CATCH cx_sy_itab_line_not_found.
            ENDTRY.
          ENDIF.
        ENDIF. " IF <fs_app_server>-hec_ip_server_guid  IS NOT INITIAL AND

        "-----------------------------------
        " Update Backup Qty
        "-----------------------------------
        lr_app_storage->hec_backup_qty = lines( VALUE /hec1/t_data_app_backup_ct( FOR backup IN lt_app_backup
                                                                                  WHERE ( parent_key = lr_app_storage->key )
                                                                                   ( backup )                                ) ).

        INSERT VALUE #( data        = lr_app_storage
                        node        = /hec1/if_configuration_c=>sc_node-app_storage
                        change_mode = /bobf/if_frw_c=>sc_modify_update
                        key         = lr_app_storage->key                            ) INTO TABLE lt_modification.

        CLEAR lt_storage.
      ENDLOOP. "lt_app_storage
    ENDLOOP. "lt_app_server

    "-----------------------------------
    " Do Modify
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message) ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_app_storage_amount.

    DATA: lt_app_storage_qty TYPE /hec1/t_data_app_storageqty_ct,
          lt_app_serv_pc     TYPE /hec1/t_data_app_serv_pc_ct,
          lt_modification    TYPE /bobf/t_frw_modification.

    FIELD-SYMBOLS: <fs_param> TYPE /hec1/t_act_update_app_strgqty.


    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_param>.

    CHECK <fs_param> IS ASSIGNED.

    io_read->retrieve( EXPORTING iv_node  = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                 it_key   = VALUE #( FOR param IN <fs_param>
                                                   ( key = param-parent_key ) )
                       IMPORTING et_data  = lt_app_serv_pc ).

    " App Storage Amount (child)
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                it_key         = VALUE #( FOR param IN <fs_param>
                                                                        ( key = param-parent_key ) )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_storage_amount
                                      IMPORTING et_data        = lt_app_storage_qty      ).


    LOOP AT lt_app_storage_qty REFERENCE INTO DATA(lr_app_storage_qty).
      "-----------------------------------
      " Clear Phasing
      "-----------------------------------
      IF line_exists( <fs_param>[ do_clear_phasing = abap_true
                                  key              = lr_app_storage_qty->key ] ).

        IF lines( lt_app_storage_qty ) = 1.
          " Get Parent Phase
          TRY.
              DATA(ls_app_serv_pc) = lt_app_serv_pc[ key = lr_app_storage_qty->parent_key ].

              lr_app_storage_qty->hec_phase_guid = ls_app_serv_pc-hec_phase_guid.
              lr_app_storage_qty->hec_phase_assign_allowed = abap_false.
              lr_app_storage_qty->hec_phase_changed = abap_true.
              lr_app_storage_qty->hec_phase_fixed = abap_true.

            CATCH cx_sy_itab_line_not_found.
          ENDTRY.

        ELSE.

          CLEAR: lr_app_storage_qty->hec_phase_guid,
                 lr_app_storage_qty->hec_phase_fixed.

          lr_app_storage_qty->hec_phase_changed = abap_true.

        ENDIF. "lines(lt_db_storage_qty) = 1.

      ENDIF. "do_clear_phasing

      INSERT VALUE #( data        = lr_app_storage_qty
                      node        = /hec1/if_configuration_c=>sc_node-app_storage_amount
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_app_storage_qty->key
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


  METHOD /hec1/if_config_action_intern~update_datacenter.

    DATA: lv_datacenter_guid TYPE /hec1/datacenter_fdt_guid,
          lt_modification    TYPE /bobf/t_frw_modification.

    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_update_datacenter.


    CLEAR: eo_message,
           et_failed_key.

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    "-----------------------------------
    " Get data center, data center type
    "-----------------------------------
    SELECT *
      FROM /hec1/i_datacentertypebasic
     WHERE hec_apm_guid = @lr_landscape->hec_apm_guid
      INTO TABLE @DATA(lt_datacenter_type).

    SELECT *
      FROM /hec1/i_datacenterbasic
     WHERE hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid
      INTO TABLE @DATA(lt_data_center).


    IF is_ctx-node_key = /hec1/if_configuration_c=>sc_node-root.
      " ***************************************************************************
      " Update is triggered from Landscape
      " ***************************************************************************
      IF lines( lt_datacenter ) = 1.

        TRY.
            DATA(lr_datacenter)      = NEW /hec1/s_data_datacenter_cs( lt_datacenter[ 1 ] ).
            DATA(ls_datacenter_type) = lt_datacenter_type[ hec_datacenter_type_value = /hec1/if_config_constants=>gc_datacenter_type_primary ].

            lr_datacenter->hec_datacenter_type_value = ls_datacenter_type-hec_datacenter_type_value.
            lr_datacenter->hec_datacenter_type_descr = ls_datacenter_type-hec_datacenter_type_descr.

            IF lr_datacenter->hec_datacenter_guid IS INITIAL. "only inherit the delivery regions if no datacenter is set yet
              lr_datacenter->hec_dlvy_region_l1_guid  = lr_landscape->hec_dlvy_region_l1_guid.
              lr_datacenter->hec_dlvy_region_l1_descr = lr_landscape->hec_dlvy_region_l1_descr.
              lr_datacenter->hec_dlvy_region_l2_guid  = lr_landscape->hec_dlvy_region_l2_guid.
              lr_datacenter->hec_dlvy_region_l2_descr = lr_landscape->hec_dlvy_region_l2_descr.
              lr_datacenter->hec_datacenter_country = lr_landscape->hec_country_key.
              lr_datacenter->hec_datacenter_country_descr = lr_landscape->hec_country_descr.
            ENDIF.

            INSERT VALUE #( data        = lr_datacenter
                            node        = /hec1/if_configuration_c=>sc_node-datacenter
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_datacenter->key                            ) INTO TABLE lt_modification.

          CATCH cx_sy_itab_line_not_found.
        ENDTRY.
      ELSE.

        LOOP AT lt_datacenter REFERENCE INTO lr_datacenter
          WHERE hec_datacenter_guid IS INITIAL. "only inherit the delivery regions if no datacenter is set yet

          lr_datacenter->hec_dlvy_region_l1_guid  = lr_landscape->hec_dlvy_region_l1_guid.
          lr_datacenter->hec_dlvy_region_l1_descr = lr_landscape->hec_dlvy_region_l1_descr.
          lr_datacenter->hec_dlvy_region_l2_guid  = lr_landscape->hec_dlvy_region_l2_guid.
          lr_datacenter->hec_dlvy_region_l2_descr = lr_landscape->hec_dlvy_region_l2_descr.
          lr_datacenter->hec_datacenter_country = lr_landscape->hec_country_key.
          lr_datacenter->hec_datacenter_country_descr = lr_landscape->hec_country_descr.

          INSERT VALUE #( data        = lr_datacenter
                          node        = /hec1/if_configuration_c=>sc_node-datacenter
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_datacenter->key                            ) INTO TABLE lt_modification.

        ENDLOOP.

      ENDIF. " lines( lt_datacenter ) = 1.

    ELSEIF is_ctx-node_key = /hec1/if_configuration_c=>sc_node-delivery_unit.
      " ***************************************************************************
      " Update is triggered from Delivery Unit
      " ***************************************************************************
      ASSIGN ir_parameter->* TO <fs_act_param>.
      IF <fs_act_param> IS ASSIGNED.
        DATA(ls_act_param) = VALUE #( <fs_act_param>[ 1 ] ).

        LOOP AT lt_datacenter REFERENCE INTO lr_datacenter.

          IF ls_act_param-do_update_search_fields = abap_true.
            lr_datacenter->hec_delivery_unit_guid     = lr_dlvy_unit->hec_delivery_unit_guid.
            lr_datacenter->hec_delivery_unit_descr    = lr_dlvy_unit->hec_delivery_unit_descr.
            lr_datacenter->hec_infra_provider_guid    = lr_dlvy_unit->hec_inf_provider_guid.
            lr_datacenter->hec_inf_provider_descr     = lr_dlvy_unit->hec_inf_provider_descr.

          ELSEIF ls_act_param-do_reset = abap_true.
            CLEAR: lr_datacenter->hec_delivery_unit_guid,
                   lr_datacenter->hec_delivery_unit_descr,
                   lr_datacenter->hec_infra_provider_guid,
                   lr_datacenter->hec_inf_provider_descr,
                   lr_datacenter->hec_datacenter_country,
                   lr_datacenter->hec_datacenter_country_descr,
                   lr_datacenter->hec_datacenter_guid,
                   lr_datacenter->hec_datacenter_descr.
          ENDIF.

          INSERT VALUE #( data        = lr_datacenter
                          node        = /hec1/if_configuration_c=>sc_node-datacenter
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_datacenter->key                            ) INTO TABLE lt_modification.

        ENDLOOP.

      ENDIF. "if <fs_act_param> is assigned.
    ELSE.
      " ***************************************************************************
      " Update is triggered from App Server or DB Server
      " ***************************************************************************
      ASSIGN ir_parameter->* TO <fs_act_param>.
      IF <fs_act_param> IS ASSIGNED.

        LOOP AT <fs_act_param> ASSIGNING FIELD-SYMBOL(<fs_param>).

          TRY.
              DATA(ls_data_center) = lt_data_center[ hec_datacenter_guid = <fs_param>-hec_datacenter_fdt_guid ].

              "-----------------------------------
              " Update Datacenter
              "-----------------------------------
              LOOP AT lt_datacenter REFERENCE INTO lr_datacenter
                WHERE key = <fs_param>-key.

                lr_datacenter->hec_datacenter_guid     = ls_data_center-hec_datacenter_guid.
                lr_datacenter->hec_sec_datacenter_guid = ls_data_center-hec_sec_datacenter_guid.
                lr_datacenter->hec_datacenter_descr    = ls_data_center-hec_datacenter_descr.
                lr_datacenter->hec_datacenter_country  = ls_data_center-hec_datacenter_country.
                lr_datacenter->hec_tree_descr          = ls_data_center-hec_datacenter_descr. "#EC CI_FLDEXT_OK[2215424]


                INSERT VALUE #( data        = lr_datacenter
                                node        = /hec1/if_configuration_c=>sc_node-datacenter
                                change_mode = /bobf/if_frw_c=>sc_modify_update
                                key         = lr_datacenter->key                           ) INTO TABLE lt_modification.

              ENDLOOP.
            CATCH cx_sy_itab_line_not_found.
          ENDTRY.

          CLEAR: ls_data_center,
                 lr_datacenter.
        ENDLOOP.
      ENDIF. " IF <fs_act_param> IS ASSIGNED.
    ENDIF. " IF is_ctx-node_key = /hec1/if_configuration_c=>sc_node-landscape.


    "-----------------------------------
    " Do Modify
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message) ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_db_node.

    DATA: lt_db_node             TYPE /hec1/t_data_db_node_ct,
          lt_non_def_master_node TYPE /hec1/t_data_db_node_ct,
          lt_db_serv_pc          TYPE /hec1/t_data_db_serv_pc_ct,
          lt_node_key            TYPE /bobf/t_frw_key,
          lt_non_def_master_key  TYPE /bobf/t_frw_key,
          lt_act_param_succ      TYPE /hec1/t_act_set_success_predec,
          lt_act_param_del_node  TYPE /bobf/t_frw_node,
          lt_modification        TYPE /bobf/t_frw_modification.

    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_update_db_node.



    CLEAR: eo_message,
           et_failed_key.


    ASSIGN ir_parameter->* TO <fs_act_param>.
    IF <fs_act_param> IS ASSIGNED.
      DATA(lt_act_parameter) = <fs_act_param>.

      LOOP AT lt_act_parameter ASSIGNING FIELD-SYMBOL(<fs_act_paramter>)
        WHERE do_release_node   = abap_true OR
              do_delete_subnode = abap_true.

        IF NOT line_exists( lt_non_def_master_key[ key = <fs_act_paramter>-key ] ).
          /hec1/cl_bopf_config_validat_h=>check_standby_node_is_released( EXPORTING iv_check_rule = /hec1/if_bopf_constants=>gc_check_rule-node
                                                                                    is_ctx        = CORRESPONDING #( is_ctx )
                                                                                    it_key        = VALUE #( ( key = <fs_act_paramter>-key ) )
                                                                                    io_read       = io_read
                                                                          IMPORTING et_node_key   = lt_node_key ).

          APPEND LINES OF lt_node_key TO lt_non_def_master_key.
          CLEAR lt_node_key.
        ENDIF.
      ENDLOOP.

      " Get standby/worker node
      IF lt_non_def_master_key IS NOT INITIAL.
        io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                     it_key  = lt_non_def_master_key
                           IMPORTING et_data = lt_non_def_master_node ).

        " Get standby/worker node: server performance category
        io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                    it_key         = lt_non_def_master_key
                                                    iv_fill_data   = abap_false
                                                    iv_association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                                          IMPORTING et_key_link    = DATA(lt_spc_key_link) ).
      ENDIF.
    ENDIF. " IF <fs_act_param> IS ASSIGNED.


    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_node ).

    " DB Storage Qty
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                                      IMPORTING et_data        = lt_db_serv_pc ).




    LOOP AT lt_db_node REFERENCE INTO DATA(lr_db_node).
      "-----------------------------------
      " Release standby/worker node for
      " selection or delete subnodes of
      " standby/worker node
      "-----------------------------------
      IF line_exists( lt_act_parameter[ key               = lr_db_node->key
                                        do_release_node   = abap_true        ] ) OR
         line_exists( lt_act_parameter[ key               = lr_db_node->key
                                        do_delete_subnode = abap_true        ] ).

        " Check master node is complete configered
        " ( including sub nodes: server performance category and storage amount )
        DATA(lv_complete) = /hec1/cl_bopf_config_validat_h=>check_master_node_is_complete( iv_check_rule = /hec1/if_bopf_constants=>gc_check_rule-node
                                                                                           is_ctx        = CORRESPONDING #( is_ctx )
                                                                                           it_key        = VALUE #( ( key = lr_db_node->key ) )
                                                                                           io_read       = io_read ).

        LOOP AT lt_non_def_master_node
        REFERENCE INTO DATA(lr_node)
        WHERE parent_key = lr_db_node->parent_key.

          IF lr_node->hec_row_selectable <> lv_complete.
            lr_node->hec_row_selectable = lv_complete.
            DATA(lv_data_changed) = abap_true.
          ENDIF.


          IF line_exists( lt_act_parameter[ key               = lr_db_node->key
                                            do_delete_subnode = abap_true       ] ).

            CLEAR: lr_node->hec_phase_guid,
                   lr_node->hec_db_srv_perf_cat_qty.

            lv_data_changed = abap_true.
          ENDIF.

          IF lv_data_changed = abap_true.
            INSERT VALUE #( data        = lr_node
                            node        = is_ctx-node_key
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_node->key                     ) INTO TABLE lt_modification.
          ENDIF.
          CLEAR lv_data_changed.
        ENDLOOP.

        "-----------------------------------
        "  Fill action table for delete
        " standby/worker node subnodes
        "-----------------------------------
        IF line_exists( lt_act_parameter[ key               = lr_db_node->key
                                          do_delete_subnode = abap_true       ] ) AND
           lt_spc_key_link IS NOT INITIAL.

          lt_act_param_del_node = VALUE #( FOR wa IN lt_spc_key_link
                                          ( node = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                            key  = wa-target_key                                           ) ).
        ENDIF. " IF line_exists( lt_act_parameter[ key = lr_db_node->key...

        EXIT. ">>>>>>
      ENDIF.

      "-----------------------------------
      " UPDATE pricing for NODES
      "-----------------------------------
      IF lr_db_node->hec_effort_required = abap_true.
        DATA(ls_node_pricing) = /hec1/cl_config_helper=>do_price_validation( iv_node_key          = is_ctx-node_key
                                                                             it_key               = VALUE #( ( key = lr_db_node->key ) )
                                                                             io_read              = io_read
                                                                             iv_effort_bb_guid    = lr_db_node->hec_timebased_effort_bb_guid
                                                                             iv_tier_is_dr_node   = lr_db_node->hec_tier_is_dr_node
                                                                             iv_dr_operating_mode = lr_db_node->hec_dr_oper_mode_value ).

        lr_db_node->price = CORRESPONDING #( ls_node_pricing ).
        lv_data_changed = abap_true.
      ENDIF.

      "-----------------------------------
      " Update Serv PC Quantities
      "-----------------------------------
      DATA(lv_lines) = lines( VALUE /hec1/t_data_db_serv_pc_ct( FOR serv_pc IN lt_db_serv_pc
                                                                WHERE ( parent_key = lr_db_node->key )
                                                                      ( serv_pc )                      ) ).

      IF lr_db_node->hec_db_srv_perf_cat_qty > lv_lines.
        lr_db_node->hec_db_srv_perf_cat_qty = lv_lines.

        " Add line to adjust successor/predecessor
        INSERT VALUE #( key                  = lr_db_node->key
                        parent_key           = lr_db_node->parent_key
                        hec_no_children_node = lv_lines               ) INTO TABLE lt_act_param_succ.
      ENDIF.

      IF lv_data_changed = abap_true.
        INSERT VALUE #( data        = lr_db_node
                        node        = /hec1/if_configuration_c=>sc_node-db_node
                        source_node = /hec1/if_configuration_c=>sc_node-instance_db
                        association = /hec1/if_configuration_c=>sc_association-instance_db-db_node
                        source_key  = lr_db_node->parent_key
                        change_mode = /bobf/if_frw_c=>sc_modify_update
                        key         = lr_db_node->key                                               ) INTO TABLE lt_modification.
      ENDIF.

      CLEAR ls_node_pricing.
    ENDLOOP.


    "-----------------------------------
    " Do Modify
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message) ).
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
                                     node_key  = /hec1/if_configuration_c=>sc_node-db_node
                                     assoc_key = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat )
          it_key          = VALUE #( FOR wa_act_succ IN lt_act_param_succ
                                    ( key = wa_act_succ-key )    )
          iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-set_success_predec )
          iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
          ir_act_param    = me->mr_act_param                                                                                                                   ).

    ENDIF.


    "-----------------------------------
    " Set delete node action
    " to GENERAL
    "-----------------------------------
    IF lt_act_param_del_node IS NOT INITIAL.
      CLEAR me->mr_act_param_delete.
      me->mr_act_param_delete = NEW /bobf/t_frw_node( lt_act_param_del_node ).

      /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
          is_ctx          = CORRESPONDING #( is_ctx )
          it_key          = VALUE #( FOR wa_key IN lt_act_param_del_node
                                     ( key = wa_key-key )                )
          iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-delete_node )
          iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
          ir_act_param    = me->mr_act_param_delete ).

    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_db_server.

    DATA: lt_db_serv_perf_cat TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_server        TYPE /hec1/t_data_db_serv_ct,
          lt_modification     TYPE /bobf/t_frw_modification.

    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_update_db_server.



    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_act_param>.

    io_read->retrieve( EXPORTING iv_node    = is_ctx-node_key
                                 it_key     = it_key
                       IMPORTING et_data    = lt_db_serv_perf_cat ).

    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_server
                                      IMPORTING et_data        = lt_db_server                                                             ).

    IF lt_db_server IS INITIAL.
      RETURN. ">>>>>>
    ENDIF.

    IF <fs_act_param> IS ASSIGNED.
      "-----------------------------------
      " Fill DB server update structure
      "-----------------------------------
      LOOP AT lt_db_serv_perf_cat ASSIGNING FIELD-SYMBOL(<fs_serv_perf_cat>).

        TRY.
            DATA(ls_act_param) = <fs_act_param>[ parent_key = <fs_serv_perf_cat>-key ].

            IF ls_act_param-do_update_db_server = abap_true.
              DATA(lr_db_server) = NEW /hec1/s_data_db_serv_cs( lt_db_server[ key = ls_act_param-key ] ).
              " Update IP Server GUID
              lr_db_server->hec_ip_server_guid = ls_act_param-hec_ip_server_guid.
              DATA(lv_data_changed) = abap_true.
            ENDIF..

            "-----------------------------------
            " Fill DB server update structure
            "-----------------------------------
            IF lv_data_changed = abap_true.
              INSERT VALUE #( data        = lr_db_server
                              node        = /hec1/if_configuration_c=>sc_node-db_server
                              source_node = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                              association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_server
                              source_key  = lr_db_server->parent_key
                              change_mode = /bobf/if_frw_c=>sc_modify_update
                              key         = lr_db_server->key                                                        ) INTO TABLE lt_modification.
            ENDIF.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        CLEAR: lv_data_changed,
               ls_act_param,
               lr_db_server.
      ENDLOOP.
    ENDIF. " IF <fs_act_param> IS ASSIGNED.

    "-----------------------------------
    " Update instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_db_server_perf_cat.

    DATA: lt_db_serv_pc     TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_serv_pc_all TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_storage_qty TYPE /hec1/t_data_db_storage_qty_ct,
          lt_db_node        TYPE /hec1/t_data_db_node_ct,
          lt_act_param_succ TYPE /hec1/t_act_set_success_predec,
          lt_modification   TYPE /bobf/t_frw_modification.

    FIELD-SYMBOLS: <fs_param> TYPE /hec1/t_act_update_db_serv_pc.


    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_param>.

    CHECK <fs_param> IS ASSIGNED.

    io_read->retrieve( EXPORTING iv_node    = is_ctx-node_key
                                 it_key     = it_key
                       IMPORTING et_data    = lt_db_serv_pc ).

    " DB Node
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-to_parent
                                      IMPORTING et_data        = lt_db_node
                                                et_target_key  = DATA(lt_db_node_key)  ).

    " Get all DB Server Performance Categories
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_node
                                                it_key         = lt_db_node_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                                      IMPORTING et_data        = lt_db_serv_pc_all  ).

    " DB Storage Qty
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount
                                      IMPORTING et_data        = lt_db_storage_qty  ).

    LOOP AT lt_db_serv_pc REFERENCE INTO DATA(lr_db_serv_pc).

      "-----------------------------------
      " Update Storage Quantities
      "-----------------------------------
      IF line_exists( <fs_param>[ do_update_storage_qty = abap_true
                                  key                   = lr_db_serv_pc->key ] ).

        DATA(lv_lines) = lines( VALUE /hec1/t_data_db_storage_qty_ct( FOR storage_qty IN lt_db_storage_qty
                                                                      WHERE ( parent_key = lr_db_serv_pc->key )
                                                                            ( storage_qty ) ) ).

        IF lr_db_serv_pc->hec_storage_qty > lv_lines.

          lr_db_serv_pc->hec_storage_qty = lv_lines.

          " Add line to adjust successor/predecessor
          INSERT VALUE #( key                  = lr_db_serv_pc->key
                          parent_key           = lr_db_serv_pc->parent_key
                          hec_no_children_node = lv_lines
                          ) INTO TABLE lt_act_param_succ.
        ENDIF.

      ENDIF. "do_update_storage_qty

      "-----------------------------------
      " Clear Phasing
      "-----------------------------------
      IF line_exists( <fs_param>[ do_clear_phasing = abap_true ] ).

        IF lines( lt_db_serv_pc_all ) = 1.
          " Get Parent Phase

          DATA(ls_db_node) = lt_db_node[ key = lr_db_serv_pc->parent_key ].

          lr_db_serv_pc->hec_phase_guid = ls_db_node-hec_phase_guid.
          lr_db_serv_pc->hec_phase_assign_allowed = abap_false.
          lr_db_serv_pc->hec_phase_changed = abap_true.
          lr_db_serv_pc->hec_phase_fixed = abap_true.

        ELSE.

          CLEAR: lr_db_serv_pc->hec_phase_guid,
                 lr_db_serv_pc->hec_phase_fixed.

          lr_db_serv_pc->hec_phase_changed = abap_true.

        ENDIF. "lines(lt_db_serv_pc_all) = 1

      ENDIF. "do_clear_phasing

      INSERT VALUE #( data        = lr_db_serv_pc
                      node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_db_serv_pc->key
                      ) INTO TABLE lt_modification.

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
                                     node_key  = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                     assoc_key = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount )
          it_key          = VALUE #( FOR wa_act_succ IN lt_act_param_succ
                                    ( key = wa_act_succ-key )    )
          iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-set_success_predec )
          iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
          ir_act_param    = me->mr_act_param                                                                                                                   ).

    ENDIF.

    "-----------------------------------
    " Do Modify
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_db_storage.

    DATA: lt_db_server      TYPE /hec1/t_data_db_serv_ct,
          lt_db_serv_pc     TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_storage_qty TYPE /hec1/t_data_db_storage_qty_ct,
          lt_db_storage     TYPE /hec1/t_data_db_storage_ct,
          lt_db_backup      TYPE /hec1/t_data_db_backup_ct,
          lt_modification   TYPE /bobf/t_frw_modification.


    CLEAR: eo_message,
           et_failed_key.

    "-----------------------------------
    " this action can be triggered
    " from db server or db storage amount
    " or from db storage
    "-----------------------------------
    CHECK is_ctx-node_key = /hec1/if_configuration_c=>sc_node-db_storage.

    " Get landscape( APM GUID), delivery unit and data center
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).


    io_read->retrieve( EXPORTING iv_node      = is_ctx-node_key
                               it_key       = it_key
                               iv_fill_data = abap_true
                     IMPORTING et_data      = lt_db_storage ).

    " get backup (children)
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_storage-db_storage_backup
                                      IMPORTING et_data        = lt_db_backup ).

    " get server (parent)
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_storage-to_parent
                                      IMPORTING et_data        = lt_db_server
                                                et_target_key  = DATA(lt_db_server_key) ).

    " get storage qty (parent) - 2 steps
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server
                                                it_key         = lt_db_server_key
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server-to_parent
                                      IMPORTING et_target_key  = DATA(lt_db_serv_pc_key)
                                                et_key_link    = DATA(lt_server_to_spc_link) ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                it_key         = lt_db_serv_pc_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount
                                      IMPORTING et_key_link    = DATA(lt_spc_to_storage_qty_link)
                                                et_data        = lt_db_storage_qty ).

    "-----------------------------------
    " Update DB Storage
    "-----------------------------------
    LOOP AT lt_db_server ASSIGNING FIELD-SYMBOL(<fs_db_server>).
      LOOP AT lt_db_storage REFERENCE INTO DATA(lr_db_storage) WHERE parent_key = <fs_db_server>-key.
        TRY.
            DATA(ls_db_storage_qty) = lt_db_storage_qty[ hec_node_db_storage_qty = lr_db_storage->hec_storage_qty_ref_guid ]. "#EC CI_SORTSEQ

            lr_db_storage->hec_has_successor    = ls_db_storage_qty-hec_has_successor.
            lr_db_storage->hec_successor_guid   = ls_db_storage_qty-hec_successor_guid.
            lr_db_storage->hec_predecessor_guid = ls_db_storage_qty-hec_predecessor_guid.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        "-----------------------------------
        " Update DB storage
        "-----------------------------------
        lr_db_storage->hec_storage_quantity = COND #( WHEN <fs_db_server>-hec_srv_main_stor_qty IS NOT INITIAL
                                                          THEN <fs_db_server>-hec_srv_main_stor_qty + ls_db_storage_qty-hec_dsq_additional_stor_qty
                                                          ELSE COND #( WHEN <fs_db_server>-hec_host_type_value  = /hec1/if_config_constants=>gc_server_host_type-physical
                                                                       THEN ls_db_storage_qty-hec_dsq_main_stor_qty_physical + ls_db_storage_qty-hec_dsq_additional_stor_qty
                                                                       ELSE ls_db_storage_qty-hec_dsq_main_stor_qty_virtual  + ls_db_storage_qty-hec_dsq_additional_stor_qty ) ).

        IF <fs_db_server>-hec_ip_server_guid  IS NOT INITIAL AND
           lr_db_storage->hec_ip_storage_guid IS     INITIAL.

          SELECT *
            FROM /hec1/i_storagelbbasic
           WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid             AND
                 hec_sec_datacenter_guid = @<fs_db_server>-hec_sec_datacenter_guid AND
                 hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid
           INTO TABLE @DATA(lt_storage).

          IF lines( lt_storage ) = 1.
            TRY.
                lr_db_storage->hec_ip_storage_guid = lt_storage[ 1 ]-hec_ip_storage_guid.
              CATCH cx_sy_itab_line_not_found.
            ENDTRY.
          ENDIF.
        ENDIF. " IF <fs_db_server>-hec_ip_server_guid  IS NOT INITIAL AND


        "-----------------------------------
        " Update Backup Qty
        "-----------------------------------
        lr_db_storage->hec_backup_qty = lines( VALUE /hec1/t_data_db_backup_ct( FOR backup IN lt_db_backup
                                                                                    WHERE ( parent_key = lr_db_storage->key )
                                                                                     ( backup )                               ) ).

        INSERT VALUE #( data        = lr_db_storage
                        node        = /hec1/if_configuration_c=>sc_node-db_storage
                        source_node = /hec1/if_configuration_c=>sc_node-db_server
                        association = /hec1/if_configuration_c=>sc_association-db_server-db_storage
                        source_key  = lr_db_storage->parent_key
                        change_mode = /bobf/if_frw_c=>sc_modify_update
                        key         = lr_db_storage->key                                            ) INTO TABLE lt_modification.

      ENDLOOP. " LOOP AT lt_db_storage REFERENCE INTO DATA(lr_db_storage)...
    ENDLOOP. " LOOP AT lt_db_server ASSIGNING FIELD-SYMBOL(<fs_db_server>).


    "-----------------------------------
    " Update instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message) ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_db_storage_amount.

    DATA: lt_db_serv_pc     TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_storage_qty TYPE /hec1/t_data_db_storage_qty_ct,
          lt_modification   TYPE /bobf/t_frw_modification,
          lv_ram_class      TYPE int4.

    FIELD-SYMBOLS: <fs_param> TYPE /hec1/t_act_update_db_strg_qty.
    CONSTANTS: lc_factor TYPE p DECIMALS 1 VALUE '1.2'.

    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_param>.

    CHECK <fs_param> IS ASSIGNED.

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    io_read->retrieve( EXPORTING iv_node       = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                 it_key        = VALUE #( FOR param IN <fs_param>
                                                        ( key = param-parent_key ) )
                       IMPORTING et_data       = lt_db_serv_pc ).

    " DB Storage Amount (child)
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                it_key         = VALUE #( FOR param IN <fs_param>
                                                                        ( key = param-parent_key ) )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount
                                      IMPORTING et_data        = lt_db_storage_qty                                                                ).


    "-----------------------------------
    " Get DB server performance category
    "-----------------------------------
    DATA(lt_range_table) = VALUE /hec1/t_selection_range( FOR wa IN lt_db_serv_pc
                                                        ( option = /hec1/if_config_constants=>gc_range_option-eq
                                                          sign   = /hec1/if_config_constants=>gc_range_sign-i
                                                          low    = wa-hec_srv_perf_cat_guid                      ) ).

    SELECT *                                  "#EC CI_ALL_FIELDS_NEEDED
      FROM /hec1/i_dbservperfcatbasic
     WHERE hec_apm_guid           = @lr_landscape->hec_apm_guid AND
           hec_srv_perf_cat_guid IN @lt_range_table
      INTO TABLE @DATA(lt_serv_perf_cat).


    " Here we loop across the server performance category, which is the parent
    " The update can be executed from the server performance category and then needs to run for all child nodes
    LOOP AT lt_db_serv_pc ASSIGNING FIELD-SYMBOL(<fs_db_serv_pc>).

      LOOP AT lt_db_storage_qty
        REFERENCE INTO DATA(lr_db_storage_qty)
        WHERE parent_key = <fs_db_serv_pc>-key.
        "-----------------------------------
        " Update Storage
        "-----------------------------------
        IF line_exists( <fs_param>[ do_update_storage = abap_true
                                    parent_key        = <fs_db_serv_pc>-key ] ).

          TRY.
              DATA(ls_serv_perf_cat) = lt_serv_perf_cat[ hec_srv_perf_cat_guid = <fs_db_serv_pc>-hec_srv_perf_cat_guid ].
            CATCH cx_sy_itab_line_not_found.
          ENDTRY.

          lv_ram_class = ls_serv_perf_cat-hec_srv_ram_class.

          lr_db_storage_qty->hec_dsq_main_stor_qty_physical = COND #( WHEN <fs_db_serv_pc>-hec_db_srv_type_value = /hec1/if_config_constants=>gc_db_server_type-hana
                                                                      THEN 10
                                                                      ELSE space                                                                                     ).

          lr_db_storage_qty->hec_dsq_main_stor_qty_virtual  = COND #( WHEN <fs_db_serv_pc>-hec_db_srv_type_value = /hec1/if_config_constants=>gc_db_server_type-hana
                                                                      THEN |{ lc_factor * lv_ram_class }|
                                                                      ELSE space                                                                                     ).

          INSERT VALUE #( data        = lr_db_storage_qty
                          node        = /hec1/if_configuration_c=>sc_node-db_storage_amount
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_db_storage_qty->key                              ) INTO TABLE lt_modification.

          CLEAR: lv_ram_class,
                 ls_serv_perf_cat.

        ENDIF. " do_update_storage

        "-----------------------------------
        " Clear Phasing
        "-----------------------------------
        IF line_exists( <fs_param>[ do_clear_phasing = abap_true
                                    key              = lr_db_storage_qty->key ] ).


          IF lines( lt_db_storage_qty ) = 1.
            " Get Parent Phase
            TRY.
                DATA(ls_db_serv_pc) = lt_db_serv_pc[ key = lr_db_storage_qty->parent_key ].

                lr_db_storage_qty->hec_phase_guid = ls_db_serv_pc-hec_phase_guid.
                lr_db_storage_qty->hec_phase_assign_allowed = abap_false.
                lr_db_storage_qty->hec_phase_changed = abap_true.
                lr_db_storage_qty->hec_phase_fixed = abap_true.

              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

          ELSE.

            CLEAR: lr_db_storage_qty->hec_phase_guid,
                   lr_db_storage_qty->hec_phase_fixed.

            lr_db_storage_qty->hec_phase_changed = abap_true.

          ENDIF. "lines(lt_db_storage_qty) = 1

        ENDIF. "do_clear_phasing

        INSERT VALUE #( data        = lr_db_storage_qty
                        node        = /hec1/if_configuration_c=>sc_node-db_storage_amount
                        change_mode = /bobf/if_frw_c=>sc_modify_update
                        key         = lr_db_storage_qty->key                              ) INTO TABLE lt_modification.

      ENDLOOP. "lt_db_storage_qty
    ENDLOOP. "lt_db_serv_pc

    "-----------------------------------
    " Do Modify
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message) ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_delivery_unit.

    DATA: lt_modification TYPE /bobf/t_frw_modification.
    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_update_dlvy_unit.


    CLEAR: eo_message,
           et_failed_key.

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).
    "-----------------------------------
    " Get delivery unit and
    " infrastructure provider
    "-----------------------------------
    SELECT *                                            "#EC CI_NOWHERE
      FROM /hec1/i_deliveryunitbasic
      INTO TABLE @DATA(lt_dlvy_unit).

    SELECT *                                            "#EC CI_NOWHERE
      FROM /hec1/i_infraproviderbasic
      INTO TABLE @DATA(lt_inf_provider).


    ASSIGN ir_parameter->* TO <fs_act_param>.

    IF <fs_act_param> IS ASSIGNED.
      "-----------------------------------
      " Fill delivery unit structure
      "-----------------------------------
      LOOP AT <fs_act_param> ASSIGNING FIELD-SYMBOL(<fs_param>).

        TRY.
            DATA(ls_inf_provider) = lt_inf_provider[ hec_infra_provider_guid = <fs_param>-hec_inf_provider_guid ].
            DATA(ls_dlvy_unit)    = lt_dlvy_unit[ hec_delivery_unit_guid = ls_inf_provider-hec_delivery_unit_guid ].

            IF lr_dlvy_unit->hec_inf_provider_guid      <> ls_inf_provider-hec_infra_provider_guid    OR
               lr_dlvy_unit->hec_inf_provider_category  <> ls_inf_provider-hec_inf_provider_cat_value OR
               lr_dlvy_unit->hec_delivery_unit_guid     <> ls_dlvy_unit-hec_delivery_unit_guid        OR
               lr_dlvy_unit->hec_delivery_unit_category <> ls_dlvy_unit-hec_delivery_unit_cat_value.

              lr_dlvy_unit->hec_inf_provider_guid      = ls_inf_provider-hec_infra_provider_guid.
              lr_dlvy_unit->hec_inf_provider_descr     = ls_inf_provider-hec_inf_provider_descr.
              lr_dlvy_unit->hec_inf_provider_category  = ls_inf_provider-hec_inf_provider_cat_value.
              lr_dlvy_unit->hec_delivery_unit_guid     = ls_dlvy_unit-hec_delivery_unit_guid.
              lr_dlvy_unit->hec_delivery_unit_descr    = ls_dlvy_unit-hec_delivery_unit_descr.
              lr_dlvy_unit->hec_delivery_unit_category = ls_dlvy_unit-hec_delivery_unit_cat_value.

              INSERT VALUE #( data        = lr_dlvy_unit
                              node        = /hec1/if_configuration_c=>sc_node-delivery_unit
                              change_mode = /bobf/if_frw_c=>sc_modify_update
                              key         = lr_dlvy_unit->key                               ) INTO TABLE lt_modification.
            ENDIF.

          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        CLEAR: ls_inf_provider,
               ls_dlvy_unit.

      ENDLOOP.
    ENDIF. " IF <fs_act_param> IS ASSIGNED.

    "-----------------------------------
    " Update instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_if_baseline.

    DATA: lt_if_baseline  TYPE /hec1/t_data_if_baseline_ct,
          lt_modification TYPE /bobf/t_frw_modification.



    CLEAR: eo_message,
           et_failed_key.

    CHECK is_ctx-node_key = /hec1/if_configuration_c=>sc_node-infrastructure_baseline.

    io_read->retrieve( EXPORTING iv_node      = is_ctx-node_key
                                 it_key       = it_key
                                 iv_fill_data = abap_true
                       IMPORTING et_data      = lt_if_baseline ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).


    LOOP AT lt_if_baseline REFERENCE INTO DATA(lr_if_baseline).

      TRY.
          DATA(ls_datacenter) = lt_datacenter[ key = lr_if_baseline->parent_key ].
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.

      "-----------------------------------
      " Get Price
      "-----------------------------------
      TRY.
          DATA(lv_datacenter_guid) = lt_datacenter[ key = lr_if_baseline->parent_key ]-hec_datacenter_guid.
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.

      SELECT SINGLE hec_cb_pricing_lb_guid
        FROM /hec1/i_infrabaselinelbbasic
       WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid            AND
             hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid   AND
             hec_sec_datacenter_guid = @lv_datacenter_guid
        INTO @DATA(lv_lb_guid).


      SELECT SINGLE * FROM /hec1/c_cbp_lb     "#EC CI_ALL_FIELDS_NEEDED
         INTO @DATA(ls_pricing)
        WHERE hec_price_lb = @lv_lb_guid.

      lr_if_baseline->price = CORRESPONDING #( ls_pricing ).
      lr_if_baseline->hec_phase_guid  = ls_datacenter-hec_phase_guid.

      INSERT VALUE #( data        = lr_if_baseline
                      node        = /hec1/if_configuration_c=>sc_node-infrastructure_baseline
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_if_baseline->key                                       ) INTO TABLE lt_modification.

      CLEAR: lv_lb_guid,
             ls_pricing.
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


  METHOD /hec1/if_config_action_intern~update_man_serv_baseline.

    DATA: lt_modification TYPE /bobf/t_frw_modification.


    CLEAR: eo_message,
           et_failed_key.

    "-----------------------------------
    " Get APM model GUID and description
    " delivery unit and managed service
    " baseline
    "-----------------------------------
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key          = is_ctx-node_key
                                                        it_key               = it_key
                                                        io_read              = io_read
                                              IMPORTING er_landscape         = DATA(lr_landscape)
                                                        er_delivery_unit     = DATA(lr_dlvy_unit)
                                                        et_man_serv_baseline = DATA(lt_man_serv_baseline)
                                                        et_failed_key        = et_failed_key ).


    IF lr_dlvy_unit->hec_delivery_unit_guid               IS NOT INITIAL AND
       lr_dlvy_unit->hec_delivery_unit_category           IS NOT INITIAL AND
       lr_dlvy_unit->hec_inf_provider_guid                IS NOT INITIAL AND
       lr_dlvy_unit->hec_inf_provider_category            IS NOT INITIAL.

      " Get effort building block GUID
      SELECT SINGLE hec_timebased_effort_bb_guid
        FROM /hec1/i_managservbasetbbbbasic
       WHERE hec_apm_guid                = @lr_landscape->hec_apm_guid               AND
             hec_delivery_unit_cat_value = @lr_dlvy_unit->hec_delivery_unit_category AND
             hec_inf_provider_cat_value  = @lr_dlvy_unit->hec_inf_provider_category  AND
             hec_mat_oper_mode_value     = @lr_landscape->hec_material_opmode_value
        INTO @DATA(lv_effort_bb_guid).


      LOOP AT lt_man_serv_baseline REFERENCE INTO DATA(lr_man_serv_baseline).
        IF lv_effort_bb_guid IS NOT INITIAL.
          lr_man_serv_baseline->price = /hec1/cl_config_helper=>do_price_validation( iv_node_key          = is_ctx-node_key
                                                                                     it_key               = it_key
                                                                                     io_read              = io_read
                                                                                     iv_effort_bb_guid    = lv_effort_bb_guid
                                                                                     iv_tier_is_dr_node   = abap_false
                                                                                     iv_dr_operating_mode = ''                 ).

          INSERT VALUE #( data        = lr_man_serv_baseline
                          node        = /hec1/if_configuration_c=>sc_node-managed_service_baseline
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_man_serv_baseline->key                                   ) INTO TABLE lt_modification.

        ENDIF. " IF lv_effort_bb_guid IS NOT INITIAL.
      ENDLOOP.
    ENDIF. " IF lr_dlvy_unit->hec_delivery_unit IS NOT INITIAL AND...


    "-----------------------------------
    " Update instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message) ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_phase.

    DATA: lt_phase        TYPE /hec1/t_data_phase_ct,
          lt_phase_all    TYPE /hec1/t_data_phase_ct,
          lt_root         TYPE /hec1/t_config_root_ct,
          lt_modification TYPE /bobf/t_frw_modification.

    FIELD-SYMBOLS: <fs_param> TYPE /hec1/t_act_update_phase.

    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_param>.

    CHECK <fs_param> IS ASSIGNED.

    io_read->retrieve( EXPORTING iv_node    = is_ctx-node_key
                                 it_key     = it_key
                       IMPORTING et_data    = lt_phase ).

    io_read->get_root_key( EXPORTING iv_node       = is_ctx-node_key
                                     it_key        = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).

    io_read->retrieve( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-root
                                 it_key     = lt_root_key
                       IMPORTING et_data    = lt_root ).

    TRY.
        DATA(ls_root) = lt_root[ 1 ]. "There is only ever one root
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = VALUE #( FOR wa IN lt_phase
                                                                        ( key = wa-parent_key ) )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                      IMPORTING et_data        = lt_phase_all ).

    LOOP AT lt_phase REFERENCE INTO DATA(lr_phase).

      "-----------------------------------
      " Clear Successor Phasing
      "   This is done when the successor
      "   is deleted. Then the "successor"-
      "   field needs to be cleared on the
      "   predecessor.
      "-----------------------------------
      IF line_exists( <fs_param>[ do_clear_phasing = abap_true
                                  key              = lr_phase->key ] ).

        TRY.
            DATA(ls_phase_all) = lt_phase_all[ hec_node_phase = lr_phase->hec_phase_successor_guid ].

          CATCH cx_sy_itab_line_not_found.
            CLEAR: lr_phase->hec_phase_successor_guid,
                   lr_phase->hec_phase_successor_descr.
        ENDTRY.

        INSERT VALUE #( data        = lr_phase
                        node        = /hec1/if_configuration_c=>sc_node-phase
                        change_mode = /bobf/if_frw_c=>sc_modify_update
                        key         = lr_phase->key                           ) INTO TABLE lt_modification.
      ENDIF. "do_clear_phasing

      "-----------------------------------
      "  Update Predecessor
      "    This is done when a successor
      "    is created.
      "-----------------------------------
      IF line_exists( <fs_param>[ do_update_predecessor = abap_true
                                  key                   = lr_phase->key ] ).

        TRY.
            DATA(lr_phase_pred) = NEW /hec1/s_data_phase_cs( lt_phase_all[ key = lr_phase->hec_phase_predecessor_guid ] ).
            lr_phase_pred->hec_phase_successor_guid = lr_phase->key.
            lr_phase_pred->hec_update_from_general  = abap_true.

            INSERT VALUE #( data        = lr_phase_pred
                            node        = /hec1/if_configuration_c=>sc_node-phase
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_phase_pred->key                      ) INTO TABLE lt_modification.

          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

      ENDIF. "do_update_predecessor

      "-----------------------------------
      "  Update Phasing Duration Unit
      "-----------------------------------
      IF line_exists( <fs_param>[ do_update_duration_unit = abap_true
                                  key                     = lr_phase->key ] ).

        INSERT VALUE #( data        = NEW #( BASE lr_phase->*
                                             hec_update_from_general = abap_true
                                             hec_duration_unit       = ls_root-hec_ls_contract_dur_unit_value )
                        node        = /hec1/if_configuration_c=>sc_node-phase
                        change_mode = /bobf/if_frw_c=>sc_modify_update
                        key         = lr_phase->key                                                       ) INTO TABLE lt_modification.

      ENDIF.

      "-----------------------------------
      "  Update Default Start and End date
      "-----------------------------------
      IF line_exists( <fs_param>[ do_update_def_start_end = abap_true
                                  key                     = lr_phase->key ] ).

        "if phase dates are not filled yet
        IF lr_phase->hec_phase_start_date IS INITIAL AND lr_phase->hec_phase_end_date IS INITIAL.

          INSERT VALUE #( data        = NEW #( BASE lr_phase->*
                                               hec_update_from_general = abap_true
                                               hec_phase_start_date    = ls_root-hec_contract_start_date
                                               hec_phase_end_date      = ls_root-hec_contract_end_date )
                          node        = /hec1/if_configuration_c=>sc_node-phase
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_phase->key                           ) INTO TABLE lt_modification.

        ENDIF.
      ENDIF.
    ENDLOOP.

    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_solution.

    DATA: lt_solution     TYPE /hec1/t_data_solution_ct,
          lt_tier         TYPE /hec1/t_data_tier_ct,
          lt_modification TYPE /bobf/t_frw_modification.



    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                  it_key = it_key
                       IMPORTING et_data = lt_solution      ).


    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                      IMPORTING et_data        = lt_tier                                                ).


    LOOP AT lt_solution REFERENCE INTO DATA(lr_solution).

      " Update Number of Tiers
      lr_solution->hec_tier_qty_nprod_level = 0.
      lr_solution->hec_tier_qty_prod_level = 0.

      LOOP AT lt_tier ASSIGNING FIELD-SYMBOL(<fs_tier>)
        WHERE parent_key = lr_solution->key.
        IF <fs_tier>-hec_tier_cat_value = /hec1/if_config_constants=>gc_tier_category-nonprod.
          ADD 1 TO lr_solution->hec_tier_qty_nprod_level .
        ELSE.
          ADD 1 TO lr_solution->hec_tier_qty_prod_level .
        ENDIF.
      ENDLOOP.

      INSERT VALUE #( data        = lr_solution
                      node        = /hec1/if_configuration_c=>sc_node-solution
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_solution->key                           ) INTO TABLE lt_modification.

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


  METHOD /hec1/if_config_action_intern~update_storage_backup_price.

    DATA: lt_landscape    TYPE /hec1/t_config_root_ct,
          lt_dlvy_unit    TYPE /hec1/t_data_dlvy_unit_ct,
          lt_datacenter   TYPE /hec1/t_data_datacenter_ct,
          lt_solution     TYPE /hec1/t_data_solution_ct,
          lt_tier         TYPE /hec1/t_data_tier_ct,
          lt_db_si        TYPE /hec1/t_data_db_server_inst_ct,
          lt_db_inst      TYPE /hec1/t_data_db_inst_ct,
          lt_db_node      TYPE /hec1/t_data_db_node_ct,
          lt_db_serv_pc   TYPE /hec1/t_data_db_serv_pc_ct,
          lt_app_si       TYPE /hec1/t_data_app_serv_inst_ct,
          lt_app_node     TYPE /hec1/t_data_app_node_ct,
          lt_app_serv_pc  TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_backup   TYPE /hec1/t_data_app_backup_ct,
          lt_app_server   TYPE /hec1/t_data_app_serv_ct,
          lt_app_storage  TYPE /hec1/t_data_app_storage_ct,
          lt_db_backup    TYPE /hec1/t_data_db_backup_ct,
          lt_db_server    TYPE /hec1/t_data_db_serv_ct,
          lt_db_storage   TYPE /hec1/t_data_db_storage_ct,
          lt_modification TYPE /bobf/t_frw_modification,
          ls_pricing      TYPE /hec1/s_costbased_pricing_lb.

    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_create_db_backup.



    CLEAR: eo_message,
           et_failed_key.

    IF eo_message IS NOT BOUND.
      eo_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    io_read->get_root_key( EXPORTING iv_node = is_ctx-node_key
                                     it_key  = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).

    "landscape
    io_read->retrieve( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                 it_key         = lt_root_key
                       IMPORTING et_data        = lt_landscape ).

    "delivery unit
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = lt_root_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-delivery_unit
                                      IMPORTING et_target_key  = DATA(lt_dlvy_unit_key)
                                                et_data        = lt_dlvy_unit ).

    "datacenter
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-delivery_unit
                                                it_key         = lt_dlvy_unit_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-delivery_unit-datacenter
                                      IMPORTING et_target_key  = DATA(lt_datacenter_key)
                                                et_data        = lt_datacenter ).


    "solution
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = lt_root_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-solution
                                      IMPORTING et_target_key  = DATA(lt_solution_key)
                                                et_data        = lt_solution ).

    "tier
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-solution
                                                it_key         = lt_solution_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                      IMPORTING et_target_key  = DATA(lt_tier_key)
                                                et_data        = lt_tier ).

    "db server instance
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                it_key         = lt_tier_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier-db_server_instance
                                      IMPORTING et_target_key  = DATA(lt_db_si_key)
                                                et_data        = lt_db_si ).

    "db inst
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                it_key         = lt_db_si_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-instance_db
                                      IMPORTING et_target_key  = DATA(lt_db_inst_key)
                                                et_data        = lt_db_inst ).

    "db node
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-instance_db
                                                it_key         = lt_db_inst_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-db_node
                                      IMPORTING et_target_key  = DATA(lt_db_node_key)
                                                et_data        = lt_db_node ).

    "db serv pc
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_node
                                                it_key         = lt_db_node_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                                      IMPORTING et_target_key  = DATA(lt_db_serv_pc_key)
                                                et_data        = lt_db_serv_pc ).

    "db server
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                it_key         = lt_db_serv_pc_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_server
                                      IMPORTING et_target_key  = DATA(lt_db_server_key)
                                                et_data        = lt_db_server ).

    "db storage
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server
                                                it_key         = lt_db_server_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server-db_storage
                                      IMPORTING et_target_key  = DATA(lt_db_storage_key)
                                                et_data        = lt_db_storage ).

    "db backup
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_storage
                                                it_key         = lt_db_storage_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_storage-db_storage_backup
                                      IMPORTING et_target_key  = DATA(lt_db_backup_key)
                                                et_data        = lt_db_backup ).
    "app server instance
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                it_key         = lt_tier_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier-app_server_instance
                                      IMPORTING et_target_key  = DATA(lt_app_si_key)
                                                et_data        = lt_app_si ).

    "app node
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                it_key         = lt_app_si_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-app_node
                                      IMPORTING et_target_key  = DATA(lt_app_node_key)
                                                et_data        = lt_app_node ).

    "app serv pc
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
                                                it_key         = lt_app_node_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
                                      IMPORTING et_target_key  = DATA(lt_app_serv_pc_key)
                                                et_data        = lt_app_serv_pc ).

    "app server
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                it_key         = lt_app_serv_pc_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_server
                                      IMPORTING et_target_key  = DATA(lt_app_server_key)
                                                et_data        = lt_app_server ).

    "app storage
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server
                                                it_key         = lt_app_server_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server-app_storage
                                      IMPORTING et_target_key  = DATA(lt_app_storage_key)
                                                et_data        = lt_app_storage ).

    "app backup
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_storage
                                                it_key         = lt_app_storage_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_storage-app_storage_backup
                                      IMPORTING et_target_key  = DATA(lt_app_backup_key)
                                                et_data        = lt_app_backup ).

    " Update all app storage backup over all solutions
    LOOP AT lt_app_backup REFERENCE INTO DATA(lr_app_backup)
      WHERE hec_backup_class_guid IS NOT INITIAL AND
            price                 IS INITIAL.           "#EC CI_SORTSEQ

      "-----------------------------------
      " Get Storage Backup Price
      "-----------------------------------
      """""""""""""""""" TODO: MOve to different method
      TRY.
          DATA(ls_tier) = lt_tier[ hec_node_tier = lr_app_backup->hec_node_tier ]. " Here I use the alternate key because it's faster
          DATA(ls_landscape) = lt_landscape[ root_key = lr_app_backup->root_key ]. "should we process multiple configurations at this point, the root key is the only way to keep different landscapes apart
          DATA(ls_dlvy_unit) = lt_dlvy_unit[ root_key = lr_app_backup->root_key ].
          DATA(ls_app_server) = lt_app_server[ hec_node_app_server = lr_app_backup->hec_node_app_server ]. " Here I use the alternate key because it's faster
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.

*        " Try first to get data center from server
*        DATA(lv_datacenter) = ls_app_server-hec_sec_datacenter_guid. " Here I use the alternate key because it's faster
*
*        " If there is no data center, try to get data center from tier
*        IF lv_datacenter IS INITIAL.
*          TRY.
*              lv_datacenter = lt_datacenter[ hec_node_datacenter = ls_tier-hec_tier_datacenter_guid ]-hec_datacenter_guid.
*            CATCH cx_sy_itab_line_not_found.
*          ENDTRY.
*        ENDIF.

      " Get storage backup pricing
      /hec1/cl_config_action_helper=>/hec1/if_bopf_action_helper~get_backup_class_and_price( EXPORTING is_ctx                  = CORRESPONDING #( is_ctx )
                                                                                                       it_key                  = VALUE #( ( key = lr_app_backup->key ) )
                                                                                                       iv_app_server           = abap_true
                                                                                                       iv_tier_category_value  = lr_app_backup->hec_tier_cat_value
                                                                                                       iv_tier_datacenter_guid = lr_app_backup->hec_tier_datacenter_guid
                                                                                                       io_read                 = io_read
                                                                                             IMPORTING es_backup_class         = DATA(ls_backup_class)
                                                                                                       es_backup_pricing       = DATA(ls_backup_pricing)                   ).


      lr_app_backup->price = ls_backup_pricing.

*      " Get DT backup class data
*      DATA(lt_fdt_backup_class) = /hec1/cl_config_fdt_provider=>get_instance( )->/hec1/if_config_fdt_provider~get_storage_backup_class( iv_apm_guid          = ls_landscape-hec_apm_guid
*                                                                                                                                        iv_db_serv_type_guid = space
*                                                                                                                                        iv_server_inst_type  = |02|
*                                                                                                                                        iv_tier_category     = ls_tier-hec_tier_cat_value ).
*
*      " Get default backup class data
*      TRY.
*          DATA(ls_backup_class) = lt_fdt_backup_class[ hec_backup_class_default = abap_true ].
*        CATCH cx_sy_itab_line_not_found.
*      ENDTRY.
*
*      " Get backup pricing
*      IF ls_backup_class-hec_backup_class_guid IS NOT INITIAL.
*
*
*
*        DATA(lv_lb_guid) = /hec1/cl_config_fdt_provider=>get_instance( )->/hec1/if_config_fdt_provider~get_storage_backup_pricing_lb( iv_apm_guid          = ls_landscape-hec_apm_guid
*                                                                                                                                      iv_backup_class_guid = ls_backup_class-hec_backup_class_guid
*                                                                                                                                      iv_datacenter_guid   = lv_datacenter
*                                                                                                                                      iv_inf_provider_guid = ls_dlvy_unit-hec_inf_provider_guid ).
*
*        IF lv_lb_guid IS NOT INITIAL.
*          SELECT SINGLE * FROM /hec1/c_cbp_lb "#EC CI_ALL_FIELDS_NEEDED
*            WHERE hec_price_lb = @lv_lb_guid
*             INTO CORRESPONDING FIELDS OF @lr_app_backup->price.
*
*        ENDIF.
*      ENDIF. " IF ls_fdt_backup_class-hec_backup_class_guid IS NOT INITIAL.
*      """" End of "Move to different method"

      " Add Backup to Update table
      INSERT VALUE #( data        = lr_app_backup
                      node        = /hec1/if_configuration_c=>sc_node-app_storage_backup
                      source_node = /hec1/if_configuration_c=>sc_node-app_storage_backup
                      source_key  = lr_app_backup->key
                      change_mode = /bobf/if_frw_c=>sc_modify
                      key         = lr_app_backup->key
                      ) INTO TABLE lt_modification.

    ENDLOOP.

    " Update all DB storage backup over all solutions
    LOOP AT lt_db_backup REFERENCE INTO DATA(lr_db_backup)
      WHERE hec_backup_class_guid IS NOT INITIAL AND
            price                 IS INITIAL.           "#EC CI_SORTSEQ

      "-----------------------------------
      " Get Storage Backup Price
      "-----------------------------------
      """""""""""""""""" TODO: MOve to different method
      TRY.
          ls_tier = lt_tier[ hec_node_tier = lr_db_backup->hec_node_tier ]. " Here I use the alternate key because it's faster
          ls_landscape = lt_landscape[ root_key = lr_db_backup->root_key ]. "should we process multiple configurations at this point, the root key is the only way to keep different landscapes apart
          ls_dlvy_unit = lt_dlvy_unit[ root_key = lr_db_backup->root_key ].
          DATA(ls_solution) = lt_solution[ hec_node_solution = lr_db_backup->hec_node_solution ].
          DATA(ls_db_server) = lt_db_server[ hec_node_db_server = lr_db_backup->hec_node_db_server ]. " Here I use the alternate key because it's faster
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.

*      " Get storage backup pricing
*      /hec1/cl_config_action_helper=>/hec1/if_bopf_action_helper~get_backup_class_and_price( EXPORTING is_ctx                  = CORRESPONDING #( is_ctx )
*                                                                                                       it_key                  = VALUE #( ( key = lr_db_backup->key ) )
*                                                                                                       iv_tier_category_guid   = lr_db_backup->hec_tier_cat_value
*                                                                                                       iv_tier_datacenter_guid = lr_db_backup->hec_tier_datacenter_guid
*                                                                                                       io_read                 = io_read
*                                                                                             IMPORTING es_backup_class         = ls_backup_class
*                                                                                                       es_backup_pricing       = ls_backup_pricing                        ).


      lr_db_backup->price = ls_backup_pricing.

*      " Get DT backup class data
*      lt_fdt_backup_class = /hec1/cl_config_fdt_provider=>get_instance( )->/hec1/if_config_fdt_provider~get_storage_backup_class( iv_apm_guid          = ls_landscape-hec_apm_guid
*                                                                                                                                  iv_db_serv_type_guid = ''"ls_solution-hec_db_srv_type_guid
*                                                                                                                                  iv_server_inst_type  = |01|
*                                                                                                                                  iv_tier_category     = ls_tier-hec_tier_cat_value ).
*
*      " Get default backup class data
*      TRY.
*          ls_backup_class = lt_fdt_backup_class[ hec_backup_class_default = abap_true ].
*        CATCH cx_sy_itab_line_not_found.
*      ENDTRY.
*
*      " Get backup pricing
*      IF ls_backup_class-hec_backup_class_guid IS NOT INITIAL.
*
*        " Try first to get data center from server
*        lv_datacenter = ls_db_server-hec_datacenter_guid. " Here I use the alternate key because it's faster
*
*        " If there is no data center, try to get data center from tier
*        IF lv_datacenter IS INITIAL.
*          TRY.
*              lv_datacenter = lt_datacenter[ hec_node_datacenter = ls_tier-hec_tier_datacenter_guid ]-hec_datacenter_guid.
*            CATCH cx_sy_itab_line_not_found.
*          ENDTRY.
*        ENDIF.
*
*        lv_lb_guid = /hec1/cl_config_fdt_provider=>get_instance( )->/hec1/if_config_fdt_provider~get_storage_backup_pricing_lb( iv_apm_guid          = ls_landscape-hec_apm_guid
*                                                                                                                                iv_backup_class_guid = ls_backup_class-hec_backup_class_guid
*                                                                                                                                iv_datacenter_guid   = lv_datacenter
*                                                                                                                                iv_inf_provider_guid = ls_dlvy_unit-hec_inf_provider_guid ).
*
*        IF lv_lb_guid IS NOT INITIAL.
*          SELECT SINGLE * FROM /hec1/c_cbp_lb "#EC CI_ALL_FIELDS_NEEDED
*            WHERE hec_price_lb = @lv_lb_guid
*             INTO CORRESPONDING FIELDS OF @lr_db_backup->price.
*
*        ENDIF.
*      ENDIF. " IF ls_fdt_backup_class-hec_backup_class_guid IS NOT INITIAL.
*      """" End of "Move to different method"

      " Add Backup to Update table
      INSERT VALUE #( data        = lr_db_backup
                      node        = /hec1/if_configuration_c=>sc_node-db_storage_backup
                      source_node = /hec1/if_configuration_c=>sc_node-db_storage_backup
                      source_key  = lr_db_backup->key
                      change_mode = /bobf/if_frw_c=>sc_modify
                      key         = lr_db_backup->key                                    ) INTO TABLE lt_modification.

    ENDLOOP.

    "-----------------------------------
    " Modify instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_tier.

    DATA: lt_solution         TYPE /hec1/t_data_solution_ct,
          lt_tier             TYPE /hec1/t_data_tier_ct,
          lt_db_serv_inst     TYPE /hec1/t_data_db_server_inst_ct,
          lt_app_serv_inst    TYPE /hec1/t_data_app_serv_inst_ct,
          lt_material         TYPE /hec1/t_data_material_ct,
          lt_software_item    TYPE /hec1/t_data_sw_item_ct,
          lt_parameter        TYPE /hec1/t_act_update_tier,
          lt_modification     TYPE /bobf/t_frw_modification,
          lt_act_param_delete TYPE /bobf/t_frw_node.


    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO FIELD-SYMBOL(<fs_parameter>).
    IF <fs_parameter> IS ASSIGNED.
      lt_parameter = <fs_parameter>.
    ENDIF.

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape) ).

    io_read->retrieve( EXPORTING iv_node    = is_ctx-node_key
                                 it_key     = it_key
                       IMPORTING et_data    = lt_tier ).

    " Solution
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier-to_parent
                                      IMPORTING et_data        = lt_solution  ).

    " DB Server Instance
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier-db_server_instance
                                      IMPORTING et_data        = lt_db_serv_inst  ).

    " App Server Instance
    io_read->retrieve_by_association( EXPORTING iv_node         = is_ctx-node_key
                                                it_key          = it_key
                                                iv_fill_data    = abap_true
                                                iv_association  = /hec1/if_configuration_c=>sc_association-tier-app_server_instance
                                      IMPORTING et_data         = lt_app_serv_inst ).

    " Get Materials
    io_read->retrieve_by_association( EXPORTING iv_node         = is_ctx-node_key
                                                it_key          = it_key
                                                iv_fill_data    = abap_true
                                                iv_association  = /hec1/if_configuration_c=>sc_association-tier-material
                                      IMPORTING et_data         = lt_material
                                                et_target_key   = DATA(lt_material_key) ).

    " Get Software Items
    io_read->retrieve_by_association( EXPORTING iv_node         = /hec1/if_configuration_c=>sc_node-material
                                                it_key          = lt_material_key
                                                iv_fill_data    = abap_true
                                                iv_association  = /hec1/if_configuration_c=>sc_association-material-software_item
                                      IMPORTING et_data         = lt_software_item ).

    " Get Material List
    DATA(lt_material_list) = /hec1/cl_config_sw_helper=>get_instance( )->/hec1/if_config_sw_helper~get_material_list( ).
    " Get Software Item List
    DATA(lt_software_item_list) = /hec1/cl_config_sw_helper=>get_instance( )->/hec1/if_config_sw_helper~get_software_item_list( ).

    " own tier
    LOOP AT lt_tier REFERENCE INTO DATA(lr_tier).

      TRY.
          DATA(ls_parameter) = lt_parameter[ key = lr_tier->key ].

          "-----------------------------------
          " Update Server Instance Quantities
          "-----------------------------------
          IF ls_parameter-do_update_qty = abap_true.

            lr_tier->hec_app_srv_qty = lines( VALUE /hec1/t_data_app_serv_inst_ct( FOR app_si IN lt_app_serv_inst
                                                                                   WHERE ( parent_key = lr_tier->key AND
                                                                                           hec_srv_inst_rel_value = '01' )
                                                                                         ( app_si ) ) ).

            lr_tier->hec_app_srv_qty_opt = lines( VALUE /hec1/t_data_app_serv_inst_ct( FOR app_si IN lt_app_serv_inst
                                                                                       WHERE ( parent_key = lr_tier->key AND
                                                                                               hec_srv_inst_rel_value = '02' )
                                                                                             ( app_si ) ) ).

            lr_tier->hec_db_srv_qty = lines( VALUE /hec1/t_data_db_server_inst_ct( FOR db_si IN lt_db_serv_inst
                                                                                    WHERE ( parent_key = lr_tier->key AND
                                                                                            hec_db_srv_type_value = '01' )
                                                                                          ( db_si ) ) ).

            lr_tier->hec_db_srv_qty_opt = lines( VALUE /hec1/t_data_db_server_inst_ct( FOR db_si IN lt_db_serv_inst
                                                                                    WHERE ( parent_key = lr_tier->key AND
                                                                                            hec_db_srv_type_value = '02' )
                                                                                          ( db_si ) ) ).

          ENDIF. "do_update_qty

          "-----------------------------------
          " Update language
          "-----------------------------------
          IF ls_parameter-do_update_language = abap_true.

            TRY.
                DATA(ls_solution) = lt_solution[ key = lr_tier->parent_key ].

                lr_tier->hec_tier_language_sys_alt = ls_solution-hec_sol_language_sys_alt.
                lr_tier->hec_tier_language_sys_def = ls_solution-hec_sol_language_sys_def.
                lr_tier->hec_tier_language_list    = ls_solution-hec_sol_language_list.

              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

          ENDIF. " IF ls_parameter-do_update_language = abap_true.

          "-----------------------------------
          " Update Business Function
          "-----------------------------------
          IF ls_parameter-do_update_bf_activation = abap_true.

            TRY.
                ls_solution = lt_solution[ key = lr_tier->parent_key ].

                lr_tier->hec_bf_activation = ls_solution-hec_bf_activation.

              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

          ENDIF. "          IF ls_parameter-do_update_bf_activation = abap_true.

          IF ls_parameter-do_update_bf_tmpl_sent_to_cust = abap_true.

            TRY.
                ls_solution = lt_solution[ key = lr_tier->parent_key ].

                lr_tier->hec_bpacti_tmpl_sent_to_cust = ls_solution-hec_bpacti_tmpl_sent_to_cust.

              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

          ENDIF.  "          IF ls_parameter-do_update_bf_tmpl_sent_to_cust = abap_true.

          IF ls_parameter-do_update_bf_tmpl_upl_by_cust = abap_true.

            TRY.
                ls_solution = lt_solution[ key = lr_tier->parent_key ].

                lr_tier->hec_bpacti_tmpl_upl_by_cust = ls_solution-hec_bpacti_tmpl_upl_by_cust.

              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

          ENDIF. "          IF ls_parameter-do_update_bf_tmpl_upl_by_cust = abap_true.

          IF ls_parameter-do_update_db_version = abap_true.

            TRY.
                ls_solution = lt_solution[ key = lr_tier->parent_key ].

                lr_tier->hec_db_version_guid = ls_solution-hec_sol_db_version_guid.
                lr_tier->hec_db_version_descr = ls_solution-hec_sol_db_version_descr.
                lr_tier->hec_db_version_value = ls_solution-hec_sol_db_version_value.

              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

          ENDIF. "          IF ls_parameter-do_update_bf_tmpl_upl_by_cust = abap_true.

          IF ls_parameter-do_update_impl_type = abap_true.

            TRY.
                ls_solution = lt_solution[ key = lr_tier->parent_key ].

                lr_tier->hec_tier_impl_type_value = ls_solution-hec_sol_impl_type_value.
                lr_tier->hec_tier_impl_type_descr = ls_solution-hec_sol_impl_type_descr.
                lr_tier->hec_tier_impl_type_vlqt = ls_solution-hec_sol_impl_type_vlqt.

              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

          ENDIF. " IF ls_parameter-do_update_language = abap_true.

          "-----------------------------------
          " Insert Tier data to modification table
          "-----------------------------------
          INSERT VALUE #( data        = lr_tier
                          node        = /hec1/if_configuration_c=>sc_node-tier
                          source_node = /hec1/if_configuration_c=>sc_node-solution
                          association = /hec1/if_configuration_c=>sc_association-solution-tier
                          source_key  = lr_tier->parent_key
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_tier->key
                          ) INTO TABLE lt_modification.

        CATCH cx_sy_itab_line_not_found.
      ENDTRY.

    ENDLOOP.

    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD constructor.

    me->mo_instance = me.

  ENDMETHOD.


  METHOD get_instance.

    ro_instance = COND #( WHEN mo_instance IS BOUND
                          THEN mo_instance
                          ELSE NEW /hec1/cl_config_action_intern( ) ).


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~copy_node.
*    "disable determinations on create
*    /hec1/cl_lib_d_superclass=>set_switch( abap_false ).
*
*    TRY.
*
*        NEW /hec1/cl_copy_controller_(
*          iv_bo_key         = is_ctx-bo_key
*          io_read           = io_read
*          io_modify         = io_modify
*          iv_node_key       = is_ctx-node_key
*          it_key            = it_key
*          iv_adopt_alt_keys = abap_true
*        )->copy( ).
*
*      CATCH /hec1/cx_copy_control.
*    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_app_node.

    DATA: lt_app_server_inst TYPE /hec1/t_data_app_serv_inst_ct,
          lt_solution        TYPE /hec1/t_data_solution_ct,
          lt_tier            TYPE /hec1/t_data_tier_ct,
          lt_modification    TYPE /bobf/t_frw_modification,
          ls_landscape       TYPE /hec1/s_config_root_cs.

    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_create_app_node.


    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_act_param>.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_server_inst ).


    "-----------------------------------
    " Get APM model GUID and description
    "-----------------------------------
    /hec1/cl_config_helper=>get_apm_model( EXPORTING iv_node_key   = is_ctx-node_key
                                                     it_key        = it_key
                                                     io_read       = io_read
                                           IMPORTING et_failed_key = et_failed_key
                                                     es_apm_model  = ls_landscape ).

    "-----------------------------------
    " Get App server cluster node type
    "-----------------------------------
    DATA(lt_range_table) = VALUE /hec1/t_selection_range( FOR wa IN lt_app_server_inst
                                                        ( option = /hec1/if_config_constants=>gc_range_option-eq
                                                          sign   = /hec1/if_config_constants=>gc_range_sign-i
                                                          low    = wa-hec_app_serv_type_clust_guid            )   ).

    SELECT *
      FROM /hec1/i_appclustnodetypebasic
     WHERE hec_apm_guid                 = @ls_landscape-hec_apm_guid AND
           hec_app_serv_type_clust_guid IN @lt_range_table
      INTO TABLE @DATA(lt_cluster_node_type).


    "-----------------------------------
    " Fill App server node data
    "-----------------------------------
    LOOP AT lt_app_server_inst ASSIGNING FIELD-SYMBOL(<fs_app_serv_inst>).
      ASSIGN <fs_act_param>[ key = <fs_app_serv_inst>-key ] TO FIELD-SYMBOL(<fs_param>).

      IF <fs_act_param> IS ASSIGNED.
        " Get correct cluster node type
        TRY.
            DATA(ls_cluster_node_type) = lt_cluster_node_type[ hec_app_serv_type_clust_guid  = <fs_app_serv_inst>-hec_app_serv_type_clust_guid
                                                               hec_app_clust_node_type_value = SWITCH #( <fs_param>-hec_app_cluster_type_value
                                                                                                         WHEN /hec1/if_config_constants=>gc_app_clust_node-none
                                                                                                         THEN /hec1/if_config_constants=>gc_app_clust_node_type-master
                                                                                                         ELSE /hec1/if_config_constants=>gc_app_clust_node_type-standby ) ].
          CATCH cx_sy_itab_line_not_found.
            ls_cluster_node_type-hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master.
            ls_cluster_node_type-hec_app_clust_node_type_descr = 'Master'.
        ENDTRY.

        DATA(lr_app_node) = NEW /hec1/s_data_app_node_cs( parent_key                     = <fs_app_serv_inst>-key
                                                          key                            = /bopf/cl_frw_factory=>get_new_key( )
                                                          hec_node_solution              = <fs_app_serv_inst>-hec_node_solution
                                                          hec_node_tier                  = <fs_app_serv_inst>-hec_node_tier
                                                          hec_node_app_serv_inst         = <fs_app_serv_inst>-hec_node_app_serv_inst
                                                          hec_node_app_node              = /rbp/cl_general_utilities=>get_new_guid22( )
                                                          hec_comp_config_id             = ls_landscape-hec_confid
                                                          hec_comp_config_version        = ls_landscape-hec_conf_version
                                                          inh                            = <fs_app_serv_inst>-inh
                                                          hec_server_required            = <fs_app_serv_inst>-hec_server_required
                                                          hec_effort_required            = <fs_app_serv_inst>-hec_effort_required
                                                          hec_backup_relev_value         = <fs_app_serv_inst>-hec_backup_relev_value
                                                          hec_backup_relev_descr         = <fs_app_serv_inst>-hec_backup_relev_descr
                                                          hec_master_default             = SWITCH #( <fs_param>-hec_app_cluster_type_value
                                                                                                     WHEN /hec1/if_config_constants=>gc_app_clust_node-none
                                                                                                     THEN abap_true
                                                                                                     ELSE abap_false                                        )
                                                          hec_apm_guid                   = ls_landscape-hec_apm_guid
                                                          hec_apm_descr                  = ls_landscape-hec_apm_descr
                                                          hec_apst_clustty_clustnty_guid = ls_cluster_node_type-hec_apst_clustty_clustnty_guid
                                                          hec_default_app_server_inst    = <fs_app_serv_inst>-hec_default_app_server_inst
                                                          hec_sol_apsi_clusttyp_guid     = <fs_app_serv_inst>-hec_sol_apsi_clusttyp_guid
                                                          hec_app_cluster_type_value     = <fs_param>-hec_app_cluster_type_value
                                                          hec_app_clust_node_type_guid   = ls_cluster_node_type-hec_app_clust_node_type_guid
                                                          hec_app_clust_node_type_value  = ls_cluster_node_type-hec_app_clust_node_type_value
                                                          hec_app_clust_node_type_descr  = ls_cluster_node_type-hec_app_clust_node_type_descr
*                                                          hec_app_clust_relation_guid     = iv_clust_relation_guid
                                                          hec_app_srv_perf_cat_qty       = COND #( WHEN ls_cluster_node_type-hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master
                                                                                                   THEN 1
                                                                                                   ELSE 0                                                                                                               )
                                                          hec_phase_guid                 = COND #( WHEN ls_cluster_node_type-hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master
                                                                                                   THEN <fs_app_serv_inst>-hec_phase_guid )
                                                          hec_phase_assign_allowed       = COND #( WHEN ls_cluster_node_type-hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master
                                                                                                   THEN abap_false
                                                                                                   ELSE abap_true )
                                                          hec_tree_descr                 = ls_cluster_node_type-hec_app_clust_node_type_descr
                                                          crea_uname          = sy-uname ).

        GET TIME STAMP FIELD lr_app_node->crea_date_time.

        INSERT VALUE #( data        = lr_app_node
                        node        = /hec1/if_configuration_c=>sc_node-app_node
                        source_node = /hec1/if_configuration_c=>sc_node-app_server_instance
                        association = /hec1/if_configuration_c=>sc_association-app_server_instance-app_node
                        source_key  = <fs_app_serv_inst>-key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = lr_app_node->key                                                       ) INTO TABLE lt_modification.

      ENDIF. " IF <fs_act_param> IS ASSIGNED.

      CLEAR: ls_cluster_node_type,
             lr_app_node.
    ENDLOOP.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change) ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_app_server.

    DATA: lt_app_serv_perf_cat TYPE /hec1/t_data_app_serv_pc_ct,
          lt_solution          TYPE /hec1/t_data_solution_ct,
          lt_tier              TYPE /hec1/t_data_tier_ct,
          lt_modification      TYPE /bobf/t_frw_modification.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_serv_perf_cat ).


    "-----------------------------------
    " Get APM model GUID and description
    " delivery unit and data centers
    "-----------------------------------
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key       ).

    "-----------------------------------
    " Fill App server data
    "-----------------------------------
    LOOP AT lt_app_serv_perf_cat ASSIGNING FIELD-SYMBOL(<fs_app_serv_perf_cat>).
      DATA(lr_app_server) = NEW /hec1/s_data_app_serv_cs( parent_key               = <fs_app_serv_perf_cat>-parent_key
                                                          key                      = /bopf/cl_frw_factory=>get_new_key( )
                                                          hec_node_solution        = <fs_app_serv_perf_cat>-hec_node_solution
                                                          hec_node_tier            = <fs_app_serv_perf_cat>-hec_node_tier
                                                          hec_node_app_serv_inst   = <fs_app_serv_perf_cat>-hec_node_app_serv_inst
                                                          hec_node_app_node        = <fs_app_serv_perf_cat>-hec_node_app_node
                                                          hec_node_app_serv_pc     = <fs_app_serv_perf_cat>-hec_node_app_serv_pc
                                                          hec_node_app_server      = /rbp/cl_general_utilities=>get_new_guid22( )
                                                          hec_comp_config_id       = lr_landscape->hec_confid
                                                          hec_comp_config_version  = lr_landscape->hec_conf_version
                                                          inh                      = <fs_app_serv_perf_cat>-inh
                                                          hec_apm_guid             = lr_landscape->hec_apm_guid
                                                          hec_apm_descr            = lr_landscape->hec_apm_descr
                                                          hec_phase_fixed          = abap_true
                                                          hec_phase_assign_allowed = abap_false
                                                          hec_phase_guid           = <fs_app_serv_perf_cat>-hec_phase_guid
                                                          crea_uname               = sy-uname ).

      GET TIME STAMP FIELD lr_app_server->crea_date_time.

      INSERT VALUE #( data        = lr_app_server
                      node        = /hec1/if_configuration_c=>sc_node-app_server
                      source_node = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                      association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_server
                      source_key  = <fs_app_serv_perf_cat>-key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = lr_app_server->key                                                          ) INTO TABLE lt_modification.

      CLEAR lr_app_server.
    ENDLOOP.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_app_server_pc.

    DATA: lt_app_node     TYPE /hec1/t_data_app_node_ct,
          lt_solution     TYPE /hec1/t_data_solution_ct,
          lt_app_serv_pc  TYPE /hec1/t_data_app_serv_pc_ct,
          lt_modification TYPE /bobf/t_frw_modification.


    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_create_app_spc.


    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_act_param>.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_node     ).

    " all server performance categories need to clear the phasing for previous nodes
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
                                      IMPORTING et_data        = lt_app_serv_pc ).

    "-----------------------------------
    " Get APM model GUID and description
    " delivery unit and data centers
    "-----------------------------------
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lr_datacenter)
                                                        et_failed_key    = et_failed_key       ).

    "-----------------------------------
    " Fill App server performance
    " category data
    "-----------------------------------
    LOOP AT lt_app_node ASSIGNING FIELD-SYMBOL(<fs_app_node>).
      ASSIGN <fs_act_param>[ key = <fs_app_node>-key ] TO FIELD-SYMBOL(<fs_param>).

      IF <fs_param> IS ASSIGNED.
        DO <fs_param>-hec_app_srv_perf_cat_qty TIMES.
          DATA(lr_app_serv_perf_cat) = NEW /hec1/s_data_app_serv_pc_cs( parent_key                    = <fs_app_node>-key
                                                                        key                           = /bopf/cl_frw_factory=>get_new_key( )
                                                                        hec_node_solution             = <fs_app_node>-hec_node_solution
                                                                        hec_node_tier                 = <fs_app_node>-hec_node_tier
                                                                        hec_node_app_serv_inst        = <fs_app_node>-hec_node_app_serv_inst
                                                                        hec_node_app_node             = <fs_app_node>-hec_node_app_node
                                                                        hec_node_app_serv_pc          = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                        hec_comp_config_id            = lr_landscape->hec_confid
                                                                        hec_comp_config_version       = lr_landscape->hec_conf_version
                                                                        hec_apm_guid                  = lr_landscape->hec_apm_guid
                                                                        hec_apm_descr                 = lr_landscape->hec_apm_descr
                                                                        inh                           = <fs_app_node>-inh
*                                                                        hec_app_cluster_type_value    = <fs_app_node>-hec_app_cluster_type_value
                                                                        hec_apst_clustty_clustnty_guid = <fs_app_node>-hec_apst_clustty_clustnty_guid
                                                                        hec_app_clust_node_type_value = <fs_app_node>-hec_app_clust_node_type_value
                                                                        hec_app_node_default          = <fs_app_node>-hec_master_default
                                                                        hec_server_qty                = 1
                                                                        hec_storage_qty               = 1
                                                                        hec_phase_guid                = COND #( WHEN 1 = <fs_app_node>-hec_app_srv_perf_cat_qty
                                                                                                                THEN <fs_app_node>-hec_phase_guid
                                                                                                                ELSE space )
                                                                        hec_phase_fixed               = COND #( WHEN 1 = <fs_app_node>-hec_app_srv_perf_cat_qty
                                                                                                                THEN abap_true
                                                                                                                ELSE abap_false )
                                                                        hec_phase_assign_allowed      = abap_false
                                                                        crea_uname                    = sy-uname ).

          GET TIME STAMP FIELD lr_app_serv_perf_cat->crea_date_time.

          INSERT VALUE #( data        = lr_app_serv_perf_cat
                          node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                          source_node = /hec1/if_configuration_c=>sc_node-app_node
                          association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
                          source_key  = <fs_app_node>-key
                          change_mode = /bobf/if_frw_c=>sc_modify_create
                          key         = lr_app_serv_perf_cat->key                                                 ) INTO TABLE lt_modification.

          CLEAR lr_app_serv_perf_cat.
        ENDDO.

        "-----------------------------------
        " Clear phasing for previously last
        " object in successor/predecessor chain
        "-----------------------------------
        TRY.
            lr_app_serv_perf_cat = NEW /hec1/s_data_app_serv_pc_cs( lt_app_serv_pc[ parent_key = <fs_app_node>-key
                                                                                    hec_has_successor = abap_false ] ).

            lr_app_serv_perf_cat->hec_phase_assign_allowed = COND #( WHEN lr_app_serv_perf_cat->hec_phase_guid IS NOT INITIAL
                                                                      AND lr_app_serv_perf_cat->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master
                                                                     THEN abap_true
                                                                     ELSE abap_false ).

            CLEAR: lr_app_serv_perf_cat->hec_phase_guid,
                   lr_app_serv_perf_cat->hec_phase_changed.

            lr_app_serv_perf_cat->hec_phase_assign_allowed = abap_true.

            INSERT VALUE #( data        = lr_app_serv_perf_cat
                            node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_app_serv_perf_cat->key    ) INTO TABLE lt_modification.

          CATCH cx_sy_itab_line_not_found.
        ENDTRY.
      ENDIF. " IF <fs_act_param> IS ASSIGNED.

      UNASSIGN <fs_param>.
    ENDLOOP.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_app_storage.

    DATA: lt_app_server      TYPE /hec1/t_data_app_serv_ct,
          lt_app_storage_qty TYPE /hec1/t_data_app_storageqty_ct,
          lt_app_storage     TYPE /hec1/t_data_app_storage_ct,
          lt_modification    TYPE /bobf/t_frw_modification.

    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_create_app_storage.

    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_act_param>.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_server   ).

    "-----------------------------------
    " Get APM model GUID and description
    " delivery unit and data centers
    "-----------------------------------
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lr_datacenter)
                                                        et_failed_key    = et_failed_key       ).

    "-----------------------------------
    " Get App storage amount data
    "-----------------------------------
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server-to_app_storage_amount
                                      IMPORTING et_target_key  = DATA(lt_storage_qty_key)
                                                et_failed_key  = et_failed_key                                                              ).


    IF lt_storage_qty_key IS NOT INITIAL.
      io_read->retrieve( EXPORTING iv_node = /hec1/if_configuration_c=>sc_node-app_storage_amount
                                   it_key  = lt_storage_qty_key
                         IMPORTING et_data = lt_app_storage_qty                                   ).
    ENDIF.

    "-----------------------------------
    " Get all existing App storages
    " for the given App server
    "-----------------------------------
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server-app_storage
                                      IMPORTING et_data        = lt_app_storage
                                                et_failed_key  = et_failed_key                                                   ).


    "-----------------------------------
    " Fill App server storage data
    "-----------------------------------
    LOOP AT lt_app_server ASSIGNING FIELD-SYMBOL(<fs_app_server>).

      LOOP AT lt_app_storage_qty ASSIGNING FIELD-SYMBOL(<fs_storage_qty>)
        WHERE hec_node_solution      = <fs_app_server>-hec_node_solution      AND
              hec_node_tier          = <fs_app_server>-hec_node_tier          AND
              hec_node_app_serv_inst = <fs_app_server>-hec_node_app_serv_inst AND
              hec_node_app_node      = <fs_app_server>-hec_node_app_node      AND
              hec_node_app_serv_pc   = <fs_app_server>-hec_node_app_serv_pc.

        IF line_exists( lt_app_storage[ hec_node_solution            = <fs_storage_qty>-hec_node_solution
                                        hec_node_tier                = <fs_storage_qty>-hec_node_tier
                                        hec_node_app_serv_inst       = <fs_storage_qty>-hec_node_app_serv_inst
                                        hec_node_app_node            = <fs_storage_qty>-hec_node_app_node
                                        hec_node_app_serv_pc         = <fs_storage_qty>-hec_node_app_serv_pc
                                        hec_storage_qty_ref_guid     = <fs_storage_qty>-hec_node_app_storage_qty ] ).
          CONTINUE. " >>>>>>>
        ENDIF.

        IF <fs_act_param> IS ASSIGNED.
          ASSIGN <fs_act_param>[ key = <fs_app_server>-key ]-hec_pricing_included TO FIELD-SYMBOL(<fs_pricing_included>).

          IF <fs_pricing_included> IS ASSIGNED.
            " Get pricing for app server storage
            IF <fs_pricing_included> = abap_true.

              TRY.
                  DATA(lv_datacenter_guid) = lr_datacenter[ hec_node_datacenter = <fs_app_server>-hec_tier_datacenter_guid ]-hec_datacenter_guid.

                  " Get storage data
                  SELECT *
                    FROM /hec1/i_storagelbbasic
                   WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid          AND
                         hec_sec_datacenter_guid = @lv_datacenter_guid                  AND
                         hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid
                    INTO TABLE @DATA(lt_storage).

                  IF lines( lt_storage ) = 1.
                    DATA(ls_storage) = lt_storage[ 1 ].

                    SELECT SINGLE * FROM /hec1/c_cbp_lb "#EC CI_ALL_FIELDS_NEEDED
                       INTO @DATA(ls_pricing)
                      WHERE hec_price_lb = @ls_storage-hec_cb_pricing_lb_guid.

                  ENDIF.
                CATCH cx_sy_itab_line_not_found.
              ENDTRY.
            ENDIF. " IF <fs_pricing_included> = abap_true.
          ENDIF. " IF <fs_pricing_included> IS ASSIGNED.
        ENDIF. " IF <fs_act_param> is assigned.

        DATA(lr_app_storage) = NEW /hec1/s_data_app_storage_cs( parent_key                   = <fs_app_server>-parent_key
                                                                key                          = /bopf/cl_frw_factory=>get_new_key( )
                                                                hec_node_solution            = <fs_app_server>-hec_node_solution
                                                                hec_node_tier                = <fs_app_server>-hec_node_tier
                                                                hec_node_app_serv_inst       = <fs_app_server>-hec_node_app_serv_inst
                                                                hec_node_app_node            = <fs_app_server>-hec_node_app_node
                                                                hec_node_app_serv_pc         = <fs_app_server>-hec_node_app_serv_pc
                                                                hec_node_app_server          = <fs_app_server>-hec_node_app_server
                                                                hec_node_app_storage         = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                hec_storage_qty_ref_guid     = <fs_storage_qty>-hec_node_app_storage_qty
                                                                hec_comp_config_id           = lr_landscape->hec_confid
                                                                hec_comp_config_version      = lr_landscape->hec_conf_version
                                                                inh                          = <fs_app_server>-inh
                                                                hec_apm_guid                 = lr_landscape->hec_apm_guid
                                                                hec_apm_descr                = lr_landscape->hec_apm_descr
                                                                hec_storage_quantity         = COND #( WHEN <fs_app_server>-hec_srv_main_storage_qty IS NOT INITIAL
                                                                                                       THEN <fs_app_server>-hec_srv_main_storage_qty      +
                                                                                                            <fs_storage_qty>-hec_asq_additional_stor_qty
                                                                                                       ELSE COND #( WHEN <fs_app_server>-hec_host_type_value = /hec1/if_config_constants=>gc_server_host_type-virtual
                                                                                                                    THEN <fs_storage_qty>-hec_asq_main_stor_qty_virtual +
                                                                                                                         <fs_storage_qty>-hec_asq_additional_stor_qty
                                                                                                                    ELSE  <fs_storage_qty>-hec_asq_main_stor_qty_virtual +
                                                                                                                          <fs_storage_qty>-hec_asq_additional_stor_qty ) )
                                                                hec_ip_storage_guid           = COND #( WHEN ls_storage-hec_ip_storage_guid IS NOT INITIAL
                                                                                                        THEN ls_storage-hec_ip_storage_guid
                                                                                                        ELSE space                                         )
                                                                hec_storage_descr             = COND #( WHEN ls_storage-hec_storage_descr IS NOT INITIAL
                                                                                                        THEN ls_storage-hec_storage_descr
                                                                                                        ELSE space                                         )
                                                                hec_backup_qty                = SWITCH #( <fs_app_server>-hec_backup_relev_value
                                                                                                          WHEN '01'
                                                                                                          THEN 1
                                                                                                          ELSE 0                                 )
                                                                hec_phase_guid                = COND #( WHEN <fs_storage_qty>-hec_phase_guid IS NOT INITIAL
                                                                                                        THEN <fs_storage_qty>-hec_phase_guid
                                                                                                        ELSE space                                         )
                                                                hec_phase_fixed               = abap_true
                                                                hec_phase_assign_allowed      = abap_false
                                                                hec_tree_descr                = COND #( WHEN ls_storage-hec_storage_descr IS INITIAL
                                                                                                        THEN space
                                                                                                        ELSE ls_storage-hec_storage_descr                   )
                                                                crea_uname                    = sy-uname ).

        GET TIME STAMP FIELD lr_app_storage->crea_date_time.

        INSERT VALUE #( data        = lr_app_storage
                        node        = /hec1/if_configuration_c=>sc_node-app_storage
                        source_node = /hec1/if_configuration_c=>sc_node-app_server
                        association = /hec1/if_configuration_c=>sc_association-app_server-app_storage
                        source_key  = <fs_app_server>-key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = lr_app_storage->key                                              ) INTO TABLE lt_modification.


        CLEAR: lv_datacenter_guid,
               ls_pricing,
               lt_storage,
               lr_app_storage.

        UNASSIGN <fs_pricing_included>.
      ENDLOOP.
    ENDLOOP.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_app_storage_amount.

    DATA: lt_app_serv_perf_cat   TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_storage_qty_all TYPE /hec1/t_data_app_storageqty_ct,
          lt_modification        TYPE /bobf/t_frw_modification,
          ls_landscape           TYPE /hec1/s_config_root_cs.

    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_create_app_qty.


    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_act_param>.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_serv_perf_cat ).

    "-----------------------------------
    " Get APM model GUID and description
    "-----------------------------------
    /hec1/cl_config_helper=>get_apm_model( EXPORTING iv_node_key   = is_ctx-node_key
                                                     it_key        = it_key
                                                     io_read       = io_read
                                           IMPORTING et_failed_key = et_failed_key
                                                     es_apm_model  = ls_landscape    ).

    "-----------------------------------
    " Get App Storage Amounts
    "-----------------------------------
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_storage_amount
                                      IMPORTING et_data        = lt_app_storage_qty_all ).

    "-----------------------------------
    " Fill App storage amount data
    "-----------------------------------
    LOOP AT lt_app_serv_perf_cat ASSIGNING FIELD-SYMBOL(<fs_app_serv_perf_cat>).
      ASSIGN <fs_act_param>[ key = <fs_app_serv_perf_cat>-key ] TO FIELD-SYMBOL(<fs_param>).

      IF <fs_param> IS ASSIGNED.
        DO <fs_param>-hec_storage_amount_qty TIMES.
          DATA(lr_app_storage_qty) = NEW /hec1/s_data_app_storageqty_cs( parent_key                    = <fs_app_serv_perf_cat>-key
                                                                         key                           = /bopf/cl_frw_factory=>get_new_key( )
                                                                         hec_node_solution             = <fs_app_serv_perf_cat>-hec_node_solution
                                                                         hec_node_tier                 = <fs_app_serv_perf_cat>-hec_node_tier
                                                                         hec_node_app_serv_inst        = <fs_app_serv_perf_cat>-hec_node_app_serv_inst
                                                                         hec_node_app_node             = <fs_app_serv_perf_cat>-hec_node_app_node
                                                                         hec_node_app_serv_pc          = <fs_app_serv_perf_cat>-hec_node_app_serv_pc
                                                                         hec_node_app_storage_qty      = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                         hec_comp_config_id            = ls_landscape-hec_confid
                                                                         hec_comp_config_version       = ls_landscape-hec_conf_version
                                                                         inh                           = <fs_app_serv_perf_cat>-inh
                                                                         hec_apm_guid                  = ls_landscape-hec_apm_guid
                                                                         hec_apm_descr                 = ls_landscape-hec_apm_descr
                                                                         hec_tree_descr                = |0 + 0[GiB]|
                                                                         hec_phase_guid                = COND #( WHEN <fs_app_serv_perf_cat>-hec_storage_qty = 1
                                                                                                                 THEN <fs_app_serv_perf_cat>-hec_phase_guid )
                                                                         hec_phase_fixed               = COND #( WHEN <fs_app_serv_perf_cat>-hec_storage_qty = 1
                                                                                                                 THEN abap_true
                                                                                                                 ELSE abap_false )
                                                                         hec_phase_assign_allowed      = abap_false
                                                                         crea_uname                    = sy-uname ).

          GET TIME STAMP FIELD lr_app_storage_qty->crea_date_time.

          INSERT VALUE #( data        = lr_app_storage_qty
                          node        = /hec1/if_configuration_c=>sc_node-app_storage_amount
                          source_node = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                          association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_storage_amount
                          source_key  = <fs_app_serv_perf_cat>-key
                          change_mode = /bobf/if_frw_c=>sc_modify_create
                          key         = lr_app_storage_qty->key                                                             ) INTO TABLE lt_modification.

          CLEAR lr_app_storage_qty.
        ENDDO.

        "-----------------------------------
        " Clear phasing for previously last
        " object in successor/predecessor chain
        "-----------------------------------
        TRY.
            DATA(lr_app_storage_qty_pred) = NEW /hec1/s_data_app_storageqty_cs( lt_app_storage_qty_all[ parent_key        = <fs_app_serv_perf_cat>-key
                                                                                                        hec_has_successor = abap_false ] ).

            lr_app_storage_qty_pred->hec_phase_assign_allowed = COND #( WHEN lr_app_storage_qty_pred->hec_phase_guid IS NOT INITIAL
                                                                         AND lr_app_storage_qty->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master
                                                                        THEN abap_true
                                                                        ELSE abap_false ).

            CLEAR: lr_app_storage_qty_pred->hec_phase_guid,
                   lr_app_storage_qty_pred->hec_phase_changed.

            lr_app_storage_qty_pred->hec_phase_fixed = abap_false.

            INSERT VALUE #( data        = lr_app_storage_qty_pred
                            node        = /hec1/if_configuration_c=>sc_node-app_storage_amount
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_app_storage_qty_pred->key    ) INTO TABLE lt_modification.

          CATCH cx_sy_itab_line_not_found.
        ENDTRY.


      ENDIF. " IF <fs_param> IS ASSIGNED.

      UNASSIGN <fs_param>.
    ENDLOOP.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_app_storage_backup.

    DATA: lt_app_storage  TYPE /hec1/t_data_app_storage_ct,
          ls_landscape    TYPE /hec1/s_config_root_cs,
          lt_app_backup   TYPE /hec1/t_data_app_backup_ct,
          lt_modification TYPE /bobf/t_frw_modification.

    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_create_app_backup.


    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_act_param>.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_storage   ).

    " all server performance categories need to clear the phasing for previous nodes
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_storage-app_storage_backup
                                      IMPORTING et_data        = lt_app_backup ).

    "-----------------------------------
    " Get APM model GUID and description
    "-----------------------------------
    /hec1/cl_config_helper=>get_apm_model( EXPORTING iv_node_key   = is_ctx-node_key
                                                     it_key        = it_key
                                                     io_read       = io_read
                                           IMPORTING et_failed_key = et_failed_key
                                                     es_apm_model  = ls_landscape    ).

    "-----------------------------------
    " Fill App storage backup data
    "-----------------------------------
    LOOP AT lt_app_storage ASSIGNING FIELD-SYMBOL(<fs_app_storage>).
      ASSIGN <fs_act_param>[ key = <fs_app_storage>-key ] TO FIELD-SYMBOL(<fs_param>).

      IF <fs_param> IS ASSIGNED.
        DO <fs_param>-hec_backup_qty TIMES.

          " Get storage backup pricing
          /hec1/cl_config_action_helper=>/hec1/if_bopf_action_helper~get_backup_class_and_price( EXPORTING is_ctx                  = CORRESPONDING #( is_ctx )
                                                                                                           it_key                  = VALUE #( ( key = <fs_app_storage>-key ) )
                                                                                                           iv_app_server           = abap_true
                                                                                                           iv_tier_category_value  = <fs_app_storage>-hec_tier_cat_value
                                                                                                           iv_tier_datacenter_guid = <fs_app_storage>-hec_tier_datacenter_guid
                                                                                                           io_read                 = io_read
                                                                                                 IMPORTING es_backup_class         = DATA(ls_backup_class)
                                                                                                           es_backup_pricing       = DATA(ls_backup_pricing)                   ).


          DATA(lr_app_backup) = NEW /hec1/s_data_app_backup_cs( parent_key               = <fs_app_storage>-parent_key
                                                                key                      = /bopf/cl_frw_factory=>get_new_key( )
                                                                hec_node_solution        = <fs_app_storage>-hec_node_solution
                                                                hec_node_tier            = <fs_app_storage>-hec_node_tier
                                                                hec_node_app_serv_inst   = <fs_app_storage>-hec_node_app_serv_inst
                                                                hec_node_app_node        = <fs_app_storage>-hec_node_app_node
                                                                hec_node_app_serv_pc     = <fs_app_storage>-hec_node_app_serv_pc
                                                                hec_node_app_server      = <fs_app_storage>-hec_node_app_server
                                                                hec_node_app_storage     = <fs_app_storage>-hec_node_app_storage
                                                                hec_node_app_backup      = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                hec_comp_config_id       = ls_landscape-hec_confid
                                                                hec_comp_config_version  = ls_landscape-hec_conf_version
                                                                inh                      = <fs_app_storage>-inh
                                                                hec_apm_guid             = ls_landscape-hec_apm_guid
                                                                hec_apm_descr            = ls_landscape-hec_apm_descr
                                                                hec_backup_class_guid    = ls_backup_class-hec_backup_class_guid
                                                                hec_backup_class_descr   = ls_backup_class-hec_backup_class_descr
                                                                hec_tree_descr           = ls_backup_class-hec_backup_class_descr
                                                                price                    = ls_backup_pricing
                                                                hec_phase_guid           = COND #( WHEN <fs_app_storage>-hec_backup_qty = 1
                                                                                                   THEN <fs_app_storage>-hec_phase_guid
                                                                                                   ELSE space )
                                                                hec_phase_fixed          = COND #( WHEN <fs_app_storage>-hec_backup_qty = 1
                                                                                                   THEN abap_true
                                                                                                   ELSE abap_false )
                                                                hec_phase_assign_allowed = abap_false
                                                                crea_uname               = sy-uname                                            ).

          GET TIME STAMP FIELD lr_app_backup->crea_date_time.


          INSERT VALUE #( data        = lr_app_backup
                          node        = /hec1/if_configuration_c=>sc_node-app_storage_backup
                          source_node = /hec1/if_configuration_c=>sc_node-app_storage
                          association = /hec1/if_configuration_c=>sc_association-app_storage-app_storage_backup
                          source_key  = <fs_app_storage>-key
                          change_mode = /bobf/if_frw_c=>sc_modify_create
                          key         = lr_app_backup->key                                                      ) INTO TABLE lt_modification.


          CLEAR: ls_backup_class,
                 ls_backup_pricing,
                 lr_app_backup.
        ENDDO.

        "-----------------------------------
        " Clear phasing for previously last
        " object in successor/predecessor chain
        "-----------------------------------
        TRY.
            lr_app_backup = NEW /hec1/s_data_app_backup_cs( lt_app_backup[ parent_key = <fs_app_storage>-key
                                                                           hec_has_successor = abap_false ] ).

            lr_app_backup->hec_phase_assign_allowed = COND #( WHEN lr_app_backup->hec_phase_guid IS NOT INITIAL
                                                               AND lr_app_backup->hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master
                                                              THEN abap_true
                                                              ELSE abap_false ).

            CLEAR: lr_app_backup->hec_phase_guid,
                   lr_app_backup->hec_phase_changed.

            lr_app_backup->hec_phase_fixed = abap_false.

            INSERT VALUE #( data        = lr_app_backup
                            node        = /hec1/if_configuration_c=>sc_node-app_storage_backup
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_app_backup->key    ) INTO TABLE lt_modification.

          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

      ENDIF. "IF <fs_param> IS ASSIGNED.

      UNASSIGN <fs_param>.
    ENDLOOP.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_db_node.

    DATA: lt_instance_db  TYPE /hec1/t_data_db_inst_ct,
          lt_db_serv_inst TYPE /hec1/t_data_db_server_inst_ct,
          lt_tier         TYPE /hec1/t_data_tier_ct,
          lt_db_node      TYPE /hec1/t_data_db_node_ct,
          lt_modification TYPE /bobf/t_frw_modification,
          ls_landscape    TYPE /hec1/s_config_root_cs.

    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_create_db_node.


    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_act_param>.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_instance_db ).


    "-----------------------------------
    " Get APM model GUID and description
    "-----------------------------------
    /hec1/cl_config_helper=>get_apm_model( EXPORTING iv_node_key   = is_ctx-node_key
                                                     it_key        = it_key
                                                     io_read       = io_read
                                           IMPORTING et_failed_key = et_failed_key
                                                     es_apm_model  = ls_landscape ).

    "-----------------------------------
    " Get DB node for cluster relation
    " guid
    "-----------------------------------
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-db_node
                                      IMPORTING et_data        = lt_db_node
                                                et_failed_key  = et_failed_key ).

    "-----------------------------------
    " Get DB server cluster node type
    "-----------------------------------
    SELECT *
     FROM /hec1/i_dbclustnodetypebasic
    WHERE hec_apm_guid = @ls_landscape-hec_apm_guid
     INTO TABLE @DATA(lt_cluster_node_type).


    "-----------------------------------
    " Fill DB server node data
    "-----------------------------------
    LOOP AT lt_instance_db ASSIGNING FIELD-SYMBOL(<fs_instance_db>).
      ASSIGN <fs_act_param>[ key = <fs_instance_db>-key ] TO FIELD-SYMBOL(<fs_param>).

      IF <fs_param> IS ASSIGNED.

        IF <fs_param>-hec_def_master_node = abap_true.
          " Create cluster relation guid
          DATA(lv_clust_relation_guid) = /rbp/cl_general_utilities=>get_new_guid22( ).
        ELSE.
          " Get cluster relation guid from default master node
          lv_clust_relation_guid = lt_db_node[ parent_key                   = <fs_instance_db>-key "#EC CI_SORTSEQ
                                               hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master
                                               hec_master_default           = abap_true                                               ]-hec_db_clust_relation_guid.
        ENDIF.

        DO <fs_param>-hec_db_node_qty TIMES.
          " Get DB server cluster node type
          TRY.
              DATA(ls_cluster_node_type) = lt_cluster_node_type[ hec_dbst_nodety_clust_ty_guid = <fs_instance_db>-hec_dbst_nodety_clust_ty_guid
                                                                 hec_db_clust_node_type_value  = <fs_param>-hec_cluster_node_type_value         ].
            CATCH cx_sy_itab_line_not_found.
          ENDTRY.


          IF <fs_instance_db>-hec_tier_cat_value  IS NOT INITIAL AND
             <fs_instance_db>-hec_effort_required = abap_true.

            " Get effort building block GUID
            SELECT SINGLE hec_timebased_effort_bb_guid
             FROM /hec1/i_dbservnodetbbbbasic
            WHERE hec_apm_guid                  = @ls_landscape-hec_apm_guid                          AND
                  hec_dbst_clustty_clustntyguid = @ls_cluster_node_type-hec_dbst_clustty_clustntyguid AND
                  hec_tier_cat_value            = @<fs_instance_db>-hec_tier_cat_value
             INTO @DATA(lv_effort_bb_guid).

          ENDIF.

          " Fill DB server node data
          DATA(lr_db_node) = NEW /hec1/s_data_db_node_cs( parent_key                    = <fs_instance_db>-key
                                                          key                           = /bopf/cl_frw_factory=>get_new_key( )
                                                          hec_node_solution             = <fs_instance_db>-hec_node_solution
                                                          hec_node_tier                 = <fs_instance_db>-hec_node_tier
                                                          hec_node_db_serv_inst         = <fs_instance_db>-hec_node_db_serv_inst
                                                          hec_node_db_inst              = <fs_instance_db>-hec_node_db_inst
                                                          hec_node_db_node              = /rbp/cl_general_utilities=>get_new_guid22( )
                                                          hec_comp_config_id            = ls_landscape-hec_confid
                                                          hec_comp_config_version       = ls_landscape-hec_conf_version
                                                          inh                           = <fs_instance_db>-inh
                                                          hec_dbst_nodety_clust_ty_guid = <fs_instance_db>-hec_dbst_nodety_clust_ty_guid
                                                          hec_apm_guid                  = ls_landscape-hec_apm_guid
                                                          hec_apm_descr                 = ls_landscape-hec_apm_descr
                                                          hec_db_node_type_value        = <fs_instance_db>-hec_db_node_type_value
                                                          hec_db_cluster_type_value     = <fs_instance_db>-hec_db_cluster_type_value
                                                          hec_master_default            = <fs_param>-hec_def_master_node
                                                          hec_db_clust_relation_guid    = lv_clust_relation_guid
                                                          hec_dbst_clustty_clustntyguid = ls_cluster_node_type-hec_dbst_clustty_clustntyguid
                                                          hec_db_clust_node_type_value  = ls_cluster_node_type-hec_db_clust_node_type_value
                                                          hec_db_clust_node_type_descr  = ls_cluster_node_type-hec_db_clust_node_type_descr
                                                          hec_gen_parallel_file_sys     = ls_cluster_node_type-hec_gen_parallel_file_sys
                                                          hec_calc_setup_dr             = ls_cluster_node_type-hec_calc_setup_dr
                                                          hec_db_srv_perf_cat_qty       = SWITCH #( ls_cluster_node_type-hec_db_clust_node_type_value
                                                                                                    WHEN /hec1/if_config_constants=>gc_db_clust_node_type-master
                                                                                                    THEN 1
                                                                                                    ELSE 0                                                       )
                                                          price                         = /hec1/cl_config_helper=>do_price_validation( iv_node_key          = is_ctx-node_key
                                                                                                                                       it_key               = it_key
                                                                                                                                       io_read              = io_read
                                                                                                                                       iv_effort_bb_guid    = lv_effort_bb_guid
                                                                                                                                       iv_tier_is_dr_node   = <fs_instance_db>-hec_tier_is_dr_node
                                                                                                                                       iv_dr_operating_mode = <fs_instance_db>-hec_dr_oper_mode_value )
                                                          hec_phase_fixed               = COND #( WHEN ls_cluster_node_type-hec_db_clust_node_type_value =  /hec1/if_config_constants=>gc_db_clust_node_type-master
                                                                                                  THEN abap_true
                                                                                                  ELSE abap_false )
                                                          hec_phase_guid                = COND #( WHEN ls_cluster_node_type-hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master
                                                                                                  THEN <fs_instance_db>-hec_phase_guid
                                                                                                  ELSE space )
                                                          hec_phase_assign_allowed      = COND #( WHEN ls_cluster_node_type-hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master
                                                                                                  THEN abap_false
                                                                                                  ELSE abap_true )
                                                          hec_tree_descr                = ls_cluster_node_type-hec_db_clust_node_type_descr
                                                          crea_uname                    = sy-uname ).

          GET TIME STAMP FIELD lr_db_node->crea_date_time.

          INSERT VALUE #( data        = lr_db_node
                          node        = /hec1/if_configuration_c=>sc_node-db_node
                          source_node = /hec1/if_configuration_c=>sc_node-instance_db
                          association = /hec1/if_configuration_c=>sc_association-instance_db-db_node
                          source_key  = <fs_instance_db>-key
                          change_mode = /bobf/if_frw_c=>sc_modify_create
                          key         = lr_db_node->key                                               ) INTO TABLE lt_modification.

          CLEAR: lv_effort_bb_guid,
                 ls_cluster_node_type,
                 lr_db_node.

        ENDDO.
      ENDIF. " IF <fs_param> IS ASSIGNED.

      CLEAR lv_clust_relation_guid.
      UNASSIGN <fs_param>.
    ENDLOOP.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change) ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_db_server.

    DATA: lt_db_serv_perf_cat TYPE /hec1/t_data_db_serv_pc_ct,
          lt_solution         TYPE /hec1/t_data_solution_ct,
          lt_tier             TYPE /hec1/t_data_tier_ct,
          lt_modification     TYPE /bobf/t_frw_modification.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_serv_perf_cat ).


    "-----------------------------------
    " Get APM model GUID and description
    " delivery unit and data centers
    "-----------------------------------
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key       ).

    "-----------------------------------
    " Get tier for assigned data center
    "-----------------------------------
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-instance_db
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)
                                                et_key_link    = DATA(lt_key_link)
                                                et_failed_key  = et_failed_key                                                  ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                it_key         = lt_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-to_parent
                                      IMPORTING et_data        = lt_tier
                                                et_key_link    = DATA(lt_tier_key_link)
                                                et_failed_key  = et_failed_key                                                         ).

    "-----------------------------------
    " Get DB server data
    "-----------------------------------
    DATA(lt_range_table) = VALUE /hec1/t_selection_range( FOR wa_spc IN lt_db_serv_perf_cat
                                                        ( option = /hec1/if_config_constants=>gc_range_option-eq
                                                          sign   = /hec1/if_config_constants=>gc_range_sign-i
                                                          low    = wa_spc-hec_srv_perf_cat_guid                   ) ).

    SELECT *                                  "#EC CI_ALL_FIELDS_NEEDED
      FROM /hec1/i_serverbasic
     WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid          AND
           hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid AND
           hec_srv_perf_cat_guid   IN @lt_range_table
      INTO TABLE @DATA(lt_server_data).


    "-----------------------------------
    " Fill DB server data
    "-----------------------------------
    LOOP AT lt_db_serv_perf_cat ASSIGNING FIELD-SYMBOL(<fs_db_serv_perf_cat>).
      " Get assigned data center from tier
      TRY.
          DATA(lv_db_serv_inst_key)    = lt_key_link[ source_key = <fs_db_serv_perf_cat>-parent_key ]-target_key.
          DATA(lv_assigned_datacenter) = lt_tier[ key = lt_tier_key_link[ source_key = lv_db_serv_inst_key ]-target_key ]-hec_tier_datacenter_guid.
          DATA(lv_datacenter_guid)     = lt_datacenter[ hec_node_datacenter = lv_assigned_datacenter ]-hec_datacenter_guid.

          DATA(lt_server)  = VALUE /hec1/t_apm_server( FOR wa IN lt_server_data
                                                       WHERE ( hec_sec_datacenter_guid = lv_datacenter_guid                          AND
                                                               hec_srv_perf_cat_guid   = <fs_db_serv_perf_cat>-hec_srv_perf_cat_guid     )
                                                       ( CORRESPONDING #( wa ) )                                                           ).

          " Get DB server and pricing
          IF lines( lt_server ) = 1.
            TRY.
                DATA(ls_server) = lt_server[ 1 ].
                SELECT SINGLE hec_cb_pricing_lb_guid
                  FROM /hec1/i_serverlbbasic
                 WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid        AND
                       hec_sec_datacenter_guid = @ls_server-hec_sec_datacenter_guid AND
                       hec_infra_provider_guid = @ls_server-hec_infra_provider_guid AND
                       hec_ip_server_guid      = @ls_server-hec_ip_server_guid
                  INTO @DATA(lv_lb_guid).

                SELECT SINGLE * FROM /hec1/c_cbp_lb "#EC CI_ALL_FIELDS_NEEDED
                   INTO @DATA(ls_pricing)
                  WHERE hec_price_lb = @lv_lb_guid.

              CATCH cx_sy_itab_line_not_found.
            ENDTRY.
          ENDIF.
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.


      DATA(lr_db_server) = NEW /hec1/s_data_db_serv_cs( parent_key               = <fs_db_serv_perf_cat>-parent_key
                                                        key                      = /bopf/cl_frw_factory=>get_new_key( )
                                                        hec_node_solution        = <fs_db_serv_perf_cat>-hec_node_solution
                                                        hec_node_tier            = <fs_db_serv_perf_cat>-hec_node_tier
                                                        hec_node_db_serv_inst    = <fs_db_serv_perf_cat>-hec_node_db_serv_inst
                                                        hec_node_db_inst         = <fs_db_serv_perf_cat>-hec_node_db_inst
                                                        hec_node_db_node         = <fs_db_serv_perf_cat>-hec_node_db_node
                                                        hec_node_db_serv_pc      = <fs_db_serv_perf_cat>-hec_node_db_serv_pc
                                                        hec_node_db_server       = /rbp/cl_general_utilities=>get_new_guid22( )
                                                        hec_comp_config_id       = lr_landscape->hec_confid
                                                        hec_comp_config_version  = lr_landscape->hec_conf_version
                                                        inh                      = <fs_db_serv_perf_cat>-inh
                                                        hec_apm_guid             = lr_landscape->hec_apm_guid
                                                        hec_apm_descr            = lr_landscape->hec_apm_descr
                                                        hec_ip_server_guid       = ls_server-hec_ip_server_guid
                                                        hec_ip_server_descr      = ls_server-hec_ip_server_descr
                                                        hec_host_type_value      = ls_server-hec_srv_host_type_value
                                                        hec_host_type_descr      = ls_server-hec_srv_host_type_descr
                                                        hec_ram_size             = ls_server-hec_srv_ram_size
                                                        hec_cpu_size             = ls_server-hec_srv_cpu_size
                                                        hec_srv_main_stor_qty    = ls_server-hec_srv_main_storage_qty
                                                        hec_saps                 = ls_server-hec_saps
                                                        hec_srv_flavour          = ls_server-hec_srv_flavour
                                                        hec_approval_needed      = ls_server-hec_approval_needed
                                                        price                    = CORRESPONDING #( ls_pricing )
                                                        hec_phase_guid           = <fs_db_serv_perf_cat>-hec_phase_guid
                                                        hec_phase_fixed          = abap_true
                                                        hec_phase_assign_allowed = abap_false
                                                        hec_tree_descr           = COND #( WHEN ls_server-hec_ip_server_descr IS INITIAL
                                                                                           THEN space
                                                                                           ELSE ls_server-hec_ip_server_descr            )
                                                        crea_uname                    = sy-uname ).

      GET TIME STAMP FIELD lr_db_server->crea_date_time.

      INSERT VALUE #( data        = lr_db_server
                      node        = /hec1/if_configuration_c=>sc_node-db_server
                      source_node = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                      association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_server
                      source_key  = <fs_db_serv_perf_cat>-key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = lr_db_server->key                                                         ) INTO TABLE lt_modification.

      CLEAR: lv_datacenter_guid,
             lv_assigned_datacenter,
             lv_db_serv_inst_key,
             lv_lb_guid,
             ls_pricing,
             ls_server,
             lt_server,
             lr_db_server.

    ENDLOOP.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_db_server_pc.

    DATA: lt_db_node      TYPE /hec1/t_data_db_node_ct,
          lt_solution     TYPE /hec1/t_data_solution_ct,
          lt_db_serv_pc   TYPE /hec1/t_data_db_serv_pc_ct,
          lt_modification TYPE /bobf/t_frw_modification.


    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_create_db_spc.


    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_act_param>.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_node      ).

    "-----------------------------------
    " All server performance categories
    " need to clear the phasing for
    " previous nodes
    "-----------------------------------
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                                      IMPORTING et_data        = lt_db_serv_pc                                                          ).

    "-----------------------------------
    " Get APM model GUID and description
    " delivery unit and data centers
    "-----------------------------------
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lr_datacenter)
                                                        et_failed_key    = et_failed_key       ).

    "-----------------------------------
    " Fill DB server performance
    " category data
    "-----------------------------------
    LOOP AT lt_db_node ASSIGNING FIELD-SYMBOL(<fs_db_node>).
      ASSIGN <fs_act_param>[ key = <fs_db_node>-key ] TO FIELD-SYMBOL(<fs_param>).

      IF <fs_param> IS ASSIGNED.
        DO <fs_param>-hec_db_srv_perf_cat_qty TIMES.
          DATA(lr_db_serv_perf_cat) = NEW /hec1/s_data_db_serv_pc_cs( parent_key                    = <fs_db_node>-key
                                                                      key                           = /bopf/cl_frw_factory=>get_new_key( )
                                                                      hec_node_solution             = <fs_db_node>-hec_node_solution
                                                                      hec_node_tier                 = <fs_db_node>-hec_node_tier
                                                                      hec_node_db_serv_inst         = <fs_db_node>-hec_node_db_serv_inst
                                                                      hec_node_db_inst              = <fs_db_node>-hec_node_db_inst
                                                                      hec_node_db_node              = <fs_db_node>-hec_node_db_node
                                                                      hec_node_db_serv_pc           = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                      hec_comp_config_id            = lr_landscape->hec_confid
                                                                      hec_comp_config_version       = lr_landscape->hec_conf_version
                                                                      inh                           = <fs_db_node>-inh
                                                                      hec_dbst_clustty_clustntyguid = <fs_db_node>-hec_dbst_clustty_clustntyguid
                                                                      hec_db_clust_node_type_value  = <fs_db_node>-hec_db_clust_node_type_value
                                                                      hec_db_node_default           = <fs_db_node>-hec_master_default
                                                                      hec_apm_guid                  = lr_landscape->hec_apm_guid
                                                                      hec_apm_descr                 = lr_landscape->hec_apm_descr
                                                                      hec_server_qty                = SWITCH #( <fs_db_node>-hec_db_node_type_value
                                                                                                                 WHEN /hec1/if_config_constants=>gc_db_node_type-tenant
                                                                                                                 THEN 0
                                                                                                                 ELSE 1                                                 )
                                                                      hec_storage_qty               = SWITCH #( <fs_db_node>-hec_db_node_type_value
                                                                                                                WHEN /hec1/if_config_constants=>gc_db_node_type-tenant
                                                                                                                THEN 0
                                                                                                                ELSE 1                                                  )
                                                                      hec_phase_guid                = SWITCH #( <fs_db_node>-hec_db_srv_perf_cat_qty
                                                                                                                WHEN 1
                                                                                                                THEN <fs_db_node>-hec_phase_guid
                                                                                                                ELSE space )
                                                                      hec_phase_fixed               = SWITCH #( <fs_db_node>-hec_db_srv_perf_cat_qty
                                                                                                                WHEN 1
                                                                                                                THEN abap_true
                                                                                                                ELSE abap_false )
                                                                      hec_phase_assign_allowed      = abap_false
                                                                      crea_uname                    = sy-uname ).

          GET TIME STAMP FIELD lr_db_serv_perf_cat->crea_date_time.

          INSERT VALUE #( data        = lr_db_serv_perf_cat
                          node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                          source_node = /hec1/if_configuration_c=>sc_node-db_node
                          association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                          source_key  = <fs_db_node>-key
                          change_mode = /bobf/if_frw_c=>sc_modify_create
                          key         = lr_db_serv_perf_cat->key                                                 ) INTO TABLE lt_modification.

          CLEAR lr_db_serv_perf_cat.
        ENDDO.

        "-----------------------------------
        " Clear phasing for previously last
        " object in successor/predecessor chain
        "-----------------------------------
        TRY.
            lr_db_serv_perf_cat = NEW /hec1/s_data_db_serv_pc_cs( lt_db_serv_pc[ parent_key = <fs_db_node>-key
                                                                                 hec_has_successor = abap_false ] ).

            lr_db_serv_perf_cat->hec_phase_assign_allowed = COND #( WHEN lr_db_serv_perf_cat->hec_phase_guid IS NOT INITIAL
                                                                     AND lr_db_serv_perf_cat->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master
                                                                    THEN abap_true
                                                                    ELSE abap_false ).

            CLEAR: lr_db_serv_perf_cat->hec_phase_guid,
                   lr_db_serv_perf_cat->hec_phase_changed.

            lr_db_serv_perf_cat->hec_phase_fixed = abap_false.

            INSERT VALUE #( data        = lr_db_serv_perf_cat
                            node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                            source_node = /hec1/if_configuration_c=>sc_node-db_node
                            association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                            source_key  = <fs_db_node>-key
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_db_serv_perf_cat->key                                               ) INTO TABLE lt_modification.

          CATCH cx_sy_itab_line_not_found.
        ENDTRY.
      ENDIF. " IF <fs_act_param> IS ASSIGNED.

      UNASSIGN <fs_param>.
    ENDLOOP.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_db_storage.

    DATA: lt_db_server      TYPE /hec1/t_data_db_serv_ct,
          lt_db_storage_qty TYPE /hec1/t_data_db_storage_qty_ct,
          lt_db_storage     TYPE /hec1/t_data_db_storage_ct,
          lt_modification   TYPE /bobf/t_frw_modification.

    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_create_db_storage.


    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_act_param>.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_server   ).

    "-----------------------------------
    " Get APM model GUID and description
    " delivery unit and data centers
    "-----------------------------------
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key       ).

    "-----------------------------------
    " Get DB storage amount data
    "-----------------------------------
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)
                                                et_failed_key  = et_failed_key                                                   ).


    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                it_key         = lt_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount
                                      IMPORTING et_data        = lt_db_storage_qty
                                                et_failed_key  = et_failed_key                                                                    ).

    "-----------------------------------
    " Get all existing DB storages
    " for the given DB server
    "-----------------------------------
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server-db_storage
                                      IMPORTING et_data        = lt_db_storage
                                                et_failed_key  = et_failed_key                                                 ).


    "-----------------------------------
    " Fill DB server storage data
    "-----------------------------------
    LOOP AT lt_db_server ASSIGNING FIELD-SYMBOL(<fs_db_server>).

      LOOP AT lt_db_storage_qty ASSIGNING FIELD-SYMBOL(<fs_storage_qty>)
        WHERE hec_node_solution     = <fs_db_server>-hec_node_solution     AND
              hec_node_tier         = <fs_db_server>-hec_node_tier         AND
              hec_node_db_serv_inst = <fs_db_server>-hec_node_db_serv_inst AND
              hec_node_db_inst      = <fs_db_server>-hec_node_db_inst      AND
              hec_node_db_node      = <fs_db_server>-hec_node_db_node      AND
              hec_node_db_serv_pc   = <fs_db_server>-hec_node_db_serv_pc.

        IF line_exists( lt_db_storage[ hec_node_solution            = <fs_storage_qty>-hec_node_solution
                                       hec_node_tier                = <fs_storage_qty>-hec_node_tier
                                       hec_node_db_serv_inst        = <fs_storage_qty>-hec_node_db_serv_inst
                                       hec_node_db_inst             = <fs_storage_qty>-hec_node_db_inst
                                       hec_node_db_node             = <fs_storage_qty>-hec_node_db_node
                                       hec_node_db_serv_pc          = <fs_storage_qty>-hec_node_db_serv_pc
                                       hec_storage_qty_ref_guid = <fs_storage_qty>-hec_node_db_storage_qty ] ).
          CONTINUE. " >>>>>>>
        ENDIF.

        IF <fs_act_param> IS ASSIGNED.
          ASSIGN <fs_act_param>[ key = <fs_db_server>-key ]-hec_pricing_included TO FIELD-SYMBOL(<fs_pricing_included>).

          IF <fs_pricing_included> IS ASSIGNED.
            " Get pricing for DB server storage
            IF <fs_pricing_included> = abap_true.

              TRY.
                  DATA(lv_datacenter_guid) = lt_datacenter[ hec_node_datacenter = <fs_db_server>-hec_tier_datacenter_guid ]-hec_datacenter_guid.

                  " Get storage data
                  SELECT *
                    FROM /hec1/i_storagelbbasic
                   WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid          AND
                         hec_sec_datacenter_guid = @lv_datacenter_guid                  AND
                         hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid
                    INTO TABLE @DATA(lt_storage).


                  IF lines( lt_storage ) = 1.
                    DATA(ls_storage) = lt_storage[ 1 ].

                    SELECT SINGLE * FROM /hec1/c_cbp_lb "#EC CI_ALL_FIELDS_NEEDED
                      INTO @DATA(ls_pricing)
                     WHERE hec_price_lb = @ls_storage-hec_cb_pricing_lb_guid.

                  ENDIF.
                CATCH cx_sy_itab_line_not_found.
              ENDTRY.
            ENDIF. " IF <fs_pricing_included> = abap_true.
          ENDIF. " IF <fs_pricing_included> IS ASSIGNED.
        ENDIF. "IF <fs_act_param> is assigned.

        DATA(lr_db_storage) = NEW /hec1/s_data_db_storage_cs( parent_key                   = <fs_db_server>-parent_key
                                                              key                          = /bopf/cl_frw_factory=>get_new_key( )
                                                              hec_node_solution            = <fs_db_server>-hec_node_solution
                                                              hec_node_tier                = <fs_db_server>-hec_node_tier
                                                              hec_node_db_serv_inst        = <fs_db_server>-hec_node_db_serv_inst
                                                              hec_node_db_inst             = <fs_db_server>-hec_node_db_inst
                                                              hec_node_db_node             = <fs_db_server>-hec_node_db_node
                                                              hec_node_db_serv_pc          = <fs_db_server>-hec_node_db_serv_pc
                                                              hec_node_db_server           = <fs_db_server>-hec_node_db_server
                                                              hec_node_db_storage          = /rbp/cl_general_utilities=>get_new_guid22( )
                                                              hec_storage_qty_ref_guid     = <fs_storage_qty>-hec_node_db_storage_qty
                                                              hec_comp_config_id           = lr_landscape->hec_confid
                                                              hec_comp_config_version      = lr_landscape->hec_conf_version
                                                              inh                          = <fs_db_server>-inh
                                                              hec_apm_guid                 = lr_landscape->hec_apm_guid
                                                              hec_apm_descr                = lr_landscape->hec_apm_descr
                                                              hec_storage_quantity         = COND #( WHEN <fs_db_server>-hec_srv_main_stor_qty IS NOT INITIAL
                                                                                                     THEN <fs_db_server>-hec_srv_main_stor_qty      +
                                                                                                          <fs_storage_qty>-hec_dsq_additional_stor_qty
                                                                                                     ELSE COND #( WHEN <fs_db_server>-hec_host_type_value = /hec1/if_config_constants=>gc_server_host_type-virtual
                                                                                                                  THEN <fs_storage_qty>-hec_dsq_main_stor_qty_virtual +
                                                                                                                       <fs_storage_qty>-hec_dsq_additional_stor_qty
                                                                                                                  ELSE  <fs_storage_qty>-hec_dsq_main_stor_qty_virtual +
                                                                                                                        <fs_storage_qty>-hec_dsq_additional_stor_qty ) )
                                                              hec_backup_qty               = SWITCH #( <fs_db_server>-hec_backup_relev_value
                                                                                                       WHEN '01'
                                                                                                       THEN 1
                                                                                                       ELSE 0                                )
                                                              hec_phase_guid               = COND #( WHEN <fs_storage_qty>-hec_phase_guid IS NOT INITIAL
                                                                                                     THEN <fs_storage_qty>-hec_phase_guid
                                                                                                     ELSE space                                          )
                                                              hec_phase_fixed              = abap_true
                                                              hec_phase_assign_allowed     = abap_false
                                                              hec_tree_descr               = COND #( WHEN ls_storage-hec_storage_descr IS INITIAL
                                                                                                     THEN space
                                                                                                     ELSE ls_storage-hec_storage_descr            )
                                                              hec_db_srv_type_guid         = <fs_db_server>-hec_db_srv_type_guid
                                                              crea_uname                    = sy-uname ).

        GET TIME STAMP FIELD lr_db_storage->crea_date_time.

        INSERT VALUE #( data        = lr_db_storage
                        node        = /hec1/if_configuration_c=>sc_node-db_storage
                        source_node = /hec1/if_configuration_c=>sc_node-db_server
                        association = /hec1/if_configuration_c=>sc_association-db_server-db_storage
                        source_key  = <fs_db_server>-key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = lr_db_storage->key                                              ) INTO TABLE lt_modification.


        CLEAR: lv_datacenter_guid,
               ls_pricing,
               lt_storage,
               lr_db_storage.

        UNASSIGN <fs_pricing_included>.
      ENDLOOP.
    ENDLOOP.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_db_storage_amount.

    DATA: lt_db_serv_perf_cat   TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_storage_qty_all TYPE /hec1/t_data_db_storage_qty_ct,
          lt_db_serv_inst       TYPE /hec1/t_data_db_server_inst_ct,
          lt_tier               TYPE /hec1/t_data_tier_ct,
          lt_modification       TYPE /bobf/t_frw_modification.


    CONSTANTS: lc_factor TYPE p DECIMALS 1 VALUE '1.2'.

    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_create_db_qty.


    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_act_param>.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_serv_perf_cat ).

    "-----------------------------------
    " Get APM model GUID and description
    " delivery unit and data centers
    "-----------------------------------
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key       ).
    "-----------------------------------
    " Get tier for DB server type
    "-----------------------------------
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_node
                                                it_key         = VALUE #( FOR wa IN <fs_act_param>
                                                                          ( key = wa-parent_key ) )
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)
                                                et_key_link    = DATA(lt_key_link)
                                                et_failed_key  = et_failed_key                                                  ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-instance_db
                                                it_key         = lt_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-to_parent
                                      IMPORTING et_data        = lt_db_serv_inst
                                                et_target_key  = DATA(lt_db_serv_inst_key)
                                                et_key_link    = DATA(lt_db_serv_inst_key_link)
                                                et_failed_key  = et_failed_key                                                  ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                it_key         = lt_db_serv_inst_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-to_parent
                                      IMPORTING et_data        = lt_tier
                                                et_key_link    = DATA(lt_tier_key_link)
                                                et_failed_key  = et_failed_key                                                         ).

    "-----------------------------------
    " Get DB Storage Amounts
    "-----------------------------------
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount
                                      IMPORTING et_data        = lt_db_storage_qty_all ).

    "-----------------------------------
    " Get server performance category
    "-----------------------------------
    DATA(lt_range_table) = VALUE /hec1/t_selection_range( FOR wa_spc IN lt_db_serv_perf_cat
                                                        ( option = /hec1/if_config_constants=>gc_range_option-eq
                                                          sign   = /hec1/if_config_constants=>gc_range_sign-i
                                                          low    = wa_spc-hec_srv_perf_cat_guid                   ) ).

    SELECT *                                  "#EC CI_ALL_FIELDS_NEEDED
      FROM /hec1/i_dbservperfcatbasic
     WHERE hec_apm_guid          = @lr_landscape->hec_apm_guid          AND
           hec_inf_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid AND
           hec_srv_perf_cat_guid IN @lt_range_table
      INTO TABLE @DATA(lt_serv_perf_cat).


    "-----------------------------------
    " Fill DB storage amount data
    "-----------------------------------
    LOOP AT lt_db_serv_perf_cat ASSIGNING FIELD-SYMBOL(<fs_db_serv_perf_cat>).
      ASSIGN <fs_act_param>[ key = <fs_db_serv_perf_cat>-key ] TO FIELD-SYMBOL(<fs_param>).

      IF <fs_param> IS ASSIGNED.
        DO <fs_param>-hec_storage_amount_qty TIMES.

          " Get DB server type from tier
          TRY.
              DATA(lv_inst_db_key)      = lt_key_link[ source_key = <fs_db_serv_perf_cat>-parent_key ]-target_key.
              DATA(lv_db_serv_inst_key) = lt_db_serv_inst_key_link[ source_key = lv_inst_db_key ]-target_key.
              DATA(lv_db_server_type)   = lt_db_serv_inst[ key = lv_db_serv_inst_key ]-hec_db_srv_type_value.
            CATCH cx_sy_itab_line_not_found.
          ENDTRY.


          "***********
          " Datacenter mit in selektion?????????

          TRY.
              DATA(ls_serv_perf_cat) = lt_serv_perf_cat[ hec_srv_perf_cat_guid = <fs_db_serv_perf_cat>-hec_srv_perf_cat_guid ].
            CATCH cx_sy_itab_line_not_found.
          ENDTRY.

          DATA(lr_db_storage_qty) = NEW /hec1/s_data_db_storage_qty_cs( parent_key                    = <fs_db_serv_perf_cat>-key
                                                                       key                            = /bopf/cl_frw_factory=>get_new_key( )
                                                                       hec_node_solution              = <fs_db_serv_perf_cat>-hec_node_solution
                                                                       hec_node_tier                  = <fs_db_serv_perf_cat>-hec_node_tier
                                                                       hec_node_db_serv_inst          = <fs_db_serv_perf_cat>-hec_node_db_serv_inst
                                                                       hec_node_db_inst               = <fs_db_serv_perf_cat>-hec_node_db_inst
                                                                       hec_node_db_node               = <fs_db_serv_perf_cat>-hec_node_db_node
                                                                       hec_node_db_serv_pc            = <fs_db_serv_perf_cat>-hec_node_db_serv_pc
                                                                       hec_node_db_storage_qty        = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                       hec_comp_config_id             = lr_landscape->hec_confid
                                                                       hec_comp_config_version        = lr_landscape->hec_conf_version
                                                                       inh                            = <fs_db_serv_perf_cat>-inh
                                                                       hec_apm_guid                   = lr_landscape->hec_apm_guid
                                                                       hec_apm_descr                  = lr_landscape->hec_apm_descr
                                                                       hec_dsq_main_stor_qty_virtual  = SWITCH #( lv_db_server_type
                                                                                                                  WHEN /hec1/if_config_constants=>gc_db_server_type-hana
                                                                                                                  THEN lc_factor * ls_serv_perf_cat-hec_srv_ram_class
                                                                                                                  ELSE space                                              )
                                                                       hec_dsq_main_stor_qty_physical = 10
                                                                       hec_tree_descr                 = SWITCH #( lv_db_server_type
                                                                                                                  WHEN /hec1/if_config_constants=>gc_db_server_type-hana
                                                                                                                  THEN |{ lc_factor * ls_serv_perf_cat-hec_srv_ram_class } + 0[GiB]|
                                                                                                                  ELSE space                                                 )
                                                                       hec_phase_guid                 = COND #( WHEN <fs_db_serv_perf_cat>-hec_storage_qty = 1
                                                                                                                THEN <fs_db_serv_perf_cat>-hec_phase_guid )
                                                                       hec_phase_fixed                = COND #( WHEN <fs_db_serv_perf_cat>-hec_storage_qty = 1
                                                                                                                THEN abap_true )
                                                                       hec_phase_assign_allowed       = abap_false
                                                                       crea_uname                     = sy-uname ).

          GET TIME STAMP FIELD lr_db_storage_qty->crea_date_time.

          INSERT VALUE #( data        = lr_db_storage_qty
                            node        = /hec1/if_configuration_c=>sc_node-db_storage_amount
                            source_node = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                            association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount
                            source_key  = <fs_db_serv_perf_cat>-key
                            change_mode = /bobf/if_frw_c=>sc_modify_create
                            key         = lr_db_storage_qty->key                                                            ) INTO TABLE lt_modification.

          CLEAR: lv_inst_db_key,
                 lv_db_serv_inst_key,
                 lv_db_server_type,
                 ls_serv_perf_cat,
                 lr_db_storage_qty.
        ENDDO.

        "-----------------------------------
        " Clear phasing for previously last
        " object in successor/predecessor chain
        "-----------------------------------
        TRY.
            DATA(lr_db_storage_qty_pred) = NEW /hec1/s_data_db_storage_qty_cs( lt_db_storage_qty_all[ parent_key        = <fs_db_serv_perf_cat>-key
                                                                                                      hec_has_successor = abap_false                ] ).

            lr_db_storage_qty_pred->hec_phase_assign_allowed = COND #( WHEN lr_db_storage_qty_pred->hec_phase_guid IS NOT INITIAL
                                                                        AND lr_db_storage_qty_pred->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master
                                                                       THEN abap_true
                                                                       ELSE abap_false ).

            CLEAR: lr_db_storage_qty_pred->hec_phase_guid,
                   lr_db_storage_qty_pred->hec_phase_changed.

            lr_db_storage_qty_pred->hec_phase_fixed = abap_false.

            INSERT VALUE #( data        = lr_db_storage_qty_pred
                            node        = /hec1/if_configuration_c=>sc_node-db_storage_amount
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_db_storage_qty_pred->key    ) INTO TABLE lt_modification.

          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

      ENDIF. " IF <fs_param> IS ASSIGNED.

      UNASSIGN <fs_param>.
    ENDLOOP.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_db_storage_backup.

    DATA: lt_db_storage   TYPE /hec1/t_data_db_storage_ct,
          ls_landscape    TYPE /hec1/s_config_root_cs,
          lt_db_backup    TYPE /hec1/t_data_db_backup_ct,
          lt_modification TYPE /bobf/t_frw_modification.

    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_create_db_backup.


    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_act_param>.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_storage   ).

    " all backups need to clear the phasing for previous nodes
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_storage-db_storage_backup
                                      IMPORTING et_data        = lt_db_backup ).

    "-----------------------------------
    " Get APM model GUID and description
    "-----------------------------------
    /hec1/cl_config_helper=>get_apm_model( EXPORTING iv_node_key   = is_ctx-node_key
                                                     it_key        = it_key
                                                     io_read       = io_read
                                           IMPORTING et_failed_key = et_failed_key
                                                     es_apm_model  = ls_landscape    ).

    "-----------------------------------
    " Fill DB storage backup data
    "-----------------------------------
    LOOP AT lt_db_storage ASSIGNING FIELD-SYMBOL(<fs_db_storage>).
      ASSIGN <fs_act_param>[ key = <fs_db_storage>-key ] TO FIELD-SYMBOL(<fs_param>).

      IF <fs_param> IS ASSIGNED.
        DO <fs_param>-hec_backup_qty TIMES.

          " Get storage backup pricing
          /hec1/cl_config_action_helper=>/hec1/if_bopf_action_helper~get_backup_class_and_price( EXPORTING is_ctx                  = CORRESPONDING #( is_ctx )
                                                                                                           it_key                  = VALUE #( ( key = <fs_db_storage>-key ) )
                                                                                                           iv_tier_category_value  = <fs_db_storage>-hec_tier_cat_value
                                                                                                           iv_tier_datacenter_guid = <fs_db_storage>-hec_tier_datacenter_guid
                                                                                                           io_read                 = io_read
                                                                                                 IMPORTING es_backup_class         = DATA(ls_fdt_backup_class)
                                                                                                           es_backup_pricing       = DATA(ls_fdt_backup_pricing)                ).


          DATA(lr_db_backup) = NEW /hec1/s_data_db_backup_cs( parent_key               = <fs_db_storage>-parent_key
                                                              key                      = /bopf/cl_frw_factory=>get_new_key( )
                                                              hec_node_solution        = <fs_db_storage>-hec_node_solution
                                                              hec_node_tier            = <fs_db_storage>-hec_node_tier
                                                              hec_node_db_serv_inst    = <fs_db_storage>-hec_node_db_serv_inst
                                                              hec_node_db_inst         = <fs_db_storage>-hec_node_db_inst
                                                              hec_node_db_node         = <fs_db_storage>-hec_node_db_node
                                                              hec_node_db_serv_pc      = <fs_db_storage>-hec_node_db_serv_pc
                                                              hec_node_db_server       = <fs_db_storage>-hec_node_db_server
                                                              hec_node_db_storage      = <fs_db_storage>-hec_node_db_storage
                                                              hec_node_db_backup       = /rbp/cl_general_utilities=>get_new_guid22( )
                                                              hec_comp_config_id       = ls_landscape-hec_confid
                                                              hec_comp_config_version  = ls_landscape-hec_conf_version
                                                              inh                      = <fs_db_storage>-inh
                                                              hec_apm_guid             = ls_landscape-hec_apm_guid
                                                              hec_apm_descr            = ls_landscape-hec_apm_descr
                                                              hec_backup_class_guid    = ls_fdt_backup_class-hec_backup_class_guid
                                                              hec_backup_class_descr   = ls_fdt_backup_class-hec_backup_class_descr
                                                              hec_tree_descr           = ls_fdt_backup_class-hec_backup_class_descr
                                                              price                    = ls_fdt_backup_pricing
*                                                              hec_db_srv_type_guid     = <fs_db_storage>-hec_db_srv_type_guid
                                                              hec_phase_guid           = COND #( WHEN <fs_db_storage>-hec_backup_qty = 1
                                                                                                 THEN <fs_db_storage>-hec_phase_guid
                                                                                                 ELSE space )
                                                              hec_phase_fixed          = COND #( WHEN <fs_db_storage>-hec_backup_qty = 1
                                                                                                 THEN abap_true
                                                                                                 ELSE abap_false )
                                                              hec_phase_assign_allowed = abap_false
                                                              crea_uname               = sy-uname ).

          GET TIME STAMP FIELD lr_db_backup->crea_date_time.

          INSERT VALUE #( data        = lr_db_backup
                          node        = /hec1/if_configuration_c=>sc_node-db_storage_backup
                          source_node = /hec1/if_configuration_c=>sc_node-db_storage
                          association = /hec1/if_configuration_c=>sc_association-db_storage-db_storage_backup
                          source_key  = <fs_db_storage>-key
                          change_mode = /bobf/if_frw_c=>sc_modify_create
                          key         = lr_db_backup->key                                                      ) INTO TABLE lt_modification.


          CLEAR: ls_fdt_backup_class,
                 ls_fdt_backup_pricing,
                 lr_db_backup.
        ENDDO.

        "-----------------------------------
        " Clear phasing for previously last
        " object in successor/predecessor chain
        "-----------------------------------
        TRY.
            lr_db_backup = NEW /hec1/s_data_db_backup_cs( lt_db_backup[ parent_key = <fs_db_storage>-key
                                                                        hec_has_successor = abap_false ] ).

            lr_db_backup->hec_phase_assign_allowed = COND #( WHEN lr_db_backup->hec_phase_guid IS NOT INITIAL
                                                              AND lr_db_backup->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master
                                                             THEN abap_true
                                                             ELSE abap_false ).

            CLEAR: lr_db_backup->hec_phase_guid,
                   lr_db_backup->hec_phase_changed.

            lr_db_backup->hec_phase_fixed = abap_false.

            INSERT VALUE #( data        = lr_db_backup
                            node        = /hec1/if_configuration_c=>sc_node-db_storage_backup
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_db_backup->key    ) INTO TABLE lt_modification.

          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

      ENDIF. "IF <fs_param> IS ASSIGNED.

      UNASSIGN <fs_param>.
    ENDLOOP.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_delivery_unit.

    DATA: lt_modification TYPE /bobf/t_frw_modification,
          lt_landscape    TYPE /hec1/t_data_landscape_ct,
          lt_root         TYPE /hec1/t_config_root_ct.


    "-----------------------------------
    " Get APM model GUID and description
    " delivery unit and data centers
    "-----------------------------------
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key   = is_ctx-node_key
                                                        it_key        = it_key
                                                        io_read       = io_read
                                              IMPORTING er_landscape  = DATA(lr_landscape)
                                                        et_failed_key = et_failed_key      ).


    "this is triggered from delivery-node
    io_read->get_root_key( EXPORTING iv_node       = is_ctx-node_key
                                     it_key        = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).



    LOOP AT lt_root_key ASSIGNING FIELD-SYMBOL(<fs_root>).
      "-----------------------------------
      " Set delivery unit data
      "-----------------------------------
      DATA(lv_delivery_unit_key) = /bopf/cl_frw_factory=>get_new_key( ).

      DATA(lr_delivery_unit) = NEW /hec1/s_data_dlvy_unit_cs( parent_key              = <fs_root>-key
                                                              key                     = lv_delivery_unit_key
                                                              hec_node_delivery_unit  = /rbp/cl_general_utilities=>get_new_guid22( )
                                                              hec_comp_config_id      = lr_landscape->hec_confid
                                                              hec_comp_config_version = lr_landscape->hec_conf_version
                                                              hec_row_selectable      = abap_true
                                                              crea_uname              = sy-uname                                      ).

      GET TIME STAMP FIELD lr_delivery_unit->crea_date_time.

      INSERT VALUE #( data        = lr_delivery_unit
                      node        = /hec1/if_configuration_c=>sc_node-delivery_unit
                      source_node = /hec1/if_configuration_c=>sc_node-root
                      association = /hec1/if_configuration_c=>sc_association-root-delivery_unit
                      source_key  = <fs_root>-key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = lv_delivery_unit_key                                         ) INTO TABLE lt_modification.
    ENDLOOP.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).
      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
               IMPORTING eo_message             = DATA(lo_message)
                         eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_instance_db.

    DATA: lt_db_server_inst TYPE /hec1/t_data_db_server_inst_ct,
          lt_modification   TYPE /bobf/t_frw_modification,
          ls_landscape      TYPE /hec1/s_config_root_cs,
          lv_counter        TYPE int4.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_server_inst ).

    "-----------------------------------
    " Get APM model GUID and description
    "-----------------------------------
    /hec1/cl_config_helper=>get_apm_model( EXPORTING iv_node_key   = is_ctx-node_key
                                                     it_key        = it_key
                                                     io_read       = io_read
                                           IMPORTING et_failed_key = et_failed_key
                                                     es_apm_model  = ls_landscape    ).

    "-----------------------------------
    " Get DB node type, cluster type
    " and cluster node type
    "-----------------------------------
    SELECT *                                  "#EC CI_ALL_FIELDS_NEEDED
      FROM /hec1/i_dbnodetypebasic
     WHERE hec_apm_guid = @ls_landscape-hec_apm_guid
      INTO TABLE @DATA(lt_db_node_type).

    SELECT *                                  "#EC CI_ALL_FIELDS_NEEDED
      FROM /hec1/i_dbclustertypebasic
     WHERE hec_apm_guid = @ls_landscape-hec_apm_guid
      INTO TABLE @DATA(lt_db_cluster_type).

    SELECT *                                  "#EC CI_ALL_FIELDS_NEEDED
     FROM /hec1/i_dbclustnodetypebasic
    WHERE hec_apm_guid = @ls_landscape-hec_apm_guid
     INTO TABLE @DATA(lt_db_cluster_node_type).

    "-----------------------------------
    " Get DB node type
    "-----------------------------------
    LOOP AT lt_db_server_inst ASSIGNING FIELD-SYMBOL(<fs_db_serv_inst>).

      DATA(lt_node_type) = VALUE /hec1/t_apm_db_node_type( FOR wa_nt IN lt_db_node_type
                                                           WHERE ( hec_sol_tier_dsi_dbstype_guid  = <fs_db_serv_inst>-hec_sol_tier_dsi_dbstype_guid  AND
                                                                   hec_sol_dbst_imty_inty_al_guid = <fs_db_serv_inst>-hec_sol_dbst_imty_inty_al_guid     )
                                                           ( CORRESPONDING #( wa_nt ) )                                                ).

      " DB server instance: DB instance type = Container
      " then 2 instance DB are needed: - DB Tenant
      "                                - Container DB
      "
      " !!! Both instance DB have then the same Multitenancy Relation ID !!!
      IF line_exists( lt_node_type[ hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-container ] ).
        DATA(lv_multi_ten_id) = /rbp/cl_general_utilities=>get_new_guid22( ).
      ENDIF.

      WHILE lv_counter < <fs_db_serv_inst>-hec_db_quantity.
        ADD 1 TO lv_counter.

        TRY.
            DATA(ls_node_type) = lt_node_type[ lv_counter ].

            " Get DB server cluster type
            DATA(ls_cluster_type) = lt_db_cluster_type[ hec_sol_tier_dsi_dbstype_guid = <fs_db_serv_inst>-hec_sol_tier_dsi_dbstype_guid
                                                        hec_sol_dbst_alloc_nodety_guid = ls_node_type-hec_sol_dbst_alloc_nodety_guid
                                                        hec_db_node_type_guid          = ls_node_type-hec_db_node_type_guid
                                                        hec_db_cluster_type_value      = /hec1/if_config_constants=>gc_db_clust_node-none
                                                        hec_clu_support_stat_value     = '02'                                             ].

            " Get DB server cluster node type
            DATA(ls_cluster_node_type) = lt_db_cluster_node_type[ hec_dbst_nodety_clust_ty_guid = ls_cluster_type-hec_dbst_nodety_clust_ty_guid
                                                                  hec_db_clust_node_type_value  = /hec1/if_config_constants=>gc_db_clust_node_type-master ].

          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        DATA(lr_instance_db) = NEW /hec1/s_data_db_inst_cs( parent_key                     = <fs_db_serv_inst>-key
                                                            key                            = /bopf/cl_frw_factory=>get_new_key( )
                                                            hec_node_solution              = <fs_db_serv_inst>-hec_node_solution
                                                            hec_node_tier                  = <fs_db_serv_inst>-hec_node_tier
                                                            hec_node_db_serv_inst          = <fs_db_serv_inst>-hec_node_db_serv_inst
                                                            hec_node_db_inst               = /rbp/cl_general_utilities=>get_new_guid22( )
                                                            hec_comp_config_id             = ls_landscape-hec_confid
                                                            hec_comp_config_version        = ls_landscape-hec_conf_version
                                                            inh                            = <fs_db_serv_inst>-inh
                                                            hec_sol_tier_dsi_dbstype_guid  = <fs_db_serv_inst>-hec_sol_tier_dsi_dbstype_guid
                                                            hec_db_srv_type_guid           = <fs_db_serv_inst>-hec_db_srv_type_guid
                                                            hec_db_srv_type_value          = <fs_db_serv_inst>-hec_db_srv_type_value
                                                            hec_server_required            = <fs_db_serv_inst>-hec_server_required
                                                            hec_effort_required            = <fs_db_serv_inst>-hec_effort_required
                                                            hec_backup_relev_value         = <fs_db_serv_inst>-hec_backup_relev_value
                                                            hec_backup_relev_descr         = <fs_db_serv_inst>-hec_backup_relev_descr
                                                            hec_db_impl_type_value         = <fs_db_serv_inst>-hec_db_impl_type_value
                                                            hec_db_inst_type_value         = <fs_db_serv_inst>-hec_db_inst_type_value
                                                            hec_apm_guid                   = ls_landscape-hec_apm_guid
                                                            hec_apm_descr                  = ls_landscape-hec_apm_descr
                                                            hec_sol_dbst_alloc_nodety_guid = ls_node_type-hec_sol_dbst_alloc_nodety_guid
                                                            hec_db_node_type_guid          = ls_node_type-hec_db_node_type_guid
                                                            hec_db_node_type_value         = ls_node_type-hec_db_node_type_value
                                                            hec_db_node_type_descr         = ls_node_type-hec_db_node_type_descr
                                                            hec_multi_tenant_rel_guid      = lv_multi_ten_id
                                                            hec_dbst_nodety_clust_ty_guid  = ls_cluster_type-hec_dbst_nodety_clust_ty_guid
                                                            hec_db_cluster_type_guid       = ls_cluster_type-hec_db_cluster_type_guid
                                                            hec_db_cluster_type_value      = ls_cluster_type-hec_db_cluster_type_value
                                                            hec_db_cluster_type_descr      = ls_cluster_type-hec_db_cluster_type_descr
                                                            hec_init_clu_supp_stat_value   = ls_cluster_type-hec_clu_support_stat_value
                                                            hec_init_clu_supp_stat_descr   = ls_cluster_type-hec_clu_support_stat_descr
                                                            hec_clu_support_stat_value     = ls_cluster_type-hec_clu_support_stat_value
                                                            hec_clu_support_stat_descr     = ls_cluster_type-hec_clu_support_stat_descr
                                                            hec_db_master_node_qty         = 1
                                                            hec_db_master_node_lower_qty   = ls_cluster_node_type-hec_db_node_limit_low
                                                            hec_db_master_node_limit_qty   = ls_cluster_node_type-hec_db_node_limit_high
                                                            hec_row_selectable             = abap_true
                                                            hec_phase_fixed                = COND #( WHEN ls_node_type-hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-container
                                                                                                       OR ls_node_type-hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-single
                                                                                                     THEN abap_true
                                                                                                     ELSE abap_false )
                                                            hec_phase_guid                 = COND #( WHEN ls_node_type-hec_db_node_type_value <> /hec1/if_config_constants=>gc_db_node_type-container
                                                                                                       OR <fs_db_serv_inst>-hec_db_allocation_value <> /hec1/if_config_constants=>gc_db_allocation-separate_db
                                                                                                     THEN <fs_db_serv_inst>-hec_phase_guid )
                                                            hec_phase_assign_allowed       = COND #( WHEN ls_node_type-hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-container
                                                                                                       OR ls_node_type-hec_db_node_type_value = /hec1/if_config_constants=>gc_db_node_type-single
                                                                                                     THEN abap_false
                                                                                                     ELSE abap_true )
                                                            hec_tree_descr                 = |: { ls_node_type-hec_db_node_type_descr }|
                                                            crea_uname                     = sy-uname ).

        GET TIME STAMP FIELD lr_instance_db->crea_date_time.


        INSERT VALUE #( data        = lr_instance_db
                        node        = /hec1/if_configuration_c=>sc_node-instance_db
                        source_node = /hec1/if_configuration_c=>sc_node-db_server_instance
                        association = /hec1/if_configuration_c=>sc_association-db_server_instance-instance_db
                        source_key  = <fs_db_serv_inst>-key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = lr_instance_db->key                                                       ) INTO TABLE lt_modification.

        CLEAR: ls_node_type,
               ls_cluster_type,
               ls_cluster_node_type.
      ENDWHILE.

      CLEAR: lv_multi_ten_id,
             lv_counter,
             lt_node_type.
    ENDLOOP.


    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_man_serv_baseline.

    DATA: lt_modification TYPE /bobf/t_frw_modification,
          lt_landscape    TYPE /hec1/t_config_root_ct,
          lt_phase        TYPE /hec1/t_data_phase_ct,
          lt_root         TYPE /hec1/t_config_root_ct.


    " This is triggered from landscape node(root)
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_landscape ).


    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                      IMPORTING et_data        = lt_phase ).


    LOOP AT lt_landscape ASSIGNING FIELD-SYMBOL(<fs_landscape>).
      TRY.
          DATA(ls_phase) = lt_phase[ parent_key = <fs_landscape>-root_key ].
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.

      DATA(lv_key) = /bopf/cl_frw_factory=>get_new_key( ).
      "-----------------------------------
      " Set managed service baseline data
      "-----------------------------------
      DATA(lr_man_serv_base) = NEW /hec1/s_data_man_serv_basel_cs( BASE CORRESPONDING #( <fs_landscape> )
                                                                   parent_key               = <fs_landscape>-key
                                                                   key                      = lv_key
                                                                   hec_node_man_service_bl  = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                   hec_comp_config_id       = <fs_landscape>-hec_confid
                                                                   hec_comp_config_version  = <fs_landscape>-hec_conf_version
                                                                   hec_phase_guid           = ls_phase-hec_node_phase
                                                                   hec_phase_assign_allowed = abap_false
                                                                   crea_uname               = sy-uname ).

      GET TIME STAMP FIELD lr_man_serv_base->crea_date_time.

      INSERT VALUE #( data        = lr_man_serv_base
                      node        = /hec1/if_configuration_c=>sc_node-managed_service_baseline
                      source_node = /hec1/if_configuration_c=>sc_node-root
                      association = /hec1/if_configuration_c=>sc_association-root-managed_service_baseline
                      source_key  = <fs_landscape>-key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = lv_key                                                               ) INTO TABLE lt_modification.

      CLEAR lv_key.
    ENDLOOP.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_material.

    " input node is the tier
    " this method checks the selected materials against the existing materials and creates the delta

    DATA: lt_tier             TYPE /hec1/t_data_tier_ct,
          lt_solution         TYPE /hec1/t_data_solution_ct,
          lt_material         TYPE /hec1/t_data_material_ct,
          lt_parameter        TYPE /hec1/t_act_create_material,
          lt_act_param_delete TYPE /bobf/t_frw_node,
          lt_modification     TYPE /bobf/t_frw_modification.


    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO FIELD-SYMBOL(<fs_parameter>).

    IF <fs_parameter> IS INITIAL.
      RETURN. ">>>>
    ENDIF.

    lt_parameter = <fs_parameter>.


    "-----------------------------------
    " Get APM model GUID and description
    " delivery unit and data centers
    "-----------------------------------
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key   = is_ctx-node_key
                                                        it_key        = it_key
                                                        io_read       = io_read
                                              IMPORTING er_landscape  = DATA(lr_landscape)
                                                        et_failed_key = et_failed_key      ).

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = VALUE #( FOR param IN lt_parameter
                                                    ( key = param-parent_key ) )
                       IMPORTING et_data = lt_tier ).

    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = VALUE #( FOR param IN lt_parameter
                                                                        ( key = param-parent_key ) )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier-material
                                      IMPORTING et_data        = lt_material ).

    " Get Material List
    DATA(lt_material_list) = /hec1/cl_config_sw_helper=>get_instance( )->/hec1/if_config_sw_helper~get_material_list( ).

    LOOP AT lt_parameter ASSIGNING FIELD-SYMBOL(<fs_parameter_line>).

      TRY.
          DATA(ls_tier) = lt_tier[ key = <fs_parameter_line>-parent_key ].
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.

      " Create materials in material list
      LOOP AT lt_material_list ASSIGNING FIELD-SYMBOL(<fs_material_list>)
        WHERE hec_node_solution = ls_tier-hec_node_solution
          AND hec_mat_selection = abap_true.
        " **************
        " add material
        " **************
        " check if material exists
        IF NOT line_exists( lt_material[ hec_node_solution = <fs_material_list>-hec_node_solution
                                         hec_material_guid = <fs_material_list>-hec_material_guid ] ).

          DATA(lr_material_new) = NEW /hec1/s_data_material_cs( BASE CORRESPONDING #( <fs_material_list> )
                                                                parent_key               = ls_tier-key
                                                                key                      = /bopf/cl_frw_factory=>get_new_key( )
                                                                hec_node_solution        = ls_tier-hec_node_solution
                                                                hec_node_tier            = ls_tier-hec_node_tier
                                                                hec_node_material        = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                hec_comp_config_id       = lr_landscape->hec_confid
                                                                hec_comp_config_version  = lr_landscape->hec_conf_version
                                                                hec_row_selectable       = abap_true
                                                                hec_apm_guid             = ls_tier-hec_apm_guid
                                                                hec_apm_descr            = ls_tier-hec_apm_descr
                                                                hec_phase_guid           = ls_tier-hec_phase_guid
                                                                hec_phase_fixed          = COND #( WHEN <fs_material_list>-hec_material_rel_value = /hec1/if_config_constants=>gc_material_rel-mandatory "'01'
                                                                                                   THEN abap_true
                                                                                                   ELSE abap_false )
                                                                hec_phase_assign_allowed = COND #( WHEN <fs_material_list>-hec_material_rel_value = /hec1/if_config_constants=>gc_material_rel-mandatory "'01'
                                                                                                   THEN abap_false
                                                                                                   ELSE abap_true )
                                                                hec_phase_changed        = abap_true
                                                                crea_uname               = sy-uname ).

          GET TIME STAMP FIELD lr_material_new->crea_date_time.

          INSERT VALUE #( data        = lr_material_new
                          node        = /hec1/if_configuration_c=>sc_node-material
                          source_node = /hec1/if_configuration_c=>sc_node-tier
                          association = /hec1/if_configuration_c=>sc_association-tier-material
                          source_key  = ls_tier-key
                          change_mode = /bobf/if_frw_c=>sc_modify_create
                          key         = lr_material_new->key )
                          INTO TABLE lt_modification.

        ENDIF.

      ENDLOOP. "lt_material_list

    ENDLOOP. "lt_parameter

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.

    "-----------------------------------
    " Set Delete action to GENERAL
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


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_phase.

    DATA: lt_modification TYPE /bobf/t_frw_modification,
          lt_root         TYPE /hec1/t_config_root_ct.

    "this is triggered from root
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_root ).

    LOOP AT lt_root ASSIGNING FIELD-SYMBOL(<fs_root>).
      "-----------------------------------
      " Set default phase data
      "-----------------------------------
      INSERT VALUE #( data        = NEW /hec1/s_data_phase_cs( hec_node_parent_phase = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_root>-key )
                                                               hec_node_phase        = /rbp/cl_general_utilities=>get_new_guid22( )
                                                               hec_default_phase     = abap_true
                                                               hec_phase_descr       = |Default|
                                                               hec_phase_tree_descr  = |Default|
                                                               hec_duration_unit     = COND #( WHEN <fs_root>-hec_ls_contract_dur_unit_value IS INITIAL
                                                                                               THEN '02'
                                                                                               ELSE <fs_root>-hec_ls_contract_dur_unit_value ) ) "Months
*                                                                       "ITSHECS4HANA-1799
*                                                                       hec_phase_start_date  = iv_contract_start_date
*                                                                       hec_phase_end_date    = iv_contract_end_date
                      node        = /hec1/if_configuration_c=>sc_node-phase
                      source_node = /hec1/if_configuration_c=>sc_node-root
                      association = /hec1/if_configuration_c=>sc_association-root-phase
                      source_key  = <fs_root>-key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = /bopf/cl_frw_factory=>get_new_key( )                                            )
      INTO TABLE lt_modification.

    ENDLOOP.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).
      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
               IMPORTING eo_message             = DATA(lo_message)
                         eo_change              = DATA(lo_change)  ).
    ENDIF.

    CLEAR: lt_modification.

  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_server_instance.

    DATA: lt_tier              TYPE /hec1/t_data_tier_ct,
          lt_tier_all          TYPE /hec1/t_data_tier_ct,
          lt_root_key          TYPE /bobf/t_frw_key,
          lt_landscape         TYPE /hec1/t_data_landscape_ct,
          lt_solution          TYPE /hec1/t_data_solution_ct,
          lt_db_server_inst    TYPE /hec1/t_data_db_server_inst_ct,
          lt_app_server_inst   TYPE /hec1/t_data_app_serv_inst_ct,
          lt_db_serv_inst_mod  TYPE /bobf/t_frw_modification,
          lt_app_serv_inst_mod TYPE /bobf/t_frw_modification,
          lt_dd07v             TYPE dd07v_tab,
          ls_landscape         TYPE /hec1/s_config_root_cs.

    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_create_serv_inst.


    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_act_param>.


    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_tier ).

    " get related tier
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier-to_parent
                                      IMPORTING et_target_key  = DATA(lt_solution_key) ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-solution
                                                it_key         = lt_solution_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                      IMPORTING et_data        = lt_tier_all ).

    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier-db_server_instance
                                      IMPORTING et_data        = lt_db_server_inst ).


    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier-app_server_instance
                                      IMPORTING et_data        = lt_app_server_inst ).


    "-----------------------------------
    " Get APM model GUID and description
    "-----------------------------------
    /hec1/cl_config_helper=>get_apm_model( EXPORTING iv_node_key   = is_ctx-node_key
                                                     it_key        = it_key
                                                     io_read       = io_read
                                           IMPORTING et_failed_key = et_failed_key
                                                     es_apm_model  = ls_landscape ).


    "-----------------------------------
    " Get DB server instance data
    "-----------------------------------
    SELECT *                                  "#EC CI_ALL_FIELDS_NEEDED
      FROM /hec1/i_dbservinstancenobasic
     WHERE hec_apm_guid = @ls_landscape-hec_apm_guid
      INTO TABLE @DATA(lt_db_serv_inst_no).


    "-----------------------------------
    " Get DB server type
    "-----------------------------------
    SELECT *                                  "#EC CI_ALL_FIELDS_NEEDED
      FROM /hec1/i_dbservertypebasic
     WHERE hec_apm_guid  = @ls_landscape-hec_apm_guid
      INTO TABLE @DATA(lt_db_server_type).


    "-----------------------------------
    " Get DB server operating system
    "-----------------------------------
    SELECT *                                  "#EC CI_ALL_FIELDS_NEEDED
      FROM /hec1/i_dboperssystembasic
     WHERE hec_apm_guid  = @ls_landscape-hec_apm_guid
      INTO TABLE @DATA(lt_db_operating_sys).


    "-----------------------------------
    " Get DB server implementation type
    "-----------------------------------
    SELECT *                                  "#EC CI_ALL_FIELDS_NEEDED
      FROM /hec1/i_dbimplementtypebasic
     WHERE hec_apm_guid  = @ls_landscape-hec_apm_guid
      INTO TABLE @DATA(lt_db_impl_type).


    "-----------------------------------
    " Get DB server instance type
    "-----------------------------------
    SELECT *                                  "#EC CI_ALL_FIELDS_NEEDED
      FROM /hec1/i_dbinstancetypebasic
     WHERE hec_apm_guid  = @ls_landscape-hec_apm_guid
      INTO TABLE @DATA(lt_db_inst_type).


    "-----------------------------------
    " Get DB server allocation
    "-----------------------------------
    SELECT *                                  "#EC CI_ALL_FIELDS_NEEDED
      FROM /hec1/i_dballocationbasic
     WHERE hec_apm_guid  = @ls_landscape-hec_apm_guid
      INTO TABLE @DATA(lt_db_allocation).


    "-----------------------------------
    " Get App server instance data
    "-----------------------------------
    SELECT *                                  "#EC CI_ALL_FIELDS_NEEDED
      FROM /hec1/i_appservinstancenobasic
     WHERE hec_apm_guid = @ls_landscape-hec_apm_guid
      INTO TABLE @DATA(lt_app_serv_inst_no).

    "-----------------------------------
    " Get App server operating system
    "-----------------------------------
    SELECT *                                  "#EC CI_ALL_FIELDS_NEEDED
      FROM /hec1/i_appopersystembasic
     WHERE hec_apm_guid = @ls_landscape-hec_apm_guid
      INTO TABLE @DATA(lt_app_operating_sys).


    "-----------------------------------
    " " Get Server instance type domain
    "-----------------------------------
    CALL FUNCTION 'DDIF_DOMA_GET'
      EXPORTING
        name          = '/HEC1/DOM_SRV_INST_TYPE'
        langu         = sy-langu
      TABLES
        dd07v_tab     = lt_dd07v
      EXCEPTIONS
        illegal_input = 1
        OTHERS        = 2.

    IF sy-subrc <> 0.
      RETURN. " >>>>>>>>>
    ENDIF.



    LOOP AT lt_tier ASSIGNING FIELD-SYMBOL(<fs_tier>).
      ASSIGN <fs_act_param>[ key = <fs_tier>-key ] TO FIELD-SYMBOL(<fs_param>).

      IF <fs_param> IS ASSIGNED.
        "-----------------------------------
        " Get default DB server instances
        "-----------------------------------
        DATA(lv_tabix)      = 1.
        DATA(lv_default_si) = abap_true.

        IF <fs_param>-hec_default_server_inst = abap_true.
          DATA(lt_db_server_inst_no) = VALUE /hec1/t_apm_db_serv_inst_no( FOR wa_dbpsi IN lt_db_serv_inst_no
                                                                          WHERE ( hec_solution_guid       = <fs_tier>-hec_solution_guid                       AND
                                                                                  hec_sol_tier_stack_guid = <fs_tier>-hec_sol_tier_stack_guid                 AND
                                                                                  hec_srv_inst_rel_value  = /hec1/if_config_constants=>gc_relevance-mandatory     )
                                                                         ( wa_dbpsi )                                                                               ).
        ELSE.
          CLEAR lv_default_si.
        ENDIF. " IF <fs_param>-hec_default_server_inst = abap_true.


        "-----------------------------------
        " " Get Server instance type domain
        "-----------------------------------
        TRY.
            DATA(lv_serv_inst_type_descr) = lt_dd07v[ domvalue_l = /hec1/if_config_constants=>gc_srv_instance_type-db_server ]-ddtext.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.


        " ***************************************************************************
        " DB server instance logic
        " ***************************************************************************
        DO <fs_param>-hec_db_srv_qty TIMES.
          CASE lv_default_si.
              "-----------------------------------
              " Default DB server instance
              "-----------------------------------
            WHEN abap_true.
              TRY.
                  DATA(ls_db_serv_inst_no) = lt_db_server_inst_no[ lv_tabix ].

                  DATA(lt_server_type) = VALUE /hec1/t_apm_db_server_type( FOR wa_type IN lt_db_server_type
                                                                           WHERE ( hec_sol_tier_stack_si_guid = ls_db_serv_inst_no-hec_sol_tier_stack_si_guid )
                                                                           ( wa_type )                                                                          ).

                  IF <fs_tier>-hec_related_stack = abap_true.
                    LOOP AT lt_tier_all INTO DATA(ls_related_tier)
                      WHERE hec_related_stack_guid = <fs_tier>-hec_related_stack_guid
                        AND key <> <fs_tier>-key.
                      " there should only be one entry which is now written into <fs_related_tier>
                    ENDLOOP.
                  ENDIF.

                  IF lines( lt_server_type ) = 1.
                    DATA(ls_db_server_type)  = lt_server_type[ 1 ].
                    "-----------------------------------
                    " If there is only one operating
                    " system, then it should be
                    " preselected
                    "-----------------------------------
                    DATA(lt_operating_sys) = VALUE /hec1/t_apm_db_operating_sys( FOR wa_dbos IN lt_db_operating_sys
                                                                                 WHERE ( hec_sol_tier_dsi_dbstype_guid = ls_db_server_type-hec_sol_tier_dsi_dbstype_guid )
                                                                                 ( CORRESPONDING #( wa_dbos ) )                                                         ).

                    IF lines( lt_operating_sys ) = 1.
                      TRY.
                          DATA(ls_db_operating_sys) = lt_operating_sys[ 1 ].
                        CATCH cx_sy_itab_line_not_found.
                      ENDTRY.
                      "-----------------------------------
                      " If there are multiple operating
                      " systems possible and Linux is
                      " between them - set it preselected
                      "-----------------------------------
                    ELSEIF lines( lt_operating_sys ) > 1 AND line_exists( lt_operating_sys[ hec_operating_sys_value = /hec1/cl_rep_config_data=>c_os_linux ] ).
                      TRY.
                          ls_db_operating_sys = lt_operating_sys[ hec_operating_sys_value = /hec1/cl_rep_config_data=>c_os_linux ].
                        CATCH cx_sy_itab_line_not_found.
                      ENDTRY.
                    ENDIF. " IF lines( lt_db_operating_sys ) = 1.

                    IF ls_db_operating_sys IS NOT INITIAL.
                      DATA(lt_impl_type) = VALUE /hec1/t_apm_db_implement_type( FOR wa_imp IN lt_db_impl_type
                                                                                WHERE ( hec_sol_tier_dsi_dbstype_guid = ls_db_server_type-hec_sol_tier_dsi_dbstype_guid )
                                                                               ( CORRESPONDING #( wa_imp ) )                                                             ).

                      IF lines( lt_impl_type ) = 1.
                        TRY.
                            DATA(ls_impl_type) = lt_impl_type[ 1 ].
                            DATA(lt_inst_type)  = VALUE /hec1/t_apm_db_instance_type( FOR wa_ins IN lt_db_inst_type
                                                                                      WHERE ( hec_sol_tier_dsi_dbstype_guid = ls_impl_type-hec_sol_tier_dsi_dbstype_guid AND
                                                                                              hec_sol_dbst_impltype_guid    = ls_impl_type-hec_sol_dbst_impltype_guid        )
                                                                                      ( CORRESPONDING #( wa_ins ) )                                                            ).

                            IF lines( lt_inst_type ) = 1.
                              TRY.
                                  DATA(ls_inst_type) = lt_inst_type[ 1 ].
                                  DATA(lt_alloc) = VALUE /hec1/t_apm_db_allocation( FOR wa_alloc IN lt_db_allocation
                                                                                    WHERE ( hec_sol_tier_dsi_dbstype_guid  = ls_inst_type-hec_sol_tier_dsi_dbstype_guid  AND
                                                                                            hec_sol_dbst_impty_instty_guid = ls_inst_type-hec_sol_dbst_impty_instty_guid     )
                                                                                    ( CORRESPONDING #( wa_alloc ) )                                                            ).
                                  IF lines( lt_alloc ) = 1.
                                    DATA(ls_allocation) = lt_alloc[ 1 ].
                                  ENDIF.
                                CATCH cx_sy_itab_line_not_found.
                              ENDTRY.
                            ENDIF. " IF lines( lt_impl_type ) = 1.

                          CATCH cx_sy_itab_line_not_found.
                        ENDTRY.
                      ENDIF. " IF lines( lt_impl_type ) = 1.
                    ENDIF. " IF ls_db_operating_sys IS NOT INITIAL.
                  ENDIF. " IF lines(lt_server_type) = 1.
                CATCH cx_sy_itab_line_not_found.
              ENDTRY.

              DATA(lr_db_server_inst) = NEW /hec1/s_data_db_server_inst_cs( parent_key                     = <fs_tier>-key
                                                                            key                            = /bopf/cl_frw_factory=>get_new_key( )
                                                                            hec_node_solution              = <fs_tier>-hec_node_solution
                                                                            hec_node_tier                  = <fs_tier>-hec_node_tier
                                                                            hec_node_db_serv_inst          = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                            hec_comp_config_id             = ls_landscape-hec_confid
                                                                            hec_comp_config_version        = ls_landscape-hec_conf_version
                                                                            hec_solution_guid              = <fs_tier>-hec_solution_guid
                                                                            hec_tier_cat_value             = <fs_tier>-hec_tier_cat_value
                                                                            hec_tier_stack_guid            = <fs_tier>-hec_sol_tier_stack_guid
                                                                            hec_tier_stack_value           = <fs_tier>-hec_sol_tier_stack_value
                                                                            hec_tier_datacenter_guid       = <fs_tier>-hec_tier_datacenter_guid
                                                                            hec_tier_is_dr_node            = <fs_tier>-hec_tier_is_dr_node
                                                                            hec_disaster_rec_option        = <fs_tier>-hec_disaster_rec_option
                                                                            hec_dr_oper_mode_value         = <fs_tier>-hec_dr_oper_mode_value
                                                                            hec_dr_oper_mode_descr         = <fs_tier>-hec_dr_oper_mode_descr
                                                                            hec_apm_guid                   = ls_landscape-hec_apm_guid
                                                                            hec_apm_descr                  = ls_landscape-hec_apm_descr
                                                                            hec_default_db_server_inst     = abap_true
                                                                            hec_sol_tier_dsi_dbstype_guid  = ls_db_server_type-hec_sol_tier_dsi_dbstype_guid
                                                                            hec_db_srv_type_guid           = ls_db_server_type-hec_db_srv_type_guid
                                                                            hec_db_srv_type_value          = ls_db_server_type-hec_db_srv_type_value
                                                                            hec_db_srv_type_descr          = ls_db_server_type-hec_db_srv_type_descr
                                                                            hec_calc_setup_dr              = ls_db_server_type-hec_calc_setup_dr
                                                                            hec_init_ty_support_stat_value = ls_db_server_type-hec_ty_support_stat_value
                                                                            hec_init_ty_support_stat_descr = ls_db_server_type-hec_ty_support_stat_descr
                                                                            hec_ty_support_stat_value      = ls_db_server_type-hec_ty_support_stat_value
                                                                            hec_ty_support_stat_descr      = ls_db_server_type-hec_ty_support_stat_descr
                                                                            hec_srv_inst_type_descr        = lv_serv_inst_type_descr
                                                                            hec_sol_tier_stack_si_guid     = ls_db_serv_inst_no-hec_sol_tier_stack_si_guid
                                                                            hec_sol_tier_dsi_descr         = ls_db_serv_inst_no-hec_sol_tier_dsi_descr
                                                                            hec_srv_inst_rel_value         = ls_db_serv_inst_no-hec_srv_inst_rel_value
                                                                            hec_srv_inst_rel_descr         = ls_db_serv_inst_no-hec_srv_inst_rel_descr
                                                                            hec_main_instance              = ls_db_serv_inst_no-hec_main_instance
                                                                            hec_server_required            = ls_db_serv_inst_no-hec_server_required
                                                                            hec_effort_required            = ls_db_serv_inst_no-hec_effort_required
                                                                            hec_backup_relev_value         = SWITCH #( <fs_tier>-hec_tier_is_dr_node
                                                                                                                       WHEN abap_false
                                                                                                                       THEN ls_db_serv_inst_no-hec_backup_relevance
                                                                                                                       ELSE '03'                                    )
                                                                            hec_backup_relev_descr         = SWITCH #( <fs_tier>-hec_tier_is_dr_node
                                                                                                                       WHEN abap_false
                                                                                                                       THEN ls_db_serv_inst_no-hec_backup_relev_descr
                                                                                                                       ELSE 'None'                                    )
                                                                            hec_data_op_req_value          = ls_db_serv_inst_no-hec_data_op_req_value
                                                                            hec_data_op_req_descr          = ls_db_serv_inst_no-hec_data_op_req_descr
                                                                            hec_sol_dbst_oper_sys_guid     = ls_db_operating_sys-hec_sol_dbst_oper_sys_guid
                                                                            hec_operating_sys_guid         = ls_db_operating_sys-hec_operating_sys_guid
                                                                            hec_operating_sys_value        = ls_db_operating_sys-hec_operating_sys_value
                                                                            hec_operating_sys_descr        = ls_db_operating_sys-hec_operating_sys_descr
                                                                            hec_init_os_support_stat_value = ls_db_operating_sys-hec_os_support_stat_value
                                                                            hec_init_os_support_stat_descr = ls_db_operating_sys-hec_os_support_stat_descr
                                                                            hec_os_support_stat_value      = ls_db_operating_sys-hec_os_support_stat_value
                                                                            hec_os_support_stat_descr      = ls_db_operating_sys-hec_os_support_stat_descr
                                                                            hec_sol_dbst_impltype_guid     = ls_impl_type-hec_sol_dbst_impltype_guid
                                                                            hec_db_impl_type_guid          = ls_impl_type-hec_db_impl_type_guid
                                                                            hec_db_impl_type_value         = ls_impl_type-hec_db_impl_type_value
                                                                            hec_db_impl_type_descr         = ls_impl_type-hec_db_impl_type_descr
                                                                            hec_init_imp_supp_stat_value   = ls_impl_type-hec_imp_support_stat_value
                                                                            hec_init_imp_supp_stat_descr   = ls_impl_type-hec_imp_support_stat_descr
                                                                            hec_imp_support_stat_value     = ls_impl_type-hec_imp_support_stat_value
                                                                            hec_imp_support_stat_descr     = ls_impl_type-hec_imp_support_stat_descr
                                                                            hec_sol_dbst_impty_instty_guid = ls_inst_type-hec_sol_dbst_impty_instty_guid
                                                                            hec_db_inst_type_guid          = ls_inst_type-hec_db_inst_type_guid
                                                                            hec_db_inst_type_value         = ls_inst_type-hec_db_inst_type_value
                                                                            hec_db_inst_type_descr         = ls_inst_type-hec_db_inst_type_descr
                                                                            hec_init_inst_supp_stat_value  = ls_inst_type-hec_inst_support_stat_value
                                                                            hec_init_inst_supp_stat_descr  = ls_inst_type-hec_inst_support_stat_descr
                                                                            hec_inst_support_stat_value    = ls_inst_type-hec_inst_support_stat_value
                                                                            hec_inst_support_stat_descr    = ls_inst_type-hec_inst_support_stat_descr
                                                                            hec_sol_dbst_imty_inty_al_guid = ls_allocation-hec_sol_dbst_imty_inty_al_guid
                                                                            hec_db_allocation_guid         = ls_allocation-hec_db_allocation_guid
                                                                            hec_db_allocation_value        = ls_allocation-hec_db_allocation_value
                                                                            hec_db_allocation_descr        = ls_allocation-hec_db_allocation_descr
                                                                            hec_db_quantity                = ls_allocation-hec_db_quantity
                                                                            hec_init_alloc_supp_stat_value = ls_allocation-hec_alloc_support_stat_value
                                                                            hec_init_alloc_supp_stat_descr = ls_allocation-hec_alloc_support_stat_descr
                                                                            hec_alloc_support_stat_value   = ls_allocation-hec_alloc_support_stat_value
                                                                            hec_alloc_support_stat_descr   = ls_allocation-hec_alloc_support_stat_descr
                                                                            hec_db_tier_guid               = SWITCH #( ls_allocation-hec_db_allocation_value
                                                                                                                       WHEN /hec1/if_config_constants=>gc_db_allocation-internal
                                                                                                                       THEN <fs_tier>-hec_node_tier
                                                                                                                       WHEN /hec1/if_config_constants=>gc_db_allocation-related_stack
                                                                                                                       THEN ls_related_tier-hec_node_tier )
                                                                            hec_phase_guid                 = <fs_tier>-hec_phase_guid
                                                                            hec_phase_fixed                = abap_true
                                                                            hec_phase_assign_allowed       = abap_false  "the default db server instance always gets the tier's phase
                                                                            hec_tree_descr                 = ls_db_server_type-hec_db_srv_type_descr
                                                                            crea_uname                     = sy-uname ).

              GET TIME STAMP FIELD lr_db_server_inst->crea_date_time.

              "-----------------------------------
              " Non default DB server instance
              "-----------------------------------
            WHEN abap_false.
              lr_db_server_inst = NEW /hec1/s_data_db_server_inst_cs( parent_key                   = <fs_tier>-key
                                                                      key                          = /bopf/cl_frw_factory=>get_new_key( )
                                                                      hec_node_solution            = <fs_tier>-hec_node_solution
                                                                      hec_node_tier                = <fs_tier>-hec_node_tier
                                                                      hec_node_db_serv_inst        = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                      hec_comp_config_id           = ls_landscape-hec_confid
                                                                      hec_comp_config_version      = ls_landscape-hec_conf_version
                                                                      hec_solution_guid            = <fs_tier>-hec_solution_guid
                                                                      hec_tier_cat_value           = <fs_tier>-hec_tier_cat_value
                                                                      hec_tier_stack_guid          = <fs_tier>-hec_sol_tier_stack_guid
                                                                      hec_tier_stack_value         = <fs_tier>-hec_sol_tier_stack_value
                                                                      hec_tier_datacenter_guid     = <fs_tier>-hec_tier_datacenter_guid
                                                                      hec_tier_is_dr_node          = <fs_tier>-hec_tier_is_dr_node
                                                                      hec_disaster_rec_option      = <fs_tier>-hec_disaster_rec_option
                                                                      hec_dr_oper_mode_value       = <fs_tier>-hec_dr_oper_mode_value
                                                                      hec_dr_oper_mode_descr       = <fs_tier>-hec_dr_oper_mode_descr
                                                                      hec_apm_guid                 = ls_landscape-hec_apm_guid
                                                                      hec_apm_descr                = ls_landscape-hec_apm_descr
                                                                      hec_srv_inst_type_descr      = lv_serv_inst_type_descr
                                                                      hec_srv_inst_rel_value       = SWITCH #( <fs_tier>-hec_tier_is_dr_node
                                                                                                               WHEN abap_false
                                                                                                               THEN '02'
                                                                                                               ELSE '03'                     )
                                                                      hec_srv_inst_rel_descr       = SWITCH #( <fs_tier>-hec_tier_is_dr_node
                                                                                                               WHEN abap_false
                                                                                                               THEN 'Optional'
                                                                                                               ELSE 'None'                   )
                                                                      hec_db_srv_type_guid         = ls_db_server_type-hec_db_srv_type_guid
                                                                      hec_db_srv_type_value        = ls_db_server_type-hec_db_srv_type_value
                                                                      hec_db_srv_type_descr        = ls_db_server_type-hec_db_srv_type_descr
                                                                      hec_phase_guid               = <fs_tier>-hec_phase_guid
                                                                      hec_phase_fixed              = abap_true
                                                                      hec_phase_assign_allowed     = COND #( WHEN <fs_tier>-hec_phase_guid IS NOT INITIAL
                                                                                                             THEN abap_true
                                                                                                             ELSE abap_false ) "if the parent is not yet assigned, the phase cannot be assigned yet
                                                                      hec_tree_descr               = ls_db_server_type-hec_db_srv_type_descr
                                                                      crea_uname                   = sy-uname ).

              GET TIME STAMP FIELD lr_db_server_inst->crea_date_time.
          ENDCASE.

          INSERT VALUE #( data        = lr_db_server_inst
                          node        = /hec1/if_configuration_c=>sc_node-db_server_instance
                          source_node = /hec1/if_configuration_c=>sc_node-tier
                          association = /hec1/if_configuration_c=>sc_association-tier-db_server_instance
                          source_key  = <fs_tier>-key
                          change_mode = /bobf/if_frw_c=>sc_modify_create
                          key         = lr_db_server_inst->key                                            ) INTO TABLE lt_db_serv_inst_mod.


          CLEAR: ls_related_tier,
                 ls_db_serv_inst_no,
                 ls_db_server_type,
                 ls_db_operating_sys,
                 ls_impl_type,
                 ls_inst_type,
                 ls_allocation,
                 lt_server_type,
                 lt_operating_sys,
                 lt_impl_type,
                 lt_inst_type,
                 lt_alloc,
                 lr_db_server_inst.
        ENDDO. " DO <fs_param>-hec_db_srv_qty TIMES.


        " ***************************************************************************
        " App server instance logic
        " ***************************************************************************
        lv_default_si = abap_true.
        lv_tabix      = 1.

        "-----------------------------------
        " Get default App server instances
        "-----------------------------------
        IF <fs_param>-hec_default_server_inst = abap_true.
          DATA(lt_app_server_inst_no) = VALUE /hec1/t_apm_app_server_inst_no( FOR wa_appsi IN lt_app_serv_inst_no
                                                                              WHERE ( hec_solution_guid       = <fs_tier>-hec_solution_guid                       AND
                                                                                      hec_sol_tier_stack_guid = <fs_tier>-hec_sol_tier_stack_guid                 AND
                                                                                      hec_srv_inst_rel_value  = /hec1/if_config_constants=>gc_relevance-mandatory     )
                                                                             ( wa_appsi )                                                                               ).
        ELSE.
          CLEAR lv_default_si.
        ENDIF. " IF <fs_param>-hec_default_server_inst = abap_true.


        "-----------------------------------
        " " Get Server instance type domain
        "-----------------------------------
        CLEAR lv_serv_inst_type_descr.
        TRY.
            lv_serv_inst_type_descr = lt_dd07v[ domvalue_l = /hec1/if_config_constants=>gc_srv_instance_type-app_server ]-ddtext.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        "-----------------------------------
        " Fill App server instance data
        "-----------------------------------


        " Get App server cluster type
        SELECT SINGLE *
          FROM /hec1/i_appclustertypebasic
         WHERE hec_apm_guid               = @ls_landscape-hec_apm_guid                         AND
               hec_solution_guid          = @<fs_tier>-hec_solution_guid                       AND
               hec_sol_tier_stack_value   = @<fs_tier>-hec_sol_tier_stack_value                AND
               hec_app_cluster_type_value = @/hec1/if_config_constants=>gc_app_clust_node-none AND
               hec_clu_support_stat_value = '02'
          INTO @DATA(ls_app_clust_type).


        DO <fs_param>-hec_app_srv_qty TIMES.
          CASE lv_default_si.
              "-----------------------------------
              " Default app server instance
              "-----------------------------------
            WHEN abap_true.
              TRY.
                  DATA(ls_app_serv_inst_no) = lt_app_server_inst_no[ lv_tabix ].
                CATCH cx_sy_itab_line_not_found.
              ENDTRY.

              DATA(lt_app_oper_system) = VALUE /hec1/t_apm_app_operating_sys( FOR wa_appos IN lt_app_operating_sys
                                                                              WHERE ( hec_sol_tier_stack_si_guid = ls_app_serv_inst_no-hec_sol_tier_stack_si_guid )
                                                                             ( CORRESPONDING #( wa_appos ) )                                                      ).

              IF lines( lt_app_oper_system ) = 1.
                TRY.
                    DATA(ls_app_operating_sys) = lt_app_oper_system[ 1 ].
                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ELSEIF lines( lt_app_oper_system ) > 1.
                READ TABLE lt_app_oper_system WITH KEY hec_operating_sys_value = /hec1/cl_rep_config_data=>c_os_linux INTO ls_app_operating_sys.
              ENDIF.

              DATA(lr_app_server_inst) = NEW /hec1/s_data_app_serv_inst_cs( parent_key                   = <fs_tier>-key
                                                                            key                          = /bopf/cl_frw_factory=>get_new_key( )
                                                                            hec_node_solution            = <fs_tier>-hec_node_solution
                                                                            hec_node_tier                = <fs_tier>-hec_node_tier
                                                                            hec_node_app_serv_inst       = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                            hec_comp_config_id           = ls_landscape-hec_confid
                                                                            hec_comp_config_version      = ls_landscape-hec_conf_version
                                                                            hec_solution_guid            = <fs_tier>-hec_solution_guid
                                                                            hec_tier_cat_value           = <fs_tier>-hec_tier_cat_value
                                                                            hec_sol_tier_stack_guid      = <fs_tier>-hec_sol_tier_stack_guid
                                                                            hec_tier_stack_guid          = <fs_tier>-hec_sol_tier_stack_guid
                                                                            hec_tier_stack_value         = <fs_tier>-hec_sol_tier_stack_value
                                                                            hec_tier_datacenter_guid     = <fs_tier>-hec_tier_datacenter_guid
                                                                            hec_tier_is_dr_node          = <fs_tier>-hec_tier_is_dr_node
                                                                            hec_disaster_rec_option      = <fs_tier>-hec_disaster_rec_option
                                                                            hec_dr_oper_mode_value       = <fs_tier>-hec_dr_oper_mode_value
                                                                            hec_dr_oper_mode_descr       = <fs_tier>-hec_dr_oper_mode_descr
                                                                            hec_apm_guid                 = ls_landscape-hec_apm_guid
                                                                            hec_apm_descr                = ls_landscape-hec_apm_descr
                                                                            hec_srv_inst_type_descr      = lv_serv_inst_type_descr
                                                                            hec_default_app_server_inst  = lv_default_si
                                                                            hec_app_master_node_qty      = 1
                                                                            hec_sol_tier_stack_si_guid   = ls_app_serv_inst_no-hec_sol_tier_stack_si_guid
                                                                            hec_sol_tier_asi_descr       = ls_app_serv_inst_no-hec_sol_tier_asi_descr
                                                                            hec_srv_inst_rel_value       = ls_app_serv_inst_no-hec_srv_inst_rel_value
                                                                            hec_srv_inst_rel_descr       = ls_app_serv_inst_no-hec_srv_inst_rel_descr
                                                                            hec_main_instance            = ls_app_serv_inst_no-hec_main_instance
                                                                            hec_server_required          = ls_app_serv_inst_no-hec_server_required
                                                                            hec_effort_required          = ls_app_serv_inst_no-hec_effort_required
                                                                            hec_backup_relev_value       = SWITCH #( <fs_tier>-hec_tier_is_dr_node
                                                                                                                     WHEN abap_false
                                                                                                                     THEN ls_app_serv_inst_no-hec_backup_relevance
                                                                                                                     ELSE '03'                                     )
                                                                            hec_backup_relev_descr       = SWITCH #( <fs_tier>-hec_tier_is_dr_node
                                                                                                                     WHEN abap_false
                                                                                                                     THEN ls_app_serv_inst_no-hec_backup_relev_descr
                                                                                                                     ELSE 'None'                                     )
                                                                            hec_sol_apsi_oper_sys_guid   = ls_app_operating_sys-hec_sol_apsi_oper_sys_guid
                                                                            hec_operating_sys_guid       = ls_app_operating_sys-hec_operating_sys_guid
                                                                            hec_operating_sys_value      = ls_app_operating_sys-hec_operating_sys_value
                                                                            hec_operating_sys_descr      = ls_app_operating_sys-hec_operating_sys_descr
                                                                            hec_os_support_stat_value    = ls_app_operating_sys-hec_os_support_stat_value
                                                                            hec_os_support_stat_descr    = ls_app_operating_sys-hec_os_support_stat_descr
                                                                            hec_app_serv_type_clust_guid = ls_app_clust_type-hec_app_serv_type_clust_guid
                                                                            hec_sol_apsi_clusttyp_guid   = ls_app_clust_type-hec_sol_apsi_clusttyp_guid
                                                                            hec_app_cluster_type_guid    = ls_app_clust_type-hec_app_serv_type_clust_guid
                                                                            hec_app_cluster_type_value   = ls_app_clust_type-hec_app_cluster_type_value
                                                                            hec_app_cluster_type_descr   = ls_app_clust_type-hec_app_cluster_type_descr
                                                                            hec_clu_support_stat_value   = ls_app_clust_type-hec_clu_support_stat_value
                                                                            hec_clu_support_stat_descr   = ls_app_clust_type-hec_clu_support_stat_descr
                                                                            hec_instance_status          = 'I'
                                                                            hec_phase_guid               = <fs_tier>-hec_phase_guid
                                                                            hec_phase_fixed              = abap_true
                                                                            hec_phase_assign_allowed     = abap_false "for the default server instance the phase is always inherited from the tier
                                                                            hec_tree_descr               = ls_app_serv_inst_no-hec_sol_tier_asi_descr
                                                                            crea_uname                   = sy-uname ).

              GET TIME STAMP FIELD lr_app_server_inst->crea_date_time.

              "-----------------------------------
              " Non default app server instance
              "-----------------------------------
            WHEN abap_false.
              lr_app_server_inst = NEW /hec1/s_data_app_serv_inst_cs( parent_key                   = <fs_tier>-key
                                                                      key                          = /bopf/cl_frw_factory=>get_new_key( )
                                                                      hec_node_solution            = <fs_tier>-hec_node_solution
                                                                      hec_node_tier                = <fs_tier>-hec_node_tier
                                                                      hec_node_app_serv_inst       = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                      hec_comp_config_id           = ls_landscape-hec_confid
                                                                      hec_comp_config_version      = ls_landscape-hec_conf_version
                                                                      hec_solution_guid            = <fs_tier>-hec_solution_guid
                                                                      hec_tier_cat_value           = <fs_tier>-hec_tier_cat_value
                                                                      hec_sol_tier_stack_guid      = <fs_tier>-hec_sol_tier_stack_guid
                                                                      hec_tier_stack_guid          = <fs_tier>-hec_sol_tier_stack_guid
                                                                      hec_tier_stack_value         = <fs_tier>-hec_sol_tier_stack_value
                                                                      hec_tier_datacenter_guid     = <fs_tier>-hec_tier_datacenter_guid
                                                                      hec_tier_is_dr_node          = <fs_tier>-hec_tier_is_dr_node
                                                                      hec_disaster_rec_option      = <fs_tier>-hec_disaster_rec_option
                                                                      hec_dr_oper_mode_value       = <fs_tier>-hec_dr_oper_mode_value
                                                                      hec_dr_oper_mode_descr       = <fs_tier>-hec_dr_oper_mode_descr
                                                                      hec_apm_guid                 = ls_landscape-hec_apm_guid
                                                                      hec_apm_descr                = ls_landscape-hec_apm_descr
                                                                      hec_srv_inst_type_descr      = lv_serv_inst_type_descr
                                                                      hec_srv_inst_rel_value       = SWITCH #( <fs_tier>-hec_tier_is_dr_node
                                                                                                               WHEN abap_false
                                                                                                               THEN '02'
                                                                                                               ELSE '03'                      )
                                                                      hec_srv_inst_rel_descr       = SWITCH #( <fs_tier>-hec_tier_is_dr_node
                                                                                                               WHEN abap_false
                                                                                                               THEN 'Optional'
                                                                                                               ELSE 'None'                    )
                                                                      hec_app_cluster_type_value   = ls_app_clust_type-hec_app_cluster_type_value
                                                                      hec_app_cluster_type_descr   = ls_app_clust_type-hec_app_cluster_type_descr
                                                                      hec_app_master_node_qty      = 1
                                                                      hec_instance_status          = 'I'
                                                                      hec_phase_guid               = <fs_tier>-hec_phase_guid
                                                                      hec_phase_fixed              = abap_false
                                                                      hec_phase_assign_allowed     = COND #( WHEN <fs_tier>-hec_phase_guid IS NOT INITIAL
                                                                                                             THEN abap_true
                                                                                                             ELSE abap_false ) "for non-default app server instance, the phase can be changed if the tier has a phase assigned
                                                                      crea_uname                   = sy-uname ).

              GET TIME STAMP FIELD lr_app_server_inst->crea_date_time.
          ENDCASE.

          INSERT VALUE #( data        = lr_app_server_inst
                          node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                          source_node = /hec1/if_configuration_c=>sc_node-tier
                          association = /hec1/if_configuration_c=>sc_association-tier-app_server_instance
                          source_key  = <fs_tier>-key
                          change_mode = /bobf/if_frw_c=>sc_modify_create
                          key         = lr_app_server_inst->key                                           ) INTO TABLE lt_app_serv_inst_mod.

          CLEAR: ls_app_serv_inst_no,
                 ls_app_operating_sys,
                 ls_app_clust_type,
                 lt_app_oper_system,
                 lr_app_server_inst.

          ADD 1 TO lv_tabix.
        ENDDO.
      ENDIF. " IF <fs_param> IS ASSIGNED.

      CLEAR: lv_serv_inst_type_descr,
             lt_db_server_inst,
             lt_app_server_inst.

      lv_tabix = 1.
    ENDLOOP.


    "-----------------------------------
    " Create DB server instance
    "-----------------------------------
    IF lt_db_serv_inst_mod IS NOT INITIAL.
      io_modify->do_modify( lt_db_serv_inst_mod ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change) ).
    ENDIF.

    "-----------------------------------
    " Create App server instance
    "-----------------------------------
    IF lt_app_serv_inst_mod IS NOT INITIAL.
      io_modify->do_modify( lt_app_serv_inst_mod ).

      CLEAR: lo_message,
             lo_change.

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = lo_message
                                       eo_change              = lo_change ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_software_item.

    " input node is the material

    DATA: ls_landscape        TYPE /hec1/s_config_root_cs,
          lt_tier             TYPE /hec1/t_data_tier_ct,
          lt_solution         TYPE /hec1/t_data_solution_ct,
          lt_material         TYPE /hec1/t_data_material_ct,
          lt_sw_item          TYPE /hec1/t_data_sw_item_ct,
          lt_parameter        TYPE /hec1/t_act_create_sw_item,
          lt_act_param_delete TYPE /bobf/t_frw_node,
          lt_modification     TYPE /bobf/t_frw_modification.

    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO FIELD-SYMBOL(<fs_parameter>).

    IF <fs_parameter> IS INITIAL.
      RETURN. ">>>>
    ENDIF.

    lt_parameter = <fs_parameter>.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = VALUE #( FOR param IN lt_parameter
                                                    ( key = param-parent_key ) )
                       IMPORTING et_data = lt_material ).

    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = VALUE #( FOR param IN lt_parameter
                                                                        ( key = param-parent_key ) )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-material-software_item
                                      IMPORTING et_data        = lt_sw_item ).

    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = VALUE #( FOR param IN lt_parameter
                                                                        ( key = param-parent_key ) )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-material-to_parent
                                      IMPORTING et_data        = lt_tier ).

    "-----------------------------------
    " Get APM model GUID and description
    "-----------------------------------
    /hec1/cl_config_helper=>get_apm_model( EXPORTING iv_node_key   = is_ctx-node_key
                                                     it_key        = it_key
                                                     io_read       = io_read
                                           IMPORTING et_failed_key = et_failed_key
                                                     es_apm_model  = ls_landscape ).


    " Get Software Item List
    DATA(lt_sw_item_list) = /hec1/cl_config_sw_helper=>get_instance( )->/hec1/if_config_sw_helper~get_software_item_list( ).

    LOOP AT lt_parameter ASSIGNING FIELD-SYMBOL(<fs_parameter_line>).

      TRY.
          DATA(ls_material) = lt_material[ key = <fs_parameter_line>-parent_key ].
          DATA(ls_tier)     = lt_tier[ key = ls_material-parent_key ].
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.

      " add all materials
      LOOP AT lt_sw_item_list ASSIGNING FIELD-SYMBOL(<fs_sw_item_list>) "#EC CI_SORTSEQ
        WHERE hec_node_solution       = ls_material-hec_node_solution    AND "#EC CI_SORTSEQ
              hec_material_guid       = ls_material-hec_material_guid    AND
              hec_sw_selection        = abap_true.

        IF "( <fs_sw_item_list>-hec_hsp_swi_stack_value = /hec1/if_config_constants=>gc_sw_stack_value-none AND
           "  ls_tier-hec_sol_tier_stack_value = /hec1/if_config_constants=>gc_sw_stack_value-all )
           " OR
           ( <fs_sw_item_list>-hec_hsp_swi_stack_value = /hec1/if_config_constants=>gc_sw_stack_value-java AND
             ls_tier-hec_sol_tier_stack_value = /hec1/if_config_constants=>gc_sw_stack_value-abap )
            OR
           ( <fs_sw_item_list>-hec_hsp_swi_stack_value = /hec1/if_config_constants=>gc_sw_stack_value-abap AND
             ls_tier-hec_sol_tier_stack_value = /hec1/if_config_constants=>gc_sw_stack_value-java ).
          CONTINUE. ">>>> Skip loop
        ENDIF.

        " **************
        " add software item
        " **************
        " check if software item exists

        IF NOT line_exists( lt_sw_item[ hec_node_solution = <fs_sw_item_list>-hec_node_solution
                                        hec_material_guid = <fs_sw_item_list>-hec_material_guid ] ).

          " If tier price for solution(S/4 on premise, SAP BW etc.) exist, only optional solution materials
          " get a price, else mandatory solution materials gets not a price
          DATA(lv_get_pricing) = COND #( WHEN ls_material-hec_material_rel_value = /hec1/if_config_constants=>gc_material_rel-mandatory
                                         THEN abap_false
                                         ELSE COND #( WHEN ls_material-hec_material_rel_value = /hec1/if_config_constants=>gc_material_rel-optional
                                                      THEN abap_true
                                                      ELSE abap_true                                                                                ) ).

          IF lv_get_pricing = abap_true.
            " Get effort building block GUID
            SELECT SINGLE hec_timebased_effort_bb_guid
              FROM /hec1/i_softwareitemtbbbbasic
               INTO @DATA(lv_effort_bb_guid)
              WHERE hec_apm_guid           = @ls_landscape-hec_apm_guid
                AND hec_hsp_swi_stack_guid = @<fs_sw_item_list>-hec_hsp_swi_stack_guid
                AND hec_tier_cat_value     = @ls_tier-hec_tier_cat_value.
          ENDIF.


          DATA(lr_sw_item_new) = NEW /hec1/s_data_sw_item_cs( BASE CORRESPONDING #( <fs_sw_item_list> )
                                                                     parent_key               = ls_material-key
                                                                     key                      = /bopf/cl_frw_factory=>get_new_key( )
                                                                     hec_node_solution        = ls_material-hec_node_solution
                                                                     hec_node_tier            = ls_material-hec_node_tier
                                                                     hec_node_material        = ls_material-hec_node_material
                                                                     hec_node_sw_item         = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                     hec_comp_config_id       = ls_landscape-hec_confid
                                                                     hec_comp_config_version  = ls_landscape-hec_conf_version
                                                                     hec_row_selectable       = abap_true
                                                                     hec_apm_guid             = ls_material-hec_apm_guid
                                                                     hec_apm_descr            = ls_material-hec_apm_descr
                                                                     hec_phase_guid           = ls_material-hec_phase_guid
                                                                     hec_phase_fixed          = COND #( WHEN <fs_sw_item_list>-hec_sw_item_mat_rel_value = /hec1/if_config_constants=>gc_material_rel-mandatory " '01'
                                                                                                        THEN abap_true
                                                                                                        ELSE abap_false )
                                                                     hec_phase_assign_allowed = COND #( WHEN <fs_sw_item_list>-hec_sw_item_mat_rel_value = /hec1/if_config_constants=>gc_material_rel-mandatory " '01'
                                                                                                        THEN abap_false
                                                                                                        ELSE abap_true )
                                                                     hec_phase_changed        = abap_true
                                                                     price                    = COND #( WHEN lv_effort_bb_guid IS NOT INITIAL
                                                                                                        THEN /hec1/cl_config_helper=>do_price_validation( iv_node_key          = is_ctx-node_key
                                                                                                                                                          it_key               = it_key
                                                                                                                                                          io_read              = io_read
                                                                                                                                                          iv_effort_bb_guid    = lv_effort_bb_guid
                                                                                                                                                          iv_tier_is_dr_node   = ls_tier-hec_tier_is_dr_node
                                                                                                                                                          iv_dr_operating_mode = ls_tier-hec_dr_oper_mode_value )
                                                                                                        ELSE space                                                                                )
                                                                     crea_uname              = sy-uname                                                                                              ).

          GET TIME STAMP FIELD lr_sw_item_new->crea_date_time.


          INSERT VALUE #( data        = lr_sw_item_new
                          node        = /hec1/if_configuration_c=>sc_node-software_item
                          source_node = /hec1/if_configuration_c=>sc_node-material
                          association = /hec1/if_configuration_c=>sc_association-material-software_item
                          source_key  = ls_material-key
                          change_mode = /bobf/if_frw_c=>sc_modify_create
                          key         = lr_sw_item_new->key )
                          INTO TABLE lt_modification.

        ENDIF.  "IF NOT line_exists( lt_sw_item[ hec_node_solution = <fs_sw_item_list>-hec_node_solution

        CLEAR: lv_get_pricing,
               lv_effort_bb_guid.

      ENDLOOP. "LOOP AT lt_sw_item_list ASSIGNING FIELD-SYMBOL(<fs_sw_item_list>)
    ENDLOOP. "LOOP AT lt_parameter ASSIGNING FIELD-SYMBOL(<fs_parameter_line>).

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change) ).
    ENDIF.

    "-----------------------------------
    " Set Delete action to GENERAL
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


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_tier.

    DATA: lt_solution     TYPE /hec1/t_data_solution_ct,
          lt_root_key     TYPE /bobf/t_frw_key,
          ls_landscape    TYPE /hec1/s_config_root_cs,
          lt_modification TYPE /bobf/t_frw_modification.

    FIELD-SYMBOLS: <fs_create_tier> TYPE /hec1/t_act_create_tier.

    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_create_tier>.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_solution     ).

    "-----------------------------------
    " Get APM model GUID and description
    "-----------------------------------
    /hec1/cl_config_helper=>get_apm_model( EXPORTING iv_node_key   = is_ctx-node_key
                                                     it_key        = it_key
                                                     io_read       = io_read
                                           IMPORTING et_failed_key = et_failed_key
                                                     es_apm_model  = ls_landscape    ).


    LOOP AT lt_solution ASSIGNING FIELD-SYMBOL(<fs_solution>).
      ASSIGN <fs_create_tier>[ key = <fs_solution>-key ] TO FIELD-SYMBOL(<fs_new_tier_no>).

      IF <fs_new_tier_no> IS ASSIGNED.
        "-----------------------------------
        " Get number of stack tiers
        " per tier level
        "-----------------------------------
        SELECT SINGLE hec_sol_tier_stack_no
          FROM /hec1/i_solutionbasic
         WHERE hec_apm_guid      = @ls_landscape-hec_apm_guid       AND
               hec_solution_guid = @<fs_solution>-hec_solution_guid
          INTO @DATA(lv_stack_tier_no).

        IF lv_stack_tier_no IS INITIAL.
          lv_stack_tier_no = 1.
        ENDIF.

        "-----------------------------------
        " Fill data for new non productiv
        " tiers
        "-----------------------------------
        IF <fs_new_tier_no>-hec_tier_qty_nprod_level > 0.

          APPEND LINES OF
         /hec1/cl_config_action_helper=>/hec1/if_bopf_action_helper~create_tier( iv_create_no_tier      = CONV #( <fs_new_tier_no>-hec_tier_qty_nprod_level )        " No. of tiers to be created
                                                                                 iv_stack_tier_no       = lv_stack_tier_no                                           " Number of Stack Tiers
                                                                                 iv_tier_category_value = /hec1/if_config_constants=>gc_tier_category-nonprod        " Tier Category Value
                                                                                 is_landscape           = REF #( ls_landscape )                                      " Landscape
                                                                                 is_solution            = REF #( <fs_solution> )                                     " Solution
                                                                                 io_read                = io_read                                              )
        TO lt_modification.
        ENDIF.

        "-----------------------------------
        " Fill data for new productiv tier
        "-----------------------------------
        IF <fs_new_tier_no>-hec_tier_qty_prod_level > 0.

          APPEND LINES OF
         /hec1/cl_config_action_helper=>/hec1/if_bopf_action_helper~create_tier( iv_create_no_tier      = CONV #( <fs_new_tier_no>-hec_tier_qty_prod_level )         " No. of tiers to be created
                                                                                 iv_stack_tier_no       = lv_stack_tier_no                                           " Number of Stack Tiers
                                                                                 iv_tier_category_value = /hec1/if_config_constants=>gc_tier_category-prod           " Tier Category Value
                                                                                 is_landscape           = REF #( ls_landscape )                                      " Landscape
                                                                                 is_solution            = REF #( <fs_solution> )                                     " Solution
                                                                                 io_read                = io_read                                            )
        TO lt_modification.
        ENDIF.
      ENDIF. " IF <fs_new_tier_no> IS ASSIGNED.

      CLEAR lv_stack_tier_no.
      UNASSIGN <fs_new_tier_no>.
    ENDLOOP.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).

    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_tier_software.



  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_db_server_instance.

    DATA: lt_modification       TYPE /bobf/t_frw_modification,
          lt_db_server_instance TYPE /hec1/t_data_db_server_inst_ct,
          lt_solution           TYPE /hec1/t_data_solution_ct.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node      = is_ctx-node_key
                                 it_key       = it_key
                                 iv_fill_data = abap_true
                       IMPORTING et_data      = lt_db_server_instance ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                it_key         = VALUE #( FOR db_si IN lt_db_server_instance
                                                                        ( key = db_si-parent_key ) )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier-to_parent
                                      IMPORTING et_data        = lt_solution
                                                et_key_link    = DATA(lt_tier_sol_link) ).


*    LOOP AT lt_db_server_instance REFERENCE INTO DATA(lr_db_server_instance).
*      "-----------------------------------
*      " Fill DB server update structure
*      "-----------------------------------
*      TRY.
*          DATA(ls_solution) = lt_solution[ key = lt_tier_sol_link[ source_key = lr_db_server_instance->parent_key ]-target_key ].
*          lr_db_server_instance->hec_db_encrypted = ls_solution-hec_sol_db_encrypted.
*        CATCH cx_sy_itab_line_not_found.
*      ENDTRY.
*
*      INSERT VALUE #( data        = lr_db_server_instance
*                      node        = /hec1/if_configuration_c=>sc_node-db_server_instance
*                      source_key  = lr_db_server_instance->key
*                      change_mode = /bobf/if_frw_c=>sc_modify_update
*                      key         = lr_db_server_instance->key                           ) INTO TABLE lt_modification.
*
*    ENDLOOP. " IF <fs_act_param> IS ASSIGNED.

    "-----------------------------------
    " Update instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_tier_from_landscape.

" This method is triggered from the landscape level. All tiers are updated.

    DATA: lt_root         TYPE /hec1/t_config_root_ct,
          lt_tier         TYPE /hec1/t_data_tier_ct,
          lt_modification TYPE /bobf/t_frw_modification,
          ls_act_param    TYPE /hec1/s_act_update_tier_inhrit.

    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO FIELD-SYMBOL(<fs_param>).

    IF <fs_param> IS ASSIGNED.
      ls_act_param = <fs_param>.
    ENDIF.

    io_read->retrieve( EXPORTING iv_node    = is_ctx-node_key
                                 it_key     = it_key
                       IMPORTING et_data    = lt_root ).

    " Solution
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-solution
                                      IMPORTING et_target_key  = DATA(lt_solution_key) ).

    " Tier
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-solution
                                                it_key         = lt_solution_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                      IMPORTING et_data        = lt_tier  ).

    DATA(ls_root) = VALUE #( lt_root[ 1 ] OPTIONAL ).

    LOOP AT lt_tier REFERENCE INTO DATA(lr_tier).

      " Update Timezone
      IF ls_act_param-do_update_timezone = abap_true.

        lr_tier->hec_system_timezone = ls_root-hec_system_timezone.

      ENDIF.

      " Update Non-Production Recurrence
      IF ls_act_param-do_update_nonprod = abap_true
        AND lr_tier->hec_tier_cat_value = /hec1/if_config_constants=>gc_tier_category-nonprod.

        lr_tier->hec_tier_recurrence_type = ls_root-hec_nprod_recurrence_type.
        lr_tier->hec_tier_recurrence_interval = ls_root-hec_nprod_recurrence_interval.
        lr_tier->hec_tier_weekday = ls_root-hec_nprod_weekday.

        lr_tier->hec_tier_starttime = ls_root-hec_nprod_starttime.
        lr_tier->hec_tier_duration = ls_root-hec_nprod_duration.
        lr_tier->hec_tier_duration_unit = ls_root-hec_nprod_duration_unit.
        lr_tier->hec_tier_cmp_timezone = ls_root-hec_nprod_cmp_timezone.

      ENDIF.

      " Update Production Recurrence
      IF ls_act_param-do_update_prod = abap_true
        AND lr_tier->hec_tier_cat_value = /hec1/if_config_constants=>gc_tier_category-prod.

        lr_tier->hec_tier_recurrence_type = ls_root-hec_prod_recurrence_type.
        lr_tier->hec_tier_recurrence_interval = ls_root-hec_prod_recurrence_interval.
        lr_tier->hec_tier_weekday = ls_root-hec_prod_weekday.

        lr_tier->hec_tier_starttime = ls_root-hec_prod_starttime.
        lr_tier->hec_tier_duration = ls_root-hec_prod_duration.
        lr_tier->hec_tier_duration_unit = ls_root-hec_prod_duration_unit.
        lr_tier->hec_tier_cmp_timezone = ls_root-hec_prod_cmp_timezone.

      ENDIF.

      "-----------------------------------
      " Insert Tier data to modification table
      "-----------------------------------
      INSERT VALUE #( data        = lr_tier
                      node        = /hec1/if_configuration_c=>sc_node-tier
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_tier->key
                      ) INTO TABLE lt_modification.

    ENDLOOP.

    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_app_server.

    DATA: lt_modification      TYPE /bobf/t_frw_modification,
          lt_app_serv_perf_cat TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_server        TYPE /hec1/t_data_app_serv_ct.

    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_update_app_server.



    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_act_param>.

    io_read->retrieve( EXPORTING iv_node    = is_ctx-node_key
                                 it_key     = it_key
                       IMPORTING et_data    = lt_app_serv_perf_cat ).

    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_server
                                      IMPORTING et_data        = lt_app_server                                                              ).


    IF lt_app_server IS INITIAL.
      RETURN. ">>>>>>
    ENDIF.

    IF <fs_act_param> IS ASSIGNED.
      "-----------------------------------
      " Fill APP server update structure
      "-----------------------------------
      LOOP AT lt_app_serv_perf_cat ASSIGNING FIELD-SYMBOL(<fs_serv_perf_cat>).

        TRY.
            DATA(ls_act_param) = <fs_act_param>[ parent_key = <fs_serv_perf_cat>-key ].

            IF ls_act_param-do_update_app_server = abap_true.
              DATA(lr_app_server) = NEW /hec1/s_data_app_serv_cs( lt_app_server[ key = ls_act_param-key ] ).
              " Update IP Server GUID
              lr_app_server->hec_ip_server_guid = ls_act_param-hec_ip_server_guid.
              DATA(lv_data_changed) = abap_true.
            ENDIF.

            "-----------------------------------
            " Fill App server update structure
            "-----------------------------------
            IF lv_data_changed = abap_true.
              INSERT VALUE #( data        = lr_app_server
                              node        = /hec1/if_configuration_c=>sc_node-app_server
                              source_node = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                              association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_server
                              source_key  = lr_app_server->parent_key
                              change_mode = /bobf/if_frw_c=>sc_modify_update
                              key         = lr_app_server->key                                                          ) INTO TABLE lt_modification.
            ENDIF.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        CLEAR: lv_data_changed,
               ls_act_param,
               lr_app_server.
      ENDLOOP.
    ENDIF. " IF <fs_act_param> IS ASSIGNED.

    "-----------------------------------
    " Update instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_tier_lt_backup.

    DATA: lt_modification   TYPE /bobf/t_frw_modification,
          ls_act_param      TYPE /hec1/s_act_update_tier_ltb,
          lt_tier_lt_backup TYPE /hec1/t_data_tier_lt_backup_ct.

    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO FIELD-SYMBOL(<fs_param>).

    IF <fs_param> IS ASSIGNED.
      ls_act_param = <fs_param>.
    ENDIF.

    io_read->get_root_key(
      EXPORTING iv_node         = is_ctx-node_key
                it_key          = it_key
      IMPORTING et_target_key   = DATA(lt_root_key) ).

    " Solution
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = lt_root_key
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-solution
                                      IMPORTING et_target_key  = DATA(lt_solution_key) ).

    " Tier
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-solution
                                                it_key         = lt_solution_key
                                                iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                      IMPORTING et_target_key  = DATA(lt_tier_key)  ).

    " TIER_LT_BACKUP
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                it_key         = lt_tier_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier-tier_longterm_backup
                                      IMPORTING et_data        = lt_tier_lt_backup ).

    LOOP AT lt_tier_lt_backup REFERENCE INTO DATA(lr_tier_lt_backup)
        WHERE hec_tlt_backup_cl_node_ref = ls_act_param-hec_node_lt_backup_class.

      lr_tier_lt_backup->hec_tlt_backup_ref_descr     = ls_act_param-hec_ltb_class_descr.
      lr_tier_lt_backup->hec_tlt_backup_ref_descr_ext = ls_act_param-hec_ltb_class_descr_ext.

      "-----------------------------------
      " Insert Tier data to modification table
      "-----------------------------------
      INSERT VALUE #( data        = lr_tier_lt_backup
                      node        = /hec1/if_configuration_c=>sc_node-tier_longterm_backup
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_tier_lt_backup->key
                      ) INTO TABLE lt_modification.

    ENDLOOP.

    "-----------------------------------
    " Do Modify
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_connectivity.

    "triggered from datacenter

    DATA: lt_datacenter   TYPE /hec1/t_data_datacenter_ct,
          lt_connectivity TYPE /hec1/t_data_connectivity_ct,
          lt_modification TYPE /bobf/t_frw_modification,
          ls_landscape    TYPE /hec1/s_config_root_cs.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node      = is_ctx-node_key
                                 it_key       = it_key
                                 iv_fill_data = abap_true
                       IMPORTING et_data      = lt_datacenter ).


    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_association = /hec1/if_configuration_c=>sc_association-datacenter-connectivity
                                                iv_fill_data   = abap_true
                                      IMPORTING et_data        = lt_connectivity ).


    /hec1/cl_config_helper=>get_apm_model( EXPORTING iv_node_key   = is_ctx-node_key
                                                     it_key        = it_key
                                                     io_read       = io_read
                                           IMPORTING es_apm_model  = ls_landscape    ).



    LOOP AT lt_datacenter ASSIGNING FIELD-SYMBOL(<fs_datacenter>).

      LOOP AT lt_connectivity REFERENCE INTO DATA(lr_connectivity)
        WHERE parent_key = <fs_datacenter>-key.

        IF <fs_datacenter>-hec_sec_datacenter_guid IS INITIAL.
          CLEAR: lr_connectivity->hec_sec_datacenter_guid,
                 lr_connectivity->hec_connectivity_descr,
                 lr_connectivity->hec_connectivity_guid,
                 lr_connectivity->price.
        ELSE.
          lr_connectivity->hec_sec_datacenter_guid = <fs_datacenter>-hec_sec_datacenter_guid.
        ENDIF.

        IF lr_connectivity->hec_apm_guid IS INITIAL.
          lr_connectivity->hec_apm_guid  = ls_landscape-hec_apm_guid.
          lr_connectivity->hec_apm_descr = ls_landscape-hec_apm_descr.
        ENDIF.

        INSERT VALUE #( data        = lr_connectivity
                        node        = /hec1/if_configuration_c=>sc_node-connectivity
                        change_mode = /bobf/if_frw_c=>sc_modify_update
                        key         = lr_connectivity->key                           ) INTO TABLE lt_modification.

      ENDLOOP. " LOOP AT lt_connectivity REFERENCE INTO DATA(lr_connectivity)
    ENDLOOP. " LOOP AT lt_datacenter ASSIGNING FIELD-SYMBOL(<fs_datacenter>).


    "-----------------------------------
    " Do Modify
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message) ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_landscape.

    DATA: lt_modification TYPE /bobf/t_frw_modification,
          lt_root         TYPE /hec1/t_config_root_ct.

    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/s_act_update_landscape.

    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_act_param>.

    " Get landscape( APM GUID), delivery unit and data center
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    IF lr_landscape IS INITIAL.
      RETURN. ">>>>>>
    ENDIF.

    IF <fs_act_param> IS ASSIGNED.

      IF <fs_act_param>-do_update_region = abap_true.

        /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_region_dlvyunit_datacenter( EXPORTING it_country_key    = VALUE #( FOR datacenter IN lt_datacenter
                                                                                                                                            ( datacenter-hec_datacenter_country ) )
                                                                                                       IMPORTING et_region_l1      = DATA(lt_region_l1)
                                                                                                                 et_region_l2      = DATA(lt_region_l2)
                                                                                                                 et_region_l3      = DATA(lt_region_l3) ).

        SORT lt_region_l1 ASCENDING.
        DELETE ADJACENT DUPLICATES FROM lt_region_l1.

        SORT lt_region_l2 ASCENDING.
        DELETE ADJACENT DUPLICATES FROM lt_region_l2.

        SORT lt_region_l3 ASCENDING.
        DELETE ADJACENT DUPLICATES FROM lt_region_l3.

        IF lines( lt_region_l1 ) = 1.
          DATA(ls_region_l1) = VALUE #( lt_region_l1[ 1 ] OPTIONAL ).
          lr_landscape->hec_dlvy_region_l1_guid = ls_region_l1-value.
          lr_landscape->hec_dlvy_region_l1_descr = ls_region_l1-text.
        ELSE.
          lr_landscape->hec_dlvy_region_l1_guid = '00'.
        ENDIF.

        IF lines( lt_region_l2 ) = 1.
          DATA(ls_region_l2) = VALUE #( lt_region_l2[ 1 ] OPTIONAL ).
          lr_landscape->hec_dlvy_region_l2_guid = ls_region_l2-value.
          lr_landscape->hec_dlvy_region_l2_descr = ls_region_l2-text.
        ELSE.
          lr_landscape->hec_dlvy_region_l2_guid = '00'.
        ENDIF.

        IF lines( lt_region_l3 ) = 1.
          DATA(ls_region_l3) = VALUE #( lt_region_l3[ 1 ] OPTIONAL ).
          lr_landscape->hec_country_key = ls_region_l3-value.
          lr_landscape->hec_country_descr = ls_region_l3-text.
        ELSE.
          lr_landscape->hec_country_key = '00'.
        ENDIF.

        INSERT VALUE #( data        = lr_landscape
                        node        = /hec1/if_configuration_c=>sc_node-root
                        change_mode = /bobf/if_frw_c=>sc_modify_update
                        key         = lr_landscape->key
                        ) INTO TABLE lt_modification.

      ENDIF. "do_update_region

    ENDIF.  "<fs_act_param> is assigned.

    "-----------------------------------
    " Update
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_instance_db.

    DATA: lt_modification TYPE /bobf/t_frw_modification,
          lt_instance_db  TYPE /hec1/t_data_db_inst_ct.

    FIELD-SYMBOLS: <fs_act_param> TYPE /hec1/t_act_update_instance_db.

    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_act_param>.

    CHECK <fs_act_param> IS ASSIGNED.

    io_read->retrieve( EXPORTING iv_node      = /hec1/if_configuration_c=>sc_node-instance_db
                                 it_key       = VALUE #( FOR wa IN <fs_act_param>
                                                       ( key = wa-key ) )
                                 iv_fill_data = abap_true
                       IMPORTING et_data      = lt_instance_db ).

    LOOP AT <fs_act_param> ASSIGNING FIELD-SYMBOL(<fs_act_param_line>).

      IF <fs_act_param_line>-do_update_multi_tenancy_guid = abap_true.

        DATA(lr_instance_db) = NEW /hec1/s_data_db_inst_cs( lt_instance_db[ key = <fs_act_param_line>-key ] ).

        IF <fs_act_param_line>-do_update_multi_tenancy_guid = abap_true.

          lr_instance_db->hec_multi_tenant_rel_guid = <fs_act_param_line>-hec_multi_tenant_rel_guid.

          INSERT VALUE #( data        = lr_instance_db
                          node        = /hec1/if_configuration_c=>sc_node-instance_db
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_instance_db->key
                          ) INTO TABLE lt_modification.

        ENDIF. "<fs_act_param_line>-do_update_multi_tenancy_guid = abap_true.

      ENDIF.

    ENDLOOP.

    "-----------------------------------
    " Update instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~create_tier_sla.

    DATA: lt_tier         TYPE /hec1/t_data_tier_ct,
          lt_root_key     TYPE /bobf/t_frw_key,
          ls_landscape    TYPE /hec1/s_config_root_cs,
          lt_modification TYPE /bobf/t_frw_modification.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_tier ).

    "-----------------------------------
    " Get APM model GUID and description
    "-----------------------------------
    /hec1/cl_config_helper=>get_apm_model( EXPORTING iv_node_key   = is_ctx-node_key
                                                     it_key        = it_key
                                                     io_read       = io_read
                                           IMPORTING et_failed_key = et_failed_key
                                                     es_apm_model  = ls_landscape    ).

    LOOP AT lt_tier ASSIGNING FIELD-SYMBOL(<fs_tier>).

      DATA(lr_tier_sla_new) = NEW /hec1/s_data_tier_sla_cs( BASE CORRESPONDING #( <fs_tier> )
                                                                 parent_key               = <fs_tier>-key
                                                                 key                      = /bopf/cl_frw_factory=>get_new_key( )
                                                                 hec_node_solution        = <fs_tier>-hec_node_solution
                                                                 hec_node_tier            = <fs_tier>-hec_node_tier
                                                                 hec_node_tier_sla        = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                 hec_comp_config_id       = ls_landscape-hec_confid
                                                                 hec_comp_config_version  = ls_landscape-hec_conf_version
                                                                 hec_row_selectable       = abap_true
                                                                 hec_apm_guid             = <fs_tier>-hec_apm_guid
                                                                 hec_apm_descr            = <fs_tier>-hec_apm_descr
                                                                 hec_phase_guid           = <fs_tier>-hec_phase_guid
                                                                 hec_phase_fixed          = abap_true
                                                                 hec_phase_assign_allowed = abap_false
                                                                 hec_phase_changed        = abap_true
                                                                 crea_uname               = sy-uname                                     ).

      GET TIME STAMP FIELD lr_tier_sla_new->crea_date_time.

      INSERT VALUE #( data        = lr_tier_sla_new
                      node        = /hec1/if_configuration_c=>sc_node-tier_sla
                      source_node = /hec1/if_configuration_c=>sc_node-tier
                      association = /hec1/if_configuration_c=>sc_association-tier-tier_sla
                      source_key  = lr_tier_sla_new->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = lr_tier_sla_new->key )
                      INTO TABLE lt_modification.

    ENDLOOP.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).

    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_db_storage_backup.

    DATA: lt_db_storage   TYPE /hec1/t_data_db_storage_ct,
          lt_db_backup    TYPE /hec1/t_data_db_backup_ct,
          lt_modification TYPE /bobf/t_frw_modification.

    FIELD-SYMBOLS: <fs_param> TYPE /hec1/t_act_update_db_backup.

    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_param>.

    CHECK <fs_param> IS ASSIGNED.

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    io_read->retrieve( EXPORTING iv_node       = /hec1/if_configuration_c=>sc_node-db_storage
                                 it_key        = VALUE #( FOR param IN <fs_param>
                                                        ( key = param-parent_key ) )
                       IMPORTING et_data       = lt_db_storage ).

    " DB Storage Amount (child)
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_storage
                                                it_key         = VALUE #( FOR param IN <fs_param>
                                                                        ( key = param-parent_key ) )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_storage-db_storage_backup
                                      IMPORTING et_data        = lt_db_backup                                                                ).

    " Here we loop across the storage backup, which is the parent
    " The update can be executed from the storage and then needs to run for all child nodes
    LOOP AT lt_db_storage ASSIGNING FIELD-SYMBOL(<fs_db_storage>).

      LOOP AT lt_db_backup
        REFERENCE INTO DATA(lr_db_backup)
        WHERE parent_key = <fs_db_storage>-key.

        "-----------------------------------
        " Clear Phasing
        "-----------------------------------
        IF line_exists( <fs_param>[ do_clear_phasing = abap_true
                                    key              = lr_db_backup->key ] ).


          IF lines( lt_db_backup ) = 1.
            " Get Parent Phase
            TRY.
                DATA(ls_db_storage) = lt_db_storage[ key = lr_db_backup->parent_key ].

                lr_db_backup->hec_phase_guid = ls_db_storage-hec_phase_guid.
                lr_db_backup->hec_phase_assign_allowed = abap_false.
                lr_db_backup->hec_phase_changed = abap_true.
                lr_db_backup->hec_phase_fixed = abap_true.

              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

          ELSE.

            CLEAR: lr_db_backup->hec_phase_guid,
                   lr_db_backup->hec_phase_fixed.

            lr_db_backup->hec_phase_changed = abap_true.

          ENDIF. "lines(lt_db_storage_qty) = 1

        ENDIF. "do_clear_phasing

        INSERT VALUE #( data        = lr_db_backup
                        node        = /hec1/if_configuration_c=>sc_node-db_storage_backup
                        change_mode = /bobf/if_frw_c=>sc_modify_update
                        key         = lr_db_backup->key
                        ) INTO TABLE lt_modification.

      ENDLOOP. "lt_db_storage_qty
    ENDLOOP. "lt_db_serv_pc

    "-----------------------------------
    " Do Modify
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message) ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_app_storage_backup.

    DATA: lt_app_storage  TYPE /hec1/t_data_app_storage_ct,
          lt_app_backup   TYPE /hec1/t_data_app_backup_ct,
          lt_modification TYPE /bobf/t_frw_modification.

    FIELD-SYMBOLS: <fs_param> TYPE /hec1/t_act_update_app_backup.

    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_param>.

    CHECK <fs_param> IS ASSIGNED.

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter)
                                                        et_failed_key    = et_failed_key ).

    io_read->retrieve( EXPORTING iv_node       = /hec1/if_configuration_c=>sc_node-app_storage
                                 it_key        = VALUE #( FOR param IN <fs_param>
                                                        ( key = param-parent_key ) )
                       IMPORTING et_data       = lt_app_storage ).

    " DB Storage Amount (child)
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_storage
                                                it_key         = VALUE #( FOR param IN <fs_param>
                                                                        ( key = param-parent_key ) )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_storage-app_storage_backup
                                      IMPORTING et_data        = lt_app_backup                                                                ).

    " Here we loop across the storage backup, which is the parent
    " The update can be executed from the storage and then needs to run for all child nodes
    LOOP AT lt_app_storage ASSIGNING FIELD-SYMBOL(<fs_app_storage>).

      LOOP AT lt_app_backup
        REFERENCE INTO DATA(lr_app_backup)
        WHERE parent_key = <fs_app_storage>-key.

        "-----------------------------------
        " Clear Phasing
        "-----------------------------------
        IF line_exists( <fs_param>[ do_clear_phasing = abap_true
                                    key              = lr_app_backup->key ] ).


          IF lines( lt_app_backup ) = 1.
            " Get Parent Phase
            TRY.
                DATA(ls_app_storage) = lt_app_storage[ key = lr_app_backup->parent_key ].

                lr_app_backup->hec_phase_guid = ls_app_storage-hec_phase_guid.
                lr_app_backup->hec_phase_assign_allowed = abap_false.
                lr_app_backup->hec_phase_changed = abap_true.
                lr_app_backup->hec_phase_fixed = abap_true.

              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

          ELSE.

            CLEAR: lr_app_backup->hec_phase_guid,
                   lr_app_backup->hec_phase_fixed.

            lr_app_backup->hec_phase_changed = abap_true.

          ENDIF. "lines(lt_app_storage_qty) = 1

        ENDIF. "do_clear_phasing

        INSERT VALUE #( data        = lr_app_backup
                        node        = /hec1/if_configuration_c=>sc_node-app_storage_backup
                        change_mode = /bobf/if_frw_c=>sc_modify_update
                        key         = lr_app_backup->key
                        ) INTO TABLE lt_modification.

      ENDLOOP. "lt_app_storage_qty
    ENDLOOP. "lt_app_serv_pc

    "-----------------------------------
    " Do Modify
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message) ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_config_action_intern~update_tier_add_service.

    DATA: lt_modification     TYPE /bobf/t_frw_modification,
          lt_act_param        TYPE /hec1/t_act_update_t_add_serv,
          lt_tier_add_service TYPE /hec1/t_data_tier_add_serv_ct,
          lt_add_service      TYPE /hec1/t_data_add_services_ct.

    FIELD-SYMBOLS: <fs_param> TYPE /hec1/t_act_update_t_add_serv.

    CLEAR: eo_message,
           et_failed_key.

    ASSIGN ir_parameter->* TO <fs_param>.

    CHECK <fs_param> IS ASSIGNED.

    io_read->get_root_key( EXPORTING iv_node         = is_ctx-node_key
                                     it_key          = it_key
                           IMPORTING et_target_key   = DATA(lt_root_key) ).

    " Additional Service
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = lt_root_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-add_service
                                      IMPORTING et_data        = lt_add_service ).

    " Tier Add Service
    io_read->retrieve( EXPORTING iv_node   = is_ctx-node_key
                                 it_key    = it_key
                       IMPORTING et_data   = lt_tier_add_service ).

    LOOP AT lt_tier_add_service REFERENCE INTO DATA(lr_tier_add_service).

      IF line_exists( <fs_param>[ key               = lr_tier_add_service->key
                                  do_update_service = abap_true ] ).

        TRY.
            DATA(ls_add_service) = lt_add_service[ hec_node_service = lr_tier_add_service->hec_tas_service_ref_guid ].

            IF lr_tier_add_service->hec_tas_service_ref_descr_ext IS INITIAL.
              lr_tier_add_service->hec_tas_service_ref_descr_ext = ls_add_service-hec_as_class_descr_ext.
            ENDIF.
            lr_tier_add_service->* = VALUE #( BASE lr_tier_add_service->*
                                         hec_tas_service_ref_descr = ls_add_service-hec_ip_as_class_descr
                                         hec_tas_tier_uplift_perc  = ls_add_service-hec_as_tier_uplift_perc
                                         hec_tree_descr            = COND #( WHEN lr_tier_add_service->hec_tas_service_ref_descr_ext IS INITIAL
                                                                             THEN ls_add_service-hec_ip_as_class_descr
                                                                             ELSE |{ ls_add_service-hec_ip_as_class_descr } : { lr_tier_add_service->hec_tas_service_ref_descr_ext }| ) ).

            "-----------------------------------
            " Insert Tier data to modification table
            "-----------------------------------
            INSERT VALUE #( data        = lr_tier_add_service
                            node        = /hec1/if_configuration_c=>sc_node-tier_add_service
                            change_mode = /bobf/if_frw_c=>sc_modify_update
                            key         = lr_tier_add_service->key
                            ) INTO TABLE lt_modification.

          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

      ENDIF. "line_exists do_update_service

    ENDLOOP.

    "-----------------------------------
    " Do Modify
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).
    ENDIF.

  ENDMETHOD.
ENDCLASS.