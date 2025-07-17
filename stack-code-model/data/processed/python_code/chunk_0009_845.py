class YCL_AIM_TSK_V_CHECK_ASSIGNEE definition
  public
  inheriting from /BOBF/CL_LIB_V_SUPERCLASS
  final
  create public .

public section.

  methods /BOBF/IF_FRW_VALIDATION~EXECUTE
    redefinition .
protected section.
private section.
ENDCLASS.



CLASS YCL_AIM_TSK_V_CHECK_ASSIGNEE IMPLEMENTATION.


METHOD /bobf/if_frw_validation~execute.

    DATA lt_task    TYPE yaim_tsk_t_root.
    DATA lt_member  TYPE yaim_prj_t_member.

    CLEAR: eo_message, et_failed_key.

    io_read->retrieve(
      EXPORTING
        iv_node                 = yif_aim_tsk_yaim_task_c=>sc_node-root    " Node Name
        it_key                  = it_key    " Key Table
        iv_fill_data            = abap_true    " Data element for domain BOOLE: TRUE (='X') and FALSE (=' ')
        it_requested_attributes = VALUE #( ( yif_aim_tsk_yaim_task_c=>sc_node_attribute-root-assignee ) )    " List of Names (e.g. Fieldnames)
      IMPORTING
        et_data                 = lt_task
    ).

*  get the corresponding projects in order to determine whether the assignee is one of its' members
    DATA(lo_sm_task) = /bobf/cl_tra_serv_mgr_factory=>get_service_manager( yif_aim_tsk_yaim_task_c=>sc_bo_key ).
    lo_sm_task->retrieve_by_association(
      EXPORTING
        iv_node_key             = yif_aim_tsk_yaim_task_c=>sc_node-root    " Node Name
        it_key                  = it_key    " Key Table
        iv_association          = yif_aim_tsk_yaim_task_c=>sc_association-root-project    " Name of Association
        iv_fill_data            = abap_false    " Data Element for Domain BOOLE: TRUE (="X") and FALSE (=" ")
      IMPORTING
        et_key_link             = DATA(lt_link_task_project)    " Key Link
        et_target_key           = DATA(lt_project_key)    " Key Table
    ).

    DATA(lo_sm_project) = /bobf/cl_tra_serv_mgr_factory=>get_service_manager( yif_aim_prj_yaim_project_c=>sc_bo_key ).
    lo_sm_project->retrieve_by_association(
      EXPORTING
        iv_node_key             = yif_aim_prj_yaim_project_c=>sc_node-root    " Node
        it_key                  = lt_project_key
        iv_association          = yif_aim_prj_yaim_project_c=>sc_association-root-member    " Association
        iv_fill_data            = abap_true    " Data element for domain BOOLE: TRUE (='X') and FALSE (=' ')
        it_requested_attributes = VALUE #( ( yif_aim_prj_yaim_project_c=>sc_node_attribute-member-username ) )    " List of Names (e.g. Fieldnames)
      IMPORTING
        et_data                 = lt_member
    ).

    LOOP AT lt_task REFERENCE INTO DATA(lr_task).
      DATA(lv_member_found) = abap_false.
      READ TABLE lt_link_task_project INTO DATA(ls_link_task_project) WITH KEY source_key = lr_task->key.
      IF sy-subrc = 0.
        READ TABLE lt_member TRANSPORTING NO FIELDS WITH KEY
          parent_key = ls_link_task_project-target_key
          username   = lr_task->assignee.
        lv_member_found = boolc( sy-subrc = 0 ).
      ENDIF.

      IF lv_member_found = abap_false.
        INSERT VALUE #( key = lr_task->key ) INTO TABLE et_failed_key.

*      create a message
        IF eo_message IS INITIAL.
          eo_message = /bobf/cl_frw_factory=>get_message( ).
        ENDIF.

        eo_message->add_cm(
            io_message = NEW ycm_aim_task(
            severity                = /bobf/cm_frw=>co_severity_error
            lifetime                = /bobf/cm_frw=>co_lifetime_transition
            textid                  = ycm_aim_task=>invalid_assignee
            mv_assignee             = lr_task->assignee
            mv_project_abbreviation = lr_task->project_abbreviation
            ms_origin_location      = VALUE #(
                                          bo_key      = is_ctx-bo_key
                                          node_key    = is_ctx-node_key
                                          key         = lr_task->key
                                          attributes  = VALUE #( ( yif_aim_tsk_yaim_task_c=>sc_node_attribute-root-assignee ) )
                                      )
            )
        ).

      ENDIF.
    ENDLOOP.

  ENDMETHOD.
ENDCLASS.