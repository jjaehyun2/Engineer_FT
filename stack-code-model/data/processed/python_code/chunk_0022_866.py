class ZCL_ZPT_C_PROJECT definition
  public
  inheriting from CL_SADL_GTK_EXPOSURE_MPC
  final
  create public .

public section.
protected section.

  methods GET_PATHS
    redefinition .
  methods GET_TIMESTAMP
    redefinition .
private section.
ENDCLASS.



CLASS ZCL_ZPT_C_PROJECT IMPLEMENTATION.


  method GET_PATHS.
et_paths = VALUE #(
( |CDS~ZPT_C_PROJECT| )
).
  endmethod.


  method GET_TIMESTAMP.
RV_TIMESTAMP = 20200927033351.
  endmethod.
ENDCLASS.