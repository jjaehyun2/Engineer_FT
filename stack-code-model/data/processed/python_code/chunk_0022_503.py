CLASS /hec1/cl_bopf_config_model DEFINITION
  PUBLIC
  FINAL
  CREATE PRIVATE

  GLOBAL FRIENDS /hec1/cl_bopf_config_model_fac .

  PUBLIC SECTION.

    INTERFACES /hec1/if_bopf_config_model_act .
    INTERFACES /hec1/if_bopf_config_model_get .
    INTERFACES /hec1/if_bopf_config_model_set .
    INTERFACES /hec1/if_bopf_config_model .
    INTERFACES /hec1/if_bopf_config_model_ge .
    INTERFACES /hec1/if_bopf_config_model_se .

    METHODS constructor
      IMPORTING
        !iv_config_id      TYPE /hec1/config_id OPTIONAL
        !iv_config_version TYPE /hec1/config_version OPTIONAL .
  PROTECTED SECTION.
  PRIVATE SECTION.

    DATA mo_data_provider TYPE REF TO /hec1/if_data_provider .
    DATA mv_bo_root_key TYPE /bopf/conf_key .
    DATA mv_bo_landscape_key TYPE /bopf/conf_key .
    DATA mv_bo_dlvy_unit_key TYPE /bopf/conf_key .
    DATA ms_root_key TYPE /hec1/s_key_root .
    DATA mv_landscape_guid TYPE /hec1/landscape_guid .
    DATA mv_delivery_unit_guid TYPE /hec1/delivery_unit_guid .
    DATA mv_man_servic_baseline_guid TYPE /hec1/managed_service_bl_guid .
    DATA mv_create_new_config_version TYPE boole_d .
    DATA ms_config_changes TYPE /hec1/s_bopf_config_changes .

    METHODS copy_to_new_version
      IMPORTING
        !is_config               TYPE /hec1/s_config_root_cs
      EXPORTING
        !ev_new_hec_conf_version TYPE /hec1/config_version
      RETURNING
        VALUE(rv_success)        TYPE boole_d .
    METHODS get_bo_key_by_altern_key
      IMPORTING
        !iv_node_key   TYPE /bobf/obm_node_key
        !iv_altkey_key TYPE /bobf/obm_altkey_key DEFAULT /bobf/if_frw_c=>sc_alternative_key_key
        !it_altkey     TYPE INDEX TABLE
      EXPORTING
        !eo_change     TYPE REF TO /bobf/if_tra_change
        !et_result     TYPE /bobf/t_frw_keyindex
        !et_key        TYPE /bobf/t_frw_key
        !eo_message    TYPE REF TO /bobf/if_frw_message .
    METHODS get_full_name
      IMPORTING
        !iv_uname           TYPE xubname
      RETURNING
        VALUE(rv_full_name) TYPE string .
    METHODS get_next_config_version_number
      IMPORTING
        !iv_config_id            TYPE /hec1/config_id
      RETURNING
        VALUE(rv_config_version) TYPE /hec1/config_version .
    METHODS set_bopf_msg_to_fpm_msg
      IMPORTING
        !io_message TYPE REF TO /bobf/if_frw_message .
ENDCLASS.



CLASS /HEC1/CL_BOPF_CONFIG_MODEL IMPLEMENTATION.


  METHOD /hec1/if_bopf_config_model_set~update_app_server.

    DATA: lt_bo_key          TYPE /bobf/t_frw_key,
          lt_alt_key_app_spc TYPE TABLE OF /hec1/s_key_app_serv_pc,
          ls_alt_key_app_spc LIKE LINE OF lt_alt_key_app_spc,
          lt_alt_key         TYPE TABLE OF /hec1/s_key_app_serv,
          ls_alt_key         LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create instance node App server
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_app_server) = NEW /hec1/s_data_app_serv_cs( ).
        ASSIGN lr_app_server->* TO FIELD-SYMBOL(<fs_app_server>).
        IF <fs_app_server> IS ASSIGNED.
          <fs_app_server> = VALUE #( BASE CORRESPONDING #( is_app_server )
                                     key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_app_spc = CORRESPONDING #( is_app_server-obj_key ).
          INSERT ls_alt_key_app_spc INTO TABLE lt_alt_key_app_spc.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_server_perform_cat-app_server_perform_cat_key
                                                  it_altkey     = lt_alt_key_app_spc
                                        IMPORTING eo_change     = DATA(lo_change)
                                                  et_result     = DATA(lt_result)
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                                                              ).
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_app_server
                                                       node        = /hec1/if_configuration_c=>sc_node-app_server
                                                       source_node = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                       association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_server
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_app_server>-key                                                        ) )
                IMPORTING eo_message      = lo_message                                                                                              ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_app_server> IS ASSIGNED.

        " ****************************************
        " Update instance node App server
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_app_server-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_server
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_server-app_server_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                             ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_app_server = NEW /hec1/s_data_app_serv_cs( ).
        ASSIGN lr_app_server->* TO <fs_app_server>.
        IF <fs_app_server> IS ASSIGNED.
          <fs_app_server> = CORRESPONDING #( is_app_server ).

          " Get fields of structure
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_app_server> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_app_server
                                                        node           = /hec1/if_configuration_c=>sc_node-app_server
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                    ) )
                 IMPORTING eo_message      = lo_message                                                                   ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_app_server> IS ASSIGNED.

        " ****************************************
        " Delete instance node APP server
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_app_server-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_server
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_server-app_server_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                           ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_app_server
                                                      node           = /hec1/if_configuration_c=>sc_node-app_server
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                   ) )
               IMPORTING eo_message      = lo_message                                                                  ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_app_server_inst.

    DATA: lt_bo_key       TYPE /bobf/t_frw_key,
          lt_alt_key_tier TYPE TABLE OF /hec1/s_key_tier,
          ls_alt_key_tier LIKE LINE OF lt_alt_key_tier,
          lt_alt_key      TYPE TABLE OF /hec1/s_key_app_server_inst,
          ls_alt_key      LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create APP server instance instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_app_server_inst) = NEW /hec1/s_data_app_serv_inst_cs( ).
        ASSIGN lr_app_server_inst->* TO FIELD-SYMBOL(<fs_app_server_inst>).
        IF <fs_app_server_inst> IS ASSIGNED.
          <fs_app_server_inst> = VALUE #( BASE CORRESPONDING #( is_app_server_inst )
                                          key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_tier = CORRESPONDING #( is_app_server_inst-obj_key ).
          INSERT ls_alt_key_tier INTO TABLE lt_alt_key_tier.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-tier                             " Node
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-tier-tier_key         " Alternative Key
                                                  it_altkey     = lt_alt_key_tier
                                        IMPORTING eo_change     = DATA(lo_change)                                                    " Interface for transaction change objects
                                                  et_result     = DATA(lt_result)                                                    " Key table with explicit index
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                            ).     " Interface of Message Object
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_app_server_inst
                                                       node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                       source_node = /hec1/if_configuration_c=>sc_node-tier
                                                       association = /hec1/if_configuration_c=>sc_association-tier-app_server_instance
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_app_server_inst>-key                                          ) )
                IMPORTING eo_message      = lo_message                                                                                    ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_app_server_inst> IS ASSIGNED.

        " ****************************************
        " Update APP server instance instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_app_server_inst-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_server_instance-app_server_inst_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                           ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_app_server_inst = NEW /hec1/s_data_app_serv_inst_cs( ).
        ASSIGN lr_app_server_inst->* TO <fs_app_server_inst>.
        IF <fs_app_server_inst> IS ASSIGNED.
          <fs_app_server_inst> = CORRESPONDING #( is_app_server_inst ).

          " Get fields of structure
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = is_app_server_inst ).

          DELETE lt_comp
            WHERE name = /hec1/if_config_constants=>gc_fieldname-field_read_only OR
                  name = /hec1/if_config_constants=>gc_fieldname-field_mandatory.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data           = lr_app_server_inst
                                                        node           = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                  WHERE ( name <> /hec1/if_config_constants=>gc_fieldname-field_read_only OR
                                                                                          name <> /hec1/if_config_constants=>gc_fieldname-field_mandatory    )
                                                                                  ( wa-name )        )
                                                         key            = lv_bo_key                                            ) )
                IMPORTING eo_message      = lo_message                                                                           ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_app_server_inst> IS ASSIGNED.

        " ****************************************
        " Delete APP server instance instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_app_server_inst-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_server_instance-app_server_inst_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                          ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_app_server_inst
                                                      node           = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                            ) )
               IMPORTING eo_message      = lo_message                                                                            ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_app_server_pc.

    DATA: lt_bo_key           TYPE /bobf/t_frw_key,
          lt_alt_key_app_node TYPE TABLE OF /hec1/s_key_app_node,
          ls_alt_key_app_node LIKE LINE OF lt_alt_key_app_node,
          lt_alt_key          TYPE TABLE OF /hec1/s_key_app_serv_pc,
          ls_alt_key          LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create node
        " APP server performance category
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_app_server_spc) = NEW /hec1/s_data_app_serv_pc_cs( ).
        ASSIGN lr_app_server_spc->* TO FIELD-SYMBOL(<fs_app_server_spc>).
        IF <fs_app_server_spc> IS ASSIGNED.
          <fs_app_server_spc> = VALUE #( BASE CORRESPONDING #( is_app_serv_pc )
                                         key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_app_node = CORRESPONDING #( is_app_serv_pc-obj_key ).
          INSERT ls_alt_key_app_node INTO TABLE lt_alt_key_app_node.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_node
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_node-app_node_key
                                                  it_altkey     = lt_alt_key_app_node
                                        IMPORTING eo_change     = DATA(lo_change)
                                                  et_result     = DATA(lt_result)
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                                  ).
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_app_server_spc
                                                       node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                       source_node = /hec1/if_configuration_c=>sc_node-app_node
                                                       association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_app_server_spc>-key                                                  ) )
                IMPORTING eo_message      = lo_message                                                                                            ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_app_server_spc> IS ASSIGNED.

        " ****************************************
        " Update node
        " APP server performance category
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_app_serv_pc-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_server_perform_cat-app_server_perform_cat_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                                     ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_app_server_spc = NEW /hec1/s_data_app_serv_pc_cs( ).
        ASSIGN lr_app_server_spc->* TO <fs_app_server_spc>.
        IF <fs_app_server_spc> IS ASSIGNED.
          <fs_app_server_spc> = CORRESPONDING #( is_app_serv_pc ).

          " Get fields of structure
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_app_server_spc> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_app_server_spc
                                                        node           = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                                ) )
                 IMPORTING eo_message      = lo_message                                                                              ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_app_server_spc> IS ASSIGNED.

        " ****************************************
        " Delete node
        " APP server performance category
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_app_serv_pc-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_server_perform_cat-app_server_perform_cat_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                                     ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_app_server_spc
                                                      node           = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                                ) )
               IMPORTING eo_message      = lo_message                                                                               ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_app_storage.

    DATA: lt_bo_key           TYPE /bobf/t_frw_key,
          lt_alt_key_app_serv TYPE TABLE OF /hec1/s_key_app_serv,
          ls_alt_key_app_serv LIKE LINE OF lt_alt_key_app_serv,
          lt_alt_key          TYPE TABLE OF /hec1/s_key_app_storage,
          ls_alt_key          LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create node App storage
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_app_storage) = NEW /hec1/s_data_app_storage_cs( ).
        ASSIGN lr_app_storage->* TO FIELD-SYMBOL(<fs_app_storage>).
        IF <fs_app_storage> IS ASSIGNED.
          <fs_app_storage> = VALUE #( BASE CORRESPONDING #( is_app_storage )
                                      key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_app_serv = CORRESPONDING #( is_app_storage-obj_key ).
          INSERT ls_alt_key_app_serv INTO TABLE lt_alt_key_app_serv.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_server
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_server-app_server_key
                                                  it_altkey     = lt_alt_key_app_serv
                                        IMPORTING eo_change     = DATA(lo_change)
                                                  et_result     = DATA(lt_result)
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                                       ).
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_app_storage
                                                       node        = /hec1/if_configuration_c=>sc_node-app_storage
                                                       source_node = /hec1/if_configuration_c=>sc_node-app_server
                                                       association = /hec1/if_configuration_c=>sc_association-app_server-app_storage
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_app_storage>-key                                            ) )
                IMPORTING eo_message      = lo_message                                                                                   ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_app_storage> IS ASSIGNED.

        " ****************************************
        " Update node App storage
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_app_storage-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_storage
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_storage-app_storage_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                               ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_app_storage = NEW /hec1/s_data_app_storage_cs( ).
        ASSIGN lr_app_storage->* TO <fs_app_storage>.
        IF <fs_app_storage> IS ASSIGNED.
          <fs_app_storage> = CORRESPONDING #( is_app_storage ).

          " Get fields of structure
*          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = is_app_storage ).
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_app_storage> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_app_storage
                                                        node           = /hec1/if_configuration_c=>sc_node-app_storage
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                     ) )
                 IMPORTING eo_message      = lo_message                                                                    ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_app_storage> IS ASSIGNED.

        " ****************************************
        " Delete node App storage
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_app_storage-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_storage
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_storage-app_storage_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                               ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_app_storage
                                                      node           = /hec1/if_configuration_c=>sc_node-app_storage
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                     ) )
               IMPORTING eo_message      = lo_message                                                                    ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_app_storage_qty.

    DATA: lt_bo_key          TYPE /bobf/t_frw_key,
          lt_alt_key_app_spc TYPE TABLE OF /hec1/s_key_app_serv_pc,
          ls_alt_key_app_spc LIKE LINE OF lt_alt_key_app_spc,
          lt_alt_key         TYPE TABLE OF /hec1/s_key_app_storqty,
          ls_alt_key         LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create node App storage amount
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_app_storage_qty) = NEW /hec1/s_data_app_storageqty_cs( ).
        ASSIGN lr_app_storage_qty->* TO FIELD-SYMBOL(<fs_app_storage_qty>).
        IF <fs_app_storage_qty> IS ASSIGNED.
          <fs_app_storage_qty> = VALUE #( BASE CORRESPONDING #( is_app_storage_qty )
                                          key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_app_spc = CORRESPONDING #( is_app_storage_qty-obj_key ).
          INSERT ls_alt_key_app_spc INTO TABLE lt_alt_key_app_spc.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_server_perform_cat-app_server_perform_cat_key
                                                  it_altkey     = lt_alt_key_app_spc
                                        IMPORTING eo_change     = DATA(lo_change)
                                                  et_result     = DATA(lt_result)
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                                                               ).
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_app_storage_qty
                                                       node        = /hec1/if_configuration_c=>sc_node-app_storage_amount
                                                       source_node = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                       association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_storage_amount
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_app_storage_qty>-key                                                            ) )
                IMPORTING eo_message      = lo_message                                                                                                       ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_app_storage_qty> IS ASSIGNED.

        " ****************************************
        " Update node App storage amount
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_app_storage_qty-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_storage_amount
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_storage_amount-app_storage_amount_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                            ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_app_storage_qty = NEW /hec1/s_data_app_storageqty_cs( ).
        ASSIGN lr_app_storage_qty->* TO <fs_app_storage_qty>.
        IF <fs_app_storage_qty> IS ASSIGNED.
          <fs_app_storage_qty> = CORRESPONDING #( is_app_storage_qty ).

          " Get fields of structure
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_app_storage_qty> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_app_storage_qty
                                                        node           = /hec1/if_configuration_c=>sc_node-app_storage_amount
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                            ) )
                 IMPORTING eo_message      = lo_message                                                                           ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_app_storage_qty> IS ASSIGNED.

        " ****************************************
        " Delete node App storage amount
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_app_storage_qty-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_storage_amount
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_storage_amount-app_storage_amount_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                             ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_app_storage_qty
                                                      node           = /hec1/if_configuration_c=>sc_node-app_storage_amount
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                            ) )
               IMPORTING eo_message      = lo_message                                                                           ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_connectivity.

    DATA: lt_bo_key     TYPE /bobf/t_frw_key,
          lt_alt_key_dc TYPE TABLE OF /hec1/s_key_datacenter,
          ls_alt_key_dc LIKE LINE OF lt_alt_key_dc,
          lt_alt_key    TYPE TABLE OF /hec1/s_key_connectivity,
          ls_alt_key    LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create connectivity instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_connectivity) = NEW /hec1/s_data_connectivity_cs( ).
        ASSIGN lr_connectivity->* TO FIELD-SYMBOL(<fs_connectivity>).
        IF <fs_connectivity> IS ASSIGNED.
          <fs_connectivity> = VALUE #( BASE CORRESPONDING #( is_connectivity )
                                     key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_dc = is_connectivity-hec_node_datacenter.
          INSERT ls_alt_key_dc INTO TABLE lt_alt_key_dc.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-datacenter                                    " Node
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-datacenter-datacenter_key          " Alternative Key
                                                  it_altkey     = lt_alt_key_dc
                                        IMPORTING eo_change     = DATA(lo_change)                                                                 " Interface for transaction change objects
                                                  et_result     = DATA(lt_result)                                                                 " Key table with explicit index
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                                         ).     " Interface of Message Object
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_connectivity
                                                       node        = /hec1/if_configuration_c=>sc_node-connectivity
                                                       source_node = /hec1/if_configuration_c=>sc_node-datacenter
                                                       association = /hec1/if_configuration_c=>sc_association-datacenter-connectivity
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_connectivity>-key                                             ) )
                IMPORTING eo_message      = lo_message                                                                               ).

              ev_key_updated = <fs_connectivity>-key.
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_connectivity> IS ASSIGNED.

        " ****************************************
        " Update connectivity instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_connectivity-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-connectivity                                      " Node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-connectivity-connectivtity_key         " Alternative Key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change                                                                           " Interface for transaction change objects
                                                et_result     = lt_result                                                                           " Key table with explicit index
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                   ).     " Interface of Message Object
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_connectivity = NEW /hec1/s_data_connectivity_cs( ).
        ASSIGN lr_connectivity->* TO <fs_connectivity>.
        IF <fs_connectivity> IS ASSIGNED.
          <fs_connectivity> = CORRESPONDING #( is_connectivity ).

          " Get fields of structure
*          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = is_connectivity ).
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_connectivity> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_connectivity
                                                        node           = /hec1/if_configuration_c=>sc_node-connectivity
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                     ) )
                 IMPORTING eo_message      = lo_message                                                                    ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_connectivity> IS ASSIGNED.

        " ****************************************
        " Delete connectivity instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_connectivity-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-connectivity                                       " Node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-connectivity-connectivtity_key          " Alternative Key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change                                                                            " Interface for transaction change objects
                                                et_result     = lt_result                                                                            " Key table with explicit index
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                  ).       " Interface of Message Object
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_connectivity
                                                      node           = /hec1/if_configuration_c=>sc_node-connectivity
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                     ) )
               IMPORTING eo_message      = lo_message                                                                    ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_connect_price_aggre.

    DATA: lt_bo_key  TYPE /bobf/t_frw_key,
          lt_alt_key TYPE TABLE OF /hec1/s_key_conn_price_phase,
          ls_alt_key LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create Connectivity Price Phase instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_connect_price_aggre) = NEW /hec1/s_connect_price_aggre_cs( ).
        ASSIGN lr_connect_price_aggre->* TO FIELD-SYMBOL(<fs_connect_price_aggre>).
        IF <fs_connect_price_aggre> IS ASSIGNED.
          <fs_connect_price_aggre> = VALUE #( BASE CORRESPONDING #( is_price_aggre )
                                               key = /bopf/cl_frw_factory=>get_new_key( ) ).

          TRY .
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_connect_price_aggre
                                                       node        = /hec1/if_configuration_c=>sc_node-connectivity_price_phase
                                                       source_node = /hec1/if_configuration_c=>sc_node-root
                                                       association = /hec1/if_configuration_c=>sc_association-root-connectivity_price_phase
                                                       source_key  = me->mv_bo_root_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_connect_price_aggre>-key                                               ) )
                IMPORTING eo_message      = DATA(lo_message)                                                                               ).

            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF.

        " ****************************************
        " Update Connectivity Price Phase node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_price_aggre-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-connectivity_price_phase
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-connectivity_price_phase-connect_price_phase_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = DATA(lo_change)
                                                et_result     = DATA(lt_result)
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message ).

        TRY.
            DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. ">>>>>>>>
        ENDTRY.

        lr_connect_price_aggre = NEW /hec1/s_connect_price_aggre_cs( ).
        ASSIGN lr_connect_price_aggre->* TO <fs_connect_price_aggre>.
        IF <fs_connect_price_aggre> IS ASSIGNED.
          <fs_connect_price_aggre> = CORRESPONDING #( is_price_aggre ).

          " Get fields of structure
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_connect_price_aggre> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data           = lr_connect_price_aggre
                                                        node           = /hec1/if_configuration_c=>sc_node-connectivity_price_phase
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                     ) )
                 IMPORTING eo_message      = lo_message                                                                    ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF.

        " ****************************************
        " Delete Connectivity Price Phase node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_price_aggre-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-connectivity_price_phase
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-connectivity_price_phase-connect_price_phase_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message ).

        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. ">>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data           = lr_connect_price_aggre
                                                      node           = /hec1/if_configuration_c=>sc_node-connectivity_price_phase
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                     ) )
               IMPORTING eo_message      = lo_message                                                                    ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.

    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_datacenter.

    DATA: lt_bo_key  TYPE /bobf/t_frw_key,
          lt_alt_key TYPE TABLE OF /hec1/datacenter_guid,
          ls_alt_key LIKE LINE OF lt_alt_key.

    CLEAR ev_key_updated.
    CASE iv_update_mode.
        " ****************************************
        " Create data center instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_datacenter) = NEW /hec1/s_data_datacenter_cs( ).
        ASSIGN lr_datacenter->* TO FIELD-SYMBOL(<fs_datacenter>).
        IF <fs_datacenter> IS ASSIGNED.
          <fs_datacenter> = VALUE #( BASE CORRESPONDING #( is_datacenter )
                                     key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_datacenter
                                                       node        = /hec1/if_configuration_c=>sc_node-datacenter
                                                       source_node = /hec1/if_configuration_c=>sc_node-delivery_unit
                                                       association = /hec1/if_configuration_c=>sc_association-delivery_unit-datacenter
                                                       source_key  = me->mv_bo_dlvy_unit_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_datacenter>-key                                               ) )
                IMPORTING eo_message      = DATA(lo_message)                                                                               ).
              ev_key_updated = <fs_datacenter>-key.
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_datacenter> IS ASSIGNED.

        " ****************************************
        " Update data center instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_datacenter-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-datacenter                                    " Node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-datacenter-datacenter_key         " Alternative Key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = DATA(lo_change)                                                                 " Interface for transaction change objects
                                                et_result     = DATA(lt_result)                                                                 " Key table with explicit index
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                               ).     " Interface of Message Object
        TRY.
            DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_datacenter = NEW /hec1/s_data_datacenter_cs( ).
        ASSIGN lr_datacenter->* TO <fs_datacenter>.
        IF <fs_datacenter> IS ASSIGNED.
          <fs_datacenter> = CORRESPONDING #( is_datacenter ).

          " Get fields of structure
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_datacenter> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_datacenter
                                                        node           = /hec1/if_configuration_c=>sc_node-datacenter
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                     ) )
                 IMPORTING eo_message      = lo_message                                                                    ).
              ev_key_updated = lv_bo_key.
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_datacenter> IS ASSIGNED.

        " ****************************************
        " Delete data center instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_datacenter-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-datacenter                                    " Node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-datacenter-datacenter_key          " Alternative Key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change                                                                       " Interface for transaction change objects
                                                et_result     = lt_result                                                                       " Key table with explicit index
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                               ).     " Interface of Message Object
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_datacenter
                                                      node           = /hec1/if_configuration_c=>sc_node-datacenter
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                     ) )
               IMPORTING eo_message      = lo_message                                                                    ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_db_backup.

    DATA: lt_bo_key          TYPE /bobf/t_frw_key,
          lt_alt_key_storage TYPE /hec1/t_key_db_storage,
          ls_alt_key_storage LIKE LINE OF lt_alt_key_storage,
          lt_alt_key         TYPE /hec1/t_key_db_backup,
          ls_alt_key         LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create node DB storage backup
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_db_backup) = NEW /hec1/s_data_db_backup_cs( ).
        ASSIGN lr_db_backup->* TO FIELD-SYMBOL(<fs_db_backup>).
        IF <fs_db_backup> IS ASSIGNED.
          <fs_db_backup> = VALUE #( BASE CORRESPONDING #( is_db_backup )
                                    key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_storage = CORRESPONDING #( is_db_backup-obj_key ).
          INSERT ls_alt_key_storage INTO TABLE lt_alt_key_storage.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_storage
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_storage-db_storage_key
                                                  it_altkey     = lt_alt_key_storage
                                        IMPORTING eo_change     = DATA(lo_change)
                                                  et_result     = DATA(lt_result)
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                                        ).
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_db_backup
                                                       node        = /hec1/if_configuration_c=>sc_node-db_storage_backup
                                                       source_node = /hec1/if_configuration_c=>sc_node-db_storage
                                                       association = /hec1/if_configuration_c=>sc_association-db_storage-db_storage_backup
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_db_backup>-key                                                     ) )
                IMPORTING eo_message      = lo_message                                                                                           ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_db_backup> IS ASSIGNED.

        " ****************************************
        " Update node DB storage backup
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_db_backup-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_storage_backup
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_storage_backup-db_backup_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                     ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_db_backup = NEW /hec1/s_data_db_backup_cs( ).
        ASSIGN lr_db_backup->* TO <fs_db_backup>.
        IF <fs_db_backup> IS ASSIGNED.
          <fs_db_backup> = CORRESPONDING #( is_db_backup ).

          " Get fields of structure
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_db_backup> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_db_backup
                                                        node           = /hec1/if_configuration_c=>sc_node-db_storage_backup
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                           ) )
                 IMPORTING eo_message      = lo_message                                                                          ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_db_backup> IS ASSIGNED.

        " ****************************************
        " Delete node DB storage backup
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_db_backup-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_storage_backup
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_storage_backup-db_backup_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                      ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_db_backup
                                                      node           = /hec1/if_configuration_c=>sc_node-db_storage_backup
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                           ) )
               IMPORTING eo_message      = lo_message                                                                          ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_db_node.

    DATA: lt_bo_key          TYPE /bobf/t_frw_key,
          lt_alt_key_db_inst TYPE TABLE OF /hec1/s_key_db_inst,
          ls_alt_key_db_inst LIKE LINE OF lt_alt_key_db_inst,
          lt_alt_key         TYPE TABLE OF /hec1/s_key_db_node,
          ls_alt_key         LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create DB node instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_db_node) = NEW /hec1/s_data_db_node_cs( ).
        ASSIGN lr_db_node->* TO FIELD-SYMBOL(<fs_db_node>).
        IF <fs_db_node> IS ASSIGNED.
          <fs_db_node> = VALUE #( BASE CORRESPONDING #( is_db_node )
                                     key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_db_inst = CORRESPONDING #( is_db_node-obj_key ).
          INSERT ls_alt_key_db_inst INTO TABLE lt_alt_key_db_inst.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-instance_db
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-instance_db-instance_db_key
                                                  it_altkey     = lt_alt_key_db_inst
                                        IMPORTING eo_change     = DATA(lo_change)
                                                  et_result     = DATA(lt_result)
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                                         ).
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_db_node
                                                       node        = /hec1/if_configuration_c=>sc_node-db_node
                                                       source_node = /hec1/if_configuration_c=>sc_node-instance_db
                                                       association = /hec1/if_configuration_c=>sc_association-instance_db-db_node
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_db_node>-key                                             ) )
                IMPORTING eo_message      = lo_message                                                                               ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_db_node> IS ASSIGNED.

        " ****************************************
        " Update DB node instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_db_node-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_node-db_node_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                         ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_db_node = NEW /hec1/s_data_db_node_cs( ).
        ASSIGN lr_db_node->* TO <fs_db_node>.
        IF <fs_db_node> IS ASSIGNED.
          <fs_db_node> = CORRESPONDING #( is_db_node ).

          " Get fields of structure
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_db_node> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_db_node
                                                        node           = /hec1/if_configuration_c=>sc_node-db_node
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                     ) )
                 IMPORTING eo_message      = lo_message                                                                    ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_db_node> IS ASSIGNED.

        " ****************************************
        " Delete DB node instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_db_node-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_node-db_node_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                         ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_db_node
                                                      node           = /hec1/if_configuration_c=>sc_node-db_node
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                     ) )
               IMPORTING eo_message      = lo_message                                                                    ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_db_server.

    DATA: lt_bo_key         TYPE /bobf/t_frw_key,
          lt_alt_key_db_spc TYPE TABLE OF /hec1/s_key_db_serv_pc,
          ls_alt_key_db_spc LIKE LINE OF lt_alt_key_db_spc,
          lt_alt_key        TYPE TABLE OF /hec1/s_key_db_serv,
          ls_alt_key        LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create DB server instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_db_server) = NEW /hec1/s_data_db_serv_cs( ).
        ASSIGN lr_db_server->* TO FIELD-SYMBOL(<fs_db_server>).
        IF <fs_db_server> IS ASSIGNED.
          <fs_db_server> = VALUE #( BASE CORRESPONDING #( is_db_server )
                                     key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_db_spc = CORRESPONDING #( is_db_server-obj_key ).
          INSERT ls_alt_key_db_spc INTO TABLE lt_alt_key_db_spc.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_server_perform_cat-db_serv_perf_cat_key
                                                  it_altkey     = lt_alt_key_db_spc
                                        IMPORTING eo_change     = DATA(lo_change)
                                                  et_result     = DATA(lt_result)
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                                                        ).
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_db_server
                                                       node        = /hec1/if_configuration_c=>sc_node-db_server
                                                       source_node = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                       association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_server
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_db_server>-key                                                       ) )
                IMPORTING eo_message      = lo_message                                                                                            ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_db_server> IS ASSIGNED.

        " ****************************************
        " Update DB server instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_db_server-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_server
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_server-db_server_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                           ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_db_server = NEW /hec1/s_data_db_serv_cs( ).
        ASSIGN lr_db_server->* TO <fs_db_server>.
        IF <fs_db_server> IS ASSIGNED.
          <fs_db_server> = CORRESPONDING #( is_db_server ).

          " Get fields of structure
