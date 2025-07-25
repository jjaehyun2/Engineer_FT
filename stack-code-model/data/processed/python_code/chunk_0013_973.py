CLASS zxxx_cl_bs_log DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.
    CONSTANTS: c_msg_ident       TYPE c LENGTH 9 VALUE 'MSG_IDENT',
               c_log_number      TYPE spo_par VALUE '%LOGNUMBER',
               c_dflt_log_object TYPE balobj_d VALUE '/IWFND/'.

    CLASS-DATA: gui_docking_container TYPE REF TO  cl_gui_docking_container,
                gui_alv_grid          TYPE REF TO  cl_gui_alv_grid.

    CLASS-METHODS get_instance
      RETURNING
        VALUE(ro_instance) TYPE REF TO zxxx_cl_bs_log.
    CLASS-METHODS init
      IMPORTING
        !iv_object         TYPE balobj_d DEFAULT c_dflt_log_object
        !iv_subobject      TYPE balsubobj
        !iv_extnumber      TYPE balnrext OPTIONAL
        !it_extnumber_list TYPE stringtab OPTIONAL
      RETURNING
        VALUE(ro_instance) TYPE REF TO zxxx_cl_bs_log.

    METHODS get_protocol
      RETURNING
        VALUE(rt_protocol) TYPE bapirettab .
    METHODS log_message.
    METHODS log_exception
      IMPORTING
        !io_exception TYPE REF TO cx_root .
    METHODS log_sy_message
      IMPORTING
        !is_symsg TYPE symsg.
    METHODS log_bapiret
      IMPORTING
        !it_bapiret TYPE bapirettab .
    METHODS log_line.
    METHODS warning
      IMPORTING
        !msgtx TYPE char200 OPTIONAL
        !msgno TYPE symsgno OPTIONAL
        !msgv1 TYPE any OPTIONAL
        !msgv2 TYPE any OPTIONAL
        !msgv3 TYPE any OPTIONAL
        !msgv4 TYPE any OPTIONAL.
    METHODS log_caller .
    METHODS info
      IMPORTING
        !msgtx TYPE char200 OPTIONAL
        !msgno TYPE symsgno OPTIONAL
        !msgv1 TYPE any OPTIONAL
        !msgv2 TYPE any OPTIONAL
        !msgv3 TYPE any OPTIONAL
        !msgv4 TYPE any OPTIONAL.
    METHODS success
      IMPORTING
        !msgtx TYPE char200 OPTIONAL
        !msgno TYPE symsgno OPTIONAL
        !msgv1 TYPE any OPTIONAL
        !msgv2 TYPE any OPTIONAL
        !msgv3 TYPE any OPTIONAL
        !msgv4 TYPE any OPTIONAL.
    METHODS error
      IMPORTING
        !msgtx TYPE char200 OPTIONAL
        !msgno TYPE symsgno OPTIONAL
        !msgv1 TYPE any OPTIONAL
        !msgv2 TYPE any OPTIONAL
        !msgv3 TYPE any OPTIONAL
        !msgv4 TYPE any OPTIONAL.
    METHODS save
      IMPORTING
        !iv_finalize_log TYPE abap_bool DEFAULT abap_true.

  PROTECTED SECTION.
    TYPES: t_log_stack TYPE TABLE OF REF TO zxxx_cl_bs_log WITH DEFAULT KEY.

    CLASS-DATA: instance   TYPE REF TO zxxx_cl_bs_log,
                log_stack  TYPE t_log_stack, " LIFO: Last log initiated is first to be saved
                has_error  TYPE abap_bool,
                save_error TYPE abap_bool.

    DATA log_header TYPE bal_s_log .
    DATA log_handle TYPE balloghndl .
    DATA message_text TYPE char200 .
    DATA message_type TYPE symsgty .
    DATA content_type TYPE i .
    DATA message_class TYPE symsgid .
    DATA message_params TYPE bal_s_parm .
    DATA message_number TYPE symsgno .
    DATA message_var1 TYPE symsgv .
    DATA message_var2 TYPE symsgv .
    DATA message_var3 TYPE symsgv .
    DATA message_var4 TYPE symsgv .
    DATA message_priority TYPE balprobcl .
    DATA message_context TYPE bal_s_cont .

    DATA validity_in_days TYPE i VALUE 180 ##NO_TEXT.
    DATA log_protocol TYPE bapirettab .
    DATA log_counter TYPE i .
    DATA process_start TYPE timestampl.
    DATA process_end TYPE timestampl.
    DATA caller TYPE c LENGTH 200.

    CONSTANTS log_type_error TYPE symsgty VALUE 'E' ##NO_TEXT.
    CONSTANTS log_type_warning TYPE symsgty VALUE 'W' ##NO_TEXT.
    CONSTANTS log_type_success TYPE symsgty VALUE 'S' ##NO_TEXT.
    CONSTANTS log_type_info TYPE symsgty VALUE 'I' ##NO_TEXT.
    CONSTANTS message_text_id TYPE symsgid VALUE 'BL' ##NO_TEXT.
    CONSTANTS message_text_no TYPE symsgno VALUE '001' ##NO_TEXT.
    CONSTANTS log_process_create TYPE char4 VALUE 'CREA' ##NO_TEXT.
    CONSTANTS log_process_init TYPE char4 VALUE 'INIT' ##NO_TEXT.
    CONSTANTS log_process_save TYPE char4 VALUE 'SAVE' ##NO_TEXT.
    CONSTANTS log_process_exception TYPE char4 VALUE 'EXCP' ##NO_TEXT.

    CLASS-METHODS add_new_instance.

    METHODS add_msg_to_log_protocol
      IMPORTING
        !is_msg_handle TYPE balmsghndl .
    METHODS build_extnumber
      IMPORTING
        extnumber      TYPE balnrext OPTIONAL
        extnumber_list TYPE stringtab OPTIONAL
      CHANGING
        log_header     TYPE bal_s_log.
    METHODS error_handling
      IMPORTING
        !iv_process   TYPE char4
        !iv_subrc     TYPE sysubrc OPTIONAL
        !io_exception TYPE REF TO cx_root OPTIONAL .
    METHODS set_priority .
    METHODS set_content
      IMPORTING
        !msgtx TYPE char200
        !msgno TYPE symsgno
        !msgv1 TYPE any
        !msgv2 TYPE any
        !msgv3 TYPE any
        !msgv4 TYPE any .
    METHODS create_message
      IMPORTING
        !msgtx TYPE char200 OPTIONAL
        !msgno TYPE symsgno OPTIONAL
        !msgv1 TYPE any OPTIONAL
        !msgv2 TYPE any OPTIONAL
        !msgv3 TYPE any OPTIONAL
        !msgv4 TYPE any OPTIONAL.
    METHODS add_msg_by_message_text .
    METHODS add_msg_by_message_object .
    METHODS add_timestamp
      RETURNING
        VALUE(rv_time) TYPE symsgv .

    METHODS set_context.
    METHODS log_duration.
    METHODS det_caller.
    METHODS save_log.

