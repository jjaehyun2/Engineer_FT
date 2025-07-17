/**
 * Created by newkrok on 11/09/16.
 */
package net.fpp.pandastory.util
{
	import Box2D.Collision.Shapes.b2CircleShape;
	import Box2D.Collision.Shapes.b2PolygonShape;
	import Box2D.Dynamics.b2Body;
	import Box2D.Dynamics.b2BodyDef;
	import Box2D.Dynamics.b2FixtureDef;
	import Box2D.Dynamics.b2World;

	import flash.geom.Rectangle;

	public class PhysicsUtil
	{
		private static var _pixelsToMetre:Number;

		public static function setPixelsToMetre( value:Number ):void
		{
			_pixelsToMetre = value;
		}

		public static function createStaticRectangle( world:b2World, rectangle:Rectangle ):b2Body
		{
			return createRectangle( world, rectangle, b2Body.b2_staticBody );
		}

		public static function createDynamicRectangle( world:b2World, rectangle:Rectangle, friction:Number = 1, density:Number = 1, isFixedRotation:Boolean = false ):b2Body
		{
			return createRectangle( world, rectangle, b2Body.b2_dynamicBody, false, friction, density, isFixedRotation );
		}

		private static function createRectangle( world:b2World, rectangle:Rectangle, bodyType:uint, allowSleep:Boolean = true, friction:Number = 1, density:Number = 1, isFixedRotation:Boolean = false ):b2Body
		{
			var my_body:b2BodyDef = new b2BodyDef();
			my_body.position.Set( rectangle.x / _pixelsToMetre, rectangle.y / _pixelsToMetre );
			my_body.type = bodyType;
			my_body.allowSleep = allowSleep;
			my_body.fixedRotation = isFixedRotation;

			var my_box:b2PolygonShape = new b2PolygonShape();
			my_box.SetAsBox( rectangle.width / _pixelsToMetre, rectangle.height / _pixelsToMetre );

			var my_fixture:b2FixtureDef = new b2FixtureDef();
			my_fixture.shape = my_box;
			my_fixture.friction = friction;
			my_fixture.density = density;

			var world_body:b2Body = world.CreateBody( my_body );
			world_body.CreateFixture( my_fixture );

			return world_body;
		}

		public static function createDynamicCircle( world:b2World, x:Number, y:Number, radius:Number, friction:Number = 1, density:Number = 1, isFixedRotation:Boolean = false ):b2Body
		{
			return createCircle( world, x, y, radius, b2Body.b2_dynamicBody, true, friction, density );
		}

		private static function createCircle( world:b2World, x:Number, y:Number, radius:Number, bodyType:uint, allowSleep:Boolean = true, friction = 1, density = 1, isFixedRotation:Boolean = false ):b2Body
		{
			radius /= _pixelsToMetre;

			var my_body:b2BodyDef = new b2BodyDef();
			my_body.type = bodyType;
			my_body.position.Set( x / _pixelsToMetre, y / _pixelsToMetre );
			my_body.fixedRotation = isFixedRotation;

			var world_body:b2Body = world.CreateBody( my_body );

			var myCircle:b2CircleShape = new b2CircleShape( radius );

			var my_fixture:b2FixtureDef = new b2FixtureDef();
			my_fixture.shape = myCircle;
			my_fixture.friction = friction;
			my_fixture.density = density;

			world_body.CreateFixture( my_fixture );

			return world_body;
		}

		public static function physicsPositionToNormal( position:Number ):Number
		{
			return position * _pixelsToMetre;
		}

		public static function normalPositionToPhysics( position:Number ):Number
		{
			return position / _pixelsToMetre;
		}
	}
}