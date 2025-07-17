package com.controls.treeDatagrid.event
{
	import flash.events.Event;
	
	public class TreeAdvancedDataGridEvent extends Event
	{
		public static const EXPAND_TREE_ITEM:String = "expandTreeItem";
		
		private var _data:Object;
		private var _isOpen:Boolean;
		
		public function TreeAdvancedDataGridEvent(type:String, bubbles:Boolean=false,
												  cancelable:Boolean=false, data:Object=null, 
												  isOpen:Boolean=true)
		{
			
			_data = data;
			_isOpen = isOpen;
			
			super(type, bubbles, cancelable);
		}
		
		public function get data():Object
		{
			return _data;
		}

		public function set data(value:Object):void
		{
			_data = value;
		}

		public function get isOpen():Boolean
		{
			return _isOpen;
		}

		public function set isOpen(value:Boolean):void
		{
			_isOpen = value;
		}
	}
}