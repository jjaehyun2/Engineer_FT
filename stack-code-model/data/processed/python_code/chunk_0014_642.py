class ZCL_CODE_DOJO_SQL_DAO_HELPER definition
  public
  final
  create public .

public section.

  class-methods GET_INSTANCE
    importing
      !IV_TAB_NAME type CLIKE
    returning
      value(RO_INSTANCE) type ref to ZIF_CODE_DOJO_SQL_FAKE_DAO .
protected section.
private section.
ENDCLASS.



CLASS ZCL_CODE_DOJO_SQL_DAO_HELPER IMPLEMENTATION.


  METHOD get_instance.


    IF iv_tab_name(1) = '$'.
     ro_instance = NEW zcl_code_dojo_sql_fake_dao( iv_tab_name ).
    ELSE.
      ro_instance = NEW zcl_code_dojo_sql_dao( iv_tab_name ).
    ENDIF.

  ENDMETHOD.
ENDCLASS.