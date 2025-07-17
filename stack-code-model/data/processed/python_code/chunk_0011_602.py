CLASS /hec1/cl_config_action_helper DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.

    INTERFACES /hec1/if_bopf_action_helper .
  PROTECTED SECTION.
private section.

  class-methods CREATE_APP_SERVER
    importing
      !IV_ROOT_KEY type /BOBF/CONF_KEY
      !IS_APP_SERV_PERF_CAT type /HEC1/S_DATA_APP_SERV_PC_CS
      !IT_APP_STORAGE_QTY type /HEC1/T_DATA_APP_STORAGEQTY_CT
      !IT_APP_SERVER type /HEC1/T_DATA_APP_SERV_CT
      !IT_APP_STORAGE type /HEC1/T_DATA_APP_STORAGE_CT
      !IT_APP_BACKUP type /HEC1/T_DATA_APP_BACKUP_CT
      !IT_PHASING type /HEC1/T_DATA_PHASE_CT
      !IT_PHASING_ALL type /HEC1/T_DATA_PHASE_CT
    changing
      !CO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
      !CT_MODIFICATION type /BOBF/T_FRW_MODIFICATION .
  class-methods CREATE_APP_SERVER_PC
    importing
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IV_ROOT_KEY type /BOBF/CONF_KEY
      !IS_APP_NODE type /HEC1/S_DATA_APP_NODE_CS
      !IT_APP_SERV_PERF_CAT type /HEC1/T_DATA_APP_SERV_PC_CT
      !IT_APP_STORAGE_QTY type /HEC1/T_DATA_APP_STORAGEQTY_CT
      !IT_APP_SERVER type /HEC1/T_DATA_APP_SERV_CT
      !IT_APP_STORAGE type /HEC1/T_DATA_APP_STORAGE_CT
      !IT_APP_BACKUP type /HEC1/T_DATA_APP_BACKUP_CT
      !IT_PHASING type /HEC1/T_DATA_PHASE_CT
      !IT_PHASING_ALL type /HEC1/T_DATA_PHASE_CT
    changing
      !CO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    returning
      value(RT_MODIFICATION) type /BOBF/T_FRW_MODIFICATION .
  class-methods CREATE_APP_STORAGE
    importing
      !IV_ROOT_KEY type /BOBF/CONF_KEY
      !IS_APP_SERVER type /HEC1/S_DATA_APP_SERV_CS
      !IT_APP_STORAGE type /HEC1/T_DATA_APP_STORAGE_CT
      !IT_APP_BACKUP type /HEC1/T_DATA_APP_BACKUP_CT
      !IT_PHASING type /HEC1/T_DATA_PHASE_CT
      !IT_PHASING_ALL type /HEC1/T_DATA_PHASE_CT
    changing
      !CO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
      !CT_MODIFICATION type /BOBF/T_FRW_MODIFICATION .
  class-methods CREATE_APP_STORAGE_AMOUNT
    importing
      !IV_ROOT_KEY type /BOBF/CONF_KEY
      !IS_APP_SERV_PERF_CAT type /HEC1/S_DATA_APP_SERV_PC_CS
      !IT_APP_STORAGE_QTY type /HEC1/T_DATA_APP_STORAGEQTY_CT
      !IT_PHASING type /HEC1/T_DATA_PHASE_CT
      !IT_PHASING_ALL type /HEC1/T_DATA_PHASE_CT
    changing
      !CO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
      !CT_MODIFICATION type /BOBF/T_FRW_MODIFICATION .
  class-methods CREATE_APP_STORAGE_BACKUP
    importing
      !IV_ROOT_KEY type /BOBF/CONF_KEY
      !IS_APP_STORAGE type /HEC1/S_DATA_APP_STORAGE_CS
      !IT_APP_BACKUP type /HEC1/T_DATA_APP_BACKUP_CT
      !IT_PHASING type /HEC1/T_DATA_PHASE_CT
      !IT_PHASING_ALL type /HEC1/T_DATA_PHASE_CT
    changing
      !CO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
      !CT_MODIFICATION type /BOBF/T_FRW_MODIFICATION .
  class-methods CREATE_DB_SERVER
    importing
      !IV_ROOT_KEY type /BOBF/CONF_KEY
      !IS_DB_SERV_PERF_CAT type /HEC1/S_DATA_DB_SERV_PC_CS
      !IT_DB_STORAGE_QTY type /HEC1/T_DATA_DB_STORAGE_QTY_CT
      !IT_DB_SERVER type /HEC1/T_DATA_DB_SERV_CT
      !IT_DB_STORAGE type /HEC1/T_DATA_DB_STORAGE_CT
      !IT_DB_BACKUP type /HEC1/T_DATA_DB_BACKUP_CT
      !IT_PHASING type /HEC1/T_DATA_PHASE_CT
      !IT_PHASING_ALL type /HEC1/T_DATA_PHASE_CT
    changing
      !CO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
      !CT_MODIFICATION type /BOBF/T_FRW_MODIFICATION .
  class-methods CREATE_DB_SERVER_PC
    importing
      !IV_ROOT_KEY type /BOBF/CONF_KEY
      !IS_DB_NODE type /HEC1/S_DATA_DB_NODE_CS
      !IT_DB_SERV_PERF_CAT type /HEC1/T_DATA_DB_SERV_PC_CT
      !IT_DB_STORAGE_QTY type /HEC1/T_DATA_DB_STORAGE_QTY_CT
      !IT_DB_SERVER type /HEC1/T_DATA_DB_SERV_CT
      !IT_DB_STORAGE type /HEC1/T_DATA_DB_STORAGE_CT
      !IT_DB_BACKUP type /HEC1/T_DATA_DB_BACKUP_CT
      !IT_PHASING type /HEC1/T_DATA_PHASE_CT
      !IT_PHASING_ALL type /HEC1/T_DATA_PHASE_CT
    changing
      !CO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    returning
      value(RT_MODIFICATION) type /BOBF/T_FRW_MODIFICATION .
  class-methods CREATE_DB_STORAGE
    importing
      !IV_ROOT_KEY type /BOBF/CONF_KEY
      !IS_DB_SERVER type /HEC1/S_DATA_DB_SERV_CS
      !IT_DB_STORAGE type /HEC1/T_DATA_DB_STORAGE_CT
      !IT_DB_BACKUP type /HEC1/T_DATA_DB_BACKUP_CT
      !IT_PHASING type /HEC1/T_DATA_PHASE_CT
      !IT_PHASING_ALL type /HEC1/T_DATA_PHASE_CT
    changing
      !CO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
      !CT_MODIFICATION type /BOBF/T_FRW_MODIFICATION .
  class-methods CREATE_DB_STORAGE_AMOUNT
    importing
      !IV_ROOT_KEY type /BOBF/CONF_KEY
      !IS_DB_SERV_PERF_CAT type /HEC1/S_DATA_DB_SERV_PC_CS
      !IT_DB_STORAGE_QTY type /HEC1/T_DATA_DB_STORAGE_QTY_CT
      !IT_PHASING type /HEC1/T_DATA_PHASE_CT
      !IT_PHASING_ALL type /HEC1/T_DATA_PHASE_CT
    changing
      !CO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
      !CT_MODIFICATION type /BOBF/T_FRW_MODIFICATION .
  class-methods CREATE_DB_STORAGE_BACKUP
    importing
      !IV_ROOT_KEY type /BOBF/CONF_KEY
      !IS_DB_STORAGE type /HEC1/S_DATA_DB_STORAGE_CS
      !IT_DB_BACKUP type /HEC1/T_DATA_DB_BACKUP_CT
      !IT_PHASING type /HEC1/T_DATA_PHASE_CT
      !IT_PHASING_ALL type /HEC1/T_DATA_PHASE_CT
    changing
      !CO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
      !CT_MODIFICATION type /BOBF/T_FRW_MODIFICATION .
  class-methods GENERATE_PHASING
    importing
      !IS_NODE_PHASE type /HEC1/S_DATA_PHASE_CS
      !IT_TABLE type TABLE
      !IT_PHASING_ALL type /HEC1/T_DATA_PHASE_CT
    exporting
      !ET_PHASE_GENERATED type /HEC1/T_DATA_PHASE_CT
      !ET_NEW_INSTANCE type TABLE
    changing
      !CO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE .
ENDCLASS.



