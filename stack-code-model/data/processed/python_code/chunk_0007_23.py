class lhc_stock definition inheriting from cl_abap_behavior_handler.
  private section.

    methods get_instance_authorizations for instance authorization
      importing keys request requested_authorizations for stock result result.

    methods setValues for determine on save
      importing keys for stock~setValues.

endclass.

class lhc_stock implementation.

  method get_instance_authorizations.
* Method for instance authorization (Auth objetcs, custom validations, etc). Not relevant for demo.
  endmethod.

  method setValues.

* Read entity and fetch SKU value
    read entities of zcds_stock in local mode
    entity stock
    fields ( Sku )
    with corresponding #( keys )
    result data(lt_sku_result).

* Only modify entities where no SKU is given
    delete lt_sku_result where Sku is not initial.

    loop at lt_sku_result assigning field-symbol(<fs_sku>).
* Get a new SKU number (for thi demo it will be random, it should be a consistent number like SNRO or client specific numbering)
      data(lo_new_sku) = cl_abap_random_int=>create( exporting seed = conv i( sy-uzeit )
                                                               min  = 1
                                                               max  = 1000000 ).

* Get next number from automatic seed
      <fs_sku>-Sku = lo_new_sku->get_next( ).

* Add leading zeros to number for a more realistic experience
      <fs_sku>-Sku = |{ <fs_sku>-Sku alpha = in }|.

    endloop.

* Update values in BO
    modify entities of zcds_stock in local mode
      entity stock
      update from value #( for lwa_sku in lt_sku_result
                         (   Skuuuid = lwa_sku-%key-Skuuuid
                             Sku   = lwa_sku-Sku
                    %control-Sku   = if_abap_behv=>mk-on
                     )  ).

  endmethod.

endclass.