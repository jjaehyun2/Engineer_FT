CLASS zcl_aot_service_rest DEFINITION
  PUBLIC
  CREATE PUBLIC .

  PUBLIC SECTION.

    INTERFACES zif_aot_service .
    INTERFACES zif_swag_handler .

    METHODS objects_list
      IMPORTING
        !iv_project       TYPE zaot_project_name
        !iv_run_name      TYPE zaot_run_name
      RETURNING
        VALUE(rt_objects) TYPE zaot_objects_overview_tt .
    METHODS object_details
      IMPORTING
        !iv_project       TYPE zaot_project_name
        !iv_run_name      TYPE zaot_run_name
        !iv_object_type   TYPE zaot_objects-object_type
        !iv_object_name   TYPE zaot_objects-object_name
      RETURNING
        VALUE(rs_details) TYPE zaot_object_details .
    METHODS run_details
      IMPORTING
        !iv_project       TYPE zaot_project_name
        !iv_run_name      TYPE zaot_run_name
      RETURNING
        VALUE(rs_details) TYPE zaot_runs_details .
    METHODS list
      IMPORTING
        !iv_package       TYPE devclass
      RETURNING
        VALUE(rt_classes) TYPE zcl_aot_auto_runner=>ty_classes .
    METHODS run
      IMPORTING
        !iv_class        TYPE seoclsname
      RETURNING
        VALUE(rs_result) TYPE zcl_aot_auto_runner=>ty_test_result .
    METHODS projects_list
      RETURNING
        VALUE(rt_list) TYPE zaot_projects_tt .
    METHODS project_create
      IMPORTING
        !is_data TYPE zaot_project_data .
    METHODS project_details
      IMPORTING
        !iv_project       TYPE zaot_project_name
      RETURNING
        VALUE(rs_details) TYPE zaot_project_details .
    METHODS project_runs
      IMPORTING
        !iv_project    TYPE zaot_project_name
        !iv_days       TYPE integer
      RETURNING
        VALUE(rt_runs) TYPE zaot_runs_overview_tt .
protected section.

  constants C_BASE type STRING value '/sap/zabapopentest/rest' ##NO_TEXT.
private section.
ENDCLASS.



CLASS ZCL_AOT_SERVICE_REST IMPLEMENTATION.


  METHOD list.

    rt_classes = zcl_aot_auto_runner=>list_classes( to_upper( iv_package ) ).

  ENDMETHOD.


  METHOD objects_list.

    DATA(lo_run) = zcl_aot_run=>lookup(
      iv_project  = iv_project
      iv_run_name = iv_run_name ).

    LOOP AT lo_run->get_objects( ) INTO DATA(ls_object).
      APPEND INITIAL LINE TO rt_objects ASSIGNING FIELD-SYMBOL(<ls_object>).
      MOVE-CORRESPONDING ls_object TO <ls_object>.

* todo?

    ENDLOOP.

  ENDMETHOD.


  METHOD object_details.

    DATA(lo_run) = zcl_aot_run=>lookup(
      iv_project  = iv_project
      iv_run_name = iv_run_name ).

    READ TABLE lo_run->get_objects( ) WITH KEY
      object_type = iv_object_type
      object_name = iv_object_name
      INTO DATA(ls_object).
    ASSERT sy-subrc = 0.

    MOVE-CORRESPONDING ls_object TO rs_details.

    LOOP AT lo_run->get_blocks( ) INTO DATA(ls_block)
        WHERE prog_class = iv_object_name
        AND class_sub = 'GLOB'
        AND prog_type = iv_object_type.

      APPEND INITIAL LINE TO rs_details-blocks ASSIGNING FIELD-SYMBOL(<ls_block>).
      <ls_block> = CORRESPONDING #( ls_block EXCEPT source ).
      SPLIT ls_block-source AT |\n| INTO TABLE <ls_block>-source.

      LOOP AT lo_run->get_coverage( ) INTO DATA(ls_coverage) WHERE cblock_id = ls_block-cblock_id.

        READ TABLE <ls_block>-coverage WITH KEY
          program_name = ls_coverage-program_name
          class_name = ls_coverage-class_name
          method_name = ls_coverage-method_name
          ASSIGNING FIELD-SYMBOL(<ls_coverage>).
        IF sy-subrc <> 0.
          APPEND INITIAL LINE TO <ls_block>-coverage ASSIGNING <ls_coverage>.
          <ls_coverage>-program_name = ls_coverage-program_name.
          <ls_coverage>-class_name   = ls_coverage-class_name.
          <ls_coverage>-method_name  = ls_coverage-method_name.
        ENDIF.

        APPEND INITIAL LINE TO <ls_coverage>-meta ASSIGNING FIELD-SYMBOL(<ls_meta>).
        <ls_meta>-row   = ls_coverage-rowcov.
        <ls_meta>-col   = ls_coverage-colcov.
        <ls_meta>-color = ls_coverage-colorcov.
        <ls_meta>-icon  = ls_coverage-iconcov.

      ENDLOOP.

    ENDLOOP.

  ENDMETHOD.


  METHOD projects_list.
    rt_list = zcl_aot_project=>list( ).
  ENDMETHOD.


  METHOD project_create.

    zcl_aot_project=>create( is_data ).

  ENDMETHOD.


  METHOD project_details.

    rs_details = zcl_aot_project=>get_instance( iv_project )->get_details( ).

  ENDMETHOD.


  METHOD project_runs.

