*"* use this source file for your ABAP unit test classes
CLASS lcl_unittest DEFINITION FOR TESTING
  INHERITING FROM zcl_abak_unit_tests
  DURATION SHORT
  RISK LEVEL HARMLESS
  FINAL.

  PRIVATE SECTION.

    DATA:
      f_cut TYPE REF TO zcl_abak_data_shm.  "class under test

    METHODS: setup RAISING zcx_abak.
    METHODS: read_valid FOR TESTING RAISING zcx_abak.
    METHODS: get_name FOR TESTING RAISING zcx_abak.
*    METHODS: invalidate FOR TESTING RAISING zcx_abak.
ENDCLASS.       "lcl_Unittest


CLASS lcl_unittest IMPLEMENTATION.

  METHOD setup.
    generate_test_data( ).

    CREATE OBJECT f_cut
      EXPORTING
        i_format_type = zif_abak_consts=>format_type-database
        i_content_type = zif_abak_consts=>content_type-inline
        i_param = gc_tablename-valid.

  ENDMETHOD.

  METHOD read_valid.

    cl_abap_unit_assert=>assert_differs(
      exp = 0
      act = lines( f_cut->zif_abak_data~read( i_scope     = 'UTEST'
                                              i_fieldname = 'BUKRS'
                                              i_context   = space ) )
      msg = 'Resulting table should not be empty' ).

  ENDMETHOD.

  METHOD get_name.

    cl_abap_unit_assert=>assert_equals(
      exp = gc_tablename-valid
      act = f_cut->zif_abak_data~get_name( )
      msg = 'Name different from what was expected' ).

  ENDMETHOD.

*  METHOD invalidate.
*
*    DATA: o_data TYPE REF TO zcl_abak_data.
*
*    f_cut->zif_abak_data~read( i_scope     = 'UTEST'
*                               i_fieldname = 'BUKRS'
*                               i_context   = space ).
*
*    cl_abap_unit_assert=>assert_differs(
*      exp = 0
*      act = lines( f_cut->gt_k )
*      msg = 'Resulting table should have more than one line' ).
*
*    f_cut->zif_abak_data~invalidate( ).
*
*    o_data = f_cut.
*
*    cl_abap_unit_assert=>assert_equals(
*      exp = 0
*      act = lines( o_data->gt_k )
*      msg = 'Resulting table should have ZERO lines' ).
*
*  ENDMETHOD.

ENDCLASS.       "lcl_Unittest