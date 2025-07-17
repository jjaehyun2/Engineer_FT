class ZCL_CONST_STATIC definition
  public
  final
  create public .

public section.

  class-methods GET_RANGE
    importing
      !I_PATH type SIMPLE
    returning
      value(ET_RANGE) type ZIRANGE .
  class-methods GET_VALUES
    importing
      !I_PATH type SIMPLE
    returning
      value(ET_VALUES) type ZIVALUES .
  class-methods GET_VALUE
    importing
      !I_PATH type SIMPLE
    returning
      value(E_VALUE) type STRING .
protected section.
private section.
ENDCLASS.



CLASS ZCL_CONST_STATIC IMPLEMENTATION.


  method get_range.

    et_range =
      zcl_abap_static=>values2range(
        get_values( i_path ) ).

  endmethod.


  method get_value.

    data lt_values type zivalues.
    lt_values = get_values( i_path ).

    data ls_value like line of lt_values.
    read table lt_values into ls_value index 1.

    check sy-subrc eq 0.

    e_value = ls_value-id.

  endmethod.


  method get_values.

    data l_section_id type ze_const_section_id.
    data l_const_id type ze_const_id.
    split i_path at  '/' into l_section_id l_const_id.

    data l_logsys type logsys.
    l_logsys = zcl_abap_static=>get_logsys( ).

    select value as id
      from ztconst_i
      into table et_values
      where
        section_id eq l_section_id and
        const_id   eq l_const_id and
        logsys     eq l_logsys.
    if sy-subrc ne 0.
      select value as id
        from ztconst_i
        into table et_values
        where
          section_id eq l_section_id and
          const_id   eq l_const_id and
          logsys     eq ''.
    endif.

  endmethod.
ENDCLASS.