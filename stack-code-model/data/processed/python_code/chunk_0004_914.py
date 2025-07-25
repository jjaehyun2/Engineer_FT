CLASS zcl_abapgit_html_form DEFINITION
  PUBLIC
  FINAL
  CREATE PRIVATE.

  PUBLIC SECTION.

    CONSTANTS c_rows TYPE string VALUE 'rows'.

    CONSTANTS:
      BEGIN OF c_cmd_type,
        input  TYPE i VALUE 1,
        link   TYPE i VALUE 2,
        button TYPE i VALUE 3,
      END OF c_cmd_type.

    CLASS-METHODS create
      IMPORTING
        !iv_form_id    TYPE csequence OPTIONAL
        !iv_help_page  TYPE csequence OPTIONAL
      RETURNING
        VALUE(ro_form) TYPE REF TO zcl_abapgit_html_form.
    METHODS render
      IMPORTING
        !iv_form_class     TYPE csequence
        !io_values         TYPE REF TO zcl_abapgit_string_map
        !io_validation_log TYPE REF TO zcl_abapgit_string_map OPTIONAL
      RETURNING
        VALUE(ri_html)     TYPE REF TO zif_abapgit_html.
    METHODS command
      IMPORTING
        !iv_label      TYPE csequence
        !iv_action     TYPE csequence
        !iv_is_main    TYPE abap_bool DEFAULT abap_false
        !iv_cmd_type   TYPE i DEFAULT 1
      RETURNING
        VALUE(ro_self) TYPE REF TO zcl_abapgit_html_form.
    METHODS text
      IMPORTING
        !iv_label       TYPE csequence
        !iv_name        TYPE csequence
        !iv_hint        TYPE csequence OPTIONAL
        !iv_required    TYPE abap_bool DEFAULT abap_false
        !iv_upper_case  TYPE abap_bool DEFAULT abap_false
        !iv_readonly    TYPE abap_bool DEFAULT abap_false
        !iv_password    TYPE abap_bool DEFAULT abap_false
        !iv_placeholder TYPE csequence OPTIONAL
        !iv_side_action TYPE csequence OPTIONAL
        !iv_min         TYPE i DEFAULT cl_abap_math=>min_int4
        !iv_max         TYPE i DEFAULT cl_abap_math=>max_int4
      RETURNING
        VALUE(ro_self)  TYPE REF TO zcl_abapgit_html_form.
    METHODS textarea
      IMPORTING
        !iv_label       TYPE csequence
        !iv_name        TYPE csequence
        !iv_hint        TYPE csequence OPTIONAL
        !iv_required    TYPE abap_bool DEFAULT abap_false
        !iv_readonly    TYPE abap_bool DEFAULT abap_false
        !iv_placeholder TYPE csequence OPTIONAL
      RETURNING
        VALUE(ro_self)  TYPE REF TO zcl_abapgit_html_form.
    METHODS number
      IMPORTING
        !iv_label      TYPE csequence
        !iv_name       TYPE csequence
        !iv_hint       TYPE csequence OPTIONAL
        !iv_required   TYPE abap_bool DEFAULT abap_false
        !iv_readonly   TYPE abap_bool DEFAULT abap_false
        !iv_min        TYPE i DEFAULT cl_abap_math=>min_int4
        !iv_max        TYPE i DEFAULT cl_abap_math=>max_int4
      RETURNING
        VALUE(ro_self) TYPE REF TO zcl_abapgit_html_form.
    METHODS checkbox
      IMPORTING
        !iv_label      TYPE csequence
        !iv_name       TYPE csequence
        !iv_hint       TYPE csequence OPTIONAL
      RETURNING
        VALUE(ro_self) TYPE REF TO zcl_abapgit_html_form.
    METHODS radio
      IMPORTING
        !iv_label         TYPE csequence
        !iv_name          TYPE csequence
        !iv_default_value TYPE csequence OPTIONAL
        !iv_hint          TYPE csequence OPTIONAL
      RETURNING
        VALUE(ro_self)    TYPE REF TO zcl_abapgit_html_form.
    METHODS option
      IMPORTING
        !iv_label      TYPE csequence
        !iv_value      TYPE csequence
      RETURNING
        VALUE(ro_self) TYPE REF TO zcl_abapgit_html_form.
    METHODS table
      IMPORTING
        !iv_label      TYPE csequence
        !iv_name       TYPE csequence
        !iv_hint       TYPE csequence OPTIONAL
      RETURNING
        VALUE(ro_self) TYPE REF TO zcl_abapgit_html_form.
    METHODS column
      IMPORTING
        !iv_label      TYPE csequence
        !iv_width      TYPE csequence OPTIONAL
        !iv_readonly   TYPE abap_bool DEFAULT abap_false
      RETURNING
        VALUE(ro_self) TYPE REF TO zcl_abapgit_html_form.
    METHODS start_group
      IMPORTING
        !iv_label      TYPE csequence
        !iv_name       TYPE csequence
        !iv_hint       TYPE csequence OPTIONAL
      RETURNING
        VALUE(ro_self) TYPE REF TO zcl_abapgit_html_form.
    METHODS normalize_form_data
      IMPORTING
        !io_form_data       TYPE REF TO zcl_abapgit_string_map
      RETURNING
        VALUE(ro_form_data) TYPE REF TO zcl_abapgit_string_map
      RAISING
        zcx_abapgit_exception.
    METHODS validate_required_fields
      IMPORTING
        !io_form_data            TYPE REF TO zcl_abapgit_string_map
      RETURNING
        VALUE(ro_validation_log) TYPE REF TO zcl_abapgit_string_map
      RAISING
        zcx_abapgit_exception.
    METHODS is_empty
      IMPORTING
        !io_form_data   TYPE REF TO zcl_abapgit_string_map
      RETURNING
        VALUE(rv_empty) TYPE abap_bool
      RAISING
        zcx_abapgit_exception.
    METHODS hidden
      IMPORTING
        !iv_name       TYPE csequence
      RETURNING
        VALUE(ro_self) TYPE REF TO zcl_abapgit_html_form.

  PROTECTED SECTION.
  PRIVATE SECTION.

    TYPES:
      BEGIN OF ty_subitem,
        label    TYPE string,
        value    TYPE string,
        readonly TYPE abap_bool,
      END OF ty_subitem.
    TYPES:
      ty_subitems TYPE STANDARD TABLE OF ty_subitem WITH DEFAULT KEY.
    TYPES:
      BEGIN OF ty_field,
        type          TYPE i,
        name          TYPE string,
        label         TYPE string,
        hint          TYPE string,
        dblclick      TYPE string,
        placeholder   TYPE string,
        required      TYPE string,
        upper_case    TYPE abap_bool,
        item_class    TYPE string,
        error         TYPE string,
        default_value TYPE string,
        side_action   TYPE string,
        subitems      TYPE ty_subitems,
        readonly      TYPE abap_bool,
        password      TYPE abap_bool,
        min           TYPE i,
        max           TYPE i,
