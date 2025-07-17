package
{
	import MyClases.InGame;
	import MyClases.Menu;
	
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.KeyboardEvent;
	
	[SWF(width="800",height="512")]
	
	public class SquareDeath extends Sprite
	{
		protected var MyMenu:Menu = new Menu();
		protected var MyGame:InGame = new InGame();
		
		public function SquareDeath()
		{
			
			MyMenu.addEventListener("IWantToPlay", GoToPlay);
			
			addChild( MyMenu );
			
			stage.addEventListener(Event.ENTER_FRAME, UpdateGame);
			
		}
		
		protected function UpdateGame(event:Event):void
		{
			if( contains(MyGame) )
			{
				stage.addEventListener(KeyboardEvent.KEY_DOWN, ProcessPlayerMovement);
				stage.addEventListener(KeyboardEvent.KEY_UP, StopProcessPlayerMovement);
				MyGame.MoveEnemies();
				MyGame.ProcessEnemies();
				addChild( MyGame );
			}
		}
		
		protected function StopProcessPlayerMovement(event:KeyboardEvent):void
		{
			MyGame.StopProcessPlayerMoves(event);
		}
		
		protected function ProcessPlayerMovement(event:KeyboardEvent):void
		{
			MyGame.ProcessPlayerMoves(event);
		}
		
		protected function GoToPlay(event:Event):void
		{
			if(contains(MyMenu))
			{
				removeChild( MyMenu );
			}
			addChild( MyGame );
			stage.focus = stage;
		}
		
	}
}