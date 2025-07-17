class ZCL_VALUE definition
  public
  final
  create public .

public section.

  class-methods REDUCE_DECIMALS_NO_ROUND
    importing
      !I_INPUT type ANY
      !I_DECIMAL type N
    returning
      value(E_OUTPUT) type STRING .
  class-methods TO_CURRENCY_FORMAT
    importing
      !I_INPUT type ANY
      !I_CURRENCY type CURRENCY
    returning
      value(E_OUTPUT) type STRING .
protected section.
private section.
ENDCLASS.



CLASS ZCL_VALUE IMPLEMENTATION.


  METHOD reduce_decimals_no_round.

    DATA: lv_value_string TYPE string.

* Joga o valor para uma string
    lv_value_string = i_input.
    CONDENSE lv_value_string.
    e_output = lv_value_string.

* Calcula cadas decimais atuais
    FIND '.' IN lv_value_string MATCH OFFSET DATA(lv_position).
    CHECK sy-subrc = 0.

    DATA(lv_lenght) = strlen( lv_value_string ).

* Verifica se é um número negativo
    FIND '-' IN lv_value_string.
    IF sy-subrc = 0.
      DATA(lv_current_decimal) = lv_lenght - lv_position - 2.
    ELSE.
      lv_current_decimal = lv_lenght - lv_position - 1.
    ENDIF.

    CHECK lv_current_decimal >= i_decimal.

* Reduz para a casa decimal desejada
    IF i_decimal = 0.
      DATA(lv_new_lenght) = lv_lenght - ( lv_current_decimal + 1 ).
    ELSE.
      lv_new_lenght = lv_lenght - ( lv_current_decimal - i_decimal ).
    ENDIF.
    e_output = lv_value_string(lv_new_lenght).

  ENDMETHOD.


  METHOD to_currency_format.

    DATA: lv_p_2     TYPE p DECIMALS 2,
          lv_value_c TYPE c LENGTH 30.

    e_output = i_input.

* Check if it's number
    CHECK e_output CO '0123456789.- '.
    FIND '.' IN e_output MATCH OFFSET DATA(lv_position).
    CHECK sy-subrc = 0.

* Converte para duas casas decimais senão o write não funciona
    DATA(lv_value) = zcl_value=>reduce_decimals_no_round( EXPORTING i_input   = i_input
                                                                    i_decimal = 2 ).
* Joga para um campo do tipo p
    lv_p_2 = lv_value.

* Converte para notação de moeda
    WRITE lv_p_2 TO lv_value_c CURRENCY i_currency.
    CONDENSE lv_value_c.

* Verifica se é um numero negativo
    lv_position = strlen( lv_value_c ) - 1.
    IF lv_value_c+lv_position(1) = '-'.
      lv_value_c = '-' && lv_value_c(lv_position).
    ENDIF.

* Retorna valor
    e_output = lv_value_c.

  ENDMETHOD.
ENDCLASS.