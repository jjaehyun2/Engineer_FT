CLASS zcl_trs_factory_facade DEFINITION
  PUBLIC
  FINAL
  CREATE PRIVATE
  GLOBAL FRIENDS zcl_trs_inject_facade.

  PUBLIC SECTION.

    CLASS-METHODS:
      get_trs_fm_access RETURNING VALUE(r_fm_access) TYPE REF TO zif_trs_fm_access.

  PROTECTED SECTION.
  PRIVATE SECTION.

    CLASS-DATA: facade_fm_class TYPE REF TO zif_trs_fm_access.

ENDCLASS.



CLASS zcl_trs_factory_facade IMPLEMENTATION.

  METHOD get_trs_fm_access.

    IF facade_fm_class IS NOT BOUND.
      facade_fm_class = NEW zcl_trs_fac_fm( ).
    ENDIF.

    r_fm_access = facade_fm_class.

  ENDMETHOD.

ENDCLASS.