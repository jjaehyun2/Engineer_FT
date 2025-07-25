*&---------------------------------------------------------------------*
*&  Include           ZABAPGIT_OBJECT_TRAN
*&---------------------------------------------------------------------*

*----------------------------------------------------------------------*
*       CLASS lcl_object_tran DEFINITION
*----------------------------------------------------------------------*
*
*----------------------------------------------------------------------*
CLASS lcl_object_tran DEFINITION INHERITING FROM lcl_objects_super FINAL.

  PUBLIC SECTION.
    INTERFACES lif_object.
    ALIASES mo_files FOR lif_object~mo_files.

  PRIVATE SECTION.

    CONSTANTS: c_oo_program(9)    VALUE '\PROGRAM=',
               c_oo_class(7)      VALUE '\CLASS=',
               c_oo_method(8)     VALUE '\METHOD=',
               c_oo_tcode         TYPE tcode VALUE 'OS_APPLICATION',
               c_oo_frclass(30)   VALUE 'CLASS',
               c_oo_frmethod(30)  VALUE 'METHOD',
               c_oo_frupdtask(30) VALUE 'UPDATE_MODE',
               c_oo_synchron      VALUE 'S',
               c_oo_asynchron     VALUE 'U',
               c_true             TYPE c VALUE 'X',
               c_false            TYPE c VALUE space.

    METHODS:
      split_parameters
        CHANGING ct_rsparam TYPE s_param
                 cs_rsstcd  TYPE rsstcd
                 cs_tstcp   TYPE tstcp
                 cs_tstc    TYPE tstc,

      split_parameters_comp
        IMPORTING iv_type  TYPE any
                  iv_param TYPE any
        CHANGING  cg_value TYPE any,

      serialize_texts
        IMPORTING io_xml TYPE REF TO lcl_xml_output
        RAISING lcx_exception,

      deserialize_texts
        IMPORTING io_xml TYPE REF TO lcl_xml_input
        RAISING lcx_exception.

ENDCLASS.                    "lcl_object_TRAN DEFINITION

*----------------------------------------------------------------------*
*       CLASS lcl_object_msag IMPLEMENTATION
*----------------------------------------------------------------------*
*
*----------------------------------------------------------------------*
CLASS lcl_object_tran IMPLEMENTATION.

  METHOD lif_object~has_changed_since.
    rv_changed = abap_true.
  ENDMETHOD.  "lif_object~has_changed_since

  METHOD lif_object~changed_by.
    rv_user = c_user_unknown. " todo
  ENDMETHOD.

  METHOD lif_object~get_metadata.
    rs_metadata = get_metadata( ).
  ENDMETHOD.                    "lif_object~get_metadata

  METHOD split_parameters_comp.
    DATA: lv_off TYPE i.

    IF iv_param CS iv_type.
      lv_off = sy-fdpos + strlen( iv_type ).
      cg_value = iv_param+lv_off.
      IF cg_value CA '\'.
        CLEAR cg_value+sy-fdpos.
      ENDIF.
    ENDIF.
  ENDMETHOD.                    "split_parameters_comp

  METHOD split_parameters.
