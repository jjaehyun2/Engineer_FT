*&---------------------------------------------------------------------*
*& Report  /ENSX/TEST_SIMPLE_TRANSFORM
*&
*&---------------------------------------------------------------------*
*&
*&
*&---------------------------------------------------------------------*

REPORT /ensx/test_xslt_generator.

DATA lcx_root       TYPE REF TO cx_root.
DATA text           TYPE string.
DATA class          TYPE string.
DATA stream         TYPE xstring.
DATA xml            TYPE xstring.
DATA string         TYPE string.
DATA success        TYPE boole_d VALUE abap_true.
DATA bapireturn     TYPE /ensx/bapi_return_table.
DATA output         TYPE REF TO if_demo_output.
DATA serializer     TYPE REF TO /ensx/cl_re_sxml_provider.
DATA renderer       TYPE REF TO /ensx/if_xslt_renderer.
DATA manager        TYPE REF TO /ensx/cl_xslt_manager.

DATA: lr_obj      TYPE REF TO /ensx/if_busobj.
DATA: lr_objdata  TYPE REF TO /ensx/if_objdata.
DATA: lr_ref      TYPE REF TO data.
DATA: or_ref      TYPE REF TO data.
DATA: i_editmode  TYPE boole_d.
FIELD-SYMBOLS <data> TYPE any.

PARAMETERS: p_bus TYPE /ensx/busobj_typ MATCHCODE OBJECT /ensx/busobj.
PARAMETERS: p_key TYPE /ensx/busobj_key.
PARAMETERS: p_xml TYPE boole_d.

START-OF-SELECTION.
  TRY.
*----------------------------------------------------------------------
* Render a Transformation from the Data passed in
*----------------------------------------------------------------------
      /ensx/cl_busobj_factory=>create_obj( EXPORTING i_type = p_bus
                                                     i_key  = p_key
                                           IMPORTING e_obj  = lr_obj
                                           CHANGING  c_editmode = i_editmode ).

      lr_obj->/ensx/if_busobj_db~getdetail( IMPORTING success = success return = bapireturn ).

      lr_objdata ?= lr_obj.
      lr_ref = lr_objdata->get_attribute_by_ref(
          i_recordset = 'DATASET'
             ).
      ASSIGN lr_ref->* TO <data>.

      IF p_xml = abap_false.
        class = '/ENSX/CL_XSLT_SBO_JSN_RENDERER'.
      ELSE.
        class = '/ENSX/CL_XSLT_SBO_XML_RENDERER'.
      ENDIF.

      CREATE OBJECT renderer TYPE (class)
        EXPORTING
          bus_obj = p_bus.
      .
      renderer->add_source(
          root   = 'SUCCESS'
          data   = success
          add_skip = abap_true
             ).

      renderer->add_source(
          root   = 'DATASET'
          dref   = lr_ref
             ).

      renderer->add_source(
          root   = 'RETURN'
          data   = bapireturn
          add_skip = abap_true
             ).

      string = renderer->render(
*          dref   = lr_ref
*          data   = data
*          root   = 'DATASET'
             ).
      cl_demo_output=>display_text( text = string ).
*----------------------------------------------------------------------
* Store the transformation
*----------------------------------------------------------------------
      DATA progname   TYPE string VALUE '/ENSX/TEST_JSON_XXX'.
      DATA devclass   TYPE string VALUE '/ENSX/INTEGRATION_XSLT'.

      CREATE OBJECT manager
        EXPORTING
          progname   = progname
          devclass   = devclass
          xsltsource = string.
      .
      manager->st_program_create( re_create = abap_true ).
      manager->st_program_edit( ).
*----------------------------------------------------------------------
* Try the transformation
*----------------------------------------------------------------------
      CREATE OBJECT serializer
        EXPORTING
          use_camel_case = abap_false
          transformation = progname.

      serializer->/ensx/if_re_sxml_provider~add_source(
          name   = 'SUCCESS'
          value   = abap_true
             ).
      serializer->/ensx/if_re_sxml_provider~add_source(
          name   = 'DATASET'
          value  = <data>
             ).

      serializer->/ensx/if_re_sxml_provider~add_source(
        name   = 'RETURN'
        value  = bapireturn
            ).

      IF p_xml = abap_false.
        serializer->set_stream_type( iv_stream_type = if_sxml=>co_xt_json ).
      ELSE.
        serializer->set_stream_type( iv_stream_type = if_sxml=>co_xt_xml10 ).
      ENDIF.

      stream = serializer->/ensx/if_re_sxml_provider~serialize( ).

      cl_demo_output=>display_xml( xml = stream ).
      string = cl_abap_codepage=>convert_from( stream ).
      cl_demo_output=>display_text( text = string ).

*----------------------------------------------------------------------
* Deserialize back into a data object
*----------------------------------------------------------------------
      CREATE DATA or_ref LIKE <data>.
      IF p_xml = abap_false.
        serializer->set_stream_type( iv_stream_type = if_sxml=>co_xt_json ).
      ELSE.
        serializer->set_stream_type( iv_stream_type = if_sxml=>co_xt_xml10 ).
      ENDIF.
      serializer->/ensx/if_re_sxml_provider~deserialize(
        EXPORTING
          iv_stream    = stream
          iv_root_node = 'DATASET'
        IMPORTING
          oref_data    = or_ref
             ).
      BREAK-POINT.
*----------------------------------------------------------------------
* Delete the transformation
*----------------------------------------------------------------------
*      manager->st_program_delete( ).

    CATCH /ensx/cx_xslt
          /ensx/cx_re_http INTO lcx_root.
      /ensx/cl_abap_exceptions=>_show_exception( exception = lcx_root ).
  ENDTRY.