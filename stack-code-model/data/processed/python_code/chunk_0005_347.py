FUNCTION-POOL zdbbr_user_settings.         "MESSAGE-ID ..

* INCLUDE LZDBBR_USER_SETTINGSD...          " Local class definition

" table declarations
TABLES: sscrfields.

" global data definitions
DATA: gr_user_settings_controller TYPE REF TO zcl_dbbr_user_settings_sc,
      gr_eb_settings_view         TYPE REF TO zcl_dbbr_eb_settings_view.


SELECTION-SCREEN BEGIN OF SCREEN 100 TITLE TEXT-s01 AS WINDOW.
  SELECTION-SCREEN BEGIN OF TABBED BLOCK setting_type FOR 15 LINES.

    " settings for intro screen / general settings
    SELECTION-SCREEN TAB (30) btn_intr USER-COMMAND intro
      DEFAULT SCREEN 101.
    " settings for favorites
    SELECTION-SCREEN TAB (30) btn_fav USER-COMMAND favs
      DEFAULT SCREEN 103.
    " settings for selection screen
    SELECTION-SCREEN TAB (30) btn_sel USER-COMMAND sel
      DEFAULT SCREEN 102.
    " settings for data selection
    SELECTION-SCREEN TAB (30) btn_dsel USER-COMMAND dsel
      DEFAULT SCREEN 105.
    " settings for alv list output
    SELECTION-SCREEN TAB (30) btn_alv USER-COMMAND alv
      DEFAULT SCREEN 104.
    " settings for cds view
    SELECTION-SCREEN TAB (30) btn_cds USER-COMMAND cds
      DEFAULT SCREEN 106.

  SELECTION-SCREEN END OF BLOCK setting_type.

SELECTION-SCREEN END OF SCREEN 100.

*** SETTINGS FOR INTRO SCREEN / GENERAL SETTINGS
******************************************************
SELECTION-SCREEN BEGIN OF SCREEN 101 AS SUBSCREEN.

  " Experimental mode
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_expm TYPE zdbbr_experimental_mode AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t18 FOR FIELD p_expm.
  SELECTION-SCREEN END OF LINE.

  " advanced mode
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_advm TYPE abap_bool AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t03 FOR FIELD p_advm.
  SELECTION-SCREEN END OF LINE.

  " deactivate syntax highlighting and autocompletion in custom query editor
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_xdhlqe TYPE abap_bool AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t29 FOR FIELD p_xdhlqe.
  SELECTION-SCREEN END OF LINE.

  " Theme for code viewer
  SELECTION-SCREEN BEGIN OF LINE.
    SELECTION-SCREEN COMMENT 1(40) TEXT-t30 FOR FIELD p_cvthme.
    SELECTION-SCREEN POSITION 41.
    PARAMETERS p_cvthme TYPE zuitb_code_viewer_theme OBLIGATORY
       AS LISTBOX VISIBLE LENGTH 20 DEFAULT zif_uitb_c_code_viewer_themes=>default.
  SELECTION-SCREEN END OF LINE.

SELECTION-SCREEN END OF SCREEN 101.
******************************************************

