CLASS z_cl_dataload DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.

    TYPES:
      BEGIN OF ty_s_mrp_controller ,
        plant             TYPE werks_d,
        mrpcontroller     TYPE dispo,
        mrpcontrollername TYPE dsnam,
      END OF ty_s_mrp_controller .
    TYPES:
      tt_mrp_controller TYPE TABLE OF ty_s_mrp_controller .
    TYPES:
      BEGIN OF ty_s_cost_center,
        costcenter      TYPE kostl,
        controllingarea TYPE kokrs,
        validfrom       TYPE dats,
        validto         TYPE dats,
        name            TYPE ktext,
        description     TYPE kltxt,
        type            TYPE kosar,
        hierarchygroup  TYPE khinr,
        incharge        TYPE verak,
        companycode     TYPE bukrs,
        profitcenter    TYPE prctr,
        functionalarea  TYPE fkber,
        currency        TYPE waers,
        actualrevenues  TYPE bkzer,
        planrevenues    TYPE pkzer,
        commitmentupdt  TYPE bkzob,
      END OF ty_s_cost_center .
    TYPES:
      tt_cost_center TYPE TABLE OF ty_s_cost_center .
    TYPES:
      BEGIN OF ty_s_cost_center_hier,
        groupname             TYPE bapiset_groupname,
        controllingarea       TYPE kokrs,
        parentgroup           TYPE bapiset_groupname,
        parentcontrollingarea TYPE kokrs,
        description           TYPE bapiset_descript,
      END OF ty_s_cost_center_hier .
    TYPES:
      tt_cost_center_hier TYPE TABLE OF ty_s_cost_center_hier .
    TYPES:
      BEGIN OF ty_s_profit_center,
        profitcenter    TYPE prctr,
        controllingarea TYPE kokrs,
        validfrom       TYPE dats,
        validto         TYPE dats,
        name            TYPE ktext,
        longtext        TYPE ltext,
        segment         TYPE fb_segment,
        hierarchygroup  TYPE phinr,
        incharge        TYPE verapc,
        companycode     TYPE bukrs,
        language        TYPE spras,
      END OF ty_s_profit_center .
    TYPES:
      tt_profit_center TYPE TABLE OF ty_s_profit_center .
    TYPES:
      BEGIN OF ty_s_profit_center_hier,
        groupname             TYPE bapiset_groupname,
        controllingarea       TYPE kokrs,
        parentgroup           TYPE bapiset_groupname,
        parentcontrollingarea TYPE kokrs,
        description           TYPE bapiset_descript,
      END OF ty_s_profit_center_hier .
    TYPES:
      tt_profit_center_hier TYPE TABLE OF ty_s_profit_center_hier .
    TYPES:
      BEGIN OF ty_s_segments ,
        code        TYPE  fb_segment,
        description TYPE text50,
      END OF ty_s_segments .
    TYPES:
      tt_segments TYPE TABLE OF ty_s_segments .
    TYPES:
      BEGIN OF ty_s_fct_area,
        code        TYPE fkber,
        description TYPE fkbtx,
      END OF ty_s_fct_area .
    TYPES:
      tt_fct_area TYPE TABLE OF ty_s_fct_area .
    TYPES:
      BEGIN OF ty_s_mat_group,
        code        TYPE matkl,
        description TYPE wgbez,
      END OF ty_s_mat_group .
    TYPES:
      tt_mat_group TYPE TABLE OF ty_s_mat_group .
    TYPES:
      BEGIN OF ty_s_pur_group,
        code        TYPE ekgrp,
        description TYPE eknam,
        telephone   TYPE ektel,
        extension   TYPE ad_tlxtns,
        fax         TYPE ektfx,
        email       TYPE ad_smtpadr,
      END OF ty_s_pur_group .
    TYPES:
      tt_pur_group TYPE TABLE OF ty_s_pur_group .
    TYPES:
      BEGIN OF ty_s_cust_group,
        code        TYPE kdgrp,
        description TYPE vtxtk,
      END OF ty_s_cust_group .
    TYPES:
      tt_cust_group TYPE TABLE OF ty_s_cust_group .
    TYPES:
      BEGIN OF ty_s_acc_clerk,
        cocode          TYPE bukrs,
        accountingclerk TYPE busab,
        name            TYPE sname_001s,
      END OF ty_s_acc_clerk .
    TYPES:
      tt_acc_clerk TYPE TABLE OF ty_s_acc_clerk .
    TYPES:
      BEGIN OF ty_s_sale_price ,
        materialnumber       TYPE matnr,
        salesorganization    TYPE vkorg,
        distributionchannel  TYPE vtweg,
        conditionamount      TYPE kbetr,
        conditionunit        TYPE kvmei,
        conditionpricingunit TYPE kpein,
        currency             TYPE waers,
        validfrom(8)         TYPE c,
        validon(8)           TYPE c,
        validto(8)           TYPE c,
      END OF ty_s_sale_price .
    TYPES:
      tt_sale_price TYPE TABLE OF ty_s_sale_price .
    TYPES:
      BEGIN OF ty_s_prod_vers ,
        materialnumber               TYPE matnr,
        plant                        TYPE werks_d,
        validto                      TYPE char10,
        validfrom                    TYPE char10,
        alternativebom               TYPE stalt,
        bomusage                     TYPE stlan,
        tasklisttype                 TYPE plnty,
        keyfortasklistgroup          TYPE plnnr,
        groupcounter                 TYPE plnal,
        procurementtype              TYPE beskz,
        specialprocurementtype       TYPE sobsl,
        lotsizeproductioncost        TYPE ck_losgr,
        productionline               TYPE sa_line1,
        planningidentifictation      TYPE mdv,
        prodversiondescription       TYPE vers_text,
        usageprobability             TYPE ck_ewahr,
        distributionkeyforquantity   TYPE sa_verto,
        repetitivemanufacturing      TYPE sa_versi,
        lotsizelowvalue              TYPE sa_losvn,
        lotsizeuppervalue            TYPE sa_losbs,
        backflushforrsheader         TYPE sa_rgekz,
        receivingstoragelocation     TYPE alort,
*              tasklisttype                 TYPE plnty,
        ratebasedplanning            TYPE ratenplan,
*              groupcounter                 TYPE plnal,
        roughcutplanning             TYPE grobplan,
        apportionmentstructure       TYPE csplit,
        othermaterialbom             TYPE mkal_matko,
        proposedstoragelocation      TYPE sa_elpro,
        defaultsupplyareacomponents  TYPE sa_prvbe,
        checkstatusproductionversion TYPE prfg_f,
        lastcheckproductionversion   TYPE mkprdat,
        productionversionislocked    TYPE mksp,
        ratebasedplanningcheckstatus TYPE prfg_r,
        preliminaryplancheckstatus   TYPE prfg_g,
        bomcheckstatusprodversion    TYPE prfg_s,
        referencematerial            TYPE vbob_ob_rfmat,


      END OF ty_s_prod_vers .
    TYPES:
      tt_prod_vers TYPE TABLE OF ty_s_prod_vers .
    TYPES:
      BEGIN OF ty_s_customer,
        customernumber           TYPE bu_partner,
        bptype                   TYPE bu_type,
        customername(40)         TYPE c,
        searchterm               TYPE bu_sort1,
        title                    TYPE ad_title,
        country                  TYPE land1,
        postalcode               TYPE ad_pstcd1,
        district                 TYPE ad_city2,
        timezone                 TYPE ad_tzone,
        category                 TYPE bptaxtype,
        taxjuristiction          TYPE ad_txjcd,
        taxnumber                TYPE bptaxnumxl,
        region                   TYPE regio,
        city                     TYPE ad_city1,
        street                   TYPE ad_street,
        houseno                  TYPE ad_hsnm1,
        sex                      TYPE bu_xsexm,
        naturalperson            TYPE bu_natural_person,
        companycode              TYPE bukrs,
        reconciliationaccount    TYPE akont,
        sortkey                  TYPE dzuawa,
        paymentterms             TYPE dzterm,
        paymentmethod            TYPE dzwels,
        dunningprocedure         TYPE mahna,
        salesorganization        TYPE vkorg,
        distributionchannel      TYPE vtweg,
        division                 TYPE spart,
        salesdistrict            TYPE bzirk,
        customergroup            TYPE kdgrp,
        orderprobability         TYPE awahr,
        currency                 TYPE waers,
        pricegroup               TYPE konda,
        customerpricingprocedure TYPE kalks,
        deliverypriority         TYPE lprio,
        ordercombination         TYPE kzazu,
        deliveringplant          TYPE vwerk,
        shippingconditions       TYPE vsbed,
        inconterms               TYPE inco1,
        incotermslocation1       TYPE inco2,
        termsofpaymentsales      TYPE dzterm,
        creditcontrolarea        TYPE kkber,
        countrysales             TYPE land1,
        taxcategory              TYPE tatyp,
        accountingclerk          TYPE busab,
        accountassignmentgroup   TYPE ktgrd,
        taxclassification        TYPE takld,
      END OF ty_s_customer .
    TYPES:
      tt_customer TYPE TABLE OF ty_s_customer .
    TYPES:
      BEGIN OF ty_s_vendor,
        vendornumber          TYPE bu_partner,
        bptype                TYPE bu_type,
        title                 TYPE ad_title,
        vendorname(40)        TYPE c,
        searchterm            TYPE bu_sort1,
        street                TYPE ad_street,
        housenumber           TYPE ad_hsnm1,
        country               TYPE land1,
        postalcode            TYPE ad_pstcd1,
        district              TYPE ad_city2,
        timezone              TYPE ad_tzone,
        taxjuristiction       TYPE ad_txjcd,
        region                TYPE regio,
        city                  TYPE ad_city1,
        sex                   TYPE bu_xsexm,
        naturalperson         TYPE bu_natural_person,
        legalform             TYPE bu_legenty,
        id                    TYPE bu_bkvid,
        countrybank           TYPE  bu_banks,
        bankkey               TYPE bu_bankk,
        bankaccount           TYPE bu_bankn,
        companycode           TYPE ekorg,
        reconciliationaccount TYPE akont,
        sortkey               TYPE dzuawa,
        paymentterms          TYPE dzterm,
        paymentmethod         TYPE dzwels,
        purchasingorg         TYPE ekorg,
        ordercurrency         TYPE waers,
        shippingconditions    TYPE vsbed,
        planneddeltime        TYPE plifz,
        schemagrpsupp         TYPE kalsk,
        automaticpo           TYPE kzaut,
        accountingclerk       TYPE busab,
      END OF ty_s_vendor .
    TYPES:
      tt_vendor TYPE TABLE OF ty_s_vendor .
    TYPES:
      BEGIN OF ty_s_activity_rate,
        controllingarea     TYPE kokrs,
        costcenter          TYPE kostl,
        fromperiod          TYPE perbl,
        toperiod            TYPE perbl,
        fiscalyear          TYPE gjahr,
        version             TYPE versn,
        activitytype        TYPE lstar,
        planactivity        TYPE rkpln-lst,
        distributionkeyvar  TYPE spred,
        distributionkeyquan TYPE spred,
        uom                 TYPE leinh,
        fixedprice          TYPE rkpln-tkf,
        variableprice       TYPE rkpln-tkv,
        priceunit           TYPE rkpln-tke,
        planpriceindicator  TYPE tarkz,
        alloccostelement    TYPE vksta,
        activitytypecat     TYPE latyp,
        equivalencenr       TYPE rkpln-aeq,
        scheduledactivity   TYPE rkpln-dis,
      END OF ty_s_activity_rate .
    TYPES:
      tt_activity_rate TYPE TABLE OF ty_s_activity_rate .
    TYPES:
      BEGIN OF ty_s_routing,
        material                  TYPE matnr,
        plant                     TYPE werks_d,
        workcenter                TYPE arbpl,
        controlkey                TYPE steus,
        description               TYPE ltxa1,
        basequantity              TYPE bmsch,
        unitofmeasureforactivity  TYPE msehi,
        break                     TYPE plpod-zmerh,
        setup                     TYPE vgw01,
        unitofmeasuresetup        TYPE msehi,
        activitytypesetup         TYPE lstar,
        machine                   TYPE vgw01,
        unitofmeasuremachine      TYPE msehi,
        activitytypemachine       TYPE lstar,
        labor                     TYPE vgw01,
        unitofmeasurelabor        TYPE msehi,
        activitytypelabor         TYPE lstar,
        maximumwaittime           TYPE plpod-zlmax,
        minimumwaittime           TYPE plpod-zlpro,
        standardqueuetime         TYPE plpod-zwnor,
        minimumqueuetime          TYPE plpod-zwmin,
        standardmovetime          TYPE plpod-ztnor,
        minimummovetime           TYPE plpod-ztmin,
        numberofsplits            TYPE plpod-splim,
        minimumprocessingtime     TYPE plpod-zminb,
        overlapping               TYPE plpod-uenicht,
        minoverlaptime            TYPE plpod-zminu,
        minsendaheadquantity      TYPE plpod-minwe,
        scrap                     TYPE plpod-aufak,
        numberoftimetickets       TYPE plpod-loanz,
        numberofconfirmationslips TYPE plpod-rsanz,
        numberofemployees         TYPE plpod-anzma,
        costingrelevancy          TYPE selkz,
        itemoutlineagreement      TYPE ebelp,
        planneddeliverytime       TYPE plifz,
        priceunit                 TYPE peinh,
        usage                     TYPE verwe,
        status                    TYPE plnst,
        fromlotsize               TYPE losvn,
        tolotsize                 TYPE losbs,
        unitofmeasure             TYPE msehi,
        partiallotassignment      TYPE plkod-ppkztlzu,
        sequence                  TYPE plfld-plnfl,
        sequencecategory          TYPE tca07-flgat,
        alignmentkey              TYPE tca52-auschl,
        backflush                 TYPE rgekz,
        operationnumber           TYPE vornr,

      END OF ty_s_routing .
    TYPES:
      tt_routing TYPE TABLE OF ty_s_routing .
    TYPES:
      BEGIN OF ty_s_bom,
        material     TYPE matnr,
        plant        TYPE werks_d,
        bomusage     TYPE stlan,
        itemcategory TYPE postp,
        component    TYPE matnr,
        quantity     TYPE rc29p-menge,
        bomstatus    TYPE stlst,
        unit         TYPE msehi,

      END OF ty_s_bom .
    TYPES:
      tt_bom TYPE TABLE OF ty_s_bom .
    TYPES:
      BEGIN OF  ty_s_material ,
        materialnumber                TYPE matnr,
        materialtype                  TYPE mtart,
        plant                         TYPE werks_d,
        storagelocation               TYPE lgort_d,
        valuationclass                TYPE bklas,
        salesorg                      TYPE vkorg,
        distchan                      TYPE vtweg,
        description                   TYPE maktx_d,
        baseunitofmeasurement         TYPE meins,
        materialgroup                 TYPE matkl,
        generalitemcategorygroup      TYPE mtpos_mara,
        grossweight                   TYPE brgew,
        netweight                     TYPE ntgew,
        volume                        TYPE volum,
        unitofweight                  TYPE gewei,
        deliveringplant               TYPE dwerk,
        cashdiscount                  TYPE sktof,
        taxtype                       TYPE tatyp,
        depcountry                    TYPE aland,
        taxclassification             TYPE taxkm,
        minimumorderquantity          TYPE aumng,
        minimumdeliveryquantity       TYPE mvke-lfmng,
        deliveryunit                  TYPE scmng,
        materialstatisticsgroup       TYPE versg,
        accountassignmentgroup        TYPE ktgrm,
        itemcategorygroup             TYPE mtpos,
        prodhierarchy                 TYPE prodh,
        availabilitycheck             TYPE mtvfp,
        transportationgroup           TYPE tragr,
        setuptime                     TYPE vrvez,
        loadinggroup                  TYPE ladgr,
        processingtime                TYPE vbeaz,
        basequanforcapacityplaninship TYPE vbamg,
        profitcenter                  TYPE prctr,
        mrptype                       TYPE dismm,
        reorderpoint                  TYPE minbe,
        planningtimefence             TYPE fxhor,
        mrpcontroller                 TYPE dispo,
        lotsize                       TYPE disls,
        minimumlotsize                TYPE bstmi,
        maximumlotsize                TYPE bstma,
        maximumstocklevel             TYPE mabst,
        takttime                      TYPE takzt,
        roundingvalue                 TYPE bstrf,
        assemblyscrap                 TYPE ausss,
        procurementtype               TYPE beskz,
        prodstoragelocation           TYPE marc-lgpro,
        inhouseproduction             TYPE dzeit,
        planneddeliverytime           TYPE plifz,
        grprocessingtime              TYPE webaz,
        schedulingmarginkeyforfloats  TYPE fhori,
        minsafetystock                TYPE eislo,
        servicelevel                  TYPE lgrad,
        safetytime                    TYPE shzet,
        periodindicator               TYPE perkz,
        strategygroup                 TYPE strgr,
        consumptionmode               TYPE vrmod,
        forwardconsumptionperiod      TYPE vint2,
        backwardconsumptionperiod     TYPE vint1,
        versionindicator              TYPE verkz,
        componentscrap                TYPE kausf,
        productionsupervisor          TYPE fevor,
        productionschedulingprofile   TYPE marc-sfcpf,
        undeliverytolerancelimit      TYPE uneto,
        overdeliverytolerancelimit    TYPE ueeto,
        worksetuptime                 TYPE ruezt,
        workprocessingtime            TYPE bearz,
        interoperationtime            TYPE tranz,
        basequantity                  TYPE basmg,
        numberofgrgislipstobeprinted  TYPE wesch,
        maximumstorageperiod          TYPE maxlz,
        minimumremainingshelflige     TYPE mhdrz,
        periodindicatorforshelflige   TYPE mara-iprkz,
        totalshelflife                TYPE mhdhb,
        storagepercentage             TYPE mhdlp,
        materialledgeractivated       TYPE xfeld, "mlmaa,
        materialpricedetermination    TYPE ckmlhd-mlast,
        standardprice                 TYPE stprs,
        priceunit                     TYPE peinh,
        pricecontrol                  TYPE vprsv,
        taxprice1                     TYPE bwprs,
        taxprice2                     TYPE bwps1,
        taxprice3                     TYPE vjbws,
        lowestvaluedevaluation        TYPE abwkz,
        commercialprice1              TYPE bwprh,
        commercialprice2              TYPE bwph1,
        commercialprice3              TYPE vjbwh,
        priceunitaccounting           TYPE bwpei,
        withquantitystructure         TYPE mbew-ekalr,
        variancekey                   TYPE awsls,
        costinglotsize                TYPE losgr,
        movingprice                   TYPE verpr,
        totalreplenishment            TYPE wzeit,
        purchasinggroup               TYPE ekgrp,
        backflush                     TYPE boolean,

      END OF ty_s_material .
    TYPES:
      tt_material TYPE TABLE OF ty_s_material .
    TYPES:
      BEGIN OF ty_s_workcenter ,
        plant                          TYPE werks_d,
        workcenter                     TYPE arbpl,
        description                    TYPE cr_ktext,
        wccategory                     TYPE ap_verwe,
        personresponsible              TYPE veran,
        usage                          TYPE ap_planv,
        stdvaluekey                    TYPE vorgschl,
        unitsofmeasurementofstdvalues1 TYPE parid,
        unitsofmeasurementofstdvalues2 TYPE parid,
        unitsofmeasurementofstdvalues3 TYPE parid,
        capacityutilization            TYPE kako-ngrad,
        capacitycategory               TYPE kapart,
        setupformula                   TYPE ap_form_k1,
        processingformula              TYPE ap_form_k2,
        costcenter                     TYPE kostl,
        durationofsetup                TYPE p3005-fort1,
        processingduration             TYPE p3005-fort2,
        capacityplannergrp             TYPE kako-planr,
        factorycalendarid              TYPE kako-kalid,
        activeversion                  TYPE kako-versa,
        baseunitofmeasure              TYPE meins,
        numberofindividualcapacities   TYPE kako-aznor,
        relevanttofinitescheduling     TYPE kako-kapter,
        canbeusedbyseveraloperations   TYPE kako-kapavo,
        longtermplanning               TYPE rc68k-kaplpl,
        version                        TYPE tc36-versn,
        controllingarea                TYPE tka01-kokrs,
        activitytype1                  TYPE lstar,
        activityformulakey1            TYPE tc25-ident,
        activityunit1                  TYPE msehi,
        referencedfield1               TYPE rc68a-flg_ref,
        activitytype2                  TYPE lstar,
        activityformulakey2            TYPE tc25-ident,
        activityunit2                  TYPE msehi,
        referencedfield2               TYPE rc68a-flg_ref,
        activitytype3                  TYPE lstar,
        activityformulakey3            TYPE tc25-ident,
        referencedfield3               TYPE rc68a-flg_ref,
        activityunit3                  TYPE msehi,

      END OF ty_s_workcenter .
    TYPES:
      tt_workcenter TYPE TABLE OF ty_s_workcenter .
    TYPES:
      BEGIN OF ty_s_sc_mapping,
        sequence        TYPE i,
        object_name(30) TYPE c,
        file_stamp(40)  TYPE c,
*        object_name TYPE string,
*        file_stamp  TYPE string,
      END OF ty_s_sc_mapping .
    TYPES:
      BEGIN OF ty_s_sc_file,
        file_name(40) TYPE c,
*        file_name TYPE string,
        file_path     TYPE string,
      END OF ty_s_sc_file .
    TYPES:
      tt_sc_mapping TYPE SORTED TABLE OF ty_s_sc_mapping WITH UNIQUE KEY sequence .
    TYPES:
      tt_sc_file TYPE TABLE OF ty_s_sc_file .
    TYPES:
      BEGIN OF ty_s_sc_obj_flag,
        object_name(30) TYPE c,
        required        TYPE boolean,
        sequence        TYPE i,
      END OF ty_s_sc_obj_flag .
    TYPES:
      tt_sc_obj_flag TYPE TABLE OF ty_s_sc_obj_flag .

    CONSTANTS gc_cost_center TYPE char40 VALUE 'COST CENTER' ##NO_TEXT.
    CONSTANTS gc_customer TYPE char40 VALUE 'CUSTOMER' ##NO_TEXT.
    CONSTANTS gc_vendor TYPE char40 VALUE 'VENDOR' ##NO_TEXT.
    CONSTANTS gc_material TYPE char40 VALUE 'MATERIAL' ##NO_TEXT.
    CONSTANTS gc_bom TYPE char40 VALUE 'BOM' ##NO_TEXT.
    CONSTANTS gc_routing TYPE char40 VALUE 'ROUTING' ##NO_TEXT.
    CONSTANTS gc_activity TYPE char40 VALUE 'ACTIVITY' ##NO_TEXT.
    CONSTANTS gc_workcenter TYPE char40 VALUE 'WORKCENTER' ##NO_TEXT.
    CONSTANTS gc_message_class TYPE string VALUE 'ZDL_CL_MESSAGE' ##NO_TEXT.
    CONSTANTS gc_bom_type TYPE char1 VALUE 'M' ##NO_TEXT.
    CONSTANTS gc_max_end_date TYPE char8 VALUE '99991231' ##NO_TEXT.
    CONSTANTS gc_prodvers TYPE char40 VALUE 'PRODVERS' ##NO_TEXT.
    CONSTANTS gc_sale_price TYPE char40 VALUE 'SALE_PRICE' ##NO_TEXT.
    DATA mv_valid_from_date TYPE char10 .
    CONSTANTS gc_profit_center TYPE char40 VALUE 'PROFIT CENTER' ##NO_TEXT.
    CONSTANTS gc_segment TYPE char40 VALUE 'SEGMENT' ##NO_TEXT.
    CONSTANTS gc_func_area TYPE char40 VALUE 'FUNCTIONAL AREA' ##NO_TEXT.
    CONSTANTS gc_mat_grp TYPE char40 VALUE 'MAT GROUP' ##NO_TEXT.
    CONSTANTS gc_pur_grp TYPE char40 VALUE 'PURCHASING GROUP' ##NO_TEXT.
    CONSTANTS gc_cust_grp TYPE char40 VALUE 'CUST GROUP' ##NO_TEXT.
    CONSTANTS gc_acc_clerks TYPE char40 VALUE 'ACCOUNTING CLERK' ##NO_TEXT.
    CONSTANTS gc_profit_hier TYPE char40 VALUE 'PROFIT HIERARCHY' ##NO_TEXT.
    CONSTANTS gc_cost_hier TYPE char40 VALUE 'COST HIERARCHY' ##NO_TEXT.
    CONSTANTS gc_substitution TYPE char40 VALUE 'SUBSTITUTION' ##NO_TEXT.
    CONSTANTS gc_mrp_controller TYPE char40 VALUE 'MRP CONTROLLER' ##NO_TEXT.
    DATA mv_valid_to_date TYPE char10 .

    METHODS constructor .
    METHODS process_data
      EXPORTING
        !ev_error TYPE boolean .
    METHODS fill_required_objects
      IMPORTING
        !it_obj_flag TYPE tt_sc_obj_flag
        !iv_test     TYPE boolean OPTIONAL .
    METHODS fill_files_and_paths
      IMPORTING
        !iv_filename      TYPE string
        !iv_file_fullpath TYPE string .
    METHODS check_input_files
      EXPORTING
        !ev_error TYPE boolean .
protected section.
private section.

  constants GC_PRODVERS_F type CHAR40 value 'Production Version' ##NO_TEXT.
  constants GC_SALE_PRICE_F type CHAR40 value 'Sale price' ##NO_TEXT.
  data MT_MAPPING type TT_SC_MAPPING .
  data MT_FILES type TT_SC_FILE .
  data MT_OBJECT_FLAG type TT_SC_OBJ_FLAG .
  constants GC_COST_CENTER_F type CHAR40 value 'Cost center' ##NO_TEXT.
  constants GC_CUSTOMER_F type CHAR40 value 'Customer' ##NO_TEXT.
  constants GC_VENDOR_F type CHAR40 value 'Vendor' ##NO_TEXT.
  constants GC_MATERIAL_F type CHAR40 value 'Material' ##NO_TEXT.
  constants GC_BOM_F type CHAR40 value 'Bom' ##NO_TEXT.
  constants GC_ROUTING_F type CHAR40 value 'Routing' ##NO_TEXT.
  constants GC_ACTIVITY_F type CHAR40 value 'Activity' ##NO_TEXT.
  constants GC_WORKCENTER_F type CHAR40 value 'Workcenter' ##NO_TEXT.
  constants GC_MATERIAL_F2 type CHAR40 value 'Material Details' ##NO_TEXT.
  data MV_TEST type BOOLEAN .
  constants GC_PROFIT_CENTER_F type CHAR40 value 'Profit center' ##NO_TEXT.
  constants GC_SEGMENT_F type CHAR40 value 'Segment' ##NO_TEXT.
  constants GC_FUNC_AREA_F type CHAR40 value 'Functional area' ##NO_TEXT.
  constants GC_MAT_GRP_F type CHAR40 value 'Mat group' ##NO_TEXT.
  constants GC_PUR_GRP_F type CHAR40 value 'Purchasing group' ##NO_TEXT.
  constants GC_CUST_GRP_F type CHAR40 value 'Cust group' ##NO_TEXT.
  constants GC_ACC_CLERKS_F type CHAR40 value 'Accounting clerk' ##NO_TEXT.
  constants GC_PROFIT_HIER_F type CHAR40 value 'Profit hier' ##NO_TEXT.
  constants GC_COST_HIER_F type CHAR40 value 'Cost hier' ##NO_TEXT.
  constants GC_SUBSTITUTION_F type CHAR40 value 'Substitution' ##NO_TEXT.
  constants GC_MRP_CONTROLLER_F type CHAR40 value 'MRP Controller' ##NO_TEXT.

  methods RETRIEVE_FILE_CONTENT
    importing
      !IV_OBJECT_NAME type CHAR30
      !IV_SEQUENCE type INT4
    exporting
      !EV_ERROR type BOOLEAN
      !ET_DATA type ANY TABLE .
  methods CALL_BAPI
    importing
      !IT_TABLE type DATA
      !IV_OBJECT_NAME type CHAR30
      !IV_SEQUENCE type I
    exporting
      !EV_ERROR type BOOLEAN .
  methods CALL_BAPI_MATERIAL
    importing
      !IT_MATERIAL type TT_MATERIAL
    exporting
      !EV_ERROR type BOOLEAN .
  methods CALL_BAPI_WORKCENTER
    importing
      !IT_WORKCENTER type TT_WORKCENTER
    exporting
      !EV_ERROR type BOOLEAN .
  methods CALL_BAPI_BOM
    importing
      !IT_BOM type TT_BOM
    exporting
      !EV_ERROR type BOOLEAN .
  methods CALL_BAPI_ROUTING
    importing
      !IT_ROUTING type TT_ROUTING
    exporting
      !EV_ERROR type BOOLEAN .
  methods CALL_BAPI_CUSTOMER
    importing
      !IT_CUSTOMER type TT_CUSTOMER
    exporting
      !EV_ERROR type BOOLEAN .
  methods CALL_BAPI_VENDOR
    importing
      !IT_VENDOR type TT_VENDOR
    exporting
      !EV_ERROR type BOOLEAN .
  methods CALL_BAPI_ACTIVITY_RATE
    importing
      !IT_ACTIVITY_RATES type TT_ACTIVITY_RATE
    exporting
      !EV_ERROR type BOOLEAN .
  methods SET_MATERIAL_VERSION_FLAG
    importing
      !IT_MATERIAL type TT_MATERIAL optional
      !IT_ROUTING type TT_ROUTING optional
    exporting
      !EV_ERROR type BOOLEAN .
  methods CALL_BAPI_PRODUCTION_VERSION
    importing
      !IT_PRODUCTION_VERSION type TT_PROD_VERS
    exporting
      !EV_ERROR type BOOLEAN .
  methods CALL_BAPI_SALE_PRICE
    importing
      !IT_SALE_PRICE type TT_SALE_PRICE
    exporting
      !EV_ERROR type BOOLEAN .
  methods CALL_BAPI_PROFIT_CENTER
    importing
      !IT_PROFIT_CENTER type TT_PROFIT_CENTER
    exporting
      !EV_ERROR type BOOLEAN .
  methods CALL_BAPI_PROFIT_CENTER_HIER
    importing
      !IT_PROFIT_CENTER_HIER type TT_PROFIT_CENTER_HIER
    exporting
      !EV_ERROR type BOOLEAN .
  methods CALL_BAPI_COST_CENTER
    importing
      !IT_COST_CENTER type TT_COST_CENTER
    exporting
      !EV_ERROR type BOOLEAN .
  methods CALL_BAPI_COST_CENTER_HIER
    importing
      !IT_COST_CENTER_HIER type TT_COST_CENTER_HIER
    exporting
      !EV_ERROR type BOOLEAN .
  methods CREATE_CUST_SEGMENT
    importing
      !IT_SEGMENT type TT_SEGMENTS
    exporting
      !EV_ERROR type BOOLEAN .
  methods CREATE_CUST_ACC_CLERK
    importing
      !IT_ACCOUNTING_CLERK type TT_ACC_CLERK
    exporting
      !EV_ERROR type BOOLEAN .
  methods CREATE_CUST_FUNCTIONAL_AREA
    importing
      !IT_FUNCTIONAL_AREA type TT_FCT_AREA
    exporting
      !EV_ERROR type BOOLEAN .
  methods CREATE_CUST_MATERIAL_GROUP
    importing
      !IT_MATERIAL_GROUP type TT_MAT_GROUP
    exporting
      !EV_ERROR type BOOLEAN .
  methods CREATE_CUST_PURCHASING_GROUP
    importing
      !IT_PURCHASING_GROUP type TT_PUR_GROUP
    exporting
      !EV_ERROR type BOOLEAN .
  methods CREATE_CUST_CUSTOMER_GROUP
    importing
      !IT_CUSTOMER_GROUP type TT_CUST_GROUP
    exporting
      !EV_ERROR type BOOLEAN .
  methods CREATE_CUST_MRP_CONTROLLER
    importing
      !IT_MRP_CONTROLLER type TT_MRP_CONTROLLER
    exporting
      !EV_ERROR type BOOLEAN .
