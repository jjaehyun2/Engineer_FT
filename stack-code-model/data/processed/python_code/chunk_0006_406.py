* https://github.com/boy0korea/ZWD_INSTANT_POPUP
REPORT zwd_instant_popup.

PARAMETERS: p_wdcomp TYPE wdy_component-component_name,
            p_title  TYPE string LOWER CASE.

**********************************************************************
START-OF-SELECTION.
**********************************************************************
  PERFORM execute.


**********************************************************************
* form
**********************************************************************
FORM execute.
  DATA: ls_assist             TYPE seoclskey,
        lv_error              TYPE flag,
        lv_devclass           TYPE devclass,
        lv_corrnr             TYPE trkorr,
        lo_component          TYPE REF TO if_wdy_md_component,
        lo_controller         TYPE REF TO if_wdy_md_controller,
        lo_method             TYPE REF TO if_wdy_md_controller_method,
        lo_parameter          TYPE REF TO if_wdy_md_parameter,
        lo_view               TYPE REF TO if_wdy_md_view,
        lo_action             TYPE REF TO if_wdy_md_action,
        lo_event_handler      TYPE REF TO if_wdy_md_ctlr_event_handler,
        lo_window             TYPE REF TO if_wdy_md_window,
        lo_window_node        TYPE REF TO if_wdy_md_vset_hierarchy_node,
        lo_view_usage         TYPE REF TO if_wdy_md_view_usage,
        lv_code_body          TYPE wdy_md_text,
        lv_description        TYPE wdy_md_description,
        lv_iwci               TYPE seoclsname,
        ls_class              TYPE vseoclass,
        lt_class_descriptions TYPE TABLE OF seoclasstx,
        ls_class_descriptions TYPE seoclasstx,
        ls_inheritance        TYPE vseoextend,
        lt_attribute          TYPE seoo_attributes_r,
        ls_attribute          TYPE seoo_attribute_r,
        lt_method             TYPE seoo_methods_r,
        ls_method             TYPE seoo_method_r,
        lt_param              TYPE seos_parameters_r,
        ls_param              TYPE seos_parameter_r,
        lt_method_source      TYPE seo_method_source_table,
        ls_method_source      TYPE seo_method_source,
        lt_objects            TYPE TABLE OF dwinactiv,
        ls_objects            TYPE dwinactiv,
        lo_cross              TYPE REF TO cl_wb_crossreference,
        lv_include            TYPE programm,
        lv_offset             TYPE i.

  " check exist WD
  lv_error = cl_wdy_md_component=>check_existency( p_wdcomp ).
  IF lv_error EQ abap_true.
    MESSAGE p_wdcomp && ` already exist` TYPE 'E'.
  ENDIF.

  " check exist class
  CASE p_wdcomp(1).
    WHEN '/'.
      FIND ALL OCCURRENCES OF '/' IN p_wdcomp MATCH OFFSET lv_offset.
      lv_offset = lv_offset + 1.
      ls_assist-clsname = p_wdcomp(lv_offset) && 'CL_' && p_wdcomp+lv_offset.
    WHEN 'Z' OR 'Y'.
      ls_assist-clsname = p_wdcomp(1) && 'CL_' && p_wdcomp.
    WHEN OTHERS.
      ls_assist-clsname = 'CL_' && p_wdcomp.
  ENDCASE.
  CALL FUNCTION 'SEO_CLASS_EXISTENCE_CHECK'
    EXPORTING
      clskey       = ls_assist
    EXCEPTIONS
      not_existing = 2
      OTHERS       = 6.
  IF sy-subrc <> 2.
    MESSAGE ls_assist-clsname && ` already exist` TYPE 'E'.
  ENDIF.

  cl_wdy_md_component=>create_complete(
    EXPORTING
      name          = p_wdcomp      " Component Name
    IMPORTING
      component     = lo_component " Component Reference
    CHANGING
      devclass      = lv_devclass  " Package
      corrnr        = lv_corrnr    " Request/Task
  ).
  lv_description = p_title.
  lo_component->if_wdy_md_object~set_description( lv_description ).
  lo_component->set_assistance_class( ls_assist-clsname ).
  lo_component->unlock( dequeue_synchron = 'X' ).      " global lock
  lo_component->lock( ).        " lock component definition

