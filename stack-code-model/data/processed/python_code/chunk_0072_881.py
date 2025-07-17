package fplib.math 
{
	/**
	 * ...
	 * @author Diogo Muller
	 */
	public class Units 
	{
		//{ region Static Attributes
		/**
		 * Pixels per Meter
		 */
		private static var _ppm : Number = 1;
		/**
		 * Meters per pixel
		 */
		private static var _mpp : Number = 1;
		//} endregion Static Attributes
		
		//{ region Public Static Attributes
		public static var gravity : Vector2D = new Vector2D(0, 9.8);
		//} endregion Public Static Attributes
		
		//{ region Properties
		/**
		 * Meters per pixel
		 */
		public static function set MPP( value : Number ) : void
		{
			_mpp = value;
			_ppm = 1 / value;
		}
		public static function get MPP( ) : Number
		{
			return _mpp;
		}
		
		/**
		 * Pixels per meter.
		 */
		public static function set PPM( value : Number ) : void
		{
			_ppm = value;
			_mpp = 1 / value;
		}
		public static function get PPM( ) : Number
		{
			return _ppm;
		}
		//} endregion Properties
		
		
		//{ region Methods
		/**
		 * Converts a vector from meters to pixels.
		 * 
		 * @param	vector Vector using meters as unit.
		 * @return	Vector using pixels as unit.
		 */
		public static function MetersToPixels( vector : Vector2D ) : Vector2D
		{
			return Vector2D.divide( vector, _mpp );
		}
		//} endregion Methods
	}

}