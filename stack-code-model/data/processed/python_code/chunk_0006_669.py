*&---------------------------------------------------------------------*
*& Local class definition - Business Object Readers
*&---------------------------------------------------------------------*

INTERFACE lif_sst_constants.

  CONSTANTS: BEGIN OF cs_tabledef,
               fo_header_new TYPE /saptrx/strucdatadef VALUE 'TOR_ROOT',
               fo_header_old TYPE /saptrx/strucdatadef VALUE 'TOR_ROOT_BEFORE',
               fo_item_new   TYPE /saptrx/strucdatadef VALUE 'TOR_ITEM',
               fo_item_old   TYPE /saptrx/strucdatadef VALUE 'TOR_ITEM_BEFORE',
               fo_stop_new   TYPE /saptrx/strucdatadef VALUE 'TOR_STOP',
               fo_stop_old   TYPE /saptrx/strucdatadef VALUE 'TOR_STOP_BEFORE',
               fo_stop_addr  TYPE /saptrx/strucdatadef VALUE 'TOR_STOP_ADDR',
               fo_loc_addr   TYPE /saptrx/strucdatadef VALUE 'TOR_LOCATION_ADDR',
             END OF cs_tabledef.

  CONSTANTS: BEGIN OF cs_system_fields,
               actual_bisiness_timezone TYPE /saptrx/paramname VALUE 'ACTUAL_BUSINESS_TIMEZONE',
               actual_bisiness_datetime TYPE /saptrx/paramname VALUE 'ACTUAL_BUSINESS_DATETIME',
             END OF cs_system_fields.

  CONSTANTS: BEGIN OF cs_trxcod,
               fo_number   TYPE /saptrx/trxcod VALUE 'SHIPMENT_ORDER',
               fu_number   TYPE /saptrx/trxcod VALUE 'FREIGHT_UNIT',
               fo_resource TYPE /saptrx/trxcod VALUE 'RESOURCE',
             END OF cs_trxcod.

  CONSTANTS: BEGIN OF cs_milestone,
               fo_load_start    TYPE /saptrx/appl_event_tag VALUE 'LOAD_BEGIN',
               fo_load_end      TYPE /saptrx/appl_event_tag VALUE 'LOAD_END',
               fo_coupling      TYPE /saptrx/appl_event_tag VALUE 'COUPLING',
               fo_decoupling    TYPE /saptrx/appl_event_tag VALUE 'DECOUPLING',
               fo_shp_departure TYPE /saptrx/appl_event_tag VALUE 'DEPARTURE',
               fo_shp_arrival   TYPE /saptrx/appl_event_tag VALUE 'ARRIV_DEST',
               fo_shp_pod       TYPE /saptrx/appl_event_tag VALUE 'POD',
               fo_unload_start  TYPE /saptrx/appl_event_tag VALUE 'UNLOAD_BEGIN',
               fo_unload_end    TYPE /saptrx/appl_event_tag VALUE 'UNLOAD_END',
             END OF cs_milestone.

  CONSTANTS: BEGIN OF cs_location_type,
               logistic TYPE string VALUE 'LogisticLocation',
             END OF cs_location_type.

  CONSTANTS: BEGIN OF cs_lifecycle_status,
               draft      TYPE /scmtms/tor_lc_status VALUE '00',
               new        TYPE /scmtms/tor_lc_status VALUE '01',
               in_process TYPE /scmtms/tor_lc_status VALUE '02',
               completed  TYPE /scmtms/tor_lc_status VALUE '05',
               canceled   TYPE /scmtms/tor_lc_status VALUE '10',
             END OF cs_lifecycle_status.

  CONSTANTS: BEGIN OF cs_execution_status,
               not_relevant               TYPE /scmtms/tor_execution_status VALUE '01',
               not_started                TYPE /scmtms/tor_execution_status VALUE '02',
               in_execution               TYPE /scmtms/tor_execution_status VALUE '03',
               executed                   TYPE /scmtms/tor_execution_status VALUE '04',
               interrupted                TYPE /scmtms/tor_execution_status VALUE '05',
               canceled                   TYPE /scmtms/tor_execution_status VALUE '06',
               ready_for_transp_exec      TYPE /scmtms/tor_execution_status VALUE '07',
               not_ready_for_transp_exec  TYPE /scmtms/tor_execution_status VALUE '08',
               loading_in_process         TYPE /scmtms/tor_execution_status VALUE '09',
               capacity_planning_finished TYPE /scmtms/tor_execution_status VALUE '10',
             END OF cs_execution_status.

  CONSTANTS: BEGIN OF cs_track_exec_rel,
               no_execution                TYPE /scmtms/track_exec_rel VALUE '1',
               execution                   TYPE /scmtms/track_exec_rel VALUE '2',
               exec_with_extern_event_mngr TYPE /scmtms/track_exec_rel VALUE '3',
             END OF cs_track_exec_rel.

  CONSTANTS: BEGIN OF cs_trmodcod,
               road            TYPE /scmtms/trmodcode VALUE '01',
               rail            TYPE /scmtms/trmodcode VALUE '02',
               sea             TYPE /scmtms/trmodcode VALUE '03',
               inland_waterway TYPE /scmtms/trmodcode VALUE '04',
               air             TYPE /scmtms/trmodcode VALUE '05',
               postal_service  TYPE /scmtms/trmodcode VALUE '06',
               na              TYPE /scmtms/trmodcode VALUE '',
             END OF cs_trmodcod.
ENDINTERFACE.

CLASS lcl_bo_tor_reader DEFINITION.

  PUBLIC SECTION.
    INTERFACES: lif_bo_reader.

    METHODS constructor
      IMPORTING
        io_ef_parameters TYPE REF TO lif_ef_parameters.

  PROTECTED SECTION.

    TYPES: tv_tracked_object_type TYPE string,
           tt_tracked_object_type TYPE STANDARD TABLE OF tv_tracked_object_type WITH EMPTY KEY.

    TYPES: tv_tracked_object_id TYPE char20,
           tt_tracked_object_id TYPE STANDARD TABLE OF tv_tracked_object_type WITH EMPTY KEY.

    TYPES: tv_ref_doc_id TYPE /scmtms/btd_id,
           tt_ref_doc_id TYPE STANDARD TABLE OF tv_ref_doc_id WITH EMPTY KEY.

    TYPES: tv_ref_doc_type TYPE char35,
           tt_ref_doc_type TYPE STANDARD TABLE OF tv_ref_doc_type WITH EMPTY KEY.

    TYPES: tv_stop_id TYPE string,
           tt_stop_id TYPE STANDARD TABLE OF tv_stop_id WITH EMPTY KEY.

    TYPES: tv_ordinal_no TYPE int4,
           tt_ordinal_no TYPE STANDARD TABLE OF tv_ordinal_no WITH EMPTY KEY.

    TYPES: tv_loc_type TYPE /saptrx/loc_id_type,
           tt_loc_type TYPE STANDARD TABLE OF tv_loc_type WITH EMPTY KEY.

    TYPES: tv_loc_id TYPE /scmtms/location_id,
           tt_loc_id TYPE STANDARD TABLE OF tv_loc_id WITH EMPTY KEY.

    TYPES: tt_req_doc_line_number TYPE STANDARD TABLE OF int4 WITH EMPTY KEY.
    TYPES: tt_req_doc_number      TYPE STANDARD TABLE OF /scmtms/tor_id WITH EMPTY KEY.

    TYPES: tt_capacity_doc_line_number  TYPE STANDARD TABLE OF int4 WITH EMPTY KEY.
    TYPES: tt_capacity_doc_number TYPE STANDARD TABLE OF /scmtms/tor_id WITH EMPTY KEY.

    CONSTANTS:
      BEGIN OF cs_text_type,
        cont TYPE /bobf/txc_text_type VALUE 'CONT',
        mobl TYPE /bobf/txc_text_type VALUE 'MOBL',
      END OF cs_text_type,

      BEGIN OF cs_track_id,
        container_id  TYPE tv_tracked_object_type VALUE 'CONTAINER_ID',
        mobile_number TYPE tv_tracked_object_type VALUE 'MOBILE_NUMBER',
        truck_id      TYPE tv_tracked_object_type VALUE 'TRUCK_ID',
        license_plate TYPE tv_tracked_object_type VALUE 'LICENSE_PLATE',
        vessel        TYPE tv_tracked_object_type VALUE 'VESSEL',
      END OF cs_track_id,

      BEGIN OF cs_mapping,
        tor_id              TYPE /saptrx/paramname VALUE 'YN_SHP_NO',
        mtr                 TYPE /saptrx/paramname VALUE 'YN_SHP_MTR',
        gro_vol_val         TYPE /saptrx/paramname VALUE 'YN_SHP_VOLUMN',
        gro_vol_uni         TYPE /saptrx/paramname VALUE 'YN_SHP_VOLUMN_UOM',
        gro_wei_val         TYPE /saptrx/paramname VALUE 'YN_SHP_WEIGHT',
        gro_wei_uni         TYPE /saptrx/paramname VALUE 'YN_SHP_WEIGHT_UOM',
        qua_pcs_val         TYPE /saptrx/paramname VALUE 'YN_SHP_QUANTITY',
        qua_pcs_uni         TYPE /saptrx/paramname VALUE 'YN_SHP_QUANTITY_UOM',
        total_distance_km   TYPE /saptrx/paramname VALUE 'YN_SHP_TOTAL_DIST',
        dgo_indicator       TYPE /saptrx/paramname VALUE 'YN_SHP_CONTAIN_DGOODS',
        total_duration_net  TYPE /saptrx/paramname VALUE 'YN_SHP_PLAN_NET_DURAT',
        shipping_type       TYPE /saptrx/paramname VALUE 'YN_SHP_SHIPPING_TYPE',
        traffic_direct      TYPE /saptrx/paramname VALUE 'YN_SHP_TRAFFIC_DIRECT',
        trmodcod            TYPE /saptrx/paramname VALUE 'YN_SHP_TRANSPORTATION_MODE',
        tspid               TYPE /saptrx/paramname VALUE 'YN_SHP_SA_LBN_ID',
        tracked_object_id   TYPE /saptrx/paramname VALUE 'YN_SHP_TRACKED_RESOURCE_ID',
        tracked_object_type TYPE /saptrx/paramname VALUE 'YN_SHP_TRACKED_RESOURCE_VALUE',
        ref_doc_type        TYPE /saptrx/paramname VALUE 'YN_SHP_CARRIER_REF_TYPE',
        ref_doc_id          TYPE /saptrx/paramname VALUE 'YN_SHP_CARRIER_REF_VALUE',
        inc_class_code      TYPE /saptrx/paramname VALUE 'YN_SHP_INCOTERM',
        inc_transf_loc_n    TYPE /saptrx/paramname VALUE 'YN_SHP_INCOTERM_LOC',
        country             TYPE /saptrx/paramname VALUE 'YN_SHP_REG_COUNTRY',
        platenumber         TYPE /saptrx/paramname VALUE 'YN_SHP_REG_NUM',
        res_id              TYPE /saptrx/paramname VALUE 'YN_SHP_VEHICLE',
        pln_dep_loc_id      TYPE /saptrx/paramname VALUE 'YN_SHP_PLN_DEP_LOC_ID',
        pln_dep_loc_type    TYPE /saptrx/paramname VALUE 'YN_SHP_PLN_DEP_LOC_TYPE',
        pln_dep_timest      TYPE /saptrx/paramname VALUE 'YN_SHP_PLN_DEP_BUS_DATETIME',
        pln_dep_timezone    TYPE /saptrx/paramname VALUE 'YN_SHP_PLN_DEP_BUS_TIMEZONE',
        pln_arr_loc_id      TYPE /saptrx/paramname VALUE 'YN_SHP_PLN_AR_LOC_ID',
        pln_arr_loc_type    TYPE /saptrx/paramname VALUE 'YN_SHP_PLN_AR_LOC_TYPE',
        pln_arr_timest      TYPE /saptrx/paramname VALUE 'YN_SHP_PLN_AR_BUS_DATETIME',
        pln_arr_timezone    TYPE /saptrx/paramname VALUE 'YN_SHP_PLN_AR_BUS_TIMEZONE',
        pln_grs_duration    TYPE /saptrx/paramname VALUE 'YN_SHP_GROSS_DUR',
        stop_id             TYPE /saptrx/paramname VALUE 'YN_SHP_VP_STOP_ID',
        ordinal_no          TYPE /saptrx/paramname VALUE 'YN_SHP_VP_STOP_ORD_NO',
        loc_type            TYPE /saptrx/paramname VALUE 'YN_SHP_VP_STOP_LOC_TYPE',
        loc_id              TYPE /saptrx/paramname VALUE 'YN_SHP_VP_STOP_LOC_ID',
        item_id             TYPE /saptrx/paramname VALUE 'YN_SHP_DLV_ITM_FU_ITEM_ID',
        erp_dlv_id          TYPE /saptrx/paramname VALUE 'YN_SHP_DLV_ITM_ERP_DLV_ID',
        erp_dlv_item_id     TYPE /saptrx/paramname VALUE 'YN_SHP_DLV_ITM_ERP_DLV_ITM_ID',
        itm_qua_pcs_val     TYPE /saptrx/paramname VALUE 'YN_SHP_DLV_ITM_QUANTITY',
        itm_qua_pcs_uni     TYPE /saptrx/paramname VALUE 'YN_SHP_DLV_ITM_QUANTITY_UOM',
        product_id          TYPE /saptrx/paramname VALUE 'YN_SHP_DLV_ITM_PRODUCT_ID',
        product_txt         TYPE /saptrx/paramname VALUE 'YN_SHP_DLV_ITM_PRODUCT_TEXT',
        req_doc_line_no     TYPE /saptrx/paramname VALUE 'YN_SHP_REQ_DOC_LINE_NO',
        req_doc_no          TYPE /saptrx/paramname VALUE 'YN_SHP_REQ_DOC_NO',
        capa_doc_line_no    TYPE /saptrx/paramname VALUE 'YN_SHP_CAPA_DOC_LINE_NO',
        capa_doc_no         TYPE /saptrx/paramname VALUE 'YN_SHP_CAPA_DOC_NO',
        dlv_item_alt_id     TYPE /saptrx/paramname VALUE 'YN_SHP_DLV_ITM_ALT_ID',
        estimated_datetime  TYPE /saptrx/paramname VALUE 'YN_SHP_ESTIMATED_DATETIME',
        estimated_timezone  TYPE /saptrx/paramname VALUE 'YN_SHP_ESTIMATED_TIMEZONE',
      END OF cs_mapping,

      cs_bp_type TYPE bu_id_type VALUE 'LBN001'.

    DATA mo_ef_parameters TYPE REF TO lif_ef_parameters.

    METHODS get_data_from_text_collection
      IMPORTING
        ir_data         TYPE REF TO data
        iv_old_data     TYPE abap_bool DEFAULT abap_false
      EXPORTING
        er_text         TYPE REF TO /bobf/t_txc_txt_k
        er_text_content TYPE REF TO /bobf/t_txc_con_k
      RAISING
        cx_udm_message.

    METHODS get_container_and_mobile_track
      IMPORTING
        ir_data                TYPE REF TO data
        iv_old_data            TYPE abap_bool DEFAULT abap_false
      CHANGING
        ct_tracked_object_type TYPE tt_tracked_object_type
        ct_tracked_object_id   TYPE tt_tracked_object_id
      RAISING
        cx_udm_message.

    METHODS get_container_mobile_track_id
      IMPORTING
        is_app_object    TYPE trxas_appobj_ctab_wa
        iv_old_data      TYPE abap_bool DEFAULT abap_false
      CHANGING
        ct_track_id_data TYPE lif_ef_types=>tt_enh_track_id_data
      RAISING
        cx_udm_message.

    METHODS add_track_id_data
      IMPORTING
        is_app_object TYPE trxas_appobj_ctab_wa
        iv_trxcod     TYPE /saptrx/trxcod
        iv_trxid      TYPE /saptrx/trxid
        iv_action     TYPE /saptrx/action OPTIONAL
      CHANGING
        ct_track_id   TYPE lif_ef_types=>tt_track_id_data
      RAISING
        cx_udm_message.

    METHODS get_docref_data
      IMPORTING
        ir_root         TYPE REF TO data
        iv_old_data     TYPE abap_bool DEFAULT abap_false
      CHANGING
        ct_ref_doc_id   TYPE tt_ref_doc_id
        ct_ref_doc_type TYPE tt_ref_doc_type
      RAISING
        cx_udm_message.

    METHODS check_non_idoc_fields
      IMPORTING
        is_app_object    TYPE trxas_appobj_ctab_wa
      RETURNING
        VALUE(rv_result) TYPE lif_ef_types=>tv_condition
      RAISING
        cx_udm_message.

    METHODS check_non_idoc_status_fields
      IMPORTING
        is_app_object    TYPE trxas_appobj_ctab_wa
      RETURNING
        VALUE(rv_result) TYPE lif_ef_types=>tv_condition
      RAISING
        cx_udm_message.

    METHODS check_non_idoc_stop_fields
      IMPORTING
        is_app_object    TYPE trxas_appobj_ctab_wa
      RETURNING
        VALUE(rv_result) TYPE lif_ef_types=>tv_condition
      RAISING
        cx_udm_message.

    METHODS get_header_data_from_stop
      IMPORTING
        ir_data             TYPE REF TO data
        iv_old_data         TYPE abap_bool DEFAULT abap_false
        it_stop_seq         TYPE /scmtms/t_pln_stop_seq_d
      CHANGING
        cv_pln_dep_loc_id   TYPE /scmtms/s_em_bo_tor_stop-log_locid
        cv_pln_dep_loc_type TYPE /saptrx/loc_id_type
        cv_pln_dep_timest   TYPE char16
        cv_pln_dep_timezone TYPE ad_tzone
        cv_pln_arr_loc_id   TYPE /scmtms/s_em_bo_tor_stop-log_locid
        cv_pln_arr_loc_type TYPE /saptrx/loc_id_type
        cv_pln_arr_timest   TYPE char16
        cv_pln_arr_timezone TYPE ad_tzone
      RAISING
        cx_udm_message.

    METHODS get_stop_seq
      IMPORTING
        ir_data       TYPE REF TO data
        iv_old_data   TYPE abap_bool DEFAULT abap_false
        it_stop_seq   TYPE /scmtms/t_pln_stop_seq_d
      CHANGING
        ct_stop_id    TYPE tt_stop_id
        ct_ordinal_no TYPE tt_ordinal_no
        ct_loc_type   TYPE tt_loc_type
        ct_loc_id     TYPE tt_loc_id
      RAISING
        cx_udm_message.

    METHODS get_data_from_stop
      IMPORTING
        ir_data             TYPE REF TO data
        iv_old_data         TYPE abap_bool DEFAULT abap_false
      CHANGING
        cv_pln_dep_loc_id   TYPE /scmtms/s_em_bo_tor_stop-log_locid
        cv_pln_dep_loc_type TYPE /saptrx/loc_id_type
        cv_pln_dep_timest   TYPE char16
        cv_pln_dep_timezone TYPE ad_tzone
        cv_pln_arr_loc_id   TYPE /scmtms/s_em_bo_tor_stop-log_locid
        cv_pln_arr_loc_type TYPE /saptrx/loc_id_type
        cv_pln_arr_timest   TYPE char16
        cv_pln_arr_timezone TYPE ad_tzone
        ct_stop_id          TYPE tt_stop_id
        ct_ordinal_no       TYPE tt_ordinal_no
        ct_loc_type         TYPE tt_loc_type
        ct_loc_id           TYPE tt_loc_id
      RAISING
        cx_udm_message.

    METHODS get_customizing_aot
      IMPORTING
        iv_tor_type   TYPE /scmtms/tor_type
      RETURNING
        VALUE(rv_aot) TYPE /saptrx/aotype.

    METHODS get_requirement_doc_list
      IMPORTING
        ir_data            TYPE REF TO data
        iv_old_data        TYPE abap_bool DEFAULT abap_false
      CHANGING
        ct_req_doc_line_no TYPE tt_req_doc_line_number
        ct_req_doc_no      TYPE tt_req_doc_number
      RAISING
        cx_udm_message.

    METHODS get_carrier_name
      IMPORTING
        iv_tspid          TYPE bu_id_number
      RETURNING
        VALUE(rv_carrier) TYPE bu_id_number
      RAISING
        cx_udm_message.

