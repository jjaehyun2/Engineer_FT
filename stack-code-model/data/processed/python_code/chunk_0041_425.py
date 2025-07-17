package
{
	import flash.display.Sprite;
	
	public class Pong extends Sprite
	{
		
		private var ball:Sprite = new Sprite();
		private var rightPlayer:Sprite = new Sprite();
		private var leftPlayer:Sprite = new Sprite();
		
		public function Pong()
		{
			
			// Inicializacion
			
			ball.graphics.beginFill(0xff0000);
			ball.graphics.drawCircle(0,0,4);
			ball.graphics.endFill();
			ball.x = 250;
			ball.y = 187;
			
			rightPlayer.graphics.beginFill(0x00ff00);
			rightPlayer.graphics.drawRect(0, 0, 10, 50);
			rightPlayer.graphics.endFill();
			rightPlayer.y = 162;
			
			leftPlayer.graphics.beginFill(0x0000ff);
			leftPlayer.graphics.drawRect(0, 0, 10, 50);
			leftPlayer.graphics.endFill();
			leftPlayer.x = 490;
			leftPlayer.y = 162;
			
			// Dibujado
			addChild( ball );
			addChild( rightPlayer );
			addChild( leftPlayer );
			
		}
	}
}