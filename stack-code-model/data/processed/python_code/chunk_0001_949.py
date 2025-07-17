CLASS zcl_test DEFINITION
  PUBLIC
  INHERITING FROM zcl_test_super
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.

    ALIASES get_2
      FOR zif_test~get_2 .

    METHODS zif_test~get_1
        REDEFINITION .
    METHODS zif_test~get_2
        REDEFINITION .
PROTECTED SECTION.
  PRIVATE SECTION.
endclass.



class zcl_test implementation.


  method ZIF_TEST~GET_1.
    rv_result = 'REDEFINED!'.
  endmethod.


  METHOD zif_test~get_2.
    rv_result = 'REDEFINED!'.
  ENDMETHOD.
endclass.