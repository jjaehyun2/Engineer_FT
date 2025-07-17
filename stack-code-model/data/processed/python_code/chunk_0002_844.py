class z_cl_ascii_translator definition
  public
  final
  create public .

  public section.
    methods:
      convert_int_to_ascii
        importing
          iv_integer_value          type i
        returning
          value(rv_ascii_character) type char1,

      convert_ascii_to_int
        importing
          iv_ascii_character      type char1
        returning
          value(rv_integer_value) type int1.
endclass.



class z_cl_ascii_translator implementation.
  method convert_ascii_to_int.
    field-symbols <lv_ascii> type int1.
    assign iv_ascii_character to <lv_ascii> casting.
    rv_integer_value = <lv_ascii>.
  endmethod.

  method convert_int_to_ascii.
    check iv_integer_value >= 0 and iv_integer_value < 256.

    field-symbols <lv_char> type c.
    assign iv_integer_value to <lv_char> casting type c.
    rv_ascii_character = <lv_char>.
  endmethod.
endclass.