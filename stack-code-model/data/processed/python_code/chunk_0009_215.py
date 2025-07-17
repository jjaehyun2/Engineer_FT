class ZCL_COLOR_MANAGER definition
  public
  final
  create public .

public section.

  types:
    BEGIN OF mst_color,
        key   TYPE string,
        value TYPE REF TO zcl_color_prototype,
      END OF mst_color .
  types:
    mtt_colors TYPE HASHED TABLE OF mst_color WITH UNIQUE KEY key .

  methods CONSTRUCTOR .
  methods SET_COLOR
    importing
      !IV_KEY type STRING
      !IO_COLOR type ref to ZCL_COLOR_PROTOTYPE .
  methods GET_COLOR
    importing
      !IV_KEY type STRING
    returning
      value(RO_COLOR) type ref to ZCL_COLOR_PROTOTYPE .
  PROTECTED SECTION.
private section.

  data MR_COLORS type ref to MTT_COLORS .
  data MO_COLOR type ref to ZCL_COLOR_PROTOTYPE .
ENDCLASS.



CLASS ZCL_COLOR_MANAGER IMPLEMENTATION.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_COLOR_MANAGER->CONSTRUCTOR
* +-------------------------------------------------------------------------------------------------+
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD constructor.
    mr_colors = NEW #( ).
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_COLOR_MANAGER->GET_COLOR
* +-------------------------------------------------------------------------------------------------+
* | [--->] IV_KEY                         TYPE        STRING
* | [<-()] RO_COLOR                       TYPE REF TO ZCL_COLOR_PROTOTYPE
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD get_color.
    ro_color = mr_colors->*[ key = iv_key ]-value.
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_COLOR_MANAGER->SET_COLOR
* +-------------------------------------------------------------------------------------------------+
* | [--->] IV_KEY                         TYPE        STRING
* | [--->] IO_COLOR                       TYPE REF TO ZCL_COLOR_PROTOTYPE
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD set_color.
*    DATA(lv_key)    = iv_key.
*    DATA(lo_value)  = io_color.
    INSERT VALUE #( key = iv_key value = io_color ) INTO TABLE mr_colors->*.
  ENDMETHOD.
ENDCLASS.