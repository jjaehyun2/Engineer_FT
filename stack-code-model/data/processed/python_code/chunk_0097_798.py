package entities
{
	import flash.display.BitmapData;
	
	import net.flashpunk.Entity;
	import net.flashpunk.FP;
	import net.flashpunk.Graphic;
	import net.flashpunk.Mask;
	import net.flashpunk.graphics.Image;
	
	
	
	public class Bullets extends Entity
	{
		
		
		protected var bulletImage:Image;
		public var Score:Number = 0;
		public var Health:Number = 10;
		
		
		public function Bullets()
		{
			
			bulletImage = new Image(new BitmapData(5, 5));
			bulletImage.color = 0xf33220;
			graphic = bulletImage;
			
			setHitbox(5, 5);
			type = "bullet";
			
			trace(FP.stage.width);
			
			x = FP.stage.width/1.5 * Math.random();
			
			
			y = FP.screen.height/1.5 * Math.random();
			trace(x);
			trace(y);
		}
		
		
		public function destroy():void
		{
			// Here we could place specific destroy-behavior for the Bullet.
		//	FP.world.remove(this);
		}
		

		
	}
}