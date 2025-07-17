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

	public  class Package
	{
		public function Package()
		{
			
		}
		
		private var mLoading:Boolean= false;
		
		private var mCheckSize:CheckSize = null;		
		
		private var mLittleEndian:String = Endian.LITTLE_ENDIAN;
		
		private var mStream:ByteArray = new ByteArray();
		
		public function set LittleEndian(value:String):void
		{
			mLittleEndian = value;
		}
		
		public function get LittleEndian():String
		{
			return mLittleEndian;
		}
		
		
		public var Receive:Function;
		
		public  function Import(data:ByteArray, start:int, count:int):void
		{
			if (mCheckSize == null)
			{
				mCheckSize = new CheckSize();
				mCheckSize.LittleEndian = LittleEndian;
			}
			while (count > 0)
			{
				if (!mLoading)
				{
					mCheckSize.Reset();
					mStream.endian = LittleEndian;
					mStream.clear();
					mLoading = true;
				}
				if (mCheckSize.Length == -1)
				{
					while (count > 0 && mCheckSize.Length == -1)
					{
						mCheckSize.Import(data[start]);
						start++;
						count--;
					}
					
				}
				else
				{
					var importInfo:ImportInfo = new ImportInfo(start,count);
					if (OnImport(data, importInfo))
					{
						mLoading = false;
						if (Receive != null)
						{
							mStream.position=0;
							Receive(mStream);
						}
					}
					start= importInfo.Start;
					count=importInfo.Count;
					
				}
			}
		}   
		
		private function  OnImport(data:ByteArray, info:ImportInfo):Boolean
		{
			if (info.Count >= mCheckSize.Length)
			{
				mStream.writeBytes(data,info.Start,mCheckSize.Length);
				info.Start += mCheckSize.Length;
				info.Count -= mCheckSize.Length;
				return true;
			}
			else
			{
				mStream.writeBytes(data, info.Start, info.Count);
				info.Start += info.Count;
				mCheckSize.Length -= info.Count;
				info.Count = 0;
				return false;
			}
			
		}
		
		protected function  WriteMessageType(writer:ByteArray, message:IMessage):void
		{
		
		}
		
		protected  function GetMessage(reader:ByteArray):IMessage
		{
			return null;
		}
		
		public function SendCast(msg:Object):IMessage
		{
			return IMessage(msg);
		}
		
		public function ReceiveCaste(msg:IMessage):Object
		{
			return msg;
		}
		
		public  function FromStream(reader:ByteArray):IMessage
		{
			try
			{
				var msg:IMessage = GetMessage(reader);
				
				msg.Load(reader);
				return msg;
			}
			catch (e_:Error)
			{
				throw new Error("read message error!");
			}
			return null;
		}
		
		public function GetMessageData(msg:IMessage):ByteArray
		{
			var writer:ByteArray = new ByteArray();
			writer.endian= LittleEndian;
			WriteMessageType(writer, msg);
			msg.Save(writer);
			var result:ByteArray = new ByteArray();
			result.endian = LittleEndian;
			result.writeInt(writer.length);
			result.writeBytes(writer,0,writer.length);
			return result;
		}
	}
}