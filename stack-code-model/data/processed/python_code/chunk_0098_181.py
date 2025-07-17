package org.pong.mvcs.controller.commands
{
	import org.pong.mvcs.model.StarlingGameModel;
	
	/**
	 *
	 * Assets loading command initiates loading of all necessary game graphic assets. Later those assets can be 
	 * reached through GraphicUtils.
	 *
	 * @see org.pong.utils.graphic.GraphicUtils
	 * @author mc
	 */
	
	public class AssetsLoadingCompleteCommand
	{
		[Inject]
		public var starlingGameModel:StarlingGameModel;
	
		public function execute():void
		{
			trace(this + ", execute()");
			
			starlingGameModel.assetsLoadingComplete();
		}
	}

}