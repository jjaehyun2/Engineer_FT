class ZCL_MD_MDGBP_UTILITIES definition
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
  class-methods PROCESS_BP_BUSINESS_RULES
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
      !ET_BP_DETAILS type USMD_TS_DATA_ENTITY
      !EV_BOOL type BOOL
    changing
      !CT_FLD_PROP type ANY TABLE optional .
  class-methods READ_BP_FROM_CREQUEST
    importing
      !IV_CREQUEST type USMD_CREQUEST
    returning
      value(RV_BP_PARTNER) type BU_BUSINESSPARTNER .
  class-methods READ_TAX_FROM_CREQUEST
    importing
      !IV_CREQUEST type USMD_CREQUEST
    returning
      value(RV_BP_TAXNUM) type STRING .
  class-methods READ_BP_ROLE
    importing
      !IV_CREQUEST type USMD_CREQUEST
    returning
      value(RT_BP_ROLES) type TRTY_ROLETYP .
  class-methods READ_BP_ROLES
    returning
      value(RT_BP_ROLES) type TRTY_ROLETYP .
protected section.
private section.
ENDCLASS.



CLASS ZCL_MD_MDGBP_UTILITIES IMPLEMENTATION.


  METHOD GET_APP_CONTEXT.
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


  METHOD process_bp_business_rules.

    DATA :
      lv_bp_header     TYPE bu_businesspartner,
      lv_crequest_type TYPE usmd_crequest_type,
      lv_crequest_wfs  TYPE usmd_crequest_wfs,
      lv_crequest_id   TYPE usmd_crequest.

    FIELD-SYMBOLS:
      <ls_business_rule> TYPE zmm_st_br_result.

*   Gets App Context Values
    CALL METHOD zcl_md_mdgbp_utilities=>get_app_context
      IMPORTING
        ev_crequest_type = lv_crequest_type
        ev_crequest_step = lv_crequest_wfs
        ev_crequest_id   = lv_crequest_id.

    CALL METHOD zcl_md_mdgbp_utilities=>read_bp_from_crequest
      EXPORTING
        iv_crequest   = lv_crequest_id                 " Change Request
      RECEIVING
        rv_bp_partner = lv_bp_header.                " BP_HEADER

*   Gets Business Rules from BRF+ Application only if Rules are active
    zcl_mdgx_utilities=>get_bp_busisness_rule(
            EXPORTING
              usmd_crequest_type =   lv_crequest_type               " Type of Change Request
              usmd_crequest_wfs  =   lv_crequest_wfs                " Change Request Step
            IMPORTING
              et_br_result       =   DATA(lt_br_result)               " BP Business Rules
          ).

    LOOP AT lt_br_result ASSIGNING <ls_business_rule>.

      CASE <ls_business_rule>-br_type.
        WHEN 'D'.
*           Process Derivation Rules
          IF iv_derivation_br EQ 'D'.
            CALL METHOD zcl_md_mdg_bp_gnrl_derivations=>(<ls_business_rule>-method_name)
              EXPORTING
                io_changed_data = io_changed_data    " Read-Interface to Data Buffer
                io_write_data   = io_write_data      " Write Interface to Data Buffer
                it_data_entity  = et_bp_details      " Data for Entity Types
                io_model        = io_model           " MDG Data Model for Access from Non-SAP Standard Code
                iv_crequest     = lv_crequest_id     " Change Request
              IMPORTING
                et_message_info = et_message.
          ENDIF.


        WHEN 'V'.
