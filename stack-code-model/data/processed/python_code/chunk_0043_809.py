package flash.events
{
	import flash.display.*;
	
	public class MouseEvent extends Event
	{
		public static const MOUSE_WHEEL:String = "mouseWheel";
		public static const MOUSE_MOVE:String = "mouseMove";
		public static const ROLL_OUT:String = "rollOut";
		public static const MOUSE_OVER:String = "mouseOver";
		public static const CLICK:String = "click";
		public static const MOUSE_OUT:String = "mouseOut";
		public static const MOUSE_UP:String = "mouseUp";
		public static const DOUBLE_CLICK:String = "doubleClick";
		public static const MOUSE_DOWN:String = "mouseDown";
		public static const ROLL_OVER:String = "rollOver";
		
		public function get stageY():Number
		{
		}
		
		public function get stageX():Number
		{
		}
		
		public function get delta():int
		{
		}
		
		public function set delta(value:int):void
		{
		}
		
		public function get relatedObject():InteractiveObject
		{
		}
		
		public function set relatedObject(value:InteractiveObject):void
		{
		}
		
		public function get localX():Number
		{
		}
		
		public function set localX(value:Number):void
		{
		}
		
		public function get localY():Number
		{
		}
		
		public function set localY(value:Number):void
		{
		}
		
		public function get buttonDown():Boolean
		{
		}
		
		public function set buttonDown(value:Boolean):void
		{
		}
		
		public function get altKey():Boolean
		{
		}
		
		public function set altKey(value:Boolean):void
		{
		}
		
		public function get ctrlKey():Boolean
		{
		}
		
		public function set ctrlKey(value:Boolean):void
		{
		}
		
		public function get shiftKey():Boolean
		{
		}
		
		public function set shiftKey(value:Boolean):void
		{
		}
		
		public function MouseEvent(type:String, bubbles:Boolean = true, cancelable:Boolean = false, localX:Number = 0, localY:Number = 0, relatedObject:InteractiveObject = null, ctrlKey:Boolean = false, altKey:Boolean = false, shiftKey:Boolean = false, buttonDown:Boolean = false, delta:int = 0)
		{
		}
		
		override public function clone():Event
		{
		}
		
		override public function toString():String
		{
		}
		
		public function updateAfterEvent():void
		{
		}
		
	}
}