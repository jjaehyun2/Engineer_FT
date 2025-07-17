class /ENSX/CL_XSLT_BASE_RENDERER definition
  public
  create public .

public section.

  interfaces /ENSX/IF_XSLT_RENDERER .

  aliases GT_SOURCEBIND
    for /ENSX/IF_XSLT_RENDERER~GT_SOURCEBIND .

  types:
    BEGIN OF ty_ctxelem,
                        typeno          TYPE n LENGTH 3,
                        elemno          TYPE i,
                        level           TYPE i,
                        name            TYPE string,
                        nsprefix        TYPE string,
                        nsuri           TYPE string,
                        compname        TYPE fieldname,
                        editelem        TYPE swfdname,
                        datatype        TYPE domname,
                        complextypeno   TYPE n LENGTH 3,
                        complextypename TYPE domname,
                        istable         TYPE xfeld,
                        isoptional      TYPE xfeld,
                        isimport        TYPE xfeld,
                        isexport        TYPE xfeld,
                      END OF ty_ctxelem .
  types:
    ty_ctxelem_tab TYPE STANDARD TABLE OF ty_ctxelem WITH DEFAULT KEY .
  types:
    BEGIN OF ty_nsbinding,
                         nsuri    TYPE string,
                         nsprefix TYPE char10,
                       END OF ty_nsbinding .
  types:
    ty_nsbind_tab  TYPE HASHED TABLE OF ty_nsbinding WITH UNIQUE KEY nsuri .
  types:
    ty_string_tab TYPE STANDARD TABLE OF string WITH DEFAULT KEY .
  types TY_TRANS_SRCNAME type STRING .
  types:
    BEGIN OF ty_trans_srcbind,
        name  TYPE ty_trans_srcname,
        value TYPE REF TO data,
        skip  type boole_d,
        flatten type boole_d,
      END OF ty_trans_srcbind .
  types:
    ty_trans_srcbind_tab
           TYPE STANDARD TABLE OF ty_trans_srcbind WITH KEY name .

  constants CO_ATTR_EXPORT type STRING value 'isExport'. "#EC NOTEXT
  constants CO_ATTR_GUID type STRING value 'guid'. "#EC NOTEXT
  constants CO_ATTR_ID type STRING value 'id'. "#EC NOTEXT
  constants CO_ATTR_IMPORT type STRING value 'isImport'. "#EC NOTEXT
  constants CO_ATTR_LABEL type STRING value 'label'. "#EC NOTEXT
  constants CO_ATTR_MAXOCCURS type STRING value 'maxOccurs'. "#EC NOTEXT
  constants CO_ATTR_MINOCCURS type STRING value 'minOccurs'. "#EC NOTEXT
  constants CO_ATTR_NAME type STRING value 'name'. "#EC NOTEXT
  constants CO_ATTR_TYPE type STRING value 'type'. "#EC NOTEXT
  constants CO_ATTR_VERSION type STRING value 'version'. "#EC NOTEXT
  constants CO_CNT_SYSELEM_UC type SWFDNAME value '_GP_GENERATEDOBJECTS'. "#EC NOTEXT
  constants CO_GEN_NAMESPACE type CHAR10 value '/1SWFGP/'. "#EC NOTEXT
  constants CO_NS_GPDEF type STRING value 'http://www.sap.com/bc/bmt/wfm/gp/process-definition'. "#EC NOTEXT
  constants CO_NS_XMLSCHEMA type STRING value 'http://www.w3.org/2001/XMLSchema'. "#EC NOTEXT
  constants CO_TAG_COMPLEX type STRING value 'complexType'. "#EC NOTEXT
  constants CO_TAG_ELEMENT type STRING value 'element'. "#EC NOTEXT
  constants CO_TAG_INITIALVAL type STRING value 'initialValue'. "#EC NOTEXT
  constants CO_TAG_PROCESS type STRING value 'process'. "#EC NOTEXT
  constants CO_TAG_SEQUENCE type STRING value 'sequence'. "#EC NOTEXT
  constants CO_TAG_STRUCTURE type STRING value 'structure'. "#EC NOTEXT
  data MT_COMMENTS type TY_STRING_TAB .
  data MT_CTXELEM type TY_CTXELEM_TAB .
  data MT_MESSAGES type SWD_TERROR .
  data MT_NSBINDING type TY_NSBIND_TAB .
  data M_GPAC_KEY type SWFGPACKEY .
  data M_OBJNAME type STRING .
  data M_REUSE type BOOLE_D value SPACE. "#EC NOTEXT .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . " .
  data M_SHORTTEXT type STRING .

  methods __CHECK_FLATTEN_CONDITION
    importing
      !FLATTEN type BOOLE_D
      !NAME type STRING
    returning
      value(DO_FLATTEN) type BOOLE_D .
  methods _ADD_BOOLEAN_ELEMENT
    importing
      !NAME type STRING
      !PATH type STRING
      !ATTRIBUTE_NAME type STRING
      !IS_TABLE_LINE type BOOLE_D
      !TYPE type STRING
      !IS_FUNNY type BOOLE_D
      !IS_RELATIVE type BOOLE_D optional
    changing
      !XSLT type STRING .
  methods _ADD_SIMPLE_ELEMENT
    importing
      !NAME type STRING
      !PATH type STRING
      !ATTRIBUTE_NAME type STRING
      !IS_TABLE_LINE type BOOLE_D
      !TYPE type STRING
      !IS_FUNNY type BOOLE_D
      !IS_RELATIVE type BOOLE_D optional
    changing
      !XSLT type STRING .
  methods _ADD_STRUCTURE_ELEMENT_END
    importing
      !NAME type STRING
      !PATH type STRING
      !ATTRIBUTE_NAME type STRING
      !IS_TABLE_LINE type BOOLE_D
    changing
      !XSLT type STRING .
  methods _ADD_STRUCTURE_ELEMENT_START
    importing
      !NAME type STRING
      !PATH type STRING
      !ATTRIBUTE_NAME type STRING
      !IS_TABLE_LINE type BOOLE_D
    changing
      !XSLT type STRING .
  methods _ADD_TABLE_ELEMENT_END
    importing
      !NAME type STRING
      !PATH type STRING
      !ATTRIBUTE_NAME type STRING
      !IS_TABLE_LINE type BOOLE_D
    changing
      !XSLT type STRING .
  methods _ADD_TABLE_ELEMENT_START
    importing
      !NAME type STRING
      !PATH type STRING
      !ATTRIBUTE_NAME type STRING
      !IS_TABLE_LINE type BOOLE_D
    changing
      !XSLT type STRING .
  methods _ADD_TABLE_INDEX
    importing
      !NAME type STRING
      !PATH type STRING
      !ATTRIBUTE_NAME type STRING
      !IS_TABLE_LINE type BOOLE_D
      !TYPE type STRING
    changing
      !XSLT type STRING .
  methods CONSTRUCTOR .
  methods _GET_ELEMENT_NAME
    importing
      !TYPEDESCR type ref to CL_ABAP_TYPEDESCR
      !PATH type STRING optional
      !IS_TABLE_LINE type BOOLE_D optional
    returning
      value(NAME) type STRING
    raising
      /ENSX/CX_XSLT .
  methods _DO_FOOTER
    changing
      !XSLT type STRING .
  methods _DO_HEADER
    changing
      !XSLT type STRING .
  methods _DO_SKIP_START
    importing
      !ROOT type STRING
      !DATATYPE type CHAR30 optional
    changing
      !XSLT type STRING .
  methods _DO_SKIP_END
    importing
      !ROOT type STRING
      !DATATYPE type CHAR30 optional
    changing
      !XSLT type STRING .
  methods _DO_SERIALIZE_START
    importing
      !ROOT type STRING
      !DATATYPE type CHAR30 optional
    changing
      !XSLT type STRING .
  methods _DO_SERIALIZE_END
    importing
      !ROOT type STRING
      !DATATYPE type CHAR30 optional
    changing
      !XSLT type STRING .
  methods _DO_OBJECT_END
    importing
      !ROOT type STRING
      !DATATYPE type CHAR30 optional
    changing
      !XSLT type STRING .
  methods _DO_OBJECT_START
    importing
      !ROOT type STRING
      !DATATYPE type CHAR30 optional
    changing
      !XSLT type STRING .
  methods _DO_OBJECT_COMMENT
    importing
      !ROOT type STRING
      !DATATYPE type CHAR30 optional
    changing
      !XSLT type STRING .
  methods _DO_ROOTS
    importing
      !ROOT type STRING
      !DATATYPE type CHAR30 optional
    changing
      !XSLT type STRING .
  methods _DO_TEMPLATE_START
    changing
      !XSLT type STRING .
  methods _DESCRIBE
    importing
      !NAME type STRING optional
      !DREF type ref to DATA
      !TYPEDESCR type ref to CL_ABAP_TYPEDESCR
      !PATH type STRING
      !IS_TABLE_LINE type BOOLE_D optional
      !IS_FUNNY type BOOLE_D optional
      !IS_RELATIVE type BOOLE_D optional
      !FLATTEN type BOOLE_D optional
    changing
      !XSLT type STRING
    raising
      /ENSX/CX_XSLT .
  methods _RENDER
    changing
      !XSLT type STRING
    raising
      /ENSX/CX_XSLT .
  methods _DESCRIBE_ELEMENT
    importing
      !DREF type ref to DATA
      !PATH type STRING
      !TYPEDESCR type ref to CL_ABAP_TYPEDESCR
      !NAME type STRING optional
      !IS_TABLE_LINE type BOOLE_D optional
      !IS_FUNNY type BOOLE_D optional
      !IS_RELATIVE type BOOLE_D optional
    changing
      value(XSLT) type STRING
    raising
      /ENSX/CX_XSLT .
  methods _DESCRIBE_CDATA_ELEMENT
    importing
      !NAME type STRING optional
      !DREF type ref to DATA
      !PATH type STRING
      !TYPEDESCR type ref to CL_ABAP_TYPEDESCR
      !IS_TABLE_LINE type BOOLE_D optional
      !IS_FUNNY type BOOLE_D optional
      !IS_RELATIVE type BOOLE_D optional
    changing
      value(XSLT) type STRING
    raising
      /ENSX/CX_XSLT .
  methods _DESCRIBE_REFERENCE_ELEMENT
    importing
      !NAME type STRING optional
      !DREF type ref to DATA
      !PATH type STRING
      !TYPEDESCR type ref to CL_ABAP_TYPEDESCR
      !IS_TABLE_LINE type BOOLE_D optional
    changing
      value(XSLT) type STRING
    raising
      /ENSX/CX_XSLT .
  methods _DESCRIBE_SIMPLE_ELEMENT
    importing
      !NAME type STRING optional
      !DREF type ref to DATA
      !PATH type STRING
      !TYPEDESCR type ref to CL_ABAP_TYPEDESCR
      !IS_TABLE_LINE type BOOLE_D optional
      !IS_FUNNY type BOOLE_D optional
      !IS_RELATIVE type BOOLE_D optional
    changing
      value(XSLT) type STRING
    raising
      /ENSX/CX_XSLT .
  methods _DESCRIBE_STRUCTURE
    importing
      !DREF type ref to DATA
      !PATH type STRING
      !TYPEDESCR type ref to CL_ABAP_TYPEDESCR
      !NAME type STRING optional
      !IS_TABLE_LINE type BOOLE_D optional
      !IS_RELATIVE type BOOLE_D optional
      !IS_FUNNY type BOOLE_D optional
      !FLATTEN type BOOLE_D optional
    changing
      value(XSLT) type STRING
    raising
      /ENSX/CX_XSLT .
  methods _DESCRIBE_TABLE
    importing
      !NAME type STRING optional
      !DREF type ref to DATA
      !PATH type STRING
      !TYPEDESCR type ref to CL_ABAP_TYPEDESCR
      !IS_TABLE_LINE type BOOLE_D optional
      !IS_RELATIVE type BOOLE_D optional
      !IS_FUNNY type BOOLE_D optional
    changing
      value(XSLT) type STRING
    raising
      /ENSX/CX_XSLT .
  PROTECTED SECTION.
