class ZCL_BDS_STATIC definition
  public
  final
  create public .

*"* public components of class ZCL_BDS_STATIC
*"* do not include other source files here!!!
public section.
  type-pools SBDST .

  class-methods READ
    importing
      !I_NAME type SBDST_CLASSNAME default 'SOFFICEINTEGRATION'
      !I_TYPE type BDS_CLSTYP default 'OT'
      !I_PATH type SIMPLE
    returning
      value(E_DATA) type XSTRING
    raising
      ZCX_GENERIC .
  class-methods GET_URL
    importing
      !I_NAME type SBDST_CLASSNAME default 'SOFFICEINTEGRATION'
      !I_TYPE type BDS_CLSTYP default 'OT'
      !I_PATH type SIMPLE
    returning
      value(E_URL) type STRING
    raising
      ZCX_GENERIC .
protected section.
*"* protected components of class ZCL_BDS_STATIC
*"* do not include other source files here!!!
private section.
*"* private components of class ZCL_BDS_STATIC
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCL_BDS_STATIC IMPLEMENTATION.


method get_url.

  data l_object type sbdst_object_key.
  data l_name   type string.
  split i_path at '/' into l_object l_name.

  data lt_signature type sbdst_signature.
  field-symbols <ls_signature> like line of lt_signature.
  append initial line to lt_signature assigning <ls_signature>.
  <ls_signature>-prop_name  = 'DESCRIPTION'.
  <ls_signature>-prop_value = l_name.

  data lt_components type sbdst_components.
  data lt_uris type sbdst_uri.
  cl_bds_document_set=>get_with_url(
    exporting
      classname  = i_name
      classtype  = i_type
      object_key = l_object
    changing
      signature  = lt_signature
      components = lt_components
      uris       = lt_uris
    exceptions
      others     = 1 ).
  if sy-subrc ne 0.
    zcx_generic=>raise( ).
  endif.

  if lt_uris is initial.
    message e001 with i_path into sy-title.
    zcx_generic=>raise( ).
  endif.

  data ls_uri like line of lt_uris.
  read table lt_uris into ls_uri index 1.

  e_url = ls_uri-uri.

endmethod.


method read.

  data l_object type sbdst_object_key.
  data l_name   type string.
  split i_path at '/' into l_object l_name.

  data lt_signature type sbdst_signature.
  field-symbols <ls_signature> like line of lt_signature.
  append initial line to lt_signature assigning <ls_signature>.
  <ls_signature>-prop_name  = 'DESCRIPTION'.
  <ls_signature>-prop_value = l_name.

  data lt_components type sbdst_components.
  cl_bds_document_set=>get_info(
    exporting
      classname  = i_name
      classtype  = i_type
      object_key = l_object
    changing
      signature  = lt_signature
      components = lt_components
    exceptions
      others     = 1 ).
  if sy-subrc ne 0.
    zcx_generic=>raise( ).
  endif.

  if lt_components is initial.
    message e001 with i_path into sy-title.
    zcx_generic=>raise( ).
  endif.

  data ls_component like line of lt_components.
  read table lt_components into ls_component index 1.

  data lt_content type sbdst_content.
  cl_bds_document_set=>get_with_table(
    exporting
      classname  = i_name
      classtype  = i_type
      object_key = l_object
    changing
      signature  = lt_signature
      content    = lt_content
    exceptions
      others     = 1 ).
  if sy-subrc ne 0.
    zcx_generic=>raise( ).
  endif.

  e_data =
    zcl_convert_static=>xtable2xtext(
      i_length = ls_component-comp_size
      it_data  = lt_content ).

endmethod.
ENDCLASS.