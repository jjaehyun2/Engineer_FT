CLASS /hec1/cl_bopf_config_ui_tree_h DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.

    INTERFACES /hec1/if_bopf_config_ui_tree_h .

    METHODS constructor .
    CLASS-METHODS get_instance
      RETURNING
        VALUE(ro_instance) TYPE REF TO /hec1/cl_bopf_config_ui_tree_h .
  PROTECTED SECTION.
  PRIVATE SECTION.

    CLASS-DATA mo_instance TYPE REF TO /hec1/cl_bopf_config_ui_tree_h .
    DATA mt_tree TYPE /hec1/t_bopf_config_tree .
    DATA mt_tree_phasing TYPE /hec1/t_bopf_config_tree_phase .

    METHODS clear .
    METHODS fill_tree_data
      IMPORTING
        !is_node            TYPE /hec1/s_bopf_config_data2tree
      RETURNING
        VALUE(rs_tree_data) TYPE /hec1/s_bopf_config_tree .
    METHODS get_parent_key
      IMPORTING
        !iv_key         TYPE sysuuid_c22 OPTIONAL
        !iv_object_type TYPE /hec1/object_type
        !iv_tree_type   TYPE string DEFAULT /hec1/if_config_constants=>gc_tree_type-distribution
      RETURNING
        VALUE(rv_key)   TYPE sysuuid_c22 .
    METHODS get_text_id
      IMPORTING
        !iv_object_type   TYPE /hec1/object_type
      RETURNING
        VALUE(rv_text_id) TYPE wdr_text_key .
    METHODS load_data_by_query
      IMPORTING
        !iv_confid               TYPE /hec1/config_id
        !iv_conf_version         TYPE /hec1/config_version
      EXPORTING
        !et_tier_add_storage     TYPE /hec1/t_tier_add_storage_ct
        !et_landscape            TYPE /hec1/t_config_root_ct
        !et_delivery_unit        TYPE /hec1/t_data_dlvy_unit_ct
        !et_datacenter           TYPE /hec1/t_data_datacenter_ct
        !et_connectivity         TYPE /hec1/t_data_connectivity_ct
        !et_add_service          TYPE /hec1/t_data_add_services_ct
        !et_longterm_backup_dc   TYPE /hec1/t_data_lt_backup_dc_ct
        !et_longterm_backup_cl   TYPE /hec1/t_data_lt_backup_cl_ct
        !et_longterm_backup_am   TYPE /hec1/t_lt_backup_amount_ct
        !et_add_storage_dc       TYPE /hec1/t_add_storage_dc_ct
        !et_add_storage_cl       TYPE /hec1/t_add_storage_class_ct
        !et_add_storage_am       TYPE /hec1/t_add_storage_amount_ct
        !et_solution             TYPE /hec1/t_data_solution_ct
        !et_tier                 TYPE /hec1/t_data_tier_ct
        !et_tier_sla             TYPE /hec1/t_data_tier_sla_ct
        !et_material             TYPE /hec1/t_data_material_ct
        !et_sw_item              TYPE /hec1/t_data_sw_item_ct
        !et_tier_add_service     TYPE /hec1/t_data_tier_add_serv_ct
        !et_tier_longterm_backup TYPE /hec1/t_data_tier_lt_backup_ct
        !et_db_serv_inst         TYPE /hec1/t_data_db_server_inst_ct
        !et_instance_db          TYPE /hec1/t_data_db_inst_ct
        !et_db_node              TYPE /hec1/t_data_db_node_ct
        !et_db_serv_perf_cat     TYPE /hec1/t_data_db_serv_pc_ct
        !et_db_storage_qty       TYPE /hec1/t_data_db_storage_qty_ct
        !et_db_server            TYPE /hec1/t_data_db_serv_ct
        !et_db_storage           TYPE /hec1/t_data_db_storage_ct
        !et_db_backup            TYPE /hec1/t_data_db_backup_ct
        !et_app_serv_inst        TYPE /hec1/t_data_app_serv_inst_ct
        !et_app_node             TYPE /hec1/t_data_app_node_ct
        !et_app_serv_perf_cat    TYPE /hec1/t_data_app_serv_pc_ct
        !et_app_storage_qty      TYPE /hec1/t_data_app_storageqty_ct
        !et_app_server           TYPE /hec1/t_data_app_serv_ct
        !et_app_storage          TYPE /hec1/t_data_app_storage_ct
        !et_app_backup           TYPE /hec1/t_data_app_backup_ct
        !et_phase                TYPE /hec1/t_data_phase_ct .
    METHODS sort_tree_distribut .
    METHODS sort_tree_phasing .
ENDCLASS.



CLASS /hec1/cl_bopf_config_ui_tree_h IMPLEMENTATION.


  METHOD /hec1/if_bopf_config_ui_tree_h~set_lead_selection_key.

    CHECK iv_lead_selection_key IS NOT INITIAL.

    CASE iv_tree_type.

        " Distribution Tree
      WHEN /hec1/if_config_constants=>gc_tree_type-distribution.

        TRY.
            me->mt_tree[ hec_lead_selection = abap_true ]-hec_lead_selection = abap_false.
            me->mt_tree[ iv_lead_selection_key ]-hec_lead_selection = abap_true.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        " Phasing Tree
      WHEN /hec1/if_config_constants=>gc_tree_type-phasing.

        TRY.
            me->mt_tree_phasing[ hec_lead_selection = abap_true ]-hec_lead_selection = abap_false.
            me->mt_tree_phasing[ iv_lead_selection_key ]-hec_lead_selection = abap_true.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

    ENDCASE.

  ENDMETHOD.


  METHOD constructor.

    me->mo_instance = me.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~set_expand_key.
    CHECK iv_key IS NOT INITIAL.

    CASE iv_tree_type.

        " Distribution Tree
      WHEN /hec1/if_config_constants=>gc_tree_type-distribution.

        TRY.
            me->mt_tree[ row_key = iv_key ]-expanded = abap_true.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        " Phasing Tree
      WHEN /hec1/if_config_constants=>gc_tree_type-phasing.

        TRY.
            me->mt_tree_phasing[  row_key = iv_key ]-expanded = abap_true.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

    ENDCASE.
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~insert_phasing.

    DATA: ls_tree_phasing LIKE LINE OF me->mt_tree_phasing.

    " ******************************
    " Phasing tree - Phases
    " ******************************
    LOOP AT it_node ASSIGNING FIELD-SYMBOL(<fs_node>).

      CLEAR: ls_tree_phasing.


      MOVE-CORRESPONDING <fs_node> TO ls_tree_phasing.
      MOVE-CORRESPONDING me->fill_tree_data( CORRESPONDING #( <fs_node> ) ) TO ls_tree_phasing.

      INSERT VALUE #( BASE ls_tree_phasing
                      parent_key         = COND #( WHEN line_exists( me->mt_tree_phasing[ row_key = <fs_node>-parent_key ] )
                                                   THEN <fs_node>-parent_key
                                                   ELSE space )
                      is_leaf            = abap_true
                      expanded           = abap_true
                      hec_lead_selection = COND #( WHEN line_exists( me->mt_tree_phasing[ row_key = <fs_node>-parent_key ] )
                                                   THEN abap_false
                                                   ELSE abap_true )
                                            ) INTO TABLE  me->mt_tree_phasing.

    ENDLOOP.

    me->sort_tree_phasing( ).

    " Turn last entry in a branch into a leaf
    LOOP AT me->mt_tree_phasing ASSIGNING FIELD-SYMBOL(<fs_tree>).
      TRY.
          me->mt_tree_phasing[ row_key = <fs_tree>-parent_key ]-is_leaf = abap_false.
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.
    ENDLOOP.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~get_tree_line_phasing.

    " Phasing Tree
    TRY.
        rs_line = me->mt_tree_phasing[ row_key = iv_row_key ].
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~get_hierarchy_phasing.

    rt_tree_hierarchy = me->mt_tree_phasing.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~set_collaps_flag.

    CHECK iv_index IS NOT INITIAL.

    CASE iv_tree_type.

        " Distribution Tree
      WHEN /hec1/if_config_constants=>gc_tree_type-distribution.

        TRY.
            me->mt_tree[ iv_index ]-expanded = abap_false.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        " Phasing Tree
      WHEN /hec1/if_config_constants=>gc_tree_type-phasing.

        TRY.
            me->mt_tree_phasing[ iv_index ]-expanded = abap_false.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

    ENDCASE.

  ENDMETHOD.


  METHOD sort_tree_phasing.

    DATA: lt_tree_temp LIKE me->mt_tree_phasing.

    " the sorting groups by parent phase first
    LOOP AT me->mt_tree_phasing ASSIGNING FIELD-SYMBOL(<fs_group>) GROUP BY ( parent = <fs_group>-parent_key
                                                                              start  = <fs_group>-hec_phase_start_date
                                                                              end    = <fs_group>-hec_phase_end_date ) ASCENDING.

      LOOP AT GROUP <fs_group> ASSIGNING FIELD-SYMBOL(<fs_line>).

        " if the line already exists, it should not be added again
        IF line_exists( lt_tree_temp[ row_key = <fs_line>-row_key ] ).
          CONTINUE. ">>>>
        ENDIF.

        IF <fs_line>-hec_phase_start_date IS INITIAL
          OR <fs_line>-hec_phase_end_date IS INITIAL.
          CONTINUE. ">>>>
        ENDIF.

        " add successor/predecessor separately
        " read each successor line and add it to the result table
        IF <fs_line>-hec_phase_successor_guid IS NOT INITIAL.

          APPEND <fs_line> TO lt_tree_temp.

          DATA(lv_successor_guid) = <fs_line>-hec_phase_successor_guid.

          DO.
            TRY.
                DATA(ls_line) = me->mt_tree_phasing[ node_key = lv_successor_guid ].
                APPEND ls_line TO lt_tree_temp.

                IF ls_line-hec_phase_successor_guid IS NOT INITIAL.
                  lv_successor_guid = ls_line-hec_phase_successor_guid.
                ELSE.
                  EXIT. ">>>>
                ENDIF.

              CATCH cx_sy_itab_line_not_found.
                EXIT. ">>>>
            ENDTRY.
          ENDDO.

          CLEAR lv_successor_guid.

        ELSEIF ( <fs_line>-hec_phase_successor_guid IS NOT INITIAL
          AND <fs_line>-hec_phase_predecessor_guid IS NOT INITIAL )
          OR <fs_line>-hec_phase_successor_guid IS NOT INITIAL.

          CONTINUE. "only add successor/predecessors starting from the first node

        ELSE. "read successor/predecessor

          APPEND <fs_line> TO lt_tree_temp.
        ENDIF.

      ENDLOOP.
    ENDLOOP.

    " Add lines that don't have start or end date
    LOOP AT me->mt_tree_phasing ASSIGNING <fs_line> WHERE hec_phase_start_date IS INITIAL OR hec_phase_end_date IS INITIAL.
      " if the line already exists, it should not be added again
      IF line_exists( lt_tree_temp[ row_key = <fs_line>-row_key ] ).
        CONTINUE. ">>>>
      ENDIF.

      APPEND <fs_line> TO lt_tree_temp.
    ENDLOOP.

    IF lt_tree_temp IS NOT INITIAL.
      me->mt_tree_phasing = lt_tree_temp.
    ENDIF.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~set_parents_expanded.

    CASE iv_tree_type.

        " ***************************
        " Distribution Tree
        " ***************************
      WHEN /hec1/if_config_constants=>gc_tree_type-distribution.

        TRY.
            DATA(ls_tree_object) = me->mt_tree[ row_key = iv_key ].
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        "Expand all parents all to the top in case they were collapsed
        DATA(lv_all_updated) = abap_false.
        DATA(lv_parent_key) = ls_tree_object-parent_key.
        WHILE lv_all_updated = abap_false.
          READ TABLE me->mt_tree REFERENCE INTO DATA(lr_parent_object) WITH KEY row_key = lv_parent_key.
          IF sy-subrc = 0.
            lr_parent_object->expanded = abap_true.
            lv_parent_key = lr_parent_object->parent_key.
          ELSE.
            "top one is updated
            lv_all_updated = abap_true.
          ENDIF.
        ENDWHILE. "lv_all_updated = abap_false

        " ***************************
        " Phasing Tree
        " ***************************
      WHEN /hec1/if_config_constants=>gc_tree_type-phasing.

        TRY.
            DATA(ls_tree_object_phase) = me->mt_tree_phasing[ row_key = iv_key ].
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        "Expand all parents all to the top in case they were collapsed
        lv_all_updated = abap_false.
        lv_parent_key = ls_tree_object_phase-parent_key.
        WHILE lv_all_updated = abap_false.
          READ TABLE me->mt_tree_phasing REFERENCE INTO DATA(lr_parent_object_phase) WITH KEY row_key = lv_parent_key.
          IF sy-subrc = 0.
            lr_parent_object_phase->expanded = abap_true.
            lv_parent_key = lr_parent_object_phase->parent_key.
          ELSE.
            "top one is updated
            lv_all_updated = abap_true.
          ENDIF.
        ENDWHILE. "lv_all_updated = abap_false

    ENDCASE. " CASE iv_tree_type.

  ENDMETHOD.


  METHOD get_instance.

    ro_instance = COND #( WHEN mo_instance IS BOUND
                          THEN mo_instance
                          ELSE NEW /hec1/cl_bopf_config_ui_tree_h( ) ).

  ENDMETHOD.


  METHOD sort_tree_distribut.

* Tree should look the following after the sorting:
* Landscape
*   Delivery Unit
*     (FL) Datacenter
*       Datacenter
*         Connectivity
*   (FL) Additional Services
*   (FL) Longterm Backup Pool
*   (FL) Additional Storage Pool
*   (FL) Solutions
*     Solution
*       Tier
*         (FL) Software
*           Material
*             Software Item
*         (FL) Additional Service
*         (FL) Tier Longterm Backups
*         (FL) Tier Additional Storage
*         DB Server Instance
*           Instance DB Container
*           Instance DB Tenant
*         App Server Instance
*           App Node Master
*           App Node Standby
*           App Node Worker
*
* 1. Group by parent_key
* 2. Default object before manual objects of the same type   -> The objects need to be read for this
* 3. Successor/Predecessor always in line
* 4. Individual Rules:
*   DB Server Instance before App Server Instance (done)
*   Container before Tenant
*   Master -> Standby -> Worker
*   Storage Qty before Server (done)

    TYPES: BEGIN OF  ty_tree_sort.
             INCLUDE TYPE /hec1/s_bopf_config_tree AS line.
    TYPES:   sort TYPE i,
           END OF ty_tree_sort.

    DATA: lt_tree_temp TYPE TABLE OF ty_tree_sort.

    lt_tree_temp = VALUE #( FOR wa IN me->mt_tree
                           ( line = wa
                             sort = SWITCH #( wa-hec_obj_type
                                              " under landscape
                                              WHEN /hec1/if_config_constants=>gc_tree_child-landscape          THEN 1
                                              WHEN /hec1/if_config_constants=>gc_tree_child-delivery_unit      THEN 2
                                              WHEN /hec1/if_config_constants=>gc_tree_child-add_service_fl     THEN 3
                                              WHEN /hec1/if_config_constants=>gc_tree_child-lt_backup_fl       THEN 4
                                              WHEN /hec1/if_config_constants=>gc_tree_child-add_storage_fl     THEN 5
                                              WHEN /hec1/if_config_constants=>gc_tree_child-solution_fl        THEN 6
                                              " under tier
                                              WHEN /hec1/if_config_constants=>gc_tree_child-tier               THEN ( wa-hec_sort_order + 20 ) " Tiers are sorted in the range of 20-50
                                              WHEN /hec1/if_config_constants=>gc_tree_child-software_fl        THEN 11
                                              WHEN /hec1/if_config_constants=>gc_tree_child-tier_serv_fl       THEN 12
                                              WHEN /hec1/if_config_constants=>gc_tree_child-tier_ltbup_fl      THEN 13
                                              WHEN /hec1/if_config_constants=>gc_tree_child-tier_astor_fl      THEN 14
                                              WHEN /hec1/if_config_constants=>gc_tree_child-db_serv_inst       THEN 20
                                              WHEN /hec1/if_config_constants=>gc_tree_child-app_serv_inst      THEN 25

                                              " sort between container and tenant
                                              WHEN /hec1/if_config_constants=>gc_tree_child-db_inst            THEN ( wa-hec_sort_order + 50 ) "instance dbs are sorted from 50-60

                                              " sort between master, standby and worker
                                              WHEN /hec1/if_config_constants=>gc_tree_child-db_node            " Nodes are sorted from 60 - 70
                                                OR /hec1/if_config_constants=>gc_tree_child-app_node           THEN ( wa-hec_sort_order + 60 )

                                              " under server performance category (server is always last)
                                              WHEN /hec1/if_config_constants=>gc_tree_child-db_server
                                                OR /hec1/if_config_constants=>gc_tree_child-app_server         THEN 999

                                              " all nodes that need successor/predecessor
                                              WHEN /hec1/if_config_constants=>gc_tree_child-db_serv_pc
                                                OR /hec1/if_config_constants=>gc_tree_child-db_storage_qty
                                                OR /hec1/if_config_constants=>gc_tree_child-db_storage
                                                OR /hec1/if_config_constants=>gc_tree_child-db_backup
                                                OR /hec1/if_config_constants=>gc_tree_child-app_serv_pc
                                                OR /hec1/if_config_constants=>gc_tree_child-app_storage_qty
                                                OR /hec1/if_config_constants=>gc_tree_child-app_storage
                                                OR /hec1/if_config_constants=>gc_tree_child-app_backup          THEN 222

                                              ) ) ).

