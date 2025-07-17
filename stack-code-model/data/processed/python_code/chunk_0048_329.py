package devoron.data.core.base
{
	//import devoron.file.FilesObserver;
	import flash.events.Event;
	import flash.events.EventDispatcher;
	import flash.events.IEventDispatcher;
	import flash.utils.Proxy;
	import flash.utils.flash_proxy;
	import org.as3commons.lang.IComparable;
	import org.aswing.util.HashMap;
	
	/**
	 * DataObject
	 *
	 * Расширяет Proxy и собирает в себе данные различных типов.
	 * Способен парсить строки содержащие спец.команды:
	 * $url_ связывает свойство с изменением реального файла.
	 *
	 * @author Devoron
	 */
	[Event(name="change",type="flash.events.Event")]
	
	dynamic public class DataObject extends Proxy implements IEventDispatcher
	{
		protected var _dataType:String = null;
		protected var _dataName:String = null;
		protected var _dataChangeTimestamp:Number;
		
		protected var objectProperties:HashMap = new HashMap(); // хранилище динамических свойств
		
		protected var dispatcher:EventDispatcher;
		protected var _useUrls:Boolean = true;
		
		protected var _active:Boolean = true;
		
		public function DataObject(useUrls:Boolean = true, useEventDispatcher:Boolean = false)
		{
			_useUrls = useUrls;
			
			if (useEventDispatcher)
			{
				dispatcher = new EventDispatcher(this);
			}
		}
		
		public function isEquals(dataObject:DataObject):Boolean
		{
			var comparator:IDataObjectsComparator;
			return comparator.compare(this, dataObject, DataObjectCompareModes.NORMAL);
			//compareTo
		}
		
		override flash_proxy function deleteProperty(name:*):Boolean
		{
			objectProperties.remove(name);
			return true;
		}
		
		override flash_proxy function getProperty(name:*):*
		{
			return objectProperties.get(name);
		}
		
		override flash_proxy function setProperty(name:*, value:*):void
		{
			/*if (_useUrls && (name as String).indexOf("$url_") == 0)
				setExtenalResource(name, String(value));*/
			
			//if (_useUrls && name == "url") setExtenalResource(String(value));
			objectProperties.put(name, value);
			if (dispatcher && _active)
			{
				_dataChangeTimestamp = (new Date()).time;
				dispatcher.dispatchEvent(new Event(Event.CHANGE));
			}
		}
		
		/**
		 * Установка внешнего ресурса через свойство url.
		 * Если ссылка новая, то прежняя будет удалена из наблюдателя
		 * файлов.
		 * @param	path
		 */
		protected function setExtenalResource(name:String, path:String):void
		{
			//if (objectProperties.get("url") == path) return;
			if (objectProperties.get(name) == path)
				return;
			path = path.replace(/\\\\/g, '\\');
			//var oldUrl:String = objectProperties.get("url");
			var oldUrl:String = objectProperties.get(name);
			if (oldUrl)
			{
				oldUrl = oldUrl.replace(/\\\\/g, '\\');
					//FilesObserver.removeFileToObserve(oldUrl);
			}
			//if (path.length > 0)
			//FilesObserver.addFileToObserve(path, onExternalResourceChange);
		}
		
		/**
		 * Удаление всех внешних ресурсов,
		 * установленных через свойство url.
		 */
		public function removeAllExternalResources():void
		{
			// удаление внешних ресурсов
			/*var oldUrl:String = objectProperties.get("url");
			   if (oldUrl) oldUrl = oldUrl.replace(/\\\\/g, '\\');
			 FilesObserver.removeFileToObserve(oldUrl);*/
			
			var names:Array = objectProperties.keys();
			for each (var name:String in names)
			{
				if (name.indexOf("$url_") == 0)
				{
					var path:String = (objectProperties.get(name) as String).replace(/\\\\/g, '\\');
						//FilesObserver.removeFileToObserve(path);
				}
			}
		
		}
		
		protected function onExternalResourceChange(data:*):void
		{
			//gtrace("Изменились внешние данные ");
			if (dispatcher && _active)
				dispatcher.dispatchEvent(new Event(Event.CHANGE));
		}
		
		public function toString():String
		{
			return _dataName;
		}
		
		override flash_proxy function nextNameIndex(index:int):int
		{
			if (index < objectProperties.size())
				return index + 1;
			return 0;
		}
		
		override flash_proxy function nextName(index:int):String
		{
			return objectProperties.keys()[index - 1];
		}
		
		override flash_proxy function nextValue(index:int):*
		{
			return objectProperties.get(objectProperties.keys()[index - 1]);
		}
		
		override flash_proxy function hasProperty(name:*):Boolean
		{
			return this.hasProperty(name);
		}
		
		override flash_proxy function callProperty(name:*, ... rest):*
		{
			//gtrace("call " + name + " " + rest);
			//obj
			//return this.callProperty.apply(null, [name, 
		}
		
		/* INTERFACE flash.events.IEventDispatcher */
		
		public function addEventListener(type:String, listener:Function, useCapture:Boolean = false, priority:int = 0, useWeakReference:Boolean = false):void
		{
			dispatcher.addEventListener(type, listener, useCapture, priority, useWeakReference);
		}
		
		public function removeEventListener(type:String, listener:Function, useCapture:Boolean = false):void
		{
			dispatcher.removeEventListener(type, listener, useCapture);
		}
		
		public function dispatchEvent(event:Event):Boolean
		{
			return dispatcher.dispatchEvent(event);
		}
		
		public function hasEventListener(type:String):Boolean
		{
			return dispatcher.hasEventListener(type);
		}
		
		public function willTrigger(type:String):Boolean
		{
			return dispatcher.willTrigger(type);
		}
		
		public function get dataType():String
		{
			return _dataType;
		}
		
		public function set dataType(value:String):void
		{
			_dataType = value;
		}
		
		public function get useUrls():Boolean
		{
			return _useUrls;
		}
		
		public function set useUrls(value:Boolean):void
		{
			_useUrls = value;
		}
		
		public function get dataName():String
		{
			return _dataName;
		}
		
		public function set dataName(value:String):void
		{
			_dataName = value;
		}
		
		public function get active():Boolean
		{
			return _active;
		}
		
		public function set active(value:Boolean):void
		{
			_active = value;
		}
		
		public function get timestamp():Number
		{
			return _dataChangeTimestamp;
		}
	
	}

}