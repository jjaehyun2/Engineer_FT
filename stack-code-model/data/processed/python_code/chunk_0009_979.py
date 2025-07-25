"! <p class="shorttext synchronized" lang="en">Global constants for code search tools</p>
INTERFACE zif_adcoset_c_global
  PUBLIC.

  CONSTANTS:
    "! Minium Objects in scope that are needed so parallel
    "! processing will be used.
    c_parl_proc_min_objects   TYPE i VALUE 50,
    "! Type for Server Group (see RZ12)
    c_group_type_server_group TYPE rzlli_grpt VALUE 'S',
    "! <p class="shorttext synchronized" lang="en">Regex pattern to detect comment lines in CDS sources</p>
    "! Can be used for the following source types:
    "! <ul>
    "!   <li>DDLS</li>
    "!   <li>DCLS</li>
    "!   <li>DDLX</li>
    "! </ul>
    c_cds_comment_regex       TYPE string VALUE '^\s*(//|/\*|--)',
    "! <p class="shorttext synchronized" lang="en">Matcher types</p>
    BEGIN OF c_matcher_type,
      substring   TYPE zif_adcoset_ty_global=>ty_matcher_type VALUE '1',
      posix_regex TYPE zif_adcoset_ty_global=>ty_matcher_type VALUE '2',
      "! Perl compatible regular expression pattern
      pcre        TYPE zif_adcoset_ty_global=>ty_matcher_type VALUE '3',
    END OF c_matcher_type,

    "! <p class="shorttext synchronized" lang="en">Names of code search parameters</p>
    BEGIN OF c_search_params,
      package                TYPE string VALUE 'packageName',
      owner                  TYPE string VALUE 'owner',
      use_regex              TYPE string VALUE 'useRegex',
      match_all_patterns     TYPE string VALUE 'matchAll',
      ignore_comment_lines   TYPE string VALUE 'ignoreCommentLines',
      ignore_case            TYPE string VALUE 'ignoreCase',
      multi_line             TYPE string VALUE 'multiLine',
      read_package_hierarchy TYPE string VALUE 'readPackages',
      appl_comp              TYPE string VALUE 'applComp',
      object_name            TYPE string VALUE 'objectName',
      object_type            TYPE string VALUE 'objectType',
      search_pattern         TYPE string VALUE 'searchPattern',
      created_date           TYPE string VALUE 'createdDate',
      class_search_scope     TYPE string VALUE 'classScope',
      main_incl_search_mode  TYPE string VALUE 'mainClassInclMode',
      max_objects            TYPE string VALUE 'maxObjects',
      max_results            TYPE string VALUE 'maxResults',
      all_results            TYPE string VALUE 'allResults',
    END OF c_search_params,

    "! <p class="shorttext synchronized" lang="en">Use to signal that all objects in scope should be searched</p>
    c_max_objects_all TYPE string VALUE 'all',

    "! <p class="shorttext synchronized" lang="en">Scope for class code search</p>
    BEGIN OF c_cls_search_scope,
      all                  TYPE string VALUE 'all',
      global               TYPE string VALUE 'global',
      tests                TYPE string VALUE 'tests',
      macros               TYPE string VALUE 'macros',
      local_definitions    TYPE string VALUE 'localDef',
      local_implementation TYPE string VALUE 'localImpl',
    END OF c_cls_search_scope,


    "! <p class="shorttext synchronized" lang="en">Search modes for main class include</p>
    BEGIN OF c_cls_main_search_modes,
      "! The main source exists of the following includes: <br>
      "! <ul>
      "!  <li>Public section</li>
      "!  <li>Protected section</li>
      "!  <li>Private section</li>
      "!  <li>Methods</li>
      "! </ul>
      "! These are all separately read and searched
      search_separate_includes TYPE zif_adcoset_ty_global=>ty_cls_main_incl_search_mode VALUE 'separate',
      "! Only the single include (suffix CS in REPOSRC table) will be searched. <br>
      "! <strong>Advantage</strong>: <br>
      "! Search will be faster as only a single include has to be fetched for the main
      "! source of a global class. <br>
      "! <strong>Disadvantage</strong>: <br>
      "! If classes are also edited in SE24/SE80 the search may not be accurate as the
      "! main source include won't be updated if a single method include gets changed
      search_only_main_source  TYPE zif_adcoset_ty_global=>ty_cls_main_incl_search_mode VALUE 'combined',
    END OF c_cls_main_search_modes,

    "! <p class="shorttext synchronized" lang="en">Technical identifier for source code types</p>
    BEGIN OF c_source_code_type,
      class                 TYPE trobjtype VALUE 'CLAS',
      interface             TYPE trobjtype VALUE 'INTF',
      program               TYPE trobjtype VALUE 'PROG',
      type_group            TYPE trobjtype VALUE 'TYPE',
      data_definition       TYPE trobjtype VALUE 'DDLS',
      metadata_extension    TYPE trobjtype VALUE 'DDLX',
      access_control        TYPE trobjtype VALUE 'DCLS',
      behavior_definition   TYPE trobjtype VALUE 'BDEF',
      simple_transformation TYPE trobjtype VALUE 'XSLT',
      function_group        TYPE trobjtype VALUE 'FUGR',
      function_module       TYPE trobjtype VALUE 'FUNC',
    END OF c_source_code_type.
ENDINTERFACE.