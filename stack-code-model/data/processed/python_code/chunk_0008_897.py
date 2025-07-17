class YCL_AIM_TSK_A_FINISH definition
  public
  inheriting from /BOBF/CL_LIB_A_SUPERCLASS
  final
  create public .

public section.

  methods /BOBF/IF_FRW_ACTION~EXECUTE
    redefinition .
protected section.
private section.
ENDCLASS.



CLASS YCL_AIM_TSK_A_FINISH IMPLEMENTATION.


method /BOBF/IF_FRW_ACTION~EXECUTE.

  data lr_task type ref to yaim_tsk_s_root.

  CREATE DATA lr_task.
  lr_task->status = '03'.

  loop at it_key into data(ls_key).
  io_modify->update(
    EXPORTING
      iv_node           = yif_aim_tsk_yaim_task_c=>sc_node-root    " Node
      iv_key            = ls_key-key    " Key
      is_data           = lr_task    " Data
      it_changed_fields = value #( ( yif_aim_tsk_yaim_task_c=>sc_node_attribute-root-status ) )
  ).
  ENDLOOP.

endmethod.
ENDCLASS.