*    DATA(lv_group_counter) = 1.
*
*    " *****************************************
*    " define successor/predecessor order
*    " *****************************************
*    LOOP AT lt_tree_temp INTO DATA(ls_temp)
*      WHERE line-hec_successor_guid IS NOT INITIAL.
*
*      IF ls_temp-line-hec_obj_type = /hec1/if_config_constants=>gc_tree_child-db_storage
*        OR ls_temp-line-hec_obj_type = /hec1/if_config_constants=>gc_tree_child-app_storage.
*        " *****************************************
*        " storage nodes
*        " for storage: Successor = Storage_qty-successor
*        " *****************************************
*
*        DATA(lv_storage_type) = ls_temp-line-hec_obj_type.
*        DATA(lv_storage_qty_type) = COND #( WHEN ls_temp-line-hec_obj_type = /hec1/if_config_constants=>gc_tree_child-db_storage
*                                  THEN /hec1/if_config_constants=>gc_tree_child-db_storage_qty
*                                  ELSE /hec1/if_config_constants=>gc_tree_child-app_storage_qty ).
*
*        " get corresponding storage qty
*        TRY.
*            DATA(ls_storage_qty) = lt_tree_temp[ line-hec_obj_type       = lv_storage_qty_type
*                                                 line-hec_successor_guid = ls_temp-line-hec_successor_guid ].
*          CATCH cx_sy_itab_line_not_found.
*        ENDTRY.
*
*        " check if the storage qty has a predecessor
*        IF NOT line_exists( lt_tree_temp[ line-hec_successor_guid = ls_storage_qty-line-node_key ] ).
*
*          DATA(lv_next_node) = ls_storage_qty-line-hec_successor_guid.
*          ADD 1 TO lv_group_counter.
*          DATA(lv_counter) = lv_group_counter * 100.
*
*          DO.
*            " This is the first line in the successor-predecessor chain
*            ASSIGN lt_tree_temp[ line-hec_obj_type = lv_storage_type
*                                 line-hec_successor_guid = lv_next_node ] TO FIELD-SYMBOL(<fs_temp>).
*
*            IF <fs_temp> IS ASSIGNED.
*              ADD 1 TO lv_counter.
*              <fs_temp>-sort = lv_counter.
*              TRY.
*                  lv_next_node = lt_tree_temp[ line-node_key = lv_next_node ]-line-hec_successor_guid.
*                CATCH cx_sy_itab_line_not_found.
*              ENDTRY.
*              UNASSIGN <fs_temp>.
*            ENDIF. "<fs_temp> is assigned.
*
*            " Get Last Node in chain
*            IF lv_next_node IS INITIAL.
*              " if storage_qty(n)-successor_key is initial -> find the last key:
*              " the last entry is the only entry without a successor_key under the same server_key
*              LOOP AT lt_tree_temp ASSIGNING <fs_temp>
*                WHERE line-parent_node_key = ls_temp-line-parent_node_key
*                  AND line-hec_successor_guid IS INITIAL.
*                ADD 1 TO lv_counter.
*                <fs_temp>-sort = lv_counter.
*              ENDLOOP.
*
*              EXIT.
*            ENDIF. "lv_next_node is initial
*
*          ENDDO.
*
*        ENDIF. "first line
*
*      ELSE. "no storage-node
*        " *****************************************
*        " non-storage nodes
*        " *****************************************
*        IF NOT line_exists( lt_tree_temp[ line-hec_successor_guid = ls_temp-line-node_key ] ).
*          " This is the first entry for the successor/predecessor chain.
*          lv_next_node = ls_temp-line-node_key.
*          ADD 1 TO lv_group_counter.
*          lv_counter = lv_group_counter * 100.
*
*          " Get every successor, using the reference key field and add a counter to it.
*          DO.
*
*            ASSIGN lt_tree_temp[ line-node_key = lv_next_node ] TO <fs_temp>.
*            IF <fs_temp> IS ASSIGNED.
*
*              ADD 1 TO lv_counter.
*              <fs_temp>-sort = lv_counter.
*              lv_next_node = <fs_temp>-line-hec_successor_guid.
*              UNASSIGN <fs_temp>.
*            ENDIF. "<fs_temp> is assigned.
*
*            IF lv_next_node IS INITIAL.
*              EXIT.
*            ENDIF.
*
*          ENDDO.
*
*        ENDIF. "current entry is not a successor but the first node
*      ENDIF. "db storage / app storage
*
*    ENDLOOP. "lt_tree_temp

    SORT lt_tree_temp ASCENDING BY sort
                                   line-crea_date_time.

    me->mt_tree = VALUE #( FOR was IN lt_tree_temp
                           ( was-line ) ).

  ENDMETHOD.


  METHOD get_parent_key.

    CHECK iv_object_type IS NOT INITIAL.

    CASE iv_tree_type.

      WHEN /hec1/if_config_constants=>gc_tree_type-distribution.

        TRY.
            rv_key = COND #( WHEN iv_key IS SUPPLIED    AND
                                  iv_key IS NOT INITIAL
                             THEN me->mt_tree[ parent_key   = iv_key
                                               hec_obj_type = iv_object_type ]-row_key
                             ELSE me->mt_tree[ hec_obj_type = iv_object_type ]-row_key ).
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

      WHEN /hec1/if_config_constants=>gc_tree_type-phasing.

        TRY.
            rv_key = COND #( WHEN iv_key IS SUPPLIED    AND
                                  iv_key IS NOT INITIAL
                             THEN me->mt_tree_phasing[ parent_key   = iv_key
                                                       hec_obj_type = iv_object_type ]-row_key
                             ELSE me->mt_tree_phasing[ hec_obj_type = iv_object_type ]-row_key ).
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

    ENDCASE.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~get_hierarchy.

    rt_tree_hierarchy = me->mt_tree.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~insert.

    DATA: lv_timestamp TYPE timestampl.

    " ******************************
    " Get instance of text provider
    " ******************************
    DATA(lo_text_provider) = /hec1/cl_config_text_provider=>get_instance( /hec1/if_config_constants=>gc_classname-text_provider ).


    " ******************************
    " Insert BOPF node keys into
    " UI tree
    " ******************************
    LOOP AT it_node ASSIGNING FIELD-SYMBOL(<fs_node>).

      GET TIME STAMP FIELD lv_timestamp.

      CASE <fs_node>-hec_obj_type.
          " ******************************
          " Landscape
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-landscape.
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key         = space
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          expanded           = abap_true
                          hec_lead_selection = abap_true
                          hec_row_selectable = abap_true
                          ) INTO TABLE  me->mt_tree.

          " ******************************
          " Delivery Unit
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-delivery_unit.
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key         = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-landscape )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          expanded           = abap_true
                          hec_row_selectable = abap_true
                          ) INTO TABLE  me->mt_tree.

          " Folder data center
          INSERT VALUE #( parent_key         = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-delivery_unit )
                          row_key            = /rbp/cl_general_utilities=>get_new_guid22( )
                          expanded           = abap_true
                          is_leaf            = abap_true
                          image_src          = /hec1/if_config_constants=>gc_image_status-folder
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-datacenter_fl
                                                                           para1 = ' '      )
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-datacenter_fl
                          ) INTO TABLE  me->mt_tree.

          " Folder Additional Service
          INSERT VALUE #( parent_key         = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-landscape )
                          row_key            = /rbp/cl_general_utilities=>get_new_guid22( )
                          expanded           = abap_true
                          is_leaf            = abap_true
                          image_src          = /hec1/if_config_constants=>gc_image_status-folder
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-add_service_fl
                                                                           para1 = ' '      )
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-add_service_fl
                          ) INTO TABLE  me->mt_tree.

          " Folder Longterm Backup
          INSERT VALUE #( parent_key         = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-landscape )
                          row_key            = /rbp/cl_general_utilities=>get_new_guid22( )
                          expanded           = abap_true
                          is_leaf            = abap_true
                          image_src          = /hec1/if_config_constants=>gc_image_status-folder
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-lt_backup_fl
                                                                           para1 = ' '      )
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-lt_backup_fl
                          ) INTO TABLE  me->mt_tree.

          " Folder Additional Storage
          INSERT VALUE #( parent_key         = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-landscape )
                          row_key            = /rbp/cl_general_utilities=>get_new_guid22( )
                          expanded           = abap_true
                          is_leaf            = abap_true
                          image_src          = /hec1/if_config_constants=>gc_image_status-folder
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-add_storage_fl
                                                                           para1 = ' '      )
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-add_storage_fl
                          ) INTO TABLE  me->mt_tree.

          " Folder Solution
          INSERT VALUE #( parent_key         = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-landscape )
                          row_key            = /rbp/cl_general_utilities=>get_new_guid22( )
                          expanded           = abap_true
                          is_leaf            = abap_true
                          image_src          = /hec1/if_config_constants=>gc_image_status-folder
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-solution_fl
                                                                           para1 = ' '      )
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-solution_fl
                          ) INTO TABLE  me->mt_tree.

          " ******************************
          " Datacenter
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-datacenter.
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key         = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-datacenter_fl )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          hec_delete_visible = abap_true
                          ) INTO TABLE  me->mt_tree.

          " ******************************
          " Connectivity
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-connectivity.
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-parent_node_key )
*                          parent_key         = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-datacenter )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          hec_delete_visible = abap_true
                          ) INTO TABLE  me->mt_tree.

          " ******************************
          " Additional Services
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-add_service.
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key         = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-add_service_fl )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          hec_delete_visible = abap_true
                          ) INTO TABLE  me->mt_tree.

          " ******************************
          " Longterm Backup Datacenter Pool
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-lt_backup_dc.
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key         = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-lt_backup_fl )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          hec_delete_visible = abap_true
                          ) INTO TABLE  me->mt_tree.

          " ******************************
          " Longterm Backup Class Pool
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-lt_backup_class.
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-parent_node_key )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          hec_delete_visible = abap_true
                          ) INTO TABLE  me->mt_tree.

          " ******************************
          " Longterm Backup Amount Pool
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-lt_backup_amount.
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-parent_node_key )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          hec_delete_visible = abap_true
                          ) INTO TABLE  me->mt_tree.

          " ******************************
          " Additional Storage Datacenter Pool
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-astorage_dc.
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key         = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-add_storage_fl )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          hec_delete_visible = abap_true
                          ) INTO TABLE  me->mt_tree.

          " ******************************
          " Additional Storage Class Pool
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-astorage_class.
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-parent_node_key )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          hec_delete_visible = abap_true
                          ) INTO TABLE  me->mt_tree.

          " ******************************
          " Additional Storage Amount Pool
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-astorage_amount.
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-parent_node_key )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          hec_delete_visible = abap_true
                          ) INTO TABLE  me->mt_tree.

          " ******************************
          " Solution
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-solution.
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key         = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-solution_fl )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          hec_row_selectable = abap_true
                          hec_delete_visible = abap_true
                          ) INTO TABLE  me->mt_tree.

          " ******************************
          " Tier
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-tier.
          DATA(lv_new_tier_key) = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )  .
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-parent_node_key )
                          row_key    =  lv_new_tier_key
                          ) INTO TABLE  me->mt_tree.

          " Folder SLA
          INSERT VALUE #( parent_key         = lv_new_tier_key
                          row_key            = /rbp/cl_general_utilities=>get_new_guid22( )
                          expanded           = abap_false
                          is_leaf            = abap_true
                          image_src          = /hec1/if_config_constants=>gc_image_status-folder
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-tier_sla_fl
                                                                           para1 = ' '      )
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-tier_sla_fl
                          ) INTO TABLE  me->mt_tree.

          " Folder Software
          INSERT VALUE #( parent_key         = lv_new_tier_key
                          row_key            = /rbp/cl_general_utilities=>get_new_guid22( )
                          expanded           = abap_false
                          is_leaf            = abap_true
                          image_src          = /hec1/if_config_constants=>gc_image_status-folder
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-software_fl
                                                                           para1 = ' '      )
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-software_fl
                          ) INTO TABLE  me->mt_tree.

          " Folder Additional Tier Service
          INSERT VALUE #( parent_key         = lv_new_tier_key
                          row_key            = /rbp/cl_general_utilities=>get_new_guid22( )
                          expanded           = abap_false
                          is_leaf            = abap_true
                          image_src          = /hec1/if_config_constants=>gc_image_status-folder
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-tier_service_fl
                                                                           para1 = ' '      )
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-tier_serv_fl
                          ) INTO TABLE  me->mt_tree.

          " Folder Longterm Backup Tier Assignment
          INSERT VALUE #( parent_key         = lv_new_tier_key
                          row_key            = /rbp/cl_general_utilities=>get_new_guid22( )
                          expanded           = abap_false
                          is_leaf            = abap_true
                          image_src          = /hec1/if_config_constants=>gc_image_status-folder
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-tier_ltbup_fl
                                                                           para1 = ' '      )
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-tier_ltbup_fl
                          ) INTO TABLE  me->mt_tree.

          " Folder Additional Storage (shared) Tier Assignment
          INSERT VALUE #( parent_key         = lv_new_tier_key
                          row_key            = /rbp/cl_general_utilities=>get_new_guid22( )
                          expanded           = abap_false
                          is_leaf            = abap_true
                          image_src          = /hec1/if_config_constants=>gc_image_status-folder
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-tier_a_stor_fl
                                                                           para1 = ' '      )
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-tier_astor_fl
                          ) INTO TABLE  me->mt_tree.

          "update all parents to be expanded
          /hec1/if_bopf_config_ui_tree_h~set_parents_expanded( CONV #( lv_new_tier_key ) ).

          " ******************************
          " Tier SLA
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-tier_sla.
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key = me->get_parent_key( iv_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-parent_node_key )
                                                           iv_object_type = /hec1/if_config_constants=>gc_tree_child-tier_sla_fl                             )
                          row_key    = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          ) INTO TABLE  me->mt_tree.

          " ******************************
          " Material
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-material.
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key = me->get_parent_key( iv_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-parent_node_key )
                                                           iv_object_type = /hec1/if_config_constants=>gc_tree_child-software_fl                             )
                          row_key    = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          ) INTO TABLE  me->mt_tree.

          " ******************************
          " Software Item
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-software_item.
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-parent_node_key )
                          row_key    = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          ) INTO TABLE  me->mt_tree.

          " ******************************
          " Additional Tier Service
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-tier_service.
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key = me->get_parent_key( iv_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-parent_node_key )
                                                           iv_object_type = /hec1/if_config_constants=>gc_tree_child-tier_serv_fl                            )
                          row_key    = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          ) INTO TABLE  me->mt_tree.

          " ******************************
          " Tier Longterm Backup
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-tier_ltbup.
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key = me->get_parent_key( iv_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-parent_node_key )
                                                           iv_object_type = /hec1/if_config_constants=>gc_tree_child-tier_ltbup_fl                            )
                          row_key    = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          ) INTO TABLE  me->mt_tree.

          " ******************************
          " Tier Additional (shared) Storage
          " ******************************
        WHEN /hec1/if_config_constants=>gc_tree_child-tier_astor.
          INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                          parent_key = me->get_parent_key( iv_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-parent_node_key )
                                                           iv_object_type = /hec1/if_config_constants=>gc_tree_child-tier_astor_fl                            )
                          row_key    = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          ) INTO TABLE  me->mt_tree.

          " ******************************
          " all other Distribution nodes (e.g. DB Server / App server nodes)
          " ******************************
        WHEN OTHERS.
          IF <fs_node>-hec_obj_type = /hec1/if_config_constants=>gc_tree_child-db_storage_qty   OR
             <fs_node>-hec_obj_type = /hec1/if_config_constants=>gc_tree_child-app_storage_qty.

            CASE <fs_node>-hec_obj_type.
              WHEN /hec1/if_config_constants=>gc_tree_child-db_storage_qty.
                DATA(lv_obj_type) = /hec1/if_config_constants=>gc_tree_child-db_storage_qty.
              WHEN /hec1/if_config_constants=>gc_tree_child-app_storage_qty.
                lv_obj_type = /hec1/if_config_constants=>gc_tree_child-app_storage_qty.
              WHEN /hec1/if_config_constants=>gc_tree_child-db_storage.
                lv_obj_type = /hec1/if_config_constants=>gc_tree_child-db_storage.
              WHEN /hec1/if_config_constants=>gc_tree_child-app_storage.
                lv_obj_type = /hec1/if_config_constants=>gc_tree_child-app_storage.
            ENDCASE.

            LOOP AT me->mt_tree ASSIGNING FIELD-SYMBOL(<fs_tree>)
              WHERE parent_node_key = <fs_node>-parent_node_key AND
                    hec_obj_type    = lv_obj_type.
              DATA(lv_tabix) = sy-tabix.
            ENDLOOP.

            DATA(ls_tree) = VALUE /hec1/s_bopf_config_tree( BASE me->fill_tree_data( <fs_node> )
                                                            parent_key     = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-parent_node_key )
                                                            row_key        = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                                                            ).

            IF lv_tabix NE 0. "Line exists
              ADD 1 TO lv_tabix.
              TRY.
                  INSERT ls_tree
                    INTO me->mt_tree
                   INDEX lv_tabix.
                CATCH cx_sy_itab_duplicate_key.
              ENDTRY.
            ELSE.
              APPEND ls_tree TO me->mt_tree.
            ENDIF.

            CLEAR: lv_tabix,
                   lv_obj_type,
                   ls_tree.

            UNASSIGN <fs_tree>.
          ELSE.
            INSERT VALUE #( BASE me->fill_tree_data( <fs_node> )
                            parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-parent_node_key )
                            row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_node>-node_key )
                          ) INTO TABLE  me->mt_tree.
          ENDIF.
      ENDCASE.
    ENDLOOP.

    "Distribution
    " Turn last entry in a branch into a leaf
    LOOP AT me->mt_tree ASSIGNING <fs_tree> FROM 2.
      TRY.
          me->mt_tree[ row_key = <fs_tree>-parent_key ]-is_leaf = abap_false.
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.
    ENDLOOP.

    me->sort_tree_distribut( ).

  ENDMETHOD.


  METHOD fill_tree_data.

    DATA(lo_text_provider) = /hec1/cl_config_text_provider=>get_instance( /hec1/if_config_constants=>gc_classname-text_provider ).


    rs_tree_data = VALUE #( row_key            = is_node-row_key
                            parent_key         = is_node-parent_key
                            parent_node_key    = is_node-parent_node_key
                            node_key           = is_node-node_key
                            expanded           = abap_false
                            is_leaf            = abap_true
                            image_src          = COND #( WHEN is_node-hec_obj_type = /hec1/if_config_constants=>gc_tree_child-phase
                                                         THEN space
                                                         ELSE SWITCH #( is_node-hec_instance_status
                                                              WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                              THEN /hec1/if_config_constants=>gc_image_status-complete
                                                              ELSE /hec1/if_config_constants=>gc_image_status-incomplete  ) )
                            text               = COND #( WHEN is_node-hec_obj_type = /hec1/if_config_constants=>gc_tree_child-phase
                                                         THEN is_node-hec_tree_descr
                                                         ELSE lo_text_provider->get_text( key   = me->get_text_id( is_node-hec_obj_type )
                                                                                          para1 = COND #( WHEN is_node-hec_tree_descr IS NOT INITIAL AND
                                                                                                               is_node-hec_tree_descr NA |:|
                                                                                                          THEN |: { is_node-hec_tree_descr }|
                                                                                                          ELSE is_node-hec_tree_descr  ) ) )
                            hec_row_selectable = is_node-hec_row_selectable
                            hec_add_visible    = abap_true
                            hec_delete_visible = is_node-hec_delete_visible
                            hec_obj_type       = is_node-hec_obj_type
                            hec_sort_order     = is_node-hec_sort_order
                            hec_phase_guid     = is_node-hec_phase_guid
                            hec_successor_guid = is_node-hec_successor_guid
                            crea_date_time     = is_node-crea_date_time
                            change_request     = is_node-change_request     ).

  ENDMETHOD.


  METHOD load_data_by_query.

    DATA: lt_sel_param TYPE /bobf/t_frw_query_selparam.


    CLEAR: et_landscape,
           et_delivery_unit,
           et_datacenter,
           et_connectivity,
           et_add_service,
           et_longterm_backup_dc,
           et_longterm_backup_cl,
           et_longterm_backup_am,
           et_add_storage_dc,
           et_add_storage_cl,
           et_add_storage_am,
           et_solution,
           et_tier,
           et_tier_sla,
           et_material,
           et_sw_item,
           et_tier_add_service,
           et_tier_longterm_backup,
           et_tier_add_storage,
           et_db_serv_inst,
           et_instance_db,
           et_db_node,
           et_db_serv_perf_cat,
           et_db_storage_qty,
           et_db_server,
           et_db_storage,
           et_db_backup,
           et_app_serv_inst,
           et_app_node,
           et_app_serv_perf_cat,
           et_app_storage_qty,
           et_app_server,
           et_app_storage,
           et_app_backup,
           et_phase.


    " Get root key
    DATA(lv_root_key) = /hec1/cl_config_helper=>get_root_key_by_query( iv_confid       = iv_confid                           " Configuration ID
                                                                       iv_conf_version = iv_conf_version ).                  " Configuration Version


    IF lv_root_key IS INITIAL.
      RETURN. " >>>>>>
    ENDIF.


    " Fill selection parameter of query call
    lt_sel_param = VALUE #( ( attribute_name = 'DB_KEY' "/hec1/if_configuration_c=>sc_query_attribute-root-select_by_elements-root_key
                              low            = lv_root_key
                              option         = /hec1/if_bopf_constants=>gc_range_option-eq
                              sign           = /hec1/if_bopf_constants=>gc_range_sign-i                                          ) ).

    " Get root/landscape by query
    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-root-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = DATA(lo_message)
                                                                 ev_hits_found      = DATA(lv_hits_found)
                                                                 et_data            = et_landscape                                                    ).

    " Fill selection parameter of query call
    lt_sel_param = VALUE #( ( attribute_name = /hec1/if_configuration_c=>sc_query_attribute-root-select_by_elements-root_key
                              low            = lv_root_key
                              option         = /hec1/if_bopf_constants=>gc_range_option-eq
                              sign           = /hec1/if_bopf_constants=>gc_range_sign-i                                          ) ).

    " Get delivery unit by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-delivery_unit-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_delivery_unit                                                    ).

    " Get data center by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-datacenter-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_datacenter                                                    ).

    " Get connectivity by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-connectivity-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_connectivity                                                    ).

    " Get additional service by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-add_service-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_add_service                                                 ).


    " Get Longterm Backup Datacenter by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-lt_backup_datacenter-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_longterm_backup_dc                                              ).

    " Get Longterm Backup Class by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-lt_backup_class-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_longterm_backup_cl                                              ).
    SORT et_longterm_backup_cl BY crea_date_time.

    " Get Longterm Backup Amount by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-lt_backup_amount-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_longterm_backup_am                                              ).
    SORT et_longterm_backup_am BY crea_date_time.

    " Get Additional Storage Datacenter by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-add_storage_datacenter-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_add_storage_dc                                              ).

    SORT et_add_storage_dc BY crea_date_time.


    " Get Additional Storage Class by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-add_storage_class-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_add_storage_cl                                              ).
    SORT et_add_storage_cl BY crea_date_time.

    " Get Additional Storage Amount by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-add_storage_amount-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_add_storage_am                                              ).
    SORT et_add_storage_am BY crea_date_time.

    " Get solution by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-solution-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_solution                                                    ).

    " Get tier by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-tier-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_tier                                                    ).

    " Get SLA by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-tier_sla-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_tier_sla                                                  ).

    " Get material by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-material-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_material                                                    ).

    " Get software item by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-software_item-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_sw_item                                                          ).

    " Get tier additional service by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-tier_add_service-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_tier_add_service                                                ).


    " Get tier longterm backup by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-tier_longterm_backup-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_tier_longterm_backup                                              ).

    " Get tier Add storage  by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-tier_add_storage-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_tier_add_storage                                             ).

    " Get DB server instance by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-db_server_instance-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_db_serv_inst                                                          ).

    " Get instance DB by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-instance_db-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_instance_db                                                    ).

    " Get DB server instance by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-db_node-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_db_node                                                    ).

    " Get DB server performance category by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-db_server_perform_cat-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_db_serv_perf_cat                                                          ).

    " Get DB storage amount by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-db_storage_amount-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_db_storage_qty                                                       ).

    " Get DB server by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-db_server-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_db_server                                                    ).

    " Get DB storage by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-db_storage-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_db_storage                                                     ).


    " Get DB storage backup by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-db_storage_backup-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_db_backup                                                            ).

    " Get App server instance by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-app_server_instance-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_app_serv_inst                                                          ).

    " Get App node by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-app_node-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_app_node                                                    ).

    " Get App server performance category by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-app_server_perform_cat-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_app_serv_perf_cat                                                          ).

    " Get App storage amount by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-app_storage_amount-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_app_storage_qty                                                        ).

    " Get App server by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-app_server-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_app_server                                                    ).

    " Get App storage by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-app_storage-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_app_storage                                                    ).

    " Get App storage backup by query
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-app_storage_backup-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_app_backup                                                            ).


    " Get Phases
    CLEAR: lo_message,
           lv_hits_found.

    /hec1/cl_config_helper=>get_data_and_key_by_query( EXPORTING iv_query_key       = /hec1/if_configuration_c=>sc_query-phase-select_by_elements
                                                                 it_selection_param = lt_sel_param
                                                                 iv_fill_data       = abap_true
                                                       IMPORTING eo_message         = lo_message
                                                                 ev_hits_found      = lv_hits_found
                                                                 et_data            = et_phase                                                            ).



  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~set_collapse_key.
    CHECK iv_key IS NOT INITIAL.

    CASE iv_tree_type.

        " Distribution Tree
      WHEN /hec1/if_config_constants=>gc_tree_type-distribution.

        TRY.
            me->mt_tree[ row_key = iv_key ]-expanded = abap_false.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        " Phasing Tree
      WHEN /hec1/if_config_constants=>gc_tree_type-phasing.

        TRY.
            me->mt_tree_phasing[  row_key = iv_key ]-expanded = abap_false.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

    ENDCASE.
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~get_lead_selection_tree_key.

    CASE iv_tree_type.

        " Distribution Tree
      WHEN /hec1/if_config_constants=>gc_tree_type-distribution.
        TRY.
            rv_key = me->mt_tree[ hec_lead_selection = abap_true ]-row_key.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        " Phasing Tree
      WHEN /hec1/if_config_constants=>gc_tree_type-phasing.
        TRY.
            rv_key = me->mt_tree_phasing[ hec_lead_selection = abap_true ]-row_key.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.
    ENDCASE.

  ENDMETHOD.


  METHOD clear.
    CLEAR me->mt_tree.
    CLEAR me->mt_tree_phasing.
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~get_lead_selection_node_key.

    CASE iv_tree_type.

        " Distribution Tree
      WHEN /hec1/if_config_constants=>gc_tree_type-distribution.
        TRY.
            rv_key = me->mt_tree[ hec_lead_selection = abap_true ]-node_key.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        " Phasing Tree
      WHEN /hec1/if_config_constants=>gc_tree_type-phasing.
        TRY.
            rv_key = me->mt_tree_phasing[ hec_lead_selection = abap_true ]-node_key.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.
    ENDCASE.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~get_selected_node_type.

    TRY.
        rv_value = me->mt_tree[ hec_lead_selection = abap_true ]-hec_obj_type.
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~update_phasing.

    " ******************************
    " Update UI tree from BOPF
    " ******************************
    LOOP AT it_node ASSIGNING FIELD-SYMBOL(<fs_node>).

      " change phasing tree
      ASSIGN me->mt_tree_phasing[ node_key = <fs_node>-node_key ] TO FIELD-SYMBOL(<fs_tree>).

      IF <fs_tree> IS ASSIGNED.

        DATA(ls_tree_old) = <fs_tree>.
        <fs_tree> = CORRESPONDING #( me->fill_tree_data( CORRESPONDING #( <fs_node> ) )
                             EXCEPT expanded
                                    is_leaf ).

        <fs_tree>-row_key = ls_tree_old-row_key.
        <fs_tree>-parent_key = ls_tree_old-parent_key.
        <fs_tree>-expanded = ls_tree_old-expanded.
        <fs_tree>-is_leaf = ls_tree_old-is_leaf.
        <fs_tree>-hec_lead_selection = ls_tree_old-hec_lead_selection.
        <fs_tree>-hec_delete_visible = ls_tree_old-hec_delete_visible.

        <fs_tree>-hec_phase_start_date = <fs_node>-hec_phase_start_date.
        <fs_tree>-hec_phase_end_date = <fs_node>-hec_phase_end_date.
        <fs_tree>-hec_phase_predecessor_guid = <fs_node>-hec_phase_predecessor_guid.
        <fs_tree>-hec_phase_successor_guid = <fs_node>-hec_phase_successor_guid.

      ENDIF.

      UNASSIGN <fs_tree>.

    ENDLOOP.

    me->sort_tree_phasing( ).

  ENDMETHOD.


  METHOD get_text_id.

    rv_text_id = SWITCH #( iv_object_type
                           WHEN /hec1/if_config_constants=>gc_tree_child-landscape       THEN /hec1/if_config_constants=>gc_tree_text_id-landscape
                           WHEN /hec1/if_config_constants=>gc_tree_child-delivery_unit   THEN /hec1/if_config_constants=>gc_tree_text_id-delivery_unit
                           WHEN /hec1/if_config_constants=>gc_tree_child-datacenter_fl   THEN /hec1/if_config_constants=>gc_tree_text_id-datacenter_fl
                           WHEN /hec1/if_config_constants=>gc_tree_child-datacenter      THEN /hec1/if_config_constants=>gc_tree_text_id-datacenter
                           WHEN /hec1/if_config_constants=>gc_tree_child-connectivity    THEN /hec1/if_config_constants=>gc_tree_text_id-connectivity
                           WHEN /hec1/if_config_constants=>gc_tree_child-add_service_fl  THEN /hec1/if_config_constants=>gc_tree_text_id-add_service_fl
                           WHEN /hec1/if_config_constants=>gc_tree_child-add_service     THEN /hec1/if_config_constants=>gc_tree_text_id-add_service
                           WHEN /hec1/if_config_constants=>gc_tree_child-lt_backup_fl    THEN /hec1/if_config_constants=>gc_tree_text_id-lt_backup_fl
                           WHEN /hec1/if_config_constants=>gc_tree_child-lt_backup       THEN /hec1/if_config_constants=>gc_tree_text_id-lt_backup
                           WHEN /hec1/if_config_constants=>gc_tree_child-lt_backup_dc    THEN /hec1/if_config_constants=>gc_tree_text_id-ltbckup_dc
                           WHEN /hec1/if_config_constants=>gc_tree_child-lt_backup_class THEN /hec1/if_config_constants=>gc_tree_text_id-ltbckup_class
                           WHEN /hec1/if_config_constants=>gc_tree_child-lt_backup_amount THEN /hec1/if_config_constants=>gc_tree_text_id-ltbckup_amount
                           WHEN /hec1/if_config_constants=>gc_tree_child-add_storage_fl  THEN /hec1/if_config_constants=>gc_tree_text_id-add_storage_fl
                           WHEN /hec1/if_config_constants=>gc_tree_child-add_storage     THEN /hec1/if_config_constants=>gc_tree_text_id-add_storage
                           WHEN /hec1/if_config_constants=>gc_tree_child-astorage_dc     THEN /hec1/if_config_constants=>gc_tree_text_id-astorage_dc
                           WHEN /hec1/if_config_constants=>gc_tree_child-astorage_class  THEN /hec1/if_config_constants=>gc_tree_text_id-astorage_class
                           WHEN /hec1/if_config_constants=>gc_tree_child-astorage_amount THEN /hec1/if_config_constants=>gc_tree_text_id-astorage_amount
                           WHEN /hec1/if_config_constants=>gc_tree_child-solution_fl     THEN /hec1/if_config_constants=>gc_tree_text_id-solution_fl
                           WHEN /hec1/if_config_constants=>gc_tree_child-solution        THEN /hec1/if_config_constants=>gc_tree_text_id-solution
                           WHEN /hec1/if_config_constants=>gc_tree_child-tier            THEN /hec1/if_config_constants=>gc_tree_text_id-tier
                           WHEN /hec1/if_config_constants=>gc_tree_child-tier_sla        THEN /hec1/if_config_constants=>gc_tree_text_id-tier_sla
                           WHEN /hec1/if_config_constants=>gc_tree_child-software_fl     THEN /hec1/if_config_constants=>gc_tree_text_id-software_fl
                           WHEN /hec1/if_config_constants=>gc_tree_child-material        THEN /hec1/if_config_constants=>gc_tree_text_id-material
                           WHEN /hec1/if_config_constants=>gc_tree_child-software_item   THEN /hec1/if_config_constants=>gc_tree_text_id-software_item
                           WHEN /hec1/if_config_constants=>gc_tree_child-tier_serv_fl    THEN /hec1/if_config_constants=>gc_tree_text_id-tier_service_fl
                           WHEN /hec1/if_config_constants=>gc_tree_child-tier_service    THEN /hec1/if_config_constants=>gc_tree_text_id-tier_service
                           WHEN /hec1/if_config_constants=>gc_tree_child-tier_ltbup_fl   THEN /hec1/if_config_constants=>gc_tree_text_id-tier_ltbup_fl
                           WHEN /hec1/if_config_constants=>gc_tree_child-tier_ltbup      THEN /hec1/if_config_constants=>gc_tree_text_id-tier_ltbup
                           WHEN /hec1/if_config_constants=>gc_tree_child-tier_astor_fl   THEN /hec1/if_config_constants=>gc_tree_text_id-tier_a_stor_fl
                           WHEN /hec1/if_config_constants=>gc_tree_child-tier_astor      THEN /hec1/if_config_constants=>gc_tree_text_id-tier_astor
                           WHEN /hec1/if_config_constants=>gc_tree_child-db_serv_inst    THEN /hec1/if_config_constants=>gc_tree_text_id-db_serv_inst
                           WHEN /hec1/if_config_constants=>gc_tree_child-db_inst         THEN /hec1/if_config_constants=>gc_tree_text_id-db_inst
                           WHEN /hec1/if_config_constants=>gc_tree_child-db_node         THEN /hec1/if_config_constants=>gc_tree_text_id-db_node
                           WHEN /hec1/if_config_constants=>gc_tree_child-db_serv_pc      THEN /hec1/if_config_constants=>gc_tree_text_id-db_serv_pc
                           WHEN /hec1/if_config_constants=>gc_tree_child-db_storage_qty  THEN /hec1/if_config_constants=>gc_tree_text_id-db_storage_qty
                           WHEN /hec1/if_config_constants=>gc_tree_child-db_server       THEN /hec1/if_config_constants=>gc_tree_text_id-db_server
                           WHEN /hec1/if_config_constants=>gc_tree_child-db_storage      THEN /hec1/if_config_constants=>gc_tree_text_id-db_storage
                           WHEN /hec1/if_config_constants=>gc_tree_child-db_backup       THEN /hec1/if_config_constants=>gc_tree_text_id-db_backup
                           WHEN /hec1/if_config_constants=>gc_tree_child-app_serv_inst   THEN /hec1/if_config_constants=>gc_tree_text_id-app_serv_inst
                           WHEN /hec1/if_config_constants=>gc_tree_child-app_node        THEN /hec1/if_config_constants=>gc_tree_text_id-app_node
                           WHEN /hec1/if_config_constants=>gc_tree_child-app_serv_pc     THEN /hec1/if_config_constants=>gc_tree_text_id-app_serv_pc
                           WHEN /hec1/if_config_constants=>gc_tree_child-app_storage_qty THEN /hec1/if_config_constants=>gc_tree_text_id-app_storage_qty
                           WHEN /hec1/if_config_constants=>gc_tree_child-app_server      THEN /hec1/if_config_constants=>gc_tree_text_id-app_server
                           WHEN /hec1/if_config_constants=>gc_tree_child-app_storage     THEN /hec1/if_config_constants=>gc_tree_text_id-app_storage
                           WHEN /hec1/if_config_constants=>gc_tree_child-app_backup      THEN /hec1/if_config_constants=>gc_tree_text_id-app_backup
                           WHEN /hec1/if_config_constants=>gc_tree_child-phase           THEN /hec1/if_config_constants=>gc_tree_text_id-phase          ).
  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~get_parent_key.

    CHECK iv_key IS NOT INITIAL.

    CASE iv_tree_type.

        " Distribution Tree
      WHEN /hec1/if_config_constants=>gc_tree_type-distribution.

        TRY.
            rv_parent_key = me->mt_tree[ row_key = iv_key ]-parent_key.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        " Phasing Tree
      WHEN /hec1/if_config_constants=>gc_tree_type-phasing.

        TRY.
            rv_parent_key = me->mt_tree_phasing[ row_key = iv_key ]-parent_key.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

    ENDCASE.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~load.

    CHECK: iv_confid       IS NOT INITIAL,
           iv_conf_version IS NOT INITIAL.

    " ******************************
    " Get data by query for
    " creating the tree hierachy
    " ******************************
    me->load_data_by_query( EXPORTING iv_confid               = iv_confid                                  " Configuration ID
                                      iv_conf_version         = iv_conf_version                            " Configuration Version
                            IMPORTING et_landscape            = DATA(lt_landscape)                         " Landscape - #GENERATED#
                                      et_delivery_unit        = DATA(lt_delivery_unit)                     " Delivery unit and infrastructure prov. - #GENERATED#
                                      et_datacenter           = DATA(lt_datacenter)                        " Data center - #GENERATED#
                                      et_connectivity         = DATA(lt_connectivity)                      " Data center connectivity - #GENERATED#
                                      et_add_service          = DATA(lt_add_service)                       " Additional service - #GENERATED#
                                      et_longterm_backup_dc   = DATA(lt_longterm_backup_dc)                " Longterm backup datacenter selection - #GENERATED#
                                      et_longterm_backup_cl   = DATA(lt_longterm_backup_cl)                " Longtermbackup class nodes - #GENERATED#
                                      et_longterm_backup_am   = DATA(lt_longterm_backup_am)                " Longtermbackup amount nodes - #GENERATED#
                                      et_add_storage_dc       = DATA(lt_add_storage_dc)                    " Additional storage datacenter - #GENERATED#
                                      et_add_storage_cl       = DATA(lt_add_storage_cl)                    " Additional storage class - #GENERATED#
                                      et_add_storage_am       = DATA(lt_add_storage_am)                    " Additional storage amount - #GENERATED#
                                      et_solution             = DATA(lt_solution)                          " Solution - #GENERATED#
                                      et_tier                 = DATA(lt_tier)                              " Tier - #GENERATED#
                                      et_tier_sla             = DATA(lt_tier_sla)                          " Tier SLA - #GENERATED#
                                      et_material             = DATA(lt_material)                          " Material - #GENERATED#
                                      et_sw_item              = DATA(lt_software_item)                     " Software item - #GENERATED#
                                      et_tier_add_service     = DATA(lt_tier_add_service)                  " Additional service - #GENERATED#
                                      et_tier_longterm_backup = DATA(lt_tier_longterm_backup)              " Tier Longterm Backup - #GENERATED#
                                      et_tier_add_storage     = DATA(lt_tier_add_storage)                  " Tier additional (shared) storage - #GENERATED#
                                      et_db_serv_inst         = DATA(lt_db_serv_inst)                      " DB server instance - #GENERATED#
                                      et_instance_db          = DATA(lt_instance_db)                       " Instance DB - #GENERATED#
                                      et_db_node              = DATA(lt_db_node)                           " DB node - #GENERATED#
                                      et_db_serv_perf_cat     = DATA(lt_db_serv_perf_cat)                  " DB server performance category - #GENERATED#
                                      et_db_storage_qty       = DATA(lt_db_storage_qty)                    " DB storage amount - #GENERATED#
                                      et_db_server            = DATA(lt_db_server)                         " DB server - #GENERATED#
                                      et_db_storage           = DATA(lt_db_storage)                        " DB server storage - #GENERATED#
                                      et_db_backup            = DATA(lt_db_backup)                         " DB storage backup - #GENERATED#
                                      et_app_serv_inst        = DATA(lt_app_serv_inst)                     " Application server instance - #GENERATED#
                                      et_app_node             = DATA(lt_app_node)                          " Application server node - #GENERATED#
                                      et_app_serv_perf_cat    = DATA(lt_app_serv_perf_cat)                 " Application server performance category - #GENERATED#
                                      et_app_storage_qty      = DATA(lt_app_storage_qty)                   " Application server storage amount - #GENERATED#
                                      et_app_server           = DATA(lt_app_server)                        " Application server - #GENERATED#
                                      et_app_storage          = DATA(lt_app_storage)                       " Application server storage - #GENERATED#
                                      et_app_backup           = DATA(lt_app_backup)                        " App storage backup - #GENERATED#
                                      et_phase                = DATA(lt_phase)              ).             " App storage backup - #GENERATED#

    "clear in case of a refresh
    IF lt_landscape IS NOT INITIAL.
      me->clear( ). "vorerst auskommentiert, sonst können keine Konfigurationen angelegt werden (create), denn dann ist der Baum leer.
    ENDIF.

    " ******************************
    " Get instance of text provider
    " ******************************
    DATA(lo_text_provider) = /hec1/cl_config_text_provider=>get_instance( /hec1/if_config_constants=>gc_classname-text_provider ).


    " ******************************
    " Landscape
    " ******************************
    ASSIGN lt_landscape[ 1 ] TO FIELD-SYMBOL(<fs_landscape>).
    IF <fs_landscape> IS NOT ASSIGNED.
      RETURN. " >>>>>>>>
    ENDIF.

    APPEND VALUE #( parent_key         = space
                    row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_landscape>-key )
                    node_key           = <fs_landscape>-key
                    expanded           = abap_true
                    is_leaf            = abap_false
                    image_src          = SWITCH #( <fs_landscape>-hec_instance_status
                                                   WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                   THEN /hec1/if_config_constants=>gc_image_status-complete
                                                   ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                    text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-landscape
                                                                      para1 = COND #( WHEN <fs_landscape>-hec_landscape_descr IS NOT INITIAL AND
                                                                                           <fs_landscape>-hec_landscape_descr NA |:|
                                                                                      THEN |: { <fs_landscape>-hec_landscape_descr }|
                                                                                      ELSE <fs_landscape>-hec_landscape_descr                    ) )
                    hec_lead_selection = abap_true
                    hec_row_selectable = abap_true
                    hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-landscape
                    crea_date_time     = <fs_landscape>-crea_date_time
                    change_request     = <fs_landscape>-change_request                                                                                ) TO me->mt_tree.


    " ******************************
    " Delivery Unit
    " ******************************
    ASSIGN lt_delivery_unit[ 1 ] TO FIELD-SYMBOL(<fs_delivery_unit>).
    IF <fs_delivery_unit> IS NOT ASSIGNED.
      RETURN. " >>>>>>>>
    ENDIF.

    APPEND VALUE #( parent_key          = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-landscape )
                    row_key             = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_delivery_unit>-key )
                    parent_node_key     = <fs_delivery_unit>-parent_key
                    node_key            = <fs_delivery_unit>-key
                    expanded            = abap_true
                    is_leaf             = abap_true
                    image_src           = SWITCH #( <fs_delivery_unit>-hec_instance_status
                                                    WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                    THEN /hec1/if_config_constants=>gc_image_status-complete
                                                    ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                    text                = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-delivery_unit
                                                                      para1 = COND #( WHEN <fs_delivery_unit>-hec_delivery_unit_descr IS NOT INITIAL AND
                                                                                           <fs_delivery_unit>-hec_delivery_unit_descr NA |:|
                                                                                      THEN |: { <fs_delivery_unit>-hec_delivery_unit_descr }|
                                                                                      ELSE <fs_delivery_unit>-hec_delivery_unit_descr                    ) )
                    hec_row_selectable = abap_true
                    hec_add_visible    = abap_true
                    hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-delivery_unit
                    crea_date_time     = <fs_delivery_unit>-crea_date_time
                    change_request     = <fs_delivery_unit>-change_request                                                                                     ) TO me->mt_tree.


    " ******************************
    " Folder Data Center
    " ******************************
    APPEND VALUE #( parent_key         = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-delivery_unit )
                    row_key            = /rbp/cl_general_utilities=>get_new_guid22( )
                    expanded           = abap_true
                    is_leaf            = abap_true
                    image_src          = /hec1/if_config_constants=>gc_image_status-folder
                    text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-datacenter_fl
                                                                     para1 = ' '      )
                    hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-datacenter_fl                                       ) TO me->mt_tree.


    " ******************************
    " Datacenter
    " ******************************
    LOOP AT lt_datacenter ASSIGNING FIELD-SYMBOL(<fs_datacenter>).

      APPEND VALUE #( parent_key         = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-datacenter_fl )
                      row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_datacenter>-key )
                      parent_node_key    = <fs_datacenter>-parent_key
                      node_key           = <fs_datacenter>-key
                      expanded           = abap_false
                      is_leaf            = abap_true
                      image_src          = SWITCH #( <fs_datacenter>-hec_instance_status
                                                     WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                     THEN /hec1/if_config_constants=>gc_image_status-complete
                                                     ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                      text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-datacenter
                                                                       para1 = COND #( WHEN <fs_datacenter>-hec_tree_descr IS NOT INITIAL AND
                                                                                            <fs_datacenter>-hec_tree_descr NA |:|
                                                                                       THEN |: { <fs_datacenter>-hec_tree_descr }|
                                                                                       ELSE <fs_datacenter>-hec_tree_descr                    ) )
                      hec_delete_visible = COND #( WHEN <fs_datacenter>-hec_phase_guid IS NOT INITIAL
                                                   THEN abap_false
                                                   ELSE abap_true )
                      hec_row_selectable = abap_true
                      hec_add_visible    = abap_true
                      hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-datacenter
                      hec_phase_guid     = <fs_datacenter>-hec_phase_guid
                      crea_date_time     = <fs_datacenter>-crea_date_time
                      change_request     = <fs_datacenter>-change_request                                                                             ) TO me->mt_tree.


      " ******************************
      " Connectivity
      " ******************************
      LOOP AT lt_connectivity ASSIGNING FIELD-SYMBOL(<fs_connectivity>)
        WHERE parent_key = <fs_datacenter>-key.

        APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_datacenter>-key )
                        row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_connectivity>-key )
                        parent_node_key    = <fs_datacenter>-key
                        node_key           = <fs_connectivity>-key
                        expanded           = abap_false
                        is_leaf            = abap_true
                        image_src          = SWITCH #( <fs_connectivity>-hec_instance_status
                                                       WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                       THEN /hec1/if_config_constants=>gc_image_status-complete
                                                       ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                        text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-connectivity
                                                                         para1 = COND #( WHEN <fs_connectivity>-hec_tree_descr IS NOT INITIAL AND
                                                                                              <fs_connectivity>-hec_tree_descr NA |:|
                                                                                         THEN |: { <fs_connectivity>-hec_tree_descr }|
                                                                                         ELSE <fs_connectivity>-hec_tree_descr                    ) )
                        hec_row_selectable = <fs_connectivity>-hec_row_selectable
                        hec_delete_visible = abap_true
                        hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-connectivity
                        hec_phase_guid     = <fs_connectivity>-hec_phase_guid
                        crea_date_time     = <fs_connectivity>-crea_date_time
                        change_request     = <fs_connectivity>-change_request                                                                           ) TO me->mt_tree.

      ENDLOOP. " LOOP AT lt_connectivity...
    ENDLOOP. " LOOP AT lt_datacenter ASSIGNING...


    " ******************************
    " Folder Additional Service
    " ******************************
    APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_landscape>-key )
                    row_key            = /rbp/cl_general_utilities=>get_new_guid22( )
                    expanded           = abap_true
                    is_leaf            = abap_true
                    image_src          = /hec1/if_config_constants=>gc_image_status-folder
                    text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-add_service_fl
                                                                     para1 = ' '      )
                    hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-add_service_fl                                   ) TO me->mt_tree.


    " ******************************
    " Additional Services
    " ******************************
    LOOP AT lt_add_service ASSIGNING FIELD-SYMBOL(<fs_add_service>).

      APPEND VALUE #( parent_key         = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-add_service_fl )
                      row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_add_service>-key )
                      parent_node_key    = <fs_add_service>-parent_key
                      node_key           = <fs_add_service>-key
                      expanded           = abap_false
                      is_leaf            = abap_true
                      image_src          = SWITCH #( <fs_add_service>-hec_instance_status
                                                     WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                     THEN /hec1/if_config_constants=>gc_image_status-complete
                                                     ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                      text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-add_service
                                                                       para1 = COND #( WHEN <fs_add_service>-hec_tree_descr IS NOT INITIAL AND
                                                                                            <fs_add_service>-hec_tree_descr NA |:|
                                                                                       THEN |: { <fs_add_service>-hec_tree_descr }|
                                                                                       ELSE <fs_add_service>-hec_tree_descr                    ) )
                      hec_delete_visible = abap_true
                      hec_row_selectable = abap_true
                      hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-add_service
                      hec_phase_guid     = <fs_add_service>-hec_phase_guid
                      crea_date_time     = <fs_add_service>-crea_date_time
                      change_request     = <fs_add_service>-change_request                                                                          ) TO me->mt_tree.
    ENDLOOP.


    " ******************************
    " Folder Longterm Backup
    " ******************************
    APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_landscape>-key )
                    row_key            = /rbp/cl_general_utilities=>get_new_guid22( )
                    expanded           = abap_true
                    is_leaf            = abap_true
                    image_src          = /hec1/if_config_constants=>gc_image_status-folder
                    text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-lt_backup_fl
                                                                     para1 = ' '      )
                    hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-lt_backup_fl                                   ) TO me->mt_tree.


    " ******************************
    " Longterm Backup Datacenter
    " ******************************
    LOOP AT lt_longterm_backup_dc ASSIGNING FIELD-SYMBOL(<fs_longterm_backup_dc>).

      APPEND VALUE #( parent_key         = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-lt_backup_fl )
                      row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_longterm_backup_dc>-key )
                      parent_node_key    = <fs_longterm_backup_dc>-parent_key
                      node_key           = <fs_longterm_backup_dc>-key
                      expanded           = abap_false
                      is_leaf            = abap_true
                      image_src          = SWITCH #( <fs_longterm_backup_dc>-hec_instance_status
                                                     WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                     THEN /hec1/if_config_constants=>gc_image_status-complete
                                                     ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                      text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-ltbckup_dc
                                                                       para1 = COND #( WHEN <fs_longterm_backup_dc>-hec_tree_descr IS NOT INITIAL AND
                                                                                            <fs_longterm_backup_dc>-hec_tree_descr NA |:|
                                                                                       THEN |: { <fs_longterm_backup_dc>-hec_tree_descr }|
                                                                                       ELSE <fs_longterm_backup_dc>-hec_tree_descr                    ) )
                      hec_delete_visible = abap_true
                      hec_row_selectable = abap_true
                      hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-lt_backup_dc
                      hec_phase_guid     = <fs_longterm_backup_dc>-hec_phase_guid
                      crea_date_time     = <fs_longterm_backup_dc>-crea_date_time
                      change_request     = <fs_longterm_backup_dc>-change_request                                                                          ) TO me->mt_tree.


      " ******************************
      " Longterm Backup Class
      " ******************************
      LOOP AT lt_longterm_backup_cl ASSIGNING FIELD-SYMBOL(<fs_longterm_backup_cl>)
          WHERE parent_key = <fs_longterm_backup_dc>-key.

        APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_longterm_backup_dc>-key )
                        row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_longterm_backup_cl>-key )
                        parent_node_key    = <fs_longterm_backup_cl>-parent_key
                        node_key           = <fs_longterm_backup_cl>-key
                        expanded           = abap_true
                        is_leaf            = abap_false
                        image_src          = SWITCH #( <fs_longterm_backup_cl>-hec_instance_status
                                                       WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                       THEN /hec1/if_config_constants=>gc_image_status-complete
                                                       ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                        text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-ltbckup_class
                                                                         para1 = COND #( WHEN <fs_longterm_backup_cl>-hec_tree_descr IS NOT INITIAL AND
                                                                                              <fs_longterm_backup_cl>-hec_tree_descr NA |:|
                                                                                         THEN |: { <fs_longterm_backup_cl>-hec_tree_descr }|
                                                                                         ELSE <fs_longterm_backup_cl>-hec_tree_descr                    ) )
                        hec_delete_visible = abap_true
                        hec_row_selectable = abap_true
                        hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-lt_backup_class
                        hec_phase_guid     = <fs_longterm_backup_cl>-hec_phase_guid
                        crea_date_time     = <fs_longterm_backup_cl>-crea_date_time
                        change_request     = <fs_longterm_backup_cl>-change_request                                                                          ) TO me->mt_tree.

        " ******************************
        " Longterm Backup Amount
        " ******************************
        LOOP AT lt_longterm_backup_am ASSIGNING FIELD-SYMBOL(<fs_longterm_backup_am>)
            WHERE parent_key = <fs_longterm_backup_cl>-key.

          APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_longterm_backup_cl>-key )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_longterm_backup_am>-key )
                          parent_node_key    = <fs_longterm_backup_am>-parent_key
                          node_key           = <fs_longterm_backup_am>-key
                          expanded           = abap_false
                          is_leaf            = abap_true
                          image_src          = SWITCH #( <fs_longterm_backup_am>-hec_instance_status
                                                         WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                         THEN /hec1/if_config_constants=>gc_image_status-complete
                                                         ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-ltbckup_amount
                                                                           para1 = COND #( WHEN <fs_longterm_backup_am>-hec_tree_descr IS NOT INITIAL AND
                                                                                                <fs_longterm_backup_am>-hec_tree_descr NA |:|
                                                                                           THEN |: { <fs_longterm_backup_am>-hec_tree_descr }|
                                                                                           ELSE <fs_longterm_backup_am>-hec_tree_descr                    ) )
                          hec_delete_visible = abap_true
                          hec_row_selectable = abap_true
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-lt_backup_amount
                          hec_phase_guid     = <fs_longterm_backup_am>-hec_phase_guid
                          crea_date_time     = <fs_longterm_backup_am>-crea_date_time
                          change_request     = <fs_longterm_backup_am>-change_request                                                                          ) TO me->mt_tree.
        ENDLOOP.
      ENDLOOP.
    ENDLOOP.

    " ******************************
    " Folder Add Storage
    " ******************************
    APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_landscape>-key )
                    row_key            = /rbp/cl_general_utilities=>get_new_guid22( )
                    expanded           = abap_true
                    is_leaf            = abap_true
                    image_src          = /hec1/if_config_constants=>gc_image_status-folder
                    text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-add_storage_fl
                                                                     para1 = ' '      )
                    hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-add_storage_fl                                   ) TO me->mt_tree.

    " ******************************
    " Add Storage Datacenter
    " ******************************
    LOOP AT lt_add_storage_dc ASSIGNING FIELD-SYMBOL(<fs_add_storage_dc>).

      APPEND VALUE #( parent_key         = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-add_storage_fl )
                      row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_add_storage_dc>-key )
                      parent_node_key    = <fs_add_storage_dc>-parent_key
                      node_key           = <fs_add_storage_dc>-key
                      expanded           = abap_false
                      is_leaf            = abap_true
                      image_src          = SWITCH #( <fs_add_storage_dc>-hec_instance_status
                                                     WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                     THEN /hec1/if_config_constants=>gc_image_status-complete
                                                     ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                      text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-astorage_dc
                                                                       para1 = COND #( WHEN <fs_add_storage_dc>-hec_tree_descr IS NOT INITIAL AND
                                                                                            <fs_add_storage_dc>-hec_tree_descr NA |:|
                                                                                       THEN |: { <fs_add_storage_dc>-hec_tree_descr }|
                                                                                       ELSE <fs_add_storage_dc>-hec_tree_descr                    ) )
                      hec_delete_visible = abap_true
                      hec_row_selectable = abap_true
                      hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-astorage_dc
                      hec_phase_guid     = <fs_add_storage_dc>-hec_phase_guid
                      crea_date_time     = <fs_add_storage_dc>-crea_date_time
                      change_request     = <fs_add_storage_dc>-change_request                                                                          ) TO me->mt_tree.


      " ******************************
      " Add Storage Class
      " ******************************
      LOOP AT lt_add_storage_cl ASSIGNING FIELD-SYMBOL(<fs_add_storage_cl>)
          WHERE parent_key = <fs_add_storage_dc>-key.

        APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_add_storage_dc>-key )
                        row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_add_storage_cl>-key )
                        parent_node_key    = <fs_add_storage_cl>-parent_key
                        node_key           = <fs_add_storage_cl>-key
                        expanded           = abap_true
                        is_leaf            = abap_false
                        image_src          = SWITCH #( <fs_add_storage_cl>-hec_instance_status
                                                       WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                       THEN /hec1/if_config_constants=>gc_image_status-complete
                                                       ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                        text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-astorage_class
                                                                         para1 = COND #( WHEN <fs_add_storage_cl>-hec_tree_descr IS NOT INITIAL AND
                                                                                              <fs_add_storage_cl>-hec_tree_descr NA |:|
                                                                                         THEN |: { <fs_add_storage_cl>-hec_tree_descr }|
                                                                                         ELSE <fs_add_storage_cl>-hec_tree_descr                    ) )
                        hec_delete_visible = abap_true
                        hec_row_selectable = abap_true
                        hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-astorage_class
                        hec_phase_guid     = <fs_add_storage_cl>-hec_phase_guid
                        crea_date_time     = <fs_add_storage_cl>-crea_date_time
                        change_request     = <fs_add_storage_cl>-change_request                                                                          ) TO me->mt_tree.

        " ******************************
        " Add Storage Amount
        " ******************************
        LOOP AT lt_add_storage_am ASSIGNING FIELD-SYMBOL(<fs_add_storage_am>)
            WHERE parent_key = <fs_add_storage_cl>-key.

          APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_add_storage_cl>-key )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_add_storage_am>-key )
                          parent_node_key    = <fs_add_storage_am>-parent_key
                          node_key           = <fs_add_storage_am>-key
                          expanded           = abap_false
                          is_leaf            = abap_true
                          image_src          = SWITCH #( <fs_add_storage_am>-hec_instance_status
                                                         WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                         THEN /hec1/if_config_constants=>gc_image_status-complete
                                                         ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-astorage_amount
                                                                           para1 = COND #( WHEN <fs_add_storage_am>-hec_tree_descr IS NOT INITIAL AND
                                                                                                <fs_add_storage_am>-hec_tree_descr NA |:|
                                                                                           THEN |: { <fs_add_storage_am>-hec_tree_descr }|
                                                                                           ELSE <fs_add_storage_am>-hec_tree_descr                    ) )
                          hec_delete_visible = abap_true
                          hec_row_selectable = abap_true
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-astorage_amount
                          hec_phase_guid     = <fs_add_storage_am>-hec_phase_guid
                          crea_date_time     = <fs_add_storage_am>-crea_date_time
                          change_request     = <fs_add_storage_am>-change_request                                                                          ) TO me->mt_tree.
        ENDLOOP.
      ENDLOOP.
    ENDLOOP.


    " ******************************
    " Folder Solution
    " ******************************
    APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_landscape>-key )
                    row_key            = /rbp/cl_general_utilities=>get_new_guid22( )
                    expanded           = abap_true
                    is_leaf            = abap_true
                    image_src          = /hec1/if_config_constants=>gc_image_status-folder
                    text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-solution_fl
                                                                     para1 = ' '      )
                    hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-solution_fl                                       ) TO me->mt_tree.


    " ******************************
    " Solution
    " ******************************
    LOOP AT lt_solution ASSIGNING FIELD-SYMBOL(<fs_solution>).

      APPEND VALUE #( parent_key         = me->get_parent_key( iv_object_type = /hec1/if_config_constants=>gc_tree_child-solution_fl )
                      row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_solution>-key )
                      parent_node_key    = <fs_solution>-parent_key
                      node_key           = <fs_solution>-key
                      expanded           = abap_true
                      is_leaf            = abap_true
                      image_src          = SWITCH #( <fs_solution>-hec_instance_status
                                                     WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                     THEN /hec1/if_config_constants=>gc_image_status-complete
                                                     ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                      text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-solution
                                                                       para1 = COND #( WHEN <fs_solution>-hec_tree_descr IS NOT INITIAL AND
                                                                                            <fs_solution>-hec_tree_descr NA |:|
                                                                                       THEN |{ <fs_solution>-hec_tree_descr }|
                                                                                       ELSE <fs_solution>-hec_tree_descr                    ) )
                      hec_delete_visible = abap_true
                      hec_row_selectable = abap_true
                      hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-solution
                      crea_date_time     = <fs_solution>-crea_date_time
                      change_request     = <fs_solution>-change_request                                                                          ) TO me->mt_tree.


      " ******************************
      " Tier
      " ******************************
      LOOP AT lt_tier ASSIGNING FIELD-SYMBOL(<fs_tier>)
        WHERE parent_key = <fs_solution>-key.

        APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_solution>-key )
                        row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_tier>-key )
                        parent_node_key    = <fs_tier>-parent_key
                        node_key           = <fs_tier>-key
                        expanded           = abap_false
                        is_leaf            = abap_true
                        image_src          = SWITCH #( <fs_tier>-hec_instance_status
                                                       WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                       THEN /hec1/if_config_constants=>gc_image_status-complete
                                                       ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                        text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-tier
                                                                         para1 = COND #( WHEN <fs_tier>-hec_tree_descr IS NOT INITIAL AND
                                                                                              <fs_tier>-hec_tree_descr NA |:|
                                                                                         THEN |: { <fs_tier>-hec_tree_descr }|
                                                                                         ELSE <fs_tier>-hec_tree_descr                    ) )
                        hec_row_selectable = <fs_tier>-hec_row_selectable
                        hec_delete_visible = abap_true
                        hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-tier
                        crea_date_time     = <fs_tier>-crea_date_time
                        hec_phase_guid     = <fs_tier>-hec_phase_guid
                        hec_sort_order     = SWITCH #( <fs_tier>-hec_tier_type_value
                                                       " Sort range for tier 20-50
                                                       WHEN ''                                                    THEN 1 " Unknown
                                                       WHEN /hec1/if_config_constants=>gc_tier_type-sandbox       THEN 2 " Sandbox
                                                       WHEN /hec1/if_config_constants=>gc_tier_type-development   THEN 3 " Development
                                                       WHEN /hec1/if_config_constants=>gc_tier_type-quality       THEN 4 " Quality
                                                       WHEN /hec1/if_config_constants=>gc_tier_type-preprod       THEN 5 " Pre production
                                                       WHEN /hec1/if_config_constants=>gc_tier_type-production    THEN 6 " Production
                                                       )
                        change_request     = <fs_tier>-change_request ) TO me->mt_tree.


        " ******************************
        " Folder Tier SLA
        " ******************************
        APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_tier>-key )
                        row_key            = /rbp/cl_general_utilities=>get_new_guid22( )
                        expanded           = abap_false
                        is_leaf            = abap_true
                        image_src          = /hec1/if_config_constants=>gc_image_status-folder
                        text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-tier_sla_fl
                                                                         para1 = ' '      )
                        hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-tier_sla_fl                                       ) TO me->mt_tree.

        " ******************************
        " tier sla
        " ******************************
        LOOP AT lt_tier_sla ASSIGNING FIELD-SYMBOL(<fs_tier_sla>)
          WHERE parent_key = <fs_tier>-key.

          APPEND VALUE #( parent_key         = me->get_parent_key( iv_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_tier>-key )
                                                                   iv_object_type = /hec1/if_config_constants=>gc_tree_child-tier_sla_fl            )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_tier_sla>-key )
                          parent_node_key    = <fs_tier_sla>-parent_key
                          node_key           = <fs_tier_sla>-key
                          expanded           = abap_false
                          is_leaf            = abap_true
                          image_src          = SWITCH #( <fs_tier_sla>-hec_instance_status
                                                         WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                         THEN /hec1/if_config_constants=>gc_image_status-complete
                                                         ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-tier_sla
                                                                           para1 = COND #( WHEN <fs_tier_sla>-hec_tree_descr IS NOT INITIAL AND
                                                                                                <fs_tier_sla>-hec_tree_descr NA |:|
                                                                                           THEN |: { <fs_tier_sla>-hec_tree_descr }|
                                                                                           ELSE <fs_tier_sla>-hec_tree_descr                    ) )
                          hec_row_selectable = <fs_tier_sla>-hec_row_selectable
                          hec_delete_visible = <fs_tier_sla>-hec_delete_visible
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-tier_sla
                          hec_phase_guid     = <fs_tier_sla>-hec_phase_guid
                          crea_date_time     = <fs_tier_sla>-crea_date_time
                          change_request     = <fs_tier_sla>-change_request                                                                            ) TO me->mt_tree.

        ENDLOOP. " lt_tier_sla

        " ******************************
        " Folder Software
        " ******************************
        APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_tier>-key )
                        row_key            = /rbp/cl_general_utilities=>get_new_guid22( )
                        expanded           = abap_false
                        is_leaf            = abap_true
                        image_src          = /hec1/if_config_constants=>gc_image_status-folder
                        text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-software_fl
                                                                         para1 = ' '      )
                        hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-software_fl                                       ) TO me->mt_tree.


        " ******************************
        " Material
        " ******************************
        LOOP AT lt_material ASSIGNING FIELD-SYMBOL(<fs_material>)
          WHERE parent_key = <fs_tier>-key.

          APPEND VALUE #( parent_key         = me->get_parent_key( iv_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_tier>-key )
                                                                   iv_object_type = /hec1/if_config_constants=>gc_tree_child-software_fl            )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_material>-key )
                          parent_node_key    = <fs_material>-parent_key
                          node_key           = <fs_material>-key
                          expanded           = abap_false
                          is_leaf            = abap_true
                          image_src          = SWITCH #( <fs_material>-hec_instance_status
                                                         WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                         THEN /hec1/if_config_constants=>gc_image_status-complete
                                                         ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-material
                                                                           para1 = COND #( WHEN <fs_material>-hec_tree_descr IS NOT INITIAL AND
                                                                                                <fs_material>-hec_tree_descr NA |:|
                                                                                           THEN |: { <fs_material>-hec_tree_descr }|
                                                                                           ELSE <fs_material>-hec_tree_descr                    ) )
                          hec_row_selectable = <fs_material>-hec_row_selectable
                          hec_delete_visible = abap_true
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-material
                          hec_phase_guid     = <fs_material>-hec_phase_guid
                          crea_date_time     = <fs_material>-crea_date_time
                          change_request     = <fs_material>-change_request                                                                            ) TO me->mt_tree.


          " ******************************
          " Software Item
          " ******************************
          LOOP AT lt_software_item ASSIGNING FIELD-SYMBOL(<fs_software_item>)
            WHERE parent_key = <fs_material>-key.

            APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_software_item>-parent_key )
                            row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_software_item>-key )
                            parent_node_key    = <fs_software_item>-parent_key
                            node_key           = <fs_software_item>-key
                            expanded           = abap_false
                            is_leaf            = abap_true
                            image_src          = SWITCH #( <fs_software_item>-hec_instance_status
                                                           WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                           THEN /hec1/if_config_constants=>gc_image_status-complete
                                                           ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                            text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-software_item
                                                                             para1 = COND #( WHEN <fs_software_item>-hec_tree_descr IS NOT INITIAL AND
                                                                                                  <fs_software_item>-hec_tree_descr NA |:|
                                                                                             THEN |: { <fs_software_item>-hec_tree_descr }|
                                                                                             ELSE <fs_software_item>-hec_tree_descr                    ) )
                            hec_row_selectable = <fs_software_item>-hec_row_selectable
                            hec_delete_visible = abap_true
                            hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-software_item
                            hec_phase_guid     = <fs_software_item>-hec_phase_guid
                            crea_date_time     = <fs_software_item>-crea_date_time
                            change_request     = <fs_software_item>-change_request                                                                          ) TO me->mt_tree.

          ENDLOOP. " LOOP AT lt_software_item...
        ENDLOOP. " LOOP AT lt_material...


        " ******************************
        " Folder Additional Tier Service
        " ******************************
        APPEND VALUE #( parent_key   = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_tier>-key )
                        row_key      = /rbp/cl_general_utilities=>get_new_guid22( )
                        expanded     = abap_false
                        is_leaf      = abap_true
                        image_src    = /hec1/if_config_constants=>gc_image_status-folder
                        text         = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-tier_service_fl
                                                                   para1 = ' '      )
                        hec_obj_type = /hec1/if_config_constants=>gc_tree_child-tier_serv_fl                                          ) TO me->mt_tree.


        " ******************************
        " Tier Additional Services
        " ******************************
        LOOP AT lt_tier_add_service ASSIGNING FIELD-SYMBOL(<fs_tier_add_service>)
          WHERE parent_key = <fs_tier>-key.

          APPEND VALUE #( parent_key         = me->get_parent_key( iv_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_tier>-key )
                                                                   iv_object_type = /hec1/if_config_constants=>gc_tree_child-tier_serv_fl           )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_tier_add_service>-key )
                          parent_node_key    = <fs_tier_add_service>-parent_key
                          node_key           = <fs_tier_add_service>-key
                          expanded           = abap_false
                          is_leaf            = abap_true
                          image_src          = SWITCH #( <fs_tier_add_service>-hec_instance_status
                                                         WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                         THEN /hec1/if_config_constants=>gc_image_status-complete
                                                         ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-tier_service
                                                                           para1 = COND #( WHEN <fs_tier_add_service>-hec_tree_descr IS NOT INITIAL AND
                                                                                                <fs_tier_add_service>-hec_tree_descr NA |:|
                                                                                           THEN |: { <fs_tier_add_service>-hec_tree_descr }|
                                                                                           ELSE <fs_tier_add_service>-hec_tree_descr                    ) )
                          hec_row_selectable = <fs_tier_add_service>-hec_row_selectable
                          hec_delete_visible = abap_true
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-tier_service
                          hec_phase_guid     = <fs_tier_add_service>-hec_phase_guid
                          crea_date_time     = <fs_tier_add_service>-crea_date_time
                          change_request     = <fs_tier_add_service>-change_request                                                                          ) TO me->mt_tree.
        ENDLOOP.


        " ******************************
        " Tier Longterm Backup Folder
        " ******************************
        APPEND VALUE #( parent_key   = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_tier>-key )
                        row_key      = /rbp/cl_general_utilities=>get_new_guid22( )
                        expanded     = abap_false
                        is_leaf      = abap_true
                        image_src    = /hec1/if_config_constants=>gc_image_status-folder
                        text         = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-tier_ltbup_fl
                                                                   para1 = ' '      )
                        hec_obj_type = /hec1/if_config_constants=>gc_tree_child-tier_ltbup_fl                                          ) TO me->mt_tree.


        " ******************************
        " Tier Longterm Backup
        " ******************************
        LOOP AT lt_tier_longterm_backup ASSIGNING FIELD-SYMBOL(<fs_tier_longterm_backup>)
          WHERE parent_key = <fs_tier>-key.

          APPEND VALUE #( parent_key         = me->get_parent_key( iv_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_tier>-key )
                                                                   iv_object_type = /hec1/if_config_constants=>gc_tree_child-tier_ltbup_fl          )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_tier_longterm_backup>-key )
                          parent_node_key    = <fs_tier_longterm_backup>-parent_key
                          node_key           = <fs_tier_longterm_backup>-key
                          expanded           = abap_false
                          is_leaf            = abap_true
                          image_src          = SWITCH #( <fs_tier_longterm_backup>-hec_instance_status
                                                         WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                         THEN /hec1/if_config_constants=>gc_image_status-complete
                                                         ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-tier_ltbup
                                                                           para1 = COND #( WHEN <fs_tier_longterm_backup>-hec_tree_descr IS NOT INITIAL AND
                                                                                                <fs_tier_longterm_backup>-hec_tree_descr NA |:|
                                                                                           THEN |: { <fs_tier_longterm_backup>-hec_tree_descr }|
                                                                                           ELSE <fs_tier_longterm_backup>-hec_tree_descr                    ) )
                          hec_row_selectable = <fs_tier_longterm_backup>-hec_row_selectable
                          hec_delete_visible = abap_true
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-tier_ltbup
                          hec_phase_guid     = <fs_tier_longterm_backup>-hec_phase_guid
                          crea_date_time     = <fs_tier_longterm_backup>-crea_date_time
                          change_request     = <fs_tier_longterm_backup>-change_request                                                                          ) TO me->mt_tree.
        ENDLOOP.



        " ******************************
        " Tier Add Storage Folder
        " ******************************
        APPEND VALUE #( parent_key   = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_tier>-key )
                        row_key      = /rbp/cl_general_utilities=>get_new_guid22( )
                        expanded     = abap_false
                        is_leaf      = abap_true
                        image_src    = /hec1/if_config_constants=>gc_image_status-folder
                        text         = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-tier_a_stor_fl
                                                                   para1 = ' '      )
                        hec_obj_type = /hec1/if_config_constants=>gc_tree_child-tier_astor_fl                                          ) TO me->mt_tree.


        " ******************************
        " Tier Add Storage - parked
        " ******************************
