class cl_abap_unit_assert definition public.

  public section.
   "! Default Tolerance for comparison type F
    constants rtol_default type f value '1.E-14' ##no_Text.

    class-methods:
     "! DEPRECATED - use SKIP
     "! Skip test due to missing prerequisites
     "! @parameter msg    | Description
     "! @parameter detail | Further description
     "! @parameter quit   | OBSOLETE: use is strongly discouraged, must not be set set to QUIT-NO
     "!                   |           defaults to outdated if_Aunit_Constants=>class
     abort
       importing   !msg                    type csequence optional
                   !detail                 type csequence optional
                   !quit                   type int1 default 2
       preferred parameter msg,

     "! Assert the validity of the reference
     "!
     "! @parameter act              | Reference variable to be checked
     "! @parameter msg              | Description
     "! @parameter level            | Severity (IF_ABAP_UNIT_CONSTANT=>severity)
     "! @parameter quit             | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter assertion_Failed | Condition was not met (and QUIT = NO)
     assert_bound
       importing   value(act)              type any
                   !msg                    type csequence optional
                   !level                  type int1 default if_abap_unit_constant=>severity-medium
                   !quit                   type int1 default if_abap_unit_constant=>quit-test
       returning   value(assertion_failed) type abap_bool,

     "! Assert that character string fits to simple pattern
     "!
     "! @parameter act              | Actual Object
     "! @parameter exp              | Expected Template
     "! @parameter msg              | Message in Case of Error
     "! @parameter level            | Severity (IF_ABAP_UNIT_CONSTANT=>severity)
     "! @parameter quit             | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter assertion_Failed | Condition was not met (and QUIT = NO)
     assert_char_cp
       importing   !act                    type csequence
                   !exp                    type csequence
                   !msg                    type csequence optional
                   !level                  type int1 default if_abap_unit_constant=>severity-medium
                   !quit                   type int1 default if_abap_unit_constant=>quit-test
       returning   value(assertion_failed) type abap_bool,

     "! Assert that character string does not fit to simple pattern
     "!
     "! @parameter act              | Actual text which shall not adhere to EXP pattern
     "! @parameter exp              | Simple text pattern
     "! @parameter msg              | Description
     "! @parameter level            | Severity (see IF_ABAP_UNIT_CONSTANT=>severity)
     "! @parameter quit             | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter assertion_Failed | Condition was not met (and QUIT = NO)
     assert_char_np
       importing   value(act)              type csequence
                   !exp                    type csequence
                   !msg                    type csequence optional
                   !level                  type int1 default if_abap_unit_constant=>severity-medium
                   !quit                   type int1 default if_abap_unit_constant=>quit-test
       returning   value(assertion_failed) type abap_bool,

     "! Assert that 2 elementary data objects differ
     "!
     "! @parameter act              | Data object with current value
     "! @parameter exp              | Compare object with unexpected value
     "! @parameter tol              | Tolerance range for floating point comparison
     "! @parameter msg              | Message in case of error
     "! @parameter level            | Severity (see IF_ABAP_UNIT_CONSTANT=>severity)
     "! @parameter quit             | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter assertion_Failed | Condition was not met (and QUIT = NO)
     assert_differs
       importing   value(act)              type simple
                   value(exp)              type simple
                   !tol                    type f optional
                   !msg                    type csequence optional
                   !level                  type int1 default if_abap_unit_constant=>severity-medium
                   !quit                   type int1 default if_abap_unit_constant=>quit-test
       returning   value(assertion_failed) type abap_bool,

     "! Assert equality of two data objects
     "!
     "! @parameter act                  | Data object with current value
     "! @parameter exp                  | Data object with expected type
     "! @parameter ignore_Hash_Sequence | Ignore sequence in hash tables
     "! @parameter tol                  | Tolerance Range (for directly passed floating numbers)
     "! @parameter msg                  | Description
     "! @parameter level                | Severity (see IF_ABAP_UNIT_CONSTANT=>severity)
     "! @parameter quit                 | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter assertion_Failed     | Condition was not met (and QUIT = NO)
     assert_equals
       importing   value(act)              type any
                   value(exp)              type any
                   !ignore_hash_sequence   type abap_bool default abap_false
                   !tol                    type f optional
                   !msg                    type csequence optional
                   !level                  type int1 default if_abap_unit_constant=>severity-medium
                   !quit                   type int1 default if_abap_unit_constant=>quit-test
       returning   value(assertion_failed) type abap_bool,


     "! Assert approximate consistency of 2 floating point numbers
     "!
     "! @parameter act              | Data object with current value
     "! @parameter exp              | Data object with expected value
     "! @parameter rtol             | Relative tolerance
     "! @parameter msg              | Description
     "! @parameter level            | Severity (see IF_ABAP_UNIT_CONSTANT=>severity)
     "! @parameter quit             | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter assertion_Failed | Condition was not met (and QUIT = NO)
     assert_equals_float
       importing   value(act)              type numeric
                   value(exp)              type numeric
                   !rtol                   type numeric default cl_abap_unit_assert=>rtol_default
                   !msg                    type csequence optional
                   !level                  type int1 default if_abap_unit_constant=>severity-medium
                   !quit                   type int1 default if_abap_unit_constant=>quit-test
       returning   value(assertion_failed) type abap_bool,

     "! Assert that boolean equals ABAP_FALSE
     "!
     "! @parameter act              | Actual data object
     "! @parameter msg              | Description
     "! @parameter level            | Severity (see IF_ABAP_UNIT_CONSTANT=>severity)
     "! @parameter quit             | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter assertion_Failed | Condition was not met (and QUIT = NO)
     assert_false
       importing   value(act)              type abap_bool
                   !msg                    type csequence optional
                   !level                  type int1 default if_abap_unit_constant=>severity-medium
                   !quit                   type int1 default if_abap_unit_constant=>quit-test
       returning   value(assertion_failed) type abap_bool,

     "! Assert that data object value is initial
     "!
     "! @parameter act              | Actual data object
     "! @parameter msg              | Description
     "! @parameter level            | Severity (see IF_ABAP_UNIT_CONSTANT=>severity)
     "! @parameter quit             | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter assertion_Failed | Condition was not met (and QUIT = NO)
     assert_initial
       importing   value(act)              type any default sy-subrc
                   !msg                    type csequence optional
                   !level                  type int1 default if_abap_unit_constant=>severity-medium
                   !quit                   type int1 default if_abap_unit_constant=>quit-test
       preferred parameter act
       returning
                   value(assertion_failed) type abap_bool,

     "! Assert that reference is initial or not valid
     "!
     "! @parameter act              | Reference variable to be checked
     "! @parameter msg              | Description
     "! @parameter level            | Severity (see IF_ABAP_UNIT_CONSTANT=>severity)
     "! @parameter quit             | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter assertion_Failed | Condition was not met (and QUIT = NO)
     assert_not_bound
       importing   value(act)              type any
                   !msg                    type csequence optional
                   !level                  type int1 default if_abap_unit_constant=>severity-medium
                   !quit                   type int1 default if_abap_unit_constant=>quit-test
       returning   value(assertion_failed) type abap_bool,

     "! Assert that value of data object is not initial
     "!
     "! @parameter act              | Actual Data Object
     "! @parameter msg              | Message in Case of Error
     "! @parameter level            | Severity (see IF_ABAP_UNIT_CONSTANT=>severity)
     "! @parameter quit             | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter assertion_Failed | Condition was not met (and QUIT = NO)
     assert_not_initial
       importing   value(act)              type any
                   !msg                    type csequence optional
                   !level                  type int1 default if_abap_unit_constant=>severity-medium
                   !quit                   type int1 default if_abap_unit_constant=>quit-test
       returning
                   value(assertion_failed) type abap_bool,

     "! Assert that number is in given range
     "!
     "! @parameter lower            | Upper boundary
     "! @parameter upper            | Lower boundary
     "! @parameter number           | Number expected to be within the boundaries
     "! @parameter msg              | Description
     "! @parameter level            | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter quit             | Control flow in case of failed assertion
     "! @parameter assertion_Failed | Condition was not met (and QUIT = NO)
     assert_number_between
       importing   !lower                  type numeric
                   !upper                  type numeric
                   !number                 type numeric
                   !msg                    type csequence optional
                   !level                  type int1 default if_abap_unit_constant=>severity-medium
                   !quit                   type int1 default if_abap_unit_constant=>quit-test
       returning   value(assertion_failed) type abap_bool,


     "! Assert specific value of return code
     "!
     "! @parameter exp              | Expected return code
     "! @parameter act              | Return code. default sy-msg
     "! @parameter msg              | Description
     "! @parameter level            | Severity (see IF_ABAP_UNIT_CONSTANT=>severity)
     "! @parameter quit             | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter symsg            | System message
     "! @parameter assertion_Failed | Condition was not met (and QUIT = NO)
     assert_return_code
       importing   value(exp)              type numeric
                   value(act)              type numeric default sy-subrc
                   !msg                    type csequence optional
                   !level                  type int1 default if_abap_unit_constant=>severity-medium
                   !quit                   type int1 default if_abap_unit_constant=>quit-test
                   !symsg                  type symsg optional
       returning   value(assertion_failed) type abap_bool,


     "! Assert specific value of return code
     "!
     "! @parameter exp              | Expected return code, optional, if not zero
     "! @parameter act              | Return code of ABAP statements
     "! @parameter msg              | Description
     "! @parameter level            | Severity (see IF_ABAP_UNIT_CONSTANT=>severity)
     "! @parameter quit             | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter symsg            | System message
     "! @parameter assertion_Failed | Condition was not met (and QUIT = NO)
     assert_subrc
       importing   value(exp)              type sysubrc default 0
                   value(act)              type sysubrc default sy-subrc
                   !msg                    type csequence optional
                   !level                  type int1 default if_abap_unit_constant=>severity-medium
                   !quit                   type int1 default if_abap_unit_constant=>quit-test
                   !symsg                  type symsg optional
       preferred parameter act
       returning   value(assertion_failed) type abap_bool,

     "! Assert that data is contained as line within internal table
     "!
     "! @parameter line             | Data Object that is typed like line of TABLE
     "! @parameter table            | Internal Table that shall contain LINE
     "! @parameter msg              | Description
     "! @parameter level            | Severity (see IF_ABAP_UNIT_CONSTANT=>severity)
     "! @parameter quit             | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter assertion_Failed | Condition was not met (and QUIT = NO)
     assert_table_contains
       importing   value(line)             type any
                   !table                  type any table
                   !msg                    type csequence optional
                   !level                  type int1 default if_abap_unit_constant=>severity-medium
                   !quit                   type int1 default if_abap_unit_constant=>quit-test
       returning   value(assertion_failed) type abap_bool,

     "! Assert that data is not contained as line in internal table
     "!
     "! @parameter line             | Data Object that is typed like line of TABLE
     "! @parameter table            | Internal Table that must not contain LINE
     "! @parameter msg              | Description
     "! @parameter level            | Severity (see IF_ABAP_UNIT_CONSTANT=>severity)
     "! @parameter quit             | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter assertion_Failed | Condition was not met (and QUIT = NO)
     assert_table_not_contains
       importing   value(line)             type any
                   !table                  type any table
                   !msg                    type csequence optional
                   !level                  type int1 default if_abap_unit_constant=>severity-medium
                   !quit                   type int1 default if_abap_unit_constant=>quit-test
       returning   value(assertion_failed) type abap_bool,

     "! Assert that text matches regular expression
     "!
     "! @parameter pattern          | Regular Expression - see also TA ABAPHELP
     "! @parameter text             | Text that is assumed to met the regular expression
     "! @parameter msg              | Description
     "! @parameter level            | Severity (see IF_ABAP_UNIT_CONSTANT=>severity)
     "! @parameter quit             | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter assertion_Failed | Condition was not met (and QUIT = NO)
     assert_text_matches
       importing   value(pattern)          type csequence
                   value(text)             type csequence
                   !msg                    type csequence optional
                   !level                  type int1 default if_abap_unit_constant=>severity-medium
                   !quit                   type int1 default if_abap_unit_constant=>quit-test
       returning   value(assertion_failed) type abap_bool,

     "! Assert that a constraint is met by data object
     "!
     "! @parameter act              | Data object which should adhere to constraint EXP
     "! @parameter act_As_Text      | Description for ACT that is used in alert message text
     "! @parameter exp              | Constraint to which ACT needs to adhere
     "! @parameter msg              | Description
     "! @parameter level            | Severity (see IF_ABAP_UNIT_CONSTANT=>severity)
     "! @parameter quit             | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter assertion_Failed | Condition was not met (and QUIT = NO)
     assert_that
       importing   value(act)              type data
                   value(act_as_text)      type csequence optional
                   !exp                    type ref to if_constraint
                   !msg                    type csequence optional
                   !level                  type int1 default if_abap_unit_constant=>severity-medium
                   !quit                   type int1 default if_abap_unit_constant=>quit-test
       returning   value(assertion_failed) type abap_bool,


     "! Assert that boolean equals ABAP_TRUE
     "!
     "! @parameter act              | Actual value
     "! @parameter msg              | Description
     "! @parameter level            | Severity (see IF_ABAP_UNIT_CONSTANT=>severity)
     "! @parameter quit             | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter assertion_Failed | Condition was not met (and QUIT = NO)
     assert_true
       importing   value(act)              type abap_bool
                   !msg                    type csequence optional
                   !level                  type int1 default if_abap_unit_constant=>severity-medium
                   !quit                   type int1 default if_abap_unit_constant=>quit-test
       returning   value(assertion_failed) type abap_bool,

     "! Ensure that boolean equals ABAP_FALSE, skip test else
     "! Tests can use this method to ensure that the prerequisites of the test are met. If not,
     "! the test execution gets aborted without raising an assertion
     "!
     "! @parameter act              | Actual value
     "! @parameter msg              | Description
     assume_false
       importing   value(act)              type abap_bool
                   !msg                    type csequence,

     "! Ensure specific value of return code
     "! Tests can use this method to ensure that the prerequisites of the test are met. If not,
     "! the test execution gets aborted without raising an assertion
     "!
     "! @parameter exp              | Expected return code
     "! @parameter act              | Actual return code
     "! @parameter msg              | Description
     "! @parameter symsg            | System message
     assume_return_code
       importing   value(exp)              type numeric
                   value(act)              type numeric  default sy-subrc
                   !msg                    type csequence
                   !symsg                  type symsg optional,


     "! Ensure constraint is met data object
     "! Tests can use this method to ensure that the prerequisites of the test are met. If not,
     "! the test execution gets aborted without raising an assertion
     "!
     "! @parameter act              | Data object which should adhere to constraint EXP
     "! @parameter act_As_Text      | Description for ACT that is used in alert
     "! @parameter exp              | Constraint to which ACT shall adhere
     assume_that
       importing   value(act)              type data
                   value(act_as_text)      type csequence optional
                   !exp                    type ref to if_constraint
                   !msg                    type csequence optional,


     "! Ensure that boolean equals ABAP_TRUE, skip test else
     "! Tests can use this method to ensure that the prerequisites of the test are met. If not,
     "! the test execution gets aborted without raising an assertion
     "!
     "! @parameter act              | Actual value
     "! @parameter msg              | Description
     assume_true
       importing   value(act)              type abap_bool
                   !msg                    type csequence,

     "! Unconditional assertion
     "!
     "! @parameter msg    | Description
     "! @parameter level  | Severity (see IF_ABAP_UNIT_CONSTANT=>severity)
     "! @parameter quit   | Alter control flow/ quit test (see IF_ABAP_UNIT_CONSTANT=>quit)
     "! @parameter detail | Further Description
     fail
       importing   !msg                type csequence optional
                   !level              type int1 default if_abap_unit_constant=>severity-medium
                   !quit               type int1 default if_abap_unit_constant=>quit-test
                   !detail             type csequence optional
       preferred parameter msg,


     "! Skip test due to missing prerequisites
     "! - if called within SETUP or CLASS_SETUP all test methods get skipped
     "! - if called within TEST_METHOD the execution of this test method gets aborted
     "! @parameter msg    | Description
     "! @parameter detail | More detailed description
     skip
       importing   !msg                 type csequence
                   !detail              type csequence optional.

     
endclass.

class cl_abap_unit_assert implementation.

endclass.