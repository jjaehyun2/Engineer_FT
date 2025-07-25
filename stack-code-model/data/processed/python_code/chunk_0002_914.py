CLASS zcl_abapgit_object_fugr DEFINITION PUBLIC INHERITING FROM zcl_abapgit_objects_program FINAL.

  PUBLIC SECTION.
    INTERFACES zif_abapgit_object.
    ALIASES mo_files FOR zif_abapgit_object~mo_files.

  PRIVATE SECTION.
    TYPES: ty_rs38l_incl_tt TYPE STANDARD TABLE OF rs38l_incl WITH DEFAULT KEY.

    TYPES: BEGIN OF ty_function,
             funcname          TYPE rs38l_fnam,
             global_flag       TYPE rs38l-global,
             remote_call       TYPE rs38l-remote,
             update_task       TYPE rs38l-utask,
             short_text        TYPE tftit-stext,
             remote_basxml     TYPE rs38l-basxml_enabled,
             import            TYPE STANDARD TABLE OF rsimp WITH DEFAULT KEY,
             changing          TYPE STANDARD TABLE OF rscha WITH DEFAULT KEY,
             export            TYPE STANDARD TABLE OF rsexp WITH DEFAULT KEY,
             tables            TYPE STANDARD TABLE OF rstbl WITH DEFAULT KEY,
             exception         TYPE STANDARD TABLE OF rsexc WITH DEFAULT KEY,
             documentation     TYPE STANDARD TABLE OF rsfdo WITH DEFAULT KEY,
             exception_classes TYPE abap_bool,
           END OF ty_function.

    TYPES: ty_function_tt TYPE STANDARD TABLE OF ty_function WITH DEFAULT KEY.

    METHODS main_name
      RETURNING VALUE(rv_program) TYPE program
      RAISING   zcx_abapgit_exception.

    METHODS functions
      RETURNING VALUE(rt_functab) TYPE ty_rs38l_incl_tt
      RAISING   zcx_abapgit_exception.

    METHODS includes
      RETURNING VALUE(rt_includes) TYPE rso_t_objnm
      RAISING   zcx_abapgit_exception.

    METHODS serialize_functions
      RETURNING VALUE(rt_functions) TYPE ty_function_tt
      RAISING   zcx_abapgit_exception.

    METHODS deserialize_functions
      IMPORTING it_functions TYPE ty_function_tt
      RAISING   zcx_abapgit_exception.

    METHODS serialize_xml
      IMPORTING io_xml TYPE REF TO zcl_abapgit_xml_output
      RAISING   zcx_abapgit_exception.

    METHODS deserialize_xml
      IMPORTING io_xml     TYPE REF TO zcl_abapgit_xml_input
                iv_package TYPE devclass
      RAISING   zcx_abapgit_exception.

    METHODS serialize_includes
      RAISING zcx_abapgit_exception.

    METHODS deserialize_includes
      IMPORTING io_xml     TYPE REF TO zcl_abapgit_xml_input
                iv_package TYPE devclass
      RAISING   zcx_abapgit_exception.

    METHODS are_exceptions_class_based
      IMPORTING iv_function_name TYPE rs38l_fnam
      RETURNING VALUE(rv_return) TYPE abap_bool
      RAISING   zcx_abapgit_exception.

ENDCLASS.



