package  
{
	import flash.events.Event;
	/**
	 * ...
	 * @author Fabian Verkuijlen
	 */
	public class Ferrari extends Cars
	{
		private var ferrari : FerrariMC = new FerrariMC;
		public function Ferrari() 
		{
			addChild(ferrari);
			ferrari.x = 100;
			ferrari.y = 550;
			ferrari.z = -40;
			
			addEventListener(Event.ENTER_FRAME, loop)
			
		}
		
		private function loop(e:Event):void 
		{
			ferrari.x += 10 + Math.random() * 2;
			
			if (ferrari.x >= 1400)
			{
				ferrari.x -= 2800;
			}
		}
		
	}

}