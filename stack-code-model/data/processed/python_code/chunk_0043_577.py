package com.rockmatch.screenstates.gameplay.commands
{
	import com.rockmatch.screenstates.gameplay.events.GridRegionEvent;
	import com.rockmatch.screenstates.gameplay.models.gridregion.GridRegionStatesEnum;
	import com.rockmatch.screenstates.gameplay.models.gridregion.IGridRegionModel;

	import robotlegs.bender.bundles.mvcs.Command;


	/**
	 *
	 * @author dkoloskov
	 *
	 */
	public class SwapChipsCompleteCommand extends Command
	{
		[Inject]
		public var event:GridRegionEvent;

		[Inject]
		public var gridRegionModel:IGridRegionModel;

		//==============================================================================
		//{region							PUBLIC METHODS
		override public function execute():void
		{
			if(this.gridRegionModel.matches.length == 0)
			{
				this.gridRegionModel.state = GridRegionStatesEnum.IDLE_STATE;
			}
			else
			{
				this.gridRegionModel.state = GridRegionStatesEnum.CHIPS_EXPLOSION_STATE;
			}
		}

		//} endregion PUBLIC METHODS ===================================================
	}
}