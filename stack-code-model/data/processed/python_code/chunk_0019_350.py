class ZCL_SB_AOC_2020_D1 definition
  public
  final
  create public .

public section.

  interfaces ZIF_SB_AOC_2020 .
protected section.
private section.
ENDCLASS.



CLASS ZCL_SB_AOC_2020_D1 IMPLEMENTATION.


  METHOD zif_sb_aoc_2020~solve.

    "Part1
    DATA(lt_input_tmp) = it_input[].
    LOOP AT it_input INTO DATA(ls_input).
      DATA(lv_index) = sy-tabix.
      lv_index = lv_index + 1.
      LOOP AT lt_input_tmp INTO DATA(ls_input_tmp) FROM lv_index.
        DATA(lv_sum) = ls_input + ls_input_tmp.
        IF lv_sum = '2020'.
          DATA(lv_part1) = ls_input * ls_input_tmp.
          EXIT.
        ENDIF.
      ENDLOOP.
      IF lv_sum = '2020'.
        EXIT.
      ENDIF.
    ENDLOOP.

    "Part2
    DATA(lt_input_tmp2) = it_input[].
    LOOP AT it_input INTO ls_input.
      lv_index = sy-tabix.
      lv_index = lv_index + 1.
      LOOP AT lt_input_tmp INTO ls_input_tmp FROM lv_index.
        DATA(lv_index2) = sy-tabix.
        lv_index2 = lv_index2 + 1.
        LOOP AT lt_input_tmp2 INTO DATA(ls_input_tmp2) FROM lv_index2.
          lv_sum = ls_input + ls_input_tmp + ls_input_tmp2.
          IF lv_sum = '2020'.
            DATA(lv_part2) = ls_input * ls_input_tmp * ls_input_tmp2.
            rv_output = |{ 'Part 1:' } { lv_part1 } { 'Part 2:' } { lv_part2 } |.
            RETURN.
          ENDIF.
        ENDLOOP.
      ENDLOOP.
    ENDLOOP.
  ENDMETHOD.
ENDCLASS.