package
{
	import flash.display.MovieClip;
	import flash.events.MouseEvent;
	import flash.events.Event;
	public class LevelComplete extends MovieClip
	{
		public function LevelComplete(UnlockedWeapon,UnlockedLevel)
		{
			newCannon.visible = false;
			newLevel.visible = false;
			/*if(UnlockedWeapon == "None")
			{
				newCannon.visible = false;
			}
			if(UnlockedLevel == false)
			{
				newLevel.visible = false;
			}*/
			cont.buttonMode = true;
			restart.buttonMode = true;
			cont.addEventListener(MouseEvent.MOUSE_UP,ReturnMainMenu);
			restart.addEventListener(MouseEvent.MOUSE_UP,RestartLevel);
			Score.text = "Level Score: "+Main.LevelScore[Game.level];
		}
		public function remove()
		{
			cont.removeEventListener(MouseEvent.MOUSE_UP,ReturnMainMenu);
			restart.removeEventListener(MouseEvent.MOUSE_UP,RestartLevel);
			parent.removeChild(this);
		}
		function ReturnMainMenu(e:MouseEvent)
		{
			var game = parent;
			var main = Main.main;
			main.changeSong("MainMenuSong");
			
			main.SpawnLevelSelect();
			remove();
		}
		function RestartLevel(e:MouseEvent)
		{
			var game = parent;
			remove();
			
			game.RestartLevel();
		}
	}
}