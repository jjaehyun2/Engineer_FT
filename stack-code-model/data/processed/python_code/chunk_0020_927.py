class ZCL_GIT_ALVGRID_TEMPLATE definition
  public
  abstract
  create public .

public section.

  interfaces ZIF_GIT_REPORT_ALVGRID
      all methods abstract .

  methods CONSTRUCTOR
    importing
      !I_CONTAINER_NAME type CHAR40 default 'MY_CONTAINER'
      !I_SCREE_ALV type SY-DYNNR default '9000' .
  PROTECTED SECTION.
  PRIVATE SECTION.
ENDCLASS.



CLASS ZCL_GIT_ALVGRID_TEMPLATE IMPLEMENTATION.


  METHOD CONSTRUCTOR.

    IF  me->ZIF_GIT_REPORT_ALVGRID~m_alv_grid IS INITIAL.
      IF me->ZIF_GIT_REPORT_ALVGRID~m_alv_container IS INITIAL.
        CREATE OBJECT me->ZIF_GIT_REPORT_ALVGRID~m_alv_container
          EXPORTING
*           parent                      =     " Parent container
            container_name              = i_container_name  " Name of the Screen CustCtrl Name to Link Container To
*           style                       =     " Windows Style Attributes Applied to this Container
*           lifetime                    = LIFETIME_DEFAULT    " Lifetime
            repid                       = sy-cprog    " Screen to Which this Container is Linked
            dynnr                       = i_scree_alv    " Report To Which this Container is Linked
*           no_autodef_progid_dynnr     =     " Don't Autodefined Progid and Dynnr?
          EXCEPTIONS
            cntl_error                  = 1
            cntl_system_error           = 2
            create_error                = 3
            lifetime_error              = 4
            lifetime_dynpro_dynpro_link = 5
            OTHERS                      = 6.
        IF sy-subrc <> 0.
          MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
                     WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
        ENDIF.
      ENDIF.
      CREATE OBJECT me->ZIF_GIT_REPORT_ALVGRID~m_alv_grid
        EXPORTING
*         i_shellstyle      = 0    " Control Style
*         i_lifetime        =     " Lifetime
          i_parent          = me->ZIF_GIT_REPORT_ALVGRID~m_alv_container    " Parent Container
*         i_appl_events     = SPACE    " Register Events as Application Events
*         i_parentdbg       =     " Internal, Do not Use
*         i_applogparent    =     " Container for Application Log
*         i_graphicsparent  =     " Container for Graphics
*         i_name            =     " Name
*         i_fcat_complete   = SPACE    " Boolean Variable (X=True, Space=False)
        EXCEPTIONS
          error_cntl_create = 1
          error_cntl_init   = 2
          error_cntl_link   = 3
          error_dp_create   = 4
          OTHERS            = 5.
      IF sy-subrc <> 0.
        MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
                   WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
      ENDIF.
    ENDIF.

    "create object list for messages
    CREATE OBJECT ZIF_GIT_REPORT_ALVGRID~m_message_list.

  ENDMETHOD.
ENDCLASS.