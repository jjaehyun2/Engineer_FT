package src.menu
{
	import flash.geom.Point;

	import net.fpp.common.starling.StaticAssetManager;
	import net.fpp.common.util.NumberUtil;

	import rv2.sound.SoundHandler;

	import src.assets.Fonts;
	import src.common.DataManager;
	import src.data.LevelResultVO;
	import src.menu.events.MenuEvent;

	import starling.display.Image;
	import starling.display.Sprite;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;
	import starling.text.TextField;
	import starling.text.TextFormat;
	import starling.utils.Align;

	public class LevelButton extends Sprite
	{
		private var _title:TextField;
		private var _score:TextField;

		private var _back:Image;
		private var _lockImage:Image;
		private var _starImage:Image;

		private var _touchPoint:Point = new Point;

		private var _id:uint;
		private var _packID:uint;

		private var _isLocked:Boolean = false;

		public function LevelButton( packID:uint, id:uint ):void
		{
			_packID = packID;
			_id = id;
			var levelData:LevelResultVO = DataManager.getLevelData( _packID, _id );
			useHandCursor = true;

			addChild( _back = new Image( StaticAssetManager.instance.getTexture( "level_button_base" ) ) );
			_back.x = LevelList.LEVEL_BUTTON_SIZE.x / 2 - _back.width / 2;
			_back.y = LevelList.LEVEL_BUTTON_SIZE.y - _back.height;

			var titleTextFormat:TextFormat = new TextFormat();
			titleTextFormat.font = Fonts.getAachenLightFont().name;
			titleTextFormat.size = 12;
			titleTextFormat.color = 0xFFFFFF;
			titleTextFormat.horizontalAlign = Align.CENTER;
			titleTextFormat.verticalAlign = Align.CENTER;

			addChild( _title = new TextField( width, 25, 'LEVEL ' + ( _id + 1 ), titleTextFormat ) );
			_title.touchable = false;
			_title.x = LevelList.LEVEL_BUTTON_SIZE.x / 2 - _title.width / 2;
			_title.y = -4;

			var scoreTextFormat:TextFormat = new TextFormat();
			scoreTextFormat.font = Fonts.getAachenLightFont().name;
			scoreTextFormat.size = 12;
			scoreTextFormat.color = 0xFFFF00;
			scoreTextFormat.horizontalAlign = Align.CENTER;
			scoreTextFormat.verticalAlign = Align.CENTER;

			addChild( _score = new TextField( width, 25, NumberUtil.formatNumber( levelData.score ), scoreTextFormat ) );
			_score.touchable = false;
			_score.x = LevelList.LEVEL_BUTTON_SIZE.x / 2 - _score.width / 2;
			_score.y = 33;

			pivotX = width / 2;
			pivotY = height / 2;

			if( levelData.isEnabled )
			{
				setStars( levelData.starCount );
			}
			else
			{
				lock();
			}
			resume();
		}

		private function setStars( $starCount:uint ):void
		{
			if( _starImage )
			{
				removeChild( _starImage, true );
				_starImage = null;
			}

			if( $starCount > 3 )
			{
				$starCount = 3;
			}

			if( $starCount > 0 )
			{
				if( _lockImage )
				{
					addChildAt( _starImage = new Image( StaticAssetManager.instance.getTexture( "level_button_stars_" + $starCount.toString() ) ), getChildIndex( _lockImage ) );
				}
				else
				{
					addChild( _starImage = new Image( StaticAssetManager.instance.getTexture( "level_button_stars_" + $starCount.toString() ) ) );
				}
				_starImage.x = 9.5;
				_starImage.y = 15.5;
			}
		}

		private function lock():void
		{
			_isLocked = true;
			pause();

			addChild( _lockImage = new Image( StaticAssetManager.instance.getTexture( "level_button_locked" ) ) );
			_lockImage.x = LevelList.LEVEL_BUTTON_SIZE.x / 2 - _back.width / 2;
			_lockImage.y = LevelList.LEVEL_BUTTON_SIZE.y - _back.height;

			_title.visible = false;
			_score.visible = false;

			useHandCursor = false;
			touchable = false;
		}

		private function unlock():void
		{
			_isLocked = false;
			resume();

			if( _lockImage )
			{
				removeChild( _lockImage, true );
				_lockImage = null;
			}

			_title.visible = true;
			_score.visible = true;

			useHandCursor = true;
			touchable = true;
		}

		private function onTouch( event:TouchEvent ):void
		{
			var tp:Touch = event.touches[ 0 ];
			if( tp.phase == TouchPhase.BEGAN )
			{
				scaleX = scaleY = .9;
				_touchPoint.setTo( tp.globalX, tp.globalY );
			}
			else if( tp.phase == TouchPhase.ENDED && scaleX != 1 )
			{
				scaleX = scaleY = 1;
				if( Math.sqrt( Math.pow( _touchPoint.x - tp.globalX, 2 ) + Math.pow( _touchPoint.y - tp.globalY, 2 ) ) < 20 )
				{
					SoundHandler.play( 'SND_BUTTON' );

					var menuEvent:MenuEvent = new MenuEvent( MenuEvent.NORMAL_GAME_REQUEST, [ _id, _packID ] );
					dispatchEvent( menuEvent );
				}
			}
		}

		public function pause():void
		{
			removeEventListener( TouchEvent.TOUCH, onTouch );
		}

		public function resume():void
		{
			if( !_isLocked )
			{
				addEventListener( TouchEvent.TOUCH, onTouch );
			}
		}

		override public function dispose():void
		{
			pause();

			removeChild( _back, true );
			_back = null;

			removeChild( _title, true );
			_title = null;

			removeChild( _score, true );
			_score = null;

			if( _lockImage )
			{
				removeChild( _lockImage, true );
				_lockImage = null;
			}

			if( _starImage )
			{
				removeChild( _starImage, true );
				_starImage = null;
			}

			super.dispose();
		}
	}
}