package fplib.math 
{
	import flash.utils.Dictionary;
	import fplib.base.GameEntity;
	import net.flashpunk.FP;
	
	/**
	 * ...
	 * @author Diogo Muller
	 */
	public class PhysicsEntity extends GameEntity
	{
		//{ region Attributes
		/**
		 * Body momentum.
		 */
		public var momentum : Vector2D;
		/**
		 * Constant forces on the body.
		 */
		public var constantForces : Dictionary;
		/**
		 * Instant forces on the body.
		 */
		public var forces : Vector.<Vector2D>;
		/**
		 * Body mass.
		 */
		public var mass : Number;
		/**
		 * Do physics affect body rotation?
		 */
		public var rotate : Boolean;
		/**
		 * Air and ground friction on the body.
		 */
		public var friction : Number;
		
		/**
		 * Entity maximum speed.
		 */
		public var maximumSpeed : Number;
		
		/**
		 * Is entity on ground?
		 */
		private var _onGround : Boolean;
		//} endregion Attributes
		
		//{ region Properties
		/**
		 * Is entity on ground?
		 */
		public function get onGround() : Boolean
		{
			return _onGround;
		}
		//} endregion Properties
		
		
		//{ region Constructor
		public function PhysicsEntity( x : Number, y : Number ) 
		{
			super(x, y);
			
			forces = new Vector.<Vector2D>();
			constantForces = new Dictionary();
			
			momentum = Vector2D.ZERO;
			
			friction = 1;
			mass = 1;
		}
		//} endregion Constructor
		
		//{ region Methods
		/**
		 * Updates, considering physics.
		 */
		override public function update():void 
		{
			_onGround = collideTypes("solid", position.X, position.Y + 1) && !collideTypes("solid", position.X, position.Y);
			
			// TODO: Consider Negative and X Gravity.
			if ( onGround ) momentum.Y = 0;
			
			var forces : Vector2D = Vector2D.ZERO;
			var instantForces : Vector2D = Vector2D.ZERO;
			var secs : Number = FP.elapsed;
			
			//{ region Calculate Forces
			var force : Vector2D;
			
			for each( force in constantForces )
			{
				forces = Vector2D.add(forces, force);
			}
			
			while ( this.forces.length != 0 )
			{
				force = this.forces.pop();
				instantForces = Vector2D.add(instantForces, Vector2D.divide( force, mass ));
			}
			//} endregion Calculate Forces
			
			var acceleration : Vector2D = Vector2D.add( Vector2D.divide( forces, mass ), Units.gravity );
			var accelSecs : Vector2D = Vector2D.multiply( acceleration, secs );
			
			momentum = Vector2D.add( momentum, Vector2D.add( accelSecs, instantForces ) );
			momentum = Vector2D.multiply( momentum, friction );
			position = Vector2D.add( position, Units.MetersToPixels(Vector2D.multiply( Vector2D.add( momentum, Vector2D.divide( accelSecs, 2 ) ), secs )));
			
			if ( rotate )
			{
				// TODO: Rotation.
			}
			
			super.update();
		}
		//} endregion Methods
	}

}