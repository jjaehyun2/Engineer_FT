class ZCX_BOOK_EXCEPTION definition
  public
  inheriting from CX_STATIC_CHECK
  create public .

public section.

  constants WRONG_ORDER type SOTR_CONC value '005056A7624D1ED5BED5F65B4D0F0D40' ##NO_TEXT.
  constants TICKET_DOES_NOT_EXIST type SOTR_CONC value '005056A7624D1ED5BED5FED93EF4CD47' ##NO_TEXT.
  constants ZCX_BOOK_EXCEPTION type SOTR_CONC value '005056A7624D1ED68CC3527DA7B64C9E' ##NO_TEXT.
  data TIKNR type ZBOOK_TICKET_NR .

  methods CONSTRUCTOR
    importing
      !TEXTID like TEXTID optional
      !PREVIOUS like PREVIOUS optional
      !TIKNR type ZBOOK_TICKET_NR optional .
protected section.
private section.
ENDCLASS.



CLASS ZCX_BOOK_EXCEPTION IMPLEMENTATION.


  method CONSTRUCTOR.
CALL METHOD SUPER->CONSTRUCTOR
EXPORTING
TEXTID = TEXTID
PREVIOUS = PREVIOUS
.
 IF textid IS INITIAL.
   me->textid = ZCX_BOOK_EXCEPTION .
 ENDIF.
me->TIKNR = TIKNR .
  endmethod.
ENDCLASS.