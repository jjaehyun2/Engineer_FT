/**
 * Created by newkrok on 23/09/15.
 */
package src.menu.module.rating.view
{
	import net.fpp.common.starling.StaticAssetManager;
	import net.fpp.common.starling.module.AModuleView;

	import src.assets.Fonts;
	import src.menu.module.rating.events.RatingModuleEvent;

	import starling.display.Button;

	import starling.display.Image;
	import starling.display.Quad;

	import starling.display.Sprite;
	import starling.events.Event;
	import starling.text.TextField;
	import starling.text.TextFormat;

	public class RatingModuleView extends AModuleView
	{
		private var _elementContainer:Sprite;

		private var _background:Image;
		private var _darkBackground:Quad;
		private var _title:TextField;

		private var _rateButton:Button;
		private var _notNowButton:Button;
		private var _neverButton:Button;

		override protected function onInit():void
		{
			this.createElements();
			this.setElementContainerPosition();
		}

		private function createElements():void
		{
			this._darkBackground = new Quad( this.stage.stageWidth, this.stage.stageHeight, 0x000000 );
			this._darkBackground.width = this.stage.stageWidth;
			this._darkBackground.height = this.stage.stageHeight;
			this._darkBackground.alpha = .5;
			this.addChild( this._darkBackground );

			_elementContainer = new Sprite();
			addChild( _elementContainer );

			_background = new Image( StaticAssetManager.instance.getTexture( 'panel_background' ) );
			_elementContainer.addChild( _background );

			var titleTextFormat:TextFormat = new TextFormat();
			titleTextFormat.font = Fonts.getAachenLightFont().name;
			titleTextFormat.size = 18;
			titleTextFormat.color = 0xFFFFFF;

			this._title = new TextField( this._background.width, 50, "DO YOU LIKE THIS GAME?\nDON'T FORGET RATE FOR IT!", titleTextFormat );
			this._title.autoSize = 'center';
			this._title.x = this._background.width / 2 - this._title.width / 2;
			this._title.y = 10;
			this._elementContainer.addChild( this._title );

			var buttonTextFormat:TextFormat = new TextFormat();
			buttonTextFormat.font = Fonts.getAachenLightFont().name;
			buttonTextFormat.size = 18;
			buttonTextFormat.color = 0xFFFFFF;

			_elementContainer.addChild( _rateButton = new Button( StaticAssetManager.instance.getTexture ( "base_button" ), "RATE!" ) );
			_rateButton.textFormat = buttonTextFormat;
			_rateButton.x = _elementContainer.width / 2 - _rateButton.width / 2;
			_rateButton.y = 50;
			_rateButton.addEventListener( Event.TRIGGERED, rateRequest );

			_elementContainer.addChild( _notNowButton = new Button( StaticAssetManager.instance.getTexture ( "base_button" ), "NOT NOW" ) );
			_notNowButton.textFormat = buttonTextFormat;
			_notNowButton.x = _elementContainer.width / 2 - _rateButton.width / 2;
			_notNowButton.y = _rateButton.y + _rateButton.height;
			_notNowButton.addEventListener( Event.TRIGGERED, rateLaterRequest );

			_elementContainer.addChild( _neverButton = new Button( StaticAssetManager.instance.getTexture ( "base_button" ), "NEVER!" ) );
			_neverButton.textFormat = buttonTextFormat;
			_neverButton.x = _elementContainer.width / 2 - _neverButton.width / 2;
			_neverButton.y = _notNowButton.y + _notNowButton.height;
			_neverButton.addEventListener( Event.TRIGGERED, rateNeverRequest );
		}

		private function rateRequest():void
		{
			dispatchEvent( new RatingModuleEvent( RatingModuleEvent.RATE_REQUEST ) );
		}

		private function rateLaterRequest():void
		{
			dispatchEvent( new RatingModuleEvent( RatingModuleEvent.RATE_LATER_REQUEST ) );
		}

		private function rateNeverRequest():void
		{
			dispatchEvent( new RatingModuleEvent( RatingModuleEvent.RATE_NEVER_REQUEST ) );
		}

		private function setElementContainerPosition():void
		{
			_elementContainer.x = stage.stageWidth / 2 - _elementContainer.width / 2;
			_elementContainer.y = stage.stageHeight / 2 - _elementContainer.height / 2;
		}

		override public function dispose():void
		{
			this._elementContainer.removeFromParent( true );
			this._elementContainer = null;

			this._darkBackground.removeFromParent( true );
			this._darkBackground = null;

			this._background.removeFromParent( true );
			this._background = null;

			this._title.removeFromParent( true );
			this._title = null;

			this._rateButton.removeFromParent( true );
			this._rateButton = null;

			this._notNowButton.removeFromParent( true );
			this._notNowButton = null;

			this._neverButton.removeFromParent( true );
			this._neverButton = null;

			super.dispose();
		}
	}
}