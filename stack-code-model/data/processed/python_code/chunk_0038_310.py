package  
{
	import flash.display.MovieClip;
	import flash.geom.Point;
	
	/**
	 * ...
	 * @author sere
	 */
	public class Player extends MovieClip 
	{
		
		public var spd_def:Number = 8;
		public var life = 1;
		public var escapefg = false;
		public function Player() 
		{
			
		}
		public function move():void 
		{
			var spd:Number = ( BattleStage.downfg ? spd_def : spd_def * 1.2 );
			var mp:Point;
			var tar:Point = BattleStage.getMousePoint();
			tar.y -= 60;
			var ang:Number = Math2.getAngle( this, tar );
			if ( Math2.getRange(this, tar) < spd )
				mp = new Point( tar.x, tar.y );
			else 
				mp = new Point( x + spd * Math.cos(ang), 
								y + spd * Math.sin(ang) );
			x = mp.x;
			y = mp.y;
		}
		
	}

}