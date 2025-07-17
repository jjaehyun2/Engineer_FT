class ZALGOR_CL_LISTNODE definition
  public
  final
  create public .

public section.

  interfaces IF_SERIALIZABLE_OBJECT .

  data VAL type ZALGOR_INT4 .
  data NEXT type ref to ZALGOR_CL_LISTNODE .

  methods CONSTRUCTOR
    importing
      !IV_VAL type ZALGOR_INT4 .
protected section.
private section.
ENDCLASS.



CLASS ZALGOR_CL_LISTNODE IMPLEMENTATION.


  METHOD constructor.
    me->val = iv_val.
  ENDMETHOD.
ENDCLASS.