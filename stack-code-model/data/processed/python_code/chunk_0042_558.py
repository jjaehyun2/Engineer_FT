package  
{
	import flash.display.Sprite;
	import flash.events.Event;
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class FullCluster extends Cluster implements IEnemy
	{
		public var numHits:int = 0;
		public const MAX_HITS:int = 4;
		
		
		public var xSpeed:Number = 0;
		public var ySpeed:Number = 0;
		public var speed:Number = 15;
		
		public var moveDelay:Number = 0;
		public var moveDelayMax:Number = 35;
		
		public var allowedMoves:int = 60;
		
		
		public function FullCluster() 
		{
			addEventListener(Event.ADDED_TO_STAGE, init)
		}
		public function init(e:Event):void
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);
			
			var angleToPlayer:Number = Math.atan2(PlayState.player.y - y, PlayState.player.x -x);
			var r:Number = angleToPlayer;
			xSpeed = speed * Math.cos(r);
			ySpeed = speed * Math.sin(r);
			
		}
		
		public function frame():Boolean
		{
			moveDelay++;
			if (moveDelay > moveDelayMax)
			{
				moveDelay = 0;
				x += xSpeed;
				y += ySpeed;
				if (x < -width / 2) x = stage.stageWidth + width / 2;
				if (x > stage.stageWidth + width / 2) x = -width / 2;
				if (y < -height / 2) y = stage.stageHeight + height / 2;
				if (y > stage.stageHeight + height / 2) y = -height / 2;
				
				allowedMoves--;
				if (allowedMoves <= 0)
				{
					return true;
				}
			}
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
			var angleToPlayer:Number = Math.atan2(PlayState.player.y - y, PlayState.player.x -x);
			
			var i:int;
			for (i = 0; i < 4; i++)
			{
				var c:PartCluster = new PartCluster(angleToPlayer);
				c.x = x;
				c.y = y;
				parent.addChild(c);
				PlayState.ActiveEnemies.push(c);
			}
			
			for (i = 0; i < 10; i++)
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