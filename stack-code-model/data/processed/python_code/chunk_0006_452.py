*&---------------------------------------------------------------------*
*& Report zmns
*&---------------------------------------------------------------------*
*& method name scanner
*&---------------------------------------------------------------------*
REPORT zmns.

DATA seocompo TYPE seocompo.

SELECT-OPTIONS s_clsnam FOR seocompo-clsname MEMORY ID class.

CLASS lcl_scanner DEFINITION.

  PUBLIC SECTION.
    TYPES ty_class_selection_table TYPE RANGE OF seoclsname.

    TYPES: BEGIN OF ty_reference,
             class  TYPE seoclsname,
             method TYPE seocmpname,
           END OF ty_reference.

    TYPES ty_references TYPE TABLE OF ty_reference WITH KEY class method.

    TYPES: BEGIN OF ty_statistics_line,
             word                        TYPE string,
             count_used_overall          TYPE i,
             count_used_at_the_beginning TYPE i,
             count_used_in_the_middle    TYPE i,
             count_used_at_the_end       TYPE i,
             references                  TYPE ty_references,
           END OF ty_statistics_line.

    TYPES ty_statistics_table TYPE TABLE OF ty_statistics_line WITH KEY word.

    METHODS constructor
      IMPORTING
        class_selection TYPE ty_class_selection_table.

    METHODS run.

  PRIVATE SECTION.
    DATA class_selection TYPE ty_class_selection_table.
    DATA methods_to_analyze TYPE TABLE OF seocompo WITH KEY clsname cmpname.
    DATA statistics TYPE ty_statistics_table.

    METHODS read_method_names.

    METHODS analyze_method_names.

    METHODS count_position
      IMPORTING
        name_part_index      TYPE i
        number_of_name_parts TYPE i
      CHANGING
        line                 TYPE lcl_scanner=>ty_statistics_line.

    METHODS update_reference
      IMPORTING
        method_name TYPE REF TO seocompo
      CHANGING
        statistic   TYPE lcl_scanner=>ty_statistics_line.

    METHODS modify_statistic
      IMPORTING
        method_name          TYPE REF TO seocompo
        number_of_name_parts TYPE i
        name_part_index      TYPE i
      CHANGING
        statistic            TYPE lcl_scanner=>ty_statistics_line.
ENDCLASS.


CLASS lcl_scanner IMPLEMENTATION.
  METHOD constructor.
    me->class_selection = class_selection.
  ENDMETHOD.

  METHOD run.
    read_method_names( ).
    IF methods_to_analyze IS INITIAL.
      RETURN.
    ENDIF.
    analyze_method_names( ).
  ENDMETHOD.

  METHOD analyze_method_names.
    DATA statistic LIKE LINE OF statistics.
    DATA name_part_index TYPE sytabix.
    DATA number_of_name_parts TYPE i.


    LOOP AT methods_to_analyze REFERENCE INTO DATA(method_name).
      SPLIT method_name->cmpname AT '_' INTO TABLE DATA(method_name_parts).
      IF sy-subrc <> 0.
        CONTINUE.
      ENDIF.

      number_of_name_parts = lines( method_name_parts ).

      LOOP AT method_name_parts INTO DATA(name_part).
        name_part_index = sy-tabix.

        TRY.
            statistic = statistics[ word = name_part ].

            modify_statistic(
              EXPORTING
                method_name          = method_name
                number_of_name_parts = number_of_name_parts
                name_part_index      = name_part_index
              CHANGING
                statistic            = statistic ).

          CATCH cx_sy_itab_line_not_found.
            statistic = VALUE ty_statistics_line( word = name_part
                                                  count_used_overall = 1 ).

            count_position(
              EXPORTING
                name_part_index      = name_part_index
                number_of_name_parts = number_of_name_parts
              CHANGING
                line                 = statistic ).

            update_reference(
              EXPORTING
               method_name = method_name
              CHANGING
                statistic = statistic ).

            INSERT statistic INTO TABLE statistics.
        ENDTRY.
      ENDLOOP.
    ENDLOOP.
  ENDMETHOD.

  METHOD read_method_names.
    CONSTANTS lc_component_type_is_method TYPE seocmptype VALUE '1'.
    CONSTANTS lc_method_art_is_method TYPE seomtdtype VALUE '0'.

    SELECT * FROM seocompo
             INTO CORRESPONDING FIELDS OF TABLE @methods_to_analyze
             WHERE clsname IN @class_selection
             AND cmptype = @lc_component_type_is_method
             AND mtdtype = @lc_method_art_is_method.

    " no error handling
  ENDMETHOD.

  METHOD count_position.
    IF name_part_index = 1.
      line-count_used_at_the_beginning = line-count_used_at_the_beginning + 1.
    ELSEIF name_part_index = number_of_name_parts.
      line-count_used_at_the_end = line-count_used_at_the_end + 1.
    ELSE.
      line-count_used_in_the_middle = line-count_used_in_the_middle + 1.
    ENDIF.
  ENDMETHOD.


  METHOD update_reference.
    DATA reference TYPE ty_reference.
    reference-class = method_name->clsname.
    reference-method = method_name->cmpname.

    TRY.
        reference = statistic-references[ class = method_name->clsname
                                          method = method_name->cmpname ].
      CATCH cx_sy_itab_line_not_found..
        INSERT reference INTO TABLE statistic-references.
    ENDTRY.
  ENDMETHOD.

  METHOD modify_statistic.
    statistic-count_used_overall = statistic-count_used_overall + 1.

    count_position(
      EXPORTING
        name_part_index      = name_part_index
        number_of_name_parts = number_of_name_parts
      CHANGING
        line                 = statistic ).

    update_reference(
      EXPORTING
       method_name = method_name
      CHANGING
        statistic = statistic ).

    MODIFY TABLE statistics FROM statistic.
  ENDMETHOD.

ENDCLASS.


START-OF-SELECTION.
  DATA(scanner) = NEW lcl_scanner( s_clsnam[] ).
  scanner->run( ).