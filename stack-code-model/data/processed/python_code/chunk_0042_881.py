package com.ryzko.im.protocols.gadu.events
{
	public class ConnectionEvent extends ProtocolEvent
	{
		public static const CONNECTED:String = 'connected';
		public static const DISCONNECTED:String = 'disconnected';
		
		public function ConnectionEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
	}
}