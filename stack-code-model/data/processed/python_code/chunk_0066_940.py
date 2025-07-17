package
{
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;
	public class EnergyPrison extends MovieClip
	{
		private var angle:int;
		public var type:String;
		private var cooldown:int;
		private var time:int;
		var xPos;
		var yPos
		var Online;
		var Target:Object;
		public static var stunTime:int = 30;
		var range;
		var d:int;
		function EnergyPrison(_x,_y,Type)
		{
			lightning.visible = false;
			anim.alpha = 0;
			range = 200;
			this.buttonMode = true;
			cooldown = 15;
			Online = true;
			x = Math.round(_x);
			y = Math.round(_y);
			type = Type;
			xPos = Math.floor(x/100);
			yPos = Math.floor(y/100);
			addEventListener(Event.ENTER_FRAME,enterFrame);
			hitBox.addEventListener(MouseEvent.MOUSE_DOWN, onClick);
			hitBox.addEventListener(MouseEvent.MOUSE_OVER,onRollOver);
			hitBox.addEventListener(MouseEvent.MOUSE_OUT,onRollOut);
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
			if(lightning.currentFrame == lightning.totalFrames)
			{
				lightning.visible = false;
				lightning.stop();
			}
			if(anim.alpha < 1)anim.alpha += 0.07;
			time++;
			if(time >= cooldown)
			{
				if(Target == null)
				{
					GetTarget();
				}else{
					ShootBullet();
					time = 0;
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
		function GetTarget()
		{
			var _x = xPos
			var _y = yPos
			var Distance:int;
			var LowestDistance:int = 9999;
			var grid:Array = Game.grid;
			for(var q = _x+2;q>=_x-2;q--)
			{
				for(var w = _y+2;w>=_y-2;w--)
				{
					for(var i in grid[q+2][w+2])
					{
						Distance = CheckDistance(grid[q+2][w+2][i].x,grid[q+2][w+2][i].y,this.x,this.y);
						if(Distance<range)
						{
							if(grid[q+2][w+2][i].stunned == false)
							{
								if(grid[q+2][w+2][i].isStunnable == true)
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
			}
		}
		public function ShootBullet()
		{
			anim.alpha = 0;
			Sounds.NewSound("energyPrisonSFX");
			Target.Stun(stunTime);
			Game.NewParticle(Target.x,Target.y,"Prison",1)
			DrawLightning();
			Target = null;
		}
		function DrawLightning()
		{
			lightning.gotoAndPlay(1);
			lightning.visible = true;
			
			var dx:Number = Target.x - this.x;
			var dy:Number = Target.y - this.y;
			var Distance = CheckDistance(Target.x,Target.y,this.x,this.y)
			var Angle:Number=  Math.atan2(dx,dy)/Math.PI*180;
			lightning.height = Distance;
			lightning.rotation = -Angle-180;
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
			hitBox.removeEventListener(MouseEvent.MOUSE_DOWN, onClick);
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
			hitBox.removeEventListener(MouseEvent.MOUSE_DOWN, onClick);
			removeEventListener(Event.ENTER_FRAME,enterFrame)
		}
		public function Resume()
		{
			hitBox.addEventListener(MouseEvent.MOUSE_DOWN, onClick);
			addEventListener(Event.ENTER_FRAME,enterFrame)
		}
	}
}