*          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = is_db_server ).
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_db_server> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_db_server
                                                        node           = /hec1/if_configuration_c=>sc_node-db_server
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                    ) )
                 IMPORTING eo_message      = lo_message                                                                   ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_db_server> IS ASSIGNED.

        " ****************************************
        " Delete DB server instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_db_server-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_server
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_server-db_server_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                           ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_db_server
                                                      node           = /hec1/if_configuration_c=>sc_node-db_server
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                   ) )
               IMPORTING eo_message      = lo_message                                                                  ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_db_server_inst.

    DATA: lt_bo_key       TYPE /bobf/t_frw_key,
          lt_alt_key_tier TYPE TABLE OF /hec1/s_key_tier,
          ls_alt_key_tier LIKE LINE OF lt_alt_key_tier,
          lt_alt_key      TYPE TABLE OF /hec1/s_key_db_server_inst,
          ls_alt_key      LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create DB server instance instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_db_server_inst) = NEW /hec1/s_data_db_server_inst_cs( ).
        ASSIGN lr_db_server_inst->* TO FIELD-SYMBOL(<fs_db_server_inst>).
        IF <fs_db_server_inst> IS ASSIGNED.
          <fs_db_server_inst> = VALUE #( BASE CORRESPONDING #( is_db_server_inst )
                                         key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_tier = CORRESPONDING #( is_db_server_inst-obj_key ).
          INSERT ls_alt_key_tier INTO TABLE lt_alt_key_tier.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-tier                             " Node
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-tier-tier_key         " Alternative Key
                                                  it_altkey     = lt_alt_key_tier
                                        IMPORTING eo_change     = DATA(lo_change)                                                    " Interface for transaction change objects
                                                  et_result     = DATA(lt_result)                                                    " Key table with explicit index
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                            ).     " Interface of Message Object
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_db_server_inst
                                                       node        = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                       source_node = /hec1/if_configuration_c=>sc_node-tier
                                                       association = /hec1/if_configuration_c=>sc_association-tier-db_server_instance
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_db_server_inst>-key                                          ) )
                IMPORTING eo_message      = lo_message                                                                                    ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_db_server_inst> IS ASSIGNED.

        " ****************************************
        " Update DB server instance instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_db_server_inst-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_server_instance-db_server_inst_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                          ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_db_server_inst = NEW /hec1/s_data_db_server_inst_cs( ).
        ASSIGN lr_db_server_inst->* TO <fs_db_server_inst>.
        IF <fs_db_server_inst> IS ASSIGNED.
          <fs_db_server_inst> = CORRESPONDING #( is_db_server_inst ).

          " Get fields of structure
*          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = is_db_server_inst ).
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_db_server_inst> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_db_server_inst
                                                        node           = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                            ) )
                 IMPORTING eo_message      = lo_message                                                                           ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_db_server_inst> IS ASSIGNED.

        " ****************************************
        " Delete DB server instance instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_db_server_inst-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_server_instance-db_server_inst_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                          ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_db_server_inst
                                                      node           = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                            ) )
               IMPORTING eo_message      = lo_message                                                                            ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_db_server_pc.

    DATA: lt_bo_key          TYPE /bobf/t_frw_key,
          lt_alt_key_db_node TYPE TABLE OF /hec1/s_key_db_node,
          ls_alt_key_db_node LIKE LINE OF lt_alt_key_db_node,
          lt_alt_key         TYPE TABLE OF /hec1/s_key_db_serv_pc,
          ls_alt_key         LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create DB server performance category
        " instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_db_server_spc) = NEW /hec1/s_data_db_serv_pc_cs( ).
        ASSIGN lr_db_server_spc->* TO FIELD-SYMBOL(<fs_db_server_spc>).
        IF <fs_db_server_spc> IS ASSIGNED.
          <fs_db_server_spc> = VALUE #( BASE CORRESPONDING #( is_db_serv_pc )
                                        key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_db_node = CORRESPONDING #( is_db_serv_pc-obj_key ).
          INSERT ls_alt_key_db_node INTO TABLE lt_alt_key_db_node.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_node
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_node-db_node_key
                                                  it_altkey     = lt_alt_key_db_node
                                        IMPORTING eo_change     = DATA(lo_change)
                                                  et_result     = DATA(lt_result)
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                                  ).
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_db_server_spc
                                                       node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                       source_node = /hec1/if_configuration_c=>sc_node-db_node
                                                       association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_db_server_spc>-key                                                ) )
                IMPORTING eo_message      = lo_message                                                                                         ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_db_server_spc> IS ASSIGNED.

        " ****************************************
        " Update DB server performance category
        " instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_db_serv_pc-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_server_perform_cat-db_serv_perf_cat_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                              ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_db_server_spc = NEW /hec1/s_data_db_serv_pc_cs( ).
        ASSIGN lr_db_server_spc->* TO <fs_db_server_spc>.
        IF <fs_db_server_spc> IS ASSIGNED.
          <fs_db_server_spc> = CORRESPONDING #( is_db_serv_pc ).

          " Get fields of structure
*          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = is_db_serv_pc ).
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_db_server_spc> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_db_server_spc
                                                        node           = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                               ) )
                 IMPORTING eo_message      = lo_message                                                                             ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_db_server_spc> IS ASSIGNED.

        " ****************************************
        " Delete DB server performance category
        " instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_db_serv_pc-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_server_perform_cat-db_serv_perf_cat_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                              ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_db_server_spc
                                                      node           = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                               ) )
               IMPORTING eo_message      = lo_message                                                                              ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_db_storage.

    DATA: lt_bo_key          TYPE /bobf/t_frw_key,
          lt_alt_key_db_serv TYPE TABLE OF /hec1/s_key_db_serv,
          ls_alt_key_db_serv LIKE LINE OF lt_alt_key_db_serv,
          lt_alt_key         TYPE TABLE OF /hec1/s_key_db_storage,
          ls_alt_key         LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create DB storage instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_db_storage) = NEW /hec1/s_data_db_storage_cs( ).
        ASSIGN lr_db_storage->* TO FIELD-SYMBOL(<fs_db_storage>).
        IF <fs_db_storage> IS ASSIGNED.
          <fs_db_storage> = VALUE #( BASE CORRESPONDING #( is_db_storage )
                                     key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_db_serv = CORRESPONDING #( is_db_storage-obj_key ).
          INSERT ls_alt_key_db_serv INTO TABLE lt_alt_key_db_serv.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_server
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_server-db_server_key
                                                  it_altkey     = lt_alt_key_db_serv
                                        IMPORTING eo_change     = DATA(lo_change)
                                                  et_result     = DATA(lt_result)
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                                      ).
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_db_storage
                                                       node        = /hec1/if_configuration_c=>sc_node-db_storage
                                                       source_node = /hec1/if_configuration_c=>sc_node-db_server
                                                       association = /hec1/if_configuration_c=>sc_association-db_server-db_storage
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_db_storage>-key                                           ) )
                IMPORTING eo_message      = lo_message                                                                                 ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_db_storage> IS ASSIGNED.

        " ****************************************
        " Update DB storage instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_db_storage-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_storage
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_storage-db_storage_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                             ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_db_storage = NEW /hec1/s_data_db_storage_cs( ).
        ASSIGN lr_db_storage->* TO <fs_db_storage>.
        IF <fs_db_storage> IS ASSIGNED.
          <fs_db_storage> = CORRESPONDING #( is_db_storage ).

          " Get fields of structure
*          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = is_db_storage ).
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_db_storage> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_db_storage
                                                        node           = /hec1/if_configuration_c=>sc_node-db_storage
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                    ) )
                 IMPORTING eo_message      = lo_message                                                                   ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_db_storage> IS ASSIGNED.

        " ****************************************
        " Delete DB storage instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_db_storage-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_storage
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_storage-db_storage_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                             ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_db_storage
                                                      node           = /hec1/if_configuration_c=>sc_node-db_storage
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                    ) )
               IMPORTING eo_message      = lo_message                                                                   ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_db_storage_qty.

    DATA: lt_bo_key         TYPE /bobf/t_frw_key,
          lt_alt_key_db_spc TYPE TABLE OF /hec1/s_key_db_serv_pc,
          ls_alt_key_db_spc LIKE LINE OF lt_alt_key_db_spc,
          lt_alt_key        TYPE TABLE OF /hec1/s_key_db_storqty,
          ls_alt_key        LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create DB storage instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_db_storage_qty) = NEW /hec1/s_data_db_storage_qty_cs( ).
        ASSIGN lr_db_storage_qty->* TO FIELD-SYMBOL(<fs_db_storage_qty>).
        IF <fs_db_storage_qty> IS ASSIGNED.
          <fs_db_storage_qty> = VALUE #( BASE CORRESPONDING #( is_db_storage_qty )
                                     key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_db_spc = CORRESPONDING #( is_db_storage_qty-obj_key ).
          INSERT ls_alt_key_db_spc INTO TABLE lt_alt_key_db_spc.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_server_perform_cat-db_serv_perf_cat_key
                                                  it_altkey     = lt_alt_key_db_spc
                                        IMPORTING eo_change     = DATA(lo_change)
                                                  et_result     = DATA(lt_result)
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                                                        ).
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_db_storage_qty
                                                       node        = /hec1/if_configuration_c=>sc_node-db_storage_amount
                                                       source_node = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                       association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_db_storage_qty>-key                                                          ) )
                IMPORTING eo_message      = lo_message                                                                                                    ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_db_storage_qty> IS ASSIGNED.

        " ****************************************
        " Update DB storage amount instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_db_storage_qty-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_storage_amount
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_storage_amount-db_storage_amount_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                            ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_db_storage_qty = NEW /hec1/s_data_db_storage_qty_cs( ).
        ASSIGN lr_db_storage_qty->* TO <fs_db_storage_qty>.
        IF <fs_db_storage_qty> IS ASSIGNED.
          <fs_db_storage_qty> = CORRESPONDING #( is_db_storage_qty ).

          " Get fields of structure
*          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = is_db_storage_qty ).
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_db_storage_qty> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_db_storage_qty
                                                        node           = /hec1/if_configuration_c=>sc_node-db_storage_amount
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                            ) )
                 IMPORTING eo_message      = lo_message                                                                           ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_db_storage_qty> IS ASSIGNED.

        " ****************************************
        " Delete DB storage amount instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_db_storage_qty-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_storage_amount
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_storage_amount-db_storage_amount_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                            ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_db_storage_qty
                                                      node           = /hec1/if_configuration_c=>sc_node-db_storage_amount
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                           ) )
               IMPORTING eo_message      = lo_message                                                                         ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_delivery_unit.

    DATA: lt_bo_key  TYPE /bobf/t_frw_key,
          lt_alt_key TYPE TABLE OF /hec1/delivery_unit_guid,
          ls_alt_key LIKE LINE OF lt_alt_key.

    CASE iv_update_mode.
        " Create delivery unit instance node
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_dlvy_unit) = NEW /hec1/s_data_dlvy_unit_cs( ).
        ASSIGN lr_dlvy_unit->* TO FIELD-SYMBOL(<fs_dlvy_unit>).
        IF <fs_dlvy_unit> IS ASSIGNED.
          " Get new BO key
          me->mv_bo_dlvy_unit_key = /bopf/cl_frw_factory=>get_new_key( ).                      " Get new technical key

          <fs_dlvy_unit> = VALUE #( BASE CORRESPONDING #( is_delivery_unit )
                                    key = me->mv_bo_dlvy_unit_key            ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_dlvy_unit
                                                       node        = /hec1/if_configuration_c=>sc_node-delivery_unit
                                                       source_node = /hec1/if_configuration_c=>sc_node-root
                                                       association = /hec1/if_configuration_c=>sc_association-root-delivery_unit
                                                       source_key  = me->mv_bo_root_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_dlvy_unit>-key                                           ) )
                IMPORTING eo_message      = DATA(lo_message)                                                                          ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_dlvy_unit> IS ASSIGNED.


        " Update delivery unit instance node
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_delivery_unit-hec_node_delivery_unit.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-delivery_unit                                 " Node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-delivery_unit-dlvy_unit_key        " Alternative Key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = DATA(lo_change)                                                                 " Interface for transaction change objects
                                                et_result     = DATA(lt_result)                                                                 " Key table with explicit index
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                               ).     " Interface of Message Object
        TRY.
            DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_dlvy_unit = NEW /hec1/s_data_dlvy_unit_cs( ).
        ASSIGN lr_dlvy_unit->* TO <fs_dlvy_unit>.
        IF <fs_dlvy_unit> IS ASSIGNED.
          <fs_dlvy_unit> = CORRESPONDING #( is_delivery_unit ).

          " Get fields of structure
*          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = is_delivery_unit ).
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_dlvy_unit> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_dlvy_unit
                                                        node           = /hec1/if_configuration_c=>sc_node-delivery_unit
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                       ) )
                 IMPORTING eo_message      = lo_message                                                                      ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_dlvy_unit> IS ASSIGNED.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_if_baseline.

    DATA: lt_bo_key     TYPE /bobf/t_frw_key,
          lt_alt_key_dc TYPE TABLE OF /hec1/s_key_datacenter,
          ls_alt_key_dc LIKE LINE OF lt_alt_key_dc,
          lt_alt_key    TYPE TABLE OF /hec1/s_key_if_baseline,
          ls_alt_key    LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create connectivity instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_if_baseline) = NEW /hec1/s_data_if_baseline_cs( ).
        ASSIGN lr_if_baseline->* TO FIELD-SYMBOL(<fs_if_baseline>).
        IF <fs_if_baseline> IS ASSIGNED.
          <fs_if_baseline> = VALUE #( BASE CORRESPONDING #( is_if_baseline )
                                     key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_dc = is_if_baseline-hec_node_datacenter.
          INSERT ls_alt_key_dc INTO TABLE lt_alt_key_dc.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-datacenter                                    " Node
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-datacenter-datacenter_key          " Alternative Key
                                                  it_altkey     = lt_alt_key_dc
                                        IMPORTING eo_change     = DATA(lo_change)                                                                 " Interface for transaction change objects
                                                  et_result     = DATA(lt_result)                                                                 " Key table with explicit index
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                                         ).     " Interface of Message Object

          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_if_baseline
                                                       node        = /hec1/if_configuration_c=>sc_node-infrastructure_baseline
                                                       source_node = /hec1/if_configuration_c=>sc_node-datacenter
                                                       association = /hec1/if_configuration_c=>sc_association-datacenter-infrastructure_baseline
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_if_baseline>-key                                             ) )
                IMPORTING eo_message      = lo_message                                                                               ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF.

        " ****************************************
        " Update connectivity instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_if_baseline-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-infrastructure_baseline                                 " Node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-infrastructure_baseline-baseline_key         " Alternative Key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change                                                                                 " Interface for transaction change objects
                                                et_result     = lt_result                                                                                 " Key table with explicit index
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                   ).           " Interface of Message Object

        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_if_baseline = NEW /hec1/s_data_if_baseline_cs( ).
        ASSIGN lr_if_baseline->* TO <fs_if_baseline>.
        IF <fs_if_baseline> IS ASSIGNED.
          <fs_if_baseline> = CORRESPONDING #( is_if_baseline ).

          " Get fields of structure
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_if_baseline> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data           = lr_if_baseline
                                                        node           = /hec1/if_configuration_c=>sc_node-infrastructure_baseline
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                     ) )
                 IMPORTING eo_message      = lo_message                                                                    ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF.

        " ****************************************
        " Delete connectivity instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_if_baseline-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-infrastructure_baseline                                 " Node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-infrastructure_baseline-baseline_key         " Alternative Key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change                                                                                 " Interface for transaction change objects
                                                et_result     = lt_result                                                                                 " Key table with explicit index
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                   ).           " Interface of Message Object

        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data           = lr_if_baseline
                                                      node           = /hec1/if_configuration_c=>sc_node-infrastructure_baseline
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                     ) )
               IMPORTING eo_message      = lo_message                                                                    ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.

    ENDCASE. "CASE iv_update_mode.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_instance_db.

    DATA: lt_bo_key               TYPE /bobf/t_frw_key,
          lt_alt_key_db_serv_inst TYPE TABLE OF /hec1/s_key_db_server_inst,
          ls_alt_key_db_serv_inst LIKE LINE OF lt_alt_key_db_serv_inst,
          lt_alt_key              TYPE TABLE OF /hec1/s_key_db_inst,
          ls_alt_key              LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create instance DB instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_instance_db) = NEW /hec1/s_data_db_inst_cs( ).
        ASSIGN lr_instance_db->* TO FIELD-SYMBOL(<fs_instance_db>).
        IF <fs_instance_db> IS ASSIGNED.
          <fs_instance_db> = VALUE #( BASE CORRESPONDING #( is_db_instance )
                                         key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_db_serv_inst = CORRESPONDING #( is_db_instance-obj_key ).
          INSERT ls_alt_key_db_serv_inst INTO TABLE lt_alt_key_db_serv_inst.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-db_server_instance-db_server_inst_key
                                                  it_altkey     = lt_alt_key_db_serv_inst
                                        IMPORTING eo_change     = DATA(lo_change)
                                                  et_result     = DATA(lt_result)
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                                                    ).
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_instance_db
                                                       node        = /hec1/if_configuration_c=>sc_node-instance_db
                                                       source_node = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                       association = /hec1/if_configuration_c=>sc_association-db_server_instance-instance_db
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_instance_db>-key                                                    ) )
                IMPORTING eo_message      = lo_message                                                                                           ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_instance_db> IS ASSIGNED.

        " ****************************************
        " Update instance DB instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_db_instance-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-instance_db
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-instance_db-instance_db_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_instance_db = NEW /hec1/s_data_db_inst_cs( ).
        ASSIGN lr_instance_db->* TO <fs_instance_db>.
        IF <fs_instance_db> IS ASSIGNED.
          <fs_instance_db> = CORRESPONDING #( is_db_instance ).

          " Get fields of structure
*          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = is_db_instance ).
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_instance_db> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_instance_db
                                                        node           = /hec1/if_configuration_c=>sc_node-instance_db
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                      ) )
                 IMPORTING eo_message      = lo_message                                                                     ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_instance_db> IS ASSIGNED.

        " ****************************************
        " Delete instance DB instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_db_instance-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-instance_db
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-instance_db-instance_db_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_instance_db
                                                      node           = /hec1/if_configuration_c=>sc_node-instance_db
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                     ) )
               IMPORTING eo_message      = lo_message                                                                    ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_landscape_price_aggre.

    DATA: lt_bo_key  TYPE /bobf/t_frw_key,
          lt_alt_key TYPE /hec1/t_key_landsc_price_aggre,
          ls_alt_key LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create landscape base price phase node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_price_aggre) = NEW /hec1/s_landsc_price_aggre_cs( ).
        ASSIGN lr_price_aggre->* TO FIELD-SYMBOL(<fs_price_aggre>).
        IF <fs_price_aggre> IS ASSIGNED.
          <fs_price_aggre> = VALUE #( BASE CORRESPONDING #( is_price_aggre )
                                      key = /bopf/cl_frw_factory=>get_new_key( ) ).

          TRY .
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_price_aggre
                                                       node        = /hec1/if_configuration_c=>sc_node-landsc_base_price_phase
                                                       source_node = /hec1/if_configuration_c=>sc_node-root
                                                       association = /hec1/if_configuration_c=>sc_association-root-landsc_base_price_phase
                                                       source_key  = me->mv_bo_root_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_price_aggre>-key                                                       ) )
                IMPORTING eo_message      = DATA(lo_message)                                                                                        ).

            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF.

        " ****************************************
        " Update landscape base price phase node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_price_aggre-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-landsc_base_price_phase
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-landsc_base_price_phase-landsc_price_phase_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = DATA(lo_change)
                                                et_result     = DATA(lt_result)
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message ).

        TRY.
            DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. ">>>>>>>>
        ENDTRY.

        lr_price_aggre = NEW /hec1/s_landsc_price_aggre_cs( ).
        ASSIGN lr_price_aggre->* TO <fs_price_aggre>.
        IF <fs_price_aggre> IS ASSIGNED.
          <fs_price_aggre> = CORRESPONDING #( is_price_aggre ).

          " Get fields of structure
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_price_aggre> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data           = lr_price_aggre
                                                        node           = /hec1/if_configuration_c=>sc_node-landsc_base_price_phase
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                                 ) )
                 IMPORTING eo_message      = lo_message                                                                                 ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF.


        " ****************************************
        " Delete landscape base price phase node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_price_aggre-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-landsc_base_price_phase
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-landsc_base_price_phase-landsc_price_phase_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message ).

        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. ">>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data           = lr_price_aggre
                                                      node           = /hec1/if_configuration_c=>sc_node-landsc_base_price_phase
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                                 ) )
               IMPORTING eo_message      = lo_message                                                                                ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_man_service_baseline.

    DATA: lt_bo_key  TYPE /bobf/t_frw_key,
          lt_alt_key TYPE TABLE OF /hec1/managed_service_bl_guid,
          ls_alt_key LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create data center instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_man_service_baseline) = NEW /hec1/s_data_man_serv_basel_cs( ).
        ASSIGN lr_man_service_baseline->* TO FIELD-SYMBOL(<fs_man_service_baseline>).
        IF <fs_man_service_baseline> IS ASSIGNED.
          <fs_man_service_baseline> = VALUE #( BASE CORRESPONDING #( is_man_service_baseline )
                                               key = /bopf/cl_frw_factory=>get_new_key( ) ).

          TRY .
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_man_service_baseline
                                                       node        = /hec1/if_configuration_c=>sc_node-managed_service_baseline
                                                       source_node = /hec1/if_configuration_c=>sc_node-root
                                                       association = /hec1/if_configuration_c=>sc_association-root-managed_service_baseline
                                                       source_key  = me->mv_bo_root_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_man_service_baseline>-key                                               ) )
                IMPORTING eo_message      = DATA(lo_message)                                                                               ).

            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF.

        " ****************************************
        " Update data center instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_man_service_baseline-hec_node_man_service_bl.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-managed_service_baseline                                 " Node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-managed_service_baseline-baseline_key         " Alternative Key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = DATA(lo_change)                                                                             " Interface for transaction change objects
                                                et_result     = DATA(lt_result)                                                                             " Key table with explicit index
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                               ).                 " Interface of Message Object

        TRY.
            DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_man_service_baseline = NEW /hec1/s_data_man_serv_basel_cs( ).
        ASSIGN lr_man_service_baseline->* TO <fs_man_service_baseline>.
        IF <fs_man_service_baseline> IS ASSIGNED.
          <fs_man_service_baseline> = CORRESPONDING #( is_man_service_baseline ).

          " Get fields of structure
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_man_service_baseline> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data           = lr_man_service_baseline
                                                        node           = /hec1/if_configuration_c=>sc_node-managed_service_baseline
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                     ) )
                 IMPORTING eo_message      = lo_message                                                                    ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF.

        " ****************************************
        " Delete data center instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_man_service_baseline-hec_node_man_service_bl.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-managed_service_baseline                                 " Node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-managed_service_baseline-baseline_key         " Alternative Key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change                                                                                  " Interface for transaction change objects
                                                et_result     = lt_result                                                                                  " Key table with explicit index
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                              ).                 " Interface of Message Object

        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data           = lr_man_service_baseline
                                                      node           = /hec1/if_configuration_c=>sc_node-managed_service_baseline
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                     ) )
               IMPORTING eo_message      = lo_message                                                                    ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.

    ENDCASE. "CASE iv_update_mode.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_material.

    DATA: lt_bo_key       TYPE /bobf/t_frw_key,
          lt_alt_key_tier TYPE TABLE OF /hec1/s_key_tier,
          ls_alt_key_tier LIKE LINE OF lt_alt_key_tier,
          lt_alt_key      TYPE TABLE OF /hec1/s_key_material,
          ls_alt_key      LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create material instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_material) = NEW /hec1/s_data_material_cs( ).
        ASSIGN lr_material->* TO FIELD-SYMBOL(<fs_material>).
        IF <fs_material> IS ASSIGNED.
          <fs_material> = VALUE #( BASE CORRESPONDING #( is_material )
                                         key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_tier = CORRESPONDING #( is_material-obj_key ).
          INSERT ls_alt_key_tier INTO TABLE lt_alt_key_tier.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-tier                             " Node
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-tier-tier_key         " Alternative Key
                                                  it_altkey     = lt_alt_key_tier
                                        IMPORTING eo_change     = DATA(lo_change)                                                    " Interface for transaction change objects
                                                  et_result     = DATA(lt_result)                                                    " Key table with explicit index
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                            ).     " Interface of Message Object
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_material
                                                       node        = /hec1/if_configuration_c=>sc_node-material
                                                       source_node = /hec1/if_configuration_c=>sc_node-tier
                                                       association = /hec1/if_configuration_c=>sc_association-tier-material
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_material>-key                                      ) )
                IMPORTING eo_message      = lo_message                                                                          ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_material> IS ASSIGNED.

        " ****************************************
        " Update material instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_material-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-material
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-material-material_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                           ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_material = NEW /hec1/s_data_material_cs( ).
        ASSIGN lr_material->* TO <fs_material>.
        IF <fs_material> IS ASSIGNED.
          <fs_material> = CORRESPONDING #( is_material ).

          " Get fields of structure
*          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = is_material ).
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_material> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_material
                                                        node           = /hec1/if_configuration_c=>sc_node-material
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                  ) )
                 IMPORTING eo_message      = lo_message                                                                ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_material> IS ASSIGNED.

        " ****************************************
        " Delete material instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_material-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-material
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-material-material_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                           ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_material
                                                      node           = /hec1/if_configuration_c=>sc_node-material
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                  ) )
               IMPORTING eo_message      = lo_message                                                                 ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_network_segment.

    DATA: lt_bo_key     TYPE /bobf/t_frw_key,
          lt_alt_key_if TYPE TABLE OF /hec1/s_key_if_baseline,
          ls_alt_key_if LIKE LINE OF lt_alt_key_if,
          lt_alt_key    TYPE TABLE OF /hec1/s_key_network_segment,
          ls_alt_key    LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create connectivity instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_network_segment) = NEW /hec1/s_data_network_segm_cs( ).
        ASSIGN lr_network_segment->* TO FIELD-SYMBOL(<fs_network_segment>).
        IF <fs_network_segment> IS ASSIGNED.
          <fs_network_segment> = VALUE #( BASE CORRESPONDING #( is_network_segment )
                                     key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_if = CORRESPONDING #( is_network_segment-obj_key ).
          INSERT ls_alt_key_if INTO TABLE lt_alt_key_if.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-infrastructure_baseline                                   " Node
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-infrastructure_baseline-baseline_key           " Alternative Key
                                                  it_altkey     = lt_alt_key_if
                                        IMPORTING eo_change     = DATA(lo_change)                                                                             " Interface for transaction change objects
                                                  et_result     = DATA(lt_result)                                                                             " Key table with explicit index
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                                         ).                 " Interface of Message Object

          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_network_segment
                                                       node        = /hec1/if_configuration_c=>sc_node-network_segment
                                                       source_node = /hec1/if_configuration_c=>sc_node-infrastructure_baseline
                                                       association = /hec1/if_configuration_c=>sc_association-infrastructure_baseline-network_segment
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_network_segment>-key                                             ) )
                IMPORTING eo_message      = lo_message                                                                               ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF.

        " ****************************************
        " Update connectivity instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_network_segment-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-network_segment                                         " Node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-network_segment-segment_key                  " Alternative Key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change                                                                                 " Interface for transaction change objects
                                                et_result     = lt_result                                                                                 " Key table with explicit index
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                   ).           " Interface of Message Object

        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_network_segment = NEW /hec1/s_data_network_segm_cs( ).
        ASSIGN lr_network_segment->* TO <fs_network_segment>.
        IF <fs_network_segment> IS ASSIGNED.
          <fs_network_segment> = CORRESPONDING #( is_network_segment ).

          " Get fields of structure
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_network_segment> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data           = lr_network_segment
                                                        node           = /hec1/if_configuration_c=>sc_node-network_segment
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                     ) )
                 IMPORTING eo_message      = lo_message                                                                    ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF.

        " ****************************************
        " Delete connectivity instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_network_segment-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-network_segment                                         " Node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-network_segment-segment_key                  " Alternative Key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change                                                                                 " Interface for transaction change objects
                                                et_result     = lt_result                                                                                 " Key table with explicit index
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                   ).           " Interface of Message Object

        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data           = lr_network_segment
                                                      node           = /hec1/if_configuration_c=>sc_node-network_segment
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                     ) )
               IMPORTING eo_message      = lo_message                                                                    ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.

    ENDCASE. "CASE iv_update_mode.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_phase.

    DATA: lt_bo_key  TYPE /bobf/t_frw_key,
          lt_alt_key TYPE TABLE OF /hec1/s_key_phase,
          ls_alt_key LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create phase instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_phase) = NEW /hec1/s_data_phase_cs( ).
        ASSIGN lr_phase->* TO FIELD-SYMBOL(<fs_phase>).
        IF <fs_phase> IS ASSIGNED.
          <fs_phase> = VALUE #( BASE CORRESPONDING #( is_phase )
                                     key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_phase
                                                       node        = /hec1/if_configuration_c=>sc_node-phase
                                                       source_node = /hec1/if_configuration_c=>sc_node-root
                                                       association = /hec1/if_configuration_c=>sc_association-root-phase
                                                       source_key  = me->mv_bo_root_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_phase>-key                                      ) )
                IMPORTING eo_message      = DATA(lo_message)                                                                     ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_phase> IS ASSIGNED.

        " ****************************************
        " Update phase instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_phase-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-phase                                 " Node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-phase-phase_key         " Alternative Key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = DATA(lo_change)                                                            " Interface for transaction change objects
                                                et_result     = DATA(lt_result)                                                            " Key table with explicit index
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                          ).     " Interface of Message Object
        TRY.
            DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_phase = NEW /hec1/s_data_phase_cs( ).
        ASSIGN lr_phase->* TO <fs_phase>.
        IF <fs_phase> IS ASSIGNED.
          <fs_phase> = CORRESPONDING #( is_phase ).

          " Get fields of structure
