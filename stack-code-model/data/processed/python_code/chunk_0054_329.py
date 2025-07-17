package fplib.math.steering 
{
	import fplib.math.PhysicsBehavior;
	import fplib.math.PhysicsEntity;
	import fplib.math.Vector2D;
	import net.flashpunk.FP;
	import fplib.math.Units;
	
	/**
	 * Seek steering behavior.
	 * @author Diogo Muller
	 */
	public class Seek extends Steering
	{	
		public function Seek()
		{
			super();
		}
		
		override public function calculate():Vector2D 
		{
			var desiredVelocity : Vector2D = Vector2D.subtract(_target.position, physicsParent.position);
			desiredVelocity.normalize();
			desiredVelocity = Vector2D.multiply(desiredVelocity, physicsParent.maximumSpeed);
			
			return desiredVelocity;
		}
		
	}

}