ENDCLASS.

CLASS lcl_bo_tor_reader IMPLEMENTATION.

  METHOD constructor.
    mo_ef_parameters = io_ef_parameters.
  ENDMETHOD.

  METHOD get_carrier_name.

    CONSTANTS lc_lbn TYPE char4 VALUE 'LBN#'.

    SELECT SINGLE idnumber
      FROM but0id
      INTO @DATA(lv_idnumber)
      WHERE partner = @iv_tspid AND
            type    = @cs_bp_type.
    IF sy-subrc = 0.
      rv_carrier = lc_lbn && lv_idnumber.
    ENDIF.

  ENDMETHOD.

  METHOD get_requirement_doc_list.

    DATA lv_freight_unit_line_no TYPE int4.

    FIELD-SYMBOLS:
      <ls_tor_root>        TYPE /scmtms/s_em_bo_tor_root,
      <lt_tor_root_req>    TYPE /scmtms/t_em_bo_tor_root,
      <lt_tor_root_req_tu> TYPE /scmtms/t_em_bo_tor_root.

    ASSIGN ir_data->* TO <ls_tor_root>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    DATA(lv_tabledef_fu) = SWITCH #( iv_old_data
                             WHEN abap_false THEN /scmtms/cl_scem_int_c=>sc_table_definition-bo_tor-req_root
                             ELSE /scmtms/cl_scem_int_c=>sc_table_definition-bo_tor-req_root_before ).

    DATA(lr_req_root) = mo_ef_parameters->get_appl_table( iv_tabledef = lv_tabledef_fu ).
    ASSIGN lr_req_root->* TO <lt_tor_root_req>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO lv_dummy.
      lcl_tools=>throw_exception( ).
    ENDIF.

    DATA(lo_tor_srv_mgr) = /bobf/cl_tra_serv_mgr_factory=>get_service_manager( iv_bo_key = /scmtms/if_tor_c=>sc_bo_key ).
    lo_tor_srv_mgr->retrieve_by_association(
      EXPORTING
        iv_node_key    = /scmtms/if_tor_c=>sc_node-root
        it_key         = VALUE #( ( key = <ls_tor_root>-node_id ) )
        iv_association = /scmtms/if_tor_c=>sc_association-root-req_tor
      IMPORTING
        et_key_link    = DATA(lt_capa2req_link) ).

    LOOP AT lt_capa2req_link ASSIGNING FIELD-SYMBOL(<ls_capa2req_link>).
      ASSIGN <lt_tor_root_req>[ node_id = <ls_capa2req_link>-target_key ]-tor_id TO FIELD-SYMBOL(<lv_tor_req_id>).
      CHECK sy-subrc = 0.

      lv_freight_unit_line_no += 1.
      APPEND lv_freight_unit_line_no TO ct_req_doc_line_no.

      APPEND <lv_tor_req_id> TO ct_req_doc_no.
    ENDLOOP.

  ENDMETHOD.

  METHOD get_customizing_aot.
    SELECT SINGLE aotype
      FROM /scmtms/c_torty
      INTO rv_aot
      WHERE type = iv_tor_type.
  ENDMETHOD.

  METHOD check_non_idoc_status_fields.

    FIELD-SYMBOLS:
      <lt_header_new> TYPE /scmtms/t_em_bo_tor_root,
      <lt_header_old> TYPE /scmtms/t_em_bo_tor_root,
      <ls_header>     TYPE /scmtms/s_em_bo_tor_root.

    rv_result = lif_ef_constants=>cs_condition-false.

    DATA(lt_header_new) = mo_ef_parameters->get_appl_table(
                            iv_tabledef = lif_sst_constants=>cs_tabledef-fo_header_new ).
    DATA(lt_header_old) = mo_ef_parameters->get_appl_table(
                            iv_tabledef = lif_sst_constants=>cs_tabledef-fo_header_old ).
    ASSIGN lt_header_new->* TO <lt_header_new>.
    ASSIGN lt_header_old->* TO <lt_header_old>.

    ASSIGN is_app_object-maintabref->* TO <ls_header>.
    ASSIGN <lt_header_new>[ node_id = <ls_header>-node_id ] TO FIELD-SYMBOL(<ls_header_new>).
    ASSIGN <lt_header_old>[ node_id = <ls_header>-node_id ] TO FIELD-SYMBOL(<ls_header_old>).

    IF <ls_header> IS ASSIGNED AND <ls_header_new> IS ASSIGNED AND <ls_header_old> IS ASSIGNED.
      DATA(lv_execution_status_changed) = xsdbool(
        ( <ls_header_new>-execution = /scmtms/if_tor_status_c=>sc_root-execution-v_in_execution        OR
          <ls_header_new>-execution = /scmtms/if_tor_status_c=>sc_root-execution-v_ready_for_execution OR
          <ls_header_new>-execution = /scmtms/if_tor_status_c=>sc_root-execution-v_executed ) AND
        ( <ls_header_old>-execution <> /scmtms/if_tor_status_c=>sc_root-execution-v_in_execution        AND
          <ls_header_old>-execution <> /scmtms/if_tor_status_c=>sc_root-execution-v_ready_for_execution AND
          <ls_header_old>-execution <> /scmtms/if_tor_status_c=>sc_root-execution-v_executed ) ).

      DATA(lv_lifecycle_status_changed) = xsdbool(
        ( <ls_header_new>-lifecycle = /scmtms/if_tor_status_c=>sc_root-lifecycle-v_in_process OR
          <ls_header_new>-lifecycle = /scmtms/if_tor_status_c=>sc_root-lifecycle-v_completed ) AND
        ( <ls_header_old>-lifecycle <> /scmtms/if_tor_status_c=>sc_root-lifecycle-v_in_process AND
          <ls_header_old>-lifecycle <> /scmtms/if_tor_status_c=>sc_root-lifecycle-v_completed ) ).

      IF lv_execution_status_changed = abap_true OR lv_lifecycle_status_changed = abap_true.
        rv_result = lif_ef_constants=>cs_condition-true.
        RETURN.
      ENDIF.
    ENDIF.

  ENDMETHOD.


  METHOD check_non_idoc_stop_fields.

    FIELD-SYMBOLS:
      <lt_stop_new> TYPE /scmtms/t_em_bo_tor_stop,
      <lt_stop_old> TYPE /scmtms/t_em_bo_tor_stop,
      <ls_header>   TYPE /scmtms/s_em_bo_tor_root.

    rv_result = lif_ef_constants=>cs_condition-false.

    DATA(lt_stop_new) = mo_ef_parameters->get_appl_table(
                            iv_tabledef = lif_sst_constants=>cs_tabledef-fo_stop_new ).
    DATA(lt_stop_old) = mo_ef_parameters->get_appl_table(
                            iv_tabledef = lif_sst_constants=>cs_tabledef-fo_stop_old ).
    ASSIGN lt_stop_new->* TO <lt_stop_new>.
    ASSIGN lt_stop_old->* TO <lt_stop_old>.
    ASSIGN is_app_object-maintabref->* TO <ls_header>.
    IF sy-subrc <> 0.
      RETURN.
    ENDIF.
    LOOP AT <lt_stop_new> ASSIGNING FIELD-SYMBOL(<ls_stop_new>)
      USING KEY parent_seqnum WHERE parent_node_id = <ls_header>-node_id.
      ASSIGN <lt_stop_old>[ node_id = <ls_stop_new>-node_id ] TO FIELD-SYMBOL(<ls_stop_old>).
      CHECK sy-subrc = 0.
      IF <ls_stop_new>-aggr_assgn_start_l <> <ls_stop_old>-aggr_assgn_start_l OR
         <ls_stop_new>-aggr_assgn_end_l   <> <ls_stop_old>-aggr_assgn_end_l   OR
         <ls_stop_new>-aggr_assgn_start_c <> <ls_stop_old>-aggr_assgn_start_c OR
         <ls_stop_new>-aggr_assgn_end_c   <> <ls_stop_old>-aggr_assgn_end_c   OR
         <ls_stop_new>-plan_trans_time    <> <ls_stop_old>-plan_trans_time.
        rv_result = lif_ef_constants=>cs_condition-true.
        EXIT.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.

  METHOD get_data_from_stop.
    FIELD-SYMBOLS <ls_tor_root> TYPE /scmtms/s_em_bo_tor_root.

    ASSIGN ir_data->* TO <ls_tor_root>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    /scmtms/cl_tor_helper_stop=>get_stop_sequence(
      EXPORTING
        it_root_key     = VALUE #( ( key = <ls_tor_root>-node_id ) )
        iv_before_image = SWITCH #( iv_old_data WHEN abap_true THEN abap_true ELSE abap_false )
      IMPORTING
        et_stop_seq_d   = DATA(lt_stop_seq) ).

    get_stop_seq(
      EXPORTING
        ir_data       = ir_data
        iv_old_data   = iv_old_data
        it_stop_seq   = lt_stop_seq
      CHANGING
        ct_stop_id    = ct_stop_id
        ct_ordinal_no = ct_ordinal_no
        ct_loc_type   = ct_loc_type
        ct_loc_id     = ct_loc_id ).

    get_header_data_from_stop(
      EXPORTING
        ir_data             = ir_data
        iv_old_data         = iv_old_data
        it_stop_seq         = lt_stop_seq
      CHANGING
        cv_pln_dep_loc_id   = cv_pln_dep_loc_id
        cv_pln_dep_loc_type = cv_pln_dep_loc_type
        cv_pln_dep_timest   = cv_pln_dep_timest
        cv_pln_dep_timezone = cv_pln_dep_timezone
        cv_pln_arr_loc_id   = cv_pln_arr_loc_id
        cv_pln_arr_loc_type = cv_pln_arr_loc_type
        cv_pln_arr_timest   = cv_pln_arr_timest
        cv_pln_arr_timezone = cv_pln_arr_timezone ).

  ENDMETHOD.

  METHOD get_stop_seq.
    DATA lv_stop_num(4) TYPE n.
    FIELD-SYMBOLS <ls_tor_root> TYPE /scmtms/s_em_bo_tor_root.

    ASSIGN ir_data->* TO <ls_tor_root>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    DATA(lv_tor_id) = <ls_tor_root>-tor_id.
    SHIFT lv_tor_id LEFT DELETING LEADING '0'.

    ASSIGN it_stop_seq[ root_key = <ls_tor_root>-node_id ]-stop_seq TO FIELD-SYMBOL(<lt_stop_seq>).
    IF sy-subrc = 0.
      LOOP AT <lt_stop_seq> ASSIGNING FIELD-SYMBOL(<ls_stop_seq>).
        CHECK lcl_tools=>is_odd( <ls_stop_seq>-seq_num ).
        lv_stop_num += 1.
        CHECK <ls_stop_seq>-log_locid IS NOT INITIAL.
        APPEND |{ lv_tor_id }{ lv_stop_num }|               TO ct_stop_id.
        APPEND lv_stop_num                                  TO ct_ordinal_no.
        APPEND lif_sst_constants=>cs_location_type-logistic TO ct_loc_type.
        APPEND <ls_stop_seq>-log_locid                      TO ct_loc_id.
      ENDLOOP.
    ENDIF.

    lv_stop_num += 1.
    DATA(lv_stop_count) = lines( <lt_stop_seq> ).

    ASSIGN <lt_stop_seq>[ lv_stop_count ] TO <ls_stop_seq>.
    IF sy-subrc = 0 AND <ls_stop_seq>-log_locid IS NOT INITIAL.
      APPEND |{ lv_tor_id }{ lv_stop_num }|               TO ct_stop_id.
      APPEND lv_stop_num                                  TO ct_ordinal_no.
      APPEND lif_sst_constants=>cs_location_type-logistic TO ct_loc_type.
      APPEND <ls_stop_seq>-log_locid                      TO ct_loc_id.
    ENDIF.

    IF ct_ordinal_no IS INITIAL.
      APPEND '' TO ct_ordinal_no.
    ENDIF.

  ENDMETHOD.

  METHOD get_header_data_from_stop.

    FIELD-SYMBOLS:
      <lt_tor_stop> TYPE /scmtms/t_em_bo_tor_stop,
      <ls_tor_root> TYPE /scmtms/s_em_bo_tor_root.

    ASSIGN ir_data->* TO <ls_tor_root>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    ASSIGN it_stop_seq[ 1 ] TO FIELD-SYMBOL(<ls_stop_seq>).
    IF sy-subrc = 0.
      ASSIGN <ls_stop_seq>-stop_seq[ 1 ] TO FIELD-SYMBOL(<ls_stop_first>).
      IF sy-subrc = 0.
        IF <ls_stop_first>-log_locid IS NOT INITIAL.
          cv_pln_dep_loc_id   = <ls_stop_first>-log_locid.
          cv_pln_dep_loc_type = lif_sst_constants=>cs_location_type-logistic.
        ENDIF.
        cv_pln_dep_timest   = COND #( WHEN <ls_stop_first>-plan_trans_time IS NOT INITIAL
                                        THEN |0{ <ls_stop_first>-plan_trans_time }| ELSE '' ).
        cv_pln_dep_timezone = /scmtms/cl_common_helper=>loc_key_get_timezone( iv_loc_key = <ls_stop_first>-log_loc_uuid ).
      ENDIF.
      ASSIGN <ls_stop_seq>-stop_seq[ lines( <ls_stop_seq>-stop_seq ) ] TO FIELD-SYMBOL(<ls_stop_last>).
      IF sy-subrc = 0.
        IF <ls_stop_last>-log_locid IS NOT INITIAL.
          cv_pln_arr_loc_id   = <ls_stop_last>-log_locid.
          cv_pln_arr_loc_type = lif_sst_constants=>cs_location_type-logistic.
        ENDIF.
        cv_pln_arr_timest   = COND #( WHEN <ls_stop_last>-plan_trans_time IS NOT INITIAL
                                        THEN |0{ <ls_stop_last>-plan_trans_time }| ELSE '' ).
        cv_pln_arr_timezone = /scmtms/cl_common_helper=>loc_key_get_timezone( iv_loc_key = <ls_stop_last>-log_loc_uuid ).
      ENDIF.
    ENDIF.

  ENDMETHOD.

  METHOD check_non_idoc_fields.

    rv_result = check_non_idoc_status_fields( is_app_object ).
    IF rv_result = lif_ef_constants=>cs_condition-true.
      RETURN.
    ENDIF.

    rv_result = check_non_idoc_stop_fields( is_app_object = is_app_object ).

  ENDMETHOD.

  METHOD lif_bo_reader~get_mapping_structure.
    rr_data   = REF #( cs_mapping ).
  ENDMETHOD.

  METHOD lif_bo_reader~get_track_id_data.
  ENDMETHOD.

  METHOD lif_bo_reader~get_data.
  ENDMETHOD.

  METHOD get_docref_data.
    DATA lt_docs TYPE /scmtms/t_tor_docref_k.
    FIELD-SYMBOLS <ls_root> TYPE /scmtms/s_em_bo_tor_root.

    ASSIGN ir_root->* TO <ls_root>.
    IF sy-subrc = 0.
      /bobf/cl_tra_serv_mgr_factory=>get_service_manager(
        /scmtms/if_tor_c=>sc_bo_key )->retrieve_by_association(
        EXPORTING
          iv_node_key    = /scmtms/if_tor_c=>sc_node-root
          it_key         = VALUE #( ( key = <ls_root>-node_id ) )
          iv_association = /scmtms/if_tor_c=>sc_association-root-docreference
          iv_fill_data   = abap_true
          iv_before_image = SWITCH #( iv_old_data WHEN abap_true THEN abap_true
                                                  ELSE abap_false )
        IMPORTING
          et_data        = lt_docs ).

      LOOP AT lt_docs ASSIGNING FIELD-SYMBOL(<fs_docs>).
        SHIFT  <fs_docs>-btd_id LEFT DELETING LEADING '0'.
        APPEND <fs_docs>-btd_id  TO ct_ref_doc_id.
        APPEND <fs_docs>-btd_tco TO ct_ref_doc_type.
      ENDLOOP.
    ELSE.
      MESSAGE e002(zsst_gtt) WITH /scmtms/if_tor_c=>sc_node-root INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.
  ENDMETHOD.

  METHOD lif_bo_reader~check_relevance.
    " FO relevance function
    FIELD-SYMBOLS <ls_root> TYPE /scmtms/s_em_bo_tor_root.

    rv_result = lif_ef_constants=>cs_condition-false.

    ASSIGN is_app_object-maintabref->* TO <ls_root>.
    IF sy-subrc <> 0.
      RETURN.
    ENDIF.

    IF get_customizing_aot( <ls_root>-tor_type ) <> is_app_object-appobjtype.
      RETURN.
    ENDIF.

    IF is_app_object-maintabdef = lif_sst_constants=>cs_tabledef-fo_header_new AND
      ( <ls_root>-track_exec_rel = lif_sst_constants=>cs_track_exec_rel-execution OR
        <ls_root>-track_exec_rel = lif_sst_constants=>cs_track_exec_rel-exec_with_extern_event_mngr ) AND
      <ls_root>-lifecycle = lif_sst_constants=>cs_lifecycle_status-in_process AND
      ( <ls_root>-execution = lif_sst_constants=>cs_execution_status-in_execution OR
        <ls_root>-execution = lif_sst_constants=>cs_execution_status-ready_for_transp_exec ) AND
     <ls_root>-tspid IS NOT INITIAL AND
      ( <ls_root>-tor_cat = /scmtms/if_tor_const=>sc_tor_category-active OR
        <ls_root>-tor_cat = /scmtms/if_tor_const=>sc_tor_category-booking ).

      CASE is_app_object-update_indicator.
        WHEN lif_ef_constants=>cs_change_mode-insert.
          rv_result = lif_ef_constants=>cs_condition-true.
        WHEN lif_ef_constants=>cs_change_mode-update OR
             lif_ef_constants=>cs_change_mode-undefined.
          rv_result = lcl_tools=>are_structures_different(
                          ir_data1  = lif_bo_reader~get_data( is_app_object = is_app_object )
                          ir_data2  = lif_bo_reader~get_data(
                                          is_app_object = is_app_object
                                          iv_old_data   = abap_true ) ).
          IF rv_result = lif_ef_constants=>cs_condition-false.
            rv_result = check_non_idoc_fields( is_app_object ).
          ENDIF.
      ENDCASE.
    ENDIF.
  ENDMETHOD.

  METHOD get_data_from_text_collection.
    FIELD-SYMBOLS <ls_root> TYPE /scmtms/s_em_bo_tor_root.
    ASSIGN ir_data->* TO <ls_root>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    DATA(lv_before_image) = SWITCH abap_bool( iv_old_data WHEN abap_true THEN abap_true
                                                          ELSE abap_false ).

    DATA(lr_srvmgr_tor) = /bobf/cl_tra_serv_mgr_factory=>get_service_manager( iv_bo_key = /scmtms/if_tor_c=>sc_bo_key ).
    TRY.
        DATA(lr_bo_conf) = /bobf/cl_frw_factory=>get_configuration( iv_bo_key = /scmtms/if_tor_c=>sc_bo_key ).
      CATCH /bobf/cx_frw.
        MESSAGE e011(zsst_gtt) INTO  lv_dummy.
        lcl_tools=>throw_exception( ).
    ENDTRY.
    DATA(lv_txt_key) = lr_bo_conf->get_content_key_mapping(
                           iv_content_cat      = /bobf/if_conf_c=>sc_content_nod
                           iv_do_content_key   = /bobf/if_txc_c=>sc_node-text
                           iv_do_root_node_key = /scmtms/if_tor_c=>sc_node-textcollection ).

    DATA(lv_txt_assoc) = lr_bo_conf->get_content_key_mapping(
                             iv_content_cat      = /bobf/if_conf_c=>sc_content_ass
                             iv_do_content_key   = /bobf/if_txc_c=>sc_association-root-text
                             iv_do_root_node_key = /scmtms/if_tor_c=>sc_node-textcollection ).

    DATA(lv_cont_assoc) = lr_bo_conf->get_content_key_mapping(
                              iv_content_cat      = /bobf/if_conf_c=>sc_content_ass
                              iv_do_content_key   = /bobf/if_txc_c=>sc_association-text-text_content
                              iv_do_root_node_key = /scmtms/if_tor_c=>sc_node-textcollection ).

    lr_srvmgr_tor->retrieve_by_association(
      EXPORTING
        it_key          = VALUE #( ( key = <ls_root>-node_id ) )
        iv_node_key     = /scmtms/if_tor_c=>sc_node-root
        iv_association  = /scmtms/if_tor_c=>sc_association-root-textcollection
        iv_before_image = lv_before_image
      IMPORTING
        et_target_key   = DATA(lt_textcollection_key) ).

    CREATE DATA er_text.
    CREATE DATA er_text_content.

    IF lt_textcollection_key IS NOT INITIAL.

      lr_srvmgr_tor->retrieve_by_association(
        EXPORTING
          it_key          = lt_textcollection_key
          iv_node_key     = /scmtms/if_tor_c=>sc_node-textcollection
          iv_association  = lv_txt_assoc
          iv_fill_data    = abap_true
          iv_before_image = lv_before_image
        IMPORTING
          et_data         = er_text->* ).

      IF er_text->* IS NOT INITIAL.

        lr_srvmgr_tor->retrieve_by_association(
          EXPORTING
            it_key          = CORRESPONDING #( er_text->* )
            iv_node_key     = lv_txt_key
            iv_association  = lv_cont_assoc
            iv_fill_data    = abap_true
            iv_before_image = lv_before_image
          IMPORTING
            et_data         = er_text_content->* ).
      ENDIF.
    ENDIF.
  ENDMETHOD.

  METHOD get_container_and_mobile_track.

    get_data_from_text_collection(
      EXPORTING
        iv_old_data     = iv_old_data
        ir_data         = ir_data
      IMPORTING
        er_text         = DATA(lr_text)
        er_text_content = DATA(lr_text_content) ).

    IF lr_text->* IS NOT INITIAL AND lr_text_content->* IS NOT INITIAL.
      LOOP AT lr_text->* ASSIGNING FIELD-SYMBOL(<fs_text>).
        READ TABLE lr_text_content->* WITH KEY parent_key
          COMPONENTS parent_key = <fs_text>-key ASSIGNING FIELD-SYMBOL(<fs_text_content>).
        IF sy-subrc = 0.
          IF <fs_text>-text_type = cs_text_type-cont AND <fs_text_content>-text IS NOT INITIAL.
            APPEND cs_track_id-container_id TO ct_tracked_object_id.
            APPEND <fs_text_content>-text   TO ct_tracked_object_type.
          ELSEIF <fs_text>-text_type = cs_text_type-mobl AND <fs_text_content>-text IS NOT INITIAL.
            APPEND cs_track_id-mobile_number TO ct_tracked_object_id.
            APPEND <fs_text_content>-text    TO ct_tracked_object_type.
          ENDIF.
        ENDIF.
      ENDLOOP.
    ENDIF.

  ENDMETHOD.

  METHOD add_track_id_data.
    APPEND VALUE #( appsys     = mo_ef_parameters->get_appsys( )
                    appobjtype = is_app_object-appobjtype
                    appobjid   = is_app_object-appobjid
                    trxcod     = iv_trxcod
                    trxid      = iv_trxid
                    start_date = lcl_tools=>get_system_date_time( )
                    end_date   = lif_ef_constants=>cv_max_end_date
                    timzon     = lcl_tools=>get_system_time_zone( )
                    msrid      = space
                    action     = iv_action ) TO ct_track_id.
  ENDMETHOD.

  METHOD get_container_mobile_track_id.

    FIELD-SYMBOLS <ls_root> TYPE /scmtms/s_em_bo_tor_root.
    ASSIGN is_app_object-maintabref->* TO <ls_root>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    get_data_from_text_collection(
      EXPORTING
        ir_data         = is_app_object-maintabref
        iv_old_data     = iv_old_data
      IMPORTING
        er_text         = DATA(lr_text)
        er_text_content = DATA(lr_text_content) ).

    IF lr_text->* IS NOT INITIAL AND lr_text_content->* IS NOT INITIAL.
      LOOP AT lr_text->* ASSIGNING FIELD-SYMBOL(<fs_text>).
        READ TABLE lr_text_content->* WITH KEY parent_key
          COMPONENTS parent_key = <fs_text>-key ASSIGNING FIELD-SYMBOL(<fs_text_content>).
        CHECK sy-subrc = 0.

        IF ( <fs_text>-text_type = cs_text_type-cont OR <fs_text>-text_type = cs_text_type-mobl ) AND
             <fs_text_content>-text IS NOT INITIAL.
          APPEND VALUE #( key = <fs_text_content>-key
                   appsys      = mo_ef_parameters->get_appsys( )
                   appobjtype  = is_app_object-appobjtype
                   appobjid    = is_app_object-appobjid
                   trxcod      = lif_sst_constants=>cs_trxcod-fo_resource
                   trxid       = |{ <ls_root>-tor_id }{ <fs_text_content>-text }|
                   start_date  = lcl_tools=>get_system_date_time( )
                   end_date    = lif_ef_constants=>cv_max_end_date
                   timzon      = lcl_tools=>get_system_time_zone( )
                   msrid       = space  ) TO ct_track_id_data.
        ENDIF.
      ENDLOOP.
    ENDIF.
  ENDMETHOD.

