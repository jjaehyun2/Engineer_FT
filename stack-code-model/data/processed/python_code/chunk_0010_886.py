class ZCL_ARDRONE_DISPATCHER definition
  public
  inheriting from Y_ADL_DISP_BASE
  final
  create public .

*"* public components of class ZCL_ARDRONE_DISPATCHER
*"* do not include other source files here!!!
public section.

  methods IF_HTTP_EXTENSION~HANDLE_REQUEST
    redefinition .
*"* protected components of class ZCL_ARDRONE_DISPATCHER
*"* do not include other source files here!!!
protected section.
*"* private components of class ZCL_ARDRONE_DISPATCHER
*"* do not include other source files here!!!
private section.
ENDCLASS.



CLASS ZCL_ARDRONE_DISPATCHER IMPLEMENTATION.


method IF_HTTP_EXTENSION~HANDLE_REQUEST.

*  handler( p = '^/$' h = 'Y_ADL_SAMPLE_HANDLER' ).
*  handler( p ='^/channel/([^/]+)/sub/([^/]+)/$' h = 'Y_ADL_SAMPLE_HANDLER' ).

  handler( p ='^/$' h = 'ZCL_ARDRONE_HANDLER' ).
  handler( p ='^/command$' h = 'ZCL_ARDRONE_HANDLER' ).
  handler( p ='^/command/([^/]+)$' h = 'ZCL_ARDRONE_HANDLER' ).

  dispatch( server ).

endmethod.
ENDCLASS.