package baseflex.utils.strings
{
	//import libs.vo.GlobalsVO;
	
	public class Strings
	{
		public function Strings()
		{
		}
		
		
		/**
		 * Get the String name of the class object
		 */
		 
		public static function className(value:*):String {
			try {
				return String(String(value).split(" ")[1].split("]")[0]);
			} catch(e:Error) {}
			
			return String(value);
		}
		
		
		
		/**
		 * Create a substring
		 * @param p1:int - start pointer
		 * @param p2:int - end pointer
		 * @param arr:Array - Text Array
		 * @param delimeter:String - String Delimeter 
		 * to add to the new substring
		 */
		 
		public static function buildSentence(p1:int,p2:int,arr:Array,delimeter:String):String {
			var i:int = p1;
			var s:String = new String();
			
			while(i<p2) {
				s += arr[i]+delimeter;
				++i;
			}
			
			return s;
		}
		
		
		/**
		 * Convert a string to Boolean
		 * @param s
		 * @return 
		 */
		 		
		public static function strToBool(s:String):Boolean {
			if(s=="true") return true;
			return false;
		}
		
		
		
		
		
		
		public static function trim(value:String):String {
			return value.match(/^\s*(.*?)\s*$/)[1];
		}
		
		
		
		
		
		public static function removeChar(str:String,remove:String):String {
			return str.split(remove).join("");
		}
		
		
		/**
		 * Is the character a number 
		 * @param char
		 * @return 
		 */
		 		
		public static function isNumeric(char:uint):Boolean {
			return ( (char >= 0x30) && (char <= 0x39) );
		}
		
		
		/**
		 * Is the string a number 
		 * @param s
		 * @return 
		 */
		 		
		public static function isStringNumeric(s:String):Boolean {
			for (var i:int = 0; i < s.length; i++) {
				if (!isNumeric(s.charCodeAt(i))) {
					return false;
				}
			}
			return true;
		}
		
		
		
		
		
		/** Remove all string values before start
		 * and after end */
		public static function crop(result:String,start:String, end:String):String {
			result = result.substring(0,result.lastIndexOf(end));
			return result.substr(result.indexOf(start)+1); 
		}
		
		
		
		
		
		/**
		 * Replace from with to 
		 * @param file
		 * @param from
		 * @param to
		 * @return newString:String
		 */
		 
		public static function filter(file:String,from:String,to:String):String {
			return file.replace(from, to);
		}
	}
}