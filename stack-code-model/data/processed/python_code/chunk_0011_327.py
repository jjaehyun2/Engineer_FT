class ZCL_UT_PG_FLIGHT_STATS definition
  public
  final
  create public .

  public section.

    types:
      begin of ty_average_payment,
        average type sflight-paymentsum,
        count type i,
      end of ty_average_payment.

    methods constructor .
    methods get_average_payments
      importing
        !i_carrid type sflight-carrid
        !i_connid type sflight-connid
      returning
        value(rs_average) type ty_average_payment .
  protected section.
  private section.
    data mi_da type ref to zif_ut_pg_data_accessor.
ENDCLASS.



CLASS ZCL_UT_PG_FLIGHT_STATS IMPLEMENTATION.


  method constructor.
    mi_da = zcl_ut_pg_accessor_factory=>get_data_accessor( ).
  endmethod.


  method get_average_payments.

    data lt_flights type table of sflight.
    data lv_total type sflight-paymentsum.
    field-symbols <i> like line of lt_flights.

    lt_flights = mi_da->get_flights(
      i_carrid = i_carrid
      i_connid = i_connid ).

    if lines( lt_flights ) = 0.
      return.
    endif.

    loop at lt_flights assigning <i>.
      lv_total = lv_total + <i>-paymentsum.
    endloop.

    rs_average-count   = lines( lt_flights ).
    rs_average-average = lv_total / rs_average-count.

  endmethod.
ENDCLASS.