CLASS ZCL_ABAPGIT_OBJECT_FUGR IMPLEMENTATION.


  METHOD are_exceptions_class_based.
    DATA:
      lt_dokumentation    TYPE TABLE OF funct,
      lt_exception_list   TYPE TABLE OF rsexc,
      lt_export_parameter TYPE TABLE OF rsexp,
      lt_import_parameter TYPE TABLE OF rsimp,
      lt_tables_parameter TYPE TABLE OF rstbl.

    CALL FUNCTION 'FUNCTION_IMPORT_DOKU'
      EXPORTING
        funcname           = iv_function_name
      IMPORTING
        exception_class    = rv_return
      TABLES
        dokumentation      = lt_dokumentation
        exception_list     = lt_exception_list
        export_parameter   = lt_export_parameter
        import_parameter   = lt_import_parameter
        tables_parameter   = lt_tables_parameter
      EXCEPTIONS
        error_message      = 1
        function_not_found = 2
        invalid_name       = 3
        OTHERS             = 4.
    IF sy-subrc <> 0.
      zcx_abapgit_exception=>raise( 'Error from FUNCTION_IMPORT_DOKU' ).
    ENDIF.
  ENDMETHOD.


  METHOD deserialize_functions.

    DATA: lv_include   TYPE rs38l-include,
          lv_area      TYPE rs38l-area,
          lv_group     TYPE rs38l-area,
          lv_namespace TYPE rs38l-namespace,
          lt_source    TYPE TABLE OF abaptxt255.

    FIELD-SYMBOLS: <ls_func> LIKE LINE OF it_functions.

    LOOP AT it_functions ASSIGNING <ls_func>.

      lt_source = mo_files->read_abap( iv_extra = <ls_func>-funcname ).

      lv_area = ms_item-obj_name.

      CALL FUNCTION 'FUNCTION_INCLUDE_SPLIT'
        EXPORTING
          complete_area                = lv_area
        IMPORTING
          namespace                    = lv_namespace
          group                        = lv_group
        EXCEPTIONS
          OTHERS                       = 12.

      IF sy-subrc <> 0.
        zcx_abapgit_exception=>raise( 'error from FUNCTION_INCLUDE_SPLIT' ).
      ENDIF.

      CALL FUNCTION 'FUNCTION_EXISTS'
        EXPORTING
          funcname           = <ls_func>-funcname
        IMPORTING
          include            = lv_include
        EXCEPTIONS
          function_not_exist = 1.
      IF sy-subrc = 0.
