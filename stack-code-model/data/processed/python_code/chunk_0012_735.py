class zcl_pi_static definition
  public
  final
  create public .

*"* public components of class ZCL_PI_STATIC
*"* do not include other source files here!!!
  public section.

    class-methods get_guid
      importing
        !ir_proxy     type ref to object optional
      returning
        value(e_guid) type guid
      raising
        zcx_generic .
    class-methods get_system
      returning
        value(e_system) type text60
      raising
        zcx_generic .
    class-methods get_attachment
      importing
        !i_id         type simple optional
      returning
        value(e_data) type xstring
      raising
        zcx_generic .
    class-methods get_attachments
      returning
        value(et_attachments) type stringtab
      raising
        zcx_generic .
    class-methods add_attachment
      importing
        !ir_proxy   type ref to object
        !i_id       type simple optional
        !i_file     type simple optional
        !i_data     type xstring
      returning
        value(e_id) type string
      raising
        zcx_generic .
    class-methods set_queue_name
      importing
        !ir_proxy type ref to object
        !i_name   type simple
      raising
        zcx_generic .
    class-methods get_message_url
      importing
        !i_guid      type guid
      returning
        value(e_url) type string
      raising
        zcx_generic .
    class-methods show_message
      importing
        !i_guid type guid
      raising
        zcx_generic .
    class-methods get_output_xml
      importing
        !i_class     type simple
        !i_method    type simple
        !is_data     type data
      returning
        value(e_xml) type string
      raising
        zcx_generic .
  protected section.
*"* protected components of class ZCL_PI_STATIC
*"* do not include other source files here!!!
  private section.
*"* private components of class ZCL_PI_STATIC
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCL_PI_STATIC IMPLEMENTATION.


  method add_attachment.

    try.

        data lr_proxy type ref to if_proxy_basis.
        lr_proxy ?= ir_proxy.

        data lr_protocol type ref to if_wsprotocol_attachments.
        lr_protocol ?= lr_proxy->get_protocol( if_wsprotocol=>attachments ).

        if i_id is initial .
          data l_id type string.
          l_id = zcl_abap_static=>create_guid( ).
        else.
          l_id = i_id.
        endif.

        if i_file is initial.
          data l_type type string.
          l_type = if_xms_resource=>mimetypebin.
        else.
          l_type = zcl_file_static=>get_mime( i_file ).
        endif.

        data lr_attachment type ref to if_ai_attachment.
        lr_attachment =
          lr_protocol->get_attachment_from_binary(
            name = l_id
            type = l_type
            data = i_data ).

        data lt_attachments type prx_attach.
        lt_attachments = lr_protocol->get_attachments( ).

        insert lr_attachment into table lt_attachments.

        lr_protocol->set_attachments( lt_attachments ).

        e_id = l_id.

        data lx_root type ref to cx_root.
      catch cx_root into lx_root.
        zcx_generic=>raise( ix_root = lx_root ).
    endtry.

  endmethod.


  method get_attachment.

    try.

        data lr_context type ref to if_ws_server_context.
        lr_context = cl_proxy_access=>get_server_context( ).

        data lr_protocol type ref to if_wsprotocol.
        lr_protocol = lr_context->get_protocol( if_wsprotocol=>attachments ).

        data lr_attachments type ref to if_wsprotocol_attachments.
        lr_attachments ?= lr_protocol.

        data lt_attachments type prx_attach.
        lt_attachments = lr_attachments->get_attachments( ).

        data lx_root type ref to cx_root.
      catch cx_root into lx_root.
        zcx_generic=>raise( ix_root = lx_root ).
    endtry.

    if i_id is initial.

      data lr_attachment like line of lt_attachments.
      read table lt_attachments into lr_attachment index 1.
      check sy-subrc eq 0.

      e_data = lr_attachment->get_binary_data( ).

    else.

      loop at lt_attachments into lr_attachment.

        data l_name type string.
        l_name = lr_attachment->get_document_name( ).

        check i_id eq l_name.

        e_data = lr_attachment->get_binary_data( ).

        return.

      endloop.

    endif.

  endmethod.


  method get_attachments.

    try.

        data lr_context type ref to if_ws_server_context.
        lr_context = cl_proxy_access=>get_server_context( ).

        data lr_protocol type ref to if_wsprotocol.
        lr_protocol = lr_context->get_protocol( if_wsprotocol=>attachments ).

        data lr_attachments type ref to if_wsprotocol_attachments.
        lr_attachments ?= lr_protocol.

        data lt_attachments type prx_attach.
        lt_attachments = lr_attachments->get_attachments( ).

        data lx_root type ref to cx_root.
      catch cx_root into lx_root.
        zcx_generic=>raise( ix_root = lx_root ).
    endtry.

    data lr_attachment like line of lt_attachments.
    loop at lt_attachments into lr_attachment.

      data l_name type string.
      l_name = lr_attachment->get_document_name( ).

      append l_name to et_attachments.

    endloop.

  endmethod.


  method get_guid.

    try.

        if ir_proxy is bound.

          data lr_proxy type ref to if_proxy_basis.
          lr_proxy ?= ir_proxy.

          data lr_message type ref to if_wsprotocol_message_id.
          lr_message ?= lr_proxy->get_protocol( if_wsprotocol=>message_id ).

          e_guid = lr_message->get_message_id( ).

        else.

          cl_proxy_access=>get_inbound_message_key(
            importing message_id = e_guid ).

        endif.

        data lx_root type ref to cx_root.
      catch cx_root into lx_root.
        zcx_generic=>raise( ix_root = lx_root ).
    endtry.

  endmethod.


  method get_message_url.

    data lt_params type tihttpnvp.
    field-symbols <ls_param> like line of lt_params.

    append initial line to lt_params assigning <ls_param>.
    <ls_param>-name  = 'guid'.
    <ls_param>-value = i_guid.

    e_url =
      zcl_gui_static=>get_url(
        i_trans   = 'ZSRM_PI_MESSAGE_SHOW'
        i_action  = 'ONLI'
        it_params = lt_params ).

  endmethod.


  method get_output_xml.

    data l_class type prx_r3name.
    l_class = i_class.

    data l_method type prx_r3name.
    l_method = i_method.

    try.

        data lr_request_part type ref to if_sxmlp_data_st.
        cl_proxy_st_part=>create_for_clas_method(
          exporting
            class                    = l_class
            method                   = l_method
            for_serialize_request    = abap_true
          importing
            request_part             = lr_request_part ).

        data lt_bindings type abap_trans_resbind_tab.
        field-symbols <ls_binding> like line of lt_bindings.
        append initial line to lt_bindings assigning <ls_binding>.
        <ls_binding>-name = 'OUTPUT'.
        get reference of is_data into <ls_binding>-value.

        data lr_payload type ref to cl_ws_payload.
