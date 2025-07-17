package fplib.math 
{
	import fplib.base.Behavior;
	/**
	 * ...
	 * @author Diogo Muller
	 */
	public class PhysicsBehavior extends Behavior
	{
		/**
		 * Will cast the parent to a PhysicsEntity.
		 */
		public function get physicsParent() : PhysicsEntity 
		{
			return parent as PhysicsEntity;
		}
		
		public function PhysicsBehavior() { }
		
	}

}