*        LOOP AT lt_tier_add_storage ASSIGNING FIELD-SYMBOL(<fs_tier_add_storage>)
*          WHERE parent_key = <fs_tier>-key.
*
*          APPEND VALUE #( parent_key         = me->get_parent_key( iv_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_tier>-key )
*                                                                   iv_object_type = /hec1/if_config_constants=>gc_tree_child-tier_astor_fl          )
*                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_tier_add_storage>-key )
*                          parent_node_key    = <fs_tier_add_storage>-parent_key
*                          node_key           = <fs_tier_add_storage>-key
*                          expanded           = abap_false
*                          is_leaf            = abap_true
*                          image_src          = SWITCH #( <fs_tier_add_storage>-hec_instance_status
*                                                         WHEN /hec1/if_config_constants=>gc_instance_status-complete
*                                                         THEN /hec1/if_config_constants=>gc_image_status-complete
*                                                         ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
*                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-tier_astor
*                                                                           para1 = COND #( WHEN <fs_tier_add_storage>-hec_tree_descr IS NOT INITIAL AND
*                                                                                                <fs_tier_add_storage>-hec_tree_descr NA |:|
*                                                                                           THEN |: { <fs_tier_add_storage>-hec_tree_descr }|
*                                                                                           ELSE <fs_tier_add_storage>-hec_tree_descr                    ) )
*                          hec_row_selectable = <fs_tier_add_storage>-hec_row_selectable
*                          hec_delete_visible = abap_true
*                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-tier_astor
*                          hec_phase_guid     = <fs_tier_add_storage>-hec_phase_guid
*                          crea_date_time     = <fs_tier_add_storage>-crea_date_time
*                          change_request     = <fs_tier_add_storage>-change_request                                                                          ) TO me->mt_tree.
*        ENDLOOP.


        " ******************************
        " DB Server Instance
        " ******************************
        LOOP AT lt_db_serv_inst ASSIGNING FIELD-SYMBOL(<fs_db_server_inst>)
          WHERE parent_key = <fs_tier>-key.

          APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_tier>-key )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_db_server_inst>-key )
                          parent_node_key    = <fs_db_server_inst>-parent_key
                          node_key           = <fs_db_server_inst>-key
                          expanded           = abap_false
                          is_leaf            = abap_true
                          image_src          = SWITCH #( <fs_db_server_inst>-hec_instance_status
                                                         WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                         THEN /hec1/if_config_constants=>gc_image_status-complete
                                                         ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-db_serv_inst
                                                                           para1 = COND #( WHEN <fs_db_server_inst>-hec_tree_descr IS NOT INITIAL AND
                                                                                                <fs_db_server_inst>-hec_tree_descr NA |:|
                                                                                           THEN |: { <fs_db_server_inst>-hec_tree_descr }|
                                                                                           ELSE <fs_db_server_inst>-hec_tree_descr                    ) )
                          hec_row_selectable = <fs_db_server_inst>-hec_row_selectable
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-db_serv_inst
                          hec_phase_guid     = <fs_db_server_inst>-hec_phase_guid
                          crea_date_time     = <fs_db_server_inst>-crea_date_time
                          change_request     = <fs_db_server_inst>-change_request                                                                          ) TO me->mt_tree.


          " ******************************
          " Instance DB
          " ******************************
          LOOP AT lt_instance_db ASSIGNING FIELD-SYMBOL(<fs_instance_db>)
            WHERE parent_key = <fs_db_server_inst>-key.

            APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_instance_db>-parent_key )
                            row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_instance_db>-key )
                            parent_node_key    = <fs_instance_db>-parent_key
                            node_key           = <fs_instance_db>-key
                            expanded           = abap_false
                            is_leaf            = abap_true
                            image_src          = SWITCH #( <fs_instance_db>-hec_instance_status
                                                           WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                           THEN /hec1/if_config_constants=>gc_image_status-complete
                                                           ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                            text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-db_inst
                                                                             para1 = COND #( WHEN <fs_instance_db>-hec_tree_descr IS NOT INITIAL AND
                                                                                                  <fs_instance_db>-hec_tree_descr NA |:|
                                                                                       THEN |: { <fs_instance_db>-hec_tree_descr }|
                                                                                       ELSE <fs_instance_db>-hec_tree_descr                          ) )
                            hec_row_selectable = <fs_instance_db>-hec_row_selectable
                            hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-db_inst
                            hec_phase_guid     = <fs_instance_db>-hec_phase_guid
                            hec_sort_order      = SWITCH #( <fs_instance_db>-hec_db_node_type_value
                                                            WHEN /hec1/if_config_constants=>gc_db_node_type-container THEN 1
                                                            WHEN /hec1/if_config_constants=>gc_db_node_type-single    THEN 2
                                                            WHEN /hec1/if_config_constants=>gc_db_node_type-tenant    THEN 3 )
                            change_request     = <fs_instance_db>-change_request                                               ) TO me->mt_tree.

            " ******************************
            " DB Node
            " ******************************
            SORT lt_db_node ASCENDING BY hec_db_cluster_type_value.

            LOOP AT lt_db_node ASSIGNING FIELD-SYMBOL(<fs_db_node>)
              WHERE parent_key = <fs_instance_db>-key.

              APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_db_node>-parent_key )
                              row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_db_node>-key )
                              parent_node_key    = <fs_db_node>-parent_key
                              node_key           = <fs_db_node>-key
                              expanded           = abap_false
                              is_leaf            = abap_true
                              image_src          = SWITCH #( <fs_db_node>-hec_instance_status
                                                             WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                             THEN /hec1/if_config_constants=>gc_image_status-complete
                                                             ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                              text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-db_node
                                                                               para1 = COND #( WHEN <fs_db_node>-hec_tree_descr IS NOT INITIAL AND
                                                                                                    <fs_db_node>-hec_tree_descr NA |:|
                                                                                               THEN |: { <fs_db_node>-hec_tree_descr }|
                                                                                               ELSE <fs_db_node>-hec_tree_descr                    ) )
                              hec_row_selectable = <fs_db_node>-hec_row_selectable
                              hec_delete_visible = COND #( WHEN <fs_db_node>-hec_master_default = abap_true
                                                           THEN abap_false
                                                           ELSE abap_true )
                              hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-db_node
                              hec_phase_guid     = <fs_db_node>-hec_phase_guid
                              hec_sort_order     = SWITCH #( <fs_db_node>-hec_db_node_type_value
                                                             WHEN /hec1/if_config_constants=>gc_db_clust_node_type-master  THEN 1
                                                             WHEN /hec1/if_config_constants=>gc_db_clust_node_type-standby THEN 2
                                                             WHEN /hec1/if_config_constants=>gc_db_clust_node_type-worker  THEN 3 )
                              change_request     = <fs_db_node>-change_request                                                       ) TO me->mt_tree.

              " ******************************
              " DB Server Performance Category
              " ******************************
              LOOP AT lt_db_serv_perf_cat ASSIGNING FIELD-SYMBOL(<fs_db_server_pc>)
                WHERE parent_key = <fs_db_node>-key.

                APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_db_server_pc>-parent_key )
                                row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_db_server_pc>-key )
                                parent_node_key    = <fs_db_server_pc>-parent_key
                                node_key           = <fs_db_server_pc>-key
                                expanded           = abap_false
                                is_leaf            = abap_true
                                image_src          = SWITCH #( <fs_db_server_pc>-hec_instance_status
                                                               WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                               THEN /hec1/if_config_constants=>gc_image_status-complete
                                                               ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                                text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-db_serv_pc
                                                                                 para1 = COND #( WHEN <fs_db_server_pc>-hec_tree_descr IS NOT INITIAL AND
                                                                                                      <fs_db_server_pc>-hec_tree_descr NA |:|
                                                                                                 THEN |: { <fs_db_server_pc>-hec_tree_descr }|
                                                                                                 ELSE <fs_db_server_pc>-hec_tree_descr                    ) )
                                hec_row_selectable = <fs_db_server_pc>-hec_row_selectable
                                hec_delete_visible = abap_true
                                hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-db_serv_pc
                                hec_phase_guid     = <fs_db_server_pc>-hec_phase_guid
                                crea_date_time     = <fs_db_server_pc>-crea_date_time
                                change_request     = <fs_db_server_pc>-change_request                                                                          ) TO me->mt_tree.


                " ******************************
                " DB Storage Quantity
                " ******************************
                LOOP AT lt_db_storage_qty ASSIGNING FIELD-SYMBOL(<fs_db_storage_qty>)
                  WHERE parent_key = <fs_db_server_pc>-key.

                  APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_db_storage_qty>-parent_key )
                                  row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_db_storage_qty>-key )
                                  parent_node_key    = <fs_db_storage_qty>-parent_key
                                  node_key           = <fs_db_storage_qty>-key
                                  expanded           = abap_false
                                  is_leaf            = abap_true
                                  image_src          = SWITCH #( <fs_db_storage_qty>-hec_instance_status
                                                                 WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                 THEN /hec1/if_config_constants=>gc_image_status-complete
                                                                 ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                                  text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-db_storage_qty
                                                                                   para1 = COND #( WHEN <fs_db_storage_qty>-hec_tree_descr IS NOT INITIAL AND
                                                                                                        <fs_db_storage_qty>-hec_tree_descr NA |:|
                                                                                                   THEN |: { <fs_db_storage_qty>-hec_tree_descr }|
                                                                                                   ELSE <fs_db_storage_qty>-hec_tree_descr                    ) )
                                  hec_row_selectable = <fs_db_storage_qty>-hec_row_selectable
                                  hec_delete_visible = abap_true
                                  hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-db_storage_qty
                                  hec_phase_guid     = <fs_db_storage_qty>-hec_phase_guid
                                  hec_successor_guid = <fs_db_storage_qty>-hec_successor_guid
                                  crea_date_time     = <fs_db_storage_qty>-crea_date_time
                                  change_request     = <fs_db_storage_qty>-change_request                                                                          ) TO me->mt_tree.

                ENDLOOP. " LOOP AT lt_db_storage_qty...


                " ******************************
                " DB Server
                " ******************************
                LOOP AT lt_db_server ASSIGNING FIELD-SYMBOL(<fs_db_server>)
                  WHERE parent_key = <fs_db_server_pc>-key.

                  APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_db_server>-parent_key )
                                  row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_db_server>-key )
                                  parent_node_key    = <fs_db_server>-parent_key
                                  node_key           = <fs_db_server>-key
                                  expanded           = abap_false
                                  is_leaf            = abap_true
                                  image_src          = SWITCH #( <fs_db_server>-hec_instance_status
                                                                 WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                 THEN /hec1/if_config_constants=>gc_image_status-complete
                                                                 ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                                  text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-db_server
                                                                                   para1 = COND #( WHEN <fs_db_server>-hec_tree_descr IS NOT INITIAL AND
                                                                                                        <fs_db_server>-hec_tree_descr NA |:|
                                                                                                   THEN |: { <fs_db_server>-hec_tree_descr }|
                                                                                                   ELSE <fs_db_server>-hec_tree_descr                    ) )
                                  hec_row_selectable = <fs_db_server>-hec_row_selectable
                                  hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-db_server
                                  hec_phase_guid     = <fs_db_server>-hec_phase_guid
                                  crea_date_time     = <fs_db_server>-crea_date_time
                                  change_request     = <fs_db_server>-change_request                                                                          ) TO me->mt_tree.


                  " ******************************
                  " DB storage
                  " ******************************
                  LOOP AT lt_db_storage ASSIGNING FIELD-SYMBOL(<fs_db_storage>)
                    WHERE parent_key = <fs_db_server>-key.

                    APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_db_storage>-parent_key )
                                    row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_db_storage>-key )
                                    parent_node_key    = <fs_db_storage>-parent_key
                                    node_key           = <fs_db_storage>-key
                                    expanded           = abap_false
                                    is_leaf            = abap_true
                                    image_src          = SWITCH #( <fs_db_storage>-hec_instance_status
                                                                   WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                   THEN /hec1/if_config_constants=>gc_image_status-complete
                                                                   ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                                    text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-db_storage
                                                                                     para1 = COND #( WHEN <fs_db_storage>-hec_tree_descr IS NOT INITIAL AND
                                                                                                          <fs_db_storage>-hec_tree_descr NA |:|
                                                                                                     THEN |: { <fs_db_storage>-hec_tree_descr }|
                                                                                                     ELSE <fs_db_storage>-hec_tree_descr                    ) )
                                    hec_row_selectable = <fs_db_storage>-hec_row_selectable
                                    hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-db_storage
                                    hec_phase_guid     = <fs_db_storage>-hec_phase_guid
                                    hec_successor_guid = <fs_db_storage>-hec_successor_guid
                                    crea_date_time     = <fs_db_storage>-crea_date_time
                                    change_request     = <fs_db_storage>-change_request                                                                          ) TO me->mt_tree.


                    " ******************************
                    " DB backup
                    " ******************************
                    LOOP AT lt_db_backup ASSIGNING FIELD-SYMBOL(<fs_db_backup>)
                      WHERE parent_key = <fs_db_storage>-key.

                      APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_db_backup>-parent_key )
                                      row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_db_backup>-key )
                                      parent_node_key    = <fs_db_backup>-parent_key
                                      node_key           = <fs_db_backup>-key
                                      expanded           = abap_false
                                      is_leaf            = abap_true
                                      image_src          = SWITCH #( <fs_db_backup>-hec_instance_status
                                                                     WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                     THEN /hec1/if_config_constants=>gc_image_status-complete
                                                                     ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                                      text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-db_backup
                                                                                       para1 = COND #( WHEN <fs_db_backup>-hec_tree_descr IS NOT INITIAL AND
                                                                                                            <fs_db_backup>-hec_tree_descr NA |:|
                                                                                                       THEN |: { <fs_db_backup>-hec_tree_descr }|
                                                                                                       ELSE <fs_db_backup>-hec_tree_descr                    ) )
                                      hec_row_selectable = <fs_db_backup>-hec_row_selectable
                                      hec_delete_visible = abap_true
                                      hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-db_backup
                                      hec_phase_guid     = <fs_db_backup>-hec_phase_guid
                                      hec_successor_guid = <fs_db_backup>-hec_successor_guid
                                      crea_date_time     = <fs_db_backup>-crea_date_time
                                      change_request     = <fs_db_backup>-change_request                                                                          ) TO me->mt_tree.

                    ENDLOOP. " LOOP AT lt_db_backup...
                  ENDLOOP. " LOOP AT lt_db_storage...
                ENDLOOP. " LOOP AT lt_db_server...
              ENDLOOP. " LOOP AT lt_db_serv_perf_cat...
            ENDLOOP. " LOOP AT lt_db_node...
          ENDLOOP. " LOOP AT lt_instance_db...
        ENDLOOP. " LOOP AT lt_db_serv_inst...


        " ******************************
        " App Server Instance
        " ******************************
        LOOP AT lt_app_serv_inst ASSIGNING FIELD-SYMBOL(<fs_app_server_inst>)
          WHERE parent_key = <fs_tier>-key.

          APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_tier>-key )
                          row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_app_server_inst>-key )
                          parent_node_key    = <fs_app_server_inst>-parent_key
                          node_key           = <fs_app_server_inst>-key
                          expanded           = abap_false
                          is_leaf            = abap_true
                          image_src          = SWITCH #( <fs_app_server_inst>-hec_instance_status
                                                         WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                         THEN /hec1/if_config_constants=>gc_image_status-complete
                                                         ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                          text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-app_serv_inst
                                                                           para1 = COND #( WHEN <fs_app_server_inst>-hec_tree_descr IS NOT INITIAL AND
                                                                                                <fs_app_server_inst>-hec_tree_descr NA |:|
                                                                                           THEN |: { <fs_app_server_inst>-hec_tree_descr }|
                                                                                           ELSE <fs_app_server_inst>-hec_tree_descr                    ) )
                          hec_row_selectable = <fs_app_server_inst>-hec_row_selectable
                          hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-app_serv_inst
                          hec_phase_guid     = <fs_app_server_inst>-hec_phase_guid
                          crea_date_time     = <fs_app_server_inst>-crea_date_time
                          change_request     = <fs_app_server_inst>-change_request                                                                          ) TO me->mt_tree.


          " ******************************
          " App Node
          " ******************************
          SORT lt_app_node ASCENDING BY hec_app_clust_node_type_value.

          LOOP AT lt_app_node ASSIGNING FIELD-SYMBOL(<fs_app_node>)
            WHERE parent_key = <fs_app_server_inst>-key.

            APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_app_node>-parent_key )
                            row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_app_node>-key )
                            parent_node_key    = <fs_app_node>-parent_key
                            node_key           = <fs_app_node>-key
                            expanded           = abap_false
                            is_leaf            = abap_true
                            image_src          = SWITCH #( <fs_app_node>-hec_instance_status
                                                           WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                           THEN /hec1/if_config_constants=>gc_image_status-complete
                                                           ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                            text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-app_node
                                                                             para1 = COND #( WHEN <fs_app_node>-hec_tree_descr IS NOT INITIAL AND
                                                                                                  <fs_app_node>-hec_tree_descr NA |:|
                                                                                             THEN |: { <fs_app_node>-hec_tree_descr }|
                                                                                             ELSE <fs_app_node>-hec_tree_descr                    ) )
                            hec_row_selectable = <fs_app_node>-hec_row_selectable
                            hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-app_node
                            hec_phase_guid     = <fs_app_node>-hec_phase_guid
                            hec_sort_order     = SWITCH #( <fs_app_node>-hec_app_clust_node_type_value
                                                            WHEN /hec1/if_config_constants=>gc_app_clust_node_type-master  THEN 1
                                                            WHEN /hec1/if_config_constants=>gc_app_clust_node_type-standby THEN 2
                                                            WHEN /hec1/if_config_constants=>gc_app_clust_node_type-worker  THEN 3  )
                            change_request     = <fs_app_node>-change_request                                                        ) TO me->mt_tree.


            " ******************************
            " App Server Performance Category
            " ******************************
            LOOP AT lt_app_serv_perf_cat ASSIGNING FIELD-SYMBOL(<fs_app_server_pc>)
              WHERE parent_key = <fs_app_node>-key.

              APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_app_server_pc>-parent_key )
                              row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_app_server_pc>-key )
                              parent_node_key    = <fs_app_server_pc>-parent_key
                              node_key           = <fs_app_server_pc>-key
                              expanded           = abap_false
                              is_leaf            = abap_true
                              image_src          = SWITCH #( <fs_app_server_pc>-hec_instance_status
                                                             WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                             THEN /hec1/if_config_constants=>gc_image_status-complete
                                                             ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                              text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-app_serv_pc
                                                                               para1 = COND #( WHEN <fs_app_server_pc>-hec_tree_descr IS NOT INITIAL AND
                                                                                                    <fs_app_server_pc>-hec_tree_descr NA |:|
                                                                                               THEN |: { <fs_app_server_pc>-hec_tree_descr }|
                                                                                               ELSE <fs_app_server_pc>-hec_tree_descr                    ) )
                              hec_row_selectable = <fs_app_server_pc>-hec_row_selectable
                              hec_delete_visible = abap_true
                              hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-app_serv_pc
                              hec_phase_guid     = <fs_app_server_pc>-hec_phase_guid
                              hec_successor_guid = <fs_app_server_pc>-hec_successor_guid
                              crea_date_time     = <fs_app_server_pc>-crea_date_time
                              change_request     = <fs_app_server_pc>-change_request                                                                          ) TO me->mt_tree.


              " ******************************
              " App Storage Quantity
              " ******************************
              LOOP AT lt_app_storage_qty ASSIGNING FIELD-SYMBOL(<fs_app_storage_qty>)
                WHERE parent_key = <fs_app_server_pc>-key.

                APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_app_storage_qty>-parent_key )
                                row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_app_storage_qty>-key )
                                parent_node_key    = <fs_app_storage_qty>-parent_key
                                node_key           = <fs_app_storage_qty>-key
                                expanded           = abap_false
                                is_leaf            = abap_true
                                image_src          = SWITCH #( <fs_app_storage_qty>-hec_instance_status
                                                               WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                               THEN /hec1/if_config_constants=>gc_image_status-complete
                                                               ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                                text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-app_storage_qty
                                                                                 para1 = COND #( WHEN <fs_app_storage_qty>-hec_tree_descr IS NOT INITIAL AND
                                                                                                      <fs_app_storage_qty>-hec_tree_descr NA |:|
                                                                                                 THEN |: { <fs_app_storage_qty>-hec_tree_descr }|
                                                                                                 ELSE <fs_app_storage_qty>-hec_tree_descr                    ) )
                                hec_row_selectable = <fs_app_storage_qty>-hec_row_selectable
                                hec_delete_visible = abap_true
                                hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-app_storage_qty
                                hec_phase_guid     = <fs_app_storage_qty>-hec_phase_guid
                                hec_successor_guid = <fs_app_storage_qty>-hec_successor_guid
                                crea_date_time     = <fs_app_storage_qty>-crea_date_time
                                change_request     = <fs_app_storage_qty>-change_request                                                                          ) TO me->mt_tree.

              ENDLOOP. " LOOP AT lt_app_storage_qty...


              " ******************************
              " App Server
              " ******************************
              LOOP AT lt_app_server ASSIGNING FIELD-SYMBOL(<fs_app_server>)
                WHERE parent_key = <fs_app_server_pc>-key.

                APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_app_server>-parent_key )
                                row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_app_server>-key )
                                parent_node_key    = <fs_app_server>-parent_key
                                node_key           = <fs_app_server>-key
                                expanded           = abap_false
                                is_leaf            = abap_true
                                image_src          = SWITCH #( <fs_app_server>-hec_instance_status
                                                               WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                               THEN /hec1/if_config_constants=>gc_image_status-complete
                                                               ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                                text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-app_server
                                                                                 para1 = COND #( WHEN <fs_app_server>-hec_tree_descr IS NOT INITIAL AND
                                                                                                      <fs_app_server>-hec_tree_descr NA |:|
                                                                                                 THEN |: { <fs_app_server>-hec_tree_descr }|
                                                                                                 ELSE <fs_app_server>-hec_tree_descr                     ) )
                                hec_row_selectable = <fs_app_server>-hec_row_selectable
                                hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-app_server
                                hec_phase_guid     = <fs_app_server>-hec_phase_guid
                                crea_date_time     = <fs_app_server>-crea_date_time
                                change_request     = <fs_app_server>-change_request                                                                          ) TO me->mt_tree.


                " ******************************
                " App storage
                " ******************************
                LOOP AT lt_app_storage ASSIGNING FIELD-SYMBOL(<fs_app_storage>)
                  WHERE parent_key = <fs_app_server>-key.

                  APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_app_storage>-parent_key )
                                  row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_app_storage>-key )
                                  parent_node_key    = <fs_app_storage>-parent_key
                                  node_key           = <fs_app_storage>-key
                                  expanded           = abap_false
                                  is_leaf            = abap_true
                                  image_src          = SWITCH #( <fs_app_storage>-hec_instance_status
                                                                 WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                 THEN /hec1/if_config_constants=>gc_image_status-complete
                                                                 ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                                  text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-app_storage
                                                                                   para1 = COND #( WHEN <fs_app_storage>-hec_tree_descr IS NOT INITIAL AND
                                                                                                        <fs_app_storage>-hec_tree_descr NA |:|
                                                                                                   THEN |: { <fs_app_storage>-hec_tree_descr }|
                                                                                                   ELSE <fs_app_storage>-hec_tree_descr                    ) )
                                  hec_row_selectable = <fs_app_storage>-hec_row_selectable
                                  hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-app_storage
                                  hec_phase_guid     = <fs_app_storage>-hec_phase_guid
                                  hec_successor_guid = <fs_app_storage>-hec_successor_guid
                                  crea_date_time     = <fs_app_storage>-crea_date_time
                                  change_request     = <fs_app_storage>-change_request                                                                          ) TO me->mt_tree.


                  " ******************************
                  " App backup
                  " ******************************
                  LOOP AT lt_app_backup ASSIGNING FIELD-SYMBOL(<fs_app_backup>)
                    WHERE parent_key = <fs_app_storage>-key.

                    APPEND VALUE #( parent_key         = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_app_backup>-parent_key )
                                    row_key            = /hec1/cl_config_helper=>convert_key_2_uuid_c22( <fs_app_backup>-key )
                                    parent_node_key    = <fs_app_backup>-parent_key
                                    node_key           = <fs_app_backup>-key
                                    expanded           = abap_false
                                    is_leaf            = abap_true
                                    image_src          = SWITCH #( <fs_app_backup>-hec_instance_status
                                                                   WHEN /hec1/if_config_constants=>gc_instance_status-complete
                                                                   THEN /hec1/if_config_constants=>gc_image_status-complete
                                                                   ELSE /hec1/if_config_constants=>gc_image_status-incomplete  )
                                    text               = lo_text_provider->get_text( key   = /hec1/if_config_constants=>gc_tree_text_id-app_backup
                                                                                     para1 = COND #( WHEN <fs_app_backup>-hec_tree_descr IS NOT INITIAL AND
                                                                                                          <fs_app_backup>-hec_tree_descr NA |:|
                                                                                                     THEN |: { <fs_app_backup>-hec_tree_descr }|
                                                                                                     ELSE <fs_app_backup>-hec_tree_descr                    ) )
                                    hec_row_selectable = <fs_app_backup>-hec_row_selectable
                                    hec_delete_visible = abap_true
                                    hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-app_backup
                                    hec_phase_guid     = <fs_app_backup>-hec_phase_guid
                                    hec_successor_guid = <fs_app_backup>-hec_successor_guid
                                    crea_date_time     = <fs_app_backup>-crea_date_time
                                    change_request     = <fs_app_backup>-change_request                                                                          ) TO me->mt_tree.

                  ENDLOOP. " LOOP AT lt_app_backup...
                ENDLOOP. " LOOP AT lt_app_storage...
              ENDLOOP. " LOOP AT lt_app_server...
            ENDLOOP. " LOOP AT lt_app_serv_perf_cat...
          ENDLOOP. " LOOP AT lt_app_node...
        ENDLOOP. " LOOP AT lt_app_serv_inst...
      ENDLOOP. " LOOP AT lt_tier...
    ENDLOOP. " LOOP AT lt_solution...

    " ******************************
    " Phasing Tree - Phases
    " ******************************
    " For the phases we cannot create the hierarchy by using the BOPF Key and Parent key. We need to use the PHASE_GUID and PARENT_PHASE_GUID instead

    LOOP AT lt_phase ASSIGNING FIELD-SYMBOL(<fs_phase>).

      APPEND VALUE #( BASE CORRESPONDING #( <fs_phase> )
                      parent_key         = <fs_phase>-hec_node_parent_phase
                      row_key            = <fs_phase>-hec_node_phase
