package com.base.db.interfaces
{
	import utils.struct.MYHashMap;
	
	import flash.utils.ByteArray;

	public interface IRow
	{
		function getInt32(fieldId:uint):uint;
		function getBool(fieldId:uint):Boolean;
		function getByte(fieldId:uint):uint;
		function getString(fieldId:uint):ByteArray;
		function getArray(fieldId:uint):Array;
		function getMap(fieldId:uint): MYHashMap;
		function getValue(fieldId:uint): *;
		function hasProp(fieldId:uint):Boolean;
		
		function setInt32(fieldId:uint, val:uint):void;
		function setBool(fieldId:uint, val:Boolean):void;
		function setByte(fieldId:uint, val:uint):void;
		function setString(fieldId:uint, val:ByteArray):void;
		function setArray(fieldId:uint, val:Array):void;
		function setMap(fieldId:uint, val:MYHashMap): void;
		function setValue(fieldId:uint, val:*): void;
		function getField(fieldType: uint, fieldId: uint): *;
			
		function beginEdit(): void;
		function endEdit(): Boolean;
		function toString(): String;
		
		
		function clear():void;
		function dump():void;
	}
}