ENDCLASS.

CLASS lcl_bo_freight_order_reader DEFINITION INHERITING FROM lcl_bo_tor_reader.

  PUBLIC SECTION.
    METHODS lif_bo_reader~get_data REDEFINITION.
    METHODS lif_bo_reader~get_track_id_data REDEFINITION.

  PRIVATE SECTION.

    TYPES: BEGIN OF ts_fo_header,
             tor_id              TYPE /scmtms/s_em_bo_tor_root-tor_id,
             mtr                 TYPE /scmtms/s_em_bo_tor_root-mtr,  "/SAPAPO/TR_MOTSCODE,
             gro_vol_val         TYPE /scmtms/s_em_bo_tor_root-gro_vol_val,
             gro_vol_uni         TYPE /scmtms/s_em_bo_tor_root-gro_vol_uni,
             gro_wei_val         TYPE /scmtms/s_em_bo_tor_root-gro_wei_val,
             gro_wei_uni         TYPE /scmtms/s_em_bo_tor_root-gro_wei_uni,
             qua_pcs_val         TYPE /scmtms/s_em_bo_tor_root-qua_pcs_val,
             qua_pcs_uni         TYPE /scmtms/s_em_bo_tor_root-qua_pcs_uni,
             total_distance_km   TYPE /scmtms/s_em_bo_tor_root-total_distance_km,
             dgo_indicator       TYPE /scmtms/s_em_bo_tor_root-dgo_indicator,
             total_duration_net  TYPE /scmtms/s_em_bo_tor_root-total_duration_net,
             pln_grs_duration    TYPE /scmtms/total_duration,
             shipping_type       TYPE /scmtms/s_em_bo_tor_root-shipping_type,
             traffic_direct      TYPE /scmtms/s_em_bo_tor_root-traffic_direct,
             trmodcod            TYPE /scmtms/s_em_bo_tor_root-trmodcod,
             tspid               TYPE bu_id_number,
             tracked_object_type TYPE tt_tracked_object_type,
             tracked_object_id   TYPE tt_tracked_object_id,
             ref_doc_id          TYPE tt_ref_doc_id,
             ref_doc_type        TYPE tt_ref_doc_type,
             inc_class_code      TYPE /scmtms/s_em_bo_tor_item-inc_class_code,
             inc_transf_loc_n    TYPE /scmtms/s_em_bo_tor_item-inc_transf_loc_n,
             country             TYPE /scmtms/s_em_bo_tor_item-country,
             platenumber         TYPE /scmtms/s_em_bo_tor_item-platenumber,
             res_id              TYPE /scmtms/s_em_bo_tor_item-res_id,
             pln_dep_loc_id      TYPE /scmtms/location_id,
             pln_dep_loc_type    TYPE /saptrx/loc_id_type,
             pln_dep_timest      TYPE char16,
             pln_dep_timezone    TYPE ad_tzone,
             pln_arr_loc_id      TYPE /scmtms/location_id,
             pln_arr_loc_type    TYPE /saptrx/loc_id_type,
             pln_arr_timest      TYPE char16,
             pln_arr_timezone    TYPE ad_tzone,
             stop_id             TYPE tt_stop_id,
             ordinal_no          TYPE tt_ordinal_no,
             loc_type            TYPE tt_loc_type,
             loc_id              TYPE tt_loc_id,
             req_doc_line_no     TYPE tt_req_doc_line_number,
             req_doc_no          TYPE tt_req_doc_number,
           END OF ts_fo_header.

    METHODS get_data_from_root
      IMPORTING
        iv_old_data  TYPE abap_bool DEFAULT abap_false
        ir_root      TYPE REF TO data
      CHANGING
        cs_fo_header TYPE ts_fo_header
      RAISING
        cx_udm_message.

    METHODS get_data_from_item
      IMPORTING
        iv_old_data  TYPE abap_bool DEFAULT abap_false
        ir_item      TYPE REF TO data
      CHANGING
        cs_fo_header TYPE ts_fo_header
      RAISING
        cx_udm_message.

    METHODS get_data_from_textcoll
      IMPORTING
        iv_old_data  TYPE abap_bool DEFAULT abap_false
        ir_root      TYPE REF TO data
      CHANGING
        cs_fo_header TYPE ts_fo_header
      RAISING
        cx_udm_message.

    METHODS get_maintabref
      IMPORTING
        is_app_object        TYPE trxas_appobj_ctab_wa
      RETURNING
        VALUE(rr_maintabref) TYPE REF TO data.

    METHODS get_data_from_stops
      IMPORTING
        iv_old_data  TYPE abap_bool DEFAULT abap_false
        iv_tor_id    TYPE /scmtms/tor_id
        ir_root      TYPE REF TO data
        ir_stop      TYPE REF TO data
        ir_stop_addr TYPE REF TO data
      CHANGING
        cs_fo_header TYPE ts_fo_header
      RAISING
        cx_udm_message.
