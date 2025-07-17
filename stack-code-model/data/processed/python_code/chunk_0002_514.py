class cl_abap_random definition public.

  public section.

    types:
      p31_0 type p length 16 decimals 0.

"! Create a pseudo-random number generator. If SEED is not supplied, the sequence of
"! pseudo-random numbers is always identical.
    class-methods create
    importing
      !seed type i optional
    returning
      value(prng) type ref to cl_abap_random.
"! Return a pseudo-random integer (32-bit accuracy, signed).
    methods int
    returning
      value(value) type i.
"! Return a non-negative pseudo-random integer.
    methods int31
    returning
      value(value) type i.
"! Return a pseudo-random number f with 0 <= f < 1.
    methods float
    returning
      value(value) type f.
"! Return an arbitrary start value that can be used as SEED in the CREATE method. To ensure
"! reproducibility of subsequent program behavior, applications should log this value.
    class-methods seed
    returning
      value(seed) type i.
"! Return a pseudo-random integer i with LOW <= i <= HIGH.
"! CX_ABAP_RANDOM occurs if HIGH < LOW.
    methods intinrange
    importing
      !low type i default 0
      !high type i default 0
    returning
      value(value) type i
    raising
      cx_abap_random.
"! Return a pseudo-random number with (up to) 31 digits and no decimal places.
    methods packed
    returning
      value(value) type p31_0.
"! Return a pseudo-random number p with MIN <= p <= MAX.
"! CX_ABAP_RANDOM occurs if MAX < MIN.
    methods packedinrange
    importing
      !min type p31_0 default '-9999999999999999999999999999999'
      !max type p31_0 default '9999999999999999999999999999999'
    returning
      value(value) type p31_0
    raising
      cx_abap_random.
"! Return a pseudo-random number df with 0 <= df < 1.
    methods decfloat16
    returning
      value(value) type decfloat16.
"! Return a pseudo-random number df with 0 <= df < 1.
    methods decfloat34
    returning
      value(value) type decfloat34.
"! Return a pseudo-random integer (64-bit accuracy, signed).
    methods int8
    returning
      value(value) type int8.
"! Return a pseudo-random integer i with LOW <= i <= HIGH.
"! CX_ABAP_RANDOM occurs if HIGH < LOW.
    methods int8inrange
    importing
      !low type int8 default cl_abap_math=>min_int8
      !high type int8 default cl_abap_math=>max_int8
    returning
      value(value) type int8
    raising
      cx_abap_random.
endclass.

class cl_abap_random implementation.

endclass.