CLASS /hec1/cl_bopf_config_assoc DEFINITION
  PUBLIC
  INHERITING FROM /bobf/cl_lib_c_superclass
  FINAL
  CREATE PUBLIC

  GLOBAL FRIENDS /bobf/if_frw_association .

  PUBLIC SECTION.

    METHODS /bobf/if_frw_association~create
        REDEFINITION .
    METHODS /bobf/if_frw_association~resolve
        REDEFINITION .
  PROTECTED SECTION.
private section.

  methods RESOLVE_APP_DEF_MASTER_NODE
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_ROOT_DATACENTER
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_APP_DEF_MASTER_NODE_PC
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_APP_DEF_MASTER_NODE_SA
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_APP_NODE_TIER
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_APP_SERVER_TIER
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_APP_SPC_SOLUTION
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_DB_SERVER_TIER
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_DB_NODE_SERVER_INST
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_APP_SPC_TIER
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_DB_NODE_TIER
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_APP_STANDBY_NODE
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_APP_STANDBY_NODE_PC
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_APP_STANDBY_NODE_SA
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_APP_SERVER_APP_QTY
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_APP_STORAGE_APP_QTY
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_APP_STORAGE_APP_SPC
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_DB_STORAGE_DB_QTY
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_DB_DEF_MASTER_NODE
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_DB_DEF_MASTER_NODE_PC
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_DB_DEF_MASTER_NODE_SA
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_DB_NONE_MASTER_NODE
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_DB_NONE_MASTER_NODE_PC
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
  methods RESOLVE_DB_NONE_MASTER_NODE_SA
    importing
      !IS_CTX type /BOBF/S_FRW_CTX_ASSOC
      !IT_KEY type /BOBF/T_FRW_KEY
      !IO_READ type ref to /BOBF/IF_FRW_READ
      !IS_PARAMETERS type ref to DATA optional
      !IT_FILTERED_ATTRIBUTES type /BOBF/T_FRW_NAME optional
      !IV_INVALIDATE_CACHE type BOOLE_D default ABAP_FALSE
    exporting
      !ET_KEY_LINK type /BOBF/T_FRW_KEY_LINK
      !ET_FAILED_KEY type /BOBF/T_FRW_KEY
      !EO_MESSAGE type ref to /BOBF/IF_FRW_MESSAGE
    raising
      /BOBF/CX_FRW .
ENDCLASS.



CLASS /HEC1/CL_BOPF_CONFIG_ASSOC IMPLEMENTATION.


  METHOD /bobf/if_frw_association~create.
                                                            "#EC NEEDED
