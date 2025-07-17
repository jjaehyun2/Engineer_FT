/**
 *
 * Blackhole/Repulsor
 *
 * https://github.com/AbsolutRenal
 *
 * Copyright (c) 2012 AbsolutRenal (Renaud Cousin). All rights reserved.
 * 
 * This ActionScript source code is free.
 * You can redistribute and/or modify it in accordance with the
 * terms of the accompanying Simplified BSD License Agreement.
**/

package com.utils.trigonometry {
	import com.utils.angle.radToDeg;

	import flash.geom.Point;
	/**
	 * @author renaud.cousin
	 * @return Vector.Number => [0] : speed, [1] : orientation (in degrees)
	 * @param vect : moves vector
	 */
	public function convertVectorToAngleSpeed(moves:Point):Vector.<Number> {
//		var vect:Vector.<Number> = new Vector.<Number>();
//		
//		var speed:Number = Point.distance(new Point(), moves);
//		vect.push(speed);
//		
//		var p:Point = new Point(moves.x, 0);
//		var origin:Point = new Point();
//		var orientationRad:Number = Math.acos( Point.distance(origin, p) / Point.distance(origin, moves) );
//		var orientationDeg:Number = radToDeg(orientationRad);
//		
//		if(moves.x < 0 && moves.y < 0)
//			orientationDeg += 180;
//		else if(moves.x < 0 && moves.y > 0)
//			orientationDeg += 90;
//		else if(moves.x > 0 && moves.y < 0)
//			orientationDeg += 270;
//		
//		vect.push(orientationDeg);
//		
//		return vect;
		
		
		var vect:Vector.<Number> = new Vector.<Number>();
		
		var speed:Number = Point.distance(new Point(), moves);
		vect[0] = speed;
		
		var orientationRad:Number = Math.atan2(moves.y, moves.x);
		if (orientationRad < 0) {
			orientationRad += Math.PI * 2;
		}
		var orientationDeg:Number = radToDeg(orientationRad);
		vect[1] = orientationDeg;
		
		return vect;
	}
}