*         create implicit methods of component controller
  lo_controller = lo_component->get_component_controller( ).
  lo_controller->lock( ).
  cl_wdy_wb_method_ed=>create_predef_methods( lo_controller ).

  lo_method = lo_controller->create_method( name = 'OPEN_POPUP' ).
  lo_method->set_visibility( visibility = 2 ).
  CAST cl_wdy_md_procedure( lo_method )->set_is_interface_item( abap_true ).
  lo_parameter = lo_method->create_parameter( 'IO_COMP_USAGE' ).
  lo_parameter->set_abap_typing( 1 ).
  lo_parameter->set_abap_type( 'IF_WD_COMPONENT_USAGE' ).
  lo_parameter = lo_method->create_parameter( 'IO_EVENT_DATA' ).
  lo_parameter->set_abap_typing( 1 ).
  lo_parameter->set_abap_type( 'IF_FPM_PARAMETER' ).
  lv_code_body
   = `METHOD open_popup .` && cl_abap_char_utilities=>newline &&
     `` && cl_abap_char_utilities=>newline &&
     `  wd_assist->mo_event_data = io_event_data.` && cl_abap_char_utilities=>newline &&
     `  wd_assist->mo_comp_usage = io_comp_usage.` && cl_abap_char_utilities=>newline &&
     `` && cl_abap_char_utilities=>newline &&
     `` && cl_abap_char_utilities=>newline &&
     `` && cl_abap_char_utilities=>newline &&
     `  DATA lo_window_manager TYPE REF TO if_wd_window_manager.` && cl_abap_char_utilities=>newline &&
     `  DATA lo_api_component  TYPE REF TO if_wd_component.` && cl_abap_char_utilities=>newline &&
     `  DATA lo_window         TYPE REF TO if_wd_window.` && cl_abap_char_utilities=>newline &&
     `  DATA lt_buttons        TYPE wdr_popup_button_list.` && cl_abap_char_utilities=>newline &&
     `  DATA ls_canc_action    TYPE wdr_popup_button_action.` && cl_abap_char_utilities=>newline &&
     `` && cl_abap_char_utilities=>newline &&
     `  lo_api_component           = wd_this->wd_get_api( ).` && cl_abap_char_utilities=>newline &&
     `  lo_window_manager          = lo_api_component->get_window_manager( ).` && cl_abap_char_utilities=>newline &&
     `*   create the cancel icon, but without any action handler` && cl_abap_char_utilities=>newline &&
     `  ls_canc_action-action_name = '*'.` && cl_abap_char_utilities=>newline &&
     `*   Simple example, see docu of method create_and_open_popup for details` && cl_abap_char_utilities=>newline &&
     `  lt_buttons                 = lo_window_manager->get_buttons_ok(` && cl_abap_char_utilities=>newline &&
     `*      default_button       = if_wd_window=>co_button_ok` && cl_abap_char_utilities=>newline &&
     `   ).` && cl_abap_char_utilities=>newline &&
     `` && cl_abap_char_utilities=>newline &&
     `  lo_window                  = lo_window_manager->create_and_open_popup(` && cl_abap_char_utilities=>newline &&
     `      window_name          = 'W_MAIN'` && cl_abap_char_utilities=>newline &&
     `*      title                =` && cl_abap_char_utilities=>newline &&
     `      message_type         = if_wd_window=>co_msg_type_none` && cl_abap_char_utilities=>newline &&
     `      message_display_mode = if_wd_window=>co_msg_display_mode_selected` && cl_abap_char_utilities=>newline &&
     `*      is_resizable         = ABAP_TRUE` && cl_abap_char_utilities=>newline &&
     `      buttons              = lt_buttons` && cl_abap_char_utilities=>newline &&
     `      cancel_action        = ls_canc_action` && cl_abap_char_utilities=>newline &&
     `  ).` && cl_abap_char_utilities=>newline &&
     `` && cl_abap_char_utilities=>newline &&
     `` && cl_abap_char_utilities=>newline &&
     `  SET HANDLER wd_assist->on_close FOR lo_window.` && cl_abap_char_utilities=>newline &&
     `` && cl_abap_char_utilities=>newline &&
     `ENDMETHOD.` && cl_abap_char_utilities=>newline.
  lo_method->set_code_body( code_body = lv_code_body ).

*         create default window
*  lo_window = lo_component->create_window( name = 'W_MAIN' ).
  lo_window = cl_wdy_md_window=>create_complete(
      component_name  = p_wdcomp
      window_name = 'W_MAIN' ).
  lo_controller = lo_window->if_wdy_md_abstract_view~get_view_controller( ).
  cl_wdy_wb_method_ed=>create_predef_methods( lo_controller ).


