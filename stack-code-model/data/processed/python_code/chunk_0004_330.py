class /ENSX/CL_XSLT_MANAGER definition
  public
  create public .

public section.
  type-pools SWBM .

  data GS_ATTRIBUTES type O2XSLTATTR .
  data GV_DEVCLASS type STRING .
  data GV_PROGNAME type STRING .
  data GV_SOURCE type STRING .
  data GV_TRANSPORT type TRKORR .
  data GO_XSLTDESC type ref to CL_O2_API_XSLTDESC .

  methods CONSTRUCTOR
    importing
      !PROGNAME type STRING
      !DEVCLASS type STRING
      !XSLTSOURCE type STRING optional .
  methods GET_ATTRIBUTES
    returning
      value(ATTRIBUTES) type O2XSLTATTR .
  methods GET_SOURCE
    returning
      value(XSLTSOURCE) type STRING .
  methods GET_TRANSPORT_NUMBER
    returning
      value(TRANSPORT) type TRKORR .
  methods SET_ATTRIBUTES
    importing
      !ATTRIBUTES type O2XSLTATTR .
  methods SET_SOURCE
    importing
      !XSLTSOURCE type STRING .
  methods SET_TRANSPORT_NUMBER
    importing
      !TRANSPORT type TRKORR .
  methods ST_PROGRAM_ACTIVATE
    raising
      /ENSX/CX_XSLT .
  methods ST_PROGRAM_GENERATE
    raising
      /ENSX/CX_XSLT .
  methods ST_PROGRAM_CREATE
    importing
      !PROGNAME type STRING optional
      !DEVCLASS type STRING optional
      !RE_CREATE type BOOLE_D optional
      !COMMENT type STRING optional
    raising
      /ENSX/CX_XSLT .
  methods ST_PROGRAM_DELETE
    raising
      /ENSX/CX_XSLT .
  methods ST_PROGRAM_EDIT
    raising
      /ENSX/CX_XSLT .
  methods ST_PROGRAM_COPY
    importing
      !TARGET_PROGNAME type STRING
      !TARGET_DEVCLASS type STRING
    raising
      /ENSX/CX_XSLT .
  methods ST_PROGRAM_EXISTS
    returning
      value(EXISTS) type BOOLE_D
    raising
      /ENSX/CX_XSLT .
  methods ST_PROGRAM_LOAD
    importing
      !PROGNAME type STRING optional
      !DEVCLASS type STRING optional
    raising
      /ENSX/CX_XSLT .
  methods ST_PROGRAM_PRETTY_PRINT
    raising
      /ENSX/CX_XSLT .
  methods ST_PROGRAM_SAVE
    raising
      /ENSX/CX_XSLT .
  methods ST_PROGRAM_GET_CHANGEABLE
    returning
      value(CHANGEABLE) type BOOLE_D
    raising
      /ENSX/CX_XSLT .
  methods ST_PROGRAM_SET_CHANGEABLE
    importing
      !CHANGEABLE type BOOLE_D
    raising
      /ENSX/CX_XSLT .
  methods ST_PROGRAM_UPDATE
    importing
      !PROGNAME type STRING
      !DEVCLASS type STRING
    raising
      /ENSX/CX_XSLT .
  methods _SOURCE2STRING
    importing
      !SOURCE type O2PAGELINE_TABLE
    returning
      value(STRING) type STRING .
  methods _STRING2SOURCE
    importing
      !STRING type STRING
    returning
      value(SOURCE) type O2PAGELINE_TABLE .
  methods _XSLT_API_CREATE
    raising
      /ENSX/CX_XSLT .
protected section.
private section.
ENDCLASS.



CLASS /ENSX/CL_XSLT_MANAGER IMPLEMENTATION.


  METHOD constructor.
    gv_progname = progname.
    gv_devclass = devclass.
    gv_source   = xsltsource.
  ENDMETHOD.


  method GET_ATTRIBUTES.
    attributes = gs_attributes.
  endmethod.


  method GET_SOURCE.
    xsltsource = gv_source.
  endmethod.


  method GET_TRANSPORT_NUMBER.
    transport = gv_transport.
  endmethod.


  method SET_ATTRIBUTES.
    gs_attributes = attributes.
  endmethod.


  method SET_SOURCE.
    gv_source = xsltsource.
  endmethod.


  method SET_TRANSPORT_NUMBER.
    gv_transport = transport.
  endmethod.


