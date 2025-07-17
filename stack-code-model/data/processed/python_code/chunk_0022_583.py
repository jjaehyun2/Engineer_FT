"! <p class="shorttext synchronized" lang="en">Project Exception</p>
class ZCX_PT_MANAGEMENT definition
  public
  inheriting from /BOBF/CM_FRW
  create public .

public section.

  constants:
      "! <p class="shorttext synchronized" lang="en">Project is mandatory</p>
    BEGIN OF project_mandatory,
        msgid TYPE symsgid VALUE 'ZTT_TASK',
        msgno TYPE symsgno VALUE '001',
        attr1 TYPE scx_attrname VALUE 'TEXT1',
        attr2 TYPE scx_attrname VALUE 'TEXT2',
        attr3 TYPE scx_attrname VALUE 'TEXT3',
        attr4 TYPE scx_attrname VALUE 'TEXT4',
      END OF project_mandatory .
  constants:
      "! <p class="shorttext synchronized" lang="en">Task &amp;1 is already ended</p>
    BEGIN OF task_ended,
        msgid TYPE symsgid VALUE 'ZTT_TASK',
        msgno TYPE symsgno VALUE '002',
        attr1 TYPE scx_attrname VALUE 'TEXT1',
        attr2 TYPE scx_attrname VALUE 'TEXT2',
        attr3 TYPE scx_attrname VALUE 'TEXT3',
        attr4 TYPE scx_attrname VALUE 'TEXT4',
      END OF task_ended .
  constants:
      "! <p class="shorttext synchronized" lang="en">End time is mandatory for final status</p>
    BEGIN OF task_end_time,
        msgid TYPE symsgid VALUE 'ZTT_TASK',
        msgno TYPE symsgno VALUE '003',
        attr1 TYPE scx_attrname VALUE 'TEXT1',
        attr2 TYPE scx_attrname VALUE 'TEXT2',
        attr3 TYPE scx_attrname VALUE 'TEXT3',
        attr4 TYPE scx_attrname VALUE 'TEXT4',
      END OF task_end_time .
  constants:
      "! <p class="shorttext synchronized" lang="en">Set final status for an end time</p>
    BEGIN OF task_status_end_time,
        msgid TYPE symsgid VALUE 'ZTT_TASK',
        msgno TYPE symsgno VALUE '004',
        attr1 TYPE scx_attrname VALUE 'TEXT1',
        attr2 TYPE scx_attrname VALUE 'TEXT2',
        attr3 TYPE scx_attrname VALUE 'TEXT3',
        attr4 TYPE scx_attrname VALUE 'TEXT4',
      END OF task_status_end_time .
  constants:
      "! <p class="shorttext synchronized" lang="en">Transport Request &amp;1 is still open</p>
    BEGIN OF transport_request_open,
        msgid TYPE symsgid VALUE 'ZTT_TASK',
        msgno TYPE symsgno VALUE '005',
        attr1 TYPE scx_attrname VALUE 'TEXT1',
        attr2 TYPE scx_attrname VALUE 'TEXT2',
        attr3 TYPE scx_attrname VALUE 'TEXT3',
        attr4 TYPE scx_attrname VALUE 'TEXT4',
      END OF transport_request_open .
  constants:
      "! <p class="shorttext synchronized" lang="en">Maximum progress is 100%</p>
    BEGIN OF progress_over_100,
        msgid TYPE symsgid VALUE 'ZTT_TASK',
        msgno TYPE symsgno VALUE '006',
        attr1 TYPE scx_attrname VALUE 'TEXT1',
        attr2 TYPE scx_attrname VALUE 'TEXT2',
        attr3 TYPE scx_attrname VALUE 'TEXT3',
        attr4 TYPE scx_attrname VALUE 'TEXT4',
      END OF progress_over_100 .
  constants:
      "! <p class="shorttext synchronized" lang="en">Set 100% progress for an ended task</p>
    BEGIN OF ended_task_progress_not_100,
        msgid TYPE symsgid VALUE 'ZTT_TASK',
        msgno TYPE symsgno VALUE '007',
        attr1 TYPE scx_attrname VALUE 'TEXT1',
        attr2 TYPE scx_attrname VALUE 'TEXT2',
        attr3 TYPE scx_attrname VALUE 'TEXT3',
        attr4 TYPE scx_attrname VALUE 'TEXT4',
      END OF ended_task_progress_not_100 .
  constants:
      "! <p class="shorttext synchronized" lang="en">Task is at 100% progress, please set end status</p>
    BEGIN OF progress_100_non_ended_task,
        msgid TYPE symsgid VALUE 'ZTT_TASK',
        msgno TYPE symsgno VALUE '008',
        attr1 TYPE scx_attrname VALUE 'TEXT1',
        attr2 TYPE scx_attrname VALUE 'TEXT2',
        attr3 TYPE scx_attrname VALUE 'TEXT3',
        attr4 TYPE scx_attrname VALUE 'TEXT4',
      END OF progress_100_non_ended_task .
  constants:
      "! <p class="shorttext synchronized" lang="en">Task has been changed by another process, please refresh</p>
    BEGIN OF task_changed,
        msgid TYPE symsgid VALUE 'ZTT_TASK',
        msgno TYPE symsgno VALUE '009',
        attr1 TYPE scx_attrname VALUE 'TEXT1',
        attr2 TYPE scx_attrname VALUE 'TEXT2',
        attr3 TYPE scx_attrname VALUE 'TEXT3',
        attr4 TYPE scx_attrname VALUE 'TEXT4',
      END OF task_changed .
    "! <p class="shorttext synchronized" lang="en">Text 1</p>
  data TEXT1 type STRING .
    "! <p class="shorttext synchronized" lang="en">Text 2</p>
  data TEXT2 type STRING .
    "! <p class="shorttext synchronized" lang="en">Text 3</p>
  data TEXT3 type STRING .
    "! <p class="shorttext synchronized" lang="en">Text 4</p>
  data TEXT4 type STRING .

    "! <p class="shorttext synchronized" lang="en">Collect exception to BOPF messages</p>
    "!
    "! @parameter exception | <p class="shorttext synchronized" lang="en">Exception</p>
    "! @parameter message_type | <p class="shorttext synchronized" lang="en">Message type</p>
    "! @parameter bo_key | <p class="shorttext synchronized" lang="en">Business Object Key</p>
    "! @parameter node | <p class="shorttext synchronized" lang="en">Node</p>
    "! @parameter key | <p class="shorttext synchronized" lang="en">Key</p>
    "! @parameter attribute | <p class="shorttext synchronized" lang="en">Attribute</p>
    "! @parameter bo_messages | <p class="shorttext synchronized" lang="en">BOPF Messages</p>
  class-methods COLLECT_BO_MESSAGE
    importing
      !TEXTID type SCX_T100KEY optional
      !TEXT1 type STRING optional
      !TEXT2 type STRING optional
      !TEXT3 type STRING optional
      !TEXT4 type STRING optional
      !PREVIOUS type ref to CX_ROOT optional
      !MESSAGE_TYPE type SYMSGTY default 'E'
      !SYMPTOM type TY_MESSAGE_SYMPTOM optional
      !BO_KEY type /BOBF/OBM_BO_KEY optional
      !NODE type /BOBF/OBM_NODE_KEY optional
      !KEY type /BOBF/CONF_KEY optional
      !ACT_KEY type /BOBF/ACT_KEY optional
      !VAL_KEY type /BOBF/VAL_KEY optional
      !ATTRIBUTE type STRING optional
    changing
      !BO_MESSAGES type ref to /BOBF/IF_FRW_MESSAGE .
    "! <p class="shorttext synchronized" lang="en">Raise exception from system variables</p>
    "!
    "! @raising zcx_tt_after_req_creation | <p class="shorttext synchronized" lang="en">Tasks Tracker management exc</p>
  class-methods RAISE_SYST
    importing
      !NODE_ATTRIBUTE type STRING optional
      !ORIGIN_LOCATION type /BOBF/S_FRW_LOCATION optional
    raising
      ZCX_TT_MANAGEMENT .
    "! <p class="shorttext synchronized" lang="en">CONSTRUCTOR</p>
    "!
    "! @parameter textid | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter text1 | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter text2 | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter text3 | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter text4 | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter previous | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter severity | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter symptom | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter lifetime | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter ms_origin_location | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter mt_environment_location | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter mv_act_key | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter mv_assoc_key | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter mv_bopf_location | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter mv_det_key | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter mv_query_key | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter mv_val_key | <p class="shorttext synchronized" lang="en"></p>
  methods CONSTRUCTOR
    importing
      !TEXTID like IF_T100_MESSAGE=>T100KEY optional
      !PREVIOUS like PREVIOUS optional
      !SEVERITY type TY_MESSAGE_SEVERITY optional
      !SYMPTOM type TY_MESSAGE_SYMPTOM optional
      !LIFETIME type TY_MESSAGE_LIFETIME default CO_LIFETIME_STATE
      !MS_ORIGIN_LOCATION type /BOBF/S_FRW_LOCATION optional
      !MT_ENVIRONMENT_LOCATION type /BOBF/T_FRW_LOCATION optional
      !MV_ACT_KEY type /BOBF/ACT_KEY optional
      !MV_ASSOC_KEY type /BOBF/OBM_ASSOC_KEY optional
      !MV_BOPF_LOCATION type /BOBF/CONF_KEY optional
      !MV_DET_KEY type /BOBF/DET_KEY optional
      !MV_QUERY_KEY type /BOBF/OBM_QUERY_KEY optional
      !MV_VAL_KEY type /BOBF/VAL_KEY optional
      !TEXT1 type STRING optional
      !TEXT2 type STRING optional
      !TEXT3 type STRING optional
      !TEXT4 type STRING optional .
  PROTECTED SECTION.

  PRIVATE SECTION.

