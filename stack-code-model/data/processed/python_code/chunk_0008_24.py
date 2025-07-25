INTERFACE zif_abapgit_exit PUBLIC.

  TYPES:
    BEGIN OF ty_tadir,
      pgmid    TYPE tadir-pgmid,
      object   TYPE tadir-object,
      obj_name TYPE tadir-obj_name,
      devclass TYPE tadir-devclass,
      korrnum  TYPE tadir-korrnum,
      path     TYPE string,
    END OF ty_tadir,
    ty_tadir_tt      TYPE STANDARD TABLE OF ty_tadir WITH DEFAULT KEY,
    ty_icm_sinfo2_tt TYPE STANDARD TABLE OF icm_sinfo2 WITH DEFAULT KEY.

  METHODS:
    change_local_host
      CHANGING ct_hosts TYPE ty_icm_sinfo2_tt,
    allow_sap_objects
      RETURNING VALUE(rv_allowed) TYPE abap_bool,
    change_proxy_url
      IMPORTING iv_repo_url TYPE csequence
      CHANGING  c_proxy_url TYPE string,
    change_proxy_port
      IMPORTING iv_repo_url  TYPE csequence
      CHANGING  c_proxy_port TYPE string,
    change_proxy_authentication
      IMPORTING iv_repo_url            TYPE csequence
      CHANGING  c_proxy_authentication TYPE abap_bool,
    http_client
      IMPORTING
        ii_client TYPE REF TO if_http_client,
    change_tadir
      IMPORTING
        iv_package TYPE devclass
        io_log     TYPE REF TO zcl_abapgit_log
      CHANGING
        ct_tadir   TYPE ty_tadir_tt.

ENDINTERFACE.