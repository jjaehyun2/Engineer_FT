class ZCL_THEME_RESTRICTION_EXAMPLE definition
  public
  final
  create public .

public section.

  interfaces IF_BADI_INTERFACE .
  interfaces ZIF_EX_FLP_THEME_RESTRICTION .
protected section.
private section.
ENDCLASS.



CLASS ZCL_THEME_RESTRICTION_EXAMPLE IMPLEMENTATION.


  method zif_ex_flp_theme_restriction~modify_allowed_themes.
    if user eq 'DEVELOPER'. "Default developer on NPL system
      " Keeps only High Contrast themes.
      delete themes where theme_id NP 'sap_belize_hc*'.
    endif.
  endmethod.
ENDCLASS.