CLASS zcson_cl_ioc_container DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC.

  PUBLIC SECTION.
    TYPES:
      ty_v_scope TYPE i.

    CONSTANTS:
      BEGIN OF gc_scope,
        transient TYPE ty_v_scope VALUE 0,
        singleton TYPE ty_v_scope VALUE 1,
      END OF gc_scope,
      BEGIN OF gc_ioc_cx_msg,
        class TYPE msgid VALUE 'ZAS_MESSAGES',
        BEGIN OF nr,
          not_found        TYPE symsgno VALUE '000',
          already_reg      TYPE symsgno VALUE '001',
          method_not_found TYPE symsgno VALUE '002',
        END OF nr,
      END OF gc_ioc_cx_msg.

    METHODS:
      constructor
        IMPORTING
          ir_loader TYPE REF TO zcson_if_ioc_auto_loader,
      register
        IMPORTING
          iv_contract    TYPE string
          iv_implementer TYPE string OPTIONAL
          iv_scope       TYPE i DEFAULT zcson_cl_ioc_container=>gc_scope-transient
        RAISING
          zas_cx_ioc,
      resolve
        IMPORTING
          iv_contract           TYPE string
        RETURNING
          VALUE(rr_implementer) TYPE REF TO object
        RAISING
          zas_cx_ioc,
      is_contract_registered
        IMPORTING
          iv_contract       TYPE string
        RETURNING
          VALUE(rf_already) TYPE abap_bool.

  PROTECTED SECTION.
  PRIVATE SECTION.
    TYPES:
      BEGIN OF ty_s_entry,
        contract    TYPE string,
        implementer TYPE string,
        scope       TYPE i,
        instance    TYPE REF TO object,
      END OF ty_s_entry,
      ty_t_dictionary TYPE STANDARD TABLE OF ty_s_entry WITH KEY contract.

    DATA:
      mt_dictionary  TYPE ty_t_dictionary,
      mr_auto_loader TYPE REF TO zcson_if_ioc_auto_loader.

    METHODS:
      check_contract_registered
        IMPORTING
          iv_contract TYPE string
          if_already  TYPE abap_bool
        RAISING
          zas_cx_ioc,
      resolve_transient
        IMPORTING
          iv_contract      TYPE string
        RETURNING
          VALUE(rr_object) TYPE REF TO object
        RAISING
          zas_cx_ioc,
      resolve_singleton
        IMPORTING
          iv_contract      TYPE string
        RETURNING
          VALUE(rr_object) TYPE REF TO object
        RAISING
          zas_cx_ioc,
      get_constructor_params
        IMPORTING
          iv_class_name                TYPE string
        RETURNING
          VALUE(rt_constructor_params) TYPE abap_parmbind_tab
        RAISING
          zas_cx_ioc,
      get_singleton_method
        IMPORTING
          iv_classname     TYPE string
        RETURNING
          VALUE(rs_method) TYPE abap_methdescr,
      bind_auto_classes.

ENDCLASS.



CLASS zcson_cl_ioc_container IMPLEMENTATION.

  METHOD constructor.
*&---------------------------------------------------------------------*
*& Date:        18.09.2017
*&---------------------------------------------------------------------*
*& Description: Ctor for the IoC Container.
*&---------------------------------------------------------------------*

    me->mr_auto_loader = ir_loader.
    me->bind_auto_classes( ).

  ENDMETHOD.

  METHOD register.
*&---------------------------------------------------------------------*
*& Date:        18.09.2017
*&---------------------------------------------------------------------*
*& Description: Register a contract together with its implementer to
*&              IoC container.
*&---------------------------------------------------------------------*
    DATA: lv_contract    TYPE string,
          lv_implementer TYPE string.
