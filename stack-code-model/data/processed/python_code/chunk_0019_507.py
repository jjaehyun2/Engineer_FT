class ZCL_MDG_BP_HELPER_STAGING definition
  public
  inheriting from ZCL_MDG_BP_HELPER
  final
  create private .

public section.

  class-methods DESTRUCT_INSTANCE .
  class-methods GET_INSTANCE
    returning
      value(RO_BP_DATA) type ref to ZCL_MDG_BP_HELPER
    exceptions
      INSTANCE_CREATION_FAILED
      ENTITY_DATA_ALL_READ_ERROR
      APP_CONTEXT_GET_FAILED
      APPCONTEXT_ATTRIBUTE_GET_ERROR
      UNEXPECTED_ERROR
      MODEL_GET_FAILED .
  methods PROCESS_EXT_NUMBER_ASSIGNMENT
    importing
      !IO_CHANGED_DATA type ref to IF_USMD_DELTA_BUFFER_READ .
  PROTECTED SECTION.
  PRIVATE SECTION.

    DATA gt_all_changed_detail TYPE usmd_th_change_document_change .
    DATA gt_all_changed_value TYPE usmd_ts_change_document_value .
    DATA gt_change_documents TYPE zif_mdg_datatypes=>gty_t_change_document .
    CLASS-DATA go_instance TYPE REF TO zcl_mdg_bp_helper_staging .
    DATA gv_crid TYPE usmd_crequest .
    DATA gv_wiid TYPE sww_wiid .
    CLASS-DATA gv_final_status_set TYPE abap_bool .

    METHODS constructor
      EXCEPTIONS
        entity_data_all_read_error
        app_context_get_failed
        appcontext_attribute_get_error
        model_get_failed
        discard_instance
        unexpected_error .
    METHODS get_where_condition
      IMPORTING
        !is_record TYPE any
        !iv_entity TYPE usmd_entity
      EXPORTING
        !ev_where  TYPE string .
    METHODS read_changed_documents
      EXPORTING
        !et_change_documents   TYPE zif_mdg_datatypes=>gty_t_change_document
        !et_all_changed_detail TYPE usmd_th_change_document_change
        !et_all_changed_value  TYPE usmd_ts_change_document_value .
    METHODS read_entity_data_cr
      EXCEPTIONS
        entity_data_all_read_error
        app_context_get_failed
        appcontext_attribute_get_error
        model_get_failed
        discard_instance
        data_not_found
        dyn_assignment_failed .
    METHODS read_active_data_of_cr
      IMPORTING
*        !iv_crequest        TYPE usmd_crequest
        !io_model           TYPE REF TO if_usmd_model_ext
        !it_businesspartner TYPE ANY TABLE
      EXPORTING
        !et_entity_data_act TYPE usmd_ts_data_entity .
ENDCLASS.



