*----------------------------------------------------------------------*
*       CLASS ZCL_CA_ALV DEFINITION
*----------------------------------------------------------------------*
*
*----------------------------------------------------------------------*
CLASS zcl_ca_alv DEFINITION
  PUBLIC
  CREATE PUBLIC .

  PUBLIC SECTION.
*"* public components of class ZCL_CA_ALV
*"* do not include other source files here!!!

    INTERFACES if_salv_c_aggregation .
    INTERFACES if_salv_c_alignment .
    INTERFACES if_salv_events_actions_table .
    INTERFACES if_salv_events_functions .
    INTERFACES if_salv_events_list .

    ALIASES added_function
      FOR if_salv_events_functions~added_function .
    ALIASES after_salv_function
      FOR if_salv_events_functions~after_salv_function .
    ALIASES before_salv_function
      FOR if_salv_events_functions~before_salv_function .
    ALIASES double_click
      FOR if_salv_events_actions_table~double_click .
    ALIASES end_of_page
      FOR if_salv_events_list~end_of_page .
    ALIASES link_click
      FOR if_salv_events_actions_table~link_click .
    ALIASES top_of_page
      FOR if_salv_events_list~top_of_page .

    DATA cl_lista_funciones TYPE REF TO cl_salv_functions_list .
    CLASS-DATA dc_cab_tipo_etiqueta TYPE i VALUE 1.       "#EC NOTEXT .
    CLASS-DATA cv_header_flow_type TYPE i VALUE 2.        "#EC NOTEXT .
    CLASS-DATA dc_cab_tipo_header TYPE i VALUE 3.         "#EC NOTEXT .
    CLASS-DATA dc_cab_tipo_info TYPE i VALUE 4.           "#EC NOTEXT .
    CLASS-DATA dc_cab_tipo_texto TYPE i VALUE 5.          "#EC NOTEXT .
    CLASS-DATA dc_functions_all TYPE salv_de_constant VALUE 2. "#EC NOTEXT .
    CLASS-DATA dc_functions_default TYPE salv_de_constant VALUE 1. "#EC NOTEXT .
    CLASS-DATA dc_functions_none TYPE salv_de_constant VALUE 0. "#EC NOTEXT .

    METHODS create_alv
      IMPORTING
        !iv_list_mode      TYPE sap_bool DEFAULT if_salv_c_bool_sap=>false
        !io_container      TYPE REF TO cl_gui_container OPTIONAL
        !iv_container_name TYPE string OPTIONAL
        !iv_program        TYPE syrepid
      CHANGING
        !ct_data           TYPE table
      EXCEPTIONS
        error_create_alv .
    METHODS evt_added_function
          FOR EVENT added_function OF cl_salv_events_table
      IMPORTING
          !e_salv_function .
    METHODS evt_after_salv_function
          FOR EVENT if_salv_events_functions~after_salv_function OF cl_salv_events_table
      IMPORTING
          !e_salv_function .
    METHODS evt_before_salv_function
          FOR EVENT if_salv_events_functions~before_salv_function OF cl_salv_events_table
      IMPORTING
          !e_salv_function .
    METHODS evt_double_click
          FOR EVENT if_salv_events_actions_table~double_click OF cl_salv_events_table
      IMPORTING
          !row
          !column .
    METHODS evt_end_of_page
          FOR EVENT if_salv_events_list~end_of_page OF cl_salv_events_table
      IMPORTING
          !r_end_of_page
          !page .
    METHODS evt_link_click
          FOR EVENT if_salv_events_actions_table~link_click OF cl_salv_events_table
      IMPORTING
          !row
          !column .
    METHODS evt_top_of_page
          FOR EVENT if_salv_events_list~top_of_page OF cl_salv_events_table
      IMPORTING
          !r_top_of_page
          !page
          !table_index .
    METHODS get_alv
      RETURNING
        VALUE(ro_alv) TYPE REF TO cl_salv_table .
    METHODS get_rows_sel
      RETURNING
        VALUE(rt_rows) TYPE salv_t_row .
    METHODS show_alv .
    METHODS refresh_alv
      IMPORTING
        !iv_stable_row   TYPE lvc_rowst DEFAULT 'X'
        !iv_stable_col   TYPE lvc_colst DEFAULT 'X'
        !iv_refresh_mode TYPE salv_de_constant DEFAULT if_salv_c_refresh=>soft .
    METHODS set_alv
      IMPORTING
        !io_alv TYPE REF TO cl_salv_table .
    METHODS set_field_properties
      IMPORTING
        !iv_field           TYPE lvc_fname
        !iv_symbol          TYPE sap_bool OPTIONAL
        !iv_visible         TYPE sap_bool OPTIONAL
        !iv_all_text        TYPE scrtext_l OPTIONAL
        !iv_medium_text     TYPE scrtext_m OPTIONAL
        !iv_long_text       TYPE scrtext_l OPTIONAL
        !iv_short_text      TYPE scrtext_s OPTIONAL
        !iv_output_leng     TYPE lvc_outlen OPTIONAL
        !is_color           TYPE lvc_s_colo OPTIONAL
        !iv_cell_type       TYPE salv_de_celltype OPTIONAL
        !iv_technical       TYPE sap_bool OPTIONAL
        !iv_currency_field  TYPE lvc_cfname OPTIONAL
        !iv_unit_field      TYPE lvc_qfname OPTIONAL
        !i_optimized        TYPE sap_bool OPTIONAL
        !iv_ddic_reference  TYPE salv_s_ddic_reference OPTIONAL
        !iv_position        TYPE i OPTIONAL
        !iv_decimals        TYPE lvc_decmls OPTIONAL
        !iv_set_aggregation TYPE salv_de_aggregation OPTIONAL
        !iv_zero            TYPE sap_bool OPTIONAL
        !iv_alignment       TYPE salv_de_alignment OPTIONAL
        !iv_key             TYPE sap_bool OPTIONAL
        !iv_edit_mask       TYPE lvc_edtmsk OPTIONAL .
    METHODS set_header_page
      IMPORTING
        !iv_row        TYPE i
        !iv_column     TYPE i
        !iv_field_type TYPE i DEFAULT zcl_ca_alv=>cv_header_flow_type
        !iv_text       TYPE any
        !iv_list       TYPE sap_bool DEFAULT if_salv_c_bool_sap=>true .
    METHODS set_field_color
      IMPORTING
        !iv_field TYPE lvc_fname .
    METHODS set_symbol_field
      IMPORTING
        !iv_field  TYPE lvc_fname
        !iv_active TYPE sap_bool DEFAULT if_salv_c_bool_sap=>true .
    METHODS set_optimized_cols
      IMPORTING
        !iv_active TYPE sap_bool DEFAULT if_salv_c_bool_sap=>false .
    METHODS set_function
      IMPORTING
        !iv_function TYPE salv_de_function
        !i_boolean   TYPE sap_bool .
    METHODS set_alv_functions
      IMPORTING
        !iv_active TYPE sap_bool DEFAULT if_salv_c_bool_sap=>false
          PREFERRED PARAMETER iv_active .
    METHODS set_manag_layout
      IMPORTING
        !iv_restriction TYPE salv_de_layout_restriction DEFAULT if_salv_c_layout=>restrict_none .
    METHODS set_layout
      IMPORTING
        !iv_layout TYPE slis_vari .
    METHODS set_selection_mode
      IMPORTING
        !iv_method TYPE salv_de_constant DEFAULT if_salv_c_selection_mode=>none .
    METHODS set_zebra_mode
      IMPORTING
        !iv_active TYPE sap_bool DEFAULT if_salv_c_bool_sap=>false .
    METHODS set_pfstatus
      IMPORTING
        !iv_pfstatus  TYPE sypfkey
        !iv_functions TYPE salv_de_constant DEFAULT dc_functions_all .
    METHODS set_footer_page
      IMPORTING
        !iv_row        TYPE i
        !iv_column     TYPE i
        !iv_field_type TYPE i DEFAULT zcl_ca_alv=>cv_header_flow_type
        !iv_text       TYPE any
        !iv_list       TYPE sap_bool DEFAULT if_salv_c_bool_sap=>true .
    METHODS set_title
      IMPORTING
        !iv_title TYPE lvc_title .
    METHODS get_events
      RETURNING
        VALUE(ro_events) TYPE REF TO cl_salv_events_table .
    METHODS get_print
      EXPORTING
        !iv_value TYPE REF TO cl_salv_print .
    METHODS remove_selections .
    METHODS set_screen_popup
      IMPORTING
        !iv_start_column TYPE i
        !iv_end_column   TYPE i
        !iv_start_line   TYPE i
        !iv_end_line     TYPE i .
    METHODS add_function
      IMPORTING
        !iv_name     TYPE any
        !iv_icon     TYPE any OPTIONAL
        !iv_text     TYPE any OPTIONAL
        !iv_tooltip  TYPE any OPTIONAL
        !iv_position TYPE salv_de_function_pos DEFAULT if_salv_c_function_position=>right_of_salv_functions .
    METHODS add_sort
      IMPORTING
        !iv_columnname          TYPE lvc_fname
        !iv_position            TYPE i OPTIONAL
        !iv_sequence            TYPE salv_de_sort_sequence DEFAULT if_salv_c_sort=>sort_up
        !iv_subtotal            TYPE sap_bool DEFAULT if_salv_c_bool_sap=>false
        !iv_group               TYPE salv_de_sort_group DEFAULT if_salv_c_sort=>group_none
        !iv_mandatory           TYPE sap_bool DEFAULT if_salv_c_bool_sap=>false
        !iv_compressed_subtotal TYPE sap_bool DEFAULT if_salv_c_bool_sap=>false
      RETURNING
        VALUE(ro_value)         TYPE REF TO cl_salv_sort .
    METHODS set_celltype
      IMPORTING
        !iv_field TYPE lvc_fname .
    METHODS remove_function
      IMPORTING
        !iv_name TYPE any .
