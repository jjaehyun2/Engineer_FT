class ZCL_EXCEL_THEME_FONT_SCHEME definition
  public
  final
  create public .

public section.
*"* public components of class ZCL_EXCEL_THEME_FONT_SCHEME
*"* do not include other source files here!!!

  types:
    begin of t_font,
            script type string,
            typeface type string,
            end of t_font .
  types:
    tt_font type sorted table of t_font with unique key script .
  types:
    begin of t_fonttype,
           typeface type string,
           panose type string,
           pitchfamily type string,
           charset type string,
           end of t_fonttype .
  types:
    begin of t_fonts,
           latin type t_fonttype,
           ea type t_fonttype,
           cs type t_fonttype,
           fonts type tt_font,
           end of t_fonts .
  types:
    begin of t_scheme,
           name type string,
           major type t_fonts,
           minor type t_fonts,
           end of t_scheme .

  constants C_NAME type STRING value 'name'. "#EC NOTEXT
  constants C_SCHEME type STRING value 'fontScheme'. "#EC NOTEXT
  constants C_MAJOR type STRING value 'majorFont'. "#EC NOTEXT
  constants C_MINOR type STRING value 'minorFont'. "#EC NOTEXT
  constants C_FONT type STRING value 'font'. "#EC NOTEXT
  constants C_LATIN type STRING value 'latin'. "#EC NOTEXT
  constants C_EA type STRING value 'ea'. "#EC NOTEXT
  constants C_CS type STRING value 'cs'. "#EC NOTEXT
  constants C_TYPEFACE type STRING value 'typeface'. "#EC NOTEXT
  constants C_PANOSE type STRING value 'panose'. "#EC NOTEXT
  constants C_PITCHFAMILY type STRING value 'pitchFamily'. "#EC NOTEXT
  constants C_CHARSET type STRING value 'charset'. "#EC NOTEXT
  constants C_SCRIPT type STRING value 'script'. "#EC NOTEXT

  methods LOAD
    importing
      !IO_FONT_SCHEME type ref to IF_IXML_ELEMENT .
  methods SET_NAME
    importing
      value(IV_NAME) type STRING .
  methods BUILD_XML
    importing
      !LO_OSTREAM type ref to IF_IXML_OSTREAM .
  methods MODIFY_FONT
    importing
      value(IV_TYPE) type STRING
      value(IV_SCRIPT) type STRING
      value(IV_TYPEFACE) type STRING .
  methods MODIFY_LATIN_FONT
    importing
      value(IV_TYPE) type STRING
      value(IV_TYPEFACE) type STRING
      value(IV_PANOSE) type STRING optional
      value(IV_PITCHFAMILY) type STRING optional
      value(IV_CHARSET) type STRING optional .
  methods MODIFY_EA_FONT
    importing
      value(IV_TYPE) type STRING
      value(IV_TYPEFACE) type STRING
      value(IV_PANOSE) type STRING optional
      value(IV_PITCHFAMILY) type STRING optional
      value(IV_CHARSET) type STRING optional .
  methods MODIFY_CS_FONT
    importing
      value(IV_TYPE) type STRING
      value(IV_TYPEFACE) type STRING
      value(IV_PANOSE) type STRING optional
      value(IV_PITCHFAMILY) type STRING optional
      value(IV_CHARSET) type STRING optional .
  methods CONSTRUCTOR .
protected section.

  methods MODIFY_LEC_FONTS
    importing
      value(IV_TYPE) type STRING
      value(IV_FONT_TYPE) type STRING
      value(IV_TYPEFACE) type STRING
      value(IV_PANOSE) type STRING optional
      value(IV_PITCHFAMILY) type STRING optional
      value(IV_CHARSET) type STRING optional .
private section.

  data FONT_SCHEME type T_SCHEME .

  methods SET_DEFAULTS .
ENDCLASS.



CLASS ZCL_EXCEL_THEME_FONT_SCHEME IMPLEMENTATION.