ENDCLASS.



CLASS ZCX_PT_MANAGEMENT IMPLEMENTATION.


  METHOD COLLECT_BO_MESSAGE.

    DATA(exception) = NEW zcx_tt_management( textid              = textid
                                              text1              = text1
                                              text2              = text2
                                              text3              = text3
                                              text4              = text4
                                              previous           = previous
                                              severity           = message_type
                                              symptom            = symptom
                                              ms_origin_location =
                                                    VALUE #( bo_key     = bo_key
                                                             node_key   = node
                                                             key        = key
                                                             attributes = COND #( WHEN attribute IS NOT INITIAL
                                                                                      THEN VALUE #( ( attribute ) ) ) )
                                              mv_act_key         = act_key
                                              mv_assoc_key       = val_key
                                              mv_val_key         = val_key ).

    IF bo_messages IS NOT BOUND.
      bo_messages = /bobf/cl_frw_factory=>get_message( ).
    ENDIF.
    bo_messages->add_cm( exception ).

  ENDMETHOD.


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
me->TEXT1 = TEXT1 .
me->TEXT2 = TEXT2 .
me->TEXT3 = TEXT3 .
me->TEXT4 = TEXT4 .
clear me->textid.
if textid is initial.
  IF_T100_MESSAGE~T100KEY = IF_T100_MESSAGE=>DEFAULT_TEXTID.
else.
  IF_T100_MESSAGE~T100KEY = TEXTID.
endif.
  endmethod.


  METHOD RAISE_SYST.

    RAISE EXCEPTION TYPE zcx_tt_management
      EXPORTING
        textid             = VALUE scx_t100key( msgid = sy-msgid
                                                msgno = sy-msgno
                                                attr1 = 'TEXT1'
                                                attr2 = 'TEXT2'
                                                attr3 = 'TEXT3'
                                                attr4 = 'TEXT4' )
        text1              = CONV #( sy-msgv1 )
        text2              = CONV #( sy-msgv2 )
        text3              = CONV #( sy-msgv3 )
        text4              = CONV #( sy-msgv4 )
        ms_origin_location = origin_location.

  ENDMETHOD.
ENDCLASS.