METHOD st_program_activate.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
  DATA: lcx_root       TYPE REF TO cx_root.
  DATA: textid         TYPE scx_t100key.
  DATA: errors         TYPE o2xslterrt.
  TRY.
      IF go_xsltdesc IS NOT BOUND.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

      CALL METHOD go_xsltdesc->activate
        EXPORTING
          i_force                = abap_true
          i_suppress_corr_insert = abap_false
        IMPORTING
          e_error_list           = errors
        CHANGING
          i_transport_request    = gv_transport
        EXCEPTIONS
          syntax_errors          = 1
          storage_error          = 2
          generate_error         = 3
          OTHERS                 = 4.
      IF sy-subrc <> 0.
        textid = /ensx/cl_abap_exceptions=>_symessage_to_textid( ).
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid
            errors   = errors.
      ENDIF.

    CATCH /ensx/cx_xslt INTO lcx_root.
      RAISE EXCEPTION TYPE /ensx/cx_xslt
        EXPORTING
          previous = lcx_root
          textid   = textid.
  ENDTRY.


ENDMETHOD.


METHOD st_program_copy.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
  DATA: lcx_root       TYPE REF TO cx_root.
  DATA: textid         TYPE scx_t100key.
  DATA: errors         TYPE o2xslterrt.
  DATA: l_xsltdef      TYPE o2xsltattr.
  DATA: l_source       TYPE o2pageline_table.
  DATA: seu_objkey     TYPE seu_objkey.
  DATA: target_xslt_desc TYPE cxsltdesc.
  DATA: target_dev_class TYPE devclass.

  TRY.
      IF gv_progname IS INITIAL OR gv_devclass IS INITIAL.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

      me->st_program_load(
          progname = gv_progname
          devclass = gv_devclass
             ).

      IF me->st_program_get_changeable( ) = abap_true.
        me->st_program_set_changeable( changeable = abap_false ).
      ENDIF.

      target_xslt_desc = target_progname.
      target_dev_class = target_devclass.

      go_xsltdesc->copy(
        EXPORTING
          p_target_xslt_desc      = target_xslt_desc
          p_target_dev_class      = target_dev_class
        RECEIVING
          p_obj                   = go_xsltdesc
        EXCEPTIONS
          action_cancelled        = 1
          error_occured           = 2
          object_already_existing = 3
          object_changed          = 4
          object_invalid          = 5
          undefined_name          = 6
          others                  = 7
             ).

      IF sy-subrc NE 0.
        textid = /ensx/cl_abap_exceptions=>_symessage_to_textid( ).
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

      me->st_program_save( ).

    CATCH /ensx/cx_xslt INTO lcx_root.
      RAISE EXCEPTION TYPE /ensx/cx_xslt
        EXPORTING
          previous = lcx_root
          textid   = textid.
  ENDTRY.


ENDMETHOD.


METHOD st_program_create.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
  DATA: lcx_root       TYPE REF TO cx_root.
  DATA: textid         TYPE scx_t100key.
  DATA: l_xsltdef      TYPE o2xsltattr.
  DATA: l_source       TYPE o2pageline_table.
  DATA: l_errors       TYPE o2xslterrt.

  TRY.


      IF progname IS NOT INITIAL.
        gv_progname = progname.
      ENDIF.
      IF devclass IS NOT INITIAL.
        gv_devclass = devclass.
      ENDIF.

      IF gv_progname IS INITIAL OR gv_devclass IS INITIAL
        OR gv_source IS INITIAL.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

      IF me->st_program_exists( ) = abap_true.
        IF re_create = abap_true.
          me->st_program_delete( ).
        ELSE.
          RAISE EXCEPTION TYPE /ensx/cx_xslt
            EXPORTING
              previous = lcx_root
              textid   = textid.
        ENDIF.
      ENDIF.

      l_xsltdef-xsltdesc = gv_progname.
      l_xsltdef-devclass = gv_devclass.
      l_xsltdef-langu    = sy-langu.
      l_xsltdef-descript = 'Auto-Generated Simple Transformation'.
      IF comment IS SUPPLIED AND comment IS NOT INITIAL.
        CONCATENATE 'XSLT: ' comment INTO l_xsltdef-descript.
      ENDIF.

      l_source = me->_string2source( string = gv_source ).

      CREATE OBJECT go_xsltdesc
        EXPORTING
          p_source = l_source
          p_create = ''
          p_attr   = l_xsltdef
