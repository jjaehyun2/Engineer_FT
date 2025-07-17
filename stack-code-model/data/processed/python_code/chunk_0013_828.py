FUNCTION-POOL zgrp_alv_popup.               "MESSAGE-ID ..

* INCLUDE ZLZGRP_ALV_POPUP01.                " Local class definition

*---------------------------------------------------------------------*
*       CLASS lcl_event_handler DEFINITION
*---------------------------------------------------------------------*
CLASS handle_events DEFINITION.

  PUBLIC SECTION.

    METHODS:
      on_link_click FOR EVENT link_click
                    OF cl_salv_events_table
        IMPORTING row column,

      on_user_command FOR EVENT added_function
                    OF cl_salv_events
        IMPORTING e_salv_function.

ENDCLASS.                    "lcl_event_handler DEFINITION

DATA v_teste TYPE string.

DATA: go_salv_table TYPE REF TO cl_salv_table,
      event_handler TYPE REF TO handle_events,
      gt_hotspot    TYPE ZTHOTSPOT,
      gt_selected_rows TYPE SALV_T_ROW.

FIELD-SYMBOLS: <gt_table_data> TYPE STANDARD TABLE,
               <table_data>    TYPE any,
               <row_data>      TYPE any.