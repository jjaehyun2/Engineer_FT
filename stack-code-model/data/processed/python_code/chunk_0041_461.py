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
	import flash.display.Sprite;
	import flash.geom.Point;
	/**
	 * @author AbsolutRenal
	 */
	public function checkCirclesCollision(circle1:Sprite, circle2:Sprite):Boolean{
		return Point.distance(new Point(circle1.x, circle1.y), new Point(circle2.x, circle2.y)) <= (circle1.width + circle2.width) * .5;
	}
}