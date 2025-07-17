class ZCL_EXCEL_THEME definition
  public
  create public .

public section.
*"* public components of class ZCL_EXCEL_THEME
*"* do not include other source files here!!!

  constants C_THEME_ELEMENTS type STRING value 'themeElements'. "#EC NOTEXT
  constants C_THEME_OBJECT_DEF type STRING value 'objectDefaults'. "#EC NOTEXT
  constants C_THEME_EXTRA_COLOR type STRING value 'extraClrSchemeLst'. "#EC NOTEXT
  constants C_THEME_EXTLST type STRING value 'extLst'. "#EC NOTEXT
  constants C_THEME type STRING value 'theme'. "#EC NOTEXT
  constants C_THEME_NAME type STRING value 'name'. "#EC NOTEXT
  constants C_THEME_XMLNS type STRING value 'xmlns:a'. "#EC NOTEXT
  constants C_THEME_PREFIX type STRING value 'a'. "#EC NOTEXT
  constants C_THEME_PREFIX_WRITE type STRING value 'a:'. "#EC NOTEXT
  constants C_THEME_XMLNS_VAL type STRING value 'http://schemas.openxmlformats.org/drawingml/2006/main'. "#EC NOTEXT

  methods CONSTRUCTOR .
  methods READ_THEME
    importing
      value(IO_THEME_XML) type ref to IF_IXML_DOCUMENT .
  methods WRITE_THEME
    importing
      !LO_OSTREAM type ref to IF_IXML_OSTREAM .
  methods SET_COLOR
    importing
      value(IV_TYPE) type STRING
      value(IV_SRGB) type ZCL_EXCEL_THEME_COLOR_SCHEME=>T_SRGB optional
      value(IV_SYSCOLORNAME) type STRING optional
      value(IV_SYSCOLORLAST) type ZCL_EXCEL_THEME_COLOR_SCHEME=>T_SRGB optional .
  methods SET_COLOR_SCHEME_NAME
    importing
      value(IV_NAME) type STRING .
  methods SET_FONT
    importing
      value(IV_TYPE) type STRING
      value(IV_SCRIPT) type STRING
      value(IV_TYPEFACE) type STRING .
  methods SET_LATIN_FONT
    importing
      value(IV_TYPE) type STRING
      value(IV_TYPEFACE) type STRING
      value(IV_PANOSE) type STRING optional
      value(IV_PITCHFAMILY) type STRING optional
      value(IV_CHARSET) type STRING optional .
  methods SET_EA_FONT
    importing
      value(IV_TYPE) type STRING
      value(IV_TYPEFACE) type STRING
      value(IV_PANOSE) type STRING optional
      value(IV_PITCHFAMILY) type STRING optional
      value(IV_CHARSET) type STRING optional .
  methods SET_CS_FONT
    importing
      value(IV_TYPE) type STRING
      value(IV_TYPEFACE) type STRING
      value(IV_PANOSE) type STRING optional
      value(IV_PITCHFAMILY) type STRING optional
      value(IV_CHARSET) type STRING optional .
  methods SET_FONT_SCHEME_NAME
    importing
      value(IV_NAME) type STRING .
  methods SET_THEME_NAME
    importing
      value(IV_NAME) type STRING .
  methods GET_NAME
    returning
      value(RVAL) type STRING .
protected section.

  data ELEMENTS type ref to ZCL_EXCEL_THEME_ELEMENTS .
  data OBJECTDEFAULTS type ref to ZCL_EXCEL_THEME_OBJECTDEFAULTS .
  data EXTCLRSCHEMELST type ref to ZCL_EXCEL_THEME_ECLRSCHEMELST .
  data EXTLST type ref to ZCL_EXCEL_THEME_EXTLST .
private section.

  data THEME_CHANGED type ABAP_BOOL .
  data THEME_READ type ABAP_BOOL .
  data NAME type STRING .
  data XMLS_A type STRING .
ENDCLASS.



CLASS ZCL_EXCEL_THEME IMPLEMENTATION.


method constructor.
    create object elements.
    create object objectdefaults.
    create object extclrschemelst.
    create object extlst.
  endmethod.                    "class_constructor