CLASS ZCL_MDG_BP_HELPER_STAGING IMPLEMENTATION.


  METHOD constructor.

    super->constructor( ).

    CALL METHOD read_entity_data_cr
      EXCEPTIONS
        entity_data_all_read_error     = 1
        app_context_get_failed         = 2
        appcontext_attribute_get_error = 3
        model_get_failed               = 4
        discard_instance               = 5
        OTHERS                         = 6.

    IF sy-subrc <> 0.
      CASE sy-subrc.
        WHEN 1.
          RAISE entity_data_all_read_error.
        WHEN 2.
          RAISE app_context_get_failed.
        WHEN 3.
          RAISE appcontext_attribute_get_error.
        WHEN 4.
          RAISE model_get_failed.
        WHEN 5.
          RAISE discard_instance.
        WHEN OTHERS.
          MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 000 RAISING unexpected_error.
      ENDCASE.
    ENDIF.

  ENDMETHOD.


  METHOD destruct_instance.

    FREE go_instance.

  ENDMETHOD.


  METHOD get_instance.

    DATA:
      lo_app_context   TYPE REF TO if_usmd_app_context,
      lv_force_reload  TYPE abap_bool,
      lo_crequest_util TYPE REF TO cl_usmd_crequest_util,
      lo_model         TYPE REF TO if_usmd_model,
      ls_crequest      TYPE usmd_s_crequest,
      lt_messages      TYPE usmd_t_message,
      lv_error         TYPE abap_bool,
      lv_bp            TYPE bu_partner.

    FIELD-SYMBOLS:
      <ls_message> TYPE usmd_s_message.

    lv_force_reload = abap_false.

    CALL METHOD cl_usmd_app_context=>get_context
      RECEIVING
        eo_context = lo_app_context.

    IF ( lo_app_context IS BOUND AND lo_app_context->mv_crequest_id IS INITIAL ) OR lo_app_context IS NOT BOUND.
      lv_bp = zcl_mdg_bp_helper_utilities=>get_current_bp_from_fpm_para( ).

      CALL METHOD zcl_mdg_bp_helper_active=>get_instance
        EXPORTING
          iv_bp_id                       = lv_bp
        RECEIVING
          ro_bp_data                     = ro_bp_data
        EXCEPTIONS
          instance_creation_failed       = 1
          entity_data_all_read_error     = 2
          app_context_get_failed         = 3
          appcontext_attribute_get_error = 4
          unexpected_error               = 5
          model_get_failed               = 6
          OTHERS                         = 7.


      IF sy-subrc <> 0.
        CASE sy-subrc.
          WHEN 1.
            MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_bp TYPE 'X' NUMBER 001 RAISING entity_data_all_read_error.
          WHEN 2.
            MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 004 RAISING app_context_get_failed.
          WHEN 3.
            MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 004 RAISING app_context_get_failed .
          WHEN 4.
            MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 001 RAISING model_get_failed.
          WHEN 5.
            MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 001 RAISING instance_creation_failed.
          WHEN 6.
            MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 000 RAISING unexpected_error.
          WHEN OTHERS.
            MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 000 RAISING unexpected_error.
        ENDCASE.
      ENDIF.

      RETURN.

    ELSEIF go_instance IS BOUND.
      IF lo_app_context->mv_wi_id <> go_instance->gv_wiid OR go_instance->gv_crid <> lo_app_context->mv_crequest_id.
        go_instance->gv_wiid = lo_app_context->mv_wi_id.
        go_instance->gv_crid = lo_app_context->mv_crequest_id.
        lv_force_reload = abap_true.
      ENDIF.

      IF gv_final_status_set = abap_false.
        CREATE OBJECT lo_crequest_util.

        CALL METHOD cl_usmd_model=>get_instance
          EXPORTING
            i_usmd_model = if_mdg_bp_constants=>gc_bp_model
          IMPORTING
            eo_instance  = lo_model
            et_message   = lt_messages.

        LOOP AT lt_messages ASSIGNING <ls_message> WHERE msgty CA 'EAX'.
          lv_error = abap_true.
          EXIT.
        ENDLOOP.

        IF lv_error = abap_false.
          CALL METHOD lo_crequest_util->get_crequest
            EXPORTING
              id_crequest = lo_app_context->mv_crequest_id
              io_model    = lo_model
            IMPORTING
              es_crequest = ls_crequest.

          IF ls_crequest IS NOT INITIAL.
            IF ls_crequest-usmd_creq_status = usmd0_cs_crequest_status-finally_approved OR ls_crequest-usmd_creq_status = usmd0_cs_crequest_status-finally_approved.
              gv_final_status_set = abap_true.
              lv_force_reload = abap_true.
            ENDIF.
          ENDIF.
        ENDIF.
      ENDIF.
    ENDIF.

    IF go_instance IS INITIAL OR lv_force_reload = abap_true.

      CREATE OBJECT go_instance TYPE zcl_mdg_bp_helper_staging
        EXCEPTIONS
          entity_data_all_read_error     = 1
          app_context_get_failed         = 2
          appcontext_attribute_get_error = 3
          model_get_failed               = 4
          discard_instance               = 5
          unexpected_error               = 6
          OTHERS                         = 7.

      IF sy-subrc <> 0.
        CASE sy-subrc.
          WHEN 1.
            MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_bp TYPE 'X' NUMBER 001 RAISING entity_data_all_read_error.
          WHEN 2.
            MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 004 RAISING app_context_get_failed.
          WHEN 3.
            MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_br_bp TYPE 'X' NUMBER 004 RAISING app_context_get_failed .
          WHEN 4.
            MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 001 RAISING  model_get_failed.
          WHEN 5.
            CALL METHOD destruct_instance.
            RETURN.
          WHEN 6.
            MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 000 RAISING unexpected_error.
          WHEN OTHERS.
            MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 000 RAISING unexpected_error.
        ENDCASE.
      ELSE.
        IF go_instance IS BOUND.
          go_instance->gv_wiid = lo_app_context->mv_wi_id.
          go_instance->gv_crid = lo_app_context->mv_crequest_id.
        ENDIF.

        ro_bp_data = go_instance.

        IF ro_bp_data IS NOT BOUND.
          MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 002 RAISING instance_creation_failed.
        ENDIF.
      ENDIF.

    ELSE.
      ro_bp_data = go_instance.
    ENDIF.

  ENDMETHOD.


  METHOD get_where_condition.

    DATA:
      lt_entity_keys  TYPE usmd_t_entity.

    FIELD-SYMBOLS:
      <lv_entity_key> TYPE usmd_entity,
      <lv_data_key>   TYPE any.

    CLEAR ev_where.

    CALL METHOD get_keys_of_entity
      EXPORTING
        iv_entity      = iv_entity
      IMPORTING
        et_entity_keys = lt_entity_keys.