*         P_OTR_TEXTS =
          p_state  = ' '
*         P_GEN_FLAG =
*         P_CALLED_BY_XSLT_MAINTENANCE =
        .

      CALL FUNCTION 'XSLT_MAINTENANCE'
        EXPORTING
          i_operation        = 'CREA_ACT'
          i_xslt_attributes  = l_xsltdef
          i_xslt_source      = l_source
          i_gen_flag         = 'X'
        IMPORTING
          e_error_list       = l_errors
        EXCEPTIONS
          invalid_name       = 1
          not_existing       = 2
          lock_failure       = 3
          permission_failure = 4
          error_occured      = 5
          syntax_errors      = 6
          cancelled          = 7
          data_missing       = 8
          version_not_found  = 9
          OTHERS             = 10.

      IF sy-subrc <> 0.
        textid = /ensx/cl_abap_exceptions=>_symessage_to_textid( ).
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid
            errors   = l_errors[].
      ENDIF.

      me->st_program_set_changeable( abap_true ).

      me->st_program_pretty_print( ).

      me->st_program_save( ).

      me->st_program_activate( ).

      me->st_program_set_changeable( abap_false ).

    CATCH /ensx/cx_xslt INTO lcx_root.
      RAISE EXCEPTION TYPE /ensx/cx_xslt
        EXPORTING
          previous = lcx_root
          textid   = textid.
  ENDTRY.



ENDMETHOD.


METHOD st_program_delete.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
  DATA: lcx_root       TYPE REF TO cx_root.
  DATA: textid         TYPE scx_t100key.
  DATA: l_xsltdef       TYPE o2xsltattr.
  DATA: xsltdesc        TYPE REF TO cl_o2_api_xsltdesc .
  DATA: l_source        TYPE o2pageline_table.

  TRY.
      IF gv_progname IS INITIAL OR gv_devclass IS INITIAL
        OR gv_source IS INITIAL.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

      l_xsltdef-xsltdesc = gv_progname.
      l_xsltdef-devclass = gv_devclass.

      l_source = me->_string2source( string = gv_source ).

      IF go_xsltdesc IS NOT BOUND.
        CREATE OBJECT go_xsltdesc
          EXPORTING
            p_source = l_source
            p_create = ''
            p_attr   = l_xsltdef
*           P_OTR_TEXTS =
            p_state  = ' '
*           P_GEN_FLAG =
*           P_CALLED_BY_XSLT_MAINTENANCE =
          .
      ENDIF.
      IF me->st_program_get_changeable( ) = abap_true.
        me->st_program_set_changeable( changeable = abap_false ).
      ENDIF.

      CALL FUNCTION 'XSLT_MAINTENANCE'
        EXPORTING
          i_operation        = 'DELETE'
          i_xslt_attributes  = l_xsltdef
          i_xslt_source      = l_source
        EXCEPTIONS
          invalid_name       = 1
          not_existing       = 2
          lock_failure       = 3
          permission_failure = 4
          error_occured      = 5
          syntax_errors      = 6
          cancelled          = 7
          data_missing       = 8
          version_not_found  = 9
          OTHERS             = 10.

      IF sy-subrc <> 0.
        textid = /ensx/cl_abap_exceptions=>_symessage_to_textid( ).
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

      FREE go_xsltdesc.

    CATCH /ensx/cx_xslt INTO lcx_root.
      RAISE EXCEPTION TYPE /ensx/cx_xslt
        EXPORTING
          previous = lcx_root
          textid   = textid.
  ENDTRY.


