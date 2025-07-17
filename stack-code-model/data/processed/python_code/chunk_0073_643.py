/**
 * Created by newkrok on 11/10/15.
 */
package src.game.module.snow
{
	import net.fpp.common.starling.module.AModule;

	import src.game.module.snow.view.SnowModuleView;

	public class SnowModule extends AModule
	{
		public function SnowModule()
		{
			this._view = this.createModuleView( SnowModuleView ) as SnowModuleView;
		}

		public function update():void
		{
			( this._view as SnowModuleView ).update();
		}
	}
}