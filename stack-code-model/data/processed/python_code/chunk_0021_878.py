*&---------------------------------------------------------------------*
*& Report  Z_MONSTER_ATROCITY_DUE_LIST
*&
*&---------------------------------------------------------------------*
* This will show a list of requested atrocities to be committed by
* monsters from a particular mad scientist castle on a given day
* The user will, when the atrocity becomes due, allocate a monster
* This information will be "pushed" by means of the AMC framework
* to any running instances of the Monster Atrocity Monitor which
* have subscribed to this information
* The target Monitor report will then update itself without the user
* who is running it having to do anything (e.g. press 'refresh').
*--------------------------------------------------------------------*
* First, need to set PID of SAPGUI_PUSH_CHANNEL = X”.
* Then need to define the ABAP Messaging Channel
* In SAMC and application ID and a channel have to be defined
* I am hoping to use the PCP message type
* Then you "whitelist" programs which can send and receive information
*--------------------------------------------------------------------*
* I will make this a SALV report which will have a user command
* which lets the user choose a monster and then create the delivery and
* fire off an AMC messsage to all subscribers saying the new delivery
* has been created
*--------------------------------------------------------------------*
* Data Declarations
*--------------------------------------------------------------------*
INCLUDE z_monster_adl_top.

TABLES: ztmonster_adl.
**********************************************************************
* Selection Screen
**********************************************************************
* Monster Header Data
SELECTION-SCREEN BEGIN OF BLOCK blk1 WITH FRAME TITLE text-001.

SELECT-OPTIONS: s_date FOR ztmonster_adl-due_date,
                s_cstl FOR ztmonster_adl-castle_number.

SELECTION-SCREEN END OF BLOCK blk1.

* Display Options
SELECTION-SCREEN BEGIN OF BLOCK blk2 WITH FRAME TITLE text-002.

PARAMETERS: p_vari  LIKE disvariant-variant.

SELECTION-SCREEN END OF BLOCK blk2.


**********************************************************************
* Initialisation
**********************************************************************
INITIALIZATION.
  PERFORM initalisation.

*--------------------------------------------------------------------*
* Start-of-Selection
*--------------------------------------------------------------------*
START-OF-SELECTION.
  "This nonsense is the only way I can avoid getting bogus syntax
  "errors when doing a syntax check on the local class implementations
  CREATE OBJECT go_selections
    EXPORTING
      is_date = s_date[]
      is_cstl = s_cstl[]
      ip_vari = p_vari.

  IF zcl_bc_system_environment=>is_production( ) = abap_true.
    "In production we never want a short dump, but the "design by contract"
    "things would just confuse the user
    TRY.
        lcl_application=>main( ).
      CATCH cx_sy_no_handler INTO go_no_handler.
        "An exception was raised that was not caught at any point in the call stack
        gd_error_class = |Fatal Error concerning Class { go_no_handler->classname } - Please Call the Helpdesk|.
        MESSAGE gd_error_class TYPE 'I'.
      CATCH cx_root ##catch_all.
        "We do not know what was happened, output a message instead of dumping
        MESSAGE 'Report in Trouble - please call helpdesk' TYPE 'I'.
    ENDTRY.
  ELSE.
    "Development / Test / Quality Assurance
    "Here we DO want short dumps so we can analyse them, and we want the design by
    "contract messages to make it obvious there is a bug and the code should not
    "go to production
    "Put another the way the two DBC exceptions are impossible errors I am actively
    "looking to cause a dump. If any other sort of dump occurs then it is something
    "I am not expecting and I want to know all about it
    TRY.
        lcl_application=>main( ).
      CATCH zcx_violated_precondition INTO go_precondition.
        "A bug was detected at the start of a subroutine - the caller of the
        "subroutine is at fault
        go_precondition->mo_error_log->show_error_log( ).
      CATCH zcx_violated_postcondition INTO go_postcondition.
        "A bug was detected at the end of a subroutine - the subroutine is
        "at fault
        go_postcondition->mo_error_log->show_error_log( ).
    ENDTRY.
  ENDIF.

*----------------------------------------------------------------------*
* AT SELECTION-SCREEN ON VALUE-REQUEST                                 *
*----------------------------------------------------------------------*
AT SELECTION-SCREEN ON VALUE-REQUEST FOR p_vari.
  PERFORM f4_layouts USING cl_salv_layout=>restrict_none CHANGING p_vari.

*&---------------------------------------------------------------------*
*&      Form  F4_LAYOUTS
*&---------------------------------------------------------------------*
FORM f4_layouts USING    pud_restrict TYPE salv_de_layout_restriction
                CHANGING pcd_layout   TYPE disvariant-variant.

  DATA: ls_layout TYPE salv_s_layout_info,
        ls_key    TYPE salv_s_layout_key.

  ls_key-report = sy-repid.

  ls_layout = cl_salv_layout_service=>f4_layouts( s_key    = ls_key
                                                  layout   = pcd_layout
                                                  restrict = pud_restrict ).

  pcd_layout = ls_layout-layout.

ENDFORM.                    " F4_LAYOUTS

**********************************************************************
* Class Implementations
**********************************************************************
INCLUDE z_monster_adl_io1.

*&---------------------------------------------------------------------*
*&      Form  INITALISATION
*&---------------------------------------------------------------------*
FORM initalisation .

ENDFORM.                    " INITALISATION