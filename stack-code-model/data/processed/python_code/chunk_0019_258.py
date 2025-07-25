*"* use this source file for your ABAP unit test classes

INTERFACE lif_any.
ENDINTERFACE.

CLASS lcl_any DEFINITION.
  PUBLIC SECTION.
    INTERFACES lif_any.
ENDCLASS.

CLASS ltc_main DEFINITION
      FOR TESTING
      DURATION SHORT
      RISK LEVEL HARMLESS.

  PRIVATE SECTION.
    METHODS serialize_deserialize FOR TESTING.
    METHODS technical_type FOR TESTING.
    METHODS create_by_rtti_elem FOR TESTING RAISING cx_static_check.
    METHODS create_by_rtti_struct FOR TESTING RAISING cx_static_check.
    METHODS create_by_rtti_table FOR TESTING RAISING cx_static_check.
    METHODS create_by_rtti_ref FOR TESTING RAISING cx_static_check.
    METHODS create_by_rtti_class FOR TESTING RAISING cx_static_check.
    METHODS create_by_rtti_intf FOR TESTING RAISING cx_static_check.
    METHODS assert_attribute_values
      IMPORTING
        srtti type ref to zcl_srtti_typedescr
        absolute_name LIKE cl_abap_typedescr=>absolute_name
        type_kind     LIKE cl_abap_typedescr=>type_kind
        length        LIKE cl_abap_typedescr=>length
        decimals      LIKE cl_abap_typedescr=>decimals
        kind          LIKE cl_abap_typedescr=>kind
        is_ddic_type  TYPE abap_bool.
    DATA dref TYPE REF TO data.

ENDCLASS.

CLASS ltc_main IMPLEMENTATION.

  METHOD create_by_rtti_elem.
    DATA variable TYPE c LENGTH 20.
    DATA(srtti) = zcl_srtti_typedescr=>create_by_data_object( variable ).
    cl_abap_unit_assert=>assert_true( msg = 'is instance of zcl_srtti_elemdescr' act = xsdbool( srtti IS INSTANCE OF zcl_srtti_elemdescr ) ).
  ENDMETHOD.

  METHOD create_by_rtti_struct.
    DATA: BEGIN OF variable,
            comp1 TYPE c LENGTH 20,
          END OF variable.
    DATA(srtti) = zcl_srtti_typedescr=>create_by_data_object( variable ).
    cl_abap_unit_assert=>assert_true( msg = 'is instance of zcl_srtti_structdescr' act = xsdbool( srtti IS INSTANCE OF zcl_srtti_structdescr ) ).
  ENDMETHOD.

  METHOD create_by_rtti_table.
    DATA: BEGIN OF variable,
            comp1 TYPE c LENGTH 20,
          END OF variable.
    DATA(srtti) = zcl_srtti_typedescr=>create_by_data_object( variable ).
    cl_abap_unit_assert=>assert_true( msg = 'is instance of zcl_srtti_structdescr' act = xsdbool( srtti IS INSTANCE OF zcl_srtti_structdescr ) ).
  ENDMETHOD.

  METHOD create_by_rtti_ref.
    DATA variable TYPE REF TO flag.
    DATA(srtti) = zcl_srtti_typedescr=>create_by_data_object( variable ).
    cl_abap_unit_assert=>assert_true( msg = 'is instance of zcl_srtti_refdescr' act = xsdbool( srtti IS INSTANCE OF zcl_srtti_refdescr ) ).
  ENDMETHOD.

  METHOD create_by_rtti_class.
    DATA variable TYPE REF TO lcl_any.
    variable = NEW #( ).
    DATA(srtti) = zcl_srtti_typedescr=>create_by_rtti( CAST #( cl_abap_typedescr=>describe_by_object_ref( variable ) ) ).
    cl_abap_unit_assert=>assert_true( msg = 'is instance of zcl_srtti_classdescr' act = xsdbool( srtti IS INSTANCE OF zcl_srtti_classdescr ) ).
  ENDMETHOD.

  METHOD create_by_rtti_intf.
    DATA variable TYPE REF TO lcl_any.
    variable = NEW #( ).
    DATA(rtti_intf) = CAST cl_abap_classdescr( cl_abap_typedescr=>describe_by_object_ref( variable ) )->get_interface_type( 'LIF_ANY' ).
    DATA(srtti) = zcl_srtti_typedescr=>create_by_rtti( rtti_intf ).
    cl_abap_unit_assert=>assert_true( msg = 'is instance of zcl_srtti_intfdescr' act = xsdbool( srtti IS INSTANCE OF zcl_srtti_intfdescr ) ).
  ENDMETHOD.

  METHOD assert_attribute_values.
    cl_abap_unit_assert=>assert_equals( msg = 'absolute_name' exp = absolute_name act = srtti->absolute_name ).
    cl_abap_unit_assert=>assert_equals( msg = 'Type kind' exp = type_kind act = srtti->type_kind ).
    cl_abap_unit_assert=>assert_equals( msg = 'length' exp = length act = srtti->length ).
    cl_abap_unit_assert=>assert_equals( msg = 'decimals' exp = decimals act = srtti->decimals ).
    cl_abap_unit_assert=>assert_equals( msg = 'Kind' exp = kind act = srtti->kind ).
    cl_abap_unit_assert=>assert_equals( msg = 'is_ddic_type' exp = is_ddic_type act = srtti->is_ddic_type ).
  ENDMETHOD.

  METHOD serialize_deserialize.
    CREATE DATA dref TYPE c LENGTH 10.
    DATA(rtti) = cl_abap_typedescr=>describe_by_data_ref( dref ).
    DATA(srtti) = NEW zcl_srtti_typedescr( cl_abap_typedescr=>describe_by_data_ref( dref ) ).
* absolute_name
* type_kind
* length
* decimals
* kind
* is_ddic_type
*    cl_abap_unit_assert=>assert_equals( msg = 'absolute_name' exp = rtti->absolute_name act = srtti->absolute_name ).
*    cl_abap_unit_assert=>assert_equals( msg = 'Type kind' exp = rtti->type_kind act = srtti->type_kind ).
*    cl_abap_unit_assert=>assert_equals( msg = 'length' exp = rtti->length act = srtti->length ).
*    cl_abap_unit_assert=>assert_equals( msg = 'decimals' exp = rtti->decimals act = srtti->decimals ).
*    cl_abap_unit_assert=>assert_equals( msg = 'Kind' exp = rtti->kind act = srtti->kind ).
*    cl_abap_unit_assert=>assert_equals( msg = 'is_ddic_type' exp = rtti->is_ddic_type( ) act = srtti->is_ddic_type ).
*
*    DATA variable TYPE c LENGTH 20.
*    variable = 'Hello world'.

  ENDMETHOD.

  METHOD technical_type.

    DATA dobj_with_bound_data_type TYPE c LENGTH 20.
    DATA(srtti) = zcl_srtti_typedescr=>create_by_data_object( dobj_with_bound_data_type ).
    cl_abap_unit_assert=>assert_equals( msg = 'technical_type' exp = abap_true act = srtti->technical_type ).

  ENDMETHOD.

ENDCLASS.