*          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = is_phase ).
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_phase> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data           = lr_phase
                                                        node           = /hec1/if_configuration_c=>sc_node-phase
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                  ) )
                 IMPORTING eo_message      = lo_message                                                                 ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_phase> IS ASSIGNED.

        " ****************************************
        " Delete phase instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_phase-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-phase                                 " Node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-phase-phase_key            " Alternative Key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change                                                                  " Interface for transaction change objects
                                                et_result     = lt_result                                                                  " Key table with explicit index
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                          ).     " Interface of Message Object
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data           = lr_phase
                                                      node           = /hec1/if_configuration_c=>sc_node-phase
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                  ) )
               IMPORTING eo_message      = lo_message                                                                 ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_root.

    CASE iv_update_mode.

        "*************************
        "Create root instance node
        "*************************
      WHEN /bobf/if_frw_c=>sc_modify_create.

        DATA(lr_root) = NEW /hec1/s_config_root_cs( ).
        ASSIGN lr_root->* TO FIELD-SYMBOL(<fs_root>).
        IF <fs_root> IS ASSIGNED.
          " Get new BO key
          me->mv_bo_root_key = /bopf/cl_frw_factory=>get_new_key( ).                      " Get new technical key

          <fs_root> = VALUE #( BASE CORRESPONDING #( is_configuration )
                               key                    = me->mv_bo_root_key
                               hec_config_status      = /hec1/if_config_constants=>gc_config_status-draft
                               crea_uname             = sy-uname
                               hec_created_by_name    = me->get_full_name( sy-uname )    ).

          GET TIME STAMP FIELD <fs_root>-crea_date_time.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify( EXPORTING it_modification = VALUE #( ( data        = lr_root
                                                                                                                                                        node        = /hec1/if_configuration_c=>sc_node-root
                                                                                                                                                        change_mode = /bobf/if_frw_c=>sc_modify_create
                                                                                                                                                        key         = <fs_root>-key                          ) )
                                                                                                                 IMPORTING eo_message      = DATA(lo_message)                                                   ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_root> IS ASSIGNED.


        " ****************************************
        " Update root instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        lr_root = NEW /hec1/s_config_root_cs( ).
        ASSIGN lr_root->* TO <fs_root>.

        IF <fs_root> IS ASSIGNED.
          <fs_root> = CORRESPONDING #( is_configuration ).

          " Get fields of structure
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_root> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data           = lr_root
                                                        node           = /hec1/if_configuration_c=>sc_node-root
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp ( wa-name ) )
                                                        key            = me->mv_bo_root_key                       ) )
                 IMPORTING eo_message      = lo_message
                           ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_root> IS ASSIGNED.

    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_software_item.

    DATA: lt_bo_key           TYPE /bobf/t_frw_key,
          lt_alt_key_material TYPE TABLE OF /hec1/s_key_material,
          ls_alt_key_material LIKE LINE OF lt_alt_key_material,
          lt_alt_key          TYPE TABLE OF /hec1/s_key_sw_item,
          ls_alt_key          LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create software item instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_sw_item) = NEW /hec1/s_data_sw_item_cs( ).
        ASSIGN lr_sw_item->* TO FIELD-SYMBOL(<fs_sw_item>).
        IF <fs_sw_item> IS ASSIGNED.
          <fs_sw_item> = VALUE #( BASE CORRESPONDING #( is_software_item )
                                         key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_material = CORRESPONDING #( is_software_item-obj_key ).
          INSERT ls_alt_key_material INTO TABLE lt_alt_key_material.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-material
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-material-material_key
                                                  it_altkey     = lt_alt_key_material
                                        IMPORTING eo_change     = DATA(lo_change)
                                                  et_result     = DATA(lt_result)
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                                    ).
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_sw_item
                                                       node        = /hec1/if_configuration_c=>sc_node-software_item
                                                       source_node = /hec1/if_configuration_c=>sc_node-material
                                                       association = /hec1/if_configuration_c=>sc_association-material-software_item
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_sw_item>-key                                                 ) )
                IMPORTING eo_message      = lo_message                                                                                    ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_sw_item> IS ASSIGNED.

        " ****************************************
        " Update software item instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_software_item-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-software_item
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-software_item-sw_item_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                              ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_sw_item = NEW /hec1/s_data_sw_item_cs( ).
        ASSIGN lr_sw_item->* TO <fs_sw_item>.
        IF <fs_sw_item> IS ASSIGNED.
          <fs_sw_item> = CORRESPONDING #( is_software_item ).

          " Get fields of structure
*          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = is_software_item ).
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_sw_item> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_sw_item
                                                        node           = /hec1/if_configuration_c=>sc_node-software_item
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                       ) )
                 IMPORTING eo_message      = lo_message                                                                      ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_sw_item> IS ASSIGNED.

        " ****************************************
        " Delete software item instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_software_item-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-software_item
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-software_item-sw_item_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                              ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_sw_item
                                                      node           = /hec1/if_configuration_c=>sc_node-software_item
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                       ) )
               IMPORTING eo_message      = lo_message                                                                      ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_solution.

    DATA: lt_bo_key  TYPE /bobf/t_frw_key,
          lt_alt_key TYPE TABLE OF /hec1/s_key_solution,
          ls_alt_key LIKE LINE OF lt_alt_key.

    CLEAR ev_key_updated.

    CASE iv_update_mode.
        " ****************************************
        " Create solution instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_solution) = NEW /hec1/s_data_solution_cs( ).
        ASSIGN lr_solution->* TO FIELD-SYMBOL(<fs_solution>).
        IF <fs_solution> IS ASSIGNED.
          <fs_solution> = VALUE #( BASE CORRESPONDING #( is_solution )
                                     key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_solution
                                                       node        = /hec1/if_configuration_c=>sc_node-solution
                                                       source_node = /hec1/if_configuration_c=>sc_node-root
                                                       association = /hec1/if_configuration_c=>sc_association-root-solution
                                                       source_key  = me->mv_bo_root_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_solution>-key                                      ) )
                IMPORTING eo_message      = DATA(lo_message)   ).
              ev_key_updated =   <fs_solution>-key.
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_solution> IS ASSIGNED.

        " ****************************************
        " Update solution instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_solution-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-solution                                 " Node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-solution-solution_key         " Alternative Key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = DATA(lo_change)                                                            " Interface for transaction change objects
                                                et_result     = DATA(lt_result)                                                            " Key table with explicit index
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                          ).     " Interface of Message Object
        TRY.
            DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_solution = NEW /hec1/s_data_solution_cs( ).
        ASSIGN lr_solution->* TO <fs_solution>.
        IF <fs_solution> IS ASSIGNED.
          <fs_solution> = CORRESPONDING #( is_solution ).

          " Get fields of structure
*          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = is_solution ).
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_solution> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_solution
                                                        node           = /hec1/if_configuration_c=>sc_node-solution
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                  ) )
                 IMPORTING eo_message      = lo_message                   ).

              ev_key_updated =   lv_bo_key.
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_solution> IS ASSIGNED.

        " ****************************************
        " Delete solution instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_solution-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-solution                                 " Node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-solution-solution_key         " Alternative Key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change                                                                  " Interface for transaction change objects
                                                et_result     = lt_result                                                                  " Key table with explicit index
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                          ).     " Interface of Message Object
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_solution
                                                      node           = /hec1/if_configuration_c=>sc_node-solution
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                  ) )
               IMPORTING eo_message      = lo_message                                                                 ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.

    IF lo_message IS BOUND.
      me->set_bopf_msg_to_fpm_msg( lo_message ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_db_storage.

    DATA lt_data TYPE /hec1/t_data_db_storage_ct.

    CLEAR: eo_message,
           rt_db_storage.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-db_storage
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-db_storage-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_db_storage = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_db_storage_backup.

    DATA lt_data TYPE /hec1/t_data_db_backup_ct.

    CLEAR: eo_message,
           rt_db_backup.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-db_storage_backup
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-db_storage_backup-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_db_backup = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_db_storage_qty.

    DATA lt_data TYPE /hec1/t_data_db_storage_qty_ct.

    CLEAR: eo_message,
           rt_db_storage_qty.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-db_storage_amount
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-db_storage_amount-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_db_storage_qty = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_delivery_unit.

    DATA lt_data TYPE /hec1/t_data_dlvy_unit_ct.

    CLEAR: eo_message,
           rs_delivery_unit.

    TRY.
        me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-delivery_unit
                                                                iv_query_key = /hec1/if_configuration_c=>sc_query-delivery_unit-select_by_elements
                                                                it_key       = it_key
                                                      IMPORTING eo_message   = eo_message
                                                                rt_data      = lt_data ).

        IF lt_data IS NOT INITIAL.
          rs_delivery_unit = CORRESPONDING #( lt_data[ 1 ] ).
        ENDIF.

      CATCH cx_sy_itab_line_not_found.
        "nothing found
        "no exception
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_if_baseline.

    DATA lt_data TYPE /hec1/t_data_if_baseline_ct.

    CLEAR: eo_message,
           rt_if_baseline.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-infrastructure_baseline
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-infrastructure_baseline-select_by_elements
                                                            "it_key       = it_key
                                                            it_parent_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_if_baseline = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_instance_db.

    DATA lt_data TYPE /hec1/t_data_db_inst_ct.

    CLEAR: eo_message,
           rt_inst_db.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-instance_db
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-instance_db-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_inst_db = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_landsc_price_aggre.

    DATA lt_data TYPE /hec1/t_landsc_price_aggre_ct.

    CLEAR: eo_message,
           rt_landsc_price_aggre.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-landsc_base_price_phase
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-landsc_base_price_phase-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_landsc_price_aggre = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_lt_backup_dc.

    DATA lt_data TYPE /hec1/t_data_lt_backup_dc_ct.

    CLEAR: eo_message,
           rt_lt_backup.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-lt_backup_datacenter
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-lt_backup_datacenter-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_lt_backup = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_lt_backup_cl.

    DATA lt_data TYPE /hec1/t_data_lt_backup_cl_ct.

    CLEAR: eo_message,
           rt_lt_backup.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-lt_backup_class
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-lt_backup_class-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_lt_backup = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_lt_backup_am.

    DATA lt_data TYPE /hec1/t_lt_backup_amount_ct.

    CLEAR: eo_message,
           rt_lt_backup.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-lt_backup_amount
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-lt_backup_amount-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_lt_backup = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_man_service_baseline.

    DATA: lt_sel_param TYPE /bobf/t_frw_query_selparam,
          lt_data      TYPE /hec1/t_data_man_serv_basel_ct.

    CLEAR: eo_message,
           rt_man_service_baseline.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-managed_service_baseline
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-managed_service_baseline-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_man_service_baseline = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_material.

    DATA lt_data TYPE /hec1/t_data_material_ct.

    CLEAR: eo_message,
           rt_material.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-material
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-material-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_material = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_network_segment.

    DATA: lt_sel_param TYPE /bobf/t_frw_query_selparam,
          lt_data      TYPE /hec1/t_data_man_serv_basel_ct.

    CLEAR: eo_message,
           rt_network_segment.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-network_segment
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-network_segment-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_network_segment = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_object.

    "generic
    DATA: lo_result_descriptor TYPE REF TO cl_abap_tabledescr,
          lr_data              TYPE REF TO data,
          lt_sel_param         TYPE /bobf/t_frw_query_selparam.

    FIELD-SYMBOLS <lt_data> TYPE STANDARD TABLE.

    DATA(lo_service_manager) = /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key ).

    TRY.
        /bobf/cl_frw_factory=>get_configuration( /hec1/if_configuration_c=>sc_bo_key )->get_node( EXPORTING iv_node_key = iv_node_key
                                                                                                  IMPORTING es_node     = DATA(ls_node) ).
      CATCH /bobf/cx_frw.
        RETURN. ">>>>
    ENDTRY.

    lo_result_descriptor ?= cl_abap_tabledescr=>describe_by_name( ls_node-data_table_type ).
    CREATE DATA lr_data TYPE HANDLE lo_result_descriptor.
    ASSIGN lr_data->* TO <lt_data>.

*    IF it_key IS INITIAL AND it_parent_key IS INITIAL.
*      " ****************
*      " Get All Nodes of this type
*      " ****************
**      lt_sel_param = VALUE #( ( attribute_name = /hec1/if_configuration_c=>sc_query_attribute-landscape-select_by_element-root_key
**                                low            = me->mv_bo_root_key
**                                option         = /hec1/if_bopf_constants=>gc_range_option-eq
**                                sign           = /hec1/if_bopf_constants=>gc_range_sign-i  ) ).
**
**
**      " ATTENTION!!! This Query is only meant to get the keys of the objects.
**      "     The data is read from the database and could be different from the data in the BOPF buffer.
**      "     As a follow up step, the retrieve needs to be run.
**      /hec1/cl_bopf_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = iv_query_key
**                                                                        it_selection_param = lt_sel_param
**                                                                        iv_fill_data       = abap_false
**                                                              IMPORTING eo_message         = eo_message
**                                                                        et_key             = DATA(lt_key) ).
*    ELSEIF it_key IS INITIAL.
*      "In case when we have Parent key known we have to filter out the instance keys to select them correctly
*      LOOP AT it_parent_key REFERENCE INTO DATA(lr_parent_key).
*        lt_sel_param = VALUE #( BASE lt_sel_param
*                                ( attribute_name = /hec1/if_configuration_c=>sc_query_attribute-landscape-select_by_element-parent_key
*                                 low            = lr_parent_key->key
*                                 option         = /hec1/if_bopf_constants=>gc_range_option-eq
*                                 sign           = /hec1/if_bopf_constants=>gc_range_sign-i  ) ).
*
*      ENDLOOP.
*
*
*      " ATTENTION!!! This Query is only meant to get the keys of the objects.
*      "     The data is read from the database and could be different from the data in the BOPF buffer.
*      "     As a follow up step, the retrieve needs to be run.
*      /hec1/cl_bopf_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = iv_query_key
*                                                                        it_selection_param = lt_sel_param
*                                                                        iv_fill_data       = abap_false
*                                                              IMPORTING eo_message         = eo_message
*                                                                        et_key             = lt_key ).
*
*    ELSE.
*      lt_key = it_key.
*    ENDIF.

    lo_service_manager->retrieve(
          EXPORTING
            iv_node_key             = iv_node_key
            it_key                  = it_key
          IMPORTING
            eo_message              = eo_message
            et_data                 = <lt_data>       ).

    IF <lt_data> IS ASSIGNED.
      rt_data = CORRESPONDING #( <lt_data> ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_phase.

    DATA lt_data TYPE /hec1/t_data_phase_ct.

    CLEAR: eo_message,
           rt_phase.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-phase
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-phase-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_phase = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_root.

    DATA lt_data TYPE /hec1/t_config_root_ct.

    CLEAR: eo_message,
           rs_root.

    TRY.
        me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-root
                                                                iv_query_key = /hec1/if_configuration_c=>sc_query-root-select_by_elements
                                                                it_key       = it_key
                                                      IMPORTING eo_message   = eo_message
                                                                rt_data      = lt_data ).

        IF lt_data IS NOT INITIAL.
          rs_root = CORRESPONDING #( lt_data[ 1 ] ).
        ENDIF.

      CATCH cx_sy_itab_line_not_found.
        "nothing found
        "no exception
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_service.

    DATA lt_data TYPE /hec1/t_data_add_services_ct.

    CLEAR: eo_message,
           rt_service.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-add_service
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-add_service-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_service = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_add_storage_price_aggre.

    DATA lt_data TYPE /hec1/t_add_storage_price_phas.

    CLEAR: eo_message,
           rt_add_storage_price_aggre.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-add_storage_price_phase
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-add_storage_price_phase-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_add_storage_price_aggre = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_lt_backup_price_aggre.

    DATA lt_data TYPE /hec1/s_lt_backup_price_agg_ct.

    CLEAR: eo_message,
           rt_lt_backup_price_aggre.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-lt_backup_price_phase
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-lt_backup_price_phase-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_lt_backup_price_aggre = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_service_price_aggre.

    DATA lt_data TYPE /hec1/t_service_price_aggre_ct.

    CLEAR: eo_message,
           rt_service_price_aggre.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-add_service_price_phase
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-add_service_price_phase-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_service_price_aggre = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_software_item.

    DATA lt_data TYPE /hec1/t_data_sw_item_ct.

    CLEAR: eo_message,
           rt_software_item.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-software_item
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-software_item-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_software_item = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_solution.

    DATA lt_data TYPE /hec1/t_data_solution_ct.

    CLEAR: eo_message,
           rt_solution.

    TRY.
        me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-solution
                                                                iv_query_key = /hec1/if_configuration_c=>sc_query-solution-select_by_elements
                                                                it_key       = it_key
                                                      IMPORTING eo_message   = eo_message
                                                                rt_data      = lt_data ).

        rt_solution = CORRESPONDING #( lt_data ).

      CATCH cx_sy_itab_line_not_found.
        "nothing found
        "no exception
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_tier.

    DATA: lt_sel_param TYPE /bobf/t_frw_query_selparam,
          lt_data      TYPE /hec1/t_data_tier_ct.

    CLEAR: eo_message,
           rt_tier.

    TRY.
        me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-tier
                                                                iv_query_key = /hec1/if_configuration_c=>sc_query-tier-select_by_elements
                                                                it_key       = it_key
                                                      IMPORTING eo_message   = eo_message
                                                                rt_data      = lt_data ).

        rt_tier = CORRESPONDING #( lt_data ).

      CATCH cx_sy_itab_line_not_found.
        "nothing found
        "no exception
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_tier_add_service.

    DATA lt_data TYPE /hec1/t_data_tier_add_serv_ct.

    CLEAR: eo_message,
           rt_service.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-tier_add_service
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-tier_add_service-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_service = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_tier_add_storage.
    DATA lt_data TYPE /hec1/t_tier_add_storage_ct .

    CLEAR: eo_message,
           rt_tier_add_storage.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-tier_add_storage
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-tier_add_storage-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_tier_add_storage = CORRESPONDING #( lt_data ).
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_tier_lt_backup.
    DATA lt_data TYPE /hec1/t_data_tier_lt_backup_ct .

    CLEAR: eo_message,
           rt_tier_lt_backup.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-tier_longterm_backup
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-tier_longterm_backup-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_tier_lt_backup = CORRESPONDING #( lt_data ).
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_tier_price_aggre.

    DATA lt_data TYPE /hec1/t_tier_price_aggre_ct.

    CLEAR: eo_message,
           rt_tier_price_aggre.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-tier_price_phase
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-tier_price_phase-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_tier_price_aggre = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_add_service.

    DATA: lt_bo_key  TYPE /bobf/t_frw_key,
          lt_alt_key TYPE /hec1/t_key_service,
          ls_alt_key LIKE LINE OF lt_alt_key.

    CLEAR ev_key_updated.
    CASE iv_update_mode.
        " ****************************************
        " Create additional service
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_add_service) = NEW /hec1/s_data_add_services_cs( ).
        ASSIGN lr_add_service->* TO FIELD-SYMBOL(<fs_add_service>).
        IF <fs_add_service> IS ASSIGNED.
          <fs_add_service> = VALUE #( BASE CORRESPONDING #( is_service )
                                      key = /bopf/cl_frw_factory=>get_new_key( ) ).

          TRY .
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_add_service
                                                       node        = /hec1/if_configuration_c=>sc_node-add_service
                                                       source_node = /hec1/if_configuration_c=>sc_node-root
                                                       association = /hec1/if_configuration_c=>sc_association-root-add_service
                                                       source_key  = me->mv_bo_landscape_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_add_service>-key                                       ) )
                IMPORTING eo_message      = DATA(lo_message)                                                                        ).

              ev_key_updated = <fs_add_service>-key .
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF.

        " ****************************************
        " Update additional service
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_service-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-add_service
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-add_service-service_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = DATA(lo_change)
                                                et_result     = DATA(lt_result)
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message ).

        TRY.
            DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. ">>>>>>>>
        ENDTRY.

        lr_add_service = NEW /hec1/s_data_add_services_cs( ).
        ASSIGN lr_add_service->* TO <fs_add_service>.
        IF <fs_add_service> IS ASSIGNED.
          <fs_add_service> = CORRESPONDING #( is_service ).

          " Get fields of structure
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_add_service> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data           = lr_add_service
                                                        node           = /hec1/if_configuration_c=>sc_node-add_service
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                  ) )
                 IMPORTING eo_message      = lo_message                                                                 ).
              ev_key_updated = lv_bo_key .
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF.


        " ****************************************
        " Delete additional service
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_service-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-add_service
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-add_service-service_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message ).

        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. ">>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data           = lr_add_service
                                                      node           = /hec1/if_configuration_c=>sc_node-add_service
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                 ) )
               IMPORTING eo_message      = lo_message                                                                ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_add_serv_price_aggre.

    DATA: lt_bo_key  TYPE /bobf/t_frw_key,
          lt_alt_key TYPE /hec1/t_key_add_serv_price_pha,
          ls_alt_key LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create additional service price
        " phase node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_price_aggre) = NEW /hec1/s_service_price_aggre_cs( ).
        ASSIGN lr_price_aggre->* TO FIELD-SYMBOL(<fs_price_aggre>).
        IF <fs_price_aggre> IS ASSIGNED.
          <fs_price_aggre> = VALUE #( BASE CORRESPONDING #( is_price_aggre )
                                      key = /bopf/cl_frw_factory=>get_new_key( ) ).

          TRY .
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_price_aggre
                                                       node        = /hec1/if_configuration_c=>sc_node-add_service_price_phase
                                                       source_node = /hec1/if_configuration_c=>sc_node-root
                                                       association = /hec1/if_configuration_c=>sc_association-root-add_service_price_phase
                                                       source_key  = me->mv_bo_root_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_price_aggre>-key                                                       ) )
                IMPORTING eo_message      = DATA(lo_message)                                                                                        ).

            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF.

        " ****************************************
        " Update additional service price
        " phase node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_price_aggre-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-add_service_price_phase
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-add_service_price_phase-add_serv_price_phase_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = DATA(lo_change)
                                                et_result     = DATA(lt_result)
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message ).

        TRY.
            DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. ">>>>>>>>
        ENDTRY.

        lr_price_aggre = NEW /hec1/s_service_price_aggre_cs( ).
        ASSIGN lr_price_aggre->* TO <fs_price_aggre>.
        IF <fs_price_aggre> IS ASSIGNED.
          <fs_price_aggre> = CORRESPONDING #( is_price_aggre ).

          " Get fields of structure
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_price_aggre> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data           = lr_price_aggre
                                                        node           = /hec1/if_configuration_c=>sc_node-add_service_price_phase
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                     ) )
                 IMPORTING eo_message      = lo_message                                                                    ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF.


        " ****************************************
        " Delete additional service price
        " phase node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_price_aggre-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-add_service_price_phase
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-add_service_price_phase-add_serv_price_phase_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message ).

        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. ">>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data           = lr_price_aggre
                                                      node           = /hec1/if_configuration_c=>sc_node-add_service_price_phase
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                                 ) )
               IMPORTING eo_message      = lo_message                                                                                ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_app_backup.

    DATA: lt_bo_key          TYPE /bobf/t_frw_key,
          lt_alt_key_storage TYPE /hec1/t_key_app_storage,
          ls_alt_key_storage LIKE LINE OF lt_alt_key_storage,
          lt_alt_key         TYPE /hec1/t_key_app_backup,
          ls_alt_key         LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create node App storage backup
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_app_backup) = NEW /hec1/s_data_app_backup_cs( ).
        ASSIGN lr_app_backup->* TO FIELD-SYMBOL(<fs_app_backup>).
        IF <fs_app_backup> IS ASSIGNED.
          <fs_app_backup> = VALUE #( BASE CORRESPONDING #( is_app_backup )
                                     key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_storage = CORRESPONDING #( is_app_backup-obj_key ).
          INSERT ls_alt_key_storage INTO TABLE lt_alt_key_storage.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_storage
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_storage-app_storage_key
                                                  it_altkey     = lt_alt_key_storage
                                        IMPORTING eo_change     = DATA(lo_change)
                                                  et_result     = DATA(lt_result)
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                                          ).
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_app_backup
                                                       node        = /hec1/if_configuration_c=>sc_node-app_storage_backup
                                                       source_node = /hec1/if_configuration_c=>sc_node-app_storage
                                                       association = /hec1/if_configuration_c=>sc_association-app_storage-app_storage_backup
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_app_backup>-key                                                     ) )
                IMPORTING eo_message      = lo_message                                                                                           ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_app_backup> IS ASSIGNED.

        " ****************************************
        " Update node App storage backup
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_app_backup-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_storage_backup
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_storage_backup-app_backup_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                     ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_app_backup = NEW /hec1/s_data_app_backup_cs( ).
        ASSIGN lr_app_backup->* TO <fs_app_backup>.
        IF <fs_app_backup> IS ASSIGNED.
          <fs_app_backup> = CORRESPONDING #( is_app_backup ).

          " Get fields of structure
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_app_backup> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_app_backup
                                                        node           = /hec1/if_configuration_c=>sc_node-app_storage_backup
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                           ) )
                 IMPORTING eo_message      = lo_message                                                                          ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_app_backup> IS ASSIGNED.

        " ****************************************
        " Delete node App storage backup
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_app_backup-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_storage_backup
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_storage_backup-app_backup_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                                      ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_app_backup
                                                      node           = /hec1/if_configuration_c=>sc_node-app_storage_backup
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                           ) )
               IMPORTING eo_message      = lo_message                                                                          ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_app_node.

    DATA: lt_bo_key           TYPE /bobf/t_frw_key,
          lt_alt_key_app_inst TYPE TABLE OF /hec1/s_key_app_server_inst,
          ls_alt_key_app_inst LIKE LINE OF lt_alt_key_app_inst,
          lt_alt_key          TYPE TABLE OF /hec1/s_key_app_node,
          ls_alt_key          LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create instance APP node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_app_node) = NEW /hec1/s_data_app_node_cs( ).
        ASSIGN lr_app_node->* TO FIELD-SYMBOL(<fs_app_node>).
        IF <fs_app_node> IS ASSIGNED.
          <fs_app_node> = VALUE #( BASE CORRESPONDING #( is_app_node )
                                   key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_app_inst = CORRESPONDING #( is_app_node-obj_key ).
          INSERT ls_alt_key_app_inst INTO TABLE lt_alt_key_app_inst.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_server_instance-app_server_inst_key
                                                  it_altkey     = lt_alt_key_app_inst
                                        IMPORTING eo_change     = DATA(lo_change)
                                                  et_result     = DATA(lt_result)
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                                                     ).
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_app_node
                                                       node        = /hec1/if_configuration_c=>sc_node-app_node
                                                       source_node = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                       association = /hec1/if_configuration_c=>sc_association-app_server_instance-app_node
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_app_node>-key                                                     ) )
                IMPORTING eo_message      = lo_message                                                                                         ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_app_node> IS ASSIGNED.

        " ****************************************
        " Update instance APP node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_app_node-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_node-app_node_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                         ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_app_node = NEW /hec1/s_data_app_node_cs( ).
        ASSIGN lr_app_node->* TO <fs_app_node>.
        IF <fs_app_node> IS ASSIGNED.
          <fs_app_node> = CORRESPONDING #( is_app_node ).

          " Get fields of structure
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_app_node> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_app_node
                                                        node           = /hec1/if_configuration_c=>sc_node-app_node
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                     ) )
                 IMPORTING eo_message      = lo_message                                                                    ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_app_node> IS ASSIGNED.

        " ****************************************
        " Delete instance App node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_app_node-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-app_node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-app_node-app_node_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                         ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_app_node
                                                      node           = /hec1/if_configuration_c=>sc_node-app_node
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                  ) )
               IMPORTING eo_message      = lo_message                                                                 ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_tier.

    DATA: lt_bo_key     TYPE /bobf/t_frw_key,
          lt_alt_key_sl TYPE TABLE OF /hec1/s_key_solution,
          ls_alt_key_sl LIKE LINE OF lt_alt_key_sl,
          lt_alt_key    TYPE TABLE OF /hec1/s_key_tier,
          ls_alt_key    LIKE LINE OF lt_alt_key.
