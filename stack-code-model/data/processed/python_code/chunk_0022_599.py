class YCL_AIM_PRJ_D_DERIVE_USERDATA definition
  public
  inheriting from /BOBF/CL_LIB_D_SUPERCLASS
  create public .

public section.

  methods /BOBF/IF_FRW_DETERMINATION~EXECUTE
    redefinition .
protected section.

  data MV_DETAIL_INCLUDE_NAME type STRING value 'USER_DETAIL'. "#EC NOTEXT
  data MV_UNAME_ATTRIBUTE type STRING value 'UNAME'. "#EC NOTEXT
private section.
ENDCLASS.



CLASS YCL_AIM_PRJ_D_DERIVE_USERDATA IMPLEMENTATION.


METHOD /bobf/if_frw_determination~execute.

  FIELD-SYMBOLS <ls_user_detail>  TYPE yaim_userdata_detail.
  FIELD-SYMBOLS <lv_uname>        TYPE uname.
  FIELD-SYMBOLS <lt_node_data>    TYPE ANY TABLE.
  FIELD-SYMBOLS <lv_key>          TYPE /bobf/conf_key.

  /bobf/cl_frw_factory=>get_configuration( is_ctx-bo_key )->get_node(
    EXPORTING
      iv_node_key = is_ctx-node_key
    IMPORTING
      es_node     = DATA(ls_node) ).

  DATA lt_node_data_ref TYPE REF TO data.
  DATA ls_node_data_ref TYPE REF TO data.
  CREATE DATA lt_node_data_ref TYPE (ls_node-data_table_type).

  ASSIGN lt_node_data_ref->* TO <lt_node_data>.

  io_read->retrieve(
    EXPORTING
      iv_node                 = is_ctx-node_key    " Node Name
      it_key                  = it_key    " Key Table
      iv_fill_data            = abap_true
    IMPORTING
      et_data                 = <lt_node_data>
  ).

  LOOP AT <lt_node_data> ASSIGNING FIELD-SYMBOL(<ls_node_data>).
    ASSIGN COMPONENT mv_uname_attribute OF STRUCTURE <ls_node_data> TO <lv_uname>.
    ASSERT sy-subrc = 0.
    ASSIGN COMPONENT mv_detail_include_name OF STRUCTURE <ls_node_data> TO <ls_user_detail>.
    ASSERT sy-subrc = 0.
    ASSIGN COMPONENT /bobf/if_conf_c=>sc_attribute_name_key OF STRUCTURE <ls_node_data> TO <lv_key>.
    ASSERT sy-subrc = 0.

    ycl_aim_userdata=>get_instance( )->get_userdetails(
      EXPORTING
        iv_uname              = <lv_uname>
      CHANGING
        cs_userdetails_subset = <ls_user_detail>
    ).

    GET REFERENCE OF <ls_node_data> INTO ls_node_data_ref.
    io_modify->update(
      EXPORTING
        iv_node           = is_ctx-node_key    " Node
        iv_key            = <lv_key>    " Key
        is_data           = ls_node_data_ref    " Data
    ).

  ENDLOOP.

ENDMETHOD.
ENDCLASS.