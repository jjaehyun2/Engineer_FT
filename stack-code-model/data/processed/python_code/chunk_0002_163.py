class ZCL_MOCKUP_LOADER_DBL_FACTORY definition
  public
  inheriting from ZCL_MOCKUP_LOADER_STUB_FACTORY
  final
  create public
  for testing .

public section.

  type-pools ABAP .
  class-methods GENERATE_PARAMS
    importing
      !ID_IF_DESC type ref to CL_ABAP_OBJECTDESCR
      !I_METHOD type ABAP_METHNAME
    returning
      value(RT_PARAMS) type ABAP_PARMBIND_TAB .

  methods GENERATE_STUB
    redefinition .
protected section.
private section.
ENDCLASS.



CLASS ZCL_MOCKUP_LOADER_DBL_FACTORY IMPLEMENTATION.


method GENERATE_PARAMS.
  field-symbols <method> like line of id_if_desc->methods.
  read table id_if_desc->methods assigning <method> with key name = i_method.

  data ls_param like line of rt_params.
  data ld_data  type ref to cl_abap_datadescr.
  field-symbols <param> like line of <method>-parameters.

  loop at <method>-parameters assigning <param> where is_optional = abap_false.
    if <param>-parm_kind ca 'IC'. " importing and changing
      if <param>-type_kind ca '~&?#$'. " any, clike, csequence, data, simple
        ld_data ?= cl_abap_typedescr=>describe_by_name( 'C' ).
      else.
        ld_data = id_if_desc->get_method_parameter_type(
          p_method_name    = <method>-name
          p_parameter_name = <param>-name ).
      endif.

      ls_param-name = <param>-name.
      case <param>-parm_kind.
        when 'I'. ls_param-kind = 'E'.
        when 'C'. ls_param-kind = 'C'.
      endcase.
      create data ls_param-value type handle ld_data.
      insert ls_param into table rt_params.
    endif.
  endloop.

endmethod.


method GENERATE_STUB.
  data li_connector type ref to if_abap_testdouble_answer.
  create object li_connector type zcl_mockup_loader_stub_double
    exporting
      it_config = mt_config
      io_ml     = mo_ml.

  r_stub ?= cl_abap_testdouble=>create( object_name = mv_interface_name ).

  field-symbols <conf> like line of mt_config.
  loop at mt_config assigning <conf>.
    data lt_dummy_params type abap_parmbind_tab.
    data lv_invoke_name  type abap_methname.
    lt_dummy_params = generate_params( id_if_desc = md_if_desc i_method = <conf>-method_name ).
    lv_invoke_name  = mv_interface_name && '~' && <conf>-method_name.

    cl_abap_testdouble=>configure_call( r_stub )->ignore_all_parameters( )->set_answer( li_connector ).
    call method r_stub->(lv_invoke_name) parameter-table lt_dummy_params.
  endloop.
endmethod.
ENDCLASS.