*&---------------------------------------------------------------------*
*& Report ZCHANGE_PACKAGE
*&---------------------------------------------------------------------*
*&
*&---------------------------------------------------------------------*
REPORT zchange_package.

*--------------------------------------------------------------------*
** Global objects
*--------------------------------------------------------------------*
TABLES: e071, euobjedit.

DATA: gt_e071        TYPE TABLE OF e071,
      gt_tadir       TYPE TABLE OF tadir,
      gt_alv_9000    TYPE TABLE OF zsalv,
      go_alv_9000    TYPE REF TO cl_gui_alv_grid,
      go_cont_9000   TYPE REF TO cl_gui_docking_container,
      go_parent_9000 TYPE REF TO cl_gui_container.

*--------------------------------------------------------------------*
** Parameter screen
*--------------------------------------------------------------------*
SELECTION-SCREEN: BEGIN OF BLOCK b1 WITH FRAME TITLE TEXT-001.

  SELECT-OPTIONS: s_trkorr FOR e071-trkorr.

SELECTION-SCREEN: END OF BLOCK b1.

*--------------------------------------------------------------------*
** Main event
*--------------------------------------------------------------------*
START-OF-SELECTION.

* Display ALV
  CALL SCREEN 9000.

*&---------------------------------------------------------------------*
*& Module STATUS_9000 OUTPUT
*&---------------------------------------------------------------------*
*&
*&---------------------------------------------------------------------*
MODULE status_9000 OUTPUT.
  SET PF-STATUS 'STATUS_9000'.
  SET TITLEBAR 'TITLE_9000'.

  PERFORM get_data_alv_9000.

  PERFORM display_alv_9000.

ENDMODULE.
*&---------------------------------------------------------------------*
*&      Module  USER_COMMAND_9000  INPUT
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
MODULE user_command_9000 INPUT.

  CASE sy-ucomm.

    WHEN '&F03' OR '&F15' OR '&F12'.

      go_alv_9000->free( ).
      go_cont_9000->free( ).

      CALL METHOD cl_gui_cfw=>flush.

      CLEAR: go_alv_9000, go_cont_9000.

      LEAVE TO SCREEN 0.

    WHEN '&MVPACK'.

      PERFORM move_package.

  ENDCASE.

ENDMODULE.
*&---------------------------------------------------------------------*
*& Form get_data_alv_9000
*&---------------------------------------------------------------------*
*& text
*&---------------------------------------------------------------------*
*& -->  p1        text
*& <--  p2        text
*&---------------------------------------------------------------------*
FORM get_data_alv_9000 .

  DATA: lv_e071type    TYPE euobjedit-e071,
        lv_infprogram  TYPE euobjedit-infprogram,
        lv_adir_object TYPE euobjedit-tadir,
        lv_id          TYPE euobj-id.

* Get objects from request
  SELECT e071~obj_name e071~object
         tadir~devclass
    FROM e071
    INNER JOIN tadir
    ON e071~object    = tadir~object
    AND e071~obj_name = tadir~obj_name
    INTO CORRESPONDING FIELDS OF TABLE gt_alv_9000
    WHERE e071~trkorr IN s_trkorr.
  IF sy-subrc <> 0.
    LEAVE LIST-PROCESSING.
  ENDIF.

* Get type and object description
  LOOP AT gt_alv_9000 ASSIGNING FIELD-SYMBOL(<alv_9000>).

* Get object type
    lv_id = <alv_9000>-object.

    CALL FUNCTION 'REPOSITORY_OBJECT_INFO_GET'
      EXPORTING
        id                           = lv_id
      IMPORTING
        e071type                     = lv_e071type
        infprogram                   = lv_infprogram
        adir_object                  = lv_adir_object
      EXCEPTIONS
        only_one_input_par_requested = 1
        OTHERS                       = 2.
    IF sy-subrc <> 0.
      CONTINUE.
    ENDIF.

    SELECT SINGLE euobjedit~type, euobjt~singular
      FROM euobjedit
      INNER JOIN euobjt
      ON euobjedit~type = euobjt~type
      INTO @DATA(ls_euobjedit)
      WHERE euobjedit~tadir      = @lv_adir_object
        AND euobjedit~e071       = @lv_e071type
        AND euobjedit~infprogram = @lv_infprogram
        AND euobjt~spras         = @sy-langu.
    IF sy-subrc = 0.
      <alv_9000>-type     = ls_euobjedit-type.
      <alv_9000>-singular = ls_euobjedit-singular.
    ENDIF.

  ENDLOOP.

ENDFORM.
*&---------------------------------------------------------------------*
*& Form display_alv_9000
*&---------------------------------------------------------------------*
*& text
*&---------------------------------------------------------------------*
*& -->  p1        text
*& <--  p2        text
*&---------------------------------------------------------------------*
FORM display_alv_9000 .

  DATA: ls_layout  TYPE lvc_s_layo,
        ls_variant TYPE disvariant,
        lt_sort    TYPE lvc_t_sort,
        lt_fcat    TYPE lvc_t_fcat,
        ls_stable  TYPE lvc_s_stbl.

