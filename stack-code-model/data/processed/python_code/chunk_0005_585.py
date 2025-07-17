class ZCL_ALV_CONFIG definition
  public
  create public .

public section.

  class-methods CLASS_CONSTRUCTOR .
  class-methods GET_TEXT
    importing
      !IM_ALV_KEY type ZZE_ALV_KEY
      !IM_COLUMN_NAME type ZZE_ALV_COL_NAME
    returning
      value(RE_TEXT) type TEXT30 .
  class-methods EXISTS_TEXT
    importing
      !IM_ALV_KEY type ZZE_ALV_KEY
      !IM_COLUMN_NAME type ZZE_ALV_COL_NAME
    returning
      value(RE_FLAG) type BOOLEAN_FLG .
  class-methods GET_HEADER
    importing
      !IM_ALV_KEY type ZZE_ALV_KEY
    returning
      value(RE_TABLE) type ZZT_ALV_HEADER .
  class-methods IS_ACTIVE
    importing
      !IM_ALV_KEY type ZZE_ALV_KEY
      !IM_COLUMN_NAME type ZZE_ALV_COL_NAME
    returning
      value(RE_FLAG) type BOOLEAN_FLG .
  class-methods GET_FUNCTIONS
    importing
      !IM_ALV_KEY type ZZE_ALV_KEY
    returning
      value(RE_TABLE) type ZZT_ALV_FUNC .
  class-methods IS_HOTSPOT
    importing
      !IM_ALV_KEY type ZZE_ALV_KEY
      !IM_COLUMN_NAME type ZZE_ALV_COL_NAME
    returning
      value(RE_FLAG) type BOOLEAN_FLG .
  class-methods GET_CHILD_ALV
    importing
      !IM_ALV_KEY type ZZE_ALV_KEY
      !IM_SEQNR type ZZE_ALV_SEQNR
    returning
      value(RE_RETURN) type ZZE_ALV_KEY .
protected section.
private section.

  class-data AT_ALV_COLUMNS type ZZT_ALV_COLUMN .
  class-data AT_ALV_HEADER type ZZT_ALV_HEADER .
  class-data AT_ALV_FUNCTIONS type ZZT_ALV_FUNC .
  class-data AT_ALV_SEQUENCE type ZZT_ALV_SEQU .
ENDCLASS.



CLASS ZCL_ALV_CONFIG IMPLEMENTATION.


method CLASS_CONSTRUCTOR.

  select * from ZHRT_ALV_COLUMN into table at_alv_columns.

  select * from ZHRT_ALV_HEADER into table at_alv_header.

  select * from ZHRT_ALV_FUNC into table at_alv_functions.

  select * from ZHRT_ALV_SEQU into table at_alv_sequence.

  endmethod.


method EXISTS_TEXT.

  data lv_alv_column type ZHRT_ALV_COLUMN.

  read table at_alv_columns transporting no fields with key alv_key = im_alv_key
                                                        column_name = im_column_name.
  if sy-subrc eq 0.
    re_flag = 'X'.
  endif.

  endmethod.


method GET_CHILD_ALV.

  data lv_line type line of zzt_alv_sequ.

  read table at_alv_sequence into lv_line with key alv_parent = im_alv_key
                                                   alv_seqnr = im_seqnr.

  re_return = lv_line-alv_child.

  endmethod.


method GET_FUNCTIONS.

  data lv_line type zhrt_alv_func.

  loop at at_alv_functions into lv_line where alv_key = im_alv_key.
    insert lv_line into table re_table.
  endloop.

  endmethod.


method GET_HEADER.

  data lv_line type line of zzt_alv_header.

  loop at at_alv_header into lv_line where alv_key = im_alv_key.
    insert lv_line into table re_table.
  endloop.

  endmethod.


method GET_TEXT.

  data lv_alv_column type ZHRT_ALV_COLUMN.

  read table at_alv_columns into lv_alv_column with key alv_key = im_alv_key
                                                        column_name = im_column_name.

  re_text = lv_alv_column-text.

  endmethod.


method IS_ACTIVE.

  data lv_alv_column type ZHRT_ALV_COLUMN.

  read table at_alv_columns into lv_alv_column with key alv_key = im_alv_key
                                                        column_name = im_column_name.
  if sy-subrc eq 0.
    if lv_alv_column-active ne 'X'.
      clear re_flag.
    else.
      re_flag = 'X'.
    endif.
  else.
    re_flag = 'X'.
  endif.

  endmethod.


method IS_HOTSPOT.

  data lv_alv_column type ZHRT_ALV_COLUMN.

  read table at_alv_columns into lv_alv_column with key alv_key = im_alv_key
                                                        column_name = im_column_name.
  if sy-subrc eq 0.
    re_flag = lv_alv_column-hotspot.
  else.
    clear re_flag.
  endif.

  endmethod.
ENDCLASS.