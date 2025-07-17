class ZCL_UI_DDLB_ADJUST definition
  public
  final
  create public .

public section.

  methods CONSTRUCTOR .
  class-methods GET_INSTANCE
    returning
      value(RR_INSTANCE) type ref to ZCL_UI_DDLB_ADJUST .
  methods PROCESS_TABLE
    importing
      !IR_BOX type ref to CL_THTMLB_SELECTION_BOX .
protected section.
private section.

  data GV_ATTR type STRING .
  class-data SR_SELF type ref to ZCL_UI_DDLB_ADJUST .
  data ST_VIEWS type ZUI_DDLB_VIEW_TAB .
  class-data GT_ACCESS_SEQUENCE type BSP_DLCT_CONF_ACCESS_SEQUENCE .

  methods CHOOSE_CONFIG_BY_AC_SEQ
    importing
      !IS_SEARCH_KEY type BSP_DLCS_CONF_SEM_KEY_VAR_PART
      !IS_VIEW type ZUI_DDLB_VIEW_STRUCT
    returning
      value(RS_CONFIG) type ZUI_DDLB_CONF_STRUCT .
  class-methods BUILD_ACCESS_SEQUENCE
    returning
      value(RESULT) type BSP_DLCT_CONF_ACCESS_SEQUENCE .
ENDCLASS.



CLASS ZCL_UI_DDLB_ADJUST IMPLEMENTATION.


METHOD BUILD_ACCESS_SEQUENCE.
* Copy from CL_BSP_DLC_XML_STORAGE2
  DATA:
  ls_access_sequence TYPE bsp_dlcs_conf_access_keys.

  ls_access_sequence-role_key        = 'X'.
  ls_access_sequence-component_usage = 'X'.
  ls_access_sequence-object_type     = 'X'.
  ls_access_sequence-object_sub_type = 'X'.
  APPEND ls_access_sequence TO result.

  ls_access_sequence-role_key        = 'X'.
  ls_access_sequence-component_usage = 'X'.
  ls_access_sequence-object_type     = 'X'.
  ls_access_sequence-object_sub_type = ''.
  APPEND ls_access_sequence TO result.

* < added
  ls_access_sequence-role_key        = 'X'.
  ls_access_sequence-component_usage = ''.
  ls_access_sequence-object_type     = 'X'.
  ls_access_sequence-object_sub_type = 'X'.
  APPEND ls_access_sequence TO result.

  ls_access_sequence-role_key        = ''.
  ls_access_sequence-component_usage = 'X'.
  ls_access_sequence-object_type     = 'X'.
  ls_access_sequence-object_sub_type = 'X'.
  APPEND ls_access_sequence TO result.

  ls_access_sequence-role_key        = ''.
  ls_access_sequence-component_usage = ''.
  ls_access_sequence-object_type     = 'X'.
  ls_access_sequence-object_sub_type = 'X'.
  APPEND ls_access_sequence TO result.
* added >

  ls_access_sequence-role_key        = 'X'.
  ls_access_sequence-component_usage = ''.
  ls_access_sequence-object_type     = 'X'.
  ls_access_sequence-object_sub_type = ''.
  APPEND ls_access_sequence TO result.

  ls_access_sequence-role_key        = ''.
  ls_access_sequence-component_usage = ''.
  ls_access_sequence-object_type     = 'X'.
  ls_access_sequence-object_sub_type = ''.
  APPEND ls_access_sequence TO result.

* < added
  ls_access_sequence-role_key        = 'X'.
  ls_access_sequence-component_usage = 'X'.
  ls_access_sequence-object_type     = ''.
  ls_access_sequence-object_sub_type = ''.
  APPEND ls_access_sequence TO result.

  ls_access_sequence-role_key        = ''.
  ls_access_sequence-component_usage = 'X'.
  ls_access_sequence-object_type     = ''.
  ls_access_sequence-object_sub_type = ''.
  APPEND ls_access_sequence TO result.

  ls_access_sequence-role_key        = 'X'.
  ls_access_sequence-component_usage = ''.
  ls_access_sequence-object_type     = ''.
  ls_access_sequence-object_sub_type = ''.
  APPEND ls_access_sequence TO result.
* added >

  ls_access_sequence-role_key        = ''.
  ls_access_sequence-component_usage = ''.
  ls_access_sequence-object_type     = ''.
  ls_access_sequence-object_sub_type = ''.
  APPEND ls_access_sequence TO result.

ENDMETHOD.


  METHOD choose_config_by_ac_seq.
