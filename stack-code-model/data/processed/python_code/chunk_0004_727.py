class ZCL_AL30_EXAMPLE_EXIT definition
  public
  final
  create public .

public section.

*"* public components of class ZCL_AL30_EXAMPLE_EXIT
*"* do not include other source files here!!!
  interfaces ZIF_AL30_EXIT_CLASS .
  PROTECTED SECTION.
*"* protected components of class ZCL_AL30_EXAMPLE_EXIT
*"* do not include other source files here!!!
  PRIVATE SECTION.
*"* private components of class ZCL_AL30_EXAMPLE_EXIT
*"* do not include other source files here!!!
ENDCLASS.



CLASS ZCL_AL30_EXAMPLE_EXIT IMPLEMENTATION.


  METHOD zif_al30_exit_class~exit_after_save_data.

  ENDMETHOD.


  METHOD zif_al30_exit_class~exit_before_read_data.
  ENDMETHOD.


  METHOD zif_al30_exit_class~exit_before_save_data.

  ENDMETHOD.


  METHOD zif_al30_exit_class~exit_process_catalog_of_field.

  ENDMETHOD.


  METHOD zif_al30_exit_class~exit_verify_change_row_data.

  ENDMETHOD.


  METHOD zif_al30_exit_class~exit_verify_field_data.

  ENDMETHOD.
ENDCLASS.