ENDCLASS.



CLASS Z_CL_DATALOAD IMPLEMENTATION.


  METHOD call_bapi.

    DATA: lt_workcenter         TYPE tt_workcenter,
          ls_workcenter         TYPE ty_s_workcenter,
          lt_wc                 TYPE tt_workcenter,
          lt_material           TYPE tt_material,
          ls_material           TYPE ty_s_material,
          lt_bom                TYPE tt_bom,
          ls_bom                TYPE ty_s_bom,
          lt_routing            TYPE tt_routing,
          ls_routing            TYPE ty_s_routing,
          lt_customer           TYPE tt_customer,
          ls_customer           TYPE ty_s_customer,
          lt_vendor             TYPE tt_vendor,
          ls_vendor             TYPE ty_s_vendor,
          lt_activity_rate      TYPE tt_activity_rate,
          ls_activity_rate      TYPE ty_s_activity_rate,
          lt_prod_vers          TYPE tt_prod_vers,
          lt_sale_price         TYPE tt_sale_price,
          lt_segment            TYPE tt_segments,
          lt_fct_area           TYPE tt_fct_area,
          lt_acc_clerk          TYPE tt_acc_clerk,
          lt_mat_grp            TYPE tt_mat_group,
          lt_pur_grp            TYPE tt_pur_group,
          lt_cust_grp           TYPE tt_cust_group,
          lt_profit_center      TYPE tt_profit_center,
          lt_profit_center_hier TYPE tt_profit_center_hier,
          lt_cost_center        TYPE tt_cost_center,
          lt_cost_center_hier   TYPE tt_cost_center_hier,
          lt_mrp_controller     TYPE tt_mrp_controller.


    CASE iv_object_name.
      WHEN gc_workcenter.

        lt_workcenter = it_table.
        call_bapi_workcenter(
          EXPORTING
            it_workcenter = lt_workcenter
          IMPORTING
            ev_error      = ev_error
        ).

      WHEN gc_material.

        lt_material = it_table.
        call_bapi_material(
          EXPORTING
            it_material = lt_material
          IMPORTING
            ev_error    =  ev_error
        ).

      WHEN gc_bom.

        lt_bom = it_table.
        call_bapi_bom(
          EXPORTING
            it_bom   = lt_bom
          IMPORTING
            ev_error = ev_error
        ).

      WHEN gc_routing.

        lt_routing = it_table.
        call_bapi_routing(
          EXPORTING
            it_routing = lt_routing
          IMPORTING
            ev_error   =  ev_error
        ).

        IF ev_error = abap_false.
*          set_material_version_flag(
*            EXPORTING
*              it_routing = lt_routing
*            IMPORTING
*              ev_error    = ev_error    " Boolean Variable (X=True, -=False, Space=Unknown)
*          ).

        ENDIF.

      WHEN gc_activity.

        lt_activity_rate = it_table.
        call_bapi_activity_rate(
          EXPORTING
            it_activity_rates = lt_activity_rate
          IMPORTING
            ev_error          = ev_error
        ).

      WHEN gc_customer.

        lt_customer = it_table.
        call_bapi_customer(
          EXPORTING
            it_customer = lt_customer
          IMPORTING
            ev_error    = ev_error
        ).

      WHEN gc_vendor.

        lt_vendor = it_table.
        call_bapi_vendor(
          EXPORTING
            it_vendor = lt_vendor
          IMPORTING
            ev_error  = ev_error
        ).

      WHEN gc_prodvers.
        lt_prod_vers = it_table.

        call_bapi_production_version(
        EXPORTING
          it_production_version = lt_prod_vers
        IMPORTING
          ev_error              = ev_error    " Boolean Variable (X=True, -=False, Space=Unknown)
      ).

      WHEN gc_sale_price.
        lt_sale_price = it_table.

        call_bapi_sale_price(
          EXPORTING
            it_sale_price = lt_sale_price
          IMPORTING
            ev_error      =  ev_error   " Boolean Variable (X=True, -=False, Space=Unknown)
        ).

      WHEN gc_profit_center.
        lt_profit_center = it_table.
        call_bapi_profit_center(
          EXPORTING
            it_profit_center = lt_profit_center
          IMPORTING
            ev_error         = ev_error    " Boolean Variable (X=True, -=False, Space=Unknown)
        ).

      WHEN gc_profit_hier.
        lt_profit_center_hier = it_table.
        call_bapi_profit_center_hier(
          EXPORTING
            it_profit_center_hier = lt_profit_center_hier
          IMPORTING
            ev_error         = ev_error    " Boolean Variable (X=True, -=False, Space=Unknown)
        ).

      WHEN gc_cost_center.
        lt_cost_center = it_table.
        call_bapi_cost_center(
          EXPORTING
            it_cost_center = lt_cost_center
          IMPORTING
            ev_error         = ev_error    " Boolean Variable (X=True, -=False, Space=Unknown)
        ).

      WHEN gc_cost_hier.
        lt_cost_center_hier = it_table.
        call_bapi_cost_center_hier(
          EXPORTING
            it_cost_center_hier = lt_cost_center_hier
          IMPORTING
            ev_error         = ev_error    " Boolean Variable (X=True, -=False, Space=Unknown)
        ).

      WHEN gc_segment.
        lt_segment = it_table.
        create_cust_segment(
          EXPORTING
            it_segment = lt_segment
          IMPORTING
            ev_error   = ev_error     " Boolean Variable (X=True, -=False, Space=Unknown)
        ).

      WHEN gc_func_area.
        lt_fct_area = it_table.

        create_cust_functional_area(
          EXPORTING
            it_functional_area = lt_fct_area
          IMPORTING
            ev_error           = ev_error    " Boolean Variable (X=True, -=False, Space=Unknown)
        ).

      WHEN gc_acc_clerks.

        lt_acc_clerk = it_table.

        create_cust_acc_clerk(
          EXPORTING
            it_accounting_clerk = lt_acc_clerk
          IMPORTING
            ev_error            =  ev_error   " Boolean Variable (X=True, -=False, Space=Unknown)
        ).

      WHEN gc_mat_grp.

        lt_mat_grp = it_table.

        create_cust_material_group(
          EXPORTING
            it_material_group = lt_mat_grp
          IMPORTING
            ev_error          = ev_error    " Boolean Variable (X=True, -=False, Space=Unknown)
        ).

      WHEN gc_pur_grp.

        lt_pur_grp = it_table.

        create_cust_purchasing_group(
          EXPORTING
            it_purchasing_group = lt_pur_grp
          IMPORTING
            ev_error            =  ev_error   " Boolean Variable (X=True, -=False, Space=Unknown)
        ).

      WHEN gc_cust_grp.
        lt_cust_grp = it_table.

        create_cust_customer_group(
          EXPORTING
            it_customer_group = lt_cust_grp
          IMPORTING
            ev_error          = ev_error    " Boolean Variable (X=True, -=False, Space=Unknown)
        ).

      WHEN gc_mrp_controller.
        lt_mrp_controller = it_table.

        create_cust_mrp_controller(
          EXPORTING
            it_mrp_controller = lt_mrp_controller
          IMPORTING
            ev_error          = ev_error    " Boolean Variable (X=True, -=False, Space=Unknown)
        ).

      WHEN OTHERS.
    ENDCASE.

  ENDMETHOD.


  METHOD call_bapi_activity_rate.


    DATA: ls_activity_rate TYPE ty_s_activity_rate,
          ls_header_info   TYPE bapiplnhdr,
          lt_idx_structure TYPE TABLE OF bapiacpstru,
          lt_object        TYPE TABLE OF bapiacpobj,
          lt_per_value     TYPE TABLE OF bapiacpval,
          lt_tot_value     TYPE TABLE OF bapiacptot,
          lt_contrl        TYPE TABLE OF bapiacpctrl,
          lt_return        TYPE TABLE OF bapiret2,
          ls_idx_structure TYPE bapiacpstru,
          ls_object        TYPE bapiacpobj,
          ls_per_value     TYPE bapiacpval,
          ls_tot_value     TYPE bapiacptot,
          ls_contrl        TYPE bapiacpctrl,
          ls_return        TYPE bapiret2,
          ls_message       TYPE bapiret2,
          ls_db_return     TYPE bapiret2.

    DATA: lv_oi TYPE obj_indx,
          lv_vi TYPE val_indx,
          lv_ai TYPE atr_indx.

    IF it_activity_rates IS NOT INITIAL.
      LOOP AT it_activity_rates INTO ls_activity_rate.

        CLEAR: ls_header_info,
        ls_object,
        ls_idx_structure,
        ls_tot_value,
        ls_contrl,
        lt_contrl,
        lt_idx_structure,
        lt_object,
        lt_per_value,
        lt_return,
        lt_tot_value.

*** Fill header data
        ls_header_info-co_area = ls_activity_rate-controllingarea.
        ls_header_info-version = ls_activity_rate-version.
        ls_header_info-period_from = ls_activity_rate-fromperiod.
        ls_header_info-period_to = ls_activity_rate-toperiod.
        ls_header_info-fisc_year = ls_activity_rate-fiscalyear.
        ls_header_info-plan_currtype = 'C'.

*** Increment Object, Attribute and Value indexes for each iteration
        lv_oi = lv_oi + 000001.
        lv_vi = lv_vi + 000001.
        lv_ai = lv_ai + 000001.

* Object data
        ls_object-object_index = lv_oi.
        ls_object-acttype = ls_activity_rate-activitytype.
        ls_object-costcenter = ls_activity_rate-costcenter.
        APPEND ls_object TO lt_object.

* Index data
        ls_idx_structure-object_index = lv_oi.
        ls_idx_structure-value_index = lv_vi.
        ls_idx_structure-attrib_index = lv_ai.
        APPEND ls_idx_structure TO lt_idx_structure.

* Total data
        ls_tot_value-value_index = lv_vi.
        ls_tot_value-price_unit = ls_activity_rate-priceunit.
        ls_tot_value-price_var = ls_activity_rate-variableprice.
        ls_tot_value-price_fix = ls_activity_rate-fixedprice.

        ls_tot_value-dist_key_price_fix = ls_activity_rate-distributionkeyvar.
        ls_tot_value-dist_key_price_var = ls_activity_rate-distributionkeyvar.

        ls_tot_value-actvty_qty = ls_activity_rate-planactivity.
        ls_tot_value-dist_key_quan = ls_activity_rate-distributionkeyquan.
        ls_tot_value-equivalence_no = ls_activity_rate-equivalencenr.
        ls_tot_value-currency = 'USD'.
        APPEND ls_tot_value TO lt_tot_value.

* Control Record Data
        ls_contrl-attrib_index = lv_ai.
        ls_contrl-price_indicator = ls_activity_rate-planpriceindicator.
        ls_contrl-alloc_cost_elem = ls_activity_rate-alloccostelement.
        APPEND ls_contrl TO lt_contrl.

        CALL FUNCTION 'BAPI_COSTACTPLN_POSTACTOUTPUT'
          EXPORTING
            headerinfo     = ls_header_info
*           DELTA          = ' '
*           PRICE_QUANT_PLAN       = 'B'
          TABLES
            indexstructure = lt_idx_structure
            coobject       = lt_object
*           PERVALUE       =
            totvalue       = lt_tot_value
            contrl         = lt_contrl
            return         = lt_return.

        IF lt_return IS NOT INITIAL.
          LOOP AT lt_return INTO ls_return.
            ls_message-type = ls_return-type.
            ls_message-id = z_cl_dataload=>gc_message_class.
            ls_message-number = '030'.

            CONCATENATE gc_activity ls_activity_rate-costcenter ls_activity_rate-activitytype ls_activity_rate-version INTO ls_message-message_v1 SEPARATED BY space.
            IF strlen( ls_return-message ) > 50.
              ls_message-message_v2 = ls_return-message+0(50).
              ls_message-message_v3 = ls_return-message+50(50).
              ls_message-message_v4 = ls_return-message+100(50).
            ELSE.
              ls_message-message_v2 = ls_return-message.
            ENDIF.

            zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

            IF ls_return-type = 'A' OR ls_return-type = 'E'  OR ls_return-type = 'X'.
              ev_error = abap_true.
            ENDIF.
          ENDLOOP.
        ENDIF.
      ENDLOOP.

      IF ev_error = abap_false.
        CALL FUNCTION 'BAPI_TRANSACTION_COMMIT'
          IMPORTING
            return = ls_db_return.    " Return Messages

        IF ls_db_return IS INITIAL.
          ls_message-id = gc_message_class.
          ls_message-number = '010'.
          ls_message-type = 'S'.
          ls_message-message_v1 = z_cl_dataload=>gc_activity.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
        ELSE.
          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_db_return ).
        ENDIF.
      ELSE.
        CALL FUNCTION 'BAPI_TRANSACTION_ROLLBACK'
          IMPORTING
            return = ls_db_return.    " Return Messages

        IF ls_db_return IS NOT INITIAL.
          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_db_return ).
        ENDIF.
      ENDIF.
    ENDIF.

  ENDMETHOD.


  METHOD call_bapi_bom.

    DATA: ls_bom             TYPE ty_s_bom,
          ls_bom2            TYPE ty_s_bom,
          lt_bom2            TYPE tt_bom,
          lv_material        TYPE csap_mbom-matnr,
          lv_plant           TYPE csap_mbom-werks,
          lv_bom_usage       TYPE csap_mbom-stlan,
          lv_valid_from      TYPE csap_mbom-datuv,
          lv_change_no       TYPE csap_mbom-aennr,
          lv_revision_level  TYPE csap_mbom-revlv,
          ls_stko            TYPE stko_api01,
          lt_stpo            TYPE TABLE OF stpo_api01,
          lt_dep_data        TYPE TABLE OF csdep_dat,
          lt_dep_descr       TYPE TABLE OF csdep_desc,
          lt_dep_order       TYPE TABLE OF csdep_ord,
          lt_dep_source      TYPE TABLE OF csdep_sorc,
          lt_dep_doc         TYPE TABLE OF csdep_doc,
          lt_ltx_line        TYPE TABLE OF csltx_line,
          lt_stpu            TYPE TABLE OF stpu_api01,
          lt_sgt_bomc        TYPE sgt_comp_segment_t,
          ls_stpo            TYPE stpo_api01,
          ls_dep_data        TYPE csdep_dat,
          ls_dep_descr       TYPE csdep_desc,
          ls_dep_order       TYPE csdep_ord,
          ls_dep_source      TYPE csdep_sorc,
          ls_dep_doc         TYPE csdep_doc,
          ls_ltx_line        TYPE csltx_line,
          ls_stpu            TYPE stpu_api01,
          ls_sgt_bomc        TYPE LINE OF sgt_comp_segment_t,
          lv_warning         TYPE capiflag-flwarning,
          lv_bom_no          TYPE stko_api02-bom_no,
          lv_item_no         TYPE i,
          lv_item_number     TYPE sposn,
          flg_no_commit_work TYPE c,
          ls_message         TYPE  bapiret2,
          ls_old_bom         TYPE ty_s_bom,
          lv_index           TYPE i,
          lv_index_bom       TYPE i,
          lv_old_material    TYPE matnr,
          lv_deletion_flag   TYPE bapimatall-del_flag,
          ls_return          TYPE bapireturn1,
          lv_material_check  TYPE bapimatall-material,
          lt_return          TYPE TABLE OF bapiret2,
          ls_db_return       TYPE bapiret2.

    flg_no_commit_work = abap_true.
    EXPORT flg_no_commit_work = flg_no_commit_work TO MEMORY ID 'CS_CSAP'.
    lt_bom2 = it_bom.
    lv_item_no = 0.

    LOOP AT it_bom INTO ls_bom WHERE material IS NOT INITIAL.
      CLEAR: lv_material, lv_plant, lv_bom_no, lv_bom_usage, lv_valid_from, ls_stko, ls_stpo, lt_stpo, lv_warning, lv_change_no, lv_revision_level,
             ls_old_bom, lv_deletion_flag , ls_return.

      IF sy-tabix = 1 OR lv_old_material <> ls_bom-material.


        lv_material = ls_bom-material.
        lv_plant = ls_bom-plant.
        lv_bom_usage = ls_bom-bomusage.
        lv_valid_from = mv_valid_from_date.

* Fill STKO structure
        ls_stko-base_unit = ls_bom-unit.
        ls_stko-bom_status = ls_bom-bomstatus.
        ls_stko-base_quan = ls_bom-quantity.

* Fill STPO table
        LOOP AT lt_bom2 INTO ls_bom2 WHERE material = ls_bom-material AND plant = ls_bom-plant AND bomusage = ls_bom-bomusage.
          lv_index_bom = lv_index_bom + 1.

          lv_item_no = lv_item_no + 10.
          lv_item_number = lv_item_no.

          ls_stpo-item_categ = ls_bom2-itemcategory.
          ls_stpo-item_no = lv_item_number.
          ls_stpo-component =  ls_bom2-component.
          ls_stpo-comp_qty = ls_bom2-quantity.
          ls_stpo-comp_unit = ls_bom2-unit.
          APPEND ls_stpo TO lt_stpo.

        ENDLOOP.

        lv_material_check = ls_bom-material.
* Check existence of material
        CALL FUNCTION 'BAPI_MATERIAL_EXISTENCECHECK'
          EXPORTING
            material      = lv_material_check
          IMPORTING
            deletion_flag = lv_deletion_flag
            return        = ls_return.

        IF lv_deletion_flag = abap_true.
          ls_message-id = gc_message_class.
          ls_message-number = '011'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
          ls_message-message_v1 = ls_bom-material.
          ev_error = abap_true.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

        ELSEIF ls_return-type = cl_esh_adm_constants=>gc_msgty_e.
          ls_message-id = gc_message_class.
          ls_message-number = '027'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
          ls_message-message_v1 = ls_bom-material.
          ev_error = abap_true.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

        ELSE.
* Check if BOM already exists
          CALL FUNCTION 'BAPI_MAT_BOM_EXISTENCE_CHECK'
            EXPORTING
              material = lv_material_check
              plant    = ls_bom-plant
              bomusage = ls_bom-bomusage
            TABLES
              return   = lt_return.

          IF lt_return IS INITIAL.
            ls_message-id = gc_message_class.
            ls_message-number = '014'.
            ls_message-type = cl_esh_adm_constants=>gc_msgty_i.
            ls_message-message_v1 = ls_bom-material.


            zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
          ELSE.

            CALL FUNCTION 'CSAP_MAT_BOM_CREATE'
              EXPORTING
                material           = lv_material
                plant              = lv_plant
                bom_usage          = lv_bom_usage
                change_no          = lv_change_no
                revision_level     = lv_revision_level
                i_stko             = ls_stko
                fl_commit_and_wait = abap_false
              IMPORTING
                fl_warning         = lv_warning
                bom_no             = lv_bom_no
              TABLES
                t_stpo             = lt_stpo
              EXCEPTIONS
                error              = 1
                OTHERS             = 2.

            IF  sy-subrc IS NOT INITIAL.
              ev_error = abap_true.

              ls_message-id = gc_message_class.
              ls_message-number = '005'.
              ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
              ls_message-message_v1 = ls_bom-material.


              zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
            ENDIF.
          ENDIF.
        ENDIF.

        lv_old_material = ls_bom-material.

      ENDIF.
    ENDLOOP.

    IF ev_error = abap_false.
      CALL FUNCTION 'BAPI_TRANSACTION_ROLLBACK'
        IMPORTING
          return = ls_db_return.    " Return Messages

      flg_no_commit_work = abap_false.
      EXPORT flg_no_commit_work = flg_no_commit_work TO MEMORY ID 'CS_CSAP'.
      lt_bom2 = it_bom.
*      lv_item_no = 0.

      LOOP AT it_bom INTO ls_bom WHERE  material IS NOT INITIAL.
        CLEAR: lv_material, lv_plant, lv_bom_no, lv_bom_usage, lv_valid_from, ls_stko, ls_stpo, lt_stpo, lv_warning, lv_change_no, lv_revision_level,
               ls_old_bom, lv_deletion_flag , ls_return,  lv_material_check.

        lv_item_no = 0.
        IF sy-tabix = 1 OR lv_old_material <> ls_bom-material.


          lv_material = ls_bom-material.
          lv_plant = ls_bom-plant.
          lv_bom_usage = ls_bom-bomusage.
          lv_valid_from = mv_valid_from_date.

* Fill STKO structure
          ls_stko-base_unit = ls_bom-unit.
          ls_stko-bom_status = ls_bom-bomstatus.
          ls_stko-base_quan = ls_bom-quantity.

* Fill STPO table
          LOOP AT lt_bom2 INTO ls_bom2 WHERE material = ls_bom-material AND plant = ls_bom-plant AND bomusage = ls_bom-bomusage.
            lv_index_bom = lv_index_bom + 1.

            lv_item_no = lv_item_no + 10.
            lv_item_number = lv_item_no.

            ls_stpo-item_categ = ls_bom2-itemcategory.
            ls_stpo-item_no = lv_item_number.
            ls_stpo-component =  ls_bom2-component.
            ls_stpo-comp_qty = ls_bom2-quantity.
            ls_stpo-comp_unit = ls_bom2-unit.

            APPEND ls_stpo TO lt_stpo.

          ENDLOOP.

          lv_material_check = ls_bom-material.

* Check if BOM already exists
          CALL FUNCTION 'BAPI_MAT_BOM_EXISTENCE_CHECK'
            EXPORTING
              material = lv_material_check
              plant    = ls_bom-plant
              bomusage = ls_bom-bomusage
            TABLES
              return   = lt_return.

          IF lt_return IS NOT INITIAL.
            CALL FUNCTION 'CSAP_MAT_BOM_CREATE'
              EXPORTING
                material           = lv_material
                plant              = lv_plant
                bom_usage          = lv_bom_usage
                change_no          = lv_change_no
                valid_from         = lv_valid_from
                revision_level     = lv_revision_level
                i_stko             = ls_stko
                fl_commit_and_wait = abap_true
              IMPORTING
                fl_warning         = lv_warning
                bom_no             = lv_bom_no
              TABLES
                t_stpo             = lt_stpo
              EXCEPTIONS
                error              = 1
                OTHERS             = 2.

            IF  sy-subrc IS NOT INITIAL.
              ev_error = abap_true.

              ls_message-id = gc_message_class.
              ls_message-number = '005'.
              ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
              ls_message-message_v1 = ls_bom-material.

              zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
            ENDIF.
          ENDIF.
          lv_old_material = ls_bom-material.
        ENDIF.
      ENDLOOP.

      ls_message-number = '010'.
      ls_message-id = gc_message_class.
      ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
      ls_message-message_v1 = gc_bom.

      zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
    ELSE.
      CALL FUNCTION 'BAPI_TRANSACTION_ROLLBACK'
        IMPORTING
          return = ls_db_return.    " Return Messages

      IF ls_db_return IS NOT INITIAL.
        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_db_return ).
      ENDIF.
    ENDIF.

  ENDMETHOD.


  METHOD call_bapi_cost_center.

    DATA: lt_cost_center TYPE tt_cost_center,
          ls_cost_center TYPE ty_s_cost_center,
          lt_return      TYPE TABLE OF bapiret2,
          ls_return      TYPE bapiret2,
          ls_db_return   TYPE bapiret2,
          ls_message     TYPE bapiret2,
          lt_ccinputlist TYPE TABLE OF bapi0012_ccinputlist,
          ls_ccinputlist TYPE bapi0012_ccinputlist.
    TYPES:
      BEGIN OF ty_s_co_area,
        controllingarea TYPE kokrs,
      END OF ty_s_co_area.
    DATA: lt_co_area TYPE TABLE OF ty_s_co_area,
          ls_co_area TYPE ty_s_co_area.


    lt_cost_center = it_cost_center.
    MOVE-CORRESPONDING lt_cost_center TO lt_co_area.
    SORT lt_co_area BY controllingarea.
    DELETE ADJACENT DUPLICATES FROM lt_co_area.

    LOOP AT lt_co_area INTO ls_co_area.
      LOOP AT lt_cost_center INTO ls_cost_center WHERE controllingarea = ls_co_area-controllingarea AND costcenter IS NOT INITIAL.
        ls_ccinputlist-costcenter = ls_cost_center-costcenter.
        ls_ccinputlist-descript = ls_cost_center-description.
        ls_ccinputlist-name = ls_cost_center-name.
        ls_ccinputlist-profit_ctr = ls_cost_center-profitcenter.
        ls_ccinputlist-costcenter_type = ls_cost_center-type.
        ls_ccinputlist-func_area_long = ls_cost_center-functionalarea.
        ls_ccinputlist-comp_code = ls_cost_center-companycode.
        ls_ccinputlist-currency = ls_cost_center-currency.
        ls_ccinputlist-valid_from = ls_cost_center-validfrom.
        ls_ccinputlist-valid_to = ls_cost_center-validto.
        ls_ccinputlist-person_in_charge = ls_cost_center-incharge.
        ls_ccinputlist-costctr_hier_grp = ls_cost_center-hierarchygroup.
        ls_ccinputlist-lock_ind_actual_revenues = ls_cost_center-actualrevenues.
        ls_ccinputlist-lock_ind_plan_revenues = ls_cost_center-planrevenues.
        ls_ccinputlist-lock_ind_commitment_update = ls_cost_center-commitmentupdt.

        APPEND ls_ccinputlist TO lt_ccinputlist.
        CLEAR ls_ccinputlist.
      ENDLOOP.

      CALL FUNCTION 'BAPI_COSTCENTER_CREATEMULTIPLE'
        EXPORTING
          controllingarea = ls_co_area-controllingarea
*         TESTRUN         = ' '
*         MASTER_DATA_INACTIVE       = ' '
*         LANGUAGE        =
        TABLES
          costcenterlist  = lt_ccinputlist
          return          = lt_return
*         EXTENSIONIN     =
*         EXTENSIONOUT    =
        .

      IF lt_return IS NOT INITIAL.
        LOOP AT lt_return INTO ls_return.
          IF ls_return-type = cl_esh_adm_constants=>gc_msgty_a OR ls_return-type = cl_esh_adm_constants=>gc_msgty_e OR ls_return-type = cl_esh_adm_constants=>gc_msgty_x.
            ev_error = abap_true.
          ENDIF.

          ls_message-type = ls_return-type.
          ls_message-id = z_cl_dataload=>gc_message_class.
          ls_message-number = '030'.

          CONCATENATE gc_cost_center ls_return-message_v1 INTO ls_message-message_v1 SEPARATED BY space.

          IF strlen( ls_return-message ) > 50.
            ls_message-message_v2 = ls_return-message+0(50).
            ls_message-message_v3 = ls_return-message+50(50).
            ls_message-message_v4 = ls_return-message+100(50).
          ELSE.
            ls_message-message_v2 = ls_return-message.
          ENDIF.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
          CLEAR ls_message.
        ENDLOOP.
      ENDIF.

    ENDLOOP.

    IF ev_error = abap_false.
      CALL FUNCTION 'BAPI_TRANSACTION_COMMIT'
        IMPORTING
          return = ls_db_return.

      IF ls_db_return IS INITIAL.
        ls_message-id = gc_message_class.
        ls_message-number = '010'.
        ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
        ls_message-message_v1 = gc_cost_center.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
      ELSE.
        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_db_return ).
      ENDIF.
    ELSE.
      CALL FUNCTION 'BAPI_TRANSACTION_ROLLBACK'
        IMPORTING
          return = ls_db_return.    " Return Messages

      IF ls_db_return IS NOT INITIAL.
        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_db_return ).
      ENDIF.
    ENDIF.

  ENDMETHOD.


  METHOD call_bapi_cost_center_hier.

    DATA: lt_cost_center_hier TYPE tt_cost_center_hier,
          ls_cost_center_hier TYPE ty_s_cost_center_hier,
          ls_return           TYPE bapiret2,
          ls_return_parent    TYPE bapiret2,
          ls_message          TYPE bapiret2,
          ls_db_return        TYPE bapiret2,
          lt_nodes            TYPE TABLE OF bapiset_hier,
          ls_nodes            TYPE bapiset_hier,
          lt_hier             TYPE TABLE OF bapi1112_values,
          ls_hier             TYPE bapi1112_values,
          lv_valcount         TYPE bapiset_valcount,
          lv_duplicate        TYPE char1.

    CLEAR lv_duplicate.

    lt_cost_center_hier = it_cost_center_hier.

    LOOP AT lt_cost_center_hier INTO ls_cost_center_hier.

      IF ls_cost_center_hier-parentgroup = '0001'.
        SELECT SINGLE khinr FROM tka01 INTO ls_cost_center_hier-parentgroup
          WHERE kokrs = ls_cost_center_hier-parentcontrollingarea.
      ENDIF.

      CALL FUNCTION 'BAPI_COSTCENTERGROUP_GETDETAIL'
        EXPORTING
          controllingarea = ls_cost_center_hier-controllingarea
          groupname       = ls_cost_center_hier-groupname
*         LANGUAGE        =
        IMPORTING
          return          = ls_return
        TABLES
          hierarchynodes  = lt_nodes
          hierarchyvalues = lt_hier.


      IF lt_nodes IS INITIAL AND lt_hier IS INITIAL.


      CALL FUNCTION 'BAPI_COSTCENTERGROUP_GETDETAIL'
        EXPORTING
          controllingarea = ls_cost_center_hier-parentcontrollingarea
          groupname       = ls_cost_center_hier-parentgroup
*         LANGUAGE        =
        IMPORTING
          return          = ls_return_parent
        TABLES
          hierarchynodes  = lt_nodes
          hierarchyvalues = lt_hier.

      IF ls_return_parent IS INITIAL.
        ls_nodes-descript = ls_cost_center_hier-description.
        ls_nodes-groupname = ls_cost_center_hier-groupname.
        ls_nodes-hierlevel = '1'.
        ls_nodes-valcount = '0'.
        APPEND ls_nodes TO lt_nodes.


        CALL FUNCTION 'BAPI_COSTCENTERGROUP_CREATE'
          EXPORTING
            controllingareaimp = ls_cost_center_hier-controllingarea
*           TOPNODEONLY        = ' '
*           LANGUAGE           =
          IMPORTING
            controllingarea    = ls_cost_center_hier-controllingarea
            groupname          = ls_cost_center_hier-groupname
            return             = ls_return
          TABLES
            hierarchynodes     = lt_nodes
            hierarchyvalues    = lt_hier.
        IF ls_return IS NOT INITIAL.
          IF ls_return-type = cl_esh_adm_constants=>gc_msgty_a OR ls_return-type = cl_esh_adm_constants=>gc_msgty_e OR ls_return-type = cl_esh_adm_constants=>gc_msgty_x.
            ev_error = abap_true.
          ENDIF.

          ls_message-type = ls_return-type.
          ls_message-id = z_cl_dataload=>gc_message_class.
          ls_message-number = '030'.

          CONCATENATE gc_cost_hier ls_nodes-groupname INTO ls_message-message_v1 SEPARATED BY space.

          IF strlen( ls_return-message ) > 50.
            ls_message-message_v2 = ls_return-message+0(50).
            ls_message-message_v3 = ls_return-message+50(50).
            ls_message-message_v4 = ls_return-message+100(50).
          ELSE.
            ls_message-message_v2 = ls_return-message.
          ENDIF.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
          CLEAR ls_message.
        ENDIF.
      ELSE.
        IF ls_return_parent-type = cl_esh_adm_constants=>gc_msgty_a OR ls_return_parent-type = cl_esh_adm_constants=>gc_msgty_e OR ls_return_parent-type = cl_esh_adm_constants=>gc_msgty_x.
          ev_error = abap_true.
        ENDIF.

        ls_message-type = ls_return_parent-type.
        ls_message-id = z_cl_dataload=>gc_message_class.
        ls_message-number = '030'.

        CONCATENATE gc_cost_hier ls_cost_center_hier-parentgroup INTO ls_message-message_v1 SEPARATED BY space.

        IF strlen( ls_return_parent-message ) > 50.
          ls_message-message_v2 = ls_return_parent-message+0(50).
          ls_message-message_v3 = ls_return_parent-message+50(50).
          ls_message-message_v4 = ls_return_parent-message+100(50).
        ELSE.
          ls_message-message_v2 = ls_return_parent-message.
        ENDIF.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
        CLEAR ls_message.
      ENDIF.

        ELSE.
        ls_message-id = gc_message_class.
        ls_message-number = '046'.
        ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
        ls_message-message_v1 = ls_cost_center_hier-groupname.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
        lv_duplicate = 'X'.
        ENDIF.
    ENDLOOP.
   IF lv_duplicate IS INITIAL.
    IF ev_error = abap_false.
      CALL FUNCTION 'BAPI_TRANSACTION_COMMIT'
        IMPORTING
          return = ls_db_return.

      IF ls_db_return IS INITIAL.
        ls_message-id = gc_message_class.
        ls_message-number = '044'.
        ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
        ls_message-message_v1 = gc_cost_hier.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
      ELSE.
        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_db_return ).
      ENDIF.
    ELSE.
      CALL FUNCTION 'BAPI_TRANSACTION_ROLLBACK'
        IMPORTING
          return = ls_db_return.    " Return Messages

      IF ls_db_return IS NOT INITIAL.
        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_db_return ).
      ENDIF.
    ENDIF.
