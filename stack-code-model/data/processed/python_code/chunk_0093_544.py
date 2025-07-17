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

package com.utils.vector {
	import flash.geom.Point;
	/**
	 * @author renaud.cousin
	 */
	public function getIndexFromPoint(p:Point, width:int):int {
		return p.x + (p.y * width);
	}
}