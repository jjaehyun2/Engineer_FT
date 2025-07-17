package Beetle.NetPackage
{
	
	/**
	 * Copyright © henryfan 2013
	 * Created by henryfan on 13-7-30.
	 * homepage:www.ikende.com
	 * email:henryfan@msn.com
	 */
	import flash.utils.ByteArray;
	import flash.utils.Endian;

	internal class CheckSize
	{
		public function CheckSize()
		{
			
		}
		
		public var Length:int=-1;
		
		private var mLittleEndian:String= Endian.LITTLE_ENDIAN;
		
		private var mSizeBuffer:ByteArray = new ByteArray();
		
		public function set LittleEndian(value:String):void
		{
			mLittleEndian= value;

		}
				
		public function get LittleEndian():String
		{
			return mLittleEndian;
		}
		
		public function Import(value:int):void
		{
			mSizeBuffer.writeByte(value);
			if(mSizeBuffer.length==4)
			{
				mSizeBuffer.endian= LittleEndian;
				mSizeBuffer.position=0;
				Length = mSizeBuffer.readInt();
				
			}		
		}
		
		public function Reset():void
		{
			Length=-1;
			mSizeBuffer.clear();
		}
		
	}
}