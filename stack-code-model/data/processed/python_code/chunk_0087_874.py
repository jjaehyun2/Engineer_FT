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

package com.absolut.geometry{
	import com.absolut.utils.middleFromPoints;
	import com.absolut.utils.calculateCircleTangentePointFromPoint;
	import com.absolut.datas.Config;
	import com.absolut.utils.calculateAngleFromCoef;
	import com.absolut.utils.calculateCirclesIntersections;
	import com.absolut.utils.calculateCoefFromPoints;
	import com.absolut.utils.calculateIntersectionsFromCircleCenter;
	import com.absolut.utils.calculateLinesIntersection;
	import com.absolut.utils.checkCirclesCollision;
	import com.absolut.utils.checkCirclesCollisionButNotIncluded;
	import com.absolut.utils.degToRad;
	import com.absolut.utils.drawLine;
	import com.absolut.utils.drawPoint;

	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import flash.text.TextField;
	import flash.text.TextFormat;

	
	[SWF(backgroundColor="#FFFFFF", frameRate="31", width="1280", height="1024")]
	public class Metaballs3 extends Sprite{
		private const RADIUS_MIN:int = 40;
		private const RADIUS_RANGE:int = 300;
		
		private var radiusAmount:int = 0;
		private var stageRect:Rectangle;
		private var circleContainer:Sprite;
		private var circle1:Sprite;
		private var circle2:Sprite;
		private var zone:Sprite;
		private var dragginItem:Sprite;
		private var lineContainer:Sprite;
		private var textDebugger:TextField;
		
		public function Metaballs3(){
			init();
			initDebug();
			active();
			
			dragginItem = circle1;
			render(null);
		}
		
		
		private function init():void{
			stageRect = new Rectangle(0, 0, stage.stageWidth, stage.stageHeight);
			
			circleContainer = new Sprite();
			addChild(circleContainer);
			
			var radius:int = RADIUS_MIN + Math.random() * RADIUS_RANGE;
			radiusAmount += radius;
			
			circle1 = new Sprite();
			zone = new Sprite();
			if(Config.SHOW_WORKING_LINES){
				circle1.graphics.lineStyle(1, 0);
				circle1.graphics.drawCircle(0, 0, radius);
				circle1.graphics.moveTo(0, -4);
				circle1.graphics.lineTo(0, 5);
				circle1.graphics.moveTo(-4, 0);
				circle1.graphics.lineTo(5, 0);
				zone.alpha = .1;
			}
			zone.graphics.beginFill(0x000000);
			zone.graphics.drawCircle(0, 0, radius);
			zone.graphics.endFill();
			circle1.addChild(zone);
			circle1.x = 350;
			circle1.y = 300;
			circleContainer.addChild(circle1);
			
			radius = RADIUS_MIN + Math.random() * RADIUS_RANGE;
			radiusAmount += radius;
						
			circle2 = new Sprite();
			zone = new Sprite();
			if(Config.SHOW_WORKING_LINES){
				circle2.graphics.lineStyle(1, 0);
				circle2.graphics.drawCircle(0, 0, radius);
				circle2.graphics.moveTo(0, -4);
				circle2.graphics.lineTo(0, 5);
				circle2.graphics.moveTo(-4, 0);
				circle2.graphics.lineTo(5, 0);
				zone.alpha = .1;
			}
			zone.graphics.beginFill(0x000000);
			zone.graphics.drawCircle(0, 0, radius);
			zone.graphics.endFill();
			circle2.addChild(zone);
			circle2.x = 900;
			circle2.y = 300;
			circleContainer.addChild(circle2);
		}
		
		private function initDebug():void{
			if(Config.SHOW_WORKING_LINES){
				lineContainer = new Sprite();
				lineContainer.mouseEnabled = false;
				addChild(lineContainer);
				
				var tf:TextFormat = new TextFormat();
				tf.size = 10;
				tf.leading = -5;
				
				textDebugger = new TextField();
				textDebugger.multiline = true;
				textDebugger.wordWrap = true;
				textDebugger.width = 400;
				textDebugger.height = stage.stageHeight;
				textDebugger.defaultTextFormat = tf;
				addChildAt(textDebugger, 0);
			}
		}
		
		private function debug(msg:String):void{
			if(Config.SHOW_WORKING_LINES){
				msg = msg.replace("[DEBUG]", "<font color='#FF0000'>[DEBUG]</font>");
				msg = msg.replace("[INFO]", "<font color='#00FF00'>[INFO]</font>");
				msg = msg.replace("[XXX]", "<font color='#0000FF'>[XXX]</font>");
				textDebugger.htmlText += "<br />" + msg;
				textDebugger.scrollV = textDebugger.numLines;
				if(textDebugger.numLines > 10){
					textDebugger.htmlText = textDebugger.htmlText.replace(textDebugger.getLineText(1), "");
				}
			}
		}
		
		private function active():void{
			circle1.mouseChildren = circle2.mouseChildren = false;
			circleContainer.buttonMode = true;
			circleContainer.addEventListener(MouseEvent.MOUSE_DOWN, startDraggin);
			stage.addEventListener(MouseEvent.MOUSE_UP, stopDraggin);
		}
		
		private function startDraggin(e:MouseEvent):void{
			dragginItem = e.target as Sprite;
			dragginItem.startDrag(false, stageRect);
			
			addEventListener(Event.ENTER_FRAME, render);
		}
		
		private function stopDraggin(e:MouseEvent):void{
			if(dragginItem){
				dragginItem.stopDrag();
				dragginItem = null;
			}
			
			removeEventListener(Event.ENTER_FRAME, render);
		}
		
		private function render(e:Event):void{
			graphics.clear();
			
			
			if(Config.SHOW_WORKING_LINES){
				if(checkCirclesCollision(circle1, circle2))
					dragginItem.alpha = .2;
				else
					dragginItem.alpha = 1;
			}
			
			// CENTER CIRCLE 1
			var center1:Point = new Point(circle1.x, circle1.y);
			
			// CENTER CIRCLE 2
			var center2:Point = new Point(circle2.x, circle2.y);
			
			// COEF DIRECTEUR CENTER1-CENTER2
			var centersCoef:Number = calculateCoefFromPoints(center1, center2);
//			debug("[DEBUG] CENTERS_COEF:" + centersCoef.toString());
			var angleCenters:Number = calculateAngleFromCoef(centersCoef, center1, center2);
//			var idx:int = 0;
			var idx:int = getRightID(circle1, circle2);
			var I1:Point = calculateIntersectionsFromCircleCenter(circle1, degToRad(angleCenters))[idx];
			var I2:Point = calculateIntersectionsFromCircleCenter(circle2, degToRad(angleCenters))[1 - idx];

			// COEF DIRECTEUR PERPENDICULAIRE CENTER1-CENTER2 => INTERSECTION1-INTERSECTION2
			var coefPerpendicular:Number = -1/centersCoef;
			
			// ANGLE INTERSECTION1-INTERSECTION2
			var angleDeg:Number = calculateAngleFromCoef(coefPerpendicular, center1, center2, true);
//			debug("[DEBUG] ANGLE PERPENDICULAIRE:" + angleDeg.toString());
			var angleRad:Number = degToRad(angleDeg);
			
			var intersection:Array = calculateIntersectionsFromCircleCenter(circle1, angleRad);
			var intersect1:Point = intersection[0] as Point;
			var intersect2:Point = intersection[1] as Point;
			intersection = calculateIntersectionsFromCircleCenter(circle2, angleRad);
			var intersect3:Point = intersection[0] as Point;
			var intersect4:Point = intersection[1] as Point;
			// FIRST STEP //
			
			var coef1:Number = calculateCoefFromPoints(intersect1, intersect3);
			var coef2:Number = calculateCoefFromPoints(intersect2, intersect4);
			var tangentesIntersections:Point = calculateLinesIntersection(intersect1, coef1, intersect2, coef2);
			
			// SECOND STEP //
			var circlesIntersect:Vector.<Point>;
			if(checkCirclesCollisionButNotIncluded(circle1, circle2)){
				circlesIntersect = calculateCirclesIntersections(circle1, circle2);
				var tangentes1:Vector.<Point> = calculateCircleTangentePointFromPoint(circle1, tangentesIntersections);
				var tangentes2:Vector.<Point> = calculateCircleTangentePointFromPoint(circle2, tangentesIntersections);
				
				var c1:Point = new Point(circle1.x, circle1.y);
				var curveUp1:Number = calculateAngleFromCoef(calculateCoefFromPoints(c1, circlesIntersect[0]), c1, circlesIntersect[0]);
				var curveRef1:Number = calculateAngleFromCoef(calculateCoefFromPoints(c1, I1), c1, I1);
				var angleCurve1:Number = curveRef1 - curveUp1;
//				trace("angleCurve1:", int(angleCurve1), "curveUp1:", int(curveUp1));
				var G1:Point;
				var G2:Point;

				//
				var c2:Point = new Point(circle2.x, circle2.y);
				var curveUp2:Number = calculateAngleFromCoef(calculateCoefFromPoints(c2, circlesIntersect[0]), c2, circlesIntersect[0]);
				var curveRef2:Number = calculateAngleFromCoef(calculateCoefFromPoints(c2, I2), c2, I2);
				var angleCurve2:Number = curveRef2 - curveUp2;
				var G3:Point;
				var G4:Point;
				
				if(c1.y == c2.y && c2.x < c1.x){
					G1 = new Point(c1.x + Math.cos(degToRad(curveUp1 - angleCurve1 - 180)) * (circle1.width * .5), c1.y + Math.sin(degToRad(curveUp1 - angleCurve1 - 180)) * (circle1.width * .5));
					G2 = new Point(c1.x + Math.cos(degToRad(curveRef1 + 2 * angleCurve1 - 180)) * (circle1.width * .5), c1.y + Math.sin(degToRad(curveRef1 + 2 * angleCurve1 - 180)) * (circle1.width * .5));
				} else {
					G1 = new Point(c1.x + Math.cos(degToRad(curveUp1 - angleCurve1)) * (circle1.width * .5), c1.y + Math.sin(degToRad(curveUp1 - angleCurve1)) * (circle1.width * .5));
					G2 = new Point(c1.x + Math.cos(degToRad(curveRef1 + 2 * angleCurve1)) * (circle1.width * .5), c1.y + Math.sin(degToRad(curveRef1 + 2 * angleCurve1)) * (circle1.width * .5));
				}
				//
				if(c1.y == c2.y && c2.x > c1.x){
					G3 = new Point(c2.x + Math.cos(degToRad(curveUp2 - angleCurve2 - 180)) * (circle2.width * .5), c2.y + Math.sin(degToRad(curveUp2 - angleCurve2 - 180)) * (circle2.width * .5));
					G4 = new Point(c2.x + Math.cos(degToRad(curveRef2 + 2 * angleCurve2 - 180)) * (circle2.width * .5), c2.y + Math.sin(degToRad(curveRef2 + 2 * angleCurve2 - 180)) * (circle2.width * .5));
				} else {
					G3 = new Point(c2.x + Math.cos(degToRad(curveUp2 - angleCurve2)) * (circle2.width * .5), c2.y + Math.sin(degToRad(curveUp2 - angleCurve2)) * (circle2.width * .5));
					G4 = new Point(c2.x + Math.cos(degToRad(curveRef2 + 2 * angleCurve2)) * (circle2.width * .5), c2.y + Math.sin(degToRad(curveRef2 + 2 * angleCurve2)) * (circle2.width * .5));
				}
				
				if(!Config.SHOW_WORKING_LINES){
					graphics.beginFill(0x000000);
				} else {
					graphics.beginFill(0xA00AA0, .2);
//					graphics.lineStyle(1, 0xA00AA0);
//					graphics.moveTo(tangentes1[0].x, tangentes1[0].y);
//					graphics.lineTo(tangentes2[0].x, tangentes2[0].y);
//					graphics.lineTo(tangentes2[1].x, tangentes2[1].y);
//					graphics.lineTo(tangentes1[1].x, tangentes1[1].y);
//					graphics.lineTo(tangentes1[0].x, tangentes1[0].y);
//					graphics.endFill();
				}
				if(Config.DRAW_CURVE){
					var P1:Point, P2:Point, P3:Point, P4:Point;
					
					var dist1:Number = Point.distance(G1, I1);
					var dist2:Number = Point.distance(tangentes1[0], I1);
					var dist3:Number = Point.distance(G3, I2);
					var dist4:Number = Point.distance(tangentes2[0], I2);
					
					if(dist2 >= dist1 && Point.distance(G1, tangentes1[0]) < Point.distance(G2, tangentes1[0])){
//					if(dist2 >= dist1){
						P1 = G1;
						P2 = G2;
					} else {
						P1 = tangentes1[0];
						P2 = tangentes1[1];
					}
					
					
					if(dist3 < dist4 && Point.distance(G3, tangentes2[0]) < Point.distance(G4, tangentes2[0])){
//					if(dist3 < dist4){
						P3 = G3;
						P4 = G4;
					} else {
						P3 = tangentes2[0];
						P4 = tangentes2[1];
					}
					
					
					var coefTmp1:Number = -1 / calculateCoefFromPoints(center1, P1);
					var coefTmp2:Number = -1 / calculateCoefFromPoints(center2, P3);
					var tmpIntersectP1:Point;
					
					var coefTmp3:Number = -1 / calculateCoefFromPoints(center2, P4);
					var coefTmp4:Number = -1 / calculateCoefFromPoints(center1, P2);
					var tmpIntersectP2:Point;
					
					
//					var except:Boolean = (dist1 >= dist2 && dist3 <= dist4) || (dist1 <= dist2 && dist3 >= dist4);
//					if(except){
//						tmpIntersectP1 = middleFromPoints(G1, G3);
//						tmpIntersectP2 = middleFromPoints(G2, G4);
//					} else {
						tmpIntersectP1 = calculateLinesIntersection(P1, coefTmp1, P3, coefTmp2);
						tmpIntersectP2 = calculateLinesIntersection(P4, coefTmp3, P2, coefTmp4);
//					}
					
					graphics.moveTo(P1.x, P1.y);
					graphics.curveTo(tmpIntersectP1.x, tmpIntersectP1.y, P3.x, P3.y);
					graphics.lineTo(P4.x, P4.y);
					graphics.curveTo(tmpIntersectP2.x, tmpIntersectP2.y, P2.x, P2.y);
					graphics.lineTo(P1.x, P1.y);
				} else {
					graphics.moveTo(tangentes1[0].x, tangentes1[0].y);
					graphics.lineTo(tangentes2[0].x, tangentes2[0].y);
					graphics.lineTo(tangentes2[1].x, tangentes2[1].y);
					graphics.lineTo(tangentes1[1].x, tangentes1[1].y);
					graphics.lineTo(tangentes1[0].x, tangentes1[0].y);
				}
				graphics.endFill();
			}
			
			
			// SECOND STEP //
			
			if(Config.SHOW_WORKING_LINES){
				lineContainer.graphics.clear();
				drawLine(lineContainer, center1, center2, 0x08FF80, 2, 3, false);
				//
				drawLine(lineContainer, intersect1, intersect2, 0x0000FF, 2, 3, true);
				drawLine(lineContainer, intersect3, intersect4, 0x0000FF, 2, 3, true);
				//
				drawLine(lineContainer, center1, I1, 0x0000FF, 2, 3, true);
				drawLine(lineContainer, center2, I2, 0x0000FF, 2, 3, true);
				//
				drawLine(lineContainer, intersect1, tangentesIntersections, 0xCA080A);
				drawLine(lineContainer, intersect2, tangentesIntersections, 0xCA080A);
				drawLine(lineContainer, intersect1, intersect3, 0xCA080A);
				drawLine(lineContainer, intersect2, intersect4, 0xCA080A);
				//
				drawPoint(lineContainer, tangentesIntersections, 3, 0x00AA00);
				lineContainer.graphics.lineStyle(1, 0x00AA00);
				lineContainer.graphics.drawCircle(tangentesIntersections.x + (center1.x - tangentesIntersections.x) * .5, tangentesIntersections.y + (center1.y - tangentesIntersections.y) * .5, Point.distance(center1, tangentesIntersections) * .5);
				
				if(circlesIntersect != null){
					drawPoint(lineContainer, circlesIntersect[0], 2, 0xFFAA00);
					drawPoint(lineContainer, circlesIntersect[1], 2, 0xFFAA00 << 16);
					//
					drawPoint(lineContainer, tangentes1[0], 8, 0xF3F003);
					drawPoint(lineContainer, tangentes1[1], 4, 0xF3F003 << 16);
					drawPoint(lineContainer, tangentes2[0], 4, 0xF3F003);
					drawPoint(lineContainer, tangentes2[1], 4, 0xF3F003 << 16);
					//
					drawPoint(lineContainer, G1, 8, 0xF81AA4);
					drawPoint(lineContainer, G2, 2, 0xF81AA4 << 16);
					drawPoint(lineContainer, G3, 2, 0xF81AA4);
					drawPoint(lineContainer, G4, 2, 0xF81AA4 << 16);
				}
				//
//				drawLine(lineContainer, intersect5, center1, 0xFF0000, 3, true);
//				drawLine(lineContainer, intersect6, center1, 0xFF0000, 3, true);
//				drawLine(lineContainer, intersect7, center2, 0xFF0000, 3, true);
//				drawLine(lineContainer, intersect8, center2, 0xFF0000, 3, true);
//				drawLine(lineContainer, intersect5, intersect7, 0xFF0000, 3, false);
//				drawLine(lineContainer, intersect6, intersect8, 0xFF0000, 3, false);
			}
		}
		
		private function getRightID(c1:Sprite, c2:Sprite):int{
			var idx:int = 0;
			if(c2.x < c1.x && c1.y == c2.y)
				idx = 1;
			
//			if((c1.x < c2.x && c1.y < c2.y) || (c1.x > c2.x && c1.y > c2.y))
//				idx = 0;
//			else if((c1.x > c2.x && c1.y < c2.y) || (c1.x < c2.x && c1.y > c2.y) || (c1.x == c2.x && c1.y > c2.y) )
//				idx = 1;
				
			return idx;
		}
	}
}