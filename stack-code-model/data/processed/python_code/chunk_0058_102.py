package net.psykosoft.psykopaint2.core.views.base
{

	import net.psykosoft.psykopaint2.base.ui.base.ViewBase;
	import net.psykosoft.psykopaint2.core.signals.NotifyMemoryWarningSignal;
	import net.psykosoft.psykopaint2.core.signals.NotifyNavigationStateChangeSignal;
	import net.psykosoft.psykopaint2.core.signals.RequestNavigationStateChangeSignal;

	import robotlegs.bender.bundles.mvcs.Mediator;

	public class MediatorBase extends Mediator
	{
		[Inject]
		public var notifyMemoryWarningSignal:NotifyMemoryWarningSignal;

		[Inject]
		public var notifyStateChangeSignal:NotifyNavigationStateChangeSignal;

		[Inject]
		public var requestStateChangeSignal:RequestNavigationStateChangeSignal;

		protected var _enablingStates:Vector.<String>;
		protected var _view:ViewBase;

		public var manageStateChanges:Boolean = true;
		public var manageMemoryWarnings:Boolean = true;

		override public function initialize():void {

			trace( this, "initialize" );

			_enablingStates = new Vector.<String>();

			notifyMemoryWarningSignal.add( onMemoryWarning );
			notifyStateChangeSignal.add( onStateChange );
		}

		override public function destroy():void {

			trace( this, "*** mediator destroyed ***" );

			notifyMemoryWarningSignal.remove( onMemoryWarning );
			notifyStateChangeSignal.remove( onStateChange );

			_enablingStates = null;

			_view.dispose();
			_view = null;
		}

		protected function registerView( value:ViewBase ):void {
			_view = value;
		}

		protected function registerEnablingState( state:String ):void {
			_enablingStates.push( state );
		}

		protected function requestNavigationStateChange( state:String ):void {
			requestStateChangeSignal.dispatch( state );
		}

		protected function onStateChange( newState:String ):void {
			if( !manageStateChanges ) return;
			var viewShouldBeEnabled:Boolean = _enablingStates.indexOf( newState ) != -1;
			if( viewShouldBeEnabled ) {
				if( !_view.isEnabled ) {
					_view.enable();
				}
			}
			else {
				if( _view.isEnabled ) {
					_view.disable();
				}
			}
		}

		protected function onMemoryWarning():void {
			trace( this, "received memory warning." );
			if( !manageMemoryWarnings ) return;
			if( !_view.visible ) _view.dispose();
		}
	}
}