package org.ro.view.table {
import mx.collections.ArrayList;

import spark.components.DataGrid;
import spark.components.gridClasses.GridColumn;

public class TableBuilder {

    public static function buildDataGrid(csList:Array):DataGrid {
        var grid:DataGrid = new DataGrid();
        grid.percentWidth = 100;
        grid.percentHeight = 100;
        grid.doubleClickEnabled = true;
        grid.selectionMode = "multipleRows";
        grid.columns = new ArrayList();
        var gc:GridColumn;
        for each(var cs:ColDef in csList) {
            gc = buildColumn(cs);
            grid.columns.addItem(gc);
        }
        return grid;
    }

    private static function buildColumn(cs:ColDef):GridColumn {
        var gc:GridColumn = new GridColumn(cs.getName());
        gc.dataField = cs.getField();
        gc.percentWidth = cs.getWidth();
        gc.showDataTips = cs.hasTip();
        gc.dataTipField = cs.getTip();
        gc.itemRenderer = cs.getRenderer();
        gc.formatter = cs.getFormatter();
        return gc;
    }

}
}