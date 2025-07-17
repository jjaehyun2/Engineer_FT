class ZCL_USER_STATIC definition
  public
  final
  create public .

*"* public components of class ZCL_USER_STATIC
*"* do not include other source files here!!!
public section.
  type-pools ABAP .

  constants WFBATCH type UNAME value 'WF-BATCH' ##NO_TEXT.

  class-methods IS_EXIST
    importing
      !I_USER type SIMPLE
    returning
      value(E_EXIST) type ABAP_BOOL .
  class-methods GET_NAME
    importing
      !I_USER type SIMPLE default SY-UNAME
    returning
      value(E_NAME) type STRING
    raising
      ZCX_GENERIC .
  class-methods GET_EMAIL
    importing
      !I_USER type SIMPLE default SY-UNAME
    preferred parameter I_USER
    returning
      value(E_MAIL) type STRING
    raising
      ZCX_GENERIC .
  class-methods GET_ROLES
    importing
      !I_USER type UNAME default SY-UNAME
      !I_DATE type SY-DATLO optional
    returning
      value(ET_ROLES) type RSSBR_T_BADI_BAPIAGR .
  class-methods GET_FUNCTION
    importing
      !I_USER type UNAME default SY-UNAME
    returning
      value(E_FUNCTION) type STRING
    raising
      ZCX_GENERIC .
  class-methods GET_EMPLOYEE
    importing
      !I_USER type UNAME default SY-UNAME
    preferred parameter I_USER
    returning
      value(E_EMPLOYEE_ID) type GUID
    raising
      ZCX_GENERIC .
  class-methods GET_TIME_ZONE
    importing
      !I_USER type SIMPLE
    returning
      value(E_ZONE) type TZNZONE .
  class-methods GET_PARTNER
    importing
      !I_ID type SIMPLE default SY-UNAME
    returning
      value(E_ID) type BU_PARTNER .
  class-methods GET_WORKPLACES
    importing
      !I_USER type UNAME default SY-UNAME
    exporting
      value(ET_WORKPLACES) type TABLE
    raising
      ZCX_GENERIC .
  class-methods GET_ORG
    importing
      !I_USER type UNAME default SY-UNAME
    returning
      value(E_ORG) type HROBJID
    raising
      ZCX_GENERIC .
  class-methods GET_GROUP
    importing
      !I_USER type UNAME default SY-UNAME
    preferred parameter I_USER
    returning
      value(E_GROUP) type HROBJID
    raising
      ZCX_GENERIC .
  class-methods IS_DEVELOPER
    importing
      !I_USER type UNAME default SY-UNAME
    returning
      value(E_IS) type ABAP_BOOL .
  class-methods IS_PURCHASER
    importing
      !I_USER type UNAME default SY-UNAME
    preferred parameter I_USER
    returning
      value(E_PURCHASER) type ABAP_BOOL .
  class-methods IS_BIDDER
    importing
      !I_USER type UNAME default SY-UNAME
    preferred parameter I_USER
    returning
      value(E_BIDDER) type ABAP_BOOL .
  class-methods GET_USER_BY_EMAIL
    importing
      !I_EMAIL type SIMPLE
    returning
      value(E_USER) type UNAME .
  protected section.
*"* protected components of class ZCL_USER_STATIC
*"* do not include other source files here!!!
  private section.
*"* private components of class ZCL_USER_STATIC
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCL_USER_STATIC IMPLEMENTATION.


  method get_email.

    if i_user is initial.
      return.
    endif.

    try.
        zcl_cache_static=>get_data(
          exporting
            i_name = 'ZCLSRM_USER_STATIC=>GET_EMAIL'
            i_id   = i_user
          importing
            e_data = e_mail ).
        return.
      catch cx_root.
    endtry.

    data l_user type uname.
    l_user = i_user.

    data lt_return type bapiret2_t.
    data ls_address type bapiaddr3.
    call function 'BAPI_USER_GET_DETAIL'
      exporting
        username = l_user
      importing
        address  = ls_address
      tables
        return   = lt_return.

    loop at lt_return transporting no fields
      where
        type ca 'EAX'.
      zcx_generic=>raise(
        it_return = lt_return ).
    endloop.

    e_mail = ls_address-e_mail.

    zcl_cache_static=>set_data(
      i_name = 'ZCLSRM_USER_STATIC=>GET_EMAIL'
      i_id   = i_user
      i_data = e_mail ).

  endmethod.


  method get_employee.

