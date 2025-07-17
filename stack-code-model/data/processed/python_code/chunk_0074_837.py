package  
{
	import flash.geom.Point;
	import net.flashpunk.Entity;
	import net.flashpunk.utils.Input;
	import net.flashpunk.FP;
	
	/**
	 * ...
	 * @author Joseph O'Connor
	 */
	public class Pointer extends Entity 
	{
		public static const  down:int = 0;
		public static const    up:int = 1;
		public static const click:int = 2;
		public static const  drag:int = 3;
		
		public var pointerState:int   = up;
		public var currentPoint:Point = new Point();
		public var    downPoint:Point = new Point();
		public var      upPoint:Point = new Point();
		public var    dragPoint:Point = new Point();
		
		public function Pointer() 
		{
			setHitbox(1, 1, 0, 0);
			type = "Pointer";
			x = 0;
			y = 0;
		}
		
		override public function update():void 
		{
			x = currentPoint.x = FP.world.mouseX;
			y = currentPoint.y = FP.world.mouseY;
			
			if (pointerState == click)
			{
				pointerState = up;
				//trace("Clicked!");
			}
			
			if (Input.mousePressed)
			{
				pointerState = down;
				downPoint.x = FP.world.mouseX;
				downPoint.y = FP.world.mouseY;
				
				upPoint.x = -1;
				upPoint.y = -1;
				
				//trace("MouseDown x: " + downPoint.x + " y: " + downPoint.y);
			}
			else if (Input.mouseDown)
			{
				pointerState = drag;				
				dragPoint.x = -1 * (downPoint.x - currentPoint.x);
				dragPoint.y = -1 * (downPoint.y - currentPoint.y);
				//trace("MouseDrag x: " + dragPoint.x + " y: " + dragPoint.y);
			}
			
			if (Input.mouseReleased)
			{
				if (dragPoint.x == 0 && dragPoint.y == 0)
				{
					pointerState = click;
				}
				else
				{
					pointerState = up;
				}
				
				upPoint.x = FP.world.mouseX;
				upPoint.y = FP.world.mouseY;
				
				downPoint.x = -1;
				downPoint.y = -1;
				
				//trace("MouseUp x: " + upPoint.x + " y: " + upPoint.y);
			}
			
			super.update();
		}
	}

}