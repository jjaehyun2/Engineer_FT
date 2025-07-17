package
{
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.geom.Transform;
	import flash.geom.ColorTransform;
	import fl.motion.Color;
	import flash.media.SoundChannel;
	public class Asteroid extends Enemy
	{
		private var damage:int;
		private var grid:Array = Game.grid;
		public var speedY:Number;
		public var speedX:Number;
		public var size:int;
		public var health:int;
		private var color:Color = new Color();    
		var xPos;
		var yPos;
		var xPos2;
		var yPos2;
		var c:int;
		var impactTime:int;
		var impact:Boolean;
		var removed:Boolean = false;
		
		
		function Asteroid(_x,_y,Size)
		{
			
			impactTime = Math.random()*10+5
			c = 0;
			color.brightness = 0;
			if(_x == "default")
			{
				x = Math.random()*460+20;
			}else{
				x = _x;
			}
			if(_y == "default")
			{
				y = -50;
			}else{
				y = _y;
			}
			size=Size;
			if(size > 2)
			{
				isStunnable =false;
			}
			if(size == 1)
			{
				speedY = Math.random()*5+3;
				speedX = Math.random()*2-1;
				damage = 25
				health = 2
			}
			if(size == 2)
			{
				speedY = Math.random()*3+2;
				speedX = Math.random()*1-1;
				damage = 50
				health = 5
			}
			if(size == 3)
			{
				speedY = Math.random()*3+2;
				speedX = Math.random()*1-1;
				damage = 75
				health = 15
			}
			if(size == 4)
			{
				speedY = Math.random()*3+2;
				speedX = Math.random()*1-1;
				damage = 250
				health = 60
			}
			xPos = Math.floor(x/100);
			yPos = Math.floor(y/100);
			xPos2 = Math.floor(x/100);
			yPos2 = Math.floor(y/100);
			ChangeGridPosition(xPos,yPos);
			rotation = Math.random()*360;
			
			
			gotoAndStop(size);
			//addEventListener(MouseEvent.MOUSE_DOWN, onClick);
			addEventListener(Event.ENTER_FRAME,enterFrame);
			
			
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
		public function enterFrame(e:Event)
		{
			
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
			if(stunTime > 0)
			{
				stunTime --;
			}else{
				y += speedY;
				x += speedX;
				stunned = false;
			}
			if(impact == true)
			{
				Impact();
			}else{
				if(y > 650)
				{
					if(x < 500) 
					{
						if(x > 0)
						{
							Sounds.NewSound("enemyImpactSFX");
							Game.ChangePlanetHealth(damage);
							remove();
							return;
						}else{
							remove();
						}
					}else{
						remove();
					}
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
			if(color.brightness > 0)
			{
				c ++;
				if(c == 2)
				{
					color.brightness = 0;
					transform.colorTransform = color;
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
				Game.NewParticle(x,y,"AsteroidBits",size*3);
				Game.NewParticle(this.x,this.y,"DirtCloud",size*2);
				Game.NewImpactParticle(this.x,this.y,"ImpactParticle",null,null,1);
				
				remove();
			}
		}
		public function remove()
		{
			if(removed == false)
			{
				RemoveGridPosition(xPos,yPos);
				removeEventListener("enterFrame",enterFrame);
				parent.removeChild(this);
				removed = true;
			}
		}
		public function Damage(damage,_x,_y)
		{
			Sounds.NewSound("enemyHitSFX");
			
			
			
			if(health-damage > 0)
			{
				
				Game.NewParticle(_x,_y,"DirtCloud",damage);
				
				health -= damage;
			}else{
				if(removed == false)
				{
					Game.NewParticle(x,y,"AsteroidBits",size*2);
					Game.NewParticle(_x,_y,"DirtCloud",health);
					
					if(size > 1)
					{
	
						Game.NewEnemy(x+Math.random()*10-5,y,"Asteroid"+(size-1));
						Game.NewEnemy(x+Math.random()*10-5,y,"Asteroid"+(size-1));
					}
				}
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