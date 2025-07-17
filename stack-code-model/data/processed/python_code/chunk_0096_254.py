package com.massiveProCreation.events {
	/*// IMPORTS /*/
	import flash.events.Event;
	
	public class CustomEvent extends Event {
		// xml loaded event
		public static const XML_LOADED:String = "xmlLoaded";
		// image loaded event
		public static const IMAGE_LOADED:String = "imageLoaded";
		// thumbnail loaded event
		public static const THUMBNAIL_LOADED:String = "thumbnailLoaded";
		// button click event
		public static const BUTTON_CLICK:String = "buttonClick";
		// subbutton click event
		public static const SUBBUTTON_CLICK:String = "subbuttonClick";
		// ready to display event
		public static const READY_TO_DISPLAY:String = "readyToDisplay";
		// thumb clicked event
		public static const THUMB_CLICKED:String = "thumbClicked";
		// image changs event
		public static const IMAGE_CHANGE:String = "imageChange";
		
		public function CustomEvent (type:String, bubbles:Boolean = false, cancelable:Boolean = false) {
			super(type, bubbles, cancelable);
		}
		public override function clone() : Event{
			return new CustomEvent(type, bubbles, cancelable);
		}
		public override function toString():String {
			return formatToString("CustomEvent", "type", "bubbles", "cancelable", "eventPhase");
		}
	}
}