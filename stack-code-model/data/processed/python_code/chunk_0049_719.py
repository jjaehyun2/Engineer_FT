package devoron.components.filechooser
{
	import devoron.data.core.base.DataStructur;
	import org.aswing.table.DefaultTableModel;
	
	/**
	 * Модель таблицы мешей.
	 * @author Devoron
	 */
	public class FileChooserHelpersTableModel extends DefaultTableModel
	{
		public function FileChooserHelpersTableModel(dataStructurs:Array)
		{
			setColumnClass(0, "IFileChooserHelper");
			setColumnClass(1, "String");
			setData(dataStructurs);
			setColumnNames(["Type", "Extensions"])
		}
		
		override public function setValueAt(aValue:*, row:int, column:int):void
		{
		/*var helper:IFileChooserHelper= getData()[row] as IFileChooserHelper;
		   switch(column) {
		   case 0:
		   helper.dataName = aValue;
		   break;
		   case 1:
		   helper.dataType = aValue;
		   break;
		   }
		 fireTableCellUpdated(row, column);*/
		}
		
		/**
		 * Возвратить значение в таблицу.
		 * @param	row
		 * @param	column
		 * @return
		 */
		override public function getValueAt(row:int, column:int):*
		{
			
			var helper:IFileChooserHelper = getData()[row] as IFileChooserHelper;
			
			switch (column)
			{
				case 0: 
					return helper;
					break;
				case 1: 
					return helper.getSupportedExtensions();
					break;
			}
			
			return "undefined";
		}
		
		override public function isColumnEditable(column:int):Boolean
		{
			/*if (column == 0)
				return true;*/
			return false;
		}
		
		override public function isCellEditable(rowIndex:int, columnIndex:int):Boolean
		{
			/*if (columnIndex == 0)
				return true;*/
			return false;
		}
	
	}

}