/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.zzznake.Menu.Controller
{
	import flash.events.MouseEvent;
	
	import flash.display.Sprite;
	
	import de.p3337.zzznake.Main.Zzznake;
	import de.p3337.zzznake.Menu.Command.ICommand;
	import de.p3337.zzznake.Menu.Command.ShowHighscoreRankingViewCommand;
	import de.p3337.zzznake.Menu.Command.StartNewGameCommand;
	import de.p3337.zzznake.Menu.View.MenuView;
	import de.p3337.zzznake.Sound.Jukebox;

	/**
	 * The MenuController handles the user interactions with buttons provided by the MenuView.  
	 */
	public class MenuController {
		
		private var view:MenuView;
		
		public function MenuController() {
			this.view = new MenuView();
			
			var startNewGameCmd:StartNewGameCommand = new StartNewGameCommand();
			this.view.startGameBtn.addEventListener(MouseEvent.CLICK, function():void {
				ExecuteCommand(startNewGameCmd);
			});
			
			var showHighscoreCmd:ShowHighscoreRankingViewCommand = new ShowHighscoreRankingViewCommand();
			this.view.openHighscoreBtn.addEventListener(MouseEvent.CLICK, function():void {
				ExecuteCommand(showHighscoreCmd);
			});
		}
		
		public function getView():Sprite {
			return view.view;
		}
		
		public function ExecuteCommand(command:ICommand):void {
			Jukebox.getInstance().stop();
			de.p3337.zzznake.Main.Zzznake.getInstance().removeChildren();
			command.execute();
			de.p3337.zzznake.Main.Zzznake.getInstance().stage.focus = de.p3337.zzznake.Main.Zzznake.getInstance().stage;
		}
	}
}