CLASS /hec1/cl_config_det_a_services DEFINITION
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
    DATA mr_act_param_phasing TYPE REF TO data .
    DATA mr_act_param_tier_ltb TYPE REF TO data .
    DATA mr_act_param_lt_amount TYPE REF TO data .

    METHODS determine_lt_backup_datacenter
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key .
    METHODS determine_a_storage_datacenter
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key .
    METHODS determine_a_storage_dcenter_cr
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key .
    METHODS determine_a_storage_class
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key .
    METHODS determine_a_storage_amount
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key .
    METHODS determine_a_storage_amount_cr
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key .
    METHODS determine_a_storage_class_cr
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key .
    METHODS determine_lt_backup_datacen_cr
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key .
    METHODS determine_lt_backup_class
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key .
    METHODS determine_lt_backup_class_cr
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key .
    METHODS determine_lt_backup_amount
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key .
    METHODS determine_lt_backup_amount_cr
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key .
    METHODS determine_tier_lt_backup
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
    METHODS determine_tier_lt_backup_cr
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



CLASS /hec1/cl_config_det_a_services IMPLEMENTATION.


  METHOD execute.

*    CLEAR: eo_message,
*           et_failed_key.

    DATA(ls_root) = /hec1/cl_config_helper=>get_root_node( iv_node_key = is_ctx-node_key
                                                           it_key      = it_key
                                                           io_read     = io_read
                                                           io_modify   = io_modify ).

    TRY.
        CASE is_ctx-det_key.
          WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_datacenter-create
            OR /hec1/if_configuration_c=>sc_determination-lt_backup_datacenter-update.
*            " **********************************
*            " Determine LT Backup Datacenter
*            " **********************************
            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_lt_backup_datacenter(
                      EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                it_key        = it_key                           " Key Table
                                io_read       = io_read                          " Interface to Reading Data
                                io_modify     = io_modify                        " Interface to Change Data
                      IMPORTING eo_message    = eo_message                       " Message Object
                                et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_lt_backup_datacen_cr(
                      EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                it_key        = it_key                           " Key Table
                                io_read       = io_read                          " Interface to Reading Data
                                io_modify     = io_modify                        " Interface to Change Data
                      IMPORTING eo_message    = eo_message                       " Message Object
                                et_failed_key = et_failed_key ).                 " Key Table

            ENDCASE. "ls_root-hec_contract_status.
          WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_class-create
            OR /hec1/if_configuration_c=>sc_determination-lt_backup_class-update.
*            " **********************************
*            " Determine LT Backup Class
*            " **********************************
            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_lt_backup_class(
                      EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                it_key        = it_key                           " Key Table
                                io_read       = io_read                          " Interface to Reading Data
                                io_modify     = io_modify                        " Interface to Change Data
                      IMPORTING eo_message    = eo_message                       " Message Object
                                et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_lt_backup_class_cr(
                      EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                it_key        = it_key                           " Key Table
                                io_read       = io_read                          " Interface to Reading Data
                                io_modify     = io_modify                        " Interface to Change Data
                      IMPORTING eo_message    = eo_message                       " Message Object
                                et_failed_key = et_failed_key ).                 " Key Table

            ENDCASE. "ls_root-hec_contract_status.

          WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_amount-create
            OR /hec1/if_configuration_c=>sc_determination-lt_backup_amount-update.
*            " **********************************
*            " Determine LT Backup Quota
*            " **********************************
            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_lt_backup_amount(
                      EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                it_key        = it_key                           " Key Table
                                io_read       = io_read                          " Interface to Reading Data
                                io_modify     = io_modify                        " Interface to Change Data
                      IMPORTING eo_message    = eo_message                       " Message Object
                                et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_lt_backup_amount_cr(
                      EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                it_key        = it_key                           " Key Table
                                io_read       = io_read                          " Interface to Reading Data
                                io_modify     = io_modify                        " Interface to Change Data
                      IMPORTING eo_message    = eo_message                       " Message Object
                                et_failed_key = et_failed_key ).                 " Key Table

            ENDCASE. "ls_root-hec_contract_status.

          WHEN /hec1/if_configuration_c=>sc_determination-add_storage_datacenter-create
            OR /hec1/if_configuration_c=>sc_determination-add_storage_datacenter-update.
            " **********************************
            " Determine Additional Storage Datacenter
            " **********************************
            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_a_storage_datacenter(
                      EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                it_key        = it_key                           " Key Table
                                io_read       = io_read                          " Interface to Reading Data
                                io_modify     = io_modify                        " Interface to Change Data
                      IMPORTING eo_message    = eo_message                       " Message Object
                                et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_a_storage_dcenter_cr(
                      EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                it_key        = it_key                           " Key Table
                                io_read       = io_read                          " Interface to Reading Data
                                io_modify     = io_modify                        " Interface to Change Data
                      IMPORTING eo_message    = eo_message                       " Message Object
                                et_failed_key = et_failed_key ).                 " Key Table

            ENDCASE. "ls_root-hec_contract_status.
          WHEN /hec1/if_configuration_c=>sc_determination-add_storage_class-create
            OR /hec1/if_configuration_c=>sc_determination-add_storage_class-update.
            " **********************************
            " Determine Additional Storage Class
            " **********************************
            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_a_storage_class(
                      EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                it_key        = it_key                           " Key Table
                                io_read       = io_read                          " Interface to Reading Data
                                io_modify     = io_modify                        " Interface to Change Data
                      IMPORTING eo_message    = eo_message                       " Message Object
                                et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_a_storage_class_cr(
                      EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                it_key        = it_key                           " Key Table
                                io_read       = io_read                          " Interface to Reading Data
                                io_modify     = io_modify                        " Interface to Change Data
                      IMPORTING eo_message    = eo_message                       " Message Object
                                et_failed_key = et_failed_key ).                 " Key Table

            ENDCASE. "ls_root-hec_contract_status.
          WHEN /hec1/if_configuration_c=>sc_determination-add_storage_amount-create
            OR /hec1/if_configuration_c=>sc_determination-add_storage_amount-update.
            " **********************************
            " Determine Additional Storage Amount
            " **********************************
            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_a_storage_amount(
                      EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                it_key        = it_key                           " Key Table
                                io_read       = io_read                          " Interface to Reading Data
                                io_modify     = io_modify                        " Interface to Change Data
                      IMPORTING eo_message    = eo_message                       " Message Object
                                et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_a_storage_amount_cr(
                      EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                it_key        = it_key                           " Key Table
                                io_read       = io_read                          " Interface to Reading Data
                                io_modify     = io_modify                        " Interface to Change Data
                      IMPORTING eo_message    = eo_message                       " Message Object
                                et_failed_key = et_failed_key ).                 " Key Table

            ENDCASE. "ls_root-hec_contract_status.

          WHEN /hec1/if_configuration_c=>sc_determination-tier_longterm_backup-create            OR
               /hec1/if_configuration_c=>sc_determination-tier_longterm_backup-update            OR
               /hec1/if_configuration_c=>sc_determination-tier_longterm_backup-update_after_tier.
*            " **********************************
*            " Determination tier lt_backup
*            " **********************************
            CASE ls_root-hec_contract_status.
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                " Initial Deal
                me->determine_tier_lt_backup( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                      it_key        = it_key                           " Key Table
                                                      io_read       = io_read                          " Interface to Reading Data
                                                      io_modify     = io_modify                        " Interface to Change Data
                                            IMPORTING eo_message    = eo_message                       " Message Object
                                                      et_failed_key = et_failed_key ).                 " Key Table

              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                " Change Request
                me->determine_tier_lt_backup_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
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


  METHOD determine_lt_backup_datacenter.
    DATA: lt_longterm_backup_dc        TYPE /hec1/t_data_lt_backup_dc_ct,
          lt_longterm_backup_dc_before TYPE /hec1/t_data_lt_backup_dc_ct,
          lr_longterm_backup_dc        TYPE REF TO /hec1/s_data_lt_backup_dc_cs,
          lt_phase                     TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing         TYPE TABLE OF /hec1/s_act_phase_inherit.

    CLEAR:
        eo_message,
        et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_longterm_backup_dc  ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_datacenter-create.

            LOOP AT lt_longterm_backup_dc REFERENCE INTO lr_longterm_backup_dc.
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_longterm_backup_dc->hec_ltb_datacenter_guid IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              lr_longterm_backup_dc->hec_delete_visible = abap_true.

              " Check instance status and switch
              IF ( lv_inst_status <> lr_longterm_backup_dc->hec_instance_status ).
                lr_longterm_backup_dc->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node           = is_ctx-node_key
                                   iv_key            = lr_longterm_backup_dc->key
                                   is_data           = lr_longterm_backup_dc      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP.

*            " ***************************************************************************
*            " update mode
*            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_datacenter-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_longterm_backup_dc_before  ).

            io_read->retrieve_by_association( EXPORTING iv_node         = /hec1/if_configuration_c=>sc_node-root
                                                        it_key          = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data    = abap_true
                                                        iv_association  = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data         = lt_phase ).

            LOOP AT lt_longterm_backup_dc REFERENCE INTO lr_longterm_backup_dc.


              ASSIGN lt_longterm_backup_dc_before[ key = lr_longterm_backup_dc->key ] TO FIELD-SYMBOL(<fs_longterm_backup_dc_before>).

              IF ( <fs_longterm_backup_dc_before> IS ASSIGNED ).
*                   " if the infrastructure provider is set and there is datacenter assigned
                IF ( lr_dlvy_unit->hec_inf_provider_guid IS NOT INITIAL ).

                  DATA(ls_datacenter) = VALUE #( lt_datacenter[ hec_node_datacenter = lr_longterm_backup_dc->hec_ltb_datacenter_guid ] OPTIONAL ).
                  lr_longterm_backup_dc->* = VALUE #( BASE lr_longterm_backup_dc->*
                                                   hec_ltb_datacenter_guid  = ls_datacenter-hec_node_datacenter
                                                   hec_ltb_datacenter_descr = COND #( WHEN ls_datacenter-hec_datacenter_descr IS NOT INITIAL
                                                                                      THEN ls_datacenter-hec_datacenter_descr
                                                                                      ELSE space                                            )
                                                   hec_tree_descr           = COND #( WHEN ls_datacenter-hec_datacenter_guid IS NOT INITIAL
                                                                                      THEN |{ ls_datacenter-hec_datacenter_descr }|
                                                                                      ELSE |<new datacenter>| )
                  ).
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF ( lr_longterm_backup_dc->hec_phase_guid NE <fs_longterm_backup_dc_before>-hec_phase_guid ).

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_longterm_backup_dc->key
                                  hec_phase_guid_new = lr_longterm_backup_dc->hec_phase_guid
                                  hec_phase_guid_old = <fs_longterm_backup_dc_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_longterm_backup_dc->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "Phase changed

                " Reset Datacenter
                IF ( <fs_longterm_backup_dc_before>-hec_ltb_datacenter_guid IS NOT INITIAL ) AND ( lr_longterm_backup_dc->hec_ltb_datacenter_guid IS INITIAL ).
                  CLEAR: lr_longterm_backup_dc->hec_ltb_datacenter_descr.

                  lv_data_changed = abap_true.
                ENDIF.

                " Set Datacenter Descr / Tree Descr
                IF ( <fs_longterm_backup_dc_before>-hec_ltb_datacenter_descr NE lr_longterm_backup_dc->hec_ltb_datacenter_descr ).
                  lr_longterm_backup_dc->hec_tree_descr          = COND #( WHEN lr_longterm_backup_dc->hec_ltb_datacenter_descr IS INITIAL
                                                                           THEN ||
                                                                           ELSE |{ lr_longterm_backup_dc->hec_ltb_datacenter_descr }| ).

                  lv_data_changed = abap_true.
                ENDIF.

              ENDIF.


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_longterm_backup_dc->hec_ltb_datacenter_guid IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              lr_longterm_backup_dc->hec_delete_visible = abap_true.

              IF ( lv_inst_status <> lr_longterm_backup_dc->hec_instance_status ).
                lr_longterm_backup_dc->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node           = is_ctx-node_key
                                   iv_key            = lr_longterm_backup_dc->key
                                   is_data           = lr_longterm_backup_dc      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_longterm_backup_dc_before>.

            ENDLOOP. "LOOP AT lt_add_service REFERENCE INTO lr_add_service.

            "-----------------------------------
            " Update Phasing
            "-----------------------------------
            IF ( lt_act_param_phasing IS NOT INITIAL ).
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.

        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.

  ENDMETHOD.

  METHOD determine_lt_backup_class.
    DATA: lt_longterm_backup_class     TYPE /hec1/t_data_lt_backup_cl_ct,
          lt_longterm_backup_cl_before TYPE /hec1/t_data_lt_backup_cl_ct,
          lr_longterm_backup_cl        TYPE REF TO /hec1/s_data_lt_backup_cl_cs,
          lt_phase                     TYPE /hec1/t_data_phase_ct,
          ls_act_param_tier_ltb        TYPE /hec1/s_act_update_tier_ltb.

    CLEAR:
        eo_message,
        et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_longterm_backup_class  ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_class-create.

            LOOP AT lt_longterm_backup_class REFERENCE INTO lr_longterm_backup_cl.
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_longterm_backup_cl->hec_ltb_class_guid      IS NOT INITIAL AND
                                                                             lr_longterm_backup_cl->hec_ltb_datacenter_guid IS NOT INITIAL
*                                                                             lr_longterm_backup_cl->hec_phase_guid         IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              lr_longterm_backup_cl->hec_delete_visible = abap_true.

              " Check instance status and switch
              IF ( lv_inst_status <> lr_longterm_backup_cl->hec_instance_status ).
                lr_longterm_backup_cl->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node           = is_ctx-node_key
                                   iv_key            = lr_longterm_backup_cl->key
                                   is_data           = lr_longterm_backup_cl      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP.

*            " ***************************************************************************
*            " update mode
*            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_class-update.

            CLEAR: ls_act_param_tier_ltb.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_longterm_backup_cl_before  ).

            io_read->retrieve_by_association( EXPORTING iv_node         = /hec1/if_configuration_c=>sc_node-root
                                                        it_key          = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data    = abap_true
                                                        iv_association  = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data         = lt_phase ).

            LOOP AT lt_longterm_backup_class REFERENCE INTO lr_longterm_backup_cl.


              ASSIGN lt_longterm_backup_cl_before[ key = lr_longterm_backup_cl->key ] TO FIELD-SYMBOL(<fs_longterm_backup_before>).

              IF ( <fs_longterm_backup_before> IS ASSIGNED ).

                "-----------------------------------
                " Longterm backup GUID has changed
                "-----------------------------------
                " Get service class data
                SELECT SINGLE hec_longt_backup_class_descr INTO @DATA(lv_longterm_description)
                  FROM /hec1/i_longtermbackupbasic
                 WHERE hec_apm_guid                = @lr_landscape->hec_apm_guid
                   AND hec_longt_backup_class_guid = @lr_longterm_backup_cl->hec_ltb_class_guid.
                IF ( sy-subrc = 0 ).
                  lr_longterm_backup_cl->* = VALUE #( BASE lr_longterm_backup_cl->*
                                                       hec_ltb_class_descr     = lv_longterm_description
                                                                                                         ).
                  "Set longterm backup description in case it is empty
                  IF ( lr_longterm_backup_cl->hec_ltb_class_guid IS NOT INITIAL  ) AND
                     ( lr_longterm_backup_cl->hec_ltb_class_descr IS NOT INITIAL ) AND
                     ( lr_longterm_backup_cl->hec_ltb_class_descr_ext IS INITIAL ).
                    lr_longterm_backup_cl->hec_ltb_class_descr_ext = lr_longterm_backup_cl->hec_ltb_class_descr.
                  ENDIF.

                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Resets -> TODO move to actions
                "-----------------------------------
                " Reset Service Description
                IF ( lr_longterm_backup_cl->hec_ltb_class_guid IS INITIAL ).
                  IF ( lr_longterm_backup_cl->hec_ltb_class_descr = lr_longterm_backup_cl->hec_ltb_class_descr_ext ).
                    CLEAR: lr_longterm_backup_cl->hec_ltb_class_descr_ext.
                  ENDIF.
                  CLEAR: lr_longterm_backup_cl->hec_ltb_class_descr.

                  lv_data_changed = abap_true.
                ENDIF.

                IF ( <fs_longterm_backup_before>-hec_ltb_class_descr_ext <> lr_longterm_backup_cl->hec_ltb_class_descr_ext ).
                  lr_longterm_backup_cl->hec_tree_descr = COND #( WHEN lr_longterm_backup_cl->hec_ltb_class_descr IS NOT INITIAL
                                                     THEN |{ lr_longterm_backup_cl->hec_ltb_class_descr } : { lr_longterm_backup_cl->hec_ltb_class_descr_ext }|
                                                     ELSE |{ lr_longterm_backup_cl->hec_ltb_class_descr_ext }|  ).
                  lv_data_changed = abap_true.
                ENDIF.

                IF ( <fs_longterm_backup_before>-hec_ltb_class_descr <> lr_longterm_backup_cl->hec_ltb_class_descr ).
                  lr_longterm_backup_cl->hec_tree_descr = COND #( WHEN lr_longterm_backup_cl->hec_ltb_class_descr IS NOT INITIAL
                                                     THEN |{ lr_longterm_backup_cl->hec_ltb_class_descr } : { lr_longterm_backup_cl->hec_ltb_class_descr_ext }|
                                                     ELSE |{ lr_longterm_backup_cl->hec_ltb_class_descr_ext }|  ).
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Check instance status and switch
                "-----------------------------------
                lv_inst_status = COND /hec1/config_instance_status( WHEN lr_longterm_backup_cl->hec_ltb_class_guid      IS NOT INITIAL AND
                                                                         lr_longterm_backup_cl->hec_ltb_datacenter_guid IS NOT INITIAL
                                                                    THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                    ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

                lr_longterm_backup_cl->hec_delete_visible = abap_true.

                IF ( lv_inst_status <> lr_longterm_backup_cl->hec_instance_status ).
                  lr_longterm_backup_cl->hec_instance_status = lv_inst_status.
                  lv_data_changed = abap_true.
                ENDIF.

                " check, if assigned tier_lt_backup nodes must be updated
                IF ( lr_longterm_backup_cl->hec_ltb_class_guid <> <fs_longterm_backup_before>-hec_ltb_class_guid )
                OR ( lr_longterm_backup_cl->hec_ltb_class_descr_ext <> <fs_longterm_backup_before>-hec_ltb_class_descr_ext ).

                  ls_act_param_tier_ltb  = CORRESPONDING /hec1/s_act_update_tier_ltb( lr_longterm_backup_cl->* ).
                ENDIF.

                """"""""""""""""""""""""""""""""""""""""""""""""""""""
                " Update TIER_LT_BACKUP
                """"""""""""""""""""""""""""""""""""""""""""""""""""""

                IF ( ls_act_param_tier_ltb IS NOT INITIAL ).
                  me->mr_act_param_tier_ltb = NEW /hec1/s_act_update_tier_ltb( ls_act_param_tier_ltb ).

                  /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                      is_ctx          = CORRESPONDING #( is_ctx )
                      it_key          = it_key
                      iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_tier_lt_backup )
                      iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                      ir_act_param    = me->mr_act_param_tier_ltb ).
                ENDIF.


                IF ( lv_data_changed = abap_true ).
                  io_modify->update( iv_node           = is_ctx-node_key
                                     iv_key            = lr_longterm_backup_cl->key
                                     is_data           = lr_longterm_backup_cl      ).
                ENDIF.

                CLEAR: lv_inst_status,
                       lv_data_changed.
              ENDIF.
              UNASSIGN <fs_longterm_backup_before>.

            ENDLOOP. "LOOP AT lt_add_service REFERENCE INTO lr_add_service.

            "-----------------------------------
            " Update Phasing
            "-----------------------------------