ENDCLASS.

CLASS lcl_bo_freight_order_reader IMPLEMENTATION.

  METHOD lif_bo_reader~get_data.

    DATA: lr_fo TYPE REF TO data.
    FIELD-SYMBOLS: <ls_freight_order> TYPE ts_fo_header,
                   <ls_fo>            TYPE any,
                   <ls_maintabref>    TYPE any,
                   <lt_maintabref>    TYPE ANY TABLE.

    DATA(lr_maintabref) = get_maintabref( is_app_object ).

    rr_data   = NEW ts_fo_header( ).
    ASSIGN rr_data->* TO <ls_freight_order>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    get_data_from_root(
      EXPORTING
        iv_old_data   = iv_old_data
        ir_root       = lr_maintabref
      CHANGING
        cs_fo_header  = <ls_freight_order> ).
    IF <ls_freight_order> IS INITIAL.
      RETURN.
    ENDIF.

    get_data_from_item(
      EXPORTING
        iv_old_data   = iv_old_data
        ir_item       = mo_ef_parameters->get_appl_table(
                            SWITCH #( iv_old_data WHEN abap_true THEN lif_sst_constants=>cs_tabledef-fo_item_old
                                                  ELSE lif_sst_constants=>cs_tabledef-fo_item_new ) )
      CHANGING
        cs_fo_header  = <ls_freight_order> ).

    get_data_from_textcoll(
      EXPORTING
        iv_old_data   = iv_old_data
        ir_root       = lr_maintabref
      CHANGING
        cs_fo_header  = <ls_freight_order> ).
    IF <ls_freight_order>-tracked_object_id IS INITIAL.
      APPEND '' TO <ls_freight_order>-tracked_object_id.
    ENDIF.

    get_docref_data(
      EXPORTING
        iv_old_data     = iv_old_data
        ir_root         = lr_maintabref
      CHANGING
        ct_ref_doc_id   = <ls_freight_order>-ref_doc_id
        ct_ref_doc_type = <ls_freight_order>-ref_doc_type ).
    IF <ls_freight_order>-ref_doc_id IS INITIAL.
      APPEND '' TO <ls_freight_order>-ref_doc_id.
    ENDIF.

    get_data_from_stop(
      EXPORTING
        ir_data             = lr_maintabref
        iv_old_data         = iv_old_data
      CHANGING
        cv_pln_dep_loc_id   = <ls_freight_order>-pln_dep_loc_id
        cv_pln_dep_loc_type = <ls_freight_order>-pln_dep_loc_type
        cv_pln_dep_timest   = <ls_freight_order>-pln_dep_timest
        cv_pln_dep_timezone = <ls_freight_order>-pln_dep_timezone
        cv_pln_arr_loc_id   = <ls_freight_order>-pln_arr_loc_id
        cv_pln_arr_loc_type = <ls_freight_order>-pln_arr_loc_type
        cv_pln_arr_timest   = <ls_freight_order>-pln_arr_timest
        cv_pln_arr_timezone = <ls_freight_order>-pln_arr_timezone
        ct_stop_id          = <ls_freight_order>-stop_id
        ct_ordinal_no       = <ls_freight_order>-ordinal_no
        ct_loc_type         = <ls_freight_order>-loc_type
        ct_loc_id           = <ls_freight_order>-loc_id ).

    get_requirement_doc_list(
      EXPORTING
        ir_data            = lr_maintabref
        iv_old_data        = iv_old_data
      CHANGING
        ct_req_doc_line_no = <ls_freight_order>-req_doc_line_no
        ct_req_doc_no      = <ls_freight_order>-req_doc_no ).
    IF <ls_freight_order>-req_doc_no IS INITIAL.
      APPEND '' TO <ls_freight_order>-req_doc_line_no.
    ENDIF.

  ENDMETHOD.


  METHOD lif_bo_reader~get_track_id_data.
    "FO
    CONSTANTS: cs_mtr_truck TYPE string VALUE '31'.

    DATA:
      lr_item_new          TYPE REF TO data,
      lr_item_old          TYPE REF TO data,
      lr_root_new          TYPE REF TO data,
      lr_root_old          TYPE REF TO data,
      lt_track_id_data_new TYPE lif_ef_types=>tt_enh_track_id_data,
      lt_track_id_data_old TYPE lif_ef_types=>tt_enh_track_id_data.

    FIELD-SYMBOLS:
      <lt_item_new> TYPE /scmtms/t_em_bo_tor_item,
      <lt_item_old> TYPE /scmtms/t_em_bo_tor_item,
      <ls_root_new> TYPE /scmtms/s_em_bo_tor_root,
      <lt_root_new> TYPE /scmtms/t_em_bo_tor_root,
      <lt_root_old> TYPE /scmtms/t_em_bo_tor_root.

    ASSIGN is_app_object-maintabref->* TO <ls_root_new>.

    lr_root_old = mo_ef_parameters->get_appl_table( iv_tabledef = lif_sst_constants=>cs_tabledef-fo_header_old ).
    ASSIGN lr_root_old->* TO <lt_root_old>.
    IF <ls_root_new> IS NOT ASSIGNED OR <lt_root_old> IS NOT ASSIGNED.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    add_track_id_data(
      EXPORTING
        is_app_object = is_app_object
        iv_trxcod     = lif_sst_constants=>cs_trxcod-fo_number
        iv_trxid      = |{ <ls_root_new>-tor_id }|
      CHANGING
        ct_track_id   = et_track_id_data ).

    get_container_mobile_track_id(
      EXPORTING
        is_app_object    = is_app_object
      CHANGING
        ct_track_id_data = lt_track_id_data_new ).

    get_container_mobile_track_id(
      EXPORTING
        is_app_object    = is_app_object
        iv_old_data      = abap_true
      CHANGING
        ct_track_id_data = lt_track_id_data_old ).

    lr_item_new = mo_ef_parameters->get_appl_table( iv_tabledef = lif_sst_constants=>cs_tabledef-fo_item_new ).
    lr_item_old = mo_ef_parameters->get_appl_table( iv_tabledef = lif_sst_constants=>cs_tabledef-fo_item_old ).

    ASSIGN <lt_root_old>[ node_id = <ls_root_new>-node_id ] TO FIELD-SYMBOL(<ls_root_old>).
    IF sy-subrc = 0.
      DATA(lv_deleted) = lcl_tools=>check_is_fo_deleted(
                          is_root_new = <ls_root_new>
                          is_root_old = <ls_root_old> ).
      IF lv_deleted = lif_ef_constants=>cs_condition-true.
        CLEAR: lt_track_id_data_old, lr_item_old.
      ENDIF.
    ENDIF.

    ASSIGN lr_item_new->* TO <lt_item_new>.
    IF sy-subrc = 0.
      lcl_tools=>get_fo_tracked_item_obj(
          EXPORTING
            is_app_object    = is_app_object
            is_root          = <ls_root_new>
            it_item          = <lt_item_new>
            iv_appsys        = mo_ef_parameters->get_appsys( )
            iv_old_data      = abap_false
         CHANGING
            ct_track_id_data = lt_track_id_data_new ).
    ELSE.
      MESSAGE e010(zsst_gtt) INTO lv_dummy.
      lcl_tools=>throw_exception( ).
    ENDIF.

    ASSIGN lr_item_old->* TO <lt_item_old>.
    IF sy-subrc = 0 AND lv_deleted = lif_ef_constants=>cs_condition-false.
      lcl_tools=>get_fo_tracked_item_obj(
        EXPORTING
          is_app_object = is_app_object
          is_root       = <ls_root_old>
          it_item       = <lt_item_old>
          iv_appsys     = mo_ef_parameters->get_appsys( )
          iv_old_data   = abap_true
       CHANGING
          ct_track_id_data = lt_track_id_data_old ).
    ENDIF.

    lcl_tools=>get_track_obj_changes(
       EXPORTING
         is_app_object        = is_app_object
         iv_appsys            = mo_ef_parameters->get_appsys( )
         it_track_id_data_new = lt_track_id_data_new
         it_track_id_data_old = lt_track_id_data_old
       CHANGING
         ct_track_id_data     = et_track_id_data ).

  ENDMETHOD.

  METHOD get_data_from_root.

    FIELD-SYMBOLS:
      <ls_root>     TYPE /scmtms/s_em_bo_tor_root,
      <lt_root_old> TYPE /scmtms/t_em_bo_tor_root.

    ASSIGN ir_root->* TO <ls_root>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    IF iv_old_data = abap_true.
      DATA(lr_root_old) = mo_ef_parameters->get_appl_table( lif_sst_constants=>cs_tabledef-fo_header_old ).
      ASSIGN lr_root_old->* TO <lt_root_old>.
      IF sy-subrc = 0.
        ASSIGN <lt_root_old>[ tor_id = <ls_root>-tor_id ] TO <ls_root>.
        IF sy-subrc <> 0.
          " FO is just crerated
          RETURN.
        ENDIF.
      ENDIF.
      DATA(lv_before_image) = abap_true.
    ENDIF.

    MOVE-CORRESPONDING <ls_root> TO cs_fo_header.

    /scmtms/cl_tor_helper_root=>det_transient_root_fields(
      EXPORTING
        it_key               = VALUE #( ( key = <ls_root>-node_id ) )
        iv_get_stop_infos    = abap_true
        iv_get_mainitem_info = abap_true
        iv_before_image      = lv_before_image
      IMPORTING
        et_tor_add_info      = DATA(lt_tor_add_info) ).
    ASSIGN lt_tor_add_info[ 1 ] TO FIELD-SYMBOL(<ls_tor_additional_info>).
    IF sy-subrc = 0.
      cs_fo_header-pln_grs_duration = <ls_tor_additional_info>-tot_duration.
    ENDIF.

    cs_fo_header-tspid = get_carrier_name( iv_tspid = cs_fo_header-tspid ).

    SELECT SINGLE motscode
      FROM /sapapo/trtype
      INTO cs_fo_header-mtr
      WHERE ttype = cs_fo_header-mtr.

    SHIFT cs_fo_header-mtr    LEFT DELETING LEADING '0'.
    SHIFT cs_fo_header-tor_id LEFT DELETING LEADING '0'.

    CASE cs_fo_header-trmodcod.
      WHEN lif_sst_constants=>cs_trmodcod-road.
        cs_fo_header-trmodcod = lif_sst_constants=>cs_trmodcod-sea.
      WHEN lif_sst_constants=>cs_trmodcod-rail.
        cs_fo_header-trmodcod = lif_sst_constants=>cs_trmodcod-rail.
      WHEN lif_sst_constants=>cs_trmodcod-postal_service.
        cs_fo_header-trmodcod = lif_sst_constants=>cs_trmodcod-air.
      WHEN OTHERS.
        cs_fo_header-trmodcod = lif_sst_constants=>cs_trmodcod-na.
    ENDCASE.

  ENDMETHOD.

  METHOD get_data_from_item.

    FIELD-SYMBOLS <lt_item> TYPE /scmtms/t_em_bo_tor_item.

    ASSIGN ir_item->* TO <lt_item>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    ASSIGN <lt_item>[ item_cat = /scmtms/if_tor_const=>sc_tor_item_category-av_item ] TO FIELD-SYMBOL(<ls_item>).
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO lv_dummy.
      lcl_tools=>throw_exception( ).
    ENDIF.

    cs_fo_header-inc_class_code   =  <ls_item>-inc_class_code.
    cs_fo_header-inc_transf_loc_n =  <ls_item>-inc_transf_loc_n.
    cs_fo_header-country          =  <ls_item>-country.
    cs_fo_header-platenumber      =  <ls_item>-platenumber.
    cs_fo_header-res_id           =  <ls_item>-res_id.

  ENDMETHOD.

  METHOD get_data_from_textcoll.

    get_container_and_mobile_track(
      EXPORTING
        ir_data         = ir_root
        iv_old_data     = iv_old_data
      CHANGING
        ct_tracked_object_type = cs_fo_header-tracked_object_type
        ct_tracked_object_id   = cs_fo_header-tracked_object_id ).

    IF cs_fo_header-tor_id IS NOT INITIAL AND cs_fo_header-res_id IS NOT INITIAL.
      APPEND cs_track_id-truck_id TO cs_fo_header-tracked_object_id.
      APPEND cs_fo_header-res_id  TO cs_fo_header-tracked_object_type.
    ENDIF.
    IF cs_fo_header-tor_id IS NOT INITIAL AND cs_fo_header-platenumber IS NOT INITIAL AND cs_fo_header-mtr = '31'.
      APPEND cs_track_id-license_plate TO cs_fo_header-tracked_object_id.
      APPEND cs_fo_header-platenumber  TO cs_fo_header-tracked_object_type.
    ENDIF.

  ENDMETHOD.

  METHOD get_data_from_stops.

    DATA:
      lt_key               TYPE /bobf/t_frw_key,
      lr_stop_addr         TYPE REF TO /scmtms/s_em_bo_loc_addr,
      lv_last_loc_uuid     TYPE /scmtms/locuuid,
      lv_difference        TYPE i,
      lv_ord_no_counter(4) TYPE n.

    FIELD-SYMBOLS:
      <lt_stop>      TYPE /scmtms/t_em_bo_tor_stop,
      <lt_stop_addr> TYPE /scmtms/t_em_bo_loc_addr,
      <ls_tor_root>  TYPE /scmtms/s_em_bo_tor_root..

    ASSIGN ir_stop->*      TO <lt_stop>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    ASSIGN ir_stop_addr->* TO <lt_stop_addr>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO lv_dummy.
      lcl_tools=>throw_exception( ).
    ENDIF.

    ASSIGN ir_root->* TO <ls_tor_root>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO lv_dummy.
      lcl_tools=>throw_exception( ).
    ENDIF.

    DATA(lv_tor_id) = iv_tor_id.
    SHIFT lv_tor_id LEFT DELETING LEADING '0'.

    /scmtms/cl_tor_helper_stop=>get_stop_sequence(
      EXPORTING
        it_root_key     = VALUE #( ( key = <ls_tor_root>-node_id ) )
        iv_before_image = SWITCH #( iv_old_data WHEN abap_true THEN abap_true ELSE abap_false )
      IMPORTING
        et_stop_seq_d   = DATA(lt_stop) ).

    DATA(lv_stops) = lines( <lt_stop> ).

    LOOP AT <lt_stop> USING KEY parent_seqnum ASSIGNING FIELD-SYMBOL(<ls_stop>).
      " Source Location ID
      CASE sy-tabix.
        WHEN 1.
          ADD 1 TO lv_ord_no_counter.

          APPEND |{ lv_tor_id }{ lv_ord_no_counter }|         TO cs_fo_header-stop_id.
          APPEND lv_ord_no_counter                            TO cs_fo_header-ordinal_no.
          APPEND lif_sst_constants=>cs_location_type-logistic TO cs_fo_header-loc_type.
          APPEND <ls_stop>-log_locid                          TO cs_fo_header-loc_id.

          cs_fo_header-pln_dep_loc_id = <ls_stop>-log_locid.
          cs_fo_header-pln_dep_loc_type = lif_sst_constants=>cs_location_type-logistic.

          READ TABLE <lt_stop_addr> REFERENCE INTO lr_stop_addr
                                     WITH KEY parent_node_id = <ls_stop>-log_loc_uuid BINARY SEARCH.
          IF sy-subrc IS INITIAL.
            IF lr_stop_addr->time_zone_code IS NOT INITIAL.
              cs_fo_header-pln_dep_timest   =  COND #( WHEN <ls_stop>-plan_trans_time IS NOT INITIAL
                                                      THEN |0{ <ls_stop>-plan_trans_time }|
                                                      ELSE '' ).
              cs_fo_header-pln_dep_timezone = lr_stop_addr->time_zone_code.
            ELSE.
              cs_fo_header-pln_dep_timest   =  COND #( WHEN <ls_stop>-plan_trans_time IS NOT INITIAL
                                                      THEN |0{ <ls_stop>-plan_trans_time }|
                                                      ELSE '' ).
              cs_fo_header-pln_dep_timezone = sy-zonlo.
            ENDIF.
          ENDIF.

        WHEN lv_stops.

          " Destination Location
          ADD 1 TO lv_ord_no_counter.
          APPEND |{ lv_tor_id }{ lv_ord_no_counter }|         TO cs_fo_header-stop_id.
          APPEND lv_ord_no_counter                            TO cs_fo_header-ordinal_no.
          APPEND lif_sst_constants=>cs_location_type-logistic TO cs_fo_header-loc_type.
          APPEND <ls_stop>-log_locid                          TO cs_fo_header-loc_id.

          cs_fo_header-pln_arr_loc_id  = <ls_stop>-log_locid.
          cs_fo_header-pln_arr_loc_type = lif_sst_constants=>cs_location_type-logistic.

          READ TABLE <lt_stop_addr> REFERENCE INTO lr_stop_addr
                                     WITH KEY parent_node_id = <ls_stop>-log_loc_uuid BINARY SEARCH.

          IF sy-subrc IS INITIAL.
            IF lr_stop_addr->time_zone_code IS NOT INITIAL.
              cs_fo_header-pln_arr_timest   = COND #( WHEN <ls_stop>-plan_trans_time IS NOT INITIAL
                                                      THEN |0{ <ls_stop>-plan_trans_time }|
                                                      ELSE '' ).
              cs_fo_header-pln_arr_timezone = lr_stop_addr->time_zone_code.
            ELSE.
              cs_fo_header-pln_arr_timest   = COND #( WHEN <ls_stop>-plan_trans_time IS NOT INITIAL
                                                      THEN |0{ <ls_stop>-plan_trans_time }|
                                                      ELSE '' ).
              cs_fo_header-pln_arr_timezone = sy-zonlo.
            ENDIF.
          ENDIF.

        WHEN OTHERS.
          " new intermediate location only if the loc_uuid is different form the last intermediate location
          IF lv_last_loc_uuid <> <ls_stop>-log_loc_uuid AND <ls_stop>-log_loc_uuid <> /scmtms/if_common_c=>c_empty_key.
            ADD 1 TO lv_ord_no_counter.
            APPEND |{ lv_tor_id }{ lv_ord_no_counter }|         TO cs_fo_header-stop_id.
            APPEND lv_ord_no_counter                            TO cs_fo_header-ordinal_no.
            APPEND lif_sst_constants=>cs_location_type-logistic TO cs_fo_header-loc_type.
            APPEND <ls_stop>-log_locid                          TO cs_fo_header-loc_id.
          ENDIF.
      ENDCASE.
      lv_last_loc_uuid = <ls_stop>-log_loc_uuid.
    ENDLOOP.
  ENDMETHOD.

  METHOD get_maintabref.
    FIELD-SYMBOLS <lt_maintabref> TYPE ANY TABLE.

    ASSIGN is_app_object-maintabref->* TO FIELD-SYMBOL(<ls_maintabref>).

    IF <ls_maintabref> IS ASSIGNED AND lcl_tools=>is_table( iv_value = <ls_maintabref> ) = abap_true.
      ASSIGN <ls_maintabref> TO <lt_maintabref>.
      LOOP AT <lt_maintabref> ASSIGNING FIELD-SYMBOL(<ls_line>).
        ASSIGN COMPONENT /scmtms/if_tor_c=>sc_node_attribute-root-tor_cat
          OF STRUCTURE <ls_line> TO FIELD-SYMBOL(<lv_tor_cat>).
        IF sy-subrc = 0 AND <lv_tor_cat> = /scmtms/if_tor_const=>sc_tor_category-active.
          GET REFERENCE OF <ls_line> INTO rr_maintabref.
          EXIT.
        ENDIF.
      ENDLOOP.
    ELSEIF <ls_maintabref> IS ASSIGNED.
      GET REFERENCE OF <ls_maintabref> INTO rr_maintabref.
    ENDIF.
  ENDMETHOD.

