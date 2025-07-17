class YCL_CYGNUS definition
  public
  final
  create public .

public section.

  types YFILTERED type ref to DATA .

  methods TRIM
    importing
      !IM_STRING type STRING
    returning
      value(RE_STRING) type STRING .
  methods SPLIT
    importing
      !IM_DELIMITER type C
      !IM_STRING type STRING
    returning
      value(RE_STRINGTAB) type STRINGTAB .
  methods EQUALS
    importing
      !IM_INPUT1 type ANY
      !IM_INPUT2 type ANY
    returning
      value(RE_VALID) type ABAP_BOOL .
  methods FILTER
    importing
      !IM_FILTER type ANY
      !IM_DATA type ANY
    returning
      value(RE_FILTERED) type YFILTERED .
  methods INTERPERSE
    importing
      !IM_DELIMITER type STRING
      !IM_STRINGTAB type STRINGTAB
    returning
      value(RE_STRINGTAB) type STRINGTAB .
  methods WITHOUT
    importing
      !IM_INPUT1 type DATA
      !IM_INPUT2 type DATA
    returning
      value(RE_RESULT) type ref to DATA .
PROTECTED SECTION.
  PRIVATE SECTION.
ENDCLASS.



CLASS YCL_CYGNUS IMPLEMENTATION.


METHOD equals.
  re_valid = COND #( WHEN cl_abap_typedescr=>describe_by_data( im_input1 ) = cl_abap_typedescr=>describe_by_data( im_input2 ) THEN abap_true ELSE abap_false ).
ENDMETHOD.


  METHOD filter.

  ENDMETHOD.


METHOD interperse.
  re_stringtab = COND #( WHEN lines( im_stringtab ) > 1
                         THEN VALUE #( FOR i IN im_stringtab ( VALUE #( ) ) )
                         ELSE im_stringtab ).
ENDMETHOD.


METHOD split.

ENDMETHOD.


METHOD trim.
  re_string = shift_left( shift_right( im_string ) ).
ENDMETHOD.


  METHOD without.
    ASSIGN im_input1->* TO FIELD-SYMBOL(<input1>).
    ASSIGN im_input2->* TO FIELD-SYMBOL(<input2>).
  ENDMETHOD.
ENDCLASS.