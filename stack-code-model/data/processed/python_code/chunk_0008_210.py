class lhc_sales definition inheriting from cl_abap_behavior_handler.
  private section.

    methods get_instance_authorizations for instance authorization
      importing keys request requested_authorizations for sales result result.

    methods validateRetailerid for validate on save
      importing keys for sales~validateRetailerid.
    methods validateSku for validate on save
      importing keys for sales~validateSku.
    methods detStockFields for determine on modify
      importing keys for sales~detStockFields.

endclass.

class lhc_sales implementation.

  method get_instance_authorizations.
* Method for instance authorization (Auth objetcs, custom validations, etc). Not relevant for demo.
  endmethod.

  method validateRetailerid.

    data lr_retailer type range of zapo_sales-retailerid.

* Read entity and fetch Retailer ID value
    read entities of zcds_sales_ret in local mode
    entity sales
    fields ( Retailerid )
    with corresponding #( keys )
    result data(lt_sales_result).

* Create range with Retailer ID
    lr_retailer = value #( for lwa_retailer in lt_sales_result
                        sign = 'I'
                        option = 'EQ'
                        ( low = lwa_retailer-Retailerid ) ).

* Get records from DB from Retailer ID range
    select  *
        from zapo_retailers
        where retailerid in @lr_retailer
        into table @data(lt_retailers).

* Raise msg for non existing Retailer ID
    loop at lt_sales_result into data(lwa_sales).

      if lwa_sales-Retailerid is not initial and not line_exists( lt_retailers[ retailerid = lwa_sales-Retailerid ] ).

        append value #(  retailerid = lwa_sales-Retailerid ) to failed-sales.

        append value #(  retailerid = lwa_sales-retailerid
                         %msg      = new_message( id       = '00' "This can also be achieved by creating or using custom message clases
                                                  number   = '001'
                                                  v1       = |Retailer | && |{ lwa_sales-Retailerid }|
                                                  v2       = | doesn't exist|
                                                  severity = if_abap_behv_message=>severity-error )
                         %element-Retailerid = if_abap_behv=>mk-on ) to reported-sales.
      endif.

    endloop.

  endmethod.

  method validateSku.

    data lr_sku      type range of zapo_sales-sku.

* Read entity and fetch SKU value
    read entities of zcds_sales_ret in local mode
    entity sales
    fields ( Sku )
    with corresponding #( keys )
    result data(lt_sales_result).

* Create range with SKU
    lr_sku = value #( for lwa_retailer in lt_sales_result
                        sign = 'I'
                        option = 'EQ'
                        ( low = lwa_retailer-Sku  ) ).

* Get records from DB from SKU range
    select  *
        from zapo_sku
        where sku in @lr_sku
        into table @data(lt_sku).

* Raise msg for non existing SKU
    loop at lt_sales_result into data(lwa_sales).

      if lwa_sales-Sku is not initial and not line_exists( lt_sku[ sku = lwa_sales-Sku ] ).

        append value #(  sku = lwa_sales-Sku ) to failed-sales.

        append value #(  sku = lwa_sales-sku
                         %msg      = new_message( id       = '00' "This can also be achieved by creating or using custom message clases
                                                  number   = '001'
                                                  v1       = |Retailer | && |{ lwa_sales-Sku }|
                                                  v2       = | doesn't exist|
                                                  severity = if_abap_behv_message=>severity-error )
                         %element-Sku = if_abap_behv=>mk-on ) to reported-sales.
      endif.

    endloop.

  endmethod.

  method detStockFields.

    data lr_sku      type range of zapo_sales-sku.

* Read entity and fetch SKU value
    read entities of zcds_sales_ret in local mode
    entity sales
    fields ( Sku )
    with corresponding #( keys )
    result data(lt_sales_result).

* Create range with SKU
    lr_sku = value #( for lwa_retailer in lt_sales_result
                      sign = 'I'
                      option = 'EQ'
                      ( low = lwa_retailer-Sku  ) ).

* Get records from DB from SKU range
    select  *
        from zapo_sku
        where sku in @lr_sku
        into table @data(lt_sku).

    loop at lt_sales_result assigning field-symbol(<fs_sales>).

* Fields Description and Theme are filled with values from Master Data SKU table
      <fs_sales>-Description = value #( lt_sku[ sku = <fs_sales>-Sku ]-description optional ).
      <fs_sales>-Theme = value #( lt_sku[ sku = <fs_sales>-Sku ]-Theme optional ).

    endloop.

* Update values in BO
    modify entities of zcds_sales_ret in local mode
      entity sales
      update from value #( for lwa_sales in lt_sales_result
                         (   %tky          = lwa_sales-%tky
                             Description   = lwa_sales-Description
                             Theme         = lwa_sales-Theme
                             %control-Description   = if_abap_behv=>mk-on
                             %control-Theme   = if_abap_behv=>mk-on
                     )  )
                     reported data(update_reported).

    reported = corresponding #( deep update_reported ).

  endmethod.

endclass.