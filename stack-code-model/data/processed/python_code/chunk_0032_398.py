package com.illuzor.circles {
	
	import com.illuzor.circles.tools.AudioManager;
	import com.illuzor.circles.tools.KeyboardManager;
	import com.illuzor.circles.tools.MessageTool;
	import com.illuzor.circles.tools.ResizeManager;
	import com.illuzor.circles.tools.StorageManager;
	import com.illuzor.circles.tools.VibroManager;
	import flash.desktop.NativeApplication;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.geom.Rectangle;
	import flash.utils.setTimeout;
	import starling.core.Starling;
	import starling.events.Event;
	
	/**
	 * C:\Users\Artem\AppData\Roaming\com.illuzor.circles\Local Store
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class Main extends Sprite {
		
		private var starling:Starling;
		
		public function Main():void {
			addEventListener(flash.events.Event.ADDED_TO_STAGE, onAdded);
		}

		private function onAdded(e:flash.events.Event):void {
			removeEventListener(flash.events.Event.ADDED_TO_STAGE, onAdded);
			setTimeout(start, 1200);
		}
		
		private function start():void {
			StorageManager.init();
			KeyboardManager.init(stage);
			ResizeManager.init(stage);
			Settings.dispatcher = this;
			VibroManager.init();
			
			starling = new Starling(Game, stage, new Rectangle(0, 0, stage.stageWidth, stage.stageHeight));
			starling.antiAliasing = 8;
			starling.start();
			starling.addEventListener(starling.events.Event.FATAL_ERROR, onStarlingEvent);
			//starling.showStats = true;
			
			NativeApplication.nativeApplication.addEventListener(flash.events.Event.ACTIVATE, onNativeEvent);
			NativeApplication.nativeApplication.addEventListener(flash.events.Event.DEACTIVATE, onNativeEvent);
			NativeApplication.nativeApplication.addEventListener(flash.events.Event.SUSPEND, onNativeEvent);
		}
		
		private function onNativeEvent(e:flash.events.Event):void {
			switch (e.type) {
				case flash.events.Event.ACTIVATE:
					if (StorageManager.getBool("sound"))
						AudioManager.playMusic();
					starling.start();
				break;
				case flash.events.Event.DEACTIVATE:
					starling.stop();
					AudioManager.stopAll();
				break;
				case flash.events.Event.SUSPEND:
					NativeApplication.nativeApplication.exit();
				break;
			}
		}
		
		private function onStarlingEvent(e:starling.events.Event):void {
			starling.dispose();
			MessageTool.showMessage(stage, "Fatal Error");
		}
		
	}
}