package com.wm.net.py 
{
	import flash.utils.ByteArray;
	/**
	 * 传输用的网络整包, 包定义为: 
	 * | packet length(4) | cmd id(2) | fmt length(2) | fmt string(n) + data(m) |
	 * @author wmTiger
	 */
	public class Packet 
	{
		private static const SIZE_BYTES_HEAD : int = 8;
		
		private var _cmdId:int;
		private var _content:ByteArrayLittle;// 包含了fmt和具体数据的ByteArray
		private var _fmt:String = "";// 格式fmt
		private var _data:Array;// 数据按照列表顺序 存放/解析
		
		public function Packet(cmdId:int) 
		{
			_cmdId = cmdId;
			_content = new ByteArrayLittle();
			_data = [];
		}
		
		public static function buildPacket(buf : ByteArrayLittle) : Packet {
			var pk : Packet = new Packet(0);
			if (pk.unpack( buf )) 
			{
				return pk;
			}
			return null;
		}
		
		public function unpack(buf:ByteArray):Boolean
		{
			if (buf.bytesAvailable < SIZE_BYTES_HEAD)
			{
				return false; // 长度不够，默认是 ${SIZE_BYTES_HEAD} 的长度
			}
			var pos:int = buf.position;
			var len:uint = buf.readInt();
			if (buf.bytesAvailable < len + SIZE_BYTES_HEAD - 4)
			{
				buf.position = pos;
				return false;
			}
			_cmdId = buf.readShort();
			var fmtLen:int = buf.readShort();// fmt的字符串的长度，不能比len长
			if (len > 0 && len >= fmtLen)
			{
				_content.writeBytes(buf, buf.position, len);
				_content.position = 0;
				_fmt = _content.readUTFBytes(fmtLen);
				buf.position += len;
				_content.position = fmtLen;// 从fmt长度之后，开始读正式数据
				buildContentToData();// 按fmt顺序将获取到的参数读出，放入data列表
			}
			return true;
		}
		
		public function pack():ByteArray
		{
			buildDataToContent();
			var bytes:ByteArray = new ByteArrayLittle();
			bytes.writeInt(_content.length);
			bytes.writeShort(_cmdId);
			bytes.writeShort(_fmt.length);
			bytes.writeBytes(_content);
			return bytes;
		}
		
		private function buildDataToContent():void
		{
			// 将fmt改成展开的fmt格式，s类型不加前缀数字，比如: 3i2hss -> iiihhss
			var fmtRes:String = CmdConst.CMD_FMT[_cmdId][0];
			var fmtArray:Array = getFmtArray(fmtRes);
			var i:int;
			var total:int = 0;
			for (i = 0; i < fmtArray.length; i++) 
			{
				var tempCell:Object = fmtArray[i];
				total += tempCell['num'];
			}
			if (total != _data.length) 
			{
				throw new Error("数据定义格式长度 与 具体数据长度 不符合!写入失败!");
				return;
			}
			_fmt = getReadFmt(fmtArray);
			_content.writeUTFBytes(_fmt);
			// 将data写入content的bytearray格式
			setData(fmtArray, 1);
		}
		
		private function getReadFmt(fmtArray:Array):String
		{
			var fmt:String = "";
			var i:int = 0;
			var idx:int = 0;
			for (i = 0; i < fmtArray.length; i++) 
			{
				var tempCell:Object = fmtArray[i];
				if (tempCell['type'] == "s") 
				{
					tempCell['num'] = _data[idx].length;
					idx += 1;
				}else
				{
					idx += tempCell['num'];
				}
				
				if (tempCell['num'] > 1) 
				{
					fmt += (tempCell['num'] + tempCell['type']);
				}else
				{
					fmt += (tempCell['type']);
				}
			}
			return fmt;
		}
		
		private function buildContentToData():void 
		{
			if (_fmt && _fmt.length > 0 && _content && _content.length > 0) 
			{
				var len:int = _fmt.length;
				var fmtArray:Array = getFmtArray(_fmt);
				// 将content写入data的列表格式
				setData(fmtArray, 0);
			}
		}
		
		private function getFmtArray(fmt:String):Array
		{
			var len:int = fmt.length;
			var fmtArray:Array = [];
			var cc:int;
			var tempNum:String = "";
			var tempCellFmt:Object;// 格式为: {num:2, type:s}
			for (var i:int = 0; i < len; i++) 
			{
				cc = fmt.charCodeAt(i);
				if (cc >= 48 && cc <= 57) 
				{
					// number 0-9
					tempNum += fmt.charAt(i);
				}else if ((cc >= 65 && cc <= 90) || (cc >= 97 && cc <= 122))
				{
					tempCellFmt = { };
					tempCellFmt['num'] = tempNum.length > 0 ? int(tempNum) : 1;
					tempCellFmt['type'] = fmt.charAt(i);
					fmtArray.push(tempCellFmt);
					tempNum = "";
				}
			}
			return fmtArray;
		}
		
		/** type=0: read; type = 1: write */
		private function setData(fmtArray:Array, type:int = 0):void
		{
			var len:int = fmtArray.length;
			var j:int;
			var i:int;
			var dataIdx:int = 0;
			for (i = 0; i < len; i++) 
			{
				var tempCell:Object = fmtArray[i];
				var num:int = tempCell['num'];
				var fmtType:String = tempCell['type'] + "";
				switch (fmtType) 
				{
					case "h":
						for (j = 0; j < num; j++) 
						{
							if (type == 0) 
							{
								_data.push(_content.readShort());
							}else 
							{
								_content.writeShort(_data[dataIdx]);
								dataIdx++;
							}
						}
					break;
					case "i":
						for (j = 0; j < num; j++) 
						{
							if (type == 0) {
								_data.push(_content.readInt());
							}else {
								_content.writeInt(_data[dataIdx]);
								dataIdx++;
							}
						}
					break;
					case "d":
						for (j = 0; j < num; j++) 
						{
							if (type == 0) {
								_data.push(_content.readDouble());
							}else {
								_content.writeDouble(_data[dataIdx]);
								dataIdx++;
							}
						}
					break;
					case "s":
						if (type == 0) {
							_data.push(_content.readUTFBytes(num));
						}else {
							_content.writeUTFBytes(_data[dataIdx]);
							tempCell['num'] = _data[dataIdx].length;
							dataIdx++;
						}
					break;
					default:
					break;
				}
			}
		}
		
		public function get data():Array 
		{
			return _data;
		}
		
		public function set data(value:Array):void 
		{
			_data = value;
		}
		
		public function get cmdId():int 
		{
			return _cmdId;
		}
		
	}

}