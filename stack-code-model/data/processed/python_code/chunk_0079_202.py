package starling.events {
	import starling.events.Event;
	
	public interface IEventDispatcher {
		function addEventListener(type : String, listener : Function) : void;
		function dispatchEvent(event : Event) : void;
		function dispatchEventWith(type : String, bubbles : Boolean = false, data : Object = null) : void;
		function hasEventListener(type : String, listener:Function=null) : Boolean;
		function removeEventListener(type : String, listener : Function) : void;
		function removeEventListeners(type : String = null) : void;
	}
}