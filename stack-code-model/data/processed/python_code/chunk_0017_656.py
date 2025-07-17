class ZCL_PROXY_INPUT_PO definition
  public
  inheriting from ZCL_PROXY_INPUT
  final
  create public .

public section.
*"* public components of class ZCL_PROXY_INPUT_PO
*"* do not include other source files here!!!
protected section.
*"* protected components of class ZCL_PROXY_INPUT_PO
*"* do not include other source files here!!!

  methods CALL_PO_BAPI
    returning
      value(RT_RETURN) type BAPIRET2_T .

  methods PROCESS_MSG_DATA
    redefinition .
  methods VALIDATION_CHECK
    redefinition .
private section.
*"* private components of class ZCL_PROXY_INPUT_PO
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCL_PROXY_INPUT_PO IMPLEMENTATION.


METHOD call_po_bapi.

*  DATA:
*    ls_post_mapping_data  TYPE zesymt_purchase_order,
*    ls_poheader           TYPE bapimepoheader,
*    ls_poheaderx          TYPE bapimepoheaderx,
*    lt_poitem             TYPE STANDARD TABLE OF bapimepoitem,
*    lt_poitemx            TYPE STANDARD TABLE OF bapimepoitemx,
*    ls_poitem             LIKE LINE OF lt_poitem,
*    ls_poitemx            LIKE LINE OF lt_poitemx,
*    ls_item               LIKE LINE OF ls_post_mapping_data-mt_purchase_order-document-items.
*
*  me->get_msg_data( IMPORTING es_msg_data = ls_post_mapping_data ).
*
*  ls_poheader-comp_code = ls_post_mapping_data-mt_purchase_order-document-header-company_code.
*  ls_poheader-doc_type  = ls_post_mapping_data-mt_purchase_order-document-header-document_type.
*  ls_poheader-vendor    = ls_post_mapping_data-mt_purchase_order-document-header-vendor.
*  ls_poheader-purch_org = ls_post_mapping_data-mt_purchase_order-document-header-purch_org.
*  ls_poheader-pur_group = ls_post_mapping_data-mt_purchase_order-document-header-purch_group.
*  ls_poheader-ref_1     = ls_post_mapping_data-mt_purchase_order-document-header-your_reference.
*
*  ls_poheaderx-comp_code = 'X'.
*  ls_poheaderx-doc_type  = 'X'.
*  ls_poheaderx-vendor    = 'X'.
*  ls_poheaderx-purch_org = 'X'.
*  ls_poheaderx-pur_group = 'X'.
*  ls_poheaderx-ref_1     = 'X'.
*
*  LOOP AT ls_post_mapping_data-mt_purchase_order-document-items INTO ls_item.
*    ls_poitem-po_item   = ls_item-item_no.
*    ls_poitem-material  = ls_item-material.
*    ls_poitem-plant     = ls_item-plant.
*    ls_poitem-stge_loc  = ls_item-storage_location.
*    ls_poitem-quantity  = ls_item-quantity.
*    APPEND ls_poitem TO lt_poitem.
*
*    ls_poitemx-po_item   = ls_item-item_no.
*    ls_poitemx-material  = 'X'.
*    ls_poitemx-plant     = 'X'.
*    ls_poitemx-stge_loc  = 'X'.
*    ls_poitemx-quantity  = 'X'.
*    APPEND ls_poitemx TO lt_poitemx.
*  ENDLOOP.
*
*  CALL FUNCTION 'BAPI_PO_CREATE1'
*    EXPORTING
*      poheader  = ls_poheader
*      poheaderx = ls_poheaderx
*    TABLES
*      return    = rt_return
*      poitem    = lt_poitem
*      poitemx   = lt_poitemx.

ENDMETHOD.


METHOD process_msg_data.

*  DATA:
*    lt_return             LIKE me->t_bapiret2,
*    ls_post_mapping_data  TYPE zesymt_purchase_order.
*
*  me->get_msg_data( IMPORTING es_msg_data = ls_post_mapping_data ).
*
*  lt_return = me->call_po_bapi( ).
*
*  LOOP AT lt_return TRANSPORTING NO FIELDS WHERE type = 'A' OR type = 'E'.
*    EXIT.
*  ENDLOOP.
*  IF sy-subrc = 0.
*    me->t_bapiret2 = lt_return.
*    RAISE EXCEPTION TYPE zcx_proxy_process_error
*      EXPORTING
*        error_cat   = 'PRE'             "Processing Error
*        objtype     = 'BUS2012'         "Purchase Order
*        objkey      = ls_post_mapping_data-mt_purchase_order-document-header-your_reference
*        pre_mapping = 'X'.              "Force repeat to go through mapping and validation again
*  ENDIF.

ENDMETHOD.


METHOD validation_check.

*  DATA:
*    ls_pre_mapping_data  TYPE zesymt_purchase_order.
*
*  me->get_msg_data( EXPORTING iv_premapping = 'X'
*                    IMPORTING es_msg_data   = ls_pre_mapping_data ).
*
*  IF ls_pre_mapping_data-mt_purchase_order-document-header-your_reference NS 'YES'.
*    me->add_message( iv_msgty = 'E'
*                     iv_msgid = 'AD'
*                     iv_msgno = '010'
*                     iv_msgv1 = 'Invalid Reference'
*                     iv_msgv2 = ls_pre_mapping_data-mt_purchase_order-document-header-your_reference ).
*
*    RAISE EXCEPTION TYPE zcx_proxy_process_error
*      EXPORTING
*        error_cat   = 'DCE'             "Determination & Conversion
*        objtype     = 'BUS2012'         "Purchase Order
*        objkey      = ls_pre_mapping_data-mt_purchase_order-document-header-your_reference
*        pre_mapping = 'X'.
*  ENDIF.

ENDMETHOD.
ENDCLASS.