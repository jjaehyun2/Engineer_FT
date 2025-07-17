class ZCL_WORD_MAILMERGE definition
  public
  final
  create public .

public section.

  constants GC_MESSAGE_CLASS type ARBGB value 'ZWORD_MAILMERGE'. "#EC NOTEXT

  methods CONSTRUCTOR
    importing
      !I_WORD_DATA type ZTWORD_DATA
      !I_TEMPLATE_FILE type RLGRAP-FILENAME
      !I_MIDDLE_FILENAME type RLGRAP-FILENAME optional
      !I_DOWNLOAD_PATH type RLGRAP-FILENAME
    exceptions
      FILE_DO_NOT_EXIST .
  methods PRINT_DOCUMENT
    exceptions
      ERROR_DOWNLOAD_FILE .
protected section.
private section.

  data GV_MIDDLE_FULLPATH type STRING .
  data GV_MIDDLE_FILENAME type RLGRAP-FILENAME .
  data GV_DOWNLOAD_PATH type RLGRAP-FILENAME .
  data GV_TOTAL_COLUMNS type I .
  data GV_TOTAL_ROWS type I .
  data GV_TEMPLATE_FILE type RLGRAP-FILENAME .
  data GT_DOWNLOAD type AXT_STRINGTAB .
  type-pools OLE2 .
  data GO_WORDOBJ type OLE2_OBJECT .
  data GO_WORDAPP type OLE2_OBJECT .
  data GO_WORDDOC type OLE2_OBJECT .
  data GO_DOCUMENTS type OLE2_OBJECT .

  methods DELETE_FILE
    importing
      !I_FILENAME type STRING .
  methods CREATE_MIDDLE_FILE
    exceptions
      ERROR_DOWNLOAD .
  methods GET_WORD_VERSION
    returning
      value(E_WORD_VERSION) type INTEGER .
ENDCLASS.



CLASS ZCL_WORD_MAILMERGE IMPLEMENTATION.


METHOD constructor.

  CONSTANTS lc_tab TYPE string VALUE cl_abap_char_utilities=>horizontal_tab.

  DATA: lv_hstr(1024) TYPE c,
        lv_position   TYPE i,
        lv_filename   TYPE string,
        lv_result     TYPE abap_bool.

  FIELD-SYMBOLS: <download>   LIKE LINE OF gt_download,
                 <word_data>  LIKE LINE OF i_word_data,
                 <field_data> TYPE any.

  lv_filename = i_template_file.
  cl_gui_frontend_services=>file_exist(
    EXPORTING
      file                 = lv_filename
    RECEIVING
      result               = lv_result
    EXCEPTIONS
      cntl_error           = 1
      error_no_gui         = 2
      wrong_parameter      = 3
      not_supported_by_gui = 4
      OTHERS               = 5
  ).
  IF sy-subrc <> 0 OR lv_result <> 'X'.
    sy-msgid = gc_message_class.
    sy-msgno = '000'.
    sy-msgty = 'E'.
    sy-msgv1 = lv_filename.
    RAISE file_do_not_exist.
  ENDIF.

* Header
  APPEND INITIAL LINE TO gt_download ASSIGNING <download>.
  LOOP AT i_word_data ASSIGNING <word_data>.

    WRITE <word_data>-field TO lv_hstr LEFT-JUSTIFIED.
    IF sy-tabix > 1.
      CONCATENATE <download> lc_tab lv_hstr
                  INTO <download>.
    ELSE.
      CONCATENATE <download> lv_hstr
                  INTO <download>.
    ENDIF.

  ENDLOOP.

* Item
  APPEND INITIAL LINE TO gt_download ASSIGNING <download>.
  LOOP AT i_word_data ASSIGNING <word_data>.

    WRITE <word_data>-value TO lv_hstr LEFT-JUSTIFIED.
    IF sy-tabix > 1.
      CONCATENATE <download> lc_tab lv_hstr
                  INTO <download>.
    ELSE.
      CONCATENATE <download> lv_hstr
                  INTO <download>.
    ENDIF.

  ENDLOOP.

  gv_template_file = i_template_file.

* Total columns/rows
  gv_total_columns = lines( i_word_data ).
  gv_total_rows = lines( i_word_data ).

  gv_download_path = i_download_path.

* Name of intermediate document
  gv_middle_filename = i_middle_filename.
  IF gv_middle_filename IS INITIAL.
    gv_middle_filename = 'WORDFOLE'.
  ENDIF.

* Adjust end of download path - Check / in the end of file path
  lv_position = strlen( gv_download_path ) - 1.
  IF gv_download_path+lv_position(1) <> '\'.
    gv_download_path = gv_download_path && '\'.
  ENDIF.

* Genereate full path of intermediate document
  gv_middle_fullpath = gv_download_path && gv_middle_filename && '.DOC'.

