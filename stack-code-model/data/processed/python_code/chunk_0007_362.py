class ZCL_BI_STATIC definition
  public
  final
  create public .

*"* public components of class ZCL_BI_STATIC
*"* do not include other source files here!!!
public section.

  class-methods GET_WHERE
    importing
      !IT_SELECT type RS_T_SELECT
    returning
      value(EV_WHERE) type STRING .
protected section.
*"* protected components of class ZCL_BI_STATIC
*"* do not include other source files here!!!
private section.
*"* private components of class ZCL_BI_STATIC
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCL_BI_STATIC IMPLEMENTATION.


method get_where.

  data:
    ls_select like line of it_select.

  data:
    l_not  type string,
    l_last type string,
    l_low  type string,
    l_high type string.

  loop at it_select into ls_select.

    at new fieldnm.
      if ev_where is initial.
        concatenate ev_where '(' into ev_where separated by space.
      else.
        concatenate ev_where 'and (' into ev_where separated by space.
      endif.
    endat.

    if l_last eq ls_select-fieldnm.
      concatenate ev_where 'or' into ev_where separated by space.
    endif.

    "Ñáðàñûâàåì çíà÷åíèå not
    clear l_not.
    "Åñëè çíàê â ls_select ðàâåí Å, òî çàïîëíÿåì l_not
    if ls_select-sign eq 'E'.
      l_not = 'not'.
    endif.

    "Çàïîëíÿåì l_low è l_high ñîîòâåòñòâóþùèìè çíà÷åíèÿìè èç ls_select
    concatenate '''' ls_select-low  '''' into l_low.
    concatenate '''' ls_select-high '''' into l_high.

    "Åñëè â îïöèÿõ åñòü âûáîð çíà÷åíèé èç äèàïàçîíà, ôîðìèðóåì ñîîòâåòñòâóþùèé ñèíòàêñèñ â ev_where
    if ls_select-option eq 'BT'.
      concatenate ev_where l_not ls_select-fieldnm 'between' l_low 'and' l_high into ev_where separated by space.
    else.
      concatenate ev_where l_not ls_select-fieldnm ls_select-option l_low into ev_where separated by space.
    endif.

    l_last = ls_select-fieldnm.
    "Â ôèíàëå îáðàáîòêè çàêðûâàåì ñèíòàêñèñè çàïðîñà
    at end of fieldnm.
      concatenate ev_where ')' into ev_where separated by space.
    endat.

  endloop.

endmethod.
ENDCLASS.