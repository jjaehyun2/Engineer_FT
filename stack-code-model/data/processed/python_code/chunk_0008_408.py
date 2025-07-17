class zcl_column_tree definition
  public
  final
  create public .

*"* public components of class ZCL_COLUMN_TREE
*"* do not include other source files here!!!
  public section.

    data type type string .
    data key_field type string .
    data r_container type ref to cl_gui_container .
    data r_tree type ref to cl_gui_column_tree .
    data t_nodes type treev_ntab .
    data t_items type gui_item .
    data current_node type treev_node .

    events double_click
      exporting
        value(i_key) type simple .
    events link_click
      exporting
        value(i_column) type simple
        value(i_key) type simple .
    events button_click
      exporting
        value(i_column) type simple
        value(i_key) type simple .

    class-methods create_column_tree
      importing
        !ir_parent     type ref to cl_gui_container optional
        !i_parent      type c optional
        !i_name        type simple default 'KEY'
        !i_text        type c default 'Key'
        !i_width       type i default '40'
      returning
        value(er_tree) type ref to zcl_column_tree
      raising
        zcx_generic .
    methods constructor
      importing
        !i_type    type c
        !ir_parent type ref to cl_gui_container optional
        !i_parent  type simple optional
        !i_name    type simple optional
        !i_text    type simple optional
        !i_width   type i optional
      raising
        zcx_generic .
    methods get_selected_node
      exporting
        !current_node    type treev_node
        !e_selected_node type lvc_nkey
        !e_fieldname     type lvc_fname
      raising
        zcx_generic .
    methods get_selected_item
      exporting
        !e_selected_node type tv_nodekey
        !e_fieldname     type tv_itmname
      raising
        zcx_generic .
    methods add_column
      importing
        !i_name  type simple
        !i_text  type simple
        !i_width type i default 60
      raising
        zcx_generic .
    methods add_node
      importing
        !i_name   type simple
        !i_parent type simple optional
        !i_type   type simple default cl_gui_list_tree=>relat_last_child
        !i_folder type abap_bool default abap_true
      raising
        zcx_generic .
    methods add_item
      importing
        !i_node   type simple
        !i_column type simple
        !i_class  type simple default cl_gui_list_tree=>item_class_text
        !i_font   type simple default cl_gui_list_tree=>item_font_prop
        !i_align  type simple default cl_gui_list_tree=>align_auto
        !i_value  type simple .
    methods applay
      raising
        zcx_generic .
    methods expand_all .
    methods close .
  protected section.
*"* protected components of class ZCL_COLUMN_TREE
*"* do not include other source files here!!!
  private section.
*"* private components of class ZCL_COLUMN_TREE
*"* do not include other source files here!!!

    methods on_link
          for event link_click of cl_item_tree_control
      importing
          !node_key
          !item_name .
    methods on_button
          for event button_click of cl_item_tree_control
      importing
          !node_key
          !item_name .
    methods on_double_click
          for event node_double_click of cl_item_tree_control
      importing
          !node_key .
ENDCLASS.