* Initiate word document
  IF get_word_version( ) < 8.

    CREATE OBJECT go_wordobj 'Word.Basic'.
    CALL METHOD OF
        go_wordobj
        'AppShow'.

  ELSE.

    CREATE OBJECT go_worddoc 'Word.Document'.
    GET PROPERTY OF go_worddoc 'Application' = go_wordapp.
    SET PROPERTY OF go_wordapp 'Visible' = 1.
    GET PROPERTY OF go_wordapp 'WordBasic' = go_wordobj.
    CALL METHOD OF
        go_wordobj
        'FileClose'.

    CALL METHOD OF
        go_wordobj
        'AppShow'.

    GET PROPERTY OF go_wordapp 'Documents' = go_documents.

  ENDIF.

ENDMETHOD.


METHOD create_middle_file.

  DATA: lv_filename TYPE string.

  lv_filename = gv_middle_fullpath.
  REPLACE '.DOC' WITH '.TXT' INTO lv_filename.

* Create new file
  cl_gui_frontend_services=>gui_download(
    EXPORTING
      filename                  = lv_filename
      write_field_separator     = 'X'
      trunc_trailing_blanks     = 'X'
      codepage                  = '4110' "note 1036562
      write_bom                 = 'X'    "note 1036562
    CHANGING
      data_tab                  = gt_download
    EXCEPTIONS
      file_write_error          = 1
      no_batch                  = 2
      gui_refuse_filetransfer   = 3
      invalid_type              = 4
      no_authority              = 5
      unknown_error             = 6
      header_not_allowed        = 7
      separator_not_allowed     = 8
      filesize_not_allowed      = 9
      header_too_long           = 10
      dp_error_create           = 11
      dp_error_send             = 12
      dp_error_write            = 13
      unknown_dp_error          = 14
      access_denied             = 15
      dp_out_of_memory          = 16
      disk_full                 = 17
      dp_timeout                = 18
      file_not_found            = 19
      dataprovider_exception    = 20
      control_flush_error       = 21
      not_supported_by_gui      = 22
      error_no_gui              = 23
      OTHERS                    = 24 ).
  IF sy-subrc <> 0.
* Close document
    CALL METHOD OF
        go_wordobj
        'FileClose'.

* Close Word
    CALL METHOD OF
        go_wordobj
        'AppClose'.

    RAISE error_download.
  ENDIF.

* Open created .txt document
  IF get_word_version( ) < 8.
    CALL METHOD OF
        go_wordobj
        'FileOpen'

      EXPORTING
        #01        = lv_filename
        #02        = 0.
  ELSE.

    CALL METHOD OF
        go_documents
        'Open'

      EXPORTING
        #01          = lv_filename    "file name
        #02          = 0              "confirm conversion
        #03          = 1              "ReadOnly
        #04          = 1              "AddToRecentFile
        #05          = ''             "Passgo_worddocument
        #06          = ''             "PasswordTemplat
        #07          = 0              "Revert
        #08          = ''             "WritePassgo_worddocume
        #09          = ''             "WritePasswordTemplate
        #10          = 'wdOpenFormatAuto'.
*                        #11 = 1255.   "Encoding: e.g. hebrew=1255

  ENDIF.

  IF sy-subrc <> 0.
    delete_file( lv_filename ).
    RETURN.
  ENDIF.

* Select all rows
  CALL METHOD OF
      go_wordobj
      'EditSelectAll'.
  IF sy-subrc <> 0.
    delete_file( lv_filename ).
    RETURN.
  ENDIF.

* Convert text to table
  IF gv_total_columns <= 63.
    CALL METHOD OF
        go_wordobj
        'TextToTable'

      EXPORTING
        #01           = '1'
        #02           = gv_total_columns
        #03           = gv_total_rows.

    IF sy-subrc <> 0.
      delete_file( lv_filename ).
      RETURN.
    ENDIF.

  ENDIF.

* no comments
  CALL METHOD OF
      go_wordobj
      'ToolsOptionsSave'

    EXPORTING
      #01                = 0
      #02                = 1
      #03                = 0.
  IF sy-subrc <> 0.
    delete_file( lv_filename ).
    RETURN.
  ENDIF.

* Save new file with extension .doc
  CALL METHOD OF
      go_wordobj
      'FileSaveAs'

    EXPORTING
      #01          = gv_middle_fullpath
      #02          = 0
      #03          = 0.
*      #04          = lv_password.
  IF sy-subrc <> 0.
    CALL METHOD OF
        go_wordobj
        'DocClose'

      EXPORTING
        #01        = 2.
    RETURN."RAISE communication_error.
  ENDIF.

* Close saved file
  CALL METHOD OF
      go_wordobj
      'FileClose'.
  IF sy-subrc <> 0.
    delete_file( gv_middle_fullpath ).
    RETURN.
  ENDIF.