*            IF ( lt_act_param_phasing IS NOT INITIAL ).
*              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).
*
*              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
*                  is_ctx          = CORRESPONDING #( is_ctx )
*                  it_key          = it_key
*                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
*                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
*                  ir_act_param    = me->mr_act_param_phasing ).
*            ENDIF.
*
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.
  ENDMETHOD.


  METHOD determine_lt_backup_amount.

    DATA: lt_longterm_backup_amount     TYPE /hec1/t_lt_backup_amount_ct,
          lt_longterm_backup_bef_amount TYPE /hec1/t_lt_backup_amount_ct,
          lr_longterm_backup_amount     TYPE REF TO  /hec1/s_lt_backup_amount_cs,
          lt_phase                      TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing          TYPE TABLE OF /hec1/s_act_phase_inherit.

    CLEAR:
        eo_message,
        et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_longterm_backup_amount  ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_amount-create.

            LOOP AT lt_longterm_backup_amount REFERENCE INTO lr_longterm_backup_amount.
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_longterm_backup_amount->hec_ltb_class_guid      IS NOT INITIAL AND
                                                                             lr_longterm_backup_amount->hec_ltb_datacenter_guid IS NOT INITIAL AND
                                                                             lr_longterm_backup_amount->hec_phase_guid         IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              lr_longterm_backup_amount->hec_delete_visible = abap_true.

              " Check instance status and switch
              IF ( lv_inst_status <> lr_longterm_backup_amount->hec_instance_status ).
                lr_longterm_backup_amount->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node           = is_ctx-node_key
                                   iv_key            = lr_longterm_backup_amount->key
                                   is_data           = lr_longterm_backup_amount      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP.

*            " ***************************************************************************
*            " update mode
*            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_amount-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_longterm_backup_bef_amount  ).

            io_read->retrieve_by_association( EXPORTING iv_node         = /hec1/if_configuration_c=>sc_node-root
                                                        it_key          = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data    = abap_true
                                                        iv_association  = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data         = lt_phase ).

            LOOP AT lt_longterm_backup_amount REFERENCE INTO lr_longterm_backup_amount.


              ASSIGN lt_longterm_backup_bef_amount[ key = lr_longterm_backup_amount->key ] TO FIELD-SYMBOL(<fs_longterm_backup_befor>).

              IF ( <fs_longterm_backup_befor> IS ASSIGNED ).
                TRY.


                    " if the infrastructure provider is set and there is datacenter assigned
                    " get the pricing
                    IF ( lr_dlvy_unit->hec_inf_provider_guid IS NOT INITIAL ) AND ( lr_longterm_backup_amount->hec_ltb_datacenter_guid IS NOT INITIAL ).
                      DATA(ls_datacenter) = VALUE #( lt_datacenter[ hec_node_datacenter = lr_longterm_backup_amount->hec_ltb_datacenter_guid ] OPTIONAL ).

                      SELECT SINGLE hec_cb_pricing_lb_guid INTO @DATA(lv_ltb_legoblock)
                        FROM /hec1/a_back_lb
                       WHERE hec_apm_guid            = @lr_longterm_backup_amount->hec_apm_guid
                         AND hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid
                         AND hec_sec_datacenter_guid = @ls_datacenter-hec_datacenter_guid
                         AND hec_backup_class_guid   = @lr_longterm_backup_amount->hec_ltb_class_guid.

                      " Get pricing
                      SELECT SINGLE * INTO @DATA(ls_pricing) "#EC CI_ALL_FIELDS_NEEDED
                         FROM /hec1/c_cbp_lb
                        WHERE hec_price_lb = @lv_ltb_legoblock.
                      IF ( sy-subrc = 0 ).

                        DATA(lv_exchange_rate) = lr_longterm_backup_amount->hec_exchange_rate. "Temp field because the ls_pricing structure overwrites the real exchange_rate

                        lr_longterm_backup_amount->* = VALUE #( BASE lr_longterm_backup_amount->*
                             hec_tree_descr           = COND #( WHEN lr_longterm_backup_amount->hec_phase_guid IS INITIAL
                                                                THEN |{ VALUE #( lt_phase[ hec_node_phase = lr_longterm_backup_amount->hec_phase_guid ]-hec_phase_descr OPTIONAL ) } : { lr_longterm_backup_amount->hec_ltb_amount }|
                                                                ELSE |{ lr_longterm_backup_amount->hec_ltb_amount }| )
                             hec_month_price_fee      = lr_longterm_backup_amount->hec_ltb_amount * ls_pricing-hec_month_price_eur
*                             price                    = CORRESPONDING #( ls_pricing )
                             price                   = CORRESPONDING #( BASE ( lr_longterm_backup_amount->price ) ls_pricing )
                             hec_exchange_rate        = lv_exchange_rate
                        ).
                        lv_data_changed = abap_true.
                      ENDIF.

                      lv_data_changed = abap_true.
                    ENDIF. " IF lv_infra_provider IS NOT INITIAL.
                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF ( lr_longterm_backup_amount->hec_phase_guid NE <fs_longterm_backup_befor>-hec_phase_guid ).

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_longterm_backup_amount->key
                                  hec_phase_guid_new = lr_longterm_backup_amount->hec_phase_guid
                                  hec_phase_guid_old = <fs_longterm_backup_befor>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_longterm_backup_amount->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "Phase changed
              ENDIF. "<fs_longterm_backup_befor> is assigned


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_longterm_backup_amount->hec_ltb_class_guid      IS NOT INITIAL AND
                                                                       lr_longterm_backup_amount->hec_ltb_datacenter_guid IS NOT INITIAL AND
                                                                       lr_longterm_backup_amount->hec_phase_guid          IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              lr_longterm_backup_amount->hec_delete_visible = abap_true.

              IF ( lv_inst_status <> lr_longterm_backup_amount->hec_instance_status ).
                lr_longterm_backup_amount->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node           = is_ctx-node_key
                                   iv_key            = lr_longterm_backup_amount->key
                                   is_data           = lr_longterm_backup_amount      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_longterm_backup_befor>.

            ENDLOOP. "LOOP AT lt_add_service REFERENCE INTO lr_add_service.

            "-----------------------------------
            " Update Phasing
            "-----------------------------------
            IF ( lt_act_param_phasing IS NOT INITIAL ).
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.
*
        ENDCASE.
