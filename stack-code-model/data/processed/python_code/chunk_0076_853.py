package com.syamgot.as3.util.logging
{
	import com.syamgot.as3.util.external.External;

	public class WebKitConsoleHandler extends Handler
	{
		public function WebKitConsoleHandler()
		{
			super();
			
			if (!External.enable) 
			{
				throw new Error('ExternalInterface initialize is failed.');
			}
		}
		
		override public function publish(record:LogRecord):void 
		{
			var buf:String = formatter.format(record);
			External.call('console.log', buf);
		}
	}
}