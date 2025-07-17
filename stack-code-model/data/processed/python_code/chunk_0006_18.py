class ZCL_PROXY_INPUT definition
  public
  create protected .

public section.
*"* public components of class ZCL_PROXY_INPUT
*"* do not include other source files here!!!

  interfaces IF_ECH_ACTION
      final methods FAIL
                    FINALIZE_AFTER_RETRY_ERROR
                    FINISH
                    NO_ROLLBACK_ON_RETRY_ERROR
                    RETRY .

  class-methods S_GET_INSTANCE
    importing
      !IV_ECH_COMPONENT type ECH_DTE_COMPONENT
      !IV_ECH_PROCESS type ECH_DTE_PROCESS
    returning
      value(RO_INTERFACE) type ref to ZCL_PROXY_INPUT .
  methods EXECUTE_IN
    importing
      !IS_INPUT type ANY
    raising
      CX_AI_APPLICATION_FAULT .
  methods PPO_REPEAT
    importing
      !I_ERROR_OBJECT_ID type ECH_DTE_ERROR_OBJECT_ID
      !I_DATA type ref to STRING
    exporting
      !E_EXECUTION_FAILED type XFELD
      !E_RETURN_MESSAGE type BAPIRET2 .
  methods PPO_CONFIRM
    importing
      !I_DATA type ref to STRING
      !I_ERROR_OBJECT_ID type ECH_DTE_ERROR_OBJECT_ID optional
    exporting
      !E_EXECUTION_FAILED type XFELD
      !E_RETURN_MESSAGE type BAPIRET2 .
  methods PPO_DISCARD
    importing
      !I_DATA type ref to STRING
      !I_ERROR_OBJECT_ID type ECH_DTE_ERROR_OBJECT_ID optional
      !I_MAIN_ERROR type BAPIRET2
      !I_MESSAGES type BAPIRET2_T
      !I_ERROR_CATEGORY type ECH_DTE_ERROR_CATEGORY
    exporting
      !E_EXECUTION_FAILED type XFELD
      !E_RETURN_MESSAGE type BAPIRET2 .
protected section.
*"* protected components of class ZCL_PROXY_INPUT
*"* do not include other source files here!!!

  data O_PPO_HANDLER type ref to ZCL_PROXY_INPUT .
  data O_FEH type ref to CL_FEH_REGISTRATION .
  data T_BAPIRET2 type BAPIRET2_T .
  data V_EXCEPTION_CLASS type SEOSCONAME .
  data V_RETRY type XFELD .
  data O_SERVER_CONTEXT type ref to IF_WS_SERVER_CONTEXT .
  data O_PAYLOAD_PROTOCOL type ref to IF_WSPROTOCOL_PAYLOAD .
  data REF_PRE_MAPPING_DATA type ref to DATA .
  data REF_POST_MAPPING_DATA type ref to DATA .

  methods INIT .
  methods PROCESS_APPLICATION
    raising
      CX_AI_APPLICATION_FAULT .
  methods VALIDATION_CHECK
    raising
      ZCX_PROXY_PROCESS_ERROR .
  methods INPUT_MAPPING
    importing
      !IREF_PRE_DATA type ANY
    exporting
      !EREF_POST_DATA type ANY .
  methods PROCESS_MSG_DATA
    raising
      ZCX_PROXY_PROCESS_ERROR .
  methods UPDATE_LOGS
    importing
      !IV_PROCESSING_STATUS type CHAR1 .
  methods GET_MSG_DATA
    importing
      !IV_PREMAPPING type XFELD optional
    exporting
      !ES_MSG_DATA type ANY .
  methods ADD_MESSAGE
    importing
      !IV_MSGTY type SYMSGTY
      !IV_MSGID type MSGID
      !IV_MSGNO type ANY
      !IV_MSGV1 type ANY optional
      !IV_MSGV2 type ANY optional
      !IV_MSGV3 type ANY optional
      !IV_MSGV4 type ANY optional .
  methods COLLECT_FEH_AND_RAISE_ERROR
    importing
      !IV_ERROR_CAT type ECH_DTE_ERROR_CATEGORY
      !IV_OBJTYPE type ECH_STR_OBJECT-OBJTYPE
      !IV_OBJKEY type ANY
      !IV_PRE_MAPPING type FEH_BOOLEAN
    raising
      CX_AI_APPLICATION_FAULT .