ENDCLASS.

CLASS lcl_bo_freight_booking_reader DEFINITION INHERITING FROM lcl_bo_tor_reader.

  PUBLIC SECTION.
    METHODS lif_bo_reader~get_data REDEFINITION.
    METHODS lif_bo_reader~get_track_id_data REDEFINITION.

  PROTECTED SECTION.
    METHODS get_docref_data REDEFINITION.

  PRIVATE SECTION.
    TYPES:
      BEGIN OF ts_freight_booking,
        tor_id              TYPE /scmtms/s_em_bo_tor_root-tor_id,
        mtr                 TYPE /scmtms/s_em_bo_tor_root-mtr,
        dgo_indicator       TYPE /scmtms/s_em_bo_tor_root-dgo_indicator,
        tspid               TYPE bu_id_number,
        total_distance_km   TYPE /scmtms/total_distance_km,
        total_duration_net  TYPE /scmtms/total_duration_net,
        pln_grs_duration    TYPE /scmtms/total_duration_net,
        shipping_type       TYPE /scmtms/s_em_bo_tor_root-shipping_type,
        traffic_direct      TYPE /scmtms/s_em_bo_tor_root-traffic_direct,
        tracked_object_type TYPE tt_tracked_object_type,
        tracked_object_id   TYPE tt_tracked_object_id,
        inc_class_code      TYPE /scmtms/s_em_bo_tor_item-inc_class_code,
        inc_transf_loc_n    TYPE /scmtms/s_em_bo_tor_item-inc_transf_loc_n,
        gro_vol_val         TYPE /scmtms/s_em_bo_tor_root-gro_vol_val,
        gro_vol_uni         TYPE /scmtms/s_em_bo_tor_root-gro_vol_uni,
        gro_wei_val         TYPE /scmtms/s_em_bo_tor_root-gro_wei_val,
        gro_wei_uni         TYPE /scmtms/s_em_bo_tor_root-gro_wei_uni,
        qua_pcs_val         TYPE /scmtms/s_em_bo_tor_root-qua_pcs_val,
        qua_pcs_uni         TYPE /scmtms/s_em_bo_tor_root-qua_pcs_uni,
        trmodcod            TYPE /scmtms/s_em_bo_tor_root-trmodcod,
        ref_doc_id          TYPE tt_ref_doc_id,
        ref_doc_type        TYPE tt_ref_doc_type,
        pln_arr_loc_id      TYPE /scmtms/s_em_bo_tor_stop-log_locid,
        pln_arr_loc_type    TYPE /saptrx/loc_id_type,
        pln_arr_timest      TYPE char16,
        pln_arr_timezone    TYPE timezone,
        pln_dep_loc_id      TYPE /scmtms/s_em_bo_tor_stop-log_locid,
        pln_dep_loc_type    TYPE /saptrx/loc_id_type,
        pln_dep_timest      TYPE char16,
        pln_dep_timezone    TYPE timezone,
        stop_id             TYPE tt_stop_id,
        ordinal_no          TYPE tt_ordinal_no,
        loc_type            TYPE tt_loc_type,
        loc_id              TYPE tt_loc_id,
        req_doc_line_no     TYPE tt_req_doc_line_number,
        req_doc_no          TYPE tt_req_doc_number,
      END OF ts_freight_booking.

    CONSTANTS:
      cs_mbl_doctype_ocean TYPE string VALUE 'T52',
      cs_mbl_doctype_air   TYPE string VALUE 'T55'.

    METHODS get_data_from_maintab
      IMPORTING
        ir_maintab         TYPE REF TO data
        iv_old_data        TYPE abap_bool DEFAULT abap_false
      CHANGING
        cs_freight_booking TYPE ts_freight_booking
      RAISING
        cx_udm_message.

    METHODS get_tracked_objects
      IMPORTING
        ir_data            TYPE REF TO data
        iv_old_data        TYPE abap_bool DEFAULT abap_false
      CHANGING
        cs_freight_booking TYPE ts_freight_booking
      RAISING
        cx_udm_message.

    METHODS get_maintabref
      IMPORTING
        is_app_object        TYPE trxas_appobj_ctab_wa
      RETURNING
        VALUE(rr_maintabref) TYPE REF TO data.

    METHODS get_vessel_track
      IMPORTING
        ir_data                TYPE REF TO data
        iv_old_data            TYPE abap_bool
      CHANGING
        ct_tracked_object_type TYPE tt_tracked_object_type
        ct_tracked_object_id   TYPE tt_tracked_object_id
      RAISING
        cx_udm_message.

    METHODS get_vessel_track_id
      IMPORTING
        is_app_object    TYPE trxas_appobj_ctab_wa
      CHANGING
        ct_track_id_data TYPE lif_ef_types=>tt_track_id_data
      RAISING
        cx_udm_message.

    METHODS get_data_from_item
      IMPORTING
        ir_data            TYPE REF TO data
        iv_old_data        TYPE abap_bool DEFAULT abap_false
      CHANGING
        cs_freight_booking TYPE ts_freight_booking
      RAISING
        cx_udm_message.

ENDCLASS.