*"* protected components of class ZZC_CA00501
*"* do not include other source files here!!!
  PROTECTED SECTION.

    DATA mo_alv TYPE REF TO cl_salv_table .
    DATA mo_alv_msg TYPE REF TO cx_salv_msg .
    DATA mo_cabecera TYPE REF TO cl_salv_form_layout_grid .
    DATA mo_column TYPE REF TO cl_salv_column_table .
    DATA mo_columns TYPE REF TO cl_salv_columns_table .
    DATA mo_display TYPE REF TO cl_salv_display_settings .
    DATA mo_label TYPE REF TO cl_salv_form_label .
    DATA mo_events TYPE REF TO cl_salv_events_table .
    DATA mo_functions TYPE REF TO cl_salv_functions .
    DATA mo_header TYPE REF TO cl_salv_form_header_info .
    DATA mo_info TYPE REF TO cl_salv_form_action_info .
    DATA mo_layout TYPE REF TO cl_salv_layout .
    DATA mo_layout_flow TYPE REF TO cl_salv_form_layout_flow .
    DATA mo_footer TYPE REF TO cl_salv_form_layout_grid .
    DATA mo_selections TYPE REF TO cl_salv_selections .
    DATA mo_texto TYPE REF TO cl_salv_form_text .
    DATA mo_ordenacion TYPE REF TO cl_salv_sorts .
    DATA mv_repid TYPE syrepid .
    DATA ms_layout_key TYPE salv_s_layout_key .
    DATA ms_color TYPE lvc_s_scol .
    DATA ms_aggregation TYPE REF TO cl_salv_aggregations .

    METHODS set_alv_class .
    METHODS set_events .
    METHODS set_field_texts
      IMPORTING
        !iv_field       TYPE lvc_fname
        !iv_all_text    TYPE scrtext_l OPTIONAL
        !iv_medium_text TYPE scrtext_m OPTIONAL
        !iv_long_text   TYPE scrtext_l OPTIONAL
        !iv_short_text  TYPE scrtext_s OPTIONAL .
    METHODS set_page_field_type
      IMPORTING
        !iv_row        TYPE i
        !iv_column     TYPE i
        !iv_field_type TYPE i DEFAULT zcl_ca_alv=>cv_header_flow_type
        !iv_text       TYPE any .
