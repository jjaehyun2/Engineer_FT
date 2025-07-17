package com.demy._test.listenerview 
{
	import flash.utils.clearInterval;
	import flash.events.Event;
	import starling.events.Event;
	import flash.utils.setInterval;
	import flash.utils.setTimeout;
	import flash.events.EventDispatcher;
	import starling.events.EventDispatcher;
	/**
	 * ...
	 * @author 
	 */
	public class StarlingAsync extends flash.events.EventDispatcher
	{
		private var intervalId:int;
		
		private var cought:Boolean;
		private var data:Object;
		
		public function StarlingAsync(dispatcher:starling.events.EventDispatcher, eventType:String, timeout:int = 2000, step:int = 100) 
		{
			cought = false;
			
			dispatcher.addEventListener(eventType, catchEvent);
			intervalId = setInterval(checkData, step);
			setTimeout(endListening, timeout);
		}
		
		private function catchEvent(e:starling.events.Event):void 
		{
			cought = true;
			data = e.data;
		}
		
		private function endListening():void 
		{
			clearInterval(intervalId);
			if (!cought) dispatchEvent(new flash.events.Event(flash.events.Event.CANCEL));
		}
		
		private function checkData():void 
		{
			if (cought) dispatchEvent(new flash.events.Event(flash.events.Event.COMPLETE));
		}
		
	}

}