define _add_mu_token.
  append initial line to &1 assigning <token>.
  <token>-type    = &2.
  <token>-cond    = &3.
  <token>-level   = &4.
  <token>-content = &5.
end-of-definition.

define _add_mu_val_rc.
  append initial line to &1 assigning <rcline>.
  <rcline>-val    = &2.
  <rcline>-rc     = &3.
end-of-definition.

class ltcl_mustache_parser definition final
  for testing risk level harmless duration short.

  private section.

    constants c_nl type c value cl_abap_char_utilities=>newline.

    methods parse_template          for testing.
    methods parse_template_table    for testing.
    methods parse_template_negative for testing.
    methods parse_tag               for testing.
    methods parse_tag_negative      for testing.

endclass.

class ltcl_mustache_parser implementation.

  method parse_template.

    data:
          lt_exp      type zif_mustache=>ty_token_tt,
          lt_act      type zif_mustache=>ty_token_tt,
          lv_count    type i,
          lv_idx      type i,
          lv_template type string,
          lx          type ref to zcx_mustache_error.

    zcl_mustache_test=>get_test_case( importing ev_count = lv_count ).

    do lv_count times.
      lv_idx = sy-index.
      zcl_mustache_test=>get_test_case(
        exporting
          iv_index    = lv_idx
        importing
          ev_template = lv_template
          et_tokens   = lt_exp ).

      try .
          lt_act = zcl_mustache_parser=>parse_template( lv_template ).
          cl_abap_unit_assert=>assert_equals(
            exp = lt_exp
            act = lt_act
            msg = |parse_template, case { lv_idx }| ).
        catch zcx_mustache_error into lx.
          cl_abap_unit_assert=>fail( lx->msg ).
      endtry.

    enddo.

  endmethod.  " parse_template.

  method parse_template_negative.

    data:
          lt_tab type zcl_mustache_test=>ty_tag_rc_tt,
          lx     type ref to zcx_mustache_error.

    field-symbols <rcline> like line of lt_tab.

    _add_mu_val_rc lt_tab 'Hello {{name}!'               'CTNF'.
    _add_mu_val_rc lt_tab 'Good {{#pm}}afternoon'        'SNC'.
    _add_mu_val_rc lt_tab 'Good afternoon{{/pm}}'        'CNOS'.
    _add_mu_val_rc lt_tab 'Good {{#pm}}afternoon{{/am}}' 'CSM'.

    loop at lt_tab assigning <rcline>.
      clear lx.
      try .
          zcl_mustache_parser=>parse_template( <rcline>-val ).
        catch zcx_mustache_error into lx.
          assert 1 = 1.
      endtry.
      cl_abap_unit_assert=>assert_not_initial( act = lx ).
      cl_abap_unit_assert=>assert_equals( exp = <rcline>-rc act = lx->rc ).
    endloop.

  endmethod. "parse_template_negative

  method parse_template_table.

    data:
          lt_exp      type zif_mustache=>ty_token_tt,
          lt_act      type zif_mustache=>ty_token_tt,
          lt_template type string_table,
          lx          type ref to zcx_mustache_error.

    field-symbols <token> like line of lt_exp.

    append 'Our sales:'              to lt_template.
    append '{{#items}}'              to lt_template.
    append '* {{name}} - ${{price}}' to lt_template.
    append '{{/items}}'              to lt_template.

    _add_mu_token lt_exp zif_mustache=>c_token_type-static      ''  1   `Our sales:`.
    _add_mu_token lt_exp zif_mustache=>c_token_type-static      ''  1   c_nl.
    _add_mu_token lt_exp zif_mustache=>c_token_type-section     '=' 1   'items'.
    _add_mu_token lt_exp zif_mustache=>c_token_type-static      ''  2   `* `.
    _add_mu_token lt_exp zif_mustache=>c_token_type-etag        ''  2   'name'.
    _add_mu_token lt_exp zif_mustache=>c_token_type-static      ''  2   ` - $`.
    _add_mu_token lt_exp zif_mustache=>c_token_type-etag        ''  2   'price'.
    _add_mu_token lt_exp zif_mustache=>c_token_type-static      ''  2   c_nl.

    try.
        lt_act = zcl_mustache_parser=>parse_template( it_template = lt_template ).
      catch zcx_mustache_error into lx.
        cl_abap_unit_assert=>fail( lx->msg ).
    endtry.
    cl_abap_unit_assert=>assert_equals( exp = lt_exp act = lt_act ).

  endmethod.  " parse_template_table

  method parse_tag.

    data:
          lt_exp type zif_mustache=>ty_token_tt,
          lt_act type zif_mustache=>ty_token_tt,
          lx type ref to zcx_mustache_error.

    field-symbols <token> like line of lt_exp.

    try .
        append zcl_mustache_parser=>parse_tag( 'name' ) to lt_act.
        append zcl_mustache_parser=>parse_tag( '{ name }' ) to lt_act.
        append zcl_mustache_parser=>parse_tag( '&name' ) to lt_act.
        append zcl_mustache_parser=>parse_tag( '#name' ) to lt_act.
        append zcl_mustache_parser=>parse_tag( '# name ' ) to lt_act.
        append zcl_mustache_parser=>parse_tag( '^name' ) to lt_act.
        append zcl_mustache_parser=>parse_tag( '/name' ) to lt_act.
        append zcl_mustache_parser=>parse_tag( '!name' ) to lt_act.
        append zcl_mustache_parser=>parse_tag( '= {*  *} =' ) to lt_act.
      catch zcx_mustache_error into lx.
        cl_abap_unit_assert=>fail( lx->msg ).
    endtry.

    "                    TYPE                                  COND LEV CONTENT
    _add_mu_token lt_exp zif_mustache=>c_token_type-etag        ''  0   'name'.
    _add_mu_token lt_exp zif_mustache=>c_token_type-utag        ''  0   'name'.
    _add_mu_token lt_exp zif_mustache=>c_token_type-utag        ''  0   'name'.
    _add_mu_token lt_exp zif_mustache=>c_token_type-section     '=' 0   'name'.
    _add_mu_token lt_exp zif_mustache=>c_token_type-section     '=' 0   'name'.
    _add_mu_token lt_exp zif_mustache=>c_token_type-section     '!' 0   'name'.
    _add_mu_token lt_exp zif_mustache=>c_token_type-section_end ''  0   'name'.
    _add_mu_token lt_exp zif_mustache=>c_token_type-comment     ''  0   'name'.
    _add_mu_token lt_exp zif_mustache=>c_token_type-delimiter   ''  0   '{* *}'. " Boobs :)

    cl_abap_unit_assert=>assert_equals( exp = lt_exp act = lt_act ).

    " Path
    append initial line to lt_exp assigning <token>.
    <token>-type    = zif_mustache=>c_token_type-etag.
    <token>-content = 'A/B'.
    append 'A' to <token>-path.
    append 'B' to <token>-path.
    cl_abap_unit_assert=>assert_equals( exp = <token> act = zcl_mustache_parser=>parse_tag( 'A/B' ) ).

  endmethod. "parse_tag

  method parse_tag_negative.

    data:
          lt_tab type zcl_mustache_test=>ty_tag_rc_tt,
          lx     type ref to zcx_mustache_error.

    field-symbols <rcline> like line of lt_tab.

    _add_mu_val_rc lt_tab ''        'ET'.
    _add_mu_val_rc lt_tab '{}'      'ET'.
    _add_mu_val_rc lt_tab '   '     'ET'.
    _add_mu_val_rc lt_tab '{   }'   'ET'.
    _add_mu_val_rc lt_tab '{name'   'MC}'.
    _add_mu_val_rc lt_tab '=name'   'MC='.
    _add_mu_val_rc lt_tab '#'       'ET'.
    _add_mu_val_rc lt_tab '=xxx='   'CDF'.
    _add_mu_val_rc lt_tab '=x x x=' 'CDF'.

    loop at lt_tab assigning <rcline>.
      clear lx.
      try .
          zcl_mustache_parser=>parse_tag( <rcline>-val ).
        catch zcx_mustache_error into lx.
          assert 1 = 1.
      endtry.
      cl_abap_unit_assert=>assert_not_initial( act = lx ).
      cl_abap_unit_assert=>assert_equals( exp = <rcline>-rc act = lx->rc ).
    endloop.

  endmethod. "parse_tag_negative

endclass.