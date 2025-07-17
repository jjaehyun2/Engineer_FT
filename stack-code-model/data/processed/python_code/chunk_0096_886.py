/**
 * Created by newkrok on 13/10/16.
 */
package net.fpp.pandastory.game.module.terrain
{
	import net.fpp.common.starling.module.AModule;
	import net.fpp.pandastory.game.vo.LevelVO;
	import net.fpp.pandastory.game.module.terrain.view.TerrainModuleView;

	import starling.display.DisplayObjectContainer;

	public class TerrainModule extends AModule implements ITerrainModule
	{
		[Inject]
		public var levelDataVO:LevelVO;

		[Inject(id='worldView')]
		public var worldView:DisplayObjectContainer;

		private var _terrainModuleView:TerrainModuleView;

		public function TerrainModule()
		{
			this._terrainModuleView = this.createModuleView( TerrainModuleView ) as TerrainModuleView;
		}

		override public function onInited():void
		{
			this._terrainModuleView.createStaticTerrains( this.levelDataVO.terrain );

			this.worldView.addChild( this._terrainModuleView );
		}

		override public function dispose():void
		{
			super.dispose();

			this.levelDataVO = null;
			this.worldView = null;
			this._terrainModuleView = null;
		}
	}
}