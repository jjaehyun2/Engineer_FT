package masputih.patterns.commands
{
	
	import flash.events.Event;
	import flash.events.TimerEvent;
	import flash.utils.Timer;
	import nl.demonsters.debugger.MonsterDebugger;
	
	/**
	 * 
	 * @author Anggie Bratadinata
	 */
	public class DelayCommand extends SimpleCommand
	{
		public static const NAME:String = "DelayCommand";
		
		public function DelayCommand() 
		{
			super();
			
		}
		
		
		override public function setReceiver(receiver:* = null):void 
		{
			if (!receiver is Timer) {
				throw new Error("Receiver must be a Timer instance");
				return;
			}
			
			_receiver = receiver;
			Timer(_receiver).addEventListener(TimerEvent.TIMER_COMPLETE, onTimerComplete);
		}
		
		override public function get name():String { return DelayCommand.NAME; }
		
		
		
		/**
		 * 
		 * @param	params	An array containing delay argument for Timer object. Default value is 1000 ms.
		 * @param	event
		 */
		override public function execute(params:Array = null, event:Event = null):void 
		{
			super.execute(params, event);
			
			if (params != null && params[0] != null) {
				var delay:Number = params[0];
			}else {
				delay = _params[0];
				//MonsterDebugger.trace(this, "delay : " + delay);
			}
			
			if (_receiver == null ) {
				setReceiver(new Timer(delay, 1));
			}
			
			Timer(_receiver).start();
		}
		
		private function onTimerComplete(e:TimerEvent):void 
		{
			MonsterDebugger.trace(this, "complete");
			dispatchEvent(new CommandEvent(CommandEvent.COMPLETE));
		}
		
	}

}