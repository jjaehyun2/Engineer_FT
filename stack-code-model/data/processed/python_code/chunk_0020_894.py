class ZCL_MDG_GENERAL_FUNCTIONS definition
  public
  final
  create public .

public section.

  constants GC_MSG_CLASS_DM_GEN type SYMSGID value 'Z_MDG_DM_MSG' ##NO_TEXT.
  constants GC_MSG_CLASS_DM_MM type SYMSGID value 'Z_MDG_MM_DM_MSG' ##NO_TEXT.
  constants GC_MSG_CLASS_DM_BP type SYMSGID value 'Z_MDG_BP_DM_MSG' ##NO_TEXT.
  constants GC_MSG_CLASS_UI_BP type SYMSGID value 'Z_MDG_BP_UI_MSG' ##NO_TEXT.
  constants GC_MSG_CLASS_UI_MM type SYMSGID value 'Z_MDG_BP_MM_MSG' ##NO_TEXT.
  constants GC_MSG_CLASS_BR_BP type SYMSGID value 'Z_MDG_BP_BR_MSG' ##NO_TEXT.
  constants GC_MSG_CLASS_BR_MM type SYMSGID value 'Z_MDG_MM_BR_MSG' ##NO_TEXT.
  constants GC_MSG_CLASS_WF_BP type SYMSGID value 'Z_MDG_BP_WF_MSG' ##NO_TEXT.
  constants GC_MSG_CLASS_WF_MM type SYMSGID value 'Z_MDG_MM_WF_MSG' ##NO_TEXT.
  constants GC_MSG_CLASS_IF_BP type SYMSGID value 'Z_MDG_BP_IF_MSG' ##NO_TEXT.
  constants GC_MSG_CLASS_IF_MM type SYMSGID value 'Z_MDG_MM_IF_MSG' ##NO_TEXT.
  constants GC_MSG_CLASS_MIG_BP type SYMSGID value 'Z_MDG_BP_MIG_MSG' ##NO_TEXT.
  constants GC_MSG_CLASS_MIG_MM type SYMSGID value 'Z_MDG_MM_MIG_MSG' ##NO_TEXT.
  constants GC_WILDCARD type CHAR1 value '$' ##NO_TEXT.
  constants GC_RULE_TYPE_LIMITATION type ZMDG_DE_MM_BR_TYPE value 'L' ##NO_TEXT.
  constants GC_RULE_TYPE_VALIDATION type ZMDG_DE_MM_BR_TYPE value 'V' ##NO_TEXT.
  constants GC_RULE_TYPE_DERIVATION type ZMDG_DE_MM_BR_TYPE value 'D' ##NO_TEXT.
  constants GC_RULE_TYPE_EPROP type ZMDG_DE_MM_BR_TYPE value 'E' ##NO_TEXT.
  constants GC_RULE_TYPE_FPROP type ZMDG_DE_MM_BR_TYPE value 'F' ##NO_TEXT.
  constants:
    BEGIN OF cs_rule_type,
        der     TYPE char3 VALUE 'DER',
        val     TYPE char3 VALUE 'VAL',
        ui_rule TYPE char3 VALUE 'UIR',
        ui_con  TYPE char3 VALUE 'UIC',
        lim     TYPE char3 VALUE 'LIM',
      END OF  cs_rule_type .
  class-data GV_ERROR_MESSAGE type STRING .

  class-methods GET_MESSAGE
    importing
      !IO_MODEL type ref to IF_USMD_MODEL_EXT optional
      !IS_DATA type ANY optional
      !IV_ENTITY type USMD_ENTITY optional
      !IV_FIELDNAME type USMD_FIELDNAME optional
      !IV_MSGTY type SYMSGTY
      !IV_MSGNO type SYMSGNO
      !IV_MSGV1 type ANY optional
      !IV_MSGV2 type ANY optional
      !IV_MSGV3 type ANY optional
      !IV_MSGV4 type ANY optional
      !IV_SYMSGID type SYMSGID
    exporting
      !ES_MESSAGE type USMD_S_MESSAGE .
  class-methods GET_MESSAGE_ROW
    importing
      !IV_MODEL type USMD_MODEL
      !IS_KEY type DATA
      !IV_ENTITY type USMD_ENTITY
      !IV_FIELDNAME type USMD_FLD_SOURCE
    returning
      value(RV_ROW) type MDG_MESSAGE_ROW .
  class-methods NEGATE_BOOL
    importing
      !IV_BOOL type XFELD
    returning
      value(RV_BOOL) type XFELD .
  class-methods GET_DESCRIPTION_FROM_ATTRIBUTE
    importing
      !IV_ATTRIBUTE type USMD_ATTRIBUTE
      !IO_MODEL type ref to IF_USMD_MODEL_EXT
    returning
      value(RV_DESCR) type SCRTEXT_M .
  class-methods GET_DESCRIPTION_FROM_ENTITY
    importing
      !IV_ENTITY type USMD_ENTITY
      !IO_MODEL type ref to IF_USMD_MODEL_EXT
    returning
      value(RV_DESCR) type SCRTEXT_M .
protected section.
private section.
ENDCLASS.



CLASS ZCL_MDG_GENERAL_FUNCTIONS IMPLEMENTATION.


METHOD get_description_from_attribute.

    DATA:
          lr_prop_attr TYPE REF TO usmd_s_fprop_ext.

    IF io_model IS NOT BOUND.
      RETURN.
    ENDIF.

    READ TABLE io_model->if_usmd_model_metadata_ext~dt_fprop WITH TABLE KEY fieldname = iv_attribute REFERENCE INTO lr_prop_attr.
    IF sy-subrc EQ 0.
      rv_descr = lr_prop_attr->scrtext_m.
    ENDIF.

  ENDMETHOD.


