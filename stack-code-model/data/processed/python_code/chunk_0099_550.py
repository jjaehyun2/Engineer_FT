package com.lowoui_as.events
{
	import com.lowoui_as.interfaces.IDragSlot;
	import flash.display.Sprite;
	import flash.events.Event;
	
	public class DragEvent extends Event
	{
		public static const DROP:String = "drop";
		public static const DRAG_START:String = "dragStart";
		public static const DRAG_END:String = "dragEnd";
		public var dragData:Object;
		public var dragTarget:IDragSlot;
		public var dropTarget:IDragSlot;
		public var dragSprite:Sprite;

		public function DragEvent(type:String, data:Object, drag:IDragSlot, drop:IDragSlot, sprite:Sprite, bubbles:Boolean = true, cancelable:Boolean = true)
		{
			dragData = data;
			dragTarget = drag;
			dropTarget = drop;
			dragSprite = sprite;
			super(type, bubbles, cancelable);
		}
	}
}