* delete the function module to make sure the parameters are updated
* havent found a nice way to update the paramters
        CALL FUNCTION 'FUNCTION_DELETE'
          EXPORTING
            funcname                 = <ls_func>-funcname
            suppress_success_message = abap_true
          EXCEPTIONS
            error_message            = 1
            OTHERS                   = 2.
        IF sy-subrc <> 0.
          zcx_abapgit_exception=>raise( 'error from FUNCTION_DELETE' ).
        ENDIF.
      ENDIF.

      CALL FUNCTION 'RS_FUNCTIONMODULE_INSERT'
        EXPORTING
          funcname                = <ls_func>-funcname
          function_pool           = lv_group
          interface_global        = <ls_func>-global_flag
          remote_call             = <ls_func>-remote_call
          short_text              = <ls_func>-short_text
          update_task             = <ls_func>-update_task
          exception_class         = <ls_func>-exception_classes
          namespace               = lv_namespace
          remote_basxml_supported = <ls_func>-remote_basxml
        IMPORTING
          function_include        = lv_include
        TABLES
          import_parameter        = <ls_func>-import
          export_parameter        = <ls_func>-export
          tables_parameter        = <ls_func>-tables
          changing_parameter      = <ls_func>-changing
          exception_list          = <ls_func>-exception
          parameter_docu          = <ls_func>-documentation
        EXCEPTIONS
          double_task             = 1
          error_message           = 2
          function_already_exists = 3
          invalid_function_pool   = 4
          invalid_name            = 5
          too_many_functions      = 6
          no_modify_permission    = 7
          no_show_permission      = 8
          enqueue_system_failure  = 9
          canceled_in_corr        = 10
          OTHERS                  = 11.
      IF sy-subrc <> 0.
        zcx_abapgit_exception=>raise( |error from RS_FUNCTIONMODULE_INSERT: {
          sy-subrc } { sy-msgid }{ sy-msgno }| ).
      ENDIF.

      INSERT REPORT lv_include FROM lt_source.
    ENDLOOP.

  ENDMETHOD.                    "deserialize_functions


  METHOD deserialize_includes.

    DATA: lo_xml       TYPE REF TO zcl_abapgit_xml_input,
          ls_progdir   TYPE ty_progdir,
          lt_includes  TYPE rso_t_objnm,
          lt_tpool     TYPE textpool_table,
          lt_tpool_ext TYPE zif_abapgit_definitions=>ty_tpool_tt,
          lt_source    TYPE TABLE OF abaptxt255.

    FIELD-SYMBOLS: <lv_include> LIKE LINE OF lt_includes.


    tadir_insert( iv_package ).

    io_xml->read( EXPORTING iv_name = 'INCLUDES'
                  CHANGING cg_data = lt_includes ).

    LOOP AT lt_includes ASSIGNING <lv_include>.

      lt_source = mo_files->read_abap( iv_extra = <lv_include> ).

      lo_xml = mo_files->read_xml( <lv_include> ).

      lo_xml->read( EXPORTING iv_name = 'PROGDIR'
                    CHANGING cg_data = ls_progdir ).

      lo_xml->read( EXPORTING iv_name = 'TPOOL'
                    CHANGING cg_data = lt_tpool_ext ).
      lt_tpool = read_tpool( lt_tpool_ext ).

      deserialize_program( is_progdir = ls_progdir
                           it_source  = lt_source
                           it_tpool   = lt_tpool
                           iv_package = iv_package ).

      deserialize_textpool( iv_program    = <lv_include>
                            it_tpool      = lt_tpool
                            iv_is_include = abap_true ).

    ENDLOOP.

  ENDMETHOD.                    "deserialize_includes


  METHOD deserialize_xml.

    DATA: lv_complete  TYPE rs38l-area,
          lv_namespace TYPE rs38l-namespace,
          lv_areat     TYPE tlibt-areat,
          lv_stext     TYPE tftit-stext,
          lv_group     TYPE rs38l-area.


    lv_complete = ms_item-obj_name.

    CALL FUNCTION 'FUNCTION_INCLUDE_SPLIT'
      EXPORTING
        complete_area                = lv_complete
      IMPORTING
        namespace                    = lv_namespace
        group                        = lv_group
      EXCEPTIONS
        include_not_exists           = 1
        group_not_exists             = 2
        no_selections                = 3
        no_function_include          = 4
        no_function_pool             = 5
        delimiter_wrong_position     = 6
        no_customer_function_group   = 7
        no_customer_function_include = 8
        reserved_name_customer       = 9
        namespace_too_long           = 10
        area_length_error            = 11
        OTHERS                       = 12.
    IF sy-subrc <> 0.
      zcx_abapgit_exception=>raise( 'error from FUNCTION_INCLUDE_SPLIT' ).
    ENDIF.

    io_xml->read( EXPORTING iv_name = 'AREAT'
                  CHANGING cg_data = lv_areat ).
    lv_stext = lv_areat.

    CALL FUNCTION 'RS_FUNCTION_POOL_INSERT'
      EXPORTING
        function_pool           = lv_group
        short_text              = lv_stext
        namespace               = lv_namespace
        devclass                = iv_package
      EXCEPTIONS
        name_already_exists     = 1
        name_not_correct        = 2
        function_already_exists = 3
        invalid_function_pool   = 4
        invalid_name            = 5
        too_many_functions      = 6
        no_modify_permission    = 7
        no_show_permission      = 8
        enqueue_system_failure  = 9
        canceled_in_corr        = 10
        undefined_error         = 11
        OTHERS                  = 12.
    IF sy-subrc <> 0 AND sy-subrc <> 1 AND sy-subrc <> 3.
