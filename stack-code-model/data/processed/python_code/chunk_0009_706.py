class ZCL_FLIFM_SELECTION definition
  public
  create public .

public section.

  types:
    TYR_BUKRS TYPE RANGE OF T001-BUKRS .
  types:
    TYR_RFAREA TYPE RANGE OF FKBER .

  class-methods INITIALIZE
    exporting
      !EV_GJAHR type GJAHR
      !EV_MONAT type MONAT
      !EV_CMP_GJAHR type GJAHR
      !ER_RFAREA type ZCL_FLIFM_FETCH=>TYR_RFAREA .
  class-methods VALIDATE_INPUT
    importing
      !IV_MONAT type MONAT
    raising
      ZCX_FLIFM_EXCEPTION .
  class-methods SET_DATA
    importing
      !IR_BUKRS type TYR_BUKRS optional
      !IR_RFAREA type TYR_RFAREA optional
      !IV_GJAHR type GJAHR optional
      !IV_MONAT type MONAT optional
      !IV_CMP_GJAHR type GJAHR optional
      !IV_LEVEL type SEU_LEVEL optional
      !IV_KTOPL type KTOPL optional
      !IV_VERSN type VERSN_011 optional
      !IV_WAERS type WAERS optional
      !IV_TO_PERIOD type ZFLIFME_TO_PERIOD optional
      !IV_ZERO type C optional
      !IV_PARALLEL type C optional .
  class-methods GET_BUKRS
    returning
      value(RR_BUKRS) type TYR_BUKRS .
  class-methods GET_VERSN
    returning
      value(RV_VERSN) type VERSN_011 .
  class-methods GET_PARALLEL
    returning
      value(RV_PARALLEL) type CHAR1 .
  class-methods GET_CMP_GJAHR
    returning
      value(RV_CMP_GJAHR) type GJAHR .
  class-methods GET_GJAHR
    returning
      value(RV_GJAHR) type GJAHR .
  class-methods GET_MONAT
    returning
      value(RV_MONAT) type MONAT .
  class-methods GET_LEVEL
    returning
      value(RV_LEVEL) type SEU_LEVEL .
  class-methods GET_KTOPL
    returning
      value(RV_KTOPL) type KTOPL .
  class-methods GET_WAERS
    returning
      value(RV_WAERS) type WAERS .
  class-methods GET_TO_PERIOD
    returning
      value(RV_TO_PERIOD) type ZFLIFME_TO_PERIOD .
  class-methods GET_PARA_ZERO
    returning
      value(RV_ZERO) type CHAR1 .
  class-methods GET_RFAREA
    returning
      value(RR_RFAREA) type TYR_RFAREA .
  PROTECTED SECTION.
private section.

  class-data MR_BUKRS type TYR_BUKRS .
  class-data MR_RFAREA type TYR_RFAREA .
  class-data MV_GJAHR type GJAHR .
  class-data MV_MONAT type MONAT .
  class-data MV_CMP_GJAHR type GJAHR .
  class-data MV_LEVEL type SEU_LEVEL .
  class-data MV_VERSN type VERSN_011 .
  class-data MV_WAERS type WAERS .
  class-data MV_TO_PERIOD type ZFLIFME_TO_PERIOD .
  class-data MV_ZERO type C .
  class-data MV_PARALLEL type C .
  class-data MV_KTOPL type KTOPL .

  methods _VALIDATE_COMPANY
    raising
      ZCX_FLIFM_EXCEPTION .
ENDCLASS.



CLASS ZCL_FLIFM_SELECTION IMPLEMENTATION.


  METHOD get_bukrs.

    rr_bukrs = mr_bukrs.

  ENDMETHOD.


  METHOD get_cmp_gjahr.

    rv_cmp_gjahr = mv_cmp_gjahr.

  ENDMETHOD.


  METHOD get_gjahr.

    rv_gjahr = mv_gjahr.

  ENDMETHOD.


  METHOD get_ktopl.

    rv_ktopl = mv_ktopl.

  ENDMETHOD.


  METHOD get_level.

    rv_level = mv_level.

  ENDMETHOD.


  METHOD get_monat.

    rv_monat = mv_monat.

  ENDMETHOD.


  METHOD get_parallel.

    rv_parallel = mv_parallel.

  ENDMETHOD.


  METHOD get_para_zero.

    rv_zero = mv_zero.

  ENDMETHOD.


  METHOD GET_RFAREA.
    RR_RFAREA = MR_RFAREA.
  ENDMETHOD.


  METHOD get_to_period.

    rv_to_period = mv_to_period.

  ENDMETHOD.


  METHOD get_versn.

    rv_versn = mv_versn.

  ENDMETHOD.


  METHOD get_waers.

    rv_waers = mv_waers.

  ENDMETHOD.


  METHOD INITIALIZE.

    EV_GJAHR     = SY-DATUM(4).
    EV_MONAT     = SY-DATUM+4(2).
    EV_CMP_GJAHR = EV_GJAHR - 1.

    DATA LRS_RFAREA LIKE LINE OF ER_RFAREA.

  ENDMETHOD.


  METHOD SET_DATA.


    IF IR_BUKRS IS NOT INITIAL.
      MR_BUKRS    = IR_BUKRS.
    ENDIF.

    IF IR_RFAREA IS NOT INITIAL.
      MR_RFAREA    = IR_RFAREA.
    ENDIF.

    IF IV_GJAHR IS NOT INITIAL.
      MV_GJAHR    = IV_GJAHR.
    ENDIF.

    IF IV_MONAT IS NOT INITIAL.
      MV_MONAT    = IV_MONAT.
    ENDIF.

    IF IV_CMP_GJAHR IS NOT INITIAL.
      MV_CMP_GJAHR = IV_CMP_GJAHR.
    ENDIF.

    IF IV_LEVEL IS NOT INITIAL.
      MV_LEVEL    = IV_LEVEL.
    ENDIF.

    IF IV_ZERO IS NOT INITIAL.
      MV_ZERO     = IV_ZERO.
    ENDIF.

    IF IV_VERSN IS NOT INITIAL.
      MV_VERSN    = IV_VERSN.
    ENDIF.

    IF IV_WAERS IS NOT INITIAL.
      MV_WAERS    = IV_WAERS.
    ENDIF.

    IF IV_TO_PERIOD IS NOT INITIAL.
      MV_TO_PERIOD    = IV_TO_PERIOD.
    ENDIF.

    IF IV_PARALLEL IS NOT INITIAL.
      MV_PARALLEL = IV_PARALLEL.
    ENDIF.

    IF IV_KTOPL IS NOT INITIAL.
      MV_KTOPL    = IV_KTOPL.
    ENDIF.


  ENDMETHOD.


  METHOD validate_input.

    IF iv_monat = '00'.
      MESSAGE e014.
    ENDIF.

    IF iv_monat > '16'.
      MESSAGE e014.
    ENDIF.

  ENDMETHOD.


  METHOD _validate_company.

  ENDMETHOD.
ENDCLASS.