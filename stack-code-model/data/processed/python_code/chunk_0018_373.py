*"* use this source file for your ABAP unit test classes
CLASS ltd_trs_fac_fm DEFINITION FOR TESTING.

  PUBLIC SECTION.
    INTERFACES: zif_trs_fm_access.

ENDCLASS.

CLASS ltd_trs_fac_fm IMPLEMENTATION.

  METHOD zif_trs_fm_access~get_request.
    e_order = 'H01K100100'.
    e_task  = 'H01K100101'.
  ENDMETHOD.

  METHOD zif_trs_fm_access~insert_key.
  ENDMETHOD.

  METHOD zif_trs_fm_access~check_transport.
  ENDMETHOD.

ENDCLASS.

CLASS ltc_trs_customizing DEFINITION
                            FOR TESTING
                            RISK LEVEL HARMLESS
                            DURATION SHORT.

  PRIVATE SECTION.

    DATA: cut TYPE REF TO zif_trs_transport_request,
          key TYPE string.

    CLASS-METHODS:
      class_setup,
      class_teardown.

    METHODS:
      setup,
      teardown.

    " testing methods
    METHODS:
      " the whole e071k structure is initial
      add_e071k_initial FOR TESTING RAISING cx_static_check,

      "! for customizing requests the field e071k-mastertype / object should always be 'TABU' <br/>
      "! here it will be checked what happens if the wrong type will be passed
      add_wrong_type_to_request_obj FOR TESTING RAISING cx_static_check,

      "! for customizing requests the field e071k-mastertype / object should always be 'TABU' <br/>
      "! here it will be checked what happens if the wrong type will be passed
      add_wrong_type_to_request_mas FOR TESTING RAISING cx_static_check,

      "! here is no mastertype or object given --> exception needs to get raised
      add_type_is_initial FOR TESTING RAISING cx_static_check,

      "! the e071k-tabkey key is initial
      add_key_initial FOR TESTING RAISING cx_static_check,

      "! add correct entry with e071k-mastername entered
      add_tabu_m_to_request FOR TESTING RAISING cx_static_check,

      "! add correct entry with e071k-mastername entered
      add_tabu_o_to_request FOR TESTING RAISING cx_static_check,

      "! the field tabkey from structure e071k is not filled --> exception
      add_tabkey_is_initial FOR TESTING RAISING cx_static_check,

      "! the key which is entered into the method is empty --> nothing can get deleted
      delete_empty_key FOR TESTING RAISING cx_static_check,

      "! the given key does not exist in the given transport request
      delete_not_existant_key FOR TESTING RAISING cx_static_check.

ENDCLASS.