*        onclick ???
      END OF ty_field.
    TYPES:
      BEGIN OF ty_command,
        label    TYPE string,
        action   TYPE string,
        is_main  TYPE abap_bool,
        cmd_type TYPE i,
*        onclick ???
      END OF ty_command.
    TYPES:
      BEGIN OF ty_attr,
        value       TYPE string,
        error       TYPE string,
        hint        TYPE string,
        readonly    TYPE string,
        placeholder TYPE string,
        required    TYPE string,
      END OF ty_attr.

    CONSTANTS:
      BEGIN OF c_field_type,
        text        TYPE i VALUE 1,
        radio       TYPE i VALUE 2,
        checkbox    TYPE i VALUE 3,
        field_group TYPE i VALUE 4,
        number      TYPE i VALUE 5,
        textarea    TYPE i VALUE 6,
        table       TYPE i VALUE 7,
        hidden      TYPE i VALUE 8,
      END OF c_field_type.
    DATA:
      mt_fields TYPE STANDARD TABLE OF ty_field
          WITH UNIQUE SORTED KEY by_name COMPONENTS name.
    DATA:
      mt_commands TYPE STANDARD TABLE OF ty_command.
    DATA mv_form_id TYPE string.
    DATA mv_help_page TYPE string.

    METHODS render_field
      IMPORTING
        !ii_html           TYPE REF TO zif_abapgit_html
        !io_values         TYPE REF TO zcl_abapgit_string_map
        !io_validation_log TYPE REF TO zcl_abapgit_string_map
        !is_field          TYPE ty_field.
    METHODS render_field_text
      IMPORTING
        !ii_html  TYPE REF TO zif_abapgit_html
        !is_field TYPE ty_field
        !is_attr  TYPE ty_attr.
    METHODS render_field_textarea
      IMPORTING
        !ii_html  TYPE REF TO zif_abapgit_html
        !is_field TYPE ty_field
        !is_attr  TYPE ty_attr.
    METHODS render_field_checkbox
      IMPORTING
        !ii_html  TYPE REF TO zif_abapgit_html
        !is_field TYPE ty_field
        !is_attr  TYPE ty_attr.
    METHODS render_field_radio
      IMPORTING
        !ii_html  TYPE REF TO zif_abapgit_html
        !is_field TYPE ty_field
        !is_attr  TYPE ty_attr.
    METHODS render_field_table
      IMPORTING
        !ii_html   TYPE REF TO zif_abapgit_html
        !is_field  TYPE ty_field
        !is_attr   TYPE ty_attr
        !io_values TYPE REF TO zcl_abapgit_string_map.
    METHODS render_command
      IMPORTING
        !ii_html TYPE REF TO zif_abapgit_html
        !is_cmd  TYPE ty_command.
    METHODS render_field_hidden
      IMPORTING
        !ii_html  TYPE REF TO zif_abapgit_html
        !is_field TYPE ty_field
        !is_attr  TYPE ty_attr.
