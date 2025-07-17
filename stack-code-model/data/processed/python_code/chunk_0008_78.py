class ZCL_ZAVE_STUDENT_P definition
  public
  final
  create protected

  global friends ZCB_ZAVE_STUDENT_P .

public section.

  interfaces IF_OS_STATE .
  interfaces ZIF_ZAVE_STUDENT_P .
protected section.
private section.

  data STUDENT_ID type ZAVE_STUD_ID .
  data FIRSTNAME type ZAVE_STUD_FIRST_NAME .
  data LASTNAME type ZAVE_STUD_LAST_NAME .
  data PHONE type ZAVE_STUD_PHONE .
  data EMAIL type ZAVE_STUD_EMAIL .
  data ADDRESS type ZAVE_STUD_ADDRESS .
  data AVERAGE_MARK type ZAVE_STUD_AVG_MARK .
  data ELLIGIBLE type /MSG/R_KZ_JN .

  methods SET_ADDRESS
    importing
      !I_ADDRESS type ZAVE_STUD_ADDRESS
    raising
      CX_OS_OBJECT_NOT_FOUND .
  methods SET_AVERAGE_MARK
    importing
      !I_AVERAGE_MARK type ZAVE_STUD_AVG_MARK
    raising
      CX_OS_OBJECT_NOT_FOUND .
  methods SET_ELLIGIBLE
    importing
      !I_ELLIGIBLE type /MSG/R_KZ_JN
    raising
      CX_OS_OBJECT_NOT_FOUND .
  methods SET_EMAIL
    importing
      !I_EMAIL type ZAVE_STUD_EMAIL
    raising
      CX_OS_OBJECT_NOT_FOUND .
  methods SET_FIRSTNAME
    importing
      !I_FIRSTNAME type ZAVE_STUD_FIRST_NAME
    raising
      CX_OS_OBJECT_NOT_FOUND .
  methods SET_LASTNAME
    importing
      !I_LASTNAME type ZAVE_STUD_LAST_NAME
    raising
      CX_OS_OBJECT_NOT_FOUND .
  methods SET_PHONE
    importing
      !I_PHONE type ZAVE_STUD_PHONE
    raising
      CX_OS_OBJECT_NOT_FOUND .
  methods GET_ADDRESS
    returning
      value(RESULT) type ZAVE_STUD_ADDRESS
    raising
      CX_OS_OBJECT_NOT_FOUND .
  methods GET_AVERAGE_MARK
    returning
      value(RESULT) type ZAVE_STUD_AVG_MARK
    raising
      CX_OS_OBJECT_NOT_FOUND .
  methods GET_ELLIGIBLE
    returning
      value(RESULT) type /MSG/R_KZ_JN
    raising
      CX_OS_OBJECT_NOT_FOUND .
  methods GET_EMAIL
    returning
      value(RESULT) type ZAVE_STUD_EMAIL
    raising
      CX_OS_OBJECT_NOT_FOUND .
  methods GET_FIRSTNAME
    returning
      value(RESULT) type ZAVE_STUD_FIRST_NAME
    raising
      CX_OS_OBJECT_NOT_FOUND .
  methods GET_LASTNAME
    returning
      value(RESULT) type ZAVE_STUD_LAST_NAME
    raising
      CX_OS_OBJECT_NOT_FOUND .
  methods GET_PHONE
    returning
      value(RESULT) type ZAVE_STUD_PHONE
    raising
      CX_OS_OBJECT_NOT_FOUND .
  methods GET_STUDENT_ID
    returning
      value(RESULT) type ZAVE_STUD_ID
    raising
      CX_OS_OBJECT_NOT_FOUND .
ENDCLASS.



CLASS ZCL_ZAVE_STUDENT_P IMPLEMENTATION.


  method GET_ADDRESS.
***BUILD 090501
     " returning RESULT
     " raising CX_OS_OBJECT_NOT_FOUND
************************************************************************
* Purpose        : Get Attribute ADDRESS
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : The object state is loaded, result is set
*
* OO Exceptions  : CX_OS_OBJECT_NOT_FOUND
*
* Implementation : -
*
************************************************************************
* Changelog:
* - 2000-03-14   : (BGR) Version 2.0
* - 2000-07-28   : (SB)  OO Exceptions
************************************************************************

