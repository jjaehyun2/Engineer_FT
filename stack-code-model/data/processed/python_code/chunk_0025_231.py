package com.illuzor.otherside.screens {
	
	import com.illuzor.otherside.constants.AtlasType;
	import com.illuzor.otherside.constants.ScreenType;
	import com.illuzor.otherside.controllers.resource.ResourceManager;
	import com.illuzor.otherside.debug.log;
	import com.illuzor.otherside.events.ScreenEvent;
	import com.illuzor.otherside.graphics.ui.TextButton;
	import com.illuzor.otherside.Settings;
	import starling.display.Button;
	import starling.display.Sprite;
	import starling.events.Event;
	import starling.textures.Texture;
	import starling.textures.TextureAtlas;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public final class MainMenu extends ScreenBase {
		
		private var playButton:TextButton;
		
		override protected function init():void {
			var atlas:TextureAtlas = ResourceManager.controller.getAtlas(AtlasType.MENU_ATLAS);
			var buttonTexture:Texture = atlas.getTexture("button_bg");
			
			var buttonsContainer:Sprite = new Sprite();
			addChild(buttonsContainer);
			playButton = new TextButton(buttonTexture, Settings.langConfig.data.play);
			buttonsContainer.addChild(playButton);
			
			buttonsContainer.width = stageWidth / 3;
			buttonsContainer.scaleY = buttonsContainer.scaleX;
			buttonsContainer.x = stageWidth >> 1;
			buttonsContainer.y = stageHeight >> 1;
			
			dispatchReady();
		}
		
		override public function start():void {
			playButton.addEventListener(Event.TRIGGERED, onButtonClick);
		}
		
		private function onButtonClick(e:Event):void {
			switch (e.target) {
				case playButton:
					dispatchEvent(new ScreenEvent(ScreenEvent.CHANGE_SCREEN, ScreenType.GAME_SCREEN));
				break;
			}
		}
		
		override public function pause():void {
			
		}
		
		override public function resume():void {
			
		}
		
		override public function back():void {
			log("mm back")
		}
		
		override protected function clear():void {
			
		}
		
	}
}