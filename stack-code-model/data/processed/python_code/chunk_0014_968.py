class LCL_UNIT_TEST definition for testing FINAL
  duration short
  risk level harmless.

  private section.
    data F_CUT type ref to ZCL_WDC_SEARCH_ASSIST.  "class under test
    methods
    : SETUP
    , DO_SEARCH for testing
    .
endclass.       "lcl_Unit_Test

class LCL_UNIT_TEST implementation.

  method SETUP.
    F_CUT = new #( ).
  endmethod.

  method DO_SEARCH.
    "Дано: Строка поиска
    "Требуется: найти кол-во таб№№
    F_CUT->DO_SEARCH(
      exporting
        I_SEARCH = 'Иван'
      importing
        ET_P0001 = data(ET_P0001) ).

    "Ответ: 4
    CL_ABAP_UNIT_ASSERT=>ASSERT_EQUALS(
      ACT = LINES( ET_P0001 )
      EXP = 4
      MSG = 'Не то кол-во' ).
  endmethod.

endclass.