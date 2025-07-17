package org.pong.mvcs.view.mediator 
{
	import org.pong.mvcs.service.signals.AssetsLoadingCompleteSignal;
	import org.pong.mvcs.service.signals.AssetsLoadingProgressSignal;
	import org.pong.mvcs.view.component.LoadingScreenView;
	import org.pong.mvcs.view.signals.ScreenTransitionCompleteSignal;
	import org.pong.mvcs.view.signals.StartLoadingAssetsSignal;
	import org.pong.mvcs.view.AbstractMediator;
	
	/**
	  * Loading Screen mediator - handles assets loading.
	 * 
	 * @author mc
	 */
	public class LoadingScreenMediator extends AbstractMediator
	{
		/**
		 * Dispatched when loading screen is added to stage.
		 */
		[Inject]
		public var startLoadingAssetsSignal:StartLoadingAssetsSignal;
		
		/**
		 * Dispatched multiple times durring assets loading progress.
		 */
		[Inject]
		public var assetsLoadingProgressSignal:AssetsLoadingProgressSignal;
		
		/**
		 * Dispatche after assets finished loading.
		 */
		[Inject]
		public var assetsLoadingCompleteSignal:AssetsLoadingCompleteSignal;
		
		/**
		 * Dispatched after screen transition completes.
		 */
		[Inject]
		public var screenTransitionCompleteSignal:ScreenTransitionCompleteSignal;
		
		/**
		 * Const
		 */
		public function LoadingScreenMediator() 
		{
			super();
		}

		/**
		 * Internal initialization logic.
		 * 
		 * @private
		 */
		override public function initialize():void
		{
			super.initialize();
			
			setSignals();
		}
		
		/**
		 * Signals setter.
		 * 
		 * @private
		 */
		private function setSignals():void
		{
			addOnceToSignal(view.startLoadingSignal, startLoadingAssets);			
			addToSignal(assetsLoadingProgressSignal, assetsLoadingProgress);
			addToSignal(assetsLoadingCompleteSignal, assetsLoadingComplete);
		}
		
		/**
		 * Destructor.
		 * 
		 * @private
		 */
		override public function destroy():void
		{
			super.destroy();
			
			screenTransitionCompleteSignal.dispatch();
		}
		
		/**
		 * Start loading assets dispatcher.
		 * 
		 */
		private function startLoadingAssets():void
		{
			startLoadingAssetsSignal.dispatch();
		}
		
		/**
		 * 
		 * Assets loading progress handler. Used to updated view loading bar.
		 * 
		 * @param	ratio Assets loading ratio (0 to 1.0)
		 */
		private function assetsLoadingProgress(ratio:Number):void
		{
			view.setProgreesBar(ratio);
		}
		
		/**
		 * Dispatched when assets loaded ratio equals 1.0.
		 */
		private function assetsLoadingComplete():void
		{
			view.onLoadingCompleate.dispatch();
		}
		
		/**
		 * Dispatched when screen finished transition.
		 */
		private function screenTransitionComplete():void
		{
			screenTransitionCompleteSignal.dispatch();
		}
			
		
		/**
		 * Component view.
		 * 
		 * @private
		 */
		protected function get view():LoadingScreenView
		{
			return LoadingScreenView(viewComponent);
		}	
	}
}