*/BOBF/T_FRW_KEY

    CASE iv_update_mode.
        " ****************************************
        " Create tier instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_tier) = NEW /hec1/s_data_tier_cs( ).
        ASSIGN lr_tier->* TO FIELD-SYMBOL(<fs_tier>).
        IF <fs_tier> IS ASSIGNED.
          <fs_tier> = VALUE #( BASE CORRESPONDING #( is_tier )
                                     key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_sl = is_tier-hec_node_solution.
          INSERT ls_alt_key_sl INTO TABLE lt_alt_key_sl.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-solution                                " Node
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-solution-solution_key        " Alternative Key
                                                  it_altkey     = lt_alt_key_sl
                                        IMPORTING eo_change     = DATA(lo_change)                                                           " Interface for transaction change objects
                                                  et_result     = DATA(lt_result)                                                           " Key table with explicit index
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                                   ).     " Interface of Message Object
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_tier
                                                       node        = /hec1/if_configuration_c=>sc_node-tier
                                                       source_node = /hec1/if_configuration_c=>sc_node-solution
                                                       association = /hec1/if_configuration_c=>sc_association-solution-tier
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_tier>-key                                          ) )
                IMPORTING eo_message      = lo_message                                                                          ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_tier> IS ASSIGNED.

        " ****************************************
        " Update tier instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_tier-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-tier                            " Node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-tier-tier_key        " Alternative Key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change                                                         " Interface for transaction change objects
                                                et_result     = lt_result                                                         " Key table with explicit index
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                 ).     " Interface of Message Object
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_tier = NEW /hec1/s_data_tier_cs( ).
        ASSIGN lr_tier->* TO <fs_tier>.
        IF <fs_tier> IS ASSIGNED.
          <fs_tier> = CORRESPONDING #( is_tier ).

          " Get fields of structure
*          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = is_tier ).
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_tier> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_tier
                                                        node           = /hec1/if_configuration_c=>sc_node-tier
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                     ) )
                 IMPORTING eo_message      = lo_message                                                                    ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_tier> IS ASSIGNED.

        " ****************************************
        " Delete tier instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_tier-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-tier                               " Node
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-tier-tier_key           " Alternative Key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change                                                            " Interface for transaction change objects
                                                et_result     = lt_result                                                            " Key table with explicit index
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                  ).       " Interface of Message Object
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_tier
                                                      node           = /hec1/if_configuration_c=>sc_node-tier
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                               ) )
               IMPORTING eo_message      = lo_message                                                              ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_lt_backup_dc.

    CLEAR eo_message.

    DATA(lr_data) = NEW  /hec1/s_data_lt_backup_dc_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_lt_backup_dc.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-lt_backup_datacenter
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_lt_backup_cl.

    CLEAR eo_message.

    DATA(lr_data) = NEW  /hec1/s_data_lt_backup_cl_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_lt_backup_cl.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-lt_backup_class
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_lt_backup_price_aggre.
    "todo
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_man_service_baseline.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_man_serv_basel_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_man_service_baseline.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-managed_service_baseline
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_material.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_material_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_material.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-material
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_network_segment.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_network_segm_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_network_segment.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-network_segment
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_object.

    CLEAR eo_message.

    ASSIGN ir_data->* TO FIELD-SYMBOL(<fs_data>).

    " Get fields of structure
    DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_data> ).

    ASSIGN COMPONENT 'KEY' OF STRUCTURE <fs_data> TO FIELD-SYMBOL(<fs_key>).

    IF <fs_key> IS ASSIGNED.

      TRY.
          /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
             EXPORTING it_modification = VALUE #( ( data           = ir_data
                                                    node           = iv_node
                                                    change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                    changed_fields = VALUE #( FOR wa IN lt_comp
                                                                             ( wa-name ) )
                                                    key            = <fs_key> ) )
             IMPORTING eo_message      = eo_message ).
        CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
      ENDTRY.
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_phase.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_phase_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_phase.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-phase
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_root.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_config_root_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_configuration.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-root
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_software_item.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_sw_item_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_software_item.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-software_item
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_solution.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_solution_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_solution.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-solution
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_tier.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_tier_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_tier.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-tier
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_tier_add_service.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_tier_add_serv_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_service.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-tier_add_service
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_tier_price_aggre.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_tier_price_aggre_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_price_aggre.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-tier_price_phase
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_t_add_storage.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_tier_add_storage_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_t_add_storage.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-tier_add_storage
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_t_lt_backup.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_tier_lt_backup_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_t_lt_backup.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-tier_longterm_backup
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model~compare_changes.

    DATA: ls_key TYPE /bobf/s_frw_key,
          lt_key TYPE /bobf/t_frw_key.


    "no need to compare in case of a new Config Version (also a complete new Configuration is a "new Config Version" in this case)
    IF me->mv_create_new_config_version = abap_true.
      me->ms_config_changes-hec_confid           = me->ms_root_key-hec_confid.
      me->ms_config_changes-hec_conf_version     = me->ms_root_key-hec_conf_version.
      me->ms_config_changes-key                  = me->mv_bo_root_key.
      me->ms_config_changes-is_configversion_new = abap_true.

      IF iv_no_api_queue = abap_false.
        "set changes to queue for API
        /hec1/cl_snow_cmdb_factory=>get_model_instance( )->set_queue_data( is_config_changes = me->ms_config_changes ).
      ENDIF.

      RETURN. ">>>>>>>>
    ENDIF.


    TRY .
        DATA(lo_trans_mgr) = /bobf/cl_tra_trans_mgr_factory=>get_transaction_manager( ).

        DATA(lo_buffer) = /bobf/cl_frw_factory=>get_main_buffer( iv_bo_key = /hec1/if_configuration_c=>sc_bo_key ).
        DATA(lo_bopf_config) = /bobf/cl_frw_factory=>get_configuration( /hec1/if_configuration_c=>sc_bo_key ).
        DATA(lo_change) = CAST /bobf/cl_frw_change( /bobf/cl_frw_factory=>get_change( ) ).


        lo_bopf_config->get_node_tab( IMPORTING et_node = DATA(lt_node_tab) ).

        lo_change->set_attributes_requested( iv_attributes_requested = abap_true ).


        LOOP AT lo_trans_mgr->get_transactional_changes( )->get_changes( ) ASSIGNING FIELD-SYMBOL(<fs_changes>).

          <fs_changes>-change_object->get_changes( EXPORTING is_change_mode  = VALUE #( create   = abap_true
                                                                                        update   = abap_true
                                                                                        delete   = abap_true
                                                                                        load     = abap_false
                                                                                        check    = abap_false
                                                                                        property = abap_false
                                                                                        lock     = abap_false )
                                                   IMPORTING et_change       = DATA(lt_change)
                                                             et_changed_key  = DATA(lt_changed_key)
                                                             et_changed_node = DATA(lt_changed_node)
                                                  ).

          "loop over changes (hint: Buffer will collect all changes together, which can be accessed in LO_CHANGE instance)
          LOOP AT lt_change ASSIGNING FIELD-SYMBOL(<fs_change>) WHERE change_mode <> 'E'.   "E = Lock Change => not needed here
            CLEAR: lt_key.

            ls_key-key = <fs_change>-key.
            APPEND ls_key TO lt_key.

            lo_buffer->compare_states( EXPORTING iv_node_key      = <fs_change>-node_key
                                                 it_key           = lt_key
                                                 iv_state_current = /bobf/if_conf_c=>sc_state_current
                                                 iv_state_before  = /bobf/if_conf_c=>sc_state_database
                                                 io_change        = lo_change
                                                ).
          ENDLOOP.


          IF lo_change IS BOUND.
            lo_change->get( IMPORTING et_change             = DATA(lt_changes)
                                      ev_sorted             = DATA(lv_sorted)
                                      et_content_change     = DATA(lt_content_change)
                                      et_association_source = DATA(lt_assoc_source)
                                      et_change_load        = DATA(lt_change_load)
                                      et_change_load_key    = DATA(lt_changes_load_key) ).

            LOOP AT lt_changes ASSIGNING FIELD-SYMBOL(<fs_chg>).
              me->ms_config_changes-hec_confid               = me->ms_root_key-hec_confid.
              me->ms_config_changes-hec_conf_version         = me->ms_root_key-hec_conf_version.
              me->ms_config_changes-key                      = me->mv_bo_root_key.
              me->ms_config_changes-is_configversion_changed = abap_true.

              APPEND INITIAL LINE TO me->ms_config_changes-changes ASSIGNING FIELD-SYMBOL(<fs_config_changes>).
              <fs_config_changes>-node_key = <fs_chg>-node_key.

              TRY .
                  <fs_config_changes>-node_name = lt_node_tab[ node_key = <fs_chg>-node_key ]-node_name.
                CATCH cx_sy_itab_line_not_found.
              ENDTRY.

              <fs_config_changes>-key = <fs_chg>-key.
              <fs_config_changes>-change_mode = <fs_chg>-change_mode.
              <fs_config_changes>-changed_attributes = <fs_chg>-attributes.
            ENDLOOP.
          ENDIF.


          CLEAR: lt_changes,
                 lv_sorted,
                 lt_content_change,
                 lt_assoc_source,
                 lt_change_load,
                 lt_changes_load_key,
                 lt_change,
                 lt_changed_key,
                 lt_changed_node.
        ENDLOOP.

        IF iv_no_api_queue = abap_false.
          "set changes to queue for API
          /hec1/cl_snow_cmdb_factory=>get_model_instance( )->set_queue_data( is_config_changes = me->ms_config_changes ).
        ENDIF.

        rs_config_changes = me->ms_config_changes.

      CATCH /bobf/cx_frw INTO DATA(lo_ex).
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model~create_new_config.

    " Create BOPF instance root
    me->/hec1/if_bopf_config_model_set~update_root( iv_update_mode    = /bobf/if_frw_c=>sc_modify_create
                                                    is_configuration  = VALUE #( hec_confid       = me->ms_root_key-hec_confid
                                                                                 hec_conf_version = me->ms_root_key-hec_conf_version ) ).

    me->mv_create_new_config_version = abap_true.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model~save.

    /bobf/cl_tra_trans_mgr_factory=>get_transaction_manager( )->save( IMPORTING ev_rejected            = DATA(lv_rejected)
                                                                                eo_change              = DATA(lo_change)
                                                                                eo_message             = DATA(lo_message)
                                                                                et_rejecting_bo_key    = DATA(lo_reject_bo_key) ).

    IF ( lo_message IS BOUND ).
      me->set_bopf_msg_to_fpm_msg( lo_message ).
*      lo_message->get_messages( EXPORTING iv_severity = 'E'
*                                IMPORTING et_message  = DATA(lt_messages) ).
    ENDIF.

    IF lv_rejected = abap_false AND lo_message IS BOUND.
      rv_success = abap_true.
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model~save_new_version.

    rv_success = me->copy_to_new_version(
                                 EXPORTING
                                   is_config               = is_config                 " Configurator: Configuration
                                 IMPORTING
                                   ev_new_hec_conf_version =     ev_new_hec_conf_version             " Configuration Version
                               ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model~set_create_new_version.

    me->mv_create_new_config_version = iv_create_new_version.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model~set_lock_mode.

    DATA(lo_data_prov) = CAST /hec1/cl_data_provider( me->mo_data_provider ).
    lo_data_prov->set_lock_mode( iv_lock_mode = iv_lock_mode ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model~set_root_key.

    me->ms_root_key = is_root_key.

  ENDMETHOD.


  METHOD constructor.

    TRY .
        me->mo_data_provider = /hec1/cl_data_provider_factory=>get_instance( )->get_data_provider( iv_config_id      = iv_config_id
                                                                                                   iv_config_version = iv_config_version ).

        me->ms_root_key-hec_confid       = iv_config_id.
        me->ms_root_key-hec_conf_version = iv_config_version.

      CATCH /hec1/cx_data_provider.
        "makes no sense to continue
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD copy_to_new_version.
    DATA lt_keys TYPE /bobf/t_frw_node .
    DATA lt_root TYPE  /hec1/t_config_root_ct.

    DATA(lo_transaction_manager) = /bobf/cl_tra_trans_mgr_factory=>get_transaction_manager( ).

    lo_transaction_manager->create_sync_point( ).

    DATA(lo_service_manager) =   /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key ).
    lo_service_manager->do_action(
        EXPORTING
          iv_act_key              = /hec1/if_configuration_c=>sc_action-root-copy_node
          it_key                  = VALUE #( ( key = is_config-key ) )
          is_parameters           = NEW /hec1/s_act_copy_node( key = is_config-key node_key = /hec1/if_configuration_c=>sc_node-root mode = /hec1/cl_copy_controller=>gc_copy_mode-new_version )
        IMPORTING
          et_data                 = lt_keys
          eo_message              = DATA(lo_message)
          eo_change               = DATA(lo_change)
      ).

    IF lo_message IS NOT INITIAL AND lo_message->check( ).
      lo_transaction_manager->rollback_to_sync_point( ).
      rv_success = abap_false.
      RETURN.
    ENDIF.


    DATA(ls_key) = lt_keys[ node = /hec1/if_configuration_c=>sc_node-root ].
    lo_service_manager->retrieve(
      EXPORTING
        iv_node_key             = ls_key-node
        it_key                  = VALUE #( ( key = ls_key-key ) )
      IMPORTING
        et_data                 = lt_root
    ).



    IF lt_root IS INITIAL.
      rv_success = abap_false.
      lo_transaction_manager->rollback_to_sync_point( ).
      RETURN.
    ELSE.

      lo_transaction_manager->release_sync_point( ).

*      "When we create a new version we need to pass the user entered
*      "values for Configuration description and Version description
      DATA(ls_root) = lt_root[ 1 ].
      ls_root-hec_conf_descr = is_config-hec_conf_descr.
      ls_root-hec_conf_version_descr = is_config-hec_conf_version_descr.

      GET REFERENCE OF ls_root INTO DATA(lr_root).

      lo_service_manager->modify(
                   EXPORTING it_modification = VALUE #( ( data           = lr_root
                                                          node           = /hec1/if_configuration_c=>sc_node-root
                                                          change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                          changed_fields = VALUE #( ( /hec1/if_configuration_c=>sc_node_attribute-root-hec_conf_descr )
                                                                                    ( /hec1/if_configuration_c=>sc_node_attribute-root-hec_conf_version_descr )
                                                                                   )
                                                          key            = ls_root-key                     ) )
                   IMPORTING eo_message      = lo_message
                 ).
*
      /bobf/cl_tra_trans_mgr_factory=>get_transaction_manager( )->save( ).
*
*
      ev_new_hec_conf_version = ls_root-hec_conf_version.
      rv_success = abap_true.
    ENDIF.
  ENDMETHOD.


  METHOD get_bo_key_by_altern_key.

    FIELD-SYMBOLS: <fs_altkey> TYPE any.


    TRY .
        ASSIGN it_altkey[ 1 ] TO <fs_altkey>.
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

    IF <fs_altkey> IS ASSIGNED.
      TRY .
          DATA(lo_data_provider) = CAST /hec1/cl_data_provider( me->mo_data_provider ).

          DATA(ls_bo_key) = lo_data_provider->get_bo_key_by_root( EXPORTING iv_node_key = iv_node_key
                                                                            is_altkey   = <fs_altkey> ).

          IF ls_bo_key IS NOT INITIAL.
            APPEND ls_bo_key TO et_key.
          ENDIF.

        CATCH cx_root.
      ENDTRY.
    ENDIF.


  ENDMETHOD.


  METHOD get_full_name.

    DATA: lt_return TYPE tt_bapiret2,         "#EC CI_USAGE_OK[2371602]
          ls_adress TYPE bapiaddr3.


    CALL FUNCTION 'BAPI_USER_GET_DETAIL'
      EXPORTING
        username = iv_uname
      IMPORTING
        address  = ls_adress
      TABLES
        return   = lt_return.

    rv_full_name = COND #( WHEN ls_adress-firstname IS INITIAL OR ls_adress-lastname IS INITIAL THEN sy-uname
                                                                                                ELSE |{ ls_adress-firstname } { ls_adress-lastname }| ).

  ENDMETHOD.


  METHOD get_next_config_version_number.

    SELECT * FROM /hec1/d_root INTO TABLE @DATA(lt_root) WHERE hec_confid = @iv_config_id. "#EC CI_NOFIELD

    IF sy-subrc = 0.
      SORT lt_root BY hec_conf_version DESCENDING.

      TRY .
          rv_config_version = lt_root[ 1 ]-hec_conf_version.
          rv_config_version = rv_config_version + 1.

        CATCH cx_sy_itab_line_not_found.
      ENDTRY.
    ELSE.
      "nothing exist yet => set "1"
      rv_config_version = '001'.
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_tier_add_service.

    DATA: lt_bo_key       TYPE /bobf/t_frw_key,
          lt_alt_key_tier TYPE /hec1/t_key_tier,
          ls_alt_key_tier LIKE LINE OF lt_alt_key_tier,
          lt_alt_key      TYPE /hec1/t_key_tier_services,
          ls_alt_key      LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create additional service
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_add_service) = NEW /hec1/s_data_tier_add_serv_cs( ).
        ASSIGN lr_add_service->* TO FIELD-SYMBOL(<fs_add_service>).
        IF <fs_add_service> IS ASSIGNED.
          <fs_add_service> = VALUE #( BASE CORRESPONDING #( is_service )
                                      key = /bopf/cl_frw_factory=>get_new_key( ) ).

          ls_alt_key_tier = CORRESPONDING #( is_service-obj_key ).
          INSERT ls_alt_key_tier INTO TABLE lt_alt_key_tier.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-tier
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-tier-tier_key
                                                  it_altkey     = lt_alt_key_tier
                                        IMPORTING eo_change     = DATA(lo_change)
                                                  et_result     = DATA(lt_result)
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                            ).
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY .
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_add_service
                                                       node        = /hec1/if_configuration_c=>sc_node-add_service
                                                       source_node = /hec1/if_configuration_c=>sc_node-tier
                                                       association = /hec1/if_configuration_c=>sc_association-tier-tier_add_service
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_add_service>-key                                       ) )
                IMPORTING eo_message      = lo_message                                                                              ).
              ev_key_updated = <fs_add_service>-key.

            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF.

        " ****************************************
        " Update additional service
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_service-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-tier_add_service
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-tier_add_service-tier_add_service_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message ).

        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. ">>>>>>>>
        ENDTRY.

        lr_add_service = NEW /hec1/s_data_tier_add_serv_cs( ).
        ASSIGN lr_add_service->* TO <fs_add_service>.
        IF <fs_add_service> IS ASSIGNED.
          <fs_add_service> = CORRESPONDING #( is_service ).

          " Get fields of structure
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_add_service> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data           = lr_add_service
                                                        node           = /hec1/if_configuration_c=>sc_node-tier_add_service
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                     ) )
                 IMPORTING eo_message      = lo_message                                                                    ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF.


        " ****************************************
        " Delete additional service
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_service-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-tier_add_service
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-tier_add_service-tier_add_service_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message ).

        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. ">>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data           = lr_add_service
                                                      node           = /hec1/if_configuration_c=>sc_node-tier_add_service
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                 ) )
               IMPORTING eo_message      = lo_message                                                                ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_set~update_tier_price_aggre.

    DATA: lt_bo_key       TYPE /bobf/t_frw_key,
          lt_alt_key_tier TYPE TABLE OF /hec1/s_key_tier,
          ls_alt_key_tier LIKE LINE OF lt_alt_key_tier,
          lt_alt_key      TYPE TABLE OF /hec1/s_key_tier_price_phase,
          ls_alt_key      LIKE LINE OF lt_alt_key.


    CASE iv_update_mode.
        " ****************************************
        " Create material instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_create.
        DATA(lr_tier_price_aggre) = NEW /hec1/s_tier_price_aggre_cs( ).
        ASSIGN lr_tier_price_aggre->* TO FIELD-SYMBOL(<fs_tier_price_aggre>).
        IF <fs_tier_price_aggre> IS ASSIGNED.
          <fs_tier_price_aggre> = VALUE #( BASE CORRESPONDING #( is_price_aggre )
                                         key = /bopf/cl_frw_factory=>get_new_key( ) ).         " Get new technical key

          ls_alt_key_tier = CORRESPONDING #( is_price_aggre-obj_key ).
          INSERT ls_alt_key_tier INTO TABLE lt_alt_key_tier.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-tier                             " Node
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-tier-tier_key         " Alternative Key
                                                  it_altkey     = lt_alt_key_tier
                                        IMPORTING eo_change     = DATA(lo_change)                                                    " Interface for transaction change objects
                                                  et_result     = DATA(lt_result)                                                    " Key table with explicit index
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)                                            ).     " Interface of Message Object
          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                EXPORTING it_modification = VALUE #( ( data        = lr_tier_price_aggre
                                                       node        = /hec1/if_configuration_c=>sc_node-tier_price_phase
                                                       source_node = /hec1/if_configuration_c=>sc_node-tier
                                                       association = /hec1/if_configuration_c=>sc_association-tier-tier_price_phase
                                                       source_key  = lv_bo_key
                                                       change_mode = /bobf/if_frw_c=>sc_modify_create
                                                       key         = <fs_tier_price_aggre>-key                                      ) )
                IMPORTING eo_message      = lo_message                                                                          ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_material> IS ASSIGNED.

        " ****************************************
        " Update material instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_update.
        ls_alt_key = is_price_aggre-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-tier_price_phase
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-tier_price_phase-tier_price_phase_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                           ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        lr_tier_price_aggre = NEW /hec1/s_tier_price_aggre_cs( ).
        ASSIGN lr_tier_price_aggre->* TO <fs_tier_price_aggre>.
        IF <fs_tier_price_aggre> IS ASSIGNED.
          <fs_tier_price_aggre> = CORRESPONDING #( is_price_aggre ).

          " Get fields of structure
