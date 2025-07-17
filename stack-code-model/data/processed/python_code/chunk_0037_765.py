package 
{
	import flash.display.Bitmap;
	import flash.display.Sprite;
	import flash.events.Event;
	
	/**
	 * ...
	 * @author Mo Kakwan
	 */
	public class flyingtarget extends Sprite
	{
		public function flyingtarget() 
		{
			var ship:Bitmap = new Bitmap(ImageAssets.shipTexture);
			this.addChild(ship);
		}
		
		public function goToNewPosition() {
			var randX:Number = Math.random() * stage.stageWidth;
			var randY:Number = Math.random() * stage.stageHeight;
			var randT:Number = Math.random()* 1;
			
			var myTween:TweenLite = new TweenLite(this, randT, {x:randX,y:randY, onComplete:goToNewPosition});
		}
		
		
		
	}

}