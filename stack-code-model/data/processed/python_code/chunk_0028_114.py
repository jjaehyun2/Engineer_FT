package baseflex.utils.strings
{
	import flash.external.ExternalInterface;
	
	
	public class QueryString
	{
		
		private static const QSTART:String = "?";
		private static const QSEPARATOR:String = "&";
		private static const QVALUE:String = "=";
		
		
		
		public function QueryString() {
		}
		
		
		
		/**
		 * Create an name and value object
		 * of all the query string data 
		 * @param queryStr
		 * @return - new hash object 
		 */
		 		
		public static function parse(queryStr:String,removeLastChar:String=null):Object {
			var np:Object = new Object();
			var ar:Array = queryStr.split(QSTART);
			var params:Array = (ar.length > 1) ? ar[1].split(QSEPARATOR) : [];
			if(params.length == 0) return null;
			
			for (var g:int = 0; g < params.length; g++){
				var index:int=0;
				var kvPair:String = params[g];
					
				if((index = kvPair.indexOf(QVALUE)) > 0){
					var key:String = kvPair.substring(0,index);
					removeLastChar!=null ?
					np[key] = Strings.removeChar(kvPair.substring(index+1),removeLastChar) :
					np[key] = kvPair.substring(index+1);
				}
			}
			
			return np;
		}
	}
}