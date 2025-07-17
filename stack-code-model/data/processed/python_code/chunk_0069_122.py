package Events
{
	import flash.events.Event;
	
	public class MotionEvent extends Event
	{
		public static const UP_PRESSED:String = "up_pressed";
		public static const LEFT_PRESSED:String = "left_pressed";
		public static const DOWN_PRESSED:String = "down_pressed";
		public static const RIGHT_PRESSED:String = "right_pressed";
		public static const ATTACK_PRESSED:String = "attack_pressed";
		public var params:Object;
		
		public function MotionEvent(type:String,params:Object,bubbles:Boolean = false,cancelable:Boolean = false) 
		{
			
			super(type, bubbles, cancelable);
			this.params = params;
		}
		public override function clone():Event
		{
			return new MotionEvent(type, this.params, bubbles, cancelable);
		}
		public override function toString():String
		{
			return formatToString("CustomEvent", "params", "type", "bubbles", "cancelable");
		}
		
	}
}