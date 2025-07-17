package vzw.utils {
	public class MenuIdManager {
		private var _next_id:int = -1;
		
		private var _filterFunc:Function;
		
		private var _id_list:Array = [];

		public function MenuIdManager(ids:Array,filterFunc:Function) {
			this._filterFunc = filterFunc;
			
			var i:String;
			for (i in ids) {
				this.add_id(ids[i]);
			}
		}
		
		private function determine_greatest():void {
			var n:int = -1;
			var i:String;
			var m:int;
			for (i in this._id_list) {
				m = this._id_list[i];
				n = (m > n) ? m : n;
			}
			this._next_id = n+1;
		}
		
		public function get next_id():int {
			return this._next_id;
		}
		
		public function add_id(aValue:*):void {
			var _value:int = (aValue is String) ? this._filterFunc(aValue) : int(aValue);
			this._id_list.push(_value);
			this.determine_greatest();
		}
	}
}