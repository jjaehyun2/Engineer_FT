class ZSAPLINK_CLASS definition
  public
  inheriting from ZSAPLINK_OO
  create public .

public section.

  data MV_STEAMROLLER type ABAP_BOOL value ABAP_FALSE ##NO_TEXT.

  methods CHECKEXISTS
    redefinition .
  methods CREATEIXMLDOCFROMOBJECT
    redefinition .
  methods CREATEOBJECTFROMIXMLDOC
    redefinition .
  methods GET_VERSION_INFO
    redefinition .
protected section.

  constants C_XML_KEY_METHOD_DOCUMENTATION type STRING value 'methodDocumentation' ##NO_TEXT.
  constants C_XML_KEY_TEXTELEMENT type STRING value 'textElement' ##NO_TEXT.
  constants C_XML_KEY_TEXTPOOL type STRING value 'textPool' ##NO_TEXT.
  constants C_XML_KEY_CLASS_DOCUMENTATION type STRING value 'classDocumentation' ##NO_TEXT.
  constants C_XML_KEY_LANGUAGE type STRING value 'language' ##NO_TEXT.
  constants C_XML_KEY_OBJECT type STRING value 'OBJECT' ##NO_TEXT.
  constants C_XML_KEY_SPRAS type STRING value 'SPRAS' ##NO_TEXT.
  constants C_XML_KEY_TEXTLINE type STRING value 'textLine' ##NO_TEXT.

  methods CREATE_DOCUMENTATION .
  methods CREATE_METHOD_DOCUMENTATION
    importing
      !NODE type ref to IF_IXML_ELEMENT .
  methods CREATE_SECTIONS .
  methods CREATE_TEXTPOOL .
  methods FINDIMPLEMENTINGCLASS
    importing
      !METHODNAME type STRING
      !STARTCLASS type STRING optional
    returning
      value(CLASSNAME) type STRING .
  methods GET_DOCUMENTATION
    changing
      !ROOTNODE type ref to IF_IXML_ELEMENT .
  methods GET_METHOD_DOCUMENTATION
    importing
      !METHOD_KEY type SEOCPDKEY
    changing
      !ROOTNODE type ref to IF_IXML_ELEMENT .
  methods GET_SECTIONS
    changing
      !ROOTNODE type ref to IF_IXML_ELEMENT .
  methods GET_TEXTPOOL
    changing
      !ROOTNODE type ref to IF_IXML_ELEMENT .

  methods DELETEOBJECT
    redefinition .
  methods GETOBJECTTYPE
    redefinition .
private section.
ENDCLASS.



CLASS ZSAPLINK_CLASS IMPLEMENTATION.


method CHECKEXISTS.
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*| Copyright 2014 SAPlink project members                              |
*|                                                                     |
*| Licensed under the Apache License, Version 2.0 (the "License");     |
*| you may not use this file except in compliance with the License.    |
*| You may obtain a copy of the License at                             |
*|                                                                     |
*|     http://www.apache.org/licenses/LICENSE-2.0                      |
*|                                                                     |
*| Unless required by applicable law or agreed to in writing, software |
*| distributed under the License is distributed on an "AS IS" BASIS,   |
*| WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or     |
*| implied.                                                            |
*| See the License for the specific language governing permissions and |
*| limitations under the License.                                      |
*\---------------------------------------------------------------------/
data classkey type SEOCLSKEY.
data not_active TYPE  SEOX_BOOLEAN.

  classKey-clsName = objname.

  call function 'SEO_CLASS_EXISTENCE_CHECK'
    EXPORTING
      clskey        = classkey
    IMPORTING
      not_active    = not_active
    EXCEPTIONS
*      not_specified = 1
      not_existing  = 2.
*      is_interface  = 3
*      no_text       = 4
*      inconsistent  = 5
*      others        = 6.

  if sy-subrc <> 2.
    exists = 'X'.
  endif.
endmethod.


METHOD createixmldocfromobject.
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*| Copyright 2014 SAPlink project members                              |
*|                                                                     |
*| Licensed under the Apache License, Version 2.0 (the "License");     |
*| you may not use this file except in compliance with the License.    |
*| You may obtain a copy of the License at                             |
*|                                                                     |
*|     http://www.apache.org/licenses/LICENSE-2.0                      |
*|                                                                     |
*| Unless required by applicable law or agreed to in writing, software |
*| distributed under the License is distributed on an "AS IS" BASIS,   |
*| WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or     |
*| implied.                                                            |
*| See the License for the specific language governing permissions and |
*| limitations under the License.                                      |
*\---------------------------------------------------------------------/
  DATA localimplementation TYPE REF TO if_ixml_element.
  DATA localtypes TYPE REF TO if_ixml_element.
  DATA localmacros TYPE REF TO if_ixml_element.
  DATA rootnode TYPE REF TO if_ixml_element.
  DATA reportlist TYPE STANDARD TABLE OF string.
  DATA includename TYPE program.
  DATA _classname TYPE seoclsname.
  DATA reportstring TYPE string.
  DATA rc TYPE sysubrc.
  DATA classdescr TYPE REF TO cl_abap_classdescr.
  DATA typedescr TYPE REF TO cl_abap_typedescr.
  DATA methoddescr TYPE abap_methdescr.
  DATA methodnode TYPE REF TO if_ixml_element.
  DATA parameternode TYPE REF TO if_ixml_element.
  DATA sourcenode TYPE REF TO if_ixml_element.
  DATA exceptionnode TYPE REF TO if_ixml_element.
  DATA exceptionlist TYPE seos_exceptions_r.
  DATA anexception TYPE vseoexcep.
  DATA inheritancenode TYPE REF TO if_ixml_element.
  DATA redefnode TYPE REF TO if_ixml_element.

  DATA tempstring TYPE string.
  DATA methodkey TYPE seocpdkey.
  DATA clsmethkey TYPE seocmpkey.
  DATA methodproperties TYPE vseomethod.
  DATA classkey TYPE seoclskey.
  DATA classproperties TYPE vseoclass.
  DATA paramdescr TYPE abap_parmdescr.
  DATA paramkey TYPE seoscokey.
  DATA paramproperties TYPE vseoparam.
  DATA superclass TYPE REF TO cl_abap_typedescr.
  DATA superclassname TYPE string.
  DATA superclasskey TYPE seorelkey.

  DATA attribdescr TYPE abap_attrdescr.
  DATA attribkey TYPE seocmpkey.
  DATA attribproperties TYPE vseoattrib.
  DATA attribnode TYPE REF TO if_ixml_element.
  DATA inheritanceprops TYPE vseoextend.
  DATA redefines TYPE STANDARD TABLE OF seoredef
      WITH KEY clsname refclsname version mtdname.
  DATA inheritance TYPE seor_inheritance_r.
  DATA redefinitions TYPE seor_redefinitions_r.
  DATA redefinition LIKE LINE OF redefinitions.

  DATA otrnode TYPE REF TO if_ixml_element.
  DATA _otrguid TYPE sotr_conc.

  data: ls_version_info type gts_version_info.

  _classname = objname.
  classkey-clsname = objname.

*  setObjectType( ).

  DATA _objtype TYPE string.
*  _objType = objType.
  _objtype = getobjecttype( ).
  rootnode = xmldoc->create_element( _objtype ).
  CALL FUNCTION 'SEO_CLASS_GET'
    EXPORTING
      clskey       = classkey
      version      = '1'
    IMPORTING
      class        = classproperties
    EXCEPTIONS
      not_existing = 1
      deleted      = 2
      is_interface = 3
      model_only   = 4.

  IF sy-subrc <> 0.
    CASE sy-subrc.
      WHEN 1.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING
            textid = zcx_saplink=>not_found
            object = objname.
      WHEN 2.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING
            textid = zcx_saplink=>error_message
            msg    = 'class deleted'.
      WHEN 3.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING
            textid = zcx_saplink=>error_message
            msg    = 'interfaces not supported'.
      WHEN 4.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING
            textid = zcx_saplink=>error_message
            msg    = 'class is modeled only'.
    ENDCASE.
  ENDIF.

  setattributesfromstructure( node      = rootnode
                              structure = classproperties ).
*--------------------------------------------------------------------*
* Added versioning info
*--------------------------------------------------------------------*
  ls_version_info = get_version_info( ).
  setattributesfromstructure( node      = rootnode
                              structure = ls_version_info ).

  TRY.
      CALL METHOD cl_abap_classdescr=>describe_by_name
        EXPORTING
          p_name         = objname
        RECEIVING
          p_descr_ref    = typedescr
        EXCEPTIONS
          type_not_found = 1.
      IF sy-subrc = 0.
        classdescr ?= typedescr.
      ELSE.

      ENDIF.
    CATCH cx_root.
      RAISE EXCEPTION TYPE zcx_saplink
        EXPORTING
          textid = zcx_saplink=>system_error.
  ENDTRY.

  CALL METHOD classdescr->get_super_class_type
    RECEIVING
      p_descr_ref           = superclass
    EXCEPTIONS
      super_class_not_found = 1.

  IF sy-subrc = 0.
    superclassname = superclass->get_relative_name( ).
    IF NOT superclassname CS 'OBJECT'.
      superclasskey-clsname = objname.
      superclasskey-refclsname = superclassname.
      CALL FUNCTION 'SEO_INHERITANC_GET'
        EXPORTING
          inhkey        = superclasskey
        IMPORTING
          inheritance   = inheritanceprops
          redefinitions = redefines.
      setattributesfromstructure( node = rootnode structure =
      inheritanceprops ).
    ENDIF.
  ENDIF.

*/***TPJ - Added Logic for TYPES  -------------------*/
  DATA: types      TYPE seoo_types_r,
        wa_type    LIKE LINE OF types,
        types_node TYPE REF TO if_ixml_element.
  CALL FUNCTION 'SEO_TYPE_READ_ALL'
    EXPORTING
      cifkey            = classkey
      version           = 1
    IMPORTING
      types             = types
    EXCEPTIONS
      clif_not_existing = 1
      OTHERS            = 2.
  IF sy-subrc <> 0.
  ENDIF.
  LOOP AT types INTO wa_type.
    types_node = xmldoc->create_element( 'types' ).
    clear wa_type-TYPESRC_LENG. " Will be recalculated on import, differs depending on OS due to linebreaks
    setattributesfromstructure( node = types_node structure =
    wa_type ).
    rc = rootnode->append_child( types_node ).
  ENDLOOP.
