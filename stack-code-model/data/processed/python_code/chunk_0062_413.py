package controls.MediaPresentation.events {
	import flash.events.Event;
	import flash.geom.Point;
	
	public class ModifyLowerLeftLeftHotSpotCoordEvent extends Event {
		public function ModifyLowerLeftLeftHotSpotCoordEvent(type:String, pt:Point, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			this.pt = pt;
		}
		
		public var pt:Point;
		
		public static const TYPE_MOFIDY_LOWER_LEFT_LEFT_HOTSPOT:String = "modifyLowerLeftLeftHotSpot";
		
		override public function clone():Event {
			return new ModifyLowerLeftLeftHotSpotCoordEvent(type,this.pt);
		}
	}
}