package  
{
	import flash.display.MovieClip;
	import flash.display.Sprite;
	import flash.events.Event;
	/**
	 * ...
	 * @author sere
	 */
	public class BossGauge extends Sprite
	{
		public var life_max:int = 0;
		public var life:int = 0;
		public var width_max:Number;
		public var memori:Number;
		public var gauge:MovieClip;
		public var boss:Boss;
		public function BossGauge() 
		{
			x = 30;
			y = 70;
		}
		public function setDisp(target:Boss, life:int, life_max:int):void 
		{
			boss = target;
			this.life_max = life_max;
			this.life = life;
			this.width_max = width;
			this.memori = width / life;
			addEventListener(Event.ENTER_FRAME, ef );
		}
		private function ef(e:Event):void 
		{
			gauge.width = boss.life * memori;
		}
		
	}

}