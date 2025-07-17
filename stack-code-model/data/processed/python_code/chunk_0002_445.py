class zcl_mail_static definition
  public
  final
  create public .

*"* public components of class ZCL_MAIL_STATIC
*"* do not include other source files here!!!
  public section.

    constants default_sender type string value 'info@company.com' ##NO_TEXT.

    class-methods send
      importing
        !i_from         type simple default default_sender
        !i_to           type simple
        !i_subject      type simple
        !i_message      type simple
        !it_attachments type zifiles optional
        !i_immediately  type abap_bool default abap_true
        !i_express      type abap_bool default abap_true
        !i_commit       type abap_bool default abap_false
      raising
        zcx_generic .
    class-methods send_mass
      importing
        !i_from         type simple default default_sender
        !it_to          type stringtab
        !i_subject      type simple
        !i_message      type simple
        !it_attachments type zifiles
        !i_commit       type abap_bool default abap_false
      raising
        zcx_generic .
    class-methods send_by_user
      importing
        !i_from         type simple default default_sender
        !i_user         type simple default sy-uname
        !i_subject      type simple
        !i_message      type simple
        !it_attachments type zifiles optional
        !i_commit       type abap_bool default abap_false
      raising
        zcx_generic .
    class-methods send_by_users
      importing
        !i_from         type simple default default_sender
        !it_users       type stringtab
        !i_subject      type simple
        !i_message      type simple
        !it_attachments type zifiles optional
        !i_commit       type abap_bool default abap_false
      raising
        zcx_generic .
  protected section.
*"* protected components of class ZCL_MAIL_STATIC
*"* do not include other source files here!!!
  private section.
*"* private components of class ZCL_MAIL_STATIC
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCL_MAIL_STATIC IMPLEMENTATION.


  method send.

    data l_from type string.
    l_from  = i_from.

    if l_from is initial.
      l_from = sy-uname.
    endif.

    data l_to type string.
    l_to  = i_to.

    if l_to is initial.
      return.
    endif.

    data l_subject type so_obj_des.
    l_subject = i_subject.

    data l_html type string.
    l_html = '<!DOCTYPE html><html><meta charset="utf-8"><head></head><body>%BODY%</body></html>'. "#EC NOTEXT

    replace '%BODY%' in l_html with i_message.

    do.

      data l_offset type i.
      l_offset = ( sy-index - 1 ) * 255.

      try.
          data lt_html type soli_tab.
          data ls_html like line of lt_html.
          ls_html-line = l_html+l_offset.
          insert ls_html into table lt_html.
        catch cx_root.
          exit.
      endtry.

    enddo.

    " Get Business Communication Service
    try.
        data lr_bcs type ref to cl_bcs.
        lr_bcs = cl_bcs=>create_persistent( ).
        data lx_root type ref to cx_root.
      catch cx_root into lx_root.
        zcx_generic=>raise( ix_root = lx_root ).
    endtry.

    " Create multirelated
    data lr_multi type ref to cl_gbt_multirelated_service.
    create object lr_multi.

    lr_multi->set_main_html( lt_html ).

    " Create document
    try.
        data lr_document  type ref to cl_document_bcs.
        lr_document =
          cl_document_bcs=>create_from_multirelated(
            i_subject          = l_subject
            i_multirel_service = lr_multi ).
      catch cx_root into lx_root.
        zcx_generic=>raise( ix_root = lx_root ).
    endtry.

    " Set document
    try.
        lr_bcs->set_document( lr_document ).
      catch cx_root into lx_root.
        zcx_generic=>raise( ix_root = lx_root ).
    endtry.

    " Create sender
    find '@' in l_from.
    if sy-subrc eq 0.

      data l_email type ad_smtpadr.
      l_email = l_from.

      try.
          data lr_sender type ref to if_sender_bcs.
          lr_sender = cl_cam_address_bcs=>create_internet_address( l_email ).
        catch cx_root into lx_root.
          zcx_generic=>raise( ix_root = lx_root ).
      endtry.

    else.

      data l_user type uname.
      l_user = l_from.

      try.
          lr_sender = cl_sapuser_bcs=>create( l_user ).
        catch cx_root into lx_root.
          zcx_generic=>raise( ix_root = lx_root ).
      endtry.

    endif.

    " Set sender
    try.
        lr_bcs->set_sender( lr_sender ).
      catch cx_root into lx_root.
        zcx_generic=>raise( ix_root = lx_root ).
    endtry.

    " Create recipient
    find '@' in l_to.
    if sy-subrc eq 0.

      l_email = l_to.

      try.
          data lr_recipient type ref to if_recipient_bcs.
          lr_recipient = cl_cam_address_bcs=>create_internet_address( l_email ).
        catch cx_root into lx_root.
          zcx_generic=>raise( ix_root = lx_root ).
      endtry.

    else.

      l_user = l_to.

      try.
          lr_recipient = cl_sapuser_bcs=>create( l_user ).
        catch cx_root into lx_root.
          zcx_generic=>raise( ix_root = lx_root ).
      endtry.

    endif.

    " Set recipient
    try.
        lr_bcs->add_recipient(
          i_recipient = lr_recipient
          i_express   = i_express ).
      catch cx_root into lx_root.
        zcx_generic=>raise( ix_root = lx_root ).
    endtry.

    " Attach attachment
    field-symbols <ls_attachment> like line of it_attachments.
    loop at it_attachments assigning <ls_attachment>.

      data l_size type i.
      l_size = xstrlen( <ls_attachment>-data ).

      data lt_solix type solix_tab.
      clear lt_solix.
      zcl_convert_static=>xtext2xtable(
        exporting i_data  = <ls_attachment>-data
        importing et_data = lt_solix ).

