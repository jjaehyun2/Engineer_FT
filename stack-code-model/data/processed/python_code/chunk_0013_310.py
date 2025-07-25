*----------------------------------------------------------------------*
*       CLASS lcl_Test DEFINITION
*----------------------------------------------------------------------*
*
*----------------------------------------------------------------------*
CLASS ltcl_test DEFINITION FOR TESTING DURATION SHORT RISK LEVEL HARMLESS FINAL.

  PRIVATE SECTION.
* ================

    DATA: mt_code   TYPE string_table,
          ms_result TYPE scirest_ad,
          mo_check  TYPE REF TO zcl_aoc_check_82.

    METHODS:
      setup,
      export_import FOR TESTING,
      test001_01    FOR TESTING,
      test001_02    FOR TESTING,
      test001_03    FOR TESTING.

ENDCLASS.       "lcl_Test

*----------------------------------------------------------------------*
*       CLASS lcl_Test IMPLEMENTATION
*----------------------------------------------------------------------*
*
*----------------------------------------------------------------------*
CLASS ltcl_test IMPLEMENTATION.
* ==============================

  METHOD setup.
    CREATE OBJECT mo_check.
    zcl_aoc_unit_test=>set_check( mo_check ).
  ENDMETHOD.

  METHOD export_import.
    zcl_aoc_unit_test=>export_import( mo_check ).
  ENDMETHOD.

  METHOD test001_01.

    APPEND 'WRITE "#EC FOOBAR' TO mt_code.
    APPEND 'moo.' TO mt_code.

    ms_result = zcl_aoc_unit_test=>check( mt_code ).

    cl_abap_unit_assert=>assert_equals( exp = '001'
                                        act = ms_result-code ).

  ENDMETHOD.

  METHOD test001_02.

    APPEND 'WRITE moo.' TO mt_code.

    ms_result = zcl_aoc_unit_test=>check( mt_code ).

    cl_abap_unit_assert=>assert_initial( ms_result-code ).

  ENDMETHOD.

  METHOD test001_03.

    APPEND 'WRITE moo. "#EC FOOBAR' TO mt_code.

    ms_result = zcl_aoc_unit_test=>check( mt_code ).

    cl_abap_unit_assert=>assert_initial( ms_result-code ).

  ENDMETHOD.

ENDCLASS.