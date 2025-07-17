class ZCL_MDG_BP_HELPER_ACTIVE definition
  public
  inheriting from ZCL_MDG_BP_HELPER
  final
  create private .

public section.

  class-methods GET_INSTANCE
    importing
      !IV_BP_ID type BU_PARTNER
    returning
      value(RO_BP_DATA) type ref to ZCL_MDG_BP_HELPER
    exceptions
      INSTANCE_CREATION_FAILED
      ENTITY_DATA_ALL_READ_ERROR
      APP_CONTEXT_GET_FAILED
      APPCONTEXT_ATTRIBUTE_GET_ERROR
      UNEXPECTED_ERROR
      MODEL_GET_FAILED .
  class-methods DESTRUCT_INSTANCE
    importing
      !IV_BP_ID type BU_PARTNER .
  class-methods DESTRUCT_INSTANCES .
protected section.
PRIVATE SECTION.

  TYPES:
    BEGIN OF ty_s_instance,
      bp       TYPE bu_partner,
      instance TYPE REF TO zcl_mdg_bp_helper,
    END OF ty_s_instance .
  TYPES:
    ty_t_instance TYPE SORTED TABLE OF ty_s_instance WITH UNIQUE KEY bp .

  DATA gt_all_changed_detail TYPE usmd_th_change_document_change . ##NEEDED
  DATA gt_all_changed_value TYPE usmd_ts_change_document_value . ##NEEDED
  DATA gt_change_documents TYPE zif_mdg_datatypes=>gty_t_change_document . ##NEEDED
  CLASS-DATA gt_instances TYPE ty_t_instance .

  METHODS constructor
    IMPORTING
      !iv_bp_id TYPE bu_partner
    EXCEPTIONS
      entity_data_all_read_error
      app_context_get_failed
      appcontext_attribute_get_error
      model_get_failed
      discard_instance
      unexpected_error .
  METHODS read_data_from_bp
    IMPORTING
      !iv_bp_id TYPE bu_partner .
ENDCLASS.



CLASS ZCL_MDG_BP_HELPER_ACTIVE IMPLEMENTATION.


  METHOD constructor.

    super->constructor( ).

    IF iv_bp_id IS NOT INITIAL.
      CALL METHOD read_data_from_bp
        EXPORTING
          iv_bp_id = iv_bp_id.

      IF sy-subrc <> 0. ##SUBRC_OK
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
    ENDIF.
  ENDMETHOD.


  METHOD destruct_instance.

    DELETE gt_instances WHERE bp EQ iv_bp_id.

  ENDMETHOD.


  METHOD destruct_instances.

    CLEAR gt_instances.

  ENDMETHOD.


  METHOD get_instance.

    DATA:
      ls_instance TYPE ty_s_instance,
      lv_bp_id    TYPE bu_partner.

    FIELD-SYMBOLS:
      <ls_instance> TYPE ty_s_instance.

    IF NOT iv_bp_id(1) = '$'.
      lv_bp_id = iv_bp_id.
    ENDIF.

    READ TABLE gt_instances ASSIGNING <ls_instance> WITH TABLE KEY bp = iv_bp_id.

    IF sy-subrc = 0 AND <ls_instance>-instance IS NOT INITIAL.
      ro_bp_data = <ls_instance>-instance.
    ELSE.
*      ls_instance-bp = iv_bp_id.
      ls_instance-bp = lv_bp_id.
      CREATE OBJECT ls_instance-instance TYPE zcl_mdg_bp_helper_active
        EXPORTING
