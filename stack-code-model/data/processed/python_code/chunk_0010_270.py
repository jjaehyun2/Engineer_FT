class lcl_mockup_dbl_factory_test definition final
  for testing
  duration short
  risk level harmless.

  public section.
    constants c_base_test_class
      type string
      value '\CLASS-POOL=ZCL_MOCKUP_LOADER_STUB_FACTORY\CLASS=LCL_TEST_BASE'.

  private section.
    methods main_test_double for testing.
    methods generate_params for testing.
endclass.

class lcl_mockup_dbl_factory_test implementation.

  method main_test_double.
    call method (c_base_test_class)=>('MAIN_TEST')
      exporting
        lv_factory_classname = 'ZCL_MOCKUP_LOADER_DBL_FACTORY'.
  endmethod.

  method generate_params.

    data ld_if type ref to cl_abap_objectdescr.
    data ld_type type ref to cl_abap_typedescr.
    data lt_act type abap_parmbind_tab.
    data lt_exp type abap_parmbind_tab.
    data par like line of lt_exp.

    ld_if ?= cl_abap_typedescr=>describe_by_name( 'ZIF_MOCKUP_LOADER_STUB_DUMMY' ).

    lt_act = zcl_mockup_loader_dbl_factory=>generate_params(
      id_if_desc = ld_if
      i_method   = 'GEN_PARAM_TARGET' ).

    cl_abap_unit_assert=>assert_equals( act = lines( lt_act ) exp = 4 ).

    clear par.
    read table lt_act with key name = 'P1' into par.
    cl_abap_unit_assert=>assert_equals( act = par-kind exp = 'E' ).
    ld_type ?= cl_abap_typedescr=>describe_by_data_ref( par-value ).
    cl_abap_unit_assert=>assert_equals( act = ld_type->type_kind exp = cl_abap_typedescr=>typekind_int ).

    clear par.
    read table lt_act with key name = 'P2' into par.
    cl_abap_unit_assert=>assert_equals( act = par-kind exp = 'E' ).
    ld_type ?= cl_abap_typedescr=>describe_by_data_ref( par-value ).
    cl_abap_unit_assert=>assert_equals( act = ld_type->type_kind exp = cl_abap_typedescr=>typekind_char ).

    clear par.
    read table lt_act with key name = 'P3' into par.
    cl_abap_unit_assert=>assert_equals( act = par-kind exp = 'E' ).
    ld_type ?= cl_abap_typedescr=>describe_by_data_ref( par-value ).
    cl_abap_unit_assert=>assert_equals( act = ld_type->type_kind exp = cl_abap_typedescr=>typekind_char ).

    clear par.
    read table lt_act with key name = 'CTAB' into par.
    cl_abap_unit_assert=>assert_equals( act = par-kind exp = 'C' ).
    ld_type ?= cl_abap_typedescr=>describe_by_data_ref( par-value ).
    cl_abap_unit_assert=>assert_equals( act = ld_type->type_kind exp = cl_abap_typedescr=>typekind_table ).
    cl_abap_unit_assert=>assert_equals( act = ld_type->absolute_name exp = '\TYPE=FLIGHTTAB' ).

  endmethod.

endclass.