CLASS zcl_test_super DEFINITION
  PUBLIC
  CREATE PUBLIC .

  PUBLIC SECTION.

    INTERFACES zif_test .

  PROTECTED SECTION.
  PRIVATE SECTION.
endclass.



class zcl_test_super implementation.


  METHOD zif_test~get_1.
    rv_result = 'SUPER!'.
  ENDMETHOD.


  METHOD zif_test~get_2.
    rv_result = 'SUPER!'.
  ENDMETHOD.
endclass.