class ZCL_ARCHIV_STATIC definition
  public
  final
  create public .

*"* public components of class ZCL_ARCHIV_STATIC
*"* do not include other source files here!!!
public section.

  types:
    begin of ts_link,
        repository_id type toa02-archiv_id,
        document_id   type toa02-arc_doc_id,
        document_type type toa02-reserve,
      end of ts_link .

  class-methods GET_LINK
    importing
      !I_ID type SIMPLE
    returning
      value(ES_LINK) type TS_LINK
    raising
      ZCX_GENERIC .
  class-methods CREATE_LINK
    importing
      !I_OBJECT type SIMPLE
      !I_DATA type XSTRING
      !I_REF_OBJECT type SIMPLE
      !I_REF_ID type SIMPLE
    returning
      value(ES_LINK) type TS_LINK
    raising
      ZCX_GENERIC .
  class-methods UPDATE_LINK
    importing
      !IS_LINK type TS_LINK
      !I_DATA type XSTRING
    raising
      ZCX_GENERIC .
  class-methods READ
    importing
      !IS_LINK type TS_LINK
    returning
      value(E_DATA) type XSTRING
    raising
      ZCX_GENERIC .
  class-methods IS_LOCAL
    importing
      !I_GUID type SIMPLE
    returning
      value(E_IS) type ABAP_BOOL .
  class-methods GET_LOCAL_ID
    importing
      !I_GUID type SIMPLE
    returning
      value(E_ID) type STRING
    raising
      ZCX_GENERIC .
  class-methods GET_CHANGED_AT
    importing
      value(IS_LINK) type TS_LINK
    returning
      value(E_TIME) type TIMESTAMP
    raising
      ZCX_GENERIC .
protected section.
*"* protected components of class ZCLSRM_ARCHIVE_LINK_STATIC
*"* do not include other source files here!!!
private section.
*"* private components of class ZCL_ARCHIV_STATIC
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCL_ARCHIV_STATIC IMPLEMENTATION.


method CREATE_LINK.

  data l_object type toaom-ar_object.
  l_object = i_object.

  data l_length type sapb-length.
  l_length = xstrlen( i_data ).

  data l_ref_object type toaom-sap_object.
  l_ref_object = i_ref_object.

  data l_ref_id type sapb-sapobjid.
  l_ref_id = i_ref_id.

  data ls_doc type toadt.
  call function 'ARCHIV_CREATE_TABLE'
    exporting
      ar_object                = l_object
      object_id                = l_ref_id
      sap_object               = l_ref_object
      flength                  = l_length
      doc_type                 = 'BIN'
      document                 = i_data
    importing
      outdoc                   = ls_doc
    exceptions
      error_archiv             = 1
      error_communicationtable = 2
      error_connectiontable    = 3
      error_kernel             = 4
      error_parameter          = 5
      error_user_exit          = 6
      error_mandant            = 7
      others                   = 8.
  if sy-subrc ne 0.
    zcx_generic=>raise( ).
  endif.

  es_link-repository_id = ls_doc-contrep_id.
  es_link-document_id   = ls_doc-arc_doc_id.
  es_link-document_type = ls_doc-doc_class.

endmethod.


method GET_CHANGED_AT.

  data l_doc_id type sapb-sapadokid.
  l_doc_id = is_link-document_id.

  data l_doc_type type toaar-archiv_id.
  l_doc_type = is_link-document_type.

  data lt_components type table of components.
  call function 'ARCHIVOBJECT_STATUS'
    exporting
      archiv_doc_id            = l_doc_id
      archiv_id                = l_doc_type
    tables
      al_components            = lt_components
    exceptions
      error_archiv             = 1
      error_communicationtable = 2
      error_kernel             = 3
      others                   = 4.
  if sy-subrc <> 0.
    zcx_generic=>raise( ).
  endif.

  data ls_conponent like line of lt_components.
  loop at lt_components into ls_conponent
    where compid eq 'data'.

    data l_time like e_time.
    l_time =
      zcl_time_static=>get_timestamp(
        i_date = ls_conponent-compdatem
        i_time = ls_conponent-comptimem
        i_zone = zcl_time_static=>tz_utc ).

    if e_time lt l_time.
      e_time = l_time.
    endif.

  endloop.
  if sy-subrc ne 0.
    zcx_generic=>raise( ).
  endif.

endmethod.


method get_link.

  data ls_toa02 type toa02.
  select single * from toa02 into ls_toa02
    where object_id eq i_id.
  if sy-subrc ne 0.
    zcx_generic=>raise( ).
  endif.

  es_link-repository_id = ls_toa02-archiv_id.
  es_link-document_id   = ls_toa02-arc_doc_id.
  es_link-document_type = ls_toa02-reserve.

endmethod.


method GET_LOCAL_ID.

  data ls_toa02 type toa02.
  select single * from toa02 into ls_toa02
    where arc_doc_id eq i_guid.

  e_id = ls_toa02-object_id.

endmethod.


method IS_LOCAL.

  data ls_toa02 type toa02.
  select single * from toa02 into ls_toa02
    where arc_doc_id eq i_guid.
  if sy-subrc eq 0.
    e_is = abap_true.
  endif.

endmethod.


method READ.

  data ls_doc type toadt.
  ls_doc-contrep_id = is_link-repository_id.
  ls_doc-arc_doc_id = is_link-document_id.
  ls_doc-doc_class  = is_link-document_type.

  data l_length type sapb-length.
  data lt_data type table of tbl1024.
  call function 'ARCHIVOBJECT_GET_TABLE'
    exporting
      archiv_id                = ls_doc-contrep_id
      document_type            = ls_doc-doc_class
      archiv_doc_id            = ls_doc-arc_doc_id
    importing
      binlength                = l_length
    tables
      binarchivobject          = lt_data
    exceptions
      error_archiv             = 1
      error_communicationtable = 2
      error_kernel             = 3
      others                   = 4.
  if sy-subrc ne 0.
    zcx_generic=>raise( ).
  endif.

  e_data =
    zcl_convert_static=>xtable2xtext(
      i_length = l_length
      it_data  = lt_data ).

endmethod.


method UPDATE_LINK.

  data l_archive_id type toaar-archiv_id.
  l_archive_id = is_link-repository_id.

  data l_archivedoc_id type toav0-arc_doc_id.
  l_archivedoc_id = is_link-document_id.

  data l_doc_class type toadd-doc_type.
  l_doc_class = is_link-document_type.

  data l_length type sapb-length.
  l_length = xstrlen( i_data ).

  data lt_data type table of tbl1024.
  zcl_convert_static=>xtext2xtable(
    exporting i_data = i_data
    importing et_data = lt_data ).

  call function 'ARCHIVOBJECT_UPDATE'
    exporting
      archive_id      = l_archive_id
      archivedoc_id   = l_archivedoc_id
      documentclass   = l_doc_class
      length          = l_length
      compid          = 'data'
    tables
      binarchivobject = lt_data
    exceptions
      error_archiv    = 1
      others          = 2.
  if sy-subrc ne 0.
    zcx_generic=>raise( ).
  endif.

endmethod.
ENDCLASS.