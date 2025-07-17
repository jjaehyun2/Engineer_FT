CLASS /hec1/cl_config_determination DEFINITION
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
    DATA mr_act_param_phasing TYPE REF TO data .
    DATA mr_act_param_delete TYPE REF TO data .
    DATA mr_act_param_material_add TYPE REF TO data .
    DATA mr_act_param_sw_item_add TYPE REF TO data .
    DATA mr_act_param_landscape TYPE REF TO data .
    DATA mr_act_param_sla TYPE REF TO data .

    METHODS determine_add_service
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
    METHODS determine_add_service_cr
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
    METHODS determine_root_cr
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
    METHODS determine_root
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
    METHODS determine_tier_add_service_cr
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
    METHODS determine_tier_add_service
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
    METHODS determine_connectivity
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
    METHODS determine_connectivity_cr
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
    METHODS determine_datacenter
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
    METHODS determine_datacenter_cr
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
    METHODS determine_delivery_unit
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
    METHODS determine_delivery_unit_cr
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
    METHODS determine_infr_baseline
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
    METHODS determine_infr_baseline_cr
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
    METHODS modify_aggre_mod_type
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key .
    METHODS determine_man_serv_baseline
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
    METHODS determine_man_serv_baseline_cr
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
    METHODS determine_network_segment_cr
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
    METHODS determine_network_segment
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
    METHODS determine_material_cr
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
    METHODS determine_material
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
    METHODS determine_solution
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
    METHODS determine_solution_cr
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
    METHODS determine_sw_item
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
    METHODS determine_sw_item_cr
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
    METHODS determine_tier
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
    METHODS determine_tier_cr
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
    METHODS determine_tier_sla
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
    METHODS determine_transport_path
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
    METHODS determine_tier_sla_cr
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
    METHODS determine_transport_path_cr
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
    METHODS determine_phase
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
    METHODS determine_phase_cr
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
    METHODS determine_contact_reference_cr
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
    METHODS determine_contact_reference
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
    METHODS determine_contact_cr
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
    METHODS determine_contact
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
    METHODS determine_tier_add_storage
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key .
    METHODS determine_tier_add_storage_cr
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key .
ENDCLASS.



CLASS /hec1/cl_config_determination IMPLEMENTATION.


  METHOD determine_add_service.

    DATA: lt_add_service        TYPE /hec1/t_data_add_services_ct,
          lt_add_service_before TYPE /hec1/t_data_add_services_ct,
          lr_add_service        TYPE REF TO /hec1/s_data_add_services_cs,
          lt_phase              TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing  TYPE TABLE OF /hec1/s_act_phase_inherit.

    CLEAR: eo_message,
           et_failed_key.



    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_add_service ).


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
          WHEN /hec1/if_configuration_c=>sc_determination-add_service-create.

            IF lines( lt_datacenter ) = 1.
              " Get data center data
              TRY.
                  DATA(ls_datacenter) = lt_datacenter[ 1 ].
                CATCH cx_sy_itab_line_not_found.
              ENDTRY.
            ENDIF.


            LOOP AT lt_add_service REFERENCE INTO lr_add_service.

              lr_add_service->hec_delete_visible = abap_true.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_add_service->hec_as_class_guid      IS NOT INITIAL AND
                                                                             lr_add_service->hec_as_datacenter_guid IS NOT INITIAL AND
                                                                             lr_add_service->hec_phase_guid         IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_add_service->hec_instance_status.
                lr_add_service->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Assign data center
              "-----------------------------------
              IF ls_datacenter-hec_datacenter_guid IS NOT INITIAL.
                lr_add_service->hec_as_datacenter_guid  = ls_datacenter-hec_node_datacenter.
                lr_add_service->hec_as_datacenter_descr = ls_datacenter-hec_datacenter_descr.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify additional service
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_add_service->key
                                   is_data = lr_add_service ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP.

            " ***************************************************************************
            " update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-add_service-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_add_service_before ).


            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).



            LOOP AT lt_add_service REFERENCE INTO lr_add_service.
              lr_add_service->hec_delete_visible = abap_true.
              ASSIGN lt_add_service_before[ key = lr_add_service->key ] TO FIELD-SYMBOL(<fs_add_service_before>).

              " Get data center data
              TRY.
                  ls_datacenter = lt_datacenter[ hec_node_datacenter = lr_add_service->hec_as_datacenter_guid ].
                CATCH cx_sy_itab_line_not_found.
              ENDTRY.

              IF <fs_add_service_before> IS ASSIGNED.
                "-----------------------------------
                " Service class GUID has changed
                "-----------------------------------
                IF lr_dlvy_unit->hec_inf_provider_guid IS NOT INITIAL                              AND
                   ls_datacenter-hec_datacenter_guid   IS NOT INITIAL                              AND
                   lr_add_service->hec_as_class_guid   IS NOT INITIAL                              AND
                   <fs_add_service_before>-hec_as_class_guid <> lr_add_service->hec_as_class_guid.

                  " Get number of service class entries
                  DATA(lv_count_class_guid) = lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_datac_add_service_class( iv_apm_guid          = lr_landscape->hec_apm_guid
                                                                                                                                                 iv_inf_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                                                                                                 iv_datacenter_guid   = ls_datacenter-hec_datacenter_guid   ) ).

                  " Get additional service data
                  SELECT SINGLE *
                    FROM /hec1/i_addserviceclassbasic
                   WHERE hec_apm_guid      = @lr_landscape->hec_apm_guid        AND
                         hec_as_class_guid = @lr_add_service->hec_as_class_guid
                    INTO CORRESPONDING FIELDS OF @lr_add_service->*.


                  " Set additional service description in case it is empty
                  IF lr_add_service->hec_as_class_guid      IS NOT INITIAL AND
                     lr_add_service->hec_as_class_descr     IS NOT INITIAL AND
                     lr_add_service->hec_as_class_descr_ext IS INITIAL.
                    lr_add_service->hec_as_class_descr_ext = lr_add_service->hec_as_class_descr.
                  ENDIF.


                  " Get number of service entries
                  SELECT COUNT(*)
                    FROM /hec1/i_addserviceclasslbbasic
                   WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid          AND
                         hec_sec_datacenter_guid = @ls_datacenter-hec_datacenter_guid   AND
                         hec_inf_provider_guid   = @lr_dlvy_unit->hec_inf_provider_guid AND
                         hec_as_class_guid       = @lr_add_service->hec_as_class_guid
                   INTO @DATA(lv_count).

                  IF lv_count = 1.
                    SELECT SINGLE *
                      FROM /hec1/i_addserviceclasslbbasic
                     WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid          AND
                           hec_sec_datacenter_guid = @ls_datacenter-hec_datacenter_guid   AND
                           hec_inf_provider_guid   = @lr_dlvy_unit->hec_inf_provider_guid AND
                           hec_as_class_guid       = @lr_add_service->hec_as_class_guid
                      INTO @DATA(ls_service_data).

                    " Get pricing
                    SELECT SINGLE * FROM /hec1/c_cbp_lb "#EC CI_ALL_FIELDS_NEEDED
                       INTO @DATA(ls_pricing)
                      WHERE hec_price_lb = @ls_service_data-hec_cb_pricing_lb_guid.

                  ENDIF. " IF lv_count = 1.

                  DATA(lv_exchange_rate) = lr_add_service->hec_exchange_rate. "Temp field because the ls_pricing structure overwrites the real exchange_rate

                  lr_add_service->* = VALUE #( BASE lr_add_service->*
                                               hec_as_class_vlqt       = SWITCH #( lv_count_class_guid
                                                                                   WHEN 0
                                                                                   THEN space
                                                                                   WHEN 1
                                                                                   THEN /hec1/if_config_constants=>gc_value_list_quantity-single
                                                                                   ELSE /hec1/if_config_constants=>gc_value_list_quantity-multi  )
                                               hec_ip_as_class_guid    = ls_service_data-hec_ip_as_class_guid
                                               hec_ip_as_class_descr   = ls_service_data-hec_ip_as_class_descr
                                               hec_ip_as_class_vlqt    = SWITCH #( lv_count
                                                                                   WHEN 0
                                                                                   THEN space
                                                                                   WHEN 1
                                                                                   THEN /hec1/if_config_constants=>gc_value_list_quantity-single
                                                                                   ELSE /hec1/if_config_constants=>gc_value_list_quantity-multi  )
                                               hec_as_quota            = ls_service_data-hec_as_quota
                                               hec_as_tier_uplift_perc = ls_service_data-hec_as_upflift_percent
                                               hec_price_lb            = ls_service_data-hec_cb_pricing_lb_guid
                                               hec_as_datacenter_guid  = COND #( WHEN ls_datacenter-hec_datacenter_guid IS NOT INITIAL
                                                                                 THEN ls_datacenter-hec_node_datacenter
                                                                                 ELSE space                                             )
                                               hec_as_datacenter_descr = COND #( WHEN ls_datacenter-hec_datacenter_descr IS NOT INITIAL
                                                                                 THEN ls_datacenter-hec_datacenter_descr
                                                                                 ELSE space                                             )
                                               hec_tree_descr          = COND #( WHEN ls_datacenter-hec_datacenter_guid IS INITIAL
                                                                                 THEN |{ lr_add_service->hec_as_class_descr } : { lr_add_service->hec_as_class_descr_ext }|
                                                                                 ELSE |{ lr_add_service->hec_as_class_descr } - { ls_datacenter-hec_datacenter_descr } : { lr_add_service->hec_as_class_descr_ext }| )
                                               price                   = CORRESPONDING #( BASE ( lr_add_service->price ) ls_pricing )
                                               hec_exchange_rate       = lv_exchange_rate                                                       ).

                  lv_data_changed = abap_true.
                ENDIF. " IF lr_add_service->hec_as_class_guid IS NOT INITIAL AND


                "-----------------------------------
                " Service GUID has changed
                "-----------------------------------
                IF lr_dlvy_unit->hec_inf_provider_guid  IS NOT INITIAL                                  AND
                   ls_datacenter-hec_datacenter_guid    IS NOT INITIAL                                  AND
                   lr_add_service->hec_as_class_guid    IS NOT INITIAL                                  AND
                   lr_add_service->hec_ip_as_class_guid IS NOT INITIAL                                  AND
                   <fs_add_service_before>-hec_ip_as_class_guid <> lr_add_service->hec_ip_as_class_guid.

                  " Get number of service entries
                  SELECT COUNT(*)
                    FROM /hec1/i_addserviceclasslbbasic
                   WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid          AND
                         hec_sec_datacenter_guid = @ls_datacenter-hec_datacenter_guid   AND
                         hec_inf_provider_guid   = @lr_dlvy_unit->hec_inf_provider_guid AND
                         hec_as_class_guid       = @lr_add_service->hec_as_class_guid
                   INTO @lv_count.


                  SELECT SINGLE *
                    FROM /hec1/i_addserviceclasslbbasic
                   WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid           AND
                         hec_sec_datacenter_guid = @ls_datacenter-hec_datacenter_guid    AND
                         hec_inf_provider_guid   = @lr_dlvy_unit->hec_inf_provider_guid  AND
                         hec_as_class_guid       = @lr_add_service->hec_as_class_guid    AND
                         hec_ip_as_class_guid    = @lr_add_service->hec_ip_as_class_guid
                    INTO @ls_service_data.

                  " Get pricing
                  SELECT SINGLE * FROM /hec1/c_cbp_lb "#EC CI_ALL_FIELDS_NEEDED
                     INTO @ls_pricing
                    WHERE hec_price_lb = @ls_service_data-hec_cb_pricing_lb_guid.

                  lv_exchange_rate = lr_add_service->hec_exchange_rate. "Temp field because the ls_pricing structure overwrites the real exchange_rate

                  lr_add_service->* = VALUE #( BASE lr_add_service->*
                                               hec_ip_as_class_guid    = ls_service_data-hec_ip_as_class_guid
                                               hec_ip_as_class_descr   = ls_service_data-hec_ip_as_class_descr
                                               hec_ip_as_class_vlqt    = SWITCH #( lv_count
                                                                                   WHEN 0
                                                                                   THEN space
                                                                                   WHEN 1
                                                                                   THEN /hec1/if_config_constants=>gc_value_list_quantity-single
                                                                                   ELSE /hec1/if_config_constants=>gc_value_list_quantity-multi  )
                                               hec_as_quota            = ls_service_data-hec_as_quota
                                               hec_as_tier_uplift_perc = ls_service_data-hec_as_upflift_percent
                                               hec_price_lb            = ls_service_data-hec_cb_pricing_lb_guid
                                               hec_as_datacenter_guid  = COND #( WHEN ls_datacenter-hec_datacenter_guid IS NOT INITIAL
                                                                                 THEN ls_datacenter-hec_node_datacenter
                                                                                 ELSE space                                             )
                                               hec_as_datacenter_descr = COND #( WHEN ls_datacenter-hec_datacenter_descr IS NOT INITIAL
                                                                                 THEN ls_datacenter-hec_datacenter_descr
                                                                                 ELSE space                                             )
                                               hec_tree_descr          = COND #( WHEN ls_datacenter-hec_datacenter_guid IS INITIAL
                                                                                 THEN |{ lr_add_service->hec_as_class_descr } : { lr_add_service->hec_as_class_descr_ext }|
                                                                                 ELSE |{ lr_add_service->hec_as_class_descr } - { ls_datacenter-hec_datacenter_descr } : { lr_add_service->hec_as_class_descr_ext }| )
                                               price                   = CORRESPONDING #( BASE ( lr_add_service->price ) ls_pricing )
                                               hec_exchange_rate       = lv_exchange_rate                                                       ).

                  lv_data_changed = abap_true.
                ENDIF. " IF lr_dlvy_unit->hec_inf_provider_guid  IS NOT INITIAL AND

                "-----------------------------------
                " Data center GUID has changed
                "-----------------------------------
                IF ls_datacenter-hec_datacenter_guid              IS NOT INITIAL AND
                   lr_add_service->hec_as_datacenter_guid         IS NOT INITIAL AND
                   <fs_add_service_before>-hec_as_datacenter_guid IS     INITIAL.
                  lr_add_service->hec_as_datacenter_descr = ls_datacenter-hec_datacenter_descr.
                ENDIF.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_add_service->hec_phase_guid NE <fs_add_service_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_add_service->key
                                  hec_phase_guid_new = lr_add_service->hec_phase_guid
                                  hec_phase_guid_old = <fs_add_service_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_add_service->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "Phase changed

                "-----------------------------------
                " Resets -> TODO move to actions
                "-----------------------------------

                " Reset Service Class GUID
                IF lr_add_service->hec_as_class_guid IS INITIAL.
                  IF lr_add_service->hec_as_class_descr = lr_add_service->hec_as_class_descr_ext.
                    CLEAR: lr_add_service->hec_as_class_descr_ext.
                  ENDIF.
                  CLEAR: lr_add_service->hec_as_class_descr,
                         lr_add_service->hec_as_class_vlqt,
                         lr_add_service->hec_as_tier_counter,
                         lr_add_service->hec_as_tier_uplift,
                         lr_add_service->hec_ip_as_class_guid,
                         lr_add_service->hec_ip_as_class_descr,
                         lr_add_service->hec_ip_as_class_vlqt,
                         lr_add_service->hec_as_quota,
                         lr_add_service->hec_as_tier_uplift_perc,
                         lr_add_service->price.

                  lv_data_changed = abap_true.
                ENDIF.


                " Reset Service GUID
                IF lr_add_service->hec_ip_as_class_guid IS     INITIAL AND
                   lr_add_service->hec_as_class_guid    IS NOT INITIAL.
                  CLEAR: lr_add_service->hec_ip_as_class_descr,
                         lr_add_service->hec_as_quota,
                         lr_add_service->hec_as_tier_uplift_perc,
                         lr_add_service->price.

                  lv_data_changed = abap_true.
                ENDIF.


                " Reset Datacenter
                IF <fs_add_service_before>-hec_as_datacenter_guid IS NOT INITIAL AND
                   lr_add_service->hec_as_datacenter_guid         IS     INITIAL.
                  CLEAR: lr_add_service->hec_as_datacenter_descr.

                  lv_data_changed = abap_true.
                ENDIF.

                IF <fs_add_service_before>-hec_as_datacenter_descr <> lr_add_service->hec_as_datacenter_descr.
                  lr_add_service->hec_tree_descr = COND #( WHEN ls_datacenter-hec_datacenter_descr IS INITIAL
                                                           THEN |{ lr_add_service->hec_as_class_descr } : { lr_add_service->hec_as_class_descr_ext }|
                                                           ELSE |{ lr_add_service->hec_as_class_descr } - { ls_datacenter-hec_datacenter_descr } : { lr_add_service->hec_as_class_descr_ext }| ).

                  lv_data_changed = abap_true.
                ENDIF.
              ENDIF. "<fs_add_service_before> is assigned


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_add_service->hec_as_class_guid      IS NOT INITIAL AND
                                                                       lr_add_service->hec_as_datacenter_guid IS NOT INITIAL AND
                                                                       lr_add_service->hec_phase_guid         IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_add_service->hec_instance_status.
                lr_add_service->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify aditional service
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_add_service->key
                                   is_data = lr_add_service ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_exchange_rate,
                     lv_count,
                     lv_count_class_guid,
                     ls_datacenter,
                     ls_service_data,
                     ls_pricing.

              UNASSIGN <fs_add_service_before>.
            ENDLOOP. "LOOP AT lt_add_service REFERENCE INTO lr_add_service.

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

        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_connectivity.

    DATA: lt_datacenter          TYPE /hec1/t_data_datacenter_ct,
          lt_connectivity        TYPE /hec1/t_data_connectivity_ct,
          lt_connectivity_before TYPE /hec1/t_data_connectivity_ct,
          lt_phase               TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing   TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_connectivity ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create and update after data center
            " mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-connectivity-create OR
               /hec1/if_configuration_c=>sc_determination-connectivity-update_after_datacenter.

            " Get data center (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-connectivity-to_parent
                                              IMPORTING et_data        = lt_datacenter ).

            LOOP AT lt_connectivity REFERENCE INTO DATA(lr_connectivity).

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              lr_connectivity->hec_connectivity_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_connectivity(
                                                                                                 iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                                 iv_sec_datacenter_guid = lr_connectivity->hec_sec_datacenter_guid ) )
                                                               THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                               ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              "-----------------------------------
              " Set tree control
              "-----------------------------------
              lr_connectivity->hec_delete_visible = abap_true.

              IF is_ctx-det_key = /hec1/if_configuration_c=>sc_determination-connectivity-create.
                lr_connectivity->hec_row_selectable = abap_true.
                lr_connectivity->hec_delete_visible = abap_true.
              ENDIF.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_connectivity->hec_connectivity_guid IS NOT INITIAL AND
                                                                             lr_connectivity->hec_phase_guid   IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_connectivity->hec_instance_status.
                lr_connectivity->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_datacenter[ key = lr_connectivity->parent_key ] TO FIELD-SYMBOL(<fs_datacenter>).

              IF <fs_datacenter> IS ASSIGNED.
                IF <fs_datacenter>-hec_datacenter_guid IS NOT INITIAL.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_connectivity->hec_row_selectable.
                lr_connectivity->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Modify
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_connectivity->key
                                   is_data = lr_connectivity ).
              ENDIF.

              UNASSIGN <fs_datacenter>.

              CLEAR: lv_inst_status,
                     lv_release,
                     lv_data_changed.

            ENDLOOP. " LOOP AT lt_connectivity REFERENCE INTO lr_connectivity.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-connectivity-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_connectivity_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get parent node (datacenter)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-connectivity-to_parent
                                              IMPORTING et_data        = lt_datacenter ).


            LOOP AT lt_connectivity REFERENCE INTO lr_connectivity.

              ASSIGN lt_connectivity_before[ key = lr_connectivity->key ] TO FIELD-SYMBOL(<fs_connectivity_before>).
              IF <fs_connectivity_before> IS ASSIGNED.

                "-----------------------------------
                " Get connectivity pricing
                "-----------------------------------
                IF <fs_connectivity_before>-hec_connectivity_guid IS INITIAL      AND
                   lr_connectivity->hec_connectivity_guid         IS NOT INITIAL.

                  " There is only one parent node, so one datacenter
                  TRY.
                      DATA(ls_datacenter) = lt_datacenter[ key = lr_connectivity->parent_key ].

                      SELECT SINGLE hec_cb_pricing_lb_guid
                        FROM /hec1/i_connectivitylbbasic
                       WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid              AND
                             hec_connectivity_guid   = @lr_connectivity->hec_connectivity_guid  AND
                             hec_sec_datacenter_guid = @ls_datacenter-hec_datacenter_guid       AND
                             hec_infra_provider_guid = @lr_delivery_unit->hec_inf_provider_guid
                        INTO @DATA(lv_pricing_legoblock).


                      SELECT SINGLE *
                        FROM /hec1/c_cbp_lb   "#EC CI_ALL_FIELDS_NEEDED
                       WHERE hec_price_lb = @lv_pricing_legoblock
                        INTO @DATA(ls_pricing).

                      lr_connectivity->* = CORRESPONDING #( BASE ( lr_connectivity->* ) ls_pricing ).

                      lv_data_changed = abap_true.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  "-----------------------------------
                  " Set Value List Quantity
                  "-----------------------------------
                  lr_connectivity->hec_connectivity_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_connectivity(
                                                                                                     iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                                     iv_sec_datacenter_guid = lr_connectivity->hec_sec_datacenter_guid ) )
                                                                   THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                   ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                ENDIF. " IF <fs_connectivity_before>-hec_connectivity_guid IS INITIAL

                "-----------------------------------
                " Get connectivity description
                "-----------------------------------
                IF lr_connectivity->hec_connectivity_guid  IS NOT INITIAL AND
                   lr_connectivity->hec_connectivity_descr IS INITIAL.

                  SELECT SINGLE hec_connectivity_descr
                    FROM /hec1/i_connectivitybasic
                   WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid             AND
                         hec_connectivity_guid   = @lr_connectivity->hec_connectivity_guid
                    INTO @lr_connectivity->hec_connectivity_descr.

                  lr_connectivity->hec_tree_descr = lr_connectivity->hec_connectivity_descr. "#EC CI_FLDEXT_OK[2215424]
                  lv_data_changed                 = abap_true.

                ENDIF. " IF lr_connectivity->hec_connectivity_guid  IS NOT INITIAL

                "-----------------------------------
                " Get APM Description
                "-----------------------------------
                lr_connectivity->hec_apm_descr = lr_landscape->hec_apm_descr.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_connectivity->hec_phase_guid NE <fs_connectivity_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_connectivity->key
                                  hec_phase_guid_new = lr_connectivity->hec_phase_guid
                                  hec_phase_guid_old = <fs_connectivity_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_connectivity->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "Phase changed

                "-----------------------------------
                " Reset connectivity GUID - TODO action
                "-----------------------------------
                IF <fs_connectivity_before>-hec_connectivity_guid IS NOT INITIAL AND
                   lr_connectivity->hec_connectivity_guid     IS INITIAL.

                  CLEAR: lr_connectivity->descr,
                         lr_connectivity->hec_connectivity_guid,
                         lr_connectivity->hec_connectivity_descr,
                         lr_connectivity->hec_tree_descr,
                         lr_connectivity->price.

                  lv_data_changed = abap_true.
                ENDIF.
              ENDIF. "<fs_connectivity_before> is assigned.


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_connectivity->hec_connectivity_guid IS NOT INITIAL AND
                                                                       lr_connectivity->hec_phase_guid   IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_connectivity->hec_instance_status.
                lr_connectivity->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_connectivity->key
                                   is_data = lr_connectivity ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_connectivity_before>.

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

        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_datacenter.

    DATA: lt_datacenter             TYPE /hec1/t_data_datacenter_ct,
          lt_datacenter_before      TYPE /hec1/t_data_datacenter_ct,
          lt_phase                  TYPE /hec1/t_data_phase_ct,
          lt_if_baseline            TYPE /hec1/t_data_if_baseline_ct,
          lt_add_service            TYPE /hec1/t_data_add_services_ct,
          lt_solution               TYPE /hec1/t_data_solution_ct,
          lt_tier                   TYPE /hec1/t_data_tier_ct,
*          lt_act_param              TYPE /hec1/t_data_datacenter_ct,
          lt_act_create_connect     TYPE /hec1/t_act_create_connect,
          ls_act_param_landscape    TYPE /hec1/s_act_update_landscape,
          lt_act_param_connectivity TYPE /bobf/t_frw_key,
          lt_act_param_dlvy_unit    TYPE /hec1/t_act_update_dlvy_unit,
          lt_act_param_add_service  TYPE /bobf/t_frw_key,
          lt_act_param_if_baseline  TYPE /bobf/t_frw_key,
          lt_act_param_tier         TYPE /bobf/t_frw_key,
          lt_act_param_phasing      TYPE TABLE OF /hec1/s_act_phase_inherit.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_datacenter ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit) ).

    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-datacenter-infrastructure_baseline
                                      IMPORTING et_data        = lt_if_baseline ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Set data center country name
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-datacenter-get_country_descr.

            LOOP AT lt_datacenter REFERENCE INTO DATA(lr_datacenter)
              WHERE hec_datacenter_guid               IS NOT INITIAL AND
                    hec_datacenter_country       IS NOT INITIAL AND
                    hec_datacenter_country_descr IS INITIAL.

              " Get data center country name
              SELECT SINGLE landx FROM t005t
                       INTO lr_datacenter->hec_datacenter_country_descr
                      WHERE spras = sy-langu
                        AND land1 = lr_datacenter->hec_datacenter_country.

              io_modify->update( iv_node = is_ctx-node_key
                                 iv_key  = lr_datacenter->key
                                 is_data = lr_datacenter ).

            ENDLOOP.

            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-datacenter-create.

            LOOP AT lt_datacenter REFERENCE INTO lr_datacenter.

              lr_datacenter->hec_delete_visible = COND #( WHEN lr_datacenter->hec_phase_guid IS NOT INITIAL
                                                          THEN abap_false
                                                          ELSE abap_true ).

              lr_datacenter->hec_row_selectable = abap_true.

              "-----------------------------------
              " Fill fields for Region,
              "  Delivery Unit and Infrastructure Provider
              "-----------------------------------
              lr_datacenter->* = VALUE #( BASE lr_datacenter->*
                                               hec_dlvy_region_l1_guid = lr_landscape->hec_dlvy_region_l1_guid
                                               hec_dlvy_region_l2_guid = lr_landscape->hec_dlvy_region_l2_guid
                                               hec_datacenter_country  = lr_landscape->hec_country_key
                                               hec_delivery_unit_guid  = lr_delivery_unit->hec_delivery_unit_guid
                                               hec_delivery_unit_descr = lr_delivery_unit->hec_delivery_unit_descr
                                               hec_infra_provider_guid = lr_delivery_unit->hec_inf_provider_guid
                                               hec_inf_provider_descr  = lr_delivery_unit->hec_inf_provider_descr  ).


              "-----------------------------------
              " Fill Parameter for General Call
              "  For Connectivity Creation
              "-----------------------------------
              APPEND VALUE #( parent_key = lr_datacenter->key ) TO lt_act_create_connect.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_datacenter->hec_datacenter_type_value IS NOT INITIAL AND
                                                                             lr_datacenter->hec_datacenter_guid       IS NOT INITIAL AND
                                                                             lr_datacenter->hec_datacenter_country    IS NOT INITIAL AND
                                                                             lr_datacenter->hec_phase_guid            IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_datacenter->hec_instance_status.
                lr_datacenter->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.


              "-----------------------------------
              " Modify data center
              "-----------------------------------
              IF lv_data_changed IS NOT INITIAL.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_datacenter->key
                                   is_data = lr_datacenter ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

            ENDLOOP.

            "-----------------------------------
            " Set Create Connectivity
            " action to general
            "-----------------------------------
            IF lt_act_create_connect IS NOT INITIAL.

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys_direct(
                is_ctx          = CORRESPONDING #( is_ctx )
                it_key          = VALUE #( FOR param IN lt_act_create_connect
                                           ( key = param-parent_key ) )
                iv_action       = /hec1/if_configuration_c=>sc_action-datacenter-create_connectivity
                iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation ).

            ENDIF.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-datacenter-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_datacenter_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get solution
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-solution
                                              IMPORTING et_target_key  = DATA(lt_solution_key) ).

            " Get tier
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-solution
                                                        it_key         = lt_solution_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                              IMPORTING et_data        = lt_tier ).

            "-----------------------------------
            " Get Data center from APM
            "-----------------------------------
            SELECT *
              FROM /hec1/i_regdlvyinfrdatabasic
              INTO TABLE @DATA(lt_fdt_datacenter)
               FOR ALL ENTRIES IN @lt_datacenter
             WHERE hec_datacenter_guid = @lt_datacenter-hec_datacenter_guid.


            LOOP AT lt_datacenter REFERENCE INTO lr_datacenter.
              lr_datacenter->hec_delete_visible = COND #( WHEN lr_datacenter->hec_phase_guid IS NOT INITIAL
                                                          THEN abap_false
                                                          ELSE abap_true ).

              lr_datacenter->hec_row_selectable = abap_true.

              ASSIGN lt_datacenter_before[ key = lr_datacenter->key ] TO FIELD-SYMBOL(<fs_datacenter_before>).
              IF <fs_datacenter_before> IS ASSIGNED.

                "-----------------------------------
                " Data center GUID has changed
                "-----------------------------------
                " Get data center country and description
                IF <fs_datacenter_before>-hec_datacenter_guid IS INITIAL AND
                   lr_datacenter->hec_datacenter_guid     IS NOT INITIAL.

                  lr_datacenter->* = CORRESPONDING #( BASE ( lr_datacenter->* ) VALUE #( lt_fdt_datacenter[ hec_datacenter_guid = lr_datacenter->hec_datacenter_guid ] OPTIONAL ) ).

                  lr_datacenter->hec_tree_descr = lr_datacenter->hec_datacenter_descr. "#EC CI_FLDEXT_OK[2215424]
                  lv_data_changed               = abap_true.

                  " Update Landscape
                  ls_act_param_landscape = VALUE #( key                    = lr_datacenter->root_key
                                                    hec_datacenter_country = lr_datacenter->hec_datacenter_country
                                                    do_update_region       = abap_true ).

                ENDIF. " IF ls_datacenter_old-hec_datacenter_guid IS INITIAL


                "-----------------------------------
                " Region L1-2, Delivery Unit or
                " Infrastructure Provider has
                " changed
                "-----------------------------------
                IF lr_datacenter->hec_dlvy_region_l1_guid <> <fs_datacenter_before>-hec_dlvy_region_l1_guid OR
                   lr_datacenter->hec_dlvy_region_l2_guid <> <fs_datacenter_before>-hec_dlvy_region_l2_guid OR
                   lr_datacenter->hec_datacenter_country  <> <fs_datacenter_before>-hec_datacenter_country  OR
                   lr_datacenter->hec_infra_provider_guid <> <fs_datacenter_before>-hec_infra_provider_guid OR
                   lr_datacenter->hec_delivery_unit_guid  <> <fs_datacenter_before>-hec_delivery_unit_guid.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_datacenter->hec_phase_guid NE <fs_datacenter_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_datacenter->key
                                  hec_phase_guid_new = lr_datacenter->hec_phase_guid
                                  hec_phase_guid_old = <fs_datacenter_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_datacenter->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "phasing changed


                "-----------------------------------
                " Update Delivery Unit and afterwards
                " Infrastructure baseline
                "-----------------------------------
                IF ( lr_datacenter->hec_datacenter_guid <> <fs_datacenter_before>-hec_datacenter_guid AND
                     lr_datacenter->hec_datacenter_guid IS NOT INITIAL                                    ) OR
                     lr_datacenter->hec_phase_changed  = abap_true.

                  TRY.
                      lr_datacenter->hec_infra_provider_guid = lt_fdt_datacenter[ hec_datacenter_guid = lr_datacenter->hec_datacenter_guid ]-hec_infra_provider_guid.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  INSERT VALUE #( key                   = lr_datacenter->key
                                  hec_inf_provider_guid = lr_datacenter->hec_infra_provider_guid ) INTO TABLE lt_act_param_dlvy_unit.

                  TRY.
                      DATA(ls_if_baseline) = lt_if_baseline[ parent_key = lr_datacenter->key ].
                      INSERT VALUE #( key = ls_if_baseline-key ) INTO TABLE lt_act_param_if_baseline.

                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                ENDIF. " IF ( lr_datacenter->hec_datacenter_guid <> <fs_datacenter_before>-hec_datacenter_guid...


                "-----------------------------------
                " Update additional service
                "-----------------------------------
                IF <fs_datacenter_before>-hec_datacenter_guid <> lr_datacenter->hec_datacenter_guid.
                  INSERT VALUE #( key = lr_datacenter->key ) INTO TABLE lt_act_param_add_service.
                ENDIF.


                "-----------------------------------
                " Update Tier
                "-----------------------------------
                IF <fs_datacenter_before>-hec_datacenter_guid IS INITIAL AND
                   lr_datacenter->hec_datacenter_guid     IS NOT INITIAL.

                  LOOP AT lt_tier ASSIGNING FIELD-SYMBOL(<fs_tier>).
                    INSERT VALUE #( key = <fs_tier>-key ) INTO TABLE lt_act_param_tier.
                  ENDLOOP.

                ENDIF.


                "-----------------------------------   -> later replaced by action
                " Reset data center GUID
                "-----------------------------------
                IF <fs_datacenter_before>-hec_datacenter_guid IS NOT INITIAL AND
                   lr_datacenter->hec_datacenter_guid         IS INITIAL.

                  CLEAR: lr_datacenter->hec_datacenter_country,
                         lr_datacenter->hec_datacenter_country_descr,
                         lr_datacenter->hec_datacenter_descr,
                         lr_datacenter->hec_tree_descr,
                         lr_datacenter->hec_sec_datacenter_guid.

                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Update Connectivity
                "-----------------------------------
                IF lr_datacenter->hec_sec_datacenter_guid <> <fs_datacenter_before>-hec_sec_datacenter_guid.
                  INSERT VALUE #( key = lr_datacenter->key ) INTO TABLE lt_act_param_connectivity.
                ENDIF.

              ENDIF. "<fs_datacenter> is assigned.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_datacenter->hec_datacenter_type_value IS NOT INITIAL AND
                                                                       lr_datacenter->hec_datacenter_guid       IS NOT INITIAL AND
                                                                       lr_datacenter->hec_datacenter_country    IS NOT INITIAL AND
                                                                       lr_datacenter->hec_phase_guid            IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete     ).

              IF lv_inst_status <> lr_datacenter->hec_instance_status.
                lr_datacenter->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Modify data center
              "-----------------------------------
              IF lv_data_changed IS NOT INITIAL.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_datacenter->key
                                   is_data = lr_datacenter ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_datacenter_before>.
            ENDLOOP. " LOOP AT lt_datacenter REFERENCE INTO lr_datacenter.


            "-----------------------------------
            " Update Landscape
            "-----------------------------------
            IF ls_act_param_landscape IS NOT INITIAL.
              me->mr_act_param = NEW /hec1/s_act_update_landscape( ls_act_param_landscape ).
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = CORRESPONDING #( is_ctx )
                    it_key          = it_key
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_landscape )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param ).
            ENDIF.

            "-----------------------------------
            " Update Delivery Unit
            "-----------------------------------
            IF lt_act_param_dlvy_unit IS NOT INITIAL.
              me->mr_act_param = NEW /hec1/t_act_update_dlvy_unit( lt_act_param_dlvy_unit ).
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = CORRESPONDING #( is_ctx )
                    it_key          = it_key "lt_act_param_dlvy_unit
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_delivery_unit )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param ).
            ENDIF.


            "-----------------------------------
            " Update Infrastructure Baseline
            "-----------------------------------
            IF lt_act_param_if_baseline IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                                  node_key      = /hec1/if_configuration_c=>sc_node-infrastructure_baseline )
                  it_key          = VALUE #( ( key = ls_if_baseline-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_if_baseline )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation ).
            ENDIF.


            "-----------------------------------
            " Update Connectivity
            "-----------------------------------
            IF lt_act_param_connectivity IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = CORRESPONDING #( is_ctx )
                    it_key          = lt_act_param_connectivity
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_connectivity )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation ).
            ENDIF.


            "-----------------------------------
            " Update Additional Service
            "-----------------------------------
            IF lt_act_param_add_service IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = lt_act_param_add_service
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_additional_service )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation ).
            ENDIF.


            "-----------------------------------
            " Update Tier
            "-----------------------------------
            IF lt_act_param_tier IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-tier )
                  it_key          = lt_act_param_tier
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_tier )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation ).
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
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_delivery_unit.

    DATA: lt_delivery_unit               TYPE /hec1/t_data_dlvy_unit_ct,
          lt_delivery_unit_before        TYPE /hec1/t_data_dlvy_unit_ct,
          lt_phase                       TYPE /hec1/t_data_phase_ct,
          lt_landscape                   TYPE /hec1/t_config_root_ct,
          lt_managed_service_baseline    TYPE /hec1/t_data_man_serv_basel_ct,
          lt_act_param_man_serv_baseline TYPE /bobf/t_frw_key,
          lt_act_param_datacenter        TYPE /hec1/t_act_update_datacenter,
          lt_act_param                   TYPE TABLE OF /bobf/s_frw_key,
          lt_modification                TYPE /bobf/t_frw_modification.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_delivery_unit ).


    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-delivery_unit-create.

            " there is only always one delivery unit
            TRY.
                DATA(lr_delivery_unit) = NEW /hec1/s_data_dlvy_unit_cs( lt_delivery_unit[ 1 ] ).
              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

            " get landscape = root
            io_read->retrieve( EXPORTING iv_node = /hec1/if_configuration_c=>sc_node-root
                                         it_key  = VALUE #( ( key = lr_delivery_unit->root_key ) )
                               IMPORTING et_data = lt_landscape ).

            " there is only one landscape
            TRY.
                DATA(ls_landscape) = lt_landscape[ 1 ].
              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

            "-----------------------------------
            " Set Value List Quantity
            "-----------------------------------
            " Later we might need to adjust this logic, if for some reason the number of entries can change
            lr_delivery_unit->hec_delivery_unit_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.
            lr_delivery_unit->hec_inf_provider_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.

*            " get default phase
*            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
*                                                        it_key         = VALUE #( ( key = lr_delivery_unit->root_key ) )
*                                                        iv_fill_data   = abap_true
*                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
*                                              IMPORTING et_data        = lt_phase ).
*
*            TRY.
*                DATA(ls_phase) = lt_phase[ hec_default_phase = abap_true ].
*              CATCH cx_sy_itab_line_not_found.
*            ENDTRY.

            lr_delivery_unit->hec_delete_visible = abap_false.

            "-----------------------------------
            " Check instance status and switch
            "-----------------------------------
            DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_delivery_unit->hec_delivery_unit_guid     IS NOT INITIAL AND
                                                                           lr_delivery_unit->hec_delivery_unit_category IS NOT INITIAL AND
                                                                           lr_delivery_unit->hec_inf_provider_guid      IS NOT INITIAL AND
                                                                           lr_delivery_unit->hec_inf_provider_category  IS NOT INITIAL
                                                                      THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                      ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

            IF lv_inst_status <> lr_delivery_unit->hec_instance_status.
              lr_delivery_unit->hec_instance_status = lv_inst_status.
              DATA(lv_data_changed) = abap_true.
            ENDIF.


            "-----------------------------------
            " Modify delivery unit
            "-----------------------------------
            IF lv_data_changed = abap_true.
              io_modify->update( iv_node = is_ctx-node_key
                                 iv_key  = lr_delivery_unit->key
                                 is_data = lr_delivery_unit ).
            ENDIF.

            "-----------------------------------
            " Set create Datacenter
            " action to general
            "-----------------------------------
            /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys_direct(
              is_ctx          = CORRESPONDING #( is_ctx )
              it_key          = it_key
              iv_action       = /hec1/if_configuration_c=>sc_action-delivery_unit-create_datacenter
              iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation ).


            " ***************************************************************************´
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-delivery_unit-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_delivery_unit_before ).


            SELECT *                          "#EC CI_ALL_FIELDS_NEEDED
              FROM /hec1/i_deliveryunitbasic
              INTO TABLE @DATA(lt_fdt_delivery_unit).   "#EC CI_NOWHERE

            SELECT *                          "#EC CI_ALL_FIELDS_NEEDED
              FROM /hec1/i_infraproviderbasic
              INTO TABLE @DATA(lt_fdt_infra_provider).  "#EC CI_NOWHERE



            LOOP AT lt_delivery_unit REFERENCE INTO lr_delivery_unit.
              ASSIGN lt_delivery_unit_before[ 1 ] TO FIELD-SYMBOL(<fs_delivery_unit_before>).

              IF <fs_delivery_unit_before> IS ASSIGNED.
                "-----------------------------------
                " Delivery unit has changed
                "-----------------------------------
                IF lr_delivery_unit->hec_delivery_unit_guid IS NOT INITIAL                        AND
                   lr_delivery_unit->hec_delivery_unit_guid <> <fs_delivery_unit_before>-hec_delivery_unit_guid.

                  DATA(ls_delivery_unit) = VALUE #( lt_fdt_delivery_unit[ hec_delivery_unit_guid = lr_delivery_unit->hec_delivery_unit_guid ] OPTIONAL ).

                  lr_delivery_unit->hec_delivery_unit_descr    = ls_delivery_unit-hec_delivery_unit_descr.
                  lr_delivery_unit->hec_delivery_unit_category = ls_delivery_unit-hec_delivery_unit_cat_value.
                  lr_delivery_unit->hec_sec_dlvy_unit_guid     = ls_delivery_unit-hec_sec_dlvy_unit_guid.
                  lr_delivery_unit->hec_tree_descr             = ls_delivery_unit-hec_delivery_unit_descr.

                  SELECT *
                    FROM @lt_fdt_infra_provider AS inf_prov
                    WHERE inf_prov~hec_delivery_unit_guid = @lr_delivery_unit->hec_delivery_unit_guid
                    INTO TABLE @DATA(lt_infra_provider).

                  IF lines( lt_infra_provider ) = 1.
                    DATA(ls_infra_provider) = VALUE #( lt_infra_provider[ 1 ] OPTIONAL ).
                    lr_delivery_unit->hec_inf_provider_guid = ls_infra_provider-hec_infra_provider_guid.
                  ENDIF.

                  lv_data_changed = abap_true.

                  " Set Value List Quantity
                  " Later we might need to adjust this logic, if for some reason the number of entries can change
                  lr_delivery_unit->hec_delivery_unit_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.
                  lr_delivery_unit->hec_inf_provider_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.

                  " Update datacenter search fields
                  INSERT VALUE #( BASE CORRESPONDING #( lr_delivery_unit->* )
                                       do_update_search_fields = abap_true ) INTO TABLE lt_act_param_datacenter.

                ENDIF.

                "-----------------------------------
                " Infrastructure Provider has changed
                "-----------------------------------
                IF lr_delivery_unit IS NOT INITIAL                                                             AND
                   lr_delivery_unit->hec_inf_provider_guid <> <fs_delivery_unit_before>-hec_inf_provider_guid.
                  TRY.
                      ls_infra_provider = lt_fdt_infra_provider[ hec_infra_provider_guid = lr_delivery_unit->hec_inf_provider_guid ].

                      lr_delivery_unit->hec_inf_provider_descr    = ls_infra_provider-hec_inf_provider_descr.
                      lr_delivery_unit->hec_sec_infra_prov_guid   = ls_infra_provider-hec_sec_infra_prov_guid.
                      lr_delivery_unit->hec_inf_provider_category = ls_infra_provider-hec_inf_provider_cat_value.

                      lv_data_changed                             = abap_true.

                      SELECT *
                        FROM @lt_fdt_infra_provider AS inf_prov
                        WHERE inf_prov~hec_infra_provider_guid = @lr_delivery_unit->hec_inf_provider_guid
                        INTO TABLE @lt_infra_provider.

                      IF lines( lt_infra_provider ) = 1.
                        ls_infra_provider = VALUE #( lt_infra_provider[ 1 ] OPTIONAL ).
                        lr_delivery_unit->hec_delivery_unit_guid = ls_infra_provider-hec_delivery_unit_guid.

                        ls_delivery_unit = VALUE #( lt_fdt_delivery_unit[ hec_delivery_unit_guid = ls_infra_provider-hec_delivery_unit_guid ] OPTIONAL ).

                        lr_delivery_unit->hec_delivery_unit_descr    = ls_delivery_unit-hec_delivery_unit_descr.
                        lr_delivery_unit->hec_delivery_unit_category = ls_delivery_unit-hec_delivery_unit_cat_value.
                        lr_delivery_unit->hec_sec_dlvy_unit_guid     = ls_delivery_unit-hec_sec_dlvy_unit_guid.
                        lr_delivery_unit->hec_tree_descr             = ls_delivery_unit-hec_delivery_unit_descr.
                      ENDIF.

                      " Set Value List Quantity
                      " Later we might need to adjust this logic, if for some reason the number of entries can change
                      lr_delivery_unit->hec_inf_provider_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.

                      "-----------------------------------
                      " Fill action table for update
                      " data center
                      "-----------------------------------
                      INSERT VALUE #( BASE CORRESPONDING #( lr_delivery_unit->* )
                                      do_update_search_fields = abap_true         ) INTO TABLE lt_act_param_datacenter.

                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                ENDIF. " IF lr_delivery_unit IS NOT INITIAL AND...

                "-----------------------------------
                " Update managed service baseline
                "-----------------------------------
                IF ( lr_delivery_unit->hec_delivery_unit_guid     IS NOT INITIAL AND
                     lr_delivery_unit->hec_delivery_unit_category IS NOT INITIAL AND
                     lr_delivery_unit->hec_inf_provider_guid      IS NOT INITIAL AND
                     lr_delivery_unit->hec_inf_provider_category  IS NOT INITIAL     )                                        AND
                   ( lr_delivery_unit->hec_delivery_unit_guid     <> <fs_delivery_unit_before>-hec_delivery_unit_guid     OR
                     lr_delivery_unit->hec_delivery_unit_category <> <fs_delivery_unit_before>-hec_delivery_unit_category OR
                     lr_delivery_unit->hec_inf_provider_guid      <> <fs_delivery_unit_before>-hec_inf_provider_guid      OR
                     lr_delivery_unit->hec_inf_provider_category  <> <fs_delivery_unit_before>-hec_inf_provider_category     ).

                  "-----------------------------------
                  " Fill action table for update
                  " managed service baseline
                  "-----------------------------------
                  IF NOT line_exists( lt_act_param_man_serv_baseline[ key = lr_delivery_unit->key ] ).
                    INSERT VALUE #( key = lr_delivery_unit->key ) INTO TABLE lt_act_param_man_serv_baseline.
                  ENDIF.
                ENDIF.

                "-----------------------------------
                " Reset -> Update Datacenter fields
                "-----------------------------------
                IF lr_delivery_unit->hec_delivery_unit_guid         IS     INITIAL AND
                   <fs_delivery_unit_before>-hec_delivery_unit_guid IS NOT INITIAL OR
                   lr_delivery_unit->hec_inf_provider_guid          IS     INITIAL AND
                  <fs_delivery_unit_before>-hec_inf_provider_guid   IS NOT INITIAL.

                  IF lr_delivery_unit->hec_delivery_unit_guid IS INITIAL.
                    CLEAR: lr_delivery_unit->hec_delivery_unit_category,
                           lr_delivery_unit->hec_delivery_unit_descr.
                  ENDIF.

                  IF lr_delivery_unit->hec_inf_provider_guid IS INITIAL.
                    CLEAR: lr_delivery_unit->hec_inf_provider_category,
                           lr_delivery_unit->hec_inf_provider_descr.
                  ENDIF.

                  lv_data_changed = abap_true.

                  "-----------------------------------
                  " Fill action table for update
                  " data center
                  "-----------------------------------
                  INSERT VALUE #( BASE CORRESPONDING #( lr_delivery_unit->* )
                                       do_reset = abap_true ) INTO TABLE lt_act_param_datacenter.

                ENDIF. " IF lr_delivery_unit->hec_delivery_unit_guid IS INITIAL AND...
              ENDIF. "If <fs_delivery_unit_before> is assigned

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_delivery_unit->hec_delivery_unit_guid     IS NOT INITIAL AND
                                                                       lr_delivery_unit->hec_delivery_unit_category IS NOT INITIAL AND
                                                                       lr_delivery_unit->hec_inf_provider_guid      IS NOT INITIAL AND
                                                                       lr_delivery_unit->hec_inf_provider_category  IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_delivery_unit->hec_instance_status.
                lr_delivery_unit->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Modify delivery unit
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_delivery_unit->key
                                   is_data = lr_delivery_unit ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_delivery_unit_before>.
            ENDLOOP.
        ENDCASE.


        "-----------------------------------
        " Set Update datacenter
        " action to general
        "-----------------------------------
        IF lt_act_param_datacenter IS NOT INITIAL.
          me->mr_act_param = NEW /hec1/t_act_update_datacenter( lt_act_param_datacenter ).

          /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
              is_ctx          = CORRESPONDING #( is_ctx )
              it_key          = it_key
              iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_datacenter )
              iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
              ir_act_param    = mr_act_param  ).
        ENDIF.

        "-----------------------------------
        " Set update managed service
        " baseline action to GENERAL
        "-----------------------------------
        IF lt_act_param_man_serv_baseline IS NOT INITIAL.
          /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
              is_ctx          = CORRESPONDING #( is_ctx )
              it_key          = lt_act_param_man_serv_baseline
              iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_man_serv_baseline )
              iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                                                                                ).
        ENDIF.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_infr_baseline.

    DATA: lt_infr_baseline        TYPE /hec1/t_data_if_baseline_ct,
          lt_infr_baseline_before TYPE /hec1/t_data_if_baseline_ct,
          lt_phase                TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing    TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_infr_baseline ).

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
          WHEN /hec1/if_configuration_c=>sc_determination-infrastructure_baseline-create.

            LOOP AT lt_infr_baseline REFERENCE INTO DATA(lr_infr_baseline).

*              GET TIME STAMP FIELD lr_infr_baseline->crea_date_time.

              io_modify->update( iv_node = is_ctx-node_key
                                 iv_key  = lr_infr_baseline->key
                                 is_data = lr_infr_baseline ).

            ENDLOOP.

            " ***************************************************************************
            " update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-infrastructure_baseline-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_infr_baseline_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).


            LOOP AT lt_infr_baseline REFERENCE INTO lr_infr_baseline.

              ASSIGN lt_infr_baseline_before[ key = lr_infr_baseline->key ] TO FIELD-SYMBOL(<fs_infr_baseline_before>).
              IF <fs_infr_baseline_before> IS ASSIGNED.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_infr_baseline->hec_phase_guid NE <fs_infr_baseline_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_infr_baseline->key
                                  hec_phase_guid_new = lr_infr_baseline->hec_phase_guid
                                  hec_phase_guid_old = <fs_infr_baseline_before>-hec_phase_guid ) TO lt_act_param_phasing.

                ENDIF. "phasing changed
              ENDIF. " IF <fs_infr_baseline_before> IS ASSIGNED.

              UNASSIGN <fs_infr_baseline_before>.

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

        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_man_serv_baseline.

    RETURN. ">>>>

  ENDMETHOD.


  METHOD determine_material.

    DATA: lt_tier              TYPE /hec1/t_data_tier_ct,
          lt_material          TYPE /hec1/t_data_material_ct,
          lt_material_before   TYPE /hec1/t_data_material_ct,
          lt_phase             TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing TYPE TABLE OF /hec1/s_act_phase_inherit,
          lt_act_param_sw_item TYPE /hec1/t_act_create_sw_item.


    CLEAR: eo_message,
           et_failed_key,
           me->mr_act_param.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_material ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit) ).

    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-material-to_parent
                                      IMPORTING et_data        = lt_tier ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = VALUE #( ( key = lv_root_key ) )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                      IMPORTING et_data        = lt_phase ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-material-create.

            LOOP AT lt_material REFERENCE INTO DATA(lr_material).
              lr_material->hec_delete_visible = abap_false.

              lr_material->hec_tree_descr = lr_material->hec_hsp_material_pli_name.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_material->hec_phase_guid IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_material->hec_instance_status.
                lr_material->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_tier[ key = lr_material->parent_key ] TO FIELD-SYMBOL(<fs_tier>).
              IF <fs_tier> IS ASSIGNED.
                DATA(lv_release) = COND #( WHEN <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                                                <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL AND
                                                <fs_tier>-hec_tier_type_value      IS NOT INITIAL
                                           THEN abap_true
                                           ELSE abap_false                                            ).
              ENDIF.

              IF lv_release <> lr_material->hec_row_selectable.
                lr_material->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " SW Item
              "-----------------------------------
              INSERT VALUE #( parent_key         = lr_material->key ) INTO TABLE lt_act_param_sw_item.

              "-----------------------------------
              " Modify material
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_material->key
                                   is_data = lr_material ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release.
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
            " Set Follow-Up to GENERAL
            " - Create Software Item
            "-----------------------------------
            IF lt_act_param_sw_item IS NOT INITIAL.

              me->mr_act_param_sw_item_add = NEW /hec1/t_act_create_sw_item( lt_act_param_sw_item ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                   is_ctx          = CORRESPONDING #( is_ctx )
                   it_key          = VALUE #( FOR sw_item_add IN lt_act_param_sw_item
                                            ( key = sw_item_add-parent_key ) )
                   iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_software_item )
                   iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                   ir_act_param    = me->mr_act_param_sw_item_add ).
            ENDIF.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-material-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_material_before ).

            LOOP AT lt_material REFERENCE INTO lr_material.
              lr_material->hec_delete_visible = abap_false.

              ASSIGN lt_material_before[ key = lr_material->key ] TO FIELD-SYMBOL(<fs_material_before>).
              IF <fs_material_before> IS ASSIGNED.

                lr_material->hec_tree_descr = lr_material->hec_hsp_material_pli_name.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_material->hec_phase_guid NE <fs_material_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_material->key
                                  hec_phase_guid_new = lr_material->hec_phase_guid
                                  hec_phase_guid_old = <fs_material_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_material->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. " IF lr_material->hec_phase_guid NE <fs_material_before>-hec_phase_guid.
              ENDIF. " IF <fs_material_before> IS ASSIGNED.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_material->hec_phase_guid IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_material->hec_instance_status.
                lr_material->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_tier[ key = lr_material->parent_key ] TO <fs_tier>.
              IF <fs_tier> IS ASSIGNED.
                lv_release = COND #( WHEN <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                                          <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL AND
                                          <fs_tier>-hec_tier_type_value      IS NOT INITIAL
                                     THEN abap_true
                                     ELSE abap_false                                            ).
              ENDIF.

              IF lv_release <> lr_material->hec_row_selectable.
                lr_material->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify material
              "-----------------------------------
*              DATA  lt_modification        TYPE /bobf/t_frw_modification.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_material->key
                                   is_data = lr_material ).

*
*                INSERT VALUE #( data        = lr_material
*                                node        = /hec1/if_configuration_c=>sc_node-material
*                                change_mode = /bobf/if_frw_c=>sc_modify_update
*                                key         = lr_material->key    ) INTO TABLE lt_modification.

              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release.
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

*            "-----------------------------------
*            " Change Instances
*            "-----------------------------------
*            IF lt_modification IS NOT INITIAL.
*              io_modify->do_modify( lt_modification ).
*
*              io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
*                                     IMPORTING eo_message             = DATA(lo_message)
*                                               eo_change              = DATA(lo_change)  ).
*            ENDIF.


            " ***************************************************************************
            " Update and after tier
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-material-update_after_tier.

            LOOP AT lt_material REFERENCE INTO lr_material.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_material->hec_phase_guid IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_material->hec_instance_status.
                lr_material->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_tier[ key = lr_material->parent_key ] TO <fs_tier>.
              IF <fs_tier> IS ASSIGNED.
                lv_release = COND #( WHEN <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                                          <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL AND
                                          <fs_tier>-hec_tier_type_value      IS NOT INITIAL
                                     THEN abap_true
                                     ELSE abap_false                                            ).
              ENDIF.

              IF lv_release <> lr_material->hec_row_selectable.
                lr_material->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify material
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_material->key
                                   is_data = lr_material ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release.
            ENDLOOP.

        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_network_segment.

    DATA: lt_network_segment   TYPE /hec1/t_data_network_segm_ct.

    CLEAR: eo_message,
           et_failed_key,
           me->mr_act_param.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_network_segment ).

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
          WHEN /hec1/if_configuration_c=>sc_determination-network_segment-create.

            LOOP AT lt_network_segment REFERENCE INTO DATA(lr_network_segment).

              "-----------------------------------
              " Get value list quantity
              "-----------------------------------
              lr_network_segment->hec_network_mask_vlqt = COND #( WHEN 1 < lines( /rbp/cl_fpm_utilities=>get_characteristic_values( CONV #( 'HEC_NETWORK_MASK' ) ) )
                                                                  THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                  ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              lr_network_segment->hec_network_type_vlqt = COND #( WHEN 1 < lines( /rbp/cl_fpm_utilities=>get_characteristic_values( CONV #( 'HEC_NETWORK_TYPE_VALUE' ) ) )
                                                                  THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                  ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              "-----------------------------------
              " Modify network segment
              "-----------------------------------
              io_modify->update( iv_node = is_ctx-node_key
                                 iv_key  = lr_network_segment->key
                                 is_data = lr_network_segment ).

            ENDLOOP.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-network_segment-update.

        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD determine_phase.

    DATA: lt_phase             TYPE /hec1/t_data_phase_ct,
          lt_phase_all         TYPE /hec1/t_data_phase_ct,
          lt_phase_before      TYPE /hec1/t_data_phase_ct,
          lt_phase_successor   TYPE /hec1/t_data_phase_ct,
          lt_phase_predecessor TYPE /hec1/t_data_phase_ct,
          lt_act_param         TYPE /hec1/t_act_update_phase,
          lv_date_start(10)    TYPE c,
          lv_date_end(10)      TYPE c.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_phase ).

    io_read->get_root_key( EXPORTING iv_node       = is_ctx-node_key
                                     it_key        = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = lt_root_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                      IMPORTING et_data        = lt_phase_all ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create Mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-phase-create.

            LOOP AT lt_phase REFERENCE INTO DATA(lr_phase).

              TRY.
                  IF lr_phase->hec_node_phase IS INITIAL.
                    lr_phase->hec_node_phase = /rbp/cl_general_utilities=>get_new_guid22( ).
                    DATA(lv_data_changed) = abap_true.
                  ENDIF.

                  "-----------------------------------
                  " Change predecessor assignment
                  "-----------------------------------
                  IF lr_phase->hec_phase_predecessor_guid IS NOT INITIAL.

                    INSERT VALUE #( key                   = lr_phase->key
                                    do_update_predecessor = abap_true
                                    ) INTO TABLE lt_act_param.

                  ENDIF. "predecessor exists

                  "-----------------------------------
                  " Determine Phase Duration
                  "-----------------------------------
                  IF lr_phase->hec_duration_unit    IS NOT INITIAL AND
                     lr_phase->hec_phase_start_date IS NOT INITIAL AND
                     lr_phase->hec_phase_end_date   IS NOT INITIAL.

                    lr_phase->hec_phase_duration = /hec1/cl_config_helper=>calculate_duration( iv_start_date = lr_phase->hec_phase_start_date
                                                                                               iv_end_date   = lr_phase->hec_phase_end_date
                                                                                               iv_unit       = lr_phase->hec_duration_unit ).

                    lv_data_changed = abap_true.
                  ENDIF. " IF lr_phase->hec_duration_unit    IS NOT INITIAL AND

                  "-----------------------------------
                  " Update Tree Description
                  "-----------------------------------
                  IF lr_phase->hec_phase_start_date IS NOT INITIAL
                    AND lr_phase->hec_phase_end_date IS NOT INITIAL.

                    CALL FUNCTION 'CONVERT_DATE_TO_EXTERNAL'
                      EXPORTING
                        date_internal = lr_phase->hec_phase_start_date
                      IMPORTING
                        date_external = lv_date_start.

                    CALL FUNCTION 'CONVERT_DATE_TO_EXTERNAL'
                      EXPORTING
                        date_internal = lr_phase->hec_phase_end_date
                      IMPORTING
                        date_external = lv_date_end.

                    lr_phase->hec_phase_tree_descr = COND #( WHEN lr_phase->hec_phase_predecessor_guid IS NOT INITIAL
                                                             THEN |Successor - { lv_date_start }-{ lv_date_end } - { lr_phase->hec_phase_descr }|
                                                             ELSE |{ lv_date_start }-{ lv_date_end } - { lr_phase->hec_phase_descr }| ) .

                    lv_data_changed = abap_true.

                  ENDIF. "check for tree description update requirement

                  "-----------------------------------
                  " Set Phase complete status
                  "-----------------------------------
                  lr_phase->hec_phase_complete = COND #( WHEN lr_phase->hec_phase_descr IS NOT INITIAL
                                                          AND lr_phase->hec_phase_start_date IS NOT INITIAL
                                                          AND lr_phase->hec_phase_end_date IS NOT INITIAL
                                                          AND lr_phase->hec_phase_start_date <= lr_phase->hec_phase_end_date
                                                         THEN abap_true
                                                         ELSE abap_false ).

                CATCH cx_uuid_error. " Error Class for UUID Processing Errors
              ENDTRY.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_phase->key
                                   is_data = lr_phase ).
              ENDIF.

              CLEAR: lv_data_changed.

            ENDLOOP.

            "-----------------------------------
            " Set Update Predecessor Phase
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              me->mr_act_param_phasing = NEW /hec1/t_act_update_phase( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_phase )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing  ).
            ENDIF.

            " ***************************************************************************
            " Update Mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-phase-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                                         iv_fill_data    = abap_true
                               IMPORTING et_data         = lt_phase_before ).

            LOOP AT lt_phase REFERENCE INTO lr_phase.
              ASSIGN lt_phase_before[ key = lr_phase->key ] TO FIELD-SYMBOL(<fs_phase_before>).

              IF <fs_phase_before> IS ASSIGNED.
                "-----------------------------------
                " Determine Phase Duration
                "-----------------------------------
                IF <fs_phase_before>-hec_phase_start_date <> lr_phase->hec_phase_start_date OR
                   <fs_phase_before>-hec_phase_end_date   <> lr_phase->hec_phase_end_date   OR
                   <fs_phase_before>-hec_duration_unit    <> lr_phase->hec_duration_unit    OR
                   lr_phase->hec_phase_duration              IS INITIAL.

                  IF lr_phase->hec_duration_unit    IS NOT INITIAL AND
                     lr_phase->hec_phase_start_date IS NOT INITIAL AND
                     lr_phase->hec_phase_end_date   IS NOT INITIAL.

                    lr_phase->hec_phase_duration = /hec1/cl_config_helper=>calculate_duration( iv_start_date = lr_phase->hec_phase_start_date
                                                                                               iv_end_date   = lr_phase->hec_phase_end_date
                                                                                               iv_unit       = lr_phase->hec_duration_unit ).

                    lv_data_changed = abap_true.

                  ENDIF.
                ENDIF. " check for phase update

                "-----------------------------------
                " Update Tree Description
                "-----------------------------------
                IF <fs_phase_before>-hec_phase_start_date NE lr_phase->hec_phase_start_date
                  OR <fs_phase_before>-hec_phase_end_date NE lr_phase->hec_phase_end_date
                  OR <fs_phase_before>-hec_phase_descr NE lr_phase->hec_phase_descr
                  OR <fs_phase_before>-hec_phase_predecessor_guid NE lr_phase->hec_phase_predecessor_guid.

                  CALL FUNCTION 'CONVERT_DATE_TO_EXTERNAL'
                    EXPORTING
                      date_internal = lr_phase->hec_phase_start_date
                    IMPORTING
                      date_external = lv_date_start.

                  CALL FUNCTION 'CONVERT_DATE_TO_EXTERNAL'
                    EXPORTING
                      date_internal = lr_phase->hec_phase_end_date
                    IMPORTING
                      date_external = lv_date_end.

                  lr_phase->hec_phase_tree_descr = COND #( WHEN lr_phase->hec_phase_predecessor_guid IS NOT INITIAL
                                                           THEN |Successor - { lv_date_start }-{ lv_date_end } - { lr_phase->hec_phase_descr }|
                                                           ELSE |{ lv_date_start }-{ lv_date_end } - { lr_phase->hec_phase_descr }| ) .

                  lv_data_changed = abap_true.

                ENDIF. "check for tree description update requirement

                "-----------------------------------
                " Phase changed from General
                "  e.g. Successor Changed
                "  This is relevant when a new
                "  successor is created. In that case
                "  the update of the predecessor-phase
                "  is called to update the successor
                "-----------------------------------
                IF lr_phase->hec_update_from_general = abap_true.
                  lv_data_changed = abap_true.
                ENDIF.

*                "-----------------------------------
*                " Start Date or End Date Changed
*                "  when there is a
*                "  successor or predecessor
*                "-----------------------------------
*                IF <fs_phase_before>-hec_phase_successor_guid IS NOT INITIAL
*                  AND <fs_phase_before>-hec_phase_end_date <> lr_phase->hec_phase_end_date
*                  AND <fs_phase_before>-hec_phase_end_date IS NOT INITIAL.
*
*                ENDIF.
*
*                IF <fs_phase_before>-hec_phase_predecessor_guid IS NOT INITIAL
*                  AND <fs_phase_before>-hec_phase_start_date <> lr_phase->hec_phase_start_date
*                  AND <fs_phase_before>-hec_phase_start_date IS NOT INITIAL.
*
*                ENDIF.

                "-----------------------------------
                " Set Phase complete status
                "-----------------------------------
                lr_phase->hec_phase_complete = COND #( WHEN lr_phase->hec_phase_descr IS NOT INITIAL
                                                        AND lr_phase->hec_phase_start_date IS NOT INITIAL
                                                        AND lr_phase->hec_phase_end_date IS NOT INITIAL
                                                        AND lr_phase->hec_phase_start_date <= lr_phase->hec_phase_end_date
                                                       THEN abap_true
                                                       ELSE abap_false ).

              ENDIF. "<fs_phase_before> is assigned.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_phase->key
                                   is_data = lr_phase ).
              ENDIF.

              CLEAR: lv_data_changed.

              UNASSIGN <fs_phase_before>.

            ENDLOOP. "lt_phase
        ENDCASE. "is_ctx

      CATCH /bobf/cx_frw.
      CATCH cx_uuid_error. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD determine_root.

    DATA: lt_root                   TYPE /hec1/t_config_root_ct,
          lt_root_before            TYPE /hec1/t_config_root_ct,
          lt_phase                  TYPE /hec1/t_data_phase_ct,
          lr_default_phase          TYPE REF TO /hec1/s_data_phase_cs,
          lt_act_param              TYPE TABLE OF /bobf/s_frw_key,
          ls_act_param_tier_inherit TYPE /hec1/s_act_update_tier_inhrit,
          lt_act_param_phase        TYPE /hec1/t_act_update_phase.



    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_root ). "root = landscape


    " Get before image
    io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                 it_key          = it_key
                                 iv_before_image = abap_true
                       IMPORTING et_data         = lt_root_before ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-root-create.

            LOOP AT lt_root REFERENCE INTO DATA(lr_root).

              IF ( lr_root->crea_date_time IS INITIAL ).
                GET TIME STAMP FIELD lr_root->crea_date_time.
                lr_root->crea_uname = sy-uname.
              ENDIF.

              lr_root->hec_contract_status         = /hec1/if_config_constants=>gc_contract_status-initial.
              lr_root->hec_node_landscape          = /rbp/cl_general_utilities=>get_new_guid22( ).
              lr_root->hec_landscape_config_status = /hec1/if_status_handler=>gc_landscape_status_values-draft.
              lr_root->hec_cdd_status              = /hec1/if_status_handler=>gc_cdd_status_values-not_requestable.
              lr_root->hec_s2d_status              = /hec1/if_status_handler=>gc_s2d_status_values-not_startable.
              lr_root->hec_fulfillment_status      = /hec1/if_status_handler=>gc_fulfillment_status_values-ls_build_not_startable.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_root->hec_material                IS NOT INITIAL AND
                                                                             lr_root->hec_landscape_descr         IS NOT INITIAL AND
                                                                             lr_root->hec_landscape_config_status IS NOT INITIAL AND
                                                                             lr_root->hec_ls_contract_curr        IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete     ).

              lr_root->hec_delete_visible = abap_false.

              IF lv_inst_status <> lr_root->hec_instance_status.
                lr_root->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_root->key
                                   is_data = lr_root ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

            ENDLOOP.

            "-----------------------------------
            " Set create phase
            " action to general
            "-----------------------------------
            /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                is_ctx          = CORRESPONDING #( is_ctx )
                it_key          = it_key
                iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_phase )
                iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                ).


            "-----------------------------------
            " Set create delivery unit
            " action to general
            "-----------------------------------
            /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                is_ctx          = CORRESPONDING #( is_ctx )
                it_key          = it_key
                iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_delivery_unit )
                iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                ).


            "-----------------------------------
            " Set create managed service baseline
            " action to general
            "-----------------------------------
            /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                is_ctx          = CORRESPONDING #( is_ctx )
                it_key          = it_key
                iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_man_serv_baseline )
                iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation           ).


            " ***************************************************************************
            " update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-root-update.

            " Get before image
            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_root_before ).

            "get the default phase
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).


            LOOP AT lt_root REFERENCE INTO lr_root.
              ASSIGN lt_root_before[ key = lr_root->key ] TO FIELD-SYMBOL(<fs_landscape_before>).

              IF <fs_landscape_before> IS ASSIGNED.
                "-----------------------------------
                " Convert Material to internal
                "-----------------------------------
                CALL FUNCTION 'CONVERSION_EXIT_MATN1_INPUT'
                  EXPORTING
                    input  = lr_root->hec_material
                  IMPORTING
                    output = lr_root->hec_material.

                "-----------------------------------
                " Set APM
                "-----------------------------------
                IF lr_root->hec_apm_guid <> <fs_landscape_before>-hec_apm_guid
               AND lr_root->hec_apm_guid IS NOT INITIAL.

                  SELECT SINGLE *
                    FROM /hec1/a_model
                   WHERE hec_apm_guid = @lr_root->hec_apm_guid
                    INTO CORRESPONDING FIELDS OF @lr_root->*.

                  lv_data_changed = abap_true.

                ENDIF.

                "-----------------------------------
                " Start business rules
                "-----------------------------------
                IF ( lr_root->hec_material <> <fs_landscape_before>-hec_material )
                OR ( lr_root->hec_apm_guid <> <fs_landscape_before>-hec_apm_guid ) .

                  " Get flat material data
                  SELECT SINGLE *
                    FROM /hec1/i_materialbasic
                   WHERE hec_material = @lr_root->hec_material
                    INTO @DATA(ls_material).

                  " Get contract basics
                  SELECT SINGLE *
                    FROM /hec1/i_contractbasic
                   WHERE hec_apm_guid      = @lr_root->hec_apm_guid         AND
                         hec_flat_mat_guid = @ls_material-hec_flat_mat_guid
                    INTO @DATA(ls_contract_basic).

                  lr_root->hec_flat_mat_guid              = ls_material-hec_flat_mat_guid.
                  lr_root->hec_material_opmode_value      = ls_material-hec_mat_oper_mode_value.
                  lr_root->hec_material_opmode_descr      = ls_material-hec_mat_oper_mode_descr.
                  lr_root->hec_material_licmode_value     = ls_material-hec_mat_lice_mode_value.
                  lr_root->hec_material_licmode_descr     = ls_material-hec_mat_lice_mode_descr.
                  lr_root->hec_mat_srvc_mode_value        = ls_material-hec_mat_srvc_mode_value.
                  lr_root->hec_mat_srvc_mode_descr        = ls_material-hec_mat_srvc_mode_descr.
                  lr_root->hec_ls_contract_dur_unit_value = ls_contract_basic-hec_contract_dur_u_value.
                  lr_root->hec_ls_contract_dur_unit_descr = ls_contract_basic-hec_contract_dur_u_descr.
                  lr_root->hec_ls_low_cont_term_limit     = ls_contract_basic-hec_contract_lim_low.
                  lr_root->hec_ls_up_cont_term_limit      = ls_contract_basic-hec_contract_lim_up.
                  lr_root->hec_ls_price_conv_factor       = ls_contract_basic-hec_price_conv_factor.
                  lr_root->hec_ls_uplift_percent          = ls_contract_basic-hec_upflift_percent.

                  lv_data_changed                         = abap_true.

                  "-----------------------------------
                  " Update Access/Delivery Category
                  "-----------------------------------
                  SELECT SINGLE hec_access_dlvy_cat_guid,
                                hec_acccess_dlvy_cat_value,
                                hec_acccess_dlvy_cat_descr
                   FROM /hec1/i_accesdeliverybasic
                   INTO CORRESPONDING FIELDS OF @lr_root->*
                   WHERE hec_apm_guid               = @lr_root->hec_apm_guid      AND
                         hec_flat_mat_guid          = @lr_root->hec_flat_mat_guid AND
                         hec_acc_support_stat_value = '02'.

                  "-----------------------------------
                  " Set Value List Quantity
                  "-----------------------------------

                  " Access Delivery Category
                  lr_root->hec_access_dlvy_cat_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_access_delivery_category(
                                                                                                iv_apm_guid            = lr_root->hec_apm_guid
                                                                                                iv_flat_mat_guid       = lr_root->hec_flat_mat_guid ) )
                                                              THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                              ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                  " Material
                  lr_root->hec_material_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.

*                  " Recurrence Interval
*                  lr_root->hec_nprod_recurrence_int_vlqt = COND #( WHEN 1 < lines( cl_domain=>get_fixed_values( domain_name = '/HEC1/D_PROV_S2D_RECURR_INTV'
*                                                                                                                language    = CONV #( sy-langu ) ) )
*                                                                   THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
*                                                                   ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).
*
*                  lr_root->hec_prod_recurrence_int_vlqt = COND #( WHEN 1 < lines( cl_domain=>get_fixed_values( domain_name = '/HEC1/D_PROV_S2D_RECURR_INTV'
*                                                                                                               language    = CONV #( sy-langu ) ) )
*                                                                  THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
*                                                                  ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                  "-----------------------------------
                  " Fill action table for update
                  " data center
                  "-----------------------------------
                  " - Only after the update can the datacenter type be read from the APM
                  INSERT CORRESPONDING #( lr_root->* ) INTO TABLE lt_act_param.

                ENDIF. " IF lr_root->hec_material <> <fs_landscape_before>-hec_material.

                "-----------------------------------
                " Update Region to Datacenter Level
                "-----------------------------------
                IF lr_root->hec_dlvy_region_l1_guid <> <fs_landscape_before>-hec_dlvy_region_l1_guid OR
                   lr_root->hec_dlvy_region_l2_guid <> <fs_landscape_before>-hec_dlvy_region_l2_guid OR
                   lr_root->hec_country_key         <> <fs_landscape_before>-hec_country_key.

                  " Fill Region L1
                  IF lr_root->hec_dlvy_region_l1_guid <> <fs_landscape_before>-hec_dlvy_region_l1_guid AND
                     lr_root->hec_dlvy_region_l1_guid    IS NOT INITIAL.

                    SELECT SINGLE *
                      FROM /hec1/i_deliveryregionl1basic
                      INTO @DATA(ls_region_l1)
                     WHERE hec_dlvy_region_l1_guid = @lr_root->hec_dlvy_region_l1_guid.

                    lr_root->hec_dlvy_region_l1_descr = ls_region_l1-hec_dlvy_region_l1_descr.
                  ENDIF.

                  " Fill region L2
                  IF lr_root->hec_dlvy_region_l2_guid <> <fs_landscape_before>-hec_dlvy_region_l2_guid AND
                     lr_root->hec_dlvy_region_l2_guid    IS NOT INITIAL.

                    SELECT SINGLE *
                      FROM /hec1/i_deliveryregionl2basic AS l2
                      JOIN /hec1/i_deliveryregionl1basic AS l1
                        ON l2~hec_dlvy_region_l1_guid = l1~hec_dlvy_region_l1_guid
                      INTO @DATA(ls_region_l2)
                     WHERE hec_dlvy_region_l2_guid = @lr_root->hec_dlvy_region_l2_guid.

                    lr_root->hec_dlvy_region_l2_descr = ls_region_l2-l2-hec_dlvy_region_l2_descr.
                    lr_root->hec_dlvy_region_l1_guid  = ls_region_l2-l1-hec_dlvy_region_l1_guid.
                    lr_root->hec_dlvy_region_l1_descr = ls_region_l2-l1-hec_dlvy_region_l1_descr.
                  ENDIF.

                  " Fill region L3 (country)
                  IF lr_root->hec_country_key <> <fs_landscape_before>-hec_country_key AND
                     lr_root->hec_country_key    IS NOT INITIAL.

                    SELECT SINGLE *
                      FROM /hec1/i_deliveryregionl3basic AS l3
                      JOIN /hec1/i_deliveryregionl2basic AS l2
                        ON l3~hec_dlvy_region_l2_guid = l2~hec_dlvy_region_l2_guid
                      JOIN /hec1/i_deliveryregionl1basic AS l1
                        ON l2~hec_dlvy_region_l1_guid = l1~hec_dlvy_region_l1_guid
                      INTO @DATA(ls_region_l3)
                     WHERE l3~hec_country_key = @lr_root->hec_country_key.

                    lr_root->hec_country_descr = ls_region_l3-l3-hec_country_descr.
                    lr_root->hec_dlvy_region_l2_guid  = ls_region_l3-l2-hec_dlvy_region_l2_guid.
                    lr_root->hec_dlvy_region_l2_descr = ls_region_l3-l2-hec_dlvy_region_l2_descr.
                    lr_root->hec_dlvy_region_l1_guid  = ls_region_l3-l1-hec_dlvy_region_l1_guid.
                    lr_root->hec_dlvy_region_l1_descr = ls_region_l3-l1-hec_dlvy_region_l1_descr.
                  ENDIF.

                  " Set Value List Quantity for Regions
                  " !! For now we just set the value to "multi".
                  "   At a later point we might need to restrict the values based on the selected datacenters
                  lr_root->hec_dlvy_region_l1_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.
                  lr_root->hec_dlvy_region_l2_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.
                  lr_root->hec_country_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.

                  "-----------------------------------
                  " Fill action table for update
                  " data center
                  "-----------------------------------
                  INSERT CORRESPONDING #( lr_root->* ) INTO TABLE lt_act_param.

                ENDIF. " IF lr_root->hec_dlvy_region_l1 <> <fs_landscape_before>-hec_dlvy_region_l1 OR

                "-----------------------------------
                " Update Access/Delivery Category
                "-----------------------------------
                IF lr_root->hec_access_dlvy_cat_guid <> <fs_landscape_before>-hec_access_dlvy_cat_guid AND
                   lr_root->hec_access_dlvy_cat_guid    IS NOT INITIAL.

                  SELECT SINGLE *
                    FROM /hec1/i_accesdeliverybasic
                    INTO @DATA(ls_access_delivery)
                    WHERE hec_access_dlvy_cat_guid = @lr_root->hec_access_dlvy_cat_guid.

                  lr_root->hec_acccess_dlvy_cat_descr = ls_access_delivery-hec_acccess_dlvy_cat_descr.
                  lr_root->hec_acccess_dlvy_cat_value = ls_access_delivery-hec_acccess_dlvy_cat_value.
                  lv_data_changed                    = abap_true.

                  lr_root->hec_init_acc_supp_stat_value = ls_access_delivery-hec_acc_support_stat_value.
                  lr_root->hec_init_acc_supp_stat_descr = ls_access_delivery-hec_acc_support_stat_descr.
                  lr_root->hec_acc_support_stat_value   = ls_access_delivery-hec_acc_support_stat_value.
                  lr_root->hec_acc_support_stat_descr   = ls_access_delivery-hec_acc_support_stat_descr.
                ENDIF. " IF lr_root->hec_access_dlvy_cat_guid <> <fs_landscape_before>-hec_access_dlvy_cat_guid AND

                "-----------------------------------
                " Update Currency
                "-----------------------------------
                IF lr_root->hec_ls_contract_curr <> <fs_landscape_before>-hec_ls_contract_curr AND
                   lr_root->hec_ls_contract_curr IS NOT INITIAL.

                  SELECT SINGLE hec_ls_contract_curr, ltext
                    FROM /hec1/i_currency
                   WHERE hec_ls_contract_curr = @lr_root->hec_ls_contract_curr
                    INTO @DATA(ls_currency).

                  lr_root->hec_ls_contract_curr_descr = ls_currency-ltext.

                ENDIF. "contract currency set

                "-----------------------------------
                " Update Start/End date
                "-----------------------------------
                "if we have updates to the Contract Start and End date and if the default phase start and End dates are empty
                " fill the default phase information from Landscape
                IF ( "olds are empty
                    ( <fs_landscape_before>-hec_contract_start_date IS INITIAL AND <fs_landscape_before>-hec_contract_end_date IS INITIAL ) AND
                      " new values
                    (  lr_root->hec_contract_start_date IS NOT INITIAL AND lr_root->hec_contract_end_date IS NOT INITIAL ) ) .

                  TRY.
                      lr_default_phase = NEW #( lt_phase[ hec_default_phase  = abap_true "#EC CI_SORTSEQ
                                                          hec_phase_inactive = abap_false ] ).
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  INSERT VALUE #( key                     = lr_default_phase->key
                                  do_update_def_start_end = abap_true ) INTO TABLE lt_act_param_phase.

                ENDIF.

                "-----------------------------------
                " Change Phasing Duration Unit in all Phases
                "-----------------------------------
                IF lr_root->hec_ls_contract_dur_unit_value NE <fs_landscape_before>-hec_ls_contract_dur_unit_value.

                  LOOP AT lt_phase REFERENCE INTO DATA(lr_phase).

                    INSERT VALUE #( key                     = lr_phase->key
                                    do_update_duration_unit = abap_true ) INTO TABLE lt_act_param_phase.

                  ENDLOOP.
                ENDIF. "contract duration unit changed

                "-----------------------------------
                " Change Tree description
                "-----------------------------------
                IF <fs_landscape_before>-hec_landscape_descr <> lr_root->hec_landscape_descr.
                  lr_root->hec_tree_descr = lr_root->hec_landscape_descr. "#EC CI_FLDEXT_OK[2215424]
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Inherit System Timezone
                " Recurrence Type, Recurence Interval, Weekday
                "-----------------------------------
                IF <fs_landscape_before>-hec_system_timezone <> lr_root->hec_system_timezone.
                  ls_act_param_tier_inherit-do_update_timezone = abap_true.
                  lv_data_changed = abap_true.
                ENDIF.

                "Production
                IF <fs_landscape_before>-hec_prod_recurrence_type <> lr_root->hec_prod_recurrence_type
                OR <fs_landscape_before>-hec_prod_recurrence_interval <> lr_root->hec_prod_recurrence_interval
                OR <fs_landscape_before>-hec_prod_weekday <> lr_root->hec_prod_weekday
                OR <fs_landscape_before>-hec_prod_starttime <> lr_root->hec_prod_starttime
                OR <fs_landscape_before>-hec_prod_duration <> lr_root->hec_prod_duration
                OR <fs_landscape_before>-hec_prod_duration_unit <> lr_root->hec_prod_duration_unit
                OR <fs_landscape_before>-hec_prod_cmp_timezone <> lr_root->hec_prod_cmp_timezone.
                  ls_act_param_tier_inherit-do_update_prod = abap_true.
                  lv_data_changed = abap_true.
                ENDIF.

                "Non-Production
                IF <fs_landscape_before>-hec_nprod_recurrence_type <> lr_root->hec_prod_recurrence_type
                OR <fs_landscape_before>-hec_nprod_recurrence_interval <> lr_root->hec_prod_recurrence_interval
                OR <fs_landscape_before>-hec_nprod_weekday <> lr_root->hec_prod_weekday
                OR <fs_landscape_before>-hec_nprod_starttime <> lr_root->hec_nprod_starttime
                OR <fs_landscape_before>-hec_nprod_duration <> lr_root->hec_nprod_duration
                OR <fs_landscape_before>-hec_nprod_duration_unit <> lr_root->hec_nprod_duration_unit
                OR <fs_landscape_before>-hec_nprod_cmp_timezone <> lr_root->hec_nprod_cmp_timezone.
                  ls_act_param_tier_inherit-do_update_nonprod = abap_true.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Convert Material to internal
                "-----------------------------------
                CALL FUNCTION 'CONVERSION_EXIT_MATN1_INPUT'
                  EXPORTING
                    input  = lr_root->hec_material
                  IMPORTING
                    output = lr_root->hec_material.

                lv_data_changed = abap_true.
              ENDIF. "<fs_landscape_before> is not initial

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_root->hec_material                IS NOT INITIAL AND
                                                                       lr_root->hec_landscape_descr         IS NOT INITIAL AND
                                                                       lr_root->hec_landscape_config_status IS NOT INITIAL AND
                                                                       lr_root->hec_ls_contract_curr        IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete     ).

              lr_root->hec_delete_visible = abap_false.

              IF lv_inst_status <> lr_root->hec_instance_status.
                lr_root->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_root->key
                                   is_data = lr_root ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_landscape_before>.
            ENDLOOP.


            "-----------------------------------
            " Set Update datacenter
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_datacenter )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation  ).
            ENDIF.


            "-----------------------------------
            " Set Update Tier
            " action to general
            "-----------------------------------
            IF ls_act_param_tier_inherit IS NOT INITIAL.
              me->mr_act_param1 = NEW /hec1/s_act_update_tier_inhrit( ls_act_param_tier_inherit ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_tier_from_landscape )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = mr_act_param1 ).
            ENDIF.


            "-----------------------------------
            " Set Update Phase
            " action to general
            "-----------------------------------
            IF lt_act_param_phase IS NOT INITIAL.
              mr_act_param = NEW /hec1/t_act_update_phase( lt_act_param_phase ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-phase )
                  it_key          = VALUE #( FOR phase IN lt_act_param_phase
                                             ( key = phase-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_phase )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = mr_act_param  ).
            ENDIF.
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_solution.

    DATA: lt_solution         TYPE /hec1/t_data_solution_ct,
          lt_solution_before  TYPE /hec1/t_data_solution_ct,
          lt_act_param        TYPE /hec1/t_act_create_tier,
          ls_act_param        LIKE LINE OF lt_act_param,
          lt_act_param_tier   TYPE /hec1/t_act_update_tier,
          ls_landscape        TYPE /hec1/s_config_root_cs,
          lt_tier             TYPE /hec1/t_data_tier_ct,
          lt_act_param_delete TYPE /bobf/t_frw_node,

          ls_field_usage      TYPE fpmgb_s_fieldusage.

    CLEAR: eo_message,
           et_failed_key.


    DATA(ls_fpm_runtime_info) = cl_fpm_factory=>get_instance( )->get_runtime_info( ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit) ).

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_solution ).

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
          WHEN /hec1/if_configuration_c=>sc_determination-solution-create.
            LOOP AT lt_solution REFERENCE INTO DATA(lr_solution).

              lr_solution->hec_delete_visible = abap_true.
              lr_solution->hec_delete_visible = abap_true.
              lr_solution->hec_row_selectable = abap_true.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_solution->hec_solution_guid IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_solution->hec_instance_status.
                lr_solution->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Get value list quantity
              "-----------------------------------
              " HEC_SOL_IMPL_TYPE_VALUE
              lr_solution->hec_sol_impl_type_vlqt = COND #( WHEN lines( /rbp/cl_fpm_utilities=>get_characteristic_values( CONV #( /hec1/if_configuration_c=>sc_node_attribute-solution-hec_sol_impl_type_value ) ) ) > 1
                                                            THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                            ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " HEC_SOL_LANGUAGE_SYS_DEF
              /hec1/cl_config_utilities=>get_language_value_list( EXPORTING iv_exclude_spras  = lr_solution->hec_sol_language_sys_alt
                                                                            it_language_table = CONV #( /hec1/cl_prov_utility=>conv_csv_to_table( iv_csv = CONV #( lr_solution->hec_sol_language_list ) ) )
                                                                  CHANGING  cs_field_usage    = ls_field_usage ).

              lr_solution->hec_sol_language_sys_def_vlqt = COND #( WHEN 1 < lines( ls_field_usage-fixed_values )
                                                                   THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                   ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              CLEAR ls_field_usage.

              " HEC_SOL_LANGUAGE_SYS_ALT
              /hec1/cl_config_utilities=>get_language_value_list_lim( EXPORTING iv_exclude_spras  = lr_solution->hec_sol_language_sys_def
                                                                                it_language_table = CONV #( /hec1/cl_prov_utility=>conv_csv_to_table( iv_csv = CONV #( lr_solution->hec_sol_language_list ) ) )
                                                                      CHANGING  cs_field_usage    = ls_field_usage ).

              lr_solution->hec_sol_language_sys_alt_vlqt = COND #( WHEN 1 < lines( ls_field_usage-fixed_values )
                                                                   THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                   ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              CLEAR ls_field_usage.

              "-----------------------------------
              " Set APM model
              "-----------------------------------
              IF lr_solution->hec_apm_guid  IS INITIAL.
                lr_solution->hec_apm_guid  = ls_landscape-hec_apm_guid.
                lr_solution->hec_apm_descr = ls_landscape-hec_apm_descr.

                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify solution
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_solution->key
                                   is_data = lr_solution ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-solution-update.

            " Data before update
            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_solution_before ).

            " Get tier
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                                        iv_fill_data   = abap_true
                                              IMPORTING et_data        = lt_tier ).


            LOOP AT lt_solution REFERENCE INTO lr_solution.
              ASSIGN lt_solution_before[ key = lr_solution->key ] TO FIELD-SYMBOL(<fs_sol_before>).

              IF <fs_sol_before> IS ASSIGNED.
                "-----------------------------------
                " Set Solution
                "-----------------------------------
                IF lr_solution->hec_solution_guid    IS NOT INITIAL                     AND
                   lr_solution->hec_solution_guid <> <fs_sol_before>-hec_solution_guid.

                  " Get Solution
                  SELECT SINGLE *
                    FROM /hec1/i_solutionbasic
                   WHERE hec_apm_guid      = @lr_landscape->hec_apm_guid     AND
                         hec_solution_guid = @lr_solution->hec_solution_guid
                    INTO CORRESPONDING FIELDS OF @lr_solution->*.

                  IF lr_solution->hec_initial_support_stat_value IS INITIAL.
                    lr_solution->hec_initial_support_stat_value = lr_solution->hec_support_stat_value.
                    lr_solution->hec_initial_support_stat_descr = lr_solution->hec_support_stat_descr.
                  ENDIF.

                  " Set solution material
                  /hec1/cl_config_sw_helper=>get_instance( )->/hec1/if_config_sw_helper~set_material_list( iv_apm_guid      = lr_landscape->hec_apm_guid
                                                                                                           iv_solution_guid = lr_solution->hec_solution_guid
                                                                                                           iv_node_solution = lr_solution->hec_node_solution ).

                  " Set Software Item ( included item stack )
                  /hec1/cl_config_sw_helper=>get_instance( )->/hec1/if_config_sw_helper~set_software_item_list( iv_apm_guid      = lr_landscape->hec_apm_guid
                                                                                                                iv_solution_guid = lr_solution->hec_solution_guid
                                                                                                                iv_node_solution = lr_solution->hec_node_solution ).
                ENDIF. " IF lr_solution->hec_solution_guid IS NOT INITIAL AND...


                "-----------------------------------
                " Set solution description
                "-----------------------------------
                IF lr_solution->hec_solution_guid IS NOT INITIAL.

                  SELECT SINGLE hec_sol_alias_descr
                    FROM /hec1/i_solutionbasic
                   WHERE hec_apm_guid      = @lr_landscape->hec_apm_guid     AND
                         hec_solution_guid = @lr_solution->hec_solution_guid
                    INTO @lr_solution->hec_sol_alias_descr.

                  IF lr_solution->hec_sol_alias_descr_ext IS INITIAL.
                    lr_solution->hec_sol_alias_descr_ext = lr_solution->hec_sol_alias_descr.
                  ENDIF.

                  lr_solution->hec_tree_descr = | { lr_solution->hec_sol_alias_descr  } : { lr_solution->hec_sol_alias_descr_ext } |. "#EC CI_FLDEXT_OK[2215424]
                  lv_data_changed             = abap_true.
                ENDIF. " IF lr_solution->hec_solution_guid IS NOT INITIAL.


                "-----------------------------------
                " Set implementation type descr
                "-----------------------------------
                IF lr_solution->hec_sol_impl_type_value IS NOT INITIAL                              AND
                   lr_solution->hec_sol_impl_type_value <> <fs_sol_before>-hec_sol_impl_type_value.
                  DATA(lt_value_list) = /rbp/cl_fpm_utilities=>get_characteristic_values( CONV #( /hec1/if_configuration_c=>sc_node_attribute-solution-hec_sol_impl_type_value ) ).
                  IF lt_value_list IS NOT INITIAL.
                    ASSIGN lt_value_list[ value = lr_solution->hec_sol_impl_type_value ]-text TO FIELD-SYMBOL(<fs_descr>).

                    IF <fs_descr> IS ASSIGNED.
                      lr_solution->hec_sol_impl_type_descr = <fs_descr>.
                      UNASSIGN <fs_descr>.
                    ENDIF.
                  ENDIF. " IF lt_value_list IS NOT INITIAL.
                ENDIF. " IF lr_solution->hec_sol_impl_type_value IS NOT INITIAL AND...


                "-----------------------------------
                " New tiers are added
                "-----------------------------------
                IF <fs_sol_before>-hec_tier_qty_nprod_level <> lr_solution->hec_tier_qty_nprod_level OR
                   <fs_sol_before>-hec_tier_qty_prod_level  <> lr_solution->hec_tier_qty_prod_level.

                  " The number of tiers need to be checked as well. If a node is deleted the amount of tiers on solution level need to be adjusted
                  DATA(lt_tier_prod) = VALUE /hec1/t_data_tier_ct( FOR tier IN lt_tier
                                                                   WHERE ( parent_key = lr_solution->key AND
                                                                           hec_tier_cat_value = /hec1/if_config_constants=>gc_tier_category-prod )
                                                                   ( tier ) ).

                  DATA(lt_tier_nonprod) = VALUE /hec1/t_data_tier_ct( FOR tier IN lt_tier
                                                                      WHERE ( parent_key = lr_solution->key AND
                                                                              hec_tier_cat_value = /hec1/if_config_constants=>gc_tier_category-nonprod )
                                                                      ( tier ) ).

                  "-----------------------------------
                  " Non production tier
                  "-----------------------------------
                  IF lr_solution->hec_tier_qty_nprod_level > <fs_sol_before>-hec_tier_qty_nprod_level.
                    ls_act_param = VALUE #( key             = lr_solution->key
                                            hec_tier_qty_nprod_level = lr_solution->hec_tier_qty_nprod_level - <fs_sol_before>-hec_tier_qty_nprod_level ).

                    " Success message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_non_prod_tier_added
                                                                   iv_severity = /bobf/cm_frw=>co_severity_success
                                                                   iv_attr1    = CONV #( ls_act_param-hec_tier_qty_nprod_level )
                                                         CHANGING  co_message  = eo_message ).

                  ELSEIF lr_solution->hec_tier_qty_nprod_level < <fs_sol_before>-hec_tier_qty_nprod_level
                    AND lr_solution->hec_tier_qty_nprod_level < lines( lt_tier_nonprod ).
                    DATA(lv_attr_name) = /hec1/if_configuration_c=>sc_node_attribute-solution-hec_tier_qty_nprod_level.

                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_solution->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_solution->hec_tier_qty_nprod_level = <fs_sol_before>-hec_tier_qty_nprod_level.
                    lv_data_changed = abap_true.

                  ELSEIF <fs_sol_before>-hec_tier_qty_nprod_level > lines( lt_tier_nonprod ).
                    lv_data_changed = abap_true.

                  ENDIF. " IF lr_solution->hec_tier_qty_nprod_level > <fs_sol_before>-hec_tier_qty_nprod_level.

                  "-----------------------------------
                  " Production tier
                  "-----------------------------------
                  IF lr_solution->hec_tier_qty_prod_level > <fs_sol_before>-hec_tier_qty_prod_level.
                    ls_act_param-key             = lr_solution->key.
                    ls_act_param-hec_tier_qty_prod_level = lr_solution->hec_tier_qty_prod_level - <fs_sol_before>-hec_tier_qty_prod_level.

                    " Success message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_prod_tier_added
                                                                   iv_severity = /bobf/cm_frw=>co_severity_success
                                                                   iv_attr1    = CONV #( ls_act_param-hec_tier_qty_prod_level )
                                                         CHANGING  co_message  = eo_message ).


                  ELSEIF lr_solution->hec_tier_qty_prod_level < <fs_sol_before>-hec_tier_qty_prod_level
                    AND lr_solution->hec_tier_qty_prod_level < lines( lt_tier_prod ).
                    CLEAR lv_attr_name.
                    lv_attr_name = /hec1/if_configuration_c=>sc_node_attribute-solution-hec_tier_qty_prod_level.
                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_solution->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_solution->hec_tier_qty_prod_level = <fs_sol_before>-hec_tier_qty_prod_level.
                    lv_data_changed = abap_true.

                  ELSEIF <fs_sol_before>-hec_tier_qty_prod_level > lines( lt_tier_prod ).
                    lv_data_changed = abap_true.

                  ENDIF. " IF lr_solution->hec_tier_qty_nprod_level > <fs_sol_before>-hec_tier_qty_nprod_level.

                  IF ls_act_param IS NOT INITIAL.
                    INSERT ls_act_param INTO TABLE lt_act_param.
                    CLEAR ls_act_param.
                  ENDIF.

                ENDIF. " IF <fs_sol_before>-hec_tier_qty_nprod_level <> lr_solution->hec_tier_qty_nprod_level OR...

                "-----------------------------------
                " Reset fields
                "-----------------------------------
                IF lr_solution->hec_solution_guid    IS     INITIAL AND
                   <fs_sol_before>-hec_solution_guid IS NOT INITIAL.

                  "Reset all other fields besides the following:
                  lr_solution->content = VALUE #( LET old = lr_solution->* IN
                                                 hec_apm_guid  = old-hec_apm_guid
                                                 hec_apm_descr = old-hec_apm_descr
                                                 technical     = old-technical
                                                 cdd           = old-cdd
                                                 status        = old-status
                                                 descr         = old-descr
                                                 fpm           = old-fpm
                                                 admin_data    = old-admin_data    ).

                  " reset software lists
                  " Reset solution material for solution
                  /hec1/cl_config_sw_helper=>get_instance( )->/hec1/if_config_sw_helper~delete_solution_list( lr_solution->hec_node_solution ).

                  " Add tiers to delete table
                  LOOP AT lt_tier ASSIGNING FIELD-SYMBOL(<fs_tier>)
                    WHERE parent_key = lr_solution->key.

                    INSERT VALUE #( node = /hec1/if_configuration_c=>sc_node-tier
                                    key  = <fs_tier>-key                           ) INTO TABLE lt_act_param_delete.
                  ENDLOOP.

                  lv_data_changed = abap_true.

                ENDIF. " IF is_solution-hec_solution_guid    IS INITIAL     AND

                "-----------------------------------
                " Update Language to Tier
                "-----------------------------------
                IF <fs_sol_before>-hec_sol_language_sys_alt NE lr_solution->hec_sol_language_sys_alt
                  OR <fs_sol_before>-hec_sol_language_sys_def NE lr_solution->hec_sol_language_sys_def
                  OR <fs_sol_before>-hec_sol_language_list NE lr_solution->hec_sol_language_list.

                  LOOP AT lt_tier ASSIGNING <fs_tier>
                    WHERE parent_key = lr_solution->key.

                    " every key in the parameter table should only exist once.
                    ASSIGN lt_act_param_tier[ key        = <fs_tier>-key
                                              parent_key = <fs_tier>-parent_key ] TO FIELD-SYMBOL(<fs_act_param_tier>).

                    IF <fs_act_param_tier> IS ASSIGNED.
                      <fs_act_param_tier>-do_update_language = abap_true.
                    ELSE.
                      INSERT VALUE #( key                = <fs_tier>-key
                                      parent_key         = <fs_tier>-parent_key
                                      do_update_language = abap_true ) INTO TABLE lt_act_param_tier.
                    ENDIF.

                  ENDLOOP. "lt_tier
                ENDIF. "language changed

                "-----------------------------------
                " Update Business Function
                " Activation to Tier
                "-----------------------------------
                IF <fs_sol_before>-hec_bf_activation NE lr_solution->hec_bf_activation.
                  LOOP AT lt_tier ASSIGNING <fs_tier>
                    WHERE parent_key = lr_solution->key.

                    " every key in the parameter table should only exist once.
                    ASSIGN lt_act_param_tier[ key        = <fs_tier>-key
                                              parent_key = <fs_tier>-parent_key ] TO <fs_act_param_tier>.

                    IF <fs_act_param_tier> IS ASSIGNED.
                      <fs_act_param_tier>-do_update_bf_activation = abap_true.
                    ELSE.
                      INSERT VALUE #( key                     = <fs_tier>-key
                                      parent_key              = <fs_tier>-parent_key
                                      do_update_bf_activation = abap_true ) INTO TABLE lt_act_param_tier.
                    ENDIF.

                  ENDLOOP. "lt_tier
                ENDIF. "IF <fs_sol_before>-hec_bf_activation NE lr_solution->hec_bf_activation.

                "-----------------------------------
                " Update BP Activation: Template
                " sent to customer to Tier
                "-----------------------------------
                IF <fs_sol_before>-hec_bpacti_tmpl_sent_to_cust NE lr_solution->hec_bpacti_tmpl_sent_to_cust.
                  LOOP AT lt_tier ASSIGNING <fs_tier>
                    WHERE parent_key = lr_solution->key.

                    " every key in the parameter table should only exist once.
                    ASSIGN lt_act_param_tier[ key        = <fs_tier>-key
                                              parent_key = <fs_tier>-parent_key ] TO <fs_act_param_tier>.

                    IF <fs_act_param_tier> IS ASSIGNED.
                      <fs_act_param_tier>-do_update_bf_tmpl_sent_to_cust = abap_true.
                    ELSE.
                      INSERT VALUE #( key                            = <fs_tier>-key
                                      parent_key                     = <fs_tier>-parent_key
                                      do_update_bf_tmpl_sent_to_cust = abap_true ) INTO TABLE lt_act_param_tier.
                    ENDIF.

                  ENDLOOP. "lt_tier
                ENDIF. "IF <fs_sol_before>-hec_bpacti_tmpl_sent_to_cust NE lr_solution->hec_bpacti_tmpl_sent_to_cust.

                "-----------------------------------
                " Update BP Activation: Template
                " upload to customer to Tier
                "-----------------------------------
                IF <fs_sol_before>-hec_bpacti_tmpl_upl_by_cust NE lr_solution->hec_bpacti_tmpl_upl_by_cust.
                  LOOP AT lt_tier ASSIGNING <fs_tier>
                    WHERE parent_key = lr_solution->key.

                    " every key in the parameter table should only exist once.
                    ASSIGN lt_act_param_tier[ key        = <fs_tier>-key
                                              parent_key = <fs_tier>-parent_key ] TO <fs_act_param_tier>.

                    IF <fs_act_param_tier> IS ASSIGNED.
                      <fs_act_param_tier>-do_update_bf_tmpl_upl_by_cust = abap_true.
                    ELSE.
                      INSERT VALUE #( key                           = <fs_tier>-key
                                      parent_key                    = <fs_tier>-parent_key
                                      do_update_bf_tmpl_upl_by_cust = abap_true ) INTO TABLE lt_act_param_tier.
                    ENDIF.

                  ENDLOOP. "lt_tier
                ENDIF. "IF <fs_sol_before>-hec_bpacti_tmpl_upl_by_cust NE lr_solution->hec_bpacti_tmpl_upl_by_cust.

                "-----------------------------------
                " Update DB Version to Tier
                "-----------------------------------
                IF <fs_sol_before>-hec_sol_db_version_guid NE lr_solution->hec_sol_db_version_guid.

                  LOOP AT lt_tier ASSIGNING <fs_tier>
                    WHERE parent_key = lr_solution->key.

                    " every key in the parameter table should only exist once.
                    ASSIGN lt_act_param_tier[ key        = <fs_tier>-key
                                              parent_key = <fs_tier>-parent_key ] TO <fs_act_param_tier>.

                    IF <fs_act_param_tier> IS ASSIGNED.
                      <fs_act_param_tier>-do_update_db_version = abap_true.
                    ELSE.
                      INSERT VALUE #( key                  = <fs_tier>-key
                                      parent_key           = <fs_tier>-parent_key
                                      do_update_db_version = abap_true ) INTO TABLE lt_act_param_tier.
                    ENDIF.

                  ENDLOOP. "lt_tier
                ENDIF. "language changed

                "-----------------------------------
                " Update Implementation type to Tier
                "-----------------------------------
                IF <fs_sol_before>-hec_sol_impl_type_value NE lr_solution->hec_sol_impl_type_value.

                  LOOP AT lt_tier ASSIGNING <fs_tier>
                    WHERE parent_key = lr_solution->key.

                    " every key in the parameter table should only exist once.
                    ASSIGN lt_act_param_tier[ key        = <fs_tier>-key
                                              parent_key = <fs_tier>-parent_key ] TO <fs_act_param_tier>.

                    IF <fs_act_param_tier> IS ASSIGNED.
                      <fs_act_param_tier>-do_update_impl_type = abap_true.
                    ELSE.
                      INSERT VALUE #( key                = <fs_tier>-key
                                      parent_key         = <fs_tier>-parent_key
                                      do_update_impl_type = abap_true ) INTO TABLE lt_act_param_tier.
                    ENDIF.

                  ENDLOOP. "lt_tier
                ENDIF. "Implementation type changed

              ENDIF. " IF <fs_sol_before> IS ASSIGNED.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_solution->hec_solution_guid IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).


              IF lv_inst_status <> lr_solution->hec_instance_status.
                lr_solution->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify solution
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_solution->key
                                   is_data = lr_solution ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_attr_name,
                     lv_data_changed,
                     lt_value_list,
                     lt_tier_nonprod,
                     lt_tier_prod.

              UNASSIGN <fs_sol_before>.
            ENDLOOP. " LOOP AT lt_solution REFERENCE INTO lr_solution.

            "-----------------------------------
            " Set update tier to GENERAL
            "-----------------------------------
            IF lt_act_param_tier IS NOT INITIAL.
              me->mr_act_param1 = NEW /hec1/t_act_update_tier( lt_act_param_tier ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-tier )
                  it_key          = VALUE #( FOR act_tier IN lt_act_param_tier
                                            ( key = act_tier-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_tier )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = mr_act_param1 ).
            ENDIF.

            "-----------------------------------
            " Set create tier action to GENERAL
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              me->mr_act_param = NEW /hec1/t_act_create_tier( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_db_si IN lt_act_param
                                            ( key = wa_db_si-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_tier )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                   ).
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
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD determine_sw_item.

    DATA: lt_material          TYPE /hec1/t_data_material_ct,
          lt_sw_item           TYPE /hec1/t_data_sw_item_ct,
          lt_sw_item_before    TYPE /hec1/t_data_sw_item_ct,
          lt_phase             TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key                                                                "
                       IMPORTING et_data = lt_sw_item ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create and update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-software_item-create                OR
               /hec1/if_configuration_c=>sc_determination-software_item-update                OR
               /hec1/if_configuration_c=>sc_determination-software_item-update_after_material.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true                                                                "
                               IMPORTING et_data         = lt_sw_item_before ).

            " Get material
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-software_item-to_parent
                                              IMPORTING et_data        = lt_material ).


            LOOP AT lt_sw_item REFERENCE INTO DATA(lr_sw_item).

              lr_sw_item->hec_tree_descr = lr_sw_item->hec_sw_item_hsp_name.

              ASSIGN lt_sw_item_before[ key = lr_sw_item->key ] TO FIELD-SYMBOL(<fs_sw_item_before>).
              IF <fs_sw_item_before> IS ASSIGNED.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_sw_item->hec_phase_guid NE <fs_sw_item_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_sw_item->key
                                  hec_phase_guid_new = lr_sw_item->hec_phase_guid
                                  hec_phase_guid_old = <fs_sw_item_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_sw_item->hec_phase_changed = abap_true.
                  DATA(lv_data_changed) = abap_true.

                ENDIF. "phasing changed
              ENDIF. "<fs_sw_item_before> is assigned.

              "-----------------------------------
              " Check and switch instance status
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_sw_item->hec_phase_guid IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              lr_sw_item->hec_delete_visible = abap_false.

              IF lv_inst_status <> lr_sw_item->hec_instance_status.
                lr_sw_item->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              " Release instance for selection
              ASSIGN lt_material[ key = lr_sw_item->parent_key ] TO FIELD-SYMBOL(<fs_material>).

              IF <fs_material> IS ASSIGNED.
                IF <fs_material>-hec_row_selectable <> lr_sw_item->hec_row_selectable.
                  lr_sw_item->hec_row_selectable = <fs_material>-hec_row_selectable.
                  lv_data_changed = abap_true.
                ENDIF.
              ENDIF.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_sw_item->key
                                   is_data = lr_sw_item ).
              ENDIF.

              UNASSIGN <fs_material>.
              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP. " LOOP AT lt_sw_item REFERENCE INTO ls_sw_item.

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

        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_tier.

    DATA: lt_tier               TYPE /hec1/t_data_tier_ct,
          lt_tier_before        TYPE /hec1/t_data_tier_ct,
          lt_alt_key            TYPE TABLE OF /hec1/datacenter_guid,
          lt_act_param          TYPE /hec1/t_act_create_serv_inst,
          lt_act_param_sla      TYPE /hec1/t_act_create_tier_sla,
          lt_db_serv_inst       TYPE /hec1/t_data_db_server_inst_ct,
          lt_app_serv_inst      TYPE /hec1/t_data_app_serv_inst_ct,
          ls_landscape          TYPE /hec1/s_config_root_cs,
          lt_phase              TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing  TYPE TABLE OF /hec1/s_act_phase_inherit,
          lt_act_param_material TYPE /hec1/t_act_create_material,

          ls_field_usage        TYPE fpmgb_s_fieldusage.


    CLEAR: eo_message,
           et_failed_key,
           me->mr_act_param,
           me->mr_act_param1,
           me->mr_act_param_sla.

    " Data before update
    io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                 it_key          = it_key
                                 iv_before_image = abap_true
                       IMPORTING et_data         = lt_tier_before ).

    " Data after update
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_tier ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit)
                                                        et_datacenter    = DATA(lt_datacenter) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier-create.

            LOOP AT lt_tier REFERENCE INTO DATA(lr_tier).

              "-----------------------------------
              " Set default client to 100, 000 is not allowed.
              "-----------------------------------

              lr_tier->hec_tier_requ_client_def = 100.

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              " Tier Type
              lr_tier->hec_tier_type_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_tier_type(
                                                                      iv_apm_guid       = lr_landscape->hec_apm_guid
                                                                      iv_flat_mat_guid  = lr_landscape->hec_flat_mat_guid
                                                                      iv_tier_cat_value = lr_tier->hec_tier_cat_value ) )
                                                    THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                    ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              " HEC_TIER_IMPL_TYPE_VALUE
              lr_tier->hec_tier_impl_type_vlqt = COND #( WHEN 1 < lines( /rbp/cl_fpm_utilities=>get_characteristic_values( CONV #( 'HEC_SOL_IMPL_TYPE_VALUE' ) ) )
                                                         THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                         ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              lr_tier->hec_delete_visible = abap_true.

              "-----------------------------------
              " Get data center decription
              "-----------------------------------
              IF lt_datacenter IS NOT INITIAL.
                TRY.
                    DATA(lv_datacenter_descr) = lt_datacenter[ hec_node_datacenter = lr_tier->hec_tier_datacenter_guid ]-hec_datacenter_descr.
                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_tier->hec_tier_descr           IS NOT INITIAL AND
                                                                             lr_tier->hec_tier_impl_type_value IS NOT INITIAL AND
                                                                             lr_tier->hec_tier_type_value      IS NOT INITIAL AND
                                                                             lr_tier->hec_phase_guid           IS NOT INITIAL AND
                                                                             lr_tier->hec_tier_datacenter_guid IS NOT INITIAL AND
                                                                             lv_datacenter_descr               IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_tier->hec_instance_status.
                lr_tier->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " DB/App server instance
              "-----------------------------------
              IF lr_tier->hec_db_srv_required  = abap_true  OR
                 lr_tier->hec_app_srv_required = abap_true.
                INSERT VALUE #( key                    = lr_tier->key
                                hec_db_srv_qty         = COND #( WHEN lr_tier->hec_db_srv_required = abap_true
                                                                 THEN lr_tier->hec_db_srv_qty
                                                                  ELSE 0                                        )
                                hec_app_srv_qty        = COND #( WHEN lr_tier->hec_app_srv_required = abap_true
                                                                 THEN lr_tier->hec_app_srv_qty
                                                                 ELSE 0                                         )
                                hec_default_server_inst = abap_true                                               ) INTO TABLE lt_act_param.
              ENDIF.

              "-----------------------------------
              " Implementation Type already set
              "   if implementation type is "Greenfield"
              "   the migration scenario needs to be set to
              "   "No migration"
              "-----------------------------------
              IF lr_tier->hec_tier_impl_type_value = /hec1/if_config_constants=>gc_tier_impl_type-greenfield.
                lr_tier->hec_tier_migr_scen_value = 'GR_NoMig'.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Tier is DR Tier
              "-----------------------------------
              IF lr_tier->hec_tier_is_dr_node = abap_true.
                lr_tier->hec_tree_descr = |(DR) { lr_tier->hec_tree_descr }|.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " Material
              "-----------------------------------
              INSERT VALUE #( parent_key = lr_tier->key ) INTO TABLE lt_act_param_material.

              "-----------------------------------
              " Fill action table for create
              " Tier SLA
              "-----------------------------------
              INSERT VALUE #( parent_key = lr_tier->key ) INTO TABLE lt_act_param_sla.

              "-----------------------------------
              " Modify tier
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_tier->key
                                   is_data = lr_tier ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_datacenter_descr,
                     lv_data_changed,
                     lt_datacenter.
            ENDLOOP.

            "-----------------------------------
            " Set create Tier SLA
            " action to general
            "-----------------------------------
            IF lt_act_param_sla IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_tier_sla )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                  ).
            ENDIF.


            "-----------------------------------
            " Set create DB/App server instance
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_serv_inst( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_serv_inst )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                  ).
            ENDIF.


            "-----------------------------------
            " Set Follow-Up to GENERAL
            " - Create Material
            "-----------------------------------
            IF lt_act_param_material IS NOT INITIAL.

              me->mr_act_param_material_add = NEW /hec1/t_act_create_material( lt_act_param_material ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                   is_ctx          = CORRESPONDING #( is_ctx )
                   it_key          = VALUE #( FOR mat_add IN lt_act_param_material
                                            ( key = mat_add-parent_key ) )
                   iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_material )
                   iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                   ir_act_param    = me->mr_act_param_material_add ).
            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier-update.

            " DB Server Instance
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier-db_server_instance
                                              IMPORTING et_data        = lt_db_serv_inst ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " App Server Instance
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier-app_server_instance
                                              IMPORTING et_data        = lt_app_serv_inst ).

            " DB Server Instance
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier-db_server_instance
                                              IMPORTING et_data        = lt_db_serv_inst ).



            LOOP AT lt_tier REFERENCE INTO lr_tier.
              "-----------------------------------
              " Get data center decription
              "-----------------------------------
              IF lt_datacenter IS NOT INITIAL.
                TRY.
                    lv_datacenter_descr = lt_datacenter[ hec_node_datacenter = lr_tier->hec_tier_datacenter_guid ]-hec_datacenter_descr.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.

              ASSIGN lt_tier_before[ key = lr_tier->key ] TO FIELD-SYMBOL(<fs_tier_before>).
              IF <fs_tier_before> IS ASSIGNED.

                "-----------------------------------
                " Tier type or tier description
                " has changed
                "-----------------------------------
                IF lr_tier->hec_tier_type_value <> <fs_tier_before>-hec_tier_type_value OR
                   lr_tier->hec_tier_descr      <> <fs_tier_before>-hec_tier_descr      OR
                   lr_tier->hec_tier_sid        <> <fs_tier_before>-hec_tier_sid.

                  " Get tier type description and DR option
                  SELECT SINGLE *
                   FROM /hec1/i_tiertypebasic
                  WHERE hec_apm_guid        = @lr_landscape->hec_apm_guid      AND
                        hec_flat_mat_guid   = @lr_landscape->hec_flat_mat_guid AND
                        hec_tier_type_value = @lr_tier->hec_tier_type_value
                   INTO CORRESPONDING FIELDS OF @lr_tier->*.

                  DATA(lv_tier_description) = |{ lr_tier->hec_tier_type_descr }{
                                                      COND #( WHEN lr_tier->hec_tier_type_value IS INITIAL OR
                                                                   lr_tier->hec_tier_descr      IS INITIAL
                                                              THEN ||
                                                              ELSE | : | ) }{ lr_tier->hec_tier_descr }{
                                                      COND #( WHEN lr_tier->hec_tier_sid IS INITIAL
                                                              THEN ||
                                                              ELSE | ( { lr_tier->hec_tier_sid } ) | ) }|.

                  lr_tier->hec_tree_descr = lv_tier_description.
                  lv_data_changed         = abap_true.

                  "-----------------------------------
                  " Set Value List Quantity
                  "-----------------------------------
                  " Tier Type
                  lr_tier->hec_tier_type_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_tier_type(
                                                                          iv_apm_guid       = lr_landscape->hec_apm_guid
                                                                          iv_flat_mat_guid  = lr_landscape->hec_flat_mat_guid
                                                                          iv_tier_cat_value = lr_tier->hec_tier_cat_value ) )
                                                        THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                        ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                  " HEC_TIER_LANGUAGE_SYS_DEF
                  /hec1/cl_config_utilities=>get_language_value_list( EXPORTING iv_exclude_spras  = lr_tier->hec_tier_language_sys_alt
                                                                                it_language_table = CONV #( /hec1/cl_prov_utility=>conv_csv_to_table( iv_csv = CONV #( lr_tier->hec_tier_language_list ) ) )
                                                                      CHANGING  cs_field_usage    = ls_field_usage ).

                  lr_tier->hec_tier_language_sys_def_vlqt = COND #( WHEN 1 < lines( ls_field_usage-fixed_values )
                                                                    THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                    ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                  CLEAR ls_field_usage.

                  " HEC_TIER_LANGUAGE_SYS_ALT
                  /hec1/cl_config_utilities=>get_language_value_list_lim( EXPORTING iv_exclude_spras  = lr_tier->hec_tier_language_sys_def
                                                                                    it_language_table = CONV #( /hec1/cl_prov_utility=>conv_csv_to_table( iv_csv = CONV #( lr_tier->hec_tier_language_list ) ) )
                                                                          CHANGING  cs_field_usage    = ls_field_usage ).

                  lr_tier->hec_tier_language_sys_alt_vlqt = COND #( WHEN 1 < lines( ls_field_usage-fixed_values )
                                                                    THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                    ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                  CLEAR ls_field_usage.

                ENDIF." IF lr_tier->hec_tier_type_guid <> <fs_tier_before>-hec_tier_type_guid OR...

                "-----------------------------------
                " App server instance number changed
                " added or removed
                "-----------------------------------
                IF lr_tier->hec_app_srv_qty_opt <> <fs_tier_before>-hec_app_srv_qty_opt.

                  DATA(lt_app_server_lines) = VALUE /hec1/t_data_app_serv_inst_ct( FOR app_serv_inst IN lt_app_serv_inst
                                                                                   WHERE ( parent_key = lr_tier->key )
                                                                                   ( app_serv_inst ) ).

                  DATA(lt_app_server_lines_optional) = VALUE /hec1/t_data_app_serv_inst_ct( FOR app_serv_inst IN lt_app_serv_inst
                                                                                            WHERE ( parent_key = lr_tier->key AND
                                                                                                    hec_srv_inst_rel_value = /hec1/if_config_constants=>gc_relevance-optional )
                                                                                            ( app_serv_inst ) ).

                  IF lr_tier->hec_app_srv_qty_opt > <fs_tier_before>-hec_app_srv_qty_opt.
                    INSERT VALUE #( key     = lr_tier->key
                                    hec_db_srv_qty   = 0
                                    hec_app_srv_qty  = lr_tier->hec_app_srv_qty_opt - <fs_tier_before>-hec_app_srv_qty_opt ) INTO TABLE lt_act_param.

                    " Success message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_server_added
                                                                   iv_severity = /bobf/cm_frw=>co_severity_success
                                                                   iv_attr1    = CONV #( lr_tier->hec_app_srv_qty_opt - <fs_tier_before>-hec_app_srv_qty_opt )
                                                         CHANGING  co_message  = eo_message ).


                  ELSEIF lr_tier->hec_app_srv_qty_opt < <fs_tier_before>-hec_app_srv_qty_opt
                     AND lr_tier->hec_app_srv_qty_opt < lines( lt_app_server_lines_optional ).
                    DATA(lv_attr_name) = /hec1/if_configuration_c=>sc_node_attribute-tier-hec_app_srv_qty_opt.
                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_tier->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_tier->hec_app_srv_qty_opt = <fs_tier_before>-hec_app_srv_qty_opt.
                    lv_data_changed = abap_true.

                  ELSEIF <fs_tier_before>-hec_app_srv_qty_opt > lines( lt_app_server_lines_optional ).
                    lv_data_changed = abap_true.
                  ENDIF. " IF lr_tier->hec_app_srv_qty > <fs_tier_before>-hec_app_srv_qty.
                ENDIF. " IF lr_tier->hec_app_srv_qty_opt <> <fs_tier_before>-hec_app_srv_qty_opt.


                "-----------------------------------
                " DB server instance number changed
                " added or removed
                "-----------------------------------
                IF lr_tier->hec_db_srv_qty_opt <> <fs_tier_before>-hec_db_srv_qty_opt.

                  DATA(lt_db_server_lines) = VALUE /hec1/t_data_db_server_inst_ct( FOR db_serv_inst IN lt_db_serv_inst
                                                                                   WHERE ( parent_key = lr_tier->key )
                                                                                   ( db_serv_inst )                    ).

                  DATA(lt_db_server_lines_optional) = VALUE /hec1/t_data_db_server_inst_ct( FOR db_serv_inst IN lt_db_serv_inst
                                                                                            WHERE ( parent_key = lr_tier->key AND
                                                                                                    hec_srv_inst_rel_value = /hec1/if_config_constants=>gc_relevance-optional )
                                                                                            ( db_serv_inst )                                                                    ).

                  IF lr_tier->hec_db_srv_qty_opt > <fs_tier_before>-hec_db_srv_qty_opt.

                    ASSIGN lt_act_param[ key = lr_tier->key ] TO FIELD-SYMBOL(<fs_act_param>).
                    IF <fs_act_param> IS ASSIGNED.
                      <fs_act_param>-hec_db_srv_qty = lr_tier->hec_db_srv_qty_opt - <fs_tier_before>-hec_db_srv_qty_opt.
                    ELSE.
                      INSERT VALUE #( key             = lr_tier->key
                                      hec_db_srv_qty  = lr_tier->hec_db_srv_qty_opt - <fs_tier_before>-hec_db_srv_qty_opt
                                      hec_app_srv_qty = 0                                                                 ) INTO TABLE lt_act_param.

                    ENDIF.
                    " Success message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_server_added
                                                                   iv_severity = /bobf/cm_frw=>co_severity_success
                                                                   iv_attr1    = CONV #( lr_tier->hec_db_srv_qty_opt - <fs_tier_before>-hec_db_srv_qty_opt )
                                                         CHANGING  co_message  = eo_message ).


                  ELSEIF lr_tier->hec_db_srv_qty_opt < <fs_tier_before>-hec_db_srv_qty_opt
                     AND lr_tier->hec_db_srv_qty_opt < lines( lt_db_server_lines_optional ).
                    lv_attr_name = /hec1/if_configuration_c=>sc_node_attribute-tier-hec_db_srv_qty_opt.
                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_tier->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_tier->hec_db_srv_qty_opt = <fs_tier_before>-hec_db_srv_qty_opt.
                    lv_data_changed = abap_true.

                  ELSEIF <fs_tier_before>-hec_db_srv_qty_opt > lines( lt_db_server_lines_optional ).
                    lv_data_changed = abap_true.
                  ENDIF. " IF lr_tier->hec_db_srv_qty > <fs_tier_before>-hec_db_srv_qty.
                ENDIF. " IF lr_tier->hec_db_srv_qty_opt <> <fs_tier_before>-hec_db_srv_qty_opt.

                "-----------------------------------
                " Implementation Type changed
                "   if implementation type is "Greenfield"
                "   the migration scenario needs to be set to
                "   "No migration"
                "-----------------------------------
                IF lr_tier->hec_tier_impl_type_value = /hec1/if_config_constants=>gc_tier_impl_type-greenfield
                  AND <fs_tier_before>-hec_tier_impl_type_value IS INITIAL.
                  lr_tier->hec_tier_migr_scen_value = 'GR_NoMig'.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_tier->hec_phase_guid NE <fs_tier_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_tier->key
                                  hec_phase_guid_new = lr_tier->hec_phase_guid
                                  hec_phase_guid_old = <fs_tier_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_tier->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "phasing changed
              ENDIF. "<fs_tier_before> is assigned

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_tier->hec_tier_descr           IS NOT INITIAL AND
                                                                       lr_tier->hec_tier_type_value      IS NOT INITIAL AND
                                                                       lr_tier->hec_tier_impl_type_value IS NOT INITIAL AND
                                                                       lr_tier->hec_phase_guid           IS NOT INITIAL AND
                                                                       lr_tier->hec_tier_datacenter_guid IS NOT INITIAL AND
                                                                       lv_datacenter_descr               IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_tier->hec_instance_status.
                lr_tier->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "Set default reference if only one other tier exists
              IF lr_tier->hec_tier_is_reference = abap_true.
                DATA(lt_tier_list) = /hec1/cl_config_sw_helper=>get_instance( )->/hec1/if_config_sw_helper~get_tier_list( iv_solution_guid  = lr_tier->hec_node_solution
                                                                                                                          iv_hec_node_tier  = lr_tier->hec_node_tier
                                                                                                                          iv_hec_phase_guid = lr_tier->hec_phase_guid    ).
                IF lines( lt_tier_list ) = 1.
                  lr_tier->hec_tier_reference = lt_tier_list[ 1 ]-hec_node_tier.
                  lv_data_changed = abap_true.
                ENDIF.

              ELSE.
                "clear value in case checkbox was unchecked
                IF lr_tier->hec_tier_reference IS NOT INITIAL.
                  CLEAR lr_tier->hec_tier_reference.
                  lv_data_changed = abap_true.
                ENDIF.
              ENDIF.

              "-----------------------------------
              " Modify tier
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_tier->key
                                   is_data = lr_tier ).
              ENDIF.

              CLEAR: lv_data_changed,
                     lv_inst_status,
                     lv_tier_description,
                     lv_datacenter_descr,
                     lv_attr_name,
                     lt_app_server_lines,
                     lt_app_server_lines_optional,
                     lt_db_server_lines,
                     lt_db_server_lines_optional.

              UNASSIGN: <fs_act_param>,
                        <fs_tier_before>.
            ENDLOOP. " LOOP AT lt_tier REFERENCE INTO lr_tier.

            "-----------------------------------
            " Set create DB/App server instance
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_serv_inst( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_serv_inst )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                  ).

            ENDIF.

            "-----------------------------------
            " Set Update Phasing
            " action to general
            "-----------------------------------
            IF lt_act_param_phasing IS NOT INITIAL.
              CLEAR me->mr_act_param_phasing.
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


  METHOD determine_tier_add_service.

    DATA: lt_tier_add_service        TYPE /hec1/t_data_tier_add_serv_ct,
          lt_tier_add_service_before TYPE /hec1/t_data_tier_add_serv_ct,
          lt_tier                    TYPE /hec1/t_data_tier_ct,
          lt_root_key                TYPE /bobf/t_frw_key,
          lt_landscape_key           TYPE /bobf/t_frw_key,
          lt_add_serv                TYPE /hec1/t_data_add_services_ct,
          lt_phase                   TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing       TYPE TABLE OF /hec1/s_act_phase_inherit.



    CLEAR: eo_message,
           et_failed_key.

    " Get landscape and delivery unit data
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit) ).

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_tier_add_service ).


    " Get service class data from corresponding additional service
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = VALUE #( ( key = lv_root_key ) )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-add_service
                                      IMPORTING et_data        = lt_add_serv ).


    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier_add_service-create.

            " Get tier node (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier_add_service-to_parent
                                              IMPORTING et_data        = lt_tier ).

            LOOP AT lt_tier_add_service REFERENCE INTO DATA(lr_tier_add_service).
              ASSIGN lt_tier[ key = lr_tier_add_service->parent_key ] TO FIELD-SYMBOL(<fs_tier>).

              lr_tier_add_service->hec_delete_visible = abap_true.

              IF <fs_tier> IS ASSIGNED.
                IF <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                   <fs_tier>-hec_tier_type_value      IS NOT INITIAL AND
                   <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              IF lv_release <> lr_tier_add_service->hec_row_selectable.
                lr_tier_add_service->hec_row_selectable = lv_release.
                DATA(lv_data_changed) = abap_true.
              ENDIF.


              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_tier_add_service->key
                                   is_data = lr_tier_add_service ).
              ENDIF.

              UNASSIGN <fs_tier>.
              CLEAR: lv_data_changed,
                     lv_release.
            ENDLOOP.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier_add_service-update.

            " Data before update
            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_tier_add_service_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).


            LOOP AT lt_tier_add_service REFERENCE INTO lr_tier_add_service.
              ASSIGN lt_tier_add_service_before[ key = lr_tier_add_service->key ] TO FIELD-SYMBOL(<fs_add_serv_before>).

              IF <fs_add_serv_before> IS ASSIGNED.

                IF <fs_add_serv_before>-hec_tas_service_ref_guid IS NOT INITIAL AND
                   lr_tier_add_service->hec_tas_service_ref_guid IS     INITIAL.
                  IF <fs_add_serv_before>-hec_tas_service_ref_descr = lr_tier_add_service->hec_tas_service_ref_descr_ext.
                    CLEAR lr_tier_add_service->hec_tas_service_ref_descr_ext.
                  ENDIF.
                  lr_tier_add_service->hec_tree_descr = COND #( WHEN lr_tier_add_service->hec_tas_service_ref_descr_ext IS INITIAL
                                                           THEN ''
                                                           ELSE | : { lr_tier_add_service->hec_tas_service_ref_descr_ext }|   ) .
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Service Class GUID has changed
                "-----------------------------------
                IF lr_tier_add_service->hec_tas_service_ref_guid IS NOT INITIAL                                             AND
                 ( lr_tier_add_service->hec_tas_service_ref_guid      <> <fs_add_serv_before>-hec_tas_service_ref_guid      OR
                   lr_tier_add_service->hec_tas_service_ref_descr_ext <> <fs_add_serv_before>-hec_tas_service_ref_descr_ext    ).

                  ASSIGN lt_add_serv[ hec_node_service = lr_tier_add_service->hec_tas_service_ref_guid ] TO FIELD-SYMBOL(<fs_service>).
                  IF <fs_service> IS ASSIGNED.
                    IF lr_tier_add_service->hec_tas_service_ref_descr_ext IS INITIAL.
                      lr_tier_add_service->hec_tas_service_ref_descr_ext = <fs_service>-hec_as_class_descr_ext.
                    ENDIF.
                    lr_tier_add_service->* = VALUE #( BASE lr_tier_add_service->*
                                                 hec_tas_service_ref_descr = <fs_service>-hec_ip_as_class_descr
                                                 hec_tas_tier_uplift_perc  = <fs_service>-hec_as_tier_uplift_perc
                                                 hec_tree_descr            = COND #( WHEN lr_tier_add_service->hec_tas_service_ref_descr_ext IS INITIAL
                                                                                     THEN <fs_service>-hec_ip_as_class_descr
                                                                                     ELSE |{ <fs_service>-hec_ip_as_class_descr } : { lr_tier_add_service->hec_tas_service_ref_descr_ext }| ) ).

                    lv_data_changed = abap_true.
                  ENDIF.
                ENDIF. " IF lr_service->hec_tas_service_ref_guid IS NOT INITIAL.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_tier_add_service->hec_phase_guid NE <fs_add_serv_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_tier_add_service->key
                                  hec_phase_guid_new = lr_tier_add_service->hec_phase_guid
                                  hec_phase_guid_old = <fs_add_serv_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_tier_add_service->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "phasing changed
              ENDIF. " IF <fs_add_serv_before> IS ASSIGNED.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_tier_add_service->hec_tas_service_ref_guid IS NOT INITIAL AND
                                                                             lr_tier_add_service->hec_phase_guid           IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_tier_add_service->hec_instance_status.
                lr_tier_add_service->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_tier_add_service->key
                                   is_data = lr_tier_add_service ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN: <fs_add_serv_before>.
*                        <fs_service>.
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

            " **********************************
            " Update mode after tier update
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier_add_service-update_after_tier.

            " Get tier
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier_add_service-to_parent
                                              IMPORTING et_data        = lt_tier ).


            LOOP AT lt_tier_add_service REFERENCE INTO lr_tier_add_service.

              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_tier_add_service->hec_tas_service_ref_guid IS NOT INITIAL AND
                                                                       lr_tier_add_service->hec_phase_guid           IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              " Check instance status and switch
              IF lv_inst_status <> lr_tier_add_service->hec_instance_status.
                lr_tier_add_service->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.


              ASSIGN lt_tier[ key = lr_tier_add_service->parent_key ] TO <fs_tier>.

              IF <fs_tier> IS ASSIGNED.
                IF <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                   <fs_tier>-hec_tier_type_value      IS NOT INITIAL AND
                   <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              " Release instance for selection
              IF lv_release <> lr_tier_add_service->hec_row_selectable.
                lr_tier_add_service->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_tier_add_service->key
                                   is_data = lr_tier_add_service ).
              ENDIF.

              UNASSIGN <fs_tier>.
              CLEAR: lv_release,
                     lv_data_changed.
            ENDLOOP.
        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD determine_tier_add_storage.

*    DATA: lt_tier_add_storage        TYPE /hec1/t_tier_add_storage_ct,
*          lt_tier_add_storage_before TYPE /hec1/t_tier_add_storage_ct,
*          lt_tier                    TYPE /hec1/t_data_tier_ct,
*          lt_root_key                TYPE /bobf/t_frw_key,
*          lt_landscape_key           TYPE /bobf/t_frw_key,
*          lt_add_storage             TYPE /hec1/t_data_add_storage_ct,
*          lt_phase                   TYPE /hec1/t_data_phase_ct,
*          lt_act_param_phasing       TYPE TABLE OF /hec1/s_act_phase_inherit.
*
*
*
*    CLEAR: eo_message,
*           et_failed_key.
*
*    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
*                                 it_key  = it_key
*                       IMPORTING et_data = lt_tier_add_storage ).
*
*    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
*                                                        it_key           = it_key
*                                                        io_read          = io_read
*                                              IMPORTING ev_root_key      = DATA(lv_root_key)
*                                                        er_landscape     = DATA(lr_landscape)
*                                                        er_delivery_unit = DATA(lr_delivery_unit) ).
*
*    TRY.
*        CASE is_ctx-det_key.
*            " ***************************************************************************
*            " Create mode
*            " ***************************************************************************
*          WHEN /hec1/if_configuration_c=>sc_determination-tier_add_storage-create.
*
*            " Get tier node (parent)
*            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
*                                                        it_key         = it_key
*                                                        iv_fill_data   = abap_true
*                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier_add_storage-to_parent
*                                              IMPORTING et_data        = lt_tier                                                        ).
*
*            LOOP AT lt_tier_add_storage REFERENCE INTO DATA(lr_tier_add_storage).
*              ASSIGN lt_tier[ key = lr_tier_add_storage->parent_key ] TO FIELD-SYMBOL(<fs_tier>).
*
*              lr_tier_add_storage->hec_delete_visible = abap_true.
*
*              IF ( <fs_tier>                          IS ASSIGNED )    AND
*                 ( <fs_tier>-hec_tier_descr           IS NOT INITIAL ) AND
*                 ( <fs_tier>-hec_tier_type_value      IS NOT INITIAL ) AND
*                 ( <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL ).
*                DATA(lv_release) = abap_true.
*              ENDIF.
*
*              "-----------------------------------
*              " Release instance for selection
*              "-----------------------------------
*              IF ( lv_release <> lr_tier_add_storage->hec_row_selectable ).
*                lr_tier_add_storage->hec_row_selectable = lv_release.
*                DATA(lv_data_changed) = abap_true.
*              ENDIF.
*
*
*              IF ( lv_data_changed = abap_true ).
*                io_modify->update( iv_node = is_ctx-node_key
*                                   iv_key  = lr_tier_add_storage->key
*                                   is_data = lr_tier_add_storage      ).
*              ENDIF.
*
*              UNASSIGN <fs_tier>.
*              CLEAR: lv_data_changed,
*                     lv_release.
*            ENDLOOP.
*
*            " ***************************************************************************
*            " Update mode
*            " ***************************************************************************
*          WHEN /hec1/if_configuration_c=>sc_determination-tier_add_storage-update.
*
*            " Data before update
*            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
*                                         it_key          = it_key
*                                         iv_before_image = abap_true
*                               IMPORTING et_data         = lt_tier_add_storage_before ).
*            " ROOT -> PHASE
*            io_read->retrieve_by_association( EXPORTING iv_node         = /hec1/if_configuration_c=>sc_node-root
*                                                        it_key          = VALUE #( ( key = lv_root_key ) )
*                                                        iv_fill_data    = abap_true
*                                                        iv_association  = /hec1/if_configuration_c=>sc_association-root-phase
*                                              IMPORTING et_data         = lt_phase ).
*
*
*            LOOP AT lt_tier_add_storage REFERENCE INTO lr_tier_add_storage.
*
*              ASSIGN lt_tier_add_storage_before[ key = lr_tier_add_storage->key ] TO FIELD-SYMBOL(<fs_add_storage_before>).
*              IF ( <fs_add_storage_before> IS ASSIGNED ).
*
*                "-----------------------------------
*                " Tier Add Storage Class GUID has changed ?
*                "-----------------------------------
*                IF ( lr_tier_add_storage->hec_tadd_storage_ref_guid IS NOT INITIAL ) AND
*                 ( ( lr_tier_add_storage->hec_tadd_storage_ref_guid <> <fs_add_storage_before>-hec_tadd_storage_ref_guid ) OR
*                   ( lr_tier_add_storage->hec_tadd_storage_ref_descr_ext <> <fs_add_storage_before>-hec_tadd_storage_ref_descr_ext ) ).
*
*                  " Get performance class data from corresponding additional storage
*                  IF ( lt_root_key IS INITIAL ).
*                    " Get root key
*                    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
*                                                                it_key         = it_key
*                                                                iv_fill_data   = abap_false
*                                                                iv_association = /hec1/if_configuration_c=>sc_association-tier_add_storage-to_root
*                                                      IMPORTING et_target_key  = lt_root_key                                                  ).
*
*                    " Get additional storage
*                    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
*                                                                it_key         = lt_root_key
*                                                                iv_fill_data   = abap_true
*                                                                iv_association = /hec1/if_configuration_c=>sc_association-root-add_storage
*                                                      IMPORTING et_data        = lt_add_storage                                                ).
*
*                  ENDIF.
*
*                  ASSIGN lt_add_storage[ hec_node_add_storage_guid = lr_tier_add_storage->hec_tadd_storage_ref_guid ] TO FIELD-SYMBOL(<fs_add_storage>).
*                  IF ( <fs_add_storage> IS ASSIGNED ).
*                    lr_tier_add_storage->* = VALUE #( BASE lr_tier_add_storage->*
*                                                      hec_tadd_storage_ref_descr     = <fs_add_storage>-hec_astore_class_descr
*                                                      hec_tadd_storage_ref_descr_ext = <fs_add_storage>-hec_astore_class_descr_ext
*                                                      hec_tree_descr                 = COND #( WHEN <fs_add_storage>-hec_astore_class_descr_ext IS INITIAL
*                                                                                               THEN <fs_add_storage>-hec_astore_class_descr
*                                                                                               ELSE |{ <fs_add_storage>-hec_astore_class_descr } : { <fs_add_storage>-hec_astore_class_descr_ext }| ) ).
*
*                    lv_data_changed = abap_true.
*                  ENDIF.
*                ENDIF.
*
*                "-----------------------------------
*                " Phasing has changed
*                "-----------------------------------
*                IF ( lr_tier_add_storage->hec_phase_guid NE <fs_add_storage_before>-hec_phase_guid ).
*
*                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
*                                  hec_bopf_key       = lr_tier_add_storage->key
*                                  hec_phase_guid_new = lr_tier_add_storage->hec_phase_guid
*                                  hec_phase_guid_old = <fs_add_storage_before>-hec_phase_guid ) TO lt_act_param_phasing.
*
*                  lr_tier_add_storage->hec_phase_changed = abap_true.
*                  lv_data_changed = abap_true.
*
*                ENDIF. "phasing changed
*              ENDIF. " IF <fs_add_storage_before> IS ASSIGNED.
*
*              "-----------------------------------
*              " Release instance for selection
*              "-----------------------------------
*              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_tier_add_storage->hec_tadd_storage_ref_guid IS NOT INITIAL AND
*                                                                             lr_tier_add_storage->hec_phase_guid            IS NOT INITIAL
*                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
*                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).
*
*              IF ( lv_inst_status <> lr_tier_add_storage->hec_instance_status ).
*                lr_tier_add_storage->hec_instance_status = lv_inst_status.
*                lv_data_changed = abap_true.
*              ENDIF.
*
*              IF ( lv_data_changed = abap_true ).
*                io_modify->update( iv_node = is_ctx-node_key
*                                   iv_key  = lr_tier_add_storage->key
*                                   is_data = lr_tier_add_storage      ).
*              ENDIF.
*
*              CLEAR: lv_inst_status,
*                     lv_data_changed.
*
*              UNASSIGN: <fs_add_storage_before>,
*                        <fs_add_storage>.
*            ENDLOOP.
*
*            "-----------------------------------
*            " Update Phasing
*            "-----------------------------------
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
*            " **********************************
*            " Update mode after tier update
*            " **********************************
*          WHEN /hec1/if_configuration_c=>sc_determination-tier_longterm_backup-update_after_tier.
*
*            " Get tier
*            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
*                                                        it_key         = it_key
*                                                        iv_fill_data   = abap_true
*                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier_longterm_backup-to_parent
*                                              IMPORTING et_data        = lt_tier                                                        ).
*
*
*            LOOP AT lt_tier_add_storage REFERENCE INTO lr_tier_add_storage.
*
*              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_tier_add_storage->hec_tadd_storage_ref_guid IS NOT INITIAL AND
*                                                                       lr_tier_add_storage->hec_phase_guid            IS NOT INITIAL
*                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
*                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).
*
*              " Check instance status and switch
*              IF ( lv_inst_status <> lr_tier_add_storage->hec_instance_status ).
*                lr_tier_add_storage->hec_instance_status = lv_inst_status.
*                lv_data_changed = abap_true.
*              ENDIF.
*
*
*              ASSIGN lt_tier[ key = lr_tier_add_storage->parent_key ] TO <fs_tier>.
*
*              IF ( <fs_tier> IS ASSIGNED ).
*                IF <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
*                   <fs_tier>-hec_tier_type_value      IS NOT INITIAL AND
*                   <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL.
*                  lv_release = abap_true.
*                ENDIF.
*              ENDIF.
*
*              " Release instance for selection
*              IF ( lv_release <> lr_tier_add_storage->hec_row_selectable ).
*                lr_tier_add_storage->hec_row_selectable = lv_release.
*                lv_data_changed = abap_true.
*              ENDIF.
*
*              IF ( lv_data_changed = abap_true ).
*                io_modify->update( iv_node = is_ctx-node_key
*                                   iv_key  = lr_tier_add_storage->key
*                                   is_data = lr_tier_add_storage      ).
*              ENDIF.
*
*              UNASSIGN <fs_tier>.
*              CLEAR: lv_release,
*                     lv_data_changed.
*            ENDLOOP.
*        ENDCASE.
*
*
*      CATCH /bobf/cx_frw. " Exception class
*    ENDTRY.


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
            " Determination root node
            " Root Node = Landscape Node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-root-create
            OR /hec1/if_configuration_c=>sc_determination-root-update.

*            CASE ls_root-hec_contract_status.
*                " Initial Deal
*              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
            me->determine_root( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                          it_key        = it_key                           " Key Table
                                          io_read       = io_read                          " Interface to Reading Data
                                          io_modify     = io_modify                        " Interface to Change Data
                                IMPORTING eo_message    = eo_message                       " Message Object
                                          et_failed_key = et_failed_key ).

*                " Change Request
*              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
*                me->determine_root_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
*                                                 it_key        = it_key                           " Key Table
*                                                 io_read       = io_read                          " Interface to Reading Data
*                                                 io_modify     = io_modify                        " Interface to Change Data
*                                       IMPORTING eo_message    = eo_message                       " Message Object
*                                                 et_failed_key = et_failed_key  ).
*
*            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determination Managed Service Baseline
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-managed_service_baseline-create OR
               /hec1/if_configuration_c=>sc_determination-managed_service_baseline-update.

            CASE ls_root-hec_contract_status.
                " Initial Deal
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                me->determine_man_serv_baseline( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                           it_key        = it_key                           " Key Table
                                                           io_read       = io_read                          " Interface to Reading Data
                                                           io_modify     = io_modify                        " Interface to Change Data
                                                 IMPORTING eo_message    = eo_message                       " Message Object
                                                           et_failed_key = et_failed_key ).

                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->determine_man_serv_baseline_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                              it_key        = it_key                           " Key Table
                                                              io_read       = io_read                          " Interface to Reading Data
                                                              io_modify     = io_modify                        " Interface to Change Data
                                                    IMPORTING eo_message    = eo_message                       " Message Object
                                                              et_failed_key = et_failed_key ).

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determination delivery unit node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-delivery_unit-create  OR
               /hec1/if_configuration_c=>sc_determination-delivery_unit-update.

            CASE ls_root-hec_contract_status.
                " Initial Deal
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                me->determine_delivery_unit( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                       it_key        = it_key                           " Key Table
                                                       io_read       = io_read                          " Interface to Reading Data
                                                       io_modify     = io_modify                        " Interface to Change Data
                                             IMPORTING eo_message    = eo_message                       " Message Object
                                                       et_failed_key = et_failed_key ).

                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->determine_delivery_unit_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                          it_key        = it_key                           " Key Table
                                                          io_read       = io_read                          " Interface to Reading Data
                                                          io_modify     = io_modify                        " Interface to Change Data
                                                IMPORTING eo_message    = eo_message                       " Message Object
                                                          et_failed_key = et_failed_key ).

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determination data center node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-datacenter-create            OR
               /hec1/if_configuration_c=>sc_determination-datacenter-update            OR
               /hec1/if_configuration_c=>sc_determination-datacenter-get_country_descr.

            CASE ls_root-hec_contract_status.
                " Initial Deal
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                me->determine_datacenter( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                    it_key        = it_key                           " Key Table
                                                    io_read       = io_read                          " Interface to Reading Data
                                                    io_modify     = io_modify                        " Interface to Change Data
                                          IMPORTING eo_message    = eo_message                       " Message Object
                                                    et_failed_key = et_failed_key ).

                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->determine_datacenter_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                       it_key        = it_key                           " Key Table
                                                       io_read       = io_read                          " Interface to Reading Data
                                                       io_modify     = io_modify                        " Interface to Change Data
                                             IMPORTING eo_message    = eo_message                       " Message Object
                                                       et_failed_key = et_failed_key ).

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determination infrastructure baseline node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-infrastructure_baseline-create            OR
               /hec1/if_configuration_c=>sc_determination-infrastructure_baseline-update.

            CASE ls_root-hec_contract_status.
                " Initial Deal
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                me->determine_infr_baseline( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                       it_key        = it_key                           " Key Table
                                                       io_read       = io_read                          " Interface to Reading Data
                                                       io_modify     = io_modify                        " Interface to Change Data
                                             IMPORTING eo_message    = eo_message                       " Message Object
                                                       et_failed_key = et_failed_key ).

                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->determine_infr_baseline_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                          it_key        = it_key                           " Key Table
                                                          io_read       = io_read                          " Interface to Reading Data
                                                          io_modify     = io_modify                        " Interface to Change Data
                                                IMPORTING eo_message    = eo_message                       " Message Object
                                                          et_failed_key = et_failed_key ).

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determination network segment
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-network_segment-create            OR
               /hec1/if_configuration_c=>sc_determination-network_segment-update.

            CASE ls_root-hec_contract_status.
                " Initial Deal
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                me->determine_network_segment( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                         it_key        = it_key                           " Key Table
                                                         io_read       = io_read                          " Interface to Reading Data
                                                         io_modify     = io_modify                        " Interface to Change Data
                                               IMPORTING eo_message    = eo_message                       " Message Object
                                                         et_failed_key = et_failed_key ).

                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->determine_network_segment_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                            it_key        = it_key                           " Key Table
                                                            io_read       = io_read                          " Interface to Reading Data
                                                            io_modify     = io_modify                        " Interface to Change Data
                                                  IMPORTING eo_message    = eo_message                       " Message Object
                                                            et_failed_key = et_failed_key ).

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determination connectivity node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-connectivity-create                  OR
               /hec1/if_configuration_c=>sc_determination-connectivity-update                  OR
               /hec1/if_configuration_c=>sc_determination-connectivity-update_after_datacenter.

            CASE ls_root-hec_contract_status.
                " Initial Deal
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                me->determine_connectivity( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                      it_key        = it_key                           " Key Table
                                                      io_read       = io_read                          " Interface to Reading Data
                                                      io_modify     = io_modify                        " Interface to Change Data
                                            IMPORTING eo_message    = eo_message                       " Message Object
                                                      et_failed_key = et_failed_key ).

                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->determine_connectivity_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                         it_key        = it_key                           " Key Table
                                                         io_read       = io_read                          " Interface to Reading Data
                                                         io_modify     = io_modify                        " Interface to Change Data
                                               IMPORTING eo_message    = eo_message                       " Message Object
                                                         et_failed_key = et_failed_key ).

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determination add. service node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-add_service-create OR
               /hec1/if_configuration_c=>sc_determination-add_service-update.

            CASE ls_root-hec_contract_status.
                " Initial Deal
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                me->determine_add_service( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                     it_key        = it_key                           " Key Table
                                                     io_read       = io_read                          " Interface to Reading Data
                                                     io_modify     = io_modify                        " Interface to Change Data
                                           IMPORTING eo_message    = eo_message                       " Message Object
                                                     et_failed_key = et_failed_key ).

                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->determine_add_service_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                        it_key        = it_key                           " Key Table
                                                        io_read       = io_read                          " Interface to Reading Data
                                                        io_modify     = io_modify                        " Interface to Change Data
                                              IMPORTING eo_message    = eo_message                       " Message Object
                                                        et_failed_key = et_failed_key ).

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determination solution node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-solution-create OR
               /hec1/if_configuration_c=>sc_determination-solution-update.

            CASE ls_root-hec_contract_status.
                " Initial Deal
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                me->determine_solution( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                  it_key        = it_key                           " Key Table
                                                  io_read       = io_read                          " Interface to Reading Data
                                                  io_modify     = io_modify                        " Interface to Change Data
                                        IMPORTING eo_message    = eo_message                       " Message Object
                                                  et_failed_key = et_failed_key ).

                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->determine_solution_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                     it_key        = it_key                           " Key Table
                                                     io_read       = io_read                          " Interface to Reading Data
                                                     io_modify     = io_modify                        " Interface to Change Data
                                           IMPORTING eo_message    = eo_message                       " Message Object
                                                     et_failed_key = et_failed_key ).

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determination transport path
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-transport_path-create OR
               /hec1/if_configuration_c=>sc_determination-transport_path-update.

            CASE ls_root-hec_contract_status.
                " Initial Deal
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                me->determine_transport_path( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                        it_key        = it_key                           " Key Table
                                                        io_read       = io_read                          " Interface to Reading Data
                                                        io_modify     = io_modify                        " Interface to Change Data
                                              IMPORTING eo_message    = eo_message                       " Message Object
                                                        et_failed_key = et_failed_key ).

                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->determine_transport_path_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                           it_key        = it_key                           " Key Table
                                                           io_read       = io_read                          " Interface to Reading Data
                                                           io_modify     = io_modify                        " Interface to Change Data
                                                 IMPORTING eo_message    = eo_message                       " Message Object
                                                           et_failed_key = et_failed_key ).

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determination tier node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier-create OR
               /hec1/if_configuration_c=>sc_determination-tier-update.

            CASE ls_root-hec_contract_status.
                " Initial Deal
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                me->determine_tier( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                              it_key        = it_key                           " Key Table
                                              io_read       = io_read                          " Interface to Reading Data
                                              io_modify     = io_modify                        " Interface to Change Data
                                    IMPORTING eo_message    = eo_message                       " Message Object
                                              et_failed_key = et_failed_key ).

                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->determine_tier_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                 it_key        = it_key                           " Key Table
                                                 io_read       = io_read                          " Interface to Reading Data
                                                 io_modify     = io_modify                        " Interface to Change Data
                                       IMPORTING eo_message    = eo_message                       " Message Object
                                                 et_failed_key = et_failed_key ).

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determination tier sla node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier_sla-create OR
               /hec1/if_configuration_c=>sc_determination-tier_sla-update.

            CASE ls_root-hec_contract_status.
                " Initial Deal
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                me->determine_tier_sla( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                  it_key        = it_key                           " Key Table
                                                  io_read       = io_read                          " Interface to Reading Data
                                                  io_modify     = io_modify                        " Interface to Change Data
                                        IMPORTING eo_message    = eo_message                       " Message Object
                                                  et_failed_key = et_failed_key ).

                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->determine_tier_sla_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                     it_key        = it_key                           " Key Table
                                                     io_read       = io_read                          " Interface to Reading Data
                                                     io_modify     = io_modify                        " Interface to Change Data
                                           IMPORTING eo_message    = eo_message                       " Message Object
                                                     et_failed_key = et_failed_key ).

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determination material node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-material-create            OR
               /hec1/if_configuration_c=>sc_determination-material-update            OR
               /hec1/if_configuration_c=>sc_determination-material-update_after_tier.

            CASE ls_root-hec_contract_status.
                " Initial Deal
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                me->determine_material( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                  it_key        = it_key                           " Key Table
                                                  io_read       = io_read                          " Interface to Reading Data
                                                  io_modify     = io_modify                        " Interface to Change Data
                                        IMPORTING eo_message    = eo_message                       " Message Object
                                                  et_failed_key = et_failed_key ).

                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->determine_material_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                     it_key        = it_key                           " Key Table
                                                     io_read       = io_read                          " Interface to Reading Data
                                                     io_modify     = io_modify                        " Interface to Change Data
                                           IMPORTING eo_message    = eo_message                       " Message Object
                                                     et_failed_key = et_failed_key ).

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determination software item node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-software_item-create                OR
               /hec1/if_configuration_c=>sc_determination-software_item-update                OR
               /hec1/if_configuration_c=>sc_determination-software_item-update_after_material.

            CASE ls_root-hec_contract_status.
                " Initial Deal
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                me->determine_sw_item( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                 it_key        = it_key                           " Key Table
                                                 io_read       = io_read                          " Interface to Reading Data
                                                 io_modify     = io_modify                        " Interface to Change Data
                                       IMPORTING eo_message    = eo_message                       " Message Object
                                                 et_failed_key = et_failed_key ).

                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->determine_sw_item_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                    it_key        = it_key                           " Key Table
                                                    io_read       = io_read                          " Interface to Reading Data
                                                    io_modify     = io_modify                        " Interface to Change Data
                                          IMPORTING eo_message    = eo_message                       " Message Object
                                                    et_failed_key = et_failed_key ).

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determination tier service node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier_add_service-create            OR
               /hec1/if_configuration_c=>sc_determination-tier_add_service-update            OR
               /hec1/if_configuration_c=>sc_determination-tier_add_service-update_after_tier.

            CASE ls_root-hec_contract_status.
                " Initial Deal
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                me->determine_tier_add_service( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                          it_key        = it_key                           " Key Table
                                                          io_read       = io_read                          " Interface to Reading Data
                                                          io_modify     = io_modify                        " Interface to Change Data
                                                IMPORTING eo_message    = eo_message                       " Message Object
                                                          et_failed_key = et_failed_key ).

                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->determine_tier_add_service_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                             it_key        = it_key                           " Key Table
                                                             io_read       = io_read                          " Interface to Reading Data
                                                             io_modify     = io_modify                        " Interface to Change Data
                                                   IMPORTING eo_message    = eo_message                       " Message Object
                                                             et_failed_key = et_failed_key ).

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determination tier additional (shared) storage
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier_add_storage-create            OR
               /hec1/if_configuration_c=>sc_determination-tier_add_storage-update            OR
               /hec1/if_configuration_c=>sc_determination-tier_add_storage-update_after_tier.

            CASE ls_root-hec_contract_status.
                " Initial Deal
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                me->determine_tier_add_storage( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                          it_key        = it_key                           " Key Table
                                                          io_read       = io_read                          " Interface to Reading Data
                                                          io_modify     = io_modify                        " Interface to Change Data
                                                IMPORTING eo_message    = eo_message                       " Message Object
                                                          et_failed_key = et_failed_key ).

                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->determine_tier_add_storage_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                             it_key        = it_key                           " Key Table
                                                             io_read       = io_read                          " Interface to Reading Data
                                                             io_modify     = io_modify                        " Interface to Change Data
                                                   IMPORTING eo_message    = eo_message                       " Message Object
                                                             et_failed_key = et_failed_key ).

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determine Contact
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-contact-create                       OR
               /hec1/if_configuration_c=>sc_determination-contact-update.

            CASE ls_root-hec_contract_status.
                " Initial Deal
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                me->determine_contact( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                 it_key        = it_key                           " Key Table
                                                 io_read       = io_read                          " Interface to Reading Data
                                                 io_modify     = io_modify                        " Interface to Change Data
                                       IMPORTING eo_message    = eo_message                       " Message Object
                                                 et_failed_key = et_failed_key ).

                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->determine_contact_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                    it_key        = it_key                           " Key Table
                                                    io_read       = io_read                          " Interface to Reading Data
                                                    io_modify     = io_modify                        " Interface to Change Data
                                          IMPORTING eo_message    = eo_message                       " Message Object
                                                    et_failed_key = et_failed_key ).

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determine Contact Reference
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-contact_reference-create                       OR
               /hec1/if_configuration_c=>sc_determination-contact_reference-update.

            CASE ls_root-hec_contract_status.
                " Initial Deal
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                me->determine_contact_reference( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                           it_key        = it_key                           " Key Table
                                                           io_read       = io_read                          " Interface to Reading Data
                                                           io_modify     = io_modify                        " Interface to Change Data
                                                 IMPORTING eo_message    = eo_message                       " Message Object
                                                           et_failed_key = et_failed_key ).

                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->determine_contact_reference_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                              it_key        = it_key                           " Key Table
                                                              io_read       = io_read                          " Interface to Reading Data
                                                              io_modify     = io_modify                        " Interface to Change Data
                                                    IMPORTING eo_message    = eo_message                       " Message Object
                                                              et_failed_key = et_failed_key ).

            ENDCASE. "ls_root-hec_contract_status.

            " **********************************
            " Determine Phase
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-phase-create                       OR
               /hec1/if_configuration_c=>sc_determination-phase-update.

            CASE ls_root-hec_contract_status.
                " Initial Deal
              WHEN /hec1/if_config_constants=>gc_contract_status-initial.
                me->determine_phase( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                               it_key        = it_key                           " Key Table
                                               io_read       = io_read                          " Interface to Reading Data
                                               io_modify     = io_modify                        " Interface to Change Data
                                     IMPORTING eo_message    = eo_message                       " Message Object
                                               et_failed_key = et_failed_key ).

                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->determine_phase_cr( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                  it_key        = it_key                           " Key Table
                                                  io_read       = io_read                          " Interface to Reading Data
                                                  io_modify     = io_modify                        " Interface to Change Data
                                        IMPORTING eo_message    = eo_message                       " Message Object
                                                  et_failed_key = et_failed_key ).

            ENDCASE. "ls_root-hec_contract_status.



            " **********************************
            " Determination root - CR mod type
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-root-modify_aggre_mod_type.
            CASE ls_root-hec_contract_status.
                " Change Request
              WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
                me->modify_aggre_mod_type( EXPORTING is_ctx        = is_ctx               " Context Information for Actions
                                                     it_key        = it_key               " Key Table
                                                     io_read       = io_read              " Interface to Read Data
                                                     io_modify     = io_modify            " Interface to Change Data
                                           IMPORTING eo_message    = eo_message           " Interface of Message Object
                                                     et_failed_key = et_failed_key ).
            ENDCASE.


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
    DATA lt_tree_data_update TYPE /hec1/t_bopf_config_data2tree.
    DATA lt_tree_data_insert TYPE /hec1/t_bopf_config_data2tree.
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
        " Determination root node
        " Root Node = Landscape Node
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_determination-root-create.

        lt_tree_data_insert = VALUE #( FOR wa_s IN CORRESPONDING /hec1/t_config_root_ct( <lt_data> )
                                                                                (
                                                                                  node_key = wa_s-key
                                                                                  hec_instance_status = wa_s-hec_instance_status
                                                                                  hec_tree_descr      = wa_s-hec_tree_descr
                                                                                  hec_row_selectable  = abap_true
                                                                                  hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-landscape
                                                                                  hec_delete_visible  = wa_s-hec_delete_visible
                                                                                  crea_date_time      = wa_s-crea_date_time
                                                                                 ) ).


      WHEN /hec1/if_configuration_c=>sc_determination-root-update.
        lt_tree_data_update = VALUE #( FOR wa_s IN CORRESPONDING /hec1/t_config_root_ct( <lt_data> )
                                                                                (
                                                                                  node_key            = wa_s-key
                                                                                  hec_instance_status = wa_s-hec_instance_status
                                                                                  hec_tree_descr      = wa_s-hec_tree_descr
                                                                                  hec_row_selectable  = abap_true
                                                                                  hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-landscape
                                                                                  hec_delete_visible  = wa_s-hec_delete_visible
                                                                                 ) ).

        " **********************************
        " Determination Managed Service Baseline
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_determination-managed_service_baseline-create
        OR /hec1/if_configuration_c=>sc_determination-managed_service_baseline-update.
        RETURN.

        " **********************************
        " Determination delivery unit node
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_determination-delivery_unit-create.
        lt_tree_data_insert = VALUE #( FOR wa_dlvy_unit IN CORRESPONDING /hec1/t_data_dlvy_unit_ct( <lt_data> )
                                                                                (
                                                                                  parent_node_key     = wa_dlvy_unit-parent_key
                                                                                  node_key            = wa_dlvy_unit-key
                                                                                  hec_instance_status = wa_dlvy_unit-hec_instance_status
                                                                                  hec_tree_descr      = wa_dlvy_unit-hec_tree_descr
                                                                                  hec_row_selectable  = abap_true
                                                                                  hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-delivery_unit
                                                                                  hec_delete_visible  = wa_dlvy_unit-hec_delete_visible
                                                                                  crea_date_time      = wa_dlvy_unit-crea_date_time
                                                                                  change_request      = wa_dlvy_unit-change_request
                                                                                 ) ).
      WHEN /hec1/if_configuration_c=>sc_determination-delivery_unit-update.
        lt_tree_data_update = VALUE #( FOR wa_dlvy_unit IN CORRESPONDING /hec1/t_data_dlvy_unit_ct( <lt_data> )
                                                                                (
                                                                                  parent_node_key     = wa_dlvy_unit-parent_key
                                                                                  node_key            = wa_dlvy_unit-key
                                                                                  hec_instance_status = wa_dlvy_unit-hec_instance_status
                                                                                  hec_tree_descr      = wa_dlvy_unit-hec_tree_descr
                                                                                  hec_row_selectable  = abap_true
                                                                                  hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-delivery_unit
                                                                                  hec_delete_visible  = wa_dlvy_unit-hec_delete_visible
                                                                                  change_request      = wa_dlvy_unit-change_request
                                                                                 ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-datacenter-create.
        lt_tree_data_insert = VALUE #( FOR wa_datacenter IN CORRESPONDING /hec1/t_data_datacenter_ct( <lt_data> )
                                                                                (
                                                                                  parent_node_key     = wa_datacenter-parent_key
                                                                                  node_key            = wa_datacenter-key
                                                                                  hec_instance_status = wa_datacenter-hec_instance_status
                                                                                  hec_tree_descr      = wa_datacenter-hec_tree_descr
                                                                                  hec_row_selectable  = abap_true
                                                                                  hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-datacenter
                                                                                  hec_phase_guid      = wa_datacenter-hec_phase_guid
                                                                                  hec_delete_visible  = wa_datacenter-hec_delete_visible
                                                                                  crea_date_time      = wa_datacenter-crea_date_time
                                                                                  change_request      = wa_datacenter-change_request
                                                                                 ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-datacenter-update
        OR /hec1/if_configuration_c=>sc_determination-datacenter-get_country_descr.

        lt_tree_data_update = VALUE #( FOR wa_datacenter IN CORRESPONDING /hec1/t_data_datacenter_ct( <lt_data> )
                                                                                (
                                                                                  parent_node_key     = wa_datacenter-parent_key
                                                                                  node_key            = wa_datacenter-key
                                                                                  hec_instance_status = wa_datacenter-hec_instance_status
                                                                                  hec_tree_descr      = wa_datacenter-hec_tree_descr
                                                                                  hec_row_selectable  = abap_true
                                                                                  hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-datacenter
                                                                                  hec_phase_guid      = wa_datacenter-hec_phase_guid
                                                                                  hec_delete_visible  = wa_datacenter-hec_delete_visible
                                                                                  crea_date_time      = wa_datacenter-crea_date_time
                                                                                  change_request      = wa_datacenter-change_request
                                                                                 ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-infrastructure_baseline-create
        OR /hec1/if_configuration_c=>sc_determination-infrastructure_baseline-update.
        RETURN.

      WHEN /hec1/if_configuration_c=>sc_determination-network_segment-create
        OR /hec1/if_configuration_c=>sc_determination-network_segment-update.
        RETURN.

      WHEN /hec1/if_configuration_c=>sc_determination-connectivity-create.
        lt_tree_data_insert = VALUE #( FOR wa_connectivity IN CORRESPONDING /hec1/t_data_connectivity_ct( <lt_data> )
                                                                          (
                                                                            parent_node_key     = wa_connectivity-parent_key
                                                                            node_key            = wa_connectivity-key
                                                                            hec_instance_status = wa_connectivity-hec_instance_status
                                                                            hec_tree_descr      = wa_connectivity-hec_tree_descr
                                                                            hec_row_selectable  = wa_connectivity-hec_row_selectable
                                                                            hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-connectivity
                                                                            hec_phase_guid      = wa_connectivity-hec_phase_guid
                                                                            hec_delete_visible  = wa_connectivity-hec_delete_visible
                                                                            crea_date_time      = wa_connectivity-crea_date_time
                                                                            change_request      = wa_connectivity-change_request
                                                                           ) ).


      WHEN /hec1/if_configuration_c=>sc_determination-connectivity-update
        OR /hec1/if_configuration_c=>sc_determination-connectivity-update_after_datacenter.

        lt_tree_data_update = VALUE #( FOR wa_connectivity IN CORRESPONDING /hec1/t_data_connectivity_ct( <lt_data> )
                                                                          (
                                                                            parent_node_key     = wa_connectivity-parent_key
                                                                            node_key            = wa_connectivity-key
                                                                            hec_instance_status = wa_connectivity-hec_instance_status
                                                                            hec_tree_descr      = wa_connectivity-hec_tree_descr
                                                                            hec_row_selectable  = wa_connectivity-hec_row_selectable
                                                                            hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-connectivity
                                                                            hec_phase_guid      = wa_connectivity-hec_phase_guid
                                                                            hec_delete_visible  = wa_connectivity-hec_delete_visible
                                                                            crea_date_time      = wa_connectivity-crea_date_time
                                                                            change_request      = wa_connectivity-change_request
                                                                           ) ).

      WHEN  /hec1/if_configuration_c=>sc_determination-material-create.

        lt_tree_data_insert = VALUE #( FOR wa_material IN CORRESPONDING  /hec1/t_data_material_ct( <lt_data> )
                                                                   (
                                                                     parent_node_key     = wa_material-parent_key
                                                                     node_key            = wa_material-key
                                                                     hec_instance_status = wa_material-hec_instance_status
                                                                     hec_tree_descr      = wa_material-hec_tree_descr
                                                                     hec_row_selectable  = wa_material-hec_row_selectable
                                                                     hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-material
                                                                     hec_phase_guid      = wa_material-hec_phase_guid
                                                                     hec_delete_visible  = wa_material-hec_delete_visible
                                                                     crea_date_time      = wa_material-crea_date_time
                                                                     change_request      = wa_material-change_request
                                                                    ) ).

      WHEN  /hec1/if_configuration_c=>sc_determination-material-update
         OR /hec1/if_configuration_c=>sc_determination-material-update_after_tier.

        lt_tree_data_update = VALUE #( FOR wa_material IN CORRESPONDING  /hec1/t_data_material_ct( <lt_data> )
                                                             (
                                                              parent_node_key     = wa_material-parent_key
                                                              node_key            = wa_material-key
                                                              hec_instance_status = wa_material-hec_instance_status
                                                              hec_tree_descr      = wa_material-hec_tree_descr
                                                              hec_row_selectable  = wa_material-hec_row_selectable
                                                              hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-material
                                                              hec_phase_guid      = wa_material-hec_phase_guid
                                                              hec_delete_visible  = wa_material-hec_delete_visible
                                                              crea_date_time      = wa_material-crea_date_time
                                                              change_request      = wa_material-change_request
                                                              ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-software_item-create.
        lt_tree_data_insert = VALUE #( FOR wa_software_item IN CORRESPONDING  /hec1/t_data_sw_item_ct( <lt_data> )
                                                    (
                                                     parent_node_key     = wa_software_item-parent_key
                                                     node_key            = wa_software_item-key
                                                     hec_instance_status = wa_software_item-hec_instance_status
                                                     hec_tree_descr      = wa_software_item-hec_tree_descr
                                                     hec_row_selectable  = wa_software_item-hec_row_selectable
                                                     hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-software_item
                                                     hec_phase_guid      = wa_software_item-hec_phase_guid
                                                     hec_delete_visible  = wa_software_item-hec_delete_visible
                                                     crea_date_time      = wa_software_item-crea_date_time
                                                     change_request      = wa_software_item-change_request
                                                     ) ).


      WHEN /hec1/if_configuration_c=>sc_determination-software_item-update
        OR /hec1/if_configuration_c=>sc_determination-software_item-update_after_material.
        lt_tree_data_update = VALUE #( FOR wa_software_item IN CORRESPONDING  /hec1/t_data_sw_item_ct( <lt_data> )
                                            (
                                             parent_node_key     = wa_software_item-parent_key
                                             node_key            = wa_software_item-key
                                             hec_instance_status = wa_software_item-hec_instance_status
                                             hec_tree_descr      = wa_software_item-hec_tree_descr
                                             hec_row_selectable  = wa_software_item-hec_row_selectable
                                             hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-software_item
                                             hec_phase_guid      = wa_software_item-hec_phase_guid
                                             hec_delete_visible  = wa_software_item-hec_delete_visible
                                             crea_date_time      = wa_software_item-crea_date_time
                                             change_request      = wa_software_item-change_request
                                             ) ).


      WHEN /hec1/if_configuration_c=>sc_determination-add_service-create.
        lt_tree_data_insert = VALUE #( FOR wa_add_service IN CORRESPONDING  /hec1/t_data_add_services_ct( <lt_data> )
                                    (
                                     parent_node_key     = wa_add_service-parent_key
                                     node_key            = wa_add_service-key
                                     hec_instance_status = wa_add_service-hec_instance_status
                                     hec_tree_descr      = wa_add_service-hec_tree_descr
                                     hec_row_selectable  = abap_true
                                     hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-add_service
                                     hec_phase_guid      = wa_add_service-hec_phase_guid
                                     hec_delete_visible  = wa_add_service-hec_delete_visible
                                     crea_date_time      = wa_add_service-crea_date_time
                                     change_request      = wa_add_service-change_request
                                     ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-add_service-update.
        lt_tree_data_update = VALUE #( FOR wa_add_service IN CORRESPONDING  /hec1/t_data_add_services_ct( <lt_data> )
                                (
                                 parent_node_key     = wa_add_service-parent_key
                                 node_key            = wa_add_service-key
                                 hec_instance_status = wa_add_service-hec_instance_status
                                 hec_tree_descr      = wa_add_service-hec_tree_descr
                                 hec_row_selectable  = abap_true
                                 hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-add_service
                                 hec_phase_guid      = wa_add_service-hec_phase_guid
                                 hec_delete_visible  = wa_add_service-hec_delete_visible
                                 crea_date_time      = wa_add_service-crea_date_time
                                 change_request      = wa_add_service-change_request
                                 ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-solution-create.
        lt_tree_data_insert = VALUE #( FOR wa_solution IN CORRESPONDING  /hec1/t_data_solution_ct( <lt_data> )
                (
                 parent_node_key     = wa_solution-parent_key
                 node_key            = wa_solution-key
                 hec_instance_status = wa_solution-hec_instance_status
                 hec_tree_descr      = wa_solution-hec_tree_descr
                 hec_row_selectable  = abap_true
                 hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-solution
                 hec_delete_visible  = wa_solution-hec_delete_visible
                 crea_date_time      = wa_solution-crea_date_time
                 change_request      = wa_solution-change_request
                 ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-solution-update.
        lt_tree_data_update = VALUE #( FOR wa_solution IN CORRESPONDING  /hec1/t_data_solution_ct( <lt_data> )
                (
                  parent_node_key     = wa_solution-parent_key
                  node_key            = wa_solution-key
                  hec_instance_status = wa_solution-hec_instance_status
                  hec_tree_descr      = wa_solution-hec_tree_descr
                  hec_row_selectable  = abap_true
                  hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-solution
                  hec_delete_visible  = wa_solution-hec_delete_visible
                  crea_date_time      = wa_solution-crea_date_time
                  change_request      = wa_solution-change_request
                 ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-tier_add_service-create.

        lt_tree_data_insert = VALUE #( FOR wa_tier_add_service IN CORRESPONDING /hec1/t_data_tier_add_serv_ct( <lt_data> )
                        (
                          parent_node_key     = wa_tier_add_service-parent_key
                          node_key            = wa_tier_add_service-key
                          hec_instance_status = wa_tier_add_service-hec_instance_status
                          hec_tree_descr      = wa_tier_add_service-hec_tree_descr
                          hec_row_selectable  = wa_tier_add_service-hec_row_selectable
                          hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-tier_service
                          hec_phase_guid      = wa_tier_add_service-hec_phase_guid
                          hec_delete_visible  = wa_tier_add_service-hec_delete_visible
                          crea_date_time      = wa_tier_add_service-crea_date_time
                          change_request      = wa_tier_add_service-change_request
                         ) ).

      WHEN  /hec1/if_configuration_c=>sc_determination-tier_add_service-update
        OR /hec1/if_configuration_c=>sc_determination-tier_add_service-update_after_tier.

        lt_tree_data_update = VALUE #( FOR wa_tier_add_service IN CORRESPONDING /hec1/t_data_tier_add_serv_ct( <lt_data> )
                        (
                          parent_node_key     = wa_tier_add_service-parent_key
                          node_key            = wa_tier_add_service-key
                          hec_instance_status = wa_tier_add_service-hec_instance_status
                          hec_tree_descr      = wa_tier_add_service-hec_tree_descr
                          hec_row_selectable  = wa_tier_add_service-hec_row_selectable
                          hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-tier_service
                          hec_phase_guid      = wa_tier_add_service-hec_phase_guid
                          hec_delete_visible  = wa_tier_add_service-hec_delete_visible
                          crea_date_time      = wa_tier_add_service-crea_date_time
                          change_request      = wa_tier_add_service-change_request
                         ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-tier_add_storage-create.

*        lt_tree_data_insert = VALUE #( FOR wa_tier_add_storage IN CORRESPONDING /hec1/t_tier_add_storage_ct( <lt_data> )
*                        (
*                          parent_node_key     = wa_tier_add_storage-parent_key
*                          node_key            = wa_tier_add_storage-key
*                          hec_instance_status = wa_tier_add_storage-hec_instance_status
*                          hec_tree_descr      = wa_tier_add_storage-hec_tree_descr
*                          hec_row_selectable  = abap_true
*                          hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-add_storage
*                          hec_phase_guid      = wa_tier_add_storage-hec_phase_guid
*                          hec_delete_visible  = wa_tier_add_storage-hec_delete_visible
*                          crea_date_time      = wa_tier_add_storage-crea_date_time
*                          change_request      = wa_tier_add_storage-change_request
*                         ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-tier_add_storage-update
         OR /hec1/if_configuration_c=>sc_determination-tier_add_storage-update_after_tier.

*        lt_tree_data_update = VALUE #( FOR wa_tier_add_storage IN CORRESPONDING /hec1/t_tier_add_storage_ct( <lt_data> )
*                 (
*                   parent_node_key     = wa_tier_add_storage-parent_key
*                   node_key            = wa_tier_add_storage-key
*                   hec_instance_status = wa_tier_add_storage-hec_instance_status
*                   hec_tree_descr      = wa_tier_add_storage-hec_tree_descr
*                   hec_row_selectable  = abap_true
*                   hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-add_storage
*                   hec_phase_guid      = wa_tier_add_storage-hec_phase_guid
*                   hec_delete_visible  = wa_tier_add_storage-hec_delete_visible
*                   crea_date_time      = wa_tier_add_storage-crea_date_time
*                   change_request      = wa_tier_add_storage-change_request
*                  ) ).


        " **********************************
        " Determination tier node
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_determination-tier-create.
        lt_tree_data_insert = VALUE #( FOR wa_tier IN CORRESPONDING /hec1/t_data_tier_ct( <lt_data> )
         (

          parent_node_key     = wa_tier-parent_key
          node_key            = wa_tier-key
          hec_instance_status = wa_tier-hec_instance_status
          hec_tree_descr      = wa_tier-hec_tree_descr
          hec_row_selectable  = abap_true
          hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-tier
          hec_phase_guid      = wa_tier-hec_phase_guid
          hec_delete_visible  = wa_tier-hec_delete_visible
          crea_date_time      = wa_tier-crea_date_time
          hec_sort_order      = SWITCH #( wa_tier-hec_tier_type_value
                                           " Sort range for tier 20-50
                                           WHEN ''   THEN 1 "Unknown
                                           WHEN '01' THEN 2 " Sandbox
                                           WHEN '02' THEN 3 " Development
                                           WHEN '03' THEN 4 " Quality
                                           WHEN '04' THEN 5 " Pre production
                                           WHEN '05' THEN 6 " Production
                                           )
          change_request      = wa_tier-change_request
          ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-tier-update.
        lt_tree_data_update = VALUE #( FOR wa_tier IN CORRESPONDING /hec1/t_data_tier_ct( <lt_data> )
         (
          parent_node_key     = wa_tier-parent_key
          node_key            = wa_tier-key
          hec_instance_status = wa_tier-hec_instance_status
          hec_tree_descr      = wa_tier-hec_tree_descr
          hec_row_selectable  = abap_true
          hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-tier
          hec_phase_guid      = wa_tier-hec_phase_guid
          hec_delete_visible  = wa_tier-hec_delete_visible
          crea_date_time      = wa_tier-crea_date_time
          hec_sort_order      = SWITCH #( wa_tier-hec_tier_type_value
                                           "Sort range for tier 20-50
                                           WHEN ''   THEN 1 "Unknown
                                           WHEN '01' THEN 2 " Sandbox
                                           WHEN '02' THEN 3 " Development
                                           WHEN '03' THEN 4 " Quality
                                           WHEN '04' THEN 5 " Pre production
                                           WHEN '05' THEN 6 " Production
                                           )
          change_request      = wa_tier-change_request
          ) ).

        " **********************************
        " Determination tier sla node
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_determination-tier_sla-create.
        lt_tree_data_insert = VALUE #( FOR wa_tier_sla IN CORRESPONDING /hec1/t_data_tier_sla_ct( <lt_data> )
         (
          parent_node_key     = wa_tier_sla-parent_key
          node_key            = wa_tier_sla-key
          hec_instance_status = wa_tier_sla-hec_instance_status
          hec_tree_descr      = wa_tier_sla-hec_tree_descr
          hec_row_selectable  = abap_true
          hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-tier_sla
          hec_phase_guid      = wa_tier_sla-hec_phase_guid
          hec_delete_visible  = wa_tier_sla-hec_delete_visible
          crea_date_time      = wa_tier_sla-crea_date_time
          change_request      = wa_tier_sla-change_request
          ) ).

      WHEN /hec1/if_configuration_c=>sc_determination-tier_sla-update.
        lt_tree_data_update = VALUE #( FOR wa_tier_sla IN CORRESPONDING /hec1/t_data_tier_sla_ct( <lt_data> )
         (
          parent_node_key     = wa_tier_sla-parent_key
          node_key            = wa_tier_sla-key
          hec_instance_status = wa_tier_sla-hec_instance_status
          hec_tree_descr      = wa_tier_sla-hec_tree_descr
          hec_row_selectable  = abap_true
          hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-tier_sla
          hec_phase_guid      = wa_tier_sla-hec_phase_guid
          hec_delete_visible  = wa_tier_sla-hec_delete_visible
          crea_date_time      = wa_tier_sla-crea_date_time
          change_request      = wa_tier_sla-change_request
          ) ).


      WHEN /hec1/if_configuration_c=>sc_determination-phase-create.
        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert_phasing(
                                                                                           VALUE #( FOR wa_phase IN CORRESPONDING /hec1/t_data_phase_ct( <lt_data> )
                                                                                                    WHERE ( hec_phase_generated = abap_false )
                                                                                                          (
                                                                                                          parent_key          = wa_phase-hec_node_parent_phase
                                                                                                          row_key             = wa_phase-hec_node_phase
                                                                                                          parent_node_key     = wa_phase-parent_key
                                                                                                          node_key            = wa_phase-key
                                                                                                          hec_tree_descr      = wa_phase-hec_phase_tree_descr
                                                                                                          hec_row_selectable  = abap_true
                                                                                                          hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-phase
                                                                                                          hec_delete_visible  = wa_phase-hec_delete_visible
                                                                                                          hec_phase_start_date       = wa_phase-hec_phase_start_date
                                                                                                          hec_phase_end_date         = wa_phase-hec_phase_end_date
                                                                                                          hec_phase_successor_guid   = wa_phase-hec_phase_successor_guid
                                                                                                          hec_phase_predecessor_guid = wa_phase-hec_phase_predecessor_guid ) )
                                                                                                          ).

      WHEN /hec1/if_configuration_c=>sc_determination-phase-update.
        /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update_phasing(
                                                                                              VALUE #( FOR wa_phase IN CORRESPONDING /hec1/t_data_phase_ct( <lt_data> )
                                                                                                       WHERE ( hec_phase_generated = abap_false )
                                                                                                             (
                                                                                                              parent_key          = wa_phase-hec_node_parent_phase
                                                                                                              row_key             = wa_phase-hec_node_phase
                                                                                                              parent_node_key     = wa_phase-parent_key
                                                                                                              node_key            = wa_phase-key
                                                                                                              hec_tree_descr      = wa_phase-hec_phase_tree_descr
                                                                                                              hec_row_selectable  = abap_true
                                                                                                              hec_obj_type        = /hec1/if_config_constants=>gc_tree_child-phase
                                                                                                              hec_delete_visible  = wa_phase-hec_delete_visible
                                                                                                              hec_phase_start_date       = wa_phase-hec_phase_start_date
                                                                                                              hec_phase_end_date         = wa_phase-hec_phase_end_date
                                                                                                              hec_phase_successor_guid   = wa_phase-hec_phase_successor_guid
                                                                                                              hec_phase_predecessor_guid = wa_phase-hec_phase_predecessor_guid
                                                                                                              hec_phase_complete         = wa_phase-hec_phase_complete
                                                                                                             )
                                                                                                        ) ) .

    ENDCASE.


    IF lt_tree_data_insert IS NOT INITIAL.
      /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~insert( lt_tree_data_insert ).
    ENDIF.

    IF lt_tree_data_update IS NOT INITIAL.
      /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~update( lt_tree_data_update ).
    ENDIF.

  ENDMETHOD.


  METHOD determine_tier_sla.

    DATA: lt_tier              TYPE /hec1/t_data_tier_ct,
          lt_tier_sla          TYPE /hec1/t_data_tier_sla_ct,
          lt_tier_sla_before   TYPE /hec1/t_data_tier_sla_ct,
          lt_phase             TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    " Data before update
    io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                 it_key          = it_key
                                 iv_before_image = abap_true
                       IMPORTING et_data         = lt_tier_sla_before ).

    " Data after update
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_tier_sla ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit)
                                                        et_datacenter    = DATA(lt_datacenter) ).

    " Tier
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier_sla-to_parent
                                      IMPORTING et_data        = lt_tier ).

    " Phasing
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = VALUE #( ( key = lv_root_key ) )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                      IMPORTING et_data        = lt_phase ).


    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier_sla-create.
            LOOP AT lt_tier_sla REFERENCE INTO DATA(lr_tier_sla).

              lr_tier_sla->hec_delete_visible = abap_true.

              ASSIGN lt_tier[ key = lr_tier_sla->parent_key ] TO FIELD-SYMBOL(<fs_tier>).
              IF <fs_tier> IS ASSIGNED.
                "-----------------------------------
                " Get tier SLA and uplift
                "-----------------------------------
                SELECT *
                  FROM /hec1/i_tierslabasic
                 WHERE hec_apm_guid       = @lr_landscape->hec_apm_guid      AND
                       hec_flat_mat_guid  = @lr_landscape->hec_flat_mat_guid AND
                       hec_tier_cat_value = @<fs_tier>-hec_tier_cat_value
                  INTO TABLE @DATA(lt_sla).

                "-----------------------------------
                " Set default support status
                "-----------------------------------
                TRY.
                    DATA(ls_sla) = lt_sla[ hec_sla_support_stat_value = '02'
                                           hec_tier_ha_setup          = abap_false ].


                    lr_tier_sla->hec_tier_sla                 = ls_sla-hec_tier_sla.
                    lr_tier_sla->hec_tier_sla_uplift          = ls_sla-hec_tier_sla_uplift.
                    lr_tier_sla->hec_tier_ha_setup            = ls_sla-hec_tier_ha_setup.
                    lr_tier_sla->hec_init_sla_sup_stat_value  = ls_sla-hec_sla_support_stat_value.
                    lr_tier_sla->hec_init_sla_supp_stat_descr = ls_sla-hec_sla_support_stat_descr.
                    lr_tier_sla->hec_sla_support_stat_value   = ls_sla-hec_sla_support_stat_value.
                    lr_tier_sla->hec_sla_support_stat_descr   = ls_sla-hec_sla_support_stat_descr.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF. " IF <fs_tier> IS ASSIGNED.

              "-----------------------------------
              " Set Tree Description
              "-----------------------------------
              lr_tier_sla->hec_tree_descr = |{ lr_tier_sla->hec_tier_sla } { VALUE #( lt_phase[ hec_node_phase = lr_tier_sla->hec_phase_guid ]-hec_phase_descr OPTIONAL ) }|.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_tier_sla->hec_tier_sla   IS NOT INITIAL AND
                                                                             lr_tier_sla->hec_phase_guid IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_tier_sla->hec_instance_status.
                lr_tier_sla->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify tier
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_tier_sla->key
                                   is_data = lr_tier_sla ).
              ENDIF.

              UNASSIGN <fs_tier>.
              CLEAR: lv_inst_status,
                     lv_data_changed,
                     ls_sla,
                     lt_sla.
            ENDLOOP.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier_sla-update.
            LOOP AT lt_tier_sla REFERENCE INTO lr_tier_sla.

              ASSIGN lt_tier_sla_before[ key = lr_tier_sla->key ] TO FIELD-SYMBOL(<fs_tier_sla_before>).
              IF <fs_tier_sla_before> IS ASSIGNED.

                ASSIGN lt_tier[ key = lr_tier_sla->parent_key ] TO <fs_tier>.
                IF <fs_tier> IS ASSIGNED.

                  "-----------------------------------
                  " SLA has changed
                  "-----------------------------------
                  IF lr_tier_sla->hec_tier_sla IS NOT INITIAL                        AND
                     lr_tier_sla->hec_tier_sla <> <fs_tier_sla_before>-hec_tier_sla.

                    " Get tier SLA and uplift
                    SELECT SINGLE *
                      FROM /hec1/i_tierslabasic
                     WHERE hec_apm_guid       = @lr_landscape->hec_apm_guid      AND
                           hec_flat_mat_guid  = @lr_landscape->hec_flat_mat_guid AND
                           hec_tier_cat_value = @<fs_tier>-hec_tier_cat_value    AND
                           hec_tier_sla       = @lr_tier_sla->hec_tier_sla
                      INTO @ls_sla.

                    lr_tier_sla->hec_tier_sla                 = ls_sla-hec_tier_sla.
                    lr_tier_sla->hec_tier_sla_uplift          = ls_sla-hec_tier_sla_uplift.
                    lr_tier_sla->hec_tier_ha_setup            = ls_sla-hec_tier_ha_setup.
                    lr_tier_sla->hec_init_sla_sup_stat_value  = ls_sla-hec_sla_support_stat_value.
                    lr_tier_sla->hec_init_sla_supp_stat_descr = ls_sla-hec_sla_support_stat_descr.
                    lr_tier_sla->hec_sla_support_stat_value   = ls_sla-hec_sla_support_stat_value.
                    lr_tier_sla->hec_sla_support_stat_descr   = ls_sla-hec_sla_support_stat_descr.
                    lv_data_changed                           = abap_true.
                  ENDIF. " IF lr_tier_sla->hec_tier_sla IS NOT INITIAL AND...
                ENDIF. " IF <fs_tier> IS ASSIGNED.

                "-----------------------------------
                " Value List Quantity - SLA
                "-----------------------------------
                lr_tier_sla->hec_tier_sla_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_tier_sla(
                                                                                iv_apm_guid       = lr_landscape->hec_apm_guid
                                                                                iv_flat_mat_guid  = lr_landscape->hec_flat_mat_guid
                                                                                iv_tier_cat_value = <fs_tier>-hec_tier_cat_value
                                                                                iv_tier_ha_setup  = abap_false ) )
                                                         THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                         ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_tier_sla->hec_phase_guid NE <fs_tier_sla_before>-hec_phase_guid.

*                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
*                                  hec_bopf_key       = lr_tier_sla->key
*                                  hec_phase_guid_new = lr_tier_sla->hec_phase_guid
*                                  hec_phase_guid_old = <fs_tier_sla_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_tier_sla->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "phasing changed

                "-----------------------------------
                " Set Tree Description
                "-----------------------------------
                IF lr_tier_sla->hec_tier_sla NE <fs_tier_sla_before>-hec_tier_sla
                  OR lr_tier_sla->hec_phase_guid NE <fs_tier_sla_before>-hec_phase_guid.
                  lr_tier_sla->hec_tree_descr = |{ lr_tier_sla->hec_tier_sla } { VALUE #( lt_phase[ hec_node_phase = lr_tier_sla->hec_phase_guid ]-hec_phase_descr OPTIONAL ) }|.
                ENDIF.

              ENDIF. "<fs_tier_sla_before> is assigned

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_tier_sla->hec_tier_sla   IS NOT INITIAL AND
                                                                       lr_tier_sla->hec_phase_guid IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_tier_sla->hec_instance_status.
                lr_tier_sla->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify tier sla
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_tier_sla->key
                                   is_data = lr_tier_sla ).
              ENDIF.

              CLEAR: lv_data_changed,
                     lv_inst_status.

              UNASSIGN: <fs_tier_sla_before>,
                        <fs_tier>.
            ENDLOOP. " LOOP AT lt_tier_sla REFERENCE INTO lr_tier_sla.


*            "-----------------------------------
*            " Update Phasing
*            "-----------------------------------
*            IF lt_act_param_phasing IS NOT INITIAL.
*              CLEAR me->mr_act_param_phasing.
*              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).
*
*              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
*                  is_ctx          = CORRESPONDING #( is_ctx )
*                  it_key          = it_key
*                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
*                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
*                  ir_act_param    = me->mr_act_param_phasing ).
*            ENDIF.
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_contact.

    DATA: lt_contact        TYPE /hec1/t_data_contact_ct,
          lt_contact_before TYPE /hec1/t_data_contact_ct.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_contact ).

    io_read->get_root_key( EXPORTING iv_node       = is_ctx-node_key
                                     it_key        = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create Mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-contact-create.

            LOOP AT lt_contact REFERENCE INTO DATA(lr_contact).

*            IF lv_data_changed = abap_true.
*              io_modify->update( iv_node = is_ctx-node_key
*                                 iv_key  = lr_phase->key
*                                 is_data = lr_phase   ).
*            ENDIF.
*
*            CLEAR: lv_data_changed.

            ENDLOOP.

            " ***************************************************************************
            " Update Mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-contact-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                                         iv_fill_data    = abap_true
                               IMPORTING et_data         = lt_contact_before ).

            LOOP AT lt_contact REFERENCE INTO lr_contact.
              ASSIGN lt_contact_before[ key = lr_contact->key ] TO FIELD-SYMBOL(<fs_contact_before>).

              IF <fs_contact_before> IS ASSIGNED.

              ENDIF. "<fs_contact_before> is assigned.

*              IF lv_data_changed = abap_true.
*                io_modify->update( iv_node = is_ctx-node_key
*                                   iv_key  = lr_phase->key
*                                   is_data = lr_phase   ).
*              ENDIF.
*
*              CLEAR: lv_data_changed.

              UNASSIGN <fs_contact_before>.

            ENDLOOP. "lt_contact
        ENDCASE. "is_ctx

      CATCH /bobf/cx_frw.
      CATCH cx_uuid_error. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD determine_contact_reference.

    DATA: lt_contact_ref        TYPE /hec1/t_data_contact_ref_ct,
          lt_contact_ref_before TYPE /hec1/t_data_contact_ref_ct.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_contact_ref ).

    io_read->get_root_key( EXPORTING iv_node       = is_ctx-node_key
                                     it_key        = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create Mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-contact_reference-create.

            LOOP AT lt_contact_ref REFERENCE INTO DATA(lr_contact_ref).

*            IF lv_data_changed = abap_true.
*              io_modify->update( iv_node = is_ctx-node_key
*                                 iv_key  = lr_phase->key
*                                 is_data = lr_phase   ).
*            ENDIF.
*
*            CLEAR: lv_data_changed.

            ENDLOOP.

            " ***************************************************************************
            " Update Mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-contact_reference-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                                         iv_fill_data    = abap_true
                               IMPORTING et_data         = lt_contact_ref_before ).

            LOOP AT lt_contact_ref REFERENCE INTO lr_contact_ref.
              ASSIGN lt_contact_ref_before[ key = lr_contact_ref->key ] TO FIELD-SYMBOL(<fs_contact_ref_before>).

              IF <fs_contact_ref_before> IS ASSIGNED.

              ENDIF. "<fs_contact_ref_before> is assigned.

*              IF lv_data_changed = abap_true.
*                io_modify->update( iv_node = is_ctx-node_key
*                                   iv_key  = lr_phase->key
*                                   is_data = lr_phase   ).
*              ENDIF.
*
*              CLEAR: lv_data_changed.

              UNASSIGN <fs_contact_ref_before>.

            ENDLOOP. "lt_contact_ref
        ENDCASE. "is_ctx

      CATCH /bobf/cx_frw.
      CATCH cx_uuid_error. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD determine_tier_sla_cr.

    DATA: lt_tier              TYPE /hec1/t_data_tier_ct,
          lt_tier_sla          TYPE /hec1/t_data_tier_sla_ct,
          lt_tier_sla_before   TYPE /hec1/t_data_tier_sla_ct,
          lt_phase             TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    " Data before update
    io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                 it_key          = it_key
                                 iv_before_image = abap_true
                       IMPORTING et_data         = lt_tier_sla_before ).

    " Data after update
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_tier_sla ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit)
                                                        et_datacenter    = DATA(lt_datacenter) ).

    " Tier
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier_sla-to_parent
                                      IMPORTING et_data        = lt_tier ).

    " Phasing
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = VALUE #( ( key = lv_root_key ) )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                      IMPORTING et_data        = lt_phase ).


    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier_sla-create.
            LOOP AT lt_tier_sla REFERENCE INTO DATA(lr_tier_sla).

              lr_tier_sla->hec_delete_visible = abap_true.

              ASSIGN lt_tier[ key = lr_tier_sla->parent_key ] TO FIELD-SYMBOL(<fs_tier>).
              IF <fs_tier> IS ASSIGNED.
                "-----------------------------------
                " Get tier SLA and uplift
                "-----------------------------------
                SELECT *
                  FROM /hec1/i_tierslabasic
                 WHERE hec_apm_guid       = @lr_landscape->hec_apm_guid      AND
                       hec_flat_mat_guid  = @lr_landscape->hec_flat_mat_guid AND
                       hec_tier_cat_value = @<fs_tier>-hec_tier_cat_value
                  INTO TABLE @DATA(lt_sla).

                "-----------------------------------
                " Set default support status
                "-----------------------------------
                TRY.
                    DATA(ls_sla) = lt_sla[ hec_sla_support_stat_value = '02'
                                           hec_tier_ha_setup          = abap_false ].


                    lr_tier_sla->hec_tier_sla                 = ls_sla-hec_tier_sla.
                    lr_tier_sla->hec_tier_sla_uplift          = ls_sla-hec_tier_sla_uplift.
                    lr_tier_sla->hec_tier_ha_setup            = ls_sla-hec_tier_ha_setup.
                    lr_tier_sla->hec_init_sla_sup_stat_value  = ls_sla-hec_sla_support_stat_value.
                    lr_tier_sla->hec_init_sla_supp_stat_descr = ls_sla-hec_sla_support_stat_descr.
                    lr_tier_sla->hec_sla_support_stat_value   = ls_sla-hec_sla_support_stat_value.
                    lr_tier_sla->hec_sla_support_stat_descr   = ls_sla-hec_sla_support_stat_descr.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF. " IF <fs_tier> IS ASSIGNED.

              "-----------------------------------
              " Set Tree Description
              "-----------------------------------
              lr_tier_sla->hec_tree_descr = |{ lr_tier_sla->hec_tier_sla } { VALUE #( lt_phase[ hec_node_phase = lr_tier_sla->hec_phase_guid ]-hec_phase_descr OPTIONAL ) }|.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_tier_sla->hec_tier_sla   IS NOT INITIAL AND
                                                                             lr_tier_sla->hec_phase_guid IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_tier_sla->hec_instance_status.
                lr_tier_sla->hec_instance_status = lv_inst_status.
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
                  is_node_data = lr_tier_sla
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              "-----------------------------------
              " Modify tier
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_tier_sla->key
                                   is_data = lr_tier_sla ).
              ENDIF.

              UNASSIGN <fs_tier>.
              CLEAR: lv_inst_status,
                     lv_data_changed,
                     ls_sla,
                     lt_sla.
            ENDLOOP.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier_sla-update.
            LOOP AT lt_tier_sla REFERENCE INTO lr_tier_sla.

              ASSIGN lt_tier_sla_before[ key = lr_tier_sla->key ] TO FIELD-SYMBOL(<fs_tier_sla_before>).
              IF <fs_tier_sla_before> IS ASSIGNED.

                ASSIGN lt_tier[ key = lr_tier_sla->parent_key ] TO <fs_tier>.
                IF <fs_tier> IS ASSIGNED.

                  "-----------------------------------
                  " SLA has changed
                  "-----------------------------------
                  IF lr_tier_sla->hec_tier_sla IS NOT INITIAL                        AND
                     lr_tier_sla->hec_tier_sla <> <fs_tier_sla_before>-hec_tier_sla.

                    " Get tier SLA and uplift
                    SELECT SINGLE *
                      FROM /hec1/i_tierslabasic
                     WHERE hec_apm_guid       = @lr_landscape->hec_apm_guid      AND
                           hec_flat_mat_guid  = @lr_landscape->hec_flat_mat_guid AND
                           hec_tier_cat_value = @<fs_tier>-hec_tier_cat_value    AND
                           hec_tier_sla       = @lr_tier_sla->hec_tier_sla
                      INTO @ls_sla.

                    lr_tier_sla->hec_tier_sla                 = ls_sla-hec_tier_sla.
                    lr_tier_sla->hec_tier_sla_uplift          = ls_sla-hec_tier_sla_uplift.
                    lr_tier_sla->hec_tier_ha_setup            = ls_sla-hec_tier_ha_setup.
                    lr_tier_sla->hec_init_sla_sup_stat_value  = ls_sla-hec_sla_support_stat_value.
                    lr_tier_sla->hec_init_sla_supp_stat_descr = ls_sla-hec_sla_support_stat_descr.
                    lr_tier_sla->hec_sla_support_stat_value   = ls_sla-hec_sla_support_stat_value.
                    lr_tier_sla->hec_sla_support_stat_descr   = ls_sla-hec_sla_support_stat_descr.
                    lv_data_changed                           = abap_true.
                  ENDIF. " IF lr_tier_sla->hec_tier_sla IS NOT INITIAL AND...
                ENDIF. " IF <fs_tier> IS ASSIGNED.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_tier_sla->hec_phase_guid NE <fs_tier_sla_before>-hec_phase_guid.

*                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
*                                  hec_bopf_key       = lr_tier_sla->key
*                                  hec_phase_guid_new = lr_tier_sla->hec_phase_guid
*                                  hec_phase_guid_old = <fs_tier_sla_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_tier_sla->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "phasing changed

                "-----------------------------------
                " Set Tree Description
                "-----------------------------------
                IF lr_tier_sla->hec_tier_sla NE <fs_tier_sla_before>-hec_tier_sla
                  OR lr_tier_sla->hec_phase_guid NE <fs_tier_sla_before>-hec_phase_guid.
                  lr_tier_sla->hec_tree_descr = |{ lr_tier_sla->hec_tier_sla } { VALUE #( lt_phase[ hec_node_phase = lr_tier_sla->hec_phase_guid ]-hec_phase_descr OPTIONAL ) }|.
                ENDIF.

              ENDIF. "<fs_tier_sla_before> is assigned

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_tier_sla->hec_tier_sla   IS NOT INITIAL AND
                                                                       lr_tier_sla->hec_phase_guid IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_tier_sla->hec_instance_status.
                lr_tier_sla->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify tier sla
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_tier_sla->key
                                   is_data = lr_tier_sla ).
              ENDIF.

              CLEAR: lv_data_changed,
                     lv_inst_status.

              UNASSIGN: <fs_tier_sla_before>,
                        <fs_tier>.
            ENDLOOP. " LOOP AT lt_tier_sla REFERENCE INTO lr_tier_sla.


*            "-----------------------------------
*            " Update Phasing
*            "-----------------------------------
*            IF lt_act_param_phasing IS NOT INITIAL.
*              CLEAR me->mr_act_param_phasing.
*              me->mr_act_param_phasing = NEW /hec1/t_act_phase_inherit( lt_act_param_phasing ).
*
*              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
*                  is_ctx          = CORRESPONDING #( is_ctx )
*                  it_key          = it_key
*                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-inherit_phase_assignment )
*                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
*                  ir_act_param    = me->mr_act_param_phasing ).
*            ENDIF.
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_tier_cr.

    DATA: lt_tier               TYPE /hec1/t_data_tier_ct,
          lt_tier_before        TYPE /hec1/t_data_tier_ct,
          lt_alt_key            TYPE TABLE OF /hec1/datacenter_guid,
          lt_act_param          TYPE /hec1/t_act_create_serv_inst,
          lt_act_param_sla      TYPE /hec1/t_act_create_tier_sla,
          lt_db_serv_inst       TYPE /hec1/t_data_db_server_inst_ct,
          lt_app_serv_inst      TYPE /hec1/t_data_app_serv_inst_ct,
          ls_landscape          TYPE /hec1/s_config_root_cs,
          lt_phase              TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing  TYPE TABLE OF /hec1/s_act_phase_inherit,
          lt_act_param_material TYPE /hec1/t_act_create_material.


    CLEAR: eo_message,
           et_failed_key,
           me->mr_act_param,
           me->mr_act_param1,
           me->mr_act_param_sla.

    " Data before update
    io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                 it_key          = it_key
                                 iv_before_image = abap_true
                       IMPORTING et_data         = lt_tier_before ).

    " Data after update
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_tier ).


    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit)
                                                        et_datacenter    = DATA(lt_datacenter) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier-create.

            LOOP AT lt_tier REFERENCE INTO DATA(lr_tier).

              "-----------------------------------
              " Set Value List Quantity - Tier Type
              "-----------------------------------
              lr_tier->hec_tier_type_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_tier_type(
                                                                      iv_apm_guid       = lr_landscape->hec_apm_guid
                                                                      iv_flat_mat_guid  = lr_landscape->hec_flat_mat_guid
                                                                      iv_tier_cat_value = lr_tier->hec_tier_cat_value ) )
                                                    THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                    ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              lr_tier->hec_delete_visible = abap_true.

              "-----------------------------------
              " Get data center decription
              "-----------------------------------
              IF lt_datacenter IS NOT INITIAL.
                TRY.
                    DATA(lv_datacenter_descr) = lt_datacenter[ hec_node_datacenter = lr_tier->hec_tier_datacenter_guid ]-hec_datacenter_descr.
                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_tier->hec_tier_descr           IS NOT INITIAL AND
                                                                             lr_tier->hec_tier_impl_type_value IS NOT INITIAL AND
                                                                             lr_tier->hec_tier_type_value      IS NOT INITIAL AND
                                                                             lr_tier->hec_phase_guid           IS NOT INITIAL AND
                                                                             lr_tier->hec_tier_datacenter_guid IS NOT INITIAL AND
                                                                             lv_datacenter_descr               IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_tier->hec_instance_status.
                lr_tier->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " DB/App server instance
              "-----------------------------------
              IF lr_tier->hec_db_srv_required  = abap_true  OR
                 lr_tier->hec_app_srv_required = abap_true.
                INSERT VALUE #( key                    = lr_tier->key
                                hec_db_srv_qty         = COND #( WHEN lr_tier->hec_db_srv_required = abap_true
                                                                 THEN lr_tier->hec_db_srv_qty
                                                                  ELSE 0                                        )
                                hec_app_srv_qty        = COND #( WHEN lr_tier->hec_app_srv_required = abap_true
                                                                 THEN lr_tier->hec_app_srv_qty
                                                                 ELSE 0                                         )
                                hec_default_server_inst = abap_true                                               ) INTO TABLE lt_act_param.
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
                  is_node_data = lr_tier
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              IF lv_data_changed = abap_false.
                lv_data_changed = lv_cr_data_changed.
              ENDIF.

              "-----------------------------------
              " Implementation Type already set
              "   if implementation type is "Greenfield"
              "   the migration scenario needs to be set to
              "   "No migration"
              "-----------------------------------
              IF lr_tier->hec_tier_impl_type_value = /hec1/if_config_constants=>gc_tier_impl_type-greenfield.
                lr_tier->hec_tier_migr_scen_value = 'GR_NoMig'.
              ENDIF.

              "-----------------------------------
              " Fill action table for create
              " Material
              "-----------------------------------
              INSERT VALUE #( parent_key = lr_tier->key ) INTO TABLE lt_act_param_material.

              "-----------------------------------
              " Fill action table for create
              " Tier SLA
              "-----------------------------------
              INSERT VALUE #( parent_key = lr_tier->key ) INTO TABLE lt_act_param_sla.

              "-----------------------------------
              " Modify tier
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_tier->key
                                   is_data = lr_tier ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_datacenter_descr,
                     lv_data_changed,
                     lt_datacenter.
            ENDLOOP.

            "-----------------------------------
            " Set create Tier SLA
            " action to general
            "-----------------------------------
            IF lt_act_param_sla IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_tier_sla )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                  ).
            ENDIF.


            "-----------------------------------
            " Set create DB/App server instance
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_serv_inst( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_serv_inst )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                  ).
            ENDIF.


            "-----------------------------------
            " Set Follow-Up to GENERAL
            " - Create Material
            "-----------------------------------
            IF lt_act_param_material IS NOT INITIAL.

              me->mr_act_param_material_add = NEW /hec1/t_act_create_material( lt_act_param_material ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                   is_ctx          = CORRESPONDING #( is_ctx )
                   it_key          = VALUE #( FOR mat_add IN lt_act_param_material
                                            ( key = mat_add-parent_key ) )
                   iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_material )
                   iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                   ir_act_param    = me->mr_act_param_material_add ).
            ENDIF.


            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier-update.

            " DB Server Instance
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier-db_server_instance
                                              IMPORTING et_data        = lt_db_serv_inst ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " App Server Instance
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier-app_server_instance
                                              IMPORTING et_data        = lt_app_serv_inst ).

            " DB Server Instance
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier-db_server_instance
                                              IMPORTING et_data        = lt_db_serv_inst ).



            LOOP AT lt_tier REFERENCE INTO lr_tier.
              "-----------------------------------
              " Get data center decription
              "-----------------------------------
              IF lt_datacenter IS NOT INITIAL.
                TRY.
                    lv_datacenter_descr = lt_datacenter[ hec_node_datacenter = lr_tier->hec_tier_datacenter_guid ]-hec_datacenter_descr.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF.

              ASSIGN lt_tier_before[ key = lr_tier->key ] TO FIELD-SYMBOL(<fs_tier_before>).
              IF <fs_tier_before> IS ASSIGNED.

                "-----------------------------------
                " Tier type or tier description
                " has changed
                "-----------------------------------
                IF lr_tier->hec_tier_type_value <> <fs_tier_before>-hec_tier_type_value OR
                   lr_tier->hec_tier_descr      <> <fs_tier_before>-hec_tier_descr      OR
                   lr_tier->hec_tier_sid        <> <fs_tier_before>-hec_tier_sid.

                  " Get tier type description and DR option
                  SELECT SINGLE *
                   FROM /hec1/i_tiertypebasic
                  WHERE hec_apm_guid        = @lr_landscape->hec_apm_guid      AND
                        hec_flat_mat_guid   = @lr_landscape->hec_flat_mat_guid AND
                        hec_tier_type_value = @lr_tier->hec_tier_type_value
                   INTO CORRESPONDING FIELDS OF @lr_tier->*.

                  DATA(lv_tier_description) = |{ lr_tier->hec_tier_type_descr }{
                                                      COND #( WHEN lr_tier->hec_tier_type_value IS INITIAL OR
                                                                   lr_tier->hec_tier_descr      IS INITIAL
                                                              THEN ||
                                                              ELSE | : | ) }{ lr_tier->hec_tier_descr }{
                                                      COND #( WHEN lr_tier->hec_tier_sid IS INITIAL
                                                              THEN ||
                                                              ELSE | ( { lr_tier->hec_tier_sid } ) | ) }|.

                  lr_tier->hec_tree_descr = lv_tier_description.
                  lv_data_changed         = abap_true.

                  " Set Value List Quantity - Tier Type
                  lr_tier->hec_tier_type_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_tier_type(
                                                                          iv_apm_guid       = lr_landscape->hec_apm_guid
                                                                          iv_flat_mat_guid  = lr_landscape->hec_flat_mat_guid
                                                                          iv_tier_cat_value = lr_tier->hec_tier_cat_value ) )
                                                        THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                        ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                ENDIF." IF lr_tier->hec_tier_type_guid <> <fs_tier_before>-hec_tier_type_guid OR...

                "-----------------------------------
                " App server instance number changed
                " added or removed
                "-----------------------------------
                IF lr_tier->hec_app_srv_qty_opt <> <fs_tier_before>-hec_app_srv_qty_opt.

                  DATA(lt_app_server_lines) = VALUE /hec1/t_data_app_serv_inst_ct( FOR app_serv_inst IN lt_app_serv_inst
                                                                                   WHERE ( parent_key = lr_tier->key )
                                                                                   ( app_serv_inst ) ).

                  DATA(lt_app_server_lines_optional) = VALUE /hec1/t_data_app_serv_inst_ct( FOR app_serv_inst IN lt_app_serv_inst
                                                                                            WHERE ( parent_key = lr_tier->key AND
                                                                                                    hec_srv_inst_rel_value = /hec1/if_config_constants=>gc_relevance-optional )
                                                                                            ( app_serv_inst ) ).

                  IF lr_tier->hec_app_srv_qty_opt > <fs_tier_before>-hec_app_srv_qty_opt.
                    INSERT VALUE #( key     = lr_tier->key
                                    hec_db_srv_qty   = 0
                                    hec_app_srv_qty  = lr_tier->hec_app_srv_qty_opt - <fs_tier_before>-hec_app_srv_qty_opt ) INTO TABLE lt_act_param.

                    " Success message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_server_added
                                                                   iv_severity = /bobf/cm_frw=>co_severity_success
                                                                   iv_attr1    = CONV #( lr_tier->hec_app_srv_qty_opt - <fs_tier_before>-hec_app_srv_qty_opt )
                                                         CHANGING  co_message  = eo_message ).


                  ELSEIF lr_tier->hec_app_srv_qty_opt < <fs_tier_before>-hec_app_srv_qty_opt
                     AND lr_tier->hec_app_srv_qty_opt < lines( lt_app_server_lines_optional ).
                    DATA(lv_attr_name) = /hec1/if_configuration_c=>sc_node_attribute-tier-hec_app_srv_qty_opt.
                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_tier->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_tier->hec_app_srv_qty_opt = <fs_tier_before>-hec_app_srv_qty_opt.
                    lv_data_changed = abap_true.

                  ELSEIF <fs_tier_before>-hec_app_srv_qty_opt > lines( lt_app_server_lines_optional ).
                    lv_data_changed = abap_true.
                  ENDIF. " IF lr_tier->hec_app_srv_qty > <fs_tier_before>-hec_app_srv_qty.
                ENDIF. " IF lr_tier->hec_app_srv_qty_opt <> <fs_tier_before>-hec_app_srv_qty_opt.


                "-----------------------------------
                " DB server instance number changed
                " added or removed
                "-----------------------------------
                IF lr_tier->hec_db_srv_qty_opt <> <fs_tier_before>-hec_db_srv_qty_opt.

                  DATA(lt_db_server_lines) = VALUE /hec1/t_data_db_server_inst_ct( FOR db_serv_inst IN lt_db_serv_inst
                                                                                   WHERE ( parent_key = lr_tier->key )
                                                                                   ( db_serv_inst )                    ).

                  DATA(lt_db_server_lines_optional) = VALUE /hec1/t_data_db_server_inst_ct( FOR db_serv_inst IN lt_db_serv_inst
                                                                                            WHERE ( parent_key = lr_tier->key AND
                                                                                                    hec_srv_inst_rel_value = /hec1/if_config_constants=>gc_relevance-optional )
                                                                                            ( db_serv_inst )                                                                    ).

                  IF lr_tier->hec_db_srv_qty_opt > <fs_tier_before>-hec_db_srv_qty_opt.

                    ASSIGN lt_act_param[ key = lr_tier->key ] TO FIELD-SYMBOL(<fs_act_param>).
                    IF <fs_act_param> IS ASSIGNED.
                      <fs_act_param>-hec_db_srv_qty = lr_tier->hec_db_srv_qty_opt - <fs_tier_before>-hec_db_srv_qty_opt.
                    ELSE.
                      INSERT VALUE #( key             = lr_tier->key
                                      hec_db_srv_qty  = lr_tier->hec_db_srv_qty_opt - <fs_tier_before>-hec_db_srv_qty_opt
                                      hec_app_srv_qty = 0                                                                 ) INTO TABLE lt_act_param.

                    ENDIF.
                    " Success message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_server_added
                                                                   iv_severity = /bobf/cm_frw=>co_severity_success
                                                                   iv_attr1    = CONV #( lr_tier->hec_db_srv_qty_opt - <fs_tier_before>-hec_db_srv_qty_opt )
                                                         CHANGING  co_message  = eo_message ).


                  ELSEIF lr_tier->hec_db_srv_qty_opt < <fs_tier_before>-hec_db_srv_qty_opt
                     AND lr_tier->hec_db_srv_qty_opt < lines( lt_db_server_lines_optional ).
                    lv_attr_name = /hec1/if_configuration_c=>sc_node_attribute-tier-hec_db_srv_qty_opt.
                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_tier->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_tier->hec_db_srv_qty_opt = <fs_tier_before>-hec_db_srv_qty_opt.
                    lv_data_changed = abap_true.

                  ELSEIF <fs_tier_before>-hec_db_srv_qty_opt > lines( lt_db_server_lines_optional ).
                    lv_data_changed = abap_true.
                  ENDIF. " IF lr_tier->hec_db_srv_qty > <fs_tier_before>-hec_db_srv_qty.
                ENDIF. " IF lr_tier->hec_db_srv_qty_opt <> <fs_tier_before>-hec_db_srv_qty_opt.

                "-----------------------------------
                " Implementation Type changed
                "   if implementation type is "Greenfield"
                "   the migration scenario needs to be set to
                "   "No migration"
                "-----------------------------------
                IF lr_tier->hec_tier_impl_type_value = /hec1/if_config_constants=>gc_tier_impl_type-greenfield
                  AND <fs_tier_before>-hec_tier_impl_type_value IS INITIAL.
                  lr_tier->hec_tier_migr_scen_value = 'GR_NoMig'.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_tier->hec_phase_guid NE <fs_tier_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_tier->key
                                  hec_phase_guid_new = lr_tier->hec_phase_guid
                                  hec_phase_guid_old = <fs_tier_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_tier->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "phasing changed
              ENDIF. "<fs_tier_before> is assigned

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_tier->hec_tier_descr           IS NOT INITIAL AND
                                                                       lr_tier->hec_tier_type_value      IS NOT INITIAL AND
                                                                       lr_tier->hec_tier_impl_type_value IS NOT INITIAL AND
                                                                       lr_tier->hec_phase_guid           IS NOT INITIAL AND
                                                                       lr_tier->hec_tier_datacenter_guid IS NOT INITIAL AND
                                                                       lv_datacenter_descr               IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_tier->hec_instance_status.
                lr_tier->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "Set default reference if only one other tier exists
              IF lr_tier->hec_tier_is_reference = abap_true.
                DATA(lt_tier_list) = /hec1/cl_config_sw_helper=>get_instance( )->/hec1/if_config_sw_helper~get_tier_list(
*                                                                                iv_apm           =
                                                                                iv_solution_guid = lr_tier->hec_node_solution
                                                                                iv_hec_node_tier = lr_tier->hec_node_tier
                                                                                iv_hec_phase_guid = lr_tier->hec_phase_guid
                                                                              ).
                IF lines( lt_tier_list ) = 1.
                  lr_tier->hec_tier_reference = lt_tier_list[ 1 ]-hec_node_tier.
                  lv_data_changed = abap_true.
                ENDIF.
              ELSE.
                "clear value in case checkbox was unchecked
                IF lr_tier->hec_tier_reference IS NOT INITIAL.
                  CLEAR lr_tier->hec_tier_reference.
                  lv_data_changed = abap_true.
                ENDIF.
              ENDIF.

              "-----------------------------------
              " Modify tier
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_tier->key
                                   is_data = lr_tier ).
              ENDIF.

              CLEAR: lv_data_changed,
                     lv_inst_status,
                     lv_tier_description,
                     lv_datacenter_descr,
                     lv_attr_name,
                     lt_app_server_lines,
                     lt_app_server_lines_optional,
                     lt_db_server_lines,
                     lt_db_server_lines_optional.

              UNASSIGN: <fs_act_param>,
                        <fs_tier_before>.
            ENDLOOP. " LOOP AT lt_tier REFERENCE INTO lr_tier.

            "-----------------------------------
            " Set create DB/App server instance
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              CLEAR me->mr_act_param.
              me->mr_act_param = NEW /hec1/t_act_create_serv_inst( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_serv_inst )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                  ).

            ENDIF.

            "-----------------------------------
            " Set Update Phasing
            " action to general
            "-----------------------------------
            IF lt_act_param_phasing IS NOT INITIAL.
              CLEAR me->mr_act_param_phasing.
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


  METHOD determine_tier_add_storage_cr.

*    DATA: lt_tier_add_storage        TYPE /hec1/t_tier_add_storage_ct,
*          lt_tier_add_storage_before TYPE /hec1/t_tier_add_storage_ct,
*          lt_tier                    TYPE /hec1/t_data_tier_ct,
*          lt_root_key                TYPE /bobf/t_frw_key,
*          lt_landscape_key           TYPE /bobf/t_frw_key,
*          lt_add_storage             TYPE /hec1/t_data_add_storage_ct,
*          lt_phase                   TYPE /hec1/t_data_phase_ct,
*          lt_act_param_phasing       TYPE TABLE OF /hec1/s_act_phase_inherit.
*
*
*
*    CLEAR: eo_message,
*           et_failed_key.
*
*    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
*                                 it_key  = it_key
*                       IMPORTING et_data = lt_tier_add_storage ).
*
*    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
*                                                        it_key           = it_key
*                                                        io_read          = io_read
*                                              IMPORTING ev_root_key      = DATA(lv_root_key)
*                                                        er_landscape     = DATA(lr_landscape)
*                                                        er_delivery_unit = DATA(lr_delivery_unit) ).
*
*    TRY.
*        CASE is_ctx-det_key.
*            " ***************************************************************************
*            " Create mode
*            " ***************************************************************************
*          WHEN /hec1/if_configuration_c=>sc_determination-tier_add_storage-create.
*
*            " Get tier node (parent)
*            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
*                                                        it_key         = it_key
*                                                        iv_fill_data   = abap_true
*                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier_add_storage-to_parent
*                                              IMPORTING et_data        = lt_tier                                                        ).
*
*            LOOP AT lt_tier_add_storage REFERENCE INTO DATA(lr_tier_add_storage).
*              ASSIGN lt_tier[ key = lr_tier_add_storage->parent_key ] TO FIELD-SYMBOL(<fs_tier>).
*
*              lr_tier_add_storage->hec_delete_visible = abap_true.
*
*              IF ( <fs_tier>                          IS ASSIGNED )    AND
*                 ( <fs_tier>-hec_tier_descr           IS NOT INITIAL ) AND
*                 ( <fs_tier>-hec_tier_type_value      IS NOT INITIAL ) AND
*                 ( <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL ).
*                DATA(lv_release) = abap_true.
*              ENDIF.
*
*              "-----------------------------------
*              " Release instance for selection
*              "-----------------------------------
*              IF ( lv_release <> lr_tier_add_storage->hec_row_selectable ).
*                lr_tier_add_storage->hec_row_selectable = lv_release.
*                DATA(lv_data_changed) = abap_true.
*              ENDIF.
*
*              "------------------------------------------
*              " Set CR related fields from the ROOT node
*              "------------------------------------------
*              DATA(lv_cr_data_changed) = /hec1/cl_config_helper=>set_cr_fields_from_root(
*                EXPORTING
*                  is_ctx       = is_ctx
*                  it_key       = it_key
*                  io_read      = io_read
*                  io_modify    = io_modify
*                  iv_mod_type  = /hec1/if_config_constants=>gc_comp_mod_type-added
*                  is_node_data = lr_tier_add_storage
*              ).
*
*
*              IF ( lv_data_changed = abap_true ).
*                io_modify->update( iv_node = is_ctx-node_key
*                                   iv_key  = lr_tier_add_storage->key
*                                   is_data = lr_tier_add_storage      ).
*              ENDIF.
*
*              UNASSIGN <fs_tier>.
*              CLEAR: lv_data_changed,
*                     lv_release.
*            ENDLOOP.
*
*            " ***************************************************************************
*            " Update mode
*            " ***************************************************************************
*          WHEN /hec1/if_configuration_c=>sc_determination-tier_add_storage-update.
*
*            " Data before update
*            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
*                                         it_key          = it_key
*                                         iv_before_image = abap_true
*                               IMPORTING et_data         = lt_tier_add_storage_before ).
*            " ROOT -> PHASE
*            io_read->retrieve_by_association( EXPORTING iv_node         = /hec1/if_configuration_c=>sc_node-root
*                                                        it_key          = VALUE #( ( key = lv_root_key ) )
*                                                        iv_fill_data    = abap_true
*                                                        iv_association  = /hec1/if_configuration_c=>sc_association-root-phase
*                                              IMPORTING et_data         = lt_phase ).
*
*
*            LOOP AT lt_tier_add_storage REFERENCE INTO lr_tier_add_storage.
*
*              ASSIGN lt_tier_add_storage_before[ key = lr_tier_add_storage->key ] TO FIELD-SYMBOL(<fs_add_storage_before>).
*              IF ( <fs_add_storage_before> IS ASSIGNED ).
*
*                "-----------------------------------
*                " Tier Add Storage Class GUID has changed ?
*                "-----------------------------------
*                IF ( lr_tier_add_storage->hec_tadd_storage_ref_guid IS NOT INITIAL ) AND
*                 ( ( lr_tier_add_storage->hec_tadd_storage_ref_guid <> <fs_add_storage_before>-hec_tadd_storage_ref_guid ) OR
*                   ( lr_tier_add_storage->hec_tadd_storage_ref_descr_ext <> <fs_add_storage_before>-hec_tadd_storage_ref_descr_ext ) ).
*
*                  " Get performance class data from corresponding additional storage
*                  IF ( lt_root_key IS INITIAL ).
*                    " Get root key
*                    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
*                                                                it_key         = it_key
*                                                                iv_fill_data   = abap_false
*                                                                iv_association = /hec1/if_configuration_c=>sc_association-tier_add_storage-to_root
*                                                      IMPORTING et_target_key  = lt_root_key                                                  ).
*
*                    " Get additional storage
*                    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
*                                                                it_key         = lt_root_key
*                                                                iv_fill_data   = abap_true
*                                                                iv_association = /hec1/if_configuration_c=>sc_association-root-add_storage
*                                                      IMPORTING et_data        = lt_add_storage                                                ).
*
*                  ENDIF.
*
*                  ASSIGN lt_add_storage[ hec_node_add_storage_guid = lr_tier_add_storage->hec_tadd_storage_ref_guid ] TO FIELD-SYMBOL(<fs_add_storage>).
*                  IF ( <fs_add_storage> IS ASSIGNED ).
*                    lr_tier_add_storage->* = VALUE #( BASE lr_tier_add_storage->*
*                                                      hec_tadd_storage_ref_descr     = <fs_add_storage>-hec_astore_class_descr
*                                                      hec_tadd_storage_ref_descr_ext = <fs_add_storage>-hec_astore_class_descr_ext
*                                                      hec_tree_descr                 = COND #( WHEN <fs_add_storage>-hec_astore_class_descr_ext IS INITIAL
*                                                                                               THEN <fs_add_storage>-hec_astore_class_descr
*                                                                                               ELSE |{ <fs_add_storage>-hec_astore_class_descr } : { <fs_add_storage>-hec_astore_class_descr_ext }| ) ).
*
*                    lv_data_changed = abap_true.
*                  ENDIF.
*                ENDIF.
*
*                "-----------------------------------
*                " Phasing has changed
*                "-----------------------------------
*                IF ( lr_tier_add_storage->hec_phase_guid NE <fs_add_storage_before>-hec_phase_guid ).
*
*                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
*                                  hec_bopf_key       = lr_tier_add_storage->key
*                                  hec_phase_guid_new = lr_tier_add_storage->hec_phase_guid
*                                  hec_phase_guid_old = <fs_add_storage_before>-hec_phase_guid ) TO lt_act_param_phasing.
*
*                  lr_tier_add_storage->hec_phase_changed = abap_true.
*                  lv_data_changed = abap_true.
*
*                ENDIF. "phasing changed
*              ENDIF. " IF <fs_add_storage_before> IS ASSIGNED.
*
*              "-----------------------------------
*              " Release instance for selection
*              "-----------------------------------
*              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_tier_add_storage->hec_tadd_storage_ref_guid IS NOT INITIAL AND
*                                                                             lr_tier_add_storage->hec_phase_guid            IS NOT INITIAL
*                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
*                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).
*
*              IF ( lv_inst_status <> lr_tier_add_storage->hec_instance_status ).
*                lr_tier_add_storage->hec_instance_status = lv_inst_status.
*                lv_data_changed = abap_true.
*              ENDIF.
*
*              IF ( lv_data_changed = abap_true ).
*                io_modify->update( iv_node = is_ctx-node_key
*                                   iv_key  = lr_tier_add_storage->key
*                                   is_data = lr_tier_add_storage      ).
*              ENDIF.
*
*              CLEAR: lv_inst_status,
*                     lv_data_changed.
*
*              UNASSIGN: <fs_add_storage_before>,
*                        <fs_add_storage>.
*            ENDLOOP.
*
*            "-----------------------------------
*            " Update Phasing
*            "-----------------------------------
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
*            " **********************************
*            " Update mode after tier update
*            " **********************************
*          WHEN /hec1/if_configuration_c=>sc_determination-tier_longterm_backup-update_after_tier.
*
*            " Get tier
*            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
*                                                        it_key         = it_key
*                                                        iv_fill_data   = abap_true
*                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier_longterm_backup-to_parent
*                                              IMPORTING et_data        = lt_tier                                                        ).
*
*
*            LOOP AT lt_tier_add_storage REFERENCE INTO lr_tier_add_storage.
*
*              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_tier_add_storage->hec_tadd_storage_ref_guid IS NOT INITIAL AND
*                                                                       lr_tier_add_storage->hec_phase_guid            IS NOT INITIAL
*                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
*                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).
*
*              " Check instance status and switch
*              IF ( lv_inst_status <> lr_tier_add_storage->hec_instance_status ).
*                lr_tier_add_storage->hec_instance_status = lv_inst_status.
*                lv_data_changed = abap_true.
*              ENDIF.
*
*
*              ASSIGN lt_tier[ key = lr_tier_add_storage->parent_key ] TO <fs_tier>.
*
*              IF ( <fs_tier> IS ASSIGNED ).
*                IF <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
*                   <fs_tier>-hec_tier_type_value      IS NOT INITIAL AND
*                   <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL.
*                  lv_release = abap_true.
*                ENDIF.
*              ENDIF.
*
*              " Release instance for selection
*              IF ( lv_release <> lr_tier_add_storage->hec_row_selectable ).
*                lr_tier_add_storage->hec_row_selectable = lv_release.
*                lv_data_changed = abap_true.
*              ENDIF.
*
*              IF ( lv_data_changed = abap_true ).
*                io_modify->update( iv_node = is_ctx-node_key
*                                   iv_key  = lr_tier_add_storage->key
*                                   is_data = lr_tier_add_storage      ).
*              ENDIF.
*
*              UNASSIGN <fs_tier>.
*              CLEAR: lv_release,
*                     lv_data_changed.
*            ENDLOOP.
*        ENDCASE.
*
*
*      CATCH /bobf/cx_frw. " Exception class
*    ENDTRY.


  ENDMETHOD.


  METHOD determine_tier_add_service_cr.

    DATA: lt_add_service        TYPE /hec1/t_data_tier_add_serv_ct,
          lt_add_service_before TYPE /hec1/t_data_tier_add_serv_ct,
          lt_tier               TYPE /hec1/t_data_tier_ct,
          lt_root_key           TYPE /bobf/t_frw_key,
          lt_landscape_key      TYPE /bobf/t_frw_key,
          lt_add_serv           TYPE /hec1/t_data_add_services_ct,
          lt_phase              TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing  TYPE TABLE OF /hec1/s_act_phase_inherit.



    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_add_service ).

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
          WHEN /hec1/if_configuration_c=>sc_determination-tier_add_service-create.

            " Get tier node (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier_add_service-to_parent
                                              IMPORTING et_data        = lt_tier ).

            LOOP AT lt_add_service REFERENCE INTO DATA(lr_add_service).
              ASSIGN lt_tier[ key = lr_add_service->parent_key ] TO FIELD-SYMBOL(<fs_tier>).

              lr_add_service->hec_delete_visible = abap_true.

              IF <fs_tier> IS ASSIGNED.
                IF <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                   <fs_tier>-hec_tier_type_value      IS NOT INITIAL AND
                   <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              IF lv_release <> lr_add_service->hec_row_selectable.
                lr_add_service->hec_row_selectable = lv_release.
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
                  is_node_data = lr_add_service
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              IF lv_data_changed = abap_false.
                lv_data_changed = lv_cr_data_changed.
              ENDIF.


              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_add_service->key
                                   is_data = lr_add_service ).
              ENDIF.

              UNASSIGN <fs_tier>.
              CLEAR: lv_data_changed,
                     lv_release.
            ENDLOOP.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier_add_service-update.

            " Data before update
            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_add_service_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).


            LOOP AT lt_add_service REFERENCE INTO lr_add_service.

              ASSIGN lt_add_service_before[ key = lr_add_service->key ] TO FIELD-SYMBOL(<fs_add_serv_before>).
              IF <fs_add_serv_before> IS ASSIGNED.
                IF ( <fs_add_serv_before>-hec_tas_service_ref_guid IS NOT INITIAL AND  lr_add_service->hec_tas_service_ref_guid IS INITIAL ).
                  IF <fs_add_serv_before>-hec_tas_service_ref_descr = lr_add_service->hec_tas_service_ref_descr_ext.
                    CLEAR lr_add_service->hec_tas_service_ref_descr_ext.
                  ENDIF.
                  lr_add_service->hec_tree_descr    =    COND #( WHEN lr_add_service->hec_tas_service_ref_descr_ext IS INITIAL
                                                                                           THEN ''
                                                                                           ELSE | : { lr_add_service->hec_tas_service_ref_descr_ext }| ) .

                  lv_data_changed = abap_true.
                ENDIF.
                "-----------------------------------
                " Service Class GUID has changed
                "-----------------------------------
                IF lr_add_service->hec_tas_service_ref_guid IS NOT INITIAL                                                 AND
                 ( lr_add_service->hec_tas_service_ref_guid      <> <fs_add_serv_before>-hec_tas_service_ref_guid      OR
                   lr_add_service->hec_tas_service_ref_descr_ext <> <fs_add_serv_before>-hec_tas_service_ref_descr_ext    ).
                  " Get service class data from corresponding additional service
                  IF lt_root_key IS INITIAL.
                    " Get root key
                    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                                it_key         = it_key
                                                                iv_fill_data   = abap_false
                                                                iv_association = /hec1/if_configuration_c=>sc_association-tier_add_service-to_root
                                                      IMPORTING et_target_key  = lt_root_key ).

                    " Get additional service
                    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                                it_key         = lt_root_key
                                                                iv_fill_data   = abap_true
                                                                iv_association = /hec1/if_configuration_c=>sc_association-root-add_service
                                                      IMPORTING et_data        = lt_add_serv ).

                  ENDIF.

                  ASSIGN lt_add_serv[ hec_node_service = lr_add_service->hec_tas_service_ref_guid ] TO FIELD-SYMBOL(<fs_service>).
                  IF <fs_service> IS ASSIGNED.
                    IF lr_add_service->hec_tas_service_ref_descr_ext IS INITIAL.
                      lr_add_service->hec_tas_service_ref_descr_ext = <fs_service>-hec_as_class_descr_ext.
                    ENDIF.
                    lr_add_service->* = VALUE #( BASE lr_add_service->*
                                                 hec_tas_service_ref_descr = <fs_service>-hec_as_class_descr
                                                 hec_tas_tier_uplift_perc  = <fs_service>-hec_as_tier_uplift_perc
                                                 hec_tree_descr            = COND #( WHEN lr_add_service->hec_tas_service_ref_descr_ext IS INITIAL
                                                                                     THEN <fs_service>-hec_as_class_descr
                                                                                     ELSE |{ <fs_service>-hec_as_class_descr } : { lr_add_service->hec_tas_service_ref_descr_ext }| ) ).

                    lv_data_changed = abap_true.
                  ENDIF.
                ENDIF. " IF lr_service->hec_tas_service_ref_guid IS NOT INITIAL.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_add_service->hec_phase_guid NE <fs_add_serv_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_add_service->key
                                  hec_phase_guid_new = lr_add_service->hec_phase_guid
                                  hec_phase_guid_old = <fs_add_serv_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_add_service->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "phasing changed
              ENDIF. " IF <fs_add_serv_before> IS ASSIGNED.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_add_service->hec_tas_service_ref_guid IS NOT INITIAL AND
                                                                             lr_add_service->hec_phase_guid           IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_add_service->hec_instance_status.
                lr_add_service->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_add_service->key
                                   is_data = lr_add_service ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN: <fs_add_serv_before>.
*                        <fs_service>.
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

            " **********************************
            " Update mode after tier update
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-tier_add_service-update_after_tier.

            " Get tier
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-tier_add_service-to_parent
                                              IMPORTING et_data        = lt_tier ).


            LOOP AT lt_add_service REFERENCE INTO lr_add_service.

              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_add_service->hec_tas_service_ref_guid IS NOT INITIAL AND
                                                                       lr_add_service->hec_phase_guid           IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              " Check instance status and switch
              IF lv_inst_status <> lr_add_service->hec_instance_status.
                lr_add_service->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.


              ASSIGN lt_tier[ key = lr_add_service->parent_key ] TO <fs_tier>.

              IF <fs_tier> IS ASSIGNED.
                IF <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                   <fs_tier>-hec_tier_type_value      IS NOT INITIAL AND
                   <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL.
                  lv_release = abap_true.
                ENDIF.
              ENDIF.

              " Release instance for selection
              IF lv_release <> lr_add_service->hec_row_selectable.
                lr_add_service->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_add_service->key
                                   is_data = lr_add_service ).
              ENDIF.

              UNASSIGN <fs_tier>.
              CLEAR: lv_release,
                     lv_data_changed.
            ENDLOOP.
        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD determine_sw_item_cr.

    DATA: lt_material          TYPE /hec1/t_data_material_ct,
          lt_sw_item           TYPE /hec1/t_data_sw_item_ct,
          lt_sw_item_before    TYPE /hec1/t_data_sw_item_ct,
          lt_phase             TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key                                                                "
                       IMPORTING et_data = lt_sw_item ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create and update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-software_item-create                OR
               /hec1/if_configuration_c=>sc_determination-software_item-update                OR
               /hec1/if_configuration_c=>sc_determination-software_item-update_after_material.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true                                                                "
                               IMPORTING et_data         = lt_sw_item_before ).

            " Get material
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-software_item-to_parent
                                              IMPORTING et_data        = lt_material ).


            LOOP AT lt_sw_item REFERENCE INTO DATA(lr_sw_item).

              lr_sw_item->hec_tree_descr = lr_sw_item->hec_sw_item_hsp_name.

              ASSIGN lt_sw_item_before[ key = lr_sw_item->key ] TO FIELD-SYMBOL(<fs_sw_item_before>).
              IF <fs_sw_item_before> IS ASSIGNED.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_sw_item->hec_phase_guid NE <fs_sw_item_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_sw_item->key
                                  hec_phase_guid_new = lr_sw_item->hec_phase_guid
                                  hec_phase_guid_old = <fs_sw_item_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_sw_item->hec_phase_changed = abap_true.
                  DATA(lv_data_changed) = abap_true.

                ENDIF. "phasing changed
              ENDIF. "<fs_sw_item_before> is assigned.

              "-----------------------------------
              " Check and switch instance status
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_sw_item->hec_phase_guid IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              lr_sw_item->hec_delete_visible = abap_false.

              IF lv_inst_status <> lr_sw_item->hec_instance_status.
                lr_sw_item->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "------------------------------------------
              " Set CR related fields from the ROOT node
              "------------------------------------------
              IF ( is_ctx-det_key = /hec1/if_configuration_c=>sc_determination-software_item-create ).
                DATA(lv_cr_data_changed) = /hec1/cl_config_helper=>SET_CR_RELATED_FIELDS(
                  EXPORTING
                    is_ctx       = is_ctx
                    it_key       = it_key
                    io_read      = io_read
                    io_modify    = io_modify
                    iv_mod_type  = /hec1/if_config_constants=>gc_comp_mod_type-added
                    is_node_data = lr_sw_item
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
                ).
              ENDIF.

              " Release instance for selection
              ASSIGN lt_material[ key = lr_sw_item->parent_key ] TO FIELD-SYMBOL(<fs_material>).

              IF <fs_material> IS ASSIGNED.
                IF <fs_material>-hec_row_selectable <> lr_sw_item->hec_row_selectable.
                  lr_sw_item->hec_row_selectable = <fs_material>-hec_row_selectable.
                  lv_data_changed = abap_true.
                ENDIF.
              ENDIF.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_sw_item->key
                                   is_data = lr_sw_item ).
              ENDIF.

              UNASSIGN <fs_material>.
              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP. " LOOP AT lt_sw_item REFERENCE INTO ls_sw_item.

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

        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_solution_cr.

    DATA: lt_solution         TYPE /hec1/t_data_solution_ct,
          lt_solution_before  TYPE /hec1/t_data_solution_ct,
          lt_act_param        TYPE /hec1/t_act_create_tier,
          ls_act_param        LIKE LINE OF lt_act_param,
          lt_act_param_tier   TYPE /hec1/t_act_update_tier,
          ls_landscape        TYPE /hec1/s_config_root_cs,
          lt_tier             TYPE /hec1/t_data_tier_ct,
          lt_act_param_delete TYPE /bobf/t_frw_node.

    CLEAR: eo_message,
           et_failed_key.

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit) ).

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_solution ).

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
          WHEN /hec1/if_configuration_c=>sc_determination-solution-create.

            LOOP AT lt_solution REFERENCE INTO DATA(lr_solution).

              lr_solution->hec_delete_visible = abap_true.
              lr_solution->hec_delete_visible = abap_true.
              lr_solution->hec_row_selectable = abap_true.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_solution->hec_solution_guid IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_solution->hec_instance_status.
                lr_solution->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Set APM model
              "-----------------------------------
              IF lr_solution->hec_apm_guid  IS INITIAL.
                lr_solution->hec_apm_guid  = ls_landscape-hec_apm_guid.
                lr_solution->hec_apm_descr = ls_landscape-hec_apm_descr.

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
                  is_node_data = lr_solution
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              IF lv_data_changed = abap_false.
                lv_data_changed = lv_cr_data_changed.
              ENDIF.

              "-----------------------------------
              " Modify solution
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_solution->key
                                   is_data = lr_solution ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-solution-update.

            " Data before update
            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_solution_before ).

            " Get tier
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                                        iv_fill_data   = abap_true
                                              IMPORTING et_data        = lt_tier ).


            LOOP AT lt_solution REFERENCE INTO lr_solution.
              ASSIGN lt_solution_before[ key = lr_solution->key ] TO FIELD-SYMBOL(<fs_sol_before>).

              IF <fs_sol_before> IS ASSIGNED.
                "-----------------------------------
                " Set Solution
                "-----------------------------------
                IF lr_solution->hec_solution_guid    IS NOT INITIAL                     AND
                   lr_solution->hec_solution_guid <> <fs_sol_before>-hec_solution_guid.

                  " Get Solution
                  SELECT SINGLE *
                    FROM /hec1/i_solutionbasic
                   WHERE hec_apm_guid      = @lr_landscape->hec_apm_guid     AND
                         hec_solution_guid = @lr_solution->hec_solution_guid
                    INTO CORRESPONDING FIELDS OF @lr_solution->*.

                  IF lr_solution->hec_initial_support_stat_value IS INITIAL.
                    lr_solution->hec_initial_support_stat_value = lr_solution->hec_support_stat_value.
                    lr_solution->hec_initial_support_stat_descr = lr_solution->hec_support_stat_descr.
                  ENDIF.

                  " Set solution material
                  /hec1/cl_config_sw_helper=>get_instance( )->/hec1/if_config_sw_helper~set_material_list( iv_apm_guid      = lr_landscape->hec_apm_guid
                                                                                                           iv_solution_guid = lr_solution->hec_solution_guid
                                                                                                           iv_node_solution = lr_solution->hec_node_solution ).

                  " Set Software Item ( included item stack )
                  /hec1/cl_config_sw_helper=>get_instance( )->/hec1/if_config_sw_helper~set_software_item_list( iv_apm_guid      = lr_landscape->hec_apm_guid
                                                                                                                iv_solution_guid = lr_solution->hec_solution_guid
                                                                                                                iv_node_solution = lr_solution->hec_node_solution ).
                ENDIF. " IF lr_solution->hec_solution_guid IS NOT INITIAL AND...


                "-----------------------------------
                " Set solution description
                "-----------------------------------
                IF lr_solution->hec_solution_guid IS NOT INITIAL.

                  SELECT SINGLE hec_sol_alias_descr
                    FROM /hec1/i_solutionbasic
                   WHERE hec_apm_guid      = @lr_landscape->hec_apm_guid     AND
                         hec_solution_guid = @lr_solution->hec_solution_guid
                    INTO @lr_solution->hec_sol_alias_descr.

                  IF lr_solution->hec_sol_alias_descr_ext IS INITIAL.
                    lr_solution->hec_sol_alias_descr_ext = lr_solution->hec_sol_alias_descr.
                  ENDIF.

                  lr_solution->hec_tree_descr = | { lr_solution->hec_sol_alias_descr  } : { lr_solution->hec_sol_alias_descr_ext } |. "#EC CI_FLDEXT_OK[2215424]
                  lv_data_changed             = abap_true.
                ENDIF. " IF lr_solution->hec_solution_guid IS NOT INITIAL.


                "-----------------------------------
                " New tiers are added
                "-----------------------------------
                IF <fs_sol_before>-hec_tier_qty_nprod_level <> lr_solution->hec_tier_qty_nprod_level OR
                   <fs_sol_before>-hec_tier_qty_prod_level  <> lr_solution->hec_tier_qty_prod_level.

                  " The number of tiers need to be checked as well. If a node is deleted the amount of tiers on solution level need to be adjusted
                  DATA(lt_tier_prod) = VALUE /hec1/t_data_tier_ct( FOR tier IN lt_tier
                                                                   WHERE ( parent_key = lr_solution->key AND
                                                                           hec_tier_cat_value = /hec1/if_config_constants=>gc_tier_category-prod )
                                                                   ( tier ) ).

                  DATA(lt_tier_nonprod) = VALUE /hec1/t_data_tier_ct( FOR tier IN lt_tier
                                                                      WHERE ( parent_key = lr_solution->key AND
                                                                              hec_tier_cat_value = /hec1/if_config_constants=>gc_tier_category-nonprod )
                                                                      ( tier ) ).

                  "-----------------------------------
                  " Non production tier
                  "-----------------------------------
                  IF lr_solution->hec_tier_qty_nprod_level > <fs_sol_before>-hec_tier_qty_nprod_level.
                    ls_act_param = VALUE #( key             = lr_solution->key
                                            hec_tier_qty_nprod_level = lr_solution->hec_tier_qty_nprod_level - <fs_sol_before>-hec_tier_qty_nprod_level ).

                    " Success message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_non_prod_tier_added
                                                                   iv_severity = /bobf/cm_frw=>co_severity_success
                                                                   iv_attr1    = CONV #( ls_act_param-hec_tier_qty_nprod_level )
                                                         CHANGING  co_message  = eo_message ).

                  ELSEIF lr_solution->hec_tier_qty_nprod_level < <fs_sol_before>-hec_tier_qty_nprod_level
                    AND lr_solution->hec_tier_qty_nprod_level < lines( lt_tier_nonprod ).
                    DATA(lv_attr_name) = /hec1/if_configuration_c=>sc_node_attribute-solution-hec_tier_qty_nprod_level.

                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_solution->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_solution->hec_tier_qty_nprod_level = <fs_sol_before>-hec_tier_qty_nprod_level.
                    lv_data_changed = abap_true.

                  ELSEIF <fs_sol_before>-hec_tier_qty_nprod_level > lines( lt_tier_nonprod ).
                    lv_data_changed = abap_true.

                  ENDIF. " IF lr_solution->hec_tier_qty_nprod_level > <fs_sol_before>-hec_tier_qty_nprod_level.

                  "-----------------------------------
                  " Production tier
                  "-----------------------------------
                  IF lr_solution->hec_tier_qty_prod_level > <fs_sol_before>-hec_tier_qty_prod_level.
                    ls_act_param-key             = lr_solution->key.
                    ls_act_param-hec_tier_qty_prod_level = lr_solution->hec_tier_qty_prod_level - <fs_sol_before>-hec_tier_qty_prod_level.

                    " Success message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = /hec1/cx_bopf_config=>new_prod_tier_added
                                                                   iv_severity = /bobf/cm_frw=>co_severity_success
                                                                   iv_attr1    = CONV #( ls_act_param-hec_tier_qty_prod_level )
                                                         CHANGING  co_message  = eo_message ).


                  ELSEIF lr_solution->hec_tier_qty_prod_level < <fs_sol_before>-hec_tier_qty_prod_level
                    AND lr_solution->hec_tier_qty_prod_level < lines( lt_tier_prod ).
                    CLEAR lv_attr_name.
                    lv_attr_name = /hec1/if_configuration_c=>sc_node_attribute-solution-hec_tier_qty_prod_level.
                    " Error message
                    /hec1/cl_config_helper=>set_message( EXPORTING iv_textid          = /hec1/cx_bopf_config=>object_no_not_higher
                                                                   is_origin_location = VALUE #( node_key = is_ctx-node_key
                                                                                                 key      = lr_solution->key
                                                                                                 attributes = VALUE #( ( lv_attr_name ) ) )
                                                         CHANGING  co_message         = eo_message ).

                    " Set node number to value before update
                    lr_solution->hec_tier_qty_prod_level = <fs_sol_before>-hec_tier_qty_prod_level.
                    lv_data_changed = abap_true.

                  ELSEIF <fs_sol_before>-hec_tier_qty_prod_level > lines( lt_tier_prod ).
                    lv_data_changed = abap_true.

                  ENDIF. " IF lr_solution->hec_tier_qty_nprod_level > <fs_sol_before>-hec_tier_qty_nprod_level.

                  IF ls_act_param IS NOT INITIAL.
                    INSERT ls_act_param INTO TABLE lt_act_param.
                    CLEAR ls_act_param.
                  ENDIF.

                ENDIF. " IF <fs_sol_before>-hec_tier_qty_nprod_level <> lr_solution->hec_tier_qty_nprod_level OR...

                "-----------------------------------
                " Reset fields
                "-----------------------------------
                IF lr_solution->hec_solution_guid    IS     INITIAL AND
                   <fs_sol_before>-hec_solution_guid IS NOT INITIAL.

                  "Reset all other fields besides the following:
                  lr_solution->content = VALUE #( LET old = lr_solution->* IN
                                                 hec_apm_guid  = old-hec_apm_guid
                                                 hec_apm_descr = old-hec_apm_descr
                                                 technical     = old-technical
                                                 cdd           = old-cdd
                                                 status        = old-status
                                                 descr         = old-descr
                                                 fpm           = old-fpm
                                                 admin_data    = old-admin_data    ).

                  " reset software lists
                  " Reset solution material for solution
                  /hec1/cl_config_sw_helper=>get_instance( )->/hec1/if_config_sw_helper~delete_solution_list( lr_solution->hec_node_solution ).

                  " Add tiers to delete table
                  LOOP AT lt_tier ASSIGNING FIELD-SYMBOL(<fs_tier>)
                    WHERE parent_key = lr_solution->key.

                    INSERT VALUE #( node = /hec1/if_configuration_c=>sc_node-tier
                                    key  = <fs_tier>-key                           ) INTO TABLE lt_act_param_delete.
                  ENDLOOP.

                  lv_data_changed = abap_true.

                ENDIF. " IF is_solution-hec_solution_guid    IS INITIAL     AND

                "-----------------------------------
                " Update Language to Tier
                "-----------------------------------
                IF <fs_sol_before>-hec_sol_language_sys_alt NE lr_solution->hec_sol_language_sys_alt
                  OR <fs_sol_before>-hec_sol_language_sys_def NE lr_solution->hec_sol_language_sys_def
                  OR <fs_sol_before>-hec_sol_language_list NE lr_solution->hec_sol_language_list.

                  LOOP AT lt_tier ASSIGNING <fs_tier>
                    WHERE parent_key = lr_solution->key.

                    " every key in the parameter table should only exist once.
                    ASSIGN lt_act_param_tier[ key        = <fs_tier>-key
                                              parent_key = <fs_tier>-parent_key ] TO FIELD-SYMBOL(<fs_act_param_tier>).

                    IF <fs_act_param_tier> IS ASSIGNED.
                      <fs_act_param_tier>-do_update_language = abap_true.
                    ELSE.
                      INSERT VALUE #( key                = <fs_tier>-key
                                      parent_key         = <fs_tier>-parent_key
                                      do_update_language = abap_true ) INTO TABLE lt_act_param_tier.
                    ENDIF.

                  ENDLOOP. "lt_tier
                ENDIF. "language changed

                "-----------------------------------
                " Update Business Function
                " Activation to Tier
                "-----------------------------------
                IF <fs_sol_before>-hec_bf_activation NE lr_solution->hec_bf_activation.
                  LOOP AT lt_tier ASSIGNING <fs_tier>
                    WHERE parent_key = lr_solution->key.

                    " every key in the parameter table should only exist once.
                    ASSIGN lt_act_param_tier[ key        = <fs_tier>-key
                                              parent_key = <fs_tier>-parent_key ] TO <fs_act_param_tier>.

                    IF <fs_act_param_tier> IS ASSIGNED.
                      <fs_act_param_tier>-do_update_bf_activation = abap_true.
                    ELSE.
                      INSERT VALUE #( key                     = <fs_tier>-key
                                      parent_key              = <fs_tier>-parent_key
                                      do_update_bf_activation = abap_true ) INTO TABLE lt_act_param_tier.
                    ENDIF.

                  ENDLOOP. "lt_tier
                ENDIF. "IF <fs_sol_before>-hec_bf_activation NE lr_solution->hec_bf_activation.

                "-----------------------------------
                " Update BP Activation: Template
                " sent to customer to Tier
                "-----------------------------------
                IF <fs_sol_before>-hec_bpacti_tmpl_sent_to_cust NE lr_solution->hec_bpacti_tmpl_sent_to_cust.
                  LOOP AT lt_tier ASSIGNING <fs_tier>
                    WHERE parent_key = lr_solution->key.

                    " every key in the parameter table should only exist once.
                    ASSIGN lt_act_param_tier[ key        = <fs_tier>-key
                                              parent_key = <fs_tier>-parent_key ] TO <fs_act_param_tier>.

                    IF <fs_act_param_tier> IS ASSIGNED.
                      <fs_act_param_tier>-do_update_bf_tmpl_sent_to_cust = abap_true.
                    ELSE.
                      INSERT VALUE #( key                            = <fs_tier>-key
                                      parent_key                     = <fs_tier>-parent_key
                                      do_update_bf_tmpl_sent_to_cust = abap_true ) INTO TABLE lt_act_param_tier.
                    ENDIF.

                  ENDLOOP. "lt_tier
                ENDIF. "IF <fs_sol_before>-hec_bpacti_tmpl_sent_to_cust NE lr_solution->hec_bpacti_tmpl_sent_to_cust.

                "-----------------------------------
                " Update BP Activation: Template
                " upload to customer to Tier
                "-----------------------------------
                IF <fs_sol_before>-hec_bpacti_tmpl_upl_by_cust NE lr_solution->hec_bpacti_tmpl_upl_by_cust.
                  LOOP AT lt_tier ASSIGNING <fs_tier>
                    WHERE parent_key = lr_solution->key.

                    " every key in the parameter table should only exist once.
                    ASSIGN lt_act_param_tier[ key        = <fs_tier>-key
                                              parent_key = <fs_tier>-parent_key ] TO <fs_act_param_tier>.

                    IF <fs_act_param_tier> IS ASSIGNED.
                      <fs_act_param_tier>-do_update_bf_tmpl_upl_by_cust = abap_true.
                    ELSE.
                      INSERT VALUE #( key                           = <fs_tier>-key
                                      parent_key                    = <fs_tier>-parent_key
                                      do_update_bf_tmpl_upl_by_cust = abap_true ) INTO TABLE lt_act_param_tier.
                    ENDIF.

                  ENDLOOP. "lt_tier
                ENDIF. "IF <fs_sol_before>-hec_bpacti_tmpl_upl_by_cust NE lr_solution->hec_bpacti_tmpl_upl_by_cust.

                "-----------------------------------
                " Update DB Version to Tier
                "-----------------------------------
                IF <fs_sol_before>-hec_sol_db_version_guid NE lr_solution->hec_sol_db_version_guid.

                  LOOP AT lt_tier ASSIGNING <fs_tier>
                    WHERE parent_key = lr_solution->key.

                    " every key in the parameter table should only exist once.
                    ASSIGN lt_act_param_tier[ key        = <fs_tier>-key
                                              parent_key = <fs_tier>-parent_key ] TO <fs_act_param_tier>.

                    IF <fs_act_param_tier> IS ASSIGNED.
                      <fs_act_param_tier>-do_update_db_version = abap_true.
                    ELSE.
                      INSERT VALUE #( key                  = <fs_tier>-key
                                      parent_key           = <fs_tier>-parent_key
                                      do_update_db_version = abap_true ) INTO TABLE lt_act_param_tier.
                    ENDIF.

                  ENDLOOP. "lt_tier
                ENDIF. "language changed

                "-----------------------------------
                " Update Implementation type to Tier
                "-----------------------------------
                IF <fs_sol_before>-hec_sol_impl_type_value NE lr_solution->hec_sol_impl_type_value.

                  LOOP AT lt_tier ASSIGNING <fs_tier>
                    WHERE parent_key = lr_solution->key.

                    " every key in the parameter table should only exist once.
                    ASSIGN lt_act_param_tier[ key        = <fs_tier>-key
                                              parent_key = <fs_tier>-parent_key ] TO <fs_act_param_tier>.

                    IF <fs_act_param_tier> IS ASSIGNED.
                      <fs_act_param_tier>-do_update_impl_type = abap_true.
                    ELSE.
                      INSERT VALUE #( key                = <fs_tier>-key
                                      parent_key         = <fs_tier>-parent_key
                                      do_update_impl_type = abap_true ) INTO TABLE lt_act_param_tier.
                    ENDIF.

                  ENDLOOP. "lt_tier
                ENDIF. "Implementation type changed

              ENDIF. " IF <fs_sol_before> IS ASSIGNED.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_solution->hec_solution_guid IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).


              IF lv_inst_status <> lr_solution->hec_instance_status.
                lr_solution->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify solution
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_solution->key
                                   is_data = lr_solution ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_attr_name,
                     lv_data_changed,
                     lt_tier_nonprod,
                     lt_tier_prod.

              UNASSIGN <fs_sol_before>.
            ENDLOOP. "            LOOP AT lt_solution REFERENCE INTO lr_solution.

            "-----------------------------------
            " Set update tier to GENERAL
            "-----------------------------------
            IF lt_act_param_tier IS NOT INITIAL.
              me->mr_act_param1 = NEW /hec1/t_act_update_tier( lt_act_param_tier ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-tier )
                  it_key          = VALUE #( FOR act_tier IN lt_act_param_tier
                                            ( key = act_tier-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_tier )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = mr_act_param1 ).
            ENDIF.

            "-----------------------------------
            " Set create tier action to GENERAL
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              me->mr_act_param = NEW /hec1/t_act_create_tier( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_db_si IN lt_act_param
                                            ( key = wa_db_si-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_tier )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param                                   ).
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
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD determine_root_cr.

    DATA: lt_root                   TYPE /hec1/t_config_root_ct,
          lt_root_before            TYPE /hec1/t_config_root_ct,
          lt_phase                  TYPE /hec1/t_data_phase_ct,
          lr_default_phase          TYPE REF TO /hec1/s_data_phase_cs,
          lt_modification           TYPE /bobf/t_frw_modification,
          lt_act_param              TYPE TABLE OF /bobf/s_frw_key,
          ls_act_param_tier_inherit TYPE /hec1/s_act_update_tier_inhrit,
          lt_act_param_phase        TYPE /hec1/t_act_update_phase.



    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_root ). "root = landscape


    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-root-create.

            LOOP AT lt_root REFERENCE INTO DATA(lr_root).

              lr_root->hec_node_landscape          = /rbp/cl_general_utilities=>get_new_guid22( ).
              lr_root->hec_landscape_config_status = /hec1/if_status_handler=>gc_landscape_status_values-draft.
              lr_root->hec_cdd_status              = /hec1/if_status_handler=>gc_cdd_status_values-not_requestable.
              lr_root->hec_s2d_status              = /hec1/if_status_handler=>gc_s2d_status_values-not_startable.
              lr_root->hec_fulfillment_status      = /hec1/if_status_handler=>gc_fulfillment_status_values-ls_build_not_startable.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_root->hec_material                IS NOT INITIAL AND
                                                                             lr_root->hec_landscape_descr         IS NOT INITIAL AND
                                                                             lr_root->hec_landscape_config_status IS NOT INITIAL AND
                                                                             lr_root->hec_ls_contract_curr        IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete     ).

              lr_root->hec_delete_visible = abap_false.

              IF lv_inst_status <> lr_root->hec_instance_status.
                lr_root->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_root->key
                                   is_data = lr_root ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

            ENDLOOP.

            "-----------------------------------
            " Set create phase
            " action to general
            "-----------------------------------
            /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                is_ctx          = CORRESPONDING #( is_ctx )
                it_key          = it_key
                iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_phase )
                iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                ).


            "-----------------------------------
            " Set create delivery unit
            " action to general
            "-----------------------------------
            /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                is_ctx          = CORRESPONDING #( is_ctx )
                it_key          = it_key
                iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_delivery_unit )
                iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                ).


            "-----------------------------------
            " Set create managed service baseline
            " action to general
            "-----------------------------------
            /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                is_ctx          = CORRESPONDING #( is_ctx )
                it_key          = it_key
                iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_man_serv_baseline )
                iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation           ).


            "-----------------------------------
            " Create instances
            "-----------------------------------
            IF lt_modification IS NOT INITIAL.
              io_modify->do_modify( lt_modification ).

              io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                                     IMPORTING eo_message             = DATA(lo_message)
                                               eo_change              = DATA(lo_change) ).
            ENDIF.


            " ***************************************************************************
            " update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-root-update.

            " Get before image
            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_root_before ).

            "get the default phase
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).


            LOOP AT lt_root REFERENCE INTO lr_root.
              ASSIGN lt_root_before[ key = lr_root->key ] TO FIELD-SYMBOL(<fs_landscape_before>).

              IF <fs_landscape_before> IS ASSIGNED.
                "-----------------------------------
                " Convert Material to internal
                "-----------------------------------
                CALL FUNCTION 'CONVERSION_EXIT_MATN1_INPUT'
                  EXPORTING
                    input  = lr_root->hec_material
                  IMPORTING
                    output = lr_root->hec_material.

                "-----------------------------------
                " Set APM
                "-----------------------------------
                IF lr_root->hec_apm_guid <> <fs_landscape_before>-hec_apm_guid
               AND lr_root->hec_apm_guid IS NOT INITIAL.

                  SELECT SINGLE *
                    FROM /hec1/a_model
                   WHERE hec_apm_guid = @lr_root->hec_apm_guid
                    INTO CORRESPONDING FIELDS OF @lr_root->*.

                  lv_data_changed = abap_true.

                ENDIF.

                "-----------------------------------
                " Start business rules
                "-----------------------------------
                IF ( lr_root->hec_material <> <fs_landscape_before>-hec_material )
                OR ( lr_root->hec_apm_guid <> <fs_landscape_before>-hec_apm_guid ) .

                  " Get flat material data
                  SELECT SINGLE *
                    FROM /hec1/i_materialbasic
                   WHERE hec_material = @lr_root->hec_material
                    INTO @DATA(ls_material).

                  " Get contract basics
                  SELECT SINGLE *
                    FROM /hec1/i_contractbasic
                   WHERE hec_apm_guid      = @lr_root->hec_apm_guid         AND
                         hec_flat_mat_guid = @ls_material-hec_flat_mat_guid
                    INTO @DATA(ls_contract_basic).

                  lr_root->hec_flat_mat_guid              = ls_material-hec_flat_mat_guid.
                  lr_root->hec_material_opmode_value      = ls_material-hec_mat_oper_mode_value.
                  lr_root->hec_material_opmode_descr      = ls_material-hec_mat_oper_mode_descr.
                  lr_root->hec_material_licmode_value     = ls_material-hec_mat_lice_mode_value.
                  lr_root->hec_material_licmode_descr     = ls_material-hec_mat_lice_mode_descr.
                  lr_root->hec_mat_srvc_mode_value        = ls_material-hec_mat_srvc_mode_value.
                  lr_root->hec_mat_srvc_mode_descr        = ls_material-hec_mat_srvc_mode_descr.
                  lr_root->hec_ls_contract_dur_unit_value = ls_contract_basic-hec_contract_dur_u_value.
                  lr_root->hec_ls_contract_dur_unit_descr = ls_contract_basic-hec_contract_dur_u_descr.
                  lr_root->hec_ls_low_cont_term_limit     = ls_contract_basic-hec_contract_lim_low.
                  lr_root->hec_ls_up_cont_term_limit      = ls_contract_basic-hec_contract_lim_up.
                  lr_root->hec_ls_price_conv_factor       = ls_contract_basic-hec_price_conv_factor.
                  lr_root->hec_ls_uplift_percent          = ls_contract_basic-hec_upflift_percent.

                  lv_data_changed                         = abap_true.

                  "-----------------------------------
                  " Update Access/Delivery Category
                  "-----------------------------------
                  SELECT SINGLE hec_access_dlvy_cat_guid,
                                hec_acccess_dlvy_cat_value,
                                hec_acccess_dlvy_cat_descr
                   FROM /hec1/i_accesdeliverybasic
                   INTO CORRESPONDING FIELDS OF @lr_root->*
                   WHERE hec_apm_guid               = @lr_root->hec_apm_guid      AND
                         hec_flat_mat_guid          = @lr_root->hec_flat_mat_guid AND
                         hec_acc_support_stat_value = '02'.

                  " Set Value List Quantity - Access Delivery Category
                  lr_root->hec_access_dlvy_cat_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_access_delivery_category(
                                                                                                iv_apm_guid            = lr_root->hec_apm_guid
                                                                                                iv_flat_mat_guid       = lr_root->hec_flat_mat_guid ) )
                                                              THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                              ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                  " Set Value List Quantity - Material
                  lr_root->hec_material_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.

                  "-----------------------------------
                  " Fill action table for update
                  " data center
                  "-----------------------------------
                  " - Only after the update can the datacenter type be read from the APM
                  INSERT CORRESPONDING #( lr_root->* ) INTO TABLE lt_act_param.

                ENDIF. " IF lr_root->hec_material <> <fs_landscape_before>-hec_material.

                "-----------------------------------
                " Update Region to Datacenter Level
                "-----------------------------------
                IF lr_root->hec_dlvy_region_l1_guid <> <fs_landscape_before>-hec_dlvy_region_l1_guid OR
                   lr_root->hec_dlvy_region_l2_guid <> <fs_landscape_before>-hec_dlvy_region_l2_guid OR
                   lr_root->hec_country_key         <> <fs_landscape_before>-hec_country_key.

                  " Fill Region L1
                  IF lr_root->hec_dlvy_region_l1_guid <> <fs_landscape_before>-hec_dlvy_region_l1_guid AND
                     lr_root->hec_dlvy_region_l1_guid    IS NOT INITIAL.

                    SELECT SINGLE *
                      FROM /hec1/i_deliveryregionl1basic
                      INTO @DATA(ls_region_l1)
                     WHERE hec_dlvy_region_l1_guid = @lr_root->hec_dlvy_region_l1_guid.

                    lr_root->hec_dlvy_region_l1_descr = ls_region_l1-hec_dlvy_region_l1_descr.
                  ENDIF.

                  " Fill region L2
                  IF lr_root->hec_dlvy_region_l2_guid <> <fs_landscape_before>-hec_dlvy_region_l2_guid AND
                     lr_root->hec_dlvy_region_l2_guid    IS NOT INITIAL.

                    SELECT SINGLE *
                      FROM /hec1/i_deliveryregionl2basic AS l2
                      JOIN /hec1/i_deliveryregionl1basic AS l1
                        ON l2~hec_dlvy_region_l1_guid = l1~hec_dlvy_region_l1_guid
                      INTO @DATA(ls_region_l2)
                     WHERE hec_dlvy_region_l2_guid = @lr_root->hec_dlvy_region_l2_guid.

                    lr_root->hec_dlvy_region_l2_descr = ls_region_l2-l2-hec_dlvy_region_l2_descr.
                    lr_root->hec_dlvy_region_l1_guid  = ls_region_l2-l1-hec_dlvy_region_l1_guid.
                    lr_root->hec_dlvy_region_l1_descr = ls_region_l2-l1-hec_dlvy_region_l1_descr.
                  ENDIF.

                  " Fill region L3 (country)
                  IF lr_root->hec_country_key <> <fs_landscape_before>-hec_country_key AND
                     lr_root->hec_country_key    IS NOT INITIAL.

                    SELECT SINGLE *
                      FROM /hec1/i_deliveryregionl3basic AS l3
                      JOIN /hec1/i_deliveryregionl2basic AS l2
                        ON l3~hec_dlvy_region_l2_guid = l2~hec_dlvy_region_l2_guid
                      JOIN /hec1/i_deliveryregionl1basic AS l1
                        ON l2~hec_dlvy_region_l1_guid = l1~hec_dlvy_region_l1_guid
                      INTO @DATA(ls_region_l3)
                     WHERE l3~hec_country_key = @lr_root->hec_country_key.

                    lr_root->hec_country_descr = ls_region_l3-l3-hec_country_descr.
                    lr_root->hec_dlvy_region_l2_guid  = ls_region_l3-l2-hec_dlvy_region_l2_guid.
                    lr_root->hec_dlvy_region_l2_descr = ls_region_l3-l2-hec_dlvy_region_l2_descr.
                    lr_root->hec_dlvy_region_l1_guid  = ls_region_l3-l1-hec_dlvy_region_l1_guid.
                    lr_root->hec_dlvy_region_l1_descr = ls_region_l3-l1-hec_dlvy_region_l1_descr.
                  ENDIF.

                  " Set Value List Quantity for Regions
                  " !! For now we just set the value to "multi".
                  "   At a later point we might need to restrict the values based on the selected datacenters
                  lr_root->hec_dlvy_region_l1_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.
                  lr_root->hec_dlvy_region_l2_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.
                  lr_root->hec_country_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.

                  "-----------------------------------
                  " Fill action table for update
                  " data center
                  "-----------------------------------
                  INSERT CORRESPONDING #( lr_root->* ) INTO TABLE lt_act_param.

                ENDIF. " IF lr_root->hec_dlvy_region_l1 <> <fs_landscape_before>-hec_dlvy_region_l1 OR

                "-----------------------------------
                " Update Access/Delivery Category
                "-----------------------------------
                IF lr_root->hec_access_dlvy_cat_guid <> <fs_landscape_before>-hec_access_dlvy_cat_guid AND
                   lr_root->hec_access_dlvy_cat_guid    IS NOT INITIAL.

                  SELECT SINGLE *
                    FROM /hec1/i_accesdeliverybasic
                    INTO @DATA(ls_access_delivery)
                    WHERE hec_access_dlvy_cat_guid = @lr_root->hec_access_dlvy_cat_guid.

                  lr_root->hec_acccess_dlvy_cat_descr = ls_access_delivery-hec_acccess_dlvy_cat_descr.
                  lr_root->hec_acccess_dlvy_cat_value = ls_access_delivery-hec_acccess_dlvy_cat_value.
                  lv_data_changed                    = abap_true.

                  lr_root->hec_init_acc_supp_stat_value = ls_access_delivery-hec_acc_support_stat_value.
                  lr_root->hec_init_acc_supp_stat_descr = ls_access_delivery-hec_acc_support_stat_descr.
                  lr_root->hec_acc_support_stat_value   = ls_access_delivery-hec_acc_support_stat_value.
                  lr_root->hec_acc_support_stat_descr   = ls_access_delivery-hec_acc_support_stat_descr.
                ENDIF. " IF lr_root->hec_access_dlvy_cat_guid <> <fs_landscape_before>-hec_access_dlvy_cat_guid AND

                "-----------------------------------
                " Update Currency
                "-----------------------------------
                IF lr_root->hec_ls_contract_curr <> <fs_landscape_before>-hec_ls_contract_curr AND
                   lr_root->hec_ls_contract_curr IS NOT INITIAL.

                  SELECT SINGLE hec_ls_contract_curr, ltext
                    FROM /hec1/i_currency
                   WHERE hec_ls_contract_curr = @lr_root->hec_ls_contract_curr
                    INTO @DATA(ls_currency).

                  lr_root->hec_ls_contract_curr_descr = ls_currency-ltext.

                ENDIF. "contract currency set

                "-----------------------------------
                " Update Start/End date
                "-----------------------------------
                "if we have updates to the Contract Start and End date and if the default phase start and End dates are empty
                " fill the default phase information from Landscape
                IF ( "olds are empty
                    ( <fs_landscape_before>-hec_contract_start_date IS INITIAL AND <fs_landscape_before>-hec_contract_end_date IS INITIAL ) AND
                      " new values
                    (  lr_root->hec_contract_start_date IS NOT INITIAL AND lr_root->hec_contract_end_date IS NOT INITIAL ) ) .

                  TRY.
                      lr_default_phase = NEW #( lt_phase[ hec_default_phase  = abap_true "#EC CI_SORTSEQ
                                                          hec_phase_inactive = abap_false ] ).
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  INSERT VALUE #( key                     = lr_default_phase->key
                                  do_update_def_start_end = abap_true ) INTO TABLE lt_act_param_phase.

                ENDIF.

                "-----------------------------------
                " Change Phasing Duration Unit in all Phases
                "-----------------------------------
                IF lr_root->hec_ls_contract_dur_unit_value NE <fs_landscape_before>-hec_ls_contract_dur_unit_value.

                  LOOP AT lt_phase REFERENCE INTO DATA(lr_phase).

                    INSERT VALUE #( key                     = lr_phase->key
                                    do_update_duration_unit = abap_true ) INTO TABLE lt_act_param_phase.

                  ENDLOOP.
                ENDIF. "contract duration unit changed

                "-----------------------------------
                " Change Tree description
                "-----------------------------------
                IF <fs_landscape_before>-hec_landscape_descr <> lr_root->hec_landscape_descr.
                  lr_root->hec_tree_descr = lr_root->hec_landscape_descr. "#EC CI_FLDEXT_OK[2215424]
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Inherit System Timezone
                " Recurrence Type, Recurence Interval, Weekday
                "-----------------------------------
                IF <fs_landscape_before>-hec_system_timezone <> lr_root->hec_system_timezone.
                  ls_act_param_tier_inherit-do_update_timezone = abap_true.
                  lv_data_changed = abap_true.
                ENDIF.

                "Production
                IF <fs_landscape_before>-hec_prod_recurrence_type <> lr_root->hec_prod_recurrence_type
                OR <fs_landscape_before>-hec_prod_recurrence_interval <> lr_root->hec_prod_recurrence_interval
                OR <fs_landscape_before>-hec_prod_weekday <> lr_root->hec_prod_weekday
                OR <fs_landscape_before>-hec_prod_starttime <> lr_root->hec_prod_starttime
                OR <fs_landscape_before>-hec_prod_duration <> lr_root->hec_prod_duration
                OR <fs_landscape_before>-hec_prod_duration_unit <> lr_root->hec_prod_duration_unit
                OR <fs_landscape_before>-hec_prod_cmp_timezone <> lr_root->hec_prod_cmp_timezone.
                  ls_act_param_tier_inherit-do_update_prod = abap_true.
                  lv_data_changed = abap_true.
                ENDIF.

                "Non-Production
                IF <fs_landscape_before>-hec_nprod_recurrence_type <> lr_root->hec_prod_recurrence_type
                OR <fs_landscape_before>-hec_nprod_recurrence_interval <> lr_root->hec_prod_recurrence_interval
                OR <fs_landscape_before>-hec_nprod_weekday <> lr_root->hec_prod_weekday
                OR <fs_landscape_before>-hec_nprod_starttime <> lr_root->hec_nprod_starttime
                OR <fs_landscape_before>-hec_nprod_duration <> lr_root->hec_nprod_duration
                OR <fs_landscape_before>-hec_nprod_duration_unit <> lr_root->hec_nprod_duration_unit
                OR <fs_landscape_before>-hec_nprod_cmp_timezone <> lr_root->hec_nprod_cmp_timezone.
                  ls_act_param_tier_inherit-do_update_nonprod = abap_true.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Convert Material to internal
                "-----------------------------------
                CALL FUNCTION 'CONVERSION_EXIT_MATN1_INPUT'
                  EXPORTING
                    input  = lr_root->hec_material
                  IMPORTING
                    output = lr_root->hec_material.

                lv_data_changed = abap_true.
              ENDIF. "<fs_landscape_before> is not initial

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_root->hec_material                IS NOT INITIAL AND
                                                                       lr_root->hec_landscape_descr         IS NOT INITIAL AND
                                                                       lr_root->hec_landscape_config_status IS NOT INITIAL AND
                                                                       lr_root->hec_ls_contract_curr        IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete     ).

              lr_root->hec_delete_visible = abap_false.

              IF lv_inst_status <> lr_root->hec_instance_status.
                lr_root->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_root->key
                                   is_data = lr_root ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_landscape_before>.
            ENDLOOP.


            "-----------------------------------
            " Set Update datacenter
            " action to general
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_datacenter )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation  ).
            ENDIF.


            "-----------------------------------
            " Set Update Tier
            " action to general
            "-----------------------------------
            IF ls_act_param_tier_inherit IS NOT INITIAL.
              me->mr_act_param1 = NEW /hec1/s_act_update_tier_inhrit( ls_act_param_tier_inherit ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = it_key
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_tier_from_landscape )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = mr_act_param1 ).
            ENDIF.


            "-----------------------------------
            " Set Update Phase
            " action to general
            "-----------------------------------
            IF lt_act_param_phase IS NOT INITIAL.
              mr_act_param = NEW /hec1/t_act_update_phase( lt_act_param_phase ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-phase )
                  it_key          = VALUE #( FOR phase IN lt_act_param_phase
                                             ( key = phase-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_phase )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = mr_act_param  ).
            ENDIF.
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_contact_reference_cr.

    DATA: lt_contact_ref        TYPE /hec1/t_data_contact_ref_ct,
          lt_contact_ref_before TYPE /hec1/t_data_contact_ref_ct.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_contact_ref ).

    io_read->get_root_key( EXPORTING iv_node       = is_ctx-node_key
                                     it_key        = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create Mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-contact_reference-create.

            LOOP AT lt_contact_ref REFERENCE INTO DATA(lr_contact_ref).

*            IF lv_data_changed = abap_true.
*              io_modify->update( iv_node = is_ctx-node_key
*                                 iv_key  = lr_phase->key
*                                 is_data = lr_phase   ).
*            ENDIF.
*
*            CLEAR: lv_data_changed.

            ENDLOOP.

            " ***************************************************************************
            " Update Mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-contact_reference-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                                         iv_fill_data    = abap_true
                               IMPORTING et_data         = lt_contact_ref_before ).

            LOOP AT lt_contact_ref REFERENCE INTO lr_contact_ref.
              ASSIGN lt_contact_ref_before[ key = lr_contact_ref->key ] TO FIELD-SYMBOL(<fs_contact_ref_before>).

              IF <fs_contact_ref_before> IS ASSIGNED.

              ENDIF. "<fs_contact_ref_before> is assigned.

*              IF lv_data_changed = abap_true.
*                io_modify->update( iv_node = is_ctx-node_key
*                                   iv_key  = lr_phase->key
*                                   is_data = lr_phase   ).
*              ENDIF.
*
*              CLEAR: lv_data_changed.

              UNASSIGN <fs_contact_ref_before>.

            ENDLOOP. "lt_contact_ref
        ENDCASE. "is_ctx

      CATCH /bobf/cx_frw.
      CATCH cx_uuid_error. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD determine_phase_cr.

    DATA: lt_phase             TYPE /hec1/t_data_phase_ct,
          lt_phase_all         TYPE /hec1/t_data_phase_ct,
          lt_phase_before      TYPE /hec1/t_data_phase_ct,
          lt_phase_successor   TYPE /hec1/t_data_phase_ct,
          lt_phase_predecessor TYPE /hec1/t_data_phase_ct,
          lt_act_param         TYPE /hec1/t_act_update_phase,
          lv_date_start(10)    TYPE c,
          lv_date_end(10)      TYPE c,
          lt_root              TYPE /hec1/t_config_root_ct.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_phase ).

    io_read->get_root_key( EXPORTING iv_node       = is_ctx-node_key
                                     it_key        = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).

    " Get root
    io_read->retrieve( EXPORTING iv_node = /hec1/if_configuration_c=>sc_node-root
                                 it_key  = lt_root_key
                       IMPORTING et_data = lt_root ).

    DATA(ls_root) = VALUE #( lt_root[ 1 ] OPTIONAL ). "there is only always one root-line

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = lt_root_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                      IMPORTING et_data        = lt_phase_all ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create Mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-phase-create.

            LOOP AT lt_phase REFERENCE INTO DATA(lr_phase).

              TRY.
                  IF lr_phase->hec_node_phase IS INITIAL.
                    lr_phase->hec_node_phase = /rbp/cl_general_utilities=>get_new_guid22( ).
                    DATA(lv_data_changed) = abap_true.
                  ENDIF.

                  "-----------------------------------
                  " Change predecessor assignment
                  "-----------------------------------
                  IF lr_phase->hec_phase_predecessor_guid IS NOT INITIAL.

                    INSERT VALUE #( key                   = lr_phase->key
                                    do_update_predecessor = abap_true
                                    ) INTO TABLE lt_act_param.

                  ENDIF. "predecessor exists

                  "-----------------------------------
                  " Determine Phase Duration
                  "-----------------------------------
                  IF lr_phase->hec_duration_unit    IS NOT INITIAL AND
                     lr_phase->hec_phase_start_date IS NOT INITIAL AND
                     lr_phase->hec_phase_end_date   IS NOT INITIAL.

                    lr_phase->hec_phase_duration = /hec1/cl_config_helper=>calculate_duration( iv_start_date = lr_phase->hec_phase_start_date
                                                                                               iv_end_date   = lr_phase->hec_phase_end_date
                                                                                               iv_unit       = lr_phase->hec_duration_unit ).

                    lv_data_changed = abap_true.
                  ENDIF. " IF lr_phase->hec_duration_unit    IS NOT INITIAL AND

                  "-----------------------------------
                  " Update Tree Description
                  "-----------------------------------
                  IF lr_phase->hec_phase_start_date IS NOT INITIAL
                    AND lr_phase->hec_phase_end_date IS NOT INITIAL.

                    CALL FUNCTION 'CONVERT_DATE_TO_EXTERNAL'
                      EXPORTING
                        date_internal = lr_phase->hec_phase_start_date
                      IMPORTING
                        date_external = lv_date_start.

                    CALL FUNCTION 'CONVERT_DATE_TO_EXTERNAL'
                      EXPORTING
                        date_internal = lr_phase->hec_phase_end_date
                      IMPORTING
                        date_external = lv_date_end.

                    lr_phase->hec_phase_tree_descr = COND #( WHEN lr_phase->hec_phase_predecessor_guid IS NOT INITIAL
                                                             THEN |Successor - { lv_date_start }-{ lv_date_end } - { lr_phase->hec_phase_descr }|
                                                             ELSE |{ lv_date_start }-{ lv_date_end } - { lr_phase->hec_phase_descr }| ) .

                    lv_data_changed = abap_true.

                  ENDIF. "check for tree description update requirement

                  "-----------------------------------
                  " Set Phase complete status
                  "-----------------------------------
                  lr_phase->hec_phase_complete = COND #( WHEN lr_phase->hec_phase_descr IS NOT INITIAL
                                                          AND lr_phase->hec_phase_start_date IS NOT INITIAL
                                                          AND lr_phase->hec_phase_end_date IS NOT INITIAL
                                                          AND lr_phase->hec_phase_start_date <= lr_phase->hec_phase_end_date
                                                         THEN abap_true
                                                         ELSE abap_false ).

*                  "-----------------------------------
*                  " Inherit CR Counter from Root to Phase (only at create phase)
*                  "-----------------------------------
*                  IF ls_root-hec_cr_counter IS NOT INITIAL.
*                    lr_phase->hec_comp_cr_counter = ls_root-hec_cr_counter.
*
*                    lv_data_changed = abap_true.
*                  ENDIF.

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
                      is_node_data = lr_phase
                      iv_set_apm   = abap_true
                      iv_clear_phase = abap_true
                  ).

                  IF lv_data_changed = abap_false.
                    lv_data_changed = lv_cr_data_changed.
                  ENDIF.

                CATCH cx_uuid_error. " Error Class for UUID Processing Errors
              ENDTRY.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_phase->key
                                   is_data = lr_phase ).
              ENDIF.

              CLEAR: lv_data_changed.

            ENDLOOP.

            "-----------------------------------
            " Set Update Predecessor Phase
            "-----------------------------------
            IF lt_act_param IS NOT INITIAL.
              me->mr_act_param_phasing = NEW /hec1/t_act_update_phase( lt_act_param ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = VALUE #( FOR wa_act IN lt_act_param
                                            ( key = wa_act-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_phase )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                  ir_act_param    = me->mr_act_param_phasing  ).
            ENDIF.

            " ***************************************************************************
            " Update Mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-phase-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                                         iv_fill_data    = abap_true
                               IMPORTING et_data         = lt_phase_before ).

            LOOP AT lt_phase REFERENCE INTO lr_phase.
              ASSIGN lt_phase_before[ key = lr_phase->key ] TO FIELD-SYMBOL(<fs_phase_before>).

              IF <fs_phase_before> IS ASSIGNED.
                "-----------------------------------
                " Determine Phase Duration
                "-----------------------------------
                IF <fs_phase_before>-hec_phase_start_date <> lr_phase->hec_phase_start_date OR
                   <fs_phase_before>-hec_phase_end_date   <> lr_phase->hec_phase_end_date   OR
                   <fs_phase_before>-hec_duration_unit    <> lr_phase->hec_duration_unit    OR
                   lr_phase->hec_phase_duration              IS INITIAL.

                  IF lr_phase->hec_duration_unit    IS NOT INITIAL AND
                     lr_phase->hec_phase_start_date IS NOT INITIAL AND
                     lr_phase->hec_phase_end_date   IS NOT INITIAL.

                    lr_phase->hec_phase_duration = /hec1/cl_config_helper=>calculate_duration( iv_start_date = lr_phase->hec_phase_start_date
                                                                                               iv_end_date   = lr_phase->hec_phase_end_date
                                                                                               iv_unit       = lr_phase->hec_duration_unit ).

                    lv_data_changed = abap_true.

                  ENDIF.
                ENDIF. " check for phase update

                "-----------------------------------
                " Update Tree Description
                "-----------------------------------
                IF <fs_phase_before>-hec_phase_start_date NE lr_phase->hec_phase_start_date
                  OR <fs_phase_before>-hec_phase_end_date NE lr_phase->hec_phase_end_date
                  OR <fs_phase_before>-hec_phase_descr NE lr_phase->hec_phase_descr
                  OR <fs_phase_before>-hec_phase_predecessor_guid NE lr_phase->hec_phase_predecessor_guid.

                  CALL FUNCTION 'CONVERT_DATE_TO_EXTERNAL'
                    EXPORTING
                      date_internal = lr_phase->hec_phase_start_date
                    IMPORTING
                      date_external = lv_date_start.

                  CALL FUNCTION 'CONVERT_DATE_TO_EXTERNAL'
                    EXPORTING
                      date_internal = lr_phase->hec_phase_end_date
                    IMPORTING
                      date_external = lv_date_end.

                  lr_phase->hec_phase_tree_descr = COND #( WHEN lr_phase->hec_phase_predecessor_guid IS NOT INITIAL
                                                           THEN |Successor - { lv_date_start }-{ lv_date_end } - { lr_phase->hec_phase_descr }|
                                                           ELSE |{ lv_date_start }-{ lv_date_end } - { lr_phase->hec_phase_descr }| ) .

                  lv_data_changed = abap_true.

                ENDIF. "check for tree description update requirement

                "-----------------------------------
                " Phase changed from General
                "  e.g. Successor Changed
                "  This is relevant when a new
                "  successor is created. In that case
                "  the update of the predecessor-phase
                "  is called to update the successor
                "-----------------------------------
                IF lr_phase->hec_update_from_general = abap_true.
                  lv_data_changed = abap_true.
                ENDIF.

*                "-----------------------------------
*                " Start Date or End Date Changed
*                "  when there is a
*                "  successor or predecessor
*                "-----------------------------------
*                IF <fs_phase_before>-hec_phase_successor_guid IS NOT INITIAL
*                  AND <fs_phase_before>-hec_phase_end_date <> lr_phase->hec_phase_end_date
*                  AND <fs_phase_before>-hec_phase_end_date IS NOT INITIAL.
*
*                ENDIF.
*
*                IF <fs_phase_before>-hec_phase_predecessor_guid IS NOT INITIAL
*                  AND <fs_phase_before>-hec_phase_start_date <> lr_phase->hec_phase_start_date
*                  AND <fs_phase_before>-hec_phase_start_date IS NOT INITIAL.
*
*                ENDIF.

                "-----------------------------------
                " Set Phase complete status
                "-----------------------------------
                lr_phase->hec_phase_complete = COND #( WHEN lr_phase->hec_phase_descr IS NOT INITIAL
                                                        AND lr_phase->hec_phase_start_date IS NOT INITIAL
                                                        AND lr_phase->hec_phase_end_date IS NOT INITIAL
                                                        AND lr_phase->hec_phase_start_date <= lr_phase->hec_phase_end_date
                                                       THEN abap_true
                                                       ELSE abap_false ).

              ENDIF. "<fs_phase_before> is assigned.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_phase->key
                                   is_data = lr_phase ).
              ENDIF.

              CLEAR: lv_data_changed.

              UNASSIGN <fs_phase_before>.

            ENDLOOP. "lt_phase
        ENDCASE. "is_ctx

      CATCH /bobf/cx_frw.
      CATCH cx_uuid_error. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD determine_datacenter_cr.

    DATA: lt_datacenter             TYPE /hec1/t_data_datacenter_ct,
          lt_datacenter_before      TYPE /hec1/t_data_datacenter_ct,
          lt_phase                  TYPE /hec1/t_data_phase_ct,
          lt_if_baseline            TYPE /hec1/t_data_if_baseline_ct,
          lt_add_service            TYPE /hec1/t_data_add_services_ct,
          lt_solution               TYPE /hec1/t_data_solution_ct,
          lt_tier                   TYPE /hec1/t_data_tier_ct,
          lt_act_param              TYPE /hec1/t_data_datacenter_ct,
          lt_act_create_connect     TYPE /hec1/t_act_create_connect,
          ls_act_param_landscape    TYPE /hec1/s_act_update_landscape,
          lt_act_param_connectivity TYPE /bobf/t_frw_key,
          lt_act_param_dlvy_unit    TYPE /hec1/t_act_update_dlvy_unit,
          lt_act_param_add_service  TYPE /bobf/t_frw_key,
          lt_act_param_if_baseline  TYPE /bobf/t_frw_key,
          lt_act_param_tier         TYPE /bobf/t_frw_key,
          lt_act_param_phasing      TYPE TABLE OF /hec1/s_act_phase_inherit.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_datacenter ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit) ).

    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-datacenter-infrastructure_baseline
                                      IMPORTING et_data        = lt_if_baseline ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Set data center country name
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-datacenter-get_country_descr.

            LOOP AT lt_datacenter REFERENCE INTO DATA(lr_datacenter)
              WHERE hec_datacenter_guid               IS NOT INITIAL AND
                    hec_datacenter_country       IS NOT INITIAL AND
                    hec_datacenter_country_descr IS INITIAL.

              " Get data center country name
              SELECT SINGLE landx FROM t005t
                       INTO lr_datacenter->hec_datacenter_country_descr
                      WHERE spras = sy-langu
                        AND land1 = lr_datacenter->hec_datacenter_country.

              io_modify->update( iv_node = is_ctx-node_key
                                 iv_key  = lr_datacenter->key
                                 is_data = lr_datacenter ).

            ENDLOOP.

            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-datacenter-create.

            LOOP AT lt_datacenter REFERENCE INTO lr_datacenter.

              lr_datacenter->hec_delete_visible = COND #( WHEN lr_datacenter->hec_phase_guid IS NOT INITIAL
                                                          THEN abap_false
                                                          ELSE abap_true ).

              lr_datacenter->hec_row_selectable = abap_true.

              "-----------------------------------
              " Fill fields for Region,
              "  Delivery Unit and Infrastructure Provider
              "-----------------------------------
              lr_datacenter->* = VALUE #( BASE lr_datacenter->*
                                               hec_dlvy_region_l1_guid = lr_landscape->hec_dlvy_region_l1_guid
                                               hec_dlvy_region_l2_guid = lr_landscape->hec_dlvy_region_l2_guid
                                               hec_datacenter_country  = lr_landscape->hec_country_key
                                               hec_delivery_unit_guid  = lr_delivery_unit->hec_delivery_unit_guid
                                               hec_delivery_unit_descr = lr_delivery_unit->hec_delivery_unit_descr
                                               hec_infra_provider_guid = lr_delivery_unit->hec_inf_provider_guid
                                               hec_inf_provider_descr  = lr_delivery_unit->hec_inf_provider_descr  ).


              "-----------------------------------
              " Fill Parameter for General Call
              "  For Connectivity Creation
              "-----------------------------------
              INSERT VALUE #( BASE CORRESPONDING #( lr_datacenter->* )
                                  parent_key              = lr_datacenter->key
                                  hec_node_connectivity   = /rbp/cl_general_utilities=>get_new_guid22( ) ) INTO TABLE lt_act_create_connect.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_datacenter->hec_datacenter_type_value IS NOT INITIAL AND
                                                                             lr_datacenter->hec_datacenter_guid       IS NOT INITIAL AND
                                                                             lr_datacenter->hec_datacenter_country    IS NOT INITIAL AND
                                                                             lr_datacenter->hec_phase_guid            IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_datacenter->hec_instance_status.
                lr_datacenter->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.


              "-----------------------------------
              " Modify data center
              "-----------------------------------
              IF lv_data_changed IS NOT INITIAL.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_datacenter->key
                                   is_data = lr_datacenter ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

            ENDLOOP.

            "-----------------------------------
            " Set Create Connectivity
            " action to general
            "-----------------------------------
            IF lt_act_create_connect IS NOT INITIAL.

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys_direct(
                is_ctx          = CORRESPONDING #( is_ctx )
                it_key          = VALUE #( FOR param IN lt_act_create_connect
                                           ( key = param-parent_key ) )
                iv_action       = /hec1/if_configuration_c=>sc_action-datacenter-create_connectivity
                iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation ).

            ENDIF.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-datacenter-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_datacenter_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get solution
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-solution
                                              IMPORTING et_target_key  = DATA(lt_solution_key) ).

            " Get tier
            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-solution
                                                        it_key         = lt_solution_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                              IMPORTING et_data        = lt_tier ).

            "-----------------------------------
            " Get Data center from APM
            "-----------------------------------
            SELECT *
              FROM /hec1/i_regdlvyinfrdatabasic
              INTO TABLE @DATA(lt_fdt_datacenter)
               FOR ALL ENTRIES IN @lt_datacenter
             WHERE hec_datacenter_guid = @lt_datacenter-hec_datacenter_guid.


            LOOP AT lt_datacenter REFERENCE INTO lr_datacenter.
              lr_datacenter->hec_delete_visible = COND #( WHEN lr_datacenter->hec_phase_guid IS NOT INITIAL
                                                          THEN abap_false
                                                          ELSE abap_true ).

              lr_datacenter->hec_row_selectable = abap_true.

              ASSIGN lt_datacenter_before[ key = lr_datacenter->key ] TO FIELD-SYMBOL(<fs_datacenter_before>).
              IF <fs_datacenter_before> IS ASSIGNED.

                "-----------------------------------
                " Data center GUID has changed
                "-----------------------------------
                " Get data center country and description
                IF <fs_datacenter_before>-hec_datacenter_guid IS INITIAL AND
                   lr_datacenter->hec_datacenter_guid     IS NOT INITIAL.

                  lr_datacenter->* = CORRESPONDING #( BASE ( lr_datacenter->* ) VALUE #( lt_fdt_datacenter[ hec_datacenter_guid = lr_datacenter->hec_datacenter_guid ] OPTIONAL ) ).

                  lr_datacenter->hec_tree_descr = lr_datacenter->hec_datacenter_descr. "#EC CI_FLDEXT_OK[2215424]
                  lv_data_changed               = abap_true.

                  " Update Landscape
                  ls_act_param_landscape = VALUE #( key                    = lr_datacenter->root_key
                                                    hec_datacenter_country = lr_datacenter->hec_datacenter_country
                                                    do_update_region       = abap_true ).

                ENDIF. " IF ls_datacenter_old-hec_datacenter_guid IS INITIAL


                "-----------------------------------
                " Region L1-2, Delivery Unit or
                " Infrastructure Provider has
                " changed
                "-----------------------------------
                IF lr_datacenter->hec_dlvy_region_l1_guid <> <fs_datacenter_before>-hec_dlvy_region_l1_guid OR
                   lr_datacenter->hec_dlvy_region_l2_guid <> <fs_datacenter_before>-hec_dlvy_region_l2_guid OR
                   lr_datacenter->hec_datacenter_country  <> <fs_datacenter_before>-hec_datacenter_country  OR
                   lr_datacenter->hec_infra_provider_guid <> <fs_datacenter_before>-hec_infra_provider_guid OR
                   lr_datacenter->hec_delivery_unit_guid  <> <fs_datacenter_before>-hec_delivery_unit_guid.
                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_datacenter->hec_phase_guid NE <fs_datacenter_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_datacenter->key
                                  hec_phase_guid_new = lr_datacenter->hec_phase_guid
                                  hec_phase_guid_old = <fs_datacenter_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_datacenter->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "phasing changed


                "-----------------------------------
                " Update Delivery Unit and afterwards
                " Infrastructure baseline
                "-----------------------------------
                IF ( lr_datacenter->hec_datacenter_guid <> <fs_datacenter_before>-hec_datacenter_guid AND
                     lr_datacenter->hec_datacenter_guid IS NOT INITIAL                                    ) OR
                     lr_datacenter->hec_phase_changed  = abap_true.

                  TRY.
                      lr_datacenter->hec_infra_provider_guid = lt_fdt_datacenter[ hec_datacenter_guid = lr_datacenter->hec_datacenter_guid ]-hec_infra_provider_guid.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  INSERT VALUE #( key                   = lr_datacenter->key
                                  hec_inf_provider_guid = lr_datacenter->hec_infra_provider_guid ) INTO TABLE lt_act_param_dlvy_unit.

                  TRY.
                      DATA(ls_if_baseline) = lt_if_baseline[ parent_key = lr_datacenter->key ].
                      INSERT VALUE #( key = ls_if_baseline-key ) INTO TABLE lt_act_param_if_baseline.

                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                ENDIF. " IF ( lr_datacenter->hec_datacenter_guid <> <fs_datacenter_before>-hec_datacenter_guid...


                "-----------------------------------
                " Update additional service
                "-----------------------------------
                IF <fs_datacenter_before>-hec_datacenter_guid <> lr_datacenter->hec_datacenter_guid.
                  INSERT VALUE #( key = lr_datacenter->key ) INTO TABLE lt_act_param_add_service.
                ENDIF.


                "-----------------------------------
                " Update Tier
                "-----------------------------------
                IF <fs_datacenter_before>-hec_datacenter_guid IS INITIAL AND
                   lr_datacenter->hec_datacenter_guid     IS NOT INITIAL.

                  LOOP AT lt_tier ASSIGNING FIELD-SYMBOL(<fs_tier>).
                    INSERT VALUE #( key = <fs_tier>-key ) INTO TABLE lt_act_param_tier.
                  ENDLOOP.

                ENDIF.


                "-----------------------------------   -> later replaced by action
                " Reset data center GUID
                "-----------------------------------
                IF <fs_datacenter_before>-hec_datacenter_guid IS NOT INITIAL AND
                   lr_datacenter->hec_datacenter_guid         IS INITIAL.

                  CLEAR: lr_datacenter->hec_datacenter_country,
                         lr_datacenter->hec_datacenter_country_descr,
                         lr_datacenter->hec_datacenter_descr,
                         lr_datacenter->hec_tree_descr,
                         lr_datacenter->hec_sec_datacenter_guid.

                  lv_data_changed = abap_true.
                ENDIF.

                "-----------------------------------
                " Update Connectivity
                "-----------------------------------
                IF lr_datacenter->hec_sec_datacenter_guid <> <fs_datacenter_before>-hec_sec_datacenter_guid.
                  INSERT VALUE #( key = lr_datacenter->key ) INTO TABLE lt_act_param_connectivity.
                ENDIF.

              ENDIF. "<fs_datacenter> is assigned.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_datacenter->hec_datacenter_type_value IS NOT INITIAL AND
                                                                       lr_datacenter->hec_datacenter_guid       IS NOT INITIAL AND
                                                                       lr_datacenter->hec_datacenter_country    IS NOT INITIAL AND
                                                                       lr_datacenter->hec_phase_guid            IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete     ).

              IF lv_inst_status <> lr_datacenter->hec_instance_status.
                lr_datacenter->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Modify data center
              "-----------------------------------
              IF lv_data_changed IS NOT INITIAL.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_datacenter->key
                                   is_data = lr_datacenter ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_datacenter_before>.
            ENDLOOP. " LOOP AT lt_datacenter REFERENCE INTO lr_datacenter.


            "-----------------------------------
            " Update Landscape
            "-----------------------------------
            IF ls_act_param_landscape IS NOT INITIAL.
              me->mr_act_param = NEW /hec1/s_act_update_landscape( ls_act_param_landscape ).
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = CORRESPONDING #( is_ctx )
                    it_key          = it_key
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_landscape )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param ).
            ENDIF.

            "-----------------------------------
            " Update Delivery Unit
            "-----------------------------------
            IF lt_act_param_dlvy_unit IS NOT INITIAL.
              me->mr_act_param = NEW /hec1/t_act_update_dlvy_unit( lt_act_param_dlvy_unit ).
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = CORRESPONDING #( is_ctx )
                    it_key          = it_key "lt_act_param_dlvy_unit
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_delivery_unit )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                    ir_act_param    = me->mr_act_param ).
            ENDIF.


            "-----------------------------------
            " Update Infrastructure Baseline
            "-----------------------------------
            IF lt_act_param_if_baseline IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                                  node_key      = /hec1/if_configuration_c=>sc_node-infrastructure_baseline )
                  it_key          = VALUE #( ( key = ls_if_baseline-key ) )
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_if_baseline )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation ).
            ENDIF.


            "-----------------------------------
            " Update Connectivity
            "-----------------------------------
            IF lt_act_param_connectivity IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                    is_ctx          = CORRESPONDING #( is_ctx )
                    it_key          = lt_act_param_connectivity
                    iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_connectivity )
                    iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation ).
            ENDIF.


            "-----------------------------------
            " Update Additional Service
            "-----------------------------------
            IF lt_act_param_add_service IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = CORRESPONDING #( is_ctx )
                  it_key          = lt_act_param_add_service
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_additional_service )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation ).
            ENDIF.


            "-----------------------------------
            " Update Tier
            "-----------------------------------
            IF lt_act_param_tier IS NOT INITIAL.
              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                  is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                             node_key = /hec1/if_configuration_c=>sc_node-tier )
                  it_key          = lt_act_param_tier
                  iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_tier )
                  iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation ).
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
        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_network_segment_cr.

    RETURN. ">>>>>

  ENDMETHOD.


  METHOD determine_add_service_cr.

    DATA: lt_add_service        TYPE /hec1/t_data_add_services_ct,
          lt_add_service_before TYPE /hec1/t_data_add_services_ct,
          lr_add_service        TYPE REF TO /hec1/s_data_add_services_cs,
          lt_phase              TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing  TYPE TABLE OF /hec1/s_act_phase_inherit.

    CLEAR: eo_message,
           et_failed_key.



    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_add_service ).


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
          WHEN /hec1/if_configuration_c=>sc_determination-add_service-create.

            IF lines( lt_datacenter ) = 1.
              " Get data center data
              TRY.
                  DATA(ls_datacenter) = lt_datacenter[ 1 ].
                CATCH cx_sy_itab_line_not_found.
              ENDTRY.
            ENDIF.

            LOOP AT lt_add_service REFERENCE INTO lr_add_service.

              lr_add_service->hec_delete_visible = abap_true.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_add_service->hec_as_class_guid      IS NOT INITIAL AND
                                                                             lr_add_service->hec_as_datacenter_guid IS NOT INITIAL AND
                                                                             lr_add_service->hec_phase_guid         IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).




              IF lv_inst_status <> lr_add_service->hec_instance_status.
                lr_add_service->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Assign data center
              "-----------------------------------
              IF ls_datacenter-hec_datacenter_guid IS NOT INITIAL.
                lr_add_service->hec_as_datacenter_guid  = ls_datacenter-hec_node_datacenter.
                lr_add_service->hec_as_datacenter_descr = ls_datacenter-hec_datacenter_descr.
                lv_data_changed = abap_true.
              ENDIF.

              "------------------------------------------
              " Set CR related fields from the ROOT node
              "------------------------------------------
              DATA(lv_cr_data_changed) = /hec1/cl_config_helper=>set_cr_related_fields(
                EXPORTING
                  is_ctx       = is_ctx
                  it_key       = it_key
                  io_read      = io_read
                  io_modify    = io_modify
                  iv_mod_type  = /hec1/if_config_constants=>gc_comp_mod_type-added
                  is_node_data = lr_add_service
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              "-----------------------------------
              " Modify aditional service
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_add_service->key
                                   is_data = lr_add_service ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.
            ENDLOOP.

            " ***************************************************************************
            " update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-add_service-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_add_service_before ).


            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).



            LOOP AT lt_add_service REFERENCE INTO lr_add_service.
              lr_add_service->hec_delete_visible = abap_true.
              ASSIGN lt_add_service_before[ key = lr_add_service->key ] TO FIELD-SYMBOL(<fs_add_service_before>).

              " Get data center data
              TRY.
                  ls_datacenter = lt_datacenter[ hec_node_datacenter = lr_add_service->hec_as_datacenter_guid ].
                CATCH cx_sy_itab_line_not_found.
              ENDTRY.

              IF <fs_add_service_before> IS ASSIGNED.
                "-----------------------------------
                " Service class GUID has changed
                "-----------------------------------
                IF lr_dlvy_unit->hec_inf_provider_guid IS NOT INITIAL                              AND
                   ls_datacenter-hec_datacenter_guid   IS NOT INITIAL                              AND
                   lr_add_service->hec_as_class_guid   IS NOT INITIAL                              AND
                   <fs_add_service_before>-hec_as_class_guid <> lr_add_service->hec_as_class_guid.

                  " Get number of service class entries
                  DATA(lv_count_class_guid) = lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_datac_add_service_class( iv_apm_guid          = lr_landscape->hec_apm_guid
                                                                                                                                                 iv_inf_provider_guid = lr_dlvy_unit->hec_inf_provider_guid
                                                                                                                                                 iv_datacenter_guid   = ls_datacenter-hec_datacenter_guid   ) ).

                  " Get additional service data
                  SELECT SINGLE *
                    FROM /hec1/i_addserviceclassbasic
                   WHERE hec_apm_guid      = @lr_landscape->hec_apm_guid        AND
                         hec_as_class_guid = @lr_add_service->hec_as_class_guid
                    INTO CORRESPONDING FIELDS OF @lr_add_service->*.


                  " Set additional service description in case it is empty
                  IF lr_add_service->hec_as_class_guid      IS NOT INITIAL AND
                     lr_add_service->hec_as_class_descr     IS NOT INITIAL AND
                     lr_add_service->hec_as_class_descr_ext IS INITIAL.
                    lr_add_service->hec_as_class_descr_ext = lr_add_service->hec_as_class_descr.
                  ENDIF.


                  " Get number of service entries
                  SELECT COUNT(*)
                    FROM /hec1/i_addserviceclasslbbasic
                   WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid          AND
                         hec_sec_datacenter_guid = @ls_datacenter-hec_datacenter_guid   AND
                         hec_inf_provider_guid   = @lr_dlvy_unit->hec_inf_provider_guid AND
                         hec_as_class_guid       = @lr_add_service->hec_as_class_guid
                   INTO @DATA(lv_count).

                  IF lv_count = 1.
                    SELECT SINGLE *
                      FROM /hec1/i_addserviceclasslbbasic
                     WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid          AND
                           hec_sec_datacenter_guid = @ls_datacenter-hec_datacenter_guid   AND
                           hec_inf_provider_guid   = @lr_dlvy_unit->hec_inf_provider_guid AND
                           hec_as_class_guid       = @lr_add_service->hec_as_class_guid
                      INTO @DATA(ls_service_data).

                    " Get pricing
                    SELECT SINGLE * FROM /hec1/c_cbp_lb "#EC CI_ALL_FIELDS_NEEDED
                       INTO @DATA(ls_pricing)
                      WHERE hec_price_lb = @ls_service_data-hec_cb_pricing_lb_guid.

                  ENDIF. " IF lv_count = 1.

                  DATA(lv_exchange_rate) = lr_add_service->hec_exchange_rate. "Temp field because the ls_pricing structure overwrites the real exchange_rate

                  lr_add_service->* = VALUE #( BASE lr_add_service->*
                                               hec_as_class_vlqt       = SWITCH #( lv_count_class_guid
                                                                                   WHEN 0
                                                                                   THEN space
                                                                                   WHEN 1
                                                                                   THEN /hec1/if_config_constants=>gc_value_list_quantity-single
                                                                                   ELSE /hec1/if_config_constants=>gc_value_list_quantity-multi  )
                                               hec_ip_as_class_guid    = ls_service_data-hec_ip_as_class_guid
                                               hec_ip_as_class_descr   = ls_service_data-hec_ip_as_class_descr
                                               hec_ip_as_class_vlqt    = SWITCH #( lv_count
                                                                                   WHEN 0
                                                                                   THEN space
                                                                                   WHEN 1
                                                                                   THEN /hec1/if_config_constants=>gc_value_list_quantity-single
                                                                                   ELSE /hec1/if_config_constants=>gc_value_list_quantity-multi  )
                                               hec_as_quota            = ls_service_data-hec_as_quota
                                               hec_as_tier_uplift_perc = ls_service_data-hec_as_upflift_percent
                                               hec_price_lb            = ls_service_data-hec_cb_pricing_lb_guid
                                               hec_as_datacenter_guid  = COND #( WHEN ls_datacenter-hec_datacenter_guid IS NOT INITIAL
                                                                                 THEN ls_datacenter-hec_node_datacenter
                                                                                 ELSE space                                             )
                                               hec_as_datacenter_descr = COND #( WHEN ls_datacenter-hec_datacenter_descr IS NOT INITIAL
                                                                                 THEN ls_datacenter-hec_datacenter_descr
                                                                                 ELSE space                                             )
                                               hec_tree_descr          = COND #( WHEN ls_datacenter-hec_datacenter_guid IS INITIAL
                                                                                 THEN |{ lr_add_service->hec_as_class_descr } : { lr_add_service->hec_as_class_descr_ext }|
                                                                                 ELSE |{ lr_add_service->hec_as_class_descr } - { ls_datacenter-hec_datacenter_descr } : { lr_add_service->hec_as_class_descr_ext }| )
                                               price                   = CORRESPONDING #( BASE ( lr_add_service->price ) ls_pricing )
                                               hec_exchange_rate       = lv_exchange_rate                                                       ).

                  lv_data_changed = abap_true.
                ENDIF. " IF lr_add_service->hec_as_class_guid IS NOT INITIAL AND


                "-----------------------------------
                " Service GUID has changed
                "-----------------------------------
                IF lr_dlvy_unit->hec_inf_provider_guid  IS NOT INITIAL                                  AND
                   ls_datacenter-hec_datacenter_guid    IS NOT INITIAL                                  AND
                   lr_add_service->hec_as_class_guid    IS NOT INITIAL                                  AND
                   lr_add_service->hec_ip_as_class_guid IS NOT INITIAL                                  AND
                   <fs_add_service_before>-hec_ip_as_class_guid <> lr_add_service->hec_ip_as_class_guid.

                  " Get number of service entries
                  SELECT COUNT(*)
                    FROM /hec1/i_addserviceclasslbbasic
                   WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid          AND
                         hec_sec_datacenter_guid = @ls_datacenter-hec_datacenter_guid   AND
                         hec_inf_provider_guid   = @lr_dlvy_unit->hec_inf_provider_guid AND
                         hec_as_class_guid       = @lr_add_service->hec_as_class_guid
                   INTO @lv_count.


                  SELECT SINGLE *
                    FROM /hec1/i_addserviceclasslbbasic
                   WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid           AND
                         hec_sec_datacenter_guid = @ls_datacenter-hec_datacenter_guid    AND
                         hec_inf_provider_guid   = @lr_dlvy_unit->hec_inf_provider_guid  AND
                         hec_as_class_guid       = @lr_add_service->hec_as_class_guid    AND
                         hec_ip_as_class_guid    = @lr_add_service->hec_ip_as_class_guid
                    INTO @ls_service_data.

                  " Get pricing
                  SELECT SINGLE * FROM /hec1/c_cbp_lb "#EC CI_ALL_FIELDS_NEEDED
                     INTO @ls_pricing
                    WHERE hec_price_lb = @ls_service_data-hec_cb_pricing_lb_guid.

                  lv_exchange_rate = lr_add_service->hec_exchange_rate. "Temp field because the ls_pricing structure overwrites the real exchange_rate

                  lr_add_service->* = VALUE #( BASE lr_add_service->*
                                               hec_ip_as_class_guid    = ls_service_data-hec_ip_as_class_guid
                                               hec_ip_as_class_descr   = ls_service_data-hec_ip_as_class_descr
                                               hec_ip_as_class_vlqt    = SWITCH #( lv_count
                                                                                   WHEN 0
                                                                                   THEN space
                                                                                   WHEN 1
                                                                                   THEN /hec1/if_config_constants=>gc_value_list_quantity-single
                                                                                   ELSE /hec1/if_config_constants=>gc_value_list_quantity-multi  )
                                               hec_as_quota            = ls_service_data-hec_as_quota
                                               hec_as_tier_uplift_perc = ls_service_data-hec_as_upflift_percent
                                               hec_price_lb            = ls_service_data-hec_cb_pricing_lb_guid
                                               hec_as_datacenter_guid  = COND #( WHEN ls_datacenter-hec_datacenter_guid IS NOT INITIAL
                                                                                 THEN ls_datacenter-hec_node_datacenter
                                                                                 ELSE space                                             )
                                               hec_as_datacenter_descr = COND #( WHEN ls_datacenter-hec_datacenter_descr IS NOT INITIAL
                                                                                 THEN ls_datacenter-hec_datacenter_descr
                                                                                 ELSE space                                             )
                                               hec_tree_descr          = COND #( WHEN ls_datacenter-hec_datacenter_guid IS INITIAL
                                                                                 THEN |{ lr_add_service->hec_as_class_descr } : { lr_add_service->hec_as_class_descr_ext }|
                                                                                 ELSE |{ lr_add_service->hec_as_class_descr } - { ls_datacenter-hec_datacenter_descr } : { lr_add_service->hec_as_class_descr_ext }| )
                                               price                   = CORRESPONDING #( BASE ( lr_add_service->price ) ls_pricing )
                                               hec_exchange_rate       = lv_exchange_rate                                                       ).

                  lv_data_changed = abap_true.
                ENDIF. " IF lr_dlvy_unit->hec_inf_provider_guid  IS NOT INITIAL AND

                "-----------------------------------
                " Data center GUID has changed
                "-----------------------------------
                IF ls_datacenter-hec_datacenter_guid              IS NOT INITIAL AND
                   lr_add_service->hec_as_datacenter_guid         IS NOT INITIAL AND
                   <fs_add_service_before>-hec_as_datacenter_guid IS     INITIAL.
                  lr_add_service->hec_as_datacenter_descr = ls_datacenter-hec_datacenter_descr.
                ENDIF.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_add_service->hec_phase_guid NE <fs_add_service_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_add_service->key
                                  hec_phase_guid_new = lr_add_service->hec_phase_guid
                                  hec_phase_guid_old = <fs_add_service_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_add_service->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "Phase changed

                "-----------------------------------
                " Resets -> TODO move to actions
                "-----------------------------------

                " Reset Service Class GUID
                IF lr_add_service->hec_as_class_guid IS INITIAL.
                  IF lr_add_service->hec_as_class_descr = lr_add_service->hec_as_class_descr_ext.
                    CLEAR: lr_add_service->hec_as_class_descr_ext.
                  ENDIF.
                  CLEAR: lr_add_service->hec_as_class_descr,
                         lr_add_service->hec_as_class_vlqt,
                         lr_add_service->hec_as_tier_counter,
                         lr_add_service->hec_as_tier_uplift,
                         lr_add_service->hec_ip_as_class_guid,
                         lr_add_service->hec_ip_as_class_descr,
                         lr_add_service->hec_ip_as_class_vlqt,
                         lr_add_service->hec_as_quota,
                         lr_add_service->hec_as_tier_uplift_perc,
                         lr_add_service->price.

                  lv_data_changed = abap_true.
                ENDIF.


                " Reset Service GUID
                IF lr_add_service->hec_ip_as_class_guid IS     INITIAL AND
                   lr_add_service->hec_as_class_guid    IS NOT INITIAL.
                  CLEAR: lr_add_service->hec_ip_as_class_descr,
                         lr_add_service->hec_as_quota,
                         lr_add_service->hec_as_tier_uplift_perc,
                         lr_add_service->price.

                  lv_data_changed = abap_true.
                ENDIF.


                " Reset Datacenter
                IF <fs_add_service_before>-hec_as_datacenter_guid IS NOT INITIAL AND
                   lr_add_service->hec_as_datacenter_guid         IS     INITIAL.
                  CLEAR: lr_add_service->hec_as_datacenter_descr.

                  lv_data_changed = abap_true.
                ENDIF.

                IF <fs_add_service_before>-hec_as_datacenter_descr <> lr_add_service->hec_as_datacenter_descr.
                  lr_add_service->hec_tree_descr = COND #( WHEN ls_datacenter-hec_datacenter_descr IS INITIAL
                                                           THEN |{ lr_add_service->hec_as_class_descr } : { lr_add_service->hec_as_class_descr_ext }|
                                                           ELSE |{ lr_add_service->hec_as_class_descr } - { ls_datacenter-hec_datacenter_descr } : { lr_add_service->hec_as_class_descr_ext }| ).

                  lv_data_changed = abap_true.
                ENDIF.
              ENDIF. "<fs_add_service_before> is assigned


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_add_service->hec_as_class_guid      IS NOT INITIAL AND
                                                                       lr_add_service->hec_as_datacenter_guid IS NOT INITIAL AND
                                                                       lr_add_service->hec_phase_guid         IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete   ).

              IF lv_inst_status <> lr_add_service->hec_instance_status.
                lr_add_service->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify aditional service
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_add_service->key
                                   is_data = lr_add_service ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_exchange_rate,
                     lv_count,
                     lv_count_class_guid,
                     ls_datacenter,
                     ls_service_data,
                     ls_pricing.

              UNASSIGN <fs_add_service_before>.
            ENDLOOP. "LOOP AT lt_add_service REFERENCE INTO lr_add_service.

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


        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_material_cr.

    DATA: lt_tier              TYPE /hec1/t_data_tier_ct,
          lt_material          TYPE /hec1/t_data_material_ct,
          lt_material_before   TYPE /hec1/t_data_material_ct,
          lt_phase             TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing TYPE TABLE OF /hec1/s_act_phase_inherit,
          lt_act_param_sw_item TYPE /hec1/t_act_create_sw_item.


    CLEAR: eo_message,
           et_failed_key,
           me->mr_act_param.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_material ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit) ).

    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-material-to_parent
                                      IMPORTING et_data        = lt_tier ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = VALUE #( ( key = lv_root_key ) )
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                      IMPORTING et_data        = lt_phase ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-material-create.

            LOOP AT lt_material REFERENCE INTO DATA(lr_material).
              lr_material->hec_delete_visible = abap_false.

              lr_material->hec_tree_descr = lr_material->hec_hsp_material_pli_name.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_material->hec_phase_guid IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_material->hec_instance_status.
                lr_material->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_tier[ key = lr_material->parent_key ] TO FIELD-SYMBOL(<fs_tier>).
              IF <fs_tier> IS ASSIGNED.
                DATA(lv_release) = COND #( WHEN <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                                                <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL AND
                                                <fs_tier>-hec_tier_type_value      IS NOT INITIAL
                                           THEN abap_true
                                           ELSE abap_false                                            ).
              ENDIF.

              IF lv_release <> lr_material->hec_row_selectable.
                lr_material->hec_row_selectable = lv_release.
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
                  is_node_data = lr_material
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              "-----------------------------------
              " Fill action table for create
              " SW Item
              "-----------------------------------
              INSERT VALUE #( parent_key         = lr_material->key ) INTO TABLE lt_act_param_sw_item.

              "-----------------------------------
              " Modify material
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_material->key
                                   is_data = lr_material ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release.
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
            " Set Follow-Up to GENERAL
            " - Create Software Item
            "-----------------------------------
            IF lt_act_param_sw_item IS NOT INITIAL.

              me->mr_act_param_sw_item_add = NEW /hec1/t_act_create_sw_item( lt_act_param_sw_item ).

              /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
                   is_ctx          = CORRESPONDING #( is_ctx )
                   it_key          = VALUE #( FOR sw_item_add IN lt_act_param_sw_item
                                            ( key = sw_item_add-parent_key ) )
                   iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-create_software_item )
                   iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
                   ir_act_param    = me->mr_act_param_sw_item_add ).
            ENDIF.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-material-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_material_before ).

            LOOP AT lt_material REFERENCE INTO lr_material.
              lr_material->hec_delete_visible = abap_false.

              ASSIGN lt_material_before[ key = lr_material->key ] TO FIELD-SYMBOL(<fs_material_before>).
              IF <fs_material_before> IS ASSIGNED.

                lr_material->hec_tree_descr = lr_material->hec_hsp_material_pli_name.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_material->hec_phase_guid NE <fs_material_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_material->key
                                  hec_phase_guid_new = lr_material->hec_phase_guid
                                  hec_phase_guid_old = <fs_material_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_material->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. " IF lr_material->hec_phase_guid NE <fs_material_before>-hec_phase_guid.
              ENDIF. " IF <fs_material_before> IS ASSIGNED.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_material->hec_phase_guid IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_material->hec_instance_status.
                lr_material->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_tier[ key = lr_material->parent_key ] TO <fs_tier>.
              IF <fs_tier> IS ASSIGNED.
                lv_release = COND #( WHEN <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                                          <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL AND
                                          <fs_tier>-hec_tier_type_value      IS NOT INITIAL
                                     THEN abap_true
                                     ELSE abap_false                                            ).
              ENDIF.

              IF lv_release <> lr_material->hec_row_selectable.
                lr_material->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify material
              "-----------------------------------
*              DATA  lt_modification        TYPE /bobf/t_frw_modification.

              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_material->key
                                   is_data = lr_material ).

*
*                INSERT VALUE #( data        = lr_material
*                                node        = /hec1/if_configuration_c=>sc_node-material
*                                change_mode = /bobf/if_frw_c=>sc_modify_update
*                                key         = lr_material->key    ) INTO TABLE lt_modification.

              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release.
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

*            "-----------------------------------
*            " Change Instances
*            "-----------------------------------
*            IF lt_modification IS NOT INITIAL.
*              io_modify->do_modify( lt_modification ).
*
*              io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
*                                     IMPORTING eo_message             = DATA(lo_message)
*                                               eo_change              = DATA(lo_change)  ).
*            ENDIF.


            " ***************************************************************************
            " Update and after tier
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-material-update_after_tier.

            LOOP AT lt_material REFERENCE INTO lr_material.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_material->hec_phase_guid IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_material->hec_instance_status.
                lr_material->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_tier[ key = lr_material->parent_key ] TO <fs_tier>.
              IF <fs_tier> IS ASSIGNED.
                lv_release = COND #( WHEN <fs_tier>-hec_tier_descr           IS NOT INITIAL AND
                                          <fs_tier>-hec_tier_impl_type_value IS NOT INITIAL AND
                                          <fs_tier>-hec_tier_type_value      IS NOT INITIAL
                                     THEN abap_true
                                     ELSE abap_false                                            ).
              ENDIF.

              IF lv_release <> lr_material->hec_row_selectable.
                lr_material->hec_row_selectable = lv_release.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify material
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_material->key
                                   is_data = lr_material ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed,
                     lv_release.
            ENDLOOP.

        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_connectivity_cr.

    DATA: lt_datacenter          TYPE /hec1/t_data_datacenter_ct,
          lt_connectivity        TYPE /hec1/t_data_connectivity_ct,
          lt_connectivity_before TYPE /hec1/t_data_connectivity_ct,
          lt_phase               TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing   TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_connectivity ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create and update after data center
            " mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-connectivity-create OR
               /hec1/if_configuration_c=>sc_determination-connectivity-update_after_datacenter.

            " Get data center (parent)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-connectivity-to_parent
                                              IMPORTING et_data        = lt_datacenter ).

            LOOP AT lt_connectivity REFERENCE INTO DATA(lr_connectivity).

              "-----------------------------------
              " Set Value List Quantity
              "-----------------------------------
              lr_connectivity->hec_connectivity_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_connectivity(
                                                                                                 iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                                 iv_sec_datacenter_guid = lr_connectivity->hec_sec_datacenter_guid ) )
                                                               THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                               ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

              "-----------------------------------
              " Set tree control
              "-----------------------------------
              lr_connectivity->hec_delete_visible = abap_true.

              IF is_ctx-det_key = /hec1/if_configuration_c=>sc_determination-connectivity-create.
                lr_connectivity->hec_row_selectable = abap_true.
                lr_connectivity->hec_delete_visible = abap_true.
              ENDIF.

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_connectivity->hec_connectivity_guid IS NOT INITIAL AND
                                                                             lr_connectivity->hec_phase_guid   IS NOT INITIAL
                                                                        THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                        ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_connectivity->hec_instance_status.
                lr_connectivity->hec_instance_status = lv_inst_status.
                DATA(lv_data_changed) = abap_true.
              ENDIF.

              "-----------------------------------
              " Release instance for selection
              "-----------------------------------
              ASSIGN lt_datacenter[ key = lr_connectivity->parent_key ] TO FIELD-SYMBOL(<fs_datacenter>).

              IF <fs_datacenter> IS ASSIGNED.
                IF <fs_datacenter>-hec_datacenter_guid IS NOT INITIAL.
                  DATA(lv_release) = abap_true.
                ENDIF.
              ENDIF.

              IF lv_release <> lr_connectivity->hec_row_selectable.
                lr_connectivity->hec_row_selectable = lv_release.
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
                  is_node_data = lr_connectivity
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              IF lv_data_changed = abap_false.
                lv_data_changed = lv_cr_data_changed.
              ENDIF.

              "-----------------------------------
              " Modify
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_connectivity->key
                                   is_data = lr_connectivity ).
              ENDIF.

              UNASSIGN <fs_datacenter>.

              CLEAR: lv_inst_status,
                     lv_release,
                     lv_data_changed.

            ENDLOOP. " LOOP AT lt_connectivity REFERENCE INTO lr_connectivity.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-connectivity-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_connectivity_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).

            " Get parent node (datacenter)
            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-connectivity-to_parent
                                              IMPORTING et_data        = lt_datacenter ).


            LOOP AT lt_connectivity REFERENCE INTO lr_connectivity.

              ASSIGN lt_connectivity_before[ key = lr_connectivity->key ] TO FIELD-SYMBOL(<fs_connectivity_before>).
              IF <fs_connectivity_before> IS ASSIGNED.

                "-----------------------------------
                " Get connectivity pricing
                "-----------------------------------
                IF <fs_connectivity_before>-hec_connectivity_guid IS INITIAL      AND
                   lr_connectivity->hec_connectivity_guid         IS NOT INITIAL.

                  " There is only one parent node, so one datacenter
                  TRY.
                      DATA(ls_datacenter) = lt_datacenter[ key = lr_connectivity->parent_key ].

                      SELECT SINGLE hec_cb_pricing_lb_guid
                        FROM /hec1/i_connectivitylbbasic
                       WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid              AND
                             hec_connectivity_guid   = @lr_connectivity->hec_connectivity_guid  AND
                             hec_sec_datacenter_guid = @ls_datacenter-hec_datacenter_guid       AND
                             hec_infra_provider_guid = @lr_delivery_unit->hec_inf_provider_guid
                        INTO @DATA(lv_pricing_legoblock).


                      SELECT SINGLE *
                        FROM /hec1/c_cbp_lb   "#EC CI_ALL_FIELDS_NEEDED
                       WHERE hec_price_lb = @lv_pricing_legoblock
                        INTO @DATA(ls_pricing).

                      lr_connectivity->* = CORRESPONDING #( BASE ( lr_connectivity->* ) ls_pricing ).

                      lv_data_changed = abap_true.
                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.

                  "-----------------------------------
                  " Set Value List Quantity
                  "-----------------------------------
                  lr_connectivity->hec_connectivity_vlqt = COND #( WHEN 1 < lines( /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_connectivity(
                                                                                                     iv_apm_guid            = lr_landscape->hec_apm_guid
                                                                                                     iv_sec_datacenter_guid = lr_connectivity->hec_sec_datacenter_guid ) )
                                                                   THEN /hec1/if_config_constants=>gc_value_list_quantity-multi
                                                                   ELSE /hec1/if_config_constants=>gc_value_list_quantity-single ).

                ENDIF. " IF <fs_connectivity_before>-hec_connectivity_guid IS INITIAL

                "-----------------------------------
                " Get connectivity description
                "-----------------------------------
                IF lr_connectivity->hec_connectivity_guid  IS NOT INITIAL AND
                   lr_connectivity->hec_connectivity_descr IS INITIAL.

                  SELECT SINGLE hec_connectivity_descr
                    FROM /hec1/i_connectivitybasic
                   WHERE hec_apm_guid            = @lr_landscape->hec_apm_guid             AND
                         hec_connectivity_guid   = @lr_connectivity->hec_connectivity_guid
                    INTO @lr_connectivity->hec_connectivity_descr.

                  lr_connectivity->hec_tree_descr = lr_connectivity->hec_connectivity_descr. "#EC CI_FLDEXT_OK[2215424]
                  lv_data_changed                 = abap_true.

                ENDIF. " IF lr_connectivity->hec_connectivity_guid  IS NOT INITIAL

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_connectivity->hec_phase_guid NE <fs_connectivity_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_connectivity->key
                                  hec_phase_guid_new = lr_connectivity->hec_phase_guid
                                  hec_phase_guid_old = <fs_connectivity_before>-hec_phase_guid ) TO lt_act_param_phasing.

                  lr_connectivity->hec_phase_changed = abap_true.
                  lv_data_changed = abap_true.

                ENDIF. "Phase changed

                "-----------------------------------
                " Reset connectivity GUID - TODO action
                "-----------------------------------
                IF <fs_connectivity_before>-hec_connectivity_guid IS NOT INITIAL AND
                   lr_connectivity->hec_connectivity_guid     IS INITIAL.

                  CLEAR: lr_connectivity->descr,
                         lr_connectivity->hec_connectivity_guid,
                         lr_connectivity->hec_connectivity_descr,
                         lr_connectivity->hec_tree_descr,
                         lr_connectivity->price.

                  lv_data_changed = abap_true.
                ENDIF.
              ENDIF. "<fs_connectivity_before> is assigned.


              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_connectivity->hec_connectivity_guid IS NOT INITIAL AND
                                                                       lr_connectivity->hec_phase_guid   IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_connectivity->hec_instance_status.
                lr_connectivity->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.

              "-----------------------------------
              " Modify
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_connectivity->key
                                   is_data = lr_connectivity ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_connectivity_before>.

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

        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_man_serv_baseline_cr.

    RETURN. ">>>>

  ENDMETHOD.


  METHOD determine_infr_baseline_cr.

    DATA: lt_infr_baseline        TYPE /hec1/t_data_if_baseline_ct,
          lt_infr_baseline_before TYPE /hec1/t_data_if_baseline_ct,
          lt_phase                TYPE /hec1/t_data_phase_ct,
          lt_act_param_phasing    TYPE TABLE OF /hec1/s_act_phase_inherit.


    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_infr_baseline ).

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
          WHEN /hec1/if_configuration_c=>sc_determination-infrastructure_baseline-create.

            LOOP AT lt_infr_baseline REFERENCE INTO DATA(lr_infr_baseline).

              io_modify->update( iv_node = is_ctx-node_key
                                 iv_key  = lr_infr_baseline->key
                                 is_data = lr_infr_baseline ).

            ENDLOOP.

            " ***************************************************************************
            " update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-infrastructure_baseline-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_infr_baseline_before ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                        it_key         = VALUE #( ( key = lv_root_key ) )
                                                        iv_fill_data   = abap_true
                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                              IMPORTING et_data        = lt_phase ).


            LOOP AT lt_infr_baseline REFERENCE INTO lr_infr_baseline.

              ASSIGN lt_infr_baseline_before[ key = lr_infr_baseline->key ] TO FIELD-SYMBOL(<fs_infr_baseline_before>).
              IF <fs_infr_baseline_before> IS ASSIGNED.

                "-----------------------------------
                " Phasing has changed
                "-----------------------------------
                IF lr_infr_baseline->hec_phase_guid NE <fs_infr_baseline_before>-hec_phase_guid.

                  APPEND VALUE #( hec_node_key       = is_ctx-node_key
                                  hec_bopf_key       = lr_infr_baseline->key
                                  hec_phase_guid_new = lr_infr_baseline->hec_phase_guid
                                  hec_phase_guid_old = <fs_infr_baseline_before>-hec_phase_guid ) TO lt_act_param_phasing.

                ENDIF. "phasing changed
              ENDIF. " IF <fs_infr_baseline_before> IS ASSIGNED.

              UNASSIGN <fs_infr_baseline_before>.

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

        ENDCASE.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_contact_cr.

    DATA: lt_contact        TYPE /hec1/t_data_contact_ct,
          lt_contact_before TYPE /hec1/t_data_contact_ct.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_contact ).

    io_read->get_root_key( EXPORTING iv_node       = is_ctx-node_key
                                     it_key        = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create Mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-contact-create.

            LOOP AT lt_contact REFERENCE INTO DATA(lr_contact).

*            IF lv_data_changed = abap_true.
*              io_modify->update( iv_node = is_ctx-node_key
*                                 iv_key  = lr_phase->key
*                                 is_data = lr_phase   ).
*            ENDIF.
*
*            CLEAR: lv_data_changed.

            ENDLOOP.

            " ***************************************************************************
            " Update Mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-contact-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                                         iv_fill_data    = abap_true
                               IMPORTING et_data         = lt_contact_before ).

            LOOP AT lt_contact REFERENCE INTO lr_contact.
              ASSIGN lt_contact_before[ key = lr_contact->key ] TO FIELD-SYMBOL(<fs_contact_before>).

              IF <fs_contact_before> IS ASSIGNED.

              ENDIF. "<fs_contact_before> is assigned.

*              IF lv_data_changed = abap_true.
*                io_modify->update( iv_node = is_ctx-node_key
*                                   iv_key  = lr_phase->key
*                                   is_data = lr_phase   ).
*              ENDIF.
*
*              CLEAR: lv_data_changed.

              UNASSIGN <fs_contact_before>.

            ENDLOOP. "lt_contact
        ENDCASE. "is_ctx

      CATCH /bobf/cx_frw.
      CATCH cx_uuid_error. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD determine_delivery_unit_cr.

    DATA: lt_delivery_unit               TYPE /hec1/t_data_dlvy_unit_ct,
          lt_delivery_unit_before        TYPE /hec1/t_data_dlvy_unit_ct,
          lt_phase                       TYPE /hec1/t_data_phase_ct,
          lt_landscape                   TYPE /hec1/t_config_root_ct,
          lt_managed_service_baseline    TYPE /hec1/t_data_man_serv_basel_ct,
          lt_act_param_man_serv_baseline TYPE /bobf/t_frw_key,
          lt_act_param_datacenter        TYPE /hec1/t_act_update_datacenter,
          lt_act_param                   TYPE TABLE OF /bobf/s_frw_key,
          lt_modification                TYPE /bobf/t_frw_modification.

    CLEAR: eo_message,
           et_failed_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_delivery_unit ).


    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-delivery_unit-create.

            " there is only always one delivery unit
            TRY.
                DATA(lr_delivery_unit) = NEW /hec1/s_data_dlvy_unit_cs( lt_delivery_unit[ 1 ] ).
              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

            " get landscape = root
            io_read->retrieve( EXPORTING iv_node = /hec1/if_configuration_c=>sc_node-root
                                         it_key  = VALUE #( ( key = lr_delivery_unit->root_key ) )
                               IMPORTING et_data = lt_landscape ).

            " there is only one landscape
            TRY.
                DATA(ls_landscape) = lt_landscape[ 1 ].
              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

            "-----------------------------------
            " Set Value List Quantity
            "-----------------------------------
            " Later we might need to adjust this logic, if for some reason the number of entries can change
            lr_delivery_unit->hec_delivery_unit_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.
            lr_delivery_unit->hec_inf_provider_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.

*            " get default phase
*            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
*                                                        it_key         = VALUE #( ( key = lr_delivery_unit->root_key ) )
*                                                        iv_fill_data   = abap_true
*                                                        iv_association = /hec1/if_configuration_c=>sc_association-root-phase
*                                              IMPORTING et_data        = lt_phase ).
*
*            TRY.
*                DATA(ls_phase) = lt_phase[ hec_default_phase = abap_true ].
*              CATCH cx_sy_itab_line_not_found.
*            ENDTRY.

            lr_delivery_unit->hec_delete_visible = abap_false.

            "-----------------------------------
            " Check instance status and switch
            "-----------------------------------
            DATA(lv_inst_status) = COND /hec1/config_instance_status( WHEN lr_delivery_unit->hec_delivery_unit_guid     IS NOT INITIAL AND
                                                                           lr_delivery_unit->hec_delivery_unit_category IS NOT INITIAL AND
                                                                           lr_delivery_unit->hec_inf_provider_guid      IS NOT INITIAL AND
                                                                           lr_delivery_unit->hec_inf_provider_category  IS NOT INITIAL
                                                                      THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                      ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

            IF lv_inst_status <> lr_delivery_unit->hec_instance_status.
              lr_delivery_unit->hec_instance_status = lv_inst_status.
              DATA(lv_data_changed) = abap_true.
            ENDIF.


            "-----------------------------------
            " Modify delivery unit
            "-----------------------------------
            IF lv_data_changed = abap_true.
              io_modify->update( iv_node = is_ctx-node_key
                                 iv_key  = lr_delivery_unit->key
                                 is_data = lr_delivery_unit ).
            ENDIF.

            "-----------------------------------
            " Set create Datacenter
            " action to general
            "-----------------------------------
            /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys_direct(
              is_ctx          = CORRESPONDING #( is_ctx )
              it_key          = it_key
              iv_action       = /hec1/if_configuration_c=>sc_action-delivery_unit-create_datacenter
              iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation ).


            " ***************************************************************************´
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-delivery_unit-update.

            io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                         it_key          = it_key
                                         iv_before_image = abap_true
                               IMPORTING et_data         = lt_delivery_unit_before ).


            SELECT *                          "#EC CI_ALL_FIELDS_NEEDED
              FROM /hec1/i_deliveryunitbasic
              INTO TABLE @DATA(lt_fdt_delivery_unit).   "#EC CI_NOWHERE

            SELECT *                          "#EC CI_ALL_FIELDS_NEEDED
              FROM /hec1/i_infraproviderbasic
              INTO TABLE @DATA(lt_fdt_infra_provider).  "#EC CI_NOWHERE



            LOOP AT lt_delivery_unit REFERENCE INTO lr_delivery_unit.
              ASSIGN lt_delivery_unit_before[ 1 ] TO FIELD-SYMBOL(<fs_delivery_unit_before>).

              IF <fs_delivery_unit_before> IS ASSIGNED.
                "-----------------------------------
                " Delivery unit has changed
                "-----------------------------------
                IF lr_delivery_unit->hec_delivery_unit_guid IS NOT INITIAL                        AND
                   lr_delivery_unit->hec_delivery_unit_guid <> <fs_delivery_unit_before>-hec_delivery_unit_guid.

                  DATA(ls_delivery_unit) = VALUE #( lt_fdt_delivery_unit[ hec_delivery_unit_guid = lr_delivery_unit->hec_delivery_unit_guid ] OPTIONAL ).

                  lr_delivery_unit->hec_delivery_unit_descr    = ls_delivery_unit-hec_delivery_unit_descr.
                  lr_delivery_unit->hec_delivery_unit_category = ls_delivery_unit-hec_delivery_unit_cat_value.
                  lr_delivery_unit->hec_sec_dlvy_unit_guid     = ls_delivery_unit-hec_sec_dlvy_unit_guid.
                  lr_delivery_unit->hec_tree_descr             = ls_delivery_unit-hec_delivery_unit_descr.

                  SELECT *
                    FROM @lt_fdt_infra_provider AS inf_prov
                    WHERE inf_prov~hec_delivery_unit_guid = @lr_delivery_unit->hec_delivery_unit_guid
                    INTO TABLE @DATA(lt_infra_provider).

                  IF lines( lt_infra_provider ) = 1.
                    DATA(ls_infra_provider) = VALUE #( lt_infra_provider[ 1 ] OPTIONAL ).
                    lr_delivery_unit->hec_inf_provider_guid = ls_infra_provider-hec_infra_provider_guid.
                  ENDIF.

                  lv_data_changed = abap_true.

                  " Set Value List Quantity
                  " Later we might need to adjust this logic, if for some reason the number of entries can change
                  lr_delivery_unit->hec_delivery_unit_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.
                  lr_delivery_unit->hec_inf_provider_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.

                  " Update datacenter search fields
                  INSERT VALUE #( BASE CORRESPONDING #( lr_delivery_unit->* )
                                       do_update_search_fields = abap_true ) INTO TABLE lt_act_param_datacenter.

                ENDIF.

                "-----------------------------------
                " Infrastructure Provider has changed
                "-----------------------------------
                IF lr_delivery_unit IS NOT INITIAL                                                             AND
                   lr_delivery_unit->hec_inf_provider_guid <> <fs_delivery_unit_before>-hec_inf_provider_guid.
                  TRY.
                      ls_infra_provider = lt_fdt_infra_provider[ hec_infra_provider_guid = lr_delivery_unit->hec_inf_provider_guid ].

                      lr_delivery_unit->hec_inf_provider_descr    = ls_infra_provider-hec_inf_provider_descr.
                      lr_delivery_unit->hec_sec_infra_prov_guid   = ls_infra_provider-hec_sec_infra_prov_guid.
                      lr_delivery_unit->hec_inf_provider_category = ls_infra_provider-hec_inf_provider_cat_value.

                      lv_data_changed                             = abap_true.

                      SELECT *
                        FROM @lt_fdt_infra_provider AS inf_prov
                        WHERE inf_prov~hec_infra_provider_guid = @lr_delivery_unit->hec_inf_provider_guid
                        INTO TABLE @lt_infra_provider.

                      IF lines( lt_infra_provider ) = 1.
                        ls_infra_provider = VALUE #( lt_infra_provider[ 1 ] OPTIONAL ).
                        lr_delivery_unit->hec_delivery_unit_guid = ls_infra_provider-hec_delivery_unit_guid.

                        ls_delivery_unit = VALUE #( lt_fdt_delivery_unit[ hec_delivery_unit_guid = ls_infra_provider-hec_delivery_unit_guid ] OPTIONAL ).

                        lr_delivery_unit->hec_delivery_unit_descr    = ls_delivery_unit-hec_delivery_unit_descr.
                        lr_delivery_unit->hec_delivery_unit_category = ls_delivery_unit-hec_delivery_unit_cat_value.
                        lr_delivery_unit->hec_sec_dlvy_unit_guid     = ls_delivery_unit-hec_sec_dlvy_unit_guid.
                        lr_delivery_unit->hec_tree_descr             = ls_delivery_unit-hec_delivery_unit_descr.
                      ENDIF.

                      " Set Value List Quantity
                      " Later we might need to adjust this logic, if for some reason the number of entries can change
                      lr_delivery_unit->hec_inf_provider_vlqt = /hec1/if_config_constants=>gc_value_list_quantity-multi.

                      "-----------------------------------
                      " Fill action table for update
                      " data center
                      "-----------------------------------
                      INSERT VALUE #( BASE CORRESPONDING #( lr_delivery_unit->* )
                                      do_update_search_fields = abap_true         ) INTO TABLE lt_act_param_datacenter.

                    CATCH cx_sy_itab_line_not_found.
                  ENDTRY.
                ENDIF. " IF lr_delivery_unit IS NOT INITIAL AND...

                "-----------------------------------
                " Update managed service baseline
                "-----------------------------------
                IF ( lr_delivery_unit->hec_delivery_unit_guid     IS NOT INITIAL AND
                     lr_delivery_unit->hec_delivery_unit_category IS NOT INITIAL AND
                     lr_delivery_unit->hec_inf_provider_guid      IS NOT INITIAL AND
                     lr_delivery_unit->hec_inf_provider_category  IS NOT INITIAL     )                                        AND
                   ( lr_delivery_unit->hec_delivery_unit_guid     <> <fs_delivery_unit_before>-hec_delivery_unit_guid     OR
                     lr_delivery_unit->hec_delivery_unit_category <> <fs_delivery_unit_before>-hec_delivery_unit_category OR
                     lr_delivery_unit->hec_inf_provider_guid      <> <fs_delivery_unit_before>-hec_inf_provider_guid      OR
                     lr_delivery_unit->hec_inf_provider_category  <> <fs_delivery_unit_before>-hec_inf_provider_category     ).

                  "-----------------------------------
                  " Fill action table for update
                  " managed service baseline
                  "-----------------------------------
                  IF NOT line_exists( lt_act_param_man_serv_baseline[ key = lr_delivery_unit->key ] ).
                    INSERT VALUE #( key = lr_delivery_unit->key ) INTO TABLE lt_act_param_man_serv_baseline.
                  ENDIF.
                ENDIF.

                "-----------------------------------
                " Reset -> Update Datacenter fields
                "-----------------------------------
                IF lr_delivery_unit->hec_delivery_unit_guid         IS     INITIAL AND
                   <fs_delivery_unit_before>-hec_delivery_unit_guid IS NOT INITIAL OR
                   lr_delivery_unit->hec_inf_provider_guid          IS     INITIAL AND
                  <fs_delivery_unit_before>-hec_inf_provider_guid   IS NOT INITIAL.

                  IF lr_delivery_unit->hec_delivery_unit_guid IS INITIAL.
                    CLEAR: lr_delivery_unit->hec_delivery_unit_category,
                           lr_delivery_unit->hec_delivery_unit_descr.
                  ENDIF.

                  IF lr_delivery_unit->hec_inf_provider_guid IS INITIAL.
                    CLEAR: lr_delivery_unit->hec_inf_provider_category,
                           lr_delivery_unit->hec_inf_provider_descr.
                  ENDIF.

                  lv_data_changed = abap_true.

                  "-----------------------------------
                  " Fill action table for update
                  " data center
                  "-----------------------------------
                  INSERT VALUE #( BASE CORRESPONDING #( lr_delivery_unit->* )
                                       do_reset = abap_true ) INTO TABLE lt_act_param_datacenter.

                ENDIF. " IF lr_delivery_unit->hec_delivery_unit_guid IS INITIAL AND...
              ENDIF. "If <fs_delivery_unit_before> is assigned

              "-----------------------------------
              " Check instance status and switch
              "-----------------------------------
              lv_inst_status = COND /hec1/config_instance_status( WHEN lr_delivery_unit->hec_delivery_unit_guid     IS NOT INITIAL AND
                                                                       lr_delivery_unit->hec_delivery_unit_category IS NOT INITIAL AND
                                                                       lr_delivery_unit->hec_inf_provider_guid      IS NOT INITIAL AND
                                                                       lr_delivery_unit->hec_inf_provider_category  IS NOT INITIAL
                                                                  THEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                  ELSE /hec1/if_config_constants=>gc_instance_status-incomplete ).

              IF lv_inst_status <> lr_delivery_unit->hec_instance_status.
                lr_delivery_unit->hec_instance_status = lv_inst_status.
                lv_data_changed = abap_true.
              ENDIF.


              "-----------------------------------
              " Modify delivery unit
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_delivery_unit->key
                                   is_data = lr_delivery_unit ).
              ENDIF.

              CLEAR: lv_inst_status,
                     lv_data_changed.

              UNASSIGN <fs_delivery_unit_before>.
            ENDLOOP.
        ENDCASE.


        "-----------------------------------
        " Set Update datacenter
        " action to general
        "-----------------------------------
        IF lt_act_param_datacenter IS NOT INITIAL.
          me->mr_act_param = NEW /hec1/t_act_update_datacenter( lt_act_param_datacenter ).

          /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
              is_ctx          = CORRESPONDING #( is_ctx )
              it_key          = it_key
              iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_datacenter )
              iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
              ir_act_param    = mr_act_param  ).
        ENDIF.

        "-----------------------------------
        " Set update managed service
        " baseline action to GENERAL
        "-----------------------------------
        IF lt_act_param_man_serv_baseline IS NOT INITIAL.
          /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
              is_ctx          = CORRESPONDING #( is_ctx )
              it_key          = lt_act_param_man_serv_baseline
              iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_man_serv_baseline )
              iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation                                                                                                ).
        ENDIF.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD determine_transport_path.

    DATA: lt_transport_path        TYPE /hec1/t_data_transport_path_ct,
          lt_transport_path_before TYPE /hec1/t_data_transport_path_ct,
          lt_tier                  TYPE /hec1/t_data_tier_ct.

    CLEAR: eo_message,
           et_failed_key.

    " Data before update
    io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                 it_key          = it_key
                                 iv_before_image = abap_true
                       IMPORTING et_data         = lt_transport_path_before ).

    " Data after update
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_transport_path ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit)
                                                        et_datacenter    = DATA(lt_datacenter) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-transport_path-create.
            LOOP AT lt_transport_path REFERENCE INTO DATA(lr_transport_path).

              lr_transport_path->hec_delete_visible = abap_true.

              "-----------------------------------
              " Modify tier
              "-----------------------------------
              io_modify->update( iv_node = is_ctx-node_key
                                 iv_key  = lr_transport_path->key
                                 is_data = lr_transport_path ).

            ENDLOOP.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-transport_path-update.

            io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                        it_key         = it_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-transport_path-to_parent
                                              IMPORTING et_target_key  = DATA(lt_solution_key) ).

            io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-solution
                                                        it_key         = lt_solution_key
                                                        iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                                        iv_fill_data   = abap_true
                                              IMPORTING et_data        = lt_tier ).

            LOOP AT lt_transport_path REFERENCE INTO lr_transport_path.

              ASSIGN lt_transport_path_before[ key = lr_transport_path->key ] TO FIELD-SYMBOL(<fs_transport_path_before>).
              IF <fs_transport_path_before> IS ASSIGNED.

                "-----------------------------------
                " Source Tier was changed
                "-----------------------------------
                IF lr_transport_path->hec_source_tier <> <fs_transport_path_before>-hec_source_tier.
                  " clear the client, because only clients
                  " for the selected tier are possible
                  CLEAR lr_transport_path->hec_source_client.

                  " change source SID
                  lr_transport_path->hec_source_sid = VALUE #( lt_tier[ hec_node_tier = lr_transport_path->hec_source_tier ]-hec_tier_sid OPTIONAL ).
                  DATA(lv_data_changed) = abap_true.

                ENDIF.

                "-----------------------------------
                " Target Tier was changed
                "-----------------------------------
                IF lr_transport_path->hec_target_tier <> <fs_transport_path_before>-hec_target_tier.
                  " clear the client, because only clients
                  " for the selected tier are possible
                  CLEAR lr_transport_path->hec_target_client.

                  " change target SID
                  lr_transport_path->hec_target_sid = VALUE #( lt_tier[ hec_node_tier = lr_transport_path->hec_target_tier ]-hec_tier_sid OPTIONAL ).
                  lv_data_changed = abap_true.

                ENDIF.

              ENDIF. "<fs_tier_sla_before> is assigned

              "-----------------------------------
              " Modify tier sla
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_transport_path->key
                                   is_data = lr_transport_path ).
              ENDIF.

              CLEAR: lv_data_changed.

              UNASSIGN: <fs_transport_path_before>.
            ENDLOOP. " LOOP AT lt_tier_sla REFERENCE INTO lr_tier_sla.

        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD determine_transport_path_cr.

    DATA: lt_transport_path        TYPE /hec1/t_data_transport_path_ct,
          lt_transport_path_before TYPE /hec1/t_data_transport_path_ct.

    CLEAR: eo_message,
           et_failed_key.

    " Data before update
    io_read->retrieve( EXPORTING iv_node         = is_ctx-node_key
                                 it_key          = it_key
                                 iv_before_image = abap_true
                       IMPORTING et_data         = lt_transport_path_before ).

    " Data after update
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_transport_path ).

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_delivery_unit)
                                                        et_datacenter    = DATA(lt_datacenter) ).

    TRY.
        CASE is_ctx-det_key.
            " ***************************************************************************
            " Create mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-transport_path-create.
            LOOP AT lt_transport_path REFERENCE INTO DATA(lr_transport_path).

              lr_transport_path->hec_delete_visible = abap_true.

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
                  is_node_data = lr_transport_path
                  iv_set_apm   = abap_true
                  iv_clear_phase = abap_true
              ).

              "-----------------------------------
              " Modify tier
              "-----------------------------------
              io_modify->update( iv_node = is_ctx-node_key
                                 iv_key  = lr_transport_path->key
                                 is_data = lr_transport_path ).

            ENDLOOP.

            " ***************************************************************************
            " Update mode
            " ***************************************************************************
          WHEN /hec1/if_configuration_c=>sc_determination-transport_path-update.
            LOOP AT lt_transport_path REFERENCE INTO lr_transport_path.

              ASSIGN lt_transport_path_before[ key = lr_transport_path->key ] TO FIELD-SYMBOL(<fs_transport_path_before>).
              IF <fs_transport_path_before> IS ASSIGNED.

                DATA(lv_data_changed) = abap_true.

              ENDIF. "<fs_tier_sla_before> is assigned

              "-----------------------------------
              " Modify tier sla
              "-----------------------------------
              IF lv_data_changed = abap_true.
                io_modify->update( iv_node = is_ctx-node_key
                                   iv_key  = lr_transport_path->key
                                   is_data = lr_transport_path ).
              ENDIF.

              CLEAR: lv_data_changed.

              UNASSIGN: <fs_transport_path_before>.
            ENDLOOP. " LOOP AT lt_tier_sla REFERENCE INTO lr_tier_sla.

        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD modify_aggre_mod_type.

    DATA: lt_modification  TYPE /bobf/t_frw_modification.

    DATA: l_mod_type TYPE /hec1/comp_mod_type.

    DATA: para              TYPE tpara-paramid VALUE '/HEC1/CONFIG_DEBUG',
          ls_debug_own_code TYPE /hec1/s_config_debug_modus.

    GET PARAMETER ID para FIELD ls_debug_own_code.

    "Safety first
*    IF ls_debug_own_code-hec_debug_modus      = abap_true AND "Todo (remove before transport  )
*       ls_debug_own_code-hec_debuf_modus_vers = '09'.

    CHECK is_ctx-node_key = /hec1/if_configuration_c=>sc_node-root.

    /hec1/cl_config_helper=>get_price_relevant_node_data( EXPORTING is_ctx                   = CORRESPONDING #( is_ctx )
                                                                    it_key                   = it_key
                                                                    io_read                  = io_read
                                                          IMPORTING et_landscape             = DATA(lt_landscape)
                                                                    et_tier                  = DATA(lt_tier)
                                                                    et_lt_backup_datacenter  = DATA(lt_lt_backup_datacenter)
                                                                    et_tier_price_phase      = DATA(lt_tier_price_phase)
                                                                    et_landsc_price_phase    = DATA(lt_landscape_price_phase)
                                                                    et_connect_price_phase   = DATA(lt_connectivity_price_phase)
                                                                    et_service_price_phase   = DATA(lt_add_service_price_phase)
                                                                    et_lt_backup_price_phase = DATA(lt_lt_backup_price_phase)
                                                                   ).


    DATA(ls_landscape) = VALUE #( lt_landscape[ 1 ] OPTIONAL ).

    CHECK: ls_landscape IS NOT INITIAL.

    "-----------------------------------
    "Get complete Configuration in unified format for easier handling
    "-----------------------------------
    /hec1/cl_rep_config_data=>read_config_data( EXPORTING i_config_id       = ls_landscape-hec_confid
                                                          i_config_version  = ls_landscape-hec_conf_version
                                                IMPORTING es_config_head    = DATA(ls_config_head)
                                                          et_config_data    = DATA(lt_config_data)
                                                          et_cfg_price_data = DATA(lt_price_data)
                                                          e_subrc           = DATA(l_subrc) ).

    "-----------------------------------
    "Check if Connectivity Node is modified, if yes -> write Modification type into all linked aggr. connectivity price phase objects
    "-----------------------------------
    LOOP AT lt_config_data[] ASSIGNING FIELD-SYMBOL(<ls_connectivity>) WHERE level_id = /hec1/cl_rep_config_data=>c_level_connectivity.
      IF <ls_connectivity>-hec_comp_mod_type IS NOT INITIAL.
        LOOP AT lt_connectivity_price_phase REFERENCE INTO DATA(lr_connectivity_price_phase) WHERE hec_node_connectivity = <ls_connectivity>-hec_node_id.
          lr_connectivity_price_phase->hec_aggr_mod_type = <ls_connectivity>-hec_comp_mod_type.
          lr_connectivity_price_phase->hec_aggr_modified = abap_true.

          INSERT VALUE #( data        = lr_connectivity_price_phase
                          node        = /hec1/if_configuration_c=>sc_node-connectivity_price_phase
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_connectivity_price_phase->key                           ) INTO TABLE lt_modification.
        ENDLOOP.
      ENDIF.
    ENDLOOP.

    "-----------------------------------
    "Check if Additional Service is modified, if yes -> write Modification type into all linked price phase objects
    "-----------------------------------
    LOOP AT lt_config_data[] ASSIGNING FIELD-SYMBOL(<ls_add_service>) WHERE level_id = /hec1/cl_rep_config_data=>c_level_service.
      IF <ls_add_service>-hec_comp_mod_type IS NOT INITIAL.
        LOOP AT lt_add_service_price_phase REFERENCE INTO DATA(lr_add_service_price_phase) WHERE hec_node_service = <ls_add_service>-hec_node_id.
          lr_add_service_price_phase->hec_aggr_mod_type = <ls_add_service>-hec_comp_mod_type.
          lr_add_service_price_phase->hec_aggr_modified = abap_true.

          INSERT VALUE #( data        = lr_add_service_price_phase
                          node        = /hec1/if_configuration_c=>sc_node-add_service_price_phase
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_add_service_price_phase->key                           ) INTO TABLE lt_modification.
        ENDLOOP.
      ENDIF.
    ENDLOOP.


    LOOP AT lt_config_data[] ASSIGNING FIELD-SYMBOL(<ls_tier_data>)
      WHERE level_id = /hec1/cl_rep_config_data=>c_level_tier.

      CLEAR: l_mod_type.

*      READ TABLE lt_tier ASSIGNING FIELD-SYMBOL(<ls_tier>) WITH KEY hec_node_solution = <ls_tier_data>-hec_node_solution hec_node_tier = <ls_tier_data>-hec_node_tier.
*      IF sy-subrc <> 0.
*        EXIT.
*      ENDIF.

      DATA(lt_tier_subtree_data) = /hec1/cl_rep_config_data=>get_subtree( EXPORTING it_config_data = lt_config_data[]
                                                                                    i_row_id       = <ls_tier_data>-row_id ).

*      DATA(lr_tier) = NEW /hec1/s_data_tier_cs( CORRESPONDING #( <ls_tier> ) ) .

      IF <ls_tier_data>-hec_comp_mod_type IS NOT INITIAL.
        l_mod_type = <ls_tier_data>-hec_comp_mod_type.
      ELSE.
        LOOP AT lt_tier_subtree_data ASSIGNING FIELD-SYMBOL(<ls_tier_subtree>).
          CASE <ls_tier_subtree>-hec_comp_mod_type.
            WHEN '01'. "01 Added
              l_mod_type = '02'. "02 Changed
              EXIT.
            WHEN '02'. "02 Changed
              l_mod_type = '02'. "02 Changed
              EXIT.
            WHEN '03'. "03 Deleted
              l_mod_type = '02'. "02 Changed
              EXIT.
            WHEN '04'. "04 Retired
              l_mod_type = '02'. "02 Changed
              EXIT.
            WHEN '05'. "05 Replaced
              l_mod_type = '02'. "02 Changed
              EXIT.
            WHEN '06'. "06 Phase shifted
              l_mod_type = '02'. "02 Changed
              EXIT.
            WHEN '07'. "07 Reconfigured
              l_mod_type = '02'. "02 Changed
              EXIT.
          ENDCASE.
        ENDLOOP.


      ENDIF.

      IF l_mod_type IS NOT INITIAL.
        LOOP AT lt_tier_price_phase REFERENCE INTO DATA(lr_tier_price_phase) WHERE hec_node_tier = <ls_tier_data>-hec_node_tier.
          lr_tier_price_phase->hec_aggr_mod_type = l_mod_type.
          lr_tier_price_phase->hec_aggr_modified = abap_true.

          INSERT VALUE #( data        = lr_tier_price_phase
                          node        = /hec1/if_configuration_c=>sc_node-tier_price_phase
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_tier_price_phase->key                           ) INTO TABLE lt_modification.
        ENDLOOP.
      ENDIF.
    ENDLOOP.


    LOOP AT lt_config_data[] ASSIGNING FIELD-SYMBOL(<ls_config_data_ltb_cl>)
      WHERE level_id = /hec1/cl_rep_config_data=>c_level_ltb_class.

      CLEAR: l_mod_type.

*      READ TABLE lt_lt_backup_datacenter ASSIGNING FIELD-SYMBOL(<ls_ltb_dc>) WITH KEY hec_node_lt_backup_dc = <ls_config_data_ltb_dc>-hec_node_id.
*      IF sy-subrc <> 0.
*        EXIT.
*      ENDIF.

      DATA(lt_ltb_cl_subtree_data) = /hec1/cl_rep_config_data=>get_subtree( EXPORTING it_config_data = lt_config_data[]
                                                                                      i_row_id       = <ls_config_data_ltb_cl>-row_id ).

*      DATA(lr_ltb_dc) = NEW /hec1/s_data_lt_backup_dc_cs( CORRESPONDING #( <ls_ltb_dc> ) ) .

      IF <ls_config_data_ltb_cl>-hec_comp_mod_type IS NOT INITIAL.
        l_mod_type = <ls_config_data_ltb_cl>-hec_comp_mod_type.
      ELSE.
        LOOP AT lt_ltb_cl_subtree_data ASSIGNING FIELD-SYMBOL(<ls_ltb_cl_subtree>).
          CASE <ls_ltb_cl_subtree>-hec_comp_mod_type.

            WHEN '01'. "01 Added
              l_mod_type = '02'. "02 Changed
              EXIT.
            WHEN '02'. "02 Changed
              l_mod_type = '02'. "02 Changed
              EXIT.
            WHEN '03'. "03 Deleted
              l_mod_type = '02'. "02 Changed
              EXIT.
            WHEN '04'. "04 Retired
              l_mod_type = '02'. "02 Changed
              EXIT.
            WHEN '05'. "05 Replaced
              l_mod_type = '02'. "02 Changed
              EXIT.
            WHEN '06'. "06 Phase shifted
              l_mod_type = '02'. "02 Changed
              EXIT.
            WHEN '07'. "07 Reconfigured
              l_mod_type = '02'. "02 Changed
              EXIT.
          ENDCASE.
        ENDLOOP.
      ENDIF.

      IF l_mod_type IS NOT INITIAL.
        LOOP AT lt_lt_backup_price_phase REFERENCE INTO DATA(lr_lt_backup_price_phase) WHERE hec_node_lt_backup_class = <ls_config_data_ltb_cl>-hec_node_id.
          lr_lt_backup_price_phase->hec_aggr_mod_type = l_mod_type.
          lr_lt_backup_price_phase->hec_aggr_modified = abap_true.

          INSERT VALUE #( data        = lr_lt_backup_price_phase
                          node        = /hec1/if_configuration_c=>sc_node-lt_backup_price_phase
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_lt_backup_price_phase->key                           ) INTO TABLE lt_modification.
        ENDLOOP.
      ENDIF.

    ENDLOOP.


    "-----------------------------------
    " Modify instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change) ).
    ENDIF.

*    ENDIF.

  ENDMETHOD.
ENDCLASS.