method GET_NAME.
  rval = me->name.
endmethod.


method read_theme.
    data: lo_node_theme type ref to if_ixml_element.
    data: lo_theme_children type ref to if_ixml_node_list.
    data: lo_theme_iterator type ref to if_ixml_node_iterator.
    data: lo_theme_element type ref to if_ixml_element.
    check io_theme_xml is not initial.

    lo_node_theme  = io_theme_xml->get_root_element( )."   find_from_name( name = c_theme ).
    if lo_node_theme is bound.
      name = lo_node_theme->get_attribute( name = c_theme_name ).
      xmls_a = lo_node_theme->get_attribute( name = c_theme_xmlns ).
      lo_theme_children = lo_node_theme->get_children( ).
      lo_theme_iterator = lo_theme_children->create_iterator( ).
      lo_theme_element ?= lo_theme_iterator->get_next( ).
      while lo_theme_element is bound.
        case lo_theme_element->get_name( ).
          when c_theme_elements.
            elements->load( io_elements = lo_theme_element ).
          when c_theme_object_def.
            objectdefaults->load( io_object_def = lo_theme_element ).
          when c_theme_extra_color.
            extclrschemelst->load( io_extra_color = lo_theme_element ).
          when c_theme_extlst.
            extlst->load( io_extlst = lo_theme_element ).
        endcase.
        lo_theme_element ?= lo_theme_iterator->get_next( ).
      endwhile.
    endif.
  endmethod.                    "read_theme


method set_color.
    elements->color_scheme->set_color(
      exporting
        iv_type         = iv_type
        iv_srgb         = iv_srgb
        iv_syscolorname = iv_syscolorname
        iv_syscolorlast = iv_syscolorlast
    ).
  endmethod.                    "set_color


method set_color_scheme_name.
    elements->color_scheme->set_name( iv_name = iv_name ).
  endmethod.                    "set_color_scheme_name


method set_cs_font.
    elements->font_scheme->modify_cs_font(
      exporting
        iv_type        = iv_type
        iv_typeface    = iv_typeface
        iv_panose      = iv_panose
        iv_pitchfamily = iv_pitchfamily
        iv_charset     = iv_charset
    ).
  endmethod.                    "set_cs_font


method set_ea_font.
    elements->font_scheme->modify_ea_font(
      exporting
        iv_type        = iv_type
        iv_typeface    = iv_typeface
        iv_panose      = iv_panose
        iv_pitchfamily = iv_pitchfamily
        iv_charset     = iv_charset
    ).
  endmethod.                    "set_ea_font


method set_font.
    elements->font_scheme->modify_font(
      exporting
        iv_type     = iv_type
        iv_script   = iv_script
        iv_typeface = iv_typeface
    ).
  endmethod.                    "set_font


method set_font_scheme_name.
    elements->font_scheme->set_name( iv_name = iv_name ).
  endmethod.                    "set_font_scheme_name


method set_latin_font.
    elements->font_scheme->modify_latin_font(
      exporting
        iv_type        = iv_type
        iv_typeface    = iv_typeface
        iv_panose      = iv_panose
        iv_pitchfamily = iv_pitchfamily
        iv_charset     = iv_charset
    ).
  endmethod.                    "set_latin_font


method set_theme_name.
    name = iv_name.
  endmethod.


METHOD write_theme.
  lo_ostream->write_string( '<?xml version="1.0" encoding="utf-8" standalone="yes"?>' ).

  lo_ostream->write_string( |<{ c_theme_prefix }:{ c_theme }| ).
  lo_ostream->write_string( | { c_theme_xmlns }="{ c_theme_xmlns_val }"| ).
  lo_ostream->write_string( | { c_theme_name }="{ name }">| ).

  elements->build_xml( lo_ostream ).
  objectdefaults->build_xml( lo_ostream ).
  extclrschemelst->build_xml( lo_ostream ).
  extlst->build_xml( lo_ostream ).

  lo_ostream->write_string( |</{ c_theme_prefix }:{ c_theme }>| ).

ENDMETHOD.                    "write_theme
ENDCLASS.