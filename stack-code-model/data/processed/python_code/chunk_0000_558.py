class ZCL_RETURN_TEST definition
  public
  create public .

public section.

  types:
    ty_table_type TYPE STANDARD TABLE OF usr02 WITH DEFAULT KEY .

  methods CONSTRUCTOR
    importing
      !IV_ROWS type I .
  methods EXPORTING
    exporting
      !ET_VALUES type TY_TABLE_TYPE .
  methods RETURN_BY_VALUE
    returning
      value(RT_VALUES) type TY_TABLE_TYPE .
protected section.
private section.

  data MV_ROWS type I .
ENDCLASS.



CLASS ZCL_RETURN_TEST IMPLEMENTATION.


  METHOD constructor.

    mv_rows = iv_rows.

  ENDMETHOD.


  METHOD exporting.

    FIELD-SYMBOLS: <ls_value> LIKE LINE OF et_values.

    DO mv_rows TIMES.
      APPEND INITIAL LINE TO et_values ASSIGNING <ls_value>.
      <ls_value>-bname = sy-index.
    ENDDO.

  ENDMETHOD.


  METHOD return_by_value.

    FIELD-SYMBOLS: <ls_value> LIKE LINE OF rt_values.

    DO mv_rows TIMES.
      APPEND INITIAL LINE TO rt_values ASSIGNING <ls_value>.
      <ls_value>-bname = sy-index.
    ENDDO.

*    DATA: lt_values LIKE rt_values.
*    DO 100000 TIMES.
*      APPEND INITIAL LINE TO lt_values ASSIGNING <ls_value>.
*      <ls_value>-bname = sy-index.
*    ENDDO.
*
*break-point.

  ENDMETHOD.
ENDCLASS.