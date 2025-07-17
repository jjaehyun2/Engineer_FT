CLASS /hec1/cl_config_action DEFINITION
  PUBLIC
  INHERITING FROM /hec1/cl_lib_a_superclass
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.

    METHODS /bobf/if_frw_action~execute
        REDEFINITION .
  PROTECTED SECTION.
  PRIVATE SECTION.

    DATA mr_act_param_delete TYPE REF TO data .
    DATA mr_act_param TYPE REF TO data .
    DATA mr_act_param_phase TYPE REF TO data .
    DATA mr_act_param_solution TYPE REF TO data .
    DATA mr_act_param_tier TYPE REF TO data .
    DATA mr_act_param_db_node TYPE REF TO data .
    DATA mr_act_param_db_serv_pc TYPE REF TO data .
    DATA mr_act_param_db_storage TYPE REF TO data .
    DATA mr_act_param_app_node TYPE REF TO data .
    DATA mr_act_param_app_serv_pc TYPE REF TO data .
    DATA mr_act_param_app_storage TYPE REF TO data .
    DATA mr_act_param_db_backup TYPE REF TO data .
    DATA mr_act_param_app_backup TYPE REF TO data .
    DATA mr_act_param_db_storage_qty TYPE REF TO data .
    DATA mr_act_param_app_storage_qty TYPE REF TO data .

    METHODS apm_change
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS apm_change_cr
      IMPORTING
        !io_modify     TYPE REF TO /bobf/if_frw_modify
        !io_read       TYPE REF TO /bobf/if_frw_read
        !it_key        TYPE /bobf/t_frw_key
        !is_ctx        TYPE /bobf/s_frw_ctx_act
        !is_parameters TYPE /hec1/s_act_apm_change
      EXPORTING
        !et_data       TYPE INDEX TABLE
      RAISING
        /bobf/cx_frw_contrct_violation
        /hec1/cx_copy_control
        /hec1/cx_standard_exception .
    METHODS apm_change_init_deal
      IMPORTING
        !io_modify     TYPE REF TO /bobf/if_frw_modify
        !io_read       TYPE REF TO /bobf/if_frw_read
        !it_key        TYPE /bobf/t_frw_key
        !is_ctx        TYPE /bobf/s_frw_ctx_act
        !is_parameters TYPE /hec1/s_act_apm_change
      EXPORTING
        !et_data       TYPE INDEX TABLE
      RAISING
        /bobf/cx_frw_contrct_violation
        /hec1/cx_copy_control
        /hec1/cx_standard_exception .
    METHODS check_apm_validity
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS clone_cr
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS convert_currency
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS copy_node
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS copy_to_new_config
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS create_add_service
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS create_connectivity
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS create_contact
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS create_contact_reference
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS create_cr
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS create_cr_cms_case
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS create_datacenter
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS create_dr_datacenter
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS create_dr_tier
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS create_network_segment
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS create_solution
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS create_tier_add_service
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS create_tier_add_storage
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS create_tier_lt_backup
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS create_transport_path
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS delete_node
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS delete_node_cr
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS do_price_aggregation
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS get_ha_type
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS get_software
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS is_phase_assign_allowed
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS reset_add_service
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS reset_connectivity
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS reset_datacenter
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS reset_delivery_unit
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS reset_infrastructure_provider
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS reset_landscape
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS reset_solution
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS reset_tier
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS select_software
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS update_modification_type
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
    METHODS update_pricing
      IMPORTING
        !is_ctx                  TYPE /bobf/s_frw_ctx_act
        !it_key                  TYPE /bobf/t_frw_key
        !io_read                 TYPE REF TO /bobf/if_frw_read
        !io_modify               TYPE REF TO /bobf/if_frw_modify
        !is_parameters           TYPE REF TO data
      EXPORTING
        !eo_message              TYPE REF TO /bobf/if_frw_message
        !et_failed_key           TYPE /bobf/t_frw_key
        !ev_static_action_failed TYPE abap_bool
        !et_data                 TYPE INDEX TABLE
        !et_data_link            TYPE /bobf/t_frw_act_exp_data_link .
ENDCLASS.



CLASS /HEC1/CL_CONFIG_ACTION IMPLEMENTATION.


  METHOD update_pricing.

*  DATA: lt_man_serv_base TYPE /hec1/t_data_man_serv_basel_ct,
    DATA: lt_modification  TYPE /bobf/t_frw_modification.

    DATA: lv_changed TYPE sap_bool.

    DATA: para              TYPE tpara-paramid VALUE '/HEC1/CONFIG_DEBUG',
          ls_debug_own_code TYPE /hec1/s_config_debug_modus.

    CLEAR: eo_message,
           et_failed_key,
           ev_static_action_failed,
           et_data,
           et_data_link.

    GET PARAMETER ID para FIELD ls_debug_own_code.


    "Safety first
    IF ls_debug_own_code-hec_debug_modus      = abap_true AND "Todo (remove before transport )
       ls_debug_own_code-hec_debuf_modus_vers = '09'.

      IF eo_message IS NOT BOUND.
        eo_message = /bobf/cl_frw_factory=>get_message( ).
      ENDIF.


      "-----------------------------------
      " Get all relevant nodes data with root key where
      " prices are stored for validation, if prices
      " have changed in the meanwhile
      "-----------------------------------

      /hec1/cl_config_helper=>get_price_relevant_node_data( EXPORTING is_ctx                   = CORRESPONDING #( is_ctx )
                                                                      it_key                   = it_key
                                                                      io_read                  = io_read
                                                            IMPORTING et_landscape             = DATA(lt_landscape)
                                                                      et_managed_serv_baseline = DATA(lt_man_serv_base)
                                                                      et_delivery_unit         = DATA(lt_delivery_unit)
                                                                      et_infra_struc_baseline  = DATA(lt_inf_base)
                                                                      et_connectivity          = DATA(lt_connectivity)
                                                                      et_add_service           = DATA(lt_add_service)
                                                                      et_tier                  = DATA(lt_tier)
                                                                      et_tier_add_service      = DATA(lt_tier_add_service)
                                                                      et_db_node               = DATA(lt_db_node)
                                                                      et_db_server             = DATA(lt_db_server)
                                                                      et_db_storage            = DATA(lt_db_storage)
                                                                      et_db_backup             = DATA(lt_db_backup)
                                                                      et_app_serv_perf_cat     = DATA(lt_app_serv_perf_cat)
                                                                      et_app_server            = DATA(lt_app_server)
                                                                      et_app_storage           = DATA(lt_app_storage)
                                                                      et_app_backup            = DATA(lt_app_backup) ).

      READ TABLE lt_landscape INTO DATA(ls_landscape) INDEX 1.
      READ TABLE lt_delivery_unit INTO DATA(ls_delivery_unit) INDEX 1.

      "-----------------------------------
      " Loop at all relevant objects and get the legoblock-data from Database
      " Comparing of the price fields, if there is a difference in any object, loop will and and the validation is done
      " Due to the next step (update prices, where a full validation is done), there is no need to compare all items
      "-----------------------------------


      "-----------------------------------
      " Managed service baseline
      "-----------------------------------
      LOOP AT lt_man_serv_base REFERENCE INTO DATA(lr_man_serv_base).

*        DATA(ls_man_serv_base_lb) = /hec1/cl_config_helper=>get_price_timebased_bb( iv_effort_bb_guid = lr_man_serv_base->hec_timebased_effort_bb_guid
*                                                                                    iv_root_key       = lr_man_serv_base->root_key
*                                                                                    io_read           = io_read ).

        DATA(ls_man_serv_base_lb) = /hec1/cl_config_helper=>do_price_validation( iv_node_key          = is_ctx-node_key
                                                                                 it_key               = it_key
                                                                                 io_read              = io_read
                                                                                 iv_effort_bb_guid    = lr_man_serv_base->hec_timebased_effort_bb_guid
                                                                                 iv_tier_is_dr_node   = abap_false
                                                                                 iv_dr_operating_mode = '' ).

        IF ls_man_serv_base_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: lv_changed.

        IF lr_man_serv_base->hec_one_time_setup_effort    <> ls_man_serv_base_lb-hec_one_time_setup_effort.     lv_changed = abap_true. ENDIF.
        IF lr_man_serv_base->hec_monthly_operating_effort <> ls_man_serv_base_lb-hec_monthly_operating_effort.  lv_changed = abap_true. ENDIF.
        IF lr_man_serv_base->hec_setup_rate               <> ls_man_serv_base_lb-hec_setup_rate.                lv_changed = abap_true. ENDIF.
        IF lr_man_serv_base->hec_operation_rate           <> ls_man_serv_base_lb-hec_operation_rate.            lv_changed = abap_true. ENDIF.
        IF lr_man_serv_base->hec_monthly_setup_fee        <> ls_man_serv_base_lb-hec_monthly_setup_fee.         lv_changed = abap_true. ENDIF.
        IF lr_man_serv_base->hec_monthly_operation_fee    <> ls_man_serv_base_lb-hec_monthly_operation_fee.     lv_changed = abap_true. ENDIF.

        IF lv_changed = abap_true.
          lr_man_serv_base->hec_one_time_setup_effort    = ls_man_serv_base_lb-hec_one_time_setup_effort.
          lr_man_serv_base->hec_monthly_operating_effort = ls_man_serv_base_lb-hec_monthly_operating_effort.
          lr_man_serv_base->hec_setup_rate               = ls_man_serv_base_lb-hec_setup_rate.
          lr_man_serv_base->hec_operation_rate           = ls_man_serv_base_lb-hec_operation_rate.
          lr_man_serv_base->hec_monthly_setup_fee        = ls_man_serv_base_lb-hec_monthly_setup_fee.
          lr_man_serv_base->hec_monthly_operation_fee    = ls_man_serv_base_lb-hec_monthly_operation_fee.

          INSERT VALUE #( data        = lr_man_serv_base
                          node        = /hec1/if_configuration_c=>sc_node-managed_service_baseline
                          source_node = /hec1/if_configuration_c=>sc_node-root
                          association = /hec1/if_configuration_c=>sc_association-managed_service_baseline-to_parent
                          source_key  = lr_man_serv_base->parent_key
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_man_serv_base->key                                                        ) INTO TABLE lt_modification.
        ENDIF.

      ENDLOOP.



      "-----------------------------------
      " Infrastructure baseline
      "-----------------------------------
      LOOP AT lt_inf_base REFERENCE INTO DATA(lr_inf_base).

        DATA(ls_inf_base_lb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = lr_inf_base->hec_price_lb ).

        IF ls_inf_base_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: lv_changed.

        IF lr_inf_base->hec_final_month_cost_eur <> ls_inf_base_lb-hec_final_month_cost_eur.   lv_changed = abap_true. ENDIF.
        IF lr_inf_base->hec_cost_of_sales_eur    <> ls_inf_base_lb-hec_cost_of_sales_eur.      lv_changed = abap_true. ENDIF.
        IF lr_inf_base->hec_margin_eur           <> ls_inf_base_lb-hec_margin_eur.             lv_changed = abap_true. ENDIF.
        IF lr_inf_base->hec_month_price_eur      <> ls_inf_base_lb-hec_month_price_eur.        lv_changed = abap_true. ENDIF.

        IF lv_changed = abap_true.
          lr_inf_base->hec_final_month_cost_eur = ls_inf_base_lb-hec_final_month_cost_eur.
          lr_inf_base->hec_cost_of_sales_eur    = ls_inf_base_lb-hec_cost_of_sales_eur.
          lr_inf_base->hec_margin_eur           = ls_inf_base_lb-hec_margin_eur.
          lr_inf_base->hec_month_price_eur      = ls_inf_base_lb-hec_month_price_eur.

          INSERT VALUE #( data        = lr_inf_base
                          node        = /hec1/if_configuration_c=>sc_node-infrastructure_baseline
                          source_node = /hec1/if_configuration_c=>sc_node-datacenter
                          association = /hec1/if_configuration_c=>sc_association-infrastructure_baseline-to_parent
                          source_key  = lr_inf_base->parent_key
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_inf_base->key                                                            ) INTO TABLE lt_modification.
        ENDIF.

      ENDLOOP.



      "-----------------------------------
      " Connectivity
      "-----------------------------------
      LOOP AT lt_connectivity REFERENCE INTO DATA(lr_connectivity).

        DATA(ls_connectivity_lb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = lr_connectivity->hec_price_lb ).

        IF ls_connectivity_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: lv_changed.

        IF lr_connectivity->hec_final_month_cost_eur <> ls_connectivity_lb-hec_final_month_cost_eur.   lv_changed = abap_true. ENDIF.
        IF lr_connectivity->hec_cost_of_sales_eur    <> ls_connectivity_lb-hec_cost_of_sales_eur.      lv_changed = abap_true. ENDIF.
        IF lr_connectivity->hec_margin_eur           <> ls_connectivity_lb-hec_margin_eur.             lv_changed = abap_true. ENDIF.
        IF lr_connectivity->hec_month_price_eur      <> ls_connectivity_lb-hec_month_price_eur.        lv_changed = abap_true. ENDIF.

        IF lv_changed = abap_true.
          lr_connectivity->hec_final_month_cost_eur = ls_connectivity_lb-hec_final_month_cost_eur.
          lr_connectivity->hec_cost_of_sales_eur    = ls_connectivity_lb-hec_cost_of_sales_eur.
          lr_connectivity->hec_margin_eur           = ls_connectivity_lb-hec_margin_eur.
          lr_connectivity->hec_month_price_eur      = ls_connectivity_lb-hec_month_price_eur.

          INSERT VALUE #( data        = lr_connectivity
                          node        = /hec1/if_configuration_c=>sc_node-connectivity
                          source_node = /hec1/if_configuration_c=>sc_node-datacenter
                          association = /hec1/if_configuration_c=>sc_association-datacenter-connectivity
                          source_key  = lr_connectivity->parent_key
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_connectivity->key                                                        ) INTO TABLE lt_modification.
        ENDIF.

      ENDLOOP.



      "-----------------------------------
      " Additional Service
      "-----------------------------------
      LOOP AT lt_add_service REFERENCE INTO DATA(lr_add_service).

        DATA(ls_add_service_lb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = lr_add_service->hec_price_lb ).

        IF ls_add_service_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: lv_changed.

        IF lr_add_service->hec_final_month_cost_eur <> ls_add_service_lb-hec_final_month_cost_eur.   lv_changed = abap_true. ENDIF.
        IF lr_add_service->hec_cost_of_sales_eur    <> ls_add_service_lb-hec_cost_of_sales_eur.      lv_changed = abap_true. ENDIF.
        IF lr_add_service->hec_margin_eur           <> ls_add_service_lb-hec_margin_eur.             lv_changed = abap_true. ENDIF.
        IF lr_add_service->hec_month_price_eur      <> ls_add_service_lb-hec_month_price_eur.        lv_changed = abap_true. ENDIF.

        IF lv_changed = abap_true.
          lr_add_service->hec_final_month_cost_eur = ls_add_service_lb-hec_final_month_cost_eur.
          lr_add_service->hec_cost_of_sales_eur    = ls_add_service_lb-hec_cost_of_sales_eur.
          lr_add_service->hec_margin_eur           = ls_add_service_lb-hec_margin_eur.
          lr_add_service->hec_month_price_eur      = ls_add_service_lb-hec_month_price_eur.

          INSERT VALUE #( data        = lr_add_service
                          node        = /hec1/if_configuration_c=>sc_node-add_service
                          source_node = /hec1/if_configuration_c=>sc_node-root
                          association = /hec1/if_configuration_c=>sc_association-add_service-to_parent
                          source_key  = lr_add_service->parent_key
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_add_service->key                                             ) INTO TABLE lt_modification.
        ENDIF.

      ENDLOOP.



      "-----------------------------------
      " Tier
      "-----------------------------------
      LOOP AT lt_tier REFERENCE INTO DATA(lr_tier).

