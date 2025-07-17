package model {
	
	/**
	 * ...
	 * @author hongjie
	 */
	public final class XianCao extends Cell {
		
		private var _dir:int;
		
		private var _typeStr:String = '';
		
		public function XianCao(width:int, height:int, dir:int) {
			super(width, height, 0x5b9bd5);
			_dir = dir
		}
		
		public function get dir():int {
			return _dir;
		}
		
		public function set dir(value:int):void {
			_dir = value;
		}
		
		public function get size():int {
			return _dir == Enum.H ? _h : _w;
		}
		
		public function set size(val:int):void {
			if (_dir == Enum.H) {
				setSize(_w, val);
			} else {
				setSize(val, _h);
			}
		}
		
		public function get typeStr():String {
			return _typeStr;
		}
		
		public function set typeStr(value:String):void {
			_typeStr = value;
		}
		
		override public function toXML():String {
			// return '<trunking NAME="Trunk_0001" SIZE="800,10" START="0,0" END= "0,800" />';
			return '<trunking type="' + _typeStr + '" name="' + this.name + '" x="' + this.x + '" y="' + this.y + '" w="' + this.reallyWidth + '" h="' + this.reallyHeight + '" dir="' + dir + '" />';
		}
	
	}

}