* Build where condition
    LOOP AT lt_entity_keys ASSIGNING <lv_entity_key>.
      ASSIGN COMPONENT <lv_entity_key> OF STRUCTURE is_record TO <lv_data_key>.
      IF sy-subrc = 0 AND <lv_data_key> IS NOT INITIAL.
        IF ev_where IS NOT INITIAL.
          CONCATENATE ev_where ' AND ' INTO ev_where RESPECTING BLANKS.
        ENDIF.
        CONCATENATE ev_where <lv_entity_key> ' = ''' <lv_data_key> '''' INTO ev_where RESPECTING BLANKS.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD process_ext_number_assignment.

    DATA:
      lr_data_upd_bp_header TYPE REF TO data,
      lr_data_upd_bp_cntrl  TYPE REF TO data,
      lr_entity_data_struc  TYPE REF TO data,
      lr_entity_data_table  TYPE REF TO data,
      lv_is_tmp_key         TYPE usmd_flg,
      lr_entity             TYPE REF TO data,
      lt_bp_header          TYPE zif_mdg_bp_datatypes=>gty_t_bp_header,
      lt_bp_rel             TYPE zif_mdg_bp_datatypes=>gty_t_bp_rel,
      lv_main_bp            TYPE bu_partner,
      lt_entity_keys        TYPE usmd_t_entity,
      lv_where              TYPE string.

    FIELD-SYMBOLS:
      <lt_data_upd_bp_header>  TYPE SORTED TABLE,
      <ls_data_upd_bp_header>  TYPE any,
      <lt_data_upd_bp_cntrl>   TYPE SORTED TABLE,
      <lv_bp_header>           TYPE any,
      <lv_entity>              TYPE usmd_entity,
      <lt_entity>              TYPE SORTED TABLE,
      <ls_entity>              TYPE any,
      <lt_entity_exchg_new>    TYPE SORTED TABLE,
      <ls_entity_exchg_new>    TYPE any,
      <lv_bp_header_exchg_key> TYPE any,
      <ls_bp_header>           TYPE /mdgbp/_s_bp_pp_bp_header.

* get header data
    CALL METHOD io_changed_data->read_data
      EXPORTING
        i_entity      = if_mdg_bp_constants~gc_bp_model_entity-bp
        i_struct      = if_usmd_model_ext=>gc_struct_key_attr
      IMPORTING
        er_t_data_upd = lr_data_upd_bp_header.

    UNASSIGN <lt_data_upd_bp_header>.
    ASSIGN lr_data_upd_bp_header->* TO <lt_data_upd_bp_header>.

* get central data
    CALL METHOD io_changed_data->read_data
      EXPORTING
        i_entity      = if_mdg_bp_constants~gc_bp_model_entity-central
        i_struct      = if_usmd_model_ext=>gc_struct_key_attr
      IMPORTING
        er_t_data_upd = lr_data_upd_bp_cntrl.

    UNASSIGN <lt_data_upd_bp_cntrl>.
    ASSIGN lr_data_upd_bp_cntrl->* TO <lt_data_upd_bp_cntrl>.

* check if specific case is triggered (update of centrl and header at once)
    IF <lt_data_upd_bp_header> IS ASSIGNED AND <lt_data_upd_bp_cntrl> IS ASSIGNED.
      READ TABLE <lt_data_upd_bp_header> ASSIGNING <ls_data_upd_bp_header> INDEX 1.
      ASSIGN COMPONENT if_mdg_bp_constants~gc_field-bp_header OF STRUCTURE <ls_data_upd_bp_header> TO <lv_bp_header>.
      IF <lv_bp_header> IS ASSIGNED.

        "only process if tempory key was provided before
        CALL METHOD go_model->is_temporary_key
          EXPORTING
            i_fieldname  = if_mdg_bp_constants~gc_field-bp_header
            is_key       = <ls_data_upd_bp_header>
          RECEIVING
            ef_temporary = lv_is_tmp_key.
        IF lv_is_tmp_key = abap_false.
          " get additional entities to identfy previous key
          CALL METHOD get_bp_header
            IMPORTING
              et_bp_header = lt_bp_header.

          CALL METHOD get_bp_rel
            IMPORTING
              et_bp_rel = lt_bp_rel.

          LOOP AT lt_bp_header ASSIGNING <ls_bp_header>.
            READ TABLE lt_bp_rel WITH KEY partner2 = <ls_bp_header>-bp_header TRANSPORTING NO FIELDS. "#EC CI_SORTSEQ
            IF sy-subrc <> 0.
              "that's the key
              lv_main_bp = <ls_bp_header>-bp_header.
              EXIT.
            ENDIF.
          ENDLOOP.

          " check if extnumber is already assigned --> skip
          IF <lv_bp_header> = lv_main_bp.
            RETURN.
          ENDIF.

          " drop all entries based on previous key
          LOOP AT get_all_entities( ) ASSIGNING <lv_entity>.
            CLEAR: lv_where.
            CALL METHOD get_keys_of_entity
              EXPORTING
                iv_entity      = <lv_entity>
              IMPORTING
                et_entity_keys = lt_entity_keys.

            " consider use of different key name in serveral entities
            READ TABLE lt_entity_keys WITH KEY table_line = if_mdg_bp_constants~gc_field-bp_header TRANSPORTING NO FIELDS ##WARN_OK.
            IF sy-subrc = 0.
              CONCATENATE 'BP_HEADER = ' '''' lv_main_bp '''' INTO lv_where RESPECTING BLANKS.
            ELSE.
              READ TABLE lt_entity_keys WITH KEY table_line = if_mdg_bp_constants~gc_field-partner1 TRANSPORTING NO FIELDS ##WARN_OK.
              IF sy-subrc = 0.
                CONCATENATE 'PARTNER1 = ' '''' lv_main_bp '''' INTO lv_where RESPECTING BLANKS.
              ELSE.
                "if key is not available --> proceed with next
                CONTINUE.
              ENDIF.
            ENDIF.

            " fetch table and execute DELETE to drop old key entries
            CALL METHOD get_entity_reference
              EXPORTING
                iv_entity = <lv_entity>
              IMPORTING
                er_entity = lr_entity.
            IF lr_entity IS NOT BOUND.
              MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_bp TYPE 'X' NUMBER 003 INTO zcl_mdg_general_functions=>gv_error_message.
            ENDIF.

            " for all entites, exchange the temporary key with the external number
            ASSIGN lr_entity->* TO <lt_entity>.
            IF <lt_entity> IS ASSIGNED AND <lt_entity> IS NOT INITIAL.

              CREATE DATA lr_entity_data_table LIKE <lt_entity>.
              ASSIGN lr_entity_data_table->* TO <lt_entity_exchg_new>.

              LOOP AT <lt_entity> ASSIGNING <ls_entity>. "#EC CI_NESTED

                " create empty structure of same type and move all data into it
                CREATE DATA lr_entity_data_struc LIKE LINE OF <lt_entity>.
                ASSIGN lr_entity_data_struc->* TO <ls_entity_exchg_new>.
                MOVE-CORRESPONDING <ls_entity> TO <ls_entity_exchg_new>.

                " exchange BP number with new external number
                ASSIGN COMPONENT 'BP_HEADER' OF STRUCTURE <ls_entity_exchg_new> TO <lv_bp_header_exchg_key>.
                IF sy-subrc = 0.
                  <lv_bp_header_exchg_key> = <lv_bp_header>.
                ELSE.
                  ASSIGN COMPONENT 'PARTNER1' OF STRUCTURE <ls_entity_exchg_new> TO <lv_bp_header_exchg_key>.
                  IF sy-subrc = 0.
                    <lv_bp_header_exchg_key> = <lv_bp_header>.
                  ELSE.
                    CONTINUE.
                  ENDIF.
                ENDIF.

                " insert entity into temporary table
                INSERT <ls_entity_exchg_new> INTO TABLE <lt_entity_exchg_new>.
              ENDLOOP.

              " delete all old entries and insert new
              DELETE <lt_entity> WHERE (lv_where).
              IF sy-subrc = 0.
                INSERT LINES OF <lt_entity_exchg_new> INTO TABLE <lt_entity>.
              ENDIF.
            ENDIF.
          ENDLOOP.
        ENDIF.
      ENDIF.
    ENDIF.

  ENDMETHOD.


  METHOD read_active_data_of_cr.

    DATA:
      ls_bp_rel_sel      TYPE usmd_s_sel,
      lt_bp_rel1_sel     TYPE usmd_ts_sel,
      lt_bp_rel2_sel     TYPE usmd_ts_sel,
      ls_sel             TYPE usmd_s_sel,
      lt_sel             TYPE usmd_ts_sel,
      lt_entity_data_act TYPE usmd_ts_data_entity.

    FIELD-SYMBOLS:
      <lv_bp>                  TYPE bu_partner,
      <ls_data_bp_rel_all>     TYPE usmd_sx_data_entity,
      <lv_partner1>            TYPE any,
      <lv_partner2>            TYPE any,
      <lt_bp_rel_data>         TYPE ANY TABLE,
      <ls_bp_rel_data>         TYPE any,
      <ls_entity_data_act_tmp> TYPE usmd_sx_data_entity,
      <ls_entity_data_act>     TYPE usmd_sx_data_entity,
      <lt_data_tmp>            TYPE ANY TABLE,
      <ls_data_tmp>            TYPE any,
      <lt_data_act>            TYPE ANY TABLE.


    CLEAR et_entity_data_act.


    LOOP AT it_businesspartner ASSIGNING <lv_bp>. ##GEN_OK
      ls_sel-fieldname = if_mdg_bp_constants~gc_field-bp_header.
      ls_sel-sign = usmd0_cs_ra-sign_i.
      ls_sel-option = usmd0_cs_ra-option_eq.
      ls_sel-low = <lv_bp>.
      INSERT ls_sel INTO TABLE lt_sel.

      " get BP_REL data
      ls_bp_rel_sel-sign = usmd0_cs_ra-sign_i.
      ls_bp_rel_sel-option = usmd0_cs_ra-option_eq.
      ls_bp_rel_sel-low = <lv_bp>.

      " get BP_REL data of partner 1 into active data
      ls_bp_rel_sel-fieldname = if_mdg_bp_constants~gc_field-partner1.
      INSERT ls_bp_rel_sel INTO TABLE lt_bp_rel1_sel.

      " get BP_REL data of partner 2 into active data
      ls_bp_rel_sel-fieldname = if_mdg_bp_constants~gc_field-partner2.
      INSERT ls_bp_rel_sel INTO TABLE lt_bp_rel2_sel.

    ENDLOOP.


    "Read BP_REL active data of partner 1
    IF lt_bp_rel1_sel IS NOT INITIAL.
      CALL METHOD io_model->read_entity_data_all
        EXPORTING
          i_fieldname    = if_mdg_bp_constants~gc_field-bp_rel
          if_active      = abap_true
          it_sel         = lt_bp_rel1_sel
        IMPORTING
          et_data_entity = lt_entity_data_act.
    ENDIF.

    INSERT LINES OF lt_entity_data_act INTO TABLE et_entity_data_act.
*    APPEND LINES OF lt_entity_data_act TO lt_entity_data_bprel.
    CLEAR lt_entity_data_act.

    "Read BP_REL active data of partner 2
    IF lt_bp_rel2_sel IS NOT INITIAL.
      CALL METHOD io_model->read_entity_data_all
        EXPORTING
          i_fieldname    = if_mdg_bp_constants~gc_field-bp_rel
          if_active      = abap_true
          it_sel         = lt_bp_rel2_sel
        IMPORTING
          et_data_entity = lt_entity_data_act.
    ENDIF.


*merge BP_REL data of partner 2 and all active data

    LOOP AT lt_entity_data_act ASSIGNING <ls_entity_data_act_tmp>.
      UNASSIGN <ls_entity_data_act>.
      READ TABLE et_entity_data_act ASSIGNING <ls_entity_data_act> WITH TABLE KEY usmd_entity      = <ls_entity_data_act_tmp>-usmd_entity
                                                                                  usmd_entity_cont = <ls_entity_data_act_tmp>-usmd_entity_cont
                                                                                  struct           = <ls_entity_data_act_tmp>-struct.
      IF <ls_entity_data_act> IS ASSIGNED.
        ASSIGN <ls_entity_data_act_tmp>-r_t_data->* TO <lt_data_tmp>.
        ASSIGN <ls_entity_data_act>-r_t_data->* TO <lt_data_act>.

        LOOP AT <lt_data_tmp> ASSIGNING <ls_data_tmp>. "#EC CI_NESTED
          INSERT <ls_data_tmp> INTO TABLE <lt_data_act>.
        ENDLOOP.
      ELSE.
        INSERT <ls_entity_data_act_tmp> INTO TABLE et_entity_data_act.
      ENDIF.
    ENDLOOP.

* re-load the data of the related BP
    LOOP AT et_entity_data_act ASSIGNING <ls_data_bp_rel_all>
       WHERE usmd_entity = if_mdg_bp_constants~gc_bp_model_entity-relation
         AND usmd_entity_cont IS INITIAL.
      UNASSIGN: <lt_bp_rel_data>, <ls_bp_rel_data>, <lv_partner1>, <lv_partner2>.
      CLEAR ls_sel-low.
      ASSIGN <ls_data_bp_rel_all>-r_t_data->* TO <lt_bp_rel_data>.
      LOOP AT <lt_bp_rel_data> ASSIGNING <ls_bp_rel_data>. "#EC CI_NESTED
        "partner 1
        ASSIGN COMPONENT if_mdg_bp_constants~gc_field-partner1 OF STRUCTURE <ls_bp_rel_data> TO <lv_partner1>.
        IF <lv_partner1> IS ASSIGNED AND <lv_partner1> IS NOT INITIAL.
          READ TABLE lt_sel WITH KEY low = <lv_partner1> TRANSPORTING NO FIELDS. "#EC CI_SORTSEQ
          IF sy-subrc NE 0.
            ls_sel-low = <lv_partner1>.
            INSERT ls_sel INTO TABLE lt_sel.
          ENDIF.
        ENDIF.
        "partner 2
        ASSIGN COMPONENT if_mdg_bp_constants~gc_field-partner2 OF STRUCTURE <ls_bp_rel_data> TO <lv_partner2>.
        IF <lv_partner2> IS ASSIGNED AND <lv_partner2> IS NOT INITIAL.
          READ TABLE lt_sel WITH KEY low = <lv_partner2> TRANSPORTING NO FIELDS. "#EC CI_SORTSEQ
          IF sy-subrc NE 0.
            ls_sel-low = <lv_partner2>.
            INSERT ls_sel INTO TABLE lt_sel.
          ENDIF.
        ENDIF.
      ENDLOOP.
    ENDLOOP.


    CLEAR: lt_entity_data_act.

    "Read active data of main BP
    IF lt_sel IS NOT INITIAL.
      CALL METHOD io_model->read_entity_data_all
        EXPORTING
          i_fieldname    = if_mdg_bp_constants~gc_field-bp_header
          if_active      = abap_true
          it_sel         = lt_sel
        IMPORTING
          et_data_entity = lt_entity_data_act.
    ENDIF.

    INSERT LINES OF lt_entity_data_act INTO TABLE et_entity_data_act.



  ENDMETHOD.


  METHOD read_changed_documents.

    TYPES:
      BEGIN OF ty_s_tab,
        field(50),
      END OF ty_s_tab.

    DATA:
      lo_adapter           TYPE REF TO if_usmd_chg_doc_adapter,
      lt_change_request_id TYPE cl_usmd_mdf_change_document=>t_change_request,
      lt_document_header   TYPE cl_usmd_mdf_change_document=>t_document_header,
      lt_changed_value     TYPE usmd_ts_change_document_value,
      lt_changed_detail    TYPE usmd_th_change_document_change,
      lt_compound_value    TYPE usmd_ts_change_document_value,
      lt_message           TYPE usmd_t_message,
      ls_change_document   TYPE zif_mdg_datatypes=>gty_s_change_document,
      lt_tab               TYPE TABLE OF ty_s_tab,
      lv_line              TYPE i,
      lv_field             TYPE string,
      lv_crequest          TYPE usmd_crequest,
      lo_app_context       TYPE REF TO if_usmd_app_context.

    CLEAR:et_change_documents,et_all_changed_detail,et_all_changed_value.
    FIELD-SYMBOLS: <ls_docu_header>    TYPE if_usmd_chg_doc_adapter_type=>s_document_header,
                   <ls_changed_detail> TYPE usmd_s_change_document_change.

    lo_app_context = cl_usmd_app_context=>get_context( ).

    lo_app_context->get_attributes(
      IMPORTING
        ev_crequest_id    =   lv_crequest
    ).

    IF gt_change_documents IS INITIAL.
      cl_usmd_adapter_provider=>get_chg_document_adapter(
        EXPORTING
          i_usmd_model       =    zcl_mdg_bp_helper=>if_mdg_bp_constants~gc_bp_model
        IMPORTING
          eo_chg_doc_adapter =     lo_adapter
      ).

      IF lo_adapter IS NOT BOUND OR lv_crequest IS INITIAL.
        RETURN.
      ENDIF.

* Read change document header data
      INSERT lv_crequest INTO TABLE lt_change_request_id.
      lo_adapter->read_document_header(
        EXPORTING
          it_crequest         = lt_change_request_id
        IMPORTING
          et_document_header  = lt_document_header
      ).

* Read change document position data
      LOOP AT lt_document_header ASSIGNING <ls_docu_header>.

        lo_adapter->read_document_lines(
          EXPORTING
            is_document_header = <ls_docu_header>
          IMPORTING
            et_changed_value   = lt_changed_value
            et_changed_detail  = lt_changed_detail
            et_compound_value  = lt_compound_value
            et_message         = lt_message
        ).

        CLEAR: ls_change_document-changed_value, ls_change_document-compound_value,
               ls_change_document-message, ls_change_document-changed_details.

        APPEND LINES OF: lt_changed_value   TO ls_change_document-changed_value,
                         lt_compound_value  TO ls_change_document-compound_value,
                         lt_message         TO ls_change_document-message.

        INSERT LINES OF lt_changed_detail INTO TABLE ls_change_document-changed_details.

* MDG API returns text with table name, extract the table name from relationship details.
        LOOP AT lt_changed_detail ASSIGNING <ls_changed_detail>. "#EC CI_NESTED
          SPLIT <ls_changed_detail>-table AT space INTO TABLE lt_tab.
          DESCRIBE TABLE lt_tab LINES lv_line.
          READ TABLE lt_tab TRANSPORTING ALL FIELDS INTO lv_field INDEX lv_line.
          IF sy-subrc = 0.
            <ls_changed_detail>-table = lv_field.
          ENDIF.
          INSERT <ls_changed_detail> INTO TABLE et_all_changed_detail.
        ENDLOOP.
        APPEND LINES OF lt_changed_value TO et_all_changed_value.
        APPEND ls_change_document TO et_change_documents.
      ENDLOOP.
      gt_change_documents = et_change_documents.
      gt_all_changed_detail = et_all_changed_detail.
      gt_all_changed_value = et_all_changed_value.
    ELSE.
      et_change_documents = gt_change_documents.
      et_all_changed_detail = gt_all_changed_detail.
      et_all_changed_value = gt_all_changed_value.
    ENDIF.

  ENDMETHOD.


  METHOD read_entity_data_cr.

    TYPES: BEGIN OF ty_s_usmd1222,
             entity_type       TYPE usmd_entity,
             entity_key        TYPE usmd_entity_key_hash,
             entity_key_string TYPE usmd_entity_key_string,
           END OF ty_s_usmd1222,
           ty_t_usmd1222 TYPE SORTED TABLE OF ty_s_usmd1222 WITH UNIQUE KEY entity_type entity_key.

    CONSTANTS:
      lc_prefix      TYPE string VALUE 'GT_',
      lc_suffix_text TYPE string VALUE '_TXT'.

    DATA:
      lt_key_all               TYPE usmd_ts_entity_data,
      lo_context               TYPE REF TO if_usmd_app_context,
      lo_model                 TYPE REF TO if_usmd_model_ext,
      lt_entity_data           TYPE usmd_ts_data_entity,
      lt_entity_data_act       TYPE usmd_ts_data_entity,
      ls_entity_data_act       TYPE usmd_sx_data_entity,
      lt_data_entity_bp_ad     TYPE usmd_ts_data_entity,
      lt_data_entity_bp_rel    TYPE usmd_ts_data_entity,
*      lt_message               TYPE usmd_t_message, ##NEEDED
      lv_entity                TYPE usmd_entity,
      lv_fieldname             TYPE usmd_fieldname,
      lr_entity_key_struc      TYPE REF TO data,
      lr_entity_key_struc_1222 TYPE REF TO data,
      lo_key_conv              TYPE REF TO if_usmd_key_conversion,
      lt_usmd1222              TYPE ty_t_usmd1222,
      lv_is_parallel           TYPE boolean,
      lt_businesspartner       TYPE TABLE OF bu_partner,
      lv_found                 TYPE boolean,
      lv_updated               TYPE boolean,
      lr_entity                TYPE REF TO data,
      lv_entity_tabname        TYPE seocpdname.

    FIELD-SYMBOLS:
      <ls_usmd1222>              TYPE ty_s_usmd1222,
      <ls_entity_data>           TYPE usmd_sx_data_entity,
      <ls_entity_data_act>       TYPE usmd_sx_data_entity,
      <lt_entity>                TYPE ANY TABLE,
      <lt_entity_act>            TYPE ANY TABLE,
      <ls_entity>                TYPE any,
      <ls_entity_act>            TYPE any,
      <ls_entity_key_struc>      TYPE any,
      <ls_entity_key_struc_1222> TYPE any,
      <lt_data>                  TYPE ANY TABLE,
      <lt_mt_entity>             TYPE SORTED TABLE,
      <ls_key_all>               TYPE usmd_sx_entity_data,
      <lt_key>                   TYPE ANY TABLE.


    CALL METHOD cl_usmd_app_context=>get_context
      RECEIVING
        eo_context = lo_context.

    IF lo_context IS NOT BOUND.
      RAISE app_context_get_failed.
    ENDIF.

*Get Model Instance and CR ID from the aplication context
    CALL METHOD lo_context->get_attributes
      IMPORTING
        eo_model = lo_model.
    IF lo_model IS NOT BOUND.
      RAISE appcontext_attribute_get_error.
    ENDIF.

    "Set key fields: CR ID, WI ID, Final status
    me->gv_crid = lo_context->mv_crequest_id.
    me->gv_wiid = lo_context->mv_wi_id.

    IF cl_usmd_crequest_util=>is_crequest_closed( i_crequest_status = cl_usmd_crequest_util=>get_cr_status_by_cr(
                                                                        i_crequest = lo_context->mv_crequest_id
                                                                      )  ).
      me->gv_final_status_set = abap_true.
    ENDIF.

* Get all business partner in CR

    CALL METHOD lo_model->get_cr_objectlist
      EXPORTING
        i_crequest = lo_context->mv_crequest_id
      IMPORTING
        et_key_all = lt_key_all.

    READ TABLE lt_key_all ASSIGNING <ls_key_all> WITH TABLE KEY entity = if_mdg_bp_constants~gc_field-bp_header.
    IF sy-subrc IS INITIAL.
      ASSIGN <ls_key_all>-r_data->* TO <lt_key>.
      lt_businesspartner = <lt_key>.
    ELSE.
      RETURN.
    ENDIF.


    IF me->gv_final_status_set EQ abap_false.
*read all BP entity DATA from staging area
      CALL METHOD lo_model->read_entity_data_all
        EXPORTING
          i_fieldname    = if_mdg_bp_constants~gc_field-bp_header
          i_crequest     = lo_context->mv_crequest_id
          if_active      = abap_false
        IMPORTING
*          et_message     = lt_message
          et_data_entity = lt_entity_data.

* special handling for entity bp_rel
      CALL METHOD lo_model->read_entity_data_all
        EXPORTING
          i_fieldname    = 'BP_REL'
          i_crequest     = lo_context->mv_crequest_id
          if_active      = abap_false
        IMPORTING
*          et_message     = lt_message
          et_data_entity = lt_data_entity_bp_rel.

      INSERT LINES OF lt_data_entity_bp_rel INTO TABLE lt_entity_data.

* Special handling for entity ADDRNO
      CALL METHOD lo_model->read_entity_data_all
        EXPORTING
          i_fieldname    = 'ADDRNO'
          i_crequest     = lo_context->mv_crequest_id
          if_active      = abap_false
        IMPORTING
*          et_message     = lt_message
          et_data_entity = lt_data_entity_bp_ad.

      INSERT LINES OF lt_data_entity_bp_ad INTO TABLE lt_entity_data.

    ELSE.

      CALL METHOD read_active_data_of_cr
        EXPORTING
*          iv_crequest        = lo_context->mv_crequest_id
          io_model           = lo_model
          it_businesspartner = lt_businesspartner
        IMPORTING
          et_entity_data_act = lt_entity_data.

    ENDIF.

    "If we have a CR type that has parallel processing enabled we have to remove changes from other CRs
    CALL METHOD cl_usmd2_cust_access_service=>is_parallel_cr_type
      EXPORTING
        iv_creq_type   = lo_context->mv_crequest_type
      RECEIVING
        rv_is_parallel = lv_is_parallel.

    IF lv_is_parallel EQ abap_true.
      SELECT entity_type entity_key entity_key_string FROM usmd1222 "#EC CI_SUBRC
        INTO TABLE lt_usmd1222
        WHERE crequest_id EQ lo_context->mv_crequest_id.

      "Get active data
      CALL METHOD read_active_data_of_cr
        EXPORTING
*          iv_crequest        = lo_context->mv_crequest_id
          io_model           = lo_model
          it_businesspartner = lt_businesspartner
        IMPORTING
          et_entity_data_act = lt_entity_data_act.

      CALL METHOD cl_usmd_key_conversion=>get_instance
        RECEIVING
          ro_key_conversion = lo_key_conv.

      LOOP AT lt_usmd1222 ASSIGNING <ls_usmd1222>.
        lv_entity = <ls_usmd1222>-entity_type.
        lv_fieldname = lv_entity.

        CALL METHOD lo_model->create_data_reference
          EXPORTING
            i_fieldname = lv_fieldname
            i_struct    = lo_model->gc_struct_key
            if_table    = abap_false
          IMPORTING
            er_data     = lr_entity_key_struc_1222.
        ASSIGN lr_entity_key_struc_1222->* TO <ls_entity_key_struc_1222>.

        CALL METHOD lo_model->create_data_reference
          EXPORTING
            i_fieldname = lv_fieldname
            i_struct    = lo_model->gc_struct_key
            if_table    = abap_false
          IMPORTING
            er_data     = lr_entity_key_struc.
        ASSIGN lr_entity_key_struc->* TO <ls_entity_key_struc>.

        "Get key of change
        CALL METHOD lo_key_conv->string_tech_2_entity_key
          EXPORTING
            iv_key_string  = <ls_usmd1222>-entity_key_string
          IMPORTING
            ev_entity_type = lv_entity
            es_entity_key  = <ls_entity_key_struc_1222>.

        "Get the corresponding inactive data
        UNASSIGN <ls_entity_data>.
        READ TABLE lt_entity_data ASSIGNING <ls_entity_data>
          WITH KEY usmd_entity = if_mdg_bp_constants~gc_field-bp_header
                   usmd_entity_cont = lv_entity.
        IF sy-subrc IS NOT INITIAL.
          READ TABLE lt_entity_data ASSIGNING <ls_entity_data>
            WITH KEY usmd_entity = lv_entity
                     usmd_entity_cont = space.
        ENDIF.

        IF <ls_entity_data> IS ASSIGNED.
          ASSIGN <ls_entity_data>-r_t_data->* TO <lt_entity>.
          lv_found = abap_false.
          LOOP AT <lt_entity> ASSIGNING <ls_entity>.     "#EC CI_NESTED
            MOVE-CORRESPONDING <ls_entity> TO <ls_entity_key_struc>.
            IF <ls_entity_key_struc> EQ <ls_entity_key_struc_1222>.
              lv_found = abap_true.
              EXIT.
            ENDIF.
          ENDLOOP.

          "If found replace the act data with inact data
          "If NOT found we have a deletion -> remove from active data
          IF lv_found EQ abap_true.
            "Update or Insert
            UNASSIGN  <ls_entity_data_act>.
            READ TABLE lt_entity_data_act ASSIGNING <ls_entity_data_act>
              WITH KEY usmd_entity = if_mdg_bp_constants~gc_field-bp_header
                       usmd_entity_cont = lv_entity.
            IF sy-subrc IS NOT INITIAL.
              READ TABLE lt_entity_data_act ASSIGNING <ls_entity_data_act>
                WITH KEY usmd_entity = lv_entity
                         usmd_entity_cont = space.
            ENDIF.

            IF <ls_entity_data_act> IS ASSIGNED. "Update
              lv_updated = abap_false.
              ASSIGN <ls_entity_data_act>-r_t_data->* TO <lt_entity_act>.
              LOOP AT <lt_entity_act> ASSIGNING <ls_entity_act>. "#EC CI_NESTED
                MOVE-CORRESPONDING <ls_entity_act> TO <ls_entity_key_struc>.
                IF <ls_entity_key_struc> EQ <ls_entity_key_struc_1222>.
                  DELETE TABLE <lt_entity_act> FROM <ls_entity_act>. "#EC CI_ANYSEQ
                  INSERT <ls_entity> INTO TABLE <lt_entity_act>.
                  lv_updated = abap_true.
                  EXIT.
                ENDIF.
              ENDLOOP.
              IF lv_updated EQ abap_false. "Insert new entry
                INSERT <ls_entity> INTO TABLE <lt_entity_act>.
              ENDIF.
            ELSE. "Insert
              CLEAR ls_entity_data_act.
              ls_entity_data_act-struct = <ls_entity_data>-struct.
              ls_entity_data_act-usmd_entity = <ls_entity_data>-usmd_entity.
              ls_entity_data_act-usmd_entity_cont = <ls_entity_data>-usmd_entity_cont.
              CREATE DATA ls_entity_data_act-r_t_data LIKE <lt_entity>.
              ASSIGN ls_entity_data_act-r_t_data->* TO <lt_entity_act>.
              INSERT <ls_entity> INTO TABLE <lt_entity_act>.
              INSERT ls_entity_data_act INTO TABLE lt_entity_data_act.
            ENDIF.


          ELSE. "delete
            UNASSIGN  <ls_entity_data_act>.
            READ TABLE lt_entity_data_act ASSIGNING <ls_entity_data_act>
              WITH KEY usmd_entity = if_mdg_bp_constants~gc_field-bp_header
                       usmd_entity_cont = lv_entity.
            IF sy-subrc IS NOT INITIAL.
              READ TABLE lt_entity_data_act ASSIGNING <ls_entity_data_act>
                WITH KEY usmd_entity = lv_entity
                         usmd_entity_cont = space.
            ENDIF.
            IF <ls_entity_data_act> IS ASSIGNED.
              ASSIGN <ls_entity_data_act>-r_t_data->* TO <lt_entity_act>.
              LOOP AT <lt_entity_act> ASSIGNING <ls_entity_act>. "#EC CI_NESTED
                MOVE-CORRESPONDING <ls_entity_act> TO <ls_entity_key_struc>.
                IF <ls_entity_key_struc> EQ <ls_entity_key_struc_1222>.
                  DELETE TABLE <lt_entity_act> FROM <ls_entity_act>. "#EC CI_ANYSEQ
                ENDIF.
              ENDLOOP.
            ENDIF. "IF <ls_entity_data_act> IS ASSIGNED.
          ENDIF.
        ELSE. "Delete
          UNASSIGN  <ls_entity_data_act>.
          READ TABLE lt_entity_data_act ASSIGNING <ls_entity_data_act>
            WITH KEY usmd_entity = if_mdg_bp_constants~gc_field-bp_header
                     usmd_entity_cont = lv_entity.
          IF sy-subrc IS NOT INITIAL.
            READ TABLE lt_entity_data_act ASSIGNING <ls_entity_data_act>
              WITH KEY usmd_entity = lv_entity
                       usmd_entity_cont = space.
          ENDIF.
          IF <ls_entity_data_act> IS ASSIGNED.
            ASSIGN <ls_entity_data_act>-r_t_data->* TO <lt_entity_act>.
            LOOP AT <lt_entity_act> ASSIGNING <ls_entity_act>. "#EC CI_NESTED
              MOVE-CORRESPONDING <ls_entity_act> TO <ls_entity_key_struc>.
              IF <ls_entity_key_struc> EQ <ls_entity_key_struc_1222>.
                DELETE TABLE <lt_entity_act> FROM <ls_entity_act>. "#EC CI_ANYSEQ
              ENDIF.
            ENDLOOP.
          ENDIF."IF <ls_entity_data_act> IS ASSIGNED.
        ENDIF.
      ENDLOOP.

      lt_entity_data = lt_entity_data_act.
    ENDIF. "IF lv_is_parallel EQ abap_true.


    "Now we have gathered the correct data
    "It has to be stored in the GTs
* Transform untyped to typed data
    LOOP AT lt_entity_data ASSIGNING <ls_entity_data>.
      CLEAR: lv_entity_tabname, lr_entity.
      UNASSIGN: <ls_entity>, <lt_data>, <lt_mt_entity>.
* Construct export table name and assign it to field symbol (it's used to fill the related mt)

      CASE <ls_entity_data>-struct.
        WHEN if_usmd_model_ext=>gc_struct_key_attr.
          IF <ls_entity_data>-usmd_entity_cont IS INITIAL.
            CONCATENATE lc_prefix <ls_entity_data>-usmd_entity INTO lv_entity_tabname.
          ELSE.
            CONCATENATE lc_prefix <ls_entity_data>-usmd_entity_cont INTO lv_entity_tabname.
          ENDIF.
        WHEN if_usmd_model_ext=>gc_struct_key_txt_langu.
          IF <ls_entity_data>-usmd_entity_cont IS INITIAL.
            CONCATENATE lc_prefix <ls_entity_data>-usmd_entity lc_suffix_text INTO lv_entity_tabname.
          ELSE.
            CONCATENATE lc_prefix <ls_entity_data>-usmd_entity_cont lc_suffix_text INTO lv_entity_tabname.
          ENDIF.
      ENDCASE.

* write data to gt_* tables
      ASSIGN (lv_entity_tabname) TO <lt_mt_entity>.       "#EC CI_SUBRC
      IF <lt_mt_entity> IS NOT ASSIGNED.
        MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_bp TYPE 'X' NUMBER 002 WITH lv_entity_tabname.
        RAISE dyn_assignment_failed.
      ENDIF.

      CREATE DATA lr_entity LIKE LINE OF <lt_mt_entity>.
      ASSIGN lr_entity->* TO <ls_entity>.
      IF <ls_entity> IS NOT ASSIGNED.
        MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_bp TYPE 'X' NUMBER 002 WITH lv_entity_tabname.
        RAISE dyn_assignment_failed.
      ENDIF.

      CLEAR: <ls_entity>, <lt_mt_entity>.

      ASSIGN <ls_entity_data>-r_t_data->* TO <lt_data>.
      IF sy-subrc <> 0.
        MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_bp TYPE 'X' NUMBER 002 WITH lv_entity_tabname.
        RAISE dyn_assignment_failed.
      ENDIF.

      IF <lt_data> IS ASSIGNED.
        MOVE-CORRESPONDING <lt_data> TO <lt_mt_entity>.
      ENDIF.

    ENDLOOP.

  ENDMETHOD.
ENDCLASS.