*&---------------------------------------------------------------------*

    check_contract_registered(
      iv_contract = iv_contract
      if_already  = abap_true ).

    lv_contract = |{ iv_contract CASE = UPPER }|.

    IF iv_implementer IS INITIAL.
      lv_implementer = lv_contract.
    ELSE.
      lv_implementer = |{ iv_implementer CASE = UPPER }|.
    ENDIF.

    APPEND INITIAL LINE TO mt_dictionary ASSIGNING FIELD-SYMBOL(<ls_entry>).
    <ls_entry>-contract = lv_contract.
    <ls_entry>-implementer = lv_implementer.
    <ls_entry>-scope = iv_scope.

  ENDMETHOD.

  METHOD resolve.
*&---------------------------------------------------------------------*
*& Date:        18.09.2017
*&---------------------------------------------------------------------*
*& Description: Retrieve the implementation of a specific contract.
*&---------------------------------------------------------------------*
    DATA: lv_contract TYPE string.
*&---------------------------------------------------------------------*

    check_contract_registered(
      iv_contract = iv_contract
      if_already  = abap_false ).

    lv_contract = |{ iv_contract CASE = UPPER }|.

    ASSIGN mt_dictionary[ contract = lv_contract ] TO FIELD-SYMBOL(<ls_entry>).
    IF <ls_entry>-instance IS BOUND.
      rr_implementer = <ls_entry>-instance.
      RETURN.
    ENDIF.

    IF <ls_entry>-scope = gc_scope-singleton.
      <ls_entry>-instance = resolve_singleton( lv_contract ).
      rr_implementer = <ls_entry>-instance.
    ELSE.
      TRY.
          rr_implementer = resolve_transient( lv_contract ).
        CATCH cx_sy_no_handler.
          " In case normal instantiation fails, treat it as
          " a singleton.
          rr_implementer = resolve_singleton( lv_contract ).
      ENDTRY.
    ENDIF.

  ENDMETHOD.

  METHOD is_contract_registered.
*&---------------------------------------------------------------------*
*& Date:        18.09.2017
*&---------------------------------------------------------------------*
*& Description: Was the contract already registered in the container?
*&---------------------------------------------------------------------*

    rf_already = abap_false.

    TRY.
        me->check_contract_registered(
          iv_contract = iv_contract
          if_already  = abap_true ).
      CATCH zas_cx_ioc.
        rf_already = abap_true.
    ENDTRY.

  ENDMETHOD.

  METHOD check_contract_registered.
*&---------------------------------------------------------------------*
*& Date:        18.09.2017
*&---------------------------------------------------------------------*
*& Description: Check if a contract has already been registered.
*&---------------------------------------------------------------------*
    DATA: lv_contract TYPE string,
          lf_exists   TYPE abap_bool,
          lv_msgno    TYPE symsgno.
*&---------------------------------------------------------------------*

    lv_contract = |{ iv_contract CASE = UPPER }|.

    IF line_exists( mt_dictionary[ contract = lv_contract ] ).
      lf_exists = abap_true.
    ELSE.
      lf_exists = abap_false.
    ENDIF.

    IF if_already = abap_true.
      lv_msgno = gc_ioc_cx_msg-nr-already_reg.
    ELSE.
      lv_msgno = gc_ioc_cx_msg-nr-not_found.
    ENDIF.

    IF lf_exists = abap_true AND if_already = abap_true OR
       lf_exists = abap_false AND if_already = abap_false.
      RAISE EXCEPTION TYPE zas_cx_ioc
        EXPORTING
          textid = VALUE #(
            msgid = gc_ioc_cx_msg-class
            msgno = lv_msgno
            attr1 = lv_contract ).
    ENDIF.

  ENDMETHOD.

  METHOD resolve_transient.
*&---------------------------------------------------------------------*
*& Date:        18.09.2017
*&---------------------------------------------------------------------*
*& Description: Handle the instantiation of a transient object.
*&---------------------------------------------------------------------*
    FIELD-SYMBOLS: <lv_implementer> TYPE string.