*         create default view
*  lo_view = lo_component->create_view( name = 'V_MAIN' ).
  lo_view = cl_wdy_md_view=>create_complete(
      component_name  = p_wdcomp
      view_name = 'V_MAIN' ).
  lo_controller = lo_view->get_view_controller( ).
  cl_wdy_wb_method_ed=>create_predef_methods( lo_controller ).


  lo_event_handler = lo_controller->create_event_handler( 'ONACTIONPOPUP_BUTTON' ).
  lo_action = lo_controller->create_action( 'POPUP_BUTTON' ).
  lo_action->create_parameter( 'ID' )->set_abap_type( 'STRING' ).
  lo_action->set_event_handler( lo_event_handler ).
  lv_code_body
   = `METHOD onactionpopup_button .` && cl_abap_char_utilities=>newline &&
     `` && cl_abap_char_utilities=>newline &&
     `` && cl_abap_char_utilities=>newline &&
     `  CASE wdevent->name.` && cl_abap_char_utilities=>newline &&
     `    WHEN 'ON_OK'` && cl_abap_char_utilities=>newline &&
     `      OR 'ON_YES'.` && cl_abap_char_utilities=>newline &&
     `      " OK button` && cl_abap_char_utilities=>newline &&
     `      on_ok( ).` && cl_abap_char_utilities=>newline &&
     `    WHEN OTHERS.` && cl_abap_char_utilities=>newline &&
     `      " other button (Cancel, Close ...)` && cl_abap_char_utilities=>newline &&
     `      close_popup( ).` && cl_abap_char_utilities=>newline &&
     `  ENDCASE.` && cl_abap_char_utilities=>newline &&
     `ENDMETHOD.` && cl_abap_char_utilities=>newline.
  lo_event_handler->set_code_body( code_body = lv_code_body ).
  lo_method = lo_controller->create_method( 'CLOSE_POPUP' ).
  lv_code_body
   = `METHOD close_popup .` && cl_abap_char_utilities=>newline &&
     `  wd_this->wd_get_api( )->get_embedding_window( )->close( ).` && cl_abap_char_utilities=>newline &&
     `ENDMETHOD.` && cl_abap_char_utilities=>newline.
  lo_method->set_code_body( code_body = lv_code_body ).
  lo_method = lo_controller->create_method( 'DO_INIT' ).
  lo_parameter = lo_method->create_parameter( 'IO_VIEW' ).
  lo_parameter->set_abap_typing( 1 ).
  lo_parameter->set_abap_type( 'IF_WD_VIEW' ).
  lv_code_body
   = `METHOD do_init .` && cl_abap_char_utilities=>newline &&
     `  DATA: lo_popup TYPE REF TO if_wd_window.` && cl_abap_char_utilities=>newline &&
     `` && cl_abap_char_utilities=>newline &&
     `  lo_popup = wd_this->wd_get_api( )->get_embedding_window( ).` && cl_abap_char_utilities=>newline &&
     `  IF lo_popup IS NOT INITIAL AND lo_popup->is_modal( ) EQ abap_true.` && cl_abap_char_utilities=>newline &&
     `    lo_popup->set_window_title( '` && p_title && `' ).` && cl_abap_char_utilities=>newline &&
     `    lo_popup->set_close_button( abap_true ).` && cl_abap_char_utilities=>newline &&
     `    lo_popup->set_close_in_any_case( abap_false ).` && cl_abap_char_utilities=>newline &&
     `    lo_popup->set_button_kind( if_wd_window=>co_buttons_okcancel ).` && cl_abap_char_utilities=>newline &&
     `    lo_popup->set_default_button( if_wd_window=>co_button_none ).` && cl_abap_char_utilities=>newline &&
     `    lo_popup->set_on_close_action(` && cl_abap_char_utilities=>newline &&
     `      EXPORTING` && cl_abap_char_utilities=>newline &&
     `        view               = io_view` && cl_abap_char_utilities=>newline &&
     `        action_name        = 'POPUP_BUTTON'` && cl_abap_char_utilities=>newline &&
     `    ).` && cl_abap_char_utilities=>newline &&
     `    lo_popup->subscribe_to_button_event(` && cl_abap_char_utilities=>newline &&
     `      EXPORTING` && cl_abap_char_utilities=>newline &&
     `        button            = if_wd_window=>co_button_ok` && cl_abap_char_utilities=>newline &&
     `        action_name       = 'POPUP_BUTTON'` && cl_abap_char_utilities=>newline &&
     `        action_view       = io_view` && cl_abap_char_utilities=>newline &&
     `    ).` && cl_abap_char_utilities=>newline &&
     `    lo_popup->subscribe_to_button_event(` && cl_abap_char_utilities=>newline &&
     `      EXPORTING` && cl_abap_char_utilities=>newline &&
     `        button            = if_wd_window=>co_button_cancel` && cl_abap_char_utilities=>newline &&
     `        action_name       = 'POPUP_BUTTON'` && cl_abap_char_utilities=>newline &&
     `        action_view       = io_view` && cl_abap_char_utilities=>newline &&
     `    ).` && cl_abap_char_utilities=>newline &&
     `  ENDIF.` && cl_abap_char_utilities=>newline &&
     `` && cl_abap_char_utilities=>newline &&
     `*  io_view->request_focus_on_view_elem( io_view->get_element( 'UI_EL_ID' ) ).` && cl_abap_char_utilities=>newline &&
     `` && cl_abap_char_utilities=>newline &&
     `ENDMETHOD.` && cl_abap_char_utilities=>newline.
  lo_method->set_code_body( code_body = lv_code_body ).
  lo_method = lo_controller->create_method( 'ON_OK' ).
  lv_code_body
   = `METHOD on_ok .` && cl_abap_char_utilities=>newline &&
     `` && cl_abap_char_utilities=>newline &&
     `  wd_assist->on_ok(` && cl_abap_char_utilities=>newline &&
     `*    EXPORTING` && cl_abap_char_utilities=>newline &&
     `*      iv_value = return_value` && cl_abap_char_utilities=>newline &&
     `  ).` && cl_abap_char_utilities=>newline &&
     `  close_popup( ).` && cl_abap_char_utilities=>newline &&
     `` && cl_abap_char_utilities=>newline &&
     `ENDMETHOD.` && cl_abap_char_utilities=>newline.
  lo_method->set_code_body( code_body = lv_code_body ).
  lv_code_body
   = `METHOD wddomodifyview .` && cl_abap_char_utilities=>newline &&
     `  IF first_time EQ abap_true.` && cl_abap_char_utilities=>newline &&
     `    do_init( view ).` && cl_abap_char_utilities=>newline &&
     `  ENDIF.` && cl_abap_char_utilities=>newline &&
     `ENDMETHOD.` && cl_abap_char_utilities=>newline.
  lo_controller->get_method( 'WDDOMODIFYVIEW' )->set_code_body( code_body = lv_code_body ).


*         embed view into window
  IF lo_window IS BOUND AND lo_view IS BOUND.
*           create the "view usage" node:
    lo_view_usage ?= lo_window->create_root_node(
         name   = 'V_MAIN_USAGE_0'
         type   = if_wdy_md_vset_hierarchy_node=>co_view_usage ).
*           put the view into the view usage:
    lo_view_usage->set_view( view = lo_view ).
