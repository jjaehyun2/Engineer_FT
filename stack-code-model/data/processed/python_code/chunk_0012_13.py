class ZAVE_FPM_CL_REPOSITORY_INIT definition
  public
  final
  create public .

public section.

  class-methods CLASS_CONSTRUCTOR .
  class-methods INIT_REPOSITORY_FACTORY .
protected section.
private section.

  class-data ST_REPOSITORY_MAP type ZAVE_FPM_CL_REPOSITORY_FACTORY=>MTT_REPOSITORY_CLASS_NAMES .
ENDCLASS.



CLASS ZAVE_FPM_CL_REPOSITORY_INIT IMPLEMENTATION.


  METHOD class_constructor.
    INSERT VALUE #( repository_id = zave_fpm_cl_repository_factory=>gc_services-student
                    class_name = 'ZCL_ZAVE_STUDENT_REP'  ) INTO TABLE st_repository_map.
  ENDMETHOD.


  METHOD init_repository_factory.
    zave_fpm_cl_repository_factory=>set_class_map( st_repository_map  ).
  ENDMETHOD.
ENDCLASS.