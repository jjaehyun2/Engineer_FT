package com.illuzor.otherside.graphics.screens {
	
	import com.illuzor.otherside.errors.ScreenError;
	import com.illuzor.otherside.events.ScreenEvent;
	import com.illuzor.otherside.tools.ResizeManager;
	import starling.display.Sprite;
	import starling.events.Event;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class ScreenBase extends Sprite {
		
		protected var stageWidth:uint;
		protected var stageHeight:uint;
		
		public function ScreenBase() {
			ResizeManager.addResize(resize);
			addEventListener(Event.ADDED_TO_STAGE, onAdded);
		}
		
		private function onAdded(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, onAdded);
			start();
		}
		
		protected function start():void {
			throw new ScreenError("start() function must be overrided");
		}
		
		protected function errorOccured():void {
			dispatchEvent(new ScreenEvent(ScreenEvent.ERROR));
		}
		
		private function resize(stageWidth:uint, stageHeight:uint):void{
			this.stageWidth = stageWidth;
			this.stageHeight = stageHeight;
		}
		
		override public function dispose():void {
			ResizeManager.removeResize(resize);
			super.dispose();
		}
		
	}
}