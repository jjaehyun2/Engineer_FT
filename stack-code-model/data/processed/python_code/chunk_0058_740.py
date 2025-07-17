/**
 * Created by newkrok on 15/08/16.
 */
package net.fpp.pandastory.game.module.physicsworld
{
	import Box2D.Common.Math.b2Vec2;
	import Box2D.Dynamics.Joints.b2Joint;
	import Box2D.Dynamics.Joints.b2JointDef;
	import Box2D.Dynamics.b2Body;
	import Box2D.Dynamics.b2DebugDraw;
	import Box2D.Dynamics.b2World;

	import flash.geom.Rectangle;

	import net.fpp.common.starling.module.AModule;
	import net.fpp.pandastory.constant.CPhysics;
	import net.fpp.pandastory.game.vo.LevelVO;
	import net.fpp.pandastory.util.PhysicsUtil;

	public class PhysicsWorldModule extends AModule implements IPhysicsWorldModule
	{
		[Inject]
		public var levelDataVO:LevelVO;

		private var _physicsWorldModel:PhysicsWorldModel;

		public function PhysicsWorldModule()
		{
			PhysicsUtil.setPixelsToMetre( CPhysics.PIXELS_TO_METRE );

			this._physicsWorldModel = this.createModel( PhysicsWorldModel ) as PhysicsWorldModel;

			this._physicsWorldModel.physicsWorld = new b2World( new b2Vec2( 0, CPhysics.GRAVITY ), true );
		}

		override public function onInited():void
		{
			this._physicsWorldModel.createTerrains( levelDataVO.terrain );
		}

		public function createDynamicsRectangle( rectangle:Rectangle, friction:Number = 1, density:Number = 1, isFixedRotation:Boolean = false ):b2Body
		{
			return this._physicsWorldModel.createDynamicsRectangle( rectangle, friction, density, isFixedRotation );
		}

		public function createDynamicsCircle( x:Number, y:Number, radius:Number, friction:Number = 1, density:Number = 1, isFixedRotation:Boolean = false ):b2Body
		{
			return this._physicsWorldModel.createDynamicsCircle( x, y, radius, friction, density, isFixedRotation );
		}

		public function createJoint( jointDefinition:b2JointDef ):b2Joint
		{
			return this._physicsWorldModel.createJoint( jointDefinition );
		}

		public function setDebugDraw( value:b2DebugDraw ):void
		{
			this._physicsWorldModel.physicsWorld.SetDebugDraw( value );
		}

		public function drawDebugData():void
		{
			this._physicsWorldModel.physicsWorld.DrawDebugData();
		}

		public function onUpdate():void
		{
			this._physicsWorldModel.physicsWorld.Step( CPhysics.BOX2D_TIMESTEP, CPhysics.BOX2D_VELOCITY_ITERATIONS, CPhysics.BOX2D_POSITION_ITERATIONS );
			this._physicsWorldModel.physicsWorld.ClearForces();
		}

		public function getUpdateFrequency():int
		{
			return 0;
		}

		override public function dispose():void
		{
			super.dispose();

			this.levelDataVO = null;
			this._physicsWorldModel = null;
		}
	}
}