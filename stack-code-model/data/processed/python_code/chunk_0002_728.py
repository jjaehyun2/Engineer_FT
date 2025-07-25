CLASS ycl_abapgit_object_dsys DEFINITION PUBLIC INHERITING FROM ycl_abapgit_objects_super FINAL.

  PUBLIC SECTION.
    INTERFACES yif_abapgit_object.
    ALIASES mo_files FOR yif_abapgit_object~mo_files.

    METHODS constructor
      IMPORTING
        is_item     TYPE yif_abapgit_definitions=>ty_item
        iv_language TYPE spras.

  PRIVATE SECTION.
    CONSTANTS: c_typ     TYPE dokhl-typ VALUE 'E',
               c_version TYPE dokhl-dokversion VALUE '0001',
               c_id      TYPE dokhl-id VALUE 'HY',
               c_dokclas TYPE doku_class VALUE 'SIMG'.
    DATA: mv_object  TYPE dokhl-object,
          mv_dokname TYPE doku_obj.

    TYPES: BEGIN OF ty_data,
             doctitle TYPE dsyst-doktitle,
             head     TYPE thead,
             lines    TYPE tline_tab,
           END OF ty_data.

    METHODS: read
      RETURNING VALUE(rs_data) TYPE ty_data.

ENDCLASS.

CLASS ycl_abapgit_object_dsys IMPLEMENTATION.

  METHOD constructor.

    super->constructor( is_item = is_item
                        iv_language = iv_language ).

    mv_object  = ms_item-obj_name.
    mv_dokname = mv_object+4(*).

  ENDMETHOD.

  METHOD yif_abapgit_object~has_changed_since.
    rv_changed = abap_true.
  ENDMETHOD.

  METHOD yif_abapgit_object~changed_by.
    rv_user = read( )-head-tdluser.
    IF rv_user IS INITIAL.
      rv_user = c_user_unknown.
    ENDIF.
  ENDMETHOD.

  METHOD yif_abapgit_object~get_metadata.
    rs_metadata = get_metadata( ).
    rs_metadata-delete_tadir = abap_true.
  ENDMETHOD.

  METHOD yif_abapgit_object~jump.

    CALL FUNCTION 'DSYS_SHOW'
      EXPORTING
        dokclass         = c_dokclas
        dokname          = mv_dokname
      EXCEPTIONS
        class_unknown    = 1
        object_not_found = 2
        OTHERS           = 3.

    IF sy-subrc <> 0.
      ycx_abapgit_exception=>raise( 'error from DSYS_EDIT' ).
    ENDIF.

  ENDMETHOD.

  METHOD yif_abapgit_object~exists.

    SELECT SINGLE object FROM dokil INTO mv_object
           WHERE id   = c_id
           AND object = mv_object.                      "#EC CI_GENBUFF

    rv_bool = boolc( sy-subrc = 0 ).

  ENDMETHOD.

  METHOD yif_abapgit_object~delete.

    CALL FUNCTION 'DOCU_DEL'
      EXPORTING
        id       = c_id
        langu    = mv_language
        object   = mv_object
        typ      = c_typ
      EXCEPTIONS
        ret_code = 1
        OTHERS   = 2.

    IF sy-subrc <> 0.
      ycx_abapgit_exception=>raise( 'error from DOCU_DEL' ).
    ENDIF.

  ENDMETHOD.

  METHOD yif_abapgit_object~serialize.

    DATA: ls_data   TYPE ty_data.

    ls_data = read( ).

    CLEAR: ls_data-head-tdfuser,
           ls_data-head-tdfreles,
           ls_data-head-tdfdate,
           ls_data-head-tdftime,
           ls_data-head-tdluser,
           ls_data-head-tdlreles,
           ls_data-head-tdldate,
           ls_data-head-tdltime.

    io_xml->add( iv_name = 'DSYS'
                 ig_data = ls_data ).

  ENDMETHOD.

  METHOD yif_abapgit_object~deserialize.

    DATA: ls_data TYPE ty_data.

    io_xml->read( EXPORTING iv_name = 'DSYS'
                  CHANGING cg_data = ls_data ).

    CALL FUNCTION 'DOCU_UPDATE'
      EXPORTING
        head    = ls_data-head
        state   = 'A'
        typ     = c_typ
        version = c_version
      TABLES
        line    = ls_data-lines.

    tadir_insert( iv_package ).

  ENDMETHOD.

  METHOD yif_abapgit_object~compare_to_remote_version.
    CREATE OBJECT ro_comparison_result TYPE ycl_abapgit_comparison_null.
  ENDMETHOD.

  METHOD read.

    CALL FUNCTION 'DOCU_READ'
      EXPORTING
        id       = c_id
        langu    = mv_language
        object   = mv_object
        typ      = c_typ
        version  = c_version
      IMPORTING
        doktitle = rs_data-doctitle
        head     = rs_data-head
      TABLES
        line     = rs_data-lines.

  ENDMETHOD.

  METHOD yif_abapgit_object~is_locked.

    rv_is_locked = abap_false.

  ENDMETHOD.

ENDCLASS.