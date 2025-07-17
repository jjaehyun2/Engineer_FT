class zcl_markdown_docu_clas definition public
  inheriting from zcl_markdown_data.

  public section.
    types:
      begin of t_attribute,
        name         type string,
        type_kind    type string,
        visibility   type string,
        is_inherited type string,
        is_class     type string,
        is_read_only type string,
      end of t_attribute,
      t_attributes type standard table of t_attribute with empty key.

    methods constructor
      importing class_name type seoclsname
                document   type ref to zif_zmd_document.

  private section.
    data: descr type ref to cl_abap_classdescr.
    methods attributes.

endclass.



class zcl_markdown_docu_clas implementation.

  method constructor.

    super->constructor( document ).
    descr = cast #( cl_abap_classdescr=>describe_by_name( class_name ) ).

    doc->heading( level = 1 val = to_lower( descr->get_relative_name( ) ) ).

    doc->______________________________( ).

    if descr->interfaces is not initial.
      doc->heading( level = 2 val = `Interfaces` ).
      data_table( data = descr->interfaces auto_header_row = abap_false ).
    endif.

    doc->______________________________( ).

    if descr->types is not initial.
      doc->heading( level = 2 val = `Types` ).
      data_table( data = descr->types auto_header_row = abap_false ).
    endif.

    doc->______________________________( ).

    if descr->methods is not initial.
      doc->heading( level = 2 val = `Methods` ).
      loop at descr->methods assigning field-symbol(<method>).
        data_table( data = descr->types auto_header_row = abap_false ).
      endloop.
    endif.

    attributes( ).

  endmethod.

  method attributes.

    if descr->attributes is not initial.
      doc->heading( level = 2 val = `Attributes` ).

      data: attributes type t_attributes.
      loop at descr->attributes assigning field-symbol(<attr>)
        where is_constant = abap_true. " constants
        append value #(
          name = <attr>-name
          type_kind = <attr>-type_kind
          visibility = <attr>-visibility
          is_inherited = <attr>-is_inherited
          is_class = <attr>-is_class
          is_read_only = <attr>-is_class
        ) to attributes.
      endloop.

      if attributes is not initial.
        doc->heading( level = 3 val = 'Constants' ).
        data_table( attributes ).
        clear attributes.
      endif.

      loop at descr->attributes assigning <attr>
        where is_class = abap_true and is_constant = abap_false.
        append value #(
          name = <attr>-name
          type_kind = <attr>-type_kind
          visibility = <attr>-visibility
          is_inherited = <attr>-is_inherited
          is_read_only = <attr>-is_class
        ) to attributes.

      endloop.

      if attributes is not initial.
        doc->heading( level = 3 val = 'Class Attributes' ).
        data_table( attributes ).
        clear attributes.
      endif.

      loop at descr->attributes assigning <attr>
        where is_class = abap_false and is_constant = abap_false.
        append value #(
          name = <attr>-name
          type_kind = <attr>-type_kind
          visibility = <attr>-visibility
          is_inherited = <attr>-is_inherited
          is_read_only = <attr>-is_class
        ) to attributes.

      endloop.

      if attributes is not initial.
        doc->heading( level = 3 val = 'Member Attributes' ).
        data_table( attributes ).
        clear attributes.
      endif.

    endif.

  endmethod.

endclass.