ENDCLASS.



CLASS zxxx_cl_bs_log IMPLEMENTATION.

  METHOD add_msg_by_message_object.

    DATA(ls_msg) = VALUE bal_s_msg( msgty     = message_type
                                    probclass = message_priority
                                    context   = message_context
                                    params    = message_params
                                    msgid     = message_class
                                    msgno     = message_number
                                    msgv1     = message_var1
                                    msgv2     = message_var2
                                    msgv3     = message_var3
                                    msgv4     = message_var4 ).

    DATA(ls_msg_handle) = VALUE balmsghndl( ).

    CALL FUNCTION 'BAL_LOG_MSG_ADD'
      EXPORTING
        i_log_handle     = log_handle
        i_s_msg          = ls_msg
      IMPORTING
        e_s_msg_handle   = ls_msg_handle
      EXCEPTIONS
        log_not_found    = 1
        msg_inconsistent = 2
        log_is_full      = 3
        OTHERS           = 4.

    IF sy-subrc <> 0.

      CALL METHOD error_handling
        EXPORTING
          iv_process = log_process_create
          iv_subrc   = sy-subrc.

    ELSE.

      CALL METHOD add_msg_to_log_protocol
        EXPORTING
          is_msg_handle = ls_msg_handle.

    ENDIF.

  ENDMETHOD.


  METHOD add_msg_by_message_text.

    DATA(ls_msg_handle) = VALUE balmsghndl( ).

    CALL FUNCTION 'BAL_LOG_MSG_ADD_FREE_TEXT'
      EXPORTING
        i_log_handle     = log_handle
        i_msgty          = message_type
        i_probclass      = message_priority
        i_s_context      = message_context
        i_text           = message_text
        i_s_params       = message_params
      IMPORTING
        e_s_msg_handle   = ls_msg_handle
      EXCEPTIONS
        log_not_found    = 1
        msg_inconsistent = 2
        log_is_full      = 3
        OTHERS           = 4.

    IF sy-subrc <> 0.

      CALL METHOD error_handling
        EXPORTING
          iv_process = log_process_create
          iv_subrc   = sy-subrc.

    ELSE.

      CALL METHOD add_msg_to_log_protocol
        EXPORTING
          is_msg_handle = ls_msg_handle.

    ENDIF.

  ENDMETHOD.


  METHOD add_msg_to_log_protocol.

    DATA(ls_msg) = VALUE bal_s_msg( ).

    CALL FUNCTION 'BAL_LOG_MSG_READ'
      EXPORTING
        i_s_msg_handle = is_msg_handle
      IMPORTING
        e_s_msg        = ls_msg
      EXCEPTIONS
        log_not_found  = 1
        msg_not_found  = 2
        OTHERS         = 3.

    IF sy-subrc = 0.
      DATA(ls_bapiret2) = CORRESPONDING bapiret2( ls_msg MAPPING id         = msgid
                                                                 type       = msgty
                                                                 number     = msgno
                                                                 message_v1 = msgv1
                                                                 message_v2 = msgv2
                                                                 message_v3 = msgv3
                                                                 message_v4 = msgv4 ).
      APPEND ls_bapiret2 TO log_protocol.
    ENDIF.

  ENDMETHOD.


  METHOD add_new_instance.

    instance = NEW zxxx_cl_bs_log( ).
    APPEND instance TO log_stack.

  ENDMETHOD.


  METHOD add_timestamp.

    DATA: lv_timestamp TYPE timestampl.

    GET TIME STAMP FIELD lv_timestamp.
    rv_time = |{ lv_timestamp }|.

    " DD.MM.YYYY, hh:mm:ss.ms
    rv_time = |{ rv_time+6(2) }.{ rv_time+4(2) }.{ rv_time(4) }, | &
              |{ rv_time+8(2) }:{ rv_time+10(2) }:{ rv_time+12(2) }{ rv_time+14 }|.

  ENDMETHOD.


  METHOD build_extnumber.

    DATA(lt_extnumber_list) = VALUE stringtab( ).

    IF extnumber IS NOT INITIAL.

      APPEND extnumber TO lt_extnumber_list.

    ELSEIF extnumber_list IS NOT INITIAL.

      lt_extnumber_list = extnumber_list.

    ENDIF.

    IF lt_extnumber_list IS NOT INITIAL.

      LOOP AT lt_extnumber_list ASSIGNING FIELD-SYMBOL(<v_extnumber>).

        CASE sy-tabix.
          WHEN 1.
            log_header-extnumber = |{ <v_extnumber> }|.

          WHEN OTHERS.
            log_header-extnumber = |{ log_header-extnumber } { <v_extnumber> }|.

        ENDCASE.

      ENDLOOP.

    ELSE.

      SELECT SINGLE *
        FROM balsubt
        INTO @DATA(ls_balsubt)
        WHERE spras     EQ @sy-langu
          AND object    EQ @log_header-object
          AND subobject EQ @log_header-subobject.

      log_header-extnumber = ls_balsubt-subobjtxt.

    ENDIF.

  ENDMETHOD.


  METHOD create_message.

    CALL METHOD set_content
      EXPORTING
        msgtx = msgtx
        msgno = msgno
        msgv1 = msgv1
        msgv2 = msgv2
        msgv3 = msgv3
        msgv4 = msgv4.

    CALL METHOD set_context.

    CALL METHOD set_priority.

    ADD 1 TO log_counter.

    CASE content_type.
      WHEN 1.
        CALL METHOD add_msg_by_message_text.

      WHEN 2.
        CALL METHOD add_msg_by_message_object.

    ENDCASE.

    CLEAR: message_params.

  ENDMETHOD.


  METHOD det_caller.

    CHECK caller CO ' _0'.

    CALL METHOD zxxx_cl_bs_session=>get_callstack
      IMPORTING
        ev_function = DATA(lv_function)
        ev_method   = DATA(lv_method)
        ev_class    = DATA(lv_class)
        ev_report   = DATA(lv_report).

    IF lv_function IS NOT INITIAL.

      caller = lv_function.

    ELSEIF lv_class IS NOT INITIAL
      AND lv_method IS NOT INITIAL.

      CONCATENATE lv_class '=>' lv_method INTO caller.

    ELSEIF lv_report IS NOT INITIAL.

      caller = lv_report.

    ELSE.

      RETURN.

    ENDIF.

  ENDMETHOD.


  METHOD error.

    message_type = log_type_error.

    CALL METHOD create_message
      EXPORTING
        msgtx = msgtx
        msgno = msgno
        msgv1 = msgv1
        msgv2 = msgv2
        msgv3 = msgv3
        msgv4 = msgv4.

  ENDMETHOD.


  METHOD error_handling.

    " Stellt sicher, dass Fehlerhandling pro Fehler nur
    " einmal fehlschlagen kann und keine Endlosschleife
    " entsteht.
    CHECK has_error  EQ abap_false
      AND save_error EQ abap_false.
    has_error = abap_true.

