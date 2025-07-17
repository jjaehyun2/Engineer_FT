class ZCL_MD_MDGMM_UTILITIES definition
  public
  final
  create public .

public section.

  types:
    BEGIN OF ty_s_plant_data,
        lv_werks TYPE werks_d,
        lv_beskz TYPE beskz,
      END   OF ty_s_plant_data .
  types:
    ty_t_plant_data TYPE STANDARD TABLE OF ty_s_plant_data .

  class-methods GET_APP_CONTEXT
    exporting
      !EV_CREQUEST_TYPE type USMD_CREQUEST_TYPE
      !EV_CREQUEST_STEP type USMD_CREQUEST_WFS
      !EV_CREQUEST_ID type USMD_CREQUEST .
  class-methods READ_MTART
    importing
      !IV_CREQUEST type USMD_CREQUEST
    exporting
      !ET_MESSAGE type USMD_T_MESSAGE
      !EV_MTART type MTART .
  class-methods PROCESS_MM_BUSINESS_RULES
    importing
      !IV_ENTITY type USMD_ENTITY optional
      !IO_MODEL type ref to IF_USMD_MODEL_EXT optional
      !IO_CHANGED_DATA type ref to IF_USMD_DELTA_BUFFER_READ optional
      !IO_WRITE_DATA type ref to IF_USMD_DELTA_BUFFER_WRITE optional
      !IT_DATA type ANY TABLE optional
      !IV_FIELD_PROP_BR type CHAR20 optional
      !IV_VALIDATION_BR type CHAR20 optional
      !IV_DERIVATION_BR type CHAR20 optional
      !IV_DEFAULTING_BR type CHAR20 optional
    exporting
      !ET_MESSAGE type USMD_T_MESSAGE
      !ET_MM_DETAILS type USMD_TS_DATA_ENTITY
      !EV_BOOL type BOOL
    changing
      !CT_FLD_PROP type ANY TABLE optional .
  class-methods GET_MM_BUSINESS_RULES
    importing
      !IV_CREQUEST type USMD_CREQUEST optional
      !IV_CREQUEST_TYPE type USMD_CREQUEST_TYPE optional
      !IV_ENTITY type USMD_ENTITY optional
      !IV_CREQUEST_WFS type USMD_CREQUEST_WFS optional
      !IV_MTART type MTART optional
      !IV_BESKZ type BESKZ optional
      !IV_WERKS type WERKS_D optional
      !IT_WERKS type TY_T_PLANT_DATA optional
    exporting
      !ET_BUSINESS_RULE type ZMD_MDG_RESULT_TTY .
  class-methods READ_MATNR_FROM_CREQUEST
    importing
      !IV_CREQUEST type USMD_CREQUEST
    returning
      value(RV_MATNR) type MATNR .
  class-methods GET_WERKS_FROM_CR
    importing
      !IV_MATNR type MATNR
    exporting
      value(ER_WERKS) type DATA .
  class-methods READ_WERKS_FROM_CREQ
    importing
      !IV_CREQUEST type USMD_CREQUEST
    returning
      value(RV_WERKS) type WERKS_D .
  class-methods GET_CREQUEST_FROM_MATNR
    importing
      !IV_MATNR type MATNR
    exporting
      !EV_CREQUEST type USMD_CREQUEST .
protected section.
private section.
ENDCLASS.



CLASS ZCL_MD_MDGMM_UTILITIES IMPLEMENTATION.


  METHOD get_app_context.
*& LOCAL data declaration
    DATA: lo_cxt TYPE REF TO if_usmd_app_context.

    CALL METHOD cl_usmd_app_context=>get_context
      RECEIVING
        eo_context = lo_cxt.

*&  Check if context is bound
    CHECK lo_cxt IS BOUND.

*&  Get Context Attributes
    CALL METHOD lo_cxt->get_attributes
      IMPORTING
        ev_crequest_type = ev_crequest_type
        ev_crequest_step = ev_crequest_step
        ev_crequest_id   = ev_crequest_id.
  ENDMETHOD.


  METHOD get_crequest_from_matnr.
    DATA lv_crequest_id TYPE usmd_crequest.