ENDIF.

  ENDMETHOD.


  METHOD call_bapi_customer.


    DATA: ls_customer       TYPE ty_s_customer,
          ls_partner_categ  TYPE bapibus1006_head-partn_cat,
          ls_central_data   TYPE bapibus1006_central,
          ls_address        TYPE bapibus1006_address,
          ls_central_org    TYPE bapibus1006_central_organ,
          ls_central_person TYPE bapibus1006_central_person,
          lv_busr_number    TYPE bu_partner,
          lt_return_0       TYPE TABLE OF bapiret2,
          ls_return_0       TYPE bapiret2,
          lt_return         TYPE TABLE OF bapiret2,
          ls_return         TYPE bapiret2,
          ls_tax            TYPE cmds_ei_tax_ind,
          ls_db_return      TYPE bapiret2.

    DATA: i_data                         TYPE cvis_ei_extern_t,
          lte_return                     TYPE bapiretm,
          lse_return                     LIKE LINE OF lte_return,
          wa_data                        LIKE LINE OF i_data,
          wa_partn                       TYPE bus_ei_extern,
          wa_partn_hdr                   TYPE bus_ei_header,
          wa_partn_hdr_object_instance   TYPE bus_ei_instance,
          wa_partn_ctr_data              TYPE bus_ei_central_data,
          wa_partn_ctr_data_common       TYPE bus_ei_bupa_central,
          wa_partn_ctr_data_role         TYPE bus_ei_bupa_roles,
          wa_partn_ctr_data_bankdetail   TYPE bus_ei_bankdetail,
          wa_partn_ctr_data_ident_number TYPE bus_ei_identification,
          wa_partn_ctr_data_taxnumber    TYPE BUS_EI_BUPA_TAXNUMBER , "bus_ei_taxnumber,
          wa_partn_ctr_data_addr         TYPE bus_ei_address,
          wa_partn_ctr_data_addr_addres  TYPE bus_ei_bupa_address,
          wa_partn_ctr_data_taxclass     TYPE bus_ei_tax_classification,
          wa_company                     TYPE cmds_ei_company,
          ls_msg                         TYPE bapiretc,
          v_partner.

    DATA: lt_sales           TYPE cmds_ei_sales_t,
          ls_sales           TYPE cmds_ei_sales,
          wa_relation        TYPE burs_ei_extern,
          lv_guid            TYPE sysuuid_c32,
          wa_role            TYPE bus_ei_bupa_roles,
          wa_role_2          TYPE bus_ei_bupa_roles,
          ls_function        TYPE cmds_ei_functions,
          ls_bapiret2        TYPE bapiret2,
          ls_dunning         TYPE cmds_ei_dunning,
          lt_check_existence TYPE TABLE OF bapiret2,
          ls_message         TYPE bapiret2,
          lv_check           TYPE boolean.

    IF it_customer IS NOT INITIAL.
      LOOP AT it_customer INTO ls_customer WHERE customernumber IS NOT INITIAL .
        CLEAR: lt_check_existence.

*** Check if customer is already created
        CALL FUNCTION 'BAPI_BUPA_EXISTENCE_CHECK'
          EXPORTING
            businesspartner = ls_customer-customernumber
          TABLES
            return          = lt_check_existence.

        IF lt_check_existence IS INITIAL.
          ls_message-id = gc_message_class.
          ls_message-number = '025'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_i.
          ls_message-message_v1 = ls_customer-customernumber .

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
        ELSE.

          lv_check = abap_true.
          CLEAR: lv_guid,
                 ls_central_data,
                 ls_central_org,
                 ls_central_person,
                 ls_address,
                 lv_busr_number,
                 wa_partn_hdr,
                 wa_role,
                 wa_role_2,
                 wa_company,
                 ls_dunning,
                 ls_sales,
                 wa_data, i_data,
                 ls_function,
                 wa_partn,
                 lt_return,
                 lt_return_0,
                 ls_return_0,
                 lte_return,
                 lse_return,
                 ls_message.

          ls_central_data-searchterm1 = ls_customer-searchterm.
          IF ls_customer-bptype = '1'.
            ls_central_person-lastname = ls_customer-customername.
            ls_central_person-sex = ls_customer-sex.
            ls_central_person-correspondlanguage = 'E'.
          ELSEIF ls_customer-bptype = '2'.
            ls_central_org-name1 = ls_customer-customername.
            ls_address-langu = 'E'.
          ENDIF.

          ls_central_data-title_key = ls_customer-title.
          ls_address-district = ls_customer-district.
          ls_address-postl_cod1 = ls_customer-postalcode.
          ls_address-city = ls_customer-city.
          ls_address-street = ls_customer-street.
          ls_address-house_no = ls_customer-houseno.
          ls_address-country = ls_customer-country.
          ls_address-region = ls_customer-region.
          ls_address-taxjurcode = ls_customer-taxjuristiction.
          ls_address-time_zone = ls_customer-timezone.


          IF ls_customer-bptype = '1'.
            CALL FUNCTION 'BAPI_BUPA_CREATE_FROM_DATA'
              EXPORTING
                businesspartnerextern = ls_customer-customernumber
                partnercategory       = '1'  "Organisation
                centraldata           = ls_central_data
                centraldataperson     = ls_central_person
                addressdata           = ls_address
              IMPORTING
                businesspartner       = lv_busr_number
              TABLES
                return                = lt_return_0.

          ELSEIF ls_customer-bptype = '2'.
            CALL FUNCTION 'BAPI_BUPA_CREATE_FROM_DATA'
              EXPORTING
                businesspartnerextern   = ls_customer-customernumber
                partnercategory         = '2'  "Organisation
                centraldata             = ls_central_data
                centraldataorganization = ls_central_org
                addressdata             = ls_address
              IMPORTING
                businesspartner         = lv_busr_number
              TABLES
                return                  = lt_return_0.
          ENDIF.

          IF lt_return_0 IS NOT INITIAL.
            LOOP AT lt_return_0 INTO ls_return_0.
              ls_message-type = ls_return_0-type.
              ls_message-id = z_cl_dataload=>gc_message_class.
              ls_message-number = '030'.

              CONCATENATE gc_customer ls_customer-customernumber INTO ls_message-message_v1 SEPARATED BY space.

              IF strlen( ls_return_0-message ) > 50.
                ls_message-message_v2 = ls_return_0-message+0(50).
                ls_message-message_v3 = ls_return_0-message+50(50).
                ls_message-message_v4 = ls_return_0-message+100(50).
              ELSE.
                ls_message-message_v2 = ls_return_0-message.
              ENDIF.

              zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

              IF ls_return_0-type = 'E' OR ls_return_0-type = 'A'.
                ev_error = abap_true.
              ENDIF.

            ENDLOOP.

            IF ev_error = abap_true.
              CONTINUE.
            ENDIF.

          ENDIF.

          CALL FUNCTION 'BAPI_BUPA_GET_NUMBERS'
            EXPORTING
              businesspartner        = lv_busr_number
            IMPORTING
              businesspartnerguidout = lv_guid.

          IF lv_guid IS NOT INITIAL.

            wa_partn_hdr-object_instance-bpartner     = lv_busr_number.
            wa_partn_hdr-object_instance-bpartnerguid = lv_guid.
            wa_partn_hdr-object_task              = 'M'.

            MOVE-CORRESPONDING wa_partn_hdr TO wa_partn-header.
            IF ls_customer-bptype = '1'.
              wa_partn-central_data-taxnumber-common-data-nat_person = ls_customer-naturalperson.
              wa_partn-central_data-taxnumber-common-datax-nat_person = 'X'.
            ENDIF.
            MOVE-CORRESPONDING wa_partn TO wa_data-partner.

********* FI Customer
            wa_role_2-task = 'M'. "Modify
            wa_role_2-data_key = 'FLCU00'. "Role key - customer
            wa_role_2-data-rolecategory = 'FLCU00'.
            wa_role_2-data-valid_from = sy-datum.
            wa_role_2-data-valid_to = '99991231'.
            wa_role_2-currently_valid = abap_true.

            wa_role_2-datax-valid_from = abap_true.
            wa_role_2-datax-valid_to = abap_true.

            APPEND wa_role_2 TO wa_data-partner-central_data-role-roles.

********** Customer
            wa_role-task = 'M'. "Modify
            wa_role-data_key = 'FLCU01'. "Role key - customer
            wa_role-data-rolecategory = 'FLCU01'.
            wa_role-data-valid_from = sy-datum.
            wa_role-data-valid_to = '99991231'.
            wa_role-currently_valid = abap_true.

            wa_role-datax-valid_from = abap_true.
            wa_role-datax-valid_to = abap_true.

            APPEND wa_role TO wa_data-partner-central_data-role-roles.
            wa_data-partner-central_data-role-current_state = abap_true.


*--- Customer / company data ------------------------------------
            wa_company-task        = 'M'.    "Modify
            wa_company-data_key-bukrs = ls_customer-companycode.
            wa_company-data-zterm  = ls_customer-paymentterms.
            wa_company-data-akont = ls_customer-reconciliationaccount.
            wa_company-data-zuawa = ls_customer-sortkey.
            wa_company-data-zwels = ls_customer-paymentmethod.
            wa_company-data-busab = ls_customer-accountingclerk.

            wa_company-datax-zterm = 'X'.
            wa_company-datax-akont = 'X'.
            wa_company-datax-zuawa = 'X'.
            wa_company-datax-zwels = 'X'.
            wa_company-datax-busab = 'X'.

            ls_dunning-data-mahna = ls_customer-dunningprocedure.
            IF ls_customer-dunningprocedure IS NOT INITIAL.
              ls_dunning-datax-mahna = 'X'.
            ENDIF.
            APPEND ls_dunning TO wa_company-dunning-dunning.

            APPEND wa_company TO wa_data-customer-company_data-company.
            wa_data-customer-company_data-current_state = abap_true.

*--- Customer / sales organization data ------------------------------------
            ls_sales-task = 'M'.
            ls_sales-data_key-vkorg = ls_customer-salesorganization.
            ls_sales-data_key-vtweg = ls_customer-distributionchannel.
            ls_sales-data_key-spart = ls_customer-division.


            ls_sales-data-bzirk = ls_customer-salesdistrict.
            ls_sales-data-kdgrp = ls_customer-customergroup.
            ls_sales-data-awahr = ls_customer-orderprobability.
            ls_sales-data-waers = ls_customer-currency.
            ls_sales-data-konda = ls_customer-pricegroup.
            ls_sales-data-kalks = ls_customer-customerpricingprocedure.
            ls_sales-data-lprio = ls_customer-deliverypriority.
            ls_sales-data-kzazu = ls_customer-ordercombination.
            ls_sales-data-vwerk = ls_customer-deliveringplant.
            ls_sales-data-vsbed = ls_customer-shippingconditions.
            ls_sales-data-inco1 = ls_customer-inconterms.
            ls_sales-data-inco2_l = ls_customer-incotermslocation1.
            ls_sales-data-zterm = ls_customer-termsofpaymentsales.
            ls_sales-data-kkber = ls_customer-creditcontrolarea.
            ls_sales-data-ktgrd = ls_customer-accountassignmentgroup.

            ls_sales-datax-bzirk = 'X'.
            ls_sales-datax-kdgrp = 'X'.
            ls_sales-datax-awahr = 'X'.
            ls_sales-datax-waers = 'X'.
            ls_sales-datax-konda = 'X'.
            ls_sales-datax-kalks = 'X'.
            ls_sales-datax-lprio = 'X'.
            IF ls_customer-ordercombination IS NOT INITIAL.
              ls_sales-datax-kzazu = 'X'.
            ENDIF.
            ls_sales-datax-vwerk = 'X'.
            ls_sales-datax-vsbed = 'X'.
            ls_sales-datax-inco1 = 'X'.
            ls_sales-datax-inco2_l  = 'X'.
            ls_sales-datax-zterm = 'X'.
            ls_sales-datax-kkber = 'X'.
            ls_sales-datax-ktgrd = 'X'.

            ls_tax-data_key-aland = ls_customer-countrysales.
            ls_tax-data_key-tatyp = ls_customer-taxcategory.
            ls_tax-data-taxkd = ls_customer-taxclassification.

            ls_tax-datax-taxkd = 'X'.
            APPEND ls_tax TO wa_data-customer-central_data-tax_ind-tax_ind.

            ls_function-task = 'I'.
            ls_function-data_key-parvw = 'RE'.
            APPEND ls_function TO ls_sales-functions-functions.

            ls_function-data_key-parvw = 'AG'.
            APPEND ls_function TO ls_sales-functions-functions.

            ls_function-data_key-parvw = 'RG'.
            APPEND ls_function TO ls_sales-functions-functions.

            ls_function-data_key-parvw = 'WE'.
            APPEND ls_function TO ls_sales-functions-functions.

            APPEND ls_sales TO wa_data-customer-sales_data-sales.
            wa_data-customer-sales_data-current_state = space.

*--- Customer / Header --------------------------------------------
            wa_data-customer-header-object_task = 'I'.
            wa_data-customer-header-object_instance = lv_busr_number.
            wa_data-ensure_create-create_customer = abap_true.

*--- Add tax Number **--------- addition by i065658
            wa_data-partner-central_data-taxnumber-current_state = abap_true.
            wa_partn_ctr_data_taxnumber-task = 'I'.
            wa_partn_ctr_data_taxnumber-DATA_KEY-TAXTYPE =  ls_customer-category.  " TAXNUMBER TAXNUMXL
            wa_partn_ctr_data_taxnumber-DATA_KEY-TAXNUMBER = ls_customer-taxnumber.
            append wa_partn_ctr_data_taxnumber to wa_data-partner-central_data-taxnumber-TAXNUMBERS.
*            append wa_partn_ctr_data_taxnumber to wa_data-partner-central_data-taxnumber-TAXNUMBERS.
*********            end of addition by i065658

            APPEND wa_data TO i_data.

            CALL FUNCTION 'CVI_EI_INBOUND_MAIN'
              EXPORTING
                i_data   = i_data
              IMPORTING
                e_return = lte_return.

            IF lte_return IS NOT INITIAL.
              LOOP AT lte_return INTO lse_return.
                LOOP AT lse_return-object_msg INTO ls_msg.
                  ls_message-type = ls_msg-type.
                  ls_message-id = z_cl_dataload=>gc_message_class.
                  ls_message-number = '030'.

                  CONCATENATE gc_customer ls_customer-customernumber INTO ls_message-message_v1 SEPARATED BY space.

                  IF strlen( ls_msg-message ) > 50.
                    ls_message-message_v2 = ls_msg-message+0(50).
                    ls_message-message_v3 = ls_msg-message+50(50).
                    ls_message-message_v4 = ls_msg-message+100(50).
                  ELSE.
                    ls_message-message_v2 = ls_msg-message.
                  ENDIF.

                  zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
                  CLEAR ls_message.

                  IF ls_msg-type = cl_esh_adm_constants=>gc_msgty_a OR ls_msg-type = cl_esh_adm_constants=>gc_msgty_e OR ls_msg-type = cl_esh_adm_constants=>gc_msgty_x.
                    ev_error = abap_true.
                  ENDIF.
                ENDLOOP.
              ENDLOOP.
            ENDIF.
          ENDIF.

        ENDIF.
      ENDLOOP.

      IF lv_check = abap_true.
        IF ev_error = abap_false.
          CALL FUNCTION 'BAPI_TRANSACTION_COMMIT'
            IMPORTING
              return = ls_db_return.    " Return Messages

          IF ls_db_return IS INITIAL.
            ls_message-id = gc_message_class.
            ls_message-number = '010'.
            ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
            ls_message-message_v1 = gc_customer.

            zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
          ELSE.
            zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_db_return ).
          ENDIF.
        ELSE.
          CALL FUNCTION 'BAPI_TRANSACTION_ROLLBACK'
            IMPORTING
              return = ls_db_return.    " Return Messages

          IF ls_db_return IS NOT INITIAL.
            zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_db_return ).
          ENDIF.
        ENDIF.
      ENDIF.
    ENDIF.

  ENDMETHOD.


  METHOD call_bapi_material.

    DATA:

      ls_headdata1      TYPE bapimathead,
      ls_mara1          TYPE bapi_mara,
      ls_marax1         TYPE bapi_marax,
      ls_marc1          TYPE bapi_marc,
      ls_marcx1         TYPE bapi_marcx,
      ls_mpop1          TYPE bapi_mpop,
      ls_mpopx1         TYPE bapi_mpopx,
      ls_mpgd1          TYPE bapi_mpgd,
      ls_mpgdx1         TYPE bapi_mpgdx,
      ls_mard1          TYPE bapi_mard,
      ls_mardx1         TYPE bapi_mardx,
      ls_mbew1          TYPE bapi_mbew,
      ls_mbewx1         TYPE bapi_mbewx,
      ls_mlgn1          TYPE bapi_mlgn,
      ls_mlgnx1         TYPE bapi_mlgnx,
      ls_mvke1          TYPE bapi_mvke,
      ls_mvkex1         TYPE bapi_mvkex,
      ls_mlgt1          TYPE bapi_mlgt,
      ls_mlgtx1         TYPE bapi_mlgtx,
      ls_return1        TYPE bapiret2,
      ls_makt1          TYPE bapi_makt,
      ls_marm1          TYPE bapi_marm,
      ls_marmx1         TYPE bapi_marmx,
      lt_makt1          TYPE TABLE OF bapi_makt,
      lt_marm1          TYPE TABLE OF bapi_marm,
      lt_marmx1         TYPE TABLE OF bapi_marmx,
      ls_headdata       TYPE bapie1matheader,
      ls_mara           TYPE bapie1mara,
      ls_marax          TYPE bapie1marax,
      ls_marc           TYPE bapie1marc,
      ls_marcx          TYPE bapie1marcx,
      ls_mpop           TYPE bapie1mpop,
      ls_mpopx          TYPE bapie1mpopx,
      ls_mpgd           TYPE bapie1mpgd,
      ls_mpgdx          TYPE bapie1mpgdx,
      ls_mard           TYPE bapie1mard,
      ls_mardx          TYPE bapie1mardx,
      ls_mbew           TYPE bapie1mbew,
      ls_mbewx          TYPE bapie1mbewx,
      ls_mlgn           TYPE bapie1mlgn,
      ls_mlgnx          TYPE bapie1mlgnx,
      ls_mvke           TYPE bapie1mvke,
      ls_mvkex          TYPE bapie1mvkex,
      ls_mlgt           TYPE bapie1mlgt,
      ls_mlgtx          TYPE bapie1mlgtx,
      ls_return         TYPE bapiret2,
      lt_headdata       TYPE TABLE OF bapie1matheader,
      lt_mara           TYPE TABLE OF bapie1mara,
      lt_marax          TYPE TABLE OF bapie1marax,
      lt_marc           TYPE TABLE OF bapie1marc,
      lt_marcx          TYPE TABLE OF bapie1marcx,
      lt_mpop           TYPE TABLE OF bapie1mpop,
      lt_mpopx          TYPE TABLE OF bapie1mpopx,
      lt_mpgd           TYPE TABLE OF bapie1mpgd,
      lt_mpgdx          TYPE TABLE OF bapie1mpgdx,
      lt_mard           TYPE TABLE OF bapie1mard,
      lt_mardx          TYPE TABLE OF bapie1mardx,
      lt_mbew           TYPE TABLE OF bapie1mbew,
      lt_mbewx          TYPE TABLE OF bapie1mbewx,
      lt_mlgn           TYPE TABLE OF bapie1mlgn,
      lt_mlgnx          TYPE TABLE OF bapie1mlgnx,
      lt_mvke           TYPE TABLE OF bapie1mvke,
      lt_mvkex          TYPE TABLE OF bapie1mvkex,
      lt_mlgt           TYPE TABLE OF bapie1mlgt,
      lt_mlgtx          TYPE TABLE OF bapie1mlgtx,
      lt_return         TYPE TABLE OF bapiret2,
      lt_makt           TYPE TABLE OF bapie1makt,
      lt_marm           TYPE TABLE OF bapie1marm,
      lt_marmx          TYPE TABLE OF bapie1marmx,
      lt_mean           TYPE TABLE OF bapie1mean,
      lt_mltx           TYPE TABLE OF bapie1mltx,
      lt_mlan           TYPE TABLE OF bapie1mlan,
      lt_matreturn      TYPE TABLE OF bapie1matreturn2,
      lt_mfhm           TYPE TABLE OF bapie1mfhm,
      lt_mfhmx          TYPE TABLE OF bapie1mfhmx,
      ls_makt           TYPE bapie1makt,
      ls_marm           TYPE bapie1marm,
      ls_marmx          TYPE bapie1marmx,
      ls_material       TYPE ty_s_material,
      lv_iso_langu      TYPE laiso,
      ls_message        TYPE bapiret2,
      lv_deletion_flag  TYPE bapimatall-del_flag,
      ls_bapireturn1    TYPE bapireturn1,
      lv_material_check TYPE bapimatall-material,
      temp_marc         TYPE marc,
      lv_check          TYPE boolean,
*      lt_mlan TYPE TABLE OF BAPIE1MLAN,
      ls_mlan           TYPE bapie1mlan,
      lt_mlan1          TYPE TABLE OF bapi_mlan,
      ls_mlan1          TYPE bapi_mlan.

    LOOP AT it_material INTO ls_material WHERE materialnumber IS NOT INITIAL .
* Check if material already exists

      CLEAR: ls_headdata, ls_makt,ls_mara,ls_marax,ls_marc, ls_marcx,ls_mard, ls_mardx,ls_marm, ls_marmx,ls_mbew , ls_mbewx,
                   ls_mlgn, ls_mlgnx, ls_mlgt , ls_mlgtx, ls_mpgd , ls_mpgdx, ls_mpop , ls_mpopx, ls_mvke, ls_mvkex, lt_marm, lt_makt, ls_return,
                   lt_headdata, lt_makt,lt_mara,lt_marax,lt_marc, lt_marcx,lt_mard, lt_mardx,lt_marm, lt_marmx,lt_mbew , lt_mbewx,
                   lt_mlgn, lt_mlgnx, lt_mlgt , lt_mlgtx, lt_mpgd , lt_mpgdx, lt_mpop , lt_mpopx, lt_mvke, lt_mvkex, lt_marm, lt_makt, lt_return,
                   lv_material_check, lv_deletion_flag, ls_return1, ls_bapireturn1,temp_marc.

      lv_material_check = ls_material-materialnumber.

      CALL FUNCTION 'BAPI_MATERIAL_EXISTENCECHECK'
        EXPORTING
          material      = lv_material_check
        IMPORTING
          deletion_flag = lv_deletion_flag
          return        = ls_bapireturn1.

      IF lv_deletion_flag = abap_true.
* Material is flagged for deletion
        ls_message-id = gc_message_class.
        ls_message-number = '011'.
        ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
        ls_message-message_v1 = ls_material-materialnumber.
        ev_error = abap_true.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

      ELSE. " ELSEIF ls_bapireturn1-type = cl_esh_adm_constants=>gc_msgty_s.
* Material is already created

***         check if it exists in the plant/compcode/org unit it is trying to create
        SELECT single * FROM marc INTO temp_marc WHERE matnr = lv_material_check AND werks = ls_material-plant.
        IF sy-subrc IS INITIAL. " already exists in the plant
          ls_message-id = gc_message_class.
          ls_message-number = '019'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_i.
          ls_message-message_v1 = ls_material-materialnumber.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

        ELSE.
          lv_check = abap_true.
* Check if material can be created

* Fill HEADDATA structure

          ls_headdata-material = ls_material-materialnumber.
          ls_headdata-matl_type = ls_material-materialtype.
          ls_headdata-material_long = ls_material-materialnumber .
          ls_headdata-ind_sector = 'M'.
          ls_headdata-basic_view = abap_true.
          ls_headdata-sales_view = abap_true.
          ls_headdata-purchase_view = abap_true.
          ls_headdata-mrp_view = abap_true.
          ls_headdata-forecast_view = abap_true.
          ls_headdata-work_sched_view = abap_true.
          ls_headdata-prt_view = abap_true.
          ls_headdata-storage_view = abap_true.
          ls_headdata-warehouse_view = abap_true.
          ls_headdata-quality_view = abap_true.
          ls_headdata-account_view = abap_true.
          ls_headdata-cost_view = abap_true.

          APPEND ls_headdata TO lt_headdata.

* Fill MARC structure
          ls_marc-plant = ls_material-plant .
          ls_marc-availcheck = ls_material-availabilitycheck.
          ls_marc-loadinggrp = ls_material-loadinggroup.
          ls_marc-profit_ctr = ls_material-profitcenter.
          ls_marc-mrp_type = ls_material-mrptype .
          ls_marc-mrp_ctrler = ls_material-mrpcontroller .
          ls_marc-lotsizekey = ls_material-lotsize.
          ls_marc-proc_type = ls_material-procurementtype.
          ls_marc-iss_st_loc = ls_material-prodstoragelocation.
          ls_marc-inhseprodt = ls_material-inhouseproduction.
          ls_marc-period_ind = ls_material-periodindicator.
          ls_marc-plan_strgp = ls_material-strategygroup .
          ls_marc-consummode = ls_material-consumptionmode.
          ls_marc-fwd_cons = ls_material-forwardconsumptionperiod.
          ls_marc-bwd_cons = ls_material-backwardconsumptionperiod.
          ls_marc-replentime = ls_material-totalreplenishment.
          ls_marc-production_scheduler = ls_material-productionsupervisor.
          ls_marc-prodprof = ls_material-productionschedulingprofile.
          ls_marc-variance_key = ls_material-variancekey .
          ls_marc-lot_size = ls_material-costinglotsize.
          ls_marc-material = ls_material-materialnumber.
          ls_marc-material_long = ls_material-materialnumber.
          ls_marc-pur_group = ls_material-purchasinggroup.
          ls_marc-backflush = ls_material-backflush.

          APPEND ls_marc TO lt_marc.


* Fill MARCX structure
          ls_marcx-plant = ls_material-plant.
          IF ls_marc-availcheck IS NOT INITIAL.
            ls_marcx-availcheck = abap_true.
          ENDIF.

          IF ls_marc-loadinggrp IS NOT INITIAL.
            ls_marcx-loadinggrp = abap_true.
          ENDIF.

          IF ls_marc-profit_ctr IS NOT INITIAL.
            ls_marcx-profit_ctr = abap_true.
          ENDIF.

          IF ls_marc-mrp_type IS NOT  INITIAL.
            ls_marcx-mrp_type = abap_true.
          ENDIF.

          IF ls_marc-mrp_ctrler IS NOT INITIAL.
            ls_marcx-mrp_ctrler = abap_true.
          ENDIF.

          IF ls_marc-lotsizekey IS NOT INITIAL.
            ls_marcx-lotsizekey = abap_true.
          ENDIF.

          IF ls_marc-proc_type IS NOT INITIAL.
            ls_marcx-proc_type = abap_true.
          ENDIF.

          IF ls_marc-iss_st_loc IS NOT INITIAL.
            ls_marcx-iss_st_loc = abap_true.
          ENDIF.

          IF ls_marc-inhseprodt IS NOT INITIAL.
            ls_marcx-inhseprodt = abap_true.
          ENDIF.

          IF ls_marc-period_ind IS NOT INITIAL.
            ls_marcx-period_ind = abap_true.
          ENDIF.

          IF ls_marc-plan_strgp IS  NOT  INITIAL.
            ls_marcx-plan_strgp = abap_true.
          ENDIF.

          IF ls_marc-consummode IS NOT INITIAL.
            ls_marcx-consummode = abap_true.
          ENDIF.

          IF ls_marc-fwd_cons IS NOT INITIAL.
            ls_marcx-fwd_cons = abap_true.
          ENDIF.

          IF ls_marc-bwd_cons IS NOT INITIAL.
            ls_marcx-bwd_cons = abap_true.
          ENDIF.

          IF ls_marc-replentime IS  NOT INITIAL.
            ls_marcx-replentime = abap_true.
          ENDIF.

          IF  ls_marc-production_scheduler IS NOT INITIAL.
            ls_marcx-production_scheduler = abap_true.
          ENDIF.

          IF ls_marc-prodprof IS NOT INITIAL.
            ls_marcx-prodprof = abap_true.
          ENDIF.

          IF ls_marc-variance_key IS NOT INITIAL.
            ls_marcx-variance_key = abap_true.
          ENDIF.

          IF  ls_marc-lot_size IS NOT INITIAL.
            ls_marcx-lot_size = abap_true.
          ENDIF.

          IF  ls_marc-pur_group IS NOT INITIAL.
            ls_marcx-pur_group = abap_true.
          ENDIF.

          IF ls_marc-backflush IS NOT INITIAL.
            ls_marcx-backflush = abap_true.
          ENDIF.

          ls_marcx-material = ls_material-materialnumber.
          ls_marcx-material_long = ls_material-materialnumber.

          APPEND ls_marcx TO lt_marcx.

* Fill MARD structure
          ls_mard-stge_loc = ls_material-storagelocation.
          ls_mard-plant = ls_material-plant.
          ls_mard-material = ls_material-materialnumber.
          ls_mard-material_long = ls_material-materialnumber.
          APPEND ls_mard TO lt_mard.

* Fill MARDX structure
          ls_mardx-stge_loc = ls_material-storagelocation.
          ls_mardx-plant = ls_material-plant.
          ls_mardx-material = ls_material-materialnumber.
          ls_mardx-material_long = ls_material-materialnumber.
          APPEND ls_mardx TO lt_mardx.

* Fill MBEW structure
          ls_mbew-val_class = ls_material-valuationclass .
          ls_mbew-val_area = ls_material-plant .
          ls_mbew-ml_active = abap_true.
          ls_mbew-std_price = ls_material-standardprice .
          ls_mbew-price_unit = ls_material-priceunit.
          ls_mbew-price_ctrl = ls_material-pricecontrol.
          ls_mbew-commprice1 = ls_material-commercialprice1.
          ls_mbew-qty_struct = abap_true.
          ls_mbew-material = ls_material-materialnumber.
          ls_mbew-material_long  = ls_material-materialnumber.
          ls_mbew-moving_pr = ls_material-movingprice.
          APPEND ls_mbew TO lt_mbew.

* Fill MBEWX structure
          ls_mbewx-val_class = abap_true.
          ls_mbewx-val_area = ls_material-plant.
          ls_mbewx-ml_active = abap_true.
          ls_mbewx-price_unit = abap_true.
          ls_mbewx-price_ctrl = abap_true.
          ls_mbewx-std_price = abap_true.
          ls_mbewx-commprice1 = abap_true.
          ls_mbewx-qty_struct = abap_true.
          ls_mbewx-material = ls_material-materialnumber.
          ls_mbewx-material_long  = ls_material-materialnumber.
          ls_mbewx-moving_pr = abap_true.
          APPEND ls_mbewx TO lt_mbewx.

