package  
{
	import flash.display.Sprite;
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class BigBit extends Hexagon implements IEnemy
	{
		public var rotationAmount:int = 1;
		public var numHits:int = 0;
		public const MAX_HITS:int = 4;
		
		public var xSpeed:Number = 0;
		public var ySpeed:Number = 0;
		public var speed:Number = 2;
		public function BigBit() 
		{
			var r:Number = Math.random() * Math.PI*2;
			xSpeed = speed * Math.cos(r);
			ySpeed = speed * Math.sin(r);
		}
		
		public function frame():Boolean
		{
			rotation += rotationAmount;
			x += xSpeed;
			y += ySpeed;
			
			if (x < -width / 2) x = stage.stageWidth + width / 2;
			if (x > stage.stageWidth + width / 2) x = -width / 2;
			if (y < -height / 2) y = stage.stageHeight + height / 2;
			if (y > stage.stageHeight + height / 2) y = -height / 2;
			
			return false;
		}
		
		public function hitTest(s:Sprite):Boolean
		{
			return hitTestPoint(s.x, s.y, true);
		}
		
		public function takeDamage(num:int):Boolean
		{
			numHits++;
			
			if (numHits > MAX_HITS)
			{
				return true;
			}
			return false;
		}
		
		public function die():void
		{
			for (var i:int = 0; i < 10; i++)
			{
				var p:Pickup = new Pickup();
				p.x = x;
				p.y = y;
				parent.addChild(p);
			}
			parent.removeChild(this);
		}
	}

}