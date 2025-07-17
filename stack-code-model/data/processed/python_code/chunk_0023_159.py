**********************************************************************
* UTILS
**********************************************************************

class lcl_utils definition final.
  public section.

    class-methods normalize_path
      importing
        iv_path type string
      returning
        value(rv_path) type string.
    class-methods split_path
      importing
        iv_path type string
      returning
        value(rv_path_name) type zif_ajson=>ty_path_name.
    class-methods validate_array_index
      importing
        iv_path type string
        iv_index type string
      returning
        value(rv_index) type i
      raising
        zcx_ajson_error.

endclass.

class lcl_utils implementation.

  method validate_array_index.

    if not iv_index co '0123456789'.
      zcx_ajson_error=>raise( |Cannot add non-numeric key [{ iv_index }] to array [{ iv_path }]| ).
    endif.
    rv_index = iv_index.
    if rv_index = 0.
      zcx_ajson_error=>raise( |Cannot add zero key to array [{ iv_path }]| ).
    endif.

  endmethod.

  method normalize_path.

    rv_path = iv_path.
    if strlen( rv_path ) = 0.
      rv_path = '/'.
    endif.
    if rv_path+0(1) <> '/'.
      rv_path = '/' && rv_path.
    endif.
    if substring( val = rv_path off = strlen( rv_path ) - 1 ) <> '/'.
      rv_path = rv_path && '/'.
    endif.

  endmethod.

  method split_path.

    data lv_offs type i.
    data lv_len type i.
    data lv_trim_slash type i.

    lv_len = strlen( iv_path ).
    if lv_len = 0 or iv_path = '/'.
      return. " empty path is the alias for root item = '' + ''
    endif.

    if substring( val = iv_path off = lv_len - 1 ) = '/'.
      lv_trim_slash = 1. " ignore last '/'
    endif.

    lv_offs = find( val = reverse( iv_path ) sub = '/' off = lv_trim_slash ).
    if lv_offs = -1.
      lv_offs  = lv_len. " treat whole string as the 'name' part
    endif.
    lv_offs = lv_len - lv_offs.

    rv_path_name-path = normalize_path( substring( val = iv_path len = lv_offs ) ).
    rv_path_name-name = substring( val = iv_path off = lv_offs len = lv_len - lv_offs - lv_trim_slash ).

  endmethod.

endclass.


**********************************************************************
* PARSER
**********************************************************************

class lcl_json_parser definition final.
  public section.

    methods parse
      importing
        iv_json type string
      returning
        value(rt_json_tree) type zif_ajson=>ty_nodes_tt
      raising
        zcx_ajson_error.

  private section.

    types:
      ty_stack_tt type standard table of ref to zif_ajson=>ty_node.

    data mt_stack type ty_stack_tt.

    class-methods join_path
      importing
        it_stack type ty_stack_tt
      returning
        value(rv_path) type string.

    methods raise
      importing
        iv_error type string
      raising
        zcx_ajson_error.

    methods _parse
      importing
        iv_json type string
      returning
        value(rt_json_tree) type zif_ajson=>ty_nodes_tt
      raising
        zcx_ajson_error cx_sxml_error.

    methods _get_location
      importing
        iv_json            type string
        iv_offset          type i
      returning
        value(rv_location) type string.

endclass.

