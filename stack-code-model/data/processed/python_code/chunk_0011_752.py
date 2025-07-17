class ZAVE_FPM_CL_REPOSITORY_FACTORY definition
  public
  final
  create public .

public section.

  interfaces ZIF_ZAVE_STUDENT_REP .

  types MVT_REP_ID type I .
  types:
    BEGIN OF mst_repository_class_name,
        repository_id TYPE i,
        class_name    TYPE clasname,
      END OF mst_repository_class_name .
  types:
    mtt_repository_class_names TYPE HASHED TABLE OF mst_repository_class_name WITH UNIQUE KEY repository_id .

  constants:
    BEGIN OF gc_services,
        student TYPE mvt_rep_id VALUE 1,
      END OF gc_services .

  class-methods CLASS_CONSTRUCTOR .
  class-methods GET_INSTANCE
    returning
      value(RO_INSTANCE) type ref to ZAVE_FPM_CL_REPOSITORY_FACTORY .
  class-methods SET_CLASS_MAP
    importing
      !IT_CLASS_MAP type MTT_REPOSITORY_CLASS_NAMES .
  methods CONSTRUCTOR .
  methods SET_REPOSITORY
    importing
      !IV_REPO_ID type MVT_REP_ID
      !IO_REPOSITORY type ref to OBJECT .
  PROTECTED SECTION.
private section.

  class-data SO_INSTANCE type ref to ZAVE_FPM_CL_REPOSITORY_FACTORY .
  data:
    mt_repository_map TYPE STANDARD TABLE OF REF TO object WITH DEFAULT KEY .
  data MT_REPOSITORY_CLASS_NAMES type MTT_REPOSITORY_CLASS_NAMES .

  methods GET_REPOSITORY
    importing
      !IV_REPO_ID type MVT_REP_ID
    returning
      value(RO_REPOSITORY) type ref to OBJECT .
ENDCLASS.



CLASS ZAVE_FPM_CL_REPOSITORY_FACTORY IMPLEMENTATION.


  METHOD class_constructor.
    so_instance = NEW #( ).
  ENDMETHOD.


  METHOD constructor.

    DO.

      ASSIGN COMPONENT sy-index of STRUCTURE gc_services TO FIELD-SYMBOL(<lv_service_name>).

      IF sy-subrc = 4.
        EXIT.
      ENDIF.

      APPEND INITIAL LINE TO mt_repository_map.

    ENDDO.
  ENDMETHOD.


  METHOD get_instance.
    ro_instance = so_instance.
  ENDMETHOD.


  METHOD get_repository.

    ro_repository = mt_repository_map[ iv_repo_id ].

    IF ro_repository IS NOT BOUND.
      ASSERT mt_repository_class_names IS NOT INITIAL.
      DATA(lv_class) = mt_repository_class_names[ repository_id = iv_repo_id ]-class_name.
      CREATE OBJECT ro_repository TYPE (lv_class).
      mt_repository_map[ iv_repo_id ] = ro_repository.
    ENDIF.

  ENDMETHOD.


  METHOD set_class_map.
    DATA(lo_instance) = get_instance( ).
    lo_instance->mt_repository_class_names = it_class_map.
  ENDMETHOD.


  METHOD set_repository.
    mt_repository_map[ iv_repo_id ] = io_repository.
  ENDMETHOD.


  METHOD zif_zave_student_rep~create_student.
    CAST zif_zave_student_rep( get_repository( gc_services-student  ) )->create_student( is_student ).
  ENDMETHOD.


  METHOD zif_zave_student_rep~delete_student.
    CAST zif_zave_student_rep( get_repository( gc_services-student ) )->delete_student( iv_id ).
  ENDMETHOD.


  METHOD zif_zave_student_rep~get_all_students.
    rt_students = CAST zif_zave_student_rep(
                        get_repository( gc_services-student )
                          )->get_all_students( ).
  ENDMETHOD.


  METHOD zif_zave_student_rep~get_student_by_id.
    ro_student = CAST zif_zave_student_rep( get_repository( gc_services-student ) )->get_student_by_id( iv_id ).
  ENDMETHOD.


  METHOD zif_zave_student_rep~update_student.
    CAST zif_zave_student_rep( get_repository( gc_services-student ) )->update_student( io_student ).
  ENDMETHOD.
ENDCLASS.