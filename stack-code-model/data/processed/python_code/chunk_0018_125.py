class /ENSX/CL_RE_XSLT_PROCESSOR definition
  public
  create public .

*"* public components of class /ENSX/CL_RE_XSLT_PROCESSOR
*"* do not include other source files here!!!
*"* protected components of class CL_IXML_UTILITY
*"* do not include other source files here!!!
public section.

  class-methods PARSE_TO_DOCUMENT
    importing
      !STREAM_XSTRING type XSTRING optional
      !STREAM_STRING type STRING optional
      !STREAM_TABLE type STANDARD TABLE optional
      !STREAM_TABLE_SIZE type I optional
      !UN_PRETTY_PRINT type I default 0
      !NAMESPACE_AWARE type I default 1
      !VALIDATING type I default 0
    returning
      value(DOCUMENT) type ref to IF_IXML_DOCUMENT
    raising
      CX_XSLT_EXCEPTION .
  class-methods RENDER_TO_STRING
    importing
      !DOCUMENT type ref to IF_IXML_DOCUMENT
      !PRETTY_PRINT type I default 0
      value(ENCODING) type STRING optional
    returning
      value(STREAM_STRING) type STRING
    raising
      CX_XSLT_EXCEPTION .
  class-methods RENDER_TO_TABLE_OF_C
    importing
      !DOCUMENT type ref to IF_IXML_DOCUMENT
      !PRETTY_PRINT type I default 0
      value(ENCODING) type STRING optional
    exporting
      value(STREAM_TABLE) type STANDARD TABLE
      !STREAM_TABLE_SIZE type I
    raising
      CX_XSLT_EXCEPTION .
  class-methods RENDER_TO_TABLE_OF_X
    importing
      !DOCUMENT type ref to IF_IXML_DOCUMENT
      !PRETTY_PRINT type I default 0
      value(ENCODING) type STRING optional
    exporting
      value(STREAM_TABLE) type STANDARD TABLE
      !STREAM_TABLE_SIZE type I
    raising
      CX_XSLT_EXCEPTION .
  class-methods RENDER_TO_XSTRING
    importing
      !DOCUMENT type ref to IF_IXML_DOCUMENT
      !PRETTY_PRINT type I default 0
      value(ENCODING) type STRING optional
    returning
      value(STREAM_XSTRING) type XSTRING
    raising
      CX_XSLT_EXCEPTION .
  class-methods XSL_TRANSFORM_DOCUMENT
    importing
      !XML type ref to IF_IXML_DOCUMENT
      !XSLT type PROGNAME
    returning
      value(OUTPUT) type ref to IF_IXML_DOCUMENT
    raising
      CX_XSLT_EXCEPTION .
  class-methods XSL_TRANSFORM_STRING
    importing
      !XML type STRING
      !XSLT type PROGNAME
      value(RESULT_ENCODING) type STRING optional
    returning
      value(RESULT) type STRING
    raising
      CX_XSLT_EXCEPTION .
  class-methods XSL_TRANSFORM_TABLE_OF_C
    importing
      !XML type STANDARD TABLE
      !XML_SIZE type I
      !XSLT type PROGNAME
      value(RESULT_ENCODING) type STRING optional
    exporting
      value(RESULT) type STANDARD TABLE
      !RESULT_SIZE type I
    raising
      CX_XSLT_EXCEPTION .
  class-methods XSL_TRANSFORM_TABLE_OF_X
    importing
      !XML type STANDARD TABLE
      !XML_SIZE type I
      !XSLT type PROGNAME
      value(RESULT_ENCODING) type STRING optional
    exporting
      value(RESULT) type STANDARD TABLE
      !RESULT_SIZE type I
    raising
      CX_XSLT_EXCEPTION .
  class-methods XSL_TRANSFORM_XSTRING
    importing
      !XML type XSTRING
      !XSLT type PROGNAME
      value(RESULT_ENCODING) type STRING optional
    returning
      value(RESULT) type XSTRING
    raising
      CX_XSLT_EXCEPTION
      CX_IXML_EXCEPTION .
  PROTECTED SECTION.
