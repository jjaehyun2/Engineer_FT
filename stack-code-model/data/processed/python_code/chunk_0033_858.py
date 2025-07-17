package controls.MediaPresentation.events {
	import flash.events.Event;
	import flash.geom.Point;
	
	public class ModifyCenterHotSpotCoordEvent extends Event {
		public function ModifyCenterHotSpotCoordEvent(type:String, pt:Point, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			this.pt = pt;
		}
		
		public var pt:Point;
		
		public static const TYPE_MOFIDY_CENTER_HOTSPOT:String = "modifyCenterHotSpot";
		
		override public function clone():Event {
			return new ModifyCenterHotSpotCoordEvent(type,this.pt);
		}
	}
}