* * Inform class agent and handle exceptions
  state_read_access.

  result = ADDRESS.

           " GET_ADDRESS
  endmethod.


  method GET_AVERAGE_MARK.
***BUILD 090501
     " returning RESULT
     " raising CX_OS_OBJECT_NOT_FOUND
************************************************************************
* Purpose        : Get Attribute AVERAGE_MARK
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : The object state is loaded, result is set
*
* OO Exceptions  : CX_OS_OBJECT_NOT_FOUND
*
* Implementation : -
*
************************************************************************
* Changelog:
* - 2000-03-14   : (BGR) Version 2.0
* - 2000-07-28   : (SB)  OO Exceptions
************************************************************************

* * Inform class agent and handle exceptions
  state_read_access.

  result = AVERAGE_MARK.

           " GET_AVERAGE_MARK
  endmethod.


  method GET_ELLIGIBLE.
***BUILD 090501
     " returning RESULT
     " raising CX_OS_OBJECT_NOT_FOUND
************************************************************************
* Purpose        : Get Attribute ELLIGIBLE
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : The object state is loaded, result is set
*
* OO Exceptions  : CX_OS_OBJECT_NOT_FOUND
*
* Implementation : -
*
************************************************************************
* Changelog:
* - 2000-03-14   : (BGR) Version 2.0
* - 2000-07-28   : (SB)  OO Exceptions
************************************************************************

* * Inform class agent and handle exceptions
  state_read_access.

  result = ELLIGIBLE.

           " GET_ELLIGIBLE
  endmethod.


  method GET_EMAIL.
***BUILD 090501
     " returning RESULT
     " raising CX_OS_OBJECT_NOT_FOUND
************************************************************************
* Purpose        : Get Attribute EMAIL
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : The object state is loaded, result is set
*
* OO Exceptions  : CX_OS_OBJECT_NOT_FOUND
*
* Implementation : -
*
************************************************************************
* Changelog:
* - 2000-03-14   : (BGR) Version 2.0
* - 2000-07-28   : (SB)  OO Exceptions
************************************************************************

* * Inform class agent and handle exceptions
  state_read_access.

  result = EMAIL.

           " GET_EMAIL
  endmethod.


  method GET_FIRSTNAME.
***BUILD 090501
     " returning RESULT
     " raising CX_OS_OBJECT_NOT_FOUND
************************************************************************
* Purpose        : Get Attribute FIRSTNAME
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : The object state is loaded, result is set
*
* OO Exceptions  : CX_OS_OBJECT_NOT_FOUND
*
* Implementation : -
*
************************************************************************
* Changelog:
* - 2000-03-14   : (BGR) Version 2.0
* - 2000-07-28   : (SB)  OO Exceptions
************************************************************************

* * Inform class agent and handle exceptions
  state_read_access.

  result = FIRSTNAME.

           " GET_FIRSTNAME
  endmethod.


  method GET_LASTNAME.
***BUILD 090501
     " returning RESULT
     " raising CX_OS_OBJECT_NOT_FOUND
************************************************************************
* Purpose        : Get Attribute LASTNAME
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : The object state is loaded, result is set
*
* OO Exceptions  : CX_OS_OBJECT_NOT_FOUND
*
* Implementation : -
*
************************************************************************
* Changelog:
* - 2000-03-14   : (BGR) Version 2.0
* - 2000-07-28   : (SB)  OO Exceptions
************************************************************************

* * Inform class agent and handle exceptions
  state_read_access.

  result = LASTNAME.

           " GET_LASTNAME
  endmethod.


  method GET_PHONE.
***BUILD 090501
     " returning RESULT
     " raising CX_OS_OBJECT_NOT_FOUND
************************************************************************
* Purpose        : Get Attribute PHONE
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : The object state is loaded, result is set
*
* OO Exceptions  : CX_OS_OBJECT_NOT_FOUND
*
* Implementation : -
*
************************************************************************
* Changelog:
* - 2000-03-14   : (BGR) Version 2.0
* - 2000-07-28   : (SB)  OO Exceptions
************************************************************************

