CLASS y_check_is_interface_in_class DEFINITION
  PUBLIC
  INHERITING FROM y_check_base
  CREATE PUBLIC .

  PUBLIC SECTION.

    METHODS constructor .
  PROTECTED SECTION.
    METHODS inspect_tokens REDEFINITION.
    METHODS execute_check REDEFINITION.

  PRIVATE SECTION.
    DATA public_method_counter TYPE i VALUE 0.
ENDCLASS.



CLASS Y_CHECK_IS_INTERFACE_IN_CLASS IMPLEMENTATION.


  METHOD constructor.
    super->constructor( ).

    settings-pseudo_comment = '"#EC INTF_IN_CLASS' ##NO_TEXT.
    settings-disable_threshold_selection = abap_true.
    settings-threshold = 1.
    settings-prio = c_warning.
    settings-documentation = |{ c_docs_path-checks }interface-in-class.md|.

    set_check_message( '&1 public methods without interface!' ).
  ENDMETHOD.


  METHOD execute_check.
    LOOP AT ref_scan_manager->get_structures( ) ASSIGNING FIELD-SYMBOL(<structure>)
      WHERE stmnt_type EQ scan_struc_stmnt_type-class_definition.

      is_testcode = test_code_detector->is_testcode( <structure> ).

      TRY.
          DATA(check_config) = check_configurations[ apply_on_testcode = abap_true ].
        CATCH cx_sy_itab_line_not_found.
          IF is_testcode EQ abap_true.
            CONTINUE.
          ENDIF.
      ENDTRY.

      READ TABLE ref_scan_manager->get_statements( ) INTO DATA(statement_for_message)
              INDEX <structure>-stmnt_from.
      public_method_counter = 0.

      LOOP AT ref_scan_manager->get_statements( ) ASSIGNING FIELD-SYMBOL(<statement>)
        FROM <structure>-stmnt_from TO <structure>-stmnt_to.

        IF get_token_abs( <statement>-from ) EQ 'PROTECTED' OR
           get_token_abs( <statement>-from ) EQ 'PRIVATE'.
          EXIT.
        ENDIF.

        inspect_tokens( statement = <statement> ).
      ENDLOOP.

      DATA(check_configuration) = detect_check_configuration( error_count = public_method_counter
                                                              statement = statement_for_message ).

      IF check_configuration IS INITIAL.
        CONTINUE.
      ENDIF.

      raise_error( statement_level     = statement_for_message-level
                   statement_index     = <structure>-stmnt_from
                   statement_from      = statement_for_message-from
                   error_priority      = check_configuration-prio
                   parameter_01        = |{ public_method_counter }| ).
    ENDLOOP.
  ENDMETHOD.


  METHOD inspect_tokens.
    CHECK get_token_abs( statement-from ) = 'METHODS'
      AND get_token_abs( statement-from + 1 ) <> 'CONSTRUCTOR'
      AND get_token_abs( statement-from + 2 ) <> 'ABSTRACT'
      AND get_token_abs( statement-to ) <> 'REDEFINITION'.
    CHECK get_token_abs( statement-from ) = 'METHODS'
      AND get_token_abs( statement-from + 2 ) <> 'FOR'
      AND get_token_abs( statement-from + 3 ) <> 'TESTING'.
    ADD 1 TO public_method_counter.
  ENDMETHOD.
ENDCLASS.