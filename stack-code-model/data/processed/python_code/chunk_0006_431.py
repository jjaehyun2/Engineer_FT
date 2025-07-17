class ZAVE_CL_STUDENT_E definition
  public
  final
  create public .

public section.

  interfaces ZAVE_IF_STUDENT_E .

  data MO_STUDENT_P type ref to ZIF_ZAVE_STUDENT_P .

  methods CONSTRUCTOR
    importing
      !IO_STUDENT_P type ref to ZIF_ZAVE_STUDENT_P .
protected section.
private section.
ENDCLASS.



CLASS ZAVE_CL_STUDENT_E IMPLEMENTATION.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_STUDENT_E->CONSTRUCTOR
* +-------------------------------------------------------------------------------------------------+
* | [--->] IO_STUDENT_P                   TYPE REF TO ZIF_ZAVE_STUDENT_P
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD constructor.
    mo_student_p = io_student_p.
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_STUDENT_E->ZAVE_IF_STUDENT_E~GET_AVG_MARK
* +-------------------------------------------------------------------------------------------------+
* | [<-()] RV_AVG_MARK                    TYPE        ZAVE_STUD_AVG_MARK
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD zave_if_student_e~get_avg_mark.
    rv_avg_mark = mo_student_p->get_avg_mark( ).
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_STUDENT_E->ZAVE_IF_STUDENT_E~GET_ELLIGIBLE
* +-------------------------------------------------------------------------------------------------+
* | [<-()] RV_ELLIGIBLE                   TYPE        BOOLE_D
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD zave_if_student_e~get_elligible.
    rv_elligible = mo_student_p->get_elligible( ).
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_STUDENT_E->ZAVE_IF_STUDENT_E~GET_EMAIL
* +-------------------------------------------------------------------------------------------------+
* | [<-()] RV_EMAIL                       TYPE        ZAVE_STUD_EMAIL
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD zave_if_student_e~get_email.
    rv_email = mo_student_p->get_email( ).
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_STUDENT_E->ZAVE_IF_STUDENT_E~GET_FIRST_NAME
* +-------------------------------------------------------------------------------------------------+
* | [<-()] RV_FIRST_NAME                  TYPE        ZAVE_STUD_FIRST_NAME
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD zave_if_student_e~get_first_name.
    rv_first_name = mo_student_p->get_first_name( ).
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZAVE_CL_STUDENT_E->ZAVE_IF_STUDENT_E~GET_LAST_NAME
* +-------------------------------------------------------------------------------------------------+
* | [<-()] RV_LAST_NAME                   TYPE        ZAVE_STUD_LAST_NAME
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD zave_if_student_e~get_last_name.
    rv_last_name = mo_student_p->get_last_name( ).
  ENDMETHOD.
ENDCLASS.