* todo, change description
      zcx_abapgit_exception=>raise( 'error from RS_FUNCTION_POOL_INSERT' ).
    ENDIF.

  ENDMETHOD.                    "deserialize_xml


  METHOD functions.

    DATA: lv_area TYPE rs38l-area.


    lv_area = ms_item-obj_name.

    CALL FUNCTION 'RS_FUNCTION_POOL_CONTENTS'
      EXPORTING
        function_pool           = lv_area
      TABLES
        functab                 = rt_functab
      EXCEPTIONS
        function_pool_not_found = 1
        OTHERS                  = 2.
    IF sy-subrc <> 0.
      zcx_abapgit_exception=>raise( 'Error from RS_FUNCTION_POOL_CONTENTS' ).
    ENDIF.

    SORT rt_functab BY funcname ASCENDING.
    DELETE ADJACENT DUPLICATES FROM rt_functab COMPARING funcname.

  ENDMETHOD.                    "functions


  METHOD includes.

    TYPES: BEGIN OF ty_reposrc,
             progname TYPE reposrc-progname,
             cnam     TYPE reposrc-cnam,
           END OF ty_reposrc.

    DATA: lt_reposrc   TYPE STANDARD TABLE OF ty_reposrc WITH DEFAULT KEY,
          ls_reposrc   LIKE LINE OF lt_reposrc,
          lv_program   TYPE program,
          lv_offset_ns TYPE i,
          lv_tabix     LIKE sy-tabix,
          lt_functab   TYPE ty_rs38l_incl_tt.

    FIELD-SYMBOLS: <lv_include> LIKE LINE OF rt_includes,
                   <ls_func>    LIKE LINE OF lt_functab.


    lv_program = main_name( ).
    lt_functab = functions( ).

    CALL FUNCTION 'RS_GET_ALL_INCLUDES'
      EXPORTING
        program      = lv_program
*       WITH_RESERVED_INCLUDES =
*       WITH_CLASS_INCLUDES    = ' ' hmm, todo
      TABLES
        includetab   = rt_includes
      EXCEPTIONS
        not_existent = 1
        no_program   = 2
        OTHERS       = 3.
    IF sy-subrc <> 0.
      zcx_abapgit_exception=>raise( 'Error from RS_GET_ALL_INCLUDES' ).
    ENDIF.

    LOOP AT lt_functab ASSIGNING <ls_func>.
      DELETE TABLE rt_includes FROM <ls_func>-include.
    ENDLOOP.

* handle generated maintenance views
    APPEND INITIAL LINE TO rt_includes ASSIGNING <lv_include>.
    IF ms_item-obj_name(1) <> '/'.
      "FGroup name does not contain a namespace
      <lv_include> = |L{ ms_item-obj_name }T00|.
    ELSE.
      "FGroup name contains a namespace
      lv_offset_ns = find( val = ms_item-obj_name+1 sub = '/' ).
      lv_offset_ns = lv_offset_ns + 2.
      <lv_include> = |{ ms_item-obj_name(lv_offset_ns) }L{ ms_item-obj_name+lv_offset_ns }T00|.
    ENDIF.

    IF lines( rt_includes ) > 0.
      SELECT progname cnam FROM reposrc
        INTO TABLE lt_reposrc
        FOR ALL ENTRIES IN rt_includes
        WHERE progname = rt_includes-table_line
        AND r3state = 'A'.
      SORT lt_reposrc BY progname ASCENDING.
    ENDIF.

    LOOP AT rt_includes ASSIGNING <lv_include>.
      lv_tabix = sy-tabix.

* skip SAP standard includes and also make sure the include exists
      READ TABLE lt_reposrc INTO ls_reposrc
        WITH KEY progname = <lv_include> BINARY SEARCH.
      IF sy-subrc <> 0 OR ls_reposrc-cnam = 'SAP'.
        DELETE rt_includes INDEX lv_tabix.
      ENDIF.

    ENDLOOP.

    APPEND lv_program TO rt_includes.

  ENDMETHOD.                    "includes


  METHOD main_name.

    DATA: lv_area      TYPE rs38l-area,
          lv_namespace TYPE rs38l-namespace,
          lv_group     TYPE rs38l-area.


    lv_area = ms_item-obj_name.

    CALL FUNCTION 'FUNCTION_INCLUDE_SPLIT'
      EXPORTING
        complete_area                = lv_area
      IMPORTING
        namespace                    = lv_namespace
        group                        = lv_group
      EXCEPTIONS
        include_not_exists           = 1
        group_not_exists             = 2
        no_selections                = 3
        no_function_include          = 4
        no_function_pool             = 5
        delimiter_wrong_position     = 6
        no_customer_function_group   = 7
        no_customer_function_include = 8
        reserved_name_customer       = 9
        namespace_too_long           = 10
        area_length_error            = 11
        OTHERS                       = 12.
    IF sy-subrc <> 0.
      zcx_abapgit_exception=>raise( 'Error from FUNCTION_INCLUDE_SPLIT' ).
    ENDIF.

    CONCATENATE lv_namespace 'SAPL' lv_group INTO rv_program.

  ENDMETHOD.                    "main_name


  METHOD serialize_functions.

    DATA:
      lt_source     TYPE TABLE OF rssource,
      lt_functab    TYPE ty_rs38l_incl_tt,
      lt_new_source TYPE rsfb_source,
      ls_function   LIKE LINE OF rt_functions.

    FIELD-SYMBOLS: <ls_func> LIKE LINE OF lt_functab.


    lt_functab = functions( ).

    LOOP AT lt_functab ASSIGNING <ls_func>.
