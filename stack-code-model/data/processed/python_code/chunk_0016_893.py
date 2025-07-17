class ZCL_ZPT_C_TASK definition
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



CLASS ZCL_ZPT_C_TASK IMPLEMENTATION.


  method GET_PATHS.
et_paths = VALUE #(
( |CDS~ZPT_C_TASK| )
).
  endmethod.


  method GET_TIMESTAMP.
RV_TIMESTAMP = 20200927093502.
  endmethod.
ENDCLASS.