*/***TPJ - End of Added Logic for TYPES  -------------------*/

*/***TPJ - Added Logic for Friends  -------------------*/
  DATA: clif_keys     TYPE STANDARD TABLE OF seoclskey,
        friends       TYPE STANDARD TABLE OF seofriends,
        wa_friend     LIKE LINE OF friends,
        friends_node  TYPE REF TO if_ixml_element.

  APPEND classkey TO clif_keys.
  CALL FUNCTION 'SEO_FRIENDS_SELECT'
    EXPORTING
      with_external_ref = 'X'
    TABLES
      clif_keys         = clif_keys
      friends_relations = friends.
  IF sy-subrc <> 0.
  ENDIF.
  LOOP AT friends INTO wa_friend.
    friends_node = xmldoc->create_element( c_xml_key_friends ).
    setattributesfromstructure( node = friends_node structure =
    wa_friend ).
    rc = rootnode->append_child( friends_node ).
  ENDLOOP.
*/***TPJ - End of Added Logic for Friends  -------------------*/

*/***ewH - Added Logic for Interfaces  -------------------*/
*/***uku - discard included interfaces -------------------*/
  DATA: it_implementings TYPE seor_implementings_r,
        lt_implementings_copy TYPE seor_implementings_r,
        wa_implementings LIKE LINE OF it_implementings,
        implementingnode TYPE REF TO if_ixml_element,
        ls_interface TYPE seoc_interface_r,
        lt_comprisings TYPE seor_comprisings_r,
        ls_intfkey TYPE seoclskey.
  FIELD-SYMBOLS <ls_comprisings> TYPE seor_comprising_r.

  CALL FUNCTION 'SEO_IMPLEMENTG_READ_ALL'
    EXPORTING
      clskey             = classkey
    IMPORTING
      implementings      = it_implementings
    EXCEPTIONS
      class_not_existing = 1
      OTHERS             = 2.

  lt_implementings_copy = it_implementings.
  LOOP AT it_implementings INTO wa_implementings.
    CLEAR: ls_intfkey.
    ls_intfkey-clsname = wa_implementings-refclsname.
    CALL FUNCTION 'SEO_INTERFACE_TYPEINFO_GET'
      EXPORTING
        intkey      = ls_intfkey
      IMPORTING
        comprisings = lt_comprisings.
    LOOP AT lt_comprisings ASSIGNING <ls_comprisings>.
      DELETE lt_implementings_copy WHERE refclsname = <ls_comprisings>-refclsname.
    ENDLOOP.
  ENDLOOP.

  LOOP AT lt_implementings_copy INTO wa_implementings.
    implementingnode = xmldoc->create_element( 'implementing' ).
    setattributesfromstructure( node = implementingnode structure =
    wa_implementings ).
    rc = rootnode->append_child( implementingnode ).
  ENDLOOP.
*/***uku - End of discard included interfaces -------------------*/
*/***ewH - End of Added Logic for Interfaces  -------------------*/
*/***rrq - Added Logic for EVENTS  -------------------*/
  DATA: events      TYPE seoo_events_r,
        wa_event    LIKE LINE OF events,
        event_node  TYPE REF TO if_ixml_element,
        eventkey    TYPE seocmpkey,
        eventparams TYPE seos_parameters_r,
        wa_params   TYPE seos_parameter_r.
  CALL FUNCTION 'SEO_EVENT_READ_ALL'
    EXPORTING
      cifkey            = classkey
      version           = 1
    IMPORTING
      events            = events
    EXCEPTIONS
      clif_not_existing = 1
      OTHERS            = 2.
  IF sy-subrc <> 0.
  ENDIF.
  LOOP AT events INTO wa_event.
    eventkey-clsname = wa_event-clsname.
    eventkey-cmpname = wa_event-cmpname.
    event_node = xmldoc->create_element( 'events' ).
    setattributesfromstructure( node = event_node structure =
    wa_event ).
    CALL FUNCTION 'SEO_EVENT_SIGNATURE_GET'
      EXPORTING
        evtkey     = eventkey
      IMPORTING
        parameters = eventparams.

*   parameters
    LOOP AT eventparams INTO wa_params.

      parameternode = xmldoc->create_element( 'parameter' ).
      setattributesfromstructure( node = parameternode
      structure = wa_params ).
      rc = event_node->append_child( parameternode ).
    ENDLOOP.
    rc = rootnode->append_child( event_node ).
  ENDLOOP.
*/***rrq - End of Added Logic for EVENTS  -------------------*/
* removed by Rene.
  get_sections( CHANGING rootnode = rootnode ) .
*|--------------------------------------------------------------------|
  includename = cl_oo_classname_service=>get_ccimp_name( _classname ).
  READ REPORT includename INTO reportlist.
  localimplementation = xmldoc->create_element( 'localImplementation' ).
  reportstring = buildsourcestring( sourcetable = reportlist ).
  rc = localimplementation->if_ixml_node~set_value( reportstring ).
*|--------------------------------------------------------------------|
  includename = cl_oo_classname_service=>get_ccdef_name( _classname ).
  READ REPORT includename INTO reportlist.
  localtypes = xmldoc->create_element( 'localTypes' ).
  reportstring = buildsourcestring( sourcetable = reportlist ).
  rc = localtypes->if_ixml_node~set_value( reportstring ).
*|--------------------------------------------------------------------|
  includename = cl_oo_classname_service=>get_ccmac_name( _classname ).
  READ REPORT includename INTO reportlist.
  localmacros = xmldoc->create_element( 'localMacros' ).
  reportstring = buildsourcestring( sourcetable = reportlist ).
  rc = localmacros->if_ixml_node~set_value( reportstring ).
*|--------------------------------------------------------------------|
*/***EVP - Added Logic for Local Test Classes  ----------------------*/
  DATA localtestclasses TYPE REF TO if_ixml_element.
  DATA localtestclassesexist TYPE i.

  includename = cl_oo_classname_service=>get_local_testclasses_include( _classname ).
  READ REPORT includename INTO reportlist.
  " If sy-subrc = 0 the local test classes do exist
  localtestclassesexist = sy-subrc.
  IF localtestclassesexist = 0.
    localtestclasses = xmldoc->create_element( 'localTestClasses' ).
    reportstring = buildsourcestring( sourcetable = reportlist ).
    rc = localtestclasses->if_ixml_node~set_value( reportstring ).
  ENDIF.
*/***EVP - End of Added Logic for Local Test Classes  ---------------*/
*|                                                                    |
*\--------------------------------------------------------------------/
  rc = rootnode->append_child( localimplementation ).
  rc = rootnode->append_child( localtypes ).
  rc = rootnode->append_child( localmacros ).
*/***EVP - Added Logic for Local Test Classes  -------------------*/
  IF localtestclassesexist = 0.
    rc = rootnode->append_child( localtestclasses ).
  ENDIF.
*/***EVP - End of Added Logic for Local Test Classes  ------------*/
**// Rich:  Start
  get_textpool( CHANGING rootnode = rootnode ).
  get_documentation( CHANGING rootnode = rootnode ).
**// Rich:  End
  get_typepusage( CHANGING  xo_rootnode = rootnode ).
  get_clsdeferrd( CHANGING  xo_rootnode = rootnode ).
  get_intdeferrd( CHANGING  xo_rootnode = rootnode ).

*  classDescriptor ?= cl_abap_typedescr=>describe_by_name( className ).
  attribkey-clsname = objname.

  LOOP AT classdescr->attributes INTO attribdescr
  WHERE is_inherited = abap_false
  AND is_interface = abap_false. "rrq:issue 46
    attribnode = xmldoc->create_element( 'attribute' ).
    attribkey-cmpname = attribdescr-name.
    CALL FUNCTION 'SEO_ATTRIBUTE_GET'
      EXPORTING
        attkey    = attribkey
      IMPORTING
        attribute = attribproperties.

*   include OTR if necessary (for exception classes)
    IF attribproperties-type = 'SOTR_CONC' AND attribproperties-attvalue
    IS NOT INITIAL.
      _otrguid = attribproperties-attvalue+1(32).
      otrnode = get_otr( _otrguid ).
      IF otrnode IS BOUND.
        rc = attribnode->append_child( otrnode ).
        " Issue #222 - get_text empty when ZCX_SAPLINK exception is raised
        " Gregor Wolf, 2012-12-20
        " As GUID for OTR Node is created new in every system we import
        " the Slinkee we should empty it
        CLEAR: attribproperties-attvalue.
      ENDIF.
    ENDIF.

*   append attribute node to parent node
    setattributesfromstructure( node      = attribnode
                                structure = attribproperties ).
    rc = rootnode->append_child( attribnode ).
  ENDLOOP.

*// ewH: begin of logic for interface methods & inheritance redesign-->
* inheritances & redefinitions: old source removed-recover w/subversion
  CALL FUNCTION 'SEO_INHERITANC_READ'
    EXPORTING
      clskey             = classkey
    IMPORTING
      inheritance        = inheritance
      redefinitions      = redefinitions
    EXCEPTIONS
      class_not_existing = 1
      OTHERS             = 2.

  IF inheritance IS NOT INITIAL.
    inheritancenode = xmldoc->create_element( c_xml_key_inheritance ).
    setattributesfromstructure( node = inheritancenode structure =
    inheritance ).

    LOOP AT redefinitions INTO redefinition.
      redefnode = xmldoc->create_element( 'redefinition' ).
      setattributesfromstructure( node = redefnode structure =
      redefinition ).
      rc = inheritancenode->append_child( redefnode ).
    ENDLOOP.
    rc = rootnode->append_child( inheritancenode ).
  ENDIF.

* methods with out alias We handle this later
  LOOP AT classdescr->methods INTO methoddescr WHERE alias_for IS INITIAL AND
  NOT ( is_inherited = 'X' AND is_redefined IS INITIAL ).
    methodkey-clsname = _classname.
    methodkey-cpdname = methoddescr-name.
