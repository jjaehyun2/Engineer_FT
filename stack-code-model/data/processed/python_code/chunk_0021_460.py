class ZCL_CODE_DOJO_SQL_DAO definition
  public
  final
  create public .

public section.

  interfaces ZIF_CODE_DOJO_SQL_FAKE_DAO .

  aliases READ_TABCLASS
    for ZIF_CODE_DOJO_SQL_FAKE_DAO~READ_TABCLASS .

  methods CONSTRUCTOR
    importing
      !I_TABNAME type CLIKE .
PROTECTED SECTION.
  PRIVATE SECTION.
    DATA mv_tabname TYPE string.
ENDCLASS.



CLASS ZCL_CODE_DOJO_SQL_DAO IMPLEMENTATION.


  METHOD CONSTRUCTOR.

    mv_tabname = i_tabname.

  ENDMETHOD.


  METHOD ZIF_CODE_DOJO_SQL_FAKE_DAO~READ_TABCLASS.

    SELECT SINGLE tabclass
    FROM dd02l
    INTO r_tabclass
    WHERE tabname = mv_tabname
      AND as4local = 'A'
      AND as4vers = 0.

  ENDMETHOD.
ENDCLASS.