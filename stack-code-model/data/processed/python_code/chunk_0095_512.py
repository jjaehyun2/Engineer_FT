package
{
	import flash.display.DisplayObject;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.geom.Point;
	
	import mx.events.SandboxMouseEvent;
	
	import spark.components.Button;
	import spark.components.SkinnableContainer;
	import spark.effects.Animate;
	import spark.effects.animation.MotionPath;
	import spark.effects.animation.SimpleMotionPath;
	
	/**
	 * A subclass of SkinnableContainer that initially doesn't display
	 * its elements, but provides a thumb Button that can be dragged to 
	 * expose them.
	 * 
	 * This is a simple implementation that only supports dragging.  It
	 * could be extended to support throw gestures as well.
	 */
	public class WindowShade extends SkinnableContainer
	{
		[Bindable]
		[SkinPart(required="true")]
		
		/** The Button that is dragged to resize the contentGroup */
		public var thumbButton:Button;
		
		/** Distance from the top of the button to the mouseDown position */
		private var mouseDownYOffset:Number = 0;
		
		private var animation:Animate;
		private var animationPath:SimpleMotionPath;
		
		public function WindowShade()
		{
			super();
			
			animationPath = new SimpleMotionPath("height");
			
			animation = new Animate();
			animation.motionPaths = new Vector.<MotionPath>();
			animation.motionPaths.push(animationPath);
		}
		
		override protected function partAdded(partName:String, instance:Object):void
		{
			super.partAdded(partName, instance);
			
			if (instance == thumbButton)
			{
				thumbButton.addEventListener(MouseEvent.MOUSE_DOWN, thumbButton_mouseDownHandler);
			}
			
			if (instance == contentGroup)
			{
				// start the contentGroup with no height
				contentGroup.height = 0;
				
				// set the animation's target
				animation.target = contentGroup;
			}
		}
		
		private function thumbButton_mouseDownHandler(event:MouseEvent):void
		{
			mouseDownYOffset = event.localY;
			
			var sbRoot:DisplayObject = systemManager.getSandboxRoot();
			sbRoot.addEventListener(MouseEvent.MOUSE_MOVE, mouseMoveHandler, true);
			sbRoot.addEventListener(MouseEvent.MOUSE_UP, mouseUpHandler, true);
			sbRoot.addEventListener(SandboxMouseEvent.MOUSE_UP_SOMEWHERE, mouseUpHandler);
		}
		
		private function mouseMoveHandler(event:MouseEvent):void 
		{
			// change the size of the contentGroup
			var globalPoint:Point = localToGlobal(new Point(0, contentGroup.y));
			contentGroup.height = event.stageY - globalPoint.y  - mouseDownYOffset;
		}
		
		private function mouseUpHandler(event:Event):void 
		{
			// cleanup event listeners                
			var sbRoot:DisplayObject = systemManager.getSandboxRoot();
			sbRoot.removeEventListener(MouseEvent.MOUSE_MOVE, mouseMoveHandler, true);
			sbRoot.removeEventListener(MouseEvent.MOUSE_UP, mouseUpHandler, true);
			sbRoot.removeEventListener(SandboxMouseEvent.MOUSE_UP_SOMEWHERE, mouseUpHandler);
			
			if (event is MouseEvent)
			{
				// play an effect to change the size of this container 
				if ((event as MouseEvent).stageY < stage.stageHeight / 2)
					close();
				else
					open();
			}
			
		}
		
		private function animateSize(from:Number, to:Number):void 
		{
			animationPath.valueFrom = from;
			animationPath.valueTo = to;
			animation.play();
		}
		
		/** Brings the height to zero */
		public function close():void 
		{
			animateSize(contentGroup.height, 0);
		}
		
		/** Brings the height to the max available in its parent */
		public function open():void 
		{
			animateSize(contentGroup.height, 
				parent.height - thumbButton.height - contentGroup.y - y);
		}
	}
}