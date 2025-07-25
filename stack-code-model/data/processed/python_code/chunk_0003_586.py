class ZSAPLINK_TRANSFORMATION definition
  public
  inheriting from ZSAPLINK
  create public .

public section.

  methods CHECKEXISTS
    redefinition .
  methods CREATEIXMLDOCFROMOBJECT
    redefinition .
  methods CREATEOBJECTFROMIXMLDOC
    redefinition .
protected section.

  constants C_OBJECT_TYPE type STRING value 'XSLT' ##NO_TEXT.
  data XSLT_NAME type CXSLTDESC .
  constants C_TAG_SOURCE type STRING value 'source' ##NO_TEXT.

  methods GET_XSLT
    importing
      !I_XSLT_NAME type CSEQUENCE optional
    returning
      value(RO_XSLT) type ref to CL_O2_API_XSLTDESC
    raising
      ZCX_SAPLINK .
  methods SAVE_XSLT
    importing
      !IO_XSLT type ref to CL_O2_API_XSLTDESC
    raising
      ZCX_SAPLINK .
  methods SET_XSLT_CHANGEABLE
    importing
      !I_CHANGEABLE type ABAP_BOOL default ABAP_TRUE
      !IO_XSLT type ref to CL_O2_API_XSLTDESC
    preferred parameter I_CHANGEABLE
    raising
      ZCX_SAPLINK .
  methods SET_XSLT_NAME .

  methods DELETEOBJECT
    redefinition .
  methods GETOBJECTTYPE
    redefinition .
private section.
ENDCLASS.



CLASS ZSAPLINK_TRANSFORMATION IMPLEMENTATION.


METHOD checkexists .
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*|Copyright 2006-2015 by Nicola Fankhauser(nicola.fankhauser@variant.ch)
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

  CONSTANTS:
    lc_exists TYPE char1 VALUE '1'.

  set_xslt_name( ).

  IF cl_o2_api_xsltdesc=>exists( xslt_name ) EQ lc_exists.
    exists = abap_true.
  ENDIF.

ENDMETHOD.


METHOD createixmldocfromobject .
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*|Copyright 2006-2015 by Nicola Fankhauser(nicola.fankhauser@variant.ch)
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

  DATA:
    lo_xslt TYPE REF TO cl_o2_api_xsltdesc,
    ls_attributes TYPE o2xsltattr,
    lo_rootnode TYPE REF TO if_ixml_element,
    lt_xslt_source TYPE o2pageline_table,
    lo_node TYPE REF TO if_ixml_element,
    l_source TYPE string.

* set internal object name
  set_xslt_name( ).

* load XSLT transformation
  lo_xslt = get_xslt( xslt_name ).

* create parent node with attributes
  lo_rootnode = xmldoc->create_element( c_object_type ).

* 1. get attributes
  ls_attributes = lo_xslt->get_attributes( ).
  setattributesfromstructure( node = lo_rootnode structure = ls_attributes ).

* 2. get XSLT source
  lt_xslt_source = lo_xslt->get_source( ).

  l_source = zsaplink_transformation=>buildsourcestring( pagetable = lt_xslt_source ).
  lo_node = xmldoc->create_element( c_tag_source ).
  lo_node->set_value( l_source ).
  lo_rootnode->append_child( lo_node ).

  xmldoc->append_child( lo_rootnode ).

  ixmldocument = xmldoc.

ENDMETHOD.


METHOD createobjectfromixmldoc .
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*|Copyright 2006-2015 by Nicola Fankhauser(nicola.fankhauser@variant.ch)
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

  DATA:
    lo_rootnode TYPE REF TO if_ixml_element,
    lo_node TYPE REF TO if_ixml_element,
    lo_filter TYPE REF TO if_ixml_node_filter,
    lo_iterator TYPE REF TO if_ixml_node_iterator,
    lo_xslt TYPE REF TO cl_o2_api_xsltdesc,
    ls_attributes TYPE o2xsltattr,
    lt_xslt_source TYPE o2pageline_table,
    ls_xslt_source LIKE LINE OF lt_xslt_source,
    l_source TYPE string,
    lt_source TYPE table_of_strings.

* try to find a XSLT transformation in the XML tree
  xmldoc = ixmldocument.
  lo_rootnode = xmldoc->find_from_name( c_object_type ).

* 1. get attributes
  getstructurefromattributes( EXPORTING node = lo_rootnode CHANGING structure = ls_attributes ).

* set XSLT transformation name
  objname = ls_attributes-xsltdesc.
  set_xslt_name( ).

* check whether object already exists and if overwriting
* is allowed
  IF checkexists( ) IS NOT INITIAL.
    IF overwrite IS INITIAL.
      RAISE EXCEPTION TYPE zcx_saplink
        EXPORTING textid = zcx_saplink=>existing.
    ELSE.
*     delete object for new install
      deleteobject( ).
    ENDIF.
  ENDIF.

* 2. get XSLT source
  CLEAR: lo_filter, lo_iterator, lo_node.
  lo_filter = xmldoc->create_filter_name( c_tag_source ).
  lo_iterator = xmldoc->create_iterator_filtered( lo_filter ).
  lo_node ?= lo_iterator->get_next( ).

  IF lo_node IS NOT INITIAL.
    l_source = lo_node->get_value( ).
    lt_source = zsaplink_transformation=>buildtablefromstring( source = l_source ).

    LOOP AT lt_source INTO l_source.
      CLEAR ls_xslt_source.
      ls_xslt_source-line = l_source.
      APPEND ls_xslt_source TO lt_xslt_source.
    ENDLOOP.
  ENDIF.

