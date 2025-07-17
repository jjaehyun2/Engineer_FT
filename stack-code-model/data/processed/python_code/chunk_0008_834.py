CLASS zcl_001_mylyn_service DEFINITION
  PUBLIC
  ABSTRACT
  CREATE PUBLIC .

  PUBLIC SECTION.
*"* public components of class ZCL_001_MYLYN_SERVICE
*"* do not include other source files here!!!

    METHODS constructor
      IMPORTING
        !io_server TYPE REF TO if_http_server .
protected section.
*"* protected components of class ZCL_001_MYLYN_SERVICE
*"* do not include other source files here!!!

  data MT_PARAMETER type ZTT001_QUERY_PARAMETER .
  data MO_HTTP_SERVER type ref to IF_HTTP_SERVER .

  methods PARSE_PARAMETERS .
  methods GET_PARAMETER_VALUE
    importing
      !IV_NAME type ZE_000_RSS_PARAMETER_NAME
    returning
      value(RV_VALUE) type ZE_000_RSS_PARAMETER_VALUE .
  PRIVATE SECTION.
*"* private components of class ZCL_001_MYLYN_SERVICE
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCL_001_MYLYN_SERVICE IMPLEMENTATION.


  METHOD constructor.
    mo_http_server = io_server.
    parse_parameters( ).
  ENDMETHOD.                    "constructor


  METHOD get_parameter_value.

    FIELD-SYMBOLS: <s_parameter> LIKE LINE OF mt_parameter.

    READ TABLE mt_parameter ASSIGNING <s_parameter> WITH TABLE KEY name = iv_name.

    IF sy-subrc = 0.
      rv_value = <s_parameter>-value.
    ELSE.
      CLEAR rv_value.
    ENDIF.

  ENDMETHOD.                    "get_parameter_value


  METHOD parse_parameters.

    DATA: lt_name_value_params TYPE TABLE OF string,
        ls_parameter TYPE zs000_rss_parameter,
        lv_parameter_string TYPE string,
        lv_name_value_string TYPE string.


    lv_parameter_string = mo_http_server->request->get_header_field( if_http_header_fields_sap=>query_string ).


    SPLIT lv_parameter_string AT '&' INTO TABLE lt_name_value_params.

    LOOP AT lt_name_value_params INTO lv_name_value_string.

      SPLIT lv_name_value_string AT '=' INTO ls_parameter-name ls_parameter-value.

      TRANSLATE: ls_parameter-name  TO UPPER CASE,
                 ls_parameter-value TO UPPER CASE.

      INSERT ls_parameter INTO TABLE mt_parameter.

    ENDLOOP.

  ENDMETHOD.                    "parse_parameters
ENDCLASS.