*        DATA(ls_tier_lb) = /hec1/cl_config_helper=>get_price_timebased_bb( iv_effort_bb_guid = lr_tier->hec_timebased_effort_bb_guid
*                                                                           iv_root_key       = lr_tier->root_key
*                                                                           io_read           = io_read ).


        DATA(ls_tier_lb) = /hec1/cl_config_helper=>do_price_validation( iv_node_key          = is_ctx-node_key
                                                                        it_key               = it_key
                                                                        io_read              = io_read
                                                                        iv_effort_bb_guid    = lr_tier->hec_timebased_effort_bb_guid
                                                                        iv_tier_is_dr_node   = lr_tier->hec_tier_is_dr_node
                                                                        iv_dr_operating_mode = lr_tier->hec_dr_oper_mode_value ).


        IF ls_tier_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: lv_changed.

        IF lr_tier->hec_one_time_setup_effort    <> ls_tier_lb-hec_one_time_setup_effort.    lv_changed = abap_true. ENDIF.
        IF lr_tier->hec_monthly_operating_effort <> ls_tier_lb-hec_monthly_operating_effort. lv_changed = abap_true. ENDIF.
        IF lr_tier->hec_setup_rate               <> ls_tier_lb-hec_setup_rate.               lv_changed = abap_true. ENDIF.
        IF lr_tier->hec_operation_rate           <> ls_tier_lb-hec_operation_rate.           lv_changed = abap_true. ENDIF.
        IF lr_tier->hec_monthly_setup_fee        <> ls_tier_lb-hec_monthly_setup_fee.        lv_changed = abap_true. ENDIF.
        IF lr_tier->hec_monthly_operation_fee    <> ls_tier_lb-hec_monthly_operation_fee.    lv_changed = abap_true. ENDIF.

        IF lv_changed = abap_true.
          lr_tier->hec_one_time_setup_effort    = ls_tier_lb-hec_one_time_setup_effort.
          lr_tier->hec_monthly_operating_effort = ls_tier_lb-hec_monthly_operating_effort.
          lr_tier->hec_setup_rate               = ls_tier_lb-hec_setup_rate.
          lr_tier->hec_operation_rate           = ls_tier_lb-hec_operation_rate.
          lr_tier->hec_monthly_setup_fee        = ls_tier_lb-hec_monthly_setup_fee.
          lr_tier->hec_monthly_operation_fee    = ls_tier_lb-hec_monthly_operation_fee.

          INSERT VALUE #( data        = lr_tier
                          node        = /hec1/if_configuration_c=>sc_node-tier
                          source_node = /hec1/if_configuration_c=>sc_node-solution
                          association = /hec1/if_configuration_c=>sc_association-tier-to_parent
                          source_key  = lr_tier->parent_key
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_tier->key                                             ) INTO TABLE lt_modification.
        ENDIF.

      ENDLOOP.



      "-----------------------------------
      " DB Node
      "-----------------------------------
      LOOP AT lt_db_node REFERENCE INTO DATA(lr_db_node).
        DATA(ls_db_node_lb) = /hec1/cl_config_helper=>do_price_validation( iv_node_key          = is_ctx-node_key
                                                                           it_key               = it_key
                                                                           io_read              = io_read
                                                                           iv_effort_bb_guid    = lr_db_node->hec_timebased_effort_bb_guid
                                                                           iv_tier_is_dr_node   = lr_db_node->hec_tier_is_dr_node
                                                                           iv_dr_operating_mode = lr_db_node->hec_dr_oper_mode_value ).

        IF ls_db_node_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: lv_changed.

        IF lr_db_node->hec_one_time_setup_effort    <> ls_db_node_lb-hec_one_time_setup_effort.    lv_changed = abap_true. ENDIF.
        IF lr_db_node->hec_monthly_operating_effort <> ls_db_node_lb-hec_monthly_operating_effort. lv_changed = abap_true. ENDIF.
        IF lr_db_node->hec_setup_rate               <> ls_db_node_lb-hec_setup_rate.               lv_changed = abap_true. ENDIF.
        IF lr_db_node->hec_operation_rate           <> ls_db_node_lb-hec_operation_rate.           lv_changed = abap_true. ENDIF.
        IF lr_db_node->hec_monthly_setup_fee        <> ls_db_node_lb-hec_monthly_setup_fee.        lv_changed = abap_true. ENDIF.
        IF lr_db_node->hec_monthly_operation_fee    <> ls_db_node_lb-hec_monthly_operation_fee.    lv_changed = abap_true. ENDIF.

        IF lv_changed = abap_true.
          lr_db_node->hec_one_time_setup_effort    = ls_db_node_lb-hec_one_time_setup_effort.
          lr_db_node->hec_monthly_operating_effort = ls_db_node_lb-hec_monthly_operating_effort.
          lr_db_node->hec_setup_rate               = ls_db_node_lb-hec_setup_rate.
          lr_db_node->hec_operation_rate           = ls_db_node_lb-hec_operation_rate.
          lr_db_node->hec_monthly_setup_fee        = ls_db_node_lb-hec_monthly_setup_fee.
          lr_db_node->hec_monthly_operation_fee    = ls_db_node_lb-hec_monthly_operation_fee.

          INSERT VALUE #( data        = lr_db_node
                          node        = /hec1/if_configuration_c=>sc_node-db_node
                          source_node = /hec1/if_configuration_c=>sc_node-instance_db
                          association = /hec1/if_configuration_c=>sc_association-db_node-to_parent
                          source_key  = lr_db_node->parent_key
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_db_node->key                                              ) INTO TABLE lt_modification.
        ENDIF.

      ENDLOOP.



      "-----------------------------------
      " DB Server
      "-----------------------------------
      LOOP AT lt_db_server REFERENCE INTO DATA(lr_db_server).

        DATA(ls_db_server_cblb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = lr_db_server->hec_price_lb ).

        IF ls_db_server_cblb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: lv_changed.

        IF lr_db_server->hec_final_month_cost_eur <> ls_db_server_cblb-hec_final_month_cost_eur.   lv_changed = abap_true. ENDIF.
        IF lr_db_server->hec_cost_of_sales_eur    <> ls_db_server_cblb-hec_cost_of_sales_eur.      lv_changed = abap_true. ENDIF.
        IF lr_db_server->hec_margin_eur           <> ls_db_server_cblb-hec_margin_eur.             lv_changed = abap_true. ENDIF.
        IF lr_db_server->hec_month_price_eur      <> ls_db_server_cblb-hec_month_price_eur.        lv_changed = abap_true. ENDIF.

        IF lv_changed = abap_true.
          lr_db_server->hec_final_month_cost_eur = ls_db_server_cblb-hec_final_month_cost_eur.
          lr_db_server->hec_cost_of_sales_eur    = ls_db_server_cblb-hec_cost_of_sales_eur.
          lr_db_server->hec_margin_eur           = ls_db_server_cblb-hec_margin_eur.
          lr_db_server->hec_month_price_eur      = ls_db_server_cblb-hec_month_price_eur.

          INSERT VALUE #( data        = lr_db_server
                          node        = /hec1/if_configuration_c=>sc_node-db_server
                          source_node = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                          association = /hec1/if_configuration_c=>sc_association-db_server-to_parent
                          source_key  = lr_db_server->parent_key
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_db_server->key                                              ) INTO TABLE lt_modification.
        ENDIF.

      ENDLOOP.



      "-----------------------------------
      " DB Storage
      "-----------------------------------
      LOOP AT lt_db_storage REFERENCE INTO DATA(lr_db_storage).

        DATA(ls_db_storage_lb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = lr_db_storage->hec_price_lb ).

        IF ls_db_storage_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: lv_changed.

        IF lr_db_storage->hec_final_month_cost_eur <> ls_db_storage_lb-hec_final_month_cost_eur.   lv_changed = abap_true. ENDIF.
        IF lr_db_storage->hec_cost_of_sales_eur    <> ls_db_storage_lb-hec_cost_of_sales_eur.      lv_changed = abap_true. ENDIF.
        IF lr_db_storage->hec_margin_eur           <> ls_db_storage_lb-hec_margin_eur.             lv_changed = abap_true. ENDIF.
        IF lr_db_storage->hec_month_price_eur      <> ls_db_storage_lb-hec_month_price_eur.        lv_changed = abap_true. ENDIF.

        IF lv_changed = abap_true.
          lr_db_storage->hec_final_month_cost_eur = ls_db_storage_lb-hec_final_month_cost_eur.
          lr_db_storage->hec_cost_of_sales_eur    = ls_db_storage_lb-hec_cost_of_sales_eur.
          lr_db_storage->hec_margin_eur           = ls_db_storage_lb-hec_margin_eur.
          lr_db_storage->hec_month_price_eur      = ls_db_storage_lb-hec_month_price_eur.

          INSERT VALUE #( data        = lr_db_storage
                          node        = /hec1/if_configuration_c=>sc_node-db_storage
                          source_node = /hec1/if_configuration_c=>sc_node-db_server
                          association = /hec1/if_configuration_c=>sc_association-db_storage-to_parent
                          source_key  = lr_db_storage->parent_key
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_db_storage->key                                            ) INTO TABLE lt_modification.
        ENDIF.

      ENDLOOP.



      "-----------------------------------
      " DB Backup
      "-----------------------------------
      LOOP AT lt_db_backup REFERENCE INTO DATA(lr_db_backup).

        DATA(ls_db_backup_lb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = lr_db_backup->hec_price_lb ).

        IF ls_db_backup_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: lv_changed.

        IF lr_db_backup->hec_final_month_cost_eur <> ls_db_backup_lb-hec_final_month_cost_eur.   lv_changed = abap_true. ENDIF.
        IF lr_db_backup->hec_cost_of_sales_eur    <> ls_db_backup_lb-hec_cost_of_sales_eur.      lv_changed = abap_true. ENDIF.
        IF lr_db_backup->hec_margin_eur           <> ls_db_backup_lb-hec_margin_eur.             lv_changed = abap_true. ENDIF.
        IF lr_db_backup->hec_month_price_eur      <> ls_db_backup_lb-hec_month_price_eur.        lv_changed = abap_true. ENDIF.

        IF lv_changed = abap_true.
          lr_db_backup->hec_final_month_cost_eur = ls_db_backup_lb-hec_final_month_cost_eur.
          lr_db_backup->hec_cost_of_sales_eur    = ls_db_backup_lb-hec_cost_of_sales_eur.
          lr_db_backup->hec_margin_eur           = ls_db_backup_lb-hec_margin_eur.
          lr_db_backup->hec_month_price_eur      = ls_db_backup_lb-hec_month_price_eur.

          INSERT VALUE #( data        = lr_db_backup
                          node        = /hec1/if_configuration_c=>sc_node-db_storage_backup
                          source_node = /hec1/if_configuration_c=>sc_node-db_storage
                          association = /hec1/if_configuration_c=>sc_association-db_storage_backup-to_parent
                          source_key  = lr_db_backup->parent_key
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_db_backup->key                                                     ) INTO TABLE lt_modification.
        ENDIF.

      ENDLOOP.



      "-----------------------------------
      " App Server Performance Category
      "-----------------------------------
      LOOP AT lt_app_serv_perf_cat REFERENCE INTO DATA(lr_app_serv_perf_cat).
        DATA(ls_app_serv_pc_lb) = /hec1/cl_config_helper=>do_price_validation( iv_node_key          = is_ctx-node_key
                                                                               it_key               = it_key
                                                                               io_read              = io_read
                                                                               iv_effort_bb_guid    = lr_app_serv_perf_cat->hec_timebased_effort_bb_guid
                                                                               iv_tier_is_dr_node   = lr_app_serv_perf_cat->hec_tier_is_dr_node
                                                                               iv_dr_operating_mode = lr_app_serv_perf_cat->hec_dr_oper_mode_value ).

        IF ls_app_serv_pc_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: lv_changed.

        IF lr_app_serv_perf_cat->hec_one_time_setup_effort    <> ls_app_serv_pc_lb-hec_one_time_setup_effort.    lv_changed = abap_true. ENDIF.
        IF lr_app_serv_perf_cat->hec_monthly_operating_effort <> ls_app_serv_pc_lb-hec_monthly_operating_effort. lv_changed = abap_true. ENDIF.
        IF lr_app_serv_perf_cat->hec_setup_rate               <> ls_app_serv_pc_lb-hec_setup_rate.               lv_changed = abap_true. ENDIF.
        IF lr_app_serv_perf_cat->hec_operation_rate           <> ls_app_serv_pc_lb-hec_operation_rate.           lv_changed = abap_true. ENDIF.
        IF lr_app_serv_perf_cat->hec_monthly_setup_fee        <> ls_app_serv_pc_lb-hec_monthly_setup_fee.        lv_changed = abap_true. ENDIF.
        IF lr_app_serv_perf_cat->hec_monthly_operation_fee    <> ls_app_serv_pc_lb-hec_monthly_operation_fee.    lv_changed = abap_true. ENDIF.

        IF lv_changed = abap_true.
          lr_app_serv_perf_cat->hec_one_time_setup_effort    = ls_app_serv_pc_lb-hec_one_time_setup_effort.
          lr_app_serv_perf_cat->hec_monthly_operating_effort = ls_app_serv_pc_lb-hec_monthly_operating_effort.
          lr_app_serv_perf_cat->hec_setup_rate               = ls_app_serv_pc_lb-hec_setup_rate.
          lr_app_serv_perf_cat->hec_operation_rate           = ls_app_serv_pc_lb-hec_operation_rate.
          lr_app_serv_perf_cat->hec_monthly_setup_fee        = ls_app_serv_pc_lb-hec_monthly_setup_fee.
          lr_app_serv_perf_cat->hec_monthly_operation_fee    = ls_app_serv_pc_lb-hec_monthly_operation_fee.

          INSERT VALUE #( data        = lr_app_serv_perf_cat
                          node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                          source_node = /hec1/if_configuration_c=>sc_node-app_node
                          association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_parent
                          source_key  = lr_app_serv_perf_cat->parent_key
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_app_serv_perf_cat->key                                                  ) INTO TABLE lt_modification.
        ENDIF.
      ENDLOOP.


      "-----------------------------------
      " App Server
      "-----------------------------------
      LOOP AT lt_app_server REFERENCE INTO DATA(lr_app_server).

        DATA(ls_app_server_lb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = lr_app_server->hec_price_lb ).

        IF ls_app_server_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: lv_changed.

        IF lr_app_server->hec_final_month_cost_eur <> ls_app_server_lb-hec_final_month_cost_eur.   lv_changed = abap_true. ENDIF.
        IF lr_app_server->hec_cost_of_sales_eur    <> ls_app_server_lb-hec_cost_of_sales_eur.      lv_changed = abap_true. ENDIF.
        IF lr_app_server->hec_margin_eur           <> ls_app_server_lb-hec_margin_eur.             lv_changed = abap_true. ENDIF.
        IF lr_app_server->hec_month_price_eur      <> ls_app_server_lb-hec_month_price_eur.        lv_changed = abap_true. ENDIF.

        IF lv_changed = abap_true.
          lr_app_server->hec_final_month_cost_eur = ls_app_server_lb-hec_final_month_cost_eur.
          lr_app_server->hec_cost_of_sales_eur    = ls_app_server_lb-hec_cost_of_sales_eur.
          lr_app_server->hec_margin_eur           = ls_app_server_lb-hec_margin_eur.
          lr_app_server->hec_month_price_eur      = ls_app_server_lb-hec_month_price_eur.


          INSERT VALUE #( data        = lr_app_server
                          node        = /hec1/if_configuration_c=>sc_node-app_server
                          source_node = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                          association = /hec1/if_configuration_c=>sc_association-app_server-to_parent
                          source_key  = lr_app_server->parent_key
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_app_server->key                                            ) INTO TABLE lt_modification.
        ENDIF.
      ENDLOOP.



      "-----------------------------------
      " App Storage
      "-----------------------------------
      LOOP AT lt_app_storage REFERENCE INTO DATA(lr_app_storage).

        DATA(ls_app_storage_lb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = lr_app_storage->hec_price_lb ).

        IF ls_app_storage_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: lv_changed.

        IF lr_app_storage->hec_final_month_cost_eur <> ls_app_storage_lb-hec_final_month_cost_eur.   lv_changed = abap_true. ENDIF.
        IF lr_app_storage->hec_cost_of_sales_eur    <> ls_app_storage_lb-hec_cost_of_sales_eur.      lv_changed = abap_true. ENDIF.
        IF lr_app_storage->hec_margin_eur           <> ls_app_storage_lb-hec_margin_eur.             lv_changed = abap_true. ENDIF.
        IF lr_app_storage->hec_month_price_eur      <> ls_app_storage_lb-hec_month_price_eur.        lv_changed = abap_true. ENDIF.

        IF lv_changed = abap_true.
          lr_app_storage->hec_final_month_cost_eur = ls_app_storage_lb-hec_final_month_cost_eur.
          lr_app_storage->hec_cost_of_sales_eur    = ls_app_storage_lb-hec_cost_of_sales_eur.
          lr_app_storage->hec_margin_eur           = ls_app_storage_lb-hec_margin_eur.
          lr_app_storage->hec_month_price_eur      = ls_app_storage_lb-hec_month_price_eur.


          INSERT VALUE #( data        = lr_app_storage
                          node        = /hec1/if_configuration_c=>sc_node-app_storage
                          source_node = /hec1/if_configuration_c=>sc_node-app_server
                          association = /hec1/if_configuration_c=>sc_association-app_storage-to_parent
                          source_key  = lr_app_storage->parent_key
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_app_storage->key                                            ) INTO TABLE lt_modification.
        ENDIF.

      ENDLOOP.



      "-----------------------------------
      " App Backup
      "-----------------------------------
      LOOP AT lt_app_backup REFERENCE INTO DATA(lr_app_backup).

        DATA(ls_app_backup_lb) = /hec1/cl_config_helper=>get_price_costbased( iv_price_lb_guid = lr_app_backup->hec_price_lb ).

        IF ls_app_backup_lb IS INITIAL.
          EXIT.
        ENDIF.

        CLEAR: lv_changed.

        IF lr_app_backup->hec_final_month_cost_eur <> ls_app_backup_lb-hec_final_month_cost_eur.   lv_changed = abap_true. ENDIF.
        IF lr_app_backup->hec_cost_of_sales_eur    <> ls_app_backup_lb-hec_cost_of_sales_eur.      lv_changed = abap_true. ENDIF.
        IF lr_app_backup->hec_margin_eur           <> ls_app_backup_lb-hec_margin_eur.             lv_changed = abap_true. ENDIF.
        IF lr_app_backup->hec_month_price_eur      <> ls_app_backup_lb-hec_month_price_eur.        lv_changed = abap_true. ENDIF.

        IF lv_changed = abap_true.
          lr_app_backup->hec_final_month_cost_eur = ls_app_backup_lb-hec_final_month_cost_eur.
          lr_app_backup->hec_cost_of_sales_eur    = ls_app_backup_lb-hec_cost_of_sales_eur.
          lr_app_backup->hec_margin_eur           = ls_app_backup_lb-hec_margin_eur.
          lr_app_backup->hec_month_price_eur      = ls_app_backup_lb-hec_month_price_eur.

          INSERT VALUE #( data        = lr_app_backup
                          node        = /hec1/if_configuration_c=>sc_node-app_storage_backup
                          source_node = /hec1/if_configuration_c=>sc_node-app_storage
                          association = /hec1/if_configuration_c=>sc_association-app_storage_backup-to_parent
                          source_key  = lr_app_backup->parent_key
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = lr_app_backup->key                                                     ) INTO TABLE lt_modification.
        ENDIF.

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

    ENDIF.


  ENDMETHOD.


  METHOD select_software.

    DATA: lt_solution           TYPE /hec1/t_data_solution_ct,
          lt_material           TYPE /hec1/t_data_material_ct,
          lt_software_item      TYPE /hec1/t_data_sw_item_ct,
          ls_software_item_list TYPE /hec1/s_data_sw_item_list,
          ls_material_list      TYPE /hec1/s_data_material_list,
          lt_tier               TYPE /hec1/t_data_tier_ct,
          lt_modification       TYPE /bobf/t_frw_modification.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_solution ).

    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                      IMPORTING et_data        = lt_tier
                                                et_target_key  = DATA(lt_tier_key) ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                it_key         = lt_tier_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier-material
                                      IMPORTING et_data        = lt_material
                                                et_target_key  = DATA(lt_material_key) ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-material
                                                it_key         = lt_material_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-material-software_item
                                      IMPORTING et_data        = lt_software_item ).

    " there is only one line when an action is called
    TRY.
        DATA(ls_solution) = lt_solution[ 1 ].
      CATCH cx_sy_itab_line_not_found.
        RETURN. ">>>>
    ENDTRY.

    ASSIGN is_parameters->* TO FIELD-SYMBOL(<fs_parameters>).
    IF <fs_parameters> IS NOT ASSIGNED.
      RETURN. ">>>>
    ENDIF.

    CASE is_ctx-act_key.

        " **********************************
        " Select/Deselect Material List
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_action-solution-select_material.

        "1. Update Material Table
        ls_material_list = <fs_parameters>.

        /hec1/cl_config_sw_helper=>get_instance( )->/hec1/if_config_sw_helper~select_material( EXPORTING it_material_list = VALUE #( ( ls_material_list ) ) ).

        " deactivate selection for software items if the material isn't selected
        /hec1/cl_config_sw_helper=>get_instance( )->/hec1/if_config_sw_helper~set_swi_list_selectable( iv_node_solution_guid = ls_material_list-hec_node_solution
                                                                                                       iv_material_guid      = ls_material_list-hec_material_guid
                                                                                                       iv_row_selectable     = ls_material_list-hec_mat_selection ).

        "2. Update Material (Add/Remove)
        LOOP AT lt_tier ASSIGNING FIELD-SYMBOL(<fs_tier>).

          IF ls_material_list-hec_mat_selection = abap_true.

            " Add
            DATA(ls_material_new) = VALUE /hec1/s_data_material_cs( BASE CORRESPONDING #( ls_material_list )
                                                                         parent_key         = <fs_tier>-key
                                                                         key                = /bopf/cl_frw_factory=>get_new_key( )
                                                                         hec_node_solution  = <fs_tier>-hec_node_solution
                                                                         hec_node_tier      = <fs_tier>-hec_node_tier
                                                                         hec_node_material  = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                         hec_row_selectable = abap_true
                                                                         hec_apm_guid       = <fs_tier>-hec_apm_guid
                                                                         hec_apm_descr      = <fs_tier>-hec_apm_descr
                                                                         hec_phase_guid     = <fs_tier>-hec_phase_guid
                                                                         hec_phase_fixed    = COND #( WHEN ls_material_list-hec_material_rel_value = '01' "Mandatory
                                                                                                      THEN abap_true
                                                                                                      ELSE abap_false )
                                                                         hec_phase_changed  = abap_true ).

            INSERT VALUE #( data        = NEW /hec1/s_data_material_cs( ls_material_new )
                            node        = /hec1/if_configuration_c=>sc_node-material
                            source_node = /hec1/if_configuration_c=>sc_node-tier
                            association = /hec1/if_configuration_c=>sc_association-tier-material
                            source_key  = <fs_tier>-key
                            change_mode = /bobf/if_frw_c=>sc_modify_create
                            key         = ls_material_new-key )
                            INTO TABLE lt_modification.

          ELSE.
            " Delete
            TRY.
                DATA(ls_material) = lt_material[ parent_key = <fs_tier>-key
                                                 hec_material_guid = ls_material_list-hec_material_guid ].

                INSERT VALUE #( node        = /hec1/if_configuration_c=>sc_node-material
                                change_mode = /bobf/if_frw_c=>sc_modify_delete
                                key         = ls_material-key ) INTO TABLE lt_modification.

              CATCH cx_sy_itab_line_not_found.
            ENDTRY.

          ENDIF. "hec_mat_selection
        ENDLOOP. "lt_tier


        " **********************************
        " Select/Deselect Software Item List
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_action-solution-select_software_item.

        "1. Update Software Table
        ls_software_item_list = <fs_parameters>.

        /hec1/cl_config_sw_helper=>get_instance( )->/hec1/if_config_sw_helper~select_software_item( it_software_item_list = VALUE #( ( ls_software_item_list ) ) ).

        "2. Update Software (Add/Remove)
        LOOP AT lt_tier ASSIGNING <fs_tier>.

          TRY.
              ls_material = lt_material[ parent_key        = <fs_tier>-key
                                         hec_material_guid = ls_software_item_list-hec_material_guid ].

              IF ls_software_item_list-hec_sw_selection = abap_true.
                " add
                DATA(ls_sw_item_new) = VALUE /hec1/s_data_sw_item_cs( BASE CORRESPONDING #( ls_software_item_list )
                                                                      parent_key         = ls_material-key
                                                                      key                = /bopf/cl_frw_factory=>get_new_key( )
                                                                      hec_node_solution  = ls_material-hec_node_solution
                                                                      hec_node_tier      = ls_material-hec_node_tier
                                                                      hec_node_material  = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                      hec_row_selectable = abap_true
                                                                      hec_apm_guid       = ls_material-hec_apm_guid
                                                                      hec_apm_descr      = ls_material-hec_apm_descr
                                                                      hec_phase_guid     = ls_material-hec_phase_guid
                                                                      hec_phase_fixed    = COND #( WHEN ls_software_item_list-hec_sw_item_mat_rel_value = '01'            "Mandatory
                                                                                                   THEN abap_true
                                                                                                   ELSE abap_false                                              )
                                                                      hec_phase_changed  = abap_true                                                              ).

                INSERT VALUE #( data        = NEW /hec1/s_data_sw_item_cs( ls_sw_item_new )
                                node        = /hec1/if_configuration_c=>sc_node-software_item
                                source_node = /hec1/if_configuration_c=>sc_node-material
                                association = /hec1/if_configuration_c=>sc_association-material-software_item
                                source_key  = ls_material-key
                                change_mode = /bobf/if_frw_c=>sc_modify_create
                                key         = ls_sw_item_new-key                                               ) INTO TABLE lt_modification.

              ELSE.
                " Delete
                TRY.
                    DATA(ls_sw_item) = lt_software_item[ parent_key = <fs_tier>-key
                                                         hec_material_guid = ls_material_list-hec_material_guid ].

                    INSERT VALUE #( node        = /hec1/if_configuration_c=>sc_node-material
                                    change_mode = /bobf/if_frw_c=>sc_modify_delete
                                    key         = ls_material-key                            ) INTO TABLE lt_modification.

                  CATCH cx_sy_itab_line_not_found.
                ENDTRY.
              ENDIF. "hec_sw_selection
            CATCH cx_sy_itab_line_not_found.
          ENDTRY.
        ENDLOOP. "lt_tier
    ENDCASE. "is_ctx-act_key


    "-----------------------------------
    " perform modification
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change) ).
    ENDIF.

    LOOP AT lt_modification INTO DATA(ls_modification)
      WHERE change_mode = /bobf/if_frw_c=>sc_modify_delete.

      /hec1/cl_bopf_config_ui_tree_h=>get_instance( )->/hec1/if_bopf_config_ui_tree_h~delete( iv_node_key = ls_modification-key ).
    ENDLOOP.

  ENDMETHOD.


  METHOD reset_tier.

    CASE is_ctx-act_key.
      WHEN /hec1/if_configuration_c=>sc_action-tier-modify_datac_assignment.
      WHEN /hec1/if_configuration_c=>sc_action-tier-reset_implementation_type.
      WHEN /hec1/if_configuration_c=>sc_action-tier-reset_tier_type.
    ENDCASE.

  ENDMETHOD.


  METHOD reset_solution.

    CASE is_ctx-act_key.
      WHEN /hec1/if_configuration_c=>sc_action-solution-reset_solution.
      WHEN /hec1/if_configuration_c=>sc_action-solution-reset_implementation_type.
    ENDCASE.

  ENDMETHOD.


  METHOD reset_landscape.

    CASE is_ctx-act_key.
      WHEN /hec1/if_configuration_c=>sc_action-root-modify_config_status.
      WHEN /hec1/if_configuration_c=>sc_action-root-modify_acc_dlvy_category.
      WHEN /hec1/if_configuration_c=>sc_action-root-modify_cloud_offering.
      WHEN /hec1/if_configuration_c=>sc_action-root-reset_currency.
      WHEN /hec1/if_configuration_c=>sc_action-root-reset_dlvy_region_l1.
      WHEN /hec1/if_configuration_c=>sc_action-root-reset_dlvy_region_l2.
      WHEN /hec1/if_configuration_c=>sc_action-root-reset_dlvy_region_l3.
    ENDCASE.


  ENDMETHOD.


  METHOD reset_infrastructure_provider.



  ENDMETHOD.


  METHOD reset_delivery_unit.




  ENDMETHOD.


  METHOD reset_datacenter.


  ENDMETHOD.


  METHOD reset_connectivity.

    DATA: lt_connectivity TYPE /hec1/t_data_connectivity_ct.

    CLEAR: eo_message,
           et_failed_key.

    " **********************************
    " Check instance status and switch
    " **********************************
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_connectivity ).

    TRY.
        DATA(lr_connectivity) = REF #( lt_connectivity[ 1 ] ).
      CATCH cx_sy_itab_line_not_found.
        RETURN. ">>>>
    ENDTRY.

    CLEAR: lr_connectivity->hec_connectivity_guid,
           lr_connectivity->hec_connectivity_descr,
           lr_connectivity->price,
           lr_connectivity->hec_tree_descr.

    io_modify->update( iv_node = is_ctx-node_key
                       iv_key  = lr_connectivity->key
                       is_data = lr_connectivity ).

  ENDMETHOD.


  METHOD get_software.

    DATA: lt_solution TYPE /hec1/t_data_solution_ct.

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key  = is_ctx-node_key
                                                        it_key       = it_key
                                                        io_read      = io_read
                                              IMPORTING ev_root_key  = DATA(lv_root_key)
                                                        er_landscape = DATA(lr_landscape) ).

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_solution ).

    " there is only one line when an action is called
    TRY.
        DATA(ls_solution) = lt_solution[ 1 ].
      CATCH cx_sy_itab_line_not_found.
        RETURN. ">>>>
    ENDTRY.

    CASE is_ctx-act_key.
        " **********************************
        " Get Software Item List
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_action-solution-get_software_item_list.

        et_data = /hec1/cl_config_sw_helper=>get_instance( )->/hec1/if_config_sw_helper~get_software_item_list( iv_apm_guid      = lr_landscape->hec_apm_guid
                                                                                                                iv_solution_guid = ls_solution-hec_solution_guid
                                                                                                                iv_node_solution = ls_solution-hec_node_solution ).

        " **********************************
        " Get Material List
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_action-solution-get_material_list.

        et_data = /hec1/cl_config_sw_helper=>get_instance( )->/hec1/if_config_sw_helper~get_material_list( iv_apm_guid      = lr_landscape->hec_apm_guid
                                                                                                           iv_solution_guid = ls_solution-hec_solution_guid
                                                                                                           iv_node_solution = ls_solution-hec_node_solution ).

    ENDCASE.

  ENDMETHOD.


  METHOD do_price_aggregation.

    DATA: l_price_agg               TYPE /hec1/tier_aggr_price_new,
          lt_landsc_base_price_old  TYPE /hec1/t_landsc_price_aggre_ct,
          lt_connectivity_price_old TYPE /hec1/t_connect_price_aggre_ct,
          lt_add_service_price_old  TYPE /hec1/t_service_price_aggre_ct,
          l_add_service_guid        TYPE /hec1/add_service_guid,
          l_sla_uplift_perc         TYPE /hec1/sla_uplift,
          l_adv_uplift_perc         TYPE /hec1/adv_edition_uplift,
          l_add_service_uplift_perc TYPE /hec1/add_service_uplift,
          l_uplift_perc             TYPE /hec1/sla_uplift,
          rt_phase_guid             TYPE RANGE OF /hec1/phase_guid,
          l_hec_aggre_price_tier    TYPE /hec1/aggre_price_eur_out,
          lt_modification           TYPE /bobf/t_frw_modification.

    DATA: para              TYPE tpara-paramid VALUE '/HEC1/CONFIG_DEBUG',
          ls_debug_own_code TYPE /hec1/s_config_debug_modus.
    GET PARAMETER ID para FIELD ls_debug_own_code.


    CHECK is_ctx-node_key = /hec1/if_configuration_c=>sc_node-root.

    "-----------------------------------
    "Get all price relevant objects from config
    "-----------------------------------

    /hec1/cl_config_helper=>get_price_relevant_node_data( EXPORTING is_ctx                     = CORRESPONDING #( is_ctx )
                                                                    it_key                     = it_key
                                                                    io_read                    = io_read
                                                          IMPORTING et_landscape               = DATA(lt_landscape)
                                                                    et_phase                   = DATA(lt_phase)
                                                                    et_managed_serv_baseline   = DATA(lt_man_serv_base)
                                                                    et_delivery_unit           = DATA(lt_delivery_unit)
                                                                    et_infra_struc_baseline    = DATA(lt_inf_base)
                                                                    et_connectivity            = DATA(lt_connectivity)
                                                                    et_add_service             = DATA(lt_add_service)
                                                                    et_lt_backup_class         = DATA(lt_lt_backup_class)
                                                                    et_lt_backup_amount        = DATA(lt_lt_backup_amount)
                                                                    et_add_storage_class       = DATA(lt_add_storage_class)
                                                                    et_add_storage_amount      = DATA(lt_add_storage_amount)
                                                                    et_tier                    = DATA(lt_tier)
                                                                    et_tier_add_service        = DATA(lt_tier_add_service)
                                                                    et_db_node                 = DATA(lt_db_node)
                                                                    et_db_server               = DATA(lt_db_server)
                                                                    et_db_storage              = DATA(lt_db_storage)
                                                                    et_db_backup               = DATA(lt_db_backup)
                                                                    et_app_serv_perf_cat       = DATA(lt_app_serv_perf_cat)
                                                                    et_app_server              = DATA(lt_app_server)
                                                                    et_app_storage             = DATA(lt_app_storage)
                                                                    et_app_backup              = DATA(lt_app_backup)
                                                                    et_tier_price_phase        = DATA(lt_tier_price_old)
                                                                    et_lt_backup_price_phase   = DATA(lt_lt_backup_old)
                                                                    et_add_storage_price_phase = DATA(lt_add_storage_old) ).

    DATA(ls_landscape)        = VALUE #( lt_landscape[ 1 ]     OPTIONAL ).
    DATA(ls_man_svc_baseline) = VALUE #( lt_man_serv_base[ 1 ] OPTIONAL ).

    CHECK: ls_man_svc_baseline IS NOT INITIAL,
           ls_landscape IS NOT INITIAL.

    "-----------------------------------
    "No phase, no prices
    "-----------------------------------

    IF lt_phase[] IS INITIAL.
      RETURN.
    ENDIF.

    /hec1/cl_rep_config_data=>read_config_data( EXPORTING i_config_id       = ls_landscape-hec_confid
                                                          i_config_version  = ls_landscape-hec_conf_version
                                                IMPORTING es_config_head    = DATA(ls_config_head)
                                                          et_config_data    = DATA(lt_config_data)
                                                          et_cfg_price_data = DATA(lt_price_data)
                                                          e_subrc           = DATA(l_subrc) ).

    "-----------------------------------
    "Clean up 'old' Price Objects
    "All Price-Aggregation-BO will be deleted before
    "-----------------------------------
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-landsc_base_price_phase
                                      IMPORTING et_data        = lt_landsc_base_price_old ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-connectivity_price_phase
                                      IMPORTING et_data        = lt_connectivity_price_old ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = it_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-add_service_price_phase
                                      IMPORTING et_data        = lt_add_service_price_old ).


    LOOP AT lt_landsc_base_price_old REFERENCE INTO DATA(lr_landsc_base_price_old).
      INSERT VALUE #( data        = lr_landsc_base_price_old
                      node        = /hec1/if_configuration_c=>sc_node-landsc_base_price_phase
                      source_node = /hec1/if_configuration_c=>sc_node-root
                      association = /hec1/if_configuration_c=>sc_association-landsc_base_price_phase-to_parent
                      source_key  = lr_landsc_base_price_old->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_delete
                      key         = lr_landsc_base_price_old->key                                              ) INTO TABLE lt_modification.
    ENDLOOP.

    LOOP AT lt_connectivity_price_old REFERENCE INTO DATA(lr_connectivity_price_old).
      INSERT VALUE #( data        = lr_connectivity_price_old
                      node        = /hec1/if_configuration_c=>sc_node-connectivity_price_phase
                      source_node = /hec1/if_configuration_c=>sc_node-root
                      association = /hec1/if_configuration_c=>sc_association-connectivity_price_phase-to_parent
                      source_key  = lr_connectivity_price_old->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_delete
                      key         = lr_connectivity_price_old->key                                               ) INTO TABLE lt_modification.
    ENDLOOP.

    LOOP AT lt_add_service_price_old REFERENCE INTO DATA(lr_add_service_price_old).
      INSERT VALUE #( data        = lr_add_service_price_old
                      node        = /hec1/if_configuration_c=>sc_node-add_service_price_phase
                      source_node = /hec1/if_configuration_c=>sc_node-root
                      association = /hec1/if_configuration_c=>sc_association-add_service_price_phase-to_parent
                      source_key  = lr_add_service_price_old->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_delete
                      key         = lr_add_service_price_old->key                                              ) INTO TABLE lt_modification.
    ENDLOOP.


    LOOP AT lt_tier_price_old REFERENCE INTO DATA(lr_tier_price_old).
      INSERT VALUE #( data        = lr_tier_price_old
                      node        = /hec1/if_configuration_c=>sc_node-tier_price_phase
                      source_node = /hec1/if_configuration_c=>sc_node-tier
                      association = /hec1/if_configuration_c=>sc_association-tier_price_phase-to_parent
                      source_key  = lr_tier_price_old->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_delete
                      key         = lr_tier_price_old->key                                              ) INTO TABLE lt_modification.
    ENDLOOP.


    LOOP AT lt_lt_backup_old REFERENCE INTO DATA(lr_lt_backup_old).
      INSERT VALUE #( data        = lr_lt_backup_old
                      node        = /hec1/if_configuration_c=>sc_node-lt_backup_price_phase
                      source_node = /hec1/if_configuration_c=>sc_node-root
                      association = /hec1/if_configuration_c=>sc_association-lt_backup_price_phase-to_parent
                      source_key  = lr_lt_backup_old->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_delete
                      key         = lr_lt_backup_old->key                                                   ) INTO TABLE lt_modification.
    ENDLOOP.


    LOOP AT lt_add_storage_old REFERENCE INTO DATA(lr_add_storage_old).
      INSERT VALUE #( data        = lr_add_storage_old
                      node        = /hec1/if_configuration_c=>sc_node-add_storage_price_phase
                      source_node = /hec1/if_configuration_c=>sc_node-root
                      association = /hec1/if_configuration_c=>sc_association-add_storage_price_phase-to_parent
                      source_key  = lr_add_storage_old->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_delete
                      key         = lr_add_storage_old->key                                                   ) INTO TABLE lt_modification.
    ENDLOOP.


    "-----------------------------------
    " Aggregation of Landscape Base price
    "-----------------------------------

    READ TABLE lt_phase INTO DATA(ls_phase) WITH KEY hec_node_phase = ls_man_svc_baseline-hec_phase_guid.

    DATA(lr_landscape_price) = NEW /hec1/s_landsc_price_aggre_cs( BASE CORRESPONDING #( ls_landscape )
                                                                  parent_key              = ls_landscape-key
                                                                  key                     = /bopf/cl_frw_factory=>get_new_key( )
                                                                  hec_phase_start_date    = ls_phase-hec_phase_start_date
                                                                  hec_phase_end_date      = ls_phase-hec_phase_end_date
                                                                  hec_phase_descr         = ls_phase-hec_phase_descr
                                                                  hec_no_of_days          = /hec1/cl_price_helper=>get_days_between(
                                                                                              iv_start_date = ls_phase-hec_phase_start_date
                                                                                              iv_end_date   = ls_phase-hec_phase_end_date
                                                                                            )
                                                                  hec_node_landscape      = ls_landscape-hec_node_landscape
                                                                  hec_node_landscape_base = /rbp/cl_general_utilities=>get_new_guid22( )           ).

    lr_landscape_price->hec_aggre_price = + ls_man_svc_baseline-hec_monthly_setup_fee + ls_man_svc_baseline-hec_monthly_operation_fee.
    lr_landscape_price->hec_exchange_value = + ls_man_svc_baseline-hec_exchange_value.
    lr_landscape_price->hec_exchange_rate = ls_man_svc_baseline-hec_exchange_rate.
    lr_landscape_price->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.

    "The Landscape base price doesnt change for the whole landscape time, so each phase/infrastructure baseline has to sum up
    LOOP AT lt_phase[] ASSIGNING FIELD-SYMBOL(<ls_phase>).

      LOOP AT lt_inf_base ASSIGNING FIELD-SYMBOL(<ls_inf_base>) WHERE hec_phase_guid = <ls_phase>-hec_node_phase.

        lr_landscape_price->hec_aggre_price = lr_landscape_price->hec_aggre_price + <ls_inf_base>-hec_month_price_eur.
        lr_landscape_price->hec_exchange_value = lr_landscape_price->hec_exchange_value + <ls_inf_base>-hec_exchange_value.
        lr_landscape_price->hec_if_baseline_guid = <ls_inf_base>-hec_node_if_baseline.
        lr_landscape_price->hec_phase_guid = <ls_phase>-hec_node_phase.

      ENDLOOP.

    ENDLOOP.

    lr_landscape_price->hec_price_ssp100 = lr_landscape_price->hec_aggre_price.
    lr_landscape_price->hec_price_ssp100_exchange = lr_landscape_price->hec_exchange_value.

    "Advanced Edition uplift calculation
    IF ls_landscape-hec_ls_uplift_percent IS NOT INITIAL.
      lr_landscape_price->hec_adv_edition_uplift_perc = ls_landscape-hec_ls_uplift_percent.
      lr_landscape_price->hec_adv_edition_uplift_incl = abap_true.
      lr_landscape_price->hec_adv_edition_uplift = lr_landscape_price->hec_aggre_price * ( ls_landscape-hec_ls_uplift_percent / 100 ).
      lr_landscape_price->hec_price_ssp100 = lr_landscape_price->hec_aggre_price + lr_landscape_price->hec_adv_edition_uplift.
      lr_landscape_price->hec_price_ssp100_exchange = lr_landscape_price->hec_exchange_value + ( lr_landscape_price->hec_exchange_value * ( ls_landscape-hec_ls_uplift_percent / 100 ) ).
    ENDIF.

    "SSP115 = SSP100 + Uplift + 15%
    lr_landscape_price->hec_price_ssp115 = lr_landscape_price->hec_price_ssp100 * ( 115 / 100 ).
    lr_landscape_price->hec_price_ssp115_exchange = lr_landscape_price->hec_price_ssp100_exchange * ( 115 / 100 ).

    "SSP85 = SSP100 + Uplift - 15%
    lr_landscape_price->hec_price_ssp85 = lr_landscape_price->hec_price_ssp100 * ( 85 / 100 ).
    lr_landscape_price->hec_price_ssp85_exchange = lr_landscape_price->hec_price_ssp100_exchange * ( 85 / 100 ).

    lr_landscape_price->hec_price_ssp100_year = lr_landscape_price->hec_price_ssp100 * 12.
    lr_landscape_price->hec_price_ssp115_year = lr_landscape_price->hec_price_ssp115 * 12.
    lr_landscape_price->hec_price_ssp85_year  = lr_landscape_price->hec_price_ssp85 * 12.

    lr_landscape_price->hec_price_ssp100_year_exchange = lr_landscape_price->hec_price_ssp100_exchange * 12.
    lr_landscape_price->hec_price_ssp115_year_exchange = lr_landscape_price->hec_price_ssp115_exchange * 12.
    lr_landscape_price->hec_price_ssp85_year_exchange = lr_landscape_price->hec_price_ssp85_exchange * 12.

    INSERT VALUE #( data        = lr_landscape_price
                    node        = /hec1/if_configuration_c=>sc_node-landsc_base_price_phase
                    source_node = /hec1/if_configuration_c=>sc_node-root
                    association = /hec1/if_configuration_c=>sc_association-landsc_base_price_phase-to_parent
                    source_key  = lr_landscape_price->parent_key
                    change_mode = /bobf/if_frw_c=>sc_modify_create
                    key         = lr_landscape_price->key                                                    ) INTO TABLE lt_modification.



    "-----------------------------------
    "Aggregation of Connectivity Costs
    "-----------------------------------

    LOOP AT lt_phase[] ASSIGNING <ls_phase>.

      LOOP AT lt_connectivity ASSIGNING FIELD-SYMBOL(<ls_connectivity>) WHERE hec_phase_guid = <ls_phase>-hec_node_phase. "#EC CI_SORTSEQ

        DATA(lr_connectivity_price) = NEW /hec1/s_connect_price_aggre_cs( BASE CORRESPONDING #( <ls_connectivity> )
                                                                          parent_key              = ls_landscape-key
                                                                          key                     = /bopf/cl_frw_factory=>get_new_key( )
                                                                          hec_phase_start_date    = <ls_phase>-hec_phase_start_date
                                                                          hec_phase_end_date      = <ls_phase>-hec_phase_end_date
                                                                          hec_no_of_days          = /hec1/cl_price_helper=>get_days_between(
                                                                                                      iv_start_date = <ls_phase>-hec_phase_start_date
                                                                                                      iv_end_date   = <ls_phase>-hec_phase_end_date
                                                                                                    )
                                                                          hec_node_landscape      = ls_landscape-hec_node_landscape
                                                                          hec_node_connectivity   = <ls_connectivity>-hec_node_connectivity
                                                                          hec_phase_guid          = <ls_connectivity>-hec_phase_guid                   ).



        lr_connectivity_price->hec_aggre_price = <ls_connectivity>-hec_month_price_eur.
        lr_connectivity_price->hec_exchange_value = <ls_connectivity>-hec_exchange_value.
        lr_connectivity_price->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.

        lr_connectivity_price->hec_price_ssp100 = lr_connectivity_price->hec_aggre_price.
        lr_connectivity_price->hec_price_ssp100_exchange = lr_connectivity_price->hec_exchange_value.

        IF ls_landscape-hec_ls_uplift_percent IS NOT INITIAL.
          lr_connectivity_price->hec_adv_edition_uplift_perc = ls_landscape-hec_ls_uplift_percent.
          lr_connectivity_price->hec_adv_edition_uplift_incl = abap_true.
          lr_connectivity_price->hec_adv_edition_uplift = lr_connectivity_price->hec_aggre_price * ( ls_landscape-hec_ls_uplift_percent / 100 ).
          lr_connectivity_price->hec_price_ssp100 = lr_connectivity_price->hec_aggre_price + lr_connectivity_price->hec_adv_edition_uplift.
          lr_connectivity_price->hec_price_ssp100_exchange = lr_connectivity_price->hec_exchange_value + ( lr_connectivity_price->hec_exchange_value * ( ls_landscape-hec_ls_uplift_percent / 100 ) ).
        ENDIF.

        "SSP115 = SSP100 + Uplift + 15%
        lr_connectivity_price->hec_price_ssp115 = lr_connectivity_price->hec_price_ssp100 * ( 115 / 100 ).
        lr_connectivity_price->hec_price_ssp115_exchange = lr_connectivity_price->hec_price_ssp100_exchange * ( 115 / 100 ).

        "SSP85 = SSP100 + Uplift - 15%
        lr_connectivity_price->hec_price_ssp85 = lr_connectivity_price->hec_price_ssp100 * ( 85 / 100 ).
        lr_connectivity_price->hec_price_ssp85_exchange = lr_connectivity_price->hec_price_ssp100_exchange * ( 85 / 100 ).

        lr_connectivity_price->hec_price_ssp100_year = lr_connectivity_price->hec_price_ssp100 * 12.
        lr_connectivity_price->hec_price_ssp115_year = lr_connectivity_price->hec_price_ssp115 * 12.
        lr_connectivity_price->hec_price_ssp85_year  = lr_connectivity_price->hec_price_ssp85 * 12.

        lr_connectivity_price->hec_price_ssp100_year_exchange = lr_connectivity_price->hec_price_ssp100_exchange * 12.
        lr_connectivity_price->hec_price_ssp115_year_exchange = lr_connectivity_price->hec_price_ssp115_exchange * 12.
        lr_connectivity_price->hec_price_ssp85_year_exchange = lr_connectivity_price->hec_price_ssp85_exchange * 12.

        INSERT VALUE #( data        = lr_connectivity_price
                        node        = /hec1/if_configuration_c=>sc_node-connectivity_price_phase
                        source_node = /hec1/if_configuration_c=>sc_node-root
                        association = /hec1/if_configuration_c=>sc_association-connectivity_price_phase-to_parent
                        source_key  = lr_connectivity_price->parent_key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = lr_connectivity_price->key                                                    ) INTO TABLE lt_modification.

      ENDLOOP.
    ENDLOOP.

    "-----------------------------------
    "Aggregation of Additional Services on Landscape level
    "-----------------------------------

    LOOP AT lt_phase[] ASSIGNING <ls_phase>.

      CLEAR: l_add_service_guid.

      "Same GUID for all Add Services
      l_add_service_guid = /rbp/cl_general_utilities=>get_new_guid22( ).

      LOOP AT lt_add_service ASSIGNING FIELD-SYMBOL(<ls_add_service>) WHERE hec_phase_guid = <ls_phase>-hec_node_phase. "#EC CI_SORTSEQ

        DATA(lr_add_service_price) = NEW /hec1/s_service_price_aggre_cs( BASE CORRESPONDING #( <ls_add_service> )
                                                                         parent_key              = ls_landscape-key
                                                                         key                     = /bopf/cl_frw_factory=>get_new_key( )
                                                                         hec_phase_start_date    = <ls_phase>-hec_phase_start_date
                                                                         hec_phase_end_date      = <ls_phase>-hec_phase_end_date
                                                                         hec_no_of_days          = /hec1/cl_price_helper=>get_days_between(
                                                                                                     iv_start_date = <ls_phase>-hec_phase_start_date
                                                                                                     iv_end_date   = <ls_phase>-hec_phase_end_date
                                                                                                   )
                                                                         hec_node_service        = <ls_add_service>-hec_node_service
                                                                         hec_node_landscape      = ls_landscape-hec_node_landscape
                                                                         hec_phase_guid          = <ls_add_service>-hec_phase_guid                   ).


        lr_add_service_price->hec_aggre_price = <ls_add_service>-hec_month_price_eur.
        lr_add_service_price->hec_exchange_value = + <ls_add_service>-hec_exchange_value.
        lr_add_service_price->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.

        lr_add_service_price->hec_price_ssp100 = lr_add_service_price->hec_aggre_price.
        lr_add_service_price->hec_price_ssp100_exchange = lr_add_service_price->hec_exchange_value.

        IF ls_landscape-hec_ls_uplift_percent IS NOT INITIAL.
          lr_add_service_price->hec_adv_edition_uplift_perc = ls_landscape-hec_ls_uplift_percent.
          lr_add_service_price->hec_adv_edition_uplift_incl = abap_true.
          lr_add_service_price->hec_adv_edition_uplift = lr_add_service_price->hec_aggre_price * ( ls_landscape-hec_ls_uplift_percent / 100 ).
          lr_add_service_price->hec_price_ssp100 = lr_add_service_price->hec_aggre_price + lr_add_service_price->hec_adv_edition_uplift.
          lr_add_service_price->hec_price_ssp100_exchange = lr_add_service_price->hec_exchange_value + ( lr_add_service_price->hec_exchange_value * ( ls_landscape-hec_ls_uplift_percent / 100 ) ).
        ENDIF.

        "SSP115 = SSP100 + Uplift + 15%
        lr_add_service_price->hec_price_ssp115 = lr_add_service_price->hec_price_ssp100 * ( 115 / 100 ).
        lr_add_service_price->hec_price_ssp115_exchange = lr_add_service_price->hec_price_ssp100_exchange * ( 115 / 100 ).

        "SSP85 = SSP100 + Uplift - 15%
        lr_add_service_price->hec_price_ssp85 = lr_add_service_price->hec_price_ssp100 * ( 85 / 100 ).
        lr_add_service_price->hec_price_ssp85_exchange = lr_add_service_price->hec_price_ssp100_exchange * ( 85 / 100 ).

        lr_add_service_price->hec_price_ssp100_year = lr_add_service_price->hec_price_ssp100 * 12.
        lr_add_service_price->hec_price_ssp115_year = lr_add_service_price->hec_price_ssp115 * 12.
        lr_add_service_price->hec_price_ssp85_year  = lr_add_service_price->hec_price_ssp85 * 12.

        lr_add_service_price->hec_price_ssp100_year_exchange = lr_add_service_price->hec_price_ssp100_exchange * 12.
        lr_add_service_price->hec_price_ssp115_year_exchange = lr_add_service_price->hec_price_ssp115_exchange * 12.
        lr_add_service_price->hec_price_ssp85_year_exchange  = lr_add_service_price->hec_price_ssp85_exchange * 12.

        INSERT VALUE #( data        = lr_add_service_price
                        node        = /hec1/if_configuration_c=>sc_node-add_service_price_phase
                        source_node = /hec1/if_configuration_c=>sc_node-root
                        association = /hec1/if_configuration_c=>sc_association-add_service_price_phase-to_parent
                        source_key  = lr_add_service_price->parent_key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = lr_add_service_price->key                                                  ) INTO TABLE lt_modification.

      ENDLOOP.
    ENDLOOP.


    "-----------------------------------
    "Aggregation of Longterm Backup on Landscape level
    "-----------------------------------

    LOOP AT lt_config_data[] ASSIGNING FIELD-SYMBOL(<ls_ltb_data>) WHERE level_id = /hec1/cl_rep_config_data=>c_level_ltb_class.

      /hec1/cl_rep_config_data=>get_price_phases( EXPORTING it_config_data    = lt_config_data[]
                                                            it_cfg_price_data = lt_price_data[]
                                                            i_row_id          = <ls_ltb_data>-row_id
                                                  IMPORTING et_price_phases   = DATA(lt_ltb_price_phases) ).

      READ TABLE lt_lt_backup_class ASSIGNING FIELD-SYMBOL(<ls_ltb_class>) WITH KEY hec_node_lt_backup_class = <ls_ltb_data>-hec_node_id.
      IF sy-subrc <> 0.
        EXIT.
      ENDIF.

      LOOP AT lt_ltb_price_phases ASSIGNING FIELD-SYMBOL(<ls_ltb_price_phases>).
        CLEAR: rt_phase_guid[].
        rt_phase_guid[] = VALUE #( FOR wa IN <ls_ltb_price_phases>-phases
                                     ( low    = wa-guid
                                       sign   = 'I'
                                       option = 'EQ' )                ).

        DATA(lt_ltb_subtree_data) = /hec1/cl_rep_config_data=>get_subtree( EXPORTING it_config_data = lt_config_data[]
                                                                                     i_row_id       = <ls_ltb_data>-row_id ).

        DELETE lt_ltb_subtree_data[] WHERE hec_phase_guid NOT IN rt_phase_guid.

        DATA(lr_lt_backup_price) = NEW /hec1/s_lt_backup_price_agg_cs( BASE CORRESPONDING #( <ls_ltb_data> )
                                                                       parent_key              = ls_landscape-key
                                                                       hec_node_landscape      = ls_landscape-hec_node_landscape
                                                                       hec_node_lt_backup_class = <ls_ltb_data>-hec_node_id
                                                                       hec_phase_start_date    = <ls_ltb_price_phases>-start_date
                                                                       hec_phase_end_date      = <ls_ltb_price_phases>-end_date
                                                                       hec_no_of_days          = /hec1/cl_price_helper=>get_days_between(
                                                                                                   iv_start_date = <ls_ltb_price_phases>-start_date
                                                                                                   iv_end_date   = <ls_ltb_price_phases>-end_date
                                                                                                 )                                                  ).

        lr_lt_backup_price->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.

        LOOP AT lt_ltb_subtree_data[] ASSIGNING FIELD-SYMBOL(<ls_ltb_subtree_data>).
          lr_lt_backup_price->hec_aggre_price = lr_lt_backup_price->hec_aggre_price + ( <ls_ltb_subtree_data>-month_price_fee ).
          lr_lt_backup_price->hec_exchange_value = ( <ls_ltb_subtree_data>-hec_exchange_value ).
        ENDLOOP.

        lr_lt_backup_price->hec_price_ssp100 = lr_lt_backup_price->hec_aggre_price.
        lr_lt_backup_price->hec_price_ssp100_exchange = lr_lt_backup_price->hec_exchange_value.

        IF ls_landscape-hec_ls_uplift_percent IS NOT INITIAL.
          lr_lt_backup_price->hec_adv_edition_uplift_perc = ls_landscape-hec_ls_uplift_percent.
          lr_lt_backup_price->hec_adv_edition_uplift_incl = abap_true.
          lr_lt_backup_price->hec_adv_edition_uplift = lr_lt_backup_price->hec_aggre_price * ( ls_landscape-hec_ls_uplift_percent / 100 ).
          lr_lt_backup_price->hec_price_ssp100 = lr_lt_backup_price->hec_aggre_price + lr_lt_backup_price->hec_adv_edition_uplift.
          lr_lt_backup_price->hec_price_ssp100_exchange = lr_lt_backup_price->hec_exchange_value + ( lr_lt_backup_price->hec_exchange_value * ( ls_landscape-hec_ls_uplift_percent / 100 ) ).
        ENDIF.

        "SSP115 = SSP100 + Uplift + 15%
        lr_lt_backup_price->hec_price_ssp115 = lr_lt_backup_price->hec_price_ssp100 * ( 115 / 100 ).
        lr_lt_backup_price->hec_price_ssp115_exchange = lr_lt_backup_price->hec_price_ssp100_exchange * ( 115 / 100 ).

        "SSP85 = SSP100 + Uplift - 15%
        lr_lt_backup_price->hec_price_ssp85 = lr_lt_backup_price->hec_price_ssp100 * ( 85 / 100 ).
        lr_lt_backup_price->hec_price_ssp85_exchange = lr_lt_backup_price->hec_price_ssp100_exchange * ( 85 / 100 ).

        lr_lt_backup_price->hec_price_ssp100_year = lr_lt_backup_price->hec_price_ssp100 * 12.
        lr_lt_backup_price->hec_price_ssp115_year = lr_lt_backup_price->hec_price_ssp115 * 12.
        lr_lt_backup_price->hec_price_ssp85_year  = lr_lt_backup_price->hec_price_ssp85 * 12.

        lr_lt_backup_price->hec_price_ssp100_year_exchange = lr_lt_backup_price->hec_price_ssp100_exchange * 12.
        lr_lt_backup_price->hec_price_ssp115_year_exchange = lr_lt_backup_price->hec_price_ssp115_exchange * 12.
        lr_lt_backup_price->hec_price_ssp85_year_exchange  = lr_lt_backup_price->hec_price_ssp85_exchange * 12.

        INSERT VALUE #( data        = lr_lt_backup_price
                        node        = /hec1/if_configuration_c=>sc_node-lt_backup_price_phase
                        source_node = /hec1/if_configuration_c=>sc_node-root
                        association = /hec1/if_configuration_c=>sc_association-root-lt_backup_price_phase
                        source_key  = lr_lt_backup_price->root_key
                        change_mode = /bobf/if_frw_c=>sc_modify_create                                         ) INTO TABLE lt_modification.


      ENDLOOP.
    ENDLOOP.

    "-----------------------------------
    "Aggregation of Additional Storage on Landscape level
    "-----------------------------------

    LOOP AT lt_config_data[] ASSIGNING FIELD-SYMBOL(<ls_add_storage_data>) WHERE level_id = /hec1/cl_rep_config_data=>c_level_add_storage_class.

      /hec1/cl_rep_config_data=>get_price_phases( EXPORTING it_config_data    = lt_config_data[]
                                                            it_cfg_price_data = lt_price_data[]
                                                            i_row_id          = <ls_add_storage_data>-row_id
                                                  IMPORTING et_price_phases   = DATA(lt_add_storage_price_phases) ).

      READ TABLE lt_add_storage_class ASSIGNING FIELD-SYMBOL(<ls_add_storage_class>) WITH KEY hec_node_add_storage_class = <ls_add_storage_data>-hec_node_id.
      IF sy-subrc <> 0.
        EXIT.
      ENDIF.

      LOOP AT lt_add_storage_price_phases ASSIGNING FIELD-SYMBOL(<ls_add_storage_price_phases>).
        CLEAR: rt_phase_guid[].
        rt_phase_guid[] = VALUE #( FOR wa IN <ls_add_storage_price_phases>-phases
                                     ( low    = wa-guid
                                       sign   = 'I'
                                       option = 'EQ' )                            ).

        DATA(lt_add_storage_subtree_data) = /hec1/cl_rep_config_data=>get_subtree( EXPORTING it_config_data = lt_config_data[]
                                                                                             i_row_id       = <ls_add_storage_data>-row_id ).

        DELETE lt_add_storage_subtree_data[] WHERE hec_phase_guid NOT IN rt_phase_guid.

        DATA(lr_add_storage_price) = NEW /hec1/s_add_storage_price_phas( BASE CORRESPONDING #( <ls_add_storage_data> )
                                                                       parent_key              = ls_landscape-key
                                                                       hec_node_landscape      = ls_landscape-hec_node_landscape
                                                                       hec_node_add_storage_guid = <ls_add_storage_data>-hec_node_id
                                                                       hec_phase_start_date    = <ls_add_storage_price_phases>-start_date
                                                                       hec_phase_end_date      = <ls_add_storage_price_phases>-end_date
                                                                       hec_no_of_days          = /hec1/cl_price_helper=>get_days_between(
                                                                                                   iv_start_date = <ls_add_storage_price_phases>-start_date
                                                                                                   iv_end_date   = <ls_add_storage_price_phases>-end_date
                                                                                                 )                                                  ).

        lr_add_storage_price->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.

        LOOP AT lt_add_storage_subtree_data[] ASSIGNING FIELD-SYMBOL(<ls_add_storage_subtree_data>).
          lr_add_storage_price->hec_aggre_price = lr_add_storage_price->hec_aggre_price + ( <ls_add_storage_subtree_data>-month_price_fee ).
          lr_add_storage_price->hec_exchange_value = ( <ls_add_storage_subtree_data>-hec_exchange_value ).
        ENDLOOP.

        lr_add_storage_price->hec_price_ssp100 = lr_add_storage_price->hec_aggre_price.
        lr_add_storage_price->hec_price_ssp100_exchange = lr_add_storage_price->hec_exchange_value.

        IF ls_landscape-hec_ls_uplift_percent IS NOT INITIAL.
          lr_add_storage_price->hec_adv_edition_uplift_perc = ls_landscape-hec_ls_uplift_percent.
          lr_add_storage_price->hec_adv_edition_uplift_incl = abap_true.
          lr_add_storage_price->hec_adv_edition_uplift = lr_add_storage_price->hec_aggre_price * ( ls_landscape-hec_ls_uplift_percent / 100 ).
          lr_add_storage_price->hec_price_ssp100 = lr_add_storage_price->hec_aggre_price + lr_add_storage_price->hec_adv_edition_uplift.
          lr_add_storage_price->hec_price_ssp100_exchange = lr_add_storage_price->hec_exchange_value + ( lr_add_storage_price->hec_exchange_value * ( ls_landscape-hec_ls_uplift_percent / 100 ) ).
        ENDIF.

        "SSP115 = SSP100 + Uplift + 15%
        lr_add_storage_price->hec_price_ssp115 = lr_add_storage_price->hec_price_ssp100 * ( 115 / 100 ).
        lr_add_storage_price->hec_price_ssp115_exchange = lr_add_storage_price->hec_price_ssp100_exchange * ( 115 / 100 ).

        "SSP85 = SSP100 + Uplift - 15%
        lr_add_storage_price->hec_price_ssp85 = lr_add_storage_price->hec_price_ssp100 * ( 85 / 100 ).
        lr_add_storage_price->hec_price_ssp85_exchange = lr_add_storage_price->hec_price_ssp100_exchange * ( 85 / 100 ).

        lr_add_storage_price->hec_price_ssp100_year = lr_add_storage_price->hec_price_ssp100 * 12.
        lr_add_storage_price->hec_price_ssp115_year = lr_add_storage_price->hec_price_ssp115 * 12.
        lr_add_storage_price->hec_price_ssp85_year  = lr_add_storage_price->hec_price_ssp85 * 12.

        lr_add_storage_price->hec_price_ssp100_year_exchange = lr_add_storage_price->hec_price_ssp100_exchange * 12.
        lr_add_storage_price->hec_price_ssp115_year_exchange = lr_add_storage_price->hec_price_ssp115_exchange * 12.
        lr_add_storage_price->hec_price_ssp85_year_exchange  = lr_add_storage_price->hec_price_ssp85_exchange * 12.

        INSERT VALUE #( data        = lr_add_storage_price
                        node        = /hec1/if_configuration_c=>sc_node-add_storage_price_phase
                        source_node = /hec1/if_configuration_c=>sc_node-root
                        association = /hec1/if_configuration_c=>sc_association-root-add_storage_price_phase
                        source_key  = lr_add_storage_price->root_key
                        change_mode = /bobf/if_frw_c=>sc_modify_create                                         ) INTO TABLE lt_modification.


      ENDLOOP.
    ENDLOOP.



    "-----------------------------------
    "Aggregation of Tier price for each price phase
    "-----------------------------------

    LOOP AT lt_config_data[] ASSIGNING FIELD-SYMBOL(<ls_tier_data>)
      WHERE level_id = /hec1/cl_rep_config_data=>c_level_tier.

      /hec1/cl_rep_config_data=>get_price_phases( EXPORTING it_config_data    = lt_config_data[]
                                                            it_cfg_price_data = lt_price_data[]
                                                            i_row_id          = <ls_tier_data>-row_id
                                                  IMPORTING et_price_phases   = DATA(lt_price_phases) ).

      READ TABLE lt_tier ASSIGNING FIELD-SYMBOL(<ls_tier>) WITH KEY hec_node_solution = <ls_tier_data>-hec_node_solution hec_node_tier = <ls_tier_data>-hec_node_tier.
      IF sy-subrc <> 0.
        EXIT.
      ENDIF.

      LOOP AT lt_price_phases ASSIGNING FIELD-SYMBOL(<ls_price_phases>).

        "<ls_price_phases>-phases-guid convert to range and sort out lines of lt_tier_data
        CLEAR: rt_phase_guid[].
        rt_phase_guid[] = VALUE #( FOR wa IN <ls_price_phases>-phases
                                     ( low    = wa-guid
                                       sign   = 'I'
                                       option = 'EQ' )                ).

        DATA(lt_tier_subtree_data) = /hec1/cl_rep_config_data=>get_subtree( EXPORTING it_config_data = lt_config_data[]
                                                                                      i_row_id       = <ls_tier_data>-row_id ).

        DELETE lt_tier_subtree_data[] WHERE hec_phase_guid NOT IN rt_phase_guid.

        DATA(lr_tier_price) = NEW /hec1/s_tier_price_aggre_cs( BASE CORRESPONDING #( <ls_tier> )
                                                               parent_key              = <ls_tier>-key
                                                               key                     = /bopf/cl_frw_factory=>get_new_key( )
                                                               hec_node_tier_aggre     = /rbp/cl_general_utilities=>get_new_guid22( )
                                                               hec_phase_start_date    = <ls_price_phases>-start_date
                                                               hec_phase_end_date      = <ls_price_phases>-end_date
                                                               hec_no_of_days          = /hec1/cl_price_helper=>get_days_between(
                                                                                         iv_start_date = <ls_price_phases>-start_date
                                                                                         iv_end_date   = <ls_price_phases>-end_date   ) ).

        lr_tier_price->hec_aggre_price = lr_tier_price->hec_aggre_price + ( <ls_tier>-hec_monthly_setup_fee + <ls_tier>-hec_monthly_operation_fee ).
        lr_tier_price->hec_exchange_value = ( <ls_tier>-hec_exchange_value ).
        lr_tier_price->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.

        LOOP AT lt_tier_subtree_data ASSIGNING FIELD-SYMBOL(<ls_tier_subtree>).

          CASE <ls_tier_subtree>-level_id.

            WHEN /hec1/cl_rep_config_data=>c_level_db_node.
              lr_tier_price->hec_aggre_price = lr_tier_price->hec_aggre_price + ( <ls_tier_subtree>-hec_monthly_setup_fee + <ls_tier_subtree>-hec_monthly_operation_fee ).
              lr_tier_price->hec_exchange_value = lr_tier_price->hec_exchange_value + <ls_tier_subtree>-hec_exchange_value.

            WHEN /hec1/cl_rep_config_data=>c_level_db_server.
              lr_tier_price->hec_aggre_price = lr_tier_price->hec_aggre_price + ( <ls_tier_subtree>-hec_month_price_eur ).
              lr_tier_price->hec_exchange_value = lr_tier_price->hec_exchange_value + <ls_tier_subtree>-hec_exchange_value.

            WHEN /hec1/cl_rep_config_data=>c_level_db_storage.
              lr_tier_price->hec_aggre_price = lr_tier_price->hec_aggre_price + ( <ls_tier_subtree>-month_price_fee ).
              lr_tier_price->hec_exchange_value = lr_tier_price->hec_exchange_value + <ls_tier_subtree>-hec_exchange_value.

            WHEN /hec1/cl_rep_config_data=>c_level_db_storage_backup.
              lr_tier_price->hec_aggre_price = lr_tier_price->hec_aggre_price + ( <ls_tier_subtree>-month_price_fee ).
              lr_tier_price->hec_exchange_value = lr_tier_price->hec_exchange_value + <ls_tier_subtree>-hec_exchange_value.

            WHEN /hec1/cl_rep_config_data=>c_level_app_srv_perf_cat.
              lr_tier_price->hec_aggre_price = lr_tier_price->hec_aggre_price + ( <ls_tier_subtree>-hec_monthly_setup_fee + <ls_tier_subtree>-hec_monthly_operation_fee ).
              lr_tier_price->hec_exchange_value = lr_tier_price->hec_exchange_value + <ls_tier_subtree>-hec_exchange_value.

            WHEN /hec1/cl_rep_config_data=>c_level_app_server.
              lr_tier_price->hec_aggre_price = lr_tier_price->hec_aggre_price + ( <ls_tier_subtree>-hec_month_price_eur ).
              lr_tier_price->hec_exchange_value = lr_tier_price->hec_exchange_value + <ls_tier_subtree>-hec_exchange_value.

            WHEN /hec1/cl_rep_config_data=>c_level_app_storage.
              lr_tier_price->hec_aggre_price = lr_tier_price->hec_aggre_price + ( <ls_tier_subtree>-month_price_fee ).
              lr_tier_price->hec_exchange_value = lr_tier_price->hec_exchange_value + <ls_tier_subtree>-hec_exchange_value.

            WHEN /hec1/cl_rep_config_data=>c_level_app_storage_backup.
              lr_tier_price->hec_aggre_price = lr_tier_price->hec_aggre_price + ( <ls_tier_subtree>-month_price_fee ).
              lr_tier_price->hec_exchange_value = lr_tier_price->hec_exchange_value + <ls_tier_subtree>-hec_exchange_value.

            WHEN /hec1/cl_rep_config_data=>c_level_add_tier_service.
              IF <ls_tier_subtree>-hec_tas_tier_uplift_perc > 0.
                lr_tier_price->hec_add_service_uplift_perc = <ls_tier_subtree>-hec_tas_tier_uplift_perc.
                lr_tier_price->hec_add_service_uplift_incl = abap_true.
              ENDIF.
            WHEN /hec1/cl_rep_config_data=>c_level_software_item.
              lr_tier_price->hec_aggre_price = lr_tier_price->hec_aggre_price + ( <ls_tier_subtree>-hec_monthly_setup_fee + <ls_tier_subtree>-hec_monthly_operation_fee ).
              lr_tier_price->hec_exchange_value = lr_tier_price->hec_exchange_value + <ls_tier_subtree>-hec_exchange_value.
            WHEN OTHERS.
          ENDCASE.

        ENDLOOP.

        IF ls_landscape-hec_ls_uplift_percent IS NOT INITIAL.
          lr_tier_price->hec_adv_edition_uplift_perc = ls_landscape-hec_ls_uplift_percent.
          lr_tier_price->hec_adv_edition_uplift_incl = abap_true.
        ENDIF.

        CLEAR: l_sla_uplift_perc, l_add_service_guid, l_adv_uplift_perc.

        READ TABLE lt_tier_subtree_data[] ASSIGNING FIELD-SYMBOL(<ls_tier_sla>) WITH KEY level_id = 'SLA'.
        IF sy-subrc = 0.
          l_sla_uplift_perc = ( 1 + ( <ls_tier_sla>-hec_tier_sla_uplift / 100 ) ).
        ELSE.
          l_sla_uplift_perc = 1.
        ENDIF.

        l_adv_uplift_perc = ( 1 + ( lr_tier_price->hec_adv_edition_uplift_perc / 100 ) ).
        l_add_service_uplift_perc = ( 1 + ( lr_tier_price->hec_add_service_uplift_perc / 100 ) ).

        l_uplift_perc = l_sla_uplift_perc * l_adv_uplift_perc * l_add_service_uplift_perc.

        lr_tier_price->hec_price_ssp100 = lr_tier_price->hec_aggre_price * l_uplift_perc.
        lr_tier_price->hec_price_ssp100_exchange = lr_tier_price->hec_exchange_value * l_uplift_perc.


        lr_tier_price->hec_price_ssp115 = lr_tier_price->hec_price_ssp100 * ( 115 / 100 ). "SSP115 = SSP100 + Uplift + 15%
        lr_tier_price->hec_price_ssp115_exchange = lr_tier_price->hec_price_ssp100_exchange * ( 115 / 100 ). "SSP115 = SSP100 + Uplift + 15%


        lr_tier_price->hec_price_ssp85 = lr_tier_price->hec_price_ssp100 * ( 85 / 100 ). "SSP85 = SSP100 + Uplift - 15%
        lr_tier_price->hec_price_ssp85_exchange = lr_tier_price->hec_price_ssp100_exchange * ( 85 / 100 ). "SSP85 = SSP100 + Uplift - 15%

        lr_tier_price->hec_price_ssp100_year = lr_tier_price->hec_price_ssp100 * 12.
        lr_tier_price->hec_price_ssp115_year = lr_tier_price->hec_price_ssp115 * 12.
        lr_tier_price->hec_price_ssp85_year  = lr_tier_price->hec_price_ssp85 * 12.

        lr_tier_price->hec_price_ssp100_year_exchange = lr_tier_price->hec_price_ssp100_exchange * 12.
        lr_tier_price->hec_price_ssp115_year_exchange = lr_tier_price->hec_price_ssp115_exchange * 12.
        lr_tier_price->hec_price_ssp85_year_exchange = lr_tier_price->hec_price_ssp85_exchange * 12.

        INSERT VALUE #( data        = lr_tier_price
                        node        = /hec1/if_configuration_c=>sc_node-tier_price_phase
                        source_node = /hec1/if_configuration_c=>sc_node-tier
                        association = /hec1/if_configuration_c=>sc_association-tier_price_phase-to_parent
                        source_key  = lr_tier_price->parent_key
                        change_mode = /bobf/if_frw_c=>sc_modify_create
                        key         = lr_tier_price->key                                                  ) INTO TABLE lt_modification.

      ENDLOOP.

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

  ENDMETHOD.


  METHOD delete_node.

    " ***************************************************************************
    " Because of the complexity of the delete logic, the entire code was put
    "  into the helper class /HEC1/CL_CONFIG_ACT_DEL_HELPER
    "
    "  There, each method processes one node type there
    " ***************************************************************************

    /hec1/cl_config_act_del_helper=>/hec1/if_bopf_act_del_helper~delete_helper( is_ctx        = is_ctx
                                                                                it_key        = it_key
                                                                                io_read       = io_read
                                                                                io_modify     = io_modify
                                                                                is_parameters = is_parameters ).

  ENDMETHOD.


  METHOD create_tier_lt_backup.

    DATA: lt_tier         TYPE /hec1/t_data_tier_ct,
          lt_landscape    TYPE /hec1/t_config_root_ct,
          lt_modification TYPE /bobf/t_frw_modification.

    CLEAR: eo_message,
           et_failed_key.

    IF eo_message IS NOT BOUND.
      eo_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_tier ).

    io_read->get_root_key( EXPORTING iv_node       = is_ctx-node_key
                                     it_key        = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).

    io_read->retrieve( EXPORTING iv_node = /hec1/if_configuration_c=>sc_node-root
                                 it_key  = lt_root_key
                       IMPORTING et_data = lt_landscape ).

    " There is only ever one landscape!
    TRY.
        DATA(ls_landscape) = lt_landscape[ 1 ].
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

    LOOP AT lt_tier ASSIGNING FIELD-SYMBOL(<fs_tier>).

      "-----------------------------------
      " add tier longterm backup
      "-----------------------------------
      DATA(lr_tier_longterm_backup) = NEW /hec1/s_data_tier_lt_backup_cs(
                     BASE CORRESPONDING #( <fs_tier> )
                     parent_key               = <fs_tier>-key
                     key                      = /bopf/cl_frw_factory=>get_new_key( )
                     hec_node_tier_ltbackup   = /rbp/cl_general_utilities=>get_new_guid22( )
                     hec_apm_guid             = ls_landscape-hec_apm_guid
                     hec_apm_descr            = ls_landscape-hec_apm_descr
                     hec_instance_status      = /hec1/if_config_constants=>gc_instance_status-incomplete
                     hec_row_selectable       = abap_true
                     hec_delete_visible       = abap_true
                     hec_phase_assign_allowed = abap_true
                     crea_uname               = sy-uname ).

      GET TIME STAMP FIELD lr_tier_longterm_backup->crea_date_time.

      INSERT VALUE #( data        = lr_tier_longterm_backup
                      node        = /hec1/if_configuration_c=>sc_node-tier_longterm_backup
                      source_node = /hec1/if_configuration_c=>sc_node-tier
                      association = /hec1/if_configuration_c=>sc_association-tier-tier_longterm_backup
                      source_key  = <fs_tier>-key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = lr_tier_longterm_backup->key
                      ) INTO TABLE lt_modification.

    ENDLOOP.

    "-----------------------------------
    " Fill export parameter
    "-----------------------------------
    ASSIGN et_data TO FIELD-SYMBOL(<fs_export_parameters>).
    DATA(lt_export_parameters) = VALUE /bobf/t_frw_key_incl( ( key        = lr_tier_longterm_backup->key
                                                               parent_key = lr_tier_longterm_backup->parent_key
                                                               root_key   = lr_tier_longterm_backup->root_key ) ).
    <fs_export_parameters> = lt_export_parameters.



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


  METHOD create_tier_add_storage.

    DATA: lt_tier         TYPE /hec1/t_data_tier_ct,
          lt_landscape    TYPE /hec1/t_config_root_ct,
          lt_modification TYPE /bobf/t_frw_modification.

    CLEAR: eo_message,
           et_failed_key.

    IF eo_message IS NOT BOUND.
      eo_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_tier ).

    io_read->get_root_key( EXPORTING iv_node       = is_ctx-node_key
                                     it_key        = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).

    io_read->retrieve( EXPORTING iv_node = /hec1/if_configuration_c=>sc_node-root
                                 it_key  = lt_root_key
                       IMPORTING et_data = lt_landscape ).

    " There is only ever one landscape!
    TRY.
        DATA(ls_landscape) = lt_landscape[ 1 ].
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

    LOOP AT lt_tier ASSIGNING FIELD-SYMBOL(<fs_tier>).

      "-----------------------------------
      " add tier add storage
      "-----------------------------------
      DATA(lr_tier_add_storage) = NEW /hec1/s_tier_add_storage_cs( BASE CORRESPONDING #( <fs_tier> )
                                                                     parent_key               = <fs_tier>-key
                                                                     key                      = /bopf/cl_frw_factory=>get_new_key( )
                                                                     hec_node_tier_a_storage  = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                     hec_apm_guid             = ls_landscape-hec_apm_guid
                                                                     hec_apm_descr            = ls_landscape-hec_apm_descr
                                                                     hec_row_selectable       = abap_true
                                                                     hec_delete_visible       = abap_true
                                                                     hec_phase_assign_allowed = abap_true
                                                                     crea_uname               = sy-uname ).

      GET TIME STAMP FIELD lr_tier_add_storage->crea_date_time.

      INSERT VALUE #( data        = lr_tier_add_storage
                      node        = /hec1/if_configuration_c=>sc_node-tier_add_storage
                      source_node = /hec1/if_configuration_c=>sc_node-tier
                      association = /hec1/if_configuration_c=>sc_association-tier-tier_add_storage
                      source_key  = <fs_tier>-key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = lr_tier_add_storage->key
                      ) INTO TABLE lt_modification.

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


  METHOD create_tier_add_service.

    DATA: lt_tier         TYPE /hec1/t_data_tier_ct,
          lt_landscape    TYPE /hec1/t_config_root_ct,
          lt_modification TYPE /bobf/t_frw_modification.

    CLEAR: eo_message,
           et_failed_key.

    IF eo_message IS NOT BOUND.
      eo_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_tier ).

    io_read->get_root_key( EXPORTING iv_node       = is_ctx-node_key
                                     it_key        = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).

    io_read->retrieve( EXPORTING iv_node = /hec1/if_configuration_c=>sc_node-root
                                 it_key  = lt_root_key
                       IMPORTING et_data = lt_landscape ).

    " There is only ever one landscape!
    TRY.
        DATA(ls_landscape) = lt_landscape[ 1 ].
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

    LOOP AT lt_tier ASSIGNING FIELD-SYMBOL(<fs_tier>).

      "-----------------------------------
      " add tier additional service
      "-----------------------------------
      DATA(lr_tier_add_service) = NEW /hec1/s_data_tier_add_serv_cs( BASE CORRESPONDING #( <fs_tier> )
                                                                     parent_key               = <fs_tier>-key
                                                                     key                      = /bopf/cl_frw_factory=>get_new_key( )
                                                                     hec_node_tier_service    = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                     hec_apm_guid             = ls_landscape-hec_apm_guid
                                                                     hec_apm_descr            = ls_landscape-hec_apm_descr
                                                                     hec_row_selectable       = abap_true
                                                                     hec_delete_visible       = abap_true
                                                                     hec_phase_assign_allowed = abap_true
                                                                     crea_uname               = sy-uname ).

      GET TIME STAMP FIELD lr_tier_add_service->crea_date_time.

      INSERT VALUE #( data        = lr_tier_add_service
                      node        = /hec1/if_configuration_c=>sc_node-tier_add_service
                      source_node = /hec1/if_configuration_c=>sc_node-tier
                      association = /hec1/if_configuration_c=>sc_association-tier-tier_add_service
                      source_key  = <fs_tier>-key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = lr_tier_add_service->key
                      ) INTO TABLE lt_modification.

    ENDLOOP.

    "-----------------------------------
    " Fill export parameter
    "-----------------------------------
    ASSIGN et_data TO FIELD-SYMBOL(<fs_export_parameters>).
    DATA(lt_export_parameters) = VALUE /bobf/t_frw_key_incl( ( key        = lr_tier_add_service->key
                                                               parent_key = lr_tier_add_service->parent_key
                                                               root_key   = lr_tier_add_service->root_key ) ).
    <fs_export_parameters> = lt_export_parameters.


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


  METHOD create_solution.

    DATA: lt_landscape    TYPE /hec1/t_config_root_ct,
          lt_modification TYPE /bobf/t_frw_modification.

    CLEAR: eo_message,
           et_failed_key.

    IF eo_message IS NOT BOUND.
      eo_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    io_read->get_root_key( EXPORTING iv_node       = is_ctx-node_key
                                     it_key        = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).

    io_read->retrieve( EXPORTING iv_node = /hec1/if_configuration_c=>sc_node-root
                                 it_key  = lt_root_key
                       IMPORTING et_data = lt_landscape ).

    " There is only ever one landscape!
    TRY.
        DATA(ls_root_key) = lt_root_key[ 1 ].
        DATA(ls_landscape) = lt_landscape[ 1 ].
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

    "-----------------------------------
    " add solution
    "-----------------------------------
    DATA(lr_solution) = NEW /hec1/s_data_solution_cs( BASE CORRESPONDING #( ls_landscape )
                                                                  parent_key          = ls_root_key-key
                                                                  key                 = /bopf/cl_frw_factory=>get_new_key( )
                                                                  hec_node_solution   = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                  hec_apm_guid        = ls_landscape-hec_apm_guid
                                                                  hec_apm_descr       = ls_landscape-hec_apm_descr
                                                                  hec_row_selectable  = abap_true
                                                                  hec_delete_visible  = abap_true
                                                                  crea_uname          = sy-uname ).

    GET TIME STAMP FIELD lr_solution->crea_date_time.

    INSERT VALUE #( data        = lr_solution
                    node        = /hec1/if_configuration_c=>sc_node-solution
                    source_node = /hec1/if_configuration_c=>sc_node-root
                    association = /hec1/if_configuration_c=>sc_association-root-solution
                    source_key  = ls_root_key-key
                    change_mode = /bobf/if_frw_c=>sc_modify_create
                    key         = lr_solution->key
                    ) INTO TABLE lt_modification.

    "-----------------------------------
    " Fill export parameter
    "-----------------------------------
    ASSIGN et_data TO FIELD-SYMBOL(<fs_export_parameters>).
    DATA(lt_export_parameters) = VALUE /bobf/t_frw_key_incl( ( key        = lr_solution->key
                                                               parent_key = lr_solution->parent_key
                                                               root_key   = lr_solution->root_key ) ).
    <fs_export_parameters> = lt_export_parameters.


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


  METHOD create_network_segment.

