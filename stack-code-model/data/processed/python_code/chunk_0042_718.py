package 
{
	import flash.display.Bitmap;
	import flash.display.Loader;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.net.URLRequest;
	
	/**
	 * ...
	 * @author Mike
	 */
	public class EndScreen extends Sprite
	{
		public var _BgMovieClip:Loader = new Loader();
		//[Embed(source = "lib/eindscherm.png")]
		
		//private var backgroundImage:Class;
		//private var bgImage:Bitmap;
		
		
		
		public function EndScreen() 
		{
			this.addEventListener(Event.ADDED_TO_STAGE, init);
			_BgMovieClip.load(new URLRequest("../animations/screens/game_over_scherm.swf"));
			_BgMovieClip.scaleX = 1.25;
			_BgMovieClip.scaleY = 1.25;
			_BgMovieClip.x = -250;
			_BgMovieClip.y = -200;
		}  
		
		private function init(e:Event):void
		{
			//bgImage = new backgroundImage();
			//addChild(bgImage);
			//
			//var scale:Number =  stage.stageWidth / bgImage.width;
//
			//// if the height of the image will be taller than the stage,
			//// set the scale to fit the height of the image to the height of the stage
			//if(bgImage.height * scale <= stage.stageHeight){
				//scale = stage.stageHeight / bgImage.height;
			//}   
//
			//// apply the scale to the image
			//bgImage.scaleX = bgImage.scaleY = scale;
			
			addChild(_BgMovieClip);
			
			
		}
		
	}

}