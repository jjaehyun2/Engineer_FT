class YCL_AIM_PRJ_D_MEMBER_USERDATA definition
  public
  inheriting from YCL_AIM_PRJ_D_DERIVE_USERDATA
  create public .

public section.

  methods CONSTRUCTOR .
protected section.
private section.
ENDCLASS.



CLASS YCL_AIM_PRJ_D_MEMBER_USERDATA IMPLEMENTATION.


method CONSTRUCTOR.
    super->constructor( ).
    mv_uname_attribute = YIF_AIM_PRJ_YAIM_PROJECT_C=>sc_node_attribute-member-username.
  endmethod.
ENDCLASS.