class ZCL_SB_AOC_2020_D3 definition
  public
  final
  create public .

public section.

  interfaces ZIF_SB_AOC_2020 .
protected section.
private section.
ENDCLASS.



CLASS ZCL_SB_AOC_2020_D3 IMPLEMENTATION.


  METHOD zif_sb_aoc_2020~solve.
    DATA lv_lengo TYPE i.
    DATA lv_ifrom TYPE i.
    DATA lv_trees TYPE string.
    DATA lv_right TYPE i.
    DATA lv_down TYPE i.

    DATA(ls_input) = it_input[ 1 ].
    DATA(lv_len) = strlen( ls_input ).

    "Part1
    lv_right = '3'.
    LOOP AT it_input INTO ls_input FROM 2.
      lv_lengo = lv_lengo + lv_right.
      IF lv_lengo GE lv_len.
        lv_lengo = lv_lengo - lv_len.
      ENDIF.
      IF ls_input+lv_lengo(1) = '#'.
        lv_trees = lv_trees + 1.
      ENDIF.
    ENDLOOP.
    DATA(lv_part1) = lv_trees.

    "Part2
    DATA(lv_part2) = lv_part1.
    DO 4 TIMES.
      CLEAR lv_trees.
      CLEAR lv_down.
      CLEAR lv_lengo.
      CLEAR lv_ifrom.
      CASE sy-index.
        WHEN 1."Right 1, down 1.
          lv_right = 1.
*        WHEN 2."Right 1, down 1. "Already added in part1.
*          lv_right = 3.
*          lv_down = 1.
        WHEN 2."Right 5, down 1.
          lv_right = 5.
        WHEN 3."Right 7, down 1.
          lv_right = 7.
        WHEN 4."Right 1, down 2.
          lv_right = 1.
          lv_down = 1.
        WHEN OTHERS.
      ENDCASE.

      LOOP AT it_input INTO ls_input FROM 2.
        IF lv_down GT lv_ifrom.
          lv_ifrom = lv_ifrom + 1.
          CONTINUE.
        ELSE.
          lv_ifrom = 0.
          lv_lengo = lv_lengo + lv_right.
          IF lv_lengo GE lv_len.
            lv_lengo = lv_lengo - lv_len.
          ENDIF.
          IF ls_input+lv_lengo(1) = '#'.
            lv_trees = lv_trees + 1.
          ENDIF.
        ENDIF.
      ENDLOOP.
      lv_part2 = lv_trees * lv_part2.
    ENDDO.

    rv_output = |{ 'Part 1:' } { lv_part1 } { 'Part 2:' } { lv_part2 } |.

  ENDMETHOD.
ENDCLASS.