*         iv_bp_id                       = iv_bp_id
          iv_bp_id                       = lv_bp_id
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
            CALL METHOD destruct_instance
              EXPORTING
                iv_bp_id = iv_bp_id.
            RETURN.
          WHEN 6.
            MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 000 RAISING unexpected_error.
          WHEN OTHERS.
            MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 000 RAISING unexpected_error.
        ENDCASE.
      ENDIF.

      INSERT ls_instance INTO TABLE gt_instances.

      ro_bp_data = ls_instance-instance.
    ENDIF.

    IF ro_bp_data IS NOT BOUND.
      MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 002 RAISING instance_creation_failed.
    ENDIF.

  ENDMETHOD.


  METHOD READ_DATA_FROM_BP.

    CONSTANTS:
      lc_prefix      TYPE string VALUE 'GT_',
      lc_suffix_text TYPE string VALUE '_TXT'.

    DATA:
      lt_data_entity_bp     TYPE usmd_ts_data_entity,
      lt_data_entity_bp_rel TYPE usmd_ts_data_entity,
      lt_data_entity_bp_ad  TYPE usmd_ts_data_entity,
      lt_data_entity_all    TYPE usmd_ts_data_entity,
      lt_message            TYPE usmd_t_message,
      lv_entity_tabname     TYPE seocpdname,
      lt_bp_selection       TYPE usmd_ts_sel,
      ls_bp_selection       TYPE usmd_s_sel,
      lt_ad_selection       TYPE usmd_ts_sel,
      ls_ad_selection       TYPE usmd_s_sel,
      lt_bp_rel_sel         TYPE usmd_ts_sel,
      ls_bp_rel_sel         TYPE usmd_s_sel,
      lr_entity             TYPE REF TO data,
      lv_active             TYPE abap_bool.

    FIELD-SYMBOLS:
      <ls_bp_entity_rel_data> TYPE usmd_sx_data_entity,
      <lt_bp_rel_data>        TYPE ANY TABLE,
      <ls_bp_rel_data>        TYPE any,
      <lv_partner2>           TYPE any,
      <ls_data>               TYPE any,
      <ls_data_entity>        TYPE usmd_sx_data_entity,
      <lt_mt_entity>          TYPE SORTED TABLE,
      <ls_entity>             TYPE any,
      <lt_data>               TYPE ANY TABLE,
      <lv_addrno>             TYPE ad_addrnum.

    IF iv_bp_id  IS INITIAL.
      MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 000.
    ENDIF.

    IF iv_bp_id CA '$'.
      lv_active = abap_false.
    ELSE.
      lv_active = abap_true.
    ENDIF.

    IF sy-subrc = 0 AND iv_bp_id IS NOT INITIAL.
      ls_bp_selection-fieldname = if_mdg_bp_constants=>gc_bp_model_entity-bp.
      ls_bp_selection-sign      = usmd0_cs_ra-sign_i.
      ls_bp_selection-option    = usmd0_cs_ra-option_eq.
      ls_bp_selection-low       = iv_bp_id .
      INSERT ls_bp_selection INTO TABLE lt_bp_selection.

*********************
*special handling for BP_REL and corresponding contact persons
** build selection parameters to read relevant relations
      ls_bp_rel_sel-sign   = usmd0_cs_ra-sign_i.
      ls_bp_rel_sel-option = usmd0_cs_ra-option_eq.
      ls_bp_rel_sel-fieldname = ZCL_MDG_BP_HELPER=>if_mdg_bp_constants~gc_field-partner1.
      ls_bp_rel_sel-low       = iv_bp_id .
      INSERT ls_bp_rel_sel INTO TABLE lt_bp_rel_sel.
    ENDIF.

    IF lt_bp_rel_sel IS NOT INITIAL.
      CALL METHOD go_model->read_entity_data_all
        EXPORTING
          i_fieldname    = ZCL_MDG_BP_HELPER=>if_mdg_bp_constants~gc_field-bp_rel
          it_sel         = lt_bp_rel_sel
          if_active      = lv_active
        IMPORTING
          et_message     = lt_message
          et_data_entity = lt_data_entity_bp_rel.

      IF lt_message IS NOT INITIAL.
        RETURN.
      ENDIF.
    ENDIF.

* also fill contact person into selection of BPs that need to be read
    LOOP AT lt_data_entity_bp_rel ASSIGNING <ls_bp_entity_rel_data>
       WHERE usmd_entity = ZCL_MDG_BP_HELPER=>if_mdg_bp_constants~gc_bp_model_entity-relation
         AND usmd_entity_cont IS INITIAL.

      UNASSIGN: <lt_bp_rel_data>, <ls_bp_rel_data>, <lv_partner2>.
      CLEAR ls_bp_selection-low.
      ASSIGN <ls_bp_entity_rel_data>-r_t_data->* TO <lt_bp_rel_data>.
      LOOP AT <lt_bp_rel_data> ASSIGNING <ls_bp_rel_data>. "#EC CI_NESTED
        ASSIGN COMPONENT ZCL_MDG_BP_HELPER=>if_mdg_bp_constants~gc_field-partner2 OF STRUCTURE <ls_bp_rel_data> TO <lv_partner2>.
        IF <lv_partner2> IS ASSIGNED AND <lv_partner2> IS NOT INITIAL.
          ls_bp_selection-low = <lv_partner2>.
          INSERT ls_bp_selection INTO TABLE lt_bp_selection.
        ENDIF.
      ENDLOOP.
    ENDLOOP.

    IF lt_bp_selection IS NOT INITIAL.
