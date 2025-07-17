CLASS zcl_swi_switch DEFINITION
  PUBLIC
  FINAL
  CREATE PRIVATE.

  PUBLIC SECTION.
    INTERFACES:
      zif_swi_switch.

    ALIASES:
      status FOR zif_swi_switch~status.

    CLASS-METHODS get
      IMPORTING
        iv_switch     TYPE zswi_switch_code
      RETURNING
        VALUE(result) TYPE REF TO zif_swi_switch
      RAISING
        zcx_swi_switch.

  PROTECTED SECTION.

  PRIVATE SECTION.
    CLASS-DATA:
      go_buffer TYPE REF TO lcl_buffer.

    DATA:
      ms_switch_data          TYPE zswi_switch,
      mi_custom_determination TYPE REF TO zif_swi_custom_determination.

    CLASS-METHODS initialize_buffer.

    METHODS initialize_custom_det_class
      RAISING
        zcx_swi_switch.

ENDCLASS.



CLASS zcl_swi_switch IMPLEMENTATION.


  METHOD get.

    initialize_buffer( ).

    result = go_buffer->get_switch( iv_switch ).

  ENDMETHOD.


  METHOD zif_swi_switch~get_code.

    result = ms_switch_data-code.

  ENDMETHOD.


  METHOD zif_swi_switch~get_status.

    IF mi_custom_determination IS BOUND AND
        ms_switch_data-status <> status-inactive AND
        ms_switch_data-status <> status-activated.
      result = mi_custom_determination->get_status( is_switch = ms_switch_data ir_data = ir_data ).
    ELSE.
      result = ms_switch_data-status.
    ENDIF.

  ENDMETHOD.


  METHOD zif_swi_switch~is_activated.

    result = boolc( zif_swi_switch~get_status( ir_data ) = status-activated ).

  ENDMETHOD.


  METHOD initialize_buffer.

    IF go_buffer IS BOUND.
      RETURN.
    ENDIF.

    CREATE OBJECT go_buffer.

  ENDMETHOD.


  METHOD initialize_custom_det_class.

    DATA:
      lv_text1 TYPE string.

    IF ms_switch_data-custom_determination_class IS INITIAL.
      RETURN.
    ENDIF.

    TRY.
        CREATE OBJECT mi_custom_determination TYPE (ms_switch_data-custom_determination_class).
      CATCH cx_root.
        lv_text1 = ms_switch_data-custom_determination_class.
        RAISE EXCEPTION TYPE zcx_swi_switch
          EXPORTING
            textid = zcx_swi_switch=>switch_not_exists
            text1  = lv_text1.
    ENDTRY.

  ENDMETHOD.


ENDCLASS.