package com.qcenzo.flake2d.system
{
	import flash.utils.getTimer;

	public class Clock
	{
		private var _running:Boolean;
		private var _fps:Number;
		private var _time0:int;
		private var _time1:int;
		private var _dt:int;
		private var _frames:int;
		private var _delay:int;
		private var _onInterval:Function;
		private var _interval0:int;

		public function Clock()
		{
			_time0 = getTimer();
			_running = true;
		}
		
		public function togglePause():void
		{
			_running = !_running;
		}
		
		/**
		 * 
		 * @param listener
		 * @param delay 间隔时间(单位秒), <=0不触发<code>listener</code>
		 * 
		 */
		public function setInterval(listener:Function, delay:int):void
		{
			if (delay <= 0)
				return;
			 _onInterval = listener;
			 _delay = delay * 1000; 
			 _interval0 = getTimer();
		}
		
		public function get fps():int
		{
			return _fps * 1000;
		}
		
		flake2d function tick():Boolean
		{
			_frames++;
			_time1 = getTimer();
			_dt = _time1 - _time0;
			if (_dt >= 1000)
			{
				_fps = _frames / _dt;
				_time0 = _time1;
				_frames = 0;
			}
			
			if (_onInterval != null && _time1 - _interval0 >= _delay)
			{
				_onInterval();
				_interval0 = _time1;
			}
			 
			return _running;
		}
	}
}