* todo, handle IV_DAYS

    DATA(lt_runs) = zcl_aot_project=>get_instance( iv_project )->list_runs( ).

    LOOP AT lt_runs INTO DATA(ls_run).
      APPEND INITIAL LINE TO rt_runs ASSIGNING FIELD-SYMBOL(<ls_run>).
      MOVE-CORRESPONDING ls_run TO <ls_run>.

      DATA(lo_run) = zcl_aot_run=>get_instance( ls_run-run_id ).

      <ls_run>-objects = lines( lo_run->get_objects( ) ).
      <ls_run>-tests_total = lines( lo_run->get_tests( ) ).

      LOOP AT lo_run->get_tests( ) ASSIGNING FIELD-SYMBOL(<ls_test>).
        IF <ls_test>-kind IS INITIAL.
          <ls_run>-tests_passed = <ls_run>-tests_passed + 1.
        ELSE.
          <ls_run>-tests_failed = <ls_run>-tests_failed + 1.
        ENDIF.
      ENDLOOP.
    ENDLOOP.

  ENDMETHOD.


  METHOD run.

    rs_result = zcl_aot_auto_runner=>run_test( iv_class ).

  ENDMETHOD.


  METHOD run_details.

    DATA(lo_run) = zcl_aot_run=>lookup(
      iv_project  = iv_project
      iv_run_name = iv_run_name ).

    rs_details-run     = lo_run->get_details( ).
    rs_details-objects = lo_run->get_objects( ).
    rs_details-tests   = lo_run->get_tests( ).

  ENDMETHOD.


  METHOD zif_aot_service~run.

    DATA: lo_swag TYPE REF TO zcl_swag.


    CREATE OBJECT lo_swag
      EXPORTING
        ii_server = ii_server
        iv_base   = c_base
        iv_title  = 'abapOpenTest'.
    lo_swag->register( me ).

    lo_swag->run( ).

  ENDMETHOD.


  METHOD zif_swag_handler~meta.

    FIELD-SYMBOLS: <ls_meta> LIKE LINE OF rt_meta.

    APPEND INITIAL LINE TO rt_meta ASSIGNING <ls_meta>.
    <ls_meta>-summary   = 'List Classes'(001).
    <ls_meta>-url-regex = '/auto_runner/list$'.
    <ls_meta>-method    = zcl_swag=>c_method-get.
    <ls_meta>-handler   = 'LIST'.
    APPEND 'auto_runner' TO <ls_meta>-tags ##NO_TEXT.

    APPEND INITIAL LINE TO rt_meta ASSIGNING <ls_meta>.
    <ls_meta>-summary   = 'Run Test'(002).
    <ls_meta>-url-regex = '/auto_runner/run$'.
    <ls_meta>-method    = zcl_swag=>c_method-post.
    <ls_meta>-handler   = 'RUN'.
    APPEND 'auto_runner' TO <ls_meta>-tags ##NO_TEXT.

