/**
 * Created by newkrok on 12/09/16.
 */
package net.fpp.pandastory.game.module.character
{
	import Box2D.Dynamics.b2Body;

	import net.fpp.common.starling.module.AModel;
	import net.fpp.pandastory.game.module.characteranimation.ICharacterAnimationModule;
	import net.fpp.pandastory.vo.CharacterVO;

	public class CharacterModel extends AModel
	{
		public var characterPhysicsObject:b2Body;
		public var characterRadiusPhysicsObject:b2Body;

		private var _characterAnimationModule:ICharacterAnimationModule;

		private var _state:String;
		private var _direction:int;

		private var _isOnGround:Boolean;

		private var _characterVO:CharacterVO;

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

		public function setIsOnGround( value:Boolean ):void
		{
			this._isOnGround = value;
		}

		public function getIsOnGround():Boolean
		{
			return this._isOnGround;
		}

		public function setDirection( value:int ):void
		{
			this._direction = value;
		}

		public function getDirection():int
		{
			return this._direction;
		}

		public function setCharacterVO( value:CharacterVO ):void
		{
			this._characterVO = value;
		}

		public function getCharacterVO():CharacterVO
		{
			return this._characterVO;
		}
	}
}