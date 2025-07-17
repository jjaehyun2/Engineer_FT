package  as3lib.helper.evt
{
	import flash.events.Event;
	import flash.events.IEventDispatcher;
	
	public class VisualDispatcher implements IEventDispatcher
	{
		protected var typeListeners:Object = [];
		public function VisualDispatcher()
		{
		}
		public function toExtend(dispatcher:IEventDispatcher):void
		{
			for each(var listener:Array in typeListeners)
			{
				dispatcher.addEventListener.apply(null,listener);
			}
			typeListeners = null;
		}
			
		public function addEventListener(type:String, listener:Function, useCapture:Boolean=false, priority:int=0, useWeakReference:Boolean=false):void
		{
			typeListeners.push([type,listener,useCapture,priority,useWeakReference]);
		}
		
		public function removeEventListener(type:String, listener:Function, useCapture:Boolean=false):void
		{
		}
		
		public function dispatchEvent(event:Event):Boolean
		{
			return false;
		}
		
		public function hasEventListener(type:String):Boolean
		{
			return false;
		}
		
		public function willTrigger(type:String):Boolean
		{
			return false;
		}
	}
}