class ZCL_CLASS_STATIC definition
  public
  final
  create public .

*"* public components of class ZCL_CLASS_STATIC
*"* do not include other source files here!!!
public section.

  types:
    tt_api_values type table of api_value .

  class-methods BAPI_GET_VALUES
    importing
      !I_KEY type SIMPLE
      !I_TABLE type SIMPLE
      !I_TYPE type SIMPLE
      !I_NAME type SIMPLE
    exporting
      !ET_NUMS type TT_BAPI1003_ALLOC_VALUES_NUM
      !ET_CHARS type TT_BAPI1003_ALLOC_VALUES_CHAR
      !ET_CURRS type TT_BAPI1003_ALLOC_VALUES_CURR
    raising
      ZCX_GENERIC .
  type-pools ABAP .
  class-methods BAPI_SET_VALUES
    importing
      !I_KEY type SIMPLE
      !I_TABLE type SIMPLE
      !I_TYPE type SIMPLE
      !I_NAME type SIMPLE
      !IT_NUMS type TT_BAPI1003_ALLOC_VALUES_NUM optional
      !IT_CHARS type TT_BAPI1003_ALLOC_VALUES_CHAR optional
      !IT_CURRS type TT_BAPI1003_ALLOC_VALUES_CURR optional
      !I_COMMIT type ABAP_BOOL default ABAP_FALSE
    raising
      ZCX_GENERIC .
  class-methods CREATE
    importing
      !I_KEY type SIMPLE
      !I_TABLE type SIMPLE
      !I_TYPE type SIMPLE
      !I_NAME type SIMPLE
      !I_COMMIT type ABAP_BOOL default ABAP_FALSE
    raising
      ZCX_GENERIC .
  class-methods DELETE
    importing
      !I_KEY type SIMPLE
      !I_TABLE type SIMPLE
      !I_TYPE type SIMPLE
      !I_NAME type SIMPLE
      !I_COMMIT type ABAP_BOOL default ABAP_FALSE
    raising
      ZCX_GENERIC .
  class-methods FILL_ATTR_VALUE
    importing
      !I_TYPE type SIMPLE
      !I_CHAR type SIMPLE optional
      !I_NUM type SIMPLE optional
    exporting
      !E_VALUE type SIMPLE
    raising
      ZCX_GENERIC .
  class-methods GET_ATTR_DESCR
    importing
      !I_NAME type SIMPLE
    returning
      value(E_DESCR) type STRING .
  class-methods GET_ATTR_ID
    importing
      !I_NAME type SIMPLE
    returning
      value(E_ID) type ATINN .
  class-methods GET_ATTR_NAME
    importing
      !I_ID type SIMPLE
    returning
      value(E_NAME) type STRING .
  class-methods GET_ATTR_TEXT
    importing
      !I_OBJECT type SIMPLE
    returning
      value(E_VALUE) type STRING .
  class-methods GET_ATTR_TYPE
    importing
      !I_ATTR type SIMPLE
    returning
      value(E_TYPE) type CHAR4 .
  class-methods GET_ATTR_VALUE
    importing
      !I_ATTR type SIMPLE
      !I_CHAR type SIMPLE optional
      !I_NUM type SIMPLE optional
    exporting
      value(E_VALUE) type SIMPLE
    raising
      ZCX_GENERIC .
  class-methods GET_BUFFERED_AUSP
    importing
      !I_OBJECT type SIMPLE
    returning
      value(ET_AUSP) type TT_AUSP .
  class-methods GET_BUFFERED_VALUES
    exporting
      !ET_VALUES type TT_API_VALUES .
  class-methods GET_VALUE
    importing
      !I_TYPE type KLASSENART
      !I_CLASS type KLASSE_D
      !I_ATTRIBUTE type ATNAM
      !I_OBJECT type SIMPLE
    returning
      value(E_VALUE) type STRING
    raising
      ZCX_GENERIC .
  class-methods SELECT
    importing
      !I_TYPE type SIMPLE
      !I_NAME type SIMPLE
      !I_MAX type INT4 default 9999999999
      !IT_CRITERIONS type TT_BAPI_SELECTION_CRITERIONS
    returning
      value(ET_OBJECTS) type TT_BAPI_SELECTED_OBJECTS .
  class-methods SET_VALUE
    importing
      !I_KEY type SIMPLE
      !I_TABLE type SIMPLE
      !I_TYPE type SIMPLE
      !I_NAME type SIMPLE
      !I_ATTR type SIMPLE
      !I_VALUE type SIMPLE
      !I_COMMIT type ABAP_BOOL default ABAP_FALSE
    raising
      ZCX_GENERIC .
  class-methods SET_VALUES
    importing
      !I_KEY type SIMPLE
      !I_TABLE type SIMPLE
      !I_TYPE type SIMPLE
      !I_NAME type SIMPLE
      !IT_ATTRIBUTES type ZCL_ABAP_STATIC=>TT_FIELDS
      !I_COMMIT type ABAP_BOOL default ABAP_FALSE
    raising
      ZCX_GENERIC .
  class-methods WAS_CREATED
    importing
      !I_KEY type SIMPLE
      !I_TABLE type SIMPLE
      !I_TYPE type SIMPLE
      !I_NAME type SIMPLE
    returning
      value(E_WAS) type ABAP_BOOL
    raising
      ZCX_GENERIC .
