report zcreatequotations.



class lcl_app definition.
  public section.

    class-data: r_eban   type ref to eban.


    types:  begin of ty_alv,
              iconv  type icon_d,
              matnr type mara-matnr,
              mtart type mara-mtart,
              matkl type mara-matkl,
              matkx type makt-maktx,
              vpsta type mara-vpsta,
            end of ty_alv.

    types:  begin of ty_item,
              banfn type eban-banfn,
              bnfpo type eban-bnfpo,
              knttp type eban-knttp,
              ekgrp type eban-ekgrp,
              matnr type eban-matnr,
              txz01 type eban-txz01,
              menge type eban-menge,
              meins type eban-meins,
              ekorg type eban-ekorg,
              werks type eban-werks,
              lgort type eban-lgort,


            end of ty_item.


    types: begin of ty_vendor,
             iconv   type icon_d,
             lifnr  type lfa1-lifnr,
             name1  type lfa1-name1,
             ebeln  type ekko-ebeln,
             submi  type ekko-submi,
             amount type ekpo-brtwr,
             ekorg  type lfm1-ekorg,
             regio  type lfa1-regio,
             stcd1  type lfa1-stcd1,
             waers  type lfm1-waers,
             zterm  type lfm1-zterm,
             inco1  type lfm1-inco1,
             inco2  type lfm1-inco2,
             verkf  type lfm1-verkf,
             telf1  type lfm1-telf1,



           end of ty_vendor.

    types: begin of ty_rfq,
             submi   type ekko-submi,
             lifnr   type ekko-lifnr,
             waers   type ekko-waers,
             aedat   type ekko-aedat,
             agdat   type ekpo-agdat,
             zterm   type ekko-zterm,
             inco1   type ekko-inco1,
             inco2   type ekko-inco2,
             ekgrp   type ekko-ekgrp,
             verkf   type ekko-verkf,
             telf1   type ekko-telf1,
             name1   type lfa1-name1,
             stcd1   type lfa1-stcd1,
             regio   type lfa1-regio,
             ebeln   type ekpo-ebeln,
             ebelp   type ekpo-ebelp,
             loekz   type ekpo-loekz,
             statu   type ekpo-statu,
             txz01   type ekpo-txz01,
             matnr   type ekpo-matnr,
             werks   type ekpo-werks,
             lgort   type ekpo-lgort,
             matkl   type ekpo-matkl,
             meins   type ekpo-meins,
             menge   type ekpo-ktmng,
             brtwr   type ekpo-brtwr,
             netwr   type ekpo-netwr,
             mwskz   type ekpo-mwskz,
             vlrcomp type ekpo-brtwr, "valor para comparação
             icon    type icon_d,
             perc    type p length 3 decimals 2,
             abskz   type ekpo-abskz,
             agmem   type ekpo-agmem,
             banfn   type ekpo-banfn,
             bnfpo   type ekpo-bnfpo,

           end of ty_rfq.

    types: begin of ty_quotation,
             submi   type ekko-submi,
             lifnr   type ekko-lifnr,
             name1   type lfa1-name1,
             aedat   type ekko-aedat,
             agdat   type ekpo-agdat,
             ebeln   type ekko-ebeln,
             ebelp   type ekpo-ebelp,
             statu   type ekpo-statu,
             matnr   type ekpo-matnr,
             txz01   type ekpo-txz01,
             werks   type ekpo-werks,
             lgort   type ekpo-lgort,
             menge   type ekpo-menge,
             meins   type ekpo-meins,
             netpr   type ekpo-netpr,
             brtwr   type ekpo-brtwr,
             vlrcomp type ekpo-brtwr, "valor para comparação
             icon    type icon_d,
             perc    type p length 3 decimals 2,
             abskz   type ekpo-abskz,
             agmem   type ekpo-agmem,
             mwskz   type ekpo-mwskz,
             banfn   type ekpo-banfn,
             bnfpo   type ekpo-bnfpo,

           end of ty_quotation.





    types: ty_sval type table of sval.


    data:  i_werks  type  werks_d,
           i_submi  type ekko-submi,
           i_ekgrp  type eban-ekgrp,
           rg_banfn type range of eban-banfn.

    data: r_docking    type ref to cl_gui_docking_container,

          r_customcontainer type ref to cl_gui_custom_container,
          r_splitter   type ref to cl_gui_splitter_container,
          r_splittera  type ref to cl_gui_splitter_container,

          " r_splitter1  type ref to cl_gui_easy_splitter_container,
          " r_splitter2  type ref to cl_gui_easy_splitter_container,

          r_container0 type ref to cl_gui_container,
          r_container1 type ref to cl_gui_container,
          r_container2 type ref to cl_gui_container,
          r_container3 type ref to cl_gui_container.
    "r_container4 type ref to cl_gui_container.



    data: "gt_mara         type table of mara,
      "gt_makt         type table of makt,
      "gt_alv          type table of ty_alv,
      gt_item           type table of ty_item,
      gt_vendor         type table of ty_vendor,
      gt_quotation      type table of ty_quotation,
      gt_rfq            type table of ty_rfq,
      gt_msgerror       type table of bdcmsgcoll,
      r_alv_item        type ref to cl_salv_table,
      r_item_selections type ref to cl_salv_selections,
      r_alv_vendor      type ref to cl_salv_table,
      r_alv_quotation   type ref to cl_salv_table,

      lv_teste          type char0010.

    class-methods check_werks.
    class-methods check_banf.
    class-methods check_rfp.
    class-methods check_fields.

    methods constructor.

    methods start.

    methods pbo importing i_dynnr    type sy-dynnr
                          i_title    type c optional
                          i_pfstatus type c optional.

    methods pai importing i_dynnr type sy-dynnr
                          i_ucomm type sy-ucomm.

    methods get_numrfp.

    methods get_data.

    methods process_data.

    methods show_alv_item.

    methods show_alv_vendor.

    methods show_alv_quotation.

    methods on_user_command for event added_function of cl_salv_events importing e_salv_function.

    methods on_double_click for event double_click of cl_salv_events_table importing row column .

    methods on_link_click for event link_click of cl_salv_events_table importing row column.

    methods action importing i_action type c.

    methods get_popup importing i_title        type c
                                i_start_column type i optional
                                i_start_row    type i optional
                      changing  it_sval        type ty_sval.

    methods get_listrequisition importing it_sval type ty_sval.

    methods get_material importing it_sval type ty_sval.

    methods get_vendor importing it_sval type ty_sval.

    methods get_price_compare changing i_item type ty_rfq.

    methods remove_row importing i_object type ref to cl_salv_table .

    methods generator_quotation.

    methods create_quotation importing i_lifnr type ekko-lifnr.

    methods update_item_quotation importing i_item type ty_quotation.

    methods recuseall.
    "i_items type ty_item.

    methods get_bestquotation.

    methods get_bestprice.

    methods show_log_erros.

    methods show_map.

    methods choice_quotation.

    methods create_doc.

endclass.

class lcl_app implementation.
  method check_werks.

  endmethod.
  method check_banf.

  endmethod.
  method check_rfp.

  endmethod.
  method check_fields.

  endmethod.

  method constructor.
    "Para quando a classe é iniciada!
    lv_teste  =  'Construiu'.


  endmethod.
  method start.



    if i_werks is initial.
*      message |Informe um centro| type 'E'.
*      leave to screen 0.
    endif.

    if i_ekgrp is initial.
*      message |Informe um grupo comprador| type 'E'.
*      leave program.
    endif.

    if rg_banfn is initial.

    endif.

    if i_submi is initial.
      me->get_numrfp( ).
    endif.
    get_data( ).
    process_data( ).
    call screen 9000.

  endmethod.

  method pbo.

    if i_dynnr = '9000'.
      set pf-status '9000'.
      set titlebar i_dynnr with  i_submi.
    endif.

