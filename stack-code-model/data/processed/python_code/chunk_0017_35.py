"! <p class="shorttext synchronized" lang="en">Resolves CDS Field Hierarchy</p>
"! This class can be used to resolve the complete hierachy
"! of a specific field of a CDS view. The hierarchy will be return in a deep
"! structure
CLASS zcl_sat_cds_field_hier_res DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.
    "! <p class="shorttext synchronized" lang="en">CONSTRUCTOR</p>
    METHODS constructor.
    "! <p class="shorttext synchronized" lang="en">CLASS CONSTRUCTOR</p>
    CLASS-METHODS class_constructor.

    "! <p class="shorttext synchronized" lang="en">Resolve field hierarchy of the given CDS field</p>
    METHODS resolve_field_hierarchy
      IMPORTING
        iv_cds_view         TYPE zsat_cds_view_name
        iv_cds_view_field   TYPE fieldname
      RETURNING
        VALUE(rs_hierarchy) TYPE zsat_adt_element_info.
  PROTECTED SECTION.
  PRIVATE SECTION.
    TYPES: ty_t_field_hierarchy_flat TYPE STANDARD TABLE OF zsat_i_cdsfieldhierarchy.
    TYPES:
      BEGIN OF ty_s_cached_node,
        entity    TYPE tabname,
        field_ref TYPE REF TO lcl_field,
      END OF ty_s_cached_node.
    DATA mt_cached_nodes TYPE STANDARD TABLE OF ty_s_cached_node.
    DATA mo_path_resolver TYPE REF TO cl_ddic_adt_ddls_path_resolver.
    "! <p class="shorttext synchronized" lang="en">Retrieve all child nodes for the given view field</p>
    METHODS get_children
      IMPORTING
        iv_viewname  TYPE tabname
        iv_fieldname TYPE fieldname
        it_hierarchy TYPE ty_t_field_hierarchy_flat
        io_field     TYPE REF TO lcl_field.

    "! <p class="shorttext synchronized" lang="en">Converts field information to element info</p>
    METHODS convert_field_to_elem_info
      IMPORTING
        io_field     TYPE REF TO lcl_field
      CHANGING
        cs_elem_info TYPE zsat_adt_element_info.
    "! <p class="shorttext synchronized" lang="en">Fills element info from field</p>
    METHODS fill_element_info_from_field
      IMPORTING
        io_field     TYPE REF TO lcl_field
      CHANGING
        cs_elem_info TYPE zsat_adt_element_info.
    "! <p class="shorttext synchronized" lang="en">Fills entity type information of fields</p>
    METHODS fill_type_information.
ENDCLASS.



CLASS zcl_sat_cds_field_hier_res IMPLEMENTATION.

  METHOD constructor.
    mo_path_resolver  = NEW cl_ddic_adt_ddls_path_resolver( ).
  ENDMETHOD.

  METHOD class_constructor.
  ENDMETHOD.

  METHOD resolve_field_hierarchy.
    FIELD-SYMBOLS: <ls_current_hierarchy> TYPE zsat_adt_element_info.

    SELECT
      FROM zsat_i_cdsfieldhierarchy( p_cdsviewname = @iv_cds_view, p_cdsfieldname = @iv_cds_view_field )
      FIELDS *
      ORDER BY level
    INTO TABLE @DATA(lt_hierarchy_flat).

    CHECK sy-subrc = 0.

    DATA(ls_base_row) = lt_hierarchy_flat[ 1 ].

    DATA(lo_root_field) = NEW lcl_field( ).

    lo_root_field->field = ls_base_row-viewfield.
    lo_root_field->raw_field = ls_base_row-viewfieldraw.
    lo_root_field->view_name = ls_base_row-viewname.
    lo_root_field->view_raw_name = ls_base_row-entityname.
    lo_root_field->secondary_entity = ls_base_row-ddlname.
    lo_root_field->adt_type = zif_sat_c_adt_utils=>c_adt_types-data_definition.
    lo_root_field->uri = zcl_sat_adt_util=>create_adt_uri(
      iv_name2 = CONV #( ls_base_row-ddlname )
      iv_type  = zif_sat_c_entity_type=>cds_view
    )-uri.

    get_children(
        iv_viewname  = ls_base_row-viewname
        iv_fieldname = ls_base_row-viewfield
        it_hierarchy = lt_hierarchy_flat
        io_field     = lo_root_field
    ).

    fill_type_information( ).

*.. Convert result into element info structure for ADT resource
    convert_field_to_elem_info(
      EXPORTING io_field     = lo_root_field
      CHANGING  cs_elem_info = rs_hierarchy
    ).
  ENDMETHOD.

  METHOD get_children.
    FIELD-SYMBOLS: <lt_child_nodes> TYPE zsat_adt_element_info_t.

    LOOP AT it_hierarchy ASSIGNING FIELD-SYMBOL(<ls_hierarchy>) WHERE viewname = iv_viewname
                                                                  AND viewfield = iv_fieldname.

      DATA(lv_base_table) = <ls_hierarchy>-basetable.
      IF lv_base_table IN zcl_sat_cds_view_factory=>gt_helper_ddl_tab_names.
