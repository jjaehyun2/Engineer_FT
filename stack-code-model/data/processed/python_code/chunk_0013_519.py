class YCL_AIM_TSK_D_SET_AUTHOR definition
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



CLASS YCL_AIM_TSK_D_SET_AUTHOR IMPLEMENTATION.


METHOD /bobf/if_frw_determination~execute.

  DATA lr_comment TYPE REF TO yaim_tsk_s_comment.

  CREATE DATA lr_comment.
  lr_comment->author = sy-uname.

  LOOP AT it_key INTO DATA(ls_key).
    io_modify->update(
      EXPORTING
        iv_node           = yif_aim_tsk_yaim_task_c=>sc_node-comment    " Node
        iv_key            = ls_key-key
        is_data           = lr_comment
        it_changed_fields = VALUE #( ( yif_aim_tsk_yaim_task_c=>sc_node_attribute-comment-author ) )
    ).
  ENDLOOP.

ENDMETHOD.
ENDCLASS.