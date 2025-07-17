package com.illuzor.spinner.screens.subscreens {
	
	import com.illuzor.spinner.constants.HideActionType;
	import com.illuzor.spinner.controllers.AppController;
	import com.illuzor.spinner.screens.subscreens.SubscreenBase;
	import starling.display.Button;
	import starling.display.Sprite;
	import starling.events.Event;
	import starling.textures.TextureAtlas;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class ReplayScreen extends SubscreenBase {
		
		private var replayButton:Button;
		
		override protected function start():void {
			super.start();
			var container:Sprite = new Sprite();
			addChild(container);
			
			var atlas:TextureAtlas = AppController.assetManager.getTextureAtlas("atlas1");
			replayButton = new Button(atlas.getTexture("btn_replay"));
			
			container.addChild(replayButton);
			
			container.width = stageWidth * .2;
			container.scaleY = container.scaleX;
			container.x = (stageWidth - container.width) >> 1;
			container.y = (stageHeight - container.height) >> 1;
			
			replayButton.addEventListener(Event.TRIGGERED, onButtonClick);
		}
		
		private function onButtonClick(e:Event):void {
			switch (e.target) {
				case replayButton:
					hide();
				break;
			}
		}
		
		override public function hide():void {
			super.hide();
			hideData = { hide:HideActionType.REPLAY };
		}
		
	}
}