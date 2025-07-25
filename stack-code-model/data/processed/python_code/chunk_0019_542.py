class zcl_abap_graph_node_record  definition public final create private .

  public section.
    interfaces: zif_abap_graph_node.
    aliases: attributes  for zif_abap_graph_node~attributes,
             id          for zif_abap_graph_node~id,
             graph       for zif_abap_graph_node~graph,
             ty_link     for zif_abap_graph_node~ty_link,
             tt_link     for zif_abap_graph_node~tt_link,
             getlinks    for zif_abap_graph_node~getlinks ,
             linkto      for zif_abap_graph_node~linkto ,
             render      for zif_abap_graph_node~render ,
             tt_node     for zif_abap_graph_node~tt_node ,
             ty_nod      for zif_abap_graph_node~ty_node .
    types: begin of ty_component,
             name            type string,
             value           type string,
             partid          type string,
             nameattributes  like attributes,
             valueattributes like attributes,
           end of ty_component,
           tt_component type table of ty_component.

    data: headerattr  like attributes read-only.

    class-methods create importing id              type string
                                   label           type string optional
                                   graph           type ref to zcl_abap_graph
                                   escape          type abap_bool default abap_true
                         returning value(r_result) type ref to zcl_abap_graph_node_record.
    methods: addcomponent importing name               type string
                                    value              type string
                                    escape             type abap_bool default abap_true
                                    bgcolor            type string optional
                                    value(partid)      type string optional
                                    nameattributes     like attributes optional
                                    valueattributes    like attributes optional
                          returning value(componentid) type string.


  protected section.
    data: mainlabel type string.
  private section.
    data: links      type tt_link,
          components type tt_component.

    methods validatesource
      importing
        i_source type string.
    methods getcomp
      importing
        partid          type string
      returning
        value(r_result) type string.

endclass.



class zcl_abap_graph_node_record implementation.
  method create.
    if not graph is bound.
      zcx_abap_graph=>raise( 'A node requires valid parent graph' ).
    endif.
    create object r_result.
    r_result->id = zcl_abap_graph_utilities=>quoteifneeded( id ).
    r_result->graph = graph.
    r_result->attributes = zcl_abap_graph_attr=>create( ).
    if escape = abap_true.
      r_result->mainlabel = cl_http_utility=>escape_html( label ).
    else.
      r_result->mainlabel = label .
    endif.
    r_result->attributes->set( name  = 'shape' value = 'plaintext' ).
    r_result->headerattr = zcl_abap_graph_attr=>create( abap_true ).
    graph->addnode( r_result ).
  endmethod.

  method zif_abap_graph_node~getlinks.
    links = me->links.
  endmethod.

  method zif_abap_graph_node~linkto.
    data: esclabel type string.
    field-symbols: <link> like line of links.

    append initial line to links assigning <link>.
    if source = ''.
      <link>-parentid = id.
    else.
      validatesource( source ).
      <link>-parentid = source.
    endif.
    if graph->has_id( destination ) = abap_false.
      zcx_abap_graph=>raise( 'Destination must be a valid part of the node' ).
    endif.
    <link>-childid    = destination.
    <link>-attributes = zcl_abap_graph_attr=>create( ).
    esclabel = cl_http_utility=>escape_html( label ).
    <link>-attributes->set( name  = 'label' value = esclabel ).
    <link>-attributes->set( name  = 'color' value = color ).
    <link>-attributes->set( name  = 'fontcolor' value = color ).
  endmethod.

  method zif_abap_graph_node~render.
    data: temp      type string,
          nameattr  type string,
          valueattr type string,
          comp      type string.

    field-symbols: <comp> like line of components.
    agdefinitions.

    temp = headerattr->render( ).

    agexpand '<<table border="0" cellborder="1" cellspacing="0">\n<tr><td colspan="2" {temp}>{mainlabel}</td></tr>'
             temp.


    loop at components assigning <comp>.
      comp = getcomp( <comp>-partid ).
      nameattr = <comp>-nameattributes->render( ).
      valueattr = <comp>-valueattributes->render( ).
      agexpand '{temp}\n<tr><td{nameattr}>{<comp>-name}</td><td{valueattr}{comp}>{<comp>-value}</td></tr>' temp.
    endloop.
    agexpand '{temp}\n</table>>' temp.

    attributes->setraw( name  = 'label' value = temp ).
    temp = attributes->render( ).

    agexpand '{id}{temp};' dotsource.

  endmethod.

  method addcomponent.

    field-symbols: <comp> like line of components.

    if partid <> ''.
      partid = zcl_abap_graph_utilities=>quoteifneeded( partid ).
      concatenate id ':' partid into componentid.
      "will raise an exception for invalid/already used IDs
      graph->register_id( componentid ).
    endif.

    append initial line to components assigning <comp>.

    <comp>-name       = name.
    <comp>-partid     = partid.
    if escape = abap_true.
      <comp>-value      = cl_http_utility=>escape_html( value ).
    else.
      <comp>-value      = value .
    endif.
    if nameattributes is bound.
      <comp>-nameattributes = nameattributes.
    else.
      <comp>-nameattributes = zcl_abap_graph_attr=>create( abap_true ).
    endif.
    if valueattributes is bound.
      <comp>-valueattributes = valueattributes.
    else.
      <comp>-valueattributes = zcl_abap_graph_attr=>create( abap_true ).
    endif.
    if bgcolor <> ''.
      <comp>-nameattributes->set( name  = 'bgcolor' value = bgcolor ).
      <comp>-valueattributes->set( name  = 'bgcolor' value = bgcolor ).
    endif.

  endmethod.


  method validatesource.
    data: parent type string,
          child  type string.
    if graph->has_id( i_source ) = abap_true.
      find regex '(".+"):(".+")$' in i_source submatches parent child.
    endif.
    if sy-subrc <> 0 or parent <> id.
      zcx_abap_graph=>raise( 'Source must be a valid part of the node' ).
    endif.
  endmethod.


  method getcomp.
    if partid <> ''.
      concatenate ' port=' partid ' ' into r_result respecting blanks.
    endif.
  endmethod.

endclass.