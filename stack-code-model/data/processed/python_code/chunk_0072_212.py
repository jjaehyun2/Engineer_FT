package com.illluzor.effect1 {
	
	import com.leapmotion.leap.events.LeapEvent;
	import com.leapmotion.leap.Finger;
	import com.leapmotion.leap.Frame;
	import com.leapmotion.leap.Gesture;
	import com.leapmotion.leap.Hand;
	import com.leapmotion.leap.KeyTapGesture;
	//import com.leapmotion.leap.LeapMotion;
	import com.leapmotion.leap.Vector3;
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.geom.Point;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	[SWF(backgroundColor="#000000",frameRate="60",width="1000",height="1000")]
	
	public class Main extends Sprite {
		
		private const CIRCLES_NUM:uint = 12;
		private const DRAW_DISTANCE:uint = 250;
		
		private var circlesList:Vector.<Object> = new Vector.<Object>();
		private var graphicsContainer:Shape;
		private var currentCircle:Object;
		//private var leap:LeapMotion;
		private var fingersNum:uint;
		private var whiteFillBegins:Boolean;
		
		public function Main():void {
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			
			createCircles();
			addElements();
			//initController();
			
			addEventListener(Event.ENTER_FRAME, onUpdate);
			stage.addEventListener(MouseEvent.MOUSE_DOWN, onMouseEvent);
			stage.addEventListener(MouseEvent.MOUSE_UP, onMouseEvent);
		}
		
		private function onMouseEvent(e:MouseEvent):void {
			if (e.type == MouseEvent.MOUSE_DOWN) {
				for (var i:int = 0; i < circlesList.length; i++) {
					if (mouseX > circlesList[i].x - 6 && mouseX < circlesList[i].x + 6 && mouseY > circlesList[i].y - 6 && mouseY < circlesList[i].y + 6) {
						currentCircle = circlesList[i];
						circlesList[i].dragged = true;
						break;
					}
				}
			} else {
				if (currentCircle) {
					currentCircle.dragged = false;
					currentCircle = null;
				}
			}
		}
		
		private function createCircles():void {
			for (var i:int = 0; i < CIRCLES_NUM+5; i++) {
				putCircle();
			}
		}
		
		private function putCircle(extra:Boolean = false, cX:uint = 0, cY:uint = 0):void {
			var circleObj:Object = {};
			circleObj.speed = Math.random() * 3 + .3;
			circleObj.directionX = Math.random() * randomBool();
			circleObj.directionY = Math.random() * randomBool();
			circleObj.dragged = false;
			if (extra) {
				circleObj.color = 0x3535FF;
				circleObj.x = cX;
				circleObj.y = cY;
				circlesList.unshift(circleObj);
			} else {
				circleObj.x = ((stage.stageWidth - 120) * Math.random()) + 60;
				circleObj.y = ((stage.stageHeight - 120) * Math.random()) + 60;
				circlesList.push(circleObj);
			}
		}
		
		private function addElements():void {
			graphicsContainer = new Shape();
			addChild(graphicsContainer);
		}
		
		private function onUpdate(e:Event):void {
			graphicsContainer.graphics.clear();
			move();
			
			for (var i:int = 0; i < circlesList.length - 1 - (5 - fingersNum); i++) {
				
				for (var j:int = 0; j < circlesList.length - (5 - fingersNum); j++) {
					if (i != j) {
						
						var point1:Point = new Point(circlesList[i].x, circlesList[i].y);
						var point2:Point = new Point(circlesList[j].x, circlesList[j].y);
						var distance:uint = Point.distance(point1, point2);
						
						if (distance < DRAW_DISTANCE && j > i) {
							graphicsContainer.graphics.lineStyle(3 * (1 - 0.005 * distance) + .2, 0xFFFFFF, 1 - 0.005 * distance);
							graphicsContainer.graphics.moveTo(circlesList[i].x, circlesList[i].y);
							graphicsContainer.graphics.lineTo(circlesList[j].x, circlesList[j].y);
						}
					}
				}
			}
		}
		
		private function move():void {
			graphicsContainer.graphics.beginFill(0xFFFFFF, 1);
			
			for (var i:int = 0; i < circlesList.length - (5 - fingersNum); i++) {
				
				if (circlesList[i].dragged) {
					currentCircle.x = mouseX;
					currentCircle.y = mouseY;
				} else {
					circlesList[i].x += circlesList[i].speed * circlesList[i].directionX;
					circlesList[i].y += circlesList[i].speed * circlesList[i].directionY;
				}
				
				if (circlesList[i].x <= 4) {
					circlesList[i].x = 5;
					circlesList[i].directionX = -circlesList[i].directionX;
				} else if (circlesList[i].x >= stage.stageWidth - 4) {
					circlesList[i].x = stage.stageWidth - 5;
					circlesList[i].directionX = -circlesList[i].directionX;
				}
				
				if (circlesList[i].y <= 4) {
					circlesList[i].y = 5;
					circlesList[i].directionY = -circlesList[i].directionY;
				} else if (circlesList[i].y >= stage.stageHeight - 4) {
					circlesList[i].y = stage.stageHeight - 5;
					circlesList[i].directionY = -circlesList[i].directionY;
				}

				if (i >= circlesList.length - 5) {
					graphicsContainer.graphics.beginFill(0xE80D12, 1);
				} else {
					if (circlesList[i].hasOwnProperty("color")) {
						graphicsContainer.graphics.beginFill(circlesList[i].color, 1);
					}
					else {
						if (!whiteFillBegins) {
							graphicsContainer.graphics.beginFill(0xFFFFFF, 1);
							whiteFillBegins = true;
						}
					}
				}
				graphicsContainer.graphics.drawCircle(circlesList[i].x, circlesList[i].y, 6);
			}
			whiteFillBegins = false;
			graphicsContainer.graphics.endFill();
		}
		
		private function randomBool():Number {
			if (Math.random() < 0.5) return -1;
			return 1;
		}
		
		/*private function initController():void {
			leap = new LeapMotion();
			leap.controller.addEventListener(LeapEvent.LEAPMOTION_CONNECTED, onLeapConnected);
		}
		
		private function onLeapUpdate(e:LeapEvent):void {
			var frame:Frame = e.frame;
			if (frame.hands.length > 0) {
				
				var hand:Hand = frame.hands[0];
				var fingers:Vector.<Finger> = hand.fingers;
				fingersNum = fingers.length;
				if (fingersNum > 5)
					fingersNum = 5;
				
				if (fingers.length > 0) {
					for (var i:int = 0; i < fingersNum; i++) {
						var startPos:Vector3 = e.frame.pointables[i].tipPosition;

						circlesList[circlesList.length - 5 + i].x = (startPos.x * 2) + stage.stageWidth / 2;
						circlesList[circlesList.length - 5 + i].y = (-startPos.y * 2) + (stage.stageWidth / 4 * 3);
					}
				}
			}

			var gestures:Vector.<Gesture> = e.frame.gestures();
			for each (var gesture:Gesture in gestures) {
				if (gesture is KeyTapGesture) {
					var tipPosition:Vector3 = gesture.frame.fingers[0].tipPosition;
					putCircle(true, (tipPosition.x*2)+ stage.stageWidth / 2, (-tipPosition.y * 2) + (stage.stageWidth / 4 * 3))
				}
			}
		}
		
		private function onLeapConnected(e:Event):void {
			leap.controller.enableGesture(Gesture.TYPE_KEY_TAP);
			leap.controller.addEventListener(LeapEvent.LEAPMOTION_FRAME, onLeapUpdate);
		}*/
	
	}
}