*//nbus: added logic for exception class
    IF    methoddescr-name         =  'CONSTRUCTOR'
      AND classproperties-category =  seoc_category_exception
      and me->mv_steamroller       <> abap_true.
      " Constructor() will be generated automatically into the
      " target system once the class is saved
      CONTINUE.
    ENDIF.
*//nbus: end of added logic for exception class
*   interface methods
    IF methoddescr-is_interface = 'X'.
      CALL METHOD cl_oo_classname_service=>get_method_include
        EXPORTING
          mtdkey              = methodkey
        RECEIVING
          result              = includename
        EXCEPTIONS
          method_not_existing = 1.
      IF sy-subrc = 0.
        methodnode = xmldoc->create_element( 'interfaceMethod' ).
        setattributesfromstructure( node = methodnode structure =
        methodkey ).
        sourcenode = xmldoc->create_element( 'source' ).
*        tempString = includeName.
*        rc = sourceNode->set_attribute(
*          name = 'includeName' value = tempString ).
        READ REPORT includename INTO reportlist.
        reportstring = buildsourcestring( sourcetable = reportlist ).
        rc = sourcenode->if_ixml_node~set_value( reportstring ).
        rc = methodnode->append_child( sourcenode ).
        rc = rootnode->append_child( methodnode ).
      ENDIF.
*   other methods
    ELSE.
      clsmethkey-clsname = _classname.
      clsmethkey-cmpname = methoddescr-name.
      CLEAR methodproperties.

      IF methoddescr-is_redefined = 'X'.
        methodnode = xmldoc->create_element( 'method' ).
        MOVE-CORRESPONDING clsmethkey TO methodproperties.
*// ewh: begin of forward compatibility hack, can be removed for next
*//      major release-->
        READ TABLE redefinitions INTO redefinition
          WITH KEY mtdname = methoddescr-name.
        IF sy-subrc = 0.
          methodproperties-clsname = redefinition-refclsname.
        ENDIF.
*//<--ewH: end of forward compatibility hack
        setattributesfromstructure( node = methodnode structure =
        methodproperties ).
      ELSE.
        CALL FUNCTION 'SEO_METHOD_GET'
          EXPORTING
            mtdkey       = clsmethkey
          IMPORTING
            method       = methodproperties
          EXCEPTIONS
            not_existing = 1.
        IF sy-subrc = 0.
          methodnode = xmldoc->create_element( 'method' ).
          setattributesfromstructure( node = methodnode structure =
          methodproperties ).

*         parameters
          LOOP AT methoddescr-parameters INTO paramdescr.
            CLEAR paramproperties.
            parameternode = xmldoc->create_element( 'parameter' ).
            paramkey-cmpname = clsmethkey-cmpname.
            paramkey-sconame = paramdescr-name.
            paramkey-clsname = objname.
            CALL FUNCTION 'SEO_PARAMETER_GET'
              EXPORTING
                parkey    = paramkey
                version   = '1'
              IMPORTING
                parameter = paramproperties.
            setattributesfromstructure( node = parameternode
            structure = paramproperties ).
            rc = methodnode->append_child( parameternode ).
          ENDLOOP.

*         exceptions
          CALL FUNCTION 'SEO_METHOD_SIGNATURE_GET'
            EXPORTING
              mtdkey  = clsmethkey
              version = '1'
            IMPORTING
              exceps  = exceptionlist.
          LOOP AT exceptionlist INTO anexception.
            exceptionnode = xmldoc->create_element( 'exception' ).
            setattributesfromstructure( node = exceptionnode
            structure = anexception ).
            rc = methodnode->append_child( exceptionnode ).
          ENDLOOP.
        ENDIF. "method found
      ENDIF. "is_redefined?
*     source
      CALL METHOD cl_oo_classname_service=>get_method_include
        EXPORTING
          mtdkey              = methodkey
        RECEIVING
          result              = includename
        EXCEPTIONS
          method_not_existing = 1.
      IF sy-subrc = 0.
        READ REPORT includename INTO reportlist.
        reportstring = buildsourcestring( sourcetable = reportlist ).
        sourcenode = xmldoc->create_element( 'source' ).
        rc = sourcenode->if_ixml_node~set_value( reportstring ).
        rc = methodnode->append_child( sourcenode ).
      ENDIF.
** StartInsert Rich - Handle method documenation
      get_method_documentation(  EXPORTING method_key = methodkey
                                 CHANGING  rootnode   = methodnode ).
** EndInsert Rich - Handle method documenation
      rc = rootnode->append_child( methodnode ).
    ENDIF. "is_interface?
  ENDLOOP.
* create alias info for load.
  get_alias_method( EXPORTING it_methods     = classdescr->methods
                    CHANGING  xo_rootnode    = rootnode ).
* append root node to xmldoc
  rc = xmldoc->append_child( rootnode ).
  ixmldocument = xmldoc.
*// <--ewH: end of logic for interface methods & inheritance redesign
ENDMETHOD.


method CREATEOBJECTFROMIXMLDOC.
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*| Copyright 2014 SAPlink project members                              |
*|                                                                     |
*| Licensed under the Apache License, Version 2.0 (the "License");     |
*| you may not use this file except in compliance with the License.    |
*| You may obtain a copy of the License at                             |
*|                                                                     |
*|     http://www.apache.org/licenses/LICENSE-2.0                      |
*|                                                                     |
*| Unless required by applicable law or agreed to in writing, software |
*| distributed under the License is distributed on an "AS IS" BASIS,   |
*| WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or     |
*| implied.                                                            |
*| See the License for the specific language governing permissions and |
*| limitations under the License.                                      |
*\---------------------------------------------------------------------/
  DATA rootnode TYPE REF TO if_ixml_element.
  DATA classkey TYPE seoclskey.
  DATA filter TYPE REF TO if_ixml_node_filter.
  DATA iterator TYPE REF TO if_ixml_node_iterator.
  DATA node TYPE REF TO if_ixml_element.
  DATA otrnode TYPE REF TO if_ixml_element.
  DATA filter2 TYPE REF TO if_ixml_node_filter.
  DATA iterator2 TYPE REF TO if_ixml_node_iterator.
  DATA superclass TYPE vseoextend-clsname.
  DATA superclasskey TYPE vseoextend.
  DATA methodsourcenode TYPE REF TO if_ixml_node.
  DATA sourcenode TYPE REF TO if_ixml_node.
  DATA source TYPE string.
  DATA sourcetable TYPE TABLE OF string.
  DATA methodkey TYPE seocpdkey.
  DATA node2 TYPE REF TO if_ixml_element.
  DATA _objtype TYPE string.
  DATA aobjname TYPE e071-obj_name.
  DATA inheritancenode TYPE REF TO if_ixml_element.
  DATA redefnode TYPE REF TO if_ixml_element.
  DATA includename TYPE program.
  DATA mtdkey   TYPE seocpdkey.

*data excClass type ref to ZCX_SAPLINK.

*// --> begin of new data type rrq
  DATA:
*exporting dataTypes
  e_corrnr                 TYPE trkorr,
  e_devclass               TYPE devclass,
  e_version                TYPE seoversion,
  e_genflag                TYPE genflag,
  e_authority_check        TYPE seox_boolean,
  e_overwrite              TYPE seox_boolean,
*e_suppress_meth_gen      type SEOX_BOOLEAN,
*e_suppress_refac_gen     type SEOX_BOOLEAN,
  e_method_sources         TYPE seo_method_source_table,
  e_locals_def             TYPE rswsourcet,
  e_locals_imp             TYPE rswsourcet,
  e_locals_mac             TYPE rswsourcet,
*e_suppress_ind_update    type SEOX_BOOLEAN,
*importing dataTypes
  i_korrnr                 TYPE trkorr,
*changing dataTypes
  ch_class                 TYPE vseoclass,
  ch_inheritance           TYPE vseoextend,
  ch_redefinitions         TYPE seor_redefinitions_r,
  ch_implementings         TYPE seor_implementings_r,
  ch_impl_details          TYPE seo_redefinitions,
  ch_attributes            TYPE seoo_attributes_r,
  ch_methods               TYPE seoo_methods_r,
  ch_events                TYPE seoo_events_r,
  ch_types                 TYPE seoo_types_r,
  ch_type_source           TYPE seop_source,
  ch_type_source_temp      TYPE seop_source,
  ch_parameters            TYPE seos_parameters_r,
  ch_exceps                TYPE seos_exceptions_r,
  ch_aliases               TYPE seoo_aliases_r,
  ch_typepusages           TYPE seot_typepusages_r,
  ch_clsdeferrds           TYPE seot_clsdeferrds_r,
  ch_intdeferrds           TYPE seot_intdeferrds_r,
  ch_friendships           TYPE seo_friends,
**table dataTypes
*tb_classDescription      type table of seoclasstx,
*tb_component_descr       type table of seocompotx,
*tb_subcomponent_descr    type table of seosubcotx,
* work areas for the tables
  wa_attributes            TYPE seoo_attribute_r,
  wa_types                 TYPE seoo_type_r,
  wa_friends               TYPE seofriends,
  wa_implementings         TYPE seor_implementing_r,
  wa_redefinitions         TYPE seoredef,
  wa_methods               TYPE seoo_method_r,
  wa_parameters            TYPE seos_parameter_r,
  wa_exceps                TYPE seos_exception_r,
  wa_method_sources        TYPE seo_method_source,
  wa_events                TYPE seoo_event_r.
  DATA: lines TYPE i,
        l_msg TYPE string.
*//<-- end of new data types rrq

  CALL FUNCTION 'SEO_BUFFER_INIT'.

  e_devclass = devclass.
  _objtype = getobjecttype( ).
  e_overwrite = overwrite.
  xmldoc = ixmldocument.
  rootnode = xmldoc->find_from_name( _objtype ).

  CALL METHOD getstructurefromattributes
    EXPORTING
      node      = rootnode
    CHANGING
      structure = ch_class.

  objname = classkey-clsname = ch_class-clsname.
  ch_class-version = '0'.
  superclass = rootnode->get_attribute( name = 'REFCLSNAME' ).
  IF superclass IS NOT INITIAL.