* Copy from CL_BSP_DLC_XML_STORAGE2

    DATA: ls_access_key TYPE bsp_dlcs_conf_access_keys,
          ls_key        TYPE bsp_dlcs_conf_sem_key_var_part.

    LOOP AT gt_access_sequence INTO ls_access_key.
      ls_key = is_search_key.
      IF ls_access_key-role_key IS INITIAL.
        ls_key-role_key = cl_bsp_dlc_xml_storage2=>default_role_key.
      ENDIF.
      IF ls_access_key-component_usage IS INITIAL.
        ls_key-component_usage  = cl_bsp_dlc_xml_storage2=>default_component_usage.
      ENDIF.
      IF ls_access_key-object_type IS INITIAL.
        ls_key-object_type  = cl_bsp_dlc_xml_storage2=>default_object_type.
      ENDIF.
      IF ls_access_key-object_sub_type IS INITIAL.
        ls_key-object_sub_type = cl_bsp_dlc_xml_storage2=>default_object_sub_type.
      ENDIF.

      TRY .
          rs_config = is_view-configs[ role_key = ls_key-role_key
                                       component_usage = ls_key-component_usage
                                       object_type = ls_key-object_type
                                       object_sub_type = ls_key-object_sub_type ].
          "found
          EXIT.
        CATCH cx_sy_itab_line_not_found.
          "not found - continue
      ENDTRY.
    ENDLOOP.
  ENDMETHOD.


  METHOD constructor.

    DATA: lt_configs TYPE TABLE OF zui_ddlb_config,
          lt_attrs   TYPE TABLE OF zui_ddlb_v_attr,
          lt_ddlbs   TYPE TABLE OF zui_ddlb_v_sort.
    DATA: ls_config TYPE zui_ddlb_config,
          ls_attr   TYPE zui_ddlb_v_attr,
          ls_ddlb   TYPE zui_ddlb_v_sort.

    FIELD-SYMBOLS: <fs_view> TYPE zui_ddlb_view_struct,
                   <fs_config> TYPE zui_ddlb_conf_struct,
                   <fs_attr>   TYPE zui_ddlb_attr_struct,
                   <fs_ddlb>   TYPE zui_ddlb_sort_struct.

    gt_access_sequence = build_access_sequence( ).

    SELECT * INTO CORRESPONDING FIELDS OF TABLE st_views
      FROM zui_ddlb_views.

    SELECT * INTO CORRESPONDING FIELDS OF TABLE lt_configs
      FROM zui_ddlb_config.

    SELECT * INTO CORRESPONDING FIELDS OF TABLE lt_attrs
      FROM zui_ddlb_v_attr.

    SELECT * INTO CORRESPONDING FIELDS OF TABLE lt_ddlbs
      FROM zui_ddlb_v_sort.

    LOOP AT st_views ASSIGNING <fs_view>.
      LOOP AT lt_configs INTO ls_config
        WHERE component_name = <fs_view>-component_name
          AND view_name = <fs_view>-view_name.
        APPEND INITIAL LINE TO <fs_view>-configs ASSIGNING <fs_config>.
        MOVE-CORRESPONDING ls_config TO <fs_config>.

        LOOP AT lt_attrs INTO ls_attr
          WHERE context_id = ls_config-context_id.
          APPEND INITIAL LINE TO <fs_config>-attrs ASSIGNING <fs_attr>.
          MOVE-CORRESPONDING ls_attr TO <fs_attr>.

          LOOP AT lt_ddlbs INTO ls_ddlb
            WHERE context_id = ls_attr-context_id
              AND attr_name = ls_attr-attr_name.
            APPEND INITIAL LINE TO <fs_attr>-ddlbs ASSIGNING <fs_ddlb>.
            MOVE-CORRESPONDING ls_ddlb TO <fs_ddlb>.

          ENDLOOP.
        ENDLOOP.
      ENDLOOP.
    ENDLOOP.
  ENDMETHOD.


  method GET_INSTANCE.

    IF sr_self IS NOT BOUND.
      CREATE OBJECT sr_self.
    ENDIF.

    rr_instance = sr_self.
  endmethod.


  METHOD process_table.

    TYPES:  BEGIN OF ts_sort_tabel,
              sequence TYPE zui_attr_value_sequence,
              data     TYPE REF TO data,
            END OF ts_sort_tabel.
    DATA: ls_sort TYPE ts_sort_tabel,
          lt_sort TYPE SORTED TABLE OF ts_sort_tabel WITH NON-UNIQUE KEY sequence.

    DATA: lr_page_context    TYPE REF TO cl_bsp_page_context,
          lr_controller      TYPE REF TO cl_bsp_wd_view_controller,
          lr_advs_controller TYPE REF TO cl_bsp_wd_advsearch_controller,
          lr_dropdown        TYPE REF TO clg_thtmlb_dropdownlistbox.

    DATA: lv_component  TYPE bsp_wd_component_name,
          lv_viewname	  TYPE o2pageext,
          ls_search_key TYPE bsp_dlcs_conf_sem_key_var_part,
          lv_attr       TYPE string,
          lv_index      TYPE string,
          lv_dummy      TYPE string.
    DATA: ls_view   TYPE zui_ddlb_view_struct,
          ls_config TYPE zui_ddlb_conf_struct,
          ls_attr   TYPE zui_ddlb_attr_struct,
          ls_ddlb   TYPE zui_ddlb_sort_struct.

    CONSTANTS: lc_min TYPE zui_attr_value_sequence VALUE '-1',
               lc_max TYPE zui_attr_value_sequence VALUE '9999'.

    FIELD-SYMBOLS <tc> TYPE INDEX TABLE.
    FIELD-SYMBOLS: <rc>   TYPE any,
                   <key>  TYPE any,
                   <temp> TYPE any.

    TRY.
        lr_page_context ?= ir_box->m_page_context.
        lr_controller ?= lr_page_context->m_caller.
        lr_dropdown ?= ir_box->m_parent.
        lv_attr = to_upper( lr_dropdown->_selection ). "binding string

        IF lv_attr IS INITIAL. "in case of advanced search page
          lr_advs_controller ?= lr_page_context->m_caller.
          IF lr_advs_controller IS BOUND.
            IF lr_dropdown->id CS '.FIELD'. "always first in any row of selection criteria
              "..._btqact_parameters[8].FIELD__key
              gv_attr = to_upper( ir_box->selection ).
            ELSEIF lr_dropdown->id CS '.VALUE1' OR lr_dropdown->id CS '.VALUE2'.
              "..._btqact_parameters[6].VALUE1__key
              lv_attr = gv_attr.
            ENDIF.
          ENDIF.
        ENDIF.
      CATCH cx_root.
        RETURN.
    ENDTRY.

    CHECK lr_controller IS BOUND AND lv_attr IS NOT INITIAL.

    lr_controller->configuration_descr->get_config_key(
      IMPORTING
        ev_component       =  lv_component   " Component Name
        ev_viewname        =  lv_viewname   " Name of BSP Page/Controller (Case-Sensitive)
        ev_role_key        =  ls_search_key-role_key   " Role Configuration Key
        ev_component_usage =  ls_search_key-component_usage   " Component Usage
        ev_object_type     =  ls_search_key-object_type   " UI Object Type
        ev_object_sub_type =  ls_search_key-object_sub_type   " Object Subtype
    ).

    lv_viewname = to_upper( lv_viewname ).

