CLASS /dmo/cl_rap_node DEFINITION
  PUBLIC
  CREATE PUBLIC
  GLOBAL FRIENDS /dmo/cl_rap_xco_json_visitor.

  PUBLIC SECTION.

    CONSTANTS:
      "the RAP generator only supports certain combinations of implementation type and key type
      BEGIN OF implementation_type,
        managed_uuid      TYPE string VALUE 'managed_uuid',
        managed_semantic  TYPE string VALUE 'managed_semantic',
        unmanged_semantic TYPE string VALUE 'unmanaged_semantic',
      END OF implementation_type,

      BEGIN OF additional_fields_object_types,
        cds_interface_view  TYPE string VALUE 'cds_interface_view',
        cds_projection_view TYPE string VALUE 'cds_projection_view',
        draft_table         TYPE string VALUE 'draft_table',
      END OF additional_fields_object_types,

      BEGIN OF data_source_types,
        table     TYPE string VALUE 'table',
        cds_view  TYPE string VALUE 'cds_view',
        abap_type TYPE string VALUE 'abap_type',
        structure TYPE string VALUE 'structure',
      END OF data_source_types,

      BEGIN OF cardinality,
        zero_to_one TYPE string VALUE 'zero_to_one',
        one         TYPE string VALUE 'one',
        zero_to_n   TYPE string VALUE 'zero_to_n',
        one_to_n    TYPE string VALUE 'one_to_n',
        one_to_one  TYPE string VALUE 'one_to_one',
      END OF cardinality,


      BEGIN OF additionalBinding_usage,
        filter            TYPE string VALUE 'FILTER',
        filter_and_result TYPE string VALUE 'FILTER_AND_RESULT',
        result            TYPE string VALUE 'RESULT',
      END OF additionalBinding_usage,

      BEGIN OF binding_type_name,
        odata_v4_ui      TYPE string VALUE 'odata_v4_ui',
        odata_v2_ui      TYPE string VALUE 'odata_v2_ui',
        odata_v4_web_api TYPE string VALUE 'odata_v4_web_api',
        odata_v2_web_api TYPE string VALUE 'odata_v2_web_api',
      END OF binding_type_name,

      BEGIN OF  protocol_version_suffix,
        OData_V2 TYPE string VALUE '_O2',
        OData_V4 TYPE string VALUE '_O4',
      END OF protocol_version_suffix,

      BEGIN OF binding_type_prefix,
        ui      TYPE string VALUE 'UI_',
        Web_API TYPE string VALUE 'API_',
      END OF binding_type_prefix,

      BEGIN OF node_object_suffix,
        custom_entity           TYPE string VALUE 'I_',
        custom_query_impl_class TYPE string VALUE 'CL_CE_',
        cds_view_i              TYPE string VALUE 'I_',
        "ddic_view_i             TYPE sxco_dbt_object_name,
        cds_view_p              TYPE string VALUE 'C_',
        meta_data_extension     TYPE string VALUE 'C_',
        behavior_implementation TYPE string VALUE 'BP_I_',
        control_structure       TYPE string VALUE 'S',
      END OF node_object_suffix,



      BEGIN OF root_node_object_suffix,
        behavior_definition_i TYPE string VALUE 'I_',
        behavior_definition_p TYPE string VALUE 'C_',
        service_definition    TYPE string VALUE 'C_',
        service_binding       TYPE string VALUE 'C_',
      END OF root_node_object_suffix,

      supported_binding_types  TYPE string VALUE 'odata_v4_ui, odata_v2_ui, odata_v4_web_api, odata_v2_web_api',

      uuid_type                TYPE cl_xco_ad_built_in_type=>tv_type   VALUE 'RAW',
      uuid_length              TYPE cl_xco_ad_built_in_type=>tv_length  VALUE 16,

      singleton_field_name     TYPE sxco_cds_field_name  VALUE 'SingletonID',
      singleton_suffix         TYPE string VALUE '_S',
      singleton_child_tab_name TYPE string VALUE 'child_tab'.



    .


    TYPES:
      BEGIN OF root_cause_textid,
        msgid TYPE symsgid,
        msgno TYPE symsgno,
        attr1 TYPE scx_attrname,
        attr2 TYPE scx_attrname,
        attr3 TYPE scx_attrname,
        attr4 TYPE scx_attrname,
      END OF root_cause_textid.

    TYPES:
      BEGIN OF ts_manage_buiness_config,
        namespace   TYPE if_mbc_cp_api_business_config=>ty_namespace,
        identifier  TYPE if_mbc_cp_api_business_config=>ty_identifier,
        name        TYPE if_mbc_cp_api_business_config=>ty_name,
        description TYPE if_mbc_cp_api_business_config=>ty_description,
      END OF ts_manage_buiness_config.


    TYPES:
      BEGIN OF ts_field_name,
        client                         TYPE string,
        uuid                           TYPE string,
        parent_uuid                    TYPE string,
        root_uuid                      TYPE string,
        created_by                     TYPE string,
        created_at                     TYPE string,
        last_changed_by                TYPE string,
        last_changed_at                TYPE string,
        local_instance_last_changed_at TYPE string,
        local_instance_last_changed_by TYPE string,
        language                       TYPE string,
        etag_master                    TYPE string,
        total_etag                     TYPE string,

      END OF ts_field_name.

    TYPES :  tt_childnodes TYPE STANDARD TABLE OF REF TO /dmo/cl_rap_node WITH EMPTY KEY.
    TYPES :  ty_childnode TYPE REF TO /dmo/cl_rap_node.

    TYPES :  tt_semantic_key_fields TYPE TABLE OF sxco_ad_field_name.
    TYPES :
      BEGIN OF ts_semantic_key,
        name           TYPE sxco_ad_field_name,
        cds_view_field TYPE sxco_ad_field_name,
      END OF ts_semantic_key.
    TYPES    : tt_semantic_key TYPE TABLE OF  ts_semantic_key.

    TYPES:
      BEGIN OF ts_field,
        name                   TYPE sxco_ad_object_name,
        doma                   TYPE sxco_ad_object_name,
        data_element           TYPE sxco_ad_object_name,
        key_indicator          TYPE abap_bool,
        not_null               TYPE abap_bool,
        domain_fixed_value     TYPE abap_bool,
        cds_view_field         TYPE sxco_cds_field_name,
        has_association        TYPE abap_bool,
        has_valuehelp          TYPE abap_bool,
        currencyCode           TYPE sxco_cds_field_name,
        unitOfMeasure          TYPE sxco_cds_field_name,
        is_data_element        TYPE abap_bool,
        is_built_in_type       TYPE abap_bool,
        is_hidden              TYPE abap_bool,
        is_currencyCode        TYPE abap_bool,
        is_unitOfMeasure       TYPE abap_bool,
        "built_in_type_object TYPE REF TO cl_xco_ad_built_in_type,
        built_in_type          TYPE cl_xco_ad_built_in_type=>tv_type,
        built_in_type_length   TYPE cl_xco_ad_built_in_type=>tv_length,
        built_in_type_decimals TYPE cl_xco_ad_built_in_type=>tv_decimals,
      END OF ts_field.

    TYPES : tt_fields TYPE STANDARD TABLE OF ts_field WITH EMPTY KEY.

    TYPES : tt_fields_default_key TYPE STANDARD TABLE OF ts_field WITH DEFAULT KEY.

    TYPES:
      BEGIN OF ts_node_objects,
        custom_entity           TYPE sxco_cds_object_name,
        custom_query_impl_class TYPE sxco_ao_object_name,
        cds_view_i              TYPE sxco_cds_object_name,
        ddic_view_i             TYPE sxco_dbt_object_name,
        cds_view_p              TYPE sxco_cds_object_name,
        meta_data_extension     TYPE sxco_cds_object_name,
        alias                   TYPE sxco_ddef_alias_name,
        behavior_implementation TYPE sxco_ao_object_name,
        control_structure       TYPE sxco_ad_object_name,
      END OF ts_node_objects.

    TYPES:
      BEGIN OF ts_root_node_objects,
        behavior_definition_i TYPE sxco_cds_object_name,
        behavior_definition_p TYPE sxco_cds_object_name,
        service_definition    TYPE sxco_ao_object_name,
        service_binding       TYPE sxco_ao_object_name,
      END OF ts_root_node_objects.

    TYPES:
      BEGIN OF ts_additional_fields,
        field_name             TYPE string,
        alias                  TYPE sxco_ddef_alias_name,
        data_element           TYPE sxco_ad_object_name,
        built_in_type          TYPE cl_xco_ad_built_in_type=>tv_type,
        built_in_type_length   TYPE cl_xco_ad_built_in_type=>tv_length,
        built_in_type_decimals TYPE cl_xco_ad_built_in_type=>tv_decimals,
        localized              TYPE abap_bool,
      END OF ts_additional_fields,

      tt_additional_fields TYPE STANDARD TABLE OF ts_additional_fields WITH DEFAULT KEY.

    TYPES:
      BEGIN OF ts_additional_fields_2,
        name                   TYPE string,
        cds_view_field         TYPE sxco_ddef_alias_name,
        data_element           TYPE sxco_ad_object_name,
        built_in_type          TYPE cl_xco_ad_built_in_type=>tv_type,
        built_in_type_length   TYPE cl_xco_ad_built_in_type=>tv_length,
        built_in_type_decimals TYPE cl_xco_ad_built_in_type=>tv_decimals,
        is_hidden              TYPE abap_bool,
        localized              TYPE abap_bool,
        cds_interface_view     TYPE abap_bool,
        cds_projection_view    TYPE abap_bool,
        draft_table            TYPE abap_bool,
      END OF ts_additional_fields_2,

      tt_additional_fields_2 TYPE STANDARD TABLE OF ts_additional_fields_2 WITH DEFAULT KEY.


    TYPES:
      BEGIN OF ts_objects_with_add_fields,
        object            TYPE string,
        additional_fields TYPE tt_additional_fields,
      END OF ts_objects_with_add_fields,

      tt_objects_with_add_fields TYPE STANDARD TABLE OF ts_objects_with_add_fields WITH DEFAULT KEY.

    TYPES:
      BEGIN OF ts_abap_type,
        prefix    TYPE sxco_ao_object_name,
        type_name TYPE   sxco_ao_component_name,
      END OF ts_abap_type.

    TYPES:
      BEGIN OF ts_condition_fields,
        projection_field  TYPE sxco_cds_field_name,
        association_field TYPE sxco_cds_field_name,
      END OF ts_condition_fields,


      tt_condition_fields TYPE STANDARD TABLE OF ts_condition_fields WITH EMPTY KEY,

      BEGIN OF ts_assocation,
        name                 TYPE sxco_ddef_alias_name,
        target               TYPE sxco_cds_object_name,
        condition_components TYPE tt_condition_fields,
        cardinality          TYPE string,
      END OF ts_assocation,

      tt_assocation TYPE STANDARD TABLE OF ts_assocation,

      BEGIN OF ts_additionalBinding,
        localElement TYPE sxco_cds_field_name,
        element      TYPE sxco_cds_field_name,
        usage        TYPE string,
      END OF ts_additionalBinding,

      tt_addtionalBinding TYPE STANDARD TABLE OF ts_additionalbinding WITH DEFAULT KEY,

      BEGIN OF ts_valuehelp,
        name              TYPE sxco_cds_object_name,
        alias             TYPE sxco_ddef_alias_name,
        localElement      TYPE sxco_cds_field_name,
        element           TYPE sxco_cds_field_name,
        additionalBinding TYPE tt_addtionalbinding,
      END OF ts_valuehelp,

      tt_valuehelp TYPE STANDARD TABLE OF ts_valuehelp WITH DEFAULT KEY.

    DATA generate_only_node_hierachy TYPE abap_bool.

    DATA xco_lib TYPE REF TO /dmo/cl_rap_xco_lib.
    DATA data_source_type    TYPE string READ-ONLY.
    DATA lt_valuehelp TYPE tt_valuehelp READ-ONLY.
    DATA lt_objects_with_add_fields TYPE tt_objects_with_add_fields READ-ONLY.
    DATA lt_messages TYPE TABLE OF string READ-ONLY.
    DATA field_name TYPE ts_field_name READ-ONLY.
    DATA lt_association TYPE tt_assocation READ-ONLY.
    DATA rap_node_objects TYPE ts_node_objects READ-ONLY.
    DATA rap_root_node_objects TYPE ts_root_node_objects READ-ONLY.
    DATA lt_fields TYPE STANDARD TABLE OF ts_field WITH DEFAULT KEY READ-ONLY.
    DATA lt_additional_fields TYPE STANDARD TABLE OF ts_additional_fields_2 WITH DEFAULT KEY READ-ONLY.
    DATA lt_all_fields TYPE STANDARD TABLE OF ts_field WITH DEFAULT KEY READ-ONLY.
    DATA lt_fields_persistent_table TYPE STANDARD TABLE OF ts_field WITH DEFAULT KEY READ-ONLY.
    DATA table_name          TYPE sxco_dbt_object_name READ-ONLY.
    DATA structure_name      TYPE sxco_ad_object_name READ-ONLY.
    DATA abap_type_name TYPE string.
    DATA semantic_key TYPE tt_semantic_key.
    DATA suffix              TYPE string READ-ONLY.
    DATA prefix              TYPE string READ-ONLY.
    DATA namespace           TYPE string READ-ONLY.
    DATA entityname          TYPE sxco_ddef_alias_name READ-ONLY.
    DATA node_number         TYPE i READ-ONLY.
    DATA object_id           TYPE sxco_ad_field_name READ-ONLY.
    DATA object_id_cds_field_name TYPE sxco_ad_field_name READ-ONLY.
    DATA all_childnodes TYPE STANDARD TABLE OF REF TO /dmo/cl_rap_node READ-ONLY.
    DATA childnodes TYPE STANDARD TABLE OF REF TO /dmo/cl_rap_node READ-ONLY.
    DATA root_node TYPE REF TO /dmo/cl_rap_node READ-ONLY.
    DATA parent_node TYPE REF TO /dmo/cl_rap_node READ-ONLY.
    DATA is_finalized           TYPE abap_bool READ-ONLY .
    DATA package          TYPE sxco_package READ-ONLY.
    DATA lt_mapping TYPE HASHED TABLE OF  if_xco_gen_bdef_s_fo_b_mapping=>ts_field_mapping
                                  WITH UNIQUE KEY cds_view_field dbtable_field.
    DATA ls_mapping TYPE if_xco_gen_bdef_s_fo_b_mapping=>ts_field_mapping  .
    DATA transactional_behavior TYPE abap_bool READ-ONLY.
    DATA multi_edit TYPE abap_bool READ-ONLY.
    DATA manage_business_configuration TYPE abap_bool READ-ONLY.
    DATA manage_business_config_names TYPE ts_manage_buiness_config READ-ONLY.
    DATA publish_service            TYPE abap_bool READ-ONLY.
    DATA cds_view_name TYPE string READ-ONLY.
    DATA data_source_name TYPE string READ-ONLY.
    DATA persistent_table_name TYPE string READ-ONLY.
    DATA draft_table_name TYPE sxco_dbt_object_name READ-ONLY.
    DATA binding_type TYPE string READ-ONLY.
    DATA transport_request TYPE string READ-ONLY.
    DATA draft_enabled TYPE abap_bool READ-ONLY .
    DATA useUpperCamelCase TYPE abap_bool READ-ONLY .
    DATA skip_activation TYPE abap_bool READ-ONLY.
    DATA add_meta_data_extensions TYPE abap_bool READ-ONLY.
    DATA is_customizing_table TYPE abap_bool READ-ONLY.


    " DATA rap_generator_xco_lib TYPE REF TO zif_rap_generator_xco_lib.

    METHODS constructor
      IMPORTING io_xco_lib TYPE REF TO /dmo/cl_rap_xco_lib OPTIONAL
      RAISING   /dmo/cx_rap_generator.

    METHODS set_xco_lib
      IMPORTING io_xco_lib TYPE REF TO /dmo/cl_rap_xco_lib
      RAISING   /dmo/cx_rap_generator.

    METHODS add_transactional_behavior
      IMPORTING iv_value TYPE abap_bool .

    METHODS set_generate_only_node_hierach
      IMPORTING iv_value TYPE abap_bool.


    METHODS add_multi_edit
      IMPORTING iv_value TYPE abap_bool.

    METHODS add_to_manage_business_config
      IMPORTING iv_value TYPE abap_bool .

    METHODS generate_bil
      RETURNING VALUE(result) TYPE abap_bool.

    METHODS generate_custom_entity
      RETURNING VALUE(result) TYPE abap_bool.

    METHODS set_mbc_namespace.


    METHODS set_mbc_identifier
      IMPORTING iv_value TYPE string . "if_mbc_cp_api_business_config=>ty_identifier.

    METHODS set_mbc_name
      IMPORTING iv_value TYPE  string. "if_mbc_cp_api_business_config=>ty_name.

    METHODS set_mbc_description
      IMPORTING iv_value TYPE string. "if_mbc_cp_api_business_config=>ty_description.

    METHODS set_is_customizing_table
      IMPORTING iv_value TYPE abap_bool.

    METHODS  set_publish_service
      IMPORTING iv_value TYPE abap_bool .

    METHODS  set_draft_enabled
      IMPORTING iv_value TYPE abap_bool .

    METHODS set_add_meta_data_extensions
      IMPORTING iv_value TYPE abap_bool .

    METHODS set_skip_activation
      IMPORTING iv_value TYPE abap_bool .

    METHODS add_to_all_childnodes
      IMPORTING VALUE(io_child_node) TYPE REF TO /dmo/cl_rap_node.

    METHODS set_mapping
      IMPORTING it_field_mappings TYPE if_xco_gen_bdef_s_fo_b_mapping=>tt_field_mapping OPTIONAL
      RAISING   /dmo/cx_rap_generator.

    METHODS set_package
      IMPORTING VALUE(iv_package) TYPE sxco_package
      RAISING   /dmo/cx_rap_generator.

    METHODS set_entity_name
      IMPORTING VALUE(iv_entity_name) TYPE sxco_ddef_alias_name
      RAISING   /dmo/cx_rap_generator.

    METHODS get_implementation_type
      RETURNING VALUE(rv_implementation_type) TYPE string.

    METHODS get_root_exception
      IMPORTING
        !ix_exception  TYPE REF TO cx_root
      RETURNING
        VALUE(rx_root) TYPE REF TO cx_root .

    METHODS get_root_cause_textid
      IMPORTING
                ix_previous                 TYPE REF TO cx_root
      RETURNING VALUE(rs_root_cause_textid) TYPE root_cause_textid.

    METHODS set_implementation_type
      IMPORTING
                VALUE(iv_implementation_type) TYPE string
      RAISING   /dmo/cx_rap_generator.



    METHODS add_child
      RETURNING VALUE(ro_child_node)
                  TYPE REF TO /dmo/cl_rap_node
      RAISING   /dmo/cx_rap_generator.

    METHODS add_virtual_root_node
      RETURNING VALUE(ro_virtual_root_node)
                  TYPE REF TO /dmo/cl_rap_node
      RAISING   /dmo/cx_rap_generator.

    METHODS add_child_node_hierarchy
      IMPORTING
                child_node TYPE REF TO /dmo/cl_rap_node
      RAISING   /dmo/cx_rap_generator.

    METHODS check_repository_object_name
      IMPORTING
                iv_type TYPE sxco_ar_object_type
                iv_name TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS check_parameter
      IMPORTING
                iv_parameter_name TYPE string
                iv_value          TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS check_table_package_assignment
      RAISING /dmo/cx_rap_generator.

    METHODS finalize
      RAISING /dmo/cx_rap_generator.

    METHODS validate_bo
      RAISING /dmo/cx_rap_generator.

    METHODS get_fields
      RAISING /dmo/cx_rap_generator.

    METHODS get_fields_persistent_table
      RAISING /dmo/cx_rap_generator.

    METHODS set_namespace
      IMPORTING
                iv_namespace TYPE sxco_ar_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS set_prefix
      IMPORTING
                iv_prefix TYPE    sxco_ar_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS set_suffix
      IMPORTING
                iv_suffix TYPE    sxco_ar_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS set_parent
      IMPORTING
                io_parent_node TYPE REF TO /dmo/cl_rap_node
      RAISING   /dmo/cx_rap_generator.

    METHODS set_root
      IMPORTING
                io_root_node TYPE REF TO /dmo/cl_rap_node
      RAISING   /dmo/cx_rap_generator.

    METHODS is_root RETURNING VALUE(rv_is_root) TYPE abap_bool.
    METHODS is_virtual_root RETURNING VALUE(rv_is_virtual_root) TYPE abap_bool.

    METHODS is_child RETURNING VALUE(rv_is_child) TYPE abap_bool.

    METHODS is_grand_child_or_deeper RETURNING VALUE(rv_is_grand_child) TYPE abap_bool.

    METHODS set_table
      IMPORTING
                iv_table TYPE sxco_ar_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS set_cds_view
      IMPORTING
                iv_cds_view TYPE sxco_cds_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS set_structure
      IMPORTING
                iv_structure TYPE sxco_ad_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS set_abap_type
      IMPORTING iv_abap_type TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS split_and_check_abap_type_name
      IMPORTING iv_abap_type_name TYPE string
      EXPORTING ev_class_name     TYPE sxco_ao_object_name
                ev_type_name      TYPE sxco_ao_component_name .

    METHODS set_data_source
      IMPORTING
                iv_data_source TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS set_binding_type
      IMPORTING
                iv_binding_type TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS set_transport_request
      IMPORTING
                iv_transport_request TYPE sxco_transport
      RAISING   /dmo/cx_rap_generator.

    METHODS set_persistent_table
      IMPORTING
                iv_persistent_table TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS set_draft_table
      IMPORTING
                iv_draft_table TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS set_data_source_type
      IMPORTING
                iv_data_source_type TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS has_childs
      RETURNING VALUE(rv_has_childs) TYPE abap_bool.

    METHODS set_semantic_key_fields
      IMPORTING it_semantic_key TYPE tt_semantic_key_fields
      RAISING   /dmo/cx_rap_generator.

    METHODS set_cds_view_i_name
      IMPORTING iv_name                   TYPE sxco_cds_object_name OPTIONAL
      RETURNING VALUE(rv_cds_i_view_name) TYPE sxco_cds_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS set_custom_entity_name
      IMPORTING iv_name                      TYPE sxco_cds_object_name OPTIONAL
      RETURNING VALUE(rv_custom_entity_name) TYPE sxco_cds_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS set_cds_view_p_name
      IMPORTING iv_name                   TYPE sxco_cds_object_name OPTIONAL
      RETURNING VALUE(rv_cds_p_view_name) TYPE sxco_cds_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS set_mde_name
      IMPORTING iv_name            TYPE sxco_cds_object_name OPTIONAL
      RETURNING VALUE(rv_mde_name) TYPE sxco_cds_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS get_valid_draft_table_name
      IMPORTING iv_name                    TYPE sxco_dbt_object_name OPTIONAL
      RETURNING VALUE(rv_ddic_i_view_name) TYPE sxco_dbt_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS get_valid_mbc_identifier
      IMPORTING iv_name                  TYPE sxco_cds_object_name OPTIONAL
      RETURNING VALUE(rv_mbc_identifier) TYPE sxco_cds_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS set_behavior_impl_name
      IMPORTING iv_name                     TYPE sxco_cds_object_name OPTIONAL
      RETURNING VALUE(rv_behavior_imp_name) TYPE sxco_cds_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS set_custom_query_impl_name
      IMPORTING iv_name                           TYPE sxco_cds_object_name OPTIONAL
      RETURNING VALUE(rv_custom_query_impl_class) TYPE sxco_cds_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS set_behavior_def_i_name
      IMPORTING iv_name                       TYPE sxco_cds_object_name OPTIONAL
      RETURNING VALUE(rv_behavior_dev_i_name) TYPE sxco_cds_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS set_behavior_def_p_name
      IMPORTING iv_name                       TYPE sxco_cds_object_name OPTIONAL
      RETURNING VALUE(rv_behavior_dev_p_name) TYPE sxco_cds_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS set_service_definition_name
      IMPORTING iv_name                           TYPE sxco_cds_object_name OPTIONAL
      RETURNING VALUE(rv_service_definition_name) TYPE sxco_cds_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS set_service_binding_name
      IMPORTING iv_name                        TYPE sxco_cds_object_name OPTIONAL
      RETURNING VALUE(rv_service_binding_name) TYPE sxco_cds_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS set_control_structure_name
      IMPORTING iv_name                           TYPE sxco_cds_object_name OPTIONAL
      RETURNING VALUE(rv_controle_structure_name) TYPE sxco_dbt_object_name
      RAISING   /dmo/cx_rap_generator.

    METHODS is_alpha_numeric
      IMPORTING iv_string                  TYPE string
      RETURNING VALUE(rv_is_alpha_numeric) TYPE abap_bool.

    METHODS contains_no_blanks
      IMPORTING iv_string                    TYPE string
      RETURNING VALUE(rv_contains_no_blanks) TYPE abap_bool.

    METHODS underscore_at_pos_2_3
      IMPORTING iv_string                          TYPE string
      RETURNING VALUE(rv_no_underscore_at_pos_2_3) TYPE abap_bool.

    METHODS is_consistent
      RETURNING VALUE(rv_is_consistent) TYPE abap_bool.

    METHODS set_field_name_client
      IMPORTING iv_string TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS set_field_name_language
      IMPORTING iv_string TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS set_field_name_uuid
      IMPORTING iv_string TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS set_field_name_parent_uuid
      IMPORTING iv_string TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS set_field_name_root_uuid
      IMPORTING iv_string TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS set_field_name_created_by
      IMPORTING iv_string TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS set_field_name_created_at
      IMPORTING iv_string TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS set_field_name_last_changed_by
      IMPORTING iv_string TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS set_field_name_last_changed_at
      IMPORTING iv_string TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS set_field_name_loc_last_chg_at
      IMPORTING iv_string TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS set_field_name_loc_last_chg_by
      IMPORTING iv_string TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS set_field_name_etag_master
      IMPORTING iv_string TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS set_field_name_total_etag
      IMPORTING iv_string TYPE string
      RAISING   /dmo/cx_rap_generator.

    METHODS add_association
      IMPORTING
        iv_name             TYPE sxco_ddef_alias_name
        iv_target           TYPE sxco_cds_object_name
        it_condition_fields TYPE tt_condition_fields
        iv_cardinality      TYPE string
      RAISING
        /dmo/cx_rap_generator.


    METHODS add_valuehelp
      IMPORTING
        "alias used in service definition
        iv_alias              TYPE sxco_ddef_alias_name
        "name of CDS view used as value help
        iv_name               TYPE sxco_cds_object_name
        iv_localElement       TYPE sxco_cds_field_name
        iv_element            TYPE sxco_cds_field_name
        it_additional_Binding TYPE tt_addtionalbinding OPTIONAL
      RAISING
        /dmo/cx_rap_generator.

    METHODS add_additional_fields
      IMPORTING
        iv_object            TYPE string
        it_additional_fields TYPE tt_additional_fields.

    METHODS add_additional_fields_2
      IMPORTING
        it_additional_fields TYPE tt_additional_fields_2.

    METHODS add_additonal_to_all_fields.

    METHODS add_fields_to_all_fields.


    METHODS add_valuehelp_for_curr_quan.

    METHODS set_is_root_node
      "  IMPORTING io_is_root_node TYPE abap_bool OPTIONAL.
      IMPORTING io_is_root_node TYPE abap_bool DEFAULT abap_true.

    METHODS set_is_virtual_root_node
      IMPORTING io_is_root_node TYPE abap_bool OPTIONAL.

    METHODS set_object_id
      IMPORTING
        iv_object_id TYPE sxco_ad_field_name
      RAISING
        /dmo/cx_rap_generator.

    METHODS set_is_abstract_or_cust_entity
      IMPORTING iv_value TYPE abap_bool DEFAULT abap_true.

    METHODS is_abstract_or_custom_entity
      RETURNING VALUE(rv_is_abstract_or_cust_entity) TYPE abap_bool.

  PROTECTED SECTION.

    DATA is_test_run TYPE abap_bool.
    DATA implementationtype  TYPE string.
    DATA is_root_node        TYPE abap_bool.
    DATA is_virtual_root_node TYPE abap_bool.
    DATA is_child_node       TYPE abap_bool.
    DATA is_grand_child_node TYPE abap_bool.
    DATA bo_node_is_consistent  TYPE abap_bool.
    DATA keytype             TYPE string.


    METHODS right_string
      IMPORTING
                iv_length        TYPE i
                iv_string        TYPE string
      RETURNING VALUE(rv_string) TYPE string.

    METHODS set_number
      IMPORTING
                iv_number TYPE i
      RAISING   cx_parameter_invalid.

    METHODS admin_fields_exist
      RETURNING VALUE(rv_admin_fields_exists) TYPE abap_bool.

    METHODS field_name_exists_in_cds_view
      IMPORTING
                iv_field_name               TYPE string
      RETURNING VALUE(rv_field_name_exists) TYPE abap_bool.


    METHODS field_name_exists_in_db_table
      IMPORTING
                iv_field_name               TYPE string
      RETURNING VALUE(rv_field_name_exists) TYPE abap_bool.

    METHODS get_database_table_fields
      IMPORTING
        io_database_table TYPE REF TO if_xco_database_table
      EXPORTING
        et_fields         TYPE tt_fields_default_key  .

    METHODS get_field
      IMPORTING
                name            TYPE ts_field-name
      RETURNING VALUE(rs_field) TYPE ts_field.

    METHODS get_abap_type_components
      IMPORTING
                name             TYPE string
      RETURNING VALUE(et_fields) TYPE tt_fields_default_key  .

    METHODS get_structure_components
      IMPORTING
                io_components    TYPE REF TO if_xco_ad_structure
      RETURNING VALUE(et_fields)
                  TYPE tt_fields_default_key  .

    METHODS get_fields_cds_view
      IMPORTING
                io_cds_view_name TYPE sxco_cds_object_name
      RETURNING VALUE(et_fields)
                  TYPE tt_fields_default_key  .


    METHODS      read_data_element
      IMPORTING
        io_data_element TYPE REF TO if_xco_ad_data_element
        is_fields       TYPE ts_field
      EXPORTING
        es_fields       TYPE ts_field .

    METHODS      read_domain
      IMPORTING
        io_domain TYPE REF TO if_xco_domain
        is_fields TYPE ts_field
      EXPORTING
        es_fields TYPE ts_field.



  PRIVATE SECTION.
    DATA is_abstract_or_cust_entity TYPE abap_bool.
    METHODS set_repository_object_names.
