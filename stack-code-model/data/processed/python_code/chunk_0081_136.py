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

package test {
	import com.utils.trigonometry.convertVectorToAngleSpeed;
	import com.utils.trigonometry.convertAngleSpeedToVector;
	import flash.geom.Point;
	import com.utils.angle.degToRad;
	import com.greensock.TweenLite;
	import flash.events.Event;
	import flash.display.Sprite;

	/**
	 * @author renaud.cousin
	 */
	public class BallTest extends Sprite {
		public static const DESTROY:String = "destroy";
		public static const BALL_RADIUS:int = 3;
		
		private var _orientation:Number;
		private var _speedX:Number;
		private var _speedY:Number;
		
		private const SPEED:Number = 10;
		private const BALL_COLOR:uint = 0xCC0000;
		private const LINE_COLOR:uint = 0x0880CC;
		
		private var ball:Sprite;

		public function BallTest() {
			addEventListener(Event.ADDED_TO_STAGE, onAddedToStage);
		}
		
		
		//----------------------------------------------------------------------
		// E V E N T S
		//----------------------------------------------------------------------

		private function onAddedToStage(event:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, onAddedToStage);
			
			init();
		}

		private function onEnterFrame(event:Event):void {
			ball.x += SPEED * Math.cos(degToRad(orientation));
			ball.y += SPEED * Math.sin(degToRad(orientation));
			
			this.graphics.lineTo(ball.x, ball.y);
			
			if((ball.x + x) > stage.stageWidth
			|| (ball.x + x) < 0
			|| (ball.y + y) > stage.stageHeight
			|| (ball.y + y) < 0){
				removeEventListener(Event.ENTER_FRAME, onEnterFrame);
				TweenLite.to(this, .8, {alpha:0, onComplete:kill});
			}
		}
		
		
		//----------------------------------------------------------------------
		// P R I V A T E
		//----------------------------------------------------------------------

		private function init():void {
			orientation = (BallDirectionTest.LAUNCH_DIRECTION == "left")? 0 : (BallDirectionTest.LAUNCH_DIRECTION == "right")? 180 : (BallDirectionTest.LAUNCH_DIRECTION == "top")? 90 : -90 ;
			
			this.graphics.lineStyle(1, LINE_COLOR);
			this.graphics.moveTo(0, 0);
			
			ball = new Sprite();
			ball.graphics.beginFill(BALL_COLOR);
			ball.graphics.drawCircle(0, 0, BALL_RADIUS);
			ball.graphics.endFill();
			addChild(ball);
			
			addEventListener(Event.ENTER_FRAME, onEnterFrame);
		}
		
		private function kill():void{
			dispatchEvent(new Event(DESTROY));
		}
		
		
		//----------------------------------------------------------------------
		// P U B L I C
		//----------------------------------------------------------------------
		
		public function setVector(sx:Number, sy:Number):void{
			_speedX = sx;
			_speedY = sy;
			_orientation = convertVectorToAngleSpeed(new Point(_speedX, _speedY))[1];
		}
		
		
		//----------------------------------------------------------------------
		// G E T T E R / S E T T E R
		//----------------------------------------------------------------------
		
		public function get position():Point{
			return new Point(x + ball.x, y + ball.y);
		}

		public function get orientation():Number {
			return _orientation;
		}

		public function set orientation(value:Number):void {
			_orientation = value;
			
			var vect:Point = convertAngleSpeedToVector(SPEED, _orientation);
			_speedX = vect.x;
			_speedY = vect.y;
		}

		public function get speedX():Number {
			return _speedX;
		}

		public function get speedY():Number {
			return _speedY;
		}
	}
}