*         Process Validation Rules
          IF iv_validation_br EQ 'V'.
            CALL METHOD zcl_md_mdg_bp_gnrl_validations=>(<ls_business_rule>-method_name)
              EXPORTING
                io_changed_data = io_changed_data    " Read-Interface to Data Buffer
                io_write_data   = io_write_data      " Write Interface to Data Buffer
                it_data_entity  = et_bp_details      " Data for Entity Types
                io_model        = io_model           " MDG Data Model for Access from Non-SAP Standard Code
                iv_crequest     = lv_crequest_id     " Change Request
                iv_bp_header    = lv_bp_header
              IMPORTING
                et_message      = et_message.
          ENDIF.

      ENDCASE.
    ENDLOOP.
  ENDMETHOD.


  METHOD read_bp_from_crequest.
    "Get Model Instance
    cl_usmd_model_ext=>get_instance( EXPORTING i_usmd_model = 'BP'
                                     IMPORTING eo_instance  = DATA(lo_model) ).

    IF lo_model IS BOUND.
      "Get Model Object List
      lo_model->if_usmd_model_cr_ext~get_cr_objectlist( EXPORTING i_crequest = iv_crequest
                                                        IMPORTING et_key_all = DATA(lt_key_all) ).
      "Get MATERIAL Entity Keys
      READ TABLE lt_key_all ASSIGNING FIELD-SYMBOL(<ls_key_all>) WITH KEY entity = 'BP_HEADER'.
      IF <ls_key_all> IS ASSIGNED.
        FIELD-SYMBOLS <lt_data> TYPE ANY TABLE.
        ASSIGN <ls_key_all>-r_data->* TO <lt_data>.
        IF <lt_data> IS ASSIGNED.
          LOOP AT <lt_data> ASSIGNING FIELD-SYMBOL(<ls_data>).

            rv_bp_partner = <ls_data>.
            EXIT.
          ENDLOOP.
        ENDIF.
      ENDIF.
    ENDIF.

  ENDMETHOD.


  method READ_BP_ROLE.

    DATA : lo_model     TYPE REF TO if_usmd_model_ext,
           lt_message   TYPE usmd_t_message,
           lt_entities  TYPE usmd_t_entity . "#EC NEEDED

    FIELD-SYMBOLS  :
      <lt_data_ent> TYPE ANY TABLE,
      <ls_data_ent> TYPE any,
      <ls_taxnr>    TYPE any.


    rt_bp_roles = read_bp_roles( ).

    cl_usmd_model_ext=>get_instance(
      EXPORTING
        i_usmd_model =  'BP'
      IMPORTING
        eo_instance  =    lo_model
        et_message   =    lt_message
    ).
    CHECK lo_model IS NOT INITIAL.


    lo_model->read_entity_data_all(
      EXPORTING
        i_fieldname      =   'BP_HEADER'
        if_active        =   abap_false
        i_crequest       =   iv_crequest
        it_entity_filter =   lt_entities
      IMPORTING
        et_message       =   lt_message
        et_data_entity   =   DATA(lt_data_entity)
    ).

    READ TABLE lt_data_entity INTO DATA(ls_data_entity) WITH KEY usmd_entity = 'BP_HEADER'
                                                                usmd_entity_cont = 'BP_TAXNUM' .

    IF sy-subrc EQ 0.

      ASSIGN ls_data_entity-r_t_data->* TO <lt_data_ent>.

      CHECK <lt_data_ent> IS ASSIGNED.

      LOOP AT <lt_data_ent> ASSIGNING <ls_data_ent>.

        ASSIGN COMPONENT 'TAXNUM' OF STRUCTURE <ls_data_ent> TO <ls_taxnr>.
        IF sy-subrc = 0.
          rt_bp_roles = <ls_taxnr>.
        ENDIF.

      ENDLOOP.

    ENDIF.
  endmethod.


  method READ_BP_ROLES.
*----------------------------------------------------------------------
* [Entwicklungstyp][Entwicklungsnummer]
* [ggf. Kurztext zur Entwicklungsnummer]
* [ggf. Hinweis auf den Programmverantwortlichen bei Porsche]
*----------------------------------------------------------------------
******************** !!!ACHTUNG BITTE BEACHTEN!!! *********************
* Die Veränderung oder Verwendung von Modularisierungseinheiten dieses
* Programms ist ohne Abstimmung mit bzw.
* wortliche Applikation Management nicht zulässig.
*----------------------------------------------------------------------
*----------------------------------------------------------------------
* Programmteile:
* [Bestandteile der Entwicklung]
*----------------------------------------------------------------------
* Beschreibung:
* [Fachliche Kurzbeschreibung, ggf. Referenz auf Anwenderdokumentation.]
* [Technische Kurzbeschreibung, ggf. Referenz auf Systemdokumentation.]
*----------------------------------------------------------------------*
* Legende Deklarationskonventionen:                                    *
* [Deklarationskonventionen]                                           *
*----------------------------------------------------------------------*
* IS-Konzept...: [Angaben zum Konzeptverantwortlichen]                 *
* IS-Betreuung.: Bernhard Brendel, FIF1
* FB-Betreuung.: Lara Schultheis, xxx
*----------------------------------------------------------------------*
*Entwickler...: X500606, Steffen Schwarz MHP
*----------------------------------------------------------------------*
*Änderungshistorie                                                     *
*Datum | Entwickler | Bemerkung                                        *
*======================================================================*
* JJJJMMDD | USERID | Anlage Entwicklungsobjekt
*----------------------------------------------------------------------*

