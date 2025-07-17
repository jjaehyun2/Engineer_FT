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
	public function drawPoint(container:Sprite, p:Point, radius:int, color:uint):void{
		container.graphics.beginFill(color);
		container.graphics.drawCircle(p.x, p.y, radius);
		container.graphics.endFill();
	}
}