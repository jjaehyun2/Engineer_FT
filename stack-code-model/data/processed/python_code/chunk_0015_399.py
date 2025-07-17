class z_cl_binary_operations definition
  public
  final
  create public .

  public section.
    methods:
      dec_to_bin
        importing
          iv_dec              type i
        returning
          value(rv_bin_repre) type string,

      bin_to_dec
        importing
          iv_bin              type string
        returning
          value(rv_dec_repre) type i,

      dec_digit_to_four_bits
        importing
          iv_dec_digit        type c
        returning
          value(rv_four_bits) type char4.
  protected section.
  private section.
endclass.



class z_cl_binary_operations implementation.
  method dec_to_bin.
    data(lv_input_number) = iv_dec.

    while lv_input_number > 0.
      if ( lv_input_number mod 2 ) = 1.
        concatenate '1' rv_bin_repre into rv_bin_repre.
        lv_input_number = lv_input_number - 1.
      else.
        concatenate '0' rv_bin_repre into rv_bin_repre.
      endif.

      lv_input_number = lv_input_number / 2.
    endwhile.

    if strlen( rv_bin_repre ) = 0.
      rv_bin_repre = '0'.
    endif.
  endmethod.

  method bin_to_dec.
    data lv_power type i value 0.
    data(lv_input_binary) = iv_bin.

    while strlen( lv_input_binary ) > 0.
      data(ls_length) = strlen( lv_input_binary ).
      data(ls_last_bit) = substring( val = lv_input_binary off = ls_length - 1 ).

      rv_dec_repre = rv_dec_repre + ( ls_last_bit * ( 2 ** lv_power ) ).
      lv_power = lv_power + 1.

      lv_input_binary = substring( val = lv_input_binary len = ls_length - 1 ).
    endwhile.
  endmethod.

  method dec_digit_to_four_bits.
    data(ls_bin_representation) = dec_to_bin( conv #( iv_dec_digit ) ).

    while strlen( ls_bin_representation ) < 4.
      concatenate '0' ls_bin_representation into ls_bin_representation.
    endwhile.

    rv_four_bits = ls_bin_representation.
  endmethod.

endclass.