class ZCA_BUG_TAG_PERSIST definition
  public
  inheriting from ZCB_BUG_TAG_PERSIST
  final
  create private .

public section.
*"* public components of class ZCA_BUG_TAG_PERSIST
*"* do not include other source files here!!!

  class-data AGENT type ref to ZCA_BUG_TAG_PERSIST read-only .

  class-methods CLASS_CONSTRUCTOR .
protected section.
*"* protected components of class ZCA_BUG_TAG_PERSIST
*"* do not include other source files here!!!
private section.
*"* private components of class ZCA_BUG_TAG_PERSIST
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCA_BUG_TAG_PERSIST IMPLEMENTATION.


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
      I_CLASS_NAME          = 'ZCL_BUG_TAG_PERSIST'
      I_CLASS_AGENT_NAME    = 'ZCA_BUG_TAG_PERSIST'
      I_CLASS_GUID          = '080027EE3DEB1ED0A8D2DFEF7F376FA3'
      I_CLASS_AGENT_GUID    = '080027EE3DEB1ED0A8D2DFEF7F38EFA3'
      I_AGENT               = AGENT
      I_STORAGE_LOCATION    = 'ZBT_BUG_TAG'
      I_CLASS_AGENT_VERSION = '2.0'.

           "CLASS_CONSTRUCTOR
endmethod.
ENDCLASS.