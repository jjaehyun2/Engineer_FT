package elements 
{
	import starling.display.Sprite;
	/**
	 * ...
	 * @author LeleoSan
	 */
	public class BoxMenu extends Sprite
	{
		
		public function BoxMenu() 
		{
			
		}
		public function destroy():void
		{
			removeChildren(0, -1, true);
			removeFromParent(true);
		}
	}

}