*"* use this source file for your ABAP unit test classes
class ltcl_comp_itabs definition deferred.
class zcl_tools_comp_itabs definition local friends ltcl_comp_itabs.

class ltcl_comp_itabs definition final for testing
  duration long
  risk level harmless.

  public section.
    interfaces zif_tools_comp_itabs.

  private section.
    data cut type ref to zcl_tools_comp_itabs.
    methods:
      setup,
      add_changes_by for testing raising cx_static_check,
      add_changes for testing raising cx_static_check,
      compare_itabs_with_itabs for testing raising cx_static_check,
      compare_itabs_with_areas for testing raising cx_static_check.
endclass.


class ltcl_comp_itabs implementation.

  method setup.
    cut = new #( ).
  endmethod.

  method add_changes_by.
    data itab_mara_old type mara.
    data itab_mara_new like itab_mara_old.

    " given
    itab_mara_old = value #(
      matnr = '10111115'
      meins = 'ST'
      ean11 = '10235689741'
      zzmhdd = 1
     ).

    itab_mara_new = value #(
      matnr = '10111116'
      meins = 'VPE'
      ean11 = '10235689742'
      zzmhdd = 2
     ).

    data(expected) = value zif_tools_comp_itabs~tt_changed_data(
      (
        table_name = 'MARA'
        field_name = 'MATNR'
        tabix      = 1
        value_old  = '10111115'
        value_new  = '10111116'
      )
      (
        table_name = 'MARA'
        field_name = 'MEINS'
        tabix      = 1
        value_old  = 'ST'
        value_new  = 'VPE'
      )
      (
        table_name = 'MARA'
        field_name = 'EAN11'
        tabix      = 1
        value_old  = '10235689741'
        value_new  = '10235689742'
      )
      (
        table_name = 'MARA'
        field_name = 'ZZMHDD'
        tabix      = 1
        value_old  = '1'
        value_new  = '2'
      )
    ).

    " when
    cut->add_changes_by(
    iv_tablename = 'MARA'
    wa_new = itab_mara_new
    wa_old = itab_mara_old ).


    " then
    cl_abap_unit_assert=>assert_equals(
      act = cut->return_changes( )
      exp = expected ).


  endmethod.

  method compare_itabs_with_itabs.
    data itab_makt_old type standard table of makt.
    data itab_makt_new like itab_makt_old.

    " given
    itab_makt_old = value #(
    (
      maktg = 'BAR'
      maktx = 'Bar Produkte'
      mandt = '010'
      matnr = '11111111'
      spras = 'DE'
     )
    (
      maktg = 'BAR'
      maktx = 'Bar products'
      mandt = '010'
      matnr = '11111111'
      spras = 'EN'
     )
    ).

    itab_makt_new = value #(
    (
      maktg = 'FOO'
      maktx = 'Foo Produkte'
      mandt = '010'
      matnr = '11111111'
      spras = 'DE'
    )
    (
      maktg = 'FOO'
      maktx = 'Foo products'
      mandt = '010'
      matnr = '11111111'
      spras = 'EN'
     )
    ).

    data(expected) = value zif_tools_comp_itabs~tt_changed_data(
      (
        table_name = 'TT_MAKT'
        field_name = 'MAKTX'
        tabix      = 4
        value_old  = 'Bar Produkte'
        value_new  = 'Foo Produkte'
      )
      (
        table_name = 'TT_MAKT'
        field_name = 'MAKTG'
        tabix      = 5
        value_old  = 'BAR'
        value_new  = 'FOO'
      )
      (
        table_name = 'TT_MAKT'
        field_name = 'MAKTX'
        tabix      = 4
        value_old  = 'Bar products'
        value_new  = 'Foo products'
      )
      (
        table_name = 'TT_MAKT'
        field_name = 'MAKTG'
        tabix      = 5
        value_old  = 'BAR'
        value_new  = 'FOO'
      )
    ).

    " when
    cut->compare_itabs(
      exporting
        iv_tablename = 'TT_MAKT'
        itab_old     = itab_makt_old
        itab_new     = itab_makt_new
    ).

    " then
    cl_abap_unit_assert=>assert_equals(
      act = cut->return_changes( )
      exp = expected
    ).
  endmethod.


  method compare_itabs_with_areas.
    data wa_mara_old type mara.
    data wa_mara_new like wa_mara_old.

    " given
    wa_mara_old = value #(
      matnr = '10111115'
      meins = 'ST'
      ean11 = '10235689741'
      zzmhdd = 1
     ).

    wa_mara_new = value #(
      matnr = '10111116'
      meins = 'VPE'
      ean11 = '10235689742'
      zzmhdd = 2
     ).

    data(expected) = value zif_tools_comp_itabs~tt_changed_data(
      (
        table_name = 'MARA'
        field_name = 'MATNR'
        tabix      = 1
        value_old  = '10111115'
        value_new  = '10111116'
      )
      (
        table_name = 'MARA'
        field_name = 'MEINS'
        tabix      = 1
        value_old  = 'ST'
        value_new  = 'VPE'
      )
      (
        table_name = 'MARA'
        field_name = 'EAN11'
        tabix      = 1
        value_old  = '10235689741'
        value_new  = '10235689742'
      )
      (
        table_name = 'MARA'
        field_name = 'ZZMHDD'
        tabix      = 1
        value_old  = '1'
        value_new  = '2'
      )
    ).

    " when
    cut->compare_itabs(
    iv_tablename = 'MARA'
    itab_old = wa_mara_old
    itab_new = wa_mara_new ).


    " then
    cl_abap_unit_assert=>assert_equals(
      act = cut->return_changes( )
      exp = expected ).
  endmethod.

  method add_changes.
    " when
    cut->add_changes( changed_fields = value #(
      table_name = 'STPO'
      field_name = 'IDNRK'
      ) ).

      data(expected) = value zif_tools_comp_itabs~tt_changed_data(
        (
          table_name = 'STPO'
          field_name = 'IDNRK'
        )
      ).

      " then
    cl_abap_unit_assert=>assert_equals(
      act = cut->return_changes( )
      exp = expected
    ).
  endmethod.

endclass.