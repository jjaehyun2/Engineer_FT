package baseflex.utils.objects {
	import flash.utils.ByteArray;
	
	public class ObjectUtils {
		public static function keys(obj:*):Array {
			var i:String;
			var keys:Array = [];
			for (i in obj) {
				keys.push(i);
			}
			return keys;
		}

		public static function initialize(obj:*):void {
			var i:String;
			var keys:Array = keys(obj);
			for (i in keys) {
				obj[i] = null;
			}
		}

		public static function deepCopyFrom(source:Object):* {
		    var myBA:ByteArray = new ByteArray();
		    myBA.writeObject(source);
		    myBA.position = 0;
		    var o:Object = myBA.readObject();
		    return(o);
		}
	}
}