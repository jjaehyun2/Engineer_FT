*&---------------------------------------------------------------------*
*& Report  ZDEMOGIT_REPT_ALV_FACTORY3
*&
*&---------------------------------------------------------------------*
*& ALV Factory along with Class ZCL_GIT_ALVFACTGRID_TEMPLATE
*&
*&---------------------------------------------------------------------*
REPORT zdemogit_rept_alv_factory3.

*------------------------------------------------------------------------------*
* SELECTION SCREEN
*------------------------------------------------------------------------------*
SELECTION-SCREEN BEGIN OF BLOCK report WITH FRAME TITLE text-001.
PARAMETERS : p_date TYPE zzbc_log_ks-start_date DEFAULT sy-datum OBLIGATORY.
*SELECT-OPTIONS s_time FOR ztimez-uzeit DEFAULT sy-timlo.
*
*PARAMETERS: p_sddoc TYPE vbeln OBLIGATORY,
*            p_func  TYPE sycprog DEFAULT 'ZKS_SD_DOC_CHANGE' NO-DISPLAY,
*            p_uname TYPE uname DEFAULT 'RFCPO' NO-DISPLAY.
*
SELECTION-SCREEN END OF BLOCK report.

CLASS lcl_report DEFINITION FINAL CREATE PRIVATE.
  PUBLIC SECTION.
    INTERFACES zif_git_report_v2 .
    ALIASES: start_of_selection FOR zif_git_report_v2~start_of_selection,
             initialization FOR zif_git_report_v2~initialization.
    CLASS-DATA instance TYPE REF TO lcl_report.
    CLASS-METHODS: class_constructor.
ENDCLASS.

CLASS lcl_report IMPLEMENTATION.
  METHOD class_constructor.
    " do any post initialization to your global class report
    instance = NEW lcl_report( ).
  ENDMETHOD.
  METHOD initialization.
    " do any initialization to your global class report
  ENDMETHOD.

  METHOD start_of_selection.
    DATA: lo_template_cl TYPE REF TO zcl_git_alvfactgrid_template.

    TRY.
        lo_template_cl = zcl_git_alvfactgrid_template=>get_instance( iv_date = p_date ).

        lo_template_cl->run( ).
      CATCH zcx_bc_exception INTO DATA(lx_error).
        lx_error->display_popup( ).
*        cl_demo_output=>display(
*         EXPORTING
*           data = lx_error->get_longtext( )    " Text or Data
*           name = 'Error'
*       ).
    ENDTRY.
  ENDMETHOD.

  METHOD zif_git_report_v2~end_of_selection.
  ENDMETHOD.
  METHOD zif_git_report_v2~load_of_program.
    " do any initialization to your global class report at load report
  ENDMETHOD.
  METHOD zif_git_report_v2~at_selection_screen_output.
  ENDMETHOD.
  METHOD zif_git_report_v2~at_selection_screen.
  ENDMETHOD.
  METHOD zif_git_report_v2~at_selection_screen_on.
  ENDMETHOD.
  METHOD zif_git_report_v2~at_selection_screen_on_end_of.
  ENDMETHOD.
  METHOD zif_git_report_v2~atsel_scrn_on_help_request_for.
  ENDMETHOD.
  METHOD zif_git_report_v2~atsel_scr_on_value_request_for.
  ENDMETHOD.
  METHOD zif_git_report_v2~at_selection_screen_on_block.
  ENDMETHOD.
  METHOD zif_git_report_v2~atsel_scr_on_radiobutton_group.
  ENDMETHOD.
ENDCLASS.


INITIALIZATION.
  lcl_report=>instance->initialization( ).

AT SELECTION-SCREEN OUTPUT.
  lcl_report=>instance->zif_git_report_v2~at_selection_screen_output( ).

AT SELECTION-SCREEN.
  lcl_report=>instance->zif_git_report_v2~at_selection_screen( ).

LOAD-OF-PROGRAM.
  lcl_report=>instance->zif_git_report_v2~load_of_program( ).

START-OF-SELECTION.
  lcl_report=>instance->start_of_selection( ).

END-OF-SELECTION.
  lcl_report=>instance->zif_git_report_v2~end_of_selection( ).

*AT SELECTION-SCREEN ON p_test.
*  lcl_report=>instance->zif_git_report_v2~at_selection_screen_on( ).

*AT SELECTION-SCREEN ON END OF p_test.
*  lcl_report=>instance->zif_git_report_v2~at_selection_screen_on_end_of( ).

*AT SELECTION-SCREEN ON HELP-REQUEST FOR p_test.
*  lcl_report=>instance->zif_git_report_v2~atsel_scrn_on_help_request_for( ).

*AT SELECTION-SCREEN ON VALUE-REQUEST FOR  p_test.
*  lcl_report=>instance->zif_git_report_v2~atsel_scr_on_value_request_for( ).

*  AT SELECTION-SCREEN ON BLOCK
*  lcl_report=>instance->zif_git_report_v2~at_selection_screen_on_block( ).
*    AT SELECTION-SCREEN on RADIOBUTTON GROUP
*  lcl_report=>instance->zif_git_report_v2~atsel_scr_on_radiobutton_group( ).