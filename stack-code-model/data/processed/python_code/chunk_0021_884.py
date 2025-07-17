class ZCL_REF_TO definition
  public
  final
  create public .

public section.
protected section.
private section.

  methods METHOD1 .
ENDCLASS.



CLASS ZCL_REF_TO IMPLEMENTATION.


  METHOD method1.

    DATA: type_ref_to_table TYPE zref_to.

    WRITE: / 'foobar'.

  ENDMETHOD.
ENDCLASS.