*    if  r_customcontainer is INITIAL.
*        r_customcontainer = new cl_gui_custom_container( container_name = 'CUSTOM').
*    endif.

    if r_docking is initial.
      try.
          r_docking = new cl_gui_docking_container( repid = sy-repid
                                                    dynnr = sy-dynnr
                                                    extension = 100

                                                    side = cl_gui_docking_container=>dock_at_top  ).
        catch cx_root.
          message |erro| type 'I'.

      endtry.
    endif.

   " r_container0 = new cl_gui_container(  container_name = '0' clsid = '0'  ).

    if r_splitter is initial.
      try.
         r_splitter = new cl_gui_splitter_container(  parent = r_docking rows = 1 columns = 2 ).
          "r_splitter = new cl_gui_splitter_container(  parent = r_customcontainer rows = 1 columns = 2 ).
        catch cx_root.
          message |erro| type 'I'.

      endtry.
    endif.


    r_splitter->get_container( exporting row = 1 column = 1 receiving container = r_container1  ).
    r_splitter->get_container( exporting row = 1 column = 2 receiving container = r_container2 ).
    "r_splitter->get_container( exporting row = 2 column = 1 receiving container = r_container3 ).



    show_alv_item( ).
    show_alv_vendor( ).
    show_alv_quotation( ).
    "  show_alv_item_quo( ).
  endmethod.

  method pai.

    me->on_user_command( exporting e_salv_function = sy-ucomm ).

  endmethod.

  method get_numrfp.
    "Utilizar numeração aleatorioa ou indicar um contatdor no SNUM. retornar o valor para i_submit
    data lc_guid type ref to cl_abap_random_packed.
    data lv_seed type i.
    data lv_guid type p.

    cl_abap_random=>seed( receiving seed = lv_seed ).

    cl_abap_random_packed=>create( exporting seed = lv_seed
                                              min = 1000000000
                                              max = 9999999999
                                   receiving  prng = lc_guid ).

    i_submi = lc_guid->get_next( ).

  endmethod.

  method get_data.

    select ekko~submi ekko~lifnr ekko~waers ekko~aedat ekko~angdt ekko~zterm ekko~inco1 ekko~inco2 ekko~ekgrp ekko~verkf ekko~telf1 lfa1~name1 lfa1~stcd1 lfa1~regio  ekpo~ebeln ekpo~ebelp ekpo~loekz ekpo~statu ekpo~txz01 ekpo~matnr
             ekpo~werks ekpo~lgort ekpo~agdat  ekpo~matkl ekpo~ktmng ekpo~meins ekpo~ktmng as menge ekpo~netpr ekpo~brtwr ekpo~netwr ekpo~mwskz ekpo~abskz ekpo~agmem ekpo~banfn ekpo~bnfpo
      from ( ekko inner join lfa1 on  lfa1~lifnr = ekko~lifnr
                  inner join ekpo      on  ekpo~ebeln = ekko~ebeln )
           into corresponding fields of table gt_rfq
           where ekko~submi eq i_submi .


    if gt_rfq is not initial.
      i_ekgrp = gt_rfq[ 1 ]-ekgrp.
      i_werks = gt_rfq[ 1 ]-werks.

      select * from m_mekke into table @data(gt_mekke) for all entries in @gt_rfq where ebeln = @gt_rfq-ebeln.
      sort gt_rfq ascending by ebeln ebelp.
      sort gt_mekke ascending by ebeln ebelp.
      loop at gt_rfq assigning field-symbol(<fs_rfq>).

        try.
            <fs_rfq>-banfn = gt_mekke[ ebeln = <fs_rfq>-ebeln ebelp = <fs_rfq>-ebelp ]-banfn.
            <fs_rfq>-bnfpo = gt_mekke[ ebeln = <fs_rfq>-ebeln ebelp = <fs_rfq>-ebelp ]-bnfpo.
          catch cx_sy_itab_line_not_found.
        endtry.

        me->get_price_compare( changing i_item = <fs_rfq> ).

      endloop.

      gt_quotation = corresponding #( gt_rfq ).
      gt_item = corresponding #( gt_quotation ).

      sort  gt_item ascending by banfn bnfpo matnr.
      delete adjacent duplicates from gt_item  comparing banfn bnfpo matnr.

      if lines( gt_vendor ) is INITIAL.
        gt_vendor = corresponding #( gt_rfq ).
        loop at gt_vendor assigning field-symbol(<fs_vendor>).
          if <fs_vendor>-ebeln is not initial.
            <fs_vendor>-iconv = icon_led_green.
          endif.
        endloop.
        delete adjacent duplicates from gt_vendor  comparing lifnr.
      else.

        loop at gt_vendor assigning <fs_vendor>.
          if <fs_vendor>-ebeln is not initial.
            <fs_vendor>-iconv = icon_led_green.
          endif.
        endloop.
      endif.
    endif.



  endmethod.

  method process_data.


    "move os campos correspondentes com parametro de filtro
*    gt_alv = corresponding #( gt_mara ).
*
*
*    loop at gt_alv assigning field-symbol(<fs_alv>).
*      try.
*          <fs_alv>-matkx = gt_makt[ matnr = <fs_alv>-matnr ]-maktx.
*          <fs_alv>-icon = icon_checked.
*        catch cx_sy_itab_line_not_found.
*          <fs_alv>-matkx = 'description not found!'.
*          <fs_alv>-icon = icon_incomplete.
*
*      endtry.
*
*
*    endloop.

  endmethod.


  method show_alv_item.
    data: r_events     type ref to cl_salv_events_table,
          r_selections type ref to cl_salv_selections,
          r_functions  type ref to cl_salv_functions,
          r_columns    type ref to cl_salv_columns_table,
          r_column     type ref to cl_salv_column_table.


    if r_alv_item is not bound.
      try.
*          Monta lista ALV de acordo com a tabela GT_CTE:
          cl_salv_table=>factory(
            exporting
              list_display   = if_salv_c_bool_sap=>false
              r_container    = r_container1

              "container_name = ''
            importing
              r_salv_table   = r_alv_item
            changing
              t_table        = gt_item ).

*          STATUS_GUI:
*           r_alv->set_screen_status(
*             pfstatus      =  'STATUS_1'
*             report        =  sy-repid
*             set_functions = r_alv->c_functions_all ).

        catch cx_salv_msg.

      endtry.
    endif.
*   Seleção das linhas:
    r_selections = r_alv_item->get_selections( ).
    r_selections->set_selection_mode( if_salv_c_selection_mode=>row_column ).

    " r_item_selections = r_alv_item->get_selections( ).
    "r_item_selections->set_selection_mode( if_salv_c_selection_mode=>row_column ).


*   Adiciona funções ao toolbar
    r_functions = r_alv_item->get_functions( ).
    r_functions->set_all( abap_true ).

    try.
        r_functions->add_function(
                      name = 'REQUISITION'
                      icon = conv string( icon_insert_multiple_lines )
                      "text = 'Requisições'
                      tooltip = 'Indicar requisições'
                      position = if_salv_c_function_position=>right_of_salv_functions ).
      catch cx_salv_existing cx_salv_wrong_call.
    endtry.

    try.
        r_functions->add_function(
                      name = 'ADDMAT'
                      icon = conv string( icon_insert_row )
                      "text = 'Adicionar material'
                      tooltip = 'Adicionar Material'
                      position = if_salv_c_function_position=>right_of_salv_functions ).
      catch cx_salv_existing cx_salv_wrong_call.
    endtry.

    try.
        r_functions->add_function(
                      name = 'DELMAT'
                      icon = conv string( icon_delete_row )
                      "text = 'Remover material'
                      tooltip = 'Remover Material'
                      position = if_salv_c_function_position=>right_of_salv_functions ).
      catch cx_salv_existing cx_salv_wrong_call.
    endtry.


    r_columns = r_alv_item->get_columns( ).
    try.
        r_column ?= r_columns->get_column('MATNR').
        r_column->set_cell_type( if_salv_c_cell_type=>hotspot ).
      catch cx_salv_not_found.
    endtry.


*   Seta eventos
    r_events = r_alv_item->get_event( ).
    set handler on_user_command for r_events.

    set handler on_link_click for r_events.


*   Exibe:
    r_alv_item->display( ).
  endmethod.

  method show_alv_vendor.
    data: r_events     type ref to cl_salv_events_table,
          r_selections type ref to cl_salv_selections,
          r_functions  type ref to cl_salv_functions,
          r_columns    type ref to cl_salv_columns_table,
          r_column     type ref to cl_salv_column_table.
    " lt_rows      type salv_t_row.

    if r_alv_vendor is not bound.
      try.
*       Monta lista ALV de acordo com a tabela GT_CTE:
          cl_salv_table=>factory(
            exporting
              list_display   = if_salv_c_bool_sap=>false
              r_container    = r_container2
              "container_name = ''
            importing
              r_salv_table   = r_alv_vendor
            changing
              t_table        = gt_vendor ).

*       STATUS_GUI:
*        r_alv->set_screen_status(
*          pfstatus      =  'STATUS_1'
*          report        =  sy-repid
*          set_functions = r_alv->c_functions_all ).

        catch cx_salv_msg.

      endtry.
    endif.