*

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD determine_tier_lt_backup.
    DATA: lt_tier_lt_backup        TYPE /hec1/t_data_tier_lt_backup_ct,
          lt_tier_lt_backup_before TYPE /hec1/t_data_tier_lt_backup_ct,
          lt_tier                  TYPE /hec1/t_data_tier_ct,
          lt_root_key              TYPE /bobf/t_frw_key,
          lt_landscape_key         TYPE /bobf/t_frw_key,
          lt_longt_backup_cl       TYPE /hec1/t_data_lt_backup_cl_ct,
          lt_phase                 TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing     TYPE TABLE OF /hec1/s_act_phase_inherit.



    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_tier_lt_backup ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier_longterm_backup-create.

            " Get tier node (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier_longterm_backup-to_parent
                                              IMPORTING et_data        = lt_tier                                                        ).

            LOOP AT lt_tier_lt_backup REFERENCE INTO DATA(lr_tier_lt_backup).
              ASSIGN lt_tier[ key = lr_tier_lt_backup->parent_key ] TO FIELD-SYMBOL(<fs_tier>).

              lr_tier_lt_backup->hec_delete_visible = abap_true.

              IF ( <fs_tier>                          IS ASSIGNED )    AND
                 ( <fs_tier>-hec_tier_descr           IS NOT INITIAL ) AND
                 ( <fs_tier>-hec_tier_type_value      IS NOT INITIAL ) AND
                 ( <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL ).
                DATA(lv_release) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              IF ( lv_release <> lr_tier_lt_backup->hec_row_selectable ).
                lr_tier_lt_backup->hec_row_selectable = lv_release.
                DATA(lv_data_changed) = abap_true.
              ENDIF.


              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_tier_lt_backup->key
                                   is_data = lr_tier_lt_backup      ).
              ENDIF.

              UNASSIGN <fs_tier>.
              CLEAR: lv_data_changed,
                     lv_release.
            ENDLOOP.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier_longterm_backup-update.

            " Data before update
            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_tier_lt_backup_before ).
            " ROOT -> PHASE
            io_read->retrieve_by_association( EXPORTING iv_node         = /hec1/if_configuration_c=>sc_node-root
                                                        it_key          = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data    = abap_true
                                                        iv_association  = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data         = lt_phase ).


            LOOP AT lt_tier_lt_backup REFERENCE INTO lr_tier_lt_backup.

              ASSIGN lt_tier_lt_backup_before[ key = lr_tier_lt_backup->key ] TO FIELD-SYMBOL(<fs_lt_backup_before>).
              IF ( <fs_lt_backup_before> IS ASSIGNED ).

                "-----------------------------------
                " Service Class GUID has changed ?
                "-----------------------------------
                IF ( lr_tier_lt_backup->hec_tlt_backup_cl_node_ref IS NOT INITIAL ) AND
                 ( ( lr_tier_lt_backup->hec_tlt_backup_cl_node_ref <> <fs_lt_backup_before>-hec_tlt_backup_cl_node_ref ) ).

                  " Get service class data from corresponding longterm backup pool
                  IF ( lt_root_key IS INITIAL ).

                    APPEND VALUE #( key = lr_tier_lt_backup->root_key ) TO lt_root_key.

                    " Get longterm backup datacenter
                    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                                it_key         = lt_root_key
                                                                iv_association = /hec1/if_configuration_c=>sc_association-root-lt_backup_datacenter
                                                      IMPORTING et_target_key  = DATA(lt_longt_backup_dc_key)                                      ).
                    " Get longterm backup class
                    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-lt_backup_datacenter
                                                                it_key         = lt_longt_backup_dc_key
                                                                iv_fill_data   = abap_true
                                                                iv_association = /hec1/if_configuration_c=>sc_association-lt_backup_datacenter-lt_backup_class
                                                      IMPORTING et_data        = lt_longt_backup_cl                                                           ).

                  ENDIF.

                  " select assigned class node
                  ASSIGN lt_longt_backup_cl[ hec_node_lt_backup_class = lr_tier_lt_backup->hec_tlt_backup_cl_node_ref ] TO FIELD-SYMBOL(<fs_longterm_backup_cl>).
                  IF ( <fs_longterm_backup_cl> IS ASSIGNED ).
                    lr_tier_lt_backup->* = VALUE #( BASE lr_tier_lt_backup->*
                                                 hec_tlt_backup_ref_descr       = <fs_longterm_backup_cl>-hec_ltb_class_descr
                                                 hec_tlt_backup_ref_descr_ext   = <fs_longterm_backup_cl>-hec_ltb_class_descr_ext
                                                 hec_tree_descr                 = |{ <fs_longterm_backup_cl>-hec_ltb_class_descr } : { lr_tier_lt_backup->hec_tlt_backup_ref_descr_ext }| ).

                    lv_data_changed = abap_true.
                  ENDIF.
                ENDIF.

                " Reset Service Description
                IF ( lr_tier_lt_backup->hec_tlt_backup_cl_node_ref IS INITIAL ).

                  CLEAR: lr_tier_lt_backup->hec_tlt_backup_ref_descr_ext.
                  CLEAR: lr_tier_lt_backup->hec_tlt_backup_ref_descr.

                  lv_data_changed = abap_true.
                ENDIF.

                IF ( <fs_lt_backup_before>-hec_tlt_backup_ref_descr_ext <> lr_tier_lt_backup->hec_tlt_backup_ref_descr_ext ).
                  lr_tier_lt_backup->hec_tree_descr = COND #( WHEN lr_tier_lt_backup->hec_tlt_backup_ref_descr IS NOT INITIAL
                                                     THEN |{ lr_tier_lt_backup->hec_tlt_backup_ref_descr } : { lr_tier_lt_backup->hec_tlt_backup_ref_descr_ext }|
                                                     ELSE |{ lr_tier_lt_backup->hec_tlt_backup_ref_descr_ext }|  ).
                  lv_data_changed = abap_true.
                ENDIF.

                IF ( <fs_lt_backup_before>-hec_tlt_backup_ref_descr <> lr_tier_lt_backup->hec_tlt_backup_ref_descr ).
                  lr_tier_lt_backup->hec_tree_descr = COND #( WHEN lr_tier_lt_backup->hec_tlt_backup_ref_descr IS NOT INITIAL
                                                     THEN |{ lr_tier_lt_backup->hec_tlt_backup_ref_descr } : { lr_tier_lt_backup->hec_tlt_backup_ref_descr_ext }|
                                                     ELSE |{ lr_tier_lt_backup->hec_tlt_backup_ref_descr_ext }|  ).
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF ( lr_tier_lt_backup->hec_phase_guid NE <fs_lt_backup_before>-hec_phase_guid ).

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_tier_lt_backup->key
                                  hec_phase_guid_new = lr_tier_lt_backup->hec_phase_guid
                                  hec_phase_guid_old = <fs_lt_backup_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_tier_lt_backup->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "phasing changed
              ENDIF. " IF <fs_lt_backup_before> IS ASSIGNED.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_tier_lt_backup->hec_tlt_backup_cl_node_ref IS NOT INITIAL AND
                                                                             lr_tier_lt_backup->hec_phase_guid           IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF ( lv_inst_status <> lr_tier_lt_backup->hec_instance_status ).
                lr_tier_lt_backup->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_tier_lt_backup->key
                                   is_data = lr_tier_lt_backup      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN: <fs_lt_backup_before>,
                        <fs_longterm_backup_cl>.
            ENDLOOP.

            "-----------------------------------
            " Update Phasing
            "-----------------------------------
            IF ( lt_act_param_phasing IS NOT INITIAL ).
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.

            " **********************************
            " Update mode after tier update
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier_longterm_backup-update_after_tier.

            " Get tier
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier_longterm_backup-to_parent
                                              IMPORTING et_data        = lt_tier                                                        ).


            LOOP AT lt_tier_lt_backup REFERENCE INTO lr_tier_lt_backup.

              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_tier_lt_backup->hec_tlt_backup_cl_node_ref IS NOT INITIAL AND
                                                                       lr_tier_lt_backup->hec_phase_guid          IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              " Check instance status and switch
              IF ( lv_inst_status <> lr_tier_lt_backup->hec_instance_status ).
                lr_tier_lt_backup->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.


              ASSIGN lt_tier[ key = lr_tier_lt_backup->parent_key ] TO <fs_tier>.

              IF ( <fs_tier> IS ASSIGNED ).
                IF <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                   <fs_tier>-hec_tier_type_value      IS NOT INITIAL AND
                   <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              " Release instance for selection
              IF ( lv_release <> lr_tier_lt_backup->hec_row_selectable ).
                lr_tier_lt_backup->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_tier_lt_backup->key
                                   is_data = lr_tier_lt_backup      ).
              ENDIF.

              UNASSIGN <fs_tier>.
              CLEAR: lv_release,
                     lv_data_changed.
            ENDLOOP.
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
             EXPORTING iv_node = is_ctx-node_key
                       it_key  = it_key
             IMPORTING et_data = <lt_data> ).

    ENDIF.

    IF <lt_data> IS NOT ASSIGNED OR <lt_data> IS INITIAL.
      RETURN.
    ENDIF.

    CASE is_ctx-det_key.
      WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_datacenter-create.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_lt_backup_dc_ct IN CORRESPONDING  /hec1/t_data_lt_backup_dc_ct( <lt_data> )
                                                                                                  ( VALUE #( parent_node_key     = wa_lt_backup_dc_ct-parent_key
                                                                                                             node_key            = wa_lt_backup_dc_ct-key
                                                                                                             hec_instance_status = wa_lt_backup_dc_ct-hec_instance_status
                                                                                                             hec_tree_descr      = wa_lt_backup_dc_ct-hec_tree_descr
                                                                                                             hec_row_selectable  = abap_true
                                                                                                             hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-lt_backup_dc
                                                                                                             hec_phase_guid      = wa_lt_backup_dc_ct-hec_phase_guid
                                                                                                             hec_delete_visible  = wa_lt_backup_dc_ct-hec_delete_visible
                                                                                                             change_request      = wa_lt_backup_dc_ct-change_request ) ) ) ).
      WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_datacenter-update.
        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_lt_backup_dc_ct IN CORRESPONDING  /hec1/t_data_lt_backup_dc_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_lt_backup_dc_ct-parent_key
                                                                                                                    node_key            = wa_lt_backup_dc_ct-key
                                                                                                                    hec_instance_status = wa_lt_backup_dc_ct-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_lt_backup_dc_ct-hec_tree_descr
                                                                                                                    hec_row_selectable  = abap_true
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-lt_backup_dc
                                                                                                                    hec_phase_guid      = wa_lt_backup_dc_ct-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_lt_backup_dc_ct-hec_delete_visible
                                                                                                                    change_request      = wa_lt_backup_dc_ct-change_request ) ) ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_class-create.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_longterm_backup_clas IN CORRESPONDING /hec1/t_data_lt_backup_cl_ct( <lt_data> )
                                                                                                 ( VALUE #( parent_node_key     = wa_longterm_backup_clas-parent_key
                                                                                                            node_key            = wa_longterm_backup_clas-key
                                                                                                            hec_instance_status = wa_longterm_backup_clas-hec_instance_status
                                                                                                            hec_tree_descr      = wa_longterm_backup_clas-hec_tree_descr
                                                                                                            hec_row_selectable  = abap_true
                                                                                                            hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-lt_backup_class
                                                                                                            hec_phase_guid      = wa_longterm_backup_clas-hec_phase_guid
                                                                                                            hec_delete_visible  = wa_longterm_backup_clas-hec_delete_visible
                                                                                                            change_request      = wa_longterm_backup_clas-change_request ) ) ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_class-update.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_longterm_backup_clas IN CORRESPONDING /hec1/t_data_lt_backup_cl_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_longterm_backup_clas-parent_key
                                                                                                                    node_key            = wa_longterm_backup_clas-key
                                                                                                                    hec_instance_status = wa_longterm_backup_clas-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_longterm_backup_clas-hec_tree_descr
                                                                                                                    hec_row_selectable  = abap_true
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-lt_backup_class
                                                                                                                    hec_phase_guid      = wa_longterm_backup_clas-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_longterm_backup_clas-hec_delete_visible
                                                                                                                    change_request      = wa_longterm_backup_clas-change_request ) ) ) ).


      WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_amount-create.
        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_longterm_backup_amount IN CORRESPONDING /hec1/s_lt_backup_amount_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_longterm_backup_amount-parent_key
                                                                                                                    node_key            = wa_longterm_backup_amount-key
                                                                                                                    hec_instance_status = wa_longterm_backup_amount-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_longterm_backup_amount-hec_tree_descr
                                                                                                                    hec_row_selectable  = abap_true
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-lt_backup_amount
                                                                                                                    hec_phase_guid      = wa_longterm_backup_amount-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_longterm_backup_amount-hec_delete_visible
                                                                                                                    change_request      = wa_longterm_backup_amount-change_request ) ) ) ).
      WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_amount-update.
        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_longterm_backup_amount IN CORRESPONDING /hec1/s_lt_backup_amount_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_longterm_backup_amount-parent_key
                                                                                                                    node_key            = wa_longterm_backup_amount-key
                                                                                                                    hec_instance_status = wa_longterm_backup_amount-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_longterm_backup_amount-hec_tree_descr
                                                                                                                    hec_row_selectable  = abap_true
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-lt_backup_amount
                                                                                                                    hec_phase_guid      = wa_longterm_backup_amount-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_longterm_backup_amount-hec_delete_visible
                                                                                                                    change_request      = wa_longterm_backup_amount-change_request ) ) ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-add_storage_datacenter-create.
        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_add_storage_dc_ct IN CORRESPONDING /hec1/t_add_storage_dc_ct( <lt_data> )
                                                                                                  ( VALUE #( parent_node_key     = wa_add_storage_dc_ct-parent_key
                                                                                                             node_key            = wa_add_storage_dc_ct-key
                                                                                                             hec_instance_status = wa_add_storage_dc_ct-hec_instance_status
                                                                                                             hec_tree_descr      = wa_add_storage_dc_ct-hec_tree_descr
                                                                                                             hec_row_selectable  = abap_true
                                                                                                             hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-astorage_dc
                                                                                                             hec_phase_guid      = wa_add_storage_dc_ct-hec_phase_guid
                                                                                                             hec_delete_visible  = wa_add_storage_dc_ct-hec_delete_visible
                                                                                                             change_request      = wa_add_storage_dc_ct-change_request ) ) ) ).
      WHEN /hec1/if_configuration_c=>sc_determination-add_storage_datacenter-update.
        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_add_storage_dc_ct IN CORRESPONDING  /hec1/t_add_storage_dc_ct( <lt_data> )
                                                                                                                 ( VALUE #( parent_node_key     = wa_add_storage_dc_ct-parent_key
                                                                                                                            node_key            = wa_add_storage_dc_ct-key
                                                                                                                            hec_instance_status = wa_add_storage_dc_ct-hec_instance_status
                                                                                                                            hec_tree_descr      = wa_add_storage_dc_ct-hec_tree_descr
                                                                                                                            hec_row_selectable  = abap_true
                                                                                                                            hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-astorage_dc
                                                                                                                            hec_phase_guid      = wa_add_storage_dc_ct-hec_phase_guid
                                                                                                                            hec_delete_visible  = wa_add_storage_dc_ct-hec_delete_visible
                                                                                                                            change_request      = wa_add_storage_dc_ct-change_request ) ) ) ).
      WHEN /hec1/if_configuration_c=>sc_determination-add_storage_class-create.
        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_add_storage_cl_ct IN CORRESPONDING /hec1/t_add_storage_class_ct( <lt_data> )
                                                                                                  ( VALUE #( parent_node_key     = wa_add_storage_cl_ct-parent_key
                                                                                                             node_key            = wa_add_storage_cl_ct-key
                                                                                                             hec_instance_status = wa_add_storage_cl_ct-hec_instance_status
                                                                                                             hec_tree_descr      = wa_add_storage_cl_ct-hec_tree_descr
                                                                                                             hec_row_selectable  = abap_true
                                                                                                             hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-astorage_class
                                                                                                             hec_phase_guid      = wa_add_storage_cl_ct-hec_phase_guid
                                                                                                             hec_delete_visible  = wa_add_storage_cl_ct-hec_delete_visible
                                                                                                             change_request      = wa_add_storage_cl_ct-change_request ) ) ) ).
      WHEN /hec1/if_configuration_c=>sc_determination-add_storage_class-update.
        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_add_storage_cl_ct IN CORRESPONDING  /hec1/t_add_storage_class_ct( <lt_data> )
                                                                                                                 ( VALUE #( parent_node_key     = wa_add_storage_cl_ct-parent_key
                                                                                                                            node_key            = wa_add_storage_cl_ct-key
                                                                                                                            hec_instance_status = wa_add_storage_cl_ct-hec_instance_status
                                                                                                                            hec_tree_descr      = wa_add_storage_cl_ct-hec_tree_descr
                                                                                                                            hec_row_selectable  = abap_true
                                                                                                                            hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-astorage_class
                                                                                                                            hec_phase_guid      = wa_add_storage_cl_ct-hec_phase_guid
                                                                                                                            hec_delete_visible  = wa_add_storage_cl_ct-hec_delete_visible
                                                                                                                            change_request      = wa_add_storage_cl_ct-change_request ) ) ) ).
      WHEN /hec1/if_configuration_c=>sc_determination-add_storage_amount-create.
        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_add_storage_am_ct IN CORRESPONDING /hec1/t_add_storage_amount_ct( <lt_data> )
                                                                                                  ( VALUE #( parent_node_key     = wa_add_storage_am_ct-parent_key
                                                                                                             node_key            = wa_add_storage_am_ct-key
                                                                                                             hec_instance_status = wa_add_storage_am_ct-hec_instance_status
                                                                                                             hec_tree_descr      = wa_add_storage_am_ct-hec_tree_descr
                                                                                                             hec_row_selectable  = abap_true
                                                                                                             hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-astorage_amount
                                                                                                             hec_phase_guid      = wa_add_storage_am_ct-hec_phase_guid
                                                                                                             hec_delete_visible  = wa_add_storage_am_ct-hec_delete_visible
                                                                                                             change_request      = wa_add_storage_am_ct-change_request ) ) ) ).
      WHEN /hec1/if_configuration_c=>sc_determination-add_storage_amount-update.
        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_add_storage_am_ct IN CORRESPONDING /hec1/t_add_storage_amount_ct( <lt_data> )
                                                                                                                 ( VALUE #( parent_node_key     = wa_add_storage_am_ct-parent_key
                                                                                                                            node_key            = wa_add_storage_am_ct-key
                                                                                                                            hec_instance_status = wa_add_storage_am_ct-hec_instance_status
                                                                                                                            hec_tree_descr      = wa_add_storage_am_ct-hec_tree_descr
                                                                                                                            hec_row_selectable  = abap_true
                                                                                                                            hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-astorage_amount
                                                                                                                            hec_phase_guid      = wa_add_storage_am_ct-hec_phase_guid
                                                                                                                            hec_delete_visible  = wa_add_storage_am_ct-hec_delete_visible
                                                                                                                            change_request      = wa_add_storage_am_ct-change_request ) ) ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-tier_longterm_backup-create.
        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( VALUE #( FOR wa_tier_lt_backup IN CORRESPONDING  /hec1/t_data_tier_lt_backup_ct( <lt_data> )
                                                                                                          ( VALUE #( parent_node_key     = wa_tier_lt_backup-parent_key
                                                                                                                     node_key            = wa_tier_lt_backup-key
                                                                                                                     hec_instance_status = wa_tier_lt_backup-hec_instance_status
                                                                                                                     hec_tree_descr      = wa_tier_lt_backup-hec_tree_descr
                                                                                                                     hec_row_selectable  = wa_tier_lt_backup-hec_row_selectable
                                                                                                                     hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-tier_ltbup
                                                                                                                     hec_phase_guid      = wa_tier_lt_backup-hec_phase_guid
                                                                                                                     hec_delete_visible  = wa_tier_lt_backup-hec_delete_visible
                                                                                                                     change_request      = wa_tier_lt_backup-change_request ) ) ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-tier_longterm_backup-update
        OR /hec1/if_configuration_c=>sc_determination-tier_longterm_backup-update_after_tier.

        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( VALUE #( FOR wa_tier_lt_backup IN CORRESPONDING  /hec1/t_data_tier_lt_backup_ct( <lt_data> )
                                                                                                         ( VALUE #( parent_node_key     = wa_tier_lt_backup-parent_key
                                                                                                                    node_key            = wa_tier_lt_backup-key
                                                                                                                    hec_instance_status = wa_tier_lt_backup-hec_instance_status
                                                                                                                    hec_tree_descr      = wa_tier_lt_backup-hec_tree_descr
                                                                                                                    hec_row_selectable  = wa_tier_lt_backup-hec_row_selectable
                                                                                                                    hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-tier_ltbup
                                                                                                                    hec_phase_guid      = wa_tier_lt_backup-hec_phase_guid
                                                                                                                    hec_delete_visible  = wa_tier_lt_backup-hec_delete_visible
                                                                                                                    change_request      = wa_tier_lt_backup-change_request ) ) ) ).

    ENDCASE.


  ENDMETHOD.


  METHOD determine_lt_backup_amount_cr.

    DATA: lt_longterm_backup_amount     TYPE /hec1/t_lt_backup_amount_ct,
          lt_longterm_backup_bef_amount TYPE /hec1/t_lt_backup_amount_ct,
          lr_longterm_backup_amount     TYPE REF TO  /hec1/s_lt_backup_amount_cs,
          lt_phase                      TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing          TYPE TABLE OF /hec1/s_act_phase_inherit.

    CLEAR:
        eo_message,
        et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_longterm_backup_amount  ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_amount-create.

            LOOP AT lt_longterm_backup_amount REFERENCE INTO lr_longterm_backup_amount.
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_longterm_backup_amount->hec_ltb_class_guid      IS NOT INITIAL AND
                                                                             lr_longterm_backup_amount->hec_ltb_datacenter_guid IS NOT INITIAL AND
                                                                             lr_longterm_backup_amount->hec_phase_guid         IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              lr_longterm_backup_amount->hec_delete_visible = abap_true.

              " Check instance status and switch
              IF ( lv_inst_status <> lr_longterm_backup_amount->hec_instance_status ).
                lr_longterm_backup_amount->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node           = is_ctx-node_key
                                   iv_key            = lr_longterm_backup_amount->key
                                   is_data           = lr_longterm_backup_amount      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP.

