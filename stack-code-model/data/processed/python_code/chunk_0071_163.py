package
{
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import starling.core.Starling;
	import starling.events.ResizeEvent;
	
	/**
	 * ...
	 * @author LeleoSan
	 */
	public class Main extends Sprite 
	{
		/** objects */
		private var starling:Starling;
		/** statics */
		public static const SIZE:Point = new Point(450, 768);
		
		public function Main() 
		{
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void 
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);
			
			stage.align = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.EXACT_FIT;
			
			Starling.handleLostContext = true;
			starling = new Starling(Root, stage);
			starling.antiAliasing = 1;
			//starling.showStats = true;
			starling.start();
			stage.addEventListener(ResizeEvent.RESIZE, resizeStage);
			resizeStage(null);
			addEventListener(Event.ENTER_FRAME, checking);
		}
		private function resizeStage(e:Event):void
		{
			var viewPortRectangle:Rectangle = new Rectangle();
			if (Main.SIZE.x > Main.SIZE.y) {
				viewPortRectangle.width = stage.stageWidth;
				viewPortRectangle.height = viewPortRectangle.width * 0.5859375;
				if (viewPortRectangle.height > stage.stageHeight) {
					viewPortRectangle.height = stage.stageHeight;
					viewPortRectangle.width = viewPortRectangle.height / 0.5859375;
				}
			} else {
				viewPortRectangle.height = stage.stageHeight;
				viewPortRectangle.width = viewPortRectangle.height * 0.5859375;
				if (viewPortRectangle.width > stage.stageWidth) {
					viewPortRectangle.width = stage.stageWidth;
					viewPortRectangle.height = viewPortRectangle.width / 0.5859375;
				}
			}
			//Centers the viewPort so you have black bars around it
			viewPortRectangle.x = (stage.stageWidth - viewPortRectangle.width) / 2;
			viewPortRectangle.y = (stage.stageHeight - viewPortRectangle.height) / 2;
			
			Starling.current.viewPort = viewPortRectangle;
		}
		private function checking(e:Event):void
		{
			if (starling.isStarted && starling.root) {
				removeEventListener(Event.ENTER_FRAME, checking);
				Object(starling.root).init();
			}
		}
		private function destroy():void
		{
			removeChildren();
			Root(starling.root).destroy();
			starling.removeEventListeners();
			starling.juggler.purge();
			starling.stop();
			starling.dispose();
			starling = null;
		}
	}
	
}