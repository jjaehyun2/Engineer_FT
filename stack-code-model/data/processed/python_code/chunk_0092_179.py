package com.syamgot.as3.util.logging
{
	public class StreamHandler extends Handler
	{
		public function StreamHandler()
		{
			super();
		}
		
		override public function publish(record:LogRecord):void 
		{
			return;	
		}
		
		override public function close():void 
		{
			return;
		}
	}
}