*          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = is_material ).
          DATA(lt_comp) = /rbp/cl_general_utilities=>get_components_of_struc( is_data = <fs_tier_price_aggre> ).

          TRY.
              /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
                 EXPORTING it_modification = VALUE #( ( data          = lr_tier_price_aggre
                                                        node           = /hec1/if_configuration_c=>sc_node-tier_price_phase
                                                        change_mode    = /bobf/if_frw_c=>sc_modify_update
                                                        changed_fields = VALUE #( FOR wa IN lt_comp
                                                                                 ( wa-name )        )
                                                        key            = lv_bo_key                                  ) )
                 IMPORTING eo_message      = lo_message                                                                ).
            CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
          ENDTRY.
        ENDIF. "IF <fs_material> IS ASSIGNED.

        " ****************************************
        " Delete material instance node
        " ****************************************
      WHEN /bobf/if_frw_c=>sc_modify_delete.
        ls_alt_key = is_price_aggre-obj_key.
        INSERT ls_alt_key INTO TABLE lt_alt_key.

        me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-tier_price_phase
                                                iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-tier_price_phase-tier_price_phase_key
                                                it_altkey     = lt_alt_key
                                      IMPORTING eo_change     = lo_change
                                                et_result     = lt_result
                                                et_key        = lt_bo_key
                                                eo_message    = lo_message                                                           ).
        TRY.
            lv_bo_key = lt_bo_key[ 1 ]-key.
          CATCH cx_sy_itab_line_not_found.
            RETURN. " >>>>>>>>
        ENDTRY.

        TRY.
            /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->modify(
               EXPORTING it_modification = VALUE #( ( data          = lr_tier_price_aggre
                                                      node           = /hec1/if_configuration_c=>sc_node-tier_price_phase
                                                      change_mode    = /bobf/if_frw_c=>sc_modify_delete
                                                      key            = lv_bo_key                                  ) )
               IMPORTING eo_message      = lo_message                                                                 ).
          CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
        ENDTRY.
    ENDCASE. "CASE iv_update_mode.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_add_service.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_add_services_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_service.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-add_service
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_add_serv_price_aggre.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_service_price_aggre_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_price_aggre.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-add_service_price_phase
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_app_backup.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_app_backup_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_app_backup.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-app_storage_backup
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_app_node.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_app_node_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_app_node.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-app_node
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_app_server.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_app_serv_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_app_server.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-app_server
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_app_server_inst.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_app_serv_inst_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_app_server_inst.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_app_server_pc.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_app_serv_pc_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_app_serv_pc.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_app_storage.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_app_storage_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_app_storage.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-app_storage
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_app_storage_qty.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_app_storageqty_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_app_storage_qty.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-app_storage_amount
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_connectivity.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_connectivity_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_connectivity.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-connectivity
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_connect_price_aggre.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_connect_price_aggre_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_price_aggre.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-connectivity_price_phase
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_datacenter.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_datacenter_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_datacenter.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-datacenter
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_db_backup.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_db_backup_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_db_backup.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-db_storage_backup
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_db_node.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_db_node_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_db_node.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-db_node
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_db_server.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_db_serv_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_db_server.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-db_server
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_db_server_inst.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_db_server_inst_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_db_server_inst.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_db_server_pc.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_db_serv_pc_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_db_serv_pc.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_db_storage.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_db_storage_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_db_storage.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-db_storage
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_db_storage_qty.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_db_storage_qty_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_db_storage_qty.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node = /hec1/if_configuration_c=>sc_node-db_storage_amount
                                                               ir_data = lr_data "is_db_storage_qty
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_delivery_unit.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_dlvy_unit_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_delivery_unit.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-delivery_unit
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_if_baseline.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_if_baseline_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_if_baseline.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-infrastructure_baseline
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_instance_db.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_db_inst_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_db_instance.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-instance_db
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_landscape_price_aggre.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_landsc_price_aggre_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_price_aggre.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-landsc_base_price_phase
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_db_server_pc.

    DATA lt_data TYPE /hec1/t_data_db_serv_pc_ct.

    CLEAR: eo_message,
           rt_db_serv_pc.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-db_server_perform_cat-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_db_serv_pc = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~select_material.
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~select_software_item.
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_add_service_multi.

    DATA: ls_key          TYPE /hec1/s_key_tier,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_solution IS INITIAL AND
           iv_guid_tier     IS INITIAL.

          "get ALL for complete Config
          rt_service = me->mo_data_provider->get_tier_add_service_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution = iv_guid_solution.
          ls_key-hec_node_tier     = iv_guid_tier.

          "determine source key structure
          IF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_tier_add_serv_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_service = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_add_service_single.

    TRY .
        rs_service = me->mo_data_provider->get_tier_add_service( is_key = VALUE #( hec_node_solution     = iv_guid_solution
                                                                              hec_node_tier         = iv_guid_tier
                                                                              hec_node_tier_service = iv_guid_tier_service  ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_app_node_multi.

    DATA: ls_key          TYPE /hec1/s_key_app_server_inst,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.


    TRY .
        IF iv_guid_solution      IS INITIAL AND
           iv_guid_tier          IS INITIAL AND
           iv_guid_app_serv_inst IS INITIAL.

          "get ALL for complete Config
*          rt_app_node = me->mo_data_provider->get_app_nodes_by_config( is_config_key = me->ms_root_key ).
          rt_app_node = me->mo_data_provider->get_app_nodes_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution      = iv_guid_solution.
          ls_key-hec_node_tier          = iv_guid_tier.
          ls_key-hec_node_app_serv_inst = iv_guid_app_serv_inst.

          "determine source key structure
          IF iv_guid_app_serv_inst IS NOT INITIAL.
            IF iv_guid_tier     IS INITIAL OR
               iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-app_srv_inst.
            ENDIF.
          ELSEIF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_app_node_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_app_node = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_app_node_single.

    TRY .
        rs_app_node = CORRESPONDING #( me->mo_data_provider->get_app_node( is_key = VALUE #( hec_node_solution      = iv_guid_solution
                                                                            hec_node_tier          = iv_guid_tier
                                                                            hec_node_app_serv_inst = iv_guid_app_serv_inst
                                                                            hec_node_app_node      = iv_guid_app_node       ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_app_server_inst_multi.

    DATA: ls_key          TYPE /hec1/s_key_tier,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.


    TRY .
        IF iv_guid_solution      IS INITIAL AND
           iv_guid_tier          IS INITIAL.

          "get ALL for complete Config
*          rt_app_serv_inst = me->mo_data_provider->get_app_server_insts_by_config( is_config_key = me->ms_root_key ).
          rt_app_serv_inst = me->mo_data_provider->get_app_server_insts_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution      = iv_guid_solution.
          ls_key-hec_node_tier          = iv_guid_tier.

          "determine source key structure
          IF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_app_serv_inst_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_app_serv_inst = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_app_server_inst_single.

    TRY .
        rs_app_serv_inst = CORRESPONDING #( me->mo_data_provider->get_app_server_inst( is_key = VALUE #( hec_node_solution      = iv_guid_solution
                                                                                        hec_node_tier          = iv_guid_tier
                                                                                        hec_node_app_serv_inst = iv_guid_app_serv_inst ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_app_server_multi.

    DATA: ls_key          TYPE /hec1/s_key_app_serv_pc,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.


    TRY .
        IF iv_guid_solution      IS INITIAL AND
           iv_guid_tier          IS INITIAL AND
           iv_guid_app_serv_inst IS INITIAL AND
           iv_guid_app_node      IS INITIAL AND
           iv_guid_app_serv_pc   IS INITIAL.

          "get ALL for complete Config
*          rt_app_server = me->mo_data_provider->get_app_servers_by_config( is_config_key = me->ms_root_key ).
          rt_app_server = me->mo_data_provider->get_app_servers_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution      = iv_guid_solution.
          ls_key-hec_node_tier          = iv_guid_tier.
          ls_key-hec_node_app_serv_inst = iv_guid_app_serv_inst.
          ls_key-hec_node_app_node      = iv_guid_app_node.
          ls_key-hec_node_app_serv_pc   = iv_guid_app_serv_pc.

          "determine source key structure
          IF iv_guid_app_serv_pc IS NOT INITIAL.
            IF iv_guid_app_node      IS INITIAL OR
               iv_guid_app_serv_inst IS INITIAL OR
               iv_guid_tier          IS INITIAL OR
               iv_guid_solution      IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-app_srv_pc.
            ENDIF.
          ELSEIF iv_guid_app_node IS NOT INITIAL.
            IF iv_guid_app_serv_inst IS INITIAL OR
               iv_guid_tier          IS INITIAL OR
               iv_guid_solution      IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-app_node.
            ENDIF.
          ELSEIF iv_guid_app_serv_inst IS NOT INITIAL.
            IF iv_guid_tier     IS INITIAL OR
               iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-app_srv_inst.
            ENDIF.
          ELSEIF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_app_serv_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_app_server = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_app_server_pc_multi.

    DATA: ls_key          TYPE /hec1/s_key_app_node,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.


    TRY .
        IF iv_guid_solution      IS INITIAL AND
           iv_guid_tier          IS INITIAL AND
           iv_guid_app_serv_inst IS INITIAL AND
           iv_guid_app_node      IS INITIAL.

          "get ALL for complete Config
*          rt_app_serv_pc = me->mo_data_provider->get_app_server_pcats_by_config( is_config_key = me->ms_root_key ).
          rt_app_serv_pc = me->mo_data_provider->get_app_server_pcats_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution      = iv_guid_solution.
          ls_key-hec_node_tier          = iv_guid_tier.
          ls_key-hec_node_app_serv_inst = iv_guid_app_serv_inst.
          ls_key-hec_node_app_node      = iv_guid_app_node.

          "determine source key structure
          IF iv_guid_app_node IS NOT INITIAL.
            IF iv_guid_app_serv_inst IS INITIAL OR
               iv_guid_tier          IS INITIAL OR
               iv_guid_solution      IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-app_node.
            ENDIF.
          ELSEIF iv_guid_app_serv_inst IS NOT INITIAL.
            IF iv_guid_tier     IS INITIAL OR
               iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-app_srv_inst.
            ENDIF.
          ELSEIF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_app_serv_pc_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_app_serv_pc = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_app_server_pc_single.

    TRY .
        rs_app_serv_pc = CORRESPONDING #( me->mo_data_provider->get_app_server_pcat( is_key = VALUE #( hec_node_solution      = iv_guid_solution
                                                                                      hec_node_tier          = iv_guid_tier
                                                                                      hec_node_app_serv_inst = iv_guid_app_serv_inst
                                                                                      hec_node_app_node      = iv_guid_app_node
                                                                                      hec_node_app_serv_pc   = iv_guid_app_serv_pc  ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_app_server_single.

    TRY .
        rs_app_server = CORRESPONDING #( me->mo_data_provider->get_app_server( is_key = VALUE #( hec_node_solution      = iv_guid_solution
                                                                                hec_node_tier          = iv_guid_tier
                                                                                hec_node_app_serv_inst = iv_guid_app_serv_inst
                                                                                hec_node_app_node      = iv_guid_app_node
                                                                                hec_node_app_serv_pc   = iv_guid_app_serv_pc
                                                                                hec_node_app_server    = iv_guid_app_server   ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_app_storage_backup_multi.

    DATA: ls_key          TYPE /hec1/s_key_app_storage,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_solution      IS INITIAL AND
           iv_guid_tier          IS INITIAL AND
           iv_guid_app_serv_inst IS INITIAL AND
           iv_guid_app_node      IS INITIAL AND
           iv_guid_app_serv_pc   IS INITIAL AND
           iv_guid_app_server    IS INITIAL AND
           iv_guid_app_storage   IS INITIAL.

          "get ALL for complete Config
          rt_storage_backup = me->mo_data_provider->get_app_backups_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution      = iv_guid_solution.
          ls_key-hec_node_tier          = iv_guid_tier.
          ls_key-hec_node_app_serv_inst = iv_guid_app_serv_inst.
          ls_key-hec_node_app_node      = iv_guid_app_node.
          ls_key-hec_node_app_serv_pc   = iv_guid_app_serv_pc.
          ls_key-hec_node_app_server    = iv_guid_app_server.
          ls_key-hec_node_app_storage   = iv_guid_app_storage.

          "determine source key structure
          IF iv_guid_app_storage IS NOT INITIAL.
            IF iv_guid_app_server    IS INITIAL OR
               iv_guid_app_serv_pc   IS INITIAL OR
               iv_guid_app_node      IS INITIAL OR
               iv_guid_app_serv_inst IS INITIAL OR
               iv_guid_tier          IS INITIAL OR
               iv_guid_solution      IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-app_storage.
            ENDIF.
          ELSEIF iv_guid_app_server IS NOT INITIAL.
            IF iv_guid_app_serv_pc   IS INITIAL OR
               iv_guid_app_node      IS INITIAL OR
               iv_guid_app_serv_inst IS INITIAL OR
               iv_guid_tier          IS INITIAL OR
               iv_guid_solution      IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-app_srv.
            ENDIF.
          ELSEIF iv_guid_app_serv_pc IS NOT INITIAL.
            IF iv_guid_app_node      IS INITIAL OR
               iv_guid_app_serv_inst IS INITIAL OR
               iv_guid_tier          IS INITIAL OR
               iv_guid_solution      IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-app_srv_pc.
            ENDIF.
          ELSEIF iv_guid_app_node IS NOT INITIAL.
            IF iv_guid_app_serv_inst IS INITIAL OR
               iv_guid_tier          IS INITIAL OR
               iv_guid_solution      IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-app_node.
            ENDIF.
          ELSEIF iv_guid_app_serv_inst IS NOT INITIAL.
            IF iv_guid_tier     IS INITIAL OR
               iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-app_srv_inst.
            ENDIF.
          ELSEIF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_app_backup_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_storage_backup = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_app_storage_backup_single.

    TRY.
        rs_storage_backup = me->mo_data_provider->get_app_backup( is_key = VALUE #( hec_node_solution      = iv_guid_solution
                                                                                    hec_node_tier          = iv_guid_tier
                                                                                    hec_node_app_serv_inst = iv_guid_app_serv_inst
                                                                                    hec_node_app_node      = iv_guid_app_node
                                                                                    hec_node_app_serv_pc   = iv_guid_app_serv_pc
                                                                                    hec_node_app_server    = iv_guid_app_server
                                                                                    hec_node_app_storage   = iv_guid_app_storage
                                                                                    hec_node_app_backup    = iv_guid_app_backup    ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_app_storage_multi.

    DATA: ls_key          TYPE /hec1/s_key_app_serv,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.


    TRY .
        IF iv_guid_solution      IS INITIAL AND
           iv_guid_tier          IS INITIAL AND
           iv_guid_app_serv_inst IS INITIAL AND
           iv_guid_app_node      IS INITIAL AND
           iv_guid_app_serv_pc   IS INITIAL AND
           iv_guid_app_server    IS INITIAL.

          "get ALL for complete Config
*          rt_app_storage = me->mo_data_provider->get_app_storages_by_config( is_config_key = me->ms_root_key ).
          rt_app_storage = me->mo_data_provider->get_app_storages_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution      = iv_guid_solution.
          ls_key-hec_node_tier          = iv_guid_tier.
          ls_key-hec_node_app_serv_inst = iv_guid_app_serv_inst.
          ls_key-hec_node_app_node      = iv_guid_app_node.
          ls_key-hec_node_app_serv_pc   = iv_guid_app_serv_pc.
          ls_key-hec_node_app_server    = iv_guid_app_server.

          "determine source key structure
          IF iv_guid_app_server IS NOT INITIAL.
            IF iv_guid_app_serv_pc   IS INITIAL OR
               iv_guid_app_node      IS INITIAL OR
               iv_guid_app_serv_inst IS INITIAL OR
               iv_guid_tier          IS INITIAL OR
               iv_guid_solution      IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-app_srv.
            ENDIF.
          ELSEIF iv_guid_app_serv_pc IS NOT INITIAL.
            IF iv_guid_app_node      IS INITIAL OR
               iv_guid_app_serv_inst IS INITIAL OR
               iv_guid_tier          IS INITIAL OR
               iv_guid_solution      IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-app_srv_pc.
            ENDIF.
          ELSEIF iv_guid_app_node IS NOT INITIAL.
            IF iv_guid_app_serv_inst IS INITIAL OR
               iv_guid_tier          IS INITIAL OR
               iv_guid_solution      IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-app_node.
            ENDIF.
          ELSEIF iv_guid_app_serv_inst IS NOT INITIAL.
            IF iv_guid_tier     IS INITIAL OR
               iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-app_srv_inst.
            ENDIF.
          ELSEIF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_app_storage_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_app_storage = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_app_storage_qty_multi.

    DATA: ls_key          TYPE /hec1/s_key_app_serv_pc,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.


    TRY .
        IF iv_guid_solution      IS INITIAL AND
           iv_guid_tier          IS INITIAL AND
           iv_guid_app_serv_inst IS INITIAL AND
           iv_guid_app_node      IS INITIAL AND
           iv_guid_app_serv_pc   IS INITIAL.

          "get ALL for complete Config
*          rt_app_storage_qty = me->mo_data_provider->get_app_storage_amns_by_config( is_config_key = me->ms_root_key ).
          rt_app_storage_qty = me->mo_data_provider->get_app_storage_amns_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution      = iv_guid_solution.
          ls_key-hec_node_tier          = iv_guid_tier.
          ls_key-hec_node_app_serv_inst = iv_guid_app_serv_inst.
          ls_key-hec_node_app_node      = iv_guid_app_node.
          ls_key-hec_node_app_serv_pc   = iv_guid_app_serv_pc.

          "determine source key structure
          IF iv_guid_app_serv_pc IS NOT INITIAL.
            IF iv_guid_app_node      IS INITIAL OR
               iv_guid_app_serv_inst IS INITIAL OR
               iv_guid_tier          IS INITIAL OR
               iv_guid_solution      IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-app_srv_pc.
            ENDIF.
          ELSEIF iv_guid_app_node IS NOT INITIAL.
            IF iv_guid_app_serv_inst IS INITIAL OR
               iv_guid_tier          IS INITIAL OR
               iv_guid_solution      IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-app_node.
            ENDIF.
          ELSEIF iv_guid_app_serv_inst IS NOT INITIAL.
            IF iv_guid_tier     IS INITIAL OR
               iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-app_srv_inst.
            ENDIF.
          ELSEIF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_app_storageqty_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_app_storage_qty = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_app_storage_qty_single.

    TRY .
        rs_app_storage_qty = CORRESPONDING #( me->mo_data_provider->get_app_storage_amn( is_key = VALUE #( hec_node_solution        = iv_guid_solution
                                                                                          hec_node_tier            = iv_guid_tier
                                                                                          hec_node_app_serv_inst   = iv_guid_app_serv_inst
                                                                                          hec_node_app_node        = iv_guid_app_node
                                                                                          hec_node_app_serv_pc     = iv_guid_app_serv_pc
                                                                                          hec_node_app_storage_qty = iv_guid_app_storage_qty ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_app_storage_single.

    TRY .
        rs_app_storage = CORRESPONDING #( me->mo_data_provider->get_app_storage( is_key = VALUE #( hec_node_solution      = iv_guid_solution
                                                                                  hec_node_tier          = iv_guid_tier
                                                                                  hec_node_app_serv_inst = iv_guid_app_serv_inst
                                                                                  hec_node_app_node      = iv_guid_app_node
                                                                                  hec_node_app_serv_pc   = iv_guid_app_serv_pc
                                                                                  hec_node_app_server    = iv_guid_app_server
                                                                                  hec_node_app_storage   = iv_guid_app_storage    ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_configuration.

    DATA: lt_bo_key            TYPE /bobf/t_frw_key,
          lt_alt_key           TYPE TABLE OF /hec1/s_key_root,
          ls_alt_key           LIKE LINE OF lt_alt_key,
          lt_alt_key_landscape TYPE TABLE OF /hec1/landscape_guid,
          ls_alt_key_landscape LIKE LINE OF lt_alt_key_landscape,
          lt_alt_key_dlvy_unit TYPE TABLE OF /hec1/delivery_unit_guid,
          ls_alt_key_dlvy_unit LIKE LINE OF lt_alt_key_dlvy_unit.

    TRY .
        rs_configuration = me->mo_data_provider->get_landscape_by_config( ).

        "read root BO key, if not set yet
        IF me->mv_bo_root_key IS INITIAL.
          CLEAR: lt_bo_key.

          ls_alt_key = me->ms_root_key.
          INSERT ls_alt_key INTO TABLE lt_alt_key.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-root
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-root-root_key
                                                  it_altkey     = lt_alt_key
                                        IMPORTING eo_change     = DATA(lo_change)
                                                  et_result     = DATA(lt_result)
                                                  et_key        = lt_bo_key
                                                  eo_message    = DATA(lo_message)
                                                  ).

          TRY.
              DATA(lv_bo_key) = lt_bo_key[ 1 ]-key.
              me->mv_bo_root_key = lv_bo_key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.
        ENDIF.

        IF me->mv_bo_dlvy_unit_key IS INITIAL.
          CLEAR: lt_bo_key,
                 lv_bo_key.

          ls_alt_key_dlvy_unit = me->/hec1/if_bopf_config_model_get~get_delivery_unit( )-hec_node_delivery_unit.
          INSERT ls_alt_key_dlvy_unit INTO TABLE lt_alt_key_dlvy_unit.

          me->get_bo_key_by_altern_key( EXPORTING iv_node_key   = /hec1/if_configuration_c=>sc_node-delivery_unit
                                                  iv_altkey_key = /hec1/if_configuration_c=>sc_alternative_key-delivery_unit-dlvy_unit_key
                                                  it_altkey     = lt_alt_key_dlvy_unit
                                        IMPORTING eo_change     = lo_change
                                                  et_result     = lt_result
                                                  et_key        = lt_bo_key
                                                  eo_message    = lo_message ).

          TRY.
              lv_bo_key = lt_bo_key[ 1 ]-key.
              me->mv_bo_dlvy_unit_key = lv_bo_key.
            CATCH cx_sy_itab_line_not_found.
              RETURN. " >>>>>>>>
          ENDTRY.
        ENDIF.


      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_connectivity_multi.

    DATA: ls_key          TYPE /hec1/datacenter_guid,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_datacenter IS INITIAL.

          "get ALL for complete Config
*          rt_connectivity = me->mo_data_provider->get_connectivities_by_config( is_config_key = me->ms_root_key ).
          rt_connectivity = me->mo_data_provider->get_connectivities_by_config( ).

        ELSE.
          "set key structure
          ls_key          = iv_guid_datacenter.
          lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-datacenter.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_connectivity_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          <fs_key> = iv_guid_datacenter.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_connectivity = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_connectivity_single.

    TRY .
        rs_connectivity = CORRESPONDING #( me->mo_data_provider->get_connectivity( is_key = VALUE #( hec_node_datacenter   = iv_guid_datacenter
                                                                                    hec_node_connectivity = iv_guid_connectivity ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_connect_price_aggre_multi.

    DATA: ls_key          TYPE /hec1/landscape_guid,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_landscape IS INITIAL.

          "get ALL for complete Config
          rt_connect_price_aggre = CORRESPONDING #( me->mo_data_provider->get_conn_price_aggre_by_config( ) ).

        ELSE.
          "set key structure
          ls_key          = iv_guid_landscape.
          lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-landscape.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_connect_price_aggre_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          <fs_key> = iv_guid_landscape.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_connect_price_aggre = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_connect_price_aggre_single.

    TRY .
        rs_connect_price_aggre = CORRESPONDING #( me->mo_data_provider->get_connect_price_aggregation( is_key = VALUE #( hec_node_landscape    = iv_guid_landscape
                                                                                                        hec_node_connectivity = iv_guid_connectivity ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_datacenter_multi.

    TRY .
*        rt_datacenter = me->mo_data_provider->get_datacenters_by_config( is_config_key = me->ms_root_key ).
        rt_datacenter = me->mo_data_provider->get_datacenters_by_config( ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_datacenter_single.

    TRY .
        rs_datacenter = CORRESPONDING #( me->mo_data_provider->get_datacenter( is_key = iv_guid_datacenter ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_db_node_multi.

    DATA: ls_key          TYPE /hec1/s_key_db_inst,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_solution     IS INITIAL AND
           iv_guid_tier         IS INITIAL AND
           iv_guid_db_serv_inst IS INITIAL AND
           iv_guid_db_inst      IS INITIAL.

          "get ALL for complete Config
*          rt_db_node = me->mo_data_provider->get_db_nodes_by_config( is_config_key = me->ms_root_key ).
          rt_db_node = me->mo_data_provider->get_db_nodes_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution     = iv_guid_solution.
          ls_key-hec_node_tier         = iv_guid_tier.
          ls_key-hec_node_db_serv_inst = iv_guid_db_serv_inst.
          ls_key-hec_node_db_inst      = iv_guid_db_inst.

          "determine source key structure
          IF iv_guid_db_inst IS NOT INITIAL.
            IF iv_guid_db_serv_inst IS INITIAL OR
               iv_guid_tier         IS INITIAL OR
               iv_guid_solution     IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_inst.
            ENDIF.
          ELSEIF iv_guid_db_serv_inst IS NOT INITIAL.
            IF iv_guid_tier     IS INITIAL OR
               iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_srv_inst.
            ENDIF.
          ELSEIF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_db_node_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_db_node = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~create_phase.

    IF iv_phase_key IS INITIAL.
      RETURN. ">>>>>>>
    ENDIF.

    TRY.
        /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->do_action( EXPORTING iv_act_key           = /hec1/if_configuration_c=>sc_action-phase-create
                                                                                                                        it_key               = VALUE #( ( key = iv_phase_key ) )
                                                                                                                        is_parameters        = REF #( is_create_param )
                                                                                                              IMPORTING eo_message           = DATA(lo_message)
                                                                                                                        et_failed_key        = DATA(lt_failed_key)
                                                                                                                        et_failed_action_key = DATA(lt_failed_action) ).

      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~delete_node.

    " IV_TREE_TYPE is set to distribution by default. Only when deleting phases does the tree type need to be passed.

    " IV_KEY and IV_NODE can be read from the current tree entry in most cases
    "       Only for objects like Managed Service Baseline or Network Segment
    "       these values need to be taken as they don't have tree entries.

    DATA(lo_tree) = /hec1/cl_bopf_config_ui_tree_h=>get_instance( ).

    IF iv_key IS NOT INITIAL
      AND iv_node IS NOT INITIAL.

      DATA(lv_node_type) = iv_node.
      DATA(lv_key) = iv_key.

    ELSE.
      "get selection
      CASE iv_tree_type.
        WHEN /hec1/if_config_constants=>gc_tree_type-distribution.
          DATA(lt_tree_dist) = lo_tree->/hec1/if_bopf_config_ui_tree_h~get_hierarchy( ).
          DATA(ls_selection_dist) = VALUE #( lt_tree_dist[ hec_lead_selection = abap_true ] OPTIONAL ).
          lv_node_type = ls_selection_dist-hec_obj_type.
        WHEN /hec1/if_config_constants=>gc_tree_type-phasing.
          DATA(lt_tree_phase) = lo_tree->/hec1/if_bopf_config_ui_tree_h~get_hierarchy_phasing( ).
          DATA(ls_selection_phase) = VALUE #( lt_tree_phase[ hec_lead_selection = abap_true ] OPTIONAL ).
          lv_node_type = ls_selection_phase-hec_obj_type.
      ENDCASE.

      lv_key = COND #( WHEN lv_node_type = /hec1/if_config_constants=>gc_tree_child-phase
                       THEN lo_tree->/hec1/if_bopf_config_ui_tree_h~get_tree_line_phasing(
                               lo_tree->/hec1/if_bopf_config_ui_tree_h~get_lead_selection_tree_key(
                                 iv_tree_type = /hec1/if_config_constants=>gc_tree_type-phasing ) )-node_key
                       ELSE lo_tree->/hec1/if_bopf_config_ui_tree_h~get_tree_line(
                               lo_tree->/hec1/if_bopf_config_ui_tree_h~get_lead_selection_tree_key( ) )-node_key  ).

    ENDIF.

    "***************************
    " Get root key
    "***************************
    " we need the root key at this point, because the delete action is performed on the root level
    " so we need a node that can give us the root key (e.g. landscape)
    DATA(ls_root) = me->/hec1/if_bopf_config_model_get~get_root( ).

    DATA(ls_delete_parameter) = VALUE /hec1/s_act_delete_node( node     = lv_node_type
                                                               root_key = ls_root-root_key
                                                               key      = lv_key ).

    TRY.
        /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->do_action( EXPORTING iv_act_key           = /hec1/if_configuration_c=>sc_action-root-delete_node
                                                                                                                        it_key               = VALUE #( ( key = ls_root-key ) )
                                                                                                                        is_parameters        = REF #( ls_delete_parameter )
                                                                                                              IMPORTING eo_message           = DATA(lo_message)
                                                                                                                        et_failed_key        = DATA(lt_failed_key)
                                                                                                                        et_failed_action_key = DATA(lt_failed_action) ).

      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

    IF lo_message IS BOUND.
      me->set_bopf_msg_to_fpm_msg( lo_message ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~do_synchronize_container.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~do_synchronize_node.

    CHECK: iv_key      IS NOT INITIAL,
           iv_node_key IS NOT INITIAL.

    TRY.
        /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->do_action( EXPORTING iv_act_key           = SWITCH #( iv_node_key
                                                                                                                                                         WHEN /hec1/if_configuration_c=>sc_node-app_node
                                                                                                                                                         THEN /hec1/if_configuration_c=>sc_action-app_node-sync_config
                                                                                                                                                         ELSE /hec1/if_configuration_c=>sc_action-db_node-sync_config  )
                                                                                                                        it_key               = VALUE #( ( key = iv_key ) )
                                                                                                              IMPORTING eo_message           = DATA(lo_message)
                                                                                                                        et_failed_key        = DATA(lt_failed_key)
                                                                                                                        et_failed_action_key = DATA(lt_failed_action)                                    ).


      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

    IF lo_message IS BOUND.
      me->set_bopf_msg_to_fpm_msg( lo_message ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~get_material_list.

    TRY.
        /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->do_action( EXPORTING iv_act_key           = /hec1/if_configuration_c=>sc_action-solution-get_material_list
                                                                                                                        it_key               = VALUE #( ( key = is_solution-key ) )
                                                                                                              IMPORTING eo_message           = DATA(lo_message)
                                                                                                                        et_failed_key        = DATA(lt_failed_key)
                                                                                                                        et_failed_action_key = DATA(lt_failed_action)                                                  ).

      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

    IF lo_message IS BOUND.
      me->set_bopf_msg_to_fpm_msg( lo_message ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~get_software_item_list.
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~modify_app_server_instance.

    TRY.
        /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->do_action( EXPORTING iv_act_key           = /hec1/if_configuration_c=>sc_action-app_server_instance-modify_cluster_type
                                                                                                                        it_key               = VALUE #( ( key = iv_key ) )
                                                                                                                        is_parameters        = REF #( is_app_server_instance )
                                                                                                              IMPORTING eo_message           = DATA(lo_message)
                                                                                                                        et_failed_key        = DATA(lt_failed_key)
                                                                                                                        et_failed_action_key = DATA(lt_failed_action)                                                  ).


      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

    IF lo_message IS BOUND.
      me->set_bopf_msg_to_fpm_msg( lo_message ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~modify_instance_db.

    TRY.
        /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->do_action( EXPORTING iv_act_key           = /hec1/if_configuration_c=>sc_action-instance_db-modify_cluster_type
                                                                                                                        it_key               = VALUE #( ( key = iv_key ) )
                                                                                                                        is_parameters        = REF #( is_instance_db )
                                                                                                              IMPORTING eo_message           = DATA(lo_message)
                                                                                                                        et_failed_key        = DATA(lt_failed_key)
                                                                                                                        et_failed_action_key = DATA(lt_failed_action) ).

      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

    IF lo_message IS BOUND.
      me->set_bopf_msg_to_fpm_msg( lo_message ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~reset_app_backup.

    TRY.
        /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->do_action( EXPORTING iv_act_key           = /hec1/if_configuration_c=>sc_action-app_storage_backup-reset_backup
                                                                                                                        it_key               = VALUE #( ( key = iv_key ) )
                                                                                                              IMPORTING eo_message           = DATA(lo_message)
                                                                                                                        et_failed_key        = DATA(lt_failed_key)
                                                                                                                        et_failed_action_key = DATA(lt_failed_action)                                              ).


      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

    IF lo_message IS BOUND.
      me->set_bopf_msg_to_fpm_msg( lo_message ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~reset_app_server.

    TRY.
        /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->do_action( EXPORTING iv_act_key           = /hec1/if_configuration_c=>sc_action-app_server-reset_server
                                                                                                                        it_key               = VALUE #( ( key = iv_key ) )
                                                                                                              IMPORTING eo_message           = DATA(lo_message)
                                                                                                                        et_failed_key        = DATA(lt_failed_key)
                                                                                                                        et_failed_action_key = DATA(lt_failed_action)                                       ).


      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

    IF lo_message IS BOUND.
      me->set_bopf_msg_to_fpm_msg( lo_message ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~reset_app_server_instance.

    " differentiate between different fields
    DATA(lv_action) = COND /bobf/act_key( WHEN iv_fieldname = /hec1/if_configuration_c=>sc_node_attribute-app_server_instance-hec_sol_tier_stack_si_guid
                                          THEN /hec1/if_configuration_c=>sc_action-app_server_instance-reset_server_instance
                                          WHEN iv_fieldname = /hec1/if_configuration_c=>sc_node_attribute-app_server_instance-hec_sol_apsi_oper_sys_guid
                                          THEN /hec1/if_configuration_c=>sc_action-app_server_instance-reset_operating_system                             ).


    TRY.
        /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->do_action( EXPORTING iv_act_key           = lv_action
                                                                                                                        it_key               = VALUE #( ( key = iv_key ) )
                                                                                                              IMPORTING eo_message           = DATA(lo_message)
                                                                                                                        et_failed_key        = DATA(lt_failed_key)
                                                                                                                        et_failed_action_key = DATA(lt_failed_action)                                                  ).


      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

    IF lo_message IS BOUND.
      me->set_bopf_msg_to_fpm_msg( lo_message ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~reset_app_server_pc.

    TRY.
        /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->do_action( EXPORTING iv_act_key           = /hec1/if_configuration_c=>sc_action-app_server_perform_cat-reset_server_pc
                                                                                                                        it_key               = VALUE #( ( key = iv_key ) )
                                                                                                              IMPORTING eo_message           = DATA(lo_message)
                                                                                                                        et_failed_key        = DATA(lt_failed_key)
                                                                                                                        et_failed_action_key = DATA(lt_failed_action)                                                  ).


      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

    IF lo_message IS BOUND.
      me->set_bopf_msg_to_fpm_msg( lo_message ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~reset_app_storage.

    TRY.
        /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->do_action( EXPORTING iv_act_key           = /hec1/if_configuration_c=>sc_action-app_storage-reset_storage
                                                                                                                        it_key               = VALUE #( ( key = iv_key ) )
                                                                                                              IMPORTING eo_message           = DATA(lo_message)
                                                                                                                        et_failed_key        = DATA(lt_failed_key)
                                                                                                                        et_failed_action_key = DATA(lt_failed_action)                                        ).


      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

    IF lo_message IS BOUND.
      me->set_bopf_msg_to_fpm_msg( lo_message ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~reset_connectivity.
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~reset_datacenter.
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~reset_db_backup.

    TRY.
        /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->do_action( EXPORTING iv_act_key           = /hec1/if_configuration_c=>sc_action-db_storage_backup-reset_backup
                                                                                                                        it_key               = VALUE #( ( key = iv_key ) )
                                                                                                              IMPORTING eo_message           = DATA(lo_message)
                                                                                                                        et_failed_key        = DATA(lt_failed_key)
                                                                                                                        et_failed_action_key = DATA(lt_failed_action)                                              ).


      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

    IF lo_message IS BOUND.
      me->set_bopf_msg_to_fpm_msg( lo_message ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~reset_db_server.

    TRY.
        /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->do_action( EXPORTING iv_act_key           = /hec1/if_configuration_c=>sc_action-db_server-reset_server
                                                                                                                        it_key               = VALUE #( ( key = iv_key ) )
                                                                                                              IMPORTING eo_message           = DATA(lo_message)
                                                                                                                        et_failed_key        = DATA(lt_failed_key)
                                                                                                                        et_failed_action_key = DATA(lt_failed_action)                                     ).


      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

    IF lo_message IS BOUND.
      me->set_bopf_msg_to_fpm_msg( lo_message ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~reset_db_server_instance.

    " differentiate between different fields
    DATA(lv_action) = COND /bobf/act_key( WHEN iv_fieldname = /hec1/if_configuration_c=>sc_node_attribute-db_server_instance-hec_sol_tier_stack_si_guid
                                          THEN /hec1/if_configuration_c=>sc_action-db_server_instance-modify_server_instance
                                          WHEN iv_fieldname = /hec1/if_configuration_c=>sc_node_attribute-db_server_instance-hec_sol_tier_dsi_dbstype_guid
                                          THEN /hec1/if_configuration_c=>sc_action-db_server_instance-modify_db_type
                                          WHEN iv_fieldname = /hec1/if_configuration_c=>sc_node_attribute-db_server_instance-hec_sol_dbst_impltype_guid
                                          THEN /hec1/if_configuration_c=>sc_action-db_server_instance-modify_implement_type
                                          WHEN iv_fieldname = /hec1/if_configuration_c=>sc_node_attribute-db_server_instance-hec_sol_dbst_impty_instty_guid
                                          THEN /hec1/if_configuration_c=>sc_action-db_server_instance-modify_instance_type
                                          WHEN iv_fieldname = /hec1/if_configuration_c=>sc_node_attribute-db_server_instance-hec_sol_dbst_imty_inty_al_guid
                                          THEN /hec1/if_configuration_c=>sc_action-db_server_instance-modify_allocation
                                          WHEN iv_fieldname = /hec1/if_configuration_c=>sc_node_attribute-db_server_instance-hec_sol_dbst_oper_sys_guid
                                          THEN /hec1/if_configuration_c=>sc_action-db_server_instance-reset_operating_system                              ).


    TRY.
        /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->do_action( EXPORTING iv_act_key           = lv_action
                                                                                                                        it_key               = VALUE #( ( key = iv_key ) )
                                                                                                                        is_parameters        = REF #( is_db_serv_inst )
                                                                                                              IMPORTING eo_message           = DATA(lo_message)
                                                                                                                        et_failed_key        = DATA(lt_failed_key)
                                                                                                                        et_failed_action_key = DATA(lt_failed_action) ).

      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

    IF lo_message IS BOUND.
      me->set_bopf_msg_to_fpm_msg( lo_message ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~reset_db_server_pc.

    TRY.
        /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->do_action( EXPORTING iv_act_key           = /hec1/if_configuration_c=>sc_action-db_server_perform_cat-reset_server_pc
                                                                                                                        it_key               = VALUE #( ( key = iv_key ) )
                                                                                                              IMPORTING eo_message           = DATA(lo_message)
                                                                                                                        et_failed_key        = DATA(lt_failed_key)
                                                                                                                        et_failed_action_key = DATA(lt_failed_action)                                                  ).

      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

    IF lo_message IS BOUND.
      me->set_bopf_msg_to_fpm_msg( lo_message ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~reset_db_storage.

    TRY.
        /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key )->do_action( EXPORTING iv_act_key           = /hec1/if_configuration_c=>sc_action-db_storage-reset_storage
                                                                                                                        it_key               = VALUE #( ( key = iv_key ) )
                                                                                                              IMPORTING eo_message           = DATA(lo_message)
                                                                                                                        et_failed_key        = DATA(lt_failed_key)
                                                                                                                        et_failed_action_key = DATA(lt_failed_action)                                       ).


      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

    IF lo_message IS BOUND.
      me->set_bopf_msg_to_fpm_msg( lo_message ).
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~reset_delivery_unit.
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~reset_landscape.
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~reset_service.
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~reset_solution.
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~reset_tier.
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~reset_tier_service.
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_db_node_single.

    TRY .
        rs_db_node = CORRESPONDING #( me->mo_data_provider->get_db_node( is_key = VALUE #( hec_node_solution     = iv_guid_solution
                                                                          hec_node_tier         = iv_guid_tier
                                                                          hec_node_db_serv_inst = iv_guid_db_serv_inst
                                                                          hec_node_db_inst      = iv_guid_db_inst
                                                                          hec_node_db_node      = iv_guid_db_node      ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_service_multi.

    DATA: ls_key          TYPE /hec1/landscape_guid,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_landscape IS INITIAL.

          "get ALL for complete Config
          rt_service = me->mo_data_provider->get_services_by_config( ).

        ELSE.
          "set key structure
          ls_key          = iv_guid_landscape.
          lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-landscape.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_add_services_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          <fs_key> = iv_guid_landscape.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_service = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_tier_add_service_multi.

    DATA: ls_key          TYPE /hec1/landscape_guid,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_landscape IS INITIAL.

          "get ALL for complete Config
          rt_tier_add_service = me->mo_data_provider->get_tier_add_service_by_config( ).

        ELSE.
          "set key structure
          ls_key          = iv_guid_landscape.
          lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-landscape.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_tier_add_serv_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          <fs_key> = iv_guid_landscape.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_tier_add_service = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_service_price_aggre_multi.

    DATA: ls_key          TYPE /hec1/landscape_guid,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_landscape IS INITIAL.

          "get ALL for complete Config
          rt_service_price_aggre = CORRESPONDING #( me->mo_data_provider->get_addsrv_price_aggre_by_conf( ) ).

        ELSE.
          "set key structure
          ls_key          = iv_guid_landscape.
          lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-landscape.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_service_price_aggre_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          <fs_key> = iv_guid_landscape.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_service_price_aggre = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_service_single.

    TRY .
        rs_service = CORRESPONDING #( me->mo_data_provider->get_service( is_key = iv_guid_service ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_software_item_multi.

    DATA: ls_key          TYPE /hec1/s_key_material,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.


    TRY .
        IF iv_guid_solution IS INITIAL AND
           iv_guid_tier     IS INITIAL AND
           iv_guid_material IS INITIAL.

          "get ALL for complete Config
*          rt_software_item = me->mo_data_provider->get_software_items_by_config( is_config_key = me->ms_root_key ).
          rt_software_item = me->mo_data_provider->get_software_items_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution = iv_guid_solution.
          ls_key-hec_node_tier     = iv_guid_tier.
          ls_key-hec_node_material = iv_guid_material.

          "determine source key structure
          IF iv_guid_material IS NOT INITIAL.
            IF iv_guid_tier     IS INITIAL OR
               iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-material.
            ENDIF.
          ELSEIF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_sw_item_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_software_item = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_software_item_single.

    TRY .
        rs_software_item = CORRESPONDING #( me->mo_data_provider->get_software_item( is_key = VALUE #( hec_node_solution = iv_guid_solution
                                                                                      hec_node_tier     = iv_guid_tier
                                                                                      hec_node_material = iv_guid_material
                                                                                      hec_node_sw_item  = iv_guid_software_item  ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_solution_multi.

    TRY .
*        rt_solution = me->mo_data_provider->get_solutions_by_config( is_config_key = me->ms_root_key ).
        rt_solution = me->mo_data_provider->get_solutions_by_config( ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_solution_single.

    TRY .
        rs_solution = CORRESPONDING #( me->mo_data_provider->get_solution( is_key = iv_guid_solution ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_tier_multi.

    DATA: ls_key          TYPE /hec1/solution_guid,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_solution IS INITIAL.

          "get ALL for complete Config
*          rt_tier = me->mo_data_provider->get_tiers_by_config( is_config_key = me->ms_root_key ).
          rt_tier = me->mo_data_provider->get_tiers_by_config( ).

        ELSE.
          "set key structure
          ls_key          = iv_guid_solution.
          lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_tier_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          <fs_key> = iv_guid_solution.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_tier = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_tier_price_aggre_multi.

    DATA: ls_key          TYPE /hec1/s_key_tier,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_solution IS INITIAL AND
           iv_guid_tier     IS INITIAL.

          "get ALL for complete Config
          rt_tier_price_aggre = CORRESPONDING #( me->mo_data_provider->get_tier_price_aggre_by_config( ) ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution = iv_guid_solution.
          ls_key-hec_node_tier     = iv_guid_tier.

          "determine source key structure
          IF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_tier_price_aggre_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_tier_price_aggre = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_tier_single.

    TRY .
        rs_tier = CORRESPONDING #( me->mo_data_provider->get_tier( is_key = VALUE #( hec_node_solution = iv_guid_solution
                                                                    hec_node_tier     = iv_guid_tier      ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_tree_distribut.
* Not used
    DATA: ls_datacenter       TYPE REF TO /hec1/s_data_datacenter,
          ls_connectivity     TYPE REF TO /hec1/s_data_connectivity,
          ls_add_service      TYPE REF TO /hec1/s_data_add_services,
          ls_solution         TYPE REF TO /hec1/s_data_solution,
          ls_tier             TYPE REF TO /hec1/s_data_tier,
          ls_material         TYPE REF TO /hec1/s_data_material,
          ls_software_item    TYPE REF TO /hec1/s_data_sw_item,
          ls_tier_add_service TYPE REF TO /hec1/s_data_tier_add_services,
          ls_db_serv_inst	    TYPE REF TO /hec1/s_data_db_server_inst,
          ls_db_inst          TYPE REF TO /hec1/s_data_db_inst,
          ls_db_node          TYPE REF TO /hec1/s_data_db_node,
          ls_db_serv_pc       TYPE REF TO /hec1/s_data_db_serv_pc,
          ls_db_storage_qty   TYPE REF TO /hec1/s_data_db_storage_qty,
          ls_db_server        TYPE REF TO /hec1/s_data_db_serv,
          ls_db_storage       TYPE REF TO /hec1/s_data_db_storage,
          ls_db_backup        TYPE REF TO /hec1/s_data_db_backup,
          ls_app_serv_inst    TYPE REF TO /hec1/s_data_app_server_inst,
          ls_app_node         TYPE REF TO /hec1/s_data_app_node,
          ls_app_serv_pc      TYPE REF TO /hec1/s_data_app_serv_pc,
          ls_app_storage_qty  TYPE REF TO /hec1/s_data_app_storage_qty,
          ls_app_server       TYPE REF TO /hec1/s_data_app_serv,
          ls_app_storage      TYPE REF TO /hec1/s_data_app_storage,
          ls_app_backup       TYPE REF TO /hec1/s_data_app_backup,
          lv_timestamp        TYPE timestampl.

    "TODO: In Process

    " This method should returns the entire tree structure of a configuration. It will be called when the tree is setup initially
    " It should be called whenever there are changes in the tree structure, like adding or removing nodes
    " It should also be used to communicate changes in status and description to the UI

    " Future addition: The method could also be used to return part of the tree, like a single branch
    "     - remove text logic and add the object type to the description field inside the object itself

    DATA(lo_text_provider) = /hec1/cl_config_text_provider=>get_instance( /hec1/if_config_constants=>gc_classname-text_provider ).

    TRY.
        DATA(ls_landscape)       = me->mo_data_provider->get_landscape_by_config( ).
        DATA(ls_delivery_unit)   = me->mo_data_provider->get_delivery_unit_by_config( ).
        DATA(lt_datacenter)      = me->mo_data_provider->get_datacenters_by_config( ).
        DATA(lt_connectivity)    = me->mo_data_provider->get_connectivities_by_config( ).
        DATA(lt_add_service)     = me->mo_data_provider->get_services_by_config( ).
        DATA(lt_solution)        = me->mo_data_provider->get_solutions_by_config( ).
        DATA(lt_tier)            = me->mo_data_provider->get_tiers_by_config( ).
        DATA(lt_material)        = me->mo_data_provider->get_materials_by_config( ).
        DATA(lt_software_item)   = me->mo_data_provider->get_software_items_by_config( ).
        DATA(lt_tier_add_serv)   = me->mo_data_provider->get_tier_add_service_by_config( ).
        DATA(lt_db_server_inst)  = me->mo_data_provider->get_db_server_insts_by_config( ).
        DATA(lt_instance_db)     = me->mo_data_provider->get_db_instances_by_config( ).
        DATA(lt_db_node)         = me->mo_data_provider->get_db_nodes_by_config( ).
        DATA(lt_db_server_pc)    = me->mo_data_provider->get_db_server_pcats_by_config( ).
        DATA(lt_db_storage_qty)  = me->mo_data_provider->get_db_storage_amnts_by_config( ).
        DATA(lt_db_server)       = me->mo_data_provider->get_db_servers_by_config( ).
        DATA(lt_db_storage)      = me->mo_data_provider->get_db_storages_by_config( ).
        DATA(lt_db_backup)       = me->mo_data_provider->get_db_backups_by_config( ).
        DATA(lt_app_server_inst) = me->mo_data_provider->get_app_server_insts_by_config( ).
        DATA(lt_app_node)        = me->mo_data_provider->get_app_nodes_by_config( ).
        DATA(lt_app_server_pc)   = me->mo_data_provider->get_app_server_pcats_by_config( ).
        DATA(lt_app_storage_qty) = me->mo_data_provider->get_app_storage_amns_by_config( ).
        DATA(lt_app_server)      = me->mo_data_provider->get_app_servers_by_config( ).
        DATA(lt_app_storage)     = me->mo_data_provider->get_app_storages_by_config( ).
        DATA(lt_app_backup)      = me->mo_data_provider->get_app_backups_by_config( ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

    " Landscape
    GET TIME STAMP FIELD lv_timestamp.
    DATA(lv_landscape_row_key) = |{ lv_timestamp }|.

    APPEND VALUE #( BASE CORRESPONDING #( ls_landscape )
                    row_key    = lv_landscape_row_key
                    expanded   = abap_true
                    is_leaf    = abap_true
                    image_src  = COND #( WHEN ls_landscape-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                         THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                         ELSE /hec1/if_config_constants=>gc_image_status-complete )
                    text       = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-landscape
                                                             para1 = COND #( WHEN ls_landscape-hec_landscape_descr IS NOT INITIAL
                                                                              AND ls_landscape-hec_landscape_descr NA |:|
                                                                             THEN |: { ls_landscape-hec_landscape_descr }|
                                                                             ELSE ls_landscape-hec_landscape_descr ) )
                    hec_add_visible    = abap_false
                    hec_delete_visible = abap_false
                    hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-landscape
                    hec_node_landscape = /hec1/if_config_constants=>gc_tree_child-landscape
                    hec_row_selectable = abap_true
                    ) TO rt_distribut_tree.

    " Delivery Unit
    GET TIME STAMP FIELD lv_timestamp.
    DATA(lv_dlvy_unit_row_key) = |{ lv_timestamp }|.

    APPEND VALUE #( BASE CORRESPONDING #( ls_delivery_unit )
                    parent_key = lv_landscape_row_key
                    row_key    = lv_dlvy_unit_row_key
                    expanded   = abap_true
                    is_leaf    = abap_true
                    image_src  = COND #( WHEN ls_delivery_unit-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                         THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                         ELSE /hec1/if_config_constants=>gc_image_status-complete )
                    text       = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-delivery_unit
                                                             para1 = COND #( WHEN ls_delivery_unit-hec_delivery_unit_descr IS NOT INITIAL
                                                                              AND ls_delivery_unit-hec_delivery_unit_descr NA |:|
                                                                             THEN |: { ls_delivery_unit-hec_delivery_unit_descr }|
                                                                             ELSE ls_delivery_unit-hec_delivery_unit_descr ) )
                    hec_row_selectable = abap_true
                    hec_add_visible    = abap_true
                    hec_delete_visible = abap_false
                    hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-delivery_unit
                    hec_node_delivery_unit = /hec1/if_config_constants=>gc_tree_child-delivery_unit
                    ) TO rt_distribut_tree.

    " Folder Data Center
    GET TIME STAMP FIELD lv_timestamp.
    DATA(lv_datacenter_fl_row_key) = |{ lv_timestamp }|.

    APPEND VALUE #( BASE CORRESPONDING #( ls_delivery_unit )
                    parent_key         = lv_dlvy_unit_row_key
                    row_key            = lv_datacenter_fl_row_key
                    expanded           = abap_true
                    is_leaf            = abap_true
                    image_src          = /hec1/if_config_constants=>gc_image_status-folder
                    text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-datacenter_fl
                                                                     para1 = ' '      )
                    hec_row_selectable = abap_false
                    hec_add_visible    = abap_false
                    hec_delete_visible = abap_false
                    hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-datacenter_fl
                    ) TO rt_distribut_tree.

    " Datacenter
    LOOP AT lt_datacenter ASSIGNING FIELD-SYMBOL(<fs_datacenter>).

      GET TIME STAMP FIELD lv_timestamp.
      DATA(lv_datacenter_row_key) = |{ lv_timestamp }|.

      APPEND VALUE #( BASE CORRESPONDING #( <fs_datacenter> )
                      parent_key         = lv_datacenter_fl_row_key
                      row_key            = lv_datacenter_row_key
                      expanded           = abap_true
                      is_leaf            = abap_true
                      image_src          = COND #( WHEN <fs_datacenter>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                   THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                   ELSE /hec1/if_config_constants=>gc_image_status-complete )
                      text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-datacenter
                                                                       para1 = COND #( WHEN <fs_datacenter>-hec_tree_descr IS NOT INITIAL
                                                                                        AND <fs_datacenter>-hec_tree_descr NA |:|
                                                                                       THEN |: { <fs_datacenter>-hec_tree_descr }|
                                                                                       ELSE <fs_datacenter>-hec_tree_descr ) )
                      hec_delete_visible = COND #( WHEN <fs_datacenter>-hec_phase_guid IS NOT INITIAL
                                                   THEN abap_false
                                                   ELSE abap_true )
                      hec_row_selectable = abap_true
                      hec_add_visible    = abap_true
                      hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-datacenter
                    ) TO rt_distribut_tree.

      " Connectivity
      LOOP AT lt_connectivity ASSIGNING FIELD-SYMBOL(<fs_connectivity>) WHERE hec_node_datacenter = <fs_datacenter>-hec_node_datacenter.

        GET TIME STAMP FIELD lv_timestamp.
        DATA(lv_connectivity_row_key) = |{ lv_timestamp }|.

        APPEND VALUE #( BASE CORRESPONDING #( <fs_connectivity> )
                        parent_key         = lv_datacenter_row_key
                        row_key            = lv_connectivity_row_key
                        expanded           = abap_true
                        is_leaf            = abap_true
                        image_src          = COND #( WHEN <fs_connectivity>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                     THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                     ELSE /hec1/if_config_constants=>gc_image_status-complete )
                        text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-connectivity
                                                                         para1 = COND #( WHEN <fs_connectivity>-hec_tree_descr IS NOT INITIAL
                                                                                          AND <fs_connectivity>-hec_tree_descr NA |:|
                                                                                         THEN |: { <fs_connectivity>-hec_tree_descr }|
                                                                                         ELSE <fs_connectivity>-hec_tree_descr ) )
                        hec_row_selectable = <fs_connectivity>-hec_row_selectable
                        hec_add_visible    = abap_false
                        hec_delete_visible = abap_true
                        hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-connectivity
                        ) TO rt_distribut_tree.

      ENDLOOP. "lt_connectivity

    ENDLOOP. "lt_datacenter

    " Folder Additional Service
    GET TIME STAMP FIELD lv_timestamp.
    DATA(lv_add_service_fl_row_key) = |{ lv_timestamp }|.

    APPEND VALUE #( BASE CORRESPONDING #( ls_landscape )
                    parent_key         = lv_landscape_row_key
                    row_key            = |{ lv_add_service_fl_row_key }|
                    expanded           = abap_true
                    is_leaf            = abap_true
                    image_src          = /hec1/if_config_constants=>gc_image_status-folder
                    text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-add_service_fl
                                                                     para1 = ' '      )
                    hec_row_selectable = abap_false
                    hec_add_visible    = abap_false
                    hec_delete_visible = abap_false
                    hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-add_service_fl
                    ) TO rt_distribut_tree.

    " Additional Services
    LOOP AT lt_add_service ASSIGNING FIELD-SYMBOL(<fs_add_service>).

      GET TIME STAMP FIELD lv_timestamp.
      DATA(lv_service_row_key) = |{ lv_timestamp }|.

      APPEND VALUE #( BASE CORRESPONDING #( <fs_add_service> )
                      parent_key         = lv_add_service_fl_row_key
                      row_key            = lv_service_row_key
                      expanded           = abap_true
                      is_leaf            = abap_true
                      image_src          = COND #( WHEN <fs_add_service>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                   THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                   ELSE /hec1/if_config_constants=>gc_image_status-complete )
                      text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-add_service
                                                                       para1 = COND #( WHEN <fs_add_service>-hec_tree_descr IS NOT INITIAL
                                                                                        AND <fs_add_service>-hec_tree_descr NA |:|
                                                                                       THEN |: { <fs_add_service>-hec_tree_descr }|
                                                                                       ELSE <fs_add_service>-hec_tree_descr ) )
                      hec_delete_visible = abap_true
                      hec_row_selectable = abap_true
                      hec_add_visible    = abap_false
                      hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-add_service
                      ) TO rt_distribut_tree.

    ENDLOOP.

    " Folder Solution
    GET TIME STAMP FIELD lv_timestamp.
    DATA(lv_solution_fl_row_key) = |{ lv_timestamp }|.

    APPEND VALUE #( BASE CORRESPONDING #( ls_landscape )
                    parent_key         = lv_landscape_row_key
                    row_key            = lv_solution_fl_row_key
                    expanded           = abap_true
                    is_leaf            = abap_true
                    image_src          = /hec1/if_config_constants=>gc_image_status-folder
                    text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-solution_fl
                                                                     para1 = ' '      )
                    hec_row_selectable = abap_false
                    hec_add_visible    = abap_false
                    hec_delete_visible = abap_false
                    hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-solution_fl
                    ) TO rt_distribut_tree.

    " Solution
    LOOP AT lt_solution ASSIGNING FIELD-SYMBOL(<fs_solution>).

      GET TIME STAMP FIELD lv_timestamp.
      DATA(lv_solution_row_key) = |{ lv_timestamp }|.

      APPEND VALUE #( BASE CORRESPONDING #( <fs_solution> )
                      parent_key         = lv_solution_fl_row_key
                      row_key            = lv_solution_row_key
                      expanded           = abap_true
                      is_leaf            = abap_true
                      image_src          = COND #( WHEN <fs_solution>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                   THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                   ELSE /hec1/if_config_constants=>gc_image_status-complete )
                      text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-solution
                                                                       para1 = COND #( WHEN <fs_solution>-hec_tree_descr IS NOT INITIAL
                                                                                        AND <fs_solution>-hec_tree_descr NA |:|
                                                                                       THEN |: { <fs_solution>-hec_tree_descr }|
                                                                                       ELSE <fs_solution>-hec_tree_descr ) )
                      hec_delete_visible = abap_true
                      hec_row_selectable = abap_true
                      hec_add_visible    = abap_false
                      hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-solution
      ) TO rt_distribut_tree.

      " Tier
      LOOP AT lt_tier ASSIGNING FIELD-SYMBOL(<fs_tier>)
        WHERE hec_node_solution = <fs_solution>-hec_node_solution.

        GET TIME STAMP FIELD lv_timestamp.
        DATA(lv_tier_row_key) = |{ lv_timestamp }|.

        APPEND VALUE #( BASE CORRESPONDING #( <fs_tier> )
                        parent_key         = lv_solution_row_key
                        row_key            = lv_tier_row_key
                        expanded           = abap_true
                        is_leaf            = abap_true
                        image_src          = COND #( WHEN <fs_tier>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                     THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                     ELSE /hec1/if_config_constants=>gc_image_status-complete )
                        text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-tier
                                                                         para1 = COND #( WHEN <fs_tier>-hec_tree_descr IS NOT INITIAL
                                                                                          AND <fs_tier>-hec_tree_descr NA |:|
                                                                                         THEN |: { <fs_tier>-hec_tree_descr }|
                                                                                         ELSE <fs_tier>-hec_tree_descr ) )
                        hec_delete_visible = abap_true
                        hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-tier
                        ) TO rt_distribut_tree.

        " Folder Software
        GET TIME STAMP FIELD lv_timestamp.
        DATA(lv_software_fl_row_key) = |{ lv_timestamp }|.

        APPEND VALUE #( BASE CORRESPONDING #( <fs_tier> )
                        parent_key         = lv_tier_row_key
                        row_key            = lv_software_fl_row_key
                        expanded           = abap_true
                        is_leaf            = abap_true
                        image_src          = /hec1/if_config_constants=>gc_image_status-folder
                        text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-software_fl
                                                                         para1 = ' '      )
                        hec_row_selectable = abap_false
                        hec_add_visible    = abap_false
                        hec_delete_visible = abap_false
                        hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-software_fl
                        ) TO rt_distribut_tree.

        " Material
        LOOP AT lt_material ASSIGNING FIELD-SYMBOL(<fs_material>)
          WHERE hec_node_solution = <fs_tier>-hec_node_solution
            AND hec_node_tier     = <fs_tier>-hec_node_tier.

          GET TIME STAMP FIELD lv_timestamp.
          DATA(lv_material_row_key) = |{ lv_timestamp }|.

          APPEND VALUE #( BASE CORRESPONDING #( <fs_material> )
                          parent_key         = lv_software_fl_row_key
                          row_key            = lv_material_row_key
                          expanded           = abap_true
                          is_leaf            = abap_true
                          image_src          = COND #( WHEN <fs_material>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                       THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                       ELSE /hec1/if_config_constants=>gc_image_status-complete )
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-material
                                                                           para1 = COND #( WHEN <fs_material>-hec_tree_descr IS NOT INITIAL
                                                                                            AND <fs_material>-hec_tree_descr NA |:|
                                                                                           THEN |: { <fs_material>-hec_tree_descr }|
                                                                                           ELSE <fs_material>-hec_tree_descr ) )
                          hec_delete_visible = abap_true
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-material
                          ) TO rt_distribut_tree.

          " Software Item
          LOOP AT lt_software_item ASSIGNING FIELD-SYMBOL(<fs_software_item>)
            WHERE hec_node_solution = <fs_material>-hec_node_solution
              AND hec_node_tier     = <fs_material>-hec_node_tier
              AND hec_node_material = <fs_material>-hec_node_material.

            GET TIME STAMP FIELD lv_timestamp.
            DATA(lv_software_item_row_key) = |{ lv_timestamp }|.

            APPEND VALUE #( BASE CORRESPONDING #( <fs_software_item> )
                            parent_key         = lv_material_row_key
                            row_key            = lv_software_item_row_key
                            expanded           = abap_true
                            is_leaf            = abap_true
                            image_src          = COND #( WHEN <fs_tier>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                         THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                         ELSE /hec1/if_config_constants=>gc_image_status-complete )
                            text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-software_item
                                                                             para1 = COND #( WHEN <fs_software_item>-hec_tree_descr IS NOT INITIAL
                                                                                              AND <fs_software_item>-hec_tree_descr NA |:|
                                                                                             THEN |: { <fs_software_item>-hec_tree_descr }|
                                                                                             ELSE <fs_software_item>-hec_tree_descr ) )
                            hec_delete_visible = abap_true
                            hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-software_item
                            ) TO rt_distribut_tree.

          ENDLOOP. "software_item
        ENDLOOP. "material

        " Folder additional tier service
        GET TIME STAMP FIELD lv_timestamp.
        DATA(lv_tier_service_fl_row_key) = |{ lv_timestamp }|.

        APPEND VALUE #( BASE CORRESPONDING #( <fs_tier> )
                        parent_key         = lv_tier_row_key
                        row_key            = lv_tier_service_fl_row_key
                        expanded           = abap_true
                        is_leaf            = abap_true
                        image_src          = /hec1/if_config_constants=>gc_image_status-folder
                        text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-tier_service_fl
                                                                         para1 = ' '      )
                        hec_row_selectable = abap_false
                        hec_add_visible    = abap_false
                        hec_delete_visible = abap_false
                        hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-tier_serv_fl
                        ) TO rt_distribut_tree.

        " Tier Additional Services
        LOOP AT lt_tier_add_serv ASSIGNING FIELD-SYMBOL(<fs_tier_add_service>)
          WHERE hec_node_solution = <fs_tier>-hec_node_solution
            AND hec_node_tier     = <fs_tier>-hec_node_tier.

          GET TIME STAMP FIELD lv_timestamp.
          DATA(lv_tier_add_service_row_key) = |{ lv_timestamp }|.

          APPEND VALUE #( BASE CORRESPONDING #( <fs_tier_add_service> )
                          parent_key         = lv_tier_service_fl_row_key
                          row_key            = lv_tier_add_service_row_key
                          expanded           = abap_true
                          is_leaf            = abap_true
                          image_src          = COND #( WHEN <fs_tier_add_service>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                       THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                       ELSE /hec1/if_config_constants=>gc_image_status-complete )
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-tier_service
                                                                           para1 = COND #( WHEN <fs_tier_add_service>-hec_tree_descr IS NOT INITIAL
                                                                                            AND <fs_tier_add_service>-hec_tree_descr NA |:|
                                                                                           THEN |: { <fs_tier_add_service>-hec_tree_descr }|
                                                                                           ELSE <fs_tier_add_service>-hec_tree_descr ) )
                          hec_delete_visible = abap_true
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-tier_service
                          ) TO rt_distribut_tree.

        ENDLOOP. "tier additional service

        " DB Server Instance
        LOOP AT lt_db_server_inst ASSIGNING FIELD-SYMBOL(<fs_db_server_inst>)
          WHERE hec_node_solution = <fs_tier>-hec_node_solution
            AND hec_node_tier     = <fs_tier>-hec_node_tier.

          GET TIME STAMP FIELD lv_timestamp.
          DATA(lv_db_server_inst_row_key) = |{ lv_timestamp }|.

          APPEND VALUE #( BASE CORRESPONDING #( <fs_db_server_inst> )
                          parent_key         = lv_tier_row_key
                          row_key            = lv_db_server_inst_row_key
                          expanded           = abap_true
                          is_leaf            = abap_true
                          image_src          = COND #( WHEN <fs_db_server_inst>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                       THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                       ELSE /hec1/if_config_constants=>gc_image_status-complete )
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-db_serv_inst
                                                                           para1 = COND #( WHEN <fs_db_server_inst>-hec_tree_descr IS NOT INITIAL
                                                                                            AND <fs_db_server_inst>-hec_tree_descr NA |:|
                                                                                           THEN |: { <fs_db_server_inst>-hec_tree_descr }|
                                                                                           ELSE <fs_db_server_inst>-hec_tree_descr ) )
                          hec_delete_visible = abap_false
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-db_serv_inst
                          ) TO rt_distribut_tree.

          " Instance DB
          LOOP AT lt_instance_db ASSIGNING FIELD-SYMBOL(<fs_instance_db>)
            WHERE hec_node_solution     = <fs_db_server_inst>-hec_node_solution
              AND hec_node_tier         = <fs_db_server_inst>-hec_node_tier
              AND hec_node_db_serv_inst = <fs_db_server_inst>-hec_node_db_serv_inst.

            GET TIME STAMP FIELD lv_timestamp.
            DATA(lv_instance_db_row_key) = |{ lv_timestamp }|.

            APPEND VALUE #( BASE CORRESPONDING #( <fs_instance_db> )
                            parent_key         = lv_db_server_inst_row_key
                            row_key            = lv_instance_db_row_key
                            expanded           = abap_true
                            is_leaf            = abap_true
                            image_src          = COND #( WHEN <fs_instance_db>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                         THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                         ELSE /hec1/if_config_constants=>gc_image_status-complete )
                            text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-db_inst
                                                                             para1 = COND #( WHEN <fs_instance_db>-hec_tree_descr IS NOT INITIAL
                                                                                              AND <fs_instance_db>-hec_tree_descr NA |:|
                                                                                             THEN |: { <fs_instance_db>-hec_tree_descr }|
                                                                                             ELSE <fs_instance_db>-hec_tree_descr ) )
                            hec_delete_visible = abap_false
                            hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-db_inst
                            ) TO rt_distribut_tree.

            " DB Node
            SORT lt_db_node ASCENDING BY hec_db_cluster_type_value.

            LOOP AT lt_db_node ASSIGNING FIELD-SYMBOL(<fs_db_node>)
              WHERE hec_node_solution     = <fs_instance_db>-hec_node_solution
                AND hec_node_tier         = <fs_instance_db>-hec_node_tier
                AND hec_node_db_serv_inst = <fs_instance_db>-hec_node_db_serv_inst
                AND hec_node_db_inst      = <fs_instance_db>-hec_node_db_inst.

              GET TIME STAMP FIELD lv_timestamp.
              DATA(lv_db_node_row_key) = |{ lv_timestamp }|.

              APPEND VALUE #( BASE CORRESPONDING #( <fs_db_node> )
                              parent_key         = lv_instance_db_row_key
                              row_key            = lv_db_node_row_key
                              expanded           = abap_true
                              is_leaf            = abap_true
                              image_src          = COND #( WHEN <fs_db_node>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                           THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                           ELSE /hec1/if_config_constants=>gc_image_status-complete )
                              text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-db_node
                                                                               para1 = COND #( WHEN <fs_db_node>-hec_tree_descr IS NOT INITIAL
                                                                                                AND <fs_db_node>-hec_tree_descr NA |:|
                                                                                               THEN |: { <fs_db_node>-hec_tree_descr }|
                                                                                               ELSE <fs_db_node>-hec_tree_descr ) )
                              hec_delete_visible = COND #( WHEN <fs_db_node>-hec_master_default = abap_true
                                                           THEN abap_false
                                                           ELSE abap_true )
                              hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-db_node
                              ) TO rt_distribut_tree.

              " DB Server Performance Category
              LOOP AT lt_db_server_pc ASSIGNING FIELD-SYMBOL(<fs_db_server_pc>)
                WHERE hec_node_solution     = <fs_db_node>-hec_node_solution
                  AND hec_node_tier         = <fs_db_node>-hec_node_tier
                  AND hec_node_db_serv_inst = <fs_db_node>-hec_node_db_serv_inst
                  AND hec_node_db_inst      = <fs_db_node>-hec_node_db_inst
                  AND hec_node_db_node      = <fs_db_node>-hec_node_db_node.

                GET TIME STAMP FIELD lv_timestamp.
                DATA(lv_db_server_pc_row_key) = |{ lv_timestamp }|.

                APPEND VALUE #( BASE CORRESPONDING #( <fs_db_server_pc> )
                                parent_key         = lv_db_node_row_key
                                row_key            = lv_db_server_pc_row_key
                                expanded           = abap_true
                                is_leaf            = abap_true
                                image_src          = COND #( WHEN <fs_db_server_pc>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                             THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                             ELSE /hec1/if_config_constants=>gc_image_status-complete )
                                text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-db_serv_pc
                                                                                 para1 = COND #( WHEN <fs_db_server_pc>-hec_tree_descr IS NOT INITIAL
                                                                                                  AND <fs_db_server_pc>-hec_tree_descr NA |:|
                                                                                                 THEN |: { <fs_db_server_pc>-hec_tree_descr }|
                                                                                                 ELSE <fs_db_server_pc>-hec_tree_descr ) )
                                hec_delete_visible = abap_true
                                hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-db_serv_pc
                                ) TO rt_distribut_tree.

                " DB Storage Quantity
                LOOP AT lt_db_storage_qty ASSIGNING FIELD-SYMBOL(<fs_db_storage_qty>)
                  WHERE hec_node_solution     = <fs_db_server_pc>-hec_node_solution
                    AND hec_node_tier         = <fs_db_server_pc>-hec_node_tier
                    AND hec_node_db_serv_inst = <fs_db_server_pc>-hec_node_db_serv_inst
                    AND hec_node_db_inst      = <fs_db_server_pc>-hec_node_db_inst
                    AND hec_node_db_node      = <fs_db_server_pc>-hec_node_db_node
                    AND hec_node_db_serv_pc   = <fs_db_server_pc>-hec_node_db_serv_pc.

                  GET TIME STAMP FIELD lv_timestamp.
                  DATA(lv_db_storage_qty_row_key) = |{ lv_timestamp }|.

                  APPEND VALUE #( BASE CORRESPONDING #( <fs_db_storage_qty> )
                                  parent_key         = lv_db_server_pc_row_key
                                  row_key            = lv_db_storage_qty_row_key
                                  expanded           = abap_true
                                  is_leaf            = abap_true
                                  image_src          = COND #( WHEN <fs_db_storage_qty>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                               THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                               ELSE /hec1/if_config_constants=>gc_image_status-complete )
                                  text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-db_storage_qty
                                                                                   para1 = COND #( WHEN <fs_db_storage_qty>-hec_tree_descr IS NOT INITIAL
                                                                                                    AND <fs_db_storage_qty>-hec_tree_descr NA |:|
                                                                                                   THEN |: { <fs_db_storage_qty>-hec_tree_descr }|
                                                                                                   ELSE <fs_db_storage_qty>-hec_tree_descr ) )
                                  hec_delete_visible = abap_true
                                  hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-db_storage_qty
                                  ) TO rt_distribut_tree.

                ENDLOOP. "db_storage_qty

                " DB Server
                LOOP AT lt_db_server ASSIGNING FIELD-SYMBOL(<fs_db_server>)
                  WHERE hec_node_solution     = <fs_db_server_pc>-hec_node_solution
                    AND hec_node_tier         = <fs_db_server_pc>-hec_node_tier
                    AND hec_node_db_serv_inst = <fs_db_server_pc>-hec_node_db_serv_inst
                    AND hec_node_db_inst      = <fs_db_server_pc>-hec_node_db_inst
                    AND hec_node_db_node      = <fs_db_server_pc>-hec_node_db_node
                    AND hec_node_db_serv_pc   = <fs_db_server_pc>-hec_node_db_serv_pc.

                  GET TIME STAMP FIELD lv_timestamp.
                  DATA(lv_db_server_row_key) = |{ lv_timestamp }|.

                  APPEND VALUE #( BASE CORRESPONDING #( <fs_db_server> )
                                  parent_key         = lv_db_server_pc_row_key
                                  row_key            = lv_db_server_row_key
                                  expanded           = abap_true
                                  is_leaf            = abap_true
                                  image_src          = COND #( WHEN <fs_db_server>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                               THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                               ELSE /hec1/if_config_constants=>gc_image_status-complete )
                                  text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-db_server
                                                                                   para1 = COND #( WHEN <fs_db_server>-hec_tree_descr IS NOT INITIAL
                                                                                                    AND <fs_db_server>-hec_tree_descr NA |:|
                                                                                                   THEN |: { <fs_db_server>-hec_tree_descr }|
                                                                                                   ELSE <fs_db_server>-hec_tree_descr ) )
                                  hec_delete_visible = abap_false
                                  hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-db_server
                                  ) TO rt_distribut_tree.

                  " DB storage
                  LOOP AT lt_db_storage ASSIGNING FIELD-SYMBOL(<fs_db_storage>)
                    WHERE hec_node_solution     = <fs_db_server>-hec_node_solution
                      AND hec_node_tier         = <fs_db_server>-hec_node_tier
                      AND hec_node_db_serv_inst = <fs_db_server>-hec_node_db_serv_inst
                      AND hec_node_db_inst      = <fs_db_server>-hec_node_db_inst
                      AND hec_node_db_serv_pc   = <fs_db_server>-hec_node_db_serv_pc
                      AND hec_node_db_server    = <fs_db_server>-hec_node_db_server.

                    GET TIME STAMP FIELD lv_timestamp.
                    DATA(lv_db_storage_row_key) = |{ lv_timestamp }|.

                    APPEND VALUE #( BASE CORRESPONDING #( <fs_db_storage> )
                                    parent_key         = lv_db_server_row_key
                                    row_key            = lv_db_storage_row_key
                                    expanded           = abap_true
                                    is_leaf            = abap_true
                                    image_src          = COND #( WHEN <fs_db_storage>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                                 THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                                 ELSE /hec1/if_config_constants=>gc_image_status-complete )
                                    text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-db_storage
                                                                                     para1 = COND #( WHEN <fs_db_storage>-hec_tree_descr IS NOT INITIAL
                                                                                                      AND <fs_db_storage>-hec_tree_descr NA |:|
                                                                                                     THEN |: { <fs_db_storage>-hec_tree_descr }|
                                                                                                     ELSE <fs_db_storage>-hec_tree_descr ) )
                                    hec_delete_visible = abap_false
                                    hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-db_storage
                                    ) TO rt_distribut_tree.

                    " DB backup
                    LOOP AT lt_db_backup ASSIGNING FIELD-SYMBOL(<fs_db_backup>)
                      WHERE hec_node_solution     = <fs_db_storage>-hec_node_solution
                        AND hec_node_tier         = <fs_db_storage>-hec_node_tier
                        AND hec_node_db_serv_inst = <fs_db_storage>-hec_node_db_serv_inst
                        AND hec_node_db_inst      = <fs_db_storage>-hec_node_db_inst
                        AND hec_node_db_serv_pc   = <fs_db_storage>-hec_node_db_serv_pc
                        AND hec_node_db_server    = <fs_db_storage>-hec_node_db_server
                        AND hec_node_db_storage   = <fs_db_storage>-hec_node_db_storage.

                      GET TIME STAMP FIELD lv_timestamp.
                      DATA(lv_db_backup_row_key) = |{ lv_timestamp }|.

                      APPEND VALUE #( BASE CORRESPONDING #( <fs_db_backup> )
                                      parent_key         = lv_db_storage_row_key
                                      row_key            = lv_db_backup_row_key
                                      expanded           = abap_true
                                      is_leaf            = abap_true
                                      image_src          = COND #( WHEN <fs_db_backup>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                                   THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                                   ELSE /hec1/if_config_constants=>gc_image_status-complete )
                                      text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-db_backup
                                                                                       para1 = COND #( WHEN <fs_db_backup>-hec_tree_descr IS NOT INITIAL
                                                                                                        AND <fs_db_backup>-hec_tree_descr NA |:|
                                                                                                       THEN |: { <fs_db_backup>-hec_tree_descr }|
                                                                                                       ELSE <fs_db_backup>-hec_tree_descr ) )
                                      hec_delete_visible = abap_true
                                      hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-db_backup
                                      ) TO rt_distribut_tree.

                    ENDLOOP. "db_backup
                  ENDLOOP. "db_storage
                ENDLOOP. "db_server
              ENDLOOP. "db_server_pc
            ENDLOOP. "db_node
          ENDLOOP. "instance_db
        ENDLOOP. "db_server_inst

        " App  Server Instance
        LOOP AT lt_app_server_inst ASSIGNING FIELD-SYMBOL(<fs_app_server_inst>)
          WHERE hec_node_solution = <fs_tier>-hec_node_solution
            AND hec_node_tier     = <fs_tier>-hec_node_tier.

          GET TIME STAMP FIELD lv_timestamp.
          DATA(lv_app_server_inst_row_key) = |{ lv_timestamp }|.

          APPEND VALUE #( BASE CORRESPONDING #( <fs_app_server_inst> )
                          parent_key         = lv_tier_row_key
                          row_key            = lv_app_server_inst_row_key
                          expanded           = abap_true
                          is_leaf            = abap_true
                          image_src          = COND #( WHEN <fs_app_server_inst>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                       THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                       ELSE /hec1/if_config_constants=>gc_image_status-complete )
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-app_serv_inst
                                                                           para1 = COND #( WHEN <fs_app_server_inst>-hec_tree_descr IS NOT INITIAL
                                                                                            AND <fs_app_server_inst>-hec_tree_descr NA |:|
                                                                                           THEN |: { <fs_app_server_inst>-hec_tree_descr }|
                                                                                           ELSE <fs_app_server_inst>-hec_tree_descr ) )
                          hec_delete_visible = abap_false
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-app_serv_inst
                          ) TO rt_distribut_tree.

          " App Node
          SORT lt_app_node ASCENDING BY hec_app_clust_node_type_value.

          LOOP AT lt_app_node ASSIGNING FIELD-SYMBOL(<fs_app_node>)
            WHERE hec_node_solution      = <fs_app_server_inst>-hec_node_solution
              AND hec_node_tier          = <fs_app_server_inst>-hec_node_tier
              AND hec_node_app_serv_inst = <fs_app_server_inst>-hec_node_app_serv_inst.

            GET TIME STAMP FIELD lv_timestamp.
            DATA(lv_app_node_row_key) = |{ lv_timestamp }|.

            APPEND VALUE #( BASE CORRESPONDING #( <fs_app_node> )
                            parent_key         = lv_app_server_inst_row_key
                            row_key            = lv_app_node_row_key
                            expanded           = abap_true
                            is_leaf            = abap_true
                            image_src          = COND #( WHEN <fs_app_node>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                         THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                         ELSE /hec1/if_config_constants=>gc_image_status-complete )
                            text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-app_node
                                                                             para1 = COND #( WHEN <fs_app_node>-hec_tree_descr IS NOT INITIAL
                                                                                              AND <fs_app_node>-hec_tree_descr NA |:|
                                                                                             THEN |: { <fs_app_node>-hec_tree_descr }|
                                                                                             ELSE <fs_app_node>-hec_tree_descr ) )
                            hec_delete_visible = abap_false
                            hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-app_node
                            ) TO rt_distribut_tree.

            " App Server Performance Category
            LOOP AT lt_app_server_pc ASSIGNING FIELD-SYMBOL(<fs_app_server_pc>)
              WHERE hec_node_solution      = <fs_app_node>-hec_node_solution
                AND hec_node_tier          = <fs_app_node>-hec_node_tier
                AND hec_node_app_serv_inst = <fs_app_node>-hec_node_app_serv_inst
                AND hec_node_app_node      = <fs_app_node>-hec_node_app_node.

              GET TIME STAMP FIELD lv_timestamp.
              DATA(lv_app_server_pc_row_key) = |{ lv_timestamp }|.

              APPEND VALUE #( BASE CORRESPONDING #( <fs_app_server_pc> )
                              parent_key         = lv_app_node_row_key
                              row_key            = lv_app_server_pc_row_key
                              expanded           = abap_true
                              is_leaf            = abap_true
                              image_src          = COND #( WHEN <fs_app_server_pc>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                           THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                           ELSE /hec1/if_config_constants=>gc_image_status-complete )
                              text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-app_serv_pc
                                                                               para1 = COND #( WHEN <fs_app_server_pc>-hec_tree_descr IS NOT INITIAL
                                                                                                AND <fs_app_server_pc>-hec_tree_descr NA |:|
                                                                                               THEN |: { <fs_app_server_pc>-hec_tree_descr }|
                                                                                               ELSE <fs_app_server_pc>-hec_tree_descr ) )
                              hec_delete_visible = abap_true
                              hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-app_serv_pc
                              ) TO rt_distribut_tree.

              " App Storage Quantity
              LOOP AT lt_app_storage_qty ASSIGNING FIELD-SYMBOL(<fs_app_storage_qty>)
                WHERE hec_node_solution      = <fs_app_server_pc>-hec_node_solution
                  AND hec_node_tier          = <fs_app_server_pc>-hec_node_tier
                  AND hec_node_app_serv_inst = <fs_app_server_pc>-hec_node_app_serv_inst
                  AND hec_node_app_node      = <fs_app_server_pc>-hec_node_app_node
                  AND hec_node_app_serv_pc   = <fs_app_server_pc>-hec_node_app_serv_pc.

                GET TIME STAMP FIELD lv_timestamp.
                DATA(lv_app_storage_qty_row_key) = |{ lv_timestamp }|.

                APPEND VALUE #( BASE CORRESPONDING #( <fs_app_storage_qty> )
                                parent_key         = lv_app_server_pc_row_key
                                row_key            = lv_app_storage_qty_row_key
                                expanded           = abap_true
                                is_leaf            = abap_true
                                image_src          = COND #( WHEN <fs_app_storage_qty>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                             THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                             ELSE /hec1/if_config_constants=>gc_image_status-complete )
                                text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-app_storage_qty
                                                                                 para1 = COND #( WHEN <fs_app_storage_qty>-hec_tree_descr IS NOT INITIAL
                                                                                                  AND <fs_app_storage_qty>-hec_tree_descr NA |:|
                                                                                                 THEN |: { <fs_app_storage_qty>-hec_tree_descr }|
                                                                                                 ELSE <fs_app_storage_qty>-hec_tree_descr ) )
                                hec_delete_visible = abap_true
                                hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-app_storage_qty
                                ) TO rt_distribut_tree.

              ENDLOOP. "db_storage_qty

              " App Server
              LOOP AT lt_app_server ASSIGNING FIELD-SYMBOL(<fs_app_server>)
                WHERE hec_node_solution      = <fs_app_server_pc>-hec_node_solution
                  AND hec_node_tier          = <fs_app_server_pc>-hec_node_tier
                  AND hec_node_app_serv_inst = <fs_app_server_pc>-hec_node_app_serv_inst
                  AND hec_node_app_node      = <fs_app_server_pc>-hec_node_app_node
                  AND hec_node_app_serv_pc   = <fs_app_server_pc>-hec_node_app_serv_pc.

                GET TIME STAMP FIELD lv_timestamp.
                DATA(lv_app_server_row_key) = |{ lv_timestamp }|.

                APPEND VALUE #( BASE CORRESPONDING #( <fs_app_server> )
                                parent_key         = lv_app_server_pc_row_key
                                row_key            = lv_app_server_row_key
                                expanded           = abap_true
                                is_leaf            = abap_true
                                image_src          = COND #( WHEN <fs_app_server>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                             THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                             ELSE /hec1/if_config_constants=>gc_image_status-complete )
                                text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-app_server
                                                                                 para1 = COND #( WHEN <fs_app_server>-hec_tree_descr IS NOT INITIAL
                                                                                                  AND <fs_app_server>-hec_tree_descr NA |:|
                                                                                                 THEN |: { <fs_app_server>-hec_tree_descr }|
                                                                                                 ELSE <fs_app_server>-hec_tree_descr ) )
                                hec_delete_visible = abap_false
                                hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-app_server
                                ) TO rt_distribut_tree.

                " App storage
                LOOP AT lt_app_storage ASSIGNING FIELD-SYMBOL(<fs_app_storage>)
                  WHERE hec_node_solution      = <fs_app_server>-hec_node_solution
                    AND hec_node_tier          = <fs_app_server>-hec_node_tier
                    AND hec_node_app_serv_inst = <fs_app_server>-hec_node_app_serv_inst
                    AND hec_node_app_serv_pc   = <fs_app_server>-hec_node_app_serv_pc
                    AND hec_node_app_server    = <fs_app_server>-hec_node_app_server.

                  GET TIME STAMP FIELD lv_timestamp.
                  DATA(lv_app_storage_row_key) = |{ lv_timestamp }|.

                  APPEND VALUE #( BASE CORRESPONDING #( <fs_app_storage> )
                                  parent_key         = lv_app_server_row_key
                                  row_key            = lv_app_storage_row_key
                                  expanded           = abap_true
                                  is_leaf            = abap_true
                                  image_src          = COND #( WHEN <fs_app_storage>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                               THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                               ELSE /hec1/if_config_constants=>gc_image_status-complete )
                                  text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-app_storage
                                                                                   para1 = COND #( WHEN <fs_app_storage>-hec_tree_descr IS NOT INITIAL
                                                                                                    AND <fs_app_storage>-hec_tree_descr NA |:|
                                                                                                   THEN |: { <fs_app_storage>-hec_tree_descr }|
                                                                                                   ELSE <fs_app_storage>-hec_tree_descr ) )
                                  hec_delete_visible = abap_false
                                  hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-app_storage
                                  ) TO rt_distribut_tree.

                  " App backup
                  LOOP AT lt_app_backup ASSIGNING FIELD-SYMBOL(<fs_app_backup>)
                    WHERE hec_node_solution      = <fs_app_storage>-hec_node_solution
                      AND hec_node_tier          = <fs_app_storage>-hec_node_tier
                      AND hec_node_app_serv_inst = <fs_app_storage>-hec_node_app_serv_inst
                      AND hec_node_app_serv_pc   = <fs_app_storage>-hec_node_app_serv_pc
                      AND hec_node_app_server    = <fs_app_storage>-hec_node_app_server
                      AND hec_node_app_storage   = <fs_app_storage>-hec_node_app_storage.

                    GET TIME STAMP FIELD lv_timestamp.
                    DATA(lv_app_backup_row_key) = |{ lv_timestamp }|.

                    APPEND VALUE #( BASE CORRESPONDING #( <fs_app_backup> )
                                    parent_key         = lv_app_storage_row_key
                                    row_key            = lv_app_backup_row_key
                                    expanded           = abap_true
                                    is_leaf            = abap_true
                                    image_src          = COND #( WHEN <fs_app_backup>-hec_instance_status = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                                 THEN /hec1/if_config_constants=>gc_image_status-incomplete
                                                                 ELSE /hec1/if_config_constants=>gc_image_status-complete )
                                    text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-app_backup
                                                                                     para1 = COND #( WHEN <fs_app_backup>-hec_tree_descr IS NOT INITIAL
                                                                                                      AND <fs_app_backup>-hec_tree_descr NA |:|
                                                                                                     THEN |: { <fs_app_backup>-hec_tree_descr }|
                                                                                                     ELSE <fs_app_backup>-hec_tree_descr ) )
                                    hec_delete_visible = abap_true
                                    hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-app_backup
                                    ) TO rt_distribut_tree.

                  ENDLOOP. "app_backup
                ENDLOOP. "app_storage
              ENDLOOP. "app_server
            ENDLOOP. "app_server_pc
          ENDLOOP. "app_node
        ENDLOOP. "app_server_inst

      ENDLOOP. " LOOP AT lt_tier
    ENDLOOP. " LOOP AT lt_solution

    " turn last entry in a branch into a leaf
    LOOP AT rt_distribut_tree INTO DATA(ls_distribut_tree) FROM 2.
      ASSIGN rt_distribut_tree[ row_key = ls_distribut_tree-parent_key ] TO FIELD-SYMBOL(<fs_tree>).
      <fs_tree>-is_leaf = abap_false.
    ENDLOOP.

    SORT rt_distribut_tree ASCENDING.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_add_service.

    DATA lt_data TYPE /hec1/t_data_add_services_ct.

    CLEAR: eo_message,
           rt_service.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-add_service
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-add_service-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_service = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_add_storage_dc.

    DATA lt_data TYPE /hec1/t_add_storage_dc_ct.

    CLEAR: eo_message,
           rt_add_storage_dc.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-add_storage_datacenter
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-add_storage_datacenter-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_add_storage_dc = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_add_storage_cl.

    DATA lt_data TYPE /hec1/t_add_storage_class_ct.

    CLEAR: eo_message,
           rt_add_storage_cl.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-add_storage_class
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-add_storage_class-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_add_storage_cl = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_add_storage_am.

    DATA lt_data TYPE /hec1/t_add_storage_amount_ct.

    CLEAR: eo_message,
           rt_add_storage_am.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-add_storage_amount
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-add_storage_amount-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_add_storage_am = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_app_node.

    DATA lt_data TYPE /hec1/t_data_app_node_ct.

    CLEAR: eo_message,
           rt_app_node.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-app_node
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-app_node-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_app_node = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_app_server.

    DATA lt_data TYPE /hec1/t_data_app_serv_ct.

    CLEAR: eo_message,
           rt_app_server.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-app_server
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-app_server-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_app_server = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_app_server_inst.

    DATA lt_data TYPE /hec1/t_data_app_serv_inst_ct.

    CLEAR: eo_message,
           rt_app_serv_inst.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-app_server_instance-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_app_serv_inst = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_app_server_pc.

    DATA lt_data TYPE /hec1/t_data_app_serv_pc_ct.

    CLEAR: eo_message,
           rt_app_serv_pc.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-app_server_perform_cat-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_app_serv_pc = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_app_storage.

    DATA lt_data TYPE /hec1/t_data_app_storage_ct.

    CLEAR: eo_message,
           rt_app_storage.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-app_storage
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-app_storage-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_app_storage = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_app_storage_backup.

    DATA lt_data TYPE /hec1/t_data_app_backup_ct.

    CLEAR: eo_message,
           rt_app_backup.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-app_storage_backup
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-app_storage_backup-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_app_backup = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_app_storage_qty.

    DATA lt_data TYPE /hec1/t_data_app_storageqty_ct.

    CLEAR: eo_message,
           rt_app_storage_qty.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-app_storage_amount
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-app_storage_amount-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_app_storage_qty = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_connectivity.

    DATA lt_data TYPE /hec1/t_data_connectivity_ct.

    CLEAR: eo_message,
           rt_connectivity.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-connectivity
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-connectivity-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_connectivity = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_connect_price_aggre.

    DATA lt_data TYPE /hec1/t_service_price_aggre_ct.

    CLEAR: eo_message,
           rt_connect_price_aggre.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-connectivity_price_phase
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-connectivity_price_phase-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_connect_price_aggre = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_datacenter.

    DATA: lt_sel_param TYPE /bobf/t_frw_query_selparam,
          lt_data      TYPE /hec1/t_data_datacenter_ct.

    CLEAR: eo_message,
           rt_datacenter.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-datacenter
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-datacenter-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_datacenter = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_datacenter_ct.

    TRY.
        rt_data = me->mo_data_provider->get_datacenters_ct( ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_db_node.

    DATA lt_data TYPE /hec1/t_data_db_node_ct.

    CLEAR: eo_message,
           rt_db_node.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-db_node
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-db_node-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_db_node = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_db_server.

    DATA lt_data TYPE /hec1/t_data_db_serv_ct.

    CLEAR: eo_message,
           rt_db_server.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-db_server
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-db_server-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_db_server = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_db_server_inst.

    DATA lt_data TYPE /hec1/t_data_db_server_inst_ct.

    CLEAR: eo_message,
           rt_db_serv_inst.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-db_server_instance-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_db_serv_inst = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_db_server_inst_multi.

    DATA: ls_key          TYPE /hec1/s_key_tier,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_solution IS INITIAL AND
           iv_guid_tier     IS INITIAL.

          "get ALL for complete Config
*          rt_db_serv_inst = me->mo_data_provider->get_db_server_insts_by_config( is_config_key = me->ms_root_key ).
          rt_db_serv_inst = me->mo_data_provider->get_db_server_insts_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution = iv_guid_solution.
          ls_key-hec_node_tier     = iv_guid_tier.

          "determine source key structure
          IF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_db_server_inst_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_db_serv_inst = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_db_server_inst_single.

    TRY .
        rs_db_serv_inst = CORRESPONDING #( me->mo_data_provider->get_db_server_inst( is_key = VALUE #( hec_node_solution     = iv_guid_solution
                                                                                      hec_node_tier         = iv_guid_tier
                                                                                      hec_node_db_serv_inst = iv_guid_db_serv_inst ) ) ) .

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_db_server_multi.

    DATA: ls_key          TYPE /hec1/s_key_db_serv_pc,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_solution     IS INITIAL AND
           iv_guid_tier         IS INITIAL AND
           iv_guid_db_serv_inst IS INITIAL AND
           iv_guid_db_inst      IS INITIAL AND
           iv_guid_db_node      IS INITIAL AND
           iv_guid_db_serv_pc   IS INITIAL.

          "get ALL for complete Config
