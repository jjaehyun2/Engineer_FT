class ZCL_AOF_AOC_CHECK_30 definition
  public
  create public .

public section.

  interfaces ZIF_AOF_FIXER .
  PROTECTED SECTION.
  PRIVATE SECTION.
ENDCLASS.



CLASS ZCL_AOF_AOC_CHECK_30 IMPLEMENTATION.


  METHOD zif_aof_fixer~is_fixable.

    rv_fixable = boolc( is_result-test = 'ZCL_AOC_CHECK_30' ).

  ENDMETHOD.


  METHOD zif_aof_fixer~run.

    DATA: lv_code TYPE string.

    FIELD-SYMBOLS: <ls_result> LIKE LINE OF rs_data-results,
                   <lv_code>   TYPE string,
                   <ls_change> LIKE LINE OF rs_data-changes.


    rs_data = is_data.

    SORT rs_data-results BY
      sobjtype ASCENDING
      sobjname ASCENDING
      line DESCENDING.

    LOOP AT rs_data-results ASSIGNING <ls_result>.
      READ TABLE rs_data-changes ASSIGNING <ls_change>
        WITH KEY sobjtype = <ls_result>-sobjtype
                 sobjname = <ls_result>-sobjname.
      ASSERT sy-subrc = 0.

      READ TABLE <ls_change>-code_after INDEX <ls_result>-line ASSIGNING <lv_code>.
      ASSERT sy-subrc = 0.

      lv_code = <lv_code>.
      CONDENSE lv_code.
      IF lv_code = 'EXPORTING' OR lv_code = 'exporting'.
        DELETE <ls_change>-code_after INDEX <ls_result>-line.
      ELSE.
        REPLACE FIRST OCCURRENCE OF `EXPORTING ` IN <lv_code> WITH ''.
        IF sy-subrc <> 0.
          REPLACE FIRST OCCURRENCE OF `exporting ` IN <lv_code> WITH ''.
        ENDIF.
      ENDIF.
    ENDLOOP.

  ENDMETHOD.
ENDCLASS.