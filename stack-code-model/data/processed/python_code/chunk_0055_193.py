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
	import com.absolut.datas.Config;

	import flash.display.Sprite;
	import flash.geom.Point;
	/**
	 * @author AbsolutRenal
	 */
	public function drawLine(container:Sprite, p1:Point, p2:Point, color:uint, thickness:Number = 1, radius:int = 3, drawPoint:Boolean = false):void{
		if(Config.SHOW_WORKING_LINES){
			container.graphics.lineStyle(thickness, color);
			container.graphics.moveTo(p1.x, p1.y);
			container.graphics.lineTo(p2.x, p2.y);
			if(drawPoint){
				container.graphics.beginFill(color);
				container.graphics.drawCircle(p1.x, p1.y, radius);
				container.graphics.endFill();
				container.graphics.beginFill(color << 16);
				container.graphics.drawCircle(p2.x, p2.y, radius);
				container.graphics.endFill();
			}
		}
	}
}