package com.illuzor.spinner.screens.subscreens {
	
	import com.greensock.TweenLite;
	import com.illuzor.spinner.screens.ScreenBase;
	import starling.display.Quad;
	import starling.display.Sprite;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class SubscreenBase extends ScreenBase {
		
		private var container:Sprite;
		protected var hideble:Boolean = false;
		
		override protected function start():void {
			container = new Sprite();
			addChild(container);
			var quad:Quad = new Quad(stageWidth, stageHeight, 0x0);
			container.addChild(quad);
			container.alpha = 0;
			TweenLite.to(container, .65, { alpha:.7 } );
			
			if(hideble)
				container.addEventListener(TouchEvent.TOUCH, onContainerTouch);
		}
		
		private function onContainerTouch(e:TouchEvent):void {
			var touch:Touch = e.getTouch(container, TouchPhase.BEGAN);
			if (touch) {
				container.removeEventListener(TouchEvent.TOUCH, onContainerTouch);
				hide();
			}
		}
		
		override public function hide():void {
			super.hide();
			if(!_progress){
				_progress = true;
				TweenLite.to(container, .4, { alpha:0, onComplete:dispatchHided } );
			}
		}
		
		override public function dispose():void {
			container.removeEventListener(TouchEvent.TOUCH, onContainerTouch);
			TweenLite.killTweensOf(container);
			container.dispose();
			super.dispose();
		}
		
	}
}