/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.zzznake.Menu.Command
{	
	import de.p3337.zzznake.Main.Zzznake;

	/**
	 * The ShowHighscoreRankingViewCommand provides an action to show the highscore.
	 */
	public class ShowHighscoreRankingViewCommand implements ICommand {
		
		/**
		 * Loads the HighscoreRankingView.
		 */
		public function execute():void {
			Zzznake.getInstance().setBackCommand(new ShowMenuCommand());
			Zzznake.getInstance().highscoreController.setHighscoreRankingViewAsCurrentView();
			Zzznake.getInstance().setView(Zzznake.getInstance().highscoreController.getView());
		}
	}
}