*                      parent_node_key    = <fs_phase>-parent_key
                      node_key           = <fs_phase>-key
                      hec_row_selectable = abap_true
                      expanded           = abap_true
                      is_leaf            = abap_true
                      text               = <fs_phase>-hec_phase_tree_descr
                      hec_delete_visible = abap_true
                      hec_obj_type       = /hec1/if_config_constants=>gc_tree_child-phase
                      hec_lead_selection = COND #( WHEN <fs_phase>-hec_default_phase = abap_true
                                                   THEN abap_true
                                                   ELSE abap_false ) ) TO me->mt_tree_phasing.

    ENDLOOP. " LOOP AT lt_phase...

    " Clear Top Phase Key
    LOOP AT me->mt_tree_phasing ASSIGNING FIELD-SYMBOL(<fs_tree_phasing>).
      IF NOT line_exists( me->mt_tree_phasing[ row_key = <fs_tree_phasing>-parent_key ] ).
        CLEAR <fs_tree_phasing>-parent_key.
      ENDIF.
    ENDLOOP.

    " Distribution Tree
    " Turn last entry in a branch into a leaf
    LOOP AT me->mt_tree ASSIGNING FIELD-SYMBOL(<fs_tree>) FROM 2.
      TRY.
          me->mt_tree[ row_key = <fs_tree>-parent_key ]-is_leaf = abap_false.
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.
    ENDLOOP.

    " Phasing tree
    " Turn last entry in a branch into a leaf
    LOOP AT me->mt_tree_phasing ASSIGNING <fs_tree_phasing>.
      TRY.
          me->mt_tree_phasing[ row_key = <fs_tree_phasing>-parent_key ]-is_leaf = abap_false.
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.
    ENDLOOP.

    me->sort_tree_phasing( ).
    me->sort_tree_distribut( ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~get_lead_selection_pa_node_key.

    CASE iv_tree_type.

        " Distribution Tree
      WHEN /hec1/if_config_constants=>gc_tree_type-distribution.
        TRY.
            rv_key = me->mt_tree[ hec_lead_selection = abap_true ]-parent_node_key.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        " Phasing Tree
      WHEN /hec1/if_config_constants=>gc_tree_type-phasing.
*        TRY.
*            rv_key = me->mt_tree_phasing[ hec_lead_selection = abap_true ]-parent_node_key.
*          CATCH cx_sy_itab_line_not_found.
*        ENDTRY.
    ENDCASE.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~set_expand_flag.

    CHECK iv_index IS NOT INITIAL.

    CASE iv_tree_type.

        " Distribution Tree
      WHEN /hec1/if_config_constants=>gc_tree_type-distribution.

        TRY.
            me->mt_tree[ iv_index ]-expanded = abap_true.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

        " Phasing Tree
      WHEN /hec1/if_config_constants=>gc_tree_type-phasing.

        TRY.
            me->mt_tree_phasing[ iv_index ]-expanded = abap_true.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.

    ENDCASE.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~get_tree_line.

    TRY.
        rs_line = me->mt_tree[ row_key = iv_row_key ].
      CATCH cx_sy_itab_line_not_found.
    ENDTRY.

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~update.

    " ******************************
    " Update UI tree from BOPF
    " ******************************
    LOOP AT it_node ASSIGNING FIELD-SYMBOL(<fs_node>).

      " change distribution tree
      ASSIGN me->mt_tree[ parent_node_key = <fs_node>-parent_node_key
                          node_key        = <fs_node>-node_key        ] TO FIELD-SYMBOL(<fs_tree>).

      IF <fs_tree> IS ASSIGNED.

        DATA(ls_tree_old) = <fs_tree>.
        <fs_tree> = CORRESPONDING #( BASE ( <fs_tree> ) me->fill_tree_data( <fs_node> )
                                     EXCEPT row_key
                                            parent_key
                                            expanded
                                            is_leaf
                                            hec_lead_selection
                                            hec_delete_visible
                                            crea_date_time
                                            ).