*******************************

    APPEND INITIAL LINE TO rt_meta ASSIGNING <ls_meta>.
    <ls_meta>-summary   = 'List Projects'(003).
    <ls_meta>-url-regex = '/listProjects$'.
    <ls_meta>-method    = zcl_swag=>c_method-get.
    <ls_meta>-handler   = 'PROJECTS_LIST'.
    APPEND 'projects' TO <ls_meta>-tags ##NO_TEXT.

    APPEND INITIAL LINE TO rt_meta ASSIGNING <ls_meta>.
    <ls_meta>-summary   = 'Create Project'(004).
    <ls_meta>-url-regex = '/createProject$'.
    <ls_meta>-method    = zcl_swag=>c_method-post.
    <ls_meta>-handler   = 'PROJECT_CREATE'.
    APPEND 'projects' TO <ls_meta>-tags ##NO_TEXT.

    APPEND INITIAL LINE TO rt_meta ASSIGNING <ls_meta>.
    <ls_meta>-summary   = 'Project Details'(005).
    <ls_meta>-url-regex = '/projects/([\w-]+)$'.
    APPEND 'IV_PROJECT' TO <ls_meta>-url-group_names.
    <ls_meta>-method    = zcl_swag=>c_method-get.
    <ls_meta>-handler   = 'PROJECT_DETAILS'.
    APPEND 'projects' TO <ls_meta>-tags ##NO_TEXT.

    APPEND INITIAL LINE TO rt_meta ASSIGNING <ls_meta>.
    <ls_meta>-summary   = 'Project Runs'(006).
    <ls_meta>-url-regex = '/projects/([\w-]+)/listRuns$'.
    APPEND 'IV_PROJECT' TO <ls_meta>-url-group_names.
    <ls_meta>-method    = zcl_swag=>c_method-get.
    <ls_meta>-handler   = 'PROJECT_RUNS'.
    APPEND 'projects' TO <ls_meta>-tags ##NO_TEXT.

*******************************

    APPEND INITIAL LINE TO rt_meta ASSIGNING <ls_meta>.
    <ls_meta>-summary   = 'Run Details'(007).
    <ls_meta>-url-regex = '/projects/([\w-]+)/runs/([\w-]+)$'.
    APPEND 'IV_PROJECT' TO <ls_meta>-url-group_names.
    APPEND 'IV_RUN_NAME' TO <ls_meta>-url-group_names.
    <ls_meta>-method    = zcl_swag=>c_method-get.
    <ls_meta>-handler   = 'RUN_DETAILS'.
    APPEND 'runs' TO <ls_meta>-tags ##NO_TEXT.

    APPEND INITIAL LINE TO rt_meta ASSIGNING <ls_meta>.
    <ls_meta>-summary   = 'List Objects'(008).
    <ls_meta>-url-regex = '/projects/([\w-]+)/runs/([\w-]+)/objects$'.
    APPEND 'IV_PROJECT' TO <ls_meta>-url-group_names.
    APPEND 'IV_RUN_NAME' TO <ls_meta>-url-group_names.
    <ls_meta>-method    = zcl_swag=>c_method-get.
    <ls_meta>-handler   = 'OBJECTS_LIST'.
    APPEND 'runs' TO <ls_meta>-tags ##NO_TEXT.

    APPEND INITIAL LINE TO rt_meta ASSIGNING <ls_meta>.
    <ls_meta>-summary   = 'Object Details'(009).
    <ls_meta>-url-regex = '/projects/([\w-]+)/runs/([\w-]+)/objects/([\w-]+)/([\w-]+)$'.
    APPEND 'IV_PROJECT' TO <ls_meta>-url-group_names.
    APPEND 'IV_RUN_NAME' TO <ls_meta>-url-group_names.
    APPEND 'IV_OBJECT_TYPE' TO <ls_meta>-url-group_names.
    APPEND 'IV_OBJECT_NAME' TO <ls_meta>-url-group_names.
    <ls_meta>-method    = zcl_swag=>c_method-get.
    <ls_meta>-handler   = 'OBJECT_DETAILS'.
    APPEND 'runs' TO <ls_meta>-tags ##NO_TEXT.

  ENDMETHOD.
ENDCLASS.