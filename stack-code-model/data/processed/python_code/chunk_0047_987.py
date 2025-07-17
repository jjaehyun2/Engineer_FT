package com.game.unit.core
{
	import com.Track;
	
	import core.unit.behavior.IRateabel;

	public class RateBehavior implements IRateabel
	{
		protected var _rate:int;
		protected var _tick:int=-1;
		protected var _count:int;
		public function RateBehavior()
		{
		}
		
		public function rateRender(tick:int):void{
			if(_tick == -1){
				_tick = tick;
			}
			
			else
			if(tick - _tick > Track.TIME_PER_TICK){
				var frames:int = (tick - _tick)/Track.TIME_PER_TICK;
				_tick += frames * Track.TIME_PER_TICK;
				if(count>0){
//					count--;
					count-=frames;
					
					if(count<0) count=0;
				}
			}
		}
		
		public function isCool():Boolean{
			return _count <= 0;
		}
		
		public function coolDown():void{
			count = _rate;
		}
		
		protected function set count(value:int):void{
			_count = value;
		}
		
		protected function get count():int{
			return _count;
		}
		
		public function set rate(value:int):void
		{
			_rate = value/Track.TIME_PER_TICK;
		}
		
		public function get rate():int
		{
			return _rate*Track.TIME_PER_TICK;
		}
		
		public function resetTick(tick:int=-1):void{
			_tick = tick;
		}
		
		public function get percent():Number{
			return (_rate - _count)/_rate;
		}
	}
}