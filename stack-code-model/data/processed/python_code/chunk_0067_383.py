package  as3lib.core
{
	import mx.controls.AdvancedDataGrid;
	import mx.controls.advancedDataGridClasses.AdvancedDataGridColumn;
	import mx.core.mx_internal;
	
	public function rowLabelFunction(item:Object,column:AdvancedDataGridColumn):String
	{
		var dataGrid:AdvancedDataGrid =column.mx_internal::owner.dataProvider;
		return dataGrid.dataProvider.getItemIndex(item)+1;
	}
}