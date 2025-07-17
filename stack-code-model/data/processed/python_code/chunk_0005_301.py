class ZCL_WD_CONTEXT definition
  public
  final
  create public .

*"* public components of class ZCL_WD_CONTEXT
*"* do not include other source files here!!!
public section.
  type-pools ABAP .
  interface IF_WD_CONTEXT_NODE load .
  interface IF_WD_CONTEXT_NODE_INFO load .

  data R_CONTEXT type ref to IF_WD_CONTEXT_NODE .

  class-methods GET
    importing
      !IR_CONTEXT type ref to IF_WD_CONTEXT_NODE
    returning
      value(ER_CONTEXT) type ref to ZCL_WD_CONTEXT .
  methods CONSTRUCTOR
    importing
      !IR_CONTEXT type ref to IF_WD_CONTEXT_NODE .
  methods CREATE_NODE
    importing
      !I_PATH type STRING
      !IT_FIELDS type ZCL_ABAP_STATIC=>TT_FIELDS
      !I_INITIALIZE_LEAD_SELECTION type ABAP_BOOL default ABAP_FALSE
      !IS_MULTIPLE_SELECTION type ABAP_BOOL default ABAP_FALSE
    returning
      value(ER_INFO) type ref to IF_WD_CONTEXT_NODE_INFO .
  methods GET_NODE
    importing
      !I_PATH type STRING
    returning
      value(ER_NODE) type ref to IF_WD_CONTEXT_NODE .
  methods CLEAR
    importing
      !I_PATH type SIMPLE .
  methods GET_VALUE
    importing
      !I_PATH type STRING
      !I_INDEX type I default IF_WD_CONTEXT_NODE=>USE_LEAD_SELECTION
      !I_FIELD type STRING optional
    returning
      value(E_VALUE) type STRING .
  methods SET_VALUE
    importing
      !I_PATH type STRING
      !I_INDEX type I default IF_WD_CONTEXT_NODE=>USE_LEAD_SELECTION
      !I_FIELD type STRING optional
      !I_VALUE type DATA optional .
  methods GET_STRUCTURE
    importing
      !I_PATH type STRING
      !I_INDEX type I default IF_WD_CONTEXT_NODE=>USE_LEAD_SELECTION
    exporting
      value(ES_DATA) type DATA .
  methods SET_STRUCTURE
    importing
      !I_PATH type STRING
      !I_INDEX type I default IF_WD_CONTEXT_NODE=>USE_LEAD_SELECTION
      !IS_DATA type DATA .
  methods GET_TABLE
    importing
      !I_PATH type STRING
      !I_STATIC type ABAP_BOOL default ABAP_TRUE
    exporting
      !ET_DATA type TABLE .
  methods SET_TABLE
    importing
      !I_PATH type STRING
      !IT_DATA type ANY TABLE
      !I_SOFT type ABAP_BOOL default ABAP_FALSE
      !I_FIELD type STRING optional .
  methods SELECT
    importing
      !I_PATH type STRING
      !I_INDEX type I default 1 .
  methods GET_SELECTION
    importing
      !I_PATH type STRING
    returning
      value(E_INDEX) type I .
  methods CLEAR_SELECTION
    importing
      !I_PATH type STRING .
  methods GET_SELECTED
    importing
      !I_PATH type STRING
    exporting
      value(ET_DATA) type DATA .
  methods DELETE_SELECTED
    importing
      !I_PATH type STRING .
  methods UPDATE_SELECTED
    importing
      !I_PATH type SIMPLE
      !IS_DATA type DATA .
  methods SET_PROPERTY
    importing
      !I_PATH type STRING
      !I_INDEX type I default IF_WD_CONTEXT_NODE=>USE_LEAD_SELECTION
      !I_FIELD type STRING optional
      !I_PROPERTY type STRING
      !I_VALUE type ABAP_BOOL default ABAP_FALSE .
  methods GET_VALUES
    importing
      !I_PATH type STRING
      !I_FIELD type STRING optional
    returning
      value(ET_VALUES) type ZIVALUES .
  methods SET_VALUES
    importing
      !I_PATH type STRING
      !I_FIELD type STRING optional
      !IT_VALUES type ZIVALUES .
  methods SET_NULLABLE
    importing
      !I_PATH type STRING
      !I_FIELD type STRING optional .
  methods SET_SEARCH_HELP
    importing
      !I_PATH type SIMPLE
      !I_FIELD type SIMPLE optional
      !I_NAME type SIMPLE optional
      !I_MODE type I default IF_WD_CONTEXT_NODE_INFO=>C_VALUE_HELP_MODE-DDIC .
  methods ADD_FIELD
    importing
      !I_PATH type STRING
      !I_NAME type STRING
      !I_TYPE type STRING .
  methods ADD_FIELDS
    importing
      !I_PATH type STRING
      !IT_FIELDS type ZCL_ABAP_STATIC=>TT_FIELDS .
  methods APPEND
    importing
      !I_PATH type STRING
      !IS_DATA type DATA .
  methods SET_TRUE
    importing
      !I_PATH type STRING .
  methods SET_FALSE
    importing
      !I_PATH type STRING .
  methods SET_CHANGED
    importing
      !I_PATH type SIMPLE .
  methods WAS_CHANGED
    importing
      !I_PATH type SIMPLE
    returning
      value(E_IS) type ABAP_BOOL .
  methods RESET_CHANGED
    importing
      !I_PATH type SIMPLE .
  protected section.
