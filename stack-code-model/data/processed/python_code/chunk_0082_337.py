/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.zzznake.Highscore.Controller
{
	import flash.events.EventDispatcher;
	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;
	
	import flash.display.Sprite;
	
	import de.p3337.zzznake.Game.GameEvent;
	import de.p3337.zzznake.Highscore.Model.HighscoreModel;
	import de.p3337.zzznake.Highscore.View.HighscoreNewEntryView;
	import de.p3337.zzznake.Highscore.View.HighscoreRankingView;
	import de.p3337.zzznake.Main.Zzznake;
	import de.p3337.zzznake.Menu.Command.ShowHighscoreRankingViewCommand;
	import de.p3337.zzznake.Sound.Jukebox;

	/**
	 * The HighscoreController handles the user interactions with buttons to store a new entry or to close the high score table.  
	 */
	public class HighscoreController extends EventDispatcher {
		
		private var model:HighscoreModel;
		
		private var view:Sprite;
		private var highscoreRankingView:HighscoreRankingView;
		private var highscoreNewEntryView:HighscoreNewEntryView;
		
		/**
		 * Creates a new HighscoreController.
		 * 
		 * @param HighscoreModel
		 */
		public function HighscoreController(highscoreModel:HighscoreModel) {
			model = highscoreModel;
			createHighscoreRankingView();
			createHighscoreNewEntryView();
		}
		
		public function setHighscoreRankingViewAsCurrentView():void {
			Jukebox.getInstance().stop();
			view = highscoreRankingView.view;
		}
		
		public function setHighscoreNewEntryViewAsCurrentView():void {
			view = highscoreNewEntryView.view;
		}
		
		public function setFocusToNewEntryInputField():void {
			Zzznake.getInstance().stage.focus = highscoreNewEntryView.highscoreInput.getInputTextField();
		}
		
		public function getView():Sprite {
			return view;
		}
		
		public function createHighscoreRankingView():void {
			highscoreRankingView = new HighscoreRankingView(model);
			highscoreRankingView.backButton.addEventListener(MouseEvent.CLICK, function():void {
				Zzznake.getInstance().showMenu();
			});
			model.addEventListener(GameEvent.GAME_UPDATE, highscoreRankingView.update);
		}
		
		public function createHighscoreNewEntryView():void {
			highscoreNewEntryView = new HighscoreNewEntryView(model);
			highscoreNewEntryView.saveButton.addEventListener(MouseEvent.CLICK, function():void {
				storeEntry();
			});
			highscoreNewEntryView.highscoreInput.getInputTextField().addEventListener(KeyboardEvent.KEY_DOWN, inputTextFieldOnKeyEnter);
			model.addEventListener(GameEvent.GAME_UPDATE, highscoreNewEntryView.update);
		}
		
		private function inputTextFieldOnKeyEnter(event:KeyboardEvent):void {
			if(event.charCode == 13) {
				Zzznake.getInstance().stage.focus = Zzznake.getInstance().stage;
				storeEntry();
			}
		}
		
		/**
		 * Stores the specified username and its score and redirects to the highscore table. 
		 */
		public function storeEntry():void {
			var username:String = highscoreNewEntryView.getUsername();
			username = (username.length > 0)? username : 'Unknown';
			model.storeNewEntry(username);
			Zzznake.getInstance().ExecuteCommand(new ShowHighscoreRankingViewCommand());
		}
	}
}