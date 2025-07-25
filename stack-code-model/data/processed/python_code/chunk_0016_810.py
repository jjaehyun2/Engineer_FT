*"* use this source file for the definition and implementation of
*"* local helper classes, interface definitions and type
*"* declarations

CLASS lcl_coverage_walker DEFINITION FINAL.

  PUBLIC SECTION.
*    TYPES: BEGIN OF ty_cover,
*             class TYPE seoclsname,
*             meta  TYPE cvt_stmnt_cov_meta_data,
*           END OF ty_cover.
*
*    TYPES: BEGIN OF ty_result,
*             class  TYPE seoclsname,
*             method TYPE seocpdname,
*             source TYPE svt_src,
*             cover  TYPE STANDARD TABLE OF ty_cover WITH EMPTY KEY,
*           END OF ty_result.
*
*    TYPES: ty_result_tt TYPE SORTED TABLE OF ty_result WITH UNIQUE KEY class method.

    METHODS:
      constructor
        IMPORTING
          ii_coverage TYPE REF TO if_aucv_cvrg_rslt_provider
          io_run      TYPE REF TO zcl_aot_run
          iv_class    TYPE tadir-obj_name,
      run.

  PRIVATE SECTION.
*    TYPES: BEGIN OF ty_item,
*             pb_type    TYPE cvd_pb_type,
*             pb_name    TYPE cvd_pb_name,
*             prog_class TYPE cvd_prog_class,
*             class_sub  TYPE c LENGTH 4,
*             prog_type  TYPE cvd_prog_type,
*             prog_name  TYPE cvd_prog_name,
*             executed   TYPE i,
*           END OF ty_item.

    DATA:
*      mt_result TYPE ty_result_tt,
      mo_run    TYPE REF TO zcl_aot_run,
      mv_class  TYPE tadir-obj_name,
*      mt_items  TYPE STANDARD TABLE OF ty_item WITH EMPTY KEY,
      mi_result TYPE REF TO if_scv_result.

    METHODS:
      traverse
        IMPORTING
          ii_node TYPE REF TO if_scv_result_node. " TODO, naming conventions IR/II?

ENDCLASS.

CLASS lcl_coverage_walker IMPLEMENTATION.

  METHOD constructor.
    mo_run   = io_run.
    mv_class = iv_class.

    TRY.
        mi_result = ii_coverage->build_coverage_result( ).
      CATCH cx_scv_execution_error.
        ASSERT 0 = 1.
    ENDTRY.
  ENDMETHOD.

  METHOD run.

    DATA(li_root) = mi_result->get_root_node( ).

    LOOP AT li_root->get_children( ) INTO DATA(li_node).
      traverse( li_node ).
    ENDLOOP.

  ENDMETHOD.

  METHOD traverse.

    IF ii_node->has_children( ) = abap_false.
      mo_run->append_coverage(
        ii_node   = ii_node
        ii_result = mi_result
        iv_class  = mv_class ).
    ENDIF.

    DATA(lt_children) = ii_node->get_children( ).

    LOOP AT lt_children INTO DATA(li_node).
      traverse( li_node ).
    ENDLOOP.

  ENDMETHOD.

ENDCLASS.