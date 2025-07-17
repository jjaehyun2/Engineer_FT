package com.arxterra.events
{
	import flash.events.Event;
	import flash.utils.ByteArray;
	
	public class SocketBytesEvent extends Event
	{
		// event type constants
		public static const SOCKET_BYTES:String = 'socketBytes';
		
		// event properties
		public var bytes:ByteArray;
		
		// constructor
		public function SocketBytesEvent ( type:String, bytes:ByteArray, bubbles:Boolean = false, cancelable:Boolean = false )
		{
			super ( type, bubbles, cancelable );
			this.bytes = bytes;
		}
		
		// overrides
		public override function clone ( ) : Event
		{
			return new SocketBytesEvent ( type, this.bytes, bubbles, cancelable );
		}
		
		public override function toString ( ) : String
		{
			return formatToString ( 'SocketBytesEvent', 'type', 'bytes', 'bubbles', 'cancelable' );
		}
	}
}