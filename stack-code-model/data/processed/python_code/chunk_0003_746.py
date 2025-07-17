CLASS /hec1/cl_lib_d_superclass DEFINITION
  PUBLIC
  INHERITING FROM /bobf/cl_lib_d_superclass
  ABSTRACT
  CREATE PUBLIC
  GLOBAL FRIENDS /hec1/cl_lib_a_superclass.

  PUBLIC SECTION.

    METHODS /bobf/if_frw_determination~execute REDEFINITION.
  PROTECTED SECTION.

    METHODS execute ABSTRACT
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key
      RAISING
        /bobf/cx_frw
      .


    METHODS execute_tree
      IMPORTING
        !is_ctx        TYPE /bobf/s_frw_ctx_det
        !it_key        TYPE /bobf/t_frw_key
        !io_read       TYPE REF TO /bobf/if_frw_read
        !io_modify     TYPE REF TO /bobf/if_frw_modify
      EXPORTING
        !eo_message    TYPE REF TO /bobf/if_frw_message
        !et_failed_key TYPE /bobf/t_frw_key
      RAISING
        /bobf/cx_frw
      .

  PRIVATE SECTION.

    CLASS-DATA gv_switch TYPE abap_bool VALUE abap_true.
    CLASS-METHODS: set_switch IMPORTING iv_on TYPE any.
    CLASS-METHODS: get_switch RETURNING VALUE(rv_on) TYPE abap_bool.

    CLASS-DATA gv_tree_switch TYPE abap_bool VALUE abap_true.
    CLASS-METHODS: set_tree_switch IMPORTING iv_on TYPE any.
    CLASS-METHODS: get_tree_switch RETURNING VALUE(rv_on) TYPE abap_bool.

ENDCLASS.



CLASS /HEC1/CL_LIB_D_SUPERCLASS IMPLEMENTATION.


  METHOD /bobf/if_frw_determination~execute.

    " ************************************
    " THIS IS A TEMPORARY FIX TO ENSURE
    " THAT OLD CONFIGURATIONS ARE UPDATED
    " ************************************
    DATA: lt_root TYPE /hec1/t_config_root_ct.

    io_read->get_root_key( EXPORTING iv_node         = is_ctx-node_key
                                     it_key          = it_key
                           IMPORTING et_target_key   = DATA(lt_root_key) ).

    io_read->retrieve( EXPORTING iv_node                 = /hec1/if_configuration_c=>sc_node-root
                                 it_key                  = lt_root_key
                                 iv_fill_data            = abap_true
                       IMPORTING et_data                 = lt_root ).

    LOOP AT lt_root REFERENCE INTO DATA(lr_root)
      WHERE hec_contract_status IS INITIAL.

      lr_root->hec_contract_status = /hec1/if_config_constants=>gc_contract_status-initial.

      TRY.
          io_modify->update( EXPORTING iv_node  = /hec1/if_configuration_c=>sc_node-root
                                       iv_key   = lr_root->key
                                       is_data  = lr_root ).
        CATCH /bobf/cx_frw_contrct_violation.
      ENDTRY.

    ENDLOOP.
        " ************************************
    " END OF FIX
    " ************************************

    IF get_switch( ).
      me->execute(
        EXPORTING
          is_ctx        = is_ctx
          it_key        = it_key
          io_read       = io_read
          io_modify     = io_modify
        IMPORTING
          eo_message    = eo_message
          et_failed_key = et_failed_key
      ).
    ENDIF.

    IF get_tree_switch( ).
      me->execute_tree(
        EXPORTING
          is_ctx        = is_ctx
          it_key        = it_key
          io_read       = io_read
          io_modify     = io_modify
        IMPORTING
          eo_message    = eo_message
          et_failed_key = et_failed_key
      ).
    ENDIF.

  ENDMETHOD.


  METHOD get_switch.
    rv_on = gv_switch.
  ENDMETHOD.


  METHOD set_switch.
    gv_switch = iv_on.
  ENDMETHOD.


  METHOD get_tree_switch.
    rv_on = gv_tree_switch.
  ENDMETHOD.


  METHOD set_tree_switch.
    gv_tree_switch = iv_on.
  ENDMETHOD.


  METHOD execute_tree.
    RETURN.
  ENDMETHOD.
ENDCLASS.