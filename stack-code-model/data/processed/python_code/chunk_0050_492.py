package
{
	import flash.geom.Point;
	
	import net.flashpunk.Entity;
	import net.flashpunk.FP;
	import net.flashpunk.graphics.Image;
	import net.flashpunk.utils.Input;
	import net.flashpunk.utils.Key;
	
	public class Player extends Entity
	{
		private var generator:MazeGenerator;
		
		private var direction:Point;
		
		private var canStart:Boolean;
		private var lavaTick:Number;
		private var startTick:Number;
		
		public function Player(generator:MazeGenerator)
		{
			this.generator = generator;
			
			type    = "player";
			layer   = 0;
			graphic = new Image(Assets.PLAYER);
			
			setHitbox(10, 10);
			
			var point:Point = generator.getStartPoint();
			x = point.x * generator.getTileWidth() + (generator.getTileWidth() - width) / 2;
			y = point.y * generator.getTileHeight() + (generator.getTileHeight() - height) / 2;
			
			direction = new Point(0, 0);
			
			canStart  = false;
			lavaTick  = 0;
			startTick = 0;
			
			Input.define("left", Key.A, Key.LEFT);
			Input.define("right", Key.D, Key.RIGHT);
			Input.define("up", Key.W, Key.UP);
			Input.define("down", Key.S, Key.DOWN);
		}
		
		override public function update():void
		{
			updateMovement();
			updateCollision();
			
			if (!canStart)
				return;
			
			startTick += FP.elapsed;
			if (startTick < 2.0)
				return;
			
			var tick:Number = .19 - Number(generator.getLevel()) / 100;
			
			lavaTick += FP.elapsed;
			if (lavaTick >= tick)
			{
				lavaTick -= tick;
				generator.propogateLavaStep();
			}
		}
		
		private function updateMovement():void
		{
			direction.x = direction.y = 0;
			
			if (Input.check("left")) direction.x -= 1;
			if (Input.check("right")) direction.x += 1;
			if (Input.check("up")) direction.y -= 1;
			if (Input.check("down")) direction.y += 1;
			
			direction.x *= 80 * FP.elapsed;
			direction.y *= 80 * FP.elapsed;
			
			if (!collide("start", x, y))
				canStart = true;
		}
		
		private function updateCollision():void
		{
			if (collide("lava", x, y))
				FP.world = new TitleWorld(generator, false);
			
			if (collide("exit", x, y))
			{
				generator.setLevel(generator.getLevel() + 1);
				FP.world = generator.getLevel() != 6 ? new MazeWorld(generator) : new TitleWorld(generator, false);
			}
			
			x += direction.x;
			
			var tileWidth:uint  = generator.getTileWidth();
			if (collide("maze", x, y) || x < 0 || x > (FP.screen.width - width))
			{
				if (FP.sign(direction.x) > 0)
				{
					direction.x = 0;
					x = Math.floor(x / tileWidth) * tileWidth + tileWidth - width;
				} else
				{
					direction.x = 0;
					x = Math.floor(x / tileWidth) * tileWidth + tileWidth;
				}
			}
			
			y += direction.y;
			
			var tileHeight:uint = generator.getTileHeight();
			if (collide("maze", x, y) || y < 0 || y > (FP.screen.height - height))
			{
				if (FP.sign(direction.y) > 0)
				{
					direction.y = 0;
					y = Math.floor(y / tileHeight) * tileHeight + tileHeight - height;
				} else
				{
					direction.y = 0;
					y = Math.floor(y / tileHeight) * tileHeight + tileHeight;
				}
			}
		}
	}
}