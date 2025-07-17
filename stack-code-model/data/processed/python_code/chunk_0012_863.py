*&---------------------------------------------------------------------*
*& Report ZTESTMARKDOWN
*&---------------------------------------------------------------------*
*&
*&---------------------------------------------------------------------*
REPORT ZTESTMARKDOWN_KAMAL.


*DATA: ztestclass TYPE REF TO zmarkdown.
*
*DATA: va_text TYPE clike.
*
*
*va_text = ztestclass->text( ).


data(o_markdown) = new zmarkdown( ).

data(v_html) = o_markdown->text( 'Hello _ABAP Markdown_!' ).
write / v_html.