* set something for inheritence
    superclasskey-clsname = classkey-clsname.
    superclasskey-refclsname = superclass.
    superclasskey-version = '0'.
    superclasskey-state = '1'.
    MOVE-CORRESPONDING superclasskey TO ch_inheritance.
    ch_inheritance-author = 'BCUSER'.
    ch_inheritance-createdon = sy-datum.
  ENDIF.

*Add attributes to new class
  DATA otrconcept TYPE sotr_text-concept.
  filter = xmldoc->create_filter_name( 'attribute' ).
  iterator = xmldoc->create_iterator_filtered( filter ).
  node ?= iterator->get_next( ).

  WHILE node IS NOT INITIAL.
*   create OTR texts if necessary (for exception classes)
    CLEAR otrconcept.
    otrnode = node->find_from_name( c_xml_key_sotr ).
    IF otrnode IS NOT INITIAL.
*     ewH:33-->create new concept with new guid
*      me->createotrfromnode( otrnode ).
      me->create_otr(
        EXPORTING node = otrnode
        IMPORTING concept = otrconcept ).
    ENDIF.
    CLEAR wa_attributes.
*   create attribute
    CALL METHOD getstructurefromattributes
      EXPORTING
        node      = node
      CHANGING
        structure = wa_attributes.
    wa_attributes-version = '0'.
*   ewH:issue33-->6.40 and above, must create new concept
    IF otrconcept IS NOT INITIAL.
      CONCATENATE `'` otrconcept `'` INTO wa_attributes-attvalue.
    ENDIF.
    APPEND wa_attributes TO ch_attributes.
    node ?= iterator->get_next( ).
  ENDWHILE.

*/***TPJ - Added Logic for TYPES  -------------------*/
*  DATA: types           TYPE seoo_types_r,
*        type_properties LIKE LINE OF types.

  filter = xmldoc->create_filter_name( 'types' ).
  iterator = xmldoc->create_iterator_filtered( filter ).
  node ?= iterator->get_next( ).
  WHILE node IS NOT INITIAL.
    CLEAR wa_types.
    CALL METHOD getstructurefromattributes
      EXPORTING
        node      = node
      CHANGING
        structure = wa_types.
    wa_types-version = '0'.
    APPEND wa_types TO ch_types.
    node ?= iterator->get_next( ).
  ENDWHILE.
*/***TPJ - End of Added Logic for TYPES  -------------------*/

*/***TPJ - Added Logic for Friends  -------------------*/
*  DATA: wa_friends type seofriends.

  filter = xmldoc->create_filter_name( C_XML_KEY_FRIENDS ).
  iterator = xmldoc->create_iterator_filtered( filter ).
  node ?= iterator->get_next( ).
  WHILE node IS NOT INITIAL.
    CLEAR wa_friends.
    CALL METHOD getstructurefromattributes
      EXPORTING
        node      = node
      CHANGING
        structure = wa_friends.
    wa_friends-version = '0'.
    APPEND wa_friends TO ch_friendships.
    node ?= iterator->get_next( ).
  ENDWHILE.
*/***TPJ - End of Added Logic for Friends  -------------------*/

*// ewH: Added Logic for Implementings(interfaces)-->
  filter = xmldoc->create_filter_name( 'implementing' ).
  iterator = xmldoc->create_iterator_filtered( filter ).
  node ?= iterator->get_next( ).
  WHILE node IS NOT INITIAL.
    CLEAR wa_implementings.
    CALL METHOD getstructurefromattributes
      EXPORTING
        node      = node
      CHANGING
        structure = wa_implementings.
    APPEND wa_implementings TO ch_implementings.
    node ?= iterator->get_next( ).
  ENDWHILE.
*//<--ewH: End of Added Logic for Implementings(interfaces)

*// rrq: Added Logic for events-->
  filter = xmldoc->create_filter_name( 'events' ).
  iterator = xmldoc->create_iterator_filtered( filter ).
  node ?= iterator->get_next( ).
  WHILE node IS NOT INITIAL.
    CLEAR wa_events.
    CALL METHOD getstructurefromattributes
      EXPORTING
        node      = node
      CHANGING
        structure = wa_events.
    APPEND wa_events TO ch_events.
    filter2 = node->create_filter_name( 'parameter' ).
    iterator2 = node->create_iterator_filtered( filter2 ).
    node2 ?= iterator2->get_next( ).
    WHILE node2 IS NOT INITIAL.
      CLEAR wa_parameters.
      CALL METHOD getstructurefromattributes
        EXPORTING
          node      = node2
        CHANGING
          structure = wa_parameters.

      "//-> Mar: Added logic for parameter/interface implementation - 08/20/2008
      IF NOT wa_parameters-clsname IS INITIAL.
        APPEND wa_parameters TO ch_parameters.
      ENDIF.
      "//<- Mar: Added logic for parameter/interface implementation - 08/20/2008

      node2 ?= iterator2->get_next( ).
    ENDWHILE.
    node ?= iterator->get_next( ).
  ENDWHILE.
*//<--rrq: End of Added Logic for events

*// ewH: start redesign method/inheritances-->
* inheritance
  inheritancenode = rootnode->find_from_name( c_xml_key_inheritance ).
  IF inheritancenode IS BOUND.
    CALL METHOD getstructurefromattributes
      EXPORTING
        node      = inheritancenode
      CHANGING
        structure = ch_inheritance.
*   redefs
    filter = inheritancenode->create_filter_name( 'redefinition' ).
    iterator = inheritancenode->create_iterator_filtered( filter ).
    redefnode ?= iterator->get_next( ).
    WHILE redefnode IS NOT INITIAL.
      CALL METHOD getstructurefromattributes
        EXPORTING
          node      = redefnode
        CHANGING
          structure = wa_redefinitions.
      APPEND wa_redefinitions TO ch_redefinitions.
      redefnode ?= iterator->get_next( ).
    ENDWHILE.
  ENDIF.

*Add Methods to new class
  filter = xmldoc->create_filter_name( 'method' ).
  iterator = xmldoc->create_iterator_filtered( filter ).
  node ?= iterator->get_next( ).
  WHILE node IS NOT INITIAL.
    CLEAR wa_methods.
    CALL METHOD getstructurefromattributes
      EXPORTING
        node      = node
      CHANGING
        structure = wa_methods.

*   only create metadata if method is not a redefinition
    READ TABLE ch_redefinitions INTO wa_redefinitions
    WITH KEY mtdname = wa_methods-cmpname.
    IF sy-subrc = 0.
      node ?= iterator->get_next( ).
      CONTINUE.
    ENDIF.
*// ewh: begin of backward compatibility hack, can be removed for next
*//      major release-->
    IF wa_methods-clsname <> ch_class-clsname.
      MOVE-CORRESPONDING wa_methods TO wa_redefinitions.
      wa_redefinitions-clsname = ch_class-clsname.
      wa_redefinitions-refclsname = wa_methods-clsname.
      wa_redefinitions-version = '0'.
      wa_redefinitions-mtdabstrct = ''.
      wa_redefinitions-mtdname = wa_methods-cmpname.
      APPEND wa_redefinitions TO ch_redefinitions.

      node ?= iterator->get_next( ).
      CONTINUE.
    ENDIF.
*// <--ewH: break in backward compatibility hack - 2Bcontinued below

    filter2 = node->create_filter_name( 'parameter' ).
    iterator2 = node->create_iterator_filtered( filter2 ).
    node2 ?= iterator2->get_next( ).
    WHILE node2 IS NOT INITIAL.
      CLEAR wa_parameters.
      CALL METHOD getstructurefromattributes
        EXPORTING
          node      = node2
        CHANGING
          structure = wa_parameters.

      "//-> Mar: Added logic for parameter/interface implementation - 08/20/2008
      IF NOT wa_parameters-clsname IS INITIAL.
        APPEND wa_parameters TO ch_parameters.
      ENDIF.
      "//<- Mar: Added logic for parameter/interface implementation - 08/20/2008

      node2 ?= iterator2->get_next( ).
    ENDWHILE.
    filter2 = node->create_filter_name( 'exception' ).
    iterator2 = node->create_iterator_filtered( filter2 ).
    node2 ?= iterator2->get_next( ).
    WHILE node2 IS NOT INITIAL.
      CALL METHOD getstructurefromattributes
        EXPORTING
          node      = node2
        CHANGING
          structure = wa_exceps.
      APPEND wa_exceps TO ch_exceps.
      node2 ?= iterator2->get_next( ).
    ENDWHILE.
    APPEND wa_methods TO ch_methods.

** StartInsert Rich - Handle method documenation
    create_method_documentation( node = node ).
** EndInsert Rich - Handle method documenation

    node ?= iterator->get_next( ).
  ENDWHILE.
*// <--ewH: end redesign method/inheritances
*// ewh: continuation of backward compatibility hack-->
*  IF ( ch_redefinitions IS NOT INITIAL OR superclass-clsname
*  IS NOT INITIAL ) and ch_inheritance is initial.
*    CALL FUNCTION 'SEO_INHERITANC_CREATE_F_DATA'
*      EXPORTING
*        save          = ' '
*      CHANGING
*        inheritance   = superclasskey
*        redefinitions = ch_redefinitions.
*  ENDIF.
*// <--ewH: end of backward compatibility hack

  create_typepusage( CHANGING xt_typepusages = ch_typepusages ).
  create_clsdeferrd( CHANGING xt_clsdeferrds = ch_clsdeferrds ).
  create_intdeferrd( CHANGING xt_intdeferrds = ch_intdeferrds ).

*Insert source code into the methods
  filter = xmldoc->create_filter_name( 'method' ).
  iterator = xmldoc->create_iterator_filtered( filter ).
  node ?= iterator->get_next( ).

  WHILE node IS NOT INITIAL.
    CALL METHOD getstructurefromattributes
      EXPORTING
        node      = node
      CHANGING
        structure = wa_methods.
    methodkey-clsname = objname.
    methodkey-cpdname = wa_methods-cmpname.
    aobjname = methodkey.
    methodsourcenode = node->find_from_name( 'source' ).
    IF methodsourcenode IS NOT INITIAL.
      CLEAR wa_method_sources.
      source = methodsourcenode->get_value( ).
      sourcetable = buildtablefromstring( source ).
      READ TABLE ch_redefinitions INTO wa_redefinitions
      WITH KEY mtdname = methodkey-cpdname.
      IF sy-subrc = 0.
        wa_method_sources-redefine = 'X'.
      ENDIF.
      wa_method_sources-cpdname = methodkey-cpdname.
      wa_method_sources-source = sourcetable.
      APPEND wa_method_sources TO e_method_sources.
    ENDIF.
    node ?= iterator->get_next( ).
  ENDWHILE.
