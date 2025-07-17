class ZCL_PLANEJAMENTO_CCUSTO definition
  public
  final
  create public .

public section.

  constants GC_PLPROF type RKPP6-PLPROF value 'ZPROFILE' ##NO_TEXT.
  constants GC_KOKRS type COBK-KOKRS value 'CSBR' ##NO_TEXT.
  constants GC_VRGNG type COBK-VRGNG value 'RKP1' ##NO_TEXT.
  constants GC_PERAB type COBK-PERAB value '001' ##NO_TEXT.
  constants GC_PERBI type COBK-PERBI value '012' ##NO_TEXT.
  constants GC_LEDNR type RKU01JA-LEDNR value '0' ##NO_TEXT.
  constants GC_WAERS type RKU01JA-TWAER value 'BRL' ##NO_TEXT.

  methods CONSTRUCTOR
    importing
      !I_HEADER type ZDT_DOCUMENT_POST_HEADER
      !I_ITENS type ZDT_DOCUMENT_POST_ITENS_TAB .
  methods CALL_KP04 .
  methods SET_KP06 .
  methods CALL_KP06 .
protected section.
private section.

  data GS_HEADER type ZDT_DOCUMENT_POST_HEADER .
  data GT_ITENS type ZDT_DOCUMENT_POST_ITENS_TAB .
  data GO_SHDB type ref to ZCL_SHDB .
ENDCLASS.



CLASS ZCL_PLANEJAMENTO_CCUSTO IMPLEMENTATION.


  METHOD call_kp04.
*--------------------------------------------------------------------*
* Executes transaction KP04 to load the profile created for the process.
* This point is not necessary if the profile is already parameterized correctly by user.
*--------------------------------------------------------------------*

    DATA: lv_mode   TYPE c VALUE 'N',
          lv_update TYPE c VALUE 'S'.

    go_shdb->reset( ).
    go_shdb->set_dynpro( i_program = 'SAPLKPP6' i_dynpro  = '1007' ).
    go_shdb->set_field( i_fnam = 'BDC_CURSOR'   i_fval = 'RKPP6-PLPROF' ).
    go_shdb->set_field( i_fnam = 'BDC_OKCODE'   i_fval = '=CWEI' ).
    go_shdb->set_field( i_fnam = 'RKPP6-PLPROF' i_fval = CONV string( gc_plprof ) ).

    go_shdb->call_transaction(
      EXPORTING
        i_tcode  = 'KP04'              " Código de transação
        i_mode   = lv_mode             " Modo
        i_update = lv_update           " Atualização
      IMPORTING
        e_msg    = DATA(lt_error_msg)  " Tabela de mensagens na transação
    ).

  ENDMETHOD.


  METHOD call_kp06.

    DATA: lv_mode      TYPE c VALUE 'N',
          lv_update    TYPE c VALUE 'S',
          lv_month     TYPE i,
          lv_month_str TYPE char02,
          lv_fnam      TYPE string.

    go_shdb->reset( ).

* KP06 - Header
    go_shdb->set_dynpro( i_program = 'SAPLKPP0'    i_dynpro  = '1000' ).
    go_shdb->set_field( i_fnam = 'BDC_CURSOR'      i_fval = 'KPP1B-FORPL' ).
    go_shdb->set_field( i_fnam = 'BDC_OKCODE'      i_fval = '=CSUB' ).
    go_shdb->set_field( i_fnam = 'KPP1B-ONLY'      i_fval = '' ).
    go_shdb->set_field( i_fnam = 'KPP1B-FORPL'     i_fval = 'X' ).
    go_shdb->set_field( i_fnam = 'KPP0B-VALUE(01)' i_fval = gs_header-versao ).
    go_shdb->set_field( i_fnam = 'KPP0B-VALUE(02)' i_fval = gs_header-exercicio ).
    go_shdb->set_field( i_fnam = 'KPP0B-VALUE(03)' i_fval = gs_header-centro_custo ).
    go_shdb->set_field( i_fnam = 'KPP0B-VALUE(05)' i_fval = gs_header-classe_custo ).
    go_shdb->set_field( i_fnam = 'BDC_SUBSCR'      i_fval = 'SAPLKPP0                                1100APPLIKAT' ).

