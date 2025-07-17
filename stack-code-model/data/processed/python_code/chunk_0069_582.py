package devoron.data.core.base
{
	import flash.events.Event;
	
	/**
	 * StudioEvent
	 * @author Devoron
	 */
	public class DataStructurEvent extends Event
	{
		//public static var DATA_STRUCTUR_OBJECT_CHANGED:String = "change_file_manager";
		
		
		public static var DATA_STRUCTUR_OBJECT_CHANGED:String = "change_file_manager";
		public static var DATA_STRUCTUR_OBJECT_ADDED:String = "change_file_manager";
		public static var DATA_STRUCTUR_OBJECT_REMOVED:String = "change_file_manager";
		public static var LEVELS_DATA_READY:String = "levels_data_ready";
		public static var CHANGE_GAME_EDITOR_MODUL:String = "change_game_editor_modul";
		
		public static var STAGE_ACCESS_ON:String = "stage_access_on";
		public static var STAGE_ACCESS_OFF:String = "stage_access_off";
		static public const DATA_STRUCTUR_CREATED:String = "data_structur_created";
		
		private var _data:Object;
		
		public function DataStructurEvent(data:Object, type:String, bubbles:Boolean = false, cancelable:Boolean = false)
		{
			super(type, bubbles, cancelable);
			_data = data;
		}
		
		public function get data():Object
		{
			return _data;
		}
	
	}

}