*** Eingangsdaten sichern
    DATA(lv_msg_object) = log_header-object.
    DATA(lv_msg_subobj) = log_header-subobject.
    DATA(lv_msg_extnum) = log_header-extnumber.
    DATA(lv_msg_alddel) = log_header-aldate_del.

    DATA(lv_msg_class)  = message_class.
    DATA(lv_msg_typ)    = message_type.
    DATA(lv_msg_txt)    = message_text.
    DATA(lv_msg_nr)     = message_number.
    DATA(lv_msg_v1)     = message_var1.
    DATA(lv_msg_v2)     = message_var2.
    DATA(lv_msg_v3)     = message_var3.
    DATA(lv_msg_v4)     = message_var4.

    " Versuch zum alten Log Fehlernachricht bzgl.
    " fehlgeschlagenem Logging hinzuzufügen.
    MESSAGE e001(zxxx_log) INTO DATA(lv_msg).
    log_message( ).

*** Bestehendes Log abschließen und neues für Fehlerbehandlung erzeugen
    save( ).

    init( iv_object    = c_dflt_log_object
          iv_subobject = 'LOG'
          iv_extnumber = 'Logging: Fehlerbehandlung' ).

    MESSAGE e000(zxxx_log) WITH iv_process INTO lv_msg.
    log_message( ).