CLASS ZCL_COLUMN_TREE IMPLEMENTATION.


  method add_column.

    data l_name type tv_itmname.
    l_name = i_name.

    data l_text type tv_heading.
    l_text = i_text.

    if type eq 'COLUMN'.

      r_tree->add_column(
        exporting
          name                         = l_name
          width                        = i_width
          header_text                  = l_text
        exceptions
          column_exists                 = 1
          illegal_column_name           = 2
          too_many_columns              = 3
          illegal_alignment             = 4
          different_column_types        = 5
          cntl_system_error             = 6
          failed                        = 7
          predecessor_column_not_found  = 8 ).
      if sy-subrc ne 0.
        zcx_generic=>raise( ).
      endif.

    endif.

  endmethod.


  method add_item.

    data ls_item like line of t_items.
    ls_item-node_key         = i_node.
    ls_item-item_name        = i_column.
    ls_item-class            = i_class.
    ls_item-font             = i_font.
    ls_item-alignment        = i_align.
    ls_item-text             = i_value.
    insert ls_item into table t_items.

  endmethod.


  method add_node.

    data ls_node like line of t_nodes.
    ls_node-node_key         = i_name.
    ls_node-relatkey         = i_parent.
    ls_node-relatship        = i_type.
    ls_node-isfolder         = i_folder.
    insert ls_node into table t_nodes.

  endmethod.


  method applay.

    r_tree->add_nodes_and_items(
      exporting
        node_table                     = t_nodes
        item_table                     = t_items
        item_table_structure_name      = 'MTREEITM'
      exceptions
        failed                         = 1
        cntl_system_error              = 3
        error_in_tables                = 4
        dp_error                       = 5
        table_structure_name_not_found = 6 ).
    if sy-subrc ne 0.
      zcx_generic=>raise( ).
    endif.

  endmethod.


  method close.

    case type.
      when 'COLUMN'.
        r_tree->free( ).
    endcase.

    r_container->free( ).

  endmethod.


  method constructor.

    type      = i_type.
    key_field = i_name.

    if ir_parent is bound.
      r_container = ir_parent.
    else.
      data lr_container type ref to cl_gui_custom_container.
      create object lr_container
        exporting
          container_name = i_parent.
      r_container ?= lr_container.
    endif.

    data lt_events type cntl_simple_events.
    data ls_event like line of lt_events.
    ls_event-eventid    = cl_gui_list_tree=>eventid_item_double_click.
    ls_event-appl_event = abap_true.
    insert ls_event into table lt_events.

    ls_event-eventid    = cl_gui_list_tree=>eventid_link_click.
    ls_event-appl_event = abap_true.
    insert ls_event into table lt_events.

    ls_event-eventid    = cl_gui_list_tree=>eventid_button_click.
    ls_event-appl_event = abap_true.
    insert ls_event into table lt_events.

    case type.
      when 'SIMPLE'.
        " Íå ðåàëèîâàíî
      when 'LIST'.
        " Íå ðåàëèîâàíî
      when 'COLUMN'.

        data ls_hierarchy_header type treev_hhdr.
        ls_hierarchy_header-heading = i_text.
        ls_hierarchy_header-width   = i_width.

        data l_name type tv_itmname.
        l_name = i_name.

        " Ñîçäà¸ì îáúåêò äåðåâà
        create object r_tree
          exporting
            parent                      = r_container
            node_selection_mode         = cl_gui_list_tree=>node_sel_mode_single
            hide_selection              = abap_false
            item_selection              = abap_true
            hierarchy_column_name       = l_name
            hierarchy_header            = ls_hierarchy_header
          exceptions
            cntl_system_error           = 1
            create_error                = 2
            failed                      = 3
            illegal_node_selection_mode = 4
            lifetime_error              = 5
            others                      = 6.
        if sy-subrc ne 0.
          zcx_generic=>raise( ).
        endif.

        r_tree->set_registered_events(
          exporting
            events                    = lt_events
          exceptions
            cntl_error                = 1
            cntl_system_error         = 2
            illegal_event_combination = 3 ).
        if sy-subrc ne 0.
          zcx_generic=>raise( ).
        endif.

        set handler on_link   for r_tree.
        set handler on_button for r_tree.

    endcase.

  endmethod.


  method create_column_tree.

    create object er_tree
      exporting
        i_type    = 'COLUMN'
        ir_parent = ir_parent
        i_parent  = i_parent
        i_name    = i_name
        i_text    = i_text
        i_width   = i_width.

  endmethod.


  method expand_all.

    case type.
      when 'COLUMN'.
        r_tree->expand_root_nodes(
          level_count    = 9
          expand_subtree = abap_true ).
    endcase.

  endmethod.


  method get_selected_item.

    r_tree->get_selected_item(
      importing
        node_key          = e_selected_node
        item_name         = e_fieldname
      exceptions
        failed            = 1
        cntl_system_error = 2
        no_item_selection = 3
        others            = 4 ).
    if sy-subrc <> 0.
      zcx_generic=>raise( ).
    endif.

  endmethod.


  method get_selected_node.

    r_tree->get_selected_node(
      importing
        node_key                   = current_node-node_key
      exceptions
        failed                     = 1
        single_node_selection_only = 2
        cntl_system_error          = 3
        others                     = 4 ).
    if sy-subrc <> 0.
      zcx_generic=>raise( ).
    endif.

  endmethod.


  method on_button.

    raise event link_click
      exporting
        i_column = item_name
        i_key    = node_key.

  endmethod.


  method on_double_click.

    raise event double_click
      exporting
        i_key    = node_key.

  endmethod.


  method on_link.

    raise event link_click
      exporting
        i_column = item_name
        i_key    = node_key.

  endmethod.
ENDCLASS.