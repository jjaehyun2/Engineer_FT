class ZCA_ZAVE_STUDENT_P definition
  public
  inheriting from ZCB_ZAVE_STUDENT_P
  final
  create private .

public section.

  class-data AGENT type ref to ZCA_ZAVE_STUDENT_P read-only .

  class-methods CLASS_CONSTRUCTOR .
protected section.
private section.
ENDCLASS.



CLASS ZCA_ZAVE_STUDENT_P IMPLEMENTATION.


  method CLASS_CONSTRUCTOR.
***BUILD 090501
************************************************************************
* Purpose        : Initialize the 'class'.
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : Singleton is created.
*
* OO Exceptions  : -
*
* Implementation : -
*
************************************************************************
* Changelog:
* - 1999-09-20   : (OS) Initial Version
* - 2000-03-06   : (BGR) 2.0 modified REGISTER_CLASS_AGENT
************************************************************************
* GENERATED: Do not modify
************************************************************************

  create object AGENT.

  call method AGENT->REGISTER_CLASS_AGENT
    exporting
      I_CLASS_NAME          = 'ZCL_ZAVE_STUDENT_P'
      I_CLASS_AGENT_NAME    = 'ZCA_ZAVE_STUDENT_P'
      I_CLASS_GUID          = '00505692515B1ED892A8D094BF05B98E'
      I_CLASS_AGENT_GUID    = '00505692515B1ED892A8D0AE1BEFF98E'
      I_AGENT               = AGENT
      I_STORAGE_LOCATION    = 'ZAVE_FPM_STUD'
      I_CLASS_AGENT_VERSION = '2.0'.

           "CLASS_CONSTRUCTOR
  endmethod.
ENDCLASS.