*
**// ewH: create interface methods-->
  filter = xmldoc->create_filter_name( 'interfaceMethod' ).
  iterator = xmldoc->create_iterator_filtered( filter ).
  node ?= iterator->get_next( ).

  WHILE node IS NOT INITIAL.
    CALL METHOD getstructurefromattributes
      EXPORTING
        node      = node
      CHANGING
        structure = methodkey.
    aobjname = methodkey.
    methodsourcenode = node->find_from_name( 'source' ).
    IF methodsourcenode IS NOT INITIAL.
      CLEAR wa_method_sources.
      source = methodsourcenode->get_value( ).
      sourcetable = buildtablefromstring( source ).
      wa_method_sources-cpdname = methodkey-cpdname.
      READ TABLE ch_redefinitions INTO wa_redefinitions
      WITH KEY mtdname = methodkey-cpdname.
      IF sy-subrc = 0.
        wa_method_sources-redefine = 'X'.
      ENDIF.
*      wa_method_sources-redefine = wa_methods-redefin.
      wa_method_sources-source = sourcetable.

      APPEND wa_method_sources TO e_method_sources.
    ENDIF.

    node ?= iterator->get_next( ).
  ENDWHILE.
*// <--ewH: end create interface methods

* local implementation
  DATA _classname TYPE seoclsname.
  _classname = objname.
  sourcenode = xmldoc->find_from_name( 'localImplementation' ).
  IF sourcenode IS NOT INITIAL.
    source = sourcenode->get_value( ).
    e_locals_imp = buildtablefromstring( source ).
  ENDIF.

* local types
  sourcenode = xmldoc->find_from_name( 'localTypes' ).
  IF sourcenode IS NOT INITIAL.
    source = sourcenode->get_value( ).
    e_locals_def = buildtablefromstring( source ).
  ENDIF.

* local macros
  sourcenode = xmldoc->find_from_name( 'localMacros' ).
  IF sourcenode IS NOT INITIAL.
    source = sourcenode->get_value( ).
    e_locals_mac = buildtablefromstring( source ).
  ENDIF.
* We don't need the sections for now. Code moved by Rene
  create_sections( ).

*Add Alias to new class
  create_alias_method( CHANGING xt_aliases_method = ch_aliases ).

  name = objname.

  CALL FUNCTION 'SEO_CLASS_CREATE_COMPLETE'
   EXPORTING
     corrnr                             = e_corrnr
     devclass                           = e_devclass
     version                            = e_version
     genflag                            = e_genflag
     authority_check                    = e_authority_check
     overwrite                          = e_overwrite
*   SUPPRESS_METHOD_GENERATION         = e_suppress_meth_gen
*   SUPPRESS_REFACTORING_SUPPORT       = e_suppress_refac_gen
*     method_sources                     = e_method_sources
     locals_def                         = e_locals_def
     locals_imp                         = e_locals_imp
     locals_mac                         = e_locals_mac
*   SUPPRESS_INDEX_UPDATE              = e_suppress_ind_update
   IMPORTING
     korrnr                             = i_korrnr
* TABLES
*   CLASS_DESCRIPTIONS                 = tb_classDescription
*   COMPONENT_DESCRIPTIONS             = tb_component_descr
*   SUBCOMPONENT_DESCRIPTIONS          = tb_subcomponent_descr
    CHANGING
      class                              = ch_class
     inheritance                        = ch_inheritance
     redefinitions                      = ch_redefinitions
     implementings                      = ch_implementings
     impl_details                       = ch_impl_details
     attributes                         = ch_attributes
     methods                            = ch_methods
     events                             = ch_events
     types                              = ch_types
*   TYPE_SOURCE                        = ch_type_source "???
     PARAMETERS                         = ch_parameters
     exceps                             = ch_exceps
     aliases                            = ch_aliases
     typepusages                        = ch_typepusages
     clsdeferrds                        = ch_clsdeferrds
     intdeferrds                        = ch_intdeferrds
     friendships                        = ch_friendships
   EXCEPTIONS
     existing                           = 1
     is_interface                       = 2
     db_error                           = 3
     component_error                    = 4
     no_access                          = 5
     other                              = 6
     OTHERS                             = 7.
  CASE sy-subrc.
    WHEN '0'.
** i guess if we made it this far, we will assume success
** successful install
    WHEN '1'.
      RAISE EXCEPTION TYPE zcx_saplink
        EXPORTING
          textid = zcx_saplink=>existing.
    WHEN OTHERS.
      RAISE EXCEPTION TYPE zcx_saplink
        EXPORTING
          textid = zcx_saplink=>system_error.
  ENDCASE.
* Now let's add the methods
  LOOP AT e_method_sources INTO wa_method_sources.
    mtdkey-clsname = objname.
    mtdkey-cpdname = wa_method_sources-cpdname.

    CALL FUNCTION 'SEO_METHOD_GENERATE_INCLUDE'
      EXPORTING
        mtdkey                               = mtdkey
        version                              = e_version
        force                                = e_overwrite
        redefine                             = wa_method_sources-redefine
*     SUPPRESS_CORR                        = SEOX_FALSE
        implementation_expanded              = wa_method_sources-source
*     IMPLEMENTATION                       =
        suppress_mtdkey_check                = seox_true
*     EDITOR_LOCK                          = SEOX_FALSE
*     GENERATED                            = SEOX_FALSE
        corrnr                               = e_corrnr
        without_method_frame                 = seox_true
*     WITH_SUPER_CALL                      = SEOX_FALSE
*     SUPPRESS_INDEX_UPDATE                = SEOX_FALSE
*     EXTEND                               = SEOX_FALSE
*     ENHANCEMENT                          = ' '
*     SUPPRESS_MODIFICATION_SUPPORT        = SEOX_FALSE
   EXCEPTIONS
     not_existing                         = 1
     model_only                           = 2
     include_existing                     = 3
     method_imp_not_generated             = 4
     method_imp_not_initialised           = 5
     _internal_class_not_existing         = 6
     _internal_method_overflow            = 7
     cancelled                            = 8
     method_is_abstract_implemented       = 9
     method_is_final_implemented          = 10
     internal_error_insert_report         = 11
     OTHERS                               = 12
              .
    CASE sy-subrc.
      WHEN '0'.
** i guess if we made it this far, we will assume success
** successful install
      WHEN '3'.
        l_msg = mtdkey.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING
            textid = zcx_saplink=>existing
            msg    = l_msg.
      WHEN OTHERS.
        l_msg = mtdkey.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING
            textid = zcx_saplink=>system_error
            msg    = l_msg.
    ENDCASE.
  ENDLOOP.

*ewH:insert pub, prot, and priv sections manually to keep any direct
* attribute/type definitions
  aobjname = classkey-clsname.
**public
  sourcenode = xmldoc->find_from_name( 'publicSection' ).
  IF sourcenode IS NOT INITIAL.
    includename = cl_oo_classname_service=>get_pubsec_name( _classname ).
    source = sourcenode->get_value( ).
    sourcetable = buildtablefromstring( source ).
    INSERT REPORT includename FROM sourcetable EXTENSION TYPE
    srext_ext_class_public STATE 'I'.
  ENDIF.

**protected
  sourcenode = xmldoc->find_from_name( 'protectedSection' ).
  IF sourcenode IS NOT INITIAL.
    includename = cl_oo_classname_service=>get_prosec_name( _classname ).
    source = sourcenode->get_value( ).
    sourcetable = buildtablefromstring( source ).
    INSERT REPORT includename FROM sourcetable EXTENSION TYPE
    srext_ext_class_protected STATE 'I'.
  ENDIF.

**private
  sourcenode = xmldoc->find_from_name( 'privateSection' ).
  IF sourcenode IS NOT INITIAL.
    includename = cl_oo_classname_service=>get_prisec_name( _classname ).
    source = sourcenode->get_value( ).
    sourcetable = buildtablefromstring( source ).
    INSERT REPORT includename FROM sourcetable EXTENSION TYPE
    srext_ext_class_private STATE 'I'.
  ENDIF.
*/***EVP - Added Logic for Local Test Classes  -------------------*/
**local test classes
  sourcenode = xmldoc->find_from_name( 'localTestClasses' ).
  IF sourcenode IS NOT INITIAL.
    DATA clskey TYPE seoclskey.
    source = sourcenode->get_value( ).
    sourcetable = buildtablefromstring( source ).

    clskey-clsname = _classname.
    CALL FUNCTION 'SEO_CLASS_GENERATE_LOCALS'
      EXPORTING
        clskey                 = clskey
        force                  = overwrite
        locals_testclasses     = sourcetable
      EXCEPTIONS
        not_existing           = 1
        model_only             = 2
        locals_not_generated   = 3
        locals_not_initialised = 4
        OTHERS                 = 5.
    IF sy-subrc <> 0.
    ENDIF.
  ENDIF.
*/***EVP - End Of Added Logic for Local Test Classes  -------------------*/

**// Rich:  Start
* Create class textpool
  create_textpool( ).

  create_documentation( ).
**// Rich:  End

* insert inactive sections into worklist
  CALL FUNCTION 'RS_INSERT_INTO_WORKING_AREA'
    EXPORTING
      object            = 'CPUB'
      obj_name          = aobjname
    EXCEPTIONS
      wrong_object_name = 1.
  IF sy-subrc <> 0.
  ENDIF.

  CALL FUNCTION 'RS_INSERT_INTO_WORKING_AREA'
    EXPORTING
      object            = 'CPRO'
      obj_name          = aobjname
    EXCEPTIONS
      wrong_object_name = 1.
  IF sy-subrc <> 0.
  ENDIF.

  CALL FUNCTION 'RS_INSERT_INTO_WORKING_AREA'
    EXPORTING
      object            = 'CPRI'
      obj_name          = aobjname
    EXCEPTIONS
      wrong_object_name = 1.
  IF sy-subrc <> 0.
  ENDIF.