private section.
ENDCLASS.



CLASS /ENSX/CL_XSLT_BASE_RENDERER IMPLEMENTATION.


  METHOD /ensx/if_xslt_renderer~add_source.
    DATA: l_dref TYPE REF TO data.
    FIELD-SYMBOLS: <source> TYPE /ensx/cl_xslt_base_renderer=>ty_trans_srcbind.
    READ TABLE me->/ensx/if_xslt_renderer~gt_sourcebind ASSIGNING <source> WITH KEY name = root.
    IF sy-subrc NE 0.
      APPEND INITIAL LINE TO me->/ensx/if_xslt_renderer~gt_sourcebind ASSIGNING <source>.
    ENDIF.
    <source>-name = root.
    IF data IS SUPPLIED.
      GET REFERENCE OF data INTO l_dref.
      <source>-value = l_dref.
    ENDIF.
    IF dref IS SUPPLIED AND dref IS BOUND.
      <source>-value = dref.
    ENDIF.
    IF <source>-value IS NOT BOUND.
      RAISE EXCEPTION TYPE /ensx/cx_xslt.
    ENDIF.
    <source>-skip = add_skip.
    <source>-flatten = flatten.
  ENDMETHOD.


  METHOD /ensx/if_xslt_renderer~render.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
    DATA: lcx_root       TYPE REF TO cx_root.
    DATA: textid         TYPE scx_t100key.
    DATA: lo_ref         TYPE REF TO data.

    TRY.
        IF root IS NOT INITIAL.
          IF dref IS BOUND.
            lo_ref = dref.
          ENDIF.

          IF data IS SUPPLIED AND data IS NOT INITIAL.
            GET REFERENCE OF data INTO lo_ref.
          ENDIF.

          IF lo_ref IS NOT BOUND.
            RAISE EXCEPTION TYPE /ensx/cx_xslt
              EXPORTING
                previous = lcx_root
                textid   = textid.
          ENDIF.

          me->/ensx/if_xslt_renderer~add_source(
              root   = root
              dref   = lo_ref
                 ).
        ENDIF.

        me->_render( CHANGING xslt   = xslt ).

      CATCH /ensx/cx_xslt INTO lcx_root.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
    ENDTRY.

  ENDMETHOD.


  METHOD constructor.
    DATA: nsbinding TYPE ty_nsbinding.
    super->constructor( ).
    nsbinding-nsuri    = 'http://www.sap.com/abapxml/types/dictionary'.
    nsbinding-nsprefix = 'ddic'.
    INSERT nsbinding INTO TABLE mt_nsbinding.
    nsbinding-nsuri    = 'http://www.sap.com/abapxml/types/defined'.
    nsbinding-nsprefix = 'def'.
    INSERT nsbinding INTO TABLE mt_nsbinding.
  ENDMETHOD.


  METHOD _ADD_BOOLEAN_ELEMENT.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.

    add_st_component_simple_start type attribute_name.
    IF is_table_line = abap_false.
      add_st_component_simple_value path.
    ELSE.
      add_st_component_simple_value name.
    ENDIF.
    add_st_component_simple_end   type.
  ENDMETHOD.


  METHOD _add_simple_element.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.

    add_st_component_simple_start type attribute_name.
    IF is_table_line = abap_false.
      add_st_component_simple_value path.
    ELSE.
      add_st_component_simple_value name.
    ENDIF.
    add_st_component_simple_end   type.
  ENDMETHOD.


  METHOD _add_structure_element_end.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.
    add_st_object_end name.
  ENDMETHOD.


  METHOD _add_structure_element_start.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.

    add_st_object_start name.

  ENDMETHOD.


  METHOD _add_table_element_end.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.

    add_st_table_end.
    add_st_object_end name.
  ENDMETHOD.


  METHOD _add_table_element_start.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.

    add_st_object_start attribute_name.
    add_st_table_start  path name.
  ENDMETHOD.


  METHOD _add_table_index.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.

    add_st_component_simple_start type attribute_name.
    add_st_component_simple_value name.
    add_st_component_simple_end   type.
  ENDMETHOD.


  METHOD _describe.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
    DATA: lcx_root       TYPE REF TO cx_root.
    DATA: textid         TYPE scx_t100key.
    DATA: l_path         TYPE string.

    TRY.
        l_path = path.

        CASE typedescr->kind.
          WHEN cl_abap_typedescr=>kind_table.
            me->_describe_table(
              EXPORTING
                name      = name
                dref      = dref
                path      = l_path
                typedescr = typedescr
                is_table_line = is_table_line
                is_relative = is_relative
              CHANGING
                xslt      = xslt
                   ).
          WHEN cl_abap_typedescr=>kind_struct.
            me->_describe_structure(
              EXPORTING
                name      = name
                dref      = dref
                path      = l_path
                typedescr = typedescr
                is_table_line = is_table_line
                is_relative = is_relative
                flatten     = flatten
              CHANGING
                xslt      = xslt
                   ).
          WHEN cl_abap_typedescr=>kind_elem.
            me->_describe_element(
              EXPORTING
                name      = name
                dref      = dref
                path      = l_path
                typedescr = typedescr
                is_table_line = is_table_line
                is_funny  = is_funny
                is_relative = is_relative
              CHANGING
                xslt      = xslt
                   ).
          WHEN OTHERS.
        ENDCASE.

      CATCH /ensx/cx_xslt INTO lcx_root.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
    ENDTRY.

  ENDMETHOD.


  METHOD _describe_cdata_element.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
    DATA: lcx_root       TYPE REF TO cx_root.
    DATA: textid         TYPE scx_t100key.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.

    TRY.

      CATCH /ensx/cx_xslt INTO lcx_root.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
    ENDTRY.

  ENDMETHOD.


  METHOD _describe_element.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
    DATA: lcx_root       TYPE REF TO cx_root.
    DATA: textid         TYPE scx_t100key.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.

    TRY.

        CASE typedescr->type_kind.
          WHEN 'r' OR '*' OR '+'. " Object References
            RETURN.
          WHEN 'y'. " XSTRING - would need to be CDATA
            me->_describe_cdata_element(
              EXPORTING
                name      = name
                dref      = dref
                path      = path
                typedescr = typedescr
                is_table_line = is_table_line
                is_funny  = is_funny
                is_relative = is_relative
              CHANGING
                xslt      = xslt
                   ).
          WHEN 'C' OR 'N' OR 'I' OR 'g' OR 'w' OR 's' OR 'b' OR 'F' OR 'X' OR 'D' OR 'T' OR 'P'. "simple attributes
            me->_describe_simple_element(
              EXPORTING
                name      = name
                dref      = dref
                path      = path
                typedescr = typedescr
                is_table_line = is_table_line
                is_funny  = is_funny
                is_relative = is_relative
              CHANGING
                xslt      = xslt
                   ).
          WHEN 'u' OR 'v'. "structured attributes
            me->_describe_structure(
              EXPORTING
                name      = name
                dref      = dref
                path      = path
                typedescr = typedescr
                is_table_line = is_table_line
                is_funny    = is_funny
                is_relative = is_relative
              CHANGING
                xslt      = xslt
                   ).
          WHEN 'h'.
            me->_describe_table(
              EXPORTING
                name      = name
                dref      = dref
                path      = path
                typedescr = typedescr
                is_table_line = is_table_line
                is_relative = is_relative
              CHANGING
                xslt      = xslt
                   ).
          WHEN 'l'. " Reference
            me->_describe_reference_element(
              EXPORTING
                name      = name
                dref      = dref
                path      = path
                typedescr = typedescr
                is_table_line = is_table_line
              CHANGING
                xslt      = xslt
                   ).
        ENDCASE.


      CATCH /ensx/cx_xslt INTO lcx_root.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
    ENDTRY.

  ENDMETHOD.


  METHOD _describe_reference_element.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
    DATA: lcx_root       TYPE REF TO cx_root.
    DATA: textid         TYPE scx_t100key.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.

    TRY.


      CATCH /ensx/cx_xslt INTO lcx_root.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
    ENDTRY.

  ENDMETHOD.


  METHOD _describe_simple_element.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
    DATA: lcx_root       TYPE REF TO cx_root.
    DATA: textid         TYPE scx_t100key.
    DATA: l_datadescr    TYPE REF TO cl_abap_datadescr.
    DATA: l_typedescr    TYPE REF TO cl_abap_structdescr.
    DATA: l_path         TYPE string.
    DATA: datatype           TYPE char30.
    DATA: attribute_name     TYPE string.
    DATA: is_ddic_type       TYPE boole_d.

    FIELD-SYMBOLS: <component> TYPE abap_compdescr.

    TRY.
        datatype = typedescr->get_relative_name( ).
        attribute_name = me->_get_element_name( typedescr = typedescr
                                                path      = path
                                                is_table_line = is_table_line ).
        is_ddic_type = typedescr->is_ddic_type( ).

        CASE typedescr->type_kind.
          WHEN cl_abap_typedescr=>typekind_int
            OR cl_abap_typedescr=>typekind_int1
            OR cl_abap_typedescr=>typekind_int2
            OR cl_abap_typedescr=>typekind_float
            OR cl_abap_typedescr=>typekind_decfloat
            OR cl_abap_typedescr=>typekind_decfloat16
            OR cl_abap_typedescr=>typekind_decfloat34
            OR cl_abap_typedescr=>typekind_numeric.
            me->_add_simple_element(
               EXPORTING
                 name           = name
                 path           = path
                 attribute_name = attribute_name
                 is_table_line  = is_table_line
                 type           = 'num'
                 is_funny       = is_funny
                 is_relative    = is_relative
               CHANGING
                 xslt           = xslt
                    ).
          WHEN cl_abap_typedescr=>typekind_num. "NUMC
            me->_add_simple_element(
               EXPORTING
                 name           = name
                 path           = path
                 attribute_name = attribute_name
                 is_table_line  = is_table_line
                 type           = 'str'
                 is_funny       = is_funny
                 is_relative    = is_relative
               CHANGING
                 xslt           = xslt
                    ).
          WHEN OTHERS.
            IF datatype CS 'BOOL' OR datatype CS 'XFELD' OR datatype CS 'FLAG'.
              me->_add_boolean_element(
                EXPORTING
                  name           = name
                  path           = path
                  attribute_name = attribute_name
                  is_table_line  = is_table_line
                  type           = 'str'
                  is_funny       = is_funny
                  is_relative    = is_relative
                CHANGING
                  xslt           = xslt
                     ).
            ELSE.
              me->_add_simple_element(
                 EXPORTING
                   name           = name
                   path           = path
                   attribute_name = attribute_name
                   is_table_line  = is_table_line
                   type           = 'str'
                   is_funny       = is_funny
                   is_relative    = is_relative
                 CHANGING
                   xslt           = xslt
                      ).
            ENDIF.
        ENDCASE.

      CATCH /ensx/cx_xslt INTO lcx_root.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
    ENDTRY.

  ENDMETHOD.


  METHOD _describe_structure.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
    DATA: lcx_root       TYPE REF TO cx_root.
    DATA: textid         TYPE scx_t100key.
    DATA: l_datadescr    TYPE REF TO cl_abap_datadescr.
    DATA: l_typedescr    TYPE REF TO cl_abap_typedescr.
    DATA: structdescr    TYPE REF TO cl_abap_structdescr.
    DATA: l_path         TYPE string.
    DATA: datatype           TYPE char30.
    DATA: l_is_table_line    TYPE boole_d.
    DATA: l_is_relative      TYPE boole_d.
    DATA: attribute_name     TYPE string.

    FIELD-SYMBOLS: <component> TYPE abap_compdescr.

    TRY.
        structdescr ?= typedescr.
        datatype = structdescr->get_relative_name( ).


        IF me->__check_flatten_condition(
            flatten    = flatten
            name       = name
               ) = abap_false.

          me->_add_structure_element_start(
            EXPORTING
              name           = name
              path           = path
              attribute_name = attribute_name
              is_table_line  = is_table_line
            CHANGING
              xslt           = xslt
                 ).
        ENDIF.

        LOOP AT structdescr->components ASSIGNING <component>.
          attribute_name = <component>-name.

          CONCATENATE path '.' attribute_name INTO l_path.

          structdescr->get_component_type(
            EXPORTING
              p_name                 = <component>-name
            RECEIVING
              p_descr_ref            = l_datadescr
            EXCEPTIONS
              component_not_found    = 1
              unsupported_input_type = 2
              OTHERS                 = 3
                 ).
          IF sy-subrc <> 0.
            RAISE EXCEPTION TYPE /ensx/cx_xslt
              EXPORTING
                previous = lcx_root
                textid   = textid.
          ENDIF.

          l_typedescr ?= l_datadescr.

          IF l_typedescr->kind NE cl_abap_typedescr=>kind_elem
            AND is_table_line = abap_true.
            l_is_relative   = abap_true.
            l_is_table_line = abap_false.
            CONCATENATE '.' attribute_name INTO l_path.
          ELSE.
            l_is_relative   = is_relative.
            l_is_table_line = is_table_line.
          ENDIF.

          me->_describe(
            EXPORTING
              name      = attribute_name
              dref      = dref
              typedescr = l_typedescr
              path      = l_path
              is_table_line = l_is_table_line
              is_funny  = space
              is_relative = l_is_relative
              flatten     = flatten
            CHANGING
              xslt      = xslt
                 ).

        ENDLOOP.

        IF me->__check_flatten_condition(
            flatten    = flatten
            name       = name
               ) = abap_false.
          me->_add_structure_element_end(
            EXPORTING
              name           = name
              path           = path
              attribute_name = attribute_name
              is_table_line  = is_table_line
            CHANGING
              xslt           = xslt
                 ).
        ENDIF.

      CATCH /ensx/cx_xslt INTO lcx_root.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
    ENDTRY.

  ENDMETHOD.


  METHOD _describe_table.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
    DATA: lcx_root       TYPE REF TO cx_root.
    DATA: textid         TYPE scx_t100key.
    DATA: tabledescr     TYPE REF TO cl_abap_tabledescr.
    DATA: l_typedescr    TYPE REF TO cl_abap_typedescr.
    DATA: l_path         TYPE string.
    DATA: l_datatype     TYPE char30.
    DATA: l_is_funny       TYPE boole_d.
    DATA: attribute_name TYPE string.

    TRY.

        tabledescr ?= typedescr.
        l_typedescr  ?= tabledescr->get_table_line_type( ).
        l_datatype  = l_typedescr->get_relative_name( ).
        IF l_typedescr->kind = cl_abap_typedescr=>kind_elem.
          l_is_funny = abap_true. " Most probably the item line is not typed
        ENDIF.

        IF name IS SUPPLIED AND name IS NOT INITIAL.
          attribute_name = name.
        ELSE.
          attribute_name = me->_get_element_name( typedescr = typedescr ).
        ENDIF.

