package com.ryzko.im.protocols.gadu.socket
{
	import flash.net.Socket;
	import flash.utils.ByteArray;
	
	import com.ryzko.im.protocols.gadu.packets.PacketHeader;
	
	public class GaduSocket extends Socket
	{
		public function GaduSocket(host:String=null, port:int=0)
		{
			super(host, port);
		}
		
		public function writeHeader(header:PacketHeader):void
		{
			writeInt(header.type);
			writeInt(header.length);
		}
		
		public function writeBody(body:ByteArray):void
		{
			body.position = 0;
			writeBytes(body, 0, body.bytesAvailable);
			flush();
		}
	}
}