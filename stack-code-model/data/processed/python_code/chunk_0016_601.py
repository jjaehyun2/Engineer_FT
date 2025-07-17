*"* use this source file for your ABAP unit test classes
class ltcl_test_user definition final for testing
  duration short
  risk level harmless.

  private section.
    methods:
      first_test for testing raising cx_static_check.
endclass.


class ltcl_test_user implementation.


  method first_test.

  "given
  data(cut) = new Z_CL_I338058(   ).

  "when
  cut->get_user( importing ev_user = data(lv_user) ).

  "then
  cl_abap_unit_assert=>assert_equals( act = lv_user
  exp = sy-uname ).

  "cl_abap_unit_assert=>fail( 'Implement your first test here' ).
  endmethod.

endclass.