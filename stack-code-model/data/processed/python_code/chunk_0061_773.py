package framework.utils
{
	import mx.core.Application;
	import mx.utils.StringUtil;
	
	public class HeliumHelper
	{
		/**
		 *  These constants are directions of conversion.
		 */
		public static const SERVER_TO_CLIENT:int = 1;
		public static const CLIENT_TO_SERVER:int = 2;
		/**
		 *  These constants are formats of date.
		 */
		public static const DATE_CLIENT_FORMAT:String = "DD/MM/YYYY";
		public static const DATE_SERVER_FORMAT:String = "YYYY-MM-DD";
		
		/**
		 *  Convert date from one format to other.
		 *  
		 *  @param date:String - date as string for view;
		 *  @param direction:int - direction of conversation (format type).
		 *  
		 *  @return date as formatted by output format.
		 *  
		 *  @usage
		 *      var date:String = "2010-02-25";
		 *      var convert:String = HeliumHelper.dateConvert(date, HeliumHelper.SERVER_TO_CLIENT);
		 *      trace("convert date = " + convert);    // convert date = 25/02/2010
		 */
		public static function dateConvert(date:String, direction:int):String
		{
			if (null == date) return "";
			
			var parts:Array = [];
			var inputDelimeter:String;
			var outputDelimeter:String;
			// check direction of convertoim
			switch (direction)
			{
				// YYYY-MM-DD -> DD/MM/YYYY
				case SERVER_TO_CLIENT:
					inputDelimeter = "-";
					outputDelimeter = "/";
					break;
				// DD/MM/YYYY -> YYYY-MM-DD
				case CLIENT_TO_SERVER:
					inputDelimeter = "/";
					outputDelimeter = "-";
					break;
			}
			// split input date by delimeter
			parts = date.split(inputDelimeter);
			if (parts.length != 3)
			{
				return "Error convert";
			}
			// make convert
			return StringUtil.substitute("{0}" + outputDelimeter + "{1}" + outputDelimeter + "{2}",
				parts[2], parts[1], parts[0]);
		}
		
		public static var rootURL:String = "";
	}
}