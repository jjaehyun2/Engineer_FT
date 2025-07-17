package org.pong.mvcs.controller.commands 
{
	import org.pong.mvcs.model.StarlingGameModel;
	
	/**
	 * 
	 * Command which informs the <code>StarlingGameModel</code> of it's screen transition completion. When 
	 * <code>Loading Screen</code> finishes initial assets loading, there is a quick animation between screens.
	 * When this animation is over StarlingGameModel needs to be informed.
	 * 
	 * @author mc
	 */
	
	public class ScreenTransitionCompleteCommand 
	{
		[Inject]
		public var starlingGameModel:StarlingGameModel;
		
		public function execute():void
		{
			trace(this + ", execute()");
			
			starlingGameModel.screenTransitionComplete();
		}
	}
}