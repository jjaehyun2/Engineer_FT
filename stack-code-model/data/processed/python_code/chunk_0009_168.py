class ZCL_REST_RESOURCE_HANDLER_BASE definition
  public
  abstract
  create public .

public section.

  interfaces ZIF_REST_RESOURCE_HANDLER_BASE .

  methods CONSTRUCTOR
    importing
      !IO_HELPER type ref to ZIF_REST_RESOURCE_UTILITIES optional .
protected section.

  data MO_HELPER type ref to ZIF_REST_RESOURCE_UTILITIES .

  methods GET_URI_ATTRIBUTES
    importing
      !IO_REQUEST type ref to IF_REST_REQUEST
    returning
      value(RV_VALUE) type STRING .
  methods GET_URL_PARAMETERS
    importing
      !IO_REQUEST type ref to IF_REST_REQUEST
    returning
      value(RS_URL_PARAMETER) type ZREST_URL_PARAMETER_S .
  methods PARSE_QUERY_FILTER
    importing
      !IV_FILTER type STRING
    returning
      value(RT_QUERY_FILTER) type ZREST_QUERY_FILTER_T .
private section.
ENDCLASS.



CLASS ZCL_REST_RESOURCE_HANDLER_BASE IMPLEMENTATION.


  METHOD constructor.

    IF io_helper IS BOUND.
      mo_helper = io_helper.
    ELSE.
      mo_helper = NEW zcl_rest_resource_utilities( ).
    ENDIF.

  ENDMETHOD.


  METHOD get_uri_attributes.


    " Make this method better. We should transfer to a range table?
    " More generic
    DATA lt_name_value TYPE tihttpnvp.

    lt_name_value = io_request->get_uri_attributes( ).

    LOOP AT lt_name_value ASSIGNING FIELD-SYMBOL(<ls_name_value>).
      rv_value = <ls_name_value>-value.
      RETURN.
    ENDLOOP.

  ENDMETHOD.


  METHOD GET_URL_PARAMETERS.

    DATA(lt_name_value) = io_request->get_uri_query_parameters( iv_encoded = abap_false ).

    LOOP AT lt_name_value ASSIGNING FIELD-SYMBOL(<ls_name_value>).
      CASE to_upper( <ls_name_value>-name ).
        WHEN 'FILTER'.
          rs_url_parameter-filter = <ls_name_value>-value.
        WHEN 'TOP'.
          rs_url_parameter-top = <ls_name_value>-value.
        WHEN 'SKIP'.
          rs_url_parameter-skip = <ls_name_value>-value.
        WHEN 'ORDERBY'.
          rs_url_parameter-orderby = <ls_name_value>-value.
        WHEN OTHERS.
          "To do - Raise Exception
      ENDCASE.
    ENDLOOP.

  ENDMETHOD.


  METHOD parse_query_filter.

    DATA lt_filter TYPE TABLE OF string.
    DATA lv_property TYPE string.
    DATA lv_option TYPE string.
    DATA lv_value TYPE string.
    DATA ls_range TYPE rsrange.

    SPLIT iv_filter AT ',' INTO TABLE lt_filter.

    LOOP AT lt_filter ASSIGNING FIELD-SYMBOL(<lv_filter>).

      FIND REGEX '([[:print:]]+)\s(eq|cp|bt|le|ge|ne|nb|np|gt|lt)\s([[:print:]]+)' IN <lv_filter>
      IGNORING CASE SUBMATCHES lv_property lv_option lv_value.

      IF lv_property IS INITIAL OR
         lv_option IS INITIAL OR
         lv_value IS INITIAL.
        CONTINUE.
      ENDIF.

      lv_property = to_upper( lv_property ).
      lv_option   = to_upper( lv_option ).

      CLEAR ls_range.
      ls_range-sign = 'I'.
      ls_range-option = lv_option.

      CASE lv_option.
        WHEN 'EQ' OR 'CP' OR 'LE' OR 'GE' OR 'NE' OR 'NP' OR 'GT' OR 'LT'.
          ls_range-low = lv_value.

        WHEN 'BT' OR 'NB'.
          SPLIT lv_value AT ':' INTO ls_range-low ls_range-high.
          IF ls_range-low IS INITIAL OR
             ls_range-high IS INITIAL.
            CONTINUE.
          ENDIF.
        WHEN OTHERS.
          " To Do - raise Exception
      ENDCASE.

      READ TABLE rt_query_filter ASSIGNING FIELD-SYMBOL(<ls_query_filter>) WITH KEY property = lv_property BINARY SEARCH.

      IF sy-subrc <> 0.
        INSERT INITIAL LINE INTO rt_query_filter ASSIGNING <ls_query_filter> INDEX sy-tabix.
        <ls_query_filter>-property = lv_property.
      ENDIF.

      APPEND ls_range TO <ls_query_filter>-range_table.

    ENDLOOP.

  ENDMETHOD.


  method ZIF_REST_RESOURCE_HANDLER_BASE~CREATE.