*    CASE is_ctx-act_key.
*      WHEN /hec1/if_configuration_c=>sc_action-tier-reset_tier_description.
*      WHEN /hec1/if_configuration_c=>sc_action-tier-modify_tier_datacenter.
*      WHEN /hec1/if_configuration_c=>sc_action-tier-reset_tier_implementation_type.
*      WHEN /hec1/if_configuration_c=>sc_action-tier-reset_tier_sla.
*      WHEN /hec1/if_configuration_c=>sc_action-tier-reset_tier_type.
*    ENDCASE.

  ENDMETHOD.


  METHOD create_datacenter.

    " This method only creates the primary datacenter
    " DR Datacenters are created from the primary center

    DATA: lt_dlvy_unit    TYPE /hec1/t_data_dlvy_unit_ct,
          lt_phase        TYPE /hec1/t_data_phase_ct,
          lt_datacenter   TYPE /hec1/t_data_datacenter_ct,
          lt_modification TYPE /bobf/t_frw_modification,
          ls_parameters   TYPE /hec1/s_act_create_datacenter,
          lt_landscape    TYPE /hec1/t_config_root_ct.
    DATA: lt_created_data TYPE /hec1/t_data_datacenter_ct,
          lo_type_descr   TYPE REF TO cl_abap_typedescr,
          lo_type_descr2  TYPE REF TO cl_abap_typedescr.

    CLEAR: eo_message,
           et_failed_key.

    ASSIGN is_parameters->* TO FIELD-SYMBOL(<fs_parameters>).
    IF <fs_parameters> IS ASSIGNED.
      ls_parameters = <fs_parameters>.       "#EC CI_FLDEXT_OK[2215424]
    ENDIF.

    "is_ctx-node_key = delivery_unit

    IF eo_message IS NOT BOUND.
      eo_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_dlvy_unit ).

    io_read->get_root_key( EXPORTING iv_node       = is_ctx-node_key
                                     it_key        = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).

    io_read->retrieve( EXPORTING iv_node = /hec1/if_configuration_c=>sc_node-root
                                 it_key  = lt_root_key
                       IMPORTING et_data = lt_landscape ).

    " there is only ever one landscape
    TRY.
        DATA(ls_landscape) = lt_landscape[ 1 ].
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = lt_root_key
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-delivery_unit
                                      IMPORTING et_target_key  = DATA(lt_dlvy_unit_key) ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-delivery_unit
                                                it_key         = lt_dlvy_unit_key
                                                iv_association = /hec1/if_configuration_c=>sc_association-delivery_unit-datacenter
                                      IMPORTING et_data        = lt_datacenter
                                                et_target_key  = DATA(lt_datacenter_key) ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = lt_root_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-phase
                                      IMPORTING et_data        = lt_phase ).

    LOOP AT lt_dlvy_unit ASSIGNING FIELD-SYMBOL(<fs_dlvy_unit>).

      " if the first datacenter is added, the default phase needs to be assigned
      IF lines( lt_datacenter ) = 0.
        TRY.
            DATA(ls_default_phase) = lt_phase[ hec_default_phase  = abap_true "#EC CI_SORTSEQ
                                               hec_phase_inactive = abap_false ].
            DATA(lv_datacenter_first) = abap_true.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.
      ENDIF.

      "-----------------------------------
      " add phase
      "-----------------------------------
      DATA(lr_datacenter) = NEW /hec1/s_data_datacenter_cs( BASE CORRESPONDING #( ls_parameters )
                                                                         parent_key              = <fs_dlvy_unit>-key
                                                                         key                     = /bopf/cl_frw_factory=>get_new_key( )
                                                                         hec_node_datacenter     = COND #( WHEN ls_parameters-hec_node_datacenter IS NOT INITIAL
                                                                                                           THEN ls_parameters-hec_node_datacenter
                                                                                                           ELSE /rbp/cl_general_utilities=>get_new_guid22( ) )
                                                                         hec_apm_guid             = ls_landscape-hec_apm_guid
                                                                         hec_apm_descr            = ls_landscape-hec_apm_descr
                                                                         hec_phase_guid           = ls_default_phase-hec_node_phase
                                                                         hec_phase_fixed          = COND #( WHEN ls_default_phase IS NOT INITIAL
                                                                                                            THEN abap_true
                                                                                                            ELSE abap_false )
                                                                         hec_phase_assign_allowed = COND #( WHEN ls_default_phase IS NOT INITIAL
                                                                                                            THEN abap_false
                                                                                                            ELSE abap_true )
                                                                         hec_datacenter_is_first  = lv_datacenter_first
                                                                         crea_uname               = sy-uname ).

      GET TIME STAMP FIELD lr_datacenter->crea_date_time.

      " make sure that the datacenter type is set
      DATA(lt_datacenter_type) = /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_datacenter_type(
        iv_apm_guid      = ls_landscape-hec_apm_guid
        iv_flat_mat_guid = ls_landscape-hec_flat_mat_guid
      ).
      TRY.
          DATA(ls_datacenter_type) = lt_datacenter_type[ value = /hec1/if_config_constants=>gc_datacenter_type_primary ].
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.

      lr_datacenter->hec_datacenter_type_value = ls_datacenter_type-value.
      lr_datacenter->hec_datacenter_type_descr = ls_datacenter_type-text.

      INSERT VALUE #( data        = lr_datacenter
                      node        = /hec1/if_configuration_c=>sc_node-datacenter
                      source_node = /hec1/if_configuration_c=>sc_node-delivery_unit
                      association = /hec1/if_configuration_c=>sc_association-delivery_unit-datacenter
                      source_key  = <fs_dlvy_unit>-key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = lr_datacenter->key
                      ) INTO TABLE lt_modification.

      "-----------------------------------
      " add infrastructure baseline
      "-----------------------------------
      DATA(lr_if_baseline) = NEW /hec1/s_data_if_baseline_cs( parent_key               = lr_datacenter->key
                                                              key                      = /bopf/cl_frw_factory=>get_new_key( )
                                                              hec_node_datacenter      = lr_datacenter->hec_node_datacenter
                                                              hec_node_if_baseline     = /rbp/cl_general_utilities=>get_new_guid22( )
                                                              hec_phase_guid           = lr_datacenter->hec_phase_guid
                                                              hec_phase_assign_allowed = abap_false
                                                              ).
      GET TIME STAMP FIELD lr_if_baseline->crea_date_time.

      INSERT VALUE #( data        = lr_if_baseline
                      node        = /hec1/if_configuration_c=>sc_node-infrastructure_baseline
                      source_node = /hec1/if_configuration_c=>sc_node-datacenter
                      association = /hec1/if_configuration_c=>sc_association-datacenter-infrastructure_baseline
                      source_key  = lr_datacenter->key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = lr_if_baseline->key
                      ) INTO TABLE lt_modification.

      "-----------------------------------
      " add network segment
      "-----------------------------------
      DATA(lr_network_segm) = NEW /hec1/s_data_network_segm_cs( parent_key               = lr_if_baseline->key
                                                                key                      = /bopf/cl_frw_factory=>get_new_key( )
                                                                hec_node_datacenter      = lr_datacenter->hec_node_datacenter
                                                                hec_node_if_baseline     = lr_if_baseline->hec_node_if_baseline
                                                                hec_node_network_segment = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                ).

      GET TIME STAMP FIELD lr_network_segm->crea_date_time.

      INSERT VALUE #( data        = lr_network_segm
                      node        = /hec1/if_configuration_c=>sc_node-network_segment
                      source_node = /hec1/if_configuration_c=>sc_node-infrastructure_baseline
                      association = /hec1/if_configuration_c=>sc_association-infrastructure_baseline-network_segment
                      source_key  = lr_if_baseline->key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = lr_network_segm->key
                      ) INTO TABLE lt_modification.
      "return created data
      APPEND lr_datacenter->* TO lt_created_data .
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


  METHOD create_connectivity.

    "triggered from datacenter

    DATA: lt_datacenter   TYPE /hec1/t_data_datacenter_ct,
          lt_modification TYPE /bobf/t_frw_modification,
          lt_add_values   TYPE /hec1/t_name_value_pair,
          lt_created_data TYPE /hec1/t_data_connectivity_ct,
          lo_type_descr   TYPE REF TO cl_abap_typedescr,
          lo_type_descr2  TYPE REF TO cl_abap_typedescr.

    CLEAR: eo_message,
           et_failed_key.

    IF eo_message IS NOT BOUND.
      eo_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_failed_key    = et_failed_key ).

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_datacenter ).

    LOOP AT lt_datacenter ASSIGNING FIELD-SYMBOL(<fs_datacenter>).

      DATA(lr_connectivity) = NEW /hec1/s_data_connectivity_cs( root_key                 = <fs_datacenter>-root_key
                                                                parent_key               = <fs_datacenter>-key
                                                                key                      = /bopf/cl_frw_factory=>get_new_key( )
                                                                hec_node_datacenter      = <fs_datacenter>-hec_node_datacenter
                                                                hec_node_connectivity    = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                hec_apm_guid             = lr_landscape->hec_apm_guid
                                                                hec_apm_descr            = lr_landscape->hec_apm_descr
                                                                hec_phase_guid           = <fs_datacenter>-hec_phase_guid
                                                                hec_phase_fixed          = abap_false
                                                                hec_phase_assign_allowed = abap_true
                                                                hec_sec_datacenter_guid  = <fs_datacenter>-hec_sec_datacenter_guid
                                                                crea_uname               = sy-uname ).

      GET TIME STAMP FIELD lr_connectivity->crea_date_time.

      INSERT VALUE #( data        = lr_connectivity
                      node        = /hec1/if_configuration_c=>sc_node-connectivity
                      source_node = /hec1/if_configuration_c=>sc_node-datacenter
                      association = /hec1/if_configuration_c=>sc_association-datacenter-connectivity
                      source_key  = <fs_datacenter>-key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = lr_connectivity->key
                      ) INTO TABLE lt_modification.
      "return created data
      APPEND lr_connectivity->* TO lt_created_data .

    ENDLOOP.
    TRY.
        lo_type_descr ?= cl_abap_typedescr=>describe_by_data( p_data = et_data ).
        lo_type_descr2 ?= cl_abap_typedescr=>describe_by_data( p_data = lt_created_data ).
        IF lo_type_descr->absolute_name = lo_type_descr2->absolute_name.
          et_data = lt_created_data.         "#EC CI_FLDEXT_OK[2215424]
        ENDIF.

      CATCH cx_root.

    ENDTRY.

    "-----------------------------------
    " Fill export parameter
    "-----------------------------------
    ASSIGN et_data TO FIELD-SYMBOL(<fs_export_parameters>).
    DATA(lt_export_parameters) = VALUE /bobf/t_frw_key_incl( ( key        = lr_connectivity->key
                                                               parent_key = lr_connectivity->parent_key
                                                               root_key   = lr_connectivity->root_key ) ).
    <fs_export_parameters> = lt_export_parameters.


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


  METHOD create_add_service.

    DATA: lt_landscape    TYPE /hec1/t_config_root_ct,
          lt_modification TYPE /bobf/t_frw_modification.

    CLEAR: eo_message,
           et_failed_key.

    IF eo_message IS NOT BOUND.
      eo_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    io_read->get_root_key( EXPORTING iv_node       = is_ctx-node_key
                                     it_key        = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).

    io_read->retrieve( EXPORTING iv_node = /hec1/if_configuration_c=>sc_node-root
                                 it_key  = lt_root_key
                       IMPORTING et_data = lt_landscape ).

    " There is only ever one landscape!
    TRY.
        DATA(ls_landscape) = lt_landscape[ 1 ].
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

    "-----------------------------------
    " add additional service
    "-----------------------------------
    DATA(lr_add_service) = NEW /hec1/s_data_add_services_cs( BASE CORRESPONDING #( ls_landscape )
                                                                  parent_key               = ls_landscape-key
                                                                  key                      = /bopf/cl_frw_factory=>get_new_key( )
                                                                  hec_node_service         = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                  hec_apm_guid             = ls_landscape-hec_apm_guid
                                                                  hec_apm_descr            = ls_landscape-hec_apm_descr
                                                                  hec_row_selectable       = abap_true
                                                                  hec_delete_visible       = abap_true
                                                                  hec_phase_assign_allowed = abap_true
                                                                  crea_uname               = sy-uname ).

    GET TIME STAMP FIELD lr_add_service->crea_date_time.

    INSERT VALUE #( data        = lr_add_service
                    node        = /hec1/if_configuration_c=>sc_node-add_service
                    source_node = /hec1/if_configuration_c=>sc_node-root
                    association = /hec1/if_configuration_c=>sc_association-root-add_service
                    source_key  = ls_landscape-key
                    change_mode = /bobf/if_frw_c=>sc_modify_create
                    key         = lr_add_service->key
                    ) INTO TABLE lt_modification.

    "-----------------------------------
    " Fill export parameter
    "-----------------------------------
    ASSIGN et_data TO FIELD-SYMBOL(<fs_export_parameters>).
    DATA(lt_export_parameters) = VALUE /bobf/t_frw_key_incl( ( key        = lr_add_service->key
                                                               parent_key = lr_add_service->parent_key
                                                               root_key   = lr_add_service->root_key ) ).
    <fs_export_parameters> = lt_export_parameters.

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


  METHOD convert_currency.

    DATA: lt_modification  TYPE /bobf/t_frw_modification.

    DATA: lv_changed TYPE sap_bool.