METHOD get_description_from_entity.

    DATA:
      lr_prop_entity TYPE REF TO usmd_s_fprop_ext.

    IF io_model IS NOT BOUND.
      RETURN.
    ENDIF.

    READ TABLE io_model->if_usmd_model_metadata_ext~dt_fprop WITH TABLE KEY fieldname = iv_entity REFERENCE INTO lr_prop_entity.
    IF sy-subrc EQ 0.
      rv_descr = lr_prop_entity->scrtext_m.
    ENDIF.

  ENDMETHOD.


METHOD get_message.

    DATA:
      ls_ui_message TYPE usmd_s_message,
      lr_key        TYPE REF TO data,
      lo_strucdesc  TYPE REF TO cl_abap_structdescr,
      lt_components TYPE abap_component_tab,
      ls_components TYPE LINE OF abap_component_tab,
      lv_fieldname  TYPE usmd_fieldname.

    FIELD-SYMBOLS:
      <ls_key>    TYPE any,
      <lv_source> TYPE any,
      <lv_dest>   TYPE any.

* populate message components in UI message forMM
    ls_ui_message-msgid = iv_symsgid.
    ls_ui_message-msgty = iv_msgty.
    ls_ui_message-msgno = iv_msgno.
    IF iv_msgv1 IS NOT INITIAL.
      ls_ui_message-msgv1 = iv_msgv1.
    ENDIF.
    IF iv_msgv2 IS NOT INITIAL.
      ls_ui_message-msgv2 = iv_msgv2.
    ENDIF.
    IF iv_msgv3 IS NOT INITIAL.
      ls_ui_message-msgv3 = iv_msgv3.
    ENDIF.
    IF iv_msgv4 IS NOT INITIAL.
      ls_ui_message-msgv4 = iv_msgv4.
    ENDIF.

    IF iv_entity IS NOT INITIAL AND iv_fieldname IS NOT INITIAL.
      CONCATENATE iv_entity '-' iv_fieldname INTO ls_ui_message-fieldname.
    ENDIF.

* if called from validations enhance with message navigation
    IF      io_model     IS SUPPLIED
        AND iv_entity    IS SUPPLIED
        AND iv_fieldname IS SUPPLIED
        AND is_data      IS SUPPLIED
        AND io_model->d_usmd_model NE if_mdg_bs_mat_gen_c=>gc_model_mm.

      lv_fieldname = iv_entity.
      CALL METHOD io_model->create_data_reference
        EXPORTING
          i_fieldname = lv_fieldname
          i_struct    = if_usmd_model_ext=>gc_struct_key
          if_table    = abap_false
        IMPORTING
          er_data     = lr_key.

      ASSIGN lr_key->* TO <ls_key>.
      IF sy-subrc IS NOT INITIAL.
        RETURN.
      ENDIF.

      lo_strucdesc ?= cl_abap_structdescr=>describe_by_data( p_data = <ls_key> ).
      lt_components = lo_strucdesc->get_components( ).
      LOOP AT lt_components INTO ls_components.
        ASSIGN COMPONENT ls_components-name OF STRUCTURE <ls_key> TO <lv_dest>.
        IF sy-subrc <> 0.
          RETURN.
        ENDIF.

        ASSIGN COMPONENT ls_components-name OF STRUCTURE is_data TO <lv_source>.
        IF sy-subrc <> 0.
          RETURN.
        ENDIF.
        <lv_dest> = <lv_source>.
      ENDLOOP.

      ls_ui_message-row = cl_mdg_bs_key_row_map_service=>set_key(
        is_key       = lr_key
        iv_entity    = iv_entity
        iv_fieldname = iv_fieldname ).

    ENDIF.

    es_message = ls_ui_message.

  ENDMETHOD.


METHOD get_message_row.

    DATA:
      lo_model     TYPE REF TO if_usmd_model_ext,
      lv_fieldname TYPE usmd_fieldname,
      lr_key_struc TYPE REF TO data.

    FIELD-SYMBOLS:
      <ls_key> TYPE any.

    CLEAR rv_row.

    CHECK: is_key IS NOT INITIAL,
           iv_entity IS NOT INITIAL,
           iv_fieldname IS NOT INITIAL.

    cl_usmd_model_ext=>get_instance(
      EXPORTING
        i_usmd_model = iv_model                 " Data model
      IMPORTING
        eo_instance  = lo_model                 " MDM Data Model for Access from Non-SAP Standard
    ).

    CHECK lo_model IS NOT INITIAL.


    lv_fieldname = iv_entity.
    lo_model->create_data_reference(
      EXPORTING
        i_fieldname          = lv_fieldname                  " Field Name
        i_struct             = lo_model->gc_struct_key     " Structure
        if_table             = abap_false
      IMPORTING
        er_data              = lr_key_struc
    ).

    ASSIGN lr_key_struc->* TO <ls_key>.

    MOVE-CORRESPONDING is_key TO <ls_key>.

    cl_mdg_bs_key_row_map_service=>set_key(
      EXPORTING
        is_key       = lr_key_struc                 " Reference to key
        iv_entity    = iv_entity                 " Entity Type
        iv_fieldname = iv_fieldname                 " Source Field
      RECEIVING
        rv_row       = rv_row                 " MDG message navigation: row referencing a key
    ).
  ENDMETHOD.


METHOD negate_bool.

    IF iv_bool = abap_true.
      rv_bool = abap_false.
    ELSEIF iv_bool = abap_false.
      rv_bool = abap_true.
    ELSE.
      "something went wrong
      ASSERT 1 = 0.
    ENDIF.

  ENDMETHOD.
ENDCLASS.