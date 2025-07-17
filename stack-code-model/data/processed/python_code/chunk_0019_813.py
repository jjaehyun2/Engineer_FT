class ZCL_RETURN_TEST2 definition
  public
  create public .

public section.

  types:
    ty_table_type TYPE STANDARD TABLE OF usr02 WITH DEFAULT KEY .

  methods CONSTRUCTOR
    importing
      !IV_ROWS type I optional .
  methods RETURN_MEMBER
    returning
      value(RT_VALUES) type TY_TABLE_TYPE .
  methods RETURN_LOCAL
    importing
      !IV_ROWS type I
    returning
      value(RT_VALUES) type TY_TABLE_TYPE .
protected section.
private section.

  data MT_DATA type TY_TABLE_TYPE .
ENDCLASS.



CLASS ZCL_RETURN_TEST2 IMPLEMENTATION.


  METHOD constructor.

    FIELD-SYMBOLS: <ls_value> LIKE LINE OF mt_data.


    IF iv_rows > 0.
      DO iv_rows TIMES.
        APPEND INITIAL LINE TO mt_data ASSIGNING <ls_value>.
        <ls_value>-bname = sy-index.
      ENDDO.
    ENDIF.

  ENDMETHOD.


  METHOD return_local.

    FIELD-SYMBOLS: <ls_value> LIKE LINE OF rt_values.

    DO iv_rows TIMES.
      APPEND INITIAL LINE TO rt_values ASSIGNING <ls_value>.
      <ls_value>-bname = sy-index.
    ENDDO.

  ENDMETHOD.


  METHOD return_member.

    rt_values = mt_data.

  ENDMETHOD.
ENDCLASS.