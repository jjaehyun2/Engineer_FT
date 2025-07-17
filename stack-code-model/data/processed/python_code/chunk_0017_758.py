class ZCX_EC_TABLO_BOS definition
  public
  inheriting from CX_STATIC_CHECK
  create public .

public section.

  interfaces IF_T100_DYN_MSG .
  interfaces IF_T100_MESSAGE .

  constants:
    begin of BOMBOS,
      msgid type symsgid value 'ZKKM',
      msgno type symsgno value '004',
      attr1 type scx_attrname value 'TABNAME',
      attr2 type scx_attrname value '',
      attr3 type scx_attrname value '',
      attr4 type scx_attrname value '',
    end of BOMBOS .
  constants:
    begin of BU_SENE_BOS,
      msgid type symsgid value 'ZKKM',
      msgno type symsgno value '005',
      attr1 type scx_attrname value 'TABNAME',
      attr2 type scx_attrname value '',
      attr3 type scx_attrname value '',
      attr4 type scx_attrname value '',
    end of BU_SENE_BOS .
  data TABNAME type TABNAME .

  methods CONSTRUCTOR
    importing
      !TEXTID like IF_T100_MESSAGE=>T100KEY optional
      !PREVIOUS like PREVIOUS optional
      !TABNAME type TABNAME optional .
protected section.
private section.
ENDCLASS.



CLASS ZCX_EC_TABLO_BOS IMPLEMENTATION.


  method CONSTRUCTOR.
CALL METHOD SUPER->CONSTRUCTOR
EXPORTING
PREVIOUS = PREVIOUS
.
me->TABNAME = TABNAME .
clear me->textid.
if textid is initial.
  IF_T100_MESSAGE~T100KEY = IF_T100_MESSAGE=>DEFAULT_TEXTID.
else.
  IF_T100_MESSAGE~T100KEY = TEXTID.
endif.
  endmethod.
ENDCLASS.