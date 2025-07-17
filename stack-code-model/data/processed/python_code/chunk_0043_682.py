package com.cupcake.game.graphics {
	
	import com.cupcake.game.logic.HandShape;
	import flash.display.MovieClip;	
	import flash.events.MouseEvent;
	import flash.utils.getDefinitionByName;
	import flash.utils.getQualifiedClassName;
	
	public class Game extends MovieClip{
		
		public static var isIaVsIa:Boolean;
		public static var enableSpockLizardGame:Boolean = false;
		
		public function Game(isIaVsIa:Boolean){
			Game.isIaVsIa = isIaVsIa;
			
			initGame();
		}	
		
		private var gameBG:MovieClip = new GameBG();
		private function initGame():void 
		{
			addChild(gameBG);
			
			if (isIaVsIa){
				var rand:int = randomize();
				onPlay(rand);
				
				gameBG.chooseYourHand.visible = false;
			}
			
			gameBG.rock.addEventListener(MouseEvent.CLICK, rockSelected);
			gameBG.paper.addEventListener(MouseEvent.CLICK, paperSelected);
			gameBG.scissors.addEventListener(MouseEvent.CLICK, scissorsSelected);
			if (enableSpockLizardGame){
				//todo
				gameBG.spock.visible = true;
				gameBG.lizard.visible = true;
				
				gameBG.spock.addEventListener(MouseEvent.CLICK, spockSelected);
				gameBG.lizard.addEventListener(MouseEvent.CLICK, lizardSelected);
			}
		}
		
		private function lizardSelected(e:MouseEvent):void 
		{
			onPlay(5);	
		}
		
		private function spockSelected(e:MouseEvent):void 
		{
			onPlay(4);
		}
		
		private function rockSelected(e:MouseEvent):void 
		{
			onPlay(1);
		}
		
		private function paperSelected(e:MouseEvent):void 
		{
			onPlay(2);
		}
		
		private function scissorsSelected(e:MouseEvent):void 
		{
			onPlay(3);
		}
		
		private function onPlay(handPlayed:Number):void 
		{		
			var selectedHand:HandShape = HandShape.getShapeTypes()[handPlayed-1];
			
			gameBG.myPlay.visible = true;
			gameBG.myPlay.gotoAndStop(handPlayed);
			
			//HAND / RAND -- hahaa little inside joke about Iron Fist Series. 
			var rand:int = randomize();
			gameBG.otherPlay.gotoAndStop(rand);
			gameBG.otherPlay.visible = true;
			
			var otherHand:HandShape = HandShape.getShapeTypes()[rand - 1];						
			
			checkPlay(selectedHand, otherHand);
		}
		
		private function checkPlay(selectedHand:HandShape, otherHand:HandShape):void 
		{
			if (selectedHand is Object(otherHand).constructor){
				result("draw");
				return;
			}
			
			var beats:Array = selectedHand.beats();
			var res:String = "lost";
			for (var i:uint = 0; i < beats.length; i++) {				
				if (otherHand is beats[i]) res = "win";				
			}
						
			result(res);
		}
		
		private function result(res:String):void 
		{
			var endGameOverlay:EndGameOverlay = new EndGameOverlay();
			endGameOverlay.init(res);
			
			addChild(endGameOverlay);
			
		}
		
		private function randomize():int 
		{
			return int(Math.random() * HandShape.getShapeTypes().length) + 1;
		}
	}	
}