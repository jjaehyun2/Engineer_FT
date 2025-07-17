class ZCL_MDG_BP_HELPER_UTILITIES definition
  public
  final
  create public .

public section.

  class-methods GET_CURRENT_BP
    importing
      !IO_BP_DATA type ref to ZCL_MDG_BP_HELPER
    returning
      value(RV_BP) type BU_PARTNER .
  class-methods GET_CURRENT_BP_FROM_FPM_PARA
    returning
      value(RV_BP) type BU_PARTNER .
  class-methods GET_MDG_ATTR_FROM_GENIL_FLD
    importing
      !IV_FIELD_NAME type NAME_KOMP
      !IO_BP_DATA type ref to ZCL_MDG_BP_HELPER optional
    returning
      value(RV_ATTRIBUTE) type USMD_ATTRIBUTE .
  class-methods GET_MDG_FIELDNAMES
    importing
      !IO_BP_DATA type ref to ZCL_MDG_BP_HELPER optional
    exporting
      !ET_FIELD_NAMES type ZIF_MDG_BP_DATATYPES=>GTY_T_MDG_BS_BP_FLDGRP .
  PROTECTED SECTION.
  PRIVATE SECTION.

    CLASS-DATA gt_mdg_fieldnames TYPE zif_mdg_bp_datatypes=>gty_t_mdg_bs_bp_fldgrp .
ENDCLASS.



CLASS ZCL_MDG_BP_HELPER_UTILITIES IMPLEMENTATION.


  METHOD get_current_bp.

    DATA:
      lt_bp_header TYPE zif_mdg_bp_datatypes=>gty_t_bp_header,
      ls_bp_header TYPE /mdgbp/_s_bp_pp_bp_header.


    CALL METHOD get_current_bp_from_fpm_para
      RECEIVING
        rv_bp = rv_bp.

    IF rv_bp IS INITIAL.
      CALL METHOD io_bp_data->get_bp_header
        IMPORTING
          et_bp_header = lt_bp_header.
      READ TABLE lt_bp_header INDEX 1 INTO ls_bp_header.
      rv_bp = ls_bp_header-bp_header.
    ENDIF.

  ENDMETHOD.


  METHOD get_current_bp_from_fpm_para.
    DATA:
      lo_fpm TYPE REF TO if_fpm.

*&---Get the handle to the IF_FPM interface.
    lo_fpm = cl_fpm_factory=>get_instance( ).

