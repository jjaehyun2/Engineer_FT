package
{
	import feathers.controls.ScreenNavigator;
	import feathers.controls.ScreenNavigatorItem;
	import feathers.motion.transitions.ScreenSlidingStackTransitionManager;
	import feathers.themes.PowerChalkTheme;
	
	import so.cuo.anes.admob.AdEvent;
	import so.cuo.anes.admob.AdSize;
	import so.cuo.anes.admob.Admob;
	
	import starling.display.Sprite;
	import starling.events.Event;

	public class FIFA14 extends Sprite
	{
		private var nav:ScreenNavigator;
		//iOS
		private var admobId:String = 'ca-app-pub-7133433021804463/5470484435';
		//Android
		//private var admobId:String = 'ca-app-pub-7133433021804463/7677404435';
		private var admob:Admob;
		
		public function FIFA14()
		{
			this.addEventListener( Event.ADDED_TO_STAGE, addedToStageHandler );
			
		}
		private function addedToStageHandler( event:Event ):void
		{
			//var theme:MetalWorksMobileTheme = new MetalWorksMobileTheme(stage);
			//var theme:AzureMobileTheme = new AzureMobileTheme(stage);
			var theme:PowerChalkTheme = new PowerChalkTheme(stage);
			
			nav = new ScreenNavigator();
			addChild(nav);
			
			var indexScreen:ScreenNavigatorItem = new ScreenNavigatorItem( IndexScreen );
			nav.addScreen(Constants.INDEX_SCREEN, indexScreen);
			
			nav.showScreen(Constants.INDEX_SCREEN);
			
			var transition:ScreenSlidingStackTransitionManager = new ScreenSlidingStackTransitionManager(nav);
			
			showAd();
		}
		private function showAd():void
		{
			admob = Admob.getInstance();
			if (admob.isSupported)
			{
				trace("supported");
				admob.createADView(AdSize.SMART_BANNER, admobId); //create a banner ad view.this init the view 
				admob.addToStage(0,10); // ad to displaylist position 0,0
				admob.load(false); // send a ad request. 
				admob.dispatcher.addEventListener(AdEvent.onReceiveAd,onAdEvent);
			}
			else
			{
				trace("not support");
			}
		}
		private function onAdEvent(e:AdEvent):void
		{
			trace("Ad height:"+admob.getAdSize().height+"screen size:"+admob.getScreenSize());
			Main._model.setAdHeight(admob.getAdSize().height-10);
			IndexScreen(nav.activeScreen).reDraw();
		}
	}
}