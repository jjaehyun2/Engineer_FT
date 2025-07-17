package entities
{
	
	import flash.display.BitmapData;
	import net.flashpunk.Entity;
	import net.flashpunk.Graphic;
	import net.flashpunk.Mask;
	import net.flashpunk.graphics.Image;
	import net.flashpunk.FP;
	
	
	public class Ball extends Entity
	{
		private var randomMaxNumbers:int = 5;
		private var randomMinNumbers:int = -3;
		protected var randomNumber:int = Math.floor(Math.random() * (1+randomMaxNumbers - randomMinNumbers))+ randomMinNumbers;	
		protected var randomNumber2:int = Math.floor(Math.random() * (1+randomMaxNumbers - randomMinNumbers))+ randomMinNumbers;
		protected var ballImage:Image;
		public function Ball()
		{
			
			
			
			
			
			
			
			
				
				ballImage = new Image(new BitmapData(20, 20));
				ballImage.color = 0xa43456;
				graphic = ballImage;
				
				setHitbox(20, 20);
				width = 20;
				height = 20;
				type = "ball";
				
				
				x = FP.stage.width/1.5 * Math.random();
				
				
				y = FP.screen.height/1.5 * Math.random();
			}
			
			
			public function destroy():void
			{
				// Here we could place specific destroy-behavior for the Bullet.
				FP.world.remove(this);
			}
			
			public override function update():void
			{
				
			
				
				
			
				//Math.floor(Math.random() * 41) + 10;  //number between 10 -50
	
				
				y =y +  randomNumber;
				
				x = x + randomNumber2;
				
				
				
				//if () {
					
			//	}
				
				//Here is the positions of the balls, working pretty nice this way. Not going too much outside the screen and bouncing unpredictable.
				if (y <=0) {
					y= 0;
					randomNumber = Math.floor(Math.random() * (1+randomMaxNumbers - randomMinNumbers))+ randomMinNumbers;
					
				}
				
				if (y >= FP.stage.height / 1.5) {
					//y = FP.stage.height / 1.5;
					y = -y;
					randomNumber2 = Math.floor(Math.random() * (1+randomMaxNumbers - randomMinNumbers))+ randomMinNumbers;
					if (x == y) {
						y = x+1;
					}
				}
				
				if (x <= 0) {
					
					y = y+2;
					
				//	if (y>x) {
				//		x=y+2;	
				//	}
					randomNumber = Math.floor(Math.random() * (1+randomMaxNumbers - randomMinNumbers))+ randomMinNumbers;
				///	if (x == y) {
				//		x = y+1;
				//	}
				}
				
				if ( x >= FP.stage.width /1.5) {
					//x = 0;
					x = FP.stage.width / 1.5;
					randomNumber2 = Math.floor(Math.random() * (1+randomMaxNumbers - randomMinNumbers))+ randomMinNumbers;
					if (x == y) {
						x = y+1;
					}
				}
				

				
				// end HelloWorld.update
			}
			
			
			
		
		}
	}