class ZCL_REST_RESOURCE_UTILITIES definition
  public
  final
  create public .

public section.

  interfaces ZIF_REST_RESOURCE_UTILITIES .
protected section.
private section.
ENDCLASS.



CLASS ZCL_REST_RESOURCE_UTILITIES IMPLEMENTATION.


  METHOD zif_rest_resource_utilities~deserialize_json.

    DATA lv_json TYPE string.
    DATA lo_rest_entity TYPE REF TO if_rest_entity.

    lo_rest_entity = io_request->get_entity( ).
    lv_json        = lo_rest_entity->get_string_data( ).

    /ui2/cl_json=>deserialize(
      EXPORTING
           json         = lv_json
            pretty_name = abap_true
      CHANGING
           data = ev_data ).

  ENDMETHOD.


  METHOD zif_rest_resource_utilities~serialize_json.

    DATA lv_string_data TYPE string.
    DATA lo_rest_entity TYPE REF TO if_rest_entity.

    lo_rest_entity = io_response->create_entity( ).
    lv_string_data = /ui2/cl_json=>serialize( data        = iv_data
                                              compress    = abap_true
                                              pretty_name = abap_true ).

    lo_rest_entity->set_content_type( if_rest_media_type=>gc_appl_json ).
    lo_rest_entity->set_string_data( lv_string_data ).

  ENDMETHOD.
ENDCLASS.