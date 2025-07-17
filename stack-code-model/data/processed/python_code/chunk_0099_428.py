package screens {
	import application.AssetsLoader;
	import application.utils.StaticGUI;
	import feathers.controls.Button;
	import feathers.controls.Header;
	import feathers.controls.text.TextFieldTextRenderer;
	import feathers.core.ITextRenderer;
	import feathers.layout.AnchorLayoutData;
	import feathers.motion.Slide;
	import feathers.skins.ImageSkin;
	import starling.display.DisplayObject;
	import starling.display.Image;
	import starling.display.Quad;
	import starling.events.Event;
	import starling.text.TextFormat;
	import starling.textures.TextureSmoothing;
	

	public class TopHeader extends Header {
		
		private var btnLeftSkin:ImageSkin;
		private var btnRightSkin:ImageSkin;
		private var bgQuad:Quad;
		private var bgSkin:Image;
		private var titleGeoStyle:TextFormat;
		
		public static const FAQ_BLUE_ITEM:String                        = 'faqBlueItem';
		public static const MENU_BLUE_ITEM:String                       = 'menuBlueItem';
		public static const FAQ_WHITE_ITEM:String                       = 'faqWhiteItem';
		public static const MENU_WHITE_ITEM:String                      = 'menuWhiteItem';
		public static const EDIT_WHITE_ITEM:String                      = 'editWhiteItem';
		public static const EDIT_DISABLED_WHITE_ITEM:String             = 'editDisabledWhiteItem';
		public static const ARROWTOLEFT_WHITE_ITEM:String               = 'arrowToLeftWhiteItem';
		public static const CLOSE_WHITE_ITEM:String                     = 'closeWhiteItem';
		public static const MAP_WHITE_SETTINGS:String                   = 'mapSettingsWhiteItem';
		
		public static const LEFT_ITEM:String                            = 'leftSideItem';
		public static const RIGHT_ITEM:String                           = 'rightSideItem';
		
		private var menuItems:Vector.<Object>;
		public static var _currentLeftItem:String;
		public static var _currentRightItem:String;
		
		
		
		public function TopHeader() {
			super();
			
			menuItems = new Vector.<Object>;
			
			menuItems.push({name:FAQ_BLUE_ITEM,                texture:'faq_blue_btn.png',                widthDPI:50,     heightDPI:50});
			menuItems.push({name:FAQ_WHITE_ITEM,               texture:'faq_white_btn.png',               widthDPI:50,     heightDPI:50});
			menuItems.push({name:MENU_BLUE_ITEM,               texture:'menu_blue_btn.png',               widthDPI:48,     heightDPI:34});
			menuItems.push({name:MENU_WHITE_ITEM,              texture:'menu_white_btn.png',              widthDPI:48,     heightDPI:34});
			menuItems.push({name:EDIT_WHITE_ITEM,              texture:'edit_white_btn.png',              widthDPI:41,     heightDPI:40});
			menuItems.push({name:EDIT_DISABLED_WHITE_ITEM,     texture:'edit_disabled_white_btn.png',     widthDPI:41,     heightDPI:40});
			menuItems.push({name:ARROWTOLEFT_WHITE_ITEM,       texture:'arrowtoleft_white_btn.png',       widthDPI:47,     heightDPI:40});
			menuItems.push({name:CLOSE_WHITE_ITEM,             texture:'close_white_btn.png',             widthDPI:38,     heightDPI:38});
			menuItems.push({name:MAP_WHITE_SETTINGS,           texture:'map_settings_white_btn.png',      widthDPI:49,     heightDPI:39});
			
			
			this.addEventListener(Event.ADDED_TO_STAGE, added)
			
		}
		
		public function _changeBackgroundSkin(bgColor:uint = 0xffffff):void {
			var bgQuad:Quad = new Quad(10, 10, bgColor);
			
			this.backgroundSkin = bgQuad;
			//this.refreshBackgroundSkin();
			
		}
		
		private function added(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, added);
			this.addEventListener(Event.REMOVED_FROM_STAGE, removed);
			
			this.paddingLeft = Settings._getIntByDPI(0);
			this.paddingRight = Settings._getIntByDPI(0);
			this.paddingTop = Settings._getIntByDPI(25);
			
			//_setMenuItems(MENU_WHITE_ITEM, LEFT_ITEM);
			//_setMenuItems(FAQ_WHITE_ITEM, RIGHT_ITEM);
			
			titleGeoStyle = new TextFormat;
			titleGeoStyle.font = '_bpgMrglovaniCapsRegular';//_hKolkhetyMtavBold
			titleGeoStyle.size = Settings._getIntByDPI(30);
			titleGeoStyle.color = 0xFFFFFF;
			
			this.fontStyles = titleGeoStyle;
			title = 'მთავარი';
			
			titleFactory = function():ITextRenderer {
				var titleRenderer:TextFieldTextRenderer = new TextFieldTextRenderer();
				
				titleRenderer.embedFonts = true;
				return titleRenderer;
			}
			
			this.width = stage.stageWidth;
			this.height = Settings._getIntByDPI(130);
			validate();
		}
		
		public function _changeTitle(titleStr:String = ''):void {
			title = titleStr;
		}
		
		
		public function _setMenuItems(setIco:String = null, side:String = LEFT_ITEM, clear:Boolean = false):void {
			
			var skin:ImageSkin;
			var btn:Button;
			var i:uint;
			var removeItem:DisplayObject;
			if (side == LEFT_ITEM && leftItems && clear) {
			
				for (i = 0; i < leftItems.length; i++ ) {
					removeItem = leftItems[i] as DisplayObject;
					
					removeItem.parent.removeChild(removeItem);
					
					if (removeItem) removeItem = StaticGUI._safeRemoveChildren(removeItem, true);
				}
				
				leftItems = null;
				_currentLeftItem = '';
			}
			
			if (side == RIGHT_ITEM && rightItems && clear) {
				
				for (i = 0; i < rightItems.length; i++ ) {
					removeItem = rightItems[i] as DisplayObject;
					
					removeItem.parent.removeChild(removeItem);
					if (removeItem) removeItem = StaticGUI._safeRemoveChildren(removeItem, true);
				}
				
				rightItems = null
				_currentRightItem = '';
			}
			if (!setIco) return;
			
			for (i = 0; i < menuItems.length; i++ ) {
				if (setIco  == menuItems[i].name) {
					skin = new ImageSkin(AssetsLoader._asset.getTexture(menuItems[i].texture));
					skin.width = Settings._getIntByDPI(menuItems[i].widthDPI);
					skin.height = Settings._getIntByDPI(menuItems[i].heightDPI);
					//skin.textureSmoothing = TextureSmoothing.TRILINEAR;
					var q:Quad = new Quad(this.height, this.height-this.paddingTop);
					q.alpha = 0;
					btn = new Button();
					
					btn.defaultSkin = q;
					btn.defaultIcon = skin;
					btn.name = menuItems[i].name;
					if (side == LEFT_ITEM) {
						
						if (!leftItems) leftItems = new <DisplayObject>[];
						leftItems.push(btn);
						_currentLeftItem = menuItems[i].name;
						btn.addEventListener(Event.TRIGGERED, headerLeftNavHandler);
						
					}else if (side == RIGHT_ITEM) {
						
						if (!rightItems) rightItems = new <DisplayObject>[];
						rightItems.push(btn);
						_currentRightItem = menuItems[i].name;
						btn.addEventListener(Event.TRIGGERED, headerRightNavHandler);
						
					}else {
						
					}
					break;	
				}
			}
		}
		
		
		public function _changeHeaderState(screenID:String):void {
			visible = false;
			
			_setMenuItems(null, TopHeader.LEFT_ITEM, true);
			_setMenuItems(null, TopHeader.RIGHT_ITEM, true);
			
			switch(screenID) {
				case ScreenID.INTRO:
					
					
					break;
				
				case ScreenID.LOGIN:
				case ScreenID.LOGIN_CASE:
				case ScreenID.REGISTER:	
					
					visible = true;
					_changeBackgroundSkin(0xffffff);
					_setMenuItems(MENU_BLUE_ITEM);
					_setMenuItems(FAQ_BLUE_ITEM, RIGHT_ITEM);
					
					break;
					
				case ScreenID.MAIN_MAILS:
					
					_changeBackgroundSkin(0x00b7f0);
					_setMenuItems(MENU_WHITE_ITEM);
					_setMenuItems(FAQ_WHITE_ITEM, RIGHT_ITEM);
					visible = true;
					
				break	
					
				case ScreenID.DECLARE_MAIL:
					
					_setMenuItems(CLOSE_WHITE_ITEM);
					_changeBackgroundSkin(0x00b7f0);
					visible = true;
					
				break;
				
				case ScreenID.MAIL_CONTENT:
					
					_setMenuItems(ARROWTOLEFT_WHITE_ITEM);
					_changeBackgroundSkin(0x00b7f0);
					visible = true;
					
				break
					
				case ScreenID.ALL_MAILS:
					
					visible = true;
					_changeBackgroundSkin(0x00b7f0);
					_setMenuItems(MENU_WHITE_ITEM);
					_setMenuItems(FAQ_WHITE_ITEM, RIGHT_ITEM);
					
					break;
				case ScreenID.ARRIVED_MAIL:
					
				    visible = true;
					_changeBackgroundSkin(0x00b7f0);
					_setMenuItems(ARROWTOLEFT_WHITE_ITEM);
					_setMenuItems(FAQ_WHITE_ITEM, RIGHT_ITEM);
					
					break;
					
				case ScreenID.MAPS:
				case ScreenID.MAPS_ADDRESS:
					
					visible = true;
					_changeBackgroundSkin(0x00b7f0);
					
					if (screenID == ScreenID.MAPS_ADDRESS) {
						_setMenuItems(MAP_WHITE_SETTINGS);
					}else {
						_setMenuItems(ARROWTOLEFT_WHITE_ITEM);
					}
					
					
					break;
					
				case ScreenID.FAQ:	
					
					visible = true;
					_changeBackgroundSkin(0x00b7f0);
					_setMenuItems(ARROWTOLEFT_WHITE_ITEM);
					
					break;	
					
			}
		}
		
		private function headerLeftNavHandler(e:Event):void {
			
			switch(_currentLeftItem) {
				case MENU_BLUE_ITEM:
				case MENU_WHITE_ITEM:
					
					this.dispatchEventWith(AppEvent.TOGGLE_LEFT_DRAWER, true);
					break;
					
				case ARROWTOLEFT_WHITE_ITEM:
					
					Settings._splash._navigator.popScreen();
					break
				
				case CLOSE_WHITE_ITEM:
					
					Settings._splash._navigator.pushScreen(ScreenID.MAIN_MAILS, null, Slide.createSlideRightTransition());
					break;
					
				case MAP_WHITE_SETTINGS:
					
					if (Settings._mapSettingsDrawer) Settings._mapSettingsDrawer.toggleTopDrawer();
					break;	
			}	
		}
		
		private function headerRightNavHandler(e:Event):void {
			
			switch(_currentRightItem) {
				case FAQ_BLUE_ITEM:
				case FAQ_WHITE_ITEM:
					
					Settings._splash._navigator.pushScreen(ScreenID.FAQ);
					break;
					
				case EDIT_WHITE_ITEM:
					
					break;
					
				case EDIT_DISABLED_WHITE_ITEM:
					
					break;
					
				
			}
			
			
		}
		
		private function removed(e:Event):void {
			removeEventListener(Event.REMOVED_FROM_STAGE, removed);
		}
		
	}

}