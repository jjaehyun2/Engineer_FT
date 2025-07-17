package com.ryzko.im.protocols.gadu.packets.outbound
{
	import com.ryzko.im.protocols.gadu.socket.GaduSocket;
	//import com.ryzko.im.protocols.gadu.user.LocalUserStatus;
	
	public class NewStatus80 extends OutboundPacket
	{
		
		public var status:int;				/* nowy status */
		public var flags:int;              	/* nowe flagi */
		public var descriptionSize:int;   	/* rozmiar opisu */
		public var description:String;		/* opis (nie musi wystąpić, bez \0) */

		
		public function NewStatus80()
		{
			super();
		}
		
		public function setOptions(status:int, _description:String = ""):void
		{
				
			this.status = status;
			this.description = _description;
			this.descriptionSize = description.length;
		}
		
		public override function write(socket:GaduSocket):void
		{
			body.writeInt(status);
			body.writeInt(0x00000001);
			body.writeInt(descriptionSize);
			body.writeUTFBytes(description);
			body.position = 0;
			
			header.type = OutboundPacketType.GG_NEW_STATUS80;
			header.length = body.bytesAvailable;
			
			sendPacket(socket);
			
		}
		
	}
}