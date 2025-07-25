class ZCL_AOT_PACKAGES definition
  public
  create public .

public section.

  class-methods FIND_ALL_SUBPACKAGES
    importing
      !IV_DEVCLASS type DEVCLASS
    returning
      value(RT_PACKAGES) type GAKH_T_TDEVC .
  class-methods FIND_SUBPACKAGES
    importing
      !IV_PACKAGE type DEVCLASS
    returning
      value(RT_PACKAGES) type CL_PAK_PACKAGE_QUERIES=>TT_SUBPACKAGE_INFO .
protected section.
private section.
ENDCLASS.



CLASS ZCL_AOT_PACKAGES IMPLEMENTATION.


  METHOD find_all_subpackages.

* todo, merge methods FIND_ALL_SUBPACKAGES and FIND_SUBPACKAGES ?

* todo, caching?

    DATA(lv_package) = iv_devclass.

    SELECT * FROM tdevc APPENDING TABLE rt_packages WHERE devclass = lv_package.

    LOOP AT rt_packages INTO DATA(ls_package).
      SELECT * FROM tdevc APPENDING TABLE rt_packages WHERE parentcl = ls_package-devclass.
    ENDLOOP.

  ENDMETHOD.


  METHOD find_subpackages.

    cl_pak_package_queries=>get_all_subpackages(
      EXPORTING
        im_package                    = iv_package
        im_also_local_packages        = abap_true
      IMPORTING
        et_subpackages                = rt_packages
      EXCEPTIONS
        no_package_specified          = 1
        package_has_no_tdevc_record   = 2
        package_has_no_tadir_record   = 3
        package_does_not_exist        = 4
        invalid_superpackage          = 5
        no_output_parameter_requested = 6
        OTHERS                        = 7 ).
    IF sy-subrc <> 0.
      RETURN.
    ENDIF.

    INSERT VALUE #( package = iv_package ) INTO TABLE rt_packages.

  ENDMETHOD.
ENDCLASS.