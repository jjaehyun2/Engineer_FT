FUNCTION-POOL za2xh_email.                  "MESSAGE-ID ..

DATA: go_cont   TYPE REF TO cl_gui_custom_container,
      go_edit   TYPE REF TO cl_gui_textedit,
      go_assist TYPE REF TO zcl_za2xh_email_popup,
      gv_email  TYPE string.

* INCLUDE LZA2XH_EMAILD...                   " Local class definition