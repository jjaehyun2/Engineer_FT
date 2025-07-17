package controls.MediaPresentation.events {
	import flash.events.Event;
	import flash.geom.Point;
	
	public class ModifyLowerRightRightHotSpotCoordEvent extends Event {
		public function ModifyLowerRightRightHotSpotCoordEvent(type:String, pt:Point, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			this.pt = pt;
		}
		
		public var pt:Point;
		
		public static const TYPE_MOFIDY_LOWER_RIGHT_RIGHT_HOTSPOT:String = "modifyLowerRightRightHotSpot";
		
		override public function clone():Event {
			return new ModifyLowerRightRightHotSpotCoordEvent(type,this.pt);
		}
	}
}