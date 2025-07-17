class ycl_data_view definition public create public.
  public section.
    methods constructor
      importing
        value(buffer) type xstring.

    methods get_length
      returning
        value(length) type i.

    methods get_uint8
      importing
        value(offset)           type i
        value(is_little_endian) type boolean default abap_false
      returning
        value(uint8)            type int1.

    methods get_uint32
      importing
        value(offset)           type i
        value(is_little_endian) type boolean default abap_false
      returning
        value(uint32)           type int4.

  protected section.
    methods _create_conv_in_ce.
    methods _reset_conv_in_ce
      importing
        value(is_little_endian) type boolean default abap_false
        value(skip_length)      type i default 0.

  private section.
    data buffer type xstring.
    data buffer_length type i value 0.
    data abap_endian type abap_endian.
    data conv_in_ce type ref to cl_abap_conv_in_ce.

ENDCLASS.



CLASS YCL_DATA_VIEW IMPLEMENTATION.


  method constructor.
    me->buffer = buffer.
    me->buffer_length = xstrlen( me->buffer ).
    me->_create_conv_in_ce( ).
  endmethod.


  method get_length.
    length = me->buffer_length.
  endmethod.


  method get_uint32.
    me->_reset_conv_in_ce( is_little_endian = is_little_endian skip_length = offset ).
    conv_in_ce->read( exporting n = 4 importing data = uint32 ).
  endmethod.


  method get_uint8.
    me->_reset_conv_in_ce( is_little_endian = is_little_endian skip_length = offset ).
    conv_in_ce->read( exporting n = 1 importing data = uint8 ).
  endmethod.


  method _create_conv_in_ce.
    conv_in_ce = cl_abap_conv_in_ce=>create( input = buffer ).
  endmethod.


  method _reset_conv_in_ce.
    data(abap_endian) = cond #( when is_little_endian eq abap_true then 'L' else 'B' ).
    conv_in_ce->reset( input = buffer endian = abap_endian ).
    conv_in_ce->skip_x( n = skip_length ).
  endmethod.
ENDCLASS.