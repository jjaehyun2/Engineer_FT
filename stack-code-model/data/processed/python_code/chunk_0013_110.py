class ZCL_EXCEL_THEME_OBJECTDEFAULTS definition
  public
  final
  create public .

public section.
*"* public components of class ZCL_EXCEL_THEME_OBJECTDEFAULTS
*"* do not include other source files here!!!

  methods LOAD
    importing
      !IO_OBJECT_DEF type ref to IF_IXML_ELEMENT .
  methods BUILD_XML
    importing
      !LO_OSTREAM type ref to IF_IXML_OSTREAM .
protected section.
private section.

  data OBJECTDEFAULTS type ref to IF_IXML_ELEMENT .
ENDCLASS.



CLASS ZCL_EXCEL_THEME_OBJECTDEFAULTS IMPLEMENTATION.


METHOD build_xml.
  IF objectdefaults IS INITIAL.
    lo_ostream->write_string( |<{ zcl_excel_theme=>c_theme_prefix }:{ zcl_excel_theme=>c_theme_object_def }/>| ).
  ELSE.
    objectdefaults->render( ostream = lo_ostream  recursive = abap_true ).
  ENDIF.
ENDMETHOD.                    "build_xml


method load.
    "! so far copy only existing values
    objectdefaults ?= io_object_def.
  endmethod.                    "load
ENDCLASS.