*          rt_db_server = me->mo_data_provider->get_db_servers_by_config( is_config_key = me->ms_root_key ).
          rt_db_server = me->mo_data_provider->get_db_servers_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution     = iv_guid_solution.
          ls_key-hec_node_tier         = iv_guid_tier.
          ls_key-hec_node_db_serv_inst = iv_guid_db_serv_inst.
          ls_key-hec_node_db_inst      = iv_guid_db_inst.
          ls_key-hec_node_db_node      = iv_guid_db_node.
          ls_key-hec_node_db_serv_pc   = iv_guid_db_serv_pc.

          "determine source key structure
          IF iv_guid_db_serv_pc IS NOT INITIAL.
            IF iv_guid_db_node      IS INITIAL OR
               iv_guid_db_inst      IS INITIAL OR
               iv_guid_db_serv_inst IS INITIAL OR
               iv_guid_tier         IS INITIAL OR
               iv_guid_solution     IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_srv_pc.
            ENDIF.
          ELSEIF iv_guid_db_node IS NOT INITIAL.
            IF iv_guid_db_inst      IS INITIAL OR
               iv_guid_db_serv_inst IS INITIAL OR
               iv_guid_tier         IS INITIAL OR
               iv_guid_solution     IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_node.
            ENDIF.
          ELSEIF iv_guid_db_inst IS NOT INITIAL.
            IF iv_guid_db_serv_inst IS INITIAL OR
               iv_guid_tier         IS INITIAL OR
               iv_guid_solution     IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_inst.
            ENDIF.
          ELSEIF iv_guid_db_serv_inst IS NOT INITIAL.
            IF iv_guid_tier     IS INITIAL OR
               iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_srv_inst.
            ENDIF.
          ELSEIF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_db_serv_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_db_server = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_db_server_pc_multi.

    DATA: ls_key          TYPE /hec1/s_key_db_node,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_solution     IS INITIAL AND
           iv_guid_tier         IS INITIAL AND
           iv_guid_db_serv_inst IS INITIAL AND
           iv_guid_db_inst      IS INITIAL AND
           iv_guid_db_node      IS INITIAL.

          "get ALL for complete Config
