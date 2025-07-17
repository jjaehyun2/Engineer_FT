class ZCL_REST_SERVICE_RESOURCE definition
  public
  inheriting from CL_REST_RESOURCE
  create public .

public section.

  methods CONSTRUCTOR
    importing
      !IS_RESOURCE_METADATA type ZREST_RESOURCE_METADATA_S .

  methods IF_REST_RESOURCE~GET
    redefinition .
protected section.
private section.

  data MS_RESOURCE_METADATA type ZREST_RESOURCE_METADATA_S .
ENDCLASS.



CLASS ZCL_REST_SERVICE_RESOURCE IMPLEMENTATION.


  method CONSTRUCTOR.
    super->constructor( ).
    ms_resource_metadata = is_resource_metadata.
  endmethod.


  METHOD if_rest_resource~get.

    DATA lo_rest_concrete_source TYPE REF TO zif_rest_resource_handler_base.

    IF ms_resource_metadata-is_function_import = abap_true.
      "toDo
    ELSE.

      CREATE OBJECT lo_rest_concrete_source TYPE (ms_resource_metadata-handler_class).
      IF ms_resource_metadata-is_query = abap_true.
        mo_response = lo_rest_concrete_source->query( io_request     = mo_request
                                                      io_context     = mo_context
                                                      iv_conditional = mv_conditional
                                                      io_response    = mo_response ).
      ELSE.
        mo_response = lo_rest_concrete_source->read( io_request     = mo_request
                                                     io_response    = mo_response
                                                     io_context     = mo_context
                                                     iv_conditional = mv_conditional ).
      ENDIF.

    ENDIF.

  ENDMETHOD.
ENDCLASS.