class lcl_json_parser implementation.

  method parse.
    data lx_sxml_parse type ref to cx_sxml_parse_error.
    data lx_sxml type ref to cx_sxml_error.
    data lv_location type string.
    try.
      rt_json_tree = _parse( iv_json ).
    catch cx_sxml_parse_error into lx_sxml_parse.
      lv_location = _get_location(
        iv_json   = iv_json
        iv_offset = lx_sxml_parse->xml_offset ).
      zcx_ajson_error=>raise(
        iv_msg      = |Json parsing error (SXML): { lx_sxml_parse->get_text( ) }|
        iv_location = lv_location ).
    catch cx_sxml_error into lx_sxml.
      zcx_ajson_error=>raise(
        iv_msg      = |Json parsing error (SXML): { lx_sxml->get_text( ) }|
        iv_location = '@PARSER' ).
    endtry.
  endmethod.

  method _get_location.

    data lv_json type string.
    data lv_offset type i.
    data lt_text type table of string.
    data lv_text type string.
    data lv_line type i.
    data lv_pos type i.

    lv_offset = iv_offset.
    if lv_offset < 0.
      lv_offset = 0.
    endif.
    if lv_offset > strlen( iv_json ).
      lv_offset = strlen( iv_json ).
    endif.

    lv_json = iv_json(lv_offset).

    replace all occurrences of cl_abap_char_utilities=>cr_lf
      in lv_json with cl_abap_char_utilities=>newline.

    split lv_json at cl_abap_char_utilities=>newline into table lt_text.

    lv_line = lines( lt_text ).
    if lv_line = 0.
      lv_line = 1.
      lv_pos = 1.
    else.
      read table lt_text index lv_line into lv_text.
      lv_pos = strlen( lv_text ) + 1.
    endif.

    rv_location = |Line { lv_line }, Offset { lv_pos }|.

  endmethod.

  method _parse.

    data lo_reader type ref to if_sxml_reader.
    data lr_stack_top like line of mt_stack.
    data lo_node type ref to if_sxml_node.
    field-symbols <item> like line of rt_json_tree.

    clear mt_stack.
    if iv_json is initial.
      return.
    endif.
    lo_reader = cl_sxml_string_reader=>create( cl_abap_codepage=>convert_to( iv_json ) ).

    " TODO: self protection, check non-empty, check starting from object ...

    do.
      lo_node = lo_reader->read_next_node( ).
      if lo_node is not bound.
        exit.
      endif.


      case lo_node->type.
        when if_sxml_node=>co_nt_element_open.
          data lt_attributes type if_sxml_attribute=>attributes.
          data lo_attr like line of lt_attributes.
          data lo_open type ref to if_sxml_open_element.
          lo_open ?= lo_node.

          append initial line to rt_json_tree assigning <item>.

          <item>-type = to_lower( lo_open->qname-name ).

          read table mt_stack index 1 into lr_stack_top.
          if sy-subrc = 0.
            <item>-path = join_path( mt_stack ).
            lr_stack_top->children = lr_stack_top->children + 1.

            if lr_stack_top->type = 'array'.
              <item>-name = |{ lr_stack_top->children }|.
              <item>-index = lr_stack_top->children.
            else.
              lt_attributes = lo_open->get_attributes( ).
              loop at lt_attributes into lo_attr.
                if lo_attr->qname-name = 'name' and lo_attr->value_type = if_sxml_value=>co_vt_text.
                  <item>-name = lo_attr->get_value( ).
                endif.
              endloop.
            endif.
          endif.

          get reference of <item> into lr_stack_top.
          insert lr_stack_top into mt_stack index 1.

        when if_sxml_node=>co_nt_element_close.
          data lo_close type ref to if_sxml_close_element.
          lo_close ?= lo_node.

          read table mt_stack index 1 into lr_stack_top.
          delete mt_stack index 1.
          if lo_close->qname-name <> lr_stack_top->type.
            raise( 'Unexpected closing node type' ).
          endif.

        when if_sxml_node=>co_nt_value.
          data lo_value type ref to if_sxml_value_node.
          lo_value ?= lo_node.

          <item>-value = lo_value->get_value( ).

        when others.
          raise( 'Unexpected node type' ).
      endcase.
    enddo.

    if lines( mt_stack ) > 0.
      raise( 'Unexpected end of data' ).
    endif.

  endmethod.

  method join_path.

    field-symbols <ref> like line of it_stack.

    loop at it_stack assigning <ref>.
      rv_path = <ref>->name && '/' && rv_path.
    endloop.

  endmethod.

  method raise.

    zcx_ajson_error=>raise(
      iv_location = join_path( mt_stack )
      iv_msg      = |JSON PARSER: { iv_error } @ { join_path( mt_stack ) }| ).

  endmethod.

endclass.

**********************************************************************
* SERIALIZER
**********************************************************************

class lcl_json_serializer definition final create private.
  public section.

    class-methods stringify
      importing
        it_json_tree type zif_ajson=>ty_nodes_ts
        iv_indent type i default 0
        iv_keep_item_order type abap_bool default abap_false
      returning
        value(rv_json_string) type string
      raising
        zcx_ajson_error.

    class-methods class_constructor.

  private section.

    class-data gv_comma_with_lf type string.

    data mt_json_tree type zif_ajson=>ty_nodes_ts.
    data mv_keep_item_order type abap_bool.
    data mt_buffer type string_table.
    data mv_indent_step type i.
    data mv_level type i.

    class-methods escape
      importing
        iv_unescaped type string
      returning
        value(rv_escaped) type string.

    methods _stringify
      returning
        value(rv_json_string) type string
      raising
        zcx_ajson_error.

    methods stringify_node
      importing
        is_node type zif_ajson=>ty_node
      raising
        zcx_ajson_error.

    methods stringify_set
      importing
        iv_parent_path type string
        iv_array type abap_bool
      raising
        zcx_ajson_error.

endclass.

