class YDKMSG definition
  public
  final
  create public .

public section.

  types:
    BEGIN OF ty_msg,
        msgid TYPE sy-msgid,
        msgno TYPE sy-msgno,
        msgty TYPE sy-msgty,
        msgv1 TYPE string,
        msgv2 TYPE string,
        msgv3 TYPE string,
        msgv4 TYPE string,
      END   OF ty_msg .
  types:
    ty_msg_tab TYPE STANDARD TABLE OF ty_msg WITH DEFAULT KEY .
  types TY_BDCMSGCOLL type BDCMSGCOLL .
  types:
    ty_bdcmsgcoll_tab TYPE STANDARD TABLE OF bdcmsgcoll WITH DEFAULT KEY .
  types TY_BAPIRET1 type BAPIRET1 .
  types:
    ty_bapiret1_tab TYPE STANDARD TABLE OF bapiret1 WITH DEFAULT KEY .
  types TY_BAPIRET2 type BAPIRET2 .
  types:
    ty_bapiret2_tab TYPE STANDARD TABLE OF bapiret2 WITH DEFAULT KEY .

  constants:
    BEGIN OF c_msgty,
        information TYPE sy-msgty VALUE 'I',
        status      TYPE sy-msgty VALUE 'I',
        warning     TYPE sy-msgty VALUE 'W',
        error       TYPE sy-msgty VALUE 'E',
        abort       TYPE sy-msgty VALUE 'A',
        dump        TYPE sy-msgty VALUE 'X',
      END   OF c_msgty .

  class-events MESSAGE
    exporting
      value(MSG) type TY_MSG .

  class-methods RAISE_MESSAGE
    importing
      !MSGID type CLIKE
      !MSGNO type SY-MSGNO
      !MSGTY type CLIKE optional
      !MSGV1 type CLIKE optional
      !MSGV2 type CLIKE optional
      !MSGV3 type CLIKE optional
      !MSGV4 type CLIKE optional .
  class-methods RAISE_MESSAGE_FROM
    importing
      !MSG_STRUCT type DATA .
  class-methods RAISE_TEXT
    importing
      !TEXT type CLIKE .
  class-methods MESSAGE_MOVE_TO
    importing
      !SRC type DATA
    changing
      !DEST type DATA .
  class-methods MSG
    importing
      !MSG_STRUCT type DATA
    returning
      value(MSG) type TY_MSG .
  class-methods DISPLAY_MESSAGE
    importing
      !MSG_STRUCT type DATA
      !MSGTY type SY-MSGTY optional
      !DISPLAY_LIKE type SY-MSGTY optional .
  class-methods MESSAGE_TO_STR
    importing
      !MSG_STRUCT type DATA
    returning
      value(RET) type STRING .
  class-methods RAISE_MESSAGE_EVENT
    importing
      !MSG_STRUCT type DATA .
protected section.
private section.
ENDCLASS.



CLASS YDKMSG IMPLEMENTATION.


  METHOD DISPLAY_MESSAGE.

    DATA(msg) = msg( msg_struct ).

    IF msgty IS NOT INITIAL.
      msg-msgty = msgty.
    ENDIF.

    IF msg-msgty IS INITIAL.
      msg-msgty = 'S'.
    ENDIF.

    IF display_like IS INITIAL.
      MESSAGE ID msg-msgid TYPE msg-msgty NUMBER msg-msgno WITH msg-msgv1 msg-msgv2 msg-msgv3 msg-msgv4.
    ELSE.
      MESSAGE ID msg-msgid TYPE msg-msgty NUMBER msg-msgno WITH msg-msgv1 msg-msgv2 msg-msgv3 msg-msgv4 DISPLAY LIKE display_like.
    ENDIF.
  ENDMETHOD.


  METHOD message_move_to.
    DATA: param_index TYPE i.
    DATA: src_index TYPE i.
    DATA: f_index TYPE i.

    DATA: fname TYPE fieldname.

    FIELD-SYMBOLS <src_param>  TYPE any.
    FIELD-SYMBOLS <dest_param> TYPE any.

    DO 7 TIMES.
      param_index = sy-index.

      UNASSIGN: <src_param>, <dest_param>.

      DO 2 TIMES.
        src_index = sy-index.

        DO.
          f_index = sy-index.

          CASE param_index.
            WHEN 1. " MSGID
              CASE f_index.
                WHEN 1. fname = 'MSGID'.
                WHEN 2. fname = 'MESSAGE_ID'.
                WHEN 3. fname = 'ID'.
                WHEN OTHERS.
                  EXIT.
              ENDCASE.
            WHEN 2. " MSGNO
              CASE f_index.
                WHEN 1. fname = 'MSGNO'.
                WHEN 2. fname = 'MSGNR'.
                WHEN 3. fname = 'MSG_NUMBER'.
                WHEN 4. fname = 'MESSAGE_NR'.
                WHEN 5. fname = 'NUMBER'.
                WHEN OTHERS.
                  EXIT.
              ENDCASE.
            WHEN 3. " MSGTY
              CASE f_index.
                WHEN 1. fname = 'MSGTY'.
                WHEN 2. fname = 'MSG_TYP'.
                WHEN 3. fname = 'MSG_TYPE'.
                WHEN 4. fname = 'MSGTYPE'.
                WHEN 5. fname = 'MESSAGE_TYPE'.
                WHEN 6. fname = 'MSGTYP'.
                WHEN 7. fname = 'TYPE'.
                WHEN OTHERS.
                  EXIT.
              ENDCASE.
            WHEN 4. " MSGV1
              CASE f_index.
                WHEN 1. fname = 'MSGV1'.
                WHEN 2. fname = 'MESSAGE_V1'.
                WHEN OTHERS.
                  EXIT.
              ENDCASE.
            WHEN 5. " MSGV2
              CASE f_index.
                WHEN 1. fname = 'MSGV2'.
                WHEN 2. fname = 'MESSAGE_V2'.
                WHEN OTHERS.
                  EXIT.
              ENDCASE.
            WHEN 6. " MSGV3
              CASE f_index.
                WHEN 1. fname = 'MSGV3'.
                WHEN 2. fname = 'MESSAGE_V3'.
                WHEN OTHERS.
                  EXIT.
              ENDCASE.
            WHEN 7. " MSGV4
              CASE f_index.
                WHEN 1. fname = 'MSGV4'.
                WHEN 2. fname = 'MESSAGE_V4'.
                WHEN OTHERS.
                  EXIT.
              ENDCASE.
          ENDCASE.

          CASE src_index.
            WHEN 1. ASSIGN COMPONENT fname OF STRUCTURE src  TO <src_param>.
            WHEN 2. ASSIGN COMPONENT fname OF STRUCTURE dest TO <dest_param>.
          ENDCASE.

          IF sy-subrc = 0.
            EXIT.
          ENDIF.
        ENDDO.
      ENDDO.

      IF <src_param> IS ASSIGNED AND <dest_param> IS ASSIGNED.
        <dest_param> = <src_param>.
      ELSE.
        IF ( <src_param> IS ASSIGNED AND <src_param> IS NOT INITIAL AND <dest_param> IS NOT ASSIGNED ) " есть источник и нет приёмника
        OR ( <dest_param> IS ASSIGNED AND <src_param> IS NOT ASSIGNED ). " есть приёмник и нет источника