* fm RPY_FUNCTIONMODULE_READ does not support source code
* lines longer than 72 characters
      CLEAR ls_function.
      MOVE-CORRESPONDING <ls_func> TO ls_function.

      CLEAR lt_new_source.
      CLEAR lt_source.

      CALL FUNCTION 'RPY_FUNCTIONMODULE_READ_NEW'
        EXPORTING
          functionname            = <ls_func>-funcname
        IMPORTING
          global_flag             = ls_function-global_flag
          remote_call             = ls_function-remote_call
          update_task             = ls_function-update_task
          short_text              = ls_function-short_text
          remote_basxml_supported = ls_function-remote_basxml
        TABLES
          import_parameter        = ls_function-import
          changing_parameter      = ls_function-changing
          export_parameter        = ls_function-export
          tables_parameter        = ls_function-tables
          exception_list          = ls_function-exception
          documentation           = ls_function-documentation
          source                  = lt_source
        CHANGING
          new_source              = lt_new_source
        EXCEPTIONS
          error_message           = 1
          function_not_found      = 2
          invalid_name            = 3
          OTHERS                  = 4.
      IF sy-subrc = 2.
        CONTINUE.
      ELSEIF sy-subrc <> 0.
        zcx_abapgit_exception=>raise( 'Error from RPY_FUNCTIONMODULE_READ_NEW' ).
      ENDIF.

      ls_function-exception_classes = are_exceptions_class_based( <ls_func>-funcname ).

      APPEND ls_function TO rt_functions.

      IF NOT lt_new_source IS INITIAL.
        mo_files->add_abap( iv_extra = <ls_func>-funcname
                            it_abap  = lt_new_source ).
      ELSE.
        mo_files->add_abap( iv_extra = <ls_func>-funcname
                            it_abap  = lt_source ).
      ENDIF.

    ENDLOOP.

  ENDMETHOD.                    "serialize_functions


  METHOD serialize_includes.

    DATA: lt_includes TYPE rso_t_objnm.

    FIELD-SYMBOLS: <lv_include> LIKE LINE OF lt_includes.


    lt_includes = includes( ).

    LOOP AT lt_includes ASSIGNING <lv_include>.

