REPORT zabapgit_api_create_and_pull.

PARAMETERS:
  p_url    TYPE text100 DEFAULT 'https://github.com/abapGit-tests/VIEW.git' OBLIGATORY,
  p_branch TYPE text100 DEFAULT 'refs/heads/master' OBLIGATORY,
  p_devc   TYPE devclass DEFAULT '$VIEW' OBLIGATORY.

START-OF-SELECTION.
  PERFORM run.

FORM run.

  TRY.
      DATA(lo_repo) = zcl_abapgit_repo_srv=>get_instance( )->new_online(
        iv_url         = CONV #( p_url )
        iv_branch_name = CONV #( p_branch )
        iv_package     = p_devc ).

      DATA(ls_checks) = lo_repo->deserialize_checks( ).

* if there are conflicts or other stuff, this has to be filled in LS_CHECKS

      lo_repo->deserialize( ls_checks ).

    CATCH zcx_abapgit_exception INTO DATA(lx_error).
      WRITE: / 'Error,', lx_error->get_text( ).
  ENDTRY.

ENDFORM.