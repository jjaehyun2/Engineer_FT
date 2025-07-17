CLASS /iwbep/cl_cos_logger DEFINITION
  PUBLIC
  FINAL
  CREATE PRIVATE .

  PUBLIC SECTION.

    TYPES:
      BEGIN OF ty_bapiret_msg_struct ,
        object_key      TYPE  /iwbep/sup_altern_id,
        type            TYPE  bapi_mtype,
        id              TYPE  symsgid,
        number          TYPE  symsgno,
        message         TYPE  bapi_msg,
        message_v1      TYPE  symsgv,
        message_v2      TYPE  symsgv,
        message_v3      TYPE  symsgv,
        message_v4      TYPE  symsgv,
        field           TYPE  bapi_fld,
        error_category  TYPE  char15,
        message_creator TYPE  /iwbep/sup_iw_agent,
      END OF ty_bapiret_msg_struct .
    TYPES:
      ty_c_ccms TYPE STANDARD TABLE OF  /iwbep/c_ccms .
    TYPES:
      ty_c_ccmst TYPE SORTED TABLE OF /iwbep/c_ccmst WITH NON-UNIQUE KEY
          node langu .
    TYPES:
      ty_dd07v TYPE STANDARD TABLE OF dd07v .

    CONSTANTS addinfo TYPE balprobcl VALUE 4.               "#EC NOTEXT
    CONSTANTS bep2gw TYPE /iwbep/sup_req_dir VALUE 'BEP to Gateway'. "#EC NOTEXT
    CONSTANTS cancel TYPE c VALUE 'A'.                      "#EC NOTEXT
    CONSTANTS context TYPE baltabname VALUE '/IWBEP/S_LOGGER_CONTEXT'. "#EC NOTEXT
    CONSTANTS context_header TYPE baltabname VALUE '/IWBEP/S_LOGGER_CONTEXT_HEAD'. "#EC NOTEXT
    CONSTANTS error TYPE c VALUE 'E'.                       "#EC NOTEXT
    CLASS-DATA go_logger TYPE REF TO /iwbep/cl_cos_logger .
    DATA gs_context_header TYPE /iwbep/s_logger_context_head .
    CLASS-DATA gt_c_ccms TYPE ty_c_ccms .
    CLASS-DATA gt_c_ccmst TYPE ty_c_ccmst .
    DATA gv_log_header TYPE bal_s_log .
    CONSTANTS gw2bep TYPE /iwbep/sup_req_dir VALUE 'Gateway to BEP'. "#EC NOTEXT
    CONSTANTS gwconn TYPE almtcreate-cusgroupmt VALUE 'Groupware Connectivity'. "#EC NOTEXT
    CONSTANTS il TYPE almtcreate-cusgroupmt VALUE 'Interface Layer'. "#EC NOTEXT
    CONSTANTS important TYPE balprobcl VALUE 2.             "#EC NOTEXT
    CONSTANTS info TYPE c VALUE 'I'.                        "#EC NOTEXT
    CONSTANTS iwapps TYPE almtcreate-cusgroupmt VALUE 'IW Applications'. "#EC NOTEXT
    CONSTANTS iwgc TYPE almtcreate-cusgroupmt VALUE 'IW General Components'. "#EC NOTEXT
    CONSTANTS iw_agent TYPE /iwbep/sup_ccms_level VALUE 02. "#EC NOTEXT
    CONSTANTS iw_context TYPE /iwbep/sup_ccms_level VALUE 00. "#EC NOTEXT
    CONSTANTS iw_layer TYPE /iwbep/sup_ccms_level VALUE 01. "#EC NOTEXT
    CONSTANTS mc_logger TYPE symsgid VALUE '/IWBEP/CM_LOGGING'. "#EC NOTEXT
    CONSTANTS medium TYPE balprobcl VALUE 3.                "#EC NOTEXT
    CONSTANTS object TYPE balobj_d VALUE '/IWBEP/'.         "#EC NOTEXT
    CONSTANTS reporting TYPE almtcreate-cusgroupmt VALUE 'Reporting'. "#EC NOTEXT
    CLASS-DATA requestguid TYPE string .
    CONSTANTS services TYPE almtcreate-cusgroupmt VALUE 'Sample Services'. "#EC NOTEXT
    CONSTANTS subobject TYPE balsubobj VALUE 'RUNTIM'.      "#EC NOTEXT
    CONSTANTS success TYPE c VALUE 'S'.                     "#EC NOTEXT
    CONSTANTS vimportant TYPE balprobcl VALUE 1.            "#EC NOTEXT
    CONSTANTS warning TYPE c VALUE 'W'.                     "#EC NOTEXT
    CONSTANTS cons TYPE /iwbep/sup_req_dir VALUE 'Consumer'. "#EC NOTEXT
    CONSTANTS security TYPE c VALUE 'S'.                    "#EC NOTEXT

    CLASS-METHODS get_logger
      RETURNING
        VALUE(ro_logger) TYPE REF TO /iwbep/cl_cos_logger .
    CLASS-METHODS init_logger
      IMPORTING
        !iv_userid            TYPE uname
        !iv_requestguid       TYPE string OPTIONAL
        !iv_object            TYPE balobj_d OPTIONAL
        !iv_subobject         TYPE balsubobj OPTIONAL
        !iv_request_direction TYPE /iwbep/sup_req_dir OPTIONAL
        !iv_operation         TYPE char10 OPTIONAL
      RETURNING
        VALUE(ro_logger)      TYPE REF TO /iwbep/cl_cos_logger .
    TYPE-POOLS abap .
    METHODS check_agent_exist
      IMPORTING
        !iv_agent             TYPE /iwbep/sup_iw_agent
      EXPORTING
        !ev_agent_description TYPE /iwbep/sup_description
        !ev_agent_exists      TYPE abap_bool .
    METHODS close_logger .
    METHODS display_log_pop_up
      IMPORTING
        !it_message_filter TYPE bal_r_idno .
    METHODS error_log_write
      IMPORTING
        !iv_main_entry TYPE xsdboolean DEFAULT abap_true
        !io_exception  TYPE REF TO cx_root OPTIONAL
        !iv_error_info TYPE any OPTIONAL
        !iv_msgid      TYPE symsgid OPTIONAL
        !iv_msgno      TYPE symsgno OPTIONAL
        !iv_msgv1      TYPE csequence OPTIONAL
        !iv_msgv2      TYPE csequence OPTIONAL
        !iv_msgv3      TYPE csequence OPTIONAL
        !iv_msgv4      TYPE csequence OPTIONAL .
    METHODS finish_business_process .
    METHODS init_business_process .
    METHODS log_bapi_return
      IMPORTING
        !is_object_key    TYPE /iwbep/sup_altern_id OPTIONAL
        !it_bapi_messages TYPE bapiret2_t
        !iv_agent         TYPE /iwbep/sup_iw_agent
        !iv_is_external   TYPE boolean OPTIONAL .
    METHODS log_free_text_message
      IMPORTING
        !iv_msg_text         TYPE /iwbep/sup_msg_longtext
        !is_msg              TYPE bal_s_msg
      RETURNING
        VALUE(rv_msg_handle) TYPE balmsghndl .
    METHODS log_message
      IMPORTING
        !iv_msg_type         TYPE symsgty
        !iv_msg_id           TYPE symsgid OPTIONAL
        !iv_msg_number       TYPE symsgno OPTIONAL
        !iv_msg_text         TYPE /iwbep/sup_msg_longtext OPTIONAL
        !iv_msg_v1           TYPE any OPTIONAL
        !iv_msg_v2           TYPE any OPTIONAL
        !iv_msg_v3           TYPE any OPTIONAL
        !iv_msg_v4           TYPE any OPTIONAL
        !iv_system_alias     TYPE /iwbep/defi_system_alias OPTIONAL
        !is_object_key       TYPE /iwbep/sup_altern_id OPTIONAL
        !iv_agent            TYPE /iwbep/sup_iw_agent
        !iv_problem_class    TYPE bal_s_msg-probclass OPTIONAL
        !iv_msg_handle       TYPE balmsghndl OPTIONAL
        !iv_log_to_ccms      TYPE /iwbep/sup_log_ccms OPTIONAL
        !iv_log_msg_text     TYPE boolean OPTIONAL
      RETURNING
        VALUE(rv_msg_handle) TYPE balmsghndl .
    METHODS log_message_container
      IMPORTING
        !is_message_structure TYPE /iwbep/s_message_container
        !iv_log_msg_text      TYPE boolean DEFAULT abap_false
        !iv_msg_handle        TYPE balmsghndl OPTIONAL
      RETURNING
        VALUE(rv_msg_handle)  TYPE balmsghndl .
    METHODS log_monitoring_information
      IMPORTING
        !iv_msg_type     TYPE symsgty
        !iv_msg_id       TYPE symsgid
        !iv_msg_number   TYPE symsgno
        !iv_msg_v1       TYPE any OPTIONAL
        !iv_msg_v2       TYPE any OPTIONAL
        !iv_msg_v3       TYPE any OPTIONAL
        !iv_msg_v4       TYPE any OPTIONAL
        !iv_system_alias TYPE char16 OPTIONAL
        !is_object_key   TYPE /iwbep/sup_altern_id OPTIONAL
        !iv_agent        TYPE /iwbep/sup_iw_agent .
    METHODS log_security_message
      IMPORTING
        !iv_msg_text         TYPE string
        !iv_ext_key          TYPE string
        !iv_msg_handle       TYPE balmsghndl OPTIONAL
      RETURNING
        VALUE(rv_msg_handle) TYPE balmsghndl .
    METHODS log_step_completion
      IMPORTING
        !iv_msg_type      TYPE symsgty
        !iv_msg_id        TYPE symsgid
        !iv_msg_number    TYPE symsgno
        !iv_msg_v1        TYPE any OPTIONAL
        !iv_msg_v2        TYPE any OPTIONAL
        !iv_msg_v3        TYPE any OPTIONAL
        !iv_msg_v4        TYPE any OPTIONAL
        !iv_system_alias  TYPE /iwbep/defi_system_alias OPTIONAL
        !is_object_key    TYPE /iwbep/sup_altern_id OPTIONAL
        !iv_agent         TYPE /iwbep/sup_iw_agent
        !iv_problem_class TYPE bal_s_msg-probclass OPTIONAL
        !iv_msg_handle    TYPE balmsghndl OPTIONAL
        !iv_log_to_ccms   TYPE /iwbep/sup_log_ccms OPTIONAL .
    METHODS log_step_completion_exception
      IMPORTING
        !io_exception          TYPE REF TO /iwbep/cx_mgw_base_exception OPTIONAL
        !io_exception_extern   TYPE REF TO cx_root OPTIONAL
        !iv_msg_id             TYPE symsgid OPTIONAL
        !iv_msg_number         TYPE symsgno OPTIONAL
        !iv_msg_v1             TYPE any OPTIONAL
        !iv_msg_v2             TYPE any OPTIONAL
        !iv_msg_v3             TYPE any OPTIONAL
        !iv_msg_v4             TYPE any OPTIONAL
        !iv_system_alias       TYPE /iwbep/defi_system_alias OPTIONAL
        !is_object_key         TYPE /iwbep/sup_altern_id OPTIONAL
        !iv_agent              TYPE /iwbep/sup_iw_agent
        !iv_msg_handle         TYPE balmsghndl OPTIONAL
        !iv_log_to_ccms        TYPE /iwbep/sup_log_ccms OPTIONAL
        !iv_is_logger_internal TYPE xsdboolean DEFAULT abap_false .
    METHODS log_step_init
      IMPORTING
        !iv_msg_number       TYPE symsgno
        !iv_msg_id           TYPE symsgid
        !iv_msg_v1           TYPE any OPTIONAL
        !iv_msg_v2           TYPE any OPTIONAL
        !iv_msg_v3           TYPE any OPTIONAL
        !iv_msg_v4           TYPE any OPTIONAL
        !iv_system_alias     TYPE /iwbep/defi_system_alias OPTIONAL
        !is_object_key       TYPE /iwbep/sup_altern_id OPTIONAL
        !iv_agent            TYPE /iwbep/sup_iw_agent
      RETURNING
        VALUE(rv_msg_handle) TYPE balmsghndl .
    METHODS save_log .
    METHODS set_header_direction
      IMPORTING
        !iv_request_direction TYPE /iwbep/sup_req_dir .
    METHODS set_header_operation
      IMPORTING
        !iv_operation TYPE char10 .