class lcl_json_serializer implementation.

  method class_constructor.
    gv_comma_with_lf = ',' && cl_abap_char_utilities=>newline.
  endmethod.

  method stringify.

    data lo type ref to lcl_json_serializer.
    create object lo.
    lo->mt_json_tree = it_json_tree.
    lo->mv_indent_step = iv_indent.
    lo->mv_keep_item_order = iv_keep_item_order.
    rv_json_string = lo->_stringify( ).

  endmethod.

  method _stringify.

    field-symbols <n> like line of mt_json_tree.
    read table mt_json_tree assigning <n>
      with key
        path = ''
        name = ''. " Root
    if sy-subrc <> 0.
      return.
    endif.

    stringify_node( <n> ).

    rv_json_string = concat_lines_of( table = mt_buffer ).

  endmethod.

  method stringify_node.

    data lv_item type string.
    data lv_indent_prefix type string.

    if mv_indent_step > 0.
      lv_indent_prefix = repeat( val = ` ` occ = mv_indent_step * mv_level ).
      lv_item = lv_indent_prefix.
    endif.

    if is_node-name is not initial and is_node-index is initial. " Not root, not array item
      if mv_indent_step > 0.
        lv_item = lv_item && |"{ is_node-name }": |.
      else.
        lv_item = |"{ is_node-name }":|.
      endif.
    endif.

    case is_node-type.
      when zif_ajson=>node_type-array.
        lv_item = lv_item && '['.
      when zif_ajson=>node_type-object.
        lv_item = lv_item && '{'.
      when zif_ajson=>node_type-string.
        lv_item = lv_item && |"{ escape( is_node-value ) }"|.
      when zif_ajson=>node_type-boolean or zif_ajson=>node_type-number.
        lv_item = lv_item && is_node-value.
      when zif_ajson=>node_type-null.
        lv_item = lv_item && 'null'.
      when others.
        zcx_ajson_error=>raise(
          iv_msg = |Unexpected type [{ is_node-type }]|
          iv_location = is_node-path && is_node-name ).
    endcase.

    if mv_indent_step > 0
      and ( is_node-type = zif_ajson=>node_type-array or is_node-type = zif_ajson=>node_type-object )
      and is_node-children > 0.
      mv_level = mv_level + 1.
      lv_item = lv_item && cl_abap_char_utilities=>newline.
    endif.

    append lv_item to mt_buffer.

    " finish complex item

    if is_node-type = zif_ajson=>node_type-array or is_node-type = zif_ajson=>node_type-object.
      data lv_children_path type string.
      data lv_tail type string.

      lv_children_path = is_node-path && is_node-name && '/'. " for root: path = '' and name = '', so result is '/'

      case is_node-type.
        when zif_ajson=>node_type-array.
          if is_node-children > 0.
            stringify_set(
              iv_parent_path = lv_children_path
              iv_array       = abap_true ).
          endif.
          lv_tail = ']'.
        when zif_ajson=>node_type-object.
          if is_node-children > 0.
            stringify_set(
              iv_parent_path = lv_children_path
              iv_array       = abap_false ).
          endif.
          lv_tail = '}'.
      endcase.

      if mv_indent_step > 0 and is_node-children > 0.
        lv_tail = lv_indent_prefix && lv_tail.
        mv_level = mv_level - 1.
      endif.
      append lv_tail to mt_buffer.
    endif.

  endmethod.

  method stringify_set.

    data lv_tab_key type string.
    data lv_first_done type abap_bool.
    field-symbols <n> like line of mt_json_tree.

    if iv_array = abap_true.
      lv_tab_key = 'array_index'. " path + index
    elseif mv_keep_item_order = abap_true.
      lv_tab_key = 'item_order'. " path + order
    else.
      lv_tab_key = 'primary_key'. " path + name
    endif.

    loop at mt_json_tree assigning <n> using key (lv_tab_key) where path = iv_parent_path.
      if lv_first_done = abap_false.
        lv_first_done = abap_true.
      elseif mv_indent_step > 0.
        append gv_comma_with_lf to mt_buffer.
      else.
        append ',' to mt_buffer.
      endif.
      stringify_node( <n> ).
    endloop.

    if mv_indent_step > 0 and lv_first_done = abap_true. " only of items were in the list
      append cl_abap_char_utilities=>newline to mt_buffer.
    endif.

  endmethod.

  method escape.

    rv_escaped = iv_unescaped.
    if rv_escaped ca |"\\\t\n\r|.
      " TODO consider performance ...
      " see also https://www.json.org/json-en.html
      rv_escaped = replace(
        val = rv_escaped
        sub = '\'
        with = '\\'
        occ = 0 ).
      rv_escaped = replace(
        val = rv_escaped
        sub = |\n|
        with = '\n'
        occ = 0 ).
      rv_escaped = replace(
        val = rv_escaped
        sub = |\r|
        with = '\r'
        occ = 0 ).
      rv_escaped = replace(
        val = rv_escaped
        sub = |\t|
        with = '\t'
        occ = 0 ).
      rv_escaped = replace(
        val = rv_escaped
        sub = '"'
        with = '\"'
        occ = 0 ).

    endif.

  endmethod.

endclass.


**********************************************************************
* JSON_TO_ABAP
**********************************************************************

class lcl_json_to_abap definition final.
  public section.

    methods find_loc
      importing
        iv_path type string
        iv_name type string optional " not mandatory
        iv_append_tables type abap_bool default abap_false
      returning
        value(r_ref) type ref to data
      raising
        zcx_ajson_error.

    class-methods bind
      importing
        !ii_custom_mapping type ref to zif_ajson_mapping optional
      changing
        c_obj              type any
        co_instance        type ref to lcl_json_to_abap.

    methods to_abap
      importing
        it_nodes type zif_ajson=>ty_nodes_ts
      raising
        zcx_ajson_error.

    methods to_timestamp
      importing
        is_path          type zif_ajson=>ty_node
      returning
        value(rv_result) type timestamp
      raising
        zcx_ajson_error.

  private section.
    data mr_obj type ref to data.
    data mi_custom_mapping type ref to zif_ajson_mapping.

endclass.