* Fill MVKE structure
          ls_mvke-sales_org = ls_material-salesorg.
          ls_mvke-distr_chan = ls_material-distchan.
          ls_mvke-delyg_plnt = ls_material-deliveringplant.
          ls_mvke-cash_disc = abap_true.
          ls_mvke-matl_stats = ls_material-materialstatisticsgroup .
          ls_mvke-acct_assgt = ls_material-accountassignmentgroup.
          ls_mvke-item_cat = ls_material-itemcategorygroup.
          ls_mvke-prod_hier = ls_material-prodhierarchy.
          ls_mvke-material = ls_material-materialnumber.
          ls_mvke-material_long  = ls_material-materialnumber.
          APPEND ls_mvke TO lt_mvke.

* Fill MVKEX structure
          IF  ls_mvke-sales_org IS NOT INITIAL.
            ls_mvkex-sales_org =  ls_material-salesorg.
          ENDIF.

          IF ls_mvke-distr_chan IS NOT INITIAL.
            ls_mvkex-distr_chan =  ls_material-distchan.
          ENDIF.

          ls_mvkex-delyg_plnt =  abap_true.
          ls_mvkex-cash_disc = abap_true.
          ls_mvkex-matl_stats =  abap_true.
          ls_mvkex-acct_assgt =  abap_true .
          ls_mvkex-item_cat =  abap_true.
          ls_mvkex-prod_hier = abap_true.
          ls_mvkex-material = ls_material-materialnumber.
          ls_mvkex-material_long  = ls_material-materialnumber.
          APPEND ls_mvkex TO lt_mvkex.

* Fill MARA structure
          CALL FUNCTION 'CONVERSION_EXIT_CUNIT_INPUT'
            EXPORTING
              input          = ls_material-baseunitofmeasurement
              language       = sy-langu
            IMPORTING
              output         = ls_mara-base_uom
            EXCEPTIONS
              unit_not_found = 1
              OTHERS         = 2.

          IF ls_mara-base_uom IS NOT INITIAL.
            CALL FUNCTION 'UNIT_OF_MEASURE_SAP_TO_ISO'
              EXPORTING
                sap_code = ls_mara-base_uom
              IMPORTING
                iso_code = ls_mara-base_uom_iso.
*         EXCEPTIONS
*           NOT_FOUND         = 1
*           NO_ISO_CODE       = 2
*           OTHERS            = 3
            .
          ENDIF.

*        ls_mara-base_uom_iso = 'HUR'.
          ls_mara-material = ls_material-materialnumber.
          ls_mara-material_long = ls_material-materialnumber.
          ls_mara-matl_group = ls_material-materialgroup.
          ls_mara-item_cat = ls_material-generalitemcategorygroup.
          ls_mara-net_weight = ls_material-netweight.
          ls_mara-unit_of_wt = ls_material-unitofweight.
          ls_mara-trans_grp = ls_material-transportationgroup.
          ls_mara-period_ind_expiration_date = ls_material-periodindicatorforshelflige.
          APPEND ls_mara TO lt_mara.

* Fill MARAX structure
          IF ls_mara-base_uom IS NOT INITIAL.
            ls_marax-base_uom = abap_true.
          ENDIF.

          IF ls_mara-material IS NOT INITIAL.
            ls_marax-material = ls_mara-material.
          ENDIF.

          IF ls_mara-material_long IS NOT INITIAL.
            ls_marax-material_long = ls_material-materialnumber.
          ENDIF.
          IF ls_mara-base_uom_iso IS NOT INITIAL.
            ls_marax-base_uom_iso = abap_true.
          ENDIF.
          IF ls_mara-matl_group IS NOT INITIAL.
            ls_marax-matl_group = abap_true.
          ENDIF.

          IF ls_mara-item_cat IS   NOT INITIAL.
            ls_marax-item_cat = abap_true.
          ENDIF.

          IF ls_mara-net_weight IS NOT INITIAL.
            ls_marax-net_weight = abap_true.
          ENDIF.

          IF ls_mara-unit_of_wt IS NOT INITIAL.
            ls_marax-unit_of_wt = abap_true.
          ENDIF.

          IF ls_mara-trans_grp IS NOT INITIAL.
            ls_marax-trans_grp = abap_true.
          ENDIF.

          IF ls_mara-period_ind_expiration_date IS NOT INITIAL.
            ls_marax-period_ind_expiration_date = abap_true.
          ENDIF.
          APPEND ls_marax TO lt_marax.

* Fill MAKT table
          lv_iso_langu = sy-langu.
          ls_makt-langu = cl_srt_wsp_helper_methods=>convert_iso_lang_to_sap_lang( iso_lang_code =  lv_iso_langu ).
          ls_makt-langu_iso = sy-langu.
          ls_makt-matl_desc =  ls_material-description.
          ls_makt-material = ls_material-materialnumber.
          ls_makt-material_long = ls_material-materialnumber.
          APPEND ls_makt TO lt_makt.

* Fill MARM table
          ls_marm-material = ls_material-materialnumber.
          ls_marm-material_long = ls_material-materialnumber.
          ls_marm-alt_unit = ls_mara-base_uom.
          IF ls_mara-base_uom IS NOT INITIAL.
            CALL FUNCTION 'UNIT_OF_MEASURE_SAP_TO_ISO'
              EXPORTING
                sap_code = ls_mara-base_uom
              IMPORTING
                iso_code = ls_marm-alt_unit_iso.
*         EXCEPTIONS
*           NOT_FOUND         = 1
*           NO_ISO_CODE       = 2
*           OTHERS            = 3
            .
          ENDIF.

*        ls_marm-alt_unit_iso = ls_mara-base_uom.
          ls_marm-numerator =  1.
          ls_marm-denominatr = 1.
          ls_marm-gross_wt = ls_material-grossweight.
          ls_marm-volume = ls_material-volume.
          ls_marm-material = ls_material-materialnumber.
          APPEND ls_marm TO lt_marm.

          ls_marmx-alt_unit = abap_true.
          ls_marmx-alt_unit_iso = abap_true.
          ls_marm-numerator =  1.
          ls_marmx-denominatr = 1.
          ls_marmx-gross_wt = abap_true.
          ls_marmx-volume = abap_true.
          APPEND ls_marmx TO lt_marmx.

          ls_mlan-material = ls_material-materialnumber.
          ls_mlan-material_long = ls_material-materialnumber.
          ls_mlan-taxclass_1 = ls_material-taxclassification.
          ls_mlan-depcountry = ls_material-depcountry.
          ls_mlan-tax_type_1 = ls_material-taxtype.
          APPEND ls_mlan TO lt_mlan.

          CALL FUNCTION 'BAPI_MATERIAL_SAVEREPLICA'
            EXPORTING
              noappllog            = abap_true
              nochangedoc          = abap_true
              testrun              = abap_true
              inpfldcheck          = ''
            IMPORTING
              return               = ls_return
            TABLES
              headdata             = lt_headdata
              clientdata           = lt_mara
              clientdatax          = lt_marax
              plantdata            = lt_marc
              plantdatax           = lt_marcx
              forecastparameters   = lt_mpop
              forecastparametersx  = lt_mpopx
              planningdata         = lt_mpgd
              planningdatax        = lt_mpgdx
              storagelocationdata  = lt_mard
              storagelocationdatax = lt_mardx
              valuationdata        = lt_mbew
              valuationdatax       = lt_mbewx
              warehousenumberdata  = lt_mlgn
              warehousenumberdatax = lt_mlgnx
              salesdata            = lt_mvke
              salesdatax           = lt_mvkex
              storagetypedata      = lt_mlgt
              storagetypedatax     = lt_mlgtx
              materialdescription  = lt_makt
              unitsofmeasure       = lt_marm
              unitsofmeasurex      = lt_marmx
              taxclassifications   = lt_mlan
              returnmessages       = lt_return.

          IF ls_return-type = cl_esh_adm_constants=>gc_msgty_e OR ls_return-type =  cl_esh_adm_constants=>gc_msgty_a .
            ev_error = abap_true.

            ls_message-type = ls_return-type.
            ls_message-id = z_cl_dataload=>gc_message_class.
            ls_message-number = '030'.

            CONCATENATE gc_material ls_material-materialnumber INTO ls_message-message_v1 SEPARATED BY space.
            IF strlen( ls_return-message ) > 50.
              ls_message-message_v2 = ls_return-message+0(50).
              ls_message-message_v3 = ls_return-message+50(50).
              ls_message-message_v4 = ls_return-message+100(50).
            ELSE.
              ls_message-message_v2 = ls_return-message.
            ENDIF.

            zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
          ENDIF.


        ENDIF.



      ENDIF.

    ENDLOOP.

* Check if al least one material needs to be created
    IF lv_check = abap_true.
      IF ev_error = abap_false.


        LOOP AT it_material INTO ls_material WHERE materialnumber IS NOT INITIAL.

          CLEAR: ls_headdata1, ls_makt1,ls_mara1,ls_marax1,ls_marc1, ls_marcx1,ls_mard1, ls_mardx1,ls_marm1, ls_marmx1,ls_mbew1 , ls_mbewx1,
                 ls_mlgn1, ls_mlgnx1, ls_mlgt1 , ls_mlgtx1, ls_mpgd1 , ls_mpgdx1, ls_mpop1 , ls_mpopx1, ls_mvke1, ls_mvkex1, lt_marm1,lt_marmx1, lt_makt1, ls_return1,
                 lv_material_check.

* Fill HEADDATA structure
          ls_headdata1-material = ls_material-materialnumber.
          ls_headdata1-matl_type = ls_material-materialtype.
          ls_headdata1-material_long = ls_material-materialnumber .
          ls_headdata1-ind_sector = 'M'.
          ls_headdata1-basic_view = abap_true.
          ls_headdata1-sales_view = abap_true.
          ls_headdata1-purchase_view = abap_true.
          ls_headdata1-mrp_view = abap_true.
          ls_headdata1-forecast_view = abap_true.
          ls_headdata1-work_sched_view = abap_true.
          ls_headdata1-prt_view = abap_true.
          ls_headdata1-storage_view = abap_true.
          ls_headdata1-warehouse_view = abap_true.
          ls_headdata1-quality_view = abap_true.
          ls_headdata1-account_view = abap_true.
          ls_headdata1-cost_view = abap_true.

          IF ls_material-materialtype = 'ROH' OR ls_material-materialtype = 'SERV'.
            ls_headdata1-sales_view = abap_false.
          ENDIF.
*        APPEND ls_headdata TO lt_headdata.

* Fill MARC structure
          ls_marc1-plant = ls_material-plant .
          ls_marc1-availcheck = ls_material-availabilitycheck.
          ls_marc1-loadinggrp = ls_material-loadinggroup.
          ls_marc1-profit_ctr = ls_material-profitcenter.
          ls_marc1-mrp_type = ls_material-mrptype .
          ls_marc1-mrp_ctrler = ls_material-mrpcontroller .
          ls_marc1-lotsizekey = ls_material-lotsize.
          ls_marc1-proc_type = ls_material-procurementtype.
          ls_marc1-iss_st_loc = ls_material-prodstoragelocation.
          ls_marc1-inhseprodt = ls_material-inhouseproduction.
          ls_marc1-period_ind = ls_material-periodindicator.
          ls_marc1-plan_strgp = ls_material-strategygroup .
          ls_marc1-consummode = ls_material-consumptionmode.
          ls_marc1-fwd_cons = ls_material-forwardconsumptionperiod.
          ls_marc1-bwd_cons = ls_material-backwardconsumptionperiod.
          ls_marc1-replentime = ls_material-totalreplenishment.
          ls_marc1-production_scheduler = ls_material-productionsupervisor.
          ls_marc1-prodprof = ls_material-productionschedulingprofile.
          ls_marc1-variance_key = ls_material-variancekey .
          ls_marc1-lot_size = ls_material-costinglotsize.
          ls_marc1-pur_group = ls_material-purchasinggroup.
          ls_marc1-backflush = ls_material-backflush.

* Fill MARCX structure
          ls_marcx1-plant = ls_material-plant.
          IF ls_marc1-availcheck IS NOT INITIAL.
            ls_marcx1-availcheck = abap_true.
          ENDIF.

          IF ls_marc1-loadinggrp IS NOT INITIAL.
            ls_marcx1-loadinggrp = abap_true.
          ENDIF.

          IF ls_marc1-profit_ctr IS NOT INITIAL.
            ls_marcx1-profit_ctr = abap_true.
          ENDIF.

          IF ls_marc1-mrp_type IS NOT  INITIAL.
            ls_marcx1-mrp_type = abap_true.
          ENDIF.

          IF ls_marc1-mrp_ctrler IS NOT INITIAL.
            ls_marcx1-mrp_ctrler = abap_true.
          ENDIF.

          IF ls_marc1-lotsizekey IS NOT INITIAL.
            ls_marcx1-lotsizekey = abap_true.
          ENDIF.

          IF ls_marc1-proc_type IS NOT INITIAL.
            ls_marcx1-proc_type = abap_true.
          ENDIF.

          IF ls_marc1-inhseprodt IS NOT INITIAL.
            ls_marcx1-inhseprodt = abap_true.
          ENDIF.

          IF ls_marc1-iss_st_loc IS NOT INITIAL.
            ls_marcx1-iss_st_loc = abap_true.
          ENDIF.

          IF ls_marc1-period_ind IS NOT INITIAL.
            ls_marcx1-period_ind = abap_true.
          ENDIF.

          IF ls_marc1-plan_strgp IS  NOT  INITIAL.
            ls_marcx1-plan_strgp = abap_true.
          ENDIF.

          IF ls_marc1-consummode IS NOT INITIAL.
            ls_marcx1-consummode = abap_true.
          ENDIF.

          IF ls_marc1-fwd_cons IS NOT INITIAL.
            ls_marcx1-fwd_cons = abap_true.
          ENDIF.

          IF ls_marc1-bwd_cons IS NOT INITIAL.
            ls_marcx1-bwd_cons = abap_true.
          ENDIF.

          IF ls_marc1-replentime IS  NOT INITIAL.
            ls_marcx1-replentime = abap_true.
          ENDIF.

          IF  ls_marc1-production_scheduler IS NOT INITIAL.
            ls_marcx1-production_scheduler = abap_true.
          ENDIF.

          IF ls_marc1-prodprof IS NOT INITIAL.
            ls_marcx1-prodprof = abap_true.
          ENDIF.

          IF ls_marc1-variance_key IS NOT INITIAL.
            ls_marcx1-variance_key = abap_true.
          ENDIF.

          IF  ls_marc1-lot_size IS NOT INITIAL.
            ls_marcx1-lot_size = abap_true.
          ENDIF.

          IF  ls_marc1-pur_group IS NOT INITIAL.
            ls_marcx1-pur_group = abap_true.
          ENDIF.

          IF ls_marc1-backflush IS NOT INITIAL.
            ls_marcx1-backflush = abap_true.
          ENDIF.

* Fill MARD structure
          ls_mard1-stge_loc = ls_material-storagelocation.
          ls_mard1-plant = ls_material-plant.

* Fill MARDX structure
          ls_mardx1-stge_loc = ls_material-storagelocation.
          ls_mardx1-plant = ls_material-plant.

* Fill MBEW structure
          ls_mbew1-val_class = ls_material-valuationclass .
          ls_mbew1-val_area = ls_material-plant .
          ls_mbew1-ml_active = abap_true.
          ls_mbew1-std_price = ls_material-standardprice .
          ls_mbew1-price_unit = ls_material-priceunit.
          ls_mbew1-price_ctrl = ls_material-pricecontrol.
          ls_mbew1-commprice1 = ls_material-commercialprice1.
          ls_mbew1-qty_struct = abap_true.
          ls_mbew1-moving_pr = ls_material-movingprice.

* Fill MBEWX structure
          ls_mbewx1-val_class = abap_true.
          ls_mbewx1-val_area = ls_material-plant.
          ls_mbewx1-ml_active = abap_true.
          ls_mbewx1-price_unit = abap_true.
          ls_mbewx1-price_ctrl = abap_true.
          ls_mbewx1-std_price = abap_true.
          ls_mbewx1-commprice1 = abap_true.
          ls_mbewx1-qty_struct = abap_true.
          ls_mbewx1-moving_pr = abap_true.

* Fill MVKE structure
          ls_mvke1-sales_org = ls_material-salesorg.
          ls_mvke1-distr_chan = ls_material-distchan.
          ls_mvke1-delyg_plnt = ls_material-deliveringplant.
          ls_mvke1-cash_disc = abap_true.
          ls_mvke1-matl_stats = ls_material-materialstatisticsgroup .
          ls_mvke1-acct_assgt = ls_material-accountassignmentgroup.
          ls_mvke1-item_cat = ls_material-itemcategorygroup.
          ls_mvke1-prod_hier = ls_material-prodhierarchy.

* Fill MVKEX structure
          IF  ls_mvke1-sales_org IS NOT INITIAL.
            ls_mvkex1-sales_org =  ls_material-salesorg.
          ENDIF.

          IF ls_mvke1-distr_chan IS NOT INITIAL.
            ls_mvkex1-distr_chan =  ls_material-distchan.
          ENDIF.

          ls_mvkex1-delyg_plnt =  abap_true.
          ls_mvkex1-cash_disc = abap_true.
          ls_mvkex1-matl_stats =  abap_true.
          ls_mvkex1-acct_assgt =  abap_true .
          ls_mvkex1-item_cat =  abap_true.
          ls_mvkex1-prod_hier = abap_true.

* Fill MARA structure
          CALL FUNCTION 'CONVERSION_EXIT_CUNIT_INPUT'
            EXPORTING
              input          = ls_material-baseunitofmeasurement
              language       = sy-langu
            IMPORTING
              output         = ls_mara1-base_uom
            EXCEPTIONS
              unit_not_found = 1
              OTHERS         = 2.

          IF ls_mara1-base_uom IS NOT INITIAL.
            CALL FUNCTION 'UNIT_OF_MEASURE_SAP_TO_ISO'
              EXPORTING
                sap_code = ls_mara1-base_uom
              IMPORTING
                iso_code = ls_mara1-base_uom_iso.
*         EXCEPTIONS
*           NOT_FOUND         = 1
*           NO_ISO_CODE       = 2
*           OTHERS            = 3
            .
          ENDIF.

*          ls_mara1-base_uom_iso = 'HUR'.
          ls_mara1-matl_group = ls_material-materialgroup.
          ls_mara1-item_cat = ls_material-generalitemcategorygroup.
          ls_mara1-net_weight = ls_material-netweight.
          ls_mara1-unit_of_wt = ls_material-unitofweight.
          ls_mara1-trans_grp = ls_material-transportationgroup.
          ls_mara1-period_ind_expiration_date = ls_material-periodindicatorforshelflige.

* Fill MARAX structure
          IF ls_mara1-base_uom IS NOT INITIAL.
            ls_marax1-base_uom = abap_true.
          ENDIF.

          IF ls_mara1-base_uom_iso IS NOT INITIAL.
            ls_marax1-base_uom_iso = abap_true.
          ENDIF.

          IF ls_mara1-matl_group IS NOT INITIAL.
            ls_marax1-matl_group = abap_true.
          ENDIF.

          IF ls_mara1-item_cat IS   NOT INITIAL.
            ls_marax1-item_cat = abap_true.
          ENDIF.

          IF ls_mara1-net_weight IS NOT INITIAL.
            ls_marax1-net_weight = abap_true.
          ENDIF.

          IF ls_mara1-unit_of_wt IS NOT INITIAL.
            ls_marax1-unit_of_wt = abap_true.
          ENDIF.

          IF ls_mara1-trans_grp IS NOT INITIAL.
            ls_marax1-trans_grp = abap_true.
          ENDIF.

          IF ls_mara1-period_ind_expiration_date IS NOT INITIAL.
            ls_marax1-period_ind_expiration_date = abap_true.
          ENDIF.

* Fill MAKT table
          lv_iso_langu = sy-langu.
          ls_makt1-langu = cl_srt_wsp_helper_methods=>convert_iso_lang_to_sap_lang( iso_lang_code =  lv_iso_langu ).
          ls_makt1-langu_iso = sy-langu.
          ls_makt1-matl_desc =  ls_material-description.
          APPEND ls_makt1 TO lt_makt1.

* Fill MARM table
          ls_marm1-alt_unit = ls_mara1-base_uom.
*          ls_marm1-alt_unit_iso = ls_mara-base_uom.
          IF ls_mara-base_uom IS NOT INITIAL.
            CALL FUNCTION 'UNIT_OF_MEASURE_SAP_TO_ISO'
              EXPORTING
                sap_code = ls_mara1-base_uom
              IMPORTING
                iso_code = ls_marm1-alt_unit_iso.
          ENDIF.

          ls_marm1-numerator =  1.
          ls_marm1-denominatr = 1.
          ls_marm1-gross_wt = ls_material-grossweight.
          ls_marm1-unit_of_wt = ls_material-unitofweight.
          ls_marm1-volume = ls_material-volume.

          IF ls_material-unitofweight IS NOT INITIAL.
            CALL FUNCTION 'UNIT_OF_MEASURE_SAP_TO_ISO'
              EXPORTING
                sap_code = ls_material-unitofweight
              IMPORTING
                iso_code = ls_marm1-unit_of_wt_iso.
          ENDIF.

          APPEND ls_marm1 TO lt_marm1.

          IF ls_marm1-alt_unit IS NOT INITIAL.
            ls_marmx1-alt_unit = ls_marm1-alt_unit.
          ENDIF.

          IF ls_marm1-alt_unit_iso IS NOT INITIAL.
            ls_marmx1-alt_unit_iso = ls_marm1-alt_unit_iso.
          ENDIF.

          ls_marmx1-numerator =  1.
          ls_marmx1-denominatr = 1.

          IF ls_marm1-gross_wt IS NOT INITIAL.
            ls_marmx1-gross_wt = abap_true.
          ENDIF.

          IF ls_marm1-unit_of_wt IS NOT INITIAL.
            ls_marmx1-unit_of_wt = abap_true.
          ENDIF.

          IF ls_marm1-unit_of_wt_iso IS NOT INITIAL.
            ls_marmx1-unit_of_wt_iso = abap_true.
          ENDIF.

          ls_marmx1-volume = abap_true.
          APPEND ls_marmx1 TO lt_marmx1.


          ls_mlan1-taxclass_1 = ls_material-taxclassification.
          ls_mlan1-tax_type_1 = ls_material-taxtype.
          ls_mlan1-depcountry = ls_material-depcountry.
          APPEND ls_mlan1 TO lt_mlan1.


          CALL FUNCTION 'BAPI_MATERIAL_SAVEDATA'
            EXPORTING
              headdata             = ls_headdata1
              clientdata           = ls_mara1
              clientdatax          = ls_marax1
              plantdata            = ls_marc1
              plantdatax           = ls_marcx1
              forecastparameters   = ls_mpop1
              forecastparametersx  = ls_mpopx1
              planningdata         = ls_mpgd1
              planningdatax        = ls_mpgdx1
              storagelocationdata  = ls_mard1
              storagelocationdatax = ls_mardx1
              valuationdata        = ls_mbew1
              valuationdatax       = ls_mbewx1
              warehousenumberdata  = ls_mlgn1
              warehousenumberdatax = ls_mlgnx1
              salesdata            = ls_mvke1
              salesdatax           = ls_mvkex1
              storagetypedata      = ls_mlgt1
              storagetypedatax     = ls_mlgtx1
            IMPORTING
              return               = ls_return1
            TABLES
              materialdescription  = lt_makt1
              unitsofmeasure       = lt_marm1
              unitsofmeasurex      = lt_marmx1
              taxclassifications   = lt_mlan1.


          IF ls_return1-type = cl_esh_adm_constants=>gc_msgty_e OR ls_return1-type = cl_esh_adm_constants=>gc_msgty_a.

            ev_error = abap_true.

            ls_message-type = ls_return1-type.
            ls_message-id = z_cl_dataload=>gc_message_class.
            ls_message-number = '030'.

            CONCATENATE gc_material ls_material-materialnumber INTO ls_message-message_v1 SEPARATED BY space.
            IF strlen( ls_return1-message ) > 50.
              ls_message-message_v2 = ls_return1-message+0(50).
              ls_message-message_v3 = ls_return1-message+50(50).
              ls_message-message_v4 = ls_return1-message+100(50).
            ELSE.
              ls_message-message_v2 = ls_return1-message.
            ENDIF.

            zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
          ENDIF.

        ENDLOOP.


        ls_message-id = gc_message_class.
        ls_message-number = '010'.
        ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
        ls_message-message_v1 = gc_material.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

      ENDIF.
    ENDIF.



  ENDMETHOD.


  METHOD call_bapi_production_version.

    DATA: lt_mkal_i     TYPE TABLE OF mkal,
          ls_mkal_i     TYPE          mkal,
          ls_prod_vers  TYPE          ty_s_prod_vers,
          lt_prod_vers  TYPE TABLE OF ty_s_prod_vers,
          lt_prod_vers2 TYPE TABLE OF ty_s_prod_vers,
          lt_mkal_aend  TYPE TABLE OF mkal_aend,
          ls_mkal_aend  TYPE          mkal_aend,
          lt_mkal_u     TYPE TABLE OF mkal,
          lt_mkal_d     TYPE TABLE OF mkal,
          lv_verid      TYPE          verid,
          lt_mapl       TYPE TABLE OF mapl,
          ls_mapl       TYPE          mapl,
          ltr_matnr     TYPE RANGE OF matnr,
          ls_matnr      LIKE LINE OF  ltr_matnr,
          ls_message    TYPE          bapiret2.

    DATA: ls_mkal        TYPE  mkal,
          ls_mkal_aend_2 TYPE  mkal_aend,
          ls_return      TYPE  bapiret2.

    lt_prod_vers = it_production_version.
    lt_prod_vers2 = lt_prod_vers.

* Retrieve Routing Group Counter for Materials
    SELECT *  FROM mapl INTO TABLE lt_mapl FOR ALL ENTRIES IN lt_prod_vers
      WHERE matnr = lt_prod_vers-materialnumber
      AND   werks = lt_prod_vers-plant.

    TRY.
        LOOP AT it_production_version INTO ls_prod_vers WHERE materialnumber is NOT INITIAL.

          lv_verid = sy-tabix.
          CALL FUNCTION 'CONVERSION_EXIT_ALPHA_INPUT'
            EXPORTING
              input  = lv_verid
            IMPORTING
              output = lv_verid.

          READ TABLE lt_mapl INTO  ls_mapl WITH KEY matnr = ls_prod_vers-materialnumber.
          IF sy-subrc IS  INITIAL.
            ls_mkal_i-plnnr   = ls_mapl-plnnr .
          ENDIF.

          ls_mkal_i-mandt   = sy-mandt.
          ls_mkal_i-matnr   = ls_prod_vers-materialnumber.
          ls_mkal_i-werks   = ls_prod_vers-plant.
          ls_mkal_i-verid   = lv_verid.
          ls_mkal_i-stlal   = ls_prod_vers-alternativebom .
          ls_mkal_i-stlan   = ls_prod_vers-bomusage .
          ls_mkal_i-plnty   = ls_prod_vers-tasklisttype .
          ls_mkal_i-alnal   = ls_prod_vers-groupcounter .
          ls_mkal_i-beskz   = ls_prod_vers-procurementtype .
          ls_mkal_i-sobsl   = ls_prod_vers-specialprocurementtype.
          ls_mkal_i-losgr   = ls_prod_vers-lotsizeproductioncost .
          ls_mkal_i-mdv01   = ls_prod_vers-productionline.
          ls_mkal_i-mdv02   = ls_prod_vers-planningidentifictation  .
          ls_mkal_i-text1   = ls_prod_vers-prodversiondescription .
          ls_mkal_i-ewahr   = ls_prod_vers-usageprobability .
          ls_mkal_i-verto   = ls_prod_vers-distributionkeyforquantity .
          ls_mkal_i-serkz   = ls_prod_vers-repetitivemanufacturing .
          ls_mkal_i-bstmi   = ls_prod_vers-lotsizelowvalue .
          ls_mkal_i-bstma   = ls_prod_vers-lotsizeuppervalue .
          ls_mkal_i-rgekz   = ls_prod_vers-backflushforrsheader .
          ls_mkal_i-alort   = ls_prod_vers-receivingstoragelocation .
          ls_mkal_i-plnng   = ls_prod_vers-ratebasedplanning .
          ls_mkal_i-plnnm   = ls_prod_vers-roughcutplanning .
          ls_mkal_i-csplt   = ls_prod_vers-apportionmentstructure .
          ls_mkal_i-matko   = ls_prod_vers-othermaterialbom .
          ls_mkal_i-elpro   = ls_prod_vers-proposedstoragelocation .
          ls_mkal_i-prvbe   = ls_prod_vers-defaultsupplyareacomponents .
          ls_mkal_i-prfg_f  = ls_prod_vers-checkstatusproductionversion .
          ls_mkal_i-prdat   = ls_prod_vers-lastcheckproductionversion .
          ls_mkal_i-mksp    = ls_prod_vers-productionversionislocked.
          ls_mkal_i-prfg_r  = ls_prod_vers-ratebasedplanningcheckstatus .
          ls_mkal_i-prfg_g  = ls_prod_vers-preliminaryplancheckstatus .
          ls_mkal_i-prfg_s  = ls_prod_vers-bomcheckstatusprodversion .
          ls_mkal_i-ucmat   = ls_prod_vers-referencematerial .
          ls_mkal_i-prdat   = sy-datum.



          CALL FUNCTION 'CONVERT_DATE_TO_INTERNAL'
            EXPORTING
              date_external            = mv_valid_to_date "ls_prod_vers-validto
            IMPORTING
              date_internal            = ls_mkal_i-bdatu
            EXCEPTIONS
              date_external_is_invalid = 1
              OTHERS                   = 2.

          CALL FUNCTION 'CONVERT_DATE_TO_INTERNAL'
            EXPORTING
              date_external            = mv_valid_from_date  "ls_prod_vers-validfrom
            IMPORTING
              date_internal            = ls_mkal_i-adatu
            EXCEPTIONS
              date_external_is_invalid = 1
              OTHERS                   = 2.


          ls_mkal_aend-mandt = sy-mandt.
          ls_mkal_aend-matnr = ls_prod_vers-materialnumber.
          ls_mkal_aend-werks = ls_prod_vers-plant.
          ls_mkal_aend-verid = lv_verid.
          ls_mkal_aend-zaehl = sy-tabix.
          ls_mkal_aend-vbkz  = 'I'.
          ls_mkal_aend-annam = sy-uname.
          ls_mkal_aend-aedat = sy-datum.



          CALL FUNCTION 'CM_FV_PROD_VERS_CHECK_SINGLE'
            EXPORTING
              is_mkal      = ls_mkal_i
              is_mkal_aend = ls_mkal_aend
            IMPORTING
              es_mkal      = ls_mkal
              es_mkal_aend = ls_mkal_aend_2
              es_return    = ls_return.

          APPEND ls_mkal  TO lt_mkal_i.
          APPEND ls_mkal_aend_2  TO lt_mkal_aend.


          CALL FUNCTION 'CM_FV_PROD_VERS_DB_UPDATE'
            TABLES
              it_mkal_i    = lt_mkal_i
              it_mkal_u    = lt_mkal_u
              it_mkal_d    = lt_mkal_d
              it_mkal_aend = lt_mkal_aend.

          CLEAR: ls_mkal, ls_mkal_aend, ls_mkal_aend_2, ls_mkal_i, lt_mkal_aend, lt_mkal_i .
        ENDLOOP.

