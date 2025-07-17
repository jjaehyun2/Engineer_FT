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
	import com.utils.angle.degToRad;
	import flash.geom.Point;

	/**
	 * @author renaud.cousin
	 * @return speed and orientation as Vector (Point)
	 * @param speed : move speed (positive)
	 * @param orientation : move orientation (in degrees)
	 */
	public function convertAngleSpeedToVector(speed:Number, orientation:Number):Point {
		var orientationRad:Number = degToRad(orientation);
		var vect:Point = new Point();
		
		vect.x = speed * Math.cos(orientationRad);
		vect.y = speed * Math.sin(orientationRad);
		
		return vect;
	}
}