*        <fs_tree> = CORRESPONDING #( me->fill_tree_data( <fs_node> )
*                                     EXCEPT expanded
*                                            is_leaf
*                                            crea_date_time ).
*
*        <fs_tree>-row_key = ls_tree_old-row_key.
*        <fs_tree>-parent_key = ls_tree_old-parent_key.
*        <fs_tree>-expanded = ls_tree_old-expanded.
*        <fs_tree>-is_leaf = ls_tree_old-is_leaf.
*        <fs_tree>-hec_lead_selection = ls_tree_old-hec_lead_selection.
*        <fs_tree>-hec_delete_visible = ls_tree_old-hec_delete_visible.

      ENDIF.

      UNASSIGN <fs_tree>.

    ENDLOOP.

    me->sort_tree_distribut(  ).

  ENDMETHOD.


  METHOD /hec1/if_bopf_config_ui_tree_h~delete.

    DATA: lt_buffer       LIKE me->mt_tree,
          lt_buffer_phase LIKE me->mt_tree_phasing.

    " get selection
    IF iv_tree_type = /hec1/if_config_constants=>gc_tree_type-distribution.
      ASSIGN me->mt_tree TO FIELD-SYMBOL(<fs_tree>).
      ASSIGN me->mt_tree[ node_key = iv_node_key ] TO FIELD-SYMBOL(<fs_line>).

      IF <fs_line> IS NOT ASSIGNED
        OR <fs_line>-hec_obj_type = /hec1/if_config_constants=>gc_tree_root
        OR <fs_line>-hec_obj_type CS '_FL'.
        RETURN. ">>>
      ENDIF.

      APPEND <fs_line> TO lt_buffer.

      DATA(ls_new_selection) = <fs_tree>[ row_key = <fs_line>-parent_key ].

      "********************
      " Delete tree entries
      "********************

      LOOP AT <fs_tree> ASSIGNING FIELD-SYMBOL(<fs_tree_line>).
        IF line_exists( lt_buffer[ node_key = <fs_tree_line>-parent_node_key ] ).
          APPEND CORRESPONDING #( <fs_tree_line> ) TO lt_buffer.
          DELETE <fs_tree>.
        ELSEIF line_exists( lt_buffer[ node_key = <fs_tree_line>-node_key ] )..
          DELETE <fs_tree>.
        ENDIF.
      ENDLOOP.

      "*********************
      " Define new selection
      "*********************

      IF NOT line_exists( <fs_tree>[ hec_lead_selection = abap_true ] ).
        TRY.
            IF ls_new_selection-hec_obj_type CS '_FL'.