protected section.
*"* protected components of class ZCL_CLASS_STATIC
*"* do not include other source files here!!!
private section.
*"* private components of class ZCL_CLASS_STATIC
*"* do not include other source files here!!!

  class-data DUMMY type DUMMY .

  class-methods MAP_VALUE2AUSP
    importing
      !IS_VALUE type API_VALUE
    returning
      value(ES_AUSP) type AUSP .
  class-methods MAP_VALUES2AUSP
    importing
      !IT_VALUES type TT_API_VALUES
    returning
      value(ET_AUSP) type TT_AUSP .
ENDCLASS.



CLASS ZCL_CLASS_STATIC IMPLEMENTATION.


method bapi_get_values.

    data l_object_key type bapi1003_key-object.
    l_object_key = i_key.

    data l_object_table type bapi1003_key-objecttable.
    l_object_table = i_table.

    data l_object_classnum type bapi1003_key-classnum.
    l_object_classnum = i_name.

    data l_object_classtype type bapi1003_key-classtype.
    l_object_classtype = i_type.

    data lt_return type bapiret2_t.
    call function 'BAPI_OBJCL_GETDETAIL'
      exporting
        objectkey       = l_object_key
        objecttable     = l_object_table
        classnum        = l_object_classnum
        classtype       = l_object_classtype
      tables
        allocvaluesnum  = et_nums
        allocvalueschar = et_chars
        allocvaluescurr = et_currs
        return          = lt_return.

    loop at lt_return transporting no fields where type ca 'EAX'.
      zcx_generic=>raise( it_return = lt_return ).
    endloop.

  endmethod.


method bapi_set_values.

  data l_object_key type bapi1003_key-object.
  l_object_key = i_key.

  data l_object_table type bapi1003_key-objecttable.
  l_object_table = i_table.

  data l_object_classnum type bapi1003_key-classnum.
  l_object_classnum = i_name.

  data l_object_classtype type bapi1003_key-classtype.
  l_object_classtype = i_type.

  data lt_nums like it_nums.
  lt_nums = it_nums.

  data lt_chars like it_chars.
  lt_chars = it_chars.

  data lt_currs like it_currs.
  lt_currs = it_currs.

  data lt_return type bapiret2_t.
  call function 'BAPI_OBJCL_CHANGE'
    exporting
      objectkey          = l_object_key
      objecttable        = l_object_table
      classnum           = l_object_classnum
      classtype          = l_object_classtype
    tables
      allocvaluesnumnew  = lt_nums
      allocvaluescharnew = lt_chars
      allocvaluescurrnew = lt_currs
      return             = lt_return.

  loop at lt_return transporting no fields where type ca 'EAX'.
    zcx_generic=>raise( it_return = lt_return ).
  endloop.

  if i_commit eq abap_true.
    zcl_abap_static=>commit( ).
  endif.

endmethod.


method create.

  data l_object_key type bapi1003_key-object.
  l_object_key = i_key.

  data l_object_table type bapi1003_key-objecttable.
  l_object_table = i_table.

  data l_object_classnum type bapi1003_key-classnum.
  l_object_classnum = i_name.

  data l_object_classtype type bapi1003_key-classtype.
  l_object_classtype = i_type.

  data lt_return type bapiret2_t.
  call function 'BAPI_OBJCL_CREATE'
    exporting
      objectkeynew   = l_object_key
      objecttablenew = l_object_table
      classnumnew    = l_object_classnum
      classtypenew   = l_object_classtype
    tables
      return         = lt_return.

  loop at lt_return transporting no fields where type ca 'EAX'.
    zcx_generic=>raise( it_return = lt_return ).
  endloop.

  if i_commit eq abap_true.
    zcl_abap_static=>commit( ).
  endif.

