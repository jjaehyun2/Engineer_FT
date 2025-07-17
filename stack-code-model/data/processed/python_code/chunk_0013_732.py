class ZCL_WD_TABLE definition
  public
  final
  create public .

*"* public components of class ZCL_WD_TABLE
*"* do not include other source files here!!!
public section.
  type-pools ABAP .

  data R_WD_TABLE type ref to IWCI_SALV_WD_TABLE .
  data R_CONFIG type ref to CL_SALV_WD_CONFIG_TABLE .
  data R_TABLE type ref to IF_SALV_WD_TABLE_SETTINGS .
  data R_HIERARCHY type ref to IF_SALV_WD_TABLE_HIERARCHY .
  data R_COLUMNS type ref to IF_SALV_WD_COLUMN_SETTINGS .
  data R_FIELDS type ref to IF_SALV_WD_FIELD_SETTINGS .
  data R_S_FUNC type ref to IF_SALV_WD_STD_FUNCTIONS .
  data R_U_FUNC type ref to IF_SALV_WD_FUNCTION_SETTINGS .

  methods CONSTRUCTOR
    importing
      !IR_TABLE type ref to IWCI_SALV_WD_TABLE .
  class-methods GET
    importing
      !IR_TABLE type ref to IWCI_SALV_WD_TABLE
    returning
      value(ER_TABLE) type ref to ZCL_WD_TABLE .
  class-methods GET_BY_USAGE
    importing
      !IR_USAGE type ref to IF_WD_COMPONENT_USAGE
    returning
      value(ER_TABLE) type ref to ZCL_WD_TABLE .
  methods INIT
    importing
      !IV_VARIANT type I default 1 .
  methods REFRESH .
  methods SET_TITLE
    importing
      !IV_TEXT type DATA .
  methods SET_ROWS
    importing
      !I_ROWS type I .
  methods SET_WIDTH
    importing
      !I_WIDTH type SIMPLE optional .
  methods ENABLE_HIERARCHY
    importing
      !I_EXPANDED type ABAP_BOOL default ABAP_TRUE .
  methods ADD_SEPARATOR
    importing
      !IV_ID type STRING optional .
  methods ADD_BUTTON
    importing
      !IV_ID type SIMPLE
      !IV_TEXT type SIMPLE optional
      !IV_IMAGE type SIMPLE optional
      !IV_CHOICE type ABAP_BOOL default ABAP_FALSE
      !IT_CHOICES type ZIVALUES optional
      !IV_SEPARATOR type ABAP_BOOL default ABAP_FALSE .
  methods ADD_CHOICE
    importing
      !IV_BUTTON type STRING
      !IV_ID type STRING
      !IV_TEXT type DATA .
  methods REMOVE_CHOICES
    importing
      !IV_BUTTON type SIMPLE .
  methods REMOVE_CHOICE
    importing
      !IV_BUTTON type STRING
      !IV_ID type STRING .
  methods ADD_INPUT
    importing
      !IV_ID type SIMPLE
      !IV_TEXT type SIMPLE optional .
  methods ADD_LINK
    importing
      !IV_ID type SIMPLE
      !IV_TEXT type SIMPLE .
  methods SET_LINK
    importing
      !IV_ID type SIMPLE
      !IV_TEXT type SIMPLE .
  methods DISABLE_BUTTON
    importing
      !IV_ID type STRING .
  methods ENABLE_BUTTON
    importing
      !IV_ID type STRING .
  methods HIDE_FUNCTIONS .
  methods HIDE_FUNCTION
    importing
      !IV_ID type STRING .
  methods SHOW_FUNCTIONS .
  methods SHOW_FUNCTION
    importing
      !IV_ID type STRING .
  methods DISABLE_FUNCTIONS .
  methods DISABLE_FUNCTION
    importing
      !IV_ID type STRING .
  methods ENABLE_FUNCTIONS .
  methods ENABLE_FUNCTION
    importing
      !IV_ID type STRING .
  methods GET_COLUMNS
    returning
      value(ET_COLUMNS) type STRINGTAB .
  methods HIDE_COLUMN
    importing
      !IV_ID type STRING .
  methods HIDE_COLUMNS .
  methods SHOW_COLUMN
    importing
      !IV_ID type STRING
      !IV_POSITION type I optional .
  methods SET_COLUMN
    importing
      !IV_ID type SIMPLE
      !IV_TEXT type SIMPLE optional
      !IV_POSITION type I optional
      !IV_VISIBLE type SIMPLE optional
      !IV_ALIGN type SIMPLE optional
      !IV_WIDTH type SIMPLE optional
      !IV_FIXED type ABAP_BOOL optional
      !IV_HIERARCHY type ABAP_BOOL optional
      !IV_COLOR type SIMPLE optional
      !IV_SUM type ABAP_BOOL optional .
  methods SET_COLUMN_READONLY
    importing
      !I_ID type SIMPLE
      !I_READONLY type SIMPLE .
  methods SET_COLUMN_REQUIRED
    importing
      !I_ID type SIMPLE
      !I_REQUIRED type SIMPLE .
  methods SET_CELL_INPUT
    importing
      !IV_ID type SIMPLE
      !IV_READONLY type SIMPLE optional
      !IV_ENABLED type SIMPLE optional
      !IV_COLOR type SIMPLE optional
      !IV_VALUE type SIMPLE optional
      !IV_OBLIG type SIMPLE optional .
  methods SET_CELL_LINK
    importing
      !IV_ID type STRING
      !IV_TYPE type STRING default 'ACTION'
      !IV_ENABLED type STRING optional
      !IV_ENABLED_X type ABAP_BOOL optional
      !IV_COLOR type STRING optional
      !IV_IMAGE type SIMPLE optional
      !IV_WRAPPING type ABAP_BOOL optional .
  methods SET_CELL_CHECKBOX
    importing
      !IV_ID type STRING
      !IV_READONLY type SIMPLE optional
      !IV_READONLY_X type ABAP_BOOL optional .
  methods SET_CELL_DROPDOWN
    importing
      !IV_ID type STRING
      !IV_TYPE type STRING default 'KEY'
      !IV_VALUESET type STRING optional
      !IV_READONLY type SIMPLE optional
      !IV_OBLIG type SIMPLE optional .
  methods SET_CELL_TEXTVIEW
    importing
      !IV_ID type STRING
      !IV_ALIGN type SIMPLE optional
      !IV_WRAPPING type ABAP_BOOL default ABAP_TRUE
      !IV_WIDTH type SIMPLE optional .
  methods SET_CELL_IMAGE
    importing
      !IV_ID type STRING .
  methods SORT
    importing
      !IV_ID type STRING
      !IV_ORDER type SIMPLE default IF_SALV_WD_C_SORT=>SORT_ORDER_ASCENDING
      !IV_POSITION type I optional
      !IV_SUM type ABAP_BOOL optional .
  methods GET_READONLY
    returning
      value(E_READONLY) type ABAP_BOOL .
  methods SET_READONLY
    importing
      !I_READONLY type ABAP_BOOL .
  methods SET_EDIT_MODE .
  methods SET_DISPLAY_MODE .
  methods SET_EMPTY_TABLE_TEXT
    importing
      !I_TEXT type SIMPLE .
  methods SET_METADATA
    importing
      !IT_METADATA type ZCL_WD_STATIC=>TT_METADATA .
  protected section.
