package  
{
	import effects.Sword;
	import net.flashpunk.Entity;
	import net.flashpunk.tweens.misc.Alarm;
	import net.flashpunk.utils.Input;
	import net.flashpunk.utils.Key;
	import roshan.buffer.ACTION;
	public class Inventory extends Entity
	{
		private var sword:Sword = null;
		private var attachedTo:Hero;
		public  var startActionCallback:Function = null;
		private var stopAlarm:Alarm = new Alarm(0.3, swordDeactivate);
		private var repeat:int = 0;
		
		public function Inventory(attach:Hero, inStartActionCallback:Function = null)
		{
			startActionCallback = inStartActionCallback;
			attachedTo = attach;
			addTween(stopAlarm);
		}
		
		public function keyActivation():void {
			if (Input.pressed(Key.Q)) {
				startActionCallback(ACTION.SWORD, attachedTo.direction);
				swordActivate();
			}
		}
		
		// ------------------------------------ //
		
		public function swordActivate():void {
			if (sword == null) sword = new Sword(attachedTo);
			//if (startActionCallback != null) startActionCallback(ACTION.SWORD, attachedTo.direction);
			if (stopAlarm.remaining > 0) {
				repeat++;
				return;
			} 
			repeat = 0;
			stopAlarm.start();
			sword.start();
			world.add(sword);
		}
		
		public function swordReset():void {
			stopAlarm.complete = swordDeactivate
		}
		
		public function swordDeactivate():void {
			if (repeat > 0) {
				repeat--;
				sword.start();
				stopAlarm.start();
				return;
			}
			if (sword == null) sword = new Sword(attachedTo);
			world.remove(sword);
		}
		
		
	}

}