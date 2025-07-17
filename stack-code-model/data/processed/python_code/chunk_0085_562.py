/**
 * Created by newkrok on 30/12/15.
 */
package src.game.library.crates
{
	import Box2D.Collision.Shapes.b2PolygonShape;
	import Box2D.Dynamics.b2World;

	import flash.geom.Point;

	import net.fpp.common.starling.StaticAssetManager;

	import src.constant.CBox2D;

	import starling.display.Image;

	public class Crate extends BaseCrate
	{
		private const WIDTH:uint = 37;
		private const HEIGHT:uint = 37;

		public function Crate( world:b2World, position:Point, scale:Number )
		{
			super( world, position, scale );
		}

		override protected function createShape():b2PolygonShape
		{
			var polygonShape:b2PolygonShape = new b2PolygonShape();
			polygonShape.SetAsBox( this.WIDTH / 2 / CBox2D.PIXELS_TO_METRE, this.HEIGHT / 2 / CBox2D.PIXELS_TO_METRE );

			return polygonShape;
		}

		override protected function createImage():void
		{
			this._image = new Image( StaticAssetManager.instance.getTexture( 'crate_1' ) );
		}
	}
}