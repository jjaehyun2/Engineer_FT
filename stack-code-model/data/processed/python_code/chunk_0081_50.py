/**
 * Created by newkrok on 12/09/16.
 */
package net.fpp.pandastory.game.module.character
{
	import Box2D.Common.Math.b2Vec2;
	import Box2D.Dynamics.Contacts.b2Contact;
	import Box2D.Dynamics.Contacts.b2ContactEdge;
	import Box2D.Dynamics.Joints.b2WeldJointDef;
	import Box2D.Dynamics.b2Body;

	import flash.geom.Rectangle;

	import net.fpp.common.geom.SimplePoint;
	import net.fpp.common.starling.module.AModule;
	import net.fpp.pandastory.game.module.character.view.CharacterModuleView;
	import net.fpp.pandastory.game.module.characteranimation.ICharacterAnimationModule;
	import net.fpp.pandastory.game.module.physicsworld.IPhysicsWorldModule;
	import net.fpp.pandastory.util.PhysicsUtil;
	import net.fpp.pandastory.vo.CharacterVO;

	import starling.display.DisplayObjectContainer;

	public class CharacterModule extends AModule implements ICharacterModule
	{
		[Inject]
		public var physicsWorldModule:IPhysicsWorldModule;

		[Inject]
		public var characterAnimationModule:ICharacterAnimationModule;

		[Inject(id='worldView')]
		public var worldView:DisplayObjectContainer;

		private var _characterModuleView:CharacterModuleView;
		private var _characterModel:CharacterModel;

		public function CharacterModule()
		{
			this._characterModuleView = this.createModuleView( CharacterModuleView ) as CharacterModuleView;

			this._characterModel = this.createModel( CharacterModel ) as CharacterModel;
		}

		override public function onInited():void
		{
			this._characterModel.setCharacterAnimationModule( this.characterAnimationModule );

			this._characterModuleView.init();

			const characterPosition:SimplePoint = new SimplePoint( 100, 100 );
			const characterSize:Number = 16;
			const characterFrameSize:Number = 5;

			this._characterModel.characterPhysicsObject = physicsWorldModule.createDynamicsRectangle(
					new Rectangle( characterPosition.x, characterPosition.y, characterSize, characterSize ),
					.2, .1, true
			);

			this._characterModel.characterRadiusPhysicsObject = physicsWorldModule.createDynamicsCircle(
					characterPosition.x, characterPosition.y - characterFrameSize, characterSize + characterFrameSize,
					0, .1, true
			);

			var weldJointDef:b2WeldJointDef = new b2WeldJointDef();
			weldJointDef.Initialize( this._characterModel.characterRadiusPhysicsObject, this._characterModel.characterPhysicsObject, this._characterModel.characterRadiusPhysicsObject.GetWorldCenter() );
			physicsWorldModule.createJoint( weldJointDef );

			this.worldView.addChild( this._characterModuleView );
		}

		public function setCharacterVO( value:CharacterVO ):void
		{
			this._characterModel.setCharacterVO( value );
			this._characterModuleView.updateSkin();
		}

		public function getCharacterPhysicsObject():b2Body
		{
			return this._characterModel.characterPhysicsObject;
		}

		public function getIsOnGround():Boolean
		{
			return this._characterModel.getIsOnGround();
		}

		public function setDirection( value:int ):void
		{
			if( this._characterModel.getDirection() != value )
			{
				this._characterModel.setDirection( value );

				this._characterModuleView.updateDirection();
			}
		}

		public function getDirection():int
		{
			return this._characterModel.getDirection();
		}

		public function setState( value:String ):void
		{
			if( this._characterModel.getState() != value )
			{
				this._characterModel.setState( value );

				this._characterModuleView.updateState();
			}
		}

		public function getState():String
		{
			return this._characterModel.getState();
		}

		public function onUpdate():void
		{
			this.calculateOnGround();

			this._characterModuleView.update();

			if( this._characterModuleView.y > 500 )
			{
				this.setPosition( new SimplePoint( Math.random() * 900, Math.random() * 100 ) );
			}
		}

		private function calculateOnGround():void
		{
			var contactList:b2ContactEdge = this._characterModel.characterPhysicsObject.GetContactList();
			var isInGround:Boolean = false;

			while( contactList && !isInGround )
			{
				var fixture:b2Contact = contactList.contact;
				if( fixture.IsTouching() )
				{
					isInGround = true;
				}
				else
				{
					contactList = contactList.next;
				}
			}

			this._characterModel.setIsOnGround( isInGround );
		}

		public function getCharacterVO():CharacterVO
		{
			return this._characterModel.getCharacterVO();
		}

		public function setPosition( startPoint:SimplePoint ):void
		{
			var newPosition:b2Vec2 = new b2Vec2( PhysicsUtil.normalPositionToPhysics( startPoint.x ), PhysicsUtil.normalPositionToPhysics( startPoint.y ) );

			this._characterModel.characterPhysicsObject.SetLinearVelocity( newPosition );
			this._characterModel.characterPhysicsObject.SetPosition( newPosition );

			this._characterModel.characterRadiusPhysicsObject.SetLinearVelocity( newPosition );
			this._characterModel.characterRadiusPhysicsObject.SetPosition( newPosition );
		}

		public function getUpdateFrequency():int
		{
			return 0;
		}

		override public function dispose():void
		{
			super.dispose();

			this.physicsWorldModule = null;
			this.characterAnimationModule = null;
			this.worldView = null;
			this._characterModuleView = null;
			this._characterModel = null;
		}
	}
}