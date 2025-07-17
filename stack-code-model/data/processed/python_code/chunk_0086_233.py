package com.ryzko.im.protocols.gadu.packets.outbound
{
	import com.ryzko.im.protocols.gadu.settings.ProtocolSettings;
	import com.ryzko.im.protocols.gadu.socket.GaduSocket;
	//import com.ryzko.im.protocols.gadu.user.LocalUserStatus;
	
	public class Login80Packet extends OutboundPacket
	{
		
		public var hash:String;
		private var settings:ProtocolSettings;
		
		public function Login80Packet()
		{
			settings = ProtocolSettings.getInstance();
		}
		
		public override function write(socket:GaduSocket):void
		{
			
			var uin:int = settings.UID;            	/* numer Gadu-Gadu */
	        var language:String = 'pl';     								/* język: "pl" */
	        var hash_type:uint = 0x02;       								/* rodzaj funkcji skrótu hasła */
	        //var hash:String;        										/* skrót hasła dopełniony \0 */
	        var status:uint = settings.STATUS;           							/* początkowy status połączenia */
	        var flags:int;            										/* początkowe flagi połączenia */
	        var features:int = 0x00000007;//0x00000737;         			/* opcje protokołu (0x00000367)*/
	        var local_ip:int = 0;         									/* lokalny adres połączeń bezpośrednich (nieużywany) */
	        var local_port:int = 0;     									/* lokalny port połączeń bezpośrednich (nieużywany) */
	        var external_ip:int = 0;     									/* zewnętrzny adres (nieużywany) */
	        var external_port:int = 0;  									/* zewnętrzny port (nieużywany) */
	        var image_size:uint = 0;      									/* maksymalny rozmiar grafiki w KB */
	        var unknown2:uint = 0x64;        								/* 0x64 */
	        var version_len:int = 0x23;     								/* długość ciągu z wersją (0x23) */
	        var version:String = "Gadu-Gadu Client build 10.0.0.10547";     /* "Gadu-Gadu Client build 10.0.0.10450" (bez \0) */
	        var description_size:int = settings.DESC.length; 									/* rozmiar opisu */
	        var description:String = settings.DESC;   								/* opis (nie musi wystąpić, bez \0) */
	        
	       	body.writeInt(uin);
			body.writeUTFBytes(language);
			body.writeByte(hash_type);
			
			for (var j:Number = 0; j<20; j++)
			{
				var t:String = hash.slice(j*2,j*2+2)
				var u:uint = uint('0x'+t);
				body.writeByte(u);
			}

			for (var i:Number = 0; i<44; i++)
			{
				body.writeByte(0x0);
			}
			
			body.writeInt(status);
			body.writeInt(3);
			body.writeInt(features);
			body.writeInt(0);
			body.writeShort(0);
			body.writeInt(0);
			body.writeShort(0);
			body.writeByte(0xff);
			body.writeByte(unknown2);
			body.writeInt(version.length);
			body.writeUTFBytes(version);
			body.writeInt(description_size);
			body.writeUTFBytes(description);
			body.position = 0;
			
			header.type = OutboundPacketType.GG_LOGIN80;
			header.length = body.bytesAvailable;
			
			sendPacket(socket);
		
		}

	}
}