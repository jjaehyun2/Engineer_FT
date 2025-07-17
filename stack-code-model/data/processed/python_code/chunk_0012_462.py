class lhc_retailers definition inheriting from cl_abap_behavior_handler.
  private section.

    methods get_instance_authorizations for instance authorization
      importing keys request requested_authorizations for retailers result result.
    methods validateland1 for validate on save
      importing keys for retailers~validateland1.

endclass.

class lhc_retailers implementation.

  method get_instance_authorizations.
* Method for instance authorization (Auth objetcs, custom validations, etc). Not relevant for demo.
  endmethod.

  method validateLand1.

    data lr_land1 type range of land1.

* Read entity and fetch Country value
    read entities of zcds_retailers in local mode
    entity retailers
    fields ( Land1 )
    with corresponding #( keys )
    result data(lt_retailers_result).

* Create range with Country
    lr_land1 = value #( for lwa_land1 in lt_retailers_result
                        sign = 'I'
                        option = 'EQ'
                        ( low = lwa_land1-Land1 ) ).

* Get records from DB from Country range
    select  *
        from I_Country
        where Country in @lr_land1
        into table @data(lt_countries).

* Raise msg for non existing Country
    loop at lt_retailers_result into data(lwa_retailers).

      if lwa_retailers-Land1 is not initial and not line_exists( lt_countries[ Country = lwa_retailers-Land1 ] ).

        append value #(  retailerid = lwa_retailers-Retailerid ) to failed-retailers.

        append value #(  retailerid = lwa_retailers-retailerid
                         %msg      = new_message( id       = '00' "This can also be achieved by creating or using custom message clases
                                                  number   = '001'
                                                  v1       = |Country | && |{ lwa_retailers-Land1 }|
                                                  v2       = | doesn't exist|
                                                  severity = if_abap_behv_message=>severity-error )
                         %element-Land1 = if_abap_behv=>mk-on ) to reported-retailers.
      endif.

    endloop.

  endmethod.

endclass.