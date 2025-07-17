package com.lowoui_as.events
{
	import flash.events.Event;
	
	public class DialogEvent extends Event
	{
		public static const CLOSE:String = "dialogClose";
		public static const SUBMIT:String = "dialogSubmit";
		
		public function DialogEvent(type:String, bubbles:Boolean = false, cancelable:Boolean = true)
		{
			super(type, bubbles, cancelable);
		}
	}
}