class ZCL_AOT_SICF definition
  public
  create public .

public section.

  interfaces IF_HTTP_EXTENSION .
protected section.
private section.
ENDCLASS.



CLASS ZCL_AOT_SICF IMPLEMENTATION.


  METHOD if_http_extension~handle_request.

    DATA: lv_path    TYPE string,
          li_service TYPE REF TO zif_aot_service.


    lv_path = server->request->get_header_field( '~path' ).

    IF lv_path CP '/sap/zabapopentest/rest/*'.
      CREATE OBJECT li_service TYPE zcl_aot_service_rest.
    ELSE.
      CREATE OBJECT li_service TYPE zcl_aot_service_static.
    ENDIF.

    TRY.
        li_service->run( server ).
      CATCH cx_static_check.
        ASSERT 0 = 1.
    ENDTRY.

  ENDMETHOD.
ENDCLASS.