endmethod.


method CREATE_DOCUMENTATION.
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*| Copyright 2014 SAPlink project members                              |
*|                                                                     |
*| Licensed under the Apache License, Version 2.0 (the "License");     |
*| you may not use this file except in compliance with the License.    |
*| You may obtain a copy of the License at                             |
*|                                                                     |
*|     http://www.apache.org/licenses/LICENSE-2.0                      |
*|                                                                     |
*| Unless required by applicable law or agreed to in writing, software |
*| distributed under the License is distributed on an "AS IS" BASIS,   |
*| WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or     |
*| implied.                                                            |
*| See the License for the specific language governing permissions and |
*| limitations under the License.                                      |
*\---------------------------------------------------------------------/
  DATA txtline_node     TYPE REF TO if_ixml_element.
  DATA txtline_filter   TYPE REF TO if_ixml_node_filter.
  DATA txtline_iterator TYPE REF TO if_ixml_node_iterator.

  DATA docnode          TYPE REF TO if_ixml_element.

  DATA lang_node        TYPE REF TO if_ixml_element.
  DATA lang_filter      TYPE REF TO if_ixml_node_filter.
  DATA lang_iterator    TYPE REF TO if_ixml_node_iterator.

  DATA obj_name TYPE dokhl-object.
  DATA class_name TYPE string.
  DATA language  TYPE string.
  DATA obj_langu TYPE dokhl-langu.
  DATA lv_str TYPE string.
  DATA rc TYPE sy-subrc.

  DATA lt_lines  TYPE TABLE OF tline.
  FIELD-SYMBOLS: <ls_lines> LIKE LINE OF lt_lines.

  docnode = xmldoc->find_from_name( c_xml_key_class_documentation ).

  IF docnode IS NOT BOUND.
    RETURN.
  ENDIF.

  class_name = docnode->get_attribute( name = c_xml_key_object ).
  obj_name = class_name.

* If no class name, then there was no class documenation, just return.
  IF class_name IS INITIAL.
    RETURN.
  ENDIF.

* Get languages from XML
  FREE: lang_filter, lang_iterator, lang_node.
  lang_filter = docnode->create_filter_name( c_xml_key_language ).
  lang_iterator = docnode->create_iterator_filtered( lang_filter ).
  lang_node ?= lang_iterator->get_next( ).
  WHILE lang_node IS NOT INITIAL.

    REFRESH lt_lines.
    language = lang_node->get_attribute( name = c_xml_key_spras ).
    obj_langu = language.

* Get TextLines from XML
    FREE: txtline_filter, txtline_iterator, txtline_node.
    txtline_filter = lang_node->create_filter_name( c_xml_key_textline ).
    txtline_iterator = lang_node->create_iterator_filtered( txtline_filter ).
    txtline_node ?= txtline_iterator->get_next( ).
    WHILE txtline_node IS NOT INITIAL.
      APPEND INITIAL LINE TO lt_lines ASSIGNING <ls_lines>.
      me->getstructurefromattributes(
              EXPORTING   node      = txtline_node
              CHANGING    structure = <ls_lines> ).
      txtline_node ?= txtline_iterator->get_next( ).
    ENDWHILE.

* Delete any documentation that may currently exist.
    CALL FUNCTION 'DOCU_DEL'
      EXPORTING
        id       = 'CL'
        langu    = obj_langu
        object   = obj_name
        typ      = 'E'
      EXCEPTIONS
        ret_code = 1
        OTHERS   = 2.

* Now update with new documentation text
    CALL FUNCTION 'DOCU_UPD'
      EXPORTING
        id       = 'CL'
        langu    = obj_langu
        object   = obj_name
        typ      = 'E'
      TABLES
        line     = lt_lines
      EXCEPTIONS
        ret_code = 1
        OTHERS   = 2.
    IF sy-subrc <> 0.
      RAISE EXCEPTION TYPE zcx_saplink
        EXPORTING
          textid = zcx_saplink=>error_message
          msg    = `Class Documentation object import failed`.
    ENDIF.

    lang_node ?= lang_iterator->get_next( ).
  ENDWHILE.

endmethod.


method CREATE_METHOD_DOCUMENTATION.
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*| Copyright 2014 SAPlink project members                              |
*|                                                                     |
*| Licensed under the Apache License, Version 2.0 (the "License");     |
*| you may not use this file except in compliance with the License.    |
*| You may obtain a copy of the License at                             |
*|                                                                     |
*|     http://www.apache.org/licenses/LICENSE-2.0                      |
*|                                                                     |
*| Unless required by applicable law or agreed to in writing, software |
*| distributed under the License is distributed on an "AS IS" BASIS,   |
*| WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or     |
*| implied.                                                            |
*| See the License for the specific language governing permissions and |
*| limitations under the License.                                      |
*\---------------------------------------------------------------------/
  DATA txtline_node     TYPE REF TO if_ixml_element.
  DATA txtline_filter   TYPE REF TO if_ixml_node_filter.
  DATA txtline_iterator TYPE REF TO if_ixml_node_iterator.

  data: methdocnode     TYPE REF TO if_ixml_element.

  DATA lang_node        TYPE REF TO if_ixml_element.
  DATA lang_filter      TYPE REF TO if_ixml_node_filter.
  DATA lang_iterator    TYPE REF TO if_ixml_node_iterator.

  data obj_name type DOKHL-OBJECT.
  data classmeth_name type string.
  data language  type string.
  data obj_langu type DOKHL-LANGU.
  data lv_str type string.
  data rc type sy-subrc.

  DATA lt_lines  TYPE TABLE OF tline.
  FIELD-SYMBOLS: <ls_lines> LIKE LINE OF lt_lines.

  methdocnode = node->find_from_name( 'methodDocumentation' ).

  if methdocnode is not bound.
    return.
  endif.

  classmeth_name = methdocNode->get_attribute( name = 'OBJECT' ).
  obj_name = classmeth_name.

* If no class method name, then there was no class method documenation, just return.
  if classmeth_name is initial.
    return.
  endif.

* Get languages from XML
  FREE: lang_filter, lang_iterator, lang_node.
  lang_filter = methdocNode->create_filter_name( `language` ).
  lang_iterator = methdocNode->create_iterator_filtered( lang_filter ).
  lang_node ?= lang_iterator->get_next( ).
  WHILE lang_node IS NOT INITIAL.

    refresh lt_lines.
    language = lang_node->get_attribute( name = 'SPRAS' ).
    obj_langu = language.

* Get TextLines from XML
    FREE: txtline_filter, txtline_iterator, txtline_node.
    txtline_filter = lang_node->create_filter_name( `textLine` ).
    txtline_iterator = lang_node->create_iterator_filtered( txtline_filter ).
    txtline_node ?= txtline_iterator->get_next( ).
    WHILE txtline_node IS NOT INITIAL.
      APPEND INITIAL LINE TO lt_lines ASSIGNING <ls_lines>.
      me->getstructurefromattributes(
              EXPORTING   node      = txtline_node
              CHANGING    structure = <ls_lines> ).
      txtline_node ?= txtline_iterator->get_next( ).
    ENDWHILE.

* Delete any documentation that may currently exist.
    CALL FUNCTION 'DOCU_DEL'
      EXPORTING
        id       = 'CO'
        langu    = obj_langu
        object   = obj_name
        typ      = 'E'
      EXCEPTIONS
        ret_code = 1
        OTHERS   = 2.

* Now update with new documentation text
    CALL FUNCTION 'DOCU_UPD'
      EXPORTING
        id       = 'CO'
        langu    = obj_langu
        object   = obj_name
        typ      = 'E'
      TABLES
        line     = lt_lines
      EXCEPTIONS
        ret_code = 1
        OTHERS   = 2.
    IF sy-subrc <> 0.
      RAISE EXCEPTION TYPE zcx_saplink
        EXPORTING
          textid = zcx_saplink=>error_message
          msg    = `Class Method Documentation object import failed`.
    ENDIF.

    lang_node ?= lang_iterator->get_next( ).
  ENDWHILE.

endmethod.


method CREATE_SECTIONS.

*ewH-not sure how this type_source param works. type sources can come
* from private or protected sections, but there is no way to pass
* these separately into the class create FM. After debugging into
* FM->clif_save_all->generate_classpool it treats the source table
* as one, so I am not sure how to get it to differentiate between
* private and protected sections. If only one section has types
* defined, the FM call works, otherwise all hell breaks loose. To
* solve the problem for now, we will just do an insert report for
* the sections after the class creation, since that's all the FM
* does in the end anyway. Wow, this is a really long comment, but
* I dont want to have to try to remember what the hell was going
* on here later...sorry.  :)
*insert code for publicSection
*  sourcenode = xmldoc->find_from_name( 'publicSection' )
*  IF sourcenode IS NOT INITIAL.
*    source = sourcenode->get_value( ).
*    ch_type_source = buildtablefromstring( source ).
*  ENDIF.
**insert code for pivateSection
*  sourcenode = xmldoc->find_from_name( 'privateSection' ).
*  IF sourcenode IS NOT INITIAL.
*    source = sourcenode->get_value( ).
*    ch_type_source_temp = buildtablefromstring( source ).
*    append lines of ch_type_source_temp to ch_type_source.
*  ENDIF.
**insert code for ProtectedSection
*  sourcenode = xmldoc->find_from_name( 'protectedSection' ).
*  IF sourcenode IS NOT INITIAL.
*    source = sourcenode->get_value( ).
*    ch_type_source_temp = buildtablefromstring( source ).
*    append lines of ch_type_source_temp to ch_type_source.
*  ENDIF.

endmethod.


