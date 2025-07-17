package org.pong.mvcs.view.mediator 
{
	import org.pong.mvcs.view.component.StarlingGameView
	import org.pong.mvcs.view.signals.TickSignal;
	import robotlegs.bender.extensions.starlingViewMap.impl.SignalMediator;
	
	/**
	 * 
	 * Starling Game mediator - every frame it dipatches Tick signal that is handeled by every game view.
	 * 
	 * @author mc
	 */
	
	public class StarlingGameMediator extends SignalMediator
	{
		/**
		 * Tick signal - dispatched once every frame.
		 */
		[Inject]
		public var tickSignal:TickSignal;
		
		/**
		 * const
		 */
		public function StarlingGameMediator()
		{
			super();
		}
		
		/**
		 * Internal initialization.
		 * 
		 * @private
		 */
		override public function initialize():void
		{
			super.initialize();
			
			trace( this + ", initialize()" );
			
			addToSignal(starlingGameView.tickSignal, dispatchTickSignal);
		}
		
		/**
		 * Destructor
		 * 
		 * @private
		 */
		override public function destroy():void
		{
			trace( this + ", destroy()" );
			
			super.destroy();
		}
		
		/**
		 * 
		 * Dispatches Tick signal every frame.
		 * 
		 * @event tickSignal() sent every frame
		 * 
		 * @param	passedTime
		 */
		private function dispatchTickSignal(passedTime:Number):void
		{
			tickSignal.dispatch(passedTime);
		}
		
		/**
		 * 
		 * Compoenet view.
		 * 
		 * @private
		 */
		protected function get starlingGameView():StarlingGameView
		{
			return StarlingGameView(viewComponent);
		}
	}
}