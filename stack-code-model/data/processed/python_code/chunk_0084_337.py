package com.profusiongames.util
{
	import flash.geom.Point;

	public class Vector2D {

		public var x:Number = 0;
		public var y:Number = 0;

		public function Vector2D(dx:Number = 0, dy:Number = 0){
			x = dx;
			y = dy;
		}

		public function initFromPoint( p:Point ):Vector2D
		{
			x = p.x;
			y = p.y;
			return this;
		}

		public function reset():Vector2D {
			x = 0;
			y = 0;
			return this;
		}
		//
		public function add(ov:Vector2D):Vector2D {
			x += ov.x;
			y += ov.y;
			return this;
		}
		//
		public function subtract(ov:Vector2D):Vector2D {
			x -= ov.x;
			y -= ov.y;
			return this;
		}

		public function multiply(ov:Vector2D):Vector2D {
			x *= ov.x;
			y *= ov.y;
			return this;
		}

		//apply scalars		
		public function multiplyLength(o:Number):Vector2D {
			x *= o;
			y *= o;
			return this;
		}

		public function divideLength(o:Number):Vector2D {
			x /= o;
			y /= o;
			return this;
		}

		//give() gives the x,y values of this instance to another
		public function give(ov:Vector2D):Vector2D {
			ov.x = x;
			ov.y = y;
			return this;
		}

		//copy() copies the x,y values of another instance to this
		public function copy(ov:Vector2D):Vector2D {
			x = ov.x;
			y = ov.y;
			return this;
		}

		public function set angle(n:Number):void {
			var l:Number = length;
			x = Math.cos(n)*l;
			y = Math.sin(n)*l;
		}

		public function set angleDeg(n:Number):void {
			n *= 0.0174532925;
			var l:Number = length;
			x = Math.cos(n)*l;
			y = Math.sin(n)*l;
		}

		public function setAngle(n:Number):Vector2D {
			var l:Number = length;
			x = Math.cos(n)*l;
			y = Math.sin(n) * l;
			return this;
		}

		public function setAngleDeg(n:Number):Vector2D {
			n *= 0.0174532925;
			var l:Number = length;
			x = Math.cos(n)*l;
			y = Math.sin(n) * l;
			return this;
		}

		public function rotateBy(n:Number):Vector2D {
			var angle:Number = getAngle();
			var length:Number = Math.sqrt(x*x+y*y);
			x = Math.cos(n+angle)*length;
			y = Math.sin(n + angle) * length;
			return this;
		}

		public function rotateByDeg(n:Number):Vector2D {
			n *= 0.0174532925;
			rotateBy(n);
			return this;
		}

		public function normalise( n:Number = 1.0 ):Vector2D {
			normalize(n);
			return this;
		}
 
		public function normalize( n:Number = 1.0 ):Vector2D {
			var length:Number = Math.sqrt(x*x+y*y);
			x = (x/length) * n;
			y = (y / length) * n;
			return this;
		}

		public function get length():Number {
			return (Math.sqrt(x*x+y*y));
		}

		public function getLength():Number {
			return ( Math.sqrt(x*x+y*y) );
		}

		public function set length( newlength:Number ):void {
			normalize(1);
			x *= newlength;
			y *= newlength;
		}

		public function setLength(newlength:Number):Vector2D {
			normalize(1);
			x *= newlength;
			y *= newlength;
			return this;
		}
		//
		public function getAngle():Number {
			return (Math.atan2(y,x));
		}

		public function getAngleDeg():Number {
			return (Math.atan2(y,x) * 57.2957 );
		}
		//
		public function dot(ov:Vector2D):Number {
			return (x*ov.x+y*ov.y);
		}

		public function clone():Vector2D
		{
			return new Vector2D(x, y)
		}

		public function zero():Vector2D
		{
			x = 0;
			y = 0;
			return this;
		}

		public function lookAt( ov:Vector2D ):Vector2D
		{
			var vectorToTarget:Vector2D = new Vector2D( ov.x - x, ov.y - y  );
			setAngle( vectorToTarget.getAngle() );
			return this;
		}

		//operations returning new Vectors

		public function minus(ov:Vector2D):Vector2D {
			return new Vector2D( x -= ov.x, y -= ov.y );
		}

		//public function times(ov:*):void {
			//return new Vector2D( x * ov.x, y * ov.y );
		//}

		public function times(scalar:Number):Vector2D {
			return new Vector2D( x * scalar, y * scalar );
		}

		public function plus(ov:Vector2D):Vector2D {
			return new Vector2D( x -= ov.x, y -= ov.y );
		}
		
		
		public function equals(v:Vector2D):Boolean
		{
			return x == v.x && y == v.y;
		}
		public static function interpolate(v:Vector2D, v2:Vector2D, f:Number):Vector2D
		{
			return new Vector2D(f * v.x + (1 - f) * v2.x, f * v.y + (1 - f) * v2.y);
		}
		
		public function toString():String
		{
			return "Vector2D{ " + x + ", " + y + " }";
		}

	} // end class

}