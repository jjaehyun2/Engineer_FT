class ZCL_IM_DOP_MUST_US definition
  public
  final
  create public .

public section.

  interfaces ZIF_EX_DOP_MUST_BADI .
protected section.
private section.
ENDCLASS.



CLASS ZCL_IM_DOP_MUST_US IMPLEMENTATION.


  method ZIF_EX_DOP_MUST_BADI~KDV_HESAPLA.
    DATA : LS_VBAP TYPE VBAP,
           LV_TOPLAM TYPE P.

    CHECK FLT_VAL = 'US'.

    LOOP AT IT_VBAP INTO LS_VBAP.
      ADD LS_VBAP-NETWR TO LV_TOPLAM.
    ENDLOOP.

    EV_KDV = LV_TOPLAM * '0.10' .
  endmethod.
ENDCLASS.