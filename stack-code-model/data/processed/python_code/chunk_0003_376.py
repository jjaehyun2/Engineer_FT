*&---------------------------------------------------------------------*
*&  Include           /ENSX/INCL_XSLT_MACROS
*&---------------------------------------------------------------------*
*"* use this source file for any macro definitions you need
*"* in the implementation part of the class

* Macros for class generation - type definition

  DEFINE add_cl_srcline_1.
    lv_src = &1.
    lv_par = &2. replace '%1' in lv_src with lv_par.
    CONCATENATE xslt lv_src cl_abap_char_utilities=>cr_lf into xslt SEPARATED BY space.
  END-OF-DEFINITION.

  DEFINE add_cl_srcline_2.
    lv_src = &1.
    lv_par = &2. replace '%1' in lv_src with lv_par.
    lv_par = &3. replace '%2' in lv_src with lv_par.
    CONCATENATE xslt lv_src cl_abap_char_utilities=>cr_lf into xslt SEPARATED BY space.
  END-OF-DEFINITION.


**********************************************************************

* Macros for simple transformation generation

  DEFINE add_st_srcline.
    lv_lin = &1.
    concatenate xslt lv_lin cl_abap_char_utilities=>cr_lf into xslt.
  END-OF-DEFINITION.

  DEFINE add_st_srcline_1.
    lv_lin = &1.
    lv_par = &2. replace all occurrences of '%1'  in lv_lin with lv_par.
    concatenate xslt lv_lin cl_abap_char_utilities=>cr_lf into xslt.
  END-OF-DEFINITION.

  DEFINE add_st_srcline_2.
    lv_lin = &1.
    lv_par = &2. replace all occurrences of '%1'  in lv_lin with lv_par.
    lv_par = &3. replace all occurrences of '%2'  in lv_lin with lv_par.
    concatenate xslt lv_lin cl_abap_char_utilities=>cr_lf into xslt.
  END-OF-DEFINITION.

* st header & footer

  DEFINE add_st_header.
    add_st_srcline   '<?sap.transform simple?>'.            "#EC NOTEXT
    add_st_srcline   '<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"'. "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_namespace.
    add_st_srcline_2   'xmlns:%1="%2"' &1 &2.               "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_header2.
    add_st_srcline   '>'.
    add_st_srcline   ''.
  END-OF-DEFINITION.

  DEFINE add_st_footer.
    add_st_srcline   '</tt:transform>'.                     "#EC NOTEXT
  END-OF-DEFINITION.

* comments

  DEFINE add_st_comment_start.
    add_st_srcline   '<!-- ******************************************************************'. "#EC NOTEXT
    add_st_srcline   ''.
  END-OF-DEFINITION.

  DEFINE add_st_comment.
    lv_lin = &1. replace all occurrences of '--' in lv_lin with '__'.
    concatenate xslt lv_lin cl_abap_char_utilities=>cr_lf into xslt.
  END-OF-DEFINITION.

  DEFINE add_st_comment_end.
    add_st_srcline   '******************************************************************* -->'. "#EC NOTEXT
    add_st_srcline   ''.
  END-OF-DEFINITION.

* templates
  DEFINE add_st_base_root.
    add_st_srcline '  <tt:root name="ROOT" type="?"/>'.
  END-OF-DEFINITION.

  DEFINE add_st_json_roots.
    add_st_srcline_2   '<tt:root name="%1" type="ddic:%2"/>' &1 &2. "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_json_roots_notype.
    add_st_srcline_1   '<tt:root name="%1"/>' &1.           "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_json_template_start.
    add_st_srcline   ''.
    add_st_srcline   '<tt:template>'.                       "#EC NOTEXT
*    add_st_srcline   '<object>'.                            "#EC NOTEXT
    if lv_initial is not initial.
      add_st_srcline '<initialValue>'.                      "#EC NOTEXT
    else.
"      add_st_srcline '<context>'.                           "#EC NOTEXT
    endif.
  END-OF-DEFINITION.

  DEFINE add_st_json_template_end.
    if lv_initial is not initial.
      add_st_srcline '</initialValue>'.                     "#EC NOTEXT
    else.
*      add_st_srcline '</context>'.                          "#EC NOTEXT
    endif.
*    add_st_srcline   '</object>'.                           "#EC NOTEXT
    add_st_srcline   '</tt:template>'.                      "#EC NOTEXT
    add_st_srcline   ''.
  END-OF-DEFINITION.

  DEFINE add_st_main_template_start.
    add_st_srcline   ''.
    add_st_srcline   '<tt:template>'.                       "#EC NOTEXT
*    add_st_srcline_1   '<tt:ref name="%1">' &1.                "#EC NOTEXT
    if lv_initial is not initial.
      add_st_srcline '<initialValue>'.                      "#EC NOTEXT
    else.
