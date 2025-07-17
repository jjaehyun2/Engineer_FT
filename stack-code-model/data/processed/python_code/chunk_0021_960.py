class ZCL_EXCEL_THEME_COLOR_SCHEME definition
  public
  final
  create public

  global friends ZCL_EXCEL_THEME
                 ZCL_EXCEL_THEME_ELEMENTS .

public section.
*"* public components of class ZCL_EXCEL_THEME_COLOR_SCHEME
*"* do not include other source files here!!!

  types T_SRGB type STRING .
  types:
    begin of t_syscolor,
              val type string,
              lastclr type t_srgb,
             end of t_syscolor .
  types:
    begin of t_color,
             srgb type t_srgb,
             syscolor type t_syscolor,
             end of t_color .

  constants C_DARK1 type STRING value 'dk1'. "#EC NOTEXT
  constants C_DARK2 type STRING value 'dk2'. "#EC NOTEXT
  constants C_LIGHT1 type STRING value 'lt1'. "#EC NOTEXT
  constants C_LIGHT2 type STRING value 'lt2'. "#EC NOTEXT
  constants C_ACCENT1 type STRING value 'accent1'. "#EC NOTEXT
  constants C_ACCENT2 type STRING value 'accent2'. "#EC NOTEXT
  constants C_ACCENT3 type STRING value 'accent3'. "#EC NOTEXT
  constants C_ACCENT4 type STRING value 'accent4'. "#EC NOTEXT
  constants C_ACCENT5 type STRING value 'accent5'. "#EC NOTEXT
  constants C_ACCENT6 type STRING value 'accent6'. "#EC NOTEXT
  constants C_HLINK type STRING value 'hlink'. "#EC NOTEXT
  constants C_FOLHLINK type STRING value 'folHlink'. "#EC NOTEXT
  constants C_SYSCOLOR type STRING value 'sysClr'. "#EC NOTEXT
  constants C_SRGBCOLOR type STRING value 'srgbClr'. "#EC NOTEXT
  constants C_VAL type STRING value 'val'. "#EC NOTEXT
  constants C_LASTCLR type STRING value 'lastClr'. "#EC NOTEXT
  constants C_NAME type STRING value 'name'. "#EC NOTEXT
  constants C_SCHEME type STRING value 'clrScheme'. "#EC NOTEXT

  methods LOAD
    importing
      !IO_COLOR_SCHEME type ref to IF_IXML_ELEMENT .
  methods SET_COLOR
    importing
      value(IV_TYPE) type STRING
      value(IV_SRGB) type T_SRGB optional
      value(IV_SYSCOLORNAME) type STRING optional
      value(IV_SYSCOLORLAST) type T_SRGB .
  methods BUILD_XML
    importing
      !LO_OSTREAM type ref to IF_IXML_OSTREAM .
  methods CONSTRUCTOR .
  methods SET_NAME
    importing
      value(IV_NAME) type STRING .
protected section.

  data NAME type STRING .
  data DARK1 type T_COLOR .
  data DARK2 type T_COLOR .
  data LIGHT1 type T_COLOR .
  data LIGHT2 type T_COLOR .
  data ACCENT1 type T_COLOR .
  data ACCENT2 type T_COLOR .
  data ACCENT3 type T_COLOR .
  data ACCENT4 type T_COLOR .
  data ACCENT5 type T_COLOR .
  data ACCENT6 type T_COLOR .
  data HLINK type T_COLOR .
  data FOLHLINK type T_COLOR .
private section.

  methods GET_COLOR
    importing
      !IO_OBJECT type ref to IF_IXML_ELEMENT
    returning
      value(RV_COLOR) type T_COLOR .
  methods SET_DEFAULTS .
ENDCLASS.



CLASS ZCL_EXCEL_THEME_COLOR_SCHEME IMPLEMENTATION.


METHOD build_xml.
  DEFINE add_color.
*   &1 - name
*   &2 - color

    lo_ostream->write_string( |<{ zcl_excel_theme=>c_theme_prefix }:{ &1 }>| ).

    IF &2-srgb IS NOT INITIAL.
      lo_ostream->write_string( |<{ zcl_excel_theme=>c_theme_prefix }:{ c_srgbcolor }| ).
      lo_ostream->write_string( | { c_val }="{ &2-srgb }"/>| ).
    ELSE.
      lo_ostream->write_string( |<{ zcl_excel_theme=>c_theme_prefix }:{ c_syscolor }| ).
      lo_ostream->write_string( | { c_val }="{ &2-syscolor-val }"| ).
      lo_ostream->write_string( | { c_lastclr }="{ &2-syscolor-lastclr }"/>| ).
    ENDIF.

    lo_ostream->write_string( |</{ zcl_excel_theme=>c_theme_prefix }:{ &1 }>| ).

  END-OF-DEFINITION.


  lo_ostream->write_string( |<{ zcl_excel_theme=>c_theme_prefix }:{ zcl_excel_theme_elements=>c_color_scheme }| ).
  lo_ostream->write_string( | { c_name }="{ name }">| ).

  add_color c_dark1 dark1.
  add_color c_light1 light1.
  add_color c_dark2 dark2.
  add_color c_light2 light2.
  add_color c_accent1 accent1.
  add_color c_accent2 accent2.
  add_color c_accent3 accent3.
  add_color c_accent4 accent4.
  add_color c_accent5 accent5.
  add_color c_accent6 accent6.
  add_color c_hlink hlink.
  add_color c_folhlink folhlink.

  lo_ostream->write_string( |</{ zcl_excel_theme=>c_theme_prefix }:{ zcl_excel_theme_elements=>c_color_scheme }>| ).