ENDCLASS.
CLASS /iwbep/cl_cos_logger IMPLEMENTATION.
  METHOD check_agent_exist.
  ENDMETHOD.
  METHOD close_logger.
  ENDMETHOD.
  METHOD display_log_pop_up.
  ENDMETHOD.
  METHOD finish_business_process.
  ENDMETHOD.
  METHOD get_logger.
  ENDMETHOD.
  METHOD init_business_process.
  ENDMETHOD.
  METHOD init_logger.
  ENDMETHOD.
  METHOD log_bapi_return.
  ENDMETHOD.
  METHOD log_free_text_message.
  ENDMETHOD.
  METHOD log_message.
  ENDMETHOD.
  METHOD log_monitoring_information.
  ENDMETHOD.
  METHOD log_security_message.
  ENDMETHOD.
  METHOD log_step_completion.
  ENDMETHOD.
  METHOD log_step_completion_exception.
  ENDMETHOD.
  METHOD log_step_init.
  ENDMETHOD.
  METHOD set_header_direction.
  ENDMETHOD.
  METHOD set_header_operation.
  ENDMETHOD.
  METHOD log_message_container.
  ENDMETHOD.
  METHOD save_log.
  ENDMETHOD.
  METHOD error_log_write.
  ENDMETHOD.
ENDCLASS.