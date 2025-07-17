package com.illuzor.otherside.controllers {
	
	import com.illuzor.otherside.events.WeaponEvent;
	import starling.events.EventDispatcher;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public final class WeaponController extends EventDispatcher {
		
		private var timers:Vector.<WeaponTimer>;
		
		public function WeaponController(configs:Array) {
			timers = new Vector.<WeaponTimer>();
			for (var i:int = 0; i < configs.length; i++) {
				var timer:WeaponTimer = new WeaponTimer(configs[i].type, configs[i].delay, configs[i].x, configs[i].y);
				timers.push(timer);
				timer.addEventListener(WeaponEvent.SHOOT, onShoot);
			}
		}
		
		private function onShoot(e:WeaponEvent):void {
			dispatchEvent(new WeaponEvent(WeaponEvent.SHOOT, e.weaponType, e.x, e.y));
		}
		
		public function play():void {
			for (var i:int = 0; i < timers.length; i++) {
				timers[i].play();
			}
		}
		
		public function pause():void {
			for (var i:int = 0; i < timers.length; i++) {
				timers[i].pause();
			}
		}
		
		public function dispose():void {
			for (var i:int = 0; i < timers.length; i++) {
				timers[i].removeEventListener(WeaponEvent.SHOOT, onShoot);
				timers[i].dispose();
			}
			timers = null;
		}
		
	}
}