*"* private components of class /ENSX/CL_RE_XSLT_PROCESSOR
*"* do not include other source files here!!!
  PRIVATE SECTION.

    CLASS-DATA c_ixml TYPE REF TO if_ixml .
    CLASS-DATA c_ixml_stream_factory TYPE REF TO if_ixml_stream_factory .
    CLASS-DATA c_xslt_processor TYPE REF TO cl_xslt_processor .

    CLASS-METHODS init_ixml .
    CLASS-METHODS init_xslt .
ENDCLASS.



CLASS /ENSX/CL_RE_XSLT_PROCESSOR IMPLEMENTATION.


  METHOD init_ixml .


* uses ****************************************************************

    CLASS cl_ixml DEFINITION LOAD.


* data ****************************************************************



* code ****************************************************************


* initialized already?
    IF c_ixml IS NOT INITIAL. RETURN. ENDIF.


* initialize otherwise
    c_ixml = cl_ixml=>create( ).
    IF c_ixml IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml'.                           "#EC NOTEXT
    ENDIF.

    c_ixml_stream_factory = c_ixml->create_stream_factory( ).
    IF c_ixml_stream_factory IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_stream_factory'.            "#EC NOTEXT
    ENDIF.


  ENDMETHOD.


  METHOD init_xslt .


* uses ****************************************************************

    CLASS cl_ixml DEFINITION LOAD.


* data ****************************************************************



* code ****************************************************************


* XSLT initialized already?
    IF c_xslt_processor IS NOT INITIAL. RETURN. ENDIF.


* iXML initialized already?
    IF c_ixml IS INITIAL. init_ixml( ). ENDIF.


* initialize otherwise
    CREATE OBJECT c_xslt_processor.


  ENDMETHOD.


  METHOD parse_to_document .


* uses
****************************************************************


* data
****************************************************************

    DATA: l_ixml_document TYPE REF TO if_ixml_document,
          l_ixml_stream   TYPE REF TO if_ixml_istream,
          l_ixml_parser   TYPE REF TO if_ixml_parser.


* code
****************************************************************


* initialized already?
    IF c_ixml IS INITIAL. init_ixml( ). ENDIF.


* any stream supplied?
    IF stream_string  IS NOT SUPPLIED AND
       stream_xstring IS NOT SUPPLIED AND
       stream_table   IS NOT SUPPLIED.
      RAISE EXCEPTION TYPE cx_ixml_inv_arg
        EXPORTING
          argument = 'stream_*'.                 "#EC NOTEXT
    ENDIF.

    IF stream_string IS SUPPLIED.
      IF stream_string IS INITIAL.
        RAISE EXCEPTION TYPE cx_ixml_inv_arg
          EXPORTING
            argument = 'stream_string'.          "#EC NOTEXT
      ENDIF.
*   get istream
      l_ixml_stream = c_ixml_stream_factory->create_istream_cstring(
        stream_string ).


    ELSEIF stream_xstring IS SUPPLIED.
      IF stream_xstring IS INITIAL.
        RAISE EXCEPTION TYPE cx_ixml_inv_arg
          EXPORTING
            argument = 'stream_xstring'.         "#EC NOTEXT
      ENDIF.
*   get istream
      l_ixml_stream = c_ixml_stream_factory->create_istream_xstring(
        stream_xstring ).


    ELSEIF stream_table IS SUPPLIED.
      IF stream_table IS INITIAL.
        RAISE EXCEPTION TYPE cx_ixml_inv_arg
          EXPORTING
            argument = 'stream_table'.           "#EC NOTEXT
      ENDIF.
*   get istream
      l_ixml_stream = c_ixml_stream_factory->create_istream_itable(
        table = stream_table
        size  = stream_table_size ).
    ENDIF.

    IF l_ixml_stream IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_istream'.              "#EC NOTEXT
    ENDIF.