* Find filter and sort settings
    IF line_exists( st_views[ component_name = lv_component view_name = lv_viewname ] ).

      ls_view = st_views[ component_name = lv_component view_name = lv_viewname ].

      ls_config = choose_config_by_ac_seq( is_view = ls_view is_search_key = ls_search_key ).
      IF ls_config IS INITIAL.
        RETURN. "no configuration found
      ENDIF.

      IF line_exists( ls_config-attrs[ attr_name = lv_attr ] ).
        " set 'future' flag of custom sorting
        ASSIGN ir_box->('CUSTOMSORTING') TO FIELD-SYMBOL(<fs_customsorting>).
        IF <fs_customsorting> IS ASSIGNED.
          <fs_customsorting> = abap_true.
        ENDIF.

        ls_attr = ls_config-attrs[ attr_name = lv_attr ].
        DATA(lf_all_hidden) = ls_attr-all_hidden.

        ASSIGN ir_box->table->* TO <tc>.
        LOOP AT <tc> ASSIGNING <rc>.
          ASSIGN COMPONENT ir_box->nameofkeycolumn OF STRUCTURE <rc> TO <key>.

          CLEAR ls_sort.

          IF <key> IS NOT INITIAL.

            TRY .
                ls_ddlb = ls_attr-ddlbs[ ddlb_key = <key> ].

                IF ls_ddlb-is_hidden EQ abap_true.
                  "current key is hidden
                  CONTINUE.
                ELSEIF ls_ddlb-sequence IS INITIAL.
                  "no sequence defined - set max
                  ls_sort-sequence = lc_max.
                ELSE.
                  ls_sort-sequence = ls_ddlb-sequence.
                ENDIF.
              CATCH cx_sy_itab_line_not_found.
                "no such key defined explicitly
                IF lf_all_hidden EQ abap_true.
                  "'hide all except explicitly defined' and no such a key
                  CONTINUE.
                ELSE.
                  "for not explicilty defined set sequence as max
                  ls_sort-sequence = lc_max.
                ENDIF.
            ENDTRY.
          ELSE.
            ls_sort-sequence = lc_min.
          ENDIF.

          CREATE DATA ls_sort-data LIKE <rc>.
          ASSIGN ls_sort-data->* TO <temp>.
          <temp> = <rc>.

          INSERT ls_sort INTO TABLE lt_sort.

        ENDLOOP.

        REFRESH <tc>.

        LOOP AT lt_sort INTO ls_sort.
          ASSIGN ls_sort-data->* TO <rc>.
          APPEND <rc> TO <tc>.
        ENDLOOP.

      ENDIF.

    ENDIF.
  ENDMETHOD.
ENDCLASS.