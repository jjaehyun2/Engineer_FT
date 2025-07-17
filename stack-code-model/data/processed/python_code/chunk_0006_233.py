class YCL_AIM_PRJ_D_PREFIX definition
  public
  inheriting from /BOBF/CL_LIB_D_SUPERCLASS
  final
  create public .

public section.

  methods /BOBF/IF_FRW_DETERMINATION~EXECUTE
    redefinition .
protected section.
private section.
ENDCLASS.



CLASS YCL_AIM_PRJ_D_PREFIX IMPLEMENTATION.


METHOD /bobf/if_frw_determination~execute.

  DATA lt_project TYPE yaim_prj_t_root.

  io_read->retrieve(
    EXPORTING
      iv_node                 = is_ctx-node_key    " Node Name
      it_key                  = it_key    " Key Table
      iv_fill_data            = abap_true    " Data element for domain BOOLE: TRUE (='X') and FALSE (=' ')
      it_requested_attributes = VALUE #( ( yif_aim_prj_yaim_project_c=>sc_node_attribute-root-abbreviation ) )
    IMPORTING
      et_data                 = lt_project    " Data Return Structure
  ).

  LOOP AT lt_project REFERENCE INTO DATA(lr_project).
    lr_project->abbreviation = |{ condense( lr_project->abbreviation  ) CASE = (cl_abap_format=>c_upper) }|.

    io_modify->update(
      EXPORTING
        iv_node           = is_ctx-node_key    " Node
        iv_key            = lr_project->key    " Key
        is_data           = lr_project
        it_changed_fields = VALUE #( ( yif_aim_prj_yaim_project_c=>sc_node_attribute-root-abbreviation ) )
    ).
  ENDLOOP.

ENDMETHOD.
ENDCLASS.