***    call function 'BBP_PDH_GET_PARTNERS_FROM_USER'
***      exporting
***        i_user_name               = i_user
***        i_reltype                 = /sapsrm/if_pdo_bupa_c=>gc_is_employee
***      importing
***        e_partner_guid            = e_employee_id
***      exceptions
***        relationtype_not_permitted = 1
***        no_partner_data_for_user   = 2
***        no_org_found               = 3
***        others                     = 4.
***    if sy-subrc ne 0.
***      zcx_generic=>raise( ).
***    endif.

  endmethod.


  method get_function.

    try.
        zcl_cache_static=>get_data(
          exporting i_name = 'ZCLSRM_USER_STATIC=>GET_FUNCTION'
                    i_id   = i_user
          importing e_data = e_function ).
        return.
      catch cx_root.
    endtry.

    data lt_return type bapiret2_t.
    data ls_address type bapiaddr3.
    call function 'BAPI_USER_GET_DETAIL'
      exporting
        username = i_user
      importing
        address  = ls_address
      tables
        return   = lt_return.

    loop at lt_return transporting no fields
      where type ca 'EAX'.
      zcx_generic=>raise( it_return = lt_return ).
    endloop.

    e_function = ls_address-function.

    zcl_cache_static=>set_data(
      i_name = 'ZCLSRM_USER_STATIC=>GET_FUNCTION'
      i_id   = i_user
      i_data = e_function ).

  endmethod.


  method get_group.

***    data ls_grp type bbps_sh_res_keyval.
***    call function 'BBP_OM_FIND_RESP_ORG_EXT'
***      exporting
***        i_language = 'RU'
***        i_user_id  = i_user
***      importing
***        es_pur_grp = ls_grp.
***
***    if ls_grp is initial.
***      message e002 with i_user into dummy.
***      zcx_generic=>raise( ).
***    endif.
***
***    e_group = ls_grp-res_key+2.

  endmethod.


  method get_name.

    if i_user is initial.
      return.
    endif.

    try.
        zcl_cache_static=>get_data(
          exporting
            i_name = 'ZCLSRM_USER_STATIC=>GET_NAME'
            i_id   = i_user
          importing
            e_data = e_name ).
        return.
      catch cx_root.
    endtry.

    data l_user type uname.
    l_user = i_user.

    data lt_return type bapiret2_t.
    data ls_address type bapiaddr3.
    call function 'BAPI_USER_GET_DETAIL'
      exporting
        username = l_user
      importing
        address  = ls_address
      tables
        return   = lt_return.

    data ls_return like line of lt_return.
    loop at lt_return transporting no fields
      where
        type ca 'EAX'.
      zcx_generic=>raise(
        it_return = lt_return ).
    endloop.

    concatenate ls_address-firstname ls_address-middlename ls_address-lastname
      into e_name separated by space.

    zcl_cache_static=>set_data(
      i_name = 'ZCLSRM_USER_STATIC=>GET_NAME'
      i_id   = i_user
      i_data = e_name ).

  endmethod.


  method get_org.

