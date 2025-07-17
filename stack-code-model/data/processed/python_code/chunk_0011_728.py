"! Workflow test class
CLASS zcl_abapgit_testing_wf DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC.

  PUBLIC SECTION.
    INTERFACES:
      if_workflow.
    CLASS-METHODS:
      static_method.
    METHODS:
      instance_method.
    CLASS-DATA:
      gv_static_attribute      TYPE string,
      gv_static_read_only_attr TYPE string READ-ONLY.
    DATA:
      mv_instance_attribute      TYPE string,
      mv_instance_read_only_attr TYPE string READ-ONLY,
      mv_wf_key                  TYPE string READ-ONLY,
      mv_normal_description TYPE string,
      "! <p class="shorttext synchronized" lang="en">Synchronized description</p>
      mv_synchronized_description TYPE string.
  PROTECTED SECTION.
  PRIVATE SECTION.
ENDCLASS.



CLASS zcl_abapgit_testing_wf IMPLEMENTATION.
  METHOD instance_method ##NEEDED.
  ENDMETHOD.

  METHOD static_method ##NEEDED.
  ENDMETHOD.

  METHOD bi_object~default_attribute_value.
  ENDMETHOD.

  METHOD bi_object~execute_default_method.
  ENDMETHOD.

  METHOD bi_persistent~find_by_lpor.
  ENDMETHOD.

  METHOD bi_persistent~lpor.
  ENDMETHOD.

  METHOD bi_persistent~refresh.
  ENDMETHOD.

  METHOD bi_object~release.
  ENDMETHOD.
ENDCLASS.