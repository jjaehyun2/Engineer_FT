class ZCL_CARROS definition
  public
  final
  create public .

public section.

  interfaces ZINT_CARROS .
protected section.
private section.
ENDCLASS.



CLASS ZCL_CARROS IMPLEMENTATION.


  method ZINT_CARROS~MONTA.
      resultado = |Nome:{ nome } Cor:{ cor } Potencia:{ potencia } Tanques Gasolina:{ tanques_gasolina }|.
  endmethod.
ENDCLASS.