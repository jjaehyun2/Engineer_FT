class YCL_AIM_TSK_D_ACTION_PROPERTIE definition
  public
  inheriting from /BOBF/CL_LIB_D_SUPERCLASS
  final
  create public .

public section.

  methods /BOBF/IF_FRW_DETERMINATION~EXECUTE
    redefinition .
protected section.
private section.
ENDCLASS.



CLASS YCL_AIM_TSK_D_ACTION_PROPERTIE IMPLEMENTATION.


METHOD /bobf/if_frw_determination~execute.

    DATA lt_task TYPE yaim_tsk_t_root.
    DATA lo_property_helper TYPE REF TO /bobf/cl_lib_h_set_property.

    io_read->retrieve(
      EXPORTING
        iv_node                 = yif_aim_tsk_yaim_task_c=>sc_node-root    " Node Name
        it_key                  = it_key    " Key Table
        iv_fill_data            = abap_true    " Data element for domain BOOLE: TRUE (='X') and FALSE (=' ')
        it_requested_attributes = VALUE #( ( yif_aim_tsk_yaim_task_c=>sc_node_attribute-root-status ) )    " List of Names (e.g. Fieldnames)
      IMPORTING
        et_data                 = lt_task
    ).

    CREATE OBJECT lo_property_helper
      EXPORTING
        is_context = is_ctx    " Context Information for Determinations
        io_modify  = io_modify.    " Interface to Change Data

    LOOP AT lt_task REFERENCE INTO DATA(lr_task).

      lo_property_helper->set_action_enabled(
          iv_action_key = yif_aim_tsk_yaim_task_c=>sc_action-root-start    " Key of the action for which the property is to be set
          iv_key        = lr_task->key    " Key of the instance for which the property is to be set
          iv_value      = boolc( lr_task->status = '01' OR lr_task->status = '04' )    " New value of this property (true/false)
      ).

      lo_property_helper->set_action_enabled(
          iv_action_key = yif_aim_tsk_yaim_task_c=>sc_action-root-finish    " Key of the action for which the property is to be set
          iv_key        = lr_task->key    " Key of the instance for which the property is to be set
          iv_value      = boolc( lr_task->status = '02' )    " New value of this property (true/false)
      ).

      lo_property_helper->set_action_enabled(
          iv_action_key = yif_aim_tsk_yaim_task_c=>sc_action-root-reopen    " Key of the action for which the property is to be set
          iv_key        = lr_task->key    " Key of the instance for which the property is to be set
          iv_value      = boolc( lr_task->status = '03' )    " New value of this property (true/false)
      ).

    ENDLOOP.

  ENDMETHOD.
ENDCLASS.