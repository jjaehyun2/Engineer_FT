CLASS zcl_code_dojo_sql_fake_dao DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.

    INTERFACES: zif_code_dojo_sql_fake_dao.
    ALIASES: read_tabclass FOR zif_code_dojo_sql_fake_dao~read_tabclass.

    METHODS constructor
      IMPORTING
        i_tabname TYPE clike.

PROTECTED SECTION.
  PRIVATE SECTION.
    DATA mv_tabname TYPE string.
ENDCLASS.



CLASS ZCL_CODE_DOJO_SQL_FAKE_DAO IMPLEMENTATION.


  METHOD constructor.

    mv_tabname = i_tabname.

  ENDMETHOD.


  METHOD zif_code_dojo_sql_fake_dao~read_tabclass.

    CASE mv_tabname.
      WHEN '$NICO'.
        r_tabclass = 'INTTAB'.
      WHEN '$ENNO'.
        r_tabclass = 'TRANSP'.
    ENDCASE.

  ENDMETHOD.
ENDCLASS.