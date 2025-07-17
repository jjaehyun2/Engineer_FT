package controls.MediaPresentation.events {
	import flash.events.Event;
	import flash.geom.Point;
	
	public class ModifyLowerLeftRightHotSpotCoordEvent extends Event {
		public function ModifyLowerLeftRightHotSpotCoordEvent(type:String, pt:Point, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			this.pt = pt;
		}
		
		public var pt:Point;
		
		public static const TYPE_MOFIDY_LOWER_LEFT_RIGHT_HOTSPOT:String = "modifyLowerLeftRightHotSpot";
		
		override public function clone():Event {
			return new ModifyLowerLeftRightHotSpotCoordEvent(type,this.pt);
		}
	}
}