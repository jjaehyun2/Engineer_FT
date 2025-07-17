class ZCL_PT_A_CREATE_TR_CU definition
  public
  inheriting from ZCL_PT_A_TASK_CREATE_TR
  final
  create public .

public section.
protected section.

  methods GET_TR_TYPE
    redefinition .
private section.
ENDCLASS.



CLASS ZCL_PT_A_CREATE_TR_CU IMPLEMENTATION.


  method GET_TR_TYPE.

    type = 'W'.

  endmethod.
ENDCLASS.