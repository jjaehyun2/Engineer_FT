package
{
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.utils.getTimer;
	
	import bt.BTCreator;
	
	import org.hammerc.archer.bt.BehaviorTree;
	
	[SWF(width="800", height="600", frameRate="60")]
	public class BTTest extends Sprite
	{
		private var _shape:Shape = new Shape();
		
		private var _lastTime:int;
		
		private var _tree:BehaviorTree;
		
		public function BTTest()
		{
			if(stage)
			{
				init();
			}
			else
			{
				addEventListener(Event.ADDED_TO_STAGE, init);
			}
		}
		
		private function init():void
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);
			
			_shape.x = 400;
			_shape.y = 300;
			_shape.graphics.beginFill(0xff0000);
			_shape.graphics.drawRect(-50, -50, 100, 100);
			_shape.graphics.endFill();
			addChild(_shape);
			
			BTCreator.init();
			
			_tree = new BehaviorTree();
			_tree.data = _shape;
			//actionTest
			//_tree.root = BTCreator.actionTest;
			//sequenceTest
			//_tree.root = BTCreator.sequenceTest;
			//selectorTest
			//_tree.root = BTCreator.selectorTest;
			//selectorRandomTest
			//_tree.root = BTCreator.selectorRandomTest;
			//parallelTest
			_tree.root = BTCreator.parallelTest;
			
			_tree.printTreeStructure();
			
			addEventListener(Event.ENTER_FRAME, enterFrameHandler);
			_lastTime = getTimer();
		}
		
		private function enterFrameHandler(event:Event):void
		{
			var now:int = getTimer();
			var interval:Number = (now - _lastTime) * 0.001;
			_tree.execute(interval);
			_lastTime = now;
		}
	}
}