private section.
*"* private components of class ZCL_PROXY_INPUT
*"* do not include other source files here!!!

  class-data O_INTERFACE type ref to ZCL_PROXY_INPUT .

  methods GET_PPO_HANDLER
    importing
      !IV_ERROR_OBJECT_ID type ECH_DTE_ERROR_OBJECT_ID
    exporting
      !EV_EXECUTION_FAILED type XFELD
      !ES_RETURN_MESSAGE type BAPIRET2
      !EO_HANDLER type ref to ZCL_PROXY_INPUT .
ENDCLASS.



CLASS ZCL_PROXY_INPUT IMPLEMENTATION.


METHOD add_message.

  DATA:
   ls_bapiret2 LIKE LINE OF me->t_bapiret2.

  ls_bapiret2-type        = iv_msgty.
  ls_bapiret2-id          = iv_msgid.
  ls_bapiret2-number      = iv_msgno.
  ls_bapiret2-message_v1  = iv_msgv1.
  ls_bapiret2-message_v2  = iv_msgv2.
  ls_bapiret2-message_v3  = iv_msgv3.
  ls_bapiret2-message_v4  = iv_msgv4.
  APPEND ls_bapiret2 TO me->t_bapiret2.

ENDMETHOD.


METHOD collect_feh_and_raise_error.

  DATA:
    ls_main_object  TYPE ech_str_object,
    ls_bapiret2     LIKE LINE OF me->t_bapiret2.
  FIELD-SYMBOLS:
    <lfs_msg_data>  TYPE any.

*-------------------------------------------------------------------------
* (1) Collect the error message into FEH
*-------------------------------------------------------------------------
  ls_main_object-objcat  = '1'.           "Business Object
  ls_main_object-objtype = iv_objtype.    "Based on /SAPPO/S_OBJECT
  ls_main_object-objkey  = iv_objkey.

* Set the first message from BAPIRET as the main message.
  LOOP AT me->t_bapiret2 INTO ls_bapiret2 WHERE type = 'E' OR type = 'A'.
    EXIT.
  ENDLOOP.

  TRY.
      IF iv_pre_mapping = 'X'.
        ASSIGN me->ref_pre_mapping_data->* TO <lfs_msg_data>.
      ELSE.
        ASSIGN me->ref_post_mapping_data->* TO <lfs_msg_data>.
      ENDIF.
      me->o_feh->collect(  i_single_bo      = <lfs_msg_data>
                           i_error_category = iv_error_cat    "Based on values in /SAPPO/SERR_CAT
                           i_main_message   = ls_bapiret2
                           i_messages       = me->t_bapiret2
                           i_main_object    = ls_main_object
                           i_pre_mapping    = iv_pre_mapping ).
    CATCH cx_ai_system_fault .                          "#EC NO_HANDLER
  ENDTRY.

*-------------------------------------------------------------------------
* (2) Trigger application fault to enable ECH/FEH to be triggered
*     Only from proxy execution and not from PPO retry
*-------------------------------------------------------------------------
  IF me->v_retry IS INITIAL.
    cl_proxy_fault=>raise( exception_class_name = me->v_exception_class
                           bapireturn_tab       = me->t_bapiret2 ).
  ENDIF.

ENDMETHOD.


METHOD execute_in.

* Input data is stored as generic reference for subsequent accesses
  GET REFERENCE OF is_input INTO me->ref_pre_mapping_data.

  me->init( ).

  TRY.
      me->o_feh = cl_feh_registration=>s_initialize( ).
    CATCH cx_ai_system_fault.                           "#EC NO_HANDLER
  ENDTRY.

  me->process_application( ).

ENDMETHOD.


METHOD get_msg_data.

  FIELD-SYMBOLS:
    <lfs_msg_data> TYPE any.

  IF iv_premapping = 'X'.
    ASSIGN me->ref_pre_mapping_data->* TO <lfs_msg_data>.
  ELSE.
    ASSIGN me->ref_post_mapping_data->* TO <lfs_msg_data>.
  ENDIF.

  es_msg_data = <lfs_msg_data>.

ENDMETHOD.


METHOD get_ppo_handler.

  DATA:
    lv_order_key    TYPE /sappo/str_order_key,
    ls_order_detail TYPE /sappo/str_order_detail,
    lv_classname    TYPE string.

  CLEAR: ev_execution_failed, es_return_message, eo_handler.

  lv_order_key-order_id = iv_error_object_id.