ENDCLASS.



CLASS zcl_abapgit_html_form IMPLEMENTATION.


  METHOD checkbox.

    DATA ls_field LIKE LINE OF mt_fields.

    ls_field-type  = c_field_type-checkbox.
    ls_field-name  = iv_name.
    ls_field-label = iv_label.
    ls_field-hint  = iv_hint.

    APPEND ls_field TO mt_fields.

    ro_self = me.

  ENDMETHOD.


  METHOD column.

    FIELD-SYMBOLS <ls_last> LIKE LINE OF mt_fields.
    DATA ls_column LIKE LINE OF <ls_last>-subitems.
    DATA lv_size TYPE i.

    lv_size = lines( mt_fields ).
    ASSERT lv_size > 0. " Exception ? Maybe add zcx_no_check ?

    READ TABLE mt_fields INDEX lv_size ASSIGNING <ls_last>.
    ASSERT sy-subrc = 0.
    ASSERT <ls_last>-type = c_field_type-table.

    ls_column-label    = iv_label.
    ls_column-value    = iv_width.
    ls_column-readonly = iv_readonly.

    APPEND ls_column TO <ls_last>-subitems.

    ro_self = me.

  ENDMETHOD.


  METHOD command.

    DATA ls_cmd LIKE LINE OF mt_commands.

    ASSERT iv_cmd_type BETWEEN 1 AND 3.

    ls_cmd-label    = iv_label.
    ls_cmd-action   = iv_action.
    ls_cmd-is_main  = iv_is_main.
    ls_cmd-cmd_type = iv_cmd_type.

    APPEND ls_cmd TO mt_commands.

    ro_self = me.

  ENDMETHOD.


  METHOD create.

    DATA lv_ts TYPE timestampl.

    CREATE OBJECT ro_form.
    ro_form->mv_form_id = iv_form_id.
    ro_form->mv_help_page = iv_help_page.

    IF ro_form->mv_form_id IS INITIAL.
      GET TIME STAMP FIELD lv_ts.
      ro_form->mv_form_id = |form_{ lv_ts }|.
    ENDIF.

  ENDMETHOD.


  METHOD hidden.

    DATA ls_field LIKE LINE OF mt_fields.

    ls_field-type  = c_field_type-hidden.
    ls_field-name  = iv_name.
    APPEND ls_field TO mt_fields.

  ENDMETHOD.


  METHOD is_empty.

    DATA:
      lv_value TYPE string,
      lv_rows  TYPE i,
      lv_row   TYPE i.

    FIELD-SYMBOLS <ls_field> LIKE LINE OF mt_fields.

    rv_empty = abap_true.
    LOOP AT mt_fields ASSIGNING <ls_field> WHERE type <> c_field_type-field_group.
      lv_value = condense(
        val = io_form_data->get( <ls_field>-name )
        del = ` ` ).

      IF <ls_field>-type = c_field_type-number.
        rv_empty = boolc( lv_value IS INITIAL OR lv_value = '0' ).
      ELSEIF <ls_field>-type = c_field_type-table.
        lv_rows = io_form_data->get( |{ <ls_field>-name }-{ c_rows }| ).
        DO lv_rows TIMES.
          lv_row = sy-index.
          DO lines( <ls_field>-subitems ) TIMES.
            lv_value = io_form_data->get( |{ <ls_field>-name }-{ lv_row }-{ sy-index }| ).
            rv_empty = boolc( lv_value IS INITIAL ).
            IF rv_empty <> abap_true.
              RETURN.
            ENDIF.
          ENDDO.
        ENDDO.
      ELSEIF <ls_field>-type = c_field_type-textarea.
        REPLACE ALL OCCURRENCES OF zif_abapgit_definitions=>c_crlf IN lv_value WITH ''.
        REPLACE ALL OCCURRENCES OF zif_abapgit_definitions=>c_newline IN lv_value WITH ''.
        rv_empty = boolc( lv_value IS INITIAL ).
      ELSE.
        rv_empty = boolc( lv_value IS INITIAL ).
      ENDIF.

      IF rv_empty <> abap_true.
        RETURN.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.


  METHOD normalize_form_data.

    DATA:
      lv_value TYPE string,
      lv_rows  TYPE i,
      lv_row   TYPE i,
      lv_len   TYPE i.

    FIELD-SYMBOLS <ls_field> LIKE LINE OF mt_fields.

    CREATE OBJECT ro_form_data.

    LOOP AT mt_fields ASSIGNING <ls_field> WHERE type <> c_field_type-field_group.
      CLEAR lv_value.
      lv_value = io_form_data->get( <ls_field>-name ).

      IF <ls_field>-type = c_field_type-checkbox.
        ro_form_data->set(
          iv_key = <ls_field>-name
          iv_val = boolc( lv_value = 'on' ) ).
      ELSEIF <ls_field>-type = c_field_type-text AND <ls_field>-upper_case = abap_true.
        ro_form_data->set(
          iv_key = <ls_field>-name
          iv_val = to_upper( lv_value ) ).
      ELSEIF <ls_field>-type = c_field_type-number.
        " Numeric value is checked in validation
        ro_form_data->set(
          iv_key = <ls_field>-name
          iv_val = condense( val = lv_value del = ` ` ) ).
      ELSEIF <ls_field>-type = c_field_type-table.
        lv_rows = io_form_data->get( |{ <ls_field>-name }-{ c_rows }| ).
        DO lv_rows TIMES.
          lv_row = sy-index.
          DO lines( <ls_field>-subitems ) TIMES.
            lv_value = io_form_data->get( |{ <ls_field>-name }-{ lv_row }-{ sy-index }| ).
            ro_form_data->set(
              iv_key = |{ <ls_field>-name }-{ lv_row }-{ sy-index }|
              iv_val = lv_value ).
          ENDDO.
        ENDDO.
        ro_form_data->set(
          iv_key = |{ <ls_field>-name }-{ c_rows }|
          iv_val = |{ lv_rows }| ).
      ELSEIF <ls_field>-type = c_field_type-textarea.
        REPLACE ALL OCCURRENCES OF zif_abapgit_definitions=>c_crlf IN lv_value
          WITH zif_abapgit_definitions=>c_newline.

        " Remove last line if empty (ie 2x newline)
        lv_len = strlen( lv_value ) - 2.
        IF lv_len >= 0 AND lv_value+lv_len(1) = zif_abapgit_definitions=>c_newline.
          lv_len = lv_len + 1.
          lv_value = lv_value(lv_len).
        ENDIF.

        ro_form_data->set(
          iv_key = <ls_field>-name
          iv_val = lv_value ).
      ELSE.
        ro_form_data->set(
          iv_key = <ls_field>-name
          iv_val = lv_value ).
      ENDIF.

    ENDLOOP.

  ENDMETHOD.


  METHOD number.

    DATA ls_field LIKE LINE OF mt_fields.

    ls_field-type     = c_field_type-number.
    ls_field-name     = iv_name.
    ls_field-label    = iv_label.
    ls_field-readonly = iv_readonly.
    ls_field-min      = iv_min.
    ls_field-max      = iv_max.
    ls_field-hint     = iv_hint.
    ls_field-required = iv_required.

    APPEND ls_field TO mt_fields.

    ro_self = me.

  ENDMETHOD.


  METHOD option.

    FIELD-SYMBOLS <ls_last> LIKE LINE OF mt_fields.
    DATA ls_option LIKE LINE OF <ls_last>-subitems.
    DATA lv_size TYPE i.

    lv_size = lines( mt_fields ).
    ASSERT lv_size > 0. " Exception ? Maybe add zcx_no_check ?

    READ TABLE mt_fields INDEX lv_size ASSIGNING <ls_last>.
    ASSERT sy-subrc = 0.
    ASSERT <ls_last>-type = c_field_type-radio. " Or dropdown - TODO in future

    ls_option-label = iv_label.
    ls_option-value = iv_value.

    APPEND ls_option TO <ls_last>-subitems.

    ro_self = me.

  ENDMETHOD.


  METHOD radio.

    DATA ls_field LIKE LINE OF mt_fields.

    ls_field-type  = c_field_type-radio.
    ls_field-name  = iv_name.
    ls_field-label = iv_label.
    ls_field-default_value = iv_default_value.
    ls_field-hint  = iv_hint.

    APPEND ls_field TO mt_fields.

    ro_self = me.

  ENDMETHOD.


  METHOD render.

    FIELD-SYMBOLS <ls_field> LIKE LINE OF mt_fields.
    FIELD-SYMBOLS <ls_cmd> LIKE LINE OF mt_commands.
    DATA lv_hint TYPE string.
    DATA ls_form_id TYPE string.
    DATA lv_cur_group TYPE string.
    DATA lv_url TYPE string.

    IF mv_form_id IS NOT INITIAL.
      ls_form_id = | id="{ mv_form_id }"|.
    ENDIF.

    CREATE OBJECT ri_html TYPE zcl_abapgit_html.

    ri_html->add( |<div class="{ iv_form_class }">| ).
    ri_html->add( |<form method="post"{ ls_form_id }>| ).

    " Add hidden button that triggers main command when pressing enter
    LOOP AT mt_commands ASSIGNING <ls_cmd> WHERE is_main = abap_true.
      ri_html->add( |<button type="submit" formaction="sapevent:{ <ls_cmd>-action
                    }" class="hidden-submit" aria-hidden="true" tabindex="-1"></button>| ).
      EXIT.
    ENDLOOP.

    LOOP AT mt_fields ASSIGNING <ls_field>.
      AT FIRST.
        IF <ls_field>-type <> c_field_type-field_group.
          ri_html->add( |<ul>| ).
        ENDIF.
      ENDAT.

      IF <ls_field>-type = c_field_type-field_group.
        IF lv_cur_group IS NOT INITIAL AND lv_cur_group <> <ls_field>-name.
          ri_html->add( |</ul>| ).
          ri_html->add( |</fieldset>| ).
        ENDIF.
        IF <ls_field>-hint IS NOT INITIAL.
          lv_hint = | title="{ <ls_field>-hint }"|.
        ELSE.
          lv_hint = ''.
        ENDIF.
        lv_cur_group = <ls_field>-name.
        ri_html->add( |<fieldset name="{ <ls_field>-name }">| ).
        ri_html->add( |<legend{ lv_hint }>{ <ls_field>-label }</legend>| ).
        ri_html->add( |<ul>| ).
        CONTINUE.
      ENDIF.

      render_field(
        ii_html           = ri_html
        io_values         = io_values
        io_validation_log = io_validation_log
        is_field          = <ls_field> ).

      AT LAST.
        ri_html->add( |</ul>| ).
        IF lv_cur_group IS NOT INITIAL.
          ri_html->add( |</fieldset>| ).
        ENDIF.
      ENDAT.
    ENDLOOP.

    ri_html->add( |<ul>| ).
    ri_html->add( |<li class="dialog-commands">| ).

    IF mv_help_page IS NOT INITIAL.
      lv_url = escape( val    = mv_help_page
                       format = cl_abap_format=>e_url ).
      ri_html->add_a(
        iv_txt   = zcl_abapgit_gui_buttons=>help( )
        iv_act   = |{ zif_abapgit_definitions=>c_action-url }?url={ lv_url }|
        iv_class = 'dialog-help'
        iv_title = 'Help' ).
    ENDIF.

    LOOP AT mt_commands ASSIGNING <ls_cmd>.
      render_command(
        ii_html = ri_html
        is_cmd  = <ls_cmd> ).
    ENDLOOP.

    ri_html->add( |</li>| ).
    ri_html->add( |</ul>| ).
    ri_html->add( |</form>| ).
    ri_html->add( |</div>| ).

  ENDMETHOD.


  METHOD render_command.

    DATA lv_main_submit TYPE string.

    CASE is_cmd-cmd_type.
      WHEN c_cmd_type-link.

        ii_html->add_a(
          iv_txt   = is_cmd-label
          iv_act   = is_cmd-action
          iv_class = 'dialog-commands' ).

      WHEN c_cmd_type-button.

        ii_html->add( |<button type="submit" name="action" value="{
          is_cmd-action }" class="action-commands">{ is_cmd-label }</button>| ).

      WHEN c_cmd_type-input.

        IF is_cmd-is_main = abap_true.
          lv_main_submit = ' class="main"'.
        ELSE.
          CLEAR lv_main_submit.
        ENDIF.
        ii_html->add( |<input type="submit" value="{
          is_cmd-label }"{ lv_main_submit } formaction="sapevent:{ is_cmd-action }">| ).

      WHEN OTHERS.
        ASSERT 0 = 1.

    ENDCASE.

  ENDMETHOD.


  METHOD render_field.

    DATA:
      ls_attr       TYPE ty_attr,
      lv_item_class TYPE string.

    " Get value and validation error
    ls_attr-value = escape( val    = io_values->get( is_field-name )
                            format = cl_abap_format=>e_html_attr ).

    IF io_validation_log IS BOUND.
      ls_attr-error = io_validation_log->get( is_field-name ).
      IF ls_attr-error IS NOT INITIAL.
        ls_attr-error = escape( val    = ls_attr-error
                                format = cl_abap_format=>e_html_text ).
        ls_attr-error = |<small>{ ls_attr-error }</small>|.
      ENDIF.
    ENDIF.

    " Prepare field attributes
    IF is_field-required = abap_true.
      ls_attr-required = ' <em>*</em>'.
    ENDIF.

    IF is_field-hint IS NOT INITIAL.
      ls_attr-hint = escape( val    = is_field-hint
                             format = cl_abap_format=>e_html_attr ).
      ls_attr-hint = | title="{ ls_attr-hint }"|.
    ENDIF.

    IF is_field-placeholder IS NOT INITIAL.
      ls_attr-placeholder = escape( val    = is_field-placeholder
                                    format = cl_abap_format=>e_html_attr ).
      ls_attr-placeholder = | placeholder="{ ls_attr-placeholder }"|.
    ENDIF.

    IF is_field-readonly = abap_true.
      ls_attr-readonly = ' readonly'.
    ENDIF.

    " Prepare item class
    lv_item_class = is_field-item_class.
    IF ls_attr-error IS NOT INITIAL.
      lv_item_class = condense( lv_item_class && ' error' ).
    ENDIF.
    IF is_field-type = c_field_type-text AND is_field-max BETWEEN 1 AND 20.
      " Reduced width for short fields
      lv_item_class = lv_item_class && ' w40'.
    ENDIF.
    IF lv_item_class IS NOT INITIAL.
      lv_item_class = | class="{ lv_item_class }"|.
    ENDIF.

    " Render field
    ii_html->add( |<li{ lv_item_class }>| ).

    CASE is_field-type.
      WHEN c_field_type-text OR c_field_type-number.

        render_field_text(
          ii_html  = ii_html
          is_field = is_field
          is_attr  = ls_attr ).

      WHEN c_field_type-textarea.

        render_field_textarea(
          ii_html  = ii_html
          is_field = is_field
          is_attr  = ls_attr ).

      WHEN c_field_type-checkbox.

        render_field_checkbox(
          ii_html  = ii_html
          is_field = is_field
          is_attr  = ls_attr ).

      WHEN c_field_type-radio.

        render_field_radio(
          ii_html  = ii_html
          is_field = is_field
          is_attr  = ls_attr ).

      WHEN c_field_type-table.

        render_field_table(
          ii_html   = ii_html
          is_field  = is_field
          is_attr   = ls_attr
          io_values = io_values ).

      WHEN c_field_type-hidden.

        render_field_hidden(
          ii_html  = ii_html
          is_field = is_field
          is_attr  = ls_attr ).

      WHEN OTHERS.
        ASSERT 1 = 0.
    ENDCASE.

    ii_html->add( '</li>' ).

  ENDMETHOD.


  METHOD render_field_checkbox.

    DATA lv_checked TYPE string.

    IF is_attr-error IS NOT INITIAL.
      ii_html->add( is_attr-error ).
    ENDIF.

    IF is_attr-value = abap_true OR is_attr-value = 'on'.
      " boolc return ` ` which is not initial -> bug after 1st validation
      lv_checked = ' checked'.
    ENDIF.

    ii_html->add( |<input type="checkbox" name="{ is_field-name }" id="{ is_field-name }"{ lv_checked }>| ).
    ii_html->add( |<label for="{ is_field-name }"{ is_attr-hint }>{ is_field-label }</label>| ).

  ENDMETHOD.


  METHOD render_field_hidden.

    ii_html->add( |<input type="hidden" name="{ is_field-name }" id="{
                  is_field-name }" value="{ is_attr-value }">| ).

  ENDMETHOD.


  METHOD render_field_radio.

    DATA:
      lv_value     TYPE string,
      lv_checked   TYPE string,
      lv_opt_id    TYPE string,
      lv_opt_value TYPE string.

    FIELD-SYMBOLS <ls_opt> LIKE LINE OF is_field-subitems.

    ii_html->add( |<label{ is_attr-hint }>{ is_field-label }</label>| ).

    IF is_attr-error IS NOT INITIAL.
      ii_html->add( is_attr-error ).
    ENDIF.

    ii_html->add( |<div class="radio-container">| ).

    LOOP AT is_field-subitems ASSIGNING <ls_opt>.
      lv_opt_value = escape( val    = <ls_opt>-value
                             format = cl_abap_format=>e_html_attr ).

      CLEAR lv_checked.
      IF is_attr-value = lv_opt_value OR ( is_attr-value IS INITIAL AND lv_opt_value = is_field-default_value ).
        lv_checked = ' checked'.
      ENDIF.

      lv_opt_id = |{ is_field-name }{ sy-tabix }|.
      ii_html->add( |<input type="radio" name="{ is_field-name }" id="{
                    lv_opt_id }" value="{ lv_opt_value }"{ lv_checked }>| ).
      ii_html->add( |<label for="{ lv_opt_id }">{ <ls_opt>-label }</label>| ).
    ENDLOOP.

    ii_html->add( '</div>' ).

  ENDMETHOD.


  METHOD render_field_table.

    DATA:
      lv_value     TYPE string,
      lv_readonly  TYPE string,
      lv_rows      TYPE i,
      lv_cell_id   TYPE string,
      lv_opt_value TYPE string.

    FIELD-SYMBOLS <ls_subitem> LIKE LINE OF is_field-subitems.

    ii_html->add( |<label for="{ is_field-name }"{ is_attr-hint }>{ is_field-label }</label>| ).

    IF is_attr-error IS NOT INITIAL.
      ii_html->add( is_attr-error ).
    ENDIF.

    ii_html->add( |<table name="{ is_field-name }" id="{ is_field-name }" class="table-container">| ).

    ii_html->add( |<thead>| ).
    ii_html->add( |<tr>| ).
    LOOP AT is_field-subitems ASSIGNING <ls_subitem>.
      CLEAR lv_value.
      IF <ls_subitem>-value IS NOT INITIAL.
        lv_value = escape( val    = <ls_subitem>-value
                           format = cl_abap_format=>e_html_attr ).
        lv_value = | width="{ lv_value }"|.
      ENDIF.
      ii_html->add( |<td{ lv_value }>{ <ls_subitem>-label }</td>| ).
    ENDLOOP.
    ii_html->add( |</tr>| ).
    ii_html->add( |</thead>| ).

    lv_rows = io_values->get( |{ is_field-name }-{ c_rows }| ).

    ii_html->add( |<tbody>| ).
    DO lv_rows TIMES.
      lv_rows = sy-index.
      ii_html->add( |<tr>| ).
      LOOP AT is_field-subitems ASSIGNING <ls_subitem>.
        lv_cell_id = |{ is_field-name }-{ lv_rows }-{ sy-tabix }|.
        lv_value = escape( val    = io_values->get( lv_cell_id )
                           format = cl_abap_format=>e_html_attr ).
        CLEAR lv_readonly.
        IF <ls_subitem>-readonly = abap_true.
          lv_readonly = | readonly|.
        ENDIF.
        ii_html->add( |<td><input type="text" name="{ lv_cell_id }" id="{
                      lv_cell_id }" value="{ lv_value }"{ lv_readonly }></td>| ).
      ENDLOOP.
      ii_html->add( |</tr>| ).
    ENDDO.
    ii_html->add( |</tbody>| ).

    ii_html->add( |</table>| ).

    " Hidden field with number of rows to simplify getting values from form
    lv_value = |{ is_field-name }-{ c_rows }|.
    ii_html->add( |<input type="number" name="{ lv_value }" id="{
                  lv_value }" value="{ lv_rows }" style="display:none">| ).

  ENDMETHOD.


  METHOD render_field_text.

    DATA lv_type TYPE string.

    ii_html->add( |<label for="{ is_field-name }"{ is_attr-hint }>{
                  is_field-label }{ is_attr-required }</label>| ).

    IF is_attr-error IS NOT INITIAL.
      ii_html->add( is_attr-error ).
    ENDIF.

    IF is_field-side_action IS NOT INITIAL.
      ii_html->add( '<div class="input-container">' ). " Ugly :(
    ENDIF.

    IF is_field-type = c_field_type-number.
      lv_type = 'number'.
    ELSEIF is_field-password = abap_true.
      lv_type = 'password'.
    ELSE.
      lv_type = 'text'.
    ENDIF.

    ii_html->add( |<input type="{ lv_type }" name="{ is_field-name }" id="{
                  is_field-name }" value="{ is_attr-value }" { is_field-dblclick }{
                  is_attr-placeholder }{ is_attr-readonly }>| ).

    IF is_field-side_action IS NOT INITIAL.
      ii_html->add( '</div>' ).
      ii_html->add( '<div class="command-container">' ).
      ii_html->add( |<input type="submit" value="&#x2026;" formaction="sapevent:{ is_field-side_action }">| ).
      ii_html->add( '</div>' ).
    ENDIF.

  ENDMETHOD.


  METHOD render_field_textarea.

    DATA lv_rows TYPE i.

    ii_html->add( |<label for="{ is_field-name }"{ is_attr-hint }>{
                  is_field-label }{ is_attr-required }</label>| ).

    IF is_attr-error IS NOT INITIAL.
      ii_html->add( is_attr-error ).
    ENDIF.

    lv_rows = lines( zcl_abapgit_convert=>split_string( is_attr-value ) ).

    ii_html->add( |<textarea name="{ is_field-name }" id="{
                  is_field-name }" rows="{ lv_rows }"{ is_attr-readonly }>| ).
    ii_html->add( escape( val    = is_attr-value
                          format = cl_abap_format=>e_html_attr ) ).
    ii_html->add( |</textarea>| ).

  ENDMETHOD.


  METHOD start_group.

    DATA ls_field LIKE LINE OF mt_fields.

    ls_field-type  = c_field_type-field_group.
    ls_field-label = iv_label.
    ls_field-name  = iv_name.
    ls_field-hint  = iv_hint.

    APPEND ls_field TO mt_fields.

    ro_self = me.

  ENDMETHOD.


  METHOD table.

    DATA ls_field LIKE LINE OF mt_fields.

    ls_field-type  = c_field_type-table.
    ls_field-name  = iv_name.
    ls_field-label = iv_label.
    ls_field-hint  = iv_hint.

    APPEND ls_field TO mt_fields.

    ro_self = me.

  ENDMETHOD.


  METHOD text.

    DATA ls_field LIKE LINE OF mt_fields.

    ls_field-type       = c_field_type-text.
    ls_field-name       = iv_name.
    ls_field-label      = iv_label.
    ls_field-upper_case = iv_upper_case.
    ls_field-readonly   = iv_readonly.
    ls_field-min        = iv_min.
    ls_field-max        = iv_max.
    ls_field-password   = iv_password.
    ls_field-hint       = iv_hint.
    ls_field-required   = iv_required.
    ls_field-placeholder = iv_placeholder.

    IF iv_side_action IS NOT INITIAL AND mv_form_id IS NOT INITIAL.
      ls_field-item_class = 'with-command'.
      ls_field-side_action = iv_side_action.
      ls_field-dblclick = | ondblclick="document.getElementById('{ mv_form_id
        }').action = 'sapevent:{ iv_side_action
        }'; document.getElementById('{ mv_form_id
        }').submit()"|.
    ENDIF.

    APPEND ls_field TO mt_fields.

    ro_self = me.

  ENDMETHOD.


  METHOD textarea.

    DATA ls_field LIKE LINE OF mt_fields.

    ls_field-type        = c_field_type-textarea.
    ls_field-name        = iv_name.
    ls_field-label       = iv_label.
    ls_field-readonly    = iv_readonly.
    ls_field-hint        = iv_hint.
    ls_field-required    = iv_required.
    ls_field-placeholder = iv_placeholder.

    APPEND ls_field TO mt_fields.

    ro_self = me.

  ENDMETHOD.


  METHOD validate_required_fields.

    DATA lv_value TYPE string.
    DATA lv_number TYPE i.
    FIELD-SYMBOLS <ls_field> LIKE LINE OF mt_fields.

    CREATE OBJECT ro_validation_log.

    LOOP AT mt_fields ASSIGNING <ls_field>.
      lv_value = io_form_data->get( <ls_field>-name ).
      IF <ls_field>-required IS NOT INITIAL AND lv_value IS INITIAL.
        ro_validation_log->set(
          iv_key = <ls_field>-name
          iv_val = |{ <ls_field>-label } cannot be empty| ).
      ENDIF.
      CASE <ls_field>-type.
        WHEN c_field_type-text.
          IF <ls_field>-min <> cl_abap_math=>min_int4 AND strlen( lv_value ) < <ls_field>-min.
            ro_validation_log->set(
              iv_key = <ls_field>-name
              iv_val = |{ <ls_field>-label } must not be shorter than { <ls_field>-min } characters| ).
          ENDIF.
          IF <ls_field>-max <> cl_abap_math=>max_int4 AND strlen( lv_value ) > <ls_field>-max.
            ro_validation_log->set(
              iv_key = <ls_field>-name
              iv_val = |{ <ls_field>-label } must not be longer than { <ls_field>-max } characters| ).
          ENDIF.
        WHEN c_field_type-number.
          TRY.
              lv_number = lv_value.
            CATCH cx_root.
              ro_validation_log->set(
                iv_key = <ls_field>-name
                iv_val = |{ <ls_field>-label } is not numeric| ).
              CONTINUE.
          ENDTRY.
          IF <ls_field>-min <> cl_abap_math=>min_int4 AND lv_number < <ls_field>-min.
            ro_validation_log->set(
              iv_key = <ls_field>-name
              iv_val = |{ <ls_field>-label } must not be lower than { <ls_field>-min }| ).
          ENDIF.
          IF <ls_field>-max <> cl_abap_math=>max_int4 AND lv_number > <ls_field>-max.
            ro_validation_log->set(
              iv_key = <ls_field>-name
              iv_val = |{ <ls_field>-label } must not be higher than { <ls_field>-max }| ).
          ENDIF.
      ENDCASE.
    ENDLOOP.

  ENDMETHOD.
ENDCLASS.