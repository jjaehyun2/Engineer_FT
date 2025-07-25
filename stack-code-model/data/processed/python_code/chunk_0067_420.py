package net.psykosoft.psykopaint2.app.states
{

	import net.psykosoft.psykopaint2.app.states.transitions.TransitionPaintToHomeState;
	import net.psykosoft.psykopaint2.base.states.State;
	import net.psykosoft.psykopaint2.base.states.ns_state_machine;
	import net.psykosoft.psykopaint2.core.managers.gestures.GrabThrowController;
	import net.psykosoft.psykopaint2.core.models.NavigationStateType;
	import net.psykosoft.psykopaint2.core.models.PaintingModel;
	import net.psykosoft.psykopaint2.core.rendering.CanvasRenderer;
	import net.psykosoft.psykopaint2.core.signals.NavigationCanHideWithGesturesSignal;
	import net.psykosoft.psykopaint2.core.signals.NotifyPaintingInfoSavedSignal;
	import net.psykosoft.psykopaint2.core.signals.NotifyToggleTransformGestureSignal;
	import net.psykosoft.psykopaint2.core.signals.RequestNavigationStateChangeSignal;
	import net.psykosoft.psykopaint2.core.views.debug.ConsoleView;
	import net.psykosoft.psykopaint2.paint.signals.RequestClosePaintViewSignal;
	import net.psykosoft.psykopaint2.paint.signals.RequestPaintingDiscardSignal;
	import net.psykosoft.psykopaint2.paint.signals.RequestPaintingSaveSignal;

	use namespace ns_state_machine;

	public class PaintState extends State
	{
		[Inject]
		public var requestStateChangeSignal:RequestNavigationStateChangeSignal;

		[Inject]
		public var transitionToHomeState:TransitionPaintToHomeState;

		[Inject]
		public var requestClosePaintView:RequestClosePaintViewSignal;

		[Inject]
		public var requestPaintingSaveSignal:RequestPaintingSaveSignal;
		
		[Inject]
		public var requestPaintingDiscardSignal:RequestPaintingDiscardSignal;

		[Inject]
		public var notifyPaintingSavedSignal:NotifyPaintingInfoSavedSignal;

		[Inject]
		public var paintingModel:PaintingModel;
		
		[Inject]
		public var canvasRenderer:CanvasRenderer;

		[Inject]
		public var toggleTransformGestureSignal:NotifyToggleTransformGestureSignal;

		[Inject]
		public var navigationCanHideWithGesturesSignal:NavigationCanHideWithGesturesSignal;

		public function PaintState() {
		}

		override ns_state_machine function activate( data:Object = null ):void {
			
			GrabThrowController.gesturesEnabled=true;

			
			ConsoleView.instance.log( this, "activating..." );
			ConsoleView.instance.logMemory();
			requestClosePaintView.add( onClosePaintView );
			requestStateChangeSignal.dispatch( NavigationStateType.PAINT_SELECT_BRUSH );
			navigationCanHideWithGesturesSignal.dispatch( true );
			toggleTransformGestureSignal.dispatch( true );
		}

		override ns_state_machine function deactivate():void {
			
			ConsoleView.instance.log( this, "deactivating..." );
			ConsoleView.instance.logMemory();
			requestClosePaintView.remove( onClosePaintView );
			toggleTransformGestureSignal.dispatch( false );
		}

		private function onClosePaintView( save:Boolean ):void {
			ConsoleView.instance.log( this, "closing painting view..." );
			ConsoleView.instance.logMemory();
			
			
			if ( save ) savePainting();
			else discardPainting();
		}

		private function discardPainting():void {
			ConsoleView.instance.log( this, "discarding painting..." );
			ConsoleView.instance.logMemory();
			notifyPaintingSavedSignal.addOnce( onPaintingSaved );
			requestPaintingDiscardSignal.dispatch();
			//			setTimeout( function():void {
			//				requestPaintingSaveSignal.dispatch( paintingModel.activePaintingId, true );
			//			}, 2000 );
		}
		
		private function savePainting():void {
			ConsoleView.instance.log( this, "saving painting..." );
			ConsoleView.instance.logMemory();
			
			
			//THIS BLOB IS SAVING TO CAMERA ROLL
			/*var bitmapData:BitmapData = canvasRenderer.renderToBitmapData();
			
			// Write bmd
			if( CoreSettings.RUNNING_ON_iPAD ) {
				var iosImageSaveUtil:IosImageSaveUtil = new IosImageSaveUtil();
				iosImageSaveUtil.saveImageToCameraRoll( bitmapData, onWriteComplete );
			}
			else {
				var desktopImageSaveUtil:DesktopImageSaveUtil = new DesktopImageSaveUtil();
				desktopImageSaveUtil.saveImageToDesktop( bitmapData, onWriteComplete );
			}*/
			
			
			notifyPaintingSavedSignal.addOnce( onPaintingSaved );
			requestPaintingSaveSignal.dispatch( paintingModel.activePaintingId, true );
//			setTimeout( function():void {
//				requestPaintingSaveSignal.dispatch( paintingModel.activePaintingId, true );
//			}, 2000 );
		}
		
		private function onWriteComplete():void
		{
			// TODO Auto Generated method stub
			
		}
		
		private function onPaintingSaved( success:Boolean ):void {
			continueToHome();
		}

		private function continueToHome():void {
			stateMachine.setActiveState( transitionToHomeState );
		}
	}
}