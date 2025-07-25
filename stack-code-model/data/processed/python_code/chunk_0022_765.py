class ZCL_AUTEX_COMBINATIONS definition
  public
  final
  create public .

public section.

  types:
    _option TYPE c LENGTH 1 .

  constants VISIBLE_ALWAYS type _OPTION value 'X' ##NO_TEXT.
  constants VISIBLE_NEVER type _OPTION value 'N' ##NO_TEXT.
  constants VISIBLE_OVERVIEW type _OPTION value 'O' ##NO_TEXT.

  methods CHECK_COMBINATION
    importing
      !OPTION_GENERAL type _OPTION
      !OPTION_SPECIFIC type _OPTION
    returning
      value(OPTION_VALID) type _OPTION .
  PROTECTED SECTION.
  PRIVATE SECTION.
ENDCLASS.



CLASS ZCL_AUTEX_COMBINATIONS IMPLEMENTATION.


  METHOD check_combination.


    "there is an object that can have three different levels of visibility:
    " - displayed                   -> VISIBLE_ALWAYS
    " - displayed only in overview  -> VISIBLE_OVERVIEW
    " - hidden                      -> VISIBLE_NEVER

    " there is customizing that defines the "view level" for a general view and for a specific view
    " this function returns the option that needs to be used for displaying the object

    " example:
    " if the general option allows "display in overview" but the specific setting is "hidden"
    " then the specific option overrules the general option because specific allows "less"
    " and therfore returns the specific option

    " if the general option allows "overview" but the specific setting is "always" then the
    " specific option cannot overrule the general option because it would grant more visibility
    " what is not allowed and therfore returns the general option


    CASE option_general.

      WHEN visible_never.
        "general NEVER VISIBLE
        CASE option_specific.
          WHEN visible_never.
            "ok
            option_valid = option_general.

          WHEN visible_overview.
            "not allowed - set option to "not visible"
            option_valid = visible_never.

          WHEN visible_always.
            "specific cannot be "better" than general
            option_valid = option_general.

          WHEN space.
            "not chosen yet - set default
            option_valid = option_general.

        ENDCASE.

      WHEN visible_overview.
        "option: VISIBLE ONLY IN OVERVIEW
        CASE option_specific.
          WHEN visible_never.
            "ok
            option_valid = option_specific.

          WHEN visible_overview.
            "ok
            option_valid = option_specific.

          WHEN visible_always.
            "specific cannot be "better" than general
            option_valid = option_general.

          WHEN space.
            "not chosen yet - set default
            option_valid = option_general.

        ENDCASE.

      WHEN visible_always.
        "option: ALWAYS VISIBLE
        CASE option_specific.
          WHEN visible_never.
            "ok
            option_valid = option_specific.

          WHEN visible_overview.
            "ok
            option_valid = option_specific.

          WHEN visible_always.
            "ok
            option_valid = option_general.

          WHEN space.
            "not chosen yet - set default
            option_valid = option_general.

        ENDCASE.

      WHEN space.
        "not chosen - set customer option also to space
        option_valid  = space.

    ENDCASE.

  ENDMETHOD.
ENDCLASS.