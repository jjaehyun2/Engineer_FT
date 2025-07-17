package com.syamgot.as3.util.logging
{
	public class TraceHandler extends Handler
	{
		public function TraceHandler()
		{
			super();
		}
		
		override public function publish(record:LogRecord):void 
		{
			var buf:String = formatter.format(record);
			
			if (buf.substr(-1, 1) == "\n") 
			{
				buf = buf.substr(0, buf.length - 1);
			}
			trace(buf);
		}
		
	}
}