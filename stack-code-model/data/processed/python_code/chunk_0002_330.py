class ZCL_AOT_RUN definition
  public
  create private .

public section.

  class-methods CREATE
    importing
      !IO_PROJECT type ref to ZCL_AOT_PROJECT
    returning
      value(RO_RUN) type ref to ZCL_AOT_RUN .
  class-methods GET_INSTANCE
    importing
      !IV_RUN_ID type ZAOT_RUN_ID
    returning
      value(RO_RUN) type ref to ZCL_AOT_RUN .
  class-methods LOOKUP
    importing
      !IV_PROJECT type ZAOT_PROJECT_NAME
      !IV_RUN_NAME type ZAOT_RUN_NAME
    returning
      value(RO_RUN) type ref to ZCL_AOT_RUN .
  methods APPEND_COVERAGE
    importing
      !II_NODE type ref to IF_SCV_RESULT_NODE
      !II_RESULT type ref to IF_SCV_RESULT
      !IV_CLASS type TADIR-OBJ_NAME .
  methods APPEND_OBJECT
    importing
      !IS_OBJECT type ZAOT_OBJECTS .
  methods APPEND_TEST
    importing
      !IS_TEST type ZAOT_TESTS .
  methods GET_BLOCKS
    returning
      value(RT_BLOCKS) type ZAOT_CBLOCKS_TT .
  methods GET_COVERAGE
    returning
      value(RT_COVERAGE) type ZAOT_COVERAGE_TT .
  methods GET_DETAILS
    returning
      value(RS_RUN) type ZAOT_RUNS .
  methods GET_OBJECTS
    returning
      value(RT_OBJECTS) type ZAOT_OBJECTS_TT .
  methods GET_TESTS
    returning
      value(RT_TESTS) type ZAOT_TESTS_TT .
  methods SAVE .
  methods SET_END_TIME .
  methods SET_START_TIME .
protected section.
private section.

  data MS_RUN type ZAOT_RUNS .
  data MT_TESTS type ZAOT_TESTS_TT .
  data MT_OBJECTS type ZAOT_OBJECTS_TT .
  data MT_BLOCKS type ZAOT_CBLOCKS_TT .
  data MT_COVERAGE type ZAOT_COVERAGE_TT .

  methods GET_CONTAINER
    importing
      !IO_INSP type ref to CL_SCV_PBLOCK_INSPECTOR
      !II_RESULT type ref to IF_SCV_RESULT
    returning
      value(RI_CONTAINER) type ref to IF_SCOV_STMNT_DATA_CONTAINER .
ENDCLASS.



CLASS ZCL_AOT_RUN IMPLEMENTATION.


  METHOD append_coverage.

    DATA: ls_block TYPE zaot_cblocks_data.

*    DATA(lv_executed) = ii_node->get_coverage( ce_scv_coverage_type=>statement )->get_executed( ).

    CASE ii_node->subtype.
      WHEN 'METH'.
        DATA(lo_insp) = cl_scv_pblock_inspector=>create( ii_node ).
        ls_block-pb_type    = 'METH'.
        ls_block-pb_name    = lo_insp->get_method_name( ).
        ls_block-prog_class = lo_insp->get_class_name( ).
        ls_block-class_sub  = lo_insp->get_class_subtype( ).
        ls_block-prog_type  = lo_insp->get_program_subtype( ).
        ls_block-prog_name  = lo_insp->get_program_name( ).

        IF ls_block-class_sub = 'LOCL'.
* todo
          RETURN.
        ENDIF.
      WHEN OTHERS.
* todo
        RETURN.
    ENDCASE.

    DATA(li_container) = get_container(
      io_insp   = lo_insp
      ii_result = ii_result ).