**** SETTINGS FOR OBJECT NAVIGATOR
******************************************************
SELECTION-SCREEN BEGIN OF SCREEN 103 AS SUBSCREEN.
  " show object navigator at start
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_onast TYPE abap_bool AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t05 FOR FIELD p_onast.
  SELECTION-SCREEN END OF LINE.

  " Dock object navigator on the right side instead of the left
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_xdonor TYPE abap_bool AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t38 FOR FIELD p_xdonor.
  SELECTION-SCREEN END OF LINE.

  " initial object navigator mode
  SELECTION-SCREEN BEGIN OF LINE.
    SELECTION-SCREEN COMMENT (36) TEXT-t33 FOR FIELD p_iobjm.
    SELECTION-SCREEN POSITION 37.
    PARAMETERS p_iobjm TYPE zdbbr_obj_navigator_mode OBLIGATORY
       AS LISTBOX VISIBLE LENGTH 20 DEFAULT zif_dbbr_c_obj_navigator_mode=>favorites.
  SELECTION-SCREEN END OF LINE.

  SELECTION-SCREEN SKIP.

  SELECTION-SCREEN BEGIN OF BLOCK history WITH FRAME TITLE TEXT-b06 NO INTERVALS.
    " number of recently used entries that should be shown
    SELECTION-SCREEN BEGIN OF LINE.
      SELECTION-SCREEN COMMENT (34) TEXT-t06 FOR FIELD p_flused.
      SELECTION-SCREEN POSITION 35.
      PARAMETERS p_flused TYPE sy-tabix DEFAULT 10.
    SELECTION-SCREEN END OF LINE.
  SELECTION-SCREEN END OF BLOCK history.

  SELECTION-SCREEN BEGIN OF BLOCK favorites WITH FRAME TITLE TEXT-b04 NO INTERVALS.

    " the favorite menu mode
    SELECTION-SCREEN BEGIN OF LINE.
      SELECTION-SCREEN COMMENT (34) TEXT-t35 FOR FIELD p_favmo.
      SELECTION-SCREEN POSITION 35.
      PARAMETERS p_favmo TYPE zdbbr_fav_user_mode OBLIGATORY
         AS LISTBOX VISIBLE LENGTH 20 DEFAULT zif_dbbr_c_global=>c_fav_user_modes-global.
    SELECTION-SCREEN END OF LINE.

  SELECTION-SCREEN END OF BLOCK favorites.

  SELECTION-SCREEN BEGIN OF BLOCK object_browser WITH FRAME TITLE TEXT-b05 NO INTERVALS.
    " initial object browser mode
    SELECTION-SCREEN BEGIN OF LINE.
      SELECTION-SCREEN COMMENT (34) TEXT-t36 FOR FIELD p_iobbrm.
      SELECTION-SCREEN POSITION 35.
      PARAMETERS p_iobbrm TYPE zdbbr_obj_browser_mode OBLIGATORY
         AS LISTBOX VISIBLE LENGTH 20 DEFAULT zif_dbbr_c_object_browser_mode=>package.
    SELECTION-SCREEN END OF LINE.
  SELECTION-SCREEN END OF BLOCK object_browser.

SELECTION-SCREEN END OF SCREEN 103.
******************************************************

*** SETTINGS FOR SELECTION SCREEN
******************************************************
SELECTION-SCREEN BEGIN OF SCREEN 102 AS SUBSCREEN.

  " technical view
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_tview TYPE abap_bool AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t01 FOR FIELD p_tview.
  SELECTION-SCREEN END OF LINE.

  " Compact column view
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_xscccw TYPE abap_bool AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t39 FOR FIELD p_xscccw.
  SELECTION-SCREEN END OF LINE.

  " Activate maintain entries for editable tables
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_xdbedt TYPE zdbbr_maint_db_setting AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t22 FOR FIELD p_xdbedt.
  SELECTION-SCREEN END OF LINE.

  " tech fields first
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_tfirst TYPE abap_bool AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t02 FOR FIELD p_tfirst.
  SELECTION-SCREEN END OF LINE.

  " show db table length in title bar
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_rddbsz TYPE zdbbr_read_db_length AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t19 FOR FIELD p_rddbsz.
  SELECTION-SCREEN END OF LINE.

  " Disable Date to timestamp conversion
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_xdd2tc TYPE zdbbr_dsbl_date_to_times_conv AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t27 FOR FIELD p_xdd2tc.
  SELECTION-SCREEN END OF LINE.

*SELECTION-SCREEN SKIP.

  SELECTION-SCREEN BEGIN OF BLOCK variant_control WITH FRAME TITLE TEXT-b07 NO INTERVALS.
    " Automatic saving of last used filter criteria
    SELECTION-SCREEN BEGIN OF LINE.
      PARAMETERS p_xatscr TYPE zdbbr_auto_selct_crit_saving AS CHECKBOX.
      SELECTION-SCREEN COMMENT 3(50) TEXT-t32 FOR FIELD p_xatscr.
    SELECTION-SCREEN END OF LINE.

    " Always load default variant at start
    SELECTION-SCREEN BEGIN OF LINE.
      PARAMETERS p_xldvas TYPE zdbbr_def_var_filter_first AS CHECKBOX.
      SELECTION-SCREEN COMMENT 3(50) TEXT-t37 FOR FIELD p_xldvas.
    SELECTION-SCREEN END OF LINE.
  SELECTION-SCREEN END OF BLOCK variant_control.

