class YCL_AIM_USERDATA definition
  public
  create protected .

public section.

  class-methods GET_INSTANCE
    returning
      value(RO_INSTANCE) type ref to YCL_AIM_USERDATA .
  methods GET_USERDETAILS
    importing
      !IV_UNAME type UNAME
    exporting
      !ES_USERDETAILS type YAIM_USERDATA_DETAIL_ALL
    changing
      !CS_USERDETAILS_SUBSET type DATA optional .
protected section.

  class-data GO_INSTANCE type ref to YCL_AIM_USERDATA .
private section.
ENDCLASS.



CLASS YCL_AIM_USERDATA IMPLEMENTATION.


METHOD get_instance.
  IF go_instance IS INITIAL.
    CREATE OBJECT go_instance.
  ENDIF.

  ro_instance = go_instance.
ENDMETHOD.


METHOD get_userdetails.

    DATA ls_address TYPE bapiaddr3.
    DATA ls_company TYPE bapiuscomp.
    DATA lt_return  TYPE TABLE OF bapiret2.
    DATA lt_tel     TYPE TABLE OF bapiadtel.
    DATA ls_tel     TYPE bapiadtel.

    CLEAR es_userdetails.

    CALL FUNCTION 'BAPI_USER_GET_DETAIL'
      EXPORTING
        username = iv_uname
      IMPORTING
        address  = ls_address
        company  = ls_company
      TABLES
        addtel   = lt_tel
        return   = lt_return.
    IF lt_return IS INITIAL.
      MOVE-CORRESPONDING ls_address TO es_userdetails.

      READ TABLE lt_tel INTO ls_tel INDEX 1.
      IF sy-subrc = 0.
        es_userdetails-country = ls_tel-countryiso.
        es_userdetails-tel1_numbr = ls_tel-telephone.
      ENDIF.

      es_userdetails-formatted_full_name = |{ es_userdetails-firstname } { es_userdetails-lastname }|.

    ENDIF.

    IF cs_userdetails_subset IS REQUESTED.
      MOVE-CORRESPONDING es_userdetails TO cs_userdetails_subset.
    ENDIF.
  ENDMETHOD.
ENDCLASS.