* Update Version Indicator Flag ( it cannot be updated with BAPI_MATERIAL_SAVEDATA)
        SORT lt_prod_vers BY materialnumber ASCENDING.
        DELETE ADJACENT DUPLICATES FROM lt_prod_vers COMPARING materialnumber.

        LOOP AT lt_prod_vers INTO ls_prod_vers WHERE materialnumber IS NOT INITIAL .
          ls_matnr-low = ls_prod_vers-materialnumber.
          ls_matnr-sign = 'I'.
          ls_matnr-option = 'EQ'.

          APPEND ls_matnr TO ltr_matnr.
        ENDLOOP.


        UPDATE marc
    SET verkz = abap_true
    WHERE matnr IN ltr_matnr.

      CATCH cx_root.
        ls_message-id = gc_message_class.
        ls_message-number = '031'.
        ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
        ev_error = abap_true.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
    ENDTRY.

  ENDMETHOD.


  METHOD call_bapi_profit_center.

    DATA: lt_profit_center TYPE tt_profit_center,
          ls_profit_center TYPE ty_s_profit_center,
          ls_basic_data    TYPE bapi0015_4,
          ls_return        TYPE bapiret2,
          lt_company_code  TYPE TABLE OF bapi0015_7,
          ls_company_code  TYPE bapi0015_7,
          ls_profit_ctr    TYPE bapi0015id2,
          ls_langu         TYPE bapi0015_10,
          lv_profit_center TYPE prctr,
          ls_message       TYPE bapiret2,
          ls_db_return     TYPE bapiret2,
          lv_count         TYPE i,
          lv_index         TYPE i.

    lt_profit_center = it_profit_center.
    SORT lt_profit_center BY profitcenter.
    DESCRIBE TABLE lt_profit_center LINES lv_count.

    LOOP AT lt_profit_center INTO ls_profit_center WHERE profitcenter is NOT INITIAL.
      lv_index = sy-tabix.

      IF lv_profit_center = ls_profit_center-profitcenter.
        ls_company_code-comp_code = ls_profit_center-companycode.
        ls_company_code-assign_to_prctr = 'X'.
        APPEND ls_company_code TO lt_company_code.
      ELSE.

        IF lv_profit_center IS NOT INITIAL.
          CALL FUNCTION 'BAPI_PROFITCENTER_CREATE'
            EXPORTING
              profitcenterid = ls_profit_ctr
              validfrom      = ls_profit_center-validfrom
              validto        = ls_profit_center-validto
              basicdata      = ls_basic_data
*             ADDRESS        =
*             COMMUNICATION  =
*             INDICATORS     =
*             TESTRUN        =
              language       = ls_langu
            IMPORTING
              return         = ls_return
*             PROFITCENTER   =
*             CONTROLLINGAREA       =
            TABLES
              companycodes   = lt_company_code.

          IF ls_return IS NOT INITIAL.
            IF ls_return-type = cl_esh_adm_constants=>gc_msgty_a OR ls_return-type = cl_esh_adm_constants=>gc_msgty_e OR ls_return-type = cl_esh_adm_constants=>gc_msgty_x.
              ev_error = abap_true.
            ENDIF.

            ls_message-type = ls_return-type.
            ls_message-id = z_cl_dataload=>gc_message_class.
            ls_message-number = '030'.

            CONCATENATE gc_profit_center ls_profit_center-profitcenter INTO ls_message-message_v1 SEPARATED BY space.

            IF strlen( ls_return-message ) > 50.
              ls_message-message_v2 = ls_return-message+0(50).
              ls_message-message_v3 = ls_return-message+50(50).
              ls_message-message_v4 = ls_return-message+100(50).
            ELSE.
              ls_message-message_v2 = ls_return-message.
            ENDIF.

            zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
            CLEAR ls_message.
          ENDIF.

          CLEAR: ls_company_code, lt_company_code.
        ENDIF.

        ls_profit_ctr-profit_ctr = ls_profit_center-profitcenter.
        ls_profit_ctr-co_area = ls_profit_center-controllingarea.

        ls_basic_data-long_text = ls_profit_center-longtext.
        ls_basic_data-prctr_name = ls_profit_center-name.
        ls_basic_data-segment = ls_profit_center-segment.
        ls_basic_data-prctr_hier_grp = ls_profit_center-hierarchygroup.
        ls_basic_data-in_charge = ls_profit_center-incharge.

        ls_company_code-comp_code = ls_profit_center-companycode.
        ls_company_code-assign_to_prctr = 'X'.
        APPEND ls_company_code TO lt_company_code.

        ls_langu-langu = ls_profit_center-language.
      ENDIF.

      IF lv_index = lv_count.
        CALL FUNCTION 'BAPI_PROFITCENTER_CREATE'
          EXPORTING
            profitcenterid = ls_profit_ctr
            validfrom      = ls_profit_center-validfrom
            validto        = ls_profit_center-validto
            basicdata      = ls_basic_data
*           ADDRESS        =
*           COMMUNICATION  =
*           INDICATORS     =
*           TESTRUN        =
            language       = ls_langu
          IMPORTING
            return         = ls_return
*           PROFITCENTER   =
*           CONTROLLINGAREA       =
          TABLES
            companycodes   = lt_company_code.

        IF ls_return IS NOT INITIAL.
          IF ls_return-type = cl_esh_adm_constants=>gc_msgty_a OR ls_return-type = cl_esh_adm_constants=>gc_msgty_e OR ls_return-type = cl_esh_adm_constants=>gc_msgty_x.
            ev_error = abap_true.
          ENDIF.

          ls_message-type = ls_return-type.
          ls_message-id = z_cl_dataload=>gc_message_class.
          ls_message-number = '030'.

          CONCATENATE gc_profit_center ls_profit_center-profitcenter INTO ls_message-message_v1 SEPARATED BY space.

          IF strlen( ls_return-message ) > 50.
            ls_message-message_v2 = ls_return-message+0(50).
            ls_message-message_v3 = ls_return-message+50(50).
            ls_message-message_v4 = ls_return-message+100(50).
          ELSE.
            ls_message-message_v2 = ls_return-message.
          ENDIF.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
          CLEAR ls_message.
        ENDIF.
      ENDIF.

      lv_profit_center = ls_profit_center-profitcenter.
    ENDLOOP.

    IF ev_error = abap_false.
      CALL FUNCTION 'BAPI_TRANSACTION_COMMIT'
        IMPORTING
          return = ls_db_return.

      IF ls_db_return IS INITIAL.
        ls_message-id = gc_message_class.
        ls_message-number = '010'.
        ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
        ls_message-message_v1 = gc_profit_center.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
      ELSE.
        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_db_return ).
      ENDIF.
    ELSE.
      CALL FUNCTION 'BAPI_TRANSACTION_ROLLBACK'
        IMPORTING
          return = ls_db_return.    " Return Messages

      IF ls_db_return IS NOT INITIAL.
        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_db_return ).
      ENDIF.
    ENDIF.

  ENDMETHOD.


  METHOD call_bapi_profit_center_hier.

    DATA: lt_profit_center_hier TYPE tt_profit_center_hier,
          ls_profit_center_hier TYPE ty_s_profit_center_hier,
          ls_return             TYPE bapiret2,
          ls_return_parent      TYPE bapiret2,
          ls_return_c           TYPE bapiret2,
          ls_message            TYPE bapiret2,
          ls_db_return          TYPE bapiret2,
          lt_nodes              TYPE TABLE OF bapiset_hier,
          lt_nodes_c            TYPE TABLE OF bapiset_hier,
          lt_nodes_sort         TYPE TABLE OF bapiset_hier,
          ls_nodes              TYPE bapiset_hier,
          lt_hier               TYPE TABLE OF bapi1116_values,
          lt_hier_c             TYPE TABLE OF bapi1116_values,
          ls_hier               TYPE bapi1116_values,
          lv_valcount           TYPE bapiset_valcount,
          ls_hier_top           TYPE tka01,
          lv_check              TYPE boolean.

    lt_profit_center_hier = it_profit_center_hier.

    LOOP AT lt_profit_center_hier INTO ls_profit_center_hier.

*** Check profit center hierarchy existence
      CALL FUNCTION 'BAPI_PROFITCENTERGRP_GETDETAIL'
        EXPORTING
          controllingarea = ls_profit_center_hier-controllingarea
          groupname       = ls_profit_center_hier-groupname
*         LANGUAGE        =
        IMPORTING
          return          = ls_return_c
        TABLES
          hierarchynodes  = lt_nodes_c
          hierarchyvalues = lt_hier_c.

      IF lt_nodes_c IS INITIAL AND lt_hier_c IS INITIAL.

*** Check the highest node in the hierarchy
        IF ls_profit_center_hier-parentgroup = 'YBPH'.
          SELECT SINGLE * FROM tka01 INTO ls_hier_top
            WHERE kokrs  = ls_profit_center_hier-parentcontrollingarea.

          IF ls_hier_top IS NOT INITIAL.
            ls_profit_center_hier-parentgroup = ls_hier_top-phinr.
          ENDIF.
        ENDIF.

        CALL FUNCTION 'BAPI_PROFITCENTERGRP_GETDETAIL'
          EXPORTING
            controllingarea = ls_profit_center_hier-parentcontrollingarea
            groupname       = ls_profit_center_hier-parentgroup
*           LANGUAGE        =
          IMPORTING
            return          = ls_return_parent
          TABLES
            hierarchynodes  = lt_nodes
            hierarchyvalues = lt_hier.

        IF ls_return_parent IS INITIAL.
          lt_nodes_sort = lt_nodes.
          SORT lt_nodes_sort BY hierlevel valcount ASCENDING.
          CLEAR lv_valcount.
          LOOP AT lt_nodes_sort INTO ls_nodes. "WHERE valcount = 0.
            AT LAST.
              lv_valcount = ls_nodes-valcount.
            ENDAT.
          ENDLOOP.

          ls_nodes-descript = ls_profit_center_hier-description.
          ls_nodes-groupname = ls_profit_center_hier-groupname.
          ls_nodes-hierlevel = '1'.
          ls_nodes-valcount = '0'.
          APPEND ls_nodes TO lt_nodes.
*        SORT lt_nodes BY hierlevel valcount ASCENDING.

          CALL FUNCTION 'BAPI_PROFITCENTERGRP_CREATE'
            EXPORTING
              controllingareaimp = ls_profit_center_hier-controllingarea
*             TOPNODEONLY        = ' '
*             LANGUAGE           =
            IMPORTING
*             controllingarea    = ls_profit_center_hier-controllingarea
*             groupname          = ls_profit_center_hier-groupname
              return             = ls_return
            TABLES
              hierarchynodes     = lt_nodes
              hierarchyvalues    = lt_hier.

          IF ls_return IS NOT INITIAL.
            IF ls_return-type = cl_esh_adm_constants=>gc_msgty_a OR ls_return-type = cl_esh_adm_constants=>gc_msgty_e OR ls_return-type = cl_esh_adm_constants=>gc_msgty_x.
              ev_error = abap_true.
            ENDIF.

            ls_message-type = ls_return-type.
            ls_message-id = z_cl_dataload=>gc_message_class.
            ls_message-number = '030'.

            CONCATENATE gc_profit_hier ls_profit_center_hier-groupname INTO ls_message-message_v1 SEPARATED BY space.

            IF strlen( ls_return-message ) > 50.
              ls_message-message_v2 = ls_return-message+0(50).
              ls_message-message_v3 = ls_return-message+50(50).
              ls_message-message_v4 = ls_return-message+100(50).
            ELSE.
              ls_message-message_v2 = ls_return-message.
            ENDIF.

            zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
            CLEAR ls_message.
          ELSE.
            lv_check = abap_true.
          ENDIF.
        ELSE.
          IF ls_return_parent-type = cl_esh_adm_constants=>gc_msgty_a OR ls_return_parent-type = cl_esh_adm_constants=>gc_msgty_e OR ls_return_parent-type = cl_esh_adm_constants=>gc_msgty_x.
            ev_error = abap_true.
          ENDIF.

          ls_message-type = ls_return_parent-type.
          ls_message-id = z_cl_dataload=>gc_message_class.
          ls_message-number = '030'.

          CONCATENATE gc_profit_hier ls_profit_center_hier-parentgroup INTO ls_message-message_v1 SEPARATED BY space.

          IF strlen( ls_return_parent-message ) > 50.
            ls_message-message_v2 = ls_return_parent-message+0(50).
            ls_message-message_v3 = ls_return_parent-message+50(50).
            ls_message-message_v4 = ls_return_parent-message+100(50).
          ELSE.
            ls_message-message_v2 = ls_return_parent-message.
          ENDIF.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
          CLEAR ls_message.
        ENDIF.

      ELSE.
        ls_message-id = gc_message_class.
        ls_message-number = '045'.
        ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
        ls_message-message_v1 = ls_profit_center_hier-groupname.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
      ENDIF.

    ENDLOOP.

    IF ev_error = abap_false.
      CALL FUNCTION 'BAPI_TRANSACTION_COMMIT'
        IMPORTING
          return = ls_db_return.

      IF ls_db_return IS INITIAL.
        IF lv_check = abap_true.
          ls_message-id = gc_message_class.
          ls_message-number = '044'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
          ls_message-message_v1 = gc_profit_hier.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
        ENDIF.
      ELSE.
        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_db_return ).
      ENDIF.
    ELSE.
      CALL FUNCTION 'BAPI_TRANSACTION_ROLLBACK'
        IMPORTING
          return = ls_db_return.    " Return Messages

      IF ls_db_return IS NOT INITIAL.
        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_db_return ).
      ENDIF.
    ENDIF.

  ENDMETHOD.


METHOD call_bapi_routing.
*{   INSERT         EBSK900008                                        1
TYPES: begin of ty_mat,
  matnr type matnr,
  werks type werks,
  end of ty_mat.
*}   INSERT

  DATA: ls_routing                TYPE ty_s_routing,
        ls_routing2               TYPE ty_s_routing,
        lt_routing2               TYPE tt_routing,
        lv_group                  TYPE bapi1012_tsk_c-task_list_group, "#EC NEEDED
        lv_group_counter          TYPE bapi1012_tsk_c-group_counter, "#EC NEEDED
        lt_task                   TYPE TABLE OF bapi1012_tsk_c,
        ls_task                   TYPE  bapi1012_tsk_c,
        lt_material_task_alloc    TYPE TABLE OF bapi1012_mtk_c,
        ls_material_task_alloc    TYPE bapi1012_mtk_c,
        lt_operation              TYPE TABLE OF bapi1012_opr_c,
        ls_operation              TYPE bapi1012_opr_c,
        lt_component_alloc        TYPE TABLE OF bapi1012_com_c,
        ls_component_alloc        TYPE bapi1012_com_c,
        lt_return                 TYPE TABLE OF bapiret2,
        ls_return                 TYPE  bapiret2,
        lv_msg                    TYPE string,
        lv_flg_error              TYPE eseboole,
        lv_matnr_current          TYPE matnr,
        lv_plant_current          TYPE werks_d,
        lv_last_activity          TYPE vornr,
        lv_mast_stlnr             TYPE mast-stlnr,
        lv_activity_counter(8)    TYPE n,
        lv_item_counter(8)        TYPE n,
        lv_bom_nr                 TYPE mast-stlnr,
        ls_sequence               TYPE bapi1012_seq_c,
        lt_sequence               TYPE TABLE OF bapi1012_seq_c,
        lv_bom_alt                TYPE stalt,
        lv_activity               TYPE vornr,
        lv_operation_measure_unit TYPE vorme,
        lv_operation_id           TYPE oprid,
        lv_measure_unit           TYPE plnme,
        lv_index                  TYPE i,
        ls_message                TYPE bapiret2,
        lv_old_material           TYPE matnr,
        lv_deletion_flag          TYPE bapimatall-del_flag,
        ls_return1                TYPE bapireturn1,
        lv_material_check         TYPE bapimatall-material,
        lv_material               TYPE bapi1080_mbm_c-material,
        lv_plant                  TYPE bapi1080_mbm_c-plant,
        lv_bomusage               TYPE bapi1080_mbm_c-bom_usage,
        ls_db_return              TYPE bapiret2,
*{   REPLACE        EBSK900008                                        2
*\        lt_matnr                  TYPE TABLE OF matnr,
        lt_matnr                  TYPE TABLE of ty_mat,
*}   REPLACE
        lv_check                  TYPE boolean,
        lv_bapiflag               TYPE bapiflag,
        index                     TYPE string,
        lv_routing_usage          TYPE bapi1012_control_data-bom_usage,
        lt_stpo                   TYPE TABLE OF stpo,
        ls_stpo                   TYPE stpo,
        lv_bom_components         TYPE i,
        lv_counter                TYPE i,
        lv_item_id                TYPE itmid,
        lv_current_year           TYPE string.

  lt_routing2 = it_routing.

  lv_current_year = sy-datum+0(4).

*{   REPLACE        EBSK900008                                        3
*\  SELECT matnr INTO TABLE lt_matnr FROM mapl FOR ALL ENTRIES IN lt_routing2 WHERE matnr = lt_routing2-material AND loekz = abap_false .
  SELECT matnr werks INTO TABLE lt_matnr FROM mapl FOR ALL ENTRIES IN lt_routing2 WHERE matnr = lt_routing2-material AND loekz = abap_false .
*}   REPLACE

  LOOP AT it_routing INTO ls_routing WHERE material is NOT INITIAL.

    CLEAR: ls_task, lt_task, ls_material_task_alloc, lt_material_task_alloc, ls_operation, lt_operation,
           ls_sequence, lt_sequence, lv_bom_alt, lv_bom_nr, ls_component_alloc, lt_component_alloc, lt_return, ls_return, lv_material_check, lt_stpo, ls_stpo.

    IF sy-tabix = 1 OR ls_routing-material <> lv_old_material.
* Check if Routing exists
*{   REPLACE        EBSK900008                                        4
*\      READ TABLE lt_matnr WITH KEY table_line = ls_routing-material TRANSPORTING NO FIELDS.
      READ TABLE lt_matnr WITH KEY matnr = ls_routing-material
                                   werks = ls_routing-plant TRANSPORTING NO FIELDS.
*}   REPLACE

      IF  sy-subrc IS INITIAL.
        ls_message-number = '028'.
        ls_message-id = gc_message_class.
        ls_message-type = cl_esh_adm_constants=>gc_msgty_i.
        ls_message-message_v1 = ls_routing-material.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
        lv_old_material = ls_routing-material.
      ELSE.
* Check if BOM exists

        lv_material_check = ls_routing-material.
        lv_material = ls_routing-material.
        lv_plant = ls_routing-plant.
        lv_bomusage = ls_routing-usage.

        CALL FUNCTION 'BAPI_MAT_BOM_EXISTENCE_CHECK'
          EXPORTING
            material = lv_material_check
            plant    = lv_plant
            bomusage = lv_bomusage
          TABLES
            return   = lt_return.

        IF lt_return  IS NOT INITIAL.
          ls_message-id = gc_message_class.
          ls_message-number = '023'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
          ls_message-message_v1 = ls_routing-material.
          ev_error = abap_true.

          lv_old_material = ls_routing-material.
          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

        ELSE.

* Check if material is marked for deletion
          lv_material_check = ls_routing-material.

          CALL FUNCTION 'BAPI_MATERIAL_EXISTENCECHECK'
            EXPORTING
              material      = lv_material_check
            IMPORTING
              deletion_flag = lv_deletion_flag
              return        = ls_return1.

          IF lv_deletion_flag = abap_true.
            ls_message-id = gc_message_class.
            ls_message-number = '011'.
            ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
            ls_message-message_v1 = ls_routing-material.
            ev_error = abap_true.

            zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
          ELSEIF ls_return1-type <> cl_esh_adm_constants=>gc_msgty_s.
            ls_message-id = gc_message_class.
            ls_message-number = '027'.
            ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
            ls_message-message_v1 = ls_routing-material.
            ev_error = abap_true.

            zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
          ELSE.
            CALL FUNCTION 'CONVERSION_EXIT_CUNIT_INPUT'
              EXPORTING
                input          = ls_routing-unitofmeasure
                language       = sy-langu
              IMPORTING
                output         = lv_measure_unit
              EXCEPTIONS
                unit_not_found = 1
                OTHERS         = 2.

* Fill TASK table
            ls_task-plant = ls_routing-plant.
*            ls_task-valid_from = sy-datum.
            CONCATENATE lv_current_year '0101' INTO ls_task-valid_from .
            ls_task-task_list_status = ls_routing-status.
            ls_task-task_list_usage = ls_routing-usage.
            ls_task-task_measure_unit = lv_measure_unit.
            ls_task-lot_size_from = ls_routing-fromlotsize.
            ls_task-lot_size_to = ls_routing-tolotsize.
            ls_task-insppoint_partiallot_assgnmt = ls_routing-partiallotassignment.
            APPEND ls_task TO lt_task.

* Fill MATERIAL table
            ls_material_task_alloc-material = ls_routing-material.
            ls_material_task_alloc-material_long = ls_routing-material.
            ls_material_task_alloc-plant = ls_routing-plant.
*            ls_material_task_alloc-valid_from = sy-datum.
            CONCATENATE lv_current_year '0101' INTO ls_material_task_alloc-valid_from .
            APPEND ls_material_task_alloc TO lt_material_task_alloc.

            CLEAR: lv_index, lv_activity, lv_operation_id.
            LOOP AT lt_routing2 INTO ls_routing2 WHERE material = ls_routing-material AND plant = ls_routing-plant ."AND usage = ls_routing-usage AND status = ls_routing-status.
              lv_index = lv_index + 1.

              index = lv_index.
              lv_activity = index * 10.
              lv_operation_id  = index * 10.

              CALL FUNCTION 'CONVERSION_EXIT_ALPHA_INPUT'
                EXPORTING
                  input  = lv_activity
                IMPORTING
                  output = lv_activity.

              CALL FUNCTION 'CONVERSION_EXIT_ALPHA_INPUT'
                EXPORTING
                  input  = lv_operation_id
                IMPORTING
                  output = lv_operation_id.

              CALL FUNCTION 'CONVERSION_EXIT_CUNIT_INPUT'
                EXPORTING
                  input          = ls_routing2-unitofmeasureforactivity
                  language       = sy-langu
                IMPORTING
                  output         = lv_operation_measure_unit
                EXCEPTIONS
                  unit_not_found = 1
                  OTHERS         = 2.

* Fill OPERATION table
              ls_operation-nominator = 1.
              ls_operation-denominator = 1.
              ls_operation-activity =  lv_activity.
              ls_operation-operation_id = lv_operation_id.
              ls_operation-work_cntr = ls_routing2-workcenter.
              ls_operation-plant = ls_routing-plant.
              ls_operation-base_quantity = ls_routing2-basequantity.
              ls_operation-operation_measure_unit = lv_operation_measure_unit.
              ls_operation-control_key = ls_routing2-controlkey.
              ls_operation-description = ls_routing2-description.
              ls_operation-break_time = ls_routing2-break.
              ls_operation-std_unit_01 = ls_routing2-unitofmeasuresetup.
              ls_operation-std_value_01 = ls_routing2-setup.
              ls_operation-acttype_01 = ls_routing2-activitytypesetup.
              ls_operation-std_unit_02 = ls_routing2-unitofmeasuremachine.
              ls_operation-std_value_02 = ls_routing2-machine.
              ls_operation-acttype_02 = ls_routing2-activitytypemachine.
              ls_operation-std_unit_03 = ls_routing2-unitofmeasurelabor.
              ls_operation-std_value_03 = ls_routing2-labor.
              ls_operation-acttype_03 = ls_routing2-activitytypelabor.
              ls_operation-required_overlapping = ls_routing2-overlapping.
              ls_operation-cost_relevant = ls_routing2-costingrelevancy.
*              ls_operation-valid_from = sy-datum.
              CONCATENATE lv_current_year '0101' INTO ls_operation-valid_from .
              APPEND ls_operation TO lt_operation.

            ENDLOOP.

            SELECT SINGLE stlnr stlal FROM mast INTO (lv_bom_nr, lv_bom_alt) WHERE
                      matnr = ls_routing-material AND
                      werks = ls_routing-plant AND
                      stlan = ls_routing-usage.         "#EC CI_NOORDER

            SELECT * FROM stpo INTO TABLE lt_stpo WHERE stlnr = lv_bom_nr. "#EC CI_NOFIRST
            DESCRIBE TABLE lt_stpo LINES lv_bom_components.

            lv_counter = 0.
            DO lv_bom_components TIMES.
              lv_counter = lv_counter + 1.
              lv_item_id = lv_counter * 10.
              lv_operation_id = ls_routing-operationnumber.
              CALL FUNCTION 'CONVERSION_EXIT_ALPHA_INPUT'
                EXPORTING
                  input  = lv_operation_id
                IMPORTING
                  output = lv_operation_id.

              READ TABLE lt_stpo INTO ls_stpo INDEX lv_counter.
*              ls_component_alloc-valid_from = sy-datum.
              CONCATENATE lv_current_year '0101' INTO ls_component_alloc-valid_from .
              ls_component_alloc-operation_id = lv_operation_id.
              ls_component_alloc-plant = ls_routing-plant.
              ls_component_alloc-material = ls_stpo-idnrk.
              ls_component_alloc-material_long = ls_stpo-idnrk.
              ls_component_alloc-bom_type = gc_bom_type.
              ls_component_alloc-bom_no = lv_bom_nr.
              ls_component_alloc-alternative_bom = lv_bom_alt .
              ls_component_alloc-item_id = ls_stpo-stlkn.
              ls_component_alloc-item_no = ls_stpo-posnr.
              ls_component_alloc-activity = ls_routing-operationnumber.
              ls_component_alloc-bom_type_root = gc_bom_type.
              ls_component_alloc-backflush = ls_routing-backflush.
              ls_component_alloc-bom_no_root = lv_bom_nr.
              ls_component_alloc-sequence_no = '000000'.
              APPEND ls_component_alloc TO lt_component_alloc.
            ENDDO.


            lv_bapiflag = 'X'.
            lv_routing_usage = ls_routing-usage.
            CALL FUNCTION 'BAPI_ROUTING_CREATE'
              EXPORTING
                testrun                = lv_bapiflag
                profile                = '1'     " PI: 'PP01'
                bomusage               = lv_routing_usage
                application            = 'P'     " PI: space
              IMPORTING
                group                  = lv_group
                groupcounter           = lv_group_counter
              TABLES
                task                   = lt_task
                materialtaskallocation = lt_material_task_alloc
                operation              = lt_operation
                componentallocation    = lt_component_alloc
                return                 = lt_return.

            READ TABLE lt_return  WITH KEY type = cl_esh_adm_constants=>gc_msgty_e TRANSPORTING NO FIELDS.
            IF sy-subrc IS INITIAL.

              ev_error = abap_true.
              LOOP AT lt_return INTO ls_return WHERE message IS  NOT INITIAL.
                ls_message-type = ls_return-type.
                ls_message-id = z_cl_dataload=>gc_message_class.
                ls_message-number = '030'.

                CONCATENATE gc_routing ls_routing-material INTO ls_message-message_v1 SEPARATED BY space.

                IF strlen( ls_return-message ) > 50.
                  ls_message-message_v2 = ls_return-message+0(50).
                  ls_message-message_v3 = ls_return-message+50(50).
                  ls_message-message_v4 = ls_return-message+100(50).
                ELSE.
                  ls_message-message_v2 = ls_return-message.
                ENDIF.

                zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
              ENDLOOP.
            ELSE.
              READ TABLE lt_return  WITH KEY type = cl_esh_adm_constants=>gc_msgty_a TRANSPORTING NO FIELDS.
              IF sy-subrc IS INITIAL.

                ev_error = abap_true.
                LOOP AT lt_return INTO ls_return WHERE message IS  NOT INITIAL.
                  ls_message-type = ls_return-type.
                  ls_message-id = z_cl_dataload=>gc_message_class.
                  ls_message-number = '030'.

                  CONCATENATE gc_routing ls_routing-material INTO ls_message-message_v1 SEPARATED BY space.

                  IF strlen( ls_return-message ) > 50.
                    ls_message-message_v2 = ls_return-message+0(50).
                    ls_message-message_v3 = ls_return-message+50(50).
                    ls_message-message_v4 = ls_return-message+100(50).
                  ELSE.
                    ls_message-message_v2 = ls_return-message.
                  ENDIF.

                  zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
                ENDLOOP.

              ELSE.
                CALL FUNCTION 'BAPI_TRANSACTION_COMMIT'
                  IMPORTING
                    return = ls_db_return.    " Return Messages
              ENDIF.

            ENDIF.
            lv_old_material = ls_routing-material.
          ENDIF.

        ENDIF.
      ENDIF.
    ENDIF.
  ENDLOOP.

  IF ev_error = abap_false.

    CALL FUNCTION 'BAPI_TRANSACTION_ROLLBACK'
      IMPORTING
        return = ls_db_return.    " Return Messages


    LOOP AT it_routing INTO ls_routing WHERE material is NOT INITIAL.

      CLEAR: ls_task, lt_task, ls_material_task_alloc, lt_material_task_alloc, ls_operation, lt_operation,
             ls_sequence, lt_sequence, lv_bom_alt, lv_bom_nr, ls_component_alloc, lt_component_alloc, lt_return, ls_return, lv_material_check, lt_stpo, ls_stpo.

      IF sy-tabix = 1 OR ls_routing-material <> lv_old_material.
* Check if Routing exists
        READ TABLE lt_matnr WITH KEY table_line = ls_routing-material TRANSPORTING NO FIELDS.

        IF  sy-subrc IS INITIAL.
          lv_old_material = ls_routing-material.

        ELSE.
* Check if BOM exists

          lv_material_check = ls_routing-material.
          lv_material = ls_routing-material.
          lv_plant = ls_routing-plant.
          lv_bomusage = ls_routing-usage.

          CALL FUNCTION 'BAPI_MAT_BOM_EXISTENCE_CHECK'
            EXPORTING
              material = lv_material_check
              plant    = lv_plant
              bomusage = lv_bomusage
            TABLES
              return   = lt_return.

          IF lt_return  IS NOT INITIAL.

            ev_error = abap_true.
            lv_old_material = ls_routing-material.

          ELSE.

* Check if material is marked for deletion
            lv_material_check = ls_routing-material.

            CALL FUNCTION 'BAPI_MATERIAL_EXISTENCECHECK'
              EXPORTING
                material      = lv_material_check
              IMPORTING
                deletion_flag = lv_deletion_flag
                return        = ls_return1.

            IF lv_deletion_flag = abap_true.

              ev_error = abap_true.

            ELSEIF ls_return1-type <> cl_esh_adm_constants=>gc_msgty_s.

              ev_error = abap_true.

            ELSE.
              CALL FUNCTION 'CONVERSION_EXIT_CUNIT_INPUT'
                EXPORTING
                  input          = ls_routing-unitofmeasure
                  language       = sy-langu
                IMPORTING
                  output         = lv_measure_unit
                EXCEPTIONS
                  unit_not_found = 1
                  OTHERS         = 2.

* Fill TASK table

              ls_task-plant = ls_routing-plant.
*              ls_task-valid_from = '20160101'.
              CONCATENATE lv_current_year '0101' INTO ls_task-valid_from .
              ls_task-task_list_status = ls_routing-status.
              ls_task-task_list_usage = ls_routing-usage.
              ls_task-task_measure_unit = lv_measure_unit.
              ls_task-lot_size_from = ls_routing-fromlotsize.
              ls_task-lot_size_to = ls_routing-tolotsize.
              ls_task-insppoint_partiallot_assgnmt = ls_routing-partiallotassignment.
              APPEND ls_task TO lt_task.

* Fill MATERIAL table
              ls_material_task_alloc-material = ls_routing-material.
              ls_material_task_alloc-material_long = ls_routing-material.
              ls_material_task_alloc-plant = ls_routing-plant.
