package com.illuzor.otherside.editor.screen.components {
	
	import com.bit101.components.Label;
	import com.illuzor.framework.display.FastRect;
	import flash.display.Sprite;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class ComponentBase extends Sprite {
		
		protected var label:Label;
		protected var eventType:uint;
		
		public function ComponentBase(eventType:uint, w:uint, text:String) {
			this.eventType = eventType;
			var background:FastRect = new FastRect(w, 20, 0xFFFFFF, .8);
			addChild(background);
			label = new Label(this, 4, 0,  text.concat(":"));
		}
		
		public function dispose():void {
			throw new Error("ComponentBase.dispose() function must be overrided");
		}
		
	}
}