endmethod.


method delete.

  data l_object_key type bapi1003_key-object.
  l_object_key = i_key.

  data l_object_table type bapi1003_key-objecttable.
  l_object_table = i_table.

  data l_object_classnum type bapi1003_key-classnum.
  l_object_classnum = i_name.

  data l_object_classtype type bapi1003_key-classtype.
  l_object_classtype = i_type.

  data lt_return type bapiret2_t.
  call function 'BAPI_OBJCL_DELETE'
    exporting
      objectkey   = l_object_key
      objecttable = l_object_table
      classnum    = l_object_classnum
      classtype   = l_object_classtype
    tables
      return      = lt_return.

  loop at lt_return transporting no fields where type ca 'EAX'.
    zcx_generic=>raise( it_return = lt_return ).
  endloop.

  if i_commit eq abap_true.
    zcl_abap_static=>commit( ).
  endif.

endmethod.


method fill_attr_value.

  try.

      case i_type.
        when 'CHAR'.
          e_value = i_char.

        when 'NUM'.
          e_value = i_num.

        when 'DATE'.

          check i_num is not initial.

          data l_date_i type i.
          data l_date_c(8).
          e_value = l_date_c = l_date_i = i_num.

      endcase.

      data lx_root type ref to cx_root.
    catch cx_root into lx_root.
      zcx_generic=>raise( ix_root = lx_root ).
  endtry.

endmethod.


method get_attr_descr.

  data l_atinn type atinn.
  l_atinn = get_attr_id( i_name ).

  select single atbez into e_descr
    from cabnt
    where atinn eq l_atinn and
          spras eq sy-langu.

endmethod.


method get_attr_id.

  try.
      zcl_cache_static=>get_data(
        exporting i_name = 'ZCL_CLASS_STATIC=>GET_ATTR_ID'
                  i_id   = i_name
        importing e_data = e_id ).
      return.
    catch cx_root.
  endtry.

  data l_atnam type atnam.
  l_atnam = i_name.

  call function 'CONVERSION_EXIT_ATINN_INPUT'
    exporting
      input  = l_atnam
    importing
      output = e_id.

  zcl_cache_static=>set_data(
    i_name = 'ZCL_CLASS_STATIC=>GET_ATTR_ID'
    i_id   = i_name
    i_data = e_id ).

endmethod.


method get_attr_name.

  try.
      zcl_cache_static=>get_data(
        exporting i_name = 'zcl_CLASS_STATIC=>GET_ATTR_NAME'
                  i_id   = i_id
        importing e_data = e_name ).
      return.
    catch cx_root.
  endtry.

  data l_atinn type atinn.
  l_atinn = i_id.

  call function 'CONVERSION_EXIT_ATINN_OUTPUT'
    exporting
      input  = l_atinn
    importing
      output = e_name.

  zcl_cache_static=>set_data(
    i_name = 'ZCL_CLASS_STATIC=>GET_ATTR_NAME'
    i_id   = i_id
    i_data = e_name ).

endmethod.


method get_attr_text.

  select single atwtb into e_value
    from cawnt
      join cawn
        on cawn~atinn eq cawnt~atinn and
           cawn~atzhl eq cawnt~atzhl and
           cawn~adzhl eq cawnt~adzhl
    where cawn~atwrt  eq i_object and
          cawnt~spras eq sy-langu.

endmethod.


method get_attr_type.

  try.
      zcl_cache_static=>get_data(
        exporting i_name = 'ZCL_CLASS_STATIC=>GET_ATTR_TYPE'
                  i_id   = i_attr
        importing e_data = e_type ).
      return.
    catch cx_root.
  endtry.

  data l_atinn type atinn.
  l_atinn = get_attr_id( i_attr ).

  select single atfor from cabn into e_type
    where atinn eq l_atinn.

  zcl_cache_static=>set_data(
    i_name = 'ZCL_CLASS_STATIC=>GET_ATTR_TYPE'
    i_id   = i_attr
    i_data = e_type ).

endmethod.


method get_attr_value.

  data l_type(4).
  l_type = get_attr_type( i_attr ).

  fill_attr_value(
    exporting
      i_type  = l_type
      i_char  = i_char
      i_num   = i_num
    importing
      e_value = e_value ).

endmethod.


