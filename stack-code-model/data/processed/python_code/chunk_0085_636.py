package com.lowoui_as.component 
{
	import com.lowoui_as.core.UIComponent;
	import com.lowoui_as.events.ButtonEvent;
	import com.lowoui_as.events.ButtonGroupEvent;
	import com.lowoui_as.events.DragBarEvent;
	import com.lowoui_as.events.ListEvent;
	import flash.display.DisplayObject;
	import flash.display.DisplayObjectContainer;
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.geom.Rectangle;
	import com.greensock.TweenLite;
	import com.greensock.easing.*;
	
	[Event(name = "itemClick", type = "com.lowoui_as.events.ListEvent")]

	public class ListCon extends UIComponent
	{
		protected var _dispatchInfo:*;
		protected var _btnTypeGroup:ButtonGroup;
		
		private var missionArr:Vector.<DisplayObjectContainer>;
		private var dataArr:Array;
		
		//list style
		private var maxLine        :uint;
		private const xDelta_scroll:uint = 3;
		private var w              :uint;
		private var h              :uint;
		private var spacing        :uint;
		private var itemConClass   :Class;
		private var itemConW       :uint;
		private var itemConH       :uint;
		private var textAutoSize   :String;
		private var rectShape      :Rectangle;
		private var container      :Sprite;
		
		//scroll bar
		private var indicator     :Object;
		
		public function ListCon() 
		{
			super();
			
			//add container
			container = new Sprite();
			this.addChild(container);
			container.x = 0;
			container.y = 0;
			
			rectShape  = new Rectangle(0, 0, 0, 0);	
			
			indicator.addEventListener(DragBarEvent.DRAG, fOnDragIndicator);
			indicator.visible = false;
		}
		override protected function initialize()
		{
			missionArr = new Vector.<DisplayObjectContainer>();
			dataArr = [];
			indicator = this["scrollIndicator"];
		}
		private function enableMouseWheel(bool:Boolean):void 
		{
			if (bool) { this.addEventListener(MouseEvent.MOUSE_WHEEL, onMouseWheel); }
			else      { this.removeEventListener(MouseEvent.MOUSE_WHEEL, onMouseWheel); }
		}
		private function onMouseWheel(e:MouseEvent):void 
		{
			indicator.position += e.delta > 0? -0.1:0.1;
			updateContainerPos();
		}
		private function checkListHeight(listH:Number, conH:uint): Boolean 
		{
			indicator.visible = listH > conH;
			
			return listH > conH;
		}
		private function fOnDragIndicator(e:DragBarEvent):void 
		{
			updateContainerPos();
		}
		private function updateContainerPos()
		{
			var tarY:Number = 0 - (container.height - h) * indicator.position;
			TweenLite.to(container, 0.3, {y: tarY, ease: Sine.easeOut});
		}
		private function resetThisComponent()
		{
			for each (var _obj in missionArr)
			{container.removeChild(_obj);}
				
			missionArr.length = 0;
			indicator.position = 0;
			container.x = 0;
			container.y = 0;
		}
		
		public function getWidth() : uint        { return w; }
		public function getHeight(): uint        { return h; }
		public function get itemGroup(): ButtonGroup   { return _btnTypeGroup; }
		public function get dispatchInfo():Array { return _dispatchInfo; }
		public function setConStyle(itemConObj_:Class, itemConW_:uint, itemConH_:uint, spacing_:uint, maxLine_:uint):void
		{
			//todo: reset first
			itemConClass = null;
			
			w = itemConW_;
			h = itemConH_ + (itemConH_ + spacing_) * (maxLine_ - 1);
			
			spacing = spacing_;
			itemConClass = itemConObj_;
			itemConW = itemConW_;
			itemConH = itemConH_;
			maxLine = maxLine_;
			
			//update scroll bar style
			indicator.x = w + xDelta_scroll;
			indicator.setHeight(h);
		}
		public function updateTaskListCon(_arr:Array):void 
		{
			if (missionArr.length != 0) { resetThisComponent(); }
			
			dataArr = _arr;
			_btnTypeGroup = new ButtonGroup();
			var _groupBtnArr:Array = [];
			
			if (_arr.length == 0) 
			{
				return;
			}
			
			var _itemListH:Number = _arr.length * itemConH + spacing * (_arr.length - 1);
			var _isScrollBar:Boolean = checkListHeight(_itemListH , h);
			
			for (var i:int = 0; i < _arr.length; i++) 
			{
				var _taskItem:* = new itemConClass();
				//trace("check item type:" + _taskItem is Button);
				
				_taskItem.x = itemConW / 2;
				_taskItem.y = itemConH / 2 + i * (itemConH + spacing);
				//set item con data
				_taskItem.setData(_taskItem,_arr[i]);
				
				missionArr.push(_taskItem); 
				container.addChild(_taskItem);
				
				_groupBtnArr[i] = [_taskItem,_arr[i][0]];
			}
			
			var currH:Number = itemConH + (_arr.length - 1) * (itemConH + spacing);
			if (currH > h)
			{
				//draw scroll rect shape
				rectShape.width = itemConW + xDelta_scroll + 20;
				rectShape.height = h;
				this.scrollRect = rectShape;
				enableMouseWheel(true);
			}
			else
			{
				this.scrollRect = null;
				enableMouseWheel(false);
			}
			
			_btnTypeGroup.addButton(_groupBtnArr);
			_btnTypeGroup.addEventListener(ButtonGroupEvent.BUTTON_SELECT, fOnBtnGroupSelect);
			_btnTypeGroup.setValue(_groupBtnArr[0][1]);
			
		}
		private function fOnBtnGroupSelect(e:ButtonGroupEvent)
		{
			//trace("button:" + e.target.value);
			for each (var obj:Array in dataArr)
				if (e.target.value == obj[0])
					_dispatchInfo = obj;
			
			dispatchEvent(new ListEvent(ListEvent.ITEM_CLICK));
		}
		//private function setData(itemObj:Object,arr:Array):void{}
	}
}