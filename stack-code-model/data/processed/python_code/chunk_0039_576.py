package  {
	
	import flash.display.Sprite;
	import flash.display.Shape;
	
	public class Pixel extends Sprite {
		
		private const BLACK:Shape = Pixel.drawPixel(0x000000);
		private const RED:Shape = Pixel.drawPixel(0xFF0000);
		private const GREEN:Shape = Pixel.drawPixel(0x00FF00);
		private const BLUE:Shape = Pixel.drawPixel(0x0000FF);
		private const YELLOW:Shape = Pixel.drawPixel(0xFFFF00);
		private const MAGENTA:Shape = Pixel.drawPixel(0xFF00FF);
		private const CYAN:Shape = Pixel.drawPixel(0x00FFFF);
		private const WHITE:Shape = Pixel.drawPixel(0xFFFFFF);
		
		private static function drawPixel(color:int):Shape {
			var result:Shape = new Shape();
			result.graphics.beginFill(color);
			result.graphics.drawRect(0, 0, 1, 1);
			result.graphics.endFill();
			return result;
		}

		public function Pixel() {
			// constructor code
			addChild(BLACK);
			addChild(RED);
			addChild(GREEN);
			addChild(BLUE);
			addChild(YELLOW);
			addChild(MAGENTA);
			addChild(CYAN);
			addChild(WHITE);
		}
		
		public function changeColorPortion(red:Number, green:Number, blue:Number, yellow:Number, magenta:Number, cyan:Number, white:Number):void {
			RED.alpha = red;
			GREEN.alpha = green;
			BLUE.alpha = blue;
			YELLOW.alpha = yellow;
			MAGENTA.alpha = magenta;
			CYAN.alpha = cyan;
			WHITE.alpha = white;
		}

	}
	
}