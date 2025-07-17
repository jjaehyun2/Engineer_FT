package src.menu
{
	import caurina.transitions.Tweener;

	import net.fpp.common.starling.StaticAssetManager;

	import rv2.sound.SoundHandler;

	import src.AbstractPanel;
	import src.menu.events.MenuEvent;

	import starling.core.Starling;
	import starling.display.Button;
	import starling.events.Event;

	public class MainMenu extends AbstractPanel
	{
		private var _playGameButton:Button;
		private var _toplistButton:Button;
		private var _facebookButton:Button;
		private var _twitterButton:Button;
		private var _optionsButton:Button;
		private var _homeButton:Button;

		public function MainMenu():void
		{
		}

		override public function init():void
		{
			var baseDelay:Number = 1;
			var margin:Number = 10;

			addChild( _playGameButton = new Button( StaticAssetManager.instance.getTexture( "play_game_button" ) ) );
			_playGameButton.name = "startGameRequest";
			_playGameButton.x = stage.stageWidth / 2;
			_playGameButton.y = stage.stageHeight / 2 + 30;
			_playGameButton.pivotX = _playGameButton.width / 2;
			_playGameButton.pivotY = _playGameButton.height / 2;
			_playGameButton.alpha = 0;
			_playGameButton.scaleX = _playGameButton.scaleY = .5;
			Tweener.addTween( _playGameButton, {delay: 1.5, time: .5, scaleX: 1, scaleY: 1, alpha: 1} );

			addChild( _toplistButton = new Button( StaticAssetManager.instance.getTexture( "toplist_button" ) ) );
			_toplistButton.name = "toplist";
			_toplistButton.x = margin;
			_toplistButton.y = Starling.current.stage.stageHeight;
			Tweener.addTween( _toplistButton, {
				delay: baseDelay + Math.random() * .5,
				time: .5,
				y: Starling.current.stage.stageHeight - _toplistButton.height - margin
			} );

			addChild( _facebookButton = new Button( StaticAssetManager.instance.getTexture( "facebook_button" ) ) );
			_facebookButton.name = "facebook";
			_facebookButton.x = Starling.current.stage.stageWidth;
			_facebookButton.y = margin;
			Tweener.addTween( _facebookButton, {
				delay: baseDelay + Math.random() * .5,
				time: .5,
				x: Starling.current.stage.stageWidth - _facebookButton.width - margin
			} );

			// Egyenlore a twitter gomb kikapcsolva
			addChild( _twitterButton = new Button( StaticAssetManager.instance.getTexture( "twitter_button" ) ) );
			_twitterButton.visible = false;
			_twitterButton.name = "twitter";
			_twitterButton.x = Starling.current.stage.stageWidth;
			_twitterButton.y = _facebookButton.y + _facebookButton.height + margin;
			Tweener.addTween( _twitterButton, {
				delay: baseDelay + Math.random() * .5,
				time: .5,
				x: Starling.current.stage.stageWidth - _twitterButton.width - margin
			} );

			addChild( _optionsButton = new Button( StaticAssetManager.instance.getTexture( "options_button" ) ) );
			_optionsButton.name = "options";
			_optionsButton.x = Starling.current.stage.stageWidth - _optionsButton.width - margin;
			_optionsButton.y = Starling.current.stage.stageHeight;
			Tweener.addTween( _optionsButton, {
				delay: baseDelay + Math.random() * .5,
				time: .5,
				y: Starling.current.stage.stageHeight - _optionsButton.height - margin
			} );

			addChild( _homeButton = new Button( StaticAssetManager.instance.getTexture( "home_button" ) ) );
			_homeButton.name = "home";
			_homeButton.x = -_optionsButton.width;
			_homeButton.y = margin;
			Tweener.addTween( _homeButton, {delay: baseDelay + Math.random() * .5, time: .5, x: margin} );

			Tweener.addTween( this, {time: 1, onComplete: inited} );
		}

		private function inited():void
		{
			resume();
		}

		private function onButtonTriggered( event:Event ):void
		{
			SoundHandler.play( 'SND_BUTTON' );

			var button:Button = event.target as Button;
			var needPauseTheApp:Boolean = true;

			switch( button.name )
			{
				case "startGameRequest":
					dispatchEvent( new MenuEvent( MenuEvent.NORMAL_GAME_REQUEST ) );
					break;
				case "toplist":
					MountainMonsterIOSMain.openToplist();
					needPauseTheApp = false;
					break;
				case "achievements":
					MountainMonsterIOSMain.openAchievements();
					needPauseTheApp = false;
					break;
				case "facebook":
					MountainMonsterIOSMain.facebookRequest();
					needPauseTheApp = false;
					break;
				case "options":
					dispatchEvent( new MenuEvent( MenuEvent.OPTIONS_REQUEST ) );
					break;
				case "home":
					MountainMonsterIOSMain.goToHome();
					needPauseTheApp = false;
					break;
			}

			if( needPauseTheApp )
			{
				pause();
			}
		}

		public function pause():void
		{
			removeEventListener( Event.TRIGGERED, onButtonTriggered );
			touchable = false;
		}

		public function resume():void
		{
			addEventListener( Event.TRIGGERED, onButtonTriggered );
			touchable = true;
		}

		override public function dispose():void
		{
			pause();

			Tweener.removeTweens( _playGameButton );
			removeChild( _playGameButton, true );
			_playGameButton = null;

			Tweener.removeTweens( _toplistButton );
			removeChild( _toplistButton, true );
			_toplistButton = null;

			Tweener.removeTweens( _facebookButton );
			removeChild( _facebookButton, true );
			_facebookButton = null;

			Tweener.removeTweens( _twitterButton );
			removeChild( _twitterButton, true );
			_twitterButton = null;

			Tweener.removeTweens( _optionsButton );
			removeChild( _optionsButton, true );
			_optionsButton = null;

			Tweener.removeTweens( _homeButton );
			removeChild( _homeButton, true );
			_homeButton = null;

			super.dispose();
		}
	}
}