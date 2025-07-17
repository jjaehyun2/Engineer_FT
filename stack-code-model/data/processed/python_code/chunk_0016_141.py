class ZCL_REST_SERVICE_HANDLER definition
  public
  inheriting from CL_REST_HTTP_HANDLER
  create public .

public section.

  methods CONSTRUCTOR .

  methods IF_REST_APPLICATION~GET_ROOT_HANDLER
    redefinition .
protected section.
private section.

  data MT_RESOURCE_METADATA type ZREST_RESOURCE_METADATA_T .
ENDCLASS.



CLASS ZCL_REST_SERVICE_HANDLER IMPLEMENTATION.


  METHOD constructor.
    super->constructor( ).

    mt_resource_metadata = VALUE #( ( template      = '/scarr/{CARRID}'
                                      handler_class = 'ZCL_REST_SOURCE_SCARR' )

                                    ( template      = '/scarr'
                                      handler_class = 'ZCL_REST_SOURCE_SCARR'
                                      is_query      = abap_true )  ).

  ENDMETHOD.


  METHOD if_rest_application~get_root_handler.

    DATA lt_parameter	   TYPE abap_parmbind_tab.
    DATA lr_parameter    TYPE REF TO data.


    DATA(lo_rest_handler) = NEW cl_rest_router( ).

    LOOP AT mt_resource_metadata ASSIGNING FIELD-SYMBOL(<ls_resource_metadata>).

      lt_parameter = VALUE #( ( name  = 'IS_RESOURCE_METADATA'
                                kind  = cl_abap_objectdescr=>exporting
                                value = REF #( <ls_resource_metadata> ) ) ).

      lo_rest_handler->attach( iv_template      = <ls_resource_metadata>-template
                               iv_handler_class = 'ZCL_REST_SERVICE_RESOURCE'
                               it_parameter     = lt_parameter  ).
    ENDLOOP.

    ro_root_handler = lo_rest_handler.

  ENDMETHOD.
ENDCLASS.