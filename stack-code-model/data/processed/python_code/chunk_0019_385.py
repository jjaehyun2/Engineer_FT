class YCL_AIM_TSK_A_START definition
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



CLASS YCL_AIM_TSK_A_START IMPLEMENTATION.


METHOD /bobf/if_frw_action~execute.

  DATA lr_task TYPE REF TO yaim_tsk_s_root.

  CREATE DATA lr_task.
  lr_task->status = '02'.
  lr_task->assignee = sy-uname.

  LOOP AT it_key INTO DATA(ls_key).
    io_modify->update(
      EXPORTING
        iv_node           = yif_aim_tsk_yaim_task_c=>sc_node-root    " Node
        iv_key            = ls_key-key    " Key
        is_data           = lr_task    " Data
        it_changed_fields = VALUE #(
                              ( yif_aim_tsk_yaim_task_c=>sc_node_attribute-root-status )
                              ( yif_aim_tsk_yaim_task_c=>sc_node_attribute-root-assignee )
                            )
    ).
  ENDLOOP.

ENDMETHOD.
ENDCLASS.