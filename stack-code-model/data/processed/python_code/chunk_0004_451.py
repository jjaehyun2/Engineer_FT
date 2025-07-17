class zcson_t_simple_class definition
  public
  create public .

  public section.
    methods:
      add
        importing
          iv_value type i,
      get_value
        returning
          value(rv_value) type i.

  protected section.
  private section.
    data:
      mv_number type i.
endclass.



class zcson_t_simple_class implementation.

  method add.

    try.
        me->mv_number = me->mv_number + iv_value.
      catch cx_root.
    endtry.

  endmethod.

  method get_value.

    rv_value = me->mv_number.

  endmethod.

endclass.