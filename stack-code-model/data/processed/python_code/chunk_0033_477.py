package devoron.components.tables.variables
{
	import org.aswing.table.DefaultTableModel;
	
	public class DefaultArgumentsTableModel extends DefaultTableModel
	{
		
		public function DefaultArgumentsTableModel(properties:Array = null)
		{
			setData((properties != null) ? properties : new Array());
			setColumnNames(["N", "Value", "Type", "Optional"]);
			setColumnClass(1, "String");
		}
		
		override public function setValueAt(aValue:*, row:int, column:int):void
		{
			var element:Object = getData()[row];
			switch (column)
			{
				case 0: 
					//element.name = aValue;
					break;
				case 1: 
					element.value = aValue;
					break;
				case 2: 
					element.type = aValue;
					break;
				case 3: 
					element.optional = aValue;
					break;
			}
			fireTableCellUpdated(row, column);
		}
		
		override public function getValueAt(row:int, column:int):*
		{
			var element:Object = getData()[row];
			
			switch (column)
			{
				case 0: 
					return String(row);
					break;
				case 1: 
					return element.value;
					break;
				case 2: 
					return element.type;
					break;
				case 3: 
					return element.optional;
					break;
			}
			
			return "undefined";
		}
		
		override public function isColumnEditable(column:int):Boolean
		{
			return column == 1 ? true : false;
		}
		
		override public function isCellEditable(rowIndex:int, columnIndex:int):Boolean
		{
			return columnIndex == 1 ? true : false;
		}
	
	}
}