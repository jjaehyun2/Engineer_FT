class ZCA_TRANSPORT_PERSIST definition
  public
  inheriting from ZCB_TRANSPORT_PERSIST
  final
  create private .

*"* public components of class ZCA_TRANSPORT_PERSIST
*"* do not include other source files here!!!
public section.

  class-data AGENT type ref to ZCA_TRANSPORT_PERSIST read-only .

  class-methods CLASS_CONSTRUCTOR .
protected section.
*"* protected components of class ZCA_TRANSPORT_PERSIST
*"* do not include other source files here!!!
private section.
*"* private components of class ZCA_TRANSPORT_PERSIST
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCA_TRANSPORT_PERSIST IMPLEMENTATION.


method CLASS_CONSTRUCTOR.
***BUILD 051401
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
      I_CLASS_NAME          = 'ZCL_TRANSPORT_PERSIST'
      I_CLASS_AGENT_NAME    = 'ZCA_TRANSPORT_PERSIST'
      I_CLASS_GUID          = 'DF3C439AA02015F19291080027E6C24E'
      I_CLASS_AGENT_GUID    = 'DF3C439AA02021F19291080027E6C24E'
      I_AGENT               = AGENT
      I_STORAGE_LOCATION    = 'ZBT_TRANSPORTER'
      I_CLASS_AGENT_VERSION = '2.0'.

           "CLASS_CONSTRUCTOR
endmethod.
ENDCLASS.