*...... Is indication that the field is calculated and a parsing of the owning CDS view
*........ is needed to get the origin of the field (e.g. case when ... then view1.field2 else view2.field3 )
        io_field->is_calculated = abap_true.
        RETURN.
      ENDIF.

      DATA(lo_child_field) = NEW lcl_field( ).
      lo_child_field->field = <ls_hierarchy>-basefield.
      lo_child_field->secondary_entity = <ls_hierarchy>-baseddlname.
      lo_child_field->raw_field = COND #( WHEN <ls_hierarchy>-basefieldraw IS NOT INITIAL THEN <ls_hierarchy>-basefieldraw ELSE <ls_hierarchy>-basefield ).
      lo_child_field->view_name = to_upper( <ls_hierarchy>-basetable ).
      lo_child_field->view_raw_name = COND #( WHEN <ls_hierarchy>-baseentityname IS NOT INITIAL THEN <ls_hierarchy>-baseentityname ELSE <ls_hierarchy>-basetable ).
      lo_child_field->source_type = <ls_hierarchy>-basesourcetype.

*.... Recursive call to get all the sub children
      get_children(
          iv_viewname  = <ls_hierarchy>-basetable
          iv_fieldname = <ls_hierarchy>-basefield
          it_hierarchy = it_hierarchy
          io_field     = lo_child_field
      ).

      CHECK lo_child_field IS NOT INITIAL.

*...... Add field to the children of the current hierarchy level
      IF io_field->children IS INITIAL.
        io_field->children = VALUE #( ).
      ENDIF.

      io_field->children = VALUE #( BASE io_field->children ( lo_child_field ) ).
      mt_cached_nodes = VALUE #( BASE mt_cached_nodes ( entity = to_upper( lo_child_field->view_raw_name ) field_ref = lo_child_field ) ).
    ENDLOOP.

  ENDMETHOD.

  METHOD convert_field_to_elem_info.
    FIELD-SYMBOLS: <lt_children> TYPE zsat_adt_element_info_t.

    fill_element_info_from_field( EXPORTING io_field = io_field CHANGING cs_elem_info = cs_elem_info ).

    IF io_field->children IS NOT INITIAL.
      cs_elem_info-children = NEW zsat_adt_element_info_t( ).
      ASSIGN cs_elem_info-children->* TO <lt_children>.
    ENDIF.

    LOOP AT io_field->children INTO DATA(lo_child).
      APPEND INITIAL LINE TO <lt_children> ASSIGNING FIELD-SYMBOL(<ls_child_eleminfo>).
      convert_field_to_elem_info(
        EXPORTING io_field      = lo_child
        CHANGING  cs_elem_info = <ls_child_eleminfo>
      ).
    ENDLOOP.
  ENDMETHOD.

  METHOD fill_element_info_from_field.
    cs_elem_info-name = COND #( WHEN io_field->secondary_entity IS NOT INITIAL THEN io_field->secondary_entity ELSE io_field->view_name ).
    cs_elem_info-type = io_field->adt_type.
    cs_elem_info-uri = io_field->uri.
    cs_elem_info-raw_name = io_field->view_raw_name.

*.. Fill properties
    IF io_field->raw_field IS NOT INITIAL.
      cs_elem_info-properties = VALUE #( BASE cs_elem_info-properties
        ( key   = 'FIELD'
          value = io_field->raw_field )
      ).
    ENDIF.
    IF io_field->source_type IS NOT INITIAL.
      cs_elem_info-properties = VALUE #( BASE cs_elem_info-properties
        ( key   = 'SOURCE_TYPE'
          value = io_field->source_type )
      ).
    ENDIF.
    IF io_field->is_calculated = abap_true.
      cs_elem_info-properties = VALUE #( BASE cs_elem_info-properties
        ( key   = 'IS_CALCULATED'
          value = 'X' )
      ).
    ENDIF.
  ENDMETHOD.


  METHOD fill_type_information.
    DATA: lt_entity       TYPE RANGE OF zsat_entity_id,
          lv_name_for_uri TYPE string,
          ls_wb_type      TYPE wbobjtype.

    CHECK mt_cached_nodes IS NOT INITIAL.

    lt_entity = VALUE #( FOR field IN mt_cached_nodes ( sign = 'I' option = 'EQ' low = field-entity ) ).
    SELECT *
     FROM zsat_i_databaseentitywotext
     WHERE entity IN @lt_entity
    INTO TABLE @DATA(lt_entity_type).

    CHECK sy-subrc = 0.

    LOOP AT lt_entity_type ASSIGNING FIELD-SYMBOL(<ls_entity_type>).

      LOOP AT mt_cached_nodes ASSIGNING FIELD-SYMBOL(<ls_cached_node>) WHERE entity = <ls_entity_type>-entity.
*...... Fill the URI
        DATA(ls_adt_obj_ref) = zcl_sat_adt_util=>create_adt_uri(
            iv_type  = <ls_entity_type>-type
            iv_name  = CONV #( <ls_cached_node>-field_ref->view_name )
            iv_name2 = CONV #( <ls_cached_node>-field_ref->secondary_entity )
        ).
        <ls_cached_node>-field_ref->uri = ls_adt_obj_ref-uri.
        <ls_cached_node>-field_ref->adt_type = ls_adt_obj_ref-type.
      ENDLOOP.

    ENDLOOP.
  ENDMETHOD.

ENDCLASS.