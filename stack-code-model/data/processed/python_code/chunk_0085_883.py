package com.tourism_in_lviv.air.services
{

	public class UrlParameter
	{
		private var _name:String;
		private var _value:String;

		public function UrlParameter( name:String, value:String )
		{
			_name = name;
			_value = value;
		}

		public function toString():String
		{
			return _name + "=" + _value;
		}
	}
}