*"* private components of class ZCL_CA_ALV
*"* do not include other source files here!!!
  PRIVATE SECTION.
ENDCLASS.



CLASS zcl_ca_alv IMPLEMENTATION.


  METHOD add_function.


    DATA ld_icon TYPE string.
    DATA ld_text TYPE string.
    DATA ld_tooltip TYPE string.
    DATA ld_name TYPE salv_de_function.
    TRY.

        "El campo de entrada icono es de cualquier tipo para poder se llamado directamente
        "a través del type-pools: ICON. Pero aquí lo convierto para poder ser llamado al método estándar
        ld_icon = iv_icon.

        "Hago lo mismo para el resto de campos.
        ld_text = iv_text.
        ld_tooltip = iv_tooltip.
        ld_name = iv_name.

        cl_lista_funciones->add_function( name     = ld_name
                                          icon     = ld_icon
                                          text     = ld_text
                                          tooltip  = ld_tooltip
                                          position = iv_position ).
      CATCH cx_salv_existing .
        MESSAGE s000(fb) WITH TEXT-e02 iv_name.
      CATCH cx_salv_wrong_call .
        MESSAGE s000(fb) WITH TEXT-e02 iv_name.
    ENDTRY.

  ENDMETHOD.


  METHOD add_sort.

    TRY.
        CALL METHOD mo_ordenacion->add_sort
          EXPORTING
            columnname = iv_columnname
            position   = iv_position
            sequence   = iv_sequence
            subtotal   = iv_subtotal
            group      = iv_group
            obligatory = iv_mandatory
          RECEIVING
            value      = ro_value.

        IF iv_compressed_subtotal IS SUPPLIED.
          mo_ordenacion->set_compressed_subtotal( iv_columnname ).
        ENDIF.

      CATCH cx_salv_not_found .
      CATCH cx_salv_existing .
      CATCH cx_salv_data_error .
    ENDTRY.


  ENDMETHOD.


  METHOD create_alv.

    "La instanciación de la clase se hace entre un TRY..CATCH para
    "poder capturar cualquier excepción.
    TRY.

        "Al método estático que instancia la clase con el ALV se le pasa la tabla
        "de datos y la clase propiamente dicha.
        "La llamada dependerá si se ha pasado la información del container donde se
        "mostrará el ALV.
        IF io_container IS SUPPLIED.

          CALL METHOD cl_salv_table=>factory
            EXPORTING
              r_container    = io_container
              container_name = iv_container_name
            IMPORTING
              r_salv_table   = mo_alv
            CHANGING
              t_table        = ct_data.

        ELSE.

          CALL METHOD cl_salv_table=>factory
            EXPORTING
              list_display = iv_list_mode
            IMPORTING
              r_salv_table = mo_alv
            CHANGING
              t_table      = ct_data.

        ENDIF.

        "Inicializo las clases que servirán para ir ajustando el ALV
        me->set_alv_class( ).

        "Activo la escucha de los eventos
        me->set_events( ).

        "Guardo el programa pasado
        mv_repid = iv_program.

        "paso el nombre del programa a la estructura clave
        "que es usada en otras partes del programa.
        ms_layout_key-report = mv_repid.

      "La excepción es pasada a la clase CL_ALV_MSG.
      CATCH cx_salv_msg INTO mo_alv_msg.

        "En este caso se muestra el mensaje de error pero se podría hacer
        "cualquier otra cosa.
        MESSAGE mo_alv_msg TYPE 'I'.

        RAISE error_create_alv.

    ENDTRY.

  ENDMETHOD.


  METHOD evt_added_function.

    "Lanzo el evento added_function
    RAISE EVENT added_function
      EXPORTING
        e_salv_function = e_salv_function.

  ENDMETHOD.


  METHOD evt_after_salv_function.

    "Lanzo la función after_salv_function
    RAISE EVENT after_salv_function
      EXPORTING
        e_salv_function = e_salv_function.

  ENDMETHOD.


  METHOD evt_before_salv_function.

    "Lanzo el evento before_salv_function
    RAISE EVENT before_salv_function
      EXPORTING
        e_salv_function = e_salv_function.

  ENDMETHOD.


  METHOD evt_double_click.

    "Lanzo el evento de doble click
    RAISE EVENT double_click
      EXPORTING
        row    = row
        column = column.

  ENDMETHOD.


  METHOD evt_end_of_page.

    "Lanzo el evento end of page
    RAISE EVENT end_of_page
      EXPORTING
        r_end_of_page = r_end_of_page
        page          = page.

  ENDMETHOD.


  METHOD evt_link_click.

    "Lanzo el evento "link click".
    RAISE EVENT link_click
      EXPORTING
        row    = row
        column = column.

  ENDMETHOD.


  METHOD evt_top_of_page.

    "Lanzo el evento de cabecera de página
    RAISE EVENT top_of_page
      EXPORTING
        r_top_of_page = r_top_of_page
        page          = page
        table_index   = table_index.

  ENDMETHOD.


  METHOD get_alv.

    ro_alv = mo_alv.

  ENDMETHOD.


  METHOD get_events.

    ro_events = mo_events.

  ENDMETHOD.


  METHOD get_print.

    CALL METHOD mo_alv->get_print
      RECEIVING
        value = iv_value.

  ENDMETHOD.


  METHOD get_rows_sel.

    "Recupero las filas seleccionadas
    rt_rows = mo_selections->get_selected_rows( ).

  ENDMETHOD.


  METHOD refresh_alv.

    DATA ls_stable  TYPE lvc_s_stbl.

    ls_stable-row = iv_stable_row.
    ls_stable-col = iv_stable_col.

    mo_alv->refresh( EXPORTING s_stable = ls_stable refresh_mode = iv_refresh_mode ).

  ENDMETHOD.


  METHOD remove_function.
    DATA ld_name TYPE salv_de_function.

    ld_name = iv_name.
    TRY.
        cl_lista_funciones->remove_function( name = ld_name ).
      CATCH cx_root.
    ENDTRY.
  ENDMETHOD.


  METHOD remove_selections.
    DATA: lt_rows TYPE salv_t_row.

    mo_selections->set_selected_rows( value = lt_rows ).


  ENDMETHOD.


  METHOD set_alv.

    mo_alv = io_alv.

    "Vuelvo a inicializar las clases que servirán para ir ajustando el ALV
    me->set_alv_class( ).

  ENDMETHOD.


  METHOD set_alv_class.

    "Cambiar propiedades de las columnas en general
    mo_columns = mo_alv->get_columns( ).

    "Apariencia de la ALV
    mo_display = mo_alv->get_display_settings( ).

    "Selecciones
    mo_selections = mo_alv->get_selections( ).

    "Gestión de eventos
    mo_events = mo_alv->get_event( ).

    "Layout del ALV
    mo_layout = mo_alv->get_layout( ).

    "Recupero la funciones del ALV
    mo_functions = mo_alv->get_functions( ).

    "Recupero la lista de funciones del ALV, es decir, botones del PF-STATUS.
    cl_lista_funciones = mo_alv->get_functions( ).

    "Recupero la clase para hacer avergaes, sumas, mínimos y máximos
    ms_aggregation = mo_alv->get_aggregations( ).

    "Recupero la clase para realizar ordenaciones por defecto en el listado
    mo_ordenacion = mo_alv->get_sorts( ).

    "Instancio la clase que servira para pintar la cabecera
    "CREATE OBJECT cl_cabecera.

    "Instancio la clase que servira para pintar el pie de página
    "CREATE OBJECT cl_pie.

  ENDMETHOD.


  METHOD set_alv_functions.

    "Activan todas las funciones
    mo_functions->set_all( iv_active ).

  ENDMETHOD.


  METHOD set_celltype.
    TRY.
        mo_columns->set_cell_type_column( iv_field ).
      CATCH cx_root.
    ENDTRY.
  ENDMETHOD.


  METHOD set_events.

    "Activo la escucha del evento "user_command".
    SET HANDLER
              me->evt_added_function FOR mo_events.

    "Activo la escucha del evento "doble click".
    SET HANDLER
              me->evt_double_click FOR mo_events.

    "Activo la escucha del evento cuando se pulse un enlace o botón
    SET HANDLER
              me->evt_link_click FOR mo_events.

    "Activo el evento de cabecera de página
    SET HANDLER
              me->evt_top_of_page FOR mo_events.

    "Activo el evento de pie de página
    SET HANDLER
              me->evt_end_of_page FOR mo_events.

    "Activo el evento "Before salv function"
    SET HANDLER
              me->evt_before_salv_function FOR mo_events.

    "Activo el evento "After salv function"
    SET HANDLER
              me->evt_after_salv_function FOR mo_events.

  ENDMETHOD.


  METHOD set_field_color.

    "Indica el campo que indicará el color de una fila
    mo_columns->set_color_column( iv_field ).

  ENDMETHOD.


  METHOD set_field_properties.

    TRY.

        "Recupero los atributos del campo
        mo_column ?= mo_columns->get_column( iv_field ).

        "Simbolo del campo
        IF iv_symbol IS SUPPLIED.
          mo_column->set_symbol( iv_symbol ).
        ENDIF.

        "Visibilidad del campo
        IF iv_visible IS SUPPLIED.
          mo_column->set_visible( iv_visible ).
        ENDIF.

        "Llamo al método que actualiza las denominaciones del campo
        CALL METHOD set_field_texts
          EXPORTING
            iv_field       = iv_field
            iv_all_text    = iv_all_text
            iv_medium_text = iv_medium_text
            iv_long_text   = iv_long_text
            iv_short_text  = iv_short_text.

        "Pongo la longitud de salida
        IF iv_output_leng IS SUPPLIED.
          mo_column->set_output_length( iv_output_leng ).
        ENDIF.

        "Pongo el color del campo
        IF is_color IS SUPPLIED.
          mo_column->set_color( is_color ).
        ENDIF.

        "Pongo el tipo de campo:
        IF iv_cell_type IS SUPPLIED.
        "Los posibles valores se definen en la interface: IF_SALV_C_CELL_TYPE
          mo_column->set_cell_type( iv_cell_type ).
        ENDIF.

        "Pongo si el campo es técnico, es decir, no saldrá el ALV, ni siquiera en
        "el pool de campos
        IF iv_technical IS SUPPLIED.
          mo_column->set_technical( iv_technical ).
        ENDIF.

        "Pongo el campo de importe si esta informado
        IF iv_currency_field IS SUPPLIED.
          mo_column->set_currency_column( iv_currency_field ).
        ENDIF.

        "Pongo el campo de cantidad si esta informado
        IF iv_unit_field IS SUPPLIED.
          mo_column->set_quantity_column( iv_unit_field ).
        ENDIF.

        "Pongo el atibuto optimizar a la columna
        IF i_optimized IS SUPPLIED.
          mo_column->set_optimized( i_optimized ).
        ENDIF.

        "Referencia al diccionario
        IF iv_ddic_reference IS SUPPLIED.
          mo_column->set_ddic_reference( iv_ddic_reference  ).
        ENDIF.

        "Posicion
        IF iv_position IS SUPPLIED.
          mo_columns->set_column_position( columnname = iv_field position = iv_position ).
        ENDIF.

        "Decimales
        IF iv_decimals IS SUPPLIED.
          mo_column->set_decimals( iv_decimals  ).
        ENDIF.

        "Sumatorio
        IF iv_set_aggregation IS SUPPLIED.
          ms_aggregation->add_aggregation( columnname = iv_field
                                           aggregation = iv_set_aggregation ).
        ENDIF.

        "Sin ceros en celdas vacias
        IF iv_zero IS SUPPLIED.
          mo_column->set_zero( iv_zero ).
        ENDIF.

        "Alineación
        IF iv_alignment IS SUPPLIED.
          mo_column->set_alignment( iv_alignment ).
        ENDIF.

        "Campo clave
        IF iv_key IS SUPPLIED.
          mo_column->set_key( iv_key ).
        ENDIF.

        "Mascara de edicion
        IF iv_edit_mask IS SUPPLIED.
          mo_column->set_edit_mask( iv_edit_mask ).
        ENDIF.


      CATCH cx_salv_not_found.                          "#EC NO_HANDLER
    ENDTRY.

  ENDMETHOD.


  METHOD set_field_texts.
    DATA: d_texto_corto TYPE scrtext_s,
          d_texto_medio TYPE scrtext_m,
          d_texto_largo TYPE scrtext_l.

    "Miro si el texto para todas las denominaciones del campo esta informado
    IF iv_all_text IS NOT INITIAL.
      d_texto_corto = iv_all_text.
      d_texto_medio = iv_all_text.
      d_texto_largo = iv_all_text.
    ELSE.

      "Voy mirando cada una de las denominaciones par air poniendolas en variables.
      IF iv_short_text IS NOT INITIAL.
        d_texto_corto = iv_short_text.
      ENDIF.

      IF iv_medium_text IS NOT INITIAL.
        d_texto_medio = iv_medium_text.
      ENDIF.

      IF iv_long_text IS NOT INITIAL.
        d_texto_largo = iv_long_text.
      ENDIF.

    ENDIF.

    "Dependiendo de las variables de textos informadas voy llamando a los método correspondientes.
    IF d_texto_medio IS NOT INITIAL.
      mo_column->set_medium_text( d_texto_medio ).
    ENDIF.

    IF d_texto_largo IS NOT INITIAL.
      mo_column->set_long_text( d_texto_largo ).
    ENDIF.

    IF d_texto_corto IS NOT INITIAL.
      mo_column->set_short_text( d_texto_corto ).
    ENDIF.

  ENDMETHOD.


  METHOD set_footer_page.

    "Creo el tipo de campo para la cabecera de la página
    CALL METHOD me->set_page_field_type
      EXPORTING
        iv_row        = iv_row
        iv_column     = iv_column
        iv_field_type = iv_field_type
        iv_text       = iv_text.

    "Paso los construidos de la cabecera al ALV
    mo_alv->set_end_of_list( mo_cabecera ).

    "Si se indica que el listado por impresora tendrá el mismo formato
    "que el normal, entonces pasa la clase con la cabecera al ALV.
    IF iv_list = if_salv_c_bool_sap=>true.
      mo_alv->set_end_of_list( mo_cabecera ).
    ENDIF.

  ENDMETHOD.


  METHOD set_function.


    TRY.

        "Oculto o visualizo el botón pasado por parametro.
        cl_lista_funciones->set_function( name    = iv_function
                                           boolean = i_boolean ).

      CATCH cx_salv_not_found cx_salv_wrong_call.

        MESSAGE s000(fb) WITH iv_function TEXT-e01.

    ENDTRY.

  ENDMETHOD.


  METHOD set_header_page.

    "Creo el tipo de campo para la cabecera de la página
    CALL METHOD me->set_page_field_type
      EXPORTING
        iv_row        = iv_row
        iv_column     = iv_column
        iv_field_type = iv_field_type
        iv_text       = iv_text.

    "Paso los construidos de la cabecera al ALV
    mo_alv->set_top_of_list( mo_cabecera ).

    "Si se indica que el listado por impresora tendrá el mismo formato
    "que el normal, entonces pasa la clase con la cabecera al ALV.
    IF iv_list = if_salv_c_bool_sap=>true.
      mo_alv->set_top_of_list_print( mo_cabecera ).
    ENDIF.

  ENDMETHOD.


  METHOD set_layout.

    CALL METHOD mo_layout->set_initial_layout
      EXPORTING
        value = iv_layout.

  ENDMETHOD.


  METHOD set_manag_layout.

    "Actualizo la clave de la gestión
    mo_layout->set_key( ms_layout_key ).

    "E indico las restricciones existentes en la gestion de layout
    mo_layout->set_save_restriction( iv_restriction ).


  ENDMETHOD.


  METHOD set_optimized_cols.

    "Ajustar ancho de las columnas al contenido de los campos
    mo_columns->set_optimize( cl_salv_display_settings=>true ).

  ENDMETHOD.


  METHOD set_page_field_type.

    "Creo y asocio el tipo de campo de la cabecera o pie de pagina.
    CASE iv_field_type.
      WHEN cv_header_flow_type.

        mo_layout_flow = mo_cabecera->create_flow( row = iv_row
                                              column = iv_column ).
        mo_layout_flow->create_text( text = iv_text
                                tooltip = iv_text ).

      WHEN dc_cab_tipo_etiqueta.

        mo_label = mo_cabecera->create_label( row = iv_row
                                                 column = iv_column
                                                 text = iv_text
                                                 tooltip = iv_text ).

      WHEN dc_cab_tipo_header.

        mo_header = mo_cabecera->create_header_information( row = iv_row
                                                            column = iv_column
                                                            text = iv_text
                                                            tooltip = iv_text ).

      WHEN dc_cab_tipo_info.

        mo_info = mo_cabecera->create_action_information( row = iv_row
                                                          column = iv_column
                                                          text = iv_text
                                                          tooltip = iv_text ).
      WHEN dc_cab_tipo_texto.

        mo_texto = mo_cabecera->create_text( row = iv_row
                                             column = iv_column
                                             text = iv_text
                                             tooltip = iv_text
                                             rowspan = iv_row colspan = iv_column ).


    ENDCASE.

  ENDMETHOD.


  METHOD set_pfstatus.
    DATA: cl_excep TYPE REF TO cx_salv_method_not_supported.

    TRY.

        "Funciones
        mo_alv->set_screen_status( pfstatus = iv_pfstatus
                                   report = mv_repid
                                   set_functions = iv_functions ).

      CATCH cx_salv_method_not_supported INTO cl_excep.

        MESSAGE e000(fb) WITH cl_excep->key.

    ENDTRY.


  ENDMETHOD.


  METHOD set_screen_popup.

    mo_alv->set_screen_popup(
      start_column = iv_start_column
      end_column   = iv_end_column
      start_line   = iv_start_line
      end_line     = iv_end_line ).

  ENDMETHOD.


  METHOD set_selection_mode.

    "Los tipos de selección lo indica la interface: IF_SALV_C_SELECTION_MODE
    mo_selections->set_selection_mode( iv_method ).

  ENDMETHOD.


  METHOD set_symbol_field.

    "Indico que el campo bloqueo es un icono
    mo_column ?= mo_columns->get_column( iv_field ).
    mo_column->set_symbol( iv_active ).

  ENDMETHOD.


  METHOD set_title.

    mo_display->set_list_header( iv_title ).

  ENDMETHOD.


  METHOD set_zebra_mode.

    "Patrón de visualización Zebra
    mo_display->set_striped_pattern( iv_active ).

  ENDMETHOD.


  METHOD show_alv.

    mo_alv->display( ).

  ENDMETHOD.
ENDCLASS.