* Retrieve the order details based on Message ID
  CALL FUNCTION '/SAPPO/MAPI_ORDER_GET_DETAIL'
    EXPORTING
      i_str_order_key    = lv_order_key
    IMPORTING
      e_str_order_detail = ls_order_detail
    EXCEPTIONS
      luw_inconsistent   = 1
      not_found          = 2
      no_authority       = 3
      OTHERS             = 4.
  IF sy-subrc <> 0.
    es_return_message-type        = sy-msgty.
    es_return_message-id          = sy-msgid.
    es_return_message-number      = sy-msgno.
    es_return_message-message_v1  = sy-msgv1.
    es_return_message-message_v2  = sy-msgv2.
    es_return_message-message_v3  = sy-msgv3.
    es_return_message-message_v4  = sy-msgv4.
  ELSE.
*   Based on PPO business process, retrieve the ECH processing class
*   and instantiate it for subsequent PPO-based processing (retry, confirm, fail)
    SELECT a~action_class UP TO 1 ROWS
           INTO lv_classname
           FROM echc_processes AS a
           JOIN echc_pp_process AS b
             ON a~component = b~component
             AND a~process  = b~process
           WHERE b~pp_component = ls_order_detail-component
             AND b~pp_process   = ls_order_detail-business_process.
    ENDSELECT.
    IF sy-subrc = 0.
      TRY .
          CREATE OBJECT eo_handler TYPE (lv_classname).
        CATCH cx_sy_create_object_error.
          es_return_message-type        = 'E'.
          es_return_message-id          = 'AD'.
          es_return_message-number      = '010'.
          es_return_message-message_v1  = 'Error creating object'.
          es_return_message-message_v2  = lv_classname.
      ENDTRY.
    ELSE.
      es_return_message-type        = 'E'.
      es_return_message-id          = 'AD'.
      es_return_message-number      = '010'.
      es_return_message-message_v1  = 'PPO configuration not found'.
      es_return_message-message_v2  = ls_order_detail-component.
      es_return_message-message_v3  = ls_order_detail-business_process.
    ENDIF.
  ENDIF.

  IF es_return_message IS NOT INITIAL.
    ev_execution_failed = 'X'.
  ENDIF.

ENDMETHOD.


METHOD if_ech_action~fail.

  me->get_ppo_handler( EXPORTING iv_error_object_id  = i_error_object_id
                       IMPORTING ev_execution_failed = e_execution_failed
                                 es_return_message   = e_return_message
                                 eo_handler          = me->o_ppo_handler ).

  IF e_execution_failed IS INITIAL.
    me->o_ppo_handler->ppo_discard( EXPORTING i_data             = i_data
                                              i_error_object_id  = i_error_object_id
                                              i_main_error       = i_main_error
                                              i_messages         = i_messages
                                              i_error_category   = i_error_category
                                    IMPORTING e_execution_failed = e_execution_failed
                                              e_return_message   = e_return_message ).
  ENDIF.

ENDMETHOD.


METHOD if_ech_action~finalize_after_retry_error.


ENDMETHOD.


METHOD if_ech_action~finish.

  me->get_ppo_handler( EXPORTING iv_error_object_id  = i_error_object_id
                       IMPORTING ev_execution_failed = e_execution_failed
                                 es_return_message   = e_return_message
                                 eo_handler          = me->o_ppo_handler ).

  IF e_execution_failed IS INITIAL.
    me->o_ppo_handler->ppo_confirm( EXPORTING i_data             = i_data
                                              i_error_object_id  = i_error_object_id
                                    IMPORTING e_execution_failed = e_execution_failed
                                              e_return_message   = e_return_message ).
  ENDIF.

ENDMETHOD.


METHOD if_ech_action~no_rollback_on_retry_error.


ENDMETHOD.


METHOD if_ech_action~retry.

  me->get_ppo_handler( EXPORTING iv_error_object_id  = i_error_object_id
                       IMPORTING ev_execution_failed = e_execution_failed
                                 es_return_message   = e_return_message
                                 eo_handler          = me->o_ppo_handler ).

  IF e_execution_failed IS INITIAL.
    me->o_ppo_handler->ppo_repeat( EXPORTING i_error_object_id  = i_error_object_id
                                             i_data             = i_data
                                 	 IMPORTING e_execution_failed = e_execution_failed
                                             e_return_message   = e_return_message ).
  ENDIF.

ENDMETHOD.


METHOD if_ech_action~s_create.

