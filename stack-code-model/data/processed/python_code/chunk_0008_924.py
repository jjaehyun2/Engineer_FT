class ZCL_EXCEL_THEME_ECLRSCHEMELST definition
  public
  final
  create public .

public section.
*"* public components of class ZCL_EXCEL_THEME_ECLRSCHEMELST
*"* do not include other source files here!!!

  methods LOAD
    importing
      !IO_EXTRA_COLOR type ref to IF_IXML_ELEMENT .
  methods BUILD_XML
    importing
      !LO_OSTREAM type ref to IF_IXML_OSTREAM .
protected section.
private section.

  data EXTRACOLOR type ref to IF_IXML_ELEMENT .
ENDCLASS.



CLASS ZCL_EXCEL_THEME_ECLRSCHEMELST IMPLEMENTATION.


METHOD build_xml.

  IF extracolor IS INITIAL.
    lo_ostream->write_string( |<{ zcl_excel_theme=>c_theme_prefix }:{ zcl_excel_theme=>c_theme_extra_color }/>| ).
  ELSE.
    extracolor->render( ostream = lo_ostream recursive = abap_true ).
  ENDIF.

ENDMETHOD.                    "build_xml


method load.
    "! so far copy only existing values
    extracolor ?= io_extra_color.
  endmethod.                    "load
ENDCLASS.