CLASS lcl_bo_freight_booking_reader IMPLEMENTATION.

  METHOD lif_bo_reader~get_data.

    FIELD-SYMBOLS <ls_freight_booking> TYPE ts_freight_booking.

    rr_data = NEW ts_freight_booking( ).
    ASSIGN rr_data->* TO <ls_freight_booking>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    DATA(lr_maintabref) = get_maintabref( is_app_object ).
    get_data_from_maintab(
      EXPORTING
        iv_old_data        = iv_old_data
        ir_maintab         = lr_maintabref
      CHANGING
        cs_freight_booking = <ls_freight_booking> ).
    IF <ls_freight_booking> IS INITIAL.
      RETURN.
    ENDIF.

    get_tracked_objects(
      EXPORTING
        iv_old_data        = iv_old_data
        ir_data            = lr_maintabref
      CHANGING
        cs_freight_booking = <ls_freight_booking> ).
    IF <ls_freight_booking>-tracked_object_id IS INITIAL.
      APPEND '' TO <ls_freight_booking>-tracked_object_id.
    ENDIF.

    get_data_from_item(
      EXPORTING
        iv_old_data        = iv_old_data
        ir_data            = lr_maintabref
      CHANGING
        cs_freight_booking = <ls_freight_booking> ).

    get_docref_data(
      EXPORTING
        iv_old_data     = iv_old_data
        ir_root         = lr_maintabref
      CHANGING
        ct_ref_doc_id   = <ls_freight_booking>-ref_doc_id
        ct_ref_doc_type = <ls_freight_booking>-ref_doc_type ).
    IF <ls_freight_booking>-ref_doc_id IS INITIAL.
      APPEND '' TO <ls_freight_booking>-ref_doc_id.
    ENDIF.

    get_data_from_stop(
      EXPORTING
        ir_data             = lr_maintabref
        iv_old_data         = iv_old_data
      CHANGING
        cv_pln_dep_loc_id   = <ls_freight_booking>-pln_dep_loc_id
        cv_pln_dep_loc_type = <ls_freight_booking>-pln_dep_loc_type
        cv_pln_dep_timest   = <ls_freight_booking>-pln_dep_timest
        cv_pln_dep_timezone = <ls_freight_booking>-pln_dep_timezone
        cv_pln_arr_loc_id   = <ls_freight_booking>-pln_arr_loc_id
        cv_pln_arr_loc_type = <ls_freight_booking>-pln_arr_loc_type
        cv_pln_arr_timest   = <ls_freight_booking>-pln_arr_timest
        cv_pln_arr_timezone = <ls_freight_booking>-pln_arr_timezone
        ct_stop_id          = <ls_freight_booking>-stop_id
        ct_ordinal_no       = <ls_freight_booking>-ordinal_no
        ct_loc_type         = <ls_freight_booking>-loc_type
        ct_loc_id           = <ls_freight_booking>-loc_id ).

    get_requirement_doc_list(
      EXPORTING
        ir_data            = lr_maintabref
        iv_old_data        = iv_old_data
      CHANGING
        ct_req_doc_line_no = <ls_freight_booking>-req_doc_line_no
        ct_req_doc_no      = <ls_freight_booking>-req_doc_no ).
    IF <ls_freight_booking>-req_doc_no IS INITIAL.
      APPEND '' TO <ls_freight_booking>-req_doc_line_no.
    ENDIF.

  ENDMETHOD.

  METHOD lif_bo_reader~get_track_id_data.
    "FB
    DATA: lr_item_new          TYPE REF TO data,
          lr_item_old          TYPE REF TO data,
          lr_root_new          TYPE REF TO data,
          lr_root_old          TYPE REF TO data,
          lt_track_id_data_new TYPE lif_ef_types=>tt_enh_track_id_data,
          lt_track_id_data_old TYPE lif_ef_types=>tt_enh_track_id_data.

    FIELD-SYMBOLS: <lt_item_new> TYPE /scmtms/t_em_bo_tor_item,
                   <lt_item_old> TYPE /scmtms/t_em_bo_tor_item,
                   <ls_root_new> TYPE /scmtms/s_em_bo_tor_root,
                   <lt_root_new> TYPE /scmtms/t_em_bo_tor_root,
                   <lt_root_old> TYPE /scmtms/t_em_bo_tor_root.

    ASSIGN is_app_object-maintabref->* TO <ls_root_new>.
    IF sy-subrc <> 0.
      RETURN.
    ENDIF.

    lr_root_new = mo_ef_parameters->get_appl_table( iv_tabledef = lif_sst_constants=>cs_tabledef-fo_header_new ).
    ASSIGN lr_root_new->* TO <lt_root_new>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    lr_root_old = mo_ef_parameters->get_appl_table( iv_tabledef = lif_sst_constants=>cs_tabledef-fo_header_old ).
    ASSIGN lr_root_old->* TO <lt_root_old>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO lv_dummy.
      lcl_tools=>throw_exception( ).
    ENDIF.

    add_track_id_data(
      EXPORTING
        is_app_object = is_app_object
        iv_trxcod     = lif_sst_constants=>cs_trxcod-fo_number
        iv_trxid      = |{ <ls_root_new>-tor_id }|
      CHANGING
        ct_track_id   = et_track_id_data ).

    get_container_mobile_track_id(
      EXPORTING
        is_app_object    = is_app_object
      CHANGING
        ct_track_id_data = lt_track_id_data_new ).

    get_container_mobile_track_id(
      EXPORTING
        is_app_object    = is_app_object
        iv_old_data      = abap_true
      CHANGING
        ct_track_id_data = lt_track_id_data_old ).

    lr_item_new     = mo_ef_parameters->get_appl_table( iv_tabledef = lif_sst_constants=>cs_tabledef-fo_item_new ).
    lr_item_old = mo_ef_parameters->get_appl_table( iv_tabledef = lif_sst_constants=>cs_tabledef-fo_item_old ).

    ASSIGN <lt_root_old>[ node_id = <ls_root_new>-node_id ] TO FIELD-SYMBOL(<ls_root_old>).
    IF sy-subrc = 0.
      DATA(lv_deleted) = lcl_tools=>check_is_fo_deleted(
                          is_root_new = <ls_root_new>
                          is_root_old = <ls_root_old> ).
      IF lv_deleted = lif_ef_constants=>cs_condition-true.
        CLEAR: lt_track_id_data_old, lr_item_old.
      ENDIF.
    ENDIF.

    ASSIGN lr_item_new->* TO <lt_item_new>.
    IF <lt_item_new> IS ASSIGNED.
      LOOP AT <lt_item_new> ASSIGNING FIELD-SYMBOL(<ls_item>).

        IF <ls_item>-vessel_id IS ASSIGNED AND <ls_item>-item_id   IS ASSIGNED AND
           <ls_item>-item_cat IS ASSIGNED AND <ls_item>-item_cat = /scmtms/if_tor_const=>sc_tor_item_category-booking.

          IF <ls_root_new>-tor_id IS NOT INITIAL AND <ls_item>-vessel_id IS NOT INITIAL.
            APPEND VALUE #( key = <ls_item>-item_id
                    appsys      = mo_ef_parameters->get_appsys( )
                    appobjtype  = is_app_object-appobjtype
                    appobjid    = is_app_object-appobjid
                    trxcod      = lif_sst_constants=>cs_trxcod-fo_resource
                    trxid       = |{ <ls_root_new>-tor_id }{ <ls_item>-vessel_id }|
                    start_date  = lcl_tools=>get_system_date_time( )
                    end_date    = lif_ef_constants=>cv_max_end_date
                    timzon      = lcl_tools=>get_system_time_zone( )
                    msrid       = space  ) TO lt_track_id_data_new.
          ENDIF.
        ENDIF.
      ENDLOOP.
    ELSE.
    ENDIF.

    ASSIGN lr_item_old->* TO <lt_item_old>.
    IF sy-subrc = 0 AND lv_deleted = lif_ef_constants=>cs_condition-false.
      LOOP AT <lt_item_old> ASSIGNING FIELD-SYMBOL(<ls_item_old>).

        IF <ls_item>-vessel_id IS ASSIGNED AND <ls_item>-item_id   IS ASSIGNED AND
           <ls_item>-item_cat IS ASSIGNED AND <ls_item>-item_cat = /scmtms/if_tor_const=>sc_tor_item_category-booking.

          IF <ls_root_old>-tor_id IS NOT INITIAL AND <ls_item>-vessel_id IS NOT INITIAL.
            APPEND VALUE #( key = <ls_item>-item_id
                    appsys      = mo_ef_parameters->get_appsys( )
                    appobjtype  = is_app_object-appobjtype
                    appobjid    = is_app_object-appobjid
                    trxcod      = lif_sst_constants=>cs_trxcod-fo_resource
                    trxid       = |{ <ls_root_old>-tor_id }{ <ls_item>-vessel_id }|
                    start_date  = lcl_tools=>get_system_date_time( )
                    end_date    = lif_ef_constants=>cv_max_end_date
                    timzon      = lcl_tools=>get_system_time_zone( )
                    msrid       = space  ) TO lt_track_id_data_old.
          ENDIF.
        ENDIF.
      ENDLOOP.
    ENDIF.

    lcl_tools=>get_track_obj_changes(
    EXPORTING
      is_app_object        = is_app_object
      iv_appsys            = mo_ef_parameters->get_appsys( )
      it_track_id_data_new = lt_track_id_data_new
      it_track_id_data_old = lt_track_id_data_old
    CHANGING
      ct_track_id_data     = et_track_id_data ).

  ENDMETHOD.

  METHOD get_data_from_maintab.

    FIELD-SYMBOLS:
      <ls_root>     TYPE /scmtms/s_em_bo_tor_root,
      <lt_root_old> TYPE /scmtms/t_em_bo_tor_root.

    ASSIGN ir_maintab->* TO <ls_root>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    IF iv_old_data = abap_true.
      DATA(lr_root_old) = mo_ef_parameters->get_appl_table( lif_sst_constants=>cs_tabledef-fo_header_old ).

      ASSIGN lr_root_old->* TO <lt_root_old>.
      IF sy-subrc = 0.
        ASSIGN <lt_root_old>[ tor_id = <ls_root>-tor_id ] TO <ls_root>.
        IF sy-subrc <> 0.
          " Record was just created
          RETURN.
        ENDIF.
      ENDIF.
      DATA(lv_before_image) = abap_true.
    ENDIF.

    cs_freight_booking-tor_id = <ls_root>-tor_id.
    SHIFT cs_freight_booking-tor_id LEFT DELETING LEADING '0'.
    cs_freight_booking-dgo_indicator = <ls_root>-dgo_indicator.
    cs_freight_booking-tspid = get_carrier_name( iv_tspid = CONV #( <ls_root>-tspid ) ).

    SELECT SINGLE motscode
      FROM /sapapo/trtype
      INTO cs_freight_booking-mtr
      WHERE ttype = <ls_root>-mtr.
    SHIFT cs_freight_booking-mtr LEFT DELETING LEADING '0'.

    /scmtms/cl_tor_helper_root=>det_transient_root_fields(
      EXPORTING
        it_key               = VALUE #( ( key = <ls_root>-node_id ) )
        iv_get_stop_infos    = abap_true
        iv_get_mainitem_info = abap_true
        iv_before_image      = lv_before_image
      IMPORTING
        et_tor_add_info      = DATA(lt_tor_add_info) ).
    ASSIGN lt_tor_add_info[ 1 ] TO FIELD-SYMBOL(<ls_tor_additional_info>).
    IF sy-subrc = 0.
      cs_freight_booking-pln_grs_duration = <ls_tor_additional_info>-tot_duration.
    ENDIF.

    cs_freight_booking-total_duration_net = <ls_root>-total_duration_net.
    cs_freight_booking-total_distance_km  = <ls_root>-total_distance_km.
    cs_freight_booking-traffic_direct     = <ls_root>-traffic_direct.
    cs_freight_booking-shipping_type      = <ls_root>-shipping_type.
    IF <ls_root>-trmodcod = lif_sst_constants=>cs_trmodcod-air.
      cs_freight_booking-trmodcod = lif_sst_constants=>cs_trmodcod-inland_waterway.
    ELSE.
      cs_freight_booking-trmodcod = lif_sst_constants=>cs_trmodcod-road.
    ENDIF.
  ENDMETHOD.

  METHOD get_data_from_item.

    FIELD-SYMBOLS:
      <lt_tor_item> TYPE /scmtms/t_em_bo_tor_item,
      <ls_tor_root> TYPE /scmtms/s_em_bo_tor_root.

    ASSIGN ir_data->* TO <ls_tor_root>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    DATA(lr_item) = mo_ef_parameters->get_appl_table(
                        SWITCH #( iv_old_data WHEN abap_true THEN lif_sst_constants=>cs_tabledef-fo_item_old
                                              ELSE lif_sst_constants=>cs_tabledef-fo_item_new ) ).
    ASSIGN lr_item->* TO <lt_tor_item>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO lv_dummy.
      lcl_tools=>throw_exception( ).
    ENDIF.

    ASSIGN <lt_tor_item>[ item_cat       = /scmtms/if_tor_const=>sc_tor_item_category-booking
                          parent_node_id = <ls_tor_root>-node_id ] TO FIELD-SYMBOL(<ls_booking_item>).
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO lv_dummy.
      lcl_tools=>throw_exception( ).
    ENDIF.

    cs_freight_booking-inc_class_code   = <ls_booking_item>-inc_class_code.
    cs_freight_booking-inc_transf_loc_n = <ls_booking_item>-inc_transf_loc_n.
    cs_freight_booking-gro_vol_val      = <ls_booking_item>-gro_vol_val.
    cs_freight_booking-gro_vol_uni      = <ls_booking_item>-gro_vol_uni.
    cs_freight_booking-gro_wei_val      = <ls_booking_item>-gro_wei_val.
    cs_freight_booking-gro_wei_uni      = <ls_booking_item>-gro_wei_uni.
    cs_freight_booking-qua_pcs_val      = <ls_booking_item>-qua_pcs_val.
    cs_freight_booking-qua_pcs_uni      = <ls_booking_item>-qua_pcs_uni.

  ENDMETHOD.

  METHOD get_maintabref.
    FIELD-SYMBOLS <lt_maintabref> TYPE ANY TABLE.

    ASSIGN is_app_object-maintabref->* TO FIELD-SYMBOL(<ls_maintabref>).

    IF <ls_maintabref> IS ASSIGNED AND lcl_tools=>is_table( iv_value = <ls_maintabref> ) = abap_true.
      ASSIGN <ls_maintabref> TO <lt_maintabref>.
      LOOP AT <lt_maintabref> ASSIGNING FIELD-SYMBOL(<ls_line>).
        ASSIGN COMPONENT /scmtms/if_tor_c=>sc_node_attribute-root-tor_cat
          OF STRUCTURE <ls_line> TO FIELD-SYMBOL(<lv_tor_cat>).
        IF sy-subrc = 0 AND <lv_tor_cat> = /scmtms/if_tor_const=>sc_tor_category-booking.
          GET REFERENCE OF <ls_line> INTO rr_maintabref.
          EXIT.
        ENDIF.
      ENDLOOP.
    ELSEIF <ls_maintabref> IS ASSIGNED.
      GET REFERENCE OF <ls_maintabref> INTO rr_maintabref.
    ENDIF.
  ENDMETHOD.

  METHOD get_vessel_track.

    FIELD-SYMBOLS:
      <lt_tor_item> TYPE /scmtms/t_em_bo_tor_item,
      <ls_tor_root> TYPE /scmtms/s_em_bo_tor_root.

    ASSIGN ir_data->* TO <ls_tor_root>.
    IF sy-subrc = 0.
      DATA(lr_item) = mo_ef_parameters->get_appl_table(
                        SWITCH #( iv_old_data WHEN abap_false THEN lif_sst_constants=>cs_tabledef-fo_item_new
                                              ELSE lif_sst_constants=>cs_tabledef-fo_item_old ) ).
      ASSIGN lr_item->* TO <lt_tor_item>.
      IF sy-subrc = 0.
        ASSIGN <lt_tor_item>[ item_cat       = /scmtms/if_tor_const=>sc_tor_item_category-booking
                              parent_node_id = <ls_tor_root>-node_id ]-vessel_id TO FIELD-SYMBOL(<lv_vessel_id>).
        IF sy-subrc = 0.
          IF <lv_vessel_id> IS NOT INITIAL.
            APPEND cs_track_id-vessel TO ct_tracked_object_id.
            APPEND <lv_vessel_id>     TO ct_tracked_object_type.
          ENDIF.
        ENDIF.
      ENDIF.
    ENDIF.
  ENDMETHOD.

  METHOD get_vessel_track_id.

    FIELD-SYMBOLS:
      <lt_tor_item> TYPE /scmtms/t_em_bo_tor_item,
      <ls_tor_root> TYPE /scmtms/s_em_bo_tor_root.

    ASSIGN is_app_object-maintabref->* TO <ls_tor_root>.
    IF sy-subrc = 0.
      DATA(lr_item) = mo_ef_parameters->get_appl_table( iv_tabledef = lif_sst_constants=>cs_tabledef-fo_item_new ).
      ASSIGN lr_item->* TO <lt_tor_item>.
      IF sy-subrc = 0.
        ASSIGN <lt_tor_item>[ item_cat       = /scmtms/if_tor_const=>sc_tor_item_category-booking
                              parent_node_id = <ls_tor_root>-node_id ]-vessel_id TO FIELD-SYMBOL(<lv_vessel_id>).
        IF sy-subrc = 0.
          add_track_id_data(
            EXPORTING
              is_app_object = is_app_object
              iv_trxcod     = lif_sst_constants=>cs_trxcod-fo_resource
              iv_trxid      = |{ <ls_tor_root>-tor_id }{ <lv_vessel_id> }|
            CHANGING
              ct_track_id   = ct_track_id_data ).
        ENDIF.
      ENDIF.
    ENDIF.
  ENDMETHOD.

  METHOD get_tracked_objects.

    get_container_and_mobile_track(
      EXPORTING
        ir_data                = ir_data
        iv_old_data            = iv_old_data
      CHANGING
        ct_tracked_object_type = cs_freight_booking-tracked_object_type
        ct_tracked_object_id   = cs_freight_booking-tracked_object_id ).

    get_vessel_track(
      EXPORTING
        iv_old_data            = iv_old_data
        ir_data                = ir_data
      CHANGING
        ct_tracked_object_type = cs_freight_booking-tracked_object_type
        ct_tracked_object_id   = cs_freight_booking-tracked_object_id ).

  ENDMETHOD.

  METHOD get_docref_data.

    DATA: lv_master_bill_of_landing TYPE string.

    FIELD-SYMBOLS:
      <ls_root>     TYPE /scmtms/s_em_bo_tor_root,
      <lt_root_old> TYPE /scmtms/t_em_bo_tor_root.

    super->get_docref_data(
      EXPORTING
        ir_root         = ir_root
        iv_old_data     = iv_old_data
      CHANGING
        ct_ref_doc_id   = ct_ref_doc_id
        ct_ref_doc_type = ct_ref_doc_type ).

    ASSIGN ir_root->* TO <ls_root>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    IF iv_old_data = abap_true.
      DATA(lr_root_old) = mo_ef_parameters->get_appl_table( lif_sst_constants=>cs_tabledef-fo_header_old ).
      ASSIGN lr_root_old->* TO <lt_root_old>.
      IF sy-subrc = 0.
        ASSIGN <lt_root_old>[ tor_id = <ls_root>-tor_id ] TO <ls_root>.
        IF sy-subrc <> 0.
          MESSAGE e010(zsst_gtt) INTO lv_dummy.
          lcl_tools=>throw_exception( ).
        ENDIF.
        DATA(lv_before_image) = abap_true.
      ENDIF.
    ENDIF.


    IF <ls_root>-trmodcod = lif_sst_constants=>cs_trmodcod-air.
      IF <ls_root>-tsp_airlcawb IS NOT INITIAL AND <ls_root>-partner_mbl_id IS INITIAL.
        lv_master_bill_of_landing = <ls_root>-tsp_airlcawb.
      ELSEIF <ls_root>-tsp_airlcawb IS INITIAL AND <ls_root>-partner_mbl_id IS NOT INITIAL.
        lv_master_bill_of_landing = <ls_root>-partner_mbl_id.
      ELSEIF <ls_root>-tsp_airlcawb IS NOT INITIAL AND <ls_root>-partner_mbl_id IS NOT INITIAL.
        lv_master_bill_of_landing = |{ <ls_root>-tsp_airlcawb }-{ <ls_root>-partner_mbl_id }|.
      ENDIF.
      IF lv_master_bill_of_landing IS NOT INITIAL.
        APPEND lv_master_bill_of_landing TO ct_ref_doc_id.
        APPEND cs_mbl_doctype_air TO ct_ref_doc_type.
      ENDIF.
    ELSE.
      IF <ls_root>-partner_mbl_id IS NOT INITIAL.
        APPEND <ls_root>-partner_mbl_id TO ct_ref_doc_id.
        APPEND cs_mbl_doctype_ocean TO ct_ref_doc_type.
      ENDIF.
    ENDIF.

  ENDMETHOD.

ENDCLASS.

