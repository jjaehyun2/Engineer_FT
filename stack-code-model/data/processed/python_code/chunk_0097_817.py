package controls.MediaPresentation.events {
	import flash.events.Event;
	import flash.geom.Point;
	
	public class ModifyLowerLeftHotSpotCoordEvent extends Event {
		public function ModifyLowerLeftHotSpotCoordEvent(type:String, pt:Point, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			this.pt = pt;
		}
		
		public var pt:Point;
		
		public static const TYPE_MOFIDY_LOWER_LEFT_HOTSPOT:String = "modifyLowerLeftHotSpot";
		
		override public function clone():Event {
			return new ModifyLowerLeftHotSpotCoordEvent(type,this.pt);
		}
	}
}