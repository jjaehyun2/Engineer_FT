// ========================================================
// http://www.sephiroth.it/tutorials/flashPHP/cellRenderer
// Alessandro Crugnola
// =======================================================


// import the Serializer Class, this is needed for work with this tutorial.
// you can found this at: https://sourceforge.net/projects/serializerclass
import it.sephiroth.Serializer
import mx.controls.gridclasses.DataGridColumn

function init_grid(){
	var column: DataGridColumn = new DataGridColumn("id")
	column.headerText = "Item ID"
	column.width = 50
	grid.addColumn(column)
	
	var column: DataGridColumn = new DataGridColumn("available")
	column.headerText = "Available"
	column.cellRenderer = "checkCellRender" // [check] cell renderer
	column.width = 60
	grid.addColumn(column)
	var column: DataGridColumn = new DataGridColumn("item")
	column.headerText = "Item Name"
	//column.setStyle("fontWeight","bold")
	column.width = 100
	grid.addColumn(column)
	
	var column: DataGridColumn = new DataGridColumn("preview")
	column.headerText = "Preview"
	column.width = 60
	column.cellRenderer = "imageCellRender" // [image] cell renderer
	grid.addColumn(column)
	
	var column: DataGridColumn = new DataGridColumn("quantity") // quantity
	column.headerText = "Quant."
	column.width = 100
	column.cellRenderer = "numericRenderer" // cell renderer
	grid.addColumn(column)
	
	var column: DataGridColumn = new DataGridColumn("price") // price
	column.headerText = "Price"
	grid.addColumn(column)
	
	var column: DataGridColumn = new DataGridColumn("total") // total
	column.headerText = "Total"
	grid.addColumn(column)
	// ROW heigth
	grid.rowHeight = 25
} // init_grid

// first initialize the grid
init_grid()

// now load the PHP variables
var Class_Serializer:Serializer = new Serializer()
var myLoadVars:LoadVars = new LoadVars();
var data:Object;
myLoadVars.load('http://localhost/tutorials/flashPHP/cellRenderer/files/server.php');
myLoadVars.onLoad = function(success){
	// unserialize the data objecta
	data = Class_Serializer.unserialize(this.output)
	grid.dataProvider = data // populate datagrid
}