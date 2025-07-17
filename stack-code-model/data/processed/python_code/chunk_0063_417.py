package Beetle.NetPackage
{
	/**
	 * Copyright © henryfan 2013
	 * Created by henryfan on 13-7-30.
	 * homepage:www.ikende.com
	 * email:henryfan@msn.com
	 */
	import flash.utils.ByteArray;
	import Beetle.NetPackage.IMessage;
	public interface IDataWriter
	{
		function GetByteArray():ByteArray;
		
		function WriteBoolean(value:Boolean):void;
		
		function WriteByte(value:int):void;
		
		function WriteBytes(bytes:ByteArray, offset:uint = 0, length:uint = 0):void;
		
		function WriteDouble(value:Number):void;
		
		function WriteFloat(value:Number):void;
		
		function WriteInt(value:int):void;
		
		function WriteShort(value:int):void;
		
		function WriteUnsignedInt(value:uint):void;
		
		function WriteUTF(value:String):void;
		
		function Write(msg:IMessage):void;
	}
}