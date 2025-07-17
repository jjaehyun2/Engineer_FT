class cl_abap_browser definition public.

  public section.

    types:
  html_line type c length 255 .
    types:
  html_table type standard table of html_line with non-unique key table_line .
    types:
  begin of load_tab_line,
      name type        string,
      type type        string,
      dref type ref to data,
    end of load_tab_line .
    types:
  load_tab type hashed table of load_tab_line with unique key name .
    types:
  title type c length 255 .

    constants navigate_html type c length 1 value 'X' ##NO_TEXT.
    constants navigate_html_after_sap_event like navigate_html value 'E' ##NO_TEXT.
    constants navigate_off like navigate_html value ' ' ##NO_TEXT.
    constants small type string value 'S' ##NO_TEXT.
    constants medium type string value 'M' ##NO_TEXT.
    constants large type string value 'L' ##NO_TEXT.
    constants xlarge type string value 'XL' ##NO_TEXT.
    constants vlarge type string value 'XXL' ##NO_TEXT.
    constants portrait type string value 'P' ##NO_TEXT.
    constants landscape type string value 'L' ##NO_TEXT.
    constants topleft type string value 'TL' ##NO_TEXT.
    constants middle type string value 'M' ##NO_TEXT.

    class-methods show_html
    importing
      !html type cl_abap_browser=>html_table optional
      !title type cl_abap_browser=>title optional
      !size type string default cl_abap_browser=>medium
      value(modal) type abap_bool default abap_true
      !html_string type string optional
      !printing type abap_bool default abap_false
      !buttons like navigate_html default navigate_off
      !format type string default cl_abap_browser=>landscape
      !position type string default cl_abap_browser=>topleft
      !data_table type load_tab optional
      !anchor type string optional
      !context_menu type abap_bool default abap_false
      !html_xstring type xstring optional
      !check_html type abap_bool default abap_true
      !container type ref to cl_gui_container optional
      !dialog type abap_bool default abap_true
    exporting
      !html_errors type standard table .
    class-methods show_xml
    importing
      !xml_string type string optional
      !xml_xstring type xstring optional
      !title type cl_abap_browser=>title optional
      !size type string default cl_abap_browser=>medium
      value(modal) type abap_bool default abap_true
      !printing type abap_bool default abap_false
      !buttons like navigate_html default navigate_off
      !format type string default cl_abap_browser=>landscape
      !position type string default cl_abap_browser=>topleft
      !context_menu type abap_bool default abap_false
      !container type ref to cl_gui_container optional
      !check_xml type abap_bool default abap_true
      !dialog type abap_bool default abap_true
    preferred parameter xml_string .
    class-methods close_browser .
    class-methods show_url
    importing
      !url type csequence
      !title type cl_abap_browser=>title optional
      !size type string default cl_abap_browser=>medium
      value(modal) type abap_bool default abap_true
      !printing type abap_bool default abap_false
      !buttons like navigate_html default navigate_off
      !format type string default cl_abap_browser=>landscape
      !position type string default cl_abap_browser=>topleft
      !container type ref to cl_gui_container optional
      !context_menu type abap_bool default abap_false
      !dialog type abap_bool default abap_true .
    methods create_browser
    importing
      !container type ref to cl_gui_container optional .


endclass.

class cl_abap_browser implementation.

endclass.