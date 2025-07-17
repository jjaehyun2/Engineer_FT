class ZCL_UI5_STATIC definition
  public
  final
  create public .

public section.

  class-methods GET_URL
    importing
      !I_APP type SIMPLE
      !I_PAGE type SIMPLE default 'index.html'
      !I_GUID type SIMPLE
      !IT_PARAMETERS type TIHTTPNVP
      !I_HTTPS type ABAP_BOOL default ABAP_TRUE
      !I_LANGUAGE type LANGU default SY-LANGU
    returning
      value(E_URL) type STRING .
protected section.
private section.
ENDCLASS.



CLASS ZCL_UI5_STATIC IMPLEMENTATION.


method get_url.

  e_url =
    zcl_bsp_static=>get_url(
      i_app         = i_app
      i_page        = i_page
      i_guid        = i_guid
      i_https       = i_https
      i_language    = i_language
      it_parameters = it_parameters ).

  replace 'bsp' in e_url with 'ui5_ui5'.

endmethod.
ENDCLASS.