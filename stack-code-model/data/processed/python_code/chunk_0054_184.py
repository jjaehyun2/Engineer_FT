package
{
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.media.SoundChannel;
	public class Cluster extends MovieClip
	{
		private var damage:int;
		private var grid:Array = Game.grid;
		public var speedY:Number;
		public var speedX:Number;
		public var health:int;
		var xPos;
		var yPos;
		var xPos2;
		var yPos2;
		var impactTime:int;
		var impact:Boolean;
		var removed:Boolean = false;
		var position:Array;
		var units:int;
		var time:int;
		var time2:int;
		var cooldown:int;
		function Cluster(_x,_y)
		{
			lightning.light1.gotoAndPlay(Math.random()*(totalFrames)+1)
			lightning.light2.gotoAndPlay(Math.random()*(totalFrames)+1)
			lightning.light3.gotoAndPlay(Math.random()*(totalFrames)+1)
			
			
			cooldown = 30;
			position=["Empty","Empty","Empty","Empty","Empty","Empty","Empty"];
			if(_x == "default")
			{
				x = Math.random()*400+50;
			}else{
				x = _x;
			}
			if(_y == "default")
			{
				y = -50;
			}else{
				y = _y;
			}
			
			//addEventListener(MouseEvent.MOUSE_DOWN, onClick);
			addEventListener("enterFrame",enterFrame);
			speedY = 2;
			
			units = 7;
			speedX = 0;
			time2 = 0;
		}
		public function enterFrame(e:Event)
		{
			lightning.rotation -= 1
			
			if(position[0]!="Empty")
			{
				time = 0;
				if(units<7)MoveCenterUnit();
			}else{
				
				time++;
				if(time>= cooldown)
				{
					Game.NewClusterUnit(x,y,this,0);
					units ++;
					time = 0;
					var c = parent.numChildren -1;
					parent.setChildIndex(this, c);
				}
			}
			y += speedY;
			time2++;
			if(time2>= cooldown*2)
			{
				rotateUnits();
				time2 = 0
			}
			if (units == 0)
			{
				remove();
			}
			if(units == 7)
			{
				anim.gotoAndStop(1);
			}else{
				anim.play();
			}
		}
		public function rotateUnits():void
		{
			var p0=position[0]
			var p1=position[1]
			var p2=position[2]
			var p3=position[3]
			var p4=position[4]
			var p5=position[5]
			var p6=position[6]
			for(var o in p2)
			{
				//trace(p2[o].position);
				//trace(position[o].position);
			}
			for(var i=1;i <6;i++)
			{
				if(position[i] != "Empty")
				{
					position[i].position=i+1;
				}
			}
			if(position[6] != "Empty")
			{
				position[6].position=1;
			}
			position = [p0,p6,p1,p2,p3,p4,p5];
			
			return;
		}
		public function remove()
		{
			if(removed == false)
			{
				Game.NewParticle(x,y,"Lightning",7);
				removeEventListener("enterFrame",enterFrame);
				parent.removeChild(this);
				removed = true;
			}
					
		}
		public function MoveCenterUnit()
		{
			for(var i in position)
			{
				if(i!=0)
				{
					if(position[i] == "Empty")
					{
						var index = i;
						break;
					}
				}
			}
			MoveUnit(0,index);
		}
		public function MoveUnit(from,to)
		{
			position[from].position=to;
			position[to] = position[from];
			position[from] = "Empty";
			
		}
		public function Pause()
		{
			lightning.light1.stop();
			lightning.light2.stop();
			lightning.light3.stop();
			anim.stop();
			//removeEventListener(MouseEvent.MOUSE_DOWN, onClick);
			removeEventListener(Event.ENTER_FRAME,enterFrame)
		}
		public function Resume()
		{
			//addEventListener(MouseEvent.MOUSE_DOWN, onClick);
			lightning.light1.play();
			lightning.light2.play();
			lightning.light3.play();
			anim.play();
			addEventListener(Event.ENTER_FRAME,enterFrame)
		}
	}
}