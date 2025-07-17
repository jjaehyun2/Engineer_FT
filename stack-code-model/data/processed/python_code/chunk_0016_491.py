class ZCL_FLIFM_SERVICES_FILAB definition
  public
  create public .

public section.

  constants MC_FILAB_HOMEPAGE type STRING value 'http://www.fi-lab.com' ##NO_TEXT.
  constants MC_FILAB_HELP type STRING value 'https://tawk.to/chat/59ed41a7c28eca75e46277ea/default' ##NO_TEXT.

  class-methods OPEN_FILAB_HOMEPAGE
    raising
      ZCX_FLIFM_EXCEPTION .
  class-methods OPEN_FILAB_HELP
    raising
      ZCX_FLIFM_EXCEPTION .
protected section.
private section.
ENDCLASS.



CLASS ZCL_FLIFM_SERVICES_FILAB IMPLEMENTATION.


  method OPEN_FILAB_HELP.


    cl_gui_frontend_services=>execute(
      EXPORTING document = mc_filab_help
      EXCEPTIONS OTHERS = 1 ).

    IF sy-subrc <> 0.
      zcx_flifm_exception=>raise_msg( 'Opening "FI LAB help page" failed.' ).
    ENDIF.


  endmethod.


  method OPEN_FILAB_HOMEPAGE.


    cl_gui_frontend_services=>execute(
      EXPORTING document = mc_filab_homepage
      EXCEPTIONS OTHERS = 1 ).

    IF sy-subrc <> 0.
      zcx_flifm_exception=>raise_msg( 'Opening "http://www.fi-lab.com" failed.' ).
    ENDIF.


  endmethod.
ENDCLASS.