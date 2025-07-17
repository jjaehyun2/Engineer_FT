package {
	import application.AssetsLoader;
	import application.utils.UserPrefs;
	import drawer.Drawer;
	import feathers.controls.Button;
	import feathers.controls.TextCallout;
	import feathers.themes.TopcoatLightMobileTheme;
	import flash.utils.clearInterval;
	import flash.utils.setInterval;
	import starling.display.Sprite;
	import starling.events.Event;
	
	public class Main extends Sprite {
		
		private var assetLoadingInterval:uint;
	
		public function Main() {
			
			this.addEventListener(Event.ADDED_TO_STAGE, addedToStageHandler);
		}
		
		protected var button:Button;
		
		
		protected function addedToStageHandler(event:Event):void {
			
			this.removeEventListener(Event.ADDED_TO_STAGE, addedToStageHandler);
			assetLoadingInterval = setInterval (checkIfAssetsLoaded, 500);
			
			new TopcoatLightMobileTheme();
				
		}
		
		
		private function checkIfAssetsLoaded():void {
			
			if (AssetsLoader._asset._loaded) {
				AppPreloader._cont._assetLoaded();
				clearInterval(assetLoadingInterval);
			}else {
				return;	
			}
			
			
			
			
			/*this.button = new Button();
			this.button.label = "Click Me";
			
			
			this.button.addEventListener(Event.TRIGGERED, button_triggeredHandler);
			this.addChild(this.button);
			
			this.button.validate();

			trace(DeviceInfo.dpiScaleMultiplier);
			this.button.width = stage.stageWidth * (1 / DeviceInfo.dpiScaleMultiplier);
			this.button.x = Math.round((this.stage.stageWidth - this.button.width) / 2);
			this.button.y = Math.round((this.stage.stageHeight - this.button.height) / 2);*/
			
			var spl:Drawer = new Drawer;
			addChild(spl);
			
			UserPrefs._write();
			var ob:Object = UserPrefs._read();
			
		}

		protected function button_triggeredHandler(event:Event):void {
			TextCallout.show("Hi, I'm Feathers!\nHave a nice day.", this.button);
		}
	}
}