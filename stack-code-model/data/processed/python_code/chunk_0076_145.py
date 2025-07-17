package
{
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;
	public class Cannon extends MovieClip
	{
		private var time:int;
		public var interval:int;
		public var type:String;
		var Online;
		var Target:Object;
		function Cannon(_x,_y,Type)
		{
			range.visible = false;
			this.buttonMode = true;
			Online = true;
			x = Math.round(_x);
			y = Math.round(_y);
			type = Type;
			if(type == "Cannon")
			{
				cannon.gotoAndPlay(6);
				interval = 20;
			}
			if(type == "Laser")
			{
				cannon.gotoAndPlay(5);
				interval = 60;
			}
			if(type == "SpreadCannon")
			{
				interval = 40;
			}
			time = interval;
			gotoAndStop(type);
			addEventListener(Event.ENTER_FRAME,enterFrame);
			addEventListener(MouseEvent.MOUSE_DOWN, onClick);
			addEventListener(MouseEvent.ROLL_OVER, rollOver);
			addEventListener(MouseEvent.ROLL_OUT, rollOut);
		}
		function onClick(e:MouseEvent)
		{
			range.visible = false;
			FakeCannon.DragOn(this,type);
		}
		function rollOver(e:MouseEvent)
		{
			range.visible = true;
		}
		function rollOut(e:MouseEvent)
		{
			range.visible = false;
		}
		public function enterFrame(e:Event)
		{
			if(type == "Cannon")
			{
				if(cannon.currentFrame == 20)
				{
					cannon.stop();
				}
			}
			if(type == "SpreadCannon")
			{
				if(cannon.currentFrame == 40)
				{
					cannon.stop();
				}
			}
			time++;
			if(time > interval)
			{
				ShootBullet();
				
				time = 0;
			}
		}
		public function ShootBullet()
		{
			cannon.gotoAndPlay(1);
			if(type == "Cannon")
			{
				Sounds.NewSound("weapon1SFX");
			}
			if(type == "Laser")
			{
				Sounds.NewSound("weapon2SFX");
			}
			if(type != "SpreadCannon")
			{
				
				Game.NewBullet(x,y-10,type,0);
			}else{
				Sounds.NewSound("spreadCannonShotSFX");
				Game.NewBullet(x,y-30,type,0);
			}
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
			removeEventListener(MouseEvent.MOUSE_DOWN, onClick);
			removeEventListener(MouseEvent.ROLL_OVER, rollOver);
			removeEventListener(MouseEvent.ROLL_OUT, rollOut);
			parent.removeChild(this);
		}
		function GoOffline()
		{
			cannon.stop();
			Online = false;
			alpha = 0.50;
			removeEventListener(Event.ENTER_FRAME, enterFrame);
			removeEventListener(MouseEvent.ROLL_OVER, rollOver);
			removeEventListener(MouseEvent.ROLL_OUT, rollOut);
		}
		function GoOnline()
		{
			cannon.play();
			Online = true;
			alpha = 1;
			addEventListener(Event.ENTER_FRAME, enterFrame);
			addEventListener(MouseEvent.ROLL_OVER, rollOver);
			addEventListener(MouseEvent.ROLL_OUT, rollOut);
		}
		public function Pause()
		{
			cannon.stop();
			removeEventListener(MouseEvent.MOUSE_DOWN, onClick);
			removeEventListener(Event.ENTER_FRAME,enterFrame)
			removeEventListener(MouseEvent.ROLL_OVER, rollOver);
			removeEventListener(MouseEvent.ROLL_OUT, rollOut);
		}
		public function Resume()
		{
			cannon.play()
			addEventListener(MouseEvent.MOUSE_DOWN, onClick);
			addEventListener(Event.ENTER_FRAME,enterFrame)
			addEventListener(MouseEvent.ROLL_OVER, rollOver);
			addEventListener(MouseEvent.ROLL_OUT, rollOut);
		}
	}
}