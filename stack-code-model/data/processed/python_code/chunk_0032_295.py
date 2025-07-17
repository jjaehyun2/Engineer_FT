package
{
	import flash.display.MovieClip;
	import flash.events.Event;
	public class Laser extends MovieClip
	{
		var Removed:Boolean;
		private var damage:int;
		private var xPos:int;
		private var yPos:int;
		private var i:int;
		public function Laser(_x,_y):void
		{
			Removed = false;
			x=_x;
			y=_y;
			xPos = Math.floor(x/100);
			yPos = Math.floor(y/100);
			damage = 4;
			addEventListener("enterFrame",enterFrame);
		}
		public function CheckGridCollision(_x,_y)
		{
			var grid:Array = Game.grid;
			for(var q = _x-1;q<=_x+1;q++)
			{
				for(var w = _y-6;w<=_y;w++)
				{
					for(var i in grid[q+2][w+2])
					{
						if(grid[q+2][w+2][i].hitTestObject(this))
						{
							Game.NewBulletParticle(grid[q+2][w+2][i].x,grid[q+2][w+2][i].y,4);
							grid[q+2][w+2][i].Damage(damage,this.x,grid[q+2][w+2][i].y);
							break;
						}
					}
				}
			}
		}
		public function enterFrame(e:Event):void
		{
			i ++;
			
			if(i > 1)
			{
				remove();
			}
			
			CheckGridCollision(xPos,yPos);
		}
		public function remove():void
		{
			if(Removed == false)
			{
				removeEventListener("enterFrame",enterFrame);
				parent.removeChild(this);
				Removed = true;
			}
		}
		public function Pause()
		{

			removeEventListener(Event.ENTER_FRAME,enterFrame)
		}
		public function Resume()
		{

			addEventListener(Event.ENTER_FRAME,enterFrame)
		}
	}
}