class lcl_json_to_abap implementation.

  method bind.
    create object co_instance.
    get reference of c_obj into co_instance->mr_obj.
    co_instance->mi_custom_mapping = ii_custom_mapping.
  endmethod.

  method to_abap.

    data lr_ref type ref to data.
    data lv_type type c.
    data lx type ref to cx_root.
    field-symbols <n> like line of it_nodes.
    field-symbols <value> type any.

    try.
      loop at it_nodes assigning <n> using key array_index.
        lr_ref = find_loc(
          iv_append_tables = abap_true
          iv_path = <n>-path
          iv_name = <n>-name ).
        assign lr_ref->* to <value>.
        assert sy-subrc = 0.
        describe field <value> type lv_type.

        case <n>-type.
          when zif_ajson=>node_type-null.
            " Do nothing
          when zif_ajson=>node_type-boolean.
            <value> = boolc( <n>-value = 'true' ).
          when zif_ajson=>node_type-number.
            <value> = <n>-value.
          when zif_ajson=>node_type-string.
            if lv_type = 'D' and <n>-value is not initial.
              data lv_y type c length 4.
              data lv_m type c length 2.
              data lv_d type c length 2.

              find first occurrence of regex '^(\d{4})-(\d{2})-(\d{2})(T|$)' "#EC NOTEXT
                in <n>-value
                submatches lv_y lv_m lv_d.
              if sy-subrc <> 0.
                zcx_ajson_error=>raise(
                  iv_msg      = 'Unexpected date format'
                  iv_location = <n>-path && <n>-name ).
              endif.
              concatenate lv_y lv_m lv_d into <value>.
            elseif lv_type = 'P' and <n>-value is not initial.
              <value> = to_timestamp( is_path = <n> ).
            else.
              <value> = <n>-value.
            endif.
          when zif_ajson=>node_type-object.
            if not lv_type co 'uv'.
              zcx_ajson_error=>raise(
                iv_msg      = 'Expected structure'
                iv_location = <n>-path && <n>-name ).
            endif.
          when zif_ajson=>node_type-array.
            if not lv_type co 'h'.
              zcx_ajson_error=>raise(
                iv_msg      = 'Expected table'
                iv_location = <n>-path && <n>-name ).
            endif.
          when others.
            zcx_ajson_error=>raise(
              iv_msg      = |Unexpected JSON type [{ <n>-type }]|
              iv_location = <n>-path && <n>-name ).
        endcase.

      endloop.
    catch cx_sy_conversion_no_number into lx.
      zcx_ajson_error=>raise(
        iv_msg      = |Source is not a number|
        iv_location = <n>-path && <n>-name ).
    endtry.

  endmethod.

  method find_loc.

    data lt_path type string_table.
    data lv_trace type string.
    data lv_seg like line of lt_path.
    data lv_type type c.
    data lv_size type i.
    data lv_index type i.
    field-symbols <struc> type any.
    field-symbols <table> type standard table.
    field-symbols <value> type any.
    field-symbols <seg> like line of lt_path.

    split iv_path at '/' into table lt_path.
    delete lt_path where table_line is initial.
    if iv_name is not initial.
      append iv_name to lt_path.
    endif.

    r_ref = mr_obj.

    loop at lt_path assigning <seg>.
      lv_trace = lv_trace && '/' && <seg>.

      if mi_custom_mapping is bound.
        lv_seg = mi_custom_mapping->to_abap( iv_path = iv_path iv_name = <seg> ).
      else.
        clear lv_seg.
      endif.

      if lv_seg is initial.
        lv_seg = to_upper( <seg> ).
      else.
        lv_seg = to_upper( lv_seg ).
      endif.

      assign r_ref->* to <struc>.
      assert sy-subrc = 0.
      describe field <struc> type lv_type.

      if lv_type ca 'lr'. " data/obj ref
        " TODO maybe in future
        zcx_ajson_error=>raise(
          iv_msg      = 'Cannot assign to ref'
          iv_location = lv_trace ).

      elseif lv_type = 'h'. " table
        if not lv_seg co '0123456789'.
          zcx_ajson_error=>raise(
            iv_msg      = 'Need index to access tables'
            iv_location = lv_trace ).
        endif.
        lv_index = lv_seg.
        assign r_ref->* to <table>.
        assert sy-subrc = 0.

        lv_size = lines( <table> ).
        if iv_append_tables = abap_true and lv_index = lv_size + 1.
          append initial line to <table>.
        endif.

        read table <table> index lv_index assigning <value>.
        if sy-subrc <> 0.
          zcx_ajson_error=>raise(
            iv_msg      = 'Index not found in table'
            iv_location = lv_trace ).
        endif.

      elseif lv_type ca 'uv'. " structure
        assign component lv_seg of structure <struc> to <value>.
        if sy-subrc <> 0.
          zcx_ajson_error=>raise(
            iv_msg      = 'Path not found'
            iv_location = lv_trace ).
        endif.
      else.
        zcx_ajson_error=>raise(
          iv_msg = 'Target is not deep'
          iv_location = lv_trace ).
      endif.
      get reference of <value> into r_ref.
    endloop.

  endmethod.

  method to_timestamp.

    constants lc_utc type c length 6 value 'UTC'.
    constants lc_regex_ts_with_hour type string
      value `^(\d{4})-(\d{2})-(\d{2})(T)(\d{2}):(\d{2}):(\d{2})(\+)(\d{2}):(\d{2})`. "#EC NOTEXT
    constants lc_regex_ts_utc type string
      value `^(\d{4})-(\d{2})-(\d{2})(T)(\d{2}):(\d{2}):(\d{2})(Z|$)`. "#EC NOTEXT

    data:
      begin of ls_timestamp,
        year         type c length 4,
        month        type c length 2,
        day          type c length 2,
        t            type c length 1,
        hour         type c length 2,
        minute       type c length 2,
        second       type c length 2,
        local_sign   type c length 1,
        local_hour   type c length 2,
        local_minute type c length 2,
      end of ls_timestamp.

    data lv_date type d.
    data lv_time type t.
    data lv_seconds_conv type i.
    data lv_timestamp type timestampl.

    find first occurrence of regex lc_regex_ts_with_hour
      in is_path-value submatches ls_timestamp-year ls_timestamp-month ls_timestamp-day ls_timestamp-t
                                  ls_timestamp-hour ls_timestamp-minute ls_timestamp-second
                                  ls_timestamp-local_sign ls_timestamp-local_hour ls_timestamp-local_minute.

    if sy-subrc = 0.

      lv_seconds_conv = ( ls_timestamp-local_hour * 3600 ) + ( ls_timestamp-local_minute * 60 ).

    else.

      find first occurrence of regex lc_regex_ts_utc
        in is_path-value submatches ls_timestamp-year ls_timestamp-month ls_timestamp-day ls_timestamp-t
                                    ls_timestamp-hour ls_timestamp-minute ls_timestamp-second.

      if sy-subrc <> 0.
        zcx_ajson_error=>raise(
          iv_msg      = 'Unexpected timestamp format'
          iv_location = is_path-path && is_path-name ).
      endif.

    endif.

    concatenate ls_timestamp-year ls_timestamp-month ls_timestamp-day into lv_date.
    concatenate ls_timestamp-hour ls_timestamp-minute ls_timestamp-second into lv_time.

    convert date lv_date time lv_time into time stamp lv_timestamp time zone lc_utc.

    try.

      case ls_timestamp-local_sign.
        when '-'.
          lv_timestamp = cl_abap_tstmp=>add( tstmp = lv_timestamp secs = lv_seconds_conv ).
        when '+'.
          lv_timestamp = cl_abap_tstmp=>subtractsecs( tstmp = lv_timestamp secs = lv_seconds_conv ).
      endcase.

    catch cx_parameter_invalid_range cx_parameter_invalid_type.
      zcx_ajson_error=>raise(
        iv_msg      = 'Unexpected error calculating timestamp'
        iv_location = is_path-path && is_path-name ).
    endtry.

    cl_abap_tstmp=>move( exporting tstmp_src = lv_timestamp
                         importing tstmp_tgt = rv_result ).

  endmethod.

