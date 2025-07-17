/**
 * Created by newkrok on 29/12/15.
 */
package src.game.library.crates
{
	import Box2D.Collision.Shapes.b2PolygonShape;
	import Box2D.Common.Math.b2Vec2;
	import Box2D.Dynamics.b2Body;
	import Box2D.Dynamics.b2BodyDef;
	import Box2D.Dynamics.b2FilterData;
	import Box2D.Dynamics.b2FixtureDef;
	import Box2D.Dynamics.b2World;

	import flash.geom.Point;

	import src.constant.CBox2D;

	import starling.display.Image;
	import starling.textures.Texture;

	public class BaseCrate
	{
		protected var FRICTION:Number = 0.8;
		protected var DENSITY:Number = 0.6;

		protected var FILTER_CATEGORY:Number = 3;
		protected var FILTER_MASK:Number = 3;

		protected var _world:b2World;
		protected var _body:b2Body;

		protected var _image:Image;
		protected var _position:Point;
		protected var _scale:Number;

		public function BaseCrate( world:b2World, position:Point, scale:Number )
		{
			this._world = world;
			this._position = position;
			this._scale = scale;

			this.createB2Body();
			this.createImage();

			this._image.pivotX = this.image.width / 2;
			this._image.pivotY = this.image.height / 2;
			this._image.scaleX = this._scale;
		}

		protected function createB2Body():void
		{
			var bodyDef:b2BodyDef = new b2BodyDef();

			bodyDef.position.Set( this._position.x / CBox2D.PIXELS_TO_METRE, this._position.y / CBox2D.PIXELS_TO_METRE );
			bodyDef.type = b2Body.b2_dynamicBody;
			bodyDef.fixedRotation = false;
			bodyDef.userData = 'WALL';

			var polygonShape:b2PolygonShape = this.createShape();

			var fixtureDef:b2FixtureDef = new b2FixtureDef();
			fixtureDef.shape = polygonShape;
			fixtureDef.friction = FRICTION;
			fixtureDef.density = DENSITY;

			var filter:b2FilterData = new b2FilterData();
			filter.categoryBits = FILTER_CATEGORY;
			filter.maskBits = FILTER_MASK;
			fixtureDef.filter = filter;

			_body = this._world.CreateBody( bodyDef );
			_body.CreateFixture( fixtureDef );
		}

		protected function createShape():b2PolygonShape
		{
			return new b2PolygonShape();
		}

		protected function createImage():void
		{
			this._image = new Image( new Texture() );
		}

		public function get image():Image
		{
			return this._image;
		}

		public function get body():b2Body
		{
			return this._body;
		}

		public function reset():void
		{
			this._body.SetLinearVelocity( new b2Vec2() );
			this._body.SetAngularVelocity( 0 );

			this._body.SetPositionAndAngle( new b2Vec2( this._position.x / CBox2D.PIXELS_TO_METRE, this._position.y / CBox2D.PIXELS_TO_METRE ), 0 );
		}

		public function dispose():void
		{
			this._image.removeFromParent( true );
			this._image = null;

			this._world.DestroyBody( this._body );
			this._body = null;

			this._world = null;
		}
	}
}