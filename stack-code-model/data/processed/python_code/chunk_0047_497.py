package com.yjacket.taskerTasker.util
{
	public final class TimeUtil
	{
		public static const SEC:uint = 1;
		public static const MIN:uint = SEC * 60;
		public static const HOUR:uint = MIN * 60;
		public static const DAY:uint = HOUR * 24;
		public static const YEAR:uint = DAY * 365;
		
		public static function toString(second:Number):String
		{
			var a:Array = [];
			var result:String = "";
			
			if (!second || second <= 0) return "00:00:00";
			
			if (second >= DAY) 
			{
				var t:int = int(second / DAY);
				result = t + "d ";
				second = second % DAY;
			}
			
			if (second >= HOUR) 
			{
				t = int(second / HOUR);
				result += (t < 10 ? "0" + t : t) + ":"; 
				second = second % HOUR;
			}
			else
				result += "00:";
			
			if (second >= MIN) 
			{
				t = int(second / MIN);
				result += (t < 10 ? "0" + t : t) + ":"; 
				second = second % MIN;
			}
			else
				result += "00:";
			
			if (second > 0)
				result += (second < 10 ? "0" + second : second); 
			else
				result += "00";
			
			return result;			
		}
	}
}