method CREATE_TEXTPOOL.
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*| Copyright 2014 SAPlink project members                              |
*|                                                                     |
*| Licensed under the Apache License, Version 2.0 (the "License");     |
*| you may not use this file except in compliance with the License.    |
*| You may obtain a copy of the License at                             |
*|                                                                     |
*|     http://www.apache.org/licenses/LICENSE-2.0                      |
*|                                                                     |
*| Unless required by applicable law or agreed to in writing, software |
*| distributed under the License is distributed on an "AS IS" BASIS,   |
*| WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or     |
*| implied.                                                            |
*| See the License for the specific language governing permissions and |
*| limitations under the License.                                      |
*\---------------------------------------------------------------------/
  data textPoolTable type standard table of textPool.
  data textPoolRow type textPool.
  data langIterator type ref to if_ixml_node_iterator.
  data filter type ref to if_ixml_node_filter.
  data textFilter type ref to if_ixml_node_filter.
  data textIterator type ref to if_ixml_node_iterator.
  data textpoolnode type ref to if_ixml_element.
  data langNode type ref to if_ixml_element.
  data aTextNode type ref to if_ixml_element.
  data _objName type TROBJ_NAME.
  data obj_name type SEOCLSNAME.
  data lang type spras.
  data langNodeExists type flag.
*  data logonLanguageExists type flag.                  " del #255 - seemingly not used
  data _state(1) type c.
  data classpoolname type program.
  DATA lv_original_language TYPE sylangu.                " ins #255

  textpoolnode = xmldoc->find_from_name( 'textPool' ).

  if textpoolnode is not bound.
    return.
  endif.

*--------------------------------------------------------------------*
* Ticket #255 - Error importing texts when logon language different
*               then original language of class
*--------------------------------------------------------------------*
  textpoolnode = xmldoc->find_from_name( 'CLAS' ).              " ins #255
  lv_original_language = textpoolnode->get_attribute( 'LANGU' )." ins #255
  SET LANGUAGE lv_original_language. " ins #255
  " Gregor Wolf: With this all languages from the Nugget/Slinkee are imported

  obj_name = objName.
  classpoolname = cl_oo_classname_service=>GET_CLASSPOOL_NAME( obj_Name ).
  _objName = classpoolname.

  filter = textPoolNode->create_filter_name( 'language' ).
  langIterator = textPoolNode->create_iterator_filtered( filter ).
  langNode ?= langIterator->get_next( ).

  while langNode is not initial.
    langNodeExists = 'X'.

    CALL FUNCTION 'RS_INSERT_INTO_WORKING_AREA'
      EXPORTING
        OBJECT   = 'REPT'
        OBJ_NAME = _objName
      EXCEPTIONS
        OTHERS   = 0.
    refresh textPoolTable.
    textIterator = langNode->create_iterator( ).
    aTextNode ?= textIterator->get_next( ).
*For some reason the 1st one is blank... not sure why.
    aTextNode ?= textIterator->get_next( ).
    while aTextNode is not initial.
      getstructurefromattributes(
        EXPORTING
          node            = aTextNode
        CHANGING
          structure       = textPoolRow
      ).
      append textPoolRow to textPoolTable.
      aTextNode ?= textIterator->get_next( ).
    endwhile.
    if textPoolTable is not initial.
      lang = langNode->get_attribute( 'SPRAS' ).
*      if lang = sy-langu.                " del #255 - replaced by original language
      IF lang = lv_original_language.    " ins #255 - replaced former coding
*        logonLanguageExists = 'X'.
        _state = 'I'.
      else.
*       seems that if a textpool is inserted as inactive for language
*       other than the logon language, it is lost upon activation
*       not sure inserting as active is best solution,but seems to work
*       Stefan Schmöcker:  Looks like this does not trigger on logon- " ins #255
*                          but on class original language             " ins #255
        _state = 'A'.
      endif.
      insert textpool _objName
        from textPooltable
        language lang
        state    _state.
    endif.
    langNode ?= langIterator->get_next( ).
  endwhile.
endmethod.


method DELETEOBJECT.
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*| Copyright 2014 SAPlink project members                              |
*|                                                                     |
*| Licensed under the Apache License, Version 2.0 (the "License");     |
*| you may not use this file except in compliance with the License.    |
*| You may obtain a copy of the License at                             |
*|                                                                     |
*|     http://www.apache.org/licenses/LICENSE-2.0                      |
*|                                                                     |
*| Unless required by applicable law or agreed to in writing, software |
*| distributed under the License is distributed on an "AS IS" BASIS,   |
*| WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or     |
*| implied.                                                            |
*| See the License for the specific language governing permissions and |
*| limitations under the License.                                      |
*\---------------------------------------------------------------------/
data clsKey type SEOCLSKEY.

  clsKey-clsname = objname.
  CALL FUNCTION 'SEO_CLASS_DELETE_W_DEPS'
    EXPORTING
      clskey             = clsKey
    EXCEPTIONS
     NOT_EXISTING       = 1
     IS_INTERFACE       = 2
     NOT_DELETED        = 3
     DB_ERROR           = 4
     OTHERS             = 5
            .
  if sy-subrc <> 0.
    case sy-subrc.
      when 1.
        raise exception type zcx_saplink
          exporting textid = zcx_saplink=>not_found.
      when 2.
        raise exception type zcx_saplink
          exporting
            textid = zcx_saplink=>error_message
            msg = 'interfaces not supported'.
      when 3.
        raise exception type zcx_saplink
          exporting
            textid = zcx_saplink=>error_message
            msg = 'class not deleted'.
      when others.
        raise exception type zcx_saplink
          exporting textid = zcx_saplink=>system_error.
    endcase.
  endif.
endmethod.


method FINDIMPLEMENTINGCLASS.
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*| Copyright 2014 SAPlink project members                              |
*|                                                                     |
*| Licensed under the Apache License, Version 2.0 (the "License");     |
*| you may not use this file except in compliance with the License.    |
*| You may obtain a copy of the License at                             |
*|                                                                     |
*|     http://www.apache.org/licenses/LICENSE-2.0                      |
*|                                                                     |
*| Unless required by applicable law or agreed to in writing, software |
*| distributed under the License is distributed on an "AS IS" BASIS,   |
*| WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or     |
*| implied.                                                            |
*| See the License for the specific language governing permissions and |
*| limitations under the License.                                      |
*\---------------------------------------------------------------------/
data methodKey type SEOCMPKEY.
data methodProperties type VSEOMETHOD.
data classDescr type ref to cl_abap_classdescr.
data superClass type ref to cl_abap_typeDescr.
data superClassName type string.

  if startClass is initial.
    methodKey-CLSNAME = objName.
  else.
    methodKey-clsName = startClass.
  endif.
  methodKey-CMPNAME = methodName.

  call function 'SEO_METHOD_GET'
        exporting
          MTDKEY = methodKey
        importing
          method = methodProperties
        exceptions
          NOT_EXISTING = 1.
  if sy-subrc = 0.
    className = methodProperties-clsname.
  else.
    classDescr ?= cl_abap_classDescr=>describe_by_name(
    methodKey-clsName ).
    call method classDescr->GET_SUPER_CLASS_TYPE
        receiving
         P_DESCR_REF = superClass
        exceptions
          SUPER_CLASS_NOT_FOUND = 1.
    superClassName = superClass->GET_RELATIVE_NAME( ).
    className = FINDIMPLEMENTINGCLASS( methodName = methodName
    startClass = superCLassName ).
  endif.
endmethod.


method GETOBJECTTYPE.
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*| Copyright 2014 SAPlink project members                              |
*|                                                                     |
*| Licensed under the Apache License, Version 2.0 (the "License");     |
*| you may not use this file except in compliance with the License.    |
*| You may obtain a copy of the License at                             |
*|                                                                     |
*|     http://www.apache.org/licenses/LICENSE-2.0                      |
*|                                                                     |
*| Unless required by applicable law or agreed to in writing, software |
*| distributed under the License is distributed on an "AS IS" BASIS,   |
*| WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or     |
*| implied.                                                            |
*| See the License for the specific language governing permissions and |
*| limitations under the License.                                      |
*\---------------------------------------------------------------------/

  objecttype = 'CLAS'.  "Class

endmethod.


method GET_DOCUMENTATION.
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*| Copyright 2014 SAPlink project members                              |
*|                                                                     |
*| Licensed under the Apache License, Version 2.0 (the "License");     |
*| you may not use this file except in compliance with the License.    |
*| You may obtain a copy of the License at                             |
*|                                                                     |
*|     http://www.apache.org/licenses/LICENSE-2.0                      |
*|                                                                     |
*| Unless required by applicable law or agreed to in writing, software |
*| distributed under the License is distributed on an "AS IS" BASIS,   |
*| WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or     |
*| implied.                                                            |
*| See the License for the specific language governing permissions and |
*| limitations under the License.                                      |
*\---------------------------------------------------------------------/
  DATA languagenode   TYPE REF TO if_ixml_element.
  DATA docnode       TYPE REF TO if_ixml_element.
  DATA txtlines_node TYPE REF TO if_ixml_element.
  DATA rc            TYPE sysubrc.
  DATA _objtype      TYPE string.

  TYPES: BEGIN OF t_dokhl,
          id          TYPE dokhl-id,
          object      TYPE dokhl-object,
          langu       TYPE dokhl-langu,
          typ         TYPE dokhl-typ,
          dokversion  TYPE dokhl-dokversion,
         END OF t_dokhl.

  DATA lt_dokhl TYPE TABLE OF t_dokhl.
  DATA ls_dokhl LIKE LINE OF lt_dokhl.

  DATA lt_lines TYPE TABLE OF tline.
  DATA ls_lines LIKE LINE OF lt_lines.

  DATA lv_str TYPE string.
  DATA _objname TYPE e071-obj_name.

  _objname = objname.

* Check against database
  SELECT  id object langu typ dokversion
        INTO CORRESPONDING FIELDS OF TABLE lt_dokhl
           FROM dokhl
             WHERE id = 'CL'
                AND object = _objname.

* Use only most recent version.
  SORT lt_dokhl BY id object langu typ ASCENDING dokversion DESCENDING.
  DELETE ADJACENT DUPLICATES FROM lt_dokhl COMPARING id object typ langu.

* Make sure there is at least one record here.
  CLEAR ls_dokhl.
  READ TABLE lt_dokhl INTO ls_dokhl INDEX 1.
  IF sy-subrc <> 0.
    RETURN.
  ENDIF.

  docnode = xmldoc->create_element( c_xml_key_class_documentation ).

