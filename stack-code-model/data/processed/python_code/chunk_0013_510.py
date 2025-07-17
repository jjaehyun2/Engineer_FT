class ZCL_CA_HARD_WIRED_ENCRYPTOR definition
  public
  create public .

public section.
*"* public components of class ZCL_CA_HARD_WIRED_ENCRYPTOR
*"* do not include other source files here!!!

  class-methods CLASS_CONSTRUCTOR .
  methods ENCRYPT_BYTES2BYTES
    importing
      !THE_BYTE_ARRAY type XSTRING
    returning
      value(RESULT) type XSTRING .
  type-pools ABAP .
  class-methods RUN_TEST
    returning
      value(RESULT) type ABAP_BOOL .
  methods DECRYPT_BYTES2BYTES
    importing
      !THE_BYTE_ARRAY type XSTRING
    returning
      value(RESULT) type XSTRING
    raising
      CX_ENCRYPT_ERROR .
  methods GET_BYTES
    importing
      !THE_STRING type STRING
    returning
      value(RESULT) type XSTRING
    raising
      CX_ENCRYPT_ERROR .
  methods ENCRYPT_STRING2BYTES
    importing
      !THE_STRING type STRING
    returning
      value(RESULT) type XSTRING
    raising
      CX_ENCRYPT_ERROR .
  methods BASE64_ENCODE
    importing
      !THE_BYTE_ARRAY type XSTRING
    returning
      value(RESULT) type STRING
    raising
      CX_ENCRYPT_ERROR .
  methods ENCRYPT_STRING2STRING
    importing
      !THE_STRING type STRING
    returning
      value(RESULT) type STRING
    raising
      CX_ENCRYPT_ERROR .
  methods DECRYPT_BYTES2STRING
    importing
      !THE_BYTE_ARRAY type XSTRING
    returning
      value(RESULT) type STRING
    raising
      CX_ENCRYPT_ERROR .
  methods DECRYPT_STRING2STRING
    importing
      !THE_STRING type STRING
    returning
      value(RESULT) type STRING
    raising
      CX_ENCRYPT_ERROR .
  methods BASE64_DECODE
    importing
      !THE_STRING type STRING
    returning
      value(RESULT) type XSTRING
    raising
      CX_ENCRYPT_ERROR .
  class-methods ZRUN_TEST
    importing
      !IV_INPUT type STRING
    exporting
      !EV_OUTPUT type STRING .
protected section.
*"* protected components of class ZCL_CA_HARD_WIRED_ENCRYPTOR
*"* do not include other source files here!!!
private section.
*"* private components of class ZCL_CA_HARD_WIRED_ENCRYPTOR
*"* do not include other source files here!!!

  constants XOR_VAL type X value '82'. "#EC NOTEXT
  constants ENC_FLAG type X value '01'. "#EC NOTEXT
  class-data STRING2BYTE_CONVERTER type ref to CL_ABAP_CONV_OUT_CE .
  class-data BYTE2STRING_CONVERTER type ref to CL_ABAP_CONV_IN_CE .
ENDCLASS.



CLASS ZCL_CA_HARD_WIRED_ENCRYPTOR IMPLEMENTATION.


method BASE64_DECODE .
*-- Returns Base64 encoding of THE_BYTE_ARRAY

  CALL FUNCTION 'SSFC_BASE64_DECODE'
    EXPORTING
      B64DATA                        = the_string
*     B64LENG                        =
*     B_CHECK                        =
   IMPORTING
     BINDATA                        = result
   EXCEPTIONS
     SSF_KRN_ERROR                  = 1
     SSF_KRN_NOOP                   = 2
     SSF_KRN_NOMEMORY               = 3
     SSF_KRN_OPINV                  = 4
     SSF_KRN_INPUT_DATA_ERROR       = 5
     SSF_KRN_INVALID_PAR            = 6
     SSF_KRN_INVALID_PARLEN         = 7
     OTHERS                         = 8
            .
  IF SY-SUBRC <> 0.
    data: cx_id type string.
    case sy-subrc.
      when 1. cx_id = 'SSF_KRN_ERROR'.
      when 2. cx_id = 'SSF_KRN_NOOP'.
      when 3. cx_id = 'SSF_KRN_NOMEMORY'.
      when 4. cx_id = 'SSF_KRN_OPINV'.
      when 5. cx_id = 'SSF_KRN_INPUT_DATA_ERROR'.
      when 6. cx_id = 'SSF_KRN_INVALID_PAR'.
      when 7. cx_id = 'SSF_KRN_INVALID_PARLEN'.
      when 8. cx_id = 'OTHERS'.
    endcase.
    raise exception type cx_encrypt_error
      exporting nested_cx = cx_id
                nested_op = 'SSFC_BASE64_DECODE'.
  ENDIF.

