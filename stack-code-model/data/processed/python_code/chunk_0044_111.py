/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.straightouttaspace.Views.Screens.HUD
{
	import flash.display.Sprite;
	
	import de.p3337.straightouttaspace.Objects.Players.Player;
	import de.p3337.straightouttaspace.Views.Screens.IScreen;
	import de.p3337.straightouttaspace.Views.Screens.PlayScreen;
	
	public class HudScreen implements IScreen
	{
		private var parent:PlayScreen;
		private var _view:Sprite = new Sprite();
		private var playerLivesView:PlayerLivesView;
		private var highscoreView:HighscoreView;
		private var weaponPowerView:WeaponPowerView;
		
		public function HudScreen(parent:PlayScreen)
		{
			this.parent = parent;
			draw();
		}
		
		private function draw():void
		{
			// add highscore to top center
			this.highscoreView = new HighscoreView(this.parent.stage);
			this.highscoreView.y = 10;
			_view.addChild(this.highscoreView);
			
			// add player lives status to bottom left
			this.playerLivesView = new PlayerLivesView(this.parent.stage);
			this.playerLivesView.x = 5;
			this.playerLivesView.y = this.parent.stage.stageHeight - playerLivesView.height;
			_view.addChild(this.playerLivesView);
			
			// add weapon power status to bottom right
			this.weaponPowerView = new WeaponPowerView(this.parent.stage);
			this.weaponPowerView.x = this.parent.stage.stageWidth - weaponPowerView.width - 5;
			this.weaponPowerView.y = this.parent.stage.stageHeight - weaponPowerView.height;
			_view.addChild(this.weaponPowerView);
		}
		
		/**
		 * @inheritDoc
		 */
		public function get view():Sprite
		{
			return _view;
		}
		
		/**
		 * @inheritDoc
		 */
		public function update():void
		{
			if(this.parent.game != null)
			{
				var player:Player = this.parent.game.board.player;
				
				this.playerLivesView.updatePlayerLives(player.spaceshipVector[0].shieldStrength);
				this.highscoreView.updateMyScore(player.score);
				this.highscoreView.updateHighScore(this.parent.game.main.highscore.getScore());
				this.weaponPowerView.updateWeaponPower(player.spaceshipVector[0].weaponPower);
			}
		}
		
		/**
		 * @inheritDoc
		 */
		public function destroy():void
		{
			this.playerLivesView.destroy();
			this.playerLivesView = null;
			this.highscoreView.destroy();
			this.highscoreView = null;
			this.weaponPowerView.destroy();
			this.weaponPowerView = null;
			this._view.removeChildren();
		}
	}
}