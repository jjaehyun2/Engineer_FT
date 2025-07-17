*&---------------------------------------------------------------------*
*& Report ztest_flight_occupancy
*&---------------------------------------------------------------------*
*&
*&---------------------------------------------------------------------*
REPORT ztest_flight_occupancy.

CLASS occupancy DEFINITION FOR TESTING DURATION SHORT
    RISK LEVEL DANGEROUS.

    PRIVATE SECTION.

        METHODS setup.

        " should be 3 seats in economy class and
        " 2 seats in business class
        METHODS should_be_3_2_seats FOR TESTING.

        " no booking for this flight
        METHODS should_be_empty FOR TESTING.

ENDCLASS.

CLASS occupancy IMPLEMENTATION.

    METHOD setup.
        DATA: bookings TYPE STANDARD TABLE OF sbook,
              flight TYPE sflight.

        flight = VALUE #( carrid = 'EK' connid = '371' fldate = '20190910' seatsmax = 500 seatsocc = 450 ).
        MODIFY sflight FROM flight.

        DELETE FROM sbook WHERE carrid = flight-carrid AND connid = flight-connid
            AND fldate = flight-fldate.

        flight = VALUE #( carrid = 'EK' connid = '371' fldate = '20190930' seatsmax = 500 seatsocc = 490 ).
        MODIFY sflight FROM flight.

        DELETE FROM sbook WHERE carrid = flight-carrid AND connid = flight-connid
            AND fldate = flight-fldate.

        bookings = VALUE #(
        ( carrid = flight-carrid connid = flight-connid fldate = flight-fldate
          bookid = 1 class = 'Y' cancelled = abap_true )
        ( carrid = flight-carrid connid = flight-connid fldate = flight-fldate
          bookid = 2 class = 'Y' )
        ( carrid = flight-carrid connid = flight-connid fldate = flight-fldate
          bookid = 3 class = 'Y' )
        ( carrid = flight-carrid connid = flight-connid fldate = flight-fldate
          bookid = 4 class = 'Y' )
        ( carrid = flight-carrid connid = flight-connid fldate = flight-fldate
          bookid = 5 class = 'C' cancelled = abap_true )
        ( carrid = flight-carrid connid = flight-connid fldate = flight-fldate
          bookid = 6 class = 'C' )
        ( carrid = flight-carrid connid = flight-connid fldate = flight-fldate
          bookid = 7 class = 'C' )
        ).

        INSERT sbook FROM TABLE bookings.
        COMMIT WORK AND WAIT.

    ENDMETHOD.

    METHOD should_be_3_2_seats.
        DATA: act_flight_occupancy TYPE STANDARD TABLE OF zflight_occupancy,
              exp_flight_occupancy LIKE act_flight_occupancy.

        exp_flight_occupancy = VALUE #(
        ( carrid = 'EK' connid = '371' fldate = '20190930' seatsocc = 3
          seatsocc_b = 2 )
        ).
        SELECT * FROM zflight_occupancy INTO TABLE @act_flight_occupancy
          WHERE carrid = 'EK' AND connid = '371' AND fldate = '20190930'
          AND cancelled = @abap_false.

        cl_abap_unit_assert=>assert_equals( exp = exp_flight_occupancy
            act = act_flight_occupancy ).

    ENDMETHOD.

    METHOD should_be_empty.
        DATA: act_flight_occupancy TYPE STANDARD TABLE OF zflight_occupancy.

        SELECT * FROM zflight_occupancy INTO TABLE @act_flight_occupancy
          WHERE carrid = 'EK' AND connid = '371' AND fldate = '20190910'
          AND cancelled = @abap_false.

        cl_abap_unit_assert=>assert_subrc( exp = 4 ).

    ENDMETHOD.

ENDCLASS.