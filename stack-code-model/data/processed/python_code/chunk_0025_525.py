package devoron.components.tables.nativecommands
{
	import devoron.components.values.nativecommand.NativeCommand;
	import devoron.data.core.base.DataStructur;
	import org.aswing.table.DefaultTableModel;
	
	/**
	 * NativeCommandsTableModel
	 * @author Devoron
	 */
	public class NativeCommandsTableModel extends DefaultTableModel
	{
		public function NativeCommandsTableModel(iconObjects:Array = null)
		{
			setColumnClass(0, "Application");
			setColumnClass(1, "Array");
			//setColumnClass(2, "Path");
			//setColumnClass(3, "Comment");
			setData(iconObjects);
			setColumnNames(["Application", "Arguments" /*, "Comment"*/])
		}
		
		override public function setValueAt(aValue:*, row:int, column:int):void
		{
			var nativeCommand:NativeCommand = getData()[row] as NativeCommand;
			
			switch (column)
			{
				case 0: 
					nativeCommand.path = aValue;
					break;
				case 1: 
					var args:Vector.<String> = nativeCommand.args;
					if (args)
					{
						args.length = 0;
						var argsArr:Array = aValue as Array;
						var l:uint = argsArr.length;
						for (var i:int = 0; i < l; i++)
						{
							args.push(argsArr[i] as String);
						}
					}
					//nativeCommand.args = aValue;
					break;
				case 2: 
					nativeCommand.workingDirectory = aValue;
					break;
				case 3: 
					nativeCommand.comment = aValue;
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
			
			var nativeCommand:NativeCommand = getData()[row] as NativeCommand;
			
			switch (column)
			{
				case 0: 
					return nativeCommand.path;
					break;
				case 1: 
					return nativeCommand.args;
					break;
				case 2: 
					return nativeCommand.workingDirectory;
					break;
				case 3: 
					return nativeCommand.comment;
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