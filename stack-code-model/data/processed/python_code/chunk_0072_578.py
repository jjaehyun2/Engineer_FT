package com.lowoui_as.component
{
	import com.lowoui_as.core.UIComponent;
	import com.lowoui_as.events.ButtonEvent;
	import com.lowoui_as.events.DropMenuEvent;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.text.TextField;
	import flash.utils.getDefinitionByName;
	
	[Event(name = "select", type = "com.lowoui_as.events.DropMenuEvent")]

	public class DropdownMenu extends UIComponent
	{
		private var _value    :String;
		private var dataArr   :Array;
		private var btnObj    :Object;
		private var valueObj  :TextField;
		private var isOpenList:Boolean;
        protected var listObjArr:Array;
		
		public function DropdownMenu() 
		{
			dataArr    = [];
			btnObj     = this["btnSelect"];
			valueObj   = this["tt"];
			isOpenList = false;
			
			listObjArr = [];
			
			thisWidth = this["bg"].width;
			thisHeight = this["bg"].height;
			
			btnObj.addEventListener(MouseEvent.CLICK,fOnClick);
		}
		private function fOnClick(e:MouseEvent):void 
		{
			if (dataArr.length != 0) { showSelectList(); }
		}
		private function updateSelectList()
		{
			var _class:Class = getDefinitionByName("btn") as Class
			
			for (var i:int = 0; i < dataArr.length; i++) 
			{
				var _listObj:* = new _class() as Object;
				_listObj.visible = isOpenList;
				_listObj.setName(dataArr[i]);
				_listObj.setSize(185,24);
				_listObj.x = 0;
				_listObj.y = thisHeight+_listObj.height*i;
				addChild(_listObj);
				listObjArr.push(_listObj);
				
				_listObj.addEventListener(ButtonEvent.CLICK,fOnSelect);
			}
		}
		private function fOnSelect(e:ButtonEvent):void 
		{
			for each (var _obj:Object in listObjArr) 
			{
				if (e.target == _obj)
				{
					valueObj.text = _obj.value;
					_value = _obj.value;
					dispatchEvent(new DropMenuEvent(DropMenuEvent.SELECT));
				}
			}
			showSelectList();
		}
		private function showSelectList()
		{
			isOpenList = !isOpenList;
			for each (var _obj:Object in listObjArr) 
			{ _obj.visible = isOpenList; }
		}
		
		public function set data(arr:Array) : void
		{
			dataArr = arr;
			updateSelectList();
		}
		public function get data() : Array
		{
			return dataArr;
		}
		public function set value(str:String) : void
		{
			_value = str;
			valueObj.text = str;
		}
		public function get value() : String
		{
			return _value;
		}
	}
}