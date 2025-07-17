REPORT zclasstest.

PARAMETERS: p_subm TYPE abap_bool RADIOBUTTON GROUP r1 DEFAULT 'X',
            p_subp TYPE abap_bool RADIOBUTTON GROUP r1.

CLASS lcl_main DEFINITION.
  PUBLIC SECTION.
    METHODS:
      run.
  PROTECTED SECTION.
  PRIVATE SECTION.
    CONSTANTS:
      gc_classname TYPE abap_classname VALUE 'ZCL_CLASSTEST_CLASS'.
    CLASS-METHODS:
      change_class IMPORTING iv_add TYPE abap_bool.
ENDCLASS.

CLASS lcl_main IMPLEMENTATION.
  METHOD run.
    DATA: lo_test   TYPE REF TO object,
          lo_test2  TYPE REF TO object,
          lo_test3  TYPE REF TO object,
          lo_test4  TYPE REF TO object,
          lv_submit TYPE abap_bool.

    IMPORT submit = lv_submit FROM MEMORY ID 'ZCT'.

    BREAK-POINT.

    IF lv_submit = abap_false.

      change_class( abap_false ).

      " This first create object is the first access to the class (since there is no statically
      " typed variable) which defines the ABAP load used in this internal mode. All other accesses
      " will use this version of the class, even when it's changed.
      CREATE OBJECT lo_test TYPE (gc_classname).
      CALL METHOD: lo_test->('TEST_1'),
                   lo_test->('TEST_2'),
                   lo_test->('TEST_3').
*      CALL METHOD lo_test->('TEST_4'). " Method does not exist yet at all

      change_class( abap_true ).

      CREATE OBJECT lo_test2 TYPE (gc_classname).
      CALL METHOD: lo_test2->('TEST_1'),
                   lo_test2->('TEST_2'),
                   lo_test2->('TEST_3').
      " Method exists now in active version, this internal mode
      " does still have the 'old' ABAP Load loaded though, so
      " it doesn't exist here, runtime error.
*      CALL METHOD lo_test2->('TEST_4').

      IF p_subm = abap_true.
        EXPORT submit = abap_true TO MEMORY ID 'ZCT'.
        SUBMIT (sy-repid) AND RETURN.
        EXPORT submit = abap_false TO MEMORY ID 'ZCT'.

      ELSEIF p_subp = abap_true.
        DATA(lt_pool) = VALUE stringtab(
          ( |PROGRAM.| )
          ( |CLASS lcl_sub DEFINITION INHERITING FROM { gc_classname }.| )
          ( |ENDCLASS.| )
        ).
        GENERATE SUBROUTINE POOL lt_pool NAME DATA(lv_prog).
        DATA(lv_classname) = |\\PROGRAM={ lv_prog }\\CLASS=LCL_SUB|.
        " Runtime error LOAD_PROGRAM_CLASS_MISMATCH here, because the subroutine pool has a class
        " that inherits from a newer version of ZCL_CLASSTEST than is active in this internal mode.
        CREATE OBJECT lo_test4 TYPE (lv_classname).
        CALL METHOD: lo_test4->('TEST_1'),
                     lo_test4->('TEST_2'),
                     lo_test4->('TEST_3').
        CALL METHOD lo_test4->('TEST_4').
      ENDIF.

    ELSE.
      " First access to the class in this internal mode -> new method is there
      CREATE OBJECT lo_test3 TYPE (gc_classname).
      CALL METHOD: lo_test3->('TEST_1'),
                   lo_test3->('TEST_2'),
                   lo_test3->('TEST_3').
      CALL METHOD lo_test3->('TEST_4'). " Now it's here
    ENDIF.

  ENDMETHOD.

  METHOD change_class.
    DATA: ls_seoclass         TYPE vseoclass,
          lt_seomethods       TYPE seoo_methods_r,
          lt_source           TYPE seo_method_source_table,
          lt_inactive_objects TYPE sabap_inact_obj_tab,
          lt_activate_objects TYPE STANDARD TABLE OF dwinactiv.

    lt_source = VALUE #(
      ( cpdname = 'TEST_1' )
      ( cpdname = 'TEST_2' )
      ( cpdname = 'TEST_3' )
      ( cpdname = 'TEST_4' )
    ).

    SELECT SINGLE * INTO @ls_seoclass
      FROM vseoclass
      WHERE clsname = @gc_classname
        AND version = @seoc_version_active.

    SELECT * INTO TABLE @lt_seomethods
      FROM vseomethod
      WHERE clsname = @gc_classname
        AND version = @seoc_version_active
      ORDER BY cmpname.

    IF iv_add = abap_true.
      APPEND lt_seomethods[ 3 ] TO lt_seomethods REFERENCE INTO DATA(lr_new).
      lr_new->cmpname = 'TEST_4'.
    ELSE.
      DELETE lt_seomethods WHERE cmpname = 'TEST_4'.
      DELETE lt_source WHERE cpdname = 'TEST_4'.
    ENDIF.

    SORT lt_seomethods BY cmpname.
    DELETE ADJACENT DUPLICATES FROM lt_seomethods.

    CALL FUNCTION 'SEO_CLASS_CREATE_COMPLETE'
      EXPORTING
        devclass        = gc_classname
        overwrite       = abap_true
        method_sources  = lt_source
      CHANGING
        class           = ls_seoclass
        methods         = lt_seomethods
      EXCEPTIONS
        existing        = 1
        is_interface    = 2
        db_error        = 3
        component_error = 4
        no_access       = 5
        other           = 6
        OTHERS          = 7.
    IF sy-subrc <> 0.
      MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
                 WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
    ENDIF.

    CALL FUNCTION 'RS_INACTIVE_OBJECTS_IN_OBJECT'
      EXPORTING
        obj_name         = CONV trobj_name( gc_classname )
        object           = 'CLAS'
      TABLES
        inactive_objects = lt_activate_objects
      EXCEPTIONS
        object_not_found = 1
        OTHERS           = 2.
    IF sy-subrc <> 0.
      MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
                 WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
    ENDIF.

    CALL FUNCTION 'RS_WORKING_OBJECTS_ACTIVATE'
      EXPORTING
        ui_decoupled           = abap_true
      TABLES
        objects                = lt_activate_objects
      EXCEPTIONS
        excecution_error       = 1
        cancelled              = 2
        insert_into_corr_error = 3
        OTHERS                 = 4.
    IF sy-subrc <> 0.
      MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
                 WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
    ENDIF.
  ENDMETHOD.
ENDCLASS.

START-OF-SELECTION.
  NEW lcl_main( )->run( ).