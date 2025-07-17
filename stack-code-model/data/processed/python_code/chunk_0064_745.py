package
{
	import flash.display.Bitmap;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.geom.Rectangle;
	import flash.system.Capabilities;
	
	import feathers.controls.ProgressBar;
	import feathers.controls.ScrollContainer;
	
	import starling.core.Starling;
	import starling.events.Event;
	import starling.utils.AssetManager;
	
	public class Main extends Sprite
	{
		public static var starling:Starling;
		private static var splashLoaded:Boolean = false;
		private var pBar:ProgressBar;
		public static var AssetMgr:AssetManager; 
		public static var _model:Model = new Model();
		public static var _appView:AppView = new AppView();
		public static var _splash:Bitmap;
		
		[Embed(source="../assets/graphics/splash.png")]
		public static const SPLASH_IMAGE:Class;
		
		public function Main()
		{
			starling = new Starling(FIFA14, stage);
			//starling.showStats = true;
			starling.addEventListener(starling.events.Event.ROOT_CREATED, starlingReady);
			
			_splash = new SPLASH_IMAGE() as Bitmap;
			_splash.width = stage.fullScreenWidth;  // Capabilities.screenResolutionY;
			_splash.height = stage.fullScreenHeight;  // Capabilities.screenResolutionX;
			//_splash.addEventListener(flash.events.Event.ADDED_TO_STAGE, onSplashLoaded);
			//addChild(_splash);
			
			var container:ScrollContainer = new ScrollContainer();
			container.height = .2 * stage.fullScreenHeight;
			container.width = stage.fullScreenWidth;
			
			pBar = new ProgressBar();
			pBar.minimum = 0;
			pBar.maximum = 100;
			pBar.value = 0;
			container.addChild( pBar );
			
			starling.antiAliasing = 1;
			starling.start();
			this.stage.addEventListener(flash.events.Event.RESIZE, stageResized);
		}
		private function onSplashLoaded(e:flash.events.Event):void
		{
			splashLoaded = true;
			_splash.removeEventListener(flash.events.Event.ADDED_TO_STAGE, onSplashLoaded);
		}
		public static function killSplash():void 
		{
			if (splashLoaded)
			{
				_splash.parent.removeChild(_splash);
				_splash = null;
				splashLoaded = false;
			}
			
		}
		private function starlingReady(e:starling.events.Event):void
		{
			starling.removeEventListener(starling.events.Event.ROOT_CREATED, starlingReady);  // one time deal
			AssetMgr.loadQueue(function onProgress(ratio:Number):void
			{
				trace("Loading assets..." + ratio);
				pBar.value = Math.floor(ratio*100);
				// a progress bar should always show the 100% for a while,
				// so we show the main menu only after a short delay. 
				
				//				if (ratio == 1)
				//					Starling.juggler.delayCall(function():void
				//					{
				//						progressBar.removeFromParent(true);
				//						showScene(Menu);
				//					}, 0.15);
			});
		}
		private function stageResized(e:flash.events.Event):void
		{
			starling.stage.stageWidth = this.stage.stageWidth;
			starling.stage.stageHeight = this.stage.stageHeight;
			const viewPort:Rectangle = starling.viewPort;
			viewPort.width = this.stage.stageWidth;
			viewPort.height = this.stage.stageHeight;
			starling.viewPort = viewPort;
			trace("Stage is " + this.stage.stageWidth + " x " + this.stage.stageHeight);
			Main._appView.setAppScale( this.stage.stageWidth / 320);
			Main._appView.stageWidth = this.stage.stageWidth;
			Main._appView.stageHeight = this.stage.stageHeight;
			
			AssetMgr = new AssetManager(Main._appView.getAppScale());
			AssetMgr.verbose = Capabilities.isDebugger;
		}
	}
}