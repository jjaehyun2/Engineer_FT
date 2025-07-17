class ycl_apc_wsp_ext_yagar_io definition public inheriting from cl_apc_wsp_ext_stateless_base final create public .

  public section.
    methods if_apc_wsp_extension~on_message redefinition.
    methods if_apc_wsp_extension~on_start redefinition.

  protected section.
  private section.

ENDCLASS.



CLASS YCL_APC_WSP_EXT_YAGAR_IO IMPLEMENTATION.


  method if_apc_wsp_extension~on_message.
    try.
      data(lv_initial_request) = i_context->get_initial_request( ).
      data(lv_socket_key) = lv_initial_request->get_header_field( 'sec-websocket-key' ).
      data(lv_message) = i_message->get_binary( ).
      data(lo_agar_packet_handler) = new ycl_agar_packet_handler( ).
      lo_agar_packet_handler->handle_message( lv_message ).
    catch cx_apc_error into data(lx_apc_error).
      message lx_apc_error->get_text( ) type 'E'.
      endtry.
  endmethod.


  method if_apc_wsp_extension~on_start.
    try.
      data(lv_initial_request) = i_context->get_initial_request( ).
      data(lv_socket_key) = lv_initial_request->get_header_field( 'sec-websocket-key' ).

*        data(lo_message_manager) = i_context->get_message_manager( ).
*        data(lo_message) = lo_message_manager->create_message( ).
*        lo_message->set_text( |{ sy-mandt }/{ sy-uname }: ON_START has been successfully executed !| ).
*        lo_message_manager->send( lo_message ).
      catch cx_apc_error into data(lx_apc_error).
        message lx_apc_error->get_text( ) type 'E'.
    endtry.
  endmethod.
ENDCLASS.