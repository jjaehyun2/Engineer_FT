package com.illuzor.otherside.editor.screen {
	
	import com.illuzor.otherside.editor.constants.ScreenType;
	import com.illuzor.otherside.editor.events.ScreenEvent;
	import com.illuzor.otherside.editor.screen.EditorScreen;
	import com.illuzor.otherside.editor.screen.LevelSelectionScreen;
	import com.illuzor.otherside.editor.screen.MainMenu;
	import com.illuzor.otherside.editor.screen.ScreenBase;
	import flash.display.Sprite;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class ScreenManager extends Sprite {
		
		private var screen:ScreenBase;
		
		public function ScreenManager() {
			screen = new MainMenu();
			addChild(screen);
			
			addEventListener(ScreenEvent.SCHANGE_SCREEN, onChangeScreen);
		}
		
		private function onChangeScreen(e:ScreenEvent):void {
			e.stopImmediatePropagation();
			screen.dispose();
			removeChild(screen);
			
			switch (e.screenType) {
				case ScreenType.MAIN_MENU_SCREEN:
					screen = new MainMenu();
				break;
				case ScreenType.EDITOR_SCREEN:
					screen = new EditorScreen(e.levelData.zone, e.levelData.level);
				break;
				case ScreenType.LEVEL_SELECTION_SCREEN:
					screen = new LevelSelectionScreen();
				break;
			}
			addChild(screen);
		}
		
	}
}