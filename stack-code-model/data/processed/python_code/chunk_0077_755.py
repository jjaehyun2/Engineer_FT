package
{
	import flash.display.MovieClip;
	import flash.events.Event;
	public class Particle extends MovieClip
	{
		public var particle:MovieClip;
		private var type:String;
		private var xSpeed:Number;
		private var ySpeed:Number;
		private var EventListener;
		private var rotationSpeed;
		private var frame;
		private var time;
		private var impactTime;
		private var impact:Boolean;
		private var time2:int;
		var removed:Boolean;
		public function Particle(_x,_y,Type)
		{
			removed = false;
			if(Type == null)
			{
				remove();
			}
			gotoAndStop(Type);
			var particle:MovieClip;
			if(Type == "WhiteGlow")
			{
				x = _x;
				y = _y;
				xSpeed = Math.random()*1.5-0.75;
				ySpeed = Math.random()*2.5;
				addEventListener(Event.ENTER_FRAME,WhiteGlow)
				EventListener = WhiteGlow;
				
			}
			if(Type == "DirtCloud")
			{
				rotationSpeed = Math.random()*5-2.5
				x = _x;
				y = _y;
				xSpeed = Math.random()*2.5-1.25;
				ySpeed = Math.random()*2.5-1.25;
				scaleX = Math.random()*0.4+0.6
				scaleY = scaleX
				rotation = Math.random()*360;
				addEventListener(Event.ENTER_FRAME,DirtCloud)
				EventListener = DirtCloud;
				
			}
			if(Type == "BlackCloud")
			{
				rotationSpeed = Math.random()*5-2.5
				x = _x;
				y = _y;
				xSpeed = Math.random()*2.5-1.25;
				ySpeed = Math.random()*2.5-1.25;
				scaleX = Math.random()*0.4+0.6
				scaleY = scaleX;
				rotation = Math.random()*360;
				addEventListener(Event.ENTER_FRAME,DirtCloud)
				EventListener = DirtCloud;
				
			}
			if(Type == "Teleporter")
			{

				x = _x + Math.random()*50-25;
				y = _y + Math.random()*50-25;
				addEventListener(Event.ENTER_FRAME,Teleporter)
				EventListener = Teleporter;
				
			}
			if(Type == "BlueCube")
			{
				x = _x + Math.random()*20-10;
				y = _y + Math.random()*20-10;
				xSpeed = Math.random()*5-2.5
				ySpeed = Math.random()*5-2.5
				scaleX = Math.random()*0.4+0.6
				scaleY = scaleX
				addEventListener(Event.ENTER_FRAME,BlueCube)
				EventListener = BlueCube;
				
			}
			if(Type == "Lightning")
			{
				x = _x + Math.random()*100-50;
				y = _y + Math.random()*100-50;
				scaleX = Math.random()*0.4+0.6
				scaleY = scaleX
				rotation = Math.random()*360;
				addEventListener(Event.ENTER_FRAME,Lightning)
				EventListener = Lightning;
				time=0;
				time2=18;
				frame = Math.round(Math.random()*5+2);
			}
			if(Type == "ImpactExplosion")
			{
				x = _x;
				y = _y;
				addEventListener(Event.ENTER_FRAME,ImpactExplosion)
				EventListener = ImpactExplosion;
				
				
			}
			if(Type == "AsteroidBits")
			{
				type = Type;
				time = 0;
				frame = Math.round(Math.random()* 3 +2);
				rotationSpeed = Math.random()*12-6;
				scaleX = Math.random()*0.4+0.6;
				scaleY = scaleX;
				
				xSpeed = (Math.random()*12)-4;
				ySpeed = (Math.random()*12)-4;
				x = _x+xSpeed*2;
				y = _y+ySpeed*2;
				addEventListener(Event.ENTER_FRAME,AsteroidBits)
				EventListener = AsteroidBits;
				impactTime = Math.random()*12+3;
				impact = false;
				
				
			}
			if(Type == "WhiteShipParticle")
			{
				type = Type;
				time = 0;
				frame = 1;
				rotationSpeed = Math.random()*12-6;
				scaleX = Math.random()*0.4+0.6;
				scaleY = scaleX;
				
				xSpeed = (Math.random()*12)-4;
				ySpeed = (Math.random()*12)-4;
				x = _x+xSpeed*2;
				y = _y+ySpeed*2;
				addEventListener(Event.ENTER_FRAME,AsteroidBits)
				EventListener = AsteroidBits;
				impactTime = Math.random()*12+3;
				impact = false;
				
				
			}
			if(Type == "GreenShipParticle")
			{
				type = Type;
				time = 0;
				frame = 1;
				rotationSpeed = Math.random()*12-6;
				scaleX = Math.random()*0.4+0.6;
				scaleY = scaleX;
				
				xSpeed = (Math.random()*12)-4;
				ySpeed = (Math.random()*12)-4;
				x = _x+xSpeed*2;
				y = _y+ySpeed*2;
				addEventListener(Event.ENTER_FRAME,AsteroidBits)
				EventListener = AsteroidBits;
				impactTime = Math.random()*12+3;
				impact = false;
			}
			if(Type == "YellowShipParticle")
			{
				type = Type;
				time = 0;
				frame = 1;
				rotationSpeed = Math.random()*12-6;
				scaleX = Math.random()*0.4+0.6;
				scaleY = scaleX;
				
				xSpeed = (Math.random()*12)-4;
				ySpeed = (Math.random()*12)-4;
				x = _x+xSpeed*2;
				y = _y+ySpeed*2;
				addEventListener(Event.ENTER_FRAME,AsteroidBits)
				EventListener = AsteroidBits;
				impactTime = Math.random()*12+3;
				impact = false;
			}
			if(Type == "BlueShipParticle")
			{
				type = Type;
				time = 0;
				frame = 1;
				rotationSpeed = Math.random()*12-6;
				scaleX = Math.random()*0.4+0.6;
				scaleY = scaleX;
				
				xSpeed = (Math.random()*12)-4;
				ySpeed = (Math.random()*12)-4;
				x = _x+xSpeed*2;
				y = _y+ySpeed*2;
				addEventListener(Event.ENTER_FRAME,AsteroidBits)
				EventListener = AsteroidBits;
				impactTime = Math.random()*12+3;
				impact = false;
			}
			if(Type == "Prison")
			{
				time = 0;
				x = _x;
				y = _y;
				time2 = EnergyPrison.stunTime;
				addEventListener(Event.ENTER_FRAME,Prison)
				EventListener = Prison;
			}
		}
		function Prison(e:Event)
		{
			time ++;
			if(time > time2)
			{
				
				remove();
			}
		}
		function WhiteGlow(e:Event)
		{
			y -= ySpeed;
			x += xSpeed;
			alpha -= 0.02;
			if(alpha < 0)
			{
				remove();
			}
		}
		function Teleporter(e:Event)
		{
			alpha -= 0.04;
			if(alpha < 0)remove();
		}
		function Lightning(e:Event)
		{
			if(particle.currentFrame == 2)
			{
				particle.gotoAndPlay(frame);
			}
			if(particle.currentFrame == particle.totalFrames)
			{
				
				remove();
			}
		}
		function DirtCloud(e:Event)
		{
			rotation += rotationSpeed;
			y += ySpeed;
			x += xSpeed;
			
			alpha -= 0.01;
			if (alpha <= 0)
			{
				remove();
			}
		}
		function BlueCube(e:Event)
		{
			y += ySpeed;
			x += xSpeed;
			ySpeed*=0.9;
			xSpeed*=0.9;
			alpha -= 0.02;
			if (alpha <= 0)
			{
				remove();
			}
		}
		function ImpactExplosion(e:Event)
		{
			if(particle.currentFrame == particle.totalFrames)
			{
				
				remove();
			}
		}
		function AsteroidBits(e:Event)
		{
			if(currentFrame != 1)
			{
				particle.gotoAndStop(frame);
			}
			rotation += rotationSpeed;
			ySpeed += 0.1;
			y += ySpeed;
			x += xSpeed;
			if(y > 650)remove();
			else if(x > 550)remove();
			else if(x <-50)remove();
			else if(y<0)remove();
			
			alpha -= 0.06;
			if(alpha < 0)remove();
		}
		public function remove()
		{
			if(removed == false)
			{
				if(EventListener != null)
				{
					removeEventListener("enterFrame",EventListener);
				}
				parent.removeChild(this);
				removed = true;
			}
		}
		public function Pause()
		{
			if(removed == false)
			{
				if(EventListener != AsteroidBits)
				{
					particle.stop();
				}else{
					particle.gotoAndStop(frame);
				}
				removeEventListener(Event.ENTER_FRAME,EventListener)
			}
		}
		public function Resume()
		{
			if(EventListener != AsteroidBits)
			{
				particle.play();
			}
			addEventListener(Event.ENTER_FRAME,EventListener)
		}
	}
}