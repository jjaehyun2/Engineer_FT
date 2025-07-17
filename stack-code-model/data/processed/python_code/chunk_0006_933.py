*"* use this source file for your ABAP unit test classes
class ltcl_zellen definition final for testing
  duration short
  risk level harmless.

  private section.
    DATA: mv_feld TYPE zcl_gol_15=>ty_feld.
    methods:
      zelle_0_nb_stirbt for testing raising cx_static_check.
endclass.


class ltcl_zellen implementation.

  method zelle_0_nb_stirbt.
    DATA: zeile  TYPE zcl_gol_15=>ty_zeile.
          zeile =  value #(   ( abap_false )  ( abap_false )  ( abap_false )  ) .
     mv_feld = value #( (  zeile ) ( zeile ) ( zeile ) ).
  endmethod.

endclass.