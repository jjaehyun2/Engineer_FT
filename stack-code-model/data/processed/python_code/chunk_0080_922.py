/**
 * Created by Administrator on 2015/8/19.
 */
package gui3D.shapes
{
	import com.greensock.TweenMax;

	import flash.display.Sprite;

	public class CubeSpread extends Sprite
	{
		private var sector:SectorShape;

		public function CubeSpread()
		{
			sector = new SectorShape();
			addChild(sector);
			sector.x = 200;
			sector.y = 200;
		}

		public function unfold():void
		{
			var obj:Object = {};
			obj.angle = sector.currentAngle;
			sector.show();
			TweenMax.to(obj, 5, {
				angle: -180, onUpdate: function ():void
				{
					sector.drawSector(0, 0, 0, 100, obj.angle, 0);
				}
			});
		}

		public function fold():void
		{
			var obj:Object = {};
			obj.angle = sector.currentAngle;
			TweenMax.to(obj, 5, {
				angle: 0, onUpdate: function ():void
				{
					sector.drawSector(0, 0, 0, 100, obj.angle, 0);
				}, onComplete: function ():void
				{
					sector.hide();
				}
			});
		}
	}
}