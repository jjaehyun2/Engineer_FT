CLASS /iwbep/cl_mgw_abs_model DEFINITION
  PUBLIC
  ABSTRACT
  CREATE PUBLIC .

  PUBLIC SECTION.
    TYPE-POOLS abap .
    TYPE-POOLS seop .

    INTERFACES /iwbep/if_mgw_med_load .

    CONSTANTS cardinality_entity TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_cardinality VALUE /iwbep/if_mgw_med_odata_types=>gcs_cardinality-cardinality_1_1. "#EC NOTEXT  "EC NO_TEXT
    CONSTANTS cardinality_entity_0 TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_cardinality VALUE /iwbep/if_mgw_med_odata_types=>gcs_cardinality-cardinality_0_1. "#EC NOTEXT  "EC NO_TEXT
    CONSTANTS cardinality_feed TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_cardinality VALUE /iwbep/if_mgw_med_odata_types=>gcs_cardinality-cardinality_0_n. "#EC NOTEXT  "EC NO_TEXT
    CONSTANTS:
      BEGIN OF gcs_fc_target_path,
        media_content_src  TYPE string VALUE 'content/@src', "#EC NOTEXT
        media_content_type TYPE string VALUE 'content/@type', "#EC NOTEXT
      END OF gcs_fc_target_path .
    CONSTANTS:
      BEGIN OF gcs_sap_semantic,
        bday             TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'bday',             "  Birth date
        categories       TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'categories',       " Calendar: comma-separated list of categories for cal. comp.
        city             TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'city',             " Address: city
        class	           TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'class',            " Calendar: access classification for a calendar component
        completed        TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'completed',        "  Calendar: date and time a to-do was actually completed
        contact          TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'contact',          " Calendar: contact info or reference to contact info
        country          TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'country',          " Address: country
        currency_code    TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'currency-code',    " Currency Code
        description      TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'description',      " Calendar: descr. of a calendar component (summary detailing)
        dtend	           TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'dtend',            " Calendar: the date and time that a calendar component ends
        dtstart          TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'dtstart',          "  Calendar: date and time that a calendar component starts
        due	             TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'due',              " Calendar: date and time a to-do is expected to be completed
        duration         TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'duration',         " Calendar: duration as an alternative to dtend
        email            TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'email',            "  Email Address
        familyname       TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'familyname',       " Last name or family name of a person
        fbtype           TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'fbtype',           " Calendar: free/busy time type
        geo_lat	         TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'geo-lat',          " Geolocation: latitude
        geo_lon          TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'geo-lon',          "  Geolocation: longitude
        givenname	       TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'givenname',        " First name or given name of a person
        honorific        TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'honorific',        "  P Title of a person (Ph.D., Dr.,…)
        location         TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'location',         " Calendar: intended venue for activity defined by cal. comp.
        mail_from        TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'from',             " Mail: author of message, see [RFC5322, section 3.6.2]
        mail_sender	     TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'sender',           " Mail: mailbox of agent responsible for actual transmission
        mail_to	         TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'to',               " Mail: comma-separated list of primary recipients, see [RFC5322, section 3.6.3]
        mail_cc	         TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'cc',               " Mail: carbon copy, comma-separated
        mail_bcc         TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'bcc',              " Mail: blind carbon copy, comma-separated
        mail_subject     TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'subject',          " Mail: topic of the message
        mail_body	       TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'body',             " Mail: message body
        mail_keywords	   TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'keywords',         " Mail: comma-separated list of important words and phrases that might be useful for the recipient
        mail_received	   TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'received',         " Mail: DateTime the message was received
        middlename       TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'middlename',       " Middle name of a person
        name             TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'name',             " Formatted text of the full name
        nickname         TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'nickname',         " Descriptive name given instead of/in addition to "name"
        note             TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'note',             " Supplemental information or comment associated with vCard
        org              TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'org',              "  Organization name
        org_role         TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'org-role',         " Organizational role
        org_unit         TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'org-unit',         " Organizational unit
        percent_complete TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'percent-complete', "  Calendar: percent completion of to-do, from 0 to 100
        photo            TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'photo',            " URI of a photo of a person
        pobox            TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'pobox',            "  Address: postal office box
        priority         TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'priority',         " Calendar: relative prio (1 highest, 9 lowest, 0 undefined)
        region           TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'region',           " Address: state or province
        status           TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'status',           " Calendar: overall status or confirmation for the cal. comp.
        street           TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'street',           " Address: street
        suffix           TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'suffix',           " Suffix
        summary	         TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'summary',          " Calendar: summary of a calendar component
        szip             TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'zip',              " Address: postal/ZIP code
        tel              TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'tel',              "  Telephone Number
        tel_cell         TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'tel;type=cell',
        tel_cell_pref    TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'tel;type=cell.pref',
        tel_work         TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'tel;type=work',
        title            TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'title',            "  P Job title
        transp           TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'transp',           " Calendar: event is transparent to busy time searches
        unit_of_measure  TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'unit-of-measure',  " Unit of Measure
        url              TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'url',              "  Web URI
        vcard            TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'vcard',            " Node: Contains contact information following the vCard standard
        vevent           TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'vevent',           " Node: Contains event information following the iCalendar standard
        vtodo            TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'vtodo',            " Node: Contains task information following the iCalendar standard
        wholeday         TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_semantic VALUE 'wholeday',         " “true” or “false”: Calendar event scheduled for whole day
      END OF gcs_sap_semantic .
    CONSTANTS:
      BEGIN OF gcs_sap_text_object_types,
        text_symbol_class TYPE /iwbep/if_mgw_med_odata_types=>ty_e_med_text_obj_type VALUE 'BP',
      END   OF gcs_sap_text_object_types .
    CONSTANTS gc_default_schema_version TYPE /iwbep/med_srv_schema_version VALUE '1'. "#EC NOTEXT  "EC NO_TEXT
    DATA model TYPE REF TO /iwbep/if_mgw_odata_model .
    DATA vocab_anno_model TYPE REF TO /iwbep/if_mgw_vocan_model .

    METHODS define
          ABSTRACT
      RAISING
        /iwbep/cx_mgw_med_exception .
    METHODS get_last_modified
      RETURNING
        VALUE(rv_last_modified) TYPE timestamp .
    METHODS get_vocan_provider_texts
      IMPORTING
        !iv_language        TYPE sy-langu
        !it_vocan_text_keys TYPE /iwbep/if_mgw_med_odata_types=>ty_t_med_vocan_texts
      CHANGING
        !ct_vocan_texts_obj TYPE /iwbep/if_mgw_med_odata_types=>ty_t_med_obj_vocan_texts
      RAISING
        /iwbep/cx_mgw_med_exception .
    METHODS get_vocan_texts
      IMPORTING
        !iv_language        TYPE sy-langu
        !it_vocan_text_keys TYPE /iwbep/if_mgw_med_odata_types=>ty_t_med_vocan_texts
      CHANGING
        !ct_vocan_texts_obj TYPE /iwbep/if_mgw_med_odata_types=>ty_t_med_obj_vocan_texts
      RAISING
        /iwbep/cx_mgw_med_exception .
  PROTECTED SECTION.

    METHODS get_model_version
      RETURNING
        VALUE(rv_version) TYPE /iwbep/med_mdl_version .
    METHODS get_model_name
      RETURNING
        VALUE(rv_mdl_name) TYPE /iwbep/med_mdl_technical_name .
    METHODS get_mp_facade
      RETURNING
        VALUE(ro_mp_facade) TYPE REF TO /iwbep/if_mgw_mp_facade
      RAISING
        /iwbep/cx_mgw_tech_exception .
ENDCLASS.
CLASS /iwbep/cl_mgw_abs_model IMPLEMENTATION.
  METHOD get_last_modified.
  ENDMETHOD.
  METHOD get_model_name.
  ENDMETHOD.
  METHOD get_model_version.
  ENDMETHOD.
  METHOD get_mp_facade.
  ENDMETHOD.
  METHOD get_vocan_provider_texts.
  ENDMETHOD.
  METHOD get_vocan_texts.
  ENDMETHOD.
ENDCLASS.