*   Seleção das linhas:
    r_selections = r_alv_vendor->get_selections( ).
    r_selections->set_selection_mode( if_salv_c_selection_mode=>row_column ).



*   Adiciona funções

*   Adiciona funções ao toolbar
    r_functions = r_alv_vendor->get_functions( ).
    r_functions->set_all( abap_true ).
    try.
        r_functions->add_function(
                      name = 'ADDVENDOR'
                      "text = 'Adicionar Fornecedor'
                      icon = conv string( icon_insert_row )
                      tooltip = 'Adicionar Fornecedor'
                      position = if_salv_c_function_position=>right_of_salv_functions ).
      catch cx_salv_existing cx_salv_wrong_call.
    endtry.

    try.
        r_functions->add_function(
                      name = 'DELVENDOR'
                      "text = 'Remove Fornecedor'
                      icon = conv string( icon_delete_row )
                      tooltip = 'Remover Fornecedor'
                      position = if_salv_c_function_position=>right_of_salv_functions ).
      catch cx_salv_existing cx_salv_wrong_call.
    endtry.

*Hotspot
    r_columns = r_alv_vendor->get_columns( ).
    try.
        r_column ?= r_columns->get_column('EBELN').
        r_column->set_cell_type( if_salv_c_cell_type=>hotspot ).
      catch cx_salv_not_found.
    endtry.



*   Seta eventos
    r_events = r_alv_vendor->get_event( ).
    set handler on_user_command for r_events.
    set handler on_link_click for r_events.


*   Exibe:
    r_alv_vendor->display( ).
  endmethod.

  method show_alv_quotation.
    data: r_events     type ref to cl_salv_events_table,
          r_functions  type ref to cl_salv_functions,
          r_selections type ref to cl_salv_selections,
          r_columns    type ref to cl_salv_columns_table,
          r_column     type ref to cl_salv_column_table.

    if r_alv_quotation is not bound.
      try.
*       Monta lista ALV de acordo com a tabela GT_CTE:
          cl_salv_table=>factory(
            exporting
              list_display   = if_salv_c_bool_sap=>false
              r_container    =  r_container3

            importing
              r_salv_table   = r_alv_quotation
            changing
              t_table        = gt_quotation ).

*       STATUS_GUI:
*        r_alv->set_screen_status(
*          pfstatus      =  'STATUS_1'
*          report        =  sy-repid
*          set_functions = r_alv->c_functions_all ).

        catch cx_salv_msg.

      endtry.
    endif.
*   Seleção das linhas:
    r_selections = r_alv_quotation->get_selections( ).
    r_selections->set_selection_mode( if_salv_c_selection_mode=>row_column ).

*   Ajuste nome da coluna
    r_columns = r_alv_quotation->get_columns( ).
    try.
        r_column ?= r_columns->get_column('VLRCOMP').
        r_column->set_long_text('Preço de comparação').
        r_column->set_medium_text('Preço de comparação').
        r_column->set_short_text('VlrComp.').

      catch cx_salv_not_found.
    endtry.

    r_columns = r_alv_quotation->get_columns( ).
    try.
        r_column ?= r_columns->get_column('PERC').
        r_column->set_long_text('Percentual').
        r_column->set_medium_text('Percentual').
        r_column->set_short_text('%').

      catch cx_salv_not_found.
    endtry.

    r_columns = r_alv_quotation->get_columns( ).
    try.
        r_column ?= r_columns->get_column('ICON').
        r_column->set_long_text('Indicador').
        r_column->set_medium_text('Indicador').
        r_column->set_short_text('Ind.').

      catch cx_salv_not_found.
    endtry.


*   Adiciona funções ao toolbar
    r_functions =  r_alv_quotation->get_functions( ).
    r_functions->set_all( abap_true ).

    try.
        r_functions->add_function(
                      name = 'RECUSE'
                      icon = conv string(  icon_incomplete )
                      text = 'Rec.fora prazo'
                      tooltip = 'Recusar cotações fora do prazo'
                      position = if_salv_c_function_position=>right_of_salv_functions ).
      catch cx_salv_existing cx_salv_wrong_call.
    endtry.

    try.
        r_functions->add_function(
                      name = 'SHOWALL'
                      icon = conv string( icon_filter_undo )
                      text = 'Todos Itens'
                      tooltip = 'Todos itens'
                      position = if_salv_c_function_position=>right_of_salv_functions ).
      catch cx_salv_existing cx_salv_wrong_call.
    endtry.

    try.
        r_functions->add_function(
                      name = 'BESTQUOTATION'
                      icon = conv string(  icon_select_with_condition )
                      text = 'Melhor Cotação'
                      tooltip = 'Melhor Cotação'
                      position = if_salv_c_function_position=>right_of_salv_functions ).
      catch cx_salv_existing cx_salv_wrong_call.
    endtry.

    try.
        r_functions->add_function(
                      name = 'BESTPRICE'
                      icon = conv string(  icon_select_with_condition )
                      text = 'Melhor Preço'
                      tooltip = 'Melhor preço'
                      position = if_salv_c_function_position=>right_of_salv_functions ).
      catch cx_salv_existing cx_salv_wrong_call.
    endtry.





*   Seta eventos
    r_events = r_alv_quotation->get_event( ).
    set handler on_user_command for r_events.
    set handler on_double_click for r_events.


*   Exibe:
    r_alv_quotation->display( ).
  endmethod.



  method on_user_command.

