package com.illuzor.thegame {
	
	import com.illuzor.thegame.events.LibEvent;
	import com.illuzor.thegame.tools.LibLoader;
	import flash.display.Sprite;
	import flash.events.Event;
	import com.illuzor.thegame.tools.Assets;
	
	/**
	 * ...
	 * @author illuzor // illuzor.com // illuzor@gmail.com
	 * 
	 * Puzzle-platformer game with level editor
	 * 
	 * Developed with FlashDevelop 4.0.3 and Flex SDK 4.6/AIR SDK 3.3 
	 * for FlashPlayer 10.3(game) and AIR 3.3(level editor)
	 * - http://www.flashdevelop.org/ 
	 * - http://sourceforge.net/adobe/flexsdk/wiki/Downloads/ 
	 * - http://www.adobe.com/devnet/air/air-sdk-download.html
	 * 
	 * Used libraries:
	 *  - flashpunk game engine — http://flashpunk.net/
	 *  - blooddy_crypto — http://www.blooddy.by/ru/crypto/
	 *  - as3crypto — http://code.google.com/p/as3crypto/
	 *  - minimalcomps — http://www.minimalcomps.com/
	 */
	
	public class Main extends Sprite {
		
		public function Main():void {
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			var loader:LibLoader = new LibLoader();
			loader.addEventListener(LibEvent.LIB_LOADED, start);
		}
		
		private function start(e:LibEvent):void {
			addChild(new Game());
		}
		
	}
}