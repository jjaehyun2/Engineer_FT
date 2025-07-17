/**
 * Created by newkrok on 12/09/16.
 */
package net.fpp.pandastory.game.module.charactercontroller
{
	import Box2D.Common.Math.b2Vec2;
	import Box2D.Dynamics.b2Body;

	import net.fpp.common.starling.module.AModule;
	import net.fpp.pandastory.game.module.character.ICharacterModule;
	import net.fpp.pandastory.game.module.character.constant.CCharacterDirection;
	import net.fpp.pandastory.game.module.character.constant.CCharacterState;
	import net.fpp.pandastory.game.module.charactercontroller.view.CharacterControllerModuleView;
	import net.fpp.pandastory.vo.CharacterVO;

	import starling.display.DisplayObjectContainer;

	public class CharacterControllerModule extends AModule implements ICharacterControllerModule
	{
		[Inject]
		public var characterModule:ICharacterModule;

		[Inject(id='guiView')]
		public var guiView:DisplayObjectContainer;

		private var _characterControllerModuleView:CharacterControllerModuleView;
		private var _characterControllerModel:CharacterControllerModel;

		public function CharacterControllerModule()
		{
			this._characterControllerModuleView = this.createModuleView( CharacterControllerModuleView ) as CharacterControllerModuleView;

			this._characterControllerModel = this.createModel( CharacterControllerModel ) as CharacterControllerModel;
		}

		override public function onInited():void
		{
			this.guiView.addChild( this._characterControllerModuleView );
		}

		public function onUpdate():void
		{
			if( this.characterModule.getIsOnGround() )
			{
				this.updateCharacterOnGround();
			}
			else
			{
				this.updateCharacterOnAir();
			}

			if( this._characterControllerModel.isJumpTriggered )
			{
				this.runJumpRoutine();
			}
		}

		private function updateCharacterOnGround():void
		{
			var characterPhysicsObject:b2Body = this.characterModule.getCharacterPhysicsObject();
			var currentVelocity:b2Vec2 = characterPhysicsObject.GetLinearVelocity();
			var characterVO:CharacterVO = this.characterModule.getCharacterVO();

			var maxSpeed:Number = characterVO.maxSpeed;
			var acceleration:Number = characterVO.acceleration;
			var deceleration:Number = characterVO.deceleration;
			var maximumJumpPush:Number = characterVO.maximumJumpPush;

			if( this._characterControllerModel.isRightActive )
			{
				if( currentVelocity.x < maxSpeed )
				{
					currentVelocity.x += acceleration;
					this.characterModule.setDirection( CCharacterDirection.RIGHT );
				}
				this.characterModule.setState( CCharacterState.RUN );
			}
			else if( this._characterControllerModel.isLeftActive )
			{
				if( currentVelocity.x > -maxSpeed )
				{
					currentVelocity.x -= acceleration;
					this.characterModule.setDirection( CCharacterDirection.LEFT );
				}
				this.characterModule.setState( CCharacterState.RUN );
			}
			else
			{
				this.characterModule.setState( CCharacterState.IDLE );
			}

			if( currentVelocity.x > 0 )
			{
				currentVelocity.x = Math.min( currentVelocity.x, maxSpeed );
			}
			else
			{
				currentVelocity.x = Math.max( currentVelocity.x, -maxSpeed );
			}

			if( !this._characterControllerModel.isRightActive && !this._characterControllerModel.isLeftActive )
			{
				currentVelocity.x *= deceleration;
			}

			if( this._characterControllerModel.isJumpActive )
			{
				if( !this._characterControllerModel.isJumpTriggered )
				{
					this._characterControllerModel.availableJumpPush = maximumJumpPush;
					this._characterControllerModel.isJumpTriggered = true;
				}
			}
			else
			{
				this._characterControllerModel.isJumpTriggered = false;
			}

			characterPhysicsObject.SetLinearVelocity( currentVelocity );
		}

		private function updateCharacterOnAir():void
		{
			var characterPhysicsObject:b2Body = this.characterModule.getCharacterPhysicsObject();
			var currentVelocity:b2Vec2 = characterPhysicsObject.GetLinearVelocity();
			var characterVO:CharacterVO = this.characterModule.getCharacterVO();

			var maxSpeedOnAir:Number = characterVO.maxSpeedOnAir;
			var acceleration:Number = characterVO.accelerationOnAir;
			var deceleration:Number = characterVO.decelerationOnAir;

			if( this._characterControllerModel.isRightActive )
			{
				if( currentVelocity.x < maxSpeedOnAir )
				{
					currentVelocity.x += acceleration;
					this.characterModule.setDirection( CCharacterDirection.RIGHT );
				}
				this.characterModule.setState( CCharacterState.RUN );
			}
			else if( this._characterControllerModel.isLeftActive )
			{
				if( currentVelocity.x > -maxSpeedOnAir )
				{
					currentVelocity.x -= acceleration;
					this.characterModule.setDirection( CCharacterDirection.LEFT );
				}
				this.characterModule.setState( CCharacterState.RUN );
			}

			if( !this._characterControllerModel.isRightActive && !this._characterControllerModel.isLeftActive )
			{
				currentVelocity.x *= deceleration;
			}

			if( currentVelocity.x > 0 )
			{
				currentVelocity.x = Math.min( currentVelocity.x, maxSpeedOnAir );
			}
			else
			{
				currentVelocity.x = Math.max( currentVelocity.x, -maxSpeedOnAir );
			}

			if( currentVelocity.y > 0 )
			{
				this.characterModule.setState( CCharacterState.FALL );
			}
			else
			{
				this.characterModule.setState( CCharacterState.JUMP );
			}

			if( !this._characterControllerModel.isJumpActive )
			{
				this._characterControllerModel.isJumpTriggered = false;
			}

			characterPhysicsObject.SetLinearVelocity( currentVelocity );
		}

		private function runJumpRoutine():void
		{
			var characterPhysicsObject:b2Body = this.characterModule.getCharacterPhysicsObject();
			var currentVelocity:b2Vec2 = characterPhysicsObject.GetLinearVelocity();
			var characterVO:CharacterVO = this.characterModule.getCharacterVO();

			var jumpPower:Number = characterVO.jumpPower;

			if( this._characterControllerModel.availableJumpPush > 0 )
			{
				this._characterControllerModel.availableJumpPush--;
				currentVelocity.y = -jumpPower;
			}

			characterPhysicsObject.SetLinearVelocity( currentVelocity );
		}

		public function getUpdateFrequency():int
		{
			return 20;
		}

		override public function dispose():void
		{
			super.dispose();

			this.characterModule = null;
			this.guiView = null;
			this._characterControllerModuleView = null;
			this._characterControllerModel = null;
		}
	}
}