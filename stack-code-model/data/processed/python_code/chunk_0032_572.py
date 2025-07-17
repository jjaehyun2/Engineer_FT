package com.controls
{
	import flash.events.FocusEvent;
	import spark.components.Scroller;
	
	/**
	 * Scroller with check of focusManager control
	 * @author adolgopolova
	 */
	public class ScrollerWithFocusManagerCheck extends Scroller
	{
		/**
		 * Constructor
		 */
		public function ScrollerWithFocusManagerCheck()
		{
			super();
		}

		/**
		 * Overrides Scroller's focusInHandler
		 * checks wether focusManager is null
		 * @param event - FocusEvent
		 */		
		override protected function focusInHandler(event:FocusEvent):void
		{
			if (focusManager != null)
			{
				super.focusInHandler(event);
			}
		}
	}
}