* get document
    l_ixml_document = c_ixml->create_document( ).
    IF l_ixml_document IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_document'.             "#EC NOTEXT
    ENDIF.


* get parser
    l_ixml_parser = c_ixml->create_parser(
      document       = l_ixml_document
      istream        = l_ixml_stream
      stream_factory = c_ixml_stream_factory ).
    IF l_ixml_parser IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_parser'.               "#EC NOTEXT
    ENDIF.


* parse ...
    IF un_pretty_print IS INITIAL.
      l_ixml_parser->set_normalizing( is_normalizing = ' ' ).
    ELSE.
      l_ixml_parser->set_normalizing( is_normalizing = 'X' ).
    ENDIF.

    IF validating IS NOT INITIAL.
      l_ixml_parser->set_validating( ).
    ENDIF.

    IF namespace_aware = 0.
      l_ixml_parser->set_namespace_mode(
        mode = if_ixml_parser=>co_namespace_unaware ).
    ELSE.
      l_ixml_parser->set_namespace_mode(
        mode = if_ixml_parser=>co_namespace_aware ).
    ENDIF.

    IF l_ixml_parser->parse( ) NE 0.

*   errors!
      IF l_ixml_parser->num_errors( ) NE 0.
        DATA: l_parse_error TYPE REF TO if_ixml_parse_error,
              l_reason      TYPE string,
              l_code        TYPE i,
              l_line        TYPE i,
              l_column      TYPE i.

        l_parse_error = l_ixml_parser->get_error( index = 0 ).
        l_code   = l_parse_error->get_number( ).
        l_line   = l_parse_error->get_line( ).
        l_column = l_parse_error->get_column( ).
        l_reason = l_parse_error->get_reason( ).

        RAISE EXCEPTION TYPE cx_ixml_parse_error
          EXPORTING
            code   = l_code
            reason = l_reason
            line   = l_line
            column = l_column.
      ENDIF.
    ENDIF.


    document = l_ixml_document.


  ENDMETHOD.


  METHOD render_to_string .


* uses
****************************************************************


* data
****************************************************************

    DATA: l_ixml_stream   TYPE REF TO if_ixml_ostream,
          l_ixml_renderer TYPE REF TO if_ixml_renderer,
          l_ixml_encoding TYPE REF TO if_ixml_encoding.


* code
****************************************************************


* initialized already?
    IF c_ixml IS INITIAL. init_ixml( ). ENDIF.


* empty stream?
    IF document IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inv_arg
        EXPORTING
          argument = 'document'.                 "#EC NOTEXT
    ENDIF.


* get encoding
    DATA: l_c             TYPE c,
          l_len           TYPE i.

    IF encoding IS INITIAL.
      DESCRIBE FIELD l_c LENGTH l_len IN BYTE MODE.
      IF l_len = 1.
        encoding = 'utf-8'.                                 "#EC NOTEXT
      ELSE.
        encoding = 'utf-16'.                                "#EC NOTEXT
      ENDIF.
    ENDIF.
    l_ixml_encoding = c_ixml->create_encoding(
      character_set = encoding
      byte_order    = 0 ).
    IF l_ixml_encoding IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_encoding'.             "#EC NOTEXT
    ENDIF.


* get ostream
    l_ixml_stream = c_ixml_stream_factory->create_ostream_cstring(
      stream_string ).
    IF l_ixml_stream IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_ostream'.              "#EC NOTEXT
    ENDIF.
    l_ixml_stream->set_encoding( encoding = l_ixml_encoding ).


* get renderer
    l_ixml_renderer = c_ixml->create_renderer(
      document = document
      ostream  = l_ixml_stream
    ).
    IF l_ixml_renderer IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_renderer'.             "#EC NOTEXT
    ENDIF.


* render now
    IF pretty_print IS INITIAL.
      l_ixml_renderer->set_normalizing( is_normalizing = ' ' ).
    ELSE.
      l_ixml_renderer->set_normalizing( is_normalizing = 'X' ).
    ENDIF.

    l_ixml_renderer->render(  ).


  ENDMETHOD.


  METHOD render_to_table_of_c .


