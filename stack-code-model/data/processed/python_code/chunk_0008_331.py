"! Deprecated - Use IF_ABAP_UNIT_CONSTANT
interface if_Aunit_Constants public.

  constants:
    "! Severity
    begin of severity,
      low               type int1 value 0,
      medium            type int1 value 1,
      high              type int1 value 2,
    end of severity.

  "! Outdated: use severity-low
  constants tolerable type int1 value 0.
  "! Outdated: use severity medium
  constants critical type int1 value 1.
  "! Outdated: use severity-high
  constants fatal type int1 value 2.
  "! Horribly Outdated: use severity low
  constants tolerant type int1 value 0.

  constants:
    "! Control flow
    begin of quit,
      "! Raise failure and continue with test
      no          type int1 value 0,
      "! Raise failure and exit the current test
      test        type int1 value 1,
    end of quit.

  "! Outdated: use quit-no
  constants no type int1 value 0.
  "! Outdated: use quit-test
  constants method type int1 value 1.
  "! Outdated & Discouraged: use quit-test
  constants class type int1 value 2.
  "! Outdated & Discouraged: use quit-test
  constants program type int1 value 3.

endinterface.