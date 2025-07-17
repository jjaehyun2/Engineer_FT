package {
	
	/**
	 * Defines a 3D environment
	 */
	public class Environment3D {
		
		/**
		 * center x location
		 */
		public var originX:Number;
			
		/**
		 * center y location
		 */
		public var originY:Number;
			
		/**
		 * focalLength of camera
		 */
		public var focalLength:Number;
			
		/**
		 * constructor
		 */
		public function Environment3D(x:Number = 0, y:Number = 0, focalLength:Number = 250){
			this.originX = x;
			this.originY = y;
			this.focalLength = focalLength;
		}
	}
}