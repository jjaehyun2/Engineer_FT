class ZCL_4_FPM_MONSTERSEARCH_FEEDER definition
  public
  create public .

public section.

  interfaces IF_FPM_GUIBB .
  interfaces IF_FPM_GUIBB_SEARCH .

  data MS_MONSTER_HEADER type Z4SC_MONSTER_HEADER .
  data MT_MONSTER_HEADERS type Z4_TT_MONSTER_HEADER .
protected section.
private section.
ENDCLASS.



CLASS ZCL_4_FPM_MONSTERSEARCH_FEEDER IMPLEMENTATION.


  method IF_FPM_GUIBB_SEARCH~CHECK_CONFIG.

  endmethod.


  method IF_FPM_GUIBB_SEARCH~FLUSH.

  endmethod.


  method IF_FPM_GUIBB_SEARCH~GET_DATA.
*--------------------------------------------------------------------*
* Listing 12.08 : Get Data Method of Feeder Class
*--------------------------------------------------------------------*
    CHECK io_event->mv_event_id = if_fpm_guibb_search=>fpm_execute_search.

    et_result_list = mt_monster_headers.

  endmethod.


  method IF_FPM_GUIBB_SEARCH~GET_DEFAULT_CONFIG.

  endmethod.


  METHOD if_fpm_guibb_search~get_definition.
*--------------------------------------------------------------------*
* Listing 12.06 : Get_Defintion Method of Feeder Class
*--------------------------------------------------------------------*
    "What are the search criteria going to be?
    eo_field_catalog_attr ?= cl_abap_structdescr=>describe_by_data( ms_monster_header ).

    "What columns are going to be displayed in a table?
    eo_field_catalog_result ?= cl_abap_tabledescr=>describe_by_data( mt_monster_headers ).

    "What are the column headings going to be?
    DATA(table_of_fields) = eo_field_catalog_attr->get_ddic_field_list( ).

    "Nice example of transforming an internal table into a
    "similar one with a slightly different format
    et_field_description_result = VALUE #(
     FOR field_info IN table_of_fields
         ( name = field_info-fieldname
           text = field_info-fieldtext ) ).

  ENDMETHOD.


  METHOD if_fpm_guibb_search~process_event.
*--------------------------------------------------------------------*
* Listing 12.07 : Process_Event Method of Feeder Class
*--------------------------------------------------------------------*
    TRY.
        cl_fpm_guibb_search_conversion=>to_abap_select_where_tab(
          EXPORTING
            it_fpm_search_criteria = it_fpm_search_criteria
            iv_table_name          = 'Z4T_MONSTER_HEAD'
          IMPORTING
            et_abap_select_table   = DATA(where_clause_table) ).

      CATCH cx_fpmgb INTO DATA(guibb_error).
        INSERT VALUE #(
        plaintext = guibb_error->get_text( ) )
        INTO TABLE et_messages.
        RETURN.
    ENDTRY.

* In real life I would transform the where clause into
* a table that the monster model could handle
* but to speed things up - direct read!
    SELECT *
      FROM z4t_monster_head
      INTO CORRESPONDING FIELDS OF TABLE mt_monster_headers
      WHERE (where_clause_table).

  ENDMETHOD."Process Event


  method IF_FPM_GUIBB~GET_PARAMETER_LIST.

  endmethod.


  method IF_FPM_GUIBB~INITIALIZE.

  endmethod.
ENDCLASS.