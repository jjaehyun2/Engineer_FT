package com.ryzko.im.protocols.gadu.events
{
	import flash.events.Event;
	
	public class ProtocolEvent extends Event
	{
		public var protocol:String;

		public function ProtocolEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=true)
		{
			super(type, bubbles, cancelable);
		}
	}
}