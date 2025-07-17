class ZCL_AIM_BUGZILLA_ADAPTER definition
  public
  inheriting from ZCL_AIM_ABSTR_EXT_TOOL_ADAPTER
  final
  create public .

public section.
protected section.
  methods get_task_from_ext_system REDEFINITION.
private section.
ENDCLASS.



CLASS ZCL_AIM_BUGZILLA_ADAPTER IMPLEMENTATION.


METHOD get_task_from_ext_system.

    DATA lv_title_bugzilla TYPE string.
    DATA lv_severity_bugzilla TYPE string.
    DATA lv_description_bugzilla TYPE string.
    DATA lv_state_bugzilla TYPE string.
    DATA lv_processor_bugzilla TYPE string.
    DATA lv_bug_not_found TYPE abap_bool.

    DATA lv_ticket_no_bugzilla TYPE string.
    lv_ticket_no_bugzilla = is_ext_reference-external_id. "An unnecessary move bites the dust

    CALL FUNCTION 'ZAIM_GET_TASK_BUGZILLA'
      EXPORTING
        iv_ticket_no     = lv_ticket_no_bugzilla
      IMPORTING
        ev_title         = lv_title_bugzilla
        ev_severity      = lv_severity_bugzilla
        ev_description   = lv_description_bugzilla
        ev_state         = lv_state_bugzilla
        ev_processor     = lv_processor_bugzilla
        ev_bug_not_found = lv_bug_not_found.

    IF lv_bug_not_found = abap_false.
      ev_exists = abap_true.
      ev_title = lv_title_bugzilla.
      ev_description = lv_description_bugzilla.

*  translate bugzilla priority to AIM priority
      CASE lv_severity_bugzilla.
        WHEN 'Very High'.
          ev_priority = yif_aim_task_constants=>priority-critical.
        WHEN 'High'.
          ev_priority = yif_aim_task_constants=>priority-high.
        WHEN 'Medium'.
          ev_priority = yif_aim_task_constants=>priority-medium.
        WHEN 'Low'.
          ev_priority = yif_aim_task_constants=>priority-low.
        WHEN OTHERS.
          "must not occur => mapping error
          ASSERT 1 = 0.
      ENDCASE.

*  translate status values to AIM
      CASE lv_state_bugzilla.
        WHEN 'New'.
          ev_status = yif_aim_task_constants=>status-new.
        WHEN 'In progress'.
          ev_status = yif_aim_task_constants=>status-in_progress.
        WHEN 'Done'.
          ev_status = yif_aim_task_constants=>status-finished.
        WHEN 'Questioned'.
          ev_status = yif_aim_task_constants=>status-reverted.
        WHEN OTHERS.
          "must not occur => mapping error
          ASSERT 1 = 0.
      ENDCASE.

*    map processor
      ev_assignee = map_full_name_to_user( lv_processor_bugzilla ).
    ELSE.
      ev_exists = abap_false.
    ENDIF.

  ENDMETHOD.
ENDCLASS.