method get_buffered_ausp.

  data lt_ausp type table of rmclausp.
  call function 'CLFM_GET_INTERNAL_TABLES'
    exporting
      i_allausp    = abap_true
    tables
      exp_ausp_tab = lt_ausp.

  if lt_ausp is not initial.

    delete lt_ausp where statu eq 'L'.

    zcl_abap_static=>table2table(
      exporting it_data = lt_ausp
      importing et_data = et_ausp ).

  endif.

endmethod.


method get_buffered_values.

  call function 'CTMS_DDB_HAS_CLASS'
    exceptions
      ddb_has_no_class = 1
      others           = 2.
  if sy-subrc eq 0.
    data lt_char type table of api_char.
    call function 'CTMS_DDB_HAS_VALUES'
      exporting
        assigned_values     = abap_true
        allowed_values      = abap_false
      tables
        imp_characteristics = lt_char
        exp_values          = et_values
      exceptions
        not_found           = 1
        others              = 2.
  endif.

endmethod.


method get_value.

  data ls_tcla type tcla.
  select single * from tcla into ls_tcla where klart = i_type.
  if sy-subrc ne 0.
    message e030 with i_type into dummy.
    zcx_generic=>raise( ).
  endif.

  data lt_attributes type tt_bapi_char.
  data lt_values type tt_bapi_char_values.
  data ls_return1 type bapireturn1.
  call function 'BAPI_CLASS_GET_CHARACTERISTICS'
    exporting
      classnum        = i_class
      classtype       = i_type
      with_values     = abap_true
    importing
      return          = ls_return1
    tables
      characteristics = lt_attributes
      char_values     = lt_values.
  data ls_return type bapiret2.
  move-corresponding ls_return1 to ls_return.
  if ls_return-type ca 'EAX'.
    zcx_generic=>raise( is_return = ls_return ).
  endif.

  data ls_attribute like line of lt_attributes.
  read table lt_attributes into ls_attribute with key name_char = i_attribute.
  if sy-subrc ne 0.
    message e029 with i_attribute into dummy.
    zcx_generic=>raise( ).
  endif.

  data l_object type objnum.
  l_object = i_object.

  data lt_nums type tt_bapi1003_alloc_values_num.
  data lt_chars type tt_bapi1003_alloc_values_char.
  data lt_currs type tt_bapi1003_alloc_values_curr.
  data lt_return type bapiret2_t.
  call function 'BAPI_OBJCL_GETDETAIL'
    exporting
      objectkey       = l_object
      objecttable     = ls_tcla-obtab
      classnum        = i_class
      classtype       = i_type
    tables
      allocvaluesnum  = lt_nums
      allocvalueschar = lt_chars
      allocvaluescurr = lt_currs
      return          = lt_return.
  loop at lt_return transporting no fields where type ca 'EAX'.
    zcx_generic=>raise( it_return = lt_return ).
  endloop.

  case ls_attribute-data_type.
    when 'CHAR'.

      data ls_char like line of lt_chars.
      read table lt_chars into ls_char with key charact = i_attribute.
      if sy-subrc ne 0.
        return.
      endif.

      e_value = ls_char-value_neutral.

    when 'DATE'.

      data ls_num like line of lt_nums.
      read table lt_nums into ls_num with key charact = i_attribute.
      if sy-subrc ne 0.
        return.
      endif.

      data l_date type n length 8.
      l_date = ls_num-value_from.

      e_value = l_date.

    when 'CURR'.

      read table lt_nums into ls_num with key charact = i_attribute.
      if sy-subrc ne 0.
        return.
      endif.

      data l_value type wertv9.
      l_value = ls_num-value_from.

      e_value = l_value.

  endcase.

endmethod.


method map_value2ausp.

  es_ausp-atinn = is_value-atinn.

  data l_type(4).
  l_type = get_attr_type( is_value-atnam ).

  case l_type.
    when 'CHAR'.

      es_ausp-atwrt = is_value-atwrt.

    when 'NUM'.

      call function 'CONVERSION_EXIT_FLOAT_INPUT'
        exporting
          input  = is_value-atwrt
        importing
          output = es_ausp-atflv.

    when 'DATE'.

      data l_date type d.
      call function 'CONVERSION_EXIT_IDATE_INPUT'
        exporting
          input  = is_value-atwrt
        importing
          output = l_date.

      data l_date_c(8).
      data l_date_i type i.
      es_ausp-atflv = l_date_i = l_date_c = l_date.

  endcase.

endmethod.


