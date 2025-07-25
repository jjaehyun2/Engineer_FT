REPORT zmime_editor_w3.

* See https://github.com/larshp/mime_editor

********************************************************************************
* The MIT License (MIT)
*
* Copyright (c) 2017 Lars Hvam
*
* Permission is hereby granted, free of charge, to any person obtaining a copy
* of this software and associated documentation files (the "Software"), to deal
* in the Software without restriction, including without limitation the rights
* to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
* copies of the Software, and to permit persons to whom the Software is
* furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included in all
* copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
* OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
* SOFTWARE.
********************************************************************************

TYPES: BEGIN OF ty_smim,
         relid TYPE wwwdata-relid,
         objid TYPE wwwdata-objid,
         ext   TYPE string,
       END OF ty_smim.

DATA: gv_ok_code   LIKE sy-ucomm,
      go_container TYPE REF TO cl_gui_custom_container,
      go_splitter  TYPE REF TO cl_gui_easy_splitter_container,
      go_tree      TYPE REF TO cl_gui_simple_tree,
      go_editor    TYPE REF TO cl_gui_abapedit,
      gs_smim      TYPE ty_smim.

TYPES: BEGIN OF ty_node.
         INCLUDE STRUCTURE treev_node.
         TYPES: text TYPE text50,
       END OF ty_node.

TYPES: ty_nodes TYPE STANDARD TABLE OF ty_node WITH DEFAULT KEY.

PARAMETERS: p_devc TYPE devclass MEMORY ID dvc OBLIGATORY.

INCLUDE zmime_editor_w3_c01.
INCLUDE zmime_editor_w3_f01.
INCLUDE zmime_editor_w3_o01.
INCLUDE zmime_editor_w3_i01.

START-OF-SELECTION.
  PERFORM run.