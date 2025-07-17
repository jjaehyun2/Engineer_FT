package com.choa.fitbit.helper 
{
	import flash.utils.Dictionary;
	/**
	 * ...
	 * @author Michael-Bryant Choa
	 */
	public class HttpUtility 
	{
		public static function parseQueryString(query:String):Dictionary
		{
			var nameValDict:Dictionary = new Dictionary();
			var queries:Array = query.split("&");
			for each(var query:String in queries)
			{
				var nameValPair:Array = query.split("=");
				nameValDict[nameValPair[0]] = nameValPair[1];
			}
			
			return nameValDict;
		}
	}

}