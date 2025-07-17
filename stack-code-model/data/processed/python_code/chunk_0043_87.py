package devoron.components.tables.variables
{
	import devoron.studio.moduls.code.tools.debugger.ParamObject;
	
	import org.aswing.table.DefaultTableModel;
	
	public class ValuesTableModel extends DefaultTableModel
	{
		
		public function ValuesTableModel(properties:Array = null)
		{
			setData((properties != null) ? properties : new Array());
			setColumnNames(["N", "Name"]);
			setColumnClass(1, "String");
		}
		
		override public function setValueAt(aValue:*, row:int, column:int):void
		{
			var element:ParamObject = getData()[row] as ParamObject;
			switch (column)
			{
				case 0: 
					//element.name = aValue;
					break;
				case 1: 
					element.type = aValue;
					break;
				case 2: 
					element.optional = aValue;
					break;
			}
			fireTableCellUpdated(row, column);
		}
		
		override public function getValueAt(row:int, column:int):*
		{
			var element:ParamObject = getData()[row] as ParamObject;
			
			switch (column)
			{
				case 0: 
					return String(row);
					break;
				case 1: 
					return element.type;
					break;
				case 2: 
					return element.optional;
					break;
			}
			
			return "undefined";
		}
		
		override public function isColumnEditable(column:int):Boolean
		{
			return column == 0 ? false : true;
		}
		
		override public function isCellEditable(rowIndex:int, columnIndex:int):Boolean
		{
			return columnIndex == 0 ? false : true;
		}
	
	}
}