* todo, filename is not correct, a include can be used in several programs
      serialize_program( is_item    = ms_item
                         io_files   = mo_files
                         iv_program = <lv_include>
                         iv_extra   = <lv_include> ).

    ENDLOOP.

  ENDMETHOD.                    "serialize_includes


  METHOD serialize_xml.

    DATA: lt_includes TYPE rso_t_objnm,
          lv_areat    TYPE tlibt-areat.


    SELECT SINGLE areat INTO lv_areat
      FROM tlibt
      WHERE spras = mv_language
      AND area = ms_item-obj_name.        "#EC CI_GENBUFF "#EC CI_SUBRC

    lt_includes = includes( ).

    io_xml->add( iv_name = 'AREAT'
                 ig_data = lv_areat ).
    io_xml->add( iv_name = 'INCLUDES'
                 ig_data = lt_includes ).

  ENDMETHOD.                    "serialize_xml


  METHOD zif_abapgit_object~changed_by.

    TYPES: BEGIN OF ty_stamps,
             user TYPE xubname,
             date TYPE d,
             time TYPE t,
           END OF ty_stamps.

    DATA: lt_stamps   TYPE STANDARD TABLE OF ty_stamps WITH DEFAULT KEY,
          lv_program  TYPE program,
          lt_includes TYPE rso_t_objnm.

    FIELD-SYMBOLS: <ls_stamp>   LIKE LINE OF lt_stamps,
                   <lv_include> LIKE LINE OF lt_includes.


    lv_program = main_name( ).

    CALL FUNCTION 'RS_GET_ALL_INCLUDES'
      EXPORTING
        program      = lv_program
      TABLES
        includetab   = lt_includes
      EXCEPTIONS
        not_existent = 1
        no_program   = 2
        OTHERS       = 3.
    IF sy-subrc <> 0.
      zcx_abapgit_exception=>raise( 'Error from RS_GET_ALL_INCLUDES' ).
    ENDIF.

    SELECT unam AS user udat AS date utime AS time FROM reposrc
      APPENDING CORRESPONDING FIELDS OF TABLE lt_stamps
      WHERE progname = lv_program
      AND   r3state = 'A'.                                "#EC CI_SUBRC

    LOOP AT lt_includes ASSIGNING <lv_include>.
      SELECT unam AS user udat AS date utime AS time FROM reposrc
        APPENDING CORRESPONDING FIELDS OF TABLE lt_stamps
        WHERE progname = <lv_include>
        AND   r3state = 'A'.                              "#EC CI_SUBRC
    ENDLOOP.

    SELECT unam AS user udat AS date utime AS time FROM repotext " Program text pool
      APPENDING CORRESPONDING FIELDS OF TABLE lt_stamps
      WHERE progname = lv_program
      AND   r3state = 'A'.                                "#EC CI_SUBRC

    SELECT vautor AS user vdatum AS date vzeit AS time FROM eudb         " GUI
      APPENDING CORRESPONDING FIELDS OF TABLE lt_stamps
      WHERE relid = 'CU'
      AND   name  = lv_program
      AND   srtf2 = 0 ##TOO_MANY_ITAB_FIELDS.

