class YCL_AIM_TSK_D_ATTRIBUTE_PROPER definition
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



CLASS YCL_AIM_TSK_D_ATTRIBUTE_PROPER IMPLEMENTATION.


METHOD /bobf/if_frw_determination~execute.

  CLEAR: eo_message, et_failed_key.

  DATA(lo_property_helper) = NEW /bobf/cl_lib_h_set_property(
      is_context = is_ctx
      io_modify  = io_modify
  ).

  DATA lt_task    TYPE yaim_tsk_t_root.

  io_read->retrieve(
    EXPORTING
      iv_node                 = is_ctx-node_key    " Node Name
      it_key                  = it_key    " Key Table
      iv_fill_data            = abap_true
      it_requested_attributes = VALUE #( ( yif_aim_tsk_yaim_task_c=>sc_node_attribute-root-status ) )
    IMPORTING
      et_data                 = lt_task
  ).

  LOOP AT lt_task REFERENCE INTO DATA(lr_task).
    lo_property_helper->set_node_update_enabled(
        iv_key   = lr_task->key
        iv_value = boolc( lr_task->status NE '03' ) "closed
    ).
  ENDLOOP.

ENDMETHOD.
ENDCLASS.