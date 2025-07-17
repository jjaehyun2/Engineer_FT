class ZCL_LOAD_BALANCER definition
  public
  final
  create protected .

public section.

  class-methods GET_LOAD_BALANCER
    returning
      value(RO_INSTANCE) type ref to ZCL_LOAD_BALANCER .
  methods SERVER
    returning
      value(RV_SERVER) type STRING .
protected section.

  methods CONSTRUCTOR .
private section.

  types:
    mtt_servers TYPE SORTED TABLE OF string WITH NON-UNIQUE DEFAULT KEY .

  class-data SO_INSTANCE type ref to ZCL_LOAD_BALANCER .
  data MT_SERVERS type MTT_SERVERS .
ENDCLASS.



CLASS ZCL_LOAD_BALANCER IMPLEMENTATION.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Protected Method ZCL_LOAD_BALANCER->CONSTRUCTOR
* +-------------------------------------------------------------------------------------------------+
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD constructor.
    INSERT CONV #( 'Server I' )   INTO TABLE mt_servers.
    INSERT CONV #( 'Server II' )  INTO TABLE mt_servers.
    INSERT CONV #( 'Server III' ) INTO TABLE mt_servers.
    INSERT CONV #( 'Server IV' )  INTO TABLE mt_servers.
    INSERT CONV #( 'Server V' )   INTO TABLE mt_servers.
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Static Public Method ZCL_LOAD_BALANCER=>GET_LOAD_BALANCER
* +-------------------------------------------------------------------------------------------------+
* | [<-()] RO_INSTANCE                    TYPE REF TO ZCL_LOAD_BALANCER
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD get_load_balancer.
    IF so_instance IS INITIAL.
      so_instance = NEW zcl_load_balancer( ).
    ENDIF.

    ro_instance = so_instance.
  ENDMETHOD.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_LOAD_BALANCER->SERVER
* +-------------------------------------------------------------------------------------------------+
* | [<-()] RV_SERVER                      TYPE        STRING
* +--------------------------------------------------------------------------------------</SIGNATURE>
  METHOD server.
    DATA(lv_seed)   = cl_abap_random=>seed( ).
    DATA(lo_random) = cl_abap_random_int=>create( seed  = lv_seed
                                                  min   = 1
                                                  max   = lines( mt_servers ) ).
    rv_server = mt_servers[ lo_random->get_next( ) ].
  ENDMETHOD.
ENDCLASS.