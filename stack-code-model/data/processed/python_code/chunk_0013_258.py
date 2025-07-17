class ZAVE_CL_FEED_STUD_MARK_CHART definition
  public
  final
  create public .

public section.

  interfaces IF_FPM_GUIBB .
  interfaces IF_FPM_GUIBB_CHART .
protected section.
private section.

  data MT_STUDENTS type ZAVE_T_STUD .
ENDCLASS.



CLASS ZAVE_CL_FEED_STUD_MARK_CHART IMPLEMENTATION.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_STUD_MARK_CHART->IF_FPM_GUIBB_CHART~CHECK_CONFIG
* +-------------------------------------------------------------------------------------------------+
* | [--->] IO_LAYOUT_CONFIG               TYPE REF TO IF_FPM_GUIBB_CHART_CONFIG
* | [<---] ET_MESSAGES                    TYPE        FPMGB_T_MESSAGES
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb_chart~check_config.

  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_STUD_MARK_CHART->IF_FPM_GUIBB_CHART~FLUSH
* +-------------------------------------------------------------------------------------------------+
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb_chart~flush.

  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_STUD_MARK_CHART->IF_FPM_GUIBB_CHART~GET_DATA
* +-------------------------------------------------------------------------------------------------+
* | [--->] IO_EVENT                       TYPE REF TO CL_FPM_EVENT
* | [--->] IV_RAISED_BY_OWN_UI            TYPE        BOOLE_D(optional)
* | [--->] IO_CHART_DATA                  TYPE REF TO IF_FPM_CHART_DATA_FACTORY
* | [--->] IO_CHART_SELECTION             TYPE REF TO IF_FPM_CHART_SELECTION_FACTORY(optional)
* | [--->] IO_CHART_SETTINGS              TYPE REF TO IF_FPM_CHART_SETTINGS(optional)
* | [--->] IO_EXTENDED_CTRL               TYPE REF TO IF_FPM_CHART_EXT_CTRL(optional)
* | [<---] ET_MESSAGES                    TYPE        FPMGB_T_MESSAGES
* | [<---] EV_ACTION_USAGE_CHANGED        TYPE        BOOLE_D
* | [<-->] CT_ACTION_USAGE                TYPE        FPMGB_T_ACTIONUSAGE
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb_chart~get_data.

    DATA(lt_students) = zave_fpm_cl_repository_factory=>get_instance( )->zif_zave_student_rep~get_all_students( ).


    mt_students = VALUE zave_t_stud( FOR lo_student IN lt_students ( id        = lo_student->mo_student_p->get_id( )
                                                                     fname     = lo_student->mo_student_p->get_first_name( )
                                                                     lname     = lo_student->mo_student_p->get_last_name( )
                                                                     phone     = lo_student->mo_student_p->get_phone_number( )
                                                                     address   = lo_student->mo_student_p->get_address( )
                                                                     email     = lo_student->mo_student_p->get_email( )
                                                                     avg_mark  = lo_student->mo_student_p->get_avg_mark( ) ) ).

    io_chart_data->get_table_model( )->set_data( it_data          = mt_students
                                                 iv_check_changed = 'X').
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_STUD_MARK_CHART->IF_FPM_GUIBB_CHART~GET_DEFAULT_CONFIG
* +-------------------------------------------------------------------------------------------------+
* | [--->] IO_LAYOUT_CONFIG               TYPE REF TO IF_FPM_GUIBB_CHART_CONFIG
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb_chart~get_default_config.
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_STUD_MARK_CHART->IF_FPM_GUIBB_CHART~GET_DEFINITION
* +-------------------------------------------------------------------------------------------------+
* | [--->] IO_CHART_MODEL                 TYPE REF TO IF_FPM_CHART_MODEL_FACTORY
* | [<---] ET_ACTION_DEFINITION           TYPE        FPMGB_T_ACTIONDEF
* | [<---] ES_MESSAGE                     TYPE        FPMGB_S_T100_MESSAGE
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb_chart~get_definition.
    DATA(lo_chart_table_model) = io_chart_model->get_table_model( ).
    DATA(lo_field_catalog) =  CAST cl_abap_tabledescr( cl_abap_typedescr=>describe_by_name( 'ZAVE_T_STUD' ) ).
    lo_chart_table_model->set_definition( io_field_catalog = lo_field_catalog ).
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_STUD_MARK_CHART->IF_FPM_GUIBB_CHART~PROCESS_EVENT
* +-------------------------------------------------------------------------------------------------+
* | [--->] IO_EVENT                       TYPE REF TO CL_FPM_EVENT
* | [--->] IV_RAISED_BY_OWN_UI            TYPE        BOOLE_D
* | [<---] EV_RESULT                      TYPE        FPM_EVENT_RESULT
* | [<---] ET_MESSAGES                    TYPE        FPMGB_T_MESSAGES
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb_chart~process_event.

  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_STUD_MARK_CHART->IF_FPM_GUIBB~GET_PARAMETER_LIST
* +-------------------------------------------------------------------------------------------------+
* | [<-()] RT_PARAMETER_DESCR             TYPE        FPMGB_T_PARAM_DESCR
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb~get_parameter_list.

  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_FEED_STUD_MARK_CHART->IF_FPM_GUIBB~INITIALIZE
* +-------------------------------------------------------------------------------------------------+
* | [--->] IT_PARAMETER                   TYPE        FPMGB_T_PARAM_VALUE
* | [--->] IO_APP_PARAMETER               TYPE REF TO IF_FPM_PARAMETER(optional)
* | [--->] IV_COMPONENT_NAME              TYPE        FPM_COMPONENT_NAME(optional)
* | [--->] IS_CONFIG_KEY                  TYPE        WDY_CONFIG_KEY(optional)
* | [--->] IV_INSTANCE_ID                 TYPE        FPM_INSTANCE_ID(optional)
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD if_fpm_guibb~initialize.

  ENDMETHOD.
ENDCLASS.