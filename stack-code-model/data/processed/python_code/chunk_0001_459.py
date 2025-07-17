class ZCL_UT_PG_ACCESSOR_FACTORY definition
  public
  final
  create public .

  public section.

    class-methods get_data_accessor
      returning
        value(ri_da) type ref to zif_ut_pg_data_accessor.

    class-methods inject_data_accessor
      importing
        ii_da type ref to zif_ut_pg_data_accessor optional.

  protected section.
  private section.
    class-data gi_da type ref to zif_ut_pg_data_accessor.
ENDCLASS.



CLASS ZCL_UT_PG_ACCESSOR_FACTORY IMPLEMENTATION.


  method get_data_accessor.
    if gi_da is not bound.
      create object gi_da type zcl_ut_pg_data_accessor.
    endif.
    ri_da = gi_da.
  endmethod.


  method inject_data_accessor.
    gi_da = ii_da.
  endmethod.
ENDCLASS.