*              ls_material_task_alloc-valid_from = sy-datum.
              CONCATENATE lv_current_year '0101' INTO ls_material_task_alloc-valid_from .
              APPEND ls_material_task_alloc TO lt_material_task_alloc.

              CLEAR: lv_index, lv_activity, lv_operation_id.
              LOOP AT lt_routing2 INTO ls_routing2 WHERE material = ls_routing-material AND plant = ls_routing-plant ."AND usage = ls_routing-usage AND status = ls_routing-status.
                lv_index = lv_index + 1.

                index = lv_index.
                lv_activity = index * 10.
                lv_operation_id  = index * 10.

                CALL FUNCTION 'CONVERSION_EXIT_ALPHA_INPUT'
                  EXPORTING
                    input  = lv_activity
                  IMPORTING
                    output = lv_activity.

                CALL FUNCTION 'CONVERSION_EXIT_ALPHA_INPUT'
                  EXPORTING
                    input  = lv_operation_id
                  IMPORTING
                    output = lv_operation_id.

                CALL FUNCTION 'CONVERSION_EXIT_CUNIT_INPUT'
                  EXPORTING
                    input          = ls_routing2-unitofmeasureforactivity
                    language       = sy-langu
                  IMPORTING
                    output         = lv_operation_measure_unit
                  EXCEPTIONS
                    unit_not_found = 1
                    OTHERS         = 2.

* Fill OPERATION table
                ls_operation-nominator = 1.
                ls_operation-denominator = 1.
                ls_operation-activity =  lv_activity.
                ls_operation-operation_id = lv_operation_id.
                ls_operation-work_cntr = ls_routing2-workcenter.
                ls_operation-plant = ls_routing-plant.
                ls_operation-base_quantity = ls_routing2-basequantity.
                ls_operation-operation_measure_unit = lv_operation_measure_unit.
                ls_operation-control_key = ls_routing2-controlkey.
                ls_operation-description = ls_routing2-description.
                ls_operation-break_time = ls_routing2-break.
                ls_operation-std_unit_01 = ls_routing2-unitofmeasuresetup.
                ls_operation-std_value_01 = ls_routing2-setup.
                ls_operation-acttype_01 = ls_routing2-activitytypesetup.
                ls_operation-std_unit_02 = ls_routing2-unitofmeasuremachine.
                ls_operation-std_value_02 = ls_routing2-machine.
                ls_operation-acttype_02 = ls_routing2-activitytypemachine.
                ls_operation-std_unit_03 = ls_routing2-unitofmeasurelabor.
                ls_operation-std_value_03 = ls_routing2-labor.
                ls_operation-acttype_03 = ls_routing2-activitytypelabor.
                ls_operation-required_overlapping = ls_routing2-overlapping.
                ls_operation-cost_relevant = ls_routing2-costingrelevancy.
*                ls_operation-valid_from = sy-datum.
                CONCATENATE lv_current_year '0101' INTO ls_operation-valid_from .
                APPEND ls_operation TO lt_operation.

              ENDLOOP.


              SELECT SINGLE stlnr stlal FROM mast INTO (lv_bom_nr, lv_bom_alt) WHERE
                      matnr = ls_routing-material AND
                      werks = ls_routing-plant AND
                      stlan = ls_routing-usage.         "#EC CI_NOORDER

              SELECT * FROM stpo INTO TABLE lt_stpo WHERE stlnr = lv_bom_nr. "#EC CI_NOFIRST
              DESCRIBE TABLE lt_stpo LINES lv_bom_components.

              lv_counter = 0.
              DO lv_bom_components TIMES.
                lv_counter = lv_counter + 1.
                lv_item_id = lv_counter * 10.
                lv_operation_id = ls_routing-operationnumber .

                CALL FUNCTION 'CONVERSION_EXIT_ALPHA_INPUT'
                  EXPORTING
                    input  = lv_operation_id
                  IMPORTING
                    output = lv_operation_id.

                READ TABLE lt_stpo INTO ls_stpo INDEX lv_counter.
*                ls_component_alloc-valid_from = sy-datum.
                CONCATENATE lv_current_year '0101' INTO ls_component_alloc-valid_from .
                ls_component_alloc-operation_id = lv_operation_id.
                ls_component_alloc-plant = ls_routing-plant.
                ls_component_alloc-material = ls_stpo-idnrk.
                ls_component_alloc-material_long = ls_stpo-idnrk.
                ls_component_alloc-bom_type = gc_bom_type.
                ls_component_alloc-bom_no = lv_bom_nr.
                ls_component_alloc-alternative_bom = lv_bom_alt .
                ls_component_alloc-item_id = ls_stpo-stlkn.
                ls_component_alloc-item_no = ls_stpo-posnr.
                ls_component_alloc-activity = ls_routing-operationnumber.
                ls_component_alloc-bom_type_root = gc_bom_type.
                ls_component_alloc-backflush = ls_routing-backflush.
                ls_component_alloc-bom_no_root = lv_bom_nr.
                ls_component_alloc-sequence_no = '000000'.
                APPEND ls_component_alloc TO lt_component_alloc.
              ENDDO.

              CLEAR lv_bapiflag.
              lv_routing_usage = ls_routing-usage.
              CALL FUNCTION 'BAPI_ROUTING_CREATE'
                EXPORTING
                  testrun                = lv_bapiflag
                  profile                = '1'     " PI: 'PP01'
                  bomusage               = lv_routing_usage
                  application            = 'P'     " PI: space
                IMPORTING
                  group                  = lv_group
                  groupcounter           = lv_group_counter
                TABLES
                  task                   = lt_task
                  materialtaskallocation = lt_material_task_alloc
                  operation              = lt_operation
                  componentallocation    = lt_component_alloc
                  return                 = lt_return.

              READ TABLE lt_return  WITH KEY type = cl_esh_adm_constants=>gc_msgty_e TRANSPORTING NO FIELDS.
              IF sy-subrc IS INITIAL.

                ev_error = abap_true.
                LOOP AT lt_return INTO ls_return WHERE message IS  NOT INITIAL.
                  ls_message-type = ls_return-type.
                  ls_message-id = z_cl_dataload=>gc_message_class.
                  ls_message-number = '030'.

                  CONCATENATE gc_routing ls_routing-material INTO ls_message-message_v1 SEPARATED BY space.

                  IF strlen( ls_return-message ) > 50.
                    ls_message-message_v2 = ls_return-message+0(50).
                    ls_message-message_v3 = ls_return-message+50(50).
                    ls_message-message_v4 = ls_return-message+100(50).
                  ELSE.
                    ls_message-message_v2 = ls_return-message.
                  ENDIF.

                  zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
                ENDLOOP.
              ELSE.
                lv_check = abap_true.
                CALL FUNCTION 'BAPI_TRANSACTION_COMMIT'
                  IMPORTING
                    return = ls_db_return.    " Return Messages
              ENDIF.
              lv_old_material = ls_routing-material.



            ENDIF.

          ENDIF.
        ENDIF.
      ENDIF.
    ENDLOOP.

    IF lv_check = abap_true.
      ls_message-number = '010'.
      ls_message-id = gc_message_class.
      ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
      ls_message-message_v1 = gc_routing.

      zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

    ENDIF.

  ELSE.
    CALL FUNCTION 'BAPI_TRANSACTION_ROLLBACK'
      IMPORTING
        return = ls_db_return.    " Return Messages

    IF ls_db_return IS NOT INITIAL.
      zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_db_return ).
    ENDIF.
  ENDIF.

ENDMETHOD.


  METHOD call_bapi_sale_price.

    DATA ls_sale_price TYPE ty_s_sale_price.
    DATA:ls_komg TYPE komg.
    DATA lv_error TYPE boolean.
    DATA ls_komv TYPE komv.
    DATA lt_komv TYPE TABLE OF komv.
    DATA: komk TYPE komk,
          komp TYPE komp.
    DATA wa_pispr TYPE pispr.
    DATA lv_new_record.
    DATA ls_message TYPE bapiret2.
    DATA lx_root TYPE REF TO cx_root.
    DATA lv_message TYPE string.
    DATA lv_date_from TYPE kodatab.
    DATA lv_date_to TYPE kodatbi.
    DATA lv_date_on TYPE kodatbi.

    IF it_sale_price IS NOT INITIAL.
      LOOP AT it_sale_price INTO ls_sale_price.

        ls_komg-matnr = ls_sale_price-materialnumber.
        ls_komg-vkorg = ls_sale_price-salesorganization.
        ls_komg-vtweg = ls_sale_price-distributionchannel.

        CLEAR: lt_komv,ls_komv.
        ls_komv-kappl = 'V'.        " Application V = Sales
        ls_komv-kschl = 'PPR0'.    " Condition type
        ls_komv-kbetr = ls_sale_price-conditionamount.
        ls_komv-kmein = ls_sale_price-conditionunit.
        ls_komv-kpein = ls_sale_price-conditionpricingunit.
        ls_komv-waers = ls_sale_price-currency.
        ls_komv-mandt = sy-mandt.
        APPEND ls_komv TO lt_komv.

        wa_pispr-matnr = ls_sale_price-materialnumber.
        wa_pispr-vkorg = ls_sale_price-salesorganization.
        wa_pispr-vtweg = ls_sale_price-distributionchannel.

        CALL FUNCTION 'SPR_KOMK_KOMP_FILL'
          EXPORTING
            pi_i_spr  = wa_pispr
          IMPORTING
            pe_i_komk = komk
            pe_i_komp = komp.

        lv_date_from = ls_sale_price-validfrom.
        lv_date_to = ls_sale_price-validto.
        lv_date_on = ls_sale_price-validon.

        TRY.
            CALL FUNCTION 'RV_CONDITION_COPY'
              EXPORTING
                application              = 'V'
                condition_table          = '304'      " 3 character cond. table
                condition_type           = 'PPR0'   " cond. type
                date_from                = lv_date_from " valid on
                date_to                  = lv_date_to " valid to
                enqueue                  = 'X'        " lock entry
                i_komk                   = komk
                i_komp                   = komp
                key_fields               = ls_komg    " key fields
                maintain_mode            = 'B'        " A= create " B= change, " C= display " D= create
                no_authority_check       = 'X'
                selection_date           = lv_date_on " valid on
                keep_old_records         = ' '
                overlap_confirmed        = 'X'
                no_db_update             = space
              IMPORTING
                e_komk                   = komk
                e_komp                   = komp
                new_record               = lv_new_record
              TABLES
                copy_records             = lt_komv
              EXCEPTIONS
                enqueue_on_record        = 1
                invalid_application      = 2
                invalid_condition_number = 3
                invalid_condition_type   = 4
                no_selection             = 5
                table_not_valid          = 6
                no_authority_ekorg       = 7
                no_authority_kschl       = 8.

            IF sy-subrc = 0.
              CALL FUNCTION 'RV_CONDITION_SAVE'.
              COMMIT WORK.
              CALL FUNCTION 'RV_CONDITION_RESET'.
              "necessary to write data
              COMMIT WORK.
            ENDIF.

          CATCH cx_root INTO lx_root.
            ev_error = abap_true.
            lv_message = lx_root->get_text( ).

            ls_message-id = gc_message_class.
            ls_message-number = '030'.
            ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
            ls_message-message_v1 = gc_sale_price.

            IF strlen( lv_message ) > 50.
              ls_message-message_v2 = lv_message+0(50).
              ls_message-message_v3 = lv_message+50(50).
              ls_message-message_v4 = lv_message+100(50).
            ELSE.
              ls_message-message_v2 = lv_message.
            ENDIF.

            zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
        ENDTRY.
      ENDLOOP.

      IF ev_error = abap_false.
        ls_message-id = gc_message_class.
        ls_message-number = '010'.
        ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
        ls_message-message_v1 = gc_sale_price.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
      ENDIF.
    ENDIF.

  ENDMETHOD.


  METHOD call_bapi_vendor.


    DATA: ls_vendor          TYPE ty_s_vendor,
          ls_partner_categ   TYPE bapibus1006_head-partn_cat,
          ls_central_data    TYPE bapibus1006_central,
          ls_address         TYPE bapibus1006_address,
          ls_central_org     TYPE bapibus1006_central_organ,
          ls_central_person  TYPE bapibus1006_central_person,
          lv_busr_number     TYPE bu_partner,
          lt_return_0        TYPE TABLE OF bapiret2,
          ls_return_0        TYPE bapiret2,
          lt_return          TYPE TABLE OF bapiret2,
          ls_return          TYPE bapiret2,
          lt_bank_return     TYPE TABLE OF bapiret2,
          ls_bank_return     TYPE bapiret2,
          lt_check_existence TYPE TABLE OF bapiret2,
          lv_check           TYPE boolean.

    DATA: i_data                         TYPE cvis_ei_extern_t,
          lte_return                     TYPE bapiretm,
          lse_return                     LIKE LINE OF lte_return,
          wa_data                        LIKE LINE OF i_data,
          wa_partn                       TYPE bus_ei_extern,
          wa_partn_hdr                   TYPE bus_ei_header,
          wa_partn_hdr_object_instance   TYPE bus_ei_instance,
          wa_partn_ctr_data              TYPE bus_ei_central_data,
          wa_partn_ctr_data_common       TYPE bus_ei_bupa_central,
          wa_partn_ctr_data_role         TYPE bus_ei_bupa_roles,
          wa_partn_ctr_data_bankdetail   TYPE bus_ei_bankdetail,
          wa_partn_ctr_data_ident_number TYPE bus_ei_identification,
          wa_partn_ctr_data_taxnumber    TYPE bus_ei_taxnumber,
          wa_partn_ctr_data_addr         TYPE bus_ei_address,
          wa_partn_ctr_data_addr_addres  TYPE bus_ei_bupa_address,
          wa_partn_ctr_data_taxclass     TYPE bus_ei_tax_classification,
          wa_company                     TYPE vmds_ei_company,
          ls_msg                         TYPE bapiretc,
          v_partner.

    DATA: lt_sales        TYPE cmds_ei_sales_t,
          ls_sales        TYPE cmds_ei_sales,
          wa_relation     TYPE burs_ei_extern,
          lv_guid         TYPE sysuuid_c32,
          wa_role         TYPE bus_ei_bupa_roles,
          wa_role_2       TYPE bus_ei_bupa_roles,
          ls_bapiret2     TYPE bapiret2,
          ls_purchasing   TYPE vmds_ei_purchasing,
          ls_function     TYPE vmds_ei_functions,
          ls_bank_details TYPE bapibus1006_bankdetail,
          ls_message      TYPE bapiret2,
          ls_db_return    TYPE bapiret2.

    IF it_vendor IS NOT INITIAL.
      LOOP AT it_vendor INTO ls_vendor WHERE vendornumber IS NOT INITIAL .

        CLEAR: lt_check_existence.

*** Check if vendor already exists
        CALL FUNCTION 'BAPI_BUPA_EXISTENCE_CHECK'
          EXPORTING
            businesspartner = ls_vendor-vendornumber
          TABLES
            return          = lt_check_existence.

        IF lt_check_existence IS INITIAL.
          ls_message-id = gc_message_class.
          ls_message-number = '026'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_i.
          ls_message-message_v1 = ls_vendor-vendornumber.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
        ELSE.

          lv_check = abap_true.
          CLEAR: lv_guid,
                ls_central_data,
                ls_central_org,
                ls_central_person,
                ls_address,
                lv_busr_number,
                wa_partn_hdr,
                wa_role,
                wa_role_2,
                wa_company,
                ls_purchasing,
                wa_data, i_data,
                ls_function,
                wa_partn, lt_return, ls_return, lt_return_0, ls_return_0, lt_bank_return, lte_return, lse_return.

          ls_central_data-searchterm1 = ls_vendor-searchterm.
          IF ls_vendor-bptype = '1'.
*{   INSERT         S4HK900005                                        1
  ls_central_person-CORRESPONDLANGUAGE = 'E'.
*}   INSERT
            ls_central_person-lastname = ls_vendor-vendorname.
            ls_central_person-sex = ls_vendor-sex.
          ELSEIF ls_vendor-bptype = '2'.
            ls_central_org-name1 = ls_vendor-vendorname.
            ls_address-langu = 'E'.
          ENDIF.

          ls_central_data-title_key = ls_vendor-title.
          ls_address-district = ls_vendor-district.
          ls_address-postl_cod1 = ls_vendor-postalcode.
          ls_address-city = ls_vendor-city.
          ls_address-country = ls_vendor-country.
          ls_address-region = ls_vendor-region.
          ls_address-taxjurcode = ls_vendor-taxjuristiction.
          ls_address-street = ls_vendor-street.
          ls_address-house_no = ls_vendor-housenumber.

          ls_central_org-legalform = ls_vendor-legalform.

          IF ls_vendor-bptype = '1'.
            CALL FUNCTION 'BAPI_BUPA_CREATE_FROM_DATA'
              EXPORTING
                businesspartnerextern = ls_vendor-vendornumber
                partnercategory       = '1'  "Organisation
                centraldata           = ls_central_data
                centraldataperson     = ls_central_person
                addressdata           = ls_address
              IMPORTING
                businesspartner       = lv_busr_number
              TABLES
                return                = lt_return_0.

          ELSEIF ls_vendor-bptype = '2'.
            CALL FUNCTION 'BAPI_BUPA_CREATE_FROM_DATA'
              EXPORTING
                businesspartnerextern   = ls_vendor-vendornumber
                partnercategory         = '2'  "Organisation
                centraldata             = ls_central_data
                centraldataorganization = ls_central_org
                addressdata             = ls_address
              IMPORTING
                businesspartner         = lv_busr_number
              TABLES
                return                  = lt_return_0.
          ENDIF.

          IF lt_return_0 IS NOT INITIAL.
            LOOP AT lt_return_0 INTO ls_return_0.
              ls_message-type = ls_return_0-type.
              ls_message-id = z_cl_dataload=>gc_message_class.
              ls_message-number = '030'.

              CONCATENATE gc_vendor ls_vendor-vendornumber INTO ls_message-message_v1 SEPARATED BY space.

              IF strlen( ls_return_0-message ) > 50.
                ls_message-message_v2 = ls_return_0-message+0(50).
                ls_message-message_v3 = ls_return_0-message+50(50).
                ls_message-message_v4 = ls_return_0-message+100(50).
              ELSE.
                ls_message-message_v2 = ls_return_0-message.
              ENDIF.

              zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

              IF ls_return_0-type = 'E' OR ls_return_0-type = 'A'.
                ev_error = abap_true.
              ENDIF.
            ENDLOOP.

            IF ev_error = abap_true.
              CONTINUE.
            ENDIF.
          ENDIF.

          IF lv_busr_number IS NOT INITIAL AND ls_vendor-bankkey IS NOT INITIAL.
            ls_bank_details-bank_key = ls_vendor-bankkey.
            ls_bank_details-bank_ctry = ls_vendor-countrybank.
            ls_bank_details-bank_acct = ls_vendor-bankaccount.

            CALL FUNCTION 'BAPI_BUPA_BANKDETAIL_ADD'
              EXPORTING
                businesspartner = lv_busr_number
                bankdetaildata  = ls_bank_details
              TABLES
                return          = lt_bank_return.


            IF lt_bank_return IS NOT INITIAL.
              LOOP AT lt_bank_return INTO ls_bank_return.
                ls_message-type = ls_bank_return-type.
                ls_message-id = z_cl_dataload=>gc_message_class.
                ls_message-number = '030'.

                CONCATENATE gc_vendor ls_vendor-vendornumber INTO ls_message-message_v1 SEPARATED BY space.

                IF strlen( ls_return_0-message ) > 50.
                  ls_message-message_v2 = ls_bank_return-message+0(50).
                  ls_message-message_v3 = ls_bank_return-message+50(50).
                  ls_message-message_v4 = ls_bank_return-message+100(50).
                ELSE.
                  ls_message-message_v2 = ls_bank_return-message.
                ENDIF.

                ls_message-message_v1 = ls_vendor-vendornumber.
                ls_message-message_v2 = ls_bank_return-message.
                ls_message-message_v3 = gc_vendor.
                zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
              ENDLOOP.
              ev_error = abap_true.
              CONTINUE.
            ENDIF.
          ENDIF.

          CALL FUNCTION 'BAPI_BUPA_GET_NUMBERS'
            EXPORTING
              businesspartner        = lv_busr_number
            IMPORTING
              businesspartnerguidout = lv_guid.

          IF lv_guid IS NOT INITIAL.

            wa_partn_hdr-object_instance-bpartner     = lv_busr_number.
            wa_partn_hdr-object_instance-bpartnerguid = lv_guid.
            wa_partn_hdr-object_task              = 'M'.

            MOVE-CORRESPONDING wa_partn_hdr TO wa_partn-header.
            IF ls_vendor-bptype = '1'.
              wa_partn-central_data-taxnumber-common-data-nat_person = ls_vendor-naturalperson.
              wa_partn-central_data-taxnumber-common-datax-nat_person = 'X'.
            ENDIF.
            MOVE-CORRESPONDING wa_partn TO wa_data-partner.

********* FI Vendor
            wa_role_2-task = 'M'. "Modify
            wa_role_2-data_key = 'FLVN00'. "Role key - customer
            wa_role_2-data-rolecategory = 'FLVN00'.
            wa_role_2-data-valid_from = sy-datum.
            wa_role_2-data-valid_to = '99991231'.
            wa_role_2-currently_valid = abap_true.

            wa_role_2-datax-valid_from = abap_true.
            wa_role_2-datax-valid_to = abap_true.

            APPEND wa_role_2 TO wa_data-partner-central_data-role-roles.

********** Vendor
            wa_role-task = 'M'. "Modify
            wa_role-data_key = 'FLVN01'. "Role key - customer
            wa_role-data-rolecategory = 'FLVN01'.
            wa_role-data-valid_from = sy-datum.
            wa_role-data-valid_to = '99991231'.
            wa_role-currently_valid = abap_true.

            wa_role-datax-valid_from = abap_true.
            wa_role-datax-valid_to = abap_true.

            APPEND wa_role TO wa_data-partner-central_data-role-roles.
            wa_data-partner-central_data-role-current_state = abap_true.

*--- Vendor / company data ------------------------------------
            wa_company-task        = 'M'.    "Modify
            wa_company-data_key-bukrs = ls_vendor-companycode.

            wa_company-data-akont = ls_vendor-reconciliationaccount.
            wa_company-data-zuawa = ls_vendor-sortkey.
            wa_company-data-zterm = ls_vendor-paymentterms.
            wa_company-data-zwels = ls_vendor-paymentmethod.
            wa_company-data-busab = ls_vendor-accountingclerk.

            wa_company-datax-akont = 'X'.
            wa_company-datax-zuawa = 'X'.
            wa_company-datax-zterm = 'X'.
            wa_company-datax-zwels = 'X'.
            wa_company-datax-busab = 'X'.

            APPEND wa_company TO wa_data-vendor-company_data-company.


*--- Vendor / purchasing data ------------------------------------
            ls_purchasing-task = 'M'.
            ls_purchasing-data_key-ekorg = ls_vendor-purchasingorg.
            ls_purchasing-data-waers = ls_vendor-ordercurrency.
            ls_purchasing-data-vsbed = ls_vendor-shippingconditions.
            ls_purchasing-data-plifz = ls_vendor-planneddeltime.
            ls_purchasing-data-kalsk = ls_vendor-schemagrpsupp.
            ls_purchasing-data-kzaut = ls_vendor-automaticpo.
            ls_purchasing-data-zterm = ls_vendor-paymentterms.

            ls_purchasing-datax-waers = 'X'.
            ls_purchasing-datax-vsbed = 'X'.
            ls_purchasing-datax-plifz = 'X'.
            ls_purchasing-datax-kalsk = 'X'.
            ls_purchasing-datax-kzaut = 'X'.
            ls_purchasing-datax-zterm = 'X'.

            ls_function-data_key-parvw = 'LF'.
            APPEND ls_function TO ls_purchasing-functions-functions.

            APPEND ls_purchasing TO wa_data-vendor-purchasing_data-purchasing.
            wa_data-vendor-purchasing_data-current_state = abap_true.

*--- Vendor / Header --------------------------------------------
            wa_data-vendor-header-object_task = 'I'.
            wa_data-vendor-header-object_instance = lv_busr_number.
            wa_data-ensure_create-create_vendor = abap_true.

            APPEND wa_data TO i_data.

            CALL FUNCTION 'CVI_EI_INBOUND_MAIN'
              EXPORTING
                i_data   = i_data
              IMPORTING
                e_return = lte_return.

            IF lte_return IS NOT INITIAL.
              LOOP AT lte_return INTO lse_return.
                LOOP AT lse_return-object_msg INTO ls_msg.
                  ls_message-type = ls_msg-type.
                  ls_message-id = z_cl_dataload=>gc_message_class.
                  ls_message-number = '030'.

                  CONCATENATE gc_vendor ls_vendor-vendornumber INTO ls_message-message_v1 SEPARATED BY space.

                  IF strlen( ls_msg-message ) > 50.
                    ls_message-message_v2 = ls_msg-message+0(50).
                    ls_message-message_v3 = ls_msg-message+50(50).
                    ls_message-message_v4 = ls_msg-message+100(50).
                  ELSE.
                    ls_message-message_v2 = ls_msg-message.
                  ENDIF.

                  zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
                  CLEAR ls_message.

                  IF ls_msg-type = cl_esh_adm_constants=>gc_msgty_a OR ls_msg-type = cl_esh_adm_constants=>gc_msgty_e OR ls_msg-type = cl_esh_adm_constants=>gc_msgty_x.
                    ev_error = abap_true.
                  ENDIF.
                ENDLOOP.
              ENDLOOP.
            ENDIF.
          ENDIF.

        ENDIF.
      ENDLOOP.

      IF lv_check = abap_true.
        IF ev_error = abap_false.
          CALL FUNCTION 'BAPI_TRANSACTION_COMMIT'
            IMPORTING
              return = ls_db_return.    " Return Messages

          IF ls_db_return IS INITIAL.
            ls_message-id = gc_message_class.
            ls_message-number = '010'.
            ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
            ls_message-message_v1 = gc_vendor.

            zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
          ELSE.
            zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_db_return ).
          ENDIF.
        ELSE.
          CALL FUNCTION 'BAPI_TRANSACTION_ROLLBACK'
            IMPORTING
              return = ls_db_return.    " Return Messages

          IF ls_db_return IS NOT INITIAL.
            zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_db_return ).
          ENDIF.
        ENDIF.
      ENDIF.
    ENDIF.

  ENDMETHOD.


  METHOD call_bapi_workcenter.


    TYPES: BEGIN OF lty_log,
             lv_wc        TYPE ty_s_workcenter-workcenter,
             lv_first_msg TYPE i,
             lv_last_msg  TYPE i,
           END OF lty_log.

    DATA: ls_wc_data           TYPE REF TO data,
          lv_test              TYPE char1,
          ls_api01             TYPE crhd_api01,
          ls_api02             TYPE crhd_api02,
          ls_api05             TYPE crhd_api05,
          ls_crco              TYPE crco_api01,
          lt_crco              TYPE TABLE OF crco_api01,
          ls_crhd              TYPE crhd_api04,
          lt_crhd              TYPE TABLE OF crhd_api04,
          lt_kapa_api01        TYPE TABLE OF kapa_api01,
          ls_kapa_api01        TYPE kapa_api01,
          lt_kapa_api02        TYPE TABLE OF kapa_api02,
          ls_kapa_api02        TYPE kapa_api02,
          lt_workcenter        TYPE  tt_workcenter,
          ls_workcenter        TYPE ty_s_workcenter,
          lt_wc                TYPE tt_workcenter,
          ls_kapa_api03        TYPE kapa_api03,
          lt_kapa_api03        TYPE TABLE OF kapa_api03,
          ls_api03             TYPE crhd_api03,
          ls_message           TYPE bapiret2,
          ls_db_return         TYPE bapiret2,
          lt_header            TYPE TABLE OF balhdr,
          lt_param             TYPE TABLE OF balhdrp,
          lt_messages          TYPE TABLE OF balm,
          ls_msg               TYPE balm,
          lt_mess_param        TYPE TABLE OF balmp,
          lv_logs              TYPE i,
          ls_log               TYPE lty_log,
          lt_log               TYPE TABLE OF lty_log,
          lv_tabix             TYPE i,
          lv_counter           TYPE i,
          lv_counter2          TYPE i,
          ls_log2              TYPE lty_log,
          lv_index             TYPE i,
          lv_message_transform TYPE string,
          lv_current_year      TYPE string.

    FIELD-SYMBOLS: <lf_msg> TYPE balm.

    lv_current_year = sy-datum+0(4).

    LOOP AT it_workcenter INTO ls_workcenter .
      CLEAR: ls_api01,ls_api02,ls_api03, ls_api05, ls_crco, lt_crco, ls_crhd, lt_crhd, ls_kapa_api01,ls_kapa_api02,ls_kapa_api03, lt_kapa_api01,lt_kapa_api02,lt_kapa_api03.
      lv_tabix = lv_tabix + 1.

* Fill APO01 structure
      ls_api01-werks = ls_workcenter-plant.
      ls_api01-arbpl = ls_workcenter-workcenter.
      ls_api01-ktext = ls_workcenter-description.
      ls_api01-verwe = ls_workcenter-wccategory.

* Fill API02 structure
      ls_api02-planv = ls_workcenter-usage.
      ls_api02-vgwts = ls_workcenter-stdvaluekey.
      ls_api02-veran = ls_workcenter-personresponsible.

* Fill API03 structure
      ls_api03-vge01 = ls_workcenter-unitsofmeasurementofstdvalues1.
      ls_api03-vge02 = ls_workcenter-unitsofmeasurementofstdvalues2.
      ls_api03-vge03 = ls_workcenter-unitsofmeasurementofstdvalues3.

* Fill API05 structure
      ls_api05-kapart = ls_workcenter-capacitycategory.
      ls_api05-fort1 = ls_workcenter-durationofsetup.
      ls_api05-fort2 = ls_workcenter-processingduration.

* Fill CRCO table
      ls_crco-kostl = ls_workcenter-costcenter.
*      ls_crco-begda = '20160101'.
      CONCATENATE lv_current_year '0101' INTO ls_crco-begda.
      ls_crco-endda = gc_max_end_date.
      ls_crco-kokrs = ls_workcenter-controllingarea.
      ls_crco-lstar1 = ls_workcenter-activitytype1.
      ls_crco-lstar_ref1 =  ls_workcenter-referencedfield1.
      ls_crco-forml1 = ls_workcenter-activityformulakey1.
      ls_crco-leinh1 = ls_workcenter-activityunit1.
      ls_crco-lstar2 =  ls_workcenter-activitytype2.
      ls_crco-lstar_ref2 = ls_workcenter-referencedfield2.
      ls_crco-leinh2 = ls_workcenter-activityunit2.
      ls_crco-forml2 = ls_workcenter-activityformulakey2.
      ls_crco-lstar3 =  ls_workcenter-activitytype3.
      ls_crco-lstar_ref3 = ls_workcenter-referencedfield3.
      ls_crco-leinh3 = ls_workcenter-activityunit3.
      ls_crco-forml3 = ls_workcenter-activityformulakey3.
      APPEND ls_crco TO lt_crco.

* Fill CRHD table
      ls_crhd-fork1 = ls_workcenter-setupformula.
      ls_crhd-fork2 = ls_workcenter-processingformula.
      APPEND ls_crhd TO lt_crhd.

* Fill KAPA_API01 table
      ls_kapa_api01-kapart = ls_workcenter-capacitycategory.
      ls_kapa_api01-werks = ls_workcenter-plant.
      ls_kapa_api01-ktext = ls_workcenter-description.
      APPEND ls_kapa_api01 TO lt_kapa_api01.

