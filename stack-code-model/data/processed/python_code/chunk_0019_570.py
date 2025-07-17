CLASS zcl_001_xml_util DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.
*"* public components of class ZCL_001_XML_UTIL
*"* do not include other source files here!!!

    CLASS-METHODS build_xml_datetime
       IMPORTING
         !iv_datetime TYPE c
         RETURNING value(rv_xml_datetime) TYPE zd_001_xml_datetime .
  PROTECTED SECTION.
*"* protected components of class ZCL_001_XML_UTIL
*"* do not include other source files here!!!
  PRIVATE SECTION.
*"* private components of class ZCL_001_XML_UTIL
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCL_001_XML_UTIL IMPLEMENTATION.


  METHOD build_xml_datetime.

    rv_xml_datetime = iv_datetime+0(4) && '-' &&
                    iv_datetime+4(2) && '-' &&
                    iv_datetime+6(2) && 'T' &&
                    iv_datetime+8(2) && ':' &&
                    iv_datetime+10(2) && ':' &&
                    iv_datetime+12(2).

  ENDMETHOD.                    "build_xml_datetime
ENDCLASS.