*          rt_db_serv_pc = me->mo_data_provider->get_db_server_pcats_by_config( is_config_key = me->ms_root_key ).
          rt_db_serv_pc = me->mo_data_provider->get_db_server_pcats_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution     = iv_guid_solution.
          ls_key-hec_node_tier         = iv_guid_tier.
          ls_key-hec_node_db_serv_inst = iv_guid_db_serv_inst.
          ls_key-hec_node_db_inst      = iv_guid_db_inst.
          ls_key-hec_node_db_node      = iv_guid_db_node.

          "determine source key structure
          IF iv_guid_db_node IS NOT INITIAL.
            IF iv_guid_db_inst      IS INITIAL OR
               iv_guid_db_serv_inst IS INITIAL OR
               iv_guid_tier         IS INITIAL OR
               iv_guid_solution     IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_node.
            ENDIF.
          ELSEIF iv_guid_db_inst IS NOT INITIAL.
            IF iv_guid_db_serv_inst IS INITIAL OR
               iv_guid_tier         IS INITIAL OR
               iv_guid_solution     IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_inst.
            ENDIF.
          ELSEIF iv_guid_db_serv_inst IS NOT INITIAL.
            IF iv_guid_tier     IS INITIAL OR
               iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_srv_inst.
            ENDIF.
          ELSEIF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_db_serv_pc_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_db_serv_pc = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_db_server_pc_single.

    TRY .
        rs_db_serv_pc = CORRESPONDING #( me->mo_data_provider->get_db_server_pcat( is_key = VALUE #( hec_node_solution     = iv_guid_solution
                                                                                    hec_node_tier         = iv_guid_tier
                                                                                    hec_node_db_serv_inst = iv_guid_db_serv_inst
                                                                                    hec_node_db_inst      = iv_guid_db_inst
                                                                                    hec_node_db_node      = iv_guid_db_node
                                                                                    hec_node_db_serv_pc   = iv_guid_db_serv_pc   ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_db_server_single.

    TRY .
        rs_db_server = CORRESPONDING #( me->mo_data_provider->get_db_server( is_key = VALUE #( hec_node_solution     = iv_guid_solution
                                                                              hec_node_tier         = iv_guid_tier
                                                                              hec_node_db_serv_inst = iv_guid_db_serv_inst
                                                                              hec_node_db_inst      = iv_guid_db_inst
                                                                              hec_node_db_node      = iv_guid_db_node
                                                                              hec_node_db_serv_pc   = iv_guid_db_serv_pc
                                                                              hec_node_db_server    = iv_guid_db_server   ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_db_storage_backup_multi.

    DATA: ls_key          TYPE /hec1/s_key_db_storage,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_solution     IS INITIAL AND
           iv_guid_tier         IS INITIAL AND
           iv_guid_db_serv_inst IS INITIAL AND
           iv_guid_db_inst      IS INITIAL AND
           iv_guid_db_node      IS INITIAL AND
           iv_guid_db_serv_pc   IS INITIAL AND
           iv_guid_db_server    IS INITIAL AND
           iv_guid_db_storage   IS INITIAL.

          "get ALL for complete Config