*           set this new node as default:
    lo_window->set_default_root_node( default_root_node = lo_view_usage ).
  ENDIF.


  lo_component->save_to_database( ).
  lo_component->unlock( ).
  lo_component->get_component_controller( )->save_to_database( ).
  lo_component->get_component_controller( )->unlock( ).
  lo_window->if_wdy_md_abstract_view~save_to_database( ).
  lo_window->if_wdy_md_abstract_view~unlock( ).
  lo_window->if_wdy_md_abstract_view~get_view_controller( )->save_to_database( ).
  lo_window->if_wdy_md_abstract_view~get_view_controller( )->unlock( ).
  lo_view->if_wdy_md_abstract_view~save_to_database( ).
  lo_view->if_wdy_md_abstract_view~unlock( ).
  lo_view->if_wdy_md_abstract_view~get_view_controller( )->save_to_database( ).
  lo_view->if_wdy_md_abstract_view~get_view_controller( )->unlock( ).


  ls_class-clsname = ls_assist-clsname.
  ls_class-exposure = 2.
  ls_class-fixpt = abap_true.
  ls_class-unicode = abap_true.
  ls_class_descriptions-clsname = ls_assist-clsname.
  ls_class_descriptions-langu = sy-langu.
  ls_class_descriptions-descript = p_title.
  APPEND ls_class_descriptions TO lt_class_descriptions.
  ls_inheritance-clsname = ls_assist-clsname.
  ls_inheritance-refclsname = 'CL_WD_COMPONENT_ASSISTANCE'.
  ls_inheritance-state = 1.

  lv_iwci = cl_wdy_wb_naming_service=>get_abap_intf_for_component( p_wdcomp ).
  CLEAR: ls_attribute.
  ls_attribute-clsname = ls_assist-clsname.
  ls_attribute-cmpname = 'GO_WD_COMP'.
  ls_attribute-exposure = 2.
  ls_attribute-state = 1.
  ls_attribute-attdecltyp = 1.
  ls_attribute-attrdonly = abap_true.
  ls_attribute-typtype = 3.
  ls_attribute-type = lv_iwci.
  APPEND ls_attribute TO lt_attribute.
  CLEAR: ls_attribute.
  ls_attribute-clsname = ls_assist-clsname.
  ls_attribute-cmpname = 'GV_WD_COMP_ID'.
  ls_attribute-exposure = 2.
  ls_attribute-state = 1.
  ls_attribute-attdecltyp = 1.
  ls_attribute-attrdonly = abap_true.
  ls_attribute-typtype = 1.
  ls_attribute-type = 'STRING'.
  APPEND ls_attribute TO lt_attribute.
  CLEAR: ls_attribute.
  ls_attribute-clsname = ls_assist-clsname.
  ls_attribute-cmpname = 'MO_COMP_USAGE'.
  ls_attribute-exposure = 2.
  ls_attribute-state = 1.
  ls_attribute-typtype = 3.
  ls_attribute-type = 'IF_WD_COMPONENT_USAGE'.
  APPEND ls_attribute TO lt_attribute.
  CLEAR: ls_attribute.
  ls_attribute-clsname = ls_assist-clsname.
  ls_attribute-cmpname = 'MO_EVENT_DATA'.
  ls_attribute-exposure = 2.
  ls_attribute-state = 1.
  ls_attribute-typtype = 3.
  ls_attribute-type = 'IF_FPM_PARAMETER'.
  APPEND ls_attribute TO lt_attribute.

  CLEAR: ls_method.
  ls_method-clsname = ls_assist-clsname.
  ls_method-cmpname = 'README'.
  ls_method-exposure = 1.
  ls_method-state = 1.
  ls_method-mtdtype = 2.
  ls_method-mtddecltyp = 1.
  APPEND ls_method TO lt_method.
  CLEAR: ls_method_source.
  ls_method_source-cpdname = 'README'.
  APPEND `  METHOD readme.` TO ls_method_source-source.
  APPEND `* https://github.com/boy0korea/ZWD_INSTANT_POPUP` TO ls_method_source-source.
  APPEND `  ENDMETHOD.` TO ls_method_source-source.
  APPEND ls_method_source TO lt_method_source.

  CLEAR: ls_method.
  ls_method-clsname = ls_assist-clsname.
  ls_method-cmpname = 'CLASS_CONSTRUCTOR'.
  ls_method-exposure = 2.
  ls_method-state = 1.
  ls_method-mtdtype = 2.
  ls_method-mtddecltyp = 1.
  APPEND ls_method TO lt_method.
  CLEAR: ls_method_source.
  ls_method_source-cpdname = 'CLASS_CONSTRUCTOR'.
  APPEND `  METHOD class_constructor.` TO ls_method_source-source.
  APPEND `    gv_wd_comp_id = CAST cl_abap_refdescr( cl_abap_typedescr=>describe_by_data( go_wd_comp ) )->get_referenced_type( )->get_relative_name( ).` TO ls_method_source-source.
  APPEND `    REPLACE 'IWCI_' IN gv_wd_comp_id WITH ''.` TO ls_method_source-source.
  APPEND `  ENDMETHOD.` TO ls_method_source-source.
  APPEND ls_method_source TO lt_method_source.

  CLEAR: ls_method.
  ls_method-clsname = ls_assist-clsname.
  ls_method-cmpname = 'DO_CALLBACK'.
  ls_method-exposure = 1.
  ls_method-state = 1.
  APPEND ls_method TO lt_method.
  CLEAR: ls_method_source.
  ls_method_source-cpdname = 'DO_CALLBACK'.
  APPEND `  METHOD do_callback.` TO ls_method_source-source.
  APPEND `    DATA: lv_event_id   TYPE fpm_event_id,` TO ls_method_source-source.
  APPEND `          lo_fpm        TYPE REF TO if_fpm,` TO ls_method_source-source.
  APPEND `          lo_event      TYPE REF TO cl_fpm_event,` TO ls_method_source-source.
  APPEND `          lo_event_orig TYPE REF TO cl_fpm_event,` TO ls_method_source-source.
  APPEND `          lt_key        TYPE TABLE OF string,` TO ls_method_source-source.
  APPEND `          lv_key        TYPE string,` TO ls_method_source-source.
  APPEND `          lr_value      TYPE REF TO data,` TO ls_method_source-source.
  APPEND `          lv_action     TYPE string,` TO ls_method_source-source.
  APPEND `          lo_view       TYPE REF TO cl_wdr_view,` TO ls_method_source-source.
  APPEND `          lo_action     TYPE REF TO if_wdr_action,` TO ls_method_source-source.
  APPEND `          lt_param      TYPE wdr_name_value_list,` TO ls_method_source-source.
  APPEND `          ls_param      TYPE wdr_name_value.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `**********************************************************************` TO ls_method_source-source.
  APPEND `* FPM` TO ls_method_source-source.
  APPEND `**********************************************************************` TO ls_method_source-source.
  APPEND `    mo_event_data->get_value(` TO ls_method_source-source.
  APPEND `      EXPORTING` TO ls_method_source-source.
  APPEND `        iv_key   = 'IV_CALLBACK_EVENT_ID'` TO ls_method_source-source.
  APPEND `      IMPORTING` TO ls_method_source-source.
  APPEND `        ev_value = lv_event_id` TO ls_method_source-source.
  APPEND `    ).` TO ls_method_source-source.
  APPEND `    IF lv_event_id IS NOT INITIAL.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `      lo_fpm = cl_fpm=>get_instance( ).` TO ls_method_source-source.
  APPEND `      CHECK: lo_fpm IS NOT INITIAL.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `      CREATE OBJECT lo_event` TO ls_method_source-source.
  APPEND `        EXPORTING` TO ls_method_source-source.
  APPEND `          iv_event_id   = lv_event_id` TO ls_method_source-source.
  APPEND `          io_event_data = mo_event_data.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `      mo_event_data->get_value(` TO ls_method_source-source.
  APPEND `        EXPORTING` TO ls_method_source-source.
  APPEND `          iv_key   = 'IO_EVENT_ORIG'` TO ls_method_source-source.
  APPEND `        IMPORTING` TO ls_method_source-source.
  APPEND `          ev_value = lo_event_orig` TO ls_method_source-source.
  APPEND `      ).` TO ls_method_source-source.
  APPEND `      IF lo_event_orig IS NOT INITIAL.` TO ls_method_source-source.
  APPEND `        lo_event->ms_source_uibb = lo_event_orig->ms_source_uibb.` TO ls_method_source-source.
  APPEND `      ENDIF.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `      lo_fpm->raise_event( lo_event ).` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `    ENDIF.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `**********************************************************************` TO ls_method_source-source.
  APPEND `* WD` TO ls_method_source-source.
  APPEND `**********************************************************************` TO ls_method_source-source.
  APPEND `    mo_event_data->get_value(` TO ls_method_source-source.
  APPEND `      EXPORTING` TO ls_method_source-source.
  APPEND `        iv_key   = 'IV_CALLBACK_ACTION'` TO ls_method_source-source.
  APPEND `      IMPORTING` TO ls_method_source-source.
  APPEND `        ev_value = lv_action` TO ls_method_source-source.
  APPEND `    ).` TO ls_method_source-source.
  APPEND `    IF lv_action IS NOT INITIAL.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `      mo_event_data->get_value(` TO ls_method_source-source.
  APPEND `        EXPORTING` TO ls_method_source-source.
  APPEND `          iv_key   = 'IO_VIEW'` TO ls_method_source-source.
  APPEND `        IMPORTING` TO ls_method_source-source.
  APPEND `          ev_value = lo_view` TO ls_method_source-source.
  APPEND `      ).` TO ls_method_source-source.
  APPEND `      CHECK: lo_view IS NOT INITIAL.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `      TRY.` TO ls_method_source-source.
  APPEND `          lo_action = lo_view->get_action_internal( lv_action ).` TO ls_method_source-source.
  APPEND `        CATCH cx_wdr_runtime INTO DATA(lx_wdr_runtime).` TO ls_method_source-source.
  APPEND `          wdr_task=>application->component->if_wd_controller~get_message_manager( )->report_error_message( lx_wdr_runtime->get_text( ) ).` TO ls_method_source-source.
  APPEND `      ENDTRY.` TO ls_method_source-source.
  APPEND `      CHECK: lo_action IS NOT INITIAL.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `      CLEAR: ls_param.` TO ls_method_source-source.
  APPEND `      ls_param-name = 'MO_EVENT_DATA'.` TO ls_method_source-source.
  APPEND `      ls_param-object = mo_event_data.` TO ls_method_source-source.
  APPEND `      ls_param-type = cl_abap_typedescr=>typekind_oref.` TO ls_method_source-source.
  APPEND `      APPEND ls_param TO lt_param.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `      lt_key = mo_event_data->get_keys( ).` TO ls_method_source-source.
  APPEND `      LOOP AT lt_key INTO lv_key.` TO ls_method_source-source.
  APPEND `        mo_event_data->get_value(` TO ls_method_source-source.
  APPEND `          EXPORTING` TO ls_method_source-source.
  APPEND `            iv_key   = lv_key` TO ls_method_source-source.
  APPEND `          IMPORTING` TO ls_method_source-source.
  APPEND `            er_value = lr_value` TO ls_method_source-source.
  APPEND `        ).` TO ls_method_source-source.
  APPEND `        CLEAR: ls_param.` TO ls_method_source-source.
  APPEND `        ls_param-name = lv_key.` TO ls_method_source-source.
  APPEND `        ls_param-dref = lr_value.` TO ls_method_source-source.
  APPEND `        ls_param-type = cl_abap_typedescr=>typekind_dref.` TO ls_method_source-source.
  APPEND `        APPEND ls_param TO lt_param.` TO ls_method_source-source.
  APPEND `      ENDLOOP.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `      lo_action->set_parameters( lt_param ).` TO ls_method_source-source.
  APPEND `      lo_action->fire( ).` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `    ENDIF.` TO ls_method_source-source.
  APPEND `  ENDMETHOD.` TO ls_method_source-source.
  APPEND ls_method_source TO lt_method_source.

  CLEAR: ls_method.
  ls_method-clsname = ls_assist-clsname.
  ls_method-cmpname = 'ON_CLOSE'.
  ls_method-exposure = 2.
  ls_method-state = 1.
  ls_method-mtdtype = 1.
  ls_method-refclsname = 'IF_WD_WINDOW'.
  ls_method-refcmpname = 'WINDOW_CLOSED'.
  APPEND ls_method TO lt_method.
  CLEAR: ls_method_source.
  ls_method_source-cpdname = 'ON_CLOSE'.
  APPEND `  METHOD on_close.` TO ls_method_source-source.
  APPEND `    mo_comp_usage->delete_component( ).` TO ls_method_source-source.
  APPEND `  ENDMETHOD.` TO ls_method_source-source.
  APPEND ls_method_source TO lt_method_source.

  CLEAR: ls_method.
  ls_method-clsname = ls_assist-clsname.
  ls_method-cmpname = 'ON_OK'.
  ls_method-exposure = 2.
  ls_method-state = 1.
  APPEND ls_method TO lt_method.
  CLEAR: ls_param.
  ls_param-clsname = ls_assist-clsname.
  ls_param-cmpname = 'ON_OK'.
  ls_param-sconame = 'IV_VALUE'.
  ls_param-cmptype = 1.
  ls_param-parpasstyp = 1.
  ls_param-typtype = 1.
  ls_param-paroptionl = abap_true.
  ls_param-type = 'STRING'.
  APPEND ls_param TO lt_param.
  CLEAR: ls_method_source.
  ls_method_source-cpdname = 'ON_OK'.
  APPEND `  METHOD on_ok.` TO ls_method_source-source.
  APPEND `    DATA: lt_callstack   TYPE abap_callstack,` TO ls_method_source-source.
  APPEND `          ls_callstack   TYPE abap_callstack_line,` TO ls_method_source-source.
  APPEND `          lo_class_desc  TYPE REF TO cl_abap_classdescr,` TO ls_method_source-source.
  APPEND `          ls_method_desc TYPE abap_methdescr,` TO ls_method_source-source.
  APPEND `          ls_param_desc  TYPE abap_parmdescr.` TO ls_method_source-source.
  APPEND `    FIELD-SYMBOLS: <lv_value> TYPE any.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `    CALL FUNCTION 'SYSTEM_CALLSTACK'` TO ls_method_source-source.
  APPEND `      EXPORTING` TO ls_method_source-source.
  APPEND `        max_level = 1` TO ls_method_source-source.
  APPEND `      IMPORTING` TO ls_method_source-source.
  APPEND `        callstack = lt_callstack.` TO ls_method_source-source.
  APPEND `    READ TABLE lt_callstack INTO ls_callstack INDEX 1.` TO ls_method_source-source.
  APPEND `    lo_class_desc ?= cl_abap_classdescr=>describe_by_name( cl_oo_classname_service=>get_clsname_by_include( ls_callstack-include ) ).` TO ls_method_source-source.
  APPEND `    READ TABLE lo_class_desc->methods INTO ls_method_desc WITH KEY name = ls_callstack-blockname.` TO ls_method_source-source.
  APPEND `    LOOP AT ls_method_desc-parameters INTO ls_param_desc WHERE parm_kind = cl_abap_classdescr=>importing.` TO ls_method_source-source.
  APPEND `      ASSIGN (ls_param_desc-name) TO <lv_value>.` TO ls_method_source-source.
  APPEND `      mo_event_data->set_value(` TO ls_method_source-source.
  APPEND `        EXPORTING` TO ls_method_source-source.
  APPEND `          iv_key   = CONV #( ls_param_desc-name )` TO ls_method_source-source.
  APPEND `          iv_value = <lv_value>` TO ls_method_source-source.
  APPEND `      ).` TO ls_method_source-source.
  APPEND `    ENDLOOP.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `    do_callback( ).` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `  ENDMETHOD.` TO ls_method_source-source.
  APPEND ls_method_source TO lt_method_source.

  CLEAR: ls_method.
  ls_method-clsname = ls_assist-clsname.
  ls_method-cmpname = 'OPEN_POPUP'.
  ls_method-exposure = 2.
  ls_method-state = 1.
  ls_method-mtddecltyp = 1.
  APPEND ls_method TO lt_method.
  CLEAR: ls_param.
  ls_param-clsname = ls_assist-clsname.
  ls_param-cmpname = 'OPEN_POPUP'.
  ls_param-sconame = 'IO_EVENT_DATA'.
  ls_param-cmptype = 1.
  ls_param-parpasstyp = 1.
  ls_param-typtype = 3.
  ls_param-type = 'IF_FPM_PARAMETER'.
  APPEND ls_param TO lt_param.
  CLEAR: ls_method_source.
  ls_method_source-cpdname = 'OPEN_POPUP'.
  APPEND `  METHOD open_popup.` TO ls_method_source-source.
  APPEND `* Please call fpm_popup( ) or wd_popup( ).` TO ls_method_source-source.
  APPEND `    DATA: lo_comp_usage TYPE REF TO if_wd_component_usage.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `    cl_wdr_runtime_services=>get_component_usage(` TO ls_method_source-source.
  APPEND `      EXPORTING` TO ls_method_source-source.
  APPEND `        component            = wdr_task=>application->component` TO ls_method_source-source.
  APPEND `        used_component_name  = gv_wd_comp_id` TO ls_method_source-source.
  APPEND `        component_usage_name = gv_wd_comp_id` TO ls_method_source-source.
  APPEND `        create_component     = abap_true` TO ls_method_source-source.
  APPEND `        do_create            = abap_true` TO ls_method_source-source.
  APPEND `      RECEIVING` TO ls_method_source-source.
  APPEND `        component_usage      = lo_comp_usage` TO ls_method_source-source.
  APPEND `    ).` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `    go_wd_comp ?= lo_comp_usage->get_interface_controller( ).` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `    go_wd_comp->open_popup(` TO ls_method_source-source.
  APPEND `        io_event_data = io_event_data` TO ls_method_source-source.
  APPEND `        io_comp_usage = lo_comp_usage` TO ls_method_source-source.
  APPEND `    ).` TO ls_method_source-source.
  APPEND `  ENDMETHOD.` TO ls_method_source-source.
  APPEND ls_method_source TO lt_method_source.

  CLEAR: ls_method.
  ls_method-clsname = ls_assist-clsname.
  ls_method-cmpname = 'WD_POPUP'.
  ls_method-exposure = 2.
  ls_method-state = 1.
  ls_method-mtddecltyp = 1.
  APPEND ls_method TO lt_method.
  CLEAR: ls_param.
  ls_param-clsname = ls_assist-clsname.
  ls_param-cmpname = 'WD_POPUP'.
  ls_param-sconame = 'IO_VIEW'.
  ls_param-editorder = 1.
  ls_param-cmptype = 1.
  ls_param-parpasstyp = 1.
  ls_param-typtype = 3.
  ls_param-type = 'IF_WD_VIEW_CONTROLLER'.
  APPEND ls_param TO lt_param.
  CLEAR: ls_param.
  ls_param-clsname = ls_assist-clsname.
  ls_param-cmpname = 'WD_POPUP'.
  ls_param-sconame = 'IV_CALLBACK_ACTION'.
  ls_param-editorder = 2.
  ls_param-cmptype = 1.
  ls_param-parpasstyp = 1.
  ls_param-typtype = 1.
  ls_param-type = 'CLIKE'.
  APPEND ls_param TO lt_param.
  CLEAR: ls_param.
  ls_param-clsname = ls_assist-clsname.
  ls_param-cmpname = 'WD_POPUP'.
  ls_param-sconame = 'IO_EVENT_DATA'.
  ls_param-editorder = 3.
  ls_param-paroptionl = abap_true.
  ls_param-cmptype = 1.
  ls_param-parpasstyp = 1.
  ls_param-typtype = 3.
  ls_param-type = 'IF_FPM_PARAMETER'.
  APPEND ls_param TO lt_param.
  CLEAR: ls_method_source.
  ls_method_source-cpdname = 'WD_POPUP'.
  APPEND `  METHOD wd_popup.` TO ls_method_source-source.
  APPEND `    DATA: lo_event_data TYPE REF TO if_fpm_parameter.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `    IF io_event_data IS NOT INITIAL.` TO ls_method_source-source.
  APPEND `      lo_event_data = io_event_data.` TO ls_method_source-source.
  APPEND `    ELSE.` TO ls_method_source-source.
  APPEND `      CREATE OBJECT lo_event_data TYPE cl_fpm_parameter.` TO ls_method_source-source.
  APPEND `    ENDIF.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `    lo_event_data->set_value(` TO ls_method_source-source.
  APPEND `      EXPORTING` TO ls_method_source-source.
  APPEND `        iv_key   = 'IV_CALLBACK_ACTION'` TO ls_method_source-source.
  APPEND `        iv_value = iv_callback_action` TO ls_method_source-source.
  APPEND `    ).` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `    lo_event_data->set_value(` TO ls_method_source-source.
  APPEND `      EXPORTING` TO ls_method_source-source.
  APPEND `        iv_key   = 'IO_VIEW'` TO ls_method_source-source.
  APPEND `        iv_value = CAST cl_wdr_view( io_view )` TO ls_method_source-source.
  APPEND `    ).` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `    open_popup( lo_event_data ).` TO ls_method_source-source.
  APPEND `  ENDMETHOD.` TO ls_method_source-source.
  APPEND ls_method_source TO lt_method_source.

  CLEAR: ls_method.
  ls_method-clsname = ls_assist-clsname.
  ls_method-cmpname = 'FPM_POPUP'.
  ls_method-exposure = 2.
  ls_method-state = 1.
  ls_method-mtddecltyp = 1.
  APPEND ls_method TO lt_method.
  CLEAR: ls_param.
  ls_param-clsname = ls_assist-clsname.
  ls_param-cmpname = 'FPM_POPUP'.
  ls_param-sconame = 'IO_EVENT_ORIG'.
  ls_param-editorder = 1.
  ls_param-paroptionl = abap_true.
  ls_param-cmptype = 1.
  ls_param-parpasstyp = 1.
  ls_param-typtype = 3.
  ls_param-type = 'CL_FPM_EVENT'.
  APPEND ls_param TO lt_param.
  CLEAR: ls_param.
  ls_param-clsname = ls_assist-clsname.
  ls_param-cmpname = 'FPM_POPUP'.
  ls_param-sconame = 'IV_CALLBACK_EVENT_ID'.
  ls_param-editorder = 2.
  ls_param-cmptype = 1.
  ls_param-parpasstyp = 1.
  ls_param-typtype = 1.
  ls_param-type = 'CLIKE'.
  APPEND ls_param TO lt_param.
  CLEAR: ls_param.
  ls_param-clsname = ls_assist-clsname.
  ls_param-cmpname = 'FPM_POPUP'.
  ls_param-sconame = 'IO_EVENT_DATA'.
  ls_param-editorder = 3.
  ls_param-paroptionl = abap_true.
  ls_param-cmptype = 1.
  ls_param-parpasstyp = 1.
  ls_param-typtype = 3.
  ls_param-type = 'IF_FPM_PARAMETER'.
  APPEND ls_param TO lt_param.
  CLEAR: ls_method_source.
  ls_method_source-cpdname = 'FPM_POPUP'.
  APPEND `  METHOD fpm_popup.` TO ls_method_source-source.
  APPEND `    DATA: lo_event_data TYPE REF TO if_fpm_parameter.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `    IF io_event_data IS NOT INITIAL.` TO ls_method_source-source.
  APPEND `      lo_event_data = io_event_data.` TO ls_method_source-source.
  APPEND `    ELSE.` TO ls_method_source-source.
  APPEND `      CREATE OBJECT lo_event_data TYPE cl_fpm_parameter.` TO ls_method_source-source.
  APPEND `    ENDIF.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `    lo_event_data->set_value(` TO ls_method_source-source.
  APPEND `      EXPORTING` TO ls_method_source-source.
  APPEND `        iv_key   = 'IV_CALLBACK_EVENT_ID'` TO ls_method_source-source.
  APPEND `        iv_value = iv_callback_event_id` TO ls_method_source-source.
  APPEND `    ).` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `    IF io_event_orig IS NOT INITIAL.` TO ls_method_source-source.
  APPEND `      lo_event_data->set_value(` TO ls_method_source-source.
  APPEND `        EXPORTING` TO ls_method_source-source.
  APPEND `          iv_key   = 'IO_EVENT_ORIG'` TO ls_method_source-source.
  APPEND `          iv_value = io_event_orig` TO ls_method_source-source.
  APPEND `      ).` TO ls_method_source-source.
  APPEND `    ENDIF.` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `` TO ls_method_source-source.
  APPEND `    open_popup( lo_event_data ).` TO ls_method_source-source.
  APPEND `  ENDMETHOD.` TO ls_method_source-source.
  APPEND ls_method_source TO lt_method_source.

  CALL FUNCTION 'SEO_CLASS_CREATE_COMPLETE'
    EXPORTING
      corrnr                         = lv_corrnr                         " Correction Number
      devclass                       = lv_devclass                       " Package
