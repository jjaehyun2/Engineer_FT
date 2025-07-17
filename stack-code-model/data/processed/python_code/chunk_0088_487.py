/**
 * Created by newkrok on 14/02/16.
 */
package net.fpp.pandastory.game.module.background.polygonbackground
{
	import net.fpp.common.starling.module.AModel;
	import net.fpp.common.util.jsonbitmapatlas.vo.BitmapDataVO;
	import net.fpp.pandastory.vo.PolygonBackgroundVO;

	public class PolygonBackgroundModel extends AModel
	{
		public var polygonBackroundVOs:Vector.<PolygonBackgroundVO>;

		private var _terrains:Vector.<BitmapDataVO>;

		public function setTerrains( value:Vector.<BitmapDataVO> ):void
		{
			this._terrains = value;
		}

		public function getTerrainById( terrainId:String ):BitmapDataVO
		{
			for( var i:int = 0; this._terrains.length; i++ )
			{
				if( this._terrains[ i ].id == terrainId )
				{
					return this._terrains[ i ];
				}
			}

			return null;
		}
	}
}