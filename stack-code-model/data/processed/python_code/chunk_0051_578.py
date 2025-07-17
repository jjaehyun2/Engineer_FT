package vo {
	
	import mx.utils.ObjectUtil;
	
	/*
	 * <ul>
	 *  <li><code>clear():void</code></li>
	 *  <li><code>containsKey(key:String):Boolean</code></li>
	 *  <li><code>containsValue(value:Object):Boolean</code></li>
	 *  <li><code>isEmpty():Boolean</code></li>
	 *  <li><code>keySet():Array</code></li>
	 *  <li><code>put(key:String,value:Object):Object</code></li>
	 *  <li><code>putAll(map:Map):void</code></li>
	 *  <li><code>get(key:String):Object</code></li>
	 *  <li><code>remove(key:String):Object</code></li>
	 *  <li><code>size():int</code></li>
	 *  <li><code> values():Array</code></li>
	 * </ul>
	 * @version 1.0 2013/11/21
	 * @author dongliyang 
	 */
	public class Map {
		
		private var _dataMap:Object = null;
		
		/**
		 * <ul>
		 *  <li><code>clear():void</code></li>
		 *  <li><code>containsKey(key:String):Boolean</code></li>
		 *  <li><code>containsValue(value:Object):Boolean</code></li>
		 *  <li><code>isEmpty():Boolean</code></li>
		 *  <li><code>keySet():Array</code></li>
		 *  <li><code>put(key:String,value:Object):Object</code></li>
		 *  <li><code>putAll(map:Map):void</code></li>
		 *  <li><code>get(key:String):Object</code></li>
		 *  <li><code>remove(key:String):Object</code></li>
		 *  <li><code>size():int</code></li>
		 *  <li><code> values():Array</code></li>
		 * </ul>
		 */
		public function Map(){
			_dataMap = new Object();
		}
		
		/**
		 */
		public function clear():void {
			for each(var key:String in keys()){
				delete _dataMap[key];
			}
		}
		
		/**
		 */
		public function containsKey(key:String):Boolean {
			if(key == null){
				return false;
			}
			return _dataMap.hasOwnProperty(key);
		}
		
		/**
		 */
		public function containsValue(value:Object):Boolean {
			for each(var key:String in keys()){
				if(ObjectUtil.compare(_dataMap[key],value) == 0){
					return true;
				}
			}
			return false;
		}
		
		/**
		 */
		public function isEmpty():Boolean {
			return keys().length == 0;
		}
		
		/**
		 */
		public function keySet():Array {
			return keys();
		}
		
		/**
		 */
		public function put(key:String,value:Object):Object {
			if(key == null){
				throw new Error("Key can not be null");
			}
			if(containsKey(key)){
				var oldValue:Object = _dataMap[key];
				_dataMap[key] = value;
				return oldValue;
			} else {
				_dataMap[key] = value;
				return null;
			}
			
		}
		
		/**
		 */
		public function putAll(map:Map):void {
			if(map == null){
				throw new Error("Specific Map is null");
			}
			
			for each(var key:String in map.keySet()){
				_dataMap[key] = map.get(key);
			}
		}
		
		/** 
		 */
		public function get(key:String):Object {
			if(containsKey(key)){
				return _dataMap[key];
			} else {
				return null;
			}
		}
		
		/**
		 */
		public function remove(key:String):Object {
			if(containsKey(key)){
				var oldValue:Object = get(key);
				delete _dataMap[key];
				return oldValue;
			} else {
				return null;
			}
		}
		
		/**
		 */
		public function size():int {
			return keys().length;
		}
		
		/**
		 */
		public function values():Array {
			var values:Array = new Array();
			for each(var key:String in keys()){
				values.push(_dataMap[key]);
			}
			return values;
		}
		
		/**
		 */
		private function keys():Array {
			var clsInfo:Object = ObjectUtil.getClassInfo(_dataMap);
			var props:Array = clsInfo["properties"];
			var keys:Array = new Array();
			for each(var q:QName in props){
				keys.push(q.localName);
			}
			return keys;
		}
	}
}