*     version                        = seoc_version_inactive          " Active/Inactive
*     genflag                        = space                          " Generation Flag
*     authority_check                = authority_check
*     overwrite                      = overwrite
*     suppress_method_generation     = suppress_method_generation
*     suppress_refactoring_support   = suppress_refactoring_support
      method_sources                 = lt_method_source                 " Table of Methodsources
*     locals_def                     = locals_def                     " Sourcetext klassenlokaler Klassen (Definitionsteil)
*     locals_imp                     = locals_imp                     " Sourcetext klassenlokaler Klassen (Implementierungsteil)
*     locals_mac                     = locals_mac                     " ABAP-Source
*     suppress_index_update          = suppress_index_update
*     typesrc                        = typesrc                        " Usage is not recommended. See documentation
*     suppress_corr                  = suppress_corr
*     suppress_dialog                = suppress_dialog
*     lifecycle_manager              = lifecycle_manager              " Lifecycle manager
*     locals_au                      = locals_au                      " Sourcecode for local testclasses
*     lock_handle                    = lock_handle                    " Lock Handle
*     suppress_unlock                = suppress_unlock
*     suppress_commit                = suppress_commit                " No DB_COMMIT will be executed
      generate_method_impls_wo_frame = abap_true " X -> METHOD_SOURCES have to contain METHOD and ENDMETHOD statements