* * Inform class agent and handle exceptions
  state_read_access.

  result = PHONE.

           " GET_PHONE
  endmethod.


  method GET_STUDENT_ID.
***BUILD 090501
     " returning RESULT
     " raising CX_OS_OBJECT_NOT_FOUND
************************************************************************
* Purpose        : Get Attribute STUDENT_ID
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : The object state is loaded, result is set
*
* OO Exceptions  : CX_OS_OBJECT_NOT_FOUND
*
* Implementation : -
*
************************************************************************
* Changelog:
* - 2000-03-14   : (BGR) Version 2.0
* - 2000-07-28   : (SB)  OO Exceptions
************************************************************************

* * Inform class agent and handle exceptions
  state_read_access.

  result = STUDENT_ID.

           " GET_STUDENT_ID
  endmethod.


  method IF_OS_STATE~GET.
***BUILD 090501
     " returning result type ref to object
************************************************************************
* Purpose        : Get state.
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : -
*
* OO Exceptions  : -
*
* Implementation : -
*
************************************************************************
* Changelog:
* - 2000-03-07   : (BGR) Initial Version 2.0
************************************************************************
* GENERATED: Do not modify
************************************************************************

  data: STATE_OBJECT type ref to CL_OS_STATE.

  create object STATE_OBJECT.
  call method STATE_OBJECT->SET_STATE_FROM_OBJECT( ME ).
  result = STATE_OBJECT.

  endmethod.


  method IF_OS_STATE~HANDLE_EXCEPTION.
***BUILD 090501
     " importing I_EXCEPTION type ref to IF_OS_EXCEPTION_INFO optional
     " importing I_EX_OS type ref to CX_OS_OBJECT_NOT_FOUND optional
************************************************************************
* Purpose        : Handles exceptions during attribute access.
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : -
*
* OO Exceptions  : CX_OS_OBJECT_NOT_FOUND
*
* Implementation : If an exception is raised during attribut access,
*                  this method is called and the exception is passed
*                  as a paramater. The default is to raise the exception
*                  again, so that the caller can handle the exception.
*                  But it is also possible to handle the exception
*                  here in the callee.
*
************************************************************************
* Changelog:
* - 2000-03-07   : (BGR) Initial Version 2.0
* - 2000-08-02   : (SB)  OO Exceptions
************************************************************************
* Modify if you like
************************************************************************

  if i_ex_os is not initial.
    raise exception i_ex_os.
  endif.

  endmethod.


  method IF_OS_STATE~INIT.
***BUILD 090501
"#EC NEEDED
************************************************************************
* Purpose        : Initialisation of the transient state partition.
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : Transient state is initial.
*
* OO Exceptions  : -
*
* Implementation : Caution!: Avoid Throwing ACCESS Events.
*
************************************************************************
* Changelog:
* - 2000-03-07   : (BGR) Initial Version 2.0
************************************************************************
* Modify if you like
************************************************************************

  endmethod.


  method IF_OS_STATE~INVALIDATE.
***BUILD 090501
"#EC NEEDED
************************************************************************
* Purpose        : Do something before all persistent attributes are
*                  cleared.
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : -
*
* OO Exceptions  : -
*
* Implementation : Whatever you like to do.
*
************************************************************************
* Changelog:
* - 2000-03-07   : (BGR) Initial Version 2.0
************************************************************************
* Modify if you like
************************************************************************

  endmethod.


  method IF_OS_STATE~SET.
***BUILD 090501
     " importing I_STATE type ref to object
************************************************************************
* Purpose        : Set state.
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : -
*
* OO Exceptions  : -
*
* Implementation : -
*
************************************************************************
* Changelog:
* - 2000-03-07   : (BGR) Initial Version 2.0
************************************************************************
* GENERATED: Do not modify
************************************************************************

  data: STATE_OBJECT type ref to CL_OS_STATE.

  STATE_OBJECT ?= I_STATE.
  call method STATE_OBJECT->SET_OBJECT_FROM_STATE( ME ).

  endmethod.


  method SET_ADDRESS.
***BUILD 090501
     " importing I_ADDRESS
     " raising CX_OS_OBJECT_NOT_FOUND
