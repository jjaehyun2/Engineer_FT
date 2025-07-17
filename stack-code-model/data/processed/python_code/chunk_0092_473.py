package com.grantech.models
{
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;
	import flash.utils.Dictionary;

	public class ControlsHelper
	{
		static public const TYPE_BUTTON:String = "button";
		static public const TYPE_SLIDER:String = "slider";
		static public const TYPE_COMBO_BOX:String = "combo";
		static public const TYPE_COLOR_PICKER:String = "color";
		public function ControlsHelper()
		{
			super();
		}
		private static var _instance:ControlsHelper;

		/**
		 * ControlsHelper singleton access method.
		 */
		public static function get instance() : ControlsHelper
		{
			if( _instance == null )
			{
				_instance = new ControlsHelper();
				_instance.init();
			}
			
			return _instance;
		}

		public var keys:Vector.<String>;
		public var elements:Dictionary;

		private function init():void
		{
			var propFile:File = File.applicationDirectory.resolvePath("config/ui-design-helper.xml");
			var propFileStream:FileStream = new FileStream();
			propFileStream.open(propFile, FileMode.READ);
			var xml:XML = new XML(propFileStream.readUTFBytes(propFileStream.bytesAvailable));
			keys = new Vector.<String>();
			elements = new Dictionary();
			var len:int = xml.item.length();
			for(var i:int = 0; i < len; i++)
			{
				var ch:XML = xml.item[i];
				keys[i] = ch.@name;
				elements[keys[i]] = { control:ch.@control.toString(), category:ch.@category.toString(),	min:Number(ch.@min),	max:Number(ch.@max),	step:Number(ch.@step),	init:Number(ch.@init),	data:String(ch.@data).split(',')}
			}
		}


		public function getInitValue(property:String):Number
		{
			if( elements.hasOwnProperty(property) )
				return elements[property].init;
			return 0;
		}

		public function getGroup(property:String):String
		{
			if( elements.hasOwnProperty(property) )
				return elements[property].category;
			return "basic";
		}

		public function getType(property:String):String
		{
			if( elements.hasOwnProperty(property) )
				return elements[property].control;
			return TYPE_SLIDER;
		}

		public function getData(property:String):Object
		{
			if( elements.hasOwnProperty(property) )
				return elements[property].data;
			return null;
		}
	
		public function getMin(property:String):Number
		{
			var value:Number = -10000;			
			value = elements[property] ? elements[property].min : NaN;
			return value;
		}

		public function getMax(property:String):Number
		{
			var value:Number = -10000;			
			value = elements[property] ? elements[property].max : NaN;
			return value;
		}

		public function getStep(property:String):Number
		{
			var value:Number = -10000;			
			value = elements[property] ? elements[property].step : NaN;
			return value;
		}
	}
}