package com.thedevstop.asbus 
{
	import com.codecatalyst.promise.Promise;
	import flash.events.Event;
	
	public interface IMediator
	{
		/**
		 * Sends the command to be acted upon.
		 */
		function send(command:Command):void
		
		/**
		 * Requests a result for the query.
		 * @return	The promise of a result.
		 */
		function request(query:Query):Promise
		
		/**
		 * Adds a listener for a type of event.
		 */
		function addEventListener(type:String, listener:Function, useCapture:Boolean = false, priority:int = 0, useWeakReference:Boolean = false):void;
		
		/**
		 * Dispatch an event to the listeners.
		 */
		function dispatchEvent(event:Event):Boolean;
		
		/**
		 * Remove a listener for a type of event.
		 */
		function removeEventListener(type:String, listener:Function, useCapture:Boolean=false):void;
	}
}