************************************************************************
* Purpose        : Set attribute ADDRESS
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : The object state is loaded, attribute is set
*
* OO Exceptions  : CX_OS_OBJECT_NOT_FOUND
*
* Implementation : -
*
************************************************************************
* Changelog:
* - 2000-03-14   : (BGR) Version 2.0
* - 2000-07-28   : (SB)  OO Exceptions
* - 2000-10-04   : (SB)  Namespaces
************************************************************************

* * Inform class agent and handle exceptions
  state_write_access.

  if ( I_ADDRESS <> ADDRESS ).

    ADDRESS = I_ADDRESS.

*   * Inform class agent and handle exceptions
    state_changed.

  endif. "( I_ADDRESS <> ADDRESS )

           " GET_ADDRESS
  endmethod.


  method SET_AVERAGE_MARK.
***BUILD 090501
     " importing I_AVERAGE_MARK
     " raising CX_OS_OBJECT_NOT_FOUND
************************************************************************
* Purpose        : Set attribute AVERAGE_MARK
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : The object state is loaded, attribute is set
*
* OO Exceptions  : CX_OS_OBJECT_NOT_FOUND
*
* Implementation : -
*
************************************************************************
* Changelog:
* - 2000-03-14   : (BGR) Version 2.0
* - 2000-07-28   : (SB)  OO Exceptions
* - 2000-10-04   : (SB)  Namespaces
************************************************************************

* * Inform class agent and handle exceptions
  state_write_access.

  if ( I_AVERAGE_MARK <> AVERAGE_MARK ).

    AVERAGE_MARK = I_AVERAGE_MARK.

*   * Inform class agent and handle exceptions
    state_changed.

  endif. "( I_AVERAGE_MARK <> AVERAGE_MARK )

           " GET_AVERAGE_MARK
  endmethod.


  method SET_ELLIGIBLE.
***BUILD 090501
     " importing I_ELLIGIBLE
     " raising CX_OS_OBJECT_NOT_FOUND
************************************************************************
* Purpose        : Set attribute ELLIGIBLE
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : The object state is loaded, attribute is set
*
* OO Exceptions  : CX_OS_OBJECT_NOT_FOUND
*
* Implementation : -
*
************************************************************************
* Changelog:
* - 2000-03-14   : (BGR) Version 2.0
* - 2000-07-28   : (SB)  OO Exceptions
* - 2000-10-04   : (SB)  Namespaces
************************************************************************

* * Inform class agent and handle exceptions
  state_write_access.

  if ( I_ELLIGIBLE <> ELLIGIBLE ).

    ELLIGIBLE = I_ELLIGIBLE.

*   * Inform class agent and handle exceptions
    state_changed.

  endif. "( I_ELLIGIBLE <> ELLIGIBLE )

           " GET_ELLIGIBLE
  endmethod.


  method SET_EMAIL.
***BUILD 090501
     " importing I_EMAIL
     " raising CX_OS_OBJECT_NOT_FOUND
************************************************************************
* Purpose        : Set attribute EMAIL
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : The object state is loaded, attribute is set
*
* OO Exceptions  : CX_OS_OBJECT_NOT_FOUND
*
* Implementation : -
*
************************************************************************
* Changelog:
* - 2000-03-14   : (BGR) Version 2.0
* - 2000-07-28   : (SB)  OO Exceptions
* - 2000-10-04   : (SB)  Namespaces
************************************************************************

* * Inform class agent and handle exceptions
  state_write_access.

  if ( I_EMAIL <> EMAIL ).

    EMAIL = I_EMAIL.

*   * Inform class agent and handle exceptions
    state_changed.

  endif. "( I_EMAIL <> EMAIL )

           " GET_EMAIL
  endmethod.


  method SET_FIRSTNAME.
***BUILD 090501
     " importing I_FIRSTNAME
     " raising CX_OS_OBJECT_NOT_FOUND
************************************************************************
* Purpose        : Set attribute FIRSTNAME
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : The object state is loaded, attribute is set
*
* OO Exceptions  : CX_OS_OBJECT_NOT_FOUND
*
* Implementation : -
*
************************************************************************
* Changelog:
* - 2000-03-14   : (BGR) Version 2.0
* - 2000-07-28   : (SB)  OO Exceptions
* - 2000-10-04   : (SB)  Namespaces
************************************************************************

