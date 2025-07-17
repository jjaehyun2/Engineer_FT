/**
 * Created by newkrok on 15/08/16.
 */
package net.fpp.pandastory.game.module.physicsworld
{
	import Box2D.Dynamics.Joints.b2Joint;
	import Box2D.Dynamics.Joints.b2JointDef;
	import Box2D.Dynamics.b2Body;
	import Box2D.Dynamics.b2World;

	import flash.geom.Rectangle;

	import net.fpp.common.starling.module.AModel;
	import net.fpp.pandastory.game.vo.TerrainVO;
	import net.fpp.pandastory.util.PhysicsUtil;

	public class PhysicsWorldModel extends AModel
	{
		public var physicsWorld:b2World;

		public function createTerrains( terrainVOs:Vector.<TerrainVO> ):void
		{
			var length:int = terrainVOs.length;

			for( var i:int = 0; i < length; i++ )
			{
				this.createStaticRectangle( terrainVOs[ i ].rectangle );
			}
		}

		public function createStaticRectangle( rectangle:Rectangle ):b2Body
		{
			return PhysicsUtil.createStaticRectangle( this.physicsWorld, rectangle );
		}

		public function createDynamicsRectangle( rectangle:Rectangle, friction:Number = 1, density:Number = 1, isFixedRotation:Boolean = false ):b2Body
		{
			return PhysicsUtil.createDynamicRectangle( this.physicsWorld, rectangle, friction, density, isFixedRotation );
		}

		public function createDynamicsCircle( x:Number, y:Number, radius:Number, friction:Number = 1, density:Number = 1, isFixedRotation:Boolean = false ):b2Body
		{
			return PhysicsUtil.createDynamicCircle( this.physicsWorld, x, y, radius, friction, density, isFixedRotation );
		}

		public function createJoint( jointDefinition:b2JointDef ):b2Joint
		{
			return this.physicsWorld.CreateJoint( jointDefinition );
		}
	}
}