*            <fs_tree>[ hec_lead_selection = abap_true ]-hec_lead_selection = abap_false.
              <fs_tree>[ row_key = ls_new_selection-parent_key ]-hec_lead_selection = abap_true.
            ELSE.
*            <fs_tree>[ hec_lead_selection = abap_true ]-hec_lead_selection = abap_false.
              <fs_tree>[ row_key = ls_new_selection-row_key ]-hec_lead_selection = abap_true.
            ENDIF.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.
      ENDIF. "no selection

      "If there is another branch of the same type, select this branch. Otherwise select the parent branch
      "Set selection in tree to parent branch -> This is done in FILL_TABLE and the application controller
      "Selecting a different branch is only necessary, if the currently selected branch is deleted. If a child node is deleted, the selection stays the same.

    ELSE. "Phasing Tree
      ASSIGN me->mt_tree_phasing TO FIELD-SYMBOL(<fs_tree_phase>).
      ASSIGN me->mt_tree_phasing[ node_key = iv_node_key ] TO FIELD-SYMBOL(<fs_line_phase>).

      IF <fs_line_phase> IS NOT ASSIGNED.
        RETURN. ">>>
      ENDIF.

      APPEND <fs_line_phase> TO lt_buffer_phase.

      TRY.
          DATA(ls_new_selection_phase) = <fs_tree_phase>[ row_key = <fs_line_phase>-parent_key ].
        CATCH cx_sy_itab_line_not_found.
          ls_new_selection_phase = <fs_tree_phase>[ 1 ].
      ENDTRY.

      "********************
      " Delete tree entries
      "********************

      LOOP AT <fs_tree_phase> ASSIGNING FIELD-SYMBOL(<fs_tree_line_phase>).
        IF line_exists( lt_buffer_phase[ row_key = <fs_tree_line_phase>-parent_key ] ).
          APPEND CORRESPONDING #( <fs_tree_line_phase> ) TO lt_buffer_phase.
          DELETE <fs_tree_phase>.
        ELSEIF line_exists( lt_buffer_phase[ row_key = <fs_tree_line_phase>-row_key ] )..
          DELETE <fs_tree_phase>.
        ENDIF.
      ENDLOOP.

      "*********************
      " Define new selection
      "*********************

      IF NOT line_exists( <fs_tree_phase>[ hec_lead_selection = abap_true ] ).
        TRY.
            IF ls_new_selection_phase-hec_obj_type CS '_FL'.