* uses
****************************************************************


* data
****************************************************************

    DATA: l_ixml_stream   TYPE REF TO if_ixml_ostream,
          l_ixml_renderer TYPE REF TO if_ixml_renderer,
          l_ixml_encoding TYPE REF TO if_ixml_encoding.

* code
****************************************************************


* initialized already?
    IF c_ixml IS INITIAL. init_ixml( ). ENDIF.


* empty stream?
    IF document IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inv_arg
        EXPORTING
          argument = 'document'.                 "#EC NOTEXT
    ENDIF.


* get encoding
    DATA: l_c             TYPE c,
          l_len           TYPE i.

    IF encoding IS INITIAL.
      DESCRIBE FIELD l_c LENGTH l_len IN BYTE MODE.
      IF l_len = 1.
        encoding = 'utf-8'.                                 "#EC NOTEXT
      ELSE.
        encoding = 'utf-16'.                                "#EC NOTEXT
      ENDIF.
    ENDIF.
    l_ixml_encoding = c_ixml->create_encoding(
      character_set = encoding
      byte_order    = 0 ).
    IF l_ixml_encoding IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_encoding'.             "#EC NOTEXT
    ENDIF.


* get ostream
    l_ixml_stream = c_ixml_stream_factory->create_ostream_itable(
      stream_table ).
    IF l_ixml_stream IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_ostream'.              "#EC NOTEXT
    ENDIF.
    l_ixml_stream->set_encoding( encoding = l_ixml_encoding ).


* get renderer
    l_ixml_renderer = c_ixml->create_renderer(
      document = document
      ostream  = l_ixml_stream
    ).
    IF l_ixml_renderer IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_renderer'.             "#EC NOTEXT
    ENDIF.


* render now
    IF pretty_print IS INITIAL.
      l_ixml_renderer->set_normalizing( is_normalizing = ' ' ).
    ELSE.
      l_ixml_renderer->set_normalizing( is_normalizing = 'X' ).
    ENDIF.

    l_ixml_renderer->render(  ).


* get number of bytes written
    stream_table_size = l_ixml_stream->get_num_written_raw( ).


  ENDMETHOD.


  METHOD render_to_table_of_x .


* uses
****************************************************************


* data
****************************************************************

    DATA: l_ixml_stream   TYPE REF TO if_ixml_ostream,
          l_ixml_renderer TYPE REF TO if_ixml_renderer,
          l_ixml_encoding TYPE REF TO if_ixml_encoding.

* code
****************************************************************


* initialized already?
    IF c_ixml IS INITIAL. init_ixml( ). ENDIF.


* empty stream?
    IF document IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inv_arg
        EXPORTING
          argument = 'document'.                 "#EC NOTEXT
    ENDIF.


* get encoding
    IF encoding IS INITIAL.
      encoding = 'utf-8'.                                   "#EC NOTEXT
    ENDIF.
    l_ixml_encoding = c_ixml->create_encoding(
      character_set = encoding
      byte_order    = 0 ).
    IF l_ixml_encoding IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_encoding'.             "#EC NOTEXT
    ENDIF.


* get ostream
    l_ixml_stream = c_ixml_stream_factory->create_ostream_itable(
      stream_table ).
    IF l_ixml_stream IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_ostream'.              "#EC NOTEXT
    ENDIF.
    l_ixml_stream->set_encoding( encoding = l_ixml_encoding ).


* get renderer
    l_ixml_renderer = c_ixml->create_renderer(
      document = document
      ostream  = l_ixml_stream
    ).
    IF l_ixml_renderer IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_renderer'.             "#EC NOTEXT
    ENDIF.


* render now
    IF pretty_print IS INITIAL.
      l_ixml_renderer->set_normalizing( is_normalizing = ' ' ).
    ELSE.
      l_ixml_renderer->set_normalizing( is_normalizing = 'X' ).
    ENDIF.

    l_ixml_renderer->render(  ).


