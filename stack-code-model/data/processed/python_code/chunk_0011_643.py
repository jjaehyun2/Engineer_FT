*&---------------------------------------------------------------------*
*&---------------------------------------------------------------------*

METHOD example_01.
  TYPES:
    " Document structure
    BEGIN OF ts_root,
      title  TYPE char15,
      text   TYPE string,
      int    TYPE i,
      bottom TYPE string, " Any field could be REF TO, STRUCTURE or TABLE
    END OF ts_root.

  DATA:
    lo_file TYPE REF TO zif_xtt_file,
    ls_root TYPE ts_root.

  " No need to fill for empty template
  IF p_temp <> abap_true.
    ls_root-title   = 'Document title'. "#EC NOTEXT
    ls_root-text    = 'Just string'. "#EC NOTEXT
    ls_root-int     = 3.
    ls_root-bottom  = 'bottom'. "#EC NOTEXT
  ENDIF.

  " Show data structure only
  IF p_stru = abap_true.
    check_break_point_id( ).
    BREAK-POINT ID zxtt_break_point. " Double click here --> ls_root <--
    RETURN.
  ENDIF.

  " Info about template & the main class itself
  CREATE OBJECT:
   lo_file TYPE zcl_xtt_file_smw0 EXPORTING
     iv_objid = iv_template,

   ro_xtt TYPE (iv_class_name) EXPORTING
    io_file = lo_file.

  " Paste data
  IF p_temp <> abap_true.
    " R is a marker in the IV_TEMPLATE
    ro_xtt->merge( is_block = ls_root iv_block_name = 'R' ).
  ENDIF.
ENDMETHOD.