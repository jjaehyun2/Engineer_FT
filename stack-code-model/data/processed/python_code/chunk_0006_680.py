class ZCL_AOT_AUTO_RUNNER definition
  public
  create public .

public section.

  types:
    BEGIN OF ty_class,
        name         TYPE seoclsname,
        last_changed TYPE c LENGTH 14,
      END OF ty_class .
  types:
    ty_classes TYPE STANDARD TABLE OF ty_class WITH DEFAULT KEY .
  types:
    BEGIN OF ty_tests,
        class  TYPE string,
        method TYPE string,
        kind   TYPE c LENGTH 1,
      END OF ty_tests .
  types:
    BEGIN OF ty_test_result,
        class   TYPE seoclsname,
        seconds TYPE p LENGTH 8 DECIMALS 2,
        tests   TYPE STANDARD TABLE OF ty_tests WITH DEFAULT KEY,
      END OF ty_test_result .

  class-methods LIST_CLASSES
    importing
      !IV_PACKAGE type DEVCLASS
    returning
      value(RT_CLASSES) type TY_CLASSES .
  class-methods RUN_TEST
    importing
      !IV_CLASS type SEOCLSNAME
    returning
      value(RS_RESULT) type TY_TEST_RESULT .
protected section.

  class-methods GET_RUNNER
    returning
      value(RO_RUNNER) type ref to CL_AUCV_TEST_RUNNER_ABSTRACT .
private section.
ENDCLASS.



CLASS ZCL_AOT_AUTO_RUNNER IMPLEMENTATION.


  METHOD get_runner.

    DATA: lo_passport TYPE REF TO object.


    CALL METHOD ('\PROGRAM=SAPLSAUCV_GUI_RUNNER\CLASS=PASSPORT')=>get
      RECEIVING
        result = lo_passport.

    ro_runner = cl_aucv_test_runner_standard=>create( lo_passport ).

  ENDMETHOD.


  METHOD list_classes.

    CONSTANTS: lc_type TYPE tadir-object VALUE 'CLAS'.


    DATA(lt_packages) = zcl_aot_packages=>find_subpackages( iv_package ).
    IF lines( lt_packages ) = 0.
      RETURN.
    ENDIF.

    SELECT obj_name FROM tadir
      INTO TABLE @DATA(lt_tadir)
      FOR ALL ENTRIES IN @lt_packages
      WHERE devclass = @lt_packages-package
      AND pgmid = 'R3TR'
      AND object = @lc_type.                            "#EC CI_GENBUFF

    SORT lt_tadir BY table_line ASCENDING AS TEXT.

    LOOP AT lt_tadir INTO DATA(ls_tadir).
      DATA(ls_aunit_info) = cl_aunit_prog_info=>get_program_info(
        allow_commit = abap_true
        obj_type     = lc_type
        obj_name     = ls_tadir-obj_name ).
      IF ls_aunit_info-has_tests = abap_true.
        DATA(ls_class) = VALUE ty_class(
          name = ls_tadir-obj_name ).

        DATA(lt_includes) = cl_oo_classname_service=>get_all_class_includes( ls_class-name ).
        IF lines( lt_includes ) = 0.
          CONTINUE.
        ENDIF.

        SELECT udat, utime FROM reposrc
          INTO TABLE @DATA(lt_reposrc)
          FOR ALL ENTRIES IN @lt_includes
          WHERE progname = @lt_includes-table_line
          AND r3state = 'A'.
        SORT lt_reposrc BY udat DESCENDING utime DESCENDING.

        ls_class-last_changed = |{ lt_reposrc[ 1 ]-udat }{ lt_reposrc[ 1 ]-utime }|.
        APPEND ls_class TO rt_classes.
      ENDIF.
    ENDLOOP.

    SORT rt_classes ASCENDING.

  ENDMETHOD.


  METHOD run_test.

    CONSTANTS: lc_risk TYPE saunit_d_allowed_risk_level VALUE 11,
               lc_dura TYPE saunit_d_allowed_rt_duration VALUE 24.

    DATA: lo_casted        TYPE REF TO cl_saunit_internal_result,
          lv_kind          TYPE c LENGTH 1,
          lv_program_index TYPE i,
          lv_class_index   TYPE i,
          lv_method_index  TYPE i,
          lv_t1            TYPE i,
          lv_t2            TYPE i.


    GET RUN TIME FIELD lv_t1.
    get_runner( )->run_for_program_keys(
      EXPORTING
        i_limit_on_duration_category = lc_dura
        i_limit_on_risk_level        = lc_risk
        i_program_keys               = VALUE #( ( obj_name = iv_class
                                                  obj_type = 'CLAS' ) )
      IMPORTING
        e_aunit_result               = DATA(li_aunit) ).
    GET RUN TIME FIELD lv_t2.

    rs_result-seconds = ( lv_t2 - lv_t1 ) / 1000000.
    rs_result-class = iv_class.

    lo_casted ?= li_aunit.

    LOOP AT lo_casted->f_task_data-programs INTO DATA(ls_program).
      lv_program_index = sy-tabix.
      LOOP AT ls_program-classes INTO DATA(ls_class).
        lv_class_index = sy-tabix.
        LOOP AT ls_class-methods INTO DATA(ls_method).
          lv_method_index = sy-tabix.

          READ TABLE lo_casted->f_task_data-alerts_by_indicies WITH KEY
            program_ndx = lv_program_index
            class_ndx = lv_class_index
            method_ndx = lv_method_index
            INTO DATA(ls_alert).
          IF sy-subrc = 0.
            lv_kind = ls_alert-alerts[ 1 ]-kind.
          ELSE.
            CLEAR lv_kind.
          ENDIF.

          APPEND VALUE #(
            class   = ls_class-info-name
            method  = ls_method-info-name
            kind    = lv_kind ) TO rs_result-tests.
        ENDLOOP.
      ENDLOOP.
    ENDLOOP.

  ENDMETHOD.
ENDCLASS.