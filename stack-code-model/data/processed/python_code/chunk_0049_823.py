package utils {
	
	/**
	 * 
	 * @author Administrator
	 */
	public class HashMap {
		private var _items:Array = new Array();
		
		public function HashMap() {
		}
		
		public function putItem(key:*, value:*):void {
			_items.push({"key": key, "value": value});
		}
		
		public function getItem(key:*):* {
			for each (var obj:Object in _items) {
				if (obj.key == key) {
					return obj.value;
					break;
				}
			}
		}
	}
}