* Edit layout
  CLEAR ls_layout.
  ls_layout-sel_mode   = 'A'.
  ls_layout-cwidth_opt = abap_true.
  ls_layout-zebra      = abap_true.

* Get Field catalog
  CLEAR lt_fcat.
  CALL FUNCTION 'LVC_FIELDCATALOG_MERGE'
    EXPORTING
      i_structure_name       = 'ZSALV'
    CHANGING
      ct_fieldcat            = lt_fcat
    EXCEPTIONS
      inconsistent_interface = 1
      program_error          = 2
      OTHERS                 = 3.
  IF sy-subrc <> 0.
    MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
      WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
  ENDIF.

  LOOP AT lt_fcat ASSIGNING FIELD-SYMBOL(<fcat>).
    IF <fcat>-fieldname = 'TYPE'.
      <fcat>-no_out = abap_true.
    ELSEIF <fcat>-fieldname = 'OBJ_NAME' OR <fcat>-fieldname = 'OBJECT'.
      <fcat>-key = abap_true.
    ENDIF.
  ENDLOOP.

* Refresh ALV
  IF go_cont_9000 IS BOUND.

    go_alv_9000->set_frontend_layout( is_layout = ls_layout ).
    go_alv_9000->set_frontend_fieldcatalog( it_fieldcatalog = lt_fcat ).

    ls_stable-row = abap_true.
    ls_stable-col = abap_true.

    go_alv_9000->refresh_table_display(
      EXPORTING
        is_stable      = ls_stable         " With Stable Rows/Columns
      EXCEPTIONS
        finished       = 1                " Display was Ended (by Export)
        OTHERS         = 2  ).
    IF sy-subrc <> 0.
      MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
        WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
    ENDIF.

  ELSE.
* Display ALV for the first time

* Creates the Container for the ALV screen
    CREATE OBJECT go_cont_9000
      EXPORTING
        side      = cl_gui_docking_container=>dock_at_top
        repid     = sy-repid
        dynnr     = '9000'
        extension = 1000
      EXCEPTIONS
        OTHERS    = 6.

* Casting for the generic type
    go_parent_9000 = go_cont_9000.

* Creates Instance of ALV, referencing the Container generated above
    CREATE OBJECT go_alv_9000
      EXPORTING
        i_parent = go_parent_9000.

    ls_variant-report = sy-repid.
    ls_variant-username = sy-uname.

* Display ALV
    go_alv_9000->set_table_for_first_display(
     EXPORTING
*     i_structure_name              = 'ZSALV'
       is_variant                    = ls_variant          " Layout
       i_save                        = 'A'                 " Save Layout
       is_layout                     = ls_layout           " Layout
      CHANGING
       it_outtab                     = gt_alv_9000         " Output Table
       it_fieldcatalog               = lt_fcat             " Field Catalog
       it_sort                       = lt_sort             " Sort Criteria
     EXCEPTIONS
       invalid_parameter_combination = 1                " Wrong Parameter
       program_error                 = 2                " Program Errors
       too_many_lines                = 3                " Too many Rows in Ready for Input Grid
       OTHERS                        = 4
    ).
    IF sy-subrc <> 0.
      MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
        WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
    ENDIF.

  ENDIF.

ENDFORM.
*&---------------------------------------------------------------------*
*& Form move_package
*&---------------------------------------------------------------------*
*& Move package of selected objects
*&---------------------------------------------------------------------*
*& -->  p1        text
*& <--  p2        text
*&---------------------------------------------------------------------*
FORM move_package .

  DATA: lt_objlist TYPE TABLE OF rseuap.

* Get selected rows
  go_alv_9000->check_changed_data( ).
  go_alv_9000->get_selected_rows( IMPORTING et_index_rows = DATA(lt_index_rows) ).

  IF lines( lt_index_rows ) = 0.
    MESSAGE 'Favor selecionar uma linha para processamento'(002) TYPE 'S' DISPLAY LIKE 'E'.
    RETURN.
  ENDIF.

* Process rows
  LOOP AT lt_index_rows ASSIGNING FIELD-SYMBOL(<index_row>).
    READ TABLE gt_alv_9000 ASSIGNING FIELD-SYMBOL(<alv_9000>) INDEX <index_row>.
    IF sy-subrc <> 0.
      CONTINUE.
    ENDIF.

    CLEAR lt_objlist.
    APPEND INITIAL LINE TO lt_objlist ASSIGNING FIELD-SYMBOL(<objlist>).
    <objlist>-obj_name = <alv_9000>-obj_name.
    <objlist>-obj_type = <alv_9000>-type.

* Call standard perform to move package of object
    PERFORM move IN PROGRAM saplseap TABLES lt_objlist.

  ENDLOOP.

ENDFORM.