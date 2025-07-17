package framework.utils
{
	public class UtilsString
	{
		public static const DECIMAL_DIGITS:String = "0123456789";
		public static const ROMAN_LETTERS:String = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
		public static const GERMAN_LETTERS:String = "AaBbÄäÖöÜü";
		public static const SPECIAL_LETTERS:String = "!\"№%:,.;(?>@#$^&*|/";
		
		/**
		 *  Check exist dictionary characters into input string.
		 *  
		 *  @param input:String - input string.
		 *  @param dictionary:String - letters dictionary (defaut "").
		 *  
		 *  @return state of existing symbols in input string similar to
		 *          dictionary symbols.
		 */
		public static function hasDictionary(input:String, dictionary:String = ""):Boolean
		{
			for(var i:int = 0; i < input.length; i++)
			{
				var inputChar:String = input.charAt(i);
				for(var j:int = 0; j < dictionary.length; j++)
				{
					if (inputChar == dictionary.charAt(j))
						return true;
				}
			}
			return false;
		}
	}
}