class zcl_web_hooks_handler definition
  public
  final
  create public .

public section.

  interfaces if_http_extension .
  types: begin of ty_request,
    action type string,
    object type string,
    event type string,
    callbackurl type string,
  end of ty_request.

  types: begin of ty_link,
    objtype type swfdevtyp-objtype,
    event type swfdevtyp-event,
    rectype type swfdevtyp-rectype,
    enabled type swfdevena-enabled,
  end of ty_link,
  ty_links type table of ty_link with key objtype event rectype.

  methods post
    importing
      !request type ref to if_http_request
      !response type ref to if_http_response .
protected section.
private section.

  methods set_cors_headers
    importing
      !response type ref to if_http_response .
  methods get_links
    importing
      !request type ty_request
    returning
      value(links) type ty_links .
  methods subscribe
    importing
      !request type ty_request .
  methods unsubscribe
    importing
      !request type ty_request .
endclass.



class zcl_web_hooks_handler implementation.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Private Method ZCL_WEB_HOOKS_HANDLER->GET_LINKS
* +-------------------------------------------------------------------------------------------------+
* | [--->] REQUEST                        TYPE        TY_REQUEST
* | [<-()] LINKS                          TYPE        TY_LINKS
* +--------------------------------------------------------------------------------------</SIGNATURE>
  method get_links.

  select swfdevtyp~objtype swfdevtyp~event swfdevtyp~rectype swfdevena~enabled from swfdevtyp inner join swfdevena on
      swfdevtyp~objcateg  = swfdevena~objcateg and
      swfdevtyp~objtype  =  swfdevena~objtype and
      swfdevtyp~event  =  swfdevena~event and
      swfdevtyp~rectype  =  swfdevena~rectype
      into table links where swfdevtyp~objtype = request-object and swfdevtyp~event = request-event.
  endmethod.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_WEB_HOOKS_HANDLER->IF_HTTP_EXTENSION~HANDLE_REQUEST
* +-------------------------------------------------------------------------------------------------+
* | [--->] SERVER                         TYPE REF TO IF_HTTP_SERVER
* +--------------------------------------------------------------------------------------</SIGNATURE>
  method if_http_extension~handle_request.
    data(l_method) = server->request->get_method( ).
    call method me->(l_method) exporting request = server->request response = server->response.
  endmethod.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_WEB_HOOKS_HANDLER->POST
* +-------------------------------------------------------------------------------------------------+
* | [--->] REQUEST                        TYPE REF TO IF_HTTP_REQUEST
* | [--->] RESPONSE                       TYPE REF TO IF_HTTP_RESPONSE
* +--------------------------------------------------------------------------------------</SIGNATURE>
  method post.
   data ls_request type ty_request.

   try.
     data(l_data) = request->get_cdata( ).
     data(lo_json) = zcl_json_document=>create_with_json( l_data ).
     lo_json->get_data( importing data = ls_request ).
     if ls_request-action = 'subscribe'.
       subscribe( ls_request ).
     elseif ls_request-action = 'unsubscribe'.
       unsubscribe( ls_request ).
     endif.
     response->set_cdata( '{"aa":"aa"}' ).
     response->set_status( code = 200 reason = 'ok' ).

     catch cx_root into data(lo_error).
   endtry.

   set_cors_headers( exporting response = response ).
  endmethod.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Private Method ZCL_WEB_HOOKS_HANDLER->SET_CORS_HEADERS
* +-------------------------------------------------------------------------------------------------+
* | [--->] RESPONSE                       TYPE REF TO IF_HTTP_RESPONSE
* +--------------------------------------------------------------------------------------</SIGNATURE>
  method set_cors_headers.
    response->set_header_field( name = 'content-type' value = 'application-json').
    response->set_header_field( name = 'content-type' value = 'application-json').
  endmethod.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Private Method ZCL_WEB_HOOKS_HANDLER->SUBSCRIBE
* +-------------------------------------------------------------------------------------------------+
* | [--->] REQUEST                        TYPE        TY_REQUEST
* +--------------------------------------------------------------------------------------</SIGNATURE>
  method subscribe.
   data l_enabled type abap_bool.
   select single enabled from swfdevena into l_enabled where objtype = request-object and event = request-event.
   if l_enabled = ''.
     data(lt_links) = get_links( request ).
     if lines( lt_links ) = 0.
       data(ls_swfdevtyp) = value swfdevtyp( objcateg = 'BO' objtype = request-object event = request-event rectype = request-callbackurl recmode = 'M' recclass = 'ZCL_WEB_HOOKS_EVENT_HANDLER' typelink = 'X' ).
       data(ls_swfdevena) = value swfdevena( objcateg = 'BO' objtype = request-object event = request-event rectype = request-callbackurl enabled = 'X' ).
       insert into swfdevtyp values ls_swfdevtyp.
       if sy-subrc = 0.
        insert into swfdevena values ls_swfdevena.
       endif.
     else.
      loop at lt_links into data(ls_link).
       ls_swfdevena = value swfdevena( objcateg = 'BO' objtype = ls_link-objtype event = ls_link-event rectype = ls_link-rectype enabled = 'X' ).
       insert into swfdevena values ls_swfdevena.
      endloop.
     endif.
   endif.
  endmethod.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Private Method ZCL_WEB_HOOKS_HANDLER->UNSUBSCRIBE
* +-------------------------------------------------------------------------------------------------+
* | [--->] REQUEST                        TYPE        TY_REQUEST
* +--------------------------------------------------------------------------------------</SIGNATURE>
  method unsubscribe.
   data ls_swfdevena type swfdevena.
   data(lt_links) = get_links( request ).
   loop at lt_links into data(ls_link) where enabled = 'X'.
    select single * from swfdevena into ls_swfdevena where objcateg = 'BO' and objtype = ls_link-objtype and event = ls_link-event and rectype = ls_link-rectype and enabled = 'X'.
    if sy-subrc = 0.
      ls_swfdevena-enabled = ''.
      insert into swfdevena values ls_swfdevena.
      if sy-subrc = 0.
      endif.
    endif.
   endloop.
  endmethod.
endclass.