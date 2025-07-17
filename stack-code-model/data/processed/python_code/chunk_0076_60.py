package
{
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;
	public class HomingCannon extends MovieClip
	{
		private var angle:int;
		private var time:int;
		private var time2:int;
		private var interval2:int;
		public var interval:int;
		public var type:String;
		private var cooldown:int;
		public var turret:MovieClip;
		var xPos;
		var yPos
		var Online;
		var Target:Object;
		var range;
		function HomingCannon(_x,_y,Type)
		{
			range = 200;
			this.buttonMode = true;
			cooldown = 15;
			Online = true;
			x = Math.round(_x);
			y = Math.round(_y);
			type = Type;
			angle = 180;
			interval = 1;
			interval2 = 9;
			xPos = Math.floor(x/100);
			yPos = Math.floor(y/100);
			time = interval;
			addEventListener(Event.ENTER_FRAME,enterFrame);
			addEventListener(MouseEvent.MOUSE_DOWN, onClick);
			addEventListener(MouseEvent.MOUSE_OVER,onRollOver);
			addEventListener(MouseEvent.MOUSE_OUT,onRollOut);
		}
		function onClick(e:MouseEvent)
		{
			FakeCannon.DragOn(this,type);
		}
		public function onRollOver(e:MouseEvent)
		{
			Game.range.x = this.x;
			Game.range.y = this.y;
			Game.range.height = range*2;
			Game.range.width = range*2;
		}
		public function onRollOut(e:MouseEvent)
		{
			Game.range.x = 5000;
			Game.range.y = 5000;
		}
		public function enterFrame(e:Event)
		{
			turret.glow.alpha = time/15
			
			time++;
			time2++;
			if(time2 < interval2)
			{
				GetTarget();
				if(Target != null)
				{
					
					ChangeAngle();
					if(time > interval)
					{
						ShootBullet();
						Target = null;
						time = 0;
					}
				}else{
					
					if(time2 > 0)
					{
						time2 -=2;
					}
				}
			}else{
				if(time2 > interval2 + cooldown)
				{
					Target = null;
					time = 0;
					time2 = 0;
				}
			}
		}
		function ChangeAngle()
		{
			if(Target != null)
			{
				var dx:Number;
				var dy:Number;
				var Angle:Number;
				if(Target.stunned == false)
				{
					dx = Target.x - this.x;
					dy = Target.y - this.y;
					
					var a:Number = Target.speedX * Target.speedX + Target.speedY * Target.speedY - 12 * 12;
					var b:Number = 2 * (Target.speedX * dx + Target.speedY * dy);
					var c:Number = dx * dx + dy * dy;
					var q:Number = b * b - 4 * a * c;
					if (q < 0) return null;
					var t:Number = ((a < 0 ? -1 : 1)*Math.sqrt(q) - b) / (2 * a);
					dx += t * Target.speedX;
					dy += t * Target.speedY;
					Angle=  Math.atan2(dx,dy)/Math.PI*180;
					angle = Angle;
				}else{
					dx = Target.x - this.x;
					dy = Target.y - this.y;
					Angle=  Math.atan2(dx,dy)/Math.PI*180;
					angle = Angle;
				}
				
			}
			turret.rotation = -angle-180;
			/*if(Target != null)
			{
				var t = CheckDistance(Target.x,Target.y,this.x,this.y)/12;
				
				var posX = Target.x + Target.speedX*t;
				var posY = Target.y + Target.speedY*t;
			}
			var dy:Number = posY-y;
			var dx:Number = posX-x;*/
			
			//angle:Number =;
			
		}
		function CheckDistance(ax,ay,bx,by)
		{
			var dx=ax - bx
			var dy=ay - by
			var d:Number=Math.sqrt(dx*dx+dy*dy)
			return d;
		}
		function GetTarget()
		{
			
			var _x = xPos
			var _y = yPos
			var Distance:int;
			var LowestDistance:int = 9999;;
			var grid:Array = Game.grid;
			for(var q = _x+2;q>=_x-2;q--)
			{
				for(var w = _y+2;w>=_y-2;w--)
				{
					for(var i in grid[q+2][w+2])
					{
						Distance = CheckDistance(grid[q+2][w+2][i].x,grid[q+2][w+2][i].y,this.x,this.y);
						if(Distance < range)
						{
							if(Distance < LowestDistance)
							{
								LowestDistance = Distance;
								Target = grid[q+2][w+2][i];
								
							}
						}
					}
				}
			}
			
			
		}
		public function ShootBullet()
		{
			Game.NewShell(x,y,angle-180)
			Sounds.NewSound("weapon1SFX");
			Game.NewBullet(x,y,type,angle+Math.random()*10-5);
		}
		public function remove()
		{
			
			var cannons:Array = Game.cannons;
			for(var i in cannons)
			{
				if(cannons[i] == this)
				{
					
					cannons.splice(i,1);
					break;
				}
			}
			removeEventListener(Event.ENTER_FRAME,enterFrame);
			removeEventListener(MouseEvent.CLICK, onClick);
			parent.removeChild(this);
		}
		function GoOffline()
		{
			
			Online = false;
			alpha = 0.50;
			removeEventListener(Event.ENTER_FRAME, enterFrame);
		}
		function GoOnline()
		{
			xPos = Math.floor(x/100);
			yPos = Math.floor(y/100);
			Online = true;
			alpha = 1;
			addEventListener(Event.ENTER_FRAME, enterFrame);
		}
		public function Pause()
		{
			removeEventListener(MouseEvent.MOUSE_UP, onClick);
			removeEventListener(Event.ENTER_FRAME,enterFrame)
		}
		public function Resume()
		{
			addEventListener(MouseEvent.MOUSE_UP, onClick);
			addEventListener(Event.ENTER_FRAME,enterFrame)
		}
	}
}