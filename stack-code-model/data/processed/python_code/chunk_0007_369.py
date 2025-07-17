class ZCL_ZAVE_STUDENT_REP definition
  public
  final
  create public .

public section.

  interfaces ZIF_ZAVE_STUDENT_REP .

  types:
    mtt_students TYPE STANDARD TABLE OF REF TO zave_cl_student_e WITH NON-UNIQUE DEFAULT KEY .
protected section.
private section.
ENDCLASS.



CLASS ZCL_ZAVE_STUDENT_REP IMPLEMENTATION.


  METHOD zif_zave_student_rep~create_student.
    TRY .
        DATA(lo_student_p) = zca_zave_student_p=>agent->create_persistent( i_student_id = is_student-id ).

        lo_student_p->zif_zave_student_p~set_first_name( is_student-fname ).
        lo_student_p->zif_zave_student_p~set_last_name( is_student-lname ).
        lo_student_p->zif_zave_student_p~set_phone_number( is_student-phone ).
        lo_student_p->zif_zave_student_p~set_address( is_student-address ).
        lo_student_p->zif_zave_student_p~set_email( is_student-email ).
        lo_student_p->zif_zave_student_p~set_elligible( 'X' ).

        COMMIT WORK.

      CATCH cx_os_object_existing.
    ENDTRY.
  ENDMETHOD.


  METHOD zif_zave_student_rep~delete_student.
    TRY.
        zca_zave_student_p=>agent->delete_persistent( i_student_id = iv_id ).

        COMMIT WORK.

      CATCH cx_os_object_not_existing.
    ENDTRY.
  ENDMETHOD.


  METHOD zif_zave_student_rep~get_all_students.
    DATA: lo_query_no_filter TYPE REF TO if_os_query.
    lo_query_no_filter = cl_os_system=>get_query_manager( )->create_query( ).

    TRY .
        DATA(lt_result) = zca_zave_student_p=>agent->if_os_ca_persistency~get_persistent_by_query( i_query = lo_query_no_filter ).

        LOOP AT lt_result ASSIGNING FIELD-SYMBOL(<lo_entry>).
          DATA(lo_student_p) = CAST zcl_zave_student_p( <lo_entry> ).
          INSERT NEW zave_cl_student_e( lo_student_p ) INTO TABLE rt_students.
        ENDLOOP.
      CATCH cx_os_object_not_found.
    ENDTRY.
  ENDMETHOD.


  METHOD zif_zave_student_rep~get_student_by_id.
    TRY .
        DATA(lo_student) = zca_zave_student_p=>agent->get_persistent( i_student_id = iv_id ).
      CATCH cx_os_object_not_found.
    ENDTRY.
    ro_student = NEW zave_cl_student_e( lo_student ).
  ENDMETHOD.


  METHOD zif_zave_student_rep~update_student.
    TRY .
        DATA(lo_student_p) = zca_zave_student_p=>agent->get_persistent( i_student_id = io_student->mo_student_p->get_id( ) ).

        lo_student_p->zif_zave_student_p~set_first_name( io_student->mo_student_p->get_first_name( ) ).
        lo_student_p->zif_zave_student_p~set_last_name( io_student->mo_student_p->get_last_name( ) ).
        lo_student_p->zif_zave_student_p~set_phone_number( io_student->mo_student_p->get_phone_number( ) ).
        lo_student_p->zif_zave_student_p~set_address( io_student->mo_student_p->get_address( ) ).
        lo_student_p->zif_zave_student_p~set_email( io_student->mo_student_p->get_email( ) ).
        lo_student_p->zif_zave_student_p~set_avg_mark( io_student->mo_student_p->get_avg_mark( ) ).
        lo_student_p->zif_zave_student_p~set_elligible( io_student->mo_student_p->get_elligible( ) ).

        COMMIT WORK.

      CATCH cx_os_object_not_found.
    ENDTRY.
  ENDMETHOD.
ENDCLASS.