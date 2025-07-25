class ZCL_AOT_PROJECT definition
  public
  create private .

public section.

  class-methods CREATE
    importing
      !IS_DATA type ZAOT_PROJECT_DATA
    returning
      value(RO_PROJECT) type ref to ZCL_AOT_PROJECT .
  class-methods GET_INSTANCE
    importing
      !IV_PROJECT type ZAOT_PROJECT_NAME
    returning
      value(RO_PROJECT) type ref to ZCL_AOT_PROJECT .
  class-methods LIST
    importing
      !IT_NAME type ZAOT_PROJECT_NAME_RANGE_TT optional
    returning
      value(RT_PROJECTS) type ZAOT_PROJECTS_TT .
  methods GET_DETAILS
    returning
      value(RS_DETAILS) type ZAOT_PROJECT_DETAILS .
  methods GET_RUN .
  methods LIST_RUNS
    returning
      value(RT_RUNS) type ZAOT_RUNS_TT .
  methods SAVE .
  methods SET_DETAILS
    importing
      !IS_DATA type ZAOT_PROJECT_DATA .
protected section.
private section.

  data MS_PROJECT type ZAOT_PROJECTS .

  methods CONSTRUCTOR
    importing
      !IV_PROJECT type ZAOT_PROJECT_NAME .
ENDCLASS.



CLASS ZCL_AOT_PROJECT IMPLEMENTATION.


  METHOD constructor.

    SELECT SINGLE * FROM zaot_projects
      INTO ms_project
      WHERE name = iv_project.                          "#EC CI_NOFIELD
    ASSERT sy-subrc = 0.

  ENDMETHOD.


  METHOD create.

    ASSERT NOT is_data-name IS INITIAL.
    ASSERT NOT is_data-devclass IS INITIAL.
    ASSERT NOT is_data-risk_level IS INITIAL.
    ASSERT NOT is_data-duration IS INITIAL.

    SELECT SINGLE * FROM tdevc INTO @DATA(ls_tdevc) WHERE devclass = @is_data-devclass.
    ASSERT sy-subrc = 0.

    DATA(ls_data) = CORRESPONDING zaot_projects( is_data ).

    ls_data-project = zcl_aot_uuid=>create( ).

    INSERT zaot_projects FROM ls_data.
    ASSERT sy-subrc = 0.

    ro_project = get_instance( is_data-name ).

  ENDMETHOD.


  METHOD get_details.

    MOVE-CORRESPONDING ms_project TO rs_details.

  ENDMETHOD.


  METHOD get_instance.

    CREATE OBJECT ro_project EXPORTING iv_project = iv_project.

  ENDMETHOD.


  METHOD get_run.

* todo

  ENDMETHOD.


  METHOD list.

    SELECT * FROM zaot_projects
      INTO TABLE rt_projects
      WHERE name IN it_name
      ORDER BY PRIMARY KEY.                             "#EC CI_NOWHERE

  ENDMETHOD.


  METHOD list_runs.

    SELECT * FROM zaot_runs
      INTO TABLE rt_runs
      WHERE project = ms_project-project.               "#EC CI_NOFIELD

  ENDMETHOD.


  METHOD save.

* todo

  ENDMETHOD.


  METHOD set_details.

* todo

  ENDMETHOD.
ENDCLASS.