*"* protected components of class ZCLSRM_CONTEXT
*"* do not include other source files here!!!
  private section.
*"* private components of class ZCL_WD_CONTEXT
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCL_WD_CONTEXT IMPLEMENTATION.


  method add_field.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( i_path ).

    data lr_info type ref to if_wd_context_node_info.
    lr_info = lr_node->get_node_info( ).

    data ls_attribute type wdr_context_attribute_info.
    ls_attribute-name = i_name.
    ls_attribute-type_name = i_type.

    lr_info->add_attribute( ls_attribute ).

  endmethod.


  method add_fields.

    data ls_field like line of it_fields.
    loop at it_fields into ls_field.

      add_field(
        i_path = i_path
        i_name = ls_field-name
        i_type = ls_field-type ).

    endloop.

  endmethod.


  method append.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( i_path ).

    lr_node->bind_structure(
      exporting
        new_item             = is_data
        set_initial_elements = abap_false ).

  endmethod.


  method clear.

    data l_path type string.
    l_path = i_path.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( l_path ).

    data lt_elements type wdr_context_element_set.
    lt_elements = lr_node->get_elements( ).

    data lr_element like line of lt_elements.
    loop at lt_elements into lr_element.

      lr_node->remove_element( lr_element ).

    endloop.

  endmethod.


  method clear_selection.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( i_path ).
    lr_node->set_lead_selection_index( if_wd_context_node=>no_selection ).

  endmethod.


  method constructor.

    r_context = ir_context.

  endmethod.


  method create_node.

    data l_path type string.
    data l_name type string.
    find regex '(.*)[.](.*)' in i_path submatches l_path l_name.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( l_path ).

    data lr_info type ref to if_wd_context_node_info.
    lr_info = lr_node->get_node_info( ).

    data lr_data type ref to data.
    lr_data = zcl_abap_static=>create_structure( it_fields ).

    data lr_structure type ref to cl_abap_structdescr.
    lr_structure ?= cl_abap_structdescr=>describe_by_data_ref( lr_data ).

    er_info =
      lr_info->add_new_child_node(
        name                         = l_name
        is_initialize_lead_selection = i_initialize_lead_selection "abap_false
        is_multiple_selection        = is_multiple_selection "abap_false
        static_element_rtti          = lr_structure
        is_static                    = abap_false ).

  endmethod.


  method delete_selected.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( i_path ).

    data lt_elements type wdr_context_element_set.
    lt_elements = lr_node->get_selected_elements( including_lead_selection = abap_true ).

    data lr_element  like line of lt_elements.
    loop at lt_elements into lr_element.
      lr_node->remove_element( lr_element ).
    endloop.

  endmethod.


  method get.

    create object er_context
      exporting
        ir_context = ir_context.

  endmethod.


  method get_node.

    er_node = r_context->path_get_node( i_path ).

  endmethod.


  method get_selected.

    field-symbols <lt_data> type standard table.
    assign et_data to <lt_data>.
    assert sy-subrc eq 0.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( i_path ).

    data lt_elements type wdr_context_element_set.
    lt_elements = lr_node->get_selected_elements( including_lead_selection = abap_true ).

    data lr_element  like line of lt_elements.
    loop at lt_elements into lr_element.

      field-symbols <ls_data> type any.
      append initial line to <lt_data> assigning <ls_data>.

      lr_element->get_static_attributes(
        importing
          static_attributes = <ls_data> ).

    endloop.

  endmethod.


  method get_selection.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( i_path ).

    e_index = lr_node->get_lead_selection_index( ).

    if e_index eq if_wd_context_node=>no_selection.
      e_index = 0.
    endif.

  endmethod.


  method get_structure.

    if i_index eq if_wd_context_node=>use_lead_selection and
       get_selection( i_path ) eq 0.
      return.
    endif.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( i_path ).

    lr_node->get_static_attributes(
      exporting
        index             = i_index
      importing
        static_attributes = es_data ).

  endmethod.


  method get_table.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( i_path ).

    if i_static eq abap_true.

      lr_node->get_static_attributes_table(
        importing
          table = et_data ).

    else.

      data lr_info type ref to if_wd_context_node_info.
      lr_info = lr_node->get_node_info( ).

      data lt_attributes type wdr_context_attr_info_map.
      lt_attributes = lr_info->get_attributes( ).

      data lt_elements type wdr_context_element_set.
      lt_elements = lr_node->get_elements( ).

      data lr_element like line of lt_elements.
      loop at lt_elements into lr_element.

        field-symbols <ls_data> type any.
        append initial line to et_data assigning <ls_data>.

        data ls_attribute like line of lt_attributes.
        loop at lt_attributes into ls_attribute.

          field-symbols <l_value> type any.
          assign component ls_attribute-name of structure <ls_data> to <l_value>.
          if sy-subrc eq 0.
            lr_element->get_attribute(
              exporting name = ls_attribute-name
              importing value = <l_value> ).
          endif.

        endloop.

      endloop.

    endif.

  endmethod.


  method get_value.

    data l_path type string.
    l_path = i_path.

    data l_field type string.
    l_field = i_field.

    if l_field is initial.
      find regex '(.*)[.](.*)' in i_path submatches l_path l_field.
    endif.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( l_path ).

    lr_node->get_attribute(
      exporting
        name  = l_field
        index = i_index
      importing
        value = e_value ).

  endmethod.


  method get_values.

    data l_path type string.
    l_path = i_path.

    data l_field type string.
    l_field = i_field.

    if l_field is initial.
      find regex '(.*)[.](.*)' in i_path submatches l_path l_field.
    endif.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( l_path ).

    data lr_info type ref to if_wd_context_node_info.
    lr_info = lr_node->get_node_info( ).

    data ls_info type wdr_context_attribute_info.
    ls_info = lr_info->get_attribute( l_field ).

    et_values = ls_info-value_set.

  endmethod.


  method reset_changed.

    data l_path type string.
    l_path = i_path.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( l_path ).

    lr_node->reset_changed_by_client( ).

  endmethod.


  method select.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( i_path ).

    lr_node->set_lead_selection_index( i_index ).

  endmethod.


  method set_changed.

    data l_path type string.
    l_path = i_path.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( l_path ).

    lr_node->set_changed_by_client( ).

    data lt_elements type wdr_context_element_set.
    lt_elements = lr_node->get_elements( ).

    data lr_element like line of lt_elements.
    loop at lt_elements into lr_element.
      lr_element->set_changed_by_client( ).
    endloop.

  endmethod.


  method set_false.

    set_value(
      i_path  = i_path
      i_value = abap_false ).

  endmethod.


  method set_nullable.

    data l_path type string.
    l_path = i_path.

    data l_field type string.
    l_field = i_field.

    if l_field is initial.
      find regex '(.*)[.](.*)' in i_path submatches l_path l_field.
    endif.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( l_path ).

    data lr_info type ref to if_wd_context_node_info.
    lr_info = lr_node->get_node_info( ).

    lr_info->set_nullable( l_field ).

  endmethod.


  method set_property.

    data l_path type string.
    l_path = i_path.

    data l_field type string.
    l_field = i_field.

    if l_field is initial.
      find regex '(.*)[.](.*)' in i_path submatches l_path l_field.
    endif.

    data l_property type i.
    case i_property.
      when 'VISIBLE'.
        l_property = if_wd_context_element=>e_property-visible.
      when 'REQUIRED'.
        l_property = if_wd_context_element=>e_property-required.
      when 'READONLY'.
        l_property = if_wd_context_element=>e_property-read_only.
      when 'ENABLED'.
        l_property = if_wd_context_element=>e_property-enabled.
      when others.
        assert 1 = 2.
    endcase.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( l_path ).

    lr_node->set_attribute_property(
      index          = i_index
      attribute_name = l_field
      property       = l_property
      value          = i_value ).

  endmethod.


  method set_search_help.

    data l_path type string.
    l_path = i_path.

    data l_field type string.
    l_field = i_field.

    if l_field is initial.
      find regex '(.*)[.](.*)' in i_path submatches l_path l_field.
    endif.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( l_path ).

    data lr_info type ref to if_wd_context_node_info.
    lr_info = lr_node->get_node_info( ).

    data l_name type string.
    l_name = i_name.

    lr_info->set_attribute_value_help(
      name            = l_field
      value_help_mode = i_mode   "if_wd_context_node_info=>c_value_help_mode-ovs
      value_help      = l_name ).

  endmethod.


  method set_structure.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( i_path ).

    lr_node->set_static_attributes(
      index             = i_index
      static_attributes = is_data ).

  endmethod.


  method set_table.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( i_path ).

    lr_node->bind_table( it_data ).

  endmethod.


  method set_true.

    set_value(
      i_path  = i_path
      i_value = abap_true ).

  endmethod.


  method set_value.

    data l_path type string.
    l_path = i_path.

    data l_field type string.
    l_field = i_field.

    if l_field is initial.
      find regex '(.*)[.](.*)' in i_path submatches l_path l_field.
    endif.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( l_path ).

    lr_node->set_attribute(
      index = i_index
      name  = l_field
      value = i_value ).

  endmethod.


  method set_values.

    data l_path type string.
    l_path = i_path.

    data l_field type string.
    l_field = i_field.

    if l_field is initial.
      find regex '(.*)[.](.*)' in i_path submatches l_path l_field.
    endif.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( l_path ).

    data lr_info type ref to if_wd_context_node_info.
    lr_info = lr_node->get_node_info( ).

    lr_info->set_attribute_value_set(
      exporting
        name      = l_field
        value_set = it_values ).

  endmethod.


  method update_selected.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( i_path ).

    data lt_elements type wdr_context_element_set.
    lt_elements =
      lr_node->get_selected_elements(
        including_lead_selection = abap_true ).

    data lr_element  like line of lt_elements.
    loop at lt_elements into lr_element.
      lr_element->set_static_attributes( is_data ).
    endloop.

  endmethod.


  method was_changed.

    data l_path type string.
    l_path = i_path.

    data lr_node type ref to if_wd_context_node.
    lr_node = r_context->path_get_node( l_path ).

    e_is = lr_node->is_changed_by_client( ).

  endmethod.
ENDCLASS.