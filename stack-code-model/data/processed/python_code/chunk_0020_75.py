class ZCL_UT_PG_DATA_ACCESSOR definition
  public
  final
  create public .

  public section.
    interfaces zif_ut_pg_data_accessor.
  protected section.
  private section.
ENDCLASS.



CLASS ZCL_UT_PG_DATA_ACCESSOR IMPLEMENTATION.


  method zif_ut_pg_data_accessor~get_flights.

    select * from sflight into table rt_flights
      where carrid = i_carrid
      and connid = i_connid.

  endmethod.
ENDCLASS.