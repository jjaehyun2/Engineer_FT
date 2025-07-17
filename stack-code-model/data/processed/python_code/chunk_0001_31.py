class ZCL_AIM_TMT_ADAPTER definition
  public
  inheriting from ZCL_AIM_ABSTR_EXT_TOOL_ADAPTER
  final
  create public .

public section.
protected section.

  methods GET_TASK_FROM_EXT_SYSTEM
    redefinition .
private section.
ENDCLASS.



CLASS ZCL_AIM_TMT_ADAPTER IMPLEMENTATION.


METHOD get_task_from_ext_system.
*    Data declarations match the external API's types.
*    Unfortunately, those developers seem not to care about proper domains
  DATA lv_title_tmt TYPE char100.
  DATA lv_severity_tmt TYPE char1.
  DATA lv_description_tmt TYPE string.
  DATA lv_state_tmt TYPE char1.
  DATA lv_processor_tmt TYPE string.

  CONSTANTS co_state_tmt_not_exists TYPE char1 VALUE 'Ö'.

  DATA lv_ticket_no_tmt TYPE char10.
  lv_ticket_no_tmt = is_ext_reference-external_id. "An unnecessary move bites the dust

  CALL FUNCTION 'ZAIM_GET_TASK_TMT'
    EXPORTING
      iv_ticket_no   = lv_ticket_no_tmt
    IMPORTING
      ev_title       = lv_title_tmt
      ev_severity    = lv_severity_tmt
      ev_description = lv_description_tmt
      ev_state       = lv_state_tmt
      ev_processor   = lv_processor_tmt.

  IF lv_state_tmt NE co_state_tmt_not_exists.

    ev_exists = abap_true.
    ev_title = lv_title_tmt.
    ev_description = lv_description_tmt.

*  translate TMT-severity to AIM priority
    CASE lv_severity_tmt.
      WHEN 'V'.
        ev_priority = yif_aim_task_constants=>priority-critical.
      WHEN 'H'.
        ev_priority = yif_aim_task_constants=>priority-high.
      WHEN 'M'.
        ev_priority = yif_aim_task_constants=>priority-medium.
      WHEN 'L'.
        ev_priority = yif_aim_task_constants=>priority-low.
      WHEN OTHERS.
        "must not occur => mapping error
        ASSERT 1 = 0.
    ENDCASE.

*  translate status values to AIM
    CASE lv_state_tmt.
      WHEN 1.
        ev_status = yif_aim_task_constants=>status-new.
      WHEN 2.
        ev_status = yif_aim_task_constants=>status-in_progress.
      WHEN 3.
        ev_status = yif_aim_task_constants=>status-finished.
      WHEN 4.
        ev_status = yif_aim_task_constants=>status-reverted.
      WHEN OTHERS.
        "must not occur => mapping error
        ASSERT 1 = 0.
    ENDCASE.

*  map the assignee
    DATA lv_assignee TYPE yaim_task_assignee.
    IF lv_processor_tmt IS NOT INITIAL.
    ev_assignee = map_full_name_to_user( lv_processor_tmt ).
    ENDIF.
    else.
        ev_exists = abap_false.
    endif.

  ENDMETHOD.
ENDCLASS.