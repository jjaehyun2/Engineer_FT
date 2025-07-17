CLASS lcl_test1 DEFINITION FOR TESTING
  DURATION SHORT
  RISK LEVEL HARMLESS
.
*?﻿<asx:abap xmlns:asx="http://www.sap.com/abapxml" version="1.0">
*?<asx:values>
*?<TESTCLASS_OPTIONS>
*?<TEST_CLASS>lcl_Test1
*?</TEST_CLASS>
*?<TEST_MEMBER>f_Cut
*?</TEST_MEMBER>
*?<OBJECT_UNDER_TEST>ZCL_DOJO_WILDCARD
*?</OBJECT_UNDER_TEST>
*?<OBJECT_IS_LOCAL/>
*?<GENERATE_FIXTURE>X
*?</GENERATE_FIXTURE>
*?<GENERATE_CLASS_FIXTURE/>
*?<GENERATE_INVOCATION/>
*?<GENERATE_ASSERT_EQUAL>X
*?</GENERATE_ASSERT_EQUAL>
*?</TESTCLASS_OPTIONS>
*?</asx:values>
*?</asx:abap>
  PRIVATE SECTION.
    DATA:
      f_cut TYPE REF TO zcl_dojo_wildcard.  "class under test

    METHODS: setup.
    METHODS: check FOR TESTING.
    METHODS: check_exact FOR TESTING.
    METHODS: check_neg FOR TESTING.
ENDCLASS.       "lcl_Test1


CLASS lcl_test1 IMPLEMENTATION.

  METHOD setup.


    CREATE OBJECT f_cut.
    f_cut->mt_wildcards = VALUE #(
    ( varbpl = 'A*' narbpl = 'A*' )
    ( varbpl = 'A200' narbpl = 'A200' )
    ).
  ENDMETHOD.



  METHOD check.
    DATA(ls_result) = f_cut->check( iv_varbpl = 'A300' iv_narbpl = 'A300' ).

    cl_abap_unit_assert=>assert_equals(
      act   = ls_result-varbpl
      exp   = 'A*'
    ).

    cl_abap_unit_assert=>assert_equals(
      act   = ls_result-narbpl
      exp   = 'A*'
    ).
  ENDMETHOD.


  METHOD check_exact.
    DATA(ls_result) = f_cut->check( iv_varbpl = 'A200' iv_narbpl = 'A200' ).

    cl_abap_unit_assert=>assert_equals(
      act   = ls_result-varbpl
      exp   = 'A200'
    ).

    cl_abap_unit_assert=>assert_equals(
      act   = ls_result-narbpl
      exp   = 'A200'
    ).
  ENDMETHOD.

  METHOD check_neg.
    DATA(ls_result) = f_cut->check( iv_varbpl = 'B1' iv_narbpl = 'A200' ).

    cl_abap_unit_assert=>assert_equals(
      act   = ls_result-varbpl
      exp   = ''
    ).

    cl_abap_unit_assert=>assert_equals(
      act   = ls_result-narbpl
      exp   = ''
    ).


  ENDMETHOD.



ENDCLASS.


CLASS lcl_test2 DEFINITION FOR TESTING
  DURATION SHORT
  RISK LEVEL HARMLESS
.

  PRIVATE SECTION.
    DATA:
      f_cut TYPE REF TO zcl_dojo_wildcard.  "class under test

    METHODS: setup.
    METHODS: check0 FOR TESTING.
    METHODS: check FOR TESTING.
    METHODS: check2 FOR TESTING.
    METHODS: check3 FOR TESTING.
ENDCLASS.       "lcl_Test1


CLASS lcl_test2 IMPLEMENTATION.

  METHOD setup.
    CREATE OBJECT f_cut.
    f_cut->mt_wildcards = VALUE #(
    ( varbpl = 'B*' narbpl = 'B300' )
    ( varbpl = 'B300' narbpl = 'B*' )
    ( varbpl = 'B3*' narbpl = 'B300' )
    ).

  ENDMETHOD.

  METHOD check0.
    DATA(ls_result) = f_cut->check( iv_varbpl = 'B500' iv_narbpl = 'B300' ).

    cl_abap_unit_assert=>assert_equals(
      act   = ls_result-varbpl
      exp   = 'B*'
    ).

    cl_abap_unit_assert=>assert_equals(
      act   = ls_result-narbpl
      exp   = 'B300'
    ).
  ENDMETHOD.


  METHOD check.
    DATA(ls_result) = f_cut->check( iv_varbpl = 'B300' iv_narbpl = 'B300' ).

    cl_abap_unit_assert=>assert_equals(
      act   = ls_result-varbpl
      exp   = 'B3*'
    ).

    cl_abap_unit_assert=>assert_equals(
      act   = ls_result-narbpl
      exp   = 'B300'
    ).
  ENDMETHOD.


  METHOD check2.
    DATA(ls_result) = f_cut->check( iv_varbpl = 'B300' iv_narbpl = 'B' ).

    cl_abap_unit_assert=>assert_equals(
      act   = ls_result-varbpl
      exp   = 'B300'
    ).

    cl_abap_unit_assert=>assert_equals(
      act   = ls_result-narbpl
      exp   = 'B*'
    ).
  ENDMETHOD.

  METHOD check3.
    DATA(ls_result) = f_cut->check( iv_varbpl = 'B330' iv_narbpl = 'B300' ).

    cl_abap_unit_assert=>assert_equals(
      act   = ls_result-varbpl
      exp   = 'B3*'
    ).
    cl_abap_unit_assert=>assert_equals(
      act   = ls_result-narbpl
      exp   = 'B300'
    ).
  ENDMETHOD.

ENDCLASS.