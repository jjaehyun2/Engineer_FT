class YCL_AIM_TSK_AUTHOR_USERDATA definition
  public
  inheriting from YCL_AIM_PRJ_D_DERIVE_USERDATA
  create public .

public section.

  methods CONSTRUCTOR .
protected section.
private section.
ENDCLASS.



CLASS YCL_AIM_TSK_AUTHOR_USERDATA IMPLEMENTATION.


method CONSTRUCTOR.
    super->constructor( ).
    mv_uname_attribute = yif_aim_tsk_yaim_task_c=>sc_node_attribute-comment-author.
  endmethod.
ENDCLASS.