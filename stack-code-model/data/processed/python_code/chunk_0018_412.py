class ZCL_BC_BDC definition
  public
  final
  create private .

public section.
*"* public components of class ZCL_BC_BDC
*"* do not include other source files here!!!

  constants CO_MSG_TYPE_INFO type C value 'I'. "#EC NOTEXT
  constants CO_MSG_TYPE_SUCCESS type C value 'S'. "#EC NOTEXT
  constants CO_MSG_TYPE_ERROR type C value 'E'. "#EC NOTEXT
  constants CO_MSG_TYPE_WARNING type C value 'W'. "#EC NOTEXT
  constants CO_MSG_TYPE_ABEND type C value 'A'. "#EC NOTEXT

  class-methods S_INSTANTIATE
    importing
      !IM_BDC_TYPE type C
      !IM_TCODE type TCODE
      !IM_BDC_MODE type C default 'N'
      !IM_UPD_MODE type C default 'S'
      !IM_GROUP type APQI-GROUPID optional
      !IM_USER type APQI-USERID default SY-UNAME
      !IM_KEEP type APQI-QERASE optional
      !IM_HOLDDATE type APQI-STARTDATE optional
    returning
      value(RE_BDC) type ref to ZCL_BC_BDC .
  class-methods S_FREE_INSTANCE .
  methods ADD_FIELD
    importing
      !IM_FLD type ANY
      !IM_VAL type ANY
      !IM_CONV type CHAR1 optional .
  methods ADD_SCREEN
    importing
      !IM_REPID type ANY
      !IM_DYNNR type ANY .
  methods PROCESS
    exporting
      !EX_SUBRC type SY-SUBRC
      !EX_MESSAGES type TAB_BDCMSGCOLL
    raising
      ZCX_BATCH_INPUT_ERROR .
  methods CLEAR_BDC_DATA .
*"* protected components of class ZCL_BC_BDC
*"* do not include other source files here!!!
protected section.
*"* protected components of class ZCL_BC_BDC
*"* do not include other source files here!!!
private section.
*"* private components of class ZCL_BC_BDC
*"* do not include other source files here!!!

  class-data BDC type ref to ZCL_BC_BDC .
  data BDCDATA type BDCDATA_TAB .
  data BDC_TYPE type CHAR2 .
  data TCODE type TCODE .
  data CT_BDC_MODE type C .
  data CT_UPD_MODE type C .
  data BI_GROUP type APQI-GROUPID .
  data BI_USER type APQI-USERID .
  data BI_KEEP type APQI-QERASE .
  data BI_HOLDDATE type APQI-STARTDATE .

  methods CONSTRUCTOR
    importing
      !IM_BDC_TYPE type C
      !IM_TCODE type TCODE
      !IM_BDC_MODE type C
      !IM_UPD_MODE type C
      !IM_GROUP type APQI-GROUPID
      !IM_USER type APQI-USERID
      !IM_KEEP type APQI-QERASE
      !IM_HOLDDATE type APQI-STARTDATE .
  methods CALL_TRANSACTION
    exporting
      !EX_SUBRC type SY-SUBRC
      !EX_MESSAGES type TAB_BDCMSGCOLL .
  methods CREATE_BATCH_INPUT_SESS
    raising
      ZCX_BATCH_INPUT_ERROR .
ENDCLASS.



CLASS ZCL_BC_BDC IMPLEMENTATION.


METHOD add_field.
*----------------------------------------------------------------------*
*       Insert field in BDC screen
*
* Additional functionality if IV_CONV is populated as below:-
*  D - Convert date from YYYYMMDD format to output format
*  S - Allow initial values to be populated in BDC
*----------------------------------------------------------------------*
  DATA:
    bdcdata LIKE LINE OF me->bdcdata.

* Initial values are skipped unless suppress 'S' is used
  IF im_val IS INITIAL AND im_conv <> 'S'.
    RETURN.
  ENDIF.

  CASE im_conv.
    WHEN 'D'.
      CALL FUNCTION 'CONVERSION_EXIT_MODAT_OUTPUT'
        EXPORTING
          input  = im_val
        IMPORTING
          output = bdcdata-fval.

    WHEN OTHERS.
      bdcdata-fval = im_val.

  ENDCASE.

  bdcdata-fnam = im_fld.
  APPEND bdcdata TO me->bdcdata.

ENDMETHOD.


method ADD_SCREEN.
*----------------------------------------------------------------------*
*       Start new BDC screen
*----------------------------------------------------------------------*
  DATA:
    bdcdata LIKE LINE OF me->bdcdata.

  bdcdata-program  = im_repid.
  bdcdata-dynpro   = im_dynnr.
  bdcdata-dynbegin = 'X'.
  APPEND bdcdata TO me->bdcdata.

endmethod.


METHOD CALL_TRANSACTION.
  DATA:
    bdc_subrc LIKE sy-subrc.

  CLEAR: ex_subrc, ex_messages.

