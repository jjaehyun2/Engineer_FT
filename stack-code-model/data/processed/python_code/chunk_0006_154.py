class ZCL_FLIFM_PROGRESS definition
  public
  create public .

public section.

  class-methods SHOW
    importing
      value(IV_PROCESSED) type I optional
      value(IV_TOTAL) type I optional
      !IV_TEXT type STRING .
protected section.
private section.
ENDCLASS.



CLASS ZCL_FLIFM_PROGRESS IMPLEMENTATION.


  method SHOW.


    IF iv_processed IS INITIAL.
      iv_processed = 1.
    ENDIF.

    IF iv_total IS INITIAL.
      iv_total = 100.
    ENDIF.

    cl_progress_indicator=>progress_indicate(
      EXPORTING
         i_text               = iv_text
*              i_msgid              = i_msgid    " Message Class (If I_TEXT is not transferred)
*              i_msgno              = i_msgno    " Message Number (If I_TEXT is not transferred)
*              i_msgv1              = i_msgv1    " Message Variable (Maximum of 50 Characters)
*              i_msgv2              = i_msgv2    " Message Variable (Maximum of 50 Characters)
*              i_msgv3              = i_msgv3    " Message Variable (Maximum of 50 Characters)
*              i_msgv4              = i_msgv4    " Message Variable (Maximum of 50 Characters)
        i_processed          = iv_processed    " Number of Objects Already Processed
        i_total              = iv_total    " Total Number of Objects to Be Processed
        i_output_immediately = abap_true    " X = Display Progress Immediately
*            importing
*              e_progress_sent      = e_progress_sent    " X = Progress Information Was Displayed
    ).


  endmethod.
ENDCLASS.