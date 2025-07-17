package com.base.db.impl
{
	import com.base.db.interfaces.IRow;
	import com.base.db.interfaces.ITable;
	import utils.struct.MYHashMap;
	

	public class TableImpl implements ITable
	{
		private var mTableId:uint = 0;
		private var mRows:MYHashMap = new MYHashMap();
		
		public function TableImpl(tableId:uint)
		{
			mTableId = tableId;
		}
		
		public function getRow(rowId:uint):IRow
		{
			return mRows.get(rowId);
		}
		
		public function getAllRows():MYHashMap
		{
			return mRows;
		}
		
		public function hasRow(rowId:uint):Boolean
		{
			return mRows.containsKey(rowId);
		}
		
		public function insertRow(rowId:uint):IRow
		{
			if(hasRow(rowId))
				return getRow(rowId);
			
			var row:IRow = new RowImpl();
			mRows.put(rowId, row);
			return row;
		}
		
		public function removeRow(rowId:uint):void
		{
			mRows.remove(rowId);
		}
		
		public function clear():void
		{
			mRows = new MYHashMap();
		}
	}
}