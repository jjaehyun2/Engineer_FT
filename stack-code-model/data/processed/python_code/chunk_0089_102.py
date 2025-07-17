package ro.ciacob.desktop.operation {
	import flash.events.TimerEvent;
	import flash.utils.Timer;

	/**
	 * @see IProcrastinator
	 */
	public class Procrastinator implements IProcrastinator {

		/**
		 * @see IProcrastinator
		 * @param	action
		 * 			A function to execute when procrastination ends.
		 * 
		 * @param	waitTime
		 * 			The minimum time, in milliseconds, to wait before executing the `action` previously
		 * 			specified. Each new call to `procrastinate()` adds at most this
		 * 			period of time to the procrastination.
		 * 
		 * @param	actionContext
		 * 			Optional. A context to execute the `action` function in. Defaults to an
		 * 			empty, anonymous object.
		 */
		public function Procrastinator(action:Function, waitTime:int, actionContext:Object = null) {
			_action = action;
			_waitTime = waitTime;
			if (actionContext == null) {
				if (_action != null) {
					actionContext = {};
				}
			}
			_actionContext = actionContext;
		}

		private var _action:Function;

		/**
		 * @see IProcrastinator
		 */
		public function get action():Function {
			return _action;
		}

		private var _actionContext:Object;

		/**
		 * @see IProcrastinator
		 */
		public function get actionContext():Object {
			return _actionContext;
		}

		private var _waitTime:int;

		/**
		 * @see IProcrastinator
		 */
		public function get waitTime():int {
			return _waitTime;
		}

		private var _timer:Timer;

		/**
		 * @see IProcrastinator
		 */
		public function abort():void {
			if (_isTimerInitialized()) {
				_stopTimer();
				_uninitializeTimer();
				_action = null;
				_actionContext = null;
				_waitTime = -1;
			}
		}

		/**
		 * @see IProcrastinator
		 */
		public function doItNow():void {
			if (_action != null) {
				if (_isTimerInitialized()) {
					_stopTimer();
				}
				_performAction();
			} else {
				_sayNothingToDo();
			}
		}

		/**
		 * @see IProcrastinator
		 */
		public function leaveItForNow():void {
			if (_action != null) {
				if (_isTimerInitialized()) {
					_stopTimer();
				}
			} else {
				_sayNothingToDo();
			}
		}

		/**
		 * @see IProcrastinator
		 */
		public function procrastinate():void {
			if (_action != null) {
				if (!_isTimerInitialized()) {
					_initializeTimer();
				}
				_resetTimer();
			} else {
				_sayNothingToDo();
			}
		}

		private function _initializeTimer():void {
			_timer = new Timer(_waitTime, 1);
			_timer.addEventListener(TimerEvent.TIMER_COMPLETE, _onTimerComplete);
		}

		private function _isTimerInitialized():Boolean {
			return (_timer != null);
		}

		private function _onTimerComplete(event:TimerEvent):void {
			_performAction();
			_stopTimer();
		}

		private function _performAction():void {
			_action.apply(_actionContext);
		}

		private function _resetTimer():void {
			_timer.reset();
			_timer.start();
		}

		private function _sayNothingToDo():void {
			trace('Procrastinator: There is nothing to be done. Have you told me to ABORT?');
		}

		private function _stopTimer():void {
			_timer.stop();
			_timer.reset();
		}

		private function _uninitializeTimer():void {
			_stopTimer();
			_timer.removeEventListener(TimerEvent.TIMER_COMPLETE, _onTimerComplete);
			_timer = null;
		}
	}
}