class ZCL_AOT_UUID definition
  public
  create public .

public section.

  class-methods CREATE
    returning
      value(RV_UUID) type SYSUUID_X16 .
protected section.
private section.
ENDCLASS.



CLASS ZCL_AOT_UUID IMPLEMENTATION.


  METHOD create.

    TRY.
        rv_uuid = cl_system_uuid=>create_uuid_x16_static( ).
      CATCH cx_uuid_error.
        ASSERT 0 = 1.
    ENDTRY.

  ENDMETHOD.
ENDCLASS.