*--------------------------------------------------------------------*
* Material without Plant b
*--------------------------------------------------------------------*

    "Get Model Instance for Entity Key Structure
    cl_usmd_model=>get_instance( EXPORTING i_usmd_model = 'MM'
                                 IMPORTING eo_instance = DATA(lo_model)
                                           et_message = DATA(lt_model_message) ) ##NEEDED.
    "Set Entity MATERIAL Key Structure
    DATA(lr_s_material_key) = lo_model->create_data_reference( i_fieldname  = 'MATERIAL'
                                                                i_struct     = 'KEY'
                                                                if_table     = abap_false ).
    ASSIGN lr_s_material_key->* TO FIELD-SYMBOL(<ls_material_key>).
    "Set Material Number
    FIELD-SYMBOLS <lv_attribute> TYPE any.
    ASSIGN COMPONENT 'MATERIAL' OF STRUCTURE <ls_material_key> TO <lv_attribute>.
    <lv_attribute> = iv_matnr.
    "Get Change Request Service Provider
    DATA(lo_cr_service_provider) = cl_usmd_cr_factory=>get_cr_service_provider( ).
    "Retrieve CR by Entity Key
    DATA(lt_crequest) = lo_cr_service_provider->if_usmd_cr_sp_query~retrieve_cr_by_entity_key( iv_entity_type = 'MATERIAL'
                                                                                               is_entity_key  = <ls_material_key>
                                                                                               iv_model       = 'MM' ).
    "Set Change Requests for each Plant
    LOOP AT lt_crequest INTO DATA(ls_crequest).
      lv_crequest_id = ls_crequest-usmd_crequest.
      SELECT SINGLE * FROM usmd120c INTO @DATA(ls_usmd120c) WHERE usmd_crequest EQ @lv_crequest_id. "#EC CI_ALL_FIELDS_NEEDED
      IF sy-subrc EQ 0.
*        APPEND INITIAL LINE TO et_crequest_by_matnr ASSIGNING FIELD-SYMBOL(<ls_crequest_by_matnr>).
*        MOVE-CORRESPONDING ls_usmd120c TO <ls_crequest_by_matnr>.
      ENDIF.
    ENDLOOP.
******************************************************************
    CLEAR: lo_model, lt_model_message.

    "Get Plant Data for Material
*    IF iv_werks IS INITIAL.<
      SELECT matnr, werks INTO TABLE @DATA(lt_marc) FROM marc WHERE matnr EQ @iv_matnr. "#EC CI_SEL_NESTED
                                                          "#EC CI_SUBRC
*    ELSE.
*      SELECT matnr werks INTO TABLE lt_marc FROM marc WHERE matnr EQ iv_matnr AND werks EQ iv_werks. "#EC CI_SEL_NESTED
*                                                          "#EC CI_SUBRC
*    ENDIF.
    LOOP AT lt_marc INTO DATA(ls_marc).

      CLEAR: lo_cr_service_provider, lt_crequest.

      "Get Model Instance for Entity Key Structure
      cl_usmd_model=>get_instance( EXPORTING i_usmd_model = 'MM'
                                   IMPORTING eo_instance  = lo_model
                                             et_message   = lt_model_message ).
      "Set Entity MARCBASIC Key Structure
      DATA(lr_s_marcbasic_key) = lo_model->create_data_reference( i_fieldname  = 'MARCBASIC'
                                                                  i_struct     = 'KEY'
                                                                  if_table     = abap_false ).
      ASSIGN lr_s_marcbasic_key->* TO FIELD-SYMBOL(<ls_marcbasic_key>).
      "Set Material Number
      ASSIGN COMPONENT 'MATERIAL' OF STRUCTURE <ls_marcbasic_key> TO <lv_attribute>.
      <lv_attribute> = ls_marc-matnr.
      "Set Plant Number
      ASSIGN COMPONENT 'WERKS' OF STRUCTURE <ls_marcbasic_key> TO <lv_attribute>.
      <lv_attribute> = ls_marc-werks.
      "Get Change Request Service Provider
      lo_cr_service_provider = cl_usmd_cr_factory=>get_cr_service_provider( ).
      "Retrieve CR by Entity Key
      lt_crequest = lo_cr_service_provider->if_usmd_cr_sp_query~retrieve_cr_by_entity_key( iv_entity_type = 'MARCBASIC'
                                                                                           is_entity_key  = <ls_marcbasic_key>
                                                                                           iv_model       = 'MM' ).
      "Set Change Requests for each Plant
      LOOP AT lt_crequest INTO ls_crequest.              "#EC CI_NESTED
        lv_crequest_id = ls_crequest-usmd_crequest.
        SELECT SINGLE * FROM usmd120c INTO ls_usmd120c WHERE usmd_crequest EQ lv_crequest_id. "#EC CI_ALL_FIELDS_NEEDED
        IF sy-subrc EQ 0.
