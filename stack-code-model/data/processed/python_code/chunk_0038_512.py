package com.illuzor.otherside.interfaces {
	
	import starling.events.Event;
	
	/**
	 * Handmade interface for starling EventDispatcher
	 * 
	 * @author illuzor  //  illuzor.com
	 */
	
	public interface IEventDispatcher {
		function addEventListener(type:String, listener:Function):void;
		function removeEventListener(type:String, listener:Function):void;
		function removeEventListeners(type:String = null):void;
		function dispatchEvent(event:Event):void;
		function dispatchEventWith(type:String, bubbles:Boolean = false, data:Object = null):void;
		function hasEventListener(type:String):Boolean;
	}
	
}