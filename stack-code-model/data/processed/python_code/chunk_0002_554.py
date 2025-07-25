class ZCL_AOT_SERVICE_STATIC definition
  public
  create public .

public section.

  interfaces ZIF_AOT_SERVICE .
protected section.

  data MI_SERVER type ref to IF_HTTP_SERVER .
private section.

  methods BUILD_PAGES .
  methods CONVERT_TIMESTAMP
    importing
      !IV_CHANGED type SMIMPHIO-CHNG_TIME
    returning
      value(RV_TIMESTAMP) type STRING .
  methods SET_CACHE
    importing
      !IV_MODIFIED type STRING
    returning
      value(RV_CACHED) type ABAP_BOOL .
  methods READ_MIME
    importing
      !IV_URL type STRING .
ENDCLASS.



CLASS ZCL_AOT_SERVICE_STATIC IMPLEMENTATION.


  METHOD build_pages.

    DATA: li_api     TYPE REF TO if_mr_api,
          lt_files   TYPE string_table,
          lv_data    TYPE xstring,
          lv_result  TYPE xstring,
          lv_max     TYPE smimphio-chng_time,
          lv_changed TYPE smimphio-chng_time,
          lv_file    LIKE LINE OF lt_files.


    li_api = cl_mime_repository_api=>if_mr_api~get_api( ).

    li_api->file_list(
      EXPORTING
        i_url   = '/SAP/PUBLIC/zabapopentest/pages/'
      IMPORTING
        e_files = lt_files ).

    SORT lt_files ASCENDING AS TEXT.

    LOOP AT lt_files INTO lv_file.
      li_api->get(
        EXPORTING
          i_url                  = lv_file
        IMPORTING
          e_content              = lv_data
          e_content_last_changed = lv_changed
        EXCEPTIONS
          not_found              = 1 ).
      ASSERT sy-subrc = 0.

      IF lv_max IS INITIAL OR lv_max < lv_changed.
        lv_max = lv_changed.
      ENDIF.

      CONCATENATE lv_result lv_data INTO lv_result IN BYTE MODE.
    ENDLOOP.

    IF set_cache( convert_timestamp( lv_max ) ) = abap_true.
      RETURN.
    ENDIF.

    mi_server->response->set_compression( ).
    mi_server->response->set_content_type( 'application/x-javascript' ).
    mi_server->response->set_data( lv_result ).

  ENDMETHOD.


  METHOD convert_timestamp.

    DATA: lv_timestamp TYPE char14.


    lv_timestamp = iv_changed.

    rv_timestamp = cl_bsp_utility=>date_to_string_http( lv_timestamp ).

  ENDMETHOD.


  METHOD read_mime.

    DATA: li_api      TYPE REF TO if_mr_api,
          lv_data     TYPE xstring,
          lv_changed  TYPE smimphio-chng_time,
          lv_modified TYPE string,
          lv_mime     TYPE string,
          lv_url      TYPE string.


    CONCATENATE '/SAP/PUBLIC/zabapopentest/' iv_url INTO lv_url.

    li_api = cl_mime_repository_api=>if_mr_api~get_api( ).

    li_api->get(
      EXPORTING
        i_url                  = lv_url
      IMPORTING
        e_content              = lv_data
        e_mime_type            = lv_mime
        e_content_last_changed = lv_changed
      EXCEPTIONS
        not_found              = 1 ).
    IF sy-subrc = 1.
      mi_server->response->set_cdata( '404' ).
      mi_server->response->set_status( code = 404 reason = '404' ).
      RETURN.
    ENDIF.

    IF set_cache( convert_timestamp( lv_changed ) ) = abap_true.
      RETURN.
    ENDIF.

    mi_server->response->set_compression( ).
    mi_server->response->set_content_type( lv_mime ).
    mi_server->response->set_data( lv_data ).

  ENDMETHOD.


  METHOD set_cache.

    IF iv_modified = mi_server->request->get_header_field( 'If-Modified-Since' ) ##NO_TEXT.
      mi_server->response->set_status( code = 304 reason = '' ).
      RETURN.
    ENDIF.

    mi_server->response->set_header_field(
      name  = 'Cache-Control'
      value = 'max-age=86400' ) ##NO_TEXT.

    mi_server->response->set_header_field(
      name  = 'Last-Modified'
      value = iv_modified ) ##NO_TEXT.

  ENDMETHOD.


  METHOD zif_aot_service~run.

    DATA: lv_name TYPE string,
          lv_path TYPE string.


    mi_server = ii_server.

    lv_path = mi_server->request->get_header_field( '~path' ).

    FIND REGEX '/sap/zabapopentest/static/(.*)'
      IN lv_path
      SUBMATCHES lv_name ##NO_TEXT.

    IF lv_name IS INITIAL.
      lv_name = 'index.html' ##NO_TEXT.
    ENDIF.

    IF lv_name = 'pages.js'.
      build_pages( ).
    ELSE.
      read_mime( lv_name ).
    ENDIF.

  ENDMETHOD.
ENDCLASS.