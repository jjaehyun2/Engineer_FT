class ZALGOR_CL_LTCD_HELPER definition
  public
  final
  create public .

public section.

  class-methods STRING_TO_INT_ARRAY
    importing
      !IV_STR type STRING
    returning
      value(RT_NUMS) type ZALGOR_IF_TOPS=>TT_INT .
  class-methods STRING_TO_INT_2D_ARRAY
    importing
      !IV_STR type STRING
    returning
      value(RT_NUMS_2D) type ZALGOR_IF_TOPS=>TT_INT_2D .
  class-methods ARRAY_TO_LISTNODE
    importing
      !IT_NUMS type ZALGOR_INT4_T
    returning
      value(RO_LN) type ref to ZALGOR_CL_LISTNODE .
protected section.
private section.
ENDCLASS.



CLASS ZALGOR_CL_LTCD_HELPER IMPLEMENTATION.


  method ARRAY_TO_LISTNODE.
  endmethod.


  METHOD STRING_TO_INT_2D_ARRAY.
    CHECK iv_str IS NOT INITIAL.
    SPLIT iv_str AT ';' INTO TABLE DATA(lt_arr_str).

    LOOP AT lt_arr_str ASSIGNING FIELD-SYMBOL(<lv_arr_str>).
      SPLIT <lv_arr_str> AT ',' INTO TABLE DATA(lt_arr).
      APPEND lt_arr TO rt_nums_2d.
    ENDLOOP.
  ENDMETHOD.


  METHOD STRING_TO_INT_ARRAY.
    CHECK iv_str IS NOT INITIAL.
    SPLIT iv_str AT ',' INTO TABLE DATA(lt_nums).
    rt_nums = lt_nums.
  ENDMETHOD.
ENDCLASS.