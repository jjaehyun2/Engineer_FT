class ZCL_ABAPGITDEMO definition
  public
  create public .

public section.

  class-methods ADD_NUMBERS
    importing
      !I_A type I
      !I_B type I
    returning
      value(R_C) type I .
protected section.
private section.
ENDCLASS.



CLASS ZCL_ABAPGITDEMO IMPLEMENTATION.


  METHOD add_numbers.
    r_c = i_a + i_b.
  ENDMETHOD.
ENDCLASS.