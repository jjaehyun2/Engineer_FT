package fplib.base 
{
	/**
	 * ...
	 * @author Diogo Muller
	 */
	public class Behavior 
	{
		//{ region Attributes
		/**
		 * Behavior parent.
		 */
		private var _parent : GameEntity;
		//} region Attributes
		
		//{ region Properties
		/**
		 * Obtains the behavior parent.
		 */
		public function set parent( value : GameEntity ) : void
		{
			_parent = value;
		}
		public function get parent( ) : GameEntity
		{
			return _parent;
		}
		//} endregion Properties
		
		//{ region Constructor
		public function Behavior() {}
		//} endregion Constructor
		
		//{ region Methods
		/**
		 * Method to be called each frame by parent. 
		 */
		public function update() : void { }	
		
		/**
		 * Method to be called on rendering by parent. 
		 */
		public function render() : void { }	
		//} endregion Methods
	}

}