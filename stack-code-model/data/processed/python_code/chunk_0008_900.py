CLASS zcl_app_rule_amdp_nl_lft_cond DEFINITION
  PUBLIC
  INHERITING FROM zcl_app_rule_amdp_new_line_lft
  CREATE PUBLIC .

  PUBLIC SECTION.

  PROTECTED SECTION.
    METHODS set_add_indent REDEFINITION.
    DATA mv_cond_fulfilled_set TYPE abap_bool.
    DATA mv_cond_fulfilled TYPE abap_bool.
  PRIVATE SECTION.

ENDCLASS.



CLASS zcl_app_rule_amdp_nl_lft_cond IMPLEMENTATION.


  METHOD set_add_indent.
    DATA lr_rule_cond TYPE REF TO zif_app_rule_condition.

    CLEAR mv_add_indent.
    IF is_logic_active( ) = abap_false.
      RETURN.
    ENDIF.

    IF mv_cond_fulfilled_set = abap_false.
      mv_cond_fulfilled_set = abap_true.
      IF mr_rule_data->rule_cond_class IS INITIAL.
        mv_cond_fulfilled = abap_true.
      ELSE.
        CREATE OBJECT lr_rule_cond TYPE (mr_rule_data->rule_cond_class).
        mv_cond_fulfilled = lr_rule_cond->is_cond_fulfilled( me ).
      ENDIF.
    ENDIF.

    IF mv_cond_fulfilled = abap_false.
      RETURN.
    ENDIF.

    super->set_add_indent( ).
  ENDMETHOD.



ENDCLASS.