* get number of bytes written
    stream_table_size = l_ixml_stream->get_num_written_raw( ).


  ENDMETHOD.


  METHOD render_to_xstring .


* uses
****************************************************************


* data
****************************************************************

    DATA: l_ixml_stream   TYPE REF TO if_ixml_ostream,
          l_ixml_renderer TYPE REF TO if_ixml_renderer,
          l_ixml_encoding TYPE REF TO if_ixml_encoding.


* code
****************************************************************


* initialized already?
    IF c_ixml IS INITIAL. init_ixml( ). ENDIF.


* empty stream?
    IF document IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inv_arg
        EXPORTING
          argument = 'document'.                 "#EC NOTEXT
    ENDIF.


* get encoding
    IF encoding IS INITIAL.
      encoding = 'utf-8'.                                   "#EC NOTEXT
    ENDIF.
    l_ixml_encoding = c_ixml->create_encoding(
      character_set = encoding
      byte_order    = 0 ).
    IF l_ixml_encoding IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_encoding'.             "#EC NOTEXT
    ENDIF.


* get ostream
    l_ixml_stream = c_ixml_stream_factory->create_ostream_xstring(
      stream_xstring ).
    IF l_ixml_stream IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_ostream'.              "#EC NOTEXT
    ENDIF.
    l_ixml_stream->set_encoding( encoding = l_ixml_encoding ).


* get renderer
    l_ixml_renderer = c_ixml->create_renderer(
      document = document
      ostream  = l_ixml_stream
    ).
    IF l_ixml_renderer IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_renderer'.             "#EC NOTEXT
    ENDIF.


* render now
    IF pretty_print IS INITIAL.
      l_ixml_renderer->set_normalizing( is_normalizing = ' ' ).
    ELSE.
      l_ixml_renderer->set_normalizing( is_normalizing = 'X' ).
    ENDIF.

    l_ixml_renderer->render(  ).


  ENDMETHOD.


  METHOD xsl_transform_document .


* uses ****************************************************************


* data ****************************************************************

    DATA: l_ixml_document TYPE REF TO if_ixml_document.


* code ****************************************************************


* XSLT initialized already?
    IF c_xslt_processor IS INITIAL. init_xslt( ). ENDIF.


* empty stream?
    IF xml IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inv_arg
        EXPORTING
          argument = 'xml'.                        "#EC NOTEXT
    ENDIF.


* set xml source xml
    c_xslt_processor->set_source_node( xml ).


* set output document
    l_ixml_document = c_ixml->create_document( ).
    IF l_ixml_document IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_document'.                  "#EC NOTEXT
    ENDIF.
    c_xslt_processor->set_result_document( l_ixml_document ).


* transform
    c_xslt_processor->run( progname = xslt ).


* set result
    output = l_ixml_document.


  ENDMETHOD.


  METHOD xsl_transform_string .


* uses ****************************************************************


* data ****************************************************************

    DATA: l_ixml_document TYPE REF TO if_ixml_document,
          l_ixml_istream  TYPE REF TO if_ixml_istream,
          l_ixml_ostream  TYPE REF TO if_ixml_ostream,
          l_ixml_encoding TYPE REF TO if_ixml_encoding.


* code ****************************************************************


* XSLT initialized already?
    IF c_xslt_processor IS INITIAL. init_xslt( ). ENDIF.


* empty stream?
    IF xml IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inv_arg
        EXPORTING
          argument = 'xml'.                        "#EC NOTEXT
    ENDIF.


* get istream
    l_ixml_istream = c_ixml_stream_factory->create_istream_cstring(
      xml ).
    IF l_ixml_istream IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_istream'.              "#EC NOTEXT
    ENDIF.


