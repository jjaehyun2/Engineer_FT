class cl_gui_frontend_services definition public.

  public section.

    constants hkey_classes_root type i value 0 ##NO_TEXT.
    constants hkey_current_user type i value 1 ##NO_TEXT.
    constants hkey_local_machine type i value 2 ##NO_TEXT.
    constants hkey_users type i value 3 ##NO_TEXT.
    constants platform_unknown type i value -1 ##NO_TEXT.
    constants platform_windows95 type i value 1 ##NO_TEXT.
    constants platform_windows98 type i value 2 ##NO_TEXT.
    constants platform_nt351 type i value 3 ##NO_TEXT.
    constants platform_nt40 type i value 4 ##NO_TEXT.
    constants platform_nt50 type i value 5 ##NO_TEXT.
    constants platform_mac type i value 6 ##NO_TEXT.
    constants platform_os2 type i value 7 ##NO_TEXT.
    constants platform_linux type i value 8 ##NO_TEXT.
    constants platform_hpux type i value 9 ##NO_TEXT.
    constants platform_tru64 type i value 10 ##NO_TEXT.
    constants platform_aix type i value 11 ##NO_TEXT.
    constants platform_solaris type i value 12 ##NO_TEXT.
    constants platform_macosx type i value 13 ##NO_TEXT.
    constants action_ok type i value 0 ##NO_TEXT.
    constants action_cancel type i value 9 ##NO_TEXT.
    class-data filetype_all type string read-only .
    class-data filetype_text type string read-only .
    class-data filetype_xml type string read-only .
    class-data filetype_html type string read-only .
    class-data filetype_excel type string read-only .
    class-data filetype_rtf type string read-only .
    class-data filetype_word type string read-only .
    class-data filetype_powerpoint type string read-only .
    constants platform_windowsxp type i value 14 ##NO_TEXT.
    constants action_append type i value 1 ##NO_TEXT.
    constants action_replace type i value 2 ##NO_TEXT.
    class-data guideline_classic type i value 1 ##NO_TEXT.
    class-data guideline_fiori_2 type i value 2 ##NO_TEXT.

    class-methods get_features_tab
    returning
      value(features_tab) type sfes_features_tab_type
    exceptions
      unknown_error .
    class-methods check_gui_support
    importing
      !component type string optional
      !feature_name type string optional
    returning
      value(result) type abap_bool
    exceptions
      cntl_error
      error_no_gui
      wrong_parameter
      not_supported_by_gui
      unknown_error .
    class-methods check_open_new_window
    returning
      value(result) type abap_bool .
    class-methods class_constructor .
    class-methods clipboard_export
    importing
      !no_auth_check type char01 default space
    exporting
      !data type standard table
    changing
      !rc type i
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui
      no_authority .
    class-methods clipboard_import
    exporting
      !data type standard table
      !length type i
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui .
    methods constructor
    exceptions
      not_supported_by_gui
      cntl_error .
    class-methods directory_browse
    importing
      value(window_title) type string optional
      value(initial_folder) type string optional
    changing
      !selected_folder type string
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods directory_create
    importing
      value(directory) type string
    changing
      !rc type i
    exceptions
      directory_create_failed
      cntl_error
      error_no_gui
      directory_access_denied
      directory_already_exists
      path_not_found
      unknown_error
      not_supported_by_gui
      wrong_parameter .
    class-methods directory_delete
    importing
      value(directory) type string
    changing
      !rc type i
    exceptions
      directory_delete_failed
      cntl_error
      error_no_gui
      path_not_found
      directory_access_denied
      unknown_error
      not_supported_by_gui
      wrong_parameter .
    class-methods directory_exist
    importing
      !directory type string
    returning
      value(result) type abap_bool
    exceptions
      cntl_error
      error_no_gui
      wrong_parameter
      not_supported_by_gui .
    class-methods directory_get_current
    changing
      !current_directory type string
    exceptions
      directory_get_current_failed
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods directory_list_files
    importing
      value(directory) type string
      value(filter) type string default '*.*'
      value(files_only) type abap_bool optional
      value(directories_only) type abap_bool optional
    changing
      !file_table type standard table
      !count type i
    exceptions
      cntl_error
      directory_list_files_failed
      wrong_parameter
      error_no_gui
      not_supported_by_gui .
    class-methods directory_set_current
    importing
      value(current_directory) type string
    changing
      !rc type i
    exceptions
      directory_set_current_failed
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods disablehistoryforfield
    importing
      value(fieldname) type string
      value(bdisabled) type abap_bool
    changing
      value(rc) type i
    exceptions
      field_not_found
      disablehistoryforfield_failed
      cntl_error
      unable_to_disable_field
      error_no_gui
      not_supported_by_gui .
    class-methods environment_get_variable
    importing
      value(variable) type string
    changing
      !value type string
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods environment_set_variable
    importing
      value(variable) type string
      value(value) type string
    changing
      !rc type i
    exceptions
      environment_set_failed
      cntl_error
      error_no_gui
      not_supported_by_gui
      wrong_parameter .
    class-methods execute
    importing
      value(document) type string optional
      value(application) type string optional
      value(parameter) type string optional
      value(default_directory) type string optional
      value(maximized) type string optional
      value(minimized) type string optional
      value(synchronous) type string optional
      value(operation) type string default 'OPEN'
    exceptions
      cntl_error
      error_no_gui
      bad_parameter
      file_not_found
      path_not_found
      file_extension_unknown
      error_execute_failed
      synchronous_failed
      not_supported_by_gui .
    class-methods file_copy
    importing
      value(source) type string
      value(destination) type string
      value(overwrite) type abap_bool default space
    exceptions
      cntl_error
      error_no_gui
      wrong_parameter
      disk_full
      access_denied
      file_not_found
      destination_exists
      unknown_error
      path_not_found
      disk_write_protect
      drive_not_ready
      not_supported_by_gui .
    class-methods file_delete
    importing
      value(filename) type string
    changing
      !rc type i
    exceptions
      file_delete_failed
      cntl_error
      error_no_gui
      file_not_found
      access_denied
      unknown_error
      not_supported_by_gui
      wrong_parameter .
    class-methods file_exist
    importing
      value(file) type string
    returning
      value(result) type abap_bool
    exceptions
      cntl_error
      error_no_gui
      wrong_parameter
      not_supported_by_gui .
    class-methods file_get_attributes
    importing
      !filename type string
    exporting
      !readonly type abap_bool
      !normal type abap_bool
      !hidden type abap_bool
      !archive type abap_bool
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui
      wrong_parameter
      file_get_attributes_failed .
    class-methods file_get_size
    importing
      value(file_name) type string
    exporting
      !file_size type i
    exceptions
      file_get_size_failed
      cntl_error
      error_no_gui
      not_supported_by_gui
      invalid_default_file_name .
    class-methods file_get_version
    importing
      value(filename) type string
    changing
      !version type string
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui
      wrong_parameter .
    class-methods file_open_dialog
    importing
      value(window_title) type string optional
      value(default_extension) type string optional
      value(default_filename) type string optional
      value(file_filter) type string optional
      value(with_encoding) type abap_bool optional
      value(initial_directory) type string optional
      value(multiselection) type abap_bool optional
    changing
      !file_table type filetable
      !rc type i
      !user_action type i optional
      !file_encoding type abap_encoding optional
    exceptions
      file_open_dialog_failed
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods file_save_dialog
    importing
      value(window_title) type string optional
      value(default_extension) type string optional
      value(default_file_name) type string optional
      !with_encoding type abap_bool optional
      value(file_filter) type string optional
      value(initial_directory) type string optional
      !prompt_on_overwrite type abap_bool default 'X'
    changing
      !filename type string
      !path type string
      !fullpath type string
      !user_action type i optional
      !file_encoding type abap_encoding optional
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui
      invalid_default_file_name .
    class-methods file_set_attributes
    importing
      !filename type string
      !readonly type abap_bool optional
      !normal type abap_bool optional
      !hidden type abap_bool optional
      !archive type abap_bool optional
    exporting
      !rc type i
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui
      wrong_parameter .
    class-methods get_computer_name
    changing
      !computer_name type string
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods get_desktop_directory
    changing
      !desktop_directory type string
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods get_drive_free_space_megabyte
    importing
      value(drive) type string default 'C:\'
    changing
      !free_space type string
    exceptions
      cntl_error
      get_free_space_failed
      error_no_gui
      wrong_parameter
      not_supported_by_gui .
    class-methods get_drive_type
    importing
      value(drive) type string
    changing
      !drive_type type string
    exceptions
      cntl_error
      bad_parameter
      error_no_gui
      not_supported_by_gui .
    class-methods get_file_separator
    changing
      value(file_separator) type c
    exceptions
      not_supported_by_gui
      error_no_gui
      cntl_error .
    class-methods get_free_space_for_drive
    importing
      value(drive) type string
    changing
      !free_space type i
    exceptions
      cntl_error
      get_free_space_failed
      error_no_gui
      wrong_parameter
      not_supported_by_gui .
    class-methods get_gui_properties
    changing
      !stream type string
    exceptions
      cntl_error
      get_gui_properties_failed
      error_no_gui
      wrong_parameter
      not_supported_by_gui .
    class-methods get_gui_version
    changing
      !version_table type filetable
      !rc type i
    exceptions
      get_gui_version_failed
      cant_write_version_table
      gui_no_version
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods get_ip_address
    returning
      value(ip_address) type string
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods get_lf_for_destination_gui
    changing
      !linefeed type string
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods get_platform
    returning
      value(platform) type i
    exceptions
      error_no_gui
      cntl_error
      not_supported_by_gui .
    class-methods get_sapgui_directory
    changing
      !sapgui_directory type string
    exceptions
      cntl_error
      not_supported_by_gui
      error_no_gui .
    class-methods get_sapgui_workdir
    changing
      !sapworkdir type string
    exceptions
      get_sapworkdir_failed
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods get_saplogon_encoding
    changing
      !file_encoding type abap_encoding
      !rc type i
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui
      cannot_initialize_globalstate .
    class-methods get_system_directory
    changing
      !system_directory type string
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods get_temp_directory
    changing
      !temp_dir type string
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods get_upload_download_path
    changing
      value(upload_path) type string
      value(download_path) type string
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui
      gui_upload_download_path
      upload_download_path_failed .
    class-methods get_user_name
    changing
      !user_name type string
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods get_windows_directory
    changing
      !windows_directory type string
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods gui_download
    importing
      !bin_filesize type i optional
      !filename type string
      !filetype type char10 default 'ASC'
      !append type char01 default space
      !write_field_separator type char01 default space
      !header type xstring default '00'
      !trunc_trailing_blanks type char01 default space
      !write_lf type char01 default 'X'
      !col_select type char01 default space
      !col_select_mask type char255 default space
      !dat_mode type char01 default space
      !confirm_overwrite type char01 default space
      !no_auth_check type char01 default space
      !codepage type abap_encoding default space
      !ignore_cerr type abap_bool default abap_true
      !replacement type abap_repl default '#'
      !write_bom type abap_bool default space
      !trunc_trailing_blanks_eol type char01 default 'X'
      !wk1_n_format type c default space
      !wk1_n_size type c default space
      !wk1_t_format type c default space
      !wk1_t_size type c default space
      !show_transfer_status type char01 default 'X'
      !fieldnames type standard table optional
      !write_lf_after_last_line type abap_bool default 'X'
      !virus_scan_profile type vscan_profile default '/SCET/GUI_DOWNLOAD'
    exporting
      value(filelength) type i
    changing
      !data_tab type standard table
    exceptions
      file_write_error
      no_batch
      gui_refuse_filetransfer
      invalid_type
      no_authority
      unknown_error
      header_not_allowed
      separator_not_allowed
      filesize_not_allowed
      header_too_long
      dp_error_create
      dp_error_send
      dp_error_write
      unknown_dp_error
      access_denied
      dp_out_of_memory
      disk_full
      dp_timeout
      file_not_found
      dataprovider_exception
      control_flush_error
      not_supported_by_gui
      error_no_gui .
    class-methods gui_upload
    importing
      !filename type string default space
      !filetype type char10 default 'ASC'
      !has_field_separator type char01 default space
      !header_length type i default 0
      !read_by_line type char01 default 'X'
      !dat_mode type char01 default space
      !codepage type abap_encoding default space
      !ignore_cerr type abap_bool default abap_true
      !replacement type abap_repl default '#'
      !virus_scan_profile type vscan_profile optional
    exporting
      value(filelength) type i
      value(header) type xstring
    changing
      !data_tab type standard table
      !isscanperformed type char01 default space
    exceptions
      file_open_error
      file_read_error
      no_batch
      gui_refuse_filetransfer
      invalid_type
      no_authority
      unknown_error
      bad_data_format
      header_not_allowed
      separator_not_allowed
      header_too_long
      unknown_dp_error
      access_denied
      dp_out_of_memory
      disk_full
      dp_timeout
      not_supported_by_gui
      error_no_gui .
    class-methods is_terminal_server
    returning
      value(result) type abap_bool
    exceptions
      cntl_error
      not_supported_by_gui
      error_no_gui .
    class-methods registry_delete_key
    importing
      value(root) type i
      value(key) type string
    exporting
      !rc type i
    exceptions
      cntl_error
      registry_delete_key_failed
      bad_parameter
      error_no_gui
      not_supported_by_gui .
    class-methods registry_delete_value
    importing
      value(root) type i
      value(key) type string
      value(value) type string
    exporting
      !rc type i
    exceptions
      cntl_error
      registry_delete_value_failed
      error_no_gui
      not_supported_by_gui .
    class-methods registry_get_dword_value
    importing
      value(root) type i
      value(key) type string
      value(value) type string optional
    exporting
      !reg_value type i
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods registry_get_value
    importing
      value(root) type i
      value(key) type string
      value(value) type string optional
      !no_flush type c optional
    exporting
      !reg_value type string
    exceptions
      get_regvalue_failed
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods registry_set_dword_value
    importing
      !root type i
      !key type string
      !value type string optional
      !dword_value type i
    exporting
      !rc type i
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods registry_set_value
    importing
      value(root) type i
      value(key) type string
      value(value_name) type string optional
      value(value) type string
    exporting
      !rc type i
    exceptions
      registry_error
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods get_screenshot
    exporting
      value(mime_type_str) type string
      value(image) type xstring
    exceptions
      access_denied
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods raise_scripting_event
    importing
      value(params) type string
    exceptions
      registry_error
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods is_scripting_active
    returning
      value(result) type i
    exceptions
      cntl_error
      not_supported_by_gui
      error_no_gui .
    class-methods show_document
    importing
      !document_name type string
      !mime_type type string
      !data_length type i
      !keep_file type xflag optional
    exporting
      !temp_file_path type string
    changing
      !document_data type standard table
    exceptions
      cntl_error
      error_no_gui
      bad_parameter
      error_writing_data
      error_starting_viewer
      unknown_mime_type
      not_supported_by_gui
      access_denied
      no_authority .
    class-methods typeahead_export
    importing
      !data type standard table
    exceptions
      cntl_error
      error_no_gui
      not_supported_by_gui .
    class-methods check_ui_guideline
    importing
      !guideline type i
    returning
      value(result) type abap_bool .
endclass.

class cl_gui_frontend_services implementation.

endclass.