*          APPEND INITIAL LINE TO et_crequest_by_matnr ASSIGNING <ls_crequest_by_matnr>.
*          <ls_crequest_by_matnr>-plant = ls_marc-werks.
*          MOVE-CORRESPONDING ls_usmd120c TO <ls_crequest_by_matnr>.
        ENDIF.
      ENDLOOP.

    ENDLOOP.

  ENDMETHOD.


  METHOD get_mm_business_rules.


  ENDMETHOD.


  METHOD GET_WERKS_FROM_CR.
    DATA:
      lr_model TYPE REF TO if_usmd_model_ext,
      lt_sel   TYPE usmd_ts_sel,
      ls_sel   TYPE usmd_s_sel,
      lr_data  TYPE REF TO data.

    FIELD-SYMBOLS:
      <lt_data_s>   TYPE SORTED TABLE,
      <lt_tax_data> TYPE STANDARD TABLE.

*   Get change request id
    get_app_context( IMPORTING ev_crequest_id = data(lv_crequest) ).

*   Get read-only access to USMD model data
    CALL METHOD cl_usmd_model_ext=>get_instance
      EXPORTING
        i_usmd_model = 'MM'
      IMPORTING
        eo_instance  = lr_model.


    CALL METHOD lr_model->create_data_reference
      EXPORTING
        i_fieldname = 'MARCBASIC'
        i_struct    = lr_model->gc_struct_key_attr
        if_table    = abap_true
        i_tabtype   = lr_model->gc_tabtype_sorted
      IMPORTING
        er_data     = lr_data.

    ASSIGN lr_data->* TO <lt_data_s>.

    CLEAR lt_sel.
    ls_sel-fieldname = 'MATERIAL'.
    ls_sel-sign   = 'I'.
    ls_sel-option = 'EQ'.
    ls_sel-low    = iv_matnr.
    INSERT ls_sel INTO TABLE lt_sel.
    ls_sel-fieldname = usmd0_cs_fld-crequest.
    ls_sel-low       = lv_crequest.
    INSERT ls_sel INTO TABLE lt_sel.

    CALL METHOD lr_model->read_char_value
      EXPORTING
        i_fieldname       = 'MARCBASIC'
        it_sel            = lt_sel
        i_readmode        = if_usmd_model_ext=>gc_readmode_default
        if_use_edtn_slice = abap_false
      IMPORTING
        et_data           = <lt_data_s>.

*   Return the one and only result
    READ TABLE <lt_data_s> TRANSPORTING NO FIELDS INDEX 1.
    CHECK sy-subrc EQ 0.

    CREATE DATA er_werks TYPE STANDARD TABLE OF /MDGMM/_S_MM_PP_MARCBASIC.
    ASSIGN er_werks->* TO <lt_tax_data>.
    MOVE-CORRESPONDING <lt_data_s> TO <lt_tax_data>.

  ENDMETHOD.


  METHOD process_mm_business_rules.

    DATA :
      lv_mtart         TYPE mtart,
      lv_matnr         TYPE matnr,
      lv_crequest_type TYPE usmd_crequest_type,
      lv_crequest_wfs  TYPE usmd_crequest_wfs,
      lv_crequest_id   TYPE usmd_crequest.

    FIELD-SYMBOLS:
      <ls_business_rule> TYPE zmm_st_br_result.


