class ZCX_EC_VERI_HATASI definition
  public
  inheriting from CX_STATIC_CHECK
  create public .

public section.

  interfaces IF_T100_DYN_MSG .
  interfaces IF_T100_MESSAGE .

  constants:
    begin of VERI_YOK,
      msgid type symsgid value 'ZKKM',
      msgno type symsgno value '000',
      attr1 type scx_attrname value '',
      attr2 type scx_attrname value '',
      attr3 type scx_attrname value '',
      attr4 type scx_attrname value '',
    end of VERI_YOK .
  constants:
    begin of MALZEME_TANIMSIZ,
      msgid type symsgid value 'ZKKM',
      msgno type symsgno value '001',
      attr1 type scx_attrname value 'MATNR',
      attr2 type scx_attrname value '',
      attr3 type scx_attrname value '',
      attr4 type scx_attrname value '',
    end of MALZEME_TANIMSIZ .
  data MATNR type CHAR18 .

  methods CONSTRUCTOR
    importing
      !TEXTID like IF_T100_MESSAGE=>T100KEY optional
      !PREVIOUS like PREVIOUS optional
      !MATNR type CHAR18 optional .
protected section.
private section.
ENDCLASS.



CLASS ZCX_EC_VERI_HATASI IMPLEMENTATION.


  method CONSTRUCTOR.
CALL METHOD SUPER->CONSTRUCTOR
EXPORTING
PREVIOUS = PREVIOUS
.
me->MATNR = MATNR .
clear me->textid.
if textid is initial.
  IF_T100_MESSAGE~T100KEY = IF_T100_MESSAGE=>DEFAULT_TEXTID.
else.
  IF_T100_MESSAGE~T100KEY = TEXTID.
endif.
  endmethod.
ENDCLASS.