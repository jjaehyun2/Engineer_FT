package
{
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.media.SoundChannel;
	public class Carrier extends Enemy
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
		var removed:Boolean = false;
		var time;
		var cooldown;
		var whiteDelay:int;
		function Carrier(_x,_y)
		{
			whiteDelay = Math.random()*5;
			lightning.gotoAndPlay(Math.random()*(totalFrames)+1)
			isStunnable = false;
			cooldown = 40;
			time = 0;
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
			damage = 50;
			health = 100;
			xPos = Math.floor(x/100);
			yPos = Math.floor(y/100);
			xPos2 = Math.floor(x/100);
			yPos2 = Math.floor(y/100);
			ChangeGridPosition(xPos,yPos);
			speedX = 0;
			speedY = 0.5;
			
			addEventListener("enterFrame",enterFrame);
			
			
		}
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
			if(whiteDelay < 0)
			{
				if(white.visible == true)
				{
					white.visible = false;
				}else{
					white.visible = true;
				}
				whiteDelay = Math.random()*5;
			}
			whiteDelay --;
			time++;
			if(time >= cooldown)
			{
				Game.NewEnemy(this.x,this.y+50,"LightShip");
				time = 0;
			}
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
			if(y < 100) y += speedY;
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
				
				Game.NewParticle(_x,_y,"YellowShipParticle",damage);
				
				health -= damage;
			}else{
				
				Game.NewParticle(_x,_y,"YellowShipParticle",health);

				
				remove();
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