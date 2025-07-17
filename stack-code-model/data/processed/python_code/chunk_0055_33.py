package  
{
	import flash.display.MovieClip;
	
	/**
	 * ...
	 * @author sere
	 */
	public class Ene extends MovieClip 
	{
		public var spd:Number = 5;
		public var life:Number = 1;
		public var escapefg = false;
		public function Ene() 
		{
			
		}
		public function move():void 
		{
			y += spd;
			if ( y > BattleStage.stageHeight + 10 )
				escapefg = true;
		}
		
	}

}