*====================================================================*
* Todo: REFACTOR!!! Dont Use CR API
*====================================================================*
    data: lt_entity type usmd_t_crequest_entity,
          lt_sel    type usmd_ts_sel,
          lt_result type table of /mdgbp/_s_bp_pp_bp_role,
          ls_sel    like line of lt_sel,
          l_bp_num  type bu_partner.

    data(lo_context) = cl_usmd_app_context=>get_context( ).
    check lo_context is bound.
    if lo_context->mv_crequest_id is not initial and lo_context->mv_crequest_id ne '000000000000'.

      call method zcl_mdga_bp_dm_usmd_model_ext=>get_instance
        exporting
          iv_usmd_crequest = lo_context->mv_crequest_id
        receiving
          ro_instance      = data(lo_model_ext_wrapper).

      call method lo_model_ext_wrapper->read_bu_partner_roles
        receiving
          rt_bu_partner_roles = rt_bp_roles.

    endif.

    " BWL Activity für LOG Aktion Display
    ">>>>>>>>>>>>>>> CHANGE 31.07.2020
    if lo_context->mv_process eq 'BPP3' or rt_bp_roles is initial.
      "<<<<<<<<<<<<<<<END CHANGE 31.07.2020
      data(lo_fpm) = cl_fpm_factory=>get_instance( ).

      check lo_fpm is bound.

      data(lo_app_parameter) = lo_fpm->mo_app_parameter.

      lo_app_parameter->get_value( exporting iv_key = 'BP_HEADER' importing ev_value = l_bp_num ).

      check l_bp_num is not initial.

      cl_usmd_model_ext=>get_instance( exporting i_usmd_model = 'BP' importing eo_instance = data(lo_model) ).

      ls_sel-fieldname = 'BP_HEADER'.
      ls_sel-sign      = 'I'.
      ls_sel-option    = 'EQ'.
      ls_sel-low       = l_bp_num.
      ls_sel-high      = ''.
      insert ls_sel into table lt_sel.

      call method lo_model->read_char_value
        exporting
          i_fieldname = 'BP_ROLE'
          it_sel      = lt_sel
          i_readmode  = if_usmd_model_ext=>gc_readmode_default
        importing
          et_data     = lt_result
*         et_message  =
        .

      loop at lt_result assigning field-symbol(<s_bp_role_model>).
        append <s_bp_role_model>-bp_rol_id to rt_bp_roles.
      endloop.

    endif.


  endmethod.


  METHOD read_tax_from_crequest.

    DATA : lo_model     TYPE REF TO if_usmd_model_ext,
           lt_message   TYPE usmd_t_message,
           lt_entities  TYPE usmd_t_entity . "#EC NEEDED

    FIELD-SYMBOLS  :
      <lt_data_ent> TYPE ANY TABLE,
      <ls_data_ent> TYPE any,
      <ls_taxnr>    TYPE any.



    cl_usmd_model_ext=>get_instance(
      EXPORTING
        i_usmd_model =  'BP'
      IMPORTING
        eo_instance  =    lo_model
        et_message   =    lt_message
    ).
    CHECK lo_model IS NOT INITIAL.


    lo_model->read_entity_data_all(
      EXPORTING
        i_fieldname      =   'BP_HEADER'
        if_active        =   abap_false
        i_crequest       =   iv_crequest
        it_entity_filter =   lt_entities
      IMPORTING
        et_message       =   lt_message
        et_data_entity   =   DATA(lt_data_entity)
    ).

    READ TABLE lt_data_entity INTO DATA(ls_data_entity) WITH KEY usmd_entity = 'BP_HEADER'
                                                                usmd_entity_cont = 'BP_TAXNUM' .

    IF sy-subrc EQ 0.

      ASSIGN ls_data_entity-r_t_data->* TO <lt_data_ent>.

      CHECK <lt_data_ent> IS ASSIGNED.

      LOOP AT <lt_data_ent> ASSIGNING <ls_data_ent>.

        ASSIGN COMPONENT 'TAXNUM' OF STRUCTURE <ls_data_ent> TO <ls_taxnr>.
        IF sy-subrc = 0.
          rv_bp_taxnum = <ls_taxnr>.
        ENDIF.

      ENDLOOP.

    ENDIF.
  ENDMETHOD.
ENDCLASS.