CLASS /HEC1/CL_CONFIG_ACTION_HELPER IMPLEMENTATION.


  METHOD /hec1/if_bopf_action_helper~create_tier.

    FIELD-SYMBOLS: <fs_landscape>  TYPE /hec1/s_config_root_cs,
                   <fs_solution>   TYPE /hec1/s_data_solution_cs,
                   <fs_datacenter> TYPE /hec1/t_data_datacenter_ct.


    ASSIGN is_landscape->* TO <fs_landscape>.
    ASSIGN is_solution->*  TO <fs_solution>.

    IF <fs_landscape> IS ASSIGNED AND
       <fs_solution>  IS ASSIGNED.
      "-----------------------------------
      " Get tier stack
      "-----------------------------------
      SELECT *                                "#EC CI_ALL_FIELDS_NEEDED
        FROM /hec1/i_tierstackbasic
       WHERE hec_apm_guid      = @<fs_landscape>-hec_apm_guid     AND
             hec_solution_guid = @<fs_solution>-hec_solution_guid
        INTO TABLE @DATA(lt_tier_stack).


      "-----------------------------------
      " Get tier category
      "-----------------------------------
      SELECT *                                "#EC CI_ALL_FIELDS_NEEDED
        FROM /hec1/i_tiercategorybasic
       WHERE hec_apm_guid      = @<fs_landscape>-hec_apm_guid      AND
             hec_flat_mat_guid = @<fs_landscape>-hec_flat_mat_guid
        INTO TABLE @DATA(lt_tier_category).


      "-----------------------------------
      " Get tier type description
      " and DR option
      "-----------------------------------
      SELECT *                                "#EC CI_ALL_FIELDS_NEEDED
        FROM /hec1/i_tiertypebasic
       WHERE hec_apm_guid      = @<fs_landscape>-hec_apm_guid      AND
             hec_flat_mat_guid = @<fs_landscape>-hec_flat_mat_guid
        INTO TABLE @DATA(lt_tier_type).


      "-----------------------------------
      " Get DB server instance data
      " for tier level
      "-----------------------------------
      IF <fs_solution>-hec_sol_db_srv_required = abap_true.

        SELECT *                              "#EC CI_ALL_FIELDS_NEEDED
          FROM /hec1/i_dbservinstancenobasic
         WHERE hec_apm_guid      = @<fs_landscape>-hec_apm_guid     AND
               hec_solution_guid = @<fs_solution>-hec_solution_guid
          INTO TABLE @DATA(lt_db_serv_inst_no).

      ENDIF.


      "-----------------------------------
      " Get App server instance data
      " for tier level
      "-----------------------------------
      IF <fs_solution>-hec_sol_app_srv_required = abap_true.

        SELECT *                              "#EC CI_ALL_FIELDS_NEEDED
          FROM /hec1/i_appservinstancenobasic
         WHERE hec_apm_guid      = @<fs_landscape>-hec_apm_guid     AND
               hec_solution_guid = @<fs_solution>-hec_solution_guid
          INTO TABLE @DATA(lt_app_serv_inst_no).

      ENDIF.


      "-----------------------------------
      " Fill tier data
      "-----------------------------------
      DO iv_create_no_tier TIMES.
        IF iv_stack_tier_no > 1.
          " Get tier stack relation GUID
          DATA(lv_relation_guid) = /rbp/cl_general_utilities=>get_new_guid22( ) .
        ENDIF.

        LOOP AT lt_tier_stack ASSIGNING FIELD-SYMBOL(<fs_stack>).
          TRY.
              DATA(ls_tier_category) = lt_tier_category[ hec_tier_cat_value = iv_tier_category_value ].
              DATA(ls_tier_type)     = lt_tier_type[ hec_tier_cat_guid = ls_tier_category-hec_tier_cat_guid ].
            CATCH cx_sy_itab_line_not_found.
          ENDTRY.

          " Get number of mandantory DB server instance
          SELECT COUNT( * )
            FROM /hec1/i_dbservinstancenobasic
           WHERE hec_apm_guid             = @<fs_landscape>-hec_apm_guid         AND
                 hec_solution_guid        = @<fs_solution>-hec_solution_guid     AND
                 hec_sol_tier_stack_value = @<fs_stack>-hec_sol_tier_stack_value AND
                 hec_tier_dbs_relev_value = '01'                                 AND
                 hec_srv_inst_rel_value   = '01'
            INTO @DATA(lv_dbsi_count).

          " Exist optional DB server instance
          SELECT SINGLE *
            FROM /hec1/i_dbservinstancenobasic
           WHERE hec_apm_guid             = @<fs_landscape>-hec_apm_guid         AND
                 hec_solution_guid        = @<fs_solution>-hec_solution_guid     AND
                 hec_sol_tier_stack_value = @<fs_stack>-hec_sol_tier_stack_value AND
                 hec_tier_dbs_relev_value = '01'                                 AND
                 hec_srv_inst_rel_value   = '02'
            INTO @DATA(ls_dbsi_optional).


          " Get number of mandantory App server instance
          SELECT COUNT( * )
            FROM /hec1/i_appservinstancenobasic
           WHERE hec_apm_guid              = @<fs_landscape>-hec_apm_guid         AND
                 hec_solution_guid         = @<fs_solution>-hec_solution_guid     AND
                 hec_sol_tier_stack_value  = @<fs_stack>-hec_sol_tier_stack_value AND
                 hec_tier_apps_relev_value = '01'                                 AND
                 hec_srv_inst_rel_value    = '01'
            INTO @DATA(lv_apsi_count).


          " Get effort building block GUID
          SELECT SINGLE hec_timebased_effort_bb_guid
            FROM /hec1/i_tiertbbbbasic
           WHERE hec_apm_guid         = @<fs_landscape>-hec_apm_guid         AND
                 hec_solution_guid    = @<fs_solution>-hec_solution_guid     AND
                 hec_tier_stack_value = @<fs_stack>-hec_sol_tier_stack_value AND
                 hec_tier_cat_value   = @iv_tier_category_value
            INTO @DATA(lv_effort_bb_guid).


          " Get data center GUID
          DATA(lr_datacenter) = /hec1/cl_config_helper=>get_datacenter( it_root_key = VALUE #( ( key = <fs_solution>-root_key ) )
                                                                        io_read     = io_read ).

          ASSIGN lr_datacenter->* TO <fs_datacenter>.
          IF <fs_datacenter> IS ASSIGNED.

            DATA(lt_datacenter) = VALUE /hec1/t_data_datacenter_ct( FOR wa IN <fs_datacenter>
                                                                    WHERE ( hec_datacenter_type_value = /hec1/if_config_constants=>gc_datacenter_type_primary )
                                                                    ( wa )                                                                                      ).

            IF lines( lt_datacenter ) = 1.
              TRY.
                  DATA(lv_datacenter_guid) = lt_datacenter[ 1 ]-hec_node_datacenter.
                CATCH cx_sy_itab_line_not_found.
              ENDTRY.
            ENDIF.
          ENDIF. " IF <fs_datacenter> IS ASSIGNED.


          DATA(lr_tier) = NEW /hec1/s_data_tier_cs( parent_key                  = <fs_solution>-key
                                                    key                         = /bopf/cl_frw_factory=>get_new_key( )
                                                    hec_node_solution           = <fs_solution>-hec_node_solution
                                                    hec_node_tier               = /rbp/cl_general_utilities=>get_new_guid22( )
                                                    hec_comp_config_id          = <fs_landscape>-hec_confid
                                                    hec_comp_config_version     = <fs_landscape>-hec_conf_version
                                                    hec_apm_guid                = <fs_landscape>-hec_apm_guid
                                                    hec_apm_descr               = <fs_landscape>-hec_apm_descr
                                                    hec_solution_guid           = <fs_solution>-hec_solution_guid
                                                    hec_related_stack           = COND #( WHEN lv_relation_guid IS INITIAL
                                                                                          THEN abap_false
                                                                                          ELSE abap_true                   )
                                                    hec_related_stack_guid      = lv_relation_guid
                                                    hec_sol_tier_stack_guid     = <fs_stack>-hec_sol_tier_stack_guid
                                                    hec_sol_tier_stack_value    = <fs_stack>-hec_sol_tier_stack_value
                                                    hec_sol_tier_stack_descr    = <fs_stack>-hec_sol_tier_stack_descr
                                                    hec_disaster_rec_option     = SWITCH #( iv_tier_category_value
                                                                                            WHEN /hec1/if_config_constants=>gc_tier_category-prod
                                                                                            THEN ls_tier_type-hec_disaster_rec_option
                                                                                            ELSE space                                             )
                                                    hec_tier_cat_value          = ls_tier_category-hec_tier_cat_value
                                                    hec_tier_cat_descr          = ls_tier_category-hec_tier_cat_descr
                                                    hec_tier_type_value         = SWITCH #( iv_tier_category_value
                                                                                            WHEN /hec1/if_config_constants=>gc_tier_category-prod
                                                                                            THEN ls_tier_type-hec_tier_type_value
                                                                                            ELSE space                                             )
                                                    hec_tier_type_descr         = SWITCH #( iv_tier_category_value
                                                                                            WHEN /hec1/if_config_constants=>gc_tier_category-prod
                                                                                            THEN ls_tier_type-hec_tier_type_descr
                                                                                            ELSE space                                             )
                                                    hec_tier_impl_type_value    = <fs_solution>-hec_sol_impl_type_value
                                                    hec_tier_impl_type_descr    = <fs_solution>-hec_sol_impl_type_descr
                                                    hec_db_srv_required         = <fs_stack>-hec_db_srv_required
                                                    hec_db_srv_relevance_value  = <fs_stack>-hec_db_srv_relevance_value
                                                    hec_db_srv_relevance_descr  = <fs_stack>-hec_db_srv_relevance_descr
                                                    hec_db_srv_qty              = lv_dbsi_count
                                                    hec_db_srv_opt_exist        = COND #( WHEN ls_dbsi_optional IS INITIAL
                                                                                          THEN abap_false
                                                                                          ELSE abap_true                   )
                                                    hec_app_srv_required        = <fs_stack>-hec_app_srv_required
                                                    hec_app_srv_relevance_value = <fs_stack>-hec_app_srv_relevance_value
                                                    hec_app_srv_relevance_descr = <fs_stack>-hec_app_srv_relevance_descr
                                                    hec_app_srv_qty             = lv_apsi_count
                                                    hec_tier_datacenter_guid    = lv_datacenter_guid
                                                    hec_system_timezone         = <fs_landscape>-hec_system_timezone
                                                    hec_businesspartner         = <fs_landscape>-hec_businesspartner
                                                    hec_tier_language_list      = <fs_solution>-hec_sol_language_list
                                                    hec_tier_language_sys_alt   = <fs_solution>-hec_sol_language_sys_alt
                                                    hec_tier_language_sys_def   = <fs_solution>-hec_sol_language_sys_def
                                                    hec_tier_recurrence_type    = COND #( WHEN iv_tier_category_value = /hec1/if_config_constants=>gc_tier_category-prod
                                                                                          THEN <fs_landscape>-hec_prod_recurrence_type
                                                                                          ELSE <fs_landscape>-hec_nprod_recurrence_type                            )
                                                    hec_tier_recurrence_interval = COND #( WHEN iv_tier_category_value = /hec1/if_config_constants=>gc_tier_category-prod
                                                                                           THEN <fs_landscape>-hec_prod_recurrence_interval
                                                                                           ELSE <fs_landscape>-hec_nprod_recurrence_interval                        )
                                                    hec_tier_weekday             = COND #( WHEN iv_tier_category_value = /hec1/if_config_constants=>gc_tier_category-prod
                                                                                           THEN <fs_landscape>-hec_prod_weekday
                                                                                           ELSE <fs_landscape>-hec_nprod_weekday                                    )
                                                    hec_tier_starttime           = COND #( WHEN iv_tier_category_value = /hec1/if_config_constants=>gc_tier_category-prod
                                                                                           THEN <fs_landscape>-hec_prod_starttime
                                                                                           ELSE <fs_landscape>-hec_nprod_starttime                                  )
                                                    hec_tier_duration            = COND #( WHEN iv_tier_category_value = /hec1/if_config_constants=>gc_tier_category-prod
                                                                                           THEN <fs_landscape>-hec_prod_duration
                                                                                           ELSE <fs_landscape>-hec_nprod_duration                                   )
                                                    hec_tier_duration_unit       = COND #( WHEN iv_tier_category_value = /hec1/if_config_constants=>gc_tier_category-prod
                                                                                           THEN <fs_landscape>-hec_prod_duration_unit
                                                                                           ELSE <fs_landscape>-hec_nprod_duration_unit                              )
                                                    hec_tier_cmp_timezone        = COND #( WHEN iv_tier_category_value = /hec1/if_config_constants=>gc_tier_category-prod
                                                                                           THEN <fs_landscape>-hec_prod_cmp_timezone
                                                                                           ELSE <fs_landscape>-hec_nprod_cmp_timezone                               )
                                                    hec_bf_activation            = <fs_solution>-hec_bf_activation
                                                    hec_bpacti_tmpl_sent_to_cust = <fs_solution>-hec_bpacti_tmpl_sent_to_cust
                                                    hec_bpacti_tmpl_upl_by_cust  = <fs_solution>-hec_bpacti_tmpl_upl_by_cust
                                                    hec_db_version_guid          = <fs_solution>-hec_sol_db_version_guid
                                                    hec_db_version_value         = <fs_solution>-hec_sol_db_version_value
                                                    hec_db_version_descr         = <fs_solution>-hec_sol_db_version_descr
                                                    hec_row_selectable           = abap_true
                                                    hec_phase_assign_allowed     = abap_true
                                                    price                        = /hec1/cl_config_helper=>get_price_timebased_bb( iv_effort_bb_guid = lv_effort_bb_guid
                                                                                                                                   iv_root_key       = <fs_solution>-root_key
                                                                                                                                   io_read           = io_read                )
                                                    crea_uname                   = sy-uname ).

          GET TIME STAMP FIELD lr_tier->crea_date_time.

          INSERT VALUE #( data        = lr_tier
                          node        = /hec1/if_configuration_c=>sc_node-tier
                          source_node = /hec1/if_configuration_c=>sc_node-solution
                          association = /hec1/if_configuration_c=>sc_association-solution-tier
                          source_key  = <fs_solution>-key
                          change_mode = /bobf/if_frw_c=>sc_modify_create
                          key         = lr_tier->key                                            ) INTO TABLE rt_modification.

          CLEAR: lv_apsi_count,
                 lv_dbsi_count,
                 lv_effort_bb_guid,
                 lv_datacenter_guid,
                 ls_dbsi_optional,
                 ls_tier_category,
                 ls_tier_type,
                 lt_datacenter,
                 lr_datacenter,
                 lr_tier.

          UNASSIGN: <fs_datacenter>.
        ENDLOOP. " LOOP AT lt_tier_stack ASSIGNING FIELD-SYMBOL(<fs_stack>).

        CLEAR lv_relation_guid.
      ENDDO. " DO lv_create_no_tier TIMES.
    ENDIF.  " IF <fs_landscape> IS ASSIGNED AND


  ENDMETHOD.


  METHOD /hec1/if_bopf_action_helper~do_synchronize_app_node.

    DATA: lt_app_node           TYPE /hec1/t_data_app_node_ct,
          lt_app_serv_perf_cat  TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_storage_qty    TYPE /hec1/t_data_app_storageqty_ct,
          lt_app_server         TYPE /hec1/t_data_app_serv_ct,
          lt_app_storage        TYPE /hec1/t_data_app_storage_ct,
          lt_app_backup         TYPE /hec1/t_data_app_backup_ct,
          lt_serv_perf_cat      TYPE /hec1/t_data_app_serv_pc_ct,
          lt_storage_qty        TYPE /hec1/t_data_app_storageqty_ct,
          lt_server             TYPE /hec1/t_data_app_serv_ct,
          lt_storage            TYPE /hec1/t_data_app_storage_ct,
          lt_backup             TYPE /hec1/t_data_app_backup_ct,
          lt_phase              TYPE /hec1/t_data_phase_ct,
          lr_app_node           TYPE REF TO /hec1/s_data_app_node_cs,
          lt_alt_key            TYPE TABLE OF /hec1/phase_guid,
          lt_phase_generated    TYPE /hec1/t_data_phase_ct,
          lt_act_param_del_node TYPE /bobf/t_frw_node.


    CLEAR: et_failed_key,
           ev_static_action_failed,
           et_data,
           et_data_link.