ENDMETHOD.


METHOD st_program_edit.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
  DATA: lcx_root       TYPE REF TO cx_root.
  DATA: textid         TYPE scx_t100key.
  DATA: errors         TYPE o2xslterrt.
  DATA: l_xsltdef      TYPE o2xsltattr.
  DATA: l_source       TYPE o2pageline_table.
  DATA: seu_objkey     TYPE seu_objkey.
  TRY.
      IF go_xsltdesc IS NOT BOUND.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

      IF gv_progname IS INITIAL OR gv_devclass IS INITIAL
        OR gv_source IS INITIAL.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

      l_xsltdef-xsltdesc = gv_progname.
      l_xsltdef-devclass = gv_devclass.

      l_source = me->_string2source( string = gv_source ).

      IF me->st_program_get_changeable( ) = abap_true.
        me->st_program_set_changeable( changeable = abap_false ).
      ENDIF.

      seu_objkey = l_xsltdef-xsltdesc.
      cl_o2_xsltdesc=>access_xslt_tool(
        EXPORTING
          p_object_name  = seu_objkey
          p_object_type  = swbm_c_type_xslt_file
          p_operation    = swbm_c_op_edit
*    p_object_state = p_object_state
        EXCEPTIONS
          not_possible   = 1
          OTHERS         = 2
             ).

      IF sy-subrc NE 0.
        textid = /ensx/cl_abap_exceptions=>_symessage_to_textid( ).
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

      CALL FUNCTION 'XSLT_MAINTENANCE'
        EXPORTING
          i_operation        = 'SHOW'
          i_xslt_attributes  = l_xsltdef
          i_xslt_source      = l_source
          i_gen_flag         = 'X'
        EXCEPTIONS
          invalid_name       = 1
          not_existing       = 2
          lock_failure       = 3
          permission_failure = 4
          error_occured      = 5
          syntax_errors      = 6
          cancelled          = 7
          data_missing       = 8
          version_not_found  = 9
          OTHERS             = 10.

      IF sy-subrc <> 0.
        textid = /ensx/cl_abap_exceptions=>_symessage_to_textid( ).
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

    CATCH /ensx/cx_xslt INTO lcx_root.
      RAISE EXCEPTION TYPE /ensx/cx_xslt
        EXPORTING
          previous = lcx_root
          textid   = textid.
  ENDTRY.


ENDMETHOD.


  METHOD st_program_exists.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
    DATA: lcx_root       TYPE REF TO cx_root.
    DATA: textid         TYPE scx_t100key.
    DATA: l_xsltdef      TYPE o2xsltattr.
    data: l_exists       type char1.
    TRY.
        IF gv_progname IS INITIAL OR gv_devclass IS INITIAL.
          RAISE EXCEPTION TYPE /ensx/cx_xslt
            EXPORTING
              previous = lcx_root
              textid   = textid.
        ENDIF.

        l_xsltdef-xsltdesc = gv_progname.
        l_xsltdef-devclass = gv_devclass.
        CALL METHOD cl_o2_api_xsltdesc=>exists
          EXPORTING
            p_xslt_desc = l_xsltdef-xsltdesc
          RECEIVING
            p_exists    = l_exists.
      if l_exists = 1.
        exists = abap_true.
      endif.

      CATCH /ensx/cx_xslt INTO lcx_root.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
    ENDTRY.

  ENDMETHOD.


METHOD st_program_generate.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
  DATA: lcx_root       TYPE REF TO cx_root.
  DATA: textid         TYPE scx_t100key.
  DATA: errors         TYPE o2xslterrt.
  TRY.
      IF go_xsltdesc IS NOT BOUND.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

      go_xsltdesc->generate(
        IMPORTING
          e_error_list   = errors
        EXCEPTIONS
          generate_error = 1
          OTHERS         = 2
             ).

      IF sy-subrc <> 0.
        textid = /ensx/cl_abap_exceptions=>_symessage_to_textid( ).
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid
            errors   = errors.
      ENDIF.

    CATCH /ensx/cx_xslt INTO lcx_root.
      RAISE EXCEPTION TYPE /ensx/cx_xslt
        EXPORTING
          previous = lcx_root
          textid   = textid.
  ENDTRY.


