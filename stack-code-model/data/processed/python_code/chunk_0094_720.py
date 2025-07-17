package com.illuzor.otherside.controllers {
	
	import com.illuzor.otherside.controllers.resource.ResourceManager;
	import com.illuzor.otherside.events.LevelControllerEvent;
	import com.illuzor.otherside.utils.MegaTimer;
	import flash.events.TimerEvent;
	import flash.utils.Dictionary;
	import flash.utils.Timer;
	import starling.events.EventDispatcher;
	import starling.textures.Texture;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class LevelController extends EventDispatcher {
		
		private var groupControllers:Vector.<SingleGroupController> = new Vector.<SingleGroupController>();
		
		private var levelData:Object;
		private var waves:Array;
		private var currentWave:Object;
		private var currentGroup:Object;
		private var textures:Dictionary;
		private var curves:Object;
		private var groupsInWaveNum:uint;
		private var currentGroupNum:uint;
		private var groupsTimer:MegaTimer;
		
		public function LevelController(levelData:Object) {
			this.levelData = levelData;
			waves = levelData.waves;
			curves = ResourceManager.controller.getCurves(levelData.curves);
			
			textures = new Dictionary();
			for (var i:int = 0; i < levelData.textures.length; i++) {
				textures[levelData.textures[i].texture] = ResourceManager.controller.getTexture(levelData.textures[i].atlas, levelData.textures[i].texture);
			}
		}
		
		public function next():void {
			nextWave();
		}
		
		private function nextWave():void {
			if (waves.length) {
				currentWave = waves[0];
				waves.removeAt(0);
				divideWaveToGroups();
			} else {
				dispatchEvent(new LevelControllerEvent(LevelControllerEvent.LEVEL_COMPLETE));
			}
		}
		
		private function divideWaveToGroups():void {
			groupsInWaveNum = currentWave.groups.length;
			currentGroupNum = 0;
			groupsTimer = new MegaTimer(currentWave.groups[0].delay*1000, 1);
			groupsTimer.start();
			groupsTimer.addEventListener(TimerEvent.TIMER_COMPLETE, onGroupCreateTimer);
		}
		
		private function onGroupCreateTimer(e:TimerEvent):void {
			if (currentGroupNum <  groupsInWaveNum) {
				currentGroup = currentWave.groups[currentGroupNum];
				parseGroup();
				
				if (currentGroupNum <  groupsInWaveNum - 1) {
					currentGroupNum++;
					groupsTimer.stop();
					groupsTimer.start(currentWave.groups[currentGroupNum].delay * 1000);
				} else {
					groupsTimer.removeEventListener(TimerEvent.TIMER_COMPLETE, onGroupCreateTimer);
					groupsTimer.dispose();
					groupsTimer = null;
				}
			} 
		}
		
		private function parseGroup():void {
			if (currentGroup.hasOwnProperty("enemies")) {
				switch (currentGroup.move) {
					case "bezier":
						makeBezierGroup();
					break;
				}
			}
			
			if (currentGroup.hasOwnProperty("asteroids")) {
				
			}
		}
		
		private function makeBezierGroup():void {
			var groupController:SingleGroupController = new SingleGroupController(currentGroup, curves, textures);
			groupController.addEventListener(LevelControllerEvent.ADD_ENEMY, onSingleControllerEvent);
			groupController.addEventListener(LevelControllerEvent.GROUP_COMPLETE, onSingleControllerEvent);
			groupControllers.push(groupController);
		}
		
		private function onSingleControllerEvent(e:LevelControllerEvent):void {
			switch (e.type) {
				case LevelControllerEvent.ADD_ENEMY:
					dispatchEvent(new LevelControllerEvent(LevelControllerEvent.ADD_ENEMY, e.enemy));
				break;
				case LevelControllerEvent.GROUP_COMPLETE:
					var groupController:SingleGroupController = e.target as SingleGroupController
					groupController.removeEventListener(LevelControllerEvent.ADD_ENEMY, onSingleControllerEvent);
					groupController.removeEventListener(LevelControllerEvent.GROUP_COMPLETE, onSingleControllerEvent);
					groupController.dispose();
					var index:uint = groupControllers.indexOf(groupController)
					groupControllers.removeAt(index);
				break;
			}
			
		}
		
		public function pause():void {
			if (groupsTimer) groupsTimer.pause();
			for (var i:int = 0; i < groupControllers.length; i++) {
				groupControllers[i].pause();
			}
		}
		
		public function play():void {
			if (groupsTimer) groupsTimer.start();
			for (var i:int = 0; i < groupControllers.length; i++) {
				groupControllers[i].play();
			}
		}
		
		public function dispose():void {
			for each (var texture:Texture in textures) {
				texture.dispose();
			}
			
			for (var i:int = 0; i < groupControllers.length; i++) {
				groupControllers[i].dispose();
			}
			
			if (groupsTimer) {
				groupsTimer.removeEventListener(TimerEvent.TIMER_COMPLETE, onGroupCreateTimer);
				groupsTimer.dispose();
				groupsTimer = null;	
			}
			
			textures = null;
			curves = null;
		}
		
	}
}