method map_values2ausp.

  data ls_value like line of it_values.
  loop at it_values into ls_value.

    field-symbols <ls_ausp> like line of et_ausp.
    append initial line to et_ausp assigning <ls_ausp>.

    <ls_ausp> = map_value2ausp( ls_value ).

  endloop.

endmethod.


method select.

  data l_object_classtype type bapi1003_key-classtype.
  l_object_classtype = i_type.

  data l_object_classnum type bapi1003_key-classnum.
  l_object_classnum = i_name.

  data ls_return type bapiret2.
  call function 'BAPI_CLASS_SELECT_OBJECTS'
    exporting
      classtype           = l_object_classtype
      classnum            = l_object_classnum
      maxhits             = i_max
    importing
      return              = ls_return
    tables
      selectioncriterions = it_criterions
      selectedobjects     = et_objects.

endmethod.


method set_value.

  data lt_attr type zcl_abap_static=>tt_fields.
  field-symbols <ls_attr> like line of lt_attr.
  append initial line to lt_attr assigning <ls_attr>.
  <ls_attr>-name  = i_attr.
  <ls_attr>-value = i_value.

  set_values(
    i_key          = i_key
    i_table        = i_table
    i_type         = i_type
    i_name         = i_name
    it_attributes  = lt_attr
    i_commit       = i_commit ).

endmethod.


method set_values.

  data lt_chars type tt_bapi1003_alloc_values_char.
  data lt_nums type tt_bapi1003_alloc_values_num.
  data lt_currs type tt_bapi1003_alloc_values_curr.

  bapi_get_values(
    exporting i_key = i_key
              i_table  = i_table
              i_type   = i_type
              i_name   = i_name
    importing et_chars = lt_chars
              et_nums  = lt_nums
              et_currs = lt_currs ).

  data ls_attr like line of it_attributes.
  loop at it_attributes into ls_attr.

    data l_atinn type atinn.
    l_atinn = get_attr_id( ls_attr-name ).

    data l_type(10).
    select single atfor from cabn into l_type
      where atinn eq l_atinn.
    if sy-subrc ne 0.
      data dummy.
      message e033 with ls_attr-name into dummy.
    endif.

    case l_type.
      when 'CHAR'.

        field-symbols <ls_char> like line of lt_chars.
        read table lt_chars assigning <ls_char> with key charact = ls_attr-name.
        if sy-subrc ne 0.
          append initial line to lt_chars assigning <ls_char>.
          <ls_char>-charact    = ls_attr-name.
        endif.

        <ls_char>-value_char    = ls_attr-value.
        <ls_char>-value_neutral = ls_attr-value.

      when 'NUM'.

        field-symbols <ls_num> like line of lt_nums.
        read table lt_nums assigning <ls_num> with key charact = ls_attr-name.
        if sy-subrc ne 0.
          append initial line to lt_nums assigning <ls_num>.
          <ls_num>-charact    = ls_attr-name.
        endif.

        <ls_num>-value_from = ls_attr-value.

      when 'DATE'.

        read table lt_nums assigning <ls_num> with key charact = ls_attr-name.
        if sy-subrc ne 0.
          append initial line to lt_nums assigning <ls_num>.
          <ls_num>-charact    = ls_attr-name.
        endif.

        data l_date_c(8).
        data l_date_i type i.
        <ls_num>-value_from = l_date_i = l_date_c = ls_attr-value.

    endcase.

  endloop.

  bapi_set_values(
    i_key    = i_key
    i_table  = i_table
    i_type   = i_type
    i_name   = i_name
    it_chars = lt_chars
    it_nums  = lt_nums
    it_currs = lt_currs
    i_commit = i_commit ).

endmethod.


method was_created.

  data l_object_key type bapi1003_key-object.
  l_object_key = i_key.

  data l_object_table type bapi1003_key-objecttable.
  l_object_table = i_table.

  data l_object_classnum type bapi1003_key-classnum.
  l_object_classnum = i_name.

  data l_object_classtype type bapi1003_key-classtype.
  l_object_classtype = i_type.

  data lt_return type bapiret2_t.
  call function 'BAPI_OBJCL_EXISTENCECHECK'
    exporting
      objectkey   = l_object_key
      objecttable = l_object_table
      classnum    = l_object_classnum
      classtype   = l_object_classtype
    tables
      return      = lt_return.

  loop at lt_return transporting no fields where type ca 'EAX'.
    zcx_generic=>raise( it_return = lt_return ).
  endloop.

  loop at lt_return transporting no fields where type eq 'S'.
    e_was = abap_true.
  endloop.

endmethod.
ENDCLASS.