class ycl_agar_packet_handler definition public final create public.
  public section.
    methods handle_message
      importing
        value(message) type xstring.

  protected section.

  private section.

ENDCLASS.



CLASS YCL_AGAR_PACKET_HANDLER IMPLEMENTATION.


  method handle_message.
    data(data_view) = new ycl_data_view( buffer = message ).
    data(packet_id) = data_view->get_uint8( offset = 0 is_little_endian = abap_true ).
    case packet_id.
      when 255.
        data(data_view_length) = data_view->get_length( ).
        if ( data_view_length eq 5 ).
          data(lv_protocol) = data_view->get_uint32( offset = 1 is_little_endian = abap_true ).
        endif.
    endcase.
  endmethod.
ENDCLASS.