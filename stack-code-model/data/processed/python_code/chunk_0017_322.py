selection-screen begin of block mode
  with frame title text-003.

  parameters:
    x_pkg  radiobutton group fsrc  default 'X' user-command sel_mode,
    x_one  radiobutton group fsrc,
    x_more radiobutton group fsrc.

selection-screen end of block mode.

selection-screen begin of block b_single
  with frame title text-001.

  parameters:
    p_type like tadir-object modif id sgl,
    p_name like tadir-obj_name modif id sgl.

selection-screen end of block b_single.

selection-screen begin of block b_multiple
  with frame title text-002.

  select-options:
      s_type for tadir-object modif id mtp,
      s_name for tadir-obj_name modif id mtp.

selection-screen end of block b_multiple.

selection-screen begin of block b_package
  with frame title text-004.

  parameters:
       p_pkg like tdevc-devclass modif id pkg.

selection-screen end of block b_package.

selection-screen begin of block b_mode
  with frame title text-005.

  parameters:
    p_mode type c length 30 as listbox visible length 30.

selection-screen end of block b_mode.


at selection-screen output.
  loop at SCREEN into data(wa).
    case wa-group1.
      when 'SGL'.
        if x_one = abap_false.
          wa-active = '0'.
          modify SCREEN.
          continue.
        endif.
      when 'MTP'.
        if x_more = abap_false.
          wa-active = '0'.
          modify SCREEN.
          continue.
        endif.
      when 'PKG'.
        if x_pkg = abap_false.
          wa-active = '0'.
          modify SCREEN.
          continue.
        endif.
    endcase.
  endloop.