*SELECTION-SCREEN SKIP.

  " max lines
  SELECTION-SCREEN BEGIN OF LINE.
    SELECTION-SCREEN COMMENT 1(37) TEXT-t04 FOR FIELD p_maxl.
    SELECTION-SCREEN POSITION 38.
    PARAMETERS p_maxl TYPE sy-tabix DEFAULT 600.
  SELECTION-SCREEN END OF LINE.

SELECTION-SCREEN END OF SCREEN 102.
******************************************************

*** SETTINGS FOR DATA SELECTION
**********************************************************************
" use reduced memory consumption
SELECTION-SCREEN BEGIN OF SCREEN 105 AS SUBSCREEN.

  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_redmem TYPE zdbbr_use_reduced_memory AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t13 FOR FIELD p_redmem.
  SELECTION-SCREEN END OF LINE.

  " Use ddl view instead of cds view for data selection
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_xddlfs TYPE zdbbr_use_ddl_view_for_select AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t28 FOR FIELD p_xddlfs.
  SELECTION-SCREEN END OF LINE.

  " Search character columns with case ignore
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_xigncs TYPE abap_bool AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t24 FOR FIELD p_xigncs.
  SELECTION-SCREEN END OF LINE.

  SELECTION-SCREEN BEGIN OF BLOCK row_count_settings WITH FRAME TITLE TEXT-b08 NO INTERVALS.
    " Disable automatic max row count determination during select
    SELECTION-SCREEN BEGIN OF LINE.
      PARAMETERS p_xdamrd TYPE abap_bool AS CHECKBOX USER-COMMAND uc_p_xdamrd.
      SELECTION-SCREEN COMMENT 3(50) TEXT-t45 FOR FIELD p_xdamrd.
    SELECTION-SCREEN END OF LINE.

    " Activate Asynchronous Row Count Determination
    SELECTION-SCREEN BEGIN OF LINE.
      PARAMETERS p_xamrde TYPE zdbbr_async_max_rows_det AS CHECKBOX.
      SELECTION-SCREEN COMMENT 3(50) TEXT-t44 FOR FIELD p_xamrde.
    SELECTION-SCREEN END OF LINE.
  SELECTION-SCREEN END OF BLOCK row_count_settings.


SELECTION-SCREEN END OF SCREEN 105.
**********************************************************************

*** SETTINGS FOR ALV LIST OUTPUT
******************************************************
SELECTION-SCREEN BEGIN OF SCREEN 104 AS SUBSCREEN.
  " show technical names in alv
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_tnames TYPE abap_bool AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t07 FOR FIELD p_tnames.
  SELECTION-SCREEN END OF LINE.

  " use no conversion exit
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_nocvex TYPE abap_bool AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t08 FOR FIELD p_nocvex.
  SELECTION-SCREEN END OF LINE.

  " key columns are not fixed
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_kcolnf TYPE abap_bool AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t09 FOR FIELD p_kcolnf.
  SELECTION-SCREEN END OF LINE.

  " no merging of cells during active sorting
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_nosrtm TYPE abap_bool AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t10 FOR FIELD p_nosrtm.
  SELECTION-SCREEN END OF LINE.

  " sign should be shown at start of number
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_notrsg TYPE abap_bool AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t11 FOR FIELD p_notrsg.
  SELECTION-SCREEN END OF LINE.

  " Zero values should be shown as blank cells
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_zerasb TYPE abap_bool AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t12 FOR FIELD p_zerasb.
  SELECTION-SCREEN END OF LINE.

  " Layout will automatically transferred from alv to selection screen
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_autol TYPE abap_bool AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t14 FOR FIELD p_autol.
  SELECTION-SCREEN END OF LINE.

  " Enable default ALV variant
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_defalv TYPE zdbbr_enable_alv_default_var AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t20 FOR FIELD p_defalv.
  SELECTION-SCREEN END OF LINE.

  " Activate ALV Live Filter
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_xflliv TYPE zdbbr_alv_live_filter_flag AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t26 FOR FIELD p_xflliv.
  SELECTION-SCREEN END OF LINE.

  " Automatically hide empty columns in ALV
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_authec TYPE abap_bool AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t40 FOR FIELD p_authec.
  SELECTION-SCREEN END OF LINE.

  SELECTION-SCREEN SKIP.

