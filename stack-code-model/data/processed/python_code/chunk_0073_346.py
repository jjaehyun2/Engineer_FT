package controls.MediaPresentation.events {
	import flash.events.Event;
	import flash.geom.Point;
	
	public class ChangeActionBar extends Event {
		public function ChangeActionBar(type:String, _is_:Boolean, _always_:Boolean=false, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			this._is_ = _is_;
			this._always_ = _always_;
		}
		
		public var _is_:Boolean;
		public var _always_:Boolean;
		
		public static const TYPE_CHANGE_ACTIONBAR:String = "changeActionBar";
		
		override public function clone():Event {
			return new ChangeActionBar(type,_is_,_always_);
		}
	}
}