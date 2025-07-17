class ZCL_CODE_DOJO_SQL_FAKE definition
  public
  final
  create public .

public section.

  class-methods CHECK_IF_TABLE
    importing
      !IV_TAB_NAME type CLIKE
    returning
      value(R_IS_TABLE) type ABAP_BOOL .

protected section.
private section.
ENDCLASS.



CLASS ZCL_CODE_DOJO_SQL_FAKE IMPLEMENTATION.


  METHOD check_if_table.


    IF zcl_code_dojo_sql_dao_helper=>get_instance( iv_tab_name )->read_tabclass( ) = 'TRANSP'.
      r_is_table = abap_true.
    ENDIF.

  ENDMETHOD.
ENDCLASS.