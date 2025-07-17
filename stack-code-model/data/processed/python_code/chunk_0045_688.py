/**
 *
 * MetaBalls
 *
 * https://github.com/AbsolutRenal
 *
 * Copyright (c) 2012 AbsolutRenal (Renaud Cousin). All rights reserved.
 * 
 * This ActionScript source code is free.
 * You can redistribute and/or modify it in accordance with the
 * terms of the accompanying Simplified BSD License Agreement.
**/

package com.absolut.utils{
	import com.absolut.metaballs.Metaball;

	import flash.geom.Point;
	/**
	 * @author AbsolutRenal
	 */
	public function calculateMetaballTangentePointFromPoint(ball:Metaball, O:Point):Vector.<Point>{
		var p1:Point = ball.position;
		var p0:Point = new Point(O.x + (p1.x - O.x) * .5, O.y + (p1.y - O.y) * .5);
		var r0:Number = Point.distance(p1, O) * .5;
		var r1:Number = ball.radius;
		
		return calculateCirclesIntersectionsFromPointRadius(p0, r0, p1, r1);
	}
}