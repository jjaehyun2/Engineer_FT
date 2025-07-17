*&---------------------------------------------------------------------*
*&  Include           ZKR_OTRT01
*&---------------------------------------------------------------------*
INCLUDE : bdcrecxy.          "BDC subroutines

TYPE-POOLS: icon.

*----------------------------------------------------------------------*
* TABLES
*----------------------------------------------------------------------*
TABLES: sotr_head, sotr_text, sotr_use.

*----------------------------------------------------------------------*
* CONSTANTS
*----------------------------------------------------------------------*
CONSTANTS : co_hypen TYPE char1 VALUE '/',
            co_wdyv  TYPE char4 VALUE 'WDYV'.


*----------------------------------------------------------------------*
* DATA: Variable
*----------------------------------------------------------------------*
DATA: gv_trkorr TYPE trkorr.
DATA: gs_opt LIKE ctu_params.
DATA: gv_paket TYPE devclass.
DATA: gv_non_org_system.

*// 조회/변경
DATA: BEGIN OF gt_outtab1 OCCURS 0,
        box        TYPE flag,
        alias_name TYPE sotr_head-alias_name,
        langu      TYPE sotr_text-langu,
        text       TYPE sotr_text-text,
        used_count TYPE i,
        chan_name  TYPE sotr_head-chan_name,
        chan_date  TYPE datum,
        chan_time  TYPE uzeit,
        concept    TYPE sotr_head-concept,
        paket      TYPE sotr_head-paket,
        trkorr     TYPE e071-trkorr,
        objid_vec  TYPE sotr_head-objid_vec,
        flag_cntxt TYPE sotr_text-flag_cntxt,
        country    TYPE sotr_text-country,
        extension  TYPE sotr_text-extension,
        status     TYPE sotr_text-status,
        length     TYPE sotr_text-length,
        object     TYPE sotr_text-object,
        last_rel   TYPE sotr_text-last_rel,
        last_irel  TYPE sotr_text-last_irel,
        add_cntxt  TYPE sotr_text-add_cntxt,
        crea_name  TYPE sotr_text-crea_name,
        crea_date  TYPE datum,
        crea_time  TYPE uzeit,
        flag_corr  TYPE sotr_text-flag_corr,
        icon       TYPE icon_d,
        message    TYPE text200,
        celltab    TYPE lvc_t_styl,
      END OF gt_outtab1.
DATA: gt_first1 LIKE TABLE OF gt_outtab1.
DATA: gt_save1 LIKE TABLE OF gt_outtab1.

DATA: g_dock_cont1 TYPE REF TO cl_gui_docking_container,
      g_grid1      TYPE REF TO cl_gui_alv_grid.
DATA: gs_layout1 TYPE lvc_s_layo,       "Layout
      gt_fdcat1  TYPE lvc_t_fcat,       "Field Catalog
      g_pos1     TYPE i,
      gt_fcode1  TYPE ui_functions,     "기본툴바 제어
      gt_sort1   TYPE lvc_t_sort.       "정렬

*// 생성

DATA: BEGIN OF gt_outtab2 OCCURS 0,
        paket      TYPE sotr_head-paket,
        alias_name TYPE sotr_head-alias_name,
        objtype    TYPE sotr_tree-object,
        en_text    TYPE sotr_text-text,
        ko_text    TYPE sotr_text-text,
        zh_text    TYPE sotr_text-text,
        zf_text    TYPE sotr_text-text,
        icon       TYPE icon_d,
        message    TYPE text200,
        celltab    TYPE lvc_t_styl,
      END OF gt_outtab2.
DATA: g_dock_cont2 TYPE REF TO cl_gui_docking_container,
      g_grid2      TYPE REF TO cl_gui_alv_grid.
DATA: gs_layout2 TYPE lvc_s_layo,       "Layout
      gt_fdcat2  TYPE lvc_t_fcat,       "Field Catalog
      g_pos2     TYPE i,
      gt_fcode2  TYPE ui_functions.     "기본툴바 제어

*// Screen Data
DATA: ok_code LIKE sy-ucomm,
      save_ok TYPE sy-ucomm.


* Excel Form Download # *---------------------------------------------
DATA : gt_intern      LIKE kcde_cells OCCURS 0 WITH HEADER LINE.
DATA : gv_stripped   TYPE string,
       gv_file_path  TYPE string,
       gv_extension  TYPE string,
       gv_split_name TYPE string,
       gv_filename   TYPE rlgrap-filename,
       gv_flag       TYPE c.

