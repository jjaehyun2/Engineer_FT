package com.illuzor.thegame.editor.panels {
	
	import com.bit101.components.PushButton;
	import flash.display.Sprite;
	
	/**
	 * ...
	 * @author illuzor // illuzor.com // illuzor@gmail.com
	 */
	
	public class MainMenuPanel extends Sprite {
		
		public var newLevel:PushButton;
		public var editLevel:PushButton;
		public var importConfig:PushButton;
		public var exportConfig:PushButton;
		
		public function MainMenuPanel() {
			newLevel = new PushButton(this, 0, 0, "NEW LEVEL");
			editLevel = new PushButton(this, 0, 30, "EDIT LEVEL");
			exportConfig = new PushButton(this, 0, 60, "EXPORT CONFIG");
			importConfig = new PushButton(this, 0, 90, "IMPORT CONFIG");
		}
		
	}
}