class ZCL_AOT_RUNNER definition
  public
  create public .

public section.

  methods CONSTRUCTOR
    importing
      !IO_PROJECT type ref to ZCL_AOT_PROJECT .
  methods RUN
    returning
      value(RO_RUN) type ref to ZCL_AOT_RUN .
protected section.
private section.

  data MO_PROJECT type ref to ZCL_AOT_PROJECT .
  data MO_RUN type ref to ZCL_AOT_RUN .

  methods ANALYZE_RESULT
    importing
      !IS_TADIR type TADIR
      !IO_RESULT type ref to CL_SAUNIT_INTERNAL_RESULT .
  methods FIND_OBJECTS
    returning
      value(RT_TADIR) type TT_TADIR .
  methods GET_RUNNER
    importing
      !IV_COVERAGE type ABAP_BOOL default ABAP_FALSE
    returning
      value(RO_RUNNER) type ref to CL_AUCV_TEST_RUNNER_ABSTRACT .
  methods HAS_TESTS
    importing
      !IS_TADIR type TADIR
    returning
      value(RV_HAS_TESTS) type ABAP_BOOL .
  methods RUN_COVERAGE
    importing
      !IS_TADIR type TADIR .
  methods RUN_NORMAL
    importing
      !IS_TADIR type TADIR .
ENDCLASS.



CLASS ZCL_AOT_RUNNER IMPLEMENTATION.


  METHOD analyze_result.

    LOOP AT io_result->f_task_data-programs INTO DATA(ls_program).
      DATA(lv_program_index) = sy-tabix.
      LOOP AT ls_program-classes INTO DATA(ls_class).
        DATA(lv_class_index) = sy-tabix.
        LOOP AT ls_class-methods INTO DATA(ls_method).
          DATA(lv_method_index) = sy-tabix.

          READ TABLE io_result->f_task_data-alerts_by_indicies WITH KEY
            program_ndx = lv_program_index
            class_ndx = lv_class_index
            method_ndx = lv_method_index
            INTO DATA(ls_alert).
          IF sy-subrc = 0.
            DATA(lv_kind) = ls_alert-alerts[ 1 ]-kind.
          ELSE.
            CLEAR lv_kind.
          ENDIF.

          mo_run->append_test(
            VALUE #(
              program_name = ls_program-info-name
              class_name   = ls_class-info-name
              method_name  = ls_method-info-name
              kind         = lv_kind
              object_name  = is_tadir-obj_name
              object_type  = is_tadir-object ) ).

        ENDLOOP.
      ENDLOOP.
    ENDLOOP.

  ENDMETHOD.


  METHOD constructor.

    mo_project = io_project.

    mo_run = zcl_aot_run=>create( io_project ).

  ENDMETHOD.


  METHOD find_objects.

    DATA(lt_packages) = zcl_aot_packages=>find_all_subpackages( mo_project->get_details( )-devclass ).

    LOOP AT lt_packages INTO DATA(ls_package).
      SELECT * FROM tadir
        APPENDING TABLE @rt_tadir
        WHERE object = 'CLAS' " TODO
        AND devclass = @ls_package-devclass.
    ENDLOOP.

  ENDMETHOD.


  METHOD get_runner.

    DATA: lo_passport TYPE REF TO object.


    CALL METHOD ('\PROGRAM=SAPLSAUCV_GUI_RUNNER\CLASS=PASSPORT')=>get
      RECEIVING
        result = lo_passport.

    IF iv_coverage = abap_true.
      ro_runner = cl_aucv_test_runner_coverage=>create( lo_passport ).
    ELSE.
      ro_runner = cl_aucv_test_runner_standard=>create( lo_passport ).
    ENDIF.

  ENDMETHOD.


  METHOD has_tests.

    DATA(ls_aunit_info) = cl_aunit_prog_info=>get_program_info(
      allow_commit = abap_true
      obj_type     = is_tadir-object
      obj_name     = is_tadir-obj_name ).

    rv_has_tests = ls_aunit_info-has_tests.

  ENDMETHOD.


  METHOD run.

    DATA(lt_tadir) = find_objects( ).

    mo_run->set_start_time( ).

    LOOP AT lt_tadir INTO DATA(ls_tadir).

      cl_progress_indicator=>progress_indicate(
        i_text               = |Processing { sy-tabix }/{ lines( lt_tadir ) } { ls_tadir-obj_name }|
        i_processed          = sy-tabix
        i_total              = lines( lt_tadir )
        i_output_immediately = abap_true ).

      IF has_tests( ls_tadir ) = abap_false.
        mo_run->append_object( VALUE #(
          object_name = ls_tadir-obj_name
          object_type = ls_tadir-object
          devclass    = ls_tadir-devclass
          has_tests   = abap_false ) ).
        CONTINUE.
      ENDIF.

* have to run the tests twice to get a proper runtime measurement
      run_normal( ls_tadir ).
      run_coverage( ls_tadir ).

    ENDLOOP.

    mo_run->set_end_time( ).

    ro_run = mo_run.

  ENDMETHOD.


  METHOD run_coverage.

    DATA: lt_packages TYPE string_sorted_table.

* TODO: optimize, this is found for every object, but will be the same for every object
    DATA(lt_tdevc) = zcl_aot_packages=>find_all_subpackages( mo_project->get_details( )-devclass ).
    LOOP AT lt_tdevc INTO DATA(ls_tdevc).
      INSERT CONV #( ls_tdevc-devclass ) INTO TABLE lt_packages.
    ENDLOOP.

* todo, RUN_FOR_TEST_CLASS_HANDLES? to get a more precise coverage?
    get_runner( abap_true )->run_for_program_keys(
      EXPORTING
        i_limit_on_duration_category = mo_project->get_details( )-duration
        i_limit_on_risk_level        = mo_project->get_details( )-risk_level
        i_program_keys               = VALUE #( ( CORRESPONDING #( is_tadir MAPPING obj_type = object ) ) )
        i_packages_to_measure        = lt_packages
      IMPORTING
        e_coverage_result            = DATA(li_coverage)
*        e_aunit_result               = DATA(li_aunit)
        ).

    NEW lcl_coverage_walker(
      ii_coverage = li_coverage
      iv_class    = is_tadir-obj_name
      io_run      = mo_run )->run( ).

  ENDMETHOD.


  METHOD run_normal.

    DATA: lo_casted TYPE REF TO cl_saunit_internal_result.

    DATA(lo_timer) = NEW zcl_aot_timer( ).
    get_runner( )->run_for_program_keys(
      EXPORTING
        i_limit_on_duration_category = mo_project->get_details( )-duration
        i_limit_on_risk_level        = mo_project->get_details( )-risk_level
        i_program_keys               = VALUE #( ( CORRESPONDING #( is_tadir MAPPING obj_type = object ) ) )
      IMPORTING
        e_aunit_result               = DATA(li_aunit) ).
    DATA(lv_milli) = lo_timer->stop( ).

    lo_casted ?= li_aunit.

    mo_run->append_object( VALUE #(
      object_name       = is_tadir-obj_name
      object_type       = is_tadir-object
      devclass          = is_tadir-devclass
      runtime           = lv_milli
      has_tests         = abap_true
      has_skipped_tests = lo_casted->f_task_data-info-has_skipped ) ).

    analyze_result( is_tadir  = is_tadir
                    io_result = lo_casted ).

  ENDMETHOD.
ENDCLASS.