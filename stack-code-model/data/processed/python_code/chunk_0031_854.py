package com.illuzor.spinner.screens {
	
	import com.illuzor.spinner.constants.ScreenType;
	import com.illuzor.spinner.controllers.AppController;
	import com.illuzor.spinner.events.ScreenEvent;
	import starling.display.Button;
	import starling.events.Event;
	import starling.textures.TextureAtlas;

	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class MainMenu extends ScreenBase {
		private var playButton:Button;
		
		override protected function start():void {
			var atlas:TextureAtlas = AppController.assetManager.getTextureAtlas("atlas1");
			playButton = new Button(atlas.getTexture("btn_play"));
			addChild(playButton);
			playButton.width = playButton.height = stageWidth * .26;
			playButton.x = (stageWidth - playButton.width) >> 1;
			playButton.y = (stageHeight - playButton.height) >> 1;
			
			playButton.addEventListener(Event.TRIGGERED, onButtonClick);
		}
		
		private function onButtonClick(e:Event):void {
			dispatchEvent(new ScreenEvent(ScreenEvent.CHANGE_SCREEN, ScreenType.SHAPE_SELECTION_MENU ));
		}
		
		override public function hide():void {
			super.hide();
		}
		
		override public function dispose():void {
			playButton.removeEventListener(Event.TRIGGERED, onButtonClick);
			playButton.dispose();
			super.dispose();
		}
		
	}
}