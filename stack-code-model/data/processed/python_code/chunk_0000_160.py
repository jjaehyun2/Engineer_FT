class ZCX_CREDIT_CALCULATOR definition
  public
  inheriting from CX_SADL_EXIT
  final
  create public .

public section.

  constants ENTITY_NOT_SUPPORTED type SOTR_CONC value '39AC48DD21231EEA84F2040017B744C4' ##NO_TEXT.
  constants FILTER_ELEMENT_WRONG type SOTR_CONC value '39AC48DD21231EEA86B273B3B726CF52' ##NO_TEXT.

  methods CONSTRUCTOR
    importing
      !TEXTID like TEXTID optional
      !PREVIOUS type ref to CX_ROOT optional .
  PROTECTED SECTION.
  PRIVATE SECTION.
ENDCLASS.



CLASS ZCX_CREDIT_CALCULATOR IMPLEMENTATION.


  METHOD constructor ##ADT_SUPPRESS_GENERATION.
    CALL METHOD super->constructor
      EXPORTING
        textid   = textid
        previous = previous.
  ENDMETHOD.
ENDCLASS.