* get encoding
    DATA: l_c             TYPE c,
          l_len           TYPE i.

    IF result_encoding IS INITIAL.
      DESCRIBE FIELD l_c LENGTH l_len IN BYTE MODE.
      IF l_len = 1.
        result_encoding = 'utf-8'.                          "#EC NOTEXT
      ELSE.
        result_encoding = 'utf-16'.                         "#EC NOTEXT
      ENDIF.
    ENDIF.
    l_ixml_encoding = c_ixml->create_encoding(
      character_set = result_encoding
      byte_order    = 0 ).
    IF l_ixml_encoding IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_encoding'.             "#EC NOTEXT
    ENDIF.


* get ostream
    l_ixml_ostream = c_ixml_stream_factory->create_ostream_cstring(
      result ).
    IF l_ixml_ostream IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_ostream'.              "#EC NOTEXT
    ENDIF.
    l_ixml_ostream->set_encoding( encoding = l_ixml_encoding ).



* set xml source xml
    c_xslt_processor->set_source_stream( stream = l_ixml_istream ).


* set output document
    l_ixml_document = c_ixml->create_document( ).
    IF l_ixml_document IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_document'.                  "#EC NOTEXT
    ENDIF.
    c_xslt_processor->set_result_document( l_ixml_document ).


* transform
    c_xslt_processor->run( progname = xslt ).


* get result
    c_xslt_processor->output_stream( stream = l_ixml_ostream ).


  ENDMETHOD.


  METHOD xsl_transform_table_of_c .


* uses ****************************************************************


* data ****************************************************************

    DATA: l_ixml_document TYPE REF TO if_ixml_document,
          l_ixml_istream  TYPE REF TO if_ixml_istream,
          l_ixml_ostream  TYPE REF TO if_ixml_ostream,
          l_ixml_encoding TYPE REF TO if_ixml_encoding.


* code ****************************************************************


* XSLT initialized already?
    IF c_xslt_processor IS INITIAL. init_xslt( ). ENDIF.


* empty stream?
    IF xml IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inv_arg
        EXPORTING
          argument = 'xml'.                        "#EC NOTEXT
    ENDIF.


* get istream
    l_ixml_istream = c_ixml_stream_factory->create_istream_itable(
      table = xml
      size  = xml_size ).
    IF l_ixml_istream IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_istream'.              "#EC NOTEXT
    ENDIF.


* get encoding
    DATA: l_c             TYPE c,
          l_len           TYPE i.

    IF result_encoding IS INITIAL.
      DESCRIBE FIELD l_c LENGTH l_len IN BYTE MODE.
      IF l_len = 1.
        result_encoding = 'utf-8'.                          "#EC NOTEXT
      ELSE.
        result_encoding = 'utf-16'.                         "#EC NOTEXT
      ENDIF.
    ENDIF.
    l_ixml_encoding = c_ixml->create_encoding(
      character_set = result_encoding
      byte_order    = 0 ).
    IF l_ixml_encoding IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_encoding'.             "#EC NOTEXT
    ENDIF.


* get ostream
    l_ixml_ostream = c_ixml_stream_factory->create_ostream_itable(
      table = result ).
    IF l_ixml_ostream IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_ostream'.              "#EC NOTEXT
    ENDIF.
    l_ixml_ostream->set_encoding( encoding = l_ixml_encoding ).



* set xml source xml
    c_xslt_processor->set_source_stream( stream = l_ixml_istream ).


* set output document
    l_ixml_document = c_ixml->create_document( ).
    IF l_ixml_document IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_document'.                  "#EC NOTEXT
    ENDIF.
    c_xslt_processor->set_result_document( l_ixml_document ).


* transform
    c_xslt_processor->run( progname = xslt ).


* get result
    c_xslt_processor->output_stream( stream = l_ixml_ostream ).
    result_size = l_ixml_ostream->get_num_written_raw( ).


  ENDMETHOD.


  METHOD xsl_transform_table_of_x .


* uses ****************************************************************


* data ****************************************************************

    DATA: l_ixml_document TYPE REF TO if_ixml_document,
          l_ixml_istream  TYPE REF TO if_ixml_istream,
          l_ixml_ostream  TYPE REF TO if_ixml_ostream,
          l_ixml_encoding TYPE REF TO if_ixml_encoding.


