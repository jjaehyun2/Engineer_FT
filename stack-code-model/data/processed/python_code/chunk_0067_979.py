package
{
	import flash.display.MovieClip;
	import flash.events.Event;
	public class Flak extends MovieClip
	{
		var Removed:Boolean;
		private const speed:int = 8;
		private var damage:int;
		private var xPos;
		private var yPos;
		var time:int;
		var xSpeed:Number;
		var ySpeed:Number;
		public function Flak(_x,_y):void
		{
			xSpeed = Math.random()*2-1;
			ySpeed = Math.random()*2-1;
			rotation = Math.random()*360
			stop();
			time = 0;
			Removed = false;
			x=_x;
			y=_y;
			xPos = Math.floor(x/100);
			yPos = Math.floor(y/100);
			damage = 3;
			addEventListener("enterFrame",enterFrame);
		}
		function damageAOE(_x,_y)
		{
			var grid:Array = Game.grid;
			for(var q = _x-1;q<=_x+1;q++)
			{
				for(var w = _y-1;w<=_y;w++)
				{
					for(var i in grid[q+2][w+2])
					{
						var Distance = CheckDistance(grid[q+2][w+2][i].x,grid[q+2][w+2][i].y,this.x,this.y);
						if(Distance < 50)
						{
							grid[q+2][w+2][i].Damage(damage,grid[q+2][w+2][i].x,grid[q+2][w+2][i].y);
						}
					}
				}
			}
		}
		function CheckDistance(ax,ay,bx,by)
		{
			var dx=ax - bx
			var dy=ay - by
			var d:Number=Math.sqrt(dx*dx+dy*dy)
			return d;
		}
		public function enterFrame(e:Event):void
		{
			time++;
			if(time == 15)
			{
				Sounds.NewSound("flakCannonSFX");
				damageAOE(xPos,yPos);
				play();
			}
			if(time > 15)
			{
				x+=xSpeed;
				y+=ySpeed;
			}
			if(currentFrame == totalFrames)
			{
				remove();
			}
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