class ltc_encode definition final for testing
  duration short
  risk level harmless.

  private section.
    data cut type ref to zcl_rle.

    methods setup.

    methods empty_string for testing raising cx_static_check.
    methods no_repeat    for testing raising cx_static_check.
    methods no_singles   for testing raising cx_static_check.
    methods mixed_singles_and_repeats for testing raising cx_static_check.
    methods mixed_and_spaces for testing raising cx_static_check.
    methods lowercase        for testing raising cx_static_check.
endclass.


class ltc_encode implementation.

  method setup.
    cut = new zcl_rle( ).
  endmethod.

  method empty_string.
    cl_abap_unit_assert=>assert_equals( act = cut->encode( `` )
                                        exp = `` ).
  endmethod.

  method no_repeat.
    cl_abap_unit_assert=>assert_equals( act = cut->encode( `XYZ` )
                                        exp = `XYZ` ).
  endmethod.

  method no_singles.
    cl_abap_unit_assert=>assert_equals( act = cut->encode( `AABBBCCCC` )
                                        exp = `2A3B4C` ).
  endmethod.

  method mixed_singles_and_repeats.
    cl_abap_unit_assert=>assert_equals( act = cut->encode( `WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB` )
                                        exp = `12WB12W3B24WB` ).
  endmethod.

  method mixed_and_spaces.
    cl_abap_unit_assert=>assert_equals( act = cut->encode( `  hsqq qww  ` )
                                        exp = `2 hs2q q2w2 ` ).
  endmethod.

  method lowercase.
    cl_abap_unit_assert=>assert_equals( act = cut->encode( `aabbbcccc` )
                                        exp = `2a3b4c` ).
  endmethod.

endclass.


class ltc_decode definition final for testing
  duration short
  risk level harmless.

  private section.
    data cut type ref to zcl_rle.

    methods setup.

    methods empty_string for testing raising cx_static_check.
    methods no_repeat    for testing raising cx_static_check.
    methods no_singles   for testing raising cx_static_check.
    methods mixed_singles_and_repeats for testing raising cx_static_check.
    methods mixed_and_spaces for testing raising cx_static_check.
    methods lowercase        for testing raising cx_static_check.
    methods encode_and_decode for testing raising cx_static_check.
endclass.


class ltc_decode implementation.

  method setup.
    cut = new zcl_rle( ).
  endmethod.

  method empty_string.
    cl_abap_unit_assert=>assert_equals( act = cut->decode( `` )
                                        exp = `` ).
  endmethod.

  method no_repeat.
    cl_abap_unit_assert=>assert_equals( act = cut->decode( `XYZ` )
                                        exp = `XYZ` ).
  endmethod.

  method no_singles.
    cl_abap_unit_assert=>assert_equals( act = cut->decode( `2A3B4C` )
                                        exp = `AABBBCCCC` ).
  endmethod.

  method mixed_singles_and_repeats.
    cl_abap_unit_assert=>assert_equals( act = cut->decode( `12WB12W3B24WB` )
                                        exp = `WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB` ).
  endmethod.

  method mixed_and_spaces.
    cl_abap_unit_assert=>assert_equals( act = cut->decode( `2 hs2q q2w2 ` )
                                        exp = `  hsqq qww  ` ).
  endmethod.

  method lowercase.
    cl_abap_unit_assert=>assert_equals( act = cut->decode( `2a3b4c` )
                                        exp = `aabbbcccc` ).
  endmethod.

  method encode_and_decode.
    cl_abap_unit_assert=>assert_equals( act = cut->decode( cut->encode( `zzz ZZ  zZ` ) )
                                        exp = `zzz ZZ  zZ` ).
  endmethod.

endclass.