*            " ***************************************************************************
*            " update mode
*            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_amount-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_longterm_backup_bef_amount  ).

            io_read->retrieve_by_association( EXPORTING iv_node         = /hec1/if_configuration_c=>sc_node-root
                                                        it_key          = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data    = abap_true
                                                        iv_association  = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data         = lt_phase ).

            LOOP AT lt_longterm_backup_amount REFERENCE INTO lr_longterm_backup_amount.


              ASSIGN lt_longterm_backup_bef_amount[ key = lr_longterm_backup_amount->key ] TO FIELD-SYMBOL(<fs_longterm_backup_befor>).

              IF ( <fs_longterm_backup_befor> IS ASSIGNED ).
                TRY.


                    " if the infrastructure provider is set and there is datacenter assigned
                    " get the pricing
                    IF ( lr_dlvy_unit->hec_inf_provider_guid IS NOT INITIAL ) AND ( lr_longterm_backup_amount->hec_ltb_datacenter_guid IS NOT INITIAL ).
                      DATA(ls_datacenter) = VALUE #( lt_datacenter[ hec_node_datacenter = lr_longterm_backup_amount->hec_ltb_datacenter_guid ] OPTIONAL ).

                      SELECT SINGLE hec_cb_pricing_lb_guid INTO @DATA(lv_ltb_legoblock)
                        FROM /hec1/a_back_lb
                       WHERE hec_apm_guid            = @lr_longterm_backup_amount->hec_apm_guid
                         AND hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid
                         AND hec_sec_datacenter_guid = @ls_datacenter-hec_datacenter_guid
                         AND hec_backup_class_guid   = @lr_longterm_backup_amount->hec_ltb_class_guid.

                      " Get pricing
                      SELECT SINGLE * INTO @DATA(ls_pricing) "#EC CI_ALL_FIELDS_NEEDED
                         FROM /hec1/c_cbp_lb
                        WHERE hec_price_lb = @lv_ltb_legoblock.
                      IF ( sy-subrc = 0 ).

                        DATA(lv_exchange_rate) = lr_longterm_backup_amount->hec_exchange_rate. "Temp field because the ls_pricing structure overwrites the real exchange_rate

                        lr_longterm_backup_amount->* = VALUE #( BASE lr_longterm_backup_amount->*
                             hec_tree_descr           = COND #( WHEN lr_longterm_backup_amount->hec_phase_guid IS INITIAL
                                                                THEN |{ VALUE #( lt_phase[ hec_node_phase = lr_longterm_backup_amount->hec_phase_guid ]-hec_phase_descr OPTIONAL ) } : { lr_longterm_backup_amount->hec_ltb_amount }|
                                                                ELSE |{ lr_longterm_backup_amount->hec_ltb_amount }| )
                             hec_month_price_fee      = lr_longterm_backup_amount->hec_ltb_amount * ls_pricing-hec_month_price_eur
*                             price                    = CORRESPONDING #( ls_pricing )
                             price                   = CORRESPONDING #( BASE ( lr_longterm_backup_amount->price ) ls_pricing )
                             hec_exchange_rate        = lv_exchange_rate
                        ).
                        lv_data_changed = abap_true.
                      ENDIF.

                      lv_data_changed = abap_true.
                    ENDIF. " IF lv_infra_provider IS NOT INITIAL.
                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF ( lr_longterm_backup_amount->hec_phase_guid NE <fs_longterm_backup_befor>-hec_phase_guid ).

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_longterm_backup_amount->key
                                  hec_phase_guid_new = lr_longterm_backup_amount->hec_phase_guid
                                  hec_phase_guid_old = <fs_longterm_backup_befor>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_longterm_backup_amount->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "Phase changed
              ENDIF. "<fs_longterm_backup_befor> is assigned


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_longterm_backup_amount->hec_ltb_class_guid      IS NOT INITIAL AND
                                                                       lr_longterm_backup_amount->hec_ltb_datacenter_guid IS NOT INITIAL AND
                                                                       lr_longterm_backup_amount->hec_phase_guid          IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              lr_longterm_backup_amount->hec_delete_visible = abap_true.

              IF ( lv_inst_status <> lr_longterm_backup_amount->hec_instance_status ).
                lr_longterm_backup_amount->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node           = is_ctx-node_key
                                   iv_key            = lr_longterm_backup_amount->key
                                   is_data           = lr_longterm_backup_amount      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_longterm_backup_befor>.

            ENDLOOP. "LOOP AT lt_add_service REFERENCE INTO lr_add_service.

            "-----------------------------------
            " Update Phasing
            "-----------------------------------
            IF ( lt_act_param_phasing IS NOT INITIAL ).
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.
*
        ENDCASE.
