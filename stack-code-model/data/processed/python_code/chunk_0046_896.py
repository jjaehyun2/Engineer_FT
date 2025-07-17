package masputih.isometric.pathfinding {
	import flash.events.Event;
	
	/**
	 *
	 * 
	 */
	public class AStarEvent extends Event {
		
		public static const SEARCH:String = "search";
		public static const COMPLETE:String = "complete";
		public static const NO_PATH:String = "noPath";
		
		public var path:Array;
		
		public function AStarEvent(type:String,path:Array = null) { 
			super(type, true);
			this.path = path;
		} 
		
		override public function clone():Event { 
			return new AStarEvent(type);
		} 
		
		override public function toString():String { 
			return formatToString("AStarEvent", "type", "bubbles", "cancelable", "eventPhase"); 
		}
		
	}
	
}