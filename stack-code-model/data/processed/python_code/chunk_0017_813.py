class zcl_aps_demo_object_select_fun definition
  public
  final
  create public.

  public section.

    interfaces:
      zif_aps_objectselector.

  protected section.
  private section.
endclass.



class zcl_aps_demo_object_select_fun implementation.
  method zif_aps_objectselector~calculateObjects.
    do 10 times.
      data(currentLoopCounter) = sy-index.

      data(singleExecutionParameters) = zcl_aps_parameterset_factory=>providefunctionunitparameters( i_settings ).

      singleExecutionParameters->addImporting(
        i_parametername  = 'I_INDEX'
        i_parametervalue = ref #( currentLoopCounter )
      ).

      singleExecutionParameters->addExporting( 'E_SQUARE' ).

      insert singleExecutionParameters
      into table result.
    enddo.
  endmethod.

endclass.