* KP06 - Periods
    go_shdb->set_dynpro( i_program = 'SAPLKPP2'    i_dynpro  = '0106' ).
    go_shdb->set_field( i_fnam = 'BDC_CURSOR'      i_fval = 'Z-BDC04(01)' ).
    go_shdb->set_field( i_fnam = 'BDC_OKCODE'      i_fval = '/00' ).

    LOOP AT gt_itens ASSIGNING FIELD-SYMBOL(<item>).
      lv_month = <item>-mes + 2.
      UNPACK lv_month TO lv_month_str.
      lv_fnam = 'Z-BDC' && lv_month_str && '(01)'.
      TRANSLATE <item>-montantes USING '.,'.
      go_shdb->set_field( i_fnam = lv_fnam  i_fval = <item>-montantes ).
    ENDLOOP.

* KP06 - Save
    go_shdb->set_dynpro( i_program = 'SAPLKPP2'    i_dynpro  = '0106' ).
    go_shdb->set_field( i_fnam = 'BDC_CURSOR'      i_fval = 'Z-BDC04(01)' ).
    go_shdb->set_field( i_fnam = 'BDC_OKCODE'      i_fval = '=CBUC' ).

    go_shdb->call_transaction(
      EXPORTING
        i_tcode  = 'KP06'              " Código de transação
        i_mode   = lv_mode             " Modo
        i_update = lv_update           " Atualização
      IMPORTING
        e_msg    = DATA(lt_error_msg)  " Tabela de mensagens na transação
    ).

  ENDMETHOD.


  method CONSTRUCTOR.

   gs_header = i_header.
   gt_itens  = i_itens.

   CREATE OBJECT go_shdb.

* load profile
   me->call_kp04( ).

  endmethod.


  METHOD set_kp06.

    DATA: lv_gjahr      TYPE cobk-gjahr,
          lv_kokrs      TYPE cobk-kokrs,
          lv_perab      TYPE cobk-perab,
          lv_perbi      TYPE cobk-perbi,
          lv_updval     TYPE flag,
          lv_versn      TYPE cobk-versn,
          lv_vrgng      TYPE cobk-vrgng,
          lv_irku01_cur TYPE rku01_cur,
          lv_mes        TYPE char03,
          lt_irku01ja   TYPE TABLE OF rku01ja.

* KP06 - Header
    lv_gjahr  = gs_header-exercicio.
    lv_kokrs  = gc_kokrs.
    lv_perab  = gc_perab.
    lv_perbi  = gc_perbi.
    lv_updval = abap_true.
    lv_versn  = gs_header-versao.
    lv_vrgng  = gc_vrgng.
    lv_irku01_cur-wtg_man = abap_true.

* KP06 - Periods
    APPEND INITIAL LINE TO lt_irku01ja ASSIGNING FIELD-SYMBOL(<irku01ja>).
    <irku01ja>-vrgng = gc_vrgng.
    <irku01ja>-lednr = gc_lednr.
    <irku01ja>-kokrs = gc_kokrs.
    <irku01ja>-kostl = gs_header-centro_custo.
    <irku01ja>-gjahr = gs_header-exercicio.
    <irku01ja>-perab = gc_perab.
    <irku01ja>-perbi = gc_perbi.
    <irku01ja>-versn = gs_header-versao.
    <irku01ja>-kstar = gs_header-classe_custo.
    <irku01ja>-twaer = gc_waers.

    LOOP AT gt_itens ASSIGNING FIELD-SYMBOL(<item>).

      UNPACK <item>-mes TO lv_mes.
      DATA(lv_fieldname) = 'WTG' && lv_mes.
      ASSIGN COMPONENT lv_fieldname OF STRUCTURE <irku01ja> TO FIELD-SYMBOL(<fieldvalue>).
      <fieldvalue> = <item>-montantes.

    ENDLOOP.

    CALL FUNCTION 'K_COSTS_PLAN_INTERFACE_PERIOD'
      EXPORTING
        gjahr            = lv_gjahr
        kokrs            = lv_kokrs
        perab            = lv_perab
        perbi            = lv_perbi
        update_values    = lv_updval
        versn            = lv_versn
        vrgng            = lv_vrgng
        irku01_cur       = lv_irku01_cur
      TABLES
        irku01ja         = lt_irku01ja
      EXCEPTIONS
        messages_occured = 1
        OTHERS           = 2.
    IF sy-subrc <> 0.

* Try using SHDB
      me->call_kp06( ).

    ENDIF.

  ENDMETHOD.
ENDCLASS.