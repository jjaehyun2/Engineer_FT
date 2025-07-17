class zcl_xml_static definition
  public
  final
  create public .

*"* public components of class ZCL_XML_STATIC
*"* do not include other source files here!!!
  public section.
    type-pools abap .

    constants true type text5 value 'true' ##NO_TEXT.
    constants false type text5 value 'false' ##NO_TEXT.

    class-methods date_in
      importing
        !i_date       type simple
      returning
        value(e_date) type d .
    class-methods date_time_in
      importing
        !i_date_time       type simple
      returning
        value(e_timestamp) type timestamp .
    class-methods date_time_out
      importing
        !i_timestamp       type timestamp
      returning
        value(e_date_time) type string .
    class-methods bool_in
      importing
        !i_value      type simple
      returning
        value(e_bool) type abap_bool .
    class-methods guid_in
      importing
        !i_guid       type simple
      returning
        value(e_guid) type guid .
    class-methods guid_out
      importing
        !i_guid       type guid
      returning
        value(e_guid) type string .
  protected section.
*"* protected components of class ZCL_XML_STATIC
*"* do not include other source files here!!!
  private section.
*"* private components of class ZCL_XML_STATIC
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCL_XML_STATIC IMPLEMENTATION.


  method bool_in.

    check i_value is not initial.

    cl_gdt_conversion=>indicator_inbound(
      exporting
        im_value = i_value
      importing
        ex_value = e_bool ).

  endmethod.


  method date_in.

    data l_date(10).
    l_date = i_date.

    replace all occurrences of '-' in l_date with ``.

    e_date = l_date.

  endmethod.


  method date_time_in.

    cl_gdt_conversion=>date_time_inbound(
      exporting
        im_value       =  i_date_time
      importing
        ex_value_short = e_timestamp ).

  endmethod.


  method date_time_out.

    cl_gdt_conversion=>date_time_outbound(
      exporting
        im_value_short = i_timestamp
      importing
        ex_value       = e_date_time ).

  endmethod.


  method guid_in.

    cl_gdt_conversion=>guid_inbound(
      exporting
        im_value  = i_guid
      importing
        ex_guid_x = e_guid ).

  endmethod.


  method guid_out.

    cl_gdt_conversion=>guid_outbound(
      exporting
        im_guid_x = i_guid
      importing
        ex_value  = e_guid ).

  endmethod.
ENDCLASS.