**TRY.
*CALL METHOD SUPER->/BOBF/IF_FRW_ASSOCIATION~CREATE
*  EXPORTING
*    IS_CTX          =
*    IT_MODIFICATION =
*    IO_READ         =
*    IO_MODIFY       =
**  IMPORTING
**    eo_message      =
*    .
**  CATCH /bobf/cx_frw.
**ENDTRY.
  ENDMETHOD.


  METHOD /bobf/if_frw_association~resolve.

    CLEAR: et_key_link,
           et_failed_key,
           eo_message.


    TRY.
        CASE is_ctx-assoc_key.
            " ----------------------------------
            " Resolve association from root
            " to data center
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-root-to_datacenter.
            me->resolve_root_datacenter( EXPORTING is_ctx                 = is_ctx
                                                   it_key                 = it_key
                                                   io_read                = io_read
                                                   is_parameters          = is_parameters
                                                   it_filtered_attributes = it_filtered_attributes
                                                   iv_invalidate_cache    = abap_false
                                         IMPORTING et_key_link            = et_key_link
                                                   et_failed_key          = et_failed_key
                                                   eo_message             = eo_message             ).

            " ----------------------------------
            " Resolve association from DB node
            " to DB default master node
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-db_node-to_def_master_node.
            me->resolve_db_def_master_node( EXPORTING is_ctx                 = is_ctx
                                                      it_key                 = it_key
                                                      io_read                = io_read
                                                      is_parameters          = is_parameters
                                                      it_filtered_attributes = it_filtered_attributes
                                                      iv_invalidate_cache    = abap_false
                                            IMPORTING et_key_link            = et_key_link
                                                      et_failed_key          = et_failed_key
                                                      eo_message             = eo_message             ).

            " ----------------------------------
            " Resolve association from DB
            " server performance category to
            " default master node
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-db_server_perform_cat-to_def_master_node.
            me->resolve_db_def_master_node_pc( EXPORTING is_ctx                 = is_ctx
                                                         it_key                 = it_key
                                                         io_read                = io_read
                                                         is_parameters          = is_parameters
                                                         it_filtered_attributes = it_filtered_attributes
                                                         iv_invalidate_cache    = abap_false
                                               IMPORTING et_key_link            = et_key_link
                                                         et_failed_key          = et_failed_key
                                                         eo_message             = eo_message             ).

            " ----------------------------------
            " Resolve association from DB node
            " to tier node
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-db_node-to_tier.
            me->resolve_db_node_tier( EXPORTING is_ctx                 = is_ctx
                                                it_key                 = it_key
                                                io_read                = io_read
                                                is_parameters          = is_parameters
                                                it_filtered_attributes = it_filtered_attributes
                                                iv_invalidate_cache    = abap_false
                                      IMPORTING et_key_link            = et_key_link
                                                et_failed_key          = et_failed_key
                                                eo_message             = eo_message              ).

            " ----------------------------------
            " Resolve association from DB
            " storage amount to default master
            " node
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-db_storage_amount-to_def_master_node.
            me->resolve_db_def_master_node_sa( EXPORTING is_ctx                 = is_ctx
                                                         it_key                 = it_key
                                                         io_read                = io_read
                                                         is_parameters          = is_parameters
                                                         it_filtered_attributes = it_filtered_attributes
                                                         iv_invalidate_cache    = abap_false
                                               IMPORTING et_key_link            = et_key_link
                                                         et_failed_key          = et_failed_key
                                                         eo_message             = eo_message             ).

            " ----------------------------------
            " Resolve association from DB node
            " to DB standby/worker node
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-db_node-to_none_master_node.
            me->resolve_db_none_master_node( EXPORTING is_ctx                 = is_ctx
                                                       it_key                 = it_key
                                                       io_read                = io_read
                                                       is_parameters          = is_parameters
                                                       it_filtered_attributes = it_filtered_attributes
                                                       iv_invalidate_cache    = abap_false
                                             IMPORTING et_key_link            = et_key_link
                                                       et_failed_key          = et_failed_key
                                                       eo_message             = eo_message             ).

            " ----------------------------------
            " Resolve association from DB
            " server performance category to
            " standby/worker node
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-db_server_perform_cat-to_none_master_node.
            me->resolve_db_none_master_node_pc( EXPORTING is_ctx                 = is_ctx
                                                          it_key                 = it_key
                                                          io_read                = io_read
                                                          is_parameters          = is_parameters
                                                          it_filtered_attributes = it_filtered_attributes
                                                          iv_invalidate_cache    = abap_false
                                                IMPORTING et_key_link            = et_key_link
                                                          et_failed_key          = et_failed_key
                                                          eo_message             = eo_message             ).

            " ----------------------------------
            " Resolve association from DB
            " storage amount to standby/worker
            " node
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-db_storage_amount-to_none_master_node.
            me->resolve_db_none_master_node_sa( EXPORTING is_ctx                 = is_ctx
                                                          it_key                 = it_key
                                                          io_read                = io_read
                                                          is_parameters          = is_parameters
                                                          it_filtered_attributes = it_filtered_attributes
                                                          iv_invalidate_cache    = abap_false
                                                IMPORTING et_key_link            = et_key_link
                                                          et_failed_key          = et_failed_key
                                                          eo_message             = eo_message             ).

            " ----------------------------------
            " Resolve association from app node
            " to tier node
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-app_node-to_tier.
            me->resolve_app_node_tier( EXPORTING is_ctx                 = is_ctx
                                                 it_key                 = it_key
                                                 io_read                = io_read
                                                 is_parameters          = is_parameters
                                                 it_filtered_attributes = it_filtered_attributes
                                                 iv_invalidate_cache    = abap_false
                                       IMPORTING et_key_link            = et_key_link
                                                 et_failed_key          = et_failed_key
                                                 eo_message             = eo_message              ).

            " ----------------------------------
            " Resolve association from app node
            " to app default master node
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-app_node-def_master_node.
            me->resolve_app_def_master_node( EXPORTING is_ctx                 = is_ctx
                                                       it_key                 = it_key
                                                       io_read                = io_read
                                                       is_parameters          = is_parameters
                                                       it_filtered_attributes = it_filtered_attributes
                                                       iv_invalidate_cache    = abap_false
                                             IMPORTING et_key_link            = et_key_link
                                                       et_failed_key          = et_failed_key
                                                       eo_message             = eo_message             ).

            " ----------------------------------
            " Resolve association from app
            " server performance category to
            " default master node
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_def_master_node.
            me->resolve_app_def_master_node_pc( EXPORTING is_ctx                 = is_ctx
                                                          it_key                 = it_key
                                                          io_read                = io_read
                                                          is_parameters          = is_parameters
                                                          it_filtered_attributes = it_filtered_attributes
                                                          iv_invalidate_cache    = abap_false
                                                IMPORTING et_key_link            = et_key_link
                                                          et_failed_key          = et_failed_key
                                                          eo_message             = eo_message             ).

            " ----------------------------------
            " Resolve association from app
            " storage amount to default master
            " node
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-app_storage_amount-to_def_master_node.
            me->resolve_app_def_master_node_sa( EXPORTING is_ctx                 = is_ctx
                                                          it_key                 = it_key
                                                          io_read                = io_read
                                                          is_parameters          = is_parameters
                                                          it_filtered_attributes = it_filtered_attributes
                                                          iv_invalidate_cache    = abap_false
                                                IMPORTING et_key_link            = et_key_link
                                                          et_failed_key          = et_failed_key
                                                          eo_message             = eo_message             ).

            " ----------------------------------
            " Resolve association from app node
            " to app standby node
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-app_node-to_standby_node.
            me->resolve_app_standby_node( EXPORTING is_ctx                 = is_ctx
                                                    it_key                 = it_key
                                                    io_read                = io_read
                                                    is_parameters          = is_parameters
                                                    it_filtered_attributes = it_filtered_attributes
                                                    iv_invalidate_cache    = abap_false
                                          IMPORTING et_key_link            = et_key_link
                                                    et_failed_key          = et_failed_key
                                                    eo_message             = eo_message             ).

            " ----------------------------------
            " Resolve association from app
            " server performance category to
            " tier node
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_tier.
            me->resolve_app_spc_tier( EXPORTING is_ctx                 = is_ctx
                                                it_key                 = it_key
                                                io_read                = io_read
                                                is_parameters          = is_parameters
                                                it_filtered_attributes = it_filtered_attributes
                                                iv_invalidate_cache    = abap_false
                                      IMPORTING et_key_link            = et_key_link
                                                et_failed_key          = et_failed_key
                                                eo_message             = eo_message             ).

            " ----------------------------------
            " Resolve association from app
            " server performance category to
            " solution node
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_solution.
            me->resolve_app_spc_solution( EXPORTING is_ctx                 = is_ctx
                                                    it_key                 = it_key
                                                    io_read                = io_read
                                                    is_parameters          = is_parameters
                                                    it_filtered_attributes = it_filtered_attributes
                                                    iv_invalidate_cache    = abap_false
                                          IMPORTING et_key_link            = et_key_link
                                                    et_failed_key          = et_failed_key
                                                    eo_message             = eo_message             ).

            " ----------------------------------
            " Resolve association from app
            " server performance category to
            " standby node
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_standby_node.
            me->resolve_app_standby_node_pc( EXPORTING is_ctx                 = is_ctx
                                                       it_key                 = it_key
                                                       io_read                = io_read
                                                       is_parameters          = is_parameters
                                                       it_filtered_attributes = it_filtered_attributes
                                                       iv_invalidate_cache    = abap_false
                                             IMPORTING et_key_link            = et_key_link
                                                       et_failed_key          = et_failed_key
                                                        eo_message             = eo_message             ).

            " ----------------------------------
            " Resolve association from app
            " storage amount to standby node
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-app_storage_amount-to_standby_node.
            me->resolve_app_standby_node_sa( EXPORTING is_ctx                 = is_ctx
                                                       it_key                 = it_key
                                                       io_read                = io_read
                                                       is_parameters          = is_parameters
                                                       it_filtered_attributes = it_filtered_attributes
                                                       iv_invalidate_cache    = abap_false
                                             IMPORTING et_key_link            = et_key_link
                                                       et_failed_key          = et_failed_key
                                                        eo_message             = eo_message             ).

            " ----------------------------------
            " Resolve association from app
            " storage to app server performance
            " category
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-app_storage-to_app_serv_perf_cat.
            me->resolve_app_storage_app_spc( EXPORTING is_ctx                 = is_ctx
                                                       it_key                 = it_key
                                                       io_read                = io_read
                                                       is_parameters          = is_parameters
                                                       it_filtered_attributes = it_filtered_attributes
                                                       iv_invalidate_cache    = abap_false
                                             IMPORTING et_key_link            = et_key_link
                                                       et_failed_key          = et_failed_key
                                                        eo_message             = eo_message             ).

            " ----------------------------------
            " Resolve association from app
            " server to app storage amount
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-app_server-to_app_storage_amount.
            me->resolve_app_server_app_qty( EXPORTING is_ctx                 = is_ctx
                                                      it_key                 = it_key
                                                      io_read                = io_read
                                                      is_parameters          = is_parameters
                                                      it_filtered_attributes = it_filtered_attributes
                                                      iv_invalidate_cache    = abap_false
                                            IMPORTING et_key_link            = et_key_link
                                                      et_failed_key          = et_failed_key
                                                      eo_message             = eo_message             ).

            " ----------------------------------
            " Resolve association from app
            " storage to app storage amount
            " ----------------------------------
          WHEN /hec1/if_configuration_c=>sc_association-app_storage-to_app_storage_amount.
            me->resolve_app_storage_app_qty( EXPORTING is_ctx                 = is_ctx
                                                       it_key                 = it_key
                                                       io_read                = io_read
                                                       is_parameters          = is_parameters
                                                       it_filtered_attributes = it_filtered_attributes
                                                       iv_invalidate_cache    = abap_false
                                             IMPORTING et_key_link            = et_key_link
                                                       et_failed_key          = et_failed_key
                                                       eo_message             = eo_message             ).

        ENDCASE.
      CATCH /bobf/cx_frw.
    ENDTRY.


  ENDMETHOD.


  METHOD resolve_app_def_master_node_sa.

    DATA: lt_app_node TYPE /hec1/t_data_app_node_ct,
          lr_app_node TYPE REF TO /hec1/s_data_app_node_cs.


    CLEAR: et_key_link,
           et_failed_key,
           eo_message.


    " **********************************
    " Get app server performance
    " category instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_storage_amount-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)                                                          ).


    " **********************************
    " Get app server node
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_parent
                                      IMPORTING et_target_key  = DATA(lt_app_node_key)                                                     ).


    " **********************************
    " Get app server instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
                                                it_key         = lt_app_node_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_app_serv_inst_key)                                  ).

    " **********************************
    " Get app node instanc
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                it_key         = lt_app_serv_inst_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-app_node
                                      IMPORTING et_data        = lt_app_node                                                            ).

    " Get default master node
    LOOP AT        lt_app_node
    REFERENCE INTO lr_app_node
             WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                   hec_master_default            = abap_true.

      INSERT VALUE #( source_key = lr_app_node->parent_key
                      target_key = lr_app_node->key        ) INTO TABLE et_key_link.

    ENDLOOP.

    " No key link found, error message has to be set...
    IF et_key_link IS INITIAL.



    ENDIF.


  ENDMETHOD.


  METHOD resolve_db_def_master_node.

    DATA: lt_db_node TYPE /hec1/t_data_db_node_ct,
          lr_db_node TYPE REF TO /hec1/s_data_db_node_cs.


    CLEAR: et_key_link,
           et_failed_key,
           eo_message.


    " **********************************
    " Get DB instance DB
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)                                               ).

    " **********************************
    " Get all DB nodes
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-instance_db
                                                it_key         = lt_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-db_node
                                      IMPORTING et_data        = lt_db_node                                                   ).

    " Get default Master node
    LOOP AT        lt_db_node
    REFERENCE INTO lr_db_node
             WHERE hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                   hec_master_default           = abap_true.

      INSERT VALUE #( source_key = lr_db_node->parent_key
                      target_key = lr_db_node->key        ) INTO TABLE et_key_link.

    ENDLOOP.

    " No key link found, error message has to be set...
    IF et_key_link IS INITIAL.



    ENDIF.

  ENDMETHOD.


  METHOD resolve_app_standby_node_pc.

    DATA: lt_app_node TYPE /hec1/t_data_app_node_ct,
          lr_app_node TYPE REF TO /hec1/s_data_app_node_cs.


    CLEAR: et_key_link,
           et_failed_key,
           eo_message.


    " **********************************
    " Get app node instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)                                                              ).


    " **********************************
    " Get app server instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_app_serv_inst_key)                                  ).


    " **********************************
    " Get all app node instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                it_key         = lt_app_serv_inst_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-app_node
                                      IMPORTING et_data        = lt_app_node                                                           ).

    " Get standby node
    LOOP AT        lt_app_node
    REFERENCE INTO lr_app_node
             WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-standby.

      INSERT VALUE #( source_key = lr_app_node->parent_key
                      target_key = lr_app_node->key        ) INTO TABLE et_key_link.

    ENDLOOP.

    " No key link found, error message has to be set...
    IF et_key_link IS INITIAL.



    ENDIF.


  ENDMETHOD.


  METHOD resolve_app_storage_app_qty.

    CLEAR: et_key_link,
           et_failed_key,
           eo_message.

    " **********************************
    " Get app server
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_storage-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)
                                                et_failed_key  = et_failed_key                                                   ).

    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
      RETURN. " >>>>>>>
    ENDIF.

    " **********************************
    " Get app server performance cat.
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server-to_parent
                                      IMPORTING et_target_key  = DATA(lt_serv_perf_cat_key)
                                                et_failed_key  = et_failed_key                                                 ).


    " No key link found, error message has to be set...
    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
    ENDIF.

    " **********************************
    " Get app server storage amount
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                it_key         = lt_serv_perf_cat_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_storage_amount
                                      IMPORTING et_key_link    = et_key_link
                                                et_failed_key  = et_failed_key                                                                       ).


  ENDMETHOD.


  METHOD resolve_app_spc_tier.

    CLEAR: et_key_link,
           et_failed_key,
           eo_message.

    " **********************************
    " Get app node
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)
                                                et_key_link    = DATA(lt_key_link)
                                                et_failed_key  = et_failed_key                                                              ).


    " **********************************
    " Get app server instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key_apsi)
                                                et_key_link    = DATA(lt_key_link_apsi)
                                                et_failed_key  = et_failed_key                                               ).

    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
      RETURN. " >>>>>>>
    ENDIF.

    " **********************************
    " Get tier
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                it_key         = lt_key_apsi
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-to_parent
                                      IMPORTING et_key_link    = DATA(lt_key_link_tier)
                                                et_failed_key  = et_failed_key                                                          ).


    " No key link found, error message has to be set...
    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
    ENDIF.

    LOOP AT lt_key_link ASSIGNING FIELD-SYMBOL(<fs_key_link>).
      TRY.
          INSERT VALUE #( source_key = <fs_key_link>-source_key
                          target_key = lt_key_link_tier[ source_key = lt_key_link_apsi[ source_key = <fs_key_link>-target_key ]-target_key ]-target_key ) INTO TABLE et_key_link.

        CATCH cx_sy_itab_line_not_found.
      ENDTRY.
    ENDLOOP.


  ENDMETHOD.


  METHOD resolve_app_def_master_node_pc.

    DATA: lt_app_node TYPE /hec1/t_data_app_node_ct,
          lr_app_node TYPE REF TO /hec1/s_data_app_node_cs.


    CLEAR: et_key_link,
           et_failed_key,
           eo_message.


    " **********************************
    " Get app node instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)                                                              ).


    " **********************************
    " Get app server instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_app_serv_inst_key)                                  ).


    " **********************************
    " Get all app node instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                it_key         = lt_app_serv_inst_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-app_node
                                      IMPORTING et_data        = lt_app_node                                                           ).

    " Get default master node
    LOOP AT        lt_app_node
    REFERENCE INTO lr_app_node
             WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                   hec_master_default            = abap_true.

      INSERT VALUE #( source_key = lr_app_node->parent_key
                      target_key = lr_app_node->key        ) INTO TABLE et_key_link.

    ENDLOOP.

    " No key link found, error message has to be set...
    IF et_key_link IS INITIAL.



    ENDIF.


  ENDMETHOD.


  METHOD resolve_app_standby_node_sa.

    DATA: lt_app_node TYPE /hec1/t_data_app_node_ct,
          lr_app_node TYPE REF TO /hec1/s_data_app_node_cs.


    CLEAR: et_key_link,
           et_failed_key,
           eo_message.


    " **********************************
    " Get app server performance
    " category instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_storage_amount-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)                                                          ).


    " **********************************
    " Get app node instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_parent
                                      IMPORTING et_target_key  = DATA(lt_app_node_key)                                                              ).


    " **********************************
    " Get app server instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
                                                it_key         = lt_app_node_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_app_serv_inst_key)                                  ).


    " **********************************
    " Get all app node instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                it_key         = lt_app_serv_inst_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-app_node
                                      IMPORTING et_data        = lt_app_node                                                           ).

    " Get standby node
    LOOP AT        lt_app_node
    REFERENCE INTO lr_app_node
             WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-standby.

      INSERT VALUE #( source_key = lr_app_node->parent_key
                      target_key = lr_app_node->key        ) INTO TABLE et_key_link.

    ENDLOOP.

    " No key link found, error message has to be set...
    IF et_key_link IS INITIAL.



    ENDIF.


  ENDMETHOD.


  METHOD resolve_app_standby_node.

    DATA: lt_app_node TYPE /hec1/t_data_app_node_ct,
          lr_app_node TYPE REF TO /hec1/s_data_app_node_cs.


    CLEAR: et_key_link,
           et_failed_key,
           eo_message.


    " **********************************
    " Get app server instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)                                                ).

    " **********************************
    " Get all app nodes
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                it_key         = lt_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-app_node
                                      IMPORTING et_data        = lt_app_node                                                            ).

    " Get Standby node
    LOOP AT        lt_app_node
    REFERENCE INTO lr_app_node
             WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-standby.

      INSERT VALUE #( source_key = lr_app_node->parent_key
                      target_key = lr_app_node->key        ) INTO TABLE et_key_link.

    ENDLOOP.

    " No key link found, error message has to be set...
    IF et_key_link IS INITIAL.



    ENDIF.


  ENDMETHOD.


  METHOD resolve_db_node_tier.

    CLEAR: et_key_link,
           et_failed_key,
           eo_message.

    " **********************************
    " Get instance DB
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)
                                                et_failed_key  = et_failed_key                                               ).

    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
      RETURN. " >>>>>>>
    ENDIF.

    " **********************************
    " Get DB server instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-instance_db
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-to_parent
                                      IMPORTING et_target_key  = DATA(lt_db_serv_inst_key)
                                                et_failed_key  = et_failed_key                                                  ).

    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
      RETURN. " >>>>>>>
    ENDIF.


    " **********************************
    " Get tier
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_instance
                                                it_key         = lt_db_serv_inst_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_instance-to_parent
                                      IMPORTING et_key_link    = et_key_link
                                                et_failed_key  = et_failed_key                                                         ).


    " No key link found, error message has to be set...
    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
    ENDIF.


  ENDMETHOD.


  METHOD resolve_app_server_app_qty.

    CLEAR: et_key_link,
           et_failed_key,
           eo_message.

    " **********************************
    " Get app server performance cat.
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)
                                                et_failed_key  = et_failed_key                                                 ).


    " No key link found, error message has to be set...
    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
    ENDIF.

    " **********************************
    " Get app server storage amount
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-app_storage_amount
                                      IMPORTING et_key_link    = et_key_link
                                                et_failed_key  = et_failed_key                                                                       ).


  ENDMETHOD.


  METHOD resolve_db_def_master_node_pc.

    DATA: lt_db_node TYPE /hec1/t_data_db_node_ct,
          lr_db_node TYPE REF TO /hec1/s_data_db_node_cs.


    CLEAR: et_key_link,
           et_failed_key,
           eo_message.


    " **********************************
    " Get DB node instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)                                                             ).


    " **********************************
    " Get instance DB
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_node
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_instance_db_key)                                   ).


    " **********************************
    " Get all DB node instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-instance_db
                                                it_key         = lt_instance_db_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-db_node
                                      IMPORTING et_data        = lt_db_node                                                   ).

    " Get default master node
    LOOP AT        lt_db_node
    REFERENCE INTO lr_db_node
             WHERE hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                   hec_master_default           = abap_true.

      INSERT VALUE #( source_key = lr_db_node->parent_key
                      target_key = lr_db_node->key        ) INTO TABLE et_key_link.

    ENDLOOP.

    " No key link found, error message has to be set...
    IF et_key_link IS INITIAL.



    ENDIF.


  ENDMETHOD.


  METHOD resolve_db_def_master_node_sa.

    DATA: lt_db_node TYPE /hec1/t_data_db_node_ct,
          lr_db_node TYPE REF TO /hec1/s_data_db_node_cs.


    CLEAR: et_key_link,
           et_failed_key,
           eo_message.


    " **********************************
    " Get DB server performance
    " category instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_storage_amount-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)                                                         ).


    " **********************************
    " Get DB server node
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-to_parent
                                      IMPORTING et_target_key  = DATA(lt_db_node_key)                                                     ).


    " **********************************
    " Get instance DB
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_node
                                                it_key         = lt_db_node_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_instance_db_key)                                  ).

    " **********************************
    " Get DB node instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-instance_db
                                                it_key         = lt_instance_db_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-db_node
                                      IMPORTING et_data        = lt_db_node                                                   ).

    " Get default master node
    LOOP AT        lt_db_node
    REFERENCE INTO lr_db_node
             WHERE hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-master AND
                   hec_master_default           = abap_true.

      INSERT VALUE #( source_key = lr_db_node->parent_key
                      target_key = lr_db_node->key        ) INTO TABLE et_key_link.

    ENDLOOP.

    " No key link found, error message has to be set...
    IF et_key_link IS INITIAL.



    ENDIF.


  ENDMETHOD.


  METHOD resolve_db_none_master_node.

    DATA: lt_db_node TYPE /hec1/t_data_db_node_ct,
          lr_db_node TYPE REF TO /hec1/s_data_db_node_cs.


    CLEAR: et_key_link,
           et_failed_key,
           eo_message.


    " **********************************
    " Get instance DB
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)                                               ).

    " **********************************
    " Get all DB nodes
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-instance_db
                                                it_key         = lt_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-db_node
                                      IMPORTING et_data        = lt_db_node                                                   ).

    " Get standby/worker node
    LOOP AT        lt_db_node
    REFERENCE INTO lr_db_node
             WHERE hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-standby OR
                   hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-worker.

      INSERT VALUE #( source_key = lr_db_node->parent_key
                      target_key = lr_db_node->key        ) INTO TABLE et_key_link.

    ENDLOOP.

    " No key link found, error message has to be set...
    IF et_key_link IS INITIAL.



    ENDIF.


  ENDMETHOD.


  METHOD resolve_app_spc_solution.

    CLEAR: et_key_link,
           et_failed_key,
           eo_message.

    " **********************************
    " Get app node
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)
                                                et_key_link    = DATA(lt_key_link)
                                                et_failed_key  = et_failed_key                                                              ).


    " **********************************
    " Get app server instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key_apsi)
                                                et_key_link    = DATA(lt_key_link_apsi)
                                                et_failed_key  = et_failed_key                                               ).

    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
      RETURN. " >>>>>>>
    ENDIF.

    " **********************************
    " Get tier
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                it_key         = lt_key_apsi
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key_tier)
                                                et_key_link    = DATA(lt_key_link_tier)
                                                et_failed_key  = et_failed_key                                                          ).

    " **********************************
    " Get solution
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-tier
                                                it_key         = lt_key_tier
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-tier-to_parent
                                      IMPORTING et_key_link    = DATA(lt_key_link_solution)
                                                et_failed_key  = et_failed_key                                            ).

    " No key link found, error message has to be set...
    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
    ENDIF.

    LOOP AT lt_key_link ASSIGNING FIELD-SYMBOL(<fs_key_link>).
      TRY.
          INSERT VALUE #( source_key = <fs_key_link>-source_key
                          target_key = lt_key_link_solution[ source_key = lt_key_link_tier[ source_key = lt_key_link_apsi[ source_key = <fs_key_link>-target_key ]-target_key ]-target_key ]-target_key )
          INTO TABLE et_key_link.

        CATCH cx_sy_itab_line_not_found.
      ENDTRY.
    ENDLOOP.


  ENDMETHOD.


  METHOD resolve_db_none_master_node_pc.

    DATA: lt_db_node TYPE /hec1/t_data_db_node_ct,
          lr_db_node TYPE REF TO /hec1/s_data_db_node_cs.


    CLEAR: et_key_link,
           et_failed_key,
           eo_message.


    " **********************************
    " Get DB node instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)                                                              ).


    " **********************************
    " Get instance DB
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_node
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_instance_db_key)                                   ).


    " **********************************
    " Get all DB node instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-instance_db
                                                it_key         = lt_instance_db_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-db_node
                                      IMPORTING et_data        = lt_db_node                                                   ).

    " Get standby/worker node
    LOOP AT        lt_db_node
    REFERENCE INTO lr_db_node
             WHERE hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-standby OR
                   hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-worker.

      INSERT VALUE #( source_key = lr_db_node->parent_key
                      target_key = lr_db_node->key        ) INTO TABLE et_key_link.

    ENDLOOP.

    " No key link found, error message has to be set...
    IF et_key_link IS INITIAL.



    ENDIF.


  ENDMETHOD.


  METHOD resolve_app_node_tier.

    CLEAR: et_key_link,
           et_failed_key,
           eo_message.

    " **********************************
    " Get app server instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)
                                                et_failed_key  = et_failed_key                                               ).

    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
      RETURN. " >>>>>>>
    ENDIF.

    " **********************************
    " Get tier
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-to_parent
                                      IMPORTING et_key_link    = et_key_link
                                                et_failed_key  = et_failed_key                                                          ).


    " No key link found, error message has to be set...
    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
    ENDIF.


  ENDMETHOD.


  METHOD resolve_app_storage_app_spc.

    CLEAR: et_key_link,
           et_failed_key,
           eo_message.

    " **********************************
    " Get app server
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_storage-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)
                                                et_failed_key  = et_failed_key                                                   ).

    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
      RETURN. " >>>>>>>
    ENDIF.

    " **********************************
    " Get app server performance cat.
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server-to_parent
                                      IMPORTING et_key_link    = et_key_link
                                                et_failed_key  = et_failed_key                                                 ).


    " No key link found, error message has to be set...
    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
    ENDIF.


  ENDMETHOD.


  METHOD resolve_app_server_tier.

    CLEAR: et_key_link,
           et_failed_key,
           eo_message.


    " **********************************
    " Get app server perf. category
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)
                                                et_key_link    = DATA(lt_key_link)
                                                et_failed_key  = et_failed_key                                                  ).


    " **********************************
    " Get app node
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key_node)
                                                et_key_link    = DATA(lt_key_link_node)
                                                et_failed_key  = et_failed_key                                                              ).


    " **********************************
    " Get app server instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
                                                it_key         = lt_key_node
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key_apsi)
                                                et_key_link    = DATA(lt_key_link_apsi)
                                                et_failed_key  = et_failed_key                                               ).

    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
      RETURN. " >>>>>>>
    ENDIF.

    " **********************************
    " Get tier
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                it_key         = lt_key_apsi
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key_tier)
                                                et_key_link    = DATA(lt_key_link_tier)
                                                et_failed_key  = et_failed_key                                                          ).


    " No key link found, error message has to be set...
    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
    ENDIF.

    LOOP AT lt_key_link ASSIGNING FIELD-SYMBOL(<fs_key_link>).
      TRY.
          INSERT VALUE #( source_key = <fs_key_link>-source_key
                          target_key = lt_key_link_tier[ source_key = lt_key_link_apsi[ source_key = lt_key_link_node[ source_key = <fs_key_link>-target_key ]-target_key ]-target_key ]-target_key )
          INTO TABLE et_key_link.

        CATCH cx_sy_itab_line_not_found.
      ENDTRY.
    ENDLOOP.


  ENDMETHOD.


  METHOD resolve_app_def_master_node.

    DATA: lt_app_node TYPE /hec1/t_data_app_node_ct,
          lr_app_node TYPE REF TO /hec1/s_data_app_node_cs.


    CLEAR: et_key_link,
           et_failed_key,
           eo_message.


    " **********************************
    " Get app server instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)                                                ).

    " **********************************
    " Get all app nodes
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                it_key         = lt_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-app_node
                                      IMPORTING et_data        = lt_app_node                                                            ).

    " Get default master node
    LOOP AT        lt_app_node
    REFERENCE INTO lr_app_node
             WHERE hec_app_clust_node_type_value = /hec1/if_config_constants=>gc_app_clust_node_type-master AND
                   hec_master_default            = abap_true.

      INSERT VALUE #( source_key = lr_app_node->parent_key
                      target_key = lr_app_node->key        ) INTO TABLE et_key_link.

    ENDLOOP.

    " No key link found, error message has to be set...
    IF et_key_link IS INITIAL.



    ENDIF.

  ENDMETHOD.


  METHOD resolve_db_node_server_inst.

    CLEAR: et_key_link,
           et_failed_key,
           eo_message.


    " **********************************
    " Get instance DB
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)
                                                et_key_link    = DATA(lt_key_link)
                                                et_failed_key  = et_failed_key                                                ).


    " **********************************
    " Get DB server instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-instance_db
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key_dbsi)
                                                et_key_link    = DATA(lt_key_link_dbsi)
                                                et_failed_key  = et_failed_key                                                   ).

    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
      RETURN. " >>>>>>>
    ENDIF.


    " No key link found, error message has to be set...
    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
    ENDIF.

    LOOP AT lt_key_link ASSIGNING FIELD-SYMBOL(<fs_key_link>).
      TRY.
          INSERT VALUE #( source_key = <fs_key_link>-source_key
                          target_key = lt_key_link_dbsi[ source_key = <fs_key_link>-target_key ]-target_key )
          INTO TABLE et_key_link.

        CATCH cx_sy_itab_line_not_found.
      ENDTRY.
    ENDLOOP.


  ENDMETHOD.


  METHOD resolve_db_none_master_node_sa.

    DATA: lt_db_node TYPE /hec1/t_data_db_node_ct,
          lr_db_node TYPE REF TO /hec1/s_data_db_node_cs.


    CLEAR: et_key_link,
           et_failed_key,
           eo_message.


    " **********************************
    " Get DB server performance
    " category instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_storage_amount-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)                                                         ).


    " **********************************
    " Get DB node instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_server_perform_cat
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-to_parent
                                      IMPORTING et_target_key  = DATA(lt_db_node_key)                                                     ).


    " **********************************
    " Get instance DB
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-db_node
                                                it_key         = lt_db_node_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_instance_db_key)                                   ).


    " **********************************
    " Get all DB node instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-instance_db
                                                it_key         = lt_instance_db_key
                                                iv_fill_data   = abap_true
                                                iv_association = /hec1/if_configuration_c=>sc_association-instance_db-db_node
                                      IMPORTING et_data        = lt_db_node                                                   ).

    " Get standby/worker node
    LOOP AT        lt_db_node
    REFERENCE INTO lr_db_node
             WHERE hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-standby OR
                   hec_db_clust_node_type_value = /hec1/if_config_constants=>gc_db_clust_node_type-worker.

      INSERT VALUE #( source_key = lr_db_node->parent_key
                      target_key = lr_db_node->key        ) INTO TABLE et_key_link.

    ENDLOOP.

    " No key link found, error message has to be set...
    IF et_key_link IS INITIAL.



    ENDIF.


  ENDMETHOD.


  METHOD resolve_db_server_tier.

    CLEAR: et_key_link,
           et_failed_key,
           eo_message.


    " **********************************
    " Get DB server perf. category
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)
                                                et_key_link    = DATA(lt_key_link)
                                                et_failed_key  = et_failed_key                                                  ).


    " **********************************
    " Get DB node
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_perform_cat-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key_node)
                                                et_key_link    = DATA(lt_key_link_node)
                                                et_failed_key  = et_failed_key                                                              ).

    " **********************************
    " Get instance DB
    " **********************************


    " **********************************
    " Get DB server instance
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_node
                                                it_key         = lt_key_node
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_node-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key_apsi)
                                                et_key_link    = DATA(lt_key_link_apsi)
                                                et_failed_key  = et_failed_key                                               ).

    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
      RETURN. " >>>>>>>
    ENDIF.

    " **********************************
    " Get tier
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_instance
                                                it_key         = lt_key_apsi
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-app_server_instance-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key_tier)
                                                et_key_link    = DATA(lt_key_link_tier)
                                                et_failed_key  = et_failed_key                                                          ).


    " No key link found, error message has to be set...
    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
    ENDIF.

    LOOP AT lt_key_link ASSIGNING FIELD-SYMBOL(<fs_key_link>).
      TRY.
          INSERT VALUE #( source_key = <fs_key_link>-source_key
                          target_key = lt_key_link_tier[ source_key = lt_key_link_apsi[ source_key = lt_key_link_node[ source_key = <fs_key_link>-target_key ]-target_key ]-target_key ]-target_key )
          INTO TABLE et_key_link.

        CATCH cx_sy_itab_line_not_found.
      ENDTRY.
    ENDLOOP.


  ENDMETHOD.


  METHOD resolve_db_storage_db_qty.

    CLEAR: et_key_link,
           et_failed_key,
           eo_message.

    " **********************************
    " Get DB server performance cat.
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server-to_parent
                                      IMPORTING et_target_key  = DATA(lt_key)
                                                et_failed_key  = et_failed_key                                                   ).

    IF et_failed_key IS NOT INITIAL.
      "ToDo merror message
      RETURN. " >>>>>>>
    ENDIF.

    " **********************************
    " Get app server storage amount
    " **********************************
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-app_server_perform_cat
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-db_server_perform_cat-db_storage_amount
                                      IMPORTING et_key_link    = et_key_link
                                                et_failed_key  = et_failed_key                                                                    ).


  ENDMETHOD.


  METHOD resolve_root_datacenter.

    CLEAR: et_key_link,
           et_failed_key,
           eo_message.


    " ----------------------------------
    " Get delivery unit
    " ----------------------------------
    io_read->retrieve_by_association( EXPORTING iv_node        = is_ctx-node_key
                                                it_key         = it_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-root-delivery_unit
                                      IMPORTING et_target_key  = DATA(lt_key)                                                ).

    " ----------------------------------
    " Get all data center
    " ----------------------------------
    io_read->retrieve_by_association( EXPORTING iv_node        = /hec1/if_configuration_c=>sc_node-delivery_unit
                                                it_key         = lt_key
                                                iv_fill_data   = abap_false
                                                iv_association = /hec1/if_configuration_c=>sc_association-delivery_unit-datacenter
                                      IMPORTING et_key_link    = et_key_link
                                                et_failed_key  = et_failed_key                                                     ).


  ENDMETHOD.
ENDCLASS.