*-----------------------------------------------------------------------
* Call BDC
*-----------------------------------------------------------------------
* Call the transaction and collect the messages
  CALL TRANSACTION me->tcode
                   USING  me->bdcdata
                   MODE   me->ct_bdc_mode
                   UPDATE me->ct_upd_mode
                   MESSAGES INTO ex_messages.

  bdc_subrc = sy-subrc.

*-----------------------------------------------------------------------
* Process BDC messages
*-----------------------------------------------------------------------

* Check if there are any errors
  LOOP AT ex_messages TRANSPORTING NO FIELDS
                     WHERE msgtyp = co_msg_type_error
                     OR    msgtyp = co_msg_type_abend.
    EXIT. "Exit loop
  ENDLOOP.

  IF sy-subrc = 0 OR bdc_subrc <> 0.
    ex_subrc = 4.
  ENDIF.

ENDMETHOD.


METHOD CLEAR_BDC_DATA.

  CLEAR: me->bdcdata.

ENDMETHOD.


METHOD constructor.

  me->bdc_type    = im_bdc_type.
  me->tcode       = im_tcode.
  me->ct_bdc_mode = im_bdc_mode.
  me->ct_upd_mode = im_upd_mode.
  me->bi_group    = im_group.
  me->bi_user     = im_user.
  me->bi_keep     = im_keep.
  me->bi_holddate = im_holddate.

ENDMETHOD.


METHOD create_batch_input_sess.

  CALL FUNCTION 'BDC_OPEN_GROUP'
    EXPORTING
      group               = me->bi_group
      holddate            = me->bi_holddate
      keep                = me->bi_keep
      user                = me->bi_user
    EXCEPTIONS
      client_invalid      = 1
      destination_invalid = 2
      group_invalid       = 3
      group_is_locked     = 4
      holddate_invalid    = 5
      internal_error      = 6
      queue_error         = 7
      running             = 8
      system_lock_error   = 9
      user_invalid        = 10
      OTHERS              = 11.
  IF sy-subrc <> 0.
    RAISE EXCEPTION TYPE zcx_batch_input_error
      EXPORTING
        msgty = sy-msgty
        msgid = sy-msgid
        msgno = sy-msgno
        msgv1 = sy-msgv1
        msgv2 = sy-msgv2
        msgv3 = sy-msgv3
        msgv4 = sy-msgv4.
  ENDIF.

  CALL FUNCTION 'BDC_INSERT'
    EXPORTING
      tcode            = me->tcode
    TABLES
      dynprotab        = me->bdcdata
    EXCEPTIONS
      internal_error   = 1
      not_open         = 2
      queue_error      = 3
      tcode_invalid    = 4
      printing_invalid = 5
      posting_invalid  = 6
      OTHERS           = 7.
  IF sy-subrc <> 0.
    RAISE EXCEPTION TYPE zcx_batch_input_error
      EXPORTING
        msgty = sy-msgty
        msgid = sy-msgid
        msgno = sy-msgno
        msgv1 = sy-msgv1
        msgv2 = sy-msgv2
        msgv3 = sy-msgv3
        msgv4 = sy-msgv4.
  ENDIF.

  CALL FUNCTION 'BDC_CLOSE_GROUP'
    EXCEPTIONS
      not_open    = 1
      queue_error = 2
      OTHERS      = 3.
  IF sy-subrc <> 0.
    RAISE EXCEPTION TYPE zcx_batch_input_error
      EXPORTING
        msgty = sy-msgty
        msgid = sy-msgid
        msgno = sy-msgno
        msgv1 = sy-msgv1
        msgv2 = sy-msgv2
        msgv3 = sy-msgv3
        msgv4 = sy-msgv4.
  ENDIF.

ENDMETHOD.


METHOD process.

  CLEAR: ex_subrc, ex_messages.

  CASE me->bdc_type.
    WHEN 'CT'.
      me->call_transaction( IMPORTING ex_subrc    = ex_subrc
                                      ex_messages = ex_messages ).
    WHEN 'BI'.
      me->create_batch_input_sess( ).
  ENDCASE.

ENDMETHOD.


METHOD s_free_instance.

  FREE zcl_bc_bdc=>bdc.

ENDMETHOD.


METHOD s_instantiate.

* Create singleton so that in any single session, only
* one instance of class exists
  IF zcl_bc_bdc=>bdc IS NOT BOUND.
    ASSERT FIELDS im_tcode CONDITION im_tcode IS NOT INITIAL.

    ASSERT FIELDS im_bdc_type CONDITION im_bdc_type = 'CT' OR im_bdc_type = 'BI'.

    CREATE OBJECT zcl_bc_bdc=>bdc
      EXPORTING
        im_bdc_type = im_bdc_type
        im_tcode    = im_tcode
        im_bdc_mode = im_bdc_mode
        im_upd_mode = im_upd_mode
        im_group    = im_group
        im_user     = im_user
        im_keep     = im_keep
        im_holddate = im_holddate.
  ENDIF.
  re_bdc = zcl_bc_bdc=>bdc.

ENDMETHOD.
ENDCLASS.