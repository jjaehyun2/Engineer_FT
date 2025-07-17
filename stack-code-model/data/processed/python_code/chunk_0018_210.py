class lhc_ret definition inheriting from cl_abap_behavior_handler.
  private section.

    methods get_instance_authorizations for instance authorization
      importing keys request requested_authorizations for ret result result.

endclass.

class lhc_ret implementation.

  method get_instance_authorizations.
* Method for instance authorization (Auth objetcs, custom validations, etc). Not relevant for demo.
  endmethod.

endclass.