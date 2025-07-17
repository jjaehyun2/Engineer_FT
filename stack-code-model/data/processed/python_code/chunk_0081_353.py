package com.adobe.dashboard.model
{

	public class SeriesModel implements ISeriesModel
	{
		private var _axis:String;

		[Bindable]
		public function get axis():String
		{
			return _axis;
		}

		public function set axis(value:String):void
		{
			_axis = value;
		}


		private var _field:String;

		[Bindable]
		public function get field():String
		{
			return _field;
		}

		public function set field(value:String):void
		{
			_field = value;
		}


		private var _name:String;

		[Bindable]
		public function get name():String
		{
			return _name;
		}

		public function set name(value:String):void
		{
			_name = value;
		}



		public function SeriesModel(axis:String = null, field:String = null, name:String = null)
		{
			_axis = axis;
			_field = field;
			_name = name;
		}


		public static function fromXML(x:XML):SeriesModel
		{
			return new SeriesModel(x.axis, x.field, x.name);
		}
	}
}