package core.timeline
{

	import flash.events.Event;
	import flash.events.EventDispatcher;
	import flash.events.TimerEvent;
	import flash.utils.Timer;

	[Event(name="change", type="flash.events.Event")]
	public class TimerTrack extends EventDispatcher implements ITrack
	{
		private var timer:Timer;	
		public function TimerTrack(delay:Number)
		{
			timer=new Timer(delay);
			timer.addEventListener(TimerEvent.TIMER,onTimer);
		}
		protected function onTimer(event:TimerEvent):void
		{
			this.dispatchEvent(new Event(Event.CHANGE));
		}
		/**
		 * 轨道跳动的间隔时间
		 * @return
		 */
		public function get delay():Number{
			return timer.delay;
		}
		public function set delay(value:Number):void{
			if(timer.delay==value){
				return;
			}
			timer.delay=value;
		}
		public function get running():Boolean
		{
			return timer.running;
		}
		public function start():void
		{
			timer.start();
		}
		
		public function stop():void
		{
			timer.stop();
		}
		public function get bewrite():String{
			return 'TimerTrack:delay='+delay;
		}
	}
}