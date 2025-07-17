CLASS /hec1/cl_config_act_a_services DEFINITION
  PUBLIC
  INHERITING FROM /hec1/cl_lib_a_superclass
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.

    METHODS /bobf/if_frw_action~execute
        REDEFINITION .
  PROTECTED SECTION.
  PRIVATE SECTION.
    METHODS add_add_storage_amount
      IMPORTING
        is_ctx                  TYPE /bobf/s_frw_ctx_act
        it_key                  TYPE /bobf/t_frw_key
        io_read                 TYPE REF TO /bobf/if_frw_read
        io_modify               TYPE REF TO /bobf/if_frw_modify
        is_parameters           TYPE REF TO data
      EXPORTING
        eo_message              TYPE REF TO /bobf/if_frw_message
        et_failed_key           TYPE /bobf/t_frw_key
        ev_static_action_failed TYPE abap_bool
        et_data                 TYPE INDEX TABLE
        et_data_link            TYPE /bobf/t_frw_act_exp_data_link.
    METHODS add_add_storage_class
      IMPORTING
        is_ctx                  TYPE /bobf/s_frw_ctx_act
        it_key                  TYPE /bobf/t_frw_key
        io_read                 TYPE REF TO /bobf/if_frw_read
        io_modify               TYPE REF TO /bobf/if_frw_modify
        is_parameters           TYPE REF TO data
      EXPORTING
        eo_message              TYPE REF TO /bobf/if_frw_message
        et_failed_key           TYPE /bobf/t_frw_key
        ev_static_action_failed TYPE abap_bool
        et_data                 TYPE INDEX TABLE
        et_data_link            TYPE /bobf/t_frw_act_exp_data_link.
    METHODS add_add_storage_datacenter
      IMPORTING
        is_ctx                  TYPE /bobf/s_frw_ctx_act
        it_key                  TYPE /bobf/t_frw_key
        io_read                 TYPE REF TO /bobf/if_frw_read
        io_modify               TYPE REF TO /bobf/if_frw_modify
        is_parameters           TYPE REF TO data
      EXPORTING
        eo_message              TYPE REF TO /bobf/if_frw_message
        et_failed_key           TYPE /bobf/t_frw_key
        ev_static_action_failed TYPE abap_bool
        et_data                 TYPE INDEX TABLE
        et_data_link            TYPE /bobf/t_frw_act_exp_data_link.
    METHODS add_lt_backup_amount
      IMPORTING
        is_ctx                  TYPE /bobf/s_frw_ctx_act
        it_key                  TYPE /bobf/t_frw_key
        io_read                 TYPE REF TO /bobf/if_frw_read
        io_modify               TYPE REF TO /bobf/if_frw_modify
        is_parameters           TYPE REF TO data
      EXPORTING
        eo_message              TYPE REF TO /bobf/if_frw_message
        et_failed_key           TYPE /bobf/t_frw_key
        ev_static_action_failed TYPE abap_bool
        et_data                 TYPE INDEX TABLE
        et_data_link            TYPE /bobf/t_frw_act_exp_data_link.
    METHODS add_lt_backup_datacenter
      IMPORTING
        is_ctx                  TYPE /bobf/s_frw_ctx_act
        it_key                  TYPE /bobf/t_frw_key
        io_read                 TYPE REF TO /bobf/if_frw_read
        io_modify               TYPE REF TO /bobf/if_frw_modify
        is_parameters           TYPE REF TO data
      EXPORTING
        eo_message              TYPE REF TO /bobf/if_frw_message
        et_failed_key           TYPE /bobf/t_frw_key
        ev_static_action_failed TYPE abap_bool
        et_data                 TYPE INDEX TABLE
        et_data_link            TYPE /bobf/t_frw_act_exp_data_link.
    METHODS add_lt_backup_class
      IMPORTING
        is_ctx                  TYPE /bobf/s_frw_ctx_act
        it_key                  TYPE /bobf/t_frw_key
        io_read                 TYPE REF TO /bobf/if_frw_read
        io_modify               TYPE REF TO /bobf/if_frw_modify
        is_parameters           TYPE REF TO data
      EXPORTING
        eo_message              TYPE REF TO /bobf/if_frw_message
        et_failed_key           TYPE /bobf/t_frw_key
        ev_static_action_failed TYPE abap_bool
        et_data                 TYPE INDEX TABLE
        et_data_link            TYPE /bobf/t_frw_act_exp_data_link.


