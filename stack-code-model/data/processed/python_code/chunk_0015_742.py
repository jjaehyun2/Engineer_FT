class ZCA_ABAPGIT_TESTING_PERSISTENC definition
  public
  inheriting from ZCB_ABAPGIT_TESTING_PERSISTENC
  final
  create private .

public section.

  class-data AGENT type ref to ZCA_ABAPGIT_TESTING_PERSISTENC read-only .

  class-methods CLASS_CONSTRUCTOR .
protected section.
private section.
ENDCLASS.



CLASS ZCA_ABAPGIT_TESTING_PERSISTENC IMPLEMENTATION.


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
      I_CLASS_NAME          = 'ZCL_ABAPGIT_TESTING_PERSISTENC'
      I_CLASS_AGENT_NAME    = 'ZCA_ABAPGIT_TESTING_PERSISTENC'
      I_CLASS_GUID          = '02FBA84C29D01ED980DD66A95EA2DABB'
      I_CLASS_AGENT_GUID    = '02FBA84C29D01ED980DD66CABF2E9AC0'
      I_AGENT               = AGENT
      I_STORAGE_LOCATION    = 'ZABAPGIT_TST_CLP'
      I_CLASS_AGENT_VERSION = '2.0'.

           "CLASS_CONSTRUCTOR
  endmethod.
ENDCLASS.