*&---------------------------------------------------------------------*

    ASSIGN mt_dictionary[ contract = iv_contract ]-implementer TO <lv_implementer>.
    IF <lv_implementer> IS NOT ASSIGNED.
      RETURN.
    ENDIF.

    DATA(lt_constructor_params) = get_constructor_params( <lv_implementer> ).
    IF lt_constructor_params IS INITIAL.
      CREATE OBJECT rr_object TYPE (<lv_implementer>).
    ELSE.
      CREATE OBJECT rr_object TYPE (<lv_implementer>)
        PARAMETER-TABLE lt_constructor_params.
    ENDIF.

  ENDMETHOD.

  METHOD resolve_singleton.
*&---------------------------------------------------------------------*
*& Date:        18.09.2017
*&---------------------------------------------------------------------*
*& Description: Handle the instantiation of a singleton object.
*&---------------------------------------------------------------------*
    DATA: lt_param TYPE abap_parmbind_tab,
          ls_param TYPE abap_parmbind.

    FIELD-SYMBOLS: <lv_implementer> TYPE string.
*&---------------------------------------------------------------------*

    ASSIGN mt_dictionary[ contract = iv_contract ]-implementer TO <lv_implementer>.
    IF <lv_implementer> IS NOT ASSIGNED.
      RETURN.
    ENDIF.

    DATA(ls_method) = get_singleton_method( <lv_implementer> ).

    IF ls_method IS INITIAL.
      RAISE EXCEPTION TYPE zas_cx_ioc
        EXPORTING
          textid = VALUE #(
            msgid = gc_ioc_cx_msg-class
            msgno = gc_ioc_cx_msg-nr-method_not_found ).
    ENDIF.

    ls_param-name = ls_method-parameters[ 1 ]-name.
    ls_param-kind = cl_abap_objectdescr=>receiving.
    ls_param-value = REF #( rr_object ).

    INSERT ls_param INTO TABLE lt_param.

    CALL METHOD (<lv_implementer>)=>(ls_method-name)
      PARAMETER-TABLE lt_param.

  ENDMETHOD.

  METHOD get_constructor_params.
*&---------------------------------------------------------------------*
*& Date:        18.09.2017
*&---------------------------------------------------------------------*
*& Description: Resolve the constructor parameters returning a table
*&              which can be used to directly instantiate a given object.
*&---------------------------------------------------------------------*
    DATA: lr_object_descr TYPE REF TO cl_abap_objectdescr,
          ls_param_bind   TYPE abap_parmbind,
          lr_ref_descr    TYPE REF TO cl_abap_refdescr,
          lv_param_type   TYPE string,
          lr_constructor  TYPE REF TO abap_methdescr.
*&---------------------------------------------------------------------*

    lr_object_descr ?= cl_abap_objectdescr=>describe_by_name( iv_class_name ).

    READ TABLE lr_object_descr->methods REFERENCE INTO lr_constructor
      WITH KEY name = 'CONSTRUCTOR'.

    IF lr_constructor IS NOT BOUND.
      RETURN.
    ENDIF.

    " Attempt to inject the dependencies of the object (specified in constructor)
    LOOP AT lr_constructor->parameters ASSIGNING FIELD-SYMBOL(<ls_param>).
      " TODO: Add support for other data types (new method to register them)
      IF <ls_param>-parm_kind <> cl_abap_objectdescr=>importing OR
         <ls_param>-type_kind <> cl_abap_objectdescr=>typekind_oref.
        CONTINUE.
      ENDIF.
      " The dependency must already be registered in the container.
      ASSERT line_exists( mt_dictionary[ implementer = <ls_param>-name ] ).

      ls_param_bind-name = <ls_param>-name.
      ls_param_bind-kind = cl_abap_objectdescr=>exporting.

      lr_ref_descr ?= lr_object_descr->get_method_parameter_type(
                        p_method_name    = lr_constructor->name
                        p_parameter_name = <ls_param>-name ).

      CREATE DATA ls_param_bind-value TYPE HANDLE lr_ref_descr.
      ASSIGN ls_param_bind-value->* TO FIELD-SYMBOL(<lv_param>).

      lv_param_type = lr_ref_descr->get_referenced_type( )->absolute_name.
      <lv_param> = resolve( lv_param_type ).

      INSERT ls_param_bind INTO TABLE rt_constructor_params.
    ENDLOOP.

  ENDMETHOD.

  METHOD get_singleton_method.