ENDMETHOD.


METHOD st_program_get_changeable.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
  DATA: lcx_root       TYPE REF TO cx_root.
  DATA: textid         TYPE scx_t100key.

  TRY.
      IF go_xsltdesc IS NOT BOUND.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

      go_xsltdesc->get_changeable(
        RECEIVING
          p_changeable   = changeable
        EXCEPTIONS
          object_invalid = 1
          OTHERS         = 2
             ).

      IF sy-subrc <> 0.
        textid = /ensx/cl_abap_exceptions=>_symessage_to_textid( ).
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

    CATCH /ensx/cx_xslt INTO lcx_root.
      RAISE EXCEPTION TYPE /ensx/cx_xslt
        EXPORTING
          previous = lcx_root
          textid   = textid.
  ENDTRY.


ENDMETHOD.


  METHOD st_program_load.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
    DATA: lcx_root       TYPE REF TO cx_root.
    DATA: textid         TYPE scx_t100key.
    DATA: l_xsltdef      TYPE o2xsltattr.
    DATA: l_state        TYPE r3state.
    DATA: l_source       TYPE o2pageline_table.
*DATA P_XSLT_DESC                  TYPE CXSLTDESC.
*DATA P_NO_INSTANCE_CREATE         TYPE FLAG.
*DATA P_DESIRED_STATE              TYPE R3STATE.
*DATA P_GEN_FLAG                   TYPE GENFLAG.
*DATA P_CALLED_BY_XSLT_MAINTENANCE TYPE FLAG.
*DATA P_OBJ                        TYPE REF TO CL_O2_API_XSLTDESC.

*DATA P_ATTRIBUTES                 TYPE O2XSLTATTR.
*DATA P_OTR_TEXTS                  TYPE TXSLTOTR.
*DATA P_STATE                      TYPE R3STATE.

    TRY.
        IF progname IS NOT INITIAL.
          gv_progname = progname.
        ENDIF.
        IF devclass IS NOT INITIAL.
          gv_devclass = devclass.
        ENDIF.

        IF gv_progname IS INITIAL OR gv_devclass IS INITIAL.
          RAISE EXCEPTION TYPE /ensx/cx_xslt
            EXPORTING
              previous = lcx_root
              textid   = textid.
        ENDIF.

        l_xsltdef-xsltdesc = gv_progname.
        l_xsltdef-devclass = gv_devclass.

        IF me->st_program_exists( ) = abap_false.
          RAISE EXCEPTION TYPE /ensx/cx_xslt
            EXPORTING
              previous = lcx_root
              textid   = textid.
        ENDIF.

        cl_o2_api_xsltdesc=>load(
          EXPORTING
            p_xslt_desc                  = l_xsltdef-xsltdesc
*    p_no_instance_create         = p_no_instance_create
*    p_desired_state              = p_desired_state
*    p_gen_flag                   = p_gen_flag
*    p_called_by_xslt_maintenance = p_called_by_xslt_maintenance
          IMPORTING
            p_obj                        = go_xsltdesc
            p_source                     = l_source
            p_attributes                 = gs_attributes
*    p_otr_texts                  = p_otr_texts
            p_state                      = l_state
          EXCEPTIONS
            error_occured                = 1
            not_existing                 = 2
            permission_failure           = 3
            version_not_found            = 4
            OTHERS                       = 5
               ).
        IF sy-subrc <> 0.
                  textid = /ensx/cl_abap_exceptions=>_symessage_to_textid( ).
          RAISE EXCEPTION TYPE /ensx/cx_xslt
            EXPORTING
              previous = lcx_root
              textid   = textid.
        ENDIF.


        gv_source = me->_source2string( source = l_source ).

      CATCH /ensx/cx_xslt INTO lcx_root.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
    ENDTRY.

  ENDMETHOD.


