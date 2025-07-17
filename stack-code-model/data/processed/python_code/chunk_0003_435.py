class ZCL_ZODATA4_MPC definition
  public
  inheriting from /IWBEP/CL_V4_ABS_MODEL_PROV
  create public .

public section.

  types:
         TS_ZENTITYNAME type USR02 .
  types:
         TT_ZENTITYNAME type standard table of TS_ZENTITYNAME .

  methods /IWBEP/IF_V4_MP_BASIC~DEFINE
    redefinition .
protected section.
private section.

  methods DEFINE_ZENTITYNAME
    importing
      !IO_MODEL type ref to /IWBEP/IF_V4_MED_MODEL
    raising
      /IWBEP/CX_GATEWAY .
ENDCLASS.



CLASS ZCL_ZODATA4_MPC IMPLEMENTATION.


  method /IWBEP/IF_V4_MP_BASIC~DEFINE.
*&----------------------------------------------------------------------------------------------*
*&* This class has been generated on 28.05.2019 10:22:32 in client 001
*&*
*&*       WARNING--> NEVER MODIFY THIS CLASS <--WARNING
*&*   If you want to change the MPC implementation, use the
*&*   generated methods inside MPC subclass - ZCL_ZODATA4_MPC_EXT
*&-----------------------------------------------------------------------------------------------*
  define_zentityname( io_model ).
  endmethod.


  method DEFINE_ZENTITYNAME.
*&----------------------------------------------------------------------------------------------*
*&* This class has been generated on 28.05.2019 10:22:32 in client 001
*&*
*&*       WARNING--> NEVER MODIFY THIS CLASS <--WARNING
*&*   If you want to change the MPC implementation, use the
*&*   generated methods inside MPC subclass - ZCL_ZODATA4_MPC_EXT
*&-----------------------------------------------------------------------------------------------*

 DATA lo_entity_type    TYPE REF TO /iwbep/if_v4_med_entity_type.
 DATA lo_property       TYPE REF TO /iwbep/if_v4_med_prim_prop.
 DATA lv_zentityname  TYPE usr02.
***********************************************************************************************************************************
*   ENTITY - zentityname
***********************************************************************************************************************************
 lo_entity_type = io_model->create_entity_type_by_struct( iv_entity_type_name = 'ZENTITYNAME' is_structure = lv_zentityname
                                                          iv_add_conv_to_prim_props = abap_true ). "#EC NOTEXT

 lo_entity_type->set_edm_name( 'zentityname' ).             "#EC NOTEXT

***********************************************************************************************************************************
*   Properties
***********************************************************************************************************************************
 lo_property = lo_entity_type->create_prim_property( iv_property_name = 'BNAME' ). "#EC NOTEXT
 lo_property->set_add_annotations( abap_true ).
 lo_property->set_edm_name( 'bname' ).                      "#EC NOTEXT
 lo_property->set_edm_type( iv_edm_type = 'String' ).       "#EC NOTEXT
 lo_property->set_is_key( ).
 lo_property->set_max_length( iv_max_length = '12' ).       "#EC NOTEXT
  endmethod.
ENDCLASS.