ENDMETHOD.                    "build_xml


method constructor.
    set_defaults( ).
  endmethod.                    "constructor


method get_color.
    data: lo_color_children type ref to if_ixml_node_list.
    data: lo_color_iterator type ref to if_ixml_node_iterator.
    data: lo_color_element type ref to if_ixml_element.
    check io_object  is not initial.

    lo_color_children = io_object->get_children( ).
    lo_color_iterator = lo_color_children->create_iterator( ).
    lo_color_element ?= lo_color_iterator->get_next( ).
    if lo_color_element is bound.
      case lo_color_element->get_name( ).
        when c_srgbcolor.
          rv_color-srgb = lo_color_element->get_attribute( name = c_val ).
        when c_syscolor.
          rv_color-syscolor-val = lo_color_element->get_attribute( name = c_val ).
          rv_color-syscolor-lastclr = lo_color_element->get_attribute( name = c_lastclr ).
      endcase.
    endif.
  endmethod.                    "get_color


method load.
    data: lo_scheme_children type ref to if_ixml_node_list.
    data: lo_scheme_iterator type ref to if_ixml_node_iterator.
    data: lo_scheme_element type ref to if_ixml_element.
    check io_color_scheme  is not initial.

    name = io_color_scheme->get_attribute( name = c_name ).
    lo_scheme_children = io_color_scheme->get_children( ).
    lo_scheme_iterator = lo_scheme_children->create_iterator( ).
    lo_scheme_element ?= lo_scheme_iterator->get_next( ).
    while lo_scheme_element is bound.
      case lo_scheme_element->get_name( ).
        when c_dark1.
          dark1 = me->get_color( lo_scheme_element ).
        when c_dark2.
          dark2 = me->get_color( lo_scheme_element ).
        when c_light1.
          light1 = me->get_color( lo_scheme_element ).
        when c_light2.
          light2 = me->get_color( lo_scheme_element ).
        when c_accent1.
          accent1 = me->get_color( lo_scheme_element ).
        when c_accent2.
          accent2 = me->get_color( lo_scheme_element ).
        when c_accent3.
          accent3 = me->get_color( lo_scheme_element ).
        when c_accent4.
          accent4 = me->get_color( lo_scheme_element ).
        when c_accent5.
          accent5 = me->get_color( lo_scheme_element ).
        when c_accent6.
          accent6 = me->get_color( lo_scheme_element ).
        when c_hlink.
          hlink = me->get_color( lo_scheme_element ).
        when c_folhlink.
          folhlink = me->get_color( lo_scheme_element ).
      endcase.
      lo_scheme_element ?= lo_scheme_iterator->get_next( ).
    endwhile.
  endmethod.                    "load


method set_color.
    field-symbols: <color> type t_color.
    check iv_type is not initial.
    check iv_srgb is not initial or  iv_syscolorname is not initial.
    case iv_type.
      when c_dark1.
        assign dark1 to <color>.
      when c_dark2.
        assign dark2 to <color>.
      when c_light1.
        assign light1 to <color>.
      when c_light2.
        assign light2 to <color>.
      when c_accent1.
        assign accent1 to <color>.
      when c_accent2.
        assign accent2 to <color>.
      when c_accent3.
        assign accent3 to <color>.
      when c_accent4.
        assign accent4 to <color>.
      when c_accent5.
        assign accent5 to <color>.
      when c_accent6.
        assign accent6 to <color>.
      when c_hlink.
        assign hlink to <color>.
      when c_folhlink.
        assign folhlink to <color>.
    endcase.
    check <color> is assigned.
    clear <color>.
    if iv_srgb is not initial.
      <color>-srgb = iv_srgb.
    else.
      <color>-syscolor-val = iv_syscolorname.
      if iv_syscolorlast is not initial.
        <color>-syscolor-lastclr = iv_syscolorlast.
      else.
        <color>-syscolor-lastclr = '000000'.
      endif.
    endif.
  endmethod.                    "set_color


method set_defaults.
    name = 'Office'.
    dark1-syscolor-val = 'windowText'.
    dark1-syscolor-lastclr = '000000'.
    light1-syscolor-val = 'window'.
    light1-syscolor-lastclr = 'FFFFFF'.
    dark2-srgb = '44546A'.
    light2-srgb = 'E7E6E6'.
    accent1-srgb = '5B9BD5'.
    accent2-srgb = 'ED7D31'.
    accent3-srgb = 'A5A5A5'.
    accent4-srgb = 'FFC000'.
    accent5-srgb = '4472C4'.
    accent6-srgb = '70AD47'.
    hlink-srgb   = '0563C1'.
    folhlink-srgb = '954F72'.
  endmethod.                    "set_defaults


method set_name.
    if strlen( iv_name ) > 50.
      name = iv_name(50).
    else.
      name = iv_name.
    endif.
  endmethod.                    "set_name
ENDCLASS.