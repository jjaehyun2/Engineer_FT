package
{
	import Beetle.NetPackage.IDataReader;
	import Beetle.NetPackage.IDataWriter;
	import Beetle.NetPackage.IMessage;
	import Beetle.NetPackage.Package;
	
	import flash.utils.ByteArray;
	
	public class NPPackage extends Package
	{
		public function NPPackage()
		{
			super();
		}
		protected override function  WriteMessageType(writer:IDataWriter, message:IMessage):void
		{
			writer.WriteUTF(flash.utils.getQualifiedClassName(message));	
		}
		
		protected override  function GetMessage(reader:IDataReader):IMessage
		{
			var name:String = reader.ReadUTF();
			if(name=="Register")
				return new Register();
			return null;
		}
	}
}