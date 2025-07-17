package
{
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	
	public class FiveFactorial extends Sprite
	{
		public function FiveFactorial()
		{
			super();
			
			// support autoOrients
			stage.align = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.NO_SCALE;
			
			// displays the factorial of 5 in debug window
			trace("Result: " + factorial(5));
		}
		
		public function factorial(num:Number):Number {
			if (num <= 1) {
				return num;
			} else {
				return num * factorial(num - 1);
			}
		}
	}
}