*"* protected components of class ZCL_WD_TABLE
*"* do not include other source files here!!!
  private section.
*"* private components of class ZCL_WD_TABLE
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCL_WD_TABLE IMPLEMENTATION.


  method add_button.

    data l_image type string.
    l_image = iv_image.

    data l_text type string.
    l_text = iv_text.

    if iv_separator eq abap_true.
      data lv_id type string.
      concatenate iv_id '_SPR' into lv_id.
      add_separator( lv_id ).
    endif.

    data lr_function type ref to cl_salv_wd_function.
    lr_function = r_u_func->create_function( iv_id ).

    if iv_choice eq abap_true.

      data lr_button_choice type ref to cl_salv_wd_fe_button_choice.
      create object lr_button_choice.
      lr_button_choice->set_text( l_text ).
      lr_button_choice->set_repeat_selected_action( abap_false ).

      if iv_image is supplied.
        lr_button_choice->set_image_source( l_image ).
      endif.

      data ls_choice like line of it_choices.
      loop at it_choices into ls_choice.

        data lr_choice type ref to cl_salv_wd_menu_action_item.
        create object lr_choice
          exporting
            id = ls_choice-id.

        lr_choice->set_text( ls_choice-text ).

        lr_button_choice->add_choice( lr_choice ).

      endloop.

      lr_function->set_editor( lr_button_choice ).

    else.

      data lr_button type ref to cl_salv_wd_fe_button.
      create object lr_button.
      lr_button->set_text( l_text ).

      if iv_image is supplied.
        lr_button->set_image_source( l_image ).
      endif.

      lr_function->set_editor( lr_button ).

    endif.

  endmethod.


  method add_choice.

    data lr_function type ref to cl_salv_wd_function.
    lr_function = r_u_func->get_function( iv_button ).

    data lr_button_choice type ref to cl_salv_wd_fe_button_choice.
    lr_button_choice ?= lr_function->get_editor( ).

    data lr_choice type ref to cl_salv_wd_menu_action_item.
    create object lr_choice
      exporting
        id = iv_id.

    lr_choice->set_text( iv_text ).
    lr_button_choice->add_choice( lr_choice ).

  endmethod.


  method add_input.

    data lr_function type ref to cl_salv_wd_function.
    lr_function = r_u_func->create_function( iv_id ).

    data lr_input type ref to cl_salv_wd_fe_input_field.
    create object lr_input
      exporting
        value_elementname = iv_id.

    if iv_text is supplied.

      data l_text type string.
      l_text = iv_text.

      lr_input->set_label_text( l_text ).

    endif.

    lr_function->set_editor( lr_input ).

  endmethod.


  method add_link.

    data l_id type string.
    l_id = iv_id.

    data lr_function type ref to cl_salv_wd_function.
    lr_function = r_u_func->create_function( l_id ).

    data lr_link type ref to cl_salv_wd_fe_link_to_action.
    create object lr_link.

    data l_text type string.
    l_text = iv_text.

    lr_link->set_text( l_text ).

    lr_function->set_editor( lr_link ).

  endmethod.


  method add_separator.

    data lr_separator type ref to cl_salv_wd_fe_separator.
    create object lr_separator.

    data lv_id type string.
    lv_id = iv_id.
    if lv_id is initial.
      lv_id = zcl_abap_static=>create_guid( ).
    endif.

    data lr_function type ref to cl_salv_wd_function.
    lr_function = r_u_func->create_function( iv_id ).

    lr_function->set_editor( lr_separator ).

  endmethod.


  method constructor.

    r_wd_table  = ir_table.

    r_config = r_wd_table->get_model( ).

    r_table     ?= r_config.
    r_hierarchy ?= r_config.
    r_columns   ?= r_config.
    r_fields    ?= r_config.
    r_s_func    ?= r_config.
    r_u_func    ?= r_config.

  endmethod.


  method disable_button.

    data lr_function type ref to cl_salv_wd_function.
    lr_function = r_u_func->get_function( iv_id ).
    lr_function->set_visible( cl_wd_uielement=>e_visible-none ).

    data lr_button type ref to cl_salv_wd_fe_button.
    lr_button ?= lr_function->get_editor( ).
    lr_button->set_enabled( abap_false ).

  endmethod.


  method disable_function.

    data lr_function type ref to cl_salv_wd_function.
    lr_function = r_u_func->get_function( iv_id ).

    if lr_function is bound.

      data lr_editor type ref to cl_salv_wd_fe_interactive.
      lr_editor ?= lr_function->get_editor( ).

      lr_editor->set_enabled( abap_false ).

    endif.

  endmethod.


  method disable_functions.

    data lt_functions type salv_wd_t_function_ref.
    lt_functions = r_u_func->get_functions( ).

    data ls_function like line of lt_functions.
    loop at lt_functions into ls_function.

      data lr_editor type ref to cl_salv_wd_fe_interactive.
      lr_editor ?= ls_function-r_function->get_editor( ).

      lr_editor->set_enabled( abap_false ).

    endloop.

  endmethod.


  method enable_button.

    data lr_function type ref to cl_salv_wd_function.
    lr_function = r_u_func->get_function( iv_id ).
    lr_function->set_visible( cl_wd_uielement=>e_visible-visible ).

    data lr_button type ref to cl_salv_wd_fe_button.
    lr_button ?= lr_function->get_editor( ).
    lr_button->set_enabled( abap_true ).

  endmethod.


  method enable_function.

    data lr_function type ref to cl_salv_wd_function.
    lr_function = r_u_func->get_function( iv_id ).

    if lr_function is bound.

      data lr_editor type ref to cl_salv_wd_fe_interactive.
      lr_editor ?= lr_function->get_editor( ).

      lr_editor->set_enabled( abap_true ).

    endif.

  endmethod.


  method enable_functions.

    data lt_functions type salv_wd_t_function_ref.
    lt_functions = r_u_func->get_functions( ).

    data ls_function like line of lt_functions.
    loop at lt_functions into ls_function.

      data lr_editor type ref to cl_salv_wd_fe_interactive.
      lr_editor ?= ls_function-r_function->get_editor( ).

      lr_editor->set_enabled( abap_true ).

    endloop.

  endmethod.


  method enable_hierarchy.

    r_table->set_display_type( if_salv_wd_c_table_settings=>display_type_hierarchy ).

    r_hierarchy->set_expanded( i_expanded ).

  endmethod.


  method get.

    create object er_table
      exporting
        ir_table = ir_table.

  endmethod.


  method get_by_usage.

    if ir_usage->has_active_component( ) eq abap_false.
      ir_usage->create_component( ).
    endif.

    data lr_controller type ref to iwci_salv_wd_table.
    lr_controller ?= ir_usage->get_interface_controller( ).

    er_table = get( lr_controller ).

  endmethod.


  method get_columns.

    data lt_columns type salv_wd_t_column_ref.
    lt_columns = r_columns->get_columns( ).

    data ls_column like line of lt_columns.
    loop at lt_columns into ls_column.
      insert ls_column-r_column->id into table et_columns.
    endloop.

  endmethod.


  method get_readonly.

    r_table->get_read_only( ).

  endmethod.


  method hide_column.

    data lr_column type ref to cl_salv_wd_column.
    lr_column = r_columns->get_column( iv_id ).

    if lr_column is bound.
      lr_column->set_visible( cl_wd_uielement=>e_visible-none ).
    endif.

  endmethod.


  method hide_columns.

    data lt_columns type salv_wd_t_column_ref.
    lt_columns = r_columns->get_columns( ).

    data ls_column like line of lt_columns.
    loop at lt_columns into ls_column.
      ls_column-r_column->set_visible( cl_wd_uielement=>e_visible-none ).
    endloop.

  endmethod.


  method hide_function.

    data lr_function type ref to cl_salv_wd_function.
    lr_function = r_u_func->get_function( iv_id ).
    if lr_function is bound.
      lr_function->set_visible( cl_wd_uielement=>e_visible-none ).
    endif.

  endmethod.


  method hide_functions.

    data lt_functions type salv_wd_t_function_ref.
    lt_functions = r_u_func->get_functions( ).

    data ls_function like line of lt_functions.
    loop at lt_functions into ls_function.
      ls_function-r_function->set_visible( cl_wd_uielement=>e_visible-none ).
    endloop.

  endmethod.


  method init.

    if iv_variant eq 1.

      " Table
      r_table->set_visible_row_count( 10 ).
      r_table->set_display_empty_rows( abap_false ).
      r_table->set_multi_column_sort( abap_true ).
      r_table->set_cell_action_event_enabled( abap_true ).
      r_table->set_data_check( if_salv_wd_c_table_settings=>data_check_on_cell_event ).
      "r_table->set_read_only( abap_true ).
      "r_table->set_width( '100%' ).

      " Functions
      r_s_func->set_view_list_allowed( abap_true ).
      r_s_func->set_export_allowed( abap_true ).
      r_s_func->set_pdf_allowed( abap_false ).

      r_s_func->set_sort_complex_allowed( abap_true ).
      r_s_func->set_filter_filterline_allowed( abap_true ).

      r_s_func->set_display_settings_allowed( abap_true ).
      r_s_func->set_dialog_settings_allowed( abap_true ).
      r_s_func->set_dialog_settings_as_popup( abap_true ).

      r_s_func->set_aggregation_allowed( abap_true ).
      r_s_func->set_group_aggregation_allowed( abap_true ).
      r_s_func->set_count_records_allowed( abap_true ).

      " Toolbar
      r_s_func->set_fixed_cols_left_allowed( abap_true ).
      r_s_func->set_fixed_cols_right_allowed( abap_true ).

      r_s_func->set_edit_check_available( abap_false ).
      r_s_func->set_edit_append_row_allowed( abap_false ).
      r_s_func->set_edit_insert_row_allowed( abap_false ).
      r_s_func->set_edit_delete_row_allowed( abap_false ).

      " Columns
      data ls_column like line of r_columns->t_columns.
      loop at r_columns->t_columns into ls_column.

        if ls_column-r_column->r_header is not initial.
          ls_column-r_column->r_header->set_header_text_wrapping( ).
        endif.


        try.
            data lr_cell_textview type ref to cl_salv_wd_uie_text_view.
            lr_cell_textview ?= ls_column-r_column->get_cell_editor( ).

            lr_cell_textview->set_wrapping( abap_true ).
          catch cx_sy_move_cast_error.
            " ...
        endtry.


        if ls_column-r_column->id cs 'GUID' or
           ls_column-r_column->id cs 'READONLY' or
           ls_column-r_column->id cs 'READ_ONLY' or
           ls_column-r_column->id cs '_RO_' or
           ls_column-r_column->id cs '_RD_' or
           ls_column-r_column->id cs '_XRO_' or
           ls_column-r_column->id cs 'VISIBLE' or
           ls_column-r_column->id cs 'COLOR' or
           ls_column-r_column->id cs 'TECH' or
           ls_column-r_column->id cs 'DUMMY'.

          hide_column( ls_column-r_column->id ).

        endif.

        if ls_column-r_column->id cs 'IMAGE_' or
           ls_column-r_column->id cs '_IMAGE' or
           ls_column-r_column->id cs 'ICON_'  or
           ls_column-r_column->id cs '_ICON'.

          set_column(
            iv_id    = ls_column-r_column->id
            iv_align = 'C' ).

          set_cell_image( ls_column-r_column->id ).

        endif.

        if ls_column-r_column->id cs 'LINK_' or
           ls_column-r_column->id cs '_LINK' or
           ls_column-r_column->id cs '_LNK'.

          set_column(
            iv_id    = ls_column-r_column->id
            iv_align = 'C' ).

          set_cell_link(
            iv_id       = ls_column-r_column->id
            iv_wrapping = abap_true ).

        endif.

      endloop.

    endif.

    if iv_variant eq 2.

      init( ).

      " Functions
      r_s_func->set_view_list_allowed( abap_false ).
      r_s_func->set_export_allowed( abap_false ).
      r_s_func->set_pdf_allowed( abap_false ).
      r_s_func->set_sort_complex_allowed( abap_false ).
      r_s_func->set_filter_filterline_allowed( abap_false ).
      r_s_func->set_display_settings_allowed( abap_false ).
      r_s_func->set_dialog_settings_allowed( abap_false ).
      r_s_func->set_dialog_settings_as_popup( abap_false ).

    endif.

  endmethod.


  method refresh.

    data ls_refresh type if_salv_wd_table=>s_type_param_refresh_in.
    ls_refresh-dummy = abap_true.

    r_wd_table->refresh( ls_refresh ).

  endmethod.


  method remove_choice.

    data lr_function type ref to cl_salv_wd_function.
    lr_function = r_u_func->get_function( iv_button ).

    data lr_button_choice type ref to cl_salv_wd_fe_button_choice.
    lr_button_choice ?= lr_function->get_editor( ).

    lr_button_choice->remove_choice(
      id = iv_id ).

  endmethod.


  method remove_choices.

    data l_button type string.
    l_button = iv_button.

    data lr_function type ref to cl_salv_wd_function.
    lr_function = r_u_func->get_function( l_button ).

    data lr_button_choice type ref to cl_salv_wd_fe_button_choice.
    lr_button_choice ?= lr_function->get_editor( ).

    data lt_choices type salv_wd_t_menu_action_item_ref.
    lt_choices = lr_button_choice->get_choices( ).

    data ls_choice like line of lt_choices.
    loop at lt_choices into ls_choice.

      lr_button_choice->remove_choice(
        id = ls_choice-id ).

    endloop.

  endmethod.


  method set_cell_checkbox.

    data lr_column type ref to cl_salv_wd_column.
    lr_column = r_columns->get_column( iv_id ).

    lr_column->set_h_align( cl_wd_table_column=>e_h_align-center ).

    data lr_checkbox type ref to cl_salv_wd_uie_checkbox.
    create object lr_checkbox
      exporting
        checked_fieldname = lr_column->id.

    if iv_readonly is supplied.
      if iv_readonly eq abap_true.
        lr_checkbox->set_read_only( abap_true ).
      elseif iv_readonly eq abap_false.
        lr_checkbox->set_read_only( abap_false ).
      else.
        lr_checkbox->set_read_only_fieldname( iv_readonly ).
      endif.
    endif.

    if iv_readonly_x is supplied.
      lr_checkbox->set_read_only( iv_readonly_x ).
    endif.

    lr_column->set_cell_editor( lr_checkbox ).

  endmethod.


  method set_cell_dropdown.

    data lr_column type ref to cl_salv_wd_column.
    lr_column = r_columns->get_column( iv_id ).

    if iv_type eq 'KEY'.

      data lr_ddk type ref to cl_salv_wd_uie_dropdown_by_key.
      create object lr_ddk
        exporting
          selected_key_fieldname = lr_column->id.

      if iv_readonly is supplied.
        if iv_readonly eq abap_true.
          lr_ddk->set_read_only( abap_true ).
        elseif iv_readonly eq abap_false.
          lr_ddk->set_read_only( abap_false ).
        else.
          lr_ddk->set_read_only_fieldname( iv_readonly ).
        endif.
      endif.

      if iv_oblig is supplied.

        data l_oblig.
        l_oblig = iv_oblig.

        if l_oblig eq abap_true.
          lr_ddk->set_state( cl_wd_abstract_input_field=>e_state-required ).
        else.
          lr_ddk->set_state( cl_wd_abstract_input_field=>e_state-normal ).
        endif.

      endif.

      lr_column->set_cell_editor( lr_ddk ).

    elseif iv_type eq 'INDEX'.

      data lr_ddi type ref to cl_salv_wd_uie_dropdown_by_idx.
      create object lr_ddi
        exporting
          selected_key_fieldname = lr_column->id.

      lr_ddi->set_valueset_fieldname( iv_valueset ).

      if iv_readonly is supplied.
        if iv_readonly eq abap_true.
          lr_ddi->set_read_only( abap_true ).
        elseif iv_readonly eq abap_false.
          lr_ddi->set_read_only( abap_false ).
        else.
          lr_ddi->set_read_only_fieldname( iv_readonly ).
        endif.
      endif.

      if iv_oblig is supplied.

        l_oblig = iv_oblig.

        if l_oblig eq abap_true.
          lr_ddi->set_state( cl_wd_abstract_input_field=>e_state-required ).
        else.
          lr_ddi->set_state( cl_wd_abstract_input_field=>e_state-normal ).
        endif.

      endif.

      lr_column->set_cell_editor( lr_ddi ).

    endif.

  endmethod.


  method set_cell_image.

    data lr_column type ref to cl_salv_wd_column.
    lr_column = r_columns->get_column( iv_id ).

    data lr_image type ref to cl_salv_wd_uie_image.
    create object lr_image.
    lr_image->set_source_fieldname( iv_id ).

    lr_column->set_cell_editor( lr_image ).

  endmethod.


  method set_cell_input.

    data l_id type string.
    l_id = iv_id.

    data lr_column type ref to cl_salv_wd_column.
    lr_column = r_columns->get_column( l_id ).

    data lr_input type ref to cl_salv_wd_uie_input_field.
    create object lr_input
      exporting
        value_fieldname = lr_column->id.

    if iv_enabled is supplied.

      data l_enebled type string.
      l_enebled = iv_enabled.

      if l_enebled eq abap_true.
        lr_input->set_enabled( abap_true ).
      elseif l_enebled eq abap_false.
        lr_input->set_enabled( abap_false ).
      else.
        lr_input->set_enabled_fieldname( l_enebled ).
      endif.

    endif.

    if iv_readonly is supplied.

      data l_readonly type string.
      l_readonly = iv_readonly.

      if l_readonly eq abap_true.
        lr_input->set_read_only( abap_true ).
      elseif l_readonly eq abap_false.
        lr_input->set_read_only( abap_false ).
      else.
        lr_input->set_read_only_fieldname( l_readonly ).
      endif.

    endif.

    if iv_value is supplied.

      data l_value type string.
      l_value = iv_value.

      lr_input->set_value_fieldname( l_value ).

    endif.

    if iv_color is supplied.

      data l_color type string.
      l_color = iv_color.

      lr_column->set_cell_design_fieldname( l_color ).

    endif.

    if iv_oblig is supplied.

      data l_oblig.
      l_oblig = iv_oblig.

      if l_oblig eq abap_true.
        lr_input->set_state( cl_wd_abstract_input_field=>e_state-required ).
      else.
        lr_input->set_state( cl_wd_abstract_input_field=>e_state-normal ).
      endif.

    endif.

    lr_column->set_cell_editor( lr_input ).

  endmethod.


  method set_cell_link.

    data lr_column type ref to cl_salv_wd_column.
    lr_column = r_columns->get_column( iv_id ).

    case iv_type.
      when 'ACTION'.

        data lr_link_to_action type ref to cl_salv_wd_uie_link_to_action.
        create object lr_link_to_action.

        lr_link_to_action->set_wrapping( abap_true ).

        lr_link_to_action->set_text_fieldname( lr_column->id ).

        if iv_enabled is supplied.
          if iv_enabled eq abap_true.
            lr_link_to_action->set_enabled( abap_true  ).
          elseif iv_enabled eq abap_false.
            lr_link_to_action->set_enabled( abap_false  ).
          else.
            lr_link_to_action->set_enabled_fieldname( iv_enabled ).
          endif.
        endif.

        if iv_enabled_x is supplied.
          lr_link_to_action->set_enabled( iv_enabled_x ).
        endif.

        if iv_image is not initial.

          data l_image_kind.
          l_image_kind = iv_image.

          data l_image type string.
          l_image = iv_image.

          if l_image_kind eq '~'.
            lr_link_to_action->set_image_source( l_image ).
          else.
            lr_link_to_action->set_image_source_fieldname( l_image ).
          endif.

        endif.

        if iv_wrapping is supplied.

          lr_link_to_action->set_wrapping( iv_wrapping ).

        endif.

        lr_column->set_cell_editor( lr_link_to_action ).

      when 'URL'.

        data lr_link_to_url type ref to cl_salv_wd_uie_link_to_url.
        create object lr_link_to_url.

        lr_link_to_url->set_text_fieldname( lr_column->id ).

        if iv_enabled is supplied.
          if iv_enabled eq abap_true.
            lr_link_to_url->set_enabled( abap_true  ).
          elseif iv_enabled eq abap_false.
            lr_link_to_url->set_enabled( abap_false  ).
          else.
            lr_link_to_url->set_enabled_fieldname( iv_enabled ).
          endif.
        endif.

        if iv_enabled_x is supplied.
          lr_link_to_url->set_enabled( iv_enabled_x ).
        endif.

        lr_column->set_cell_editor( lr_link_to_url ).

      when others.
        assert 1 = 2.
    endcase.

  endmethod.


  method set_cell_textview.

    data lr_column type ref to cl_salv_wd_column.
    lr_column = r_columns->get_column( iv_id ).

    if iv_align is not initial.

      case iv_align.
        when 'L'.
          data l_align type n length 2.
          l_align = cl_wd_text_view=>e_h_align-forced_left.
        when 'C'.
          l_align = cl_wd_text_view=>e_h_align-center.
        when 'R'.
          l_align = cl_wd_text_view=>e_h_align-forced_right.
        when others.
          l_align = cl_wd_text_view=>e_h_align-auto.
      endcase.

      lr_column->set_h_align( l_align ).

    endif.

    if iv_width is not initial.

      data l_width type string.
      l_width = iv_width.

      lr_column->set_width( l_width ).

    endif.

    data lr_text_view type ref to cl_salv_wd_uie_text_view.
    create object lr_text_view.

    lr_text_view->set_text_fieldname( iv_id ).

    lr_text_view->set_wrapping( iv_wrapping ).

    if iv_width is not initial.
      lr_text_view->set_width( l_width ).
    endif.

    lr_column->set_cell_editor( lr_text_view ).

  endmethod.


  method set_column.

    data l_id type string.
    l_id = iv_id.

    data lr_column type ref to cl_salv_wd_column.
    lr_column = r_columns->get_column( l_id ).
    if lr_column is not bound.
      return.
    endif.

    if iv_text is supplied.
      lr_column->r_header->set_text( iv_text ).
      lr_column->r_header->set_tooltip( iv_text ).
      lr_column->r_header->set_prop_ddic_binding_field( ).
    endif.

    if iv_fixed is supplied.
      lr_column->set_fixed_position( cl_wd_abstr_table_column=>e_fixed_position-left ).
    endif.

    if iv_position is supplied.
      lr_column->set_position( iv_position ).
    endif.

    if iv_visible is not initial.

    endif.

    if iv_align is not initial.

      data l_align like cl_wd_table_column=>e_h_align-auto.
      l_align = cl_wd_table_column=>e_h_align-auto.

      case iv_align.
        when 'L'.
          l_align = cl_wd_table_column=>e_h_align-forced_left.
        when 'C'.
          l_align = cl_wd_table_column=>e_h_align-center.
        when 'R'.
          l_align = cl_wd_table_column=>e_h_align-forced_right.
      endcase.

      lr_column->set_h_align( l_align ).

    endif.

    if iv_width is supplied.

      data l_width type string.
      l_width = iv_width.

      lr_column->set_width( l_width ).

    endif.

    if iv_hierarchy is supplied.
      lr_column->if_salv_wd_column_hierarchy~set_hierarchy_column( iv_hierarchy ).
    endif.

    if iv_color is supplied.
      if iv_color between '00' and '99'.

        data l_color(2) type n.
        l_color = iv_color.

        lr_column->set_cell_design( l_color ).

      else.
        lr_column->set_cell_design_fieldname( iv_color ).
      endif.
    endif.

    if iv_sum is supplied.
      if iv_sum eq abap_true.

        data lr_field type ref to cl_salv_wd_field.
        lr_field = r_fields->get_field( l_id ).

        lr_field->if_salv_wd_aggr~create_aggr_rule( ).

      endif.
    endif.

  endmethod.


  method set_column_readonly.

    data lr_column type ref to cl_salv_wd_column.
    lr_column = r_columns->get_column( i_id ).

    check lr_column is bound.

    data lr_editor type ref to cl_salv_wd_uie.
    lr_editor = lr_column->get_cell_editor( ).

    data l_readonly.
    l_readonly = i_readonly.

    case lr_editor->cid.
      when 'CL_SALV_WD_UIE_A_INPUT'.

        data lr_input_field type ref to cl_salv_wd_uie_input_field.
        lr_input_field ?= lr_editor.

        lr_input_field->set_read_only( l_readonly ).

      when 'CL_SALV_WD_UIE_CHECKBOX'.

        data lr_checkbox type ref to cl_salv_wd_uie_checkbox.
        lr_checkbox ?= lr_editor.

        lr_checkbox->set_read_only( l_readonly ).

      when 'CL_SALV_WD_UIE_A_DRDN_BY_KEY'.

        data lr_dropdown_by_key type ref to cl_salv_wd_uie_dropdown_by_key.
        lr_dropdown_by_key ?= lr_editor.

        lr_dropdown_by_key->set_read_only( l_readonly ).

    endcase.

  endmethod.


  method set_column_required.

    data lr_column type ref to cl_salv_wd_column.
    lr_column = r_columns->get_column( i_id ).

    check lr_column is bound.

    data lr_editor type ref to cl_salv_wd_uie.
    lr_editor = lr_column->get_cell_editor( ).

    case lr_editor->cid.
      when 'CL_SALV_WD_UIE_A_INPUT'.

        data lr_input_field type ref to cl_salv_wd_uie_input_field.
        lr_input_field ?= lr_editor.

        if i_required eq abap_true.
          lr_input_field->set_state( cl_wd_abstract_input_field=>e_state-required ).
        else.
          lr_input_field->set_state( cl_wd_abstract_input_field=>e_state-normal ).
        endif.

      when 'CL_SALV_WD_UIE_CHECKBOX'.

        data lr_checkbox type ref to cl_salv_wd_uie_checkbox.
        lr_checkbox ?= lr_editor.

        if i_required eq abap_true.
          lr_checkbox->set_state( cl_wd_abstract_input_field=>e_state-required ).
        else.
          lr_checkbox->set_state( cl_wd_abstract_input_field=>e_state-normal ).
        endif.

      when 'CL_SALV_WD_UIE_A_DRDN_BY_KEY'.

        data lr_dropdown_by_key type ref to cl_salv_wd_uie_dropdown_by_key.
        lr_dropdown_by_key ?= lr_editor.

        if i_required eq abap_true.
          lr_dropdown_by_key->set_state( cl_wd_abstract_input_field=>e_state-required ).
        else.
          lr_dropdown_by_key->set_state( cl_wd_abstract_input_field=>e_state-normal ).
        endif.

    endcase.

  endmethod.


  method set_display_mode.

    set_readonly( abap_true ).

  endmethod.


  method set_edit_mode.

    set_readonly( abap_false ).

  endmethod.


  method set_empty_table_text.

    data l_text type string.
    l_text = i_text.

    r_table->set_empty_table_text( l_text ).

  endmethod.


  method set_link.

    data l_id type string.
    l_id = iv_id.

    data lr_function type ref to cl_salv_wd_function.
    lr_function = r_u_func->get_function( l_id ).

    data lr_link type ref to cl_salv_wd_fe_link_to_action.
    lr_link ?= lr_function->get_editor( ).

    data l_text type string.
    l_text = iv_text.

    lr_link->set_text( l_text ).

  endmethod.


  method set_metadata.

    check it_metadata is not initial.

    data lt_columns type stringtab.
    lt_columns = get_columns( ).

    data l_column like line of lt_columns.
    loop at lt_columns into l_column.

      data ls_metadata like line of it_metadata.
      read table it_metadata into ls_metadata
        with key
          field = l_column.
      check sy-subrc eq 0.

      case ls_metadata-visible.
        when zcl_abap_static=>yes.
          show_column( l_column ).
        when zcl_abap_static=>no.
          hide_column( l_column ).
      endcase.

      case ls_metadata-editable.
        when zcl_abap_static=>yes.
          set_column_readonly(
            i_id       = l_column
            i_readonly = abap_false ).

        when zcl_abap_static=>no.
          set_column_readonly(
            i_id       = l_column
            i_readonly = abap_true ).

      endcase.

      case ls_metadata-required.
        when zcl_abap_static=>yes.
          set_column_required(
            i_id       = l_column
            i_required = abap_true ).

        when zcl_abap_static=>no.
          set_column_required(
            i_id       = l_column
            i_required = abap_false ).

      endcase.

    endloop.

  endmethod.


  method set_readonly.

    r_table->set_read_only( i_readonly ).

  endmethod.


  method set_rows.

    r_table->set_visible_row_count( i_rows ).

  endmethod.


  method set_title.

    data l_text type string.
    l_text = iv_text.

    r_table->r_header->set_text( l_text ).

  endmethod.


  method set_width.

    r_table->set_width( i_width ).

  endmethod.


  method show_column.

    data lr_column type ref to cl_salv_wd_column.
    lr_column = r_columns->get_column( iv_id ).

    if lr_column is bound.

      lr_column->set_visible( cl_wd_uielement=>e_visible-visible ).

      if iv_position is not initial.
        lr_column->set_position( iv_position ).
      endif.

    endif.

  endmethod.


  method show_function.

    data lr_function type ref to cl_salv_wd_function.
    lr_function = r_u_func->get_function( iv_id ).

    if lr_function is bound.
      lr_function->set_visible( cl_wd_uielement=>e_visible-visible ).
    endif.

  endmethod.


  method show_functions.

    data lt_functions type salv_wd_t_function_ref.
    lt_functions = r_u_func->get_functions( ).

    data ls_function like line of lt_functions.
    loop at lt_functions into ls_function.
      ls_function-r_function->set_visible( cl_wd_uielement=>e_visible-visible ).
    endloop.

  endmethod.


  method sort.

    data lr_field type ref to cl_salv_wd_field.
    lr_field = r_fields->get_field( iv_id ).

    lr_field->if_salv_wd_sort~create_sort_rule(
      sort_order        = iv_order
      sort_position     = iv_position
      group_aggregation = iv_sum ).

  endmethod.
ENDCLASS.