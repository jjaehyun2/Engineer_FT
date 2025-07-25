class ZCX_BC009_REQUEST definition
  public
  inheriting from CX_STATIC_CHECK
  create public .

public section.

  interfaces IF_T100_MESSAGE .

  data MESSAGE_VARIABLE_1 type SYMSGV .
  data MESSAGE_VARIABLE_2 type SYMSGV .
  data MESSAGE_VARIABLE_3 type SYMSGV .
  data MESSAGE_VARIABLE_4 type SYMSGV .

  methods CONSTRUCTOR
    importing
      !TEXTID like IF_T100_MESSAGE=>T100KEY optional
      !PREVIOUS like PREVIOUS optional
      !MESSAGE_VARIABLE_1 type SYMSGV optional
      !MESSAGE_VARIABLE_2 type SYMSGV optional
      !MESSAGE_VARIABLE_3 type SYMSGV optional
      !MESSAGE_VARIABLE_4 type SYMSGV optional .
protected section.
private section.
ENDCLASS.



CLASS ZCX_BC009_REQUEST IMPLEMENTATION.


method CONSTRUCTOR.
CALL METHOD SUPER->CONSTRUCTOR
EXPORTING
PREVIOUS = PREVIOUS
.
me->MESSAGE_VARIABLE_1 = MESSAGE_VARIABLE_1 .
me->MESSAGE_VARIABLE_2 = MESSAGE_VARIABLE_2 .
me->MESSAGE_VARIABLE_3 = MESSAGE_VARIABLE_3 .
me->MESSAGE_VARIABLE_4 = MESSAGE_VARIABLE_4 .
clear me->textid.
if textid is initial.
  IF_T100_MESSAGE~T100KEY = IF_T100_MESSAGE=>DEFAULT_TEXTID.
else.
  IF_T100_MESSAGE~T100KEY = TEXTID.
endif.
endmethod.
ENDCLASS.