CLASS zcl_abaplint_configuration DEFINITION
  PUBLIC
  CREATE PUBLIC .

  PUBLIC SECTION.

    TYPES:
      ty_packages TYPE STANDARD TABLE OF zabaplint_pack WITH EMPTY KEY .

    METHODS read_package
      IMPORTING
        !iv_devclass   TYPE devclass
      RETURNING
        VALUE(rv_json) TYPE string .
    METHODS get_global
      RETURNING
        VALUE(rs_data) TYPE zabaplint_glob_data .
    METHODS set_global
      IMPORTING
        !is_data TYPE zabaplint_glob_data .
    METHODS list_packages
      RETURNING
        VALUE(rt_data) TYPE ty_packages .
    METHODS add_package
      IMPORTING
        !iv_devclass TYPE devclass .
    METHODS remove_package
      IMPORTING
        !iv_devclass TYPE devclass .
    METHODS change_package
      IMPORTING
        !iv_devclass TYPE zabaplint_pack-devclass
        !iv_json     TYPE zabaplint_pack-json .
  PROTECTED SECTION.
  PRIVATE SECTION.
ENDCLASS.



CLASS ZCL_ABAPLINT_CONFIGURATION IMPLEMENTATION.


  METHOD add_package.

    DATA: ls_data TYPE zabaplint_pack.

    ASSERT zcl_abapgit_factory=>get_sap_package( iv_devclass )->exists( ) = abap_true.

    ls_data-devclass = iv_devclass.

    INSERT zabaplint_pack FROM ls_data.
    ASSERT sy-subrc = 0.

  ENDMETHOD.


  METHOD change_package.

    UPDATE zabaplint_pack
      SET json = iv_json
      WHERE devclass = iv_devclass.
    ASSERT sy-dbcnt = 1.

  ENDMETHOD.


  METHOD get_global.

    SELECT SINGLE * FROM zabaplint_glob
      INTO CORRESPONDING FIELDS OF @rs_data
      WHERE sysid = @sy-sysid.

  ENDMETHOD.


  METHOD list_packages.

    SELECT * FROM zabaplint_pack
      INTO TABLE @rt_data
      ORDER BY PRIMARY KEY.

  ENDMETHOD.


  METHOD read_package.

    SELECT SINGLE json
      FROM zabaplint_pack
      INTO @rv_json
      WHERE devclass = @iv_devclass.
    ASSERT sy-subrc = 0.

  ENDMETHOD.


  METHOD remove_package.

    DELETE FROM zabaplint_pack WHERE devclass = iv_devclass.
    ASSERT sy-subrc = 0.

  ENDMETHOD.


  METHOD set_global.

    DATA: ls_data TYPE zabaplint_glob.

    MOVE-CORRESPONDING is_data TO ls_data.
    ls_data-sysid = sy-sysid.

    MODIFY zabaplint_glob FROM ls_data.
    ASSERT sy-subrc = 0.

  ENDMETHOD.
ENDCLASS.