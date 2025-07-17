package com.syamgot.as3.util.external
{
	import flash.external.ExternalInterface;

	public class External
	{

		public static function get enable():Boolean
		{
			if (!ExternalInterface.available)
			{
				return false;
			}

			if(ExternalInterface.call('function(){ return 1; }') == null)
			{
				return false;
			}

			return true;
		}
		
		public static function call(func:String, ... args:Array):String
		{
			if (!enable)
			{
				return '';
			}
			args.unshift(func);
			return ExternalInterface.call.apply(null, args);
		}

		public function External()
		{
		}
	}
}