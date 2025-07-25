CLASS zcx_dynscreen_value_error DEFINITION PUBLIC INHERITING FROM zcx_dynscreen_dyna_chk_base FINAL CREATE PUBLIC.
  PUBLIC SECTION.
    CONSTANTS:
      BEGIN OF zcx_dynscreen_value_error,
        msgid TYPE symsgid VALUE 'Z_DYNSCREEN',
        msgno TYPE symsgno VALUE '010',
        attr1 TYPE scx_attrname VALUE '' ##MG_MISSING,
        attr2 TYPE scx_attrname VALUE '' ##MG_MISSING,
        attr3 TYPE scx_attrname VALUE '' ##MG_MISSING,
        attr4 TYPE scx_attrname VALUE '' ##MG_MISSING,
      END OF zcx_dynscreen_value_error,
      BEGIN OF value_error_with_prev,
        msgid TYPE symsgid VALUE 'Z_DYNSCREEN',
        msgno TYPE symsgno VALUE '010',
        attr1 TYPE scx_attrname VALUE 'PREVIOUS_ERROR+000(50)' ##MG_MIS_ATT,
        attr2 TYPE scx_attrname VALUE 'PREVIOUS_ERROR+050(50)' ##MG_MIS_ATT,
        attr3 TYPE scx_attrname VALUE 'PREVIOUS_ERROR+100(50)' ##MG_MIS_ATT,
        attr4 TYPE scx_attrname VALUE 'PREVIOUS_ERROR+150(50)' ##MG_MIS_ATT,
      END OF value_error_with_prev,
      BEGIN OF no_value_provided,
        msgid TYPE symsgid VALUE 'Z_DYNSCREEN',
        msgno TYPE symsgno VALUE '011',
        attr1 TYPE scx_attrname VALUE '',
        attr2 TYPE scx_attrname VALUE '',
        attr3 TYPE scx_attrname VALUE '',
        attr4 TYPE scx_attrname VALUE '',
      END OF no_value_provided,
      BEGIN OF invalid_value,
        msgid TYPE symsgid VALUE 'Z_DYNSCREEN',
        msgno TYPE symsgno VALUE '012',
        attr1 TYPE scx_attrname VALUE 'VALUE',
        attr2 TYPE scx_attrname VALUE '',
        attr3 TYPE scx_attrname VALUE '',
        attr4 TYPE scx_attrname VALUE '',
      END OF invalid_value,
      BEGIN OF invalid_conversion,
        msgid TYPE symsgid VALUE 'Z_DYNSCREEN',
        msgno TYPE symsgno VALUE '013',
        attr1 TYPE scx_attrname VALUE 'CONVERSION',
        attr2 TYPE scx_attrname VALUE '',
        attr3 TYPE scx_attrname VALUE '',
        attr4 TYPE scx_attrname VALUE '',
      END OF invalid_conversion,
      BEGIN OF set_value_write_conv,
        msgid TYPE symsgid VALUE 'Z_DYNSCREEN',
        msgno TYPE symsgno VALUE '014',
        attr1 TYPE scx_attrname VALUE '',
        attr2 TYPE scx_attrname VALUE '',
        attr3 TYPE scx_attrname VALUE '',
        attr4 TYPE scx_attrname VALUE '',
      END OF set_value_write_conv,
      BEGIN OF get_value_write_conv_selopt,
        msgid TYPE symsgid VALUE 'Z_DYNSCREEN',
        msgno TYPE symsgno VALUE '015',
        attr1 TYPE scx_attrname VALUE '',
        attr2 TYPE scx_attrname VALUE '',
        attr3 TYPE scx_attrname VALUE '',
        attr4 TYPE scx_attrname VALUE '',
      END OF get_value_write_conv_selopt.
    DATA:
      previous_error TYPE mty_previous_error READ-ONLY,
      value          TYPE string READ-ONLY,
      parent_class   TYPE seoclsname READ-ONLY,
      conversion     TYPE c LENGTH 1 READ-ONLY.
    METHODS:
      constructor IMPORTING textid       LIKE if_t100_message=>t100key OPTIONAL
                            previous     LIKE previous OPTIONAL
                            parent_class TYPE REF TO object OPTIONAL
                            value        TYPE any OPTIONAL
                            conversion   LIKE conversion OPTIONAL.
  PROTECTED SECTION.
  PRIVATE SECTION.
ENDCLASS.



CLASS zcx_dynscreen_value_error IMPLEMENTATION.

  METHOD constructor ##ADT_SUPPRESS_GENERATION.
* ---------------------------------------------------------------------
    super->constructor( previous = previous ).

* ---------------------------------------------------------------------
    CLEAR me->textid.

* ---------------------------------------------------------------------
    me->parent_class = get_class_name( parent_class ).
    me->conversion   = conversion.
    me->value        = value.

* ---------------------------------------------------------------------
    IF textid IS INITIAL.
      if_t100_message~t100key = zcx_dynscreen_value_error.
    ELSE.
      if_t100_message~t100key = textid.
    ENDIF.

* ---------------------------------------------------------------------
    IF textid = value_error_with_prev.
      previous_error = get_previous_text( ).
    ENDIF.

* ---------------------------------------------------------------------
  ENDMETHOD.

ENDCLASS.