endmethod.


method BASE64_ENCODE.
*-- Returns Base64 encoding of THE_BYTE_ARRAY

  CALL FUNCTION 'SSFC_BASE64_ENCODE'
    EXPORTING
      BINDATA                        = the_byte_array
*     BINLENG                        =
   IMPORTING
     B64DATA                         = result
   EXCEPTIONS
     SSF_KRN_ERROR                  = 1
     SSF_KRN_NOOP                   = 2
     SSF_KRN_NOMEMORY               = 3
     SSF_KRN_OPINV                  = 4
     SSF_KRN_INPUT_DATA_ERROR       = 5
     SSF_KRN_INVALID_PAR            = 6
     SSF_KRN_INVALID_PARLEN         = 7
     OTHERS                         = 8
            .
  IF SY-SUBRC <> 0.
    data: cx_id type string.
    case sy-subrc.
      when 1. cx_id = 'SSF_KRN_ERROR'.
      when 2. cx_id = 'SSF_KRN_NOOP'.
      when 3. cx_id = 'SSF_KRN_NOMEMORY'.
      when 4. cx_id = 'SSF_KRN_OPINV'.
      when 5. cx_id = 'SSF_KRN_INPUT_DATA_ERROR'.
      when 6. cx_id = 'SSF_KRN_INVALID_PAR'.
      when 7. cx_id = 'SSF_KRN_INVALID_PARLEN'.
      when 8. cx_id = 'OTHERS'.
    endcase.
    raise exception type cx_encrypt_error
      exporting nested_cx = cx_id
                nested_op = 'SSFC_BASE64_ENCODE'.
  ENDIF.

endmethod.


method CLASS_CONSTRUCTOR.
*-- initializes class variables to make them available for instances

  string2byte_converter = cl_abap_conv_out_ce=>create( encoding = 'UTF-8' ).
  byte2string_converter = cl_abap_conv_in_ce=>create( encoding = 'UTF-8' ).

endmethod.


method DECRYPT_BYTES2BYTES .
*-- Returns a hard-wired encryption of THE_BYTE_ARRAY.

  data: leng       type i,
        result_len type i,
        src_offs   type i,
        tgt_offs   type i,
        l_ref      type ref to data,
        a_byte     type x.
  field-symbols:
        <copy_dat> type x.


* -- check for errors
  leng = xstrlen( the_byte_array ).
  if leng <= 0.
    raise exception type cx_encrypt_error
          exporting textid = cx_encrypt_error=>invalid_size
                    param  = 'THE_BYTE_ARRAY'.
  endif.
  a_byte = the_byte_array(1).
  if a_byte <> enc_flag.
    raise exception type cx_encrypt_error
          exporting textid = cx_encrypt_error=>unencrypted
                    param  = 'THE_BYTE_ARRAY'.
  endif.

* -- everything seems okay
  result_len = leng - 1.
  if result_len < 1.
    clear result.
    exit. "added, MM
  endif.

  create data l_ref type x length result_len.
  assign l_ref->* to <copy_dat>.
  tgt_offs = result_len.
  do result_len times.
    src_offs = sy-index.
    tgt_offs = tgt_offs - 1.
    <copy_dat>+tgt_offs(1) = the_byte_array+src_offs(1) bit-xor xor_val.
  enddo.

  result = <copy_dat>.

endmethod.


method DECRYPT_BYTES2STRING .
*-- Returns String built from decryption of THE_BYTE_ARRAY

  data: decrypted_bytes type xstring,
        cx              type ref to cx_root.

  decrypted_bytes = decrypt_bytes2bytes( the_byte_array ).
  TRY.
  CALL METHOD BYTE2STRING_CONVERTER->CONVERT
    EXPORTING
      INPUT                         = decrypted_bytes
*      N                             = -1
    IMPORTING
      DATA                          = result
*      LEN                           =
*      INPUT_TOO_SHORT               =
      .
   CATCH CX_SY_CONVERSION_CODEPAGE
         CX_SY_CODEPAGE_CONVERTER_INIT
         CX_PARAMETER_INVALID_TYPE     into cx.

      raise exception type cx_encrypt_error
              exporting previous = cx
                        nested_op = 'BYTE2STRING_CONVERTER->CONVERT'.
  ENDTRY.