DATA : gv_file_length TYPE i.
DATA : go_excel  TYPE ole2_object, " Excel object
       go_mapl   TYPE ole2_object,        " list of workbooks
       go_map    TYPE ole2_object,        " workbook
       go_sheets TYPE ole2_object,        " workbook's sheets
       go_sheet  TYPE ole2_object,        " workbook's sheet
       go_zl     TYPE ole2_object,        " cell
       go_zl2    TYPE ole2_object,        " cell
       go_f      TYPE ole2_object,        " font
       go_zrl    TYPE ole2_object.        " RANGE

" 엑셀 업로드 테이블
DATA : BEGIN OF gs_excel_up ,
         alias_name TYPE sotr_alias,
         en_text    TYPE sotr_txt,
         ko_text    TYPE sotr_txt,
         zh_text    TYPE sotr_txt,
         zf_text    TYPE sotr_txt,
       END OF gs_excel_up,
       gt_excel_up LIKE TABLE OF gs_excel_up.


**********************************************************************
* LOCAL CLASSES: Definition
**********************************************************************
CLASS lcl_event_handler DEFINITION.
  PUBLIC SECTION.
    METHODS :
      hotspot_click          FOR EVENT hotspot_click OF cl_gui_alv_grid
        IMPORTING e_row_id e_column_id .
ENDCLASS.                    "LCL_EVENT_HANDLER DEFINITION
*********************************************************************
* LOCAL CLASSES: Implementation
*********************************************************************
CLASS lcl_event_handler IMPLEMENTATION.
  METHOD hotspot_click.
    PERFORM event_hotspot_click USING e_row_id
                                      e_column_id.
  ENDMETHOD.                    "top_of_page

ENDCLASS.                    "LCL_EVENT_HANDLER IMPLEMENTATION

DATA: g_events       TYPE REF TO lcl_event_handler.

*----------------------------------------------------------------------*
*SELECT-OPTIONS & PARAMETERS
*----------------------------------------------------------------------*
*// 검색탭
SELECTION-SCREEN BEGIN OF SCREEN 100 AS SUBSCREEN.
  "Package 검색
  PARAMETERS: p_pkg TYPE devclass AS LISTBOX VISIBLE LENGTH 50 MEMORY ID dvc.
*----------------------------------
  " 언어키
  SELECTION-SCREEN BEGIN OF LINE.
    SELECTION-SCREEN COMMENT 1(33) TEXT-009.
    PARAMETERS: p_en AS CHECKBOX DEFAULT 'X'.
    SELECTION-SCREEN COMMENT 37(7) TEXT-007 FOR FIELD p_en.
    PARAMETERS: p_ko AS CHECKBOX DEFAULT 'X'.
    SELECTION-SCREEN COMMENT 47(7) TEXT-006 FOR FIELD p_ko.
    PARAMETERS: p_zh AS CHECKBOX DEFAULT 'X'.
    SELECTION-SCREEN COMMENT 57(7) TEXT-008 FOR FIELD p_zh.
    PARAMETERS: p_zf AS CHECKBOX DEFAULT 'X'.
    SELECTION-SCREEN COMMENT 67(13) TEXT-004 FOR FIELD p_zf.
  SELECTION-SCREEN END OF LINE.
  SELECTION-SCREEN ULINE 1(79).
*----------------------------------
  "
  SELECT-OPTIONS: s_text FOR sotr_text-text  NO INTERVALS.
  SELECT-OPTIONS: s_alias FOR sotr_head-alias_name NO INTERVALS.
  SELECT-OPTIONS: s_concpt FOR sotr_head-concept NO INTERVALS.
  SELECT-OPTIONS: s_pgid FOR sotr_use-obj_name NO INTERVALS.

SELECTION-SCREEN END OF SCREEN 100.

*--------------------------------------------------------------------*
*// 생성탭
SELECTION-SCREEN BEGIN OF SCREEN 200 AS SUBSCREEN.

  PARAMETERS: p_pkgc TYPE devclass AS LISTBOX VISIBLE LENGTH 50 MEMORY ID dvc.

SELECTION-SCREEN END OF SCREEN 200.


SELECTION-SCREEN: BEGIN OF TABBED BLOCK mytab FOR 20 LINES,
TAB (20) button1 USER-COMMAND push1,
TAB (20) button2 USER-COMMAND push2,
END OF BLOCK mytab.