*            <fs_tree_phase>[ hec_lead_selection = abap_true ]-hec_lead_selection = abap_false.
              <fs_tree_phase>[ row_key = ls_new_selection_phase-parent_key ]-hec_lead_selection = abap_true.
            ELSE.
*            <fs_tree_phase>[ hec_lead_selection = abap_true ]-hec_lead_selection = abap_false.
              <fs_tree_phase>[ row_key = ls_new_selection_phase-row_key ]-hec_lead_selection = abap_true.
            ENDIF.
          CATCH cx_sy_itab_line_not_found.
        ENDTRY.
      ENDIF. "no selection

      "If there is another branch of the same type, select this branch. Otherwise select the parent branch
      "Set selection in tree to parent branch -> This is done in FILL_TABLE and the application controller
      "Selecting a different branch is only necessary, if the currently selected branch is deleted. If a child node is deleted, the selection stays the same.

    ENDIF. "iv_tree_type

    " Turn last entry in a branch into a leaf
    "Distribution
    LOOP AT me->mt_tree ASSIGNING <fs_tree_line> FROM 2.
      TRY.
          me->mt_tree[ row_key = <fs_tree_line>-parent_key ]-is_leaf = abap_false.
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.
    ENDLOOP.

    "Phasing
    LOOP AT me->mt_tree_phasing ASSIGNING FIELD-SYMBOL(<fs_tree_phasing>).
      TRY.
          me->mt_tree_phasing[ row_key = <fs_tree_phasing>-parent_key ]-is_leaf = abap_false.
        CATCH cx_sy_itab_line_not_found.
      ENDTRY.
    ENDLOOP.

  ENDMETHOD.
ENDCLASS.