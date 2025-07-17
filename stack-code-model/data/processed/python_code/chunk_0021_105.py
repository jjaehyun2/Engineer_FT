class YCL_AIM_TSK_V_ACTION_MANAGEMEN definition
  public
  inheriting from /BOBF/CL_LIB_V_SUPERCLASS
  final
  create public .

public section.

  methods /BOBF/IF_FRW_VALIDATION~EXECUTE
    redefinition .
protected section.
private section.
ENDCLASS.



CLASS YCL_AIM_TSK_V_ACTION_MANAGEMEN IMPLEMENTATION.


METHOD /bobf/if_frw_validation~execute.

  DATA lt_task TYPE yaim_tsk_t_root.

  io_read->retrieve(
    EXPORTING
      iv_node                 = yif_aim_tsk_yaim_task_c=>sc_node-root    " Node Name
      it_key                  = it_key    " Key Table
      iv_fill_data            = abap_true    " Data element for domain BOOLE: TRUE (='X') and FALSE (=' ')
      it_requested_attributes = VALUE #( ( yif_aim_tsk_yaim_task_c=>sc_node_attribute-root-status ) )    " List of Names (e.g. Fieldnames)
    IMPORTING
      et_data                 = lt_task
  ).

  LOOP AT lt_task REFERENCE INTO DATA(lr_task).
    CASE lr_task->status.
      WHEN '01' OR '04'. "New or stopped
        IF is_ctx-act_key NE yif_aim_tsk_yaim_task_c=>sc_action-root-start.
          INSERT VALUE #( key = lr_task->key ) INTO TABLE et_failed_key.
        ENDIF.
      WHEN '02'. "In Progress
        IF is_ctx-act_key NE yif_aim_tsk_yaim_task_c=>sc_action-root-finish.
          INSERT VALUE #( key = lr_task->key ) INTO TABLE et_failed_key.
        ENDIF.
      WHEN '03'. "Finished
        IF is_ctx-act_key NE yif_aim_tsk_yaim_task_c=>sc_action-root-reopen.
          INSERT VALUE #( key = lr_task->key ) INTO TABLE et_failed_key.
        ENDIF.
    ENDCASE.

  ENDLOOP.

ENDMETHOD.
ENDCLASS.