endclass.

**********************************************************************
* ABAP_TO_JSON
**********************************************************************

class lcl_abap_to_json definition final.
  public section.

    class-methods convert
      importing
        iv_data            type any
        is_prefix          type zif_ajson=>ty_path_name optional
        iv_array_index     type i default 0
        ii_custom_mapping  type ref to zif_ajson_mapping optional
        iv_keep_item_order type abap_bool default abap_false
      returning
        value(rt_nodes)   type zif_ajson=>ty_nodes_tt
      raising
        zcx_ajson_error.

    class-methods insert_with_type
      importing
        iv_data            type any
        iv_type            type string
        is_prefix          type zif_ajson=>ty_path_name optional
        iv_array_index     type i default 0
        ii_custom_mapping  type ref to zif_ajson_mapping optional
        iv_keep_item_order type abap_bool default abap_false
      returning
        value(rt_nodes)   type zif_ajson=>ty_nodes_tt
      raising
        zcx_ajson_error.

    class-methods class_constructor.

  private section.

    class-data gv_ajson_absolute_type_name type string.
    data mi_custom_mapping type ref to zif_ajson_mapping.
    data mv_keep_item_order type abap_bool.

    methods convert_any
      importing
        iv_data type any
        io_type type ref to cl_abap_typedescr
        is_prefix type zif_ajson=>ty_path_name
        iv_index type i default 0
        iv_item_order type i default 0
      changing
        ct_nodes type zif_ajson=>ty_nodes_tt
      raising
        zcx_ajson_error.

    methods convert_ajson
      importing
        io_json type ref to zcl_ajson
        is_prefix type zif_ajson=>ty_path_name
        iv_index type i default 0
      changing
        ct_nodes type zif_ajson=>ty_nodes_tt
      raising
        zcx_ajson_error.

    methods convert_value
      importing
        iv_data type any
        io_type type ref to cl_abap_typedescr
        is_prefix type zif_ajson=>ty_path_name
        iv_index type i default 0
        iv_item_order type i default 0
      changing
        ct_nodes type zif_ajson=>ty_nodes_tt
      raising
        zcx_ajson_error.

    methods convert_ref
      importing
        iv_data type any
        is_prefix type zif_ajson=>ty_path_name
        iv_index type i default 0
        iv_item_order type i default 0
      changing
        ct_nodes type zif_ajson=>ty_nodes_tt
      raising
        zcx_ajson_error.

    methods convert_struc
      importing
        iv_data type any
        io_type type ref to cl_abap_typedescr
        is_prefix type zif_ajson=>ty_path_name
        iv_index type i default 0
        iv_item_order type i default 0
      changing
        ct_nodes type zif_ajson=>ty_nodes_tt
        cs_root  type zif_ajson=>ty_node optional
      raising
        zcx_ajson_error.

    methods convert_table
      importing
        iv_data type any
        io_type type ref to cl_abap_typedescr
        is_prefix type zif_ajson=>ty_path_name
        iv_index type i default 0
        iv_item_order type i default 0
      changing
        ct_nodes type zif_ajson=>ty_nodes_tt
      raising
        zcx_ajson_error.

    methods insert_value_with_type
      importing
        iv_data type any
        iv_type type string
        io_type type ref to cl_abap_typedescr
        is_prefix type zif_ajson=>ty_path_name
        iv_index type i default 0
        iv_item_order type i default 0
      changing
        ct_nodes type zif_ajson=>ty_nodes_tt
      raising
        zcx_ajson_error.

