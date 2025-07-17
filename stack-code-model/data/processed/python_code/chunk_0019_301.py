class YCL_AIM_TSK_D_ON_TASK_CREATED definition
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



CLASS YCL_AIM_TSK_D_ON_TASK_CREATED IMPLEMENTATION.


METHOD /bobf/if_frw_determination~execute.
    CLEAR: eo_message, et_failed_key.

    LOOP AT it_key INTO DATA(ls_key).
      io_modify->update(
        EXPORTING
          iv_node           = yif_aim_tsk_yaim_task_c=>sc_node-root
          iv_key            = ls_key-key
          is_data           = NEW yaim_tsk_s_root( status = '01' )
          it_changed_fields = VALUE #( ( yif_aim_tsk_yaim_task_c=>sc_node_attribute-root-status ) )
      ).
    ENDLOOP.
  ENDMETHOD.
ENDCLASS.