CLASS lcl_bo_freight_unit_reader DEFINITION INHERITING FROM lcl_bo_tor_reader.

  PUBLIC SECTION.
    METHODS lif_bo_reader~get_data          REDEFINITION.
    METHODS lif_bo_reader~check_relevance   REDEFINITION.
    METHODS lif_bo_reader~get_track_id_data REDEFINITION.

    TYPES:
      BEGIN OF ts_freight_unit,
        tor_id             TYPE /scmtms/s_em_bo_tor_root-tor_id,
        shipping_type      TYPE /scmtms/s_em_bo_tor_root-shipping_type,
        inc_class_code     TYPE /scmtms/s_em_bo_tor_item-inc_class_code,
        trmodcod           TYPE /scmtms/s_em_bo_tor_root-trmodcod,
        total_distance_km  TYPE /scmtms/total_distance_km,
        pln_grs_duration   TYPE /scmtms/total_duration_net,
        total_duration_net TYPE /scmtms/total_duration_net,
        dgo_indicator      TYPE /scmtms/s_em_bo_tor_root-dgo_indicator,
        pln_arr_loc_id     TYPE /scmtms/s_em_bo_tor_stop-log_locid,
        pln_arr_loc_type   TYPE /saptrx/loc_id_type,
        pln_arr_timest     TYPE char16,
        pln_arr_timezone   TYPE timezone,
        pln_dep_loc_id     TYPE /scmtms/s_em_bo_tor_stop-log_locid,
        pln_dep_loc_type   TYPE /saptrx/loc_id_type,
        pln_dep_timest     TYPE char16,
        pln_dep_timezone   TYPE timezone,
        tspid              TYPE bu_id_number,
        ref_doc_id         TYPE tt_ref_doc_id,
        ref_doc_type       TYPE tt_ref_doc_type,
        stop_id            TYPE tt_stop_id,
        ordinal_no         TYPE tt_ordinal_no,
        loc_type           TYPE tt_loc_type,
        loc_id             TYPE tt_loc_id,
        item_id            TYPE STANDARD TABLE OF /scmtms/item_id              WITH EMPTY KEY,
        erp_dlv_id         TYPE STANDARD TABLE OF /scmtms/erp_shpm_dlv_id      WITH EMPTY KEY,
        erp_dlv_item_id    TYPE STANDARD TABLE OF /scmtms/erp_shpm_dlv_item_id WITH EMPTY KEY,
        itm_qua_pcs_val	   TYPE STANDARD TABLE OF /scmtms/qua_pcs_val          WITH EMPTY KEY,
        itm_qua_pcs_uni	   TYPE STANDARD TABLE OF /scmtms/qua_pcs_uni          WITH EMPTY KEY,
        product_id         TYPE STANDARD TABLE OF /scmtms/product_id           WITH EMPTY KEY,
        product_txt        TYPE STANDARD TABLE OF /scmtms/item_description     WITH EMPTY KEY,
        dlv_item_alt_id    TYPE STANDARD TABLE OF char16                       WITH EMPTY KEY,
        capa_doc_line_no   TYPE tt_capacity_doc_line_number,
        capa_doc_no        TYPE tt_capacity_doc_number,
      END OF ts_freight_unit.

    CONSTANTS:
      cs_base_btd_tco_inb_dlv       TYPE /scmtms/base_btd_tco VALUE '58',
      cs_base_btd_tco_outb_dlv      TYPE /scmtms/base_btd_tco VALUE '73',
      cs_base_btd_tco_delivery_item TYPE /scmtms/base_btd_item_tco VALUE '14'.

    METHODS get_data_from_maintab
      IMPORTING
        ir_maintab      TYPE REF TO data
        iv_old_data     TYPE abap_bool DEFAULT abap_false
      CHANGING
        cs_freight_unit TYPE ts_freight_unit
      RAISING
        cx_udm_message.

    METHODS check_fo_track_obj_changes
      IMPORTING
        is_app_object    TYPE trxas_appobj_ctab_wa
      RETURNING
        VALUE(rv_result) TYPE lif_ef_types=>tv_condition
      RAISING
        cx_udm_message.

    METHODS get_maintabref
      IMPORTING
        is_app_object        TYPE trxas_appobj_ctab_wa
      RETURNING
        VALUE(rr_maintabref) TYPE REF TO data.

    METHODS get_data_from_item
      IMPORTING
        ir_data         TYPE REF TO data
        iv_old_data     TYPE abap_bool DEFAULT abap_false
      CHANGING
        cs_freight_unit TYPE ts_freight_unit
      RAISING
        cx_udm_message.

    METHODS get_capacity_doc_list
      IMPORTING
        ir_data             TYPE REF TO data
        iv_old_data         TYPE abap_bool DEFAULT abap_false
      CHANGING
        ct_capa_doc_line_no TYPE tt_capacity_doc_line_number
        ct_capa_doc_no      TYPE tt_capacity_doc_number
      RAISING
        cx_udm_message.

    METHODS check_fo_route_change
      IMPORTING
        is_app_object    TYPE trxas_appobj_ctab_wa
      RETURNING
        VALUE(rv_result) TYPE lif_ef_types=>tv_condition
      RAISING
        cx_udm_message.

  PROTECTED SECTION.
    METHODS check_non_idoc_stop_fields REDEFINITION.
    METHODS check_non_idoc_fields      REDEFINITION.

ENDCLASS.

