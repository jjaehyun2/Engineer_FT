package com.illuzor.airlab {
	
	import com.illuzor.airlab.screens.mainScreens.MainScreen;
	import flash.desktop.NativeApplication;
	import flash.events.Event;
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.geom.Rectangle;
	import flash.ui.Multitouch;
	import flash.ui.MultitouchInputMode;
	import starling.core.Starling;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	public class Main extends Sprite {
		private var starling:Starling;
		
		public function Main():void {
			stage.scaleMode = StageScaleMode.NO_SCALE;
			stage.align = StageAlign.TOP_LEFT;
			Multitouch.inputMode = MultitouchInputMode.TOUCH_POINT;
			//stage.addEventListener(Event.DEACTIVATE, deactivate);
			
			starling = new Starling(MainScreen, stage);
			starling.start();
			
			stage.addEventListener(Event.RESIZE, onResize);
		}
		
		private function onResize(e:Event):void {
			starling.viewPort = new Rectangle(0, 0, stage.stageWidth, stage.stageHeight);
		}
		
		/*private function deactivate(e:Event):void {
			// auto-close
			NativeApplication.nativeApplication.exit();
		}*/
		
	}
	
}