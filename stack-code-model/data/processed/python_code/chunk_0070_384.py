package devoron.components.tables.icons 
{
	import devoron.data.core.base.DataStructur;
	import org.aswing.table.DefaultTableModel;
	
	/**
	 * Модель таблицы мешей.
	 * @author Devoron
	 */
	public class IconsTableModel extends DefaultTableModel
	{
		public function IconsTableModel(iconObjects:Array=null) 
		{
			setColumnClass(0, "Path");
			setData(iconObjects);
			setColumnNames(["Path to library"])
		}
		
		override public function setValueAt(aValue:*, row:int, column:int):void 
		{
			var libObject:Object= getData()[row] as Object;
				switch(column) {
				case 0:
					libObject["$url_" + libObject] = aValue;
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
			
			var iconObject:Object= getData()[row] as Object;
			
			switch(column) {
				case 0:
					return iconObject["$url_" + iconObject.size + "x" + iconObject.size];
					break;
			}
			
			return "undefined";
		}
		
		override public function isColumnEditable(column:int):Boolean 
		{
			return true;
		}
		
		
		override public function isCellEditable(rowIndex:int, columnIndex:int):Boolean 
		{
			return true;
		}

		
	}

}