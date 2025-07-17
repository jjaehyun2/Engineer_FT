CLASS zcson_cl_tadir_handler DEFINITION
  PUBLIC
  CREATE PUBLIC.

  PUBLIC SECTION.
    TYPES:
      ty_t_objnames   TYPE STANDARD TABLE OF sobj_name,
      ty_t_classnames TYPE STANDARD TABLE OF abap_classname,
      ty_t_packages   TYPE STANDARD TABLE OF devclass.

    METHODS:
      get_objects_for_packages_deep
        IMPORTING
          it_roots     TYPE ty_t_packages
          iv_obj_type  TYPE trobjtype
        EXPORTING
          et_obj_names TYPE ty_t_objnames,
      get_objects_for_packages
        IMPORTING
          it_packages  TYPE ty_t_packages
          iv_obj_type  TYPE trobjtype
        EXPORTING
          et_obj_names TYPE ty_t_objnames,
      get_descendant_packages
        IMPORTING
          iv_root     TYPE devclass
        EXPORTING
          et_packages TYPE ty_t_packages.

  PROTECTED SECTION.
  PRIVATE SECTION.
ENDCLASS.



CLASS zcson_cl_tadir_handler IMPLEMENTATION.

  METHOD get_descendant_packages.
*&---------------------------------------------------------------------*
*& Date:        08.12.2017
*&---------------------------------------------------------------------*
*& Description: Retrieve all descendant packages of the given package.
*&---------------------------------------------------------------------*
    DATA: lt_packages TYPE ty_t_packages.
*&---------------------------------------------------------------------*

    IF iv_root IS INITIAL.
      RETURN.
    ENDIF.

    SELECT devclass FROM tdevc
      WHERE parentcl = @iv_root
      INTO TABLE @lt_packages BYPASSING BUFFER.

    APPEND LINES OF lt_packages TO et_packages.

    LOOP AT lt_packages ASSIGNING FIELD-SYMBOL(<ls_package>).
      get_descendant_packages(
        EXPORTING
          iv_root     = <ls_package>
        IMPORTING
          et_packages = et_packages ).
    ENDLOOP.

  ENDMETHOD.

  METHOD get_objects_for_packages.
*&---------------------------------------------------------------------*
*& Date:        08.12.2017
*&---------------------------------------------------------------------*
*& Description: Retrieve all objects of the given type from the given
*&              packages.
*&---------------------------------------------------------------------*

    DATA lt_selopt TYPE STANDARD TABLE OF selopt.
    LOOP AT it_packages ASSIGNING FIELD-SYMBOL(<lv_package>).
      APPEND INITIAL LINE TO lt_selopt ASSIGNING FIELD-SYMBOL(<ls_selopt>).
      <ls_selopt>-sign   = 'I'.
      <ls_selopt>-option = 'EQ'.
      <ls_selopt>-low    = <lv_package>.
    ENDLOOP.

    IF lt_selopt IS NOT INITIAL.
      SELECT obj_name FROM tadir
        WHERE devclass IN @lt_selopt AND
              object   = @iv_obj_type AND
              delflag  = @abap_false
        INTO TABLE @et_obj_names BYPASSING BUFFER.
    ENDIF.

  ENDMETHOD.

  METHOD get_objects_for_packages_deep.
*&---------------------------------------------------------------------*
*& Date:        08.12.2017
*&---------------------------------------------------------------------*
*& Description: Retrieve all objects of the given type from the given
*&              packages and sub-packages.
*&---------------------------------------------------------------------*
    DATA: lt_packages TYPE ty_t_packages.
*&---------------------------------------------------------------------*

    APPEND LINES OF it_roots TO lt_packages.

    LOOP AT it_roots ASSIGNING FIELD-SYMBOL(<ls_root>).
      get_descendant_packages(
        EXPORTING
          iv_root     = <ls_root>
        IMPORTING
          et_packages = lt_packages ).
    ENDLOOP.

    get_objects_for_packages(
      EXPORTING
        it_packages  = lt_packages
        iv_obj_type  = iv_obj_type
      IMPORTING
        et_obj_names = et_obj_names ).

  ENDMETHOD.

ENDCLASS.