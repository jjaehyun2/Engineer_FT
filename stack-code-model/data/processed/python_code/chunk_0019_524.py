class zcl_web_hooks_event_handler definition
  public
  create public .

public section.

  interfaces bi_event_handler_static .
  class-methods send importing rectype type swfdevtyp-rectype data type string.
  class-methods convert_to_json importing id type string container type ref to if_swf_ifs_parameter_container returning value(data) type string.
protected section.
private section.
endclass.



class zcl_web_hooks_event_handler implementation.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Static Public Method ZCL_WEB_HOOKS_EVENT_HANDLER=>BI_EVENT_HANDLER_STATIC~ON_EVENT
* +-------------------------------------------------------------------------------------------------+
* | [--->] SENDER                         TYPE        SIBFLPORB
* | [--->] EVENT                          TYPE        SIBFEVENT
* | [--->] EVENT_CONTAINER                TYPE REF TO IF_SWF_IFS_PARAMETER_CONTAINER
* | [--->] RECTYPE                        TYPE        SWFERECTYP
* | [--->] HANDLER                        TYPE        SIBFLPORB
* | [<---] RESULT                         TYPE        SWFREVRSLT
* | [!CX!] CX_BO_ERROR
* | [!CX!] CX_BO_TEMPORARY
* +--------------------------------------------------------------------------------------</SIGNATURE>
  method bi_event_handler_static~on_event.
    data l_rectype type swfdevtyp-rectype.

    select single swfdevtyp~rectype from swfdevtyp inner join swfdevena on
      swfdevtyp~objcateg  = swfdevena~objcateg and
      swfdevtyp~objtype  =  swfdevena~objtype and
      swfdevtyp~event  =  swfdevena~event and
      swfdevtyp~rectype  =  swfdevena~rectype
      into l_rectype
      where swfdevtyp~objcateg = 'BO'
        and swfdevtyp~objtype = sender-objtype
        and swfdevtyp~event = event
        and swfdevtyp~rectype = rectype
        and swfdevena~enabled = 'X'.

    if sy-subrc = 0.
      send( rectype = l_rectype data = convert_to_json( id = conv #( sender-instid ) container = event_container ) ).
    endif.
  endmethod.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Static Public Method ZCL_WEB_HOOKS_EVENT_HANDLER=>CONVERT_TO_JSON
* +-------------------------------------------------------------------------------------------------+
* | [--->] ID                             TYPE        STRING
* | [--->] CONTAINER                      TYPE REF TO IF_SWF_IFS_PARAMETER_CONTAINER
* | [<-()] DATA                           TYPE        STRING
* +--------------------------------------------------------------------------------------</SIGNATURE>
  method convert_to_json.
    data(lo_json) = zcl_json_document=>create( ).
    lo_json->append_data( exporting iv_name = 'id' data = id ).
    data(lt_par_names) = container->list_names( ).
    loop at lt_par_names into data(l_par_name).
     container->get_value_ref( exporting name = l_par_name importing value_ref = data(lo_par) ).
     lo_json->append_data( exporting iv_name = conv #( l_par_name ) data = lo_par ).
    endloop.
    data = lo_json->get_json( ).
  endmethod.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Static Public Method ZCL_WEB_HOOKS_EVENT_HANDLER=>SEND
* +-------------------------------------------------------------------------------------------------+
* | [--->] RECTYPE                        TYPE        SWFDEVTYP-RECTYPE
* | [--->] DATA                           TYPE        STRING
* +--------------------------------------------------------------------------------------</SIGNATURE>
  method send.
    cl_http_client=>create(
      exporting
        host = conv #( rectype )
        service = ''
      importing
        client = data(lo_client)
      exceptions
        others = 4 ).
    if sy-subrc <> 0.
      return.
    endif.
    lo_client->request->set_method( 'POST' ).
    lo_client->request->set_cdata( data ).
    lo_client->send(
      exceptions
        others = 4 ).
    if sy-subrc <> 0.
      lo_client->get_last_error(
        importing message = data(smsg) ).
      return.
    endif.

    lo_client->receive(
      exceptions
        others = 4 ).
    if sy-subrc <> 0.
      lo_client->get_last_error(
        importing message = data(rmsg) ).
      return.
    endif.

    data(l_return) = lo_client->response->get_cdata( ).
    lo_client->close( ).
  endmethod.
endclass.