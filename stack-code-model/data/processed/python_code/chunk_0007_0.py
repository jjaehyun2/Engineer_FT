INTERFACE zif_ref_data
  PUBLIC .

  TYPES:
    BEGIN OF ts_list_refs,
      level             TYPE i,
      type              TYPE trobjtype,
      object            TYPE progname,
      internal_name     TYPE progname,
      type_ref          TYPE trobjtype,
      object_ref        TYPE string,
      fullname_ref      TYPE string,
      internal_name_ref TYPE progname,
    END OF ts_list_refs .
  TYPES:
    tt_list_refs TYPE STANDARD TABLE OF ts_list_refs .

  CONSTANTS: BEGIN OF cs_types,
               program     TYPE trobjtype VALUE 'PROG',
               class       TYPE trobjtype VALUE 'CLAS',
               interface   TYPE trobjtype VALUE 'INTF',
               function    TYPE trobjtype VALUE 'FUNC',
               webdynpro   TYPE trobjtype VALUE 'WDYN',
               messclas    TYPE trobjtype VALUE 'MSAG',
               table       TYPE trobjtype VALUE 'TABL',
               struc       TYPE trobjtype VALUE 'STRU',
               dataelem    TYPE trobjtype VALUE 'DTEL',
               domain      TYPE trobjtype VALUE 'DOMA',
               tabltype    TYPE trobjtype VALUE 'TTYP',
               seahlp      TYPE trobjtype VALUE 'SHLP',
               view        TYPE trobjtype VALUE 'VIEW',
               single_mess TYPE trobjtype VALUE 'MESS',
             END OF cs_types.

ENDINTERFACE.