CLASS ltc_trs_customizing IMPLEMENTATION.

  METHOD class_setup.
    zcl_trs_inject_facade=>inject_fm_access( NEW ltd_trs_fac_fm( ) ).
  ENDMETHOD.

  METHOD class_teardown.

  ENDMETHOD.

  METHOD setup.
    cut = zcl_trs_tr_factory=>get_customizing_request( ).
    key = '200DE'.
  ENDMETHOD.

  METHOD teardown.

  ENDMETHOD.

  METHOD add_e071k_initial.

    DATA e071k TYPE e071k.

    TRY.
        cut->add_key_to_request( e071k ).
        cl_abap_unit_assert=>fail( ).
      CATCH zcx_trs_no_key.
        cl_abap_unit_assert=>assert_true( 'X' ).
    ENDTRY.

  ENDMETHOD.

  METHOD add_key_initial.

    DATA e071k TYPE e071k.

    e071k-tabkey = key.
    e071k-trkorr = e071k-viewname = e071k-objfunc = space.
    e071k-pgmid = 'R3TR'.
    e071k-object = e071k-mastertype = 'TABU'.
    e071k-as4pos = 0.
    CLEAR: e071k-objname, e071k-mastername. " only to be sure, that the key will not be given to the method

    TRY.
        cut->add_key_to_request( e071k ).
        cl_abap_unit_assert=>fail( ).
      CATCH zcx_trs_no_key.
        cl_abap_unit_assert=>assert_true( abap_true ).
    ENDTRY.

  ENDMETHOD.

  METHOD add_wrong_type_to_request_obj.

    DATA e071k TYPE e071k.

    e071k-object = 'CLAS'.
    e071k-mastername = 'T005'.
    e071k-tabkey = key.
    TRY.
        cut->add_key_to_request( e071k ).
        cl_abap_unit_assert=>fail( ).
        RETURN.
      CATCH zcx_trs_wrong_object_type.
        " assert true method will be called at the end, if everything went fine
    ENDTRY.

    CLEAR e071k-object.

    e071k-object = 'REPS'.

    TRY.
        cut->add_key_to_request( e071k ).
        cl_abap_unit_assert=>fail( ).
        RETURN.
      CATCH zcx_trs_wrong_object_type.
        " assert true method will be called at the end, if everything went fine
    ENDTRY.

    cl_abap_unit_assert=>assert_true( abap_true ).

  ENDMETHOD.

  METHOD add_tabu_m_to_request.

    DATA e071k TYPE e071k.

    e071k-object = 'TABU'.
    e071k-mastername = 'T005'.
    e071k-tabkey = key.

    TRY.
        cut->add_key_to_request( e071k ).
        cl_abap_unit_assert=>assert_true( abap_true ).
      CATCH cx_static_check.
        cl_abap_unit_assert=>fail( ).
    ENDTRY.

  ENDMETHOD.

  METHOD add_tabu_o_to_request.

    DATA e071k TYPE e071k.

    e071k-object = 'TABU'.
    e071k-objname = 'T005'.
    e071k-tabkey = key.

    TRY.
        cut->add_key_to_request( e071k ).
        cl_abap_unit_assert=>assert_true( abap_true ).
      CATCH cx_static_check.
        cl_abap_unit_assert=>fail( ).
    ENDTRY.

  ENDMETHOD.

  METHOD add_wrong_type_to_request_mas.

    DATA e071k TYPE e071k.

    e071k-mastertype = 'CLAS'.
    e071k-mastername = 'T005'.
    e071k-tabkey = key.

    TRY.
        cut->add_key_to_request( e071k ).
        cl_abap_unit_assert=>fail( ).
        RETURN.
      CATCH zcx_trs_wrong_object_type.
        " assert true method will be called at the end, if everything went fine
    ENDTRY.

    CLEAR e071k-mastertype.

    " try with another mastertype

    e071k-mastertype = 'REPS'.

    TRY.
        cut->add_key_to_request( e071k ).
        cl_abap_unit_assert=>fail( ).
        RETURN.
      CATCH zcx_trs_wrong_object_type.
        " assert true method will be called at the end, if everything went fine
    ENDTRY.

    cl_abap_unit_assert=>assert_true( abap_true ).
  ENDMETHOD.

  METHOD add_type_is_initial.

    DATA e071k TYPE e071k.

    e071k-objname = 'T005'.
    e071k-tabkey = key.

    TRY.
        cut->add_key_to_request( e071k  ).
        cl_abap_unit_assert=>fail( ).
      CATCH zcx_trs_no_object_type.    "
        " assert true method will be called at the end, if everything went fine
    ENDTRY.

    cl_abap_unit_assert=>assert_true( abap_true ).
  ENDMETHOD.

  METHOD add_tabkey_is_initial.

    DATA e071k TYPE e071k.

    e071k-object = 'TABU'.
    e071k-objname = 'T005'.

    TRY.

        cut->add_key_to_request( e071k ).
        cl_abap_unit_assert=>fail( ).
      CATCH zcx_trs_no_key.
        " assert true method will be called at the end, if everything went fine
    ENDTRY.

    cl_abap_unit_assert=>assert_true( abap_true ).

  ENDMETHOD.

  METHOD delete_empty_key.

  ENDMETHOD.

  METHOD delete_not_existant_key.

  ENDMETHOD.

ENDCLASS.

CLASS ltc_how_to_use DEFINITION FOR TESTING
                            DURATION SHORT
                            RISK LEVEL HARMLESS.

  PRIVATE SECTION.

    CLASS-METHODS: class_setup.

    DATA: cut TYPE REF TO zif_trs_transport_request.

    METHODS add_key_to_transport_request FOR TESTING RAISING cx_static_check.

    METHODS delete_key_from_request FOR TESTING RAISING cx_static_check.

ENDCLASS.

CLASS ltc_how_to_use IMPLEMENTATION.

  METHOD class_setup.
    " only needed because this here is to show how to use the class
    zcl_trs_inject_facade=>inject_fm_access( NEW ltd_trs_fac_fm( ) ).
  ENDMETHOD.

  METHOD add_key_to_transport_request.

    cut = zcl_trs_tr_factory=>get_customizing_request( ).

    TRY.
        cut->add_key_to_request( i_e071k = VALUE e071k( object = 'TABU' objname = 'T005' tabkey = '200DE' ) ).

        " the method run through correct --> test did not fail
        cl_abap_unit_assert=>assert_true( abap_true ).

      CATCH zcx_trs_no_key.    "
        cl_abap_unit_assert=>fail( ).
      CATCH zcx_trs_wrong_object_type.    "
        cl_abap_unit_assert=>fail( ).
      CATCH zcx_trs_no_object_type.    "
        cl_abap_unit_assert=>fail( ).
    ENDTRY.

  ENDMETHOD.

  METHOD delete_key_from_request.

  ENDMETHOD.

ENDCLASS.