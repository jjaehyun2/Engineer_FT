*&---------------------------------------------------------------------*
*& Report Z_DATA_LOAD
*&---------------------------------------------------------------------*
*& The report allows the import of master data (customers, vendors,
*& materials, BOMs, workcenters, routings and activity rates) based on
*& pre-defined tab-delimited text documents.
*&---------------------------------------------------------------------*
REPORT z_data_load.


INCLUDE z_data_load_top.     " Global Data

INCLUDE z_data_load_sel.     " Selection Screen

INCLUDE z_data_load_process. " Processing Part

INCLUDE z_data_load_f01.     " Subroutines