*    RAISE EXCEPTION TYPE cx_rest_resource_exception
*      EXPORTING
*        status_code    = cl_rest_status_code=>gc_client_error_meth_not_allwd
*        request_method = if_rest_message=>gc_method_delete
*        textid         = cx_rest_resource_exception=>method_not_supported.

    RAISE EXCEPTION TYPE zcx_rest_service_exception
      EXPORTING
        textid = zcx_rest_service_exception=>method_not_supported
        method = zif_rest_constants=>gc_method_post.
  endmethod.


  method ZIF_REST_RESOURCE_HANDLER_BASE~DELETE.
*    RAISE EXCEPTION TYPE cx_rest_resource_exception
*      EXPORTING
*        status_code    = cl_rest_status_code=>gc_client_error_meth_not_allwd
*        request_method = if_rest_message=>gc_method_delete
*        textid         = cx_rest_resource_exception=>method_not_supported.

    RAISE EXCEPTION TYPE zcx_rest_service_exception
      EXPORTING
        textid = zcx_rest_service_exception=>method_not_supported
        method = zif_rest_constants=>gc_method_delete.
  endmethod.


  method ZIF_REST_RESOURCE_HANDLER_BASE~GET_URI_ATTRIBUTES.
*    RAISE EXCEPTION TYPE cx_rest_resource_exception
*      EXPORTING
*        status_code    = cl_rest_status_code=>gc_client_error_meth_not_allwd
*        request_method = if_rest_message=>gc_method_delete
*        textid         = cx_rest_resource_exception=>method_not_supported.

    RAISE EXCEPTION TYPE zcx_rest_service_exception
      EXPORTING
        textid = zcx_rest_service_exception=>method_not_supported
        method = zif_rest_constants=>gc_method_get.
  endmethod.


  method ZIF_REST_RESOURCE_HANDLER_BASE~GET_URL_PARAM.
*    RAISE EXCEPTION TYPE cx_rest_resource_exception
*      EXPORTING
*        status_code    = cl_rest_status_code=>gc_client_error_meth_not_allwd
*        request_method = if_rest_message=>gc_method_delete
*        textid         = cx_rest_resource_exception=>method_not_supported.

    RAISE EXCEPTION TYPE zcx_rest_service_exception
      EXPORTING
        textid = zcx_rest_service_exception=>method_not_supported
        method = zif_rest_constants=>gc_method_get.
  endmethod.


  method ZIF_REST_RESOURCE_HANDLER_BASE~PARSE_QUERY_FILTER.
*    RAISE EXCEPTION TYPE cx_rest_resource_exception
*      EXPORTING
*        status_code    = cl_rest_status_code=>gc_client_error_meth_not_allwd
*        request_method = if_rest_message=>gc_method_delete
*        textid         = cx_rest_resource_exception=>method_not_supported.

    RAISE EXCEPTION TYPE zcx_rest_service_exception
      EXPORTING
        textid = zcx_rest_service_exception=>method_not_supported
        method = zif_rest_constants=>gc_method_get.
  endmethod.


  method ZIF_REST_RESOURCE_HANDLER_BASE~PARSE_QUERY_ORDERBY.
*    RAISE EXCEPTION TYPE cx_rest_resource_exception
*      EXPORTING
*        status_code    = cl_rest_status_code=>gc_client_error_meth_not_allwd
*        request_method = if_rest_message=>gc_method_delete
*        textid         = cx_rest_resource_exception=>method_not_supported.

    RAISE EXCEPTION TYPE zcx_rest_service_exception
      EXPORTING
        textid = zcx_rest_service_exception=>method_not_supported
        method = zif_rest_constants=>gc_method_get.
  endmethod.


  METHOD zif_rest_resource_handler_base~query.

*    RAISE EXCEPTION TYPE cx_rest_resource_exception
*      EXPORTING
*        status_code    = cl_rest_status_code=>gc_client_error_meth_not_allwd
*        request_method = if_rest_message=>gc_method_delete
*        textid         = cx_rest_resource_exception=>method_not_supported.

    RAISE EXCEPTION TYPE zcx_rest_service_exception
      EXPORTING
        textid = zcx_rest_service_exception=>method_not_supported
        method = zif_rest_constants=>gc_method_get.

  ENDMETHOD.


  method ZIF_REST_RESOURCE_HANDLER_BASE~READ.

*    RAISE EXCEPTION TYPE cx_rest_resource_exception
*      EXPORTING
*        status_code    = cl_rest_status_code=>gc_client_error_meth_not_allwd
*        request_method = if_rest_message=>gc_method_delete
*        textid         = cx_rest_resource_exception=>method_not_supported.

    RAISE EXCEPTION TYPE zcx_rest_service_exception
      EXPORTING
        textid = zcx_rest_service_exception=>method_not_supported
        method = zif_rest_constants=>gc_method_get.

  endmethod.


  method ZIF_REST_RESOURCE_HANDLER_BASE~UPDATE.
*    RAISE EXCEPTION TYPE cx_rest_resource_exception
*      EXPORTING
*        status_code    = cl_rest_status_code=>gc_client_error_meth_not_allwd
*        request_method = if_rest_message=>gc_method_delete
*        textid         = cx_rest_resource_exception=>method_not_supported.

    RAISE EXCEPTION TYPE zcx_rest_service_exception
      EXPORTING
        textid = zcx_rest_service_exception=>method_not_supported
        method = zif_rest_constants=>gc_method_put.
  endmethod.
ENDCLASS.