*** Allgemeine Log-Daten loggen
    DATA(lv_msg_txt_gen) = VALUE char200( ).
    lv_msg_txt_gen = |; OBJECT: { lv_msg_object }; SUBOBJ: { lv_msg_subobj }| &&
                     |; EXTNUM: { lv_msg_extnum }; ALDDEL: { lv_msg_alddel }|.

    error( msgtx = lv_msg_txt_gen ).

    CASE iv_process.
      WHEN log_process_init.
        CASE iv_subrc.
          WHEN 1.
            MESSAGE e006(zxxx_log) WITH iv_subrc INTO lv_msg.

          WHEN OTHERS.
            MESSAGE e007(zxxx_log) WITH iv_subrc INTO lv_msg.

        ENDCASE.

      WHEN log_process_save.
        CASE iv_subrc.
          WHEN 1.
            MESSAGE e008(zxxx_log) WITH iv_subrc INTO lv_msg.

          WHEN 2.
            MESSAGE e009(zxxx_log) WITH iv_subrc INTO lv_msg.

          WHEN 3.
            MESSAGE e010(zxxx_log) WITH iv_subrc INTO lv_msg.

          WHEN OTHERS.
            MESSAGE e011(zxxx_log) WITH iv_subrc INTO lv_msg.

        ENDCASE.

      WHEN OTHERS.
        CASE sy-subrc.
          WHEN 1.
            MESSAGE e008(zxxx_log) WITH iv_subrc INTO lv_msg.

          WHEN 2.
            MESSAGE e012(zxxx_log) WITH iv_subrc INTO lv_msg.

          WHEN 3.
            MESSAGE e013(zxxx_log) WITH iv_subrc INTO lv_msg.

          WHEN OTHERS.
            MESSAGE e014(zxxx_log) WITH iv_subrc INTO lv_msg.

        ENDCASE.

    ENDCASE.

    log_message( ).

