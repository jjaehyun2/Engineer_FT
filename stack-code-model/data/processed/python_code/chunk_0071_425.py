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

package com.utils.trigonometry 
{
	import flash.geom.Point;
	
	public function getCirclesBounceVector(pointA:Point, pointB:Point, radiusA:Number, radiusB:Number, vectorAX:Number, vectorAY:Number, vectorBX:Number, vectorBY:Number):Object
	{
		var nX1:Number = pointA.x;
		var nY1:Number = pointA.y;
		var nDistX:Number = pointB.x - nX1;
		var nDistY:Number = pointB.y - nY1;
		
		var nDistance:Number = Math.sqrt ( nDistX * nDistX + nDistY * nDistY );
		
		var nNormalX:Number = nDistX/nDistance;
		var nNormalY:Number = nDistY/nDistance;
		
		var nMidpointX:Number = ( nX1 + pointB.x )/2;
		var nMidpointY:Number = ( nY1 + pointB.y )/2;
		
		var nVector:Number = ( ( vectorAX - vectorBX ) * nNormalX )+ ( ( vectorAY - vectorBY ) * nNormalY );
		var nVelX:Number = nVector * nNormalX;
		var nVelY:Number = nVector * nNormalY;
		
		var circleA:Object = new Object();
		circleA.newX = nMidpointX - nNormalX * radiusA;
		circleA.newY = nMidpointY - nNormalY * radiusA;
		circleA.vectorX = vectorAX - nVelX;
		circleA.vectorY = vectorAY - nVelY;
		
		var circleB:Object = new Object();
		circleB.newX = nMidpointX + nNormalX * radiusB;
		circleB.newY = nMidpointY + nNormalY * radiusB;
		circleB.vectorX = vectorBX + nVelX;
		circleB.vectorY = vectorBY + nVelY;
		
		var oReturn:Object = new Object();
		oReturn.circleA = circleA;
		oReturn.circleB = circleB;
		
		return oReturn;
	}

}