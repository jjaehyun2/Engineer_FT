package com.illuzor.otherside.screens {
	
	import com.illuzor.otherside.controllers.ResizeManager;
	import com.illuzor.otherside.errors.ScreenError;
	import com.illuzor.otherside.events.ScreenEvent;
	import starling.display.Sprite;
	import starling.events.Event;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class ScreenBase extends Sprite {
		
		private var _stageWidth:uint;
		private var _stageHeight:uint;
		
		public function ScreenBase() {
			_stageWidth = ResizeManager.stageWidth;
			_stageHeight = ResizeManager.stageHeight;
			addEventListener(Event.ADDED_TO_STAGE, onAdded);
		}
		
		private function onAdded(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, onAdded);
			addEventListener(Event.REMOVED_FROM_STAGE, onRemoved);
			init();
		}
		
		protected function init():void {
			throw new ScreenError("ScreenBase, protected method init() must be overrided");
		}
		
		public function start():void {
			throw new ScreenError("ScreenBase, public method start() methond must be overrided");
		}
		
		public function pause():void {
			throw new ScreenError("ScreenBase, public method pause() methond must be overrided");
		}
		
		public function resume():void {
			throw new ScreenError("ScreenBase, public method resume() methond must be overrided");
		}
		
		public function back():void {
			throw new ScreenError("ScreenBase, public method back() methond must be overrided");
		}
		
		protected function clear():void {
			throw new ScreenError("ScreenBase, public method clear() methond must be overrided");
		}
		
		protected function dispatchReady():void {
			dispatchEvent(new ScreenEvent(ScreenEvent.SCREEN_READY));
		}
		
		private function onRemoved(e:Event):void {
			removeEventListener(Event.REMOVED_FROM_STAGE, onRemoved);
			clear();
		}
		
		public function get stageWidth():uint {
			return _stageWidth;
		}
		
		public function get stageHeight():uint {
			return _stageHeight;
		}
		
	}
}