*** Prozessbedingte Log-Daten loggen
    CASE iv_process.
      WHEN log_process_init.
        " Nichts Besonderes zum Loggen

      WHEN log_process_create.
        IF message_text CN ' _0'.

          MESSAGE e015(zxxx_log) WITH lv_msg_typ INTO lv_msg.
          log_message( ).

          CALL METHOD error
            EXPORTING
              msgtx = lv_msg_txt.

        ELSEIF message_number CN ' _0'.

          MESSAGE e003(zxxx_log) WITH lv_msg_nr lv_msg_class INTO lv_msg.
          log_message( ).

          MESSAGE e004(zxxx_log) WITH lv_msg_v1 lv_msg_v2 lv_msg_v3 lv_msg_v4 INTO lv_msg.
          log_message( ).

        ELSE.

          MESSAGE e002(zxxx_log) INTO lv_msg.
          log_message( ).

        ENDIF.

      WHEN log_process_exception.
        DATA(lo_exc_descr) = NEW cl_instance_description( the_subject = io_exception ).

        MESSAGE e005(zxxx_log) WITH lo_exc_descr->class_name INTO lv_msg.
        log_message( ).

      WHEN log_process_save.
    ENDCASE.

    " Ermögliche Speichern des Fehlerlogs
    save_error = abap_true.

    " Log für Fehlerbehandlung speichern
    save_log( ).

    " Fehlerhandling kann jetzt wieder aufgerufen werden
    has_error = abap_false.
    save_error = abap_false.

  ENDMETHOD.


  METHOD get_instance.

