class ZAVE_CL_FEED_LIST_STUD definition
  public
  final
  create public .

public section.

  interfaces IF_FPM_GUIBB .
  interfaces IF_FPM_GUIBB_LIST .

  methods CONSTRUCTOR .
  methods CHECK_EVENT_AND_NAVIGATE
    importing
      !IO_EVENT type ref to CL_FPM_EVENT
      !IT_STUDENTS type ZAVE_T_STUD
      !INDEX type SYTABIX .
  PROTECTED SECTION.
private section.

  data MO_STUDENT_REP type ref to ZIF_ZAVE_STUDENT_REP .
ENDCLASS.



CLASS ZAVE_CL_FEED_LIST_STUD IMPLEMENTATION.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_LIST_STUD->CHECK_EVENT_AND_NAVIGATE
* +-------------------------------------------------------------------------------------------------+
* | [--->] IO_EVENT                       TYPE REF TO CL_FPM_EVENT
* | [--->] IT_STUDENTS                    TYPE        ZAVE_T_STUD
* | [--->] INDEX                          TYPE        SYTABIX
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD CHECK_EVENT_AND_NAVIGATE.
    IF io_event->mv_event_id = 'FPM_GUIBB_LIST_ON_LEAD_SELECTI'.
      DATA: ls_stud  TYPE zave_s_stud,
            lo_event TYPE REF TO cl_fpm_event.

      ls_stud = it_students[ index ].

      lo_event = cl_fpm_event=>create_by_id( 'FPM_CHANGE_CONTENT_AREA' ).
      lo_event->mo_event_data->set_value( iv_key = 'TARGET_CONTENT_AREA'
                                          iv_value = 'PAGE_2' ).
      lo_event->mo_event_data->set_value( iv_key = 'SELECTED_STUD'
                                          iv_value = ls_stud-id ).

      cl_fpm=>get_instance( )->raise_event( lo_event ).
    ENDIF.
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_LIST_STUD->CONSTRUCTOR
* +-------------------------------------------------------------------------------------------------+
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD constructor.
    zave_fpm_cl_repository_init=>init_repository_factory( ).
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_LIST_STUD->IF_FPM_GUIBB_LIST~CHECK_CONFIG
* +-------------------------------------------------------------------------------------------------+
* | [--->] IO_LAYOUT_CONFIG               TYPE REF TO IF_FPM_GUIBB_LIST_CONFIG
* | [<---] ET_MESSAGES                    TYPE        FPMGB_T_MESSAGES
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb_list~check_config.
    RETURN.
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_LIST_STUD->IF_FPM_GUIBB_LIST~FLUSH
* +-------------------------------------------------------------------------------------------------+
* | [--->] IT_CHANGE_LOG                  TYPE        FPMGB_T_CHANGELOG
* | [--->] IT_DATA                        TYPE REF TO DATA
* | [--->] IV_OLD_LEAD_SEL                TYPE        I(optional)
* | [--->] IV_NEW_LEAD_SEL                TYPE        I(optional)
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb_list~flush.
    RETURN.
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_LIST_STUD->IF_FPM_GUIBB_LIST~GET_DATA
* +-------------------------------------------------------------------------------------------------+
* | [--->] IV_EVENTID                     TYPE REF TO CL_FPM_EVENT
* | [--->] IT_SELECTED_FIELDS             TYPE        FPMGB_T_SELECTED_FIELDS(optional)
* | [--->] IV_RAISED_BY_OWN_UI            TYPE        BOOLE_D(optional)
* | [--->] IV_VISIBLE_ROWS                TYPE        I(optional)
* | [--->] IV_EDIT_MODE                   TYPE        FPM_EDIT_MODE(optional)
* | [--->] IO_EXTENDED_CTRL               TYPE REF TO IF_FPM_LIST_ATS_EXT_CTRL(optional)
* | [<---] ET_MESSAGES                    TYPE        FPMGB_T_MESSAGES
* | [<---] EV_DATA_CHANGED                TYPE        BOOLE_D
* | [<---] EV_FIELD_USAGE_CHANGED         TYPE        BOOLE_D
* | [<---] EV_ACTION_USAGE_CHANGED        TYPE        BOOLE_D
* | [<---] EV_SELECTED_LINES_CHANGED      TYPE        BOOLE_D
* | [<---] EV_DND_ATTR_CHANGED            TYPE        BOOLE_D
* | [<---] EO_ITAB_CHANGE_LOG             TYPE REF TO IF_SALV_ITAB_CHANGE_LOG
* | [<-->] CT_DATA                        TYPE        DATA
* | [<-->] CT_FIELD_USAGE                 TYPE        FPMGB_T_FIELDUSAGE
* | [<-->] CT_ACTION_USAGE                TYPE        FPMGB_T_ACTIONUSAGE
* | [<-->] CT_SELECTED_LINES              TYPE        RSTABIXTAB
* | [<-->] CV_LEAD_INDEX                  TYPE        SYTABIX
* | [<-->] CV_FIRST_VISIBLE_ROW           TYPE        I
* | [<-->] CS_ADDITIONAL_INFO             TYPE        FPMGB_S_ADDITIONAL_INFO(optional)
* | [<-->] CT_DND_ATTRIBUTES              TYPE        FPMGB_T_DND_DEFINITION(optional)
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb_list~get_data.

    DATA(lt_students) = zave_fpm_cl_repository_factory=>get_instance( )->zif_zave_student_rep~get_all_students( ).

    ct_data = VALUE zave_t_stud( FOR lo_student IN lt_students ( id        = lo_student->mo_student_p->get_id( )
                                                                 fname     = lo_student->mo_student_p->get_first_name( )
                                                                 lname     = lo_student->mo_student_p->get_last_name( )
                                                                 phone     = lo_student->mo_student_p->get_phone_number( )
                                                                 address   = lo_student->mo_student_p->get_address( )
                                                                 email     = lo_student->mo_student_p->get_email( )
                                                                 avg_mark  = lo_student->mo_student_p->get_avg_mark( ) ) ).

    check_event_and_navigate( io_event    = iv_eventid
                              it_students = ct_data
                              index       = cv_lead_index  ).

  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_LIST_STUD->IF_FPM_GUIBB_LIST~GET_DEFAULT_CONFIG