*    IF co_message IS NOT BOUND.
*      co_message = /bobf/cl_frw_factory=>get_message( ).
*    ENDIF.

    " **********************************
    " Get none default master node
    " **********************************
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_app_node     ).

    " **********************************
    " Get Phasing
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = VALUE #( FOR app IN lt_app_node
                                                                        ( key = app-root_key ) )
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                                iv_fill_data   = abap_true
                                      IMPORTING et_data        = lt_phase ).

    " I know that all method for BOPF are mass enabled, but this action can only triggered out
    " of the BOPF object from one single BOPF instance, so therefore it should never happen, that
    " in lt_app_node is more then one instance, otherwise it is an error
    IF lines( lt_app_node ) <> 1.
      " Todo error message
      " Error
      RETURN. " >>>>>>
    ELSE.
      " Get the phasing data
      TRY.
          DATA(ls_node_phase) = lt_phase[ hec_node_phase = lt_app_node[ 1 ]-hec_phase_guid ].
          " Get app node standby
          DATA(ls_app_node) = lt_app_node[ 1 ].
        CATCH cx_sy_itab_line_not_found.
          " Todo error message
      ENDTRY.
    ENDIF.

    " **********************************
    " Get root key
    " **********************************
    io_read->get_root_key( EXPORTING iv_node         = is_ctx-node_key
                                     it_key          = it_key
                           IMPORTING et_target_key   = DATA(lt_root_key) ).

    " The root instance should exist always once
    TRY.
        DATA(lv_root_key) = lt_root_key[ 1 ]-key.
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

    " **********************************
    " Get master node
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-def_master_node
                                      IMPORTING et_key_link    = DATA(lt_key_link)
                                                et_target_key  = DATA(lt_key)                                                      ).

    " **********************************
    " Get server performance categories
    " of master node
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = lt_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
                                      IMPORTING et_data        = lt_app_serv_perf_cat                                                     ).

    " **********************************
    " Get server storage amount
    " of master node
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                it_key         = VALUE #( FOR wa IN lt_app_serv_perf_cat
                                                                         ( key = wa-key )                )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_storage_amount
                                      IMPORTING et_data        = lt_app_storage_qty                                                                  ).

    " **********************************
    " Get server of master node
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                it_key         = VALUE #( FOR wa IN lt_app_serv_perf_cat
                                                                         ( key = wa-key )                )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_server
                                      IMPORTING et_data        = lt_app_server                                                              ).


    " **********************************
    " Get server storage of master node
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server
                                                it_key         = VALUE #( FOR wa_serv IN lt_app_server
                                                                         ( key = wa_serv-key )                )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server-app_storage
                                      IMPORTING et_data        = lt_app_storage                                                  ).

    " **********************************
    " Get storage backup of master node
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_storage
                                                it_key         = VALUE #( FOR wa_stor IN lt_app_storage
                                                                         ( key = wa_stor-key )                )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_storage-app_storage_backup
                                      IMPORTING et_data        = lt_app_backup                                                           ).


    " Generate phasing and instances to create
    " for app server performance category
    generate_phasing( EXPORTING is_node_phase      = ls_node_phase
                                it_table           = lt_app_serv_perf_cat
                                it_phasing_all     = lt_phase
                      IMPORTING et_phase_generated = lt_phase_generated
                                et_new_instance    = lt_serv_perf_cat
                      CHANGING  co_message         = co_message            ).


    " Create all dependent sub nodes data
    DATA(rt_modification) = create_app_server_pc( EXPORTING io_read              = io_read
                                                            iv_root_key          = lv_root_key
                                                            is_app_node          = ls_app_node
                                                            it_app_serv_perf_cat = lt_serv_perf_cat
                                                            it_app_storage_qty   = lt_app_storage_qty
                                                            it_app_server        = lt_app_server
                                                            it_app_storage       = lt_app_storage
                                                            it_app_backup        = lt_app_backup
                                                            it_phasing_all       = lt_phase
                                                            it_phasing           = lt_phase_generated
                                                   CHANGING co_message           = co_message          ).

    IF co_message IS BOUND.
      DATA(lv_has_error_msg) = co_message->check( iv_consistency_messages = abap_true
                                                  iv_action_messages      = abap_true ).
    ENDIF.

    IF lv_has_error_msg = abap_false   AND
       rt_modification IS NOT INITIAL.

      " Update no. of server performance category
      LOOP AT        lt_app_node
      REFERENCE INTO lr_app_node.

        lr_app_node->hec_app_srv_perf_cat_qty = lines( lt_serv_perf_cat ).
        lr_app_node->hec_instance_status      = /hec1/if_config_constants=>gc_instance_status-complete.

        INSERT VALUE #( data        = lr_app_node
                        node        = is_ctx-node_key
                        change_mode = /bobf/if_frw_c=>sc_modify_update
                        key         = lr_app_node->key                 ) INTO TABLE rt_modification.

      ENDLOOP.

      " Create all sub nodes
      io_modify->do_modify( rt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).

      /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>sync_config_successfully
                                                     iv_severity = /bobf/cm_frw=>co_severity_success
                                           CHANGING co_message   = co_message                                     ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_bopf_action_helper~do_synchronize_db_node.

    DATA: lt_db_node          TYPE /hec1/t_data_db_node_ct,
          lt_db_serv_perf_cat TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_storage_qty   TYPE /hec1/t_data_db_storage_qty_ct,
          lt_db_server        TYPE /hec1/t_data_db_serv_ct,
          lt_db_storage       TYPE /hec1/t_data_db_storage_ct,
          lt_db_backup        TYPE /hec1/t_data_db_backup_ct,
          lt_serv_perf_cat    TYPE /hec1/t_data_db_serv_pc_ct,
          lt_storage_qty      TYPE /hec1/t_data_db_storage_qty_ct,
          lt_server           TYPE /hec1/t_data_db_serv_ct,
          lt_storage          TYPE /hec1/t_data_db_storage_ct,
          lt_backup           TYPE /hec1/t_data_db_backup_ct,
          lt_phase            TYPE /hec1/t_data_phase_ct,
          lr_db_node          TYPE REF TO /hec1/s_data_db_node_cs,
          lt_alt_key          TYPE TABLE OF /hec1/phase_guid,
          lt_phase_generated  TYPE /hec1/t_data_phase_ct.



    CLEAR: et_failed_key,
           ev_static_action_failed,
           et_data,
           et_data_link.