*    IMPORTING
*     korrnr                         = lv_corrnr                         " Request/Task
    TABLES
      class_descriptions             = lt_class_descriptions             " Short description class/interface
*     component_descriptions         = component_descriptions         " Short description class/interface component
*     subcomponent_descriptions      = subcomponent_descriptions      " Class/interface subcomponent short description
    CHANGING
      class                          = ls_class
      inheritance                    = ls_inheritance
*     redefinitions                  = redefinitions
*     implementings                  = implementings
*     impl_details                   = impl_details
      attributes                     = lt_attribute
      methods                        = lt_method
*     events                         = events
*     types                          = types
*     type_source                    = type_source                    " This parameter is deprecated. Please use typesrc.
      parameters                     = lt_param
*     exceps                         = exceps
*     aliases                        = aliases
*     typepusages                    = typepusages                    " Type group application
*     clsdeferrds                    = clsdeferrds
*     intdeferrds                    = intdeferrds
*     friendships                    = friendships
    EXCEPTIONS
      existing                       = 1
      is_interface                   = 2
      db_error                       = 3
      component_error                = 4
      no_access                      = 5
      other                          = 6
      OTHERS                         = 7.
  IF sy-subrc <> 0.
    MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
      WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
  ENDIF.


  CLEAR: ls_objects.
  ls_objects-object = 'WDYN'.
  ls_objects-obj_name = p_wdcomp.
  APPEND ls_objects TO lt_objects.
  CLEAR: ls_objects.
  ls_objects-object = 'CLAS'.
  ls_objects-obj_name = ls_assist-clsname.
  APPEND ls_objects TO lt_objects.
  CALL FUNCTION 'RS_WORKING_OBJECTS_ACTIVATE'
    EXPORTING
      with_popup             = abap_true
    TABLES
      objects                = lt_objects
    EXCEPTIONS
      excecution_error       = 1
      cancelled              = 2
      insert_into_corr_error = 3
      OTHERS                 = 4.
  IF sy-subrc <> 0.
    MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
      WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
  ENDIF.

  lv_include = cl_oo_classname_service=>get_classpool_name( ls_assist-clsname ).
  CREATE OBJECT lo_cross
    EXPORTING
      p_name    = lv_include
      p_include = lv_include.
  lo_cross->index_actualize( ).

  CALL FUNCTION 'WB_TREE_UPDATE_OBJECTLIST'
    EXPORTING
      p_object_type       = swbm_c_type_wdy_component
      p_object_name       = p_wdcomp
      p_operation         = swbm_c_op_insert
      p_package_name      = lv_devclass
      p_author            = sy-uname
    EXCEPTIONS
      error_occured       = 1
      invalid_operation   = 2
      no_objectlist_found = 3
      long_object_name    = 4
      OTHERS              = 5.
  IF sy-subrc <> 0.
    MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
      WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
  ENDIF.

ENDFORM.