***        lr_payload ?=
***          cl_ws_payload_handler=>zz_serialize(
***            part     = lr_request_part
***            bindings = lt_bindings ).

        e_xml = lr_payload->if_ws_payload~get_xml_text( ).

        data lx_root type ref to cx_root.
      catch cx_root into lx_root.

        zcx_generic=>raise(
          ix_root = lx_root ).

    endtry.

  endmethod.


  method get_system.

    call function 'LCR_GET_OWN_BUSINESS_SYSTEM'
      importing
        bs_key_name = e_system
      exceptions
        others      = 1.
    if sy-subrc ne 0.
      zcx_generic=>raise( ).
    endif.

  endmethod.


  method set_queue_name.

    data l_name type prx_scnt.
    l_name = i_name.

    try.

        data lr_proxy type ref to if_proxy_basis.
        lr_proxy ?= ir_proxy.

        data lr_protocol type ref to if_wsprotocol_async_messaging.
        lr_protocol ?= lr_proxy->get_protocol( if_wsprotocol=>async_messaging ).

        lr_protocol->set_serialization_context( l_name ).

        data lx_root type ref to cx_root.
      catch cx_root into lx_root.
        zcx_generic=>raise( ix_root = lx_root ).
    endtry.

  endmethod.


  method show_message.

    data lr_bdc type ref to zcl_bdc.
    create object lr_bdc.

    lr_bdc->mode = 'E'.

    lr_bdc->add_screen(
      i_prog   = 'RSXMB_SELECT_MESSAGES'
      i_number = '1000' ).

    lr_bdc->add_action( '=''EXTD''' ).

    lr_bdc->add_screen(
      i_prog   = 'RSXMB_SELECT_MESSAGES'
      i_number = '1000' ).

    lr_bdc->add_action( '=ONLI' ).

    lr_bdc->add_field(
      i_name  = 'MSGGUID-LOW'
      i_value = i_guid ).

    lr_bdc->add_screen(
      i_prog   = 'RSXMB_SELECT_MESSAGES'
      i_number = '0100' ).

    lr_bdc->add_screen(
      i_prog   = 'RSXMB_SELECT_MESSAGES'
      i_number = '1000' ).

    lr_bdc->add_action( '/EE' ).

    data lt_messages type zimessages.
    lt_messages = lr_bdc->run( 'SXI_MONITOR' ).

    loop at lt_messages transporting no fields
      where
        msgty ca 'EAX'.
      zcx_generic=>raise(
        it_messages = lt_messages ).
    endloop.

  endmethod.
ENDCLASS.