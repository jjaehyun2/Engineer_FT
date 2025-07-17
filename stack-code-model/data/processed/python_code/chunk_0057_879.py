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
	import flash.geom.Point;
	/**
	 * @author renaud.cousin
	 * @return new bullet vector (Point)
	 * @param p1 (Point) : bullet position
	 * @param moves (Point) : bullet moves vector
	 * @param p2 (Point) : backhole position
	 * @param effectRadius (uint) : blackhole effect radius
	 * @param gravity (uint) : the smaller the stronger, can't be neither equal to 0 nor negative
	 * @param repulse (Boolean) : does the backhole attract or repulse
	 */
	public function getGravityAffectedVector(p1:Point, moves:Point, p2:Point, effectRadius:uint, repulse:Boolean, gravity:uint):Point {
		var props:Vector.<Number> = convertVectorToAngleSpeed(moves);
		
		var speed:Number = props[0];
		var angleDeg:Number = props[1];
		
		var angleNew:Number = getGravityAffectedDirection(p1, angleDeg, p2, effectRadius, repulse, gravity);
		var newVect:Point = convertAngleSpeedToVector(speed, angleNew);
		
		return newVect;
	}
}