*

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD determine_lt_backup_class_cr.
    DATA: lt_longterm_backup_class     TYPE /hec1/t_data_lt_backup_cl_ct,
          lt_longterm_backup_cl_before TYPE /hec1/t_data_lt_backup_cl_ct,
          lr_longterm_backup_cl        TYPE REF TO /hec1/s_data_lt_backup_cl_cs,
          lt_phase                     TYPE /hec1/t_data_phase_ct,
          ls_act_param_tier_ltb        TYPE /hec1/s_act_update_tier_ltb.

    CLEAR:
        eo_message,
        et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_longterm_backup_class  ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_class-create.

            LOOP AT lt_longterm_backup_class REFERENCE INTO lr_longterm_backup_cl.
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_longterm_backup_cl->hec_ltb_class_guid      IS NOT INITIAL AND
                                                                             lr_longterm_backup_cl->hec_ltb_datacenter_guid IS NOT INITIAL
*                                                                             lr_longterm_backup_cl->hec_phase_guid         IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              lr_longterm_backup_cl->hec_delete_visible = abap_true.

              " Check instance status and switch
              IF ( lv_inst_status <> lr_longterm_backup_cl->hec_instance_status ).
                lr_longterm_backup_cl->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node           = is_ctx-node_key
                                   iv_key            = lr_longterm_backup_cl->key
                                   is_data           = lr_longterm_backup_cl      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP.

*            " ***************************************************************************
*            " update mode
*            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_class-update.

            CLEAR: ls_act_param_tier_ltb.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_longterm_backup_cl_before  ).

            io_read->retrieve_by_association( EXPORTING iv_node         = /hec1/if_configuration_c=>sc_node-root
                                                        it_key          = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data    = abap_true
                                                        iv_association  = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data         = lt_phase ).

            LOOP AT lt_longterm_backup_class REFERENCE INTO lr_longterm_backup_cl.


              ASSIGN lt_longterm_backup_cl_before[ key = lr_longterm_backup_cl->key ] TO FIELD-SYMBOL(<fs_longterm_backup_before>).

              IF ( <fs_longterm_backup_before> IS ASSIGNED ).

                "-----------------------------------
                " Longterm backup GUID has changed
                "-----------------------------------
                " Get service class data
                SELECT SINGLE hec_longt_backup_class_descr INTO @DATA(lv_longterm_description)
                  FROM /hec1/i_longtermbackupbasic
                 WHERE hec_apm_guid                = @lr_landscape->hec_apm_guid
                   AND hec_longt_backup_class_guid = @lr_longterm_backup_cl->hec_ltb_class_guid.
                IF ( sy-subrc = 0 ).
                  lr_longterm_backup_cl->* = VALUE #( BASE lr_longterm_backup_cl->*
                                                       hec_ltb_class_descr     = lv_longterm_description
                                                                                                         ).
                  "Set longterm backup description in case it is empty
                  IF ( lr_longterm_backup_cl->hec_ltb_class_guid IS NOT INITIAL  ) AND
                     ( lr_longterm_backup_cl->hec_ltb_class_descr IS NOT INITIAL ) AND
                     ( lr_longterm_backup_cl->hec_ltb_class_descr_ext IS INITIAL ).
                    lr_longterm_backup_cl->hec_ltb_class_descr_ext = lr_longterm_backup_cl->hec_ltb_class_descr.
                  ENDIF.

                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Resets -> TODO move to actions
                "-----------------------------------
                " Reset Service Description
                IF ( lr_longterm_backup_cl->hec_ltb_class_guid IS INITIAL ).
                  IF ( lr_longterm_backup_cl->hec_ltb_class_descr = lr_longterm_backup_cl->hec_ltb_class_descr_ext ).
                    CLEAR: lr_longterm_backup_cl->hec_ltb_class_descr_ext.
                  ENDIF.
                  CLEAR: lr_longterm_backup_cl->hec_ltb_class_descr.

                  lv_data_changed = abap_true.
                ENDIF.

                IF ( <fs_longterm_backup_before>-hec_ltb_class_descr_ext <> lr_longterm_backup_cl->hec_ltb_class_descr_ext ).
                  lr_longterm_backup_cl->hec_tree_descr = COND #( WHEN lr_longterm_backup_cl->hec_ltb_class_descr IS NOT INITIAL
                                                     THEN |{ lr_longterm_backup_cl->hec_ltb_class_descr } : { lr_longterm_backup_cl->hec_ltb_class_descr_ext }|
                                                     ELSE |{ lr_longterm_backup_cl->hec_ltb_class_descr_ext }|  ).
                  lv_data_changed = abap_true.
                ENDIF.

                IF ( <fs_longterm_backup_before>-hec_ltb_class_descr <> lr_longterm_backup_cl->hec_ltb_class_descr ).
                  lr_longterm_backup_cl->hec_tree_descr = COND #( WHEN lr_longterm_backup_cl->hec_ltb_class_descr IS NOT INITIAL
                                                     THEN |{ lr_longterm_backup_cl->hec_ltb_class_descr } : { lr_longterm_backup_cl->hec_ltb_class_descr_ext }|
                                                     ELSE |{ lr_longterm_backup_cl->hec_ltb_class_descr_ext }|  ).
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Check instance status and switch
                "-----------------------------------
                lv_inst_status = COND /hec1/config_instance_status( WHEN lr_longterm_backup_cl->hec_ltb_class_guid      IS NOT INITIAL AND
                                                                         lr_longterm_backup_cl->hec_ltb_datacenter_guid IS NOT INITIAL
                                                                    THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                    ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

                lr_longterm_backup_cl->hec_delete_visible = abap_true.

                IF ( lv_inst_status <> lr_longterm_backup_cl->hec_instance_status ).
                  lr_longterm_backup_cl->hec_instance_status = lv_inst_status.
                  lv_data_changed = abap_true.
                ENDIF.

                " check, if assigned tier_lt_backup nodes must be updated
                IF ( lr_longterm_backup_cl->hec_ltb_class_guid <> <fs_longterm_backup_before>-hec_ltb_class_guid )
                OR ( lr_longterm_backup_cl->hec_ltb_class_descr_ext <> <fs_longterm_backup_before>-hec_ltb_class_descr_ext ).

                  ls_act_param_tier_ltb  = CORRESPONDING /hec1/s_act_update_tier_ltb( lr_longterm_backup_cl->* ).
                ENDIF.

                """"""""""""""""""""""""""""""""""""""""""""""""""""""
                " Update TIER_LT_BACKUP
                """"""""""""""""""""""""""""""""""""""""""""""""""""""

                IF ( ls_act_param_tier_ltb IS NOT INITIAL ).
                  me->mr_act_param_tier_ltb = NEW /hec1/s_act_update_tier_ltb( ls_act_param_tier_ltb ).

                  /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                      is_ctx          = CORRESPONDING #( is_ctx )
                      it_key          = it_key
                      iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_tier_lt_backup )
                      iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                      ir_act_param    = me->mr_act_param_tier_ltb ).
                ENDIF.


                IF ( lv_data_changed = abap_true ).
                  io_modify->update( iv_node           = is_ctx-node_key
                                     iv_key            = lr_longterm_backup_cl->key
                                     is_data           = lr_longterm_backup_cl      ).
                ENDIF.

                CLEAR: lv_inst_status,
                       lv_data_changed.
              ENDIF.
              UNASSIGN <fs_longterm_backup_before>.

            ENDLOOP. "LOOP AT lt_add_service REFERENCE INTO lr_add_service.

            "-----------------------------------
            " Update Phasing
            "-----------------------------------
*            IF ( lt_act_param_phasing IS NOT INITIAL ).
*              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).
*
*              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
*                  is_ctx          = CORRESPONDING #( is_ctx )
*                  it_key          = it_key
*                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
*                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
*                  ir_act_param    = me->mr_act_param_phasing ).
*            ENDIF.
*
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.
  ENDMETHOD.


  METHOD determine_lt_backup_datacen_cr.
    DATA: lt_longterm_backup_dc        TYPE /hec1/t_data_lt_backup_dc_ct,
          lt_longterm_backup_dc_before TYPE /hec1/t_data_lt_backup_dc_ct,
          lr_longterm_backup_dc        TYPE REF TO /hec1/s_data_lt_backup_dc_cs,
          lt_phase                     TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing         TYPE TABLE OF /hec1/s_act_phase_inherit.

    CLEAR:
        eo_message,
        et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_longterm_backup_dc  ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_datacenter-create.

            LOOP AT lt_longterm_backup_dc REFERENCE INTO lr_longterm_backup_dc.
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_longterm_backup_dc->hec_ltb_datacenter_guid IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              lr_longterm_backup_dc->hec_delete_visible = abap_true.

              " Check instance status and switch
              IF ( lv_inst_status <> lr_longterm_backup_dc->hec_instance_status ).
                lr_longterm_backup_dc->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node           = is_ctx-node_key
                                   iv_key            = lr_longterm_backup_dc->key
                                   is_data           = lr_longterm_backup_dc      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP.

*            " ***************************************************************************
*            " update mode
*            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_datacenter-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_longterm_backup_dc_before  ).

            io_read->retrieve_by_association( EXPORTING iv_node         = /hec1/if_configuration_c=>sc_node-root
                                                        it_key          = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data    = abap_true
                                                        iv_association  = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data         = lt_phase ).

            LOOP AT lt_longterm_backup_dc REFERENCE INTO lr_longterm_backup_dc.


              ASSIGN lt_longterm_backup_dc_before[ key = lr_longterm_backup_dc->key ] TO FIELD-SYMBOL(<fs_longterm_backup_dc_before>).

              IF ( <fs_longterm_backup_dc_before> IS ASSIGNED ).
*                   " if the infrastructure provider is set and there is datacenter assigned
                IF ( lr_dlvy_unit->hec_inf_provider_guid IS NOT INITIAL ).

                  DATA(ls_datacenter) = VALUE #( lt_datacenter[ hec_node_datacenter = lr_longterm_backup_dc->hec_ltb_datacenter_guid ] OPTIONAL ).
                  lr_longterm_backup_dc->* = VALUE #( BASE lr_longterm_backup_dc->*
                                                   hec_ltb_datacenter_guid  = ls_datacenter-hec_node_datacenter
                                                   hec_ltb_datacenter_descr = COND #( WHEN ls_datacenter-hec_datacenter_descr IS NOT INITIAL
                                                                                      THEN ls_datacenter-hec_datacenter_descr
                                                                                      ELSE space                                            )
                                                   hec_tree_descr           = COND #( WHEN ls_datacenter-hec_datacenter_guid IS NOT INITIAL
                                                                                      THEN |{ ls_datacenter-hec_datacenter_descr }|
                                                                                      ELSE |<new datacenter>| )
                  ).
                  lv_data_changed = abap_true.
                ENDIF.

*                "-----------------------------------
*                " Phasing has changed
*                "-----------------------------------
*                IF ( lr_longterm_backup_dc->hec_phase_guid NE <fs_longterm_backup_dc_before>-hec_phase_guid ).
*
*                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
*                                  hec_bopf_key       = lr_longterm_backup_dc->key
*                                  hec_phase_guid_new = lr_longterm_backup_dc->hec_phase_guid
*                                  hec_phase_guid_old = <fs_longterm_backup_dc_before>-hec_phase_guid ) TO lt_act_param_phasing.
*
*                  lr_longterm_backup_dc->hec_phase_changed = abap_true.
*                  lv_data_changed = abap_true.
*
*                ENDIF. "Phase changed

                " Reset Datacenter
                IF ( <fs_longterm_backup_dc_before>-hec_ltb_datacenter_guid IS NOT INITIAL ) AND ( lr_longterm_backup_dc->hec_ltb_datacenter_guid IS INITIAL ).
                  CLEAR: lr_longterm_backup_dc->hec_ltb_datacenter_descr.

                  lv_data_changed = abap_true.
                ENDIF.

                " Set Datacenter Descr / Tree Descr
                IF ( <fs_longterm_backup_dc_before>-hec_ltb_datacenter_descr NE lr_longterm_backup_dc->hec_ltb_datacenter_descr ).
                  lr_longterm_backup_dc->hec_tree_descr          = COND #( WHEN lr_longterm_backup_dc->hec_ltb_datacenter_descr IS INITIAL
                                                                           THEN ||
                                                                           ELSE |{ lr_longterm_backup_dc->hec_ltb_datacenter_descr }| ).

                  lv_data_changed = abap_true.
                ENDIF.

              ENDIF.


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_longterm_backup_dc->hec_ltb_datacenter_guid IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              lr_longterm_backup_dc->hec_delete_visible = abap_true.

              IF ( lv_inst_status <> lr_longterm_backup_dc->hec_instance_status ).
                lr_longterm_backup_dc->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node           = is_ctx-node_key
                                   iv_key            = lr_longterm_backup_dc->key
                                   is_data           = lr_longterm_backup_dc      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_longterm_backup_dc_before>.

            ENDLOOP. "LOOP AT lt_add_service REFERENCE INTO lr_add_service.

            "-----------------------------------
            " Update Phasing
            "-----------------------------------