***    lt_solix = cl_document_bcs=>xstring_to_solix( <ls_attachment>-data ).

      data l_attachment_subject type sood-objdes.
      l_attachment_subject = <ls_attachment>-name.

      data l_attachment_type type soodk-objtp.
      l_attachment_type = 'BIN'.

      if l_size ne 0.
        data l_attachment_size type so_obj_len.
        l_attachment_size = zcl_abap_static=>value2text( l_size ).
      endif.

      data lt_attachment_header type soli_tab.
      field-symbols <l_attachment_header> like line of lt_attachment_header.
      append initial line to lt_attachment_header assigning <l_attachment_header>.
      <l_attachment_header>-line = '&SO_FILENAME=' && <ls_attachment>-name.

      append initial line to lt_attachment_header assigning <l_attachment_header>.
      <l_attachment_header>-line = '&SO_FORMAT=BIN'.

      try.
          lr_document->add_attachment(
            i_attachment_subject = l_attachment_subject
            i_attachment_type    = l_attachment_type
            i_attachment_size    = l_attachment_size
            i_attachment_header  = lt_attachment_header
            i_att_content_hex    = lt_solix ).
        catch cx_root into lx_root.
          zcx_generic=>raise( ix_root = lx_root ).
      endtry.

    endloop.

    " Set send immediately
    try.
        lr_bcs->set_send_immediately( i_immediately ).
      catch cx_root into lx_root.
        zcx_generic=>raise( ix_root = lx_root ).
    endtry.

    " Send
    try.
        lr_bcs->send( ).
      catch cx_root into lx_root.
        zcx_generic=>raise( ix_root = lx_root ).
    endtry.

    if i_commit eq abap_true.
      zcl_abap_static=>commit( ).
    endif.

  endmethod.


  method send_by_user.

    data l_email type string.
    l_email = zcl_user_static=>get_email( i_user ).

    check l_email is not initial.

    data l_name type string.
    l_name = zcl_user_static=>get_name( i_user ).

    data l_message  type string.
    l_message = i_message.

    replace '%NAME%' in l_message with l_name.
    replace '%FIO%'  in l_message with l_name.

    send(
      i_from         = i_from
      i_to           = l_email
      i_subject      = i_subject
      i_message      = l_message
      it_attachments = it_attachments
      i_commit       = i_commit ).

  endmethod.


  method send_by_users.

    data lt_users like it_users.
    lt_users = it_users.

    sort lt_users.

    delete adjacent duplicates from lt_users.

    data l_user like line of lt_users.
    loop at lt_users into l_user.

      send_by_user(
        i_from         = i_from
        i_user         = l_user
        i_subject      = i_subject
        i_message      = i_message
        it_attachments = it_attachments
        i_commit       = abap_false ).

    endloop.

    if i_commit eq abap_true.
      zcl_abap_static=>commit( ).
    endif.

  endmethod.


  method send_mass.

    data l_to like line of it_to.
    loop at it_to into l_to.

      send(
        i_from         = i_from
        i_to           = l_to
        i_subject      = i_subject
        i_message      = i_message
        it_attachments = it_attachments
        i_commit       = abap_false ).

    endloop.

    if i_commit eq abap_true.
      zcl_abap_static=>commit( ).
    endif.

  endmethod.
ENDCLASS.