*        CONCATENATE path '.' attribute_name INTO l_path.
        l_path = path+1.
        me->_do_skip_start(
          EXPORTING
            root     = l_path
*    datatype = datatype
          CHANGING
            xslt     = xslt
               ).

        me->_add_table_element_start(
          EXPORTING
            name           = name
            path           = path
            attribute_name = attribute_name
            is_table_line  = is_table_line
          CHANGING
            xslt           = xslt
               ).

        me->_describe(
          EXPORTING
            name   = attribute_name
            dref   = dref
            path   = path
            typedescr = l_typedescr
            is_table_line = abap_true
            is_funny   = l_is_funny
          CHANGING
            xslt   = xslt
               ).

        me->_add_table_element_end(
          EXPORTING
            name           = name
            path           = path
            attribute_name = attribute_name
            is_table_line  = is_table_line
          CHANGING
            xslt           = xslt
               ).
        me->_do_skip_end(
          EXPORTING
            root     = l_path
*    datatype = datatype
          CHANGING
            xslt     = xslt
               ).

      CATCH /ensx/cx_xslt INTO lcx_root.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
    ENDTRY.

  ENDMETHOD.


  METHOD _do_footer.
    DATA: lv_initial  TYPE boole_d.
    DATA: lv_comment  TYPE string.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.

    add_st_json_template_end.
    add_st_footer.
  ENDMETHOD.


  METHOD _do_header.
    data: temp           type string.
    DATA: lv_initial  TYPE boole_d.
    DATA: lv_comment  TYPE string.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.
    FIELD-SYMBOLS: <nsbinding> TYPE ty_nsbinding.

    add_st_header.                                          "#EC NOTEXT

    LOOP AT mt_nsbinding ASSIGNING <nsbinding>.
      add_st_namespace <nsbinding>-nsprefix <nsbinding>-nsuri. "#EC NOTEXT
    ENDLOOP.

    add_st_header2.                                         "#EC NOTEXT

    add_st_comment_start.                                   "#EC NOTEXT
    add_st_comment 'Generated Simple Transformation'.
    CONCATENATE 'Generated by ' sy-uname ' on ' sy-datum into temp RESPECTING BLANKS.
    add_st_comment temp.
    add_st_comment ''.                                      "#EC NOTEXT
    LOOP AT mt_comments INTO lv_comment.
      add_st_comment lv_comment.                            "#EC NOTEXT
    ENDLOOP.
    add_st_comment_end.                                     "#EC NOTEXT

    add_st_base_root.
  ENDMETHOD.


  METHOD _DO_OBJECT_COMMENT.
    data: temp           type string.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.

    add_st_comment_start.                                   "#EC NOTEXT
    CONCATENATE 'Data Object "' root '" of type "' datatype into temp RESPECTING BLANKS.
    add_st_comment temp.
    add_st_comment_end.
  ENDMETHOD.


  METHOD _DO_OBJECT_END.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.

    add_st_object_end root.
  ENDMETHOD.


  METHOD _DO_OBJECT_START.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.

    add_st_object_start root.
  ENDMETHOD.


  METHOD _do_roots.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.
    IF datatype IS NOT INITIAL.
      add_st_json_roots root datatype.
    ELSE.
      add_st_json_roots_notype root.
    ENDIF.
  ENDMETHOD.


  METHOD _DO_SERIALIZE_END.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.

    add_st_serialize_end root.
  ENDMETHOD.


  METHOD _DO_SERIALIZE_START.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.

    add_st_serialize_start root.
  ENDMETHOD.


  METHOD _do_skip_end.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.

    add_st_cond_end root.
    add_st_cond_end root.
  ENDMETHOD.


  METHOD _DO_SKIP_START.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.

    add_st_scond_exists_start root.
    add_st_scond_check_start root.
  ENDMETHOD.


  METHOD _DO_TEMPLATE_START.
    data: lv_initial     type boole_d.
    DATA: lv_lin         TYPE string.
    DATA: lv_src         TYPE string.
    DATA: lv_par         TYPE string.

    add_st_json_template_start.
  ENDMETHOD.


  METHOD _get_element_name.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
    DATA: lcx_root       TYPE REF TO cx_root.
    DATA: textid         TYPE scx_t100key.
    DATA: x031l          TYPE dd_x031l_table.
    DATA: x030l          TYPE x030l.
    DATA: flddescr       TYPE dfies.
    DATA: strtab         TYPE string_table.
    DATA: lines          TYPE i.
    FIELD-SYMBOLS: <x031l> TYPE x031l.
    TRY.

        CASE typedescr->kind.
          WHEN cl_abap_typedescr=>kind_table
            OR cl_abap_typedescr=>kind_struct.
            typedescr->get_ddic_header(
              RECEIVING
                p_header     = x030l
              EXCEPTIONS
                not_found    = 1
                no_ddic_type = 2
                OTHERS       = 3
                   ).
            IF sy-subrc <> 0.
              RAISE EXCEPTION TYPE /ensx/cx_xslt
                EXPORTING
                  previous = lcx_root
                  textid   = textid.
            ENDIF.
            name = x030l-tabname.
            REPLACE ALL OCCURRENCES OF '/' IN name WITH '--'.
          WHEN OTHERS.
            SPLIT path AT '.' INTO TABLE strtab.
            lines = lines( strtab ).
            READ TABLE strtab INTO name INDEX lines.
            IF sy-subrc NE 0 OR name IS INITIAL.
              typedescr->get_ddic_object(
                RECEIVING
                  p_object     = x031l
                EXCEPTIONS
                  not_found    = 1
                  no_ddic_type = 2
                  OTHERS       = 3
                     ).
              IF sy-subrc <> 0.
                RAISE EXCEPTION TYPE /ensx/cx_xslt
                  EXPORTING
                    previous = lcx_root
                    textid   = textid.
              ENDIF.
              READ TABLE x031l ASSIGNING <x031l> INDEX 1.
              IF sy-subrc <> 0.
                RAISE EXCEPTION TYPE /ensx/cx_xslt
                  EXPORTING
                    previous = lcx_root
                    textid   = textid.
              ENDIF.
              name = <x031l>-fieldname.
            ENDIF.
            REPLACE ALL OCCURRENCES OF '/' IN name WITH '--'.
        ENDCASE.
      CATCH /ensx/cx_xslt INTO lcx_root.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
    ENDTRY.

  ENDMETHOD.


  METHOD _render.
