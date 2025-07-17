package  {
	
	import flash.geom.Point;
	import flash.events.TimerEvent;
	import flash.utils.Timer;
	import starling.display.Image;
	import starling.display.Sprite;
	import starling.display.Stage;	
	import starling.events.Event;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;
	import starling.text.TextField;
	import starling.textures.TextureSmoothing;
	import starling.utils.HAlign;
	import starling.utils.VAlign;
	
	
	public class Tutorial {
		
		static var dotWidth = int(Environment.rectSprite.width*0.1734375);
		static var tutorialTextIntro:TextField;
		static var tutSprite:Sprite;
		
		
		static function display(stage:Stage) {
			
			// TUTORIAL BOARD
			tutSprite = new Sprite();
			stage.addChild(tutSprite);
			Screens.tutorialScreenObjects.push(tutSprite);
			var boardFiller:Image = Atlas.generate("filler");
			boardFiller.width = dotWidth*5;
			boardFiller.height = dotWidth*5;
			tutSprite.addChild(boardFiller);
			boardFiller.touchable = false;
			boardFiller.visible = false;
			tutSprite.x = int(Environment.rectSprite.x + Environment.rectSprite.width/2 - tutSprite.width/2);
			tutSprite.y = int((Environment.rectSprite.height*0.2966) - dotWidth + Environment.rectSprite.y);
			
			// EXAMPLES
			Example1.setup(stage, dotWidth);
		}
		
		
		static function finish() {
			Data.saveObj.firstPlay = false;
			Screens.setIntro();
		}
	}
}