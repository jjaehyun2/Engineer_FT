class ZCL_WDC_SEARCH_ASSIST definition
  public
  inheriting from CL_WD_COMPONENT_ASSISTANCE
  create public .

public section.

  methods EXP_EXCEL
    importing
      !IT_0001 type P0001_TAB
    exporting
      !E_CONTENT type XSTRING .
  methods DO_SEARCH
    importing
      !I_SEARCH type CSEQUENCE
    exporting
      !ET_P0001 type P0001_TAB .
protected section.
private section.
ENDCLASS.



CLASS ZCL_WDC_SEARCH_ASSIST IMPLEMENTATION.


method DO_SEARCH.
  DATA lv_sname TYPE p0001-SNAME.
  lv_sname = I_SEARCH.
  TRANSLATE lv_sname TO UPPER CASE.
  lv_sname = lv_sname && '%'.

  SELECT *  INTO CORRESPONDING FIELDS OF TABLE ET_P0001
    FROM PA0001
    WHERE sname like lv_sname.
endmethod.


method EXP_EXCEL.
  data(LO_FILE) = new ZCL_XTT_FILE_SMW0( 'Z_WD_TEMPLATE' ).
  data(LO_XTT) = new ZCL_XTT_EXCEL_XLSX( LO_FILE ).

  data: begin of LS_DATA
  ,  DATUM type D
  ,  TABLE type P0001_TAB
  , end of LS_DATA
  .
  LS_DATA-DATUM = SY-DATUM.
  LS_DATA-TABLE = IT_0001.
  LO_XTT->MERGE( IS_BLOCK = LS_DATA  ).
  E_CONTENT = LO_XTT->GET_RAW( ).

endmethod.
ENDCLASS.