class ZCL_AIM_ABSTR_EXT_TOOL_ADAPTER definition
  public
  abstract
  create public .

public section.

  interfaces ZIF_AIM_EXTERNAL_TOOL_ADAPTER .
protected section.

  methods VALIDATE_REFERENCE_FORMAT
    importing
      !IV_EXT_REFERENCE_EXTERNAL_ID type YAIM_TASK_EXT_REF-EXTERNAL_ID
    raising
      ZCX_AIM_EXTERNAL_TOOL .
  methods CHECK_REMOTE_CONNECTION
    raising
      ZCX_AIM_EXTERNAL_TOOL .
  methods GET_TASK_FROM_EXT_SYSTEM
  abstract
    importing
      !IS_EXT_REFERENCE type YAIM_TASK_EXT_REF
    exporting
      !EV_EXISTS type ABAP_BOOL
      !EV_TITLE type YAIM_TASK_TITLE
      !EV_PRIORITY type YAIM_TASK_PRIORITY
      !EV_DESCRIPTION type YAIM_TASK_DESCRIPTION
      !EV_STATUS type YAIM_TASK_STATUS
      !EV_ASSIGNEE type YAIM_TASK_ASSIGNEE
    raising
      ZCX_AIM_EXTERNAL_TOOL .
  methods MAP_FULL_NAME_TO_USER
    importing
      !IV_PERSON_FULL_NAME type STRING
    returning
      value(RV_USER_NAME) type YAIM_TASK_ASSIGNEE .
private section.
ENDCLASS.



CLASS ZCL_AIM_ABSTR_EXT_TOOL_ADAPTER IMPLEMENTATION.










ENDCLASS.