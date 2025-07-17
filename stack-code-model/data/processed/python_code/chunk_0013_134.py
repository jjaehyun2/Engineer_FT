class Y_CHECK_EXITING_CATCH definition
  public
  inheriting from Y_CHECK_BASE
  create public .

public section.

  methods CONSTRUCTOR .
  PROTECTED SECTION.
    METHODS inspect_tokens REDEFINITION .

  PRIVATE SECTION.
    METHODS get_next_token_from_index IMPORTING index         TYPE i
                                      RETURNING VALUE(result) TYPE stokesx.

ENDCLASS.



CLASS Y_CHECK_EXITING_CATCH IMPLEMENTATION.


  METHOD CONSTRUCTOR.
    super->constructor( ).

    settings-pseudo_comment = '"#EC EXITING_CATCH' ##NO_TEXT.
    settings-disable_threshold_selection = abap_true.
    settings-threshold = 0.
    settings-prio = c_error.
    settings-documentation = |{ c_docs_path-checks }exiting-catch.md|.

    set_check_message( 'Catch block terminated with &1 !' ).
  ENDMETHOD.


  METHOD GET_NEXT_TOKEN_FROM_INDEX.
    LOOP AT ref_scan_manager->tokens ASSIGNING FIELD-SYMBOL(<token>)
      FROM index WHERE type EQ 'I'.
      IF result IS INITIAL.
        result = <token>.
        EXIT.
      ENDIF.
    ENDLOOP.
  ENDMETHOD.


  METHOD inspect_tokens.
    CHECK get_next_token_from_index( statement-from )-str EQ 'CATCH' AND
      (
        ( get_next_token_from_index( statement-to + 1 )-str EQ 'CHECK' ) OR
        ( get_next_token_from_index( statement-to + 1 )-str EQ 'EXIT' ) OR
        ( get_next_token_from_index( statement-to + 1 )-str EQ 'LEAVE' ) OR
        ( get_next_token_from_index( statement-to + 1 )-str EQ 'RETURN' )
      ).

    DATA(check_configuration) = detect_check_configuration( statement ).

    IF check_configuration IS INITIAL.
      RETURN.
    ENDIF.

    raise_error( statement_level      = statement-level
                 statement_index      = index
                 statement_from       = statement-from
                 error_priority       = check_configuration-prio
                 parameter_01         = get_next_token_from_index( statement-to + 1 )-str ).
  ENDMETHOD.
ENDCLASS.