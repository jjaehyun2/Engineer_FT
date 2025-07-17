package
{
	import flash.display.MovieClip;
	import flash.events.Event;
	public class Bullet extends MovieClip
	{
		var Removed:Boolean;
		private const speed:int = 8;
		private var damage:int;
		private var xPos;
		private var yPos;
		public function Bullet(_x,_y):void
		{
			Removed = false;
			x=_x;
			y=_y;
			
			damage = 5;
			addEventListener("enterFrame",enterFrame);
		}
		public function CheckGridCollision(_x,_y)
		{
			var grid:Array = Game.grid;
			for(var q = _x-1;q<=_x+1;q++)
			{
				for(var w = _y-1;w<=_y;w++)
				{
					for(var i in grid[q+2][w+2])
					{
						if(grid[q+2][w+2][i].hitTestObject(this))
						{
							if(this.damage > 0)
							{
								var dmg:int = this.damage;
								this.damage -= grid[q+2][w+2][i].health;
								grid[q+2][w+2][i].Damage(dmg,this.x,this.y);
								dmg = 0;
								Game.NewBulletParticle(this.x,this.y,1);
								if(this.damage < 1)
								{
									remove();
								}
								break;
							}
						}
					}
				}
			}
		}
		public function enterFrame(e:Event):void
		{
			xPos = Math.floor(x/100);
			yPos = Math.floor(y/100);
			CheckGridCollision(xPos,yPos);
			y -= speed;
			if(y < 0)
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