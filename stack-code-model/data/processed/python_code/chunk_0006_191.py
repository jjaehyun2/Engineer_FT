class ZCL_SB_AOC_2020_D2 definition
  public
  final
  create public .

public section.

  interfaces ZIF_SB_AOC_2020 .
protected section.
private section.
ENDCLASS.



CLASS ZCL_SB_AOC_2020_D2 IMPLEMENTATION.


  METHOD zif_sb_aoc_2020~solve.

    DATA: BEGIN OF ls_list,
            lowest   TYPE string,
            highest  TYPE string,
            letter   TYPE string,
            password TYPE string,
          END OF ls_list.
    DATA lv_part1 TYPE i.
    DATA lv_part2 TYPE i.

    LOOP AT it_input INTO DATA(ls_input).

      SPLIT ls_input AT '-' INTO ls_list-lowest ls_list-highest.
      SPLIT ls_list-highest AT space INTO ls_list-highest ls_list-letter ls_list-password.
      REPLACE ALL OCCURRENCES OF ':' IN ls_list-letter WITH space.

      FIND ALL OCCURRENCES OF ls_list-letter IN ls_list-password MATCH COUNT DATA(lv_count).
      IF lv_count GE ls_list-lowest AND lv_count LE ls_list-highest.
        lv_part1 = lv_part1 + 1.
      ENDIF.
      DATA(lv_low) = ls_list-lowest - 1.
      DATA(lv_high) = ls_list-highest - 1.

      IF ( ls_list-password+lv_low(1) = ls_list-letter AND ls_list-password+lv_high(1) NE ls_list-letter )
      OR ( ls_list-password+lv_low(1) NE ls_list-letter AND ls_list-password+lv_high(1) = ls_list-letter ).
        lv_part2 = lv_part2 + 1.
      ENDIF.

    ENDLOOP.

    rv_output = |{ 'Part 1:' } { lv_part1 } { 'Part 2:' } { lv_part2 } |.

  ENDMETHOD.
ENDCLASS.