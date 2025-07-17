REPORT zguidrasil_init_controls.

CONSTANTS c_type_container TYPE c LENGTH 1 VALUE 'C'.
CONSTANTS c_type_control   TYPE c LENGTH 1 VALUE 'O'.

PARAMETERS p_del  AS CHECKBOX DEFAULT space.
PARAMETERS p_test AS CHECKBOX DEFAULT 'X'.

START-OF-SELECTION.
  PERFORM init.

FORM init.

  DATA(oo_class) = NEW cl_oo_class( clsname = 'ZCL_GUIDRASIL_CONTROL_BASE' ).
  DATA(subclasses) = oo_class->get_subclasses( ).
  DATA controls TYPE STANDARD TABLE OF zguidrasil_ctls.
  DATA control  TYPE zguidrasil_ctls.
  DATA seoclskey TYPE seoclskey.

  DATA class                        TYPE vseoclass.

  IF p_test = abap_false
  AND p_del = abap_true.
    "Delete controls
    DELETE FROM zguidrasil_ctls WHERE usable = abap_true.
  ENDIF.

  LOOP AT subclasses INTO DATA(subclass).
    CLEAR control.
    SELECT SINGLE * FROM zguidrasil_ctls INTO control WHERE classname = subclass-clsname.
    CHECK sy-subrc > 0.
    control-classname = subclass-clsname.
    seoclskey-clsname = subclass-clsname.

    "Get class name
    CALL FUNCTION 'SEO_CLASS_GET'
      EXPORTING
        clskey = seoclskey
      IMPORTING
        class  = class
      EXCEPTIONS
        OTHERS = 5.
    IF sy-subrc = 0.
      control-quickinfo = class-descript.
    ELSE.
      control-quickinfo = subclass-clsname.
    ENDIF.


    CASE subclass-clsname.
      WHEN 'ZCL_GUIDRASIL_DESIGN_CONTAINER'.
        CONTINUE.
      WHEN 'ZCL_GUIDRASIL_CONTROL_CUSTOM'
        OR 'ZCL_GUIDRASIL_CONTROL_DIABOX'
        OR 'ZCL_GUIDRASIL_CONTROL_DOCKING'.
        CONTINUE.
      WHEN 'ZCL_GUIDRASIL_CONTROL_SPLITTER'.
        control-type   = c_type_container.
        control-usable = abap_true.

      WHEN OTHERS.
        control-type   = c_type_control.
        control-usable = abap_true.
        CASE subclass-clsname.
          WHEN 'ZCL_GUIDRASIL_CONTROL_ALV'.
            control-iconname = 'ICON_TABLE_SETTINGS'.
          WHEN 'ZCL_GUIDRASIL_CONTROL_CALENDAR'.
            control-iconname = 'ICON_DATE'.
          WHEN 'ZCL_GUIDRASIL_CONTROL_ICON'.
            control-iconname = 'ICON_LED_GREEN'.
          WHEN 'ZCL_GUIDRASIL_CONTROL_TEXT'.
            control-iconname = 'ICON_WD_TEXT_EDIT'.
          WHEN OTHERS.
            control-iconname = 'ICON_DETAIL'.
        ENDCASE.
    ENDCASE.
    control-usable = abap_true.
    APPEND control TO controls.

    WRITE: / control-classname, 'added'.

  ENDLOOP.

  IF p_test = abap_false.
    IF controls IS INITIAL.
      WRITE: / 'no updates done'.
    ELSE.
      INSERT zguidrasil_ctls FROM TABLE controls.
      IF sy-subrc = 0.
        WRITE: / 'zguidrasil_ctls table updated'.
      ELSE.
        ROLLBACK WORK.
        WRITE: / 'error updating zguidrasil_ctls'.
      ENDIF.
    ENDIF.
  ENDIF.

ENDFORM.