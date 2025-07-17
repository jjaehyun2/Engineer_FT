class zcl_ftp_client definition
  public
  final
  create public .

  public section.
    type-pools abap .

    data dest type rfcdest .
    data handle type i read-only .
    data local type abap_bool read-only .
    data host type string read-only .
    data user type string read-only .
    data password type string read-only .

    methods constructor
      importing
        !i_host     type simple optional
        !i_user     type simple optional
        !i_password type simple optional
        !i_local    type abap_bool default abap_false .
    methods connect
      importing
        !i_host     type simple optional
        !i_user     type simple optional
        !i_password type simple optional
      raising
        zcx_generic .
    methods disconnect
      raising
        zcx_generic .
    methods are_files_exist
      importing
        !i_path     type simple
      returning
        value(e_is) type abap_bool
      raising
        zcx_generic .
    methods get_files
      importing
        !i_path        type simple
      returning
        value(et_list) type stringtab
      raising
        zcx_generic .
    methods delete_files
      importing
        !i_path type simple
      raising
        zcx_generic .
    methods is_file_exist
      importing
        !i_path     type simple
        !i_name     type simple
      returning
        value(e_is) type abap_bool
      raising
        zcx_generic .
    methods get_file
      importing
        !i_path       type simple
      returning
        value(e_data) type xstring
      raising
        zcx_generic .
    methods create_file
      importing
        !i_path type simple
        !i_data type xstring
      raising
        zcx_generic .
    methods delete_file
      importing
        !i_path type simple
      raising
        zcx_generic .
    methods copy_file
      importing
        !i_from type simple
        !i_to   type simple
      raising
        zcx_generic .
    methods move_file
      importing
        !i_from type simple
        !i_to   type simple
      raising
        zcx_generic .
    methods is_directories_exist
      importing
        !i_path     type simple
      returning
        value(e_is) type abap_bool
      raising
        zcx_generic .
    methods get_directories
      importing
        !i_path        type simple
      returning
        value(et_list) type stringtab
      raising
        zcx_generic .
    methods delete_directories
      importing
        !i_path type simple
      raising
        zcx_generic .
    methods is_directory_exist
      importing
        !i_path     type simple
        !i_name     type simple
      returning
        value(e_is) type abap_bool
      raising
        zcx_generic .
    methods create_directory
      importing
        !i_path type simple
      raising
        zcx_generic .
    methods delete_directory
      importing
        !i_path type simple
      raising
        zcx_generic .
  protected section.
  private section.

    methods command
      importing
        !i_command     type simple
      returning
        value(et_data) type stringtab
      raising
        zcx_generic .
ENDCLASS.



