package com.adrienheisch.spacewar.game
{
	import com.adrienheisch.neuralnetwork.Genetic;
	import com.adrienheisch.spacewar.Main;
	import flash.display.Stage;
	import flash.events.Event;
	
	/**
	 * ...
	 * @author Adrien Heisch
	 */
	public class GameManager
	{
		protected static const GAMELOOP_CLASSES:Vector.<Class> = new <Class>[Ship, Bullet, Explosion];
		
		protected static const N_SHIPS:uint = 2; // 2 - 4 ships
		protected static const N_PLAYERS:uint = 1; // 1 <= N_PLAYERS <= 2
		
		protected static var stage:Stage;
		
		public static function init():void
		{
			stage = Main.instance.stage;
			
			stage.focus = stage;
			
			stage.addChild(GameContainer.instance);
		}
		
		public static function startGame():void
		{
			var lShip:Ship;
			var shipsPerLine:uint = 2;
			for (var i:int = 0; i < N_SHIPS - N_SHIPS % shipsPerLine; ++i)
			{
				GameContainer.instance.addChild(lShip = (N_PLAYERS > i) ? new PlayerShip() : new AIShip());
				lShip.x = (shipsPerLine * (i % shipsPerLine) + 1) * stage.stageWidth / (2 + shipsPerLine);
				lShip.y = (i - (i % shipsPerLine) + 1) * stage.stageHeight / (N_SHIPS);
				lShip.rotation = (i % 2 == 0) ? 0 : 180;
			}
			if (N_SHIPS % 2 != 0)
			{
				GameContainer.instance.addChild(lShip = (N_PLAYERS == N_SHIPS) ? new PlayerShip() : new NeuralShip());
				lShip.x = 1 * stage.stageWidth / 2;
				lShip.y = (N_SHIPS - 1) / shipsPerLine * stage.stageHeight / (N_SHIPS / shipsPerLine);
				lShip.rotation = -90;
			}
			
			stage.addEventListener(Event.ENTER_FRAME, gameLoop);
		}
		
		protected static function gameLoop(pEvent:Event):void
		{
			var lClass:Class;
			for (var i:int = GAMELOOP_CLASSES.length - 1; i >= 0; i--)
			{
				lClass = GAMELOOP_CLASSES[i];
				for (var j:int = lClass.list.length - 1; j >= 0; j--)
				{
					lClass.list[j].gameLoop();
				}
			}
			
			if (Ship.list.length <= 1)
			{
				gameOver();
			}
			
			for (i = GameContainer.instance.numChildren - 1; i >= 0; i--)
			{
				GameContainer.instance.getChildAt(i).scaleX = 0.5;
				GameContainer.instance.getChildAt(i).scaleY = 0.5;
			}
		
		}
		
		protected static function gameOver()
		{
			stage.removeEventListener(Event.ENTER_FRAME, gameLoop);
			Genetic.nextChromosome();
		}
		
		public static function destroyAllInstances():void
		{
			var lClass:Class;
			for (var i = GAMELOOP_CLASSES.length - 1; i >= 0; i--)
			{
				lClass = GAMELOOP_CLASSES[i];
				for (var j = lClass.list.length - 1; j >= 0; j--)
				{
					lClass.list[j].destroy();
				}
			}
		}
	
	}

}