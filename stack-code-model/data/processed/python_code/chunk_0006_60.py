class ZCX_IDOC_PREPROCESS_ERROR definition
  public
  inheriting from CX_STATIC_CHECK
  final
  create public .

public section.

*"* public components of class ZCX_IDOC_PREPROCESS_ERROR
*"* do not include other source files here!!!
  constants ZCX_IDOC_PREPROCESS_ERROR type SOTR_CONC value '00505697691A1ED98BBA9D424302851D' ##NO_TEXT.

  methods CONSTRUCTOR
    importing
      !TEXTID like TEXTID optional
      !PREVIOUS like PREVIOUS optional .
protected section.
*"* protected components of class ZCX_IDOC_PREPROCESS_ERROR
*"* do not include other source files here!!!
private section.
*"* private components of class ZCX_IDOC_PREPROCESS_ERROR
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCX_IDOC_PREPROCESS_ERROR IMPLEMENTATION.


  method CONSTRUCTOR.
CALL METHOD SUPER->CONSTRUCTOR
EXPORTING
TEXTID = TEXTID
PREVIOUS = PREVIOUS
.
 IF textid IS INITIAL.
   me->textid = ZCX_IDOC_PREPROCESS_ERROR .
 ENDIF.
  endmethod.
ENDCLASS.