* see subroutine split_parameters in include LSEUKF01

    DATA: lv_off       TYPE i,
          lv_param_beg TYPE i,
          lv_length    TYPE i,
          ls_param     LIKE LINE OF ct_rsparam.

    FIELD-SYMBOLS <lg_f> TYPE any.


    CLEAR cs_rsstcd-s_vari.

    IF cs_tstcp-param(1) = '\'.             " OO-Transaktion ohne FR
      split_parameters_comp( EXPORTING iv_type = c_oo_program
                                       iv_param = cs_tstcp-param
                             CHANGING  cg_value = cs_tstc-pgmna ).
      split_parameters_comp( EXPORTING iv_type = c_oo_class
                                       iv_param = cs_tstcp-param
                             CHANGING  cg_value = cs_rsstcd-classname ).
      split_parameters_comp( EXPORTING iv_type = c_oo_method
                                       iv_param = cs_tstcp-param
                             CHANGING  cg_value = cs_rsstcd-method ).

      IF NOT cs_tstc-pgmna IS INITIAL.
        cs_rsstcd-s_local = c_true.
      ENDIF.
      RETURN.
    ELSEIF cs_tstcp-param(1) = '@'.         " Transaktionsvariante
      cs_rsstcd-s_vari = c_true.
      IF cs_tstcp-param(2) = '@@'.
        cs_rsstcd-s_ind_vari = c_true.
        lv_off = 2.
      ELSE.
        CLEAR cs_rsstcd-s_ind_vari.
        lv_off = 1.
      ENDIF.
      sy-fdpos = sy-fdpos - lv_off.
      IF sy-fdpos > 0.
        cs_rsstcd-call_tcode = cs_tstcp-param+lv_off(sy-fdpos).
        sy-fdpos = sy-fdpos + 1 + lv_off.
        cs_rsstcd-variant = cs_tstcp-param+sy-fdpos.
      ENDIF.
    ELSEIF cs_tstcp-param(1) = '/'.
      cs_rsstcd-st_tcode = c_true.
      cs_rsstcd-st_prog  = space.
      IF cs_tstcp-param+1(1) = '*'.
        cs_rsstcd-st_skip_1 = c_true.
      ELSE.
        CLEAR cs_rsstcd-st_skip_1.
      ENDIF.
      lv_param_beg = sy-fdpos + 1.
      sy-fdpos = sy-fdpos - 2.
      IF sy-fdpos > 0.
        cs_rsstcd-call_tcode = cs_tstcp-param+2(sy-fdpos).
      ENDIF.
      SHIFT cs_tstcp-param BY lv_param_beg PLACES.
    ELSE.
      cs_rsstcd-st_tcode = space.
      cs_rsstcd-st_prog  = c_true.
    ENDIF.

    DO 254 TIMES.
      IF cs_tstcp-param = space.
        EXIT.
      ENDIF.
      CLEAR ls_param.
      IF cs_tstcp-param CA '='.
        CHECK sy-fdpos <> 0.
        ASSIGN cs_tstcp-param(sy-fdpos) TO <lg_f>.
        ls_param-field = <lg_f>.
        IF ls_param-field(1) = space.
          SHIFT ls_param-field.
        ENDIF.
        sy-fdpos = sy-fdpos + 1.
        SHIFT cs_tstcp-param BY sy-fdpos PLACES.
        IF cs_tstcp-param CA ';'.
          IF sy-fdpos <> 0.
            ASSIGN cs_tstcp-param(sy-fdpos) TO <lg_f>.
            ls_param-value = <lg_f>.
            IF ls_param-value(1) = space.
              SHIFT ls_param-value.
            ENDIF.
          ENDIF.
          sy-fdpos = sy-fdpos + 1.
          SHIFT cs_tstcp-param BY sy-fdpos PLACES.
          APPEND ls_param TO ct_rsparam.
        ELSE.
          lv_length = strlen( cs_tstcp-param ).
          CHECK lv_length > 0.
          ASSIGN cs_tstcp-param(lv_length) TO <lg_f>.
          ls_param-value = <lg_f>.
          IF ls_param-value(1) = space.
            SHIFT ls_param-value.
          ENDIF.
          lv_length = lv_length + 1.
          SHIFT cs_tstcp-param BY lv_length PLACES.
          APPEND ls_param TO ct_rsparam.
        ENDIF.
      ENDIF.
    ENDDO.
* oo-Transaktion mit Framework
    IF cs_rsstcd-call_tcode = c_oo_tcode.
      cs_rsstcd-s_trframe = c_true.
      LOOP AT ct_rsparam INTO ls_param.
        CASE ls_param-field.
          WHEN c_oo_frclass.
            cs_rsstcd-classname = ls_param-value.
          WHEN c_oo_frmethod.
            cs_rsstcd-method   = ls_param-value.
          WHEN c_oo_frupdtask.
            IF ls_param-value = c_oo_synchron.
              cs_rsstcd-s_upddir  = c_true.
              cs_rsstcd-s_updtask = c_false.
              cs_rsstcd-s_updlok  = c_false.
            ELSEIF ls_param-value = c_oo_asynchron.
              cs_rsstcd-s_upddir  = c_false.
              cs_rsstcd-s_updtask = c_true.
              cs_rsstcd-s_updlok  = c_false.
            ELSE.
              cs_rsstcd-s_upddir  = c_false.
              cs_rsstcd-s_updtask = c_false.
              cs_rsstcd-s_updlok  = c_true.
            ENDIF.
        ENDCASE.
      ENDLOOP.
    ENDIF.
  ENDMETHOD.                    "split_parameters

  METHOD lif_object~exists.

    DATA: lv_tcode TYPE tstc-tcode.


    SELECT SINGLE tcode FROM tstc INTO lv_tcode
      WHERE tcode = ms_item-obj_name.                   "#EC CI_GENBUFF
    rv_bool = boolc( sy-subrc = 0 ).

  ENDMETHOD.                    "lif_object~exists

  METHOD lif_object~jump.

    DATA: lt_bdcdata TYPE TABLE OF bdcdata.

    FIELD-SYMBOLS: <ls_bdcdata> LIKE LINE OF lt_bdcdata.


    APPEND INITIAL LINE TO lt_bdcdata ASSIGNING <ls_bdcdata>.
    <ls_bdcdata>-program  = 'SAPLSEUK'.
    <ls_bdcdata>-dynpro   = '0390'.
    <ls_bdcdata>-dynbegin = abap_true.

    APPEND INITIAL LINE TO lt_bdcdata ASSIGNING <ls_bdcdata>.
    <ls_bdcdata>-fnam = 'BDC_OKCODE'.
    <ls_bdcdata>-fval = '=SHOW'.

    APPEND INITIAL LINE TO lt_bdcdata ASSIGNING <ls_bdcdata>.
    <ls_bdcdata>-fnam = 'TSTC-TCODE'.
    <ls_bdcdata>-fval = ms_item-obj_name.

    CALL FUNCTION 'ABAP4_CALL_TRANSACTION'
      STARTING NEW TASK 'GIT'
      EXPORTING
        tcode                 = 'SE93'
        mode_val              = 'E'
      TABLES
        using_tab             = lt_bdcdata
      EXCEPTIONS
        system_failure        = 1
        communication_failure = 2
        resource_failure      = 3
        OTHERS                = 4
        ##fm_subrc_ok.    "#EC CI_SUBRC

  ENDMETHOD.                    "jump

  METHOD lif_object~delete.

    DATA: lv_transaction TYPE tstc-tcode.


    lv_transaction = ms_item-obj_name.

    CALL FUNCTION 'RPY_TRANSACTION_DELETE'
      EXPORTING
        transaction      = lv_transaction
      EXCEPTIONS
        not_excecuted    = 1
        object_not_found = 2
        OTHERS           = 3.
    IF sy-subrc <> 0.
      lcx_exception=>raise( 'Error from RPY_TRANSACTION_DELETE' ).
    ENDIF.

  ENDMETHOD.                    "delete

  METHOD lif_object~deserialize.

    CONSTANTS: lc_hex_tra TYPE x VALUE '00',