*            IF ( lt_act_param_phasing IS NOT INITIAL ).
*              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).
*
*              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
*                  is_ctx          = CORRESPONDING #( is_ctx )
*                  it_key          = it_key
*                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
*                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
*                  ir_act_param    = me->mr_act_param_phasing ).
*            ENDIF.
*
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD determine_tier_lt_backup_cr.
    DATA: lt_tier_lt_backup        TYPE /hec1/t_data_tier_lt_backup_ct,
          lt_tier_lt_backup_before TYPE /hec1/t_data_tier_lt_backup_ct,
          lt_tier                  TYPE /hec1/t_data_tier_ct,
          lt_root_key              TYPE /bobf/t_frw_key,
          lt_landscape_key         TYPE /bobf/t_frw_key,
          lt_longt_backup_cl       TYPE /hec1/t_data_lt_backup_cl_ct,
          lt_phase                 TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing     TYPE TABLE OF /hec1/s_act_phase_inherit.



    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_tier_lt_backup ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier_longterm_backup-create.

            " Get tier node (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier_longterm_backup-to_parent
                                              IMPORTING et_data        = lt_tier                                                        ).

            LOOP AT lt_tier_lt_backup REFERENCE INTO DATA(lr_tier_lt_backup).
              ASSIGN lt_tier[ key = lr_tier_lt_backup->parent_key ] TO FIELD-SYMBOL(<fs_tier>).

              lr_tier_lt_backup->hec_delete_visible = abap_true.

              IF ( <fs_tier>                          IS ASSIGNED )    AND
                 ( <fs_tier>-hec_tier_descr           IS NOT INITIAL ) AND
                 ( <fs_tier>-hec_tier_type_value      IS NOT INITIAL ) AND
                 ( <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL ).
                DATA(lv_release) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              IF ( lv_release <> lr_tier_lt_backup->hec_row_selectable ).
                lr_tier_lt_backup->hec_row_selectable = lv_release.
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
                  is_node_data = lr_tier_lt_backup
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).


              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_tier_lt_backup->key
                                   is_data = lr_tier_lt_backup      ).
              ENDIF.

              UNASSIGN <fs_tier>.
              CLEAR: lv_data_changed,
                     lv_release.
            ENDLOOP.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier_longterm_backup-update.

            " Data before update
            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_tier_lt_backup_before ).
            " ROOT -> PHASE
            io_read->retrieve_by_association( EXPORTING iv_node         = /hec1/if_configuration_c=>sc_node-root
                                                        it_key          = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data    = abap_true
                                                        iv_association  = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data         = lt_phase ).


            LOOP AT lt_tier_lt_backup REFERENCE INTO lr_tier_lt_backup.

              ASSIGN lt_tier_lt_backup_before[ key = lr_tier_lt_backup->key ] TO FIELD-SYMBOL(<fs_lt_backup_before>).
              IF ( <fs_lt_backup_before> IS ASSIGNED ).

                "-----------------------------------
                " Service Class GUID has changed ?
                "-----------------------------------
                IF ( lr_tier_lt_backup->hec_tlt_backup_cl_node_ref IS NOT INITIAL ) AND
                 ( ( lr_tier_lt_backup->hec_tlt_backup_cl_node_ref <> <fs_lt_backup_before>-hec_tlt_backup_cl_node_ref ) ).

                  " Get service class data from corresponding longterm backup pool
                  IF ( lt_root_key IS INITIAL ).

                    APPEND VALUE #( key = lr_tier_lt_backup->root_key ) TO lt_root_key.

                    " Get longterm backup datacenter
                    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                                it_key         = lt_root_key
                                                                iv_association = /hec1/if_configuration_c=>sc_association-root-lt_backup_datacenter
                                                      IMPORTING et_target_key  = DATA(lt_longt_backup_dc_key)                                      ).
                    " Get longterm backup class
                    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-lt_backup_datacenter
                                                                it_key         = lt_longt_backup_dc_key
                                                                iv_fill_data   = abap_true
                                                                iv_association = /hec1/if_configuration_c=>sc_association-lt_backup_datacenter-lt_backup_class
                                                      IMPORTING et_data        = lt_longt_backup_cl                                                           ).

                  ENDIF.

                  " select assigned class node
                  ASSIGN lt_longt_backup_cl[ hec_node_lt_backup_class = lr_tier_lt_backup->hec_tlt_backup_cl_node_ref ] TO FIELD-SYMBOL(<fs_longterm_backup_cl>).
                  IF ( <fs_longterm_backup_cl> IS ASSIGNED ).
                    lr_tier_lt_backup->* = VALUE #( BASE lr_tier_lt_backup->*
                                                 hec_tlt_backup_ref_descr       = <fs_longterm_backup_cl>-hec_ltb_class_descr
                                                 hec_tlt_backup_ref_descr_ext   = <fs_longterm_backup_cl>-hec_ltb_class_descr_ext
                                                 hec_tree_descr                 = |{ <fs_longterm_backup_cl>-hec_ltb_class_descr } : { lr_tier_lt_backup->hec_tlt_backup_ref_descr_ext }| ).

                    lv_data_changed = abap_true.
                  ENDIF.
                ENDIF.

                " Reset Service Description
                IF ( lr_tier_lt_backup->hec_tlt_backup_cl_node_ref IS INITIAL ).

                  CLEAR: lr_tier_lt_backup->hec_tlt_backup_ref_descr_ext.
                  CLEAR: lr_tier_lt_backup->hec_tlt_backup_ref_descr.

                  lv_data_changed = abap_true.
                ENDIF.

                IF ( <fs_lt_backup_before>-hec_tlt_backup_ref_descr_ext <> lr_tier_lt_backup->hec_tlt_backup_ref_descr_ext ).
                  lr_tier_lt_backup->hec_tree_descr = COND #( WHEN lr_tier_lt_backup->hec_tlt_backup_ref_descr IS NOT INITIAL
                                                     THEN |{ lr_tier_lt_backup->hec_tlt_backup_ref_descr } : { lr_tier_lt_backup->hec_tlt_backup_ref_descr_ext }|
                                                     ELSE |{ lr_tier_lt_backup->hec_tlt_backup_ref_descr_ext }|  ).
                  lv_data_changed = abap_true.
                ENDIF.

                IF ( <fs_lt_backup_before>-hec_tlt_backup_ref_descr <> lr_tier_lt_backup->hec_tlt_backup_ref_descr ).
                  lr_tier_lt_backup->hec_tree_descr = COND #( WHEN lr_tier_lt_backup->hec_tlt_backup_ref_descr IS NOT INITIAL
                                                     THEN |{ lr_tier_lt_backup->hec_tlt_backup_ref_descr } : { lr_tier_lt_backup->hec_tlt_backup_ref_descr_ext }|
                                                     ELSE |{ lr_tier_lt_backup->hec_tlt_backup_ref_descr_ext }|  ).
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF ( lr_tier_lt_backup->hec_phase_guid NE <fs_lt_backup_before>-hec_phase_guid ).

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_tier_lt_backup->key
                                  hec_phase_guid_new = lr_tier_lt_backup->hec_phase_guid
                                  hec_phase_guid_old = <fs_lt_backup_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_tier_lt_backup->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "phasing changed
              ENDIF. " IF <fs_lt_backup_before> IS ASSIGNED.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_tier_lt_backup->hec_tlt_backup_cl_node_ref IS NOT INITIAL AND
                                                                             lr_tier_lt_backup->hec_phase_guid           IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF ( lv_inst_status <> lr_tier_lt_backup->hec_instance_status ).
                lr_tier_lt_backup->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_tier_lt_backup->key
                                   is_data = lr_tier_lt_backup      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN: <fs_lt_backup_before>,
                        <fs_longterm_backup_cl>.
            ENDLOOP.

            "-----------------------------------
            " Update Phasing
            "-----------------------------------
            IF ( lt_act_param_phasing IS NOT INITIAL ).
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.

            " **********************************
            " Update mode after tier update
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier_longterm_backup-update_after_tier.

            " Get tier
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier_longterm_backup-to_parent
                                              IMPORTING et_data        = lt_tier                                                        ).


            LOOP AT lt_tier_lt_backup REFERENCE INTO lr_tier_lt_backup.

              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_tier_lt_backup->hec_tlt_backup_cl_node_ref IS NOT INITIAL AND
                                                                       lr_tier_lt_backup->hec_phase_guid          IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              " Check instance status and switch
              IF ( lv_inst_status <> lr_tier_lt_backup->hec_instance_status ).
                lr_tier_lt_backup->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.


              ASSIGN lt_tier[ key = lr_tier_lt_backup->parent_key ] TO <fs_tier>.

              IF ( <fs_tier> IS ASSIGNED ).
                IF <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                   <fs_tier>-hec_tier_type_value      IS NOT INITIAL AND
                   <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              " Release instance for selection
              IF ( lv_release <> lr_tier_lt_backup->hec_row_selectable ).
                lr_tier_lt_backup->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_tier_lt_backup->key
                                   is_data = lr_tier_lt_backup      ).
              ENDIF.

              UNASSIGN <fs_tier>.
              CLEAR: lv_release,
                     lv_data_changed.
            ENDLOOP.
        ENDCASE.
      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.
  ENDMETHOD.

  METHOD determine_a_storage_datacenter.
    DATA: lt_add_storage_dc        TYPE /hec1/t_add_storage_dc_ct,
          lt_add_storage_dc_before TYPE /hec1/t_add_storage_dc_ct,
          lr_add_storage_dc        TYPE REF TO /hec1/s_add_storage_dc_cs,
          lt_phase                 TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing     TYPE TABLE OF /hec1/s_act_phase_inherit.

    CLEAR:
        eo_message,
        et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_add_storage_dc  ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-add_storage_datacenter-create.

            LOOP AT lt_add_storage_dc REFERENCE INTO lr_add_storage_dc.
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_add_storage_dc->hec_node_datacenter_ref IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              lr_add_storage_dc->hec_delete_visible = abap_true.

              " Check instance status and switch
              IF ( lv_inst_status <> lr_add_storage_dc->hec_instance_status ).
                lr_add_storage_dc->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node           = is_ctx-node_key
                                   iv_key            = lr_add_storage_dc->key
                                   is_data           = lr_add_storage_dc      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP.

*            " ***************************************************************************
*            " update mode
*            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-add_storage_datacenter-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_add_storage_dc_before  ).

            io_read->retrieve_by_association( EXPORTING iv_node         = /hec1/if_configuration_c=>sc_node-root
                                                        it_key          = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data    = abap_true
                                                        iv_association  = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data         = lt_phase ).

            LOOP AT lt_add_storage_dc REFERENCE INTO lr_add_storage_dc.


              ASSIGN lt_add_storage_dc_before[ key = lr_add_storage_dc->key ] TO FIELD-SYMBOL(<fs_add_storage_dc_before>).

              IF ( <fs_add_storage_dc_before> IS ASSIGNED ).
