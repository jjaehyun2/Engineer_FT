package ml.L10NE	{	//	https://github.com/mattlohkamp/L10NE	Matt Lohkamp	work@mattlohkamp.com	mattlohkamp.com/portfolio

	import flash.events.EventDispatcher;
	import flash.events.Event;
	
	public class L10NE	{
				
			//	model stuff + accessors

		private static var dictionaries:Array = new Array();
		public static function getDictionaries():Array	{	return dictionaries;	}
		
		private static var $currentDictID:String;
		public static function get currentDictID():String	{	return $currentDictID;	}
		public static function set currentDictID(_currentDictID:String):void	{
			$currentDictID = _currentDictID;
			dispatchEvent(new Event(Event.CHANGE));
		}
		
		public static function getDictByID(id:String):L10NEDictionary	{	return dictionaries[id];	}
		public static function getCurrentDict():L10NEDictionary	{	return getDictByID($currentDictID);	}
		
		public static function addDictionary(dictionary:L10NEDictionary):void	{
			if(!$currentDictID){	$currentDictID = dictionary.id	}
			dictionaries[dictionary.id] = dictionary;
			dispatchEvent(new Event(Event.ADDED));
		}
		
			//	main function
		
		public static function lionize(target:*, dictID:String = null):*	{	//	takes String or XML, returns String or XML
			return getValue(getDictionaryEntry(getLionID(target),dictID));
		}
		
			// internal dictionary interaction
		
		private static function getLionID(target:*):String	{	//	takes String or XML
			if(target is String){	//	then it's easy
				return String(target);
			}else if(target is XML){	//	get the lionid attribute and use that
				return XML(target).@lionid[0].toString();
			}
			return null;
		}
		
		private static function getDictionaryEntry(lionid:String, dictID:String = null):XML	{
			if(dictID){
				return getDictByID(dictID).getValueByID(lionid)[0];
			}
			return getCurrentDict().getValueByID(lionid)[0];
		}
		
		private static function getValue(dictEntry:XML):*	{	//	returns String or XML
			switch(dictEntry.localName()){
				case 'node':
					return dictEntry;
				break;
				case 'string':
				default:
					return dictEntry.toString();
				break;
			}
			
			return null;
		}
		
			//	event dispatch + listening
		
		/*
			Event list:		
				Event.CHANGE		Fires when currentDictID accessor is SET, aka when $currentDictID is changed
		*/
		
		private static var dispatcher:EventDispatcher = new EventDispatcher();
		
		public static function addEventListener(type:String, listener:Function, useCapture:Boolean = false, priority:int = 0, useWeakReference:Boolean = false):void {
            dispatcher.addEventListener(type, listener, useCapture, priority, useWeakReference);
        }
        public static function removeEventListener(type:String, listener:Function, useCapture:Boolean = false):void {
            dispatcher.removeEventListener(type, listener, useCapture);
        }
        public static function dispatchEvent(event:Event):Boolean {
            return dispatcher.dispatchEvent(event);
        }
        public static function hasEventListener(type:String):Boolean {
            return dispatcher.hasEventListener(type);
        }
	}
}