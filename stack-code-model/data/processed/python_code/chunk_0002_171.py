class zcl_portal_static definition
  public
  final
  create public .

*"* public components of class ZCL_PORTAL_STATIC
*"* do not include other source files here!!!
  public section.

    class-methods navigate
      importing
        !ir_controller type ref to if_wd_component
        !i_system      type simple optional
        !i_object_type type simple
        !i_operation   type simple
        !it_params     type wdy_key_value_listgen .
    class-methods navigate_absolute
      importing
        !ir_controller type ref to if_wd_component
        !i_path        type simple
        !i_mode        type simple default if_wd_portal_integration=>co_show_inplace
        !i_post        type wdy_boolean optional
        !it_params     type wdy_key_value_listgen optional .
  protected section.
*"* protected components of class ZCL_PORTAL_STATIC
*"* do not include other source files here!!!
  private section.
*"* private components of class ZCL_PORTAL_STATIC
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCL_PORTAL_STATIC IMPLEMENTATION.


  method navigate.

    data lr_portal type ref to if_wd_portal_integration.
    lr_portal = ir_controller->get_portal_manager( ).

    lr_portal->navigate_to_object(
      system              = i_system
      object_type         = i_object_type
      operation           = i_operation
      business_parameters = it_params ).

  endmethod.


  method navigate_absolute.

    data lr_portal type ref to if_wd_portal_integration.
    lr_portal = ir_controller->get_portal_manager( ).

    lr_portal->navigate_absolute(
      navigation_target   = i_path
      navigation_mode     = if_wd_portal_integration=>co_show_external
      "window_features     = 'toolbar=no,resizable=yes,scrollbars=yes'
      business_parameters = it_params
      post_parameters     = i_post ).

  endmethod.
ENDCLASS.