*-----------------------------------------------------------------------
*
*-----------------------------------------------------------------------
    DATA: lcx_root       TYPE REF TO cx_root.
    DATA: textid         TYPE scx_t100key.
    DATA: typedescr      TYPE REF TO cl_abap_typedescr.
    DATA: l_path         TYPE string.
    DATA: l_datatype     TYPE char30.

    FIELD-SYMBOLS: <source> TYPE /ensx/cl_xslt_base_renderer=>ty_trans_srcbind.
    TRY.
        " Add the header
        me->_do_header( CHANGING  xslt     = xslt ).
        " Add all roots
        " ------------------------------------------------------------
        LOOP AT gt_sourcebind ASSIGNING <source>.

          cl_abap_typedescr=>describe_by_data_ref(
            EXPORTING
              p_data_ref           = <source>-value
            RECEIVING
              p_descr_ref          = typedescr
            EXCEPTIONS
              reference_is_initial = 1
              OTHERS               = 2
                 ).

          IF sy-subrc <> 0.
            RAISE EXCEPTION TYPE /ensx/cx_xslt
              EXPORTING
                previous = lcx_root
                textid   = textid.
          ENDIF.
          l_datatype = typedescr->get_relative_name( ).

          IF typedescr->is_ddic_type( ) = abap_false.
            CLEAR l_datatype. "no datatype, else syintax error in transformation
          ENDIF.

          me->_do_roots(
            EXPORTING
              root     = <source>-name
              datatype = l_datatype
            CHANGING
              xslt     = xslt
                 ).

        ENDLOOP.
        " Start the template
        " ------------------------------------------------------------
        me->_do_template_start( CHANGING xslt = xslt   ).

        me->_do_object_start(
          EXPORTING
            root     = m_objname
          CHANGING
            xslt     = xslt
               ).
        " Create the transformations
        " ------------------------------------------------------------
        LOOP AT gt_sourcebind ASSIGNING <source>.

          cl_abap_typedescr=>describe_by_data_ref(
            EXPORTING
              p_data_ref           = <source>-value
            RECEIVING
              p_descr_ref          = typedescr
            EXCEPTIONS
              reference_is_initial = 1
              OTHERS               = 2
                 ).

          IF sy-subrc <> 0.
            RAISE EXCEPTION TYPE /ensx/cx_xslt
              EXPORTING
                previous = lcx_root
                textid   = textid.
          ENDIF.

          l_datatype = typedescr->get_relative_name( ).

          me->_do_object_comment(
            EXPORTING
              root     = <source>-name
              datatype = l_datatype
            CHANGING
              xslt     = xslt
                 ).

          IF <source>-skip = abap_true.
            me->_do_serialize_start(
              EXPORTING
                root     = <source>-name
              CHANGING
                xslt     = xslt
                   ).
            IF typedescr->kind NE cl_abap_typedescr=>kind_table.
              " This will be done automatically for tables
              me->_do_skip_start(
                EXPORTING
                  root     = <source>-name
                CHANGING
                  xslt     = xslt
                     ).
            ENDIF.
          ENDIF.

          CONCATENATE '.' <source>-name INTO l_path.
          me->_describe(
            EXPORTING
              name      = <source>-name
              dref      = <source>-value
              typedescr = typedescr
              path      = l_path
              is_funny  = space
              flatten   = <source>-flatten
            CHANGING
              xslt      = xslt
                 ).

          IF <source>-skip = abap_true.
            IF typedescr->kind NE cl_abap_typedescr=>kind_table.
              " This will be done automatically for tables
              me->_do_skip_end(
                EXPORTING
                  root     = <source>-name
                CHANGING
                  xslt     = xslt
                     ).
            ENDIF.
            me->_do_serialize_end(
              EXPORTING
                root     = <source>-name
              CHANGING
                xslt     = xslt
                   ).
          ENDIF.

        ENDLOOP.

        me->_do_object_end(
          EXPORTING
            root     = m_objname
          CHANGING
            xslt     = xslt
               ).
        me->_do_footer( CHANGING xslt = xslt   ).

      CATCH /ensx/cx_xslt INTO lcx_root.
        RAISE EXCEPTION TYPE /ensx/cx_xslt
          EXPORTING
            previous = lcx_root
            textid   = textid.
    ENDTRY.

  ENDMETHOD.


  method __CHECK_FLATTEN_CONDITION.
  endmethod.
ENDCLASS.