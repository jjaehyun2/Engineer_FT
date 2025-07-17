class YCM_AIM_TASK definition
  public
  inheriting from /BOBF/CM_FRW
  create public .

public section.

  constants:
    begin of INVALID_ASSIGNEE,
      msgid type symsgid value 'YAIM_TASK',
      msgno type symsgno value '001',
      attr1 type scx_attrname value 'MV_ASSIGNEE',
      attr2 type scx_attrname value 'MV_PROJECT_ABBREVIATION',
      attr3 type scx_attrname value '',
      attr4 type scx_attrname value '',
    end of INVALID_ASSIGNEE .
  data MV_ASSIGNEE type YAIM_TASK_ASSIGNEE .
  data MV_PROJECT_ABBREVIATION type YAIM_PROJECT_ABBREVIATION .

  methods CONSTRUCTOR
    importing
      !TEXTID like IF_T100_MESSAGE=>T100KEY optional
      !PREVIOUS like PREVIOUS optional
      !SEVERITY type TY_MESSAGE_SEVERITY optional
      !SYMPTOM type TY_MESSAGE_SYMPTOM optional
      !LIFETIME type TY_MESSAGE_LIFETIME default CO_LIFETIME_TRANSITION
      !MS_ORIGIN_LOCATION type /BOBF/S_FRW_LOCATION optional
      !MT_ENVIRONMENT_LOCATION type /BOBF/T_FRW_LOCATION optional
      !MV_ACT_KEY type /BOBF/ACT_KEY optional
      !MV_ASSOC_KEY type /BOBF/OBM_ASSOC_KEY optional
      !MV_BOPF_LOCATION type /BOBF/CONF_KEY optional
      !MV_DET_KEY type /BOBF/DET_KEY optional
      !MV_QUERY_KEY type /BOBF/OBM_QUERY_KEY optional
      !MV_VAL_KEY type /BOBF/VAL_KEY optional
      !MV_ASSIGNEE type YAIM_TASK_ASSIGNEE optional
      !MV_PROJECT_ABBREVIATION type YAIM_PROJECT_ABBREVIATION optional .
protected section.
private section.
ENDCLASS.



CLASS YCM_AIM_TASK IMPLEMENTATION.


  method CONSTRUCTOR.
CALL METHOD SUPER->CONSTRUCTOR
EXPORTING
PREVIOUS = PREVIOUS
SEVERITY = SEVERITY
SYMPTOM = SYMPTOM
LIFETIME = LIFETIME
MS_ORIGIN_LOCATION = MS_ORIGIN_LOCATION
MT_ENVIRONMENT_LOCATION = MT_ENVIRONMENT_LOCATION
MV_ACT_KEY = MV_ACT_KEY
MV_ASSOC_KEY = MV_ASSOC_KEY
MV_BOPF_LOCATION = MV_BOPF_LOCATION
MV_DET_KEY = MV_DET_KEY
MV_QUERY_KEY = MV_QUERY_KEY
MV_VAL_KEY = MV_VAL_KEY
.
me->MV_ASSIGNEE = MV_ASSIGNEE .
me->MV_PROJECT_ABBREVIATION = MV_PROJECT_ABBREVIATION .
clear me->textid.
if textid is initial.
  IF_T100_MESSAGE~T100KEY = IF_T100_MESSAGE=>DEFAULT_TEXTID.
else.
  IF_T100_MESSAGE~T100KEY = TEXTID.
endif.
  endmethod.
ENDCLASS.