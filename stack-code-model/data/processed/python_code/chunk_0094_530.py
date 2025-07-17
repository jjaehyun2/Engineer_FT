/**
 * Created by newkrok on 20/10/16.
 */
package net.fpp.pandastory.config.level
{
	import flash.geom.Rectangle;
	import flash.geom.Rectangle;

	import net.fpp.common.geom.SimplePoint;
	import net.fpp.pandastory.constant.CTerrainType;
	import net.fpp.pandastory.game.vo.LevelVO;
	import net.fpp.pandastory.game.vo.TerrainVO;

	public class Level1VO extends LevelVO
	{
		public function Level1VO()
		{
			this.terrain = this.convert( '{"rectangleBackgroundData":[{"polygon":[{"x":5,"y":275},{"x":676,"y":275},{"x":676,"y":353},{"x":5,"y":353}],"terrainTextureId":"TERRAIN_0"},{"polygon":[{"x":659,"y":524},{"x":1479,"y":524},{"x":1479,"y":582},{"x":659,"y":582}],"terrainTextureId":"TERRAIN_0"},{"polygon":[{"x":58,"y":580},{"x":517,"y":580},{"x":517,"y":694},{"x":58,"y":694}],"terrainTextureId":"TERRAIN_0"},{"polygon":[{"x":1161,"y":345},{"x":1280,"y":345},{"x":1280,"y":397},{"x":1161,"y":397}],"terrainTextureId":"TERRAIN_0"},{"polygon":[{"x":1412,"y":289},{"x":1524,"y":289},{"x":1524,"y":326},{"x":1412,"y":326}],"terrainTextureId":"TERRAIN_0"}],"enemyPathData":null,"libraryElements":null,"staticElementData":null,"polygonBackgroundData":[{"polygon":[{"x":414,"y":274},{"x":511.05,"y":246.05},{"x":581,"y":172},{"x":711.9,"y":223.45},{"x":673.8,"y":305.9},{"x":849,"y":364},{"x":749.1,"y":359.45},{"x":649.2,"y":354.9},{"x":549.3,"y":350.4},{"x":384,"y":343}],"terrainTextureId":"polygon_terrain_1"}],"dynamicElementData":null}' );

			this.startPoint = new SimplePoint( 100, 100 );
		}

		private function convert( rawData:String ):Vector.<TerrainVO>
		{
			var result:Vector.<TerrainVO> = new <TerrainVO>[];
			var data:Object = JSON.parse( rawData );

			for ( var i:int = 0; i < data.rectangleBackgroundData.length; i++ )
			{
				var width:Number = ( data.rectangleBackgroundData[i].polygon[2].x - data.rectangleBackgroundData[i].polygon[0].x ) / 2;
				var height:Number = ( data.rectangleBackgroundData[i].polygon[2].y - data.rectangleBackgroundData[i].polygon[0].y ) / 2;

				result.push(
						new TerrainVO(
								CTerrainType.NORMAL,
								//data.rectangleBackgroundData[i].terrainTextureId,
								new Rectangle(
										data.rectangleBackgroundData[i].polygon[0].x - width / 2,
										data.rectangleBackgroundData[i].polygon[0].y - height / 2,
										width,
										height
								)
						) );
			}

			return result;
		}
	}
}