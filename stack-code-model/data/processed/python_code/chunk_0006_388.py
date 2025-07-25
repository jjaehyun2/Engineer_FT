class ZCX_DELETE_EXCEPTION definition
  public
  inheriting from ZCX_BUGTRACKER_SYSTEM
  final
  create public .

*"* public components of class ZCX_DELETE_EXCEPTION
*"* do not include other source files here!!!
public section.

  constants:
    begin of ZCX_DELETE_EXCEPTION,
      msgid type symsgid value 'ZBT_CONTROLLER_MSG',
      msgno type symsgno value '001',
      attr1 type scx_attrname value '',
      attr2 type scx_attrname value '',
      attr3 type scx_attrname value '',
      attr4 type scx_attrname value '',
    end of ZCX_DELETE_EXCEPTION .

  methods CONSTRUCTOR
    importing
      !TEXTID like IF_T100_MESSAGE=>T100KEY optional
      !PREVIOUS like PREVIOUS optional .
protected section.
*"* protected components of class ZCX_DELETE_EXCEPTION
*"* do not include other source files here!!!
private section.
*"* private components of class ZCX_DELETE_EXCEPTION
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCX_DELETE_EXCEPTION IMPLEMENTATION.


method CONSTRUCTOR.
CALL METHOD SUPER->CONSTRUCTOR
EXPORTING
PREVIOUS = PREVIOUS
.
clear me->textid.
if textid is initial.
  IF_T100_MESSAGE~T100KEY = ZCX_DELETE_EXCEPTION .
else.
  IF_T100_MESSAGE~T100KEY = TEXTID.
endif.
endmethod.
ENDCLASS.