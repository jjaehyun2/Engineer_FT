class ZCL_AOT_TIMER definition
  public
  create public .

public section.

  methods STOP
    returning
      value(RV_MILLI) type INTEGER .
  methods CONSTRUCTOR .
protected section.
private section.

  data MV_START type INTEGER .
ENDCLASS.



CLASS ZCL_AOT_TIMER IMPLEMENTATION.


  METHOD constructor.

    GET RUN TIME FIELD mv_start.

  ENDMETHOD.


  METHOD stop.

    DATA: lv_stop TYPE i.

    GET RUN TIME FIELD lv_stop.

    rv_milli = lv_stop - mv_start.

  ENDMETHOD.
ENDCLASS.