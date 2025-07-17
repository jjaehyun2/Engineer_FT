class ZCX_PROXY_PROCESS_ERROR definition
  public
  inheriting from CX_STATIC_CHECK
  final
  create public .

public section.
*"* public components of class ZCX_PROXY_PROCESS_ERROR
*"* do not include other source files here!!!

  constants ZCX_PROXY_PROCESS_ERROR type SOTR_CONC value '5345E4A869E00D40E10080000AD00C21'. "#EC NOTEXT
  data ERROR_CAT type ECH_DTE_ERROR_CATEGORY .
  data OBJTYPE type ECH_DTE_OBJTYPE .
  data OBJKEY type STRING .
  data PRE_MAPPING type FEH_BOOLEAN .

  methods CONSTRUCTOR
    importing
      !TEXTID like TEXTID optional
      !PREVIOUS like PREVIOUS optional
      !ERROR_CAT type ECH_DTE_ERROR_CATEGORY optional
      !OBJTYPE type ECH_DTE_OBJTYPE optional
      !OBJKEY type STRING optional
      !PRE_MAPPING type FEH_BOOLEAN optional .
protected section.
*"* protected components of class ZCX_PROXY_PROCESS_ERROR
*"* do not include other source files here!!!
private section.
*"* private components of class ZCX_PROXY_PROCESS_ERROR
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCX_PROXY_PROCESS_ERROR IMPLEMENTATION.


method CONSTRUCTOR.
CALL METHOD SUPER->CONSTRUCTOR
EXPORTING
TEXTID = TEXTID
PREVIOUS = PREVIOUS
.
 IF textid IS INITIAL.
   me->textid = ZCX_PROXY_PROCESS_ERROR .
 ENDIF.
me->ERROR_CAT = ERROR_CAT .
me->OBJTYPE = OBJTYPE .
me->OBJKEY = OBJKEY .
me->PRE_MAPPING = PRE_MAPPING .
endmethod.
ENDCLASS.