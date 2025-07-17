package com.adobe.dashboard.event
{
	import flash.events.Event;

	public class SetUpEvent extends Event
	{
		public static const SET_UP_EVENT:String="setUpEvent";

		public static const SET_UP_COMPLETE_EVENT:String="setUpCompleteEvent";


		/**
		 * constuctor
		 */
		public function SetUpEvent(type:String)
		{
			super(type);
		}

		/**
		 * always override the clone method
		 */
		override public function clone():Event
		{
			return new SetUpEvent(type);
		}
	}
}