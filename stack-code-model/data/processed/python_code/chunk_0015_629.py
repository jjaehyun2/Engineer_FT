*&---------------------------------------------------------------------*
*&  Z_ALV_MVC_TEMPLATE
*&
*&---------------------------------------------------------------------*
*&
*&
*&---------------------------------------------------------------------*

INCLUDE z_alv_mvc_template_top. "types + class definition
INCLUDE z_alv_mvc_template_s00. "selection screen

INCLUDE z_alv_mvc_template_f00. "mvc model
INCLUDE z_alv_mvc_template_f01. "mvc view
INCLUDE z_alv_mvc_template_f02. "mvc controller

START-OF-SELECTION.
  SET SCREEN 100.

  DATA go_controller TYPE REF TO lcl_mvc_controller.
  CREATE OBJECT go_controller.
  go_controller->run( ).

INCLUDE z_alv_mvc_template_m00. " pai100 pbo100