package screens {
	import application.AssetsLoader;
	import feathers.controls.LayoutGroup;
	import feathers.controls.StackScreenNavigator;
	import feathers.controls.StackScreenNavigatorItem;
	import feathers.events.FeathersEventType;
	import feathers.layout.AnchorLayout;
	import feathers.layout.AnchorLayoutData;
	import feathers.motion.Slide;
	import screens.faq.ScreenFAQ;
	import screens.map.DrawerMapAddress;
	import screens.map.ScreenMap;
	import screens.posta.ScreenAllMails;
	import screens.posta.ScreenToPayMails;
	import screens.posta.ScreenDeclareMail;
	import screens.posta.ScreenMailContent;
	import screens.posta.ScreenMainMails;
	import screens.splash.ScreenIntro;
	import screens.splash.ScreenLang;
	import screens.splash.ScreenLogin;
	import screens.splash.ScreenLoginCase;
	import starling.display.Image;
	import starling.display.Quad;
	import starling.events.Event;
	import starling.textures.Texture;
	
	
	public class Splash extends LayoutGroup {
		
		private var logoWiteTexture:Texture;
		private var logoBlueTexture:Texture;
		
		private var logoImg:Image;
		private var shadowQade:Quad;
		private var topHeader:TopHeader;
		private var statusBar:StatusBar;
		private var topFooter:TopFooter;
		public var _savedScreenID:String;
		
		public function Splash() {
			
			super();
		}
		
		public var _navigator:StackScreenNavigator;
		
		
		override protected function initialize():void {
			
			this.layout = new AnchorLayout();
			Settings._splash = this;
			
			_changeBackgroundSkin(0xecf0f4);
			topHeader = new TopHeader;
			statusBar = new StatusBar;
			
			var bottomLayout:AnchorLayoutData = new AnchorLayoutData();
			bottomLayout.bottom = 0;
			topFooter = new TopFooter;
			topFooter.layoutData = bottomLayout;
			addChild(topFooter);
			
			logoWiteTexture = AssetsLoader._asset.getTexture("maleo_logo_wite.png");
			logoBlueTexture = AssetsLoader._asset.getTexture("maleo_logo_blue.png");
			
			logoImg = new Image(logoWiteTexture);
			logoImg.width = Settings._getIntByDPI(280);
			logoImg.height = Settings._getIntByDPI(55);
			logoImg.x = Math.round((stage.stageWidth - logoImg.width) / 2);
			logoImg.y = Settings._getIntByDPI(209);
			
			_navigator = new StackScreenNavigator();
			_navigator.pushTransition = Slide.createSlideLeftTransition();
			_navigator.popTransition = Slide.createSlideRightTransition();
			_navigator.addEventListener(FeathersEventType.TRANSITION_START, navigatorTransitionCompleteHandler);
			
			var item:StackScreenNavigatorItem = new StackScreenNavigatorItem(ScreenIntro); //ScreenIntro  ScreenLoginCase ScreenAllMails
			item.setScreenIDForPushEvent(AppEvent.COMPLETED, ScreenID.LANG_SELECT);
			_navigator.addScreen(ScreenID.INTRO, item);
			
			
			item = new StackScreenNavigatorItem(ScreenLang);
			item.setScreenIDForPushEvent(AppEvent.COMPLETED, ScreenID.LOGIN_CASE);
			item.addPopEvent(AppEvent.CANCEL);
			_navigator.addScreen(ScreenID.LANG_SELECT, item);
			
			item = new StackScreenNavigatorItem(ScreenLoginCase);
			item.setScreenIDForPushEvent(AppEvent.COMPLETED, ScreenID.ALL_MAILS);
			item.setScreenIDForPushEvent(AppEvent.LOGIN_NATIVE, ScreenID.LOGIN);
			item.addPopToRootEvent(AppEvent.CLOSE);
			_navigator.addScreen(ScreenID.LOGIN_CASE, item);
			
			item = new StackScreenNavigatorItem(ScreenLogin);
			item.setScreenIDForPushEvent(AppEvent.LOGIN_NATIVE, ScreenID.MAIN_MAILS);
			item.setScreenIDForReplaceEvent(AppEvent.LOGIN_FACEBOOK, ScreenID.LOGIN_CASE);
			item.addPopEvent(AppEvent.CANCEL);
			_navigator.addScreen(ScreenID.LOGIN, item);
			
			
			item = new StackScreenNavigatorItem(ScreenMainMails);
			item.setScreenIDForPushEvent(AppEvent.COMPLETED, ScreenID.ARRIVED_MAIL);
			item.setScreenIDForReplaceEvent(AppEvent.CANCEL, ScreenID.LOGIN_CASE);
			item.addPopEvent(AppEvent.CANCEL);
			_navigator.addScreen(ScreenID.MAIN_MAILS, item);
			
			item = new StackScreenNavigatorItem(ScreenToPayMails);
			item.setScreenIDForPushEvent(AppEvent.COMPLETED, ScreenID.LOGIN_CASE);
			item.addPopEvent(AppEvent.CANCEL);
			_navigator.addScreen(ScreenID.ARRIVED_MAIL, item);
			
			item = new StackScreenNavigatorItem(ScreenAllMails);
			item.setScreenIDForPushEvent(AppEvent.COMPLETED, ScreenID.LOGIN_CASE);
			item.addPopEvent(AppEvent.CANCEL);
			_navigator.addScreen(ScreenID.ALL_MAILS, item);
			
			item = new StackScreenNavigatorItem(ScreenDeclareMail);
			_navigator.addScreen(ScreenID.DECLARE_MAIL, item);
			
			item = new StackScreenNavigatorItem(ScreenMailContent);
			_navigator.addScreen(ScreenID.MAIL_CONTENT, item);
			
			item = new StackScreenNavigatorItem(ScreenFAQ);
			_navigator.addScreen(ScreenID.FAQ, item);
			
			
			item = new StackScreenNavigatorItem(DrawerMapAddress);
			//item.setScreenIDForPushEvent(AppEvent.COMPLETED, ScreenID.LOGIN_CASE);
			item.addPopEvent(AppEvent.CANCEL);
			_navigator.addScreen(ScreenID.MAPS_ADDRESS, item);
			
			
			item = new StackScreenNavigatorItem(ScreenMap);
			//item.setScreenIDForPushEvent(AppEvent.COMPLETED, ScreenID.LOGIN_CASE);
			item.addPopEvent(AppEvent.CANCEL);
			_navigator.addScreen(ScreenID.MAPS, item);			
			
			
			//item = new StackScreenNavigatorItem(ScreenLoginCase);
			//itemLoginCase.pushTransition = Fade.createFadeInTransition();
			//item.addPopEvent(AppEvent.CANCEL);
			//navigator.addScreen(ScreenID.LOGIN_CASE, item);
			
			/*var itemC:StackScreenNavigatorItem = new StackScreenNavigatorItem(ScreenLogin);
			   itemC.addPopToRootEvent(Event.CLOSE);
			   itemC.addPopEvent(Event.CANCEL);
			   this._navigator.addScreen(SCREEN_LOGIN, itemC);*/
			
			_navigator.rootScreenID = ScreenID.INTRO; //ScreenID.INTRO
			this.addChild(_navigator);
			//this.validate();
			
			//addChild(logoImg);
			
			addChild(topHeader);
			
			statusBar.y = topHeader.height;
			addChild(statusBar);
			
			addChild(topFooter);
			topFooter.validate();
		
		}
		
		public function _changeBackgroundSkin(bgColor:uint = 0xffffff):void {
			var bgQuad:Quad = new Quad(10, 10, bgColor);
			
			this.backgroundSkin = bgQuad;
			this.refreshBackgroundSkin();
			
			if (shadowQade) {
				this.removeChild(shadowQade);
				shadowQade.dispose();
				shadowQade = null;
			}
			shadowQade = new Quad(50, stage.stageHeight, bgColor);
			//shadowQade.filter = new DropShadowFilter(4, Math.PI);
			addChildAt(shadowQade, 0);
		
		}
		
		private function navigatorTransitionCompleteHandler(e:Event):void {
			
			if (logoImg && contains(logoImg)) removeChild(logoImg);
			
			topFooter.visible = false;
			topFooter._tabBar.selectedIndex = 0;
			statusBar._visible = false;
			
			
			var currentSt:String = StackScreenNavigator(e.target).activeScreenID;
			_savedScreenID = currentSt;
			topHeader._changeHeaderState(currentSt);
			
			switch (currentSt) {
				
				case ScreenID.INTRO: 
					
					logoImg.texture = logoWiteTexture;
					addChild(logoImg);
					break;
				
				case ScreenID.LANG_SELECT: 
				case ScreenID.LOGIN: 
				case ScreenID.LOGIN_CASE: 
				case ScreenID.REGISTER:
					
					logoImg.texture = logoBlueTexture;
					addChild(logoImg);
					
					_changeBackgroundSkin(0xffffff);
					
					break;
					
				case ScreenID.MAIN_MAILS:
					_changeBackgroundSkin(0xecf0f4);
					topFooter.visible = true;
					
					topFooter._tabBar.selectedIndex = 0;
					
					break;	
					
				case ScreenID.ALL_MAILS:
					_changeBackgroundSkin(0xecf0f4);
					topFooter.visible = true;
					topFooter._tabBar.selectedIndex = 1;
					
					break;	
					
				case ScreenID.ARRIVED_MAIL:
					
					_changeBackgroundSkin(0xecf0f4);
					topFooter.visible = false;
					
					break;	
					
				case ScreenID.DECLARE_MAIL:
					_changeBackgroundSkin(0xffffff);
					
					break;
						
					
				case ScreenID.MAIL_CONTENT:
					statusBar._visible = true;
					_changeBackgroundSkin(0xffffff);
					
					break;
					
				case ScreenID.MAPS:
				case ScreenID.MAPS_ADDRESS:
					topFooter._tabBar.selectedIndex = 3;
					topFooter.visible = true;
					_changeBackgroundSkin(0xffffff);
					break;
					
				case ScreenID.FAQ:
					
					
					break;
				
				default: 
					if (logoImg && contains(logoImg)) removeChild(logoImg);
				
			}
		}
	}
}