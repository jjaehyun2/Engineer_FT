/**
 * Created by newkrok on 16/10/16.
 */
package net.fpp.pandastory.game.module.synccharactermodule
{
	import com.greensock.TweenLite;
	import com.greensock.easing.Linear;

	import net.fpp.common.starling.module.AModule;
	import net.fpp.pandastory.game.module.characteranimation.ICharacterAnimationModule;
	import net.fpp.pandastory.game.module.synccharactermodule.view.SyncCharacterModuleView;
	import net.fpp.pandastory.vo.CharacterVO;

	import starling.display.DisplayObjectContainer;

	public class SyncCharacterModule extends AModule implements ISyncCharacterModule
	{
		[Inject]
		public var characterAnimationModule:ICharacterAnimationModule;

		[Inject(id='worldView')]
		public var worldView:DisplayObjectContainer;

		private var _syncCharacterModuleView:SyncCharacterModuleView;
		private var _syncCharacterModel:SyncCharacterModel;

		public function SyncCharacterModule()
		{
			this._syncCharacterModuleView = this.createModuleView( SyncCharacterModuleView ) as SyncCharacterModuleView;
			this._syncCharacterModuleView.visible = false;

			this._syncCharacterModel = this.createModel( SyncCharacterModel ) as SyncCharacterModel;
		}

		override public function onInited():void
		{
			this._syncCharacterModel.setCharacterAnimationModule( this.characterAnimationModule );

			this.worldView.addChild( this._syncCharacterModuleView );

			this._syncCharacterModuleView.init();
		}

		public function setCharacterDirection( value:int ):void
		{
			if( this._syncCharacterModel.getDirection() != value )
			{
				this._syncCharacterModel.setDirection( value );

				this._syncCharacterModuleView.updateDirection();
			}
		}

		public function setCharacterState( value:String ):void
		{
			if( this._syncCharacterModel.getState() != value )
			{
				this._syncCharacterModel.setState( value );

				this._syncCharacterModuleView.updateState();
			}
		}

		public function setPosition( x:Number, y:Number ):void
		{
			this._syncCharacterModel.x = x;
			this._syncCharacterModel.y = y;

			TweenLite.killTweensOf( this._syncCharacterModuleView );
			TweenLite.to( this._syncCharacterModuleView, .1, {x: x, y: y, ease: Linear.ease} );
		}

		public function getXPosition():Number
		{
			return this._syncCharacterModel.x;
		}

		public function getYPosition():Number
		{
			return this._syncCharacterModel.y;
		}

		public function setCharacterVO( value:CharacterVO ):void
		{
			this._syncCharacterModel.setCharacterVO( value );
			this._syncCharacterModuleView.updateSkin();

			this._syncCharacterModuleView.visible = true;
		}

		override public function dispose():void
		{
			super.dispose();

			this.characterAnimationModule = null;
			this.worldView = null;
			this._syncCharacterModuleView = null;
			this._syncCharacterModel = null;
		}
	}
}