package
{
	import flash.display.MovieClip;
	import flash.events.MouseEvent;
	import flash.display.Stage;
	public class PauseScreen extends MovieClip
	{
		public var mainMenuButton:MovieClip;
		function PauseScreen()
		{
			resumeGame.addEventListener(MouseEvent.MOUSE_UP,ResumeGame)
			mainMenuButton.addEventListener(MouseEvent.MOUSE_UP,ReturnMainMenu);
			restartLevel.addEventListener(MouseEvent.MOUSE_UP,RestartLevel);
			sOn.addEventListener(MouseEvent.MOUSE_UP,soundOn);
			sOff.addEventListener(MouseEvent.MOUSE_UP,soundOff);
			mOn.addEventListener(MouseEvent.MOUSE_UP,musicOn);
			mOff.addEventListener(MouseEvent.MOUSE_UP,musicOff);
			high.addEventListener(MouseEvent.MOUSE_UP,gHigh);
			low.addEventListener(MouseEvent.MOUSE_UP,gLow);
			if(Main.sounds == true)sOff.alpha = 0.5; else sOn.alpha = 0.5;
			if(Main.music == true)mOff.alpha = 0.5; else mOn.alpha = 0.5;
			if(Main.gfx == true)low.alpha = 0.5; else high.alpha = 0.5;
			resumeGame.buttonMode = true;
			sOn.buttonMode = true;
			sOff.buttonMode = true;
			mOn.buttonMode = true;
			mOff.buttonMode = true;
			mainMenuButton.buttonMode = true;
			restartLevel.buttonMode = true;
			
		}
		function ResumeGame(e:MouseEvent)
		{
			var game = parent;
			game.ResumeAll();
		}
		function RestartLevel(e:MouseEvent)
		{
			var game = parent;
			game.RestartLevel();
			remove()
		}
		function gHigh(e:MouseEvent)
		{
			
			Main.gfx = true;
			var main = Main.main;
			main.SaveOptions();
			low.alpha = 0.5;
			high.alpha = 1;
			stage.quality = "HIGH"
		}
		function gLow(e:MouseEvent)
		{
			Main.gfx = false;
			var main = Main.main;
			main.SaveOptions();
			high.alpha = 0.5;
			low.alpha = 1;
			stage.quality = "LOW"
		}
		function ReturnMainMenu(e:MouseEvent)
		{
			var game = parent;
			var main = Main.main;
			main.changeSong("MainMenuSong");
			main.SpawnLevelSelect();
		}
		function remove()
		{
			resumeGame.removeEventListener(MouseEvent.MOUSE_UP,ResumeGame)
			restartLevel.removeEventListener(MouseEvent.MOUSE_UP,RestartLevel);
			mainMenuButton.removeEventListener(MouseEvent.MOUSE_UP,ReturnMainMenu);
			sOn.removeEventListener(MouseEvent.MOUSE_UP,soundOn);
			sOff.removeEventListener(MouseEvent.MOUSE_UP,soundOff);
			mOn.removeEventListener(MouseEvent.MOUSE_UP,musicOn);
			mOff.removeEventListener(MouseEvent.MOUSE_UP,musicOff);
			parent.removeChild(this);
		}
		function soundOn(e:MouseEvent)
		{
			var main = Main.main;
			Main.sounds = true;
			main.SaveOptions();
			sOn.alpha = 1;
			sOff.alpha = 0.5;
			
		}
		function soundOff(e:MouseEvent)
		{
			var main = Main.main;
			Main.sounds = false;
			main.SaveOptions();
			sOn.alpha = 0.5;
			sOff.alpha = 1;
			
		}
		function musicOn(e:MouseEvent)
		{
			Sounds.PlayMusic();
			mOn.alpha = 1;
			mOff.alpha = 0.5;
			Main.music = true;
			var main = Main.main;
			main.SaveOptions();
		}
		function musicOff(e:MouseEvent)
		{
			Sounds.StopMusic();
			mOn.alpha = 0.5;
			mOff.alpha = 1;
			Main.music = false;
			var main = Main.main;
			main.SaveOptions();
		}
	}
	
}