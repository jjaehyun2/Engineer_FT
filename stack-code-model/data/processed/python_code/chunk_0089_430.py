package  
{
	import flash.display.MovieClip;
	import BattleStage;
	import Math2;
	/**
	 * ...
	 * @author sere
	 */
	public class Tama2 extends MovieClip
	{
		public var escapefg:Boolean = false;
		public var ang:Number;
		public var mx:Number;
		public var my:Number;
		public var spd:Number = 8;
		public function Tama2(ang_rad:Number) 
		{
			ang = ang_rad;
			mx = Math.cos(ang) * spd;
			my = Math.sin(ang) * spd;
		}
		public function move():void 
		{
			x += mx;
			y += my;
			
			trace( x , y );
			
			if ( 
				y < 0 - 5 
			||	y > BattleStage.stageHeight + 5
			||	x < -5
			||	x > BattleStage.stageWidth + 5
			) escapefg = true;
			
		}
	}

}