*    DATA: para              TYPE tpara-paramid VALUE '/HEC1/CONFIG_DEBUG',
*          ls_debug_own_code TYPE /hec1/s_config_debug_modus.

    CLEAR: eo_message,
           et_failed_key,
           ev_static_action_failed,
           et_data,
           et_data_link.

*    GET PARAMETER ID para FIELD ls_debug_own_code.

    CHECK is_ctx-node_key = /hec1/if_configuration_c=>sc_node-root.


    "Safety first
*    IF ls_debug_own_code-hec_debug_modus      = abap_true AND "Todo (remove before transport )
*       ls_debug_own_code-hec_debuf_modus_vers = '09'.

    IF eo_message IS NOT BOUND.
      eo_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.


    "-----------------------------------
    " Get all relevant nodes data with root key where
    " prices are stored for currency conversation
    "-----------------------------------

    /hec1/cl_config_helper=>get_price_relevant_node_data( EXPORTING is_ctx                   = CORRESPONDING #( is_ctx )
                                                                    it_key                   = it_key
                                                                    io_read                  = io_read
                                                          IMPORTING et_landscape             = DATA(lt_landscape)
                                                                    et_managed_serv_baseline = DATA(lt_man_serv_base)
                                                                    et_delivery_unit         = DATA(lt_delivery_unit)
                                                                    et_infra_struc_baseline  = DATA(lt_inf_base)
                                                                    et_connectivity          = DATA(lt_connectivity)
                                                                    et_add_service           = DATA(lt_add_service)
                                                                    et_lt_backup_amount      = DATA(lt_lt_backup_amount)
                                                                    et_add_storage_amount    = DATA(lt_add_storage_amount)
                                                                    et_tier                  = DATA(lt_tier)
                                                                    et_software_item         = DATA(lt_software_item)
                                                                    et_tier_add_service      = DATA(lt_tier_add_service)
                                                                    et_db_node               = DATA(lt_db_node)
                                                                    et_db_server             = DATA(lt_db_server)
                                                                    et_db_storage            = DATA(lt_db_storage)
                                                                    et_db_backup             = DATA(lt_db_backup)
                                                                    et_app_serv_perf_cat     = DATA(lt_app_serv_perf_cat)
                                                                    et_app_server            = DATA(lt_app_server)
                                                                    et_app_storage           = DATA(lt_app_storage)
                                                                    et_app_backup            = DATA(lt_app_backup) ).

    READ TABLE lt_landscape INTO DATA(ls_landscape) INDEX 1.
    READ TABLE lt_delivery_unit INTO DATA(ls_delivery_unit) INDEX 1.

    IF ls_landscape-hec_ls_contract_curr IS INITIAL.
      RETURN.
    ENDIF.

    "-----------------------------------
    " Get Exchange Rate Calculation Date from APM-Table with APM Guid
    " TODO: For CR each object has to read the apm-Table, it can be different from initial deal
    "-----------------------------------
    SELECT SINGLE hec_apm_guid, hec_apm_fx_rate_date FROM /hec1/a_model
      WHERE hec_apm_guid = @ls_landscape-hec_apm_guid
      INTO @DATA(ls_apm).

    "-----------------------------------
    " Loop at all relevant objects and get calculate/convert the currency
    "-----------------------------------

    LOOP AT lt_landscape REFERENCE INTO DATA(lr_landscape).
      lr_landscape->hec_apm_fx_rate_date = ls_apm-hec_apm_fx_rate_date.

      INSERT VALUE #( data        = lr_landscape
                      node        = /hec1/if_configuration_c=>sc_node-root
