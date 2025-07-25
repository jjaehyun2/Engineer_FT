class YCX_ADDICT_LOCK definition
  public
  inheriting from CX_STATIC_CHECK
  create public .

public section.

  interfaces IF_T100_DYN_MSG .
  interfaces IF_T100_MESSAGE .

  constants:
    begin of ALL_ITEMS_LOCKED,
      msgid type symsgid value 'YADDICT',
      msgno type symsgno value '214',
      attr1 type scx_attrname value '',
      attr2 type scx_attrname value '',
      attr3 type scx_attrname value '',
      attr4 type scx_attrname value '',
    end of ALL_ITEMS_LOCKED .
  constants:
    begin of ITEM_LOCKED,
      msgid type symsgid value 'YADDICT',
      msgno type symsgno value '255',
      attr1 type scx_attrname value 'OBJECTID',
      attr2 type scx_attrname value '',
      attr3 type scx_attrname value '',
      attr4 type scx_attrname value '',
    end of ITEM_LOCKED .
  constants:
    begin of NOT_LOCKED_YET,
      msgid type symsgid value 'YADDICT',
      msgno type symsgno value '535',
      attr1 type scx_attrname value '',
      attr2 type scx_attrname value '',
      attr3 type scx_attrname value '',
      attr4 type scx_attrname value '',
    end of NOT_LOCKED_YET .
  constants:
    begin of LOCKED_FOR_TOO_LONG,
      msgid type symsgid value 'YADDICT',
      msgno type symsgno value '526',
      attr1 type scx_attrname value 'OBJECTID',
      attr2 type scx_attrname value 'BNAME',
      attr3 type scx_attrname value '',
      attr4 type scx_attrname value '',
    end of LOCKED_FOR_TOO_LONG .
  constants:
    begin of ITEM_LOCKED_BY_USER,
      msgid type symsgid value 'YADDICT',
      msgno type symsgno value '254',
      attr1 type scx_attrname value 'OBJECTID',
      attr2 type scx_attrname value 'BNAME',
      attr3 type scx_attrname value '',
      attr4 type scx_attrname value '',
    end of ITEM_LOCKED_BY_USER .
  constants:
    begin of LOCKED_BY_USER,
      msgid type symsgid value 'YADDICT',
      msgno type symsgno value '220',
      attr1 type scx_attrname value 'BNAME',
      attr2 type scx_attrname value '',
      attr3 type scx_attrname value '',
      attr4 type scx_attrname value '',
    end of LOCKED_BY_USER .
  data BNAME type XUBNAME .
  data OBJECTID type CDOBJECTV .

  methods CONSTRUCTOR
    importing
      !TEXTID like IF_T100_MESSAGE=>T100KEY optional
      !PREVIOUS like PREVIOUS optional
      !BNAME type XUBNAME optional
      !OBJECTID type CDOBJECTV optional .
protected section.
private section.
ENDCLASS.



CLASS YCX_ADDICT_LOCK IMPLEMENTATION.


  method CONSTRUCTOR.
CALL METHOD SUPER->CONSTRUCTOR
EXPORTING
PREVIOUS = PREVIOUS
.
me->BNAME = BNAME .
me->OBJECTID = OBJECTID .
clear me->textid.
if textid is initial.
  IF_T100_MESSAGE~T100KEY = IF_T100_MESSAGE=>DEFAULT_TEXTID.
else.
  IF_T100_MESSAGE~T100KEY = TEXTID.
endif.
  endmethod.
ENDCLASS.