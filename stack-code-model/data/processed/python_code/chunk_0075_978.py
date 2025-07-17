package com.lowoui_as.component 
{
	import com.lowoui_as.events.ButtonEvent;
	import com.lowoui_as.evcom.lowoui_as.events.ButtonEventt flash.events.Event;
	import flash.display.Sprite;
	import flash.events.MouseEvent;
	
	[Event(name = "buttonSelect", type = "com.lowoui_as.events.ButtonGroupEvent")]

	public class ButtonGroup extends Sprite
	{
		private var btnArr:Array;
		private var valueArr:Array;
		private var selectIdx:uint;
		
		private var _value:String;
		
		public function ButtonGroup() 
		{
			btnArr = [];
			valueArr = [];
			selectIdx = 0;
		}
		private function selectItem(obj:Object):void
		{
			for each (var _obj:Object in btnArr) 
			{
				if (_obj.selected)
				{
					if (obj != _obj) 
					_obj.selected = false; 
				}
				else
				{
					if (obj == _obj) 	
					{
						_obj.selected = true;
						selectIdx = btnArr.indexOf(_obj);
						dispatchEvent(new ButtonGroupEvent(ButtonGroupEvent.BUTTON_SELECT));
					}
				}
			}
		}
		private function fOnSelect(e:ButtonEvent):void 
		{
			selectItem(e.target);
		}
		private function updateButtons():void 
		{
			for each(var _obj:Object in valueArr)
				if (_obj == _value) 
					selectIdx = valueArr.indexOf(_obj);
			
			btnArr[selectIdx].selected = true;
			
			selectItem(btnArr[selectIdx]);
		}
		
		public function addButton(arr:Object):void
		{
			btnArr = [];
			valueArr = [];
			
			/**if arr is a type of object variable*/
			/*for (var _obj:String in arr) 
			{
				valueArr.push(_obj);
				btnArr.push(arr[_obj]);
				
				arr[_obj].setName(_obj);
				arr[_obj].addEventListener(ButtonEvent.CLICK,fOnSelect);
			}*/
			
			/** if arr is a type of array*/
			for each(var _obj:Object in arr) 
			{
				btnArr.push(_obj[0]);
				valueArr.push(_obj[1]);
				
				_obj[0].setName(_obj[1]);
				_obj[0].addEventListener(ButtonEvent.CLICK,fOnSelect);
			}
		}
		public function setLayout(xBeginPos:Number,yBeginPos:Number,btnWidth:uint,btnHeight:uint,spacing:uint):void
		{
			for each(var _obj:Object in btnArr) 
			{
				_obj.setSize(btnWidth, btnHeight);
				var idx:uint = btnArr.indexOf(_obj);
				_obj.x = xBeginPos + idx * (btnWidth+spacing);
				_obj.y = yBeginPos;
			}
		}
		public function set value(str:String):void
		{
			_value = str;
			updateButtons();
			dispatchEvent(new ButtonGroupEvent(ButtonGroupEvent.BUTTON_SELECT));
		}
		public function get value() : String
		{
			return valueArr[selectIdx];
		}
		
		public function setValue(str:String):void
		{
			_value = str;
			updateButtons();
			dispatchEvent(new ButtonGroupEvent(ButtonGroupEvent.BUTTON_SELECT));
		}
		public function getValue() : String
		{
			return valueArr[selectIdx];
		}
	}
}