class ZCL_COLOR_PROTOTYPE definition
  public
  abstract
  create public .

public section.

  methods CLONE
    returning
      value(RO_PROTOTYPE) type ref to ZCL_COLOR_PROTOTYPE .
protected section.
private section.
ENDCLASS.



CLASS ZCL_COLOR_PROTOTYPE IMPLEMENTATION.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_COLOR_PROTOTYPE->CLONE
* +-------------------------------------------------------------------------------------------------+
* | [<-()] RO_PROTOTYPE                   TYPE REF TO ZCL_COLOR_PROTOTYPE
* +--------------------------------------------------------------------------------------</SIGNATURE>
  method CLONE.
  endmethod.
ENDCLASS.