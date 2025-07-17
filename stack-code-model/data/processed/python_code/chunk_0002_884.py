class ZCL_PT_D_ADMIN_DATA definition
  public
  inheriting from /BOBF/CL_LIB_D_SUPERCL_SIMPLE
  final
  create public .

public section.

  methods /BOBF/IF_FRW_DETERMINATION~EXECUTE
    redefinition .
protected section.
private section.
ENDCLASS.



CLASS ZCL_PT_D_ADMIN_DATA IMPLEMENTATION.


  METHOD /bobf/if_frw_determination~execute.
    IF is_ctx-exectime <> /bobf/if_conf_c=>sc_time_at_save.
      RAISE EXCEPTION TYPE /bobf/cx_lib
        EXPORTING
          textid = /bobf/cx_lib=>wrong_determination_time.
    ENDIF.

    DATA(context) = is_ctx.
    context-exectime = /bobf/if_conf_c=>sc_time_before_save.

    NEW /bobf/cl_lib_d_admin_data_tsm( )->/bobf/if_frw_determination~execute(
      EXPORTING
        is_ctx        = context
        it_key        = it_key
        io_read       = io_read
        io_modify     = io_modify
      IMPORTING
        eo_message    = eo_message
        et_failed_key = et_failed_key ).
  ENDMETHOD.
ENDCLASS.