* * Inform class agent and handle exceptions
  state_write_access.

  if ( I_FIRSTNAME <> FIRSTNAME ).

    FIRSTNAME = I_FIRSTNAME.

*   * Inform class agent and handle exceptions
    state_changed.

  endif. "( I_FIRSTNAME <> FIRSTNAME )

           " GET_FIRSTNAME
  endmethod.


  method SET_LASTNAME.
***BUILD 090501
     " importing I_LASTNAME
     " raising CX_OS_OBJECT_NOT_FOUND
************************************************************************
* Purpose        : Set attribute LASTNAME
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : The object state is loaded, attribute is set
*
* OO Exceptions  : CX_OS_OBJECT_NOT_FOUND
*
* Implementation : -
*
************************************************************************
* Changelog:
* - 2000-03-14   : (BGR) Version 2.0
* - 2000-07-28   : (SB)  OO Exceptions
* - 2000-10-04   : (SB)  Namespaces
************************************************************************

* * Inform class agent and handle exceptions
  state_write_access.

  if ( I_LASTNAME <> LASTNAME ).

    LASTNAME = I_LASTNAME.

*   * Inform class agent and handle exceptions
    state_changed.

  endif. "( I_LASTNAME <> LASTNAME )

           " GET_LASTNAME
  endmethod.


  method SET_PHONE.
***BUILD 090501
     " importing I_PHONE
     " raising CX_OS_OBJECT_NOT_FOUND
************************************************************************
* Purpose        : Set attribute PHONE
*
* Version        : 2.0
*
* Precondition   : -
*
* Postcondition  : The object state is loaded, attribute is set
*
* OO Exceptions  : CX_OS_OBJECT_NOT_FOUND
*
* Implementation : -
*
************************************************************************
* Changelog:
* - 2000-03-14   : (BGR) Version 2.0
* - 2000-07-28   : (SB)  OO Exceptions
* - 2000-10-04   : (SB)  Namespaces
************************************************************************

* * Inform class agent and handle exceptions
  state_write_access.

  if ( I_PHONE <> PHONE ).

    PHONE = I_PHONE.

*   * Inform class agent and handle exceptions
    state_changed.

  endif. "( I_PHONE <> PHONE )

           " GET_PHONE
  endmethod.


  METHOD zif_zave_student_p~get_address.
    rv_address = get_address( ).
  ENDMETHOD.


  METHOD zif_zave_student_p~get_avg_mark.
    rv_avg_mark = get_average_mark( ).
  ENDMETHOD.


  METHOD zif_zave_student_p~get_elligible.
    rf_elligible = get_elligible( ).
  ENDMETHOD.


  METHOD zif_zave_student_p~get_email.
    rv_email = get_email( ).
  ENDMETHOD.


  METHOD zif_zave_student_p~get_first_name.
    rv_fname = get_firstname( ).
  ENDMETHOD.


  METHOD zif_zave_student_p~get_id.
    rv_id = get_student_id( ).
  ENDMETHOD.


  METHOD zif_zave_student_p~get_last_name.
    rv_last_name = get_lastname( ).
  ENDMETHOD.


  METHOD zif_zave_student_p~get_phone_number.
    rv_phone_no = get_phone( ).
  ENDMETHOD.


  METHOD zif_zave_student_p~set_address.
    set_address( iv_address ).
  ENDMETHOD.


  METHOD zif_zave_student_p~set_avg_mark.
    set_average_mark( iv_avg_mark ).
  ENDMETHOD.


  METHOD zif_zave_student_p~set_elligible.
    set_elligible( if_elligible ).
  ENDMETHOD.


  METHOD zif_zave_student_p~set_email.
    set_email( iv_email ).
  ENDMETHOD.


  METHOD zif_zave_student_p~set_first_name.
    set_firstname( iv_fname ).
  ENDMETHOD.


  METHOD zif_zave_student_p~set_id.
    student_id = iv_id.
  ENDMETHOD.


  METHOD zif_zave_student_p~set_last_name.
    set_lastname( iv_lastname ).
  ENDMETHOD.


  METHOD zif_zave_student_p~set_phone_number.
    set_phone( iv_phone_no ).
  ENDMETHOD.
ENDCLASS.