* create new XSLT transformation
  cl_o2_api_xsltdesc=>create_new(
    EXPORTING
      p_source                     = lt_xslt_source
      p_attr                       = ls_attributes
    IMPORTING
      p_obj                        = lo_xslt
    EXCEPTIONS
      object_already_existing      = 1
      not_authorized               = 2
      undefined_name               = 3
      OTHERS                       = 4 ).

  IF sy-subrc NE 0.
    CASE sy-subrc.

*     object must not be existing already at this stage
      WHEN 1.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING textid = zcx_saplink=>existing.

      WHEN 2.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING textid = zcx_saplink=>not_authorized.
      WHEN 3.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING textid = zcx_saplink=>not_found.
      WHEN OTHERS.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING textid = zcx_saplink=>system_error.
    ENDCASE.
  ENDIF.

* check for valid object reference
  IF lo_xslt IS NOT BOUND.

    RAISE EXCEPTION TYPE zcx_saplink
      EXPORTING textid = zcx_saplink=>system_error.

  ENDIF.

* save XSLT transformation
  save_xslt( lo_xslt ).

* reset
  set_xslt_changeable( i_changeable = abap_false io_xslt = lo_xslt ).

  name = objname.

ENDMETHOD.


METHOD deleteobject .
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*|Copyright 2006-2015 by Nicola Fankhauser(nicola.fankhauser@variant.ch)
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

  DATA:
    lo_xslt TYPE REF TO cl_o2_api_xsltdesc.

* set internal object name
  set_xslt_name( ).

* load XSLT transformation
  lo_xslt = get_xslt( xslt_name ).

* set changeable
  set_xslt_changeable( i_changeable = abap_true io_xslt = lo_xslt ).

* delete XSLT transformation
  lo_xslt->delete(
    EXCEPTIONS
      object_invalid        = 1
      object_not_changeable = 2
      OTHERS                = 3 ).

  IF sy-subrc <> 0.
    CASE sy-subrc.
      WHEN 1.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING textid = zcx_saplink=>not_found.
      WHEN 2.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING textid = zcx_saplink=>locked.
      WHEN OTHERS.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING textid = zcx_saplink=>system_error.
    ENDCASE.
  ENDIF.

* only this call really deletes the XSLT
  save_xslt( lo_xslt ).

ENDMETHOD.


METHOD getobjecttype .
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*|Copyright 2006-2015 by Nicola Fankhauser(nicola.fankhauser@variant.ch)
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

  objecttype = c_object_type. " XSLT transformation

ENDMETHOD.


METHOD get_xslt .
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*|Copyright 2006-2015 by Nicola Fankhauser(nicola.fankhauser@variant.ch)
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

* load XSLT transformation
  cl_o2_api_xsltdesc=>load(
    EXPORTING
      p_xslt_desc                  = i_xslt_name
    IMPORTING
      p_obj                        = ro_xslt
    EXCEPTIONS
      not_existing                 = 1
      permission_failure           = 2
      OTHERS                       = 5 ).

  IF sy-subrc <> 0.
    CASE sy-subrc.
      WHEN 1.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING textid = zcx_saplink=>not_found.
      WHEN 2.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING textid = zcx_saplink=>not_authorized.
      WHEN OTHERS.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING textid = zcx_saplink=>system_error.
    ENDCASE.
  ENDIF.
ENDMETHOD.


METHOD SAVE_XSLT .
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*|Copyright 2006-2015 by Nicola Fankhauser(nicola.fankhauser@variant.ch)
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

* save XSLT transformation
  io_xslt->save(
    EXCEPTIONS
      permission_failure        = 5
      OTHERS                    = 6 ).

  IF sy-subrc <> 0.
    CASE sy-subrc.
      WHEN 5.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING textid = zcx_saplink=>not_authorized.
      WHEN OTHERS.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING textid = zcx_saplink=>system_error.
    ENDCASE.
  ENDIF.

ENDMETHOD.


METHOD set_xslt_changeable.
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*|Copyright 2006-2015 by Nicola Fankhauser(nicola.fankhauser@variant.ch)
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

* set changeable
  io_xslt->set_changeable(
    EXPORTING
      p_changeable                = i_changeable
    EXCEPTIONS
      object_already_unlocked     = 4
      object_already_changeable   = 5
      object_locked_by_other_user = 3
      permission_failure          = 2
      OTHERS                      = 10 ).

  IF sy-subrc <> 0.
    CASE sy-subrc.
      WHEN 1.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING textid = zcx_saplink=>not_found.
      WHEN 2.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING textid = zcx_saplink=>not_authorized.
      WHEN 3.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING textid = zcx_saplink=>locked.
      WHEN 4 OR 5. " do nothing, continue
      WHEN OTHERS.
        RAISE EXCEPTION TYPE zcx_saplink
          EXPORTING textid = zcx_saplink=>system_error.
    ENDCASE.
  ENDIF.

ENDMETHOD.


METHOD set_xslt_name.
*/---------------------------------------------------------------------\
*| This file is part of SAPlink.                                       |
*|                                                                     |
*|Copyright 2006-2015 by Nicola Fankhauser(nicola.fankhauser@variant.ch)
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

  xslt_name = objname.

ENDMETHOD.
ENDCLASS.