*                   " if the infrastructure provider is set and there is datacenter assigned
                IF ( lr_dlvy_unit->hec_inf_provider_guid IS NOT INITIAL ).

                  DATA(ls_datacenter) = VALUE #( lt_datacenter[ hec_node_datacenter = lr_add_storage_dc->hec_node_datacenter_ref ] OPTIONAL ).
                  lr_add_storage_dc->* = VALUE #( BASE lr_add_storage_dc->*
                                                   hec_node_datacenter_ref  = ls_datacenter-hec_node_datacenter
                                                   hec_datacenter_descr_ref = COND #( WHEN ls_datacenter-hec_datacenter_descr IS NOT INITIAL
                                                                                      THEN ls_datacenter-hec_datacenter_descr
                                                                                      ELSE space                                            )
                                                   hec_tree_descr           = COND #( WHEN ls_datacenter-hec_datacenter_guid IS NOT INITIAL
                                                                                      THEN |{ ls_datacenter-hec_datacenter_descr }|
                                                                                      ELSE |<new datacenter>| )
                  ).
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF ( lr_add_storage_dc->hec_phase_guid NE <fs_add_storage_dc_before>-hec_phase_guid ).

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_add_storage_dc->key
                                  hec_phase_guid_new = lr_add_storage_dc->hec_phase_guid
                                  hec_phase_guid_old = <fs_add_storage_dc_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_add_storage_dc->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "Phase changed

                " Reset Datacenter
                IF ( <fs_add_storage_dc_before>-hec_node_datacenter_ref IS NOT INITIAL ) AND ( lr_add_storage_dc->hec_node_datacenter_ref IS INITIAL ).
                  CLEAR: lr_add_storage_dc->hec_datacenter_descr_ref.

                  lv_data_changed = abap_true.
                ENDIF.

                " Set Datacenter Descr / Tree Descr
                IF ( <fs_add_storage_dc_before>-hec_datacenter_descr_ref NE lr_add_storage_dc->hec_datacenter_descr_ref ).
                  lr_add_storage_dc->hec_tree_descr          = COND #( WHEN lr_add_storage_dc->hec_datacenter_descr_ref IS INITIAL
                                                                           THEN ||
                                                                           ELSE |{ lr_add_storage_dc->hec_datacenter_descr_ref }| ).

                  lv_data_changed = abap_true.
                ENDIF.

              ENDIF.


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_add_storage_dc->hec_node_datacenter_ref IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              lr_add_storage_dc->hec_delete_visible = abap_true.

              IF ( lv_inst_status <> lr_add_storage_dc->hec_instance_status ).
                lr_add_storage_dc->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node           = is_ctx-node_key
                                   iv_key            = lr_add_storage_dc->key
                                   is_data           = lr_add_storage_dc      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_add_storage_dc_before>.

            ENDLOOP. "LOOP AT lt_add_service REFERENCE INTO lr_add_service.

            "-----------------------------------
            " Update Phasing
            "-----------------------------------
            IF ( lt_act_param_phasing IS NOT INITIAL ).
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.

        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.
  ENDMETHOD.

  METHOD determine_a_storage_dcenter_cr.
    DATA: lt_add_storage_dc        TYPE /hec1/t_add_storage_dc_ct,
          lt_add_storage_dc_before TYPE /hec1/t_add_storage_dc_ct,
          lr_add_storage_dc        TYPE REF TO /hec1/s_add_storage_dc_cs,
          lt_phase                 TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing     TYPE TABLE OF /hec1/s_act_phase_inherit.

    CLEAR:
        eo_message,
        et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_add_storage_dc  ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-add_storage_datacenter-create.

            LOOP AT lt_add_storage_dc REFERENCE INTO lr_add_storage_dc.
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_add_storage_dc->hec_node_datacenter_ref IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              lr_add_storage_dc->hec_delete_visible = abap_true.

              " Check instance status and switch
              IF ( lv_inst_status <> lr_add_storage_dc->hec_instance_status ).
                lr_add_storage_dc->hec_instance_status = lv_inst_status.
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
                  is_node_data = lr_add_storage_dc
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              IF lv_data_changed = abap_false.
                lv_data_changed = lv_cr_data_changed.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node           = is_ctx-node_key
                                   iv_key            = lr_add_storage_dc->key
                                   is_data           = lr_add_storage_dc      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP.

*            " ***************************************************************************
*            " update mode
*            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-add_storage_datacenter-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_add_storage_dc_before  ).

            io_read->retrieve_by_association( EXPORTING iv_node         = /hec1/if_configuration_c=>sc_node-root
                                                        it_key          = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data    = abap_true
                                                        iv_association  = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data         = lt_phase ).

            LOOP AT lt_add_storage_dc REFERENCE INTO lr_add_storage_dc.


              ASSIGN lt_add_storage_dc_before[ key = lr_add_storage_dc->key ] TO FIELD-SYMBOL(<fs_add_storage_dc_before>).

              IF ( <fs_add_storage_dc_before> IS ASSIGNED ).
*                   " if the infrastructure provider is set and there is datacenter assigned
                IF ( lr_dlvy_unit->hec_inf_provider_guid IS NOT INITIAL ).

                  DATA(ls_datacenter) = VALUE #( lt_datacenter[ hec_node_datacenter = lr_add_storage_dc->hec_node_datacenter_ref ] OPTIONAL ).
                  lr_add_storage_dc->* = VALUE #( BASE lr_add_storage_dc->*
                                                   hec_node_datacenter_ref  = ls_datacenter-hec_node_datacenter
                                                   hec_datacenter_descr_ref = COND #( WHEN ls_datacenter-hec_datacenter_descr IS NOT INITIAL
                                                                                      THEN ls_datacenter-hec_datacenter_descr
                                                                                      ELSE space                                            )
                                                   hec_tree_descr           = COND #( WHEN ls_datacenter-hec_datacenter_guid IS NOT INITIAL
                                                                                      THEN |{ ls_datacenter-hec_datacenter_descr }|
                                                                                      ELSE |<new datacenter>| )
                  ).
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF ( lr_add_storage_dc->hec_phase_guid NE <fs_add_storage_dc_before>-hec_phase_guid ).

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_add_storage_dc->key
                                  hec_phase_guid_new = lr_add_storage_dc->hec_phase_guid
                                  hec_phase_guid_old = <fs_add_storage_dc_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_add_storage_dc->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "Phase changed

                " Reset Datacenter
                IF ( <fs_add_storage_dc_before>-hec_node_datacenter_ref IS NOT INITIAL ) AND ( lr_add_storage_dc->hec_node_datacenter_ref IS INITIAL ).
                  CLEAR: lr_add_storage_dc->hec_datacenter_descr_ref.

                  lv_data_changed = abap_true.
                ENDIF.

                " Set Datacenter Descr / Tree Descr
                IF ( <fs_add_storage_dc_before>-hec_datacenter_descr_ref NE lr_add_storage_dc->hec_datacenter_descr_ref ).
                  lr_add_storage_dc->hec_tree_descr          = COND #( WHEN lr_add_storage_dc->hec_datacenter_descr_ref IS INITIAL
                                                                           THEN ||
                                                                           ELSE |{ lr_add_storage_dc->hec_datacenter_descr_ref }| ).

                  lv_data_changed = abap_true.
                ENDIF.

              ENDIF.


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_add_storage_dc->hec_node_datacenter_ref IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              lr_add_storage_dc->hec_delete_visible = abap_true.

              IF ( lv_inst_status <> lr_add_storage_dc->hec_instance_status ).
                lr_add_storage_dc->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node           = is_ctx-node_key
                                   iv_key            = lr_add_storage_dc->key
                                   is_data           = lr_add_storage_dc      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_add_storage_dc_before>.

            ENDLOOP. "LOOP AT lt_add_service REFERENCE INTO lr_add_service.

            "-----------------------------------
            " Update Phasing
            "-----------------------------------
            IF ( lt_act_param_phasing IS NOT INITIAL ).
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.

        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.
  ENDMETHOD.

  METHOD determine_a_storage_class.
    DATA: lt_add_storage_class         TYPE /hec1/t_add_storage_class_ct,
          lt_longterm_backup_cl_before TYPE /hec1/t_add_storage_class_ct,
          lr_add_storage_cl            TYPE REF TO /hec1/s_add_storage_class_cs,
          lt_phase                     TYPE /hec1/t_data_phase_ct.
*          ls_act_param_tier_ltb        TYPE /hec1/s_act_update_tier_ltb. "not supported yet

    CLEAR:
        eo_message,
        et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_add_storage_class  ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-add_storage_class-create.

            LOOP AT lt_add_storage_class REFERENCE INTO lr_add_storage_cl.
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_add_storage_cl->hec_astore_class_guid   IS NOT INITIAL AND
                                                                             lr_add_storage_cl->hec_node_datacenter_ref IS NOT INITIAL
*                                                                             lr_add_storage_cl->hec_phase_guid         IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              lr_add_storage_cl->hec_delete_visible = abap_true.

              " Check instance status and switch
              IF ( lv_inst_status <> lr_add_storage_cl->hec_instance_status ).
                lr_add_storage_cl->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node           = is_ctx-node_key
                                   iv_key            = lr_add_storage_cl->key
                                   is_data           = lr_add_storage_cl      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP.

*            " ***************************************************************************
*            " update mode
*            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-add_storage_class-update.

