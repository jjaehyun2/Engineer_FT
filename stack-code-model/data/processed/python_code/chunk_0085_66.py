package com.riaspace.nativeApplicationUpdater.events {
	import flash.events.Event;

	public class CannotPerformUpdateEvent extends Event {
		public function CannotPerformUpdateEvent(type:String, error:Error, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			this.error = error;
		}
		
		public var error:Error;
		
        public static const TYPE_CANNOT_PERFORM_UPDATE:String = "cannotPerformUpdate";

        override public function clone():Event {
            return new CannotPerformUpdateEvent(type,this.error);
        }
	}
}