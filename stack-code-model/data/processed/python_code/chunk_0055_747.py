package gd.eggs.util
{
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.TimerEvent;
	import flash.utils.Timer;
	import flash.utils.getTimer;


	/**
	 * ...
	 * @author Dukobpa3
	 */
	public class GlobalTimer
	{
		//=====================================================================
		//      CONSTANTS
		//=====================================================================

		//=====================================================================
		//      PARAMETERS
		//=====================================================================
		//-----------------------------
		//      Enterfrtame
		//-----------------------------
		private static var _visualBus:Sprite = new Sprite();

		//-----------------------------
		//      Timer
		//-----------------------------
		private static var _currentDate:Date;
		private static var _timer:Timer = new Timer(1000);
		private static var _synced:Boolean;

		//-----------------------------
		//      Callbacks
		//-----------------------------
		private static var _timerCallBacks:Vector.<Function> = new Vector.<Function>();
		private static var _frameCallBacks:Vector.<Function> = new Vector.<Function>();

		//=====================================================================
		//      PUBLIC
		//=====================================================================
		public static function updateDate(date:Date):void
		{
			if (!_timer.hasEventListener(TimerEvent.TIMER))
			{
				_timer.addEventListener(TimerEvent.TIMER, onTimer);
			}

			_currentDate = date;
			_timer.reset();
			_timer.start();

			_synced = true;
		}

		/**
		 * Добавить коллбек ентерфрейма
		 * @param       func function onTimer(date:Date):void {} // коллбек принимает текущую дату getTimer().
		 */
		public static function addFrameCallback(func:Function):void
		{
			if (_frameCallBacks.indexOf(func) == -1)
			{
				_frameCallBacks.push(func);
			}

			if (!_visualBus.hasEventListener(Event.ENTER_FRAME))
			{
				// если не подписаны - подписаться на ентерфейм
				_visualBus.addEventListener(Event.ENTER_FRAME, onEnterFrame);
			}
		}

		/**
		 * Убрать коллбек энтерфрейма
		 * @param       func
		 */
		public static function removeFrameCallback(func:Function):void
		{
			if (_frameCallBacks.indexOf(func) != -1)
			{
				_frameCallBacks.splice(_frameCallBacks.indexOf(func), 1);
			}
			if (!_frameCallBacks.length && _visualBus.hasEventListener(Event.ENTER_FRAME))
			{
				_visualBus.removeEventListener(Event.ENTER_FRAME, onEnterFrame);
			}
		}

		/**
		 * Добавить коллбек таймера
		 * @param       func function onTimer(unixtime:int):void {} // коллбек принимает текущую дату сервера.
		 *              // текущую, которая установлена в таймере, а не в системеДля синхронизации с сервером.
		 */
		public static function addTimerCallback(func:Function):void
		{
			if (!_synced) updateDate(new Date());

			if (_timerCallBacks.indexOf(func) == -1)
			{
				_timerCallBacks.push(func);
			}

			if (!_timer.hasEventListener(TimerEvent.TIMER))
			{
				_timer.addEventListener(TimerEvent.TIMER, onTimer);
				_timer.start();
			}
		}

		/**
		 * Убрать коллбек таймера
		 * @param       func
		 */
		public static function removeTimerCallback(func:Function):void
		{
			if (_timerCallBacks.indexOf(func) != -1)
			{
				_timerCallBacks.splice(_timerCallBacks.indexOf(func), 1);
			}
			if (!_timerCallBacks.length && _timer.hasEventListener(TimerEvent.TIMER))
			{
				_timer.removeEventListener(TimerEvent.TIMER, onTimer);
				_timer.stop();
			}
		}

		//=====================================================================
		//      PRIVATE
		//=====================================================================

		//=====================================================================
		//      HANDLERS
		//=====================================================================
		private static function onTimer(event:TimerEvent):void
		{
			if (!_currentDate)return;
			_currentDate.seconds++;

			for (var i:int = 0; i < _timerCallBacks.length; i++)
			{
				_timerCallBacks[i](_currentDate);
			}
		}

		private static function onEnterFrame(event:Event):void
		{
			for (var i:int = 0; i < _frameCallBacks.length; i++)
			{
				_frameCallBacks[i](getTimer());
			}
		}

		//=====================================================================
		//      ACCESSORS
		//=====================================================================
		public static function get currentDate():Date { return _currentDate; }
	}

}