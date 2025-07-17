package devoron.data.core.base 
{
	import flash.system.ApplicationDomain;
	
	/**
	 * IDataProcessorDomain
	 * @author Devoron
	 */
	public interface IDataProcessorDomain 
	{
		function removeDataLinks(uids:Array, targets:Vector.<IDataProcessor> = null):void;
		
		function setApplicationDomain(domain:ApplicationDomain):void;
		function registerDataProcessor(processor:IDataProcessor):void;
		function unregisterDataProcesor(processor:IDataProcessor):void;
		
		function getDataProcessor(uid:String):IDataProcessor;
		function getDataProcessorByType(type:String):IDataProcessor;
		
		function setParentDataProcessorDomain(domain:IDataProcessorDomain):void;
		function getParentDataProcessorDomain():IDataProcessorDomain;
		function registerDataProcessors(processors:Vector.<Class>):void;
		function unregisterDataProcessors(processors:Vector.<Class>):void;
		
	}
	
}