CLASS zcl_abapgit_object_wdcc DEFINITION INHERITING FROM zcl_abapgit_objects_super FINAL.

  PUBLIC SECTION.
    INTERFACES zif_abapgit_object.
    ALIASES mo_files FOR zif_abapgit_object~mo_files.

*    METHODS constructor
*      IMPORTING
*                is_item TYPE ty_item
*      RAISING   cx_sy_create_object_error.

  PRIVATE SECTION.
    METHODS read
      EXPORTING es_outline TYPE wdy_cfg_outline_data
                et_data    TYPE wdy_cfg_persist_data_tab
      RAISING   zcx_abapgit_exception.

    METHODS save
      IMPORTING is_outline TYPE wdy_cfg_outline_data
                it_data    TYPE wdy_cfg_persist_data_tab
                iv_package TYPE devclass
      RAISING   zcx_abapgit_exception.

ENDCLASS.                    "lcl_object_wdca DEFINITION

*----------------------------------------------------------------------*
*       CLASS zcl_abapgit_object_wdcc IMPLEMENTATION
*----------------------------------------------------------------------*
*
*----------------------------------------------------------------------*
*----------------------------------------------------------------------*
*       CLASS zcl_abapgit_object_wdcc IMPLEMENTATION
*----------------------------------------------------------------------*
*
*----------------------------------------------------------------------*
CLASS zcl_abapgit_object_wdcc IMPLEMENTATION.
  "lif_object~get_metadata
  METHOD save.
