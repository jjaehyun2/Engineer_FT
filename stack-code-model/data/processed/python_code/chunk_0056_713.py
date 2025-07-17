////////////////////////////////////////////////////////////////////////////////
//
//  CODE11.COM
//  Copyright 2011
//  licenced under GPU
//
//  @author		Romeo Copaciu romeo.copaciu@code11.com
//  @date		24 May 2011
//  @version	1.0
//  @site		code11.com
//
////////////////////////////////////////////////////////////////////////////////

package com.code11.google.calendar.util
{
	import mx.formatters.DateFormatter;

	public class CalendarUtil
	{
		public function CalendarUtil()
		{
		}
		
		private static var dateFormatter:DateFormatter;
		public static function dateToTimestamp(date:Date):String {
			if (!dateFormatter) {
				dateFormatter = new DateFormatter();
				dateFormatter.formatString = "YYYY-MM-DDTJ:NN:SS";
			}
			var dateString:String = dateFormatter.format(date);
			if (dateString.length < 19) dateString = dateString.replace("T","T0");
			return dateString;
		}
		
		private static var simpleDateFormatter:DateFormatter;
		public static function dateToSimpletime(date:Date):String {
			if (!simpleDateFormatter) {
				simpleDateFormatter = new DateFormatter();
				simpleDateFormatter.formatString = "YYYYMMDDTJNNSS";
			}
			var dateString:String = simpleDateFormatter.format(date);
			if (dateString.length < 15) dateString = dateString.replace("T","T0");
			return dateString;
		}
		
	}
}