*    IF co_message IS NOT BOUND.
*      co_message = /bobf/cl_frw_factory=>get_message( ).
*    ENDIF.

    " **********************************
    " Get none default master node
    " **********************************
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_db_node     ).

    " **********************************
    " Get Phasing
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = VALUE #( FOR db IN lt_db_node
                                                                        ( key = db-root_key ) )
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                                iv_fill_data   = abap_true
                                      IMPORTING et_data        = lt_phase ).

    " I know that all method for BOPF are mass enabled, but this action can only triggered out
    " of the BOPF object from one single BOPF instance, so therefore it should never happen, that
    " in lt_db_node is more then one instance, otherwise it is an error
    IF lines( lt_db_node ) <> 1.
      " Todo error message
      " Error
      RETURN. " >>>>>>
    ELSE.
      " Get the phasing data
      TRY.
          DATA(ls_node_phase) = lt_phase[ hec_node_phase = lt_db_node[ 1 ]-hec_phase_guid ].
          " Get DB node standby/worker
          DATA(ls_db_node) = lt_db_node[ 1 ].
        CATCH cx_sy_itab_line_not_found.
          " Todo error message
      ENDTRY.
    ENDIF.

    " **********************************
    " Get root key
    " **********************************
    io_read->get_root_key( EXPORTING iv_node         = is_ctx-node_key
                                     it_key          = it_key
                           IMPORTING et_target_key   = DATA(lt_root_key) ).

    " The root instance should exist always once
    TRY.
        DATA(lv_root_key) = lt_root_key[ 1 ]-key.
      CATCH cx_sy_itab_line_not_found.
        " ToDo error message
    ENDTRY.

    " **********************************
    " Get master node
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_node-to_def_master_node
                                      IMPORTING et_key_link    = DATA(lt_key_link)
                                                et_target_key  = DATA(lt_key)                                                        ).

    " **********************************
    " Get server performance categories
    " of master node
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = lt_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                                      IMPORTING et_data        = lt_db_serv_perf_cat                                                     ).

    " **********************************
    " Get server storage amount
    " of master node
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                it_key         = VALUE #( FOR wa IN lt_db_serv_perf_cat
                                                                         ( key = wa-key )                )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount
                                      IMPORTING et_data        = lt_db_storage_qty                                                                ).

    " **********************************
    " Get server of master node
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                it_key         = VALUE #( FOR wa IN lt_db_serv_perf_cat
                                                                         ( key = wa-key )                )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_server
                                      IMPORTING et_data        = lt_db_server                                                             ).


    " **********************************
    " Get server storage of master node
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server
                                                it_key         = VALUE #( FOR wa_serv IN lt_db_server
                                                                         ( key = wa_serv-key )                )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server-db_storage
                                      IMPORTING et_data        = lt_db_storage                                                 ).

    " **********************************
    " Get storage backup of master node
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_storage
                                                it_key         = VALUE #( FOR wa_stor IN lt_db_storage
                                                                         ( key = wa_stor-key )                )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_storage-db_storage_backup
                                      IMPORTING et_data        = lt_db_backup                                                          ).


    " Generate phasing and instances to create
    " for app server performance category
    generate_phasing( EXPORTING is_node_phase      = ls_node_phase
                                it_table           = lt_db_serv_perf_cat
                                it_phasing_all     = lt_phase
                      IMPORTING et_phase_generated = lt_phase_generated
                                et_new_instance    = lt_serv_perf_cat
                      CHANGING  co_message         = co_message            ).


    " Create all dependent sub nodes data
    DATA(rt_modification) = create_db_server_pc( EXPORTING iv_root_key         = lv_root_key
                                                           is_db_node          = ls_db_node
                                                           it_db_serv_perf_cat = lt_serv_perf_cat
                                                           it_db_storage_qty   = lt_db_storage_qty
                                                           it_db_server        = lt_db_server
                                                           it_db_storage       = lt_db_storage
                                                           it_db_backup        = lt_db_backup
                                                           it_phasing_all      = lt_phase
                                                           it_phasing          = lt_phase_generated
                                                 CHANGING  co_message          = co_message          ).


    " Update no. of server performance category
    LOOP AT        lt_db_node
    REFERENCE INTO lr_db_node.

      lr_db_node->hec_db_srv_perf_cat_qty = lines( lt_serv_perf_cat ).
      lr_db_node->hec_instance_status     = /hec1/if_config_constants=>gc_instance_status-complete.

      INSERT VALUE #( data        = lr_db_node
                      node        = is_ctx-node_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_db_node->key                   ) INTO TABLE rt_modification.

    ENDLOOP.


    IF co_message IS BOUND.
      DATA(lv_has_error_msg) = co_message->check( iv_consistency_messages = abap_true
                                                  iv_action_messages      = abap_true ).
    ENDIF.

    IF lv_has_error_msg = abap_false   AND
       rt_modification IS NOT INITIAL.

      " Update no. of server performance category
      LOOP AT        lt_db_node
      REFERENCE INTO lr_db_node.

        lr_db_node->hec_db_srv_perf_cat_qty = lines( lt_serv_perf_cat ).
        lr_db_node->hec_instance_status      = /hec1/if_config_constants=>gc_instance_status-complete.

        INSERT VALUE #( data        = lr_db_node
                        node        = is_ctx-node_key
                        change_mode = /bobf/if_frw_c=>sc_modify_update
                        key         = lr_db_node->key                 ) INTO TABLE rt_modification.

      ENDLOOP.

      " Create all sub nodes
      io_modify->do_modify( rt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change)  ).

      /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>sync_config_successfully
                                                     iv_severity = /bobf/cm_frw=>co_severity_success
                                           CHANGING co_message   = co_message                                     ).
    ENDIF.


  ENDMETHOD.


  METHOD /hec1/if_bopf_action_helper~get_backup_class_and_price.

    CLEAR: es_backup_class,
           es_backup_pricing.

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
                                                        et_failed_key    = DATA(lt_failed_key) ).


    " Get backup class data
    IF iv_app_server IS NOT INITIAL.
      SELECT *
        FROM /hec1/i_appservbackupbasic
       WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid AND
             hec_tier_category_value = @iv_tier_category_value
        INTO TABLE @DATA(lt_app_backup_class).

      es_backup_class_lines = lines( lt_app_backup_class ).
    ELSE.
      SELECT *
        FROM /hec1/i_dbservbackupbasic
       WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid AND
             hec_tier_category_value = @iv_tier_category_value
        INTO TABLE @DATA(lt_db_backup_class).

      es_backup_class_lines = lines( lt_db_backup_class ).
    ENDIF.

    " support status 02 als default
    TRY.
        IF iv_backup_class_guid IS INITIAL.
          IF lt_app_backup_class IS NOT INITIAL.
            " Get default backup class data
            es_backup_class = CORRESPONDING #( lt_app_backup_class[ hec_backup_support_stat_value = '02' ] ).
          ELSE.
            es_backup_class = CORRESPONDING #( lt_db_backup_class[ hec_backup_support_stat_value = '02' ] ).
          ENDIF.
        ELSE.
          " Get selected backup class
          IF lt_app_backup_class IS NOT INITIAL.
            es_backup_class = CORRESPONDING #( lt_app_backup_class[ hec_backup_class_guid = iv_backup_class_guid ] ).
          ELSE.
            es_backup_class = CORRESPONDING #( lt_db_backup_class[ hec_backup_class_guid = iv_backup_class_guid ] ).
          ENDIF.
        ENDIF.

        IF es_backup_class-hec_backup_class_guid IS NOT INITIAL.
          " Get data center GUID
          DATA(lv_datacenter_guid) = lt_datacenter[ hec_node_datacenter = iv_tier_datacenter_guid ]-hec_datacenter_guid.

          " Get backup class pricing
          SELECT SINGLE hec_cb_pricing_lb_guid
            FROM /hec1/i_serverbackuplbbasic
           WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid            AND
                 hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid   AND
                 hec_sec_datacenter_guid = @lv_datacenter_guid                    AND
                 hec_backup_class_guid   = @es_backup_class-hec_backup_class_guid
            INTO @DATA(lv_lb_guid).


          IF lv_lb_guid IS NOT INITIAL.
            SELECT SINGLE * FROM /hec1/c_cbp_lb "#EC CI_ALL_FIELDS_NEEDED
              WHERE hec_price_lb = @lv_lb_guid
               INTO CORRESPONDING FIELDS OF @es_backup_pricing.

          ENDIF.
        ENDIF. " IF ls_fdt_backup_class-hec_backup_class_guid IS NOT INITIAL.
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.


  ENDMETHOD.


  METHOD create_app_server.

    DATA: lr_app_server           TYPE REF TO /hec1/s_data_app_serv_cs,
          lt_storage_qty_filtered TYPE /hec1/t_data_app_storageqty_ct,
          lt_storage_qty          TYPE /hec1/t_data_app_storageqty_ct,
          lt_storage_filtered     TYPE /hec1/t_data_app_storage_ct,
          lt_storage              TYPE /hec1/t_data_app_storage_ct.


    IF co_message IS NOT BOUND.
      co_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    " Create app server instance
    LOOP AT it_app_server ASSIGNING FIELD-SYMBOL(<fs_app_server>).
      ASSIGN it_phasing[ sy-tabix ] TO FIELD-SYMBOL(<fs_phase>).
      IF <fs_phase> IS ASSIGNED.

        " Filter app storage table for
        " creating the new instances
        lt_storage_filtered = VALUE #( FOR wa IN it_app_storage
                                       WHERE ( hec_node_app_serv_inst = <fs_app_server>-hec_node_app_serv_inst AND
                                               hec_node_app_node      = <fs_app_server>-hec_node_app_node      AND
                                               hec_node_app_serv_pc   = <fs_app_server>-hec_node_app_serv_pc   AND
                                               hec_node_app_server    = <fs_app_server>-hec_node_app_server        )
                                       ( wa )                                                                        ).

        " Filter app storage amount table for
        " creating the new instances
        lt_storage_qty_filtered = VALUE #( FOR wa_qty IN it_app_storage_qty
                                           WHERE ( hec_node_app_serv_inst = <fs_app_server>-hec_node_app_serv_inst AND
                                                   hec_node_app_node      = <fs_app_server>-hec_node_app_node      AND
                                                   hec_node_app_serv_pc   = <fs_app_server>-hec_node_app_serv_pc       )
                                            ( wa_qty )                                                                         ).

        " Insert new phase reference
        INSERT VALUE #( data        = NEW /hec1/s_data_phase_cs( <fs_phase> )
                        node        = /hec1/if_configuration_c=>sc_node-phase
                        source_node = /hec1/if_configuration_c=>sc_node-root
                        association = /hec1/if_configuration_c=>sc_association-root-phase
                        source_key  = iv_root_key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = /bopf/cl_frw_factory=>get_new_key( )                 ) INTO TABLE ct_modification.


        " Create und fill App server reference
        lr_app_server = NEW /hec1/s_data_app_serv_cs( BASE CORRESPONDING #( <fs_app_server> EXCEPT key                      hec_app_clust_node_type_value
                                                                                                   parent_key               hec_app_node_default
                                                                                                   hec_node_app_node        crea_date_time
                                                                                                   hec_node_app_serv_pc     crea_uname
                                                                                                   hec_node_app_server      lchg_date_time
                                                                                                   hec_phase_guid           lchg_uname                      )
                                                      key                           = /bopf/cl_frw_factory=>get_new_key( )
                                                      parent_key                    = is_app_serv_perf_cat-key
                                                      hec_node_app_node             = is_app_serv_perf_cat-hec_node_app_node
                                                      hec_node_app_serv_pc          = is_app_serv_perf_cat-hec_node_app_serv_pc
                                                      hec_node_app_server           = /rbp/cl_general_utilities=>get_new_guid22( )
                                                      hec_phase_guid                = <fs_phase>-hec_node_phase
                                                      crea_uname                    = sy-uname
                                                      hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-standby                  ).


        GET TIME STAMP FIELD lr_app_server->crea_date_time.

        " Insert App server reference
        INSERT VALUE #( data        = lr_app_server
                        node        = /hec1/if_configuration_c=>sc_node-app_server
                        source_node = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                        association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_server
                        source_key  = is_app_serv_perf_cat-key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = lr_app_server->key                                                          ) INTO TABLE ct_modification.


        " Generate phasing and instances to create
        " for app storage
        generate_phasing( EXPORTING is_node_phase      = CORRESPONDING #( <fs_phase> )
                                    it_table           = lt_storage_qty_filtered
                                    it_phasing_all     = it_phasing_all
                          IMPORTING et_phase_generated = DATA(lt_phase_generated)
                                    et_new_instance    = lt_storage_qty
                          CHANGING  co_message         = co_message                    ).


        IF lines( lt_storage_filtered ) = 1.
          lt_storage = lt_storage_filtered.
        ELSE.
          lt_storage = VALUE #( FOR wa_qty IN lt_storage_qty
                                FOR wa IN lt_storage_filtered
                                WHERE ( hec_storage_qty_ref_guid = wa_qty-hec_node_app_storage_qty )
                                ( wa )                                                              ).
        ENDIF.

        " Create App storage reference
        create_app_storage( EXPORTING iv_root_key     = iv_root_key
                                      is_app_server   = lr_app_server->*
                                      it_app_storage  = lt_storage
                                      it_app_backup   = it_app_backup
                                      it_phasing_all  = it_phasing_all
                                      it_phasing      = lt_phase_generated
                            CHANGING  co_message      = co_message
                                      ct_modification = ct_modification    ).

      ENDIF. " IF <fs_phase> IS ASSIGNED.

      UNASSIGN <fs_phase>.
      CLEAR: lt_phase_generated,
             lt_storage_qty,
             lt_storage_qty_filtered,
             lt_storage,
             lt_storage_filtered,
             lr_app_server.
    ENDLOOP.


  ENDMETHOD.


  METHOD create_app_server_pc.

    DATA: lr_app_serv_perf_cat    TYPE REF TO /hec1/s_data_app_serv_pc_cs,
          lt_storage_qty_filtered TYPE /hec1/t_data_app_storageqty_ct,
          lt_storage_qty          TYPE /hec1/t_data_app_storageqty_ct,
          lt_server_filtered      TYPE /hec1/t_data_app_serv_ct,
          lt_server               TYPE /hec1/t_data_app_serv_ct,
          lt_range                TYPE RANGE OF string.


    IF co_message IS NOT BOUND.
      co_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    DATA(lv_entry_no) = lines( it_app_serv_perf_cat ).
    DATA(lv_counter)  = 1.

    " Create app server performance category instance
    LOOP AT it_app_serv_perf_cat ASSIGNING FIELD-SYMBOL(<fs_app_serv_perf>).
      ASSIGN it_phasing[ sy-tabix ] TO FIELD-SYMBOL(<fs_phase>).
      IF <fs_phase> IS ASSIGNED.

        " Filter app storage amount table for
        " creating the new instances
        lt_storage_qty_filtered = VALUE #( FOR wa IN it_app_storage_qty
                                           WHERE ( hec_node_app_serv_inst = <fs_app_serv_perf>-hec_node_app_serv_inst AND
                                                   hec_node_app_node      = <fs_app_serv_perf>-hec_node_app_node      AND
                                                   hec_node_app_serv_pc   = <fs_app_serv_perf>-hec_node_app_serv_pc       )
                                            ( wa )                                                                         ).


        " Filter app server table for
        " creating the new instances
        lt_server_filtered = VALUE #( FOR wa_serv IN it_app_server
                                      WHERE ( hec_node_app_serv_inst = <fs_app_serv_perf>-hec_node_app_serv_inst AND
                                              hec_node_app_node      = <fs_app_serv_perf>-hec_node_app_node      AND
                                              hec_node_app_serv_pc   = <fs_app_serv_perf>-hec_node_app_serv_pc       )
                                       ( wa_serv )                                                                         ).


        " Insert new phase reference
        INSERT VALUE #( data        = NEW /hec1/s_data_phase_cs( <fs_phase> )
                        node        = /hec1/if_configuration_c=>sc_node-phase
                        source_node = /hec1/if_configuration_c=>sc_node-root
                        association = /hec1/if_configuration_c=>sc_association-root-phase
                        source_key  = iv_root_key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = /bopf/cl_frw_factory=>get_new_key( )                 ) INTO TABLE rt_modification.


        " Create und fill App server performance category reference
        lr_app_serv_perf_cat = NEW /hec1/s_data_app_serv_pc_cs( BASE CORRESPONDING #( <fs_app_serv_perf> EXCEPT key                     hec_has_successor       hec_app_clust_node_type_value
                                                                                                                parent_key              hec_successor_guid      hec_app_node_default
                                                                                                                                                                hec_apst_clustty_clustnty_guid
                                                                                                                hec_node_app_node       hec_predecessor_guid    price
                                                                                                                hec_node_app_serv_pc    hec_successor_descr     crea_date_time
                                                                                                                hec_phase_guid          hec_predecessor_descr   crea_uname
                                                                                                                                                                lchg_date_time
                                                                                                                                                                lchg_uname                     )
                                                                key                            = /bopf/cl_frw_factory=>get_new_key( )
                                                                parent_key                     = is_app_node-key
                                                                hec_node_app_node              = is_app_node-hec_node_app_node
                                                                hec_node_app_serv_pc           = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                hec_phase_guid                 = <fs_phase>-hec_node_phase
                                                                crea_uname                     = sy-uname
                                                                hec_app_clust_node_type_value  = /hec1/if_config_constants=>gc_app_clust_node_type-standby
                                                                hec_apst_clustty_clustnty_guid = is_app_node-hec_apst_clustty_clustnty_guid                                                       ).

        " ---------------------------
        " Get pricing
        " ---------------------------
        IF lr_app_serv_perf_cat->hec_effort_required = abap_true.
          " Get effort time based legoblock GUID
          SELECT hec_ram_condition_op,
                 hec_ram_condition,
                 hec_timebased_effort_bb_guid
            FROM /hec1/i_appservnodetbbbbasic
           WHERE hec_apm_guid                   = @lr_app_serv_perf_cat->hec_apm_guid                   AND
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
            DATA(ls_price) = /hec1/cl_config_helper=>do_price_validation( iv_node_key          = /hec1/if_configuration_c=>sc_node-root
                                                                          it_key               = VALUE #( ( key = iv_root_key ) )
                                                                          io_read              = io_read
                                                                          iv_effort_bb_guid    = lv_effort_bb_guid
                                                                          iv_tier_is_dr_node   = lr_app_serv_perf_cat->hec_tier_is_dr_node
                                                                          iv_dr_operating_mode = lr_app_serv_perf_cat->hec_dr_oper_mode_value ).

            lr_app_serv_perf_cat->price = CORRESPONDING #( ls_price ).
          ENDIF.
        ENDIF. " IF lr_app_serv_perf_cat->hec_effort_required = abap_true.


        " Set successor/predecessor
        IF lv_counter = 1.
          IF lv_entry_no > 1.
            DATA(lv_predecessor)                    = lr_app_serv_perf_cat->key.
            lr_app_serv_perf_cat->hec_has_successor = abap_true.
          ENDIF.
        ELSE.
          IF lv_counter < lv_entry_no AND
             sy-tabix > 1.
            lr_app_serv_perf_cat->hec_has_successor    = abap_true.
            lr_app_serv_perf_cat->hec_predecessor_guid = lv_predecessor.
            lv_predecessor                             = lr_app_serv_perf_cat->key.
          ELSEIF lv_counter = lv_entry_no.
            lr_app_serv_perf_cat->hec_has_successor    = abap_false.
            lr_app_serv_perf_cat->hec_predecessor_guid = lv_predecessor.
          ENDIF.
        ENDIF. " IF lv_counter = 1.

        GET TIME STAMP FIELD lr_app_serv_perf_cat->crea_date_time.

        " Insert App server performance category reference
        INSERT VALUE #( data        = lr_app_serv_perf_cat
                        node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                        source_node = /hec1/if_configuration_c=>sc_node-app_node
                        association = /hec1/if_configuration_c=>sc_association-app_node-app_server_perform_cat
                        source_key  = is_app_node-key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = lr_app_serv_perf_cat->key                                                 ) INTO TABLE rt_modification.


        " Generate phasing and instances to create
        " for app storage amount
        generate_phasing( EXPORTING is_node_phase      = CORRESPONDING #( <fs_phase> )
                                    it_table           = lt_storage_qty_filtered
                                    it_phasing_all     = it_phasing_all
                          IMPORTING et_phase_generated = DATA(lt_phase_generated)
                                    et_new_instance    = lt_storage_qty
                          CHANGING  co_message         = co_message ).


        " Create App storage amount reference
        create_app_storage_amount( EXPORTING iv_root_key          = iv_root_key
                                             is_app_serv_perf_cat = lr_app_serv_perf_cat->*
                                             it_app_storage_qty   = lt_storage_qty
                                             it_phasing_all       = it_phasing_all
                                             it_phasing           = lt_phase_generated
                                   CHANGING  co_message           = co_message
                                             ct_modification      = rt_modification ).


        " Generate phasing and instances to create
        " for app server
        CLEAR lt_phase_generated.
        generate_phasing( EXPORTING is_node_phase      = CORRESPONDING #( <fs_phase> )
                                    it_table           = lt_server_filtered
                                    it_phasing_all     = it_phasing_all
                          IMPORTING et_phase_generated = lt_phase_generated
                                    et_new_instance    = lt_server
                          CHANGING  co_message         = co_message ).


        " Create App server reference
        create_app_server( EXPORTING iv_root_key          = iv_root_key
                                     is_app_serv_perf_cat = lr_app_serv_perf_cat->*
                                     it_app_storage_qty   = it_app_storage_qty
                                     it_app_server        = lt_server
                                     it_app_storage       = it_app_storage
                                     it_app_backup        = it_app_backup
                                     it_phasing_all       = it_phasing_all
                                     it_phasing           = lt_phase_generated
                           CHANGING  co_message           = co_message
                                     ct_modification      = rt_modification ).

      ENDIF. " IF <fs_phase> IS ASSIGNED.

      ADD 1 TO lv_counter.

      UNASSIGN <fs_phase>.
      CLEAR: lt_phase_generated,
             lt_storage_qty,
             lt_storage_qty_filtered,
             lt_server,
             lt_server_filtered,
             lr_app_serv_perf_cat.
    ENDLOOP.


  ENDMETHOD.


  METHOD create_app_storage.

    DATA: lr_app_storage     TYPE REF TO /hec1/s_data_app_storage_cs,
          lt_backup_filtered TYPE /hec1/t_data_app_backup_ct,
          lt_backup          TYPE /hec1/t_data_app_backup_ct.


    IF co_message IS NOT BOUND.
      co_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    DATA(lv_entry_no) = lines( it_app_storage ).
    DATA(lv_counter)  = 1.

    " Create app storage backup instance
    LOOP AT it_app_storage ASSIGNING FIELD-SYMBOL(<fs_app_storage>).
      ASSIGN it_phasing[ sy-tabix ] TO FIELD-SYMBOL(<fs_phase>).
      IF <fs_phase> IS ASSIGNED.


        " Filter app storage backup table for
        " creating the new instances
        lt_backup_filtered = VALUE #( FOR wa IN it_app_backup
                                      WHERE ( hec_node_app_serv_inst = <fs_app_storage>-hec_node_app_serv_inst AND
                                              hec_node_app_node      = <fs_app_storage>-hec_node_app_node      AND
                                              hec_node_app_serv_pc   = <fs_app_storage>-hec_node_app_serv_pc   AND
                                              hec_node_app_server    = <fs_app_storage>-hec_node_app_server    AND
                                              hec_node_app_storage   = <fs_app_storage>-hec_node_app_storage       )
                                       ( wa )                                                                        ).


        " Insert new phase reference
        INSERT VALUE #( data        = NEW /hec1/s_data_phase_cs( <fs_phase> )
                        node        = /hec1/if_configuration_c=>sc_node-phase
                        source_node = /hec1/if_configuration_c=>sc_node-root
                        association = /hec1/if_configuration_c=>sc_association-root-phase
                        source_key  = iv_root_key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = /bopf/cl_frw_factory=>get_new_key( )                ) INTO TABLE ct_modification.


        " Create und fill App storage reference
        lr_app_storage = NEW /hec1/s_data_app_storage_cs( BASE CORRESPONDING #( <fs_app_storage> EXCEPT key                     hec_has_successor       hec_app_clust_node_type_value
                                                                                                        parent_key              hec_successor_guid      hec_app_node_default
                                                                                                        hec_node_app_node       hec_predecessor_guid    crea_date_time
                                                                                                        hec_node_app_serv_pc    hec_successor_descr     crea_uname
                                                                                                        hec_node_app_server     hec_predecessor_descr   lchg_date_time
                                                                                                        hec_node_app_storage                            lchg_uname                     )
                                                          key                           = /bopf/cl_frw_factory=>get_new_key( )
                                                          parent_key                    = is_app_server-key
                                                          hec_node_app_node             = is_app_server-hec_node_app_node
                                                          hec_node_app_serv_pc          = is_app_server-hec_node_app_serv_pc
                                                          hec_node_app_server           = is_app_server-hec_node_app_server
                                                          hec_node_app_storage          = /rbp/cl_general_utilities=>get_new_guid22( )
                                                          hec_phase_guid                = <fs_phase>-hec_node_phase
                                                          hec_backup_qty                = 0
                                                          crea_uname                    = sy-uname
                                                          hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-standby                                       ).


        " Set successor/predecessor
        IF lv_counter = 1.
          IF lv_entry_no > 1.
            DATA(lv_predecessor)              = lr_app_storage->key.
            lr_app_storage->hec_has_successor = abap_true.
          ENDIF.
        ELSE.
          IF lv_counter < lv_entry_no AND
             sy-tabix > 1.
            lr_app_storage->hec_has_successor    = abap_true.
            lr_app_storage->hec_predecessor_guid = lv_predecessor.
            lv_predecessor                       = lr_app_storage->key.
          ELSEIF lv_counter = lv_entry_no.
            lr_app_storage->hec_has_successor    = abap_false.
            lr_app_storage->hec_predecessor_guid = lv_predecessor.
          ENDIF.
        ENDIF. " IF lv_counter = 1.

        GET TIME STAMP FIELD lr_app_storage->crea_date_time.

        " Insert App storage reference
        INSERT VALUE #( data        = lr_app_storage
                        node        = /hec1/if_configuration_c=>sc_node-app_storage
                        source_node = /hec1/if_configuration_c=>sc_node-app_server
                        association = /hec1/if_configuration_c=>sc_association-app_server-app_storage
                        source_key  = is_app_server-key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = lr_app_storage->key                                             ) INTO TABLE ct_modification.


