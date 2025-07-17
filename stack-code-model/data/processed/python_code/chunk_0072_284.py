package
{
	import flash.display.MovieClip;
	import flash.display.Shape;
	import flash.events.Event;
	import flash.events.MouseEvent;
	public class ChargingLaser extends MovieClip
	{
		
		private var angle:int;
		public var type:String;
		public var turret:MovieClip;
		private var time:int;
		var xPos;
		var yPos
		var Online;
		var Target:Object;
		var damage = 1;
		var laserTime:int;
		var laser:Shape;
		var Energy:int;
		var EnergyMax:int;
		var Shooting:Boolean
		var EnergyCost;
		var CanShoot;
		var sound;
		var range;
		function ChargingLaser(_x,_y,Type)
		{
			range = 200;
			this.buttonMode = true;
			sound = null;
			CanShoot = true;
			Shooting = false;
			EnergyCost = 6;
			EnergyMax = 450;
			Energy = 0;
			Online = true;
			x = Math.round(_x);
			y = Math.round(_y);
			type = Type;
			angle = 180;
			xPos = Math.floor(x/100);
			yPos = Math.floor(y/100);
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
			if(Shooting == true)
			{
				if(sound == null)
				{
					sound = Sounds.LaserSound();
				}
			}else{
				if(sound!= null)
				{
					sound.stop()
					sound = null;
				}
			}
			ChargeBar.width = 17 * Energy / EnergyMax;
			if(Energy < EnergyMax)
			{
				Energy+=1;
			}
			laserTime ++;
			time++;
			
			if(laser!=null)
			{
				if(laserTime > 2)
				{
					removeChild(laser);
					laser = null;
				}
			}
			if(Target == null)
			{
				Shooting = false;
				GetTarget();
					
			}else{
				if(Energy > 0)
				{
					Shooting = true;
					if(laser!= null)
					{
						removeChild(laser)
						laser = null;
					}
					ChangeAngle();
					laser = ShootBullet();
					Energy-=EnergyCost;
				}else{
					Shooting = false;
				}
			}
		}
		function ChangeAngle()
		{
			var dx:Number = Target.x - this.x;
			var dy:Number = Target.y - this.y;
			var Angle:Number=  Math.atan2(dx,dy)/Math.PI*180;
			angle = Angle;
			turret.rotation = -angle-180;
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
							if(Distance < LowestDistance)
							{
								LowestDistance = Distance;
								Target = grid[q+2][w+2][i];
								return;
							}
						}
					}
				}
			}
			return Target = null;
		}
		public function ShootBullet()
		{
			var l = DrawLaser();
			Target.Damage(damage,Target.x,Target.y);
			GetTarget();
			return l;
		}
		public function DrawLaser():Shape
		{
			laserTime = 0;
			var l:Shape = new Shape;
			addChild(l);
			l.x = turret.x+Math.sin((angle)*Math.PI/180)*20;
			l.y = turret.y+Math.cos((angle)*Math.PI/180)*20;
			l.graphics.lineStyle(5, 0x00FF00, 1);
			l.graphics.lineTo(Target.x-x, Target.y-y);
			
			return l;
		}
		public function remove()
		{
			if(this.sound != undefined)
			{
				this.sound.stop();
			}
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
			if(this.sound != undefined)
			{
				this.sound.stop();
			}
			removeEventListener(MouseEvent.MOUSE_UP, onClick);
			removeEventListener(Event.ENTER_FRAME,enterFrame)
		}
		public function Resume()
		{
			if(this.sound != undefined)
			{
				this.sound.play();
			}
			addEventListener(MouseEvent.MOUSE_UP, onClick);
			addEventListener(Event.ENTER_FRAME,enterFrame)
		}
	}
}