package 
{
	import flash.display.Sprite;
	import flash.display.Stage;
	import flash.display.NativeWindow;
	import flash.events.Event;
	
	/**
	 * ...
	 * @author Jake
	 */
	[SWF(backgroundColor= "0xFFFFFF", width="1366", height ="768", frameRate='30')]
	public class Main extends Sprite 
	{
		public function Main():void 
		{
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void 
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);
			addChild(new PrintPage(stage));
		}
	}

}