endclass.

class lcl_abap_to_json implementation.

  method class_constructor.

    data lo_dummy type ref to zcl_ajson.
    data lo_type type ref to cl_abap_refdescr.
    lo_type ?= cl_abap_typedescr=>describe_by_data( lo_dummy ).
    gv_ajson_absolute_type_name = lo_type->get_referenced_type( )->absolute_name.

  endmethod.

  method convert.

    data lo_type type ref to cl_abap_typedescr.
    data lo_converter type ref to lcl_abap_to_json.

    lo_type = cl_abap_typedescr=>describe_by_data( iv_data ).

    create object lo_converter.
    lo_converter->mi_custom_mapping  = ii_custom_mapping.
    lo_converter->mv_keep_item_order = iv_keep_item_order.

    lo_converter->convert_any(
      exporting
        iv_data   = iv_data
        io_type   = lo_type
        is_prefix = is_prefix
        iv_index  = iv_array_index
      changing
        ct_nodes = rt_nodes ).

  endmethod.

  method convert_any.

    case io_type->kind.
      when cl_abap_typedescr=>kind_elem.
        convert_value(
          exporting
            iv_data   = iv_data
            io_type   = io_type
            is_prefix = is_prefix
            iv_index  = iv_index
            iv_item_order = iv_item_order
          changing
            ct_nodes = ct_nodes ).

      when cl_abap_typedescr=>kind_struct.
        convert_struc(
          exporting
            iv_data   = iv_data
            io_type   = io_type
            is_prefix = is_prefix
            iv_index  = iv_index
            iv_item_order = iv_item_order
          changing
            ct_nodes = ct_nodes ).

      when cl_abap_typedescr=>kind_table.
        convert_table(
          exporting
            iv_data   = iv_data
            io_type   = io_type
            is_prefix = is_prefix
            iv_index  = iv_index
            iv_item_order = iv_item_order
          changing
            ct_nodes = ct_nodes ).

      when others.

        if io_type->type_kind = cl_abap_typedescr=>typekind_dref.
          convert_ref(
            exporting
              iv_data   = iv_data
              is_prefix = is_prefix
              iv_index  = iv_index
              iv_item_order = iv_item_order
            changing
              ct_nodes = ct_nodes ).

        elseif io_type->type_kind = cl_abap_typedescr=>typekind_oref
          and cl_abap_typedescr=>describe_by_object_ref( iv_data )->absolute_name = gv_ajson_absolute_type_name.
          convert_ajson(
            exporting
              io_json   = iv_data
              is_prefix = is_prefix
              iv_index  = iv_index
            changing
              ct_nodes = ct_nodes ).
        else.
          zcx_ajson_error=>raise( |Unsupported type [{ io_type->type_kind
            }] @{ is_prefix-path && is_prefix-name }| ).
        endif.

    endcase.

  endmethod.

  method convert_ajson.

    field-symbols <src> like line of ct_nodes.
    field-symbols <dst> like line of ct_nodes.

    if io_json is not bound.
      return.
    endif.

    loop at io_json->mt_json_tree assigning <src>.
      append <src> to ct_nodes assigning <dst>.

      if <dst>-path is initial and <dst>-name is initial. " root node
        <dst>-path  = is_prefix-path.
        <dst>-name  = is_prefix-name.
        <dst>-index = iv_index.
      else.
        <dst>-path = is_prefix-path && is_prefix-name && <dst>-path.
      endif.
    endloop.

  endmethod.

  method convert_value.

    data ls_node like line of ct_nodes.

    ls_node-path  = is_prefix-path.
    ls_node-name  = is_prefix-name.
    ls_node-index = iv_index.
    ls_node-order = iv_item_order.

    if mi_custom_mapping is bound.
      ls_node-name = mi_custom_mapping->to_json(
        iv_path = is_prefix-path
        iv_name = is_prefix-name ).
    endif.

    if ls_node-name is initial.
      ls_node-name  = is_prefix-name.
    endif.

    if io_type->absolute_name = '\TYPE-POOL=ABAP\TYPE=ABAP_BOOL'
        or io_type->absolute_name = '\TYPE=ABAP_BOOLEAN'
        or io_type->absolute_name = '\TYPE=XSDBOOLEAN'
        or io_type->absolute_name = '\TYPE=FLAG'
        or io_type->absolute_name = '\TYPE=XFELD'.
      ls_node-type = zif_ajson=>node_type-boolean.
      if iv_data is not initial.
        ls_node-value = 'true'.
      else.
        ls_node-value = 'false'.
      endif.
    elseif io_type->type_kind co 'CNgXyDT'. " Char like, date/time, xstring
      ls_node-type = zif_ajson=>node_type-string.
      ls_node-value = |{ iv_data }|.
    elseif io_type->type_kind co 'bsI8PaeF'. " Numeric
      ls_node-type = zif_ajson=>node_type-number.
      ls_node-value = |{ iv_data }|.
    else.
      zcx_ajson_error=>raise( |Unexpected elementary type [{
        io_type->type_kind }] @{ is_prefix-path && is_prefix-name }| ).
    endif.

    append ls_node to ct_nodes.

  endmethod.

  method convert_ref.

    data ls_node like line of ct_nodes.

    ls_node-path  = is_prefix-path.
    ls_node-name  = is_prefix-name.
    ls_node-index = iv_index.
    ls_node-order = iv_item_order.

    if mi_custom_mapping is bound.
      ls_node-name = mi_custom_mapping->to_json(
        iv_path = is_prefix-path
        iv_name = is_prefix-name ).
    endif.

    if ls_node-name is initial.
      ls_node-name  = is_prefix-name.
    endif.

    if iv_data is initial.
      ls_node-type  = zif_ajson=>node_type-null.
      ls_node-value = 'null'.
    else.
      " TODO support data references
      zcx_ajson_error=>raise( |Unexpected reference @{ is_prefix-path && is_prefix-name }| ).
    endif.

    append ls_node to ct_nodes.

  endmethod.

  method convert_struc.

    data lo_struc type ref to cl_abap_structdescr.
    data lt_comps type cl_abap_structdescr=>component_table.
    data ls_next_prefix like is_prefix.
    data lv_item_order type i.
    data ls_root like line of ct_nodes.

    field-symbols <root> like ls_root.
    field-symbols <c> like line of lt_comps.
    field-symbols <val> type any.

    " Object root

    if cs_root is supplied. " call for include structure
      assign cs_root to <root>.
    else. " First call
      ls_root-path  = is_prefix-path.
      ls_root-name  = is_prefix-name.
      ls_root-type  = zif_ajson=>node_type-object.
      ls_root-index = iv_index.

      if mi_custom_mapping is bound.
        ls_root-name = mi_custom_mapping->to_json(
          iv_path = is_prefix-path
          iv_name = is_prefix-name ).
      endif.

      if ls_root-name is initial.
        ls_root-name  = is_prefix-name.
      endif.

      ls_root-order = iv_item_order.

      append ls_root to ct_nodes assigning <root>.

    endif.

    " Object attributes

    lo_struc ?= io_type.
    lt_comps = lo_struc->get_components( ).
    " get_components is potentially much slower than lo_struc->components
    " but ! we still need it to identify booleans
    " and rtti seems to cache type descriptions really well (https://github.com/sbcgua/benchmarks.git)
    " the structures will be repeated in real life

    ls_next_prefix-path = is_prefix-path && is_prefix-name && '/'.

    loop at lt_comps assigning <c>.

      if <c>-as_include = abap_true.

        convert_struc(
          exporting
            iv_data   = iv_data
            io_type   = <c>-type
            is_prefix = is_prefix
          changing
            cs_root  = <root>
            ct_nodes = ct_nodes ).

      else.

        <root>-children = <root>-children + 1.
        ls_next_prefix-name = to_lower( <c>-name ).
        assign component <c>-name of structure iv_data to <val>.
        assert sy-subrc = 0.

        if mv_keep_item_order = abap_true.
          lv_item_order = <root>-children.
        endif.

        convert_any(
          exporting
            iv_data   = <val>
            io_type   = <c>-type
            is_prefix = ls_next_prefix
            iv_item_order = lv_item_order
          changing
            ct_nodes = ct_nodes ).

      endif.

    endloop.

  endmethod.

  method convert_table.

    data lo_table type ref to cl_abap_tabledescr.
    data lo_ltype type ref to cl_abap_typedescr.
    data ls_next_prefix like is_prefix.
    data lv_tabix type sy-tabix.
    data ls_root like line of ct_nodes.

    field-symbols <root> like ls_root.
    field-symbols <tab> type any table.
    field-symbols <val> type any.

    " Array root

    ls_root-path  = is_prefix-path.
    ls_root-name  = is_prefix-name.
    ls_root-type  = zif_ajson=>node_type-array.
    ls_root-index = iv_index.
    ls_root-order = iv_item_order.

    if mi_custom_mapping is bound.
      ls_root-name = mi_custom_mapping->to_json(
        iv_path = is_prefix-path
        iv_name = is_prefix-name ).
    endif.

    if ls_root-name is initial.
      ls_root-name  = is_prefix-name.
    endif.

    append ls_root to ct_nodes assigning <root>.

    " Array items

    lo_table ?= io_type.
    lo_ltype  = lo_table->get_table_line_type( ).

    ls_next_prefix-path = is_prefix-path && is_prefix-name && '/'.
    assign iv_data to <tab>.

    lv_tabix = 1.
    loop at <tab> assigning <val>.
      ls_next_prefix-name = to_lower( |{ lv_tabix }| ).

      convert_any(
        exporting
          iv_data   = <val>
          io_type   = lo_ltype
          is_prefix = ls_next_prefix
          iv_index  = <root>-children + 1
        changing
          ct_nodes = ct_nodes ).

      <root>-children = <root>-children + 1.
      lv_tabix = lv_tabix + 1.
    endloop.

  endmethod.

  method insert_with_type.

    data lo_type type ref to cl_abap_typedescr.
    data lo_converter type ref to lcl_abap_to_json.

    lo_type = cl_abap_typedescr=>describe_by_data( iv_data ).

    create object lo_converter.
    lo_converter->mi_custom_mapping  = ii_custom_mapping.
    lo_converter->mv_keep_item_order = iv_keep_item_order.

    lo_converter->insert_value_with_type(
      exporting
        iv_data   = iv_data
        iv_type   = iv_type
        io_type   = lo_type
        is_prefix = is_prefix
        iv_index  = iv_array_index
      changing
        ct_nodes = rt_nodes ).

  endmethod.

  method insert_value_with_type.

    data lv_prefix type string.
    data ls_node like line of ct_nodes.

    lv_prefix = is_prefix-path && is_prefix-name.
    if io_type->type_kind co 'CNgXyDT'. " Char like, date/time, xstring
      if iv_type = zif_ajson=>node_type-boolean and iv_data <> 'true' and iv_data <> 'false'.
        zcx_ajson_error=>raise( |Unexpected boolean value [{ iv_data }] @{ lv_prefix }| ).
      elseif iv_type = zif_ajson=>node_type-null and iv_data is not initial.
        zcx_ajson_error=>raise( |Unexpected null value [{ iv_data }] @{ lv_prefix }| ).
      elseif iv_type = zif_ajson=>node_type-number and iv_data cn '0123456789. E+-'.
        zcx_ajson_error=>raise( |Unexpected numeric value [{ iv_data }] @{ lv_prefix }| ).
      elseif iv_type <> zif_ajson=>node_type-string and iv_type <> zif_ajson=>node_type-boolean
        and iv_type <> zif_ajson=>node_type-null and iv_type <> zif_ajson=>node_type-number.
        zcx_ajson_error=>raise( |Unexpected type for value [{ iv_type },{ iv_data }] @{ lv_prefix }| ).
      endif.
    elseif io_type->type_kind co 'bsI8PaeF'. " Numeric
      if iv_type <> zif_ajson=>node_type-number.
        zcx_ajson_error=>raise( |Unexpected value for numeric [{ iv_data }] @{ lv_prefix }| ).
      endif.
    else.
      zcx_ajson_error=>raise( |Unexpected type [{ io_type->type_kind }] @{ lv_prefix }| ).
    endif.

    ls_node-path  = is_prefix-path.
    ls_node-name  = is_prefix-name.
    ls_node-index = iv_index.
    ls_node-value = iv_data.
    ls_node-type  = iv_type.
    ls_node-order = iv_item_order.

    if mi_custom_mapping is bound.
      ls_node-name = mi_custom_mapping->to_json(
        iv_path = is_prefix-path
        iv_name = is_prefix-name ).
    endif.

    if ls_node-name is initial.
      ls_node-name  = is_prefix-name.
    endif.

    append ls_node to ct_nodes.

  endmethod.

