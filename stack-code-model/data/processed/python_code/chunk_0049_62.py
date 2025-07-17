/**
 * Created by newkrok on 16/10/16.
 */
package net.fpp.pandastory.game.module.synccharactermodule
{
	import net.fpp.common.starling.module.AModel;
	import net.fpp.pandastory.game.module.characteranimation.ICharacterAnimationModule;
	import net.fpp.pandastory.vo.CharacterVO;

	public class SyncCharacterModel extends AModel
	{
		private var _characterAnimationModule:ICharacterAnimationModule;

		private var _state:String;
		private var _direction:int;
		private var _characterVO:CharacterVO;

		public var x:Number = 0;
		public var y:Number = 0;

		public function setCharacterAnimationModule( value:ICharacterAnimationModule ):void
		{
			this._characterAnimationModule = value;
		}

		public function getCharacterAnimationModule():ICharacterAnimationModule
		{
			return this._characterAnimationModule;
		}

		public function setState( value:String ):void
		{
			this._state = value;
		}

		public function getState():String
		{
			return this._state;
		}

		public function setDirection( value:int ):void
		{
			this._direction = value;
		}

		public function setCharacterVO( value:CharacterVO ):void
		{
			this._characterVO = value;
		}

		public function getCharacterVO():CharacterVO
		{
			return this._characterVO;
		}

		public function getDirection():int
		{
			return this._direction;
		}
	}
}