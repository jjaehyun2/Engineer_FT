package com.base.errors
{
	public class CallError extends Error
	{
		public function CallError(message:*="", id:*=0)
		{
			super(message, id);
		}
		
		public static function check(condition: Boolean, error: String): Boolean
		{
			if(!condition) throw new CallError(error);
			
			return !condition;
		}
	}
}