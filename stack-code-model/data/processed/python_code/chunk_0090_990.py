package
{
	import flash.display.Graphics;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;


	public class MovingObject extends Sprite
	{
		private var origin :Object;
		protected var sizeWidth :int;
        protected var sizeHeight :int;
		private var radius :int;
		private var speed :Number;
		
		private var angle :int;
		private var reverse :Boolean;
		
	
		public function MovingObject(origin:Object, sizeWidth :int, sizeHeight :int, radius :int, speed :Number, reverse :Boolean,angle:int)
		{
			super();
			this.origin = origin;
			this.angle  = angle;
			this.sizeWidth = sizeWidth;
            this.sizeHeight = sizeHeight;
			this.radius = radius;
			this.speed = speed;
			this.reverse = reverse;
		}

		protected function moveStatic(e :Event) :void
		{
			var rad :Number = this.angle * (Math.PI / 180);
			this.x = this.origin.x + this.radius * Math.cos(rad);
			this.y = this.origin.y + this.radius * Math.sin(rad);
			
			if (this.reverse == false)
			{
				this.angle += this.speed ;
			}
			else
			{
				this.angle -= this.speed;
			}
						
			this.angle %= 360;
		}

        protected function moveDynamic(e :Event) :void
		{
			var rad :Number = this.angle * (Math.PI / 180);
			this.x = this.radius * Math.cos(rad);
			this.y = this.radius * Math.sin(rad);
			
			if (this.reverse == false)
			{
				this.angle += this.speed ;
			}
			else
			{
				this.angle -= this.speed;
			}
						
			this.angle %= 360;
		}
	}
}