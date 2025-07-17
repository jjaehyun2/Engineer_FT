package
{
	import flash.display.MovieClip;
	import flash.events.Event;
	public class Shell extends MovieClip
	{
		var angle:Number;
		var rSpeed:Number;
		var time:int;
		var speed:Number;
		var xSpeed:Number;
		var ySpeed:Number;
		function Shell(_x,_y,Angle)
		{
			rotation = Math.abs(Angle);
			speed = Math.random()*2+1;
			
			angle = Angle+Math.random()*10-5;
			rSpeed = Math.random()*10-5;
			addEventListener(Event.ENTER_FRAME,enterFrame);
			xSpeed = Math.sin(angle*Math.PI/180)*speed;
			ySpeed = Math.cos(angle*Math.PI/180)*speed;
			x = _x+Math.sin((Angle-40)*Math.PI/180)*15;
			y = _y+Math.cos((Angle-40)*Math.PI/180)*15;
		}
		function enterFrame(e:Event)
		{
			time ++;
			if(time < 20)
			{
				x += xSpeed;
				y += ySpeed;
			}else{
				Game.NewImpactParticle(x,y,"ShellMc",rotation,null,null);
				remove()
			}
			rotation += rSpeed;

		}
		public function Pause()
		{
			removeEventListener(Event.ENTER_FRAME,enterFrame)
		}
		public function Resume()
		{
			addEventListener(Event.ENTER_FRAME,enterFrame)
		}
		function remove()
		{
			removeEventListener(Event.ENTER_FRAME,enterFrame);
			parent.removeChild(this);
		}
	}
}