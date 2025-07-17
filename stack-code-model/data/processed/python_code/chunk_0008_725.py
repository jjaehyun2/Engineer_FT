class YCX_DK_MSG definition
  public
  inheriting from CX_NO_CHECK
  final
  create public .

public section.

  class YDKMSG definition load .
  data MSG type YDKMSG=>TY_MSG read-only .

  methods CONSTRUCTOR
    importing
      !TEXTID like TEXTID optional
      !PREVIOUS like PREVIOUS optional
      !MSG type YDKMSG=>TY_MSG optional .

  methods IF_MESSAGE~GET_LONGTEXT
    redefinition .
  methods IF_MESSAGE~GET_TEXT
    redefinition .
protected section.
private section.
ENDCLASS.



CLASS YCX_DK_MSG IMPLEMENTATION.


  method CONSTRUCTOR.
CALL METHOD SUPER->CONSTRUCTOR
EXPORTING
TEXTID = TEXTID
PREVIOUS = PREVIOUS
.
me->MSG = MSG .
  endmethod.


  METHOD IF_MESSAGE~GET_LONGTEXT.
    result = me->get_text( ).
  ENDMETHOD.


  METHOD if_message~get_text.
    IF msg-msgid IS INITIAL.
      CONCATENATE msg-msgv1 msg-msgv2 msg-msgv3 msg-msgv4 INTO result SEPARATED BY space.
      RETURN.
    ENDIF.

    result = ydkmsg=>message_to_str( msg ).
  ENDMETHOD.
ENDCLASS.