*          rt_db_storage = me->mo_data_provider->get_db_storages_by_config( is_config_key = me->ms_root_key ).
          rt_storage_backup = me->mo_data_provider->get_db_backups_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution     = iv_guid_solution.
          ls_key-hec_node_tier         = iv_guid_tier.
          ls_key-hec_node_db_serv_inst = iv_guid_db_serv_inst.
          ls_key-hec_node_db_inst      = iv_guid_db_inst.
          ls_key-hec_node_db_node      = iv_guid_db_node.
          ls_key-hec_node_db_serv_pc   = iv_guid_db_serv_pc.
          ls_key-hec_node_db_server    = iv_guid_db_server.
          ls_key-hec_node_db_storage   = iv_guid_db_storage.

          "determine source key structure
          IF iv_guid_db_storage IS NOT INITIAL.
            IF iv_guid_db_server    IS INITIAL OR
               iv_guid_db_serv_pc   IS INITIAL OR
               iv_guid_db_node      IS INITIAL OR
               iv_guid_db_inst      IS INITIAL OR
               iv_guid_db_serv_inst IS INITIAL OR
               iv_guid_tier         IS INITIAL OR
               iv_guid_solution     IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_storage.
            ENDIF.
          ELSEIF iv_guid_db_server IS NOT INITIAL.
            IF iv_guid_db_serv_pc   IS INITIAL OR
               iv_guid_db_node      IS INITIAL OR
               iv_guid_db_inst      IS INITIAL OR
               iv_guid_db_serv_inst IS INITIAL OR
               iv_guid_tier         IS INITIAL OR
               iv_guid_solution     IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_srv.
            ENDIF.
          ELSEIF iv_guid_db_serv_pc IS NOT INITIAL.
            IF iv_guid_db_node      IS INITIAL OR
               iv_guid_db_inst      IS INITIAL OR
               iv_guid_db_serv_inst IS INITIAL OR
               iv_guid_tier         IS INITIAL OR
               iv_guid_solution     IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_srv_pc.
            ENDIF.
          ELSEIF iv_guid_db_node IS NOT INITIAL.
            IF iv_guid_db_inst      IS INITIAL OR
               iv_guid_db_serv_inst IS INITIAL OR
               iv_guid_tier         IS INITIAL OR
               iv_guid_solution     IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_node.
            ENDIF.
          ELSEIF iv_guid_db_inst IS NOT INITIAL.
            IF iv_guid_db_serv_inst IS INITIAL OR
               iv_guid_tier         IS INITIAL OR
               iv_guid_solution     IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_inst.
            ENDIF.
          ELSEIF iv_guid_db_serv_inst IS NOT INITIAL.
            IF iv_guid_tier     IS INITIAL OR
               iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_srv_inst.
            ENDIF.
          ELSEIF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_db_backup_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_storage_backup = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_db_storage_backup_single.

    TRY .
        rs_storage_backup = CORRESPONDING #( me->mo_data_provider->get_db_backup( is_key = VALUE #( hec_node_solution       = iv_guid_solution
                                                                                   hec_node_tier           = iv_guid_tier
                                                                                   hec_node_db_serv_inst   = iv_guid_db_serv_inst
                                                                                   hec_node_db_inst        = iv_guid_db_inst
                                                                                   hec_node_db_node        = iv_guid_db_node
                                                                                   hec_node_db_serv_pc     = iv_guid_db_serv_pc
                                                                                   hec_node_db_server      = iv_guid_db_server
                                                                                   hec_node_db_storage     = iv_guid_db_storage
                                                                                   hec_node_db_backup      = iv_guid_db_backup    ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_db_storage_multi.

    DATA: ls_key          TYPE /hec1/s_key_db_serv,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_solution     IS INITIAL AND
           iv_guid_tier         IS INITIAL AND
           iv_guid_db_serv_inst IS INITIAL AND
           iv_guid_db_inst      IS INITIAL AND
           iv_guid_db_node      IS INITIAL AND
           iv_guid_db_serv_pc   IS INITIAL AND
           iv_guid_db_server    IS INITIAL.

          "get ALL for complete Config
*          rt_db_storage = me->mo_data_provider->get_db_storages_by_config( is_config_key = me->ms_root_key ).
          rt_db_storage = me->mo_data_provider->get_db_storages_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution     = iv_guid_solution.
          ls_key-hec_node_tier         = iv_guid_tier.
          ls_key-hec_node_db_serv_inst = iv_guid_db_serv_inst.
          ls_key-hec_node_db_inst      = iv_guid_db_inst.
          ls_key-hec_node_db_node      = iv_guid_db_node.
          ls_key-hec_node_db_serv_pc   = iv_guid_db_serv_pc.
          ls_key-hec_node_db_server    = iv_guid_db_server.

          "determine source key structure
          IF iv_guid_db_server IS NOT INITIAL.
            IF iv_guid_db_serv_pc   IS INITIAL OR
               iv_guid_db_node      IS INITIAL OR
               iv_guid_db_inst      IS INITIAL OR
               iv_guid_db_serv_inst IS INITIAL OR
               iv_guid_tier         IS INITIAL OR
               iv_guid_solution     IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_srv.
            ENDIF.
          ELSEIF iv_guid_db_serv_pc IS NOT INITIAL.
            IF iv_guid_db_node      IS INITIAL OR
               iv_guid_db_inst      IS INITIAL OR
               iv_guid_db_serv_inst IS INITIAL OR
               iv_guid_tier         IS INITIAL OR
               iv_guid_solution     IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_srv_pc.
            ENDIF.
          ELSEIF iv_guid_db_node IS NOT INITIAL.
            IF iv_guid_db_inst      IS INITIAL OR
               iv_guid_db_serv_inst IS INITIAL OR
               iv_guid_tier         IS INITIAL OR
               iv_guid_solution     IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_node.
            ENDIF.
          ELSEIF iv_guid_db_inst IS NOT INITIAL.
            IF iv_guid_db_serv_inst IS INITIAL OR
               iv_guid_tier         IS INITIAL OR
               iv_guid_solution     IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_inst.
            ENDIF.
          ELSEIF iv_guid_db_serv_inst IS NOT INITIAL.
            IF iv_guid_tier     IS INITIAL OR
               iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_srv_inst.
            ENDIF.
          ELSEIF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_db_storage_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_db_storage = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_db_storage_qty_multi.

    DATA: ls_key          TYPE /hec1/s_key_db_serv_pc,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_solution     IS INITIAL AND
           iv_guid_tier         IS INITIAL AND
           iv_guid_db_serv_inst IS INITIAL AND
           iv_guid_db_inst      IS INITIAL AND
           iv_guid_db_node      IS INITIAL AND
           iv_guid_db_serv_pc   IS INITIAL.

          "get ALL for complete Config
*          rt_db_storage_qty = me->mo_data_provider->get_db_storage_amnts_by_config( is_config_key = me->ms_root_key ).
          rt_db_storage_qty = me->mo_data_provider->get_db_storage_amnts_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution     = iv_guid_solution.
          ls_key-hec_node_tier         = iv_guid_tier.
          ls_key-hec_node_db_serv_inst = iv_guid_db_serv_inst.
          ls_key-hec_node_db_inst      = iv_guid_db_inst.
          ls_key-hec_node_db_node      = iv_guid_db_node.
          ls_key-hec_node_db_serv_pc   = iv_guid_db_serv_pc.

          "determine source key structure
          IF iv_guid_db_serv_pc IS NOT INITIAL.
            IF iv_guid_db_node      IS INITIAL OR
               iv_guid_db_inst      IS INITIAL OR
               iv_guid_db_serv_inst IS INITIAL OR
               iv_guid_tier         IS INITIAL OR
               iv_guid_solution     IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_srv_pc.
            ENDIF.
          ELSEIF iv_guid_db_node IS NOT INITIAL.
            IF iv_guid_db_inst      IS INITIAL OR
               iv_guid_db_serv_inst IS INITIAL OR
               iv_guid_tier         IS INITIAL OR
               iv_guid_solution     IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_node.
            ENDIF.
          ELSEIF iv_guid_db_inst IS NOT INITIAL.
            IF iv_guid_db_serv_inst IS INITIAL OR
               iv_guid_tier         IS INITIAL OR
               iv_guid_solution     IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_inst.
            ENDIF.
          ELSEIF iv_guid_db_serv_inst IS NOT INITIAL.
            IF iv_guid_tier     IS INITIAL OR
               iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_srv_inst.
            ENDIF.
          ELSEIF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_db_storage_qty_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_db_storage_qty = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_db_storage_qty_single.

    TRY .
        rs_db_storage_qty = CORRESPONDING #( me->mo_data_provider->get_db_storage_amnt( is_key = VALUE #( hec_node_solution       = iv_guid_solution
                                                                                         hec_node_tier           = iv_guid_tier
                                                                                         hec_node_db_serv_inst   = iv_guid_db_serv_inst
                                                                                         hec_node_db_inst        = iv_guid_db_inst
                                                                                         hec_node_db_node        = iv_guid_db_node
                                                                                         hec_node_db_serv_pc     = iv_guid_db_serv_pc
                                                                                         hec_node_db_storage_qty = iv_guid_db_storage_qty  ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_db_storage_single.

    TRY .
        rs_db_storage = CORRESPONDING #( me->mo_data_provider->get_db_storage( is_key = VALUE #( hec_node_solution       = iv_guid_solution
                                                                                hec_node_tier           = iv_guid_tier
                                                                                hec_node_db_serv_inst   = iv_guid_db_serv_inst
                                                                                hec_node_db_inst        = iv_guid_db_inst
                                                                                hec_node_db_node        = iv_guid_db_node
                                                                                hec_node_db_serv_pc     = iv_guid_db_serv_pc
                                                                                hec_node_db_server      = iv_guid_db_server
                                                                                hec_node_db_storage     = iv_guid_db_storage    ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_delivery_unit.

    TRY .
        IF me->mv_delivery_unit_guid IS NOT INITIAL.
          rs_delivery_unit = CORRESPONDING #( me->mo_data_provider->get_delivery_unit( is_key = me->mv_delivery_unit_guid ) ).
        ELSE.
*          rs_delivery_unit = me->mo_data_provider->get_delivery_unit_by_config( is_config_key = me->ms_root_key ).
          rs_delivery_unit = CORRESPONDING #(  me->mo_data_provider->get_delivery_unit_by_config( ) ).
          me->mv_delivery_unit_guid = rs_delivery_unit-hec_node_delivery_unit.
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_if_baseline_multi.

    DATA: ls_key          TYPE /hec1/datacenter_guid,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_datacenter IS INITIAL.

          "get ALL for complete Config
*          rt_if_baseline = me->mo_data_provider->get_infstr_baselines_by_config( is_config_key = me->ms_root_key ).
          rt_if_baseline = me->mo_data_provider->get_infstr_baselines_by_config( ).

        ELSE.
          "set key structure
          ls_key          = iv_guid_datacenter.
          lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-datacenter.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_if_baseline_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          <fs_key> = iv_guid_datacenter.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_if_baseline = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_if_baseline_single.

    TRY .
        rs_if_baseline = CORRESPONDING #( me->mo_data_provider->get_infstr_baseline( is_key = VALUE #( hec_node_datacenter  = iv_guid_datacenter
                                                                                      hec_node_if_baseline = iv_guid_if_baseline ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_instance_db_multi.

    DATA: ls_key          TYPE /hec1/s_key_db_server_inst,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_solution     IS INITIAL AND
           iv_guid_tier         IS INITIAL AND
           iv_guid_db_serv_inst IS INITIAL.

          "get ALL for complete Config
*          rt_inst_db = me->mo_data_provider->get_db_instances_by_config( is_config_key = me->ms_root_key ).
          rt_inst_db = me->mo_data_provider->get_db_instances_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution     = iv_guid_solution.
          ls_key-hec_node_tier         = iv_guid_tier.
          ls_key-hec_node_db_serv_inst = iv_guid_db_serv_inst.

          "determine source key structure
          IF iv_guid_db_serv_inst IS NOT INITIAL.
            IF iv_guid_tier     IS INITIAL OR
               iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-db_srv_inst.
            ENDIF.
          ELSEIF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_db_inst_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_inst_db = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_instance_db_single.

    TRY .
        rs_inst_db = CORRESPONDING #( me->mo_data_provider->get_db_instance( is_key = VALUE #( hec_node_solution       = iv_guid_solution
                                                                              hec_node_tier           = iv_guid_tier
                                                                              hec_node_db_serv_inst   = iv_guid_db_serv_inst
                                                                              hec_node_db_inst        = iv_guid_db_inst      ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_landsc_price_aggre_multi.

    DATA: ls_key          TYPE /hec1/landscape_guid,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_landscape_guid IS INITIAL.

          "get ALL for complete Config
          rt_landsc_price_aggre = CORRESPONDING #( me->mo_data_provider->get_landsc_price_aggre_by_conf( ) ).

        ELSE.
          "set key structure
          ls_key          = iv_landscape_guid.
          lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-landscape.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_landsc_price_aggre_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          <fs_key> = iv_landscape_guid.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_landsc_price_aggre = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_man_service_baseline.

*    TRY .
*        IF me->mv_man_servic_baseline_guid IS NOT INITIAL.
*          rs_man_service_baseline = me->mo_data_provider->get_man_svc_baseline( is_key = me->mv_man_servic_baseline_guid ).
*        ELSE.
**          rs_man_service_baseline = me->mo_data_provider->get_man_svc_baseline_by_config( is_config_key = me->ms_root_key ).
**          rs_man_service_baseline = me->mo_data_provider->get_man_svc_baseline_by_config( ).
*          me->mv_man_servic_baseline_guid = rt_man_service_baseline[ 1 ]-hec_node_man_service_bl.
*        ENDIF.
*
*      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
*        RETURN. ">>>>>>>>
*    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_material_multi.

    DATA: ls_key          TYPE /hec1/s_key_tier,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_solution IS INITIAL AND
           iv_guid_tier     IS INITIAL.

          "get ALL for complete Config
*          rt_material = me->mo_data_provider->get_materials_by_config( is_config_key = me->ms_root_key ).
          rt_material = me->mo_data_provider->get_materials_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution = iv_guid_solution.
          ls_key-hec_node_tier     = iv_guid_tier.

          "determine source key structure
          IF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_material_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_material = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_material_single.

    TRY .
        rs_material =  CORRESPONDING #( me->mo_data_provider->get_material( is_key = VALUE #( hec_node_solution = iv_guid_solution
                                                                            hec_node_tier     = iv_guid_tier
                                                                            hec_node_material = iv_guid_material  ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_network_segment_multi.

    DATA: ls_key          TYPE /hec1/s_key_if_baseline,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_datacenter  IS INITIAL AND
           iv_guid_if_baseline IS INITIAL.

          "get ALL for complete Config
*          rt_network_segment = me->mo_data_provider->get_network_segments_by_config( is_config_key = me->ms_root_key ).
          rt_network_segment = me->mo_data_provider->get_network_segments_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_datacenter  = iv_guid_datacenter.
          ls_key-hec_node_if_baseline = iv_guid_if_baseline.

          "determine source key structure
          IF iv_guid_if_baseline IS NOT INITIAL.
            IF iv_guid_datacenter IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-if_baseline.
            ENDIF.
          ELSEIF iv_guid_datacenter IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-datacenter.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_network_segm_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-datacenter.
            <fs_key> = iv_guid_datacenter.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_network_segment = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_network_segment_single.

    TRY .
        rs_network_segment = CORRESPONDING #( me->mo_data_provider->get_network_segment( is_key = VALUE #( hec_node_datacenter      = iv_guid_datacenter
                                                                                          hec_node_if_baseline     = iv_guid_if_baseline
                                                                                          hec_node_network_segment = iv_guid_network_segment ) ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_phase_multi.

    IF iv_guid_parent_phase IS INITIAL AND
       iv_guid_phase        IS INITIAL.

      "get all from Config
      TRY .
*          rt_phase = me->mo_data_provider->get_phases_by_config( is_config_key = me->ms_root_key ).
          rt_phase = me->mo_data_provider->get_phases_by_config( ).

        CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
          RETURN. ">>>>>>>>
      ENDTRY.

    ELSEIF iv_guid_parent_phase IS NOT INITIAL AND
           iv_guid_phase        IS INITIAL.

      "first get all from Config, then filter
      TRY .
*          rt_phase = me->mo_data_provider->get_phases_by_config( is_config_key = me->ms_root_key ).
          rt_phase = me->mo_data_provider->get_phases_by_config( ).
          DELETE rt_phase WHERE hec_node_parent_phase <> iv_guid_parent_phase. "#EC CI_SORTSEQ

        CATCH /hec1/cx_data_provider INTO lo_cx.
          RETURN. ">>>>>>>>
      ENDTRY.

    ELSEIF iv_guid_parent_phase IS INITIAL.
      RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_phase_single.

    TRY .
        rs_phase = CORRESPONDING #( me->mo_data_provider->get_phase( iv_key = iv_guid_phase ) ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_root.

    TRY .
        rs_root = me->mo_data_provider->get_landscape_by_config( ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_add_storage_dc.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_add_storage_dc_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_add_storage_dc.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-add_storage_datacenter
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_add_storage_cl.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_add_storage_class_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_add_storage_cl.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-add_storage_class
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_add_storage_am.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_add_storage_amount_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_add_storage_am.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-add_storage_amount
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_contact.

    DATA lt_data TYPE /hec1/t_data_contact_ct.

    CLEAR: eo_message,
           rt_contact.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-contact
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-contact-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_contact = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_contact_multi.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        "get ALL for complete Config
        rt_contact = me->mo_data_provider->get_contacts_by_config( ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_contact.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_contact_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_contact.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-contact
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD set_bopf_msg_to_fpm_msg.

    IF io_message IS BOUND.
      io_message->get_messages( IMPORTING et_message = DATA(lt_message) ).  " Table of msg instance that are contained in the msg object

      LOOP AT lt_message ASSIGNING FIELD-SYMBOL(<fs_message>).
        cl_fpm=>get_instance( )->mo_message_manager->report_message( iv_message_text = <fs_message>-message->get_text( )             " Message text to be reported
                                                                     is_enable_message_navigation = abap_true

                                                                     iv_severity     = SWITCH #( <fs_message>-severity              " Report the severity of the message
                                                                                                 WHEN 'I' THEN 'W'
                                                                                                 ELSE <fs_message>-severity ) ).
      ENDLOOP.
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_tier_sla.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_tier_sla_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_tier_sla.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-tier_sla
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_tier_sla.

    DATA: lt_sel_param TYPE /bobf/t_frw_query_selparam,
          lt_data      TYPE /hec1/t_data_tier_sla_ct.

    CLEAR: eo_message,
           rt_tier_sla.

    TRY.
        me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-tier_sla
                                                                iv_query_key = /hec1/if_configuration_c=>sc_query-tier_sla-select_by_elements
                                                                it_key       = it_key
                                                      IMPORTING eo_message   = eo_message
                                                                rt_data      = lt_data ).

        rt_tier_sla = CORRESPONDING #( lt_data ).

      CATCH cx_sy_itab_line_not_found.
        "nothing found
        "no exception
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_tier_sla_multi.

    DATA: ls_key          TYPE /hec1/s_key_tier,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_solution IS INITIAL AND
           iv_guid_tier     IS INITIAL.

          "get ALL for complete Config
*          rt_material = me->mo_data_provider->get_materials_by_config( is_config_key = me->ms_root_key ).
          rt_tier_sla = me->mo_data_provider->get_tier_slas_by_config( ).

        ELSE.
          "set key structure
          ls_key-hec_node_solution = iv_guid_solution.
          ls_key-hec_node_tier     = iv_guid_tier.

          "determine source key structure
          IF iv_guid_tier IS NOT INITIAL.
            IF iv_guid_solution IS INITIAL.
              RETURN. ">>>>>>>>   INCOMPLETE KEY - not possible to get data
            ELSE.
              lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-tier.
            ENDIF.
          ELSEIF iv_guid_solution IS NOT INITIAL.
            lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
          ENDIF.

          "only to prevent dump - this should not happen here
          IF lv_struc_source IS INITIAL.
            RETURN. ">>>>>>>>
          ENDIF.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_material_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          IF lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.
            <fs_key> = iv_guid_solution.
          ELSE.
            <fs_key> = CORRESPONDING #( ls_key ).
          ENDIF.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_tier_sla = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_lt_backup_am.
    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_lt_backup_amount_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_lt_backup_amount.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-lt_backup_amount
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_contact_ref.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_contact_ref_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_contact_ref.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-contact_reference
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_contact_ref.

    DATA lt_data TYPE /hec1/t_data_contact_ref_ct.

    CLEAR: eo_message,
           rt_contact_ref.

    me->/hec1/if_bopf_config_model_ge~get_object( EXPORTING iv_node_key  = /hec1/if_configuration_c=>sc_node-contact_reference
                                                            iv_query_key = /hec1/if_configuration_c=>sc_query-contact_reference-select_by_elements
                                                            it_key       = it_key
                                                  IMPORTING eo_message   = eo_message
                                                            rt_data      = lt_data ).

    rt_contact_ref = CORRESPONDING #( lt_data ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_contact_ref_multi.

    DATA: ls_key          TYPE /hec1/contact_guid,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_contact IS INITIAL.

          "get ALL for complete Config
          rt_contact_ref = me->mo_data_provider->get_contacts_refs_by_config( ).

        ELSE.
          "set key structure
          ls_key          = iv_guid_contact.
          lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-contact.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_contact_ref_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          <fs_key> = iv_guid_contact.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_contact_ref = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_se~update_transport_path.

    CLEAR eo_message.

    DATA(lr_data) = NEW /hec1/s_data_transport_path_cs( ).
    ASSIGN lr_data->* TO FIELD-SYMBOL(<fs_data>).

    <fs_data> = is_transport_path.

    me->/hec1/if_bopf_config_model_se~update_object( EXPORTING iv_node    = /hec1/if_configuration_c=>sc_node-transport_path
                                                               ir_data    = lr_data
                                                     IMPORTING eo_message = eo_message ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_transport_path_multi.

    DATA: ls_key          TYPE /hec1/solution_guid,
          lr_data         TYPE REF TO data,
          lv_struc_source TYPE strukname.

    FIELD-SYMBOLS: <fs_key>  TYPE any,
                   <fs_data> TYPE ANY TABLE.

    TRY .
        IF iv_guid_solution IS INITIAL.

          "get ALL for complete Config
          rt_transport_path = me->mo_data_provider->get_transport_paths_by_config( ).

        ELSE.
          "set key structure
          ls_key          = iv_guid_solution.
          lv_struc_source = /hec1/if_bopf_constants=>gc_struc_key-solution.

          "create source & target
          CREATE DATA lr_data TYPE (lv_struc_source).
          ASSIGN lr_data->* TO <fs_key>.
          CREATE DATA lr_data TYPE /hec1/t_data_transport_path_ct.
          ASSIGN lr_data->* TO <fs_data>.

          "set values to source
          <fs_key> = iv_guid_solution.

          "get data from BOPF
          me->mo_data_provider->get_objects_dynamic( EXPORTING is_key  = <fs_key>
                                                     IMPORTING et_data = <fs_data> ).

          rt_transport_path = CORRESPONDING #( <fs_data> ).
        ENDIF.

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_act~apm_change.

    DATA lt_keys TYPE /bobf/t_frw_node .
    DATA lt_root TYPE /hec1/t_config_root_ct.

    DATA(lo_transaction_manager) = /bobf/cl_tra_trans_mgr_factory=>get_transaction_manager( ).

    lo_transaction_manager->create_sync_point( ).

    DATA(lo_service_manager) =   /bobf/cl_tra_serv_mgr_factory=>get_service_manager( /hec1/if_configuration_c=>sc_bo_key ).

    lo_service_manager->do_action( EXPORTING iv_act_key           = /hec1/if_configuration_c=>sc_action-root-apm_change
                                             it_key               = VALUE #( ( key = iv_key ) )
                                             is_parameters        = REF #( is_act_apm_change )
                                   IMPORTING et_data              = lt_keys
                                             eo_message           = DATA(lo_message)
                                             et_failed_key        = DATA(lt_failed_key)
                                             et_failed_action_key = DATA(lt_failed_action) ).

    IF lo_message IS NOT INITIAL AND lo_message->check( ).
      me->set_bopf_msg_to_fpm_msg( io_message = lo_message ).
      lo_transaction_manager->rollback_to_sync_point( ).
      rv_success = abap_false.
      RETURN.
    ENDIF.

    TRY.
        DATA(ls_key) = lt_keys[ node = /hec1/if_configuration_c=>sc_node-root ].
        lo_service_manager->retrieve(
          EXPORTING
            iv_node_key             = ls_key-node
            it_key                  = VALUE #( ( key = ls_key-key ) )
          IMPORTING
            et_data                 = lt_root
            eo_message              = lo_message
        ).
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

    IF ( lt_root IS INITIAL ).
      rv_success = abap_false.
      lo_transaction_manager->rollback_to_sync_point( ).
      RETURN.
    ELSE.

      lo_transaction_manager->release_sync_point( ).
      lo_transaction_manager->save(  ). " /bobf/if_tra_c=>gc_tp_save
      TRY.
          ev_new_hec_conf_version = lt_root[ 1 ]-hec_conf_version.
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.
      rv_success = abap_true.
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_ge~get_transport_path.
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_model_get~get_man_service_baseline_multi.
" Das ist ein Test.
    TRY .
        rt_man_service_baseline = me->mo_data_provider->get_man_svc_baseline_by_config( ).

      CATCH /hec1/cx_data_provider INTO DATA(lo_cx).
        RETURN. ">>>>>>>>
    ENDTRY.

  ENDMETHOD.
ENDCLASS.