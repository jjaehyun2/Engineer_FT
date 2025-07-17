package com.base.db.interfaces
{
	import utils.struct.MYHashMap;

	public interface ITable
	{
		function getRow(rowId:uint):IRow;
		function getAllRows():MYHashMap;
		function hasRow(rowId:uint):Boolean;
		function insertRow(rowId:uint):IRow;
		function removeRow(rowId:uint):void;
		function clear():void;
	}
}