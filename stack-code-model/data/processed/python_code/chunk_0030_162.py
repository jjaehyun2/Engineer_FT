package me.rainssong.geom
{
	import flash.display.Graphics;
	
	/**
	 * ...
	 * @author Rainssong
	 */
	
	public class Vector2D
	{
		private var _x:Number;
		private var _y:Number;
		
		/**
		 * Constructor.
		 */
		public function Vector2D(x:Number = 0, y:Number = 0)
		{
			_x = x;
			_y = y;
		}
		
		/**
		 * Can be used to visualize the vector. Generally used for debug purposes
		   only.
		 * @param graphics The Graphics instance to draw the vector on.
		 * @param color The color of the line used to represent the vector.
		 */
		public function draw(graphics:Graphics, color:uint = 0):void
		{
			graphics.lineStyle(0, color);
			graphics.moveTo(0, 0);
			graphics.lineTo(_x, _y);
		}
		
		/**
		 * Generates a copy of this vector.
		 * @return Vector2D A copy of this vector.
		 */
		public function clone():Vector2D
		{
			return new Vector2D(x, y);
		}
		
		/**
		 * Sets this vector's x and y values, and thus length, to zero.
		 * @return Vector2D A reference to this vector.
		 */
		public function zero():Vector2D
		{
			_x = 0;
			_y = 0;
			return this;
		}
		
		/**
		 * Whether or not this vector is equal to zero, i.e. its x, y, and length
		   are zero.
		 * @return Boolean True if vector is zero, otherwise false.
		 */
		public function isZero():Boolean
		{
			return _x == 0 && _y == 0;
		}
		
		/**
		 * Sets / gets the length or magnitude of this vector. Changing the length
		   will change the x and y but not the angle of this vector.
		 */
		public function set length(value:Number):void
		{
			var a:Number = radians;
			_x = Math.cos(a) * value;
			_y = Math.sin(a) * value;
		}
		
		public function get length():Number
		{
			return Math.sqrt(lengthSQ);
		}
		
		/**
		 * Gets the length of this vector, squared.
		 */
		public function get lengthSQ():Number
		{
			return _x * _x + _y * _y;
		}
		
		/**
		 * Gets / sets the angle of this vector. Changing the angle changes the x
		   and y but retains the same length.
		 */
		public function set radians(value:Number):void
		{
			var len:Number = length;
			_x = Math.cos(value) * len;
			_y = Math.sin(value) * len;
		}
		
		public function get radians():Number
		{
			return Math.atan2(_y, _x);
		}
		
		public function set degree(value:Number):void
		{
			radians = value / 180 * Math.PI;
		}
		
		public function get degree():Number
		{
			return radians/Math.PI*180;
		}
		
		
		
		/**
		 * Normalizes this vector. Equivalent to setting the length to one, but
		   more efficient.
		 * @return Vector2D A reference to this vector.
		 */
		public function normalize():Vector2D
		{
			if (length == 0)
			{
				_x = 1;
				return this;
			}
			var len:Number = length;
			_x /= len;
			_y /= len;
			return this;
		}
		
		/**
		 * Ensures the length of the vector is no longer than the given value.
		 * @param max The maximum value this vector should be. If length is larger
		   than max, it will be truncated to this value.
		 * @return Vector2D A reference to this vector.
		 */
		public function truncate(max:Number):Vector2D
		{
			length = Math.min(max, length);
			return this;
		}
		
		/**
		 * Reverses the direction of this vector.
		 * @return Vector2D A reference to this vector.
		 */
		public function reverse():Vector2D
		{
			_x = -_x;
			_y = -_y;
			return this;
		}
		
		/**
		 * Whether or not this vector is normalized, i.e. its length is equal to
		   one.
		 * @return Boolean True if length is one, otherwise false.
		 */
		public function isNormalized():Boolean
		{
			return length == 1.0;
		}
		
		/**
		 * Calculates the dot product of this vector and another given vector.
		 * @param v2 Another Vector2D instance.
		 * @return Number The dot product of this vector and the one passed in as a
		   parameter.
		 */
		public function dotProd(v2:Vector2D):Number
		{
			return _x * v2.x + _y * v2.y;
		}
		
		/**
		 * Calculates the cross product of this vector and another given vector.
		 * @param v2 Another Vector2D instance.
		 * @return Number The cross product of this vector and the one passed in as
		   a parameter.
		 */
		public function crossProd(v2:Vector2D):Number
		{
			return _x * v2.y - _y * v2.x;
		}
		
		/**
		 * Calculates the angle between two vectors.
		 * @param v1 The first Vector2D instance.
		 * @param v2 The second Vector2D instance.
		 * @return Number the angle between the two given vectors.
		 */
		public static function angleBetween(v1:Vector2D, v2:Vector2D):Number
		{
			if (!v1.isNormalized())
				v1 = v1.clone().normalize();
			
			if (!v2.isNormalized())
				v2 = v2.clone().normalize();
			return Math.acos(v1.dotProd(v2));
		}
		
		/**
		 * Determines if a given vector is to the right or left of this vector.
		 * @return int If to the left, returns -1. If to the right, +1.
		 */
		public function sign(v2:Vector2D):int
		{
			return perp.dotProd(v2) < 0 ? -1 : 1;
		}
		
		/**
		 * Finds a vector that is perpendicular to this vector.
		 * @return Vector2D A vector that is perpendicular to this vector.
		 */
		public function get perp():Vector2D
		{
			return new Vector2D(-y, x);
		}
		
		/**
		 * Calculates the distance from this vector to another given vector.
		 * @param v2 A Vector2D instance.
		 * @return Number The distance from this vector to the vector passed as a
		   parameter.
		 */
		public function dist(v2:Vector2D):Number
		{
			return Math.sqrt(distSQ(v2));
		}
		
		/**
		 * Calculates the distance squared from this vector to another given vector.
		 * @param v2 A Vector2D instance.
		 * @return Number The distance squared from this vector to the vector
		   passed as a parameter.
		 */
		public function distSQ(v2:Vector2D):Number
		{
			var dx:Number = v2.x - x;
			var dy:Number = v2.y - y;
			return dx * dx + dy * dy;
		}
		
		/**
		   9
		 * Adds a vector to this vector, creating a new Vector2D instance to hold
		   the result.
		 * @param v2 A Vector2D instance.
		 * @return Vector2D A new vector containing the results of the addition.
		 */
		public function add(v2:Vector2D):Vector2D
		{
			return new Vector2D(_x + v2.x, _y + v2.y);
		}
		
		/**
		 * Subtacts a vector to this vector, creating a new Vector2D instance to
		   hold the result.
		 * @param v2 A Vector2D instance.
		 * @return Vector2D A new vector containing the results of the subtraction.
		 */
		public function subtract(v2:Vector2D):Vector2D
		{
			return new Vector2D(_x - v2.x, _y - v2.y);
		}
		
		/**
		 * Multiplies this vector by a value, creating a new Vector2D instance to
		   hold the result.
		 * @param v2 A Vector2D instance.
		 * @return Vector2D A new vector containing the results of the
		   multiplication.
		 */
		public function multiply(value:Number):Vector2D
		{
			return new Vector2D(_x * value, _y * value);
		}
		
		/**
		 * Divides this vector by a value, creating a new Vector2D instance to hold
		   the result.
		 * @param v2 A Vector2D instance.
		 * @return Vector2D A new vector containing the results of the division.
		 */
		public function divide(value:Number):Vector2D
		{
			return new Vector2D(_x / value, _y / value);
		}
		
		/**
		 * Indicates whether this vector and another Vector2D instance are equal in
		   value.
		   10
		 * @param v2 A Vector2D instance.
		 * @return Boolean True if the other vector is equal to this one, false if
		   not.
		 */
		public function equals(v2:Vector2D):Boolean
		{
			return _x == v2.x && _y == v2.y;
		}
		
		/**
		 * Sets / gets the x value of this vector.
		 */
		public function set x(value:Number):void
		{
			_x = value;
		}
		
		public function get x():Number
		{
			return _x;
		}
		
		/**
		 * Sets / gets the y value of this vector.
		 */
		public function set y(value:Number):void
		{
			_y = value;
		}
		
		public function get y():Number
		{
			return _y;
		}
		
		/**
		 * Generates a string representation of this vector.
		 * @return String A description of this vector.
		 */
		public function toString():String
		{
			return "[Vector2D (x:" + _x + ", y:" + _y + ")]";
		}
	}
}