* For proxy processing, O_INTERFACE already created
* For PPO processing, O_INTERFACE will be instance of ZCL_PROXY_INPUT
  IF o_interface IS NOT BOUND.
    CREATE OBJECT o_interface.
  ENDIF.
  r_action_class = o_interface.

ENDMETHOD.


METHOD init.

  DATA:
    lv_proxy_class  TYPE seoclsname,
    lv_proxy_method TYPE seocmpname.

  TRY .
      me->o_server_context    = cl_proxy_access=>get_server_context( ).
      me->o_payload_protocol ?= me->o_server_context->get_protocol( if_wsprotocol=>payload ).
      cl_proxy_access=>get_inbound_message_key( IMPORTING message_class  = lv_proxy_class
                                                          message_method = lv_proxy_method ).
    CATCH cx_ai_system_fault.                           "#EC NO_HANDLER
  ENDTRY.

* Retrieve the exception class for fault message associated to current proxy
  SELECT sconame UP TO 1 ROWS
         FROM seosubco
         INTO me->v_exception_class
         WHERE clsname = lv_proxy_class
         AND   cmpname = lv_proxy_method
         AND   cmptype = '1'    "Method
         AND   scotype = '1'.   "Exception
  ENDSELECT.

  SET UPDATE TASK LOCAL.

ENDMETHOD.


METHOD input_mapping.

* Simplest approach is no mapping involved, so direct assign pre to post
* This should be redefined at subclass if mapping between pre and post DDIC structures are required

  eref_post_data = iref_pre_data.

ENDMETHOD.


METHOD PPO_CONFIRM.

  cl_feh_registration=>s_finish( EXPORTING i_data             = i_data
                                 IMPORTING e_execution_failed = e_execution_failed
                                           e_return_message   = e_return_message ).

ENDMETHOD.


METHOD PPO_DISCARD.

  cl_feh_registration=>s_fail( EXPORTING i_data             = i_data
                               IMPORTING e_execution_failed = e_execution_failed
                                         e_return_message   = e_return_message ).

ENDMETHOD.


METHOD PPO_REPEAT.

  CLEAR: e_execution_failed, e_return_message.

  me->o_feh = cl_feh_registration=>s_retry( i_error_object_id ).

  me->o_feh->retrieve_data( EXPORTING i_data                  = i_data                        "XML data
                            IMPORTING e_pre_mapping_data_ref  = me->ref_pre_mapping_data      "DDIC data - pre mapping
                                      e_post_mapping_data_ref = me->ref_post_mapping_data ).  "DDIC data - post mapping

  me->v_retry = 'X'.

  me->process_application( ).

  me->o_feh->resolve_retry( ).

ENDMETHOD.


METHOD process_application.

  DATA:
    lo_exception TYPE REF TO zcx_proxy_process_error.

  TRY .
*     Post mapping data will be empty during initial proxy processing
*     or PPO retrying an error that occurred pre-mapping
      IF me->ref_post_mapping_data IS INITIAL.
        me->validation_check( ).

        me->input_mapping( EXPORTING iref_pre_data  = me->ref_pre_mapping_data
                           IMPORTING eref_post_data = me->ref_post_mapping_data ).
      ENDIF.

      me->process_msg_data( ).

      me->update_logs( 'S' ).

    CATCH zcx_proxy_process_error INTO lo_exception.
      me->update_logs( 'E' ).

      me->collect_feh_and_raise_error( iv_error_cat   = lo_exception->error_cat
                                       iv_objtype     = lo_exception->objtype
                                       iv_objkey      = lo_exception->objkey
                                       iv_pre_mapping = lo_exception->pre_mapping ).
  ENDTRY.

ENDMETHOD.


METHOD process_msg_data.

* Redefine this method at subclass to process the post-mapping data
* into the appropriate application object

ENDMETHOD.


METHOD s_get_instance.

  DATA:
    lv_classname TYPE string.

  IF o_interface IS NOT BOUND.
*   Dynamically determine the processing & fault class from config table
    SELECT SINGLE action_class
           FROM echc_processes
           INTO lv_classname
           WHERE component = iv_ech_component
             AND process   = iv_ech_process.

    CREATE OBJECT o_interface TYPE (lv_classname).
  ENDIF.
  ro_interface = o_interface.

ENDMETHOD.


METHOD update_logs.

* Enter custom logging here
  CASE iv_processing_status.
    WHEN 'S'.

    WHEN 'E'.

  ENDCASE.

ENDMETHOD.


METHOD validation_check.

* Enter custom validation checks here

ENDMETHOD.
ENDCLASS.