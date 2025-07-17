class ZCX_REST_SERVICE_EXCEPTION definition
  public
  inheriting from CX_NO_CHECK
  create public .

public section.

  interfaces IF_T100_DYN_MSG .
  interfaces IF_T100_MESSAGE .

  constants:
    begin of METHOD_NOT_SUPPORTED,
      msgid type symsgid value 'ZREST_MESSAGES',
      msgno type symsgno value '001',
      attr1 type scx_attrname value 'METHOD',
      attr2 type scx_attrname value '',
      attr3 type scx_attrname value '',
      attr4 type scx_attrname value '',
    end of METHOD_NOT_SUPPORTED .
  data METHOD type STRING .

  methods CONSTRUCTOR
    importing
      !TEXTID like IF_T100_MESSAGE=>T100KEY optional
      !PREVIOUS like PREVIOUS optional
      !METHOD type STRING optional .
protected section.
private section.
ENDCLASS.



CLASS ZCX_REST_SERVICE_EXCEPTION IMPLEMENTATION.


  method CONSTRUCTOR.
CALL METHOD SUPER->CONSTRUCTOR
EXPORTING
PREVIOUS = PREVIOUS
.
me->METHOD = METHOD .
clear me->textid.
if textid is initial.
  IF_T100_MESSAGE~T100KEY = IF_T100_MESSAGE=>DEFAULT_TEXTID.
else.
  IF_T100_MESSAGE~T100KEY = TEXTID.
endif.
  endmethod.
ENDCLASS.