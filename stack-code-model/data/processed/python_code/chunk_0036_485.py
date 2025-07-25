﻿/*
 * Scratch Project Editor and Player
 * Copyright (C) 2014 Massachusetts Institute of Technology
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 */

package svgeditor  {
	import flash.display.BitmapData;
	import flash.display.Graphics;
	import flash.display.Sprite;
	import flash.geom.Matrix;
	import flash.geom.Point;
	import flash.geom.Rectangle;

	public class DashDrawer {
		private static var lineBitmaps:Object = new Object();

		public function DashDrawer() {
			throw new Error("Static Class - Use the static methods!");
		}

		public static function drawBox(g:Graphics, rect:Rectangle, dashLength:int, dashColor:int):void {
			// Get the dash bitmap
			var bd:BitmapData = getDashBitmap(dashLength, dashColor);

			// Draw the horizontal walls
			g.beginBitmapFill(bd);
			g.moveTo(rect.left, rect.top);
			g.lineTo(rect.right, rect.top);
			g.lineTo(rect.right, rect.top + 1);
			g.lineTo(rect.left, rect.top + 1);
			g.endFill();

			g.beginBitmapFill(bd);
			g.moveTo(rect.left, rect.bottom);
			g.lineTo(rect.right, rect.bottom);
			g.lineTo(rect.right, rect.bottom + 1);
			g.lineTo(rect.left, rect.bottom + 1);
			g.endFill();

			// Draw the vertical walls
			var m:Matrix = new Matrix();
			m.rotate(Math.PI / 2);
			g.beginBitmapFill(bd, m);
			g.moveTo(rect.left, rect.top);
			g.lineTo(rect.left + 1, rect.top);
			g.lineTo(rect.left + 1, rect.bottom);
			g.lineTo(rect.left, rect.bottom);
			g.endFill();

			g.beginBitmapFill(bd, m);
			g.moveTo(rect.right, rect.top);
			g.lineTo(rect.right + 1, rect.top);
			g.lineTo(rect.right + 1, rect.bottom);
			g.lineTo(rect.right, rect.bottom);
			g.endFill();
		}

		public static function drawLine(g:Graphics, start:Point, end:Point, dashLength:int, dashColor:int):void {
			// Get the dash bitmap
			var bd:BitmapData = getDashBitmap(dashLength, dashColor);

			// Get the angle of the line so that we can adjust the bitmap rendering
			var m:Matrix = new Matrix();
			var p:Point = end.subtract(start);
			m.rotate(Math.atan2(p.y, p.x));
			p.x = 0; p.y = 1;
			p = m.transformPoint(p);

			// Draw the line
			g.beginBitmapFill(bd, m);
			//trace("g.moveTo("+start.x+", "+start.y+");");
			g.moveTo(start.x, start.y);
			//trace("g.lineTo("+end.x+", "+end.y+");");
			g.lineTo(end.x, end.y);
			g.lineTo(end.x + p.x, end.y + p.y);
			g.lineTo(start.x + p.x, start.y + p.y);
			g.endFill();
		}

		public static function drawPoly(g:Graphics, points:Array, dashLength:int, dashColor:int):void {
			// Get the dash bitmap
			var bd:BitmapData = getDashBitmap(dashLength, dashColor);

			// Get the angle of the line so that we can adjust the bitmap rendering
			for(var i:int = 0; i<points.length; ++i) {
				var start:Point = points[i];
				var end:Point;
				if(i < points.length - 1) {
					end = points[i + 1];
				} else {
					end = points[0];
				}

				drawLine(g, start, end, dashLength, dashColor);
			}
		}


		// Get a reference to the bitmap for a specified dash length
		public static function getDashBitmap(dashLength:int, dashColor:int):BitmapData {
			var key:String = dashLength + " " + dashColor;
			var bd:BitmapData = lineBitmaps[key];
			if(bd == null) {
				bd = lineBitmaps[key] = generateDashBitmap(dashLength, dashColor);
			}

			return bd;
		}

		// Creates a bitmap twice as long as the dash length for drawing dashed lines
		private static function generateDashBitmap(dashLength:int, dashColor:int):BitmapData {
			var c:Sprite = new Sprite();
			c.graphics.clear();
			c.graphics.lineStyle(2, dashColor, 1, true);
			c.graphics.moveTo(0, 0);
			c.graphics.lineTo(dashLength, 0);
			var bd:BitmapData = new BitmapData(dashLength * 2, 1, true, 0x00000000);
			bd.draw(c);
			return bd;
		}
	}
}