* Set file
  CALL METHOD OF
      go_wordobj
      'SetAttr'

    EXPORTING
      #01        = gv_middle_fullpath
      #02        = 2.

* Delete file with the extension .txt
  delete_file( lv_filename ).

  cl_gui_cfw=>flush(
    EXCEPTIONS
      cntl_system_error = 1
      cntl_error        = 2
      OTHERS            = 3 ).
  IF sy-subrc <> 0.
* MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
*            WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
  ENDIF.

ENDMETHOD.


METHOD delete_file.

  DATA: lv_rc TYPE i.

  cl_gui_frontend_services=>file_delete(
    EXPORTING
      filename             = i_filename
    CHANGING
      rc                   = lv_rc
    EXCEPTIONS
      file_delete_failed   = 1
      cntl_error           = 2
      error_no_gui         = 3
      file_not_found       = 4
      access_denied        = 5
      unknown_error        = 6
      not_supported_by_gui = 7
      wrong_parameter      = 8
      OTHERS               = 9 ).
  IF sy-subrc <> 0.
* MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
*            WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
  ENDIF.

  cl_gui_cfw=>flush(
    EXCEPTIONS
      cntl_system_error = 1
      cntl_error        = 2
      OTHERS            = 3 ).
  IF sy-subrc <> 0.
* MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
*            WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
  ENDIF.

ENDMETHOD.


METHOD get_word_version.

  DATA: lv_reg_value TYPE string,
        lv_version   TYPE char80.

  cl_gui_frontend_services=>registry_get_value(
    EXPORTING
      root                 = cl_gui_frontend_services=>hkey_classes_root
      key                  = 'Word.Basic\CurVer'
      value                = space
    IMPORTING
      reg_value            = lv_reg_value
    EXCEPTIONS
      get_regvalue_failed  = 1
      cntl_error           = 2
      error_no_gui         = 3
      not_supported_by_gui = 4
      OTHERS               = 5 ).
  IF sy-subrc <> 0.
*    MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
*               WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
  ENDIF.

  cl_gui_cfw=>flush(
    EXCEPTIONS
      cntl_system_error = 1
      cntl_error        = 2
      OTHERS            = 3 ).
  IF sy-subrc <> 0.
* MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
*            WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
  ENDIF.

  lv_version = lv_reg_value.
  SHIFT lv_version LEFT BY 11 PLACES.
  MOVE lv_version TO e_word_version.

ENDMETHOD.


METHOD print_document.

  DATA: lv_password TYPE char15,
        lv_filename TYPE string.

* Delete atual file
  delete_file( gv_middle_fullpath ).

* Create intermediate file
  create_middle_file(
    EXCEPTIONS
      error_download = 1
      OTHERS         = 2
  ).
  IF sy-subrc <> 0.
    raise error_download_file.
  ENDIF.

* Open template document
  CALL METHOD OF
      go_wordobj
      'FileOpen'

    EXPORTING
      #01        = gv_template_file
      #02        = 0.

* Open Mail Merge using intermediate document
  CALL METHOD OF
      go_wordobj
      'MailMergeOpenDataSource'

    EXPORTING
      #01                       = gv_middle_fullpath
      #02                       = 0
      #03                       = 1
      #04                       = 0
      #05                       = 0
      #06                       = lv_password.
  IF sy-subrc <> 0.
    delete_file( gv_middle_fullpath ).
    RETURN.
  ENDIF.

* Edit document
  CALL METHOD OF
      go_wordobj
      'MailMergeEditMainDocument'.
  IF sy-subrc <> 0.
    delete_file( gv_middle_fullpath ).
    RETURN.
  ENDIF.

* Click on view data results
  CALL METHOD OF
      go_wordobj
      'MAILMERGEVIEWDATA'.

* Done and print after save
  CALL METHOD OF
      go_wordobj
      'MAILMERGETOPRINTER'.

* Save as new document to print
  CONCATENATE gv_template_file '2' INTO lv_filename.
  CALL METHOD OF
      go_wordobj
      'FileSaveAs'

    EXPORTING
      #01          = lv_filename
      #02          = 0
      #03          = 0
      #04          = lv_password.
  IF sy-subrc <> 0.
    CALL METHOD OF
        go_wordobj
        'DocClose'

      EXPORTING
        #01        = 2.
    RETURN. "RAISE communication_error.
  ENDIF.

* Close document
  CALL METHOD OF
      go_wordobj
      'FileClose'.

* Close Word
  CALL METHOD OF
      go_wordobj
      'AppClose'.

  cl_gui_cfw=>flush(
    EXCEPTIONS
      cntl_system_error = 1
      cntl_error        = 2
      OTHERS            = 3 ).
  IF sy-subrc <> 0.
* MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno
*            WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.
  ENDIF.

* Delete createds files after print
  delete_file( gv_middle_fullpath ).
  delete_file( lv_filename ).

ENDMETHOD.
ENDCLASS.