class ZCL_ARDRONE_BSP_APP definition
  public
  final
  create public .

*"* public components of class ZCL_ARDRONE_BSP_APP
*"* do not include other source files here!!!
public section.

  interfaces IF_BSP_APPLICATION_EVENTS .
*"* protected components of class ZCL_ARDRONE_BSP_APP
*"* do not include other source files here!!!
protected section.
*"* private components of class ZCL_ARDRONE_BSP_APP
*"* do not include other source files here!!!
private section.

  methods SEND_COMMAND
    importing
      !REQUEST type ref to IF_HTTP_REQUEST .
ENDCLASS.



CLASS ZCL_ARDRONE_BSP_APP IMPLEMENTATION.


method IF_BSP_APPLICATION_EVENTS~ON_REQUEST.

  CASE runtime->page_name.
    WHEN 'command.json'.
      send_command( request ).
    WHEN OTHERS.
  ENDCASE.

endmethod.


method IF_BSP_APPLICATION_EVENTS~ON_RESPONSE.
endmethod.


method IF_BSP_APPLICATION_EVENTS~ON_START.
endmethod.


method IF_BSP_APPLICATION_EVENTS~ON_STOP.
endmethod.


method SEND_COMMAND.
  DATA: command TYPE char20.

  command = request->get_form_field( 'command' ).

  CHECK command IS NOT INITIAL.

  TRANSLATE command to UPPER CASE.

  TRY.
      CALL METHOD zcl_ardrone_control=>(command).
    CATCH cx_root.
  ENDTRY.

endmethod.
ENDCLASS.