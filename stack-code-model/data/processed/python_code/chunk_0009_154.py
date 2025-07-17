"! <p class="shorttext synchronized" lang="zh">Action: 创建传输请求(ABSTRACT)</p>
class ZCL_PT_A_TASK_CREATE_TR definition
  public
  inheriting from /BOBF/CL_LIB_A_SUPERCL_SIMPLE
  abstract
  create public .

public section.

  methods /BOBF/IF_FRW_ACTION~EXECUTE
    redefinition .
protected section.

  methods GET_TR_TYPE
  abstract
    returning
      value(TYPE) type TRFUNCTION .
  methods READ_PROJECT
    importing
      !CODE type ZE_PT_PROJECT_NO
    returning
      value(PROJECT) type ZPT_T_PROJECT .
private section.

  data CONTEXT type /BOBF/S_FRW_CTX_ACT .
  data READ type ref to /BOBF/IF_FRW_READ .
  data MODIFY type ref to /BOBF/IF_FRW_MODIFY .

  methods CREATE_REQUEST
    importing
      !TYPE type TRFUNCTION
      !TASK type ZSPTI_TASK
    returning
      value(NEW_REQUEST) type TRKORR
    raising
      ZCX_TT_MANAGEMENT .
  methods CREATE_BO
    importing
      !NEW_REQUEST type TRKORR
      !TASK type ZSPTI_TASK
      !ERROR_AFTER_CREATION type ABAP_BOOL default ABAP_FALSE
    returning
      value(CREATED_REQUEST) type ZTPTI_TASK_TRAN_REQ .
ENDCLASS.



CLASS ZCL_PT_A_TASK_CREATE_TR IMPLEMENTATION.


  METHOD /BOBF/IF_FRW_ACTION~EXECUTE.

    DATA: tasks TYPE ZTPTI_TASK.

    context = is_ctx.
    read    = io_read.
    modify  = io_modify.

    io_read->retrieve( EXPORTING iv_node = is_ctx-node_key
                                 it_key  = it_key
                       IMPORTING et_data = tasks ).

    LOOP AT tasks INTO DATA(task).

      DATA(error_after_creation) = abap_false.

      TRY.
          DATA(new_request) = create_request( type  = get_tr_type( )
                                              task = task ).
        CATCH zcx_pt_after_req_creation INTO DATA(lx_after_req_creation).
          zcx_pt_management=>collect_bo_message( EXPORTING textid       = lx_after_req_creation->if_t100_message~t100key
                                                           text1        = lx_after_req_creation->text1
                                                           text2        = lx_after_req_creation->text2
                                                           text3        = lx_after_req_creation->text3
                                                           text4        = lx_after_req_creation->text4
                                                           message_type = 'W'
                                                           node         = is_ctx-node_key
                                                           key          = task-key
                                                 CHANGING  bo_messages  = eo_message ).
          error_after_creation = abap_true.
        CATCH zcx_pt_management INTO DATA(lx_management).
          zcx_pt_management=>collect_bo_message( EXPORTING textid      = lx_management->if_t100_message~t100key
                                                           text1       = lx_management->text1
                                                           text2       = lx_management->text2
                                                           text3       = lx_management->text3
                                                           text4       = lx_management->text4
                                                           node        = is_ctx-node_key
                                                           key         = task-key
                                                 CHANGING  bo_messages = eo_message ).

          INSERT VALUE #( key = task-key ) INTO TABLE et_failed_key.
          CONTINUE.
      ENDTRY.

      create_bo( new_request = new_request task = task error_after_creation = error_after_creation ).

    ENDLOOP.


  ENDMETHOD.


  METHOD create_bo.

    DATA(copy_request) = VALUE zspti_task_tran_req( transport_request = new_request ).

    modify->create( EXPORTING iv_node            = zif_pt_i_task_c=>sc_node-zpt_i_task_tran_req
                              iv_assoc_key       = zif_pt_i_task_c=>sc_association-zpt_i_task-_transportrequests
                              iv_source_node_key = zif_pt_i_task_c=>sc_node-zpt_i_task
                              iv_source_key      = task-key
                              is_data            = REF #( copy_request )
                    IMPORTING ev_key             = DATA(lv_key) ).

    IF lv_key IS NOT INITIAL.
      read->retrieve( EXPORTING iv_node         = zif_pt_i_task_c=>sc_node-zpt_i_task_tran_req
                                it_key          = VALUE #( ( key = lv_key ) )
                                iv_before_image = abap_true
                      IMPORTING et_data         = created_request ).
    ENDIF.

  ENDMETHOD.


  METHOD CREATE_REQUEST.

    DATA: users              TYPE scts_users,
          attributes         TYPE scts_attrs,
          new_request_header TYPE trwbo_request_header.

    DATA(project) = read_project( task-project_no ).

    DATA(request_copy_text) = CONV as4text( task-description ).

    IF task-functional_resp IS NOT INITIAL.
      INSERT VALUE #( user = task-functional_resp type = 'X' ) INTO TABLE users.
    ENDIF.

    IF task-technical_resp IS NOT INITIAL.
      INSERT VALUE #( user = task-technical_resp  type = 'X' ) INTO TABLE users.
    ENDIF.

    attributes = COND #( WHEN project-cts_project IS NOT INITIAL
                             THEN VALUE #( ( attribute = 'SAP_CTS_PROJECT' value = project-cts_project ) ) ).

    CALL FUNCTION 'TR_INSERT_REQUEST_WITH_TASKS'
      EXPORTING
        iv_type            = type
        iv_text            = request_copy_text
        iv_target          = project-tr_target
        it_attributes      = attributes
        it_users           = users
        iv_with_badi_check = abap_true
      IMPORTING
        es_request_header  = new_request_header
      EXCEPTIONS
        insert_failed      = 1
        enqueue_failed     = 2
        OTHERS             = 3.
    IF sy-subrc <> 0.
      zcx_pt_management=>raise_syst( ).
    ENDIF.

    new_request = new_request_header-trkorr.

  ENDMETHOD.


  METHOD READ_PROJECT.

    SELECT SINGLE *
      INTO @project
      FROM zpt_t_project
      WHERE project_no = @code.

  ENDMETHOD.
ENDCLASS.