METHOD build_xml.
  FIELD-SYMBOLS: <font> TYPE t_font.

  lo_ostream->write_string( |<{ zcl_excel_theme=>c_theme_prefix }:{ zcl_excel_theme_elements=>c_font_scheme }| ).
  lo_ostream->write_string( | { c_name }="{ font_scheme-name }">| ).

  lo_ostream->write_string( |<{ zcl_excel_theme=>c_theme_prefix }:{ c_major }>| ).


  lo_ostream->write_string( |<{ zcl_excel_theme=>c_theme_prefix }:{ c_latin }| ).

  lo_ostream->write_string( | { c_typeface }="{ font_scheme-major-latin-typeface }"| ).

  IF font_scheme-major-latin-panose IS NOT INITIAL.
    lo_ostream->write_string( | { c_panose }="{ font_scheme-major-latin-panose }"| ).
  ENDIF.
  IF font_scheme-major-latin-pitchfamily IS NOT INITIAL.
    lo_ostream->write_string( | { c_pitchfamily }="{ font_scheme-major-latin-pitchfamily }"| ).
  ENDIF.
  IF font_scheme-major-latin-charset IS NOT INITIAL.
    lo_ostream->write_string( | { c_charset }="{ font_scheme-major-latin-charset }"| ).
  ENDIF.

  lo_ostream->write_string( |/>| ).


  lo_ostream->write_string( |<{ zcl_excel_theme=>c_theme_prefix }:{ c_ea }| ).

  lo_ostream->write_string( | { c_typeface }="{ font_scheme-major-ea-typeface }"| ).

  IF font_scheme-major-ea-panose IS NOT INITIAL.
    lo_ostream->write_string( | { c_panose }="{ font_scheme-major-ea-panose }"| ).
  ENDIF.
  IF font_scheme-major-ea-pitchfamily IS NOT INITIAL.
    lo_ostream->write_string( | { c_pitchfamily }="{ font_scheme-major-ea-pitchfamily }"| ).
  ENDIF.
  IF font_scheme-major-ea-charset IS NOT INITIAL.
    lo_ostream->write_string( | { c_charset }="{ font_scheme-major-ea-charset }"| ).
  ENDIF.

  lo_ostream->write_string( |/>| ).

  lo_ostream->write_string( |<{ zcl_excel_theme=>c_theme_prefix }:{ c_cs }| ).

  lo_ostream->write_string( | { c_typeface }="{ font_scheme-major-cs-typeface }"| ).

  IF font_scheme-major-cs-panose IS NOT INITIAL.
    lo_ostream->write_string( | { c_panose }="{ font_scheme-major-cs-panose }"| ).
  ENDIF.
  IF font_scheme-major-cs-pitchfamily IS NOT INITIAL.
    lo_ostream->write_string( | { c_pitchfamily }="{ font_scheme-major-cs-pitchfamily }"| ).
  ENDIF.
  IF font_scheme-major-cs-charset IS NOT INITIAL.
    lo_ostream->write_string( | { c_charset }="{ font_scheme-major-ea-charset }"| ).
  ENDIF.

  lo_ostream->write_string( |/>| ).

  LOOP AT font_scheme-major-fonts ASSIGNING <font>.
    IF <font>-script IS NOT INITIAL AND <font>-typeface IS NOT INITIAL.
      lo_ostream->write_string( |<{ zcl_excel_theme=>c_theme_prefix }:{ c_font }| ).
      lo_ostream->write_string( | { c_script }="{ <font>-script }"| ).
      lo_ostream->write_string( | { c_typeface }="{ <font>-typeface }"/>| ).
    ENDIF.
  ENDLOOP.

  lo_ostream->write_string( |</{ zcl_excel_theme=>c_theme_prefix }:{ c_major }>| ).

  lo_ostream->write_string( |<{ zcl_excel_theme=>c_theme_prefix }:{ c_minor }>| ).


  lo_ostream->write_string( |<{ zcl_excel_theme=>c_theme_prefix }:{ c_latin }| ).

  lo_ostream->write_string( | { c_typeface }="{ font_scheme-minor-latin-typeface }"| ).

  IF font_scheme-minor-latin-panose IS NOT INITIAL.
    lo_ostream->write_string( | { c_panose }="{ font_scheme-minor-latin-panose }"| ).
  ENDIF.
  IF font_scheme-minor-latin-pitchfamily IS NOT INITIAL.
    lo_ostream->write_string( | { c_pitchfamily }="{ font_scheme-minor-latin-pitchfamily }"| ).
  ENDIF.
  IF font_scheme-minor-latin-charset IS NOT INITIAL.
    lo_ostream->write_string( | { c_charset }="{ font_scheme-minor-latin-charset }"| ).
  ENDIF.

  lo_ostream->write_string( |/>| ).


  lo_ostream->write_string( |<{ zcl_excel_theme=>c_theme_prefix }:{ c_ea }| ).

  lo_ostream->write_string( | { c_typeface }="{ font_scheme-minor-ea-typeface }"| ).

  IF font_scheme-minor-ea-panose IS NOT INITIAL.
    lo_ostream->write_string( | { c_panose }="{ font_scheme-minor-ea-panose }"| ).
  ENDIF.
  IF font_scheme-minor-ea-pitchfamily IS NOT INITIAL.
    lo_ostream->write_string( | { c_pitchfamily }="{ font_scheme-minor-ea-pitchfamily }"| ).
  ENDIF.
  IF font_scheme-minor-ea-charset IS NOT INITIAL.
    lo_ostream->write_string( | { c_charset }="{ font_scheme-minor-ea-charset }"| ).
  ENDIF.

  lo_ostream->write_string( |/>| ).

  lo_ostream->write_string( |<{ zcl_excel_theme=>c_theme_prefix }:{ c_cs }| ).

  lo_ostream->write_string( | { c_typeface }="{ font_scheme-minor-cs-typeface }"| ).

  IF font_scheme-minor-cs-panose IS NOT INITIAL.
    lo_ostream->write_string( | { c_panose }="{ font_scheme-minor-cs-panose }"| ).
  ENDIF.
  IF font_scheme-minor-cs-pitchfamily IS NOT INITIAL.
    lo_ostream->write_string( | { c_pitchfamily }="{ font_scheme-minor-cs-pitchfamily }"| ).
  ENDIF.
  IF font_scheme-minor-cs-charset IS NOT INITIAL.
    lo_ostream->write_string( | { c_charset }="{ font_scheme-minor-ea-charset }"| ).
  ENDIF.

  lo_ostream->write_string( |/>| ).

  LOOP AT font_scheme-minor-fonts ASSIGNING <font>.
    IF <font>-script IS NOT INITIAL AND <font>-typeface IS NOT INITIAL.
      lo_ostream->write_string( |<{ zcl_excel_theme=>c_theme_prefix }:{ c_font }| ).
      lo_ostream->write_string( | { c_script }="{ <font>-script }"| ).
      lo_ostream->write_string( | { c_typeface }="{ <font>-typeface }"/>| ).
    ENDIF.
  ENDLOOP.

  lo_ostream->write_string( |</{ zcl_excel_theme=>c_theme_prefix }:{ c_minor }>| ).

  lo_ostream->write_string( |</{ zcl_excel_theme=>c_theme_prefix }:{ zcl_excel_theme_elements=>c_font_scheme }>| ).