ENDCLASS.



CLASS /dmo/cl_rap_node IMPLEMENTATION.


  METHOD set_data_source_type.

    CASE iv_data_source_type.

      WHEN 'table'.
        data_source_type = data_source_types-table.
      WHEN 'cds_view'.
        data_source_type = data_source_types-cds_view.
      WHEN 'abap_type'.
        data_source_type = data_source_types-abap_type.
      WHEN 'structure'.
        data_source_type = data_source_types-structure.
      WHEN OTHERS.

        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid   = /dmo/cx_rap_generator=>invalid_data_source_type
            mv_value = iv_data_source_type.

    ENDCASE.

  ENDMETHOD.

  METHOD get_valid_mbc_identifier.

    "lv_name will be shortened to 16 characters
    DATA lv_name TYPE string.
    DATA lv_entityname TYPE sxco_ddef_alias_name.
    DATA is_valid_mbc_identifier TYPE abap_bool.
    DATA li_counter TYPE i.

    IF iv_name IS INITIAL.
      "      DATA(lv_name) = ||.


      DATA(lv_mandatory_name_components) =   to_upper( prefix )  && to_upper( suffix  ).
      DATA(max_length_mandatory_name_comp) = 10.
      DATA(length_mandatory_name_comp) = strlen( lv_mandatory_name_components ).
      DATA(remaining_num_characters) = 20 - length_mandatory_name_comp.

      IF length_mandatory_name_comp > max_length_mandatory_name_comp.
        APPEND |{ lv_mandatory_name_components } mandatory components are too long more than { max_length_mandatory_name_comp } characters| TO lt_messages.
        bo_node_is_consistent = abap_false.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid        = /dmo/cx_rap_generator=>is_too_long
            mv_value      = |{ lv_mandatory_name_components } mandatory components for MBC identifier |
            mv_max_length = max_length_mandatory_name_comp.
      ENDIF.

      IF strlen( entityname ) > remaining_num_characters - 3.
        lv_entityname = substring( val = entityname len = remaining_num_characters - 3 ).
      ELSE.
        lv_entityname = entityname.
      ENDIF.

      is_valid_mbc_identifier = abap_false.

      li_counter       = 0.
      DATA(unique_hex_number) = CONV xstring( li_counter ).

      lv_name = |{ prefix }{ lv_entityname }{ unique_hex_number }{ suffix }|.
      lv_name = to_upper( lv_name ).

      WHILE is_valid_mbc_identifier = abap_false AND li_counter < 255 .
        "check if a table with this name alreardy exists.

        DATA(first_letter_mbc_namespace) = substring( val = me->namespace  len = 1 ).

        "The MBC registration API uses a namespace only if it is a "real" namespace.
        "If a customer namespace 'Y' or 'Z' is used or if
        "SAP objects are created such as I_Test that also do not have a namespace
        "then the MBC namespace must be initial.

        CASE first_letter_mbc_namespace.
          WHEN '/' .
            DATA(abap_object_mbc_name) = namespace && lv_name.
          WHEN 'Y' OR 'Z'.
            abap_object_mbc_name = namespace && lv_name.
          WHEN OTHERS.
            abap_object_mbc_name = lv_name.
        ENDCASE.

        SELECT * FROM I_CustABAPObjDirectoryEntry WHERE
        ABAPObject = @abap_object_mbc_name AND ABAPObjectCategory = 'R3TR' AND ABAPObjectType = 'SMBC' INTO TABLE @DATA(lt_smbc).

        IF lines( lt_smbc ) = 0.
          is_valid_mbc_identifier = abap_true.
        ENDIF.



