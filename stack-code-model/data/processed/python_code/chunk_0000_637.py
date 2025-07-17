class zcl_fpm_static definition
  public
  final
  create public .

*"* public components of class ZCL_FPM_STATIC
*"* do not include other source files here!!!
  public section.
    interface if_wd_window load .

    class-data r_oif type ref to cl_fpm_oif .

    class-methods clear .
    class-methods message
      importing
        !i_type     type msgty optional
        !i_text     type simple optional
        !is_message type zsmessage optional
      raising
        zcx_generic .
    class-methods messages
      importing
        !it_messages type zimessages optional
      raising
        zcx_generic .
    class-methods get_severity
      importing
        !iv_type           type msgty optional
      returning
        value(ev_severity) type fpm_message_severity .
    class-methods get
      returning
        value(er_fpm) type ref to if_fpm
      raising
        zcx_generic .
    class-methods get_idr
      returning
        value(er_idr) type ref to cl_fpm_idr
      raising
        zcx_generic .
    class-methods get_oif
      returning
        value(er_oif) type ref to if_fpm_cnr_oif
      raising
        zcx_generic .
    class-methods create_event
      importing
        !i_id          type fpm_event_id
        !ir_param      type ref to if_fpm_parameter optional
      returning
        value(r_event) type ref to cl_fpm_event .
    class-methods raise_event
      importing
        !i_event  type simple
        !ir_param type ref to cl_fpm_parameter optional .
  protected section.
*"* protected components of class ZCL_FPM_STATIC
*"* do not include other source files here!!!
  private section.
*"* private components of class ZCL_FPM_STATIC
*"* do not include other source files here!!!

    class-data dummy type dummy .
ENDCLASS.



CLASS ZCL_FPM_STATIC IMPLEMENTATION.


  method clear.

    try.

        data lr_fpm type ref to if_fpm.
        lr_fpm = get( ).

        lr_fpm->mo_message_manager->clear_messages( lr_fpm ).

      catch cx_root.
        assert 1 = 2.
    endtry.

  endmethod.


  method create_event.

* Determine, whether event is validating or not; default to true
    data l_is_validating type boole_d.
    l_is_validating = 'X'.
    if i_id = cl_fpm_event=>gc_event_cancel or
       i_id = cl_fpm_event=>gc_event_previous_step.
      l_is_validating = ' '.
    endif.

* Determine, whether IF_FPM_TRANSACTION is to be processed; default is false
    data l_is_transactional type boole_d.
    l_is_transactional = ' '.
    if i_id = cl_fpm_event=>gc_event_save or
       i_id = cl_fpm_event=>gc_event_save_as or
       i_id = cl_fpm_event=>gc_event_delete_current_object.
      l_is_transactional = 'X'.
    endif.

* Create event
    data lr_event type ref to cl_fpm_event.
    create object lr_event
      exporting
        iv_event_id         = i_id
        iv_is_validating    = l_is_validating
        iv_is_transactional = l_is_transactional
        io_event_data       = ir_param.

    r_event = lr_event.

  endmethod.


  method get.

    er_fpm ?= cl_fpm=>get_instance( ).

  endmethod.


  method get_idr.

    data lr_fpm type ref to if_fpm.
    lr_fpm = get( ).

    er_idr ?= lr_fpm->get_service( 'IDR' ).

  endmethod.


  method get_oif.

    data lr_fpm type ref to if_fpm.
    lr_fpm = get( ).

    er_oif ?= lr_fpm->get_service( 'CNR_OIF' ).

  endmethod.


  method get_severity.

    if iv_type is initial.
      data lv_type like iv_type.
      lv_type = sy-msgty.
    else.
      lv_type = iv_type.
    endif.

    case lv_type.
      when 'S'.
        ev_severity = if_fpm_message_manager=>gc_severity_success.
      when 'W'.
        ev_severity = if_fpm_message_manager=>gc_severity_warning.
      when 'E' or 'A' or 'X'.
        ev_severity = if_fpm_message_manager=>gc_severity_error.
    endcase.

  endmethod.


  method message.

    data lr_fpm type ref to if_fpm.
    lr_fpm = get( ).

    if lr_fpm is not bound.
      return.
    endif.

    if i_text is not initial.

      " Set message
      data l_text type string.
      l_text = i_text.

      " Set type
      data l_severity type fpm_message_severity.
      l_severity = get_severity( i_type ).

    elseif is_message is not initial.

      l_text = zcl_message_static=>get_text(
        is_message = is_message ).

      l_severity = get_severity( is_message-msgty ).

    else.

      l_text = zcl_message_static=>get_text( ).

      l_severity = get_severity( ).

    endif.

    lr_fpm->mo_message_manager->report_message(
      io_component    = lr_fpm
      iv_message_text = l_text
      iv_severity     = l_severity ).

  endmethod.


  method messages.

    data ls_message like line of it_messages.
    loop at it_messages into ls_message.

      message( is_message = ls_message ).

    endloop.

  endmethod.


  method raise_event.

    data l_event type fpm_event_id.
    l_event = i_event.

    data lr_event type ref to cl_fpm_event.
    lr_event =
      create_event(
        i_id     = l_event
        ir_param = ir_param ).

    data lr_fpm type ref to if_fpm.
    lr_fpm = cl_fpm_factory=>get_instance( ).

    lr_fpm->raise_event( lr_event ).

  endmethod.
ENDCLASS.