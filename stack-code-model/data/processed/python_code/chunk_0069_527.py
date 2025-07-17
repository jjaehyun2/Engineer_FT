package com.ryzko.im.protocols.gadu.events
{
	import flash.events.Event;

	public class HTTPServicesEvent extends Event
	{
		
		public static const SERVER_INFO_RESPONSE:String = 'server_info_response';
		
		public var host:String;
		public var port:int;
		
		public function HTTPServicesEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
		
	}
}