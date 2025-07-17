/**
 * Created by newkrok on 14/02/16.
 */
package net.fpp.pandastory.game.module.background.polygonbackground
{
	import net.fpp.common.starling.module.IModule;
	import net.fpp.common.util.jsonbitmapatlas.vo.BitmapDataVO;
	import net.fpp.pandastory.vo.PolygonBackgroundVO;

	public interface IPolygonBackgroundModule extends IModule
	{
		function setPolygonBackgroundVO( polygonBackroundVOs:Vector.<PolygonBackgroundVO> ):void

		function setTerrainInformations( terrains:Vector.<BitmapDataVO> ):void
	}
}