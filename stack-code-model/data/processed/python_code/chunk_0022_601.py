class ZAVE_CL_FEED_DETAILS_STUD definition
  public
  final
  create public .

public section.

  interfaces IF_FPM_GUIBB .
  interfaces IF_FPM_GUIBB_FORM .
  PROTECTED SECTION.
  PRIVATE SECTION.
ENDCLASS.



CLASS ZAVE_CL_FEED_DETAILS_STUD IMPLEMENTATION.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_DETAILS_STUD->IF_FPM_GUIBB_FORM~CHECK_CONFIG
* +-------------------------------------------------------------------------------------------------+
* | [--->] IO_LAYOUT_CONFIG               TYPE REF TO IF_FPM_GUIBB_FORM_CONFIG
* | [--->] IO_LAYOUT_CONFIG_GL2           TYPE REF TO IF_FPM_GUIBB_FORM_CFG_GL2(optional)
* | [<---] ET_MESSAGES                    TYPE        FPMGB_T_MESSAGES
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb_form~check_config.
    RETURN.
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_DETAILS_STUD->IF_FPM_GUIBB_FORM~FLUSH
* +-------------------------------------------------------------------------------------------------+
* | [--->] IT_CHANGE_LOG                  TYPE        FPMGB_T_CHANGELOG
* | [--->] IS_DATA                        TYPE REF TO DATA
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb_form~flush.
    RETURN.
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_DETAILS_STUD->IF_FPM_GUIBB_FORM~GET_DATA
* +-------------------------------------------------------------------------------------------------+
* | [--->] IO_EVENT                       TYPE REF TO CL_FPM_EVENT
* | [--->] IV_RAISED_BY_OWN_UI            TYPE        BOOLE_D(optional)
* | [--->] IT_SELECTED_FIELDS             TYPE        FPMGB_T_SELECTED_FIELDS(optional)
* | [--->] IV_EDIT_MODE                   TYPE        FPM_EDIT_MODE(optional)
* | [--->] IO_EXTENDED_CTRL               TYPE REF TO IF_FPM_FORM_EXT_CTRL(optional)
* | [<---] ET_MESSAGES                    TYPE        FPMGB_T_MESSAGES
* | [<---] EV_DATA_CHANGED                TYPE        BOOLE_D
* | [<---] EV_FIELD_USAGE_CHANGED         TYPE        BOOLE_D
* | [<---] EV_ACTION_USAGE_CHANGED        TYPE        BOOLE_D
* | [<-->] CS_DATA                        TYPE        DATA
* | [<-->] CT_FIELD_USAGE                 TYPE        FPMGB_T_FIELDUSAGE
* | [<-->] CT_ACTION_USAGE                TYPE        FPMGB_T_ACTIONUSAGE
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb_form~get_data.
    IF io_event->mv_event_id = 'FPM_CHANGE_CONTENT_AREA'.
      DATA: lv_stud_id TYPE zave_stud_id,
            ls_student TYPE zave_s_stud.
      io_event->mo_event_data->get_value( EXPORTING iv_key = 'SELECTED_STUD'
                                          IMPORTING ev_value = lv_stud_id ).

      SELECT SINGLE * FROM zave_fpm_stud WHERE student_id = @lv_stud_id INTO @DATA(ls_student_db).

      cs_data = CORRESPONDING zave_s_stud( ls_student_db MAPPING id = student_id
                                                                 fname = firstname
                                                                 lname = lastname
                                                                 avg_mark = average_mark ).
      ev_data_changed = abap_true.
    ENDIF.

  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_DETAILS_STUD->IF_FPM_GUIBB_FORM~GET_DEFAULT_CONFIG
* +-------------------------------------------------------------------------------------------------+
* | [--->] IO_LAYOUT_CONFIG               TYPE REF TO IF_FPM_GUIBB_FORM_CONFIG
* | [--->] IO_LAYOUT_CONFIG_GL2           TYPE REF TO IF_FPM_GUIBB_FORM_CFG_GL2(optional)
* +--------------------------------------------------------------------------------------</SIGNATURE>
  method IF_FPM_GUIBB_FORM~GET_DEFAULT_CONFIG.
    RETURN.
  endmethod.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_DETAILS_STUD->IF_FPM_GUIBB_FORM~GET_DEFINITION
* +-------------------------------------------------------------------------------------------------+
* | [<---] EO_FIELD_CATALOG               TYPE REF TO CL_ABAP_STRUCTDESCR
* | [<---] ET_FIELD_DESCRIPTION           TYPE        FPMGB_T_FORMFIELD_DESCR
* | [<---] ET_ACTION_DEFINITION           TYPE        FPMGB_T_ACTIONDEF
* | [<---] ET_SPECIAL_GROUPS              TYPE        FPMGB_T_SPECIAL_GROUPS
* | [<---] ET_DND_DEFINITION              TYPE        FPMGB_T_DND_DEFINITION
* | [<---] ES_OPTIONS                     TYPE        FPMGB_S_FORM_OPTIONS
* | [<---] ES_MESSAGE                     TYPE        FPMGB_S_T100_MESSAGE
* | [<---] EV_ADDITIONAL_ERROR_INFO       TYPE        DOKU_OBJ
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb_form~get_definition.

    eo_field_catalog = CAST #( cl_abap_typedescr=>describe_by_name( 'ZAVE_S_STUD' ) ).

  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_DETAILS_STUD->IF_FPM_GUIBB_FORM~PROCESS_EVENT
* +-------------------------------------------------------------------------------------------------+
* | [--->] IO_EVENT                       TYPE REF TO CL_FPM_EVENT
* | [--->] IV_RAISED_BY_OWN_UI            TYPE        BOOLE_D(optional)
* | [<---] EV_RESULT                      TYPE        FPM_EVENT_RESULT
* | [<---] ET_MESSAGES                    TYPE        FPMGB_T_MESSAGES
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb_form~process_event.
    RETURN.
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_DETAILS_STUD->IF_FPM_GUIBB~GET_PARAMETER_LIST
* +-------------------------------------------------------------------------------------------------+
* | [<-()] RT_PARAMETER_DESCR             TYPE        FPMGB_T_PARAM_DESCR
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb~get_parameter_list.
    RETURN.
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_DETAILS_STUD->IF_FPM_GUIBB~INITIALIZE
* +-------------------------------------------------------------------------------------------------+
* | [--->] IT_PARAMETER                   TYPE        FPMGB_T_PARAM_VALUE
* | [--->] IO_APP_PARAMETER               TYPE REF TO IF_FPM_PARAMETER(optional)
* | [--->] IV_COMPONENT_NAME              TYPE        FPM_COMPONENT_NAME(optional)
* | [--->] IS_CONFIG_KEY                  TYPE        WDY_CONFIG_KEY(optional)
* | [--->] IV_INSTANCE_ID                 TYPE        FPM_INSTANCE_ID(optional)
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb~initialize.
    RETURN.
  ENDMETHOD.
ENDCLASS.