* Fill KAPA_API02 table
      ls_kapa_api02-ngrad = ls_workcenter-capacityutilization.
      ls_kapa_api02-aznor = ls_workcenter-numberofindividualcapacities.
      ls_kapa_api02-kapeh = 'H'.
      ls_kapa_api02-planr = ls_workcenter-capacityplannergrp.
      ls_kapa_api02-meins = ls_workcenter-baseunitofmeasure.
      ls_kapa_api02-kalid = ls_workcenter-factorycalendarid.
      ls_kapa_api02-versa = ls_workcenter-activeversion.
      ls_kapa_api02-kapter = ls_workcenter-relevanttofinitescheduling.
      ls_kapa_api02-kapavo = ls_workcenter-canbeusedbyseveraloperations.
      ls_kapa_api02-kaplpl = ls_workcenter-longtermplanning.
      APPEND ls_kapa_api02 TO lt_kapa_api02 .

      ls_kapa_api03-versn = ls_workcenter-version.
      APPEND ls_kapa_api03 TO lt_kapa_api03.

      lv_test = abap_false.

* Create workcenter
      CALL FUNCTION 'CRAP_WORKCENTER_CREATE'
        EXPORTING
          in_crhd_api01 = ls_api01
          in_crhd_api02 = ls_api02
          in_crhd_api03 = ls_api03
          in_crhd_api05 = ls_api05
          test          = lv_test
          iv_no_commit  = abap_true
        TABLES
          in_kapa_api01 = lt_kapa_api01
          in_kapa_api02 = lt_kapa_api02
          in_crhd_api04 = lt_crhd
          in_crco_api01 = lt_crco.

* Read application log
      CLEAR: lv_logs, lt_header, lt_param, lt_mess_param, lt_messages.
      CALL FUNCTION 'APPL_LOG_READ_INTERN'
        EXPORTING
          object                 = 'CRAP'
        IMPORTING
          number_of_logs         = lv_logs
        TABLES
          header_data            = lt_header
          header_parameters      = lt_param
          messages               = lt_messages
          message_parameters     = lt_mess_param
        EXCEPTIONS
          object_not_found       = 1
          subobject_not_found    = 2
          function_not_completed = 3
          message_not_found      = 4
          parameter_missing      = 5
          OTHERS                 = 6.

      IF lv_tabix = 1.
        ls_log-lv_wc = ls_workcenter-workcenter.
        DESCRIBE TABLE lt_messages LINES lv_counter.
        ls_log-lv_first_msg = 1.
        ls_log-lv_last_msg = lv_counter.
        APPEND ls_log TO lt_log.

      ELSE.
        CLEAR ls_log2.
        ls_log-lv_wc = ls_workcenter-workcenter.
        lv_index = lv_tabix - 1.
        READ TABLE lt_log INTO ls_log2 INDEX lv_index.
        ls_log-lv_first_msg = ls_log2-lv_last_msg + 1.
        DESCRIBE TABLE lt_messages LINES lv_counter2.
        ls_log-lv_last_msg = ls_log2-lv_last_msg + lv_counter2 - lv_counter.
        lv_counter = ls_log-lv_last_msg.

        APPEND ls_log TO lt_log.
      ENDIF.
    ENDLOOP.

    LOOP AT lt_log INTO ls_log.
      LOOP AT lt_messages ASSIGNING <lf_msg> FROM ls_log-lv_first_msg TO ls_log-lv_last_msg WHERE msgty = cl_esh_adm_constants=>gc_msgty_e OR msgty = cl_esh_adm_constants=>gc_msgty_a.
        IF <lf_msg>-msgno <> '010'.

          ls_message-number = '030'.
          ls_message-id = gc_message_class.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_e.

          CONCATENATE gc_workcenter ls_log-lv_wc INTO ls_message-message_v1 SEPARATED BY space.
          CALL FUNCTION 'MESSAGE_TEXT_BUILD'
            EXPORTING
              msgid               = <lf_msg>-msgid
              msgnr               = <lf_msg>-msgno
              msgv1               = <lf_msg>-msgv1
              msgv2               = <lf_msg>-msgv2
              msgv3               = <lf_msg>-msgv3
              msgv4               = <lf_msg>-msgv4
            IMPORTING
              message_text_output = lv_message_transform.

          IF strlen( lv_message_transform ) > 50.
            ls_message-MESSAGE = lv_message_transform.
*            ls_message-message_v2 = lv_message_transform+0(50).
*            ls_message-message_v3 = lv_message_transform+50(50).
*            ls_message-message_v4 = lv_message_transform+100(50).
          ELSE.
            ls_message-message_v2 = lv_message_transform.
          ENDIF.

          ev_error = abap_true.
        ELSE.
          ls_message-number = '030'.
          ls_message-id = gc_message_class.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_i.

          CONCATENATE gc_workcenter ls_log-lv_wc INTO ls_message-message_v1 SEPARATED BY space.
          CALL FUNCTION 'MESSAGE_TEXT_BUILD'
            EXPORTING
              msgid               = <lf_msg>-msgid
              msgnr               = <lf_msg>-msgno
              msgv1               = <lf_msg>-msgv1
              msgv2               = <lf_msg>-msgv2
              msgv3               = <lf_msg>-msgv3
              msgv4               = <lf_msg>-msgv4
            IMPORTING
              message_text_output = lv_message_transform.

          IF strlen( lv_message_transform ) > 50.
            ls_message-MESSAGE = lv_message_transform.
*            ls_message-message_v2 = lv_message_transform+0(50).
*            ls_message-message_v3 = lv_message_transform+50(50).
*            ls_message-message_v4 = lv_message_transform+100(50).
          ELSE.
            ls_message-message_v2 = lv_message_transform.
          ENDIF.
        ENDIF.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
      ENDLOOP.
    ENDLOOP.

    IF ev_error = abap_false.
* No error occurs, COMMIT work
      CALL FUNCTION 'BAPI_TRANSACTION_COMMIT'
        IMPORTING
          return = ls_db_return.

      IF ls_db_return IS INITIAL.
        ls_message-number = '010'.
        ls_message-id = gc_message_class.
        ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
        ls_message-message_v1 = gc_workcenter.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
      ELSE.
        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_db_return ).
      ENDIF.

    ELSE.
* Rollback work
      CALL FUNCTION 'BAPI_TRANSACTION_ROLLBACK'
        IMPORTING
          return = ls_db_return.

      IF ls_db_return IS NOT INITIAL.
        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_db_return ).
      ENDIF.
    ENDIF.

  ENDMETHOD.


  METHOD check_input_files.


    DATA: ls_obj_flag     TYPE ty_s_sc_obj_flag,
          ls_mapping      TYPE ty_s_sc_mapping,
          ls_files        TYPE ty_s_sc_file,
          lv_check_all    TYPE boolean,
          lv_error_flag   TYPE boolean,
          lv_length_stamp TYPE i,
          lv_check        TYPE boolean,
          ls_message      TYPE bapiret2.

    LOOP AT mt_object_flag INTO ls_obj_flag WHERE required  = abap_true.
      LOOP AT mt_mapping INTO ls_mapping WHERE object_name = ls_obj_flag-object_name. "#EC CI_SORTSEQ

        lv_length_stamp = strlen( ls_mapping-file_stamp ).
        LOOP AT mt_files INTO ls_files.
          IF ls_files-file_name+0(lv_length_stamp) = ls_mapping-file_stamp.
            lv_check = abap_true.
          ENDIF.
        ENDLOOP.

        IF lv_check = abap_false.
          ls_message-id = gc_message_class.
          ls_message-number = '001'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
          ls_message-message_v1 = ls_mapping-file_stamp.
          ls_message-message_v2 = ls_mapping-object_name.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
          ev_error = abap_true.
        ENDIF.

        CLEAR lv_check.
      ENDLOOP.
    ENDLOOP.

  ENDMETHOD.


  METHOD constructor.

    DATA: ls_defaults TYPE bapidefaul,
          lt_return   TYPE TABLE OF bapiret2,
          lv_datfm TYPE XUDATFM.

* As some of the objects are required to exist in order for the others to be created, a certain sequence has to be implemented
    mt_mapping = VALUE #(
      ( sequence = '1001'       object_name = 'SEGMENT'           file_stamp = gc_segment_f  )
      ( sequence = '1002'       object_name = 'FUNCTIONAL AREA'   file_stamp = gc_func_area_f  )
      ( sequence = '1003'       object_name = 'MAT GROUP'         file_stamp = gc_mat_grp_f  )
      ( sequence = '1004'       object_name = 'PURCHASING GROUP'  file_stamp = gc_pur_grp_f  )
      ( sequence = '1005'       object_name = 'CUST GROUP'        file_stamp = gc_cust_grp_f  )
      ( sequence = '1006'       object_name = 'ACCOUNTING CLERK'  file_stamp = gc_acc_clerks_f  )
      ( sequence = '1007'       object_name = 'PROFIT HIERARCHY'  file_stamp = gc_profit_hier_f  )
      ( sequence = '1008'       object_name = 'COST HIERARCHY'    file_stamp = gc_cost_hier_f  )
*      ( sequence = '1009'       object_name = 'SUBSTITUTION'      file_stamp = gc_substitution_f  )
      ( sequence = '1010'       object_name = 'MRP CONTROLLER'    file_stamp = gc_mrp_controller_f )
      ( sequence = '2001'       object_name = 'PROFIT CENTER'     file_stamp = gc_profit_center_f  )
      ( sequence = '2002'       object_name = 'COST CENTER'       file_stamp = gc_cost_center_f  )
      ( sequence = '2003'       object_name = 'CUSTOMER'          file_stamp = gc_customer_f  )
      ( sequence = '2004'       object_name = 'VENDOR'            file_stamp = gc_vendor_f  )
      ( sequence = '2005'       object_name = 'MATERIAL'          file_stamp = gc_material_f  )
      ( sequence = '2006'       object_name = 'BOM'               file_stamp = gc_bom_f  )
      ( sequence = '2007'       object_name = 'ACTIVITY'          file_stamp = gc_activity_f  )
      ( sequence = '2008'       object_name = 'WORKCENTER'        file_stamp = gc_workcenter_f  )
      ( sequence = '2009'       object_name = 'ROUTING'           file_stamp = gc_routing_f  )
      ( sequence = '2010'       object_name = 'PRODVERS'          file_stamp = gc_prodvers_f  )
      ( sequence = '2011'       object_name = 'SALE_PRICE'        file_stamp = gc_sale_price_f  )
      ).

* Initialize the message buffer class
    zcl_dataload_message_buffer=>init( ).

     call function 'SUSR_USER_DEFAULT_DATE_FORMAT'
                      importing datfm = lv_datfm.
    UPDATE usr01
       SET dcpfm = ''
       datfm = lv_datfm " '1'
       WHERE bname = sy-uname .

    COMMIT WORK.

** Retrieve Date Format from User Settings
*    CALL FUNCTION 'BAPI_USER_GET_DETAIL'
*      EXPORTING
*        username = sy-uname
*      IMPORTING
*        defaults = ls_defaults
*      TABLES
*        return   = lt_return.
*
*    CASE ls_defaults-datfm.                                 "#EC DATFM
    CASE lv_datfm .
      WHEN '1'.
*        mv_valid_from_date = '01.01.2016'.
        CONCATENATE '01.01.' sy-datum+0(4) INTO mv_valid_from_date .
        mv_valid_to_date =  '31.12.9999' .

      WHEN '2'.
*        mv_valid_from_date = '01/01/2016'.
        CONCATENATE '01/01/' sy-datum+0(4) INTO mv_valid_from_date .
        mv_valid_to_date =  '12/31/9999' .

      WHEN '3'.
*        mv_valid_from_date = '01-01-2016'.
        CONCATENATE '01-01-' sy-datum+0(4) INTO mv_valid_from_date .
        mv_valid_to_date =  '12-31-9999' .

      WHEN '4'.
*        mv_valid_from_date = '2016.01.01'.
        CONCATENATE sy-datum+0(4) '.01.01'  INTO mv_valid_from_date .
        mv_valid_to_date =  '9999.12.31' .

      WHEN '5'.
*        mv_valid_from_date = '2016/01/01'.
        CONCATENATE sy-datum+0(4) '/01/01'  INTO mv_valid_from_date .
        mv_valid_to_date =  '9999/12/31' .

      WHEN '6'.
*        mv_valid_from_date = '2016-01-01'.
        CONCATENATE sy-datum+0(4) '-01-01'  INTO mv_valid_from_date .
        mv_valid_to_date =  '9999-12-31' .

      WHEN OTHERS.
    ENDCASE.




  ENDMETHOD.


  METHOD create_cust_acc_clerk.


    DATA: lt_acc_clerk        TYPE TABLE OF t001s,
          ls_acc_clerk        TYPE t001s,
          ls_accounting_clerk TYPE ty_s_acc_clerk,
          lt_accounting_clerk TYPE TABLE OF t001s,
          ls_message          TYPE bapiret2.



    SELECT * INTO TABLE lt_accounting_clerk FROM t001s.

    LOOP AT it_accounting_clerk INTO ls_accounting_clerk WHERE accountingclerk is NOT INITIAL.

      READ TABLE lt_accounting_clerk WITH KEY busab = ls_accounting_clerk-accountingclerk BUKRS = ls_accounting_clerk-cocode TRANSPORTING NO FIELDS.

      IF sy-subrc IS INITIAL.
        ls_message-id = gc_message_class.
        ls_message-number = '037'.
        ls_message-type = cl_esh_adm_constants=>gc_msgty_i.
        ls_message-message_v1 = ls_accounting_clerk-accountingclerk.
        ls_message-message_v2 = ls_accounting_clerk-name.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

      ELSE.

        ls_acc_clerk-mandt = sy-mandt.
        ls_acc_clerk-bukrs = ls_accounting_clerk-cocode.
        ls_acc_clerk-busab = ls_accounting_clerk-accountingclerk.
        ls_acc_clerk-sname = ls_accounting_clerk-name .
        APPEND ls_acc_clerk TO lt_acc_clerk.


      ENDIF.

    ENDLOOP.

    IF lt_acc_clerk IS NOT INITIAL.

      TRY .
          INSERT t001s FROM TABLE lt_acc_clerk.

          ls_message-id = gc_message_class.
          ls_message-number = '044'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
          ls_message-message_v1 = gc_acc_clerks.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

        CATCH cx_root .
          ev_error = abap_true.

          ls_message-id = gc_message_class.
          ls_message-number = '043'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
          ls_message-message_v1 = ls_accounting_clerk-accountingclerk.
          ls_message-message_v2 = ls_accounting_clerk-name.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
      ENDTRY.

    ENDIF.



  ENDMETHOD.


  METHOD create_cust_customer_group.

    DATA: lt_cust_group     TYPE TABLE OF t151,
          ls_cust_group     TYPE t151,
          lt_cust_group_t   TYPE TABLE OF t151t,
          ls_cust_group_t   TYPE t151t,
          ls_customer_group TYPE ty_s_cust_group,
          lt_customer_group TYPE TABLE OF t151,
          ls_message        TYPE bapiret2.

    CLEAR: ls_cust_group ,lt_cust_group ,ls_cust_group_t ,lt_cust_group_t .

    SELECT * INTO TABLE lt_customer_group FROM t151.

    LOOP AT it_customer_group INTO ls_customer_group WHERE code is NOT INITIAL.

      READ TABLE lt_customer_group WITH KEY kdgrp = ls_customer_group-code TRANSPORTING NO FIELDS.

      IF sy-subrc IS INITIAL.
        ls_message-id = gc_message_class.
        ls_message-number = '036'.
        ls_message-type = cl_esh_adm_constants=>gc_msgty_i.
        ls_message-message_v1 = ls_customer_group-code.
        ls_message-message_v2 = ls_customer_group-description.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

      ELSE.

        ls_cust_group-mandt = sy-mandt.
        ls_cust_group-kdgrp = ls_customer_group-code.
        APPEND ls_cust_group TO lt_cust_group.

        ls_cust_group_t-mandt = sy-mandt.
        ls_cust_group_t-kdgrp = ls_customer_group-code.
        ls_cust_group_t-spras = sy-langu.
        ls_cust_group_t-ktext = ls_customer_group-description.
        APPEND ls_cust_group_t TO lt_cust_group_t.

      ENDIF.

    ENDLOOP.

    IF lt_cust_group IS NOT INITIAL AND lt_cust_group_t IS NOT INITIAL.

      TRY .
          INSERT t151 FROM TABLE lt_cust_group.
          INSERT t151t FROM TABLE lt_cust_group_t.

          ls_message-id = gc_message_class.
          ls_message-number = '044'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
          ls_message-message_v1 = gc_cust_grp.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

        CATCH cx_root .
          ev_error = abap_true.

          ls_message-id = gc_message_class.
          ls_message-number = '042'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
          ls_message-message_v1 = ls_customer_group-code.
          ls_message-message_v2 = ls_customer_group-description.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

      ENDTRY.

    ENDIF.


  ENDMETHOD.


  METHOD create_cust_functional_area.

    DATA : lt_fct_area        TYPE TABLE OF tfkb,
           ls_fct_area        TYPE tfkb,
           lt_fct_area_t      TYPE TABLE OF tfkbt,
           ls_fct_area_t      TYPE tfkbt,
           ls_functional_area TYPE ty_s_fct_area,
           lt_functional_area TYPE TABLE OF tfkb,
           ls_message         TYPE bapiret2.

    SELECT * INTO TABLE lt_functional_area FROM tfkb .

    LOOP AT it_functional_area INTO ls_functional_area WHERE code  IS NOT INITIAL.

      READ TABLE lt_functional_area WITH KEY fkber = ls_functional_area-code  TRANSPORTING NO FIELDS.
      IF sy-subrc IS  INITIAL.

        ls_message-id = gc_message_class.
        ls_message-number = '033'.
        ls_message-type = cl_esh_adm_constants=>gc_msgty_i.
        ls_message-message_v1 = ls_functional_area-code.
        ls_message-message_v2 = ls_functional_area-description.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

      ELSE.
        ls_fct_area-fkber = ls_functional_area-code.
        ls_fct_area-mandt = sy-mandt.
        APPEND ls_fct_area TO lt_fct_area.

        ls_fct_area_t-fkber =  ls_functional_area-code.
        ls_fct_area_t-mandt = sy-mandt.
        ls_fct_area_t-spras = sy-langu.
        ls_fct_area_t-fkbtx =  ls_functional_area-description.
        APPEND ls_fct_area_t TO lt_fct_area_t.
      ENDIF.

    ENDLOOP.

    IF lt_fct_area IS NOT INITIAL AND lt_fct_area_t IS NOT INITIAL.

      TRY.
          INSERT tfkb FROM TABLE lt_fct_area.
          INSERT tfkbt FROM TABLE lt_fct_area_t.

          ls_message-id = gc_message_class.
          ls_message-number = '044'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
          ls_message-message_v1 = gc_func_area.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

        CATCH cx_root.
          ev_error = abap_true.

          ls_message-id = gc_message_class.
          ls_message-number = '039'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
          ls_message-message_v1 = ls_functional_area-code.
          ls_message-message_v2 = ls_functional_area-description.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

      ENDTRY.

    ENDIF.

  ENDMETHOD.


  METHOD create_cust_material_group.

    DATA: lt_mat_group      TYPE TABLE OF t023,
          ls_mat_group      TYPE t023,
          lt_mat_group_t    TYPE TABLE OF t023t,
          ls_mat_group_t    TYPE t023t,
          ls_material_group TYPE ty_s_mat_group,
          lt_material_group TYPE TABLE OF t023,
          ls_message        TYPE bapiret2.

    CLEAR: ls_mat_group ,lt_mat_group ,ls_mat_group_t ,lt_mat_group_t .

    SELECT * INTO TABLE lt_material_group FROM t023.

    LOOP AT it_material_group INTO ls_material_group WHERE code IS NOT INITIAL.
      READ TABLE lt_material_group WITH KEY matkl = ls_material_group-code TRANSPORTING NO FIELDS.

      IF sy-subrc IS INITIAL.

        ls_message-id = gc_message_class.
        ls_message-number = '034'.
        ls_message-type = cl_esh_adm_constants=>gc_msgty_i.
        ls_message-message_v1 = ls_material_group-code.
        ls_message-message_v2 = ls_material_group-description.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).


      ELSE.
        ls_mat_group-mandt = sy-mandt.
        ls_mat_group-matkl = ls_material_group-code.
        APPEND ls_mat_group TO lt_mat_group.

        ls_mat_group_t-mandt = sy-mandt.
        ls_mat_group_t-matkl = ls_material_group-code.
        ls_mat_group_t-spras = sy-langu.
        ls_mat_group_t-wgbez = ls_material_group-description.
        APPEND ls_mat_group_t TO lt_mat_group_t.

      ENDIF.
    ENDLOOP.

    IF lt_mat_group IS NOT INITIAL AND lt_mat_group_t IS NOT INITIAL.

      TRY .
          INSERT t023 FROM TABLE lt_mat_group.
          INSERT t023t FROM TABLE lt_mat_group_t.

          ls_message-id = gc_message_class.
          ls_message-number = '044'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
          ls_message-message_v1 = gc_mat_grp.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

        CATCH cx_root.
          ev_error = abap_true.

          ls_message-id = gc_message_class.
          ls_message-number = '040'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
          ls_message-message_v1 = ls_material_group-code.
          ls_message-message_v2 = ls_material_group-description.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
      ENDTRY.

    ENDIF.


  ENDMETHOD.


  METHOD create_cust_mrp_controller.

    DATA : lt_mrp     TYPE  TABLE OF t024d,
           ls_mrp     TYPE t024d,
           lt_mrpt    TYPE TABLE OF t001w,
           ls_mrpt    TYPE t001w,
           ls_mrp_ctr TYPE ty_s_mrp_controller,
           ls_message TYPE bapiret2,
           lt_mrp_ctr TYPE TABLE OF t024d.

    CLEAR: ls_mrp, ls_mrpt, lt_mrp, lt_mrpt.
    SELECT * INTO TABLE lt_mrp_ctr FROM t024d .

    LOOP AT it_mrp_controller INTO ls_mrp_ctr WHERE mrpcontroller is NOT INITIAL.
      READ TABLE lt_mrp_ctr WITH KEY dispo = ls_mrp_ctr-mrpcontroller werks = ls_mrp_ctr-plant TRANSPORTING NO FIELDS.
      IF sy-subrc IS  INITIAL.
        ls_message-id = gc_message_class.
        ls_message-number = '047'.
        ls_message-type = cl_esh_adm_constants=>gc_msgty_i.
        ls_message-message_v1 = ls_mrp_ctr-plant.
        ls_message-message_v2 = ls_mrp_ctr-mrpcontroller.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

      ELSE.
        ls_mrp-mandt = sy-mandt.
        ls_mrp-werks = ls_mrp_ctr-plant.
        ls_mrp-dispo = ls_mrp_ctr-mrpcontroller.
        ls_mrp-dsnam = ls_mrp_ctr-mrpcontrollername.
        APPEND ls_mrp TO lt_mrp.

      ENDIF.
    ENDLOOP.

    IF lt_mrp IS NOT INITIAL .

      TRY .
          INSERT t024d FROM TABLE lt_mrp.

          ls_message-id = gc_message_class.
          ls_message-number = '044'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
          ls_message-message_v1 = gc_mrp_controller.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

        CATCH cx_root.
          ev_error = abap_true.
          ls_message-id = gc_message_class.
          ls_message-number = '048'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_e .

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).



      ENDTRY.

    ENDIF.


  ENDMETHOD.


  METHOD create_cust_purchasing_group.

    DATA: lt_pur_group        TYPE TABLE OF t024,
          ls_pur_group        TYPE t024,
          ls_purchasing_group TYPE ty_s_pur_group,
          lt_purchasing_group TYPE TABLE OF t024,
          ls_message          TYPE bapiret2.

    CLEAR: ls_pur_group ,lt_pur_group .

    SELECT * INTO TABLE lt_purchasing_group FROM t024.

    LOOP AT it_purchasing_group INTO ls_purchasing_group WHERE code is NOT INITIAL.

      READ TABLE lt_purchasing_group WITH KEY ekgrp = ls_purchasing_group-code TRANSPORTING NO FIELDS.
      IF sy-subrc IS INITIAL.

        ls_message-id = gc_message_class.
        ls_message-number = '035'.
        ls_message-type = cl_esh_adm_constants=>gc_msgty_i.
        ls_message-message_v1 = ls_purchasing_group-code.
        ls_message-message_v2 = ls_purchasing_group-description.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

      ELSE.

        ls_pur_group-mandt = sy-mandt.
        ls_pur_group-ekgrp = ls_purchasing_group-code.
        ls_pur_group-eknam = ls_purchasing_group-description.
        ls_pur_group-ektel = ls_purchasing_group-telephone .
        ls_pur_group-tel_extens = ls_purchasing_group-extension.
        ls_pur_group-telfx  = ls_purchasing_group-fax .
        ls_pur_group-smtp_addr = ls_purchasing_group-email .
        APPEND ls_pur_group TO lt_pur_group.

      ENDIF.

    ENDLOOP.

    IF lt_pur_group IS NOT INITIAL.
      TRY .
          INSERT t024 FROM TABLE lt_pur_group.

          ls_message-id = gc_message_class.
          ls_message-number = '044'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
          ls_message-message_v1 = gc_pur_grp.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

        CATCH cx_root.
          ev_error = abap_true.

          ls_message-id = gc_message_class.
          ls_message-number = '041'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
          ls_message-message_v1 = ls_purchasing_group-code.
          ls_message-message_v2 = ls_purchasing_group-description.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

      ENDTRY.
    ENDIF.


  ENDMETHOD.


  METHOD create_cust_segment.

    DATA : lt_segm    TYPE  TABLE OF fagl_segm,
           ls_segm    TYPE fagl_segm,
           lt_segmt   TYPE TABLE OF fagl_segmt,
           ls_segmt   TYPE fagl_segmt,
           ls_segment TYPE ty_s_segments,
           ls_message TYPE bapiret2,
           lt_segment TYPE TABLE OF fagl_segm.

    CLEAR: ls_segm, ls_segmt, lt_segm, lt_segmt.
    SELECT * INTO TABLE lt_segment FROM fagl_segm .

    LOOP AT it_segment INTO ls_segment WHERE code IS NOT INITIAL.
      READ TABLE lt_segment WITH KEY segment = ls_segment-code TRANSPORTING NO FIELDS.
      IF sy-subrc IS  INITIAL.
        ls_message-id = gc_message_class.
        ls_message-number = '032'.
        ls_message-type = cl_esh_adm_constants=>gc_msgty_i.
        ls_message-message_v1 = ls_segment-code.
        ls_message-message_v2 = ls_segment-description.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

      ELSE.
        ls_segm-mandt = sy-mandt.
        ls_segm-segment = ls_segment-code.
        APPEND ls_segm TO lt_segm.

        ls_segmt-langu = sy-langu.
        ls_segmt-mandt = sy-mandt.
        ls_segmt-segment = ls_segment-code.
        ls_segmt-name = ls_segment-description.
        APPEND ls_segmt TO lt_segmt.

      ENDIF.
    ENDLOOP.

    IF lt_segm IS NOT INITIAL AND lt_segmt IS NOT INITIAL.

      TRY .
          INSERT fagl_segm FROM TABLE lt_segm.
          INSERT fagl_segmt FROM TABLE lt_segmt.

          ls_message-id = gc_message_class.
          ls_message-number = '044'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
          ls_message-message_v1 = gc_segment.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

        CATCH cx_root.
          ev_error = abap_true.
          ls_message-id = gc_message_class.
          ls_message-number = '038'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_e .

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).



      ENDTRY.

    ENDIF.

  ENDMETHOD.


  METHOD fill_files_and_paths.

    DATA ls_file TYPE ty_s_sc_file.


    IF iv_filename IS NOT INITIAL AND iv_file_fullpath IS NOT INITIAL.
      ls_file-file_name = iv_filename.
      ls_file-file_path = iv_file_fullpath.
      APPEND ls_file TO mt_files.
    ENDIF.

  ENDMETHOD.


  METHOD fill_required_objects.


    DATA: ls_object_flag LIKE LINE OF mt_object_flag,
          ls_mapping     LIKE LINE OF mt_mapping.

    LOOP AT it_obj_flag INTO ls_object_flag.            "#EC CI_SORTSEQ
      LOOP AT mt_mapping INTO ls_mapping WHERE object_name = ls_object_flag-object_name.
        ls_object_flag-sequence = ls_mapping-sequence.
        APPEND ls_object_flag TO mt_object_flag.
      ENDLOOP.
    ENDLOOP.

    SORT mt_object_flag ASCENDING BY sequence.

  ENDMETHOD.


  METHOD process_data.


    DATA: ls_object_flag        LIKE LINE OF mt_object_flag,
          ls_file               LIKE LINE OF mt_files,
          ls_mapping            LIKE LINE OF mt_mapping,
          lt_wc_data            TYPE REF TO data,
          lt_material_data      TYPE REF TO data,
          lt_bom_data           TYPE REF TO data,
          lt_activity_data      TYPE REF TO data,
          lt_customer_data      TYPE REF TO data,
          lt_vendor_data        TYPE REF TO data,
          lt_cost_center_data   TYPE REF TO data,
          lt_routing_data       TYPE REF TO data,
          ls_message            TYPE        bapiret2,
          lt_prodvers_data      TYPE REF TO data,
          lt_sale_price         TYPE REF TO data,
          lt_segment            TYPE REF TO data,
          lt_mat_group          TYPE REF TO data,
          lt_pur_group          TYPE REF TO data,
          lt_cust_group         TYPE REF TO data,
          lt_acc_clerk          TYPE REF TO data,
          lt_fct_area           TYPE REF TO data,
          lt_profit_center      TYPE REF TO data,
          lt_profit_center_hier TYPE REF TO data,
          lt_cost_center        TYPE REF TO data,
          lt_cost_center_hier   TYPE REF TO data,
          lt_mrp_controller     TYPE REF TO data.

    FIELD-SYMBOLS: <lft_data> TYPE ANY TABLE.

    SORT mt_object_flag ASCENDING BY sequence.

    READ TABLE mt_object_flag INTO ls_object_flag WITH KEY required = abap_true.
    IF ls_object_flag IS INITIAL.
      ls_message-id = gc_message_class.
      ls_message-number = '029'.
      ls_message-type = cl_esh_adm_constants=>gc_msgty_e.

      zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
      ev_error = abap_true.
      RETURN.
    ENDIF.

    LOOP AT mt_object_flag INTO ls_object_flag WHERE required = abap_true.

      CASE ls_object_flag-object_name.
        WHEN gc_workcenter.
          CREATE DATA lt_wc_data TYPE tt_workcenter.
          ASSIGN lt_wc_data->* TO <lft_data>.

        WHEN gc_material.
          CREATE DATA lt_material_data TYPE tt_material.
          ASSIGN lt_material_data->* TO <lft_data>.

        WHEN gc_bom.
          CREATE DATA lt_bom_data TYPE tt_bom.
          ASSIGN lt_bom_data->* TO <lft_data>.

        WHEN gc_routing.
          CREATE DATA lt_routing_data TYPE tt_routing.
          ASSIGN lt_routing_data->* TO <lft_data>.

        WHEN gc_activity.
          CREATE DATA lt_activity_data TYPE tt_activity_rate.
          ASSIGN lt_activity_data->* TO <lft_data>.

        WHEN gc_customer.
          CREATE DATA lt_customer_data TYPE tt_customer.
          ASSIGN lt_customer_data->* TO <lft_data>.

        WHEN gc_vendor.
          CREATE DATA lt_vendor_data TYPE tt_vendor.
          ASSIGN lt_vendor_data->* TO <lft_data>.

        WHEN gc_prodvers .
          CREATE DATA lt_prodvers_data TYPE tt_prod_vers.
          ASSIGN lt_prodvers_data->* TO <lft_data>.

        WHEN gc_sale_price.
          CREATE DATA lt_sale_price TYPE tt_sale_price.
          ASSIGN lt_sale_price->* TO <lft_data>.

        WHEN gc_segment.
          CREATE DATA lt_segment TYPE tt_segments.
          ASSIGN lt_segment->* TO <lft_data>.

        WHEN gc_acc_clerks.
          CREATE DATA lt_acc_clerk TYPE tt_acc_clerk.
          ASSIGN lt_acc_clerk->* TO <lft_data>.

        WHEN gc_func_area.
          CREATE DATA lt_fct_area TYPE tt_fct_area.
          ASSIGN lt_fct_area->* TO <lft_data>.

        WHEN gc_mat_grp.
          CREATE DATA lt_mat_group TYPE tt_mat_group.
          ASSIGN lt_mat_group->* TO <lft_data>.

        WHEN gc_pur_grp.
          CREATE DATA lt_pur_group TYPE tt_pur_group.
          ASSIGN lt_pur_group->* TO <lft_data>.

        WHEN gc_cust_grp.
          CREATE DATA lt_cust_group TYPE tt_cust_group.
          ASSIGN lt_cust_group->* TO <lft_data>.

        WHEN gc_profit_center.
          CREATE DATA lt_profit_center TYPE tt_profit_center.
          ASSIGN lt_profit_center->* TO <lft_data>.

        WHEN gc_profit_hier.
          CREATE DATA lt_profit_center_hier TYPE tt_profit_center_hier.
          ASSIGN lt_profit_center_hier->* TO <lft_data>.

        WHEN gc_cost_center.
          CREATE DATA lt_cost_center TYPE tt_cost_center.
          ASSIGN lt_cost_center->* TO <lft_data>.

        WHEN gc_cost_hier.
          CREATE DATA lt_cost_center_hier TYPE tt_cost_center_hier.
          ASSIGN lt_cost_center_hier->* TO <lft_data>.

        WHEN gc_mrp_controller.
          CREATE DATA lt_mrp_controller TYPE tt_mrp_controller.
          ASSIGN lt_mrp_controller->* TO <lft_data>.

        WHEN OTHERS.

      ENDCASE.

      retrieve_file_content(
        EXPORTING
          iv_object_name = ls_object_flag-object_name    " 30 Characters
          iv_sequence    = ls_object_flag-sequence    " Natural number
        IMPORTING
          et_data        = <lft_data>
          ev_error       = ev_error
      ).

      IF <lft_data> IS NOT INITIAL AND ev_error = abap_false.
        call_bapi(
          EXPORTING
            it_table       = <lft_data>
            iv_object_name = ls_object_flag-object_name
            iv_sequence    = ls_object_flag-sequence
          IMPORTING
            ev_error       = ev_error
        ).

        IF ev_error = abap_true.
          EXIT.
        ENDIF.
      ENDIF.
    ENDLOOP.

    IF ev_error = abap_true.
      ls_message-id = gc_message_class.
      ls_message-number = '013'.
      ls_message-type = cl_esh_adm_constants=>gc_msgty_e.

      zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
    ENDIF.

  ENDMETHOD.


  METHOD retrieve_file_content.


    TYPES: BEGIN OF l_typ_confrontation,
             intfieldname TYPE string,
             intfieldpos  TYPE i,
             intfieldtyp  TYPE string,
             csvfieldpos  TYPE i,
             csvfieldname TYPE string,
           END OF l_typ_confrontation.

    DATA: lt_csv_data         TYPE stringtab,
          lt_fields           TYPE STANDARD TABLE OF string,
          ls_mapping          LIKE LINE OF mt_mapping,
          lv_full_path        TYPE string,
          ls_file             LIKE LINE OF mt_files,
          lv_length           TYPE i,
          lv_string           TYPE string,
          l_rda_data          TYPE REF TO data,
          l_rda_wa            TYPE REF TO data,
          l_rcl_descr_tab     TYPE REF TO cl_abap_tabledescr,
          l_rcl_descr_struc   TYPE REF TO cl_abap_structdescr,
          l_comp_descr        TYPE abap_compdescr,
          l_tab_content       TYPE STANDARD TABLE OF string,
          l_line              TYPE string VALUE '',
          l_tab_confrontation TYPE STANDARD TABLE OF l_typ_confrontation WITH KEY csvfieldpos,
          l_fieldname         TYPE string VALUE '',
          l_content           TYPE string VALUE '',
          l_conf              TYPE l_typ_confrontation,
          ls_message          TYPE bapiret2.

    FIELD-SYMBOLS: <l_table> TYPE STANDARD TABLE,
                   <l_comp>  TYPE any,
                   <l_wa>    TYPE any,
                   <line>    TYPE string.

    READ TABLE mt_mapping INTO ls_mapping WITH KEY object_name = iv_object_name
                                                   sequence    = iv_sequence.

    IF ls_mapping-file_stamp IS NOT INITIAL.
      lv_length = strlen( ls_mapping-file_stamp ).

      LOOP AT mt_files INTO ls_file.
        lv_string = ls_file-file_name+0(lv_length).

        IF lv_string = ls_mapping-file_stamp.
          lv_full_path = ls_file-file_path.
          EXIT.
        ENDIF.
      ENDLOOP.

      IF lv_full_path IS NOT INITIAL.

        CALL FUNCTION 'GUI_UPLOAD'
          EXPORTING
            filename = lv_full_path
            filetype = 'ASC'
          TABLES
            data_tab = lt_csv_data
          EXCEPTIONS
            OTHERS   = 1.
        IF sy-subrc  <> 0.
          ls_message-id = gc_message_class.
          ls_message-number = '002'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
          ls_message-message_v1 = ls_mapping-object_name.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

          ev_error = abap_true.
        ENDIF.

        IF lt_csv_data IS NOT INITIAL.

