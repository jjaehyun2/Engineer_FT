package com.as3long.node.utils 
{
	/**
	 * ...
	 * @author lonnyhuang
	 */
	public class Debug 
	{
		
		public function Debug() 
		{
			
		}
		
		public function outObject(obj:Object):void
		{
			for (var k:String in obj)
			{
				trace(k);
				// trace(k, obj[k]);
			}
		}
		
		private static var _one:Debug;
		public static function one():Debug
		{
			if (!_one)
			{
				_one = new Debug();
			}
			
			return _one;
		}
	}

}