* code ****************************************************************


* XSLT initialized already?
    IF c_xslt_processor IS INITIAL. init_xslt( ). ENDIF.


* empty stream?
    IF xml IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inv_arg
        EXPORTING
          argument = 'xml'.                        "#EC NOTEXT
    ENDIF.


* get istream
    l_ixml_istream = c_ixml_stream_factory->create_istream_itable(
      table = xml
      size  = xml_size ).
    IF l_ixml_istream IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_istream'.              "#EC NOTEXT
    ENDIF.


* get encoding
    IF result_encoding IS INITIAL.
      result_encoding = 'utf-8'.                            "#EC NOTEXT
    ENDIF.
    l_ixml_encoding = c_ixml->create_encoding(
      character_set = result_encoding
      byte_order    = 0 ).
    IF l_ixml_encoding IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_encoding'.             "#EC NOTEXT
    ENDIF.


* get ostream
    l_ixml_ostream = c_ixml_stream_factory->create_ostream_itable(
      table = result ).
    IF l_ixml_ostream IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_ostream'.              "#EC NOTEXT
    ENDIF.
    l_ixml_ostream->set_encoding( encoding = l_ixml_encoding ).



* set xml source xml
    c_xslt_processor->set_source_stream( stream = l_ixml_istream ).


* set output document
    l_ixml_document = c_ixml->create_document( ).
    IF l_ixml_document IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_document'.                  "#EC NOTEXT
    ENDIF.
    c_xslt_processor->set_result_document( l_ixml_document ).


* transform
    c_xslt_processor->run( progname = xslt ).


* get result
    c_xslt_processor->output_stream( stream = l_ixml_ostream ).
    result_size = l_ixml_ostream->get_num_written_raw( ).


  ENDMETHOD.


  METHOD xsl_transform_xstring .


* uses ****************************************************************


* data ****************************************************************

    DATA: l_ixml_document TYPE REF TO if_ixml_document,
          l_ixml_istream  TYPE REF TO if_ixml_istream,
          l_ixml_ostream  TYPE REF TO if_ixml_ostream,
          l_ixml_encoding TYPE REF TO if_ixml_encoding.


* code ****************************************************************


* XSLT initialized already?
    IF c_xslt_processor IS INITIAL. init_xslt( ). ENDIF.


* empty stream?
    IF xml IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inv_arg
        EXPORTING
          argument = 'xml'.                        "#EC NOTEXT
    ENDIF.


* get istream
    l_ixml_istream = c_ixml_stream_factory->create_istream_xstring(
      xml ).
    IF l_ixml_istream IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_istream'.              "#EC NOTEXT
    ENDIF.


* get encoding
    IF result_encoding IS INITIAL.
      result_encoding = 'utf-8'.                            "#EC NOTEXT
    ENDIF.
    l_ixml_encoding = c_ixml->create_encoding(
      character_set = result_encoding
      byte_order    = 0 ).
    IF l_ixml_encoding IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_encoding'.             "#EC NOTEXT
    ENDIF.


* get ostream
    l_ixml_ostream = c_ixml_stream_factory->create_ostream_xstring(
      result ).
    IF l_ixml_ostream IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_ostream'.              "#EC NOTEXT
    ENDIF.
    l_ixml_ostream->set_encoding( encoding = l_ixml_encoding ).



* set xml source xml
    c_xslt_processor->set_source_stream( stream = l_ixml_istream ).


* set output document
    l_ixml_document = c_ixml->create_document( ).
    IF l_ixml_document IS INITIAL.
      RAISE EXCEPTION TYPE cx_ixml_inst_failed
        EXPORTING
          type = 'cl_ixml_document'.                  "#EC NOTEXT
    ENDIF.
    c_xslt_processor->set_result_document( l_ixml_document ).


* transform
    c_xslt_processor->run( progname = xslt ).


* get result
    c_xslt_processor->output_stream( stream = l_ixml_ostream ).


  ENDMETHOD.
ENDCLASS.