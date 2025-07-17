package org.pong.mvcs.model.signals 
{
	import org.osflash.signals.Signal;
	
	/**
	 * 
	 * Signal dispatched every frame if Starling game model is in GameState.PLAY state. Signal Calls <code>update()</code> method
	 * on every view.
	 * 
	 * @author mc
	 */
	public class UpdateViewsSignal extends Signal 
	{	
		/**
		 * @param passedTime - time passed since the last frame/signal.
		 */
		public function UpdateViewsSignal() 
		{
			super(Number);
		}
	}
}