CLASS lcl_bo_freight_unit_reader IMPLEMENTATION.

  METHOD check_non_idoc_stop_fields.

    DATA lt_capa_stop_old TYPE /scmtms/t_tor_stop_k.

    FIELD-SYMBOLS:
      <lt_stop_new>      TYPE /scmtms/t_em_bo_tor_stop,
      <lt_stop_old>      TYPE /scmtms/t_em_bo_tor_stop,
      <lt_capa_stop_new> TYPE /scmtms/t_em_bo_tor_stop,
      <ls_header>        TYPE /scmtms/s_em_bo_tor_root.

    rv_result = lif_ef_constants=>cs_condition-false.

    DATA(lt_stop_new) = mo_ef_parameters->get_appl_table(
                            iv_tabledef = lif_sst_constants=>cs_tabledef-fo_stop_new ).
    DATA(lt_stop_old) = mo_ef_parameters->get_appl_table(
                            iv_tabledef = lif_sst_constants=>cs_tabledef-fo_stop_old ).
    DATA(lt_capa_stop_new) = mo_ef_parameters->get_appl_table(
                               /scmtms/cl_scem_int_c=>sc_table_definition-bo_tor-capa_stop ).

    ASSIGN lt_stop_new->* TO <lt_stop_new>.
    ASSIGN lt_stop_old->* TO <lt_stop_old>.
    ASSIGN lt_capa_stop_new->* TO <lt_capa_stop_new>.
    ASSIGN is_app_object-maintabref->* TO <ls_header>.
    IF <lt_stop_new>      IS NOT ASSIGNED OR <lt_stop_old> IS NOT ASSIGNED OR
       <lt_capa_stop_new> IS NOT ASSIGNED OR <ls_header> IS NOT ASSIGNED.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    DATA(lo_tor_srv_mgr) = /bobf/cl_tra_serv_mgr_factory=>get_service_manager( iv_bo_key = /scmtms/if_tor_c=>sc_bo_key ).
    DATA(lt_capa_stop_key) = VALUE /bobf/t_frw_key( FOR <ls_stop> IN <lt_stop_new> ( key = <ls_stop>-assgn_stop_key ) ).
    lo_tor_srv_mgr->retrieve(
      EXPORTING
        iv_node_key     = /scmtms/if_tor_c=>sc_node-stop
        it_key          = lt_capa_stop_key
        iv_before_image = abap_true
      IMPORTING
        et_data         = lt_capa_stop_old ).

    LOOP AT <lt_stop_new> ASSIGNING FIELD-SYMBOL(<ls_stop_new>)
      USING KEY parent_seqnum WHERE parent_node_id = <ls_header>-node_id.

      ASSIGN <lt_stop_old>[ node_id = <ls_stop_new>-node_id ] TO FIELD-SYMBOL(<ls_stop_old>).
      CHECK sy-subrc = 0.

      IF <ls_stop_new>-assgn_start <> <ls_stop_old>-assgn_start OR
         <ls_stop_new>-assgn_end   <> <ls_stop_old>-assgn_end.
        rv_result = lif_ef_constants=>cs_condition-true.
        EXIT.
      ENDIF.

      ASSIGN <lt_capa_stop_new>[ node_id = <ls_stop_new>-assgn_stop_key ] TO FIELD-SYMBOL(<ls_capa_stop_new>).
      CHECK sy-subrc = 0.

      ASSIGN lt_capa_stop_old[ key = <ls_stop_new>-assgn_stop_key ] TO FIELD-SYMBOL(<ls_capa_stop_old>).
      CHECK sy-subrc = 0.

      IF <ls_capa_stop_new>-plan_trans_time <> <ls_capa_stop_old>-plan_trans_time.
        rv_result = lif_ef_constants=>cs_condition-true.
        EXIT.
      ENDIF.

    ENDLOOP.

  ENDMETHOD.

  METHOD check_fo_track_obj_changes.
    "FU
    DATA:
      lr_item_new          TYPE REF TO data,
      lr_item_old          TYPE REF TO data,
      lr_root_new          TYPE REF TO data,
      lr_root_old          TYPE REF TO data,
      lt_track_id_data     TYPE lif_ef_types=>tt_track_id_data,
      lt_track_id_data_new TYPE lif_ef_types=>tt_enh_track_id_data,
      lt_track_id_data_old TYPE lif_ef_types=>tt_enh_track_id_data,
      ls_capa_root_fo      TYPE /scmtms/s_em_bo_tor_root.

    FIELD-SYMBOLS:
      <lt_item_new>          TYPE /scmtms/t_em_bo_tor_item,
      <lt_item_old>          TYPE /scmtms/t_em_bo_tor_item,
      <ls_root>              TYPE /scmtms/s_em_bo_tor_root,
      <ls_root_new>          TYPE /scmtms/s_em_bo_tor_root,
      <ls_root_old>          TYPE /scmtms/s_em_bo_tor_root,
      <lt_tor_root_capa_new> TYPE /scmtms/t_em_bo_tor_root,
      <lt_tor_root_capa_old> TYPE /scmtms/t_em_bo_tor_root.

    rv_result = lif_ef_constants=>cs_condition-false.

    ASSIGN is_app_object-maintabref->* TO <ls_root>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    DATA(lr_root_capa_new) = mo_ef_parameters->get_appl_table(
                                  iv_tabledef = /scmtms/cl_scem_int_c=>sc_table_definition-bo_tor-capa_root ).
    ASSIGN lr_root_capa_new->* TO <lt_tor_root_capa_new>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO lv_dummy.
      lcl_tools=>throw_exception( ).
    ENDIF.

    DATA(lr_capa_root_old) = mo_ef_parameters->get_appl_table(
                                  iv_tabledef = /scmtms/cl_scem_int_c=>sc_table_definition-bo_tor-capa_root_before ).
    ASSIGN lr_capa_root_old->* TO <lt_tor_root_capa_old>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO lv_dummy.
      lcl_tools=>throw_exception( ).
    ENDIF.

    DATA(lo_tor_srv_mgr) = /bobf/cl_tra_serv_mgr_factory=>get_service_manager( iv_bo_key = /scmtms/if_tor_c=>sc_bo_key ).
    lo_tor_srv_mgr->retrieve_by_association(
      EXPORTING
        iv_node_key    = /scmtms/if_tor_c=>sc_node-root
        it_key         = VALUE #( ( key = <ls_root>-node_id ) )
        iv_association = /scmtms/if_tor_c=>sc_association-root-capa_tor
      IMPORTING
        et_key_link    = DATA(lt_req2capa_link) ).

    LOOP AT lt_req2capa_link ASSIGNING FIELD-SYMBOL(<ls_req2capa_link>).
      ASSIGN <lt_tor_root_capa_new>[ node_id = <ls_req2capa_link>-target_key ] TO <ls_root_new>.
      CHECK sy-subrc = 0.

      ASSIGN <lt_tor_root_capa_old>[ node_id = <ls_req2capa_link>-target_key ] TO <ls_root_old>.
      CHECK sy-subrc = 0.

      DATA(ls_app_object) = is_app_object.
      ls_capa_root_fo = CORRESPONDING #( <ls_root_new> MAPPING node_id = node_id  ).
      GET REFERENCE OF ls_capa_root_fo INTO ls_app_object-maintabref.

      get_container_mobile_track_id(
        EXPORTING
          is_app_object    = ls_app_object
        CHANGING
          ct_track_id_data = lt_track_id_data_new ).

      get_container_mobile_track_id(
        EXPORTING
          is_app_object    = ls_app_object
          iv_old_data      = abap_true
        CHANGING
          ct_track_id_data = lt_track_id_data_old ).

      lr_item_new = mo_ef_parameters->get_appl_table( iv_tabledef = lif_sst_constants=>cs_tabledef-fo_item_new ).
      lr_item_old = mo_ef_parameters->get_appl_table( iv_tabledef = lif_sst_constants=>cs_tabledef-fo_item_old ).

      DATA(lv_deleted) = lcl_tools=>check_is_fo_deleted(
                             is_root_new = <ls_root_new>
                             is_root_old = <ls_root_old> ).
      IF lv_deleted = lif_ef_constants=>cs_condition-true.
        CLEAR: lt_track_id_data_old, lr_item_old.
      ENDIF.

      ASSIGN lr_item_new->* TO <lt_item_new>.
      IF <lt_item_new> IS ASSIGNED.
        lcl_tools=>get_fo_tracked_item_obj(
          EXPORTING
            is_app_object = ls_app_object
            is_root       = <ls_root_new>
            it_item       = <lt_item_new>
            iv_appsys     = mo_ef_parameters->get_appsys( )
            iv_old_data   = abap_false
         CHANGING
            ct_track_id_data = lt_track_id_data_new ).
      ELSE.
        MESSAGE e010(zsst_gtt) INTO lv_dummy.
        lcl_tools=>throw_exception( ).
      ENDIF.

      ASSIGN lr_item_old->* TO <lt_item_old>.
      IF sy-subrc = 0 AND lv_deleted =  lif_ef_constants=>cs_condition-false.
        lcl_tools=>get_fo_tracked_item_obj(
          EXPORTING
            is_app_object = ls_app_object
            is_root       = <ls_root_old>
            it_item       = <lt_item_old>
            iv_appsys     = mo_ef_parameters->get_appsys( )
            iv_old_data   = abap_true
         CHANGING
            ct_track_id_data = lt_track_id_data_old ).
      ENDIF.

      lcl_tools=>get_track_obj_changes(
        EXPORTING
          is_app_object        = ls_app_object
          iv_appsys            = mo_ef_parameters->get_appsys( )
          it_track_id_data_new = lt_track_id_data_new
          it_track_id_data_old = lt_track_id_data_old
        CHANGING
          ct_track_id_data     = lt_track_id_data ).
    ENDLOOP.

    IF lt_track_id_data IS NOT INITIAL.
      rv_result = lif_ef_constants=>cs_condition-true.
      RETURN.
    ENDIF.
  ENDMETHOD.

  METHOD check_fo_route_change.

    FIELD-SYMBOLS <ls_header> TYPE /scmtms/s_em_bo_tor_root.

    DATA:
      lv_stage_num_difference    TYPE i,
      lv_stage_num_difference_bi TYPE i.

    rv_result = lif_ef_constants=>cs_condition-false.

    ASSIGN is_app_object-maintabref->* TO <ls_header>.
    IF sy-subrc <> 0.
      RETURN.
    ENDIF.

    DATA(lo_tor_srv_mgr) = /bobf/cl_tra_serv_mgr_factory=>get_service_manager( iv_bo_key = /scmtms/if_tor_c=>sc_bo_key ).
    lo_tor_srv_mgr->retrieve_by_association(
      EXPORTING
        iv_node_key    = /scmtms/if_tor_c=>sc_node-root
        it_key         = VALUE #( ( key = <ls_header>-node_id ) )
        iv_association = /scmtms/if_tor_c=>sc_association-root-capa_tor
      IMPORTING
        et_key_link    = DATA(lt_req2capa_kl)
        et_target_key  = DATA(lt_tor_capa_key) ).

    /scmtms/cl_tor_helper_stage=>get_stage(
      EXPORTING
        it_root_key = VALUE #( ( key = <ls_header>-node_id ) )
      IMPORTING
        et_stage    = DATA(lt_req_stage) ).

    /scmtms/cl_tor_helper_stage=>get_stage(
      EXPORTING
        it_root_key = lt_tor_capa_key
      IMPORTING
        et_stage    = DATA(lt_capa_stage) ).

    /scmtms/cl_tor_helper_stage=>get_stage(
      EXPORTING
        it_root_key     = lt_tor_capa_key
        iv_before_image = abap_true
      IMPORTING
        et_stage        = DATA(lt_capa_stage_bi) ).

    DATA(lv_req_stage_count) = lines( lt_req_stage ).
    DATA(lv_stop_des_key) = lt_req_stage[ lv_req_stage_count ]-dest_stop-assgn_stop_key.
    DATA(lv_stop_src_key) = lt_req_stage[ 1 ]-source_stop-assgn_stop_key.

    DO 1 TIMES.

      ASSIGN lt_capa_stage[ KEY source_stop_key COMPONENTS
        source_stop_key = lv_stop_src_key ]-seq_num TO FIELD-SYMBOL(<lv_capa_stage_first_num>).
      CHECK sy-subrc = 0.

      ASSIGN lt_capa_stage[ dest_stop_key = lv_stop_des_key ]-seq_num TO FIELD-SYMBOL(<lv_capa_stage_last_num>).
      CHECK sy-subrc = 0.

      lv_stage_num_difference = <lv_capa_stage_last_num> - <lv_capa_stage_first_num>.

      ASSIGN lt_capa_stage_bi[ KEY source_stop_key COMPONENTS
        source_stop_key = lv_stop_src_key ]-seq_num TO FIELD-SYMBOL(<lv_capa_stage_first_num_bi>).
      CHECK sy-subrc = 0.

      ASSIGN lt_capa_stage_bi[ dest_stop_key = lv_stop_des_key ]-seq_num TO FIELD-SYMBOL(<lv_capa_stage_last_num_bi>).
      CHECK sy-subrc = 0.

      lv_stage_num_difference_bi = <lv_capa_stage_last_num_bi> - <lv_capa_stage_first_num_bi>.

    ENDDO.

    IF lv_stage_num_difference <> lv_stage_num_difference_bi.
      rv_result = lif_ef_constants=>cs_condition-true.
    ENDIF.

  ENDMETHOD.

  METHOD check_non_idoc_fields.

    rv_result = check_non_idoc_stop_fields( is_app_object = is_app_object ).
    IF rv_result = lif_ef_constants=>cs_condition-true.
      RETURN.
    ENDIF.

    rv_result = check_fo_route_change( is_app_object = is_app_object ).

  ENDMETHOD.

  METHOD get_capacity_doc_list.

    DATA lv_capa_doc_line_no TYPE int4.

    FIELD-SYMBOLS:
      <ls_tor_root>      TYPE /scmtms/s_em_bo_tor_root,
      <lt_tor_root_capa> TYPE /scmtms/t_em_bo_tor_root.

    ASSIGN ir_data->* TO <ls_tor_root>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    DATA(lv_tabledef) = SWITCH #( iv_old_data
                          WHEN abap_false THEN /scmtms/cl_scem_int_c=>sc_table_definition-bo_tor-capa_root
                          ELSE /scmtms/cl_scem_int_c=>sc_table_definition-bo_tor-capa_root_before ).

    DATA(lr_req_root) = mo_ef_parameters->get_appl_table( iv_tabledef = lv_tabledef ).
    ASSIGN lr_req_root->* TO <lt_tor_root_capa>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO lv_dummy.
      lcl_tools=>throw_exception( ).
    ENDIF.

    DATA(lo_tor_srv_mgr) = /bobf/cl_tra_serv_mgr_factory=>get_service_manager( iv_bo_key = /scmtms/if_tor_c=>sc_bo_key ).
    lo_tor_srv_mgr->retrieve_by_association(
      EXPORTING
        iv_node_key    = /scmtms/if_tor_c=>sc_node-root
        it_key         = VALUE #( ( key = <ls_tor_root>-node_id ) )
        iv_association = /scmtms/if_tor_c=>sc_association-root-capa_tor
      IMPORTING
        et_key_link    = DATA(lt_req2capa_link) ).

    LOOP AT lt_req2capa_link ASSIGNING FIELD-SYMBOL(<ls_req2capa_link>).
      ASSIGN <lt_tor_root_capa>[ node_id = <ls_req2capa_link>-target_key ]-tor_id TO FIELD-SYMBOL(<lv_tor_capa_id>).
      CHECK sy-subrc = 0.

      lv_capa_doc_line_no += 1.
      APPEND lv_capa_doc_line_no TO ct_capa_doc_line_no.

      APPEND <lv_tor_capa_id> TO ct_capa_doc_no.
    ENDLOOP.

  ENDMETHOD.

  METHOD lif_bo_reader~get_data.

    FIELD-SYMBOLS <ls_freight_unit> TYPE ts_freight_unit.

    rr_data = NEW ts_freight_unit( ).
    ASSIGN rr_data->* TO <ls_freight_unit>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    DATA(lr_maintabref) = get_maintabref( is_app_object ).
    get_data_from_maintab(
      EXPORTING
        iv_old_data     = iv_old_data
        ir_maintab      = lr_maintabref
      CHANGING
        cs_freight_unit = <ls_freight_unit> ).
    IF <ls_freight_unit> IS INITIAL.
      RETURN.
    ENDIF.

    get_data_from_item(
      EXPORTING
        iv_old_data     = iv_old_data
        ir_data         = lr_maintabref
      CHANGING
        cs_freight_unit = <ls_freight_unit> ).
    IF <ls_freight_unit>-item_id IS INITIAL.
      APPEND '' TO <ls_freight_unit>-item_id.
    ENDIF.

    get_docref_data(
      EXPORTING
        iv_old_data     = iv_old_data
        ir_root         = lr_maintabref
      CHANGING
        ct_ref_doc_id   = <ls_freight_unit>-ref_doc_id
        ct_ref_doc_type = <ls_freight_unit>-ref_doc_type ).
    IF <ls_freight_unit>-ref_doc_id IS INITIAL.
      APPEND '' TO <ls_freight_unit>-ref_doc_id.
    ENDIF.

    get_data_from_stop(
      EXPORTING
        ir_data             = lr_maintabref
        iv_old_data         = iv_old_data
      CHANGING
        cv_pln_dep_loc_id   = <ls_freight_unit>-pln_dep_loc_id
        cv_pln_dep_loc_type = <ls_freight_unit>-pln_dep_loc_type
        cv_pln_dep_timest   = <ls_freight_unit>-pln_dep_timest
        cv_pln_dep_timezone = <ls_freight_unit>-pln_dep_timezone
        cv_pln_arr_loc_id   = <ls_freight_unit>-pln_arr_loc_id
        cv_pln_arr_loc_type = <ls_freight_unit>-pln_arr_loc_type
        cv_pln_arr_timest   = <ls_freight_unit>-pln_arr_timest
        cv_pln_arr_timezone = <ls_freight_unit>-pln_arr_timezone
        ct_stop_id          = <ls_freight_unit>-stop_id
        ct_ordinal_no       = <ls_freight_unit>-ordinal_no
        ct_loc_type         = <ls_freight_unit>-loc_type
        ct_loc_id           = <ls_freight_unit>-loc_id ).

    get_capacity_doc_list(
      EXPORTING
        ir_data             = lr_maintabref
        iv_old_data         = iv_old_data
      CHANGING
        ct_capa_doc_line_no = <ls_freight_unit>-capa_doc_line_no
        ct_capa_doc_no      = <ls_freight_unit>-capa_doc_no ).
    IF <ls_freight_unit>-capa_doc_no IS INITIAL.
      APPEND '' TO <ls_freight_unit>-capa_doc_line_no.
    ENDIF.

  ENDMETHOD.

  METHOD get_data_from_maintab.

    FIELD-SYMBOLS:
      <ls_root>     TYPE /scmtms/s_em_bo_tor_root,
      <lt_root_old> TYPE /scmtms/t_em_bo_tor_root.

    ASSIGN ir_maintab->* TO <ls_root>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    IF iv_old_data = abap_true.
      DATA(lr_root_old) = mo_ef_parameters->get_appl_table( lif_sst_constants=>cs_tabledef-fo_header_old ).

      ASSIGN lr_root_old->* TO <lt_root_old>.
      IF sy-subrc = 0.
        ASSIGN <lt_root_old>[ tor_id = <ls_root>-tor_id ] TO <ls_root>.
        IF sy-subrc <> 0.
          " Record was just created
          RETURN.
        ENDIF.
      ENDIF.
      DATA(lv_before_image) = abap_true.
    ENDIF.

    cs_freight_unit-tor_id = <ls_root>-tor_id.
    SHIFT cs_freight_unit-tor_id LEFT DELETING LEADING '0'.
    cs_freight_unit-dgo_indicator = <ls_root>-dgo_indicator.

    cs_freight_unit-tspid = get_carrier_name( iv_tspid = cs_freight_unit-tspid ).

    /scmtms/cl_tor_helper_root=>det_transient_root_fields(
      EXPORTING
        it_key               = VALUE #( ( key = <ls_root>-node_id ) )
        iv_get_stop_infos    = abap_true
        iv_get_mainitem_info = abap_true
        iv_before_image      = lv_before_image
      IMPORTING
        et_tor_add_info      = DATA(lt_tor_add_info) ).
    ASSIGN lt_tor_add_info[ 1 ] TO FIELD-SYMBOL(<ls_tor_additional_info>).
    IF sy-subrc = 0.
      cs_freight_unit-pln_grs_duration = <ls_tor_additional_info>-tot_duration.
    ENDIF.

    cs_freight_unit-total_duration_net = <ls_root>-total_duration_net.
    cs_freight_unit-total_distance_km  = <ls_root>-total_distance_km.
    cs_freight_unit-shipping_type      = <ls_root>-shipping_type.
    IF <ls_root>-trmodcod = lif_sst_constants=>cs_trmodcod-air.
      cs_freight_unit-trmodcod = lif_sst_constants=>cs_trmodcod-inland_waterway.
    ELSE.
      cs_freight_unit-trmodcod = <ls_root>-trmodcod.
    ENDIF.
  ENDMETHOD.

  METHOD get_data_from_item.
    DATA:
      lv_item_id    TYPE /scmtms/item_id,
      lv_product_id TYPE /scmtms/product_id.

    FIELD-SYMBOLS:
      <lt_tor_item> TYPE /scmtms/t_em_bo_tor_item,
      <ls_tor_root> TYPE /scmtms/s_em_bo_tor_root.

    ASSIGN ir_data->* TO <ls_tor_root>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    DATA(lr_item) = mo_ef_parameters->get_appl_table(
                        SWITCH #( iv_old_data WHEN abap_true THEN lif_sst_constants=>cs_tabledef-fo_item_old
                                              ELSE lif_sst_constants=>cs_tabledef-fo_item_new ) ).
    ASSIGN lr_item->* TO <lt_tor_item>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO lv_dummy.
      lcl_tools=>throw_exception( ).
    ENDIF.

    ASSIGN <lt_tor_item>[ item_cat       = /scmtms/if_tor_const=>sc_tor_item_category-fu_root
                          parent_node_id = <ls_tor_root>-node_id ] TO FIELD-SYMBOL(<ls_fu_item>).
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO lv_dummy.
      lcl_tools=>throw_exception( ).
    ENDIF.

    cs_freight_unit-inc_class_code = <ls_fu_item>-inc_class_code.

    SORT <lt_tor_item> BY item_id.

    LOOP AT <lt_tor_item> ASSIGNING FIELD-SYMBOL(<ls_tor_item>) USING KEY parent_node_track_rel
      WHERE parent_node_id = <ls_tor_root>-node_id AND
            item_cat = /scmtms/if_tor_const=>sc_tor_item_category-product.

      CALL FUNCTION 'CONVERSION_EXIT_ALPHA_OUTPUT'
        EXPORTING
          input  = <ls_tor_item>-item_id
        IMPORTING
          output = lv_item_id.
      APPEND lv_item_id TO cs_freight_unit-item_id.

      IF <ls_tor_item>-base_btd_tco = cs_base_btd_tco_inb_dlv OR
         <ls_tor_item>-base_btd_tco = cs_base_btd_tco_outb_dlv.
        DATA(lv_base_btd_id) = <ls_tor_item>-base_btd_id.
        SHIFT  lv_base_btd_id LEFT DELETING LEADING '0'.
        APPEND lv_base_btd_id TO cs_freight_unit-erp_dlv_id.
      ELSE.
        APPEND '' TO cs_freight_unit-erp_dlv_id.
      ENDIF.

      IF  <ls_tor_item>-base_btditem_tco = cs_base_btd_tco_delivery_item.
        DATA(lv_base_btditem_id) = <ls_tor_item>-base_btditem_id.
        SHIFT  lv_base_btditem_id LEFT DELETING LEADING '0'.
        APPEND lv_base_btditem_id TO cs_freight_unit-erp_dlv_item_id.
      ELSE.
        APPEND '' TO cs_freight_unit-erp_dlv_item_id.
      ENDIF.

      IF ( <ls_tor_item>-base_btd_tco = cs_base_btd_tco_inb_dlv OR
           <ls_tor_item>-base_btd_tco = cs_base_btd_tco_outb_dlv ) AND
          <ls_tor_item>-base_btditem_tco = cs_base_btd_tco_delivery_item.
        DATA(lv_base_btd_alt_item_id) = '00' && lv_base_btd_id && <ls_tor_item>-base_btditem_id+4(6).
        APPEND lv_base_btd_alt_item_id TO cs_freight_unit-dlv_item_alt_id.
      ELSE.
        APPEND '' TO cs_freight_unit-dlv_item_alt_id.
      ENDIF.
      APPEND <ls_tor_item>-qua_pcs_val TO cs_freight_unit-itm_qua_pcs_val.
      APPEND <ls_tor_item>-qua_pcs_uni TO cs_freight_unit-itm_qua_pcs_uni.
      APPEND <ls_tor_item>-item_descr  TO cs_freight_unit-product_txt.

      CALL FUNCTION 'CONVERSION_EXIT_MATN1_OUTPUT'
        EXPORTING
          input  = <ls_tor_item>-product_id
        IMPORTING
          output = lv_product_id.
      APPEND lv_product_id TO cs_freight_unit-product_id.

    ENDLOOP.

  ENDMETHOD.

  METHOD get_maintabref.
    " FU
    FIELD-SYMBOLS <lt_maintabref> TYPE ANY TABLE.

    ASSIGN is_app_object-maintabref->* TO FIELD-SYMBOL(<ls_maintabref>).

    IF <ls_maintabref> IS ASSIGNED AND lcl_tools=>is_table( iv_value = <ls_maintabref> ) = abap_true.
      ASSIGN <ls_maintabref> TO <lt_maintabref>.
      LOOP AT <lt_maintabref> ASSIGNING FIELD-SYMBOL(<ls_line>).
        ASSIGN COMPONENT /scmtms/if_tor_c=>sc_node_attribute-root-tor_cat
          OF STRUCTURE <ls_line> TO FIELD-SYMBOL(<lv_tor_cat>).
        IF sy-subrc = 0 AND <lv_tor_cat> = /scmtms/if_tor_const=>sc_tor_category-freight_unit.
          GET REFERENCE OF <ls_line> INTO rr_maintabref.
          EXIT.
        ENDIF.
      ENDLOOP.
    ELSEIF <ls_maintabref> IS ASSIGNED.
      GET REFERENCE OF <ls_maintabref> INTO rr_maintabref.
    ENDIF.
  ENDMETHOD.

  METHOD lif_bo_reader~check_relevance.
    " FU relevance function
    FIELD-SYMBOLS <ls_root> TYPE /scmtms/s_em_bo_tor_root.

    rv_result = lif_ef_constants=>cs_condition-false.
    ASSIGN is_app_object-maintabref->* TO <ls_root>.
    IF sy-subrc <> 0.
      RETURN.
    ENDIF.

    IF get_customizing_aot( <ls_root>-tor_type ) <> is_app_object-appobjtype.
      RETURN.
    ENDIF.

    IF is_app_object-maintabdef = lif_sst_constants=>cs_tabledef-fo_header_new AND
      ( <ls_root>-track_exec_rel = lif_sst_constants=>cs_track_exec_rel-execution OR
        <ls_root>-track_exec_rel = lif_sst_constants=>cs_track_exec_rel-exec_with_extern_event_mngr ).

      CASE is_app_object-update_indicator.
        WHEN lif_ef_constants=>cs_change_mode-insert.
          rv_result = lif_ef_constants=>cs_condition-true.
        WHEN lif_ef_constants=>cs_change_mode-update OR
             lif_ef_constants=>cs_change_mode-undefined.
          rv_result = lcl_tools=>are_structures_different(
                          ir_data1  = lif_bo_reader~get_data( is_app_object = is_app_object )
                          ir_data2  = lif_bo_reader~get_data(
                                          is_app_object = is_app_object
                                          iv_old_data   = abap_true ) ).
          IF rv_result = lif_ef_constants=>cs_condition-false.
            rv_result = check_non_idoc_fields( is_app_object ).
          ENDIF.
      ENDCASE.
    ENDIF.

  ENDMETHOD.

  METHOD lif_bo_reader~get_track_id_data.

    FIELD-SYMBOLS <ls_root> TYPE /scmtms/s_em_bo_tor_root.

    CLEAR: et_track_id_data.

    ASSIGN is_app_object-maintabref->* TO <ls_root>.
    IF sy-subrc <> 0.
      MESSAGE e010(zsst_gtt) INTO DATA(lv_dummy).
      lcl_tools=>throw_exception( ).
    ENDIF.

    add_track_id_data(
      EXPORTING
        is_app_object = is_app_object
        iv_trxcod     = lif_sst_constants=>cs_trxcod-fu_number
        iv_trxid      = |{ <ls_root>-tor_id }|
      CHANGING
        ct_track_id   = et_track_id_data ).

  ENDMETHOD.

ENDCLASS.