*... Navigation via associations settings
  SELECTION-SCREEN BEGIN OF BLOCK navigation WITH FRAME TITLE TEXT-b02 NO INTERVALS.
    SELECTION-SCREEN BEGIN OF LINE.
      SELECTION-SCREEN COMMENT (34) TEXT-t31 FOR FIELD p_asnvmo.
      SELECTION-SCREEN POSITION 35.
      PARAMETERS p_asnvmo TYPE zdbbr_assoc_selection_mode OBLIGATORY
        AS LISTBOX VISIBLE LENGTH 25 DEFAULT zif_dbbr_c_assoc_select_mode=>popup.
    SELECTION-SCREEN END OF LINE.

*... Show association browser immediately at start of output
*... if associations exist (i.e. currently only for cds views)
    SELECTION-SCREEN BEGIN OF LINE.
      PARAMETERS p_asslst TYPE abap_bool AS CHECKBOX.
      SELECTION-SCREEN COMMENT 3(50) TEXT-t25 FOR FIELD p_asslst.
    SELECTION-SCREEN END OF LINE.

  SELECTION-SCREEN END OF BLOCK navigation.

  SELECTION-SCREEN BEGIN OF BLOCK colors WITH FRAME TITLE TEXT-b01 NO INTERVALS.
    " coloring of formula fields
    SELECTION-SCREEN BEGIN OF LINE.
      PARAMETERS p_colff TYPE abap_bool AS CHECKBOX.
      SELECTION-SCREEN COMMENT 3(50) TEXT-t15 FOR FIELD p_colff.
    SELECTION-SCREEN END OF LINE.

    " coloring of sort columns
    SELECTION-SCREEN BEGIN OF LINE.
      PARAMETERS p_colso TYPE abap_bool AS CHECKBOX.
      SELECTION-SCREEN COMMENT 3(50) TEXT-t16 FOR FIELD p_colso.
    SELECTION-SCREEN END OF LINE.

    " coloring of add text fields
    SELECTION-SCREEN BEGIN OF LINE.
      PARAMETERS p_colat TYPE abap_bool AS CHECKBOX.
      SELECTION-SCREEN COMMENT 3(50) TEXT-t17 FOR FIELD p_colat.
    SELECTION-SCREEN END OF LINE.

    " coloring of calculated fields of CDS Views
    SELECTION-SCREEN BEGIN OF LINE.
      PARAMETERS p_colcf TYPE abap_bool AS CHECKBOX.
      SELECTION-SCREEN COMMENT 3(50) TEXT-t43 FOR FIELD p_colcf.
    SELECTION-SCREEN END OF LINE.

  SELECTION-SCREEN END OF BLOCK colors.
SELECTION-SCREEN END OF SCREEN 104.
******************************************************

*** SETTINGS FOR CDS VIEW
**********************************************************************
" use reduced memory consumption
SELECTION-SCREEN BEGIN OF SCREEN 106 AS SUBSCREEN.

  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_calcve TYPE abap_bool AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t41 FOR FIELD p_calcve.
  SELECTION-SCREEN END OF LINE.

  " Use ddl view instead of cds view for data selection
  SELECTION-SCREEN BEGIN OF LINE.
    PARAMETERS p_igevec TYPE abap_bool AS CHECKBOX.
    SELECTION-SCREEN COMMENT 3(50) TEXT-t42 FOR FIELD p_igevec.
  SELECTION-SCREEN END OF LINE.

SELECTION-SCREEN END OF SCREEN 106.
**********************************************************************

*... Screen for user settings of entity browser
******************************************************
SELECTION-SCREEN BEGIN OF SCREEN 200 TITLE TEXT-s02 AS WINDOW.

  SELECTION-SCREEN BEGIN OF BLOCK search_settings WITH FRAME TITLE TEXT-b03.
    PARAMETERS p_ebensf TYPE zdbbr_obj_browser_mode AS LISTBOX VISIBLE LENGTH 35 OBLIGATORY DEFAULT zif_dbbr_c_object_browser_mode=>cds_view.
    PARAMETERS p_eblimo TYPE zdbbr_entity_browser_link_mode AS LISTBOX VISIBLE LENGTH 35 OBLIGATORY DEFAULT zif_sat_c_entity_type=>table.
    PARAMETERS p_ebbmax TYPE int2 DEFAULT 500.
  SELECTION-SCREEN END OF BLOCK search_settings.

SELECTION-SCREEN END OF SCREEN 200.
******************************************************