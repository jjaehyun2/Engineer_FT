class ZCL_MDG_GENERAL_HELPER definition
  public
  final
  create public .

public section.

  class-methods BACKGROUND_DEBUG
    importing
      !IM_CR_NUMBER type USMD_CREQUEST optional .
protected section.
private section.
ENDCLASS.



CLASS ZCL_MDG_GENERAL_HELPER IMPLEMENTATION.


METHOD background_debug.

    IF im_cr_number IS NOT INITIAL.
      DATA(lv_cr_number) = im_cr_number.
    ELSE.
*     Get CR Number from App Context.
      lv_cr_number = cl_usmd_app_context=>get_context( )->mv_crequest_id.
    ENDIF.

    SELECT SINGLE @abap_true
      FROM usmd120c
     WHERE usmd_crequest = @lv_cr_number
      INTO @DATA(lv_cr_exists).
*   If the CR is found, check user parameter of the id who created this CR.
    IF sy-subrc = 0 AND lv_cr_exists = abap_true.
      DO.
        SELECT SINGLE "#EC *
               a~usmd_created_by,
               b~bname,
               b~parid,
               b~parva
          FROM usmd120c AS a
          JOIN usr05    AS b
            ON b~bname = a~usmd_created_by
         WHERE a~usmd_crequest = @lv_cr_number
           AND b~parid = 'ZBGRND_DEBUG'
          INTO @DATA(lst_cr_usr_param).
        IF lst_cr_usr_param-parva = space.
          EXIT.
        ENDIF.
      ENDDO.

*   If the CR is not yet submitted, then get CR details from CONV API.
*   This case occurs when Rule Service BAdI is called from DIF
    ELSE.

*     Get Model from App Context.
      DATA(lv_model) = cl_usmd_app_context=>get_context( )->mv_usmd_model.

*     Check if instance of governance API exists.
      DATA(lv_flg_gov_api) = cl_usmd_gov_api=>check_instance_exists(
                               iv_model_name = lv_model ).

*     Check if instance of convenience API exists.
      DATA(lv_flg_conv_api) =
        cl_usmd_conv_som_gov_api=>check_instance_exists(
          iv_model_name = lv_model ).

      TRY.
*         If governance API exists and convenience API does not, then use GOV API.
          IF lv_flg_gov_api = abap_true AND lv_flg_conv_api = abap_false.
            DATA(lo_gov_api) = cl_usmd_gov_api=>get_instance(
                                 iv_model_name = lv_model ).
            IF lo_gov_api IS BOUND.
*             Get the id who created Change Request.
              DATA(lv_created_by) =
                lo_gov_api->get_crequest_attributes(
                  iv_crequest_id = lv_cr_number )-usmd_created_by.
            ENDIF.

*         Else use convenience API
          ELSE.

*           Get the instance of Convenience API
            DATA(lo_conv_api) = cl_usmd_conv_som_gov_api=>get_instance(
                                  iv_model_name = lv_model ).

            IF lo_conv_api IS BOUND.
*             Set the change number in Convenience API
              lo_conv_api->set_environment(
                iv_crequest_id = lv_cr_number
              ).

*             Get the id who created Change Request.
              lv_created_by =
                lo_conv_api->get_crequest_attributes( )-usmd_created_by.
            ENDIF.
          ENDIF.

        CATCH cx_usmd_conv_som_gov_api .
        CATCH cx_usmd_app_context_cons_error .
        CATCH cx_usmd_conv_som_gov_api_env.
        CATCH cx_usmd_gov_api .

*         If any error, then use SY-UNAME for endless loop.
          lv_created_by = sy-uname.
      ENDTRY.

*     Run endless loop.
      DO.
        SELECT SINGLE "#EC CI_SUBRC
               bname,
               parid,
               parva
          FROM usr05
         WHERE bname = @lv_created_by
           AND parid = 'ZBGRND_DEBUG'
          INTO @DATA(lst_usr_param).
        IF lst_usr_param-parva = space.
          EXIT.
        ENDIF.
      ENDDO.
    ENDIF.

  ENDMETHOD.
ENDCLASS.