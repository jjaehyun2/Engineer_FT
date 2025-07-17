package {
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.text.TextField;

	import Helpers.Console;

	public class Main extends Sprite {

		public function Main(){
			try {
				stage.align = StageAlign.TOP_LEFT;
				stage.scaleMode = StageScaleMode.EXACT_FIT;
	
				var txt:TextField = new TextField();
				txt.text = "Hello World";
				addChild(txt);
			}
			catch(e:Error){
				Console.log(e.message);
			}
		}
	}
}