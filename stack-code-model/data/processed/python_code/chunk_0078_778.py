package com.ryzko.im.protocols.gadu.events
{
	import com.ryzko.im.protocols.gadu.message.Message;

	public class MessageEvent extends ProtocolEvent
	{
		
		public static const MESSAGE_RECEIVED:String = 'messageReceived';
		public static const MESSAGE_SEND_SUCCEED:String = 'message_send_succeed';
		public static const MESSAGE_SEND_FAILED:String = 'message_send_failed';
		
		public var message:Message;
		
		public function MessageEvent(type:String = MESSAGE_RECEIVED, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
	}
}