*               c_hex_men TYPE x VALUE '01',
               lc_hex_par TYPE x VALUE '02',
               lc_hex_rep TYPE x VALUE '80'.
*               c_hex_rpv TYPE x VALUE '10',
*               c_hex_obj TYPE x VALUE '08',
*               c_hex_chk TYPE x VALUE '04',
*               c_hex_enq TYPE x VALUE '20'.

    DATA: lv_dynpro       TYPE d020s-dnum,
          ls_tstc         TYPE tstc,
          lv_type         TYPE rglif-docutype,
          ls_tstct        TYPE tstct,
          ls_tstcc        TYPE tstcc,
          ls_tstcp        TYPE tstcp,
          lt_param_values TYPE TABLE OF rsparam,
          ls_rsstcd       TYPE rsstcd.


    IF lif_object~exists( ) = abap_true.
      lif_object~delete( ).
    ENDIF.

    io_xml->read( EXPORTING iv_name = 'TSTC'
                  CHANGING cg_data = ls_tstc ).
    io_xml->read( EXPORTING iv_name = 'TSTCC'
                  CHANGING cg_data = ls_tstcc ).
    io_xml->read( EXPORTING iv_name = 'TSTCT'
                  CHANGING cg_data = ls_tstct ).
    io_xml->read( EXPORTING iv_name = 'TSTCP'
                  CHANGING cg_data = ls_tstcp ).

    lv_dynpro = ls_tstc-dypno.

    CASE ls_tstc-cinfo.
      WHEN lc_hex_tra.
        lv_type = ststc_c_type_dialog.
      WHEN lc_hex_rep.
        lv_type = ststc_c_type_report.
      WHEN lc_hex_par.
        lv_type = ststc_c_type_parameters.
