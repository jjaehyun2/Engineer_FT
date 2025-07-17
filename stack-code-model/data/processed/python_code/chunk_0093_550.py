package com.illuzor.otherside.controllers {
	
	import com.illuzor.otherside.constants.WeaponType;
	import com.illuzor.otherside.events.WeaponEvent;
	import flash.events.TimerEvent;
	import flash.utils.Timer;
	import starling.events.EventDispatcher;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class WeaponsController extends EventDispatcher {
		
		private var gunTimer:Timer;
		
		public function WeaponsController(config:Object = null) {
			gunTimer = new Timer(700);
			gunTimer.addEventListener(TimerEvent.TIMER, onGun);
		}
		
		public function play():void {
			gunTimer.start();
		}
		
		public function pause():void {
			gunTimer.stop();
		}
		
		private function onGun(e:TimerEvent):void {
			dispatchEvent(new WeaponEvent(WeaponEvent.SHOOT, WeaponType.GUN));
		}
		
	}
}