*   Eventos:
    case e_salv_function.

      when '&CANCEL'.
        leave program.
      when 'REQUISITION'.
        me->action( i_action = e_salv_function ).

      when 'ADDMAT'.
        me->action( i_action = e_salv_function ).
      when 'ADDVENDOR'.
        me->action( i_action = e_salv_function ).

      when 'DELVENDOR'.
        me->action( i_action = e_salv_function ).

      when 'DELMAT'.
        me->action( i_action = e_salv_function ).

      when '&MAPACOMP'.
        me->show_map( ).
      when '&CRIACOT'.
        me->generator_quotation( ).

      when '&LOGEVENT'.
        me->show_log_erros( ).

      when '&CREATDOC'.
        me->choice_quotation( ).

      when 'RECUSE'.
        "Recusa todos os itens das cotações com prazo de resposta vencido.
        me->recuseall( ).
      when 'SHOWALL'.
        me->get_data( ).
        r_alv_quotation->refresh( ).

      when 'BESTQUOTATION'.
        me->get_bestquotation( ).

      when 'BESTPRICE'.
        me->get_bestprice( ).

    endcase.

  endmethod.
  method on_double_click.


    data: row_c(4)     type c,
          ls_quotation type ty_quotation.


    data: lr_selections type ref to cl_salv_selections.

    row_c = row.

    read table gt_quotation index row_c into ls_quotation. "gt_output is the output internal table.

    set parameter id 'ANF' field ls_quotation-ebeln.
    set parameter id 'BSP' field ls_quotation-ebelp.
    call transaction 'ME47' and skip first screen.



  endmethod.

  method on_link_click.
    data: ls_item   type ty_item,
          ls_vendor type ty_vendor.

    gt_quotation = corresponding #( gt_rfq ).
    case column.
      when 'MATNR'.

        try.
            ls_item = corresponding #( gt_item[ row ] ).
            delete gt_quotation where matnr ne ls_item-matnr.
          catch cx_sy_itab_line_not_found.

        endtry.

      when 'EBELN'.
        try.
            ls_vendor = corresponding #( gt_vendor[ row ] ).
            delete gt_quotation where ebeln ne ls_vendor-ebeln.
          catch cx_sy_itab_line_not_found.

        endtry.

    endcase.

    r_alv_quotation->refresh( ).






  endmethod.
  method action.
    data: gt_sval         type table of sval,

          wa_sval         type sval,
          vl_title(20)    type c,
          vl_return(1)    type c,
          vl_start_column type i,
          vl_start_row    type i.

    "Valor padrão para abrir o popup
    vl_start_column = 5.
    vl_start_row = 5.
    clear gt_sval.

    case i_action.

      when 'REQUISITION'.
        if lines( gt_quotation ) = 0.
          wa_sval-tabname = 'EBAN'.
          wa_sval-fieldname = 'BANFN'.
          wa_sval-value = ''.
          wa_sval-field_obl = ''.
          append wa_sval to gt_sval.
          clear wa_sval.

          wa_sval-tabname = 'EBAN'.
          wa_sval-fieldname = 'BNFPO'.
          wa_sval-value = ''.
          wa_sval-field_obl = ''.
          append wa_sval to gt_sval.
          clear wa_sval.

          wa_sval-tabname = 'EBAN'.
          wa_sval-fieldname = 'EKGRP'.
          wa_sval-value = me->i_ekgrp.
          wa_sval-field_obl = 'X'.
          append wa_sval to gt_sval.


          me->get_popup( exporting i_title = 'Requição'
                                   i_start_column = '5'
                                   i_start_row = '5'
                         changing  it_sval = gt_sval ) .

          me->get_listrequisition( exporting it_sval =  gt_sval ).
        else.
          message |Já existem cotações criadas, não é possivel adicionar mais material| type 'I'.
        endif.



      when 'ADDMAT'.
        if lines( gt_quotation ) = 0.

          wa_sval-tabname = 'EBAN'.
          wa_sval-fieldname = 'MATNR'.
          wa_sval-value = ''.
          wa_sval-field_obl = 'X'.
          append wa_sval to gt_sval.
          clear wa_sval.

          wa_sval-tabname = 'EBAN'.
          wa_sval-fieldname = 'MENGE'.
          wa_sval-value = ''.
          wa_sval-field_obl = 'X'.
          append wa_sval to gt_sval.

          wa_sval-tabname = 'EBAN'.
          wa_sval-fieldname = 'EKGRP'.
          wa_sval-value = me->i_ekgrp.
          wa_sval-field_obl = 'X'.
          append wa_sval to gt_sval.

          wa_sval-tabname = 'EBAN'.
          wa_sval-fieldname = 'WERKS'.
          wa_sval-value = me->i_werks.
          wa_sval-field_attr = '02'.
          "wa_sval-field_obl = 'X'.

          append wa_sval to gt_sval.


          me->get_popup( exporting i_title = 'Material'
                                   i_start_column = '5'
                                   i_start_row = '5'
                         changing  it_sval = gt_sval ) .

          me->get_material( exporting it_sval = gt_sval ).
        else.
          message |Já existem cotações criadas, não é possivel adicionar mais material| type 'I'.
        endif.
      when 'ADDVENDOR'.
        wa_sval-tabname = 'EBAN'.
        wa_sval-fieldname = 'LIFNR'.
        wa_sval-value = ''.
        wa_sval-field_obl = 'X'.
        append wa_sval to gt_sval.
        me->get_popup( exporting i_title = 'Fornecedor'
                                 i_start_column = 110
                                 i_start_row = 5
                       changing  it_sval = gt_sval ) .

        me->get_vendor( exporting it_sval =  gt_sval ).

      when 'DELMAT'.
        if lines( gt_quotation ) = 0.
          me->remove_row( i_object = r_alv_item ).
        else.
          message |Já existem cotações criadas, não é possivel remover!| type 'I'.
        endif.
      when 'DELVENDOR'.
        me->remove_row( i_object = r_alv_vendor ).

    endcase.
  endmethod.

  method get_popup.
    data: gt_sval         type table of sval,
          wa_sval         type sval,
          vl_title(20)    type c,
          vl_return(1)    type c,
          vl_start_column type i,
          vl_start_row    type i.

    "Valor padrão para abrir o popup

    if i_start_column  is initial.
      vl_start_column = 5.
    else.
      vl_start_column = i_start_column.
    endif.

    if i_start_row is initial.
      vl_start_row = 5.
    else.
      vl_start_row = i_start_row .
    endif.


    call function 'POPUP_GET_VALUES'
      exporting
        no_value_check  = 'X'
        popup_title     = i_title
        start_column    = vl_start_column
        start_row       = vl_start_row
      importing
        returncode      = vl_return
      tables
        fields          = it_sval
      exceptions
        error_in_fields = 1
        others          = 2.
    if vl_return eq 'A'.
      "eerro"
    else.


    endif.

  endmethod.
  method remove_row.

    break-point.
    data : lt_row type salv_t_row.
    " lt_row_item   type salv_t_row,


    i_object->get_metadata( ).
    "  r_alv_vendor->get_metadata( ).
    "r_item_selections = r_alv_item->get_selections( )->get_selected_rows( ).

    " r_alv_vendor->get_metadata( ).

    lt_row = i_object->get_selections( )->get_selected_rows( ).

    "    lt_row_vendor = r_alv_vendor->get_selections( )->get_selected_rows( ).
  endmethod.
  method get_listrequisition.
    data :  r_alv_requisition type ref to cl_salv_table,
            r_selections      type ref to cl_salv_selections,
            r_functions       type ref to cl_salv_functions_list,
            lt_rows           type salv_t_row,
            lt_requisition    type table of ty_item,
            wa_requisition    type ty_item,
            vl_banfn          type eban-banfn,
            vl_bnfpo          type eban-bnfpo,
            vl_ekgrp          type eban-ekgrp,
            vl_where          type string.

    check it_sval is not initial.


    try.
        vl_banfn = it_sval[ fieldname = 'BANFN' ]-value.

      catch cx_sy_itab_line_not_found.

    endtry.
    try.
        vl_bnfpo = it_sval[ fieldname = 'BNFPO' ]-value.

      catch cx_sy_itab_line_not_found.

    endtry.
    try.
        vl_ekgrp = it_sval[ fieldname = 'EKGRP' ]-value.

      catch cx_sy_itab_line_not_found.

    endtry.

    data(sql_werks) = 'werks eq ''' &&  i_werks && ''''.
    data(sql_ekgrp) = 'and ekgrp eq ''' && vl_ekgrp && ''''.
    data(sql_statu) = 'and statu in (''A'',''N'') and loekz ne ''X''  and ebakz ne ''X'' '.
    "data(sql_banpr) = 'and banpr in ()'.
    data(sql_banfn) = 'and banfn eq '''  && vl_banfn && ''''.
    data(sql_bnfpo) = 'and bnfpo eq '''  && vl_bnfpo && ''''.


    concatenate sql_werks sql_ekgrp sql_statu into vl_where separated by space.

    if vl_banfn > 0.
      concatenate vl_where sql_banfn into vl_where separated by space.
    endif.
    if vl_bnfpo > 0.
      concatenate vl_where sql_bnfpo into vl_where separated by space.
    endif.

    select * from eban
      into corresponding fields of table lt_requisition
      where (vl_where).


    try.
        cl_salv_table=>factory(
          importing
            r_salv_table = r_alv_requisition
          changing
            t_table      = lt_requisition  ).

      catch cx_salv_msg.
    endtry.

    r_selections = r_alv_requisition->get_selections( ).
    r_selections->set_selection_mode( if_salv_c_selection_mode=>row_column ).

    r_functions = r_alv_requisition->get_functions( ).
    r_functions->set_all( 'X' ).

    if r_alv_requisition is bound.

      r_alv_requisition->set_screen_popup(
        start_column = 10
        end_column  = 120
        start_line  = 5
        end_line    = 15 ).

      r_alv_requisition->display( ).
    endif.


    lt_rows = r_alv_requisition->get_selections( )->get_selected_rows( ).

    if  lt_rows is not initial.
      loop at lt_rows assigning field-symbol(<fs_row>).
        wa_requisition = corresponding #( lt_requisition[ <fs_row> ] ).
        append wa_requisition to gt_item.
      endloop.
      sort gt_item ascending by banfn bnfpo matnr.
      delete adjacent duplicates from gt_item comparing banfn bnfpo matnr.
    endif.
    r_alv_item->refresh( refresh_mode = 2  ).

  endmethod.
  method get_material.
    data: vl_matnr type eban-matnr,
          vl_ekgrp type eban-ekgrp,
          vl_menge type eban-menge,
          wa_item  type ty_item.

    check it_sval is not initial.

    try.
        vl_matnr = it_sval[ fieldname = 'MATNR' ]-value.

      catch cx_sy_itab_line_not_found.

    endtry.

    try.
        vl_menge = it_sval[ fieldname = 'MENGE' ]-value.

      catch cx_sy_itab_line_not_found.

    endtry.


    try.
        vl_ekgrp = it_sval[ fieldname = 'EKGRP' ]-value.

      catch cx_sy_itab_line_not_found.

    endtry.


    select single mara~matnr, mara~meins, makt~maktx,  marc~werks,  marc~ekgrp
         from ( mara inner join makt on  makt~matnr = mara~matnr
                inner join marc on  marc~matnr = makt~matnr )
         into @data(wa_material)
         where mara~matnr eq @vl_matnr
           and marc~werks eq @me->i_werks.

    if wa_material is not initial.
      wa_item = corresponding #( wa_material ).
      wa_item-ekgrp = vl_ekgrp.
      wa_item-menge = vl_menge.
      wa_item-txz01 = wa_material-maktx.

      append wa_item to gt_item.
    endif.

    r_alv_item->refresh( refresh_mode = 2 ).
  endmethod.

  method get_vendor.
    data: vl_lifnr type ekko-lifnr.

    check it_sval is not initial.

    try.
        vl_lifnr = it_sval[ fieldname = 'LIFNR' ]-value.

      catch cx_sy_itab_line_not_found.

    endtry.

    select lfa1~lifnr lfa1~name1 lfa1~regio lfa1~stcd1
           lfm1~ekorg lfm1~waers lfm1~zterm lfm1~inco1 lfm1~inco2 lfm1~verkf lfm1~telf1
        from ( lfa1 inner join lfm1 on lfa1~lifnr = lfm1~lifnr )
      appending corresponding fields of table  gt_vendor
      where lfa1~lifnr eq vl_lifnr.

    sort gt_vendor ascending by lifnr.
    delete adjacent duplicates from gt_vendor comparing lifnr.

    r_alv_vendor->refresh( refresh_mode = 2 ).

  endmethod.

  method get_price_compare.
    data: gl_bestbuy type table of ty_rfq,
          wl_bestbuy type ty_rfq.
    "seleciona ultimo preço do material/centro na unidade de medida da cotação
    "popular esta variável com a logica para buscar um preço de comparaçao,
    "preço co ultimo pedido, mestre de materiais...


    "se o preço nao é indicado/encontrado utiliza o menor preço de todos os itens da respectiva cotação
    if i_item-statu is not initial.
    gl_bestbuy = gt_rfq.
    delete gl_bestbuy where statu is INITIAL.
    " sort  gl_bestbuy ascending by ebelp .

    "delete adjacent duplicates from gl_bestbuy.

    "delete adjacent duplicates from gl_bestbuy comparing ebelp.

    sort  gl_bestbuy ascending by brtwr ebelp. "ordena pelo menor preço

    if i_item-vlrcomp  eq 0.
      try.
          i_item-vlrcomp = gl_bestbuy[ ebelp = i_item-ebelp ]-brtwr .

          "append  wl_bestbuy to gt_bestbuy.
          "e_bestbuy =  wl_bestbuy ."CORRESPONDING #( gl_bestbuy[ 1 ] ).
        catch cx_sy_itab_line_not_found.
          i_item-vlrcomp = 0.
      endtry.

    endif.
    try.
        i_item-perc = ( ( i_item-brtwr - i_item-vlrcomp ) / i_item-vlrcomp )  * 100  .

      catch cx_sy_zerodivide.
        i_item-perc = 100.
    endtry.

      i_item-icon = cond #( when i_item-perc = 0 then icon_equal_green
                            when i_item-perc > 0 then icon_outgoing_object
                            when i_item-perc < 0 then icon_incoming_object ).
    endif.






  endmethod.
  method generator_quotation.

    data : lt_row_vendor type salv_t_row,
           lt_row_item   type salv_t_row,
           wa_vendor     type ty_vendor,
           r_selections  type ref to cl_salv_selections.

    r_alv_item->get_metadata( ).
    r_alv_vendor->get_metadata( ).
    "r_item_selections = r_alv_item->get_selections( )->get_selected_rows( ).

    " r_alv_vendor->get_metadata( ).

    lt_row_item = r_alv_item->get_selections( )->get_selected_rows( ).

    lt_row_vendor = r_alv_vendor->get_selections( )->get_selected_rows( ).


    if lt_row_vendor is initial.
      message |selecione ao menos um fornecedor!| type 'I'.
      exit.
    endif.
    if lines( lt_row_vendor ) > 6 .
      message |selecione até 5 fornecedores!| type 'I'.
      exit.
    endif.

    if lines( gt_item ) is initial.
      message |Lista de itens/requisição esta vazia!| type 'I'.
      exit.
    endif.

    loop at lt_row_vendor assigning field-symbol(<fs_vendor>).
      try.
          wa_vendor = gt_vendor[ <fs_vendor> ].

          if wa_vendor-ebeln is initial.
            create_quotation( exporting i_lifnr = wa_vendor-lifnr  ).
            cl_progress_indicator=>progress_indicate( i_text = |Criando nova cotação: { sy-tabix } / { lines( lt_row_vendor ) }| i_output_immediately = abap_true ).
          else.
            message | Fornecedor | && wa_vendor-name1 && |já possui cotação criada!| type 'I'.
          endif.

        catch cx_sy_itab_line_not_found.
      endtry.
    endloop.

    me->get_data( ).
    me->r_alv_vendor->refresh( ).
    me->r_alv_quotation->refresh( ).

  endmethod.

  method create_quotation.

    data: wa_ekko     type ekko,
          wa_ekpo     type ekpo,
          lt_ekpo     type table of ekpo,

          vl_item     type i,
          vl_delivery type dats,

          head1_dbc   type table of bdcdata,
          head2_dbc   type table of bdcdata,
          head3_dbc   type table of bdcdata,
          itens_dbc   type table of bdcdata,
          bdcdata_tab type table of bdcdata,
          wa_bdcdata  type bdcdata,
          opt         type ctu_params,
          lt_message  type standard table of bdcmsgcoll,

          it_message  type standard table of bdcmsgcoll,
          wa_message  type bdcmsgcoll.

    clear: head1_dbc,head2_dbc, bdcdata_tab,opt,lt_ekpo.

    wa_ekko-bsart = 'AN'.
    wa_ekko-spras = sy-langu.
    wa_ekko-bnddt = sy-datum.
    wa_ekko-angdt = sy-datum + 15.
    wa_ekko-ekorg = '1000'."buscar organizaco de compras conforme o centor do item
    wa_ekko-ekgrp = me->i_ekgrp.
    "wa_ekko-werks = me->i_werks.
    wa_ekko-submi = i_submi. "criar recurso para gerar numero automatico

    wa_ekko-kdatb = sy-datum.
    wa_ekko-kdate = sy-datum + 30.
    wa_ekko-ihrez = 'tes'.
    wa_ekko-lifnr = i_lifnr.


    lt_ekpo = corresponding #( gt_item ).

    head1_dbc = value #(
                         ( program  = 'SAPMM06E' dynpro   = '0300' dynbegin = 'X' )
                         ( fnam = 'BDC_CURSOR'       fval = 'RM06E-WERKS' )
                         ( fnam = 'BDC_OKCODE'       fval = '=KOPF' )
                         ( fnam = 'RM06E-ASART'      fval =  wa_ekko-bsart )
                         ( fnam = 'EKKO-SPRAS'       fval =  wa_ekko-spras  )
                         ( fnam = 'RM06E-ANFDT'      fval =  wa_ekko-bnddt+6(2) && wa_ekko-bnddt+4(2) &&  wa_ekko-bnddt(4) )
                         ( fnam = 'EKKO-ANGDT'       fval =  wa_ekko-angdt+6(2) && wa_ekko-angdt+4(2) &&  wa_ekko-angdt(4) )
                         ( fnam = 'EKKO-EKORG'       fval =  wa_ekko-ekorg )
                         ( fnam = 'EKKO-EKGRP'       fval =  wa_ekko-ekgrp )
                         ( fnam = 'RM06E-LPEIN'      fval = 'T' )
                         ( fnam = 'RM06E-WERKS'      fval = me->i_werks )


                         ( program  = 'SAPMM06E' dynpro   = '0301' dynbegin = 'X' )
                         ( fnam = 'BDC_CURSOR'       fval = 'EKKO-KDATB' )
                         ( fnam = 'BDC_OKCODE'       fval = '/00' )
                         ( fnam = 'EKKO-SUBMI'      fval =  wa_ekko-submi )
                         ( fnam = 'EKKO-KDATB'      fval =  wa_ekko-kdatb+6(2) && wa_ekko-kdatb+4(2) && wa_ekko-kdatb(4) )
                         ( fnam = 'EKKO-KDATE'      fval =  wa_ekko-kdate+6(2) && wa_ekko-kdate+4(2) && wa_ekko-kdate(4) )
                         ( fnam = 'EKKO-IHREZ'      fval =  wa_ekko-ihrez )

                      "   ( program  = 'SAPMM06E' dynpro   = '0301' dynbegin = 'X' )
                         ( fnam = 'BDC_OKCODE'       fval = '=AB' )


                          ).

    head2_dbc = value #(
                        ( fnam = 'BDC_OKCODE'           fval = '/00' )
                        ( fnam = 'BDC_OKCODE'           fval = '=LS' )
                        ( program  = 'SAPMM06E'         dynpro   = '0140' dynbegin = 'X' )
                        ( fnam = 'BDC_CURSOR'           fval = 'EKKO-LIFNR'  )
                        ( fnam = 'BDC_OKCODE'           fval = '/00' )
                        ( fnam = 'EKKO-LIFNR'           fval = wa_ekko-lifnr )

                        ( program  = 'SAPLMEXF'         dynpro   = '0100' dynbegin = 'X' )
                        ( fnam = 'BDC_OKCODE'           fval = '=ENTE' )
                        ( fnam = 'BDC_CURSOR'           fval = 'RM06E-SPRAS'  )
                        ( fnam = 'BUTTON_VENDOR'        fval = 'X' )

                        ( program  = 'SAPMM06E'         dynpro   = '0140' dynbegin = 'X' )
                        ( fnam = 'BDC_OKCODE'           fval = '=BU' )
                        ( fnam = 'BDC_CURSOR'           fval = 'EKKO-LIFNR'  )

                        "( program  = 'SAPMM06E'         dynpro   = '0140' dynbegin = 'X' )
                        "( fnam = 'BDC_OKCODE'           fval = '/ENN' )
                        "( fnam = 'BDC_CURSOR'           fval = 'EKKO-LIFNR'  )

*                        ( program  = 'SAPLSPO1' dynpro   = '0300' dynbegin = 'X' )
*                        ( fnam = 'BDC_OKCODE'           fval = '=YES' )
                       ).


    vl_delivery = sy-datum + 20.



    loop at gt_item assigning field-symbol(<fs_item>).

      "verifica se o item tem requisição
      vl_item = vl_item + 1.
      if <fs_item>-banfn is not initial.
        wa_bdcdata-program = 'SAPMM06E'.
        wa_bdcdata-dynpro = '0320'.
        wa_bdcdata-dynbegin = 'X'.
        wa_bdcdata-fnam = 'BDC_CURSOR'.
        wa_bdcdata-fval = 'EKKO-ANGDT'.
        wa_bdcdata-fnam = 'BDC_OKCODE'.
        wa_bdcdata-fval = '=BS'.

        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.


        wa_bdcdata-program = 'SAPMM06E'.
        wa_bdcdata-dynpro = '0501'.
        wa_bdcdata-dynbegin = 'X'.
        wa_bdcdata-fnam = 'BDC_CURSOR'.
        wa_bdcdata-fval = 'EKET-BNFPO'.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.

        wa_bdcdata-fnam = 'BDC_OKCODE'.
        wa_bdcdata-fval = '=ENTE'.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.

        wa_bdcdata-fnam = 'EKET-BANFN'.
        wa_bdcdata-fval = <fs_item>-banfn.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.

        wa_bdcdata-fnam = 'EKET-BNFPO'.
        wa_bdcdata-fval = <fs_item>-bnfpo.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.

        wa_bdcdata-fnam = 'EBAN-EKGRP'.
        wa_bdcdata-fval = ''.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.


        wa_bdcdata-program = 'SAPMM06E'.
        wa_bdcdata-dynpro = '0125'.
        wa_bdcdata-dynbegin = 'X'.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.


        wa_bdcdata-fnam = 'BDC_CURSOR'.
        wa_bdcdata-fval = 'EBAN-LGORT(01)'.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.

        wa_bdcdata-fnam = 'BDC_OKCODE'.
        wa_bdcdata-fval = '=MALL'.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.

        wa_bdcdata-program = 'SAPMM06E'.
        wa_bdcdata-dynpro = '0125'.
        wa_bdcdata-dynbegin = 'X'.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.


        wa_bdcdata-fnam = 'BDC_CURSOR'.
        wa_bdcdata-fval = 'EBAN-LGORT(01)'.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.

        wa_bdcdata-fnam = 'BDC_OKCODE'.
        wa_bdcdata-fval = '=REFH'.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.


        wa_bdcdata-program = 'SAPMM06E'.
        wa_bdcdata-dynpro = '0311'.
        wa_bdcdata-dynbegin = 'X'.
        wa_bdcdata-fnam = 'BDC_CURSOR'.
        wa_bdcdata-fval = 'RM06E-EEIND'.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.

        wa_bdcdata-fnam = 'BDC_OKCODE'.
        wa_bdcdata-fval = '/00'.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.



        wa_bdcdata-fnam = 'RM06E-EEIND'.
        wa_bdcdata-fval = vl_delivery+6(2) && vl_delivery+4(2) && vl_delivery(4) .

        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.





      else.


        " Itens da cotação
        wa_bdcdata-program = 'SAPMM06E'.
        wa_bdcdata-dynpro = '0320'.
        wa_bdcdata-dynbegin = 'X'.
        wa_bdcdata-fnam = ''.
        wa_bdcdata-fval = ''.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.


        wa_bdcdata-program = ''.
        wa_bdcdata-dynpro = ''.
        wa_bdcdata-dynbegin = ''.
        wa_bdcdata-fnam = 'BDC_CURSOR'.
        wa_bdcdata-fval = 'RM06E-EBELP'.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.

        wa_bdcdata-program = ''.
        wa_bdcdata-dynpro = ''.
        wa_bdcdata-dynbegin = ''.
        wa_bdcdata-fnam = 'BDC_OKCODE'.
        wa_bdcdata-fval = '/00'.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.

        wa_bdcdata-program = ''.
        wa_bdcdata-dynpro = ''.
        wa_bdcdata-dynbegin = ''.
        wa_bdcdata-fnam = 'RM06E-EBELP'.
        wa_bdcdata-fval = vl_item * 10.
        condense wa_bdcdata-fval.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.

        wa_bdcdata-program = ''.
        wa_bdcdata-dynpro = ''.
        wa_bdcdata-dynbegin = ''.
        if vl_item = 1 .
          wa_bdcdata-fnam = 'EKPO-EMATN(01)'.
        else.
          wa_bdcdata-fnam = 'EKPO-EMATN(02)'.
        endif.
        wa_bdcdata-fval = <fs_item>-matnr.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.

        wa_bdcdata-program = ''.
        wa_bdcdata-dynpro = ''.
        wa_bdcdata-dynbegin = ''.
        if vl_item = 1 .
          wa_bdcdata-fnam = 'RM06E-ANMNG(01)'.
        else.
          wa_bdcdata-fnam = 'RM06E-ANMNG(02)'.
        endif.
        wa_bdcdata-fval = <fs_item>-menge.
        condense wa_bdcdata-fval.
        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.

        wa_bdcdata-program = ''.
        wa_bdcdata-dynpro = ''.
        wa_bdcdata-dynbegin = ''.
        if vl_item = 1 .
          wa_bdcdata-fnam = 'RM06E-EEIND(01)'.
        else.
          wa_bdcdata-fnam = 'RM06E-EEIND(02)'.
        endif.

        wa_bdcdata-fval = vl_delivery+6(2) && vl_delivery+4(2) && vl_delivery(4) .

        append wa_bdcdata to itens_dbc.
        clear: wa_bdcdata.


      endif.
    endloop.

    append lines of head1_dbc to bdcdata_tab.
    append lines of itens_dbc to bdcdata_tab.
    "    if i_head-lifnr = '0000899999'.
    "     append lines of head3_dbc to bdcdata_tab.
    "   else.
    append lines of head2_dbc to bdcdata_tab.
    "   endif.


    opt-racommit = 'X'.
    opt-dismode = 'N'.
    opt-defsize = 'X'.
    opt-updmode = 'A'.

    call transaction 'ME41' with authority-check using bdcdata_tab options from opt messages into it_message.

    append lines of it_message to lt_message.
    append lines of it_message to gt_msgerror.


    delete lt_message where msgnr ne '017'. "elimina mensagens de erro.


    loop at gt_vendor assigning field-symbol(<fs_vendor>) where lifnr = i_lifnr.
      if lt_message is not initial.
        try.
            data(vl_ebeln) = lt_message[ msgnr = '017' ]-msgv2.

            <fs_vendor>-iconv = icon_led_green.
            <fs_vendor>-ebeln = vl_ebeln.
            <fs_vendor>-submi = i_submi.

          catch  cx_sy_itab_line_not_found.
            <fs_vendor>-iconv = icon_led_red.
        endtry.
      else.
        <fs_vendor>-iconv = icon_led_red.
      endif.
    endloop.




  endmethod.
  method update_item_quotation.
    data: wa_ekko     type ekko,
          wa_ekpo     type ekpo,
          lt_ekpo     type table of ekpo,

          vl_item     type i,
          vl_delivery type dats,

          head1_dbc   type table of bdcdata,
          head2_dbc   type table of bdcdata,
          head3_dbc   type table of bdcdata,
          itens_dbc   type table of bdcdata,
          bdcdata_tab type table of bdcdata,
          wa_bdcdata  type bdcdata,
          opt         type ctu_params,
          lt_message  type standard table of bdcmsgcoll,

          it_message  type standard table of bdcmsgcoll,
          wa_message  type bdcmsgcoll.

    clear: head1_dbc,head2_dbc, bdcdata_tab,opt,lt_ekpo.



    head1_dbc = value #(
                         ( program  = 'SAPMM06E' dynpro   = '0305' dynbegin = 'X' )
                         ( fnam = 'BDC_CURSOR'       fval = 'RM06E-ANFNR' )
                         ( fnam = 'BDC_OKCODE'       fval = '/00' )
                         ( fnam = 'RM06E-ANFNR'      fval =  i_item-ebeln )

                         ( program  = 'SAPMM06E' dynpro   = '0323' dynbegin = 'X' )
                         ( fnam = 'BDC_CURSOR'       fval = 'RM06E-EBELP' )
                         ( fnam = 'BDC_OKCODE'       fval = '/00' )
                         ( fnam = 'RM06E-EBELP'      fval =  i_item-ebelp )

                         ( program  = 'SAPMM06E'         dynpro   = '0323' dynbegin = 'X' )
                         ( fnam = 'BDC_CURSOR'           fval = 'RM06E-ANFPS(01)' )
                         ( fnam = 'BDC_OKCODE'           fval = '=DETA' )
                         ( fnam = 'RM06E-TCSELFLAG(01)'  fval =  'X' )
                         ( fnam = 'RM06E-EBELP'          fval =  i_item-ebelp )



                         ( program  = 'SAPMM06E' dynpro   = '0311' dynbegin = 'X' )
                         ( fnam = 'BDC_CURSOR'       fval = 'EKPO-MWSKZ' )
                         ( fnam = 'BDC_OKCODE'       fval = '/00' )
                         ( fnam = 'EKPO-NETPR'      fval =  i_item-netpr )
                         ( fnam = 'EKPO-MWSKZ'      fval =  i_item-mwskz )
                         ( fnam = 'EKPO-AGMEM'      fval =  i_item-agmem )
                         ( fnam = 'EKPO-ABSKZ'      fval =  i_item-abskz )

                         ( program  = 'SAPMM06E' dynpro   = '0323' dynbegin = 'X' )
                         ( fnam = 'BDC_CURSOR'       fval = 'RM06E-ANFPS(01)' )
                         ( fnam = 'BDC_OKCODE'       fval = '=BU' )
                         ( fnam = 'RM06E-EBELP'      fval =  i_item-ebelp )

                          ).

    append lines of head1_dbc to bdcdata_tab.

    opt-racommit = 'X'.
    opt-dismode = 'N'.
    opt-defsize = 'X'.
    opt-updmode = 'A'.

    call transaction 'ME47' with authority-check using bdcdata_tab options from opt messages into it_message.

    append lines of it_message to lt_message.
    "append lines of it_message to lt_message_erro.

    delete lt_message where msgnr ne '017'. "elimina mensagens de erro.

*

    if lt_message is not initial.
      r_alv_quotation->refresh( ).
*      me->get_sourcing( exporting  i_sourcing = lo_sourcing ).
*
*      lo_grid2->refresh_table_display( ).
*
*      lo_grid3->refresh_table_display( ).


    endif.
  endmethod.

  method recuseall.
    data: lv_answer type c.

    call function 'POPUP_TO_CONFIRM'
      exporting
        titlebar              = 'Recusar Cotações.'
        text_question         = 'Deseja marcar como recusado as cotações com prazo de apresentação vencido?'
        text_button_1         = 'OK'
        icon_button_1         = 'ICON_CHECKED'
        text_button_2         = 'CANCEL'
        icon_button_2         = 'ICON_CANCEL'
        display_cancel_button = ' '
        popup_type            = 'ICON_MESSAGE_ERROR'
      importing
        answer                = lv_answer.

    if lv_answer = 1.
      "verifica as cotações com prazo vencido
      "verifica se há itens com caracteristica nao preenchida
      "chama bapi e marca como recusado os itens e caracteristica recusa
      loop at gt_quotation assigning field-symbol(<fs_item>).
        if <fs_item>-abskz is initial
           and <fs_item>-agmem is initial
           and <fs_item>-brtwr eq 0
           and <fs_item>-agdat < sy-datum.

          <fs_item>-abskz = abap_true.
          <fs_item>-agmem = 'AB1'. "Indicar o motivo padrao

          me->update_item_quotation( exporting i_item =  <fs_item> ).
        endif.
      endloop.
    endif.
    r_alv_quotation->refresh( ).
  endmethod.

  method get_bestquotation.
    data: ls_best  type ty_rfq,

          lt_best  type table of ty_rfq,
          ls_erro  type i,
          ls_count type i,
          ls_ebelp type i.
    clear lt_best.

    gt_quotation = corresponding #( gt_rfq ).

    "Faz contagem de quantos itens distintos tem nas cotações
    ls_count = lines( gt_item ).

    break-point.

    "faz  atribuição apenas das cotações cujo o item possui valor indicado,
    "as cotações sem valor em um item nao são levadas em consideração
    loop at gt_rfq assigning field-symbol(<fs_rfq>) where statu is not initial.
      if <fs_rfq>-brtwr = 0 .
        ls_erro = ls_erro + 1 .
      endif.
      "encontrar a quantidade de itens pra validar.
      <fs_rfq>-menge = 1.
      ls_best-ebeln = <fs_rfq>-ebeln.
      ls_best-menge = <fs_rfq>-menge .
      ls_best-brtwr = <fs_rfq>-brtwr.
      collect ls_best into lt_best.


      clear ls_best.
    endloop.
    clear: ls_best, ls_ebelp.


    if ls_erro > 0.
      message |há item sem preço! A escolha da melhor cotação não pode ser feita.| type 'I'.
    else.


      "elimina cotações sumarizada que nao possuem todos os itens com valores .
      delete lt_best where menge <> ls_count.
      "ordena pelo menor preço
      sort lt_best ascending by brtwr.
      try.
          ls_best = lt_best[ 1 ].
          delete gt_quotation where ebeln ne ls_best-ebeln.
        catch cx_sy_itab_line_not_found.
      endtry.
      r_alv_quotation->refresh( ).
    endif.


  endmethod.

  method get_bestprice.
    data: ls_best type ty_rfq,
          lt_best type table of ty_rfq,
          ls_erro type i.

    clear lt_best.

    gt_quotation = corresponding #( gt_rfq ).
    lt_best = corresponding #( gt_rfq ).

    delete gt_quotation where statu is initial.
    delete lt_best  where statu is initial.

    sort lt_best ascending by ebelp.
    delete adjacent duplicates from lt_best comparing ebelp.

    sort gt_quotation ascending by ebelp brtwr.

    loop at lt_best assigning field-symbol(<fs_best>).
      try.
          <fs_best>-ebeln =  gt_quotation[ ebelp = <fs_best>-ebelp  ]-ebeln .
        catch cx_sy_itab_line_not_found.
      endtry.
    endloop.


    loop at gt_quotation assigning field-symbol(<fs_quotation>) .
      if <fs_quotation>-brtwr = 0 .
        ls_erro = ls_erro + 1 .
      else.
        try.
            ls_best = lt_best[ ebeln = <fs_quotation>-ebeln ebelp = <fs_quotation>-ebelp ] .
          catch cx_sy_itab_line_not_found.
            <fs_quotation>-ebelp = 0.
            <fs_quotation>-ebeln = 0.
        endtry.
      endif.
    endloop.





    if ls_erro > 0.
      message |há item sem preço! A escolha da melhor cotação não pode ser feita.| type 'I'.
    else.
      delete gt_quotation where ebelp = 0.
      r_alv_quotation->refresh( ).
    endif.
  endmethod.

   method show_log_erros.
    data : lt_log_erro type  esp1_message_tab_type,
           wa_log_erro type line of esp1_message_tab_type.

    delete adjacent duplicates from gt_msgerror .

    loop at gt_msgerror assigning field-symbol(<fs_erro>).
      wa_log_erro-msgid = <fs_erro>-msgid.
      wa_log_erro-msgty = <fs_erro>-msgtyp.
      wa_log_erro-msgno = <fs_erro>-msgnr.
      wa_log_erro-msgv1 = <fs_erro>-msgv1.
      wa_log_erro-msgv2 = <fs_erro>-msgv2.
      wa_log_erro-msgv3 = <fs_erro>-msgv2.
      wa_log_erro-msgv4 = <fs_erro>-msgv4.
      append wa_log_erro to lt_log_erro.
      clear : wa_log_erro.
    endloop.



    call function 'C14Z_MESSAGES_SHOW_AS_POPUP'
      tables
        i_message_tab = lt_log_erro.


  endmethod.

  method show_map.
    message | chamada ao smartform para demonstrar o mapa comparativo| type 'I'.


  DATA: v_form_name TYPE rs38l_fnam,
        w_compop    TYPE ssfcompop,
        w_ctrlop    TYPE ssfctrlop.

  DATA: wa_lvc_t_row TYPE lvc_t_row,
        vl_formname  TYPE c LENGTH 30.



       vl_formname = 'Z_MAPRFQ'.

  free r_container3.

    CALL FUNCTION 'SSF_FUNCTION_MODULE_NAME'
      EXPORTING
        formname           = vl_formname
      IMPORTING
        fm_name            = v_form_name
      EXCEPTIONS
        no_form            = 1
        no_function_module = 2
        OTHERS             = 3.
    IF sy-subrc <> 0.
      MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
      WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
    ENDIF.

**     "Impressao com preview
**    w_compop-tddest    = 'LOCL'. "Interactive - Printer from selection-screen
**    w_ctrlop-preview   = 'X'.
**
**
**


    CALL FUNCTION v_form_name
*      TABLES
*        it_mm_etq        = itmmetq
*        it_ydpp023       = it_ydpp023
      EXCEPTIONS
        formatting_error = 1
        internal_error   = 2
        send_error       = 3
        user_canceled    = 4
        OTHERS           = 5.
    IF sy-subrc <> 0.
      MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
      WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.


    ENDIF.



  ENDMETHOD.

  method choice_quotation.
    data: vl_erro type i.

    "verifica se existe cotações
    if gt_quotation is INITIAL.
       message |Não existe cotações para criar o documento de compras| type 'I'.
    endif.

    "Verifica se as cotações estão com valores respondidos.
    loop at gt_quotation ASSIGNING FIELD-SYMBOL(<fs_quotation>).
      if <fs_quotation>-statu is INITIAL.
         vl_erro = vl_erro + 1.
      endif.
    endloop.


     "abrir tela com opçao para : indicar qual o cenário de melhor compra
    "1 - Melhor cotação : Valor Total R$ XXXX
    "2 - Melhor preço : "valor Total R# XXXX
    "3 - Especifica: indicar cotação: valor total
     data: vl_answer type c,
           gt_sval         type table of sval,

          wa_sval         type sval.


    call function 'POPUP_WITH_3_BUTTONS_TO_CHOOSE'
      exporting
*       DEFAULTOPTION       = '1'
        diagnosetext1       = 'Para qual opção deseja '
        DIAGNOSETEXT2       = 'criar o documento de compras? '
*       DIAGNOSETEXT3       = ' '
        textline1           = ' '
        TEXTLINE2           = ' '
*       TEXTLINE3           = ' '
        text_option1        = 'Melhor Cotação'
        text_option2        = 'Melhor Preço'
        text_option3        = 'Escolher..'
        titel               = 'Criar documento de compras'
     IMPORTING
              ANSWER        = vl_answer.

     case vl_answer.
       when '1'.
         me->get_bestquotation( ).

         wa_sval-tabname = 'EKKO'.
        wa_sval-fieldname = 'BSART'.
        wa_sval-value = ''.
        wa_sval-field_obl = 'X'.
        append wa_sval to gt_sval.
        me->get_popup( exporting i_title = 'Tipo de documento'
                                 i_start_column = 110
                                 i_start_row = 50
                       changing  it_sval = gt_sval ) .

       " me->get_vendor( exporting it_sval =  gt_sval ).


       when '2'.
         me->get_bestprice( ).
       when '3'.

         data :  r_alv_choice type ref to cl_salv_table,
            r_selections      type ref to cl_salv_selections,
            r_functions       type ref to cl_salv_functions_list,
            lt_rows           type salv_t_row,
            lt_vendor    type table of ty_vendor,
            wa_vendor    type ty_vendor.


    try.
        cl_salv_table=>factory(
          importing
            r_salv_table = r_alv_choice
          changing
            t_table      = gt_vendor  ).

      catch cx_salv_msg.
    endtry.

    r_selections = r_alv_choice->get_selections( ).
    r_selections->set_selection_mode( if_salv_c_selection_mode=>row_column ).

    r_functions = r_alv_choice->get_functions( ).
    r_functions->set_all( 'X' ).

    if r_alv_choice is bound.

      r_alv_choice->set_screen_popup(
        start_column = 10
        end_column  = 120
        start_line  = 5
        end_line    = 15 ).

      r_alv_choice->display( ).
    endif.


    lt_rows = r_alv_choice->get_selections( )->get_selected_rows( ).

    if  lt_rows is not initial.
      loop at lt_rows assigning field-symbol(<fs_row>).
        wa_vendor = corresponding #( lt_vendor[ <fs_row> ] ).

      endloop.

    endif.




       when 'A'.
     endcase.


     BREAK-POINT.
  ENDMETHOD.

  method create_doc.

  ENDMETHOD.
endclass.






selection-screen begin of block bl01.

selection-screen begin of block bl02 with frame.
parameters: p_new   radiobutton group rad1 default 'X' user-command comand1.

selection-screen begin of block bl03 with frame.
parameters: p_werks type t001w-werks,
            p_ekgrp type eban-ekgrp.
select-options: s_banfn for lcl_app=>r_eban->banfn no intervals.

selection-screen end of block bl03.

parameters: p_consul radiobutton group rad1.

selection-screen begin of block bl04 with frame.

parameters p_rfp     type ekko-submi. "matchcode object yaprfp.

selection-screen end of block bl04.

selection-screen end of block bl02.

selection-screen end of block bl01.


at selection-screen output.

  if p_new = abap_true.
    clear p_rfp.
    loop at screen.
      if screen-name eq 'P_WERKS' or screen-name eq 'P_EKGRP' or screen-name eq 'S_BANFN'..
        screen-input = '1'.
        "screen-required = '1'.
        modify screen.
      endif.
      if screen-name eq 'P_RFP'.
        screen-input = '0'.
        " screen-required = '0'.
        modify screen.
      endif.
      modify screen.
    endloop.

  endif.
  if p_consul = abap_true.
    clear: p_werks, s_banfn, p_ekgrp.

    loop at screen.
      if screen-name eq 'P_WERKS' or screen-name eq 'P_EKGRP' or screen-name eq 'S_BANFN'.
        screen-input = '0'.
        "screen-required = '0'.
        modify screen.
      endif.

      if screen-name eq 'P_RFP'.
        screen-input = '1'.
        " screen-required = '1'.
        modify screen.
      endif.
      modify screen.
    endloop.
  endif.



start-of-selection.

  data r_app type ref to lcl_app.

  "create OBJECT r_app.
  r_app = new lcl_app( ).

  r_app->i_werks = p_werks.
  r_app->i_ekgrp = p_ekgrp.
  r_app->i_submi = p_rfp.
  r_app->rg_banfn = s_banfn[].

  r_app->start( ).


*&---------------------------------------------------------------------*
*&      Module  PBO  OUTPUT
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
module pbo output.
  r_app->pbo( exporting i_dynnr = sy-dynnr  i_pfstatus = '0000' i_title = 'RFP'  ).
endmodule.
*&---------------------------------------------------------------------*
*&      Module  PAI  INPUT
*&---------------------------------------------------------------------*
*       text
*----------------------------------------------------------------------*
module pai input.
  r_app->pai( i_ucomm = sy-ucomm i_dynnr = sy-dynnr ).
endmodule.