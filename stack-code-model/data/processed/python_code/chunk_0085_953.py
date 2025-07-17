/**
 * Created by newkrok on 20/10/16.
 */
package net.fpp.pandastory.game.module.movingplatform
{
	import flash.geom.Rectangle;

	import net.fpp.common.starling.module.AModule;
	import net.fpp.pandastory.game.module.movingplatform.view.MovingPlatformModuleView;
	import net.fpp.pandastory.game.vo.LevelVO;

	import starling.display.DisplayObjectContainer;

	public class MovingPlatform extends AModule implements IMovingPlatform
	{
		[Inject]
		public var levelDataVO:LevelVO;

		[Inject(id='worldView')]
		public var worldView:DisplayObjectContainer;

		private var _movingPlatformModuleView:MovingPlatformModuleView;

		public function MovingPlatform()
		{
			this._movingPlatformModuleView = this.createModuleView( MovingPlatformModuleView ) as MovingPlatformModuleView;
		}

		override public function onInited():void
		{
			this._movingPlatformModuleView.createMovingPlatforms( this.levelDataVO.movingPlatform );

			this.worldView.addChild( this._movingPlatformModuleView );
		}

		override public function dispose():void
		{
			super.dispose();

			this.levelDataVO = null;
			this.worldView = null;
			this._movingPlatformModuleView = null;
		}
	}
}