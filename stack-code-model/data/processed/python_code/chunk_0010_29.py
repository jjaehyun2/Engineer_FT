class ZCL_FLOW_TEST_030 definition
  public
  create public .

public section.

  methods TEST01
    importing
      !IV_WHERE type STRING .
  methods TEST02
    importing
      !IV_WHERE type STRING .
  methods TEST03
    importing
      !IV_WHERE type STRING .
  methods TEST04
    importing
      !IV_WHERE type STRING .
protected section.
private section.

  methods DEAD_END
    importing
      !IV_FOO type STRING
    returning
      value(RV_BAR) type STRING .
  methods MULTI
    importing
      !IV_IN1 type STRING
      !IV_IN2 type STRING
    exporting
      !EV_OUT1 type STRING
      !EV_OUT2 type STRING .
  methods NESTED
    importing
      !IV_FOO type STRING
    returning
      value(RV_MOO) type STRING .
  methods SEQUENTIAL
    importing
      !IV_FOO type STRING
      !IV_BAR type STRING
    returning
      value(RV_MOO) type STRING .
  methods UTIL
    importing
      !IV_FOO type STRING
    returning
      value(RV_BAR) type STRING .
ENDCLASS.



CLASS ZCL_FLOW_TEST_030 IMPLEMENTATION.


  METHOD DEAD_END.

* IV_FOO is not used

    rv_bar = 'sdf'.

  ENDMETHOD.


  METHOD MULTI.

* todo
    BREAK-POINT.

  ENDMETHOD.


  METHOD NESTED.

    rv_moo = iv_foo.

  ENDMETHOD.


  METHOD SEQUENTIAL.

    rv_moo = iv_foo && iv_bar.

  ENDMETHOD.


  METHOD TEST01.

    DATA(lv_sql) = sequential( iv_foo = util( 'foo' )
                               iv_bar = util( iv_where ) ).

    NEW zcl_flow_test_sql( lv_sql ).

  ENDMETHOD.


  METHOD TEST02.

    DATA(lv_sql) = nested( iv_foo = util( iv_foo = util( iv_foo = iv_where ) ) ).

    NEW zcl_flow_test_sql( lv_sql ).

  ENDMETHOD.


  METHOD TEST03.

    DATA(lv_sql) = sequential( iv_foo = util( 'foo' )
                               iv_bar = sequential( iv_foo = iv_where
                                                    iv_bar = 'sdf' ) ).

    NEW zcl_flow_test_sql( lv_sql ).

  ENDMETHOD.


  METHOD TEST04.

    DATA(lv_sql) = dead_end( iv_where ).

    NEW zcl_flow_test_sql( lv_sql ).

  ENDMETHOD.


  METHOD UTIL.

    rv_bar = iv_foo.

  ENDMETHOD.
ENDCLASS.