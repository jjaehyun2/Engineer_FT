class ZCX_PT_AFTER_REQ_CREATION definition
  public
  inheriting from ZCX_PT_MANAGEMENT
  create public .

public section.

    "! <p class="shorttext synchronized" lang="en">CONSTRUCTOR</p>
    "!
    "! @parameter textid   | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter text1    | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter text2    | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter text3    | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter text4    | <p class="shorttext synchronized" lang="en"></p>
    "! @parameter previous | <p class="shorttext synchronized" lang="en"></p>
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
    "! <p class="shorttext synchronized" lang="en">Raise exception from system variables</p>
    "!
    "! @raising zcx_tt_after_req_creation | <p class="shorttext synchronized" lang="en">After request creation exc.</p>
  class-methods RAISE_SYST_AFTER_REQ_CREATION
    raising
      ZCX_TT_AFTER_REQ_CREATION .
protected section.
  PRIVATE SECTION.
ENDCLASS.



CLASS ZCX_PT_AFTER_REQ_CREATION IMPLEMENTATION.


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
TEXT1 = TEXT1
TEXT2 = TEXT2
TEXT3 = TEXT3
TEXT4 = TEXT4
.
clear me->textid.
if textid is initial.
  IF_T100_MESSAGE~T100KEY = IF_T100_MESSAGE=>DEFAULT_TEXTID.
else.
  IF_T100_MESSAGE~T100KEY = TEXTID.
endif.
  endmethod.


  METHOD RAISE_SYST_AFTER_REQ_CREATION.

    RAISE EXCEPTION TYPE zcx_tt_after_req_creation
      EXPORTING
        message_key = VALUE scx_t100key( msgid = sy-msgid
                                         msgno = sy-msgno
                                         attr1 = 'TEXT1'
                                         attr2 = 'TEXT2'
                                         attr3 = 'TEXT3'
                                         attr4 = 'TEXT4' )
        text_attr1  = CONV #( sy-msgv1 )
        text_attr2  = CONV #( sy-msgv2 )
        text_attr3  = CONV #( sy-msgv3 )
        text_attr4  = CONV #( sy-msgv4 ).

  ENDMETHOD.
ENDCLASS.