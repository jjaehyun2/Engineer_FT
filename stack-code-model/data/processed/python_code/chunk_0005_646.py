CLASS zunitdemo_simple DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.
    METHODS constructor
      IMPORTING
        date_for_test    TYPE d OPTIONAL
        actdate_provider TYPE REF TO zunitdemo_simple_actdate OPTIONAL
        actdate_interface TYPE REF TO zunitdemo_interface_actdate OPTIONAL.
    "! Returns the day of the actual date
    METHODS actual_day
      RETURNING
        VALUE(r_result) TYPE numc2.
    METHODS actual_day2
      RETURNING
        VALUE(r_result) TYPE numc2.
    METHODS actual_day3
      RETURNING
        VALUE(r_result) TYPE numc2.
    METHODS actual_day4
      RETURNING
        VALUE(r_result) TYPE numc2.

  PROTECTED SECTION.
  PRIVATE SECTION.
    DATA g_date_for_test TYPE d.
    DATA g_actdate_provider TYPE REF TO zunitdemo_simple_actdate.
    DATA g_actdate_interface TYPE REF TO zunitdemo_interface_actdate.
ENDCLASS.



CLASS ZUNITDEMO_SIMPLE IMPLEMENTATION.


  METHOD actual_day.

    " To be tested with test seams

    TEST-SEAM sy_datum.

      DATA(date) = sy-datum.
      " A change

    END-TEST-SEAM.

    r_result = date+6(2).

  ENDMETHOD.


  METHOD actual_day2.

    " Use a global parameter to enable unit testing

    IF g_date_for_test IS NOT INITIAL.
      DATA(date) = g_date_for_test.
    ELSE.
      date = sy-datum.
    ENDIF.

    r_result = date+6(2).

  ENDMETHOD.


  METHOD actual_day3.

    " Use a separate class with an instance methods
    " to get the actual date.
    " During tests inject a mock instance in the
    " constructor.

    DATA(date) = g_actdate_provider->get_date( ).

    r_result = date+6(2).

  ENDMETHOD.


  METHOD actual_day4.

    " Use an interface
    " to get the actual date.
    " Use the test double framework in the Unit Test.

    DATA(date) = g_actdate_interface->get_date( ).

    r_result = date+6(2).

  ENDMETHOD.


  METHOD constructor.

    g_date_for_test = date_for_test.
    g_actdate_provider = actdate_provider.
    g_actdate_interface = actdate_interface.

  ENDMETHOD.
ENDCLASS.