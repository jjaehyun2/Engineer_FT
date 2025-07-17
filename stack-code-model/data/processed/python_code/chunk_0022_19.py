class ZCX_BATCH_INPUT_ERROR definition
  public
  inheriting from CX_DYNAMIC_CHECK
  final
  create public .

public section.
*"* public components of class ZCX_BATCH_INPUT_ERROR
*"* do not include other source files here!!!

  constants ZCX_BATCH_INPUT_ERROR type SOTR_CONC value '5361291C4CF11650E10080000AD00C21'. "#EC NOTEXT
  data MSGTY type SY-MSGTY .
  data MSG type STRING .
  data MSGID type SY-MSGID .
  data MSGNO type SY-MSGNO .
  data MSGV1 type SY-MSGV1 .
  data MSGV2 type SY-MSGV2 .
  data MSGV3 type SY-MSGV3 .
  data MSGV4 type SY-MSGV4 .

  methods CONSTRUCTOR
    importing
      !TEXTID like TEXTID optional
      !PREVIOUS like PREVIOUS optional
      !MSGTY type SY-MSGTY optional
      !MSG type STRING optional
      !MSGID type SY-MSGID optional
      !MSGNO type SY-MSGNO optional
      !MSGV1 type SY-MSGV1 optional
      !MSGV2 type SY-MSGV2 optional
      !MSGV3 type SY-MSGV3 optional
      !MSGV4 type SY-MSGV4 optional .
protected section.
*"* protected components of class ZCX_BATCH_INPUT_ERROR
*"* do not include other source files here!!!
private section.
*"* private components of class ZCX_BATCH_INPUT_ERROR
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCX_BATCH_INPUT_ERROR IMPLEMENTATION.


method CONSTRUCTOR.
CALL METHOD SUPER->CONSTRUCTOR
EXPORTING
TEXTID = TEXTID
PREVIOUS = PREVIOUS
.
 IF textid IS INITIAL.
   me->textid = ZCX_BATCH_INPUT_ERROR .
 ENDIF.
me->MSGTY = MSGTY .
me->MSG = MSG .
me->MSGID = MSGID .
me->MSGNO = MSGNO .
me->MSGV1 = MSGV1 .
me->MSGV2 = MSGV2 .
me->MSGV3 = MSGV3 .
me->MSGV4 = MSGV4 .
endmethod.
ENDCLASS.