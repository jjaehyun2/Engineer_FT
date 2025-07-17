package com.illuzor.engine3d {
	
	import com.illuzor.engine3d.net.DataLoader;
	import com.illuzor.engine3d.notifications.NotificationManager;
	import com.illuzor.engine3d.tools.ModelRotator;
	import com.illuzor.engine3d.tools.Parser;
	import com.illuzor.engine3d.ui.screens.ScreenManager;
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;

	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	[Frame(factoryClass="com.illuzor.engine3d.Preloader")]
	
	public class Main extends Sprite {
		
		static public var data:Object;
		
		private const XML_PATH:String = "_settings.xml";
		
		public function Main():void {
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}

		private function init(e:Event = null):void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			
			stage.scaleMode = StageScaleMode.NO_SCALE;
			stage.align = StageAlign.TOP_LEFT;
			
			ModelRotator.init(stage);
			NotificationManager.addWaitingMessage("loading settings...");
			DataLoader.loadXML(XML_PATH, getXML);
			
		}
		
		private function getXML(xml:XML):void {
			NotificationManager.removeWaitingMessage();
			data = Parser.parseXML(xml);
			
			var screenMangaer:ScreenManager = new ScreenManager();
			addChild(screenMangaer);
		}
	
	}
}