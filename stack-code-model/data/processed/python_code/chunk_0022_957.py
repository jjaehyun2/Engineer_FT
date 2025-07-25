"! <p class="shorttext synchronized" lang="en">Global types for advanced code search</p>
INTERFACE zif_adcoset_ty_global
  PUBLIC.

  TYPES:
    ty_server_group              TYPE rzlli_apcl,
    ty_package_name              TYPE devclass,
    ty_package_names             TYPE STANDARD TABLE OF devclass WITH EMPTY KEY,
    ty_package_name_range        TYPE RANGE OF devclass,
    ty_tadir_types               TYPE STANDARD TABLE OF trobjtype WITH EMPTY KEY,
    ty_obj_names                 TYPE STANDARD TABLE OF sobj_name WITH EMPTY KEY,
    ty_cls_main_incl_search_mode TYPE string,
    ty_matcher_type              TYPE c LENGTH 1,
    ty_duration_in_s             TYPE p LENGTH 15 DECIMALS 2,
    ty_duration_in_ms            TYPE i,
    ty_duration_in_micros        TYPE p LENGTH 12 DECIMALS 2,
    "! Type for DDLX Source name (not available on 7.40)
    ty_ddlxname                  TYPE progname,

    BEGIN OF ty_method_param_info,
      "! Name of a method parameter
      name        TYPE seocmpname,
      "! Type handle of the parameter
      type_handle TYPE REF TO cl_abap_datadescr,
    END OF ty_method_param_info,

    " <p class="shorttext synchronized" lang="en">Param definitions for parallel processing handler</p>
    BEGIN OF ty_parallel_handler,
      "! Class name of the parallel handler
      classname    TYPE string,
      "! Method name of the parallel handler
      method       TYPE seocpdname,
      "! Information about input parameter
      input_param  TYPE ty_method_param_info,
      "! Information about output parameter
      output_param TYPE ty_method_param_info,
    END OF ty_parallel_handler,

    BEGIN OF ty_tadir_object,
      name         TYPE sobj_name,
      type         TYPE trobjtype,
      owner        TYPE responsibl,
      package_name TYPE devclass,
    END OF ty_tadir_object,

    ty_tadir_objects TYPE STANDARD TABLE OF ty_tadir_object WITH EMPTY KEY,

    BEGIN OF ty_object,
      name TYPE sobj_name,
      type TYPE wbobjtype,
    END OF ty_object,

    ty_objects TYPE STANDARD TABLE OF ty_object WITH EMPTY KEY,

    "! <p class="shorttext synchronized" lang="en">Ranges for search scope</p>
    BEGIN OF ty_search_scope,
      package_range     TYPE ty_package_name_range,
      object_type_range TYPE RANGE OF trobjtype,
      object_name_range TYPE RANGE OF sobj_name,
      owner_range       TYPE RANGE OF uname,
      created_on_range  TYPE RANGE OF tadir-created_on,
      appl_comp_range   TYPE RANGE OF df14l-ps_posid,
      max_objects       TYPE i,
    END OF ty_search_scope,

    "! <p class="shorttext synchronized" lang="en">Uniquely identifies a match</p>
    BEGIN OF ty_match_identifier,
      display_name     TYPE string,
      main_include     TYPE program,
      include          TYPE program,
      "! ADT type for the include - if the include is filled<br>
      "! <br>
      "! Reason:<br>
      "! the uri mapper does not create the most suitable type which will be used
      "! to fetch the right image in ADT, so we write the correct one in this
      "! component
      adt_include_type TYPE string,
    END OF ty_match_identifier.

  TYPES BEGIN OF ty_search_match.
  INCLUDE TYPE ty_match_identifier.
  TYPES:
    start_line   TYPE i,
    start_column TYPE i,
    end_line     TYPE i,
    end_column   TYPE i,
    snippet      TYPE string.
  TYPES END OF ty_search_match.

  TYPES ty_search_matches TYPE STANDARD TABLE OF ty_search_match WITH EMPTY KEY.

  TYPES:
    BEGIN OF ty_search_result_object,
      object       TYPE ty_tadir_object,
      text_matches TYPE ty_search_matches,
      match_count  TYPE i,
    END OF ty_search_result_object,

    ty_search_result_objects TYPE SORTED TABLE OF ty_search_result_object WITH UNIQUE KEY object-name object-type,

    "! Code search result
    BEGIN OF ty_search_result,
      results        TYPE ty_search_result_objects,
      duration_in_ms TYPE ty_duration_in_ms,
    END OF ty_search_result,

    "! <p class="shorttext synchronized" lang="en">Settings for code based class search</p>
    BEGIN OF ty_cls_search_settings,
      search_main_incl       TYPE abap_bool,
      search_methods_incl    TYPE abap_bool,
      search_test_incl       TYPE abap_bool,
      search_macro_incl      TYPE abap_bool,
      search_local_def_incl  TYPE abap_bool,
      search_local_impl_incl TYPE abap_bool,
      main_incl_search_mode  TYPE ty_cls_main_incl_search_mode,
    END OF ty_cls_search_settings,

    "! <p class="shorttext synchronized" lang="en">Basic search settings</p>
    BEGIN OF ty_search_settings,
      line_feed            TYPE string,
      ignore_comment_lines TYPE abap_bool,
      match_all_patterns   TYPE abap_bool,
      multiline_search     TYPE abap_bool,
      max_results          TYPE i,
      all_results          TYPE abap_bool,
    END OF ty_search_settings,

    BEGIN OF ty_custom_search_settings,
      class TYPE ty_cls_search_settings,
    END OF ty_custom_search_settings,

    BEGIN OF ty_parl_processing,
      enabled      TYPE abap_bool,
      server_group TYPE ty_server_group,
    END OF ty_parl_processing,

    BEGIN OF ty_pattern_config,
      ignore_case   TYPE abap_bool,
      matcher_type  TYPE ty_matcher_type,
      pattern_range TYPE RANGE OF string,
    END OF ty_pattern_config.


  "! <p class="shorttext synchronized" lang="en">Internal code search settings</p>
  TYPES BEGIN OF ty_search_settings_int.
  INCLUDE TYPE ty_search_settings AS basic_settings.
  INCLUDE TYPE ty_pattern_config AS pattern_config.
  TYPES:
    custom_settings TYPE ty_custom_search_settings.
  TYPES END OF ty_search_settings_int.

  "! <p class="shorttext synchronized" lang="en">External settings for code search API</p>
  TYPES BEGIN OF ty_search_settings_external.
  INCLUDE TYPE ty_search_settings_int AS internal_settings.
  TYPES:
    parallel_processing TYPE ty_parl_processing,
    search_scope        TYPE ty_search_scope.
  TYPES END OF ty_search_settings_external.


  "! <p class="shorttext synchronized" lang="en">Defines search package for parallel search</p>
  TYPES BEGIN OF ty_search_package.
  INCLUDE TYPE ty_search_settings_int AS settings.
  TYPES objects TYPE ty_tadir_objects.
  TYPES END OF ty_search_package.

  TYPES:
    "! <p class="shorttext synchronized" lang="en">Value range for search option</p>
    BEGIN OF ty_search_option_range,
      sign    TYPE ddsign,
      sign2   TYPE ddsign,
      option  TYPE ddoption,
      option2 TYPE ddoption,
      low     TYPE string,
      high    TYPE string,
    END OF ty_search_option_range,

    "! <p class="shorttext synchronized" lang="en">Table of option value ranges</p>
    ty_search_option_ranges TYPE STANDARD TABLE OF ty_search_option_range WITH EMPTY KEY,

    "! <p class="shorttext synchronized" lang="en">Represents search option with its values</p>
    BEGIN OF ty_search_option,
      option TYPE string,
      ranges TYPE ty_search_option_ranges,
    END OF ty_search_option,

    "! <p class="shorttext synchronized" lang="en">Table of search options</p>
    ty_search_options TYPE STANDARD TABLE OF ty_search_option WITH KEY option.

ENDINTERFACE.