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
	public function calculateMetaballIntersections(ball1:Metaball, ball2:Metaball):Vector.<Point>{
		return calculateCirclesIntersectionsFromPointRadius(ball1.position, ball1.radius, ball2.position, ball2.radius);
	}
}