* todo, or ststc_c_type_variant?
      WHEN OTHERS.
        lcx_exception=>raise( 'Transaction, unknown CINFO' ).
    ENDCASE.

    IF ls_tstcp IS NOT INITIAL.
      split_parameters(
        CHANGING
          ct_rsparam = lt_param_values
          cs_rsstcd  = ls_rsstcd
          cs_tstcp   = ls_tstcp
          cs_tstc    = ls_tstc ).
    ENDIF.

    CALL FUNCTION 'RPY_TRANSACTION_INSERT'
      EXPORTING
        transaction             = ls_tstc-tcode
        program                 = ls_tstc-pgmna
        dynpro                  = lv_dynpro
        language                = mv_language
        development_class       = iv_package
        transaction_type        = lv_type
        shorttext               = ls_tstct-ttext
        called_transaction      = ls_rsstcd-call_tcode
        called_transaction_skip = ls_rsstcd-st_skip_1
        variant                 = ls_rsstcd-variant
        cl_independend          = ls_rsstcd-s_ind_vari
        html_enabled            = ls_tstcc-s_webgui
        java_enabled            = ls_tstcc-s_platin
        wingui_enabled          = ls_tstcc-s_win32
      TABLES
        param_values            = lt_param_values
      EXCEPTIONS
        cancelled               = 1
        already_exist           = 2
        permission_error        = 3
        name_not_allowed        = 4
        name_conflict           = 5
        illegal_type            = 6
        object_inconsistent     = 7
        db_access_error         = 8
        OTHERS                  = 9.
    IF sy-subrc <> 0.
      lcx_exception=>raise( 'Error from RPY_TRANSACTION_INSERT' ).
    ENDIF.

    " Texts deserializing (translations)
    deserialize_texts( io_xml ).

  ENDMETHOD.                    "deserialize

  METHOD lif_object~serialize.

    DATA: lv_transaction TYPE tstc-tcode,
          lt_tcodes      TYPE TABLE OF tstc,
          ls_tcode       LIKE LINE OF lt_tcodes,
          ls_tstct       TYPE tstct,
          ls_tstcp       TYPE tstcp,
          lt_gui_attr    TYPE TABLE OF tstcc,
          ls_gui_attr    LIKE LINE OF lt_gui_attr.


    lv_transaction = ms_item-obj_name.

    CALL FUNCTION 'RPY_TRANSACTION_READ'
      EXPORTING
        transaction      = lv_transaction
      TABLES
        tcodes           = lt_tcodes
        gui_attributes   = lt_gui_attr
      EXCEPTIONS
        permission_error = 1
        cancelled        = 2
        not_found        = 3
        object_not_found = 4
        OTHERS           = 5.
    IF sy-subrc = 4 OR sy-subrc = 3.
      RETURN.
    ELSEIF sy-subrc <> 0.
      lcx_exception=>raise( 'Error from RPY_TRANSACTION_READ' ).
    ENDIF.

    SELECT SINGLE * FROM tstct INTO ls_tstct
      WHERE sprsl = mv_language
      AND tcode = lv_transaction.         "#EC CI_SUBRC "#EC CI_GENBUFF

    SELECT SINGLE * FROM tstcp INTO ls_tstcp
      WHERE tcode = lv_transaction.       "#EC CI_SUBRC "#EC CI_GENBUFF

    READ TABLE lt_tcodes INDEX 1 INTO ls_tcode.
    ASSERT sy-subrc = 0.
    READ TABLE lt_gui_attr INDEX 1 INTO ls_gui_attr.
    ASSERT sy-subrc = 0.

    io_xml->add( iv_name = 'TSTC'
                 ig_data = ls_tcode ).
    io_xml->add( iv_name = 'TSTCC'
                 ig_data = ls_gui_attr ).
    io_xml->add( iv_name = 'TSTCT'
                 ig_data = ls_tstct ).
    IF ls_tstcp IS NOT INITIAL.
      io_xml->add( iv_name = 'TSTCP'
                   ig_data = ls_tstcp ).
    ENDIF.

    " Texts serializing (translations)
    serialize_texts( io_xml ).

  ENDMETHOD.                    "serialize

  METHOD lif_object~compare_to_remote_version.
    CREATE OBJECT ro_comparison_result TYPE lcl_null_comparison_result.
  ENDMETHOD.

  METHOD serialize_texts.

    DATA lt_tpool_i18n TYPE TABLE OF tstct.

    " Skip master language - it was already serialized
    " Don't serialize t-code itself
    SELECT sprsl ttext
      INTO CORRESPONDING FIELDS OF TABLE lt_tpool_i18n
      FROM tstct
      WHERE sprsl <> mv_language
      AND   tcode = ms_item-obj_name.

    IF lines( lt_tpool_i18n ) > 0.
      SORT lt_tpool_i18n BY sprsl ASCENDING.
      io_xml->add( iv_name = 'I18N_TPOOL'
                   ig_data = lt_tpool_i18n ).
    ENDIF.

  ENDMETHOD.                    "serialize_texts

  METHOD deserialize_texts.

    DATA lt_tpool_i18n TYPE TABLE OF tstct.

    FIELD-SYMBOLS <tpool> LIKE LINE OF lt_tpool_i18n.

    " Read XML-files data
    io_xml->read( EXPORTING iv_name = 'I18N_TPOOL'
                  CHANGING  cg_data = lt_tpool_i18n ).

    " Force t-code name (security reasons)
    LOOP AT lt_tpool_i18n ASSIGNING <tpool>.
      <tpool>-tcode = ms_item-obj_name.
    ENDLOOP.

    IF lines( lt_tpool_i18n ) > 0.
      MODIFY tstct FROM TABLE lt_tpool_i18n.
      IF sy-subrc <> 0.
        lcx_exception=>raise( 'Update of t-code translations failed' ).
      ENDIF.
    ENDIF.

  ENDMETHOD.                    "deserialize_texts
ENDCLASS.                    "lcl_object_tran IMPLEMENTATION