* Screens: username not stored in D020S database table

    SORT lt_stamps BY date DESCENDING time DESCENDING.

    READ TABLE lt_stamps INDEX 1 ASSIGNING <ls_stamp>.
    IF sy-subrc = 0.
      rv_user = <ls_stamp>-user.
    ELSE.
      rv_user = c_user_unknown.
    ENDIF.

  ENDMETHOD.


  METHOD zif_abapgit_object~compare_to_remote_version.
    CREATE OBJECT ro_comparison_result TYPE zcl_abapgit_comparison_null.
  ENDMETHOD.


  METHOD zif_abapgit_object~delete.

    DATA: lv_area TYPE rs38l-area.


    lv_area = ms_item-obj_name.

    CALL FUNCTION 'RS_FUNCTION_POOL_DELETE'
      EXPORTING
        area                   = lv_area
        suppress_popups        = abap_true
        skip_progress_ind      = abap_true
      EXCEPTIONS
        canceled_in_corr       = 1
        enqueue_system_failure = 2
        function_exist         = 3
        not_executed           = 4
        no_modify_permission   = 5
        no_show_permission     = 6
        permission_failure     = 7
        pool_not_exist         = 8
        cancelled              = 9
        OTHERS                 = 10.
    IF sy-subrc <> 0.
      zcx_abapgit_exception=>raise( 'error from RS_FUNCTION_POOL_DELETE' ).
    ENDIF.

  ENDMETHOD.                    "delete


  METHOD zif_abapgit_object~deserialize.

    DATA: lv_program_name TYPE programm,
          lt_functions    TYPE ty_function_tt,
          lt_dynpros      TYPE ty_dynpro_tt,
          ls_cua          TYPE ty_cua.


    deserialize_xml(
      io_xml     = io_xml
      iv_package = iv_package ).

    io_xml->read( EXPORTING iv_name = 'FUNCTIONS'
                  CHANGING cg_data = lt_functions ).
    deserialize_functions( lt_functions ).

    deserialize_includes(
      io_xml     = io_xml
      iv_package = iv_package ).

    lv_program_name = main_name( ).

    io_xml->read( EXPORTING iv_name = 'DYNPROS'
                  CHANGING cg_data = lt_dynpros ).
    deserialize_dynpros( it_dynpros = lt_dynpros ).

    io_xml->read( EXPORTING iv_name = 'CUA'
                  CHANGING cg_data = ls_cua ).
    deserialize_cua( iv_program_name = lv_program_name
                     is_cua = ls_cua ).

  ENDMETHOD.                    "deserialize


  METHOD zif_abapgit_object~exists.

    DATA: lv_pool  TYPE tlibg-area.


    lv_pool = ms_item-obj_name.
    CALL FUNCTION 'RS_FUNCTION_POOL_EXISTS'
      EXPORTING
        function_pool   = lv_pool
      EXCEPTIONS
        pool_not_exists = 1.
    rv_bool = boolc( sy-subrc <> 1 ).

  ENDMETHOD.                    "zif_abapgit_object~exists


  METHOD zif_abapgit_object~get_metadata.
    rs_metadata = get_metadata( ).
  ENDMETHOD.                    "zif_abapgit_object~get_metadata


  METHOD zif_abapgit_object~has_changed_since.

    DATA: lt_functab  TYPE ty_rs38l_incl_tt,
          lt_includes TYPE rso_t_objnm.

    FIELD-SYMBOLS: <ls_func>         LIKE LINE OF lt_functab,
                   <lv_include_name> LIKE LINE OF lt_includes.


    lt_includes = includes( ). " Main prog also included here

    LOOP AT lt_includes ASSIGNING <lv_include_name>.
      rv_changed = check_prog_changed_since(
        iv_program   = <lv_include_name>
        iv_timestamp = iv_timestamp ).
      IF rv_changed = abap_true.
        RETURN.
      ENDIF.
    ENDLOOP.

    lt_functab = functions( ).

    LOOP AT lt_functab ASSIGNING <ls_func>.
      rv_changed = check_prog_changed_since(
        iv_program   = <ls_func>-include
        iv_timestamp = iv_timestamp ).
      IF rv_changed = abap_true.
        RETURN.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.  "zif_abapgit_object~has_changed_since


  METHOD zif_abapgit_object~jump.

    CALL FUNCTION 'RS_TOOL_ACCESS'
      EXPORTING
        operation     = 'SHOW'
        object_name   = ms_item-obj_name
        object_type   = 'FUGR'
        in_new_window = abap_true.

  ENDMETHOD.                    "jump


  METHOD zif_abapgit_object~serialize.

* function group SEUF
* function group SIFP
* function group SUNI

    DATA: lt_functions    TYPE ty_function_tt,
          ls_progdir      TYPE ty_progdir,
          lv_program_name TYPE programm,
          lt_dynpros      TYPE ty_dynpro_tt,
          ls_cua          TYPE ty_cua.

    IF zif_abapgit_object~exists( ) = abap_false.
      RETURN.
    ENDIF.

    serialize_xml( io_xml ).

    lt_functions = serialize_functions( ).
    io_xml->add( iv_name = 'FUNCTIONS'
                 ig_data = lt_functions ).

    serialize_includes( ).

    lv_program_name = main_name( ).
    ls_progdir = read_progdir( lv_program_name ).

    IF ls_progdir-subc = 'F'.
      lt_dynpros = serialize_dynpros( lv_program_name ).
      io_xml->add( iv_name = 'DYNPROS'
                   ig_data = lt_dynpros ).

      ls_cua = serialize_cua( lv_program_name ).
      io_xml->add( iv_name = 'CUA'
                   ig_data = ls_cua ).
    ENDIF.

  ENDMETHOD.                    "serialize
ENDCLASS.