***    data ls_org type bbps_sh_res_keyval.
***    call function 'BBP_OM_FIND_RESP_ORG_EXT'
***      exporting
***        i_language = 'RU'
***        i_user_id  = i_user
***      importing
***        es_pur_org  = ls_org.
***
***    if ls_org is initial.
***      message e003 with i_user into dummy.
***      zcx_generic=>raise( ).
***    endif.
***
***    e_org = ls_org-res_key+2.

  endmethod.


  method get_partner.

    data lt_user type table of usselmodbe.
    zcl_abap_static=>table2table(
      exporting it_data = zcl_abap_static=>value2range( i_id )
      importing et_data = lt_user ).

    data lt_partners type bu_partner_t.
    call function 'BP_BUPA_SEARCH_BY_USER'
      exporting
        maxrows    = 1
      importing
        et_partner = lt_partners
      tables
        ir_user    = lt_user.

    data ls_partner like line of lt_partners.
    read table lt_partners into ls_partner index 1.

    e_id = ls_partner-partner.

  endmethod.


  method get_roles.

    try.
        zcl_cache_static=>get_data(
          exporting
            i_name = 'ZCLSRM_USER_STATIC=>GET_ROLES'
            i_id   = i_user
          importing
            e_data = et_roles ).
        return.
      catch cx_root.
    endtry.

    data lt_roles type standard table of bapiagr.
    data lt_return type standard table of bapiret2.
    call function 'BAPI_USER_GET_DETAIL'
      exporting
        username       = i_user
      tables
        activitygroups = et_roles
        return         = lt_return.

    delete et_roles
      where
        not ( from_dat le i_date and
              to_dat   gt i_date ).

    zcl_cache_static=>set_data(
      i_name = 'ZCLSRM_USER_STATIC=>GET_ROLES'
      i_id   = i_user
      i_data = et_roles ).

  endmethod.


  method get_time_zone.

    data l_user	type uname.
    l_user = i_user.

    data lt_return  type bapiret2_t.
    data ls_address type bapiaddr3.
    call function 'BAPI_USER_GET_DETAIL'
      exporting
        username = l_user
      importing
        address  = ls_address
      tables
        return   = lt_return.

    e_zone = ls_address-time_zone.

  endmethod.


  method get_user_by_email.

    check i_email is not initial.

    data lt_selection_range type table of bapiussrge.
    field-symbols <ls_selection_range> like line of lt_selection_range.
    append initial line to lt_selection_range assigning <ls_selection_range>.
    <ls_selection_range>-parameter = 'ADDRESS'.
    <ls_selection_range>-field     = 'E_MAIL'.
    <ls_selection_range>-sign      = 'I'.
    <ls_selection_range>-option    = 'EQ'.
    <ls_selection_range>-low       = i_email.

    data lt_list type table of bapiusname.
    call function 'BAPI_USER_GETLIST'
      tables
        selection_range = lt_selection_range
        userlist        = lt_list.

    data ls_list like line of lt_list.
    read table lt_list into ls_list index 1.

    e_user = ls_list-username.

  endmethod.


  method get_workplaces.

***  data ls_select type bbps_um_ui_tblselect.
***  ls_select-employee_guid = get_employee( i_user ).
***
***  call function 'BBP_UM_UI_GET_POSITIONS'
***    exporting
***      is_select_line = ls_select
***    importing
***      et_workplaces  = et_workplaces.

  endmethod.


  method is_bidder.

***  if /sapsrm/cl_pdo_rfq_util=>get_user_role( i_user ) eq /sapsrm/if_pdo_bid_const=>c_role_bidder.
***    e_bidder = abap_true.
***  endif.

  endmethod.


  method is_developer.

    data l_user type uname.
    select single uname
      from devaccess
      into l_user
      where uname eq i_user.
    if sy-subrc eq 0.
      e_is = abap_true.
    endif.

  endmethod.


  method is_exist.

    data l_user type uname.
    l_user = i_user.

    data ls_return type bapiret2.
    call function 'BAPI_USER_EXISTENCE_CHECK'
      exporting
        username = l_user
      importing
        return   = ls_return.

    if ls_return-number eq '088'.
      e_exist = abap_true.
    endif.

  endmethod.


  method is_purchaser.

***  if /sapsrm/cl_pdo_rfq_util=>get_user_role( i_user ) eq /sapsrm/if_pdo_bid_const=>c_role_purchaser.
***    e_purchaser = abap_true.
***  endif.

  endmethod.
ENDCLASS.