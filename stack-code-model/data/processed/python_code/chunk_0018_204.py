class ZCL_REST_SOURCE_SCARR definition
  public
  inheriting from ZCL_REST_RESOURCE_HANDLER_BASE
  create public .

public section.

  methods CONSTRUCTOR
    importing
      !IO_HELPER type ref to ZIF_REST_RESOURCE_UTILITIES optional
      !IO_DAO type ref to ZIF_REST_PERSISTENCE optional .

  methods ZIF_REST_RESOURCE_HANDLER_BASE~READ
    redefinition .
  methods ZIF_REST_RESOURCE_HANDLER_BASE~QUERY
    redefinition .
protected section.

  data MO_SCARR_DAO type ref to ZIF_REST_PERSISTENCE .
private section.
ENDCLASS.



CLASS ZCL_REST_SOURCE_SCARR IMPLEMENTATION.


  METHOD constructor.
    super->constructor( ).

    IF io_dao IS BOUND.
      mo_scarr_dao = io_dao.
    ELSE.
      mo_scarr_dao = NEW zcl_rest_source_scarr_dao( ).
    ENDIF.

  ENDMETHOD.


  method ZIF_REST_RESOURCE_HANDLER_BASE~QUERY.

    DATA lv_max_rows TYPE i.
    DATA lt_sql_order_by TYPE string_table.

    DATA(ls_url_param) = get_url_parameters( io_request ).
    "Skip und Top addieren
    lv_max_rows = ls_url_param-top + ls_url_param-skip.

    DATA(lt_query_filter) = parse_query_filter( ls_url_param-filter ).

*    lt_sql_order_by = parse_query_orderby(
*      iv_tabname = 'SNWD_SO'
*      iv_orderby = ls_url_param-orderby ).

    LOOP AT lt_query_filter ASSIGNING FIELD-SYMBOL(<ls_query_filter>).
      CASE <ls_query_filter>-property.
        WHEN 'CARRID'.
          DATA(lt_range_table_carrid)   = <ls_query_filter>-range_table.
        WHEN 'CARRNAME'.
          DATA(lt_range_table_carrname) = <ls_query_filter>-range_table.
        WHEN 'CURRCODE'.
          DATA(lt_range_table_currcode) = <ls_query_filter>-range_table.
        WHEN 'URL'.
          DATA(lt_range_table_url)      = <ls_query_filter>-range_table.
        WHEN OTHERS.
          " raise exception
      ENDCASE.
    ENDLOOP.

    "selectieren bis skip+top rows
    SELECT * FROM scarr INTO TABLE @DATA(lt_headers)
      UP TO @lv_max_rows ROWS
      WHERE carrid   IN @lt_range_table_carrid
        AND carrname IN @lt_range_table_carrname
        AND currcode IN @lt_range_table_currcode
        AND url      IN @lt_range_table_url.
*      ORDER BY (lt_sql_order_by).

    "Zeile 1 bis zeile "skip" löschen
    IF ls_url_param-skip > 0.
      DELETE lt_headers FROM 1 TO ls_url_param-skip.
    ENDIF.

    mo_helper->serialize_json( iv_data     = lt_headers
                               io_response = io_response ).
  endmethod.


  METHOD zif_rest_resource_handler_base~read.

    DATA(lv_attribute) = get_uri_attributes( io_request ).

    SELECT SINGLE * FROM scarr INTO @DATA(ls_scarr)
      WHERE carrid = @lv_attribute.

    IF sy-subrc <> 0.
      " raise exception
    ENDIF.

    mo_helper->serialize_json( iv_data = ls_scarr
                               io_response = io_response ).

  ENDMETHOD.
ENDCLASS.