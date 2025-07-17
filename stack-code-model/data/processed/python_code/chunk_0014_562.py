class ZCL_ARDRONE_HANDLER definition
  public
  inheriting from Y_ADL_RES_BASE
  final
  create public .

public section.
*"* public components of class ZCL_ARDRONE_HANDLER
*"* do not include other source files here!!!

  methods GET
    importing
      !MATCHES type STRINGTAB optional .
*"* protected components of class ZCL_ARDRONE_HANDLER
*"* do not include other source files here!!!
protected section.
private section.
*"* private components of class ZCL_ARDRONE_HANDLER
*"* do not include other source files here!!!

  methods GET_COMMAND_LIST .
ENDCLASS.



CLASS ZCL_ARDRONE_HANDLER IMPLEMENTATION.


method GET.
  DATA: command TYPE string.

  READ TABLE matches INTO command INDEX 1.
  IF sy-subrc = 0.
    TRANSLATE command TO UPPER CASE.
    TRY.
        CALL METHOD zcl_ardrone_control=>(command).
        app( `{ "response": "Command ` && command && ` sent to Drone" }` ).
      CATCH cx_root.
        app( `{ "response": "ARDroid command ` && command && ` not known" }`).
    ENDTRY.
  ELSE.
    get_command_list( ).
  ENDIF.

  response->append_cdata( payload ).

  response->if_http_entity~set_content_type( 'application/json'   ).

endmethod.


method GET_COMMAND_LIST.
  DATA: url_prefix TYPE string
        VALUE 'http://demojam.yelcho.com.au/ardrone/command',
        lv_method TYPE tmdir-methodname.

*  app( `{<br/>` ). "cl_abap_char_utilities=>cr_lf ).
*  app( `&nbsp;&nbsp;"commands":<br/>`  ).
*  app( `&nbsp;&nbsp;&nbsp;&nbsp;[` && `<br/>`  ).
*  SELECT methodname FROM tmdir
*    INTO lv_method
*    WHERE classname = 'ZCL_ARDRONE_CONTROL'.
*    CHECK lv_method IS NOT INITIAL.
*    check lv_method ne 'SEND_COMMAND'.
*    TRANSLATE lv_method TO LOWER CASE.
*    app( `&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ "command": "` && lv_method &&
*          `", "url": "<a href="` && url_prefix && `/` &&
*          lv_method && `">` && url_prefix && `/` && lv_method && `</a> },` && `<br/>` ).
*  ENDSELECT.
*    app( `&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ "command": "` && `flattrim` &&
*          `", "url": "<a href="./` &&
*          lv_method && `">` && url_prefix && `/` && `flattrim` && `</a> },` && `<br/>` ).
*  app( `&nbsp;&nbsp;&nbsp;&nbsp;]` && `<br/>`  ).
*  app( `}` && `<br/>`  ).

  app( `{` ). "cl_abap_char_utilities=>cr_lf ).
  app( `"commands":`  ).
  app( `[` ).
  SELECT methodname FROM tmdir
    INTO lv_method
    WHERE classname = 'ZCL_ARDRONE_CONTROL'.
    CHECK lv_method IS NOT INITIAL.
    check lv_method ne 'SEND_COMMAND'.
    TRANSLATE lv_method TO LOWER CASE.
    app( `{ "command": "` && lv_method &&
          `", "url": "` && url_prefix && `/` &&
          lv_method && `" },` ).
  ENDSELECT.
    app( `{ "command": "` && `flattrim` &&
          `", "url": "` && url_prefix && `/` &&
          `flattrim` && `" }` ).
  app( `]` ).
  app( `}` ).

endmethod.
ENDCLASS.