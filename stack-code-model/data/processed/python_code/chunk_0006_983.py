class Z2MSE_TEST_CL_A definition
  public
  create public .

public section.

  interfaces z2mse_test_if_a_00000000000000 .

  events EVENT_A .

  methods CONSTRUCTOR .
  methods METHOD_A .
  methods EVENTHANDLER_A
    for event EVENT_A of Z2MSE_TEST_CL_A .
  PROTECTED SECTION.
private section.
ENDCLASS.



CLASS Z2MSE_TEST_CL_A IMPLEMENTATION.


  METHOD constructor.

    SET HANDLER eventhandler_a FOR ALL INSTANCES.

  ENDMETHOD.


  METHOD eventhandler_a.

  ENDMETHOD.


  METHOD method_a.

    DATA z2mse_test_a TYPE z2mse_test_a.

    SELECT SINGLE * FROM z2mse_test_a INTO z2mse_test_a.

    RAISE EVENT event_a.

  ENDMETHOD.


  METHOD z2mse_test_if_a_00000000000000~method_a_000000000000000000000.
    data: class_b2 TYPE REF TO Z2MSE_TEST_CL_B2.
    class_b2 = new #( ).
    class_b2->method_a( ).
  ENDMETHOD.
ENDCLASS.