package
{
	import flash.display.MovieClip;
	import flash.events.MouseEvent;
	import flash.events.Event;
	public class MissionFailed extends MovieClip
	{
		public function MissionFailed()
		{
			cont.buttonMode = true;
			restart.buttonMode = true;
			cont.addEventListener(MouseEvent.MOUSE_UP,ReturnMainMenu);
			restart.addEventListener(MouseEvent.MOUSE_UP,RestartLevel);
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
			remove();
			main.SpawnLevelSelect();
		}
		function RestartLevel(e:MouseEvent)
		{
			var game = parent;
			remove();
			
			game.RestartLevel();
		}
	}
}