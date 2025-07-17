/**
 * Created by newkrok on 12/09/16.
 */
package net.fpp.pandastory.game.module.charactercontroller.view
{
	import net.fpp.common.starling.StaticAssetManager;
	import net.fpp.common.starling.module.AModel;
	import net.fpp.common.starling.module.AModuleView;
	import net.fpp.pandastory.constant.CSkinId;
	import net.fpp.pandastory.game.module.charactercontroller.CharacterControllerModel;

	import starling.display.Button;
	import starling.events.KeyboardEvent;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;

	CONFIG::IS_KEY_CONTROL_ENABLED
	{
		import flash.ui.Keyboard;
	}

	public class CharacterControllerModuleView extends AModuleView
	{
		private var _characterControllerModel:CharacterControllerModel;

		private var _leftButton:Button;
		private var _rightButton:Button;
		private var _jumpButton:Button;

		public function CharacterControllerModuleView()
		{
		}

		override public function setModel( model:AModel ):void
		{
			this._characterControllerModel = model as CharacterControllerModel;

			super.setModel( model );
		}

		override protected function onInit():void
		{
			super.onInit();

			this._leftButton = new Button( StaticAssetManager.instance.getTexture( CSkinId.LEFT_BUTTON ) );
			this._leftButton.addEventListener( TouchEvent.TOUCH, this.onLeftButtonTouched );
			this.addChild( this._leftButton );

			this._rightButton = new Button( StaticAssetManager.instance.getTexture( CSkinId.RIGHT_BUTTON ) );
			this._rightButton.addEventListener( TouchEvent.TOUCH, this.onRightButtonTouched );
			this.addChild( this._rightButton );

			this._jumpButton = new Button( StaticAssetManager.instance.getTexture( CSkinId.JUMP_BUTTON ) );
			this._jumpButton.addEventListener( TouchEvent.TOUCH, this.onJumpButtonTouched );
			this.addChild( this._jumpButton );

			const margin:Number = 10;

			this._leftButton.x = margin;
			this._leftButton.y = this.stage.stageHeight - this._leftButton.height - margin;

			this._rightButton.x = this._leftButton.x + this._leftButton.width + margin;
			this._rightButton.y = this._leftButton.y;

			this._jumpButton.x = this.stage.stageWidth - this._jumpButton.width - margin;
			this._jumpButton.y = this._leftButton.y;

			CONFIG::IS_KEY_CONTROL_ENABLED
			{
				this.stage.addEventListener( KeyboardEvent.KEY_DOWN, this.onKeyDownHandler );
				this.stage.addEventListener( KeyboardEvent.KEY_UP, this.onKeyUpHandler );
			}
		}

		private function onLeftButtonTouched( e:TouchEvent ):void
		{
			var touch:Touch = e.getTouch( this._leftButton );
			if ( !touch )
			{
				return;
			}

			if( touch.phase == TouchPhase.BEGAN )
			{
				this._characterControllerModel.isLeftActive = true;
			}
			else if( touch.phase == TouchPhase.ENDED )
			{
				this._characterControllerModel.isLeftActive = false;
			}
		}

		private function onRightButtonTouched( e:TouchEvent ):void
		{
			var touch:Touch = e.getTouch( this._rightButton );
			if ( !touch )
			{
				return;
			}

			if( touch.phase == TouchPhase.BEGAN )
			{
				this._characterControllerModel.isRightActive = true;
			}
			else if( touch.phase == TouchPhase.ENDED )
			{
				this._characterControllerModel.isRightActive = false;
			}
		}

		private function onJumpButtonTouched( e:TouchEvent ):void
		{
			var touch:Touch = e.getTouch( this._jumpButton );
			if ( !touch )
			{
				return;
			}

			if( touch.phase == TouchPhase.BEGAN )
			{
				this._characterControllerModel.isJumpActive = true;
			}
			else if( touch.phase == TouchPhase.ENDED )
			{
				this._characterControllerModel.isJumpActive = false;
			}
		}

		CONFIG::IS_KEY_CONTROL_ENABLED
		{
			private function onKeyDownHandler( e:KeyboardEvent ):void
			{
				switch( e.keyCode )
				{
					case Keyboard.LEFT:
						this._characterControllerModel.isLeftActive = true;
						break;
					case Keyboard.RIGHT:
						this._characterControllerModel.isRightActive = true;
						break;
					case Keyboard.UP:
						this._characterControllerModel.isJumpActive = true;
						break;
				}
			}

			private function onKeyUpHandler( e:KeyboardEvent ):void
			{
				switch( e.keyCode )
				{
					case Keyboard.LEFT:
						this._characterControllerModel.isLeftActive = false;
						break;
					case Keyboard.RIGHT:
						this._characterControllerModel.isRightActive = false;
						break;
					case Keyboard.UP:
						this._characterControllerModel.isJumpActive = false;
						break;
				}
			}
		}

		override public function dispose():void
		{
			CONFIG::IS_KEY_CONTROL_ENABLED
			{
				this.stage.removeEventListener( KeyboardEvent.KEY_DOWN, this.onKeyDownHandler );
				this.stage.removeEventListener( KeyboardEvent.KEY_UP, this.onKeyUpHandler );
			}

			this._leftButton.removeEventListener( TouchEvent.TOUCH, this.onLeftButtonTouched );
			this._rightButton.removeEventListener( TouchEvent.TOUCH, this.onRightButtonTouched );
			this._jumpButton.removeEventListener( TouchEvent.TOUCH, this.onJumpButtonTouched );

			super.dispose();
		}
	}
}