package devoron.data.core.base
{
	
	import flash.events.Event;
	import flash.events.EventDispatcher;
	import flash.events.IEventDispatcher;
	import flash.utils.Proxy;
	import flash.utils.flash_proxy;
	import org.aswing.util.HashMap;
	
	use namespace flash_proxy;
	
	dynamic public class DataStructurObject extends DataObject
	{
		private var _dataStructur:DataStructur = null;
		protected var _dataLiveMode:Boolean = false;
		
		public function DataStructurObject(useUrls:Boolean = true, useEventDispatcher:Boolean = true)
		{
			super(useUrls, useEventDispatcher);
		}
		
		public function clear():void
		{
			objectProperties.clear();
			if (_dataStructur && _active) _dataStructur.serialize();
			if (dispatcher && _active) dispatcher.dispatchEvent(new Event(Event.CHANGE));
		}
		
		override flash_proxy function deleteProperty(name:*):Boolean
		{
			//gtrace("удаление свойста");
			objectProperties.remove(name);
			if (_dataStructur && _active) _dataStructur.serialize();
			if (dispatcher && _active) dispatcher.dispatchEvent(new Event(Event.CHANGE));
			return true;
		}
		
		override flash_proxy function setProperty(name:*, value:*):void
		{
			//gtrace("установка свойста " + name + " " + value);
			//if (_useUrls && name == "url") setExtenalResource(String(value));
			
			if (_useUrls && (name is String)) {
				if(name.indexOf("$url_") == 0) {
				setExtenalResource(name, String(value));
			}
			}
			objectProperties.put(name, value);
			
			//if (_dataStructur && _active) _dataStructur.serialize();
			
			_dataChangeTimestamp = (new Date()).time;

			if (_dataStructur && _dataLiveMode && _active) _dataStructur.serializePart();
			else if (_dataStructur && _active) _dataStructur.serialize();
			
		if (dispatcher && _active) 
			dispatcher.dispatchEvent(new Event(Event.CHANGE));
		}
		
		override protected function onExternalResourceChange(data:*):void
		{
			if (_dataStructur && _active) _dataStructur.serialize();
			super.onExternalResourceChange(data);
		}
		
		public function clone(targetClass:Class = null):DataStructurObject
		{
			var dataStructurObject:DataStructurObject = targetClass ? new targetClass : new DataStructurObject();
			dataStructurObject.dataName = _dataName;
			dataStructurObject.dataType = _dataType;
			dataStructurObject.active = _active;
			dataStructurObject.dataLiveMode = _dataLiveMode;
			dataStructurObject.useUrls = _useUrls;
			
			var value:*;
			for (var prop:String in this)
			{ // nextName/nextNameIndex
				value = this[prop];
				if (value is Array || value is Vector.<*>)
				{
					var arr:Array = [];
					var thisArr:Array = value;
					for each (var item:* in thisArr)
					{
						if (item.hasOwnProperty("clone")) arr.push(item.clone());
						else arr.push(item);
					}
					dataStructurObject[prop] = arr;
				}
				else if (value.hasOwnProperty("clone")) {
					dataStructurObject[prop] = value.clone();
				}
				else
				{
					dataStructurObject[prop] = value;
				}
				
			}
			return dataStructurObject;
		}
		
		public function get dataStructur():DataStructur
		{
			return _dataStructur;
		}
		
		public function set dataStructur(value:DataStructur):void
		{
			_dataStructur = value;
		}
		
		override public function set active(value:Boolean):void
		{
			super.active = value;
			// именно здесь нужно предпринять какие-то шаги, чтобы избежать сериализации целой структуры данных
			// т.е нужно именно в структуре данных собрать данные только с одного контейнера
			// и после 
			if (_dataStructur && _dataLiveMode && _active) _dataStructur.serializePart();
			else if (_dataStructur && _active) _dataStructur.serialize();
		}
		
		public function get dataLiveMode():Boolean 
		{
			return _dataLiveMode;
		}
		
		public function set dataLiveMode(value:Boolean):void 
		{
			_dataLiveMode = value;
		}
	
	}
}