ENDCLASS.



CLASS /hec1/cl_config_act_a_services IMPLEMENTATION.


  METHOD /bobf/if_frw_action~execute.

    TRY.
        CASE is_ctx-act_key.

            " **********************************
            " Add LT_BACKUP_DATACENTER node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-create_lt_backup_dc.

            me->add_lt_backup_datacenter(
                EXPORTING is_ctx                  = is_ctx
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
            " Add LT_BACKUP_CLASS node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-lt_backup_datacenter-add_ltb_class.

            me->add_lt_backup_class(
                EXPORTING is_ctx                  = is_ctx
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
            " Add LT_BACKUP_AMOUNT node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-lt_backup_class-add_lt_backup_amount.
            me->add_lt_backup_amount(
                EXPORTING is_ctx                  = is_ctx
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
            " Add Add Storage Datacenter node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-root-create_add_storage_dc.
            me->add_add_storage_datacenter(
                EXPORTING is_ctx                  = is_ctx
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
            " Add Add Storage Class node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-add_storage_datacenter-add_astorage_class.
            me->add_add_storage_class(
                EXPORTING is_ctx                  = is_ctx
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
            " Add Add Storage Quota node
            " **********************************
          WHEN /hec1/if_configuration_c=>sc_action-add_storage_class-add_astorage_amount.
            me->add_add_storage_amount(
                EXPORTING is_ctx                  = is_ctx
                          it_key                  = it_key
                          io_read                 = io_read
                          io_modify               = io_modify
                          is_parameters           = is_parameters
                IMPORTING eo_message              = eo_message
                          et_failed_key           = et_failed_key
                          ev_static_action_failed = ev_static_action_failed
                          et_data                 = et_data
                          et_data_link            = et_data_link            ).
        ENDCASE.
      CATCH /bobf/cx_frw. " Exception class
    ENDTRY.

  ENDMETHOD.

  METHOD add_lt_backup_class.
    DATA:
      lt_modification          TYPE /bobf/t_frw_modification,
      lt_longterm_backup_dc    TYPE /hec1/t_data_lt_backup_dc_ct,
      lr_longterm_backup_class TYPE REF TO /hec1/s_data_lt_backup_cl_cs.

    io_read->retrieve(
      EXPORTING
        iv_node                 = is_ctx-node_key
        it_key                  = it_key
        iv_fill_data            = abap_true
      IMPORTING
        eo_message              = eo_message
        et_data                 = lt_longterm_backup_dc
    ).

    DATA(ls_longterm_backup_dc) = VALUE #( lt_longterm_backup_dc[ 1 ] OPTIONAL ).

    lr_longterm_backup_class = NEW /hec1/s_data_lt_backup_cl_cs( ).
    lr_longterm_backup_class->hec_node_lt_backup_dc    = ls_longterm_backup_dc-hec_node_lt_backup_dc.
    lr_longterm_backup_class->hec_node_lt_backup_class = /rbp/cl_general_utilities=>get_new_guid22( ).
    lr_longterm_backup_class->hec_apm_guid             = ls_longterm_backup_dc-hec_apm_guid.
    lr_longterm_backup_class->hec_apm_descr            = ls_longterm_backup_dc-hec_apm_descr.
    lr_longterm_backup_class->hec_ltb_datacenter_guid  = ls_longterm_backup_dc-hec_ltb_datacenter_guid.
    lr_longterm_backup_class->hec_ltb_datacenter_descr = ls_longterm_backup_dc-hec_ltb_datacenter_descr.
    lr_longterm_backup_class->hec_row_selectable       = abap_true.
    lr_longterm_backup_class->hec_delete_visible       = abap_true.
    GET TIME STAMP FIELD lr_longterm_backup_class->crea_date_time.

    TRY.
        io_modify->create(
          EXPORTING
            iv_node            = /hec1/if_configuration_c=>sc_node-lt_backup_class                              " Node to Create
            is_data            = lr_longterm_backup_class                                                       " Data
            iv_assoc_key       = /hec1/if_configuration_c=>sc_association-lt_backup_datacenter-lt_backup_class  " Association
            iv_source_node_key = is_ctx-node_key                                                                " Parent Node
            iv_source_key      = ls_longterm_backup_dc-key                                                      " NodeID of Parent Instance
            iv_root_key        = ls_longterm_backup_dc-root_key                                                 " Root NodeID
          IMPORTING
            ev_key             = DATA(new_instance_key)
        ).

        "-----------------------------------
        " Fill export parameter
        "-----------------------------------
        ASSIGN et_data TO FIELD-SYMBOL(<fs_export_parameters>).
        DATA(lt_export_parameters) = VALUE /bobf/t_frw_key_incl( ( key        = new_instance_key
                                                                   parent_key = ls_longterm_backup_dc-key
                                                                   root_key   = ls_longterm_backup_dc-root_key ) ).
        <fs_export_parameters> = lt_export_parameters.

      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

  ENDMETHOD.

  METHOD add_lt_backup_datacenter.
    DATA:
      lt_modification    TYPE /bobf/t_frw_modification,
      lr_longterm_backup TYPE REF TO /hec1/s_data_lt_backup_dc_cs.

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING er_landscape     = DATA(lr_landscape) ).

    lr_longterm_backup = NEW /hec1/s_data_lt_backup_dc_cs( ).
    lr_longterm_backup->hec_node_lt_backup_dc = /rbp/cl_general_utilities=>get_new_guid22( ).
    lr_longterm_backup->hec_apm_guid          = lr_landscape->hec_apm_guid.
    lr_longterm_backup->hec_apm_descr         = lr_landscape->hec_apm_descr.
    lr_longterm_backup->hec_row_selectable    = abap_true.
    lr_longterm_backup->hec_delete_visible    = abap_true.
    GET TIME STAMP FIELD lr_longterm_backup->crea_date_time.

    TRY.
        io_modify->create(
          EXPORTING
            iv_node            = /hec1/if_configuration_c=>sc_node-lt_backup_datacenter               " Node to Create
            is_data            = lr_longterm_backup                                                   " Data
            iv_assoc_key       = /hec1/if_configuration_c=>sc_association-root-lt_backup_datacenter   " Association
            iv_source_node_key = is_ctx-node_key                                                      " Parent Node
            iv_source_key      = it_key[ 1 ]-key                                                      " NodeID of Parent Instance
            iv_root_key        = it_key[ 1 ]-key                                                      " Root NodeID
          IMPORTING
            ev_key             = DATA(new_instance_key)
        ).

        "-----------------------------------
        " Fill export parameter
        "-----------------------------------
        ASSIGN et_data TO FIELD-SYMBOL(<fs_export_parameters>).
        DATA(lt_export_parameters) = VALUE /bobf/t_frw_key_incl( ( key        = new_instance_key
                                                                   parent_key = it_key[ 1 ]-key
                                                                   root_key   = it_key[ 1 ]-key ) ).
        <fs_export_parameters> = lt_export_parameters.

      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

  ENDMETHOD.


  METHOD add_lt_backup_amount.
    DATA:
      lt_modification           TYPE /bobf/t_frw_modification,
      lt_longterm_backup_class  TYPE /hec1/t_data_lt_backup_cl_ct,
      lr_longterm_backup_amount TYPE REF TO /hec1/s_lt_backup_amount_cs.

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING er_landscape     = DATA(lr_landscape) ).

    io_read->retrieve(
      EXPORTING
        iv_node                 = is_ctx-node_key
        it_key                  = it_key
        iv_fill_data            = abap_true
      IMPORTING
        eo_message              = eo_message
        et_data                 = lt_longterm_backup_class
    ).

    DATA(ls_longterm_backup_class) = VALUE #( lt_longterm_backup_class[ 1 ] OPTIONAL ).

    lr_longterm_backup_amount = NEW /hec1/s_lt_backup_amount_cs( ).
    lr_longterm_backup_amount->hec_node_lt_backup_dc    = ls_longterm_backup_class-hec_node_lt_backup_dc.
    lr_longterm_backup_amount->hec_node_lt_backup_class = ls_longterm_backup_class-hec_node_lt_backup_class.
    lr_longterm_backup_amount->hec_node_lt_backup_amount =  /rbp/cl_general_utilities=>get_new_guid22( ).
    lr_longterm_backup_amount->hec_apm_guid             = ls_longterm_backup_class-hec_apm_guid.
    lr_longterm_backup_amount->hec_apm_descr            = ls_longterm_backup_class-hec_apm_descr.
    lr_longterm_backup_amount->hec_ltb_class_guid       = ls_longterm_backup_class-hec_ltb_class_guid.
    lr_longterm_backup_amount->hec_ltb_class_descr      = ls_longterm_backup_class-hec_ltb_class_descr.
    lr_longterm_backup_amount->hec_ltb_datacenter_guid  = ls_longterm_backup_class-hec_ltb_datacenter_guid.
    lr_longterm_backup_amount->hec_ltb_datacenter_descr = ls_longterm_backup_class-hec_ltb_datacenter_descr.
    lr_longterm_backup_amount->hec_row_selectable       = abap_true.
    lr_longterm_backup_amount->hec_delete_visible       = abap_true.
    GET TIME STAMP FIELD lr_longterm_backup_amount->crea_date_time.

    TRY.
        io_modify->create(
          EXPORTING
            iv_node            = /hec1/if_configuration_c=>sc_node-lt_backup_amount                              " Node to Create
            is_data            = lr_longterm_backup_amount                                                       " Data
            iv_assoc_key       = /hec1/if_configuration_c=>sc_association-lt_backup_class-lt_backup_amount       " Association
            iv_source_node_key = is_ctx-node_key                                                                 " Parent Node
            iv_source_key      = ls_longterm_backup_class-key                                                    " NodeID of Parent Instance
            iv_root_key        = ls_longterm_backup_class-root_key                                               " Root NodeID
          IMPORTING
            ev_key             = DATA(new_instance_key)
        ).

        "-----------------------------------
        " Fill export parameter
        "-----------------------------------
        ASSIGN et_data TO FIELD-SYMBOL(<fs_export_parameters>).
        DATA(lt_export_parameters) = VALUE /bobf/t_frw_key_incl( ( key        = new_instance_key
                                                                   parent_key = ls_longterm_backup_class-key
                                                                   root_key   = ls_longterm_backup_class-root_key ) ).
        <fs_export_parameters> = lt_export_parameters.

      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.
  ENDMETHOD.


  METHOD add_add_storage_datacenter.
    DATA:
      lt_modification   TYPE /bobf/t_frw_modification,
      lr_add_storage_dc TYPE REF TO /hec1/s_add_storage_dc_cs.

    /hec1/cl_config_helper=>get_general_data( EXPORTING iv_node_key      = is_ctx-node_key
                                                        it_key           = it_key
                                                        io_read          = io_read
                                              IMPORTING er_landscape     = DATA(lr_landscape) ).

    lr_add_storage_dc = NEW /hec1/s_add_storage_dc_cs( ).

    lr_add_storage_dc->hec_node_add_storage_dc  = /rbp/cl_general_utilities=>get_new_guid22( ).
    lr_add_storage_dc->hec_apm_guid             = lr_landscape->hec_apm_guid.
    lr_add_storage_dc->hec_apm_descr            = lr_landscape->hec_apm_descr.
    lr_add_storage_dc->hec_row_selectable       = abap_true.
    lr_add_storage_dc->hec_delete_visible       = abap_true.
    GET TIME STAMP FIELD lr_add_storage_dc->crea_date_time.

    TRY.
        io_modify->create(
          EXPORTING
            iv_node            = /hec1/if_configuration_c=>sc_node-add_storage_datacenter             " Node to Create
            is_data            = lr_add_storage_dc                                                    " Data
            iv_assoc_key       = /hec1/if_configuration_c=>sc_association-root-add_storage_datacenter " Association
            iv_source_node_key = is_ctx-node_key                                                      " Parent Node
            iv_source_key      = lr_landscape->key                                                    " NodeID of Parent Instance
            iv_root_key        = lr_landscape->root_key                                               " Root NodeID
          IMPORTING
            ev_key             = DATA(new_instance_key)
        ).

        "-----------------------------------
        " Fill export parameter
        "-----------------------------------
        ASSIGN et_data TO FIELD-SYMBOL(<fs_export_parameters>).
        DATA(lt_export_parameters) = VALUE /bobf/t_frw_key_incl( ( key        = new_instance_key
                                                                   parent_key = it_key[ 1 ]-key
                                                                   root_key   = it_key[ 1 ]-key ) ).
        <fs_export_parameters> = lt_export_parameters.

      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.
  ENDMETHOD.


  METHOD add_add_storage_class.
    DATA:
      lt_modification      TYPE /bobf/t_frw_modification,
      lt_add_storage_dc    TYPE /hec1/t_add_storage_dc_ct,
      lr_add_storage_class TYPE REF TO /hec1/s_add_storage_class_cs.

    io_read->retrieve(
      EXPORTING
        iv_node                 = is_ctx-node_key
        it_key                  = it_key
        iv_fill_data            = abap_true
      IMPORTING
        eo_message              = eo_message
        et_data                 = lt_add_storage_dc
    ).

    DATA(ls_add_storage_dc) = VALUE #( lt_add_storage_dc[ 1 ] OPTIONAL ).

    lr_add_storage_class = NEW /hec1/s_add_storage_class_cs( ).
    lr_add_storage_class->hec_node_add_storage_dc    = ls_add_storage_dc-hec_node_add_storage_dc.
    lr_add_storage_class->hec_node_add_storage_class = /rbp/cl_general_utilities=>get_new_guid22( ).
    lr_add_storage_class->hec_apm_guid               = ls_add_storage_dc-hec_apm_guid.
    lr_add_storage_class->hec_apm_descr              = ls_add_storage_dc-hec_apm_descr.
    lr_add_storage_class->hec_node_datacenter_ref    = ls_add_storage_dc-hec_node_datacenter_ref.
    lr_add_storage_class->hec_datacenter_descr_ref   = ls_add_storage_dc-hec_datacenter_descr_ref.
    lr_add_storage_class->hec_row_selectable         = abap_true.
    lr_add_storage_class->hec_delete_visible         = abap_true.
    GET TIME STAMP FIELD lr_add_storage_class->crea_date_time.

    TRY.
        io_modify->create(
          EXPORTING
        iv_node            = /hec1/if_configuration_c=>sc_node-add_storage_class                                    " Node to Create
            is_data            = lr_add_storage_class                                                               " Data
            iv_assoc_key       = /hec1/if_configuration_c=>sc_association-add_storage_datacenter-add_storage_class  " Association
            iv_source_node_key = is_ctx-node_key                                                                    " Parent Node
            iv_source_key      = ls_add_storage_dc-key                                                              " NodeID of Parent Instance
            iv_root_key        = ls_add_storage_dc-root_key                                                         " Root NodeID
          IMPORTING
            ev_key             = DATA(new_instance_key)
        ).

        "-----------------------------------
        " Fill export parameter
        "-----------------------------------
        ASSIGN et_data TO FIELD-SYMBOL(<fs_export_parameters>).
        DATA(lt_export_parameters) = VALUE /bobf/t_frw_key_incl( ( key        = new_instance_key
                                                                   parent_key = ls_add_storage_dc-key
                                                                   root_key   = ls_add_storage_dc-root_key ) ).
        <fs_export_parameters> = lt_export_parameters.

      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.

  ENDMETHOD.


  METHOD add_add_storage_amount.
    DATA:
      lt_modification       TYPE /bobf/t_frw_modification,
      lt_add_storage_class  TYPE /hec1/t_add_storage_class_ct,
      lr_add_storage_amount TYPE REF TO /hec1/s_add_storage_amount_cs.

    io_read->retrieve(
      EXPORTING
        iv_node                 = is_ctx-node_key
        it_key                  = it_key
        iv_fill_data            = abap_true
      IMPORTING
        eo_message              = eo_message
        et_data                 = lt_add_storage_class
    ).

    DATA(ls_add_storage_class) = VALUE #( lt_add_storage_class[ 1 ] OPTIONAL ).

    lr_add_storage_amount = NEW /hec1/s_add_storage_amount_cs( ).
    lr_add_storage_amount->hec_node_add_storage_dc     = ls_add_storage_class-hec_node_add_storage_dc.
    lr_add_storage_amount->hec_node_add_storage_class  = ls_add_storage_class-hec_node_add_storage_class.
    lr_add_storage_amount->hec_astore_class_guid       = ls_add_storage_class-hec_astore_class_guid.
    lr_add_storage_amount->hec_node_add_storage_amount = /rbp/cl_general_utilities=>get_new_guid22( ).
    lr_add_storage_amount->hec_apm_guid                = ls_add_storage_class-hec_apm_guid.
    lr_add_storage_amount->hec_apm_descr               = ls_add_storage_class-hec_apm_descr.
    lr_add_storage_amount->hec_node_datacenter_ref     = ls_add_storage_class-hec_node_datacenter_ref.
    lr_add_storage_amount->hec_datacenter_descr_ref    = ls_add_storage_class-hec_datacenter_descr_ref.
    lr_add_storage_amount->hec_row_selectable          = abap_true.
    lr_add_storage_amount->hec_delete_visible          = abap_true.
    GET TIME STAMP FIELD lr_add_storage_amount->crea_date_time.

    TRY.
        io_modify->create(
          EXPORTING
            iv_node            = /hec1/if_configuration_c=>sc_node-add_storage_amount                           " Node to Create
            is_data            = lr_add_storage_amount                                                          " Data
            iv_assoc_key       = /hec1/if_configuration_c=>sc_association-add_storage_class-add_storage_amount  " Association
            iv_source_node_key = is_ctx-node_key                                                                " Parent Node
            iv_source_key      = ls_add_storage_class-key                                                       " NodeID of Parent Instance
            iv_root_key        = ls_add_storage_class-root_key                                                  " Root NodeID
          IMPORTING
            ev_key             = DATA(new_instance_key)
        ).

        "-----------------------------------
        " Fill export parameter
        "-----------------------------------
        ASSIGN et_data TO FIELD-SYMBOL(<fs_export_parameters>).
        DATA(lt_export_parameters) = VALUE /bobf/t_frw_key_incl( ( key        = new_instance_key
                                                                   parent_key = ls_add_storage_class-key
                                                                   root_key   = ls_add_storage_class-root_key ) ).
        <fs_export_parameters> = lt_export_parameters.


      CATCH /bobf/cx_frw_contrct_violation. " Caller violates a BOPF contract
    ENDTRY.
  ENDMETHOD.

ENDCLASS.