* +-------------------------------------------------------------------------------------------------+
* | [--->] IO_LAYOUT_CONFIG               TYPE REF TO IF_FPM_GUIBB_LIST_CONFIG
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb_list~get_default_config.
    RETURN.
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_LIST_STUD->IF_FPM_GUIBB_LIST~GET_DEFINITION
* +-------------------------------------------------------------------------------------------------+
* | [<---] EO_FIELD_CATALOG               TYPE REF TO CL_ABAP_TABLEDESCR
* | [<---] ET_FIELD_DESCRIPTION           TYPE        FPMGB_T_LISTFIELD_DESCR
* | [<---] ET_ACTION_DEFINITION           TYPE        FPMGB_T_ACTIONDEF
* | [<---] ET_SPECIAL_GROUPS              TYPE        FPMGB_T_SPECIAL_GROUPS
* | [<---] ES_MESSAGE                     TYPE        FPMGB_S_T100_MESSAGE
* | [<---] EV_ADDITIONAL_ERROR_INFO       TYPE        DOKU_OBJ
* | [<---] ET_DND_DEFINITION              TYPE        FPMGB_T_DND_DEFINITION
* | [<---] ET_ROW_ACTIONS                 TYPE        FPMGB_T_ROW_ACTION
* | [<---] ES_OPTIONS                     TYPE        FPMGB_S_LIST_OPTIONS
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb_list~get_definition.

      eo_field_catalog = CAST #( cl_abap_typedescr=>describe_by_name( 'ZAVE_T_STUD' ) ).

  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_LIST_STUD->IF_FPM_GUIBB_LIST~PROCESS_EVENT
* +-------------------------------------------------------------------------------------------------+
* | [--->] IO_EVENT                       TYPE REF TO CL_FPM_EVENT
* | [--->] IV_RAISED_BY_OWN_UI            TYPE        BOOLE_D(optional)
* | [--->] IV_LEAD_INDEX                  TYPE        SYTABIX
* | [--->] IV_EVENT_INDEX                 TYPE        SYTABIX
* | [--->] IT_SELECTED_LINES              TYPE        RSTABIXTAB
* | [--->] IO_UI_INFO                     TYPE REF TO IF_FPM_LIST_ATS_UI_INFO(optional)
* | [<---] EV_RESULT                      TYPE        FPM_EVENT_RESULT
* | [<---] ET_MESSAGES                    TYPE        FPMGB_T_MESSAGES
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb_list~process_event.
    RETURN.
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_LIST_STUD->IF_FPM_GUIBB~GET_PARAMETER_LIST
* +-------------------------------------------------------------------------------------------------+
* | [<-()] RT_PARAMETER_DESCR             TYPE        FPMGB_T_PARAM_DESCR
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb~get_parameter_list.
    RETURN.
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_LIST_STUD->IF_FPM_GUIBB~INITIALIZE
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