*** Manipulate Headline
          READ TABLE lt_csv_data INDEX 1 ASSIGNING  <line>.
          IF <line> IS ASSIGNED.
            REPLACE ALL OCCURRENCES OF '-' IN <line> WITH space.
            REPLACE ALL OCCURRENCES OF '.' IN <line> WITH space.
            REPLACE ALL OCCURRENCES OF ':' IN <line> WITH space.
            REPLACE ALL OCCURRENCES OF '(' IN <line> WITH space.
            REPLACE ALL OCCURRENCES OF ')' IN <line> WITH space.
            REPLACE ALL OCCURRENCES OF '%' IN <line> WITH space.
            REPLACE ALL OCCURRENCES OF '/' IN <line> WITH space.
            CONDENSE  <line> NO-GAPS.
            TRANSLATE <line> TO LOWER CASE.
            SPLIT  <line> AT cl_abap_char_utilities=>horizontal_tab INTO TABLE lt_fields.

            CASE iv_object_name.
              WHEN gc_customer.
                CREATE DATA l_rda_data TYPE tt_customer.
              WHEN gc_vendor.
                CREATE DATA l_rda_data TYPE tt_vendor.
              WHEN gc_activity.
                CREATE DATA l_rda_data TYPE tt_activity_rate.
              WHEN gc_material.
                CREATE DATA l_rda_data TYPE tt_material.
              WHEN gc_bom.
                CREATE DATA l_rda_data TYPE tt_bom.
              WHEN gc_workcenter.
                CREATE DATA l_rda_data TYPE tt_workcenter.
              WHEN gc_routing.
                CREATE DATA l_rda_data TYPE tt_routing.
              WHEN gc_prodvers.
                CREATE DATA l_rda_data TYPE tt_prod_vers.
              WHEN gc_sale_price.
                CREATE DATA l_rda_data TYPE tt_sale_price.
              WHEN gc_segment.
                CREATE DATA l_rda_data TYPE tt_segments.
              WHEN gc_acc_clerks.
                CREATE DATA l_rda_data TYPE tt_acc_clerk.
              WHEN gc_cust_grp.
                CREATE DATA l_rda_data TYPE tt_cust_group.
              WHEN gc_mat_grp.
                CREATE DATA l_rda_data TYPE tt_mat_group.
              WHEN gc_pur_grp.
                CREATE DATA l_rda_data TYPE tt_pur_group.
              WHEN gc_func_area.
                CREATE DATA l_rda_data TYPE tt_fct_area.
              WHEN gc_profit_center.
                CREATE DATA l_rda_data TYPE tt_profit_center.
              WHEN gc_profit_hier.
                CREATE DATA l_rda_data TYPE tt_profit_center_hier.
              WHEN gc_cost_center.
                CREATE DATA l_rda_data TYPE tt_cost_center.
              WHEN gc_cost_hier.
                CREATE DATA l_rda_data TYPE tt_cost_center_hier.
              WHEN gc_mrp_controller.
                CREATE DATA l_rda_data TYPE tt_mrp_controller.

            ENDCASE.
            ASSIGN l_rda_data->* TO <l_table>.

*** Get Structure of Table
            l_rcl_descr_tab ?= cl_abap_typedescr=>describe_by_data( <l_table> ).
            l_rcl_descr_struc ?= l_rcl_descr_tab->get_table_line_type( ).

*** Define Line of Table
            CREATE DATA l_rda_wa LIKE LINE OF  <l_table>.
            ASSIGN l_rda_wa->* TO  <l_wa>.

*-Compare field names of the table with headline of the import file
*
*- Within this step the position of the column is indiferent. It
*- is only necessary that the field of the table and the column
*- of the import file must have the same name.

            LOOP AT l_rcl_descr_struc->components INTO l_comp_descr.
              l_conf-intfieldname = l_comp_descr-name.
              l_conf-intfieldpos = sy-tabix.
              l_conf-intfieldtyp = l_comp_descr-type_kind.
              LOOP AT lt_fields INTO l_fieldname.
                l_conf-csvfieldpos = -1.
                TRANSLATE l_fieldname TO UPPER CASE.
                l_conf-csvfieldname = 'UNKNOWN'.
                IF l_comp_descr-name = l_fieldname.
                  l_conf-csvfieldname = l_fieldname.
                  l_conf-csvfieldpos = sy-tabix.
                  EXIT.
                ENDIF.
              ENDLOOP.
              APPEND l_conf TO l_tab_confrontation.
            ENDLOOP.
            DELETE l_tab_confrontation WHERE csvfieldpos = -1.
            SORT l_tab_confrontation BY csvfieldpos.

            LOOP AT lt_csv_data INTO l_line FROM 2.
              SPLIT l_line AT cl_abap_char_utilities=>horizontal_tab INTO TABLE l_tab_content.
              LOOP AT l_tab_content INTO l_content.
                CONDENSE l_content.
                READ TABLE l_tab_confrontation WITH KEY csvfieldpos = sy-tabix
                  INTO l_conf.
                IF sy-subrc = 0.
                  ASSIGN COMPONENT l_conf-intfieldname OF STRUCTURE  <l_wa>
                    TO  <l_comp>.
                  IF l_conf-intfieldtyp = 'P'.
                    REPLACE ALL OCCURRENCES OF '.' IN l_content WITH ''.
                    REPLACE ',' IN l_content WITH '.'.
                    REPLACE ALL OCCURRENCES OF '"' IN l_content WITH ''.
                    CONDENSE l_content.
                    <l_comp> = l_content.
                  ELSE.
                    <l_comp> = l_content.
                  ENDIF.
                ENDIF.
              ENDLOOP.
              APPEND  <l_wa> TO  <l_table>.
              CLEAR  <l_wa>.
            ENDLOOP.

            IF sy-subrc IS NOT INITIAL.
              ls_message-id = gc_message_class.
              ls_message-number = '022'.
              ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
              ls_message-message_v1 = ls_mapping-file_stamp.
              ls_message-message_v2 = ls_mapping-object_name.

              zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
            ELSE.
*** Write Data into Table
              et_data = <l_table>.
            ENDIF.
          ENDIF.
        ELSE.
* Import file data is initial
          ls_message-id = gc_message_class.
          ls_message-number = '022'.
          ls_message-type = cl_esh_adm_constants=>gc_msgty_e.
          ls_message-message_v1 = ls_mapping-file_stamp.
          ls_message-message_v2 = ls_mapping-object_name.

          zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).

          ev_error = abap_true.
        ENDIF.
      ENDIF.
    ENDIF.

  ENDMETHOD.


  METHOD set_material_version_flag.

    DATA:

      ls_headdata1      TYPE bapimathead,
      ls_mara1          TYPE bapi_mara,
      ls_marax1         TYPE bapi_marax,
      ls_marc1          TYPE bapi_marc,
      ls_marcx1         TYPE bapi_marcx,
      ls_mpop1          TYPE bapi_mpop,
      ls_mpopx1         TYPE bapi_mpopx,
      ls_mpgd1          TYPE bapi_mpgd,
      ls_mpgdx1         TYPE bapi_mpgdx,
      ls_mard1          TYPE bapi_mard,
      ls_mardx1         TYPE bapi_mardx,
      ls_mbew1          TYPE bapi_mbew,
      ls_mbewx1         TYPE bapi_mbewx,
      ls_mlgn1          TYPE bapi_mlgn,
      ls_mlgnx1         TYPE bapi_mlgnx,
      ls_mvke1          TYPE bapi_mvke,
      ls_mvkex1         TYPE bapi_mvkex,
      ls_mlgt1          TYPE bapi_mlgt,
      ls_mlgtx1         TYPE bapi_mlgtx,
      ls_return1        TYPE bapiret2,
      ls_makt1          TYPE bapi_makt,
      ls_marm1          TYPE bapi_marm,
      ls_marmx1         TYPE bapi_marmx,
      lt_makt1          TYPE TABLE OF bapi_makt,
      lt_marm1          TYPE TABLE OF bapi_marm,
      lt_marmx1         TYPE TABLE OF bapi_marmx,
      ls_headdata       TYPE bapie1matheader,
      ls_mara           TYPE bapie1mara,
      ls_marax          TYPE bapie1marax,
      ls_marc           TYPE bapie1marc,
      ls_marcx          TYPE bapie1marcx,
      ls_mpop           TYPE bapie1mpop,
      ls_mpopx          TYPE bapie1mpopx,
      ls_mpgd           TYPE bapie1mpgd,
      ls_mpgdx          TYPE bapie1mpgdx,
      ls_mard           TYPE bapie1mard,
      ls_mardx          TYPE bapie1mardx,
      ls_mbew           TYPE bapie1mbew,
      ls_mbewx          TYPE bapie1mbewx,
      ls_mlgn           TYPE bapie1mlgn,
      ls_mlgnx          TYPE bapie1mlgnx,
      ls_mvke           TYPE bapie1mvke,
      ls_mvkex          TYPE bapie1mvkex,
      ls_mlgt           TYPE bapie1mlgt,
      ls_mlgtx          TYPE bapie1mlgtx,
      ls_return         TYPE bapiret2,
      lt_headdata       TYPE TABLE OF bapie1matheader,
      lt_mara           TYPE TABLE OF bapie1mara,
      lt_marax          TYPE TABLE OF bapie1marax,
      lt_marc           TYPE TABLE OF bapie1marc,
      lt_marcx          TYPE TABLE OF bapie1marcx,
      lt_mpop           TYPE TABLE OF bapie1mpop,
      lt_mpopx          TYPE TABLE OF bapie1mpopx,
      lt_mpgd           TYPE TABLE OF bapie1mpgd,
      lt_mpgdx          TYPE TABLE OF bapie1mpgdx,
      lt_mard           TYPE TABLE OF bapie1mard,
      lt_mardx          TYPE TABLE OF bapie1mardx,
      lt_mbew           TYPE TABLE OF bapie1mbew,
      lt_mbewx          TYPE TABLE OF bapie1mbewx,
      lt_mlgn           TYPE TABLE OF bapie1mlgn,
      lt_mlgnx          TYPE TABLE OF bapie1mlgnx,
      lt_mvke           TYPE TABLE OF bapie1mvke,
      lt_mvkex          TYPE TABLE OF bapie1mvkex,
      lt_mlgt           TYPE TABLE OF bapie1mlgt,
      lt_mlgtx          TYPE TABLE OF bapie1mlgtx,
      lt_return         TYPE TABLE OF bapiret2,
      lt_makt           TYPE TABLE OF bapie1makt,
      lt_marm           TYPE TABLE OF bapie1marm,
      lt_marmx          TYPE TABLE OF bapie1marmx,
      lt_mean           TYPE TABLE OF bapie1mean,
      lt_mltx           TYPE TABLE OF bapie1mltx,
      lt_mlan           TYPE TABLE OF bapie1mlan,
      lt_matreturn      TYPE TABLE OF bapie1matreturn2,
      lt_mfhm           TYPE TABLE OF bapie1mfhm,
      lt_mfhmx          TYPE TABLE OF bapie1mfhmx,
      ls_makt           TYPE bapie1makt,
      ls_marm           TYPE bapie1marm,
      ls_marmx          TYPE bapie1marmx,
      ls_material       TYPE ty_s_material,
      lv_iso_langu      TYPE laiso,
      ls_message        TYPE bapiret2,
      lv_deletion_flag  TYPE bapimatall-del_flag,
      ls_bapireturn1    TYPE bapireturn1,
      lv_material_check TYPE bapimatall-material,
      lv_check          TYPE boolean,
      lt_routings       TYPE tt_routing,
      ls_routing        TYPE ty_s_routing,
      lv_bom_nr         TYPE mast-stlnr,
      lv_bom_alt        TYPE mast-stlal,
      lt_stpo           TYPE TABLE OF stpo,
      ls_stpo           TYPE stpo,
      lt_mast           TYPE TABLE OF mast,
      ls_mast           TYPE mast,
      lt_mara_matnr     TYPE TABLE OF mara,
      ls_mara_matnr     TYPE mara.

    lt_routings = it_routing.
    SORT lt_routings BY material ASCENDING.
    DELETE ADJACENT DUPLICATES FROM lt_routings COMPARING material.

*    SELECT * FROM mast INTO TABLE lt_mast FOR ALL ENTRIES IN lt_routings WHERE
*                          matnr = lt_routings-material AND
*                          werks = lt_routings-plant." AND
**                          stlan = lt_routings-usage.     "#EC CI_NOORDER
*
*    SELECT * FROM stpo INTO TABLE lt_stpo FOR ALL ENTRIES IN lt_mast  WHERE stlnr = lt_mast-stlnr .
*
*    SORT lt_stpo BY idnrk ASCENDING .
*    DELETE ADJACENT DUPLICATES FROM lt_stpo.
*    SELECT * FROM mara INTO TABLE lt_mara_matnr FOR ALL ENTRIES IN lt_stpo WHERE matnr = lt_stpo-idnrk AND mtart IN ('FERT', 'SERV').
*
*    DELETE lt_mara_matnr WHERE mtart <> 'FERT' OR mtart <> 'SERV'.


    LOOP AT lt_routings INTO ls_routing .

      CLEAR: ls_headdata1, ls_makt1,ls_mara1,ls_marax1,ls_marc1, ls_marcx1,ls_mard1, ls_mardx1,ls_marm1, ls_marmx1,ls_mbew1 , ls_mbewx1,
             ls_mlgn1, ls_mlgnx1, ls_mlgt1 , ls_mlgtx1, ls_mpgd1 , ls_mpgdx1, ls_mpop1 , ls_mpopx1, ls_mvke1, ls_mvkex1, lt_marm1, lt_makt1, ls_return1,
             lv_material_check.

* Fill HEADDATA structure
      ls_headdata1-material = ls_routing-material.
      ls_headdata1-matl_type = 'FERT'."ls_mara_matnr-mtart.
      ls_headdata1-material_long =  ls_routing-material.
      ls_headdata1-ind_sector = 'M'.
*          ls_headdata1-basic_view = abap_true.
*          ls_headdata1-sales_view = abap_false.
*          ls_headdata1-purchase_view = abap_true.
*          ls_headdata1-mrp_view = abap_true.
*          ls_headdata1-forecast_view = abap_true.
*          ls_headdata1-work_sched_view = abap_true.
*          ls_headdata1-prt_view = abap_true.
*          ls_headdata1-storage_view = abap_true.
*          ls_headdata1-warehouse_view = abap_true.
*          ls_headdata1-quality_view = abap_true.
*          ls_headdata1-account_view = abap_true.
*          ls_headdata1-cost_view = abap_true.
*
*        APPEND ls_headdata TO lt_headdata.
*
* Fill MARC structure
      ls_marc1-plant = '1710'."ls_material-plant .
*          ls_marc1-availcheck = ls_material-availabilitycheck.
*          ls_marc1-loadinggrp = ls_material-loadinggroup.
*          ls_marc1-profit_ctr = ls_material-profitcenter.
*          ls_marc1-mrp_type = ls_material-mrptype .
*          ls_marc1-mrp_ctrler = ls_material-mrpcontroller .
*          ls_marc1-lotsizekey = ls_material-lotsize.
*          ls_marc1-proc_type = ls_material-procurementtype.
      ls_marc1-iss_st_loc = '171A'."ls_material-prodstoragelocation.
*          ls_marc1-inhseprodt = ls_material-inhouseproduction.
*          ls_marc1-period_ind = ls_material-periodindicator.
*          ls_marc1-plan_strgp = ls_material-strategygroup .
*          ls_marc1-consummode = ls_material-consumptionmode.
*          ls_marc1-fwd_cons = ls_material-forwardconsumptionperiod.
*          ls_marc1-bwd_cons = ls_material-backwardconsumptionperiod.
*          ls_marc1-replentime = ls_material-totalreplenishment.
*          ls_marc1-production_scheduler = ls_material-productionsupervisor.
*          ls_marc1-prodprof = ls_material-productionschedulingprofile.
*          ls_marc1-variance_key = ls_material-variancekey .
*          ls_marc1-lot_size = ls_material-costinglotsize.

      ls_marc1-prodverscs = abap_true.
      ls_marcx1-prodverscs = abap_true.
* Fill MARCX structure
*
      ls_marcx1-plant = '1710'."ls_material-plant.
*          IF ls_marc1-availcheck IS NOT INITIAL.
*            ls_marcx1-availcheck = abap_true.
*          ENDIF.
*
*          IF ls_marc1-loadinggrp IS NOT INITIAL.
*            ls_marcx1-loadinggrp = abap_true.
*          ENDIF.
*
*          IF ls_marc1-profit_ctr IS NOT INITIAL.
*            ls_marcx1-profit_ctr = abap_true.
*          ENDIF.
*
*          IF ls_marc1-mrp_type IS NOT  INITIAL.
*            ls_marcx1-mrp_type = abap_true.
*          ENDIF.
*
*          IF ls_marc1-mrp_ctrler IS NOT INITIAL.
*            ls_marcx1-mrp_ctrler = abap_true.
*          ENDIF.
*
*          IF ls_marc1-lotsizekey IS NOT INITIAL.
*            ls_marcx1-lotsizekey = abap_true.
*          ENDIF.
*
*          IF ls_marc1-proc_type IS NOT INITIAL.
*            ls_marcx1-proc_type = abap_true.
*          ENDIF.
*
*          IF ls_marc1-inhseprodt IS NOT INITIAL.
*            ls_marcx1-inhseprodt = abap_true.
*          ENDIF.
*
      IF ls_marc1-iss_st_loc IS NOT INITIAL.
        ls_marcx1-iss_st_loc = abap_true.
      ENDIF.
*
*          IF ls_marc1-period_ind IS NOT INITIAL.
*            ls_marcx1-period_ind = abap_true.
*          ENDIF.
*
*          IF ls_marc1-plan_strgp IS  NOT  INITIAL.
*            ls_marcx1-plan_strgp = abap_true.
*          ENDIF.
*
*          IF ls_marc1-consummode IS NOT INITIAL.
*            ls_marcx1-consummode = abap_true.
*          ENDIF.
*
*          IF ls_marc1-fwd_cons IS NOT INITIAL.
*            ls_marcx1-fwd_cons = abap_true.
*          ENDIF.
*
*          IF ls_marc1-bwd_cons IS NOT INITIAL.
*            ls_marcx1-bwd_cons = abap_true.
*          ENDIF.
*
*          IF ls_marc1-replentime IS  NOT INITIAL.
*            ls_marcx1-replentime = abap_true.
*          ENDIF.
*
*          IF  ls_marc1-production_scheduler IS NOT INITIAL.
*            ls_marcx1-production_scheduler = abap_true.
*          ENDIF.
*
*          IF ls_marc1-prodprof IS NOT INITIAL.
*            ls_marcx1-prodprof = abap_true.
*          ENDIF.
*
*          IF ls_marc1-variance_key IS NOT INITIAL.
*            ls_marcx1-variance_key = abap_true.
*          ENDIF.
*
*          IF  ls_marc1-lot_size IS NOT INITIAL.
*            ls_marcx1-lot_size = abap_true.
*          ENDIF.
*
* Fill MARD structure
      ls_mard1-stge_loc = '171A'."ls_material-storagelocation.
      ls_mard1-plant = '1710'.""ls_material-plant.
*
* Fill MARDX structure
      ls_mardx1-stge_loc = '171A'."ls_material-storagelocation.
      ls_mardx1-plant = '1710'."ls_material-plant.
*
* Fill MBEW structure
*          ls_mbew1-val_class = ls_material-valuationclass .
*          ls_mbew1-val_area = ls_material-plant .
*          ls_mbew1-ml_active = abap_true.
*          ls_mbew1-std_price = ls_material-standardprice .
*          ls_mbew1-price_unit = ls_material-priceunit.
*          ls_mbew1-price_ctrl = ls_material-pricecontrol.
*          ls_mbew1-commprice1 = ls_material-commercialprice1.
*          ls_mbew1-qty_struct = abap_true.
*
** Fill MBEWX structure
*      ls_mbewx1-val_class = abap_true.
*      ls_mbewx1-val_area = ls_material-plant.
*      ls_mbewx1-ml_active = abap_true.
*      ls_mbewx1-price_unit = abap_true.
*      ls_mbewx1-price_ctrl = abap_true.
*      ls_mbewx1-std_price = abap_true.
*      ls_mbewx1-commprice1 = abap_true.
*      ls_mbewx1-qty_struct = abap_true.
*
** Fill MVKE structure
*      ls_mvke1-sales_org = ls_material-salesorg.
*      ls_mvke1-distr_chan = ls_material-distchan.
*      ls_mvke1-delyg_plnt = ls_material-deliveringplant.
*      ls_mvke1-cash_disc = abap_true.
*      ls_mvke1-matl_stats = ls_material-materialstatisticsgroup .
*      ls_mvke1-acct_assgt = ls_material-accountassignmentgroup.
*      ls_mvke1-item_cat = ls_material-itemcategorygroup.
*      ls_mvke1-prod_hier = ls_material-prodhierarchy.
*
** Fill MVKEX structure
*      IF  ls_mvke1-sales_org IS NOT INITIAL.
*        ls_mvkex1-sales_org =  ls_material-salesorg.
*      ENDIF.
*
*      IF ls_mvke1-distr_chan IS NOT INITIAL.
*        ls_mvkex1-distr_chan =  ls_material-distchan.
*      ENDIF.
*
*      ls_mvkex1-delyg_plnt =  abap_true.
*      ls_mvkex1-cash_disc = abap_true.
*      ls_mvkex1-matl_stats =  abap_true.
*      ls_mvkex1-acct_assgt =  abap_true .
*      ls_mvkex1-item_cat =  abap_true.
*      ls_mvkex1-prod_hier = abap_true.
*
** Fill MARA structure
*      CALL FUNCTION 'CONVERSION_EXIT_CUNIT_INPUT'
*        EXPORTING
*          input          = ls_material-baseunitofmeasurement
*          language       = sy-langu
*        IMPORTING
*          output         = ls_mara1-base_uom
*        EXCEPTIONS
*          unit_not_found = 1
*          OTHERS         = 2.
*
*      ls_mara1-base_uom_iso = 'HUR'.
*      ls_mara1-matl_group = ls_material-materialgroup.
*      ls_mara1-item_cat = ls_material-generalitemcategorygroup.
*      ls_mara1-net_weight = ls_material-netweight.
*      ls_mara1-unit_of_wt = ls_material-unitofweight.
*      ls_mara1-trans_grp = ls_material-transportationgroup.
*      ls_mara1-period_ind_expiration_date = ls_material-periodindicatorforshelflige.
*
** Fill MARAX structure
*      IF ls_mara1-base_uom IS NOT INITIAL.
*        ls_marax1-base_uom = abap_true.
*      ENDIF.
*
*      IF ls_mara1-base_uom_iso IS NOT INITIAL.
*        ls_marax1-base_uom_iso = abap_true.
*      ENDIF.
*
*      IF ls_mara1-matl_group IS NOT INITIAL.
*        ls_marax1-matl_group = abap_true.
*      ENDIF.
*
*      IF ls_mara1-item_cat IS   NOT INITIAL.
*        ls_marax1-item_cat = abap_true.
*      ENDIF.
*
*      IF ls_mara1-net_weight IS NOT INITIAL.
*        ls_marax1-net_weight = abap_true.
*      ENDIF.
*
*      IF ls_mara1-unit_of_wt IS NOT INITIAL.
*        ls_marax1-unit_of_wt = abap_true.
*      ENDIF.
*
*      IF ls_mara1-trans_grp IS NOT INITIAL.
*        ls_marax1-trans_grp = abap_true.
*      ENDIF.
*
*      IF ls_mara1-period_ind_expiration_date IS NOT INITIAL.
*        ls_marax1-period_ind_expiration_date = abap_true.
*      ENDIF.
*
** Fill MAKT table
*      lv_iso_langu = sy-langu.
*      ls_makt1-langu = cl_srt_wsp_helper_methods=>convert_iso_lang_to_sap_lang( iso_lang_code =  lv_iso_langu ).
*      ls_makt1-langu_iso = sy-langu.
*      ls_makt1-matl_desc =  ls_material-description.
*      APPEND ls_makt1 TO lt_makt1.
*
** Fill MARM table
*      ls_marm1-alt_unit = ls_mara-base_uom.
*      ls_marm1-alt_unit_iso = ls_mara-base_uom.
*      ls_marm1-numerator =  1.
*      ls_marm1-denominatr = 1.
*      ls_marm1-gross_wt = ls_material-grossweight.
*      ls_marm1-volume = ls_material-volume.
*      APPEND ls_marm1 TO lt_marm1.


      CALL FUNCTION 'BAPI_MATERIAL_SAVEDATA'
        EXPORTING
          headdata             = ls_headdata1
*         clientdata           = ls_mara1
*         clientdatax          = ls_marax1
          plantdata            = ls_marc1
          plantdatax           = ls_marcx1
*         forecastparameters   = ls_mpop1
*         forecastparametersx  = ls_mpopx1
*         planningdata         = ls_mpgd1
*         planningdatax        = ls_mpgdx1
          storagelocationdata  = ls_mard1
          storagelocationdatax = ls_mardx1
*         valuationdata        = ls_mbew1
*         valuationdatax       = ls_mbewx1
*         warehousenumberdata  = ls_mlgn1
*         warehousenumberdatax = ls_mlgnx1
*         salesdata            = ls_mvke1
*         salesdatax           = ls_mvkex1
*         storagetypedata      = ls_mlgt1
*         storagetypedatax     = ls_mlgtx1
        IMPORTING
          return               = ls_return1
        TABLES
          materialdescription  = lt_makt1
          unitsofmeasure       = lt_marm1.


      IF ls_return1-type = cl_esh_adm_constants=>gc_msgty_e OR ls_return1-type = cl_esh_adm_constants=>gc_msgty_a.

        ev_error = abap_true.

        ls_message-type = ls_return1-type.
        ls_message-id = z_cl_dataload=>gc_message_class.
        ls_message-number = '030'.

        CONCATENATE gc_material  ls_routing-material INTO ls_message-message_v1 SEPARATED BY space.
        IF strlen( ls_return1-message ) > 50.
          ls_message-message_v2 = ls_return1-message+0(50).
          ls_message-message_v3 = ls_return1-message+50(50).
          ls_message-message_v4 = ls_return1-message+100(50).
        ELSE.
          ls_message-message_v2 = ls_return1-message.
        ENDIF.

        zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).
      ENDIF.

    ENDLOOP.


*    ls_message-id = gc_message_class.
*    ls_message-number = '010'.
*    ls_message-type = cl_esh_adm_constants=>gc_msgty_s.
*    ls_message-message_v1 = gc_material.
*
*    zcl_dataload_message_buffer=>add_from_bapiret2( is_return = ls_message ).





  ENDMETHOD.
ENDCLASS.