ENDMETHOD.                    "build_xml


method constructor.
    set_defaults( ).
  endmethod.                    "constructor


method load.
    data: lo_scheme_children type ref to if_ixml_node_list.
    data: lo_scheme_iterator type ref to if_ixml_node_iterator.
    data: lo_scheme_element type ref to if_ixml_element.
    data: lo_major_children type ref to if_ixml_node_list.
    data: lo_major_iterator type ref to if_ixml_node_iterator.
    data: lo_major_element type ref to if_ixml_element.
    data: lo_minor_children type ref to if_ixml_node_list.
    data: lo_minor_iterator type ref to if_ixml_node_iterator.
    data: lo_minor_element type ref to if_ixml_element.
    data: ls_font type t_font.
    check io_font_scheme is not initial.
    clear font_scheme.
    font_scheme-name =  io_font_scheme->get_attribute( name = c_name ).
    lo_scheme_children = io_font_scheme->get_children( ).
    lo_scheme_iterator = lo_scheme_children->create_iterator( ).
    lo_scheme_element ?= lo_scheme_iterator->get_next( ).
    while lo_scheme_element is bound.
      case lo_scheme_element->get_name( ).
        when c_major.
          lo_major_children = lo_scheme_element->get_children( ).
          lo_major_iterator = lo_major_children->create_iterator( ).
          lo_major_element ?= lo_major_iterator->get_next( ).
          while lo_major_element is bound.
            case lo_major_element->get_name( ).
              when c_latin.
                font_scheme-major-latin-typeface = lo_major_element->get_attribute(  name = c_typeface ).
                font_scheme-major-latin-panose = lo_major_element->get_attribute(  name = c_panose ).
                font_scheme-major-latin-pitchfamily = lo_major_element->get_attribute(  name = c_pitchfamily ).
                font_scheme-major-latin-charset = lo_major_element->get_attribute(  name = c_charset ).
              when c_ea.
                font_scheme-major-ea-typeface = lo_major_element->get_attribute(  name = c_typeface ).
                font_scheme-major-ea-panose = lo_major_element->get_attribute(  name = c_panose ).
                font_scheme-major-ea-pitchfamily = lo_major_element->get_attribute(  name = c_pitchfamily ).
                font_scheme-major-ea-charset = lo_major_element->get_attribute(  name = c_charset ).
              when c_cs.
                font_scheme-major-cs-typeface = lo_major_element->get_attribute(  name = c_typeface ).
                font_scheme-major-cs-panose = lo_major_element->get_attribute(  name = c_panose ).
                font_scheme-major-cs-pitchfamily = lo_major_element->get_attribute(  name = c_pitchfamily ).
                font_scheme-major-cs-charset = lo_major_element->get_attribute(  name = c_charset ).
              when c_font.
                clear ls_font.
                ls_font-script = lo_major_element->get_attribute(  name = c_script ).
                ls_font-typeface = lo_major_element->get_attribute(  name = c_typeface ).
                try.
                    insert ls_font into table font_scheme-major-fonts.
                  catch cx_root. "not the best but just to avoid duplicate lines dump

                endtry.
            endcase.
            lo_major_element ?= lo_major_iterator->get_next( ).
          endwhile.
        when c_minor.
          lo_minor_children = lo_scheme_element->get_children( ).
          lo_minor_iterator = lo_minor_children->create_iterator( ).
          lo_minor_element ?= lo_minor_iterator->get_next( ).
          while lo_minor_element is bound.
            case lo_minor_element->get_name( ).
              when c_latin.
                font_scheme-minor-latin-typeface = lo_minor_element->get_attribute(  name = c_typeface ).
                font_scheme-minor-latin-panose = lo_minor_element->get_attribute(  name = c_panose ).
                font_scheme-minor-latin-pitchfamily = lo_minor_element->get_attribute(  name = c_pitchfamily ).
                font_scheme-minor-latin-charset = lo_minor_element->get_attribute(  name = c_charset ).
              when c_ea.
                font_scheme-minor-ea-typeface = lo_minor_element->get_attribute(  name = c_typeface ).
                font_scheme-minor-ea-panose = lo_minor_element->get_attribute(  name = c_panose ).
                font_scheme-minor-ea-pitchfamily = lo_minor_element->get_attribute(  name = c_pitchfamily ).
                font_scheme-minor-ea-charset = lo_minor_element->get_attribute(  name = c_charset ).
              when c_cs.
                font_scheme-minor-cs-typeface = lo_minor_element->get_attribute(  name = c_typeface ).
                font_scheme-minor-cs-panose = lo_minor_element->get_attribute(  name = c_panose ).
                font_scheme-minor-cs-pitchfamily = lo_minor_element->get_attribute(  name = c_pitchfamily ).
                font_scheme-minor-cs-charset = lo_minor_element->get_attribute(  name = c_charset ).
              when c_font.
                clear ls_font.
                ls_font-script = lo_minor_element->get_attribute(  name = c_script ).
                ls_font-typeface = lo_minor_element->get_attribute(  name = c_typeface ).
                try.
                    insert ls_font into table font_scheme-minor-fonts.
                  catch cx_root. "not the best but just to avoid duplicate lines dump

                endtry.
            endcase.
            lo_minor_element ?= lo_minor_iterator->get_next( ).
          endwhile.
      endcase.
      lo_scheme_element ?= lo_scheme_iterator->get_next( ).
    endwhile.
  endmethod.                    "load