*&---Get the parameter change request no. from FPM
    CALL METHOD lo_fpm->mo_app_parameter->get_value
      EXPORTING
        iv_key   = 'BP_HEADER'
      IMPORTING
        ev_value = rv_bp.

  ENDMETHOD.


  METHOD get_mdg_attr_from_genil_fld.

    DATA:
      lo_model_ext   TYPE REF TO if_usmd_model_ext,
      lo_bp_services TYPE REF TO cl_mdg_bs_fnd_bp_services,
      ls_fld_grp     TYPE zif_mdg_bp_datatypes=>gty_s_mdg_bs_bp_fldgrp,
      lt_fld_grp     TYPE mdg_bs_bp_fldgrp_t,
      lt_fldmap_ecc  TYPE usmd_ts_map_struc,
      lt_entity_keys TYPE usmd_t_entity.

    FIELD-SYMBOLS:
      <ls_entity_prop> TYPE usmd_s_entity_prop_ext,
      <ls_fldmap_ecc>  TYPE usmd_s_map_struc.

    IF gt_mdg_fieldnames IS INITIAL.

      CREATE OBJECT lo_bp_services.

      CALL METHOD cl_usmd_model_ext=>get_instance(
        EXPORTING
          i_usmd_model = if_mdg_bp_constants=>gc_bp_model
        IMPORTING
          eo_instance  = lo_model_ext ).

      LOOP AT lo_model_ext->dt_entity_prop ASSIGNING <ls_entity_prop>
        WHERE usage_type EQ if_usmd_dm_const=>usage_type_1 OR usage_type EQ if_usmd_dm_const=>usage_type_4. "#EC CI_SORTSEQ
        CLEAR:lt_fld_grp,lt_fldmap_ecc.
        lo_bp_services->get_fieldmapping_for_entity(
          EXPORTING
            io_model             = lo_model_ext
            iv_entity            = <ls_entity_prop>-usmd_entity
          IMPORTING
            et_bp_fldgrp         =  lt_fld_grp
            et_field_mapping_ecc =  lt_fldmap_ecc ).

        APPEND LINES OF lt_fld_grp TO gt_mdg_fieldnames.

        LOOP AT lt_fldmap_ecc ASSIGNING <ls_fldmap_ecc>. "#EC CI_NESTED
          ls_fld_grp-bp_fldgrp-model     = if_mdg_bp_constants=>gc_bp_model.
          ls_fld_grp-bp_fldgrp-entity    = <ls_fldmap_ecc>-usmd_entity.
          ls_fld_grp-bp_fldgrp-bapifldnm = <ls_fldmap_ecc>-fld_source.
          ls_fld_grp-bp_fldgrp-attribute = <ls_fldmap_ecc>-fieldname.

          CALL METHOD io_bp_data->get_keys_of_entity
            EXPORTING
              iv_entity      = ls_fld_grp-bp_fldgrp-entity
            IMPORTING
              et_entity_keys = lt_entity_keys.

          READ TABLE lt_entity_keys TRANSPORTING NO FIELDS WITH TABLE KEY table_line = ls_fld_grp-bp_fldgrp-attribute.
          IF sy-subrc = 0.
            ls_fld_grp-is_key_field = abap_true.
          ENDIF.

          APPEND ls_fld_grp TO gt_mdg_fieldnames.
        ENDLOOP.
      ENDLOOP.
    ENDIF.

    READ TABLE gt_mdg_fieldnames INTO ls_fld_grp WITH KEY bp_fldgrp-bapifldnm = iv_field_name.
    IF sy-subrc EQ 0.
      rv_attribute = ls_fld_grp-bp_fldgrp-attribute.
    ELSE.
      rv_attribute = iv_field_name.
    ENDIF.

  ENDMETHOD.


  METHOD get_mdg_fieldnames.

    DATA:
      lo_model_ext   TYPE REF TO if_usmd_model_ext,
      lo_bp_services TYPE REF TO cl_mdg_bs_fnd_bp_services,
      ls_fld_grp     TYPE zif_mdg_bp_datatypes=>gty_s_mdg_bs_bp_fldgrp,
      lt_fld_grp     TYPE mdg_bs_bp_fldgrp_t,
      lt_fldmap_ecc  TYPE usmd_ts_map_struc,
      lt_entity_keys TYPE usmd_t_entity.

    FIELD-SYMBOLS:
      <ls_entity_prop> TYPE usmd_s_entity_prop_ext,
      <ls_fldmap_ecc>  TYPE usmd_s_map_struc.

    IF gt_mdg_fieldnames IS INITIAL.

      CREATE OBJECT lo_bp_services.

      CALL METHOD cl_usmd_model_ext=>get_instance(
        EXPORTING
          i_usmd_model = if_mdg_bp_constants=>gc_bp_model
        IMPORTING
          eo_instance  = lo_model_ext ).

      LOOP AT lo_model_ext->dt_entity_prop ASSIGNING <ls_entity_prop>
        WHERE usage_type EQ if_usmd_dm_const=>usage_type_1 OR usage_type EQ if_usmd_dm_const=>usage_type_4. "#EC CI_SORTSEQ
        CLEAR:lt_fld_grp,lt_fldmap_ecc.
        lo_bp_services->get_fieldmapping_for_entity(
          EXPORTING
            io_model             = lo_model_ext
            iv_entity            = <ls_entity_prop>-usmd_entity
          IMPORTING
            et_bp_fldgrp         =  lt_fld_grp
            et_field_mapping_ecc =  lt_fldmap_ecc ).

        APPEND LINES OF lt_fld_grp TO gt_mdg_fieldnames.

        LOOP AT lt_fldmap_ecc ASSIGNING <ls_fldmap_ecc>. "#EC CI_NESTED
          ls_fld_grp-bp_fldgrp-model     = if_mdg_bp_constants=>gc_bp_model.
          ls_fld_grp-bp_fldgrp-entity    = <ls_fldmap_ecc>-usmd_entity.
          ls_fld_grp-bp_fldgrp-bapifldnm = <ls_fldmap_ecc>-fld_source.
          ls_fld_grp-bp_fldgrp-attribute = <ls_fldmap_ecc>-fieldname.

          CALL METHOD io_bp_data->get_keys_of_entity
            EXPORTING
              iv_entity      = ls_fld_grp-bp_fldgrp-entity
            IMPORTING
              et_entity_keys = lt_entity_keys.

          READ TABLE lt_entity_keys TRANSPORTING NO FIELDS WITH TABLE KEY table_line = ls_fld_grp-bp_fldgrp-attribute.
          IF sy-subrc = 0.
            ls_fld_grp-is_key_field = abap_true.
          ENDIF.

          APPEND ls_fld_grp TO gt_mdg_fieldnames.
        ENDLOOP.
      ENDLOOP.
    ENDIF.

    et_field_names = gt_mdg_fieldnames.

  ENDMETHOD.
ENDCLASS.