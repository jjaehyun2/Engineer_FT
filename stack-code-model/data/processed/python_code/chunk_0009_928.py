class ZCL_A_LOCK_BC_DDL_REQUEST definition
  public
  inheriting from /BOBF/CL_LIB_A_LOCK_ACTIVE
  final
  create public .

public section.

  methods /BOBF/IF_LIB_LOCK_ACTIVE~LOCK_ACTIVE_ENTITY
    redefinition .
protected section.
private section.
ENDCLASS.



CLASS ZCL_A_LOCK_BC_DDL_REQUEST IMPLEMENTATION.


  method /BOBF/IF_LIB_LOCK_ACTIVE~LOCK_ACTIVE_ENTITY.
  endmethod.
ENDCLASS.