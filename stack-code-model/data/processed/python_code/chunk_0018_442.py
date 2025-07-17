class ZCL_EXCEL_THEME_EXTLST definition
  public
  final
  create public .

public section.
*"* public components of class ZCL_EXCEL_THEME_EXTLST
*"* do not include other source files here!!!

  methods LOAD
    importing
      !IO_EXTLST type ref to IF_IXML_ELEMENT .
  methods BUILD_XML
    importing
      !LO_OSTREAM type ref to IF_IXML_OSTREAM .
protected section.
private section.

  data EXTLST type ref to IF_IXML_ELEMENT .
ENDCLASS.



CLASS ZCL_EXCEL_THEME_EXTLST IMPLEMENTATION.


METHOD build_xml.

  IF extlst IS INITIAL.
    lo_ostream->write_string( |<{ zcl_excel_theme=>c_theme_prefix }:{ zcl_excel_theme=>c_theme_extlst }/>| ).
  ELSE.
    extlst->render( ostream = lo_ostream recursive = abap_true ).
  ENDIF.

ENDMETHOD.                    "build_xml


method load.
    "! so far copy only existing values
    extlst ?= io_extlst.
  endmethod.                    "load
ENDCLASS.