CLASS /hec1/cl_config_det_field_prop DEFINITION
  PUBLIC
  INHERITING FROM /hec1/cl_lib_d_superclass
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.


  PROTECTED SECTION.

    METHODS execute
        REDEFINITION .

  PRIVATE SECTION.

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
ENDCLASS.



CLASS /HEC1/CL_CONFIG_DET_FIELD_PROP IMPLEMENTATION.


  METHOD determine_app_server_instance.
*return.
    DATA: lt_app_serv_inst TYPE /hec1/t_data_app_serv_inst_ct.


    CLEAR: eo_message,
           et_failed_key.

    TRY.
        io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                     it_key  = it_key
                           IMPORTING et_data = lt_app_serv_inst ).

        " Create a property helper class instance
        DATA(lo_property_helper) = NEW /bobf/cl_lib_h_set_property( is_context = is_ctx
                                                                    io_modify  = io_modify ).


        LOOP AT lt_app_serv_inst ASSIGNING FIELD-SYMBOL(<fs_app_serv_inst>).

          " Set all sub nodes of app server instance to update enabled/disabled
          lo_property_helper->set_nodesubtree_update_enabled( iv_key   = <fs_app_serv_inst>-key
                                                              iv_value = COND #( WHEN "<fs_app_serv_inst>-hec_app_srv_guid            IS NOT INITIAL AND
                                                                                      <fs_app_serv_inst>-hec_operating_sys_value IS NOT INITIAL AND
                                                                                      <fs_app_serv_inst>-hec_app_cluster_type_value  IS NOT INITIAL
                                                                                 THEN abap_true
                                                                                 ELSE abap_false                                                         ) ).

*          " Set actions enabled/disabled
*          lo_property_helper->set_action_enabled( iv_action_key = /hec1/if_configuration_c=>sc_action-app_node-sync_config
*                                                  iv_key        = <fs_app_serv_inst>-key
*                                                  iv_value      = COND #( WHEN <fs_app_serv_inst>-hec_app_srv_guid            IS NOT INITIAL AND
*                                                                               <fs_app_serv_inst>-hec_asi_operating_sys_value IS NOT INITIAL AND
*                                                                               <fs_app_serv_inst>-hec_app_cluster_type_value  IS NOT INITIAL
*                                                                          THEN abap_true
*                                                                          ELSE abap_false                                                         ) ).


        ENDLOOP.


      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.


  ENDMETHOD.


  METHOD execute.

    CLEAR: eo_message,
           et_failed_key.

    TRY.

        CASE is_ctx-det_key.

          WHEN /hec1/if_configuration_c=>sc_determination-solution-action_and_field_prop.
*


            " **********************************
            " Determine App server instance node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_determination-app_server_instance-action_and_field_prop.

            me->determine_app_server_instance( EXPORTING is_ctx        = is_ctx                           " Context Information for Determinations
                                                         it_key        = it_key                           " Key Table
                                                         io_read       = io_read                          " Interface to Reading Data
                                                         io_modify     = io_modify                        " Interface to Change Data
                                               IMPORTING eo_message    = eo_message                       " Message Object
                                                         et_failed_key = et_failed_key ).                 " Key Table

        ENDCASE.

      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.

  ENDMETHOD.
ENDCLASS.