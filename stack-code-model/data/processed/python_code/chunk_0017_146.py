class YCL_AIM_D_ADMIN_DATA definition
  public
  inheriting from /BOBF/CL_D_ADMIN_DATA
  create public .

public section.

  constants GC_LOCAL_ADMIN_INCLUDE_NAME type FIELDNAME value 'LOCAL_ADMIN_DATA'. "#EC NOTEXT

  methods CONSTRUCTOR .

  methods /BOBF/IF_FRW_DETERMINATION~EXECUTE
    redefinition .
protected section.

  data MV_LOCAL_ADMIN_INCLUDE_NAME type FIELDNAME .

  methods SET_LOCAL_ADMIN_DATA
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_DET
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IO_MODIFY type ref to /BOBF/IF_FRW_MODIFY
    exporting
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
private section.
ENDCLASS.



CLASS YCL_AIM_D_ADMIN_DATA IMPLEMENTATION.


METHOD /bobf/if_frw_determination~execute.
    IF is_ctx-exectime <> /bobf/if_conf_c=>sc_time_after_loading.
*      The BOPF determination which determines the admin-data shall not run after loading,
*      but only the custom part which determines the transient local attributes
      super->/bobf/if_frw_determination~execute(
        EXPORTING
          is_ctx        = is_ctx
          it_key        = it_key
          io_read       = io_read
          io_modify     = io_modify
        IMPORTING
          eo_message    = eo_message
          et_failed_key = et_failed_key
             ).
    ENDIF.

    me->set_local_admin_data(
      EXPORTING
        is_ctx        = is_ctx    " Context Information for Determinations
        it_key        = it_key    " Key Table
        io_read       = io_read    " Interface to Reading Data
        io_modify     = io_modify    " Interface to Change Data
      IMPORTING
        eo_message    = eo_message    " Message Object
    ).

  ENDMETHOD.


METHOD constructor.
    super->constructor( ).

    mv_local_admin_include_name = gc_local_admin_include_name.
  ENDMETHOD.


METHOD set_local_admin_data.
    FIELD-SYMBOLS <ls_local_admin_data> TYPE yaim_admin_data_local.
    FIELD-SYMBOLS <lt_node_data>        TYPE ANY TABLE.
    DATA ls_userdata_detail_all         TYPE yaim_userdata_detail_all.

    CLEAR eo_message.

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
      ASSIGN COMPONENT mv_local_admin_include_name OF STRUCTURE <ls_node_data> TO <ls_local_admin_data>.
      ASSERT sy-subrc = 0. "make sure the include is properly named. For deviating names, inherit from this class and change the value in the constructor.

      ASSIGN COMPONENT /bobf/if_conf_c=>sc_attribute_name_key OF STRUCTURE <ls_node_data> TO FIELD-SYMBOL(<lv_key>).
      ASSERT sy-subrc = 0.
      ASSIGN COMPONENT 'DATETIME_CR' OF STRUCTURE <ls_node_data> TO FIELD-SYMBOL(<lv_datetime_cr>).
      ASSERT sy-subrc = 0.
      ASSIGN COMPONENT 'USER_ID_CR'  OF STRUCTURE <ls_node_data> TO FIELD-SYMBOL(<lv_user_id_cr>).
      ASSERT sy-subrc = 0.
      ASSIGN COMPONENT 'DATETIME_CH' OF STRUCTURE <ls_node_data> TO FIELD-SYMBOL(<lv_datetime_ch>).
      ASSERT sy-subrc = 0.
      ASSIGN COMPONENT 'USER_ID_CH'  OF STRUCTURE <ls_node_data> TO FIELD-SYMBOL(<lv_user_id_ch>).
      ASSERT sy-subrc = 0.

*    created on and by
      CONVERT TIME STAMP <lv_datetime_cr> TIME ZONE sy-zonlo INTO DATE <ls_local_admin_data>-created_on_date TIME <ls_local_admin_data>-created_on_time.
      ycl_aim_userdata=>get_instance( )->get_userdetails(
        EXPORTING
          iv_uname              = <lv_user_id_cr>
        IMPORTING
          es_userdetails        = ls_userdata_detail_all
      ).
      <ls_local_admin_data>-created_by = ls_userdata_detail_all-formatted_full_name.

*    changed on and by
      CONVERT TIME STAMP <lv_datetime_ch> TIME ZONE sy-zonlo INTO DATE <ls_local_admin_data>-changed_on_date TIME <ls_local_admin_data>-changed_on_time.
      ycl_aim_userdata=>get_instance( )->get_userdetails(
        EXPORTING
          iv_uname              = <lv_user_id_ch>
        IMPORTING
          es_userdetails        = ls_userdata_detail_all
      ).
      <ls_local_admin_data>-changed_by = ls_userdata_detail_all-formatted_full_name.

      DATA lr_node_data TYPE REF TO data.
      GET REFERENCE OF <ls_node_data> INTO lr_node_data.
      io_modify->update(
        EXPORTING
          iv_node           = is_ctx-node_key    " Node
          iv_key            = <lv_key>    " Key
          is_data           = lr_node_data
          it_changed_fields = VALUE #(
                                  ( |CREATED_ON_DATE| )
                                  ( |CREATED_ON_TIME| )
                                  ( |CREATED_BY| )
                                  ( |CHANGED_ON_DATE| )
                                  ( |CHANGED_ON_TIME| )
                                  ( |CHANGED_BY| )
                              )
      ).

    ENDLOOP.
  ENDMETHOD.
ENDCLASS.