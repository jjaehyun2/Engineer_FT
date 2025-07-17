class zcl_tools_comp_itabs definition
  public
  final
  create public .

  public section.
    interfaces zif_tools_comp_itabs.

    methods compare_itabs
      importing
        iv_tablename type string
        itab_old     type any
        itab_new     type any.

    methods add_changes_by
      importing
        iv_tablename type string
        wa_new       type any
        wa_old       type any
        tabix        type sy-tabix default 1.

    methods add_changes
      importing
        changed_fields type zif_tools_comp_itabs~ty_changed_data.

    methods return_changes
      returning value(rt_values) type zif_tools_comp_itabs~tt_changed_data.

  protected section.
  private section.
    data mt_changes type zif_tools_comp_itabs~tt_changed_data.
endclass.



class zcl_tools_comp_itabs implementation.

  method compare_itabs.
    data(o_type_desc) = cl_abap_typedescr=>describe_by_data( itab_old ).

    case o_type_desc->kind.
      when cl_abap_typedescr=>kind_struct.
        add_changes_by(
          exporting
            iv_tablename = iv_tablename
            wa_new       = itab_new
            wa_old       = itab_old
        ).
      when cl_abap_typedescr=>kind_table.
        data r_itab_old type ref to data.
        data r_itab_new type ref to data.
        field-symbols <fs_itab_old> type standard table.
        field-symbols <fs_itab_new> type standard table.

        r_itab_old = ref #( itab_old ).
        r_itab_new = ref #( itab_new ).

        assign r_itab_old->* to <fs_itab_old>.
        assign r_itab_new->* to <fs_itab_new>.

        check lines( <fs_itab_old> ) = lines( <fs_itab_new> ).

        loop at <fs_itab_old> assigning field-symbol(<row_old>).
          read table <fs_itab_new> index sy-tabix assigning field-symbol(<row_new>).
          add_changes_by(
            exporting
              iv_tablename = iv_tablename
              wa_new       = <row_new>
              wa_old       = <row_old>
              tabix        = sy-tabix
          ).
        endloop.
    endcase.
  endmethod.

  method add_changes.
    append changed_fields to mt_changes.
  endmethod.


  method add_changes_by.
    field-symbols: <fs_row_new> type any.
    field-symbols: <fs_row_old> type any.

    assign wa_new to <fs_row_new>.
    assign wa_old to <fs_row_old>.

    assign wa_new to <fs_row_new>.
    assign wa_old to <fs_row_old>.
    check <fs_row_new> is assigned.
    check <fs_row_old> is assigned.

    data go_struct type ref to cl_abap_structdescr.
    go_struct ?= cl_abap_typedescr=>describe_by_data( <fs_row_new> ).

    loop at go_struct->components[] assigning field-symbol(<fs_col>).
      assign component <fs_col>-name of structure <fs_row_new> to field-symbol(<fs_cell_new>).
      assign component <fs_col>-name of structure <fs_row_old> to field-symbol(<fs_cell_old>).
      if sy-subrc = 0 and <fs_cell_new> <> <fs_cell_old>.
        append value #(
          table_name = iv_tablename
          field_name = <fs_col>-name
          tabix      = tabix
          value_old  = conv string( <fs_cell_old> )
          value_new  = conv string( <fs_cell_new> )
          ) to mt_changes.
      endif.
    endloop.

  endmethod.

  method return_changes.
    rt_values = mt_changes.
  endmethod.

endclass.