*            CLEAR: ls_act_param_tier_ltb.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_longterm_backup_cl_before  ).

            io_read->retrieve_by_association( EXPORTING iv_node         = /hec1/if_configuration_c=>sc_node-root
                                                        it_key          = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data    = abap_true
                                                        iv_association  = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data         = lt_phase ).

            LOOP AT lt_add_storage_class REFERENCE INTO lr_add_storage_cl.


              ASSIGN lt_longterm_backup_cl_before[ key = lr_add_storage_cl->key ] TO FIELD-SYMBOL(<fs_longterm_backup_before>).

              IF ( <fs_longterm_backup_before> IS ASSIGNED ).

                DATA(ls_datacenter) = VALUE #( lt_datacenter[ hec_node_datacenter = lr_add_storage_cl->hec_node_datacenter_ref ] OPTIONAL ).

                " Get service class data
                SELECT SINGLE hec_shared_storage_descr, hec_cb_pricing_lb_guid INTO @DATA(lv_add_storage_descr)
                  FROM /hec1/a_sha_stor
                 WHERE hec_apm_guid = @lr_add_storage_cl->hec_apm_guid
                   AND hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid
                   AND hec_sec_datacenter_guid = @ls_datacenter-hec_datacenter_guid
                   AND hec_shared_storage_guid = @lr_add_storage_cl->hec_astore_class_guid.
                IF ( sy-subrc = 0 ).
                  lr_add_storage_cl->* = VALUE #( BASE lr_add_storage_cl->*
                                                       hec_astore_class_descr     = lv_add_storage_descr-hec_shared_storage_descr
                                                                                                         ).
                  "Set add storage class description in case it is empty
                  IF ( lr_add_storage_cl->hec_astore_class_guid      IS NOT INITIAL  ) AND
                     ( lr_add_storage_cl->hec_astore_class_descr     IS NOT INITIAL ) AND
                     ( lr_add_storage_cl->hec_astore_class_descr_ext IS INITIAL ).
                    lr_add_storage_cl->hec_astore_class_descr_ext = lr_add_storage_cl->hec_astore_class_descr.
                  ENDIF.

                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Resets -> TODO move to actions
                "-----------------------------------
                " Reset Service Description
                IF ( lr_add_storage_cl->hec_astore_class_guid IS INITIAL ).
                  IF ( lr_add_storage_cl->hec_astore_class_descr = lr_add_storage_cl->hec_astore_class_descr_ext ).
                    CLEAR: lr_add_storage_cl->hec_astore_class_descr_ext.
                  ENDIF.
                  CLEAR: lr_add_storage_cl->hec_astore_class_descr.

                  lv_data_changed = abap_true.
                ENDIF.

                IF ( <fs_longterm_backup_before>-hec_astore_class_descr_ext <> lr_add_storage_cl->hec_astore_class_descr_ext ).
                  lr_add_storage_cl->hec_tree_descr = COND #( WHEN lr_add_storage_cl->hec_astore_class_descr IS NOT INITIAL
                                                     THEN |{ lr_add_storage_cl->hec_astore_class_descr } : { lr_add_storage_cl->hec_astore_class_descr_ext }|
                                                     ELSE |{ lr_add_storage_cl->hec_astore_class_descr_ext }|  ).
                  lv_data_changed = abap_true.
                ENDIF.

                IF ( <fs_longterm_backup_before>-hec_astore_class_descr <> lr_add_storage_cl->hec_astore_class_descr ).
                  lr_add_storage_cl->hec_tree_descr = COND #( WHEN lr_add_storage_cl->hec_astore_class_descr IS NOT INITIAL
                                                     THEN |{ lr_add_storage_cl->hec_astore_class_descr } : { lr_add_storage_cl->hec_astore_class_descr_ext }|
                                                     ELSE |{ lr_add_storage_cl->hec_astore_class_descr_ext }|  ).
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Check instance status and switch
                "-----------------------------------
                lv_inst_status = COND /hec1/config_instance_status( WHEN lr_add_storage_cl->hec_astore_class_guid   IS NOT INITIAL AND
                                                                         lr_add_storage_cl->hec_node_datacenter_ref IS NOT INITIAL
                                                                    THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                    ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

                lr_add_storage_cl->hec_delete_visible = abap_true.

                IF ( lv_inst_status <> lr_add_storage_cl->hec_instance_status ).
                  lr_add_storage_cl->hec_instance_status = lv_inst_status.
                  lv_data_changed = abap_true.
                ENDIF.

                " check, if assigned tier_lt_backup nodes must be updated
                IF ( lr_add_storage_cl->hec_astore_class_guid <> <fs_longterm_backup_before>-hec_astore_class_guid )
                OR ( lr_add_storage_cl->hec_astore_class_descr_ext <> <fs_longterm_backup_before>-hec_astore_class_descr_ext ).

*                  ls_act_param_tier_ltb  = CORRESPONDING /hec1/s_act_update_tier_ltb( lr_add_storage_cl->* ). "not supported yet
                ENDIF.

                """"""""""""""""""""""""""""""""""""""""""""""""""""""
                " Update TIER_ADD_STORAGE - not suported yet
                """"""""""""""""""""""""""""""""""""""""""""""""""""""
                IF ( lv_data_changed = abap_true ).
                  io_modify->update( iv_node           = is_ctx-node_key
                                     iv_key            = lr_add_storage_cl->key
                                     is_data           = lr_add_storage_cl      ).
                ENDIF.

                CLEAR: lv_inst_status,
                       lv_data_changed.
              ENDIF.
              UNASSIGN <fs_longterm_backup_before>.

            ENDLOOP. "LOOP AT lt_add_service REFERENCE INTO lr_add_service.
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.
  ENDMETHOD.

  METHOD determine_a_storage_class_cr.
    DATA: lt_add_storage_class         TYPE /hec1/t_add_storage_class_ct,
          lt_longterm_backup_cl_before TYPE /hec1/t_add_storage_class_ct,
          lr_add_storage_cl            TYPE REF TO /hec1/s_add_storage_class_cs,
          lt_phase                     TYPE /hec1/t_data_phase_ct.
*          ls_act_param_tier_ltb        TYPE /hec1/s_act_update_tier_ltb. "not supported yet

    CLEAR:
        eo_message,
        et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_add_storage_class  ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_class-create.

            LOOP AT lt_add_storage_class REFERENCE INTO lr_add_storage_cl.
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_add_storage_cl->hec_astore_class_guid   IS NOT INITIAL AND
                                                                             lr_add_storage_cl->hec_node_datacenter_ref IS NOT INITIAL
*                                                                             lr_add_storage_cl->hec_phase_guid         IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              lr_add_storage_cl->hec_delete_visible = abap_true.

              " Check instance status and switch
              IF ( lv_inst_status <> lr_add_storage_cl->hec_instance_status ).
                lr_add_storage_cl->hec_instance_status = lv_inst_status.
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
                  is_node_data = lr_add_storage_cl
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              IF lv_data_changed = abap_false.
                lv_data_changed = lv_cr_data_changed.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node           = is_ctx-node_key
                                   iv_key            = lr_add_storage_cl->key
                                   is_data           = lr_add_storage_cl      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP.

*            " ***************************************************************************
*            " update mode
*            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-lt_backup_class-update.

*            CLEAR: ls_act_param_tier_ltb.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_longterm_backup_cl_before  ).

            io_read->retrieve_by_association( EXPORTING iv_node         = /hec1/if_configuration_c=>sc_node-root
                                                        it_key          = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data    = abap_true
                                                        iv_association  = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data         = lt_phase ).

            LOOP AT lt_add_storage_class REFERENCE INTO lr_add_storage_cl.


              ASSIGN lt_longterm_backup_cl_before[ key = lr_add_storage_cl->key ] TO FIELD-SYMBOL(<fs_longterm_backup_before>).

              IF ( <fs_longterm_backup_before> IS ASSIGNED ).

                DATA(ls_datacenter) = VALUE #( lt_datacenter[ hec_node_datacenter = lr_add_storage_cl->hec_node_datacenter_ref ] OPTIONAL ).

                " Get service class data
                SELECT SINGLE hec_shared_storage_descr, hec_cb_pricing_lb_guid INTO @DATA(lv_add_storage_descr)
                  FROM /hec1/a_sha_stor
                 WHERE hec_apm_guid = @lr_add_storage_cl->hec_apm_guid
                   AND hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid
                   AND hec_sec_datacenter_guid = @ls_datacenter-hec_datacenter_guid
                   AND hec_shared_storage_guid = @lr_add_storage_cl->hec_astore_class_guid.
                IF ( sy-subrc = 0 ).
                  lr_add_storage_cl->* = VALUE #( BASE lr_add_storage_cl->*
                                                       hec_astore_class_descr     = lv_add_storage_descr-hec_shared_storage_descr
                                                                                                         ).
                  "Set longterm backup description in case it is empty
                  IF ( lr_add_storage_cl->hec_astore_class_guid      IS NOT INITIAL  ) AND
                     ( lr_add_storage_cl->hec_astore_class_descr     IS NOT INITIAL ) AND
                     ( lr_add_storage_cl->hec_astore_class_descr_ext IS INITIAL ).
                    lr_add_storage_cl->hec_astore_class_descr_ext = lr_add_storage_cl->hec_astore_class_descr.
                  ENDIF.

                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Resets -> TODO move to actions
                "-----------------------------------
                " Reset Service Description
                IF ( lr_add_storage_cl->hec_astore_class_guid IS INITIAL ).
                  IF ( lr_add_storage_cl->hec_astore_class_descr = lr_add_storage_cl->hec_astore_class_descr_ext ).
                    CLEAR: lr_add_storage_cl->hec_astore_class_descr_ext.
                  ENDIF.
                  CLEAR: lr_add_storage_cl->hec_astore_class_descr.

                  lv_data_changed = abap_true.
                ENDIF.

                IF ( <fs_longterm_backup_before>-hec_astore_class_descr_ext <> lr_add_storage_cl->hec_astore_class_descr_ext ).
                  lr_add_storage_cl->hec_tree_descr = COND #( WHEN lr_add_storage_cl->hec_astore_class_descr IS NOT INITIAL
                                                     THEN |{ lr_add_storage_cl->hec_astore_class_descr } : { lr_add_storage_cl->hec_astore_class_descr_ext }|
                                                     ELSE |{ lr_add_storage_cl->hec_astore_class_descr_ext }|  ).
                  lv_data_changed = abap_true.
                ENDIF.

                IF ( <fs_longterm_backup_before>-hec_astore_class_descr <> lr_add_storage_cl->hec_astore_class_descr ).
                  lr_add_storage_cl->hec_tree_descr = COND #( WHEN lr_add_storage_cl->hec_astore_class_descr IS NOT INITIAL
                                                     THEN |{ lr_add_storage_cl->hec_astore_class_descr } : { lr_add_storage_cl->hec_astore_class_descr_ext }|
                                                     ELSE |{ lr_add_storage_cl->hec_astore_class_descr_ext }|  ).
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Check instance status and switch
                "-----------------------------------
                lv_inst_status = COND /hec1/config_instance_status( WHEN lr_add_storage_cl->hec_astore_class_guid   IS NOT INITIAL AND
                                                                         lr_add_storage_cl->hec_node_datacenter_ref IS NOT INITIAL
                                                                    THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                    ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

                lr_add_storage_cl->hec_delete_visible = abap_true.

                IF ( lv_inst_status <> lr_add_storage_cl->hec_instance_status ).
                  lr_add_storage_cl->hec_instance_status = lv_inst_status.
                  lv_data_changed = abap_true.
                ENDIF.

                " check, if assigned tier_lt_backup nodes must be updated
                IF ( lr_add_storage_cl->hec_astore_class_guid <> <fs_longterm_backup_before>-hec_astore_class_guid )
                OR ( lr_add_storage_cl->hec_astore_class_descr_ext <> <fs_longterm_backup_before>-hec_astore_class_descr_ext ).

*                  ls_act_param_tier_ltb  = CORRESPONDING /hec1/s_act_update_tier_ltb( lr_add_storage_cl->* ). "not supported yet
                ENDIF.

                """"""""""""""""""""""""""""""""""""""""""""""""""""""
                " Update TIER_LT_BACKUP - not suported yet
                """"""""""""""""""""""""""""""""""""""""""""""""""""""

*                IF ( ls_act_param_tier_ltb IS NOT INITIAL ).
*                  me->mr_act_param_tier_ltb = NEW /hec1/s_act_update_tier_ltb( ls_act_param_tier_ltb ).
*
*                  /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
*                      is_ctx          = CORRESPONDING #( is_ctx )
*                      it_key          = it_key
*                      iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_tier_lt_backup )
*                      iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
*                      ir_act_param    = me->mr_act_param_tier_ltb ).
*                ENDIF.


                IF ( lv_data_changed = abap_true ).
                  io_modify->update( iv_node           = is_ctx-node_key
                                     iv_key            = lr_add_storage_cl->key
                                     is_data           = lr_add_storage_cl      ).
                ENDIF.

                CLEAR: lv_inst_status,
                       lv_data_changed.
              ENDIF.
              UNASSIGN <fs_longterm_backup_before>.

            ENDLOOP. "LOOP AT lt_add_service REFERENCE INTO lr_add_service.
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.
  ENDMETHOD.

  METHOD determine_a_storage_amount.

    DATA: lt_add_storage_amount     TYPE /hec1/t_add_storage_amount_ct,
          lt_add_storage_bef_amount TYPE /hec1/t_add_storage_amount_ct,
          lr_add_storage_amount     TYPE REF TO /hec1/s_add_storage_amount_cs,
          lt_phase                  TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing      TYPE TABLE OF /hec1/s_act_phase_inherit.

    CLEAR:
        eo_message,
        et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_add_storage_amount  ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-add_storage_amount-create.

            LOOP AT lt_add_storage_amount REFERENCE INTO lr_add_storage_amount.
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_add_storage_amount->hec_astore_class_guid   IS NOT INITIAL AND
                                                                             lr_add_storage_amount->hec_node_datacenter_ref IS NOT INITIAL AND
                                                                             lr_add_storage_amount->hec_phase_guid          IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              lr_add_storage_amount->hec_delete_visible = abap_true.

              " Check instance status and switch
              IF ( lv_inst_status <> lr_add_storage_amount->hec_instance_status ).
                lr_add_storage_amount->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node           = is_ctx-node_key
                                   iv_key            = lr_add_storage_amount->key
                                   is_data           = lr_add_storage_amount      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP.

*            " ***************************************************************************
*            " update mode
*            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-add_storage_amount-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_add_storage_bef_amount  ).

            io_read->retrieve_by_association( EXPORTING iv_node         = /hec1/if_configuration_c=>sc_node-root
                                                        it_key          = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data    = abap_true
                                                        iv_association  = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data         = lt_phase ).

            LOOP AT lt_add_storage_amount REFERENCE INTO lr_add_storage_amount.


              ASSIGN lt_add_storage_bef_amount[ key = lr_add_storage_amount->key ] TO FIELD-SYMBOL(<fs_add_storage_befor>).

              IF ( <fs_add_storage_befor> IS ASSIGNED ).
                TRY.


                    " if the infrastructure provider is set and there is datacenter assigned
                    " get the pricing
                    IF ( lr_dlvy_unit->hec_inf_provider_guid IS NOT INITIAL ) AND ( lr_add_storage_amount->hec_node_datacenter_ref IS NOT INITIAL ).
                      DATA(ls_datacenter) = VALUE #( lt_datacenter[ hec_node_datacenter = lr_add_storage_amount->hec_node_datacenter_ref ] OPTIONAL ).

                      SELECT SINGLE hec_cb_pricing_lb_guid INTO @DATA(lv_astore_legoblock)
                        FROM /hec1/a_sha_stor
                       WHERE hec_apm_guid = @lr_add_storage_amount->hec_apm_guid
                         AND hec_infra_provider_guid = @lr_dlvy_unit->hec_inf_provider_guid
                         AND hec_sec_datacenter_guid = @ls_datacenter-hec_datacenter_guid
                         AND hec_shared_storage_guid = @lr_add_storage_amount->hec_astore_class_guid.

                      " Get pricing
                      SELECT SINGLE * INTO @DATA(ls_pricing) "#EC CI_ALL_FIELDS_NEEDED
                         FROM /hec1/c_cbp_lb
                        WHERE hec_price_lb = @lv_astore_legoblock.
                      IF ( sy-subrc = 0 ).

                        DATA(lv_exchange_rate) = lr_add_storage_amount->hec_exchange_rate. "Temp field because the ls_pricing structure overwrites the real exchange_rate

                        lr_add_storage_amount->* = VALUE #( BASE lr_add_storage_amount->*
                             hec_tree_descr           = COND #( WHEN lr_add_storage_amount->hec_phase_guid IS INITIAL
                                                                THEN |{ VALUE #( lt_phase[ hec_node_phase = lr_add_storage_amount->hec_phase_guid ]-hec_phase_descr OPTIONAL ) } : { lr_add_storage_amount->hec_ast_amount }|
                                                                ELSE |{ lr_add_storage_amount->hec_ast_amount }| )
                             hec_month_price_fee      = lr_add_storage_amount->hec_ast_amount * ls_pricing-hec_month_price_eur
                             price                    = CORRESPONDING #( BASE ( lr_add_storage_amount->price ) ls_pricing )
                             hec_exchange_rate        = lv_exchange_rate
                        ).
                        lv_data_changed = abap_true.
                      ENDIF.

                      lv_data_changed = abap_true.
                    ENDIF. " IF lv_infra_provider IS NOT INITIAL.
                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF ( lr_add_storage_amount->hec_phase_guid NE <fs_add_storage_befor>-hec_phase_guid ).

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_add_storage_amount->key
                                  hec_phase_guid_new = lr_add_storage_amount->hec_phase_guid
                                  hec_phase_guid_old = <fs_add_storage_befor>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_add_storage_amount->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "Phase changed
              ENDIF. "<<fs_add_storage_befor>> is assigned


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_add_storage_amount->hec_astore_class_guid   IS NOT INITIAL AND
                                                                       lr_add_storage_amount->hec_node_datacenter_ref IS NOT INITIAL AND
                                                                       lr_add_storage_amount->hec_phase_guid          IS NOT INITIAL AND
                                                                       lr_add_storage_amount->hec_ast_amount > 0
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              lr_add_storage_amount->hec_delete_visible = abap_true.

              IF ( lv_inst_status <> lr_add_storage_amount->hec_instance_status ).
                lr_add_storage_amount->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              IF ( lv_data_changed = abap_true ).
                io_modify->update( iv_node           = is_ctx-node_key
                                   iv_key            = lr_add_storage_amount->key
                                   is_data           = lr_add_storage_amount      ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_add_storage_befor>.

            ENDLOOP. "LOOP AT lt_add_service REFERENCE INTO lr_add_service.

            "-----------------------------------
            " Update Phasing
            "-----------------------------------
            IF ( lt_act_param_phasing IS NOT INITIAL ).
              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing ).
            ENDIF.
*
        ENDCASE.
*

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.
  ENDMETHOD.

  METHOD determine_a_storage_amount_cr.

  ENDMETHOD.

ENDCLASS.