package com.lowoui_as.events 
{
	import flash.events.Event;
	
	public class MovieEvent extends Event
	{
		// Constants:
		public static const MOVIE_IN:String = "movieIn";
		public static const MOVIE_STAY:String = "movieStay";
		public static const MOVIE_OUT:String = "movieOut";

		/*public function MovieEvent(type:String, bubbles:Boolean = true, cancelable:Boolean = false, 
		                                    controllerIdx:uint = 0, buttonIdx:uint = 0, isKeyboard:Boolean = false,
		                                    isRepeat:Boolean = false)
		{
			super(type, bubbles, cancelable);
		}*/

		public function MovieEvent(type:String, bubbles:Boolean = false, cancelable:Boolean = true) 
		{
            super(type, bubbles, cancelable);
        }
	}
}