*                        source_node = /hec1/if_configuration_c=>sc_node-root
*                        association = /hec1/if_configuration_c=>sc_association-managed_service_baseline-to_parent
*                        source_key  = lr_man_serv_base->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_landscape->key                                             ) INTO TABLE lt_modification.
    ENDLOOP.


    "-----------------------------------
    " Managed service baseline
    "-----------------------------------
    LOOP AT lt_man_serv_base REFERENCE INTO DATA(lr_man_serv_base).

      lr_man_serv_base->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.
      lr_man_serv_base->hec_apm_fx_rate_date = ls_apm-hec_apm_fx_rate_date.

      /hec1/cl_config_helper=>do_currency_exchange(
        EXPORTING
          iv_currency_from   = 'EUR'
          iv_currency_amount = lr_man_serv_base->hec_monthly_setup_fee + lr_man_serv_base->hec_monthly_operation_fee
          iv_currency_to     = ls_landscape-hec_ls_contract_curr
          iv_date            = ls_apm-hec_apm_fx_rate_date
        IMPORTING
          ev_exchange_rate   = lr_man_serv_base->hec_exchange_rate
          ev_exchange_value  = lr_man_serv_base->hec_exchange_value
      ).

*      lr_man_serv_base->hec_exchange_rate = /hec1/cl_config_helper=>get_exchange_rate( iv_currency_from = 'EUR'
*                                                                                       iv_currency_to   = ls_landscape-hec_ls_contract_curr
*                                                                                       iv_date          = ls_apm-hec_apm_fx_rate_date       ).
*
*      lr_man_serv_base->hec_exchange_value = ( lr_man_serv_base->hec_monthly_setup_fee + lr_man_serv_base->hec_monthly_operation_fee ) * lr_man_serv_base->hec_exchange_rate.

      INSERT VALUE #( data        = lr_man_serv_base
                      node        = /hec1/if_configuration_c=>sc_node-managed_service_baseline
                      source_node = /hec1/if_configuration_c=>sc_node-root
                      association = /hec1/if_configuration_c=>sc_association-managed_service_baseline-to_parent
                      source_key  = lr_man_serv_base->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_man_serv_base->key                                             ) INTO TABLE lt_modification.


    ENDLOOP.



    "-----------------------------------
    " Infrastructure baseline
    "-----------------------------------
    LOOP AT lt_inf_base REFERENCE INTO DATA(lr_inf_base).

      lr_inf_base->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.
      lr_inf_base->hec_apm_fx_rate_date = ls_apm-hec_apm_fx_rate_date.

      /hec1/cl_config_helper=>do_currency_exchange(
        EXPORTING
          iv_currency_from   = 'EUR'
          iv_currency_amount = lr_inf_base->hec_month_price_eur
          iv_currency_to     = ls_landscape-hec_ls_contract_curr
          iv_date            = ls_apm-hec_apm_fx_rate_date
        IMPORTING
          ev_exchange_rate   = lr_inf_base->hec_exchange_rate
          ev_exchange_value  = lr_inf_base->hec_exchange_value
      ).

*      lr_inf_base->hec_exchange_rate = /hec1/cl_config_helper=>get_exchange_rate( iv_currency_from = 'EUR'
*                                                                                  iv_currency_to   = ls_landscape-hec_ls_contract_curr
*                                                                                  iv_date          = ls_apm-hec_apm_fx_rate_date       ).
*
*      lr_inf_base->hec_exchange_value = ( lr_inf_base->hec_month_price_eur ) * lr_inf_base->hec_exchange_rate.

      INSERT VALUE #( data        = lr_inf_base
                      node        = /hec1/if_configuration_c=>sc_node-infrastructure_baseline
                      source_node = /hec1/if_configuration_c=>sc_node-datacenter
                      association = /hec1/if_configuration_c=>sc_association-infrastructure_baseline-to_parent
                      source_key  = lr_inf_base->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_inf_base->key                                                            ) INTO TABLE lt_modification.

    ENDLOOP.



    "-----------------------------------
    " Connectivity
    "-----------------------------------
    LOOP AT lt_connectivity REFERENCE INTO DATA(lr_connectivity).

      lr_connectivity->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.
      lr_connectivity->hec_apm_fx_rate_date = ls_apm-hec_apm_fx_rate_date.

      /hec1/cl_config_helper=>do_currency_exchange( EXPORTING iv_currency_from   = 'EUR'
                                                              iv_currency_amount = lr_connectivity->hec_month_price_eur
                                                              iv_currency_to     = ls_landscape-hec_ls_contract_curr
                                                              iv_date            = ls_apm-hec_apm_fx_rate_date
                                                    IMPORTING ev_exchange_rate   = lr_connectivity->hec_exchange_rate
                                                              ev_exchange_value  = lr_connectivity->hec_exchange_value ).

*      lr_connectivity->hec_exchange_rate = /hec1/cl_config_helper=>get_exchange_rate( iv_currency_from = 'EUR'
*                                                                                      iv_currency_to   = ls_landscape-hec_ls_contract_curr
*                                                                                      iv_date          = ls_apm-hec_apm_fx_rate_date       ).
*
*      lr_connectivity->hec_exchange_value = ( lr_connectivity->hec_month_price_eur ) * lr_connectivity->hec_exchange_rate.

      INSERT VALUE #( data        = lr_connectivity
                      node        = /hec1/if_configuration_c=>sc_node-connectivity
                      source_node = /hec1/if_configuration_c=>sc_node-datacenter
                      association = /hec1/if_configuration_c=>sc_association-datacenter-connectivity
                      source_key  = lr_connectivity->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_connectivity->key                                                        ) INTO TABLE lt_modification.

    ENDLOOP.



    "-----------------------------------
    " Additional Service
    "-----------------------------------
    LOOP AT lt_add_service REFERENCE INTO DATA(lr_add_service).

      lr_add_service->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.
      lr_add_service->hec_apm_fx_rate_date = ls_apm-hec_apm_fx_rate_date.

      /hec1/cl_config_helper=>do_currency_exchange( EXPORTING iv_currency_from   = 'EUR'
                                                              iv_currency_amount = lr_add_service->hec_month_price_eur
                                                              iv_currency_to     = ls_landscape-hec_ls_contract_curr
                                                              iv_date            = ls_apm-hec_apm_fx_rate_date
                                                    IMPORTING ev_exchange_rate   = lr_add_service->hec_exchange_rate
                                                              ev_exchange_value  = lr_add_service->hec_exchange_value ).

*      lr_add_service->hec_exchange_rate = /hec1/cl_config_helper=>get_exchange_rate( iv_currency_from = 'EUR'
*                                                                                     iv_currency_to   = ls_landscape-hec_ls_contract_curr
*                                                                                     iv_date          = ls_apm-hec_apm_fx_rate_date       ).
*
*      lr_add_service->hec_exchange_value = ( lr_add_service->hec_month_price_eur ) * lr_add_service->hec_exchange_rate.


      INSERT VALUE #( data        = lr_add_service
                      node        = /hec1/if_configuration_c=>sc_node-add_service
*                        source_node = /hec1/if_configuration_c=>sc_node-root
*                        association = /hec1/if_configuration_c=>sc_association-add_service-to_parent
*                        source_key  = lr_add_service->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_add_service->key                                             ) INTO TABLE lt_modification.

    ENDLOOP.


    "-----------------------------------
    " Additional Storage Amount
    "-----------------------------------
    LOOP AT lt_add_storage_amount REFERENCE INTO DATA(lr_add_storage_amount).

      lr_add_storage_amount->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.
      lr_add_storage_amount->hec_apm_fx_rate_date = ls_apm-hec_apm_fx_rate_date.

      /hec1/cl_config_helper=>do_currency_exchange( EXPORTING iv_currency_from   = 'EUR'
                                                              iv_currency_amount = lr_add_storage_amount->hec_month_price_fee
                                                              iv_currency_to     = ls_landscape-hec_ls_contract_curr
                                                              iv_date            = ls_apm-hec_apm_fx_rate_date
                                                    IMPORTING ev_exchange_rate   = lr_add_storage_amount->hec_exchange_rate
                                                              ev_exchange_value  = lr_add_storage_amount->hec_exchange_value ).
      INSERT VALUE #( data        = lr_add_storage_amount
                      node        = /hec1/if_configuration_c=>sc_node-add_storage_amount
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_add_storage_amount->key                                             ) INTO TABLE lt_modification.

    ENDLOOP.


    "-----------------------------------
    " Longterm Backup
    "-----------------------------------
    LOOP AT lt_lt_backup_amount REFERENCE INTO DATA(lr_lt_backup_amount).

      lr_lt_backup_amount->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.
      lr_lt_backup_amount->hec_apm_fx_rate_date = ls_apm-hec_apm_fx_rate_date.

      /hec1/cl_config_helper=>do_currency_exchange( EXPORTING iv_currency_from   = 'EUR'
                                                              iv_currency_amount = lr_lt_backup_amount->hec_month_price_fee
                                                              iv_currency_to     = ls_landscape-hec_ls_contract_curr
                                                              iv_date            = ls_apm-hec_apm_fx_rate_date
                                                    IMPORTING ev_exchange_rate   = lr_lt_backup_amount->hec_exchange_rate
                                                              ev_exchange_value  = lr_lt_backup_amount->hec_exchange_value ).

*      lr_lt_backup_amount->hec_exchange_rate = /hec1/cl_config_helper=>get_exchange_rate( iv_currency_from = 'EUR'
*                                                                                         iv_currency_to   = ls_landscape-hec_ls_contract_curr
*                                                                                         iv_date          = ls_apm-hec_apm_fx_rate_date       ).
*
*      lr_lt_backup_amount->hec_exchange_value = ( lr_lt_backup_amount->hec_month_price_fee ) * lr_lt_backup_amount->hec_exchange_rate.


      INSERT VALUE #( data        = lr_lt_backup_amount
                      node        = /hec1/if_configuration_c=>sc_node-lt_backup_amount
*                      source_node = /hec1/if_configuration_c=>sc_node-lt_backup_class
*                      association = /hec1/if_configuration_c=>sc_association-lt_backup_quota-to_parent
*                      source_key  = lr_lt_backup_amount->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_lt_backup_amount->key                                             ) INTO TABLE lt_modification.

    ENDLOOP.

    "-----------------------------------
    " Tier
    "-----------------------------------
    LOOP AT lt_tier REFERENCE INTO DATA(lr_tier).

      lr_tier->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.
      lr_tier->hec_apm_fx_rate_date = ls_apm-hec_apm_fx_rate_date.

      /hec1/cl_config_helper=>do_currency_exchange( EXPORTING iv_currency_from   = 'EUR'
                                                              iv_currency_amount = lr_tier->hec_monthly_setup_fee + lr_tier->hec_monthly_operation_fee
                                                              iv_currency_to     = ls_landscape-hec_ls_contract_curr
                                                              iv_date            = ls_apm-hec_apm_fx_rate_date
                                                    IMPORTING ev_exchange_rate   = lr_tier->hec_exchange_rate
                                                              ev_exchange_value  = lr_tier->hec_exchange_value ).

*      lr_tier->hec_exchange_rate = /hec1/cl_config_helper=>get_exchange_rate( iv_currency_from = 'EUR'
*                                                                              iv_currency_to   = ls_landscape-hec_ls_contract_curr
*                                                                              iv_date          = ls_apm-hec_apm_fx_rate_date       ).
*
*      lr_tier->hec_exchange_value = ( lr_tier->hec_monthly_setup_fee + lr_tier->hec_monthly_operation_fee ) * lr_tier->hec_exchange_rate.

      INSERT VALUE #( data        = lr_tier
                      node        = /hec1/if_configuration_c=>sc_node-tier
                      source_node = /hec1/if_configuration_c=>sc_node-solution
                      association = /hec1/if_configuration_c=>sc_association-tier-to_parent
                      source_key  = lr_tier->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_tier->key                                             ) INTO TABLE lt_modification.

    ENDLOOP.

    "-----------------------------------
    " Software Item
    "-----------------------------------
    LOOP AT lt_software_item REFERENCE INTO DATA(lr_software_item).

      lr_software_item->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.
      lr_software_item->hec_apm_fx_rate_date = ls_apm-hec_apm_fx_rate_date.

      /hec1/cl_config_helper=>do_currency_exchange( EXPORTING iv_currency_from   = 'EUR'
                                                              iv_currency_amount = lr_software_item->hec_monthly_setup_fee + lr_software_item->hec_monthly_operation_fee
                                                              iv_currency_to     = ls_landscape-hec_ls_contract_curr
                                                              iv_date            = ls_apm-hec_apm_fx_rate_date
                                                    IMPORTING ev_exchange_rate   = lr_software_item->hec_exchange_rate
                                                              ev_exchange_value  = lr_software_item->hec_exchange_value ).

*      lr_software_item->hec_exchange_rate = /hec1/cl_config_helper=>get_exchange_rate( iv_currency_from = 'EUR'
*                                                                              iv_currency_to   = ls_landscape-hec_ls_contract_curr
*                                                                              iv_date          = ls_apm-hec_apm_fx_rate_date       ).
*
*      lr_software_item->hec_exchange_value = ( lr_software_item->hec_monthly_setup_fee + lr_software_item->hec_monthly_operation_fee ) * lr_software_item->hec_exchange_rate.

      INSERT VALUE #( data        = lr_software_item
                      node        = /hec1/if_configuration_c=>sc_node-software_item
                      source_node = /hec1/if_configuration_c=>sc_node-material
                      association = /hec1/if_configuration_c=>sc_association-software_item-to_parent
                      source_key  = lr_software_item->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_software_item->key                                             ) INTO TABLE lt_modification.

    ENDLOOP.

    "-----------------------------------
    " DB Node
    "-----------------------------------
    LOOP AT lt_db_node REFERENCE INTO DATA(lr_db_node).

      lr_db_node->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.
      lr_db_node->hec_apm_fx_rate_date = ls_apm-hec_apm_fx_rate_date.

      /hec1/cl_config_helper=>do_currency_exchange( EXPORTING iv_currency_from   = 'EUR'
                                                              iv_currency_amount = lr_db_node->hec_monthly_setup_fee + lr_db_node->hec_monthly_operation_fee
                                                              iv_currency_to     = ls_landscape-hec_ls_contract_curr
                                                              iv_date            = ls_apm-hec_apm_fx_rate_date
                                                    IMPORTING ev_exchange_rate   = lr_db_node->hec_exchange_rate
                                                              ev_exchange_value  = lr_db_node->hec_exchange_value ).

*      lr_db_node->hec_exchange_rate = /hec1/cl_config_helper=>get_exchange_rate( iv_currency_from = 'EUR'
*                                                                                 iv_currency_to   = ls_landscape-hec_ls_contract_curr
*                                                                                 iv_date          = ls_apm-hec_apm_fx_rate_date       ).
*
*      lr_db_node->hec_exchange_value = ( lr_db_node->hec_monthly_setup_fee + lr_db_node->hec_monthly_operation_fee ) * lr_db_node->hec_exchange_rate.

      INSERT VALUE #( data        = lr_db_node
                      node        = /hec1/if_configuration_c=>sc_node-db_node
                      source_node = /hec1/if_configuration_c=>sc_node-instance_db
                      association = /hec1/if_configuration_c=>sc_association-db_node-to_parent
                      source_key  = lr_db_node->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_db_node->key                                              ) INTO TABLE lt_modification.

    ENDLOOP.



    "-----------------------------------
    " DB Server
    "-----------------------------------
    LOOP AT lt_db_server REFERENCE INTO DATA(lr_db_server).

      lr_db_server->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.
      lr_db_server->hec_apm_fx_rate_date = ls_apm-hec_apm_fx_rate_date.

      /hec1/cl_config_helper=>do_currency_exchange( EXPORTING iv_currency_from   = 'EUR'
                                                              iv_currency_amount = lr_db_server->hec_month_price_eur
                                                              iv_currency_to     = ls_landscape-hec_ls_contract_curr
                                                              iv_date            = ls_apm-hec_apm_fx_rate_date
                                                    IMPORTING ev_exchange_rate   = lr_db_server->hec_exchange_rate
                                                              ev_exchange_value  = lr_db_server->hec_exchange_value ).

*      lr_db_server->hec_exchange_rate = /hec1/cl_config_helper=>get_exchange_rate( iv_currency_from = 'EUR'
*                                                                                   iv_currency_to   = ls_landscape-hec_ls_contract_curr
*                                                                                   iv_date          = ls_apm-hec_apm_fx_rate_date       ).
*
*      lr_db_server->hec_exchange_value = ( lr_db_server->hec_month_price_eur ) * lr_db_server->hec_exchange_rate.

      INSERT VALUE #( data        = lr_db_server
                      node        = /hec1/if_configuration_c=>sc_node-db_server
                      source_node = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                      association = /hec1/if_configuration_c=>sc_association-db_server-to_parent
                      source_key  = lr_db_server->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_db_server->key                                              ) INTO TABLE lt_modification.

    ENDLOOP.



    "-----------------------------------
    " DB Storage
    "-----------------------------------
    LOOP AT lt_db_storage REFERENCE INTO DATA(lr_db_storage).

      lr_db_storage->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.
      lr_db_storage->hec_apm_fx_rate_date = ls_apm-hec_apm_fx_rate_date.

      /hec1/cl_config_helper=>do_currency_exchange( EXPORTING iv_currency_from   = 'EUR'
                                                              iv_currency_amount = lr_db_storage->hec_month_price_fee
                                                              iv_currency_to     = ls_landscape-hec_ls_contract_curr
                                                              iv_date            = ls_apm-hec_apm_fx_rate_date
                                                    IMPORTING ev_exchange_rate   = lr_db_storage->hec_exchange_rate
                                                              ev_exchange_value  = lr_db_storage->hec_exchange_value ).

*      lr_db_storage->hec_exchange_rate = /hec1/cl_config_helper=>get_exchange_rate( iv_currency_from = 'EUR'
*                                                                                    iv_currency_to   = ls_landscape-hec_ls_contract_curr
*                                                                                    iv_date          = ls_apm-hec_apm_fx_rate_date       ).
*
*      lr_db_storage->hec_exchange_value = ( lr_db_storage->hec_month_price_fee ) * lr_db_storage->hec_exchange_rate.

      INSERT VALUE #( data        = lr_db_storage
                      node        = /hec1/if_configuration_c=>sc_node-db_storage
                      source_node = /hec1/if_configuration_c=>sc_node-db_server
                      association = /hec1/if_configuration_c=>sc_association-db_storage-to_parent
                      source_key  = lr_db_storage->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_db_storage->key                                                        ) INTO TABLE lt_modification.

    ENDLOOP.



    "-----------------------------------
    " DB Backup
    "-----------------------------------
    LOOP AT lt_db_backup REFERENCE INTO DATA(lr_db_backup).

      lr_db_backup->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.
      lr_db_backup->hec_apm_fx_rate_date = ls_apm-hec_apm_fx_rate_date.

      /hec1/cl_config_helper=>do_currency_exchange( EXPORTING iv_currency_from   = 'EUR'
                                                              iv_currency_amount = lr_db_backup->hec_backup_month_price_fee
                                                              iv_currency_to     = ls_landscape-hec_ls_contract_curr
                                                              iv_date            = ls_apm-hec_apm_fx_rate_date
                                                    IMPORTING ev_exchange_rate   = lr_db_backup->hec_exchange_rate
                                                              ev_exchange_value  = lr_db_backup->hec_exchange_value ).

