class ZBIL_BRF_GROUPING_RULES definition
  public
  final
  create public .

  public section.
    class-methods GET_ALLOWED_FOR_PRODUCT
      importing
        !PRODUCT      type CHAR40
      returning
        value(RETURN) TYPE ZBIL_BRF_GROUPING_CONFIG_T .
    class-methods GET_KEYFIELDS_FOR_PRODUCT
      importing
        !PRODUCT      type CHAR40
      returning
        value(RETURN) TYPE TCHAR255 .
  protected section.
  private section.
ENDCLASS.



CLASS ZBIL_BRF_GROUPING_RULES IMPLEMENTATION.
  METHOD GET_ALLOWED_FOR_PRODUCT.
    CONSTANTS:lv_function_id TYPE if_fdt_types=>id VALUE '0242AC1100021EE8A1BD90FCA835CAA2'.
    types: begin of ty_input,
             product_code type char255,
           end of ty_input.
    DATA:lv_timestamp  TYPE timestamp,
         lt_name_value TYPE abap_parmbind_tab,
         ls_name_value TYPE abap_parmbind,
         lr_data       TYPE REF TO data,
         lx_fdt        TYPE REF TO cx_fdt,
         lr_input      TYPE REF TO data,
         ls_input      type ty_input,
         ls_output     type line of  ZBIL_BRF_GROUPING_CONFIG_T.

    FIELD-SYMBOLS: <la_any>    TYPE table,
                   <lr_input>  TYPE any,
                   <fs_field>  type any,
                   <fs_result> type any.
    GET TIME STAMP FIELD lv_timestamp.

    ls_name_value-name = 'INPUT'.
    CREATE DATA lr_input TYPE ty_input.
    ASSIGN lr_input->* TO <lr_input>.
    ls_input-product_code = product.
    <lr_input> = ls_input.
    lr_data = lr_input.
    cl_fdt_function_process=>move_data_to_data_object( EXPORTING ir_data             = lr_data
                                                                 iv_function_id      = lv_function_id
                                                                 iv_data_object      = '0242AC1100021EE8A1BD4CC5978FCA75' "INPUT
                                                                 iv_timestamp        = lv_timestamp
                                                                 iv_trace_generation = abap_false
                                                                 iv_has_ddic_binding = abap_false
                                                       IMPORTING er_data             = ls_name_value-value ).
    INSERT ls_name_value INTO TABLE lt_name_value.
    cl_fdt_function_process=>get_data_object_reference( EXPORTING iv_function_id      = lv_function_id
                                                                  iv_data_object      = '_V_RESULT'
                                                                  iv_timestamp        = lv_timestamp
                                                                  iv_trace_generation = abap_false
                                                        IMPORTING er_data             = lr_data ).
    ASSIGN lr_data->* TO <la_any>.
    TRY.
        cl_fdt_function_process=>process( EXPORTING iv_function_id = lv_function_id
                                                    iv_timestamp   = lv_timestamp
                                          IMPORTING ea_result      = <la_any>
                                          CHANGING  ct_name_value  = lt_name_value ).
        loop at <la_any> assigning <fs_result>.
          ASSIGN COMPONENT 'ADDITIONAL_CODE' OF STRUCTURE <fs_result> TO <fs_field>.
          ls_output-additional_service = <fs_field>.
          ASSIGN COMPONENT 'ALLOWED' OF STRUCTURE <fs_result> TO <fs_field>.
          ls_output-allowed = <fs_field>.
          append ls_output to return.
        endloop.

      CATCH cx_fdt into lx_fdt.
****************************************************************************************************
* You can check CX_FDT->MT_MESSAGE for error handling.
****************************************************************************************************
    ENDTRY.
  ENDMETHOD.

  METHOD GET_KEYFIELDS_FOR_PRODUCT.
    CONSTANTS:lv_function_id TYPE if_fdt_types=>id VALUE '0242AC1100021EE8A1BC78E0CF130A01'.
    types: begin of ty_input,
             product_code type char255,
           end of ty_input.
    DATA:lv_timestamp  TYPE timestamp,
         lt_name_value TYPE abap_parmbind_tab,
         ls_name_value TYPE abap_parmbind,
         lr_data       TYPE REF TO data,
         lx_fdt        TYPE REF TO cx_fdt,
         lr_input      TYPE REF TO data,
         ls_input      type ty_input,
         lv_output     type char255.
    FIELD-SYMBOLS: <la_any>   TYPE table,
                   <lr_input> TYPE any,
                   <fs_output> type any,
                   <fs_field> type any.
    GET TIME STAMP FIELD lv_timestamp.

    ls_name_value-name = 'INPUT'.
    CREATE DATA lr_input TYPE ty_input .
    ASSIGN lr_input->* TO <lr_input>.
    ls_input-product_code = product.
    <lr_input> = ls_input.

    lr_data = lr_input.
    cl_fdt_function_process=>move_data_to_data_object( EXPORTING ir_data             = lr_data
                                                                 iv_function_id      = lv_function_id
                                                                 iv_data_object      = '0242AC1100021EE8A1BC12C4574CA9C3' "INPUT
                                                                 iv_timestamp        = lv_timestamp
                                                                 iv_trace_generation = abap_false
                                                                 iv_has_ddic_binding = abap_false
                                                       IMPORTING er_data             = ls_name_value-value ).
    INSERT ls_name_value INTO TABLE lt_name_value.
    cl_fdt_function_process=>get_data_object_reference( EXPORTING iv_function_id      = lv_function_id
                                                                  iv_data_object      = '_V_RESULT'
                                                                  iv_timestamp        = lv_timestamp
                                                                  iv_trace_generation = abap_false
                                                        IMPORTING er_data             = lr_data ).
    ASSIGN lr_data->* TO <la_any>.
    TRY.
        cl_fdt_function_process=>process( EXPORTING iv_function_id = lv_function_id
                                                    iv_timestamp   = lv_timestamp
                                          IMPORTING ea_result      = <la_any>
                                          CHANGING  ct_name_value  = lt_name_value ).
        loop at <la_any> assigning <fs_output>.
            ASSIGN COMPONENT 'FIELD' OF STRUCTURE <fs_output> TO <fs_field>.
            lv_output = <fs_field>.
            append lv_output to return.
        endloop.
      CATCH cx_fdt into lx_fdt.
****************************************************************************************************
* You can check CX_FDT->MT_MESSAGE for error handling.
****************************************************************************************************
    ENDTRY.
  ENDMETHOD.

ENDCLASS.