package com.illuzor.otherside.errors {
	
	import com.illuzor.otherside.debug.log;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public final class ScreenError extends Error{
		
		public function ScreenError(message:String, id:uint = 0) {
			name = "ScreenError";
			super(name + ": " + message, id);
		}
		
	}
}