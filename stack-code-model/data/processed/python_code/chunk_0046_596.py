/**
 * Created by newkrok on 13/10/16.
 */
package net.fpp.pandastory.game.module.terrain.view
{
	import flash.geom.Rectangle;

	import net.fpp.common.starling.StaticAssetManager;
	import net.fpp.common.starling.module.AModuleView;
	import net.fpp.pandastory.game.vo.TerrainVO;

	import starling.display.Image;

	public class TerrainModuleView extends AModuleView
	{
		public function TerrainModuleView()
		{
		}

		public function createStaticTerrains( terrains:Vector.<TerrainVO> ):void
		{
			for( var i:int = 0; i < terrains.length; i++ )
			{
				var terrainVO:TerrainVO = terrains[ i ];

				var image:Image = new Image( StaticAssetManager.instance.getTexture( terrainVO.type ) );

				image.textureRepeat = true;
				image.tileGrid = new Rectangle( 0, 0, image.texture.width, image.texture.height );
				image.pixelSnapping = true;

				image.width = terrainVO.rectangle.width * 2;
				image.height = terrainVO.rectangle.height * 2;
				image.x = terrainVO.rectangle.x - terrainVO.rectangle.width;
				image.y = terrainVO.rectangle.y - terrainVO.rectangle.height;

				this.addChild( image );
			}
		}
	}
}