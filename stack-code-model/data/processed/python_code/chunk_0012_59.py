CLASS zcl_abapgit_swagger DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.

    INTERFACES if_http_extension .
    INTERFACES zif_swag_handler .

    METHODS create_online_repo
      IMPORTING iv_url           TYPE        string
                iv_branch_name   TYPE        string
                iv_package       TYPE        devclass
      RETURNING VALUE(rs_checks) TYPE        zif_abapgit_definitions=>ty_deserialize_checks.

  PROTECTED SECTION.
  PRIVATE SECTION.
ENDCLASS.



CLASS ZCL_ABAPGIT_SWAGGER IMPLEMENTATION.


  METHOD create_online_repo.


    DATA(lo_repo) = zcl_abapgit_repo_srv=>get_instance( )->new_online(
      iv_url         = iv_url
      iv_branch_name = iv_branch_name
      iv_package     = iv_package ).

    rs_checks = lo_repo->deserialize_checks( ).

  ENDMETHOD.


  METHOD if_http_extension~handle_request.

    DATA: lo_swag    TYPE REF TO zcl_swag,
          lo_handler TYPE REF TO zcl_abapgit_swagger.


    CREATE OBJECT lo_swag
      EXPORTING
        ii_server = server
        iv_title  = 'abapGit-Swagger'
        iv_base   = '/'.

    CREATE OBJECT lo_handler.
    lo_swag->register( lo_handler ).

    lo_swag->run( ).

  ENDMETHOD.


  METHOD zif_swag_handler~meta.

    FIELD-SYMBOLS: <ls_meta> LIKE LINE OF rt_meta.


    APPEND INITIAL LINE TO rt_meta ASSIGNING <ls_meta>.
    <ls_meta>-summary   = 'create online repo'.
    <ls_meta>-url-regex = '/(\w*)/'.
*    APPEND 'IV_FOO' TO <ls_meta>-url-group_names.
    <ls_meta>-method    = zcl_swag=>c_method-post.
    <ls_meta>-handler   = 'CREATE_ONLINE_REPO'.

  ENDMETHOD.
ENDCLASS.