*   Gets App Context Values
    CALL METHOD zcl_md_mdgmm_utilities=>get_app_context
      IMPORTING
        ev_crequest_type = lv_crequest_type
        ev_crequest_step = lv_crequest_wfs
        ev_crequest_id   = lv_crequest_id.

    CALL METHOD zcl_md_mdgmm_utilities=>read_matnr_from_crequest
      EXPORTING
        iv_crequest = lv_crequest_id                 " Change Request
      RECEIVING
        rv_matnr    = lv_matnr.                " Material Number


    CALL METHOD zcl_md_mdgmm_utilities=>read_mtart
      EXPORTING
        iv_crequest = lv_crequest_id   " Change Request
      IMPORTING
        ev_mtart    = lv_mtart.        " Material type


*   Gets Business Rules from BRF+ Application only if Rules are active
    zcl_mdgx_utilities=>get_mm_busisness_rule(
            EXPORTING
              mtart              =   lv_mtart               " Material type
              usmd_crequest_type =   lv_crequest_type               " Type of Change Request
              usmd_crequest_wfs  =   lv_crequest_wfs               " Change Request Step
            IMPORTING
              et_br_result       =   DATA(lt_br_result)               " Material Business Rules
          ).

    LOOP AT lt_br_result ASSIGNING <ls_business_rule>.

      CASE <ls_business_rule>-br_type.
        WHEN 'D'.
*           Process Derivation Rules
          IF iv_derivation_br EQ 'D'.
            CALL METHOD zcl_md_mdg_mm_gnrl_derivations=>(<ls_business_rule>-method_name)
              EXPORTING
                io_changed_data = io_changed_data    " Read-Interface to Data Buffer
                io_write_data   = io_write_data     " Write Interface to Data Buffer
                it_data_entity  = et_mm_details     " Data for Entity Types
                io_model        = io_model        " MDG Data Model for Access from Non-SAP Standard Code
              IMPORTING
                et_message_info = et_message.

          ENDIF.


        WHEN 'V'.
*         Process Validation Rules
          IF iv_validation_br EQ 'V'.
            CALL METHOD zcl_md_mdg_mm_gnrl_validations=>(<ls_business_rule>-method_name)
              EXPORTING
                io_changed_data = io_changed_data    " Read-Interface to Data Buffer
                io_write_data   = io_write_data     " Write Interface to Data Buffer
                it_data_entity  = et_mm_details    " Data for Entity Types
                io_model        = io_model        " MDG Data Model for Access from Non-SAP Standard Code
                iv_crequest     = lv_crequest_id     " Change Request
                iv_matnr        = lv_matnr
              IMPORTING
                et_message      = et_message.
          ENDIF.

      ENDCASE.
    ENDLOOP.
  ENDMETHOD.


  METHOD read_matnr_from_crequest.
    "Get Model Instance
    cl_usmd_model_ext=>get_instance( EXPORTING i_usmd_model = 'MM'
                                     IMPORTING eo_instance  = DATA(lo_model) ).

    IF lo_model IS BOUND.
      "Get Model Object List
      lo_model->if_usmd_model_cr_ext~get_cr_objectlist( EXPORTING i_crequest = iv_crequest
                                                        IMPORTING et_key_all = DATA(lt_key_all) ).
      "Get MATERIAL Entity Keys
      READ TABLE lt_key_all ASSIGNING FIELD-SYMBOL(<ls_key_all>) WITH KEY entity = 'MATERIAL'.
      IF <ls_key_all> IS ASSIGNED.
        FIELD-SYMBOLS <lt_data> TYPE ANY TABLE.
        ASSIGN <ls_key_all>-r_data->* TO <lt_data>.
        IF <lt_data> IS ASSIGNED.
          LOOP AT <lt_data> ASSIGNING FIELD-SYMBOL(<ls_data>).
            rv_matnr = <ls_data>.
            EXIT.
          ENDLOOP.
        ENDIF.
      ENDIF.
    ENDIF.

  ENDMETHOD.


  METHOD read_mtart.
    DATA:
      lo_model         TYPE REF TO if_usmd_model_ext,
      lv_entity        TYPE usmd_entity,
      lt_entity_filter TYPE usmd_t_entity.

    FIELD-SYMBOLS:
      <lt_data_ent> TYPE ANY TABLE.