* Set docNode object attribute
  lv_str = ls_dokhl-object.
  rc = docnode->set_attribute( name = c_xml_key_object value = lv_str ).

  LOOP AT lt_dokhl INTO ls_dokhl.

* Create language node, and set attribute
    languagenode = xmldoc->create_element( c_xml_key_language ).
    lv_str = ls_dokhl-langu.
    rc = languagenode->set_attribute( name = c_xml_key_spras value = lv_str ).

* Read the documentation text
    CALL FUNCTION 'DOCU_READ'
      EXPORTING
        id      = ls_dokhl-id
        langu   = ls_dokhl-langu
        object  = ls_dokhl-object
        typ     = ls_dokhl-typ
        version = ls_dokhl-dokversion
      TABLES
        line    = lt_lines.

* Write records to XML node
    LOOP AT lt_lines INTO ls_lines.
      txtlines_node = xmldoc->create_element( c_xml_key_textline ).
      me->setattributesfromstructure( node = txtlines_node structure = ls_lines ).
      rc = languagenode->append_child( txtlines_node ).
    ENDLOOP.
    rc = docnode->append_child( languagenode ) .
  ENDLOOP.

  rc = rootnode->append_child( docnode ).

endmethod.


method GET_METHOD_DOCUMENTATION.
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*| Copyright 2014 SAPlink project members                              |
*|                                                                     |
*| Licensed under the Apache License, Version 2.0 (the "License");     |
*| you may not use this file except in compliance with the License.    |
*| You may obtain a copy of the License at                             |
*|                                                                     |
*|     http://www.apache.org/licenses/LICENSE-2.0                      |
*|                                                                     |
*| Unless required by applicable law or agreed to in writing, software |
*| distributed under the License is distributed on an "AS IS" BASIS,   |
*| WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or     |
*| implied.                                                            |
*| See the License for the specific language governing permissions and |
*| limitations under the License.                                      |
*\---------------------------------------------------------------------/
  DATA languagenode   TYPE REF TO if_ixml_element.
  DATA docnode        TYPE REF TO if_ixml_element.
  DATA txtlines_node TYPE REF TO if_ixml_element.
  DATA rc            TYPE sysubrc.
  DATA _objtype      TYPE string.

  TYPES: BEGIN OF t_dokhl,
          id          TYPE dokhl-id,
          object      TYPE dokhl-object,
          langu       TYPE dokhl-langu,
          typ         TYPE dokhl-typ,
          dokversion  TYPE dokhl-dokversion,
         END OF t_dokhl.

  DATA lt_dokhl TYPE TABLE OF t_dokhl.
  DATA ls_dokhl LIKE LINE OF lt_dokhl.

  DATA lt_lines TYPE TABLE OF tline.
  DATA ls_lines LIKE LINE OF lt_lines.

  DATA lv_str TYPE string.
  DATA _objname TYPE e071-obj_name.

  _objname = method_key.

* Check against database
  SELECT  id object langu typ dokversion
        INTO CORRESPONDING FIELDS OF TABLE lt_dokhl
           FROM dokhl
             WHERE id = 'CO'
                AND object = _objname.

* Use only most recent version.
  SORT lt_dokhl BY id object langu typ ASCENDING dokversion DESCENDING.
  DELETE ADJACENT DUPLICATES FROM lt_dokhl COMPARING id object typ langu.

* Make sure there is at least one record here.
  CLEAR ls_dokhl.
  READ TABLE lt_dokhl INTO ls_dokhl INDEX 1.
  IF sy-subrc <> 0.
    RETURN.
  ENDIF.

  docnode = xmldoc->create_element( c_xml_key_method_documentation ).

* Set docNode object attribute
  lv_str = ls_dokhl-object.
  rc = docnode->set_attribute( name = c_xml_key_object value = lv_str ).

  LOOP AT lt_dokhl INTO ls_dokhl.

* Create language node, and set attribute
    languagenode = xmldoc->create_element( c_xml_key_language ).
    lv_str = ls_dokhl-langu.
    rc = languagenode->set_attribute( name = c_xml_key_spras value = lv_str ).

* Read the documentation text
    CALL FUNCTION 'DOCU_READ'
      EXPORTING
        id      = ls_dokhl-id
        langu   = ls_dokhl-langu
        object  = ls_dokhl-object
        typ     = ls_dokhl-typ
        version = ls_dokhl-dokversion
      TABLES
        line    = lt_lines.

* Write records to XML node
    LOOP AT lt_lines INTO ls_lines.
      txtlines_node = xmldoc->create_element( c_xml_key_textline ).
      me->setattributesfromstructure( node = txtlines_node structure = ls_lines ).
      rc = languagenode->append_child( txtlines_node ).
    ENDLOOP.
    rc = docnode->append_child( languagenode ) .
  ENDLOOP.

  rc = rootnode->append_child( docnode ).

endmethod.


method GET_SECTIONS.
  DATA publicsection TYPE REF TO if_ixml_element.
  DATA protectedsection TYPE REF TO if_ixml_element.
  DATA privatesection TYPE REF TO if_ixml_element.
  DATA includename TYPE program.
  DATA reportstring TYPE string.

**/--------------------------------------------------------------------\
**|                                                                    |
*  includename = cl_oo_classname_service=>get_pubsec_name( _classname ).
*  READ REPORT includename INTO reportlist.
*  publicsection = xmldoc->create_element( 'publicSection' ).
*
*  reportstring = buildsourcestring( sourcetable = reportlist ).
*  rc = publicsection->if_ixml_node~set_value( reportstring ).
*  CLEAR reportstring.
**|--------------------------------------------------------------------|
*  includename = cl_oo_classname_service=>get_prosec_name( _classname ).
*  READ REPORT includename INTO reportlist.
*  protectedsection = xmldoc->create_element( 'protectedSection' ).
*  reportstring = buildsourcestring( sourcetable = reportlist ).
*  rc = protectedsection->if_ixml_node~set_value( reportstring ).
*  CLEAR reportstring.
**|--------------------------------------------------------------------|
*  includename = cl_oo_classname_service=>get_prisec_name( _classname ).
*  READ REPORT includename INTO reportlist.
*  privatesection = xmldoc->create_element( 'privateSection' ).
*  reportstring = buildsourcestring( sourcetable = reportlist ).
*  rc = privatesection->if_ixml_node~set_value( reportstring ).

*  rc = rootnode->append_child( publicsection ).
*  rc = rootnode->append_child( protectedsection ).
*  rc = rootnode->append_child( privatesection ).

endmethod.


method GET_TEXTPOOL.
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*| Copyright 2014 SAPlink project members                              |
*|                                                                     |
*| Licensed under the Apache License, Version 2.0 (the "License");     |
*| you may not use this file except in compliance with the License.    |
*| You may obtain a copy of the License at                             |
*|                                                                     |
*|     http://www.apache.org/licenses/LICENSE-2.0                      |
*|                                                                     |
*| Unless required by applicable law or agreed to in writing, software |
*| distributed under the License is distributed on an "AS IS" BASIS,   |
*| WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or     |
*| implied.                                                            |
*| See the License for the specific language governing permissions and |
*| limitations under the License.                                      |
*\---------------------------------------------------------------------/
  DATA atext TYPE REF TO if_ixml_element.
  DATA textpooltable TYPE STANDARD TABLE OF textpool.
  DATA textpoolrow TYPE textpool.
  DATA languagelist TYPE instlang.
  DATA alanguage TYPE spras.
  DATA _objname TYPE seoclsname.
  DATA rc TYPE i.
  DATA stemp TYPE string.
  DATA languagenode TYPE REF TO if_ixml_element.
  DATA textnode      TYPE REF TO if_ixml_element.
  DATA classpoolname TYPE program.
  DATA firstloop TYPE flag.

  _objname = objname.

  classpoolname = cl_oo_classname_service=>get_classpool_name( _objname ).

  CALL FUNCTION 'RS_TEXTLOG_GET_PARAMETERS'
    CHANGING
      installed_languages = languagelist.

  firstloop = abap_true.

  LOOP AT languagelist INTO alanguage.
    READ TEXTPOOL classpoolname INTO textpooltable LANGUAGE alanguage.
    IF sy-subrc = 0.
      IF firstloop = abap_true.
        textnode = xmldoc->create_element( c_xml_key_textpool ).
        firstloop = abap_false.
      ENDIF.
      languagenode = xmldoc->create_element( c_xml_key_language ).
      stemp = alanguage.
      rc = languagenode->set_attribute( name = c_xml_key_spras value = stemp ).
      LOOP AT textpooltable INTO textpoolrow.
        atext = xmldoc->create_element( c_xml_key_textelement ).
        setattributesfromstructure( node = atext structure =
        textpoolrow ).
        rc = languagenode->append_child( atext ).
      ENDLOOP.
      rc = textnode->append_child( languagenode ).
    ENDIF.
  ENDLOOP.

  rc = rootnode->append_child( textnode ).

endmethod.


METHOD get_version_info.

  rs_version_info-zsaplink_plugin_major_version = 0.  " We will still import anything written by older version, versioning doesn't change in- or ouptut
  rs_version_info-zsaplink_plugin_minor_version = 1.  " Since we add versioning info this has to increase
  rs_version_info-zsaplink_plugin_build_version = 0.  " minor version increased --> reset to 0

  rs_version_info-zsaplink_plugin_info1         = 'ZSAPLINK_CLASS is part of the main ZSAPLINK project --> This plugin found there instead of ZSAPLINK_PLUGINS projects'.
  rs_version_info-zsaplink_plugin_info2         = 'SAPLINK homepage: https://www.assembla.com/spaces/saplink/wiki'.
  rs_version_info-zsaplink_plugin_info3         = 'Download from https://www.assembla.com/code/saplink/subversion/nodes'.
  rs_version_info-zsaplink_plugin_info4         = 'and navigate to:  trunk -> core -> ZSAPLINK -> CLAS -> ZSAPLINK_CLASS.slnk'.
  rs_version_info-zsaplink_plugin_info5         = ''.

ENDMETHOD.
ENDCLASS.