"      add_st_srcline '<context>'.                           "#EC NOTEXT
    endif.
  END-OF-DEFINITION.

  DEFINE add_st_main_template_end.
    if lv_initial is not initial.
      add_st_srcline '</initialValue>'.                     "#EC NOTEXT
    else.
*      add_st_srcline '</context>'.                          "#EC NOTEXT
    endif.
*    add_st_srcline   '</tt:ref>'.                           "#EC NOTEXT
    add_st_srcline   '</tt:template>'.                      "#EC NOTEXT
    add_st_srcline   ''.
  END-OF-DEFINITION.

  DEFINE add_st_template_start.
    add_st_srcline_1 '<tt:template name="%1">' &1.          "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_template_end.
    add_st_srcline   '</tt:template>'.                      "#EC NOTEXT
    add_st_srcline   ''.
  END-OF-DEFINITION.

* optional
  DEFINE add_st_serialize_start.
    add_st_srcline_1   '<tt:serialize> <!-- %1 -->' &1.     "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_serialize_end.
    add_st_srcline_1   '</tt:serialize ><!-- %1 -->' &1.    "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_cond_start.
    add_st_srcline   '<tt:cond>'.                           "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_cond_check_start.
    add_st_srcline_1   '<tt:cond check="not-initial(%1)">' &1. "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_scond_check_start.
    add_st_srcline_1   '<tt:cond s-check="not-initial(%1)">' &1. "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_cond_exists_start.
    add_st_srcline_1   '<tt:cond check="exist(%1)">' &1.    "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_scond_exists_start.
    add_st_srcline_1   '<tt:cond s-check="exist(%1)">' &1.  "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_cond_end.
    add_st_srcline_1   '</tt:cond> <!-- %1 -->' &1.         "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_scond_end.
    add_st_srcline_1   '</tt:s-cond> <!-- %1 -->' &1.       "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_skip_start.
    add_st_srcline_1  '<tt:skip name="%1" count="*">' &1.   "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_skip_end.
    add_st_srcline_1  '</tt:skip> <!-- %1 -->' &1.          "#EC NOTEXT
  END-OF-DEFINITION.

* fields

  DEFINE add_st_component_start_ref.
    add_st_srcline_2 '<%1 tt:ref="%2">' &1 &2.              "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_component_start.
    add_st_srcline_1 '<%1>' &1 .                            "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_component_simple.
    add_st_srcline   '<tt:value/>'.                         "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_component_end.
    add_st_srcline_1 '</%1>' &1.                            "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_complex.
    add_st_srcline_1 '<tt:apply name="%1"/>' &1.            "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_table_start.
    add_st_srcline_2 '<tt:loop ref="%1" name="%2">' &1 &2.  "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_table_end.
    add_st_srcline   '</tt:loop>'.                          "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_component_simple_start.
    add_st_srcline_2 '<%1 name="%2">' &1 &2 .               "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_component_simple_end.
    add_st_srcline_1 '</%1>' &1.                            "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_component_simple_value.
    add_st_srcline_1 '<tt:value ref="%1"/>' &1.             "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_component_value_ref.
    add_st_srcline_2 '<%1 tt:value-ref="%2"/>' &1 &2.       "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_component_value.
    add_st_srcline_1 '<%1 tt:value/>' &1.                   "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_component_datetime.
    add_st_srcline   '<tt:value ref="DATE"/>'.              "#EC NOTEXT
    add_st_srcline   '<tt:text>T</tt:text>'.                "#EC NOTEXT
    add_st_srcline   '<tt:value ref="TIME"/>'.              "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_component_simple_boole.
    add_st_srcline_1 '<tt:value option="format(boolean)" ref="%1" />' &1.             "#EC NOTEXT
  END-OF-DEFINITION.
  DEFINE add_st_component_boole.
    add_st_srcline_2 '<%1 tt:value-ref="%2" option="format(boolean)" />' &1 &2.             "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_object_start.
    if &1 ne space.
      add_st_srcline_1 '<object name="%1">' &1.             "#EC NOTEXT
    else.
      add_st_srcline '<object>'.                            "#EC NOTEXT
    endif.
  END-OF-DEFINITION.

  DEFINE add_st_object_end.
    add_st_srcline_1 '</object> <!-- %1 -->' &1.            "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_array_start.
    add_st_srcline_1 '<array name="%1">' &1.                "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_array_end.
    add_st_srcline_1 '</array>  <!-- %1 -->' &1.            "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_member_start.
    add_st_srcline_1 '<member name="%1">' &1.               "#EC NOTEXT
  END-OF-DEFINITION.

  DEFINE add_st_member_end.
    add_st_srcline '</member>'.                             "#EC NOTEXT
  END-OF-DEFINITION.

**********************************************************************