* Get the model instance
    CALL METHOD cl_usmd_model_ext=>get_instance
      EXPORTING
        i_usmd_model = if_mdg_bs_mat_gen_c=>gc_model_mm
      IMPORTING
        eo_instance  = lo_model
        et_message   = et_message.
* Check whether local object is not initial
    CHECK lo_model IS NOT INITIAL.

* We want the material type from entity MATERIAL.
    lv_entity = if_mdg_bs_mat_gen_c=>gc_entity_material.
    INSERT lv_entity INTO TABLE lt_entity_filter.
* Read the data for the chosen entity type
    CALL METHOD lo_model->read_entity_data_all
      EXPORTING
        i_fieldname      = if_mdg_bs_mat_gen_c=>gc_fieldname_material
        if_active        = abap_false
        i_crequest       = iv_crequest
*       it_sel           =
        it_entity_filter = lt_entity_filter
      IMPORTING
        et_message       = et_message
        et_data_entity   = DATA(lt_data_entity).

* Now dereferenciate and return with the CR material type value
    READ TABLE lt_data_entity INTO DATA(ls_data_entity) WITH KEY usmd_entity = if_mdg_bs_mat_gen_c=>gc_entity_material.
    IF sy-subrc EQ 0.
      ASSIGN ls_data_entity-r_t_data->*  TO <lt_data_ent>.
      IF sy-subrc EQ 0 AND <lt_data_ent> IS ASSIGNED.
        LOOP AT <lt_data_ent> ASSIGNING FIELD-SYMBOL(<ls_data_ent>).
          ASSIGN COMPONENT if_mdg_bs_mat_gen_c=>gc_attr_mtart OF STRUCTURE <ls_data_ent> TO FIELD-SYMBOL(<lv_mtart>).
          IF sy-subrc EQ 0 AND <lv_mtart> IS ASSIGNED.
            ev_mtart = <lv_mtart>.
          ENDIF.
        ENDLOOP.
      ENDIF.
    ENDIF.
  ENDMETHOD.


  METHOD read_werks_from_creq.
    "Get Model Instance
    cl_usmd_model_ext=>get_instance( EXPORTING i_usmd_model = 'MM'
                                     IMPORTING eo_instance  = DATA(lo_model) ).

    IF lo_model IS BOUND.
      "Get Model Object List
      lo_model->if_usmd_model_cr_ext~get_cr_objectlist( EXPORTING i_crequest = iv_crequest
                                                        IMPORTING et_key_all = DATA(lt_key_all) ).
      "Get MARCBASİC Entity Keys
      READ TABLE lt_key_all ASSIGNING FIELD-SYMBOL(<ls_key_all>) WITH KEY entity = 'MARCBASIC'.
      IF <ls_key_all> IS ASSIGNED.
        FIELD-SYMBOLS <lt_data> TYPE ANY TABLE.
        ASSIGN <ls_key_all>-r_data->* TO <lt_data>.
        IF <lt_data> IS ASSIGNED.
          LOOP AT <lt_data> ASSIGNING FIELD-SYMBOL(<ls_data>).
            rv_WERKS = <ls_data>.
            EXIT.
          ENDLOOP.
        ENDIF.
      ENDIF.
    ENDIF.

  ENDMETHOD.
ENDCLASS.