*        IF NOT xco_lib->get_database_table( CONV #( lv_name ) )->exists( ).
*          is_valid_draft_table_name = abap_true.
*        ENDIF.
*
*        "check if a table with the same existis elsewhere in the BO
*        IF root_node->draft_table_name = lv_name.
*          is_valid_draft_table_name = abap_false.
*        ELSE.
*          "check if draft table name is used elsewhere in the BO
*          LOOP AT me->root_node->all_childnodes INTO DATA(lo_bo_node).
*            IF lo_bo_node->draft_table_name = lv_name.
*              is_valid_draft_table_name = abap_false.
*            ENDIF.
*          ENDLOOP.
*        ENDIF.
        IF is_valid_mbc_identifier = abap_false.
          li_counter       = li_counter + 1.
          unique_hex_number = CONV xstring( li_counter ).
          lv_name = |{ prefix }{ lv_entityname }{ unique_hex_number }{ suffix }|.
          lv_name = to_upper( lv_name ).
        ENDIF.
      ENDWHILE.

    ELSE.
      lv_name = iv_name.
    ENDIF.

    "check if name already exists within the BO


    check_repository_object_name(
     EXPORTING
       iv_type = 'SMBC'
       iv_name = lv_name
   ).

    "rap_node_objects-ddic_view_i = lv_name.
    rv_mbc_identifier = lv_name.
    "rv_ = lv_name.

  ENDMETHOD.

  METHOD get_valid_draft_table_name.

    "lv_name will be shortened to 16 characters
    DATA lv_name TYPE string.
    DATA lv_entityname TYPE sxco_ddef_alias_name.
    DATA is_valid_draft_table_name TYPE abap_bool.
    DATA li_counter TYPE i.

    IF iv_name IS INITIAL.
      "      DATA(lv_name) = ||.


      DATA(lv_mandatory_name_components) =  to_upper( namespace ) &&  to_upper( prefix )  && to_upper( suffix  ).
      DATA(max_length_mandatory_name_comp) = 10.
      DATA(length_mandatory_name_comp) = strlen( lv_mandatory_name_components ).
      DATA(remaining_num_characters) = 16 - length_mandatory_name_comp.

      IF length_mandatory_name_comp > max_length_mandatory_name_comp.
        APPEND |{ lv_mandatory_name_components } mandatory components are too long more than { max_length_mandatory_name_comp } characters| TO lt_messages.
        bo_node_is_consistent = abap_false.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid        = /dmo/cx_rap_generator=>is_too_long
            mv_value      = |{ lv_mandatory_name_components } mandatory components for draft table |
            mv_max_length = max_length_mandatory_name_comp.
      ENDIF.

      IF strlen( entityname ) > remaining_num_characters - 3.
        lv_entityname = substring( val = entityname len = remaining_num_characters - 3 ).
      ELSE.
        lv_entityname = entityname.
      ENDIF.


      is_valid_draft_table_name = abap_false.

      li_counter       = 0.
      DATA(unique_hex_number) = CONV xstring( li_counter ).
      "lv_name =  to_upper( namespace ) &&  to_upper( prefix )  && to_upper( lv_entityname ) && unique_hex_number && 'D' && to_upper( suffix  ).
      lv_name = |{ namespace }{ prefix }{ lv_entityname }{ unique_hex_number }D{ suffix }|.
      lv_name = to_upper( lv_name ).

      WHILE is_valid_draft_table_name = abap_false AND li_counter < 255 .
        "check if a table with this name alreardy exists.

        IF NOT xco_lib->get_database_table( CONV #( lv_name ) )->exists( ).
          is_valid_draft_table_name = abap_true.
        ENDIF.

        "check if a table with the same existis elsewhere in the BO
        IF root_node->draft_table_name = lv_name.
          is_valid_draft_table_name = abap_false.
        ELSE.
          "check if draft table name is used elsewhere in the BO
          LOOP AT me->root_node->all_childnodes INTO DATA(lo_bo_node).
            IF lo_bo_node->draft_table_name = lv_name.
              is_valid_draft_table_name = abap_false.
            ENDIF.
          ENDLOOP.
        ENDIF.
        IF is_valid_draft_table_name = abap_false.
          li_counter       = li_counter + 1.
          unique_hex_number = CONV xstring( li_counter ).
          "lv_name =  to_upper( namespace ) &&  to_upper( prefix )  && to_upper( lv_entityname ) && unique_hex_number && 'D' && to_upper( suffix  ).
          lv_name = |{ namespace }{ prefix }{ lv_entityname }{ unique_hex_number }D{ suffix }|.
          lv_name = to_upper( lv_name ).
        ENDIF.
      ENDWHILE.

    ELSE.
      lv_name = iv_name.
    ENDIF.

    "check if name already exists within the BO
    TEST-SEAM is_not_a_root_node.

    END-TEST-SEAM.

    check_repository_object_name(
     EXPORTING
       iv_type = 'TABL'
       iv_name = lv_name
   ).

    "rap_node_objects-ddic_view_i = lv_name.

    rv_ddic_i_view_name = lv_name.

  ENDMETHOD.


  METHOD set_draft_enabled.
    draft_enabled = iv_value.
  ENDMETHOD.


  METHOD set_draft_table.

    DATA(lv_table) = to_upper( iv_draft_table ) .

    check_repository_object_name(
      EXPORTING
         iv_type = 'TABL'
         iv_name = lv_table
     ).

    draft_table_name =  lv_table .

  ENDMETHOD.


  METHOD set_entity_name.

    DATA lt_all_childnodes  TYPE STANDARD TABLE OF REF TO /dmo/cl_rap_node .

    check_parameter(
          EXPORTING
            iv_parameter_name = 'Entity'                  ##NO_TEXT
            iv_value          = CONV #( iv_entity_name )
        ).

    IF me->root_node IS NOT INITIAL.

      lt_all_childnodes = me->root_node->all_childnodes.

      LOOP AT lt_all_childnodes INTO DATA(ls_childnode).
        IF ls_childnode->entityname = iv_entity_name.
          RAISE EXCEPTION TYPE /dmo/cx_rap_generator
            EXPORTING
              textid    = /dmo/cx_rap_generator=>entity_name_is_not_unique
              mv_entity = ls_childnode->entityname.
        ENDIF.
      ENDLOOP.

    ENDIF.

    entityname = iv_entity_name .
    rap_node_objects-alias = entityname.

  ENDMETHOD.


  METHOD set_field_name_created_at.
    check_parameter(
      EXPORTING
        iv_parameter_name = 'field_name-created_at'
        iv_value          = iv_string
    ).
    field_name-created_at = to_upper( iv_string ).
  ENDMETHOD.


  METHOD set_field_name_created_by.
    check_parameter(
      EXPORTING
        iv_parameter_name = 'field_name-created_by'
        iv_value          = iv_string
    ).
    field_name-created_by = to_upper( iv_string ).
  ENDMETHOD.


  METHOD set_field_name_last_changed_at.
    check_parameter(
      EXPORTING
        iv_parameter_name = 'field_name-last_changed_at'
        iv_value          = iv_string
    ).
    field_name-last_changed_at = to_upper( iv_string ).
  ENDMETHOD.


  METHOD set_field_name_last_changed_by.
    check_parameter(
      EXPORTING
        iv_parameter_name = 'field_name-last_changed_by'
        iv_value          = iv_string
    ).
    field_name-last_changed_by = to_upper( iv_string ).
  ENDMETHOD.


  METHOD set_field_name_loc_last_chg_at.
    check_parameter(
      EXPORTING
        iv_parameter_name = 'field_name-local_last_changed_at'
        iv_value          = iv_string
    ).
    field_name-local_instance_last_changed_at = to_upper( iv_string ).
  ENDMETHOD.


  METHOD set_field_name_loc_last_chg_by.
    check_parameter(
          EXPORTING
            iv_parameter_name = 'field_name-local_last_changed_by'
            iv_value          = iv_string
        ).
    field_name-local_instance_last_changed_by = to_upper( iv_string ).
  ENDMETHOD.


  METHOD set_field_name_etag_master.
    check_parameter(
          EXPORTING
            iv_parameter_name = 'field_name-etag_master'
            iv_value          = iv_string
        ).
    field_name-etag_master = to_upper( iv_string ).
  ENDMETHOD.


  METHOD set_field_name_total_etag.
    check_parameter(
          EXPORTING
            iv_parameter_name = 'field_name-total_etag'
            iv_value          = iv_string
        ).
    field_name-total_etag = to_upper( iv_string ).
  ENDMETHOD.


  METHOD set_field_name_parent_uuid.
    check_parameter(
      EXPORTING
        iv_parameter_name = 'field_name-parent_uuid'
        iv_value          = iv_string
    ).
    field_name-parent_uuid = to_upper( iv_string ).
  ENDMETHOD.


  METHOD set_field_name_root_uuid.
    check_parameter(
      EXPORTING
        iv_parameter_name = 'field_name-root_uuid'
        iv_value          = iv_string
    ).
    field_name-root_uuid = to_upper( iv_string ).
  ENDMETHOD.


  METHOD set_field_name_uuid.
    check_parameter(
          EXPORTING
            iv_parameter_name = 'field_name-uuid'
            iv_value          = iv_string
        ).
    field_name-uuid = to_upper( iv_string ).
  ENDMETHOD.


  METHOD set_implementation_type.

    CASE iv_implementation_type.

      WHEN implementation_type-managed_uuid.
        implementationtype = implementation_type-managed_uuid.
      WHEN implementation_type-managed_semantic.
        implementationtype = implementation_type-managed_semantic.
      WHEN implementation_type-unmanged_semantic.
        implementationtype = implementation_type-unmanged_semantic.
      WHEN OTHERS.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid   = /dmo/cx_rap_generator=>implementation_type_not_valid
            mv_value = iv_implementation_type.
    ENDCASE.

  ENDMETHOD.


  METHOD set_is_root_node.
    is_root_node = io_is_root_node.
    IF is_root_node = abap_true.
      set_root( me ).
      set_parent( me ).
    ENDIF.
  ENDMETHOD.


  METHOD set_mapping.
    "an automatic mapping can only be calculated if the data source is a table
    CLEAR lt_mapping.

    IF data_source_type = data_source_types-table
    OR data_source_type = data_source_types-structure
    OR data_source_type = data_source_types-abap_type.


      IF it_field_mappings IS NOT INITIAL.

        LOOP AT it_field_mappings INTO DATA(ls_field_mapping) WHERE dbtable_field  <> field_name-client.

          "field_is_not_in_datasource
          "field_is_not_in_cds_view

          IF field_name_exists_in_db_table( CONV #( ls_field_mapping-dbtable_field ) ) = abap_true.
            ls_mapping-dbtable_field = to_upper( ls_field_mapping-dbtable_field ).
            ls_mapping-cds_view_field =  ls_field_mapping-cds_view_field .

            "if external mapping is used
            " the name of the cds view field is being adapted to the field set by the external mapping
            " the automatic calculated mapping is adapted as well

            LOOP AT lt_fields ASSIGNING FIELD-SYMBOL(<field>) WHERE name = to_upper( ls_field_mapping-dbtable_field ).
              <field>-cds_view_field = ls_field_mapping-cds_view_field.
            ENDLOOP.

            INSERT ls_mapping INTO TABLE lt_mapping.

          ELSE.
            RAISE EXCEPTION TYPE /dmo/cx_rap_generator
              EXPORTING
                textid        = /dmo/cx_rap_generator=>field_is_not_in_datasource
                mv_table_name = CONV #( table_name )
                mv_value      = CONV #( ls_field_mapping-dbtable_field ).
          ENDIF.

        ENDLOOP.
      ENDIF.

      "add mapping for fields that have not been mapped externally
      LOOP AT lt_fields INTO  DATA(ls_fields).

        ls_mapping-dbtable_field =  ls_fields-name .
        ls_mapping-cds_view_field =  ls_fields-cds_view_field .

        DATA(mapping_exists) = xsdbool( line_exists( lt_mapping[ dbtable_field = ls_fields-name ] ) ).
        "boolc( line_exists( lt_fields[ name = lv_field_name_upper ] ) ).

        IF mapping_exists = abap_false AND ls_fields-name  <> field_name-client.
          INSERT ls_mapping INTO TABLE lt_mapping.
        ENDIF.
      ENDLOOP.


    ELSEIF data_source_type = data_source_types-cds_view AND it_field_mappings IS NOT INITIAL. "data source is a CDS view and mapping is defined

      LOOP AT it_field_mappings INTO ls_field_mapping.

        IF field_name_exists_in_db_table( CONV #( ls_field_mapping-dbtable_field ) ) = abap_false.
          RAISE EXCEPTION TYPE /dmo/cx_rap_generator
            EXPORTING
              textid        = /dmo/cx_rap_generator=>field_is_not_in_datasource
              mv_table_name = CONV #( table_name )
              mv_value      = CONV #( ls_field_mapping-dbtable_field ).
        ENDIF.

        IF field_name_exists_in_cds_view( CONV #( ls_field_mapping-cds_view_field ) ) = abap_false.
          RAISE EXCEPTION TYPE /dmo/cx_rap_generator
            EXPORTING
              textid    = /dmo/cx_rap_generator=>field_is_not_in_cds_view
              mv_entity = CONV #( entityname )
              mv_value  = CONV #( ls_field_mapping-dbtable_field ).
        ENDIF.

        ls_mapping-dbtable_field = ls_field_mapping-dbtable_field.
        ls_mapping-cds_view_field =  ls_field_mapping-cds_view_field .
        IF  ls_field_mapping-dbtable_field  <> field_name-client.
          INSERT ls_mapping INTO TABLE lt_mapping.
        ENDIF.
      ENDLOOP.

    ENDIF.
  ENDMETHOD.


  METHOD set_mbc_description.
    "  check_parameter(
    "    EXPORTING
    "      iv_parameter_name = 'manage_business_config_names-description'
    "      iv_value          = CONV string( iv_value )
    "  ).
    manage_business_config_names-description = iv_value.
  ENDMETHOD.


  METHOD set_mbc_identifier.
    check_repository_object_name(
      EXPORTING
        iv_type = 'SMBC'
        iv_name = iv_value
    ).

    DATA(first_letter_mbc_namespace) = substring( val = me->namespace  len = 1 ).

    "The MBC registration API uses a namespace only if it is a "real" namespace.
    "If a customer namespace 'Y' or 'Z' is used or if
    "SAP objects are created such as I_Test that also do not have a namespace
    "then the MBC namespace must be initial.

    CASE first_letter_mbc_namespace.
      WHEN '/' .
        " DATA(abap_object_mbc_name) = namespace && lv_name.
        manage_business_config_names-identifier = iv_value.
      WHEN 'Y' OR 'Z'.
        "abap_object_mbc_name = namespace && lv_name.
        manage_business_config_names-identifier = namespace && iv_value.
      WHEN OTHERS.
        "abap_object_mbc_name = lv_name.
        manage_business_config_names-identifier = iv_value.
    ENDCASE.




  ENDMETHOD.


  METHOD set_mbc_name.
    "  check_parameter(
    "    EXPORTING
    "      iv_parameter_name = 'manage_business_config_names-name'
    "      iv_value          =  iv_value
    "  ).
    manage_business_config_names-name = iv_value.
  ENDMETHOD.


  METHOD set_mbc_namespace.

    DATA(first_letter_mbc_namespace) = substring( val = me->namespace  len = 1 ).

    "The MBC registration API uses a namespace only if it is a "real" namespace.
    "If a customer namespace 'Y' or 'Z' is used or if
    "SAP objects are created such as I_Test that also do not have a namespace
    "then the MBC namespace must be initial.

    CASE first_letter_mbc_namespace.
      WHEN '/' .
        manage_business_config_names-namespace = namespace.
      WHEN 'Y' OR 'Z'.
        manage_business_config_names-namespace = ''.
      WHEN OTHERS.
        manage_business_config_names-namespace = ''.
    ENDCASE.

  ENDMETHOD.


  METHOD set_mde_name.

    IF iv_name IS INITIAL.
      DATA(lv_name) = |{ namespace }C_{ prefix }{ entityname }{ suffix }|.
    ELSE.
      lv_name = iv_name.
    ENDIF.


    IF lv_name IS INITIAL.
      APPEND | Projection view name is still initial | TO lt_messages.
      bo_node_is_consistent = abap_false.
    ENDIF.

    check_repository_object_name(
       EXPORTING
         iv_type = 'DDLX'
         iv_name = lv_name
     ).

    rap_node_objects-meta_data_extension = lv_name.

    rv_mde_name  = lv_name.

  ENDMETHOD.


  METHOD set_namespace.

    DATA(number_of_characters) = strlen( iv_namespace ).
    DATA(first_character) = substring( val = iv_namespace  len = 1 ).
    DATA(last_character) =  substring( val = iv_namespace off = number_of_characters - 1  len = 1 ).

    IF to_upper( first_character ) = 'Z' OR
       to_upper( first_character ) = 'Y'.
      check_parameter(
        EXPORTING
           iv_parameter_name = 'Namespace'
           iv_value          = CONV #( iv_namespace )
        ).


    ELSEIF first_character = '/' AND last_character = '/'.

      DATA(remaining_characters) = substring( val = iv_namespace off = 1  len = number_of_characters - 2 ).

      check_parameter(
        EXPORTING
           iv_parameter_name = 'Namespace without slashes'
           iv_value          = CONV #( remaining_characters )
        ).

    ELSE.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid   = /dmo/cx_rap_generator=>invalid_namespace
          mv_value = |iv_namespace|.
    ENDIF.

    namespace = iv_namespace.

  ENDMETHOD.


  METHOD set_number.
    node_number = iv_number.
  ENDMETHOD.


  METHOD set_object_id.

    check_parameter(
          EXPORTING
             iv_parameter_name = 'ObjectId'
             iv_value          = CONV #( iv_object_id )
          ).

    object_id = to_upper( iv_object_id ).

  ENDMETHOD.


  METHOD set_package.

    IF xco_lib->get_package( iv_package )->exists(  ) AND iv_package IS NOT INITIAL.
      package = iv_package.
      package = to_upper( package ).
    ELSE.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid   = /dmo/cx_rap_generator=>package_does_not_exist
          mv_value = CONV #( iv_package ).
    ENDIF.

    "set a suitable modifiable transport request for this package
    set_transport_request( iv_transport_request = CONV sxco_transport( transport_request ) ).

  ENDMETHOD.


  METHOD set_parent.
    IF io_parent_node IS NOT INITIAL.
      parent_node = io_parent_node.
    ELSE.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid            = /dmo/cx_rap_generator=>parameter_is_initial
          mv_parameter_name = 'Parent node' ##NO_TEXT.
    ENDIF.
  ENDMETHOD.


  METHOD set_persistent_table.

    DATA(lv_table) = to_upper( iv_persistent_table ) .

    persistent_table_name =  iv_persistent_table .

    IF data_source_type = data_source_types-table  OR
       data_source_type = data_source_types-cds_view.
      "check if table exists
      IF xco_lib->get_database_table(  CONV #( lv_table ) )->exists( ) = abap_false.
        APPEND | Table { lv_table } does not exist| TO lt_messages.
        bo_node_is_consistent = abap_false.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid   = /dmo/cx_rap_generator=>table_does_not_exist
            mv_value = CONV #( lv_table ).
      ENDIF.

      get_fields_persistent_table(  ).

      " ELSEIF data_source_type = data_source_types-structure.
      " @todo
      "
      " ELSEIF data_source_type = data_source_types-abap_type.
      " @todo

    ENDIF.




  ENDMETHOD.


  METHOD set_prefix.
    check_parameter(
      EXPORTING
         iv_parameter_name = 'Prefix'                  ##NO_TEXT
         iv_value          = CONV #( iv_prefix )
      ).

    prefix = iv_prefix.

  ENDMETHOD.


  METHOD set_publish_service.
    publish_service = iv_value.
  ENDMETHOD.


  METHOD set_root.
    IF  io_root_node IS INITIAL.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid            = /dmo/cx_rap_generator=>parameter_is_initial
          mv_parameter_name = 'Parent node' ##NO_TEXT.
    ENDIF.
    IF me <> io_root_node.
      root_node = io_root_node.
    ELSE.

      IF me->is_root(  ) .
        root_node = io_root_node.
      ELSE.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid    = /dmo/cx_rap_generator=>is_not_a_root_node
            mv_entity = io_root_node->entityname.
      ENDIF.
    ENDIF.

  ENDMETHOD.


  METHOD set_semantic_key_fields.
    DATA ls_semantic_key TYPE ts_semantic_key.
    IF it_semantic_key IS INITIAL.

      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid            = /dmo/cx_rap_generator=>parameter_is_initial
          mv_parameter_name = 'Semantic key field(s)' ##NO_TEXT.

    ELSE.

      CLEAR semantic_key.

      LOOP AT it_semantic_key INTO DATA(ls_semantic_key_field).

        "the cds view field name will be retrieved in the
        "finalize method because it can not
        "be assumed at this point that set_datasource
        "has already been called.
        "This is because JSON files are used as input where the order of items
        "is arbitrary
        "Hence the order of the methods for setting the values cannot be enforced
        "the semantic key field is  data base field. The name has to be converted
        "to uppercase since otherwise checks for field names will fail

        ls_semantic_key-name = to_upper( ls_semantic_key_field ).
        APPEND ls_semantic_key TO semantic_key.

      ENDLOOP.

    ENDIF.

  ENDMETHOD.


  METHOD set_service_binding_name.

    " From SAP Online Help
    " Use the prefix
    " UI_ if the service is exposed as a UI service.
    " API_ if the service is exposed as Web API.
    " Use the suffix
    " _O2 if the service is bound to OData protocol version 2.
    " _O4 if the service is bound to OData protocol version 4.
    " Example: /DMO/UI_TRAVEL_U_O2

    DATA protocol_version TYPE string.
    DATA binding TYPE string.

    CASE binding_type.
      WHEN binding_type_name-odata_v2_ui.
        protocol_version = protocol_version_suffix-odata_v2.
        binding = binding_type_prefix-ui .
      WHEN binding_type_name-odata_v4_ui.
        protocol_version = protocol_version_suffix-odata_v4.
        binding = binding_type_prefix-ui.
      WHEN binding_type_name-odata_v2_web_api.
        protocol_version = protocol_version_suffix-odata_v2.
        binding = binding_type_prefix-web_api.
      WHEN binding_type_name-odata_v4_web_api.
        protocol_version = protocol_version_suffix-odata_v4.
        binding = binding_type_prefix-web_api.
    ENDCASE.

    IF iv_name IS INITIAL.
      DATA(lv_name) = |{ namespace }{ binding }{ prefix }{ entityname }{ suffix }{ protocol_version }|.
    ELSE.
      lv_name = iv_name.
    ENDIF.

    IF rap_root_node_objects-service_definition IS INITIAL.
      APPEND | service binding name is still initial | TO lt_messages.
      bo_node_is_consistent = abap_false.
    ENDIF.

    check_repository_object_name(
       EXPORTING
         iv_type = 'SRVB'
         iv_name = lv_name
     ).


    IF is_root( ).
      rap_root_node_objects-service_binding = lv_name.
      rv_service_binding_name = lv_name.
    ELSEIF is_test_run = abap_true.
      rap_root_node_objects-service_binding = lv_name.
      rv_service_binding_name = lv_name.
    ELSE.
      APPEND | { me->entityname } is not a root node. Service binding can only be created for the root node| TO lt_messages.
      bo_node_is_consistent = abap_false.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid    = /dmo/cx_rap_generator=>is_not_a_root_node
          mv_entity = me->entityname.
    ENDIF.

  ENDMETHOD.


  METHOD set_service_definition_name.

    " Since a service definition - as a part of a business service - does not have different types or different specifications, there is (in general) no need for a prefix or suffix to differentiate meaning.
    " Example: /DMO/TRAVEL_U
    " However, in use cases where no reuse of the same service definition is planned for UI and API services, the prefix may follow the rules of the service binding.
    " Example: /DMO/UI_TRAVEL_U

    IF iv_name IS INITIAL.
      DATA(lv_name) = |{ namespace }{ prefix }{ entityname }{ suffix }|.
    ELSE.
      lv_name = iv_name.
    ENDIF.

    check_repository_object_name(
          EXPORTING
            iv_type = 'SRVD'
            iv_name = lv_name
        ).


    IF is_root( ).
      rap_root_node_objects-service_definition = lv_name.
      rv_service_definition_name = lv_name.
    ELSEIF is_test_run = abap_true.
      rap_root_node_objects-service_definition = lv_name.
      rv_service_definition_name = lv_name.
    ELSE.
      APPEND | { me->entityname } is not a root node. Service defintion can only be created for the root node| TO lt_messages.
      bo_node_is_consistent = abap_false.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid    = /dmo/cx_rap_generator=>is_not_a_root_node
          mv_entity = me->entityname.
    ENDIF.



  ENDMETHOD.


  METHOD set_suffix.

    check_parameter(
      EXPORTING
         iv_parameter_name = 'Prefix'              ##NO_TEXT
         iv_value          = CONV #( iv_suffix )
      ).
    IF iv_suffix IS NOT INITIAL.
      suffix = |{ iv_suffix }| .
    ELSE.
      suffix = iv_suffix.
    ENDIF.

  ENDMETHOD.


  METHOD set_table.

    DATA(lv_table) = to_upper( iv_table ) .

    TEST-SEAM omit_table_existence_check.

      "check if table exists and table has an active version
      IF xco_lib->get_database_table( CONV #( lv_table ) )->exists( ) = abap_false .
        APPEND | Table { lv_table } does not exist| TO lt_messages ##NO_TEXT .
        bo_node_is_consistent = abap_false.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid   = /dmo/cx_rap_generator=>table_does_not_exist
            mv_value = lv_table.
      ENDIF.

      DATA(table_state) = xco_lib->get_database_table( CONV #( lv_table ) )->get_state( xco_cp_abap_dictionary=>object_read_state->active_version ).

      DATA(check_state_active) =  xco_cp_abap_dictionary=>object_state->active.

      IF  table_state <> xco_cp_abap_dictionary=>object_state->active.
        APPEND | Table { lv_table } is not active | TO lt_messages ##NO_TEXT .
        bo_node_is_consistent = abap_false.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid   = /dmo/cx_rap_generator=>table_is_inactive
            mv_value = lv_table.
      ENDIF.
    END-TEST-SEAM.

    table_name = lv_table.

    set_persistent_table( CONV #( lv_table ) ).

    get_fields(  ).




  ENDMETHOD.


  METHOD set_transport_request.

    "set_transport request is also called at end of set_package( )
    "this method will try to reuse any suitable modifiable transport that already exists for that package and that
    "is owned by the developer
    "If nevertheless a transport request is set externally this will overrule the automatic selection
    "If no transport can be found a new transport will be generated

    IF me->package IS NOT INITIAL.

      DATA(record_object_changes) = xco_lib->get_package( me->package  )->read( )-property-record_object_changes.

      IF record_object_changes = abap_false AND iv_transport_request IS NOT INITIAL.
        DATA(error_details) = |{ me->package } does not record changes.|.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid     = /dmo/cx_rap_generator=>invalid_transport_request
            mv_value   = CONV #( iv_transport_request )
            mv_value_2 = error_details.
      ELSEIF record_object_changes = abap_false AND iv_transport_request IS INITIAL..
        EXIT.
      ENDIF.
    ELSE.
      IF me->transport_request IS INITIAL.
        "no package set, no transport can be set
        EXIT.
      ENDIF.
    ENDIF.


    "if transport request is provided take this one
    IF iv_transport_request IS NOT INITIAL.

      DATA(transport_object) = xco_cp_cts=>transport->for( iv_transport_request ).

      IF transport_object->exists(  ) = abap_false.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid   = /dmo/cx_rap_generator=>transport_does_not_exist
            mv_value = CONV #( iv_transport_request ).
      ENDIF.

      DATA(transport_status) = transport_object->get_status(  )->value.
      DATA(transport_desired_status) = xco_cp_transport=>status->modifiable->value.

      error_details = | Transport request is not modifiable.|.

      IF  transport_status =  transport_desired_status .
        transport_request = iv_transport_request.
      ELSE.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid     = /dmo/cx_rap_generator=>invalid_transport_request
            mv_value   = CONV #( iv_transport_request )
            mv_value_2 = error_details.
      ENDIF.

      "check if there is a modifiable transport request for this developer and this package
    ELSEIF me->package IS NOT INITIAL.

      IF xco_lib->get_package( me->package  )->read( )-property-record_object_changes = abap_true.

        DATA(lo_user) = xco_cp=>sy->user( ).

        DATA(lo_transport_target) = xco_lib->get_package( me->package
          )->read( )-property-transport_layer->get_transport_target( ).

        DATA(lo_status_filter) = xco_cp_transport=>filter->status( xco_cp_transport=>status->modifiable ).
        DATA(lo_owner_filter) = xco_cp_transport=>filter->owner( xco_cp_abap_sql=>constraint->equal( lo_user->name ) ).
        DATA(lo_request_type_filter) = xco_cp_transport=>filter->request_type( xco_cp_transport=>type->workbench_request ).
        DATA(lo_request_target_filter) = xco_cp_transport=>filter->request_target( xco_cp_abap_sql=>constraint->equal( lo_transport_target->value ) ).

        DATA(lt_transports) = xco_cp_cts=>transports->where( VALUE #(
          ( lo_status_filter )
          ( lo_owner_filter )
          ( lo_request_type_filter )
          ( lo_request_target_filter )
        ) )->resolve( xco_cp_transport=>resolution->request ).

        "similar logic as in ADT. Select the first suitable transport request
        "and only if no modifiable transport request for the transport target can be found
        "create a new transport request for the transport target

        IF lt_transports IS NOT INITIAL.
          transport_request = lt_transports[ 1 ]->value.
        ELSE.
          DATA(new_transport_object) = xco_cp_cts=>transports->workbench( lo_transport_target->value  )->create_request( |RAP Business object - entity name: { me->root_node->entityname } | ).
          transport_request = new_transport_object->value.
        ENDIF.

      ENDIF.

    ENDIF.


  ENDMETHOD.


  METHOD set_xco_lib.
    xco_lib = io_xco_lib.
  ENDMETHOD.


  METHOD validate_bo.

    IF data_source_type = data_source_types-table.
      "check if the client field (usually CLNT does exist

      SELECT * FROM @lt_fields AS fields WHERE name  = @field_name-client AND
                                               key_indicator = @abap_true
      INTO TABLE @DATA(result_client) .

      IF result_client IS INITIAL.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid   = /dmo/cx_rap_generator=>clnt_is_not_key_field
            mv_value = field_name-client.
      ENDIF.
    ENDIF.



    "avoid error
    "ETag delegation not supported for unmanaged query implementation
    IF ( is_child( ) OR is_grand_child_or_deeper(  ) ) AND
        generate_custom_entity(  ).
      IF NOT line_exists( lt_fields[ name = field_name-etag_master ] ).
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid    = /dmo/cx_rap_generator=>field_etag_master_missing
            mv_entity = entityname
            mv_value  = field_name-etag_master.
      ENDIF.
    ENDIF.
    "validate uuid key field structure, domains and names

    DATA key_fields TYPE string.

    IF implementationtype = implementation_type-managed_uuid.

      SELECT * FROM @lt_fields AS fields WHERE name  = @field_name-uuid INTO TABLE @DATA(result_uuid).

      IF result_uuid IS INITIAL.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid   = /dmo/cx_rap_generator=>field_uuid_missing
            mv_value = CONV #( field_name-uuid ).
      ENDIF.

      DATA(numberOfRecords) = lines( result_uuid ).
      "the underlying built in type must be of type RAW and length 16
      "@todo: the check for the data element can be removed once we can check for
      "the built in type of a non released domain

      IF numberOfRecords = 1 AND ( result_uuid[ 1 ]-data_element = 'SYSUUID_X16' OR
                                   result_uuid[ 1 ]-data_element = 'XSDUUID_RAW' ).
        " that's ok
      ELSEIF numberOfRecords = 1 AND
         (  result_uuid[ 1 ]-built_in_type_length <> uuid_length OR result_uuid[ 1 ]-built_in_type <> uuid_type ).
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid   = /dmo/cx_rap_generator=>uuid_has_invalid_data_type
            mv_value = CONV #( field_name-uuid ).
      ENDIF.

      SELECT * FROM @lt_fields AS fields WHERE key_indicator  = @abap_true
                                           AND name <> @field_name-client
                                           INTO TABLE @result_uuid.

      IF result_uuid IS INITIAL.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid    = /dmo/cx_rap_generator=>has_no_key_field
            mv_entity = entityname.
      ENDIF.

      numberOfRecords = lines( result_uuid ).


      IF numberOfRecords = 1 AND  result_uuid[ 1 ]-name <> field_name-uuid.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid    = /dmo/cx_rap_generator=>uuid_is_not_key_field
            mv_entity = entityname
            mv_value  = field_name-uuid.
      ENDIF.

      IF numberOfRecords > 1.

        LOOP AT result_uuid INTO DATA(result_uuid_line).
          IF key_fields IS INITIAL.
            key_fields =  result_uuid_line-name.
          ELSE.
            key_fields =  key_fields && ',' && result_uuid_line-name.
          ENDIF.
        ENDLOOP.

        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid    = /dmo/cx_rap_generator=>more_than_one_key_field
            mv_entity = entityname
            mv_value  = key_fields.
      ENDIF.



      IF is_child( ) OR is_grand_child_or_deeper(  ).

        SELECT * FROM @lt_fields AS fields WHERE name  = @field_name-parent_uuid INTO TABLE @DATA(result_parent_uuid).

        IF result_parent_uuid IS INITIAL.
          RAISE EXCEPTION TYPE /dmo/cx_rap_generator
            EXPORTING
              textid   = /dmo/cx_rap_generator=>field_parent_uuid_missing
              mv_value = CONV #( field_name-parent_uuid ).
        ENDIF.

        numberOfRecords = lines( result_parent_uuid ).

        IF numberOfRecords = 1 AND  ( result_parent_uuid[ 1 ]-data_element = 'SYSUUID_X16' OR
                                      result_parent_uuid[ 1 ]-data_element = 'XSDUUID_RAW' ).
          " that's ok
        ELSEIF numberOfRecords = 1 AND
           ( result_parent_uuid[ 1 ]-built_in_type_length <> uuid_length OR result_parent_uuid[ 1 ]-built_in_type <> uuid_type ).
          RAISE EXCEPTION TYPE /dmo/cx_rap_generator
            EXPORTING
              textid   = /dmo/cx_rap_generator=>uuid_has_invalid_data_type
              mv_value = CONV #( field_name-parent_uuid ).
        ENDIF.

      ENDIF.

      IF is_grand_child_or_deeper(  ).

        SELECT * FROM @lt_fields AS fields WHERE name  = @field_name-root_uuid INTO TABLE @DATA(result_root_uuid).

        IF result_root_uuid IS INITIAL.
          RAISE EXCEPTION TYPE /dmo/cx_rap_generator
            EXPORTING
              textid   = /dmo/cx_rap_generator=>field_root_uuid_missing
              mv_value = CONV #( field_name-root_uuid ).
        ENDIF.

        numberOfRecords = lines( result_root_uuid ).

        IF numberOfRecords = 1 AND  ( result_root_uuid[ 1 ]-data_element = 'SYSUUID_X16' OR
                                      result_root_uuid[ 1 ]-data_element = 'XSDUUID_RAW' ).

          " that's ok
        ELSEIF numberOfRecords = 1 AND
           ( result_root_uuid[ 1 ]-built_in_type_length <> uuid_length OR result_root_uuid[ 1 ]-built_in_type <> uuid_type ).
          RAISE EXCEPTION TYPE /dmo/cx_rap_generator
            EXPORTING
              textid   = /dmo/cx_rap_generator=>uuid_has_invalid_data_type
              mv_value = CONV #( field_name-root_uuid ).
        ENDIF.

      ENDIF.


    ENDIF.


    "validate if a name for the draft_table has been specified

    IF me->draft_enabled = abap_true AND me->draft_table_name IS INITIAL.

      draft_table_name = get_valid_draft_table_name(  ).

      IF draft_table_name IS INITIAL.

        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid         = /dmo/cx_rap_generator=>no_draft_table_specified
            mv_root_entity = me->root_node->entityname
            mv_entity      = me->entityname.
      ENDIF.
    ENDIF.




    IF root_node->draft_enabled = abap_true.

      "validate if total etag field is present in the root entity of the draft enabled BO
      IF is_root(  ).

        IF line_exists( lt_fields[ name = field_name-total_etag  ] ).
          "DATA(last_changed_at) = lt_fields[ name = field_name-last_changed_at ]-cds_view_field.
        ELSEIF line_exists( lt_additional_fields[ name = field_name-total_etag ] ).
          "last_changed_at = lt_additional_fields[ name = field_name-last_changed_at ]-cds_view_field.
        ELSE.
          RAISE EXCEPTION TYPE /dmo/cx_rap_generator
            EXPORTING
              textid    = /dmo/cx_rap_generator=>field_total_etag_missing
              mv_entity = entityname.
        ENDIF.

      ENDIF.

      "validate if local etag field is present in each node of the draft enabled BO
      " remove this check and use etag _dependent by instead
*      IF line_exists( lt_fields[ name = field_name-local_instance_last_changed_at ] ).
*        "DATA(last_changed_at) = lt_fields[ name = field_name-last_changed_at ]-cds_view_field.
*      ELSEIF line_exists( lt_additional_fields[ name = field_name-local_instance_last_changed_at ] ).
*        "last_changed_at = lt_additional_fields[ name = field_name-last_changed_at ]-cds_view_field.
*      ELSE.
*        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
*          EXPORTING
*            textid    = /dmo/cx_rap_generator=>field_local_etag_missing
*            mv_value  = field_name-local_instance_last_changed_at
*            mv_entity = entityname.
*      ENDIF.


    ENDIF.

    "check if an etag has been specified
    IF line_exists( lt_fields[ name = field_name-etag_master ] ).
    ELSEIF line_exists( lt_additional_fields[ name = field_name-etag_master ] ).
    ELSE.
      IF is_root(  ).
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid    = /dmo/cx_rap_generator=>field_etag_master_missing
            mv_entity = entityname.
      ELSE.
        APPEND |In entity: { entityname } no etag field has been specified { field_name-created_by } | TO lt_messages.
      ENDIF.
    ENDIF.

    "created_by            : syuname;
    "last_changed_by       : syuname;
    "local_last_changed_at : timestampl;

    IF  implementationtype = implementation_type-managed_semantic OR
        implementationtype = implementation_type-managed_uuid.
      IF is_root(  ).
        IF line_exists( lt_fields[ name = field_name-created_by ] ).
        ELSEIF line_exists( lt_additional_fields[ name = field_name-created_by ] ).
        ELSE.
          APPEND |{ entityname } is a managed BO. But { field_name-created_by } is not mapped| TO lt_messages.
        ENDIF.

        IF line_exists( lt_fields[ name = field_name-created_at ] ).
        ELSEIF line_exists( lt_additional_fields[ name = field_name-created_at ] ).
        ELSE.
          APPEND |{ entityname } is a managed BO. But { field_name-created_at } is not mapped| TO lt_messages.
        ENDIF.

        IF line_exists( lt_fields[ name = field_name-last_changed_by ] ).
        ELSEIF line_exists( lt_additional_fields[ name = field_name-last_changed_by ] ).
        ELSE.
          APPEND |{ entityname } is a managed BO. But { field_name-last_changed_by } is not mapped| TO lt_messages.
        ENDIF.

        IF line_exists( lt_fields[ name = field_name-last_changed_at ] ).
        ELSEIF line_exists( lt_additional_fields[ name = field_name-last_changed_at ] ).
        ELSE.
          APPEND |{ entityname } is a managed BO. But { field_name-last_changed_at } is not mapped| TO lt_messages.
        ENDIF.
      ENDIF.
      IF line_exists( lt_fields[ name = field_name-local_instance_last_changed_at ] ).
      ELSEIF line_exists( lt_additional_fields[ name = field_name-local_instance_last_changed_at ] ).
      ELSE.
        APPEND |{ entityname } is a managed BO. But { field_name-local_instance_last_changed_at } is not mapped| TO lt_messages.
      ENDIF.

    ENDIF.

    "created_by            : syuname;
    "created_at            : timestampl;
    "last_changed_by       : syuname;
    "last_changed_at       : timestampl;
    "local_last_changed_at : timestampl;




    "validate value helps

    DATA lv_target TYPE string.
    DATA ls_valuehelp TYPE ts_valuehelp.
    FIELD-SYMBOLS: <fields> TYPE ts_field.

    LOOP AT lt_valuehelp INTO ls_valuehelp.

      lv_target = to_upper( ls_valuehelp-name ).

      SELECT * FROM I_APIsForSAPCloudPlatform WHERE ReleasedObjectType = 'CDS_STOB' AND ReleasedObjectName = @lv_target INTO TABLE @DATA(lt_result)..

      "check if CDS view used as target exists
      IF NOT ( lt_result IS NOT INITIAL OR xco_lib->get_data_definition( CONV #(  lv_target ) )->exists( ) ).
        APPEND | CDS View {  lv_target  } does not exist | TO lt_messages.
        bo_node_is_consistent = abap_false.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid   = /dmo/cx_rap_generator=>cds_view_does_not_exist
            mv_value = CONV #( lv_target ).
      ENDIF.

      "@todo - check if table name can be omitted for
      "BO's that have structure as a data source
      IF table_name IS INITIAL.
        CASE   data_source_type.
          WHEN  data_source_types-structure.
          WHEN  data_source_types-abap_type.
          WHEN  data_source_types-cds_view.
          WHEN OTHERS.
            RAISE EXCEPTION TYPE /dmo/cx_rap_generator
              EXPORTING
                textid = /dmo/cx_rap_generator=>no_table_set.
        ENDCASE.
      ENDIF.

      IF NOT field_name_exists_in_cds_view( CONV #(  ls_valuehelp-localelement  ) ).
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid    = /dmo/cx_rap_generator=>not_a_field_in_cds_view
            mv_value  = CONV #( ls_valuehelp-localelement )
            mv_entity = me->entityname.
      ENDIF.

    ENDLOOP.

    "validate associations

    LOOP AT lt_association INTO DATA(ls_assocation).

      lv_target = to_upper( ls_assocation-target ).

      SELECT * FROM I_APIsForSAPCloudPlatform WHERE ReleasedObjectType = 'CDS_STOB' AND ReleasedObjectName = @lv_target INTO TABLE @lt_result.

      "check if CDS view used as target exists
      IF NOT ( lt_result IS NOT INITIAL OR xco_lib->get_data_definition( CONV #(  lv_target ) )->exists( ) ).
        APPEND | CDS View {  lv_target  } does not exist | TO lt_messages.
        bo_node_is_consistent = abap_false.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid   = /dmo/cx_rap_generator=>cds_view_does_not_exist
            mv_value = CONV #( lv_target ).
      ENDIF.


      LOOP AT ls_assocation-condition_components INTO DATA(ls_condition_fields).
        IF NOT field_name_exists_in_cds_view( CONV #( ls_condition_fields-projection_field ) ).
          RAISE EXCEPTION TYPE /dmo/cx_rap_generator
            EXPORTING
              textid    = /dmo/cx_rap_generator=>not_a_field_in_cds_view
              mv_value  = CONV #( ls_condition_fields-projection_field )
              mv_entity = me->entityname.
        ENDIF.
      ENDLOOP.
    ENDLOOP.

    "validate object id
    IF object_id IS INITIAL.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid    = /dmo/cx_rap_generator=>no_object_id_set
          mv_entity = entityname.
    ELSE.
      DATA object_id_upper_case  TYPE sxco_ad_field_name.
      object_id_upper_case = to_upper( object_id ).

      SELECT SINGLE * FROM @lt_fields AS db_field WHERE name  = @object_id_upper_case INTO @DATA(result).
      IF result IS INITIAL.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid        = /dmo/cx_rap_generator=>field_is_not_in_datasource
            mv_value      = CONV #( object_id_upper_case )
            mv_table_name = CONV #( table_name ).
      ENDIF.

      object_id_cds_field_name = result-cds_view_field.

    ENDIF.

    "validate uuid key field

    IF implementationtype = implementation_type-managed_uuid.

    ENDIF.

    " validate semantic key fields

    IF implementationtype = implementation_type-unmanged_semantic OR
            implementationtype = implementation_type-managed_semantic.

      IF semantic_key IS INITIAL.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid = /dmo/cx_rap_generator=>no_semantic_key_set.
      ENDIF.

      FIELD-SYMBOLS <ls_semantic_key> LIKE LINE OF semantic_key.

      LOOP AT semantic_key ASSIGNING <ls_semantic_key>.

        SELECT SINGLE * FROM @lt_fields AS SemanticKeyAlias WHERE name  = @<ls_semantic_key>-name INTO @DATA(resultSemanticKeyAlias).

        IF resultSemanticKeyAlias IS INITIAL.
          RAISE EXCEPTION TYPE /dmo/cx_rap_generator
            EXPORTING
              textid                = /dmo/cx_rap_generator=>sematic_key_is_not_in_table
              mv_semantic_key_field = CONV #( <ls_semantic_key>-name )
              mv_table_name         = CONV #( table_name ).
        ELSE.
          <ls_semantic_key>-cds_view_field = resultSemanticKeyAlias-cds_view_field.
        ENDIF.
        CLEAR resultSemanticKeyAlias.
      ENDLOOP.

      "mark semantic key fields as key fields in lt_fields
      IF data_source_type = data_source_types-structure OR
         data_source_type = data_source_types-abap_type.
        LOOP AT semantic_key INTO DATA(semantic_key_field).
          LOOP AT lt_fields ASSIGNING FIELD-SYMBOL(<line>) WHERE name = semantic_key_field-name.
            <line>-key_indicator = abap_true.
          ENDLOOP.
        ENDLOOP.
      ENDIF.


    ENDIF.

    "validate mapping

    LOOP AT lt_mapping INTO DATA(ls_field_mapping).

      DATA(lv_dbtablefield) = to_upper( ls_field_mapping-dbtable_field ).


      "check if database table field is part of the persistence table
      "if table is set as datasource it is automatically set as persistence table
      "if an unmanaged scenario is used no mapping can be derived from the data source
      "or from the persistence table
      IF implementationtype <> implementation_type-unmanged_semantic.
        SELECT SINGLE * FROM @lt_fields_persistent_table AS db_field WHERE name  = @lv_dbtablefield INTO @DATA(result_dbtable_field).

        IF result_dbtable_field IS INITIAL.
          RAISE EXCEPTION TYPE /dmo/cx_rap_generator
            EXPORTING
              textid        = /dmo/cx_rap_generator=>field_is_not_in_datasource
              mv_value      = CONV #( ls_field_mapping-dbtable_field )
              mv_table_name = CONV #( table_name ).
        ENDIF.
        CLEAR result_dbtable_field.
      ENDIF.


      SELECT SINGLE * FROM @lt_fields AS cds_view_field WHERE cds_view_field  = @ls_field_mapping-cds_view_field INTO @DATA(result_cds_view_field).
      IF result_cds_view_field IS INITIAL.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid    = /dmo/cx_rap_generator=>field_is_not_in_cds_view
            mv_value  = CONV #( ls_field_mapping-cds_view_field )
            mv_entity = CONV #( rap_node_objects-cds_view_i ).
      ENDIF.
      CLEAR result_cds_view_field.
    ENDLOOP.

    "check prerequisites for manage business configuration app

    IF me->manage_business_configuration = abap_true.

      IF me->draft_enabled = abap_false.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid   = /dmo/cx_rap_generator=>not_draft_enabled
            mv_value = CONV #( me->root_node->entityname ).
      ENDIF.

      IF me->binding_type <> binding_type_name-odata_v4_ui.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid   = /dmo/cx_rap_generator=>no_ui_v4_service_binding
            mv_value = CONV #( me->root_node->entityname ).
      ENDIF.



    ENDIF.

    IF me->root_node->publish_service = abap_true
       AND me->root_node->skip_activation = abap_true.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid = /dmo/cx_rap_generator=>publish_needs_active_srvd.

      .
    ENDIF.

    "validate settings for customizing table and mbc app

    IF is_customizing_table = abap_true AND is_grand_child_or_deeper(  ).
      "&1 Grandchild nodes are not supported for &2 = &3.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid     = /dmo/cx_rap_generator=>grand_child_not_supported
          mv_entity  = entityname
          mv_value   = 'iscustomizingtable'
          mv_value_2 = 'abap_true'.

    ENDIF.

    IF manage_business_configuration = abap_true AND  is_grand_child_or_deeper(  ).
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid     = /dmo/cx_rap_generator=>grand_child_not_supported
          mv_entity  = entityname
          mv_value   = 'addtomanagebusinessconfiguration'
          mv_value_2 = 'abap_true'.
    ENDIF.

    IF data_source_type = data_source_types-structure.



    ENDIF.

    IF multi_edit = abap_true AND
       ( binding_type <> binding_type_name-odata_v4_ui OR
         draft_enabled = abap_false ).

      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid    = /dmo/cx_rap_generator=>mult_edit_not_supported
          mv_entity = entityname.

    ENDIF.

    IF is_customizing_table = abap_true.

      DATA(customizing_database_table) = xco_lib->get_database_table( iv_name = table_name  ).

      DATA(delivery_class) = customizing_database_table->content( )->get_delivery_class(  )->value.

      IF delivery_class <> 'C'.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid     = /dmo/cx_rap_generator=>delivery_class_c_required
            mv_value   = CONV #( table_name )
            mv_value_2 = CONV #( delivery_class ).
      ENDIF.

    ENDIF.

  ENDMETHOD.


  METHOD set_data_source.

    CASE data_source_type.
      WHEN data_source_types-table.
        set_table( CONV sxco_ar_object_name( iv_data_source ) ).
      WHEN data_source_types-cds_view.
        set_cds_view( CONV sxco_cds_object_name( iv_data_source ) ).
      WHEN data_source_types-structure.
        set_structure( CONV sxco_ad_object_name( iv_data_source ) )  .
      WHEN data_source_types-abap_type.
        set_abap_type( iv_data_source ).
      WHEN OTHERS.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid = /dmo/cx_rap_generator=>invalid_data_source_type.
    ENDCASE.
    data_source_name = iv_data_source .


  ENDMETHOD.


  METHOD add_additional_fields.


    DATA lv_object TYPE string.
    DATA ls_additional_fields TYPE ts_additional_fields.
    DATA ls_object_with_add_fields  TYPE ts_objects_with_add_fields.

    CASE to_lower( iv_object ).

      WHEN additional_fields_object_types-cds_interface_view. "'CDS_INTERFACE_VIEW'.
      WHEN additional_fields_object_types-cds_projection_view.
      WHEN additional_fields_object_types-draft_table.
      WHEN OTHERS.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid   = /dmo/cx_rap_generator=>cannot_add_additional_fields
            mv_value = iv_object.
    ENDCASE.

    ls_object_with_add_fields-object = iv_object.
    ls_object_with_add_fields-additional_fields = it_additional_fields.

    APPEND ls_object_with_add_fields TO lt_objects_with_add_fields.

  ENDMETHOD.


  METHOD add_association.
    DATA lv_target TYPE string.
    DATA ls_assocation TYPE ts_assocation.

    check_parameter(
      EXPORTING
        iv_parameter_name = 'Association'         ##NO_TEXT
        iv_value          = CONV #( iv_name )
    ).

    lv_target = to_upper( iv_target ).

    DATA(underscore) = substring( val = iv_name  len = 1 ).

    IF underscore <> '_'.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid   = /dmo/cx_rap_generator=>starts_not_with_underscore
          mv_value = CONV #( iv_name ).
    ENDIF.


    IF  iv_cardinality = cardinality-one OR iv_cardinality = cardinality-one_to_n OR
             iv_cardinality = cardinality-zero_to_n OR iv_cardinality = cardinality-zero_to_one
             OR iv_cardinality = cardinality-one_to_one.
      ls_assocation-cardinality = iv_cardinality.
    ELSE.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid   = /dmo/cx_rap_generator=>assocation_is_not_supported
          mv_value = iv_cardinality.
    ENDIF.

    FIELD-SYMBOLS: <fields> TYPE ts_field.

    "we only support the simple case where the condition contains only one field
    " IF lines( it_condition_fields ) = 1.
    LOOP AT lt_fields  ASSIGNING <fields> WHERE cds_view_field = it_condition_fields[ 1 ]-projection_field.
      <fields>-has_association = abap_true.
    ENDLOOP.

    "Make sure that the association is also using UpperCamelCase
    "IF useuppercamelcase = abap_true.
    "  ls_assocation-name = xco_cp=>string( iv_name )->split( '_' )->compose( xco_cp_string=>composition->pascal_case )->value.
    "ELSE.
    ls_assocation-name = iv_name.
    "ENDIF.
    ls_assocation-target = iv_target.
    ls_assocation-condition_components = it_condition_fields.

    APPEND  ls_assocation TO lt_association.

    " ENDIF.

  ENDMETHOD.


  METHOD add_child.

    DATA lt_all_childnodes  TYPE STANDARD TABLE OF REF TO /dmo/cl_rap_node .

    DATA   ls_childnode  TYPE REF TO /dmo/cl_rap_node  .

    ro_child_node = NEW /dmo/cl_rap_node( ).


    "get settings from parent node
    ro_child_node->set_parent( me ).
    ro_child_node->set_root( me->root_node ).
    ro_child_node->set_namespace( CONV #( me->namespace ) ).
    ro_child_node->set_prefix( CONV #( me->prefix ) ).
    ro_child_node->set_suffix( CONV #( me->suffix ) ).
    ro_child_node->set_implementation_type( me->get_implementation_type(  ) ).
    ro_child_node->set_data_source_type( me->data_source_type ).
    ro_child_node->set_xco_lib( me->xco_lib ).
    ro_child_node->set_draft_enabled( draft_enabled ).
    ro_child_node->set_is_customizing_table( me->is_customizing_table ).
    ro_child_node->add_transactional_behavior( transactional_behavior ).


    ro_child_node->set_number( lines( me->root_node->all_childnodes ) + 1 ).

    APPEND ro_child_node TO childnodes.

    lt_all_childnodes = me->root_node->all_childnodes.
    me->root_node->add_to_all_childnodes( ro_child_node ).

  ENDMETHOD.


  METHOD add_to_all_childnodes.
    APPEND io_child_node TO all_childnodes.
  ENDMETHOD.


  METHOD add_to_manage_business_config.
    manage_business_configuration = iv_value.
  ENDMETHOD.


  METHOD add_transactional_behavior.
    transactional_behavior = iv_value.
  ENDMETHOD.

  METHOD set_generate_only_node_hierach.
    generate_only_node_hierachy = iv_value.
  ENDMETHOD.

  METHOD add_multi_edit.
    multi_edit = iv_value.
  ENDMETHOD.

  METHOD add_valuehelp.

    DATA lv_target TYPE string.
    DATA ls_valuehelp TYPE ts_valuehelp.
    FIELD-SYMBOLS: <fields> TYPE ts_field.

    lv_target = to_upper( iv_name ).

    ls_valuehelp-alias = iv_alias.
    ls_valuehelp-element = iv_element.
    ls_valuehelp-localelement = iv_localelement.
    ls_valuehelp-name = iv_name.

    IF it_additional_binding IS NOT INITIAL.

      LOOP AT it_additional_binding INTO DATA(ls_additional_binding).

        CASE ls_additional_binding-usage .
          WHEN additionalbinding_usage-filter .
          WHEN additionalbinding_usage-filter_and_result.
          WHEN additionalbinding_usage-result .
          WHEN '' .
          WHEN OTHERS.
            RAISE EXCEPTION TYPE /dmo/cx_rap_generator
              EXPORTING
                textid   = /dmo/cx_rap_generator=>usage_is_not_supported
                mv_value = ls_additional_binding-usage.
        ENDCASE.

      ENDLOOP.

    ENDIF.


    ls_valuehelp-additionalbinding = it_additional_binding.

    APPEND ls_valuehelp TO lt_valuehelp.

    LOOP AT lt_fields  ASSIGNING <fields> WHERE cds_view_field = iv_localelement.
      <fields>-has_valuehelp = abap_true.
    ENDLOOP.


  ENDMETHOD.


  METHOD add_valuehelp_for_curr_quan.
    "add valuehelp for currency fields and quantity fields
    LOOP AT lt_fields INTO DATA(field).
      IF field-currencycode IS NOT INITIAL.

        LOOP AT lt_fields ASSIGNING FIELD-SYMBOL(<field_curr>) WHERE name = field-currencycode.
          <field_curr>-is_currencycode = abap_true.
          <field_curr>-is_hidden = abap_true.
        ENDLOOP.

        "add_valuehelp  will set the flag has_valuehelp to abap_true
        IF lt_fields[ name = field-currencycode ]-has_valuehelp = abap_false.
          add_valuehelp(
            EXPORTING
              iv_alias              = 'Currency'
              iv_name               = 'I_Currency'
              iv_localelement       = lt_fields[ name = field-currencycode ]-cds_view_field
              iv_element            = 'Currency'
          ).
        ENDIF.
      ENDIF.
      IF field-unitofmeasure IS NOT INITIAL.

        LOOP AT lt_fields ASSIGNING FIELD-SYMBOL(<field_quan>) WHERE name = field-unitofmeasure.
          <field_quan>-is_unitofmeasure = abap_true.
          <field_quan>-is_hidden = abap_true.
        ENDLOOP.

        "add_valuehelp  will set the flag has_valuehelp to abap_true
        IF lt_fields[ name = field-unitofmeasure ]-has_valuehelp = abap_false.
          add_valuehelp(
            EXPORTING
              iv_alias              = 'UnitOfMeasure'
              iv_name               = 'I_UnitOfMeasure'
              iv_localelement       = lt_fields[ name = field-unitofmeasure ]-cds_view_field
              iv_element            = 'UnitOfMeasure'
          ).
        ENDIF.
      ENDIF.

      IF field-doma = field_name-language AND field-has_valuehelp = abap_false.
        add_valuehelp(
              EXPORTING
                iv_alias              = 'Language'
                iv_name               = 'I_Language'
                iv_localelement       = field-cds_view_field
                iv_element            = 'Language'
            ).
      ENDIF.

    ENDLOOP.
  ENDMETHOD.


  METHOD check_parameter.

    "IF iv_value IS INITIAL.
    "  RAISE EXCEPTION TYPE /DMO/CX_RAP_GENERATOR
    "    EXPORTING
    "      textid            = /DMO/CX_RAP_GENERATOR=>parameter_is_initial
    "      mv_parameter_name = |Object:{ iv_parameter_name } |.
    "ENDIF.

    "@todo
    "Simply return if iv_value is intial?

    "search for spaces
    IF contains_no_blanks( CONV #( iv_value ) ) = abap_false.
      APPEND |Name of { iv_parameter_name } { iv_value } contains spaces| TO lt_messages.
      bo_node_is_consistent = abap_false.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid   = /dmo/cx_rap_generator=>contains_spaces
          mv_value = |Object:{ iv_parameter_name } Name:{ iv_value }|.
    ENDIF.

    "search for non alpha numeric characters
    IF is_alpha_numeric( CONV #( iv_value ) ) = abap_false.
      APPEND |Name of { iv_parameter_name } { iv_value } contains non alpha numeric characters| TO lt_messages.
      bo_node_is_consistent = abap_false.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid   = /dmo/cx_rap_generator=>non_alpha_numeric_characters
          mv_value = |Object:{ iv_parameter_name } Name:{ iv_value }|.
    ENDIF.

    "check length
    DATA(lv_max_length) = 30.

    IF strlen( iv_value ) > lv_max_length.
      APPEND |Name of { iv_value } is too long ( { lv_max_length } chararcters max)| TO lt_messages.
      bo_node_is_consistent = abap_false.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid        = /dmo/cx_rap_generator=>is_too_long
          mv_value      = |{ iv_value } ({ strlen( iv_value ) })|
          mv_max_length = lv_max_length.
    ENDIF.


  ENDMETHOD.


  METHOD check_repository_object_name.

    "parameters have to be set to upper case
    "this will not be necessary in an upcomming release

    DATA lv_max_length TYPE i.
    DATA(lv_type) = to_upper( iv_type ).
    DATA(lv_name) = to_upper( iv_name ).
    DATA lv_object_already_exists TYPE abap_bool.

    DATA(number_of_characters_namespace) = strlen( namespace ).
    DATA(object_name_without_namespace) = substring( val = lv_name off = number_of_characters_namespace ).

    "check if repository already exists

    lv_object_already_exists = abap_false.

    CASE lv_type.
      WHEN 'BDEF' .
        IF  xco_lib->get_behavior_definition( CONV #( lv_name ) )->exists( ).
          lv_object_already_exists = abap_true.
        ENDIF.
      WHEN 'DDLS' .
        IF  xco_lib->get_data_definition( CONV #( lv_name ) )->exists( ).
          lv_object_already_exists = abap_true.
        ENDIF.
      WHEN 'DDLX' .
        IF  xco_lib->get_metadata_extension( CONV #( lv_name ) )->exists( ).
          lv_object_already_exists = abap_true.
        ENDIF.
      WHEN 'SRVD' .
        IF  xco_lib->get_service_definition( CONV #( lv_name ) )->if_xco_ar_object~exists(  ).
          lv_object_already_exists = abap_true.
        ENDIF.
      WHEN 'SRVB'.
        IF  xco_lib->get_service_binding( CONV #( lv_name ) )->if_xco_ar_object~exists(  ).
          lv_object_already_exists = abap_true.
        ENDIF.
      WHEN 'CLAS'.
        IF  xco_lib->get_class( CONV #( lv_name ) )->exists( ).
          lv_object_already_exists = abap_true.
        ENDIF.
      WHEN 'DEVC'.
        IF  xco_lib->get_package( CONV #( lv_name ) )->exists( ).
          lv_object_already_exists = abap_true.
        ENDIF.
      WHEN 'TABL'.
        IF  xco_lib->get_database_table( CONV #( lv_name ) )->exists( ).
          lv_object_already_exists = abap_true.
        ENDIF.
      WHEN 'STRU'.
        IF  xco_lib->get_structure( CONV #( lv_name ) )->exists( ).
          lv_object_already_exists = abap_true.
        ENDIF.
      WHEN 'SMBC'.
*        IF  xco_lib->get_structure( CONV #( lv_name ) )->exists( ).
*          lv_object_already_exists = abap_true.
*        ENDIF.


        DATA(first_letter_mbc_namespace) = substring( val = me->namespace  len = 1 ).

        "The MBC registration API uses a namespace only if it is a "real" namespace.
        "If a customer namespace 'Y' or 'Z' is used or if
        "SAP objects are created such as I_Test that also do not have a namespace
        "then the MBC namespace must be initial.

        CASE first_letter_mbc_namespace.
          WHEN '/' .
            DATA(abap_object_mbc_name) = namespace && lv_name.
          WHEN 'Y' OR 'Z'.
            abap_object_mbc_name = namespace && lv_name.
          WHEN OTHERS.
            abap_object_mbc_name = lv_name.
        ENDCASE.

        SELECT * FROM I_CustABAPObjDirectoryEntry WHERE
        ABAPObject = @abap_object_mbc_name AND ABAPObjectCategory = 'R3TR' AND ABAPObjectType = 'SMBC' INTO TABLE @DATA(lt_smbc).

        IF lines( lt_smbc ) = 1.
          lv_object_already_exists = abap_true.
        ENDIF.

      WHEN OTHERS.
    ENDCASE.

    IF lv_object_already_exists = abap_true.
      bo_node_is_consistent = abap_false.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid     = /dmo/cx_rap_generator=>repository_already_exists
          mv_value   = lv_name
          mv_value_2 = lv_type.
    ENDIF.




    CASE lv_type.
      WHEN 'BDEF' OR 'DDLS' OR 'DDLX' OR 'SRVD' OR 'STRU'.
        lv_max_length = 30.
      WHEN 'SRVB'.
        lv_max_length = 26.
      WHEN 'CLAS'.
        lv_max_length = 30.
      WHEN 'DEVC'.
        lv_max_length = 20.
      WHEN 'TABL'.
        lv_max_length = 16.
      WHEN 'SMBC'.
        lv_max_length = 20.
      WHEN OTHERS.
    ENDCASE.

    IF lv_type = 'STRU'.
      lv_type = 'TABL(Structure)'.
    ENDIF.

    IF lv_type = 'TABL'.
      lv_type = 'TABL(Database Table)'.
    ENDIF.

    "search for non alpha numeric characters
    IF is_alpha_numeric( CONV #( object_name_without_namespace ) ) = abap_false.
      APPEND |Name of { lv_type } { lv_name } contains non alpha numeric characters| TO lt_messages.
      bo_node_is_consistent = abap_false.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid   = /dmo/cx_rap_generator=>non_alpha_numeric_characters
          mv_value = | { lv_type }:{ lv_name }|.
    ENDIF.

    "search for spaces
    IF contains_no_blanks( CONV #( lv_name ) ) = abap_false.
      APPEND |Name of { lv_type } { lv_name } contains spaces| TO lt_messages.
      bo_node_is_consistent = abap_false.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid   = /dmo/cx_rap_generator=>contains_spaces
          mv_value = |Object Type: { lv_type } Object Name:{ lv_name }|.
    ENDIF.

    "check length
    IF strlen( lv_name ) > lv_max_length.
      APPEND |Name of { lv_type } is too long ( { lv_max_length } chararcters max)| TO lt_messages.
      bo_node_is_consistent = abap_false.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid        = /dmo/cx_rap_generator=>is_too_long
          mv_value      = |{ lv_name } ({ strlen( lv_name ) })|
          mv_max_length = lv_max_length.
    ENDIF.

    "Check table for "Underscore not permitted at 2nd or 3rd position"
    IF lv_type = 'TABL(Database Table)' AND underscore_at_pos_2_3( lv_name ) = abap_true.
      APPEND |Name of { lv_name } - underscore not permitted at 2nd or 3rd position| TO lt_messages.
      bo_node_is_consistent = abap_false.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid   = /dmo/cx_rap_generator=>underscore_not_at_pos_2_3
          mv_value = lv_name.
    ENDIF.

  ENDMETHOD.


  METHOD check_table_package_assignment.

    "check if tables that shall be used
    "and the package that has been provided
    "reside in the same software component

    " Get name of the software component of the package
    "DATA(package_object) = xco_cp_abap_repository=>object->devc->for( package ).
    DATA(package_object) = xco_lib->get_package( package ).

    DATA(swc_name_package) = package_object->read( )-property-software_component->name.

    "Compare with software components of tables
    "check table of root node

    "create object for table
    "DATA(lo_database_table) = xco_cp_abap_dictionary=>database_table( root_node->table_name ).
    DATA(lo_database_table) = xco_lib->get_database_table( root_node->table_name ).
    " Get package.
    DATA(package_of_db_table) = lo_database_table->if_xco_ar_object~get_package( )->read( ).
    " Software component.
    DATA(swc_name_db_table) = package_of_db_table-property-software_component->name.

    IF swc_name_package <> swc_name_db_table.
      IF NOT swc_name_db_table = '/DMO/SAP'  AND  swc_name_db_table = 'ZLOCAL'.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid          = /dmo/cx_rap_generator=>software_comp_do_not_match
            mv_table_name   = CONV #( root_node->table_name )
            mv_package_name = CONV #( package ).
      ENDIF.
    ENDIF.

    "check tables of child nodes

    IF root_node->has_childs(  ).
      LOOP AT root_node->all_childnodes INTO DATA(ls_childnode).

        "lo_database_table = xco_cp_abap_dictionary=>database_table( ls_childnode->table_name ).
        lo_database_table = xco_lib->get_database_table( ls_childnode->table_name ).

        package_of_db_table = lo_database_table->if_xco_ar_object~get_package( )->read( ).
        swc_name_db_table = package_of_db_table-property-software_component->name.
        IF swc_name_package <> swc_name_db_table.
          IF NOT swc_name_db_table = '/DMO/SAP'  AND  swc_name_db_table = 'ZLOCAL'.
            RAISE EXCEPTION TYPE /dmo/cx_rap_generator
              EXPORTING
                textid          = /dmo/cx_rap_generator=>software_comp_do_not_match
                mv_table_name   = CONV #( ls_childnode->table_name )
                mv_package_name = CONV #( package ).
          ENDIF.
        ENDIF.
      ENDLOOP.
    ENDIF.



  ENDMETHOD.


  METHOD constructor.

    IF io_xco_lib IS NOT INITIAL.
      xco_lib = io_xco_lib.
    ELSE.
      xco_lib = NEW /dmo/cl_rap_xco_cloud_lib( ).
    ENDIF.

    bo_node_is_consistent = abap_true.
    is_finalized = abap_false.
    draft_enabled = abap_false.
    useUpperCamelCase = abap_true.
    add_meta_data_extensions = abap_true.
    skip_activation = abap_false.


    field_name-client          = 'CLIENT'.
    field_name-uuid            = 'UUID'.
    field_name-parent_uuid     = 'PARENT_UUID'.
    field_name-root_uuid       = 'ROOT_UUID'.
    field_name-created_by      = 'CREATED_BY'.
    field_name-created_at      = 'CREATED_AT'.
    field_name-last_changed_by = 'LAST_CHANGED_BY'.
    field_name-last_changed_at = 'LAST_CHANGED_AT'.
    field_name-local_instance_last_changed_at = 'LOCAL_LAST_CHANGED_AT'.
    field_name-local_instance_last_changed_by = 'LOCAL_LAST_CHANGED_BY'.
    field_name-language        = 'SPRAS'.
    field_name-etag_master     = 'LOCAL_LAST_CHANGED_AT'.
    field_name-total_etag      = 'LAST_CHANGED_AT'.

    publish_service = abap_true.
    transactional_behavior = abap_true.
    binding_type = binding_type_name-odata_v4_ui.

    "xco_lib = NEW /dmo/cl_rap_xco_cloud_lib( ).
    "xco_lib = NEW /dmo/cl_rap_xco_on_prem_lib(  ).

    TEST-SEAM runs_as_cut.
      is_test_run = abap_false.
    END-TEST-SEAM.

  ENDMETHOD.


  METHOD contains_no_blanks.
    rv_contains_no_blanks = abap_true.
    FIND ALL OCCURRENCES OF REGEX  '[[:space:]]' IN iv_string RESULTS DATA(blanks).
    IF blanks IS NOT INITIAL.
      rv_contains_no_blanks = abap_false.
    ENDIF.
  ENDMETHOD.


  METHOD set_add_meta_data_extensions.
    add_meta_data_extensions = iv_value.
  ENDMETHOD.


  METHOD field_name_exists_in_cds_view.
    rv_field_name_exists = abap_false.
    LOOP AT lt_fields INTO DATA(ls_field).
      IF ls_field-cds_view_field = iv_field_name.
        rv_field_name_exists = abap_true.
      ENDIF.
    ENDLOOP.
  ENDMETHOD.



  METHOD field_name_exists_in_db_table.
    "safety measure if field name in JSON is not upper case
    DATA(lv_field_name_upper) = to_upper( iv_field_name ).
    "Check the field list contains a field with this name
    rv_field_name_exists = boolc( line_exists( lt_fields[ name = lv_field_name_upper ] ) ).

  ENDMETHOD.


  METHOD finalize.
    "namespace must be set for root node
    "namespace for child objects will be set in method add_child( )



    DATA manage_business_cfg_identifier TYPE if_mbc_cp_api_business_config=>ty_identifier.

    IF namespace IS INITIAL.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid = /dmo/cx_rap_generator=>no_namespace_set.
    ENDIF.

    CASE data_source_type.
      WHEN data_source_types-table.
        IF table_name IS INITIAL.
          RAISE EXCEPTION TYPE /dmo/cx_rap_generator
            EXPORTING
              textid    = /dmo/cx_rap_generator=>no_data_source_set
              mv_entity = entityname.
        ENDIF.
      WHEN data_source_types-cds_view.
        IF cds_view_name IS INITIAL.
          RAISE EXCEPTION TYPE /dmo/cx_rap_generator
            EXPORTING
              textid    = /dmo/cx_rap_generator=>no_data_source_set
              mv_entity = entityname.
        ENDIF.
    ENDCASE.
    IF implementationtype = implementation_type-unmanged_semantic OR
         implementationtype = implementation_type-managed_semantic.
      IF semantic_key IS INITIAL .
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid = /dmo/cx_rap_generator=>no_semantic_key_set.
      ENDIF.
    ENDIF.

    IF object_id IS INITIAL.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid    = /dmo/cx_rap_generator=>no_object_id_set
          mv_entity = entityname.
    ENDIF.

    "set root_uuid
*    IF is_grand_child_or_deeper(  ).
*      set_field_name_root_uuid( root_node->field_name-uuid ).
*    ENDIF.

    add_valuehelp_for_curr_quan(  ).
    "add additional checks from methods add_valuehelp( ), set_semantic_key_fields( ) and ADD ASSOCIATION( )

    "hide administrative fields
    "hide guid based fields
    LOOP AT lt_fields ASSIGNING FIELD-SYMBOL(<field_hidden>).
      CASE to_upper( <field_hidden>-name ).
        WHEN field_name-uuid.
          <field_hidden>-is_hidden = abap_true.
        WHEN field_name-last_changed_at.
          <field_hidden>-is_hidden = abap_true.
        WHEN field_name-last_changed_by .
          <field_hidden>-is_hidden = abap_true.
        WHEN field_name-created_at .
          <field_hidden>-is_hidden = abap_true.
        WHEN field_name-created_by .
          <field_hidden>-is_hidden = abap_true.
        WHEN field_name-parent_uuid .
          <field_hidden>-is_hidden = abap_true.
        WHEN field_name-root_uuid .
          <field_hidden>-is_hidden = abap_true.
        WHEN field_name-local_instance_last_changed_at.
          <field_hidden>-is_hidden = abap_true.
        WHEN field_name-local_instance_last_changed_by.
          <field_hidden>-is_hidden = abap_true.
      ENDCASE.
    ENDLOOP.
    "for custom entities the key has to be specified via the json file
    IF data_source_type = data_source_types-structure.
      LOOP AT semantic_key INTO DATA(ls_semantic_key).
        LOOP AT lt_fields ASSIGNING FIELD-SYMBOL(<field_without_key>) WHERE name = ls_semantic_key-name.
          <field_without_key>-key_indicator = abap_true.
        ENDLOOP.
      ENDLOOP.
      "to get key fields on top we have to sort by key_indicator descending
      SORT lt_fields BY key_indicator DESCENDING name ASCENDING.
    ENDIF.

    "fill lt_all_fields only after lt_fields is finalized (e.g. is_hidden is added)
    add_fields_to_all_fields(  ).
    add_additonal_to_all_fields(  ).


    validate_bo( ).

    set_repository_object_names(  ).


    IF lt_messages IS NOT INITIAL AND is_root(  ) = abap_false.
      APPEND | Messages from { entityname } | TO me->root_node->lt_messages.
      APPEND LINES OF lt_messages TO me->root_node->lt_messages.
    ENDIF.

    IF bo_node_is_consistent = abap_true.
      is_finalized = abap_true.
    ENDIF.

  ENDMETHOD.


  METHOD get_fields.



    DATA lo_struct_desc           TYPE REF TO cl_abap_structdescr.
    DATA lo_type_desc             TYPE REF TO cl_abap_typedescr.
    DATA lt_components TYPE cl_abap_structdescr=>component_table .
    DATA ls_components LIKE LINE OF lt_components.
    DATA dref_table TYPE REF TO data.
    DATA ls_fields TYPE ts_field.
    DATA semantic_key_fields  TYPE tt_semantic_key_fields .


    CASE data_source_type.
      WHEN data_source_types-table.


        TEST-SEAM get_mock_data_fields.
          "importing io_read_state  type ref to cl_xco_ad_object_read_state default xco_abap_dictionary=>object_read_state->active_version

          DATA(lo_database_table) = xco_lib->get_database_table( iv_name = table_name  ).

          get_database_table_fields(
               EXPORTING
                 io_database_table = lo_database_table
               IMPORTING
                 et_fields         = lt_Fields
             ).


        END-TEST-SEAM.

        set_mapping(  ).

      WHEN data_source_types-structure.

        DATA(lo_structure) = xco_lib->get_structure( iv_name = structure_name  ).

        lt_fields = get_structure_components( lo_structure ).


        set_mapping(  ).

      WHEN data_source_types-abap_type.

        lt_fields = get_abap_type_components( abap_type_name ).

        set_mapping(  ).

      WHEN data_source_types-cds_view.

        lt_fields = get_fields_cds_view( CONV #( cds_view_name ) ). "  abap_type_components( abap_type_name ).



      WHEN OTHERS.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid   = /dmo/cx_rap_generator=>invalid_data_source_type
            mv_value = data_source_type.


    ENDCASE.

    IF data_source_type <> data_source_types-structure AND
       data_source_type <> data_source_types-abap_type .



      IF implementationtype = implementation_type-managed_semantic OR
         implementationtype = implementation_type-unmanged_semantic.

        CLEAR semantic_key_fields.
        CLEAR semantic_key.

        LOOP AT lt_fields INTO ls_fields WHERE key_indicator = abap_true AND name <> field_name-client.
          APPEND ls_fields-name TO semantic_key_fields.
        ENDLOOP.

        set_semantic_key_fields( semantic_key_fields ).

      ENDIF.
    ENDIF.

    "fill lt_all_fields with the fields read from the data source.
    "add additional fields to lt_all_fields if additional fields are added
    "in add_additional_fields_2
    " lt_all_fields = lt_fields.

  ENDMETHOD.


  METHOD get_fields_persistent_table.

    DATA lt_components TYPE cl_abap_structdescr=>component_table .
    DATA ls_fields TYPE ts_field.
    DATA(lo_database_table) = xco_lib->get_database_table( CONV  sxco_dbt_object_name( persistent_table_name ) ).
    DATA(lt_fields_from_xco) = lo_database_table->fields->all->get( ).
    LOOP AT lt_fields_from_xco INTO DATA(ls_fields_from_xco).
      ls_fields-name = ls_fields_from_xco->name.
      APPEND ls_fields TO lt_fields_persistent_table.
    ENDLOOP.

  ENDMETHOD.


  METHOD get_implementation_type.
    rv_implementation_type = implementationtype.
  ENDMETHOD.


  METHOD get_root_cause_textid.
    "error and success messages
    TYPES: BEGIN OF ty_exception_text,
             msgv1(50),
             msgv2(50),
             msgv3(50),
             msgv4(50),
           END OF ty_exception_text.

    DATA : lx_root_cause     TYPE REF TO cx_root,
           ls_exception_text TYPE ty_exception_text.

    "the caller of this method should retrieve the error message of the root cause
    "that has been originally raised by the config facade

    lx_root_cause = ix_previous.

    WHILE lx_root_cause->previous IS BOUND.
      lx_root_cause = lx_root_cause->previous.    " Get the exception that caused this exception
    ENDWHILE.

    "move the (long) text to a structure with 4 fields of length 50 characters each
    "error messages longer than 200 characters are truncated.
    "no exception is thrown opposed to using substring
    ls_exception_text = lx_root_cause->get_longtext( ).

    IF ls_exception_text IS INITIAL.
      ls_exception_text = lx_root_cause->get_text( ).
    ENDIF.

    rs_root_cause_textid-attr1 = CONV #( ls_exception_text-msgv1 ).
    rs_root_cause_textid-attr2 = CONV #( ls_exception_text-msgv2 ).
    rs_root_cause_textid-attr3 = CONV #( ls_exception_text-msgv3 ).
    rs_root_cause_textid-attr4 = CONV #( ls_exception_text-msgv4 ).
    rs_root_cause_textid-msgid = '/DMO/CM_RAP_GEN_MSG'.
    rs_root_cause_textid-msgno = 016.

  ENDMETHOD.


  METHOD get_root_exception.
    rx_root = ix_exception.
    WHILE rx_root->previous IS BOUND.
      rx_root ?= rx_root->previous.
    ENDWHILE.
  ENDMETHOD.


  METHOD has_childs.
    IF childnodes IS NOT INITIAL.
      rv_has_childs = abap_true.
    ENDIF.
  ENDMETHOD.


  METHOD is_alpha_numeric.
    rv_is_alpha_numeric = abap_true.
    FIND ALL OCCURRENCES OF REGEX '[^[:word:]]' IN iv_string RESULTS DATA(non_alpha_numeric_characters).
    IF non_alpha_numeric_characters IS NOT INITIAL.
      rv_is_alpha_numeric = abap_false.
    ENDIF.
  ENDMETHOD.


  METHOD is_child.
    rv_is_child = abap_false.
    IF me->root_node = me->parent_node AND
    me->is_root(  ) = abap_false.
      rv_is_child = abap_true.
    ENDIF.
  ENDMETHOD.


  METHOD is_consistent.
    rv_is_consistent = bo_node_is_consistent.
  ENDMETHOD.


  METHOD is_grand_child_or_deeper.
    rv_is_grand_child = abap_false.
    IF me->root_node <> me->parent_node.
      rv_is_grand_child = abap_true.
    ENDIF.
  ENDMETHOD.


  METHOD is_root.
    rv_is_root = is_root_node.
  ENDMETHOD.


  METHOD is_virtual_root.
    rv_is_virtual_root = is_virtual_root_node.
  ENDMETHOD.

  METHOD get_structure_components.

    DATA table_fields  TYPE ts_field  .

    LOOP AT io_components->components->all->get( ) INTO DATA(lo_field).
      CLEAR table_fields.
      DATA(lo_field_content) =  lo_field->content( ).
      DATA(lo_field_content_type) = lo_field_content->get_type(  ).
      DATA(ls_field) = lo_field_content->get( ).

      table_fields-name = lo_field->name.
      IF useUpperCamelCase = abap_true.
        "table_fields-cds_view_field = to_mixed( table_fields-name ).
        table_fields-cds_view_field = xco_cp=>string( table_fields-name )->split( '_' )->compose( xco_cp_string=>composition->pascal_case )->value.
      ELSE.
        table_fields-cds_view_field = table_fields-name.
      ENDIF.

      "add hardcoded mappings
      CASE table_fields-name.
        WHEN 'SPRAS'.
          IF useUpperCamelCase = abap_true.
            table_fields-cds_view_field = 'Language'.
          ENDIF.
      ENDCASE.

      table_fields-is_data_element = lo_field_content_type->is_data_element( ).
      table_fields-is_built_in_type = lo_field_content_type->is_built_in_type(  ).
      IF table_fields-is_built_in_type = abap_true.
        table_fields-built_in_type  = lo_field_content_type->get_built_in_type(  )->type.
        table_fields-built_in_type_length = lo_field_content_type->get_built_in_type(  )->length.
        table_fields-built_in_type_decimals = lo_field_content_type->get_built_in_type(  )->decimals.
      ENDIF.
      IF table_fields-name = 'QUANTITY'.
        DATA(a) = 1.
      ENDIF.
      IF ls_field-type->is_data_element( ) EQ abap_true.
        DATA(lo_data_element) = ls_field-type->get_data_element( ).

        read_data_element(
          EXPORTING
            io_data_element = lo_data_element
            is_fields       = table_fields
          IMPORTING
            es_fields       = table_fields
        ).

      ELSE.
        IF ls_field-type->is_built_in_type(  ) = abap_true.
          table_fields-built_in_type  = ls_field-type->get_built_in_type(  )->type.
          table_fields-built_in_type_length = ls_field-type->get_built_in_type(  )->length.
          table_fields-built_in_type_decimals = ls_field-type->get_built_in_type(  )->decimals.
        ENDIF.
      ENDIF.

      DATA(currency_quantity) = ls_field-currency_quantity.

      IF currency_quantity IS NOT INITIAL.
        CASE table_fields-built_in_type.
          WHEN 'CURR'.
            table_fields-currencycode = ls_field-currency_quantity-reference_field.
          WHEN 'QUAN'.
            table_fields-unitofmeasure = ls_field-currency_quantity-reference_field.
        ENDCASE.
      ENDIF.

      IF to_upper( right_string( iv_length = 2 iv_string = CONV #( table_fields-cds_view_field ) ) ) = 'ID'.
        table_fields-cds_view_field = substring( val = table_fields-cds_view_field len = strlen( table_fields-cds_view_field ) - 2 ) && 'ID' .
      ENDIF.

      IF to_upper( right_string( iv_length = 4 iv_string = CONV #( table_fields-cds_view_field ) ) ) = 'UUID'.
        table_fields-cds_view_field = substring( val = table_fields-cds_view_field len = strlen( table_fields-cds_view_field ) - 4 ) && 'UUID' .
      ENDIF.

      APPEND table_fields TO et_fields.

    ENDLOOP.


  ENDMETHOD.

  METHOD get_database_table_fields.

    DATA table_fields  TYPE ts_field  .

    DATA(ls_database_table) = io_database_table->content( )->get( ).

    LOOP AT io_database_table->fields->all->get( ) INTO DATA(lo_field).
      CLEAR table_fields.
      DATA(lo_field_content) =  lo_field->content( ).
      DATA(lo_field_content_type) = lo_field_content->get_type(  ).
      DATA(ls_field) = lo_field_content->get( ).

      table_fields-name = lo_field->name.
      IF useUpperCamelCase = abap_true.
        "table_fields-cds_view_field = to_mixed( table_fields-name ).
        table_fields-cds_view_field = xco_cp=>string( table_fields-name )->split( '_' )->compose( xco_cp_string=>composition->pascal_case )->value.
      ELSE.
        table_fields-cds_view_field = table_fields-name.
      ENDIF.

      "add hardcoded mappings
      CASE table_fields-name.
        WHEN 'SPRAS'.
          IF useUpperCamelCase = abap_true.
            table_fields-cds_view_field = 'Language'.
          ENDIF.
      ENDCASE.

      table_fields-key_indicator = ls_field-key_indicator.
      table_fields-not_null =  ls_field-not_null.
      table_fields-is_data_element = lo_field_content_type->is_data_element( ).
      table_fields-is_built_in_type = lo_field_content_type->is_built_in_type(  ).
      IF table_fields-is_built_in_type = abap_true.
        table_fields-built_in_type  = lo_field_content_type->get_built_in_type(  )->type.
        table_fields-built_in_type_length = lo_field_content_type->get_built_in_type(  )->length.
        table_fields-built_in_type_decimals = lo_field_content_type->get_built_in_type(  )->decimals.
      ENDIF.
      IF table_fields-name = 'QUANTITY'.
        DATA(a) = 1.
      ENDIF.
      IF ls_field-type->is_data_element( ) EQ abap_true.
        DATA(lo_data_element) = ls_field-type->get_data_element( ).

        read_data_element(
          EXPORTING
            io_data_element = lo_data_element
            is_fields       = table_fields
          IMPORTING
            es_fields       = table_fields
        ).

      ELSE.
        IF ls_field-type->is_built_in_type(  ) = abap_true.
          table_fields-built_in_type  = ls_field-type->get_built_in_type(  )->type.
          table_fields-built_in_type_length = ls_field-type->get_built_in_type(  )->length.
          table_fields-built_in_type_decimals = ls_field-type->get_built_in_type(  )->decimals.
        ENDIF.
      ENDIF.

      DATA(currency_quantity) = ls_field-currency_quantity.

      IF currency_quantity IS NOT INITIAL.
        CASE table_fields-built_in_type.
          WHEN 'CURR'.
            table_fields-currencycode = ls_field-currency_quantity-reference_field.
          WHEN 'QUAN'.
            table_fields-unitofmeasure = ls_field-currency_quantity-reference_field.
        ENDCASE.
      ENDIF.

      IF to_upper( right_string( iv_length = 2 iv_string = CONV #( table_fields-cds_view_field ) ) ) = 'ID'.
        table_fields-cds_view_field = substring( val = table_fields-cds_view_field len = strlen( table_fields-cds_view_field ) - 2 ) && 'ID' .
      ENDIF.

      IF to_upper( right_string( iv_length = 4 iv_string = CONV #( table_fields-cds_view_field ) ) ) = 'UUID'.
        table_fields-cds_view_field = substring( val = table_fields-cds_view_field len = strlen( table_fields-cds_view_field ) - 4 ) && 'UUID' .
      ENDIF.

      APPEND table_fields TO et_fields.

    ENDLOOP.
  ENDMETHOD.


  METHOD read_data_element.

    es_fields   = is_fields.
    es_fields-data_element = io_data_element->name.

    DATA(ls_data_element) = io_data_element->content( )->get( ).

    "domain does not exist if
    "a) a built in type such as CUKY is used
    "b) if language version 5 is used and if the underlying domain is not c1-released.
    "   In this case the check for existence will fail since the domain is not visible for the XCO_CP libraries

    IF ls_data_element-data_type->is_domain( ) EQ abap_true.
      DATA(lo_domain) = ls_data_element-data_type->get_domain( ).

      IF lo_domain->exists(  ) = abap_true.

        read_domain(
          EXPORTING
            io_domain = lo_domain
            is_fields = es_fields
          IMPORTING
            es_fields =  es_fields
        ).

      ELSE.
        "@todo:
        "add code to call the methods
        "if_xco_dtel_data_type~GET_UNDERLYING_BUILT_IN_TYPE
        "if_xco_dtel_data_type~HAS_UNDERLYING_BUILT_IN_TYPE
      ENDIF.
    ELSE.
      IF ls_data_element-data_type->is_built_in_type(  ) = abap_true.
        es_fields-built_in_type  = ls_data_element-data_type->get_built_in_type(  )->type.
        es_fields-built_in_type_length = ls_data_element-data_type->get_built_in_type(  )->length.
        es_fields-built_in_type_decimals = ls_data_element-data_type->get_built_in_type(  )->decimals.
      ENDIF.
    ENDIF.
  ENDMETHOD.


  METHOD read_domain.

    es_fields   = is_fields.
    es_fields-doma = io_domain->name.

    DATA(lo_read_state) = xco_cp_abap_dictionary=>object_read_state->active_version.

    DATA(ls_domain) = io_domain->content( lo_read_state )->get( ).

    DATA(domain_built_in_type) = ls_domain-format->get_built_in_type(  ).
    IF domain_built_in_type IS NOT INITIAL.
      es_fields-built_in_type = domain_built_in_type->type.
      es_fields-built_in_type_length = domain_built_in_type->length.
      es_fields-built_in_type_decimals = domain_built_in_type->decimals.
    ENDIF.

    DATA(domain_fixed_values) = io_domain->fixed_values->all->get( lo_read_state ).

    IF domain_fixed_values IS NOT INITIAL.
      es_fields-domain_fixed_value = abap_true.
    ENDIF.

  ENDMETHOD.


  METHOD right_string.
    DATA(length_of_string) = strlen( iv_string ).
    IF length_of_string >= iv_length.
      rv_string = substring( val = iv_string off = length_of_string - iv_length len = iv_length ).
    ENDIF.
  ENDMETHOD.


  METHOD set_behavior_def_i_name.

    IF iv_name IS INITIAL.
      DATA(lv_name) = |{ namespace }I_{ prefix }{ entityname }{ suffix }|.
    ELSE.
      lv_name = iv_name.
    ENDIF.

    check_repository_object_name(
          EXPORTING
            iv_type = 'BDEF'
            iv_name = lv_name
        ).


    IF is_root( ).
      rap_root_node_objects-behavior_definition_i = lv_name.
      rv_behavior_dev_i_name = lv_name.
    ELSEIF is_test_run = abap_true.
      rap_root_node_objects-behavior_definition_i = lv_name.
      rv_behavior_dev_i_name = lv_name.
    ELSE.
      APPEND | { me->entityname } is not a root node. BDEF for an interface view is only generated for the root node| TO lt_messages.
      bo_node_is_consistent = abap_false.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid    = /dmo/cx_rap_generator=>is_not_a_root_node
          mv_entity = me->entityname.
    ENDIF.



  ENDMETHOD.


  METHOD set_behavior_def_p_name.

    IF iv_name IS INITIAL.
      DATA(lv_name) = |{ namespace }C_{ prefix }{ entityname }{ suffix }|.
    ELSE.
      lv_name = iv_name.
    ENDIF.


    check_repository_object_name(
          EXPORTING
            iv_type = 'BDEF'
            iv_name = lv_name
        ).

    IF is_root( ).
      rap_root_node_objects-behavior_definition_p = lv_name.
      rv_behavior_dev_p_name = lv_name.
    ELSEIF is_test_run = abap_true.
      rap_root_node_objects-behavior_definition_p = lv_name.
      rv_behavior_dev_p_name = lv_name.
    ELSE.
      APPEND | { me->entityname } is not a root node. BDEF for a projection view is only generated for the root node| TO lt_messages.
      bo_node_is_consistent = abap_false.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid    = /dmo/cx_rap_generator=>is_not_a_root_node
          mv_entity = me->entityname.
    ENDIF.

  ENDMETHOD.

  METHOD set_custom_query_impl_name.
    IF iv_name IS INITIAL.
      DATA(lv_name) = |{ namespace }CL_CE_{ prefix }{ entityname }{ suffix }|.
    ELSE.
      lv_name = iv_name.
    ENDIF.

    check_repository_object_name(
       EXPORTING
          iv_type = 'CLAS'
          iv_name = lv_name
         ).

    rap_node_objects-custom_query_impl_class = lv_name.
    rv_custom_query_impl_class = lv_name.
  ENDMETHOD.

  METHOD set_behavior_impl_name.

    IF iv_name IS INITIAL.
      DATA(lv_name) = |{ namespace }BP_I_{ prefix }{ entityname }{ suffix }|.
    ELSE.
      lv_name = iv_name.
    ENDIF.

    check_repository_object_name(
       EXPORTING
          iv_type = 'CLAS'
          iv_name = lv_name
         ).

    rap_node_objects-behavior_implementation = lv_name.
    rv_behavior_imp_name = lv_name.


  ENDMETHOD.


  METHOD set_binding_type.
    IF iv_binding_type = binding_type_name-odata_v2_ui OR iv_binding_type = binding_type_name-odata_v4_ui
    OR iv_binding_type = binding_type_name-odata_v2_web_api OR iv_binding_type = binding_type_name-odata_v4_web_api.
      binding_type = iv_binding_type.
    ELSE.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid     = /dmo/cx_rap_generator=>invalid_binding_type
          mv_value   = data_source_type
          mv_value_2 = supported_binding_types.
    ENDIF.
  ENDMETHOD.

  METHOD set_abap_type.

    abap_type_name = to_upper( iv_abap_type ) .

    split_and_check_abap_type_name( abap_type_name ).

*    DATA(typing_method) = abap_type->content( )->get_typing_method( ).
*    DATA(typing_definition) = abap_type->content( )->get_typing_definition( ).
*
*    IF typing_method->value = 1 AND typing_definition->has_value( ) = abap_true.
*      DATA(structure) = xco_lib->get_structure( CONV #( typing_definition->get_value( ) ) ).
*    ENDIF.



    get_fields(  ).

  ENDMETHOD.

  METHOD set_structure.

    DATA(lv_structure) = to_upper( iv_structure ) .




    "check if structure exists and structure has an active version
    IF xco_lib->get_structure( CONV #( lv_structure ) )->exists( ) = abap_false .
      APPEND | Structure { lv_structure } does not exist| TO lt_messages.
      bo_node_is_consistent = abap_false.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid   = /dmo/cx_rap_generator=>table_does_not_exist
          mv_value = CONV #( lv_structure ).
    ENDIF.

    DATA(structure_state) = xco_lib->get_structure( CONV #( lv_structure ) )->get_state( xco_cp_abap_dictionary=>object_read_state->active_version ).

    DATA(check_state_active) =  xco_cp_abap_dictionary=>object_state->active.

    IF  structure_state <> xco_cp_abap_dictionary=>object_state->active.
      APPEND | Structure { lv_structure } is not active | TO lt_messages.
      bo_node_is_consistent = abap_false.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid   = /dmo/cx_rap_generator=>table_is_inactive
          mv_value = CONV #( lv_structure ).
    ENDIF.

    structure_name = lv_structure.

    set_persistent_table( CONV #( lv_structure ) ).

    get_fields(  ).






  ENDMETHOD.

  METHOD set_cds_view.

    DATA(lv_cds_view) = to_upper( iv_cds_view ) .


    SELECT * FROM I_APIsForSAPCloudPlatform WHERE ReleasedObjectType = 'CDS_STOB' AND ReleasedObjectName = @lv_cds_view INTO TABLE @DATA(lt_result)..

    "check if CDS view used as target exists
    IF  lt_result IS INITIAL .
      IF xco_lib->get_data_definition( CONV #(  lv_cds_view )  )->exists( ) = abap_false .
        APPEND | CDS View {  lv_cds_view  } does not exist | TO lt_messages.
        bo_node_is_consistent = abap_false.
        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid   = /dmo/cx_rap_generator=>cds_view_does_not_exist
            mv_value = CONV #( lv_cds_view ).
      ENDIF.
    ENDIF.

*      DATA(cds_view_state) = xco_lib->get_data_definition( CONV #( lv_cds_view ) )->get_state( xco_cp_abap_dictionary=>object_read_state->active_version ).
*
*      "DATA(check_state_active) =  xco_cp_abap_dictionary=>object_state->active.
*
*      IF  cds_view_state <> xco_cp_abap_dictionary=>object_state->active.
*        APPEND | Table { lv_table } is not active | TO lt_messages.
*        bo_node_is_consistent = abap_false.
*        RAISE EXCEPTION TYPE /DMO/CX_RAP_GENERATOR
*          EXPORTING
*            textid   = /DMO/CX_RAP_GENERATOR=>table_is_inactive
*            mv_value = CONV #( lv_table ).
*      ENDIF.


    cds_view_name = lv_cds_view.



    get_fields(  ).





  ENDMETHOD.


  METHOD set_repository_object_names.

    set_cds_view_i_name( rap_node_objects-cds_view_i ).
    "we are using view entities as of 2008 and don't need to generate DDIC views anymore
    "set_ddic_view_i_name(  ).
    set_custom_entity_name( rap_node_objects-cds_view_i ).
    set_custom_query_impl_name( rap_node_objects-custom_query_impl_class ).
    set_cds_view_p_name( rap_node_objects-cds_view_p ).
    set_mde_name( rap_node_objects-cds_view_p  ).
    set_behavior_impl_name( rap_node_objects-behavior_implementation  ).

    set_control_structure_name( rap_node_objects-control_structure ).


    IF is_root(  ).
      set_behavior_def_i_name( rap_node_objects-cds_view_i ).
      set_behavior_def_p_name( rap_node_objects-cds_view_p ).
      set_service_definition_name( rap_root_node_objects-service_definition ).
      set_service_binding_name( rap_root_node_objects-service_binding ).
    ENDIF.

    IF manage_business_configuration = abap_true.

      IF manage_business_config_names-identifier IS INITIAL.


        DATA(valid_mbc_identifier) = get_valid_mbc_identifier(  ).
        set_mbc_identifier( CONV #(  valid_mbc_identifier )  ).

      ENDIF.

      IF   manage_business_config_names-name IS INITIAL.
        set_mbc_name( CONV #(  |{ root_node->rap_node_objects-alias }{ root_node->suffix } maintenance| )  ).
      ENDIF.

      IF   manage_business_config_names-description IS INITIAL.
        set_mbc_description( CONV #(  |identifier { manage_business_config_names-identifier }| )  ).
      ENDIF.

      set_mbc_namespace(  ).

    ENDIF.


  ENDMETHOD.

  METHOD set_cds_view_i_name.

    IF iv_name IS INITIAL.
      DATA(lv_name) = |{ namespace }I_{ prefix }{ entityname }{ suffix }|.
    ELSE.
      lv_name = iv_name.
    ENDIF.

    check_repository_object_name(
      EXPORTING
        iv_type = 'DDLS'
        iv_name = lv_name
    ).

    rap_node_objects-cds_view_i = lv_name.

    rv_cds_i_view_name = lv_name.

  ENDMETHOD.

  METHOD set_custom_entity_name.

    IF iv_name IS INITIAL.
      DATA(lv_name) = |{ namespace }I_{ prefix }{ entityname }{ suffix }|.
    ELSE.
      lv_name = iv_name.
    ENDIF.

    check_repository_object_name(
      EXPORTING
        iv_type = 'DDLS'
        iv_name = lv_name
    ).

    rap_node_objects-custom_entity = lv_name.

    rv_custom_entity_name = lv_name.

  ENDMETHOD.


  METHOD set_cds_view_p_name.

    IF iv_name IS INITIAL.
      DATA(lv_name) = |{ namespace }C_{ prefix }{ entityname }{ suffix }|.
    ELSE.
      lv_name = iv_name.
    ENDIF.

    check_repository_object_name(
         EXPORTING
           iv_type = 'DDLS'
           iv_name = lv_name
       ).

    rap_node_objects-cds_view_p = lv_name.

    rv_cds_p_view_name = lv_name.

  ENDMETHOD.


  METHOD set_control_structure_name.

    IF iv_name IS INITIAL.
      DATA(lv_name) = |{ namespace }S{ prefix }{ entityname }_X{ suffix }|.
    ELSE.
      lv_name = iv_name.
    ENDIF.

    "four letter acronym for structures is normally 'TABL' but this is also used for tables.
    "unfortunately tables in DDIC only allow names of length 16
    "so using another abbreviation

    check_repository_object_name(
      EXPORTING
        iv_type = 'STRU'
        iv_name = lv_name
    ).

    rap_node_objects-control_structure = lv_name.

    rv_controle_structure_name = lv_name.

  ENDMETHOD.


  METHOD set_is_customizing_table.
    is_customizing_table = iv_value.
  ENDMETHOD.


  METHOD set_skip_activation.
    skip_activation = iv_value.
  ENDMETHOD.


  METHOD underscore_at_pos_2_3.
    DATA underscore TYPE string VALUE '_'.
    rv_no_underscore_at_pos_2_3 = abap_true.
    DATA(string_pos_2_and_3) = substring( val = iv_string  len = 2 off = 1 ).
    FIND ALL OCCURRENCES OF underscore IN
         string_pos_2_and_3
         RESULTS DATA(underscores_at_2_3).
    IF underscores_at_2_3 IS INITIAL.
      rv_no_underscore_at_pos_2_3 = abap_false.
    ENDIF.
  ENDMETHOD.

  METHOD add_virtual_root_node.

    ro_virtual_root_node = NEW /dmo/cl_rap_node( ).

    ro_virtual_root_node->set_namespace( CONV #( me->namespace ) ).
    ro_virtual_root_node->set_prefix( CONV #( me->prefix ) ).
    ro_virtual_root_node->set_suffix( CONV #( me->suffix ) ).
    ro_virtual_root_node->set_implementation_type( me->get_implementation_type(  ) ).
    ro_virtual_root_node->set_data_source_type( data_source_types-cds_view ).
    ro_virtual_root_node->set_xco_lib( me->xco_lib ).
    ro_virtual_root_node->set_binding_type( me->binding_type ).

    ro_virtual_root_node->set_draft_enabled( me->draft_enabled ).
    ro_virtual_root_node->set_entity_name( |{ me->entityname }{ singleton_suffix }| ).

    ro_virtual_root_node->set_transport_request( CONV #( me->transport_request ) ).
    ro_virtual_root_node->set_package( me->package ).
    ro_virtual_root_node->set_is_customizing_table( me->is_customizing_table ).
    ro_virtual_root_node->add_to_manage_business_config( me->manage_business_configuration ).

    "ro_virtual_root_node->set_is_virtual_root_node( ).

    ro_virtual_root_node->add_child_node_hierarchy( me ).
    ro_virtual_root_node->set_is_virtual_root_node( ).
    me->set_is_root_node( abap_false ).
    me->set_parent( ro_virtual_root_node ).
    me->set_root( ro_virtual_root_node ).

    me->add_additional_fields_2(
                                 VALUE #(
                                       (
                                         name = '1'
                                         cds_view_field = 'SingletonID'
                                         built_in_type = 'INT1'
                                         cds_interface_view = abap_true
                                         cds_projection_view = abap_true
                                         draft_table = abap_true
                                         )
                                       )
                                      ).

    LOOP AT me->all_childnodes INTO DATA(childnode).
      childnode->set_root( ro_virtual_root_node ).
      childnode->add_additional_fields_2(
                            VALUE #(
                                  (
                                    name = '1'
                                    cds_view_field = 'SingletonID'
                                    built_in_type = 'INT1'
                                    cds_interface_view = abap_true
                                    cds_projection_view = abap_true
                                    draft_table = abap_true
                                    )
                                  )
                                 ).
    ENDLOOP.

  ENDMETHOD.

  METHOD add_child_node_hierarchy.
    "todo
    "delete root node flag from child_node
    "set parent_node to me
    "set root_node to me
    "loop at all childnodes and set root node to me

* loop at child_node->all_childnodes into data(all_childnode).
*
* ENDLOOP.

    IF all_childnodes IS INITIAL.
      "add the node itself and all of its child nodes to all_childnodes
      APPEND child_node TO all_childnodes.
      LOOP AT child_node->all_childnodes INTO DATA(grand_child).
        APPEND grand_child TO all_childnodes.
      ENDLOOP.

    ENDIF.

    IF childnodes IS INITIAL.
      APPEND child_node TO childnodes.
    ENDIF.

  ENDMETHOD.

  METHOD set_is_virtual_root_node.


    is_virtual_root_node = abap_true.
    set_is_root_node(  ).
    "CLEAR childnodes.
    "CLEAR all_childnodes.

    "field_name-last_changed_at =  |max ({ singleton_child_tab_name }.last_changed_at)|  .
    field_name-total_etag =  |max ({ singleton_child_tab_name }.{ childnodes[ 1 ]->field_name-total_etag } )|  .
    lt_fields = VALUE #(
      (
       name = 'CLIENT'
       cds_view_field = 'Client'
       key_indicator = 'X'
       is_data_element = 'X'
       data_element = 'MANDT'
       )
      (
       name = '1'
       cds_view_field = singleton_field_name
       key_indicator = 'X'
       is_built_in_type = 'X'
       built_in_type = 'INT1'
       built_in_type_length = 3
       )


     ).



    "DATA semantic_key_fields  TYPE tt_semantic_key  .
    semantic_key = VALUE #( ( name = '1' cds_view_field = singleton_field_name ) ).
    object_id = '1'.
    object_id_cds_field_name = singleton_field_name .
    is_finalized = abap_true.
    cds_view_name = 'I_Language'.


    me->add_additional_fields_2(
                                 VALUE #(
                                 "localInstanceLastChangedAt is used the customizing table becomes a child entity
                                 "of the virtual root node
                                       (
                                         "name = field_name-last_changed_at
                                         name = field_name-total_etag
                                         cds_view_field = 'LastChangedAtMax'
                                         data_element = 'TIMESTAMPL'
                                         cds_interface_view = abap_true
                                         cds_projection_view = abap_true
                                         draft_table = abap_true
                                         )
                                          "cast( '' as sxco_transport) as Request,
                                        (
                                         name = |cast( '' as sxco_transport)|
                                         cds_view_field = 'Request'
                                         data_element = 'sxco_transport'
                                         cds_interface_view = abap_true
                                         cds_projection_view = abap_true
                                         draft_table = abap_true
                                         )
                                         "cast( 'X' as abap_boolean) as HideTransport,
                                         (
                                         name = |cast( 'X' as abap_boolean)|
                                         cds_view_field = 'HideTransport'
                                         data_element = 'abap_boolean'
                                         cds_interface_view = abap_true
                                         cds_projection_view = abap_true
                                         draft_table = abap_true
                                         is_hidden = abap_true
                                         )
                                       )
                                      ).

    "fill lt_all_fields only after lt_fields is finalized (e.g. is_hidden is added)
    add_fields_to_all_fields(  ).
    add_additonal_to_all_fields(  ).

    data_source_name = 'I_Language'.
    " data_source_type = ''
    "set_ddic_view_i_name(  ).
    "misuse the logic to create unique name for sql view for i view
    DATA(draft_tab_name) = get_valid_draft_table_name(  ).
    set_draft_table( CONV #( draft_tab_name ) ). "ddic_view_i
    set_cds_view_i_name(  ).
    set_cds_view_p_name(  ).
    set_mde_name(  ).
    set_behavior_impl_name(  ).
    set_behavior_def_i_name(  ).
    set_behavior_def_p_name(  ).
    set_service_definition_name(  ).
    set_service_binding_name(  ).
    IF manage_business_configuration = abap_true.

      IF manage_business_config_names-identifier IS INITIAL.

        DATA(valid_mbc_identifier) = get_valid_mbc_identifier(  ).

        set_mbc_identifier( CONV #( valid_mbc_identifier ) ).
      ENDIF.

      IF   manage_business_config_names-name IS INITIAL.
        set_mbc_name( CONV #(  |{ root_node->rap_node_objects-alias }{ root_node->suffix } maintenance| )  ).
      ENDIF.

      IF   manage_business_config_names-description IS INITIAL.
        set_mbc_description( CONV #(  |identifier { manage_business_config_names-identifier }| )  ).
      ENDIF.

      set_mbc_namespace(  ).

    ENDIF.

  ENDMETHOD.

  METHOD get_field.
    "search fields from data source
    READ TABLE lt_fields INTO rs_field WITH KEY name = to_upper( name ).
    IF sy-subrc = 0.
      RETURN.
    ENDIF.


  ENDMETHOD.

  METHOD admin_fields_exist.

    rv_admin_fields_exists = abap_true.

    IF draft_enabled = abap_true.
      "local_instance_last_changed_at
      "last_changed_at
    ELSE.
      "last_changed_at
    ENDIF.



  ENDMETHOD.

  METHOD add_additional_fields_2.
    LOOP AT it_additional_fields INTO DATA(additonal_field).
      APPEND  additonal_field  TO lt_additional_fields.
    ENDLOOP.
*    "lt_all_fields = lt_fields.
*    DATA all_fields_line LIKE LINE OF lt_all_fields.
*    LOOP AT lt_additional_fields INTO DATA(additional_field).
*      MOVE-CORRESPONDING additional_field TO all_fields_line.
*      APPEND all_fields_line TO lt_all_fields.
*    ENDLOOP.
  ENDMETHOD.

  METHOD get_abap_type_components.

    DATA abap_class TYPE REF TO if_xco_ao_class  .
    DATA abap_type TYPE REF TO if_xco_ao_c_type .
    DATA abap_class_name TYPE sxco_ao_object_name .
    DATA abap_type_name TYPE sxco_ao_component_name.

    split_and_check_abap_type_name(
      EXPORTING
        iv_abap_type_name = name
      IMPORTING
        ev_class_name     = abap_class_name
        ev_type_name      = abap_type_name
    ).  "( abap_type_name ).

    "abap class and type have been checked in split_and_check_abap_type_name( )
    abap_class = xco_cp_abap=>class( abap_class_name ).
    abap_type = abap_class->definition->section-public->component->type( abap_type_name ).

    DATA(typing_method) = abap_type->content( )->get_typing_method( ).
    DATA(typing_definition) = abap_type->content( )->get_typing_definition( ).

    IF typing_method->value = 1 AND typing_definition->has_value( ) = abap_true.
      DATA(structure) = xco_lib->get_structure( CONV #( typing_definition->get_value( ) ) ).
    ENDIF.
    "io_components  type ref to if_xco_ad_structure
    IF structure IS NOT INITIAL.
      et_fields = get_structure_components( structure ).
      "the name of the structure is needed for the statement
      "mapping for <structure name> control <control structure> in BDEF
      structure_name = structure->name.
    ELSE.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid     = /dmo/cx_rap_generator=>invalid_abap_type_name
          mv_value   = | { abap_type_name } |
          mv_entity  = entityname
          mv_value_2 = | ABAP type not supported. |.
    ENDIF.

  ENDMETHOD.

  METHOD split_and_check_abap_type_name.

    DATA abap_class_name TYPE sxco_ao_object_name .
    DATA abap_type_name TYPE sxco_ao_component_name.

    DATA abap_class  TYPE REF TO if_xco_ao_class.
    DATA abap_type  TYPE REF TO if_xco_ao_c_type.


    SPLIT iv_abap_type_name AT '=>' INTO abap_class_name abap_type_name.

    abap_class = xco_cp_abap=>class( abap_class_name ).

    IF abap_class IS INITIAL.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid     = /dmo/cx_rap_generator=>invalid_abap_type_name
          mv_value   = | { iv_abap_type_name } |
          mv_entity  = entityname
          mv_value_2 = | { abap_class_name } not found |.
    ENDIF.

    abap_type = abap_class->definition->section-public->component->type( abap_type_name ).

    IF abap_type IS INITIAL.
      RAISE EXCEPTION TYPE /dmo/cx_rap_generator
        EXPORTING
          textid     = /dmo/cx_rap_generator=>invalid_abap_type_name
          mv_value   = | { iv_abap_type_name } |
          mv_entity  = entityname
          mv_value_2 = | { abap_type_name } not found in class { abap_class_name } |.
    ENDIF.

  ENDMETHOD.

  METHOD set_field_name_client.
    check_parameter(
          EXPORTING
            iv_parameter_name = 'field_name-client'
            iv_value          = iv_string
        ).
    field_name-client = to_upper( iv_string ).
  ENDMETHOD.

  METHOD set_field_name_language.
    check_parameter(
              EXPORTING
                iv_parameter_name = 'field_name-language'
                iv_value          = iv_string
            ).
    field_name-language = to_upper( iv_string ).
  ENDMETHOD.

  METHOD generate_bil.

    "for the root node we need the method get_global_authorization
    "since authorization master( global ) is set in BDEF
    DATA(is_root) = is_root(  ).

    "virtual root node needs several methods in BIL
    DATA(is_virtual_root_node) = is_virtual_root(  ).

    "all nodes that use managed_uuid need a determination for the field object_id
    IF get_implementation_type(  )  = /dmo/cl_rap_node=>implementation_type-managed_uuid.
      DATA(is_managed_uuid) = abap_true.
    ENDIF.

    "all nodes of an unmanged BO need methods such as create, read, read by association being implemented
    IF get_implementation_type(  )  = /dmo/cl_rap_node=>implementation_type-unmanged_semantic .
      DATA(is_unmanaged_semantic) = abap_true.
    ENDIF.

    result = xsdbool(
    (
**********************************************************************
** Begin of deletion 2108
**********************************************************************
*                      is_root = abap_true OR
**********************************************************************
** End of deletion 2108
**********************************************************************
                      is_virtual_root_node = abap_true OR
                      is_managed_uuid = abap_true OR
                      is_customizing_table = abap_true OR
                      is_unmanaged_semantic = abap_true )
                      "if transactional_behavior is ABAP_FALSE no
                      "BIL must be created
                      AND
                      transactional_behavior = abap_true
                      ).



  ENDMETHOD.

  METHOD add_additonal_to_all_fields.
    DATA all_fields_line LIKE LINE OF lt_all_fields.
    LOOP AT lt_additional_fields INTO DATA(additional_field).
      MOVE-CORRESPONDING additional_field TO all_fields_line.
      APPEND all_fields_line TO lt_all_fields.
    ENDLOOP.
  ENDMETHOD.

  METHOD add_fields_to_all_fields.
    CLEAR lt_all_fields.
    INSERT LINES OF lt_fields INTO TABLE lt_all_fields.
  ENDMETHOD.

  METHOD get_fields_cds_view.
    TYPES:
      BEGIN OF ts_semantics_amount,
        currencyCode TYPE string,
      END OF ts_semantics_amount.
    DATA semantic_amount TYPE ts_semantics_amount.

    TYPES:
      BEGIN OF ts_semantics_quantity,
        unitOfMeasure TYPE string,
      END OF ts_semantics_quantity.
    DATA semantic_quantity TYPE ts_semantics_quantity.

    TYPES :
      BEGIN OF ts_field_name,
        field_name TYPE sxco_cds_field_name,
      END OF ts_field_name.

    DATA association_field_names TYPE STANDARD TABLE OF ts_field_name WITH EMPTY KEY.
    DATA composition_field_names TYPE STANDARD TABLE OF ts_field_name WITH EMPTY KEY.

    DATA ls_fields TYPE ts_field.
    DATA lo_fields TYPE sxco_t_cds_fields  .
    DATA lo_assoc TYPE sxco_t_cds_associations .
    DATA lo_composition TYPE sxco_t_cds_compositions .

    DATA(lo_data_definition) = xco_lib->get_data_definition( CONV #( io_cds_view_name ) ).
    DATA(view_type) = lo_data_definition->get_type( ).

    CLEAR lo_assoc.
    CLEAR lo_composition.

    " method entity( ) works for getting fields for all entity types
    CASE view_type .
      WHEN xco_cp_data_definition=>type->view_entity.
        lo_assoc = lo_data_definition->view_entity( )->associations->all->get(  ).
        lo_composition = lo_data_definition->view_entity( )->compositions->all->get(  ).
        lo_fields = lo_data_definition->view_entity( )->fields->all->get(  ).


*        DATA(view_entity) = xco_lib->get_view_entity(  CONV #( io_cds_view_name ) ).
*
*        DATA(lo_view_entity_Fields) = view_entity->fields->all->get(  ).

      WHEN xco_cp_data_definition=>type->view.
        lo_assoc = lo_data_definition->view( )->associations->all->get(  ).
        lo_composition = lo_data_definition->view( )->compositions->all->get(  ).
        lo_fields = lo_data_definition->view( )->fields->all->get(  ).

        "get value of annotation @AbapCatalog.sqlViewName
        "to retrieve the name of the sql view name


*        DATA(view) = xco_lib->get_view_entity(  CONV #( io_cds_view_name ) ).
*
*        DATA(lo_view_Fields) = view->fields->all->get(  ).
*
*        lo_fields = lo_view_Fields.

      WHEN xco_cp_data_definition=>type->abstract_entity.
        set_is_abstract_or_cust_entity(  ).
        lo_fields = lo_data_definition->abstract_entity( )->fields->all->get(  ).
        " in abstract and custom entities associations and compositions are defined as fields
        LOOP AT lo_fields INTO DATA(lo_field).
          IF lo_field->content(  )->get(  )-association-target IS NOT INITIAL.
            APPEND lo_field->name TO association_field_names.
          ENDIF.
          IF lo_field->content(  )->get(  )-composition-target IS NOT INITIAL.
            APPEND lo_field->name TO  composition_field_names.
          ENDIF.
        ENDLOOP.

      WHEN xco_cp_data_definition=>type->custom_entity.

        set_is_abstract_or_cust_entity(  ).
        lo_fields = lo_data_definition->custom_entity( )->fields->all->get(  ).
        " in abstract and custom entities associations and compositions are defined as fields
        LOOP AT lo_fields INTO lo_field.
          IF lo_field->content(  )->get(  )-association-target IS NOT INITIAL.
            APPEND lo_field->name TO association_field_names.
          ENDIF.
          IF lo_field->content(  )->get(  )-composition-target IS NOT INITIAL.
            APPEND lo_field->name TO  composition_field_names.
          ENDIF.
        ENDLOOP.


      WHEN OTHERS.

        RAISE EXCEPTION TYPE /dmo/cx_rap_generator
          EXPORTING
            textid    = /dmo/cx_rap_generator=>view_type_not_supported
            mv_value  = | { view_type->value } |
            mv_entity = entityname.


    ENDCASE.

    LOOP AT lo_assoc INTO DATA(assoc).
      APPEND assoc->name TO association_field_names.
    ENDLOOP.
    LOOP AT lo_composition INTO DATA(composition_field).
      APPEND composition_field->content( )->get(  )-alias TO composition_field_names.
    ENDLOOP.






    LOOP AT lo_fields INTO lo_field.

      IF line_exists( association_field_names[ field_name = lo_field->name ] ).
        DATA(is_association) = abap_true.
      ENDIF.

      IF line_exists( composition_field_names[ field_name = lo_field->name ] ).
        DATA(is_composition) = abap_true.
      ENDIF.

      "only add "real" fields to the field list

      IF is_association = abap_false AND is_composition = abap_false.

        CLEAR ls_fields.
        " DATA(underscore) = substring( val = lo_field->name  len = 1 ).

        "skip associations that are added as field names as well
        "   IF underscore <> '_'.

        ls_fields-name = lo_field->name.
        DATA(field_content) = lo_field->content( )->get( ).
        IF field_content-alias IS INITIAL.
          ls_fields-cds_view_field = ls_fields-name.
        ELSE.
          ls_fields-cds_view_field = field_content-alias.
        ENDIF.

        ls_fields-key_indicator =  field_content-key_indicator.

        DATA(aggregated_annotations) = xco_lib->get_aggregated_annotations( lo_field ).

        IF aggregated_annotations->contain( 'SEMANTICS.AMOUNT' ).
          TRY.
              DATA(semantics_amount_annotation) = aggregated_annotations->pick( 'SEMANTICS.AMOUNT' )->get_value( ).
              semantics_amount_annotation->write_to(  REF #( semantic_amount ) ).
              IF semantic_amount IS NOT INITIAL.
                ls_fields-currencycode = to_upper( semantic_amount-currencycode ) .
              ENDIF.
            CATCH cx_root INTO DATA(exception).
          ENDTRY.
        ENDIF.

        "for example @Semantics.quantity.unitOfMeasure: 'QuantityUnit'
        IF aggregated_annotations->contain( 'SEMANTICS.QUANTITY' ).
          TRY.
              DATA(semantics_quantity_annotation) = aggregated_annotations->pick( 'SEMANTICS.QUANTITY' )->get_value( ).
              semantics_quantity_annotation->write_to(  REF #( semantic_quantity ) ).
              IF semantic_quantity IS NOT INITIAL.
                ls_fields-unitofmeasure = to_upper( semantic_quantity-unitofmeasure ).
              ENDIF.
            CATCH cx_root INTO exception.
          ENDTRY.
        ENDIF.

        "retrieve data elements or built in types

        DATA(field_type) = lo_field->content( )->get_type(  ).

        "For views (CDS views with a SQL view) and entity views "field_type" turned out to be initial.
        "For abstract entities it works
        "To work around this blocker and to enable the use case of generating services
        "based on Service Consumption Models (which are generating abstract entities)
        "we skip filling the information of data elements and built in types for
        "views and view entities for now

        IF field_type IS NOT INITIAL.

          IF field_type->is_data_element(  ).

            ls_fields-is_data_element = abap_true.

            DATA(lo_data_element) = field_type->get_data_element( ).

            read_data_element(
              EXPORTING
                io_data_element = lo_data_element
                is_fields       = ls_fields
              IMPORTING
                es_fields       = ls_fields
            ).

          ELSEIF field_type->is_built_in_type(  ).

            ls_fields-is_built_in_type = abap_true.

            ls_fields-built_in_type  = field_type->get_built_in_type(  )->type.
            ls_fields-built_in_type_length = field_type->get_built_in_type(  )->length.
            ls_fields-built_in_type_decimals = field_type->get_built_in_type(  )->decimals.




          ENDIF.
        ENDIF.
        "abstract entities created from service consumption models
        "contain an additional field for each field that contains
        "a value control information

        IF ls_fields-data_element NE 'RAP_CP_ODATA_VALUE_CONTROL'.
          APPEND ls_fields TO et_fields.
        ENDIF.

      ENDIF.

    ENDLOOP.


  ENDMETHOD.



  METHOD is_abstract_or_custom_entity.
    rv_is_abstract_or_cust_entity =  is_abstract_or_cust_entity.
  ENDMETHOD.

  METHOD set_is_abstract_or_cust_entity.
    is_abstract_or_cust_entity = iv_value.
  ENDMETHOD.

  METHOD generate_custom_entity.

    IF data_source_type = data_source_types-abap_type OR
       data_source_type = data_source_types-structure OR
       is_abstract_or_custom_entity(  ) .

      result = abap_true.

    ELSE.

      result = abap_false.

    ENDIF.

  ENDMETHOD.

ENDCLASS.