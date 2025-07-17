package com.illuzor.otherside.controllers {
	
	import adobe.utils.CustomActions;
	import com.illuzor.otherside.constants.AtlasType;
	import com.illuzor.otherside.constants.ScreenType;
	import com.illuzor.otherside.controllers.resource.ResourceManager;
	import com.illuzor.otherside.errors.ControllerError;
	import com.illuzor.otherside.errors.ScreenError;
	import com.illuzor.otherside.events.ResourceControllerEvent;
	import com.illuzor.otherside.events.ScreenEvent;
	import com.illuzor.otherside.screens.GameScreen;
	import com.illuzor.otherside.screens.MainMenu;
	import com.illuzor.otherside.screens.ScreenBase;
	import com.illuzor.otherside.screens.subscreens.LoadingScreen;
	import com.illuzor.otherside.Settings;
	import flash.events.Event;
	import flash.events.KeyboardEvent;
	import flash.ui.Keyboard;
	import starling.core.Starling;
	import starling.display.Sprite;

	
	CONFIG::airmobile {
		import flash.desktop.NativeApplication;
	}
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public final class AppController {
		
		private static var isMobile:Boolean;
		private static var firstRun:Boolean = true;
		private static var currentScreenType:uint;
		private static var screen:ScreenBase;
		private static var container:Sprite;
		private static var loadingScreen:LoadingScreen;
		
		public static function setContainer(container:Sprite):void {
			AppController.container = container;
			container.addEventListener(ScreenEvent.CHANGE_SCREEN, onScreenEvent);
			container.addEventListener(ScreenEvent.SCREEN_READY, onScreenEvent);
			container.addEventListener(ScreenEvent.SCREEN_ERROR, onScreenEvent);
		}
		
		public static function start():void {
			CONFIG::airmobile {
				NativeApplication.nativeApplication.addEventListener(Event.ACTIVATE, onAppEvent);
				NativeApplication.nativeApplication.addEventListener(Event.DEACTIVATE, onAppEvent);
				NativeApplication.nativeApplication.addEventListener(Event.SUSPEND, onAppEvent);
			}
			
			ResizeManager.stage.addEventListener(KeyboardEvent.KEY_DOWN, onKeyDown);
			
			isMobile = ResourceManager.controller.isMobile;
			ResourceManager.controller.initialLoad();
			ResourceManager.controller.addEventListener(ResourceControllerEvent.INITIAL_LOAD_COMPLETE, onInitialLoadComplete);
		}
		
		private static function onInitialLoadComplete(e:ResourceControllerEvent):void {
			ResourceManager.controller.removeEventListener(ResourceControllerEvent.INITIAL_LOAD_COMPLETE, onInitialLoadComplete);
			Settings.langConfig = ResourceManager.controller.lang;
			showScreen(ScreenType.MAIN_MENU);
		}
		
		CONFIG::airmobile {
		private static function onAppEvent(e:Event):void {
			switch (e.type) {
				case Event.ACTIVATE:
					Starling.current.start();
					if (screen) screen.resume();
				break;
				case Event.DEACTIVATE:
					if (screen) screen.pause();
					Starling.current.stop(true);
				break;
				case Event.SUSPEND:
					NativeApplication.nativeApplication.exit();
				break;
			}
		}
		}
		
		private static function onScreenEvent(e:ScreenEvent):void {
			e.stopImmediatePropagation();
			switch (e.type) {
				case ScreenEvent.CHANGE_SCREEN:
					showScreen(e.screenType);
				break;
				case ScreenEvent.SCREEN_READY:
					CONFIG::airmobile {
						if (loadingScreen) {
							container.removeChild(loadingScreen, true);
							loadingScreen = null;
						}
					}
					screen.start();
				break;
				case ScreenEvent.SCREEN_ERROR:
					throw new ScreenError("AppController.onScreenEvent() screenerror");
				break;
			}
		}
		
		CONFIG::airmobile {
		private static function showScreen(screenType:uint):void {
			if (screen)
				container.removeChild(screen, true);
				
			var showLoadingScreen:Boolean = true;
			
			CONFIG::android {
				if (firstRun) {
					showLoadingScreen = false;
				}
			}
			
			if(showLoadingScreen){
				loadingScreen = new LoadingScreen();
				container.addChild(loadingScreen);
			}
			
			currentScreenType = screenType;
			var dataForLoad:Object;
			if (currentScreenType == ScreenType.GAME_SCREEN) {
				dataForLoad = {atlasses:[AtlasType.ATLAS_1, AtlasType.ASTERIODS_ATLAS]};
			} else {
				dataForLoad = {atlasses:[AtlasType.MENU_ATLAS]};
			}
			ResourceManager.controller.loadResources(dataForLoad);
			ResourceManager.controller.addEventListener(ResourceControllerEvent.LOAD_COMPLETE, onResourcesLoaded);
		}
		
		private static function onResourcesLoaded(e:ResourceControllerEvent):void {
			makeScreen();
			
			CONFIG::android {
				if(firstRun)
					ResizeManager.stage.getChildAt(0).dispatchEvent(new Event(Event.COMPLETE, true));
			}
			firstRun = false;
		}
		}
		
		CONFIG::flashplayer {
		private static function showScreen(screenType:uint):void {
			if (screen) {
				container.removeChild(screen);
			}
			currentScreenType = screenType;
			makeScreen();
		}
		}
		
		private static function makeScreen():void {
			switch (currentScreenType) {
				case ScreenType.MAIN_MENU:
					screen = new MainMenu();
				break;
				case ScreenType.SETTINGS_SCREEN:
					
				break;
				case ScreenType.ABOUT_SCREEN:
					
				break;
				case ScreenType.MODE_SELECTION_SCREEN:
					
				break;
				case ScreenType.LEVELS_SELECTION_SCREEN:
					
				break;
				case ScreenType.GAME_SCREEN:
					var levelData:Object = new Object();
					levelData.weapons = [ { delay:1.2, type:0, x:0, y: -112 } ];
					levelData.level = ResourceManager.controller.getLevelConfig();
					screen = new GameScreen(levelData);
				break;
				default: throw new ControllerError("AppController.makeScreen(), wrong currentScreenType: " + currentScreenType);
			}
			container.addChild(screen);
		}
		
		private static function onKeyDown(e:KeyboardEvent):void {
			if (e.keyCode == Keyboard.BACK || e.keyCode == Keyboard.BACKSPACE) {
				e.preventDefault();
				screen.back();
			}
		}
		
	}
}