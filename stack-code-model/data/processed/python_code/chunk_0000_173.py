class ZCL_ABAK_FORMAT_FACTORY definition
  public
  final
  create public .

public section.

  class-methods GET_INSTANCE
    importing
      !I_FORMAT_TYPE type ZABAK_FORMAT_TYPE
    returning
      value(RO_INSTANCE) type ref to ZIF_ABAK_FORMAT
    raising
      ZCX_ABAK .
  PROTECTED SECTION.
private section.
ENDCLASS.



CLASS ZCL_ABAK_FORMAT_FACTORY IMPLEMENTATION.


  METHOD get_instance.

    CASE i_format_type.
      WHEN zif_abak_consts=>format_type-database.
        CREATE OBJECT ro_instance TYPE zcl_abak_format_db.

      WHEN zif_abak_consts=>format_type-xml.
        CREATE OBJECT ro_instance TYPE zcl_abak_format_xml.

      WHEN OTHERS.
        RAISE EXCEPTION TYPE zcx_abak
          EXPORTING
            textid = zcx_abak=>invalid_parameters.

    ENDCASE.

  ENDMETHOD.
ENDCLASS.