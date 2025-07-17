/*
   Copyright aswing.org, see the LICENCE.txt.
 */

package devoron.components.filechooser.contentviews
{
	
	import flash.events.Event;
	import flash.events.MouseEvent;
	
	/**
	 * The event for items of List.
	 * @author iiley
	 */
	public class FIContentViewEvent extends Event
	{
		
		public static const ITEM_CLICK:String = "itemClick";
		public static const ITEM_DOUBLE_CLICK:String = "itemDoubleClick";
		public static const ITEM_MOUSE_DOWN:String = "itemMouseDown";
		public static const ITEM_ROLL_OVER:String = "itemRollOver";
		public static const ITEM_ROLL_OUT:String = "itemRollOut";
		public static const ITEM_RELEASE_OUT_SIDE:String = "itemReleaseOutSide";
		
		private var value:*;
		private var mouseEvent:MouseEvent;
		
		/**
		 * @param type
		 * @param value
		 * @param cell
		 * @param e the original mouse event
		 */
		public function FIContentViewEvent(type:String, value:*, mouseEvent:MouseEvent)
		{
			super(type, false, false);
			this.mouseEvent = mouseEvent;
			this.value = value;
		}
		
		public function getValue():*
		{
			return value;
		}
		
		override public function clone():Event
		{
			return new FIContentViewEvent(type, value, mouseEvent.clone() as MouseEvent);
		}
	}
}