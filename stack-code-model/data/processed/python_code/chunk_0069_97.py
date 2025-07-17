package {
	
	import flash.events.EventDispatcher;
	import flash.events.TimerEvent;
	import flash.utils.getTimer;
	import flash.utils.Timer;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	[Event(name = "timerComplete", type = "flash.events.TimerEvent")]
	[Event(name = "timer", type = "flash.events.TimerEvent")]
	
	public class NewTimer extends EventDispatcher {
		
		private var timer:Timer;
		private var delay:Number;
		private var timeFromStart:uint;
		private var afterPause:Boolean;
		
		public function NewTimer(delay:Number, repeatCount:uint = 0) {
			this.delay = delay;
			timer = new Timer(delay, repeatCount);
			timer.addEventListener(TimerEvent.TIMER, onTimerEvent);
			timer.addEventListener(TimerEvent.TIMER_COMPLETE, onTimerEvent);
		}
		
		private function onTimerEvent(e:TimerEvent):void {
			if (e.type == TimerEvent.TIMER) {
				
				dispatchEvent(new TimerEvent(TimerEvent.TIMER));
				timeFromStart = getTimer();
				
				if (afterPause) {
					timer.stop();
					timer.delay = delay;
					timer.start();
					afterPause = false;
				}	
			}
			
			if (e.type == TimerEvent.TIMER_COMPLETE)
				dispatchEvent(new TimerEvent(TimerEvent.TIMER_COMPLETE));
		}
		
		public function start():void {
			timer.start();
			timeFromStart = getTimer();
		}
		
		public function pause():void {
			var timeDelta:uint = getTimer() - timeFromStart;
			timer.stop();
			timer.delay -= timeDelta;
			afterPause = true;
		}
		
		public function stop():void {
			timer.stop();
		}
		
		public function dispose():void {
			timer.stop();
			timer.removeEventListener(TimerEvent.TIMER, onTimerEvent);
			timer.removeEventListener(TimerEvent.TIMER_COMPLETE, onTimerEvent);
			timer = null;
		}
		
	}
}