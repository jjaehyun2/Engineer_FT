/**
 * Created by newkrok on 30/12/15.
 */
package src.game.library.crates
{
	import Box2D.Collision.Shapes.b2PolygonShape;
	import Box2D.Common.Math.b2Vec2;
	import Box2D.Dynamics.b2World;

	import flash.geom.Point;

	import net.fpp.common.starling.StaticAssetManager;

	import src.constant.CBox2D;

	import starling.display.Image;

	public class SmallRampCrate extends BaseCrate
	{
		private const WIDTH:uint = 50;
		private const HEIGHT:uint = 25;

		public function SmallRampCrate( world:b2World, position:Point, scale:Number )
		{
			super( world, position, scale );
		}

		override protected function createShape():b2PolygonShape
		{
			var polygonShape:b2PolygonShape = new b2PolygonShape();
			var vertices:Vector.<b2Vec2>;

			if( this._scale == 1 )
			{
				vertices = new <b2Vec2>[
					new b2Vec2( WIDTH / 2 / CBox2D.PIXELS_TO_METRE * -1, HEIGHT / 2 / CBox2D.PIXELS_TO_METRE * -1 ),
					new b2Vec2( WIDTH / 2 / CBox2D.PIXELS_TO_METRE, HEIGHT / 2 / CBox2D.PIXELS_TO_METRE ),
					new b2Vec2( WIDTH / 2 / CBox2D.PIXELS_TO_METRE * -1, HEIGHT / 2 / CBox2D.PIXELS_TO_METRE )
				];
			}
			else
			{
				vertices = new <b2Vec2>[
					new b2Vec2( WIDTH / 2 / CBox2D.PIXELS_TO_METRE, HEIGHT / 2 / CBox2D.PIXELS_TO_METRE * -1 ),
					new b2Vec2( WIDTH / 2 / CBox2D.PIXELS_TO_METRE, HEIGHT / 2 / CBox2D.PIXELS_TO_METRE ),
					new b2Vec2( WIDTH / 2 / CBox2D.PIXELS_TO_METRE * -1, HEIGHT / 2 / CBox2D.PIXELS_TO_METRE )
				];
			}

			polygonShape.SetAsVector( vertices, 3 );

			return polygonShape;
		}

		override protected function createImage():void
		{
			this._image = new Image( StaticAssetManager.instance.getTexture( 'crate_5' ) );
		}
	}
}