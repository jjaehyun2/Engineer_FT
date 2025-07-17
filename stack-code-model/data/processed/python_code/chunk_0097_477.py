package fplib.math 
{
	/**
	 * Vector2D class, with matematical and vectorial operations.
	 * Based on the C# version of the Vector2D class from http://www.pontov.com.br.
	 * Original by Vinícius G. Mendonça, ActionScript version by Diogo Muller.
	 * 
	 * @author Diogo Muller
	 */
	public class Vector2D 
	{
		//{ region Constants
		public static const ZERO : Vector2D = new Vector2D(0, 0);
		public static const ONE : Vector2D = new Vector2D(1, 1);
		//} region Constants
		
		//{ region Attrubutes	
		private var _x : Number;
		private var _y : Number;
		private var _changed : Boolean;
		//} endregion Attributes
		
		//{  region Properties 
		
		/**
		 * Vector X value.
		 */
		public function set X(value:Number) : void
		{
			_x = value;
			_changed = true;
		}
		public function get X() : Number
		{
			return _x;
		}
		
		/**
		 * Vector Y value.
		 */
		public function set Y(value:Number) : void
		{
			_y = value;
			_changed = true;
		}		
		public function get Y() : Number
		{
			return _y;
		}
		
		/**
		 * If the vector value has changed since the last update.
		 */
		public function get HasChanged() : Boolean
		{
			return _changed;
		}
		
		/**
		 * Vector size squared.
		 */
		public function get SizeSquared() : Number
		{
			return (X * X) + (Y * Y);
		}
		
		/**
		 * Vector size.
		 */
		public function get Size() : Number
		{
			return Math.sqrt(SizeSquared);
		}
		public function set Size(value : Number) : void
		{
			if ( value == 0)
			{
				set(0, 0);
			}
			else
			{
				var ratio : Number =  value / Size;
				
				X *= ratio;
				Y *= ratio;
			}
		}
		
		/**
		 * Gets the angle of the vector.
		 */
		public function get Angle() : Number
		{
			return Math.atan2(Y, X);
		}
		//} endregion Properties
		
		//{ region Constructors
		public function Vector2D(x : Number = 0, y : Number = 0)
		{
			set(x, y);
		}
		
		//} endregion Constructors
		
		//{ region Methods		
		/**
		 * Updates vector values, if needed.
		 */
		public function update() : void
		{
			_changed = false;
		}
		
		/**
		 * Creates a new Vector2D based on this one.
		 * @return New Vector2D with the same attributes as this one.
		 */
		public function clone() : Vector2D
		{
			return new Vector2D(X, Y);
		}
		
		/**
		 * Sets the vector to the desired values.
		 * @param	x X value.
		 * @param	y Y value.
		 * @return	This vector.
		 */
		public function set( x:Number, y:Number ) : Vector2D
		{
			X = x;
			Y = y;
			
			return this;
		}
		
		/**
		 * Makes this vector equal to other vector.
		 * @param	other Other vector.
		 * @return	This vector.
		 */
		public function setOther( other : Vector2D ) : Vector2D
		{
			return other == this ? this : set(other.X, other.Y);
		}
		
		/**
		 * Changes the size of this vector only if it's bigger than 
         * the size parameter. 
		 * @param	size The maximum size of this vector.
		 * @return The truncated vector.
		 */
		public function truncate( size : Number ) : Vector2D
		{
			if (SizeSquared > size * size) 
                Size = size;
				
            return this;
		}
		
		/**
		 * Rotates the vector counter-clockwise.
		 * @param	angle The angle to rotate, in radians.
		 * @return The vector itself, after the rotation.
		 */
		public function rotate( angle : Number ) : Vector2D
		{
			var s : Number = Math.sin(angle);
			var c : Number = Math.cos(angle);
			
			var newX : Number = (X * c) - (Y * s);
			var newY : Number = (X * s) + (Y * c);
			
			X = newX;
			Y = newY;
			
			return this;
		}
		
		/**
		 * Normalizes this vector.
		 * @return The vector itself, after the normalization.
		 */
		public function normalize() : Vector2D
		{
			var size : Number = Size;
			
			X /= size;
			Y /= size;
			
			return this;
		}
		
		/**
		 * Calculate the dot product of this vector and the given vector.
		 * Works only with normal vectors.
		 * @param	other Another vector.
		 * @return The dot product.
		 */
		public function dot( other : Vector2D ) : Number
		{
			return (X * other.X) + (Y * other.Y);
		}
		
		/** Returns the smallest angle between 2 vectors.
         *  The signal is used to indicate the angle rotation direction.
         *  Positive for counter-clockwise and negative for clockwise direction
         * 
         *  This method uses difference between two vectors.
		 * 
		 * @param	other The vector to calculate the angle with.
		 * @return The smallest angle between two vectors.
		 */
		public function angleBetween( other : Vector2D ) : Number
		{
			var angle : Number = other.Angle - Angle;
			
			if (Math.abs(angle) < Math.PI )
                return angle;

            return angle + (angle < 0 ? 2 * Math.PI : -2 * Math.PI);
		}
		
		/**
		 *  Return the smallest angle between 2 vectors.
         *  The signal is used to indicate the angle rotation direction.
         *  Positive for counter-clockwise and negative for clockwise direction
         *  
         *  This method uses the dot product.       
		 * @param	other The vector to calculate the angle with.
		 * @return	The smallest angle between two vectors.
		 */
		public function angleSign( other : Vector2D ) : Number
		{
			/* Must guarantee that other is a normalized vector */
            var v : Vector2D = other.clone().normalize();
            var dp : Number, angPi : Number;
			
            dp = dot(v); /* dot product */
            if (dp >= 1.0) dp = 1.0;
            if (dp <= -1.0) dp = -1.0;
            
			angPi = Math.acos(dp);
			
            /* Side test */
            if (Y * v.X > X * v.Y)
                return -angPi;
            else
                return angPi;
		}
		
		public function add( x : Number, y : Number ) : Vector2D
		{
			this.X += x;
			this.Y += y;
			
			return this;
		}
		
		/**
		 * Compares if this vector is equal to other vector.
		 * @param	other Other vector.
		 * @return	Is the other vector equal to this?
		 */
		public function equals( other : Vector2D ) : Boolean
		{
			return Vector2D.equals(this,other);
		}
		
		/**
		 * Converts the vector to a string.
		 * @param	radix Specifies the numeric base (from 2 to 36) to use for the number-to-string conversion. If you do not specify the radix parameter, the default value.
		 * @return 	String with the vector X and Y values.
		 */
		public function toString( radix:* = 10 ) : String
		{
			return "X: " + X.toString(radix) + " Y: " + Y.toString(radix); 
		}	
		//} endregion Methods
		
		//{ region Static Methods
		/**
		 * Compares two vectors.
		 * @param	v1 First vector to be compared.
		 * @param	v2 Second vector to be compared.
		 * @return	Are the two vectors equal?
		 */
		public static function equals( v1 : Vector2D, v2 : Vector2D ) : Boolean
		{
			return (v1.X == v2.X) && (v1.Y == v2.Y);
		}
		
		/**
		 * Adds two vectors.
		 * @param	v1 First vector to be added.
		 * @param	v2 Second vector to be added.
		 * @return	v1 + v2.
		 */
		public static function add( v1 : Vector2D, v2: Vector2D ) : Vector2D
		{
			return new Vector2D( v1.X + v2.X, v1.Y + v2.Y );
		}
		
		/**
		 * Subtracts two vectors.
		 * @param	v1 First vector to be subtracted.
		 * @param	v2 Second vector to be subtracted.
		 * @return	v1 - v2.
		 */
		public static function subtract( v1 : Vector2D, v2: Vector2D ) : Vector2D
		{
			return new Vector2D( v1.X - v2.X, v1.Y - v2.Y );
		}
		
		/**
		 * Multiplies a vector by a scalar.
		 * @param	vector Vector to be multiplied.
		 * @param	scalar Value the vector will be multiplied by.
		 * @return	Vector multiplied by scalar.
		 */
		public static function multiply( vector : Vector2D, scalar : Number ) : Vector2D
		{
			return new Vector2D(vector.X * scalar, vector.Y * scalar);
		}
		
		/**
		 * Divides a vector by a scalar.
		 * @param	vector Vector to be divided.
		 * @param	scalar Value the vector will be divided by.
		 * @return	Vector divided by scalar.
		 */
		public static function divide( vector : Vector2D, scalar : Number ) : Vector2D
		{
			return new Vector2D(vector.X / scalar, vector.Y / scalar);
		}
		
		/**
		 * Returns the vector * -1.
		 * @param	vector Vector to be multiplied.
		 * @return Vector * -1.
		 */
		public static function negative( vector : Vector2D ) : Vector2D
		{
			return new Vector2D( -vector.X, -vector.Y );
		}
		//} endregion Static Methods
	}
}