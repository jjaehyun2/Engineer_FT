package controls.MediaPresentation.events {
	import flash.events.Event;
	import flash.geom.Point;
	
	public class ChangeActionBarTitle extends Event {
		public function ChangeActionBarTitle(type:String, title:String, delay:int, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			this.title = title;
			this.delay = delay;
		}
		
		public var title:String;
		public var delay:int;
		
		public static const TYPE_CHANGE_ACTIONBAR_TITLE:String = "ChangeActionBarTitle";
		
		override public function clone():Event {
			return new ChangeActionBarTitle(type,title,delay);
		}
	}
}