* Look for entity in active data, if an existent business partner is changed (business activity = BPP2)
* This call triggers the derivations BAdI
      CALL METHOD go_model->read_entity_data_all
        EXPORTING
          i_fieldname    = ZCL_MDG_BP_HELPER=>if_mdg_bp_constants~gc_field-bp_header
          it_sel         = lt_bp_selection
          if_active      = lv_active
        IMPORTING
          et_message     = lt_message
          et_data_entity = lt_data_entity_bp.

      IF lt_message IS NOT INITIAL.
        RETURN.
      ENDIF.
    ENDIF.

* Get all address numbers
    LOOP AT lt_data_entity_bp ASSIGNING <ls_data_entity> WHERE usmd_entity_cont EQ ZCL_MDG_BP_HELPER=>if_mdg_bp_constants~gc_bp_model_entity-address. "#EC CI_SORTSEQ
      CLEAR ls_ad_selection.
      ls_ad_selection-sign   = usmd0_cs_ra-sign_i.
      ls_ad_selection-option = usmd0_cs_ra-option_eq.
      ls_ad_selection-fieldname = ZCL_MDG_BP_HELPER=>if_mdg_bp_constants~gc_bp_model_entity-address_number.

      ASSIGN <ls_data_entity>-r_t_data->* TO <lt_data>.
      CHECK sy-subrc IS INITIAL.
      LOOP AT <lt_data> ASSIGNING <ls_data>. "#EC CI_NESTED
        ASSIGN COMPONENT if_mdg_bp_constants~gc_bp_model_entity-address_number OF STRUCTURE <ls_data> TO <lv_addrno>.
        CHECK sy-subrc IS INITIAL.
        ls_ad_selection-low = <lv_addrno>.
        INSERT ls_ad_selection INTO TABLE lt_ad_selection.
      ENDLOOP.
    ENDLOOP.

    IF lt_ad_selection IS NOT INITIAL.
      CALL METHOD go_model->read_entity_data_all
        EXPORTING
          i_fieldname    = 'ADDRNO'
          it_sel         = lt_ad_selection
          if_active      = lv_active
        IMPORTING
          et_message     = lt_message
          et_data_entity = lt_data_entity_bp_ad.

      IF lt_message IS NOT INITIAL.
        RETURN.
      ENDIF.
    ENDIF.

    INSERT LINES OF lt_data_entity_bp     INTO TABLE lt_data_entity_all.
    INSERT LINES OF lt_data_entity_bp_rel INTO TABLE lt_data_entity_all.
    INSERT LINES OF lt_data_entity_bp_ad  INTO TABLE lt_data_entity_all.

* Transform untyped to typed data
    LOOP AT lt_data_entity_all ASSIGNING <ls_data_entity>.
      CLEAR: lv_entity_tabname, lr_entity.
      UNASSIGN: <ls_entity>, <lt_mt_entity>.
* Construct export table name and assign it to field symbol (it's used to fill the related mt)
      CASE <ls_data_entity>-struct.
        WHEN if_usmd_model_ext=>gc_struct_key_attr.
          IF <ls_data_entity>-usmd_entity_cont IS INITIAL.
            CONCATENATE lc_prefix <ls_data_entity>-usmd_entity INTO lv_entity_tabname.
          ELSE.
            CONCATENATE lc_prefix <ls_data_entity>-usmd_entity_cont INTO lv_entity_tabname.
          ENDIF.
        WHEN if_usmd_model_ext=>gc_struct_key_txt_langu.
          IF <ls_data_entity>-usmd_entity_cont IS INITIAL.
            CONCATENATE lc_prefix <ls_data_entity>-usmd_entity lc_suffix_text INTO lv_entity_tabname.
          ELSE.
            CONCATENATE lc_prefix <ls_data_entity>-usmd_entity_cont lc_suffix_text INTO lv_entity_tabname.
          ENDIF.
      ENDCASE.

* write data to gt
      ASSIGN (lv_entity_tabname) TO <lt_mt_entity>.       "#EC CI_SUBRC
      IF <lt_mt_entity> IS NOT ASSIGNED.
        MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 000.
      ENDIF.

      CREATE DATA lr_entity LIKE LINE OF <lt_mt_entity>.
      ASSIGN lr_entity->* TO <ls_entity>.
      IF <ls_entity> IS NOT ASSIGNED.
        MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 000.
      ENDIF.

      CLEAR: <ls_entity>, <lt_mt_entity>.

      ASSIGN <ls_data_entity>-r_t_data->* TO <lt_data>.
      IF sy-subrc <> 0.
        MESSAGE ID zcl_mdg_general_functions=>gc_msg_class_dm_gen TYPE 'X' NUMBER 000.
      ENDIF.

      IF <lt_data> IS ASSIGNED.
        MOVE-CORRESPONDING <lt_data> TO <lt_mt_entity>.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.
ENDCLASS.