class ZCX_ABAPGIT_TEST_SOTR definition
  public
  inheriting from CX_STATIC_CHECK
  create private .

public section.

  constants ZCX_ABAPGIT_TEST_SOTR type SOTR_CONC value '0242AC1100021ED986CD12D229594C49' ##NO_TEXT.

  methods CONSTRUCTOR
    importing
      !TEXTID like TEXTID optional
      !PREVIOUS like PREVIOUS optional .
protected section.
private section.
ENDCLASS.



CLASS ZCX_ABAPGIT_TEST_SOTR IMPLEMENTATION.


  method CONSTRUCTOR.
CALL METHOD SUPER->CONSTRUCTOR
EXPORTING
TEXTID = TEXTID
PREVIOUS = PREVIOUS
.
 IF textid IS INITIAL.
   me->textid = ZCX_ABAPGIT_TEST_SOTR .
 ENDIF.
  endmethod.
ENDCLASS.