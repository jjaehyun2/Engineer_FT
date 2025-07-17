class ZCL_COLOR definition
  public
  inheriting from ZCL_COLOR_PROTOTYPE
  final
  create public .

public section.

  methods CONSTRUCTOR
    importing
      !IV_RED type I
      !IV_GREEN type I
      !IV_BLUE type I .

  methods CLONE
    redefinition .
protected section.
private section.

  data MV_RED type I .
  data MV_GREEN type I .
  data MV_BLUE type I .
ENDCLASS.



CLASS ZCL_COLOR IMPLEMENTATION.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_COLOR->CLONE
* +-------------------------------------------------------------------------------------------------+
* | [<-()] RO_PROTOTYPE                   TYPE REF TO ZCL_COLOR_PROTOTYPE
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD clone.
    DATA lo_object TYPE REF TO zcl_color.

    WRITE: / 'Cloning color RGB: ', mv_red, mv_green, mv_blue.

    lo_object = NEW #( iv_red   = me->mv_red
                       iv_green = me->mv_green
                       iv_blue  = me->mv_blue ).

*    lo_object->mv_red = me->mv_red.
*    lo_object->mv_red = me->mv_green.
*    lo_object->mv_red = me->mv_blue.

    ro_prototype = lo_object.

  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_COLOR->CONSTRUCTOR
* +-------------------------------------------------------------------------------------------------+
* | [--->] IV_RED                         TYPE        I
* | [--->] IV_GREEN                       TYPE        I
* | [--->] IV_BLUE                        TYPE        I
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD constructor.
    super->constructor( ).
    mv_red    = iv_red.
    mv_green  = iv_green.
    mv_blue   = iv_blue.
  ENDMETHOD.
ENDCLASS.