*      lr_db_backup->hec_exchange_rate = /hec1/cl_config_helper=>get_exchange_rate( iv_currency_from = 'EUR'
*                                                                                   iv_currency_to   = ls_landscape-hec_ls_contract_curr
*                                                                                   iv_date          = ls_apm-hec_apm_fx_rate_date       ).
*
*      lr_db_backup->hec_exchange_value = ( lr_db_backup->hec_backup_month_price_fee ) * lr_db_backup->hec_exchange_rate.

      INSERT VALUE #( data        = lr_db_backup
                      node        = /hec1/if_configuration_c=>sc_node-db_storage_backup
                      source_node = /hec1/if_configuration_c=>sc_node-db_storage
                      association = /hec1/if_configuration_c=>sc_association-db_storage_backup-to_parent
                      source_key  = lr_db_backup->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_db_backup->key                                                        ) INTO TABLE lt_modification.

    ENDLOOP.



    "-----------------------------------
    " App Server Performance Category
    "-----------------------------------
    LOOP AT lt_app_serv_perf_cat REFERENCE INTO DATA(lr_app_serv_perf_cat).

      lr_app_serv_perf_cat->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.
      lr_app_serv_perf_cat->hec_apm_fx_rate_date = ls_apm-hec_apm_fx_rate_date.

      /hec1/cl_config_helper=>do_currency_exchange( EXPORTING iv_currency_from   = 'EUR'
                                                              iv_currency_amount = lr_app_serv_perf_cat->hec_monthly_setup_fee + lr_app_serv_perf_cat->hec_monthly_operation_fee
                                                              iv_currency_to     = ls_landscape-hec_ls_contract_curr
                                                              iv_date            = ls_apm-hec_apm_fx_rate_date
                                                    IMPORTING ev_exchange_rate   = lr_app_serv_perf_cat->hec_exchange_rate
                                                              ev_exchange_value  = lr_app_serv_perf_cat->hec_exchange_value ).


      INSERT VALUE #( data        = lr_app_serv_perf_cat
                      node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                      source_node = /hec1/if_configuration_c=>sc_node-app_node
                      association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_parent
                      source_key  = lr_app_serv_perf_cat->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_app_serv_perf_cat->key                                                  ) INTO TABLE lt_modification.

    ENDLOOP.



    "-----------------------------------
    " App Server
    "-----------------------------------
    LOOP AT lt_app_server REFERENCE INTO DATA(lr_app_server).

      lr_app_server->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.
      lr_app_server->hec_apm_fx_rate_date = ls_apm-hec_apm_fx_rate_date.

      /hec1/cl_config_helper=>do_currency_exchange( EXPORTING iv_currency_from   = 'EUR'
                                                              iv_currency_amount = lr_app_server->hec_month_price_eur
                                                              iv_currency_to     = ls_landscape-hec_ls_contract_curr
                                                              iv_date            = ls_apm-hec_apm_fx_rate_date
                                                    IMPORTING ev_exchange_rate   = lr_app_server->hec_exchange_rate
                                                              ev_exchange_value  = lr_app_server->hec_exchange_value ).


      INSERT VALUE #( data        = lr_app_server
                      node        = /hec1/if_configuration_c=>sc_node-app_server
                      source_node = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                      association = /hec1/if_configuration_c=>sc_association-app_server-to_parent
                      source_key  = lr_app_server->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_app_server->key                                             ) INTO TABLE lt_modification.

    ENDLOOP.



    "-----------------------------------
    " App Storage
    "-----------------------------------
    LOOP AT lt_app_storage REFERENCE INTO DATA(lr_app_storage).

      lr_app_storage->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.
      lr_app_storage->hec_apm_fx_rate_date = ls_apm-hec_apm_fx_rate_date.

      /hec1/cl_config_helper=>do_currency_exchange( EXPORTING iv_currency_from   = 'EUR'
                                                              iv_currency_amount = lr_app_storage->hec_month_price_fee
                                                              iv_currency_to     = ls_landscape-hec_ls_contract_curr
                                                              iv_date            = ls_apm-hec_apm_fx_rate_date
                                                    IMPORTING ev_exchange_rate   = lr_app_storage->hec_exchange_rate
                                                              ev_exchange_value  = lr_app_storage->hec_exchange_value ).


      INSERT VALUE #( data        = lr_app_storage
                      node        = /hec1/if_configuration_c=>sc_node-app_storage
                      source_node = /hec1/if_configuration_c=>sc_node-app_server
                      association = /hec1/if_configuration_c=>sc_association-app_storage-to_parent
                      source_key  = lr_app_storage->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_app_storage->key                                              ) INTO TABLE lt_modification.

    ENDLOOP.



    "-----------------------------------
    " App Backup
    "-----------------------------------
    LOOP AT lt_app_backup REFERENCE INTO DATA(lr_app_backup).

      lr_app_backup->hec_exchange_currency = ls_landscape-hec_ls_contract_curr.
      lr_app_backup->hec_apm_fx_rate_date = ls_apm-hec_apm_fx_rate_date.

      /hec1/cl_config_helper=>do_currency_exchange( EXPORTING iv_currency_from   = 'EUR'
                                                              iv_currency_amount = lr_app_backup->hec_backup_month_price_fee
                                                              iv_currency_to     = ls_landscape-hec_ls_contract_curr
                                                              iv_date            = ls_apm-hec_apm_fx_rate_date
                                                    IMPORTING ev_exchange_rate   = lr_app_backup->hec_exchange_rate
                                                              ev_exchange_value  = lr_app_backup->hec_exchange_value ).


      INSERT VALUE #( data        = lr_app_backup
                      node        = /hec1/if_configuration_c=>sc_node-app_storage_backup
                      source_node = /hec1/if_configuration_c=>sc_node-app_storage
                      association = /hec1/if_configuration_c=>sc_association-app_storage_backup-to_parent
                      source_key  = lr_app_backup->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_app_backup->key                                                        ) INTO TABLE lt_modification.

    ENDLOOP.

    "-----------------------------------
    " Update Instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change) ).
    ENDIF.
  ENDMETHOD.


  METHOD /bobf/if_frw_action~execute.

    TRY.
        CASE is_ctx-act_key.
            " **********************************
            " Create Datacenter
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-delivery_unit-create_datacenter.
            me->create_datacenter( EXPORTING is_ctx                  = is_ctx
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
            " Create Datacenter - Disaster Recovery
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-datacenter-create_dr_datacenter.
            me->create_dr_datacenter( EXPORTING is_ctx                  = is_ctx
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
            " Create Connectivity
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-datacenter-create_connectivity.
            me->create_connectivity( EXPORTING is_ctx                  = is_ctx
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
            " Create Contact
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-create_contact.
            me->create_contact( EXPORTING is_ctx                  = is_ctx
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
            " Create Contact Reference
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-contact-create_contact_reference.
            me->create_contact_reference( EXPORTING is_ctx                  = is_ctx
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
            " Create Additional Service
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-create_add_service.
            me->create_add_service( EXPORTING is_ctx                  = is_ctx
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
            " Create DR Tier
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-tier-create_dr_tier.
            me->create_dr_tier( EXPORTING is_ctx                  = is_ctx
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
            " Create Additional Tier Service
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-tier-create_tier_add_service.
            me->create_tier_add_service( EXPORTING is_ctx                  = is_ctx
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
            " Create Additional Tier Longterm backup
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-tier-create_tier_lt_backup.
            me->create_tier_lt_backup( EXPORTING is_ctx                  = is_ctx
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
            " Create Additional Tier Additional Storage
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-tier-create_tier_add_storage.
            me->create_tier_add_storage( EXPORTING is_ctx                  = is_ctx
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
            " Create Solution
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-create_solution.
            me->create_solution( EXPORTING is_ctx                  = is_ctx
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
            " Create Transport Path
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-solution-create_transport_path.
            me->create_transport_path( EXPORTING is_ctx                  = is_ctx
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
            " Create Network Segment
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-infrastructure_baseline-create_network_segment.
            me->create_network_segment( EXPORTING is_ctx                  = is_ctx
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
            " Do price update
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-do_price_update.
            me->update_pricing( EXPORTING is_ctx                  = is_ctx
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
            " Do price aggregation
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-do_price_aggregation.
            me->do_price_aggregation( EXPORTING is_ctx                  = is_ctx
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
            " Convert currency
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-convert_currency.
            me->convert_currency( EXPORTING is_ctx                  = is_ctx
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
            " Landscape
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-modify_config_status
            OR /hec1/if_configuration_c=>sc_action-root-modify_acc_dlvy_category
            OR /hec1/if_configuration_c=>sc_action-root-modify_cloud_offering
            OR /hec1/if_configuration_c=>sc_action-root-reset_currency
            OR /hec1/if_configuration_c=>sc_action-root-reset_dlvy_region_l1
            OR /hec1/if_configuration_c=>sc_action-root-reset_dlvy_region_l2
            OR /hec1/if_configuration_c=>sc_action-root-reset_dlvy_region_l3.
            me->reset_landscape( EXPORTING is_ctx                  = is_ctx
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
            " Reset Delivery Unit
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-delivery_unit-modify_delivery_unit
            OR /hec1/if_configuration_c=>sc_action-delivery_unit-modify_inf_provider.
            me->reset_delivery_unit( EXPORTING is_ctx                  = is_ctx
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
            " Reset Datacenter
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-datacenter-modify_datacenter.
            me->reset_datacenter( EXPORTING is_ctx                  = is_ctx
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
            " Reset Connectivity
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-connectivity-reset_connectivity.
            me->reset_connectivity( EXPORTING is_ctx                  = is_ctx
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
            " Reset Additional Services
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-add_service-modify_datac_assignment
            OR /hec1/if_configuration_c=>sc_action-add_service-reset_service_class
            OR /hec1/if_configuration_c=>sc_action-add_service-modify_service.
            me->reset_add_service( EXPORTING is_ctx                  = is_ctx
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
            " Reset Longterm Backup Data Center
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-lt_backup_datacenter-modify_datac_assignment.


            " **********************************
            " Reset Longterm Backup Class
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-lt_backup_class-reset_backup_class.


            " **********************************
            " Reset Solution
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-solution-reset_solution
            OR /hec1/if_configuration_c=>sc_action-solution-reset_implementation_type.
            me->reset_solution( EXPORTING is_ctx                  = is_ctx
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
            " Reset Tier
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-tier-modify_datac_assignment
            OR /hec1/if_configuration_c=>sc_action-tier-reset_implementation_type
            OR /hec1/if_configuration_c=>sc_action-tier-reset_tier_type.

            me->reset_tier( EXPORTING is_ctx                  = is_ctx
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
            " Create Successor SLA
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-tier_sla-create_successor_sla.



            " **********************************
            " Reset Tier SLA
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-tier_sla-reset_sla.



            " **********************************
            " Reset Additional Tier Services
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-tier_add_service-reset_service_ref.



            " **********************************
            " Reset Tier Longterm Backup
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-tier_longterm_backup-reset_backup_class_ref.



            " **********************************
            " Get Software/Material List
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-solution-get_material_list
            OR /hec1/if_configuration_c=>sc_action-solution-get_software_item_list.
            me->get_software( EXPORTING is_ctx                  = is_ctx
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
            " Select/Deselect Software/Material
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-solution-select_material
            OR /hec1/if_configuration_c=>sc_action-solution-select_software_item.
            me->select_software( EXPORTING is_ctx                  = is_ctx
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
            " Is phase assignment allowed?
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-is_phase_assign_allowed.
            me->is_phase_assign_allowed( EXPORTING is_ctx                  = is_ctx
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
            " Delete Node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-delete_node.
            me->delete_node( EXPORTING is_ctx                  = is_ctx
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
            " Copy Node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-copy_node.
            me->copy_node( EXPORTING is_ctx                  = is_ctx
                                     it_key                  = it_key
                                     io_read                 = io_read
                                     io_modify               = io_modify
                                     is_parameters           = is_parameters
                           IMPORTING eo_message              = eo_message
                                     et_failed_key           = et_failed_key
                                     ev_static_action_failed = ev_static_action_failed
                                     et_data                 = et_data
                                     et_data_link            = et_data_link ).

          WHEN /hec1/if_configuration_c=>sc_action-root-apm_change.
            me->apm_change( EXPORTING is_ctx                  = is_ctx
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
            " Create Change Request
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-create_cr.
            me->create_cr( EXPORTING is_ctx                  = is_ctx
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
            " Clone Change Request
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-clone_cr.
            me->clone_cr( EXPORTING is_ctx                  = is_ctx
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
            " Create CMS Case for Change Request
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-create_cr_cms_case.
            me->create_cr_cms_case( EXPORTING is_ctx                  = is_ctx
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
            " Check APM Validity
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-check_apm_validity.
            me->check_apm_validity( EXPORTING is_ctx                  = is_ctx
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
            " Copy to New Configuration
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-copy_to_new_config.
            me->copy_to_new_config( EXPORTING is_ctx                  = is_ctx
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
            " Get App/DB Node HA Type
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-get_ha_type.
            me->get_ha_type( EXPORTING is_ctx                  = is_ctx
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
            " Delete Node for CR
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-delete_node_cr.
            me->delete_node_cr( EXPORTING   is_ctx                  = is_ctx
                                            it_key                  = it_key
                                            io_read                 = io_read
                                            io_modify               = io_modify
                                            is_parameters           = is_parameters
                                 IMPORTING  eo_message              = eo_message
                                            et_failed_key           = et_failed_key
                                            ev_static_action_failed = ev_static_action_failed
                                            et_data                 = et_data
                                            et_data_link            = et_data_link ).

        ENDCASE.
      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.

  ENDMETHOD.


  METHOD get_ha_type.

    DATA: lv_app_node             TYPE boole_d,
          lv_clust_node_type_guid TYPE /hec1/cluster_node_type_guid,
          lv_prov_date            TYPE /hec1/ha_provisioning_date.

    FIELD-SYMBOLS: <fs_parameters> TYPE /hec1/s_act_import_parameter.



    ASSIGN is_parameters->* TO <fs_parameters>.

    IF <fs_parameters> IS ASSIGNED.
      LOOP AT <fs_parameters>-name_value ASSIGNING FIELD-SYMBOL(<fs_param>).
        CASE <fs_param>-fieldname.
          WHEN 'APP_SERVER_NODE'.
            lv_app_node = <fs_param>-value.
          WHEN 'HEC_CLUST_NODE_TYPE_GUID'.
            lv_clust_node_type_guid = <fs_param>-value.
          WHEN 'HEC_HA_TYPE_PROV_DATE'.
            lv_prov_date = <fs_param>-value.
        ENDCASE.
      ENDLOOP.
    ENDIF. " IF <fs_parameters> IS ASSIGNED.


    IF lv_prov_date            IS NOT INITIAL AND
       lv_clust_node_type_guid IS NOT INITIAL.
      et_data = /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_ha_type( iv_app_server_node        = lv_app_node
                                                                                            iv_cluster_node_type_guid = lv_clust_node_type_guid
                                                                                            iv_provisioning_date      = lv_prov_date            ).
    ENDIF.




  ENDMETHOD.


  METHOD copy_node.
    FIELD-SYMBOLS <ls_parameters> TYPE /hec1/s_act_copy_node.

    "disable determinations on create
    /hec1/cl_lib_d_superclass=>set_switch( abap_false ).

    /hec1/cl_lib_d_superclass=>set_tree_switch( abap_false ).

    TRY.

        ASSIGN is_parameters->* TO <ls_parameters>.
        IF sy-subrc <> 0.
          " Parameter structure could not be assigned for action copy
          RAISE EXCEPTION TYPE /hec1/cx_copy_control MESSAGE ID '/HEC1/MSG_BOPF_COPY' NUMBER 001.
        ENDIF.

        DATA(lt_data) = NEW /hec1/cl_copy_controller(
           iv_bo_key         = is_ctx-bo_key
           io_read           = io_read
           io_modify         = io_modify
           iv_node_key       = <ls_parameters>-node_key
           it_key            = VALUE #( ( key = <ls_parameters>-key ) )
           iv_mode           = <ls_parameters>-mode
         )->copy( ).

        io_modify->end_modify( EXPORTING iv_process_immediately = abap_true IMPORTING eo_change = DATA(lo_change) ).


        IF et_data IS SUPPLIED.
          et_data = CORRESPONDING #( lt_data ).
        ENDIF.

      CATCH cx_root INTO DATA(lo_ex).
        "in case of error =>
        /hec1/cl_lib_d_superclass=>set_switch( abap_true ).
        /hec1/cl_lib_d_superclass=>set_tree_switch( abap_true ).
        ev_static_action_failed = abap_true.
        eo_message->add_exception( lo_ex ).
    ENDTRY.

    "enable determinations on create
    /hec1/cl_lib_d_superclass=>set_switch( abap_true ).
    /hec1/cl_lib_d_superclass=>set_tree_switch( abap_true ).

  ENDMETHOD.


  METHOD create_contact.

    DATA: lt_landscape    TYPE /hec1/t_config_root_ct,
          lt_modification TYPE /bobf/t_frw_modification.

    FIELD-SYMBOLS: <fs_param> TYPE /hec1/s_act_create_contact.

    CLEAR: eo_message,
           et_failed_key.

    IF eo_message IS NOT BOUND.
      eo_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    ASSIGN is_parameters->* TO <fs_param>.

    io_read->get_root_key( EXPORTING iv_node       = is_ctx-node_key
                                     it_key        = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).

    io_read->retrieve( EXPORTING iv_node = /hec1/if_configuration_c=>sc_node-root
                                 it_key  = lt_root_key
                       IMPORTING et_data = lt_landscape ).

    " There is only ever one landscape!
    TRY.
        DATA(ls_landscape) = lt_landscape[ 1 ].
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

    "-----------------------------------
    " add contact
    "-----------------------------------
    DATA(lr_contact) = NEW /hec1/s_data_contact_cs( BASE CORRESPONDING #( ls_landscape )
                                                         parent_key          = ls_landscape-key
                                                         key                 = /bopf/cl_frw_factory=>get_new_key( )
                                                         hec_node_contact    = /rbp/cl_general_utilities=>get_new_guid22( )
                                                         hec_contact_type    = COND #( WHEN <fs_param> IS ASSIGNED
                                                                                       THEN <fs_param>-hec_contact_type )
                                                        " hec_apm_guid        = ls_landscape-hec_apm_guid
                                                        " hec_apm_descr       = ls_landscape-hec_apm_descr
                                                         hec_row_selectable  = abap_true
                                                         hec_delete_visible  = abap_true
                                                         crea_uname          = sy-uname ).

    GET TIME STAMP FIELD lr_contact->crea_date_time.

    INSERT VALUE #( data        = lr_contact
                    node        = /hec1/if_configuration_c=>sc_node-contact
                    source_node = /hec1/if_configuration_c=>sc_node-root
                    association = /hec1/if_configuration_c=>sc_association-root-contact
                    source_key  = ls_landscape-key
                    change_mode = /bobf/if_frw_c=>sc_modify_create
                    key         = lr_contact->key
                    ) INTO TABLE lt_modification.

    "-----------------------------------
    " Create instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change) ).
    ENDIF.

    INSERT lr_contact->* INTO TABLE et_data.

  ENDMETHOD.


  METHOD apm_change.
**********************************************************************
* /hec1/s_act_copy_node
* key       - node instance key (Tier1 of the node type Tier)
* node_key  - key of the node type (f.e. Tier)
* mode      - APM Change / /HEC1/CL_COPY_CONTROLLER=>GC_COPY_MODE-APM_CHANGE

    DATA:
      lt_bo_nodes  TYPE /bobf/t_frw_node,
      lt_root_data TYPE /hec1/t_config_root_ct.
    FIELD-SYMBOLS
      <ls_parameters> TYPE /hec1/s_act_apm_change.

    ASSIGN is_parameters->* TO <ls_parameters>.

    TRY.
        IF ( <ls_parameters> IS NOT ASSIGNED ).
          " Parameter structure could not be assigned for action copy
          RAISE EXCEPTION TYPE /hec1/cx_copy_control MESSAGE ID '/HEC1/MSG_BOPF_COPY' NUMBER 001.
        ENDIF.

        CASE <ls_parameters>-hec_contract_status.
          WHEN /hec1/if_config_constants=>gc_contract_status-initial.
            me->apm_change_init_deal(
              EXPORTING
                io_modify     = io_modify
                io_read       = io_read
                it_key        = it_key
                is_ctx        = is_ctx
                is_parameters = <ls_parameters>
              IMPORTING
                et_data       = et_data
            ).
          WHEN /hec1/if_config_constants=>gc_contract_status-change_request.
            me->apm_change_cr(
              EXPORTING
                io_modify     = io_modify
                io_read       = io_read
                it_key        = it_key
                is_ctx        = is_ctx
                is_parameters = <ls_parameters>
              IMPORTING
                et_data       = et_data ).
        ENDCASE.

      CATCH /hec1/cx_copy_control
            /bobf/cx_frw_contrct_violation
            /hec1/cx_standard_exception INTO DATA(lo_exception).

        ev_static_action_failed = abap_true.
        eo_message->add_exception( lo_exception ).

        "enable determinations on create
        /hec1/cl_lib_d_superclass=>set_switch( abap_true ).
        /hec1/cl_lib_d_superclass=>set_tree_switch( abap_true ).
    ENDTRY.

  ENDMETHOD.


  METHOD apm_change_init_deal.

    DATA lt_bo_nodes TYPE /bobf/t_frw_node.

    "disable determinations on create
    /hec1/cl_lib_d_superclass=>set_switch( abap_false ).
    /hec1/cl_lib_d_superclass=>set_tree_switch( abap_false ).

    DATA(lo_copy_controller_apm) = NEW /hec1/cl_copy_controller_apm(
      iv_bo_key     = is_ctx-bo_key
      io_read       = io_read
      io_modify     = io_modify
      it_key        = it_key
      iv_node_key   = is_ctx-node_key
      iv_target_apm = is_parameters-hec_target_apm_guid ).

    lt_bo_nodes = lo_copy_controller_apm->copy( ).

    io_modify->end_modify( EXPORTING iv_process_immediately = abap_true IMPORTING eo_change = DATA(lo_change) ).

    "enable determinations on create
    /hec1/cl_lib_d_superclass=>set_switch( abap_true ).
    /hec1/cl_lib_d_superclass=>set_tree_switch( abap_true ).


    DATA(ls_apm_config_data) = VALUE /hec1/s_apm_config_data( hec_confid          = is_parameters-hec_confid
                                                              hec_conf_version    = is_parameters-hec_conf_version
                                                              hec_target_apm_guid = is_parameters-hec_target_apm_guid
                                                              hec_target_apm_descr = is_parameters-hec_target_apm_descr
                                                              hec_material        = is_parameters-hec_material
                                                              hec_contract_status = is_parameters-hec_contract_status
                                                              bopf_read_object    = io_read
                                                              bopf_modify_object  = io_modify ).

    DATA(lo_apm_controller) = /hec1/cl_apm_controller=>get_instance( ).
    lo_apm_controller->set_apm_config_data( ls_apm_config_data ).

    " lt_bo_nodes contains all nodes of the new copied version, received from copy controller
    lo_apm_controller->apm_change( it_bo_nodes = lt_bo_nodes ).

    io_modify->end_modify( EXPORTING iv_process_immediately = abap_true IMPORTING eo_change = lo_change ).

    IF ( et_data IS SUPPLIED ).
      et_data = CORRESPONDING #( lt_bo_nodes ).
    ENDIF.

  ENDMETHOD.


  METHOD create_cr.

    FIELD-SYMBOLS <ls_parameters> TYPE /hec1/s_act_copy_node.

    "disable determinations on create
    /hec1/cl_lib_d_superclass=>set_switch( abap_false ).

    /hec1/cl_lib_d_superclass=>set_tree_switch( abap_false ).

    TRY.

        ASSIGN is_parameters->* TO <ls_parameters>.
        IF sy-subrc <> 0.
          " Parameter structure could not be assigned for action copy
          RAISE EXCEPTION TYPE /hec1/cx_copy_control MESSAGE ID '/HEC1/MSG_BOPF_COPY' NUMBER 001.
        ENDIF.

        DATA(lt_data) = NEW /hec1/cl_copy_controller_cr(
                  iv_bo_key         = is_ctx-bo_key
                  io_read           = io_read
                  io_modify         = io_modify
                  iv_node_key       = <ls_parameters>-node_key
                  it_key            = VALUE #( ( key = <ls_parameters>-key ) )
                  iv_mode           = <ls_parameters>-mode
                )->copy( ).

        io_modify->end_modify( EXPORTING iv_process_immediately = abap_true IMPORTING eo_change = DATA(lo_change) ).


        IF et_data IS SUPPLIED.
          et_data = CORRESPONDING #( lt_data ).
        ENDIF.

      CATCH cx_root INTO DATA(lo_ex).
        "in case of error =>
        /hec1/cl_lib_d_superclass=>set_switch( abap_true ).
        /hec1/cl_lib_d_superclass=>set_tree_switch( abap_true ).
        ev_static_action_failed = abap_true.
        eo_message->add_exception( lo_ex ).
    ENDTRY.

    "enable determinations on create
    /hec1/cl_lib_d_superclass=>set_switch( abap_true ).
    /hec1/cl_lib_d_superclass=>set_tree_switch( abap_true ).
  ENDMETHOD.


  METHOD clone_cr.

    FIELD-SYMBOLS <ls_parameters> TYPE /hec1/s_act_copy_node.

    "disable determinations on create
    /hec1/cl_lib_d_superclass=>set_switch( abap_false ).

    /hec1/cl_lib_d_superclass=>set_tree_switch( abap_false ).

    TRY.

        ASSIGN is_parameters->* TO <ls_parameters>.
        IF sy-subrc <> 0.
          " Parameter structure could not be assigned for action copy
          RAISE EXCEPTION TYPE /hec1/cx_copy_control MESSAGE ID '/HEC1/MSG_BOPF_COPY' NUMBER 001.
        ENDIF.

        DATA(lt_data) = NEW /hec1/cl_copy_controller_clone(
                  iv_bo_key         = is_ctx-bo_key
                  io_read           = io_read
                  io_modify         = io_modify
                  iv_node_key       = <ls_parameters>-node_key
                  it_key            = VALUE #( ( key = <ls_parameters>-key ) )
                  iv_mode           = <ls_parameters>-mode
                )->copy( ).

        io_modify->end_modify( EXPORTING iv_process_immediately = abap_true IMPORTING eo_change = DATA(lo_change) ).


        IF et_data IS SUPPLIED.
          et_data = CORRESPONDING #( lt_data ).
        ENDIF.

      CATCH cx_root INTO DATA(lo_ex).
        "in case of error =>
        /hec1/cl_lib_d_superclass=>set_switch( abap_true ).
        /hec1/cl_lib_d_superclass=>set_tree_switch( abap_true ).
        ev_static_action_failed = abap_true.
        eo_message->add_exception( lo_ex ).
    ENDTRY.

    "enable determinations on create
    /hec1/cl_lib_d_superclass=>set_switch( abap_true ).
    /hec1/cl_lib_d_superclass=>set_tree_switch( abap_true ).
  ENDMETHOD.


  METHOD create_contact_reference.

    " this is triggered through the contact
    " the triggering function must pass the contact as key and give the referenced node (tier, connectivity, network segment, ...) as parameters

    DATA: lt_contact      TYPE /hec1/t_data_contact_ct,
          lt_contact_ref  TYPE /hec1/t_data_contact_ref_ct,
          lt_modification TYPE /bobf/t_frw_modification.

    FIELD-SYMBOLS: <fs_param> TYPE /hec1/t_act_create_contact_ref.

    CLEAR: eo_message,
           et_failed_key.

    IF eo_message IS NOT BOUND.
      eo_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    ASSIGN is_parameters->* TO <fs_param>.

    io_read->get_root_key( EXPORTING iv_node       = is_ctx-node_key
                                     it_key        = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_contact ).

    LOOP AT lt_contact ASSIGNING FIELD-SYMBOL(<fs_contact>).

      ASSIGN <fs_param>[ key = <fs_contact>-key ] TO FIELD-SYMBOL(<fs_param_line>).
      CHECK <fs_param_line> IS NOT INITIAL.

      "-----------------------------------
      " add contact reference
      "-----------------------------------
      DATA(lr_contact_ref) = NEW /hec1/s_data_contact_ref_cs( BASE CORRESPONDING #( <fs_contact> )
                                    parent_key                = <fs_contact>-key
                                    key                       = /bopf/cl_frw_factory=>get_new_key( )
                                    hec_node_contact          = <fs_contact>-hec_node_contact
                                    hec_node_contact_ref      = /rbp/cl_general_utilities=>get_new_guid22( )
                                    hec_contact_ref_node_type = <fs_param_line>-hec_contact_ref_node_type
                                    hec_contact_ref_node_key  = <fs_param_line>-hec_contact_ref_node_key
                                    hec_row_selectable        = abap_true
                                    hec_delete_visible        = abap_true
                                    crea_uname                = sy-uname ).

      GET TIME STAMP FIELD lr_contact_ref->crea_date_time.

      INSERT VALUE #( data        = lr_contact_ref
                      node        = /hec1/if_configuration_c=>sc_node-contact_reference
                      source_node = /hec1/if_configuration_c=>sc_node-contact
                      association = /hec1/if_configuration_c=>sc_association-contact-contact_reference
                      source_key  = lr_contact_ref->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = lr_contact_ref->key
                      ) INTO TABLE lt_modification.

      INSERT lr_contact_ref->* INTO TABLE lt_contact_ref.

      UNASSIGN <fs_param_line>.

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

    et_data = lt_contact_ref.

  ENDMETHOD.


  METHOD create_transport_path.

    DATA: lt_solution     TYPE /hec1/t_data_solution_ct,
          lt_modification TYPE /bobf/t_frw_modification.

*    FIELD-SYMBOLS: <fs_param> TYPE /hec1/s_act_create_transport_path.

    CLEAR: eo_message,
           et_failed_key.

    IF eo_message IS NOT BOUND.
      eo_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

*    ASSIGN is_parameters->* TO <fs_param>.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_solution ).

    LOOP AT lt_solution ASSIGNING FIELD-SYMBOL(<fs_solution>).
      "-----------------------------------
      " add transport path
      "-----------------------------------
      DATA(lr_transport_path) = NEW /hec1/s_data_transport_path_cs( BASE CORRESPONDING #( <fs_solution> )
                                                                    parent_key               = <fs_solution>-key
                                                                    key                      = /bopf/cl_frw_factory=>get_new_key( )
                                                                    hec_node_transport_path  = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                    hec_row_selectable       = abap_true
                                                                    hec_delete_visible       = abap_true
                                                                    crea_uname               = sy-uname ).

      GET TIME STAMP FIELD lr_transport_path->crea_date_time.

      INSERT VALUE #( data        = lr_transport_path
                      node        = /hec1/if_configuration_c=>sc_node-transport_path
                      source_node = /hec1/if_configuration_c=>sc_node-solution
                      association = /hec1/if_configuration_c=>sc_association-solution-transport_path
                      source_key  = lr_transport_path->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = lr_transport_path->key
                      ) INTO TABLE lt_modification.

    ENDLOOP. "lt_solution

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


  METHOD update_modification_type.

    DATA: lt_modification  TYPE /bobf/t_frw_modification.

    DATA: para              TYPE tpara-paramid VALUE '/HEC1/CONFIG_DEBUG',
          ls_debug_own_code TYPE /hec1/s_config_debug_modus.

    GET PARAMETER ID para FIELD ls_debug_own_code.
*
*    "Safety first
*    IF ls_debug_own_code-hec_debug_modus      = abap_true AND "Todo (remove before transport  )
*       ls_debug_own_code-hec_debuf_modus_vers = '09'.

    CHECK is_ctx-node_key = /hec1/if_configuration_c=>sc_node-root.

    /hec1/cl_config_helper=>get_price_relevant_node_data( EXPORTING is_ctx                     = CORRESPONDING #( is_ctx )
                                                                    it_key                     = it_key
                                                                    io_read                    = io_read
                                                          IMPORTING et_landscape               = DATA(lt_landscape)
                                                                    et_phase                   = DATA(lt_phase)
                                                                    et_managed_serv_baseline   = DATA(lt_man_serv_base)
                                                                    et_delivery_unit           = DATA(lt_delivery_unit)
                                                                    et_infra_struc_baseline    = DATA(lt_inf_base)
                                                                    et_connectivity            = DATA(lt_connectivity)
                                                                    et_add_service             = DATA(lt_add_service)
                                                                    et_lt_backup_datacenter    = DATA(lt_lt_backup_datacenter)
                                                                    et_lt_backup_class         = DATA(lt_lt_backup_class)
                                                                    et_lt_backup_amount        = DATA(lt_lt_backup_amount)
                                                                    et_tier                    = DATA(lt_tier)
                                                                    et_tier_add_service        = DATA(lt_tier_add_service)
                                                                    et_db_node                 = DATA(lt_db_node)
                                                                    et_db_server               = DATA(lt_db_server)
                                                                    et_db_storage              = DATA(lt_db_storage)
                                                                    et_db_backup               = DATA(lt_db_backup)
                                                                    et_app_serv_perf_cat       = DATA(lt_app_serv_perf_cat)
                                                                    et_app_server              = DATA(lt_app_server)
                                                                    et_app_storage             = DATA(lt_app_storage)
                                                                    et_app_backup              = DATA(lt_app_backup)
                                                                    et_tier_price_phase        = DATA(lt_tier_price_old)
                                                                    et_lt_backup_price_phase   = DATA(lt_lt_backup_old)
                                                                    et_add_storage_price_phase = DATA(lt_add_storage_old) ).


    DATA(ls_landscape) = VALUE #( lt_landscape[ 1 ] OPTIONAL ).
    DATA(ls_man_svc_baseline) = VALUE #( lt_man_serv_base[ 1 ] OPTIONAL ).

    CHECK: ls_man_svc_baseline IS NOT INITIAL,
           ls_landscape IS NOT INITIAL.


    /hec1/cl_rep_config_data=>read_config_data( EXPORTING i_config_id       = ls_landscape-hec_confid
                                                          i_config_version  = ls_landscape-hec_conf_version
                                                IMPORTING es_config_head    = DATA(ls_config_head)
                                                          et_config_data    = DATA(lt_config_data)
                                                          et_cfg_price_data = DATA(lt_price_data)
                                                          e_subrc           = DATA(l_subrc) ).

    LOOP AT lt_config_data[] ASSIGNING FIELD-SYMBOL(<ls_tier_data>)
      WHERE level_id = /hec1/cl_rep_config_data=>c_level_tier.

      READ TABLE lt_tier ASSIGNING FIELD-SYMBOL(<ls_tier>) WITH KEY hec_node_solution = <ls_tier_data>-hec_node_solution hec_node_tier = <ls_tier_data>-hec_node_tier.
      IF sy-subrc <> 0.
        EXIT.
      ENDIF.

      DATA(lt_tier_subtree_data) = /hec1/cl_rep_config_data=>get_subtree( EXPORTING it_config_data = lt_config_data[]
                                                                                    i_row_id       = <ls_tier_data>-row_id ).

      DATA(lr_tier) = NEW /hec1/s_data_tier_cs( CORRESPONDING #( <ls_tier> ) ) .

      IF lr_tier->hec_comp_mod_type IS NOT INITIAL.
        CONTINUE.
      ENDIF.

      LOOP AT lt_tier_subtree_data ASSIGNING FIELD-SYMBOL(<ls_tier_subtree>).

        CASE <ls_tier_subtree>-hec_comp_mod_type.

          WHEN '01'. "01 Added
            lr_tier->hec_comp_mod_type = '02'. "02 Changed
            EXIT.
          WHEN '02'. "02 Changed
            lr_tier->hec_comp_mod_type = '02'. "02 Changed
            EXIT.
          WHEN '03'. "03 Deleted
            lr_tier->hec_comp_mod_type = '02'. "02 Changed
            EXIT.
          WHEN '04'. "04 Retired
            lr_tier->hec_comp_mod_type = '02'. "02 Changed
            EXIT.
          WHEN '05'. "05 Replaced
            lr_tier->hec_comp_mod_type = '02'. "02 Changed
            EXIT.
          WHEN '06'. "06 Phase shifted
            lr_tier->hec_comp_mod_type = '02'. "02 Changed
            EXIT.
          WHEN '07'. "07 Reconfigured
            lr_tier->hec_comp_mod_type = '02'. "02 Changed
            EXIT.

        ENDCASE.

      ENDLOOP.

      INSERT VALUE #( data        = lr_tier
                      node        = /hec1/if_configuration_c=>sc_node-tier
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_tier->key                           ) INTO TABLE lt_modification.


    ENDLOOP.


    LOOP AT lt_config_data[] ASSIGNING FIELD-SYMBOL(<ls_config_data_ltb_dc>)
      WHERE level_id = /hec1/cl_rep_config_data=>c_level_ltb_datacenter.

      READ TABLE lt_lt_backup_datacenter ASSIGNING FIELD-SYMBOL(<ls_ltb_dc>) WITH KEY hec_node_lt_backup_dc = <ls_config_data_ltb_dc>-hec_node_id.
      IF sy-subrc <> 0.
        EXIT.
      ENDIF.

      DATA(lt_ltb_dc_subtree_data) = /hec1/cl_rep_config_data=>get_subtree( EXPORTING it_config_data = lt_config_data[]
                                                                                      i_row_id       = <ls_config_data_ltb_dc>-row_id ).

      DATA(lr_ltb_dc) = NEW /hec1/s_data_lt_backup_dc_cs( CORRESPONDING #( <ls_ltb_dc> ) ) .

      IF lr_ltb_dc->hec_comp_mod_type IS NOT INITIAL.
        CONTINUE.
      ENDIF.

      LOOP AT lt_ltb_dc_subtree_data ASSIGNING FIELD-SYMBOL(<ls_ltb_dc_subtree>).

        CASE <ls_ltb_dc_subtree>-hec_comp_mod_type.

          WHEN '01'. "01 Added
            lr_ltb_dc->hec_comp_mod_type = '02'. "02 Changed
            EXIT.
          WHEN '02'. "02 Changed
            lr_ltb_dc->hec_comp_mod_type = '02'. "02 Changed
            EXIT.
          WHEN '03'. "03 Deleted
            lr_ltb_dc->hec_comp_mod_type = '02'. "02 Changed
            EXIT.
          WHEN '04'. "04 Retired
            lr_ltb_dc->hec_comp_mod_type = '02'. "02 Changed
            EXIT.
          WHEN '05'. "05 Replaced
            lr_ltb_dc->hec_comp_mod_type = '02'. "02 Changed
            EXIT.
          WHEN '06'. "06 Phase shifted
            lr_ltb_dc->hec_comp_mod_type = '02'. "02 Changed
            EXIT.
          WHEN '07'. "07 Reconfigured
            lr_ltb_dc->hec_comp_mod_type = '02'. "02 Changed
            EXIT.

        ENDCASE.

      ENDLOOP.

      INSERT VALUE #( data        = lr_ltb_dc
                      node        = /hec1/if_configuration_c=>sc_node-lt_backup_datacenter
                      change_mode = /bobf/if_frw_c=>sc_modify_update
                      key         = lr_ltb_dc->key                           ) INTO TABLE lt_modification.


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

  ENDMETHOD.


  METHOD create_cr_cms_case.

    DATA: lt_landscape TYPE /hec1/t_config_root_ct.
    DATA: lt_modification  TYPE /bobf/t_frw_modification.
    DATA: l_cms_case_id TYPE scmg_ext_key.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_landscape ).

    DATA(ls_landscape) = VALUE #( lt_landscape[ 1 ] OPTIONAL ).

    CHECK ls_landscape IS NOT INITIAL.


    /hec1/cl_config_helper=>create_cr_cms_case( EXPORTING is_landscape   = ls_landscape
                                                IMPORTING ev_cms_case_id = l_cms_case_id ).


    DATA(lr_landscape) = NEW /hec1/s_config_root_cs( BASE CORRESPONDING
                              #( ls_landscape )
      hec_ls_cms_case_id_cr = l_cms_case_id ).

    INSERT VALUE #( data        = lr_landscape
                    node        = /hec1/if_configuration_c=>sc_node-root
                    change_mode = /bobf/if_frw_c=>sc_modify_update
                    key         = lr_landscape->key                      ) INTO TABLE lt_modification.


    "-----------------------------------
    " Modify instances
    "-----------------------------------
    IF lt_modification IS NOT INITIAL.
      io_modify->do_modify( lt_modification ).

      io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                             IMPORTING eo_message             = DATA(lo_message)
                                       eo_change              = DATA(lo_change) ).
    ENDIF.



  ENDMETHOD.


  METHOD is_phase_assign_allowed.

    " Whenever one of the rules fail, the rule processing ends and it_key is returned as et_failed_key
    " This method is called for one single node.


    " **************************************************************************************************************************************************
    " General Procedue
    " --------------------------------------------------------------------------------------------------------------------------------------------------
    " The following rules only apply for the manual assignment of phases. Automatic assignment is still possible and will be handled by the BOPF Model
    "
    " 1. Differentiate on node-type. Some nodes ALWAYS allow phase assignment.
    "                             Other nodes NEVER allow manual phase assignment or don't have a phase assignment.
    " 2. UNDER STANDBY:         - Nodes under the standby nodes (DB or App) cannot have a phase assigned
    " 3. PARENT_NODE:           - For all other nodes the parent phase needs to be checked. If the parent phase does not have a phase assigned,
    "                             the manual phase assignment for the current node should not be possible.
    " 4. SUCCESSOR/PREDECESSOR: - If there is a predecessor and it doesn't have a phase assigned, phase assignment is not possible for the current node.
    " 5. MANDATORY/DEFAULT:     - If the current node is mandatory (e.g. material) or default (e.g. db server instance) the phase assignment
    "                             should not be possible.
    " **************************************************************************************************************************************************


    DATA: lt_root              TYPE /hec1/t_config_root_ct,
          lt_datacenter        TYPE /hec1/t_data_datacenter_ct,
          lt_connectivity      TYPE /hec1/t_data_connectivity_ct,
          lt_tier              TYPE /hec1/t_data_tier_ct,
          lt_sla               TYPE /hec1/t_data_tier_sla_ct,
          lt_material          TYPE /hec1/t_data_material_ct,
          lt_software_item     TYPE /hec1/t_data_sw_item_ct,
          lt_db_si             TYPE /hec1/t_data_db_server_inst_ct,
          lt_db_node           TYPE /hec1/t_data_db_node_ct,
          lt_db_serv_pc        TYPE /hec1/t_data_db_serv_pc_ct,
          lt_db_storage_qty    TYPE /hec1/t_data_db_storage_qty_ct,
          lt_db_backup         TYPE /hec1/t_data_db_backup_ct,
          lt_app_si            TYPE /hec1/t_data_app_serv_inst_ct,
          lt_app_node          TYPE /hec1/t_data_app_node_ct,
          lt_app_serv_pc       TYPE /hec1/t_data_app_serv_pc_ct,
          lt_app_storage_qty   TYPE /hec1/t_data_app_storageqty_ct,
          lt_app_backup        TYPE /hec1/t_data_app_backup_ct,

          lo_result_descriptor TYPE REF TO cl_abap_tabledescr,
          lr_data              TYPE REF TO data,
          lr_data_parent       TYPE REF TO data,
          lr_data_predecessor  TYPE REF TO data,
          r_descr              TYPE REF TO cl_abap_structdescr.

    FIELD-SYMBOLS: <fs_data>             TYPE STANDARD TABLE,
                   <fs_data_parent>      TYPE STANDARD TABLE,
                   <fs_data_predecessor> TYPE STANDARD TABLE,
                   <fs_param>            TYPE /bobf/s_frw_node.

    CLEAR et_failed_key.

    ASSIGN is_parameters->* TO <fs_param>.

    CHECK <fs_param> IS ASSIGNED. "the parameter contains the node and key for the object that should be checked.

    CHECK lines( it_key ) = 1. " this method only works for single nodes. Multiple nodes are not supported

    CASE <fs_param>-node.

        " **********************
        " 1a. never allowed
        " **********************
      WHEN /hec1/if_configuration_c=>sc_node-instance_db
        OR /hec1/if_configuration_c=>sc_node-db_server
        OR /hec1/if_configuration_c=>sc_node-db_storage
        OR /hec1/if_configuration_c=>sc_node-app_server
        OR /hec1/if_configuration_c=>sc_node-app_storage.

        et_failed_key = it_key.
        RETURN. ">>>>>>>

        " **********************
        " 1b. always allowed
        " **********************
      WHEN /hec1/if_configuration_c=>sc_node-add_service_class
        OR /hec1/if_configuration_c=>sc_node-add_service_datacenter
        OR /hec1/if_configuration_c=>sc_node-add_service
        OR /hec1/if_configuration_c=>sc_node-lt_backup_class
        OR /hec1/if_configuration_c=>sc_node-lt_backup_datacenter
        OR /hec1/if_configuration_c=>sc_node-lt_backup_amount
        OR /hec1/if_configuration_c=>sc_node-add_storage_amount
        OR /hec1/if_configuration_c=>sc_node-add_storage_class
        OR /hec1/if_configuration_c=>sc_node-add_storage_datacenter
        OR /hec1/if_configuration_c=>sc_node-tier.
*        " For tier, the related tier needs to have the same phase

        CLEAR et_failed_key.
        RETURN. ">>>>>>

        " **********************
        " 1c. sometimes allowed
        " **********************
      WHEN /hec1/if_configuration_c=>sc_node-datacenter.

        io_read->retrieve( EXPORTING iv_node = <fs_param>-node
                                     it_key  = VALUE #( ( key = <fs_param>-key ) )
                           IMPORTING et_data = lt_datacenter ).

        TRY.
            DATA(ls_datacenter) = lt_datacenter[ 1 ].

            " The first Datacenter will always have the default phase.
            IF ls_datacenter-hec_datacenter_is_first = abap_true.
              et_failed_key = it_key.
            ELSE.
              CLEAR et_failed_key.
            ENDIF.
            RETURN. ">>>>>>>

          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        " **********************
        " others (specific rules)
        " **********************
      WHEN OTHERS.
        "Default behavior is that phase assignment is allowed (no need for case-others)

        " ************************
        " get node dynamically
        " ************************
        " get nodes dynamically
        TRY.
            DATA(lo_bopf_config) = /bobf/cl_frw_factory=>get_configuration( /hec1/if_configuration_c=>sc_bo_key ).
          CATCH /bobf/cx_frw.
        ENDTRY.

        lo_bopf_config->get_node( EXPORTING iv_node_key = <fs_param>-node
                                  IMPORTING es_node     = DATA(ls_node_config) ).

        " Get current node details
        lo_result_descriptor ?= cl_abap_tabledescr=>describe_by_name( ls_node_config-data_table_type ).
        CREATE DATA lr_data TYPE HANDLE lo_result_descriptor.
        ASSIGN lr_data->* TO <fs_data>.

        io_read->retrieve( EXPORTING iv_node = <fs_param>-node
                                     it_key  = VALUE #( ( key = <fs_param>-key ) )
                           IMPORTING et_data = <fs_data> ).

        " check that the current object has a phase field. otherwise we can skip the entire logic
        ASSIGN <fs_data>[ 1 ] TO FIELD-SYMBOL(<fs_data_line>).
        CHECK <fs_data_line> IS ASSIGNED.
        ASSIGN COMPONENT 'HEC_PHASE_GUID' OF STRUCTURE <fs_data_line> TO FIELD-SYMBOL(<fs_phase_guid>).

        IF <fs_phase_guid> IS NOT ASSIGNED.
          " If the current node does not have the field HEC_PHASE_GUID, a phase assignment is never possible
          et_failed_key = it_key.
          RETURN. ">>>>>>>>
        ENDIF.

        " ************************
        " 2. Under Standby node?
        " ************************
        "    objects under the standyb node cannot get a phase manually assigned
        ASSIGN COMPONENT 'HEC_DB_CLUST_NODE_TYPE_VALUE' OF STRUCTURE <fs_data_line> TO FIELD-SYMBOL(<fs_db_clust_node_type_value>).
        ASSIGN COMPONENT 'HEC_APP_CLUST_NODE_TYPE_VALUE' OF STRUCTURE <fs_data_line> TO FIELD-SYMBOL(<fs_app_clust_node_type_value>).

        IF <fs_db_clust_node_type_value> IS ASSIGNED.
          IF <fs_db_clust_node_type_value> = /hec1/if_config_constants=>gc_db_clust_node_type-standby.
            et_failed_key = it_key.
            RETURN. ">>>>>>
          ENDIF.
        ELSEIF <fs_app_clust_node_type_value> IS ASSIGNED.
          IF <fs_app_clust_node_type_value> = /hec1/if_config_constants=>gc_app_clust_node_type-standby.
            et_failed_key = it_key.
            RETURN. ">>>>>>
          ENDIF.
        ENDIF. "fields found?

        " ************************
        " 3. Check, if parent has a phase assigned.
        " ************************
        " Read node type dynamically
        "  This is needed to then
        "  read the parent nodes
        r_descr ?= cl_abap_typedescr=>describe_by_data( /hec1/if_configuration_c=>sc_node ).
        LOOP AT r_descr->components ASSIGNING FIELD-SYMBOL(<fs_field>).
          ASSIGN COMPONENT <fs_field>-name OF STRUCTURE /hec1/if_configuration_c=>sc_node TO FIELD-SYMBOL(<fs_fieldvalue>).
          IF <fs_fieldvalue> IS ASSIGNED.
            IF <fs_fieldvalue> = <fs_param>-node.
              EXIT. ">>>>>
            ENDIF. "<fs_fieldvalue> = <fs_param>-node
          ENDIF. "<fs_fieldvalue> is assigned
        ENDLOOP.

        " get node association structure
        ASSIGN COMPONENT <fs_field>-name OF STRUCTURE /hec1/if_configuration_c=>sc_association
         TO FIELD-SYMBOL(<fs_association_struct>).

        CHECK <fs_association_struct> IS ASSIGNED.

        " get node-to_parent structure
        ASSIGN COMPONENT 'TO_PARENT' OF STRUCTURE <fs_association_struct>
         TO FIELD-SYMBOL(<fs_association_to_parent>).

        CHECK <fs_association_to_parent> IS ASSIGNED.

        " Get parent node
        lo_bopf_config->get_node( EXPORTING iv_node_key = ls_node_config-parent_node_key
                                  IMPORTING es_node     = DATA(ls_parent_node_config) ).

        lo_result_descriptor ?= cl_abap_tabledescr=>describe_by_name( ls_parent_node_config-data_table_type ).
        CREATE DATA lr_data_parent TYPE HANDLE lo_result_descriptor.
        ASSIGN lr_data_parent->* TO <fs_data_parent>.

        " BOPF Call
        io_read->retrieve_by_association( EXPORTING iv_node        = ls_node_config-node_key
                                                    it_key         = VALUE #( ( key = <fs_param>-key ) )
                                                    iv_fill_data   = abap_true
                                                    iv_association = <fs_association_to_parent> "e.g. /hec1/if_configuration_c=>sc_association-tier-to_parent
                                          IMPORTING et_data        = <fs_data_parent> ).

        ASSIGN <fs_data_parent>[ 1 ] TO FIELD-SYMBOL(<fs_data_parent_line>).
        CHECK <fs_data_parent_line> IS ASSIGNED.
        ASSIGN COMPONENT 'HEC_PHASE_GUID' OF STRUCTURE <fs_data_parent_line> TO FIELD-SYMBOL(<fs_parent_node_phase>).

        " Check the parent nodes phase assignment
        IF <fs_parent_node_phase> IS ASSIGNED.
          IF <fs_parent_node_phase> IS INITIAL.
            " phase assignment not allowed
            et_failed_key = it_key.
            RETURN. ">>>>>>
          ENDIF.
        ENDIF. "<fs_parent_node_phase> is assigned

        " *****************************
        " 4. Successor/Predecessor
        " *****************************
        " All Successor/Predecessor Objects have the group SUCC_PRED with the same fields
        ASSIGN COMPONENT 'HEC_SUCCESSOR_GUID' OF STRUCTURE <fs_data_line> TO FIELD-SYMBOL(<fs_successor_guid>).
        ASSIGN COMPONENT 'HEC_PREDECESSOR_GUID' OF STRUCTURE <fs_data_line> TO FIELD-SYMBOL(<fs_predecessor_guid>).

        IF <fs_successor_guid> IS ASSIGNED     AND
           <fs_predecessor_guid> IS ASSIGNED.

          IF <fs_successor_guid> IS INITIAL    AND
             <fs_predecessor_guid> IS INITIAL.
            " if there are no successors or predecessors this node is the only node on that level.
            " This means that the phase is inherited from the parent and cannot be changed
            et_failed_key = it_key.
            RETURN. ">>>>>>

          ELSEIF <fs_predecessor_guid> IS NOT INITIAL.
            " if a predecessor exists, the predecessor node needs to be read.
            " If the predecessor has a phase assigned, phase assignment should be possible for the current node

            lo_result_descriptor ?= cl_abap_tabledescr=>describe_by_name( ls_node_config-data_table_type ).
            CREATE DATA lr_data_predecessor TYPE HANDLE lo_result_descriptor.
            ASSIGN lr_data_predecessor->* TO <fs_data_predecessor>.

            " BOPF Call
            io_read->retrieve( EXPORTING iv_node = <fs_param>-node
                                         it_key  = VALUE #( ( key = <fs_predecessor_guid> ) )
                               IMPORTING et_data = <fs_data_predecessor> ).

            ASSIGN <fs_data_predecessor>[ 1 ] TO FIELD-SYMBOL(<fs_data_predecessor_line>).
            CHECK <fs_data_predecessor_line> IS ASSIGNED.
            ASSIGN COMPONENT 'HEC_PHASE_GUID' OF STRUCTURE <fs_data_predecessor_line> TO FIELD-SYMBOL(<fs_predecessor_node_phase>).

            IF <fs_predecessor_node_phase> IS ASSIGNED.
              IF <fs_predecessor_node_phase> IS INITIAL.
                " if the predecessor does not have a phase yet, the current node cannot get a phase assigned
                et_failed_key = it_key.
                RETURN. ">>>>>
              ENDIF.
            ENDIF. "if <fs_predecessor_node_phase> is assigned.

          ELSE.
            " If there is only a successor, then the current node should allow phase assignment
            " et_failed_key will stay empty
          ENDIF.
        ENDIF. "<fs_successor_guid> is assigned and <fs_predecessor_guid> is assigned.

        " *****************************
        " 5. Mandatory/Default?
        " *****************************
        " 2a. in some cases the objects are mandatory or default. This means the phase is inherited from the parent and cannot be changed
        CASE <fs_param>-node.
            " Material and Software Item
          WHEN /hec1/if_configuration_c=>sc_node-material
            OR /hec1/if_configuration_c=>sc_node-software_item.
            ASSIGN COMPONENT /hec1/if_configuration_c=>sc_node_attribute-material-hec_material_rel_value OF STRUCTURE <fs_data_line> TO FIELD-SYMBOL(<fs_material_rel_value>).

            " DB Server Instance
          WHEN /hec1/if_configuration_c=>sc_node-db_server_instance.
            ASSIGN COMPONENT /hec1/if_configuration_c=>sc_node_attribute-db_server_instance-hec_default_db_server_inst OF STRUCTURE <fs_data_line> TO FIELD-SYMBOL(<fs_is_default>).

            " DB Node
          WHEN /hec1/if_configuration_c=>sc_node-db_node.
            ASSIGN COMPONENT /hec1/if_configuration_c=>sc_node_attribute-db_node-hec_db_clust_node_type_value OF STRUCTURE <fs_data_line> TO FIELD-SYMBOL(<fs_is_master>).

            " App Server Instance
          WHEN /hec1/if_configuration_c=>sc_node-app_server_instance.
            ASSIGN COMPONENT /hec1/if_configuration_c=>sc_node_attribute-app_server_instance-hec_default_app_server_inst OF STRUCTURE <fs_data_line> TO <fs_is_default>.

            " App Node
          WHEN /hec1/if_configuration_c=>sc_node-app_node.
            ASSIGN COMPONENT /hec1/if_configuration_c=>sc_node_attribute-app_node-hec_app_clust_node_type_value OF STRUCTURE <fs_data_line> TO <fs_is_master>.

        ENDCASE.

        IF <fs_material_rel_value> IS ASSIGNED.
          IF <fs_material_rel_value> = /hec1/if_config_constants=>gc_material_rel-mandatory.
            et_failed_key = it_key.
            RETURN. ">>>>>>
          ENDIF.
        ENDIF.

        IF <fs_is_default> IS ASSIGNED.
          IF <fs_is_default> = abap_true.
            et_failed_key = it_key.
          ENDIF.
        ENDIF.

        IF <fs_is_master> IS ASSIGNED.
          IF <fs_is_master> = /hec1/if_config_constants=>gc_db_clust_node_type-master.
            et_failed_key = it_key.
          ENDIF.
        ENDIF.

    ENDCASE. "<fs_param>-node.

  ENDMETHOD.


  METHOD check_apm_validity.
    "Get ROOT Node data
    DATA(ls_root) = /hec1/cl_config_helper=>get_root_node( iv_node_key = is_ctx-node_key
                                                           it_key      = it_key
                                                           io_read     = io_read
                                                           io_modify   = io_modify ).

    DATA lt_apm_validity TYPE /hec1/t_apm_validity.

    "Get APM Validity
    /hec1/cl_config_helper=>check_apm_validity_by_grace_p( EXPORTING is_root = ls_root CHANGING ct_apm_validity = lt_apm_validity ).

    DATA(ls_apm_validity) = VALUE #( lt_apm_validity[ 1 ] OPTIONAL ).

    CASE ls_apm_validity-validity_level.
      WHEN /hec1/if_config_constants=>gc_msg_severity-error.
        et_failed_key = it_key.
        /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = VALUE #( msgid = /hec1/if_config_constants=>gc_msg_classname-config msgno = '028' )
                                                       iv_severity = /hec1/if_config_constants=>gc_msg_severity-error
                                             CHANGING  co_message  = eo_message ).

      WHEN /hec1/if_config_constants=>gc_msg_severity-warning.
        et_failed_key = it_key.
        /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = VALUE #( msgid = /hec1/if_config_constants=>gc_msg_classname-config msgno = '029' attr1 = ls_apm_validity-days_remaining )
                                                       iv_severity = /hec1/if_config_constants=>gc_msg_severity-warning
                                             CHANGING  co_message  = eo_message ).
      WHEN /hec1/if_config_constants=>gc_msg_severity-success.
        et_failed_key = it_key.
        /hec1/cl_config_helper=>set_message( EXPORTING iv_textid   = VALUE #( msgid = /hec1/if_config_constants=>gc_msg_classname-config msgno = '030' attr1 = ls_apm_validity-days_remaining )
                                                       iv_severity = /hec1/if_config_constants=>gc_msg_severity-success
                                             CHANGING  co_message  = eo_message ).
    ENDCASE.



  ENDMETHOD.


  METHOD reset_add_service.

    DATA: lt_add_service      TYPE /hec1/t_data_add_services_ct,
          lt_root             TYPE /hec1/t_config_root_ct,
          lt_datacenter       TYPE /hec1/t_data_datacenter_ct,
          lt_solution         TYPE /hec1/t_data_solution_ct,
          lt_tier             TYPE /hec1/t_data_tier_ct,
          lt_tier_add_service TYPE /hec1/t_data_tier_add_serv_ct,
          ls_parameter        TYPE /hec1/s_act_import_parameter,
          lt_modification     TYPE /bobf/t_frw_modification,
          lt_act_update       TYPE /hec1/t_act_update_t_add_serv.

    CLEAR: eo_message,
           et_failed_key.

    ASSIGN is_parameters->* TO FIELD-SYMBOL(<fs_parameters>).
    IF <fs_parameters> IS ASSIGNED.
      ls_parameter = <fs_parameters>.        "#EC CI_FLDEXT_OK[2215424]
    ENDIF.

    " Get Landscape
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_association = /hec1/if_configuration_c=>sc_association-add_service-to_root
                                                iv_fill_data   = abap_true
                                      IMPORTING et_data        = lt_root
                                                et_target_key  = DATA(lt_root_key) ).

    DATA(ls_root) = VALUE #( lt_root[ 1 ] OPTIONAL ).

    " get solution to retrieve cluster type
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-root
                                                it_key         = lt_root_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-solution
                                      IMPORTING et_target_key  = DATA(lt_solution_key) ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-solution
                                                it_key         = lt_solution_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                      IMPORTING et_target_key  = DATA(lt_tier_key) ).

    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                it_key         = lt_tier_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier-tier_add_service
                                      IMPORTING et_data        = lt_tier_add_service ).

    " Get Additional Service
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_add_service ).

    TRY.
        DATA(ls_add_service) = lt_add_service[ 1 ].
      CATCH cx_sy_itab_line_not_found.
        RETURN. ">>>>
    ENDTRY.

    CASE is_ctx-act_key.
        " **********************************
        " Reset Additional Service Class
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_action-add_service-reset_service_class.

        CLEAR: ls_add_service-hec_as_class_guid,
               ls_add_service-hec_as_class_descr,
               ls_add_service-hec_as_class_value,
               ls_add_service-hec_as_class_vlqt,
               ls_add_service-hec_as_class_descr_ext,
               ls_add_service-hec_ip_as_class_descr,
               ls_add_service-hec_ip_as_class_guid,
               ls_add_service-hec_ip_as_class_vlqt,

               ls_add_service-price.

        INSERT VALUE #( data        = REF #( ls_add_service )
                        node        = is_ctx-node_key
                        change_mode = /bobf/if_frw_c=>sc_modify_update
                        key         = ls_add_service-key
                        ) INTO TABLE lt_modification.

        " **********************************
        " Modify Datacenter Assignment
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_action-add_service-modify_datac_assignment.

        LOOP AT ls_parameter-name_value ASSIGNING FIELD-SYMBOL(<fs_name_value>).

          ASSIGN COMPONENT <fs_name_value>-fieldname OF STRUCTURE ls_add_service TO FIELD-SYMBOL(<fs_field>).
          IF <fs_field> IS ASSIGNED.
            IF <fs_field> <> <fs_name_value>-value.
              <fs_field> = <fs_name_value>-value.

              DATA(lv_changed) = abap_true.
            ENDIF.
          ENDIF.

        ENDLOOP.

        " TODO check for fitting service in the new datacenter

        IF lv_changed = abap_true.
          INSERT VALUE #( data        = REF #( ls_add_service )
                          node        = is_ctx-node_key
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = ls_add_service-key
                          ) INTO TABLE lt_modification.
        ENDIF.

        " **********************************
        " Modify Additional Service
        " **********************************
      WHEN /hec1/if_configuration_c=>sc_action-add_service-modify_service.

        LOOP AT ls_parameter-name_value ASSIGNING <fs_name_value>.

          ASSIGN COMPONENT <fs_name_value>-fieldname OF STRUCTURE ls_add_service TO <fs_field>.
          IF <fs_field> IS ASSIGNED.
            IF <fs_field> <> <fs_name_value>-value.
              <fs_field> = <fs_name_value>-value.

              lv_changed = abap_true.
            ENDIF.
          ENDIF.

        ENDLOOP.

        " Adjust Tier Assignment
        LOOP AT lt_tier_add_service ASSIGNING FIELD-SYMBOL(<fs_tier_add_service>)
          WHERE hec_tas_service_ref_guid = ls_add_service-hec_node_service.

          APPEND VALUE #( key               = <fs_tier_add_service>-key
                          parent_key        = <fs_tier_add_service>-parent_key
                          do_update_service = abap_true ) TO lt_act_update.

        ENDLOOP.

        INSERT VALUE #( data        = REF #( ls_add_service )
                        node        = is_ctx-node_key
                        change_mode = /bobf/if_frw_c=>sc_modify_update
                        key         = ls_add_service-key
                        ) INTO TABLE lt_modification.

    ENDCASE.

    "-----------------------------------
    " Set create DB/App server instance
    " action to general
    "-----------------------------------
    IF lt_act_update IS NOT INITIAL.
      CLEAR me->mr_act_param.
      me->mr_act_param = NEW /hec1/t_act_update_t_add_serv( lt_act_update ).

      /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys(
          is_ctx          = VALUE #( BASE CORRESPONDING #( is_ctx )
                                          node_key = /hec1/if_configuration_c=>sc_node-tier_add_service )
          it_key          = VALUE #( FOR line IN lt_act_update
                                     ( key = line-key ) )
          iv_action       = /hec1/cl_config_det_general=>/hec1/if_config_det_general~get_act_key( /hec1/if_config_constant=>gc_act_method-update_tier_add_service )
          iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation
          ir_act_param    = me->mr_act_param ).

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


  METHOD apm_change_cr.
    DATA lt_bo_nodes TYPE /bobf/t_frw_node.

    "disable determinations on create
    /hec1/cl_lib_d_superclass=>set_switch( abap_false ).
    /hec1/cl_lib_d_superclass=>set_tree_switch( abap_false ).

    DATA(lo_copy_controller_apm) = NEW /hec1/cl_copy_controller_apmcr(
      iv_bo_key   = is_ctx-bo_key
      io_read     = io_read
      io_modify   = io_modify
      it_key      = it_key
      iv_node_key = is_ctx-node_key
    ).

    lt_bo_nodes = lo_copy_controller_apm->copy( ).

    io_modify->end_modify( EXPORTING iv_process_immediately = abap_true IMPORTING eo_change = DATA(lo_change) ).

    "enable determinations on create
    /hec1/cl_lib_d_superclass=>set_switch( abap_true ).
    /hec1/cl_lib_d_superclass=>set_tree_switch( abap_true ).


    DATA(ls_apm_config_data) = VALUE /hec1/s_apm_config_data( hec_confid          = is_parameters-hec_confid
                                                              hec_conf_version    = is_parameters-hec_conf_version
                                                              hec_target_apm_guid = is_parameters-hec_target_apm_guid
                                                              hec_target_apm_descr = is_parameters-hec_target_apm_descr
                                                              hec_contract_status = is_parameters-hec_contract_status
                                                              bopf_read_object    = io_read
                                                              bopf_modify_object  = io_modify ).

    DATA(lo_apm_controller) = /hec1/cl_apm_controller_cr=>get_instance( ).
    lo_apm_controller->set_apm_config_data( ls_apm_config_data ).

    "all nodes of the new copied version, received from copy controller
    lo_apm_controller->apm_change( it_bo_nodes = lt_bo_nodes ).

    io_modify->end_modify( EXPORTING iv_process_immediately = abap_true IMPORTING eo_change = lo_change ).

    IF ( et_data IS SUPPLIED ).
      et_data = CORRESPONDING #( lt_bo_nodes ).
    ENDIF.
  ENDMETHOD.


  METHOD create_dr_tier.
    DATA: lt_tier         TYPE /hec1/t_data_tier_ct,
          lt_tier_related TYPE /hec1/t_data_tier_ct,
          lt_modification TYPE /bobf/t_frw_modification.

    " Get landscape data
    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING ev_root_key      = DATA(lv_root_key)
                                                        er_landscape     = DATA(lr_landscape)
                                                        er_delivery_unit = DATA(lr_dlvy_unit)
                                                        et_datacenter    = DATA(lt_datacenter) ).

    " Get complete configured DR data center
    DATA(lt_dr_datacenter) = VALUE wdr_context_attr_value_list( FOR ls_datac IN lt_datacenter
                                                                WHERE ( hec_datacenter_type_value = /hec1/if_config_constants=>gc_datacenter_type_dr AND
                                                                        hec_datacenter_guid IS NOT INITIAL                                               )
                                                               ( value = ls_datac-hec_node_datacenter
                                                                 text  = ls_datac-hec_datacenter_descr )                                                    ).

    " Get source tier(always primary tier)
    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_tier ).


    " Check if primary tier has related tier, so this related tier
    " has also to be created as DR tier
    IF line_exists( lt_tier[ hec_related_stack = abap_true ] ).
      " Get related tier
      io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-solution
                                                  it_key         = VALUE #( ( key = lt_tier[ 1 ]-parent_key ) )
                                                  iv_association = /hec1/if_configuration_c=>sc_association-solution-tier
                                                  iv_fill_data   = abap_true
                                        IMPORTING et_data        = lt_tier_related ).


      LOOP AT lt_tier_related ASSIGNING FIELD-SYMBOL(<fs_tier_related>).
        ASSIGN lt_tier[ hec_related_stack_guid = <fs_tier_related>-hec_related_stack_guid
                        hec_tier_cat_value     = <fs_tier_related>-hec_tier_cat_value     ] TO FIELD-SYMBOL(<fs_tier>).

        IF <fs_tier> IS ASSIGNED.
          IF <fs_tier>-key <> <fs_tier_related>-key.
            APPEND <fs_tier_related> TO lt_tier.
            " Generate tier stack relation GUID
            DATA(lv_relation_guid) = /rbp/cl_general_utilities=>get_new_guid22( ) .
            EXIT. " >>>>>>>
          ENDIF.
        ENDIF.
      ENDLOOP.
    ENDIF.

    SORT lt_tier
      BY hec_sol_tier_stack_value DESCENDING.


    LOOP AT lt_tier ASSIGNING <fs_tier>.

      " Get effort building block GUID
      SELECT SINGLE hec_timebased_effort_bb_guid
        FROM /hec1/i_tiertbbbbasic
       WHERE hec_apm_guid         = @lr_landscape->hec_apm_guid         AND
             hec_solution_guid    = @<fs_tier>-hec_solution_guid        AND
             hec_tier_stack_value = @<fs_tier>-hec_sol_tier_stack_value AND
             hec_tier_cat_value   = @<fs_tier>-hec_tier_cat_value
        INTO @DATA(lv_effort_bb_guid).


      DATA(lr_tier) = NEW /hec1/s_data_tier_cs( BASE CORRESPONDING #( <fs_tier> EXCEPT key                        hec_aggr_comp_price_save
                                                                                       hec_node_tier              hec_aggr_comp_price_new
                                                                                       hec_phase_guid             hec_exchange_rate
                                                                                       hec_phase_fixed            hec_exchange_currency
                                                                                       hec_phase_changed          hec_apm_fx_rate_date
                                                                                       hec_phase_start_date       hec_exchange_value
                                                                                       hec_phase_end_date         hec_comp_mod_type
                                                                                       hec_phase_description      hec_comp_cr_active
                                                                                       hec_apm_guid               hec_comp_cr_counter
                                                                                       hec_apm_descr              hec_instance_status
                                                                                       hec_related_stack_guid     hec_contract_status
                                                                                       crea_date_time             hec_price_aggre_status
                                                                                       crea_uname                 hec_provisioning_status
                                                                                       lchg_date_time             hec_cdd_status
                                                                                       lchg_uname                 hec_s2d_status
                                                                                       hec_tier_datacenter_guid   hec_fulfillment_status
                                                                                       hec_app_srv_qty_opt        hec_is_baseline
                                                                                       hec_db_srv_qty_opt         hec_is_baseline_active
                                                                                                                  hec_node_mark_as_del
                                                                                                                  price                   )
                                                 key                          = /bopf/cl_frw_factory=>get_new_key( )
                                                 hec_node_tier                = /rbp/cl_general_utilities=>get_new_guid22( )
                                                 hec_apm_guid                 = lr_landscape->hec_apm_guid
                                                 hec_apm_descr                = lr_landscape->hec_apm_descr
                                                 hec_tier_is_dr_node          = abap_true
                                                 hec_dr_oper_mode_value       = '02'
                                                 hec_dr_oper_mode_descr       = 'STD'
                                                 hec_dr_tier_primary_rel_guid = <fs_tier>-hec_node_tier
                                                 hec_related_stack_guid       = lv_relation_guid
                                                 hec_tier_datacenter_guid     = COND #( WHEN lines( lt_dr_datacenter ) = 1
                                                                                        THEN lt_dr_datacenter[ 1 ]-value   )
                                                 hec_instance_status          = /hec1/if_config_constants=>gc_instance_status-incomplete
                                                 crea_uname                   = sy-uname
                                                 price                        = /hec1/cl_config_helper=>do_price_validation( iv_node_key          = is_ctx-node_key
                                                                                                                             it_key               = it_key
                                                                                                                             io_read              = io_read
                                                                                                                             iv_effort_bb_guid    = lv_effort_bb_guid
                                                                                                                             iv_tier_is_dr_node   = abap_true
                                                                                                                             iv_dr_operating_mode = '02'               ) ).


      GET TIME STAMP FIELD lr_tier->crea_date_time.

      INSERT VALUE #( data        = lr_tier
                      node        = /hec1/if_configuration_c=>sc_node-tier
                      source_node = /hec1/if_configuration_c=>sc_node-solution
                      association = /hec1/if_configuration_c=>sc_association-solution-tier
                      source_key  = <fs_tier>-parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = lr_tier->key                                           ) INTO TABLE lt_modification.


      CLEAR lr_tier.
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


  METHOD copy_to_new_config.
    FIELD-SYMBOLS <ls_parameters> TYPE /hec1/s_act_import_parameter.
    DATA: lv_node_key TYPE /bobf/obm_node_key,
          lv_mode     TYPE /hec1/copy_mode VALUE 'NEW_VERS'.

    "disable determinations on create
    /hec1/cl_lib_d_superclass=>set_switch( abap_false ).

    /hec1/cl_lib_d_superclass=>set_tree_switch( abap_false ).

    TRY.

        ASSIGN is_parameters->* TO <ls_parameters>.
        IF sy-subrc <> 0.
          " Parameter structure could not be assigned for action copy
          RAISE EXCEPTION TYPE /hec1/cx_copy_control MESSAGE ID '/HEC1/MSG_BOPF_COPY' NUMBER 001.
        ENDIF.

        TRY.
            lv_node_key = <ls_parameters>-name_value[ fieldname = /hec1/if_config_constants=>gc_fieldname-node_key ]-value.
            DATA(lv_bp) = <ls_parameters>-name_value[ fieldname = /hec1/if_config_constants=>gc_fieldname-business_partner ]-value.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        DATA(lt_data) = NEW /hec1/cl_copy_controller_new(
                  iv_bo_key         = is_ctx-bo_key
                  io_read           = io_read
                  io_modify         = io_modify
                  iv_node_key       = lv_node_key
                  it_key            = VALUE #( ( key = <ls_parameters>-key ) )
                  iv_mode           = lv_mode
                  iv_bp             = lv_bp
                )->copy( ).

        io_modify->end_modify( EXPORTING iv_process_immediately = abap_true IMPORTING eo_change = DATA(lo_change) ).


        IF et_data IS SUPPLIED.
          et_data = CORRESPONDING #( lt_data ).
        ENDIF.

      CATCH cx_root INTO DATA(lo_ex).
        "in case of error =>
        /hec1/cl_lib_d_superclass=>set_switch( abap_true ).
        /hec1/cl_lib_d_superclass=>set_tree_switch( abap_true ).
        ev_static_action_failed = abap_true.
        eo_message->add_exception( lo_ex ).
    ENDTRY.

    "enable determinations on create
    /hec1/cl_lib_d_superclass=>set_switch( abap_true ).
    /hec1/cl_lib_d_superclass=>set_tree_switch( abap_true ).
  ENDMETHOD.


  METHOD create_dr_datacenter.

    " This method creates the DR Datacenter
    " it will be triggered by the datacenter
    " The parameters will contain the primary datacenter

    DATA: lt_datacenter   TYPE /hec1/t_data_datacenter_ct,
          lt_modification TYPE /bobf/t_frw_modification,
          ls_parameters   TYPE /hec1/s_act_import_parameter,
          lt_landscape    TYPE /hec1/t_config_root_ct.

    CLEAR: eo_message,
           et_failed_key.

    ASSIGN is_parameters->* TO FIELD-SYMBOL(<fs_parameters>).
    IF <fs_parameters> IS ASSIGNED.
      ls_parameters = <fs_parameters>.       "#EC CI_FLDEXT_OK[2215424]
    ENDIF.

    IF eo_message IS NOT BOUND.
      eo_message = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.

    io_read->get_root_key( EXPORTING iv_node       = is_ctx-node_key
                                     it_key        = it_key
                           IMPORTING et_target_key = DATA(lt_root_key) ).

    io_read->retrieve( EXPORTING iv_node = /hec1/if_configuration_c=>sc_node-root
                                 it_key  = lt_root_key
                       IMPORTING et_data = lt_landscape ).

    " there is only ever one landscape
    TRY.
        DATA(ls_landscape) = lt_landscape[ 1 ].
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = lt_datacenter ).

    TRY.
        DATA(lv_datacenter_selection) = ls_parameters-name_value[ fieldname = /hec1/if_configuration_c=>sc_node_attribute-datacenter-hec_datacenter_guid ]-value.
      CATCH cx_sy_itab_line_not_found.
        "TODO error message
    ENDTRY.

    SELECT *
      FROM /hec1/i_regdlvyinfrdatabasic       "#EC CI_ALL_FIELDS_NEEDED
      INTO TABLE @DATA(lt_fdt_datacenter)
     WHERE hec_datacenter_guid = @lv_datacenter_selection.

    LOOP AT lt_datacenter ASSIGNING FIELD-SYMBOL(<fs_datacenter>).

      TRY.
          DATA(lv_datacenter_guid) = ls_parameters-name_value[ fieldname = /hec1/if_configuration_c=>sc_node_attribute-datacenter-hec_datacenter_guid ]-value.
          DATA(lv_datac_relation_guid) = ls_parameters-name_value[ fieldname = /hec1/if_configuration_c=>sc_node_attribute-datacenter-hec_datac_dr_relation_guid ]-value.
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.

      DATA(lr_datacenter) = NEW /hec1/s_data_datacenter_cs( BASE CORRESPONDING #( <fs_datacenter> EXCEPT key
                                                                                                         hec_node_datacenter
                                                                                                         hec_sec_datacenter_guid
                                                                                                         hec_datacenter_guid
                                                                                                         hec_datacenter_type_descr
                                                                                                         hec_datacenter_type_value
                                                                                                         assignment )
                                                                 key                        = /bopf/cl_frw_factory=>get_new_key( )
                                                                 hec_node_datacenter        = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                 hec_apm_guid               = ls_landscape-hec_apm_guid
                                                                 hec_apm_descr              = ls_landscape-hec_apm_descr
                                                                 hec_datacenter_guid        = lv_datacenter_guid
                                                                 hec_phase_fixed            = abap_false
                                                                 hec_phase_assign_allowed   = abap_true
                                                                 hec_datacenter_is_first    = abap_false
                                                                 hec_datac_dr_relation_guid = lv_datac_relation_guid
                                                                 crea_uname                 = sy-uname ).

      " Get datacenter values
      lr_datacenter->* = CORRESPONDING #( BASE ( lr_datacenter->* ) VALUE #( lt_fdt_datacenter[ hec_datacenter_guid = lr_datacenter->hec_datacenter_guid ] OPTIONAL ) ).
      lr_datacenter->hec_datacenter_descr = |(DR) { lr_datacenter->hec_datacenter_descr }|.
      lr_datacenter->hec_tree_descr = lr_datacenter->hec_datacenter_descr. "#EC CI_FLDEXT_OK[2215424]

      GET TIME STAMP FIELD lr_datacenter->crea_date_time.

      " make sure that the datacenter type is set
      DATA(lt_datacenter_type) = /hec1/cl_apm_data_access_class=>/hec1/if_apm_data_access_class~get_datacenter_type(
        iv_apm_guid      = ls_landscape-hec_apm_guid
        iv_flat_mat_guid = ls_landscape-hec_flat_mat_guid
      ).

      TRY.
          DATA(ls_datacenter_type) = lt_datacenter_type[ value = /hec1/if_config_constants=>gc_datacenter_type_dr ].
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.

      lr_datacenter->hec_datacenter_type_value = ls_datacenter_type-value.
      lr_datacenter->hec_datacenter_type_descr = ls_datacenter_type-text.

      INSERT VALUE #( data        = lr_datacenter
                      node        = /hec1/if_configuration_c=>sc_node-datacenter
                      source_node = /hec1/if_configuration_c=>sc_node-delivery_unit
                      association = /hec1/if_configuration_c=>sc_association-delivery_unit-datacenter
                      source_key  = lr_datacenter->parent_key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = lr_datacenter->key
                      ) INTO TABLE lt_modification.

      "-----------------------------------
      " add infrastructure baseline
      "-----------------------------------
      DATA(lr_if_baseline) = NEW /hec1/s_data_if_baseline_cs( parent_key               = lr_datacenter->key
                                                              key                      = /bopf/cl_frw_factory=>get_new_key( )
                                                              hec_node_datacenter      = lr_datacenter->hec_node_datacenter
                                                              hec_node_if_baseline     = /rbp/cl_general_utilities=>get_new_guid22( )
                                                              hec_phase_guid           = lr_datacenter->hec_phase_guid
                                                              hec_phase_assign_allowed = abap_false
                                                              ).
      GET TIME STAMP FIELD lr_if_baseline->crea_date_time.

      INSERT VALUE #( data        = lr_if_baseline
                      node        = /hec1/if_configuration_c=>sc_node-infrastructure_baseline
                      source_node = /hec1/if_configuration_c=>sc_node-datacenter
                      association = /hec1/if_configuration_c=>sc_association-datacenter-infrastructure_baseline
                      source_key  = lr_datacenter->key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = lr_if_baseline->key
                      ) INTO TABLE lt_modification.

      "-----------------------------------
      " add network segment
      "-----------------------------------
      DATA(lr_network_segm) = NEW /hec1/s_data_network_segm_cs( parent_key               = lr_if_baseline->key
                                                                key                      = /bopf/cl_frw_factory=>get_new_key( )
                                                                hec_node_datacenter      = lr_datacenter->hec_node_datacenter
                                                                hec_node_if_baseline     = lr_if_baseline->hec_node_if_baseline
                                                                hec_node_network_segment = /rbp/cl_general_utilities=>get_new_guid22( )
                                                                ).

      GET TIME STAMP FIELD lr_network_segm->crea_date_time.

      INSERT VALUE #( data        = lr_network_segm
                      node        = /hec1/if_configuration_c=>sc_node-network_segment
                      source_node = /hec1/if_configuration_c=>sc_node-infrastructure_baseline
                      association = /hec1/if_configuration_c=>sc_association-infrastructure_baseline-network_segment
                      source_key  = lr_if_baseline->key
                      change_mode = /bobf/if_frw_c=>sc_modify_create
                      key         = lr_network_segm->key
                      ) INTO TABLE lt_modification.
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


  METHOD delete_node_cr.
    DATA: lo_config       TYPE REF TO /bobf/if_frw_configuration,
          lr_data         TYPE REF TO data,
          lr_data_struc   TYPE REF TO data,
          lv_node_key     TYPE /bobf/obm_node_key,
          lt_modification TYPE /bobf/t_frw_modification.


    FIELD-SYMBOLS: <fs_data>          TYPE STANDARD TABLE,
                   <fs_data_line>     TYPE any,
                   <fs_parameters>    TYPE /hec1/s_act_import_parameter,
                   <fs_config_status> TYPE /hec1/s_config_status,
                   <fs_config_cr>     TYPE /hec1/s_config_change_request.

    ASSIGN is_parameters->* TO <fs_parameters>.

    TRY.
        lv_node_key = <fs_parameters>-name_value[ fieldname = /hec1/if_config_constants=>gc_fieldname-node_key ]-value.
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

    TRY.
        "Get BO node configuration
        lo_config = /bobf/cl_frw_factory=>get_configuration( /hec1/if_configuration_c=>sc_bo_key ).
        lo_config->get_assoc_tab( IMPORTING et_assoc = DATA(lt_assocs) ).
        lo_config->get_node_tab( IMPORTING et_node = DATA(lt_nodes) ).

        "Get the structures of the BO Node
        DATA(ls_node) = lt_nodes[ node_key = lv_node_key ].
        DATA(lo_tabledescr) = CAST cl_abap_tabledescr( cl_abap_tabledescr=>describe_by_name( ls_node-data_table_type ) ).
        CREATE DATA lr_data TYPE HANDLE lo_tabledescr.

        "Read the node data
        ASSIGN lr_data->* TO <fs_data>.
        io_read->retrieve( EXPORTING iv_node       = lv_node_key
                                     it_key        = VALUE #( ( key = <fs_parameters>-key ) )
                                     iv_fill_data  = abap_true
                           IMPORTING et_data       = <fs_data>
                                     et_failed_key = DATA(lt_failed_key) ).
        CHECK lt_failed_key IS INITIAL.

        "/bobf/t_frw_modification only accepts structure, hence convert the table to structure
        DATA(lo_structdescr) = CAST cl_abap_structdescr( cl_abap_structdescr=>describe_by_name( ls_node-data_type ) ).
        CREATE DATA lr_data_struc TYPE HANDLE lo_structdescr.
        ASSIGN lr_data_struc->* TO <fs_data_line>.
        <fs_data_line> = <fs_data>[ 1 ].

        "Mark the node as deleted
        ASSIGN COMPONENT 'HEC_NODE_MARK_AS_DEL' OF STRUCTURE <fs_data_line> TO FIELD-SYMBOL(<fs_mark_as_del>).
        IF sy-subrc = 0.
          "Set mark as deleted
          <fs_mark_as_del> = abap_true.


          " Get ROOT node data from buffer
          DATA(ls_root) = /hec1/cl_config_helper=>get_root_node( EXPORTING iv_node_key = is_ctx-node_key
                                                                           it_key      = it_key
                                                                           io_read     = io_read
                                                                           io_modify   = io_modify    ).
          "Set CR Fields
          ASSIGN lr_data_struc->('CHANGE_REQUEST') TO <fs_config_cr>.
          IF ls_root IS NOT INITIAL AND sy-subrc = 0.
            " Copy CR related fields from the ROOT node
            <fs_config_cr>-hec_comp_cr_counter = ls_root-hec_cr_counter.
            <fs_config_cr>-hec_comp_mod_type = /hec1/if_config_constants=>gc_comp_mod_type-deleted.
          ENDIF.

          INSERT VALUE #( node        = lv_node_key
                          change_mode = /bobf/if_frw_c=>sc_modify_update
                          key         = <fs_parameters>-key
                          data        = lr_data_struc              ) INTO TABLE lt_modification.
        ENDIF.

        "Get all the child nodes and trigger this action DELETE_NODE_CR recursively
        LOOP AT lt_assocs ASSIGNING FIELD-SYMBOL(<ls_assoc>) WHERE assoc_type = 'A' AND assoc_cat = 'P' AND assoc_name = 'TO_PARENT' AND target_node_key = lv_node_key. "#EC CI_SORTSEQ
          IF line_exists( lt_nodes[ node_key = <ls_assoc>-source_node_key node_type = 'N' ] ).
            TRY.
                DATA(ls_assoc_to_child) = lt_assocs[ source_node_key = <ls_assoc>-target_node_key target_node_key = <ls_assoc>-source_node_key ]. "#EC CI_SORTSEQ

                io_read->retrieve_by_association(
                    EXPORTING
                      iv_node                 = ls_assoc_to_child-source_node_key
                      it_key                  = VALUE #( ( key = <fs_parameters>-key  ) )
                      iv_association          = ls_assoc_to_child-assoc_key
                     IMPORTING
                      eo_message              = DATA(lo_message)
                      et_target_key           = DATA(lt_children_keys)
                  ).

                LOOP AT lt_children_keys ASSIGNING FIELD-SYMBOL(<fs_children_key>).

                  /hec1/cl_config_det_general=>/hec1/if_config_det_general~set_act_node_keys_direct(
                   is_ctx          = CORRESPONDING #( is_ctx )
                   it_key          = VALUE #( ( key = <fs_parameters>-root_key ) )
                   iv_action       = /hec1/if_configuration_c=>sc_action-root-delete_node_cr
                   ir_act_param    =  NEW /hec1/s_act_import_parameter( key         = <fs_children_key>-key
                                                                        root_key    = <fs_parameters>-root_key
                                                                        name_value  = VALUE #( ( fieldname = /hec1/if_config_constants=>gc_fieldname-node_key
                                                                                                 value = ls_assoc_to_child-target_node_key ) ) )
                   iv_act_exectime = /bobf/if_conf_c=>sc_time_after_validation ).

                ENDLOOP.
              CATCH cx_sy_itab_line_not_found.
                CLEAR ls_assoc_to_child.
            ENDTRY.
          ENDIF.
        ENDLOOP.

        "-----------------------------------
        " Execute Modification ( = Delete)
        "-----------------------------------
        IF lt_modification IS NOT INITIAL.
          io_modify->do_modify( lt_modification ).
          io_modify->end_modify( EXPORTING iv_process_immediately = abap_true
                                 IMPORTING eo_message             = lo_message
                                           eo_change              = DATA(lo_change)  ).
        ENDIF.

        CLEAR:    <fs_parameters>,
                  lt_modification.
      CATCH /bobf/cx_frw INTO DATA(lo_ex).
    ENDTRY.
  ENDMETHOD.
ENDCLASS.