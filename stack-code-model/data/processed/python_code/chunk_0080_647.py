package
{
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.media.SoundChannel;
	public class ClusterUnit extends Enemy
	{
		public var speedY:int;
		public var speedY2:int;
		public var speedX:int;
		private var damage:int;
		private var grid:Array = Game.grid;
		private var speed:Number;
		public var health:int;
		var xPos;
		var yPos;
		var xPos2;
		var yPos2;
		var impactTime:int;
		var impact:Boolean;
		var removed:Boolean = false;
		var target:Object;
		var position:int;
		public var positionXY:Array;
		var randomFrame:int;
		var time:int;
		function ClusterUnit(_x,_y,Target,Position)
		{
			isStunnable = false;
			positionXY = [0,1,2,3,4,5,6]
			positionXY[0]=[0,0]
			positionXY[1]=[-22,40]
			positionXY[2]=[22,40]
			positionXY[3]=[45,0]
			positionXY[4]=[22,-40]
			positionXY[5]=[-22,-40]
			positionXY[6]=[-45,0]
			target = Target;
			speedY2 = target.speedY;
			position = Position;
			target.position[position]=this
			impactTime = Math.random()*10+5
			x = target.x;
			y = target.y;
			damage = 15;
			health = 3;
			xPos = Math.floor(x/100);
			yPos = Math.floor(y/100);
			xPos2 = Math.floor(x/100);
			yPos2 = Math.floor(y/100);
			ChangeGridPosition(xPos,yPos);
			speed=5;
			speedX=0;
			speedY=0;
			//addEventListener(MouseEvent.MOUSE_DOWN, onClick);
			addEventListener("enterFrame",enterFrame);
			time = Math.random()*3+1
			
		}
		/*public function onClick(e:MouseEvent)
		{
			
			Damage (1,e.stageX,e.stageY);
			Game.NewBulletParticle(e.stageX,e.stageY,2);
			
		}*/
		public function ChangeGridPosition(_x,_y)
		{
			RemoveGridPosition(xPos2,yPos2);
			grid[_x+2][_y+2].push(this);
			xPos2 = xPos;
			yPos2 = yPos;
		}
		public function RemoveGridPosition(_x,_y)
		{
			for(var i in grid[_x+2][_y+2])
			{
				if( grid[_x+2][_y+2][i]==this)
				{
					grid[_x+2][_y+2].splice(i,1);
					break;
				}
			}
		}
		/*public function moveTo(index)
		{
			position=index;
		}*/
		public function moveTo(index)
		{
			var targetX = target.x+positionXY[index][0];
			var targetY = target.y+positionXY[index][1];
			var dx = targetX-x;
			var dy = targetY-y;
			var c = Math.sqrt(dx*dx+dy*dy);
			var steps = c/speed;
			if(steps >= 1)
			{
				x+=dx/steps;
				y+=dy/steps;
			}else{
				x = targetX;
				y = targetY;
			}
		}
		public function enterFrame(e:Event)
		{
			time --;
			if(time < 1)
			{
				randomFrame = Math.round(Math.random()*(totalFrames)+1);
				gotoAndStop(randomFrame)
				time = Math.random()*3+1
			}
			
			moveTo(position);
			y += speedY2;
			xPos = Math.floor(x/100);
			yPos = Math.floor(y/100);
			if(xPos != xPos2)
			{
				ChangeGridPosition(xPos,yPos);
			}
			
			if(yPos != yPos2)
			{
				ChangeGridPosition(xPos,yPos);
			}
			if(Game.bigPlanet.hitTest.hitTestPoint(this.x,this.y,true))
			{
				impact = true;
			}
			if(impact == true)
			{
				Impact();
			}else{
				if(y > 650)
				{
					Sounds.NewSound("enemyImpactSFX");
					Game.ChangePlanetHealth(damage);
					remove();
					return;
				}
				else if(x > 550)
				{
					remove();
					return;
				}
				else if(x <-50)
				{
					remove();
					return;
				}
			}
		}
		public function Impact()
		{
			impactTime --;
			if(impactTime < 0)
			{
				Sounds.NewSound("enemyImpactSFX");
				Game.ChangePlanetHealth(damage);
				Game.NewParticle(this.x,this.y,"ImpactExplosion",1);
				Game.NewParticle(x,y,"BlueCube",5);
				Game.NewParticle(x,y,"AsteroidBits",3);
				Game.NewImpactParticle(this.x,this.y,"BlueCubeImpact",null,null,1);
				
				remove();
			}
		}
		public function remove()
		{
			if(removed == false)
			{
				RemoveGridPosition(xPos,yPos);
				removeEventListener("enterFrame",enterFrame);
				target.position[position]="Empty"
				target.units -= 1;
				parent.removeChild(this);
				removed = true;
				
			}
					
		}
		public function Damage(damage,_x,_y)
		{
			Sounds.NewSound("enemyHitSFX");
			
			
			
			if(health-damage > 0)
			{
				
				Game.NewParticle(_x,_y,"BlueCube",damage);
				
				health -= damage;
			}else{
				
				Game.NewParticle(_x,_y,"BlueCube",5);

				
				remove();
			}
		}
		public function Pause()
		{
			//removeEventListener(MouseEvent.MOUSE_DOWN, onClick);
			removeEventListener(Event.ENTER_FRAME,enterFrame)
		}
		public function Resume()
		{
			//addEventListener(MouseEvent.MOUSE_DOWN, onClick);
			addEventListener(Event.ENTER_FRAME,enterFrame)
		}
	}
}