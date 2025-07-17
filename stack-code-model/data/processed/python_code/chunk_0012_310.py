"! <p class="shorttext synchronized" lang="en">HTML Message</p>
CLASS zcl_html_msg DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.

    "! <p class="shorttext synchronized" lang="en">Class constructor</p>
    CLASS-METHODS class_constructor .

    "! <p class="shorttext synchronized" lang="en">get instance for this class</p>
    "!
    "! @parameter ro_object      | Returns object of this class
    CLASS-METHODS get_instance
      RETURNING VALUE(ro_object) TYPE REF TO zcl_html_msg.

      "! <p class="shorttext synchronized" lang="en">Show Message</p>
      "!
      "! @parameter im_msg     | Bal Message
         METHODS show
      IMPORTING
        im_msg TYPE bal_s_msg.

  PROTECTED SECTION.

  PRIVATE SECTION.
"! <p class="shorttext synchronized" lang="en">instance</p>
    CLASS-DATA o_instance TYPE REF TO zcl_html_msg.

    CLASS-DATA mo_box TYPE REF TO cl_gui_dialogbox_container.
    CLASS-DATA mo_html TYPE REF TO cl_gui_html_viewer.

    DATA mv_short TYPE string.
    DATA mt_long  TYPE htmltable.
    DATA ms_msg TYPE bal_s_msg.

    CLASS-METHODS build_box.
    CLASS-METHODS handle_close FOR EVENT close OF cl_gui_dialogbox_container.

    METHODS get_message_short RETURNING VALUE(rv_message) TYPE string.
    METHODS get_accordion_long RETURNING VALUE(rt_html) TYPE htmltable.
    METHODS show_message.
ENDCLASS.



CLASS zcl_html_msg IMPLEMENTATION.

  METHOD class_constructor.
    o_instance = NEW #(  ).
  ENDMETHOD.

  METHOD get_instance.
    ro_object = o_instance.
  ENDMETHOD.

  METHOD show.
    ms_msg = im_msg.
    build_box( ).
    mv_short = get_message_short( ).
    mt_long  = get_accordion_long( ).
    show_message( ).
  ENDMETHOD.

  METHOD get_accordion_long.

    DATA ls_header           TYPE thead.
    DATA l_id TYPE n LENGTH 2.
    DATA lt_itf_text         TYPE STANDARD TABLE OF tline.
    DATA lt_html_text        TYPE STANDARD TABLE OF htmlline.

    DATA lv_object                 TYPE dokhl-object.


    CALL FUNCTION 'DOCU_OBJECT_NAME_CONCATENATE'
      EXPORTING
        docu_id  = 'NA'
        element  = ms_msg-msgid
        addition = ms_msg-msgno
      IMPORTING
        object   = lv_object.


    CALL FUNCTION 'DOCU_GET'
      EXPORTING
        id     = 'NA'
        langu  = sy-langu
        object = lv_object
      IMPORTING
        head   = ls_header
      TABLES
        line   = lt_itf_text
      EXCEPTIONS
        OTHERS = 5.

    DATA(lt_conv_parformats) = VALUE tlinetab(
             ( tdformat = 'U1' tdline = '<h2><div class="w3-panel w3-blue">' )
             ( tdformat = 'U2' tdline = '<h3><div class="w3-panel w3-light-blue">' )
             ( tdformat = 'U3' tdline = '<h3><div class="w3-panel w3-sand">' )
             ( tdformat = 'AS' tdline = '<div class="w3-margin">' )
             ( tdformat = '*' tdline = '<div class="w3-margin">' )
             ( tdformat = 'PE' tdline = '<div class="w3-margin w3-light-grey">' )
             ( tdformat = 'B1' tdline = '<div class="w3-container w3-margin">' ) ).

    CALL FUNCTION 'CONVERT_ITF_TO_HTML'
      EXPORTING
        i_header          = ls_header
        i_html_header     = abap_false
      TABLES
        t_itf_text        = lt_itf_text
        t_html_text       = rt_html
        t_conv_parformats = lt_conv_parformats
      EXCEPTIONS
        OTHERS            = 4.

    DATA(lt_header) = VALUE htmltable(
             ( tdline = '<html><head>' )
             ( tdline = '<meta http-equiv="content-type" content="text/html; charset=utf-8">' )
             ( tdline = '<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">' )
             ( tdline = '<title>test</title></head><body>' )
             ( tdline = |<h1><div class="w3-panel w3-red">{ mv_short }</div></h1>| ) ).
    INSERT LINES OF lt_header INTO rt_html INDEX 1.

    DATA(lt_script) = VALUE htmltable(
             ( tdline = '    <script> ' )
             ( tdline = 'function myFunction(id) {' )
             ( tdline = '    var x = document.getElementById(id);' )
             ( tdline = '    if (x.className.indexOf("w3-show") == -1) {' )
             ( tdline = '        x.className += " w3-show";' )
             ( tdline = '    } else { ' )
             ( tdline = '        x.className = x.className.replace(" w3-show", "");' )
             ( tdline = '    }' )
             ( tdline = '}' )
             ( tdline = '</script>' ) ).
    APPEND LINES OF lt_script TO rt_html.

    DATA(lt_style) = VALUE htmltable(
                         ( tdline = '<style type="text/css">body { overflow: hidden; }</style>' ) ).

    APPEND LINES OF lt_style TO rt_html.

    APPEND '</body></html>' TO rt_html.


    LOOP AT rt_html ASSIGNING FIELD-SYMBOL(<html>).
      IF <html>(4) = '<h2>'.
        IF l_id IS NOT INITIAL.
          APPEND '</div>' TO lt_html_text.
        ENDIF.
        ADD 1 TO l_id.
        APPEND |<button onclick="myFunction('{ l_id }')" class="w3-btn w3-block w3-light-blue w3-left-align">| TO lt_html_text.
        APPEND <html> TO lt_html_text.
        APPEND |</button>| TO lt_html_text.
        APPEND |<div id="{ l_id }" class="w3-container w3-hide">| TO lt_html_text.
      ELSE.
        APPEND <html> TO lt_html_text.
      ENDIF.
    ENDLOOP.

    rt_html = lt_html_text.
  ENDMETHOD.

  METHOD get_message_short.
    MESSAGE ID ms_msg-msgid
          TYPE ms_msg-msgty
        NUMBER ms_msg-msgno
          WITH ms_msg-msgv1 ms_msg-msgv2 ms_msg-msgv3 ms_msg-msgv4
          INTO rv_message.
  ENDMETHOD.

  METHOD build_box.
    IF mo_box IS INITIAL.
      mo_box  = NEW #( width = 900 height = 400 top = 20 left = 400 ).
      mo_html = NEW #( parent = mo_box ).
      SET HANDLER handle_close FOR mo_box.
    ENDIF.
    mo_box->set_caption( 'Message' ).
  ENDMETHOD.

  METHOD handle_close.
    mo_box->set_visible( space ).
  ENDMETHOD.

  METHOD show_message.
    DATA lv_url TYPE c LENGTH 1000.
    mo_html->load_data( EXPORTING encoding     = 'utf-8'
                        IMPORTING assigned_url = lv_url
                        CHANGING  data_table   = mt_long ).
    mo_html->show_data( url = lv_url ).
    CLEAR ms_msg.
  ENDMETHOD.

ENDCLASS.