METHOD st_program_pretty_print.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
  DATA: lcx_root       TYPE REF TO cx_root.
  DATA: textid         TYPE scx_t100key.

  TRY.
      if go_xsltdesc is not bound.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

      CALL METHOD go_xsltdesc->pretty_print
        EXCEPTIONS
          not_possible = 1
          OTHERS       = 2.
      IF sy-subrc <> 0.
                textid = /ensx/cl_abap_exceptions=>_symessage_to_textid( ).
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

    CATCH /ensx/cx_xslt INTO lcx_root.
      RAISE EXCEPTION TYPE /ensx/cx_xslt
        EXPORTING
          previous = lcx_root
          textid   = textid.
  ENDTRY.


ENDMETHOD.


  METHOD st_program_save.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
    DATA: lcx_root       TYPE REF TO cx_root.
    DATA: textid         TYPE scx_t100key.

    TRY.
        IF go_xsltdesc IS NOT BOUND.
          RAISE EXCEPTION TYPE /ensx/cx_xslt
            EXPORTING
              previous = lcx_root
              textid   = textid.
        ENDIF.

        CALL METHOD go_xsltdesc->save
          EXPORTING
*           I_SOURCE_STATE            = C_REPORT_STATE_INACTIVE
            i_suppress_corr_insert    = space
            i_suppress_tree_placement = space
          CHANGING
            p_transport_request       = gv_transport
          EXCEPTIONS
            error_occured             = 1
            object_not_changeable     = 2
            object_invalid            = 3
            action_cancelled          = 4
            permission_failure        = 5
            OTHERS                    = 6.
        IF sy-subrc <> 0.
                  textid = /ensx/cl_abap_exceptions=>_symessage_to_textid( ).
          RAISE EXCEPTION TYPE /ensx/cx_xslt
            EXPORTING
              previous = lcx_root
              textid   = textid.
        ENDIF.

      CATCH /ensx/cx_xslt INTO lcx_root.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
    ENDTRY.


  ENDMETHOD.


METHOD st_program_set_changeable.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
  DATA: lcx_root       TYPE REF TO cx_root.
  DATA: textid         TYPE scx_t100key.

  TRY.
      IF go_xsltdesc IS NOT BOUND.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

      CALL METHOD go_xsltdesc->set_changeable
        EXPORTING
          p_changeable                = changeable
        EXCEPTIONS
          object_invalid              = 1
          object_just_created         = 2
          object_modified             = 3
          object_already_unlocked     = 4
          object_already_changeable   = 5
          action_cancelled            = 6
          object_locked_by_other_user = 7
          error_occured               = 8
          permission_failure          = 9
          OTHERS                      = 10.

      IF sy-subrc <> 0.
        textid = /ensx/cl_abap_exceptions=>_symessage_to_textid( ).
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

    CATCH /ensx/cx_xslt INTO lcx_root.
      RAISE EXCEPTION TYPE /ensx/cx_xslt
        EXPORTING
          previous = lcx_root
          textid   = textid.
  ENDTRY.


ENDMETHOD.


METHOD st_program_update.

*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
  DATA: lcx_root       TYPE REF TO cx_root.
  DATA: textid         TYPE scx_t100key.
  DATA: l_xsltdef       TYPE o2xsltattr.
  DATA: xsltdesc        TYPE REF TO cl_o2_api_xsltdesc .
  DATA: if_exists       TYPE c.
  DATA: l_source        TYPE o2pageline_table.
  TRY.


      IF progname IS NOT INITIAL.
        gv_progname = progname.
      ENDIF.
      IF devclass IS NOT INITIAL.
        gv_devclass = devclass.
      ENDIF.

      IF gv_progname IS INITIAL OR gv_devclass IS INITIAL
        OR gv_source IS INITIAL.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

      IF me->st_program_exists( ) = abap_true.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

      l_xsltdef-xsltdesc = gv_progname.
      l_xsltdef-devclass = gv_devclass.

      l_source = me->_string2source( string = gv_source ).

      CREATE OBJECT go_xsltdesc
        EXPORTING
          p_source = l_source
          p_create = ''
          p_attr   = l_xsltdef
*         P_OTR_TEXTS =
          p_state  = ' '