endmethod.


method DECRYPT_STRING2STRING .
*-- Returns String built from decryption of THE_BYTE_ARRAY

  data: decoded_bytes type xstring.

  decoded_bytes = base64_decode( the_string ).
  result = decrypt_bytes2string( decoded_bytes ).


endmethod.


method ENCRYPT_BYTES2BYTES .
*-- Returns a hard-wired encryption of THE_BYTE_ARRAY.

  data: leng       type i,
        result_len type i,
        offs       type i,
        l_ref      type ref to data.
  field-symbols:
        <copy_dat> type x.

  leng = xstrlen( the_byte_array ).
  if leng <= 0.
    clear result.
  endif.

  result_len = leng + 1.
  create data l_ref type x length result_len.
  assign l_ref->* to <copy_dat>.
  do leng times.
    offs = sy-index - 1.
    result_len = result_len - 1.
    <copy_dat>+result_len(1) = the_byte_array+offs(1) bit-xor xor_val.
  enddo.

  <copy_dat>(1) = enc_flag.
  result = <copy_dat>.

endmethod.


method ENCRYPT_STRING2BYTES .
*-- Returns the encryption of the byte representation of THE_STRING.

  data: string_as_xstring type xstring.

  string_as_xstring = get_bytes( the_string ).
  result = encrypt_bytes2bytes( string_as_xstring ).

endmethod.


method ENCRYPT_STRING2STRING.
*-- Returns Base64 encoding of encrypted string

  data: string_as_bytes type xstring.

  string_as_bytes = encrypt_string2bytes( the_string ).
  result = base64_encode( string_as_bytes ).
endmethod.


method GET_BYTES.
*-- returns the byte representation of THE_STRING

  data: cx type ref to cx_root.

    TRY.
    CALL METHOD STRING2BYTE_CONVERTER->CONVERT
      EXPORTING
        DATA                          = the_string
*        N                             = -1
      IMPORTING
        BUFFER                        = result
*        LEN                           =
        .
     CATCH CX_SY_CONVERSION_CODEPAGE
         CX_SY_CODEPAGE_CONVERTER_INIT
         CX_PARAMETER_INVALID_TYPE     into cx.

      raise exception type cx_encrypt_error
              exporting previous = cx
                        nested_op = 'STRING2BYTE_CONVERTER->CONVERT'.
  ENDTRY.


endmethod.


method RUN_TEST .
*-- runs a few tests; returns ABAP_TRUE iff all tests are passed.

  data: test_object  type ref to cl_hard_wired_encryptor,
        hex_in       type xstring ,
        hex_out      type xstring,
        hex_expected type xstring,
        string_in    type string,
        string_out   type string,
        string_expected type string.

  result = abap_true.

try.
*-- check byte-to-byte algorithms
  hex_in  =
'0106111D3154111A1D111F5400131118541A1C153C540611105458151D1103540135'.
  create object test_object.
  hex_out = test_object->encrypt_bytes2bytes( hex_in ).
  hex_expected =
'01417520776569612C20646572204861686E206C656774206B65696E65204569657275'
.
  if hex_out <> hex_expected.
    result = abap_false.
    return.
  endif.


  hex_out = test_object->decrypt_bytes2bytes( hex_out ).
  if hex_out <> hex_in.
    result = abap_false.
    return.
  endif.


*-- check string-to-string algorithms
  string_in = 'Au weia, der Hahn legt keine Eier'. "#EC NOTEXT
  string_out = test_object->encrypt_string2string( string_in ).
  string_expected = 'AQYRHTFUERodER9UABMRGFQaHBU8VAYREFRYFR0RA1QBNQ=='.
  if string_out <> string_expected.
    result = abap_false.
    return.
  endif.

  string_out = test_object->decrypt_string2string( string_out ).
  if string_out <> string_in.
    result = abap_false.
    return.
  endif.

catch cx_encrypt_error.
  result = abap_false.
    return.
endtry.

 endmethod.


METHOD ZRUN_TEST.
  DATA: lo_crypter TYPE REF TO zcl_ca_hard_wired_encryptor,
        lv_crypted TYPE string.

  CREATE OBJECT lo_crypter.

  lv_crypted = lo_crypter->encrypt_string2string( iv_input ).
  ev_output  = lo_crypter->decrypt_string2string( lv_crypted ).

ENDMETHOD.
ENDCLASS.