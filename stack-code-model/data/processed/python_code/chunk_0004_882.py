class lcx_excel definition inheriting from zcx_mlt_error.
  public section.
    class-methods excel_error
      importing
        msg type string
        rc  type ty_rc optional
      raising
        lcx_excel.
endclass.

class lcx_excel implementation.
  method excel_error.
    data:
      begin of ls_split_msg,
        a1 like a1,
        a2 like a1,
        a3 like a1,
        a4 like a1,
      end of ls_split_msg.

    ls_split_msg = msg.

    raise exception type lcx_excel
      exporting
        msg = msg
        rc  = rc
        a1  = ls_split_msg-a1
        a2  = ls_split_msg-a2
        a3  = ls_split_msg-a3
        a4  = ls_split_msg-a4.
  endmethod.
endclass.

**********************************************************************

interface lif_excel.

  types:
    begin of ty_sheet_content,
      cell_row    type int4,
      cell_column type int4,
      cell_value  type string,
      cell_coords type string,
      cell_style  type i,
      data_type   type string,
    end of ty_sheet_content,
    tt_sheet_content type standard table of ty_sheet_content with default key.

  types:
    begin of ty_style,
      id     type i,
      format type string,
    end of ty_style,
    tt_styles type standard table of ty_style with key id.

  methods get_sheet_names
    returning
      value(rt_sheet_names) type string_table
    raising
      lcx_excel.

  methods get_sheet_content
    importing
      iv_sheet_name type string
    returning
      value(rt_content) type tt_sheet_content
    raising
      lcx_excel.

  methods get_styles
    returning
      value(rt_styles) type tt_styles
    raising
      lcx_excel.

endinterface.