*         MESSAGE e000(ydkmsg).
          raise_message( msgid = 'YDKMSG' msgno = '000' ).
        ENDIF.
      ENDIF.
    ENDDO.
  ENDMETHOD.


  METHOD message_to_str.
    DATA(msg) = msg( msg_struct ).

*   MESSAGE ID msg-msgid TYPE 'S' NUMBER msg-msgno WITH msg-msgv1 msg-msgv2 msg-msgv3 msg-msgv4 INTO ret. " обрезает MSGV+ по 50 символов

    SELECT SINGLE text INTO ret
      FROM t100
      WHERE sprsl = sy-langu
        AND arbgb = msg-msgid
        AND msgnr = msg-msgno.

    IF ret IS INITIAL.
      CONCATENATE msg-msgv1 msg-msgv2 msg-msgv3 msg-msgv4 INTO ret SEPARATED BY space.
      RETURN.
    ENDIF.

    REPLACE ALL OCCURRENCES OF '&1' IN ret WITH '~!#1%!~'.
    REPLACE ALL OCCURRENCES OF '&2' IN ret WITH '~!#2%!~'.
    REPLACE ALL OCCURRENCES OF '&3' IN ret WITH '~!#3%!~'.
    REPLACE ALL OCCURRENCES OF '&4' IN ret WITH '~!#4%!~'.

    REPLACE FIRST OCCURRENCE OF '&' IN ret WITH '~!#1%!~'.
    REPLACE FIRST OCCURRENCE OF '&' IN ret WITH '~!#2%!~'.
    REPLACE FIRST OCCURRENCE OF '&' IN ret WITH '~!#3%!~'.
    REPLACE FIRST OCCURRENCE OF '&' IN ret WITH '~!#4%!~'.

    REPLACE ALL OCCURRENCES OF '~!#1%!~' IN ret WITH msg-msgv1.
    REPLACE ALL OCCURRENCES OF '~!#2%!~' IN ret WITH msg-msgv2.
    REPLACE ALL OCCURRENCES OF '~!#3%!~' IN ret WITH msg-msgv3.
    REPLACE ALL OCCURRENCES OF '~!#4%!~' IN ret WITH msg-msgv4.
  ENDMETHOD.


  METHOD MSG.
    message_move_to( EXPORTING src =  msg_struct CHANGING dest = msg ).
  ENDMETHOD.


  METHOD raise_message.
    RAISE EXCEPTION TYPE ycx_dk_msg
      EXPORTING
        msg = VALUE #(
          msgid = msgid
          msgno = msgno
          msgty = msgty
          msgv1 = msgv1
          msgv2 = msgv2
          msgv3 = msgv3
          msgv4 = msgv4
       ).
  ENDMETHOD.


  METHOD raise_message_event.
    RAISE EVENT message EXPORTING msg = msg( msg_struct ).
  ENDMETHOD.


  METHOD raise_message_from.
    RAISE EXCEPTION TYPE ycx_dk_msg
      EXPORTING
        msg = msg( msg_struct ).
  ENDMETHOD.


  METHOD raise_text.
*   MESSAGE e001(ydkmsg).
    raise_message( msgid = 'YDKMSG' msgno = '001' msgv1 = text ).
  ENDMETHOD.
ENDCLASS.