*    ASSERT log_stack IS NOT INITIAL.
*
*    instance = log_stack[ lines( log_stack ) ].
*
*    ro_instance = instance.

    IF log_stack IS INITIAL.

      IF instance IS NOT BOUND.

        add_new_instance( ).

      ENDIF.

    ELSE.

      instance = log_stack[ lines( log_stack ) ].

    ENDIF.

    ro_instance = instance.

  ENDMETHOD.


  METHOD get_protocol.

    rt_protocol = log_protocol.

  ENDMETHOD.


  METHOD info.

    message_type = log_type_info.

    CALL METHOD create_message
      EXPORTING
        msgtx = msgtx
        msgno = msgno
        msgv1 = msgv1
        msgv2 = msgv2
        msgv3 = msgv3
        msgv4 = msgv4.

  ENDMETHOD.


  METHOD init.

    add_new_instance( ).

    GET TIME STAMP FIELD instance->process_start.

    instance->log_header-object    = iv_object.
    instance->log_header-subobject = iv_subobject.

    CLEAR: instance->caller.
    CALL METHOD instance->det_caller.

    CALL METHOD instance->build_extnumber
      EXPORTING
        extnumber      = iv_extnumber
        extnumber_list = it_extnumber_list
      CHANGING
        log_header     = instance->log_header.

    CALL FUNCTION 'BAL_LOG_CREATE'
      EXPORTING
        i_s_log                 = instance->log_header
      IMPORTING
        e_log_handle            = instance->log_handle
      EXCEPTIONS
        log_header_inconsistent = 1
        OTHERS                  = 2.

    IF    sy-subrc <> 0
      AND has_error EQ abap_false.

      CALL METHOD instance->error_handling
        EXPORTING
          iv_process = log_process_init
          iv_subrc   = sy-subrc.

    ENDIF.

    CALL METHOD instance->log_caller.

    ro_instance = instance.

  ENDMETHOD.








  METHOD log_bapiret.

    DATA: lv_msg_txt TYPE c LENGTH 200.

    FIELD-SYMBOLS: <ls_bapiret> TYPE bapiret2.

    " Fehler loggen
    LOOP AT it_bapiret ASSIGNING <ls_bapiret>.

      CLEAR lv_msg_txt.
      lv_msg_txt = <ls_bapiret>-message.

      CASE <ls_bapiret>-type.
        WHEN log_type_error.
          CALL METHOD error
            EXPORTING
              msgtx = lv_msg_txt.

        WHEN log_type_warning.
          CALL METHOD warning
            EXPORTING
              msgtx = lv_msg_txt.

        WHEN log_type_success.
          CALL METHOD success
            EXPORTING
              msgtx = lv_msg_txt.

        WHEN log_type_info.
          CALL METHOD info
            EXPORTING
              msgtx = lv_msg_txt.

      ENDCASE.

    ENDLOOP.

  ENDMETHOD.


  METHOD log_caller.

    DATA: lv_function TYPE  dbglevent,
          lv_method   TYPE  dbglevent,
          lv_class    TYPE  dbgsrepid,
          lv_report   TYPE  dbgsrepid,
          lv_msg_txt  TYPE c LENGTH 200.

    " Returns one of the following return codes:
    " 0 - Everything's fine
    " 1 - Log could not be found
    " 2 - Message is inconsistent
    " 3 - Log is full
    " 4 - Other messages (not specified by SAP)
    " 5 - Message text is empty

    det_caller( ).

    message_type = log_type_success.
    lv_msg_txt = |***** { caller } at { add_timestamp( ) } *****|.

    CALL METHOD create_message
      EXPORTING
        msgtx = lv_msg_txt.

  ENDMETHOD.





  METHOD log_duration.

    IF    process_end   IS NOT INITIAL
      AND process_start IS NOT INITIAL.

      TRY.
          DATA(lv_duration) = cl_abap_tstmp=>subtract( tstmp1 = process_end
                                                       tstmp2 = process_start ) * 1000.

          message_type = log_type_success.

          CALL METHOD create_message
            EXPORTING
              msgtx = |Process runtime: { lv_duration } ms|.

        CATCH cx_root.
      ENDTRY.

    ENDIF.

  ENDMETHOD.


  METHOD log_exception.

    message_type  = log_type_error.

    " OTR-Text zu der Ausnahmeklasse ermitteln
    CALL METHOD io_exception->get_text
      RECEIVING
        result = message_text.

    " Name der Ausnahmeklasse ermitteln
    DATA(lo_exc_descr) = NEW cl_instance_description( io_exception ).

    CLEAR: message_params.
    message_params-altext = 'SBAL_EXCEPTION_01'.
    APPEND VALUE #( parname  = 'EXCEPTION'
                    parvalue = lo_exc_descr->class_name ) TO message_params-t_par.

    CALL METHOD create_message
      EXPORTING
        msgtx = message_text
        msgno = message_number
        msgv1 = message_var1
        msgv2 = message_var2
        msgv3 = message_var3
        msgv4 = message_var4.

  ENDMETHOD.


  METHOD log_line.

    message_type = log_type_success.

    CALL METHOD create_message
      EXPORTING
        msgtx = repeat( val = '-'
                        occ = 255 ).

  ENDMETHOD.


  METHOD log_message.

    message_class   = sy-msgid.
    message_type    = sy-msgty.

    CALL METHOD create_message
      EXPORTING
        msgno = sy-msgno
        msgv1 = sy-msgv1
        msgv2 = sy-msgv2
        msgv3 = sy-msgv3
        msgv4 = sy-msgv4.

  ENDMETHOD.





  METHOD log_sy_message.

    message_class = is_symsg-msgid.

    CASE is_symsg-msgty.
      WHEN log_type_info.
        info( msgno = is_symsg-msgno
              msgv1 = is_symsg-msgv1
              msgv2 = is_symsg-msgv2
              msgv3 = is_symsg-msgv3
              msgv4 = is_symsg-msgv4 ).

      WHEN log_type_success.
        success( msgno = is_symsg-msgno
                 msgv1 = is_symsg-msgv1
                 msgv2 = is_symsg-msgv2
                 msgv3 = is_symsg-msgv3
                 msgv4 = is_symsg-msgv4 ).

      WHEN log_type_warning.
        warning( msgno = is_symsg-msgno
                 msgv1 = is_symsg-msgv1
                 msgv2 = is_symsg-msgv2
                 msgv3 = is_symsg-msgv3
                 msgv4 = is_symsg-msgv4 ).

      WHEN log_type_error.
        error( msgno = is_symsg-msgno
               msgv1 = is_symsg-msgv1
               msgv2 = is_symsg-msgv2
               msgv3 = is_symsg-msgv3
               msgv4 = is_symsg-msgv4 ).

    ENDCASE.

  ENDMETHOD.


  METHOD save.

    IF    (    has_error  EQ abap_false
            OR save_error EQ abap_true )
      AND log_counter > 0.

      IF iv_finalize_log EQ abap_true.
        GET TIME STAMP FIELD process_end.
        CALL METHOD log_duration( ).
        CALL METHOD log_line( ).
      ENDIF.

      save_log( ).

    ELSE.

      CALL FUNCTION 'BAL_LOG_DELETE'
        EXPORTING
          i_log_handle  = log_handle
        EXCEPTIONS
          log_not_found = 1
          OTHERS        = 2.

    ENDIF.

    IF iv_finalize_log EQ abap_true.
      DELETE TABLE log_stack FROM instance.
      CLEAR: instance, log_header, log_handle.
    ENDIF.

  ENDMETHOD.


  METHOD save_log.

    DATA(lt_log_handles) = VALUE bal_t_logh( ( log_handle ) ).
    DATA(lt_new_lognumbers) = VALUE bal_t_lgnm( ).

    CALL FUNCTION 'BAL_DB_SAVE'
      EXPORTING
        i_t_log_handle       = lt_log_handles
        i_save_all           = abap_false
        i_2th_connection     = abap_true
        i_2th_connect_commit = abap_true
      IMPORTING
        e_new_lognumbers     = lt_new_lognumbers
      EXCEPTIONS
        log_not_found        = 1
        save_not_allowed     = 2
        numbering_error      = 3
        OTHERS               = 4.

    CASE sy-subrc.
      WHEN 0.
      WHEN OTHERS.
        CALL FUNCTION 'BAL_LOG_DELETE'
          EXPORTING
            i_log_handle  = log_handle
          EXCEPTIONS
            log_not_found = 1
            OTHERS        = 2.

        CLEAR: log_header, log_handle.

        CALL METHOD error_handling
          EXPORTING
            iv_process = log_process_save
            iv_subrc   = sy-subrc.

    ENDCASE.

  ENDMETHOD.


  METHOD set_content.

    DATA: lv_msg_var TYPE string.

    IF msgtx IS NOT INITIAL.

      message_text = msgtx.

      DO 4 TIMES.

        CLEAR: lv_msg_var.

        CASE sy-index.
          WHEN 1.
            lv_msg_var = msgv1.

          WHEN 2.
            lv_msg_var = msgv2.

          WHEN 3.
            lv_msg_var = msgv3.

          WHEN 4.
            lv_msg_var = msgv4.

        ENDCASE.

        IF lv_msg_var IS NOT INITIAL.

          REPLACE FIRST OCCURRENCE OF '&' IN message_text WITH lv_msg_var.

        ELSE.

          EXIT.

        ENDIF.

      ENDDO.

      content_type = 1.

    ELSEIF msgno CN ' _'.

      message_number = msgno.

      message_var1 = CONV #( msgv1 ).
      message_var2 = CONV #( msgv2 ).
      message_var3 = CONV #( msgv3 ).
      message_var4 = CONV #( msgv4 ).

      content_type = 2.

    ELSE.

      RETURN.

    ENDIF.

  ENDMETHOD.


  METHOD set_context.

    zxxx_cl_bs_session=>get_context(
      IMPORTING
        ev_program = DATA(lv_program)
        ev_blockname = DATA(lv_include)
        ev_line    = DATA(lv_line) ).

    DATA(ls_log_context) = VALUE zxxx_s_log_context( program = lv_program
                                                     include = lv_include
                                                     line    = lv_line ).
    message_context-value   = ls_log_context.
    message_context-tabname = 'ZXXX_S_LOG_CONTEXT'.

  ENDMETHOD.


  METHOD set_priority.

    CASE message_type.
      WHEN log_type_info.
        message_priority = '4'. " Zusatzinformationen

      WHEN log_type_success.
        message_priority = '3'. " Mittel

      WHEN log_type_warning.
        message_priority = '2'. " Wichtig

      WHEN log_type_error.
        message_priority = '1'. " Sehr wichtig

    ENDCASE.

  ENDMETHOD.


  METHOD success.

    message_type = log_type_success.

    CALL METHOD create_message
      EXPORTING
        msgtx = msgtx
        msgno = msgno
        msgv1 = msgv1
        msgv2 = msgv2
        msgv3 = msgv3
        msgv4 = msgv4.

  ENDMETHOD.





  METHOD warning.

    message_type = log_type_warning.

    CALL METHOD create_message
      EXPORTING
        msgtx = msgtx
        msgno = msgno
        msgv1 = msgv1
        msgv2 = msgv2
        msgv3 = msgv3
        msgv4 = msgv4.

  ENDMETHOD.

ENDCLASS.