*         P_GEN_FLAG =
*         P_CALLED_BY_XSLT_MAINTENANCE =
        .
      IF me->st_program_exists( ) = abap_false.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

      CALL FUNCTION 'XSLT_MAINTENANCE'
        EXPORTING
          i_operation        = 'MODI_ACT'
          i_xslt_attributes  = l_xsltdef
          i_xslt_source      = l_source
          i_gen_flag         = 'X'
        EXCEPTIONS
          invalid_name       = 1
          not_existing       = 2
          lock_failure       = 3
          permission_failure = 4
          error_occured      = 5
          syntax_errors      = 6
          cancelled          = 7
          data_missing       = 8
          version_not_found  = 9
          OTHERS             = 10.

      IF sy-subrc <> 0.
        textid = /ensx/cl_abap_exceptions=>_symessage_to_textid( ).
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
      ENDIF.

      me->st_program_set_changeable( abap_true ).

      me->st_program_pretty_print( ).

      me->st_program_save( ).

      me->st_program_activate( ).

    CATCH /ensx/cx_xslt INTO lcx_root.
      RAISE EXCEPTION TYPE /ensx/cx_xslt
        EXPORTING
          previous = lcx_root
          textid   = textid.
  ENDTRY.

ENDMETHOD.


  METHOD _source2string.
    FIELD-SYMBOLS <line> TYPE o2pageline.
    LOOP AT source ASSIGNING <line>.
      CONCATENATE string <line> cl_abap_char_utilities=>cr_lf INTO string RESPECTING BLANKS.
    ENDLOOP.
    ENDMETHOD.


  METHOD _string2source.
  DATA: pos TYPE i,
        source_string TYPE String,
        source_before TYPE String,
        delim TYPE String.

  source_string = string.
  CONCATENATE '.' cl_abap_char_utilities=>cr_lf '.' INTO delim.

  DO.
    pos = 1.
    SEARCH source_string FOR delim STARTING AT pos.
    IF sy-subrc = 0.
        pos = sy-fdpos + pos - 1.
        source_before = source_string(pos).
        IF pos = 0.
          APPEND INITIAL LINE TO source.
        ELSE.
          APPEND source_before TO source.
        ENDIF.
        pos = pos + 2.
        shift source_string by pos places.
    ELSE.
      EXIT.
    ENDIF.
  ENDDO.
  append source_string TO source.
  ENDMETHOD.


  METHOD _xslt_api_create.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
    DATA: lcx_root       TYPE REF TO cx_root.
    DATA: textid         TYPE scx_t100key.
    DATA: l_xsltdef      TYPE o2xsltattr.
    DATA: l_source       TYPE o2pageline_table.
*DATA P_CREATE                     TYPE CHAR1.
*DATA P_ATTR                       TYPE O2XSLTATTR.
*DATA P_OTR_TEXTS                  TYPE TXSLTOTR.
*DATA P_STATE                      TYPE R3STATE.
*DATA P_GEN_FLAG                   TYPE GENFLAG.
*DATA P_CALLED_BY_XSLT_MAINTENANCE TYPE FLAG.
*DATA P_VERI_MODE                  TYPE FLAG.

    TRY.
        IF gv_progname IS INITIAL OR gv_devclass IS INITIAL
          OR gv_source IS INITIAL.
          RAISE EXCEPTION TYPE /ensx/cx_xslt
            EXPORTING
              previous = lcx_root
              textid   = textid.
        ENDIF.

        l_xsltdef-xsltdesc = gv_progname.
        l_xsltdef-devclass = gv_devclass.

        l_source = me->_string2source( string = gv_source ).


        CREATE OBJECT go_xsltdesc
          EXPORTING
            p_source = l_source
*           p_create = p_create
            p_attr   = l_xsltdef
*           p_otr_texts = p_otr_texts
*           p_state  = C_STATE_INITIAL
*           p_gen_flag = p_gen_flag
*           p_called_by_xslt_maintenance = p_called_by_xslt_maintenance
*           p_veri_mode = p_veri_mode
          .

      CATCH /ensx/cx_xslt INTO lcx_root.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
    ENDTRY.

  ENDMETHOD.
ENDCLASS.