class ZCL_FORM_FPM_FILE_ATTACH definition
  public
  create public .

public section.

  interfaces IF_FPM_GUIBB .
  interfaces IF_FPM_GUIBB_FORM .

  types:
    BEGIN OF ts_data,
             key1 TYPE zfpmt_file-key1,
           END OF ts_data .
  PROTECTED SECTION.
  PRIVATE SECTION.

    DATA ms_data TYPE ts_data .
ENDCLASS.



CLASS ZCL_FORM_FPM_FILE_ATTACH IMPLEMENTATION.


  METHOD if_fpm_guibb_form~check_config.
  ENDMETHOD.


  METHOD if_fpm_guibb_form~flush.
    ASSIGN is_data->* TO FIELD-SYMBOL(<ls_data>).
    ms_data = <ls_data>.
  ENDMETHOD.


  METHOD if_fpm_guibb_form~get_data.
  ENDMETHOD.


  METHOD if_fpm_guibb_form~get_default_config.
  ENDMETHOD.


  METHOD if_fpm_guibb_form~get_definition.
    DATA: ls_data              TYPE ts_data,
          ls_field_description TYPE fpmgb_s_formfield_descr,
          ls_action_definition TYPE fpmgb_s_actiondef.

    eo_field_catalog ?= cl_abap_structdescr=>describe_by_data( ls_data ).

**********************************************************************
* field description
**********************************************************************
    LOOP AT eo_field_catalog->components INTO DATA(ls_comp).
      CLEAR: ls_field_description.

      ls_field_description-name = ls_comp-name.

      CASE ls_comp-name.
        WHEN 'KEY1'.
          ls_field_description-mandatory = abap_true.
          ls_field_description-ddic_shlp_name = 'ZH_ALL_ROUND'.
      ENDCASE.

      APPEND ls_field_description TO et_field_description.
    ENDLOOP.


**********************************************************************
* action definition
**********************************************************************
    CLEAR: ls_action_definition.
    ls_action_definition-id = if_fpm_constants=>gc_event-leave_initial_screen.
    APPEND ls_action_definition TO et_action_definition.

  ENDMETHOD.


  METHOD if_fpm_guibb_form~process_event.
    DATA: lo_event_data TYPE REF TO if_fpm_parameter.

    CASE io_event->mv_event_id.
      WHEN if_fpm_constants=>gc_event-leave_initial_screen.
        lo_event_data = NEW cl_fpm_parameter( ).
        lo_event_data->set_value(
          EXPORTING
            iv_key   = 'KEY1'
            iv_value = ms_data-key1
        ).
        cl_fpm=>get_instance( )->raise_event_by_id(
          EXPORTING
            iv_event_id   = 'OPEN_ATTACH_UIBB'   " This defines the ID of the FPM Event
            io_event_data = lo_event_data " Property Bag
        ).
    ENDCASE.
  ENDMETHOD.


  METHOD if_fpm_guibb~get_parameter_list.
  ENDMETHOD.


  METHOD if_fpm_guibb~initialize.
  ENDMETHOD.
ENDCLASS.