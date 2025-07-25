package com.gestureworks.cml.components 
{
	import com.gestureworks.cml.elements.*;
	import com.gestureworks.cml.events.*;
	import com.gestureworks.events.GWTouchEvent;
	import flash.display.DisplayObject;
		
	/**
	 * The MP3Player component is primarily meant to display an MP3 element and its associated meta-data.
	 * 
	 * <p>It is composed of the following: 
	 * <ul>
	 * 	<li>mp3</li>
	 * 	<li>front</li>
	 * 	<li>back</li>
	 * 	<li>menu</li>
	 * 	<li>frame</li>
	 * 	<li>background</li>
	 * </ul></p>
	 * 
	 * <p>The width and height of the component are automatically set to the dimensions of the MP3 element unless it is 
	 * previously specifed by the component.</p>
	 * 
	 * <codeblock xml:space="preserve" class="+ topic/pre pr-d/codeblock ">
	  

			
	 * </codeblock>
	 * 
	 * @author Ideum
	 * @see Component
	 * @see com.gestureworks.cml.elements.MP3
	 * @see com.gestureworks.cml.elements.TouchContainer
	 */	 	
	public class MP3Player extends Component 
	{		
		/**
		 * Constructor
		 */
		public function MP3Player() 
		{
			super();			
		}
		
		
		///////////////////////////////////////////////////////////////////////
		// Public Properties
		//////////////////////////////////////////////////////////////////////
		
		private var _mp3:*;
		/**
		 * Sets the mp3 element.
		 * This can be set using a simple CSS selector (id or class) or directly to a display object.
		 * Regardless of how this set, a corresponding display object is always returned. 
		 */		
		public function get mp3():* {return _mp3}
		public function set mp3(value:*):void 
		{
			if (!value) return;
			
			if (value is DisplayObject)
				_mp3 = value;
			else 
				_mp3 = searchChildren(value);					
		}				
		
		/**
		 * Initialization function
		 */
		override public function init():void 
		{			
			// automatically try to find elements based on AS3 class
			if (!mp3)
				mp3 = searchChildren(MP3);
			
			if (mp3) {
				mp3.addEventListener(StateEvent.CHANGE, onStateEvent);
			}
			super.init();
		}		
		
		override protected function updateLayout(event:*=null):void 
		{
			// update width and height to the size of the mp3, if not already specified
			if (!width && mp3)
				width = mp3.width;
			if (!height && mp3)
				height = mp3.height;
				
			super.updateLayout();
		}	
		
		override protected function onStateEvent(event:StateEvent):void
		{				
			super.onStateEvent(event);
			if (event.value == "close" && mp3)
				mp3.stop();
			else if (event.value == "play" && mp3)
				mp3.resume();
			else if (event.value == "pause" && mp3)
				mp3.pause();
			else if (event.property == "position" && mp3) {
				if (menu) {
					if (menu.slider) {
						Slider(menu.slider).input(event.value * 100);
					}
				}
			}
			else if (menu.slider && event.target is Slider) {
				mp3.pause();
				mp3.seek(event.value);
				addEventListener(GWTouchEvent.TOUCH_END, onRelease);
			}
		}	
		
		private function onRelease(e:*):void {
			removeEventListener(GWTouchEvent.TOUCH_END, onRelease);
			mp3.resume();
		}
		
		/**
		 * @inheritDoc
		 */
		override public function dispose():void 
		{
			super.dispose();	
			_mp3 = null;
		}
		
	}
}