*    _raise 'WDCA, save not implemented'.
    DATA: lo_cfg       TYPE REF TO cl_wdr_cfg_persistence_comp,
          ls_key       TYPE wdy_config_key,
          ls_data      LIKE LINE OF it_data,
          lv_operation TYPE i,
          lv_name      TYPE wdy_md_object_name,
          lv_exists    TYPE wdy_boolean,
          lt_data      TYPE wdy_cfg_persist_data_tab.


    MOVE-CORRESPONDING is_outline TO ls_key.

    TRY.
        CREATE OBJECT lo_cfg
          EXPORTING
            config_key  = ls_key
            object_name = lv_name.

        READ TABLE it_data INDEX 1 INTO ls_data.
        ASSERT sy-subrc = 0.
        TRY .
            lo_cfg->check_config_existent(
                     EXPORTING
                       i_outline_data       = is_outline
                       i_only_current_layer = abap_false
                       i_is_original        = abap_true
                     IMPORTING
                       e_is_existent        = lv_exists ).

          CATCH cx_wd_configuration.

        ENDTRY.
        TRY .
            lt_data = it_data.

            lo_cfg->read_data( RECEIVING config_data = lt_data ).

          CATCH cx_wd_configuration.

        ENDTRY.

        tadir_insert( iv_package ).
        DATA(lv_transport) = zcl_abapgit_default_transport=>get_instance(
                                              )->get( )-ordernum.
        lo_cfg->set_transport( devclass = iv_package ).
        lo_cfg->set_transport( trkorr = lv_transport devclass = iv_package ).
        lo_cfg->set_save_data( ls_data ).

        lo_cfg->set_config_description( is_outline ).
        lv_operation = if_wdr_cfg_constants=>c_cts_operation-e_create.
        lo_cfg->do_next_step( CHANGING c_operation = lv_operation ).
        lv_operation = if_wdr_cfg_constants=>c_cts_operation-e_save.
        lo_cfg->do_next_step( CHANGING c_operation = lv_operation ).



      CATCH cx_wd_configuration.
        zcx_abapgit_exception=>raise( 'WDCC, save error ' ).
    ENDTRY.

  ENDMETHOD.                    "save

  METHOD read.

    DATA: lo_cfg    TYPE REF TO cl_wdr_cfg_persistence_comp,
          ls_key    TYPE wdy_config_key,
          lv_exists TYPE abap_bool,
          lx_err    TYPE REF TO cx_wd_configuration,
          lv_name   TYPE wdy_md_object_name.


    CLEAR et_data.

    ls_key = ms_item-obj_name.

    TRY.
        CREATE OBJECT lo_cfg
          EXPORTING
            config_key  = ls_key
            object_name = lv_name.

        MOVE-CORRESPONDING ls_key TO es_outline.

        lo_cfg->check_config_existent(
          EXPORTING
            i_outline_data       = es_outline
            i_only_current_layer = abap_false
            i_is_original        = abap_true
          IMPORTING
            e_is_existent        = lv_exists ).
        IF lv_exists = abap_false.
          CLEAR es_outline.
          RETURN.
        ENDIF.

        es_outline = lo_cfg->read_outline_data( ).
      CATCH cx_wd_configuration INTO lx_err.
        IF lx_err->textid = cx_wd_configuration=>conf_config_not_exist.
          CLEAR es_outline.
          RETURN.
        ELSE.
          zcx_abapgit_exception=>raise( 'WDCC, read error' ).
        ENDIF.
    ENDTRY.

    CLEAR: es_outline-devclass,
           es_outline-author,
           es_outline-createdon,
           es_outline-changedby,
           es_outline-changedon.
    et_data = lo_cfg->read_data( ).

  ENDMETHOD.                    "read

  METHOD zif_abapgit_object~get_deserialize_steps.
    APPEND zif_abapgit_object=>gc_step_id-abap TO rt_steps.
  ENDMETHOD.
  METHOD zif_abapgit_object~changed_by.
    rv_user = c_user_unknown. " todo
  ENDMETHOD.
  METHOD zif_abapgit_object~delete.

    DATA: lo_component   TYPE REF TO cl_wdy_wb_component,
          lo_request     TYPE REF TO cl_wb_request,
          li_state       TYPE REF TO if_wb_program_state,
          lv_object_name TYPE seu_objkey.

    CREATE OBJECT lo_component.

    lv_object_name = ms_item-obj_name.
    CREATE OBJECT lo_request
      EXPORTING
        p_object_type = 'YC'
        p_object_name = lv_object_name
        p_operation   = swbm_c_op_delete_no_dialog.

    lo_component->if_wb_program~process_wb_request(
      p_wb_request       = lo_request
      p_wb_program_state = li_state ).

  ENDMETHOD.
  METHOD zif_abapgit_object~exists.

    DATA: ls_wdy_config_data TYPE wdy_config_data.
    DATA: ls_wdy_config_key TYPE wdy_config_key.

    ls_wdy_config_key = ms_item-obj_name.
    SELECT SINGLE * FROM wdy_config_data
      INTO ls_wdy_config_data
      WHERE config_id = ls_wdy_config_key-config_id
        AND config_type = ls_wdy_config_key-config_type
        AND config_var = ls_wdy_config_key-config_var.  "#EC CI_GENBUFF
    rv_bool = boolc( sy-subrc = 0 ).

  ENDMETHOD.
  METHOD zif_abapgit_object~get_comparator.
    RETURN.
  ENDMETHOD.
  METHOD zif_abapgit_object~get_metadata.
    rs_metadata = get_metadata( ).
  ENDMETHOD.
  METHOD zif_abapgit_object~is_active.
    rv_active = is_active( ).
  ENDMETHOD.
  METHOD zif_abapgit_object~is_locked.
    rv_is_locked = abap_false.
  ENDMETHOD.

  METHOD zif_abapgit_object~serialize.

    DATA: ls_outline TYPE wdy_cfg_outline_data,
          lt_data    TYPE wdy_cfg_persist_data_tab.


    read( IMPORTING es_outline = ls_outline
                    et_data    = lt_data ).
    IF ls_outline IS INITIAL.
      RETURN.
    ENDIF.

    io_xml->add( iv_name = 'OUTLINE'
                 ig_data = ls_outline ).
    io_xml->add( iv_name = 'DATA'
                 ig_data = lt_data ).

  ENDMETHOD.                    "serialize

  METHOD zif_abapgit_object~deserialize.

    DATA: ls_outline TYPE wdy_cfg_outline_data,
          lt_data    TYPE wdy_cfg_persist_data_tab.


    io_xml->read( EXPORTING iv_name = 'OUTLINE'
                  CHANGING cg_data = ls_outline ).
    io_xml->read( EXPORTING iv_name = 'DATA'
                  CHANGING cg_data = lt_data ).

    save( is_outline = ls_outline
          it_data    = lt_data
          iv_package = iv_package ).

  ENDMETHOD.                    "deserialize

  METHOD zif_abapgit_object~jump.

    CALL FUNCTION 'RS_TOOL_ACCESS'
      EXPORTING
        operation     = 'SHOW'
        object_name   = ms_item-obj_name
        object_type   = ms_item-obj_type
        in_new_window = abap_true.

  ENDMETHOD.                    "jump

ENDCLASS.                    "zcl_abapgit_object_wdcc IMPLEMENTATION