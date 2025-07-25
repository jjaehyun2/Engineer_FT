class ZCX_SAPLINK definition
  public
  inheriting from CX_STATIC_CHECK
  create public .

public section.

  constants ERROR_MESSAGE type SOTR_CONC value '000D3A39AB551EE8B8B7ED4A1DA1119E' ##NO_TEXT.
  constants EXISTING type SOTR_CONC value '000D3A39AB551EE8B8B7ED4A1DA1319E' ##NO_TEXT.
  constants INCORRECT_FILE_FORMAT type SOTR_CONC value '000D3A39AB551EE8B8B7ED4A1DA1519E' ##NO_TEXT.
  constants LOCKED type SOTR_CONC value '000D3A39AB551EE8B8B7ED4A1DA1719E' ##NO_TEXT.
  data MSG type STRING value '44F7518323DB08BC02000000A7E42BB6' ##NO_TEXT.
  constants NOT_AUTHORIZED type SOTR_CONC value '000D3A39AB551EE8B8B7ED4A1DA1919E' ##NO_TEXT.
  constants NOT_FOUND type SOTR_CONC value '000D3A39AB551EE8B8B7ED4A1DA1B19E' ##NO_TEXT.
  constants NO_PLUGIN type SOTR_CONC value '000D3A39AB551EE8B8B7ED4A1DA1D19E' ##NO_TEXT.
  constants SYSTEM_ERROR type SOTR_CONC value '000D3A39AB551EE8B8B7ED4A1DA1F19E' ##NO_TEXT.
  constants ZCX_SAPLINK type SOTR_CONC value '000D3A39AB551EE8B8B7ED4A1DA2119E' ##NO_TEXT.
  data OBJECT type STRING .

  methods CONSTRUCTOR
    importing
      !TEXTID like TEXTID optional
      !PREVIOUS like PREVIOUS optional
      !MSG type STRING default '44F7518323DB08BC02000000A7E42BB6'
      !OBJECT type STRING optional .
protected section.
private section.
ENDCLASS.



CLASS ZCX_SAPLINK IMPLEMENTATION.


  method CONSTRUCTOR.
CALL METHOD SUPER->CONSTRUCTOR
EXPORTING
TEXTID = TEXTID
PREVIOUS = PREVIOUS
.
 IF textid IS INITIAL.
   me->textid = ZCX_SAPLINK .
 ENDIF.
me->MSG = MSG .
me->OBJECT = OBJECT .
  endmethod.
ENDCLASS.