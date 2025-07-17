package
{
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;
	
	public class MainMenu extends MovieClip
	{
		var p;
		function MainMenu()
		{
			p = false;
			addEventListener(Event.ENTER_FRAME,enterFrame);
		}
		function enterFrame(e:Event)
		{
			if(p == false)
			{
				if(options!= null)
				{
					options.buttonMode = true;
					newGame.buttonMode = true;
					options.addEventListener(MouseEvent.MOUSE_UP,Options);
					newGame.addEventListener(MouseEvent.MOUSE_UP,NewGame);
					p = true;
				}
				
			}
			if(currentFrame == totalFrames)
			{
				stop();
			}
		}
		function Options(e:MouseEvent)
		{
			var optionsScreen = new OptionsScreen("Nope");
			addChild(optionsScreen);
		}
		function NewGame(e:MouseEvent)
		{
			
			var loadMenu = new LoadMenu();
			addChild(loadMenu);
			
		}
		function remove()
		{
			options.removeEventListener(MouseEvent.MOUSE_UP,Options);
			newGame.removeEventListener(MouseEvent.MOUSE_UP,NewGame);
			removeEventListener(Event.ENTER_FRAME,enterFrame);
			parent.removeChild(this);
		}
	}
}