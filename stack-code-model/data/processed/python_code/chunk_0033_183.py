package com.lowoui_as.utils
{
	import flash.utils.Dictionary;
	
	public class WeakRefDictionary
	{
		protected var _dictionary:Dictionary;
		
		public function WeakRefDictionary()
		{
			_dictionary = new Dictionary(true); // Create a weak ref dictionary.    
		}
		
		// Value will be stored weak-ref. This means it will actualy be used as the key internally.
		public function setValue(key:Object, value:Object):void
		{
			// Clear up any existing key-value pairs that share the same key.
			for (var k:Object in _dictionary)
			{
				if (key == _dictionary[k])
				{
					_dictionary[k] = null;
				}
			}
			
			_dictionary[value] = key;
		}
		
		// Brute force search for now.
		public function getValue(key:Object):Object
		{
			for (var k:Object in _dictionary)
			{
				if (key == _dictionary[k])
				{
					return k;
				}
			}
			return null;
		}
	}
}