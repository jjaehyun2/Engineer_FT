package Beetle.NetPackage
{
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	/**
	 * Copyright © henryfan 2013
	 * Created by henryfan on 13-7-30.
	 * homepage:www.ikende.com
	 * email:henryfan@msn.com
	 */
	public class DataWriter implements IDataWriter
	{
		public function DataWriter(stream:ByteArray,littleEndian:Boolean)
		{
			mStream = stream;
			mStream.endian = littleEndian?Endian.LITTLE_ENDIAN:Endian.BIG_ENDIAN;
		}
		
		private var mStream:ByteArray;
		
		public function GetByteArray():ByteArray
		{
			return mStream;
		}
		
		public function WriteBoolean(value:Boolean):void
		{
			mStream.writeBoolean(value);
		}
		
		public function WriteByte(value:int):void
		{
			mStream.writeByte(value);
		}
		
		public function WriteBytes(bytes:ByteArray, offset:uint = 0, length:uint = 0):void
		{
			mStream.writeBytes(bytes,offset,length);
		}
		
		public function WriteDouble(value:Number):void
		{
			mStream.writeDouble(value);
		}
		
		public function WriteFloat(value:Number):void
		{
			mStream.writeFloat(value);
		}
		
		public function WriteInt(value:int):void
		{
			mStream.writeInt(value);	
		}
		
		public function WriteShort(value:int):void
		{
			mStream.writeShort(value);	
		}
		
		public function WriteUnsignedInt(value:uint):void
		{
			mStream.writeUnsignedInt(value);	
		}
		
		public function WriteUTF(value:String):void
		{
			mStream.writeUTF(value);	
		}
		
		public function Write(msg:IMessage):void
		{
			msg.Save(this);
		}
	}
}