CLASS ZCL_FTP_CLIENT IMPLEMENTATION.


  method are_files_exist.

    data lt_list type stringtab.
    lt_list = get_files( i_path ).

    check lt_list is not initial.

    e_is = abap_true.

  endmethod.


  method command.

    data l_command(255).
    l_command = i_command.

    data lt_data type table of text255.
    call function 'FTP_COMMAND'
      exporting
        handle        = handle
        command       = l_command
        compress      = 'N'
      tables
        data          = lt_data
      exceptions
        tcpip_error   = 1
        command_error = 2
        data_error    = 3.
    if sy-subrc ne 0.
      zcx_generic=>raise( ).
    endif.

    zcl_abap_static=>list2list(
      exporting it_data = lt_data
      importing et_data = et_data ).

  endmethod.


  method connect.

    if i_host is initial.
      data l_host(255).
      l_host = host.
    else.
      l_host = i_host.
    endif.

    if i_user is initial.
      data l_user(255).
      l_user = user.
    else.
      l_user = i_user.
    endif.

    if i_password is initial.
      data l_password(255).
      l_password = password.
    else.
      l_password = i_password.
    endif.

    if l_user is initial.
      l_user     = 'anonymous'.
      l_password = 'anonymous'.
    endif.

    data l_length type i.
    l_length = strlen( l_password ).

    call function 'HTTP_SCRAMBLE'
      exporting
        source      = l_password
        sourcelen   = l_length
        key         = '26101957'
      importing
        destination = l_password.

    call function 'FTP_CONNECT'
      exporting
        host            = l_host
        user            = l_user
        password        = l_password
        rfc_destination = dest
      importing
        handle          = handle
      exceptions
        not_connected   = 1
        others          = 2.
    if sy-subrc ne 0.
      zcx_generic=>raise( ).
    endif.

    command( 'set passive on' ).

  endmethod.


  method constructor.

    host     = i_host.
    user     = i_user.
    password = i_password.

    if i_local eq abap_true.
      dest = 'SAPFTP'.
    else.
      dest = 'SAPFTPA'.
    endif.

  endmethod.


  method copy_file.

    data l_data type xstring.
    l_data = get_file( i_from ).

    create_file(
      i_path = i_to
      i_data = l_data ).

  endmethod.


  method create_directory.

    data lt_result type stringtab.
    lt_result = command( `mkdir ` && i_path ).

  endmethod.


  method create_file.

    data l_file(255).
    l_file = i_path.

    data l_length type i.
    l_length = xstrlen( i_data ).

    data lt_data type table of raw255.
    zcl_convert_static=>xtext2xtable(
      exporting i_data  = i_data
      importing et_data = lt_data ).

    call function 'FTP_R3_TO_SERVER'
      exporting
        handle        = handle
        fname         = l_file
        blob_length   = l_length
      tables
        blob          = lt_data
      exceptions
        tcpip_error   = 1
        command_error = 2
        data_error    = 3
        others        = 4.
    if sy-subrc ne 0.
      zcx_generic=>raise( ).
    endif.

  endmethod.


  method delete_directories.

    data lt_list type stringtab.
    lt_list = get_directories( i_path ).

    data l_directory like line of lt_list.
    loop at lt_list into l_directory.

      delete_directory( i_path && `/` && l_directory ).

    endloop.

  endmethod.


  method delete_directory.

    " Удаление всех директорий
    delete_directories( i_path ).

    " Удаление всех файлов
    delete_files( i_path ).

    data lt_result type stringtab.
    lt_result = command( `rmdir ` && i_path ).

  endmethod.


  method delete_file.

    data lt_result type stringtab.
    lt_result = command( `delete ` && i_path ).

  endmethod.


  method delete_files.

    data lt_list type stringtab.
    lt_list = get_files( i_path ).

    data l_file like line of lt_list.
    loop at lt_list into l_file.

      delete_file( i_path && `/` && l_file ).

    endloop.

  endmethod.


  method disconnect.

    check handle is not initial.

    call function 'FTP_DISCONNECT'
      exporting
        handle = handle.

    call function 'RFC_CONNECTION_CLOSE'
      exporting
        destination = dest
      exceptions
        others      = 1.

  endmethod.


  method get_directories.

    data lt_result type stringtab.
    lt_result = command( `ls ` && i_path ).

    "drw-rw-r--    1 572      572           252 Oct 11  2012 dirname

    data l_result like line of lt_result.
    loop at lt_result into l_result.

      check l_result(1) eq 'd'.

      condense l_result.

      data lt_data type table of string.
      clear lt_data.
      split l_result at space into table lt_data.

      data l_index type i.
      l_index = lines( lt_data ).

      data l_data like line of lt_data.
      read table lt_data into l_data index l_index.
      check sy-subrc eq 0.

      check
        l_data ne '.' and
        l_data ne '..'.

      insert l_data into table et_list.

    endloop.

  endmethod.


  method get_file.

    data l_file(255).
    l_file = i_path.

    data l_length type i.
    data lt_data type table of raw255.
    call function 'FTP_SERVER_TO_R3'
      exporting
        handle        = handle
        fname         = l_file
      importing
        blob_length   = l_length
      tables
        blob          = lt_data
      exceptions
        tcpip_error   = 1
        command_error = 2
        data_error    = 3
        others        = 4.
    if sy-subrc ne 0.
      zcx_generic=>raise( ).
    endif.

    e_data =
      zcl_convert_static=>xtable2xtext(
        i_length = l_length
        it_data  = lt_data ).

  endmethod.


  method get_files.

    data lt_result type stringtab.
    lt_result = command( `ls ` && i_path ).

    "-rw-rw-r--    1 572      572           252 Oct 11  2012 file.zip

    data l_result like line of lt_result.
    loop at lt_result into l_result.

      check l_result(1) eq '-'.

      condense l_result.

      data lt_data type table of string.
      clear lt_data.
      split l_result at space into table lt_data.

      data l_index type i.
      l_index = lines( lt_data ).

      data l_data like line of lt_data.
      read table lt_data into l_data index l_index.
      check sy-subrc eq 0.

      insert l_data into table et_list.

    endloop.

  endmethod.


  method is_directories_exist.

    data lt_list type stringtab.
    lt_list = get_directories( i_path ).

    check lt_list is not initial.

    e_is = abap_true.

  endmethod.


  method is_directory_exist.

    data lt_list type stringtab.
    lt_list = get_directories( i_path ).

    read table lt_list transporting no fields
      with key
        table_line = i_name.
    check sy-subrc eq 0.

    e_is = abap_true.

  endmethod.


  method is_file_exist.

    data lt_list type stringtab.
    lt_list = get_files( i_path ).

    read table lt_list transporting no fields
      with key
        table_line = i_name.
    check sy-subrc eq 0.

    e_is = abap_true.

  endmethod.


  method move_file.

    copy_file(
      i_from = i_from
      i_to   = i_to ).

    delete_file( i_from ).

  endmethod.
ENDCLASS.