method modify_cs_font.
    modify_lec_fonts(
      exporting
        iv_type        = iv_type
        iv_font_type   = c_cs
        iv_typeface    = iv_typeface
        iv_panose      = iv_panose
        iv_pitchfamily = iv_pitchfamily
        iv_charset     = iv_charset
    ).
  endmethod.                    "modify_latin_font


method modify_ea_font.
    modify_lec_fonts(
      exporting
        iv_type        = iv_type
        iv_font_type   = c_ea
        iv_typeface    = iv_typeface
        iv_panose      = iv_panose
        iv_pitchfamily = iv_pitchfamily
        iv_charset     = iv_charset
    ).
  endmethod.                    "modify_latin_font


method modify_font.
    data: ls_font type t_font.
    field-symbols: <font> type t_font.
    ls_font-script = iv_script.
    ls_font-typeface = iv_typeface.
    try.
        case iv_type.
          when c_major.
            read table font_scheme-major-fonts with key script = iv_script assigning <font>.
            if sy-subrc eq 0.
              <font> = ls_font.
            else.
              insert ls_font into table font_scheme-major-fonts.
            endif.
          when c_minor.
            read table font_scheme-minor-fonts with key script = iv_script assigning <font>.
            if sy-subrc eq 0.
              <font> = ls_font.
            else.
              insert ls_font into table font_scheme-minor-fonts.
            endif.
        endcase.
      catch cx_root. "not the best but just to avoid duplicate lines dump
    endtry.
  endmethod.                    "add_font