*&---------------------------------------------------------------------*
*& Date:        18.09.2017
*&---------------------------------------------------------------------*
*& Description: Attempt to find the method used to retrieve the instance
*&              of a given object.
*&---------------------------------------------------------------------*
    DATA: lv_classname        TYPE string,
          lr_obj_descriptor   TYPE REF TO cl_abap_objectdescr,
          lr_singleton_method TYPE REF TO abap_methdescr,
          lr_param_descr      TYPE REF TO cl_abap_refdescr,
          lv_class_param      TYPE abap_classname.
*&---------------------------------------------------------------------*

    lv_classname = |{ iv_classname }|.
    lr_obj_descriptor ?= cl_abap_objectdescr=>describe_by_name( lv_classname ).

    READ TABLE lr_obj_descriptor->methods REFERENCE INTO lr_singleton_method
      WITH KEY name = 'GET_INSTANCE'.

    IF lr_singleton_method IS BOUND AND
       lr_singleton_method->is_class = abap_true.
      rs_method = lr_singleton_method->*.
      RETURN.
    ENDIF.

    lv_class_param = |\\CLASS={ lv_classname }|.

    LOOP AT lr_obj_descriptor->methods ASSIGNING FIELD-SYMBOL(<ls_method>)
      WHERE is_class = abap_true.
      LOOP AT <ls_method>-parameters ASSIGNING FIELD-SYMBOL(<ls_param>)
        WHERE parm_kind = cl_abap_objectdescr=>returning AND
              type_kind = cl_abap_objectdescr=>typekind_oref.
        lr_param_descr ?= lr_obj_descriptor->get_method_parameter_type(
                            p_method_name    = <ls_method>-name
                            p_parameter_name = <ls_param>-name ).
        IF lr_param_descr IS NOT BOUND.
          CONTINUE.
        ENDIF.
        " If the type of the parameter matches the class name, the method is found
        " TODO: Handle interfaces/super-classes (low priority)
        IF lr_param_descr->get_referenced_type( )->absolute_name = lv_class_param.
          rs_method = <ls_method>.
          RETURN.
        ENDIF.
      ENDLOOP.
    ENDLOOP.

  ENDMETHOD.

  METHOD bind_auto_classes.
*&---------------------------------------------------------------------*
*& Date:        08.12.2017
*&---------------------------------------------------------------------*
*& Description:
*&---------------------------------------------------------------------*
    DATA: lr_classdescr TYPE REF TO cl_abap_classdescr,
          lv_scope      TYPE ty_v_scope.
*&---------------------------------------------------------------------*

    mr_auto_loader->get_registrations(
      IMPORTING
        et_regs = DATA(lt_class_names) ).

    LOOP AT lt_class_names ASSIGNING FIELD-SYMBOL(<lv_class>).
      lr_classdescr ?= cl_abap_classdescr=>describe_by_name( <lv_class> ).
      IF lr_classdescr IS NOT BOUND OR
         lr_classdescr->is_instantiatable( ) = abap_false.
        CONTINUE.
      ENDIF.
      IF lr_classdescr->create_visibility = cl_abap_objectdescr=>public.
        lv_scope = zif_ioc_container=>gc_scope-transient.
      ELSE.
        lv_scope = zif_ioc_container=>gc_scope-singleton.
      ENDIF.
      TRY.
          me->register(
            iv_contract    = <lv_class>
            iv_implementer = <lv_class>
            iv_scope       = lv_scope ).
        CATCH zas_cx_ioc.
      ENDTRY.
      CLEAR lr_classdescr.
    ENDLOOP.

  ENDMETHOD.

ENDCLASS.