package devoron.data.core.base
{
	import flash.events.Event;
	import flash.events.IEventDispatcher;
	import flash.system.ApplicationDomain;
	import org.aswing.util.HashMap;
	
	/**
	 * DataProcessorDomain
	 * @author Devoron
	 */
	public class DataProcessorDomain implements IDataProcessorDomain, IEventDispatcher
	{
		private var processorsHash:HashMap;
		private var dataHash:HashMap;
		
		public function DataProcessorDomain()
		{
		
		}
		
		/* INTERFACE devoron.data.core.base.IDataProcessorDomain */
		
		public function registerDataProcesor(processor:IDataProcessor):void
		{
			processorsHash = new HashMap();
			processorsHash.put(processor.getUID(), processor);
			processor.addEventListener(DataProccessorEvent.DATA_CHANGE, onDataProcessorDataChange);
		}
		
		private function onDataProcessorDataChange(e:DataProccessorEvent):void 
		{
			dispatchEvent(e);
		}
		
		public function unregisterDataProcesor(processor:IDataProcessor):void
		{
			var processor:IDataProcessor = processorsHash.get(processor.getUID());
			processor.addEventListener(DataProc
		}
		
		public function setParentDataProcessorDomain(domain:IDataProcessorDomain):void
		{
		
		}
		
		public function getParentDataProcessorDomain():IDataProcessorDomain
		{
		
		}
		
		public function registerDataProcessors(processors:Vector.<Class>):void
		{
		
		}
		
		public function unregisterDataProcessors(processors:Vector.<Class>):void
		{
		
		}
		
		/* INTERFACE flash.events.IEventDispatcher */
		
		public function addEventListener(type:String, listener:Function, useCapture:Boolean = false, priority:int = 0, useWeakReference:Boolean = false):void
		{
		
		}
		
		public function removeEventListener(type:String, listener:Function, useCapture:Boolean = false):void
		{
		
		}
		
		public function dispatchEvent(event:Event):Boolean
		{
		
		}
		
		public function hasEventListener(type:String):Boolean
		{
		
		}
		
		public function willTrigger(type:String):Boolean
		{
		
		}
		
		public function setApplicationDomain(domain:ApplicationDomain):void
		{
		
		}
	
	}

}