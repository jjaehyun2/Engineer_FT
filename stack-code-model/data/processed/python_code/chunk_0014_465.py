class ZCL_EXCEL_STATIC definition
  public
  final
  create public .

*"* public components of class ZCL_EXCEL_STATIC
*"* do not include other source files here!!!
public section.

  types:
    begin of ts_row,
        cell1(255),
        cell2(255),
        cell3(255),
        cell4(255),
        cell5(255),
        cell6(255),
        cell7(255),
        cell8(255),
        cell9(255),
        cell10(255),
        cell11(255),
        cell12(255),
        cell13(255),
        cell14(255),
        cell15(255),
        cell16(255),
        cell17(255),
        cell18(255),
        cell19(255),
        cell20(255),
        cell21(255),
        cell22(255),
        cell23(255),
        cell24(255),
        cell25(255),
        cell26(255),
        cell27(255),
        cell28(255),
        cell29(255),
        cell30(255),
        cell31(255),
        cell32(255),
        cell33(255),
        cell34(255),
        cell35(255),
        cell36(255),
        cell37(255),
        cell38(255),
        cell39(255),
        cell40(255),
        cell41(255),
        cell42(255),
        cell43(255),
        cell44(255),
        cell45(255),
        cell46(255),
        cell47(255),
        cell48(255),
        cell49(255),
        cell50(255),
        cell51(255),
        cell52(255),
        cell53(255),
        cell54(255),
        cell55(255),
        cell56(255),
        cell57(255),
        cell58(255),
        cell59(255),
        cell60(255),
        cell61(255),
        cell62(255),
        cell63(255),
        cell64(255),
        cell65(255),
        cell66(255),
        cell67(255),
        cell68(255),
        cell69(255),
        cell70(255),
        cell71(255),
        cell72(255),
        cell73(255),
        cell74(255),
        cell75(255),
        cell76(255),
        cell77(255),
        cell78(255),
        cell79(255),
        cell80(255),
        cell81(255),
        cell82(255),
        cell83(255),
        cell84(255),
        cell85(255),
        cell86(255),
        cell87(255),
        cell88(255),
        cell89(255),
        cell90(255),
        cell91(255),
        cell92(255),
        cell93(255),
        cell94(255),
        cell95(255),
        cell96(255),
        cell97(255),
        cell98(255),
        cell99(255),
        cell100(255),
      end of ts_row .
  types:
    tt_rows type table of ts_row .

  constants TRUE type CHAR10 value '-1'. "#EC NOTEXT
  constants FALSE type CHAR10 value '0'. "#EC NOTEXT
  constants COLOR_46 type CHAR10 value '46'. "#EC NOTEXT
  constants COLOR_50 type CHAR10 value '50'. "#EC NOTEXT
  constants COLOR_37 type CHAR10 value '37'. "#EC NOTEXT
  constants COLOR_36 type CHAR10 value '36'. "#EC NOTEXT
  constants COLOR_AUTOMATIC type CHAR10 value '-4105'. "#EC NOTEXT
  constants COLOR_NONE type CHAR10 value '-4142'. "#EC NOTEXT
  constants COLOR_WHITE type CHAR10 value '2'. "#EC NOTEXT
  constants COLOR_BLACK type CHAR10 value '1'. "#EC NOTEXT
  constants PATTERN_AUTOMATIC type CHAR10 value '-4105'. "#EC NOTEXT
  constants PATTERN_GRAY8 type CHAR10 value '18'. "#EC NOTEXT
  constants PATTERN_GRAY16 type CHAR10 value '17'. "#EC NOTEXT
  constants PATTERN_LIGHT_DOWN type CHAR10 value '13'. "#EC NOTEXT
  constants XL_MAXIMIZED type I value -4137. "#EC NOTEXT

  class-methods CONVERT_VALUE
    importing
      !I_VALUE type SIMPLE
    returning
      value(E_VALUE) type STRING .
protected section.
*"* protected components of class ZCL_EXCEL_STATIC
*"* do not include other source files here!!!
private section.
*"* private components of class ZCL_EXCEL_STATIC
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCL_EXCEL_STATIC IMPLEMENTATION.


method convert_value.

  e_value = i_value.

  replace '.' in e_value with ','.

  find '-' in e_value.
  if sy-subrc eq 0.
    replace '-' with space into e_value.
    concatenate '-' e_value into e_value.
    condense e_value.
  endif.

endmethod.                    "CONVERT_VALUE
ENDCLASS.