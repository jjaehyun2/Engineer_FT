package devoron.dataui 
{
	import devoron.data.core.base.DataStructur;
	import org.aswing.table.DefaultTableModel;
	
	/**
	 * Модель таблицы структур данных.
	 * @author Devoron
	 */
	public class DataStructursTableModel extends DefaultTableModel
	{
		public function DataStructursTableModel(dataStructurs:Array) 
		{
			setColumnClass(0, "String");
			setData(dataStructurs);
			setColumnNames(["Name","Type"])
		}
		
		override public function setValueAt(aValue:*, row:int, column:int):void 
		{
			var dataStructur:DataStructur= getData()[row] as DataStructur;
				switch(column) {
				case 0:
					dataStructur.dataName = aValue;
					break;
				case 1:
					dataStructur.dataType = aValue;
					break;
			}
			fireTableCellUpdated(row, column);
		}
		
		/**
		 * Возвратить значение в таблицу.
		 * @param	row
		 * @param	column
		 * @return
		 */
		override public function getValueAt(row:int, column:int):* 
		{
			
			var dataStructur:DataStructur= getData()[row] as DataStructur;
			
			switch(column) {
				case 0:
					return dataStructur.dataName;
					break;
				case 1:
					return dataStructur.dataType;
					break;
			}
			
			return "undefined";
		}
		
		override public function isColumnEditable(column:int):Boolean 
		{
			if (column == 0) return true;
			return false;
		}
		
		
		override public function isCellEditable(rowIndex:int, columnIndex:int):Boolean 
		{
			if (columnIndex == 0) return true;
			return false;
		}

		
	}

}