*        " Generate phasing and instances to create
*        " for app storage backup
*        generate_phasing( EXPORTING is_node_phase      = CORRESPONDING #( <fs_phase> )
*                                    it_table           = lt_backup_filtered
*                                    it_phasing_all     = it_phasing_all
*                          IMPORTING et_phase_generated = DATA(lt_phase_generated)
*                                    et_new_instance    = lt_backup
*                          CHANGING  co_message         = co_message                    ).


*        " Create App storage backup reference
*        create_app_storage_backup( EXPORTING iv_root_key     = iv_root_key
*                                             is_app_storage  = lr_app_storage->*
*                                             it_app_backup   = lt_backup
*                                             it_phasing_all  = it_phasing_all
*                                             it_phasing      = lt_phase_generated
*                                   CHANGING  co_message      = co_message
*                                             ct_modification = ct_modification     ).

      ENDIF. " IF <fs_phase> IS ASSIGNED.

      ADD 1 TO lv_counter.

      UNASSIGN <fs_phase>.
      CLEAR: lt_backup,
             lt_backup_filtered,
             lr_app_storage.
    ENDLOOP.


  ENDMETHOD.


  METHOD create_app_storage_amount.

    DATA: lr_app_storage_qty TYPE REF TO /hec1/s_data_app_storageqty_cs.


    IF co_message IS NOT BOUND.
      co_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    DATA(lv_entry_no) = lines( it_app_storage_qty ).
    DATA(lv_counter)  = 1.

    " Create app storage amount instance
    LOOP AT it_app_storage_qty ASSIGNING FIELD-SYMBOL(<fs_app_storage_qty>).
      ASSIGN it_phasing[ sy-tabix ] TO FIELD-SYMBOL(<fs_phase>).
      IF <fs_phase> IS ASSIGNED.

        " Insert new phase reference
        INSERT VALUE #( data        = NEW /hec1/s_data_phase_cs( <fs_phase> )
                        node        = /hec1/if_configuration_c=>sc_node-phase
                        source_node = /hec1/if_configuration_c=>sc_node-root
                        association = /hec1/if_configuration_c=>sc_association-root-phase
                        source_key  = iv_root_key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = /bopf/cl_frw_factory=>get_new_key( )                ) INTO TABLE ct_modification.


        " Create und fill App storage amount reference
        lr_app_storage_qty = NEW /hec1/s_data_app_storageqty_cs( BASE CORRESPONDING #( <fs_app_storage_qty> EXCEPT key                        hec_has_successor       hec_app_clust_node_type_value
                                                                                                                   parent_key                 hec_successor_guid      hec_app_node_default
                                                                                                                   hec_node_app_node          hec_predecessor_guid    crea_date_time
                                                                                                                   hec_node_app_serv_pc       hec_successor_descr     crea_uname
                                                                                                                   hec_node_app_storage_qty   hec_predecessor_descr   lchg_date_time
                                                                                                                                                                      lchg_uname                    )
                                                                 key                           = /bopf/cl_frw_factory=>get_new_key( )
                                                                 parent_key                    = is_app_serv_perf_cat-key
                                                                 hec_node_app_node             = is_app_serv_perf_cat-hec_node_app_node
                                                                 hec_node_app_serv_pc          = is_app_serv_perf_cat-hec_node_app_serv_pc
                                                                 hec_node_app_storage_qty      = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                 hec_phase_guid                = <fs_phase>-hec_node_phase
                                                                 crea_uname                    = sy-uname
                                                                 hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-standby                                            ).


        " Set successor/predecessor
        IF lv_counter = 1.
          IF lv_entry_no > 1.
            DATA(lv_predecessor)                  = lr_app_storage_qty->key.
            lr_app_storage_qty->hec_has_successor = abap_true.
          ENDIF.
        ELSE.
          IF lv_counter < lv_entry_no AND
             sy-tabix > 1.
            lr_app_storage_qty->hec_has_successor    = abap_true.
            lr_app_storage_qty->hec_predecessor_guid = lv_predecessor.
            lv_predecessor                           = lr_app_storage_qty->key.
          ELSEIF lv_counter = lv_entry_no.
            lr_app_storage_qty->hec_has_successor    = abap_false.
            lr_app_storage_qty->hec_predecessor_guid = lv_predecessor.
          ENDIF.
        ENDIF. " IF lv_counter = 1.

        GET TIME STAMP FIELD lr_app_storage_qty->crea_date_time.


        " Insert App storage amount reference
        INSERT VALUE #( data        = lr_app_storage_qty
                        node        = /hec1/if_configuration_c=>sc_node-app_storage_amount
                        source_node = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                        association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_storage_amount
                        source_key  = is_app_serv_perf_cat-key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = lr_app_storage_qty->key                                                            ) INTO TABLE ct_modification.

      ENDIF. " IF <fs_phase> IS ASSIGNED.

      ADD 1 TO lv_counter.

      UNASSIGN <fs_phase>.
      CLEAR lr_app_storage_qty.
    ENDLOOP.


  ENDMETHOD.


  METHOD create_app_storage_backup.

    DATA: lr_app_backup TYPE REF TO /hec1/s_data_app_backup_cs.



    IF co_message IS NOT BOUND.
      co_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    DATA(lv_entry_no) = lines( it_app_backup ).
    DATA(lv_counter)  = 1.

    " Create app storage backup instance
    LOOP AT it_app_backup ASSIGNING FIELD-SYMBOL(<fs_app_backup>).
      ASSIGN it_phasing[ sy-tabix ] TO FIELD-SYMBOL(<fs_phase>).
      IF <fs_phase> IS ASSIGNED.

        " Insert new phase reference
        INSERT VALUE #( data        = NEW /hec1/s_data_phase_cs( <fs_phase> )
                        node        = /hec1/if_configuration_c=>sc_node-phase
                        source_node = /hec1/if_configuration_c=>sc_node-root
                        association = /hec1/if_configuration_c=>sc_association-root-phase
                        source_key  = iv_root_key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = /bopf/cl_frw_factory=>get_new_key( )                ) INTO TABLE ct_modification.


        " Create und fill App storage backup reference
        lr_app_backup = NEW /hec1/s_data_app_backup_cs( BASE CORRESPONDING #( <fs_app_backup> EXCEPT key                     hec_has_successor       hec_app_clust_node_type_value
                                                                                                     parent_key              hec_successor_guid      hec_app_node_default
                                                                                                     hec_node_app_node       hec_predecessor_guid    crea_date_time
                                                                                                     hec_node_app_serv_pc    hec_successor_descr     crea_uname
                                                                                                     hec_node_app_server     hec_predecessor_descr   lchg_date_time
                                                                                                     hec_node_app_storage                            lchg_uname
                                                                                                     hec_node_app_backup
                                                                                                     hec_phase_guid                                                                 )
                                                        key                           = /bopf/cl_frw_factory=>get_new_key( )
                                                        parent_key                    = is_app_storage-key
                                                        hec_node_app_node             = is_app_storage-hec_node_app_node
                                                        hec_node_app_serv_pc          = is_app_storage-hec_node_app_serv_pc
                                                        hec_node_app_server           = is_app_storage-hec_node_app_server
                                                        hec_node_app_storage          = is_app_storage-hec_node_app_storage
                                                        hec_node_app_backup           = /rbp/cl_general_utilities=>get_new_guid22( )
                                                        hec_phase_guid                = <fs_phase>-hec_node_phase
                                                        crea_uname                    = sy-uname
                                                        hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-standby ).


        " Set successor/predecessor
        IF lv_counter = 1.
          IF lv_entry_no > 1.
            DATA(lv_predecessor)             = lr_app_backup->key.
            lr_app_backup->hec_has_successor = abap_true.
          ENDIF.
        ELSE.
          IF lv_counter < lv_entry_no AND
             sy-tabix   > 1.
            lr_app_backup->hec_has_successor    = abap_true.
            lr_app_backup->hec_predecessor_guid = lv_predecessor.
            lv_predecessor                      = lr_app_backup->key.
          ELSEIF lv_counter = lv_entry_no.
            lr_app_backup->hec_has_successor    = abap_false.
            lr_app_backup->hec_predecessor_guid = lv_predecessor.
          ENDIF.
        ENDIF. " IF lv_counter = 1.

        GET TIME STAMP FIELD lr_app_backup->crea_date_time.


        " Insert App storage backup reference
        INSERT VALUE #( data        = lr_app_backup
                        node        = /hec1/if_configuration_c=>sc_node-app_storage_backup
                        source_node = /hec1/if_configuration_c=>sc_node-app_storage
                        association = /hec1/if_configuration_c=>sc_association-app_storage-app_storage_backup
                        source_key  = is_app_storage-key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = lr_app_backup->key                                                      ) INTO TABLE ct_modification.

      ENDIF. " IF <fs_phase> IS ASSIGNED.

      ADD 1 TO lv_counter.

      UNASSIGN <fs_phase>.
      CLEAR lr_app_backup.
    ENDLOOP.


  ENDMETHOD.


  METHOD create_db_server.

    DATA: lr_db_server            TYPE REF TO /hec1/s_data_db_serv_cs,
          lt_storage_filtered     TYPE /hec1/t_data_db_storage_ct,
          lt_storage_qty_filtered TYPE /hec1/t_data_db_storage_qty_ct,
          lt_storage              TYPE /hec1/t_data_db_storage_ct,
          lt_storage_qty          TYPE /hec1/t_data_db_storage_qty_ct.


    IF co_message IS NOT BOUND.
      co_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    " Create DB server instance
    LOOP AT it_db_server ASSIGNING FIELD-SYMBOL(<fs_db_server>).
      ASSIGN it_phasing[ sy-tabix ] TO FIELD-SYMBOL(<fs_phase>).
      IF <fs_phase> IS ASSIGNED.

        " Filter DB storage table for
        " creating the new instances
        lt_storage_filtered = VALUE #( FOR wa IN it_db_storage
                                       WHERE ( hec_node_db_serv_inst = <fs_db_server>-hec_node_db_serv_inst AND
                                               hec_node_db_inst      = <fs_db_server>-hec_node_db_inst      AND
                                               hec_node_db_node      = <fs_db_server>-hec_node_db_node      AND
                                               hec_node_db_serv_pc   = <fs_db_server>-hec_node_db_serv_pc   AND
                                               hec_node_db_server    = <fs_db_server>-hec_node_db_server        )
                                       ( wa )                                                                        ).

        lt_storage_qty_filtered = VALUE #( FOR wa_qty IN it_db_storage_qty
                                       WHERE ( hec_node_db_serv_inst = <fs_db_server>-hec_node_db_serv_inst AND
                                               hec_node_db_inst      = <fs_db_server>-hec_node_db_inst      AND
                                               hec_node_db_node      = <fs_db_server>-hec_node_db_node      AND
                                               hec_node_db_serv_pc   = <fs_db_server>-hec_node_db_serv_pc       )
                                       ( wa_qty )                                                                     ).


        " Insert new phase reference
        INSERT VALUE #( data        = NEW /hec1/s_data_phase_cs( <fs_phase> )
                        node        = /hec1/if_configuration_c=>sc_node-phase
                        source_node = /hec1/if_configuration_c=>sc_node-root
                        association = /hec1/if_configuration_c=>sc_association-root-phase
                        source_key  = iv_root_key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = /bopf/cl_frw_factory=>get_new_key( )                ) INTO TABLE ct_modification.


        " Create und fill DB server reference
        lr_db_server = NEW /hec1/s_data_db_serv_cs( BASE CORRESPONDING #( <fs_db_server> EXCEPT key                       hec_db_clust_node_type_value
                                                                                                parent_key                hec_db_node_default
                                                                                                hec_node_db_node          crea_date_time
                                                                                                hec_node_db_serv_pc       crea_uname
                                                                                                hec_node_db_server        lchg_date_time
                                                                                                hec_phase_guid            lchg_uname                    )
                                                                key                          = /bopf/cl_frw_factory=>get_new_key( )
                                                                parent_key                   = is_db_serv_perf_cat-key
                                                                hec_node_db_node             = is_db_serv_perf_cat-hec_node_db_node
                                                                hec_node_db_serv_pc          = is_db_serv_perf_cat-hec_node_db_serv_pc
                                                                hec_node_db_server           = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                hec_phase_guid               = <fs_phase>-hec_node_phase
                                                                hec_db_clust_node_type_value = is_db_serv_perf_cat-hec_db_clust_node_type_value
                                                                crea_uname                   = sy-uname                                                     ).


        GET TIME STAMP FIELD lr_db_server->crea_date_time.


        " Insert DB server reference
        INSERT VALUE #( data        = lr_db_server
                        node        = /hec1/if_configuration_c=>sc_node-db_server
                        source_node = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                        association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_server
                        source_key  = is_db_serv_perf_cat-key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = lr_db_server->key                                                        ) INTO TABLE ct_modification.

        " Generate phasing and instances to create
        " for DB storage
        generate_phasing( EXPORTING is_node_phase      = CORRESPONDING #( <fs_phase> )
                                    it_table           = lt_storage_qty_filtered
                                    it_phasing_all     = it_phasing_all
                          IMPORTING et_phase_generated = DATA(lt_phase_generated)
                                    et_new_instance    = lt_storage_qty
                          CHANGING  co_message         = co_message                    ).


        IF lines( lt_storage_filtered ) = 1.
          lt_storage = lt_storage_filtered.
        ELSE.
          lt_storage = VALUE #( FOR wa_qty IN lt_storage_qty
                                FOR wa IN lt_storage_filtered
                                WHERE ( hec_storage_qty_ref_guid = wa_qty-hec_node_db_storage_qty )
                                ( wa )                                                              ).
        ENDIF.

        " Create DB storage reference
        create_db_storage( EXPORTING iv_root_key     = iv_root_key
                                     is_db_server    = lr_db_server->*
                                     it_db_storage   = lt_storage
                                     it_db_backup    = it_db_backup
                                     it_phasing_all  = it_phasing_all
                                     it_phasing      = lt_phase_generated
                           CHANGING  co_message      = co_message
                                     ct_modification = ct_modification    ).

      ENDIF. " IF <fs_phase> IS ASSIGNED.

      UNASSIGN <fs_phase>.
      CLEAR: lt_phase_generated,
             lt_storage_qty,
             lt_storage_qty_filtered,
             lt_storage,
             lt_storage_filtered,
             lr_db_server.
    ENDLOOP.


  ENDMETHOD.


  METHOD create_db_server_pc.

    DATA: lr_db_serv_perf_cat     TYPE REF TO /hec1/s_data_db_serv_pc_cs,
          lt_storage_qty_filtered TYPE /hec1/t_data_db_storage_qty_ct,
          lt_storage_qty          TYPE /hec1/t_data_db_storage_qty_ct,
          lt_server_filtered      TYPE /hec1/t_data_db_serv_ct,
          lt_server               TYPE /hec1/t_data_db_serv_ct.


    IF co_message IS NOT BOUND.
      co_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    DATA(lv_entry_no) = lines( it_db_serv_perf_cat ).
    DATA(lv_counter)  = 1.

    " Create DB server performance category instance
    LOOP AT it_db_serv_perf_cat ASSIGNING FIELD-SYMBOL(<fs_db_serv_perf>).
      ASSIGN it_phasing[ sy-tabix ] TO FIELD-SYMBOL(<fs_phase>).
      IF <fs_phase> IS ASSIGNED.

        " Filter DB storage amount table for
        " creating the new instances
        lt_storage_qty_filtered = VALUE #( FOR wa IN it_db_storage_qty
                                           WHERE ( hec_node_db_serv_inst = <fs_db_serv_perf>-hec_node_db_serv_inst AND
                                                   hec_node_db_inst      = <fs_db_serv_perf>-hec_node_db_inst      AND
                                                   hec_node_db_node      = <fs_db_serv_perf>-hec_node_db_node      AND
                                                   hec_node_db_serv_pc   = <fs_db_serv_perf>-hec_node_db_serv_pc       )
                                            ( wa )                                                                         ).


        " Filter DB server table for
        " creating the new instances
        lt_server_filtered = VALUE #( FOR wa_serv IN it_db_server
                                      WHERE ( hec_node_db_serv_inst = <fs_db_serv_perf>-hec_node_db_serv_inst AND
                                              hec_node_db_node      = <fs_db_serv_perf>-hec_node_db_node      AND
                                              hec_node_db_serv_pc   = <fs_db_serv_perf>-hec_node_db_serv_pc       )
                                       ( wa_serv )                                                                         ).



        " Insert new phase reference
        INSERT VALUE #( data        = NEW /hec1/s_data_phase_cs( <fs_phase> )
                        node        = /hec1/if_configuration_c=>sc_node-phase
                        source_node = /hec1/if_configuration_c=>sc_node-root
                        association = /hec1/if_configuration_c=>sc_association-root-phase
                        source_key  = iv_root_key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = /bopf/cl_frw_factory=>get_new_key( )                ) INTO TABLE rt_modification.


        " Create und fill DB server performance category reference
        lr_db_serv_perf_cat = NEW /hec1/s_data_db_serv_pc_cs( BASE CORRESPONDING #( <fs_db_serv_perf>  EXCEPT key                     hec_has_successor       hec_db_clust_node_type_value
                                                                                                              parent_key              hec_successor_guid      hec_db_node_default
                                                                                                              hec_node_db_node        hec_predecessor_guid    crea_date_time
                                                                                                              hec_node_db_serv_pc     hec_successor_descr     crea_uname
                                                                                                              hec_phase_guid          hec_predecessor_descr   lchg_date_time
                                                                                                                                                              lchg_uname                     )
                                                              key                          = /bopf/cl_frw_factory=>get_new_key( )
                                                              parent_key                   = is_db_node-key
                                                              hec_node_db_node             = is_db_node-hec_node_db_node
                                                              hec_node_db_serv_pc          = /rbp/cl_general_utilities=>get_new_guid22( )
                                                              hec_phase_guid               = <fs_phase>-hec_node_phase
                                                              hec_db_clust_node_type_value = is_db_node-hec_db_clust_node_type_value
                                                              crea_uname                   = sy-uname                                                                                           ).

        " Set successor/predecessor
        IF lv_counter = 1.
          IF lv_entry_no > 1.
            DATA(lv_predecessor)                   = lr_db_serv_perf_cat->key.
            lr_db_serv_perf_cat->hec_has_successor = abap_true.
          ENDIF.
        ELSE.
          IF lv_counter < lv_entry_no AND
             sy-tabix > 1.
            lr_db_serv_perf_cat->hec_has_successor    = abap_true.
            lr_db_serv_perf_cat->hec_predecessor_guid = lv_predecessor.
            lv_predecessor                            = lr_db_serv_perf_cat->key.
          ELSEIF lv_counter = lv_entry_no.
            lr_db_serv_perf_cat->hec_has_successor    = abap_false.
            lr_db_serv_perf_cat->hec_predecessor_guid = lv_predecessor.
          ENDIF.
        ENDIF. " IF lv_counter = 1.


        GET TIME STAMP FIELD lr_db_serv_perf_cat->crea_date_time.


        " Insert DB server performance category reference
        INSERT VALUE #( data        = lr_db_serv_perf_cat
                        node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                        source_node = /hec1/if_configuration_c=>sc_node-db_node
                        association = /hec1/if_configuration_c=>sc_association-db_node-db_server_perform_cat
                        source_key  = is_db_node-key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = lr_db_serv_perf_cat->key                                                ) INTO TABLE rt_modification.


        " Generate phasing and instances to create
        " for DB storage amount
        generate_phasing( EXPORTING is_node_phase      = CORRESPONDING #( <fs_phase> )
                                    it_table           = lt_storage_qty_filtered
                                    it_phasing_all     = it_phasing_all
                          IMPORTING et_phase_generated = DATA(lt_phase_generated)
                                    et_new_instance    = lt_storage_qty
                          CHANGING  co_message         = co_message                     ).


        " Create DB storage amount reference
        create_db_storage_amount( EXPORTING iv_root_key         = iv_root_key
                                            is_db_serv_perf_cat = lr_db_serv_perf_cat->*
                                            it_db_storage_qty   = lt_storage_qty
                                            it_phasing_all      = it_phasing_all
                                            it_phasing          = lt_phase_generated
                                  CHANGING  co_message          = co_message
                                            ct_modification     = rt_modification        ).


        " Generate phasing and instances to create
        " for DB server
        CLEAR lt_phase_generated.
        generate_phasing( EXPORTING is_node_phase      = CORRESPONDING #( <fs_phase> )
                                    it_table           = lt_server_filtered
                                    it_phasing_all     = it_phasing_all
                          IMPORTING et_phase_generated = lt_phase_generated
                                    et_new_instance    = lt_server
                          CHANGING  co_message         = co_message                     ).


        " Create DB server reference
        create_db_server( EXPORTING iv_root_key         = iv_root_key
                                    is_db_serv_perf_cat = lr_db_serv_perf_cat->*
                                    it_db_storage_qty   = it_db_storage_qty
                                    it_db_server        = lt_server
                                    it_db_storage       = it_db_storage
                                    it_db_backup        = it_db_backup
                                    it_phasing_all      = it_phasing_all
                                    it_phasing          = lt_phase_generated
                          CHANGING  co_message          = co_message
                                    ct_modification     = rt_modification         ).

      ENDIF. " IF <fs_phase> IS ASSIGNED.

      ADD 1 TO lv_counter.

      UNASSIGN <fs_phase>.
      CLEAR: lt_phase_generated,
             lt_storage_qty,
             lt_storage_qty_filtered,
             lt_server,
             lt_server_filtered,
             lr_db_serv_perf_cat.
    ENDLOOP.


  ENDMETHOD.


  METHOD create_db_storage.

    DATA: lr_db_storage      TYPE REF TO /hec1/s_data_db_storage_cs,
          lt_backup_filtered TYPE /hec1/t_data_db_backup_ct,
          lt_backup          TYPE /hec1/t_data_db_backup_ct.


    IF co_message IS NOT BOUND.
      co_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    DATA(lv_entry_no) = lines( it_db_storage ).
    DATA(lv_counter)  = 1.

    " Create DB storage backup instance
    LOOP AT it_db_storage ASSIGNING FIELD-SYMBOL(<fs_db_storage>).
      ASSIGN it_phasing[ sy-tabix ] TO FIELD-SYMBOL(<fs_phase>).
      IF <fs_phase> IS ASSIGNED.


        " Filter DB storage backup table for
        " creating the new instances
        lt_backup_filtered = VALUE #( FOR wa IN it_db_backup
                                      WHERE ( hec_node_db_serv_inst = <fs_db_storage>-hec_node_db_serv_inst AND
                                              hec_node_db_inst      = <fs_db_storage>-hec_node_db_inst      AND
                                              hec_node_db_node      = <fs_db_storage>-hec_node_db_node      AND
                                              hec_node_db_serv_pc   = <fs_db_storage>-hec_node_db_serv_pc   AND
                                              hec_node_db_server    = <fs_db_storage>-hec_node_db_server    AND
                                              hec_node_db_storage   = <fs_db_storage>-hec_node_db_storage       )
                                       ( wa )                                                                        ).


        " Insert new phase reference
        INSERT VALUE #( data        = NEW /hec1/s_data_phase_cs( <fs_phase> )
                        node        = /hec1/if_configuration_c=>sc_node-phase
                        source_node = /hec1/if_configuration_c=>sc_node-root
                        association = /hec1/if_configuration_c=>sc_association-root-phase
                        source_key  = iv_root_key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = /bopf/cl_frw_factory=>get_new_key( )                ) INTO TABLE ct_modification.


        " Create und fill DB storage reference
        lr_db_storage = NEW /hec1/s_data_db_storage_cs( BASE CORRESPONDING #( <fs_db_storage> EXCEPT key                       hec_has_successor       hec_db_clust_node_type_value
                                                                                                     parent_key                hec_successor_guid      hec_db_node_default
                                                                                                     hec_node_db_node          hec_predecessor_guid    crea_date_time
                                                                                                     hec_node_db_serv_pc       hec_successor_descr     crea_uname
                                                                                                     hec_node_db_server        hec_predecessor_descr   lchg_date_time
                                                                                                     hec_node_db_storage                               lchg_uname
                                                                                                     hec_phase_guid                                                                   )
                                                                key                          = /bopf/cl_frw_factory=>get_new_key( )
                                                                parent_key                   = is_db_server-key
                                                                hec_node_db_node             = is_db_server-hec_node_db_node
                                                                hec_node_db_serv_pc          = is_db_server-hec_node_db_serv_pc
                                                                hec_node_db_server           = is_db_server-hec_node_db_server
                                                                hec_node_db_storage          = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                hec_phase_guid               = <fs_phase>-hec_node_phase
                                                                hec_db_clust_node_type_value = is_db_server-hec_db_clust_node_type_value
                                                                hec_backup_qty               = SWITCH #( <fs_db_storage>-hec_db_clust_node_type_value
                                                                                                         WHEN /hec1/if_config_constants=>gc_db_clust_node_type-worker
                                                                                                         THEN <fs_db_storage>-hec_db_clust_node_type_value
                                                                                                         ELSE 0                                                       )
                                                                crea_uname                   = sy-uname                                                                                   ).


        " Set successor/predecessor
        IF lv_counter = 1.
          IF lv_entry_no > 1.
            DATA(lv_predecessor)             = lr_db_storage->key.
            lr_db_storage->hec_has_successor = abap_true.
          ENDIF.
        ELSE.
          IF lv_counter < lv_entry_no AND
             sy-tabix > 1.
            lr_db_storage->hec_has_successor    = abap_true.
            lr_db_storage->hec_predecessor_guid = lv_predecessor.
            lv_predecessor                      = lr_db_storage->key.
          ELSEIF lv_counter = lv_entry_no.
            lr_db_storage->hec_has_successor    = abap_false.
            lr_db_storage->hec_predecessor_guid = lv_predecessor.
          ENDIF.
        ENDIF. " IF lv_counter = 1.


        GET TIME STAMP FIELD lr_db_storage->crea_date_time.


        " Insert DB storage reference
        INSERT VALUE #( data        = lr_db_storage
                        node        = /hec1/if_configuration_c=>sc_node-db_storage
                        source_node = /hec1/if_configuration_c=>sc_node-db_server
                        association = /hec1/if_configuration_c=>sc_association-db_server-db_storage
                        source_key  = is_db_server-key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = lr_db_storage->key                                            ) INTO TABLE ct_modification.


        " Only for worker node
        IF lr_db_storage->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-worker.

          " Generate phasing and instances to create
          " for DB storage backup
          generate_phasing( EXPORTING is_node_phase      = CORRESPONDING #( <fs_phase> )
                                      it_table           = lt_backup_filtered
                                      it_phasing_all     = it_phasing_all
                            IMPORTING et_phase_generated = DATA(lt_phase_generated)
                                      et_new_instance    = lt_backup
                            CHANGING  co_message         = co_message                    ).


          " Create DB storage reference
          create_db_storage_backup( EXPORTING iv_root_key     = iv_root_key
                                              is_db_storage   = lr_db_storage->*
                                              it_db_backup    = lt_backup
                                              it_phasing_all  = it_phasing_all
                                              it_phasing      = lt_phase_generated
                                    CHANGING  co_message      = co_message
                                              ct_modification = ct_modification    ).

        ENDIF. " lr_db_storage->hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-worker.
      ENDIF. " IF <fs_phase> IS ASSIGNED.

      ADD 1 TO lv_counter.

      UNASSIGN <fs_phase>.
      CLEAR: lt_phase_generated,
             lt_backup,
             lt_backup_filtered,
             lr_db_storage.
    ENDLOOP.


  ENDMETHOD.


  METHOD create_db_storage_amount.

    DATA: lr_db_storage_qty TYPE REF TO /hec1/s_data_db_storage_qty_cs.


    IF co_message IS NOT BOUND.
      co_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    DATA(lv_entry_no) = lines( it_db_storage_qty ).
    DATA(lv_counter)  = 1.

    " Create DB storage amount instance
    LOOP AT it_db_storage_qty ASSIGNING FIELD-SYMBOL(<fs_db_storage_qty>).
      ASSIGN it_phasing[ sy-tabix ] TO FIELD-SYMBOL(<fs_phase>).
      IF <fs_phase> IS ASSIGNED.

        " Insert new phase reference
        INSERT VALUE #( data        = NEW /hec1/s_data_phase_cs( <fs_phase> )
                        node        = /hec1/if_configuration_c=>sc_node-phase
                        source_node = /hec1/if_configuration_c=>sc_node-root
                        association = /hec1/if_configuration_c=>sc_association-root-phase
                        source_key  = iv_root_key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = /bopf/cl_frw_factory=>get_new_key( )                ) INTO TABLE ct_modification.


        " Create und fill DB storage amount reference
        lr_db_storage_qty = NEW /hec1/s_data_db_storage_qty_cs( BASE CORRESPONDING #( <fs_db_storage_qty> EXCEPT key                       hec_has_successor       hec_db_clust_node_type_value
                                                                                                                 parent_key                hec_successor_guid      hec_db_node_default
                                                                                                                 hec_node_db_node          hec_predecessor_guid    crea_date_time
                                                                                                                 hec_node_db_serv_pc       hec_successor_descr     crea_uname
                                                                                                                 hec_node_db_storage_qty   hec_predecessor_descr   lchg_date_time
                                                                                                                 hec_phase_guid                                    lchg_uname                    )
                                                                key                          = /bopf/cl_frw_factory=>get_new_key( )
                                                                parent_key                   = is_db_serv_perf_cat-key
                                                                hec_node_db_node             = is_db_serv_perf_cat-hec_node_db_node
                                                                hec_node_db_serv_pc          = is_db_serv_perf_cat-hec_node_db_serv_pc
                                                                hec_node_db_storage_qty      = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                hec_phase_guid               = <fs_phase>-hec_node_phase
                                                                hec_db_clust_node_type_value = is_db_serv_perf_cat-hec_db_clust_node_type_value
                                                                crea_uname                   = sy-uname                                                                                                ).


        " Set successor/predecessor
        IF lv_counter = 1.
          IF lv_entry_no > 1.
            DATA(lv_predecessor)                 = lr_db_storage_qty->key.
            lr_db_storage_qty->hec_has_successor = abap_true.
          ENDIF.
        ELSE.
          IF lv_counter < lv_entry_no AND
             sy-tabix > 1.
            lr_db_storage_qty->hec_has_successor    = abap_true.
            lr_db_storage_qty->hec_predecessor_guid = lv_predecessor.
            lv_predecessor                          = lr_db_storage_qty->key.
          ELSEIF lv_counter = lv_entry_no.
            lr_db_storage_qty->hec_has_successor    = abap_false.
            lr_db_storage_qty->hec_predecessor_guid = lv_predecessor.
          ENDIF.
        ENDIF. " IF lv_counter = 1.


        GET TIME STAMP FIELD lr_db_storage_qty->crea_date_time.


        " Insert DB storage amount reference
        INSERT VALUE #( data        = lr_db_storage_qty
                        node        = /hec1/if_configuration_c=>sc_node-db_storage_amount
                        source_node = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                        association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount
                        source_key  = is_db_serv_perf_cat-key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = lr_db_storage_qty->key                                                           ) INTO TABLE ct_modification.

      ENDIF. " IF <fs_phase> IS ASSIGNED.

      ADD 1 TO lv_counter.

      UNASSIGN <fs_phase>.
      CLEAR lr_db_storage_qty.
    ENDLOOP.


  ENDMETHOD.


  METHOD create_db_storage_backup.

    DATA: lr_db_backup TYPE REF TO /hec1/s_data_db_backup_cs.


    IF co_message IS NOT BOUND.
      co_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    DATA(lv_entry_no) = lines( it_db_backup ).
    DATA(lv_counter)  = 1.

    " Create DB storage backup instance
    LOOP AT it_db_backup ASSIGNING FIELD-SYMBOL(<fs_db_backup>).
      ASSIGN it_phasing[ sy-tabix ] TO FIELD-SYMBOL(<fs_phase>).
      IF <fs_phase> IS ASSIGNED.

        " Insert new phase reference
        INSERT VALUE #( data        = NEW /hec1/s_data_phase_cs( <fs_phase> )
                        node        = /hec1/if_configuration_c=>sc_node-phase
                        source_node = /hec1/if_configuration_c=>sc_node-root
                        association = /hec1/if_configuration_c=>sc_association-root-phase
                        source_key  = iv_root_key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = /bopf/cl_frw_factory=>get_new_key( )                ) INTO TABLE ct_modification.


        " Create und fill DB storage backup reference
        lr_db_backup = NEW /hec1/s_data_db_backup_cs( BASE CORRESPONDING #( <fs_db_backup> EXCEPT key                     hec_has_successor       hec_db_clust_node_type_value
                                                                                                  parent_key              hec_successor_guid      hec_db_node_default
                                                                                                  hec_node_db_node        hec_predecessor_guid    crea_date_time
                                                                                                  hec_node_db_serv_pc     hec_successor_descr     crea_uname
                                                                                                  hec_node_db_server      hec_predecessor_descr   lchg_date_time
                                                                                                  hec_node_db_storage                             lchg_uname
                                                                                                  hec_phase_guid                                                                 )
                                                      key                          = /bopf/cl_frw_factory=>get_new_key( )
                                                      parent_key                   = is_db_storage-key
                                                      hec_node_db_node             = is_db_storage-hec_node_db_node
                                                      hec_node_db_serv_pc          = is_db_storage-hec_node_db_serv_pc
                                                      hec_node_db_server           = is_db_storage-hec_node_db_server
                                                      hec_node_db_storage          = is_db_storage-hec_node_db_storage
                                                      hec_node_db_backup           = /rbp/cl_general_utilities=>get_new_guid22( )
                                                      hec_phase_guid               = <fs_phase>-hec_node_phase
                                                      hec_db_clust_node_type_value = is_db_storage-hec_db_clust_node_type_value
                                                      crea_uname                   = sy-uname                                                                                         ).

        " Set successor/predecessor
        IF lv_counter = 1.
          IF lv_entry_no > 1.
            DATA(lv_predecessor)            = lr_db_backup->key.
            lr_db_backup->hec_has_successor = abap_true.
          ENDIF.
        ELSE.
          IF lv_counter < lv_entry_no AND
             sy-tabix > 1.
            lr_db_backup->hec_has_successor    = abap_true.
            lr_db_backup->hec_predecessor_guid = lv_predecessor.
            lv_predecessor                     = lr_db_backup->key.
          ELSEIF lv_counter = lv_entry_no.
            lr_db_backup->hec_has_successor    = abap_false.
            lr_db_backup->hec_predecessor_guid = lv_predecessor.
          ENDIF.
        ENDIF. " IF lv_counter = 1.


        GET TIME STAMP FIELD lr_db_backup->crea_date_time.


        " Insert DB storage backup reference
        INSERT VALUE #( data        = lr_db_backup
                        node        = /hec1/if_configuration_c=>sc_node-db_storage_backup
                        source_node = /hec1/if_configuration_c=>sc_node-db_storage
                        association = /hec1/if_configuration_c=>sc_association-db_storage-db_storage_backup
                        source_key  = is_db_storage-key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = lr_db_backup->key                                                     ) INTO TABLE ct_modification.

      ENDIF. " IF <fs_phase> IS ASSIGNED.

      ADD 1 TO lv_counter.

      UNASSIGN <fs_phase>.
      CLEAR lr_db_backup.
    ENDLOOP.


  ENDMETHOD.


  METHOD generate_phasing.

    DATA: lv_start_date_ext TYPE char10,
          lv_end_date_ext   TYPE char10.


    IF co_message IS NOT BOUND.
      co_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.


    LOOP AT it_table ASSIGNING FIELD-SYMBOL(<fs_table>).

      ASSIGN COMPONENT 'HEC_PHASE_GUID'
          OF STRUCTURE <fs_table>
       TO FIELD-SYMBOL(<fs_phase_guid>).

      IF <fs_phase_guid> IS ASSIGNED.
        " Get phasing from phasing tree
        TRY.
            DATA(ls_phase) = it_phasing_all[ hec_node_phase = <fs_phase_guid> ].
          CATCH cx_sy_itab_line_not_found.