* TODO: sorted table?
    READ TABLE mt_blocks ASSIGNING FIELD-SYMBOL(<ls_result>)
      WITH KEY
      pb_type = ls_block-pb_type
      pb_name = ls_block-pb_name
      prog_class = ls_block-prog_class
      class_sub = ls_block-class_sub
      prog_type = ls_block-prog_type
      prog_name = ls_block-prog_name.
    IF sy-subrc <> 0.
      DATA(lv_source) = concat_lines_of( table = li_container->get_source( ) sep = |\n| ).
      DATA(lv_cblock_id) = zcl_aot_uuid=>create( ).

      INSERT VALUE #(
        run_id     = ms_run-run_id
        cblock_id  = lv_cblock_id
        pb_type    = ls_block-pb_type
        pb_name    = ls_block-pb_name
        prog_class = ls_block-prog_class
        class_sub  = ls_block-class_sub
        prog_type  = ls_block-prog_type
        prog_name  = ls_block-prog_name
        source     = lv_source )
        INTO TABLE mt_blocks ASSIGNING <ls_result>.
    ELSE.
      lv_cblock_id = <ls_result>-cblock_id.
    ENDIF.

    IF ii_node->get_coverage( ce_scv_coverage_type=>statement )->get_executed( ) > 0.
      LOOP AT li_container->get_stmnt_cov_meta_data( ) INTO DATA(ls_cov).
        APPEND VALUE #(
          cblock_id    = lv_cblock_id
          program_name = '' " TODO
          class_name   = iv_class
          method_name  = '' " TODO
          counter      = sy-tabix
          rowcov       = ls_cov-row
          colcov       = ls_cov-col
          colorcov     = ls_cov-color
          iconcov      = ls_cov-icon )
          TO mt_coverage.
      ENDLOOP.
    ENDIF.

  ENDMETHOD.


  METHOD append_object.

    ASSERT is_object-run_id IS INITIAL.
    ASSERT NOT is_object-object_name IS INITIAL.
    ASSERT NOT is_object-object_type IS INITIAL.

    DATA(ls_object) = is_object.
    ls_object-run_id = ms_run-run_id.

    APPEND ls_object TO mt_objects.

  ENDMETHOD.


  METHOD append_test.

    ASSERT NOT is_test-program_name IS INITIAL.
    ASSERT NOT is_test-class_name IS INITIAL.
    ASSERT NOT is_test-method_name IS INITIAL.
    ASSERT NOT is_test-object_name IS INITIAL.
    ASSERT NOT is_test-object_type IS INITIAL.

    DATA(ls_test) = is_test.
    ls_test-run_id = ms_run-run_id.

    APPEND ls_test TO mt_tests.

  ENDMETHOD.


  METHOD create.

    CREATE OBJECT ro_run.
    ro_run->ms_run-project = io_project->get_details( )-project.

* This is bad, might fail in a concurrency scenario, but hmm
    SELECT MAX( run_name ) FROM zaot_runs INTO @DATA(lv_max)
      WHERE project = @ro_run->ms_run-project.          "#EC CI_NOFIELD
    ro_run->ms_run-run_name = lv_max + 1.

    ro_run->ms_run-run_id = zcl_aot_uuid=>create( ).

  ENDMETHOD.


  METHOD get_blocks.

    rt_blocks = mt_blocks.

  ENDMETHOD.


  METHOD get_container.

    DATA(lo_ui_factory) = NEW cl_scov_stmnt_cov_ui_factory( ).

    DATA(lt_tkey_selops) = VALUE cvt_test_key_selops( (
      option = 'EQ'
      sign   = 'I'
      low    = ii_result->get_measurement( )->get_testkey( ) ) ).

    ri_container = lo_ui_factory->create_stmnt_dcon_factory( lt_tkey_selops
      )->create_stmnt_data_container( io_insp->get_pb_info( ) ).

  ENDMETHOD.


  METHOD get_coverage.
    rt_coverage = mt_coverage.
  ENDMETHOD.


  METHOD get_details.

    rs_run = ms_run.

  ENDMETHOD.


  METHOD get_instance.

    CREATE OBJECT ro_run.

    SELECT SINGLE * FROM zaot_runs INTO ro_run->ms_run WHERE run_id = iv_run_id.
    ASSERT sy-subrc = 0.

    SELECT * FROM zaot_objects INTO TABLE ro_run->mt_objects
      WHERE run_id = iv_run_id
      ORDER BY PRIMARY KEY.

    SELECT * FROM zaot_tests INTO TABLE ro_run->mt_tests
      WHERE run_id = iv_run_id
      ORDER BY PRIMARY KEY.

    SELECT * FROM zaot_cblocks INTO TABLE ro_run->mt_blocks
      WHERE run_id = iv_run_id
      ORDER BY PRIMARY KEY.

    IF lines( ro_run->mt_blocks ) > 0.
      SELECT * FROM zaot_coverage INTO TABLE ro_run->mt_coverage
        FOR ALL ENTRIES IN ro_run->mt_blocks
        WHERE cblock_id = ro_run->mt_blocks-cblock_id
        ORDER BY PRIMARY KEY.
    ENDIF.

  ENDMETHOD.


  METHOD get_objects.

    rt_objects = mt_objects.

  ENDMETHOD.


  METHOD get_tests.

    rt_tests = mt_tests.

  ENDMETHOD.


  METHOD lookup.

    DATA(lt_runs) = zcl_aot_project=>get_instance( iv_project )->list_runs( ).

    READ TABLE lt_runs INTO DATA(ls_run) WITH KEY run_name = iv_run_name.
    ASSERT sy-subrc = 0.

    ro_run = zcl_aot_run=>get_instance( ls_run-run_id ).

  ENDMETHOD.


  METHOD save.

    INSERT zaot_runs FROM ms_run.
    ASSERT sy-subrc = 0.

    INSERT zaot_objects  FROM TABLE mt_objects.
    INSERT zaot_tests    FROM TABLE mt_tests.
    INSERT zaot_cblocks  FROM TABLE mt_blocks.
    INSERT zaot_coverage FROM TABLE mt_coverage.

  ENDMETHOD.


  METHOD set_end_time.

    GET TIME STAMP FIELD ms_run-end_time.

  ENDMETHOD.


  METHOD set_start_time.

    GET TIME STAMP FIELD ms_run-start_time.

  ENDMETHOD.
ENDCLASS.