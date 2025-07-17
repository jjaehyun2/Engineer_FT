class ZCL_BSP_STATIC definition
  public
  final
  create public .

*"* public components of class ZCL_BSP_STATIC
*"* do not include other source files here!!!
public section.

  class-methods GET_URL
    importing
      !I_APP type STRING
      !I_PAGE type STRING default 'index.html'
      !I_GUID type SIMPLE optional
      !I_LANGUAGE type LANGU default SY-LANGU
      !IT_PARAMETERS type TIHTTPNVP optional
      !I_HTTPS type ABAP_BOOL default ABAP_FALSE
    returning
      value(E_URL) type STRING .
  class-methods GET_PARAMETER
    importing
      !I_NAME type SIMPLE
      !I_STRICT type ABAP_BOOL default ABAP_FALSE
    returning
      value(E_VALUE) type STRING
    raising
      ZCX_GENERIC .
  class-methods FORBIDDEN
    importing
      !I_REASON type SIMPLE optional
    raising
      ZCX_GENERIC .
  class-methods FILE_DOWNLOAD
    importing
      !I_FILE type SIMPLE
      !I_MIME type SIMPLE default 'application/octet-stream'
      !I_DATA type XSTRING
    raising
      ZCX_GENERIC .
protected section.
*"* protected components of class ZCL_BSP_STATIC
*"* do not include other source files here!!!
private section.
*"* private components of class ZCL_BSP_STATIC
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCL_BSP_STATIC IMPLEMENTATION.


method FILE_DOWNLOAD.

    data l_content_disposition type string.
    l_content_disposition = 'attachment; file="%FILE%"'.

    replace '%FILE%' in l_content_disposition with i_file.

    data l_content_type type string.
    l_content_type = i_mime.

    data lr_runtime type ref to cl_bsp_runtime.
    lr_runtime =  cl_bsp_runtime=>get_runtime_instance( ).

    data lr_navigation type ref to cl_bsp_navigation.
    create object lr_navigation
      exporting
        runtime = lr_runtime.

    cl_bsp_utility=>download(
      object_s            = i_data
      content_type        = l_content_type
      content_disposition = l_content_disposition
      response            = lr_runtime->server->response
      navigation          = lr_navigation ).

  endmethod.


method FORBIDDEN.

    if i_reason is supplied.
      data l_reason type string.
      l_reason = i_reason.
    endif.

    data lr_runtime type ref to cl_bsp_runtime.
    lr_runtime ?= cl_bsp_runtime=>get_runtime_instance( ).

    lr_runtime->server->response->set_status(
      code   = 404
      reason = l_reason ).

  endmethod.


method GET_PARAMETER.

    data lr_runtime type ref to cl_bsp_runtime.
    lr_runtime ?= cl_bsp_runtime=>get_runtime_instance( ).

    if lr_runtime is not bound.
      if i_strict eq abap_true.
        zcx_generic=>raise( ).
      else.
        return.
      endif.
    endif.

    data: lt_fields type tihttpnvp.
    lr_runtime->server->request->get_form_fields(
      changing fields = lt_fields ).

    data ls_field like line of lt_fields.
    read table lt_fields into ls_field
      with key name = i_name.
    if sy-subrc ne 0.
      if i_strict eq abap_true.
        zcx_generic=>raise( ).
      else.
        return.
      endif.
    endif.

    e_value = ls_field-value.

  endmethod.


method get_url.

  data l_app type string.
  l_app = i_app.

  data l_page type string.
  l_page = i_page.

  data lt_parameters like it_parameters.
  lt_parameters = it_parameters.

  field-symbols <ls_parameter> like line of lt_parameters.
  read table lt_parameters transporting no fields
    with key
      name = 'sap-ui-language'.
  if sy-subrc ne 0.
    append initial line to lt_parameters assigning <ls_parameter>.
    <ls_parameter>-name  = 'sap-ui-language'.
    <ls_parameter>-value = zcl_abap_static=>write( i_language ).
  endif.

  if i_guid is not initial.
    append initial line to lt_parameters assigning <ls_parameter>.
    <ls_parameter>-name  = 'guid'.
    <ls_parameter>-value = i_guid.
  endif.

  if i_https eq abap_true.

    cl_bsp_runtime=>if_bsp_runtime~construct_bsp_url(
      exporting
        in_protocol    = 'https'
        in_application = l_app
        in_page        = l_page
        in_parameters	 = lt_parameters
      importing
        out_abs_url    = e_url ).

  else.

    cl_bsp_runtime=>if_bsp_runtime~construct_bsp_url(
      exporting
        in_application = l_app
        in_page        = l_page
        in_parameters	 = lt_parameters
      importing
        out_abs_url    = e_url ).

  endif.

endmethod.
ENDCLASS.