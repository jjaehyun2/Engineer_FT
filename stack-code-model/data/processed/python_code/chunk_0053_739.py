package 
{
	import com.gestureworks.cml.core.CMLParser;
	import com.gestureworks.core.GestureWorks;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import com.gestureworks.core.GestureWorksAIR; GestureWorksAIR;
	

	[SWF(width = "1280", height = "720", backgroundColor = "0x333333", frameRate = "60")]

	public class Main extends GestureWorks
	{
		public function Main():void 
		{
			super();
			fullscreen = true;
			stage.scaleMode = StageScaleMode.NO_SCALE;
			stage.align = StageAlign.TOP_LEFT;
			
			key = "cl3ar";
			
			cml = "library/cml/GigapixelElement.cml";
			CMLParser.instance.addEventListener(CMLParser.COMPLETE, cmlInit);
		}
				
		override protected function gestureworksInit():void
 		{
			trace("gestureWorksInit()");			
		}
				
		private function cmlInit(event:Event):void
		{
			trace("cmlInit()");
		}
	}
}