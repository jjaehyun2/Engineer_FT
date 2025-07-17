package com.andywoods.as3behavioursui.data
{
	public class ItemData
	{
		public var fixedProperties:Vector.<PropertyObject>;
		public var editableProperties:Vector.<PropertyObject>;
		public var events:Vector.<EventObject>;
		public var actions:Vector.<ActionObject>;
		
		public function ItemData()
		{
			fixedProperties 	= new Vector.<PropertyObject>();
			editableProperties  = new Vector.<PropertyObject>();
			events 				= new Vector.<EventObject>();
			actions 			= new Vector.<ActionObject>();
		}
	}
}