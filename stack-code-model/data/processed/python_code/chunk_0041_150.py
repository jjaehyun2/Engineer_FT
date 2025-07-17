package devoron.data.core.base
{
	import devoron.studio.core.base.IStudioModul;
	import devoron.studio.core.base.StudioEvent;
	import flash.events.Event;
	
	/**
	 * StudioModulEvent
	 * @author Devoron
	 */
	public class DataProcessorDomainEvent extends Event
	{
		private var _source:IDataProcessorDomain;
		public static var NEW_EDITOR_ADDED:String = "new_editor_added";
		public static var NEW_TOOL_ADDED:String = "new_tool_added";
		public static var NEW_PLUGIN_ADDED:String = "new_plugin_added";
		public static var STUDIO_MODUL_ADDED:String = "studio_modul_added";
		public static var STUDIO_MODUL_REMOVED:String = "studio_modul_removed";
		
		public function DataProcessorDomainEvent(source:IStudioModul, type:String, bubbles:Boolean = false, cancelable:Boolean = false)
		{
			super(type, bubbles, cancelable);
			_source = source;
		
		}
		
		public function get source():IStudioModul
		{
			return _source;
		}
	
	}

}