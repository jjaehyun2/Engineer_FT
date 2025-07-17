package zombie.behaviors 
{
	import fplib.base.Behavior;
	import fplib.math.Vector2D;
	import net.flashpunk.graphics.Image;
	import net.flashpunk.graphics.Spritemap;
	import net.flashpunk.utils.Input;
	import net.flashpunk.utils.Key;
	import net.flashpunk.FP;
	/**
	 * ...
	 * @author Diogo Muller
	 */
	public class ControlableBehavior extends Behavior
	{
		
		public function ControlableBehavior() 
		{
			Input.define("Front", Key.RIGHT, Key.D);
			Input.define("Back", Key.LEFT, Key.A);
			Input.define("Down", Key.DOWN, Key.S);
			Input.define("Up", Key.UP, Key.W);
		}
		
		override public function update():void 
		{
			var moving:Boolean = false;
			
			if (Input.check("Back")) 
			{ 
                (parent.graphic as Spritemap).flipped = true;
				parent.position.X -= (50 * FP.elapsed); 
				moving = true; 			
			}
			if (Input.check("Front")) 
			{ 
                (parent.graphic as Spritemap).flipped = false;
				parent.position.X += (50 * FP.elapsed); 
				moving = true; 	
			}
			if (Input.check("Up")) 
			{ 
				parent.position.Y -= (50 * FP.elapsed); 
				moving = true; 	
			}
			if (Input.check("Down")) 
			{ 
				parent.position.Y += (50 * FP.elapsed); 
				moving = true; 	
			}
			
			
			if ( moving )
			{
				(parent.graphic as Spritemap).play("run");
			}
			else
			{
				(parent.graphic as Spritemap).play("stand");
			}
		}
	}

}