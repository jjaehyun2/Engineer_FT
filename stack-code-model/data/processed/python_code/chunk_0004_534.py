class zcl_bank_static definition
  public
  final
  create public .

*"* public components of class ZCL_BANK_STATIC
*"* do not include other source files here!!!
  public section.
    type-pools abap .

    class-methods create
      importing
        !i_country    type banks default 'RU'
        !i_key        type bankk
        !i_commit     type abap_bool default abap_false
        !i_updatetask type abap_bool default abap_false
        !is_address   type bapi1011_address
          preferred parameter i_country
      returning
        value(ev_key) type bankk
      raising
        zcx_generic .
    class-methods change
      importing
        !i_country    type banks default 'RU'
        !i_key        type bankk
        !i_commit     type abap_bool default abap_false
        !i_updatetask type abap_bool default abap_false
        !is_address   type bapi1011_address
      raising
        zcx_generic .
  protected section.
*"* protected components of class ZCLSRM_BANK
*"* do not include other source files here!!!
  private section.
*"* private components of class ZCLSRM_BANK
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCL_BANK_STATIC IMPLEMENTATION.


  method change.

    data:
      ls_addressx type bapi1011_addressx,
      ls_return   type bapiret2.

    clear ls_addressx with abap_true.

    call function 'BAPI_BANK_CHANGE'
      exporting
        bankcountry   = i_country
        bankkey       = i_key
        bank_address  = is_address
        bank_addressx = ls_addressx
      importing
        return        = ls_return.

    if ls_return-type ca 'EAX'.
      zcx_generic=>raise( is_return = ls_return ).
    endif.

    if i_commit eq abap_true.
      zcl_abap_static=>commit( ).
    endif.

  endmethod.


  method create.

    data ls_return type bapiret2.
    call function 'BAPI_BANK_CREATE'
      exporting
        bank_ctry    = i_country
        bank_key     = i_key
        bank_address = is_address
      importing
        return       = ls_return
        bankkey      = ev_key.

    if ls_return-type ca 'EAX'.
      zcx_generic=>raise( is_return = ls_return ).
    endif.

    if i_commit eq abap_true.
      zcl_abap_static=>commit( ).
    endif.

  endmethod.
ENDCLASS.