*            co_message->add_cm( NEW /hec1/cx_bopf_config( textid             = /hec1/cx_bopf_config=>sync_config_for_node
*                                                          severity           = /bobf/cm_frw=>co_severity_error
*                                                          lifetime           = /bobf/if_frw_c=>sc_lifetime_set_by_bopf
*                                                          symptom            = /bobf/if_frw_message_symptoms=>co_bo_inconsistency
*                                                          ms_origin_location = VALUE #( node_key = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
*                                                                                        key      = <fs_app_serv_perf_cat>-key                               ) ) ).

            RETURN. " >>>>>>
        ENDTRY.
      ENDIF.

      IF et_phase_generated IS INITIAL.
        IF ( is_node_phase-hec_phase_start_date BETWEEN ls_phase-hec_phase_start_date AND
                                                        ls_phase-hec_phase_end_date       ).

          DATA(lv_start_date) = is_node_phase-hec_phase_start_date.

          ASSIGN COMPONENT 'HEC_SUCCESSOR_GUID'
              OF STRUCTURE <fs_table>
           TO FIELD-SYMBOL(<fs_successor_guid>).

          IF <fs_successor_guid> IS NOT ASSIGNED    OR
           ( <fs_successor_guid> IS ASSIGNED AND
             <fs_successor_guid> IS INITIAL      ).
            DATA(lv_end_date) = is_node_phase-hec_phase_end_date.
          ELSE.

            LOOP AT it_table ASSIGNING FIELD-SYMBOL(<fs_data>).
              ASSIGN COMPONENT 'KEY'
                  OF STRUCTURE <fs_data>
               TO FIELD-SYMBOL(<fs_key>).

              IF <fs_key> IS ASSIGNED AND
                 <fs_key> = <fs_successor_guid>.
                ASSIGN COMPONENT 'HEC_PHASE_GUID'
                    OF STRUCTURE <fs_data>
                 TO FIELD-SYMBOL(<fs_succ_phase_guid>).
                EXIT. " >>>>>>>
              ENDIF.

              UNASSIGN <fs_key>.
            ENDLOOP.

            IF <fs_succ_phase_guid> IS ASSIGNED.
              TRY.
                  DATA(ls_phase_succ) = it_phasing_all[ hec_node_phase = <fs_succ_phase_guid> ].
                CATCH cx_sy_itab_line_not_found.
              ENDTRY.

              lv_end_date = COND #( WHEN ls_phase_succ-hec_phase_start_date BETWEEN is_node_phase-hec_phase_start_date AND
                                                                                    is_node_phase-hec_phase_end_date
                                    THEN ls_phase-hec_phase_end_date
                                    ELSE is_node_phase-hec_phase_end_date                                                  ).

              DATA(lv_successor_guid) = COND #( WHEN ls_phase_succ-hec_phase_start_date BETWEEN is_node_phase-hec_phase_start_date AND
                                                                                                is_node_phase-hec_phase_end_date
                                                THEN /rbp/cl_general_utilities=>get_new_guid22( )
                                                ELSE abap_false                                                                         ).

            ENDIF. " IF <fs_succ_phase_guid> IS ASSIGNED.
          ENDIF. " IF <fs_successor_guid> IS NOT ASSIGNED    OR


          " Get new phasing GUID
          DATA(lv_phase_guid) = /rbp/cl_general_utilities=>get_new_guid22( ).

          CALL FUNCTION 'CONVERT_DATE_TO_EXTERNAL'
            EXPORTING
              date_internal = lv_start_date
            IMPORTING
              date_external = lv_start_date_ext.

          CALL FUNCTION 'CONVERT_DATE_TO_EXTERNAL'
            EXPORTING
              date_internal = lv_end_date
            IMPORTING
              date_external = lv_end_date_ext.

          DATA(ls_phase_generated) = VALUE /hec1/s_data_phase_cs( hec_node_parent_phase    = lv_phase_guid
                                                                  hec_node_phase           = lv_phase_guid
                                                                  hec_phase_descr          = |{ lv_start_date_ext } - { lv_end_date_ext }|
                                                                  hec_phase_tree_descr     = |{ lv_start_date_ext } - { lv_end_date_ext }|
                                                                  hec_phase_start_date     = lv_start_date
                                                                  hec_phase_end_date       = lv_end_date
                                                                  hec_duration_unit        = ls_phase-hec_duration_unit
                                                                  hec_phase_generated      = abap_true
                                                                  hec_phase_successor_guid = lv_successor_guid
                                                                  crea_uname               = sy-uname                                       ).

          GET TIME STAMP FIELD ls_phase_generated-crea_date_time.

          INSERT ls_phase_generated INTO TABLE et_phase_generated.
          INSERT <fs_table>         INTO TABLE et_new_instance.
        ENDIF. " IF ( is_node_phase-hec_phase_start_date BETWEEN ls_phase-hec_phase_start_date AND
      ELSE.
        IF ls_phase-hec_phase_start_date BETWEEN is_node_phase-hec_phase_start_date AND
                                                 is_node_phase-hec_phase_end_date.

          lv_start_date = ls_phase-hec_phase_start_date.
          DATA(lv_predecessor_guid) = lv_successor_guid.
          CLEAR lv_successor_guid.

          ASSIGN COMPONENT 'HEC_SUCCESSOR_GUID'
              OF STRUCTURE <fs_table>
                        TO <fs_successor_guid>.

          IF <fs_successor_guid> IS NOT ASSIGNED    OR
           ( <fs_successor_guid> IS ASSIGNED AND
             <fs_successor_guid> IS INITIAL      ).
            lv_end_date = is_node_phase-hec_phase_end_date.
          ELSE.
            LOOP AT it_table ASSIGNING <fs_data>.
              ASSIGN COMPONENT 'KEY'
                  OF STRUCTURE <fs_data>
                            TO <fs_key>.

              IF <fs_key> IS ASSIGNED AND
                 <fs_key> = <fs_successor_guid>.
                ASSIGN COMPONENT 'HEC_PHASE_GUID'
                    OF STRUCTURE <fs_data>
                              TO <fs_succ_phase_guid>.
                EXIT. " >>>>>>>
              ENDIF.
            ENDLOOP.

            IF <fs_succ_phase_guid> IS ASSIGNED.
              TRY.
                  ls_phase_succ = it_phasing_all[ hec_node_phase = <fs_succ_phase_guid> ].
                CATCH cx_sy_itab_line_not_found.
              ENDTRY.

              lv_end_date = COND #( WHEN ls_phase_succ-hec_phase_start_date BETWEEN is_node_phase-hec_phase_start_date AND
                                                                                    is_node_phase-hec_phase_end_date
                                    THEN ls_phase-hec_phase_end_date
                                    ELSE is_node_phase-hec_phase_end_date                                                  ).

              lv_successor_guid = COND #( WHEN ls_phase_succ-hec_phase_start_date BETWEEN is_node_phase-hec_phase_start_date AND
                                                                                          is_node_phase-hec_phase_end_date
                                          THEN /rbp/cl_general_utilities=>get_new_guid22( )
                                          ELSE abap_false                                                                        ).

            ENDIF. " IF <fs_succ_phase_guid> IS ASSIGNED.
          ENDIF. " IF <fs_successor_guid> IS NOT ASSIGNED    OR

          " Get new phasing GUID
          lv_phase_guid = /rbp/cl_general_utilities=>get_new_guid22( ).

          CALL FUNCTION 'CONVERT_DATE_TO_EXTERNAL'
            EXPORTING
              date_internal = lv_start_date
            IMPORTING
              date_external = lv_start_date_ext.

          CALL FUNCTION 'CONVERT_DATE_TO_EXTERNAL'
            EXPORTING
              date_internal = lv_end_date
            IMPORTING
              date_external = lv_end_date_ext.

          ls_phase_generated = VALUE /hec1/s_data_phase_cs( hec_node_parent_phase      = lv_phase_guid
                                                            hec_node_phase             = lv_phase_guid
                                                            hec_phase_descr            = COND #( WHEN lv_predecessor_guid IS INITIAL
                                                                                                 THEN |{ lv_start_date_ext } - { lv_end_date_ext }|
                                                                                                 ELSE |Successor: { lv_start_date_ext } - { lv_end_date_ext }| )
                                                            hec_phase_tree_descr       = COND #( WHEN lv_predecessor_guid IS INITIAL
                                                                                                 THEN |{ lv_start_date_ext } - { lv_end_date_ext }|
                                                                                                 ELSE |Successor: { lv_start_date_ext } - { lv_end_date_ext }| )
                                                            hec_phase_start_date       = lv_start_date
                                                            hec_phase_end_date         = lv_end_date
                                                            hec_duration_unit          = ls_phase-hec_duration_unit
                                                            hec_phase_generated        = abap_true
                                                            hec_phase_successor_guid   = lv_successor_guid
                                                            hec_phase_predecessor_guid = lv_predecessor_guid
                                                            crea_uname                 = sy-uname                                       ).

          GET TIME STAMP FIELD ls_phase_generated-crea_date_time.

          INSERT ls_phase_generated INTO TABLE et_phase_generated.
          INSERT <fs_table>         INTO TABLE et_new_instance.

          CLEAR lv_predecessor_guid.

        ENDIF. " IF ls_phase-hec_phase_start_date BETWEEN is_node_phase-hec_phase_start_date AND
      ENDIF. " IF lt_phase_generated IS INITIAL.

      CLEAR: lv_start_date,
             lv_start_date_ext,
             lv_end_date,
             lv_end_date_ext,
             lv_phase_guid,
             ls_phase_succ,
             ls_phase,
             ls_phase_generated.

      UNASSIGN: <fs_phase_guid>,
                <fs_succ_phase_guid>,
                <fs_data>,
                <fs_key>,
                <fs_successor_guid>.
    ENDLOOP.


  ENDMETHOD.
ENDCLASS.