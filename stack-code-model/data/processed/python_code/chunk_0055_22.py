/**
 * <br>Extended math helper functions focused on 2D Cartesian geometrical operations
 * <br>For reference, three methods of measuring angles are used:
 * <br>Radians: from 0 along the positive x-axis counter-clockwise
 * <br>Degrees: from 0 along the positive x-axis counter-clockwise
 * <br>Flash-Degrees: from 0 along the positive x-axis.  Up to +180 counter-clockwise, -180 clockwise
 * <br>NOTE: Unless otherwise specified, assume all angles are in radians!
 * @author Chris Sinclair - Genexis Systems Inc.
 * @version 0.4.0
 */
package com {
	import flash.geom.Point;
	import flash.geom.Rectangle;
	
	public class Math2D {
		public static const RATIO_CIRCLE_AREA_FOR_SQUARE:Number = Math.PI/4;
		
		/**
		 * Get a random point within a rectangluar area.
		 * @param aRect the rectangle
		 * @return the perimeter of the square or rectangle
		 */
		public static function getRandomPoint(rectangle:Rectangle):Point {
			var randomX:Number = MathUtils.randRange(Math.min(rectangle.left,rectangle.right),Math.max(rectangle.left,rectangle.right));
			var randomY:Number = MathUtils.randRange(Math.min(rectangle.top,rectangle.bottom),Math.max(rectangle.top,rectangle.bottom));
			return new Point(randomX, randomY);
			
		}
		
		/**
		 * Finds the permieter of a rectangle or square.
		 * @param aRect the rectangle
		 * @return the perimeter of the square or rectangle
		 */
		public static function PerimeterOfRect(aRect:Rectangle):Number {
			return (2 * aRect.width) + (2 * aRect.height);
		}
		
		/**
		 * Finds the circumference of a circle.
		 * @param radius of the circle
		 * @return the circumference of a circle
		 */
		public static function CircumferenceOfCircleForRadius(radius:Number):Number {
			return Math2D.CircumferenceOfCircleForDiameter(2 * radius);
		}
		
		/**
		 * Finds the diameter of a circle.
		 * @param circumference of the circle
		 * @return the diameter of a circle
		 */
		public static function DiameterOfCircleForCircumference(circumference:Number):Number {
			return (circumference/Math.PI);
		}
		
		/**
		 * Finds the radius of a circle.
		 * @param circumference of the circle
		 * @return the radius of a circle
		 */
		public static function RadiusOfCircleForCircumference(circumference:Number):Number {
			return Math2D.DiameterOfCircleForCircumference(circumference)/2;
		}
		
		/**
		 * Finds the circumference of a circle.
		 * @param diameter of the circle
		 * @return the circumference of a circle
		 */
		public static function CircumferenceOfCircleForDiameter(diameter:Number):Number {
			return (Math.PI * diameter);
		}
		
		/**
		 * Finds the area of a circle.
		 * @param radius of circle
		 * @return the area of a circle
		 */
		public static function AreaOfCircleForRadius(radius:Number):Number {
			return (Math.PI*Math.pow(radius,2));
		}
		
		/**
		 * Finds the area of a rectangle or square.
		 * @param aRect the rectangle
		 * @return the area of the square or rectangle
		 */
		public static function AreaOfRect(aRect:Rectangle):Number {
			return Math2D._AreaOfRect(aRect.width,aRect.height);
		}
		
		/**
		 * Finds the area of a rectangle or square, described by width and height.
		 * @param width of the rectangle
		 * @param height of the rectangle
		 * @return the area of the square or rectangle
		 */
		public static function _AreaOfRect(width:Number,height:Number):Number {
			return (width * height);
		}
		
		/**
		 * Finds the diagonal of a rectangle or square.
		 * @param aRect the rectangle
		 * @return the diagonal of the square or rectangle
		 */
		public static function DiagonalOfRect(aRect:Rectangle):Number {
			return Math.sqrt(Math.pow(aRect.width,2) + Math.pow(aRect.height,2));
		}
		
		/**
		 * Finds the area of a circle from area of rectangle.
		 * @param area of rectangle
		 * @return the area of a circle
		 */
		public static function AreaOfCircleForAreaOfRect(area_of_rect:Number):Number {
			return (area_of_rect*Math2D.RATIO_CIRCLE_AREA_FOR_SQUARE);
		}
		
		/**
		 * Finds the radius of a circle that fits inside a square or rectangle.
		 * @param length of rectangle
		 * @param width of rectangle
		 * @return the radius of a circle
		 */
		public static function RadiusOfCircleForRectangle(width:Number,height:Number):Number {
			var area_of_rect:Number = Math2D._AreaOfRect(width,height);
			var area_of_circle:Number = Math2D.AreaOfCircleForAreaOfRect(area_of_rect);
			var radius_of_circle:Number = Math.sqrt(area_of_circle/Math.PI);
			return radius_of_circle;
		}
		
		/**
		 * Converts the passed radian angle into degrees
		 * @param Radians the radian angle to convert
		 * @return an angle in degrees
		 * @see Deg2Rad
		 * @see Deg2FDeg
		 * @see Rad2FDeg
		 * @see FDeg2Deg
		 * @see FDeg2Rad
		 */
		public static function Rad2Deg(Radians:Number):Number {
			return ((Radians / Math.PI) * 180);
		}
		
		/**
		 * Converts the passed degree angle into radians
		 * @param Degrees the degree angle to convert
		 * @return an angle in radians
		 * @see Rad2Deg
		 * @see Deg2FDeg
		 * @see Rad2FDeg
		 * @see FDeg2Deg
		 * @see FDeg2Rad
		 */
		public static function Deg2Rad(Degrees:Number):Number {
			return (Degrees / 180) * Math.PI;
		}
		
		/**
		 * Converts the passed degree into Flash degrees
		 * @param Degrees the degree angle to convert
		 * @return an angle in flash degrees
		 * @see Rad2Deg
		 * @see Deg2Rad
		 * @see Rad2FDeg
		 * @see FDeg2Deg
		 * @see FDeg2Rad
		 */
		public static function Deg2FDeg(Degrees:Number):Number {
			if (Degrees > 180){
				Degrees = Degrees - 360;
			}
			return Degrees;
		}
		
		/**
		 * Converts the passed radian into flash-degrees
		 * @param Radians the radian angle to convert
		 * @return an angle in flash degrees
		 * @see Rad2Deg
		 * @see Deg2Rad
		 * @see Deg2FDeg
		 * @see FDeg2Deg
		 * @see FDeg2Rad
		 */
		public static function Rad2FDeg(Radians:Number):Number {
			var deg:Number = Rad2Deg(Radians);
			return Deg2FDeg(deg);
		}
		
		/**
		 * Converts the passed flash-degree into degrees
		 * @param FlashDegree the FlashDegree angle to convert
		 * @return an angle in degrees
		 * @see Rad2Deg
		 * @see Deg2Rad
		 * @see Deg2FDeg
		 * @see Rad2FDeg
		 * @see FDeg2Rad
		 */
		public static function FDeg2Deg(FlashDegree:Number):Number {
			if (FlashDegree < 0) {
				FlashDegree = 360 + FlashDegree;
			} else {
				//FlashDegree = 360 - FlashDegree;
			}
			return FlashDegree;
		}
		
		/**
		 * Converts the passed flash-degree into radians
		 * @param FlashDegree the FlashDegree angle to convert
		 * @return an angle in radians
		 * @see Rad2Deg
		 * @see Deg2Rad
		 * @see Deg2FDeg
		 * @see Rad2FDeg
		 * @see FDeg2Deg
		 */
		public static function FDeg2Rad(FlashDegree:Number):Number {
			var deg:Number = FDeg2Deg(FlashDegree);
			return Deg2Rad(deg);
		}
		
		/**
		 * determines the distance between the two passed points
		 * @param x1 the x coordinate of the first point
		 * @param y1 the y coordinate of the first point
		 * @param x2 the x coordinate of the second point
		 * @param y2 the y coordinate of the second point
		 * @return the distance between the two points
		 */
		public static function FindDistanceByCoordinates(x1:Number, y1:Number, x2:Number, y2:Number):Number {
			return Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
		}
		
		/**
		 * determines the distance between the two passed points
		 * @param p1 the first point
		 * @param p2 the second point
		 * @return the distance between the two points
		 */
		public static function FindDistance(p1:Point, p2:Point):Number {
			return Math.sqrt((p2.x - p1.x) * (p2.x - p1.x) + (p2.y - p1.y) * (p2.y - p1.y));
		}
		
		/**
		 * determines the distance between the two passed points as arrays where index 0 is the x coordinate and index 1 is the y coordinate
		 * @param p1 the first point in array form [x, y]
		 * @param p2 the second point in array form [x, y]
		 * @return the distance between the two points
		 */
		public static function FindDistanceByPoints(p1:Array, p2:Array):Number {
			return Math.sqrt((p2[0] - p1[0]) * (p2[0] - p1[0]) + (p2[1] - p1[1]) * (p2[1] - p1[1]));
		}
		
		/**
		 * determines the midpoint between two points
		 * @param p1 the first point in array form [x, y]
		 * @param p2 the second point in array form [x, y]
		 * @return the midpoint of the line connecting the two points in array form [x, y]
		 */
		public static function FindMidPoint(p1:Array, p2:Array):Array {
			return [Number(p1[0] / 2 + p2[0] / 2), Number(p1[1] / 2 + p2[1] / 2)];
		}
		
		/**
		 * determines the Nth point between two points given the same distance between all Nth points.
		 * @param p1 the first point in array form [x, y] can also be a Point.
		 * @param p2 the second point in array form [x, y] can also be a Point.
		 * @param n is the Nth of M equi0distant point from p1 to p2. 
		 * @param m is the total number of Nth points to consider.
		 * @return the Nth point of the line connecting the two points in array form [x, y]
		 */
		public static function FindNthPoint(p1:*, p2:*, n:int, m:int):* {
			var response:* = [];
			try {
				var isPoint_p1:Boolean = (p1 is Point);
				var isPoint_p2:Boolean = (p2 is Point);
				var x1:Number = (isPoint_p1 ? p1.x : p1[0]);
				var x2:Number = (isPoint_p2 ? p2.x : p2[0]);
				var y1:Number = (isPoint_p1 ? p1.y : p1[1]);
				var y2:Number = (isPoint_p2 ? p2.y : p2[1]);
				var _p1:Point = new Point(x1,y1);
				var _p2:Point = new Point(x2,y2);
				var dist:Number = MathHelper.precision_to(Math2D.FindDistance(_p1, _p2),5);
				var dist1:Number = (dist / m) * n;
				do {
					var slope:Number = VectorUtils.calculateSlope(_p1, _p2);
					var y_intercept:Number = VectorUtils.solve_for_y_intercept(_p1,slope);
					var guess1:Point = VectorUtils.solve_for_x(slope, new Point(0,y1+dist1), y_intercept);
					var guess2:Point = VectorUtils.solve_for_y(guess1,slope,y_intercept);
					var distGuess1:Number = MathHelper.precision_to(Math2D.FindDistance(_p1, guess1),5);
					var distGuess2:Number = MathHelper.precision_to(Math2D.FindDistance(_p1, guess2),5);
					var x:Number;
					var y:Number;
					if (distGuess1 < distGuess2) {
						x = guess1.x;
						y = guess1.y;
					} else {
						x = guess2.x;
						y = guess2.y;
					}
					if ( (distGuess1 > dist) || (distGuess2 > dist) ) {
						dist1 = dist1 * 0.9;
						var ii:int = -1;
					}
				} while ( (distGuess1 > dist) || (distGuess2 > dist) );
				response = (isPoint_p1 && isPoint_p2) ? new Point(x,y) : [x,y];
			} catch (err:Error) {}
			return response;
		}
		
		/**
		 * Finds a relative point (returned as an array) based on polar coordinates
		 * @param angle the radian direction
		 * @param length the distance to travel in the direction
		 * @return a polar coordinate in array form [x, y]
		 */
		public static function Polar(angle:Number, length:Number):Array {
			var p2x:Number = length * Math.cos(angle);
			var p2y:Number = length * Math.sin(angle);
			return [p2x, p2y];
		}
		
		/**
		 * Finds an absolute point (returned as an array) based on polar coordinates and a relative point
		 * @param p1x the x coordinate of the origin point
		 * @param p1y the y coordinate of the origin point
		 * @param angle the radian direction
		 * @param length the distance to travel in the direction
		 * @return an offset polar coordinate in array form [x, y]
		 */
		public static function Polar2(p1x:Number, p1y:Number, angle:Number, length:Number):Array {
			var p2x:Number = p1x + length * Math.cos(angle);
			var p2y:Number = p1y + length * Math.sin(angle);
			return [p2x, p2y];
		}
		
		/**
		 * Finds a relative point (returned as a point) based on polar coordinates
		 * @param angle the radian direction
		 * @param length the distance to travel in the direction
		 * @return a polar coordinate in Point form
		 */
		public static function PolarPoint(angle:Number, length:Number):Point {
			var p2x:Number = length * Math.cos(angle);
			var p2y:Number = length * Math.sin(angle);
			return new Point(p2x, p2y);
		}
		
		/**
		 * Finds an absolute point (returned as a point) based on polar coordinates and a relative point
		 * @param p the origin point
		 * @param angle the radian direction
		 * @param length the distance to travel in the direction
		 * @return an offset polar coordinate in Point form
		 */
		public static function Polar2Point(p:Point, angle:Number, length:Number):Point {
			var p2x:Number = p.x + length * Math.cos(angle);
			var p2y:Number = p.y + length * Math.sin(angle);
			return new Point(p2x, p2y);
		}
		
		/**
		 * determines the angle from point p1 to point p2
		 * @param p1 the first point in array form [x, y]
		 * @param p2 the second point in array form [x, y]
		 * @return an angle in radians
		 */
		public static function GetAngleBetweenPoints(p1:Array, p2:Array):Number {
			return Math.atan2(p2[1] - p1[1], p2[0] - p1[0]);
		}
		
		/**
		 * determines the angle between the passed points
		 * @param x1 the x coordinate of the first point
		 * @param y1 the y coordinate of the first point
		 * @param x2 the x coordinate of the second point
		 * @param y2 the y coordinate of the second point
		 * @return an angle in radians
		 */
		public static function GetAngleBetweenCoordinates(x1:Number, y1:Number, x2:Number, y2:Number):Number {
			return Math.atan2(y2 - y1, x2 - x1);
		}
		
		/**
		 * determines the angle between the passed points
		 * @param p1 the first point
		 * @param p2 the second point
		 * @return an angle in radians
		 */
		public static function GetAngleBetweenVertices(p1:Point, p2:Point):Number {
			return Math.atan2(p2.y - p1.y, p2.x - p1.x);
		}
		
		/**
		 * given point p0, and list of points p, finds which point is closest and returns its index in the list
		 * @param p0 the point for reference in array form [x, y]
		 * @param p an array of points in array form [x, y]
		 * @return an integer index for array p
		 */
		public static function GetNearestPoint(p0:Array, p:Array):Number {
			var index:Number = -1;
			var distance:Number = Number.POSITIVE_INFINITY;
			
			for (var i:Number = 0; i < p.length; i++) {
				
				var distancetemp:Number = FindDistanceByPoints(p0, p[i]);
				
				if (distancetemp < distance) {
					distance = distancetemp;
					index = i;
				}
			}
			
			return index;
		}
		
		/**
		 * rotates a given point about the origin by rotation r
		 * <br>Unreliable, may in fact return incorrect point but used in special case.
		 * <br>In general, use RotateAboutOriginPositive instead
		 * @param x1 the x coordinate of the point
		 * @param y1 the y coordinate of the point
		 * @param r the angular rotation in radians
		 * @return a point in array form [x, y]
		 */
		public static function RotateAboutOrigin(x1:Number, y1:Number, r:Number):Array {
			//doesn't use above distance functions to increase speed
			var d:Number = Math.sqrt(x1 * x1 + y1 * y1);
			var ang:Number = Math.atan2(y1, x1);
			
			return [Number(-d * Math.cos(ang + r)), Number(-d * Math.sin(ang + r))];
		}
		
		/**
		 * rotates a given point about the origin by rotation r
		 * @param x1 the x coordinate of the point
		 * @param y1 the y coordinate of the point
		 * @param r the angular rotation in radians
		 * @return a point in array form [x, y]
		 */
		public static function RotateAboutOriginPositive(x1:Number, y1:Number, r:Number):Array {
			//doesn't use above distance functions to increase speed
			if (r == 0) {
				return [x1, y1];
			}
			
			var d:Number = Math.sqrt(x1 * x1 + y1 * y1);
			var ang:Number = Math.atan2(y1, x1);
			
			return [Number(d * Math.cos(ang + r)), Number(d * Math.sin(ang + r))];
		}
		/**
		 * rotates a given point about the origin by rotation r
		 * @param x1 the x coordinate of the point
		 * @param y1 the y coordinate of the point
		 * @param r the angular rotation in radians
		 * @return a point
		 */
		public static function RotateAboutOriginPositivePoint(x1:Number, y1:Number, r:Number):Point {
			//doesn't use above distance functions to increase speed
			if (r == 0) {
				return new Point(x1, y1);
			}
			
			var d:Number = Math.sqrt(x1 * x1 + y1 * y1);
			var ang:Number = Math.atan2(y1, x1);
			
			return new Point(Number(d * Math.cos(ang + r)), Number(d * Math.sin(ang + r)));
		}
		/**
		 * rotates a given point about an arbitrary point "origin" by rotation "rotation"
		 * @param point the point to rotate
		 * @param origin the centre of rotation
		 * @param rotation the angular rotation in radians
		 * @return a point
		 */
		public static function RotateAboutPoint(point:Point, origin:Point, rotation:Number):Point {
			//doesn't use above distance functions to increase speed
			if (rotation == 0) {
				return new Point(point.x, point.y);
			}
			
			var d:Number = Math.sqrt((origin.x - point.x) * (origin.x - point.x) + (origin.y - point.y) * (origin.y - point.y));
			var ang:Number = Math.atan2((point.y - origin.y), (point.x - origin.x));
			
			
			return new Point(origin.x + Number(d * Math.cos(ang + rotation)), origin.y + Number(d * Math.sin(ang + rotation)));
		}
		
		
		/**
		 * Finds the intersection of two lines defined in point-slope form
		 * @param point1 a point on the first line
		 * @param slope1 the slope of the first line
		 * @param point2 a point on the second line
		 * @param slope2 the slope of the second line
		 * @return the intersection point, or null if the lines are parallel
		 */
		public static function FindIntersection(point1:Point, slope1:Number, point2:Point, slope2:Number):Point {
			
			if (Math.abs(slope1 - slope2) < 0.0001 || (Math.abs(slope1) > 1000000 && Math.abs(slope2) > 1000000)) {
				//parallel
				return null;
			}
			
			var x1:Number = point1.x;
			var y1:Number = point1.y;
			var x2:Number = point2.x;
			var y2:Number = point2.y;
			var x0:Number;
			var y0:Number;
			var p0:Point;
			
			//due to round-off errors, horizontal/vertical lines will not always return slopes of 0/undefined.
			//Any slopes less than / greater than these limits can safely be considered as horizontal/vertical
			if (Math.abs(slope1) > 1000000) {
				x0 = x1;
				y0 = slope2 * (x0 - x2) + y2;
			} else if (Math.abs(slope2) > 1000000) {
				x0 = x2;
				y0 = slope1 * (x0 - x1) + y1;
			} else if (Math.abs(slope1) < 0.0001) {
				y0 = y1;
				x0 = ((y0 - y2) / (slope2)) + x2;
			} else if (Math.abs(slope2) < 0.0001) {
				y0 = y2;
				x0 = ((y0 - y1) / (slope1)) + x1;
			} else {
				x0 = (-slope2 * x2 + y2 + slope1 * x1 - y1) / (slope1 - slope2);
				y0 = slope1 * x0 - slope1 * x1 + y1;
			}
			
			p0 = new Point(x0, y0);
			return p0;
		}
		
		/**
		 * Finds the intersection of two lines defined in point-slope form where a radian angle is passed instead of slope
		 * @param point1 a point on the first line
		 * @param rotation1 angular rotation in radians of the first line
		 * @param point2 a point on the second line
		 * @param rotation2 angular rotation in radians of the second line
		 * @return the intersection point, or null if the lines are parallel
		 */
		public static function FindIntersectionByRotation(point1:Point, rotation1:Number, point2:Point, rotation2:Number):Point {
			return Math2D.FindIntersection(point1, Math.tan(rotation1), point2, Math.tan(rotation2));
		}
		
		/**
		 * Finds the intersection of two line segments defined in point-point form.
		 * @param p1 the start point of the first line
		 * @param p2 the end point of the first line
		 * @param p3 the start point of the second line
		 * @param p4 the end point of the second line
		 * @return Returns an object with the following properties:
		 * <br>type (string): the intersection type [coincident, parallel, intersecting, not intersecting]
		 * <br>intersecting (boolean): whether or not the lines intersect [true, false]
		 * <br>point (flash.geom.Point): if the lines intersect (and not coincident) then this is their point of intersection
		 * <br>ua: if intersecting, also returns this significant number used in other algorithms to test for alignment
		 * <br>ub: if intersecting, also returns this significant number used in other algorithms to test for alignment
		 */
		public static function FindSegmentIntersection(p1:Point, p2:Point, p3:Point, p4:Point):Object {
			var denom:Number = (p4.y - p3.y) * (p2.x - p1.x) - (p4.x - p3.x) * (p2.y - p1.y);
			var numua:Number = (p4.x - p3.x) * (p1.y - p3.y) - (p4.y - p3.y) * (p1.x - p3.x);
			var numub:Number = (p2.x - p1.x) * (p1.y - p3.y) - (p2.y - p1.y) * (p1.x - p3.x);
			
			//uses approximations due to round-off error & significant digit tolerances
			if (Math.abs(denom) < 0.001) {
				if (Math.abs(numua) < 0.001 && Math.abs(numub) < 0.001) {
					//coincident;
					return {type:"coincident", intersecting:true, point:null};
				}
				
				//parallel;
				return {type:"parallel", intersecting:false, point:null};
			}
			
			var ua:Number = numua / denom;
			var ub:Number = numub / denom;
			if (ua >= 0 && ua <= 1 && ub >= 0 && ub <= 1) {
				var ix:Number = p1.x + ua * (p2.x - p1.x);
				var iy:Number = p1.y + ua * (p2.y - p1.y);
				
				//intersecting
				return {type:"intersecting", intersecting:true, point:new Point(ix, iy), ua:ua, ub:ub};
			}
			
			//not intersecting
			return {type:"not intersecting", intersecting:false, point:null};
		}
		
		/**
		 * Finds the distance between two parallel lines.
		 * @param p1 a point on line 1
		 * @param p2 a point on line 2
		 * @param rotation the angular rotation of the lines
		 * @return the distance between them
		 */
		public static function FindDistanceBetweenParallelLines(p1:Point, p2:Point, rotation:Number):Number {
			
			var intersection:Point = FindIntersectionByRotation(p1, rotation, p2, rotation + Math.PI / 2);
			
			if (intersection == null) {
				//failure?
				return 0;
			} else {
				//distance 0 means coincident
				return Point.distance(p2, intersection);
			}
		}
		
		/**
		 * Reduces a radian angle to an equivilent one between 0 and 2pi
		 * @param radian an angle in radians
		 * @return a radian angle between 0 and 2pi (~6.283)
		 */
		public static function ReduceRadian(radian:Number):Number {
			
			if (isNaN(radian)) {
				trace("ReduceRadian NULL/isNaN");
				return 0;
			}
			
			var IsNegative:Boolean = radian < 0;
			radian = Math.abs(radian);
			
			while (radian >= Math.PI * 2) {
				radian -= Math.PI * 2;
			}
			
			if (IsNegative && radian != 0) {
				radian = Math.PI * 2 - radian;
			}
			
			return radian;
		}
		
		/**
		 * Determines if the two passed angles are parallel or perpendicular within a default tolerance
		 * @param angle1 the first angle in radians
		 * @param angle2 the second angle in radians
		 * @param tolerance the amount of acceptable tolerance (due to precision error), optional: default = 0.001
		 * @return true if the angles are parallel or perpendicular, false otherwise
		 */
		public static function AreAnglesOrthogonalOrParallel(angle1:Number, angle2:Number, tolerance:Number):Boolean {
			if (isNaN(tolerance)) {
				tolerance = 0.001;
			}
			
			var anglediff:Number = Math.abs(Math2D.ReduceRadian(Math2D.ReduceRadian(angle2) - Math2D.ReduceRadian(angle1)) % (Math.PI / 2));
			return ((anglediff < tolerance) || (Math.PI / 2 - anglediff < tolerance));
		}
		
		/**
		 * Determines if the two passed angles are perpendicular within a default tolerance
		 * @param angle1 the first angle in radians
		 * @param angle2 the second angle in radians
		 * @param tolerance the amount of acceptable tolerance (due to precision error), optional: default = 0.001
		 * @return true if the angles are perpendicular, false otherwise
		 */
		public static function AreAnglesOrthogonal(angle1:Number, angle2:Number, tolerance:Number):Boolean {
			if (isNaN(tolerance)) {
				tolerance = 0.001;
			}
			
			var anglediff:Number = Math2D.ReduceRadian(Math2D.GetDifferenceBetweenAngles(angle1, angle2));
			return ((Math.abs(Math.PI / 2 - anglediff) < tolerance) || (Math.abs(Math.PI * (3 / 2) - anglediff) < tolerance));
		}
		
		/**
		 * Determines if the two passed angles are parallel within a default tolerance
		 * @param angle1 the first angle in radians
		 * @param angle2 the second angle in radians
		 * @param tolerance the amount of acceptable tolerance (due to precision error), optional: default = 0.001
		 * @return true if the angles are parallel, false otherwise
		 */
		public static function AreAnglesParallel(angle1:Number, angle2:Number, tolerance:Number):Boolean {
			if (isNaN(tolerance)) {
				tolerance = 0.001;
			}
			
			var anglediff:Number = Math2D.ReduceRadian(Math2D.GetDifferenceBetweenAngles(angle1, angle2));
			return ( (Math.abs(anglediff) < tolerance) || (Math.abs(Math.PI - anglediff) < tolerance) || (Math.abs(Math.PI * 2 - anglediff) < tolerance) );
		}
		
		/**
		 * Determines if the given angle is vertical or horizontal within a default tolerance
		 * @param angle the angle in radians
		 * @return true if the angle is horizontal or vertical, false otherwise
		 */
		public static function IsAngleHorizontalOrVertical(angle:Number):Boolean {
			return (Math2D.IsAngleHorizontal(angle) || Math2D.IsAngleVertical(angle));
		}
		
		/**
		 * Determines if the given angle is horizontal within a default tolerance
		 * @param angle the angle in radians
		 * @return true if the angle is horizontal, false otherwise
		 */
		public static function IsAngleHorizontal(angle:Number):Boolean {
			angle = Math2D.ReduceRadian(angle);
			return ((Math.abs(angle - Math.PI) < 0.001) || (Math.abs(angle - Math.PI * 2) < 0.001) || (Math.abs(angle - 0) < 0.001));
		}
		
		/**
		 * Determines if the given angle is vertical within a default tolerance
		 * @param angle the angle in radians
		 * @return true if the angle is vertical, false otherwise
		 */
		public static function IsAngleVertical(angle:Number):Boolean {
			angle = Math2D.ReduceRadian(angle);
			return (!((Math.abs(angle - Math.PI) < 0.001) || (Math.abs(angle - Math.PI * 2) < 0.001) || (Math.abs(angle - 0) < 0.001)) && ((Math.abs(angle - Math.PI / 2) < 0.001) || (Math.abs(angle - Math.PI * 3 / 2) < 0.001)));
		}
		
		/**
		 * returns the difference between the two passed angles
		 * @param r1 the first angle in radians
		 * @param r2 the second angle in radians
		 * @return the radian difference between both angles
		 */
		public static function GetDifferenceBetweenAngles(r1:Number, r2:Number):Number {
			r1 = Math2D.ReduceRadian(r1);
			r2 = Math2D.ReduceRadian(r2);
			
			var diff:Number = Math2D.ReduceRadian(r2 - r1);
			if (diff > Math.PI) {
				diff = Math.PI * 2 - diff;
			}
			
			return diff;
		}
		
		/**
		 * determines if the passed point "p" lies on the line segment defined by the points "lineP1", "lineP2"
		 * @param p the Point to check
		 * @param lineP1 the start point of the line
		 * @param lineP2 the end point of the line
		 * @return true if the line is on the line segment, false otherwise
		 */
		public static function PointLiesOnLineSegment(p:Point, lineP1:Point, lineP2:Point):Boolean {
			
			var angle:Number = Math2D.GetAngleBetweenVertices(lineP1, lineP2);
			
			if (Math.abs(Math2D.GetAngleBetweenVertices(lineP1, p) - angle) < 0.001) { //make sure all three points are collinear && p is in the same direction from lineP1 as lineP2 is.
				if (Math2D.FindDistance(lineP1, p) <= Math2D.FindDistance(lineP1, lineP2)) { // determines if p is between lineP1 & lineP2 as opposed to past lineP2
					return true;
				}
			}
			
			return false;
		}
		
		/**
		 * Finds the distance between a given point "p" and the line "lineP1", "lineP2" along the line's normal
		 * @param p the Point to check
		 * @param lineP1 the start point of the line
		 * @param lineP2 the end point of the line
		 * @return the distance between the point and the line
		 */
		public static function FindDistanceBetweenPointAndLine(p:Point, lineP1:Point, lineP2:Point):Number {
			var angle:Number = Math2D.GetAngleBetweenVertices(lineP1, lineP2);
			var intersection:Point = Math2D.FindIntersectionByRotation(p, angle + Math.PI/2, lineP1, angle);
			return Math2D.FindDistance(p, intersection);
		}
		
		// http://blog.yoz.sk/2010/11/4-000-000-rectangle-collisions-per-second/

		public static function calcA(x1:Number, y1:Number, x2:Number, y2:Number):Number {
			return (y1 - y2) / (x1 - x2);
		}
		
		public static function projectX( boundary1X:Number, boundary1Y:Number, boundary2X:Number, boundary2Y:Number, pointX:Number, pointY:Number):Number {
			if(boundary1X == boundary2X)
				return boundary1X;
			if(boundary1Y == boundary2Y)
				return pointX;
			var a:Number = calcA(boundary1X, boundary1Y, boundary2X, boundary2Y);
			return (pointY - boundary2Y + boundary2X * a + pointX / a) / (a + 1 / a);
		}
		
		public static function projectY( boundary1X:Number, boundary1Y:Number, boundary2X:Number, boundary2Y:Number, pointX:Number, pointY:Number):Number {
			if(boundary1X == boundary2X)
				return pointY;
			if(boundary1Y == boundary2Y)
				return boundary1Y;
			var a:Number = calcA(boundary1X, boundary1Y, boundary2X, boundary2Y);
			var x:Number = projectX(boundary1X, boundary1Y, boundary2X, boundary2Y, pointX, pointY)
			return pointY + (pointX - x) / a;
		}
		
		public static function isUnderBoundaries( boundary1X:Number, boundary1Y:Number, boundary2X:Number, boundary2Y:Number, projectedX:Number, projectedY:Number):Boolean {
			if(boundary1X == boundary2X)
				return projectedY <= (boundary1Y > boundary2Y ? boundary1Y : boundary2Y);
			return projectedX <= (boundary1X > boundary2X ? boundary1X : boundary2X);
		}
		
		public static function isOverBoundaries( boundary1X:Number, boundary1Y:Number, boundary2X:Number, boundary2Y:Number, projectedX:Number, projectedY:Number):Boolean {
			if(boundary1X == boundary2X)
				return projectedY >= (boundary1Y < boundary2Y ? boundary1Y : boundary2Y);
			return projectedX >= (boundary1X < boundary2X ? boundary1X : boundary2X);
		}
		
		public static function isProjectedUnderBoundaries( boundary1X:Number, boundary1Y:Number, boundary2X:Number, boundary2Y:Number, pointX:Number, pointY:Number):Boolean {
			var x:Number = projectX(boundary1X, boundary1Y, boundary2X, boundary2Y, pointX, pointY);
			var y:Number = projectY(boundary1X, boundary1Y, boundary2X, boundary2Y, pointX, pointY);
			return isUnderBoundaries(boundary1X, boundary1Y, boundary2X, boundary2Y, x, y);
		}
		
		public static function isProjectedOverBoundaries( boundary1X:Number, boundary1Y:Number, boundary2X:Number, boundary2Y:Number, pointX:Number, pointY:Number):Boolean {
			var x:Number = projectX(boundary1X, boundary1Y, boundary2X, boundary2Y, pointX, pointY);
			var y:Number = projectY(boundary1X, boundary1Y, boundary2X, boundary2Y, pointX, pointY);
			return isOverBoundaries(boundary1X, boundary1Y, boundary2X, boundary2Y, x, y);
		}
		
		public static function isAxisCollision( boundary1X:Number, boundary1Y:Number, boundary2X:Number, boundary2Y:Number, projected1X:Number, projected1Y:Number, projected2X:Number, projected2Y:Number, projected3X:Number, projected3Y:Number, projected4X:Number, projected4Y:Number):Boolean {
			return hasOneUnderBoundaries(boundary1X, boundary1Y,
				boundary2X, boundary2Y,
				projected1X, projected1Y,
				projected2X, projected2Y,
				projected3X, projected3Y,
				projected4X, projected4Y) &&
					hasOneOverBoundaries(boundary1X, boundary1Y,
						boundary2X, boundary2Y,
						projected1X, projected1Y,
						projected2X, projected2Y,
						projected3X, projected3Y,
						projected4X, projected4Y);
		}
		
		public static function isProjectedAxisCollision( boundary1X:Number, boundary1Y:Number, boundary2X:Number, boundary2Y:Number, point1X:Number, point1Y:Number, point2X:Number, point2Y:Number, point3X:Number, point3Y:Number, point4X:Number, point4Y:Number):Boolean {
			return isAxisCollision(boundary1X, boundary1Y, 
				boundary2X, boundary2Y, projectX(boundary1X, boundary1Y, boundary2X, boundary2Y, point1X, point1Y),
				projectY(boundary1X, boundary1Y, boundary2X, boundary2Y, point1X, point1Y), projectX(boundary1X, boundary1Y, boundary2X, boundary2Y, 
					point2X, point2Y), projectY(boundary1X, boundary1Y, boundary2X, boundary2Y, point2X, point2Y),
				projectX(boundary1X, boundary1Y, boundary2X, boundary2Y, point3X, point3Y), projectY(boundary1X, boundary1Y, boundary2X, boundary2Y, point3X, point3Y),
				projectX(boundary1X, boundary1Y, boundary2X, boundary2Y, point4X, point4Y),
				projectY(boundary1X, boundary1Y, boundary2X, boundary2Y, point4X, point4Y));
		}
		
		public static function hasOneUnderBoundaries( boundary1X:Number, boundary1Y:Number, boundary2X:Number, boundary2Y:Number, projected1X:Number, projected1Y:Number, projected2X:Number, projected2Y:Number, projected3X:Number, projected3Y:Number, projected4X:Number, projected4Y:Number):Boolean {
			if(isUnderBoundaries(boundary1X, boundary1Y, boundary2X, boundary2Y, projected1X, projected1Y))
				return true;
			if(isUnderBoundaries(boundary1X, boundary1Y, boundary2X, boundary2Y, projected2X, projected2Y))
				return true;
			if(isUnderBoundaries(boundary1X, boundary1Y, boundary2X, boundary2Y, projected3X, projected3Y))
				return true;
			if(isUnderBoundaries(boundary1X, boundary1Y, boundary2X, boundary2Y, projected4X, projected4Y))
				return true;
			return false;
		}
		
		public static function hasOneOverBoundaries(boundary1X:Number, boundary1Y:Number,boundary2X:Number, boundary2Y:Number,projected1X:Number, projected1Y:Number,projected2X:Number, projected2Y:Number,projected3X:Number, projected3Y:Number,projected4X:Number, projected4Y:Number):Boolean {
			if(isOverBoundaries(boundary1X, boundary1Y,boundary2X, boundary2Y, projected1X, projected1Y))
				return true;
			if(isOverBoundaries(boundary1X, boundary1Y, boundary2X, boundary2Y, projected2X, projected2Y))
				return true;
			if(isOverBoundaries(boundary1X, boundary1Y, boundary2X, boundary2Y, projected3X, projected3Y))
				return true;
			if(isOverBoundaries(boundary1X, boundary1Y,boundary2X, boundary2Y, projected4X, projected4Y))
				return true;
			return false;
		}
	}
}