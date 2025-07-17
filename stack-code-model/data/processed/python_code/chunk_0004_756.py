class ZCL_GIT_OBJECT_TEMPLATE definition
  public
  abstract
  final
  create public .

*"* public components of class ZCL_GIT_OBJECT_TEMPLATE
*"* do not include other source files here!!!
public section.

  class-methods CREATE
    importing
      !I_DATA type ANY
    returning
      value(R_ID) type ID
    raising
      ZCX_BC_PARAMETER .
  class-methods READ
    importing
      !I_OBJECT_ID type ANY
      !I_DETAILS type ABAP_BOOL default ABAP_FALSE
    returning
      value(R_OBJECT) type ref to OBJECT .
  methods UPDATE
    importing
      !I_DATA type ANY
    returning
      value(R_OBJECT) type ref to OBJECT .
  methods DELETE .
  class-methods FIND_BY_
    importing
      !I_CRITERION type ANY
    returning
      value(R_OBJECTS) type ZBC_OBJECT_IDS .
  class-methods CREATE_MULTIPLE
    importing
      !I_DATAS type ANY TABLE .
protected section.
*"* protected components of class ZCL_GIT_OBJECT_TEMPLATE
*"* do not include other source files here!!!
private section.
*"* private components of class ZCL_GIT_OBJECT_TEMPLATE
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCL_GIT_OBJECT_TEMPLATE IMPLEMENTATION.


method CREATE.
endmethod.


method CREATE_MULTIPLE.
endmethod.


method DELETE.
endmethod.


method FIND_BY_.
endmethod.


method READ.
endmethod.


method UPDATE.
endmethod.
ENDCLASS.