method modify_latin_font.
    modify_lec_fonts(
      exporting
        iv_type        = iv_type
        iv_font_type   = c_latin
        iv_typeface    = iv_typeface
        iv_panose      = iv_panose
        iv_pitchfamily = iv_pitchfamily
        iv_charset     = iv_charset
    ).
  endmethod.                    "modify_latin_font


method modify_lec_fonts.
    field-symbols: <type> type t_fonts,
                   <font> type t_fonttype.
    case iv_type.
      when c_minor.
        assign font_scheme-minor to <type>.
      when c_major.
        assign font_scheme-major to <type>.
      when others.
        return.
    endcase.
    check <type> is assigned.
    case iv_font_type.
      when c_latin.
        assign <type>-latin to <font>.
      when c_ea.
        assign <type>-ea to <font>.
      when c_cs.
        assign <type>-cs to <font>.
      when others.
        return.
    endcase.
    check <font> is assigned.
    <font>-typeface = iv_typeface.
    <font>-panose = iv_panose.
    <font>-pitchfamily = iv_pitchfamily.
    <font>-charset = iv_charset.
  endmethod.                    "modify_lec_fonts


method set_defaults.
    clear font_scheme.
    font_scheme-name = 'Office'.
    font_scheme-major-latin-typeface = 'Calibri Light'.
    font_scheme-major-latin-panose = '020F0302020204030204'.
    modify_font( iv_type = c_major iv_script = 'Jpan' iv_typeface = 'ＭＳ Ｐゴシック' ).
    modify_font( iv_type = c_major iv_script = 'Hang' iv_typeface = '맑은 고딕' ).
    modify_font( iv_type = c_major iv_script = 'Hans' iv_typeface = '宋体' ).
    modify_font( iv_type = c_major iv_script = 'Hant' iv_typeface = '新細明體' ).
    modify_font( iv_type = c_major iv_script = 'Arab' iv_typeface = 'Times New Roman' ).
    modify_font( iv_type = c_major iv_script = 'Hebr' iv_typeface = 'Times New Roman' ).
    modify_font( iv_type = c_major iv_script = 'Thai' iv_typeface = 'Tahoma' ).
    modify_font( iv_type = c_major iv_script = 'Ethi' iv_typeface = 'Nyala' ).
    modify_font( iv_type = c_major iv_script = 'Beng' iv_typeface = 'Vrinda' ).
    modify_font( iv_type = c_major iv_script = 'Gujr' iv_typeface = 'Shruti' ).
    modify_font( iv_type = c_major iv_script = 'Khmr' iv_typeface = 'MoolBoran' ).
    modify_font( iv_type = c_major iv_script = 'Knda' iv_typeface = 'Tunga' ).
    modify_font( iv_type = c_major iv_script = 'Guru' iv_typeface = 'Raavi' ).
    modify_font( iv_type = c_major iv_script = 'Cans' iv_typeface = 'Euphemia' ).
    modify_font( iv_type = c_major iv_script = 'Cher' iv_typeface = 'Plantagenet Cherokee' ).
    modify_font( iv_type = c_major iv_script = 'Yiii' iv_typeface = 'Microsoft Yi Baiti' ).
    modify_font( iv_type = c_major iv_script = 'Tibt' iv_typeface = 'Microsoft Himalaya' ).
    modify_font( iv_type = c_major iv_script = 'Thaa' iv_typeface = 'MV Boli' ).
    modify_font( iv_type = c_major iv_script = 'Deva' iv_typeface = 'Mangal' ).
    modify_font( iv_type = c_major iv_script = 'Telu' iv_typeface = 'Gautami' ).
    modify_font( iv_type = c_major iv_script = 'Taml' iv_typeface = 'Latha' ).
    modify_font( iv_type = c_major iv_script = 'Syrc' iv_typeface = 'Estrangelo Edessa' ).
    modify_font( iv_type = c_major iv_script = 'Orya' iv_typeface = 'Kalinga' ).
    modify_font( iv_type = c_major iv_script = 'Mlym' iv_typeface = 'Kartika' ).
    modify_font( iv_type = c_major iv_script = 'Laoo' iv_typeface = 'DokChampa' ).
    modify_font( iv_type = c_major iv_script = 'Sinh' iv_typeface = 'Iskoola Pota' ).
    modify_font( iv_type = c_major iv_script = 'Mong' iv_typeface = 'Mongolian Baiti' ).
    modify_font( iv_type = c_major iv_script = 'Viet' iv_typeface = 'Times New Roman' ).
    modify_font( iv_type = c_major iv_script = 'Uigh' iv_typeface = 'Microsoft Uighur' ).
    modify_font( iv_type = c_major iv_script = 'Geor' iv_typeface = 'Sylfaen' ).

    font_scheme-minor-latin-typeface = 'Calibri'.
    font_scheme-minor-latin-panose = '020F0502020204030204'.
    modify_font( iv_type = c_minor iv_script = 'Jpan' iv_typeface = 'ＭＳ Ｐゴシック' ).
    modify_font( iv_type = c_minor iv_script = 'Hang' iv_typeface = '맑은 고딕' ).
    modify_font( iv_type = c_minor iv_script = 'Hans' iv_typeface = '宋体' ).
    modify_font( iv_type = c_minor iv_script = 'Hant' iv_typeface = '新細明體' ).
    modify_font( iv_type = c_minor iv_script = 'Arab' iv_typeface = 'Arial' ).
    modify_font( iv_type = c_minor iv_script = 'Hebr' iv_typeface = 'Arial' ).
    modify_font( iv_type = c_minor iv_script = 'Thai' iv_typeface = 'Tahoma' ).
    modify_font( iv_type = c_minor iv_script = 'Ethi' iv_typeface = 'Nyala' ).
    modify_font( iv_type = c_minor iv_script = 'Beng' iv_typeface = 'Vrinda' ).
    modify_font( iv_type = c_minor iv_script = 'Gujr' iv_typeface = 'Shruti' ).
    modify_font( iv_type = c_minor iv_script = 'Khmr' iv_typeface = 'DaunPenh' ).
    modify_font( iv_type = c_minor iv_script = 'Knda' iv_typeface = 'Tunga' ).
    modify_font( iv_type = c_minor iv_script = 'Guru' iv_typeface = 'Raavi' ).
    modify_font( iv_type = c_minor iv_script = 'Cans' iv_typeface = 'Euphemia' ).
    modify_font( iv_type = c_minor iv_script = 'Cher' iv_typeface = 'Plantagenet Cherokee' ).
    modify_font( iv_type = c_minor iv_script = 'Yiii' iv_typeface = 'Microsoft Yi Baiti' ).
    modify_font( iv_type = c_minor iv_script = 'Tibt' iv_typeface = 'Microsoft Himalaya' ).
    modify_font( iv_type = c_minor iv_script = 'Thaa' iv_typeface = 'MV Boli' ).
    modify_font( iv_type = c_minor iv_script = 'Deva' iv_typeface = 'Mangal' ).
    modify_font( iv_type = c_minor iv_script = 'Telu' iv_typeface = 'Gautami' ).
    modify_font( iv_type = c_minor iv_script = 'Taml' iv_typeface = 'Latha' ).
    modify_font( iv_type = c_minor iv_script = 'Syrc' iv_typeface = 'Estrangelo Edessa' ).
    modify_font( iv_type = c_minor iv_script = 'Orya' iv_typeface = 'Kalinga' ).
    modify_font( iv_type = c_minor iv_script = 'Mlym' iv_typeface = 'Kartika' ).
    modify_font( iv_type = c_minor iv_script = 'Laoo' iv_typeface = 'DokChampa' ).
    modify_font( iv_type = c_minor iv_script = 'Sinh' iv_typeface = 'Iskoola Pota' ).
    modify_font( iv_type = c_minor iv_script = 'Mong' iv_typeface = 'Mongolian Baiti' ).
    modify_font( iv_type = c_minor iv_script = 'Viet' iv_typeface = 'Arial' ).
    modify_font( iv_type = c_minor iv_script = 'Uigh' iv_typeface = 'Microsoft Uighur' ).
    modify_font( iv_type = c_minor iv_script = 'Geor' iv_typeface = 'Sylfaen' ).

  endmethod.                    "set_defaults


method set_name.
    font_scheme-name = iv_name.
  endmethod.                    "set_name
ENDCLASS.