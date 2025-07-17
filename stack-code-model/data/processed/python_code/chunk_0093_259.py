package com.illuzor.thegame.editor {
	
	import com.bit101.components.PushButton;
	import com.illuzor.thegame.editor.events.TestLevelEvent;
	import com.illuzor.thegame.world.Level;
	import flash.events.MouseEvent;
	import net.flashpunk.Engine;
	import net.flashpunk.FP;
	
	/**
	 * ...
	 * @author illuzor // illuzor.com // illuzor@gmail.com
	 */
	
	[Event(name = "returnToEditor", type = "com.illuzor.thegame.editor.events.TestLevelEvent")]
	
	public class GameView extends Engine {
		
		private var levelData:Object;
		private var level:Level;
		
		public function GameView() {
			super(800, 600);
			this.levelData = levelData;
			var playLevelButton:PushButton = new PushButton(this, 810, 610, "RETURN TO EDITOR", onReturnToEditor);
		}
		
		public function start(levelData:Object):void {
			level = new Level(levelData);
			FP.world = level;
		}
		
		public function stopp():void {
			FP.world = null;
			level.removeAll();
			level = null;
		}
		
		private function onReturnToEditor(e:MouseEvent):void {
			dispatchEvent(new TestLevelEvent(TestLevelEvent.RETURN_TO_EDITOR));
		}
		
	}

}