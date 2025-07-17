package org.aswing.event
{
	import flash.display.InteractiveObject;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;
	
	/**
	 * ...
	 * @author DEVORON
	 */
	public class MouseEvent extends Touch
	{
		public var type:String;
		static public const MOUSE_DOWN:String = "mouseDown";
		static public const MOUSE_UP:String = "mouseUp";
		public var localX;
		public var localY;
		public var relatedObject;
		public var ctrlKey;
		public var altKey;
		public var shiftKey;
		public var buttonDown;
		
		public function MouseEvent(type:String, bubbles:Boolean=true, cancelable:Boolean=false, localX:Number=0, localY:Number=0, relatedObject:InteractiveObject=null, ctrlKey:Boolean=false, altKey:Boolean=false, shiftKey:Boolean=false, buttonDown:Boolean=false, delta:int=0)
		{
			super(0);
			this.type = type;
			
			//var new flash.events.MouseEvent(
		}
		
		private function onTouch(e:TouchEvent):void
		{
			//var touch:Touch = e.getTouch(stage);
			var touch:Touch = e.getTouch(null);
			if (touch)
			{
				if (touch.phase == TouchPhase.BEGAN)
				{
					//There was a touch (MouseDown)
				}
				
				else if (touch.phase == TouchPhase.ENDED)
				{
					//The Touch ended (MouseUp)
				}
				
				else if (touch.phase == TouchPhase.MOVED)
				{
					//dragging
				}
			}
		
		}
	
	}

}