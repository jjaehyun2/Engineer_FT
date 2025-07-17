package com.illuzor.circles.tools {
	
	import com.greensock.easing.*;
	import com.greensock.TweenLite;
	import com.illuzor.circles.constants.Colors;
	import com.illuzor.circles.constants.GameType;
	import com.illuzor.circles.constants.PointType;
	import com.illuzor.circles.interfaces.IController;
	import com.illuzor.circles.ui.Circle;
	import com.illuzor.circles.utils.intRandom;
	import flash.geom.Point;
	import starling.display.Sprite;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class ChallangeController extends ControllerBase implements IController {
		
		private var gameType:String;
		private var moves:Vector.<Function> = new  Vector.<Function>();
		private var circles:Vector.<Circle> = new Vector.<Circle>();
		private var easings:Array;
		private var speedAspect:Number = 1;
		private var sizeAspect:Number = 1;
		private var clockCounter:uint;
		
		public function ChallangeController(container:Sprite, circleSize:uint, gameType:String) {
			super(container, circleSize);
			this.gameType = gameType;
			makeEasings();
			makeCircles();
			makeMoves();
		}
		
		[Inline]
		private final function makeEasings():void {
			easings = [Linear.easeNone, Back.easeIn, Circ.easeIn, Circ.easeOut, 
			Cubic.easeIn, Cubic.easeOut,  Expo.easeOut,  Quad.easeIn, Quad.easeOut,
			Quart.easeIn, Quart.easeOut, Quint.easeIn, Quint.easeOut, 
			Sine.easeIn, Sine.easeOut];
		}
		
		[Inline]
		private final function makeMoves():void {
			moves.push(fromRightSide);
			moves.push(fromLeftSide);
			moves.push(fromLeftAndRigt);
			moves.push(fromRightAndLeft);
			moves.push(across);
			moves.push(clockwise);
			moves.push(counterClockwise);
		}
		
		[Inline]
		private final function makeCircles():void {
			for (var i:int = 0; i < 4; i++) {
				var circle:Circle = new Circle(circleSize, 0xFF0000)
				circles.push(circle);
				container.addChild(circle);
				circle.y = 100 * i;
			}
		}
		
		public function replay():void {
			speedAspect = 1;
			sizeAspect = 1;
			clockCounter = 0;
		}
		
		public function next():void {
			switch (gameType) {
				case GameType.TIME:
					if (speedAspect > .3) speedAspect -= .01;
				break;
				case GameType.SIZE:
					if (sizeAspect > .01) sizeAspect -= .0125;
				break;
				case GameType.COMPLETE:
					clockCounter = 0;
					if (speedAspect > .3) speedAspect -= .01;
					if (sizeAspect > .01) sizeAspect -= .0125;
				break;
			}
			stopMoving();
			moves[intRandom(0, moves.length - 1)]();
			changeColors();
		}
		
		public function getCorrectPoint(currentColor:uint):Point {
			for (var i:int = 0; i < circles.length; i++) {
				if (circles[i].color == currentColor) {
					return new Point(circles[i].x, circles[i].y);
				}
			}
			return new Point();
		}
		
		[Inline]
		private final function changeColors():void {
			var colors:Vector.<uint> = Colors.getColors(4);
			for (var i:int = 0; i < circles.length; i++) {
				circles[i].color = colors[i];
			}
		}
		
		public function getColor():uint {
			return circles[intRandom(0, circles.length - 1)].color;
		}
		
		public function pause():void {
			stopMoving();
		}
		
		private function fromRightSide():void {
			var animTime:Number = 1.8;
			animTime *= speedAspect;
			
			var endFunction:Function = fromRightSide;
			if(gameType == GameType.COMPLETE) {
				//changeColors();
				mixColors();
				endFunction = moves[intRandom(0, moves.length - 1)];
			}
			
			var ease:* = easing;
			
			circles[0].position = getPoint(PointType.RIGHT_TOP_ASIDE);
			TweenLite.to(circles[0], animTime, { x:getPoint(PointType.LEFT_TOP_ASIDE).x-circleSize * 2, y:getPoint(PointType.LEFT_TOP_ASIDE).y, ease:ease } );
			
			circles[1].position = getPoint(PointType.RIGHT_BOTTOM_ASIDE);
			TweenLite.to(circles[1], animTime, { x:getPoint(PointType.LEFT_BOTTOM_ASIDE).x-circleSize * 2, y:getPoint(PointType.LEFT_BOTTOM_ASIDE).y, ease:ease } );
			
			var secondPoint:Point = getPoint(PointType.RIGHT_TOP_ASIDE);
			secondPoint.x += circleSize * 2;
			circles[2].position = secondPoint
			TweenLite.to(circles[2], animTime, { x:getPoint(PointType.LEFT_TOP_ASIDE).x, y:getPoint(PointType.LEFT_TOP_ASIDE).y, ease:ease } );
			
			var thirdPoint:Point = getPoint(PointType.RIGHT_BOTTOM_ASIDE);
			thirdPoint.x += circleSize * 2;
			circles[3].position = thirdPoint;
			TweenLite.to(circles[3], animTime, { x:getPoint(PointType.LEFT_BOTTOM_ASIDE).x, y:getPoint(PointType.LEFT_BOTTOM_ASIDE).y, ease:ease, onComplete:endFunction } );
		}
		
		private function fromLeftSide():void {
			var animTime:Number = 1.8;
			animTime *= speedAspect;
			
			var endFunction:Function = fromLeftSide;
			if(gameType == GameType.COMPLETE) {
				//changeColors();
				mixColors();
				endFunction = moves[intRandom(0, moves.length - 1)];
			}
			
			var ease:* = easing;
			
			circles[0].position = getPoint(PointType.LEFT_TOP_ASIDE);
			TweenLite.to(circles[0], animTime, { x:getPoint(PointType.RIGHT_TOP_ASIDE).x+circleSize * 2, y:getPoint(PointType.RIGHT_TOP_ASIDE).y, ease:ease } );
			
			circles[1].position = getPoint(PointType.LEFT_BOTTOM_ASIDE);
			TweenLite.to(circles[1], animTime, { x:getPoint(PointType.RIGHT_BOTTOM_ASIDE).x+circleSize * 2, y:getPoint(PointType.RIGHT_BOTTOM_ASIDE).y, ease:ease } );
			
			var secondPoint:Point = getPoint(PointType.LEFT_TOP_ASIDE);
			secondPoint.x -= circleSize * 2;
			circles[2].position = secondPoint
			TweenLite.to(circles[2], animTime, { x:getPoint(PointType.RIGHT_TOP_ASIDE).x, y:getPoint(PointType.RIGHT_TOP_ASIDE).y, ease:ease } );
			
			var thirdPoint:Point = getPoint(PointType.LEFT_BOTTOM_ASIDE);
			thirdPoint.x -= circleSize * 2;
			circles[3].position = thirdPoint;
			TweenLite.to(circles[3], animTime, { x:getPoint(PointType.RIGHT_BOTTOM_ASIDE).x, y:getPoint(PointType.RIGHT_BOTTOM_ASIDE).y, ease:ease, onComplete:endFunction } );
		}
		
		private function fromLeftAndRigt():void {
			var animTime:Number = 1.8;
			animTime *= speedAspect;
			
			var endFunction:Function = fromLeftAndRigt;
			if(gameType == GameType.COMPLETE) {
				//changeColors();
				mixColors();
				endFunction = moves[intRandom(0, moves.length - 1)];
			}
			
			var ease:* = easing;
			
			circles[0].position = getPoint(PointType.LEFT_TOP_ASIDE);
			TweenLite.to(circles[0], animTime, { x:getPoint(PointType.RIGHT_TOP_ASIDE).x + circleSize * 2, y:getPoint(PointType.RIGHT_TOP_ASIDE).y, ease:ease } );
			
			var secondPoint:Point = getPoint(PointType.LEFT_TOP_ASIDE);
			secondPoint.x -= circleSize * 2;
			circles[2].position = secondPoint;
			TweenLite.to(circles[2], animTime, { x:getPoint(PointType.RIGHT_TOP_ASIDE).x, y:getPoint(PointType.RIGHT_TOP_ASIDE).y, ease:ease } );
			
			circles[1].position = getPoint(PointType.RIGHT_BOTTOM_ASIDE);
			TweenLite.to(circles[1], animTime, { x:getPoint(PointType.LEFT_BOTTOM_ASIDE).x - circleSize * 2, y:getPoint(PointType.LEFT_BOTTOM_ASIDE).y, ease:ease } );
			
			var thirdPoint:Point = getPoint(PointType.RIGHT_BOTTOM_ASIDE);
			thirdPoint.x += circleSize * 2;
			circles[3].position = thirdPoint;
			TweenLite.to(circles[3], animTime, { x:getPoint(PointType.LEFT_BOTTOM_ASIDE).x, y:getPoint(PointType.LEFT_BOTTOM_ASIDE).y, ease:ease, onComplete:endFunction } );
		}
		
		private function fromRightAndLeft():void {
			var animTime:Number = 1.8;
			animTime *= speedAspect;
			
			var endFunction:Function = fromRightAndLeft;
			if(gameType == GameType.COMPLETE) {
				//changeColors();
				mixColors();
				endFunction = moves[intRandom(0, moves.length - 1)];
			}
			
			var ease:* = easing;
			
			circles[0].position = getPoint(PointType.RIGHT_TOP_ASIDE);
			TweenLite.to(circles[0], animTime, { x:getPoint(PointType.LEFT_TOP_ASIDE).x - circleSize * 2, y:getPoint(PointType.LEFT_TOP_ASIDE).y, ease:ease } );
			
			var secondPoint:Point = getPoint(PointType.RIGHT_TOP_ASIDE);
			secondPoint.x += circleSize * 2;
			circles[2].position = secondPoint
			TweenLite.to(circles[2], animTime, { x:getPoint(PointType.LEFT_TOP_ASIDE).x, y:getPoint(PointType.LEFT_TOP_ASIDE).y, ease:ease } );
			
			circles[1].position = getPoint(PointType.LEFT_BOTTOM_ASIDE);
			TweenLite.to(circles[1], animTime, { x:getPoint(PointType.RIGHT_BOTTOM_ASIDE).x + circleSize * 2, y:getPoint(PointType.RIGHT_BOTTOM_ASIDE).y, ease:ease } );
			
			var thirdPoint:Point = getPoint(PointType.LEFT_BOTTOM_ASIDE);
			thirdPoint.x -= circleSize * 2;
			circles[3].position = thirdPoint;
			TweenLite.to(circles[3], animTime, { x:getPoint(PointType.RIGHT_BOTTOM_ASIDE).x, y:getPoint(PointType.RIGHT_BOTTOM_ASIDE).y, ease:ease, onComplete:endFunction } );
		}
		
		private function across():void {
			var animTime:Number = 1.2;
			animTime *= speedAspect;
			
			var endFunction:Function = across;
			if(gameType == GameType.COMPLETE) {
				//changeColors();
				mixColors();
				endFunction = moves[intRandom(0, moves.length - 1)];
			}
			
			var ease:* = easing;
			
			circles[0].position = getPoint(PointType.LEFT_TOP_ASIDE);
			TweenLite.to(circles[0], animTime, { x:getPoint(PointType.RIGHT_TOP_ASIDE).x, y:getPoint(PointType.RIGHT_TOP_ASIDE).y, ease:ease } );
			
			circles[1].position = getPoint(PointType.RIGHT_TOP_ASIDE);
			TweenLite.to(circles[1], animTime, { x:getPoint(PointType.LEFT_TOP_ASIDE).x, y:getPoint(PointType.LEFT_TOP_ASIDE).y, ease:ease } );
			
			circles[2].position = getPoint(PointType.LEFT_BOTTOM_ASIDE);
			TweenLite.to(circles[2], animTime, { x:getPoint(PointType.RIGHT_BOTTOM_ASIDE).x, y:getPoint(PointType.RIGHT_BOTTOM_ASIDE).y, ease:ease } );
			
			circles[3].position = getPoint(PointType.RIGHT_BOTTOM_ASIDE);
			TweenLite.to(circles[3], animTime, { x:getPoint(PointType.LEFT_BOTTOM_ASIDE).x, y:getPoint(PointType.LEFT_BOTTOM_ASIDE).y, ease:ease, onComplete:endFunction } );
		}
		
		private function clockwise():void {
			setSquare();
			moveClockWise();
		}
		
		private function moveClockWise():void {
			var animTime:Number = .6;
			animTime *= speedAspect;
			
			var endFunction:Function = moveClockWise;
			if(gameType == GameType.COMPLETE) {
				if (clockCounter < 3) {
					clockCounter++;
				} else {
					clockCounter = 0;
					mixColors();
					endFunction = moves[intRandom(0, moves.length - 1)];
				}
			}
			
			var ease:* = easing;
			
			var distance0:Point = getClockwiseNext(circles[0].position);
			TweenLite.to(circles[0], animTime, { x:distance0.x, y:distance0.y, ease:ease } );
			
			var distance1:Point = getClockwiseNext(circles[1].position);
			TweenLite.to(circles[1], animTime, { x:distance1.x, y:distance1.y, ease:ease } );
			
			var distance2:Point = getClockwiseNext(circles[2].position);
			TweenLite.to(circles[2], animTime, { x:distance2.x, y:distance2.y, ease:ease } );
			
			var distance3:Point = getClockwiseNext(circles[3].position);
			TweenLite.to(circles[3], animTime, { x:distance3.x, y:distance3.y, ease:ease, onComplete:endFunction } );
		}
		
		private function counterClockwise():void {
			setSquare();
			moveCounterClockWise();
		}
		
		private function moveCounterClockWise():void {
			var animTime:Number = .6;
			animTime *= speedAspect;
			
			var endFunction:Function = moveCounterClockWise;
			if(gameType == GameType.COMPLETE) {
				if (clockCounter < 3) {
					clockCounter++;
				} else {
					clockCounter = 0;
					mixColors();
					endFunction = moves[intRandom(0, moves.length - 1)];
				}
			}
			
			var ease:* = easing;
			
			var distance0:Point = getCounterclockwiseNext(circles[0].position);
			TweenLite.to(circles[0], animTime, { x:distance0.x, y:distance0.y, ease:ease } );
			
			var distance1:Point = getCounterclockwiseNext(circles[1].position);
			TweenLite.to(circles[1], animTime, { x:distance1.x, y:distance1.y, ease:ease } );
			
			var distance2:Point = getCounterclockwiseNext(circles[2].position);
			TweenLite.to(circles[2], animTime, { x:distance2.x, y:distance2.y, ease:ease } );
			
			var distance3:Point = getCounterclockwiseNext(circles[3].position);
			TweenLite.to(circles[3], animTime, { x:distance3.x, y:distance3.y, ease:ease, onComplete:endFunction } );
		}
		
		private function setSquare():void {
			for (var i:int = 0; i < 4; i++) {
				circles[i].alpha = 0;
				TweenLite.to(circles[i], .22, { alpha:1 } );
			}
			circles[0].position = getPoint(PointType.LEFT_TOP);
			circles[1].position = getPoint(PointType.RIGHT_TOP);
			circles[2].position = getPoint(PointType.RIGHT_BOTTOM);
			circles[3].position = getPoint(PointType.LEFT_BOTTOM);
		}
		
		private function mixColors():void {
			var newCircles:Vector.<Circle> = new Vector.<Circle>();
			
			while (circles.length) {
				var randomNumber:uint = intRandom(0, circles.length - 1);
				newCircles.push(circles[randomNumber]);
				circles.splice(randomNumber, 1);
			}
			circles = newCircles;
		}
		
		private function get easing():*{
			if (gameType == GameType.COMPLETE) {
				var random:uint = intRandom(0, easings.length - 1);
				return easings[random];
			}
			return Linear.easeNone;
		}
		
		public function getSizeAspect():Number {
			return sizeAspect;
		}
		
		[Inline]
		private final function stopMoving():void {
			TweenLite.killTweensOf(circles[0]);
			TweenLite.killTweensOf(circles[1]);
			TweenLite.killTweensOf(circles[2]);
			TweenLite.killTweensOf(circles[3]);
		}
		
		public function destroy():void {
			stopMoving();
		}
		
	}
}