endclass.

**********************************************************************
* FILTER RUNNER
**********************************************************************

class lcl_filter_runner definition final.
  public section.
    methods run
      importing
        ii_filter type ref to zif_ajson_filter
        it_source_tree type zif_ajson=>ty_nodes_ts
      changing
        ct_dest_tree type zif_ajson=>ty_nodes_ts
      raising
        zcx_ajson_error.

  private section.
    data mi_filter type ref to zif_ajson_filter.
    data mr_source_tree type ref to zif_ajson=>ty_nodes_ts.
    data mr_dest_tree type ref to zif_ajson=>ty_nodes_ts.

    methods walk
      importing
        iv_path type string
      changing
        cs_parent type zif_ajson=>ty_node optional
      raising
        zcx_ajson_error.

endclass.

class lcl_filter_runner implementation.

  method run.

    assert ii_filter is bound.
    mi_filter = ii_filter.
    clear ct_dest_tree.

    get reference of it_source_tree into mr_source_tree.
    get reference of ct_dest_tree into mr_dest_tree.

    walk( iv_path = '' ).

  endmethod.

  method walk.

    data ls_node type zif_ajson=>ty_node.

    loop at mr_source_tree->* into ls_node where path = iv_path.
      case ls_node-type.
        when zif_ajson=>node_type-boolean or zif_ajson=>node_type-null
          or zif_ajson=>node_type-number or zif_ajson=>node_type-string.

          if mi_filter->keep_node( ls_node ) = abap_false.
            continue.
          endif.

        when zif_ajson=>node_type-array or zif_ajson=>node_type-object.

          if mi_filter->keep_node(
              is_node  = ls_node
              iv_visit = zif_ajson_filter=>visit_type-open ) = abap_false.
            continue.
          endif.

          " Intentionally clear AFTER "open"
          clear ls_node-children.

          walk(
            exporting
              iv_path = iv_path && ls_node-name && `/`
            changing
              cs_parent    = ls_node ).

          if mi_filter->keep_node(
              is_node  = ls_node
              iv_visit = zif_ajson_filter=>visit_type-close ) = abap_false.
            continue.
          endif.

        when others.
          zcx_ajson_error=>raise( |Unexpected node type { ls_node-type }| ).
      endcase.

      if cs_parent is supplied.
        cs_parent-children = cs_parent-children + 1.
        if cs_parent-type = zif_ajson=>node_type-array.
          ls_node-name  = |{ cs_parent-children }|.
          ls_node-index = cs_parent-children.
        endif.
      endif.
      insert ls_node into table mr_dest_tree->*.

    endloop.

  endmethod.

endclass.